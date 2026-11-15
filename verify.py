#!/usr/bin/env python3
"""
Phase 4 verification: compare ZIP inventory vs repository (index + working tree) and validate
text sources, images, fonts, PDFs, 3D models, package files and asset paths.
Results are written to verification_results.json (consumed by the report generator).
"""
import os, re, io, sys, json, struct, hashlib, subprocess, collections

REPO = "/home/user/the-world-of-you"
EXTRACT = "/tmp/zip-extract/chronos"
INV = "/home/user/migration/inventory/zip_inventory.json"
OUT = "/home/user/migration/inventory/verification_results.json"
ZIPNAME = "The-World-of-You-17-Native-Worlds-Source.zip"

R = {}            # results
problems = []     # anything that is not OK
def check(name, ok, detail=""):
    print(("  [PASS] " if ok else "  [FAIL] ") + name + (f"  -> {detail}" if detail else ""))
    if not ok: problems.append(f"{name}: {detail}")
    return ok

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""): h.update(c)
    return h.hexdigest()

def git(*a):
    return subprocess.check_output(["git", *a], cwd=REPO).decode()

zip_inv = {e["path"]: e for e in json.load(open(INV))}

# ---------------------------------------------------------------- 1. inventory comparison
print("\n[1] ZIP inventory vs repository")
raw = git("ls-files", "-s", "-z").split("\0")
index = {}
for line in raw:
    if not line: continue
    meta, path = line.split("\t", 1)
    mode, blob, stage = meta.split()
    index[path] = (mode, blob)
R["index_entries"] = len(index)

missing, sha_mismatch, blob_mismatch, mode_odd = [], [], [], []
for path, e in zip_inv.items():
    if path not in index: missing.append(path); continue
    wt = os.path.join(REPO, path)
    if not os.path.isfile(wt): missing.append(path + " (not in worktree)"); continue
    if sha256(wt) != e["sha256"]: sha_mismatch.append(path)
    expect_blob = subprocess.check_output(["git", "hash-object", "--", os.path.join(EXTRACT, path)]).decode().strip()
    if index[path][1] != expect_blob: blob_mismatch.append(path)
    if index[path][0] != "100644": mode_odd.append((path, index[path][0]))
extra = sorted(set(index) - set(zip_inv))
R.update(zip_files=len(zip_inv), missing=missing, sha256_mismatch=sha_mismatch, blob_mismatch=blob_mismatch,
         extra_in_repo=extra, odd_modes=mode_odd)
check("every ZIP file is present in the git index", not missing, f"{len(zip_inv)-len(missing)}/{len(zip_inv)} present; missing={missing}")
check("sha256 of every repo file == sha256 of the ZIP file", not sha_mismatch, f"mismatches={sha_mismatch}")
check("git blob id of every staged file == git hash-object of the extracted ZIP file", not blob_mismatch, f"mismatches={blob_mismatch}")
check("all staged files are regular 100644 files (no symlinks / exec bits)", not mode_odd, str(mode_odd))
allowed_extra = sorted([ZIPNAME] + (["MIGRATION_REPORT.md"] if "MIGRATION_REPORT.md" in index else []))
check("only expected extra files in repo (preserved original ZIP + the migration report)", extra == allowed_extra, str(extra))
zip_wt = os.path.join(REPO, ZIPNAME)
pre = open("/home/user/migration/inventory/repo_pre_migration.txt").read()
check("preserved original ZIP in repo is byte-identical to pre-migration copy",
      sha256(zip_wt) in pre, sha256(zip_wt)[:16])
check("original ZIP in migration/original is still unmodified (sha256)",
      sha256("/home/user/migration/original/" + ZIPNAME) == open("/home/user/migration/ORIGINAL_ZIP.sha256").read().split()[0])
# blob in the index for the preserved zip equals GitHub's blob (5f9f1f5...)
check("preserved ZIP blob id equals the id GitHub reported (5f9f1f52b035...)", index[ZIPNAME][1].startswith("5f9f1f52b035"), index[ZIPNAME][1][:12])

# unexpected overwrites: compare pre-migration repo files
actions = json.load(open("/home/user/migration/inventory/migration_actions.json"))
overwritten = [a["path"] for a in actions["actions"] if a["action"].startswith("conflict")]
R["overwritten_existing_files"] = overwritten
check("only documented overwrite is README.md", overwritten == ["README.md"], str(overwritten))
nodemod = [p for p in index if p.startswith(("node_modules/", "dist/", ".git/")) or "/node_modules/" in p]
check("no node_modules / dist / .git content staged", not nodemod, str(nodemod[:5]))
secret_names = [p for p in index if re.search(r"(^|/)\.env|\.pem$|\.key$|\.p12$|id_rsa", p)]
check("no .env / key files staged", not secret_names, str(secret_names))

