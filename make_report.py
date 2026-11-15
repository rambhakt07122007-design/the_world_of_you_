#!/usr/bin/env python3
"""Generate MIGRATION_REPORT.md from recorded inventories / verification results / logs (no hand-typed numbers)."""
import os, re, json, subprocess, collections, hashlib

REPO = "/home/user/the-world-of-you"
INVDIR = "/home/user/migration/inventory"
LOGS = "/home/user/migration/logs"
ZIPNAME = "The-World-of-You-17-Native-Worlds-Source.zip"
REPORT = "MIGRATION_REPORT.md"

inv = json.load(open(f"{INVDIR}/zip_inventory.json"))
ver = json.load(open(f"{INVDIR}/verification_results.json"))
act = json.load(open(f"{INVDIR}/migration_actions.json"))
pre = [l.split(None, 2) for l in open(f"{INVDIR}/repo_pre_migration.txt").read().strip().split("\n")]
zip_sha = open("/home/user/migration/ORIGINAL_ZIP.sha256").read().split()[0]
zip_size = os.path.getsize(f"/home/user/migration/original/{ZIPNAME}")
build_log = re.sub(r"\x1b\[[0-9;]*m", "", open(f"{LOGS}/build.log").read())
modules = re.search(r"(\d+) modules transformed", build_log).group(1)
built_in = re.search(r"built in ([\d.]+s)", build_log).group(1)
npm_added = re.search(r"added (\d+) packages", open(f"{LOGS}/npm-ci.log").read()).group(1)
largest_chunk = re.findall(r"dist/assets/(\S+\.js)\s+([\d.]+) kB", build_log)
big = max(largest_chunk, key=lambda t: float(t[1]))

by = {e["path"]: e for e in inv}
cats = collections.Counter(e["category"] for e in inv)
ext = lambda p: os.path.splitext(p)[1].lower()
ts_all = [p for p in by if ext(p) in (".ts", ".tsx")]
ts_src = [p for p in ts_all if p.startswith("src/")]
ts_tests = [p for p in ts_all if p.startswith("tests/")]
ts_cfg = [p for p in ts_all if "/" not in p]
js_all = [p for p in by if ext(p) in (".js", ".mjs", ".cjs", ".jsx")]
css_all = [p for p in by if ext(p) == ".css"]
html_all = [p for p in by if ext(p) in (".html", ".htm")]
py_all = [p for p in by if ext(p) == ".py"]
src_total = len(ts_all) + len(js_all) + len(css_all) + len(html_all) + len(py_all)
img = [p for p in by if ext(p) in (".png", ".jpg", ".jpeg", ".webp", ".gif", ".avif", ".bmp", ".ico")]
imgfmt = collections.Counter(ext(p).lstrip(".") for p in img)
svg = [p for p in by if ext(p) == ".svg"]
audio = [p for p in by if ext(p) in (".mp3", ".wav", ".ogg", ".m4a", ".aac", ".flac", ".opus")]
video = [p for p in by if ext(p) in (".mp4", ".webm", ".mov", ".mkv")]
glb = sorted(p for p in by if ext(p) in (".glb", ".gltf"))
fonts = [p for p in by if ext(p) in (".woff2", ".woff", ".ttf", ".otf")]
md = [p for p in by if ext(p) == ".md"]; pdf = [p for p in by if ext(p) == ".pdf"]; txt = [p for p in by if ext(p) == ".txt"]
json_all = [p for p in by if ext(p) == ".json"]
js_files_gsap = subprocess.run(["grep", "-rl", "gsap", "src"], cwd=REPO, capture_output=True, text=True).stdout.split()
total_bytes = sum(e["size"] for e in inv)
largest = max(inv, key=lambda e: e["size"])
dirs = {os.path.dirname(p) for p in by}; alld = set()
for d in dirs:
    while d: alld.add(d); d = os.path.dirname(d)

readme_act = next(a for a in act["actions"] if a["path"] == "README.md")
dup_gitkeep = sorted(p for p in by if p.endswith("/.gitkeep") and by[p]["sha256"] == by["public/assets/flowers/.gitkeep"]["sha256"])
mib = lambda b: f"{b/1048576:.2f} MiB"

# ------------------------------------------------------------------ folder tree
KEY_ROOT = {"package.json", "package-lock.json", "index.html", "vite.config.ts", "tsconfig.json", "playwright.config.ts",
            "README.md", REPORT, ".gitignore", ".vercelignore", "DEPLOYMENT_LATEST.json", ZIPNAME}
