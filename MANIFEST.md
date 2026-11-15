# THE WORLD OF YOU — code manifest

Generated 2026-11-13 from git commit `e8a2e9e` (everything that changed after the migration commit `0f16a01`).

**108 code files** (12,668 lines), 10 files deleted, plus 14 documents (`docs/`, the content pack, the reports) and 20 changed binary assets under `public/` (gift posters, postcard illustrations).

| # | Status | File | Lines | What it is |
|---|---|---|---:|---|
| 1 | MODIFIED | `GIFT_CONTENT_GUIDE.md` | 68 | Gift Content Guide |
| 2 | MODIFIED | `README.md` | 115 | The World of You |
| 3 | MODIFIED | `playwright.config.ts` | 18 | QA_SLOW=1 multiplies timeouts for software WebGL (SwiftShader) where a scene needs 20-30 s to compile its first frame. |
| 4 | NEW | `scripts/content-pack/build-pack-content.py` | 355 | One-time importer for the owner's PDF "The World of You — Complete Missing Content Pack". |
| 5 | NEW | `scripts/make-asset-inventory.py` | 94 | Regenerates docs/ASSET_INVENTORY.md from the real files (public/, node_modules licences, src/engine and src/three). |
| 6 | NEW | `scripts/make-export.py` | 133 | Builds the code export of everything that changed since the migration commit, straight from git (never from the working tree): |
| 7 | NEW | `scripts/make-reports.py` | 609 | Builds the QA / audit reports in docs/ from the recorded test output, so every number in them comes from a file, not from memory. |
| 8 | NEW | `scripts/qa/README.md` | 30 | QA tooling |
| 9 | NEW | `scripts/qa/capture.mjs` | 70 | Capture every site section and every gift experience in a real browser. |
| 10 | NEW | `scripts/qa/check-pack-live.mjs` | 87 | Looks up every string of the owner's content pack (src/content/packContent.ts) in the JavaScript a deployed site serves. |
| 11 | NEW | `scripts/qa/compare-live-dist.mjs` | 48 | Compares every file of the local production build (dist/) with what a deployed site serves, byte for byte (sha256). |
| 12 | NEW | `scripts/qa/contact_sheet.py` | 17 | Tile screenshots into one labelled contact sheet.  usage: contact_sheet.py out.png cols cellW img1 img2 ... |
| 13 | NEW | `scripts/qa/dom-probe.mjs` | 18 | Prints geometry and key computed styles for selectors on the live page.  usage: node scripts/qa/dom-probe.mjs "<url path>" "<sel1>" "<sel2>" ... [--w= |
| 14 | NEW | `scripts/qa/gift-flow.mjs` | 101 | End-to-end flow for ONE gift dialog: open -> layout metrics -> real interactions -> keyboard close -> leak check. |
| 15 | NEW | `scripts/qa/keyboard-pass.mjs` | 118 | Keyboard-only pass: hero growth steps (Tab / Enter) and a gift dialog (Enter opens, focus stays inside, Escape closes, focus returns). |
| 16 | NEW | `scripts/qa/lab-shot.mjs` | 46 | Deterministic screenshots of one scene in the dev-only lab (http://localhost:4181/?lab=<kind>). |
| 17 | NEW | `scripts/qa/leak-check.mjs` | 53 | GPU / memory leak check: opens and closes one gift dialog several times and verifies that every WebGL context that was created |
| 18 | NEW | `scripts/qa/lib.mjs` | 47 | Shared helpers for the browser QA scripts (visual capture, interaction checks, leak checks). |
| 19 | NEW | `scripts/qa/pack-hero-stages.mjs` | 40 | Content-pack capture: walks the seven Birthday Garden growth stages (Seed ... Full bloom), screenshots each once it has settled and prints |
| 20 | NEW | `scripts/qa/pack-letters.mjs` | 42 | Content-pack capture: the Letter Room shelf (six envelopes), the main letter folded, open and scrolled to its end, and an empty envelope. |
| 21 | NEW | `scripts/qa/pack-postcards.mjs` | 44 | Content-pack capture: opens Future Postcards, flips each card to its reverse and back to the illustration, screenshots both sides and |
| 22 | NEW | `scripts/qa/pack-scrapbook.mjs` | 43 | Content-pack capture: the Scrapbook's owner slots. Turns the book through its spreads, screenshots each one and prints the text of every |
| 23 | NEW | `scripts/qa/prod-smoke.mjs` | 127 | Production smoke test against the BUILT site (vite preview of dist/), not the dev server. It checks: |
| 24 | NEW | `scripts/qa/render-previews.mjs` | 31 | Renders the 17 Gift Atelier preview posters (480x360) from the REAL native scenes in their finished state, |
| 25 | NEW | `scripts/qa/run-each.sh` | 10 | Run capture.mjs once per gift in its own process/browser so a renderer crash cannot take the whole run down. |
| 26 | NEW | `scripts/qa/run-flows.sh` | 14 | Runs scripts/qa/gift-flow.mjs for gifts FROM..TO (default 1..17), one fresh Chromium per gift. Appends one JSON line per gift to <out>/summary.jsonl. |
| 27 | NEW | `scripts/qa/run-list.sh` | 11 | Runs gift-flow.mjs for an explicit list of gifts, one fresh Chromium each.  usage: scripts/qa/run-list.sh <outDir> "<flags>" 01 02 03 ... |
| 28 | NEW | `scripts/qa/run-specs.py` | 39 | Runs the Playwright specs one test per process (a fresh Chromium each time: the sandbox's single-process Chromium cannot |
| 29 | NEW | `scripts/qa/section-shot.mjs` | 33 | Screenshots one page section once its 3D scene (if any) reports ready. |
| 30 | MODIFIED | `src/App.tsx` | 136 | exports App |
| 31 | MODIFIED | `src/components/ArchiveDialog.tsx` | 49 | exports ArchiveDialog |
| 32 | MODIFIED | `src/content/README.md` | 15 | Editable birthday-storybook content |
| 33 | MODIFIED | `src/content/chronosContent.ts` | 287 | exports WorldSectionId |
| 34 | MODIFIED | `src/content/giftsContent.ts` | 125 | Gift Atelier catalog and owner-editable copy slots. |
| 35 | NEW | `src/content/packContent.ts` | 473 | THE WORLD OF YOU — COMPLETE MISSING CONTENT PACK. Owner-supplied PDF (docs/content-pack/), transcribed verbatim by |
| 36 | NEW | `src/engine/anim.ts` | 52 | A reversible, scrubbable GSAP timeline whose playhead follows a target (0 = closed, 1 = open). |
| 37 | NEW | `src/engine/audio.ts` | 186 | Web Audio sound design. |
| 38 | NEW | `src/engine/dispose.ts` | 27 | Releases every GPU resource reachable from `root`: geometries, materials, every texture slot of every |
| 39 | NEW | `src/engine/environment.ts` | 106 | Image-based lighting without any HDR files: a small procedural "studio" (gradient dome + emissive softboxes) |
| 40 | NEW | `src/engine/fx.ts` | 264 | GPU-driven effects. Positions are computed in vertex shaders from a time uniform, so thousands of particles |
| 41 | NEW | `src/engine/garden.ts` | 275 | Botanical building blocks shared by every garden-like scene (Everlasting Flower, Future Garden, Wish Garden, hero meadow): |
| 42 | NEW | `src/engine/geometry.ts` | 150 | Reusable procedural geometry for the gift worlds. Everything is generated, nothing is loaded from disk. |
| 43 | NEW | `src/engine/lights.ts` | 112 | Renderer configuration, lighting presets and cheap fake shadows. |
| 44 | NEW | `src/engine/materials.ts` | 130 | Shared material system. One MaterialKit per scene: it builds PBR materials from the procedural textures and |
| 45 | NEW | `src/engine/paper.ts` | 83 | exports FoldedPaper |
| 46 | NEW | `src/engine/quality.ts` | 91 | Device capability tiers and adaptive resolution. |
| 47 | NEW | `src/engine/stage.ts` | 115 | Everything a gift/scene builder receives besides raw three.js objects: shared materials, mood presets, |
| 48 | NEW | `src/engine/textures.ts` | 230 | Procedural texture library. Every texture is generated at runtime from a 2D canvas, so the site ships no |
| 49 | NEW | `src/hooks/usePointerParallax.ts` | 33 | Publishes the pointer position over an element as CSS variables (--px / --py in -1..1, --gx / --gy in 0..100%) so pure CSS can |
| 50 | NEW | `src/lab/Lab.tsx` | 75 | Scene lab (development only). Mounts a single gift scene full-viewport and exposes `window.__lab` so |
| 51 | MODIFIED | `src/main.tsx` | 22 | Development-only scene lab (?lab=<kind>): mounts one 3D scene on its own for deterministic screenshots. |
| 52 | MODIFIED | `src/styles/giftWorlds.css` | 98 | Focused miniature worlds: one lazy R3F renderer, real objects; HTML remains the instrument panel. |
| 53 | NEW | `src/styles/sections3d.css` | 140 | ========================================================================================================== |
| 54 | MODIFIED | `src/three/GiftStage.tsx` | 75 | exports GiftStageProps |
| 55 | MODIFIED | `src/three/NativeGiftCanvas.tsx` | 199 | exports NativeGiftCanvas |
| 56 | NEW | `src/three/SectionStage.tsx` | 43 | exports SectionStageProps |
| 57 | MODIFIED | `src/three/exportModels.ts` | 37 | Offline authoring entry used by scripts/export-models.mjs, never imported by the app. |
| 58 | MODIFIED | `src/three/giftFactory.ts` | 54 | exports Builder |
| 59 | NEW | `src/three/gifts/adventure.ts` | 136 | Gift 11 - Little Adventure. |
| 60 | NEW | `src/three/gifts/cabinet.ts` | 125 | Gift 09 - Open When... |
| 61 | NEW | `src/three/gifts/cassette.ts` | 177 | Gift 05 - Bhumi FM. |
| 62 | NEW | `src/three/gifts/cinema.ts` | 163 | Gift 06 - The Memory Cinema. |
| 63 | NEW | `src/three/gifts/common.ts` | 78 | Small helpers shared by several gift scenes. |
| 64 | NEW | `src/three/gifts/coupons.ts` | 126 | Gift 14 - Coupon Book. |
| 65 | NEW | `src/three/gifts/crown.ts` | 149 | Gift 08 - The Queen's Crown. |
| 66 | NEW | `src/three/gifts/envelope.ts` | 24 | exports makeEnvelope |
| 67 | NEW | `src/three/gifts/flower.ts` | 188 | Gift 03 - The Flower That Never Fades. |
| 68 | NEW | `src/three/gifts/hopeTree.ts` | 122 | Gift 15 - Future Garden. |
| 69 | NEW | `src/three/gifts/jar.ts` | 234 | Gift 02 - A Jar of Reasons. |
| 70 | NEW | `src/three/gifts/letter.ts` | 363 | Gift 01 - The Secret Letter. |
| 71 | NEW | `src/three/gifts/machine.ts` | 191 | Gift 10 - Happiness Machine. |
| 72 | NEW | `src/three/gifts/mirror.ts` | 115 | Gift 13 - Infinite Mirror. |
| 73 | NEW | `src/three/gifts/portal.ts` | 104 | Gift 17 - The Ultimate Surprise. |
| 74 | NEW | `src/three/gifts/treasure.ts` | 149 | Gift 16 - Secret Treasure Hunt. |
| 75 | NEW | `src/three/gifts/universe.ts` | 161 | Gift 04 - Our Little Universe. |
| 76 | NEW | `src/three/gifts/vinyl.ts` | 161 | Gift 12 - The Music of Us. |
| 77 | NEW | `src/three/gifts/wishes.ts` | 148 | Gift 07 - A Thousand Wishes. |
| 78 | NEW | `src/three/kinds.ts` | 16 | Scene identifiers. |
| 79 | MODIFIED | `src/three/previewGiftModels.ts` | 22 | Offline authoring endpoint: never imported by the application. |
| 80 | MODIFIED | `src/three/runtime.ts` | 24 | exports SceneState |
| 81 | NEW | `src/three/sections/ballroom.ts` | 217 | Birthday Ballroom: the baking story (ingredients -> mixing -> oven) ends in a three-tier cake under a crystal chandelier. |
| 82 | NEW | `src/three/sections/heroGarden.ts` | 11 | Birthday Garden hero: the living cut-away garden (soil strata, seed, roots, sprout, leaves, bud, full bloom) behind the page headline. |
| 83 | NEW | `src/three/sections/observatory.ts` | 235 | Memory Observatory: a brass astronomical clock in a night dome. The hands show the visitor's real local time, a train of |
| 84 | NEW | `src/three/sections/postcards.ts` | 186 | Future Postcards: one thick, glossy postcard lying on a lamp-lit writing desk. |
| 85 | NEW | `src/three/sections/wishGarden.ts` | 234 | Wish Garden: a conservatory diorama with ten flowers (rose, daisy, tulip, ...), one per wish already written in the archive. |
| 86 | NEW | `src/vite-env.d.ts` | 1 | <reference types="vite/client" /> |
| 87 | MODIFIED | `src/world/BirthdayCake.tsx` | 184 | exports BirthdayCake |
| 88 | MODIFIED | `src/world/BirthdayGarden.tsx` | 100 | Growth stages of the living garden, one per narration of the content pack (seed, roots, sprout, leaves, bud, flower, full bloom). |
| 89 | MODIFIED | `src/world/FinalCelebration.tsx` | 78 | exports FinalCelebration |
| 90 | MODIFIED | `src/world/FlowerGarden.tsx` | 30 | exports FlowerGarden |
| 91 | MODIFIED | `src/world/FuturePostcards.tsx` | 49 | exports FuturePostcards |
| 92 | MODIFIED | `src/world/GiftExperiences.tsx` | 818 | exports GiftExperience |
| 93 | MODIFIED | `src/world/GiftRoom.tsx` | 95 | exports GiftRoom |
| 94 | MODIFIED | `src/world/LetterRoom.tsx` | 85 | exports LetterRoom |
| 95 | MODIFIED | `src/world/MusicRoom.tsx` | 112 | exports MusicRoom |
| 96 | MODIFIED | `src/world/PolaroidGallery.tsx` | 60 | exports PolaroidGallery |
| 97 | MODIFIED | `src/world/RelationshipClock.tsx` | 56 | exports RelationshipClock |
| 98 | MODIFIED | `src/world/Storybook.tsx` | 316 | exports Storybook |
| 99 | MODIFIED | `tests/cinematic.spec.ts` | 176 | Software WebGL starves the main thread; QA_SLOW=1 stretches the explicit waits that depend on real-time audio analysis. |
| 100 | NEW | `tests/content-pack-verbatim.spec.ts` | 98 | Integration audit for the owner's content pack (docs/content-pack/). No browser: it compares src/content/packContent.ts with the |
| 101 | NEW | `tests/content-pack.spec.ts` | 274 | The content pack as a visitor meets it. These checks read text and controls, not pixels, so WebGL is switched off: every scene |
| 102 | MODIFIED | `tests/letter-refinement.spec.ts` | 20 | tests, the first: letter reduced motion: open, close, replay, skip and focus return |
| 103 | MODIFIED | `tests/native-gifts.spec.ts` | 18 | tests, the first: ${title}: native mesh renders and original controls remain usable |
| 104 | MODIFIED | `tests/paper-geometry.spec.ts` | 10 | tests, the first: paper geometry: closed thickness surface, rounded crease transport and stable width |
| 105 | MODIFIED | `tests/postcard-refinement.spec.ts` | 4 | tests, the first: native postcards: flip, navigation, original caption and cleanup at ${width} |
| 106 | NEW | `tests/scrapbook-layout.spec.ts` | 49 | The Scrapbook's decorative leather body, page blocks and spine follow the flip book's real orientation: one page on a phone, |
| 107 | MODIFIED | `tests/ultra-access.spec.ts` | 13 | tests, the first: gift WebGL failure: original secret letter remains available by Skip |
| 108 | MODIFIED | `tests/ultra-gifts.spec.ts` | 20 | tests, the first: gift ${index+1}: ${kind} native world, primary action, replay and cleanup |

## Deleted (remove these from your copy)

* `src/three/SceneCanvas.tsx`
* `src/three/botanicalGift.ts`
* `src/three/cake.ts`
* `src/three/celestial.ts`
* `src/three/disposeTree.ts`
* `src/three/garden.ts`
* `src/three/giftWorlds.ts`
* `src/three/letter.ts`
* `src/three/postcard.ts`
* `src/three/scenePrimitives.ts`