# ---------------------------------------------------------------- 2. text sources
print("\n[2] Text-based files")
TEXT_EXT = {".ts", ".tsx", ".js", ".mjs", ".cjs", ".css", ".html", ".md", ".json", ".txt", ".py"}
text_files = [p for p in zip_inv if os.path.splitext(p)[1].lower() in TEXT_EXT or os.path.basename(p) in (".gitignore", ".vercelignore", ".gitkeep")]
bad_utf8, has_nul, bom, crlf, empty = [], [], [], [], []
for p in text_files:
    b = open(os.path.join(REPO, p), "rb").read()
    if not b: empty.append(p); continue
    if b"\x00" in b: has_nul.append(p)
    if b.startswith(b"\xef\xbb\xbf"): bom.append(p)
    if b"\r\n" in b: crlf.append(p)
    try: b.decode("utf-8")
    except UnicodeDecodeError: bad_utf8.append(p)
R.update(text_files_checked=len(text_files), non_utf8=bad_utf8, nul_in_text=has_nul, bom=bom, crlf_files=crlf, empty_text_files=empty)
check(f"{len(text_files)} text files decode as strict UTF-8", not bad_utf8, str(bad_utf8))
check("no NUL bytes in text files", not has_nul, str(has_nul))
print("  [INFO] files using CRLF (preserved as-is):", crlf, "| BOM files:", bom, "| empty text files:", empty)
json_bad = []
for p in [p for p in zip_inv if p.endswith(".json")]:
    try: json.load(open(os.path.join(REPO, p), encoding="utf-8"))
    except Exception as ex: json_bad.append((p, str(ex)[:80]))
check(f"all {sum(1 for p in zip_inv if p.endswith('.json'))} .json files parse", not json_bad, str(json_bad))
py_bad = []
for p in [p for p in zip_inv if p.endswith(".py")]:
    try: compile(open(os.path.join(REPO, p), encoding="utf-8").read(), p, "exec")
    except SyntaxError as ex: py_bad.append((p, str(ex)))
check("python helper scripts compile", not py_bad, str(py_bad))
mjs_bad = []
for p in [p for p in zip_inv if p.endswith((".mjs",))] + ["vercel-upload/deploy-root/build-static.js"]:
    r = subprocess.run(["node", "--check", os.path.join(REPO, p)], capture_output=True, text=True)
    if r.returncode: mjs_bad.append((p, r.stderr.strip()[:150]))
check(f"node --check passes for all .mjs/.js helper scripts", not mjs_bad, str(mjs_bad))

# ---------------------------------------------------------------- 3. images
print("\n[3] Images (full decode with Pillow)")
from PIL import Image
img_ext = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".bmp", ".ico"}
imgs = [p for p in zip_inv if os.path.splitext(p)[1].lower() in img_ext]
img_bad, dims = [], {}
for p in imgs:
    try:
        with Image.open(os.path.join(REPO, p)) as im:
            im.verify()
        with Image.open(os.path.join(REPO, p)) as im:
            im.load(); dims[p] = (im.format, im.size[0], im.size[1], im.mode)
    except Exception as ex:
        img_bad.append((p, str(ex)[:100]))
fmt = collections.Counter(v[0] for v in dims.values())
R.update(images_checked=len(imgs), images_bad=img_bad, image_formats=dict(fmt))
check(f"all {len(imgs)} raster images decode fully", not img_bad, f"formats={dict(fmt)} bad={img_bad}")
gp = sorted(p for p in imgs if "gift-previews/" in p)
check("17 gift preview images present (gift-01..gift-17)", [os.path.basename(p) for p in gp] == [f"gift-{i:02d}.webp" for i in range(1, 18)], f"{len(gp)} found")
svg = [p for p in zip_inv if p.endswith(".svg")]
print("  [INFO] standalone .svg files in ZIP:", len(svg), "(the favicon is an inline data-URI SVG inside index.html)")

# ---------------------------------------------------------------- 4. fonts / pdf
print("\n[4] Fonts and PDFs")
font_bad = []
for p in [p for p in zip_inv if p.endswith(".woff2")]:
    b = open(os.path.join(REPO, p), "rb").read()
    sig, flavor, length = struct.unpack(">4sII", b[:12])
    if sig != b"wOF2" or length != len(b): font_bad.append((p, sig, length, len(b)))
check("6 WOFF2 fonts: valid 'wOF2' signature and declared length == file size", not font_bad, str(font_bad))
pdf_bad = []
for p in [p for p in zip_inv if p.endswith(".pdf")]:
    b = open(os.path.join(REPO, p), "rb").read()
    if not b.startswith(b"%PDF-") or b"%%EOF" not in b[-2048:]: pdf_bad.append(p)