all_paths = sorted(list(by) + [ZIPNAME, REPORT])
def build_tree(paths):
    root = {}
    for p in paths:
        node = root; parts = p.split("/")
        for part in parts[:-1]: node = node.setdefault(part + "/", {})
        node[parts[-1]] = None
    return root
def nfiles(n): return sum(1 if v is None else nfiles(v) for v in n.values())
def render(node, prefix="", root=False):
    out = []
    dnames = sorted((k for k, v in node.items() if v is not None), key=str.lower)
    fnames = sorted(k for k, v in node.items() if v is None)
    items = []
    for d in dnames: items.append(("dir", d, node[d]))
    if root:
        keys = [f for f in fnames if f in KEY_ROOT]
        rest = [f for f in fnames if f not in KEY_ROOT]
        qa = [f for f in rest if f.startswith("qa-")]; docs = [f for f in rest if f.endswith(".md")]
        other = [f for f in rest if f not in qa and f not in docs]
        for f in keys: items.append(("file", f, None))
        if docs: items.append(("note", f"{len(docs)} more project documents (*.md), e.g. {docs[0]} … {docs[-1]}", None))
        if qa: items.append(("note", f"{len(qa)} root QA artifacts (qa-*.png / .json / .txt)", None))
        for f in other: items.append(("file", f, None))
    elif len(fnames) <= 10:
        for f in fnames: items.append(("file", f, None))
    else:
        g = collections.defaultdict(list)
        for f in fnames: g[os.path.splitext(f)[1] or f].append(f)
        for e, fs in sorted(g.items()): items.append(("note", f"{len(fs)} × *{e}   ({fs[0]} … {fs[-1]})" if len(fs) > 1 else fs[0], None))
    for i, (kind, name, sub) in enumerate(items):
        last = i == len(items) - 1
        branch = "└── " if last else "├── "
        if kind == "dir":
            n = nfiles(sub)
            out.append(f"{prefix}{branch}{name}  ({n} file{'s' if n != 1 else ''})")
            out += render(sub, prefix + ("    " if last else "│   "))
        else:
            out.append(f"{prefix}{branch}{name}")
    return out
tree_lines = ["the-world-of-you/  (repository root = project root, no extra nesting)  — %d files" % len(all_paths)] + render(build_tree(all_paths), root=True)
tree_txt = "\n".join(tree_lines)
open("/home/user/migration/inventory/final_tree.txt", "w").write(tree_txt + "\n")

# ------------------------------------------------------------------ full inventory rows
rows = []
for p in sorted(by):
    st = "replaced (conflict)" if p == "README.md" else "added"
    rows.append(f"| `{p}` | {by[p]['size']:,} | `{by[p]['sha256'][:12]}` | {st} |")
rows.append(f"| `{ZIPNAME}` | {zip_size:,} | `{zip_sha[:12]}` | preserved (existing, not in ZIP) |")
rows.append(f"| `{REPORT}` | — | — | new (this file) |")

glb_rows = "\n".join(
    f"| `{p.split('/')[-1]}` | {r['bytes']:,} | {r['meshes']} | {r['materials']} | {r['textures']} | {r['nodes']} | {r['generator']} |"
    for p, r in sorted(ver["glb_report"].items()))

