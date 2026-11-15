# Migration Report — THE WORLD OF YOU (A Universe Made of 17 Little Surprises)

| | |
|---|---|
| **Target repository** | https://github.com/rambhakt07122007-design/the-world-of-you |
| **Branch** | `main` (only branch) |
| **Base commit (before migration)** | `ba8d1cd65f165927f64aca68c8fc70ca8fff3f6a` — "Add files via upload" |
| **Source archive** | `The-World-of-You-17-Native-Worlds-Source.zip` — 10,737,226 bytes — SHA-256 `fbf2257a89b8f65010fa190f8f6a5acd7f90489a86c5553e9e5d9f5e971dbd9c` — git blob `5f9f1f52b0351cb100b1f7984208a205333c0e68` |
| **Prepared on** | 2026-11-11 (Asia/Calcutta) with Node v20.20.2, npm 10.8.2, git 2.47.3 |

## 1. Summary

| Metric | Result |
|---|---|
| Total ZIP entries | **240** (240 files, 0 directory entries) |
| Total extracted files | **240** in 33 directories (not counting the stripped `chronos/` wrapper), 14,208,327 bytes (13.55 MiB) |
| Total migrated files | **240** — 239 added + 1 replaced (`README.md`, see §4) |
| Existing repo files preserved | **1** — the source ZIP itself (exists only in the repo) |
| Files in the repository after migration | **242** = 240 project files + 1 preserved ZIP + this report |
| Images and media files | **53** images (27 WEBP, 25 PNG, 1 JPG), 0 SVG, **0 audio, 0 video** → 53 total |
| 3D models | **7** GLB (0 GLTF) — all structurally valid glTF 2.0 |
| Source-code files | **72** — 50 TS/TSX (41 in `src/`, 7 Playwright specs, 2 root configs), 10 JS/MJS, 7 CSS, 3 HTML, 2 Python |
| Other assets | 6 WOFF2 fonts, 40 Markdown docs, 2 PDFs, 34 text files (licences, QA logs, build chunks), 17 JSON files (incl. both lockfiles) |
| Files skipped | **0** (nothing in the ZIP matched an exclusion rule) |
| Files exceeding GitHub limits | **0** — largest file is `public/assets/models/garden.glb` at 1,541,248 bytes (1.47 MiB); GitHub warns > 50 MiB and blocks > 100 MiB. Git LFS not required and not configured. |
| Conflicts resolved | **1** — `README.md` (§4) |
| Missing files | **0** |
| Unexpected overwrites | **0** (the only overwrite is the documented `README.md` conflict) |
| Build validation | `npm ci` ✔ · `tsc` 0 errors ✔ · `npm run build` ✔ (exit 0) — details in §8 |
| Final repository status | See §10 |

## 2. Phase 1 — ZIP extraction

* Archive opened and verified: `unzip -t` → *No errors detected*; Python `zipfile.testzip()` → `None`. No encrypted entries, no symlinks, no absolute or `..` paths, no exact-duplicate or case-colliding names, no `__MACOSX`/`.DS_Store`/`Thumbs.db` junk.
* Extracted to a temporary directory (`/tmp/zip-extract`); the original ZIP was made read-only and its SHA-256 re-checked after extraction and again at the end (unchanged).
* **Actual project root: `chronos/`.** All 240 entries sit under this single wrapper folder, which contains `package.json`, `package-lock.json`, `index.html`, `vite.config.ts`, `tsconfig.json`, `src/`, `public/`. The wrapper was **stripped**, so the project root is the repository root (no `chronos/` level in the repo).
* Nested folder noted: `vercel-upload/deploy-root/` is a legacy static-export packaging folder with its own tiny `package.json`; it is not the app root (`.vercelignore` excludes it from deployments). Preserved.
* Duplicate content detected (all preserved — nothing deleted):
  * `vercel-upload/index.html` ≡ gunzip(`vercel-upload/deploy-root/index.html.gz`) ≡ brotli-decompress(`…/index.html.br`) — one 225,738-byte single-file build stored three ways (verified byte-identical).
  * `qa-results.json` ≡ `qa-refinement-initial.json` (identical QA output).
  * 4 identical `.gitkeep` placeholders (`flowers`, `gallery`, `gifts`, `objects`); a 5th, `public/assets/audio/.gitkeep`, differs by one byte.

## 3. Phase 2 — repository state before migration

| Item | State |
|---|---|
| Branches | `main` only (`ba8d1cd`) · no tags |
| Commits | `99eaa62` "Initial commit" (added `README.md`) → `ba8d1cd` "Add files via upload" (added the ZIP); both by rudra |
| Files | `README.md` (18 bytes: `# the-world-of-you`), `The-World-of-You-17-Native-Worlds-Source.zip` (10,737,226 bytes) |
| Project structure / assets | none (no `src/`, no `public/`, no `package.json`) |
| Config | none (no `.gitignore`, `.gitattributes`, LFS config, workflows or licence) |

## 4. Phase 3 — copy, comparison and conflict resolution

Every destination path was classified **before** anything was written (dry run first), using SHA-256 comparison.

| Outcome | Files |
|---|---|
| Added (did not exist in repo) | 239 |
| Identical (left as is) | 0 |
| Conflict, resolved in favour of the ZIP | 1 |
| Conflict, unresolved | 0 |
| Blocked (secret-like filename) | 0 |
| Existing repo-only file preserved | 1 |

**Conflict — `README.md`.** The repository's file was GitHub's auto-generated one-line stub (`# the-world-of-you`, 18 bytes, SHA-256 `c908a5b5b83f9178…`). The ZIP's `README.md` is the project's complete documentation (8,878 bytes, SHA-256 `8d687cf7a3481163…`). Policy "prefer the complete and verified source file" → the ZIP version was used. The old text is recorded here verbatim and remains in git history (`ba8d1cd`).