check("PDFs have %PDF header and %%EOF trailer", not pdf_bad, str(pdf_bad))

# ---------------------------------------------------------------- 5. 3D models
print("\n[5] 3D models (GLB structural validation)")
glbs = sorted(p for p in zip_inv if p.lower().endswith((".glb", ".gltf")))
glb_report, glb_bad = {}, []
for p in glbs:
    b = open(os.path.join(REPO, p), "rb").read()
    try:
        magic, ver, total = struct.unpack("<4sII", b[:12])
        assert magic == b"glTF", "bad magic"
        assert ver == 2, f"version {ver}"
        assert total == len(b), f"header length {total} != file size {len(b)}"
        off, chunks = 12, []
        while off < len(b):
            clen, ctype = struct.unpack("<I4s", b[off:off + 8])
            chunks.append((ctype, b[off + 8: off + 8 + clen])); off += 8 + clen
        assert off == len(b), "chunk walk did not end at EOF"
        assert chunks[0][0] == b"JSON", "first chunk not JSON"
        j = json.loads(chunks[0][1].decode("utf-8").rstrip(" \x00"))
        binlen = len(chunks[1][1]) if len(chunks) > 1 and chunks[1][0].startswith(b"BIN") else 0
        assert j["asset"]["version"] == "2.0", "asset.version != 2.0"
        ext_uris = [x.get("uri") for k in ("buffers", "images") for x in j.get(k, []) if x.get("uri") and not x["uri"].startswith("data:")]
        assert not ext_uris, f"external URIs (would break): {ext_uris}"
        for bv in j.get("bufferViews", []):
            assert bv["byteOffset"] + bv["byteLength"] <= binlen if "byteOffset" in bv else bv["byteLength"] <= binlen, "bufferView exceeds BIN chunk"
        for a in j.get("accessors", []):
            assert "bufferView" not in a or a["bufferView"] < len(j["bufferViews"]), "accessor -> bad bufferView"
        for m in j.get("meshes", []):
            for pr in m["primitives"]:
                for att in pr["attributes"].values(): assert att < len(j["accessors"]), "primitive -> bad accessor"
        glb_report[p] = dict(bytes=len(b), generator=j["asset"].get("generator"), scenes=len(j.get("scenes", [])), nodes=len(j.get("nodes", [])),
                             meshes=len(j.get("meshes", [])), materials=len(j.get("materials", [])), textures=len(j.get("textures", [])),
                             images=len(j.get("images", [])), animations=len(j.get("animations", [])), accessors=len(j.get("accessors", [])),
                             bin_bytes=binlen, extensions=j.get("extensionsUsed", []))
    except Exception as ex:
        glb_bad.append((p, repr(ex)[:160]))
R.update(glb_files=len(glbs), glb_bad=glb_bad, glb_report=glb_report)
check(f"all {len(glbs)} GLB models: valid glTF 2.0 container, length, chunks, JSON, buffer ranges, no external refs", not glb_bad, str(glb_bad))
for p, r in glb_report.items():
    print(f"     {p.split('/')[-1]:<20} {r['bytes']:>9,} B  meshes={r['meshes']:<3} materials={r['materials']:<3} textures={r['textures']:<2} images={r['images']:<2} nodes={r['nodes']:<4} gen={r['generator']}")

# ---------------------------------------------------------------- 6. package files
print("\n[6] package.json / lockfile")
pkg = json.load(open(os.path.join(REPO, "package.json")))
lock = json.load(open(os.path.join(REPO, "package-lock.json")))
root = lock["packages"][""]
check("lockfileVersion present", "lockfileVersion" in lock, f"v{lock.get('lockfileVersion')}")
check("lock name/version match package.json", lock["name"] == pkg["name"] and lock["version"] == pkg["version"], f"{lock['name']}@{lock['version']}")
for sect in ("dependencies", "devDependencies"):
    check(f"lock root '{sect}' == package.json '{sect}'", root.get(sect, {}) == pkg.get(sect, {}))
missing_pkgs = [d for d in {**pkg["dependencies"], **pkg["devDependencies"]} if f"node_modules/{d}" not in lock["packages"]]
check("every declared dependency has a resolved entry in the lockfile", not missing_pkgs, str(missing_pkgs))
no_integrity = [k for k, v in lock["packages"].items() if k and not v.get("link") and "integrity" not in v and not v.get("inBundle")]
check("all lockfile entries carry integrity hashes", not no_integrity, f"{len(lock['packages'])-1} packages; without integrity: {no_integrity[:3]}")
resolved_hosts = collections.Counter(re.sub(r"^(https?://[^/]+)/.*", r"\1", v["resolved"]) for v in lock["packages"].values() if "resolved" in v)
print("  [INFO] lockfile resolved hosts:", dict(resolved_hosts), "| packages:", len(lock["packages"]) - 1)
R.update(lock_packages=len(lock["packages"]) - 1, lock_hosts=dict(resolved_hosts))
for name, cmd in pkg["scripts"].items():
    print(f"  [INFO] script '{name}': {cmd}")