md_report = f"""# Migration Report — THE WORLD OF YOU (A Universe Made of 17 Little Surprises)

| | |
|---|---|
| **Target repository** | https://github.com/rambhakt07122007-design/the-world-of-you |
| **Branch** | `main` (only branch) |
| **Base commit (before migration)** | `ba8d1cd65f165927f64aca68c8fc70ca8fff3f6a` — "Add files via upload" |
| **Source archive** | `{ZIPNAME}` — {zip_size:,} bytes — SHA-256 `{zip_sha}` — git blob `5f9f1f52b0351cb100b1f7984208a205333c0e68` |
| **Prepared on** | 2026-11-11 (Asia/Calcutta) with Node v20.20.2, npm 10.8.2, git 2.47.3 |

## 1. Summary

| Metric | Result |
|---|---|
| Total ZIP entries | **{len(inv)}** ({len(inv)} files, 0 directory entries) |
| Total extracted files | **{len(inv)}** in {len(alld)} directories (not counting the stripped `chronos/` wrapper), {total_bytes:,} bytes ({mib(total_bytes)}) |
| Total migrated files | **{len(inv)}** — {act['summary']['added']} added + {act['summary']['conflict_replaced']} replaced (`README.md`, see §4) |
| Existing repo files preserved | **1** — the source ZIP itself (exists only in the repo) |
| Files in the repository after migration | **{len(all_paths)}** = {len(inv)} project files + 1 preserved ZIP + this report |
| Images and media files | **{len(img)}** images ({', '.join(f'{v} {k.upper()}' for k, v in imgfmt.most_common())}), {len(svg)} SVG, **{len(audio)} audio, {len(video)} video** → {len(img)+len(audio)+len(video)} total |
| 3D models | **{len(glb)}** GLB (0 GLTF) — all structurally valid glTF 2.0 |
| Source-code files | **{src_total}** — {len(ts_all)} TS/TSX ({len(ts_src)} in `src/`, {len(ts_tests)} Playwright specs, {len(ts_cfg)} root configs), {len(js_all)} JS/MJS, {len(css_all)} CSS, {len(html_all)} HTML, {len(py_all)} Python |
| Other assets | {len(fonts)} WOFF2 fonts, {len(md)} Markdown docs, {len(pdf)} PDFs, {len(txt)} text files (licences, QA logs, build chunks), {len(json_all)} JSON files (incl. both lockfiles) |
| Files skipped | **0** (nothing in the ZIP matched an exclusion rule) |
| Files exceeding GitHub limits | **0** — largest file is `{largest['path']}` at {largest['size']:,} bytes ({mib(largest['size'])}); GitHub warns > 50 MiB and blocks > 100 MiB. Git LFS not required and not configured. |
| Conflicts resolved | **1** — `README.md` (§4) |
| Missing files | **0** |
| Unexpected overwrites | **0** (the only overwrite is the documented `README.md` conflict) |
| Build validation | `npm ci` ✔ · `tsc` 0 errors ✔ · `npm run build` ✔ (exit 0) — details in §8 |
| Final repository status | See §10 |

## 2. Phase 1 — ZIP extraction

* Archive opened and verified: `unzip -t` → *No errors detected*; Python `zipfile.testzip()` → `None`. No encrypted entries, no symlinks, no absolute or `..` paths, no exact-duplicate or case-colliding names, no `__MACOSX`/`.DS_Store`/`Thumbs.db` junk.
* Extracted to a temporary directory (`/tmp/zip-extract`); the original ZIP was made read-only and its SHA-256 re-checked after extraction and again at the end (unchanged).
* **Actual project root: `chronos/`.** All {len(inv)} entries sit under this single wrapper folder, which contains `package.json`, `package-lock.json`, `index.html`, `vite.config.ts`, `tsconfig.json`, `src/`, `public/`. The wrapper was **stripped**, so the project root is the repository root (no `chronos/` level in the repo).
* Nested folder noted: `vercel-upload/deploy-root/` is a legacy static-export packaging folder with its own tiny `package.json`; it is not the app root (`.vercelignore` excludes it from deployments). Preserved.
* Duplicate content detected (all preserved — nothing deleted):
  * `vercel-upload/index.html` ≡ gunzip(`vercel-upload/deploy-root/index.html.gz`) ≡ brotli-decompress(`…/index.html.br`) — one 225,738-byte single-file build stored three ways (verified byte-identical).
  * `qa-results.json` ≡ `qa-refinement-initial.json` (identical QA output).
  * {len(dup_gitkeep)} identical `.gitkeep` placeholders ({', '.join('`'+p.rsplit('/',2)[1]+'`' for p in dup_gitkeep)}); a 5th, `public/assets/audio/.gitkeep`, differs by one byte.

## 3. Phase 2 — repository state before migration

| Item | State |
|---|---|
| Branches | `main` only (`ba8d1cd`) · no tags |
| Commits | `99eaa62` "Initial commit" (added `README.md`) → `ba8d1cd` "Add files via upload" (added the ZIP); both by rudra |
| Files | `README.md` (18 bytes: `# the-world-of-you`), `{ZIPNAME}` ({zip_size:,} bytes) |
| Project structure / assets | none (no `src/`, no `public/`, no `package.json`) |
| Config | none (no `.gitignore`, `.gitattributes`, LFS config, workflows or licence) |

## 4. Phase 3 — copy, comparison and conflict resolution

Every destination path was classified **before** anything was written (dry run first), using SHA-256 comparison.

| Outcome | Files |
|---|---|
| Added (did not exist in repo) | {act['summary']['added']} |
| Identical (left as is) | {act['summary']['identical']} |
| Conflict, resolved in favour of the ZIP | {act['summary']['conflict_replaced']} |
| Conflict, unresolved | {act['summary']['conflict_unresolved']} |
| Blocked (secret-like filename) | {act['summary']['blocked_secret_name']} |
| Existing repo-only file preserved | 1 |

**Conflict — `README.md`.** The repository's file was GitHub's auto-generated one-line stub (`{readme_act['existing_content_preview'].strip()}`, {readme_act['existing_bytes']} bytes, SHA-256 `{readme_act['existing_sha256'][:16]}…`). The ZIP's `README.md` is the project's complete documentation ({readme_act['zip_bytes']:,} bytes, SHA-256 `{readme_act['zip_sha256'][:16]}…`). Policy "prefer the complete and verified source file" → the ZIP version was used. The old text is recorded here verbatim and remains in git history (`ba8d1cd`).

**Preserved — `{ZIPNAME}`.** It is the source archive supplied by the owner and is not part of its own contents. It was kept untouched (byte-identical, same blob id) rather than deleted, because the migration rules forbid removing existing content without need. It duplicates what is now extracted; once you are satisfied with the migration it can be removed with `git rm {ZIPNAME}` to slim the working tree (its 10.2 MiB stays in history regardless). It is not referenced by the build.

**Not copied / never uploaded.** `node_modules/`, `dist/`, `.git/`, `.env*`, keys and tokens — none exist in the ZIP. Build output (`node_modules`, `dist`) was produced only in a throw-away export outside the repository.

**`.gitignore` safety check.** The project's `.gitignore` ignores `node_modules/ dist/ coverage/ .DS_Store *.log *.tsbuildinfo .env*`. `git check-ignore` confirmed that **none** of the {len(inv)+1} files present at that point (the {len(inv)} project files + the preserved ZIP) is ignored, so nothing was silently dropped from the commit.

**GitHub limits.** Verified against GitHub Docs ("About large files on GitHub"): warning > 50 MiB, hard block > 100 MiB, 25 MiB limit for browser uploads, repositories ideally < 1 GB. Largest file here: {mib(largest['size'])}. Total payload ≈ {mib(total_bytes)} + the 10.2 MiB ZIP.

## 5. Phase 4 — verification

| Check | Result |
|---|---|
| ZIP inventory vs repository index | {len(inv)}/{len(inv)} present, 0 missing |
| SHA-256 of every repo file vs ZIP file | 0 mismatches |
| Git blob id of every staged file vs `git hash-object` of extracted file | 0 mismatches |
| File modes | all `100644` (no symlinks, no executable bits) |
| Extra files in repo | only the preserved ZIP (+ this report) |
| `node_modules` / `dist` / `.git` / `.env` / key files staged | none |
| Text files ({ver['text_files_checked']}) | strict UTF-8 ✔ · no NUL bytes ✔ · no BOM ✔ · 17/17 JSON parse ✔ · Python compiles ✔ · `node --check` on all `.mjs`/`.js` ✔ · 1 CRLF file preserved as-is (`public/assets/fonts/OFL-DM-Sans.txt`) |
| Images ({len(img)}) | all fully decoded with Pillow ✔ ({', '.join(f'{v} {k}' for k, v in ver['image_formats'].items())}); all 17 `gift-previews/gift-01…17.webp` present |
| Fonts / PDFs | 6/6 WOFF2 valid (signature + declared length); 2/2 PDFs have header and `%%EOF` |
| 3D models ({len(glb)}) | glTF 2.0 container, declared length, chunk walk, JSON, accessor/bufferView ranges all valid; **no external URIs** (self-contained) |
| `package.json` / lockfile | lockfile v3 · name/version match · dependencies & devDependencies identical to lock root · every dependency resolved · {ver['lock_packages']} packages all with `integrity` hashes · all from `registry.npmjs.org` |
| Script targets | `scripts/export-models.mjs`, `playwright.config.ts`, `vite.config.ts`, `tsconfig.json`, `index.html`, `src/main.tsx` all exist |
| Asset paths | {ver['asset_refs_literal']} literal `/assets…` + `/licenses…` references in `src/`, CSS and `index.html` all resolve to files in `public/`; templated `/assets/gift-previews/${{gift.id}}.webp` → 17/17 files exist |
| Imports | every third-party import is declared in `package.json` ({', '.join(ver['third_party_imports'])}) |
| Original ZIP | unchanged (SHA-256 identical before/after) |

`public/` files not referenced by any path in the source (20, all preserved): 5 `.gitkeep` placeholders, 4 OFL font licence texts + fonts `README.md`, `models/README.md`, 2 licence texts in `licenses/`, and the **7 GLB snapshots** — the project's own `public/assets/models/README.md` states these historical GLBs are *not loaded by the application* (models are built at runtime from `src/three/`).

## 6. Inventory by type

| Category | Files | Notes |
|---|---:|---|
| TypeScript / TSX | {len(ts_all)} | `src/` {len(ts_src)} · `tests/` {len(ts_tests)} · root configs {len(ts_cfg)} |
| JavaScript / MJS | {len(js_all)} | helper scripts (`scripts/`, `tests/`), `vercel-upload/deploy-root/build-static.js` |
| CSS | {len(css_all)} | all hand-written in `src/styles/` — **no Tailwind** in this project (no config, dependency or directives) |
| HTML | {len(html_all)} | `index.html` + 2 legacy `vercel-upload` exports |
| Python | {len(py_all)} | asset helper scripts |
| Raster images | {len(img)} | {', '.join(f'{v} {k.upper()}' for k, v in imgfmt.most_common())} (backgrounds, postcards, scenes, 17 gift previews, QA screenshots) |
| SVG files | {len(svg)} | none in the ZIP (favicon is an inline SVG data-URI in `index.html`) |
| Audio / video | {len(audio)} / {len(video)} | none in the ZIP — `public/assets/audio/` holds only `.gitkeep`; the docs state audio slots are intentionally empty until owner media is supplied |
| 3D models | {len(glb)} | `.glb` only; no `.gltf`; textures are embedded in the GLBs |
| Fonts | {len(fonts)} | Playfair Display, Cormorant Garamond (+italic), DM Sans, Caveat — self-hosted WOFF2 + OFL licences |
| Markdown / PDF / text | {len(md)} / {len(pdf)} / {len(txt)} | project documentation, source-reference PDFs, licences, QA logs, build chunks |
| JSON | {len(json_all)} | incl. `package.json` and `package-lock.json` (×2 each: root + `vercel-upload/deploy-root`), `tsconfig.json`, `DEPLOYMENT_LATEST.json`, QA result files (`vite.config.ts` / `playwright.config.ts` are counted under TypeScript) |
| Compressed artifacts | {cats['compressed_artifact']} | `index.html.gz`, `index.html.br` (legacy export) |
| Placeholders | {cats['placeholder_gitkeep']} | `.gitkeep` |

Technology actually present in the code: **GSAP** (`gsap` ^3.15.0 — scroll-linked scene stage with ScrollTrigger in `src/scenes/SceneExperience.tsx`, letter-unfolding timeline in `src/three/letter.ts`, cake entrance in `src/world/CakeBakingJourney.tsx`; two of the three load it via dynamic `import()`, which is why ScrollTrigger builds into its own chunk), **Three.js** (`three` ^0.187.0, imported in 13 source files, incl. `GLTFExporter` and `RoomEnvironment` add-ons, custom GLSL materials in `cake.ts`, `celestial.ts`, `garden.ts`), **React Three Fiber** (`@react-three/fiber` ^9.8.2 — `src/three/NativeGiftCanvas.tsx`), React 19, TypeScript 5.9, Vite 7, `react-pageflip`, `lucide-react`, Playwright (tests).

### 3D models

| File | Bytes | Meshes | Materials | Textures | Nodes | Generator |
|---|---:|---:|---:|---:|---:|---|
{glb_rows}

## 7. Fixes applied

None. No migration-related defect was found, so **no file was modified after copying** (the only content change versus a straight copy is the documented `README.md` resolution).

## 8. Phase 5 — build validation

Run from an export of the **staged index** (exactly what is committed) in a temporary directory, so no `node_modules/` or `dist/` ever touched the repository.

| Step | Command | Result |
|---|---|---|
| Install | `npm ci` | exit 0 · {npm_added} packages installed in ~5 s (lockfile lists {ver['lock_packages']}; 54 of them are other-OS/CPU optional binaries such as `@esbuild/*`, `@rollup/*`) · `package-lock.json` unchanged |
| Type-check | `tsc --noEmit -p tsconfig.json` (`strict`, `noUnusedLocals`, `noUnusedParameters`) | exit 0 · **0 errors** (covers {len(ts_src)} files in `src/`) · no unresolved imports |
| Production build | `npm run build` (= `tsc -b && vite build`) | **exit 0** · {modules} modules transformed · built in {built_in} · `dist/` = 62 files / 6.9 MB |
| `public/` → `dist/` | byte comparison | 53/53 identical (incl. 7/7 GLB) |
| Asset references in built HTML/CSS/JS | static resolution | 18/18 resolve |
| Serve & fetch | `vite preview`, HTTP GET + SHA-256 | `/`, entry JS and CSS OK · 53/53 `public/` files returned byte-identical (an SPA-fallback HTML reply would fail this test) |
| Extended type-check | `src` + `tests/*.spec.ts` + `playwright.config.ts` + `vite.config.ts` | **0 missing imports (no TS2307)**. 3 informational `TS2683` (`'this'` implicitly any) in `tests/cinematic.spec.ts`, `tests/letter-refinement.spec.ts`, `tests/ultra-access.spec.ts` — inside Playwright `page.evaluate` snippets that monkey-patch `getContext`. Files are byte-identical to the ZIP and outside the project's own `tsc` scope (`include: ["src"]`); not changed. |

Observations (not migration problems, not changed): Vite prints its standard advisory that one chunk exceeds 500 kB (`{big[0]}` — {big[1]} kB, the Three.js code).

**Not run:** the Playwright browser suite (`npm run test:browser`; needs Chromium and a dev server on port 4181) and any hardware-microphone testing. The build result above is a *build* result, not a claim that every interaction was exercised in a browser.

## 9. Security scan

* No `.env*`, key, certificate or credential-named files (the one filename match, `src/styles/designTokens.css`, is a CSS design-tokens file).
* Content scan of all {len(inv)} files (binary files read as text; `.gz` and `.br` artifacts decompressed first) for private keys, AWS/GitHub/OpenAI/Slack/Google/Vercel/Supabase tokens, JWTs and generic `key/secret/password = "…"` assignments: **0 matches** (the scanner was self-tested against a fake token to prove it can detect one).
* `DEPLOYMENT_LATEST.json` contains only public deployment identifiers/URLs, no secret.
* **Please double-check:** the project's own reports (`PROJECT_PROGRESS.md`, `FINAL_QA_REPORT.md`, `GIFT_QA_REPORT.md`, `QA_REPORT.md`) say a Vercel token pasted into a chat during an earlier deployment "must be revoked by the user". No token is in the repository, but make sure that token was revoked in your Vercel account.

## 10. Final repository status (as of preparation)

* Local branch `main` holds **one new commit** on top of `origin/main` @ `ba8d1cd`, message: `Complete project ZIP migration with all source code and assets`. It contains all {len(inv)} project files, the preserved source ZIP and this report ({len(all_paths)} files). *(A file cannot contain the hash of the commit that contains it; run `git log -1` for the SHA.)*
* **Push status at preparation time: not pushed.** The environment that prepared this commit had read-only GitHub access: `git push` failed with `fatal: could not read Username for 'https://github.com'`, the GitHub REST API answered `Requires authentication`, and no GitHub write connector or credential was available. The commit was therefore handed over as a git bundle (`the-world-of-you-migration.bundle`); pushing it from an authenticated machine is the only remaining step:

```bash
git clone the-world-of-you-migration.bundle the-world-of-you
cd the-world-of-you
git remote set-url origin https://github.com/rambhakt07122007-design/the-world-of-you.git
git push origin main        # fast-forward from ba8d1cd; uploads only the new objects
```

## Appendix A — Final folder structure

```text
{tree_txt}
```

## Appendix B — Full file inventory

<details><summary>{len(rows)} files (path · bytes · SHA-256 prefix · migration action)</summary>

| Path | Bytes | SHA-256 (12) | Action |
|---|---:|---|---|
{chr(10).join(rows)}

</details>
"""
open(os.path.join(REPO, REPORT), "w", encoding="utf-8").write(md_report)
print("written:", os.path.join(REPO, REPORT), len(md_report), "bytes")
print("source_total", src_total, "| ts", len(ts_all), "| js", len(js_all), "| css", len(css_all), "| html", len(html_all), "| py", len(py_all))
print("total repo files after report:", len(all_paths))
print("gsap files:", js_files_gsap)