**Preserved — `The-World-of-You-17-Native-Worlds-Source.zip`.** It is the source archive supplied by the owner and is not part of its own contents. It was kept untouched (byte-identical, same blob id) rather than deleted, because the migration rules forbid removing existing content without need. It duplicates what is now extracted; once you are satisfied with the migration it can be removed with `git rm The-World-of-You-17-Native-Worlds-Source.zip` to slim the working tree (its 10.2 MiB stays in history regardless). It is not referenced by the build.

**Not copied / never uploaded.** `node_modules/`, `dist/`, `.git/`, `.env*`, keys and tokens — none exist in the ZIP. Build output (`node_modules`, `dist`) was produced only in a throw-away export outside the repository.

**`.gitignore` safety check.** The project's `.gitignore` ignores `node_modules/ dist/ coverage/ .DS_Store *.log *.tsbuildinfo .env*`. `git check-ignore` confirmed that **none** of the 241 files present at that point (the 240 project files + the preserved ZIP) is ignored, so nothing was silently dropped from the commit.

**GitHub limits.** Verified against GitHub Docs ("About large files on GitHub"): warning > 50 MiB, hard block > 100 MiB, 25 MiB limit for browser uploads, repositories ideally < 1 GB. Largest file here: 1.47 MiB. Total payload ≈ 13.55 MiB + the 10.2 MiB ZIP.

## 5. Phase 4 — verification

| Check | Result |
|---|---|
| ZIP inventory vs repository index | 240/240 present, 0 missing |
| SHA-256 of every repo file vs ZIP file | 0 mismatches |
| Git blob id of every staged file vs `git hash-object` of extracted file | 0 mismatches |
| File modes | all `100644` (no symlinks, no executable bits) |
| Extra files in repo | only the preserved ZIP (+ this report) |
| `node_modules` / `dist` / `.git` / `.env` / key files staged | none |
| Text files (170) | strict UTF-8 ✔ · no NUL bytes ✔ · no BOM ✔ · 17/17 JSON parse ✔ · Python compiles ✔ · `node --check` on all `.mjs`/`.js` ✔ · 1 CRLF file preserved as-is (`public/assets/fonts/OFL-DM-Sans.txt`) |
| Images (53) | all fully decoded with Pillow ✔ (27 WEBP, 25 PNG, 1 JPEG); all 17 `gift-previews/gift-01…17.webp` present |
| Fonts / PDFs | 6/6 WOFF2 valid (signature + declared length); 2/2 PDFs have header and `%%EOF` |
| 3D models (7) | glTF 2.0 container, declared length, chunk walk, JSON, accessor/bufferView ranges all valid; **no external URIs** (self-contained) |
| `package.json` / lockfile | lockfile v3 · name/version match · dependencies & devDependencies identical to lock root · every dependency resolved · 147 packages all with `integrity` hashes · all from `registry.npmjs.org` |
| Script targets | `scripts/export-models.mjs`, `playwright.config.ts`, `vite.config.ts`, `tsconfig.json`, `index.html`, `src/main.tsx` all exist |
| Asset paths | 16 literal `/assets…` + `/licenses…` references in `src/`, CSS and `index.html` all resolve to files in `public/`; templated `/assets/gift-previews/${gift.id}.webp` → 17/17 files exist |
| Imports | every third-party import is declared in `package.json` (@playwright/test, @react-three/fiber, @vitejs/plugin-react, gsap, lucide-react, react, react-dom, react-pageflip, three, vite) |
| Original ZIP | unchanged (SHA-256 identical before/after) |

`public/` files not referenced by any path in the source (20, all preserved): 5 `.gitkeep` placeholders, 4 OFL font licence texts + fonts `README.md`, `models/README.md`, 2 licence texts in `licenses/`, and the **7 GLB snapshots** — the project's own `public/assets/models/README.md` states these historical GLBs are *not loaded by the application* (models are built at runtime from `src/three/`).

## 6. Inventory by type

| Category | Files | Notes |
|---|---:|---|
| TypeScript / TSX | 50 | `src/` 41 · `tests/` 7 · root configs 2 |
| JavaScript / MJS | 10 | helper scripts (`scripts/`, `tests/`), `vercel-upload/deploy-root/build-static.js` |
| CSS | 7 | all hand-written in `src/styles/` — **no Tailwind** in this project (no config, dependency or directives) |
| HTML | 3 | `index.html` + 2 legacy `vercel-upload` exports |
| Python | 2 | asset helper scripts |
| Raster images | 53 | 27 WEBP, 25 PNG, 1 JPG (backgrounds, postcards, scenes, 17 gift previews, QA screenshots) |
| SVG files | 0 | none in the ZIP (favicon is an inline SVG data-URI in `index.html`) |
| Audio / video | 0 / 0 | none in the ZIP — `public/assets/audio/` holds only `.gitkeep`; the docs state audio slots are intentionally empty until owner media is supplied |
| 3D models | 7 | `.glb` only; no `.gltf`; textures are embedded in the GLBs |
| Fonts | 6 | Playfair Display, Cormorant Garamond (+italic), DM Sans, Caveat — self-hosted WOFF2 + OFL licences |
| Markdown / PDF / text | 40 / 2 / 34 | project documentation, source-reference PDFs, licences, QA logs, build chunks |
| JSON | 17 | incl. `package.json` and `package-lock.json` (×2 each: root + `vercel-upload/deploy-root`), `tsconfig.json`, `DEPLOYMENT_LATEST.json`, QA result files (`vite.config.ts` / `playwright.config.ts` are counted under TypeScript) |
| Compressed artifacts | 2 | `index.html.gz`, `index.html.br` (legacy export) |
| Placeholders | 5 | `.gitkeep` |