for f in ("scripts/export-models.mjs", "playwright.config.ts", "vite.config.ts", "tsconfig.json", "index.html", "src/main.tsx"):
    check(f"script/config target exists: {f}", os.path.isfile(os.path.join(REPO, f)))

# ---------------------------------------------------------------- 7. asset paths
print("\n[7] Asset path references (src + index.html + css) vs public/")
pub = {"/" + os.path.relpath(os.path.join(dp, f), os.path.join(REPO, "public")).replace(os.sep, "/")
       for dp, _, fs in os.walk(os.path.join(REPO, "public")) for f in fs}
src_files = [p for p in zip_inv if (p.startswith("src/") and p.endswith((".ts", ".tsx", ".css"))) or p == "index.html"]
ref_re = re.compile(r"""(?:["'`(=\s])(/(?:assets|licenses)/[A-Za-z0-9_\-./${}\[\]()+ ?:,'`]*?\.[A-Za-z0-9]+)(?=["'`)\s?#])""")
refs = collections.defaultdict(set)
for p in src_files:
    txt = open(os.path.join(REPO, p), encoding="utf-8").read()
    for m in ref_re.finditer(txt): refs[m.group(1)].add(p)
literal = {r: f for r, f in refs.items() if "${" not in r}
templ = {r: f for r, f in refs.items() if "${" in r}
unresolved = sorted(r for r in literal if r not in pub)
R.update(asset_refs_literal=len(literal), asset_refs_templated=sorted(templ), asset_refs_missing=unresolved, public_files=len(pub))
check(f"{len(literal)} literal asset references all resolve to files in public/", not unresolved, f"missing={unresolved}")
print("  [INFO] templated references (checked by expansion below):", sorted(templ))
# expand known templated patterns by checking that the pattern's files exist
for t in sorted(templ):
    pre, post = t.split("${", 1)[0], t.rsplit("}", 1)[1]
    cands = [x for x in pub if x.startswith(pre) and x.endswith(post)]
    print(f"     {t}  ->  {len(cands)} matching files in public/")
unref = sorted(x for x in pub if x not in literal and not any(x.startswith(t.split('${', 1)[0]) and x.endswith(t.rsplit('}', 1)[1]) for t in templ))
print(f"  [INFO] public/ files not referenced by a literal/templated path in src or index.html ({len(unref)}):")
for u in unref: print("       ", u)
R["public_unreferenced"] = unref

# ---------------------------------------------------------------- 8. bare imports vs package.json
print("\n[8] Third-party imports vs package.json")
declared = set(pkg["dependencies"]) | set(pkg["devDependencies"])
node_builtins = set(__import__("sys").stdlib_module_names) if False else {"fs", "path", "url", "os", "http", "https", "zlib", "crypto", "child_process", "util", "stream", "events", "assert", "module", "process", "buffer", "net", "readline", "worker_threads", "timers", "perf_hooks"}
imp_re = re.compile(r"""(?:import\s+(?:[^'"]*?\s+from\s+)?|import\(|require\(|export\s+[^'"]*?\s+from\s+)["']([^"'./][^"']*)["']""")
used = collections.defaultdict(set)
for p in zip_inv:
    if p.startswith("vercel-upload/"): continue
    if p.endswith((".ts", ".tsx", ".mjs", ".js")):
        txt = open(os.path.join(REPO, p), encoding="utf-8").read()
        for m in imp_re.finditer(txt):
            spec = m.group(1)
            if spec.startswith("node:"): continue
            name = "/".join(spec.split("/")[:2]) if spec.startswith("@") else spec.split("/")[0]
            if name in node_builtins: continue
            used[name].add(p)
undeclared = {n: sorted(f)[:3] for n, f in used.items() if n not in declared}
R.update(third_party_imports=sorted(used), undeclared_imports=undeclared)
check("every third-party import is declared in package.json", not undeclared, str(undeclared))
print("  [INFO] third-party packages imported:", sorted(used))

# ---------------------------------------------------------------- 9. counts
print("\n[9] Counts")
cats = collections.Counter(e["category"] for e in zip_inv.values())
R["category_counts"] = dict(cats)
for k, v in sorted(cats.items(), key=lambda kv: -kv[1]): print(f"   {k:<22}{v}")

R["problems"] = problems
json.dump(R, open(OUT, "w"), indent=1, default=str)
print("\n==================== RESULT ====================")
print("ALL CHECKS PASSED" if not problems else f"{len(problems)} PROBLEM(S):\n - " + "\n - ".join(problems))
print("results ->", OUT)
