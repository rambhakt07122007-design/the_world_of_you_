#!/usr/bin/env python3
"""
Compare-then-copy migration of the extracted project root into the repository working tree.

* SRC = the real project root inside the ZIP ('chronos/'); the wrapper folder is stripped so the
  project root becomes the repository root (no extra nesting level).
* Nothing is overwritten blindly. Every destination path is classified first:
    added      -> does not exist in repo                      -> copy
    identical  -> exists with identical bytes (sha256)        -> leave alone
    conflict   -> exists with different bytes                 -> resolve per policy below (never silent)
* Policy for conflicts: prefer the complete, verified source file. A destination file that is only an
  auto-generated one-line Markdown stub (<= 64 bytes, a single '# title' line) is considered a
  placeholder and is replaced by the larger ZIP file. Any other conflict is NOT overwritten: it is left
  untouched and the ZIP version is stored next to it as '<name>.from-zip' for a human decision.
* Existing repo files that are not in the ZIP are preserved untouched.
* .git/, node_modules/ and dist/ are never copied (none exist in the ZIP; guarded anyway).
"""
import os, sys, json, hashlib, shutil, re

SRC = "/tmp/zip-extract/chronos"
DST = "/home/user/the-world-of-you"
OUT = "/home/user/migration/inventory/migration_actions.json"
DRY = "--execute" not in sys.argv

NEVER_COPY_DIRS = {".git", "node_modules", "dist"}
SECRET_NAME = re.compile(r"(^\.env)|\.pem$|\.key$|\.p12$|\.pfx$|^id_rsa|^id_ed25519|\.keystore$", re.I)

def sha256(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()

def walk(root):
    for dp, dns, fns in os.walk(root):
        dns[:] = sorted(d for d in dns if d not in NEVER_COPY_DIRS)
        for fn in sorted(fns):
            full = os.path.join(dp, fn)
            yield os.path.relpath(full, root).replace(os.sep, "/"), full

def is_placeholder_stub(path):
    if os.path.getsize(path) > 64:
        return False
    txt = open(path, "rb").read().decode("utf-8", "replace")
    return re.fullmatch(r"# [^\n]*\n?", txt) is not None

src_files = dict(walk(SRC))
dst_before = dict(walk(DST))
actions, counts = [], {"added": 0, "identical": 0, "conflict_replaced": 0, "conflict_unresolved": 0, "blocked_secret_name": 0}

for rel, s in src_files.items():
    d = os.path.join(DST, rel)
    if SECRET_NAME.search(os.path.basename(rel)):
        counts["blocked_secret_name"] += 1
        actions.append({"path": rel, "action": "BLOCKED (secret-like filename)"})
        continue
    if rel not in dst_before:
        actions.append({"path": rel, "action": "added", "bytes": os.path.getsize(s), "sha256": sha256(s)})
        counts["added"] += 1
        if not DRY:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copyfile(s, d); shutil.copymode(s, d)
        continue
    ssha, dsha = sha256(s), sha256(d)
    if ssha == dsha:
        actions.append({"path": rel, "action": "identical (kept as is)", "sha256": ssha})
        counts["identical"] += 1
        continue
    # ---- conflict ----
    entry = {"path": rel, "existing_bytes": os.path.getsize(d), "existing_sha256": dsha,
             "zip_bytes": os.path.getsize(s), "zip_sha256": ssha,
             "existing_content_preview": open(d, "rb").read(200).decode("utf-8", "replace")}
    if is_placeholder_stub(d) and os.path.getsize(s) > os.path.getsize(d):
        entry["action"] = "conflict -> replaced by ZIP version"
        entry["reason"] = ("Existing file is a one-line auto-generated stub; ZIP file is the complete, "
                           "authoritative version. Old content is preserved verbatim in this log and in git history.")
        counts["conflict_replaced"] += 1
        if not DRY:
            shutil.copyfile(s, d); shutil.copymode(s, d)
    else:
        entry["action"] = "conflict -> UNRESOLVED (existing kept, ZIP copy saved as .from-zip)"
        entry["reason"] = "Both files have real content; needs a human decision."
        counts["conflict_unresolved"] += 1
        if not DRY:
            shutil.copyfile(s, d + ".from-zip")
    actions.append(entry)

preserved = [r for r in dst_before if r not in src_files]
for r in preserved:
    actions.append({"path": r, "action": "preserved (exists only in repo, not in ZIP)",
                    "bytes": os.path.getsize(os.path.join(DST, r)), "sha256": sha256(os.path.join(DST, r))})

summary = {"mode": "DRY-RUN" if DRY else "EXECUTED", "zip_files": len(src_files), "repo_files_before": len(dst_before),
           "preserved_repo_only_files": preserved, **counts}
print(json.dumps(summary, indent=2))
print("\nConflicts / non-trivial actions:")
for a in actions:
    if a["action"].startswith(("conflict", "BLOCKED", "preserved")):
        print(" -", a["path"], "=>", a["action"])
if not DRY:
    json.dump({"summary": summary, "actions": actions}, open(OUT, "w"), indent=1)
    print("\nAction log written:", OUT)