Technology actually present in the code: **GSAP** (`gsap` ^3.15.0 — scroll-linked scene stage with ScrollTrigger in `src/scenes/SceneExperience.tsx`, letter-unfolding timeline in `src/three/letter.ts`, cake entrance in `src/world/CakeBakingJourney.tsx`; two of the three load it via dynamic `import()`, which is why ScrollTrigger builds into its own chunk), **Three.js** (`three` ^0.187.0, imported in 13 source files, incl. `GLTFExporter` and `RoomEnvironment` add-ons, custom GLSL materials in `cake.ts`, `celestial.ts`, `garden.ts`), **React Three Fiber** (`@react-three/fiber` ^9.8.2 — `src/three/NativeGiftCanvas.tsx`), React 19, TypeScript 5.9, Vite 7, `react-pageflip`, `lucide-react`, Playwright (tests).

### 3D models

| File | Bytes | Meshes | Materials | Textures | Nodes | Generator |
|---|---:|---:|---:|---:|---:|---|
| `cake.glb` | 371,836 | 30 | 17 | 3 | 58 | THREE.GLTFExporter r187 |
| `crown.glb` | 398,944 | 28 | 10 | 0 | 45 | THREE.GLTFExporter r187 |
| `eternal-rose.glb` | 131,852 | 6 | 5 | 2 | 75 | THREE.GLTFExporter r187 |
| `garden.glb` | 1,541,248 | 121 | 35 | 11 | 593 | THREE.GLTFExporter r187 |
| `letter-desk.glb` | 452,160 | 15 | 10 | 3 | 18 | THREE.GLTFExporter r187 |
| `observatory.glb` | 423,504 | 129 | 5 | 0 | 137 | THREE.GLTFExporter r187 |
| `portal.glb` | 175,348 | 4 | 3 | 0 | 4 | THREE.GLTFExporter r187 |

## 7. Fixes applied

None. No migration-related defect was found, so **no file was modified after copying** (the only content change versus a straight copy is the documented `README.md` resolution).

## 8. Phase 5 — build validation

Run from an export of the **staged index** (exactly what is committed) in a temporary directory, so no `node_modules/` or `dist/` ever touched the repository.

| Step | Command | Result |
|---|---|---|
| Install | `npm ci` | exit 0 · 96 packages installed in ~5 s (lockfile lists 147; 54 of them are other-OS/CPU optional binaries such as `@esbuild/*`, `@rollup/*`) · `package-lock.json` unchanged |
| Type-check | `tsc --noEmit -p tsconfig.json` (`strict`, `noUnusedLocals`, `noUnusedParameters`) | exit 0 · **0 errors** (covers 41 files in `src/`) · no unresolved imports |
| Production build | `npm run build` (= `tsc -b && vite build`) | **exit 0** · 2134 modules transformed · built in 8.18s · `dist/` = 62 files / 6.9 MB |
| `public/` → `dist/` | byte comparison | 53/53 identical (incl. 7/7 GLB) |
| Asset references in built HTML/CSS/JS | static resolution | 18/18 resolve |
| Serve & fetch | `vite preview`, HTTP GET + SHA-256 | `/`, entry JS and CSS OK · 53/53 `public/` files returned byte-identical (an SPA-fallback HTML reply would fail this test) |
| Extended type-check | `src` + `tests/*.spec.ts` + `playwright.config.ts` + `vite.config.ts` | **0 missing imports (no TS2307)**. 3 informational `TS2683` (`'this'` implicitly any) in `tests/cinematic.spec.ts`, `tests/letter-refinement.spec.ts`, `tests/ultra-access.spec.ts` — inside Playwright `page.evaluate` snippets that monkey-patch `getContext`. Files are byte-identical to the ZIP and outside the project's own `tsc` scope (`include: ["src"]`); not changed. |

Observations (not migration problems, not changed): Vite prints its standard advisory that one chunk exceeds 500 kB (`letter-D9nCpsSk.js` — 765.72 kB, the Three.js code).

**Not run:** the Playwright browser suite (`npm run test:browser`; needs Chromium and a dev server on port 4181) and any hardware-microphone testing. The build result above is a *build* result, not a claim that every interaction was exercised in a browser.

## 9. Security scan

* No `.env*`, key, certificate or credential-named files (the one filename match, `src/styles/designTokens.css`, is a CSS design-tokens file).
* Content scan of all 240 files (binary files read as text; `.gz` and `.br` artifacts decompressed first) for private keys, AWS/GitHub/OpenAI/Slack/Google/Vercel/Supabase tokens, JWTs and generic `key/secret/password = "…"` assignments: **0 matches** (the scanner was self-tested against a fake token to prove it can detect one).
* `DEPLOYMENT_LATEST.json` contains only public deployment identifiers/URLs, no secret.
* **Please double-check:** the project's own reports (`PROJECT_PROGRESS.md`, `FINAL_QA_REPORT.md`, `GIFT_QA_REPORT.md`, `QA_REPORT.md`) say a Vercel token pasted into a chat during an earlier deployment "must be revoked by the user". No token is in the repository, but make sure that token was revoked in your Vercel account.

## 10. Final repository status (as of preparation)

* Local branch `main` holds **one new commit** on top of `origin/main` @ `ba8d1cd`, message: `Complete project ZIP migration with all source code and assets`. It contains all 240 project files, the preserved source ZIP and this report (242 files). *(A file cannot contain the hash of the commit that contains it; run `git log -1` for the SHA.)*
* **Push status at preparation time: not pushed.** The environment that prepared this commit had read-only GitHub access: `git push` failed with `fatal: could not read Username for 'https://github.com'`, the GitHub REST API answered `Requires authentication`, and no GitHub write connector or credential was available. The commit was therefore handed over as a git bundle (`the-world-of-you-migration.bundle`); pushing it from an authenticated machine is the only remaining step:

```bash
git clone the-world-of-you-migration.bundle the-world-of-you
cd the-world-of-you
git remote set-url origin https://github.com/rambhakt07122007-design/the-world-of-you.git
git push origin main        # fast-forward from ba8d1cd; uploads only the new objects
```

## Appendix A — Final folder structure

```text
the-world-of-you/  (repository root = project root, no extra nesting)  — 242 files
├── docs/  (5 files)
│   ├── source-reference/  (4 files)
│   │   ├── CHRONOS_Master_AI_Execution_Prompt.md
│   │   ├── CHRONOS_Master_AI_Execution_Prompt.pdf
│   │   ├── CHRONOS_Project_Guide.md
│   │   └── CHRONOS_Source_Code_Reference.pdf
│   └── README.md
├── public/  (53 files)
│   ├── assets/  (51 files)
│   │   ├── audio/  (1 file)
│   │   │   └── .gitkeep
│   │   ├── backgrounds/  (1 file)
│   │   │   └── birthday-garden.webp
│   │   ├── birthday/  (1 file)
│   │   │   └── invitation-envelope.webp
│   │   ├── flowers/  (1 file)
│   │   │   └── .gitkeep
│   │   ├── fonts/  (11 files)
│   │   │   ├── README.md
│   │   │   ├── 4 × *.txt   (OFL-Caveat.txt … OFL-Playfair-Display.txt)
│   │   │   └── 6 × *.woff2   (caveat-latin-variable.woff2 … playfair-display-latin-variable.woff2)
│   │   ├── gallery/  (1 file)
│   │   │   └── .gitkeep
│   │   ├── gift-previews/  (17 files)
│   │   │   └── 17 × *.webp   (gift-01.webp … gift-17.webp)
│   │   ├── gifts/  (1 file)
│   │   │   └── .gitkeep
│   │   ├── models/  (8 files)
│   │   │   ├── README.md
│   │   │   ├── cake.glb
│   │   │   ├── crown.glb
│   │   │   ├── eternal-rose.glb
│   │   │   ├── garden.glb
│   │   │   ├── letter-desk.glb
│   │   │   ├── observatory.glb
│   │   │   └── portal.glb
│   │   ├── objects/  (1 file)
│   │   │   └── .gitkeep
│   │   ├── paper/  (1 file)
│   │   │   └── writing-desk.webp
│   │   ├── postcards/  (4 files)
│   │   │   ├── home-whatever-shape.webp
│   │   │   ├── mountain-morning.webp
│   │   │   ├── sea-blue-hour.webp
│   │   │   └── unnamed-city.webp
│   │   └── scenes/  (3 files)
│   │       ├── birthday-ballroom.webp
│   │       ├── invitation-room.webp
│   │       └── memory-observatory.webp
│   └── licenses/  (2 files)
│       ├── REACT-THREE-FIBER-LICENSE.txt
│       └── THREE-LICENSE.txt
├── qa/  (22 files)
│   ├── native-worlds-review.jpg
│   └── 21 × *.png   (live-jar-baseline.png … ultra-jar-mobile.png)
├── scripts/  (8 files)
│   ├── audit-live.mjs
│   ├── check-production.mjs
│   ├── compress-gift-previews.py
│   ├── debug-native.mjs
│   ├── export-models.mjs
│   ├── inspect-jar.mjs
│   ├── preserve-content.py
│   └── render-gift-previews.mjs
├── src/  (49 files)
│   ├── components/  (1 file)
│   │   └── ArchiveDialog.tsx
│   ├── content/  (3 files)
│   │   ├── README.md
│   │   ├── chronosContent.ts
│   │   └── giftsContent.ts
│   ├── hooks/  (1 file)
│   │   └── useBlowDetection.ts
│   ├── scenes/  (2 files)
│   │   ├── SceneExperience.tsx
│   │   └── sceneCatalog.ts
│   ├── styles/  (7 files)
│   │   ├── cinematic.css
│   │   ├── designTokens.css
│   │   ├── giftAtelier.css
│   │   ├── giftWorlds.css
│   │   ├── global.css
│   │   ├── premium.css
│   │   └── sceneSystem.css
│   ├── three/  (16 files)
│   │   ├── 13 × *.ts   (botanicalGift.ts … scenePrimitives.ts)
│   │   └── 3 × *.tsx   (GiftStage.tsx … SceneCanvas.tsx)
│   ├── utils/  (1 file)
│   │   └── time.ts
│   ├── world/  (16 files)
│   │   └── 16 × *.tsx   (BirthdayCake.tsx … WorldSection.tsx)
│   ├── App.tsx
│   └── main.tsx
├── tests/  (10 files)
│   ├── cinematic.spec.ts
│   ├── debug-garden.mjs
│   ├── inspect.mjs
│   ├── letter-refinement.spec.ts
│   ├── native-gifts.spec.ts
│   ├── paper-geometry.spec.ts
│   ├── postcard-refinement.spec.ts
│   ├── ultra-access.spec.ts
│   ├── ultra-gifts.spec.ts
│   └── visual.mjs
├── vercel-upload/  (21 files)
│   ├── deploy-root/  (20 files)
│   │   ├── chunks/  (14 files)
│   │   │   └── 14 × *.txt   (css-0.txt … js-5.txt)
│   │   ├── build-static.js
│   │   ├── index.html
│   │   ├── index.html.br
│   │   ├── index.html.gz
│   │   ├── package-lock.json
│   │   └── package.json
│   └── index.html
├── .gitignore
├── .vercelignore
├── DEPLOYMENT_LATEST.json
├── MIGRATION_REPORT.md
├── README.md
├── The-World-of-You-17-Native-Worlds-Source.zip
├── index.html
├── package-lock.json
├── package.json
├── playwright.config.ts
├── tsconfig.json
├── vite.config.ts
├── 33 more project documents (*.md), e.g. 3D_IMPLEMENTATION_REPORT.md … WEBSITE_AUDIT.md
└── 29 root QA artifacts (qa-*.png / .json / .txt)
```

## Appendix B — Full file inventory

<details><summary>242 files (path · bytes · SHA-256 prefix · migration action)</summary>

| Path | Bytes | SHA-256 (12) | Action |
|---|---:|---|---|
| `.gitignore` | 66 | `b01f2f706bf0` | added |
| `.vercelignore` | 272 | `09e145a21868` | added |
| `3D_IMPLEMENTATION_REPORT.md` | 15,932 | `b30a28e145e3` | added |
| `3D_TRANSFORMATION_AUDIT.md` | 8,850 | `ac0c47b17f2d` | added |
| `ACCESSIBILITY_REPORT.md` | 4,127 | `97c084c81d3d` | added |
| `ANIMATION_AUDIT.md` | 20,899 | `e827992dfc31` | added |
| `ANIMATION_INVENTORY.md` | 20,129 | `5429c0eb5860` | added |
| `ANIMATION_SPECIFICATION.md` | 7,540 | `63a6ea98eb3c` | added |
| `ASSET_GENERATION_BACKLOG.md` | 2,476 | `7aeec1c10f76` | added |
| `ASSET_GENERATION_GUIDE.md` | 7,003 | `80e02b84ad17` | added |
| `ASSET_MANIFEST.md` | 13,319 | `7911e54d979f` | added |
| `AUDIO_IMPLEMENTATION.md` | 3,963 | `7ee437f57284` | added |
| `COMPONENT_INVENTORY.md` | 6,589 | `2039ae0dac91` | added |
| `DEPLOYMENT_LATEST.json` | 698 | `bb40f9efffe9` | added |
| `DESIGN_AUDIT.md` | 7,114 | `9b3f5536bec8` | added |
| `DESIGN_RESEARCH.md` | 7,254 | `2029fc773ac5` | added |
| `DESIGN_SYSTEM.md` | 9,017 | `83aeb4916c38` | added |
| `FINAL_IMPLEMENTATION_REPORT.md` | 15,905 | `6496946ae570` | added |
| `FINAL_QA_REPORT.md` | 10,745 | `713b0da67690` | added |
| `GIFT_ATELIER_SPECIFICATION.md` | 7,819 | `56d9bee104e3` | added |
| `GIFT_CONTENT_GUIDE.md` | 3,479 | `c32c97001c20` | added |
| `GIFT_QA_REPORT.md` | 6,988 | `d4146a6c1a2f` | added |
| `IMPLEMENTATION_CHECKLIST.md` | 6,218 | `9022e74da104` | added |
| `IMPLEMENTATION_PLAN.md` | 1,850 | `4046b71bceb6` | added |
| `IMPLEMENTATION_REPORT.md` | 10,034 | `058707816b0d` | added |
| `MOTION_LANGUAGE.md` | 1,818 | `bf145bc57101` | added |
| `OBSOLETE_GIFT_ART_REMOVAL.md` | 942 | `d99f6462f291` | added |
| `PERFORMANCE_REPORT.md` | 4,846 | `02825a6efb4d` | added |
| `PROJECT_AUDIT.md` | 2,506 | `52463601e9a2` | added |
| `PROJECT_PROGRESS.md` | 20,251 | `05327db7ec55` | added |
| `QA_REPORT.md` | 2,494 | `7da5a11fd44e` | added |
| `README.md` | 8,878 | `8d687cf7a348` | replaced (conflict) |
| `RESEARCH_SOURCES.md` | 17,113 | `eb567fbbd7cf` | added |
| `SCENE_ARCHITECTURE.md` | 8,060 | `29fc207b1b3e` | added |
| `SOURCE_RECONSTRUCTION.md` | 1,520 | `6b76532663c5` | added |
| `START_HERE.md` | 3,343 | `48a3053ad6b3` | added |
| `WEBSITE_AUDIT.md` | 7,772 | `f7901c63b820` | added |
| `docs/README.md` | 1,820 | `dfe869f7e1fd` | added |
| `docs/source-reference/CHRONOS_Master_AI_Execution_Prompt.md` | 20,143 | `8a062f7e0200` | added |
| `docs/source-reference/CHRONOS_Master_AI_Execution_Prompt.pdf` | 45,093 | `99793c343c33` | added |
| `docs/source-reference/CHRONOS_Project_Guide.md` | 14,908 | `e6447d52813b` | added |
| `docs/source-reference/CHRONOS_Source_Code_Reference.pdf` | 233,462 | `47b46cffee18` | added |
| `index.html` | 1,640 | `7d3b62648081` | added |
| `package-lock.json` | 74,535 | `038fa495ced5` | added |
| `package.json` | 860 | `118baabb9512` | added |
| `playwright.config.ts` | 479 | `3e90e57fd012` | added |
| `public/assets/audio/.gitkeep` | 62 | `0393c8885406` | added |
| `public/assets/backgrounds/birthday-garden.webp` | 178,518 | `6a451dc39422` | added |
| `public/assets/birthday/invitation-envelope.webp` | 26,078 | `eedd8d985498` | added |
| `public/assets/flowers/.gitkeep` | 61 | `d6774818349c` | added |
| `public/assets/fonts/OFL-Caveat.txt` | 4,385 | `1f9d81d09427` | added |
| `public/assets/fonts/OFL-Cormorant-Garamond.txt` | 4,387 | `60700d351cac` | added |
| `public/assets/fonts/OFL-DM-Sans.txt` | 4,482 | `9af361903324` | added |
| `public/assets/fonts/OFL-Playfair-Display.txt` | 4,449 | `566be814f8e9` | added |
| `public/assets/fonts/README.md` | 341 | `12cd04a80b63` | added |
| `public/assets/fonts/caveat-latin-variable.woff2` | 74,932 | `891951df5e8b` | added |
| `public/assets/fonts/cormorant-garamond-italic-latin-variable.woff2` | 39,260 | `6f2f5c3b1abc` | added |
| `public/assets/fonts/cormorant-garamond-latin-variable.woff2` | 37,640 | `d80df8ff5aec` | added |
| `public/assets/fonts/dm-sans-latin-variable.woff2` | 36,932 | `9fea608a947e` | added |
| `public/assets/fonts/playfair-display-italic-latin-variable.woff2` | 38,804 | `54af24bd0f91` | added |
| `public/assets/fonts/playfair-display-latin-variable.woff2` | 38,404 | `e0c764a8e9e1` | added |
| `public/assets/gallery/.gitkeep` | 61 | `d6774818349c` | added |
| `public/assets/gift-previews/gift-01.webp` | 4,094 | `7f2409d62293` | added |
| `public/assets/gift-previews/gift-02.webp` | 6,134 | `03b97c3a711d` | added |
| `public/assets/gift-previews/gift-03.webp` | 4,762 | `00ba08a7399d` | added |
| `public/assets/gift-previews/gift-04.webp` | 10,980 | `4dfecd969062` | added |
| `public/assets/gift-previews/gift-05.webp` | 4,500 | `fb49b1ae0e3f` | added |
| `public/assets/gift-previews/gift-06.webp` | 6,998 | `a3f7b1a518bc` | added |
| `public/assets/gift-previews/gift-07.webp` | 6,620 | `543f33cf7f7c` | added |
| `public/assets/gift-previews/gift-08.webp` | 5,162 | `bc9fd27f07dc` | added |
| `public/assets/gift-previews/gift-09.webp` | 3,844 | `3825d5f672d2` | added |
| `public/assets/gift-previews/gift-10.webp` | 5,246 | `b6e76995d154` | added |
| `public/assets/gift-previews/gift-11.webp` | 7,692 | `5a75aa0ad77b` | added |
| `public/assets/gift-previews/gift-12.webp` | 5,216 | `176fac0b144d` | added |
| `public/assets/gift-previews/gift-13.webp` | 5,098 | `5a5f3f61750d` | added |
| `public/assets/gift-previews/gift-14.webp` | 2,442 | `d08a6fea6a47` | added |
| `public/assets/gift-previews/gift-15.webp` | 9,886 | `86596b3aced7` | added |
| `public/assets/gift-previews/gift-16.webp` | 5,292 | `2bbf541af4db` | added |
| `public/assets/gift-previews/gift-17.webp` | 13,472 | `2b890caec2f8` | added |
| `public/assets/gifts/.gitkeep` | 61 | `d6774818349c` | added |
| `public/assets/models/README.md` | 1,247 | `cb8a04003df2` | added |
| `public/assets/models/cake.glb` | 371,836 | `0017fa26cb10` | added |
| `public/assets/models/crown.glb` | 398,944 | `e2c25a87080d` | added |
| `public/assets/models/eternal-rose.glb` | 131,852 | `6e22965c7265` | added |
| `public/assets/models/garden.glb` | 1,541,248 | `25ddea49a0ff` | added |
| `public/assets/models/letter-desk.glb` | 452,160 | `2a97b82e849a` | added |
| `public/assets/models/observatory.glb` | 423,504 | `c6ad1c2168e6` | added |
| `public/assets/models/portal.glb` | 175,348 | `e60c94043b59` | added |
| `public/assets/objects/.gitkeep` | 61 | `d6774818349c` | added |
| `public/assets/paper/writing-desk.webp` | 85,038 | `ea31525d779f` | added |
| `public/assets/postcards/home-whatever-shape.webp` | 219,378 | `eeeebd0e53b2` | added |
| `public/assets/postcards/mountain-morning.webp` | 216,920 | `ccb0fc9683a6` | added |
| `public/assets/postcards/sea-blue-hour.webp` | 213,318 | `affe78d26be7` | added |
| `public/assets/postcards/unnamed-city.webp` | 268,290 | `0c3ac5f3fda1` | added |
| `public/assets/scenes/birthday-ballroom.webp` | 137,760 | `7124900376d2` | added |
| `public/assets/scenes/invitation-room.webp` | 92,786 | `f2b855eaa230` | added |
| `public/assets/scenes/memory-observatory.webp` | 70,780 | `086896302f1c` | added |
| `public/licenses/REACT-THREE-FIBER-LICENSE.txt` | 1,072 | `9c35b5de7b74` | added |
| `public/licenses/THREE-LICENSE.txt` | 1,081 | `8b378ebe60e2` | added |
| `qa-cake-render.png` | 81,018 | `974b07c7259f` | added |
| `qa-garden-desktop.png` | 553,373 | `402ee2e80792` | added |
| `qa-garden-focused.png` | 338,249 | `236b0b105619` | added |
| `qa-garden-render.png` | 441,247 | `efce96b69d70` | added |
| `qa-jar-inspection.json` | 497 | `ca7a623ec4e5` | added |
| `qa-letter-preservation.json` | 153 | `0a12aaad3d4f` | added |
| `qa-live-audit.json` | 9,466 | `7481173076b3` | added |
| `qa-models.json` | 577 | `b8df266c9794` | added |
| `qa-native-gifts.txt` | 405 | `b27f14afc50a` | added |
| `qa-preservation.json` | 50 | `ea201e5c19cc` | added |
| `qa-production.json` | 311 | `3d36910788c8` | added |
| `qa-refinement-build.txt` | 1,056 | `fe7e172c11d7` | added |
| `qa-refinement-final.txt` | 820 | `770385e8ff94` | added |
| `qa-refinement-geometry-mobile.txt` | 303 | `794c9217746f` | added |
| `qa-refinement-initial.json` | 24,755 | `c1eeb5a4a1d7` | added |
| `qa-refinement-regression.txt` | 3,306 | `fcd4f1fcfca0` | added |
| `qa-results.json` | 24,755 | `c1eeb5a4a1d7` | added |
| `qa-ultra-audit.txt` | 24 | `6d8c5c8f3d76` | added |
| `qa-ultra-build.txt` | 1,221 | `e8a0cd24b159` | added |
| `qa-ultra-core-final.txt` | 651 | `b16ded23a433` | added |
| `qa-ultra-focused-final.txt` | 1,836 | `f2bd23db0f08` | added |
| `qa-ultra-gifts.txt` | 2,460 | `0ec83cd6d8b1` | added |
| `qa-ultra-mic-fallback.txt` | 1,951 | `d308ceadad92` | added |
| `qa-ultra-mic-final.txt` | 204 | `070f528a54d3` | added |
| `qa-ultra-mic-rerun.txt` | 2,177 | `a0cb8f599184` | added |
| `qa-ultra-preservation.json` | 317 | `dda8ed0068ab` | added |
| `qa-ultra-preview-assets.json` | 1,135 | `7329d4596b37` | added |
| `qa-ultra-production-preview.json` | 160 | `fe5e54dd2fc0` | added |
| `qa-ultra-regression.txt` | 729 | `0d95b8786059` | added |
| `qa/live-jar-baseline.png` | 412,673 | `e423f82a0bc3` | added |
| `qa/native-jar-new.png` | 197,379 | `728aec6e5d6e` | added |
| `qa/native-worlds-review.jpg` | 140,424 | `08b3ef0c106b` | added |
| `qa/ultra-gift-01.png` | 206,429 | `5bfd8621fb34` | added |
| `qa/ultra-gift-02.png` | 263,436 | `f6a63d634c11` | added |
| `qa/ultra-gift-03.png` | 149,324 | `16185a2a7d47` | added |
| `qa/ultra-gift-04.png` | 220,293 | `b9a08cb83fcd` | added |
| `qa/ultra-gift-05.png` | 210,217 | `8cf33d743821` | added |
| `qa/ultra-gift-06.png` | 228,947 | `f90219cd023a` | added |
| `qa/ultra-gift-07.png` | 239,184 | `46a1a7864fa7` | added |
| `qa/ultra-gift-08.png` | 111,063 | `11108f8cfbd3` | added |
| `qa/ultra-gift-09.png` | 323,825 | `998d4e84478d` | added |
| `qa/ultra-gift-10.png` | 204,067 | `9ab815eab7f4` | added |
| `qa/ultra-gift-11.png` | 291,357 | `b73895c46b7e` | added |
| `qa/ultra-gift-12.png` | 234,449 | `7b35e8aee64d` | added |
| `qa/ultra-gift-13.png` | 261,854 | `584b8f0af073` | added |
| `qa/ultra-gift-14.png` | 298,787 | `1a783ef631cd` | added |
| `qa/ultra-gift-15.png` | 297,869 | `f3b622f1a98d` | added |
| `qa/ultra-gift-16.png` | 331,852 | `61c67e6985c1` | added |
| `qa/ultra-gift-17.png` | 326,804 | `c0ab5d0280be` | added |
| `qa/ultra-jar-high.png` | 259,138 | `801afd90a979` | added |
| `qa/ultra-jar-mobile.png` | 107,169 | `3ed8dbb06e9b` | added |
| `scripts/audit-live.mjs` | 1,484 | `98d472bf6005` | added |
| `scripts/check-production.mjs` | 1,542 | `2d4d8093e159` | added |
| `scripts/compress-gift-previews.py` | 211 | `5159106f3f72` | added |
| `scripts/debug-native.mjs` | 884 | `26aa01ec1d3f` | added |
| `scripts/export-models.mjs` | 1,271 | `8b2d4681acbc` | added |
| `scripts/inspect-jar.mjs` | 1,258 | `239262445d1e` | added |
| `scripts/preserve-content.py` | 444 | `365072552bdd` | added |
| `scripts/render-gift-previews.mjs` | 1,059 | `bbb87ceebb96` | added |
| `src/App.tsx` | 5,885 | `aeb03c930293` | added |
| `src/components/ArchiveDialog.tsx` | 1,581 | `50d576be0e6d` | added |
| `src/content/README.md` | 1,069 | `0ad9f3b4beb2` | added |
| `src/content/chronosContent.ts` | 14,296 | `15377da72d5e` | added |
| `src/content/giftsContent.ts` | 7,171 | `242b5c41351c` | added |
| `src/hooks/useBlowDetection.ts` | 5,255 | `57478159b636` | added |
| `src/main.tsx` | 415 | `ac69eba0ae42` | added |
| `src/scenes/SceneExperience.tsx` | 8,709 | `07199e39e0d0` | added |
| `src/scenes/sceneCatalog.ts` | 3,176 | `6bb6fe977286` | added |
| `src/styles/cinematic.css` | 6,001 | `97bd114d23ed` | added |
| `src/styles/designTokens.css` | 3,410 | `3702fc9dbed0` | added |
| `src/styles/giftAtelier.css` | 33,840 | `aae6bf7cec53` | added |
| `src/styles/giftWorlds.css` | 5,124 | `63f8e727332c` | added |
| `src/styles/global.css` | 95,522 | `c396470eb18f` | added |
| `src/styles/premium.css` | 39,963 | `feecea12e2c5` | added |
| `src/styles/sceneSystem.css` | 18,685 | `b38772d801dc` | added |
| `src/three/GiftStage.tsx` | 1,107 | `dd03a09e9b06` | added |
| `src/three/NativeGiftCanvas.tsx` | 7,221 | `5d09ced19f34` | added |
| `src/three/SceneCanvas.tsx` | 4,153 | `ed7767b43544` | added |
| `src/three/botanicalGift.ts` | 7,185 | `0ea36ae51c27` | added |
| `src/three/cake.ts` | 9,705 | `760a06da09ee` | added |
| `src/three/celestial.ts` | 5,265 | `5e5c9ed75200` | added |
| `src/three/disposeTree.ts` | 593 | `34f279c5eb24` | added |
| `src/three/exportModels.ts` | 2,175 | `5f4761067346` | added |
| `src/three/garden.ts` | 11,152 | `128adbe3568e` | added |
| `src/three/giftFactory.ts` | 749 | `ae883f9ab495` | added |
| `src/three/giftWorlds.ts` | 26,510 | `ff5bd9873174` | added |
| `src/three/letter.ts` | 9,714 | `a914676a1781` | added |
| `src/three/postcard.ts` | 2,810 | `7b7dc573da73` | added |
| `src/three/previewGiftModels.ts` | 1,727 | `aaa42f73c52f` | added |
| `src/three/runtime.ts` | 6,903 | `9b02cb7966cd` | added |
| `src/three/scenePrimitives.ts` | 1,236 | `a434b1e14dc2` | added |
| `src/utils/time.ts` | 2,272 | `934c399dea46` | added |
| `src/world/BirthdayCake.tsx` | 14,734 | `a60523137af7` | added |
| `src/world/BirthdayGarden.tsx` | 3,338 | `f32f6f30b3b8` | added |
| `src/world/CakeBakingJourney.tsx` | 12,632 | `4283af251e69` | added |
| `src/world/FinalCelebration.tsx` | 4,372 | `89bd99e4ce29` | added |
| `src/world/FlowerGarden.tsx` | 3,607 | `c0e59c6a74e3` | added |
| `src/world/FuturePostcards.tsx` | 3,663 | `68e8a70ec852` | added |
| `src/world/GiftExperiences.tsx` | 51,650 | `0f88d27a2043` | added |
| `src/world/GiftRoom.tsx` | 5,336 | `2be812cb2676` | added |
| `src/world/LetterRoom.tsx` | 6,929 | `a1e369f31f9e` | added |
| `src/world/MusicRoom.tsx` | 7,218 | `2220639a8dc8` | added |
| `src/world/OpeningInvitation.tsx` | 5,414 | `4841743767d6` | added |
| `src/world/PolaroidGallery.tsx` | 3,601 | `79a2bb3bf33f` | added |
| `src/world/RelationshipClock.tsx` | 4,294 | `2919d48a20df` | added |
| `src/world/Storybook.tsx` | 12,854 | `41ad7182332c` | added |
| `src/world/WorldNav.tsx` | 4,261 | `4143b4f52d6f` | added |
| `src/world/WorldSection.tsx` | 1,527 | `888ea854b899` | added |
| `tests/cinematic.spec.ts` | 13,032 | `fba0be5efca2` | added |
| `tests/debug-garden.mjs` | 900 | `7f34d27b013e` | added |
| `tests/inspect.mjs` | 896 | `ec64b9275729` | added |
| `tests/letter-refinement.spec.ts` | 4,286 | `688e38835058` | added |
| `tests/native-gifts.spec.ts` | 1,952 | `aec9039ff2d9` | added |
| `tests/paper-geometry.spec.ts` | 1,221 | `e74fcced5744` | added |
| `tests/postcard-refinement.spec.ts` | 1,449 | `1a4746930e7e` | added |
| `tests/ultra-access.spec.ts` | 3,594 | `e95fd08bed97` | added |
| `tests/ultra-gifts.spec.ts` | 4,045 | `5b4596d2b6ef` | added |
| `tests/visual.mjs` | 751 | `8700fb32a333` | added |
| `tsconfig.json` | 508 | `16a39c6cf00c` | added |
| `vercel-upload/deploy-root/build-static.js` | 422 | `4a4f48143d73` | added |
| `vercel-upload/deploy-root/chunks/css-0.txt` | 20,000 | `4fab7ffa9414` | added |
| `vercel-upload/deploy-root/chunks/css-1.txt` | 5,300 | `9029b45a4412` | added |
| `vercel-upload/deploy-root/chunks/desk-0.txt` | 20,000 | `16ff987d1b7e` | added |
| `vercel-upload/deploy-root/chunks/desk-1.txt` | 11,732 | `c0fc53490dd6` | added |
| `vercel-upload/deploy-root/chunks/garden-0.txt` | 20,000 | `dada962479c2` | added |
| `vercel-upload/deploy-root/chunks/garden-1.txt` | 20,000 | `619221012224` | added |
| `vercel-upload/deploy-root/chunks/garden-2.txt` | 6,232 | `3aee52b5ed3c` | added |
| `vercel-upload/deploy-root/chunks/invitation-0.txt` | 10,344 | `700a33732ea6` | added |
| `vercel-upload/deploy-root/chunks/js-0.txt` | 20,000 | `67b9623c2690` | added |
| `vercel-upload/deploy-root/chunks/js-1.txt` | 20,000 | `055607a0f59c` | added |
| `vercel-upload/deploy-root/chunks/js-2.txt` | 20,000 | `6f87acb9afef` | added |
| `vercel-upload/deploy-root/chunks/js-3.txt` | 20,000 | `f52313167b7f` | added |
| `vercel-upload/deploy-root/chunks/js-4.txt` | 20,000 | `72eb090f5c4c` | added |
| `vercel-upload/deploy-root/chunks/js-5.txt` | 9,980 | `83e59b60fca5` | added |
| `vercel-upload/deploy-root/index.html` | 2,723 | `7352f2262b78` | added |
| `vercel-upload/deploy-root/index.html.br` | 168,550 | `01606d88b574` | added |
| `vercel-upload/deploy-root/index.html.gz` | 170,570 | `6812dcbfb835` | added |
| `vercel-upload/deploy-root/package-lock.json` | 143 | `330da155df56` | added |
| `vercel-upload/deploy-root/package.json` | 103 | `158626d6eec6` | added |
| `vercel-upload/index.html` | 225,738 | `be655fe49e62` | added |
| `vite.config.ts` | 261 | `de37f36a3a59` | added |
| `The-World-of-You-17-Native-Worlds-Source.zip` | 10,737,226 | `fbf2257a89b8` | preserved (existing, not in ZIP) |
| `MIGRATION_REPORT.md` | — | — | new (this file) |

</details>
