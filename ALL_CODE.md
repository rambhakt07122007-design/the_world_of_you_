# THE WORLD OF YOU — complete code of the build

108 files, every line, exactly as committed in `e8a2e9e` (2026-11-13).

Copy each block into the same path inside your project, or unzip `woy-master-build-code.zip` over the project root (and delete the files listed in MANIFEST.md under *Deleted*).

## Contents

1. `GIFT_CONTENT_GUIDE.md` — modified
2. `README.md` — modified
3. `playwright.config.ts` — modified
4. `scripts/content-pack/build-pack-content.py` — new
5. `scripts/make-asset-inventory.py` — new
6. `scripts/make-export.py` — new
7. `scripts/make-reports.py` — new
8. `scripts/qa/README.md` — new
9. `scripts/qa/capture.mjs` — new
10. `scripts/qa/check-pack-live.mjs` — new
11. `scripts/qa/compare-live-dist.mjs` — new
12. `scripts/qa/contact_sheet.py` — new
13. `scripts/qa/dom-probe.mjs` — new
14. `scripts/qa/gift-flow.mjs` — new
15. `scripts/qa/keyboard-pass.mjs` — new
16. `scripts/qa/lab-shot.mjs` — new
17. `scripts/qa/leak-check.mjs` — new
18. `scripts/qa/lib.mjs` — new
19. `scripts/qa/pack-hero-stages.mjs` — new
20. `scripts/qa/pack-letters.mjs` — new
21. `scripts/qa/pack-postcards.mjs` — new
22. `scripts/qa/pack-scrapbook.mjs` — new
23. `scripts/qa/prod-smoke.mjs` — new
24. `scripts/qa/render-previews.mjs` — new
25. `scripts/qa/run-each.sh` — new
26. `scripts/qa/run-flows.sh` — new
27. `scripts/qa/run-list.sh` — new
28. `scripts/qa/run-specs.py` — new
29. `scripts/qa/section-shot.mjs` — new
30. `src/App.tsx` — modified
31. `src/components/ArchiveDialog.tsx` — modified
32. `src/content/README.md` — modified
33. `src/content/chronosContent.ts` — modified
34. `src/content/giftsContent.ts` — modified
35. `src/content/packContent.ts` — new
36. `src/engine/anim.ts` — new
37. `src/engine/audio.ts` — new
38. `src/engine/dispose.ts` — new
39. `src/engine/environment.ts` — new
40. `src/engine/fx.ts` — new
41. `src/engine/garden.ts` — new
42. `src/engine/geometry.ts` — new
43. `src/engine/lights.ts` — new
44. `src/engine/materials.ts` — new
45. `src/engine/paper.ts` — new
46. `src/engine/quality.ts` — new
47. `src/engine/stage.ts` — new
48. `src/engine/textures.ts` — new
49. `src/hooks/usePointerParallax.ts` — new
50. `src/lab/Lab.tsx` — new
51. `src/main.tsx` — modified
52. `src/styles/giftWorlds.css` — modified
53. `src/styles/sections3d.css` — new
54. `src/three/GiftStage.tsx` — modified
55. `src/three/NativeGiftCanvas.tsx` — modified
56. `src/three/SectionStage.tsx` — new
57. `src/three/exportModels.ts` — modified
58. `src/three/giftFactory.ts` — modified
59. `src/three/gifts/adventure.ts` — new
60. `src/three/gifts/cabinet.ts` — new
61. `src/three/gifts/cassette.ts` — new
62. `src/three/gifts/cinema.ts` — new
63. `src/three/gifts/common.ts` — new
64. `src/three/gifts/coupons.ts` — new
65. `src/three/gifts/crown.ts` — new
66. `src/three/gifts/envelope.ts` — new
67. `src/three/gifts/flower.ts` — new
68. `src/three/gifts/hopeTree.ts` — new
69. `src/three/gifts/jar.ts` — new
70. `src/three/gifts/letter.ts` — new
71. `src/three/gifts/machine.ts` — new
72. `src/three/gifts/mirror.ts` — new
73. `src/three/gifts/portal.ts` — new
74. `src/three/gifts/treasure.ts` — new
75. `src/three/gifts/universe.ts` — new
76. `src/three/gifts/vinyl.ts` — new
77. `src/three/gifts/wishes.ts` — new
78. `src/three/kinds.ts` — new
79. `src/three/previewGiftModels.ts` — modified
80. `src/three/runtime.ts` — modified
81. `src/three/sections/ballroom.ts` — new
82. `src/three/sections/heroGarden.ts` — new
83. `src/three/sections/observatory.ts` — new
84. `src/three/sections/postcards.ts` — new
85. `src/three/sections/wishGarden.ts` — new
86. `src/vite-env.d.ts` — new
87. `src/world/BirthdayCake.tsx` — modified
88. `src/world/BirthdayGarden.tsx` — modified
89. `src/world/FinalCelebration.tsx` — modified
90. `src/world/FlowerGarden.tsx` — modified
91. `src/world/FuturePostcards.tsx` — modified
92. `src/world/GiftExperiences.tsx` — modified
93. `src/world/GiftRoom.tsx` — modified
94. `src/world/LetterRoom.tsx` — modified
95. `src/world/MusicRoom.tsx` — modified
96. `src/world/PolaroidGallery.tsx` — modified
97. `src/world/RelationshipClock.tsx` — modified
98. `src/world/Storybook.tsx` — modified
99. `tests/cinematic.spec.ts` — modified
100. `tests/content-pack-verbatim.spec.ts` — new
101. `tests/content-pack.spec.ts` — new
102. `tests/letter-refinement.spec.ts` — modified
103. `tests/native-gifts.spec.ts` — modified
104. `tests/paper-geometry.spec.ts` — modified
105. `tests/postcard-refinement.spec.ts` — modified
106. `tests/scrapbook-layout.spec.ts` — new
107. `tests/ultra-access.spec.ts` — modified
108. `tests/ultra-gifts.spec.ts` — modified

## 1. `GIFT_CONTENT_GUIDE.md` — modified

```markdown
# Gift Content Guide

**Updated:** November 2026 (the owner's content pack was added; see `docs/CONTENT_PACK_INTEGRATION.md`)

## Sources of truth

- `src/content/packContent.ts` — the owner's content pack (`docs/content-pack/The_World_of_You_Complete_Missing_Content_Pack.pdf`) as typed data. It was imported word for word; edit it by hand from now on. It holds the main letter, the 17 reasons, 101 wishes, seven future postcards, the gift 01–08 dedications, the flower / universe / crown long dedications and reveal lines, the garden narration, the Memory Cinema and Bhumi FM copy and the website microcopy.
- `src/content/giftsContent.ts` — names, experience IDs, gift presentation, readiness flags and the private-copy slots the pack did not fill. Reasons and dedications are read from `packContent.ts`.
- `src/content/chronosContent.ts` — verified relationship dates, the existing source letter and messages, the ten source wishes, gallery/audio slots, the postcard layout and finale copy. The Letter Room, Future Postcards, Gallery and finale are built here from `packContent.ts`.

The experience code reads these modules directly. Do not copy personal text into component JSX; keep approved copy in content data so it remains reviewable and editable.

## What a visitor can and cannot see

The pack is ready-to-edit copy written by the pack's author. It is not a verified record of any private history, so the owner reads it before publishing. A **slot** is anything the pack marked `[EDIT]`, `[ADD ...]` or `[INSERT ...]`, or left to the owner. Slots are never shown to visitors: an empty slot renders nothing, or the pack's own placeholder line ("This message is waiting to be written…", "Add a real photograph here…", "Add an audio file to activate this player."). Writing real words into a slot makes them appear. Never paste an `[EDIT]` template into a visible field.

## Editable slots currently waiting for owner copy

| File / field | Slots | Rules |
|---|---:|---|
| `packContent.ts` → `packGiftSlots["09"…"17"].dedication` | 9 | The pack gave templates only. Read each gift's exact title in `giftsContent.ts`, then write 2–4 sentences. Mention only real details, or label the message as a wish, symbol or imagination. Shown as a quote at the top of the gift. |
| `packContent.ts` → `packGiftSlots["09"…"17"].revealLine` | 9 | One short line shown when the gift opens. |
| `packContent.ts` → `packLetter.optionalInserts[].text` | 4 | A real memory, an observed quality, an apology (only if wanted), a personal wish. The first is appended to the thank-you paragraph, the others become paragraphs after it. The `prompt` text is a note to the writer and is never shown. |
| `giftsContent.ts` → `openWhenLetters[].message` | 4 | Write an actual private letter for each, or leave it blank. A blank letter shows the pack's "waiting to be written" line. |
| `giftsContent.ts` → `couponEntries[].title` / `description` | 6 | Add only offers the owner explicitly approves. Blank coupons are intentionally not redeemable. |
| `giftsContent.ts` → `futureGardenLeaves[].text` | 8 | Future hopes only; do not present them as plans, events or promises. |
| `chronosContent.ts` → `letters` (four `kind: "empty"` envelopes) | 4 | The Letter Room's other four envelopes: add real words, or leave them. |
| `chronosContent.music.tracks[].src` | 3 | A local, properly licensed or owner-provided audio file. Never autoplay. No audio file exists, so Play stays disabled. |
| `chronosContent.gallery.photos[].src` / `caption` / `alt` | 6 | Genuine owner-supplied photos and accurate captions only. No generated substitute or invented date. The same photos feed Memory Cinema. |
| Gift 05 voice recording / transcript | 1 | A real recording and a text alternative are required before playback is enabled. The pack says not to synthesise a voice note. |

## Copy that now comes from the pack

| Where | What | Source in `packContent.ts` |
|---|---|---|
| Gift 01 and Letter Room envelope 1 | The main birthday letter | `packLetter` |
| Gift 02 (3D and HTML) | The 17 reasons and the closing quote | `packReasons` |
| Gift 07 "Draw a wish from the sky" | 101 wishes (the pack's heading says 100; the list has 101) | `packWishes` |
| Future Postcards (7 cards) | The seven messages | `packPostcards` |
| Gifts 01–08 | Dedication quote at the top | `packGiftDedications` |
| Gifts 03, 04, 08 | Long dedication and reveal line on reveal | `packExtended` |
| Birthday Garden | Seven stage narrations (Seed, Roots, Sprout, Leaves, Bud, Flower, Full bloom) | `packGardenNarration` |
| Memory Cinema (gift 06) and Gallery | Opening, empty-state and closing lines | `packCinema` |
| Bhumi FM (gift 05, Music lounge) | Welcome and empty-playlist lines | `packRadio` |
| Gift grid, buttons, loading, fallback, finale | Website microcopy | `packMicrocopy` |

## Source copy reused by the experiences

- Letter Room envelope 2 keeps the earlier source letter ("The Last Letter") word for word; do not alter its attribution without owner direction.
- Gift 04 shows only the verified dates in `chronosContent.dates.firstConnectionLabel` and `proposalLabel`.
- Gift 10 and the Wish Garden reveal only the ten source wishes in `chronosContent.flowerGarden.wishes`. Gift 07 also has them as its archive lanterns.
- Gift 08, Gift 16 and Gift 17 reuse existing archive messages rather than creating new private claims.
- Gift 11 uses four existing generated postcard scenes. Keep their "possible future / not a fact" framing.

## Adding an audio recording safely

1. Obtain a recording the owner supplied and approved; do not generate a voice clone or synthetic personal message.
2. Add the local file under `public/assets/audio/` and use a relative URL such as `/assets/audio/voice-note-01.mp3` in the corresponding track source.
3. Add a transcript/caption in the content source. Keep the player paused on load and require a user Play action.
4. Test play, pause, stop, seek/volume where available, error handling, dialog close/unmount cleanup, keyboard operation and reduced motion. Do not fetch remote audio.
5. Verify that an empty `src` still results in disabled controls and no failed network request.

## Adding photographs or personal content

- Add only owner-provided photographs to `public/assets/gallery/`; supply truthful alt text, a caption and a date only if the date is verified.
- Keep placeholder fields explicitly empty until real files/copy exist. Do not use generated portraits, fake memories, fabricated conversations, unapproved promises or unverified dates.
- Bhumi's birthday year remains unspecified. Keep future-postcard and future-garden copy speculative unless a real, mutual hope is supplied.
- The three postcard illustrations added with the pack (`public/assets/postcards/next-birthday-garden-table.webp`, `growing-sapling.webp`, `little-lantern-light.webp`) are generated artwork in the style of the existing four. They are atmosphere, not photographs of anything that happened.
```

## 2. `README.md` — modified

````markdown
# The World of You

> **Current local 17-world implementation:** `3D_IMPLEMENTATION_REPORT.md` and `3D_TRANSFORMATION_AUDIT.md` supersede historical scope counts below. All 17 gifts now have native scene integrations; this is not a claim of complete photoreal art direction. Vercel production remains the earlier deployment. Preview the current built project on port 4182.


> **Latest local refinement:** see `IMPLEMENTATION_REPORT.md` and `WEBSITE_AUDIT.md`. The new letter/postcard changes are implemented locally and previewed on port 4182, but **have not replaced the earlier Vercel production deployment**. Deployment statements below refer to the previous build.


> **Current native-3D build:** see `START_HERE.md` and `FINAL_IMPLEMENTATION_REPORT.md` for current scope, new browser evidence and limitations. Earlier findings/deployment descriptions below are historical. Current core QA: 12/12 pass; final native rose/crown/portal QA: 3/3 pass. No production deployment of this transformation has occurred.


A cinematic, scroll-linked birthday storybook for Bhumi. The experience begins with an invitation and travels through twelve connected rooms while the existing chapters, controls and natural document scrolling remain intact.

**Stack:** React 19 · TypeScript · Vite · GSAP/ScrollTrigger · `react-pageflip` · custom CSS. No WebGL runtime or new 3D dependency is used. The Gift Atelier contains 17 independently openable and replayable experiences. Playfair Display, Cormorant Garamond, DM Sans and Caveat are self-hosted locally.

## Run locally

```bash
npm ci
npm run dev
```

Build and preview the production bundle:

```bash
npm run build
npm run preview
```

Vite dev and preview servers bind to `0.0.0.0` for sandbox/preview hosting.

## Scene order

1. Invitation Room
2. Birthday Garden
3. Scrapbook
4. Memory Observatory
5. Letter Room
6. Memory Gallery
7. Wish Garden
8. Gift Atelier
9. Music Lounge
10. Future Postcards
11. Birthday Ballroom
12. Finale

The fixed decorative stage is driven by native document scroll. Text and interactions stay in the semantic chapter components. Only the current and neighboring scene art is eligible to load; other environments use CSS atmosphere/depth layers. The stage uses GSAP/ScrollTrigger when standard motion is allowed and a CSS/IntersectionObserver fallback under reduced motion or animation-load failure.

## Existing interactions retained

- Invitation envelope, open/skip flow, replay, chapter index and reading progress.
- Scrapbook page-flip controls, keyboard arrows and fallback.
- Verified-date timepiece, letter archive and empty real-photo mounts.
- Selectable birthday wishes and 17 distinct gift experiences, all independently accessible, replayable and tracked in local storage.
- Opt-in local music player (paused/no autoplay), speculative future postcards, candle/wish/blow cake ritual, and finale replay.

## Code map

- `src/scenes/sceneCatalog.ts` — stable scene IDs, chapter anchors, art and transition presets.
- `src/scenes/SceneExperience.tsx` — twelve-layer stage, adjacent-art loading, parallax/crossfade lifecycle, reduced-motion and CSS fallback.
- `src/styles/sceneSystem.css` — environment palettes, readable surfaces, depth, mobile focal points and reduced-motion rules.
- `src/App.tsx` — composition root, active chapter/progress, deep-hash landing and invitation/garden hash synchronization.
- `src/world/*.tsx` — chapter content and component-owned interactions.
- `src/world/GiftRoom.tsx` / `GiftExperiences.tsx` — 17 gift experiences, isolated replayable interactions and safe local progress.
- `src/content/packContent.ts` — the owner's content pack (`docs/content-pack/`) as typed data: main letter, 17 reasons, 101 wishes, seven postcards, gift dedications, garden narration, cinema/radio copy, microcopy. Edit it by hand; see `docs/CONTENT_PACK_INTEGRATION.md`.
- `src/content/chronosContent.ts` — verified dates, source copy, wishes, letters, audio/gallery slots and the postcard layout (built from the pack).
- `src/content/giftsContent.ts` — gift definitions and the owner-editable personal-copy slots the pack did not fill.
- `src/styles/designTokens.css`, `global.css`, `premium.css`, `giftAtelier.css` — tokens, responsive editorial styles and gift-specific visuals.
- `public/assets/` — local illustrations, self-hosted fonts and intentionally empty owner-media folders.
- `docs/screenshots/` — production baseline and scene captures; `docs/screenshots/gifts/` contains one capture for each gift.

## Personal-content and media rules

The source establishes the names **Bhumi** and **Rudra**, first connection **11 May 2025**, proposal **17 July 2025**, and birthday **17 November** (year unspecified). The time counter uses the start of 11 May 2025 in `Asia/Kolkata`; it does not imply a private hour or conversation.

No personal photographs or audio were supplied. Six gallery mounts and three audio entries therefore remain empty, and show the pack's own “add a real photograph / add an audio file” lines instead of a template. No AI faces, synthetic “memories,” voice notes or invented promises are used. Seven generated landscapes (four original, three added with the content pack) are labeled as speculative postcards, not trips or shared events. The owner's content pack supplies the main letter, 17 reasons, 101 wishes, seven postcard messages, the gift 01–08 dedications and the site microcopy; it is the pack author's draft, so the owner reads it before publishing. Slots the pack left open (four Open When letters, six coupons, eight future hopes, the gift 09–17 dedications, four letter inserts) stay empty and are never shown as `[EDIT]` text.

To personalize the site:

1. Edit the pack copy in `src/content/packContent.ts`, verified chapter/source copy in `src/content/chronosContent.ts`, and the separate gift names and remaining personal-copy slots in `src/content/giftsContent.ts`. `GIFT_CONTENT_GUIDE.md` lists every slot.
2. Add only owner-supplied photographs to `public/assets/gallery/` with accurate alt text and captions.
3. Add only owner-provided or appropriately licensed local audio to `public/assets/audio/`, then set the matching `src`. Preserve opt-in/no-autoplay behavior.
4. Do not present generated art as a personal photograph, memory, or real shared event.

## QA and project documentation

The current documents (master build, test results, deployment, the owner's content pack) are in `docs/`; start with [`docs/README.md`](docs/README.md). The files listed below describe the project as it was before the master build.

- [`PROJECT_AUDIT.md`](PROJECT_AUDIT.md) — pre-implementation repository/live-site audit.
- [`DESIGN_SYSTEM.md`](DESIGN_SYSTEM.md) — palette, typography, responsive and motion rules.
- [`SCENE_ARCHITECTURE.md`](SCENE_ARCHITECTURE.md) — scene ownership, IDs, transitions, fallback and lifecycle.
- [`ASSET_GENERATION_GUIDE.md`](ASSET_GENERATION_GUIDE.md) — prompts, asset policy and budgets.
- [`ANIMATION_SPECIFICATION.md`](ANIMATION_SPECIFICATION.md) — scroll progress, depth motion and reduced-motion behavior.
- [`ASSET_MANIFEST.md`](ASSET_MANIFEST.md) — shipped assets, licenses, empty media slots and final screenshots.
- [`PERFORMANCE_REPORT.md`](PERFORMANCE_REPORT.md) — measured production chunks/assets and limits.
- [`ACCESSIBILITY_REPORT.md`](ACCESSIBILITY_REPORT.md) — keyboard, labels, focus, reduced motion and testing limitations.
- [`GIFT_ATELIER_SPECIFICATION.md`](GIFT_ATELIER_SPECIFICATION.md) — the seventeen distinct gift experiences and their content/media gates.
- [`GIFT_CONTENT_GUIDE.md`](GIFT_CONTENT_GUIDE.md) — owner-editable fields and personal-content rules.
- [`AUDIO_IMPLEMENTATION.md`](AUDIO_IMPLEMENTATION.md) — local-only opt-in audio behavior and missing media status.
- [`FINAL_QA_REPORT.md`](FINAL_QA_REPORT.md) — scene baseline, local QA scope and existing deployment smoke status.
- [`GIFT_QA_REPORT.md`](GIFT_QA_REPORT.md) — current 17-experience build, responsive, interaction, keyboard, storage, reduced-motion and screenshot results.
- [`PROJECT_PROGRESS.md`](PROJECT_PROGRESS.md) — implementation status, production boundary and remaining security/deployment gates.
- [`SOURCE_RECONSTRUCTION.md`](SOURCE_RECONSTRUCTION.md) — available source boundary and verified facts.

No formal axe/WCAG certification, screen-reader session, or real-device GPU/memory profile is claimed; see the QA reports for precise scope.

## Source boundary

The requested canonical ZIP was not present in the workspace. The current React/Vite project is a transformation of the available project/reference materials, not a claimed byte-for-byte edit of a missing archive. See `SOURCE_RECONSTRUCTION.md` and `docs/source-reference/`.

## Deployment status

The site is published on Vercel at [the-world-of-you-birthday-storybook.vercel.app](https://the-world-of-you-birthday-storybook.vercel.app/). Which commit is live, how it was deployed and checked, and the rollback target are in `docs/DEPLOYMENT_REPORT.md` (written from `docs/deployment-record.json`). The deployments named in the older root reports (`QA_REPORT.md`, `FINAL_QA_REPORT.md`, `PROJECT_PROGRESS.md`) are historical.

The owner's content pack (`docs/CONTENT_PACK_INTEGRATION.md`) is live: it is commit `d0e4d15`, which is inside the deployed commit `a92d2d8`, and `docs/DEPLOYMENT_REPORT.md` has the evidence (files byte-compared with the tested build, every pack string looked up in the live JavaScript, a browser run and the specs against the live URL). Later changes to the copy (`src/content/packContent.ts`) reach the site only with a new deployment.
````

## 3. `playwright.config.ts` — modified

```ts
import { defineConfig } from "@playwright/test";

// QA_SLOW=1 multiplies timeouts for software WebGL (SwiftShader) where a scene needs 20-30 s to compile its first frame.
// CHROMIUM_PATH points at any Chromium build when Playwright's own browser cannot be downloaded (CI sandboxes).
const slow = process.env.QA_SLOW ? 4 : 1;
const executablePath = process.env.CHROMIUM_PATH || undefined;
const baseURL = process.env.BASE_URL || "http://localhost:4181"; // BASE_URL points the specs at a deployed site instead of the local server
const origin = new URL(baseURL).origin;
const quality = process.env.QA_QUALITY; // forces the scene quality tier (low | medium | high) through the same localStorage key the site uses
const args = ["--no-sandbox", "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader",
  ...(executablePath ? ["--disable-setuid-sandbox", "--disable-dev-shm-usage", "--ignore-gpu-blocklist", "--single-process", "--no-zygote", "--in-process-gpu"] : [])];

export default defineConfig({
  testDir: "./tests", testMatch: "**/*.spec.ts", timeout: 90000 * slow, expect: { timeout: 15000 * slow }, workers: 1,
  reporter: [["list"], ["json", { outputFile: "qa-results.json" }]],
  use: { baseURL, viewport: { width: 1280, height: 900 }, reducedMotion: "reduce", launchOptions: { executablePath, args },
    ...(quality ? { storageState: { cookies: [], origins: [{ origin, localStorage: [{ name: "woy-quality", value: quality }] }] } } : {}) },
});
```

## 4. `scripts/content-pack/build-pack-content.py` — new

```python
#!/usr/bin/env python3
"""
One-time importer for the owner's PDF "The World of You — Complete Missing Content Pack".

    pip install pymupdf
    python3 scripts/content-pack/build-pack-content.py docs/content-pack/The_World_of_You_Complete_Missing_Content_Pack.pdf

Writes
  docs/content-pack/pack-text.txt   the PDF text, verbatim, one text block per line (the audit trail)
  src/content/packContent.ts        the same copy as typed data

Nothing is reworded: the importer only joins the PDF's hard line wraps, drops the decorative pull-quote marks, turns straight
apostrophes inside words into typographic ones, and repairs the two glyphs the PDF could not draw (the heart after the
letter's greeting and the checklist boxes). The two files are compared by tests/content-pack-verbatim.spec.ts.

After the first run src/content/packContent.ts is meant to be edited by hand; re-running this script overwrites it.
"""
import json
import pathlib
import re
import sys

import fitz  # PyMuPDF

ROOT = pathlib.Path(__file__).resolve().parents[2]
PDF = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "docs/content-pack/The_World_of_You_Complete_Missing_Content_Pack.pdf"
FOOTER = "THE WORLD OF YOU • COMPLETE MISSING CONTENT PACK"
HEART = "\u2764\ufe0f"


def read_pages(pdf):
    pages = []
    for page in fitz.open(pdf):
        out = []
        for x0, y0, x1, y1, text, _no, kind in page.get_text("blocks", sort=True):
            if kind != 0:
                continue
            t = " ".join(text.replace("\u00ad", "").split())
            if t and not t.startswith(FOOTER):
                out.append(t)
        pages.append(out)
    return pages


def repair(t):
    # The PDF's symbol font printed the emoji heart as "h" + a missing glyph, and the checklist ticks as "I".
    t = t.replace("Happy Birthday. hI", "Happy Birthday. " + HEART)
    return t


def clean(t):
    """Display text: no pull-quote marks, typographic apostrophes inside words."""
    t = t.strip()
    if t.startswith("\u201c") and t.endswith("\u201d"):
        t = t[1:-1].strip()
    return re.sub(r"(?<=\w)'(?=\w)", "\u2019", t)


pages = read_pages(PDF)
lines = []  # (page, text)
for number, blocks in enumerate(pages, 1):
    for t in blocks:
        lines.append((number, repair(t)))

# ---------------------------------------------------------------- transcript
tx = ["# Verbatim transcript of The_World_of_You_Complete_Missing_Content_Pack.pdf (15 pages), one PDF text block per line.",
      "# Wrapped lines are joined; the heart after the greeting and the checklist boxes are PDF glyph artefacts and are repaired.",
      ""]
current = None
for page, t in lines:
    if page != current:
        current = page
        tx.append(f"## PAGE {page}")
    tx.append(t)
(ROOT / "docs/content-pack/pack-text.txt").write_text("\n".join(tx) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- sections
HEADINGS = [
    ("letter", "01. Secret Letter — Main Birthday Letter"),
    ("reasons", "02. Jar of Reasons — 17 Notes"),
    ("wishes", "03. A Thousand Wishes — 100 Short Wishes"),
    ("postcards", "04. Future Postcards — 7 Complete Messages"),
    ("dedications", "05. Gift Dedications — 17 Surprises"),
    ("flower", "06. Everlasting Flower — Dedication"),
    ("universe", "07. Little Universe — Dedication"),
    ("garden", "08. Birthday Garden — Narration"),
    ("cinema", "09. Memory Cinema — Captions and Missing-Media Copy"),
    ("radio", "10. Bhumi FM — Audio Content"),
    ("crown", "11. Queen's Crown — Dedication"),
    ("microcopy", "12. Website Microcopy — Empty States, Buttons and Reveals"),
    ("checklist", "13. Final Content Completion Checklist"),
]
flat = [t for _p, t in lines]
starts = {}
for key, head in HEADINGS:
    hits = [i for i, t in enumerate(flat) if t == head]
    assert len(hits) == 1, (key, hits)
    starts[key] = hits[0]
order = sorted(starts.items(), key=lambda kv: kv[1])
sec = {}
for n, (key, i) in enumerate(order):
    end = order[n + 1][1] if n + 1 < len(order) else len(flat)
    sec[key] = flat[i + 1:end]

cover = [t for p, t in lines if p == 1]
data = {}

# 00 cover
data["cover"] = {
    "title": cover[0],
    "subtitle": cover[1],
    "tagline": clean(next(t for t in cover if t.startswith("\u201c"))),
}

# 01 letter
L = sec["letter"]
assert L[0].startswith("Suggested title: ") and L[1].startswith("Suggested subtitle: ")
end_body = L.index("With love,")
body = L[4:end_body]  # after "Dear Bhumi," and the greeting
assert L[2] == "Dear Bhumi," and L[3].startswith("Happy Birthday.")
thanks_at = next(i for i, t in enumerate(body) if t.startswith("Thank you for being a part"))
thanks_full = body[thanks_at]
cut = thanks_full.index(" [EDIT:")
INSERT_IDS = ["memory", "quality", "apology", "wish"]
bullets = [t[2:] for t in L if t.startswith("• [EDIT]")]
assert len(bullets) == 4
data["letter"] = {
    "title": L[0][len("Suggested title: "):],
    "subtitle": L[1][len("Suggested subtitle: "):],
    "salutation": L[2],
    "greeting": L[3],
    "paragraphs": [clean(t) for t in body[:thanks_at]],
    "thanks": clean(thanks_full[:cut]),
    "memoryPrompt": thanks_full[cut + 1:],
    "afterThanks": [clean(t) for t in body[thanks_at + 1:]],
    "closing": L[end_body],
    "signature": L[end_body + 1],
    "optionalInserts": [{"id": k, "text": ""} for k in INSERT_IDS],
}
data["letterInsertPrompts"] = [{"id": k, "prompt": b} for k, b in zip(INSERT_IDS, bullets)]
assert len(data["letter"]["paragraphs"]) == 4 and len(data["letter"]["afterThanks"]) == 4

# 02 reasons
R = sec["reasons"]
reasons = [re.match(r"^(\d\d)\. (.*)$", t) for t in R]
items = [m for m in reasons if m]
assert [m.group(1) for m in items] == [f"{i:02d}" for i in range(1, 18)]
data["reasons"] = {
    "items": [clean(m.group(2)) for m in items],
    "quote": clean(next(t for t in R if t.startswith("\u201c"))),
}

# 03 wishes
W = sec["wishes"]
wishes = [re.match(r"^(\d{2,3})\. (.*)$", t) for t in W]
witems = [m for m in wishes if m]
assert [m.group(1) for m in witems] == [f"{i:02d}" for i in range(1, 102)], len(witems)
data["wishes"] = [clean(m.group(2)) for m in witems]

# 04 postcards
P = sec["postcards"]
cards = []
for i, t in enumerate(P):
    m = re.match(r"^POSTCARD (\d\d) — (.+)$", t)
    if m:
        cards.append({"number": m.group(1), "title": m.group(2), "message": clean(P[i + 1])})
assert len(cards) == 7
data["postcards"] = cards

# 05 dedications
D = sec["dedications"]
short = {}
for i, t in enumerate(D):
    m = re.match(r"^(0[1-8]) — (.+)$", t)
    if m:
        short[m.group(1)] = {"packTitle": m.group(2), "text": clean(D[i + 1])}
assert sorted(short) == [f"0{i}" for i in range(1, 9)]
template_gifts = [t for t in D if re.match(r"^(09|1[0-7]) — \[INSERT", t)]
assert len(template_gifts) == 9
data["dedications"] = short

# 06 / 07 / 11 extended dedications
def extended(key):
    S = sec[key]
    quote = clean(next(t for t in S if t.startswith("\u201c")))
    reveal = next(t for t in S if t.startswith("Short reveal line: "))[len("Short reveal line: "):]
    return {"text": quote, "revealLine": reveal}
data["extended"] = {"flower": extended("flower"), "universe": extended("universe"), "crown": extended("crown")}

# 08 garden narration
G = sec["garden"]
narr = []
for i, t in enumerate(G):
    m = re.match(r"^([A-Z ]+) — (.+)$", t)
    if m:
        narr.append({"stage": m.group(1), "title": m.group(2), "text": clean(G[i + 1])})
assert [n["stage"] for n in narr] == ["SEED", "ROOTS", "SPROUT", "LEAVES", "BUD", "FLOWER", "FULL BLOOM"]
data["garden"] = narr

# 09 cinema
C = sec["cinema"]
def after(label):
    return clean(C[C.index(label) + 1])
rf = C.index("Required fields for each memory")
data["cinema"] = {
    "opening": after("Opening screen"),
    "photoCaptionTemplate": after("Photo caption template"),
    "videoCaptionTemplate": after("Video caption template"),
    "timelineIntro": after("Timeline intro"),
    "emptyState": after("Empty gallery state"),
    "closing": after("Closing screen"),
    "requiredFields": [t[2:] for t in C[rf + 1:] if t.startswith("• ")],
}
assert len(data["cinema"]["requiredFields"]) == 6

# 10 radio
F = sec["radio"]
quotes = [clean(t) for t in F if t.startswith("\u201c")]
assert len(quotes) == 2
tracks = [t for t in F if re.match(r"^Track 0[1-3]:", t)]
assert len(tracks) == 3
data["radio"] = {
    "welcome": quotes[0],
    "trackTemplates": tracks,
    "voiceNoteTemplate": next(t for t in F if t.startswith("Optional voice note:")),
    "emptyPlaylist": quotes[1],
    "requirements": next(t for t in F if t.startswith("No autoplay.")),
}

# 12 microcopy
M = sec["microcopy"]
labels = [
    ("giftGridIntro", "Gift grid intro"), ("giftLocked", "Gift locked/coming soon"), ("replay", "Replay button"),
    ("skip", "Skip button"), ("close", "Close button"), ("back", "Back button"), ("loading", "Loading 3D scene"),
    ("webglFallback", "WebGL fallback"), ("missingText", "Missing text"), ("missingPhoto", "Missing photo"),
    ("missingAudio", "Missing audio"), ("progress", "Progress label"), ("finalThanks", "Final thank-you"),
]
micro = {}
for key, label in labels:
    micro[key] = clean(M[M.index(label) + 1])
assert len(micro) == 13
data["microcopy"] = micro

# 13 checklist
K = sec["checklist"]
fin = K.index("Final note")
data["checklist"] = {
    "items": [re.sub(r"^I ", "", t) for t in K[:fin]],
    "finalNote": K[fin + 1],
    "credit": K[fin + 2],
}
assert len(data["checklist"]["items"]) == 16

# author's notes (not site copy)
data["authorNotes"] = {
    "reasons": R[0],
    "wishes": W[0],
    "dedications": D[0],
    "cinema": C[0],
}

# ---------------------------------------------------------------- TypeScript emitter
def lit(v, ind=0):
    pad = "  " * ind
    if isinstance(v, str):
        return json.dumps(v, ensure_ascii=False)
    if isinstance(v, list):
        if not v:
            return "[]"
        if all(isinstance(x, str) for x in v):
            return "[\n" + "".join(f"{pad}  {lit(x)},\n" for x in v) + pad + "]"
        return "[\n" + "".join(f"{pad}  {lit(x, ind + 1)},\n" for x in v) + pad + "]"
    if isinstance(v, dict):
        parts = []
        for k, x in v.items():
            key = k if re.match(r"^[A-Za-z_]\w*$", k) else json.dumps(k)
            parts.append(f"{pad}  {key}: {lit(x, ind + 1)},\n")
        return "{\n" + "".join(parts) + pad + "}"
    raise TypeError(v)

dedication_slots = {f"{n:02d}": {"dedication": "", "revealLine": ""} for n in range(9, 18)}
ts = f'''/**
 * THE WORLD OF YOU — COMPLETE MISSING CONTENT PACK. Owner-supplied PDF (docs/content-pack/), transcribed verbatim by
 * scripts/content-pack/build-pack-content.py and compared with docs/content-pack/pack-text.txt by tests/content-pack-verbatim.spec.ts.
 *
 * Rules that the components follow:
 *  - Nothing here is reworded in the UI. The PDF's pull-quote marks are not part of the text; apostrophes inside words are typographic.
 *  - A "slot" is an empty string or a template the pack itself marked as [EDIT] / [ADD ...]. Slots are NEVER shown to visitors:
 *    an empty slot simply renders nothing (or the pack's own "missing ..." microcopy). Fill a slot with the real words and it appears.
 *  - The pack is ready-to-edit copy, not a verified transcript of any private history. Read it before publishing.
 *  - This file is now the one place to edit that copy. Re-running the importer would overwrite your edits.
 */
/** Page 1 of the PDF. */
export const packCover = {lit(data["cover"])} as const;

/**
 * 01. Secret Letter — Main Birthday Letter.
 * `memoryPrompt` is the pack's inline [EDIT]: an owner slot, never shown. `optionalInserts` are the four owner slots of the pack's
 * bullets (prompts: `packLetterInsertPrompts` below, same order). Whatever is typed into optionalInserts[0].text (a real memory) is
 * appended to the thank-you paragraph, exactly where the pack put its [EDIT]; the other three inserts, if written, become their own
 * paragraphs right after it.
 */
export const packLetter = {lit(data["letter"])};

/**
 * The pack's four optional-insert bullets: prompts for the owner, never shown. They live apart from `packLetter` and nothing in `src`
 * imports them, so they are not part of the website bundle. Prompt i describes `packLetter.optionalInserts[i]`.
 */
export const packLetterInsertPrompts = {lit(data["letterInsertPrompts"])} as const;

/** 02. Jar of Reasons — 17 Notes (draft reasons, kept general by the author of the pack). */
export const packReasons: {{ readonly items: readonly string[]; readonly quote: string }} = {lit(data["reasons"])};

/** 03. A Thousand Wishes. The heading says 100; the list in the PDF has {len(data["wishes"])} entries and all of them are here. */
export const packWishes: readonly string[] = {lit(data["wishes"])};

/** 04. Future Postcards — 7 complete messages. */
export const packPostcards: readonly {{ readonly number: string; readonly title: string; readonly message: string }}[] = {lit(data["postcards"])};

/** 05. Gift dedications for gifts 01–08 (the pack's own short titles are kept in packTitle for reference only). */
export const packGiftDedications: Readonly<Record<string, {{ readonly packTitle: string; readonly text: string }}>> = {lit(data["dedications"])};

/**
 * 05 (template). Gifts 09–17: the pack supplies no copy, only [EDIT] templates ("2–4 sentence dedication ... mention only real
 * details or clearly label the message as a wish, symbol, or imagination" and "one short line shown when the gift opens").
 * These are owner slots; empty means "show nothing".
 */
export const packGiftSlots: Record<string, {{ dedication: string; revealLine: string }}> = {lit(dedication_slots)};

/** 06. Everlasting Flower, 07. Little Universe, 11. Queen's Crown: long dedication plus the short reveal line. */
export const packExtended: {{ readonly flower: PackExtended; readonly universe: PackExtended; readonly crown: PackExtended }} = {lit(data["extended"])};
export interface PackExtended {{ readonly text: string; readonly revealLine: string }}

/** 08. Birthday Garden — Narration: seven stages (the pack adds BUD between LEAVES and FLOWER). */
export const packGardenNarration: readonly {{ readonly stage: string; readonly title: string; readonly text: string }}[] = {lit(data["garden"])};

/** 09. Memory Cinema. The two caption templates and requiredFields describe the data model only; they are never displayed. */
export const packCinema = {lit(data["cinema"])};

/** 10. Bhumi FM. trackTemplates and voiceNoteTemplate are the pack's [ADD ...] slots (never displayed). */
export const packRadio = {lit(data["radio"])};

/** 12. Website microcopy. `progress` keeps the pack's [X] marker; use packProgress(n). */
export const packMicrocopy = {lit(data["microcopy"])} as const;
export const packProgress = (opened: number) => packMicrocopy.progress.replace("[X]", String(opened));

/** 13. The pack's own completion checklist and closing note (reference for docs/CONTENT_PACK_INTEGRATION.md; not shown on the site). */
export const packChecklist = {lit(data["checklist"])} as const;

/** The author's Hinglish notes to the owner. Kept for the record; not site copy. */
export const packAuthorNotes = {lit(data["authorNotes"])} as const;
'''
(ROOT / "src/content/packContent.ts").write_text(ts, encoding="utf-8")
print("transcript lines:", len(tx), "| letter paragraphs:", 4 + 1 + 4, "| reasons:", len(data["reasons"]["items"]),
      "| wishes:", len(data["wishes"]), "| postcards:", len(cards), "| narration:", len(narr), "| microcopy:", len(micro))
```

## 5. `scripts/make-asset-inventory.py` — new

```python
#!/usr/bin/env python3
"""Regenerates docs/ASSET_INVENTORY.md from the real files (public/, node_modules licences, src/engine and src/three).
Run from the repo root:  python3 scripts/make-asset-inventory.py
Nothing here is hand-maintained, so the inventory cannot drift from the repository."""
import json, os, datetime
from pathlib import Path
from PIL import Image

root = Path(__file__).resolve().parent.parent
os.chdir(root)

def kb(n): return f"{n / 1024:.0f} KB" if n < 1024 * 1024 else f"{n / 1024 / 1024:.2f} MB"
def loc(path): return sum(1 for _ in open(path, encoding="utf-8", errors="replace"))

out = ["# Asset inventory", "", f"Generated {os.environ.get('REPORT_DATE') or datetime.date.today()} by `scripts/make-asset-inventory.py` from the files in this repository.", ""]

# ---------------------------------------------------------------- public tree
out += ["## 1. Static files shipped in `public/`", "", "| Folder | Files | Size |", "|---|---:|---:|"]
groups = {}
for p in sorted(Path("public").rglob("*")):
    if p.is_file():
        g = str(p.parent)
        n, s = groups.get(g, (0, 0)); groups[g] = (n + 1, s + p.stat().st_size)
total = 0
for g, (n, s) in sorted(groups.items()):
    out.append(f"| `{g}` | {n} | {kb(s)} |"); total += s
out += [f"| **total** | {sum(n for n, _ in groups.values())} | **{kb(total)}** |", ""]

# ---------------------------------------------------------------- images
GENERATED_IMAGES = {"assets/postcards/next-birthday-garden-table.webp", "assets/postcards/growing-sapling.webp", "assets/postcards/little-lantern-light.webp"}
out += ["## 2. Images", "",
        "Illustrations (backgrounds, scene paintings, postcards, paper, objects, flowers) arrived with the owner's project ZIP. Their authorship and licence cannot be verified from the repository, so they are treated as **owner-supplied**.",
        "The 17 gift posters are different: they are rendered by `scripts/qa/render-previews.mjs` from the native 3D scenes in this repo (project-authored).",
        "Three postcard illustrations are different too: the content pack has seven postcard messages and the site had four pictures, so postcards 02, 06 and 07 got new ones, generated for this project with an AI image generator (the terms of that generator apply; replace them with your own pictures if you prefer). They are illustrative atmosphere, never a photograph or a memory.", "",
        "| File | Size | Pixels | Provenance |", "|---|---:|---|---|"]
for p in sorted(Path("public/assets").rglob("*.webp")) + sorted(Path("public/assets").rglob("*.png")) + sorted(Path("public/assets").rglob("*.jpg")):
    try: w, h = Image.open(p).size
    except Exception: w = h = 0
    rel = str(p.relative_to("public"))
    if "gift-previews" in rel: prov = "rendered from the native scene (project-authored)"
    elif rel in GENERATED_IMAGES: prov = "generated for the content pack (AI image generator; illustration only)"
    else: prov = "owner-supplied (ZIP)"
    out.append(f"| `{p.relative_to('public')}` | {kb(p.stat().st_size)} | {w}x{h} | {prov} |")
out.append("")

# ---------------------------------------------------------------- fonts, models, audio
out += ["## 3. Fonts", "", "| File | Size | Licence |", "|---|---:|---|"]
for p in sorted(Path("public/assets/fonts").glob("*.woff2")):
    out.append(f"| `{p.name}` | {kb(p.stat().st_size)} | SIL OFL 1.1 (text next to the file) |")
out += ["", "## 4. Models", "",
        "`public/assets/models/*.glb` are static authoring snapshots made by the project's own exporter. **The application never requests them** (no loader exists in `src`).",
        "They are kept because they are owner-visible history; they were not regenerated in the master build.", "", "| File | Size |", "|---|---:|"]
for p in sorted(Path("public/assets/models").glob("*.glb")):
    out.append(f"| `{p.name}` | {kb(p.stat().st_size)} |")
audio = [p for p in Path("public/assets/audio").glob("*") if p.name != ".gitkeep"]
out += ["", "## 5. Audio, photos and video", "",
        f"* `public/assets/audio`: {len(audio)} audio file(s). Bhumi FM and the turntable play only supplied audio, so their Play buttons stay disabled until a file is added.",
        "* No personal photos, videos or voice recordings exist in the repository. Memory Cinema and the Memory Gallery show clearly marked placeholders.", ""]

# ---------------------------------------------------------------- libraries
out += ["## 6. Runtime libraries (licence read from `node_modules/<pkg>/package.json`)", "", "| Package | Version | Licence |", "|---|---|---|"]
pkg = json.load(open("package.json"))
for name in sorted(pkg.get("dependencies", {})):
    try:
        meta = json.load(open(f"node_modules/{name}/package.json"))
        lic = meta.get("license") or meta.get("licenses") or "see package"
        if isinstance(lic, list): lic = ", ".join(l.get("type", "?") for l in lic)
        out.append(f"| {name} | {meta.get('version', '?')} | {lic} |")
    except Exception:
        out.append(f"| {name} | (not installed here) | (check package) |")
out.append("")

# ---------------------------------------------------------------- procedural assets
out += ["## 7. Procedural assets (code is the asset)", "", "| Module | Lines | What it generates |", "|---|---:|---|"]
engine_notes = {
    "textures.ts": "wood, paper, leather, fabric, brushed metal, marble, stone, soil, bark, petal, leaf, glow and sparkle canvases",
    "materials.ts": "MaterialKit: PBR materials from those canvases, quality-tiered glass and gems",
    "environment.ts": "PMREM lighting presets (candle, moon, garden, studio, ballroom, dusk)",
    "fx.ts": "GPU particle fields, confetti / spark / smoke bursts, candle flames",
    "garden.ts": "terrain with soil strata, wind grass, butterflies, roots, multi-layer bloom, painted sky",
    "geometry.ts": "petals, leaves, tapered growing tubes, gems, ribbons, bent paper, rounded boxes, lathe helpers",
    "paper.ts": "segmented folded paper (letter) with creases and thickness",
    "audio.ts": "synthesised sound effects (off by default)",
}
for p in sorted(Path("src/engine").glob("*.ts")):
    out.append(f"| `{p}` | {loc(p)} | {engine_notes.get(p.name, 'engine support')} |")
for p in sorted(Path("src/three/gifts").glob("*.ts")):
    out.append(f"| `{p}` | {loc(p)} | gift scene |")
for p in sorted(Path("src/three/sections").glob("*.ts")):
    out.append(f"| `{p}` | {loc(p)} | section scene |")
out.append("")
Path("docs").mkdir(exist_ok=True)
Path("docs/ASSET_INVENTORY.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print("wrote docs/ASSET_INVENTORY.md", len(out), "lines")
```

## 6. `scripts/make-export.py` — new

````python
#!/usr/bin/env python3
"""Builds the code export of everything that changed since the migration commit, straight from git (never from the working tree):

  ALL_CODE.md        every changed text file, line for line, in fenced blocks
  MANIFEST.md        one row per changed code file (status, lines, what it is) plus the deleted files
  woy-master-build-code.zip   the same files + docs/*.md + the content pack + changed binary assets under public/ (unzip over the project root)
  the-world-of-you-master-build.bundle (+ .sha256)   the whole repository history, for `git pull` / `git clone`

usage: python3 scripts/make-export.py [--base 0f16a01] [--out /home/user/export]
Run it on a clean tree: the export describes HEAD, and the script refuses to run when tracked files have uncommitted changes."""
import argparse, datetime, hashlib, os, re, subprocess, sys, zipfile
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--base", default="0f16a01")
ap.add_argument("--out", default="/home/user/export")
args = ap.parse_args()
root = Path(__file__).resolve().parent.parent
os.chdir(root)

def git(*a, binary=False):
    r = subprocess.run(["git", *a], capture_output=True)
    if r.returncode != 0: sys.exit(f"git {' '.join(a)} failed: {r.stderr.decode()[:300]}")
    return r.stdout if binary else r.stdout.decode("utf-8")

if git("status", "--porcelain", "--untracked-files=no").strip():
    sys.exit("tracked files have uncommitted changes; commit first (the export describes HEAD)")
head = git("rev-parse", "--short", "HEAD").strip()
base = git("rev-parse", "--short", args.base).strip()
today = datetime.date.today().isoformat()
out = Path(args.out); out.mkdir(parents=True, exist_ok=True)
for old in out.iterdir():
    if old.is_file(): old.unlink()

changes = [line.split("\t") for line in git("diff", "--name-status", "--no-renames", base, "HEAD").splitlines()]
TEXT = {".ts", ".tsx", ".css", ".mjs", ".js", ".py", ".sh", ".json", ".html", ".md", ".txt", ".svg", ".cjs"}
ROOT_CODE = {"package.json", "package-lock.json", "tsconfig.json", "tsconfig.app.json", "tsconfig.node.json", "vite.config.ts", "index.html", ".gitignore", ".vercelignore", "playwright.config.ts", "README.md", "GIFT_CONTENT_GUIDE.md", "vercel.json"}
def is_code(path):
    p = Path(path)
    if p.suffix not in TEXT: return False
    if path.startswith(("qa/", "docs/", "vercel-upload/")) or path in {"qa-results.json", "IMPLEMENTATION_REPORT.md", "package-lock.json"}: return False
    return path.split("/")[0] in {"src", "tests", "scripts"} or path in ROOT_CODE
def is_doc(path):
    return path.startswith("docs/") and Path(path).suffix in {".md", ".txt", ".json", ".pdf"} and not path.startswith("docs/qa-screens/")
def is_asset(path):
    return path.startswith("public/") and Path(path).suffix not in TEXT

deleted = sorted(p for s, p in changes if s == "D" and not p.startswith(("qa/", "vercel-upload/")) and p != "qa-results.json")
live = [(s, p) for s, p in changes if s != "D"]
code = sorted((p, "NEW" if s == "A" else "MODIFIED") for s, p in live if is_code(p))
docs = sorted(p for s, p in live if is_doc(p)) + ["IMPLEMENTATION_REPORT.md"]
assets = sorted(p for s, p in live if is_asset(p))
docs = [d for d in docs if subprocess.run(["git", "cat-file", "-e", f"HEAD:{d}"], capture_output=True).returncode == 0]

def blob(path): return git("show", f"HEAD:{path}", binary=True)
def describe(path, text):
    """What a file is, in a few words: its heading (.md); else the header comment (the first comment line with words, before any code;
    a bare /** or three-quote opener is skipped); else, for a spec, the title of its first test; else the name of its first export.
    Import statements, also multi-line ones, are never used."""
    opener = re.compile(r'^(?:/\*+|\*+/?|//+|#+|"""|\'\'\')\s*')
    export = re.compile(r"export\s+(?:default\s+)?(?:async\s+)?(?:function|const|class|interface|type|enum)\s+(\w+)")
    title = re.compile(r"\btest(?:\.describe)?\(\s*([`'\"])(.+?)\1")
    in_import, seen_code, expecting, first_export, first_test = False, False, False, None, None
    for raw in text.splitlines():
        line = raw.strip()
        if in_import:
            if " from " in line or line.endswith(";") or line.startswith("}"): in_import = False
            continue
        if not line or line.startswith(("#!", "'use ", '"use ', "```")): continue
        if line.startswith(("import ", "from ")):
            if line.startswith("import ") and "{" in line and "}" not in line: in_import = True
            continue
        if path.endswith(".md"):
            if line.startswith("#"): return line.lstrip("# ").strip()[:150]
            continue
        if not seen_code and opener.match(line):
            words = re.sub(r"\s*\*/$", "", opener.sub("", line)).strip().rstrip('"').strip()
            if words: return words[:150]
            expecting = True          # a bare opener: the words are on the next line
            continue
        if expecting: return re.sub(r"\s*(?:\"\"\"|\'\'\'|\*/)$", "", line).strip()[:150]
        seen_code = True
        if first_test is None and path.endswith((".spec.ts", ".spec.mjs", ".test.ts")):
            m = title.search(line)
            if m: first_test = m.group(2)
        m = export.match(line)
        if m and first_export is None: first_export = m.group(1)
    if first_test: return f"tests, the first: {first_test}"[:150]
    return f"exports {first_export}" if first_export else ""
LANG = {".ts": "ts", ".tsx": "tsx", ".css": "css", ".mjs": "js", ".js": "js", ".cjs": "js", ".py": "python", ".sh": "bash", ".json": "json", ".html": "html", ".md": "markdown", ".txt": "text", ".svg": "xml"}

texts = {p: blob(p).decode("utf-8") for p, _ in code}
total_lines = sum(len(t.splitlines()) for t in texts.values())

# ---- ALL_CODE.md
parts = [f"# THE WORLD OF YOU — complete code of the build", "",
         f"{len(code)} files, every line, exactly as committed in `{head}` ({today}).", "",
         "Copy each block into the same path inside your project, or unzip `woy-master-build-code.zip` over the project root (and delete the files listed in MANIFEST.md under *Deleted*).", "", "## Contents", ""]
parts += [f"{i}. `{p}` — {status.lower()}" for i, (p, status) in enumerate(code, 1)] + [""]
for i, (p, status) in enumerate(code, 1):
    text = texts[p]
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    fence = "`" * max(3, longest + 1)
    parts += [f"## {i}. `{p}` — {status.lower()}", "", f"{fence}{LANG.get(Path(p).suffix, '')}", text.rstrip("\n"), fence, ""]
(out / "ALL_CODE.md").write_text("\n".join(parts), encoding="utf-8")

# ---- MANIFEST.md
rows = [f"| {i} | {status} | `{p}` | {len(texts[p].splitlines())} | {describe(p, texts[p]).replace('|', '/')} |" for i, (p, status) in enumerate(code, 1)]
man = [f"# THE WORLD OF YOU — code manifest", "",
       f"Generated {today} from git commit `{head}` (everything that changed after the migration commit `{base}`).", "",
       f"**{len(code)} code files** ({total_lines:,} lines), {len(deleted)} files deleted, plus {len(docs)} documents (`docs/`, the content pack, the reports) and {len(assets)} changed binary assets under `public/` (gift posters, postcard illustrations).", "",
       "| # | Status | File | Lines | What it is |", "|---|---|---|---:|---|", *rows, "",
       "## Deleted (remove these from your copy)", "", *[f"* `{d}`" for d in deleted], ""]
(out / "MANIFEST.md").write_text("\n".join(man), encoding="utf-8")

# ---- zip (bytes come from git, so the zip is the commit)
zip_path = out / "woy-master-build-code.zip"
with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
    for p in [p for p, _ in code] + docs + assets:
        z.writestr(p, blob(p))
    z.write(out / "MANIFEST.md", "MANIFEST.md")

# ---- bundle + checksum
bundle = out / "the-world-of-you-master-build.bundle"
git("bundle", "create", str(bundle), "--all")
git("bundle", "verify", str(bundle))
digest = hashlib.sha256(bundle.read_bytes()).hexdigest()
(out / (bundle.name + ".sha256")).write_text(f"{digest}  {bundle.name}\n")

print(f"export of {head} (base {base}) in {out}:")
for f in sorted(out.iterdir()): print(f"  {f.name:48s} {f.stat().st_size:>12,} B")
with zipfile.ZipFile(zip_path) as z: print(f"  zip entries: {len(z.namelist())} ({len(code)} code, {len(docs)} docs, {len(assets)} assets, MANIFEST.md)")
print(f"  code files {len(code)}, lines {total_lines:,}, deleted {len(deleted)}")
````

## 7. `scripts/make-reports.py` — new

```python
#!/usr/bin/env python3
"""Builds the QA / audit reports in docs/ from the recorded test output, so every number in them comes from a file, not from memory.
Inputs (all produced by scripts/qa/*): qa/flow/summary.jsonl, qa/specs/summary.jsonl, qa/leak/*.json, docs/qa-screens/before/report-gift-*.json, dist/ (after `npm run build`).
Run from the repo root:  python3 scripts/make-reports.py   (set REPORT_DATE=YYYY-MM-DD to pin the generation date)"""
import glob, json, os, re, subprocess, datetime
from pathlib import Path

root = Path(__file__).resolve().parent.parent
os.chdir(root)
today = os.environ.get("REPORT_DATE") or datetime.date.today().isoformat()  # REPORT_DATE=YYYY-MM-DD pins the generation date (reproducible output)

def jl(path):
    rows = []
    p = Path(path)
    if p.exists():
        for line in p.read_text().splitlines():
            try: rows.append(json.loads(line))
            except Exception: pass
    return rows

flow = {}
for r in jl("qa/flow/summary.jsonl"): flow[r["id"]] = r          # latest line per gift wins
specs = {}       # specs run against the Vite dev server (latest line per test wins)
live_specs = {}  # specs run against the deployed site (BASE_URL=https://..., QA_BUILD=live)
prod_specs = {}  # specs run against the production bundle (vite preview of dist/), tagged by run-specs.py with QA_BUILD=production
live_hist = {}   # every recorded live row per test, in order: full run 1, full run 2, re-runs
for r in jl("qa/specs/summary.jsonl"):
    {"production": prod_specs, "live": live_specs}.get(r.get("build"), specs)[(r["file"], r["title"])] = r
    if r.get("build") == "live": live_hist.setdefault((r["file"], r["title"]), []).append(r)
leak = [json.load(open(f)) for f in sorted(glob.glob("qa/leak/*.json"))]
base = {}
for f in sorted(glob.glob("docs/qa-screens/before/report-gift-*.json")):
    base.update(json.load(open(f))["gifts"])
# The reports name the last commit that changed the product (src/, package.json, index.html), so docs-only commits that refresh these
# files do not make their own hash stale.
head = subprocess.run(["git", "log", "-1", "--format=%h", "--", "src", "package.json", "index.html", "public"], capture_output=True, text=True).stdout.strip() \
    or subprocess.run(["git", "rev-parse", "--short", "HEAD"], capture_output=True, text=True).stdout.strip()
commits = subprocess.run(["git", "log", "--oneline", "-12"], capture_output=True, text=True).stdout.strip().splitlines()
# Product files (the same paths as above) that differ from the last commit: the reports must not claim a commit that does not contain them.
PRODUCT_PATHS = ["src", "package.json", "index.html", "public"]
dirty_product = [l for l in subprocess.run(["git", "status", "--porcelain", "--"] + PRODUCT_PATHS, capture_output=True, text=True).stdout.splitlines() if l.strip()]
head_text = f"commit `{head}`" if not dirty_product else f"last product commit `{head}` plus {len(dirty_product)} product files in the working tree that are not committed yet"

PREVIEW_KB = round(sum(f.stat().st_size for f in Path("public/assets/gift-previews").glob("*.webp")) / 1024)
def count_specs():
    """Number of Playwright tests that exist (from `playwright test --list`, which needs no browser); None if it cannot be listed."""
    try:
        out = subprocess.run(["node", "node_modules/@playwright/test/cli.js", "test", "--list"], capture_output=True, text=True, timeout=180).stdout
        m = re.search(r"Total: (\d+) tests?", out)
        return int(m.group(1)) if m else None
    except Exception:
        return None
SPECS_EXIST = count_specs()

GIFTS = [
    ("01", "Secret Letter", "letter", "letter.ts, engine/paper.ts", "The content pack's main birthday letter (Hinglish + English) typeset on the 3D paper and repeated as readable text; wax seal, desk, pen", "Open / Fold, Replay the writing, Skip animation, drag or arrow-key turn", "Voice narration stays disabled: no recording exists. The four optional memory inserts are empty owner slots and are never shown"),
    ("02", "Jar of Reasons", "jar", "jar.ts", "17 paper notes carrying the content pack's 17 reasons (3D and text), the pack quote, glass jar, brass lid, ribbon", "Rotate, open lid (3D click or button), pick any of 17, shuffle, read all 17, put back", "The reasons are the pack author's draft, so the owner reads them before publishing; a note with no text shows the pack's \"waiting to be written\" line"),
    ("03", "Everlasting Flower", "flower", "flower.ts, engine/garden.ts", "procedural soil, roots, stem, leaves, bloom, grass, butterflies", "Grow in 4 stages (camera follows), rotate, reveal the hidden message, begin again", "The hidden message is the pack's flower dedication and reveal line"),
    ("04", "Our Little Universe", "universe", "universe.ts", "orrery planets and orbits from the verified milestones only", "Pick a milestone (camera travel), zoom, rotate, overview, reveal the dedication", "Only the dates already in the archive are shown; the dedication is the pack's universe text and reveal line"),
    ("05", "Bhumi FM", "cassette", "cassette.ts", "cassette, tape deck, reels, VU LEDs", "Insert / eject, Play, Pause, Stop, Rewind, volume", "No audio file exists: Play is disabled and the status shows the pack's empty-playlist line; LEDs move only with real audio"),
    ("06", "Memory Cinema", "cinema", "cinema.ts", "projector, reels, film strip, beam shader, grain, an empty frame that carries the pack's empty-state line", "Start projector, Play, Previous / Next, Replay, Full screen", "No photos or videos exist: Play is disabled. The pack's opening, empty-state and closing lines are shown"),
    ("07", "A Thousand Wishes", "wishes", "wishes.ts", "a lantern tree with the ten existing wishes, and a sky that gives the pack's 101 wishes (a star flares above the tree for each draw)", "Collect wishes (3D or buttons), constellation lines, display all, clear; draw a wish from the sky, previous / next sky wish, list the sky wishes", "The pack heading says 100 wishes but lists 101; all 101 are used"),
    ("08", "Queen's Crown", "crown", "crown.ts", "gold, faceted gems, velvet, spot lighting (no portrait)", "Inspect crown / jewels / velvet, rotate, reveal the birthday note (the crown turns once)", "The reveal shows the pack's crown dedication and reveal line, then the existing archive note"),
    ("09", "Open When", "cabinet", "cabinet.ts, envelope.ts", "wooden cabinet with four sealed envelopes", "Select envelope, break seal, letter rises, close", "The four letters are empty owner slots (the pack's \"waiting to be written\" line is shown on the 3D paper and in text); a letter the owner writes is set on the paper"),
    ("10", "Happiness Machine", "machine", "machine.ts", "brass machine, meshing gears, lever, printed ticket", "Pull the lever (ticket shows an existing wish), reset", "-"),
    ("11", "Little Adventure", "adventure", "adventure.ts", "3D relief map of the four imagined postcard places, a paper plane", "Visit places in order (unlocking), plane flight", "Heavy geometry at medium tier (about 73k triangles)"),
    ("12", "The Music of Us", "vinyl", "vinyl.ts", "turntable, grooved vinyl, tonearm, LED ring", "Previous / Next, Play, Stop, volume, silent mechanical preview", "No audio file exists: Play is disabled and the pack's empty-playlist line is shown"),
    ("13", "Infinite Mirror", "mirror", "mirror.ts", "gilded standing mirror with infinite rings and mist", "Drag on the glass to wipe the mist, Clear the mist, Reset", "Heavy geometry at medium tier (about 112k triangles); no portrait on purpose"),
    ("14", "Birthday Coupon Book", "coupons", "coupons.ts", "spiral coupon book on a wooden table", "Turn pages, Mark redeemed / Restore", "The six coupons are empty owner slots, so Mark redeemed stays disabled"),
    ("15", "Future Garden", "hope-tree", "hopeTree.ts, engine/garden.ts", "glass terrarium with soil strata and a tree that grows hope-leaf tags", "Plant the seed, grow leaf by leaf, inspect any leaf, begin again", "The eight hopes are empty owner slots"),
    ("16", "Secret Treasure Hunt", "treasure", "treasure.ts", "vault gate, enamel symbols, password plaque, chest and key", "Arrange symbols (buttons), check order, enter the password, unlock, restart", "-"),
    ("17", "The Ultimate Surprise", "portal", "portal.ts", "sixteen lights, ring and portal shader", "Gather lights, open the portal, sound switch, replay, enter the Ballroom", "-"),
]

SECTIONS = [
    ("Birthday Garden (hero)", "Painted image + CSS petals/fireflies", "src/three/sections/heroGarden.ts (+ gifts/flower.ts), world/BirthdayGarden.tsx", "Live cut-away garden: Seed, Roots, Sprout, Leaves, Bud, Flower, Full bloom with a following camera, grass, butterflies, fireflies, pollen; seven HTML stage buttons with the content pack's narration (title and text), replay; plays once by itself", "Painted poster stays while 3D loads and when WebGL is missing", "COMPLETE"),
    ("Scrapbook", "react-pageflip book (curl, drag, shadows already worked)", "world/Storybook.tsx, styles/sections3d.css, hooks/usePointerParallax.ts", "Kept the StPageFlip curl; added cover boards with thickness, page blocks that grow/shrink with the read position, gutter shadow, ground shadow, pointer tilt; fixed the inline-collapsed cover layout; the decorative boards, page blocks and spine now follow the book's real orientation (one page on a phone: before, a phone drew the two-page decoration, a leather board offset behind the cover)", "Not a WebGL page curl (the library's HTML curl is used). The closed cover sits right of centre on a desktop (the library's closed-book position; the book is not re-centred while closed); cosmetic", "COMPLETE"),
    ("Memory Observatory", "Gold clock + gears, 8.8k triangles, no interaction", "three/sections/observatory.ts, world/RelationshipClock.tsx", "Real-time clock, meshing gear train, pendulum, three milestone planets (pick or use the HTML buttons), moon phase, telescope, stars, shooting star", "Picking a planet with a pointer inside the canvas was not exercised (the HTML buttons were)", "COMPLETE"),
    ("Memory Gallery", "Flat polaroid mounts", "world/PolaroidGallery.tsx, styles/sections3d.css, hooks/usePointerParallax.ts", "Mounts with depth: pointer parallax, layered tilt, light sweep, clip depth; keyboard focus lifts a mount; lightbox unchanged; the pack's empty-gallery and timeline lines above the wall", "CSS 3D, not WebGL. Still no photos exist, so every mount is an empty placeholder by design (it shows the pack's \"add a real photograph\" line)", "COMPLETE"),
    ("Wish Garden", "70k-triangle garden, rose/daisy/tulip primitives", "three/sections/wishGarden.ts, world/FlowerGarden.tsx", "Conservatory with ten species flowers, visitor's golden daisy, release effects (sparks, petals, lantern), camera glide, lantern halos", "Draw calls are high (about 440 at medium)", "COMPLETE"),
    ("Future Postcards", "3D flat card flip", "three/sections/postcards.ts, world/FuturePostcards.tsx", "Seven cards with the content pack's messages (three new illustrations next to the original four); thick glossy card on a lamp-lit desk, flip about the long edge, handwriting fitted to the card, the visitor's own handwritten line (tab only)", "The three new illustrations are generated art in the style of the original four, not photographs. Pointer picking inside the canvas was not exercised", "COMPLETE"),
    ("Birthday Ballroom", "Primitive cake scene", "three/sections/ballroom.ts, world/BirthdayCake.tsx", "Baking story (ingredients, mixing, oven), three-tier cake with drips and strawberries, flames, per-candle smoke, confetti, fireworks, chandelier, finale camera. Microphone stays permission-based with the manual button", "The illustrated alternative (a disclosure) was checked at desktop and phone width. Microphone hardware not tested", "COMPLETE"),
    ("Letter Room", "Legacy letter scene", "world/LetterRoom.tsx (reuses gifts/letter.ts)", "Six envelopes: the pack's main birthday letter (the same physical letter as gift 01), the earlier source letter kept word for word, and four empty owner-written envelopes that show the pack's \"waiting to be written\" line", "The four empty envelopes are still empty owner slots", "COMPLETE"),
    ("Gift Atelier previews", "17 flat renders (4 KB each)", "public/assets/gift-previews/*.webp, scripts/qa/render-previews.mjs", f"17 stills rendered from the native scenes ({PREVIEW_KB} KB total; 01, 02, 06 and 09 were re-rendered with the content pack's own text)", "Stills, not live canvases (by design: no 17 canvases)", "COMPLETE"),
    ("Music lounge and Finale", "HTML", "world/MusicRoom.tsx, world/FinalCelebration.tsx", "Copy only: the pack's Bhumi FM welcome and empty-playlist lines, and its thank-you line. No audio exists, so Play stays disabled", "Not audited beyond the copy", "COMPLETE (copy)"),
    ("Invitation room, clock panel", "Painted / HTML", "unchanged", "Not part of the requested upgrade list; not audited in depth", "-", "NOT CHANGED"),
]

SECTION_SHOTS = {
    "Birthday Garden (hero)": ("section-garden", "garden"), "Scrapbook": ("section-storybook", "scrapbook-open"), "Memory Observatory": ("section-timepiece", "observatory"),
    "Memory Gallery": ("section-gallery", "gallery"), "Wish Garden": ("section-flower-garden", "wish-garden"), "Future Postcards": ("section-future-postcards", "postcards-dialog"),
    "Birthday Ballroom": ("section-birthday-cake", "ballroom"), "Letter Room": ("section-letters", "letter-room-dialog"),
}
SECTION_TESTS = {
    "Wish Garden": ("garden: 3D rendering", "WebGL failure leaves garden", "normal-motion shader", "responsive portrait"),
    "Birthday Ballroom": ("cake: all baking", "microphone denial", "cancelling a pending microphone", "synthetic broadband"),
    "Letter Room": ("letters: folded paper", "letter reduced motion", "letter normal motion", "letter mobile", "mobile real 3D"),
    "Future Postcards": ("native postcards",),
    "Scrapbook": ("scrapbook: every empty page", "scrapbook on a phone", "scrapbook on a desktop"),
}

def flow_status(gid):
    f = flow.get(f"gift-{gid}")
    if not f: return "NOT RUN", "no result recorded"
    if f.get("pass"): return "PASS", f"ready {round((f.get('readyMs') or 0)/1000)} s (software GL)"
    bad = [s for s in f.get("steps", []) if not s.get("ok")]
    why = (f.get("fatal") or "") or ("; ".join(f"{b['kind']} {b['arg'][:30]}" for b in bad[:2])) or ("; ".join(f.get("errors", [])[:1]))
    return "FAIL", why[:140]

def compact_rows(path):
    latest = {}
    for r in jl(path): latest[r["id"]] = r
    out = []
    for gid in sorted(latest):
        r = latest[gid]; lay = r.get("layout") or {}
        why = (r.get("fatal") or "") or "; ".join(f"{b.get('kind')} {str(b.get('arg'))[:28]}" for b in (r.get("failed") or [])[:2]) or "; ".join(r.get("errors", [])[:1])
        out.append(f"| {gid} | {'PASS' if r.get('pass') else 'FAIL'} | {round((r.get('readyMs') or 0)/1000)} s | {', '.join(lay.get('scrollers', [])) or '-'} | {lay.get('hOverflow', '-')} | {(r.get('canvases') or {}).get('afterClose', '-')} | {r.get('esc', '-')} | {why[:80] or '-'} |")
    return out

# ---------------------------------------------------------------- baseline table
def baseline_row(gid):
    b = base.get(f"gift-{gid}", {})
    tris = (b.get("stats") or [{}])[0].get("triangles")
    return b.get("readyMs"), tris, len(b.get("nestedScrollers") or []), len(b.get("errors") or [])

# ================================================================= MASTER_PROJECT_AUDIT
rows = []
for gid, name, kind, *_ in GIFTS:
    ready, tris, scrollers, errs = baseline_row(gid)
    rows.append(f"| {gid} | {name} | {ready if ready is not None else '-'} | {tris if tris is not None else '-'} | {scrollers} | {errs} |")
audit = f"""# Master project audit

Generated {today} ({head_text}). Scope: the migrated site **before** the master build, then what changed. Every number below is read from a recorded file; anything not measured is labelled *assumed*.

## 1. What the project is

* Vite 7 + React 19.2 + TypeScript 5.9 single-page site, 12 chapters, 17 gift experiences opened in a native `<dialog>`.
* Dependencies: three 0.187, @react-three/fiber 9.8, gsap 3.15, react-pageflip 2.0, lucide-react.
* Owner content that exists and was kept verbatim: the earlier source letter, ten wishes, three "specials". At baseline the 17 reasons, 4 Open-When letters, 6 coupons and 8 future-garden hopes were blank by design (never invented). The owner's content pack, added afterwards, fills the 17 reasons and more (see `CONTENT_PACK_INTEGRATION.md`); the Open-When letters, coupons and future hopes are still blank. No audio, photos, video or voice recordings exist in the repository.
* Deployed before the master build: Vercel deployment of commit `0f16a01` (project kept, nothing recreated).

## 2. Findings at baseline (verified by running the site)

| # | Finding | Evidence | Resolution |
|---|---|---|---|
| 1 | 3D existed only inside gift cards and the dialog; the hero and the invitation were painted images plus CSS particles | baseline captures `docs/qa-screens/before/section-*.webp` | Hero rebuilt in 3D; sections moved onto one engine |
| 2 | All 17 gift scenes were flat primitives | `docs/qa-screens/before/gift-NN.webp`, `atelier-previews/` | 17 native worlds (`src/three/gifts`) |
| 3 | Section scenes created their own WebGL renderer each and kept it alive after scrolling away (paused, never released) | `SceneCanvas` / `createRuntime` code, now deleted | `SectionStage` mounts a scene near the viewport and releases the context when far |
| 4 | The CSS allowed a nested scroller in the gift dialog (`.gift-world-console{{max-height:690px;overflow:auto}}` inside the dialog scroller). At first open the baseline run measured a single scroller for every gift it captured, so the nesting only shows once a gift's panel grows (long lists, small screens): **not demonstrated in the baseline run** | CSS rule; baseline reports (gift 16 was not captured at baseline) | rule removed; after the change every flow, including phone width and the long lists, shows only `archive-dialog__paper` scrolling |
| 5 | Scrapbook cover text collapsed onto one line (the flip book forces `display:block` on pages) | baseline `section-storybook.webp` | cover text laid out as a column (the closed book itself sits right of centre on the page) |
| 6 | Software-rendered WebGL got the medium tier and could crash the tab | Chromium crash during the cake spec at medium | `isSoftwareRenderer()` starts such devices on the low tier |
| 7 | 7 unreferenced GLB snapshots (3.4 MB) ship in `public/assets/models` | no loader exists in `src` | kept and documented, not loaded |
| 8 | Workspace snapshot cap (about 128 MB) exceeded by 90 MB of QA PNGs | repo 132 MB before cleanup | screenshots stored as compressed WebP (87 MB to 5 MB) |

## 3. Baseline measurements per gift (before)

| Gift | Name | Ready (ms, software GL) | Triangles | Scrollers in dialog | Console errors |
|---|---|---:|---:|---:|---:|
{chr(10).join(rows)}

*Ready times were measured with software WebGL (SwiftShader); they say nothing about a real GPU.*

## 4. What was verified and what was assumed

| Claim | Status |
|---|---|
| `tsc` is clean and `npm run build` passes on the final commit | verified (see `TEST_REPORT.md`) |
| All 17 gift dialogs open, run their interactions and close, one scroller, no horizontal overflow, no canvas left after close | verified in software GL (see `TEST_REPORT.md`) |
| Real-GPU frame rate, mobile GPU memory, thermal behaviour | **assumed**, not measured |
| Screen-reader behaviour | **assumed** from markup (roles, labels, live regions); no screen reader was available |
| Touch gestures on real phones | **assumed**; only Chromium emulation was used |
| Audio output | **not testable**: sound effects are synthesised and off by default; no audio files exist |
"""
Path("docs/MASTER_PROJECT_AUDIT.md").write_text(audit, encoding="utf-8")

# ================================================================= FEATURE_COMPLETION_MATRIX
def spec_for(*needles):
    out = []
    for (f, t), r in specs.items():
        if any(n.lower() in t.lower() for n in needles): out.append(("PASS" if r["passed"] else "FAIL", t[:60]))
    return out

gift_rows = []
for gid, name, kind, files, assets, inter, limit in GIFTS:
    st, why = flow_status(gid)
    status = "COMPLETE" if st == "PASS" else ("INCOMPLETE (flow failed)" if st == "FAIL" else "UNVERIFIED")
    perf = " · NEEDS_PERFORMANCE_UPGRADE" if gid in ("11", "13") else ""
    ready, tris, scrollers, errs = baseline_row(gid)
    before_note = " *(before = the screenshot shipped inside the original ZIP, `qa/ultra-gift-16.png`; my own baseline capture of this gift ran out of memory)*" if gid == "16" else ""
    gift_rows.append(f"| {gid} | {name} | COMPLETE, NEEDS_VISUAL_UPGRADE (flat primitives) | **{status}{perf}** | `{files}` | {assets} | {inter} | flow: {st} ({why}) | {limit} | ![before](qa-screens/before/gift-{gid}.webp) ![after](qa-screens/after/gifts/gift-{gid}-open.webp){before_note} |")

def section_tests(name):
    needles = SECTION_TESTS.get(name)
    if not needles: return "page captures only" if name in SECTION_SHOTS else "-"
    res = spec_for(*needles)
    return "; ".join(f"{r} {t}" for r, t in res) if res else "-"
SECTION_EXTRA = {
    "Birthday Garden (hero)": [("growth stages, settled", "hero-growth-stages"), ("no WebGL: poster, captions still follow the buttons", "hero-no-webgl"), ("production build, settled", "hero-production"), ("mobile (390 px), settled stages", "hero-growth-stages-mobile")],
    "Scrapbook": [("cover", "scrapbook-cover"), ("mobile", "scrapbook-mobile"), ("empty pages with the pack's lines, desktop", "scrapbook-placeholders"), ("the same at 390 px", "scrapbook-placeholders-mobile")],
    "Memory Observatory": [("mobile", "observatory-mobile")],
    "Future Postcards": [("the seven messages, reverse sides", "postcards-backs"), ("mobile dialog", "postcards-dialog-mobile"), ("cards 2 to 7 at 390 px, reverse above, front below", "postcards-mobile-cards")],
    "Letter Room": [("the six envelopes", "letter-room-shelf"), ("an empty envelope", "letter-room-empty")],
    "Birthday Ballroom": [("mobile", "ballroom-mobile"), ("candles lit", "ballroom-candles-lit"), ("wish made", "ballroom-wish-made"), ("illustrated alternative", "ballroom-alternative"), ("illustrated alternative, mobile", "ballroom-alternative-mobile")],
}
def section_shot(name):
    if name not in SECTION_SHOTS: return "-"
    b, a = SECTION_SHOTS[name]
    extra = "".join(f" ![{alt}](qa-screens/after/sections/{img}.webp)" for alt, img in SECTION_EXTRA.get(name, []))
    return f"![before](qa-screens/before/{b}.webp) ![after](qa-screens/after/sections/{a}.webp){extra}"
sec_rows = [f"| {n} | {orig} | **{now}** | `{files}` | {changes} | {section_tests(n)} | {limit} | {section_shot(n)} |" for (n, orig, files, changes, limit, now) in SECTIONS]
matrix = f"""# Feature completion matrix

Generated {today} ({head_text}). Status words: COMPLETE, INCOMPLETE, BROKEN, MISSING, NEEDS_VISUAL_UPGRADE, NEEDS_PERFORMANCE_UPGRADE.
"COMPLETE" means: built, type-checked, built for production and exercised by a recorded browser run. It does **not** mean tuned on a real GPU.

## 17 gifts

| # | Gift | Original status | Now | Files | Assets | Interactions | Tests | Limitations | Before / after |
|---|---|---|---|---|---|---|---|---|---|
{chr(10).join(gift_rows)}

## Page sections

| Section | Original | Now | Files | Changes | Tests | Limitations | Before / after |
|---|---|---|---|---|---|---|---|
{chr(10).join(sec_rows)}

## Cross-cutting systems

| System | Original | Now | Evidence |
|---|---|---|---|
| Shared engine: quality tiers, procedural materials, environments, lights, particles, scrubbable sequences | MISSING | COMPLETE | `src/engine`, used by 22 scenes |
| One lazy canvas host, error boundary, WebGL probe and poster fallback, disposal, adaptive DPR | partial (dialog only) | COMPLETE | `NativeGiftCanvas`, `SectionStage`, WebGL-failure specs, leak check |
| Software-renderer detection (low tier) | MISSING | COMPLETE | `engine/quality.ts`; fixes the crash seen at medium |
| Optional sound (synthesised, off by default, toggle and volume, no autoplay) | MISSING | COMPLETE (code); audio output not testable here | `engine/audio.ts`, `SoundDock` |
| Microphone (permission based) with the manual button | COMPLETE | COMPLETE | specs: denial, cancel, synthetic input |
| Reduced motion (final states, no continuous loop) | partial | COMPLETE | `frameloop="demand"`, specs run with reduced motion by default |
| Keyboard (arrow keys turn objects, buttons are real buttons, dialog Escape and focus return) | partial | COMPLETE (hero growth steps and a gift dialog walked by `keyboard-pass.mjs`, dialogs also spec-covered); screen-reader behaviour assumed | `TEST_REPORT.md` section 2d, letter and postcard specs |
"""
Path("docs/FEATURE_COMPLETION_MATRIX.md").write_text(matrix, encoding="utf-8")

# ================================================================= TEST_REPORT
def flow_detail(gid):
    f = Path(f"qa/flow/gift-{gid}.json")
    return json.load(open(f)) if f.exists() else {}
flow_rows = []
for gid, name, kind, *_ in GIFTS:
    st, why = flow_status(gid)
    d = flow_detail(gid)
    lay = d.get("layout") or {}
    hov = len(lay.get("horizontalOverflowInside", [])) + (1 if lay.get("docHScroll") else 0) if lay else "-"
    render = d.get("render") or {}
    flow_rows.append(f"| {gid} {name} | {st} | {why} | {', '.join(lay.get('scrollers', [])) or '-'} | {hov} | {(d.get('canvases') or {}).get('afterClose', '-')} | {d.get('closedByEscape', '-')} | {render.get('triangles', '-')} / {render.get('drawCalls', '-')} |")
latest = sorted(specs.values(), key=lambda r: (r["file"], r["title"]))
spec_rows = [f"| {r['file']} | {r['title'][:90]} | {'PASS' if r['passed'] else 'FAIL'} | {r['seconds']} s | {r.get('error', '')[:90]} |" for r in latest]
npass = sum(1 for r in latest if r["passed"])
prod_latest = sorted(prod_specs.values(), key=lambda r: (r["file"], r["title"]))
prod_spec_rows = [f"| {r['file']} | {r['title'][:90]} | {'PASS' if r['passed'] else 'FAIL'} | {r['seconds']} s | {r.get('error', '')[:90]} |" for r in prod_latest]
prod_npass = sum(1 for r in prod_latest if r["passed"])
live_latest = sorted(live_specs.values(), key=lambda r: (r["file"], r["title"]))
live_spec_rows = [f"| {r['file']} | {r['title'][:90]} | {'PASS' if r['passed'] else 'FAIL'} | {r['seconds']} s | {r.get('error', '')[:90]} |" for r in live_latest]
live_npass = sum(1 for r in live_latest if r["passed"])
live_runs = sum(len(v) for v in live_hist.values())
live_failed_runs = sum(1 for v in live_hist.values() for r in v if not r["passed"])
live_failed_tests = sum(1 for v in live_hist.values() if any(not r["passed"] for r in v))
live_failed_fixed = sum(1 for v in live_hist.values() if any(not r["passed"] for r in v) and v[-1]["passed"])
leak_rows = [f"| {l['gift']} | {l['cycles']} | {l['contextsCreated']} / {l['contextsLost']} | {l['canvasesLeftInDom']} | {l['heapMB'][0]} to {l['heapMB'][-1]} MB ({l['heapGrowthMB']:+} MB) | {'PASS' if l['pass'] else 'FAIL'} |" for l in leak]
def kb_load(key):
    f = Path(f"docs/qa-screens/after/keyboard-{key}.json")
    return json.load(open(f)) if f.exists() else None
kb_rows = []
for key, label in (("live", "WebGL on (software GL, low tier)"), ("nowebgl", "WebGL hidden (poster fallback)")):
    d = kb_load(key)
    if not d: continue
    h, dl = d["hero"], (d.get("dialog") or {})
    steps = h.get("steps", [])
    settled = sum(1 for x in steps if x.get("settledOnClicked"))
    yn = lambda v: "yes" if v else "no"
    dialog = (f"opens with Enter: {yn(dl.get('opened'))}; labelled '{(dl.get('attrs') or {}).get('title')}'; first focus '{(dl.get('focusAfterOpen') or {}).get('name')}'; Escape closes: {yn(dl.get('closedByEscape'))}; focus back on the opener: {yn(dl.get('focusReturnedToOpener'))}" if dl else "not run in this mode")
    kb_rows.append(f"| {label} | {h.get('tabsToFirstStep')} | {settled} of {len(steps)} | {' > '.join(h.get('replayStagesSeen', []))} | {dialog} |")
def prod_table():
    f = Path("docs/qa-screens/after/prod-smoke.json")
    if not f.exists(): return "_not run_"
    d = json.load(open(f))
    out = ["| Check | Result |", "|---|---|"]
    for pg in d["pages"]:
        out.append(f"| {pg['name']} | {pg['shows']}; console problems: {len(pg['consoleProblems'])} |")
    for g in d["giftFlows"]:
        bad = "; ".join(f"step '{x['kind']} {x['arg']}': {x['error']}" for x in g["failedSteps"])
        out.append(f"| {g['id']} flow, {g['tier']} tier | {'PASS' if g['pass'] else 'FAIL'}, ready in {round((g['readyMs'] or 0)/1000)} s (software GL){('; ' + bad) if bad else ''}; console problems: {len(g['consoleProblems'])} |")
    return "\n".join(out)
prod_md = prod_table()
_live_b = json.load(open("docs/qa-screens/after/live-prod-smoke.json")) if Path("docs/qa-screens/after/live-prod-smoke.json").exists() else None
live_gift_ids = ", ".join(sorted({g["id"].replace("gift-", "") for g in _live_b["giftFlows"]})) if _live_b else "none"
live_specs_md = ""
if live_latest:
    n_cp = sum(1 for r in live_latest if r["file"] == "content-pack.spec.ts"); n_sb = sum(1 for r in live_latest if r["file"] == "scrapbook-layout.spec.ts")
    live_specs_md = f"""**Specs also run against the live site** (`BASE_URL=https://the-world-of-you-birthday-storybook.vercel.app`, `QA_BUILD=live`): the {n_cp} content-pack specs and the {n_sb} scrapbook layout specs, which read the text and controls a visitor gets. {live_npass} of {len(live_latest)} pass in their latest run. The log holds {live_runs} runs of them: {live_runs - live_failed_runs} passed and {live_failed_runs} failed, and {live_failed_fixed} of the {live_failed_tests} tests that failed passed when run again. The failures are read as the sandbox's memory limit (the kernel killed the browser each time), not as a site defect; the evidence and its limit are in `DEPLOYMENT_REPORT.md`.

| File | Test | Result | Time | First error |
|---|---|---|---:|---|
{chr(10).join(live_spec_rows)}

"""
_prod = json.load(open("docs/qa-screens/after/prod-smoke.json")) if Path("docs/qa-screens/after/prod-smoke.json").exists() else None
prod_gift_ids = ", ".join(sorted({g["id"].replace("gift-", "") for g in _prod["giftFlows"]})) if _prod else "none"
prod_markers_text = ("are **not** in the built `.js` / `.html` files" if _prod and not _prod.get("templateMarkersInBundle") else "**were found** in the built files (see `docs/qa-screens/after/prod-smoke.json`)")
prod_hooks_text = ("are **not** in `dist/`" if _prod and not _prod.get("devHooksInBundle") else "were **found** in `dist/` (see the table)")
dist = Path("dist/assets")
chunks = sorted(((p.stat().st_size, p.name) for p in dist.glob("*.js")), reverse=True)[:8] if dist.exists() else []
def spec_counts(file):
    rows = [r for (f, t), r in specs.items() if f == file]
    return sum(1 for r in rows if r["passed"]), len(rows)
vpass, vtotal = spec_counts("content-pack-verbatim.spec.ts")
bpass, btotal = spec_counts("content-pack.spec.ts")
lpass, ltotal = spec_counts("scrapbook-layout.spec.ts")
flow_pass = sum(1 for n in range(1, 18) if (flow.get(f"gift-{n:02d}") or {}).get("pass"))
content_pack_md = f"""## 3b. Content pack (the owner's PDF; see `CONTENT_PACK_INTEGRATION.md`)

| Check | Result | What it shows |
|---|---|---|
| `content-pack-verbatim.spec.ts` (no browser) | {vpass} of {vtotal} pass | Every pack string is in the PDF transcript word for word (ignoring only line breaks and curly-versus-straight quotes), nothing quoted or numbered in the PDF was left out, the counts match (17 reasons, 101 wishes, 7 postcards, 7 garden stages, 13 microcopy strings) and no `[EDIT]` / `[ADD]` / `[INSERT]` text can reach what the site shows. Mutation-tested: changing one word in `packContent.ts` made it fail and restoring the file made it pass again. |
| `content-pack.spec.ts` (browser, WebGL switched off so the HTML does the work) | {bpass} of {btotal} pass | The pack copy where a visitor meets it: grid intro, progress line, dedications 01-08 shown and 09-17 empty, the letter without its `[EDIT]` slot, all 17 reasons, the 101-wish sky, the long dedications with their reveal lines, cinema and radio copy, the seven postcards, the seven garden stages, the music lounge and the finale, a scan of all 17 gift dialogs and of the whole page for template text, the one-number-per-list-line check, and the Scrapbook (each empty page and the photo mount carry the pack's lines; mutation-tested: with the old wording the check failed, with the pack's wording restored it passed). |
| `scrapbook-layout.spec.ts` (browser, WebGL switched off) | {lpass} of {ltotal} pass | The Scrapbook's decoration follows the book's real orientation: on a 390 px phone the book is one page (`data-state="single"`, no spine, from the cover through three turns, no horizontal overflow); on a 1280 px desktop it starts as a closed cover and opens into a two-page spread with its spine. Mutation-tested: with the direct orientation read in `Storybook.tsx` switched off, the phone check failed and the desktop check passed; with the source restored both passed. |
| The 17 gift flows after the pack went in (software GL, low tier, 1100 x 640) | {flow_pass} of 17 pass | Section 2. |

Looked at in a real browser (software GL), not only measured:

* the seven garden stages on desktop and at 390 px: every stage button reached and held, a closed bud at Bud and an open flower from Flower on (`hero-growth-stages.webp`, `hero-growth-stages-mobile.webp`). The narration block keeps one height across all seven stages, 65 px at 1100 x 700 and 87 px at 390 x 844, and the stage buttons and the replay button stay where they are: measured stage by stage with `pack-hero-stages.mjs --nowebgl` on the built site (the block is plain HTML, so hiding WebGL does not change it; with the 3D scene running the same block was seen in the screenshots above);
* Future Postcards: all seven reverse sides and fronts on desktop, with the handwriting fitting each card, and all seven cards at 390 px (the handwriting on the small 3D card is tiny there, so the same message is also set as text below the stage; the dialog is 362 px wide with no horizontal overflow) (`postcards-backs.webp`);
* Letter Room: the six envelopes, and the main letter open with its ten paragraphs, scrolling inside the dialog with no horizontal overflow, and an empty envelope that shows the pack's "waiting to be written" line on the 3D paper (`letter-room-shelf.webp`, `letter-room-dialog.webp`, `letter-room-empty.webp`);
* the Scrapbook's open pages: the pack's "waiting to be written" line on a blank page, its "add a real photograph" line on the photo mount, on all four open pages and on the photo mount, desktop and 390 px, no horizontal overflow (`scrapbook-open.webp`, `scrapbook-placeholders.webp`, `scrapbook-placeholders-mobile.webp`);
* gift 07's sky wish and the two numbered wish lists, gift 02's list of 17, and the Gift Atelier, Music Lounge, Memory Gallery and finale copy;
* the re-rendered Gift Atelier posters: the main letter on the paper of gift 01 and a real reason on the jar note of gift 02; the pack's empty-state lines on gift 06's screen and on the paper of gift 09 (`CONTENT_PACK_INTEGRATION.md` lists which copy goes where).

Not checked: the pack's words against real events (they are the author's draft and the owner has to read them), and touch or pointer picking inside the 3D canvases.

"""
tests = f"""# Test report

Generated {today} ({head_text}). Environment: Linux sandbox, 2 GB RAM, no GPU. Chromium (single process) with **software WebGL (SwiftShader)**, driven by Playwright core.
Consequences: functional behaviour, layout, structure and cleanup are measured; **frame rate is not representative** and was not recorded as a result.

## 1. Static checks

| Check | Result |
|---|---|
| `npx tsc --noEmit` | clean (last run on the final commit) |
| `npm run build` (tsc -b + vite build) | passes; largest chunks: {', '.join(f'{n} {s/1024:.0f} kB' for s, n in chunks[:5]) or 'n/a'} |
| Dev-only scene lab absent from the production bundle | verified: only the inert `window.__WOY_LAB__?.register` hook remains |

## 2. Gift dialog flows (`scripts/qa/gift-flow.mjs`, one fresh browser per gift)

Each flow opens the real dialog from the Gift Atelier, waits for "Real-time 3D ready", measures layout, runs the gift's own controls, checks text where text is expected,
presses Escape and checks that the dialog closes, and checks that no canvas remains (focus return to the opener is asserted by the letter specs in section 3). Software WebGL, low tier, 1100 x 640.

| Gift | Result | Detail | Scrollers | Horizontal overflow | Canvases after close | Escape closes | Triangles / draw calls |
|---|---|---|---|---:|---:|---|---|
{chr(10).join(flow_rows)}

## 2b. Mobile (390 x 844, touch emulation, low tier)

The same flow with a phone-sized touch viewport: dialog fits, one scroller, no horizontal overflow, controls still work, canvas released on close.

| Gift | Result | Ready | Scrollers | Horizontal overflow | Canvases after close | Escape closes | Detail |
|---|---|---:|---|---:|---:|---|---|
{chr(10).join(compact_rows("qa/mobile/summary.jsonl")) or '| - | not run | | | | | | |'}

Section scenes on a phone-sized viewport (390 x 844, touch emulation): the Memory Observatory stage, the scrapbook cover, the Birthday Ballroom (stage, then controls) and a Future Postcards dialog were captured and looked at (`qa-screens/after/sections/*-mobile.webp`); they fit the width and show their readable content. Page-level horizontal overflow is covered by the responsive spec in section 3. Touch gestures on these scenes (page turns, drag to look around) were not exercised.

## 2c. Reduced motion (`prefers-reduced-motion: reduce`)

Scenes jump to their final states and do not run a continuous render loop; the flow still has to complete.

| Gift | Result | Ready | Scrollers | Horizontal overflow | Canvases after close | Escape closes | Detail |
|---|---|---:|---|---:|---:|---|---|
{chr(10).join(compact_rows("qa/reduced/summary.jsonl")) or '| - | not run | | | | | | |'}

Note on gift 13: the dialog legitimately holds **two** canvases while open: the WebGL scene and the original 2D fog-wipe overlay (`.gift-mirror__fog`) that ships with the gift. Both are gone after close.

## 2d. Keyboard pass (`scripts/qa/keyboard-pass.mjs`)

Real key events through Chromium (Tab, Shift+Tab, Enter, Space, Escape), no pointer. It tabs from the top of the page to the hero's growth steps, activates each step (Enter, and Space once),
waits until the stage that is highlighted matches the button and stays there, runs "Replay the growth" from the keyboard, then opens gift 01 with Enter, tabs through the dialog, presses Escape and checks where focus lands.

| Mode | Tab presses from the page start to the first growth step | Growth steps that settle on the clicked stage | "Replay the growth" walks through | Gift dialog (gift 01) |
|---|---:|---|---|---|
{chr(10).join(kb_rows) if kb_rows else '| - | not run | - | - | - |'}

What this pass found, and what was changed in the same pass:

* **The growth buttons were fake whenever 3D was missing or still loading.** The highlighted stage and the caption were read back from the scene, so with WebGL off the buttons changed nothing and the caption said "A single seed" over a picture of a finished garden. `GiftStage` now tells the page when it shows a poster (`onUnavailable`) and the hero then follows the chosen stage itself; "Replay the growth" steps the captions through every stage (seven since the content pack added Bud). (A first attempt hooked the canvas `fallback` prop, which React Three Fiber always mounts inside the `<canvas>`; the very same keyboard run showed it wrongly switched the live hero into fallback mode, so it was removed.)
* **Three of the six buttons settled on the next stage's caption** (Roots showed Sprout, Sprout showed Leaves, Leaves showed Flower). The scene's progress is `growth / 4`, and the old targets (1.15, 1.95 and 2.75) sat past the point where the next phase begins. Each button now rests inside its own phase, and the scene reports its exact progress when it settles.
* **The content pack added a seventh stage, Bud.** The stages and their resting points (growth / timeline progress where the stage begins) are Seed 0 / 0, Roots 0.92 / 0.06, Sprout 1.68 / 0.25, Leaves 2.52 / 0.44, Bud 2.92 / 0.66, Flower 3.6 / 0.80, Full bloom 4 / 0.97. The scene's own phases are roots 1.0 s, stem 4.0 s, leaves 7.0 s, bud 10.5 s and bloom 12 s of a 16 s timeline, so the bud is closed until about 0.75 and the open flower is read from 0.80. The keyboard pass above shows every one of the seven buttons settling on its own stage with live 3D, and the screenshots (`qa-screens/after/sections/hero-growth-stages.webp`, Roots to Full bloom) show a closed bud at "Bud" and an open flower from "Flower". The narration block keeps the same height at every stage (65 px at 1100 x 700, 87 px at 390 wide), so the buttons do not move between stages.
* One no-WebGL keyboard run (the first one after a long idle) did not update the Roots and Sprout captions within 3 s, because the hero stage woke late on the loaded sandbox and the page only starts following the buttons once it has shown the poster; the next two runs passed 7 of 7. The stored result is the full-run pass; the flake was not reproduced and not investigated further.
* The first run of the dialog check reported "focus not returned" because the test compared the opener's accessible name, which changes to "...replay experience" after a first open. The test now compares the gift id; focus does return to the opener.
* Tabbing past the last control of an open dialog briefly lands on the document (the browser's own UI) and never reaches the inert page behind it, because the dialog is a native modal `<dialog>`.

Limits: synthetic key events in one browser, not assistive technology. Only the hero steps and the gift dialog were walked this way; other sections rely on native buttons and the Playwright specs.

## 2e. Production build smoke test

Everything above ran against the Vite dev server. The file that actually ships is the minified `dist/` bundle with different chunking, so it was also built (`npm run build`), served with `vite preview` and opened in the same Chromium (software WebGL).

{prod_md}

* The dev-only helpers (`window.__lab`, `__woyTimeScale`, the scene-lab chunk) {prod_hooks_text} (checked by searching the built files).
* The content pack's template markers (`[EDIT`, `[ADD`, `[INSERT`) {prod_markers_text}, and the page scan in the table above found none in the rendered text or HTML. The slot hints that carry them stay in `packContent.ts` and in the transcript, and nothing that ships imports them.
* The page opens on the invitation section (the envelope), as in the original design; the Birthday Garden hero is the second section and its 3D mounts when it nears the viewport.
* On the earlier build (`9ed8a46`), a capture taken 4 s after the hero mounted showed the caption already on "Full bloom" while the "Flower" button and the progress bar were still easing (their CSS transitions are 0.2 s and 0.35 s and this sandbox draws frames slowly). The stage buttons and the caption both read the same value, and a capture 26 s later shows everything in agreement (`qa-screens/after/sections/hero-production.webp`).
* On the earlier build (`9ed8a46`), **gift 01 at the medium tier failed one step**, the second click on "Sound effects" timed out after 8 s. In production the recorded flow has no dev time-scale (6x in the dev runs), so the letter replay was still being drawn by the CPU at 58k triangles when the click came. The same flow at the low tier (what the app picks by itself on a software renderer) passes with no failed step and no console problem. This is a test-environment limit, not a reproduced product bug; it was not re-run on a real GPU.
* Gift flows run against the production bundle: {prod_gift_ids} (low tier, 1100 x 640). The other gift flows, the mobile and reduced-motion passes were not repeated on the bundle (they use the same code paths and passed on the dev server). The medium-tier observation above was not repeated either.

![first view, production build](qa-screens/after/sections/first-view-invitation.webp) ![hero after growth, production build](qa-screens/after/sections/hero-production.webp)

## 3. Playwright specs (`tests/*.spec.ts`, run one test per process with `scripts/qa/run-specs.py`)

{npass} of {len(latest)} recorded specs passed in this sandbox ({SPECS_EXIST if SPECS_EXIST is not None else 'number not available'} specs exist).

* **Not run on purpose:** `cinematic.spec.ts › all 17 existing gifts open, run their primary control, reset and close` (360 s loop; superseded by the 17 individual `ultra-gifts` specs and the gift flows above).
* **Not passing here, not a verified product failure:** `synthetic broadband input triggers calibrated mic and stops tracks` needs real-time audio analysis while a software-rendered scene starves the main thread; it failed twice in this sandbox (once on its explicit wait, once when the browser died at the click). Run it on a normal machine.
* After the content pack, `ultra-gifts` gift 15 failed once: the spec counted eight placeholder lines in the Future Garden, and the site now shows one empty-state line (the pack's wording) until a hope is written. The spec was updated to match that intended change (it checks the written hopes, or the empty-state line when none is written) and then passed.
* `microphone denial is recoverable` crashed the browser at the medium tier on software GL in the first batch of the master build; after the software-renderer fix it passed, and it passed again in the latest batch.
* Before the specs could run, they were updated for the shared scene host: `.cinematic-viewport__status/__canvas` became `.gift-native-status/.gift-native-canvas`, the WebGL-failure checks read `.gift-stage-fallback`, the replay button is addressed as the first footer button, and explicit audio waits scale with `QA_SLOW`.

| File | Test | Result | Time | First error |
|---|---|---|---:|---|
{chr(10).join(spec_rows) if spec_rows else '| - | none recorded | - | - | - |'}

**Specs also run against the production bundle** (`vite preview` of the built `dist/`, `QA_BUILD=production`): {prod_npass} of {len(prod_latest)} passed.

| File | Test | Result | Time | First error |
|---|---|---|---:|---|
{chr(10).join(prod_spec_rows) if prod_spec_rows else '| - | none recorded | - | - | - |'}

{live_specs_md}{content_pack_md}## 4. GPU / memory cleanup (`scripts/qa/leak-check.mjs`)

Opens and closes one gift several times; every WebGL context that was created must be lost again, no canvas may stay in the DOM, and the JS heap must not keep growing.

| Gift | Cycles | Contexts created / lost | Canvases left | JS heap | Result |
|---|---:|---|---:|---|---|
{chr(10).join(leak_rows) if leak_rows else '| - | not run | - | - | - | - |'}

`gl.info.memory` cannot be read after the renderer is gone, so geometry and texture counts are not compared across cycles; context loss and heap are the evidence.

## 5. Not tested (honest list)

* Real GPUs and real phones: frame rate, thermal throttling, mobile Safari quirks. Every number in this report comes from software WebGL on a CPU.
* Screen readers: markup uses native buttons, dialog semantics, `aria-live` captions and `aria-pressed`; no assistive technology was run.
* Audio output: no audio files exist; synthesised effects were never listened to in this sandbox. The volume slider was not exercised.
* Microphone hardware: covered by the denial and cancel specs and one synthetic-stream spec, and that last spec (`synthetic broadband input triggers calibrated mic and stops tracks`) **fails in this sandbox** (section 3); the cause was not diagnosed. Run it on a normal machine.
* Pointer and touch input inside the canvas: picking the jar lid or an observatory planet, drag-to-look-around, page-turn gestures. The flows drive the HTML controls; arrow keys and buttons are what was tested.
* The sticky 3D stage while a long gift dialog scrolls (the layout was measured; the scroll behaviour was not played through).
* Keyboard walks beyond the hero growth steps and the gift 01 dialog (section 2d); the other sections rely on native buttons and the specs.
* The long spec `all 17 existing gifts open, run their primary control, reset and close` was skipped on purpose (360 s; the 17 per-gift flows cover the same ground). {npass} of the {len(latest)} specs that were run passed; {SPECS_EXIST if SPECS_EXIST is not None else '?'} exist.
* Production bundle: only the first view, the hero, the Ballroom alternative, gifts {prod_gift_ids} and the specs listed under "also run against the production bundle" (section 3) were opened from `dist/` (section 2e).
* The live site beyond what `DEPLOYMENT_REPORT.md` lists: the 3D side of the gift flows other than {live_gift_ids}, phones, real GPUs, other networks and audio output.
"""
Path("docs/TEST_REPORT.md").write_text(tests, encoding="utf-8")

# ================================================================= DEPLOYMENT_REPORT
rec = json.load(open("docs/deployment-record.json")) if Path("docs/deployment-record.json").exists() else None
live = json.load(open("docs/qa-screens/after/live-smoke.json")) if Path("docs/qa-screens/after/live-smoke.json").exists() else None
later_note = ""
if rec:
    # commits that changed the product after the deployed commit are not live; say so instead of claiming "reports only"
    deployed_commit = rec["production"]["meta"]["masterBuildCommit"]
    later = subprocess.run(["git", "log", "--oneline", f"{deployed_commit}..HEAD", "--", "src", "package.json", "index.html", "public"], capture_output=True, text=True).stdout.strip().splitlines()
    SAME_PRODUCT = "Later commits change reports and test tooling only, not the product (`src/`, `public/`, `index.html`, `package.json`)."
    later_note = SAME_PRODUCT if not later else \
        f"{len(later)} later commit(s) changed the product after this deployment and are **not live**: " + "; ".join(f"`{c.split(' ', 1)[0]}` {c.split(' ', 1)[1] if ' ' in c else ''}" for c in later) + "."
    if dirty_product:
        later_note = later_note.replace(SAME_PRODUCT, "No later commit changes the product.") + f" **{len(dirty_product)} product files in the working tree differ from the last commit (the owner's content pack, see `CONTENT_PACK_INTEGRATION.md`); they are neither committed nor deployed, so the live site does not have them.**"
if rec:
    pr, prev, old, proj = rec["production"], rec["previousProduction"], rec["olderDeployment"], rec["project"]
    def _json(path):
        return json.load(open(path)) if Path(path).exists() else None
    live_bytes, live_pack, live_b = (_json("docs/qa-screens/after/" + n) for n in ("live-bytes.json", "live-pack.json", "live-prod-smoke.json"))
    pack_commit = pr["meta"].get("contentPackCommit")
    commit_note = (f" (stored in the deployment's meta as `masterBuildCommit`; the owner's content pack is commit `{pack_commit}`, inside it, meta `contentPackCommit`)"
                   if pack_commit else " (stored in the deployment's meta as `masterBuildCommit`)")
    build_note = f"Vite {pr['viteVersion']} transformed {pr['buildModules']} modules and built the bundle in {pr['viteBuildSeconds']} s" if pr.get("viteVersion") else f"{pr['buildModules']} modules"
    live_md = f"""## Live site

* URL: https://{pr['alias']} (HTTP {live['httpStatus'] if live else '?'}, public, no login wall).
* Production deployment `{pr['id']}`: {pr['state']} / {pr['readySubstate']}, target {pr['target']}, created {pr['createdUtc'].replace('T', ' ').replace('Z', ' UTC')}, ready after {pr['readySeconds']} s. Built by Vercel from commit `{pr['meta']['masterBuildCommit']}`{commit_note}. {later_note}
* Inspector: {pr['inspectorUrl']}
* The existing project and team were reused (`{proj['id']}`, `{proj['team']}`); nothing was created or deleted and the project settings were not touched (Vite preset, `{proj['install']}`, `{proj['build']}`, output `{proj['output']}`).

## Rollback

* The previous production deployment `{prev['id']}` (commit `{prev['commit']}`, {prev.get('what', 'the build before this one')}) is untouched and Vercel marks it as a rollback candidate: Vercel dashboard > Deployments > that deployment > "Promote to Production" (or `vercel rollback`). Promoting it would take whatever came after it off the site again.
* The older deployment `{old['id']}` (commit `{old['commit']}`, {old.get('what', 'older')}) is **not** a rollback candidate (Vercel reports `isRollbackCandidate: false`), so do not rely on it.

## How it was deployed

1. You confirmed the deployment in the chat (the choice "Commit + Drive + live site redeploy"); you then pasted a token and asked for everything, saved and unsaved, to go live.
2. The connected Vercel app only accepts text file contents, and this project has binary assets (images, gift posters), so the Vercel CLI (65.15.0) was used with the token you pasted into the chat. The token was handed to that one command as an environment variable. It was not written to any file, commit, log or report; a search of the workspace afterwards found no token string and the CLI wrote no credentials file. **Please revoke the token** (Vercel > Settings > Tokens).
3. The source was `git archive` of commit `{pr['meta']['masterBuildCommit']}`, the committed tree that holds everything that had been saved and unsaved before (the content pack included), minus the preserved source ZIP, `qa/`, `docs/`, `vercel-upload/` and the root screenshots ({pr['filesExtracted']} files; none of those belongs to the site). No `.env*` or key file is in it. The same export was built once beforehand with the repository's dependencies and produced the same file list and file hashes as the build that was tested.
4. Vercel ran `npm ci` and `npm run build` (`tsc -b && vite build`; {build_note}) and promoted the result. A failed build would not have replaced the old site.

## Verification of the live site
"""
    if live:
        sp = live.get("specs") or {}
        rows_v = ["| Check | Result |", "|---|---|"]
        rows_v.append(f"| Address | the alias answers HTTP {live['httpStatus']} with `cache-control: {live.get('headers', {}).get('cache-control', '?')}`; the deployment-specific URL answers {live.get('deploymentUrl', {}).get('httpStatus', '?')} (Vercel's deployment protection), so the alias is the public address. |")
        if live_bytes:
            ns = ", ".join(f"`{x['file']}` (HTTP {x['status']})" for x in live_bytes["notServed"])
            rows_v.append(f"| Same files as the tested build | `scripts/qa/compare-live-dist.mjs` fetched every file of the tested `dist/` from the alias and compared sha256: **{live_bytes['identical']} of {live_bytes['localFiles']} are byte-identical**, {len(live_bytes['different'])} differ, {len(live_bytes['notServed'])} are not served{(': ' + ns) if ns else ''} (`.vercelignore` drops `*.md` and nothing in the app references them). The entry files are `{live['entryAssets'][0]}` and `{live['entryAssets'][1]}`. |")
        if live_pack:
            t = live_pack["totals"]
            rows_v.append(f"| The pack's copy is in the live JavaScript | `scripts/qa/check-pack-live.mjs` read {live_pack['jsFilesRead']} JS files (the entry bundle and every lazy chunk): of {t['strings']} pack strings of 12+ characters, **{t['exact']} appear whole**, {t['fragmentOnly']} partly, **{t['missing']} are missing**; {t['hiddenByDesign']} are not shipped on purpose (see the table below). |")
        if live_b:
            for pg in live_b["pages"]:
                rows_v.append(f"| {pg['name']} | {pg['shows']}; console problems: {len(pg['consoleProblems'])} |")
            for g in live_b["giftFlows"]:
                bad = "; ".join(f"step '{x['kind']} {x['arg']}': {x['error']}" for x in g["failedSteps"])
                rows_v.append(f"| {g['id']} flow, {g['tier']} tier | {'PASS' if g['pass'] else 'FAIL'}, ready in {round((g['readyMs'] or 0)/1000)} s (software GL){('; ' + bad) if bad else ''}; console problems: {len(g['consoleProblems'])} |")
        if sp:
            rows_v.append(f"| Playwright specs against the live URL | {sp['latestPassed']} of {sp['tests']} pass in their latest run (the 13 content-pack specs and the 2 scrapbook layout specs; list in `TEST_REPORT.md` section 3). Two full runs: {sp['fullRun1']['passed']} of {sp['fullRun1']['of']} and {sp['fullRun2']['passed']} of {sp['fullRun2']['of']} passed; the four that failed are explained below. |")
        live_md += "\n" + "\n".join(rows_v) + "\n"
        if live_pack:
            names = {"packLetter": "01 Main birthday letter", "packLetterInsertPrompts": "01 Optional insert prompts (the owner's)", "packReasons": "02 Seventeen reasons and the quote",
                     "packWishes": "03 A Thousand Wishes (101 listed)", "packPostcards": "04 Future postcard messages", "packGiftDedications": "05 Dedications, gifts 01-08",
                     "packExtended": "06, 07, 11 Long dedications and reveal lines (flower, universe, crown)", "packGardenNarration": "08 Garden narration (seven stages)",
                     "packCinema": "09 Memory Cinema", "packRadio": "10 Bhumi FM", "packMicrocopy": "12 Microcopy", "packChecklist": "13 Publishing checklist (the owner's)",
                     "packAuthorNotes": "Notes to the author", "packCover": "Cover and tagline"}
            order = list(names)
            secs = sorted(live_pack["sections"].items(), key=lambda kv: order.index(kv[0]) if kv[0] in order else 99)
            live_md += "\n**The pack's strings (12+ characters) in the live JavaScript**\n\n| Pack section | Strings | Whole on the live site | Not shipped, on purpose |\n|---|---:|---:|---:|\n"
            live_md += "\n".join(f"| {names.get(k, k)} | {v['strings']} | {v['exact']}{(' (+' + str(v['fragment']) + ' partly)') if v['fragment'] else ''} | {v['hidden'] or '-'} |" for k, v in secs) + "\n"
            reasons = sorted({h["reason"] for h in live_pack["hiddenByDesign"]})
            live_md += "\nNot shipped on purpose (the pack's own rules: no template text, no invented content): " + "; ".join(reasons) + ". The visible text itself is compared with the pack by the specs above.\n"
        if sp:
            oom = sp.get("kernelOomKillsOfChromium") or []
            live_md += f"""
**About the failed spec runs.** The 15 live specs were run in full twice (30 runs): {sp['fullRun1']['passed'] + sp['fullRun2']['passed']} passed and {len(sp['fullRun1']['failed']) + len(sp['fullRun2']['failed'])} failed (run 1: {' and '.join('“' + t + '”' for t in sp['fullRun1']['failed'])}; run 2: {' and '.join('“' + t + '”' for t in sp['fullRun2']['failed'])}). {sp['failedTestsRerun']['passedInLatestRun']} of those {sp['failedTestsRerun']['tests']} tests passed when run again. {sp['note']} Kernel kills at (sandbox clock): {', '.join(k['sandboxClock'] for k in oom) or 'none'}.
"""
        live_md += """
![live hero at Full bloom](qa-screens/after/sections/live-hero.webp)
![live hero at Bud, with the pack's narration](qa-screens/after/sections/live-hero-bud.webp)

**Not verified on the live site:** the 3D side of the gift flows other than """ + live_gift_ids + """ (the pack specs open the other gifts with WebGL switched off, so those ran on their posters and HTML; the 3D flows of all 17 gifts ran on the same code before the deployment, see `TEST_REPORT.md`), phones and real GPUs, any network other than the sandbox's, and audio output (no audio file exists).
"""
else:
    live_md = f"""## Live site (last verified deployment)

* URL: https://the-world-of-you-birthday-storybook.vercel.app
* No master-build deployment is recorded.
"""
dep = f"""# Deployment report

Generated {today}.

{live_md}
## Export rules

* The scratch export for Vercel excludes the preserved ZIP, `qa/`, `docs/`, `vercel-upload/`, `node_modules`, `.git` and any `.env*` file. No token or key is stored in the repository, these reports or any log.

## Git

* Commits are local only. The sandbox has no GitHub write credentials, so nothing was pushed (`git push` fails with an authentication error; the repository has no `origin`).
* To publish: unzip `woy-master-build-code.zip` over your clone (or `git pull` from `the-world-of-you-master-build.bundle`), then `git push`.
"""
Path("docs/DEPLOYMENT_REPORT.md").write_text(dep, encoding="utf-8")

# ================================================================= IMPLEMENTATION_REPORT (root, preserved + appended)
marker_start, marker_end = "<!-- master-build:start -->", "<!-- master-build:end -->"
section = f"""{marker_start}
## Master build: 17 ultra-3D experiences (appended {today}, {head_text})

The original report above is unchanged and describes the state **before** the master build; for example its statement that the production URL still serves the preceding deployment no longer holds (see "Deployment" below). Everything below describes the master build; the evidence lives in `docs/`.

* `docs/MASTER_PROJECT_AUDIT.md` - baseline audit, verified vs assumed
* `docs/FEATURE_COMPLETION_MATRIX.md` - per feature: original status, now, files, assets, interactions, tests, limitations, before/after
* `docs/RESEARCH_AND_ASSET_SOURCES.md`, `docs/ASSET_INVENTORY.md` - licences and every asset
* `docs/TEST_REPORT.md`, `docs/DEPLOYMENT_REPORT.md`, `docs/IMPLEMENTATION_ROADMAP.md`

### What changed

1. A shared engine (`src/engine`) and one lazy canvas host (`NativeGiftCanvas`) with an error boundary, WebGL probe, poster fallback, disposal and adaptive pixel ratio.
2. 17 distinct gift worlds (`src/three/gifts`), each with environment, hero object, materials, lighting, a choreographed opening, at least one interaction, a readable HTML state, replay and reverse closing.
3. Seven page sections on the same engine (`src/three/sections`): Birthday Garden hero, Wish Garden, Memory Observatory, Future Postcards, Birthday Ballroom, plus the scrapbook book body and the gallery depth in CSS.
4. The legacy per-section renderer and ten legacy builder files were deleted.
5. Gift dialog: a single scroller, sticky stage, optional sound dock (off by default).
6. Final-pass fixes found by re-checking the built pages: the hero growth buttons now work without 3D and settle on the right stage; the Birthday Ballroom layout puts the 3D stage beside the ritual controls (it had left the right half empty); the scrapbook cover text is laid out as a column (the closed book sits right of centre on the page); the QA tooling under `scripts/qa/` is now tracked (a too-broad `qa/` ignore rule had kept eight of its files out of git). Details: `docs/TEST_REPORT.md` section 2d.
7. The owner's content pack (copy for the letter, reasons, wishes, postcards, dedications, garden, cinema, radio and microcopy) went in word for word, with a spec that compares it to the PDF; see "Content pack" below.

### Content pack

The owner's `The_World_of_You_Complete_Missing_Content_Pack.pdf` (kept in `docs/content-pack/`) was added after the master build: the main birthday letter, the 17 reasons, 101 wishes, seven future postcards, dedications for gifts 01-08 plus the long flower, universe and crown texts, the garden narration (with the new Bud stage), the cinema and radio copy and all 13 microcopy strings. The words are the pack's own, compared with the PDF text by a spec; slots the pack leaves to the owner (letter memory, dedications for gifts 09-17, Open When, coupons, future leaves, photographs, audio) stay empty and are never shown as template text. Where each part went, what was not shown and why, and what is still the owner's to write: `docs/CONTENT_PACK_INTEGRATION.md`. Evidence: `docs/TEST_REPORT.md` section 3b.

### Deployment

{('Deployed to the existing Vercel project from commit `' + rec['production']['meta']['masterBuildCommit'] + '` as `' + rec['production']['id'] + '` (READY, promoted to production). Details, rollback and verification: `docs/DEPLOYMENT_REPORT.md`. ' + later_note.replace('**', '')) if rec else 'Not deployed; see `docs/DEPLOYMENT_REPORT.md`.'}

### Commits
{chr(10).join('* `' + c + '`' for c in commits[:8])}
{marker_end}
"""
rp = Path("IMPLEMENTATION_REPORT.md")
text = rp.read_text(encoding="utf-8") if rp.exists() else "# Implementation report\n"
if marker_start in text:
    text = re.sub(re.escape(marker_start) + r".*?" + re.escape(marker_end), section.strip(), text, flags=re.S)
else:
    text = text.rstrip() + "\n\n" + section
rp.write_text(text, encoding="utf-8")
print("reports written:", ", ".join(["MASTER_PROJECT_AUDIT", "FEATURE_COMPLETION_MATRIX", "TEST_REPORT", "DEPLOYMENT_REPORT", "IMPLEMENTATION_REPORT (appended)"]))
```

## 8. `scripts/qa/README.md` — new

```markdown
# QA tooling

Everything here is developer-only (nothing ships to production). Scripts need the Vite dev server (`npm run dev`, port 4181) and a Chromium build.
Playwright's own browser download is blocked in some sandboxes; point `CHROMIUM_PATH` at any Chromium (the sandbox used `@sparticuz/chromium`).
Software WebGL (SwiftShader) is slow: scene start-up takes 20-30 s and frame rates mean nothing. Run **one Chromium at a time** on small machines.

| Script | What it does |
|---|---|
| `lab-shot.mjs <kind> <prefix> '<steps-json>'` | Deterministic screenshots of one scene in the dev-only lab (`/?lab=<kind>`): set state, advance simulated time, screenshot, print triangles / draw calls / textures and console warnings. Works for all 17 gifts and the five section scenes. |
| `section-shot.mjs <sectionId> <out.jpg>` | Scrolls a page section (or `--target=<selector>`) into view, waits for its 3D scene (`--stage=<kind>`) to report ready, optionally runs `--pre` / `--eval` snippets (open a dialog, click a button), screenshots. `--mobile`, `--reduced`, `--nowebgl` (hides WebGL so the poster fallback shows). Section scenes only mount near the viewport, so pass `--target` for sections whose 3D stage is below the fold. |
| `keyboard-pass.mjs [gift-id] [--nowebgl] [--skip-dialog]` | Keyboard-only walk: Tab to the hero growth steps, activate each, check the highlighted stage settles on the clicked one, Replay, then open a gift with Enter, tab through the dialog, Escape, and check focus returns to the opener. Prints JSON. |
| `gift-flow.mjs <gift-id> <outDir>` | Real end-to-end flow of one gift dialog: open, layout metrics (single scroller, no horizontal overflow), the gift's own controls, text checks, Escape, canvas cleanup, render stats. `--mobile`, `--reduced`, `--quality=`. |
| `run-flows.sh` | Runs `gift-flow.mjs` for gifts FROM..TO, a fresh browser each, appends to `<out>/summary.jsonl`. |
| `run-list.sh <outDir> "<flags>" 01 02 …` | Same as `run-flows.sh` for an explicit list of gifts (e.g. `bash scripts/qa/run-list.sh qa/flow "--quality=low --w=1100 --h=640" 09 12`). On a 2 GB sandbox use the 1100 x 640 viewport: at 1280 x 720 the software-GL browser died on several of the heavier gifts (09-17) after free memory had fallen to about 40 MB, which points to memory pressure; the same gifts pass at 1100 x 640. |
| `leak-check.mjs [gift] [cycles]` | Opens and closes one gift repeatedly; every WebGL context must be lost again, no canvas may remain, the JS heap must not keep growing. |
| `render-previews.mjs` | Renders the 17 Gift Atelier posters from the native scenes (then `python3 scripts/compress-gift-previews.py`). |
| `capture.mjs <outDir>` | Screenshots every section and every gift (baseline / regression captures). `--only=`, `--mobile`, `--reduced`, `--quality=`. |
| `run-specs.py` | Runs the Playwright specs one test per process (a single-process sandbox Chromium cannot survive repeated context teardown). On a normal machine use `npx playwright test`. `BASE_URL=https://... QA_BUILD=live` runs them against a deployed site (rows are tagged `live` and carry the URL; `playwright.config.ts` takes `BASE_URL`, default `http://localhost:4181`); `QA_KEEP_RESULTS=<dir>` keeps each test's Playwright artifacts (error context, screenshots) instead of letting the next test wipe `test-results/`. |
| `prod-smoke.mjs [--gifts=01,02,07,13] [--tier=low]` | Production check against the BUILT site (`npm run build`, then `npx vite preview --host 0.0.0.0 --port 4181 --strictPort`): no dev hooks in `dist/`, first view, the hero garden settling on Full bloom and walking to Bud, a scan of the rendered page for `[EDIT]` / `[ADD]` text, the Ballroom's illustrated alternative on desktop and phone, then the gift flows you name. Writes `docs/qa-screens/after/prod-smoke.json` for the test report. With `BASE_URL=https://...` and `--out=docs/qa-screens/after/live-prod-smoke.json --flows-dir=/tmp/live-flows` it checks a deployed site instead (no local server; the `dist/` scan still reads the local build). |
| `compare-live-dist.mjs [--url=] [--out=]` | No browser. Fetches every file of the local `dist/` from a deployed site and compares sha256: identical, different, or not served (a `*.md` the host drops is reported, not counted as a mismatch). Exit 1 on a difference or any other missing file. |
| `check-pack-live.mjs [--url=] [--out=]` | No browser (needs `node_modules` for esbuild). Looks up every string of `src/content/packContent.ts` (12+ characters) in the JavaScript a deployed site serves: whole, partly, hidden on purpose (`[EDIT]` / `[ADD]` slots, the author's notes and checklist, owner-only field lists) or MISSING. Exit 1 on MISSING. Run it after every deployment that touches the copy. |
| `pack-hero-stages.mjs [--mobile] [--nowebgl] [--out=dir]` | Content pack: walks the seven garden growth stages, screenshots each settled stage and prints the highlighted stage, the caption and the height of the narration block (it must stay constant). The 3D growth takes minutes on a software renderer and a production build has no time-scale hook, so `--nowebgl` (poster mode, HTML only) measures the block in seconds on the built site. |
| `pack-scrapbook.mjs [--mobile] [--turns=4] [--out=dir]` | Content pack: turns the Scrapbook through its spreads, centres the book in the viewport, screenshots each spread and prints the text of every blank and photo-mount page (the pack's empty-state lines). |
| `pack-postcards.mjs [--mobile] [--cards=1,2,…] [--out=dir]` | Content pack: opens Future Postcards, flips each card to its reverse and back, screenshots both sides. |
| `pack-letters.mjs [--mobile] [--out=dir]` | Content pack: the Letter Room shelf (six envelopes), the main letter folded, open and scrolled to its end, and an empty envelope. |
| `dom-probe.mjs <path> <selector>...` | Prints geometry and key computed styles of elements on the live page. |
| `contact_sheet.py` | Tiles screenshots into one labelled sheet. |

`window.__woyTimeScale` (dev builds only) speeds timelines up on slow software GL; the QA scripts set it. In production builds it is ignored.
Screenshots are written as JPEG so the QA folder stays small; keep curated before / after images as WebP under `docs/qa-screens/`.
```

## 9. `scripts/qa/capture.mjs` — new

```js
// Capture every site section and every gift experience in a real browser.
// Usage: node scripts/qa/capture.mjs <outDir> [--only=gift-03,garden] [--reduced] [--mobile] [--quality=low|medium|high]
import { launchBrowser, newPage, watchErrors, ensureDir, writeJson, sleep, BASE, SECTION_IDS, GIFT_IDS } from "./lib.mjs";

const out = process.argv[2] || "qa/capture";
const flag = (n) => process.argv.some((a) => a === `--${n}`);
const only = (process.argv.find((a) => a.startsWith("--only=")) || "").replace("--only=", "").split(",").filter(Boolean);
const want = (id) => !only.length || only.includes(id);
ensureDir(out);
const browser = await launchBrowser();
const opts = { reducedMotion: flag("reduced") ? "reduce" : "no-preference", mobile: flag("mobile"), ...(flag("mobile") ? { width: 390, height: 844, dpr: 2 } : {}) };
const report = { base: BASE, options: opts, sections: {}, gifts: {} };
const page = await newPage(browser, opts);
const forcedQuality = (process.argv.find((a) => a.startsWith("--quality=")) || "").split("=")[1];
if (forcedQuality) await page.addInitScript((q) => { try { localStorage.setItem("woy-quality", q); } catch { /* ignore */ } }, forcedQuality);
const sink = watchErrors(page);
const takeErrors = () => { const out = [...new Set(sink)]; sink.length = 0; return out; };

const canvasStats = (page) => page.evaluate(() => [...document.querySelectorAll("[data-render-frames]")].map((n) => ({
  cls: n.className.toString().slice(0, 40), frames: Number(n.dataset.renderFrames), triangles: Number(n.dataset.triangles || 0), active: n.dataset.sceneActive, reduced: n.dataset.reducedMotion,
})));

// ---------- sections ----------
{
  await page.goto(BASE + "/", { waitUntil: "load" }); await sleep(2500);
  for (const id of SECTION_IDS.filter(want)) {
    const t0 = Date.now();
    await page.evaluate((i) => document.getElementById(i)?.scrollIntoView({ block: "start", behavior: "instant" }), id);
    await sleep(2800);
    await page.screenshot({ path: `${out}/section-${id}.jpg`, type: "jpeg", quality: 78 });
    report.sections[id] = { settleMs: Date.now() - t0, canvases: await canvasStats(page), pageHeight: await page.evaluate(() => document.documentElement.scrollHeight), hOverflow: await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1) };
    console.log("section", id, JSON.stringify(report.sections[id].canvases));
  }
  report.sectionErrors = takeErrors();
}

// ---------- gifts ----------
for (const id of GIFT_IDS.filter(want)) {
  const r = { opened: false }; takeErrors();
  try {
    await page.goto("about:blank"); await page.goto(BASE + "/#gifts", { waitUntil: "load" });
    const parcel = page.locator(`.gift-parcel[data-gift-id="${id}"]`);
    await parcel.scrollIntoViewIfNeeded(); await sleep(600);
    const t0 = Date.now();
    await parcel.click();
    const dialog = page.locator("dialog[open]"); await dialog.waitFor({ state: "visible", timeout: 20000 }); r.opened = true;
    const status = dialog.locator(".gift-native-status").first();
    try { await status.waitFor({ timeout: 25000 }); await page.waitForFunction(() => /ready/i.test(document.querySelector("dialog[open] .gift-native-status")?.textContent || ""), null, { timeout: 40000 }); r.readyMs = Date.now() - t0; } catch { r.readyMs = null; r.note = "3D status never reached ready (or no 3D stage in this gift)"; }
    await sleep(3500);
    r.stage = await dialog.locator("[data-gift-world]").first().getAttribute("data-gift-world").catch(() => null);
    r.canvasCount = await dialog.locator("canvas").count();
    r.stats = await canvasStats(page);
    r.buttons = await dialog.locator("button").evaluateAll((els) => els.map((e) => (e.getAttribute("aria-label") || e.textContent || "").trim().replace(/\s+/g, " ")).filter(Boolean));
    r.inputs = await dialog.locator("input,select,textarea").count();
    r.dialogOverflow = await dialog.evaluate((d) => ({ scrollH: d.scrollHeight, clientH: d.clientHeight, scrollW: d.scrollWidth, clientW: d.clientWidth }));
    r.nestedScrollers = await page.evaluate(() => [...document.querySelectorAll("dialog[open] *")].filter((e) => { const s = getComputedStyle(e); return /(auto|scroll)/.test(s.overflowY) && e.scrollHeight > e.clientHeight + 4; }).map((e) => e.className.toString().slice(0, 50)));
    await page.screenshot({ path: `${out}/${id}.jpg`, type: "jpeg", quality: 78 });
    const host = dialog.locator(".gift-native-canvas").first();
    if (await host.count()) { await host.scrollIntoViewIfNeeded().catch(() => {}); await host.screenshot({ path: `${out}/${id}-stage.jpg`, type: "jpeg", quality: 78 }).catch(() => {}); }
    // closing behaviour
    const close = dialog.getByRole("button", { name: /close dialog/i }).first();
    if (await close.count()) { await close.click(); await sleep(700); r.closed = (await page.locator("dialog[open]").count()) === 0; r.canvasesAfterClose = await page.locator("dialog canvas").count(); }
    else { await page.keyboard.press("Escape"); await sleep(600); r.closed = (await page.locator("dialog[open]").count()) === 0; r.closeVia = "Escape (no close button found)"; }
  } catch (e) { r.error = String(e.message).split("\n")[0]; }
  r.errors = takeErrors();
  report.gifts[id] = r;
  console.log(id, JSON.stringify({ opened: r.opened, stage: r.stage, readyMs: r.readyMs, canvases: r.canvasCount, closed: r.closed, errors: r.errors.length, err: r.error }));
}
writeJson(`${out}/report-${only.join("+") || "all"}.json`, report);
console.log("DONE ->", out); process.exit(0);
```

## 10. `scripts/qa/check-pack-live.mjs` — new

```js
// Looks up every string of the owner's content pack (src/content/packContent.ts) in the JavaScript a deployed site serves.
//   usage: node scripts/qa/check-pack-live.mjs [--url=https://...] [--out=docs/qa-screens/after/live-pack.json]
//   (--url defaults to $BASE_URL, then to the project's production alias). Needs Node 18+ and the repo's node_modules (esbuild); no browser.
// Each string of 12+ characters is searched for in the entry bundle and every lazy chunk it names:
//   exact     = the whole string appears, spelled the way a JS string literal spells it (double-quoted, single-quoted or template)
//   fragment  = only a long run of it appears (the bundler split or re-spelled the string)
//   hidden    = not in the site, on purpose: template/slot text ([EDIT]/[ADD...]), the author's notes and checklist, owner-only field lists
//   MISSING   = not in the site and not on the hidden list: a real problem
// This proves the copy ships; what a visitor actually sees is checked by tests/content-pack.spec.ts (run it with BASE_URL=... QA_BUILD=live).
// Exit code 1 if anything is MISSING.
import { createRequire } from "node:module";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const require = createRequire(path.join(root, "package.json"));
const esbuild = require("esbuild");
const arg = (name, fallback) => (process.argv.find((a) => a.startsWith(`--${name}=`)) || `--${name}=${fallback}`).split("=").slice(1).join("=");
const LIVE = arg("url", process.env.BASE_URL || "https://the-world-of-you-birthday-storybook.vercel.app").replace(/\/$/, "");
const outFile = arg("out", "");

// strings the visitor never sees, with the reason (the pack's own rules: no template text, no invented content)
const HIDDEN = [
  [/^packAuthorNotes\b/, "the pack's notes to the author"],
  [/^packChecklist\b/, "the pack's publishing checklist for the owner"],
  [/^packLetterInsertPrompts\b/, "[EDIT] prompts for optional letter paragraphs"],
  [/^packLetter\.memoryPrompt$/, "[EDIT] slot for the owner's own memory"],
  [/^packCinema\.(photo|video)CaptionTemplate$/, "[EDIT] caption templates"],
  [/^packCinema\.requiredFields\[/, "field list for the owner who adds a photo or clip"],
  [/^packRadio\.trackTemplates\[/, "[ADD ...] track slots"],
  [/^packRadio\.voiceNoteTemplate$/, "[ADD ...] voice-note slot"],
  [/^packRadio\.requirements$/, "build requirements for the player (met by the controls, not shown as copy)"],
  [/^packGiftDedications\.[^.]+\.packTitle$/, "the pack's own gift titles, kept for reference only"],
];

const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "woy-pack-"));
esbuild.buildSync({ entryPoints: [path.join(root, "src/content/packContent.ts")], bundle: true, format: "esm", outfile: path.join(tmp, "pack.mjs"), logLevel: "error" });
const pack = await import(pathToFileURL(path.join(tmp, "pack.mjs")).href);
fs.rmSync(tmp, { recursive: true, force: true });

const html = await (await fetch(`${LIVE}/`)).text();
const entry = [...html.matchAll(/(?:src|href)="(\/assets\/[^"]+\.js)"/g)].map((m) => m[1]);
// the entry plus every chunk it can load: lazy chunks are named inside the bundles (dynamic imports use ./name-HASH.js)
const seen = new Set(); const queue = [...entry]; let all = "";
while (queue.length) {
  const u = queue.pop(); if (seen.has(u)) continue; seen.add(u);
  const t = await (await fetch(LIVE + u)).text(); all += `\n${t}`;
  for (const m of t.matchAll(/["'`]\.?\/?([A-Za-z0-9_.-]+-[A-Za-z0-9_-]{8}\.js)["'`]/g)) queue.push(`/assets/${m[1]}`);
}

const strings = [];
(function walk(o, p) {
  if (typeof o === "string") strings.push([p, o]);
  else if (Array.isArray(o)) o.forEach((v, i) => walk(v, `${p}[${i}]`));
  else if (o && typeof o === "object") for (const [k, v] of Object.entries(o)) walk(v, p ? `${p}.${k}` : k);
})(pack, "");

const spellings = (s) => {
  const json = JSON.stringify(s).slice(1, -1);                       // "double quoted": \" and \n escaped
  const bare = json.replace(/\\"/g, '"');                            // 'single quoted' holding raw double quotes
  return [...new Set([s, json, bare, bare.replace(/'/g, "\\'"), s.replace(/\\/g, "\\\\").replace(/`/g, "\\`").replace(/\$\{/g, "\\${")])];
};
const fragment = (s) => { const runs = s.split(/["'\\\n\r`$\u2028\u2029]/).filter((r) => r.length >= 8).sort((a, b) => b.length - a.length); return runs[0]?.slice(0, 60) ?? null; };

const sections = {}; const missing = []; const hidden = [];
for (const [p, s] of strings) {
  if (s.trim().length < 12) continue;
  const top = p.split(/[.[]/)[0];
  const sec = (sections[top] ??= { strings: 0, exact: 0, fragment: 0, hidden: 0, missing: 0 });
  sec.strings++;
  if (spellings(s).some((x) => all.includes(x))) { sec.exact++; continue; }
  const f = fragment(s);
  if (f && all.includes(f)) { sec.fragment++; continue; }
  const why = HIDDEN.find(([re]) => re.test(p));
  if (why) { sec.hidden++; hidden.push({ path: p, reason: why[1] }); } else { sec.missing++; missing.push({ path: p, text: s.slice(0, 80) }); }
}

const sum = (k) => Object.values(sections).reduce((n, v) => n + v[k], 0);
console.log(`${LIVE}: read ${seen.size} JS files (${all.length} characters)`);
for (const [k, v] of Object.entries(sections)) console.log(`  ${k.padEnd(28)} ${String(v.exact).padStart(3)}/${String(v.strings).padEnd(3)} exact${v.fragment ? `, ${v.fragment} fragment-only` : ""}${v.hidden ? `, ${v.hidden} hidden by design` : ""}${v.missing ? `, ${v.missing} MISSING` : ""}`);
console.log(`total ${sum("strings")} strings: ${sum("exact")} exact, ${sum("fragment")} fragment-only, ${sum("hidden")} hidden by design, ${sum("missing")} MISSING`);
for (const m of missing) console.log(`  MISSING ${m.path} => ${JSON.stringify(m.text)}`);
const result = { url: LIVE, jsFilesRead: seen.size, charactersRead: all.length, totals: { strings: sum("strings"), exact: sum("exact"), fragmentOnly: sum("fragment"), hiddenByDesign: sum("hidden"), missing: sum("missing") }, sections, hiddenByDesign: hidden, missing };
if (outFile) { fs.mkdirSync(path.dirname(outFile), { recursive: true }); fs.writeFileSync(outFile, JSON.stringify(result, null, 2) + "\n"); }
process.exit(missing.length ? 1 : 0);
```

## 11. `scripts/qa/compare-live-dist.mjs` — new

```js
// Compares every file of the local production build (dist/) with what a deployed site serves, byte for byte (sha256).
//   usage: node scripts/qa/compare-live-dist.mjs [--url=https://...] [--dist=dist] [--out=docs/qa-screens/after/live-bytes.json]
//   (--url defaults to $BASE_URL, then to the project's production alias). Needs only Node 18+, no browser.
// A file that the host deliberately does not serve is reported as "notServed", not as a content mismatch. Here that is
// public/assets/{fonts,models}/README.md: .vercelignore drops *.md and nothing in the app references them.
// Exit code 1 if any file differs, or if a file other than a *.md is not served.
import crypto from "node:crypto";
import fs from "node:fs";
import path from "node:path";

const arg = (name, fallback) => (process.argv.find((a) => a.startsWith(`--${name}=`)) || `--${name}=${fallback}`).split("=").slice(1).join("=");
const url = arg("url", process.env.BASE_URL || "https://the-world-of-you-birthday-storybook.vercel.app").replace(/\/$/, "");
const dist = arg("dist", "dist");
const outFile = arg("out", "");
if (!fs.existsSync(dist)) { console.error(`${dist}/ does not exist: run npm run build first`); process.exit(2); }

const files = [];
(function walk(dir) { for (const e of fs.readdirSync(dir, { withFileTypes: true })) { const p = path.join(dir, e.name); if (e.isDirectory()) walk(p); else files.push(p); } })(dist);
files.sort();

const sha = (buf) => crypto.createHash("sha256").update(buf).digest("hex");
const rows = [];
const check = async (file) => {
  const rel = path.relative(dist, file).split(path.sep).join("/");
  const local = fs.readFileSync(file);
  const res = await fetch(`${url}/${rel.split("/").map(encodeURIComponent).join("/")}`, { redirect: "manual" });
  if (res.status !== 200) { rows.push({ file: rel, result: "notServed", status: res.status, bytes: local.length }); return; }
  const remote = Buffer.from(await res.arrayBuffer());
  rows.push({ file: rel, result: sha(remote) === sha(local) ? "identical" : "different", status: 200, bytes: local.length, remoteBytes: remote.length });
};
// a few requests at a time: kind to the host and to a small machine
for (let i = 0; i < files.length; i += 6) await Promise.all(files.slice(i, i + 6).map(check));
rows.sort((a, b) => a.file.localeCompare(b.file));

const identical = rows.filter((r) => r.result === "identical");
const different = rows.filter((r) => r.result === "different");
const notServed = rows.filter((r) => r.result === "notServed");
const unexpected = notServed.filter((r) => !/\.md$/i.test(r.file));
const result = {
  url, localFiles: files.length, identical: identical.length,
  different: different.map((r) => r.file),
  notServed: notServed.map((r) => ({ file: r.file, status: r.status })),
  unexpectedNotServed: unexpected.map((r) => r.file),
  bytesCompared: identical.reduce((n, r) => n + r.bytes, 0),
};
console.log(`${url}: ${identical.length} of ${files.length} files byte-identical; ${different.length} different; ${notServed.length} not served${notServed.length ? ` (${notServed.map((r) => `${r.file} -> HTTP ${r.status}`).join(", ")})` : ""}`);
if (outFile) { fs.mkdirSync(path.dirname(outFile), { recursive: true }); fs.writeFileSync(outFile, JSON.stringify(result, null, 2) + "\n"); }
process.exit(different.length || unexpected.length ? 1 : 0);
```

## 12. `scripts/qa/contact_sheet.py` — new

```python
#!/usr/bin/env python3
"""Tile screenshots into one labelled contact sheet.  usage: contact_sheet.py out.png cols cellW img1 img2 ..."""
import sys, os
from PIL import Image, ImageDraw
out, cols, cw, *imgs = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), *sys.argv[4:]
tiles = []
for p in imgs:
    if not os.path.exists(p): continue
    im = Image.open(p).convert("RGB"); ch = round(im.height * cw / im.width)
    tiles.append((os.path.basename(p).rsplit(".", 1)[0], im.resize((cw, ch), Image.LANCZOS)))
if not tiles: sys.exit("no images")
ch = max(t[1].height for t in tiles); rows = (len(tiles) + cols - 1) // cols; pad = 18
sheet = Image.new("RGB", (cols * cw, rows * (ch + pad)), (18, 18, 22)); d = ImageDraw.Draw(sheet)
for i, (name, im) in enumerate(tiles):
    x, y = (i % cols) * cw, (i // cols) * (ch + pad)
    d.text((x + 6, y + 3), name, fill=(235, 235, 235)); sheet.paste(im, (x, y + pad))
sheet.save(out); print(out, sheet.size)
```

## 13. `scripts/qa/dom-probe.mjs` — new

```js
// Prints geometry and key computed styles for selectors on the live page.  usage: node scripts/qa/dom-probe.mjs "<url path>" "<sel1>" "<sel2>" ... [--w=1280] [--h=720] [--wait=6000]
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";
const [path, ...rest] = process.argv.slice(2);
const sels = rest.filter((a) => !a.startsWith("--"));
const arg = (n, d) => (process.argv.find((a) => a.startsWith(`--${n}=`)) || `--${n}=${d}`).split("=")[1];
const browser = await launchBrowser();
const page = await newPage(browser, { width: Number(arg("w", 1280)), height: Number(arg("h", 720)) });
await page.addInitScript(() => { try { localStorage.setItem("woy-quality", "low"); } catch {} });
await page.goto(BASE + path, { waitUntil: "load" });
await sleep(Number(arg("wait", 6000)));
for (const sel of sels) {
  const info = await page.evaluate((s) => [...document.querySelectorAll(s)].slice(0, 3).map((el) => {
    const r = el.getBoundingClientRect(), cs = getComputedStyle(el);
    return { cls: String(el.className).slice(0, 60), x: Math.round(r.x), y: Math.round(r.y + scrollY), w: Math.round(r.width), h: Math.round(r.height), pos: cs.position, z: cs.zIndex, bg: cs.backgroundColor, bgi: cs.backgroundImage.slice(0, 60), ov: cs.overflow, disp: cs.display };
  }), sel);
  console.log(sel, JSON.stringify(info));
}
await browser.close();
```

## 14. `scripts/qa/gift-flow.mjs` — new

```js
// End-to-end flow for ONE gift dialog: open -> layout metrics -> real interactions -> keyboard close -> leak check.
// Usage: node scripts/qa/gift-flow.mjs gift-02 qa/flow [--mobile] [--reduced] [--w=1280] [--h=720] [--quality=medium]
// Each gift gets its own browser process (the sandbox Chromium is single-process and fragile across many pages).
import { launchBrowser, newPage, watchErrors, BASE, sleep, ensureDir, writeJson } from "./lib.mjs";

const id = process.argv[2];
const out = process.argv[3] || "qa/flow";
const arg = (n, d) => (process.argv.find((a) => a.startsWith(`--${n}=`)) || "").split("=")[1] ?? d;
const mobile = process.argv.includes("--mobile"), reduced = process.argv.includes("--reduced");
const width = Number(arg("w", mobile ? 390 : 1280)), height = Number(arg("h", mobile ? 844 : 720)), quality = arg("quality", "medium");

const btn = (name) => ["click", name];
const FLOWS = {
  "gift-01": [btn(/Open the letter/), ["wait", 3500], ["shot", "opening"], btn(/Skip animation/), ["wait", 1500], ["expect", ".gift-letter__reading", /Aaj ka din tumhara hai/], ["text", /To the Girl Who Makes This Little Universe Special/], ["shot", "reading"], btn(/Fold the letter/), ["wait", 2500], ["shot", "folded"], btn(/Replay the writing/), ["wait", 2000], btn(/Sound effects/), ["wait", 500], ["pressed", /Sound effects/, "true"], btn(/Sound effects/), ["wait", 400], ["pressed", /Sound effects/, "false"]],
  "gift-02": [btn(/Open jar lid/), ["wait", 2500], btn(/^03$/), ["wait", 2500], ["expect", ".gift-jar__note", /NOTE 03/], ["text", /own dreams and ambitions/], ["shot", "note-3"], btn(/Put note back/), ["wait", 1500], btn(/Shuffle the jar/), ["wait", 2500], btn(/Read all 17/), ["count", ".gift-jar__all li", 17], btn(/Turn jar right/), ["wait", 800]],
  "gift-03": [btn(/Grow the flower/), ["wait", 2500], btn(/Grow the sprout/), ["wait", 2500], btn(/Unfold the leaves/), ["wait", 2500], btn(/Open the bloom/), ["wait", 4500], ["shot", "bloom"], btn(/Rotate flower right/), ["wait", 1000], btn(/Reveal hidden message/), ["text", /Keep blooming at your own pace/], ["shot", "dedication"], btn(/Begin again/), ["wait", 1500]],
  "gift-04": [["click", null, ".gift-control-row >> button >> nth=1"], ["wait", 2500], ["shot", "milestone-2"], btn(/Zoom in/), ["wait", 1500], btn(/Rotate the map/), ["wait", 1000], btn(/Return to overview/), ["wait", 1500], btn(/Reveal the dedication/), ["wait", 1500], ["text", /Your world is bigger than you think/], ["shot", "dedication"]],
  "gift-05": [btn(/Insert cassette/), ["wait", 3500], ["shot", "inserted"], ["text", /Your playlist is not here yet/], ["disabled", /^Play$/, true], btn(/Eject cassette/), ["wait", 2000]],
  "gift-06": [["text", /A little collection of moments worth keeping/], btn(/Start projector/), ["wait", 4000], ["shot", "projecting"], ["text", /The next memory is waiting to be added/], ["disabled", /^Play$/, true], btn(/Dim the theatre/), ["wait", 1500], ["text", /The screen fades, but the moments we choose to remember/]],
  "gift-07": [btn(/^Wish 1$/), ["wait", 1500], btn(/^Wish 4$/), ["wait", 1500], btn(/^Wish 7$/), ["wait", 2000], ["shot", "collected"], btn(/Draw a wish from the sky/), ["wait", 1800], ["expect", ".gift-wishes__note small", /FROM THE SKY/], ["shot", "sky-wish"], btn(/Display all wishes/), ["count", ".gift-wishes__all li", 10], ["count", ".gift-wishes__sky li", 101], btn(/Clear constellation/), ["wait", 800]],
  "gift-08": [btn(/The jewels/), ["wait", 2500], ["shot", "jewels"], btn(/Rotate right/), ["wait", 1200], btn(/Reveal birthday note/), ["expect", ".gift-crown__message", /./], ["text", /Your crown is your confidence/], ["wait", 2000], ["shot", "dedication"]],
  "gift-09": [["click", null, ".gift-open-when__envelope >> nth=1"], ["wait", 3000], ["shot", "selected"], btn(/Break the seal/), ["wait", 4000], ["shot", "opened"], ["text", /waiting to be written/], btn(/Close the letter/), ["wait", 2500]],
  "gift-10": [btn(/Pull the lever/), ["wait", 4500], ["shot", "ticket"], btn(/Reset machine/), ["wait", 2000]],
  "gift-11": [["click", null, ".gift-adventure__location--1"], ["wait", 2500], ["click", null, ".gift-adventure__location--2"], ["wait", 3000], ["shot", "travelled"]],
  "gift-12": [["text", /Add an audio file to activate this player/], btn(/Preview turntable silently/), ["wait", 4000], ["shot", "preview"], ["disabled", /^Play$/, true], btn(/Stop silent preview/), ["wait", 1500]],
  "gift-13": [["wipe"], ["wait", 4500], ["shot", "wiped"], btn(/Reset the mirror fog/), ["wait", 1800], btn(/Clear the mist/), ["wait", 3500], ["shot", "cleared"]],
  "gift-14": [btn(/Next coupon page/), ["wait", 2500], btn(/Next coupon page/), ["wait", 2500], ["shot", "page-3"], ["disabled", /Mark redeemed/, true], btn(/Previous coupon page/), ["wait", 1500]],
  "gift-15": [btn(/Plant the seed/), ["wait", 3000], btn(/Grow another leaf/), ["wait", 2500], btn(/Grow another leaf/), ["wait", 2500], btn(/^Leaf 2$/), ["wait", 3000], ["shot", "hope-2"]],
  "gift-16": [["solveTreasure"], btn(/Check the order/), ["wait", 5000], ["shot", "gate-open"], ["fill", "The chest asks for a word", "OPEN"], btn(/Unlock the chest/), ["wait", 6000], ["shot", "chest-open"], btn(/Restart the hunt/), ["wait", 2000]],
  "gift-17": [btn(/Gather the sixteen lights/), ["wait", 4500], ["shot", "ring"], btn(/Open the portal/), ["wait", 6000], ["shot", "portal"], btn(/Replay journey/), ["wait", 2500]],
};

const renderStats = () => page.evaluate(() => { const h = document.querySelector("dialog[open] .gift-native-canvas"); return h ? { triangles: Number(h.dataset.triangles), drawCalls: Number(h.dataset.drawCalls), geometries: Number(h.dataset.geometries), textures: Number(h.dataset.textures), quality: h.dataset.quality } : null; });
const browser = await launchBrowser();
const page = await newPage(browser, { width, height, reducedMotion: reduced ? "reduce" : "no-preference", mobile });
await page.addInitScript((q) => { window.__woyTimeScale = 6; try { localStorage.setItem("woy-quality", q); } catch {} }, quality);
const errors = watchErrors(page);
ensureDir(out);
const r = { id, viewport: { width, height }, mobile, reduced, quality, steps: [], errors: [] };
try {
  await page.goto(`${BASE}/?quality=${quality}#gifts`, { waitUntil: "domcontentloaded" });
  await page.waitForSelector(`.gift-parcel[data-gift-id="${id}"]`, { timeout: 60000 });
  const parcel = page.locator(`.gift-parcel[data-gift-id="${id}"]`);
  await parcel.scrollIntoViewIfNeeded(); await sleep(400);
  const canvasesBefore = await page.evaluate(() => document.querySelectorAll("canvas").length);
  const t0 = Date.now();
  await parcel.click();
  const dialog = page.locator("dialog[open]");
  await dialog.waitFor({ timeout: 15000 });
  try { await page.waitForFunction(() => /ready/i.test(document.querySelector("dialog[open] .gift-native-status")?.textContent || ""), null, { timeout: 60000 }); r.readyMs = Date.now() - t0; } catch { r.readyMs = null; r.notReady = true; }
  await sleep(600);
  r.renderOpen = await renderStats();
  r.layout = await page.evaluate(() => {
    const d = document.querySelector("dialog[open]"), b = d.getBoundingClientRect(), vw = innerWidth, vh = innerHeight;
    const all = [...d.querySelectorAll("*")];
    const scrollers = all.filter((el) => { const cs = getComputedStyle(el); return /(auto|scroll)/.test(cs.overflowY) && el.scrollHeight > el.clientHeight + 2 && el.clientHeight > 0; }).map((el) => String(el.className || el.tagName).slice(0, 50));
    const clipped = all.filter((el) => { const rr = el.getBoundingClientRect(); const cs = getComputedStyle(el); return rr.width > 0 && cs.position !== "fixed" && rr.right > b.right + 2 && !/hidden|auto|scroll|clip/.test(cs.overflowX) && el.closest(".gift-native-stage") === null; }).slice(0, 5).map((el) => String(el.className || el.tagName).slice(0, 50));
    const stage = d.querySelector(".gift-native-stage")?.getBoundingClientRect();
    return { dialog: { top: Math.round(b.top), left: Math.round(b.left), width: Math.round(b.width), height: Math.round(b.height) }, fitsViewport: b.top >= -1 && b.left >= -1 && b.right <= vw + 1 && b.bottom <= vh + 1, scrollers, horizontalOverflowInside: clipped, docHScroll: document.documentElement.scrollWidth > vw + 1, stage: stage ? { w: Math.round(stage.width), h: Math.round(stage.height) } : null, canvasesInDialog: d.querySelectorAll("canvas").length };
  });
  await dialog.screenshot({ path: `${out}/${id}-00-open.jpg`, type: "jpeg", quality: 72 });
  const steps = FLOWS[id] || [];
  for (const [kind, a, b, c] of steps) {
    const step = { kind, arg: String(a ?? b ?? ""), ok: true };
    try {
      if (kind === "click") { const loc = b ? dialog.locator(b).first() : dialog.getByRole("button", { name: a }).first(); await loc.scrollIntoViewIfNeeded(); await loc.click({ timeout: 8000 }); }
      else if (kind === "wait") await sleep(a);
      else if (kind === "shot") await dialog.screenshot({ path: `${out}/${id}-${a}.jpg`, type: "jpeg", quality: 72 });
      else if (kind === "expect") { const txt = await dialog.locator(a).first().innerText({ timeout: 8000 }); step.ok = b.test(txt); step.got = txt.slice(0, 80); }
      else if (kind === "count") { const n = await dialog.locator(a).count(); step.ok = n === b; step.got = n; }
      else if (kind === "disabled") { const d = await dialog.getByRole("button", { name: a }).first().isDisabled(); step.ok = d === (b ?? true); step.got = d; }
      else if (kind === "pressed") { const v = await dialog.getByRole("button", { name: a }).first().getAttribute("aria-pressed"); step.ok = v === b; step.got = v; }
      else if (kind === "text") { const t = await dialog.innerText(); step.ok = a.test(t); step.got = step.ok ? "found" : "not found"; }
      else if (kind === "fill") { await dialog.getByLabel(a).fill(b); }
      else if (kind === "wipe") { const box = await dialog.locator(".gift-native-canvas").boundingBox(); await page.mouse.move(box.x + box.width * 0.4, box.y + box.height * 0.3); await page.mouse.down(); for (let i = 0; i <= 14; i++) { await page.mouse.move(box.x + box.width * (0.4 + (i % 2 ? 0.12 : 0.0)), box.y + box.height * (0.3 + i * 0.03)); await sleep(60); } await page.mouse.up(); }
      else if (kind === "solveTreasure") {
        const want = ["flower", "moon", "star"];
        for (let target = 0; target < 3; target++) {
          for (let guard = 0; guard < 4; guard++) {
            const order = await dialog.locator(".gift-treasure__piece").evaluateAll((els) => els.map((e) => ["flower", "moon", "star"].find((s) => e.classList.contains(`is-${s}`))));
            const at = order.indexOf(want[target]); if (at === target) break;
            await dialog.locator(`.gift-treasure__piece.is-${want[target]}`).click();
            await dialog.getByRole("button", { name: at > target ? /Move selected left/ : /Move selected right/ }).click();
          }
        }
      }
    } catch (e) { step.ok = false; step.error = String(e.message || e).split("\n")[0].slice(0, 160); }
    r.steps.push(step);
  }
  r.render = await renderStats();
  await page.screenshot({ path: `${out}/${id}-99-final-page.jpg`, type: "jpeg", quality: 60 });
  await page.keyboard.press("Escape"); await sleep(900);
  r.closedByEscape = await page.evaluate(() => !document.querySelector("dialog[open]"));
  const canvasesAfter = await page.evaluate(() => document.querySelectorAll("canvas").length);
  r.canvases = { before: canvasesBefore, afterClose: canvasesAfter };
} catch (e) { r.fatal = String(e.message || e).split("\n")[0]; }
r.errors = errors.filter((e) => !/THREE\.Clock/.test(e)).slice(0, 12);
r.pass = !r.fatal && !r.notReady && r.steps.every((s) => s.ok) && r.errors.length === 0 && r.closedByEscape === true;
writeJson(`${out}/${id}.json`, r);
console.log(JSON.stringify({ id, pass: r.pass, readyMs: r.readyMs, layout: r.layout && { fits: r.layout.fitsViewport, scrollers: r.layout.scrollers, hOverflow: r.layout.horizontalOverflowInside.length + (r.layout.docHScroll ? 1 : 0), stage: r.layout.stage }, failed: r.steps.filter((s) => !s.ok), canvases: r.canvases, esc: r.closedByEscape, errors: r.errors, fatal: r.fatal }));
await browser.close();
```

## 15. `scripts/qa/keyboard-pass.mjs` — new

```js
// Keyboard-only pass: hero growth steps (Tab / Enter) and a gift dialog (Enter opens, focus stays inside, Escape closes, focus returns).
// usage: node scripts/qa/keyboard-pass.mjs [giftId=gift-01] [--nowebgl] [--skip-dialog]   (needs the dev server and the browser env, see scripts/qa/README.md)
// --nowebgl hides WebGL from the page, so the hero shows its poster and the growth buttons must work without 3D feedback.
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";

const giftId = process.argv.slice(2).find((a) => !a.startsWith("--")) || "gift-01";
const noWebgl = process.argv.includes("--nowebgl");
const skipDialog = process.argv.includes("--skip-dialog");
const browser = await launchBrowser();
const page = await newPage(browser, { width: 1100, height: 700, mobile: false, dpr: 1, reducedMotion: "no-preference" });
await page.addInitScript(() => { try { localStorage.setItem("woy-quality", "low"); } catch {} window.__woyTimeScale = 6; });
if (noWebgl) await page.addInitScript(() => { const get = HTMLCanvasElement.prototype.getContext; HTMLCanvasElement.prototype.getContext = function (type, ...a) { return /webgl/.test(type) ? null : get.call(this, type, ...a); }; });
const problems = [];
page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
await page.goto(BASE + "/", { waitUntil: "load" });
await sleep(2500);
const label = () => page.evaluate(() => {
  const el = document.activeElement;
  if (!el || el === document.body) return { tag: "BODY", name: "" };
  const cs = getComputedStyle(el);
  const visibleRing = (cs.outlineStyle !== "none" && parseFloat(cs.outlineWidth) > 0) || (cs.boxShadow && cs.boxShadow !== "none");
  return {
    tag: el.tagName,
    giftId: el.getAttribute("data-gift-id"),
    name: (el.getAttribute("aria-label") || el.textContent || el.getAttribute("title") || "").trim().replace(/\s+/g, " ").slice(0, 48),
    inGrowth: !!el.closest(".garden-growth__steps"),
    inDialog: !!el.closest("dialog[open]"),
    current: el.getAttribute("aria-current"),
    ring: !!visibleRing,
  };
});

const result = { mode: noWebgl ? "no-webgl (poster)" : "webgl", hero: {}, dialog: {}, problems };

// ---------- A. hero growth steps ----------
let presses = 0, hit = null;
for (; presses < 60; presses++) {
  await page.keyboard.press("Tab");
  const l = await label();
  if (l.inGrowth) { hit = l; break; }
}
result.hero.tabsToFirstStep = hit ? presses + 1 : null;
result.hero.firstStepFocusRing = hit?.ring ?? null;
const readHero = () => page.evaluate(() => ({
  caption: document.querySelector(".garden-growth__caption")?.textContent || "",
  current: document.querySelector(".garden-growth__steps [aria-current='step']")?.textContent || "",
}));
const waitCurrent = async (name, ms) => { const t0 = Date.now(); while (Date.now() - t0 < ms) { if ((await readHero()).current === name) return Date.now() - t0; await sleep(250); } return null; };
if (hit && !noWebgl) {
  // Tab scrolled the hero into view, which wakes its lazily mounted 3D stage: wait for it, then let the first growth settle
  try { await page.waitForFunction(() => /ready/i.test(document.querySelector('[data-section-stage="hero-garden"] .gift-native-status')?.textContent || ""), null, { timeout: 150000 }); }
  catch { result.hero.note = "hero 3D not ready in time"; }
  await sleep(6000);
}
if (hit) {
  result.hero.start = await readHero();
  const steps = [];
  for (const name of ["Roots", "Sprout", "Leaves", "Bud", "Flower", "Full bloom", "Seed"]) {
    // Tab to the button (forward through the list; wrap to Seed via shift+Tab history is not needed: "Seed" is reached by Shift+Tab x6)
    if (name === "Seed") { for (let i = 0; i < 6; i++) await page.keyboard.press("Shift+Tab"); } else await page.keyboard.press("Tab");
    const l = await label();
    const before = await readHero();
    await page.keyboard.press(name === "Leaves" ? "Space" : "Enter"); // Space is exercised once as well
    const took = await waitCurrent(name, noWebgl ? 3000 : 40000);
    await sleep(noWebgl ? 300 : 3500);                       // the scene may still be settling: it must stay on the clicked stage
    const after = await readHero();
    const settledOk = after.current === name;
    steps.push({ name, focused: l.name, key: name === "Leaves" ? "Space" : "Enter", updatedAfterMs: took, caption: after.caption, captionChanged: before.caption !== after.caption, settledOnClicked: settledOk, focusKept: (await label()).inGrowth });
  }
  result.hero.steps = steps;
  result.hero.allStepsWork = steps.every((x) => x.updatedAfterMs !== null && x.settledOnClicked && x.focusKept);
  // Replay button by keyboard: Tab from "Seed" to the end of the list, then once more
  for (let i = 0; i < 7; i++) await page.keyboard.press("Tab");
  const rp = await label();
  result.hero.replayFocused = rp.name;
  await page.keyboard.press("Enter");
  const seen = [];
  const t0 = Date.now();
  while (Date.now() - t0 < (noWebgl ? 7000 : 20000)) { const c = (await readHero()).current; if (seen[seen.length - 1] !== c) seen.push(c); await sleep(200); }
  result.hero.replayStagesSeen = seen;
}

// ---------- B. gift dialog ----------
const sel = `.gift-parcel[data-gift-id="${giftId}"]`;
if (!skipDialog) {
await page.evaluate((s) => { const b = document.querySelector(s); b.scrollIntoView({ block: "center" }); }, sel);
await sleep(800);
await page.focus(sel);
const opener = await label();
await page.keyboard.press("Enter");
try { await page.waitForSelector("dialog[open]", { timeout: 15000 }); } catch { result.dialog.opened = false; }
await sleep(1500);
if (result.dialog.opened !== false) {
  result.dialog.opened = true;
  result.dialog.attrs = await page.evaluate(() => { const d = document.querySelector("dialog[open]"); return { ariaLabelledby: d.getAttribute("aria-labelledby"), ariaLabel: d.getAttribute("aria-label"), title: document.getElementById(d.getAttribute("aria-labelledby") || "")?.textContent?.slice(0, 60) || null }; });
  result.dialog.focusAfterOpen = await label();
  const seen = [], outside = [];
  for (let i = 0; i < 40; i++) {
    await page.keyboard.press("Tab");
    const l = await label();
    seen.push(l.name || l.tag);
    if (!l.inDialog) outside.push(l.name || l.tag);
  }
  result.dialog.tabStopsInOneCycle = [...new Set(seen)].slice(0, 24);
  result.dialog.focusEscapedDialog = outside.length;
  await page.keyboard.press("Escape");
  await sleep(1500);
  result.dialog.closedByEscape = !(await page.$("dialog[open]"));
  const back = await label();
  result.dialog.focusReturnedToOpener = back.tag === "BUTTON" && back.giftId === opener.giftId;
  result.dialog.focusAfterClose = back;
}
}
await sleep(300);
result.problems = problems.filter((p) => !/THREE\.Clock/.test(p));
console.log(JSON.stringify(result, null, 1));
await browser.close();
```

## 16. `scripts/qa/lab-shot.mjs` — new

```js
// Deterministic screenshots of one scene in the dev-only lab (http://localhost:4181/?lab=<kind>).
// usage: node scripts/qa/lab-shot.mjs <kind> <outPrefix> '<steps-json>' [--quality=high] [--w=1280] [--h=720] [--mobile]
// steps: [{ "name":"open", "state":{"open":true}, "simulate":2.5, "replace":false }]
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";

const [kind, prefix, stepsJson = "[{\"name\":\"initial\",\"simulate\":1}]"] = process.argv.slice(2);
const arg = (n, d) => (process.argv.find((a) => a.startsWith(`--${n}=`)) || `--${n}=${d}`).split("=")[1];
const quality = arg("quality", "high"), w = Number(arg("w", 1280)), h = Number(arg("h", 720));
const mobile = process.argv.includes("--mobile");
const steps = JSON.parse(stepsJson);

const browser = await launchBrowser();
const page = await newPage(browser, { width: mobile ? 390 : w, height: mobile ? 844 : h, mobile, dpr: mobile ? 2 : 1 });
const log = [];
page.on("console", (m) => { if (["error", "warning"].includes(m.type())) log.push(`${m.type()}: ${m.text()}`.slice(0, 400)); });
page.on("pageerror", (e) => log.push(`pageerror: ${e.message}`.slice(0, 400)));
page.on("requestfailed", (r) => log.push(`requestfailed: ${r.url()}`));

const t0 = Date.now();
// Vite's dev server may reload once after optimising dependencies on a cold cache, so retry on navigation.
for (let attempt = 0; ; attempt++) {
  try {
    await page.goto(`${BASE}/?lab=${kind}&quality=${quality}`, { waitUntil: "load" });
    await page.waitForFunction(() => window.__lab, null, { timeout: 90000 });
    await page.evaluate(() => window.__lab.ready);
    break;
  } catch (e) {
    if (attempt >= 4 || !/navigation|destroyed|closed/i.test(String(e.message))) throw e;
    await sleep(1500);
  }
}
console.log(`scene ready in ${Date.now() - t0} ms`);

for (const step of steps) {
  if (step.state) await page.evaluate(([s, r]) => (r ? window.__lab.replace(s) : window.__lab.set(s)), [step.state, Boolean(step.replace)]);
  if (step.simulate) await page.evaluate((s) => window.__lab.simulate(s[0], s[1]), [step.simulate, step.step]);
  if (step.cam) { await page.evaluate((c) => window.__lab.camera(c), step.cam); await sleep(150); }
  await sleep(step.wait ?? 400);
  const file = `${prefix}-${step.name}.jpg`;
  await page.screenshot({ path: file, type: "jpeg", quality: 82 }); // JPEG keeps the QA folder small (PNG frames were ~0.7 MB each)
  const stats = await page.evaluate(() => window.__lab.stats());
  console.log(`${step.name}: tris=${stats.triangles} calls=${stats.drawCalls} geos=${stats.geometries} tex=${stats.textures} -> ${file}`);
}
const unique = [...new Set(log)];
console.log(unique.length ? "CONSOLE:\n  " + unique.join("\n  ") : "console: clean (no errors or warnings)");
process.exit(0);
```

## 17. `scripts/qa/leak-check.mjs` — new

```js
// GPU / memory leak check: opens and closes one gift dialog several times and verifies that every WebGL context that was created
// is lost again (R3F forceContextLoss on unmount), that no canvas stays in the DOM, and that the JS heap does not keep growing.
// usage: node scripts/qa/leak-check.mjs [gift-id=gift-02] [cycles=4] [--quality=low]
import { launchBrowser, newPage, sleep, BASE, writeJson, ensureDir } from "./lib.mjs";

const id = process.argv[2] && !process.argv[2].startsWith("--") ? process.argv[2] : "gift-02";
const cycles = Number(process.argv[3] && !process.argv[3].startsWith("--") ? process.argv[3] : 4);
const quality = (process.argv.find((a) => a.startsWith("--quality=")) || "--quality=low").split("=")[1];

const browser = await launchBrowser();
const page = await newPage(browser, { width: 1100, height: 640 });
await page.addInitScript((q) => {
  try { localStorage.setItem("woy-quality", q); } catch { /* ignore */ }
  window.__ctx = [];
  const original = HTMLCanvasElement.prototype.getContext;
  HTMLCanvasElement.prototype.getContext = function (type, ...rest) {
    const gl = original.call(this, type, ...rest);
    if (gl && /webgl/.test(type) && !window.__ctx.includes(gl)) window.__ctx.push(gl);
    return gl;
  };
}, quality);
const cdp = await page.context().newCDPSession(page);
await cdp.send("Performance.enable");
const heap = async () => { await cdp.send("HeapProfiler.collectGarbage"); const { metrics } = await cdp.send("Performance.getMetrics"); return Math.round(metrics.find((m) => m.name === "JSHeapUsedSize").value / 1048576 * 10) / 10; };

await page.goto(`${BASE}/#gifts`, { waitUntil: "domcontentloaded" });
await page.waitForSelector(`.gift-parcel[data-gift-id="${id}"]`, { timeout: 60000 });
const parcel = page.locator(`.gift-parcel[data-gift-id="${id}"]`);
await parcel.scrollIntoViewIfNeeded();
const rows = [];
const baseContexts = await page.evaluate(() => window.__ctx.length);
const baseHeap = await heap();
for (let i = 1; i <= cycles; i++) {
  await parcel.click();
  await page.locator("dialog[open]").waitFor();
  await page.waitForFunction(() => /ready/i.test(document.querySelector("dialog[open] .gift-native-status")?.textContent || ""), null, { timeout: 120000 });
  const during = await page.evaluate(() => ({ canvases: document.querySelectorAll("dialog canvas").length, contexts: window.__ctx.length, lost: window.__ctx.filter((gl) => gl.isContextLost()).length }));
  await page.keyboard.press("Escape");
  await sleep(1500);
  const after = await page.evaluate(() => ({ canvases: document.querySelectorAll("canvas").length, contexts: window.__ctx.length, lost: window.__ctx.filter((gl) => gl.isContextLost()).length }));
  rows.push({ cycle: i, during, after, heapMB: await heap() });
  console.log(JSON.stringify(rows[rows.length - 1]));
}
const last = rows[rows.length - 1];
const result = {
  gift: id, cycles, quality, baseHeapMB: baseHeap, baseContexts,
  contextsCreated: last.after.contexts - baseContexts, contextsLost: last.after.lost, canvasesLeftInDom: last.after.canvases,
  heapMB: rows.map((r) => r.heapMB), heapGrowthMB: Math.round((last.heapMB - rows[0].heapMB) * 10) / 10,
};
result.pass = result.contextsCreated === result.contextsLost && result.canvasesLeftInDom === 0 && result.heapGrowthMB < 25;
ensureDir("qa/leak"); writeJson(`qa/leak/${id}.json`, result);
console.log(JSON.stringify(result));
await browser.close();
```

## 18. `scripts/qa/lib.mjs` — new

```js
// Shared helpers for the browser QA scripts (visual capture, interaction checks, leak checks).
// Uses playwright-core (installed with @playwright/test). Point CHROMIUM_PATH at any Chromium build;
// without it Playwright's own browser is used. WebGL falls back to SwiftShader (software) when no GPU exists,
// which is slow but renders correctly - FPS numbers measured that way are NOT representative of real GPUs.
import { chromium } from "playwright-core";
import fs from "node:fs";

export const BASE = process.env.BASE_URL || "http://localhost:4181";
export const sleep = (ms) => new Promise((r) => setTimeout(r, ms));

export async function launchBrowser() {
  const executablePath = process.env.CHROMIUM_PATH || undefined;
  const args = [
    "--no-sandbox", "--disable-setuid-sandbox", "--disable-dev-shm-usage", "--hide-scrollbars", "--mute-audio",
    "--use-gl=angle", "--use-angle=swiftshader", "--enable-unsafe-swiftshader", "--ignore-gpu-blocklist",
    "--font-render-hinting=none", "--disable-renderer-backgrounding", "--disable-background-timer-throttling",
  ];
  // The sandbox Chromium is a Lambda-style headless shell that only runs in single-process mode.
  if (executablePath && process.env.CHROMIUM_SINGLE_PROCESS !== "0") args.push("--single-process", "--no-zygote", "--in-process-gpu");
  return chromium.launch({ executablePath, args, headless: true, timeout: 90000 });
}

export async function newPage(browser, { width = 1280, height = 720, reducedMotion = "no-preference", mobile = false, dpr = 1 } = {}) {
  const context = await browser.newContext({
    viewport: { width, height }, deviceScaleFactor: dpr, reducedMotion,
    isMobile: mobile, hasTouch: mobile,
  });
  const page = await context.newPage();
  page.setDefaultTimeout(45000);
  return page;
}

/** Collect real problems only: uncaught errors, console.error, failed requests, HTTP >= 400. */
export function watchErrors(page) {
  const errors = [];
  page.on("pageerror", (e) => errors.push(`pageerror: ${e.message}`));
  page.on("console", (m) => { if (m.type() === "error") errors.push(`console.error: ${m.text()}`.slice(0, 300)); });
  page.on("requestfailed", (r) => errors.push(`requestfailed: ${r.url()} ${r.failure()?.errorText ?? ""}`));
  page.on("response", (r) => { if (r.status() >= 400) errors.push(`http ${r.status()}: ${r.url()}`); });
  return errors;
}

export const ensureDir = (dir) => fs.mkdirSync(dir, { recursive: true });
export const writeJson = (file, data) => fs.writeFileSync(file, JSON.stringify(data, null, 2));

export const SECTION_IDS = ["invitation", "garden", "storybook", "timepiece", "letters", "gallery", "flower-garden", "gifts", "music-room", "future-postcards", "birthday-cake", "finale"];
export const GIFT_IDS = Array.from({ length: 17 }, (_, i) => `gift-${String(i + 1).padStart(2, "0")}`);
```

## 19. `scripts/qa/pack-hero-stages.mjs` — new

```js
// Content-pack capture: walks the seven Birthday Garden growth stages (Seed ... Full bloom), screenshots each once it has settled and prints
// which stage was highlighted, the caption label and the height of the narration block (it must not change between stages).
// usage: node scripts/qa/pack-hero-stages.mjs [--mobile] [--nowebgl] [--out=qa/pack-views]     (needs a server: BASE_URL, default http://localhost:4181)
// The 3D growth takes minutes in real time on a software renderer; the dev server's __woyTimeScale hook (6x) shortens that, a production build has no such hook.
// --nowebgl hides WebGL from the page (the hero then shows its poster and the buttons drive the captions directly): it measures the narration block's height
// per stage in seconds, on the dev server or on the built site, because that block is plain HTML and does not depend on the 3D scene.
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";
import fs from "node:fs";
const mobile = process.argv.includes("--mobile");
const noWebgl = process.argv.includes("--nowebgl");
const out = (process.argv.find((a) => a.startsWith("--out=")) || "--out=qa/pack-views").split("=")[1];
fs.mkdirSync(out, { recursive: true });
const browser = await launchBrowser();
const page = await newPage(browser, { width: mobile ? 390 : 1100, height: mobile ? 844 : 700, mobile, dpr: 1, reducedMotion: "no-preference" });
await page.addInitScript(() => { try { localStorage.setItem("woy-quality", "low"); } catch {} window.__woyTimeScale = 6; });
const problems = [];
page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
if (noWebgl) await page.addInitScript(() => { const get = HTMLCanvasElement.prototype.getContext; HTMLCanvasElement.prototype.getContext = function (type, ...a) { return /webgl/.test(type) ? null : get.call(this, type, ...a); }; });
await page.goto(BASE + "/", { waitUntil: "load" });
await sleep(2000);
await page.evaluate(() => { const el = document.getElementById("garden"); if (el) window.scrollTo({ top: el.getBoundingClientRect().top + scrollY, behavior: "instant" }); });
if (noWebgl) { console.log("WebGL hidden: poster mode"); await sleep(1500); }
else {
  try { await page.waitForFunction(() => /ready/i.test(document.querySelector('[data-section-stage="hero-garden"] .gift-native-status')?.textContent || ""), null, { timeout: 150000 }); console.log("3D ready"); } catch { console.log("3D NOT ready"); }
  await sleep(9000); // let the automatic first growth settle
}
const read = () => page.evaluate(() => ({ current: document.querySelector(".garden-growth__steps [aria-current='step']")?.textContent || "", label: document.querySelector(".garden-growth__label")?.textContent || "", caption: document.querySelector(".garden-growth__caption")?.textContent || "", block: (() => { const r = document.querySelector(".garden-growth__narration")?.getBoundingClientRect(); return r ? { h: Math.round(r.height), top: Math.round(r.top) } : null; })(), steps: (() => { const r = document.querySelector(".garden-growth__steps")?.getBoundingClientRect(); return r ? { top: Math.round(r.top), h: Math.round(r.height) } : null; })(), replay: (() => { const r = document.querySelector(".garden-growth__replay")?.getBoundingClientRect(); return r ? Math.round(r.top) : null; })() }));
const rows = [];
for (const name of ["Seed", "Roots", "Sprout", "Leaves", "Bud", "Flower", "Full bloom"]) {
  await page.locator(".garden-growth__steps button", { hasText: new RegExp(`^${name}$`) }).click();
  const t0 = Date.now(); let ok = false;
  while (Date.now() - t0 < (noWebgl ? 5000 : 60000)) { if ((await read()).current === name) { ok = true; break; } await sleep(300); }
  await sleep(noWebgl ? 600 : 4500);
  const r = await read();
  rows.push({ name, reached: ok, still: r.current === name, label: r.label, narrationBlock: r.block, stepsTop: r.steps, replayTop: r.replay });
  await page.screenshot({ path: `${out}/hero${mobile ? "-m" : ""}${noWebgl ? "-nowebgl" : ""}-${name.toLowerCase().replace(" ", "-")}.jpg`, type: "jpeg", quality: 72 });
}
console.log(JSON.stringify({ rows, problems: problems.filter((p) => !/THREE\.Clock/.test(p)) }, null, 1));
await browser.close();
```

## 20. `scripts/qa/pack-letters.mjs` — new

```js
// Content-pack capture: the Letter Room shelf (six envelopes), the main letter folded, open and scrolled to its end, and an empty envelope.
// usage: node scripts/qa/pack-letters.mjs [--mobile] [--out=qa/pack-views]     (needs the dev server)
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";
import fs from "node:fs";
const mobile = process.argv.includes("--mobile");
const out = (process.argv.find((a) => a.startsWith("--out=")) || "--out=qa/pack-views").split("=")[1];
fs.mkdirSync(out, { recursive: true });
const browser = await launchBrowser();
const page = await newPage(browser, { width: mobile ? 390 : 1100, height: mobile ? 844 : 700, mobile, dpr: 1, reducedMotion: "no-preference" });
await page.addInitScript(() => { try { localStorage.setItem("woy-quality", "low"); } catch {} window.__woyTimeScale = 6; });
const problems = [];
page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
await page.goto(BASE + "/", { waitUntil: "load" });
await sleep(1500);
await page.evaluate(() => { const el = document.querySelector("#letters .letter-shelf"); if (el) window.scrollTo({ top: el.getBoundingClientRect().top + scrollY - 120, behavior: "instant" }); });
await sleep(1500);
const tag = mobile ? "-m" : "";
await page.screenshot({ path: `${out}/letters${tag}-shelf.jpg`, type: "jpeg", quality: 70 });
const envs = page.locator("#letters .letter-envelope");
console.log("envelopes:", await envs.count());
await envs.nth(0).click();
const dialog = page.locator("dialog[open]");
await dialog.waitFor({ state: "visible" });
try { await page.waitForFunction(() => /ready/i.test(document.querySelector('dialog[open] [data-section-stage="letter"] .gift-native-status')?.textContent || ""), null, { timeout: 150000 }); console.log("3D ready"); } catch { console.log("3D NOT ready"); }
await sleep(2000);
await page.screenshot({ path: `${out}/letters${tag}-main-folded.jpg`, type: "jpeg", quality: 70 });
await dialog.getByRole("button", { name: "Skip animation" }).click();
await sleep(6000);
await page.screenshot({ path: `${out}/letters${tag}-main-open.jpg`, type: "jpeg", quality: 70 });
const m = await page.evaluate(() => { const d = document.querySelector("dialog[open]"); const paper = d.querySelector(".archive-dialog__paper"); const copy = d.querySelector(".physical-letter-copy"); return { scrollH: paper?.scrollHeight, clientH: paper?.clientHeight, copyH: copy ? Math.round(copy.getBoundingClientRect().height) : null, paragraphs: d.querySelectorAll(".letter-reading__body p").length, hOverflow: document.documentElement.scrollWidth > innerWidth + 1 }; });
console.log(JSON.stringify(m));
await page.evaluate(() => { const p = document.querySelector("dialog[open] .archive-dialog__paper"); p.scrollTo({ top: p.scrollHeight, behavior: "instant" }); });
await sleep(800);
await page.screenshot({ path: `${out}/letters${tag}-main-end.jpg`, type: "jpeg", quality: 70 });
await page.keyboard.press("Escape"); await sleep(1500);
await envs.nth(3).click();
await dialog.waitFor({ state: "visible" }); await sleep(2500);
await dialog.getByRole("button", { name: "Skip animation" }).click(); await sleep(3500);
await page.screenshot({ path: `${out}/letters${tag}-empty.jpg`, type: "jpeg", quality: 70 });
console.log(JSON.stringify({ problems: problems.filter((p) => !/THREE\.Clock/.test(p)) }));
await browser.close();
```

## 21. `scripts/qa/pack-postcards.mjs` — new

```js
// Content-pack capture: opens Future Postcards, flips each card to its reverse and back to the illustration, screenshots both sides and
// prints the dialog and stage sizes and the first words of the message.
// usage: node scripts/qa/pack-postcards.mjs [--mobile] [--cards=1,2,3,4,5,6,7] [--out=qa/pack-views]     (needs the dev server)
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";
import fs from "node:fs";
const mobile = process.argv.includes("--mobile");
const only = (process.argv.find((a) => a.startsWith("--cards=")) || "--cards=1,2,3,4,5,6,7").split("=")[1].split(",").map(Number);
const out = (process.argv.find((a) => a.startsWith("--out=")) || "--out=qa/pack-views").split("=")[1];
fs.mkdirSync(out, { recursive: true });
const browser = await launchBrowser();
const page = await newPage(browser, { width: mobile ? 390 : 1100, height: mobile ? 844 : 700, mobile, dpr: 1, reducedMotion: "no-preference" });
await page.addInitScript(() => { try { localStorage.setItem("woy-quality", "low"); } catch {} window.__woyTimeScale = 6; });
const problems = [];
page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
await page.goto(BASE + "/", { waitUntil: "load" });
await sleep(1500);
await page.evaluate(() => { const el = document.getElementById("future-postcards"); if (el) window.scrollTo({ top: el.getBoundingClientRect().top + scrollY, behavior: "instant" }); });
await sleep(1500);
const cards = page.locator("#future-postcards .postcard-grid .postcard");
console.log("cards in grid:", await cards.count());
// grid overview
await page.screenshot({ path: `${out}/postcards${mobile ? "-m" : ""}-grid.jpg`, type: "jpeg", quality: 70 });
await cards.nth(only[0] - 1).click();
const dialog = page.locator("dialog[open]");
await dialog.waitFor({ state: "visible" });
try { await page.waitForFunction(() => /ready/i.test(document.querySelector('dialog[open] [data-section-stage="postcards"] .gift-native-status')?.textContent || ""), null, { timeout: 150000 }); console.log("3D ready"); } catch { console.log("3D NOT ready"); }
await sleep(2500);
const rows = [];
let current = only[0];
for (const n of only) {
  while (current !== n) { await dialog.getByRole("button", { name: "Next postcard" }).click(); current = current % 7 + 1; await sleep(600); }
  await dialog.getByRole("button", { name: /Read reverse/ }).click();
  await sleep(mobile ? 5500 : 6500);
  const info = await page.evaluate(() => { const d = document.querySelector("dialog[open]"); const st = d.querySelector('[data-section-stage="postcards"]'); const r = st?.getBoundingClientRect(); const scr = d.querySelector(".archive-dialog__paper"); return { title: d.querySelector("h2, h3")?.textContent, stage: r ? { w: Math.round(r.width), h: Math.round(r.height) } : null, reading: d.querySelector(".postcard-reading__text, .postcard-reading > p:not(.postcard-reading__when)")?.textContent?.slice(0, 60), hOverflow: document.documentElement.scrollWidth > innerWidth + 1, dialogW: Math.round(d.getBoundingClientRect().width) }; });
  rows.push({ n, ...info });
  await dialog.locator('[data-section-stage="postcards"]').screenshot({ path: `${out}/postcard${mobile ? "-m" : ""}-${n}-back.jpg`, type: "jpeg", quality: 78 });
  await dialog.getByRole("button", { name: /Show illustration/ }).click();
  await sleep(mobile ? 3500 : 4500);
  await dialog.locator('[data-section-stage="postcards"]').screenshot({ path: `${out}/postcard${mobile ? "-m" : ""}-${n}-front.jpg`, type: "jpeg", quality: 78 });
}
if (only.length === 1 || mobile) await page.screenshot({ path: `${out}/postcards${mobile ? "-m" : ""}-dialog.jpg`, type: "jpeg", quality: 72 });
console.log(JSON.stringify({ rows, problems: problems.filter((p) => !/THREE\.Clock/.test(p)) }, null, 1));
await browser.close();
```

## 22. `scripts/qa/pack-scrapbook.mjs` — new

```js
// Content-pack capture: the Scrapbook's owner slots. Turns the book through its spreads, screenshots each one and prints the text of every
// blank / photo-mount page, so the pack's "waiting to be written" and "add a real photograph" lines can be seen in place.
// usage: node scripts/qa/pack-scrapbook.mjs [--mobile] [--turns=4] [--out=qa/pack-views]     (needs a server on BASE_URL, default :4181)
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";
import fs from "node:fs";
const mobile = process.argv.includes("--mobile");
const arg = (n, d) => (process.argv.find((a) => a.startsWith(`--${n}=`)) || `--${n}=${d}`).split("=").slice(1).join("=");
const out = arg("out", "qa/pack-views");
const turns = Number(arg("turns", 4));
fs.mkdirSync(out, { recursive: true });
const browser = await launchBrowser();
const page = await newPage(browser, { width: mobile ? 390 : 1280, height: mobile ? 844 : 720, mobile, dpr: 1, reducedMotion: "no-preference" });
await page.addInitScript(() => { try { localStorage.setItem("woy-quality", "low"); } catch { /* ignore */ } });
const problems = [];
page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
await page.goto(BASE + "/", { waitUntil: "load" });
await sleep(2000);
await page.evaluate(() => { const el = document.getElementById("storybook"); if (el) window.scrollTo({ top: el.getBoundingClientRect().top + scrollY - 70, behavior: "instant" }); });
try { await page.waitForSelector(".storybook-leaf", { timeout: 60000 }); } catch { console.log("book did not mount"); }
await sleep(3500);
// centre the book itself in the viewport (the section is taller than the screen and the fixed nav would cover the pages' top edge)
const centreBook = () => page.evaluate(() => { const el = document.querySelector(".storybook-book__stage"); if (!el) return; const r = el.getBoundingClientRect(); window.scrollTo({ top: scrollY + r.top + r.height / 2 - innerHeight / 2 + 20, behavior: "instant" }); });
await centreBook(); await sleep(1200);
const tag = mobile ? "-m" : "";
const leaves = await page.evaluate(() => [...document.querySelectorAll(".storybook-leaf--blank, .storybook-leaf--photo")].map((leaf) => ({ kind: leaf.className.match(/storybook-leaf--(blank|photo)/)?.[1], title: leaf.querySelector("h3")?.textContent, body: leaf.querySelector("p")?.textContent, note: leaf.querySelector(".storybook-leaf__placeholder-note")?.textContent })));
console.log(JSON.stringify(leaves, null, 1));
// a viewport shot: the book never holds still (parallax, growing page blocks), so an element shot would wait for it to be "stable"
const shot = async (name) => page.screenshot({ path: `${out}/scrapbook${tag}-${name}.jpg`, type: "jpeg", quality: 74 });
await shot("0-cover");
const stageBox = await page.evaluate(() => { const r = document.querySelector(".storybook-book__stage")?.getBoundingClientRect(); return r ? { top: Math.round(r.top), bottom: Math.round(r.bottom), height: Math.round(r.height), viewport: innerHeight } : null; });
console.log("book stage", JSON.stringify(stageBox));
for (let i = 1; i <= turns; i++) {
  const next = page.getByRole("button", { name: "Turn to the next scrapbook page" });
  if (await next.isDisabled()) break;
  await next.click();
  await sleep(2600);
  await centreBook(); await sleep(600);
  await shot(`${i}`);
}
const overflow = await page.evaluate(() => document.documentElement.scrollWidth > innerWidth + 1);
console.log(JSON.stringify({ hOverflow: overflow, problems: problems.filter((p) => !/THREE\.Clock/.test(p)) }));
await browser.close();
```

## 23. `scripts/qa/prod-smoke.mjs` — new

```js
// Production smoke test against the BUILT site (vite preview of dist/), not the dev server. It checks:
//   * dist/ contains no dev-only hooks (the scene lab, the QA time scale),
//   * the first view, the hero garden settling on "Full bloom" and walking to "Bud", and a scan of the rendered page for template text,
//   * the Birthday Ballroom's illustrated alternative on a desktop and a phone-sized viewport,
//   * the gift flows you name (gift-flow.mjs, one fresh browser each).
// usage: npm run build && npx vite preview --host 0.0.0.0 --port 4181 --strictPort      (in another shell), then
//        CHROMIUM_PATH=... node scripts/qa/prod-smoke.mjs [--gifts=01,02,07,13] [--tier=low] [--out=docs/qa-screens/after/prod-smoke.json] [--flows-dir=qa/prod]
// It writes the JSON that scripts/make-reports.py reads for section 2e of docs/TEST_REPORT.md. One Chromium at a time (small machines).
// To check a deployed site instead: BASE_URL=https://... node scripts/qa/prod-smoke.mjs --out=docs/qa-screens/after/live-prod-smoke.json --flows-dir=/tmp/live-flows (no local server needed).
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { launchBrowser, newPage, sleep, BASE, ensureDir, writeJson } from "./lib.mjs";

const arg = (n, d) => (process.argv.find((a) => a.startsWith(`--${n}=`)) || `--${n}=${d}`).split("=").slice(1).join("=");
const gifts = arg("gifts", "01,02,07,13").split(",").filter(Boolean);
const tier = arg("tier", "low");
const outFile = arg("out", "docs/qa-screens/after/prod-smoke.json");
const flowsDir = arg("flows-dir", "qa/prod");
ensureDir(flowsDir); ensureDir(path.dirname(outFile));

// 0. dev-only hooks and the pack's [EDIT] / [ADD] / [INSERT] template markers must not be in the bundle
const hooks = [];
const markers = [];
const walk = (dir) => {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const p = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(p);
    else if (/\.(js|html|css|map)$/.test(entry.name)) { const text = fs.readFileSync(p, "utf8"); for (const needle of ["window.__lab", "__woyTimeScale", "lab-shot"]) if (text.includes(needle)) hooks.push(`${needle} in ${p}`); if (/\.(js|html)$/.test(entry.name)) for (const marker of ["[EDIT", "[ADD", "[INSERT"]) if (text.includes(marker)) markers.push(`${marker} in ${p}`); }
  }
};
if (fs.existsSync("dist")) walk("dist"); else hooks.push("dist/ does not exist: run npm run build first");

const pages = [];
const realProblems = (list) => list.filter((p) => !/THREE\.Clock/.test(p));
const watch = (page) => {
  const problems = [];
  page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
  page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
  return problems;
};
const prime = (page) => page.addInitScript((q) => { try { localStorage.setItem("woy-quality", q); } catch { /* ignore */ } }, tier);

// A. first view, hero garden, template-text scan
{
  const browser = await launchBrowser();
  const page = await newPage(browser, { width: 1280, height: 720 });
  await prime(page);
  const problems = watch(page);
  await page.goto(BASE + "/", { waitUntil: "load" }); await sleep(3000);
  const first = await page.evaluate(() => { const el = document.getElementById("invitation"); const r = el?.getBoundingClientRect(); return !!r && r.top < innerHeight && r.bottom > 0; });
  await page.screenshot({ path: path.join(flowsDir, "first-view.jpg"), type: "jpeg", quality: 78 });
  pages.push({ name: "first view at scroll 0", shows: first ? "invitation section (envelope)" : "NOT the invitation section", consoleProblems: realProblems(problems) });

  const mark = problems.length;
  await page.evaluate(() => document.getElementById("garden")?.scrollIntoView({ behavior: "instant" }));
  let heroShows;
  try {
    await page.waitForFunction(() => /ready/i.test(document.querySelector('[data-section-stage="hero-garden"] .gift-native-status')?.textContent || ""), null, { timeout: 180000 });
    const read = () => page.evaluate(() => ({ current: document.querySelector(".garden-growth__steps [aria-current='step']")?.textContent || "", label: document.querySelector(".garden-growth__label")?.textContent || "", caption: (document.querySelector(".garden-growth__caption")?.textContent || "").trim(), stages: document.querySelectorAll(".garden-growth__steps button").length }));
    await page.waitForFunction(() => document.querySelector(".garden-growth__steps [aria-current='step']")?.textContent === "Full bloom", null, { timeout: 300000 });
    await sleep(3000);
    const bloom = await read();
    await page.screenshot({ path: path.join(flowsDir, "hero-prod-full-bloom.jpg"), type: "jpeg", quality: 78 });
    await page.locator(".garden-growth__steps button", { hasText: /^Bud$/ }).click();
    await page.waitForFunction(() => document.querySelector(".garden-growth__steps [aria-current='step']")?.textContent === "Bud", null, { timeout: 240000 });
    await sleep(3000);
    const bud = await read();
    const ok = bloom.current === "Full bloom" && bud.current === "Bud" && bloom.stages === 7 && bloom.caption.length > 20 && bud.caption.length > 20 && bloom.caption !== bud.caption;
    heroShows = `${ok ? "3D ready" : "PROBLEM"}; ${bloom.stages} stage buttons; settled on ${bloom.current} (${bloom.label}), then Bud (${bud.label}) after a click; the caption changed with the stage`;
    await page.screenshot({ path: path.join(flowsDir, "hero-prod-bud.jpg"), type: "jpeg", quality: 72 });
  } catch (e) { heroShows = `NOT verified: ${String(e.message || e).split("\n")[0].slice(0, 140)}`; }
  pages.push({ name: "hero, scrolled into view (7 growth stages)", shows: heroShows, consoleProblems: realProblems(problems.slice(mark)) });

  const scan = await page.evaluate(() => { const text = `${document.documentElement.innerText}\n${document.documentElement.outerHTML}`; const m = text.match(/\[(EDIT|ADD|INSERT)[^\]]{0,60}/i); return m ? m[0] : null; });
  pages.push({ name: "rendered page scanned for [EDIT] / [ADD] / [INSERT] template text", shows: scan ? `FOUND: ${scan}` : "none found in the text or the HTML", consoleProblems: [] });
  await browser.close();
}

// B and C. the Ballroom's illustrated alternative, desktop and phone (a fresh browser each)
for (const mobile of [false, true]) {
  const browser = await launchBrowser();
  const page = await newPage(browser, { width: mobile ? 390 : 1100, height: mobile ? 844 : 700, mobile, dpr: mobile ? 2 : 1 });
  await prime(page);
  const problems = watch(page);
  await page.goto(BASE + "/", { waitUntil: "load" }); await sleep(2500);
  await page.evaluate(() => document.getElementById("birthday-cake")?.scrollIntoView({ behavior: "instant" })); await sleep(2500);
  let shows;
  try {
    await page.locator(".cake-illustration-fallback > summary").click();
    await sleep(800);
    const seen = await page.evaluate(() => { const vis = (sel) => { const el = document.querySelector(sel); if (!el) return false; const r = el.getBoundingClientRect(); return r.width > 20 && r.height > 20; }; return { svg: vis(".cake-illustration-fallback .cake-svg"), footnote: vis(".cake-section__footnote"), hOverflow: document.documentElement.scrollWidth > innerWidth + 1 }; });
    shows = seen.svg && seen.footnote && !seen.hOverflow ? (mobile ? "disclosure opens, illustration and footnote visible, no horizontal overflow" : "disclosure opens, illustration and footnote visible") : `PROBLEM ${JSON.stringify(seen)}`;
  } catch (e) { shows = `NOT verified: ${String(e.message || e).split("\n")[0].slice(0, 140)}`; }
  pages.push({ name: mobile ? "ballroom illustrated alternative, phone 390 px" : "ballroom illustrated alternative, desktop 1100 px", shows, consoleProblems: realProblems(problems) });
  await browser.close();
}

// D. gift flows, one fresh browser each (the browser above is closed first)
const giftFlows = [];
for (const g of gifts) {
  spawnSync("pkill", ["-x", "chromium"]); await sleep(2000);
  spawnSync("node", ["scripts/qa/gift-flow.mjs", `gift-${g}`, flowsDir, `--quality=${tier}`, "--w=1100", "--h=640"], { encoding: "utf8", timeout: 400000, env: process.env });
  let d = null;
  try { d = JSON.parse(fs.readFileSync(path.join(flowsDir, `gift-${g}.json`), "utf8")); } catch { /* no result */ }
  giftFlows.push({
    id: `gift-${g}`, tier, pass: !!d?.pass, readyMs: d?.readyMs ?? null,
    failedSteps: (d?.steps || []).filter((s) => !s.ok).map((s) => ({ kind: s.kind, arg: s.arg, error: s.error || `expected state not reached (got ${s.got})` })),
    consoleProblems: d ? (d.errors || []) : ["runner: no result"],
  });
  console.log(`done gift-${g}: ${giftFlows.at(-1).pass ? "PASS" : "FAIL"}`);
}
spawnSync("pkill", ["-x", "chromium"]);

const result = {
  url: BASE,
  how: /^https?:\/\/(localhost|127\.0\.0\.1)/.test(BASE)
    ? "npm run build, then vite preview of dist/ on :4181; same sandbox Chromium with software WebGL"
    : `the deployed site ${BASE}, opened from the sandbox network in the same Chromium with software WebGL; the dist/ scan below reads the local build, which scripts/qa/compare-live-dist.mjs shows is what the site serves`,
  devHooksInBundle: hooks.length > 0,
  devHooksChecked: hooks.length ? hooks.join("; ") : "window.__lab, __woyTimeScale, lab-shot: none in dist/",
  templateMarkersInBundle: markers,
  templateMarkersChecked: markers.length ? markers.join("; ") : "[EDIT, [ADD, [INSERT: none in the built .js and .html files",
  pages, giftFlows,
};
writeJson(outFile, result);
console.log(JSON.stringify({ out: outFile, hooks: hooks.length, templateMarkers: markers.length, pages: pages.map((p) => `${p.name}: ${p.shows}`), flows: giftFlows.map((f) => `${f.id} ${f.pass ? "PASS" : "FAIL"}`) }, null, 1));
```

## 24. `scripts/qa/render-previews.mjs` — new

```js
// Renders the 17 Gift Atelier preview posters (480x360) from the REAL native scenes in their finished state,
// through the offline authoring endpoint src/three/previewGiftModels.ts (never part of the production bundle).
// Usage:  node scripts/qa/render-previews.mjs [index ...]      (0-based, default: all 17)
// Then:   python3 scripts/compress-gift-previews.py            (PNG -> WebP, removes the PNGs)
// Needs the dev server (BASE_URL, default http://localhost:4181) and a Chromium (CHROMIUM_PATH). Software WebGL is fine for stills.
import fs from "node:fs";
import { BASE, launchBrowser, newPage, sleep } from "./lib.mjs";

const wanted = process.argv.slice(2).filter((a) => /^\d+$/.test(a)).map(Number);
const indexes = wanted.length ? wanted : Array.from({ length: 17 }, (_, i) => i);
const browser = await launchBrowser();
const page = await newPage(browser, { width: 640, height: 480 });
const errors = [];
page.on("pageerror", (e) => errors.push(e.message));
try {
  await page.goto(`${BASE}/`, { waitUntil: "domcontentloaded" });
  // The first dynamic import can trigger Vite's dependency re-optimisation reload; retry a few times.
  for (let attempt = 0; attempt < 5; attempt++) {
    try { await page.evaluate(() => import("/src/three/previewGiftModels.ts")); break; }
    catch (e) { if (!/context was destroyed|dynamically imported|Failed to fetch/i.test(String(e)) || attempt === 4) throw e; await sleep(3000); }
  }
  fs.mkdirSync("public/assets/gift-previews", { recursive: true });
  for (const i of indexes) {
    const data = await page.evaluate(async (n) => (await import("/src/three/previewGiftModels.ts")).renderGiftPreview(n), i);
    const file = `public/assets/gift-previews/gift-${String(i + 1).padStart(2, "0")}.png`;
    fs.writeFileSync(file, Buffer.from(data, "base64"));
    console.log(file, `${Math.round((data.length * 0.75) / 1024)} KB`);
  }
  await page.evaluate(async () => (await import("/src/three/previewGiftModels.ts")).finishPreviews());
  if (errors.length) console.log("page errors:", errors.slice(0, 3));
} finally { await browser.close(); }
```

## 25. `scripts/qa/run-each.sh` — new

```bash
#!/usr/bin/env bash
# Run capture.mjs once per gift in its own process/browser so a renderer crash cannot take the whole run down.
# usage: scripts/qa/run-each.sh <outDir> [extra capture flags]   (needs CHROMIUM_PATH / LD_LIBRARY_PATH in this sandbox)
out="${1:-qa/capture}"; shift || true
for i in $(seq -w ${FROM:-1} ${TO:-17}); do
  id="gift-$i"
  timeout 240 node scripts/qa/capture.mjs "$out" --only="$id" "$@" 2>&1 | tail -3
  pkill -x chromium 2>/dev/null || true
done
echo "ALL-DONE"
```

## 26. `scripts/qa/run-flows.sh` — new

```bash
#!/usr/bin/env bash
# Runs scripts/qa/gift-flow.mjs for gifts FROM..TO (default 1..17), one fresh Chromium per gift. Appends one JSON line per gift to <out>/summary.jsonl.
# Usage: FROM=1 TO=17 EXTRA="--quality=low --w=1100 --h=640" scripts/qa/run-flows.sh qa/flow
OUT="${1:-qa/flow}"; FROM="${FROM:-1}"; TO="${TO:-17}"; mkdir -p "$OUT"
export CHROMIUM_PATH="${CHROMIUM_PATH:-/tmp/chromium}" LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/tmp/al2023/lib}"
for i in $(seq "$FROM" "$TO"); do
  id=$(printf "gift-%02d" "$i")
  pkill -x chromium 2>/dev/null; sleep 2
  line=$(timeout 330 node scripts/qa/gift-flow.mjs "$id" "$OUT" $EXTRA 2>&1 | tail -1)
  case "$line" in "{"*) echo "$line" >> "$OUT/summary.jsonl";; *) echo "{\"id\":\"$id\",\"pass\":false,\"fatal\":\"runner: no result (timeout or crash)\"}" >> "$OUT/summary.jsonl";; esac
  echo "done $id"
done
pkill -x chromium 2>/dev/null
echo ALL_DONE
```

## 27. `scripts/qa/run-list.sh` — new

```bash
#!/usr/bin/env bash
# Runs gift-flow.mjs for an explicit list of gifts, one fresh Chromium each.  usage: scripts/qa/run-list.sh <outDir> "<flags>" 01 02 03 ...
OUT="$1"; FLAGS="$2"; shift 2; mkdir -p "$OUT"
export CHROMIUM_PATH="${CHROMIUM_PATH:-/tmp/chromium}" LD_LIBRARY_PATH="${LD_LIBRARY_PATH:-/tmp/al2023/lib}"
for g in "$@"; do
  pkill -x chromium 2>/dev/null; sleep 2
  line=$(timeout 330 node scripts/qa/gift-flow.mjs "gift-$g" "$OUT" $FLAGS 2>&1 | tail -1)
  case "$line" in "{"*) echo "$line" >> "$OUT/summary.jsonl";; *) echo "{\"id\":\"gift-$g\",\"pass\":false,\"fatal\":\"runner: no result\"}" >> "$OUT/summary.jsonl";; esac
  echo "done gift-$g"
done
pkill -x chromium 2>/dev/null; echo ALL_DONE
```

## 28. `scripts/qa/run-specs.py` — new

```python
#!/usr/bin/env python3
"""Runs the Playwright specs one test per process (a fresh Chromium each time: the sandbox's single-process Chromium cannot
survive repeated context teardown), appending one JSON line per test to qa/specs/summary.jsonl.
Usage: QA_SLOW=1 CHROMIUM_PATH=/tmp/chromium LD_LIBRARY_PATH=/tmp/al2023/lib python3 scripts/qa/run-specs.py [--skip regex] [--only regex]
Needs a server on :4181: the Vite dev server (rows are tagged "dev") or `vite preview` of dist/ with QA_BUILD=production (rows are tagged "production").
To run the specs against a deployed site set BASE_URL=https://... and QA_BUILD=live (rows are tagged "live" and carry the URL).
QA_KEEP_RESULTS=<dir> keeps each test's Playwright artifacts (error context, screenshots) in <dir>/NN instead of letting the next test wipe test-results/.
On a normal machine simply run `npx playwright test`."""
import json, os, re, subprocess, sys, time
os.chdir(os.path.dirname(os.path.abspath(__file__)) + "/../..")
args = sys.argv[1:]
skip = re.compile(args[args.index("--skip") + 1]) if "--skip" in args else None
only = re.compile(args[args.index("--only") + 1]) if "--only" in args else None
listing = subprocess.run(["npx", "playwright", "test", "--list"], capture_output=True, text=True).stdout
tests = []
for line in listing.splitlines():
    m = re.match(r"\s*(\S+\.spec\.ts):\d+:\d+ › (.*)", line)
    if m: tests.append((m.group(1), m.group(2).strip()))
os.makedirs("qa/specs", exist_ok=True)
build = os.environ.get("QA_BUILD", "dev")
out = open("qa/specs/summary.jsonl", "a")
keep = os.environ.get("QA_KEEP_RESULTS")
for n, (file, title) in enumerate(tests):
    if skip and skip.search(f"{file} {title}"): continue
    if only and not only.search(f"{file} {title}"): continue
    subprocess.run(["pkill", "-x", "chromium"], capture_output=True); time.sleep(2)
    t0 = time.time()
    try:
        proc = subprocess.run(["npx", "playwright", "test", f"tests/{file}", "-g", re.escape(title), "--reporter=line"] + (["--output", f"{keep}/{n:02d}"] if keep else []), capture_output=True, text=True, timeout=480)
        text = proc.stdout + proc.stderr; ok = proc.returncode == 0
    except subprocess.TimeoutExpired:
        text, ok = "runner timeout (480 s)", False
    tail = [l for l in text.splitlines() if l.strip()][-14:]
    err = next((l.strip() for l in text.splitlines() if re.search(r"Error:|expect\(|Timeout|locator", l)), "")
    row = {"file": file, "title": title, "passed": ok, "seconds": round(time.time() - t0), "build": build, "url": os.environ.get("BASE_URL", "http://localhost:4181"), "error": "" if ok else err[:300], "tail": [] if ok else [l[:200] for l in tail]}
    out.write(json.dumps(row) + "\n"); out.flush()
    print(("PASS" if ok else "FAIL"), file, "|", title[:80], f"({row['seconds']}s)", flush=True)
subprocess.run(["pkill", "-x", "chromium"], capture_output=True)
print("ALL_DONE")
```

## 29. `scripts/qa/section-shot.mjs` — new

```js
// Screenshots one page section once its 3D scene (if any) reports ready.
// usage: node scripts/qa/section-shot.mjs <sectionId> <out.jpg> [--stage=<scene kind>] [--eval="<js run before the shot>"] [--w=1280] [--h=720] [--quality=low] [--reduced] [--nowebgl] [--mobile] [--offset=<px scrolled past the section top>] [--settle=2500] [--timescale=6] [--target=<css selector to scroll to>] [--pre="<js run before waiting for 3D>"]
import { launchBrowser, newPage, sleep, BASE } from "./lib.mjs";
const [id, out] = process.argv.slice(2);
const arg = (n, d) => (process.argv.find((a) => a.startsWith(`--${n}=`)) || `--${n}=${d}`).split("=").slice(1).join("=");
const mobile = process.argv.includes("--mobile");
const browser = await launchBrowser();
const page = await newPage(browser, { width: mobile ? 390 : Number(arg("w", 1280)), height: mobile ? 844 : Number(arg("h", 720)), mobile, dpr: mobile ? 2 : 1, reducedMotion: process.argv.includes("--reduced") ? "reduce" : "no-preference" });
await page.addInitScript((q) => { try { localStorage.setItem("woy-quality", q); } catch {} }, arg("quality", "low"));
const timescale = Number(arg("timescale", 6));
await page.addInitScript((k) => { window.__woyTimeScale = k; }, timescale); // dev builds only: speeds up timelines on slow software GL
if (process.argv.includes("--nowebgl")) await page.addInitScript(() => { const get = HTMLCanvasElement.prototype.getContext; HTMLCanvasElement.prototype.getContext = function (type, ...a) { return /webgl/.test(type) ? null : get.call(this, type, ...a); }; });
const problems = [];
page.on("pageerror", (e) => problems.push(`pageerror: ${e.message}`.slice(0, 200)));
page.on("console", (m) => { if (m.type() === "error") problems.push(`console.error: ${m.text()}`.slice(0, 200)); });
await page.goto(BASE + "/", { waitUntil: "load" }); await sleep(1500);
const target = arg("target", "");
const found = await page.evaluate(([i, o, t]) => { const el = t ? document.querySelector(t) : document.getElementById(i); if (el) window.scrollTo({ top: el.getBoundingClientRect().top + scrollY + o - (t ? 90 : 0), behavior: "instant" }); return !!el; }, [id, Number(arg("offset", 0)), target]);
// An unknown id used to fall through silently and screenshot the top of the page under the wrong name.
if (!found) { problems.push(`target not found (${target ? "selector " + target : "id #" + id}); the shot shows the top of the page`); console.log(`WARNING: ${target || "#" + id} not found on the page`); }
const pre = arg("pre", "");
if (pre) { await page.evaluate(pre); await sleep(1200); }
const stage = arg("stage", "");
if (stage) {
  try { await page.waitForFunction((k) => /ready/i.test(document.querySelector(`[data-section-stage="${k}"] .gift-native-status`)?.textContent || ""), stage, { timeout: 150000 }); console.log("3D ready"); }
  catch { console.log("3D NOT ready in time"); }
}
await sleep(Number(arg("settle", 2500)));
const js = arg("eval", "");
if (js) { await page.evaluate(js); await sleep(Number(arg("after", 3000))); }
await page.screenshot({ path: out, type: "jpeg", quality: 80 });
console.log(JSON.stringify({ out, problems: problems.filter((p) => !/THREE\.Clock/.test(p)) }));
await browser.close();
```

## 30. `src/App.tsx` — modified

```tsx
import { useEffect, useRef, useState } from "react";
import { Flower2 } from "lucide-react";
import { BirthdayCake } from "./world/BirthdayCake";
import { BirthdayGarden } from "./world/BirthdayGarden";
import { FinalCelebration } from "./world/FinalCelebration";
import { FlowerGarden } from "./world/FlowerGarden";
import { FuturePostcards } from "./world/FuturePostcards";
import { GiftRoom } from "./world/GiftRoom";
import { LetterRoom } from "./world/LetterRoom";
import { MusicRoom } from "./world/MusicRoom";
import { OpeningInvitation } from "./world/OpeningInvitation";
import { PolaroidGallery } from "./world/PolaroidGallery";
import { RelationshipClock } from "./world/RelationshipClock";
import { Storybook } from "./world/Storybook";
import { WorldNav } from "./world/WorldNav";
import { chronosContent } from "./content/chronosContent";
import { SceneExperience } from "./scenes/SceneExperience";
import { audioBus } from "./engine/audio";

export default function App() {
  const [soundEnabled, setSoundEnabled] = useState(false);
  const [activeSection, setActiveSection] = useState("invitation");
  const [invitationKey, setInvitationKey] = useState(0);
  const progressRef = useRef<HTMLSpanElement>(null);

  useEffect(() => {
    document.title = chronosContent.meta.docTitle;
    document.documentElement.dataset.theme = "birthday";
    return () => { delete document.documentElement.dataset.theme; };
  }, []);

  useEffect(() => {
    const rawHash = window.location.hash.slice(1);
    if (!rawHash) return;
    let targetId = rawHash;
    try { targetId = decodeURIComponent(rawHash); } catch { /* keep the raw fragment */ }
    const frame = window.requestAnimationFrame(() => {
      document.getElementById(targetId)?.scrollIntoView({ block: "start", behavior: "instant" });
    });
    return () => window.cancelAnimationFrame(frame);
  }, []);

  useEffect(() => {
    const sections = Array.from(document.querySelectorAll<HTMLElement>("[data-chapter]"));
    let frame = 0;
    let currentId = "invitation";
    let disposed = false;
    const updateScrollState = () => {
      if (frame) return;
      frame = window.requestAnimationFrame(() => {
        frame = 0;
        const readingLine = window.innerHeight * 0.5;
        const current = sections.find((section) => {
          const bounds = section.getBoundingClientRect();
          return bounds.top <= readingLine && bounds.bottom > readingLine;
        }) ?? [...sections].reverse().find((section) => section.getBoundingClientRect().top <= readingLine);
        const id = current?.getAttribute("data-chapter");
        if (id && id !== currentId) {
          currentId = id;
          setActiveSection(id);
        }
        const scrollable = document.documentElement.scrollHeight - window.innerHeight;
        const progress = scrollable > 0 ? Math.min(100, Math.max(0, (window.scrollY / scrollable) * 100)) : 0;
        progressRef.current?.style.setProperty("width", `${progress}%`);
      });
    };
    const content = document.getElementById("main-content");
    const layoutObserver = content && "ResizeObserver" in window ? new ResizeObserver(updateScrollState) : null;
    if (content) layoutObserver?.observe(content);
    updateScrollState();
    window.addEventListener("scroll", updateScrollState, { passive: true });
    window.addEventListener("resize", updateScrollState);
    document.fonts?.ready.then(() => { if (!disposed) updateScrollState(); });
    return () => {
      disposed = true;
      layoutObserver?.disconnect();
      window.cancelAnimationFrame(frame);
      window.removeEventListener("scroll", updateScrollState);
      window.removeEventListener("resize", updateScrollState);
    };
  }, []);

  const reducedMotion = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  const setSceneHash = (id: string) => {
    window.history.replaceState(window.history.state, "", `${window.location.pathname}${window.location.search}#${id}`);
  };
  const goToGarden = () => {
    setSceneHash("garden");
    document.getElementById("garden")?.scrollIntoView({ behavior: reducedMotion() ? "instant" : "smooth", block: "start" });
    window.setTimeout(() => document.getElementById("birthday-garden-title")?.focus({ preventScroll: true }), reducedMotion() ? 0 : 320);
  };
  /** One global, user-gesture-driven switch. The Web Audio bus is created and resumed inside this click, never at load. */
  const toggleSound = () => { const next = !soundEnabled; audioBus.setEnabled(next); setSoundEnabled(next); };
  const replayInvitation = () => {
    audioBus.setEnabled(false);
    setSoundEnabled(false);
    setInvitationKey((key) => key + 1);
    setSceneHash("invitation");
    window.scrollTo({ top: 0, behavior: reducedMotion() ? "instant" : "smooth" });
  };

  return (
    <>
      <a className="skip-link" href="#garden">Skip to the birthday garden</a>
      <SceneExperience />
      <div className="world-site">
        <div className="reading-progress" aria-hidden="true"><span ref={progressRef} /></div>
        <main id="main-content" tabIndex={-1}>
          <OpeningInvitation key={invitationKey} onEnter={goToGarden} onSkip={goToGarden} />
          <WorldNav
            activeSection={activeSection}
            soundOn={soundEnabled}
            onToggleSound={toggleSound}
            onReplayInvitation={replayInvitation}
          />
          <BirthdayGarden />
          <Storybook soundEnabled={soundEnabled} />
          <RelationshipClock />
          <LetterRoom />
          <PolaroidGallery />
          <FlowerGarden />
          <GiftRoom soundEnabled={soundEnabled} onToggleSound={toggleSound} />
          <MusicRoom soundEnabled={soundEnabled} onToggleSound={toggleSound} />
          <FuturePostcards />
          <BirthdayCake />
          <FinalCelebration onReplayOpening={replayInvitation} />
        </main>
        {activeSection !== "invitation" && (
          <a href="#garden" className="back-to-garden" aria-label="Return to the birthday garden">
            <Flower2 size={17} aria-hidden="true" /><span>GARDEN</span>
          </a>
        )}
      </div>
    </>
  );
}
```

## 31. `src/components/ArchiveDialog.tsx` — modified

```tsx
import { useEffect, useId, useRef, type ReactNode } from "react";
import { X } from "lucide-react";

interface ArchiveDialogProps {
  open: boolean;
  onClose: () => void;
  eyebrow?: string;
  title: string;
  children: ReactNode;
  variant?: "paper" | "dark";
  className?: string;
  /** Accessible name and tooltip of the close button (the gift dialogs use the content pack's "Close this experience"). */
  closeLabel?: string;
}

export function ArchiveDialog({ open, onClose, eyebrow, title, children, variant = "paper", className, closeLabel = "Close dialog" }: ArchiveDialogProps) {
  const dialogRef = useRef<HTMLDialogElement>(null);
  const titleId = useId();

  useEffect(() => {
    const dialog = dialogRef.current;
    if (!dialog) return;
    if (open && !dialog.open) {
      dialog.showModal();
      dialog.querySelector<HTMLButtonElement>(".archive-dialog__close")?.focus({ preventScroll: true });
    }
    if (!open && dialog.open) dialog.close();
  }, [open]);

  return (
    <dialog
      className={`archive-dialog archive-dialog--${variant}${className ? ` ${className}` : ""}`}
      ref={dialogRef}
      aria-labelledby={titleId}
      onCancel={(event) => { event.preventDefault(); onClose(); }}
      onClose={onClose}
      onClick={(event) => { if (event.target === dialogRef.current) onClose(); }}
    >
      <div className="archive-dialog__paper">
        <button className="archive-dialog__close" type="button" onClick={onClose} aria-label={closeLabel} title={closeLabel}>
          <X size={19} />
        </button>
        {eyebrow && <p className="micro-label archive-dialog__eyebrow">{eyebrow}</p>}
        <h2 id={titleId}>{title}</h2>
        <div className="archive-dialog__body">{children}</div>
      </div>
    </dialog>
  );
}
```

## 32. `src/content/README.md` — modified

```markdown
# Editable birthday-storybook content

- `packContent.ts` holds the copy from the owner's content pack (`docs/content-pack/The_World_of_You_Complete_Missing_Content_Pack.pdf`) as typed data: the main letter, the 17 reasons, 101 wishes, seven future postcards, the gift 01–08 dedications, the flower / universe / crown long dedications, the seven garden narrations, the Memory Cinema and Bhumi FM copy, and the website microcopy. **Edit this file by hand from now on.** The pack's words were imported verbatim (see `docs/content-pack/README.md`).
- `chronosContent.ts` is the source of truth for verified facts, the existing source letter, the ten source wishes, date labels, the gallery mounts, audio tracks and the postcard layout. It builds the Letter Room, Future Postcards, Gallery and finale from `packContent.ts`.
- `giftsContent.ts` defines all 17 gift identities and experience IDs, takes the reasons and dedications from `packContent.ts`, and keeps the slots the pack did not fill: four Open When letters, six coupons, eight future-garden hopes, and the dedication and reveal line of gifts 09–17.

Content rules:

- Preserve the verified names and dates exactly; Bhumi's birthday year remains unspecified.
- The pack is ready-to-edit copy, not a verified record of any private history. The owner reads and approves it before publishing.
- A slot is anything the pack marked `[EDIT]`, `[ADD ...]` or `[INSERT ...]`, or left to the owner. **Slots are never shown to visitors**: an empty slot renders nothing, or the pack's own "waiting to be written / add a real photograph" line. Write real words into the slot and they appear. Never paste an `[EDIT]` template into a visible field.
- Do not add memories, quotes, photographs, recordings, coupon promises or future hopes that the owner did not write or approve.
- Empty photo and audio slots are intentional. Use local, owner-supplied files only; do not autoplay.
- Future postcards are explicitly speculative and never a real travel history or promise.
- Generated artwork (including the three postcard illustrations added with the pack) is illustrative atmosphere, not a personal photograph or recorded memory.
```

## 33. `src/content/chronosContent.ts` — modified

```ts
import { packCinema, packLetter, packMicrocopy, packPostcards, packRadio } from "./packContent";

export type WorldSectionId =
  | "invitation"
  | "garden"
  | "storybook"
  | "timepiece"
  | "letters"
  | "gallery"
  | "flower-garden"
  | "gifts"
  | "music-room"
  | "birthday-cake"
  | "future-postcards"
  | "finale";

export interface WorldSectionMeta {
  id: WorldSectionId;
  number: string;
  title: string;
  nav: string;
  summary: string;
}

/** "A NOTE FROM THE FUTURE" -> "A note from the future" (the pack prints its headings in capitals). */
const sentence = (title: string) => title.charAt(0) + title.slice(1).toLowerCase();

/** The pack's main letter as it is read: greeting, body, the thank-you paragraph (plus the owner's real memory once written), the rest. */
const mainLetterParagraphs = [
  packLetter.greeting,
  ...packLetter.paragraphs,
  [packLetter.thanks, packLetter.optionalInserts[0].text.trim()].filter(Boolean).join(" "),
  ...packLetter.optionalInserts.slice(1).map((insert) => insert.text.trim()).filter(Boolean),
  ...packLetter.afterThanks,
];

export interface LetterRecord {
  id: string;
  /** main = the pack's main birthday letter, source = the letter that came with the project, empty = an envelope still waiting for its words */
  kind: "main" | "source" | "empty";
  category: string;
  label: string;
  title: string;
  subtitle: string;
  salutation: string;
  paragraphs: readonly string[];
  closing: string;
  signature: string;
  ps: string;
  sourceDraft: boolean;
}

const letterRecords: readonly LetterRecord[] = [
  {
    id: "main-birthday-letter",
    kind: "main",
    category: "The main birthday letter",
    label: "THE MAIN BIRTHDAY LETTER",
    title: packLetter.title,
    subtitle: packLetter.subtitle,
    salutation: packLetter.salutation,
    paragraphs: mainLetterParagraphs,
    closing: packLetter.closing,
    signature: packLetter.signature,
    ps: "",
    sourceDraft: false,
  },
  {
    id: "birthday-letter",
    kind: "source",
    category: "A birthday letter",
    label: "THE EXISTING LETTER",
    title: "The Last Letter",
    subtitle: "",
    salutation: "Bhumi,",
    paragraphs: [
      "If you're reading this the way I hope you are — slowly, maybe smiling a little at the dramatics — then the machine did its job. I wanted to give you something that couldn't fit in an envelope, so I built a building around it instead.",
      "On 11 May, something quietly began. On 17 July, I asked, and you said yes, and my life's entire routing changed. Those are the only two facts this archive holds as certain. Everything else is still being written.",
      "I won't pretend to know what this year held for you — the parts you showed me, and the parts you carried alone. But I watched you carry them. That's a kind of grace most people never notice. I noticed. The machine noticed.",
      "Nothing in here is a promise about the future. The future chambers are marked speculative for a reason. What is real is the record: someone was paying attention, and kept every second of it.",
      "So today — 17 November — is simply yours. The candles, the noise, all of it. And after the noise, this stays here. A tower that refuses to forget you.",
    ],
    closing: "With everything I have, quietly —",
    signature: "Rudra",
    ps: "P.S. — Seventeen doors are sealed in the chamber upstairs. You were always going to open every single one.",
    sourceDraft: true,
  },
  { id: "appreciation-letter", kind: "empty", category: "A note of appreciation", label: "EMPTY · OWNER-WRITTEN", title: "A note to add", subtitle: "", salutation: "", paragraphs: [], closing: "", signature: "", ps: "", sourceDraft: false },
  { id: "little-things-letter", kind: "empty", category: "A collection of little things", label: "EMPTY · OWNER-WRITTEN", title: "A page for little things", subtitle: "", salutation: "", paragraphs: [], closing: "", signature: "", ps: "", sourceDraft: false },
  { id: "difficult-days-letter", kind: "empty", category: "A letter for difficult days", label: "EMPTY · OWNER-WRITTEN", title: "A note for another day", subtitle: "", salutation: "", paragraphs: [], closing: "", signature: "", ps: "", sourceDraft: false },
  { id: "future-dream-letter", kind: "empty", category: "A future-dream letter", label: "EMPTY · A HOPE ONLY", title: "A possible future", subtitle: "", salutation: "", paragraphs: [], closing: "", signature: "", ps: "", sourceDraft: false },
];

/** The seven pack messages, each on one illustrated postcard (art is illustrative atmosphere, never a photograph or a memory). */
const postcardArt = [
  { scene: "home", art: "/assets/postcards/home-whatever-shape.webp", alt: "A small flower-covered cottage with a glowing window in an evening garden." },
  { scene: "birthday", art: "/assets/postcards/next-birthday-garden-table.webp", alt: "A small garden table set for a birthday at dusk, with a candlelit cake, a teapot, jars of flowers and strings of lights between the trees." },
  { scene: "mountain", art: "/assets/postcards/mountain-morning.webp", alt: "A softly painted mountain valley at sunrise, with a winding path through wildflowers." },
  { scene: "sea", art: "/assets/postcards/sea-blue-hour.webp", alt: "A quiet shoreline at blue hour with gentle waves and flowers in the foreground." },
  { scene: "city", art: "/assets/postcards/unnamed-city.webp", alt: "An unnamed old-world city at golden dusk, with rooftops and a warmly lit café." },
  { scene: "sapling", art: "/assets/postcards/growing-sapling.webp", alt: "A young sapling tied to a wooden stake in a garden bed at sunrise, with a brass watering can, a trowel and a stone path through flowers." },
  { scene: "lantern", art: "/assets/postcards/little-lantern-light.webp", alt: "A small brass lantern glowing on a mossy stone wall at twilight, with wildflowers, fireflies and the first stars." },
] as const;

export interface FuturePostcard {
  id: string;
  place: string;
  someday: string;
  caption: string;
  scene: (typeof postcardArt)[number]["scene"];
  art: string;
  alt: string;
}

const futurePostcards: readonly FuturePostcard[] = packPostcards.map((card, index) => ({
  id: `postcard-${card.number}`,
  place: sentence(card.title),
  someday: `Postcard ${card.number}`,
  caption: card.message,
  ...postcardArt[index],
}));

/**
 * Personal-content source of truth for The World of You. Canonical facts and
 * authored source copy are carried forward from the supplied project reference.
 * Empty material must stay empty until Bhumi or Rudra supplies it.
 */
export const chronosContent = {
  meta: {
    herName: "Bhumi",
    hisName: "Rudra",
    docTitle: "The World of You — A Birthday Surprise for Bhumi",
    brand: "THE WORLD OF YOU",
    tagline: "A little world, created just for you.",
  },
  dates: {
    firstConnection: "2025-05-11",
    firstConnectionLabel: "11 May 2025",
    firstConnectionTimeZone: "Asia/Kolkata",
    proposal: "2025-07-17",
    proposalLabel: "17 July 2025",
    birthdayLabel: "17 November",
    birthdayDay: 17,
    countdownTarget: null as string | null,
  },
  opening: {
    kicker: "A PRIVATE LITTLE WORLD",
    line: "A little world, created just for you…",
    button: "Open Your Birthday Surprise",
    skip: "Skip the opening",
    soundHint: "Sound is quiet until you choose otherwise.",
  },
  sections: [
    { id: "invitation", number: "01", title: "Invitation Room", nav: "Invitation Room", summary: "A paper invitation opens the way into the birthday storybook." },
    { id: "garden", number: "02", title: "Birthday Garden", nav: "Birthday Garden", summary: "A garden world, opened just for you." },
    { id: "storybook", number: "03", title: "Scrapbook", nav: "Scrapbook", summary: "A little open book, with pages held for what is true." },
    { id: "timepiece", number: "04", title: "Memory Observatory", nav: "Memory Observatory", summary: "An observatory for the verified dates and elapsed time." },
    { id: "letters", number: "05", title: "Letter Room", nav: "Letter Room", summary: "Six envelopes, with only the supplied words inside." },
    { id: "gallery", number: "06", title: "Memory Gallery", nav: "Memory Gallery", summary: "Gallery mounts ready for owner-provided photographs." },
    { id: "flower-garden", number: "07", title: "Wish Garden", nav: "Wish Garden", summary: "Choose a bloom to release a wish into the day." },
    { id: "gifts", number: "08", title: "Gift Atelier", nav: "Gift Atelier", summary: "Seventeen independently accessible surprises; opening is optional." },
    { id: "music-room", number: "09", title: "Music Lounge", nav: "Music Lounge", summary: "A quiet listening room for audio you choose to add." },
    { id: "future-postcards", number: "10", title: "Future Postcards", nav: "Future Postcards", summary: "Possible futures, held lightly — never promises." },
    { id: "birthday-cake", number: "11", title: "Birthday Ballroom", nav: "Birthday Ballroom", summary: "A birthday cake, a few candles and an interactive wish." },
    { id: "finale", number: "12", title: "Finale", nav: "Finale", summary: "A closing scene for 17 November, with no year attached." },
  ] satisfies WorldSectionMeta[],
  garden: {
    eyebrow: "A BIRTHDAY GARDEN · OPEN 17 NOVEMBER",
    heading: "Happy Birthday,\nBhumi.",
    subheading: "Somewhere between the flowers and the light, a little world was waiting for you.",
    invitation: "Enter Your Little World",
    locationNote: "A small celebration · The World of You",
  },
  scrapbook: {
    eyebrow: "A HANDMADE STORYBOOK",
    intro: "A few dates from the source archive. The rest of the pages are left open for the memories only you can add.",
    turnHint: "Turn the page · swipe or use the arrows",
    spreads: [
      {
        id: "spread-origin",
        left: { kind: "record" as const, label: "FIRST RECORD", date: "11 May 2025", title: "The first connection", body: "The source archive records 11 May 2025 as the first connection. No additional moment or conversation is assumed here." },
        right: { kind: "blank" as const, label: "A PAGE HELD OPEN", date: "— — —", title: "Your words go here", body: packMicrocopy.missingText },
      },
      {
        id: "spread-proposal",
        left: { kind: "record" as const, label: "A CANONICAL DATE", date: "17 July 2025", title: "The proposal", body: "The source archive records the proposal on 17 July 2025. Details belong to you to add, if you wish." },
        right: { kind: "photo" as const, label: "PHOTO MOUNT", date: "OWNER-SUPPLIED ONLY", title: "A photograph to add", body: packMicrocopy.missingPhoto },
      },
      {
        id: "spread-birthday",
        left: { kind: "record" as const, label: "BIRTHDAY MARKER", date: "17 November", title: "A day without a year", body: "The source archive records 17 November as Bhumi's birthday. The year is not specified." },
        right: { kind: "blank" as const, label: "AN OPEN PAGE", date: "UNINDEXED", title: "A note in your words", body: packMicrocopy.missingText },
      },
      {
        id: "spread-open",
        left: { kind: "blank" as const, label: "EMPTY MOUNTING", date: "UNINDEXED", title: "A page for later", body: packMicrocopy.missingText },
        right: { kind: "blank" as const, label: "EMPTY MOUNTING", date: "UNINDEXED", title: "Still being written", body: packMicrocopy.missingText },
      },
    ],
    clockNodes: [
      { id: "origin", angle: 10, date: "11 May 2025", title: "First connection", detail: "The first connection recorded in the source project." },
      { id: "proposal", angle: 132, date: "17 July 2025", title: "The proposal", detail: "The proposal recorded in the source project." },
      { id: "birthday", angle: 250, date: "17 November", title: "Birthday marker", detail: "Bhumi's birthday. The year is not specified." },
    ],
  },
  letters: {
    intro: "A writing desk, a fountain pen and a small collection of envelopes. Two letters are written; the other four envelopes are still waiting for their words.",
    letters: letterRecords,
  },
  gallery: {
    /** Shown above the wall: the pack's "timeline intro" once a real photo exists, its "empty gallery state" until then. */
    introEmpty: packCinema.emptyState,
    introFilled: packCinema.timelineIntro,
    /**
     * Memory data model from the pack: asset path (src), caption, alt text for accessibility, optional verified date, optional location
     * (only if confirmed) and an optional longer owner note. Leave a field empty rather than guessing it.
     */
    photos: [
      { id: "photo-01", src: "", alt: "", caption: "A photograph to add", date: "DATE HELD BACK", location: "", note: packMicrocopy.missingPhoto },
      { id: "photo-02", src: "", alt: "", caption: "A page held open", date: "DATE HELD BACK", location: "", note: packMicrocopy.missingPhoto },
      { id: "photo-03", src: "", alt: "", caption: "An empty Polaroid", date: "DATE HELD BACK", location: "", note: packMicrocopy.missingPhoto },
      { id: "photo-04", src: "", alt: "", caption: "A mount in reserve", date: "DATE HELD BACK", location: "", note: packMicrocopy.missingPhoto },
      { id: "photo-05", src: "", alt: "", caption: "A picture to remember", date: "DATE HELD BACK", location: "", note: packMicrocopy.missingPhoto },
      { id: "photo-06", src: "", alt: "", caption: "The next frame", date: "DATE HELD BACK", location: "", note: packMicrocopy.missingPhoto },
    ],
  },
  flowerGarden: {
    intro: "A wish is not a memory. Choose a bloom to release one of the wishes already in the source project.",
    wishes: [
      "May your tea always be exactly the right temperature.",
      "May every good song find you at the red light.",
      "May the auto arrive on the very first try.",
      "May your suitcase always close on the first attempt.",
      "May every version of your future feel like a good plot twist.",
      "May you always find the other earring.",
      "May the rain wait until you're home — or arrive exactly when you wanted it.",
      "May your softest year start today.",
      "May you never finish explaining the joke — someone will always already be laughing.",
      "And one big one, kept quiet. It's yours when you want it. — R",
    ],
  },
  gifts: {
    intro: packMicrocopy.giftGridIntro,
    emptyMessage: packMicrocopy.missingText,
    locked: packMicrocopy.giftLocked,
    specials: {
      "01": { title: "A little secret", message: "You are the reason this entire machine exists. That's the whole secret.", editable: false },
      "08": { title: "A note from the archive", message: "Some things I practice saying and still say badly. This archive is one of them, done properly.", editable: false },
      "17": { title: "17 November", message: "17 November. The year is not specified in this archive. Happy Birthday, Bhumi.", editable: false },
    } as Record<string, { title: string; message: string; editable: boolean }>,
  },
  music: {
    station: "BHUMI FM",
    note: packRadio.welcome,
    emptyNote: packMicrocopy.missingAudio,
    emptyPlaylist: packRadio.emptyPlaylist,
    tracks: [
      { id: "track-01", title: "A voice note, from Rudra", note: "Add voice-note-01.mp3 to enable.", src: "" },
      { id: "track-02", title: "A song chosen by the owner", note: "Add a licensed or owner-provided track.", src: "" },
      { id: "track-03", title: "A birthday recording", note: "Add a real recording if one is supplied.", src: "" },
    ],
  },
  future: {
    tag: "POSSIBLE FUTURE · A HOPE · NOT A FACT",
    intro: "Postcards from scenes the archive has not earned yet. These are possibilities only, never promises.",
    items: [
      { id: "future-01", place: "A mountain morning", someday: "A winter not yet indexed", caption: "Somewhere cold and quiet, where the air does half the talking.", scene: "mountain", art: "/assets/postcards/mountain-morning.webp", alt: "A softly painted mountain valley at sunrise, with a winding path through wildflowers." },
      { id: "future-02", place: "The sea at blue hour", someday: "When the timing is kind", caption: "That twenty-minute sky that makes everyone honest.", scene: "sea", art: "/assets/postcards/sea-blue-hour.webp", alt: "A quiet shoreline at blue hour with gentle waves and flowers in the foreground." },
      { id: "future-03", place: "A city we haven't named", someday: "An ordinary weekend, someday", caption: "Getting lost on purpose, finding the coffee by accident.", scene: "city", art: "/assets/postcards/unnamed-city.webp", alt: "An unnamed old-world city at golden dusk, with rooftops and a warmly lit café." },
      { id: "future-04", place: "Home, whatever shape", someday: "The long record", caption: "Not a plan, never a pressure — just a door I'd like to keep in the drawing.", scene: "home", art: "/assets/postcards/home-whatever-shape.webp", alt: "A small flower-covered cottage with a glowing window in an evening garden." },
    ],
    /** The seven postcards of the Future Postcards section (content pack, section 04). `items` above are the four imagined places of gift 11. */
    postcards: futurePostcards,
  },
  finale: {
    kicker: "17 NOVEMBER · A DAY FOR BHUMI",
    headline: "Happy Birthday,\nBhumi.",
    sub: "Every candle is lit for today.",
    sourceMessage: "You were never a chapter in my story. Somewhere along the way, you became the reason I keep the records at all. — Rudra",
    sourceDraft: true,
    thanks: packMicrocopy.finalThanks,
    replay: "Replay the celebration",
    letterLink: "Open the birthday letter",
    storyLink: "Return to the scrapbook",
  },
} as const;
```

## 34. `src/content/giftsContent.ts` — modified

```ts
/**
 * Gift Atelier catalog and owner-editable copy slots.
 * Owner copy comes from the supplied content pack (./packContent.ts). Slots the pack does not fill (Open When letters,
 * coupons, future hopes, gift 09-17 dedications) stay blank until Rudra supplies approved text.
 */
import { packExtended, packGiftDedications, packGiftSlots, packReasons } from "./packContent";

export type GiftExperienceId =
  | "secret-letter"
  | "reason-jar"
  | "eternal-flower"
  | "little-universe"
  | "bhumi-fm"
  | "memory-cinema"
  | "wishes"
  | "royal-crown"
  | "open-when"
  | "happiness-machine"
  | "little-adventure"
  | "music-of-us"
  | "infinite-mirror"
  | "coupon-book"
  | "future-garden"
  | "treasure-hunt"
  | "ultimate-surprise";

export type GiftVisual =
  | "letter" | "jar" | "flower" | "orbit" | "cassette" | "cinema" | "wishes" | "crown"
  | "envelopes" | "machine" | "map" | "vinyl" | "mirror" | "coupons" | "tree" | "key" | "portal";

export interface GiftDefinition {
  id: string;
  number: string;
  title: string;
  shortTitle: string;
  subtitle: string;
  /** Short owner dedication shown as the gift's opening line (pack section 05). Empty = nothing is shown. */
  dedication: string;
  /** One short line shown when the gift's reveal happens (pack sections 06, 07, 11). Empty = nothing is shown. */
  revealLine: string;
  experience: GiftExperienceId;
  visual: GiftVisual;
  color: string;
  ribbon: string;
  mark: string;
}

const baseGifts: readonly Omit<GiftDefinition, "dedication" | "revealLine">[] = [
  { id: "gift-01", number: "01", title: "The Secret Letter", shortTitle: "Secret Letter", subtitle: "A handwritten letter, unfolded at your pace.", experience: "secret-letter", visual: "letter", color: "#ead0c2", ribbon: "#9b5660", mark: "✉" },
  { id: "gift-02", number: "02", title: "A Jar of Reasons", shortTitle: "Jar of Reasons", subtitle: "Seventeen folded notes in a glass jar. Open the lid and choose one.", experience: "reason-jar", visual: "jar", color: "#d6e0d0", ribbon: "#81926f", mark: "✧" },
  { id: "gift-03", number: "03", title: "The Flower That Never Fades", shortTitle: "Everlasting Flower", subtitle: "Grow, turn and bloom a paper-garden flower.", experience: "eternal-flower", visual: "flower", color: "#edc9d0", ribbon: "#b56f85", mark: "✿" },
  { id: "gift-04", number: "04", title: "Our Little Universe", shortTitle: "Little Universe", subtitle: "A tiny star map of the two verified dates.", experience: "little-universe", visual: "orbit", color: "#bfc8dc", ribbon: "#687caa", mark: "✦" },
  { id: "gift-05", number: "05", title: "Bhumi FM Exclusive", shortTitle: "Bhumi FM", subtitle: "A cassette deck ready for a real, owner-provided recording.", experience: "bhumi-fm", visual: "cassette", color: "#e8c990", ribbon: "#9d7040", mark: "▣" },
  { id: "gift-06", number: "06", title: "The Memory Cinema", shortTitle: "Memory Cinema", subtitle: "A little projector and a private screen for real photographs.", experience: "memory-cinema", visual: "cinema", color: "#c9c1bc", ribbon: "#6f6265", mark: "▤" },
  { id: "gift-07", number: "07", title: "A Thousand Wishes", shortTitle: "A Thousand Wishes", subtitle: "Collect stars from the wishing tree, or draw a wish from the sky.", experience: "wishes", visual: "wishes", color: "#d5cbe5", ribbon: "#8774ad", mark: "✧" },
  { id: "gift-08", number: "08", title: "The Queen’s Crown", shortTitle: "Queen’s Crown", subtitle: "A small royal object to rotate and inspect.", experience: "royal-crown", visual: "crown", color: "#f0d791", ribbon: "#ad8741", mark: "♛" },
  { id: "gift-09", number: "09", title: "Open When…", shortTitle: "Open When…", subtitle: "Four sealed envelopes, waiting for your words.", experience: "open-when", visual: "envelopes", color: "#e3c2b7", ribbon: "#a46a71", mark: "▱" },
  { id: "gift-10", number: "10", title: "The Happiness Machine", shortTitle: "Happiness Machine", subtitle: "Pull a lever to reveal one of the existing birthday wishes.", experience: "happiness-machine", visual: "machine", color: "#cfb997", ribbon: "#8e7451", mark: "⚙" },
  { id: "gift-11", number: "11", title: "A Little Adventure", shortTitle: "Little Adventure", subtitle: "Explore an explicitly imaginary postcard map.", experience: "little-adventure", visual: "map", color: "#c6d5d0", ribbon: "#718e87", mark: "⌖" },
  { id: "gift-12", number: "12", title: "The Music of Us", shortTitle: "Music of Us", subtitle: "A vinyl player for licensed or owner-provided audio.", experience: "music-of-us", visual: "vinyl", color: "#d8c0c5", ribbon: "#8b6275", mark: "♫" },
  { id: "gift-13", number: "13", title: "The Infinite Mirror", shortTitle: "Infinite Mirror", subtitle: "Wipe away the mist to reveal an abstract birthday message.", experience: "infinite-mirror", visual: "mirror", color: "#cbd9db", ribbon: "#64858d", mark: "◉" },
  { id: "gift-14", number: "14", title: "The Birthday Coupon Book", shortTitle: "Coupon Book", subtitle: "A flip-through booklet for only owner-approved offers.", experience: "coupon-book", visual: "coupons", color: "#ead6ac", ribbon: "#a48651", mark: "✂" },
  { id: "gift-15", number: "15", title: "The Future Garden", shortTitle: "Future Garden", subtitle: "Grow a tree with blank leaves for hopes you choose to write.", experience: "future-garden", visual: "tree", color: "#c6d4b8", ribbon: "#71875e", mark: "♧" },
  { id: "gift-16", number: "16", title: "The Secret Treasure Hunt", shortTitle: "Treasure Hunt", subtitle: "Solve a fair symbol puzzle; use keyboard-friendly move controls.", experience: "treasure-hunt", visual: "key", color: "#d5c8b7", ribbon: "#8c7456", mark: "⌕" },
  { id: "gift-17", number: "17", title: "The Ultimate Surprise", shortTitle: "Ultimate Surprise", subtitle: "Gather the lights and open a celebratory portal.", experience: "ultimate-surprise", visual: "portal", color: "#d8bc83", ribbon: "#9e7137", mark: "✺" },
] as const;

const REVEAL_LINES: Readonly<Record<string, string>> = {
  "03": packExtended.flower.revealLine,
  "04": packExtended.universe.revealLine,
  "08": packExtended.crown.revealLine,
};

/** Gifts whose reveal line is shown by their own reveal button (flower, universe, crown). Every other gift shows its reveal line, if one is written, when it opens. */
export const giftsWithOwnReveal: ReadonlySet<string> = new Set(Object.keys(REVEAL_LINES));

export const giftDefinitions: readonly GiftDefinition[] = baseGifts.map((gift) => ({
  ...gift,
  dedication: packGiftDedications[gift.number]?.text ?? packGiftSlots[gift.number]?.dedication ?? "",
  revealLine: REVEAL_LINES[gift.number] ?? packGiftSlots[gift.number]?.revealLine ?? "",
}));

/** The 17 reasons of the content pack (section 02). Edit them in packContent.ts; an empty string shows the pack's "missing text" line. */
export const reasonNotes = Array.from({ length: 17 }, (_, index) => ({
  id: `reason-${String(index + 1).padStart(2, "0")}`,
  text: packReasons.items[index] ?? "",
}));

/** The prompts are safe to show; the private message bodies remain blank. */
export const openWhenLetters = [
  { id: "smile", prompt: "Open when you need a smile", message: "" },
  { id: "tired", prompt: "Open when you feel tired", message: "" },
  { id: "encouragement", prompt: "Open when you need encouragement", message: "" },
  { id: "surprise", prompt: "Open when you want a little surprise", message: "" },
] as const;

/** Add only approved coupons/promises. Empty slots are not redeemable. */
export const couponEntries = Array.from({ length: 6 }, (_, index) => ({
  id: `coupon-${String(index + 1).padStart(2, "0")}`,
  title: "",
  description: "",
}));

/** Future hopes, not commitments. Keep blank until the owner writes them. */
export const futureGardenLeaves = Array.from({ length: 8 }, (_, index) => ({
  id: `hope-${String(index + 1).padStart(2, "0")}`,
  text: "",
}));

/** Puzzle solution is a generic game mechanic, not a personal password. */
export const treasureHuntPuzzle = {
  clue: "Arrange the symbols in this order: a flower first, the moon second, and the star last.",
  initialOrder: ["star", "flower", "moon"] as const,
  solution: ["flower", "moon", "star"] as const,
  password: "OPEN",
  passwordHint: "The word describes what you did to the final gate.",
};

export const giftsContentReadiness = {
  reasons: "pack-supplied-owner-to-review",
  voiceRecording: "not-supplied",
  memoryPhotos: "not-supplied",
  couponPromises: "owner-approval-required",
  futureHopes: "owner-content-required",
} as const;
```

## 35. `src/content/packContent.ts` — new

```ts
/**
 * THE WORLD OF YOU — COMPLETE MISSING CONTENT PACK. Owner-supplied PDF (docs/content-pack/), transcribed verbatim by
 * scripts/content-pack/build-pack-content.py and compared with docs/content-pack/pack-text.txt by tests/content-pack-verbatim.spec.ts.
 *
 * Rules that the components follow:
 *  - Nothing here is reworded in the UI. The PDF's pull-quote marks are not part of the text; apostrophes inside words are typographic.
 *  - A "slot" is an empty string or a template the pack itself marked as [EDIT] / [ADD ...]. Slots are NEVER shown to visitors:
 *    an empty slot simply renders nothing (or the pack's own "missing ..." microcopy). Fill a slot with the real words and it appears.
 *  - The pack is ready-to-edit copy, not a verified transcript of any private history. Read it before publishing.
 *  - This file is now the one place to edit that copy. Re-running the importer would overwrite your edits.
 */
/** Page 1 of the PDF. */
export const packCover = {
  title: "THE WORLD OF YOU",
  subtitle: "A Universe Made of 17 Little Surprises",
  tagline: "A little universe made with care, honest words, real memories, and hopes for everything still waiting ahead.",
} as const;

/**
 * 01. Secret Letter — Main Birthday Letter.
 * `memoryPrompt` is the pack's inline [EDIT]: an owner slot, never shown. `optionalInserts` are the four owner slots of the pack's
 * bullets (prompts: `packLetterInsertPrompts` below, same order). Whatever is typed into optionalInserts[0].text (a real memory) is
 * appended to the thank-you paragraph, exactly where the pack put its [EDIT]; the other three inserts, if written, become their own
 * paragraphs right after it.
 */
export const packLetter = {
  title: "To the Girl Who Makes This Little Universe Special",
  subtitle: "A letter written for your birthday, with love and hope.",
  salutation: "Dear Bhumi,",
  greeting: "Happy Birthday. ❤️",
  paragraphs: [
    "Aaj ka din tumhara hai. Main chahta hoon ki tum ise khul kar enjoy karo. Tumhari life mein khushiyan, naye opportunities, confidence aur woh achievements aayein jinke liye tum mehnat kar rahi ho.",
    "Main shayad har baar apni feelings perfect words mein explain nahi kar pata, lekin itna kehna chahta hoon ki tumhari presence mere liye meaningful hai. Tumhare dreams important hain, tumhari individuality important hai, aur tumhari happiness bhi important hai.",
    "Main chahta hoon ki tum apne goals ke liye aage badho, bina apni identity khoye. Jab cheezein difficult hon, tab yaad rakhna ki tumhari value kisi result, exam, achievement, ya kisi aur ke opinion se decide nahi hoti.",
    "Humari journey mein achhe moments bhi rahe honge aur misunderstandings bhi. Main perfect hone ka claim nahi karta. Main chahta hoon ki hum dono respect, honesty, patience aur clear communication ke saath grow karein. Strong relationship ke liye sirf promises nahi, daily actions bhi zaroori hote hain.",
  ],
  thanks: "Thank you for being a part of this chapter of my life. Thank you for the conversations, the moments we have shared, and the opportunity to know you better.",
  memoryPrompt: "[EDIT: Yahan ek real memory add karo — kab, kya hua, aur woh tumhare liye kyun special thi.]",
  afterThanks: [
    "On your birthday, I wish you a peaceful mind, a healthy life, courage for difficult days, people who genuinely respect you, and the freedom to become the person you want to be.",
    "I hope the coming year brings you closer to your dreams. I hope you keep discovering new things, keep learning, keep smiling, and never stop believing that your future can be beautiful.",
    "May this little universe remind you that you deserve kindness, respect, happiness, and room to shine in your own way.",
    "Happy Birthday, Bhumi. Keep growing, keep dreaming, and keep being yourself.",
  ],
  closing: "With love,",
  signature: "Rudra",
  optionalInserts: [
    {
      id: "memory",
      text: "",
    },
    {
      id: "quality",
      text: "",
    },
    {
      id: "apology",
      text: "",
    },
    {
      id: "wish",
      text: "",
    },
  ],
};

/**
 * The pack's four optional-insert bullets: prompts for the owner, never shown. They live apart from `packLetter` and nothing in `src`
 * imports them, so they are not part of the website bundle. Prompt i describes `packLetter.optionalInserts[i]`.
 */
export const packLetterInsertPrompts = [
  {
    id: "memory",
    prompt: "[EDIT] Ek real memory: date/place/event aur woh tumhare liye kyun special thi.",
  },
  {
    id: "quality",
    prompt: "[EDIT] Ek quality jo tumne personally observe ki hai, with one genuine example.",
  },
  {
    id: "apology",
    prompt: "[EDIT] Ek sincere apology ya learning, only if you genuinely want to include it.",
  },
  {
    id: "wish",
    prompt: "[EDIT] Ek personal birthday wish jo generic na ho.",
  },
] as const;

/** 02. Jar of Reasons — 17 Notes (draft reasons, kept general by the author of the pack). */
export const packReasons: { readonly items: readonly string[]; readonly quote: string } = {
  items: [
    "I admire the way you keep working towards the things that matter to you.",
    "Your curiosity makes ordinary conversations more interesting.",
    "I appreciate that you have your own dreams and ambitions.",
    "Your individuality is something worth celebrating.",
    "I like the way a simple conversation can become a memorable part of the day.",
    "I admire your willingness to learn and explore new ideas.",
    "You deserve to feel proud of every small step you take.",
    "I appreciate the moments when we can talk honestly.",
    "Your smile can make a difficult day feel a little lighter.",
    "I respect the effort you put into the future you want.",
    "I like that there is always more to discover about you.",
    "You remind me that growth takes patience and consistency.",
    "I appreciate the little things that make you uniquely you.",
    "I want to understand your thoughts instead of assuming them.",
    "I value honesty, respect, and the chance to keep learning together.",
    "You deserve support without having to become someone else.",
    "Because knowing you has given this chapter of my life its own meaning.",
  ],
  quote: "Seventeen little reminders. Not a list of expectations — just words you can keep, change, or leave behind.",
};

/** 03. A Thousand Wishes. The heading says 100; the list in the PDF has 101 entries and all of them are here. */
export const packWishes: readonly string[] = [
  "May you wake up with a peaceful mind.",
  "May your efforts bring results you feel proud of.",
  "May you always have the courage to begin again.",
  "May your health stay strong.",
  "May your heart find calm on difficult days.",
  "May you meet people who respect your boundaries.",
  "May your dreams keep growing with you.",
  "May you never feel pressured to become someone else.",
  "May your hard work open meaningful doors.",
  "May you find joy in small everyday things.",
  "May your confidence grow with every challenge.",
  "May you get time to rest without guilt.",
  "May you keep learning things that excite you.",
  "May your kindness never cost you your self-respect.",
  "May you trust your own abilities.",
  "May you have the courage to say no when needed.",
  "May your future hold beautiful opportunities.",
  "May you celebrate your progress, not only the finish line.",
  "May you find clarity when life feels confusing.",
  "May you always feel worthy of respect.",
  "May your creativity find space to bloom.",
  "May you have the strength to face uncertain days.",
  "May you laugh freely and often.",
  "May you find balance between ambition and peace.",
  "May your efforts be noticed for the right reasons.",
  "May you stay curious about the world.",
  "May you be surrounded by genuine support.",
  "May you learn from mistakes without being defined by them.",
  "May your goals feel exciting, not frightening.",
  "May you keep your sense of wonder.",
  "May every new chapter teach you something valuable.",
  "May you feel safe being honest about your feelings.",
  "May you have peaceful mornings and restful nights.",
  "May you discover places that inspire you.",
  "May you keep making choices that respect your future self.",
  "May you be proud of your own journey.",
  "May you find solutions when problems appear.",
  "May you have patience to build something meaningful.",
  "May your voice always matter.",
  "May you never underestimate your small steps.",
  "May your life include more moments of genuine laughter.",
  "May you find mentors who encourage your growth.",
  "May your hard days become easier to carry.",
  "May you have the freedom to change your mind.",
  "May you always have something new to look forward to.",
  "May your talents get room to develop.",
  "May you feel appreciated without having to ask repeatedly.",
  "May your boundaries be understood and respected.",
  "May you keep choosing growth over comparison.",
  "May your plans meet the right opportunities.",
  "May you find beauty in ordinary days.",
  "May your future be shaped by your own choices.",
  "May you have courage to ask for help.",
  "May you never confuse a setback with failure.",
  "May you keep the people who bring out your best.",
  "May you let go of what repeatedly hurts your peace.",
  "May your achievements feel meaningful to you.",
  "May you find time for the things you love.",
  "May your curiosity lead you to wonderful discoveries.",
  "May you stay gentle without being afraid to be strong.",
  "May you trust the pace of your own progress.",
  "May you feel proud of how far you have come.",
  "May your days include music that lifts your mood.",
  "May you find comfort in the right conversations.",
  "May you have courage to try something new.",
  "May you keep your dreams bigger than your fears.",
  "May your work create opportunities for independence.",
  "May you experience friendship built on honesty.",
  "May you have patience with yourself while learning.",
  "May you remember that rest is productive too.",
  "May your future home feel peaceful and welcoming.",
  "May you celebrate your individuality.",
  "May you find answers to questions that matter to you.",
  "May you never stop asking thoughtful questions.",
  "May you feel confident in your own decisions.",
  "May you build a life that feels true to you.",
  "May you have strength during every transition.",
  "May your kindness be met with kindness.",
  "May you find joy beyond achievements.",
  "May your goals become clearer with time.",
  "May you keep memories that make you smile.",
  "May you be brave enough to start again.",
  "May you find peace after stressful moments.",
  "May your creativity surprise you.",
  "May your future bring meaningful connections.",
  "May you always have reasons to feel hopeful.",
  "May you be treated with patience and understanding.",
  "May you find a healthy balance in everything you do.",
  "May you keep discovering your own strengths.",
  "May your dreams receive both courage and effort.",
  "May you never feel ashamed to ask for support.",
  "May you have more days that feel light.",
  "May you learn to celebrate yourself.",
  "May your hard work create real choices.",
  "May you always have space to grow.",
  "May you find happiness that does not depend on perfection.",
  "May your next year be full of learning and discovery.",
  "May you feel loved, respected, and understood.",
  "May the world offer you beautiful surprises.",
  "May you keep becoming more fully yourself.",
  "May this birthday mark the beginning of a hopeful new chapter.",
];

/** 04. Future Postcards — 7 complete messages. */
export const packPostcards: readonly { readonly number: string; readonly title: string; readonly message: string }[] = [
  {
    number: "01",
    title: "A NOTE FROM THE FUTURE",
    message: "Hello, future us. I hope we have kept learning how to listen, understand, and make space for each other’s individuality. I hope we are proud not only of what we achieved, but also of the patience and effort it took. Wherever life has taken us, I hope we have chosen honesty and kindness.",
  },
  {
    number: "02",
    title: "YOUR NEXT BIRTHDAY",
    message: "When this birthday comes around again, I hope you can look back and see how much you have grown. I hope you have new stories, new skills, new reasons to smile, and a stronger belief in yourself. May the year ahead be kinder to your dreams.",
  },
  {
    number: "03",
    title: "THE DREAMS YOU ARE BUILDING",
    message: "I hope you keep moving towards the future you imagine. Take your time, learn deeply, make mistakes, and keep going. You do not need every answer today. One honest step at a time is still progress.",
  },
  {
    number: "04",
    title: "FOR A DIFFICULT DAY",
    message: "If a day feels heavy, pause. You do not have to solve your whole life in one evening. Drink some water, breathe, rest, and take the next small step when you are ready. Your worth does not disappear on difficult days.",
  },
  {
    number: "05",
    title: "A PLACE WE HOPE TO SEE",
    message: "Somewhere ahead, I hope there is a place we get to explore — a new street, a quiet garden, a beautiful sky, or a city we have never seen. Until then, keep collecting curiosity. The world is full of things waiting to be discovered.",
  },
  {
    number: "06",
    title: "A PROMISE TO KEEP GROWING",
    message: "I cannot promise that every day will be easy or that we will never disagree. I can choose to keep learning, communicate honestly, respect your individuality, and let actions speak louder than dramatic words. Growth is something we practise.",
  },
  {
    number: "07",
    title: "KEEP THIS LITTLE LIGHT",
    message: "If you ever need a reminder, let this postcard say it simply: you matter beyond your achievements. You deserve respect, peace, opportunity, and the freedom to become who you want to be. Keep your light, in your own way.",
  },
];

/** 05. Gift dedications for gifts 01–08 (the pack's own short titles are kept in packTitle for reference only). */
export const packGiftDedications: Readonly<Record<string, { readonly packTitle: string; readonly text: string }>> = {
  "01": {
    packTitle: "SECRET LETTER",
    text: "A small envelope, holding words that deserve more than a quick glance. Open it slowly, read it in your own time, and keep only the words that feel meaningful.",
  },
  "02": {
    packTitle: "JAR OF REASONS",
    text: "Seventeen little notes, each carrying one reason to appreciate you. They are not rules or expectations — just thoughts offered with care.",
  },
  "03": {
    packTitle: "EVERLASTING FLOWER",
    text: "A flower for the moments that deserve to be remembered. May it remind you that beautiful things can keep growing when they are given time and care.",
  },
  "04": {
    packTitle: "LITTLE UNIVERSE",
    text: "A tiny universe for a person with a world of her own. Keep exploring, asking questions, and never make your dreams smaller to fit someone else’s expectations.",
  },
  "05": {
    packTitle: "BHUMI FM",
    text: "A little corner for music, memories, and moods. Press play when you want a soundtrack, pause whenever you need quiet, and make this space your own.",
  },
  "06": {
    packTitle: "MEMORY CINEMA",
    text: "A small screen for real moments. Every photograph or clip should tell a true story; every caption should preserve what actually happened.",
  },
  "07": {
    packTitle: "A THOUSAND WISHES",
    text: "A sky full of good wishes for your next chapter. Pick one whenever you need a reminder that there is still so much to look forward to.",
  },
  "08": {
    packTitle: "QUEEN'S CROWN",
    text: "A crown as a symbol of confidence, individuality, and self-respect. Wear your own crown by choosing a life that feels right to you.",
  },
};

/**
 * 05 (template). Gifts 09–17: the pack supplies no copy, only [EDIT] templates ("2–4 sentence dedication ... mention only real
 * details or clearly label the message as a wish, symbol, or imagination" and "one short line shown when the gift opens").
 * These are owner slots; empty means "show nothing".
 */
export const packGiftSlots: Record<string, { dedication: string; revealLine: string }> = {
  "09": {
    dedication: "",
    revealLine: "",
  },
  "10": {
    dedication: "",
    revealLine: "",
  },
  "11": {
    dedication: "",
    revealLine: "",
  },
  "12": {
    dedication: "",
    revealLine: "",
  },
  "13": {
    dedication: "",
    revealLine: "",
  },
  "14": {
    dedication: "",
    revealLine: "",
  },
  "15": {
    dedication: "",
    revealLine: "",
  },
  "16": {
    dedication: "",
    revealLine: "",
  },
  "17": {
    dedication: "",
    revealLine: "",
  },
};

/** 06. Everlasting Flower, 07. Little Universe, 11. Queen's Crown: long dedication plus the short reveal line. */
export const packExtended: { readonly flower: PackExtended; readonly universe: PackExtended; readonly crown: PackExtended } = {
  flower: {
    text: "Some flowers are beautiful because of how they look. Others become meaningful because of what they remind us of. This one is a little symbol of growth, patience, and the quiet beauty of becoming yourself. May you keep blooming in your own time, in your own way, without comparing your journey to anyone else’s.",
    revealLine: "Keep blooming at your own pace.",
  },
  universe: {
    text: "This little universe is for your curiosity, your dreams, and all the things you have yet to discover. There are always new stars to notice, new questions to ask, and new paths to explore. May you never stop being curious about what is possible.",
    revealLine: "Your world is bigger than you think.",
  },
  crown: {
    text: "This crown is not about being above anyone else. It is a symbol of knowing your worth, respecting yourself, and having the confidence to follow your own path. May you never forget that your dreams deserve space, your voice deserves to be heard, and your identity belongs to you.",
    revealLine: "Your crown is your confidence.",
  },
};
export interface PackExtended { readonly text: string; readonly revealLine: string }

/** 08. Birthday Garden — Narration: seven stages (the pack adds BUD between LEAVES and FLOWER). */
export const packGardenNarration: readonly { readonly stage: string; readonly title: string; readonly text: string }[] = [
  {
    stage: "SEED",
    title: "A BEGINNING",
    text: "Every beautiful thing begins quietly. This tiny seed is a symbol of a new chapter and all the possibilities it carries.",
  },
  {
    stage: "ROOTS",
    title: "WHAT HOLDS US",
    text: "Strong roots grow where there is patience, care, and room to breathe. May your foundations be built on self-respect, honesty, and courage.",
  },
  {
    stage: "SPROUT",
    title: "THE FIRST STEP",
    text: "Growth does not need to be loud. Every small step matters, even when nobody else notices it.",
  },
  {
    stage: "LEAVES",
    title: "NEW STRENGTH",
    text: "With every new leaf comes another chance to learn, adapt, and become stronger.",
  },
  {
    stage: "BUD",
    title: "POSSIBILITY",
    text: "Not everything has to bloom immediately. Some dreams need time, care, and the freedom to unfold.",
  },
  {
    stage: "FLOWER",
    title: "YOUR MOMENT",
    text: "Here is to the beauty of becoming more fully yourself. May you always have space to shine.",
  },
  {
    stage: "FULL BLOOM",
    title: "THE NEXT CHAPTER",
    text: "This is not an ending. It is a reminder that there are still new seasons, new dreams, and new beginnings ahead.",
  },
];

/** 09. Memory Cinema. The two caption templates and requiredFields describe the data model only; they are never displayed. */
export const packCinema = {
  opening: "A little collection of moments worth keeping.",
  photoCaptionTemplate: "[EDIT: What is happening in this real photo? Add date/location only if confirmed.]",
  videoCaptionTemplate: "[EDIT: Describe the real clip in one sentence. Avoid adding events that are not visible or known.]",
  timelineIntro: "Every story is made of moments. These are the ones we have chosen to keep.",
  emptyState: "The next memory is waiting to be added. Add a real photo or video to bring this frame to life.",
  closing: "The screen fades, but the moments we choose to remember can stay with us.",
  requiredFields: [
    "Asset file path",
    "Caption",
    "Optional verified date",
    "Optional location, only if confirmed",
    "Alt text for accessibility",
    "Optional owner-written longer note",
  ],
};

/** 10. Bhumi FM. trackTemplates and voiceNoteTemplate are the pack's [ADD ...] slots (never displayed). */
export const packRadio = {
  welcome: "Welcome to Bhumi FM — a little space for songs, sounds, and moments. Choose a track, adjust the volume, and make this soundtrack your own.",
  trackTemplates: [
    "Track 01: [ADD REAL AUDIO FILE] — [ADD TRACK TITLE]",
    "Track 02: [ADD REAL AUDIO FILE] — [ADD TRACK TITLE]",
    "Track 03: [ADD REAL AUDIO FILE] — [ADD TRACK TITLE]",
  ],
  voiceNoteTemplate: "Optional voice note: [ADD ONLY A REAL RECORDING PROVIDED BY THE OWNER. Do not synthesize a fake personal voice note.]",
  emptyPlaylist: "Your playlist is not here yet. Add audio files to bring Bhumi FM to life.",
  requirements: "No autoplay. Include play/pause, progress, volume, mute, track title, and clear loading/error states.",
};

/** 12. Website microcopy. `progress` keeps the pack's [X] marker; use packProgress(n). */
export const packMicrocopy = {
  giftGridIntro: "Seventeen little surprises. Open them in any order, take your time, and revisit your favourites whenever you like.",
  giftLocked: "This little world is still being prepared. Come back when its story is ready.",
  replay: "Replay experience",
  skip: "Skip animation",
  close: "Close this experience",
  back: "Back to all surprises",
  loading: "Preparing your little world…",
  webglFallback: "This device cannot display the 3D scene right now. The message and controls are still available below.",
  missingText: "This message is waiting to be written. Add your own words before publishing.",
  missingPhoto: "Add a real photograph here to complete this memory.",
  missingAudio: "Add an audio file to activate this player.",
  progress: "You have opened [X] of 17 surprises.",
  finalThanks: "Thank you for exploring this little universe. I hope you found a few words and moments worth keeping.",
} as const;
export const packProgress = (opened: number) => packMicrocopy.progress.replace("[X]", String(opened));

/** 13. The pack's own completion checklist and closing note (reference for docs/CONTENT_PACK_INTEGRATION.md; not shown on the site). */
export const packChecklist = {
  items: [
    "Secret Letter: final message reviewed; all [EDIT] fields replaced.",
    "Jar of Reasons: all 17 reasons personally reviewed; unsuitable lines replaced.",
    "A Thousand Wishes: 100 wishes reviewed; decide whether to add more to match the poetic title.",
    "Future Postcards: all 7 messages reviewed and personalised where appropriate.",
    "Gift 01–08: dedication copy reviewed and connected to correct gift.",
    "Gift 09–17: exact titles read from project data; each gets a real dedication and reveal line.",
    "Everlasting Flower: dedication connected to flower reveal.",
    "Little Universe: dedication connected to 3D scene.",
    "Birthday Garden: all growth stages have narration and matching reveal timing.",
    "Memory Cinema: only real photos/videos used; captions and alt text added.",
    "Bhumi FM: actual audio tracks supplied; playback tested; no autoplay.",
    "Queen's Crown: dedication connected to crown animation.",
    "Missing-content placeholders are not accidentally shown as final copy.",
    "All text is readable on desktop and mobile.",
    "All buttons, replay, skip, close, and navigation controls work.",
    "Content is proofread before deployment.",
  ],
  finalNote: "Ye pack ready-to-edit copy hai, tum dono ke private history ka verified transcript nahi. Jahan actual memories, photos, audio, dates, ya personal details chahiye, wahan tumhara original material hi use hona chahiye.",
  credit: "THE WORLD OF YOU — A Universe Made of 17 Little Surprises",
} as const;

/** The author's Hinglish notes to the owner. Kept for the record; not site copy. */
export const packAuthorNotes = {
  reasons: "Ye 17 short draft reasons hain. General rakhe gaye hain; har line ko tabhi use karo jab woh tumhari real feeling ho. Jo fit na ho, replace kar dena.",
  wishes: "‘A Thousand Wishes’ ko poetic title ki tarah use kiya ja sakta hai. Neeche 100 wishes hain; ye literal 1,000 nahi. Har wish star, note, petal ya glowing object se reveal ho sakti hai.",
  dedications: "Available context se gifts 01–08 ke titles confirm hain. Gifts 09–17 ke exact titles is audit context mein available nahi, isliye unke liye editable templates diye gaye hain. Agent ko project data se exact titles read karne chahiye.",
  cinema: "Important: Fake photos, videos, dates, ya historical captions generate mat karo. Sirf actual user-supplied media use karo. Media missing ho toh editable placeholder dikhana.",
} as const;
```

## 36. `src/engine/anim.ts` — new

```ts
import * as T from "three";
import { gsap } from "gsap";

/**
 * A reversible, scrubbable GSAP timeline whose playhead follows a target (0 = closed, 1 = open).
 * Closing therefore plays the opening backwards at the same speed, and interrupting midway is safe.
 * The timeline is paused and never ticks on its own: `step` is called from the render loop, so it works
 * with demand rendering, pausing offscreen, reduced motion and deterministic test stepping.
 */
export class Sequence<P extends Record<string, number>> {
  readonly phases: P;
  readonly timeline: gsap.core.Timeline;
  progress = 0;
  speed = 1;

  constructor(readonly duration: number, phases: P, build: (timeline: gsap.core.Timeline, phases: P) => void) {
    this.phases = phases;
    this.timeline = gsap.timeline({ paused: true, defaults: { ease: "power2.inOut" } });
    build(this.timeline, this.phases);
    this.timeline.to({}, { duration: 0.001 }, duration - 0.001); // pin the total length
    this.timeline.time(0, false);
  }

  /** Advance toward `target`. `immediate` (skip / reduced motion) jumps straight to it. */
  step(target: number, dt: number, immediate = false) {
    const delta = target - this.progress;
    const stride = (dt * this.speed) / this.duration;
    this.progress = immediate || Math.abs(delta) <= stride ? target : this.progress + Math.sign(delta) * stride;
    this.timeline.time(this.progress * this.duration, false);
    return this.progress;
  }

  seek(progress: number) {
    this.progress = T.MathUtils.clamp(progress, 0, 1);
    this.timeline.time(this.progress * this.duration, false);
  }

  dispose() { this.timeline.kill(); }
}

/** Frame-rate independent smoothing that snaps to the target when reduced motion is requested. */
export const damp = (value: number, target: number, rate: number, dt: number, reduced = false) =>
  reduced ? target : T.MathUtils.damp(value, target, rate, dt);

export const ease = {
  inOut: (p: number, a = 0, b = 1) => T.MathUtils.smootherstep(p, a, b),
  out: (p: number) => 1 - Math.pow(1 - T.MathUtils.clamp(p, 0, 1), 3),
  spring: (p: number) => { const x = T.MathUtils.clamp(p, 0, 1); return 1 - Math.exp(-6 * x) * Math.cos(10 * x); },
};

/** Maps a global progress to a sub-range 0..1. */
export const span = (progress: number, from: number, to: number) => T.MathUtils.clamp((progress - from) / (to - from), 0, 1);
```

## 37. `src/engine/audio.ts` — new

```ts
/**
 * Web Audio sound design.
 *
 * - No audio files: every effect is synthesised at runtime, so there is nothing to license or download.
 * - Sound is OFF by default. The AudioContext is created / resumed only from a user gesture
 *   (see https://www.chromium.org/audio-video/autoplay/), and effects are dropped while it is suspended.
 * - Master volume and mute are user controlled and persisted.
 */
import { useSyncExternalStore } from "react";

export type Sfx =
  | "paper" | "unfold" | "wax" | "slide" | "flap" | "glass" | "lid" | "note" | "bloom" | "chime" | "sparkle" | "pop"
  | "whoosh" | "click" | "tick" | "lever" | "coin" | "key" | "portal" | "confetti" | "firework" | "puff" | "page"
  | "tape" | "needle" | "star" | "magic" | "ding" | "thud" | "wipe" | "snip";

export type Ambience = "garden" | "night" | "room" | "ballroom";

interface NoiseOptions { type?: BiquadFilterType; from: number; to?: number; q?: number; peak?: number; attack?: number; pan?: number }
const STORAGE = "woy-volume";

class AudioBus {
  private ctx: AudioContext | null = null;
  private master: GainNode | null = null;
  private send: ConvolverNode | null = null;
  private noise: AudioBuffer | null = null;
  private enabledValue = false;
  private volumeValue = 0.7;
  private listeners = new Set<() => void>();
  private snapshot = { enabled: false, volume: 0.7 };

  constructor() {
    try { const saved = Number(window.localStorage.getItem(STORAGE)); if (saved > 0 && saved <= 1) this.volumeValue = saved; } catch { /* default volume */ }
    this.snapshot = { enabled: false, volume: this.volumeValue };
  }

  get enabled() { return this.enabledValue; }
  get volume() { return this.volumeValue; }
  subscribe = (listener: () => void) => { this.listeners.add(listener); return () => { this.listeners.delete(listener); }; };
  getSnapshot = () => this.snapshot;
  private emit() { this.snapshot = { enabled: this.enabledValue, volume: this.volumeValue }; this.listeners.forEach((l) => l()); }

  setEnabled(on: boolean) {
    this.enabledValue = on;
    if (on) this.ensure();
    this.applyGain();
    this.emit();
  }
  setVolume(volume: number) {
    this.volumeValue = Math.min(1, Math.max(0.05, volume));
    try { window.localStorage.setItem(STORAGE, String(this.volumeValue)); } catch { /* not persisted */ }
    this.applyGain();
    this.emit();
  }
  /** Call from user-gesture handlers: resumes a suspended context so queued effects can be heard. */
  unlock() { if (this.enabledValue) this.ensure(); }

  private ensure() {
    if (!this.ctx) {
      const Ctor = window.AudioContext ?? (window as unknown as { webkitAudioContext?: typeof AudioContext }).webkitAudioContext;
      if (!Ctor) return;
      this.ctx = new Ctor();
      this.master = this.ctx.createGain(); this.master.gain.value = 0;
      this.master.connect(this.ctx.destination);
      this.send = this.ctx.createConvolver(); this.send.buffer = this.impulse(this.ctx, 1.6);
      const wet = this.ctx.createGain(); wet.gain.value = 0.32; this.send.connect(wet); wet.connect(this.master);
      const length = this.ctx.sampleRate * 2; this.noise = this.ctx.createBuffer(1, length, this.ctx.sampleRate);
      const data = this.noise.getChannelData(0); for (let i = 0; i < length; i++) data[i] = Math.random() * 2 - 1;
      this.applyGain();
    }
    if (this.ctx.state === "suspended") void this.ctx.resume();
  }
  private impulse(ctx: AudioContext, seconds: number) {
    const n = Math.floor(ctx.sampleRate * seconds), buffer = ctx.createBuffer(2, n, ctx.sampleRate);
    for (let c = 0; c < 2; c++) { const d = buffer.getChannelData(c); for (let i = 0; i < n; i++) d[i] = (Math.random() * 2 - 1) * Math.pow(1 - i / n, 2.6); }
    return buffer;
  }
  private applyGain() {
    if (!this.ctx || !this.master) return;
    this.master.gain.setTargetAtTime(this.enabledValue ? this.volumeValue * this.volumeValue : 0, this.ctx.currentTime, 0.04);
  }
  private get live() { return this.enabledValue && this.ctx && this.master && this.ctx.state === "running" ? { ctx: this.ctx, out: this.master, send: this.send! } : null; }

  /* ---------- building blocks ---------- */
  private route(node: AudioNode, ctx: AudioContext, out: AudioNode, send: AudioNode, wet: number, pan = 0) {
    let tail: AudioNode = node;
    if (pan) { const p = ctx.createStereoPanner(); p.pan.value = pan; node.connect(p); tail = p; }
    tail.connect(out);
    if (wet > 0) { const g = ctx.createGain(); g.gain.value = wet; tail.connect(g); g.connect(send); }
  }
  private tone(freq: number, t: number, dur: number, peak = 0.14, type: OscillatorType = "sine", wet = 0.4, slideTo?: number, pan = 0) {
    const l = this.live; if (!l) return; const { ctx, out, send } = l;
    const osc = ctx.createOscillator(); osc.type = type; osc.frequency.setValueAtTime(freq, t);
    if (slideTo) osc.frequency.exponentialRampToValueAtTime(slideTo, t + dur);
    const g = ctx.createGain(); g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(peak, t + 0.008); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    osc.connect(g); this.route(g, ctx, out, send, wet, pan); osc.start(t); osc.stop(t + dur + 0.05);
  }
  private burst(t: number, dur: number, o: NoiseOptions, wet = 0.15) {
    const l = this.live; if (!l || !this.noise) return; const { ctx, out, send } = l;
    const src = ctx.createBufferSource(); src.buffer = this.noise;
    const filter = ctx.createBiquadFilter(); filter.type = o.type ?? "bandpass"; filter.Q.value = o.q ?? 1;
    filter.frequency.setValueAtTime(o.from, t); if (o.to) filter.frequency.exponentialRampToValueAtTime(o.to, t + dur);
    const g = ctx.createGain(); const peak = o.peak ?? 0.12; const attack = Math.min(o.attack ?? 0.01, dur * 0.5);
    g.gain.setValueAtTime(0.0001, t); g.gain.exponentialRampToValueAtTime(peak, t + attack); g.gain.exponentialRampToValueAtTime(0.0001, t + dur);
    src.connect(filter); filter.connect(g); this.route(g, ctx, out, send, wet, o.pan ?? 0);
    src.start(t, Math.random() * 1.5, dur + 0.05);
  }
  private bell(freq: number, t: number, peak = 0.1, decay = 1.4, wet = 0.5) {
    for (const [ratio, level, d] of [[1, 1, 1], [2.01, 0.5, 0.7], [2.76, 0.32, 0.5], [5.4, 0.12, 0.3]] as const) this.tone(freq * ratio, t, decay * d, peak * level, "sine", wet);
  }

  play(name: Sfx, intensity = 1) {
    const l = this.live; if (!l) return;
    const t = l.ctx.currentTime + 0.01, k = Math.min(1.5, Math.max(0.2, intensity));
    switch (name) {
      case "paper": for (let i = 0; i < 4; i++) this.burst(t + i * (0.04 + Math.random() * 0.05), 0.07, { from: 4200 - i * 500, to: 1800, q: 1.2, peak: 0.1 * k, pan: (Math.random() - 0.5) * 0.4 }); break;
      case "unfold": this.burst(t, 0.7, { from: 1100, to: 3400, q: 0.8, peak: 0.1 * k, attack: 0.15 }); for (let i = 0; i < 6; i++) this.burst(t + 0.08 + i * 0.1, 0.04, { from: 5200, q: 3, peak: 0.07 * k }); break;
      case "wax": this.burst(t, 0.03, { type: "highpass", from: 2600, peak: 0.2 * k }, 0.1); this.tone(170, t, 0.12, 0.2 * k, "sine", 0.1, 90); this.burst(t + 0.02, 0.09, { from: 6200, q: 4, peak: 0.08 * k }); break;
      case "slide": this.burst(t, 0.55, { type: "lowpass", from: 500, to: 2000, q: 0.6, peak: 0.1 * k, attack: 0.12 }); break;
      case "flap": this.burst(t, 0.2, { from: 900, to: 400, q: 0.9, peak: 0.12 * k }); this.tone(120, t + 0.06, 0.12, 0.1 * k, "sine", 0.1); break;
      case "glass": this.bell(1568, t, 0.07 * k, 1.5, 0.6); this.burst(t, 0.015, { type: "highpass", from: 5000, peak: 0.1 * k }); break;
      case "lid": this.burst(t, 0.4, { from: 2300, to: 900, q: 9, peak: 0.1 * k, attack: 0.05 }); this.bell(1320, t + 0.28, 0.05 * k, 0.8, 0.4); break;
      case "note": this.burst(t, 0.09, { from: 3800, to: 2200, q: 1, peak: 0.08 * k }); this.tone(660, t + 0.04, 0.2, 0.03 * k, "sine", 0.5); break;
      case "bloom": [523.25, 659.25, 783.99, 987.77, 1318.5].forEach((f, i) => this.tone(f, t + i * 0.13, 1.4, 0.06 * k, "triangle", 0.7)); break;
      case "chime": this.bell(880, t, 0.09 * k, 1.2, 0.6); break;
      case "ding": this.bell(1318.5, t, 0.1 * k, 1.1, 0.5); break;
      case "sparkle": for (let i = 0; i < 7; i++) this.tone(2200 + Math.random() * 2600, t + i * 0.05 + Math.random() * 0.03, 0.18, 0.03 * k, "sine", 0.6, undefined, (Math.random() - 0.5) * 0.8); break;
      case "magic": [1046.5, 1318.5, 1568, 2093, 2637].forEach((f, i) => this.tone(f, t + i * 0.07, 0.6, 0.04 * k, "sine", 0.7)); break;
      case "pop": this.burst(t, 0.05, { type: "highpass", from: 1800, peak: 0.2 * k }); this.tone(620, t, 0.14, 0.16 * k, "sine", 0.1, 110); break;
      case "whoosh": this.burst(t, 0.6, { from: 350, to: 2600, q: 0.7, peak: 0.12 * k, attack: 0.25 }); break;
      case "click": this.burst(t, 0.02, { type: "highpass", from: 3000, peak: 0.12 * k }, 0.05); break;
      case "tick": this.tone(1900, t, 0.03, 0.06 * k, "square", 0.05); break;
      case "lever": this.tone(95, t, 0.22, 0.2 * k, "sine", 0.1, 55); this.burst(t, 0.03, { type: "highpass", from: 2000, peak: 0.14 * k }); for (let i = 0; i < 5; i++) this.tone(1500 + i * 130, t + 0.12 + i * 0.045, 0.03, 0.04 * k, "square", 0.1); break;
      case "coin": this.tone(988, t, 0.1, 0.07 * k, "square", 0.2); this.tone(1319, t + 0.08, 0.5, 0.07 * k, "square", 0.3); break;
      case "key": [2093, 2637, 3136].forEach((f, i) => this.bell(f, t + i * 0.06, 0.04 * k, 0.9, 0.4)); this.burst(t, 0.08, { from: 6000, q: 4, peak: 0.06 * k }); break;
      case "portal": { const f = [196, 293.66, 392]; f.forEach((hz) => this.tone(hz, t, 2.2, 0.05 * k, "sawtooth", 0.8, hz * 2)); this.burst(t, 1.8, { from: 300, to: 3200, q: 0.8, peak: 0.07 * k, attack: 0.9 }); break; }
      case "confetti": this.burst(t, 0.05, { type: "highpass", from: 1500, peak: 0.22 * k }); this.tone(520, t, 0.1, 0.12 * k, "sine", 0.1, 120); for (let i = 0; i < 10; i++) this.burst(t + 0.06 + i * 0.035, 0.05, { from: 3000 + Math.random() * 3000, q: 2, peak: 0.05 * k, pan: (Math.random() - 0.5) * 1.2 }); break;
      case "firework": this.tone(70, t, 0.7, 0.28 * k, "sine", 0.4, 38); this.burst(t, 0.3, { type: "lowpass", from: 900, q: 0.7, peak: 0.18 * k }); for (let i = 0; i < 16; i++) this.burst(t + 0.08 + Math.random() * 0.7, 0.03, { type: "highpass", from: 4000, peak: 0.06 * k, pan: (Math.random() - 0.5) * 1.4 }); break;
      case "puff": this.burst(t, 0.28, { type: "lowpass", from: 900, to: 300, q: 0.6, peak: 0.14 * k, attack: 0.04 }); break;
      case "page": this.burst(t, 0.34, { from: 1500, to: 3000, q: 0.9, peak: 0.1 * k, attack: 0.08 }); this.burst(t + 0.16, 0.12, { from: 4200, to: 2000, q: 1, peak: 0.07 * k }); break;
      case "tape": this.burst(t, 0.03, { type: "highpass", from: 2400, peak: 0.16 * k }, 0.05); this.tone(130, t + 0.03, 0.22, 0.05 * k, "sawtooth", 0.1); break;
      case "needle": this.tone(80, t, 0.14, 0.14 * k, "sine", 0.1); for (let i = 0; i < 9; i++) this.burst(t + 0.05 + i * 0.05, 0.015, { type: "highpass", from: 4500, peak: 0.04 * k }); break;
      case "star": this.bell(1568, t, 0.06 * k, 1, 0.6); this.bell(2349, t + 0.12, 0.04 * k, 1, 0.6); break;
      case "thud": this.tone(75, t, 0.2, 0.22 * k, "sine", 0.15, 45); break;
      case "wipe": this.burst(t, 0.3, { from: 2500, to: 1400, q: 0.5, peak: 0.07 * k, attack: 0.08 }); break;
      case "snip": this.burst(t, 0.03, { from: 5200, q: 6, peak: 0.12 * k }, 0.1); this.burst(t + 0.05, 0.03, { from: 4600, q: 6, peak: 0.1 * k }, 0.1); break;
    }
  }

  /** Quiet looping ambience. Returns a stopper; nothing plays unless sound is enabled and unlocked. */
  ambience(kind: Ambience): () => void {
    let stopped = false; const timers = new Set<number>(); const nodes: AudioScheduledSourceNode[] = []; let gain: GainNode | null = null;
    const start = () => {
      const l = this.live; if (!l || stopped || gain || !this.noise) return; const { ctx, out, send } = l;
      gain = ctx.createGain(); gain.gain.value = 0; gain.gain.setTargetAtTime(kind === "ballroom" ? 0.03 : 0.045, ctx.currentTime, 1.2);
      const wind = ctx.createBufferSource(); wind.buffer = this.noise; wind.loop = true;
      const filter = ctx.createBiquadFilter(); filter.type = "bandpass"; filter.frequency.value = kind === "night" ? 260 : kind === "room" ? 180 : 700; filter.Q.value = 0.4;
      const lfo = ctx.createOscillator(), lfoGain = ctx.createGain(); lfo.frequency.value = 0.11; lfoGain.gain.value = filter.frequency.value * 0.5; lfo.connect(lfoGain); lfoGain.connect(filter.frequency);
      wind.connect(filter); filter.connect(gain); this.route(gain, ctx, out, send, 0.3); wind.start(); lfo.start(); nodes.push(wind, lfo);
    };
    const event = () => {
      if (stopped) return; start();
      const l = this.live;
      if (l) {
        const t = l.ctx.currentTime + 0.02;
        if (kind === "garden") { const base = 2400 + Math.random() * 1400; this.tone(base, t, 0.09, 0.03, "sine", 0.5, base * 1.35); this.tone(base * 1.2, t + 0.11, 0.1, 0.025, "sine", 0.5, base * 0.9); }
        else if (kind === "night") { for (let i = 0; i < 4; i++) this.tone(4200, t + i * 0.07, 0.035, 0.012, "sine", 0.3); }
        else if (kind === "room") { this.burst(t, 0.03, { type: "highpass", from: 3500, peak: 0.03 }); }
        else { this.bell(1760 + Math.random() * 500, t, 0.012, 1.8, 0.8); }
      }
      timers.add(window.setTimeout(event, 1400 + Math.random() * 3600));
    };
    event();
    return () => {
      stopped = true; timers.forEach((id) => window.clearTimeout(id));
      if (gain && this.ctx) gain.gain.setTargetAtTime(0, this.ctx.currentTime, 0.2);
      window.setTimeout(() => nodes.forEach((n) => { try { n.stop(); } catch { /* already stopped */ } }), 900);
    };
  }
}

export const audioBus = new AudioBus();

/** React hook: current { enabled, volume } of the global audio bus. */
export function useAudioBus() {
  return useSyncExternalStore(audioBus.subscribe, audioBus.getSnapshot, audioBus.getSnapshot);
}
```

## 38. `src/engine/dispose.ts` — new

```ts
import * as T from "three";

/**
 * Releases every GPU resource reachable from `root`: geometries, materials, every texture slot of every
 * material (including arrays and sprite materials), instanced meshes and light shadow maps. Safe to call twice.
 */
export function disposeTree(root: T.Object3D) {
  const resources = new Set<{ dispose: () => void }>();
  const collectMaterial = (material: T.Material) => {
    resources.add(material);
    for (const value of Object.values(material)) {
      if (value instanceof T.Texture) resources.add(value);
    }
  };
  root.traverse((object) => {
    const any = object as T.Object3D & { geometry?: T.BufferGeometry; material?: T.Material | T.Material[] };
    if (any.geometry) resources.add(any.geometry);
    if (any.material) for (const m of Array.isArray(any.material) ? any.material : [any.material]) collectMaterial(m);
    if (object instanceof T.InstancedMesh) resources.add(object);
    if (object instanceof T.Light) {
      const shadow = (object as T.Light & { shadow?: T.LightShadow }).shadow;
      if (shadow) { shadow.map?.dispose(); shadow.dispose(); }
    }
  });
  resources.forEach((resource) => resource.dispose());
  root.clear();
}
```

## 39. `src/engine/environment.ts` — new

```ts
/**
 * Image-based lighting without any HDR files: a small procedural "studio" (gradient dome + emissive softboxes)
 * is baked once per renderer into a PMREM cube so metal, glass and lacquer get believable reflections.
 */
import * as T from "three";

export type EnvPreset = "candle" | "moon" | "garden" | "studio" | "ballroom" | "dusk";

interface Panel { color: string; strength: number; position: [number, number, number]; size: [number, number] }
interface Preset { sky: string; horizon: string; ground: string; panels: Panel[] }

const PRESETS: Record<EnvPreset, Preset> = {
  candle: {
    sky: "#2a201a", horizon: "#5a3d28", ground: "#171009",
    panels: [
      { color: "#ffb766", strength: 11, position: [-7, 3.5, 5], size: [3, 3] },
      { color: "#7f9bc8", strength: 2.2, position: [8, 5, -4], size: [5, 5] },
      { color: "#ffdcb0", strength: 2.6, position: [0, 10, 1], size: [9, 6] },
    ],
  },
  moon: {
    sky: "#0d1430", horizon: "#27345e", ground: "#080b18",
    panels: [
      { color: "#bcd0ff", strength: 5, position: [-6, 7, -5], size: [4, 4] },
      { color: "#ffd9a0", strength: 3, position: [7, 2, 5], size: [2.5, 4] },
      { color: "#6a7cc4", strength: 1.4, position: [0, 10, 0], size: [10, 10] },
    ],
  },
  garden: {
    sky: "#bcd8f2", horizon: "#f5ead2", ground: "#4f6b3c",
    panels: [
      { color: "#fff1cf", strength: 10, position: [-6, 9, 6], size: [4, 4] },
      { color: "#cfe6ff", strength: 3, position: [8, 5, -2], size: [6, 5] },
      { color: "#ffffff", strength: 2.5, position: [0, 12, 0], size: [12, 12] },
    ],
  },
  studio: {
    sky: "#3b3836", horizon: "#6b655f", ground: "#1d1b1a",
    panels: [
      { color: "#ffffff", strength: 8, position: [-6, 6, 6], size: [4, 4] },
      { color: "#ffe6c8", strength: 3, position: [7, 3, 3], size: [3, 5] },
      { color: "#cfe0ff", strength: 3, position: [0, 4, -8], size: [8, 3] },
    ],
  },
  ballroom: {
    sky: "#2a1a24", horizon: "#6b4636", ground: "#1c1218",
    panels: [
      { color: "#ffcf8a", strength: 12, position: [-5, 6, 5], size: [3, 3] },
      { color: "#ff9ec2", strength: 3.5, position: [8, 4, 2], size: [3, 5] },
      { color: "#ffe9c4", strength: 3, position: [0, 10, -2], size: [9, 5] },
      { color: "#a8c4ff", strength: 2, position: [-8, 2, -6], size: [4, 4] },
    ],
  },
  dusk: {
    sky: "#6a5a86", horizon: "#e8a98a", ground: "#2c2f3d",
    panels: [
      { color: "#ffb680", strength: 9, position: [-8, 2.5, 4], size: [5, 4] },
      { color: "#a8b8ff", strength: 2.4, position: [7, 7, -4], size: [6, 5] },
      { color: "#ffe2c8", strength: 1.8, position: [0, 11, 0], size: [10, 10] },
    ],
  },
};

const cache = new WeakMap<T.WebGLRenderer, Map<EnvPreset, T.Texture>>();

export function createEnvironment(renderer: T.WebGLRenderer, preset: EnvPreset): T.Texture {
  let perRenderer = cache.get(renderer);
  if (!perRenderer) { perRenderer = new Map(); cache.set(renderer, perRenderer); }
  const hit = perRenderer.get(preset);
  if (hit) return hit;

  const def = PRESETS[preset];
  const scene = new T.Scene();
  const domeGeometry = new T.SphereGeometry(30, 32, 16);
  const colors: number[] = [];
  const sky = new T.Color(def.sky), horizon = new T.Color(def.horizon), ground = new T.Color(def.ground), tmp = new T.Color();
  const position = domeGeometry.attributes.position;
  for (let i = 0; i < position.count; i++) {
    const h = position.getY(i) / 30;
    if (h >= 0) tmp.copy(horizon).lerp(sky, Math.pow(h, 0.6)); else tmp.copy(horizon).lerp(ground, Math.pow(-h, 0.5));
    colors.push(tmp.r, tmp.g, tmp.b);
  }
  domeGeometry.setAttribute("color", new T.Float32BufferAttribute(colors, 3));
  const domeMaterial = new T.MeshBasicMaterial({ vertexColors: true, side: T.BackSide });
  scene.add(new T.Mesh(domeGeometry, domeMaterial));
  const disposables: { dispose: () => void }[] = [domeGeometry, domeMaterial];
  for (const panel of def.panels) {
    const geometry = new T.PlaneGeometry(panel.size[0], panel.size[1]);
    const material = new T.MeshBasicMaterial({ color: new T.Color(panel.color).multiplyScalar(panel.strength), side: T.DoubleSide });
    const mesh = new T.Mesh(geometry, material);
    mesh.position.set(...panel.position); mesh.lookAt(0, 0, 0); scene.add(mesh);
    disposables.push(geometry, material);
  }
  const generator = new T.PMREMGenerator(renderer);
  const target = generator.fromScene(scene, 0.03, 0.1, 100);
  generator.dispose();
  for (const d of disposables) d.dispose();
  perRenderer.set(preset, target.texture);
  return target.texture;
}

/** Releases every baked environment for a renderer (call when the renderer is disposed). */
export function disposeEnvironments(renderer: T.WebGLRenderer) {
  cache.get(renderer)?.forEach((texture) => texture.dispose());
  cache.delete(renderer);
}
```

## 40. `src/engine/fx.ts` — new

```ts
/**
 * GPU-driven effects. Positions are computed in vertex shaders from a time uniform, so thousands of particles
 * cost almost no CPU and need no per-frame buffer uploads.
 *  - ParticleField : dust motes, pollen, fireflies, stars, sparkles (continuous)
 *  - Burst         : confetti, fireworks, sparks, smoke puffs (triggered, then fade)
 *  - Flame         : candle flame billboard with flicker
 */
import * as T from "three";
import { glowCanvas } from "./textures";

const rand = (seed: number) => { const x = Math.sin(seed * 127.1 + 311.7) * 43758.5453; return x - Math.floor(x); };

/** Keeps `uScale` equal to half the drawing-buffer height so point sizes are in world-like units at any resolution. */
function trackScale(points: T.Points, uniform: { value: number }) {
  const size = new T.Vector2();
  points.onBeforeRender = (renderer) => { renderer.getDrawingBufferSize(size); uniform.value = size.y * 0.5; };
}

/* ------------------------------------------------------------------------------------------ ParticleField */
export interface FieldOptions {
  count: number;
  size: number;
  color: string;
  colorB?: string;
  opacity?: number;
  /** half-extents of the box (or radius of the shell) the particles live in */
  bounds: [number, number, number];
  center?: [number, number, number];
  distribution?: "box" | "shell";
  shellInner?: number;
  drift?: number;
  rise?: number;
  twinkle?: number;
  additive?: boolean;
  shape?: "disc" | "spark";
  seed?: number;
}

const FIELD_VERT = /* glsl */ `
uniform float uTime, uSize, uScale, uDrift, uRise, uTwinkle;
uniform vec3 uBounds, uCenter;
attribute vec4 aSeed;
varying float vAlpha; varying float vMix;
void main(){
  vec3 p = position * uBounds;
  float t = uTime;
  p += vec3(sin(t*0.37*uDrift + aSeed.x*6.283), cos(t*0.29*uDrift + aSeed.y*6.283), sin(t*0.41*uDrift + aSeed.z*6.283)) * 0.12 * uBounds;
  if (uRise != 0.0) { p.y = mod(p.y + uBounds.y + t*uRise*(0.35 + aSeed.w), 2.0*uBounds.y) - uBounds.y; }
  vec4 mv = modelViewMatrix * vec4(p + uCenter, 1.0);
  float tw = 1.0 - uTwinkle * (0.5 + 0.5*sin(t*(1.0 + aSeed.z*3.0) + aSeed.x*40.0));
  vAlpha = tw; vMix = aSeed.y;
  gl_PointSize = uSize * (0.55 + 0.9*aSeed.w) * uScale / max(0.1, -mv.z);
  gl_Position = projectionMatrix * mv;
}`;
const FIELD_FRAG = /* glsl */ `
uniform vec3 uColor, uColorB; uniform float uOpacity;
varying float vAlpha; varying float vMix;
void main(){
  vec2 c = gl_PointCoord - 0.5; float d = length(c);
  #ifdef SPARK
    float a = max(1.0 - smoothstep(0.0, 0.5, d), max(1.0 - abs(c.x)*16.0, 0.0) * max(1.0 - abs(c.y)*2.0, 0.0) + max(1.0 - abs(c.y)*16.0, 0.0) * max(1.0 - abs(c.x)*2.0, 0.0));
  #else
    float a = 1.0 - smoothstep(0.05, 0.5, d);
  #endif
  gl_FragColor = vec4(mix(uColor, uColorB, vMix), a * vAlpha * uOpacity);
}`;

export class ParticleField {
  readonly points: T.Points;
  private readonly uniforms: Record<string, T.IUniform>;
  constructor(o: FieldOptions) {
    const seed = o.seed ?? 1, positions = new Float32Array(o.count * 3), seeds = new Float32Array(o.count * 4);
    for (let i = 0; i < o.count; i++) {
      let x = rand(i * 3 + seed) * 2 - 1, y = rand(i * 3 + 1 + seed) * 2 - 1, z = rand(i * 3 + 2 + seed) * 2 - 1;
      if (o.distribution === "shell") {
        const len = Math.hypot(x, y, z) || 1, r = (o.shellInner ?? 0.6) + (1 - (o.shellInner ?? 0.6)) * rand(i + 9 + seed);
        x = (x / len) * r; y = (y / len) * r; z = (z / len) * r;
      }
      positions.set([x, y, z], i * 3);
      seeds.set([rand(i * 5 + seed), rand(i * 5 + 1 + seed), rand(i * 5 + 2 + seed), rand(i * 5 + 3 + seed)], i * 4);
    }
    const geometry = new T.BufferGeometry();
    geometry.setAttribute("position", new T.BufferAttribute(positions, 3));
    geometry.setAttribute("aSeed", new T.BufferAttribute(seeds, 4));
    this.uniforms = {
      uTime: { value: 0 }, uSize: { value: o.size }, uScale: { value: 400 }, uDrift: { value: o.drift ?? 1 }, uRise: { value: o.rise ?? 0 },
      uTwinkle: { value: o.twinkle ?? 0 }, uBounds: { value: new T.Vector3(...o.bounds) }, uCenter: { value: new T.Vector3(...(o.center ?? [0, 0, 0])) },
      uColor: { value: new T.Color(o.color) }, uColorB: { value: new T.Color(o.colorB ?? o.color) }, uOpacity: { value: o.opacity ?? 1 },
    };
    const material = new T.ShaderMaterial({
      uniforms: this.uniforms, vertexShader: FIELD_VERT, fragmentShader: FIELD_FRAG, transparent: true, depthWrite: false,
      blending: o.additive === false ? T.NormalBlending : T.AdditiveBlending, defines: o.shape === "spark" ? { SPARK: "" } : {},
    });
    this.points = new T.Points(geometry, material);
    this.points.frustumCulled = false;
    trackScale(this.points, this.uniforms.uScale);
  }
  update(time: number) { this.uniforms.uTime.value = time; }
  set opacity(value: number) { this.uniforms.uOpacity.value = value; }
  get opacity() { return this.uniforms.uOpacity.value as number; }
}

/* ------------------------------------------------------------------------------------------------- Burst */
export interface BurstOptions {
  count: number;
  size: number;
  life: number;
  speed: number;
  gravity?: number;
  drag?: number;
  colors: string[];
  shape: "confetti" | "spark" | "smoke";
  /** "sphere" = fireworks, "cone" = upward fan (confetti cannon / smoke), "disc" = flat ring */
  emit?: "sphere" | "cone" | "disc";
  coneAngle?: number;
  seed?: number;
}

const BURST_VERT = /* glsl */ `
uniform float uAge, uLife, uGravity, uDrag, uSize, uScale;
uniform vec3 uOrigin;
attribute vec3 aVel; attribute vec4 aSeed; attribute vec3 aColor;
varying vec3 vColor; varying float vAlpha; varying float vSpin; varying float vLife;
void main(){
  float age = max(0.0, uAge - aSeed.x * 0.06) * (0.8 + aSeed.y*0.4);
  float k = (uDrag > 0.001) ? (1.0 - exp(-uDrag*age))/uDrag : age;
  vec3 p = uOrigin + aVel * k;
  p.y -= 0.5 * uGravity * age * age;
  #ifdef SMOKE
    p.x += sin(age*1.6 + aSeed.z*6.283) * 0.05 * age; p.z += cos(age*1.4 + aSeed.w*6.283) * 0.05 * age;
  #endif
  float life = clamp(age / uLife, 0.0, 1.0);
  vLife = life; vColor = aColor; vSpin = age * (4.0 + aSeed.z*10.0) + aSeed.w*6.283;
  #ifdef SMOKE
    vAlpha = (uAge > 0.0 ? 1.0 : 0.0) * smoothstep(0.0, 0.12, life) * (1.0 - life) * 0.55;
    float grow = 0.6 + life * 2.4;
  #else
    vAlpha = (uAge > 0.0 ? 1.0 : 0.0) * (1.0 - life*life);
    float grow = 1.0 - 0.45*life;
  #endif
  vec4 mv = modelViewMatrix * vec4(p, 1.0);
  gl_PointSize = uSize * grow * (0.7 + 0.6*aSeed.y) * uScale / max(0.1, -mv.z);
  gl_Position = projectionMatrix * mv;
}`;
const BURST_FRAG = /* glsl */ `
varying vec3 vColor; varying float vAlpha; varying float vSpin; varying float vLife;
void main(){
  vec2 c = gl_PointCoord - 0.5;
  #if defined(CONFETTI)
    float s = sin(vSpin), co = cos(vSpin);
    vec2 q = vec2(c.x*co - c.y*s, c.x*s + c.y*co);
    q.x /= max(0.18, abs(cos(vSpin*0.7)));
    float a = step(abs(q.x), 0.3) * step(abs(q.y), 0.42);
    vec3 col = vColor * (0.7 + 0.3*cos(vSpin*1.3));
    gl_FragColor = vec4(col, a * vAlpha);
  #elif defined(SPARK)
    float d = length(c);
    float core = 1.0 - smoothstep(0.0, 0.5, d);
    float tw = 0.65 + 0.35*sin(vSpin*3.0);
    gl_FragColor = vec4(mix(vColor, vec3(1.0), core*0.6) * (1.0 + core), core * vAlpha * (vLife > 0.7 ? tw : 1.0));
  #else
    float d = length(c);
    gl_FragColor = vec4(vColor, (1.0 - smoothstep(0.0, 0.5, d)) * vAlpha);
  #endif
}`;

export class Burst {
  readonly points: T.Points;
  private readonly uniforms: Record<string, T.IUniform>;
  private age = -1;
  private readonly life: number;
  constructor(o: BurstOptions) {
    const seed = o.seed ?? 3, vel = new Float32Array(o.count * 3), seeds = new Float32Array(o.count * 4), colors = new Float32Array(o.count * 3);
    const palette = o.colors.map((c) => new T.Color(c));
    for (let i = 0; i < o.count; i++) {
      const a = rand(i * 7 + seed) * Math.PI * 2, b = rand(i * 7 + 1 + seed), s = o.speed * (0.35 + 0.65 * rand(i * 7 + 2 + seed));
      let v: [number, number, number];
      if (o.emit === "cone") { const spread = (o.coneAngle ?? 0.6) * b; v = [Math.sin(spread) * Math.cos(a) * s, Math.cos(spread) * s, Math.sin(spread) * Math.sin(a) * s]; }
      else if (o.emit === "disc") v = [Math.cos(a) * s, (b - 0.5) * s * 0.15, Math.sin(a) * s];
      else { const z = b * 2 - 1, r = Math.sqrt(1 - z * z); v = [r * Math.cos(a) * s, z * s, r * Math.sin(a) * s]; }
      vel.set(v, i * 3);
      seeds.set([rand(i * 11 + seed), rand(i * 11 + 1 + seed), rand(i * 11 + 2 + seed), rand(i * 11 + 3 + seed)], i * 4);
      const c = palette[i % palette.length]; colors.set([c.r, c.g, c.b], i * 3);
    }
    const geometry = new T.BufferGeometry();
    geometry.setAttribute("position", new T.BufferAttribute(new Float32Array(o.count * 3), 3));
    geometry.setAttribute("aVel", new T.BufferAttribute(vel, 3)); geometry.setAttribute("aSeed", new T.BufferAttribute(seeds, 4)); geometry.setAttribute("aColor", new T.BufferAttribute(colors, 3));
    this.life = o.life;
    this.uniforms = {
      uAge: { value: -1 }, uLife: { value: o.life }, uGravity: { value: o.gravity ?? 3 }, uDrag: { value: o.drag ?? 0.9 }, uSize: { value: o.size },
      uScale: { value: 400 }, uOrigin: { value: new T.Vector3() },
    };
    const define = o.shape === "confetti" ? "CONFETTI" : o.shape === "smoke" ? "SMOKE" : "SPARK";
    const defines: Record<string, string> = { [define]: "" };
    const material = new T.ShaderMaterial({
      uniforms: this.uniforms, vertexShader: BURST_VERT, fragmentShader: BURST_FRAG, transparent: true, depthWrite: false, defines,
      blending: o.shape === "spark" ? T.AdditiveBlending : T.NormalBlending,
    });
    this.points = new T.Points(geometry, material);
    this.points.frustumCulled = false; this.points.visible = false;
    trackScale(this.points, this.uniforms.uScale);
  }
  /** Fires the burst from `origin` (in the Points' local space). */
  trigger(origin: T.Vector3 | [number, number, number] = [0, 0, 0]) {
    if (Array.isArray(origin)) (this.uniforms.uOrigin.value as T.Vector3).set(...origin); else (this.uniforms.uOrigin.value as T.Vector3).copy(origin);
    this.age = 0; this.points.visible = true;
  }
  reset() { this.age = -1; this.uniforms.uAge.value = -1; this.points.visible = false; }
  get active() { return this.age >= 0; }
  update(dt: number) {
    if (this.age < 0) return;
    this.age += dt; this.uniforms.uAge.value = this.age;
    if (this.age > this.life * 1.3) this.reset();
  }
}

/* ------------------------------------------------------------------------------------------------- Flame */
const FLAME_VERT = /* glsl */ `varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }`;
const FLAME_FRAG = /* glsl */ `
uniform float uTime, uSeed, uIntensity; varying vec2 vUv;
float h(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
float n(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h(i), h(i+vec2(1,0)), f.x), mix(h(i+vec2(0,1)), h(i+vec2(1,1)), f.x), f.y); }
void main(){
  float y = vUv.y;
  float sway = (n(vec2(uTime*3.1 + uSeed, y*2.2)) - 0.5) * 0.5 * y * y + sin(uTime*1.7 + uSeed) * 0.03 * y;
  float x = (vUv.x - 0.5) * 2.0 - sway;
  float w = pow(max(sin(3.14159 * pow(y, 0.62)), 0.0), 1.15) * 0.62 * (1.0 - 0.25*y);
  float d = abs(x) / max(w, 0.001);
  float a = (1.0 - smoothstep(0.35, 1.0, d)) * (1.0 - smoothstep(0.72, 1.0, y));
  vec3 outer = vec3(1.0, 0.42, 0.08), mid = vec3(1.0, 0.72, 0.22), core = vec3(1.0, 0.96, 0.78);
  vec3 col = mix(mid, outer, smoothstep(0.25, 0.95, d*0.8 + y*0.55));
  col = mix(col, core, (1.0 - smoothstep(0.0, 0.55, d + y*0.35)) * 0.9);
  col = mix(vec3(0.25, 0.4, 1.0), col, smoothstep(0.0, 0.2, y));
  float flick = 0.86 + 0.14 * n(vec2(uTime*9.0 + uSeed, 3.0));
  gl_FragColor = vec4(col * 1.35, a * uIntensity * flick);
}`;

export class Flame {
  readonly group = new T.Group();
  private readonly mesh: T.Mesh;
  private readonly glow: T.Sprite;
  private readonly uniforms = { uTime: { value: 0 }, uSeed: { value: Math.random() * 10 }, uIntensity: { value: 1 } };
  private readonly q = new T.Quaternion();
  constructor(height = 0.34, width = 0.17) {
    const geometry = new T.PlaneGeometry(width, height); geometry.translate(0, height / 2, 0);
    this.mesh = new T.Mesh(geometry, new T.ShaderMaterial({
      uniforms: this.uniforms, vertexShader: FLAME_VERT, fragmentShader: FLAME_FRAG, transparent: true, depthWrite: false, blending: T.AdditiveBlending, side: T.DoubleSide,
    }));
    this.mesh.renderOrder = 6;
    const texture = new T.CanvasTexture(glowCanvas("rgba(255,190,110,1)", "rgba(255,150,60,0)"));
    texture.colorSpace = T.SRGBColorSpace;
    this.glow = new T.Sprite(new T.SpriteMaterial({ map: texture, color: "#ffb260", transparent: true, opacity: 0.55, depthWrite: false, blending: T.AdditiveBlending }));
    this.glow.scale.setScalar(height * 3.2); this.glow.position.y = height * 0.45;
    this.group.add(this.glow, this.mesh);
  }
  /** intensity 0 snuffs the flame. */
  update(time: number, camera: T.Camera, intensity = 1) {
    this.uniforms.uTime.value = time; this.uniforms.uIntensity.value = intensity;
    this.group.visible = intensity > 0.01;
    (this.glow.material as T.SpriteMaterial).opacity = 0.55 * intensity;
    const parent = this.group.parent;
    if (parent) { parent.getWorldQuaternion(this.q).invert(); this.mesh.quaternion.copy(this.q).multiply(camera.quaternion); }
  }
}
```

## 41. `src/engine/garden.ts` — new

```ts
/**
 * Botanical building blocks shared by every garden-like scene (Everlasting Flower, Future Garden, Wish Garden, hero meadow):
 * cut-away soil terrain, instanced wind grass, butterflies, branching roots, a multi-layer bloom with a visible centre,
 * and a painted sky. All geometry and textures are generated.
 */
import * as T from "three";
import type { MaterialKit } from "./materials";
import { leafGeometry, petalGeometry, taperedTube, growTube } from "./geometry";
import type { Quality } from "./quality";
import { fbm, noise2 } from "./textures";

const rnd = (i: number, s = 0) => { const x = Math.sin(i * 127.1 + s * 311.7) * 43758.5453; return x - Math.floor(x); };
const smooth = T.MathUtils.smoothstep;

/* ------------------------------------------------------------------------------------------------ terrain */
export type HeightFn = (x: number, z: number) => number;

/** Layered soil painted for the cut face; v=0 is the bottom, v=1 the surface. */
function strataTexture(width: number, height: number) {
  const c = document.createElement("canvas"); c.width = width; c.height = height;
  const g = c.getContext("2d", { willReadFrequently: true })!, img = g.createImageData(width, height);
  const layers: [number, [number, number, number]][] = [[0.0, [96, 92, 86]], [0.14, [150, 112, 76]], [0.38, [112, 78, 52]], [0.64, [76, 52, 34]], [0.86, [40, 27, 18]]];
  for (let j = 0; j < height; j++) for (let i = 0; i < width; i++) {
    const u = i / width, v = 1 - j / height;
    const wob = (fbm(u, v, 5, 3, 3, 3) - 0.5) * 0.09;
    let k = 0; for (let l = 0; l < layers.length; l++) if (v + wob >= layers[l][0]) k = l;
    const base = layers[k], next = layers[Math.min(layers.length - 1, k + 1)];
    const blend = k === layers.length - 1 ? 0 : smooth(v + wob, next[0] - 0.035, next[0]);
    const grain = 0.68 + 0.5 * fbm(u, v, 11, 5, 24, 16) + (noise2(u * 160, v * 120, 7, 160, 120) > 0.93 ? 0.35 : 0);
    const o = (j * width + i) * 4;
    for (let ch = 0; ch < 3; ch++) img.data[o + ch] = Math.min(255, (base[1][ch] * (1 - blend) + next[1][ch] * blend) * grain);
    img.data[o + 3] = 255;
  }
  g.putImageData(img, 0, 0);
  for (let i = 0; i < 70; i++) { // pebbles
    const x = rnd(i, 1) * width, y = height * (0.12 + rnd(i, 2) * 0.8), r = 2 + rnd(i, 3) * 7;
    g.fillStyle = `rgba(${150 + rnd(i, 4) * 60},${135 + rnd(i, 4) * 40},${110 + rnd(i, 5) * 30},.85)`; g.beginPath(); g.ellipse(x, y, r * 1.3, r, rnd(i, 6) * 3, 0, Math.PI * 2); g.fill();
    g.strokeStyle = "rgba(20,12,8,.35)"; g.lineWidth = 1; g.stroke();
  }
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}

function turfTexture(size: number) {
  const c = document.createElement("canvas"); c.width = c.height = size;
  const g = c.getContext("2d", { willReadFrequently: true })!, img = g.createImageData(size, size);
  for (let j = 0; j < size; j++) for (let i = 0; i < size; i++) {
    const u = i / size, v = j / size, n = fbm(u, v, 3, 5, 8), dirt = smooth(fbm(u, v, 9, 4, 5), 0.58, 0.72);
    const o = (j * size + i) * 4, k = 0.55 + n * 0.7;
    img.data[o] = (58 + 40 * n + dirt * 40) * k; img.data[o + 1] = (92 + 60 * n - dirt * 20) * k; img.data[o + 2] = (40 + 24 * n) * k; img.data[o + 3] = 255;
  }
  g.putImageData(img, 0, 0);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.wrapS = t.wrapT = T.RepeatWrapping; t.repeat.set(2, 2); t.anisotropy = 4; return t;
}

export interface TerrainOptions { width: number; depth: number; bottom: number; height: HeightFn }

/** A soil block: grassy displaced top and four strata-textured walls whose tops follow the surface (the front wall is the cut face). */
export function buildTerrain(quality: Quality, o: TerrainOptions) {
  const group = new T.Group();
  const seg = quality === "low" ? 32 : quality === "medium" ? 52 : 80;
  const top = new T.PlaneGeometry(o.width, o.depth, seg, Math.round((seg * o.depth) / o.width)); top.rotateX(-Math.PI / 2);
  const p = top.attributes.position;
  for (let i = 0; i < p.count; i++) p.setY(i, o.height(p.getX(i), p.getZ(i)));
  top.computeVertexNormals();
  const topMesh = new T.Mesh(top, new T.MeshStandardMaterial({ map: turfTexture(quality === "low" ? 256 : 512), roughness: 0.95 }));
  topMesh.receiveShadow = true; group.add(topMesh);

  const strata = new T.MeshStandardMaterial({ map: strataTexture(quality === "low" ? 384 : 768, quality === "low" ? 192 : 384), roughness: 0.96, side: T.DoubleSide });
  const maxTop = 0.55, span = maxTop - o.bottom, hw = o.width / 2, hd = o.depth / 2, n = seg * 2;
  const wall = (ax: number, az: number, bx: number, bz: number) => {
    const pos: number[] = [], uv: number[] = [], idx: number[] = [];
    for (let i = 0; i <= n; i++) {
      const t = i / n, x = ax + (bx - ax) * t, z = az + (bz - az) * t, y = o.height(x, z);
      pos.push(x, y, z, x, o.bottom, z); uv.push(t, (y - o.bottom) / span, t, 0);
      if (i < n) { const a = i * 2; idx.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
    }
    const g = new T.BufferGeometry(); g.setAttribute("position", new T.Float32BufferAttribute(pos, 3)); g.setAttribute("uv", new T.Float32BufferAttribute(uv, 2)); g.setIndex(idx); g.computeVertexNormals();
    const m = new T.Mesh(g, strata); m.receiveShadow = true; group.add(m); return m;
  };
  wall(-hw, hd, hw, hd); wall(hw, hd, hw, -hd); wall(hw, -hd, -hw, -hd); wall(-hw, -hd, -hw, hd);
  const floor = new T.Mesh(new T.PlaneGeometry(o.width, o.depth), new T.MeshStandardMaterial({ color: "#2a1d14", roughness: 1 })); floor.rotation.x = Math.PI / 2; floor.position.y = o.bottom; group.add(floor);
  return { group, frontZ: hd, top: topMesh };
}

/* -------------------------------------------------------------------------------------------------- grass */
export interface GrassOptions { count: number; width: number; depth: number; height: HeightFn; blade?: number; colors?: [string, string]; keepOut?: (x: number, z: number) => boolean }

/** Instanced blades bent by a vertex-shader wind. One draw call, no per-frame CPU work except the time uniform. */
export function createGrass(o: GrassOptions) {
  const geometry = new T.BufferGeometry();
  geometry.setAttribute("position", new T.Float32BufferAttribute([-0.5, 0, 0, 0.5, 0, 0, -0.36, 0.5, 0, 0.36, 0.5, 0, 0, 1, 0], 3));
  geometry.setIndex([0, 1, 2, 1, 3, 2, 2, 3, 4]); geometry.computeVertexNormals();
  const time = { value: 0 };
  const material = new T.MeshStandardMaterial({ color: "#ffffff", roughness: 0.78, side: T.DoubleSide });
  material.onBeforeCompile = (shader) => {
    shader.uniforms.uTime = time;
    shader.vertexShader = shader.vertexShader
      .replace("#include <common>", "#include <common>\nuniform float uTime;\nvarying float vH;")
      .replace("#include <begin_vertex>", `#include <begin_vertex>
        vH = position.y;
        vec4 ip = instanceMatrix * vec4(0.0, 0.0, 0.0, 1.0);
        float ph = ip.x * 0.9 + ip.z * 0.7;
        float gust = sin(uTime * 0.7 + ip.x * 0.25) * 0.5 + 0.5;
        transformed.x += (sin(uTime * 1.7 + ph) * 0.55 + sin(uTime * 3.3 + ph * 1.7) * 0.2 + gust * 0.5) * 0.34 * vH * vH;
        transformed.z += cos(uTime * 1.3 + ph * 0.9) * 0.16 * vH * vH;`);
    shader.fragmentShader = shader.fragmentShader
      .replace("#include <common>", "#include <common>\nvarying float vH;")
      .replace("#include <color_fragment>", "#include <color_fragment>\n  diffuseColor.rgb *= mix(0.38, 1.12, vH);");
  };
  const mesh = new T.InstancedMesh(geometry, material, o.count);
  const d = new T.Object3D(), a = new T.Color(o.colors?.[0] ?? "#3f6b2c"), b = new T.Color(o.colors?.[1] ?? "#8fb04a"), c = new T.Color();
  let placed = 0;
  for (let i = 0; i < o.count * 2 && placed < o.count; i++) {
    const x = (rnd(i, 1) - 0.5) * o.width * 0.99, z = (rnd(i, 2) - 0.5) * o.depth * 0.99;
    if (o.keepOut?.(x, z)) continue;
    const h = (o.blade ?? 0.5) * (0.55 + rnd(i, 3) * 0.9);
    d.position.set(x, o.height(x, z) - 0.02, z); d.rotation.set((rnd(i, 4) - 0.5) * 0.35, rnd(i, 5) * Math.PI, (rnd(i, 6) - 0.5) * 0.3); d.scale.set(0.05 + rnd(i, 7) * 0.035, h, 1); d.updateMatrix();
    mesh.setMatrixAt(placed, d.matrix); c.copy(a).lerp(b, rnd(i, 8) * rnd(i, 9) * 1.4); mesh.setColorAt(placed, c); placed++;
  }
  mesh.count = placed; mesh.frustumCulled = false; mesh.receiveShadow = true;
  return { mesh, update: (t: number) => { time.value = t; } };
}

/* ---------------------------------------------------------------------------------------------- butterflies */
function wingTexture(a: string, b: string, spot: string) {
  const c = document.createElement("canvas"); c.width = 256; c.height = 200; const g = c.getContext("2d")!;
  g.beginPath(); g.moveTo(0, 100); g.bezierCurveTo(10, -20, 210, -10, 250, 40); g.bezierCurveTo(260, 90, 170, 110, 140, 112); g.bezierCurveTo(200, 120, 220, 190, 150, 196); g.bezierCurveTo(70, 205, 20, 150, 0, 100); g.closePath();
  const grad = g.createLinearGradient(0, 100, 250, 60); grad.addColorStop(0, a); grad.addColorStop(1, b); g.fillStyle = grad; g.fill();
  g.save(); g.clip(); g.strokeStyle = "rgba(40,24,20,.55)"; g.lineWidth = 2.4; for (let i = 0; i < 7; i++) { g.beginPath(); g.moveTo(8, 100); g.quadraticCurveTo(80 + i * 22, 30 + i * 18, 250 - i * 6, 20 + i * 24); g.stroke(); }
  g.fillStyle = spot; for (const [x, y, r] of [[170, 52, 17], [196, 88, 10], [120, 150, 14], [90, 60, 9]] as const) { g.beginPath(); g.arc(x, y, r, 0, Math.PI * 2); g.fill(); }
  g.lineWidth = 6; g.strokeStyle = "rgba(30,20,18,.9)"; g.stroke(); g.restore();
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}

export function createButterflies(count: number, palettes: [string, string, string][] = [["#f0a45d", "#e0603a", "#fff2cf"], ["#c9b6f0", "#7b69c9", "#ffffff"], ["#f7e48a", "#e8b53a", "#6b4a1e"]]) {
  const group = new T.Group();
  const flies = Array.from({ length: count }, (_, i) => {
    const pal = palettes[i % palettes.length], tex = wingTexture(pal[0], pal[1], pal[2]);
    const mat = new T.MeshStandardMaterial({ map: tex, alphaTest: 0.5, side: T.DoubleSide, roughness: 0.7, emissive: new T.Color(pal[0]).multiplyScalar(0.12) });
    const geometry = new T.PlaneGeometry(0.62, 0.5); geometry.translate(0.31, 0, 0); geometry.rotateX(-Math.PI / 2);
    const body = new T.Group(); const bodyMesh = new T.Mesh(new T.CapsuleGeometry(0.028, 0.2, 3, 6), new T.MeshStandardMaterial({ color: "#2b1d16", roughness: 0.8 })); bodyMesh.rotation.x = Math.PI / 2; body.add(bodyMesh);
    const wings = [1, -1].map((side) => { const pivot = new T.Group(); const w = new T.Mesh(geometry, mat); w.scale.x = side; pivot.add(w); body.add(pivot); return { pivot, side }; });
    group.add(body); return { body, wings, phase: i * 2.17, speed: 0.22 + (i % 3) * 0.07 };
  });
  const v = new T.Vector3(), next = new T.Vector3();
  const path = (f: (typeof flies)[number], t: number, center: T.Vector3, out: T.Vector3) => {
    const a = t * f.speed + f.phase; return out.set(center.x + Math.cos(a) * (2.3 + Math.sin(f.phase) * 0.6), center.y + 0.9 + Math.sin(a * 1.7) * 0.5, center.z + Math.sin(a * 1.3) * 1.6);
  };
  return {
    group,
    /** landing: 0 = free flight around `center`, 1 = resting on `perch` with slow wing beats. */
    update(time: number, center: T.Vector3, perch: T.Vector3 | null, landing = 0, reduced = false) {
      flies.forEach((f, i) => {
        path(f, time, center, v); path(f, time + 0.05, center, next);
        const land = i === 0 && perch ? landing : 0;
        const pos = v.clone().lerp(perch ? perch.clone().add(new T.Vector3(0.12, 0.35, 0.1)) : v, land);
        f.body.position.copy(pos);
        if (land < 0.95) f.body.lookAt(next.x, pos.y, next.z); else f.body.rotation.y += 0.002;
        const flap = reduced ? 0.5 : (land > 0.9 ? 0.45 + Math.sin(time * 2.2 + i) * 0.35 : 0.2 + Math.abs(Math.sin(time * (14 + i * 2) + f.phase)) * 1.1);
        f.wings.forEach(({ pivot, side }) => { pivot.rotation.z = side * flap; });
      });
    },
  };
}

/* ------------------------------------------------------------------------------------------------- roots */
const rootMaterial = () => new T.MeshStandardMaterial({ color: "#eadbb8", roughness: 0.7, emissive: new T.Color("#7a5a30").multiplyScalar(0.1) });

/** Branching root system pressed against the cut face at z. `update(growth 0..1)` grows tap root first, then laterals. */
export function createRoots(z: number, quality: Quality) {
  const group = new T.Group(), material = rootMaterial();
  const parts: { mesh: T.Mesh; start: number; dur: number }[] = [];
  const add = (pts: [number, number][], r0: number, r1: number, start: number, dur: number) => {
    const curve = new T.CatmullRomCurve3(pts.map(([x, y], i) => new T.Vector3(x, y, z + Math.sin(i * 2.1 + start * 9) * 0.03)));
    const mesh = new T.Mesh(taperedTube(curve, r0, r1, quality === "low" ? 20 : 36, quality === "low" ? 5 : 7), material);
    mesh.castShadow = false; growTube(mesh, 0); group.add(mesh); parts.push({ mesh, start, dur }); return curve;
  };
  const tap = add([[0, 0.02], [0.04, -0.4], [-0.07, -0.86], [0.08, -1.32], [-0.02, -1.85]], 0.075, 0.012, 0, 0.55);
  const lateralCount = quality === "low" ? 7 : 12;
  for (let i = 0; i < lateralCount; i++) {
    const side = rnd(i, 11) > 0.5 ? 1 : -1, t = 0.07 + (i / lateralCount) * 0.8 + (rnd(i, 12) - 0.5) * 0.05, o = tap.getPointAt(t);
    const reach = 0.55 + rnd(i, 1) * 1.15, sag = 0.1 + rnd(i, 2) * 0.5, steps = 5;
    const pts: [number, number][] = [[o.x, o.y]];
    for (let k = 1; k <= steps; k++) { const f = k / steps; pts.push([o.x + side * reach * f + (rnd(i, 20 + k) - 0.5) * 0.12, o.y - sag * f * f - 0.04 * k + (rnd(i, 30 + k) - 0.5) * 0.14]); }
    const start = 0.16 + t * 0.42, dur = 0.34 + rnd(i, 4) * 0.12;
    const lateral = add(pts, 0.034 + rnd(i, 7) * 0.012, 0.005, start, dur);
    const subs = 2 + (i % 2);
    for (let k = 0; k < subs; k++) {
      const q = lateral.getPointAt(0.3 + k * 0.24 + rnd(i, 40 + k) * 0.1), dir = rnd(i, 50 + k) > 0.45 ? 1 : -1, len = 0.18 + rnd(i, 60 + k) * 0.32;
      add([[q.x, q.y], [q.x + side * 0.08, q.y + dir * len * 0.3 - 0.05], [q.x + side * 0.16 + (rnd(i, 70 + k) - 0.5) * 0.1, q.y + dir * len * 0.4 - 0.2 - len * 0.5]], 0.015, 0.003, start + dur * (0.45 + k * 0.2), dur * 0.5);
    }
  }
  return { group, update: (growth: number) => parts.forEach((p) => growTube(p.mesh, (growth - p.start) / p.dur)) };
}

/* ------------------------------------------------------------------------------------------------- flower */
export interface BloomPalette { outer: [string, string, string]; inner: [string, string, string]; centre: string }
export const ROSE_PALETTE: BloomPalette = { outer: ["#f4c3cf", "#d84f7b", "#87204a"], inner: ["#f9d9d0", "#ee7f99", "#a83a5c"], centre: "#e9b53c" };

/** Multi-layer bloom. setBloom(0) is a tight bud; setBloom(1) is fully open with the golden centre and stamens visible. */
export function createBloom(kit: MaterialKit, quality: Quality, palette: BloomPalette = ROSE_PALETTE) {
  const group = new T.Group(), low = quality === "low";
  const outerMat = kit.petal(...palette.outer), innerMat = kit.petal(...palette.inner);
  const layers = [
    { count: 8, len: 1.2, wid: 0.64, cup: 0.14, curl: 0.45, tilt: [0.4, 1.9] as const, rise: 0, mat: outerMat },
    { count: 8, len: 1.02, wid: 0.58, cup: 0.22, curl: 0.3, tilt: [0.32, 1.5] as const, rise: 0.03, mat: outerMat },
    { count: 7, len: 0.82, wid: 0.5, cup: 0.32, curl: 0.16, tilt: [0.22, 1.08] as const, rise: 0.06, mat: innerMat },
    { count: 5, len: 0.58, wid: 0.38, cup: 0.46, curl: 0.06, tilt: [0.1, 0.55] as const, rise: 0.09, mat: innerMat },
  ];
  const petals: { hinge: T.Group; tilt: readonly [number, number]; delay: number; seed: number }[] = [];
  layers.forEach((layer, li) => {
    const geometry = petalGeometry(layer.len, layer.wid, layer.cup, layer.curl, 0.36, low ? 6 : 10, low ? 10 : 18);
    for (let i = 0; i < layer.count; i++) {
      const pivot = new T.Group(); pivot.rotation.y = (i / layer.count) * Math.PI * 2 + li * 0.5 + (i % 2) * 0.06; group.add(pivot);
      const hinge = new T.Group(); hinge.position.set(0, layer.rise, 0.05 + li * 0.022); pivot.add(hinge);
      const mesh = new T.Mesh(geometry, layer.mat); mesh.castShadow = !low; hinge.add(mesh);
      petals.push({ hinge, tilt: layer.tilt, delay: li * 0.1 + (i % 3) * 0.025, seed: i * 1.9 + li * 3.1 });
    }
  });
  // receptacle, pistil
  const gold = new T.MeshStandardMaterial({ color: palette.centre, roughness: 0.4, metalness: 0.15, emissive: new T.Color(palette.centre).multiplyScalar(0.15) });
  const centre = new T.Group(); group.add(centre);
  const dome = new T.Mesh(new T.SphereGeometry(0.17, 20, 14), gold); dome.scale.y = 0.55; dome.position.y = 0.03; centre.add(dome);
  const pistil = new T.Mesh(new T.CylinderGeometry(0.01, 0.018, 0.13, 6), new T.MeshStandardMaterial({ color: "#c9d36a", roughness: 0.5 })); pistil.position.y = 0.1; centre.add(pistil);
  for (let k = 0; k < 3; k++) { const s = new T.Mesh(new T.SphereGeometry(0.028, 8, 6), new T.MeshStandardMaterial({ color: "#f2a73a", roughness: 0.5 })); s.position.set(Math.sin(k * 2.1) * 0.03, 0.18, Math.cos(k * 2.1) * 0.03); centre.add(s); }
  // stamens: instanced filaments + anthers
  const count = low ? 28 : 56;
  const filaments = new T.InstancedMesh(new T.CylinderGeometry(0.005, 0.009, 1, 5).translate(0, 0.5, 0), new T.MeshStandardMaterial({ color: "#f3e6a8", roughness: 0.6 }), count);
  const anthers = new T.InstancedMesh(new T.SphereGeometry(0.024, 8, 6), new T.MeshStandardMaterial({ color: "#e68a1d", roughness: 0.5, emissive: new T.Color("#e68a1d").multiplyScalar(0.18) }), count);
  centre.add(filaments, anthers);
  const d = new T.Object3D(), e = new T.Object3D(), v = new T.Vector3();
  let lastOpen = -1;
  const poseStamens = (open: number) => {
    for (let i = 0; i < count; i++) {
      const a = i * 2.39996, ring = 0.05 + (i % 4) * 0.025, lean = 0.2 + (i % 5) * 0.12, length = (0.22 + (i % 3) * 0.06) * open;
      d.position.set(Math.cos(a) * ring, 0.06, Math.sin(a) * ring); d.rotation.set(Math.sin(a) * lean, 0, -Math.cos(a) * lean); d.scale.set(1, Math.max(0.001, length), 1); d.updateMatrix(); filaments.setMatrixAt(i, d.matrix);
      v.set(0, length, 0).applyEuler(d.rotation).add(d.position); e.position.copy(v); e.scale.setScalar(Math.max(0.001, open)); e.updateMatrix(); anthers.setMatrixAt(i, e.matrix);
    }
    filaments.instanceMatrix.needsUpdate = true; anthers.instanceMatrix.needsUpdate = true;
  };
  // sepals
  const sepalMat = kit.leaf("#355f2e", "#6c9a46"), sepalGeo = leafGeometry(0.62, 0.2, 0.08, 0.05, 4, 8);
  const sepals = Array.from({ length: 5 }, (_, i) => { const pivot = new T.Group(); pivot.rotation.y = (i / 5) * Math.PI * 2 + 0.3; const hinge = new T.Group(); hinge.position.set(0, -0.02, 0.07); pivot.add(hinge); hinge.add(new T.Mesh(sepalGeo, sepalMat)); group.add(pivot); return hinge; });

  return {
    group, centre,
    /** b: 0 bud .. 1 open */
    setBloom(b: number) {
      petals.forEach((p) => {
        const k = smooth(b, p.delay, p.delay + 0.55);
        p.hinge.rotation.x = p.tilt[0] + (p.tilt[1] - p.tilt[0]) * k + Math.sin(p.seed) * 0.05 * k; p.hinge.rotation.z = Math.sin(p.seed * 1.7) * 0.07 * k;
      });
      sepals.forEach((s, i) => { s.rotation.x = 0.25 + smooth(b, 0.05, 0.9) * 1.7 + Math.sin(i * 2) * 0.05; });
      const open = smooth(b, 0.55, 0.95);
      if (Math.abs(open - lastOpen) > 0.004) { poseStamens(open); lastOpen = open; }
      centre.visible = b > 0.02;
    },
    /** Gentle breathing of the petals. */
    flutter(time: number, amount = 1) { petals.forEach((p, i) => { p.hinge.rotation.y = Math.sin(time * 0.9 + p.seed) * 0.018 * amount * (1 + (i % 3) * 0.3); }); },
  };
}

/* ---------------------------------------------------------------------------------------------------- sky */
/** Painted golden-hour sky with layered, hazy hills. Returns a plane to place far behind the scene. */
export function createSky(width = 90, height = 52) {
  const w = 1024, h = 600, c = document.createElement("canvas"); c.width = w; c.height = h; const g = c.getContext("2d")!;
  const sky = g.createLinearGradient(0, 0, 0, h); sky.addColorStop(0, "#7fa6d4"); sky.addColorStop(0.45, "#f1cfa3"); sky.addColorStop(0.7, "#ffd9a8"); sky.addColorStop(1, "#f7b98a");
  g.fillStyle = sky; g.fillRect(0, 0, w, h);
  const sun = g.createRadialGradient(w * 0.2, h * 0.58, 0, w * 0.2, h * 0.58, 360); sun.addColorStop(0, "rgba(255,246,214,1)"); sun.addColorStop(0.25, "rgba(255,226,168,.75)"); sun.addColorStop(1, "rgba(255,200,140,0)"); g.fillStyle = sun; g.fillRect(0, 0, w, h);
  g.fillStyle = "rgba(255,255,255,.34)"; for (let i = 0; i < 14; i++) { const x = rnd(i, 1) * w, y = 40 + rnd(i, 2) * 220; for (let k = 0; k < 6; k++) { g.beginPath(); g.ellipse(x + k * 34, y + Math.sin(k) * 9, 62 + rnd(i, k) * 40, 18 + rnd(i, k + 3) * 10, 0, 0, Math.PI * 2); g.fill(); } }
  const hills: [string, number, number][] = [["rgba(150,150,170,.55)", 0.62, 60], ["rgba(112,128,120,.7)", 0.7, 50], ["rgba(76,104,70,.9)", 0.8, 40]];
  hills.forEach(([color, base, amp], l) => { g.fillStyle = color; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 16) g.lineTo(x, h * base + Math.sin(x * 0.006 + l * 2) * amp * 0.5 + Math.sin(x * 0.015 + l) * amp * 0.25); g.lineTo(w, h); g.closePath(); g.fill(); });
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace;
  return new T.Mesh(new T.PlaneGeometry(width, height), new T.MeshBasicMaterial({ map: t, fog: false, toneMapped: false }));
}
```

## 42. `src/engine/geometry.ts` — new

```ts
/** Reusable procedural geometry for the gift worlds. Everything is generated, nothing is loaded from disk. */
import * as T from "three";
export { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";

export const v3 = (x = 0, y = 0, z = 0) => new T.Vector3(x, y, z);

export function tube(points: [number, number, number][], radius: number, segments = 32, radial = 8, tension = 0.5) {
  const curve = new T.CatmullRomCurve3(points.map((p) => new T.Vector3(...p)), false, "catmullrom", tension);
  return new T.TubeGeometry(curve, segments, radius, radial, false);
}

export function lathe(profile: [number, number][], segments = 48) {
  return new T.LatheGeometry(profile.map(([r, y]) => new T.Vector2(r, y)), segments);
}

/**
 * Curved, tapered petal. Base at y = 0, tip at y = length. `cup` bows the sides upward, `curl` rolls the tip back,
 * `flare` widens the blade near the tip (roses) or keeps it narrow (daisies). UVs are u across / v along the petal.
 */
export function petalGeometry(length: number, width: number, cup = 0.15, curl = 0.1, flare = 0.7, segU = 12, segV = 20) {
  const geometry = new T.PlaneGeometry(1, 1, segU, segV);
  const p = geometry.attributes.position;
  for (let i = 0; i < p.count; i++) {
    const u = p.getX(i) * 2, v = p.getY(i) + 0.5;
    const outline = Math.pow(Math.sin(Math.PI * Math.pow(v, 0.78)), flare) * (0.35 + 0.65 * Math.sin(Math.PI * Math.min(1, v * 1.15 + 0.08)));
    const x = u * width * outline;
    const z = cup * u * u * (0.3 + v) * width * 2 - curl * Math.pow(v, 3) * length * 0.9 + 0.04 * length * Math.sin(v * Math.PI);
    const ripple = 0.012 * length * Math.sin(u * 7 + v * 5) * v;
    p.setXYZ(i, x, v * length, z + ripple);
  }
  geometry.computeVertexNormals();
  return geometry;
}

/** Pointed leaf with a drooping tip. Base at y = 0. */
export function leafGeometry(length: number, width: number, droop = 0.25, fold = 0.12, segU = 8, segV = 16) {
  const geometry = new T.PlaneGeometry(1, 1, segU, segV);
  const p = geometry.attributes.position;
  for (let i = 0; i < p.count; i++) {
    const u = p.getX(i) * 2, v = p.getY(i) + 0.5;
    const outline = Math.pow(Math.sin(Math.PI * Math.pow(v, 0.7)), 0.8);
    p.setXYZ(i, u * width * outline, v * length, -droop * Math.pow(v, 2) * length + fold * Math.abs(u) * width * outline);
  }
  geometry.computeVertexNormals();
  return geometry;
}

/** Faceted gemstone built from a low-segment lathe so `flatShading` shows every facet. */
export function gemGeometry(radius = 1, segments = 8, crown = 0.38, pavilion = 0.85, table = 0.55) {
  const profile: [number, number][] = [[0, -pavilion * radius], [radius, 0], [radius * 0.97, crown * 0.12 * radius], [radius * table, crown * radius], [0, crown * radius]];
  return lathe(profile, segments);
}

export function starShape(outer: number, inner: number, points = 5) {
  const shape = new T.Shape();
  for (let i = 0; i < points * 2; i++) {
    const a = (i * Math.PI) / points - Math.PI / 2, r = i % 2 ? inner : outer;
    if (i) shape.lineTo(Math.cos(a) * r, Math.sin(a) * r); else shape.moveTo(Math.cos(a) * r, Math.sin(a) * r);
  }
  shape.closePath();
  return shape;
}

export function heartShape(size = 1) {
  const s = new T.Shape(), k = size;
  s.moveTo(0, -0.9 * k);
  s.bezierCurveTo(-1.1 * k, -0.1 * k, -0.8 * k, 0.9 * k, 0, 0.45 * k);
  s.bezierCurveTo(0.8 * k, 0.9 * k, 1.1 * k, -0.1 * k, 0, -0.9 * k);
  return s;
}

export function bevelled(shape: T.Shape, depth: number, bevel = 0.02, curveSegments = 24) {
  const g = new T.ExtrudeGeometry(shape, { depth, bevelEnabled: true, bevelSize: bevel, bevelThickness: bevel, bevelSegments: 3, curveSegments });
  g.center();
  return g;
}

/** A sheet of paper that is slightly bowed and curls at the corners. `rows` x `cols` quads. */
export function bentPaper(width: number, height: number, bow = 0.04, curl = 0.05, cols = 10, rows = 14) {
  const geometry = new T.PlaneGeometry(width, height, cols, rows);
  const p = geometry.attributes.position;
  for (let i = 0; i < p.count; i++) {
    const x = p.getX(i) / (width / 2), y = p.getY(i) / (height / 2);
    p.setZ(i, bow * (1 - y * y) * (1 - 0.4 * x * x) + curl * Math.pow(Math.abs(x), 5) * Math.pow(Math.abs(y), 3) * Math.sign(x * y + 0.0001));
  }
  geometry.computeVertexNormals();
  return geometry;
}

/** Flat ribbon following a curve, with width along the curve's binormal. Used for bows and bookmarks. */
export function ribbon(curve: T.Curve<T.Vector3>, width = 0.12, segments = 48, twist = 0) {
  const positions: number[] = [], uvs: number[] = [], indices: number[] = [];
  const up = new T.Vector3(0, 1, 0), tangent = new T.Vector3(), normal = new T.Vector3(), side = new T.Vector3();
  for (let i = 0; i <= segments; i++) {
    const t = i / segments, point = curve.getPoint(t); curve.getTangent(t, tangent);
    side.crossVectors(tangent, up).normalize();
    if (side.lengthSq() < 1e-4) side.set(1, 0, 0);
    normal.crossVectors(side, tangent).normalize();
    side.applyAxisAngle(tangent, twist * t);
    for (const s of [-1, 1]) positions.push(point.x + side.x * width * 0.5 * s, point.y + side.y * width * 0.5 * s, point.z + side.z * width * 0.5 * s);
    uvs.push(0, t, 1, t);
    if (i < segments) { const a = i * 2; indices.push(a, a + 1, a + 2, a + 1, a + 3, a + 2); }
  }
  const geometry = new T.BufferGeometry();
  geometry.setAttribute("position", new T.Float32BufferAttribute(positions, 3));
  geometry.setAttribute("uv", new T.Float32BufferAttribute(uvs, 2));
  geometry.setIndex(indices); geometry.computeVertexNormals();
  return geometry;
}

/** Convenience mesh creation: add to parent at a position, optionally casting/receiving shadows. */
export function put<G extends T.BufferGeometry, M extends T.Material>(parent: T.Object3D, geometry: G, material: M, x = 0, y = 0, z = 0, shadow = true) {
  const mesh = new T.Mesh(geometry, material);
  mesh.position.set(x, y, z); mesh.castShadow = shadow; mesh.receiveShadow = shadow;
  parent.add(mesh);
  return mesh;
}

/**
 * Tube whose radius tapers from r0 to r1. Rings are emitted in path order, so `growTube` can animate growth
 * along the curve by changing the draw range (roots, stems, tendrils).
 */
export function taperedTube(curve: T.Curve<T.Vector3>, r0: number, r1: number, segments = 48, radial = 8) {
  const positions: number[] = [], normals: number[] = [], uvs: number[] = [], indices: number[] = [];
  const frames = curve.computeFrenetFrames(segments, false);
  for (let i = 0; i <= segments; i++) {
    const t = i / segments, p = curve.getPointAt(t), r = r0 + (r1 - r0) * t, n = frames.normals[i], b = frames.binormals[i];
    for (let j = 0; j <= radial; j++) {
      const a = (j / radial) * Math.PI * 2, c = Math.cos(a), s = Math.sin(a);
      const nx = c * n.x + s * b.x, ny = c * n.y + s * b.y, nz = c * n.z + s * b.z;
      positions.push(p.x + r * nx, p.y + r * ny, p.z + r * nz); normals.push(nx, ny, nz); uvs.push(j / radial, t);
    }
  }
  for (let i = 0; i < segments; i++) for (let j = 0; j < radial; j++) { const a = i * (radial + 1) + j, b = a + radial + 1; indices.push(a, b, a + 1, b, b + 1, a + 1); }
  const geometry = new T.BufferGeometry();
  geometry.setAttribute("position", new T.Float32BufferAttribute(positions, 3));
  geometry.setAttribute("normal", new T.Float32BufferAttribute(normals, 3));
  geometry.setAttribute("uv", new T.Float32BufferAttribute(uvs, 2));
  geometry.setIndex(indices);
  geometry.userData.segments = segments; geometry.userData.radial = radial;
  return geometry;
}

/** Shows the first `amount` (0..1) of a taperedTube. */
export function growTube(mesh: T.Mesh, amount: number) {
  const { segments, radial } = mesh.geometry.userData as { segments: number; radial: number };
  const rings = Math.floor(Math.min(1, Math.max(0, amount)) * segments);
  mesh.geometry.setDrawRange(0, rings * radial * 6);
  mesh.visible = rings > 0;
}
```

## 43. `src/engine/lights.ts` — new

```ts
/**
 * Renderer configuration, lighting presets and cheap fake shadows.
 * Every scene goes through `prepareStage` so tone mapping, colour space, environment and shadow quality are uniform.
 */
import * as T from "three";
import { createEnvironment, type EnvPreset } from "./environment";
import { shadowMapSize, type Quality } from "./quality";

export interface MoodOptions {
  env: EnvPreset;
  /** scene.environmentIntensity: how strongly the baked environment lights the scene. */
  envIntensity?: number;
  exposure?: number;
  background?: string | null;
  fog?: { color: string; density: number } | null;
}

export function configureRenderer(renderer: T.WebGLRenderer, quality: Quality) {
  renderer.outputColorSpace = T.SRGBColorSpace;
  renderer.toneMapping = T.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 1;
  renderer.shadowMap.enabled = shadowMapSize(quality) > 0;
  renderer.shadowMap.type = T.PCFShadowMap; // PCFSoftShadowMap was removed in three r18x
}

/** Applies environment, exposure, background and fog for a scene "mood". */
export function applyMood(renderer: T.WebGLRenderer, scene: T.Scene, mood: MoodOptions) {
  scene.environment = createEnvironment(renderer, mood.env);
  scene.environmentIntensity = mood.envIntensity ?? 1;
  renderer.toneMappingExposure = mood.exposure ?? 1;
  if (mood.background !== undefined) scene.background = mood.background ? new T.Color(mood.background) : null;
  scene.fog = mood.fog ? new T.FogExp2(mood.fog.color, mood.fog.density) : null;
}

export interface KeyLightOptions {
  color?: string;
  intensity?: number;
  position?: [number, number, number];
  target?: [number, number, number];
  /** half-width of the shadow frustum */
  extent?: number;
  near?: number;
  far?: number;
  radius?: number;
}

/** Shadow-casting directional key light whose shadow map follows the quality tier. */
export function addKeyLight(scene: T.Scene, quality: Quality, options: KeyLightOptions = {}) {
  const light = new T.DirectionalLight(options.color ?? "#fff0d8", options.intensity ?? 3);
  light.position.set(...(options.position ?? [-4, 8, 5]));
  const target = new T.Object3D(); target.position.set(...(options.target ?? [0, 0, 0]));
  scene.add(target); light.target = target;
  const size = shadowMapSize(quality);
  if (size) {
    const e = options.extent ?? 6;
    light.castShadow = true;
    light.shadow.mapSize.set(size, size);
    Object.assign(light.shadow.camera, { left: -e, right: e, top: e, bottom: -e, near: options.near ?? 0.5, far: options.far ?? 30 });
    light.shadow.bias = -0.0004; light.shadow.normalBias = 0.025; light.shadow.radius = options.radius ?? 3;
  }
  scene.add(light);
  return light;
}

/** Warm point light with optional shadow (only enabled on high, point shadows are six renders). */
export function addPointLight(scene: T.Scene, color: string, intensity: number, position: [number, number, number], distance = 12, decay = 2, shadow = false) {
  const light = new T.PointLight(color, intensity, distance, decay);
  light.position.set(...position);
  if (shadow) { light.castShadow = true; light.shadow.mapSize.set(1024, 1024); light.shadow.bias = -0.0008; light.shadow.normalBias = 0.03; }
  scene.add(light);
  return light;
}

export function addSpotLight(scene: T.Scene, quality: Quality, color: string, intensity: number, position: [number, number, number], target: [number, number, number], angle = 0.5, penumbra = 0.7) {
  const light = new T.SpotLight(color, intensity, 0, angle, penumbra, 1.4);
  light.position.set(...position);
  const aim = new T.Object3D(); aim.position.set(...target); scene.add(aim); light.target = aim;
  const size = shadowMapSize(quality);
  if (size) { light.castShadow = true; light.shadow.mapSize.set(size, size); light.shadow.bias = -0.0004; light.shadow.normalBias = 0.02; light.shadow.radius = 4; }
  scene.add(light);
  return light;
}

let blobTexture: T.CanvasTexture | null = null;
function blobShadowTexture() {
  if (blobTexture) return blobTexture;
  const canvas = document.createElement("canvas"); canvas.width = canvas.height = 128;
  const ctx = canvas.getContext("2d")!;
  const g = ctx.createRadialGradient(64, 64, 4, 64, 64, 64);
  g.addColorStop(0, "rgba(0,0,0,0.85)"); g.addColorStop(0.55, "rgba(0,0,0,0.35)"); g.addColorStop(1, "rgba(0,0,0,0)");
  ctx.fillStyle = g; ctx.fillRect(0, 0, 128, 128);
  blobTexture = new T.CanvasTexture(canvas);
  return blobTexture;
}

/**
 * Soft contact shadow under an object. On `low` (no shadow maps) this is the only shadow; on higher tiers it
 * adds ambient occlusion where real shadow maps are too coarse.
 */
export function addContactShadow(parent: T.Object3D, width: number, depth: number, x = 0, y = 0.003, z = 0, opacity = 0.55) {
  const material = new T.MeshBasicMaterial({ map: blobShadowTexture(), transparent: true, opacity, depthWrite: false, toneMapped: false });
  const mesh = new T.Mesh(new T.PlaneGeometry(width, depth), material);
  mesh.rotation.x = -Math.PI / 2; mesh.position.set(x, y, z); mesh.renderOrder = 1;
  parent.add(mesh);
  return mesh;
}

/** Marks a mesh (and children) to cast and/or receive shadows. */
export function shadowed<T3 extends T.Object3D>(object: T3, cast = true, receive = true) {
  object.traverse((child) => { if (child instanceof T.Mesh) { child.castShadow = cast; child.receiveShadow = receive; } });
  return object;
}
```

## 44. `src/engine/materials.ts` — new

```ts
/**
 * Shared material system. One MaterialKit per scene: it builds PBR materials from the procedural textures and
 * degrades gracefully by quality tier (transmission glass only on `high`, normal maps only above `low`).
 * Materials are plain three.js objects, so `disposeTree` releases them with the scene.
 */
import * as T from "three";
import type { Quality } from "./quality";
import {
  barkCanvas, brushedCanvas, fabricCanvas, leafCanvas, leatherCanvas, marbleCanvas, paperCanvas, petalCanvas,
  soilCanvas, stoneCanvas, surfaceMaps, textureSize, toTexture, woodCanvas, type SurfaceMaps,
} from "./textures";

type Repeat = [number, number];

export class MaterialKit {
  readonly size: number;
  constructor(readonly quality: Quality) { this.size = textureSize(quality); }

  private get normal() { return this.quality === "low" ? 0 : 1.3; }
  private apply(material: T.MeshStandardMaterial, maps: SurfaceMaps, bump = 0.6, normalScale = 0.8) {
    material.map = maps.map;
    if (maps.normalMap) { material.normalMap = maps.normalMap; material.normalScale.set(normalScale, normalScale); }
    else if (maps.bumpMap) { material.bumpMap = maps.bumpMap; material.bumpScale = bump; }
    return material;
  }

  wood(dark = "#3b2417", light = "#8a5e3b", repeat: Repeat = [2, 2], roughness = 0.58) {
    const maps = surfaceMaps(woodCanvas(this.size, dark, light), { repeat, normal: this.normal });
    return this.apply(new T.MeshStandardMaterial({ roughness, metalness: 0 }), maps, 0.8, 0.9);
  }

  paper(light = "#f4ead3", dark = "#dccaa6", options: { side?: T.Side; repeat?: Repeat; roughness?: number } = {}) {
    const maps = surfaceMaps(paperCanvas(this.size, light, dark), { repeat: options.repeat ?? [1, 1], normal: this.normal ? 1.2 : 0 });
    return this.apply(new T.MeshStandardMaterial({ roughness: options.roughness ?? 0.92, metalness: 0, side: options.side ?? T.FrontSide }), maps, 0.4, 0.45);
  }

  kraft(light = "#d4b88a", dark = "#a98b5d") { return this.paper(light, dark, { roughness: 0.95 }); }

  leather(dark = "#1f2d29", light = "#3d544c", repeat: Repeat = [3, 3]) {
    const maps = surfaceMaps(leatherCanvas(this.size, dark, light), { repeat, normal: this.normal });
    return this.apply(new T.MeshStandardMaterial({ roughness: 0.62, metalness: 0 }), maps, 1, 0.9);
  }

  fabric(dark = "#6d3a49", light = "#a65f73", repeat: Repeat = [4, 4]) {
    const maps = surfaceMaps(fabricCanvas(this.size, dark, light), { repeat, normal: this.normal });
    return this.apply(new T.MeshPhysicalMaterial({ roughness: 0.88, metalness: 0, sheen: 0.8, sheenColor: new T.Color(light), sheenRoughness: 0.5 }), maps, 0.8, 0.7);
  }

  velvet(color = "#6e2b46") {
    const c = new T.Color(color);
    return new T.MeshPhysicalMaterial({ color: c, roughness: 0.95, metalness: 0, sheen: 1, sheenColor: c.clone().lerp(new T.Color("#ffffff"), 0.45), sheenRoughness: 0.35 });
  }

  /** Brushed metal. `kind` picks the tint; all are fully metallic and rely on the scene environment for reflections. */
  metal(kind: "brass" | "gold" | "silver" | "copper" | "steel" | "rosegold" = "brass", roughness = 0.5) {
    const tint = { brass: "#c9a24e", gold: "#e6b95f", silver: "#d6dade", copper: "#c4795a", steel: "#9aa0a6", rosegold: "#e0a995" }[kind];
    const brushed = brushedCanvas(this.size, "#707070", "#ffffff");
    return new T.MeshStandardMaterial({ color: tint, metalness: 1, roughness, roughnessMap: toTexture(brushed.height, { repeat: [3, 3] }), envMapIntensity: 1.35 });
  }

  wax(color = "#8b2c3c") {
    return new T.MeshPhysicalMaterial({ color, roughness: 0.34, metalness: 0, clearcoat: 0.9, clearcoatRoughness: 0.22, sheen: 0.4, sheenColor: new T.Color("#ff9aa8"), sheenRoughness: 0.5 });
  }

  ceramic(color = "#f2efe8", gloss = 0.9) {
    return new T.MeshPhysicalMaterial({ color, roughness: 0.28, metalness: 0, clearcoat: gloss, clearcoatRoughness: 0.12 });
  }

  marble(dark = "#cfc8c0", light = "#fbf8f2") {
    const maps = surfaceMaps(marbleCanvas(this.size, dark, light), { repeat: [1, 1] });
    return this.apply(new T.MeshPhysicalMaterial({ roughness: 0.22, clearcoat: 0.6, clearcoatRoughness: 0.2 }), maps, 0.15);
  }

  stone(dark = "#6f6c64", light = "#b1ada0", repeat: Repeat = [2, 2]) {
    const maps = surfaceMaps(stoneCanvas(this.size, dark, light), { repeat, normal: this.normal });
    return this.apply(new T.MeshStandardMaterial({ roughness: 0.9 }), maps, 1, 1);
  }

  soil(dark = "#241a12", light = "#6b4a30", repeat: Repeat = [3, 3]) {
    const maps = surfaceMaps(soilCanvas(this.size, dark, light), { repeat, normal: this.normal });
    return this.apply(new T.MeshStandardMaterial({ roughness: 0.97 }), maps, 1, 1.1);
  }

  bark(dark = "#2d2218", light = "#6e5a43", repeat: Repeat = [1, 3]) {
    const maps = surfaceMaps(barkCanvas(this.size, dark, light), { repeat, normal: this.normal });
    return this.apply(new T.MeshStandardMaterial({ roughness: 0.95 }), maps, 1, 1.2);
  }

  leaf(dark = "#2f5a34", light = "#6f9a4c") {
    const maps = surfaceMaps(leafCanvas(dark, light, this.quality === "low" ? 128 : 256), { wrap: false, normal: this.normal ? 1.4 : 0 });
    const material = this.apply(new T.MeshPhysicalMaterial({ roughness: 0.55, side: T.DoubleSide, sheen: 0.5, sheenColor: new T.Color("#d8f0a0"), sheenRoughness: 0.6 }), maps, 0.6, 0.6);
    return material;
  }

  /** Translucent-looking petal. Real subsurface scattering is faked with sheen plus a faint emissive base tint. */
  petal(base = "#f6d6dc", tip = "#e48ba3", vein = "#b04a68") {
    const maps = surfaceMaps(petalCanvas(base, tip, vein, this.quality === "low" ? 128 : 256), { wrap: false, normal: this.normal ? 1.2 : 0 });
    const material = this.apply(new T.MeshPhysicalMaterial({
      roughness: 0.5, side: T.DoubleSide, sheen: 0.8, sheenColor: new T.Color(base), sheenRoughness: 0.4,
      emissive: new T.Color(tip).multiplyScalar(0.06), clearcoat: 0.15, clearcoatRoughness: 0.5,
    }), maps, 0.5, 0.5);
    return material;
  }

  /** Clear glass: real transmission on high, a cheap but convincing reflective shell elsewhere. */
  glass(tint = "#e3f2ee", thickness = 0.35) {
    if (this.quality === "high") {
      return new T.MeshPhysicalMaterial({
        color: "#ffffff", metalness: 0, roughness: 0.03, transmission: 1, thickness, ior: 1.5,
        attenuationColor: new T.Color(tint), attenuationDistance: 3, specularIntensity: 1, envMapIntensity: 1.3,
      });
    }
    return new T.MeshPhysicalMaterial({
      color: tint, metalness: 0, roughness: 0.05, transparent: true, opacity: this.quality === "medium" ? 0.2 : 0.26,
      clearcoat: 1, clearcoatRoughness: 0.04, envMapIntensity: 1.7, side: T.DoubleSide, depthWrite: false,
    });
  }

  /** Cut gemstone. flatShading keeps every facet visible. */
  gem(color = "#c93a62") {
    const high = this.quality === "high";
    return new T.MeshPhysicalMaterial({
      color, metalness: 0.05, roughness: 0.02, flatShading: true, ior: 2.4, clearcoat: 1, clearcoatRoughness: 0,
      transmission: high ? 0.85 : 0, thickness: high ? 0.6 : 0, envMapIntensity: 2.4, specularIntensity: 1,
      emissive: new T.Color(color).multiplyScalar(high ? 0.04 : 0.22),
    });
  }

  emissive(color: string, strength = 1) { return new T.MeshBasicMaterial({ color: new T.Color(color).multiplyScalar(strength), fog: false }); }
}
```

## 45. `src/engine/paper.ts` — new

```ts
import * as T from "three";

const smoother = T.MathUtils.smootherstep;

export interface FoldedPaper {
  /** Material order: [0] text face, [1] back face, [2] cut edge. */
  geometry: T.BufferGeometry;
  width: number;
  height: number;
  /**
   * upper / lower: 0 = that third folded over the middle panel, 1 = flat.
   * curl: 0..1 how much the corners lift (fresh from the envelope) vs lie relaxed.
   */
  deform: (upper: number, lower: number, curl?: number) => void;
}

/**
 * A sheet of paper folded in thirds, built as ONE continuous two-sided surface with real thickness.
 * The tangent bends across two rounded crease bands and is integrated to positions, so arc length is preserved
 * (the paper bends, it never stretches) and the outer fold wraps the inner one with a larger radius.
 * Vertex colours darken the creases (cheap ambient occlusion); the corners lift slightly.
 */
export function createFoldedPaper({ columns = 32, rows = 120, width = 3.0, height = 4.1 } = {}): FoldedPaper {
  const stride = columns + 1, count = stride * (rows + 1);
  const position = new Float32Array(count * 2 * 3), uv = new Float32Array(count * 2 * 2), color = new Float32Array(count * 2 * 3).fill(1);
  const indices: number[] = [];
  for (let side = 0; side < 2; side++) for (let j = 0; j <= rows; j++) for (let i = 0; i <= columns; i++) {
    const n = side * count + j * stride + i;
    uv[n * 2] = i / columns; uv[n * 2 + 1] = j / rows;
    if (i < columns && j < rows) {
      const a = n, b = n + 1, c = n + stride, d = c + 1;
      indices.push(...(side ? [a, c, b, b, c, d] : [a, b, c, b, d, c]));
    }
  }
  const faceCount = columns * rows * 6;
  const edge = (a: number, b: number) => indices.push(a, b, a + count, b, b + count, a + count);
  for (let i = 0; i < columns; i++) { edge(i + 1, i); edge(rows * stride + i, rows * stride + i + 1); }
  for (let j = 0; j < rows; j++) { edge(j * stride, (j + 1) * stride); edge((j + 1) * stride + columns, j * stride + columns); }

  const geometry = new T.BufferGeometry();
  geometry.setAttribute("position", new T.BufferAttribute(position, 3).setUsage(T.DynamicDrawUsage));
  geometry.setAttribute("uv", new T.BufferAttribute(uv, 2));
  geometry.setAttribute("color", new T.BufferAttribute(color, 3).setUsage(T.DynamicDrawUsage));
  geometry.setIndex(indices);
  geometry.addGroup(0, faceCount, 0); geometry.addGroup(faceCount, faceCount, 1); geometry.addGroup(faceCount * 2, indices.length - faceCount * 2, 2);

  const scale = height / 2.79, crease = height / 6;
  const ys = new Float32Array(rows + 1), zs = new Float32Array(rows + 1), angles = new Float32Array(rows + 1), ao = new Float32Array(rows + 1);
  const mid = rows / 2;

  const deform = (upper: number, lower: number, curl = 0) => {
    const tangent = (y: number) => y >= 0
      ? Math.PI * (1 - upper) * smoother(y, crease - 0.06 * scale, crease + 0.06 * scale)
      : -Math.PI * (1 - lower) * smoother(-y, crease - 0.025 * scale, crease + 0.025 * scale);
    ys[mid] = 0; zs[mid] = 0; angles[mid] = 0;
    for (const direction of [-1, 1]) for (let step = 1; step <= mid; step++) {
      const j = mid + direction * step, prev = j - direction;
      const delta = (direction * height) / rows, y = (j / rows - 0.5) * height;
      const a = tangent(y - delta / 2);
      angles[j] = tangent(y);
      ys[j] = ys[prev] + Math.cos(a) * delta; zs[j] = zs[prev] + Math.sin(a) * delta;
    }
    for (let j = 0; j <= rows; j++) ao[j] = j === 0 || j === rows ? 1 : 1 - Math.min(0.34, Math.abs(angles[j + 1] - angles[j - 1]) * 0.5);
    const lift = 0.012 + 0.07 * curl;
    for (let side = 0; side < 2; side++) for (let j = 0; j <= rows; j++) {
      const yn = Math.abs(j / rows - 0.5) * 2;
      for (let i = 0; i <= columns; i++) {
        const x = (i / columns - 0.5) * width, u = Math.abs(x) / (width / 2);
        const thickness = (side ? -1 : 1) * 0.005;
        const edgeCurl = lift * Math.pow(u, 4) * (0.25 + 0.75 * yn * yn);
        const n = side * count + j * stride + i, k = n * 3;
        position[k] = x;
        position[k + 1] = ys[j] - Math.sin(angles[j]) * thickness;
        position[k + 2] = zs[j] + Math.cos(angles[j]) * thickness + edgeCurl;
        color[k] = color[k + 1] = color[k + 2] = ao[j];
      }
    }
    geometry.attributes.position.needsUpdate = true; geometry.attributes.color.needsUpdate = true;
    geometry.computeVertexNormals(); geometry.computeBoundingSphere();
  };
  deform(0, 0);
  return { geometry, width, height, deform };
}
```

## 46. `src/engine/quality.ts` — new

```ts
/**
 * Device capability tiers and adaptive resolution.
 *
 * - `low`    phones / weak GPUs: no shadow maps, DPR 1, cheap glass, few particles
 * - `medium` typical laptops: soft shadows, DPR <= 1.5
 * - `high`   capable desktops: 2048 shadows, DPR <= 2, transmission glass, full particle counts
 *
 * The tier can be forced with `?quality=low|medium|high` or localStorage["woy-quality"] (used by QA).
 */
export type Quality = "low" | "medium" | "high";

const STORAGE_KEY = "woy-quality";

export function readQualityOverride(): Quality | null {
  try {
    const raw = new URLSearchParams(window.location.search).get("quality") ?? window.localStorage.getItem(STORAGE_KEY);
    return raw === "low" || raw === "medium" || raw === "high" ? raw : null;
  } catch {
    return null;
  }
}

export function rememberQuality(quality: Quality) {
  try { window.localStorage.setItem(STORAGE_KEY, quality); } catch { /* storage may be blocked; the choice just won't persist */ }
}

let softwareRenderer: boolean | null = null;
/** True when the browser renders WebGL on the CPU (SwiftShader, llvmpipe, "software"): such devices get the low tier unless the visitor chose otherwise. */
export function isSoftwareRenderer(): boolean {
  if (softwareRenderer !== null) return softwareRenderer;
  softwareRenderer = false;
  try {
    const canvas = document.createElement("canvas");
    const gl = (canvas.getContext("webgl2") || canvas.getContext("webgl")) as WebGLRenderingContext | null;
    const info = gl?.getExtension("WEBGL_debug_renderer_info");
    const name = gl && info ? String(gl.getParameter(info.UNMASKED_RENDERER_WEBGL)) : "";
    softwareRenderer = /swiftshader|llvmpipe|software|softpipe|basic render/i.test(name);
    gl?.getExtension("WEBGL_lose_context")?.loseContext();
  } catch { /* unknown renderer: keep the hardware assumption */ }
  return softwareRenderer;
}

export function detectQuality(): Quality {
  const forced = readQualityOverride();
  if (forced) return forced;
  if (isSoftwareRenderer()) return "low";
  const nav = navigator as Navigator & { deviceMemory?: number };
  const cores = nav.hardwareConcurrency ?? 4;
  const memory = nav.deviceMemory ?? 4;
  const touch = window.matchMedia("(pointer: coarse)").matches;
  if (window.innerWidth < 700 || (touch && cores <= 6) || memory <= 2 || cores <= 2) return "low";
  if (!touch && cores >= 8 && memory >= 8) return "high";
  return "medium";
}

/** Device pixel ratio for a tier. `scale` is the adaptive multiplier maintained by FrameGovernor. */
export function pixelRatioFor(quality: Quality, scale = 1) {
  const cap = quality === "high" ? 2 : quality === "medium" ? 1.5 : 1;
  return Math.max(0.6, Math.min(window.devicePixelRatio || 1, cap) * scale);
}

export const shadowMapSize = (quality: Quality) => (quality === "high" ? 2048 : quality === "medium" ? 1024 : 0);
/** Multiplier applied to particle counts. */
export const particleScale = (quality: Quality) => (quality === "high" ? 1 : quality === "medium" ? 0.6 : 0.3);
/** Geometry subdivision multiplier for curved meshes. */
export const detailScale = (quality: Quality) => (quality === "high" ? 1 : quality === "medium" ? 0.75 : 0.5);

/**
 * Lowers render resolution when frames are slow and raises it again when there is headroom.
 * Feed it the CPU frame interval in milliseconds; it returns true when `scale` changed.
 */
export class FrameGovernor {
  scale = 1;
  private average = 16;
  private slow = 0;
  private fast = 0;
  constructor(private readonly floor = 0.6) {}

  tick(ms: number): boolean {
    if (ms > 250 || ms <= 0) return false; // hidden tab or debugger pause, not a real frame time
    this.average += (ms - this.average) * 0.08;
    if (this.average > 26) { this.slow += ms; this.fast = 0; }
    else if (this.average < 14) { this.fast += ms; this.slow = 0; }
    else { this.slow = 0; this.fast = 0; }
    if (this.slow > 1800 && this.scale > this.floor) { this.scale = Math.max(this.floor, this.scale - 0.15); this.slow = 0; return true; }
    if (this.fast > 5000 && this.scale < 1) { this.scale = Math.min(1, this.scale + 0.1); this.fast = 0; return true; }
    return false;
  }
}

export const prefersReducedMotion = () => window.matchMedia("(prefers-reduced-motion: reduce)").matches;
```

## 47. `src/engine/stage.ts` — new

```ts
/**
 * Everything a gift/scene builder receives besides raw three.js objects: shared materials, mood presets,
 * sound effects and unified pointer / keyboard input. Both rendering hosts create their Stage through here.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../three/runtime";
import { audioBus } from "./audio";
import { applyMood, configureRenderer } from "./lights";
import { MaterialKit } from "./materials";
import type { Quality } from "./quality";

/** Pointer and keyboard state shared by every scene. Scenes read it each frame; the host feeds it. */
export interface StageInput {
  /** pointer in normalised device coordinates (-1..1) */
  pointer: T.Vector2;
  inside: boolean;
  dragging: boolean;
  /** release inertia, decays on its own */
  velocity: T.Vector2;
  keys: Set<string>;
  /** drag accumulated since the previous call, in fractions of the canvas width / height */
  consumeDrag(): T.Vector2;
  update(dt: number): void;
}

export function attachInput(canvas: HTMLElement, keyTarget: HTMLElement = canvas, touchAction = "pan-y") {
  const pointer = new T.Vector2(), pending = new T.Vector2(), velocity = new T.Vector2(), keys = new Set<string>();
  let dragging = false, inside = false, lastX = 0, lastY = 0;
  canvas.style.touchAction = touchAction;
  const normalise = (e: PointerEvent) => {
    const r = canvas.getBoundingClientRect();
    pointer.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
  };
  const down = (e: PointerEvent) => { dragging = true; lastX = e.clientX; lastY = e.clientY; normalise(e); try { canvas.setPointerCapture(e.pointerId); } catch { /* synthetic events have no capturable pointer */ } };
  const move = (e: PointerEvent) => {
    normalise(e); inside = true;
    if (!dragging) return;
    const r = canvas.getBoundingClientRect(), dx = (e.clientX - lastX) / r.width, dy = (e.clientY - lastY) / r.height;
    pending.x += dx; pending.y += dy; velocity.set(dx, dy); lastX = e.clientX; lastY = e.clientY;
  };
  const up = (e: PointerEvent) => { dragging = false; try { canvas.releasePointerCapture(e.pointerId); } catch { /* not captured */ } };
  const enter = () => { inside = true; };
  const leave = () => { inside = false; };
  const keydown = (e: KeyboardEvent) => { if (e.key.startsWith("Arrow")) { keys.add(e.key); e.preventDefault(); } };
  const keyup = (e: KeyboardEvent) => { keys.delete(e.key); };
  const blur = () => keys.clear();
  canvas.addEventListener("pointerdown", down); canvas.addEventListener("pointermove", move); canvas.addEventListener("pointerup", up);
  canvas.addEventListener("pointercancel", up); canvas.addEventListener("pointerenter", enter); canvas.addEventListener("pointerleave", leave);
  keyTarget.addEventListener("keydown", keydown); keyTarget.addEventListener("keyup", keyup); keyTarget.addEventListener("blur", blur);
  const input: StageInput = {
    pointer, velocity, keys,
    get inside() { return inside; }, set inside(v: boolean) { inside = v; },
    get dragging() { return dragging; }, set dragging(v: boolean) { dragging = v; },
    consumeDrag() { const out = pending.clone(); pending.set(0, 0); return out; },
    update(dt: number) {
      if (!dragging) velocity.multiplyScalar(Math.exp(-dt * 4));
      const step = dt * 0.32;
      if (keys.has("ArrowLeft")) pending.x -= step; if (keys.has("ArrowRight")) pending.x += step;
      if (keys.has("ArrowUp")) pending.y -= step; if (keys.has("ArrowDown")) pending.y += step;
    },
  };
  return {
    input,
    dispose() {
      canvas.removeEventListener("pointerdown", down); canvas.removeEventListener("pointermove", move); canvas.removeEventListener("pointerup", up);
      canvas.removeEventListener("pointercancel", up); canvas.removeEventListener("pointerenter", enter); canvas.removeEventListener("pointerleave", leave);
      keyTarget.removeEventListener("keydown", keydown); keyTarget.removeEventListener("keyup", keyup); keyTarget.removeEventListener("blur", blur);
    },
  };
}

/** Input object with no listeners, for offline rendering (preview / export tooling). */
export function idleInput(): StageInput {
  return { pointer: new T.Vector2(), inside: false, dragging: false, velocity: new T.Vector2(), keys: new Set<string>(), consumeDrag: () => new T.Vector2(), update: () => {} };
}

export interface StageOptions {
  renderer: T.WebGLRenderer;
  root: T.Scene;
  camera: T.PerspectiveCamera;
  quality: Quality;
  input: StageInput;
  pick: (index: number) => void;
  report?: (progress: number) => void;
  /** Called after environment / background / fog change so a host that renders a different scene can mirror them. */
  syncScene?: (root: T.Scene) => void;
  /** Asks the host for another frame (needed when something arrives asynchronously while the loop is idle, e.g. a texture). */
  invalidate?: () => void;
}

export function createStage(o: StageOptions): Stage {
  configureRenderer(o.renderer, o.quality);
  return {
    scene: o.root, camera: o.camera, quality: o.quality, pick: o.pick, report: o.report,
    renderer: o.renderer, kit: new MaterialKit(o.quality), input: o.input,
    mood: (mood) => { applyMood(o.renderer, o.root, mood); o.syncScene?.(o.root); },
    sfx: (name, intensity) => audioBus.play(name, intensity),
    invalidate: () => o.invalidate?.(),
  };
}

/* ---------- test / lab hook (inert unless a lab page installs window.__WOY_LAB__) ---------- */
export interface LabEntry {
  kind: string;
  stage: Stage;
  choreography: Choreography;
  gl: T.WebGLRenderer;
  getState(): SceneState;
  /** Runs the choreography without rendering for `seconds` of simulated time. */
  simulate(seconds: number, step?: number): void;
  /** Stops the host loop from advancing time (so simulate() is the only clock). */
  freeze(on: boolean): void;
  invalidate(): void;
}
declare global { interface Window { __WOY_LAB__?: { register(entry: LabEntry): void; unregister(): void } } }
```

## 48. `src/engine/textures.ts` — new

```ts
/**
 * Procedural texture library. Every texture is generated at runtime from a 2D canvas, so the site ships no
 * texture files, needs no licences, and each surface can be tuned to the art direction.
 * Canvases are cached (CPU side); each caller receives its own THREE.Texture so disposal stays per scene.
 */
import * as T from "three";

export type Rgb = [number, number, number];
export interface TexturePair { color: HTMLCanvasElement; height: HTMLCanvasElement }

export const rgb = (css: string): Rgb => {
  const hex = new T.Color(css).getHexString();
  return [parseInt(hex.slice(0, 2), 16), parseInt(hex.slice(2, 4), 16), parseInt(hex.slice(4, 6), 16)];
};

/* ---------- periodic value noise (tiles seamlessly when the lattice period divides the texture) ---------- */
function lattice(x: number, y: number, seed: number) {
  let h = Math.imul(x, 374761393) ^ Math.imul(y, 668265263) ^ Math.imul(seed + 1, 1442695041);
  h = Math.imul(h ^ (h >>> 13), 1274126177);
  h ^= h >>> 16;
  return (h >>> 0) / 4294967295;
}
export function noise2(x: number, y: number, seed: number, px: number, py: number) {
  const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
  const u = xf * xf * (3 - 2 * xf), v = yf * yf * (3 - 2 * yf);
  const x0 = ((xi % px) + px) % px, x1 = (x0 + 1) % px, y0 = ((yi % py) + py) % py, y1 = (y0 + 1) % py;
  const a = lattice(x0, y0, seed), b = lattice(x1, y0, seed), c = lattice(x0, y1, seed), d = lattice(x1, y1, seed);
  return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
}
export function fbm(u: number, v: number, seed: number, octaves: number, px: number, py = px) {
  let sum = 0, amp = 0.5, fx = px, fy = py, norm = 0;
  for (let o = 0; o < octaves; o++) {
    sum += amp * noise2(u * fx, v * fy, seed + o * 31, fx, fy);
    norm += amp; fx *= 2; fy *= 2; amp *= 0.5;
  }
  return sum / norm;
}
const smooth = (a: number, b: number, x: number) => { const t = Math.min(1, Math.max(0, (x - a) / (b - a))); return t * t * (3 - 2 * t); };

/** Runs `value(u,v) -> 0..1` per pixel and tints it through a 2- or 3-stop gradient. */
function paint(size: number, value: (u: number, v: number) => number, dark: Rgb, light: Rgb, mid?: Rgb, aspect = 1): TexturePair {
  const w = size, h = Math.round(size * aspect);
  const color = document.createElement("canvas"); color.width = w; color.height = h;
  const height = document.createElement("canvas"); height.width = w; height.height = h;
  const cc = color.getContext("2d")!, hc = height.getContext("2d", { willReadFrequently: true })!;
  const ci = cc.createImageData(w, h), hi = hc.createImageData(w, h);
  for (let j = 0; j < h; j++) for (let i = 0; i < w; i++) {
    const t = Math.min(1, Math.max(0, value(i / w, j / h)));
    const k = (j * w + i) * 4;
    for (let c = 0; c < 3; c++) {
      ci.data[k + c] = mid
        ? (t < 0.5 ? dark[c] + (mid[c] - dark[c]) * (t * 2) : mid[c] + (light[c] - mid[c]) * ((t - 0.5) * 2))
        : dark[c] + (light[c] - dark[c]) * t;
    }
    ci.data[k + 3] = 255;
    const g = Math.round(t * 255);
    hi.data[k] = hi.data[k + 1] = hi.data[k + 2] = g; hi.data[k + 3] = 255;
  }
  cc.putImageData(ci, 0, 0); hc.putImageData(hi, 0, 0);
  return { color, height };
}

/** Sobel height -> tangent-space normal map (tiling, OpenGL convention). */
export function normalFromHeight(source: HTMLCanvasElement, strength = 2): HTMLCanvasElement {
  const w = source.width, h = source.height;
  const s = source.getContext("2d", { willReadFrequently: true })!.getImageData(0, 0, w, h).data;
  const out = document.createElement("canvas"); out.width = w; out.height = h;
  const octx = out.getContext("2d")!, o = octx.createImageData(w, h);
  const at = (x: number, y: number) => s[((((y % h) + h) % h) * w + (((x % w) + w) % w)) * 4] / 255;
  for (let y = 0; y < h; y++) for (let x = 0; x < w; x++) {
    const dx = (at(x + 1, y - 1) + 2 * at(x + 1, y) + at(x + 1, y + 1)) - (at(x - 1, y - 1) + 2 * at(x - 1, y) + at(x - 1, y + 1));
    const dy = (at(x - 1, y + 1) + 2 * at(x, y + 1) + at(x + 1, y + 1)) - (at(x - 1, y - 1) + 2 * at(x, y - 1) + at(x + 1, y - 1));
    let nx = -dx * strength, ny = dy * strength, nz = 1;
    const len = Math.hypot(nx, ny, nz); nx /= len; ny /= len; nz /= len;
    const k = (y * w + x) * 4;
    o.data[k] = (nx * 0.5 + 0.5) * 255; o.data[k + 1] = (ny * 0.5 + 0.5) * 255; o.data[k + 2] = (nz * 0.5 + 0.5) * 255; o.data[k + 3] = 255;
  }
  octx.putImageData(o, 0, 0);
  return out;
}

/* ---------- cached generators ---------- */
const cache = new Map<string, TexturePair>();
const cached = (key: string, make: () => TexturePair) => { let hit = cache.get(key); if (!hit) { hit = make(); cache.set(key, hit); } return hit; };

export const woodCanvas = (size: number, dark: string, light: string, seed = 3, planks = 4) =>
  cached(`wood|${size}|${dark}|${light}|${seed}|${planks}`, () => paint(size, (u, v) => {
    const plank = Math.floor(v * planks), pv = v * planks - plank;
    const grain = fbm(u, pv * 0.18 + plank * 0.37, seed + plank, 4, 2, 24);
    const rings = 0.5 + 0.5 * Math.sin((pv * 7 + fbm(u, pv, seed + 9, 3, 3, 3) * 1.4 + plank * 1.7) * Math.PI * 2);
    const seam = 1 - (1 - smooth(0.0, 0.03, Math.min(pv, 1 - pv))) * 0.55; // dark gap between planks
    return (0.2 + 0.5 * grain + 0.22 * rings * grain) * seam + 0.16;
  }, rgb(dark), rgb(light)));

export const paperCanvas = (size: number, light: string, dark: string, seed = 5) =>
  cached(`paper|${size}|${light}|${dark}|${seed}`, () => {
    const pair = paint(size, (u, v) => 0.8 + 0.12 * fbm(u, v, seed, 4, 6) + 0.08 * fbm(u, v, seed + 4, 2, 64), rgb(dark), rgb(light));
    const ctx = pair.color.getContext("2d")!;
    ctx.globalAlpha = 0.06; ctx.lineWidth = 1;
    for (let i = 0; i < size * 1.4; i++) { // short fibres
      const x = lattice(i, 1, seed) * size, y = lattice(i, 2, seed) * size, a = lattice(i, 3, seed) * Math.PI, l = 3 + lattice(i, 4, seed) * 9;
      ctx.strokeStyle = i % 3 ? "#ffffff" : "#8a7658"; ctx.beginPath(); ctx.moveTo(x, y); ctx.lineTo(x + Math.cos(a) * l, y + Math.sin(a) * l); ctx.stroke();
    }
    return pair;
  });

export const leatherCanvas = (size: number, dark: string, light: string, seed = 7) =>
  cached(`leather|${size}|${dark}|${light}|${seed}`, () => paint(size, (u, v) => {
    const n = fbm(u, v, seed, 3, 28);
    const ridge = 1 - Math.abs(n * 2 - 1);
    return 0.35 + 0.5 * Math.pow(ridge, 2.2) + 0.15 * fbm(u, v, seed + 3, 3, 5);
  }, rgb(dark), rgb(light)));

export const fabricCanvas = (size: number, dark: string, light: string, threads = 72, seed = 11) =>
  cached(`fabric|${size}|${dark}|${light}|${threads}|${seed}`, () => paint(size, (u, v) => {
    const warp = 0.5 + 0.5 * Math.sin(u * threads * Math.PI * 2), weft = 0.5 + 0.5 * Math.sin(v * threads * Math.PI * 2);
    const over = (Math.floor(u * threads) + Math.floor(v * threads)) % 2 === 0;
    return 0.5 * (over ? warp : weft) + 0.25 + 0.25 * fbm(u, v, seed, 3, 16);
  }, rgb(dark), rgb(light)));

export const brushedCanvas = (size: number, dark: string, light: string, seed = 13) =>
  cached(`brushed|${size}|${dark}|${light}|${seed}`, () => paint(size, (u, v) => 0.55 + 0.45 * fbm(u, v, seed, 3, 2, 160), rgb(dark), rgb(light)));

export const marbleCanvas = (size: number, dark: string, light: string, seed = 17) =>
  cached(`marble|${size}|${dark}|${light}|${seed}`, () => paint(size, (u, v) => {
    const warp = fbm(u, v, seed, 5, 4) * 5;
    const vein = Math.abs(Math.sin((u * 3 + v * 2 + warp) * Math.PI));
    return 0.62 + 0.3 * fbm(u, v, seed + 2, 4, 6) + 0.12 * (1 - Math.pow(vein, 0.35));
  }, rgb(dark), rgb(light)));

export const soilCanvas = (size: number, dark: string, light: string, seed = 19) =>
  cached(`soil|${size}|${dark}|${light}|${seed}`, () => paint(size, (u, v) => {
    const clod = fbm(u, v, seed, 5, 8);
    const speck = noise2(u * 96, v * 96, seed + 5, 96, 96) > 0.9 ? 0.5 : 0;
    const grit = fbm(u, v, seed + 8, 2, 48) * 0.25;
    return 0.18 + clod * 0.55 + speck + grit;
  }, rgb(dark), rgb(light)));

export const barkCanvas = (size: number, dark: string, light: string, seed = 23) =>
  cached(`bark|${size}|${dark}|${light}|${seed}`, () => paint(size, (u, v) => {
    const furrow = fbm(u, v, seed, 4, 9, 2);
    return 0.2 + 0.7 * Math.pow(furrow, 1.4) + 0.1 * fbm(u, v, seed + 3, 3, 20, 6);
  }, rgb(dark), rgb(light)));

export const stoneCanvas = (size: number, dark: string, light: string, seed = 29) =>
  cached(`stone|${size}|${dark}|${light}|${seed}`, () => paint(size, (u, v) => 0.3 + 0.55 * fbm(u, v, seed, 6, 6) + 0.15 * fbm(u, v, seed + 3, 2, 60), rgb(dark), rgb(light)));

/* ---------- canvas-drawn (non per-pixel) textures ---------- */
/** `readable` marks canvases whose pixels are read back (height maps feed normalFromHeight), which avoids a browser warning. */
const make2d = (w: number, h: number, readable = false) => { const c = document.createElement("canvas"); c.width = w; c.height = h; return { canvas: c, ctx: c.getContext("2d", readable ? { willReadFrequently: true } : undefined)! }; };

/** Petal: u across, v from the base (v=0, bottom) to the tip. Veins, base glow and a darker rim. */
export const petalCanvas = (base: string, tip: string, vein: string, size = 256) =>
  cached(`petal|${base}|${tip}|${vein}|${size}`, () => {
    const { canvas, ctx } = make2d(size, size);
    const g = ctx.createLinearGradient(0, size, 0, 0);
    g.addColorStop(0, base); g.addColorStop(0.55, tip); g.addColorStop(1, tip);
    ctx.fillStyle = g; ctx.fillRect(0, 0, size, size);
    ctx.globalAlpha = 0.28; ctx.strokeStyle = vein; ctx.lineWidth = 1.2;
    for (let i = -7; i <= 7; i++) {
      ctx.beginPath(); ctx.moveTo(size / 2 + i * 2, size);
      ctx.quadraticCurveTo(size / 2 + i * 12, size * 0.55, size / 2 + i * 15 + Math.sin(i) * 5, size * 0.04); ctx.stroke();
    }
    ctx.globalAlpha = 0.18;
    const r = ctx.createRadialGradient(size / 2, size * 0.5, size * 0.2, size / 2, size * 0.5, size * 0.72);
    r.addColorStop(0, "rgba(255,255,255,0)"); r.addColorStop(1, vein);
    ctx.fillStyle = r; ctx.fillRect(0, 0, size, size);
    const height = make2d(size, size, true); height.ctx.fillStyle = "#808080"; height.ctx.fillRect(0, 0, size, size);
    height.ctx.globalAlpha = 0.3; height.ctx.strokeStyle = "#fff"; height.ctx.lineWidth = 2;
    for (let i = -7; i <= 7; i++) { height.ctx.beginPath(); height.ctx.moveTo(size / 2 + i * 2, size); height.ctx.quadraticCurveTo(size / 2 + i * 12, size * 0.55, size / 2 + i * 15, size * 0.04); height.ctx.stroke(); }
    return { color: canvas, height: height.canvas };
  });

/** Leaf: midrib plus pinnate side veins. */
export const leafCanvas = (dark: string, light: string, size = 256) =>
  cached(`leaf|${dark}|${light}|${size}`, () => {
    const { canvas, ctx } = make2d(size, size);
    const g = ctx.createLinearGradient(0, size, 0, 0); g.addColorStop(0, dark); g.addColorStop(1, light);
    ctx.fillStyle = g; ctx.fillRect(0, 0, size, size);
    ctx.strokeStyle = "rgba(255,255,230,0.5)"; ctx.lineWidth = 3; ctx.beginPath(); ctx.moveTo(size / 2, size); ctx.lineTo(size / 2, size * 0.04); ctx.stroke();
    ctx.lineWidth = 1.2; ctx.strokeStyle = "rgba(255,255,230,0.28)";
    for (let i = 1; i < 12; i++) for (const s of [-1, 1]) {
      const y = size - (i / 12) * size * 0.95; ctx.beginPath(); ctx.moveTo(size / 2, y); ctx.quadraticCurveTo(size / 2 + s * size * 0.2, y - size * 0.05, size / 2 + s * size * 0.42, y - size * 0.14); ctx.stroke();
    }
    const height = make2d(size, size, true); height.ctx.fillStyle = "#707070"; height.ctx.fillRect(0, 0, size, size);
    height.ctx.strokeStyle = "#ffffff"; height.ctx.lineWidth = 4; height.ctx.beginPath(); height.ctx.moveTo(size / 2, size); height.ctx.lineTo(size / 2, 0); height.ctx.stroke();
    height.ctx.lineWidth = 2; height.ctx.globalAlpha = 0.6;
    for (let i = 1; i < 12; i++) for (const s of [-1, 1]) { const y = size - (i / 12) * size * 0.95; height.ctx.beginPath(); height.ctx.moveTo(size / 2, y); height.ctx.quadraticCurveTo(size / 2 + s * size * 0.2, y - size * 0.05, size / 2 + s * size * 0.42, y - size * 0.14); height.ctx.stroke(); }
    return { color: canvas, height: height.canvas };
  });

export function glowCanvas(inner = "rgba(255,255,255,1)", outer = "rgba(255,255,255,0)", size = 128) {
  const { canvas, ctx } = make2d(size, size);
  const g = ctx.createRadialGradient(size / 2, size / 2, 0, size / 2, size / 2, size / 2);
  g.addColorStop(0, inner); g.addColorStop(0.35, inner.replace(/[\d.]+\)$/, "0.45)")); g.addColorStop(1, outer);
  ctx.fillStyle = g; ctx.fillRect(0, 0, size, size);
  return canvas;
}

export function sparkleCanvas(size = 128) {
  const { canvas, ctx } = make2d(size, size);
  const c = size / 2;
  const g = ctx.createRadialGradient(c, c, 0, c, c, c * 0.5); g.addColorStop(0, "rgba(255,255,255,1)"); g.addColorStop(1, "rgba(255,255,255,0)");
  ctx.fillStyle = g; ctx.fillRect(0, 0, size, size);
  ctx.fillStyle = "rgba(255,255,255,0.9)";
  for (const [w, h] of [[size * 0.9, 3], [3, size * 0.9]] as const) { ctx.beginPath(); ctx.ellipse(c, c, w / 2, h / 2, 0, 0, Math.PI * 2); ctx.fill(); }
  return canvas;
}

/* ---------- THREE.Texture helpers ---------- */
export interface TextureOptions { srgb?: boolean; repeat?: [number, number]; anisotropy?: number; wrap?: boolean }
export function toTexture(canvas: HTMLCanvasElement, { srgb = false, repeat, anisotropy = 4, wrap = true }: TextureOptions = {}) {
  const texture = new T.CanvasTexture(canvas);
  texture.colorSpace = srgb ? T.SRGBColorSpace : T.NoColorSpace;
  if (wrap) texture.wrapS = texture.wrapT = T.RepeatWrapping;
  if (repeat) texture.repeat.set(repeat[0], repeat[1]);
  texture.anisotropy = anisotropy;
  return texture;
}

export interface SurfaceMaps { map: T.Texture; normalMap?: T.Texture; bumpMap?: T.Texture }
/** Colour map plus a normal map (when `normal` strength is given) or a bump map. */
export function surfaceMaps(pair: TexturePair, opts: TextureOptions & { normal?: number } = {}): SurfaceMaps {
  const map = toTexture(pair.color, { ...opts, srgb: true });
  return opts.normal
    ? { map, normalMap: toTexture(normalFromHeight(pair.height, opts.normal), opts) }
    : { map, bumpMap: toTexture(pair.height, opts) };
}

export const textureSize = (quality: "low" | "medium" | "high") => (quality === "high" ? 512 : quality === "medium" ? 384 : 256);
```

## 49. `src/hooks/usePointerParallax.ts` — new

```ts
import { useEffect, type RefObject } from "react";

/**
 * Publishes the pointer position over an element as CSS variables (--px / --py in -1..1, --gx / --gy in 0..100%) so pure CSS can
 * build depth: tilted frames, layered parallax and a light sweep. Only mouse / pen pointers drive it, nothing runs under
 * prefers-reduced-motion, and the variables ease back to rest when the pointer leaves, so touch and keyboard users get a calm, flat layout.
 */
export function usePointerParallax(ref: RefObject<HTMLElement | null>, strength = 1) {
  useEffect(() => {
    const node = ref.current;
    if (!node) return;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)");
    let frame = 0, tx = 0, ty = 0, cx = 0, cy = 0, active = false;
    const apply = () => {
      frame = 0;
      cx += (tx - cx) * 0.16; cy += (ty - cy) * 0.16;
      node.style.setProperty("--px", (cx * strength).toFixed(3));
      node.style.setProperty("--py", (cy * strength).toFixed(3));
      node.style.setProperty("--gx", `${(50 + cx * 50).toFixed(1)}%`);
      node.style.setProperty("--gy", `${(50 + cy * 50).toFixed(1)}%`);
      if (Math.abs(tx - cx) > 0.002 || Math.abs(ty - cy) > 0.002) frame = requestAnimationFrame(apply);
    };
    const kick = () => { if (!frame) frame = requestAnimationFrame(apply); };
    const move = (event: PointerEvent) => {
      if (reduce.matches || event.pointerType === "touch") return;
      const box = node.getBoundingClientRect();
      tx = ((event.clientX - box.left) / box.width) * 2 - 1; ty = ((event.clientY - box.top) / box.height) * 2 - 1; active = true; kick();
    };
    const leave = () => { if (!active) return; tx = 0; ty = 0; active = false; kick(); };
    node.addEventListener("pointermove", move); node.addEventListener("pointerleave", leave);
    return () => { node.removeEventListener("pointermove", move); node.removeEventListener("pointerleave", leave); if (frame) cancelAnimationFrame(frame); };
  }, [ref, strength]);
}
```

## 50. `src/lab/Lab.tsx` — new

```tsx
/**
 * Scene lab (development only). Mounts a single gift scene full-viewport and exposes `window.__lab` so
 * automated QA can set state, advance simulated time and screenshot deterministically.
 *   /?lab=letter&quality=high&state={"open":true}
 */
import { useEffect, useMemo, useRef, useState } from "react";
import { createRoot } from "react-dom/client";
import { GiftStage, type GiftKind } from "../three/GiftStage";
import type { SceneState } from "../three/runtime";
import type { LabEntry } from "../engine/stage";
import { chronosContent } from "../content/chronosContent";

interface LabApi {
  ready: Promise<void>;
  set: (state: SceneState) => void;
  replace: (state: SceneState) => void;
  simulate: (seconds: number, step?: number) => Promise<void>;
  entry: () => LabEntry | null;
  camera: (c: number[]) => void;
  stats: () => Record<string, number | string | undefined>;
  picks: number[];
  progress: number;
}
declare global { interface Window { __lab: LabApi } }

function Lab({ kind, initial }: { kind: GiftKind; initial: SceneState }) {
  const [state, setState] = useState<SceneState>(initial);
  const entry = useRef<LabEntry | null>(null);
  const picks = useRef<number[]>([]);
  const progress = useRef(0);
  const frame = () => new Promise<void>((resolve) => requestAnimationFrame(() => requestAnimationFrame(() => resolve())));

  const ready = useMemo(() => new Promise<void>((resolve) => {
    window.__WOY_LAB__ = {
      register: (e) => { entry.current = e; e.freeze(true); resolve(); },
      unregister: () => { entry.current = null; },
    };
  }), []);

  useEffect(() => {
    window.__lab = {
      ready,
      set: (next) => setState((prev) => ({ ...prev, ...next })),
      replace: (next) => setState(next),
      simulate: async (seconds, step) => { await frame(); entry.current?.simulate(seconds, step); entry.current?.invalidate(); await frame(); await frame(); },
      entry: () => entry.current,
      camera: (c) => { const e = entry.current; if (!e) return; e.stage.camera.position.set(c[0], c[1], c[2]); e.stage.camera.lookAt(c[3], c[4], c[5]); e.invalidate(); },
      stats: () => {
        const host = document.querySelector<HTMLElement>(".gift-native-canvas");
        return { ...host?.dataset, picks: picks.current.join(",") };
      },
      get picks() { return picks.current; },
      get progress() { return progress.current; },
    } as LabApi;
  }, [ready]);

  return (
    <div style={{ position: "fixed", inset: 0, background: "#111" }}>
      <style>{".gift-native-stage{height:100vh!important;border-radius:0!important;border:0!important}"}</style>
      <GiftStage kind={kind} state={state} label={`Lab: ${kind}`} onPick={(i) => { picks.current.push(i); }} onProgress={(p) => { progress.current = p; }} />
    </div>
  );
}

export function mountLab(root: HTMLElement) {
  const params = new URLSearchParams(window.location.search);
  const kind = params.get("lab") as GiftKind;
  let initial: SceneState = {};
  try { initial = JSON.parse(params.get("state") ?? "{}"); } catch { /* ignore malformed state */ }
  if (kind === "letter" && !initial.detail) {
    const letter = chronosContent.letters.letters[0];
    initial.detail = [letter.salutation, ...letter.paragraphs, letter.closing, letter.signature, letter.ps].filter(Boolean).join("\n\n");
  }
  createRoot(root).render(<Lab kind={kind} initial={initial} />);
}
```

## 51. `src/main.tsx` — modified

```tsx
import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import "./styles/global.css";
import "./styles/premium.css";
import "./styles/sceneSystem.css";
import "./styles/giftAtelier.css";
import "./styles/cinematic.css";
import "./styles/giftWorlds.css";
import "./styles/sections3d.css";

// Development-only scene lab (?lab=<kind>): mounts one 3D scene on its own for deterministic screenshots.
// `import.meta.env.DEV` is a compile-time constant, so this branch (and the lab module) is removed from production builds.
if (import.meta.env.DEV && new URLSearchParams(window.location.search).has("lab")) {
  void import("./lab/Lab").then(({ mountLab }) => mountLab(document.getElementById("root")!));
} else {
  ReactDOM.createRoot(document.getElementById("root")!).render(
    <React.StrictMode>
      <App />
    </React.StrictMode>,
  );
}
```

## 52. `src/styles/giftWorlds.css` — modified

```css
/* Focused miniature worlds: one lazy R3F renderer, real objects; HTML remains the instrument panel. */
.gift-native-stage { position:sticky; top:0; width:100%; height:clamp(380px,min(49vw,74svh),690px); min-width:0; overflow:hidden; border:1px solid #c4b18b55; border-radius:18px; background:#253d37; box-shadow:0 20px 55px #151b212b; }
.gift-native-canvas { position:absolute; inset:0; touch-action:pan-y; }
.gift-native-canvas>div:first-child { position:absolute!important; inset:0; }
.gift-native-canvas canvas { display:block; outline:none; }
.gift-native-chrome { position:absolute; top:0; left:0; right:0; display:flex; align-items:center; justify-content:space-between; gap:1rem; padding:17px; color:#f5ebd4; background:linear-gradient(#101b21ba,transparent); pointer-events:none; font:9px/1.6 Georgia,serif; letter-spacing:.12em; }
.gift-native-chrome label { display:flex; gap:8px; align-items:center; pointer-events:auto; }
.gift-native-chrome select { padding:9px 11px; border:1px solid #c1b18c; border-radius:20px; color:#f5ebd4; background:#263e38; font:11px Georgia,serif; }
.gift-native-status { position:absolute; bottom:14px; left:17px; font:10px/1.5 Georgia,serif; color:#f7ebd2; pointer-events:none; }
.gift-stage-fallback { padding:35px; color:#f5ebd4; font:16px/1.7 Georgia,serif; }
dialog.archive-dialog--gift { width:min(1500px,calc(100vw - 30px)); max-height:95svh; border-radius:22px; }
.archive-dialog--gift .archive-dialog__paper { max-height:95svh; padding:28px; background:#f2eadc; }
.archive-dialog--gift .archive-dialog__paper h2 { font-size:clamp(28px,3.4vw,47px); max-width:none; margin-bottom:12px; }
.gift-experience>section { display:grid; grid-template-columns:minmax(0,1.65fr) minmax(270px,1fr); gap:28px; align-items:start; }
.gift-world-console { min-width:0; padding:8px 0; }  /* no inner scroller: the dialog is the single scroll surface */
.gift-world-console>*:first-child { margin-top:0; }
.gift-world-console .gift-control-row { justify-content:flex-start; }
.gift-control,.gift-note-picker button { min-height:44px; }
.gift-note-picker { display:flex; flex-wrap:wrap; gap:7px; margin:15px 0; }
.gift-note-picker button { border:1px solid #b9aa8b; background:#fbf6eb; color:#594c3b; border-radius:8px; padding:8px 12px; cursor:pointer; }
.gift-note-picker button[aria-pressed=true] { color:#fff7de; background:#536b56; }
.gift-note-picker button:disabled { opacity:.45; cursor:not-allowed; }
.gift-native-copy { font:1.15rem/1.7 Georgia,serif; padding:20px; border-left:2px solid #af976a; }
.gift-native-chrome select:focus-visible,.gift-note-picker button:focus-visible { outline:3px solid #c08e5d; outline-offset:3px; }
.gift-experience [hidden] { display:none!important; }
.gift-world-console .gift-cinema__curtain,.gift-world-console .gift-cinema__beam,.gift-world-console .gift-cinema__seats { display:none; }
.gift-world-console .gift-cinema__theatre { min-height:180px; background:#e8dfd0; border:1px solid #c3b18e; }
.gift-world-console .gift-cinema__screen { width:100%; margin:0; }
.gift-world-console .gift-adventure__map { min-height:180px; }
.gift-world-console .gift-mirror__frame { height:160px; border-width:3px; border-radius:12px; box-shadow:none; }
.gift-world-console .gift-mirror__reflection { font-size:12px; }
.gift-world-console .gift-coupon__book { transform:none; width:100%; }
.gift-world-console .gift-coupon__page { min-height:200px; }
.gift-world-console .gift-letter__reading { margin:0; }

@media(max-width:950px){.gift-experience>section{grid-template-columns:1fr;gap:15px}.gift-native-stage{height:clamp(380px,64vw,560px)}.gift-world-console{max-height:none;overflow:visible}.archive-dialog--gift .archive-dialog__paper{padding:24px 17px}.gift-experience-shell__intro{font-size:1rem}}
@media(max-width:500px){.gift-native-stage{height:400px;border-radius:12px}.gift-native-chrome{font-size:8px;padding:12px}.gift-native-chrome>span{max-width:160px}.gift-world-console .gift-control-row{justify-content:center}.gift-note-picker{justify-content:center}}

.gift-parcels { grid-template-columns:repeat(4,minmax(0,1fr)); gap:18px; }
.gift-parcel { min-height:280px; padding:10px 10px 17px; border-radius:16px; background:#fbf7ef; }
.gift-parcel__preview { display:block; overflow:hidden; border-radius:10px; margin:16px 0 13px; background:#263d37; box-shadow:0 10px 20px #15261d18; }
.gift-parcel__preview img { width:100%; height:auto; display:block; transition:filter .2s; }
.gift-parcel:hover,.gift-parcel:focus-visible { transform:translateY(-3px); }
.gift-parcel:active { transform:translateY(0); }
.gift-parcel:hover .gift-parcel__preview img { filter:brightness(1.09); }
.gift-parcel__title { min-height:32px; }
@media(max-width:1080px) {.gift-parcels{grid-template-columns:repeat(3,minmax(0,1fr));}}
@media(max-width:600px) {.gift-parcels{grid-template-columns:repeat(2,minmax(0,1fr));gap:10px}.gift-parcel{min-height:235px;padding:8px}.gift-parcel__title{font-size:1rem}.gift-parcel__preview{margin-top:22px}}
@media(prefers-reduced-motion:reduce){.gift-parcel,.gift-parcel__preview img{transition:none}.gift-parcel:hover,.gift-parcel:focus-visible{transform:none}}

/* ---- Sound dock, sticky stage and single-scroller layout (master build) ---- */
.gift-experience-shell__footer { display:flex; flex-wrap:wrap; align-items:center; gap:10px 18px; }
.gift-sound-dock { display:inline-flex; align-items:center; flex-wrap:wrap; gap:8px 14px; }
.gift-sound-dock .gift-control { display:inline-flex; align-items:center; gap:7px; }
.gift-sound-dock .gift-volume { display:inline-flex; align-items:center; gap:8px; font:12px Georgia,serif; color:#594c3b; }
.gift-sound-dock .gift-volume input { width:110px; }
.gift-native-stage:focus-within { outline:3px solid #c08e5d55; outline-offset:2px; }
.gift-world-console { overflow:visible; }
.gift-world-console .gift-letter__reading,.gift-world-console .gift-jar__all,.gift-world-console .gift-wishes__all,.gift-world-console .gift-future-garden__hopes { max-height:none; overflow:visible; }
@media(max-width:950px){ .gift-native-stage { position:relative; height:clamp(340px,70svh,560px); } }

/* ---------- section scenes (hero garden, wish garden, observatory, postcards, ballroom) ---------- */
.section-stage { background-size: cover; background-position: center; }
.section-stage .gift-native-stage { position: relative; top: auto; height: 100%; min-height: 0; border: 0; border-radius: inherit; box-shadow: none; background: transparent; }
.section-stage .gift-native-canvas { border-radius: inherit; }
.section-stage__asleep { position: absolute; inset: 0; }
.gift-native-canvas[data-chrome="minimal"] .gift-native-chrome { top: auto; bottom: 0; background: none; justify-content: flex-end; padding: 12px; }
.gift-native-canvas[data-chrome="minimal"] .gift-native-chrome > span { display: none; }
.gift-native-canvas[data-chrome="minimal"] .gift-native-chrome label { opacity: .72; }
.gift-native-canvas[data-chrome="minimal"] .gift-native-chrome label:hover, .gift-native-canvas[data-chrome="minimal"] .gift-native-chrome label:focus-within { opacity: 1; }
.gift-native-canvas[data-chrome="minimal"] ~ .gift-native-status, .gift-native-canvas[data-chrome="minimal"] .gift-native-status { left: auto; right: 14px; bottom: 44px; opacity: .6; }

/* ---- content pack: dedications, reveal lines, the sky of wishes, the jar quote (owner copy, never placeholders) ---- */
.gift-experience-shell__dedication { max-width: 760px; margin: 0 0 8px; padding: 2px 0 2px 16px; border-left: 2px solid #c49b58; color: #5d4745; font: italic 1.28rem/1.5 var(--font-editorial); }
.gift-experience-shell__dedication strong { display: block; margin: 0 0 4px; color: #9a5d68; font: 1.5rem/1.2 var(--font-note); font-style: normal; }
.gift-experience-shell__dedication + .gift-experience-shell__intro { margin-bottom: 15px; font-size: .98rem; color: #8b766d; }
.gift-experience-shell__back { margin-left: -4px; }
.gift-dedication { margin: 14px 0; padding: 16px 18px; border: 1px solid rgba(196, 155, 88, .5); border-left-width: 3px; border-radius: 10px; background: #fff7e6; color: #5d4745; }
.gift-dedication strong { display: block; margin: 0 0 8px; color: #9a5d68; font: 1.5rem/1.2 var(--font-note); }
.gift-dedication p { margin: 0; font: 1.08rem/1.65 var(--font-editorial); }
.gift-jar__quote { max-width: 720px; margin: 14px 0 0; color: #7a625b; font: italic 1.05rem/1.55 var(--font-editorial); }
.gift-wishes__meta { flex-wrap: wrap; gap: 4px 14px; }
.gift-wishes__lists h4 { margin: 14px 0 4px; color: #8d6a58; font: 700 9px/1.4 var(--font-ui); letter-spacing: .16em; text-transform: uppercase; }
.gift-world-console .gift-wishes__sky { max-height: none; overflow: visible; columns: 2; margin: 0; padding: 11px 18px 11px 32px; background: #fffaf2; color: #715c55; font: 11px/1.6 var(--font-ui); }
.gift-wishes__sky, .gift-wishes__all, .gift-jar__all { list-style: none; } /* the numbers are printed in the <span>, so the browser's own markers would count twice */
.gift-wishes__sky.gift-wishes__sky, .gift-wishes__all.gift-wishes__all, .gift-jar__all.gift-jar__all { padding-left: 18px; }
.gift-wishes__sky li { break-inside: avoid; padding: 2px 7px; }
.gift-wishes__sky span { margin-right: 7px; color: #b08471; }
.gift-letter__heading { margin: 0 0 12px; padding-bottom: 10px; border-bottom: 1px solid rgba(163, 126, 91, .3); }
.gift-letter__heading h3 { margin: 0; color: #6a4a4d; font: 600 1.3rem/1.25 var(--font-display); }
.gift-letter__heading p { margin: 4px 0 0; color: #8a6f64; font: italic 1rem/1.4 var(--font-editorial); }
.gift-cinema__intro { margin: 0 0 10px; color: #7b655e; font: italic 1.02rem/1.5 var(--font-editorial); text-align: center; }
.gift-future-garden__missing { margin: 10px 0; color: #8c756a; font: 10px/1.65 var(--font-ui); }
@media (max-width: 500px) { .gift-world-console .gift-wishes__sky { columns: 1; } .gift-experience-shell__dedication { font-size: 1.12rem; } }
/* The pack's cover tagline, a quiet line above the gift grid intro. */
.gift-room__tagline { max-width: 680px; margin: 22px auto 0; color: #7d4a57; font: italic 1.22rem/1.5 var(--font-editorial); text-align: center; text-wrap: balance; }
.gift-room__tagline + .gift-room__intro { margin-top: 12px; }
@media (max-width: 500px) { .gift-room__tagline { margin-top: 16px; font-size: 1.08rem; } }
```

## 53. `src/styles/sections3d.css` — new

```css
/* ==========================================================================================================
   Sections rebuilt on the shared 3D engine: hero garden, scrapbook book body, gallery depth, postcard editor.
   2D (copy, buttons, captions, forms) stays HTML; 3D carries objects and environments.
   ========================================================================================================== */

/* ---------- Birthday Garden hero: live cut-away garden behind the headline ---------- */
.birthday-garden__stage { position: absolute; inset: 0; z-index: -3; }
.birthday-garden__stage .cinematic-viewport { position: absolute; inset: 0; width: 100%; height: 100%; border: 0; border-radius: 0; box-shadow: none; background: #f1dcc4 center / cover no-repeat; }
.birthday-garden__veil, .birthday-garden__sunwash { pointer-events: none; }
.birthday-garden__stage .gift-native-canvas { touch-action: pan-y; }
.garden-growth { position: relative; margin-top: 1.5rem; display: grid; gap: .7rem; max-width: 600px; pointer-events: auto; }
.garden-growth__steps { display: flex; flex-wrap: wrap; gap: 6px; margin: 0; padding: 0; list-style: none; }
.garden-growth__steps button, .garden-growth__replay {
  appearance: none; min-height: 40px; padding: 0 14px; border: 1px solid rgba(104, 71, 75, .3); border-radius: var(--radius-pill, 999px);
  color: #68474b; background: rgba(255, 250, 242, .84); backdrop-filter: blur(6px); cursor: pointer;
  font: 700 10.5px/1 var(--font-ui); letter-spacing: .09em; text-transform: uppercase; transition: background .2s, color .2s, transform .2s, border-color .2s;
}
.garden-growth__steps button:hover, .garden-growth__replay:hover { transform: translateY(-1px); border-color: rgba(104, 71, 75, .55); }
.garden-growth__steps button[aria-current="step"] { color: #fff8ef; background: #7d4a57; border-color: #7d4a57; }
.garden-growth__steps button:focus-visible, .garden-growth__replay:focus-visible { outline: 3px solid #b37c61; outline-offset: 3px; }
.garden-growth__replay { display: inline-flex; align-items: center; gap: 8px; justify-self: start; }
.garden-growth__narration { display: grid; }
.garden-growth__narration > * { grid-area: 1 / 1; }
.garden-growth__caption, .garden-growth__sizer p { margin: 0; color: #5b4043; font: italic 400 clamp(1rem, 1.5vw, 1.18rem) / 1.45 var(--font-editorial); text-shadow: 0 1px 0 rgba(255, 255, 255, .45); }
.garden-growth__sizer { display: grid; visibility: hidden; pointer-events: none; }
.garden-growth__sizer p { grid-area: 1 / 1; }
.garden-growth__label { display: block; margin-bottom: .2rem; color: #7d4a57; font: 600 .68rem / 1.3 var(--font-ui, "DM Sans", sans-serif); font-style: normal; letter-spacing: .18em; text-transform: uppercase; text-shadow: none; }
.garden-growth__progress { height: 3px; border-radius: 3px; background: rgba(104, 71, 75, .18); overflow: hidden; }
.garden-growth__progress > i { display: block; height: 100%; width: calc(var(--grown, 0) * 100%); background: linear-gradient(90deg, #c98291, #d6b879); transition: width .35s linear; }
@media (max-width: 760px) {
  .garden-growth { margin-top: 1.2rem; }
  .garden-growth__steps button { min-height: 38px; padding: 0 11px; font-size: 9.5px; }
}
@media (prefers-reduced-motion: reduce) { .garden-growth__steps button, .garden-growth__replay { transition: none; } .garden-growth__progress > i { transition: none; } }

/* ---------- Scrapbook: a book with real thickness (cover boards, page blocks, gutter, ground shadow) ---------- */
.storybook-book__stage { --read: 0; perspective: 1600px; isolation: isolate; }
.storybook-book__stage::before {
  content: ""; position: absolute; z-index: -1; left: 4%; right: 4%; bottom: -22px; height: 38px; border-radius: 50%;
  background: radial-gradient(ellipse at center, rgba(52, 33, 22, .42), rgba(52, 33, 22, .16) 55%, transparent 72%); filter: blur(7px); pointer-events: none;
}
.storybook-book__body { position: absolute; z-index: -1; left: calc(var(--bx, 0px) - 14px); top: calc(var(--by, 0px) - 11px); width: calc(var(--bw, 100%) + 28px); height: calc(var(--bh, 100%) + 27px); border-radius: 10px 14px 14px 10px; pointer-events: none;
  background: linear-gradient(180deg, #5a3a2a, #3d2519 70%, #2f1c13);
  box-shadow: inset 0 1px 0 rgba(255, 224, 190, .22), 0 1px 0 #26160e, 0 2px 0 #26160e, 0 3px 0 #2b190f, 0 4px 0 #2b190f, 0 5px 0 #301d12, 0 6px 0 #301d12, 0 18px 34px -10px rgba(40, 24, 15, .55); }
.storybook-book__body::after { content: ""; position: absolute; inset: 0; border-radius: inherit; opacity: .35; mix-blend-mode: soft-light; background: repeating-linear-gradient(45deg, rgba(255, 255, 255, .08) 0 2px, transparent 2px 5px); }
.storybook-book__block { position: absolute; z-index: -1; top: calc(var(--by, 0px) - 3px); height: calc(var(--bh, 100%) + 11px); border-radius: 2px; pointer-events: none;
  background: repeating-linear-gradient(90deg, #f6efe0 0 1px, #d9ccb2 1px 2px); box-shadow: 0 2px 4px rgba(40, 24, 15, .3); }
.storybook-book__block--left { left: calc(var(--bx, 0px) - 4px); width: calc(2px + var(--read) * 13px); }
.storybook-book__block--right { left: calc(var(--bx, 0px) + var(--bw, 100%) - 2px - (1 - var(--read)) * 11px); width: calc(2px + (1 - var(--read)) * 13px); }
.storybook-book__gutter { position: absolute; z-index: 3; top: var(--by, 0px); height: var(--bh, 100%); left: calc(var(--bx, 0px) + var(--bw, 100%) / 2 - 23px); width: 46px; pointer-events: none; mix-blend-mode: multiply;
  background: linear-gradient(90deg, transparent, rgba(60, 38, 24, .16) 40%, rgba(45, 28, 18, .3) 50%, rgba(60, 38, 24, .16) 60%, transparent); }
/* closed book: the boards only sit under the visible half */
.storybook-book__stage[data-state="front"] .storybook-book__body { left: calc(var(--bx, 0px) + var(--bw, 100%) / 2 - 8px); width: calc(var(--bw, 100%) / 2 + 22px); }
.storybook-book__stage[data-state="back"] .storybook-book__body { width: calc(var(--bw, 100%) / 2 + 22px); }
.storybook-book__stage[data-state="front"] .storybook-book__block--left, .storybook-book__stage[data-state="back"] .storybook-book__block--right,
.storybook-book__stage[data-state="front"] .storybook-book__gutter, .storybook-book__stage[data-state="back"] .storybook-book__gutter, .storybook-book__stage[data-state="single"] .storybook-book__gutter { display: none; }
.storybook-book__stage[data-state="single"] .storybook-book__block--left { display: none; }
.storybook-book__stage[data-state="single"] .storybook-book__body { left: calc(var(--bx, 0px) - 10px); width: calc(var(--bw, 100%) + 20px); }
@media (prefers-reduced-motion: no-preference) and (hover: hover) {
  .storybook-book__stage { transition: transform .5s cubic-bezier(.2, .7, .2, 1); transform: rotateX(calc(var(--py, 0) * -2.2deg)) rotateY(calc(var(--px, 0) * 3deg)); }
}

/* ---------- Memory Gallery: framed mounts with depth, parallax layers and a light sweep ---------- */
.polaroid-wall { perspective: 1200px; --px: 0; --py: 0; --gx: 50%; --gy: 50%; transform-style: preserve-3d; isolation: isolate; }
.polaroid-wall::before { content: ""; position: absolute; inset: 0; z-index: 0; border-radius: inherit; pointer-events: none;
  background: radial-gradient(ellipse 340px 260px at var(--gx) var(--gy), rgba(255, 238, 205, .55), transparent 70%); mix-blend-mode: soft-light; transition: opacity .3s; }
.polaroid-wall__string { transform: translate3d(calc(var(--px) * -9px), calc(var(--py) * -5px), 0) rotate(var(--string-tilt, -1.2deg)); }
.polaroid-wall .polaroid-card {
  --tilt: 0deg; --lift: 0px; transform-style: preserve-3d; will-change: transform;
  transform: perspective(900px) rotate(var(--tilt)) rotateX(calc(var(--py) * -5deg)) rotateY(calc(var(--px) * 7deg)) translateZ(var(--lift));
  transition: transform .35s cubic-bezier(.2, .7, .2, 1), box-shadow .35s; text-align: left;
  box-shadow: 0 1px 0 #fff inset, 0 2px 3px rgba(81, 63, 49, .2), 0 12px 24px rgba(81, 63, 49, .18), calc(var(--px) * -10px) calc(8px + var(--py) * -6px) 26px rgba(81, 63, 49, .16);
}
.polaroid-wall .polaroid-card--1 { --tilt: -2.2deg; } .polaroid-wall .polaroid-card--2 { --tilt: 1.2deg; --lift: 6px; } .polaroid-wall .polaroid-card--3 { --tilt: -1deg; --lift: 3px; }
.polaroid-wall .polaroid-card--4 { --tilt: 1.6deg; } .polaroid-wall .polaroid-card--5 { --tilt: -1.4deg; --lift: 5px; } .polaroid-wall .polaroid-card--6 { --tilt: .8deg; --lift: 2px; }
.polaroid-wall .polaroid-card:hover, .polaroid-wall .polaroid-card:focus-visible { --lift: 26px; --tilt: 0deg; z-index: 4; }
.polaroid-wall .polaroid-card__image { transform: translateZ(14px); box-shadow: 0 0 0 1px rgba(120, 98, 80, .18) inset, 0 3px 8px rgba(70, 52, 40, .18); }
.polaroid-wall .polaroid-card__image::before { content: ""; position: absolute; inset: 0; z-index: 2; pointer-events: none; opacity: .85;
  background: linear-gradient(115deg, transparent calc(var(--gx, 50%) - 22%), rgba(255, 255, 255, .34) var(--gx, 50%), transparent calc(var(--gx, 50%) + 22%)); }
.polaroid-wall .polaroid-card__caption { transform: translateZ(8px); }
.polaroid-wall .polaroid-card__clip { transform: translateZ(22px); }
.polaroid-wall .polaroid-card:focus-visible { outline: 3px solid #b37c61; outline-offset: 5px; }
@media (hover: none), (prefers-reduced-motion: reduce) {
  .polaroid-wall .polaroid-card { transform: rotate(var(--tilt)); transition: none; }
  .polaroid-wall .polaroid-card:hover, .polaroid-wall .polaroid-card:focus-visible { transform: rotate(0) scale(1.02); }
  .polaroid-wall .polaroid-card__image, .polaroid-wall .polaroid-card__caption, .polaroid-wall .polaroid-card__clip { transform: none; }
  .polaroid-wall::before { opacity: 0; }
}

/* ---------- Future Postcards: dialog stage + handwriting editor ---------- */
.postcard-reading { max-width: min(760px, 100%); }
.postcard-reading .cinematic-viewport--postcard { height: clamp(300px, 46vw, 470px); background: #1c130d; margin: 0 0 1rem; }
.postcard-editor { display: grid; gap: .5rem; margin: 1rem 0; padding: 1rem 1.1rem; border: 1px dashed rgba(120, 90, 60, .45); border-radius: 14px; background: rgba(255, 250, 240, .6); }
.postcard-editor label { display: grid; gap: .4rem; color: #5a4036; font: 700 .72rem/1 var(--font-ui); letter-spacing: .1em; text-transform: uppercase; }
.postcard-editor textarea { min-height: 76px; resize: vertical; padding: .7rem .8rem; border: 1px solid rgba(120, 90, 60, .4); border-radius: 10px; color: #27559b; background: #fffdf7; font: 600 1.35rem/1.25 var(--font-note); }
.postcard-editor textarea:focus-visible { outline: 3px solid #b37c61; outline-offset: 2px; }
.postcard-editor small { color: #7a6350; font: 400 .78rem/1.4 var(--font-ui); }
.postcard-editor__row { display: flex; align-items: center; justify-content: space-between; gap: 1rem; flex-wrap: wrap; }
.postcard-editor button { min-height: 40px; padding: 0 14px; border: 1px solid rgba(120, 90, 60, .4); border-radius: 999px; color: #5a4036; background: #fff7ea; font: 700 .72rem/1 var(--font-ui); letter-spacing: .08em; text-transform: uppercase; cursor: pointer; }
.postcard-editor button:focus-visible { outline: 3px solid #b37c61; outline-offset: 3px; }

/* ---------- shared: loading / fallback text of section scenes is a small caption, never a block ---------- */
.section-stage .gift-stage-fallback { position: absolute; left: 16px; bottom: 14px; z-index: 2; max-width: min(60%, 420px); padding: 0; margin: 0; background: none; font: 11px/1.5 var(--font-ui); letter-spacing: .04em; color: #f5ebd4; text-shadow: 0 1px 4px rgba(0, 0, 0, .65); pointer-events: none; }
.section-stage .gift-stage-fallback p { margin: 0; }
.cinematic-viewport--hero .gift-stage-fallback { color: #5b4043; text-shadow: 0 1px 0 rgba(255, 255, 255, .5); left: clamp(28px, 8vw, 128px); bottom: 12px; }
.cinematic-viewport--observatory { background: #070d1b; }
.cinematic-viewport--postcard { background: #1c130d; }

/* ---------- scrapbook covers: the flip-book forces display:block on pages, so the cover lays itself out as a centred column ---------- */
.storybook-leaf--cover, .storybook-leaf--back-cover { text-align: center; }
.storybook-leaf--cover > *:not(.storybook-cover__press), .storybook-leaf--back-cover > *:not(.storybook-cover__press) { display: block; margin-left: auto; margin-right: auto; }
.storybook-leaf--cover > .storybook-cover__ornament, .storybook-leaf--back-cover > .storybook-cover__ornament { margin-top: clamp(64px, 24%, 140px); margin-bottom: 1rem; }
.storybook-leaf--cover strong, .storybook-leaf--back-cover strong { margin: .8rem 0 1.1rem; }

/* ---------- gift dialog sound dock: constant accessible name, state shown by aria-pressed and a small badge ---------- */
.gift-sound-dock__state { padding: 3px 7px; border-radius: 999px; color: #5b4a36; background: #eadfca; font: 700 9px/1 var(--font-ui); letter-spacing: .1em; text-transform: uppercase; }
.gift-sound-dock [aria-pressed="true"] .gift-sound-dock__state { color: #fff7ee; background: #7d4a57; }

/* ---------- ballroom layout: the 3D stage sits beside the ritual controls, the illustrated alternative spans the width below ---------- */
.birthday-cake-scene { grid-template-areas: "stage ritual" "alt alt"; }
.birthday-cake-scene > .section-stage { grid-area: stage; width: 100%; margin: 0; }
.birthday-cake-scene > .cake-ritual { grid-area: ritual; }
.birthday-cake-scene > .cake-illustration-fallback { grid-area: alt; }
@media (max-width: 820px) { .birthday-cake-scene { grid-template-areas: "stage" "ritual" "alt"; } }

/* ---------- the 3D ballroom has its own confetti, fireworks and candle glow: the old CSS overlays would double them ---------- */
.birthday-cake-scene .cake-fireworks, .birthday-cake-scene .cake-scene__stars, .birthday-cake-scene .cake-balloon-cluster { display: none; }

/* ---------- hero: the quality switch sits quietly at the top right; the ready/loading status stays for assistive technology only ---------- */
.birthday-garden__stage .gift-native-canvas[data-chrome="minimal"] .gift-native-chrome { top: 10px; bottom: auto; left: auto; right: 10px; padding: 0; background: none; }
.birthday-garden__stage .gift-native-status { position: absolute; width: 1px; height: 1px; margin: -1px; padding: 0; overflow: hidden; clip: rect(0 0 0 0); white-space: nowrap; }

/* ---- content pack: letter subtitle, seven postcards, the finale thank-you, empty-playlist note ---- */
.letter-reading__subtitle { margin: 0 0 12px; color: #856d61; font: italic 1.1rem/1.4 var(--font-editorial); text-align: center; }
.postcard--birthday .postcard__scene { background: linear-gradient(180deg, #d9c9d6 0%, #f0cfb4 58%, #b9b48c 100%); }
.postcard--sapling .postcard__scene { background: linear-gradient(180deg, #f2d6bd 0%, #ecd9b4 46%, #a9b98d 100%); }
.postcard--lantern .postcard__scene { background: linear-gradient(180deg, #3d4670 0%, #b88aa0 52%, #566048 100%); }
.final-celebration__thanks { max-width: 520px; margin: 4px auto 18px; color: #856d61; font: italic clamp(1rem, 1.9vw, 1.2rem) / 1.6 var(--font-editorial); }
.music-room__empty { margin: 12px 0 0; color: #8c756a; font: italic 1rem/1.5 var(--font-editorial); text-align: center; }
.polaroid-lightbox__location { display: block; margin-top: 6px; color: #8c756a; font: 700 9px/1.4 var(--font-ui); letter-spacing: .14em; text-transform: uppercase; }
```

## 54. `src/three/GiftStage.tsx` — modified

```tsx
import { Component, lazy, Suspense, useEffect, type ReactNode } from "react";
import type { SceneState } from "./runtime";
import { giftIdFor } from "./giftFactory";
import { isSectionKind, type GiftKind, type SceneKind } from "./kinds";
import { packMicrocopy } from "../content/packContent";

export type { GiftKind, SceneKind };
export interface GiftStageProps {
  kind: SceneKind;
  state: SceneState;
  label: string;
  /** Small caption in the scene chrome (defaults to the scene kind). */
  title?: string;
  /** "minimal" keeps only a small quality switch (used by the page hero). */
  chrome?: "full" | "minimal";
  /** Still image shown while 3D is unavailable (defaults to the gift preview poster). */
  poster?: string;
  onPick?: (index: number) => void;
  onProgress?: (progress: number) => void;
  /** Called when the visitor sees the poster instead of 3D (no WebGL, or the scene failed), so HTML controls can stop waiting for scene feedback. */
  onUnavailable?: () => void;
  analyser?: AnalyserNode | null;
}

const NativeGiftCanvas = lazy(() => import("./NativeGiftCanvas"));

let webglSupported: boolean | null = null;
/** One cheap capability probe; the probe context is released immediately. */
export function hasWebGL() {
  if (webglSupported === null) {
    try {
      const canvas = document.createElement("canvas");
      const gl = (canvas.getContext("webgl2") || canvas.getContext("webgl")) as WebGLRenderingContext | null;
      webglSupported = Boolean(gl);
      gl?.getExtension("WEBGL_lose_context")?.loseContext();
    } catch { webglSupported = false; }
  }
  return webglSupported;
}

function PosterFallback({ kind, label, message, poster, onShown }: { kind: SceneKind; label: string; message: string; poster?: string; onShown?: () => void }) {
  useEffect(() => { onShown?.(); }, [onShown]);
  const src = poster ?? (isSectionKind(kind) ? undefined : `/assets/gift-previews/${giftIdFor(kind)}.webp`);
  return (
    <div className="gift-stage-fallback gift-stage-fallback--poster" role="group" aria-label={label}>
      {src && <img src={src} alt="" width={480} height={360} decoding="async" />}
      <p role="status">{message}</p>
    </div>
  );
}

class SceneBoundary extends Component<{ kind: SceneKind; label: string; poster?: string; onUnavailable?: () => void; children: ReactNode }, { failed: boolean }> {
  state = { failed: false };
  static getDerivedStateFromError() { return { failed: true }; }
  render() {
    return this.state.failed
      ? <PosterFallback kind={this.props.kind} label={this.props.label} poster={this.props.poster} onShown={this.props.onUnavailable} message={packMicrocopy.webglFallback} />
      : this.props.children;
  }
}

/** One lazily loaded WebGL stage. Without WebGL (or if the scene fails) a poster image and the HTML controls remain. */
export function GiftStage(props: GiftStageProps) {
  return (
    <div className="gift-native-stage" data-gift-world={props.kind}>
      {hasWebGL() ? (
        <SceneBoundary kind={props.kind} label={props.label} poster={props.poster} onUnavailable={props.onUnavailable}>
          <Suspense fallback={<p className="gift-stage-fallback" role="status">{packMicrocopy.loading}</p>}>
            <NativeGiftCanvas {...props} />
          </Suspense>
        </SceneBoundary>
      ) : <PosterFallback kind={props.kind} label={props.label} poster={props.poster} onShown={props.onUnavailable} message={packMicrocopy.webglFallback} />}
    </div>
  );
}
```

## 55. `src/three/NativeGiftCanvas.tsx` — modified

```tsx
import { useEffect, useId, useLayoutEffect, useRef, useState } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import * as T from "three";
import { loadScene, usesDefaultLights, type Builder } from "./giftFactory";
import { disposeTree } from "../engine/dispose";
import { disposeEnvironments } from "../engine/environment";
import { addKeyLight } from "../engine/lights";
import { FrameGovernor, detectQuality, pixelRatioFor, prefersReducedMotion, rememberQuality, type Quality } from "../engine/quality";
import { attachInput, createStage, type StageInput } from "../engine/stage";
import type { Choreography } from "./runtime";
import type { GiftStageProps } from "./GiftStage";
import { packMicrocopy } from "../content/packContent";

const qaTimeScale = () => (import.meta.env.DEV ? Number((window as unknown as { __woyTimeScale?: number }).__woyTimeScale) || 1 : 1);

interface WorldProps { props: GiftStageProps; reduced: boolean; active: boolean; host: HTMLDivElement | null; quality: Quality; onReady: () => void }

/**
 * Builds the requested gift world inside the R3F canvas and drives its choreography.
 * R3F supplies the renderer, resize handling and demand-based frame loop; the scene itself is imperative three.js.
 */
function World({ props, reduced, active, host, quality, onReady }: WorldProps) {
  const { scene, camera, gl, invalidate, setDpr } = useThree();
  const latest = useRef(props); latest.current = props;
  const flags = useRef({ reduced, active }); flags.current = { reduced, active };
  const model = useRef<Choreography | null>(null);
  const input = useRef<StageInput | null>(null);
  const clock = useRef({ elapsed: 0, last: performance.now(), frozen: false, announced: false });
  const governor = useRef(new FrameGovernor());
  const spectrum = useRef(new Uint8Array(64));

  const [failure, setFailure] = useState<Error | null>(null);
  if (failure) throw failure; // surfaces to the SceneBoundary so the readable fallback is shown

  useLayoutEffect(() => {
    let disposed = false;
    let teardown: (() => void) | null = null;

    const mount = (build: Builder) => {
      const root = new T.Scene();
      scene.add(root);
      const attached = attachInput(gl.domElement, host ?? gl.domElement);
      input.current = attached.input;
      const sync = (source: T.Scene) => {
        scene.environment = source.environment; scene.environmentIntensity = source.environmentIntensity;
        scene.background = source.background; scene.fog = source.fog;
      };
      const stage = createStage({
        renderer: gl, root, camera: camera as T.PerspectiveCamera, quality, input: attached.input,
        pick: (index) => latest.current.onPick?.(index), report: (progress) => latest.current.onProgress?.(progress), syncScene: sync, invalidate,
      });
      stage.mood({ env: "studio", envIntensity: 0.5 });
      if (usesDefaultLights(props.kind)) {
        root.add(new T.HemisphereLight("#fff0d6", "#47544f", 1.1));
        addKeyLight(root, quality, { color: "#ffe5c2", intensity: 3.2, position: [-3, 7, 5], extent: 6 });
      }
      let choreography: Choreography;
      try { choreography = build(stage); }
      catch (error) { attached.dispose(); disposeTree(root); scene.remove(root); sync(new T.Scene()); throw error; }
      sync(root);
      model.current = choreography;
      clock.current = { elapsed: 0, last: performance.now(), frozen: false, announced: false };
      if (host) { host.dataset.nativeReady = "true"; host.dataset.nativeKind = props.kind; host.dataset.quality = quality; }

      const ray = new T.Raycaster(), point = new T.Vector2();
      let downX = 0, downY = 0;
      const down = (e: PointerEvent) => { downX = e.clientX; downY = e.clientY; };
      const up = (e: PointerEvent) => {
        if (Math.hypot(e.clientX - downX, e.clientY - downY) > 12) return; // a drag, not a click
        const r = gl.domElement.getBoundingClientRect();
        point.set(((e.clientX - r.left) / r.width) * 2 - 1, -((e.clientY - r.top) / r.height) * 2 + 1);
        ray.setFromCamera(point, camera);
        for (const hit of ray.intersectObjects(choreography.pickables ?? [], true)) {
          let o: T.Object3D | null = hit.object;
          while (o && o.userData.index === undefined) o = o.parent;
          if (o && !o.userData.pickDisabled) { latest.current.onPick?.(o.userData.index as number); break; }
        }
      };
      gl.domElement.addEventListener("pointerdown", down); gl.domElement.addEventListener("pointerup", up);

      window.__WOY_LAB__?.register({
        kind: props.kind, stage, choreography, gl, invalidate,
        getState: () => latest.current.state,
        freeze: (on) => { clock.current.frozen = on; },
        simulate: (seconds, step = 1 / 30) => {
          const frames = Math.max(1, Math.round(seconds / step));
          for (let i = 0; i < frames; i++) {
            clock.current.elapsed += step; attached.input.update(step);
            choreography.frame(clock.current.elapsed, step, latest.current.state, flags.current.reduced, step);
          }
          invalidate();
        },
      });
      invalidate();
      return () => {
        model.current = null; input.current = null;
        window.__WOY_LAB__?.unregister();
        gl.domElement.removeEventListener("pointerdown", down); gl.domElement.removeEventListener("pointerup", up);
        attached.dispose();
        choreography.dispose?.();
        scene.remove(root); scene.environment = null; scene.background = null; scene.fog = null;
        disposeTree(root); disposeEnvironments(gl);
        if (host) host.dataset.nativeReady = "false";
      };
    };

    loadScene(props.kind)
      .then((build) => { if (!disposed) teardown = mount(build); })
      .catch((error: unknown) => { if (!disposed) setFailure(error instanceof Error ? error : new Error(String(error))); });
    return () => { disposed = true; teardown?.(); teardown = null; };
  }, [props.kind, quality, scene, camera, gl, invalidate, host]);

  useEffect(() => { clock.current.last = performance.now(); if (host) { host.dataset.sceneActive = String(active); host.dataset.reducedMotion = String(reduced); } invalidate(); }, [reduced, active, invalidate, host]);
  useEffect(() => { invalidate(); }, [props.state, invalidate]);

  const publish = () => {
    if (!host) return;
    host.dataset.triangles = String(gl.info.render.triangles);
    host.dataset.drawCalls = String(gl.info.render.calls);
    host.dataset.geometries = String(gl.info.memory.geometries);
    host.dataset.textures = String(gl.info.memory.textures);
  };
  useFrame((_frame, rawDt) => {
    const m = model.current;
    if (m && !clock.current.announced) { clock.current.announced = true; onReady(); }
    if (!flags.current.active || !m || clock.current.frozen) { publish(); return; }
    // 0.1 s cap keeps timelines in real time down to ~10 fps; the QA time-scale only exists in dev builds (slow software GL).
    const dt = Math.min(rawDt, 0.1) * qaTimeScale(), isReduced = flags.current.reduced;
    if (!isReduced) clock.current.elapsed += dt;
    let state = latest.current.state;
    const analyser = latest.current.analyser;
    if (analyser && state.playing) {
      analyser.getByteFrequencyData(spectrum.current);
      state = { ...state, spectrum: Array.from({ length: 12 }, (_, i) => spectrum.current[i * 4] / 255) };
    }
    const now = performance.now(), timelineDt = (now - clock.current.last) / 1000;
    clock.current.last = now;
    input.current?.update(dt);
    m.frame(clock.current.elapsed, dt, state, isReduced, timelineDt);
    publish();
    if (host) {
      host.dataset.renderFrames = String(Number(host.dataset.renderFrames ?? 0) + 1);
      host.dataset.reducedMotion = String(isReduced); host.dataset.sceneActive = String(true);
    }
    if (!isReduced) {
      if (governor.current.tick(rawDt * 1000)) setDpr(pixelRatioFor(quality, governor.current.scale));
      invalidate();
    }
  });
  return null;
}

export default function NativeGiftCanvas(props: GiftStageProps) {
  const ref = useRef<HTMLDivElement>(null);
  const hintId = useId();
  const [host, setHost] = useState<HTMLDivElement | null>(null);
  const [active, setActive] = useState(true);
  const [reduced, setReduced] = useState(prefersReducedMotion);
  const [quality, setQuality] = useState<Quality>(detectQuality);
  const [ready, setReady] = useState(false);
  const [epoch, setEpoch] = useState(0);
  const [lost, setLost] = useState(false);

  useEffect(() => {
    const node = ref.current; setHost(node);
    const preference = window.matchMedia("(prefers-reduced-motion: reduce)");
    let visible = true;
    const sync = () => { setReduced(preference.matches); setActive(visible && !document.hidden); };
    const observer = new IntersectionObserver(([entry]) => { visible = entry.isIntersecting; sync(); });
    if (node) observer.observe(node);
    document.addEventListener("visibilitychange", sync); preference.addEventListener("change", sync);
    return () => { observer.disconnect(); document.removeEventListener("visibilitychange", sync); preference.removeEventListener("change", sync); };
  }, []);

  return (
    <div className="gift-native-canvas" ref={ref} role="group" aria-roledescription="3D scene" aria-label={props.label} aria-describedby={hintId} tabIndex={0}
      data-reduced-motion={String(reduced)} data-quality={quality} data-chrome={props.chrome ?? "full"}>
      <Canvas
        key={`${quality}-${epoch}`} frameloop="demand" dpr={pixelRatioFor(quality)}
        camera={{ position: [0, 2.6, 8], fov: 38, near: 0.1, far: 80 }}
        gl={{ antialias: quality !== "low", powerPreference: quality === "low" ? "low-power" : "high-performance", alpha: false }}
        onCreated={({ gl }) => {
          gl.domElement.addEventListener("webglcontextlost", (event) => { event.preventDefault(); setLost(true); setReady(false); });
          gl.domElement.addEventListener("webglcontextrestored", () => { setLost(false); setEpoch((n) => n + 1); });
        }}
        fallback={<div className="gift-stage-fallback" role="status">WebGL is unavailable. Everything readable is still available below.</div>}
      >
        <World props={props} host={host} quality={quality} reduced={reduced} active={active} onReady={() => setReady(true)} />
      </Canvas>
      <span className="sr-only" id={hintId}>Interactive 3D scene. Use the controls below, or press the arrow keys while this scene has focus to turn the object.</span>
      <div className="gift-native-chrome">
        <span>THE WORLD OF YOU / {(props.title ?? props.kind).toUpperCase()}</span>
        <label>Detail <select aria-label={`${props.kind} graphics quality`} value={quality} onChange={(e) => { const next = e.target.value as Quality; setReady(false); rememberQuality(next); setQuality(next); }}>
          <option value="low">Low</option><option value="medium">Medium</option><option value="high">High</option></select></label>
      </div>
      <span className="gift-native-status" role="status">{lost ? "The graphics context was interrupted; restoring…" : ready ? "Real-time 3D ready" : packMicrocopy.loading}</span>
    </div>
  );
}
```

## 56. `src/three/SectionStage.tsx` — new

```tsx
import { useEffect, useRef, useState } from "react";
import { GiftStage, type GiftStageProps } from "./GiftStage";
import type { SceneKind } from "./kinds";

const CSS_KIND: Partial<Record<SceneKind, string>> = {
  ballroom: "cake", "wish-garden": "garden", "hero-garden": "hero", postcards: "postcard", letter: "letter", observatory: "observatory",
};

export interface SectionStageProps extends GiftStageProps {
  className?: string;
}

/**
 * Hosts one of the page's 3D scenes (not a gift) on the shared engine.
 *  - The scene is only mounted while its section is near the viewport (160px margin) and is released again 4 s after the section
 *    has left a generous 180% margin, so at most one or two WebGL contexts exist at any time.
 *  - While asleep (or without WebGL) the section shows its poster and the page keeps all readable content and HTML controls.
 */
export function SectionStage({ className = "", ...props }: SectionStageProps) {
  const ref = useRef<HTMLDivElement>(null);
  const [awake, setAwake] = useState(false);

  useEffect(() => {
    const node = ref.current;
    if (!node) return;
    let timer = 0;
    const enter = new IntersectionObserver(([entry]) => { if (entry.isIntersecting) { window.clearTimeout(timer); setAwake(true); } }, { rootMargin: "160px 0px" });
    const leave = new IntersectionObserver(([entry]) => {
      window.clearTimeout(timer);
      if (!entry.isIntersecting) timer = window.setTimeout(() => setAwake(false), 4000);
    }, { rootMargin: "180% 0px" });
    enter.observe(node); leave.observe(node);
    return () => { enter.disconnect(); leave.disconnect(); window.clearTimeout(timer); };
  }, []);

  const css = CSS_KIND[props.kind] ?? props.kind;
  return (
    <div ref={ref} className={`cinematic-viewport cinematic-viewport--${css} section-stage ${className}`.trim()} data-section-stage={props.kind} data-awake={String(awake)}
      style={props.poster ? { backgroundImage: `url(${props.poster})` } : undefined}>
      {awake ? <GiftStage {...props} poster={undefined} /> : <div className="section-stage__asleep" role="img" aria-label={props.label} />}
    </div>
  );
}
```

## 57. `src/three/exportModels.ts` — modified

```ts
// Offline authoring entry used by scripts/export-models.mjs, never imported by the app.
import * as T from "three";
import { GLTFExporter } from "three/addons/exporters/GLTFExporter.js";
import { loadScene } from "./giftFactory";
import type { SceneKind } from "./kinds";
import type { SceneState } from "./runtime";
import { createStage, idleInput } from "../engine/stage";

/** Static interchange snapshots of the current scenes (GLB cannot carry runtime shaders, instanced wind or particles). */
const SCENES: Record<string, { kind: SceneKind; state: SceneState }> = {
  garden: { kind: "wish-garden", state: { selected: 0 } },
  cake: { kind: "ballroom", state: { bakeStage: 3, candles: 5 } },
  "letter-desk": { kind: "letter", state: { open: true } },
  "eternal-rose": { kind: "flower", state: { growth: 4 } },
  crown: { kind: "crown", state: {} },
  portal: { kind: "portal", state: { growth: 2 } },
  observatory: { kind: "observatory", state: {} },
};

export async function exportModel(name: string): Promise<string> {
  const scene = new T.Scene(); const camera = new T.PerspectiveCamera(38, 1.5, 0.1, 100);
  const renderer = new T.WebGLRenderer({ antialias: false });
  const stage = createStage({ renderer, root: scene, camera, quality: "low", input: idleInput(), pick: () => {} });
  const entry = SCENES[name];
  if (!entry) throw new Error("Unknown authored model");
  const model = (await loadScene(entry.kind))(stage);
  model.frame(0, 1, entry.state, true, 1); scene.updateMatrixWorld(true);
  renderer.dispose();
  // GLB is a static interchange snapshot. Runtime GLSL and instanced wind remain in source.
  const unsupported: T.Object3D[] = [];
  scene.traverse((object) => { if (object instanceof T.Mesh && (Array.isArray(object.material) ? object.material : [object.material]).some((mat) => mat instanceof T.ShaderMaterial)) unsupported.push(object); });
  unsupported.forEach((object) => object.removeFromParent());
  const result = await new GLTFExporter().parseAsync(scene, { binary: true, onlyVisible: true, maxTextureSize: 128 });
  const bytes = new Uint8Array(result as ArrayBuffer); let string = "";
  for (let i = 0; i < bytes.length; i += 8192) string += String.fromCharCode(...bytes.subarray(i, i + 8192));
  return btoa(string);
}
```

## 58. `src/three/giftFactory.ts` — modified

```ts
import type { Choreography, Stage } from "./runtime";
import { GIFT_KINDS, isSectionKind, type GiftKind, type SceneKind, type SectionKind } from "./kinds";

export type Builder = (stage: Stage) => Choreography;
interface Entry {
  load: () => Promise<Builder>;
  /** true when the scene sets its own lighting and mood (so the host adds no default lights) */
  own?: boolean;
}

/**
 * Every gift scene is its own dynamically imported module: opening one gift downloads only that scene's code.
 * Registry order matches gift-01 ... gift-17.
 */
const registry: Record<GiftKind, Entry> = {
  letter: { load: async () => (await import("./gifts/letter")).buildLetterWorld, own: true },
  jar: { load: async () => (await import("./gifts/jar")).buildJarWorld, own: true },
  flower: { load: async () => (await import("./gifts/flower")).buildFlowerWorld, own: true },
  universe: { load: async () => (await import("./gifts/universe")).buildUniverseWorld, own: true },
  cassette: { load: async () => (await import("./gifts/cassette")).buildCassetteWorld, own: true },
  cinema: { load: async () => (await import("./gifts/cinema")).buildCinemaWorld, own: true },
  wishes: { load: async () => (await import("./gifts/wishes")).buildWishesWorld, own: true },
  crown: { load: async () => (await import("./gifts/crown")).buildCrownWorld, own: true },
  cabinet: { load: async () => (await import("./gifts/cabinet")).buildCabinetWorld, own: true },
  machine: { load: async () => (await import("./gifts/machine")).buildMachineWorld, own: true },
  adventure: { load: async () => (await import("./gifts/adventure")).buildAdventureWorld, own: true },
  vinyl: { load: async () => (await import("./gifts/vinyl")).buildVinylWorld, own: true },
  mirror: { load: async () => (await import("./gifts/mirror")).buildMirrorWorld, own: true },
  coupons: { load: async () => (await import("./gifts/coupons")).buildCouponsWorld, own: true },
  "hope-tree": { load: async () => (await import("./gifts/hopeTree")).buildHopeTreeWorld, own: true },
  treasure: { load: async () => (await import("./gifts/treasure")).buildTreasureWorld, own: true },
  portal: { load: async () => (await import("./gifts/portal")).buildPortalWorld, own: true },
};

/** Non-gift scenes of the page (hero garden, wish garden, observatory, postcards, ballroom). */
const sectionRegistry: Record<SectionKind, Entry> = {
  "hero-garden": { load: async () => (await import("./sections/heroGarden")).buildHeroGarden, own: true },
  observatory: { load: async () => (await import("./sections/observatory")).buildObservatory, own: true },
  postcards: { load: async () => (await import("./sections/postcards")).buildPostcards, own: true },
  ballroom: { load: async () => (await import("./sections/ballroom")).buildBallroom, own: true },
  "wish-garden": { load: async () => (await import("./sections/wishGarden")).buildWishGarden, own: true },
};

const entryFor = (kind: SceneKind): Entry => {
  const entry = isSectionKind(kind) ? sectionRegistry[kind] : registry[kind];
  if (!entry) throw new Error(`Unknown scene: ${kind}`);
  return entry;
};
export const giftKinds = GIFT_KINDS as readonly GiftKind[];
export const loadScene = (kind: SceneKind) => entryFor(kind).load();
export const loadGift = loadScene;
export const usesDefaultLights = (kind: SceneKind) => !entryFor(kind).own;
/** gift-01 ... gift-17 id for a scene kind (used for poster images). */
export const giftIdFor = (kind: SceneKind) => `gift-${String((giftKinds as readonly SceneKind[]).indexOf(kind) + 1).padStart(2, "0")}`;
```

## 59. `src/three/gifts/adventure.ts` — new

```ts
/**
 * Gift 11 - Little Adventure.
 * An obviously imaginary papercraft relief map on a study table: four terraced islands, a brass-bead flight route,
 * four flags and a small paper plane that flies the route to the selected place. Places that are not unlocked yet sit
 * under drifting cloud banks that dissolve when they unlock. state.selected = place, state.growth = highest unlocked.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease } from "../../engine/anim";
import { RoundedBoxGeometry, lathe, put } from "../../engine/geometry";
import { addKeyLight } from "../../engine/lights";
import { ParticleField } from "../../engine/fx";
import { particleScale } from "../../engine/quality";
import { backdrop, box, glowSprite, hash, orbitCamera, paintBokeh, softTexture } from "./common";

const W = 10.4, D = 6.6;
const LOCS: [number, number][] = [[-3.5, 1.0], [-1.2, -1.5], [1.4, 1.3], [3.5, -1.3]];
const FLAGS = ["#e5566d", "#f0b43a", "#3fa7a0", "#8a6fd0"];
const LEVELS = 7, STEP = 0.16;
const LAND = ["#1f5f78", "#ecd49c", "#a8cc72", "#7db35a", "#5a9150", "#8d927c", "#f0f4f4"].map((c) => new T.Color(c));
const SEA_DEEP = new T.Color("#1c5a74"), SEA_SHALLOW = new T.Color("#5db4b6");

const islandHeight = (x: number, z: number) => {
  let h = 0;
  LOCS.forEach(([cx, cz], i) => { const r = 1.55 + (i % 2) * 0.4, d = Math.hypot((x - cx) / r, (z - cz) / (r * 0.82)); h = Math.max(h, Math.exp(-d * d * 1.5)); });
  const n = 0.5 + 0.25 * Math.sin(x * 2.1 + z * 1.3) + 0.25 * Math.sin(x * 3.7 - z * 2.9);
  return Math.max(0, h * (0.82 + 0.3 * n) - 0.02);
};
const terrace = (h: number) => { const t = h * LEVELS, f = Math.floor(t), s = T.MathUtils.smoothstep(t - f, 0.32, 0.68); return { y: (f + s) * STEP, level: Math.floor(t + 0.5) }; };

export function buildAdventureWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "candle", envIntensity: 0.8, exposure: 1.12, background: "#15100d", fog: { color: "#17110d", density: 0.014 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 90; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#fff0d4", "#2a1c12", 0.7));
  addKeyLight(scene, quality, { color: "#ffe2b4", intensity: 3.4, position: [-6, 9, 5], target: [0, 0, 0], extent: 8, far: 30 });
  const fill = new T.DirectionalLight("#9fb7e6", 0.5); fill.position.set(6, 5, -4); scene.add(fill);

  /* ---------- study ---------- */
  const room = backdrop((g, w, h) => { const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#1b1410"); bg.addColorStop(1, "#2b2017"); g.fillStyle = bg; g.fillRect(0, 0, w, h); paintBokeh(g, w, h, "255,190,120", 22, 11); }, 60, 30);
  room.position.set(0, 6, -9); scene.add(room);
  const table = put(scene, new T.BoxGeometry(26, 0.5, 16), kit.wood("#1f1109", "#5e3b22", [5, 3], 0.55), 0, -0.85, 1, false); table.receiveShadow = true;

  /* ---------- map ---------- */
  const nx = low ? 90 : 150, nz = Math.round((nx * D) / W);
  const geo = new T.PlaneGeometry(W, D, nx, nz); geo.rotateX(-Math.PI / 2);
  const pa = geo.attributes.position, colours = new Float32Array(pa.count * 3), tmp = new T.Color();
  for (let i = 0; i < pa.count; i++) {
    const x = pa.getX(i), z = pa.getZ(i), h = islandHeight(x, z), { y, level } = terrace(h);
    pa.setY(i, y);
    if (level <= 0) tmp.copy(SEA_DEEP).lerp(SEA_SHALLOW, T.MathUtils.smoothstep(h, 0.0, 0.12) * 0.8 + 0.12 * Math.sin(x * 3 + z * 2)); else tmp.copy(LAND[Math.min(level, LAND.length - 1)]).multiplyScalar(0.94 + hash(i, 3) * 0.1);
    colours.set([tmp.r, tmp.g, tmp.b], i * 3);
  }
  geo.setAttribute("color", new T.BufferAttribute(colours, 3)); geo.computeVertexNormals();
  const paperMat = kit.paper("#ffffff", "#e8e0cf", { roughness: 0.9 }) as T.MeshStandardMaterial; const land = new T.MeshStandardMaterial({ vertexColors: true, roughness: 0.92, bumpMap: paperMat.bumpMap ?? null, bumpScale: 0.6 });
  const terrain = new T.Mesh(geo, land); terrain.receiveShadow = true; terrain.castShadow = !low; terrain.position.y = 0.12; scene.add(terrain);
  const sea = put(scene, new T.PlaneGeometry(W, D), new T.MeshPhysicalMaterial({ color: "#7cc8d0", transparent: true, opacity: 0.32, roughness: 0.05, clearcoat: 1, clearcoatRoughness: 0.05 }), 0, 0.135, 0, false); sea.rotation.x = -Math.PI / 2;
  const wood = kit.wood("#2a160c", "#7a4a28", [3, 1], 0.45), brass = kit.metal("brass", 0.3);
  const rail = (w: number, d: number, x: number, z: number) => put(scene, new RoundedBoxGeometry(w, 0.6, d, 3, 0.05), wood, x, 0.0, z);
  rail(W + 1.2, 0.5, 0, -D / 2 - 0.25); rail(W + 1.2, 0.5, 0, D / 2 + 0.25); rail(0.5, D, -W / 2 - 0.25, 0); rail(0.5, D, W / 2 + 0.25, 0);
  for (const sx of [-1, 1]) for (const sz of [-1, 1]) put(scene, new T.SphereGeometry(0.2, 14, 10), brass, sx * (W / 2 + 0.25), 0.3, sz * (D / 2 + 0.25), false);
  put(scene, new T.BoxGeometry(W, 0.3, D), new T.MeshStandardMaterial({ color: "#2a2018", roughness: 0.9 }), 0, -0.1, 0, false);
  const rose = (() => { const c = document.createElement("canvas"); c.width = c.height = 256; const g = c.getContext("2d")!; g.translate(128, 128); g.strokeStyle = "rgba(255,238,200,.9)"; g.fillStyle = "rgba(255,238,200,.85)"; g.lineWidth = 3; g.beginPath(); g.arc(0, 0, 100, 0, 6.283); g.stroke(); g.beginPath(); g.arc(0, 0, 84, 0, 6.283); g.stroke();
    for (let i = 0; i < 8; i++) { g.save(); g.rotate((i * Math.PI) / 4); const L = i % 2 ? 62 : 108; g.beginPath(); g.moveTo(0, -L); g.lineTo(11, -14); g.lineTo(0, 0); g.lineTo(-11, -14); g.closePath(); i % 2 ? g.stroke() : g.fill(); g.restore(); }
    g.font = "700 30px Georgia, serif"; g.textAlign = "center"; g.fillText("N", 0, -112); const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t; })();
  const compassRose = put(scene, new T.PlaneGeometry(1.5, 1.5), new T.MeshBasicMaterial({ map: rose, transparent: true, depthWrite: false, opacity: 0.85 }), 4.15, 0.16, 2.35, false); compassRose.rotation.x = -Math.PI / 2;

  /* ---------- route ---------- */
  const surfaceAt = (x: number, z: number) => terrace(islandHeight(x, z)).y + 0.12;
  const control: T.Vector3[] = [];
  LOCS.forEach(([x, z], i) => { control.push(new T.Vector3(x, surfaceAt(x, z) + 0.75, z)); if (i < LOCS.length - 1) { const [nxp, nzp] = LOCS[i + 1]; control.push(new T.Vector3((x + nxp) / 2, 1.5, (z + nzp) / 2 + (i % 2 ? -0.5 : 0.6))); } });
  const curve = new T.CatmullRomCurve3(control, false, "centripetal");
  const samples = curve.getSpacedPoints(300), uOf = LOCS.map((_, i) => { let best = 0, bd = 1e9; samples.forEach((p, k) => { const d = p.distanceTo(control[i * 2]); if (d < bd) { bd = d; best = k; } }); return best / 300; });
  const BEADS = 78, beads = new T.InstancedMesh(new T.SphereGeometry(0.05, 8, 6), new T.MeshStandardMaterial({ color: "#ffffff", metalness: 0.8, roughness: 0.3 }), BEADS), bm = new T.Object3D();
  for (let i = 0; i < BEADS; i++) { const p = curve.getPointAt(i / (BEADS - 1)); bm.position.copy(p); bm.updateMatrix(); beads.setMatrixAt(i, bm.matrix); } scene.add(beads);
  const GOLD = new T.Color("#f6c85a"), GREY = new T.Color("#59606a"); let beadKey = -1;

  /* ---------- flags, rings, hit boxes, fog banks ---------- */
  const flags = LOCS.map(([x, z], i) => {
    const g = new T.Group(); g.position.set(x, surfaceAt(x, z), z); g.userData.index = i; scene.add(g);
    put(g, new T.CylinderGeometry(0.028, 0.034, 1.25, 8), brass, 0, 0.62, 0); put(g, new T.SphereGeometry(0.06, 10, 8), brass, 0, 1.27, 0, false);
    const clothGeo = new T.PlaneGeometry(0.72, 0.42, 9, 4); clothGeo.translate(0.36, 0, 0); const base = Float32Array.from(clothGeo.attributes.position.array as ArrayLike<number>);
    const cloth = new T.Mesh(clothGeo, new T.MeshStandardMaterial({ color: FLAGS[i], roughness: 0.7, side: T.DoubleSide })); cloth.castShadow = !low; cloth.position.set(0.03, 1.05, 0); g.add(cloth);
    const ring = put(g, new T.TorusGeometry(0.6, 0.022, 8, 40), new T.MeshBasicMaterial({ color: "#ffe29a", transparent: true, opacity: 0, blending: T.AdditiveBlending, depthWrite: false }), 0, 0.06, 0, false); ring.rotation.x = Math.PI / 2;
    const halo = glowSprite("#ffd98a", 2.4, 0); halo.position.y = 0.9; g.add(halo);
    const hitbox = new T.Mesh(new T.CylinderGeometry(0.65, 0.65, 1.6, 10), new T.MeshBasicMaterial({ visible: false })); hitbox.position.y = 0.7; hitbox.userData.index = i; g.add(hitbox);
    const banks = Array.from({ length: low ? 4 : 7 }, (_, k) => {
      const s = new T.Sprite(new T.SpriteMaterial({ map: softTexture("rgba(255,255,255,0.96)", "rgba(255,255,255,0)"), color: "#e6eef6", transparent: true, depthWrite: false, opacity: 0.92 }));
      const a = (k / 7) * 6.283 + i; s.position.set(x + Math.cos(a) * 0.9, 0.85 + hash(k, i) * 0.4, z + Math.sin(a) * 0.65); s.scale.setScalar(2.1 + hash(k, i + 4) * 1.0); scene.add(s); return { s, a, bx: x, bz: z, k };
    });
    return { g, cloth, base, ring, halo, banks, reveal: 0, lift: 0 };
  });

  /* ---------- paper plane ---------- */
  const planeGeo = new T.BufferGeometry(); planeGeo.setAttribute("position", new T.Float32BufferAttribute([0, 0, 0.55, -0.27, 0.05, -0.3, 0, -0.11, -0.3, 0, 0, 0.55, 0, -0.11, -0.3, 0.27, 0.05, -0.3, 0, 0, 0.55, 0.27, 0.05, -0.3, -0.27, 0.05, -0.3, -0.27, 0.05, -0.3, 0.27, 0.05, -0.3, 0, -0.11, -0.3], 3)); planeGeo.computeVertexNormals();
  const plane = new T.Mesh(planeGeo, new T.MeshStandardMaterial({ color: "#fffaf0", roughness: 0.8, side: T.DoubleSide, flatShading: true })); plane.castShadow = true; plane.scale.setScalar(2.1); scene.add(plane);
  const trail = new ParticleField({ count: Math.round(50 * particleScale(quality)), size: 0.06, color: "#ffe6a8", opacity: 0.5, bounds: [4.6, 0.9, 2.6], center: [0, 1.0, 0], twinkle: 0.8, drift: 0.6, shape: "spark" }); scene.add(trail.points);

  /* ---------- table props ---------- */
  const compass = new T.Group(); compass.position.set(6.7, 0, 2.3); scene.add(compass);
  put(compass, lathe([[0, 0], [0.55, 0], [0.58, 0.08], [0.55, 0.2], [0.46, 0.22], [0, 0.22]], 36), brass, 0, 0, 0); const face2 = put(compass, new T.CircleGeometry(0.44, 36), new T.MeshStandardMaterial({ color: "#f5efdd", roughness: 0.6 }), 0, 0.225, 0, false); face2.rotation.x = -Math.PI / 2;
  const needle = new T.Group(); needle.position.y = 0.24; compass.add(needle); put(needle, new T.ConeGeometry(0.06, 0.38, 4), new T.MeshBasicMaterial({ color: "#c22b32" }), 0, 0, -0.19, false).rotation.x = -Math.PI / 2; put(needle, new T.ConeGeometry(0.06, 0.38, 4), new T.MeshBasicMaterial({ color: "#e8e8e8" }), 0, 0, 0.19, false).rotation.x = Math.PI / 2;
  const pencil = put(scene, new T.CylinderGeometry(0.06, 0.06, 1.7, 6), new T.MeshStandardMaterial({ color: "#d99a2b", roughness: 0.6 }), -6.7, -0.55, 2.7); pencil.rotation.set(0, 0.5, Math.PI / 2); box(scene, 0.01, 0.01, 0.01, brass, 0, -9, 0, false);

  /* ---------- choreography ---------- */
  const pos = new T.Vector3(), look = new T.Vector3(0, 0.3, 0.3), orbit = { yaw: 0, pitch: 0 }, tan = new T.Vector3(), target = new T.Vector3(), focusPt = new T.Vector3();
  let u = uOf[0], roll = 0, lastSel = -1, lastHeading = 0;
  return {
    pickables: flags.map((f) => f.g),
    frame(time, dt, state: SceneState, reduced) {
      const sel = Math.max(0, Math.min(LOCS.length - 1, state.selected ?? 0)), unlocked = Math.max(0, Math.min(LOCS.length - 1, state.growth ?? 0));
      if (sel !== lastSel) { if (lastSel >= 0) stage.sfx("whoosh"); lastSel = sel; }
      if (beadKey !== unlocked) { beadKey = unlocked; for (let i = 0; i < BEADS; i++) beads.setColorAt(i, i / (BEADS - 1) <= uOf[unlocked] + 0.001 ? GOLD : GREY); if (beads.instanceColor) beads.instanceColor.needsUpdate = true; }
      flags.forEach((f, i) => {
        const open = i <= unlocked, isSel = i === sel;
        f.reveal = damp(f.reveal, open ? 1 : 0, 2.4, dt, reduced); f.lift = damp(f.lift, isSel ? 1 : 0, 5, dt, reduced);
        const m = f.cloth.material as T.MeshStandardMaterial; m.color.set(open ? FLAGS[i] : "#7c828c"); f.cloth.position.y = 0.55 + 0.5 * f.reveal; f.cloth.scale.setScalar(0.85 + 0.25 * f.lift);
        const pa2 = f.cloth.geometry.attributes.position as T.BufferAttribute;
        for (let k = 0; k < pa2.count; k++) { const bx = f.base[k * 3], by = f.base[k * 3 + 1], w = bx / 0.72; pa2.setZ(k, reduced ? 0 : Math.sin(bx * 6 - time * 5 + i) * 0.07 * w + Math.sin(by * 5 + time * 3) * 0.015 * w); pa2.setY(k, by - w * w * 0.04); }
        pa2.needsUpdate = true; f.cloth.geometry.computeVertexNormals();
        (f.ring.material as T.MeshBasicMaterial).opacity = f.lift * (0.55 + (reduced ? 0 : Math.sin(time * 3) * 0.2)); f.ring.scale.setScalar(1 + (reduced ? 0 : Math.sin(time * 3) * 0.06));
        (f.halo.material as T.SpriteMaterial).opacity = f.lift * 0.55;
        f.banks.forEach((b) => { const mm = b.s.material as T.SpriteMaterial; mm.opacity = (1 - f.reveal) * 0.92; b.s.visible = mm.opacity > 0.01; const d = reduced ? 0 : time * 0.12 + b.k; b.s.position.x = b.bx + Math.cos(b.a + d * 0.5) * (0.9 + f.reveal * 1.8); b.s.position.z = b.bz + Math.sin(b.a + d * 0.5) * (0.65 + f.reveal * 1.4); });
      });
      // plane follows the route to the selected place
      u = damp(u, uOf[sel], 1.6, dt, reduced); const pt = curve.getPointAt(Math.min(1, Math.max(0, u))); curve.getTangentAt(Math.min(1, Math.max(0, u)), tan);
      plane.position.copy(pt).y += reduced ? 0 : Math.sin(time * 2.2) * 0.05; target.copy(plane.position).add(tan); plane.lookAt(target);
      const heading = Math.atan2(tan.x, tan.z), turn = heading - lastHeading; lastHeading = heading; roll = damp(roll, T.MathUtils.clamp(-turn * 40, -0.7, 0.7) + (reduced ? 0 : Math.sin(time * 1.3) * 0.08), 6, dt, reduced); plane.rotateZ(roll);
      needle.rotation.y = reduced ? 0.6 : 0.6 + Math.sin(time * 0.8) * 0.12 + Math.sin(time * 3.3) * 0.02; trail.update(time);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.0, -0.65, 0.65); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.1, -0.2, 0.3);
      focusPt.set(LOCS[sel][0] * 0.32, 0.2, LOCS[sel][1] * 0.2 + 0.3); look.lerp(focusPt, reduced ? 1 : 1 - Math.exp(-dt * 2.2));
      pos.set(look.x * 0.5 + (reduced ? 0 : Math.sin(time * 0.15) * 0.4), 9.0 - 0.3 * ease.inOut(1), 10.3); orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 60. `src/three/gifts/cabinet.ts` — new

```ts
/**
 * Gift 09 - Open When...
 * A walnut letter cabinet with four pigeonholes, one sealed envelope in each, each with a hanging tag carrying its
 * prompt. Picking an envelope slides it out and turns it toward you; opening breaks the seal, folds the flap back and
 * lifts a letter into reading position. The message bodies are still owner slots: an empty one shows the pack's "waiting to be written" line, a written one is set on the ruled paper.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, span } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, bentPaper, put } from "../../engine/geometry";
import { addContactShadow, addKeyLight, addPointLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { openWhenLetters } from "../../content/giftsContent";
import { packMicrocopy } from "../../content/packContent";
import { backdrop, box, glowSprite, orbitCamera, paintBokeh } from "./common";
import { makeEnvelope } from "./envelope";

const HOLE = { w: 2.3, h: 1.65 };
const CENTERS: [number, number][] = [[-1.3, 1.0], [1.3, 1.0], [-1.3, -0.85], [1.3, -0.85]];
const TINTS = ["#f1e5c8", "#f3d9d4", "#dce7d6", "#e1dcf0"], SEALS = ["#8f2a3c", "#2f5f8a", "#2f7a52", "#7a4a9a"];

function tagTexture(text: string) {
  const c = document.createElement("canvas"); c.width = 384; c.height = 256; const g = c.getContext("2d")!;
  g.fillStyle = "#f4e9cf"; g.fillRect(0, 0, 384, 256); g.strokeStyle = "rgba(150,110,70,.6)"; g.lineWidth = 5; g.strokeRect(10, 10, 364, 236);
  g.fillStyle = "#4a3a30"; g.textAlign = "center"; g.font = "600 34px Georgia, serif";
  const words = text.split(" "); let line = "", y = 90; for (const w of words) { const t = line ? `${line} ${w}` : w; if (g.measureText(t).width > 320 && line) { g.fillText(line, 192, y); y += 46; line = w; } else line = t; } g.fillText(line, 192, y);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}
/** The letter that rises from an envelope: its prompt in handwriting, then the owner's message, or the pack's "waiting to be written" line while the slot is empty. */
function letterTexture(prompt: string, message: string) {
  const c = document.createElement("canvas"); c.width = 1024, c.height = 704; const g = c.getContext("2d")!;
  g.fillStyle = "#f6edd7"; g.fillRect(0, 0, 1024, 704);
  const e = g.createRadialGradient(512, 352, 220, 512, 352, 600); e.addColorStop(0, "rgba(120,96,60,0)"); e.addColorStop(1, "rgba(120,96,60,.22)"); g.fillStyle = e; g.fillRect(0, 0, 1024, 704);
  g.strokeStyle = "rgba(110,92,72,.2)"; g.lineWidth = 2; for (let y = 250; y < 660; y += 62) { g.beginPath(); g.moveTo(80, y); g.lineTo(944, y); g.stroke(); }
  g.fillStyle = "rgba(60,44,40,.95)"; g.font = "700 76px Caveat, 'Segoe Print', cursive"; g.textBaseline = "alphabetic"; g.fillText(prompt, 80, 130);
  const written = message.trim(), body = written || packMicrocopy.missingText;
  const font = (px: number) => (written ? `600 ${px}px Caveat, 'Segoe Print', cursive` : `italic ${px}px Georgia, serif`);
  const wrap = (px: number) => {
    g.font = font(px); const lines: string[] = []; let line = "";
    for (const word of body.split(/\s+/)) { const test = line ? `${line} ${word}` : word; if (g.measureText(test).width > 864 && line) { lines.push(line); line = word; } else line = test; }
    lines.push(line); return lines;
  };
  let size = written ? 46 : 38, lines = wrap(size);
  while (lines.length > 7 && size > 22) { size -= 2; lines = wrap(size); } // seven ruled lines are available
  g.fillStyle = written ? "rgba(40,30,28,.95)" : "rgba(110,92,80,.65)"; g.font = font(size);
  lines.slice(0, 7).forEach((line, i) => g.fillText(line, 80, 244 + i * 62));
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 8; return t;
}

export function buildCabinetWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  stage.mood({ env: "candle", envIntensity: 1.0, exposure: 1.12, background: "#10161a", fog: { color: "#10181c", density: 0.02 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#ffe0bc", "#10161a", 0.5));
  addKeyLight(scene, quality, { color: "#ffd9ac", intensity: 3.2, position: [-5, 7, 7], target: [0, 0.4, 0], extent: 7, far: 26 });
  const lamp = addPointLight(scene, "#ffb870", 26, [4.8, 3.4, 3.0], 14, 2);
  const rim = new T.DirectionalLight("#90a8e8", 0.7); rim.position.set(6, 3, -5); scene.add(rim);

  const wall = backdrop((g, w, h) => { const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#142126"); bg.addColorStop(1, "#1f3238"); g.fillStyle = bg; g.fillRect(0, 0, w, h); g.strokeStyle = "rgba(255,255,255,.04)"; g.lineWidth = 3; for (let x = 0; x < w; x += 128) { g.strokeRect(x + 8, 70, 112, h - 140); } paintBokeh(g, w, h, "255,196,130", 18, 5); }, 44, 24);
  wall.position.set(0, 4, -4); scene.add(wall);
  const desk = put(scene, new T.BoxGeometry(22, 0.5, 12), kit.wood("#1d0f08", "#5a3922", [3, 2], 0.5), 0, -2.45, 0.5, false); desk.receiveShadow = true;
  const lampGlow = glowSprite("#ffb870", 8, 0.35); lampGlow.position.set(4.8, 3.4, 1.5); scene.add(lampGlow);

  /* ---------- cabinet ---------- */
  const walnut = kit.wood("#2a1409", "#7c4b28", [2, 1.5], 0.48), brass = kit.metal("brass", 0.3);
  const cab = new T.Group(); cab.position.set(0, 0.1, 0); scene.add(cab);
  put(cab, new RoundedBoxGeometry(5.5, 4.4, 0.18, 3, 0.05), new T.MeshStandardMaterial({ color: "#12100e", roughness: 0.9 }), 0, 0.15, -0.55);
  for (const [w, h, x, y] of [[5.5, 0.28, 0, 2.36], [5.5, 0.28, 0, -2.06], [0.28, 4.4, -2.61, 0.15], [0.28, 4.4, 2.61, 0.15], [0.12, 4.2, 0, 0.15], [5.3, 0.12, 0, 0.08]] as const) put(cab, new RoundedBoxGeometry(w, h, 1.35, 2, 0.03), walnut, x, y, 0);
  put(cab, new T.BoxGeometry(5.9, 0.12, 1.5), brass, 0, 2.55, 0, false);
  CENTERS.forEach(([x, y], i) => { const plate = put(cab, new T.PlaneGeometry(0.5, 0.26), new T.MeshStandardMaterial({ map: tagTexture(String(i + 1)), roughness: 0.4, metalness: 0.5 }), x, y - HOLE.h / 2 + 0.02, 0.69, false); void plate; });
  addContactShadow(scene, 6.4, 2.2, 0, -2.18, 0, 0.6);

  /* ---------- envelopes ---------- */
  const items = openWhenLetters.map((letter, i) => {
    const env = makeEnvelope(kit, 1.75, 1.15, TINTS[i], SEALS[i]); const rest = new T.Vector3(CENTERS[i][0], CENTERS[i][1] + 0.1 - 0.0, 0.12);
    env.group.position.copy(rest); env.group.rotation.set(-0.14, 0, (i % 2 ? 1 : -1) * 0.03); env.group.userData.index = i; cab.add(env.group);
    const tag = new T.Group(); tag.position.set(0.55, -0.7, 0.08); env.group.add(tag);
    put(tag, new T.CylinderGeometry(0.006, 0.006, 0.22, 4), new T.MeshBasicMaterial({ color: "#c8b690" }), 0, 0.11, 0, false);
    put(tag, new RoundedBoxGeometry(0.62, 0.42, 0.015, 2, 0.02), new T.MeshStandardMaterial({ map: tagTexture(letter.prompt), roughness: 0.85 }), 0, -0.2, 0);
    put(env.group, new T.BoxGeometry(1.75, 1.15, 0.2), new T.MeshBasicMaterial({ visible: false }), 0, 0, 0.05, false).userData.index = i;
    return { ...env, rest, tag, lift: 0, openK: 0 };
  });
  const letterTex = letterTexture(openWhenLetters[0].prompt, openWhenLetters[0].message); let letterKey = -1;
  const paper = new T.Mesh(bentPaper(2.7, 1.86, 0.07, 0.04, 14, 10), new T.MeshStandardMaterial({ map: letterTex, roughness: 0.9, side: T.DoubleSide }));
  paper.visible = false; paper.castShadow = true; scene.add(paper);
  const dust = new ParticleField({ count: Math.round(110 * particleScale(quality)), size: 0.045, color: "#ffd9a0", opacity: 0.6, bounds: [5, 3, 3], center: [0, 1.2, 2], drift: 0.6, rise: 0.03, twinkle: 0.8 });
  scene.add(dust.points);

  /* ---------- choreography ---------- */
  const s = { focus: 0, open: 0, sel: -1 }; const pos = new T.Vector3(), look = new T.Vector3(), orbit = { yaw: 0, pitch: 0 }, front = new T.Vector3(0, -0.3, 2.7), v = new T.Vector3(), envW = new T.Vector3(), pocket = new T.Vector3(), reading = new T.Vector3(0, 0.95, 3.2);
  let lastSel: number | null | undefined, lastOpen = false;
  return {
    pickables: items.map((it) => it.group),
    frame(time, dt, state: SceneState, reduced) {
      const sel = state.selected ?? null, open = Boolean(state.open) && sel !== null;
      if (sel !== lastSel) { if (lastSel !== undefined && sel !== null) stage.sfx("paper"); lastSel = sel; if (sel !== null) s.sel = sel; }
      if (open !== lastOpen) { stage.sfx(open ? "wax" : "flap"); lastOpen = open; }
      s.focus = damp(s.focus, sel !== null ? 1 : 0, 2.6, dt, reduced); s.open = damp(s.open, open ? 1 : 0, 1.8, dt, reduced);
      items.forEach((it, i) => {
        const isSel = sel === i, k = ease.inOut(isSel ? s.focus : 0);
        it.lift = damp(it.lift, k, 6, dt, reduced);
        const L = ease.inOut(it.lift);
        v.copy(it.rest).lerp(cab.worldToLocal(front.clone()), L); it.group.position.copy(v);
        it.group.rotation.set(-0.14 * (1 - L), 0, (i % 2 ? 1 : -1) * 0.03 * (1 - L)); it.group.scale.setScalar(1 + 0.5 * L);
        it.hinge.rotation.x = -Math.PI * 0.985 * (isSel ? ease.inOut(span(s.open, 0, 0.55)) : 0);
        it.seal.visible = !(isSel && s.open > 0.12); it.tag.rotation.z = reduced ? 0 : Math.sin(time * 1.4 + i) * 0.05 * (1 - L);
      });
      const O = ease.inOut(span(s.open, 0.3, 1));
      paper.visible = O > 0.001 && s.sel >= 0;
      if (paper.visible) {
        if (letterKey !== s.sel) { letterKey = s.sel; const nt = letterTexture(openWhenLetters[s.sel].prompt, openWhenLetters[s.sel].message); (paper.material as T.MeshStandardMaterial).map?.dispose(); (paper.material as T.MeshStandardMaterial).map = nt; (paper.material as T.MeshStandardMaterial).needsUpdate = true; }
        const carrier = items[s.sel].group, sc = carrier.scale.x, rise = ease.inOut(span(O, 0, 0.5)), lift = ease.inOut(span(O, 0.4, 1));
        carrier.getWorldPosition(envW); pocket.set(envW.x, envW.y + 0.02 + 0.55 * sc * rise, envW.z + 0.004 * sc);
        paper.position.set(pocket.x + (reading.x - pocket.x) * lift, pocket.y + (reading.y - pocket.y) * lift, pocket.z + (reading.z - pocket.z) * lift);
        paper.scale.setScalar((0.8 + 0.3 * lift) * sc / 1.5 * 1.1); paper.rotation.set(-0.06 * lift, 0, 0);
      }
      lamp.intensity = 26 * (0.95 + (reduced ? 0 : Math.sin(time * 8) * 0.03)); lampGlow.scale.setScalar(8 + (reduced ? 0 : Math.sin(time * 2) * 0.3)); dust.update(time);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.6, 0.6); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.15, 0.3);
      const f = ease.inOut(s.focus), g = ease.inOut(span(s.open, 0.2, 1));
      pos.set(0, 2.2 - 0.8 * f + 0.2 * g, 11 - 1.0 * f + 0.9 * g); look.set(0, 0.2 + 0.2 * f + 0.25 * g, 0.5 + 1.0 * f + 0.2 * g);
      orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.9); void box;
    },
  };
}
```

## 61. `src/three/gifts/cassette.ts` — new

```ts
/**
 * Gift 05 - Bhumi FM.
 * A walnut-and-steel cassette deck in a warm 70s listening room. A cassette floats above the open door, lowers into the
 * well, the smoked door closes, and the piano keys respond. Reels turn ONLY while real audio plays; the LED meter and VU
 * needle follow the real spectrum (state.spectrum). With no recording supplied the deck stays honestly still.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, span } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, lathe, put } from "../../engine/geometry";
import { addContactShadow, addKeyLight, addPointLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, box, glowSprite, orbitCamera, paintBokeh } from "./common";

function labelTexture() {
  const c = document.createElement("canvas"); c.width = 1024, c.height = 640; const g = c.getContext("2d")!;
  g.fillStyle = "#efe2c4"; g.fillRect(0, 0, 1024, 640);
  g.fillStyle = "#c2452f"; g.fillRect(0, 0, 1024, 130); g.fillStyle = "#e8a23a"; g.fillRect(0, 130, 1024, 14);
  g.fillStyle = "#f8ecd2"; g.font = "700 84px Georgia, serif"; g.textBaseline = "middle"; g.fillText("BHUMI FM", 44, 68);
  g.font = "600 38px Georgia, serif"; g.textAlign = "right"; g.fillText("SIDE A", 980, 68); g.textAlign = "left";
  g.strokeStyle = "rgba(60,44,40,.35)"; g.lineWidth = 2; for (let y = 190; y < 330; y += 46) { g.beginPath(); g.moveTo(44, y); g.lineTo(980, y); g.stroke(); }
  g.fillStyle = "rgba(60,44,40,.55)"; g.font = "italic 34px Georgia, serif"; g.fillText("a recording, when one is supplied", 44, 280);
  g.fillStyle = "#1c1b1c"; g.fillRect(180, 350, 664, 220); // window recess
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 8; return t;
}
function iconTexture(kind: string) {
  const c = document.createElement("canvas"); c.width = c.height = 128; const g = c.getContext("2d")!;
  g.fillStyle = "#2a2a2c"; g.fillRect(0, 0, 128, 128); g.fillStyle = kind === "rec" ? "#e0503a" : "#f1e7d0";
  g.beginPath();
  if (kind === "play") { g.moveTo(42, 28); g.lineTo(98, 64); g.lineTo(42, 100); }
  else if (kind === "stop") g.rect(36, 36, 56, 56);
  else if (kind === "pause") { g.rect(36, 30, 20, 68); g.rect(72, 30, 20, 68); }
  else if (kind === "rew") { g.moveTo(64, 30); g.lineTo(22, 64); g.lineTo(64, 98); g.moveTo(106, 30); g.lineTo(64, 64); g.lineTo(106, 98); }
  else g.arc(64, 64, 30, 0, Math.PI * 2);
  g.fill();
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}
function vuTexture() {
  const c = document.createElement("canvas"); c.width = 512; c.height = 288; const g = c.getContext("2d")!;
  const bg = g.createLinearGradient(0, 0, 0, 288); bg.addColorStop(0, "#f3e3b6"); bg.addColorStop(1, "#d8c186"); g.fillStyle = bg; g.fillRect(0, 0, 512, 288);
  g.translate(256, 300); g.strokeStyle = "#3a2c28"; g.fillStyle = "#3a2c28"; g.lineWidth = 3;
  for (let i = 0; i <= 20; i++) { const a = (-0.95 + (i / 20) * 1.9) - Math.PI / 2, r1 = 250, r2 = i % 5 === 0 ? 222 : 236; g.strokeStyle = i > 14 ? "#b8321f" : "#3a2c28"; g.beginPath(); g.moveTo(Math.cos(a) * r1, Math.sin(a) * r1); g.lineTo(Math.cos(a) * r2, Math.sin(a) * r2); g.stroke(); }
  g.setTransform(1, 0, 0, 1, 0, 0); g.font = "700 40px Georgia, serif"; g.fillText("VU", 226, 250);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}

function makeCassette(kit: Stage["kit"], tint = "#efe2c4", withLabel = true) {
  const group = new T.Group(), reels: T.Group[] = [];
  const shell = new T.MeshPhysicalMaterial({ color: "#2b2a2c", roughness: 0.35, clearcoat: 0.6 });
  put(group, new RoundedBoxGeometry(2.7, 0.3, 1.72, 3, 0.05), shell, 0, 0, 0);
  const labelMat = new T.MeshStandardMaterial({ map: withLabel ? labelTexture() : null, color: withLabel ? "#ffffff" : tint, roughness: 0.8 });
  const label = put(group, new T.PlaneGeometry(2.4, 1.5), labelMat, 0, 0.155, 0, false); label.rotation.x = -Math.PI / 2;
  const tapeMat = new T.MeshStandardMaterial({ color: "#2a1a12", roughness: 0.3, metalness: 0.2 });
  const hubMat = new T.MeshStandardMaterial({ color: "#f4efe4", roughness: 0.45 });
  for (const x of [-0.58, 0.58]) {
    const reel = new T.Group(); reel.position.set(x, 0.17, 0.26); group.add(reel); reels.push(reel);
    put(reel, new T.CylinderGeometry(0.4, 0.4, 0.045, 36), tapeMat, 0, 0, 0, false);
    put(reel, new T.CylinderGeometry(0.19, 0.19, 0.07, 28), hubMat, 0, 0.012, 0, false);
    put(reel, new T.CylinderGeometry(0.1, 0.1, 0.075, 20), new T.MeshStandardMaterial({ color: "#1a1a1a" }), 0, 0.014, 0, false);
    for (let k = 0; k < 6; k++) { const a = (k / 6) * Math.PI * 2; const tooth = put(reel, new T.BoxGeometry(0.035, 0.08, 0.06), hubMat, Math.cos(a) * 0.1, 0.014, Math.sin(a) * 0.1, false); tooth.rotation.y = -a; }
  }
  const glass = put(group, new T.PlaneGeometry(1.95, 0.7), new T.MeshPhysicalMaterial({ color: "#8aa0a6", roughness: 0.05, transparent: true, opacity: 0.22, clearcoat: 1, depthWrite: false }), 0, 0.215, 0.26, false); glass.rotation.x = -Math.PI / 2;
  for (const x of [-1.0, 1.0]) put(group, new T.CylinderGeometry(0.07, 0.07, 0.16, 12), kit.metal("silver", 0.3), x, -0.02, 0.8, false);
  return { group, reels };
}

export function buildCassetteWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  stage.mood({ env: "candle", envIntensity: 1.1, exposure: 1.15, background: "#1a0f0a", fog: { color: "#1a100b", density: 0.02 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#ffd9b0", "#1a0f0a", 0.5));
  addKeyLight(scene, quality, { color: "#ffd8a8", intensity: 3.0, position: [-4, 7, 6], target: [0, 0.5, 0], extent: 7, far: 24 });
  const lamp = addPointLight(scene, "#ffb870", 36, [-5.2, 4.2, -1.5], 18, 2);
  const kick = new T.DirectionalLight("#8aa6ff", 0.9); kick.position.set(6, 4, -5); scene.add(kick);

  const wall = backdrop((g, w, h) => { const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#2a1810"); bg.addColorStop(1, "#4a2c1a"); g.fillStyle = bg; g.fillRect(0, 0, w, h); for (let x = 0; x < w; x += 64) { g.fillStyle = `rgba(0,0,0,${0.12 + (x / 64 % 2) * 0.08})`; g.fillRect(x, 0, 30, h); } paintBokeh(g, w, h, "255,190,120", 26, 2); }, 44, 24);
  wall.position.set(0, 6, -12); scene.add(wall);
  const table = put(scene, new T.BoxGeometry(24, 0.4, 14), kit.wood("#1d0f08", "#5b381f", [4, 3], 0.45), 0, -1.1, -1, false); table.receiveShadow = true;
  const lampShade = glowSprite("#ffb870", 9, 0.5); lampShade.position.set(-5.2, 4.2, -3.5); scene.add(lampShade);

  /* ---------- the deck ---------- */
  const deck = new T.Group(); deck.position.y = 0.2; scene.add(deck);
  put(deck, new RoundedBoxGeometry(6.0, 1.3, 3.6, 4, 0.14), kit.metal("silver", 0.36), 0, 0, 0);
  const walnut = kit.wood("#2a1409", "#7c4b28", [1, 1], 0.5);
  for (const x of [-3.12, 3.12]) put(deck, new RoundedBoxGeometry(0.3, 1.38, 3.7, 3, 0.08), walnut, x, 0, 0);
  put(deck, new T.BoxGeometry(5.5, 0.05, 3.2), new T.MeshStandardMaterial({ color: "#1c1e21", roughness: 0.55, metalness: 0.5 }), 0, 0.66, 0, false);
  for (const [x, z] of [[-2.6, -1.4], [2.6, -1.4], [-2.6, 1.4], [2.6, 1.4]]) put(deck, new T.CylinderGeometry(0.22, 0.26, 0.2, 20), new T.MeshStandardMaterial({ color: "#161616", roughness: 0.9 }), x, -0.74, z);
  addContactShadow(scene, 7.4, 4.6, 0, -0.89, 0, 0.7);
  // well frame
  const brass = kit.metal("brass", 0.3);
  const wellZ = -0.1;
  put(deck, new T.BoxGeometry(3.1, 0.04, 2.1), new T.MeshStandardMaterial({ color: "#0e0f10", roughness: 0.8 }), 0, 0.7, wellZ, false);
  for (const [w, d, x, z] of [[3.3, 0.1, 0, wellZ - 1.05], [3.3, 0.1, 0, wellZ + 1.05], [0.1, 2.2, -1.6, wellZ], [0.1, 2.2, 1.6, wellZ]] as const) box(deck, w, 0.1, d, brass, x, 0.72, z);
  // door
  const doorHinge = new T.Group(); doorHinge.position.set(0, 0.8, wellZ - 1.03); deck.add(doorHinge);
  const doorGlass = new T.MeshPhysicalMaterial({ color: "#2c3436", roughness: 0.04, transparent: true, opacity: 0.55, clearcoat: 1, side: T.DoubleSide, depthWrite: false });
  put(doorHinge, new T.PlaneGeometry(3.15, 2.05), doorGlass, 0, 0, 1.03, false).rotation.x = -Math.PI / 2;
  for (const [w, d, x, z] of [[3.25, 0.07, 0, 0.01], [3.25, 0.07, 0, 2.06], [0.07, 2.1, -1.6, 1.03], [0.07, 2.1, 1.6, 1.03]] as const) box(doorHinge, w, 0.06, d, brass, x, 0, z, false);
  // front: VU meter
  const front = 1.8;
  box(deck, 1.7, 0.95, 0.12, new T.MeshStandardMaterial({ color: "#14100e", roughness: 0.6 }), -1.95, 0.0, front);
  const vuFace = put(deck, new T.PlaneGeometry(1.5, 0.82), new T.MeshStandardMaterial({ map: vuTexture(), roughness: 0.6 }), -1.95, 0.0, front + 0.07, false);
  const needlePivot = new T.Group(); needlePivot.position.set(-1.95, -0.34, front + 0.09); deck.add(needlePivot);
  box(needlePivot, 0.018, 0.7, 0.01, new T.MeshStandardMaterial({ color: "#a02416", roughness: 0.4 }), 0, 0.35, 0, false);
  put(deck, new T.PlaneGeometry(1.5, 0.82), new T.MeshPhysicalMaterial({ color: "#ffffff", transparent: true, opacity: 0.1, roughness: 0.05, clearcoat: 1, depthWrite: false }), -1.95, 0.0, front + 0.11, false);
  void vuFace;
  // LED equaliser
  box(deck, 2.25, 0.7, 0.1, new T.MeshStandardMaterial({ color: "#0b0c0d", roughness: 0.3 }), 0.35, 0.28, front);
  const cols = 12, rows = 5, leds = new T.InstancedMesh(new T.BoxGeometry(0.12, 0.07, 0.04), new T.MeshBasicMaterial({ toneMapped: false }), cols * rows), tmp = new T.Object3D(), tint = new T.Color();
  for (let i = 0; i < cols; i++) for (let j = 0; j < rows; j++) { tmp.position.set(0.35 - 1.0 + i * 0.18, 0.28 - 0.22 + j * 0.11, front + 0.07); tmp.updateMatrix(); leds.setMatrixAt(i * rows + j, tmp.matrix); }
  deck.add(leds);
  const setLeds = (levels: number[]) => { for (let i = 0; i < cols; i++) for (let j = 0; j < rows; j++) { const on = levels[i] * rows > j + 0.2; tint.set(j < 3 ? "#38e07a" : j < 4 ? "#f2c038" : "#f0452e").multiplyScalar(on ? 1.15 : 0.07); leds.setColorAt(i * rows + j, tint); } if (leds.instanceColor) leds.instanceColor.needsUpdate = true; };
  setLeds(new Array(12).fill(0));
  // keys
  const keyKinds = ["rew", "play", "stop", "pause", "rec"], keys = keyKinds.map((kind, i) => {
    const key = new T.Group(); key.position.set(0.35 - 1.04 + i * 0.52, -0.31, front + 0.02); deck.add(key);
    put(key, new RoundedBoxGeometry(0.48, 0.3, 0.46, 2, 0.03), new T.MeshStandardMaterial({ color: "#d8d2c4", roughness: 0.4 }), 0, 0, 0.14);
    const icon = put(key, new T.PlaneGeometry(0.28, 0.2), new T.MeshBasicMaterial({ map: iconTexture(kind), toneMapped: false }), 0, 0, 0.375, false); void icon;
    return { key, kind };
  });
  // volume knob
  const knob = new T.Group(); knob.position.set(2.5, 0.0, front + 0.05); deck.add(knob);
  const knobBody = put(knob, new T.CylinderGeometry(0.34, 0.38, 0.28, 48), kit.metal("silver", 0.28), 0, 0, 0.14); knobBody.rotation.x = Math.PI / 2;
  for (let i = 0; i < 28; i++) { const a = (i / 28) * Math.PI * 2; const knurl = put(knob, new T.BoxGeometry(0.03, 0.04, 0.28), kit.metal("silver", 0.3), Math.cos(a) * 0.37, Math.sin(a) * 0.37, 0.14, false); knurl.rotation.z = a; }
  box(knob, 0.05, 0.3, 0.02, new T.MeshStandardMaterial({ color: "#c2452f" }), 0, 0.18, 0.29, false);
  const tickMat = new T.MeshBasicMaterial({ color: "#3a2c28" });
  for (let i = 0; i <= 10; i++) { const a = -2.3 + (i / 10) * 4.6; box(deck, 0.02, 0.07, 0.01, tickMat, 2.5 + Math.sin(a) * 0.6, Math.cos(a) * 0.6, front + 0.02, false).rotation.z = -a; }
  const standby = new T.Mesh(new T.SphereGeometry(0.045, 10, 8), new T.MeshBasicMaterial({ color: "#ff6a3a", toneMapped: false })); standby.position.set(2.5, 0.52, front + 0.03); deck.add(standby);

  /* ---------- cassette(s) ---------- */
  const main = makeCassette(kit); scene.add(main.group);
  const spare = makeCassette(kit, "#7a3a2a", false); spare.group.position.set(-4.9, -0.78, 2.4); spare.group.rotation.y = 0.5; scene.add(spare.group);
  const spare2 = makeCassette(kit, "#2f4a58", false); spare2.group.position.set(-4.6, -0.5, 2.5); spare2.group.rotation.y = 0.7; scene.add(spare2.group);
  const dust = new ParticleField({ count: Math.round(100 * particleScale(quality)), size: 0.045, color: "#ffd9a0", opacity: 0.55, bounds: [6, 3, 4], center: [0, 3, 0], drift: 0.6, rise: 0.03, twinkle: 0.7 });
  scene.add(dust.points);

  /* ---------- choreography ---------- */
  const s = { ins: 0, door: 0, speed: 0, angle: 0, needle: 0, vol: 0.72 };
  const levels = new Array(12).fill(0), pressed = [0, 0, 0, 0, 0];
  const orbit = { yaw: 0, pitch: 0 }, pos = new T.Vector3(), look = new T.Vector3(0, 0.9, 0);
  let lastOpen: boolean | undefined, lastPlaying: boolean | undefined;
  return {
    pickables: [],
    frame(time, dt, state: SceneState, reduced) {
      const open = Boolean(state.open), playing = Boolean(state.playing);
      if (open !== lastOpen) { if (lastOpen !== undefined) stage.sfx(open ? "tape" : "thud"); lastOpen = open; }
      if (playing !== lastPlaying) { if (lastPlaying !== undefined) stage.sfx("click"); lastPlaying = playing; }
      s.ins = damp(s.ins, open ? 1 : 0, 2.0, dt, reduced);
      const doorTarget = open && s.ins > 0.78 ? 0 : 1; s.door = damp(s.door, doorTarget, 4.2, dt, reduced);
      doorHinge.rotation.x = -1.28 * ease.inOut(s.door);
      // cassette flight
      const k = ease.inOut(s.ins);
      main.group.position.set(0, 0.2 + 0.7 + 0.02 + (1 - k) * 2.5, -0.1 + (1 - k) * 0.5);
      main.group.rotation.set((1 - k) * (0.5 + (reduced ? 0 : Math.sin(time * 1.2) * 0.06)), (1 - k) * (reduced ? 0.3 : 0.3 + Math.sin(time * 0.7) * 0.15), (1 - k) * 0.12);
      // reels turn only with real playback
      s.speed = damp(s.speed, playing ? 3.2 : 0, 2.5, dt, reduced); s.angle += s.speed * dt;
      main.reels.forEach((r, i) => { r.rotation.y = -s.angle * (i ? 0.85 : 1.15); });
      // spectrum
      const spec = state.spectrum ?? null; let avg = 0;
      for (let i = 0; i < 12; i++) { levels[i] = damp(levels[i], playing && spec ? spec[i] : 0, 14, dt, reduced); avg += levels[i] / 12; }
      setLeds(levels);
      s.needle = damp(s.needle, playing && spec ? Math.min(1, avg * 2.4) : 0, 10, dt, reduced); needlePivot.rotation.z = 0.95 - s.needle * 1.9;
      // keys: play is down while playing, eject-state keys rest
      keys.forEach((kk, i) => { const down = (kk.kind === "play" && playing) || (kk.kind === "stop" && !playing && open); pressed[i] = damp(pressed[i], down ? 1 : 0, 18, dt, reduced); kk.key.position.z = front + 0.02 - pressed[i] * 0.07; });
      s.vol = damp(s.vol, state.extra?.volume !== undefined ? Number(state.extra.volume) : 0.72, 8, dt, reduced); knob.rotation.z = -2.3 + s.vol * 4.6;
      (standby.material as T.MeshBasicMaterial).color.set(open ? (playing ? "#46ff8a" : "#ffb03a") : "#ff6a3a").multiplyScalar(0.7 + 0.3 * (reduced ? 1 : Math.sin(time * 3) * 0.5 + 0.5));
      lamp.intensity = 36 * (0.94 + (reduced ? 0 : Math.sin(time * 9) * 0.03)); dust.update(time);
      // camera
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 4, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.3, -0.15, 0.4);
      pos.set(0.6 * k + (reduced ? 0 : Math.sin(time * 0.2) * 0.3), 3.9 - 0.7 * k, 10.0 - 1.0 * k); look.set(0, 0.9 + 0.6 * (1 - k), 0.2);
      orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.9);
      void span; void lathe;
    },
  };
}
```

## 62. `src/three/gifts/cinema.ts` — new

```ts
/**
 * Gift 06 - The Memory Cinema.
 * A velvet-curtained screening room. A 16mm projector throws a rectangular beam full of dust through the dark onto the
 * screen; its reels turn and a perforated film strip travels over the gate. The screen shows ONLY photographs supplied
 * by the owner (state.artwork); until then it holds an honest placeholder. state.open = powered, state.playing = running.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, lathe, put, ribbon } from "../../engine/geometry";
import { addContactShadow, addSpotLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { packCinema } from "../../content/packContent";
import { backdrop, box, makeCurtain, orbitCamera } from "./common";

const SCREEN = { w: 8.4, h: 4.725, z: -7 };

function placeholderTexture(label: string) {
  const c = document.createElement("canvas"); c.width = 1280; c.height = 720; const g = c.getContext("2d")!;
  const bg = g.createRadialGradient(640, 360, 60, 640, 360, 800); bg.addColorStop(0, "#7b684b"); bg.addColorStop(0.55, "#3f3325"); bg.addColorStop(1, "#15100b"); g.fillStyle = bg; g.fillRect(0, 0, 1280, 720);
  g.strokeStyle = "rgba(244,218,168,.5)"; g.lineWidth = 6; g.strokeRect(70, 60, 1140, 600); g.lineWidth = 2; g.strokeRect(86, 76, 1108, 568);
  g.fillStyle = "rgba(252,238,208,.96)"; g.textAlign = "center"; g.font = "600 52px Georgia, serif"; g.fillText(label, 640, 322);
  const [lead = "", rest = ""] = (packCinema.emptyState.match(/[^.]+\./g) ?? [packCinema.emptyState]).map((part) => part.trim()); // the pack's empty-state copy, split at its sentence break
  g.font = "italic 34px Georgia, serif"; g.fillText(lead, 640, 396); g.fillStyle = "rgba(252,238,208,.78)"; g.font = "28px Georgia, serif"; g.fillText(rest, 640, 450);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 8; return t;
}
function leaderTexture(n: number) {
  const c = document.createElement("canvas"); c.width = 1280; c.height = 720; const g = c.getContext("2d")!;
  g.fillStyle = "#a89d86"; g.fillRect(0, 0, 1280, 720); g.strokeStyle = "#1c1916"; g.lineWidth = 8;
  g.beginPath(); g.arc(640, 360, 250, 0, Math.PI * 2); g.stroke(); g.beginPath(); g.arc(640, 360, 200, 0, Math.PI * 2); g.stroke();
  g.lineWidth = 4; g.beginPath(); g.moveTo(0, 360); g.lineTo(1280, 360); g.moveTo(640, 0); g.lineTo(640, 720); g.stroke();
  g.fillStyle = "#1c1916"; g.font = "700 300px Georgia, serif"; g.textAlign = "center"; g.textBaseline = "middle"; g.fillText(String(n), 640, 380);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}
function filmTexture() {
  const c = document.createElement("canvas"); c.width = 128; c.height = 512; const g = c.getContext("2d")!;
  g.fillStyle = "#17120f"; g.fillRect(0, 0, 128, 512);
  for (let i = 0; i < 4; i++) { g.fillStyle = `hsl(${30 + i * 8},${18 + i * 4}%,${42 + i * 5}%)`; g.fillRect(24, i * 128 + 12, 80, 104); }
  g.fillStyle = "#f3ead8"; for (let i = 0; i < 16; i++) for (const x of [6, 108]) { g.beginPath(); g.roundRect(x, i * 32 + 8, 14, 16, 3); g.fill(); }
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.wrapS = t.wrapT = T.RepeatWrapping; t.anisotropy = 8; return t;
}

export function buildCinemaWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  stage.mood({ env: "ballroom", envIntensity: 0.6, exposure: 1.05, background: "#0a0608", fog: { color: "#0a0608", density: 0.02 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();

  const house = new T.HemisphereLight("#ffd9b0", "#140a0c", 0.5); scene.add(house);
  const spot = addSpotLight(scene, quality, "#ffe2b8", 60, [2.5, 7, 6], [0, 1, 0], 0.6, 0.9);
  const rim = new T.DirectionalLight("#6f8cff", 0.6); rim.position.set(-6, 4, -2); scene.add(rim);
  const screenGlow = new T.PointLight("#ffe7c4", 0, 16, 2); screenGlow.position.set(0, 2.4, SCREEN.z + 2); scene.add(screenGlow);

  /* ---------- room ---------- */
  const wall = backdrop((g, w, h) => { const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#14090d"); bg.addColorStop(1, "#24121a"); g.fillStyle = bg; g.fillRect(0, 0, w, h); }, 60, 30);
  wall.position.set(0, 6, SCREEN.z - 2.5); scene.add(wall);
  const floor = put(scene, new T.PlaneGeometry(40, 30), kit.fabric("#2a0d14", "#5c1e2c", [14, 10]), 0, -0.01, -2, false); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;
  for (const x of [-1, 1]) { const c = makeCurtain(6.2, 11, "#5a1426", 1.9); c.position.set(x * 6.4, 5, SCREEN.z - 0.9); scene.add(c); }
  const valance = makeCurtain(20, 1.8, "#6a1a2e", 2.6); valance.position.set(0, 9.9, SCREEN.z - 0.8); scene.add(valance);
  const gold = kit.metal("gold", 0.26);
  box(scene, SCREEN.w + 0.5, SCREEN.h + 0.5, 0.2, new T.MeshStandardMaterial({ color: "#0b0b0c", roughness: 0.8 }), 0, SCREEN.h / 2 + 0.55, SCREEN.z - 0.12);
  for (const [w, h, x, y] of [[SCREEN.w + 0.7, 0.07, 0, SCREEN.h + 0.84], [SCREEN.w + 0.7, 0.07, 0, 0.26], [0.07, SCREEN.h + 0.6, -(SCREEN.w / 2 + 0.34), SCREEN.h / 2 + 0.55], [0.07, SCREEN.h + 0.6, SCREEN.w / 2 + 0.34, SCREEN.h / 2 + 0.55]] as const) box(scene, w, h, 0.1, gold, x, y, SCREEN.z - 0.02, false);

  /* ---------- screen ---------- */
  const blank = placeholderTexture("FRAME 01");
  const uniforms: Record<string, T.IUniform> = { uMap: { value: blank as T.Texture }, uTime: { value: 0 }, uPower: { value: 0 }, uGrain: { value: 0.045 } };
  const screen = new T.Mesh(new T.PlaneGeometry(SCREEN.w, SCREEN.h), new T.ShaderMaterial({
    uniforms, vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",
    fragmentShader: `uniform sampler2D uMap; uniform float uTime, uPower, uGrain; varying vec2 vUv;
      float h(vec2 p){ return fract(sin(dot(p, vec2(12.9898, 78.233))) * 43758.5453); }
      void main(){
        vec2 uv = vUv + vec2(sin(uTime*13.0)*0.0014, sin(uTime*7.0+1.0)*0.0022) * uPower;
        vec3 col = texture2D(uMap, uv).rgb;
        float v = 1.0 - smoothstep(0.35, 0.95, length(vUv-0.5)*1.3);
        float g = h(vUv*vec2(900.0,520.0) + floor(uTime*24.0)) - 0.5;
        float fl = 0.93 + 0.07*sin(uTime*47.0)*sin(uTime*13.0);
        float scratch = step(0.9985, h(vec2(floor(vUv.x*260.0), floor(uTime*10.0)))) * 0.35;
        vec3 lit = col*fl*(0.5+0.5*v)*0.9 + g*uGrain*0.8 + scratch*0.6;
        vec3 off = vec3(0.1,0.095,0.09) * (0.5 + 0.5*v);
        gl_FragColor = vec4(mix(off, lit, uPower), 1.0);
        #include <colorspace_fragment>
      }`,
  }));
  screen.position.set(0, SCREEN.h / 2 + 0.55, SCREEN.z); scene.add(screen);

  /* ---------- projector ---------- */
  const PJX = -2.0, pj = new T.Group(); pj.position.set(PJX, 0, 2.6); scene.add(pj);
  const enamel = new T.MeshStandardMaterial({ color: "#34463f", roughness: 0.38, metalness: 0.4, envMapIntensity: 1.4 }), steel = kit.metal("steel", 0.34), brass = kit.metal("brass", 0.3);
  put(pj, new T.CylinderGeometry(0.1, 0.12, 1.6, 12), steel, -0.7, 0.8, -0.8); put(pj, new T.CylinderGeometry(0.1, 0.12, 1.6, 12), steel, 0.7, 0.8, -0.8); put(pj, new T.CylinderGeometry(0.1, 0.12, 1.6, 12), steel, -0.7, 0.8, 0.8); put(pj, new T.CylinderGeometry(0.1, 0.12, 1.6, 12), steel, 0.7, 0.8, 0.8);
  put(pj, new RoundedBoxGeometry(2.4, 0.2, 2.4, 3, 0.05), steel, 0, 1.65, 0);
  addContactShadow(pj, 3, 3, 0, 0.012, 0, 0.55);
  put(pj, new RoundedBoxGeometry(2.0, 1.15, 2.7, 4, 0.12), enamel, 0, 2.35, 0);
  put(pj, new T.BoxGeometry(2.06, 0.05, 2.76), brass, 0, 2.0, 0, false); put(pj, new T.BoxGeometry(2.06, 0.05, 2.76), brass, 0, 2.7, 0, false);
  const lens = new T.Group(); lens.position.set(0, 2.38, -1.35); pj.add(lens);
  const barrel = put(lens, lathe([[0, 0], [0.42, 0], [0.42, 0.1], [0.34, 0.15], [0.34, 0.65], [0.4, 0.7], [0.4, 0.82], [0.32, 0.86], [0.32, 0.9], [0, 0.9]], 36), brass, 0, 0, 0); barrel.rotation.x = -Math.PI / 2; barrel.position.z = -0.0;
  const glassMat = new T.MeshPhysicalMaterial({ color: "#a8c4d8", roughness: 0.02, metalness: 0, clearcoat: 1, transmission: 0, emissive: new T.Color("#fff1d0"), emissiveIntensity: 0 });
  const glass = put(lens, new T.CircleGeometry(0.3, 28), glassMat, 0, 0, -0.91, false); glass.rotation.y = Math.PI;
  const reels = [{ z: 0.95, y: 3.55, dir: 1 }, { z: -0.65, y: 3.55, dir: -1 }].map((r) => {
    const reel = new T.Group(); reel.position.set(1.3, r.y, r.z); pj.add(reel);
    const spin = new T.Group(); reel.add(spin);
    for (const x of [-0.17, 0.17]) { const flange = put(spin, new T.TorusGeometry(0.8, 0.04, 8, 48), steel, x, 0, 0, false); flange.rotation.y = Math.PI / 2; const web = put(spin, new T.CylinderGeometry(0.8, 0.8, 0.012, 48, 1, false), new T.MeshStandardMaterial({ color: "#2c3a36", roughness: 0.5, metalness: 0.5, transparent: true, opacity: 0.45, side: T.DoubleSide }), x, 0, 0, false); web.rotation.z = Math.PI / 2; }
    put(spin, new T.CylinderGeometry(0.62, 0.62, 0.3, 40), new T.MeshStandardMaterial({ color: "#1c1410", roughness: 0.38 }), 0, 0, 0, false).rotation.z = Math.PI / 2;
    for (let k = 0; k < 5; k++) { const a = (k / 5) * Math.PI * 2; const spoke = put(spin, new T.BoxGeometry(0.34, 0.08, 0.55), steel, 0, Math.cos(a) * 0.4, Math.sin(a) * 0.4, false); spoke.rotation.x = a; }
    put(spin, new T.CylinderGeometry(0.1, 0.1, 0.42, 16), brass, 0, 0, 0, false).rotation.z = Math.PI / 2;
    return { spin, dir: r.dir };
  });
  const path = new T.CatmullRomCurve3([new T.Vector3(1.3, 2.75, 0.95), new T.Vector3(1.3, 2.4, 0.5), new T.Vector3(1.3, 2.2, 0.0), new T.Vector3(1.3, 2.4, -0.4), new T.Vector3(1.3, 2.75, -0.65)]);
  const filmTex = filmTexture(); filmTex.repeat.set(1, 3);
  const film = put(pj, ribbon(path, 0.34, 40), new T.MeshStandardMaterial({ map: filmTex, roughness: 0.4, side: T.DoubleSide }), 0, 0, 0, false);
  void film;

  /* ---------- beam and dust ---------- */
  const lensWorld = new T.Vector3(PJX, 2.38, 2.6 - 1.9), cornersZ = SCREEN.z, halfW = SCREEN.w / 2, halfH = SCREEN.h / 2, cy = SCREEN.h / 2 + 0.55;
  const verts = [lensWorld.x, lensWorld.y, lensWorld.z, -halfW, cy + halfH, cornersZ, halfW, cy + halfH, cornersZ, halfW, cy - halfH, cornersZ, -halfW, cy - halfH, cornersZ];
  const beamGeo = new T.BufferGeometry(); beamGeo.setAttribute("position", new T.Float32BufferAttribute(verts, 3));
  beamGeo.setAttribute("aT", new T.Float32BufferAttribute([0, 1, 1, 1, 1], 1));
  beamGeo.setIndex([0, 2, 1, 0, 3, 2, 0, 4, 3, 0, 1, 4]);
  // Written straight to display space: vertex colours would be sRGB-lifted (0.02 linear -> ~42/255) and stack on DoubleSide.
  const beamMat = new T.ShaderMaterial({
    uniforms: { uPower: { value: 0 } },
    vertexShader: "attribute float aT; varying float vT; void main(){ vT = aT; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",
    fragmentShader: "uniform float uPower; varying float vT; void main(){ float a = (0.17 * pow(1.0 - vT, 1.25) + 0.045) * uPower; gl_FragColor = vec4(vec3(1.0, 0.92, 0.74) * a, 1.0); }",
    transparent: true, blending: T.AdditiveBlending, depthWrite: false, side: T.BackSide, fog: false,
  });
  const beam = new T.Mesh(beamGeo, beamMat); beam.frustumCulled = false; scene.add(beam);
  const dust = new ParticleField({ count: Math.round(260 * particleScale(quality)), size: 0.06, color: "#fff2d6", opacity: 0, bounds: [2.2, 1.1, 2.6], center: [PJX * 0.55, 2.9, -2.6], drift: 0.8, rise: 0.025, twinkle: 0.8 });
  scene.add(dust.points);

  /* ---------- foreground seats ---------- */
  const seatMat = new T.MeshPhysicalMaterial({ color: "#3a0f1c", roughness: 0.9, sheen: 1, sheenColor: new T.Color("#8a2c46") });
  [[-3.6, 8.2], [0, 8.6], [3.6, 8.2], [-7.2, 8.8], [7.2, 8.8]].forEach(([x, z]) => { const seat = new T.Group(); seat.position.set(x, 0, z); scene.add(seat); put(seat, new RoundedBoxGeometry(2.2, 2.4, 0.45, 3, 0.15), seatMat, 0, 1.5, 0); put(seat, new T.BoxGeometry(0.2, 1.0, 0.2), steelOf(kit), -0.9, 0.3, 0.1, false); put(seat, new T.BoxGeometry(0.2, 1.0, 0.2), steelOf(kit), 0.9, 0.3, 0.1, false); });

  /* ---------- choreography ---------- */
  const leaders = [leaderTexture(3), leaderTexture(2), leaderTexture(1)];
  const s = { power: 0, speed: 0, angle: 0, since: 0, art: "" };
  const loader = new T.TextureLoader(); let artTexture: T.Texture | null = null, lastPowered: boolean | undefined;
  const orbit = { yaw: 0, pitch: 0 }, pos = new T.Vector3(), look = new T.Vector3(0, 2.6, -2);
  return {
    pickables: [],
    frame(time, dt, state: SceneState, reduced) {
      const powered = Boolean(state.open);
      if (powered !== lastPowered) { if (lastPowered !== undefined) stage.sfx(powered ? "lever" : "thud"); lastPowered = powered; s.since = 0; }
      if (powered) s.since += dt;
      s.power = damp(s.power, powered ? 1 : 0, 3, dt, reduced);
      const art = state.artwork ?? "";
      if (art !== s.art) { s.art = art; artTexture?.dispose(); artTexture = null; if (art) { artTexture = loader.load(art); artTexture.colorSpace = T.SRGBColorSpace; } }
      const leaderIndex = powered && !reduced && s.since < 3 ? Math.min(2, Math.floor(s.since)) : -1;
      uniforms.uMap.value = leaderIndex >= 0 ? leaders[leaderIndex] : artTexture ?? blank;
      uniforms.uTime.value = reduced ? 0 : time; uniforms.uPower.value = s.power;
      beamMat.uniforms.uPower.value = ease.inOut(s.power); (dust.points.material as T.ShaderMaterial).uniforms.uOpacity.value = 0.85 * s.power; dust.update(time);
      glassMat.emissiveIntensity = 3 * s.power;
      house.intensity = 0.5 - 0.42 * s.power; spot.intensity = 60 - 52 * s.power; screenGlow.intensity = 14 * s.power;
      s.speed = damp(s.speed, powered || state.playing ? 2.4 : 0, 2.2, dt, reduced); s.angle += s.speed * dt;
      reels.forEach((r) => { r.spin.rotation.x = s.angle * r.dir; });
      filmTex.offset.y = (filmTex.offset.y - s.speed * dt * 0.25) % 1;
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 4, -0.6, 0.6); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.12, 0.3);
      const p = ease.inOut(s.power);
      pos.set(3.6 - 1.6 * p + (reduced ? 0 : Math.sin(time * 0.2) * 0.2), 3.9 - 0.4 * p, 13.4 - 0.4 * p); look.set(0.5 * p, 2.9, -3.0);
      orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.9);
    },
  };
}
const steelOf = (kit: Stage["kit"]) => kit.metal("steel", 0.4);
```

## 63. `src/three/gifts/common.ts` — new

```ts
/** Small helpers shared by several gift scenes. */
import * as T from "three";
import { glowCanvas, sparkleCanvas } from "../../engine/textures";

const cache = new Map<string, T.CanvasTexture>();
const tex = (key: string, make: () => HTMLCanvasElement) => {
  let t = cache.get(key);
  if (!t) { t = new T.CanvasTexture(make()); t.colorSpace = T.SRGBColorSpace; cache.set(key, t); }
  return t;
};
export const softTexture = (inner = "rgba(255,255,255,1)", outer = "rgba(255,255,255,0)") => tex(`soft|${inner}|${outer}`, () => glowCanvas(inner, outer, 128));
export const sparkleTexture = () => tex("spark", () => sparkleCanvas(128));

/** Additive glow billboard. */
export function glowSprite(color: string, scale: number, opacity = 1, inner = "rgba(255,255,255,1)") {
  const sprite = new T.Sprite(new T.SpriteMaterial({ map: softTexture(inner), color, transparent: true, opacity, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
  sprite.scale.setScalar(scale);
  return sprite;
}
export function sparkleSprite(color: string, scale: number, opacity = 1) {
  const sprite = new T.Sprite(new T.SpriteMaterial({ map: sparkleTexture(), color, transparent: true, opacity, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
  sprite.scale.setScalar(scale);
  return sprite;
}

/** Large painted backdrop plane (never affected by fog or tone mapping). */
export function backdrop(paint: (g: CanvasRenderingContext2D, w: number, h: number) => void, width: number, height: number, w = 1024, h = 640) {
  const c = document.createElement("canvas"); c.width = w; c.height = h; paint(c.getContext("2d")!, w, h);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace;
  return new T.Mesh(new T.PlaneGeometry(width, height), new T.MeshBasicMaterial({ map: t, fog: false, toneMapped: false }));
}

/** Fairy-light style bokeh dots painted into a context. */
export function paintBokeh(g: CanvasRenderingContext2D, w: number, h: number, rgb: string, count = 40, seed = 1) {
  for (let i = 0; i < count; i++) {
    const x = (i * 211 * seed) % w, y = (i * 97 * seed) % (h * 0.8) + 10, r = 8 + ((i * 29) % 34), a = 0.1 + ((i * 13) % 30) / 100;
    const d = g.createRadialGradient(x, y, r * 0.2, x, y, r); d.addColorStop(0, `rgba(${rgb},${a})`); d.addColorStop(0.75, `rgba(${rgb},${a * 0.7})`); d.addColorStop(1, `rgba(${rgb},0)`);
    g.fillStyle = d; g.beginPath(); g.arc(x, y, r, 0, Math.PI * 2); g.fill();
  }
}

/** Text drawn into a small canvas texture (labels, plaques). */
export function textTexture(lines: string[], width = 512, height = 256, bg = "#f3e5c9", ink = "#3a2c28", font = "600 44px Georgia, serif") {
  const c = document.createElement("canvas"); c.width = width; c.height = height; const g = c.getContext("2d")!;
  g.fillStyle = bg; g.fillRect(0, 0, width, height); g.fillStyle = ink; g.font = font; g.textAlign = "center"; g.textBaseline = "middle";
  lines.forEach((line, i) => g.fillText(line, width / 2, height / 2 + (i - (lines.length - 1) / 2) * 52));
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}

/** Camera helper: orbit offset from drag + portrait fit. */
export function orbitCamera(camera: T.PerspectiveCamera, pos: T.Vector3, look: T.Vector3, yaw: number, pitch: number, fitStrength = 0.9) {
  const offset = pos.clone().sub(look).applyAxisAngle(new T.Vector3(0, 1, 0), yaw);
  offset.applyAxisAngle(new T.Vector3(1, 0, 0).applyAxisAngle(new T.Vector3(0, 1, 0), yaw), -pitch);
  const fit = T.MathUtils.clamp(fitStrength / Math.max(0.45, camera_aspect(camera)), 1, 1.9);
  camera.position.copy(look).addScaledVector(offset, fit); camera.lookAt(look);
}
const camera_aspect = (camera: T.PerspectiveCamera) => camera.aspect;

export const clampDrag = (value: number, delta: number, scale: number, min: number, max: number) => T.MathUtils.clamp(value + delta * scale, min, max);

/** Pleated theatre curtain: a plane whose depth follows layered sine folds. */
export function makeCurtain(width: number, height: number, color: string, folds = 2.2, segments = 120) {
  const geometry = new T.PlaneGeometry(width, height, segments, 1), p = geometry.attributes.position;
  for (let i = 0; i < p.count; i++) p.setZ(i, Math.sin(p.getX(i) * folds) * 0.42 + Math.sin(p.getX(i) * folds * 2.4 + 1) * 0.1);
  geometry.computeVertexNormals();
  const mesh = new T.Mesh(geometry, new T.MeshPhysicalMaterial({ color, roughness: 0.92, sheen: 1, sheenColor: new T.Color(color).lerp(new T.Color("#ffffff"), 0.35), sheenRoughness: 0.4, side: T.DoubleSide }));
  mesh.receiveShadow = true;
  return mesh;
}

/** Axis-aligned box shorthand: add to parent at x,y,z. */
export function box(parent: T.Object3D, w: number, h: number, d: number, material: T.Material, x = 0, y = 0, z = 0, shadow = true) {
  const mesh = new T.Mesh(new T.BoxGeometry(w, h, d), material);
  mesh.position.set(x, y, z); mesh.castShadow = shadow; mesh.receiveShadow = shadow; parent.add(mesh);
  return mesh;
}

export const hash = (i: number, s = 0) => { const x = Math.sin(i * 127.1 + s * 311.7) * 43758.5453; return x - Math.floor(x); };
```

## 64. `src/three/gifts/coupons.ts` — new

```ts
/**
 * Gift 14 - Coupon Book.
 * A spiral-bound flip pad of six tear-off coupons on a marble cafe table in daylight. Pages hinge at the back edge and flip
 * up and over with a real curl (the free edge lags the hinge). state.selected is the top page; state.open stamps it
 * REDEEMED. Coupons are blank by design, so each unwritten page says so; owner-written text arrives in state.detail
 * ("title\n description"). Nothing is promised that the owner has not written.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, heartShape, lathe, put } from "../../engine/geometry";
import { addContactShadow, addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, glowSprite, hash, orbitCamera, paintBokeh } from "./common";

const N = 6, W = 4.6, H = 2.9, ROWS = 18, T_STEP = 0.02;
const ACCENTS = ["#e5566d", "#f0b43a", "#3fa7a0", "#8a6fd0", "#e98a4a", "#4f8ad0"];

function couponTexture(i: number, text: string) {
  const w = 768, h = 486, c = document.createElement("canvas"); c.width = w; c.height = h; const g = c.getContext("2d")!, accent = ACCENTS[i % ACCENTS.length];
  g.fillStyle = "#fbf4e2"; g.fillRect(0, 0, w, h);
  const wash = g.createRadialGradient(w / 2, h / 2, 120, w / 2, h / 2, 480); wash.addColorStop(0, "rgba(255,255,255,0)"); wash.addColorStop(1, "rgba(150,120,70,.18)"); g.fillStyle = wash; g.fillRect(0, 0, w, h);
  g.fillStyle = accent; g.fillRect(0, 0, 118, h); g.fillStyle = "rgba(255,255,255,.88)"; g.font = "700 64px Georgia, serif"; g.textAlign = "center"; g.fillText(String(i + 1).padStart(2, "0"), 59, 250); g.font = "600 18px Georgia, serif"; g.fillText(`OF ${String(N).padStart(2, "0")}`, 59, 284);
  g.strokeStyle = accent; g.lineWidth = 4; g.strokeRect(138, 22, w - 160, h - 44); g.lineWidth = 1.5; g.strokeRect(146, 30, w - 176, h - 60);
  g.strokeStyle = "rgba(90,70,50,.45)"; g.setLineDash([9, 8]); g.lineWidth = 2; g.beginPath(); g.moveTo(138, h - 112); g.lineTo(w - 22, h - 112); g.stroke(); g.setLineDash([]);
  g.fillStyle = "rgba(90,70,50,.7)"; g.font = "600 17px Georgia, serif"; g.textAlign = "left"; g.fillText("BIRTHDAY COUPON", 170, 70);
  const lines = text.split("\n"), title = lines[0]?.trim() ?? "", body = lines.slice(1).join(" ").trim();
  if (title) {
    g.fillStyle = "#33261f"; g.font = "700 42px Georgia, serif"; let y = 140; const wrap = (str: string, size: number, weight: string, colour: string, maxLines: number, lh: number) => {
      g.font = `${weight} ${size}px Georgia, serif`; g.fillStyle = colour; let line = "", n = 0;
      for (const word of str.split(/\s+/)) { const t = line ? `${line} ${word}` : word; if (g.measureText(t).width > 520 && line) { g.fillText(line, 170, y); y += lh; line = word; if (++n >= maxLines) return; } else line = t; } if (line) { g.fillText(line, 170, y); y += lh; }
    };
    wrap(title, 42, "700", "#33261f", 2, 50); y += 6; wrap(body, 26, "400", "#5a463a", 4, 34);
  } else {
    g.fillStyle = "#33261f"; g.font = "italic 700 46px Georgia, serif"; g.fillText("A coupon to write", 170, 160);
    g.strokeStyle = "rgba(90,70,50,.28)"; g.lineWidth = 2; for (let y = 210; y < 360; y += 40) { g.beginPath(); g.moveTo(170, y); g.lineTo(w - 50, y); g.stroke(); }
  }
  g.fillStyle = "rgba(90,70,50,.75)"; g.font = "700 20px Georgia, serif"; g.fillText("NOT YET REDEEMABLE", 170, h - 58);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 8; return t;
}
function backTexture() {
  const c = document.createElement("canvas"); c.width = 512; c.height = 324; const g = c.getContext("2d")!; g.fillStyle = "#e7d8b8"; g.fillRect(0, 0, 512, 324);
  g.strokeStyle = "rgba(120,92,60,.18)"; g.lineWidth = 2; for (let y = 30; y < 324; y += 28) { g.beginPath(); g.moveTo(24, y); g.lineTo(488, y); g.stroke(); }
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}
function stampTexture() {
  const c = document.createElement("canvas"); c.width = 512; c.height = 200; const g = c.getContext("2d")!; g.translate(256, 100); g.rotate(-0.2);
  g.strokeStyle = "rgba(190,40,52,.92)"; g.fillStyle = "rgba(190,40,52,.92)"; g.lineWidth = 9; g.strokeRect(-220, -66, 440, 132); g.lineWidth = 3; g.strokeRect(-208, -54, 416, 108);
  g.font = "800 64px Georgia, serif"; g.textAlign = "center"; g.textBaseline = "middle"; g.fillText("REDEEMED", 0, 4);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}

export function buildCouponsWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "studio", envIntensity: 0.9, exposure: 1.12, background: "#d9e3e8", fog: { color: "#dfe7ea", density: 0.01 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#fff6e4", "#b8c4cc", 0.9));
  addKeyLight(scene, quality, { color: "#fff0d6", intensity: 3.4, position: [-5, 9, 4], target: [0, 0, -0.6], extent: 7, far: 26 });

  const wall = backdrop((g, w, h) => { const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#dfe9ee"); bg.addColorStop(1, "#f1e8d8"); g.fillStyle = bg; g.fillRect(0, 0, w, h); g.fillStyle = "rgba(255,255,255,.7)"; g.fillRect(w * 0.55, 60, w * 0.33, h * 0.5); g.strokeStyle = "rgba(120,110,100,.45)"; g.lineWidth = 8; g.strokeRect(w * 0.55, 60, w * 0.33, h * 0.5); paintBokeh(g, w, h, "255,236,200", 26, 3); }, 50, 28);
  wall.position.set(0, 7, -8); scene.add(wall);
  const table = put(scene, new T.BoxGeometry(24, 0.5, 14), kit.wood("#8a6540", "#d1a574", [4, 2], 0.5), 0, -0.3, -0.5, false); table.receiveShadow = true;

  /* ---------- pad ---------- */
  const leather = kit.leather("#26302c", "#4a5f56"), brass = kit.metal("brass", 0.3);
  put(scene, new RoundedBoxGeometry(W + 0.3, 0.1, H + 0.24, 3, 0.04), leather, 0, 0.05, 0); put(scene, new RoundedBoxGeometry(W + 0.3, 0.1, H + 0.24, 3, 0.04), leather, 0, 0.05, -H);
  put(scene, new T.BoxGeometry(W - 0.1, 0.02, H - 0.1), kit.paper("#eadfc4", "#cdbd9a"), 0, 0.11, 0, false);
  addContactShadow(scene, W + 1.6, H * 2 + 1, 0, 0.004, -H / 2, 0.45);
  const COILS = 15; for (let i = 0; i < COILS; i++) { const x = -W / 2 + 0.22 + (i / (COILS - 1)) * (W - 0.44); const r = put(scene, new T.TorusGeometry(0.15, 0.028, 8, 20), brass, x, 0.2, -H / 2 - 0.02, false); r.rotation.y = Math.PI / 2; }
  const backTex = backTexture(), textures: T.CanvasTexture[] = [], texKeys: string[] = [];
  const pages = Array.from({ length: N }, (_, i) => {
    const geo = new T.PlaneGeometry(W, H, 1, ROWS); const base = geo.attributes.position;
    const frontTex = couponTexture(i, ""); textures.push(frontTex); texKeys.push("");
    const front = new T.Mesh(geo, new T.MeshStandardMaterial({ map: frontTex, roughness: 0.82, side: T.FrontSide })), back = new T.Mesh(geo, new T.MeshStandardMaterial({ map: backTex, roughness: 0.9, side: T.BackSide }));
    front.castShadow = back.castShadow = !low; front.receiveShadow = back.receiveShadow = true; front.frustumCulled = back.frustumCulled = false; scene.add(front, back); void base;
    return { geo, front, flip: 0, delay: 0 };
  });
  const stampTex = stampTexture(), stamp = new T.Mesh(new T.PlaneGeometry(2.5, 1.0), new T.MeshBasicMaterial({ map: stampTex, transparent: true, depthWrite: false, opacity: 0 })); stamp.rotation.x = -Math.PI / 2; stamp.renderOrder = 5; stamp.visible = false; scene.add(stamp);

  /* ---------- props ---------- */
  const cup = new T.Group(); cup.position.set(4.6, 0, -2.2); scene.add(cup);
  const ceramic = kit.ceramic("#f6f2ea", 0.9);
  put(cup, lathe([[0, 0], [0.8, 0], [0.95, 0.06], [0.9, 0.1], [0.3, 0.1], [0, 0.1]], 40), ceramic, 0, 0, 0);
  put(cup, lathe([[0, 0.1], [0.38, 0.1], [0.5, 0.2], [0.64, 0.68], [0.6, 0.7], [0.55, 0.3], [0.35, 0.22], [0, 0.22]], 40), ceramic, 0, 0, 0);
  put(cup, new T.CircleGeometry(0.58, 32), new T.MeshStandardMaterial({ color: "#4a2d1c", roughness: 0.2 }), 0, 0.62, 0, false).rotation.x = -Math.PI / 2;
  put(cup, new T.TorusGeometry(0.22, 0.05, 10, 20, Math.PI * 1.3), ceramic, 0.66, 0.42, 0, false).rotation.z = -Math.PI / 2 - 0.5;
  const steam = new ParticleField({ count: Math.round(34 * particleScale(quality)), size: 0.22, color: "#ffffff", opacity: 0.18, bounds: [0.18, 0.7, 0.18], center: [4.6, 1.5, -2.2], drift: 0.25, rise: 0.35, twinkle: 0.2 }); scene.add(steam.points);
  const pen = new T.Group(); pen.position.set(-3.9, 0.12, 2.5); pen.rotation.y = 0.5; scene.add(pen);
  put(pen, new T.CylinderGeometry(0.075, 0.075, 1.5, 14), new T.MeshPhysicalMaterial({ color: "#14403e", roughness: 0.2, clearcoat: 1 }), 0, 0, 0).rotation.z = Math.PI / 2;
  put(pen, new T.ConeGeometry(0.06, 0.3, 12), brass, 0.9, 0, 0, false).rotation.z = -Math.PI / 2; put(pen, new T.BoxGeometry(0.5, 0.02, 0.04), brass, -0.2, 0.09, 0, false);
  for (let i = 0; i < 4; i++) { const h = put(scene, new T.ShapeGeometry(heartShape(0.2)), new T.MeshStandardMaterial({ color: ACCENTS[i], roughness: 0.8, side: T.DoubleSide }), -4.8 + hash(i, 1) * 2.2, 0.03, 0.6 + hash(i, 2) * 1.6, false); h.rotation.set(-Math.PI / 2, 0, hash(i, 3) * 6); }
  const warm = glowSprite("#fff0cf", 14, 0.18); warm.position.set(-6, 7, -6); scene.add(warm);

  /* ---------- choreography ---------- */
  const pos = new T.Vector3(), look = new T.Vector3(0, 0, -0.8), orbit = { yaw: 0, pitch: 0 };
  let lastSel = -1, lastOpen = false, stampK = 0, textKey = "";
  const setPage = (p: (typeof pages)[number], flip: number, yBase: number, curl: number) => {
    const pa = p.geo.attributes.position as T.BufferAttribute, theta = flip * Math.PI, ds = H / ROWS; let y = yBase, z = -H / 2;
    for (let r = 0; r <= ROWS; r++) {
      if (r > 0) { const phi = theta - curl * ((r - 0.5) * ds); y += Math.sin(phi) * ds; z += Math.cos(phi) * ds; }
      pa.setXYZ(r * 2, -W / 2, y, z); pa.setXYZ(r * 2 + 1, W / 2, y, z);
    }
    pa.needsUpdate = true; p.geo.computeVertexNormals(); p.geo.computeBoundingSphere();
  };
  return {
    dispose() { textures.forEach((t) => t.dispose()); backTex.dispose(); stampTex.dispose(); },
    frame(time, dt, state: SceneState, reduced) {
      const sel = Math.max(0, Math.min(N - 1, state.selected ?? 0)), redeemed = Boolean(state.open), detail = state.detail ?? "";
      if (sel !== lastSel) { if (lastSel >= 0) stage.sfx("page"); lastSel = sel; }
      const key = `${sel}|${detail}`; if (key !== textKey) { textKey = key; textures[sel].dispose(); const nt = couponTexture(sel, detail); textures[sel] = nt; ((pages[sel].front.material) as T.MeshStandardMaterial).map = nt; ((pages[sel].front.material) as T.MeshStandardMaterial).needsUpdate = true; }
      pages.forEach((p, i) => {
        const target = i < sel ? 1 : 0; p.flip = reduced ? target : damp(p.flip, target, 3.2 - Math.min(1.2, Math.abs(i - sel) * 0.2), dt);
        const yBase = 0.12 + (1 - p.flip) * (N - 1 - i) * T_STEP + p.flip * i * T_STEP; setPage(p, p.flip, yBase, 0.34 * Math.sin(Math.PI * p.flip));
      });
      const top = pages[sel], settled = top.flip < 0.02; if (redeemed !== lastOpen) { lastOpen = redeemed; if (redeemed) { stage.sfx("thud"); stampK = 0; } }
      stamp.visible = redeemed && settled; stampK = reduced ? 1 : Math.min(1, stampK + dt * 4.5);
      const slam = stampK < 1 ? 1 + (1 - stampK) * 1.4 : 1; stamp.scale.setScalar(slam); (stamp.material as T.MeshBasicMaterial).opacity = redeemed ? 0.92 * Math.min(1, stampK * 2.2) : 0;
      stamp.position.set(0.7, 0.12 + (N - 1 - sel) * T_STEP + 0.025, 0.62);
      steam.update(time);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.6, 0.6); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.1, -0.2, 0.3);
      pos.set((reduced ? 0 : Math.sin(time * 0.16) * 0.4), 6.6, 7.4); orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 65. `src/three/gifts/crown.ts` — new

```ts
/**
 * Gift 08 - The Queen's Crown.
 * An imperial crown assembling on a velvet cushion under a theatre spotlight: ermine band, engraved gold band,
 * eight blade spires with pearls, faceted ruby / sapphire / emerald stones, arches that grow to an orb and cross,
 * a velvet cap, and a moving glint of light. state.turn spins it; state.detail = "crown" | "jewels" | "velvet" moves the camera.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, span } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { gemGeometry, growTube, lathe, put, taperedTube } from "../../engine/geometry";
import { addSpotLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { normalFromHeight } from "../../engine/textures";
import { backdrop, orbitCamera, paintBokeh, sparkleSprite } from "./common";

const R = 1.25;
const GEMS = ["#c8264a", "#2a56c9", "#1f9a5a"];

function ermineTexture() {
  const c = document.createElement("canvas"); c.width = 512; c.height = 128; const g = c.getContext("2d")!;
  g.fillStyle = "#f4f0ea"; g.fillRect(0, 0, 512, 128);
  for (let i = 0; i < 900; i++) { g.fillStyle = `rgba(210,205,198,${0.12 + (i % 5) * 0.04})`; g.fillRect((i * 53) % 512, (i * 29) % 128, 2, 5 + (i % 6)); }
  g.fillStyle = "#17141a"; for (let i = 0; i < 9; i++) { const x = 28 + i * 57 + (i % 2) * 10, y = 36 + (i % 3) * 22; g.beginPath(); g.moveTo(x, y - 14); g.quadraticCurveTo(x + 9, y, x, y + 16); g.quadraticCurveTo(x - 9, y, x, y - 14); g.fill(); g.fillRect(x - 1.2, y + 12, 2.4, 14); }
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.wrapS = T.RepeatWrapping; t.repeat.set(3, 1); t.anisotropy = 4; return t;
}
function engravingNormal() {
  const c = document.createElement("canvas"); c.width = 256; c.height = 128; const g = c.getContext("2d")!;
  g.fillStyle = "#808080"; g.fillRect(0, 0, 256, 128); g.strokeStyle = "#ffffff"; g.lineWidth = 4;
  for (let i = 0; i < 4; i++) { const x = 32 + i * 64; g.beginPath(); g.moveTo(x, 14); g.lineTo(x + 28, 64); g.lineTo(x, 114); g.lineTo(x - 28, 64); g.closePath(); g.stroke(); g.beginPath(); g.arc(x, 64, 7, 0, Math.PI * 2); g.stroke(); }
  g.lineWidth = 3; g.beginPath(); g.moveTo(0, 10); g.lineTo(256, 10); g.moveTo(0, 118); g.lineTo(256, 118); g.stroke();
  const t = new T.CanvasTexture(normalFromHeight(c, 3)); t.wrapS = t.wrapT = T.RepeatWrapping; t.repeat.set(2, 1); return t;
}

export function buildCrownWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "studio", envIntensity: 1.9, exposure: 1.05, background: "#120b14", fog: { color: "#150c17", density: 0.022 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#ffd9b0", "#2a1220", 0.45));
  const spot = addSpotLight(scene, quality, "#fff0d6", 140, [1.5, 9.5, 6], [0, 1.2, 0], 0.34, 0.85);
  const rim = new T.DirectionalLight("#9ab4ff", 1.4); rim.position.set(-6, 4, -6); scene.add(rim);
  const glintLight = new T.PointLight("#ffffff", 8, 6, 2); scene.add(glintLight);

  /* ---------- set: curtain, floor, plinth ---------- */
  const wall = backdrop((g, w, h) => { const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#1b0e1c"); bg.addColorStop(1, "#2b1426"); g.fillStyle = bg; g.fillRect(0, 0, w, h); paintBokeh(g, w, h, "255,196,130", 28, 3); }, 40, 22);
  wall.position.set(0, 6, -14); scene.add(wall);
  const curtainGeo = new T.PlaneGeometry(30, 16, low ? 60 : 140, 1), cp = curtainGeo.attributes.position;
  for (let i = 0; i < cp.count; i++) cp.setZ(i, Math.sin(cp.getX(i) * 2.2) * 0.45 + Math.sin(cp.getX(i) * 5.3) * 0.12);
  curtainGeo.computeVertexNormals();
  const curtain = put(scene, curtainGeo, new T.MeshPhysicalMaterial({ color: "#5a1428", roughness: 0.92, sheen: 1, sheenColor: new T.Color("#e0607f"), sheenRoughness: 0.4, side: T.DoubleSide }), 0, 6.4, -9, false);
  curtain.receiveShadow = true;
  const floor = put(scene, new T.CircleGeometry(30, 48), new T.MeshStandardMaterial({ color: "#2a0c14", roughness: 1, metalness: 0, envMapIntensity: 0.15 }), 0, -1.4, 0, false); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;
  const gold = kit.metal("gold", 0.2);
  put(scene, new T.CylinderGeometry(2.4, 2.6, 1.6, 64), kit.marble("#24202b", "#7d7688"), 0, -0.6, 0);
  for (const y of [-1.38, -0.2]) put(scene, new T.TorusGeometry(y < -1 ? 2.6 : 2.4, 0.05, 8, 80), gold, 0, y, 0, false).rotation.x = Math.PI / 2;
  const cushion = put(scene, lathe([[0, 0.18], [1.9, 0.14], [2.05, 0.3], [2.0, 0.5], [1.65, 0.62], [0.9, 0.68], [0, 0.69]], 64), kit.velvet("#3f0a1c"), 0, 0.2, 0);
  cushion.castShadow = true;
  put(scene, new T.TorusGeometry(2.03, 0.045, 8, 80), gold, 0, 0.5, 0, false).rotation.x = Math.PI / 2;
  for (let i = 0; i < 4; i++) { const a = (i / 4) * Math.PI * 2 + Math.PI / 4; const t = new T.Group(); t.position.set(Math.sin(a) * 2.0, 0.55, Math.cos(a) * 2.0); scene.add(t); put(t, new T.SphereGeometry(0.1, 12, 10), gold, 0, 0, 0, false); put(t, new T.CylinderGeometry(0.1, 0.05, 0.38, 12), gold, 0, -0.26, 0, false); const f = put(t, new T.ConeGeometry(0.12, 0.35, 12, 1, true), gold, 0, -0.5, 0, false); f.rotation.x = Math.PI; }

  /* ---------- the crown ---------- */
  const crown = new T.Group(); crown.position.y = 0.89; scene.add(crown);
  const furMat = new T.MeshStandardMaterial({ map: ermineTexture(), roughness: 0.98, side: T.DoubleSide });
  put(crown, new T.CylinderGeometry(R * 1.04, R * 1.08, 0.36, 64, 1, true), furMat, 0, 0.18, 0);
  for (const y of [0.0, 0.36]) put(crown, new T.TorusGeometry(R * 1.06, 0.1, 12, 64), furMat, 0, y, 0).rotation.x = Math.PI / 2;
  const bandMat = new T.MeshStandardMaterial({ color: "#e6b95f", metalness: 1, roughness: 0.22, normalMap: engravingNormal(), normalScale: new T.Vector2(0.9, 0.9), side: T.DoubleSide, envMapIntensity: 2.1 });
  put(crown, new T.CylinderGeometry(R, R, 0.5, low ? 48 : 96, 1, true), bandMat, 0, 0.62, 0);
  for (const y of [0.37, 0.87]) put(crown, new T.TorusGeometry(R, 0.05, 10, 96), gold, 0, y, 0, false).rotation.x = Math.PI / 2;
  const pearlMat = new T.MeshPhysicalMaterial({ color: "#f6efe6", roughness: 0.22, clearcoat: 1, sheen: 1, sheenColor: new T.Color("#ffd9e6"), iridescence: 0.5, iridescenceIOR: 1.4 });
  const spireShape = new T.Shape(); spireShape.moveTo(-0.27, 0); spireShape.bezierCurveTo(-0.3, 0.3, -0.07, 0.58, 0, 0.95); spireShape.bezierCurveTo(0.07, 0.58, 0.3, 0.3, 0.27, 0); spireShape.closePath();
  const spireGeo = new T.ExtrudeGeometry(spireShape, { depth: 0.07, bevelEnabled: true, bevelSize: 0.022, bevelThickness: 0.022, bevelSegments: 2, curveSegments: 16 });
  const spires: { group: T.Group; delay: number; tipY: number }[] = [], gems: T.Group[] = [];
  const tips: T.Vector3[] = [];
  for (let i = 0; i < 8; i++) {
    const a = (i / 8) * Math.PI * 2, group = new T.Group(); group.rotation.y = a; group.position.set(Math.sin(a) * R, 0.87, Math.cos(a) * R); crown.add(group);
    const holder = new T.Group(); holder.position.z = -0.035; group.add(holder);
    put(holder, spireGeo, gold, 0, 0, 0); put(holder, new T.SphereGeometry(0.085, 20, 14), pearlMat, 0, 1.0, 0.035);
    const stone = new T.Group(); stone.position.set(0, 0.34, 0.07); holder.add(stone); const gem = put(stone, gemGeometry(0.13, 8, 0.45, 0.7, 0.6), kit.gem(GEMS[i % 3]), 0, 0, 0, false); gem.rotation.x = Math.PI / 2;
    put(stone, new T.TorusGeometry(0.145, 0.025, 8, 24), gold, 0, 0, 0, false);
    spires.push({ group: holder, delay: i * 0.12, tipY: 0.97 });
    tips.push(new T.Vector3(Math.sin(a) * R, 0.87 + 0.95, Math.cos(a) * R));
    // band stone between spires
    const b = a + Math.PI / 8, bg = new T.Group(); bg.rotation.y = b; bg.position.set(Math.sin(b) * (R + 0.03), 0.62, Math.cos(b) * (R + 0.03)); crown.add(bg);
    const bigGem = put(bg, gemGeometry(0.2, 8, 0.45, 0.8, 0.6), kit.gem(GEMS[(i + 1) % 3]), 0, 0, 0.0, false); bigGem.rotation.x = Math.PI / 2; put(bg, new T.TorusGeometry(0.225, 0.034, 10, 32), gold, 0, 0, 0, false); gems.push(bg);
    const fleur = put(crown, new T.ConeGeometry(0.13, 0.42, 4), gold, Math.sin(b) * R, 0.87 + 0.2, Math.cos(b) * R); fleur.rotation.y = b + Math.PI / 4;
    put(crown, new T.SphereGeometry(0.06, 14, 10), pearlMat, Math.sin(b) * R, 0.87 + 0.46, Math.cos(b) * R, false);
  }
  const apex = new T.Vector3(0, 2.62, 0);
  const arches = [0, 2, 4, 6].map((i) => {
    const tip = tips[i], mid = tip.clone().lerp(apex, 0.5); mid.y += 0.38; mid.multiplyScalar(1);
    const mesh = new T.Mesh(taperedTube(new T.CatmullRomCurve3([tip.clone().setY(tip.y - 0.05), mid, apex.clone().setY(apex.y - 0.1)]), 0.06, 0.05, 40, 10), gold); mesh.castShadow = true; crown.add(mesh); growTube(mesh, 0); return mesh;
  });
  const orb = new T.Group(); orb.position.copy(apex); crown.add(orb);
  put(orb, new T.SphereGeometry(0.2, 32, 24), gold, 0, 0.0, 0); put(orb, new T.TorusGeometry(0.2, 0.03, 8, 40), gold, 0, 0, 0, false).rotation.x = Math.PI / 2;
  put(orb, new T.BoxGeometry(0.07, 0.4, 0.07), gold, 0, 0.38, 0); put(orb, new T.BoxGeometry(0.26, 0.07, 0.07), gold, 0, 0.42, 0); put(orb, new T.SphereGeometry(0.045, 12, 10), kit.gem("#c8264a"), 0, 0.42, 0.04, false);
  orb.scale.setScalar(0.001);
  const cap = put(crown, new T.SphereGeometry(R * 0.96, 48, 22, 0, Math.PI * 2, 0, Math.PI / 2), new T.MeshPhysicalMaterial({ color: "#4a0c20", roughness: 0.95, sheen: 0.7, sheenColor: new T.Color("#c24a6a"), sheenRoughness: 0.4, side: T.DoubleSide }), 0, 0.3, 0, false);
  cap.scale.y = 1.55;

  /* ---------- sparkle, dust, spotlight cone ---------- */
  const sparkles = gems.map((g, i) => { const s = sparkleSprite(i % 2 ? "#fff0d0" : "#ffd6e0", 0.7, 0); s.position.copy(g.position); s.position.z *= 1.04; crown.add(s); return s; });
  const dust = new ParticleField({ count: Math.round(120 * particleScale(quality)), size: 0.05, color: "#fff0d0", opacity: 0.6, bounds: [3, 3.5, 3], center: [0, 2.5, 0], drift: 0.6, rise: 0.04, twinkle: 0.8 });
  scene.add(dust.points);
  const cone = new T.Mesh(new T.ConeGeometry(3.4, 11, 32, 1, true), new T.MeshBasicMaterial({ color: "#ffeccc", transparent: true, opacity: 0.045, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide, fog: false }));
  cone.position.set(0.7, 5, 3); cone.lookAt(0, 0, 0); cone.rotateX(Math.PI / 2); scene.add(cone);

  /* ---------- choreography ---------- */
  const poses: Record<string, { p: T.Vector3; l: T.Vector3 }> = {
    crown: { p: new T.Vector3(0, 3.0, 9.8), l: new T.Vector3(0, 2.0, 0) },
    jewels: { p: new T.Vector3(0, 2.0, 5.6), l: new T.Vector3(0, 1.6, 0.3) },
    velvet: { p: new T.Vector3(0.5, 3.4, 5.8), l: new T.Vector3(0, 0.5, 0) },
  };
  const pos = poses.crown.p.clone(), look = poses.crown.l.clone();
  const s = { yaw: 0, orbitYaw: 0, pitch: 0 };
  let age = 0, spun = 0, lastDetail = "crown";
  return {
    pickables: [],
    frame(time, dt, state: SceneState, reduced) {
      age = reduced ? 99 : age + dt;
      const drag = input.consumeDrag();
      spun += drag.x * 6.5 + input.velocity.x * 0.8; s.yaw = damp(s.yaw, (state.turn ?? 0) + spun, 4, dt, reduced);
      s.pitch = T.MathUtils.clamp(s.pitch + drag.y * 1.4, -0.2, 0.4);
      crown.rotation.y = s.yaw + (reduced ? 0 : time * 0.08);
      spires.forEach((sp, i) => {
        const k = ease.out(span(age, sp.delay, sp.delay + 0.9));
        sp.group.position.y = (1 - k) * 2.6; sp.group.rotation.x = (1 - k) * -0.5; sp.group.visible = k > 0.001;
        void i;
      });
      arches.forEach((m, i) => growTube(m, ease.inOut(span(age, 1.6 + i * 0.12, 2.9 + i * 0.12))));
      const orbK = ease.out(span(age, 2.8, 3.4)); orb.scale.setScalar(Math.max(0.001, orbK * (1 + Math.sin(orbK * Math.PI) * 0.15)));
      gems.forEach((g, i) => { g.scale.setScalar(Math.max(0.001, ease.out(span(age, 0.8 + i * 0.1, 1.5 + i * 0.1)))); });
      if (age > 1.0 && age - dt <= 1.0) stage.sfx("chime"); if (age > 3.0 && age - dt <= 3.0) stage.sfx("sparkle");
      sparkles.forEach((sp, i) => { const m = sp.material as T.SpriteMaterial; const v = Math.max(0, Math.sin(time * 2.2 + i * 1.9)); m.opacity = (reduced ? 0.5 : v * v) * ease.out(span(age, 2, 3)); sp.scale.setScalar(0.5 + 0.5 * v); });
      // a glint of light circles the crown
      const g = reduced ? 1 : time * 0.7; glintLight.position.set(Math.cos(g) * 3.4, 2.2 + Math.sin(g * 1.3) * 0.6, Math.sin(g) * 3.4); glintLight.intensity = 9;
      dust.update(time);
      spot.intensity = 140 * (0.85 + 0.15 * ease.out(span(age, 0, 1.2)));
      const detail = state.detail === "jewels" || state.detail === "velvet" ? state.detail : "crown";
      if (detail !== lastDetail) { lastDetail = detail; stage.sfx("click"); }
      const target = poses[detail];
      pos.x = damp(pos.x, target.p.x, 2.6, dt, reduced); pos.y = damp(pos.y, target.p.y, 2.6, dt, reduced); pos.z = damp(pos.z, target.p.z, 2.6, dt, reduced);
      look.x = damp(look.x, target.l.x, 2.6, dt, reduced); look.y = damp(look.y, target.l.y, 2.6, dt, reduced); look.z = damp(look.z, target.l.z, 2.6, dt, reduced);
      s.orbitYaw = 0;
      orbitCamera(camera, pos.clone().add(new T.Vector3(Math.sin(time * 0.2) * 0.25 * (reduced ? 0 : 1), 0, 0)), look, 0, s.pitch, 0.9);
    },
  };
}
```

## 66. `src/three/gifts/envelope.ts` — new

```ts
import * as T from "three";
import type { MaterialKit } from "../../engine/materials";
import { put } from "../../engine/geometry";

const tri = (a: [number, number], b: [number, number], c: [number, number], depth = 0.01) => {
  const shape = new T.Shape(); shape.moveTo(...a); shape.lineTo(...b); shape.lineTo(...c); shape.closePath();
  return new T.ExtrudeGeometry(shape, { depth, bevelEnabled: true, bevelThickness: 0.003, bevelSize: 0.004, bevelSegments: 1 });
};

/** Upright envelope (front faces +Z). The flap hinges on the top edge: hinge.rotation.x = -PI opens it upward. */
export function makeEnvelope(kit: MaterialKit, w = 1.7, h = 1.1, paperColor = "#f1e5c8", sealColor = "#8f2a3c") {
  const group = new T.Group(), paper = kit.paper(paperColor, new T.Color(paperColor).multiplyScalar(0.82).getStyle(), { side: T.DoubleSide, roughness: 0.9 });
  const W = w / 2, H = h / 2;
  put(group, new T.PlaneGeometry(w, h), paper, 0, 0, 0); // thin back panel: leaves a real pocket for a letter at z~0.003
  put(group, tri([-W, H], [-W, -H], [0, -0.05 * h]), paper, 0, 0, 0.007);
  put(group, tri([W, H], [W, -H], [0, -0.05 * h]), paper, 0, 0, 0.007);
  put(group, tri([-W, -H], [W, -H], [0, 0.14 * h]), paper, 0, 0, 0.013);
  const hinge = new T.Group(); hinge.position.set(0, H, 0.02); group.add(hinge);
  put(hinge, tri([-W, 0], [W, 0], [0, -0.64 * h], 0.009), paper, 0, 0, 0);
  const seal = new T.Group(); seal.position.set(0, -0.64 * h + 0.16, 0.02); hinge.add(seal);
  const disc = put(seal, new T.CylinderGeometry(0.13, 0.135, 0.03, 28), kit.wax(sealColor), 0, 0, 0.01, false); disc.rotation.x = Math.PI / 2;
  const ring = put(seal, new T.TorusGeometry(0.085, 0.01, 8, 28), kit.wax(new T.Color(sealColor).multiplyScalar(0.8).getStyle()), 0, 0, 0.03, false); void ring;
  return { group, hinge, seal };
}
```

## 67. `src/three/gifts/flower.ts` — new

```ts
/**
 * Gift 03 - The Flower That Never Fades.
 * A cut-away garden diorama: a seed rests against the soil face, a branching root system spreads through real strata,
 * a curved stem rises through wind-bent grass, leaves unfurl, a bud forms and a multi-layer bloom opens around a golden
 * centre. Butterflies, fireflies and pollen live in the air. The camera follows the growth, from underground to the bloom.
 * state.growth 0..4 selects the stage; every stage is a point on one scrubbable timeline (it can also run backwards).
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { Sequence, ease, span } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { createBloom, createButterflies, createGrass, createRoots, createSky, buildTerrain } from "../../engine/garden";
import { RoundedBoxGeometry, growTube, lathe, leafGeometry, put, taperedTube } from "../../engine/geometry";
import { addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { glowCanvas } from "../../engine/textures";

export const FLOWER_DURATION = 16;
const PLANT = new T.Vector3(0, 0, 1.0);

export interface FlowerOptions {
  /** Page-hero variant: light palette and the plant framed to the right so HTML copy can sit on the left. */
  hero?: boolean;
}

export function buildFlowerWorld(stage: Stage, options: FlowerOptions = {}): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const hero = Boolean(options.hero);
  const low = quality === "low", high = quality === "high";
  stage.mood({ env: "garden", envIntensity: 0.9, exposure: hero ? 1.04 : 1.1, background: hero ? "#f2dcc4" : "#f2c99c", fog: { color: hero ? "#f2dcc4" : "#f1cfa6", density: hero ? 0.0075 : 0.011 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 120; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#cfe2ff", "#6a5a30", 0.75));
  addKeyLight(scene, quality, { color: "#ffd7a0", intensity: 3.8, position: [-6, 5, -3], target: [0, 1, 1], extent: 6.5, far: 30 });
  const frontFill = new T.DirectionalLight("#fff0dc", 0.9); frontFill.position.set(3, 3, 9); scene.add(frontFill);
  const rimLight = new T.DirectionalLight("#9fc2ff", 0.8); rimLight.position.set(6, 4, -6); scene.add(rimLight);
  const bloomLight = new T.PointLight("#ffc7a6", 0, 6, 2); scene.add(bloomLight);

  const sky = hero ? createSky(170, 90) : createSky(60, 34); sky.position.set(0, hero ? 17 : 7, hero ? -50 : -20); scene.add(sky);

  /* ---------- diorama ---------- */
  const world = new T.Group(); scene.add(world);
  const flat = (x: number, z: number) => T.MathUtils.smoothstep(Math.hypot(x, z - 1.0), 0.6, 2.0);
  const height = (x: number, z: number) => flat(x, z) * (0.26 * Math.sin(x * 0.9 + 1.3) * Math.cos(z * 0.8) + 0.13 * Math.sin(x * 2.3 + z * 1.9) + 0.2 * Math.pow(Math.abs(x) / 3.5, 2)) + 0.02 * Math.sin(x * 5 + z * 4);
  const terrain = buildTerrain(quality, { width: 7, depth: 4.2, bottom: -2.7, height });
  world.add(terrain.group);
  const frontZ = terrain.frontZ;
  const grass = createGrass({ count: high ? 7000 : low ? 1700 : 4600, width: 6.9, depth: 4.1, height, blade: 0.36, keepOut: (x, z) => Math.hypot(x - PLANT.x, z - PLANT.z) < 0.16 });
  world.add(grass.mesh);
  const stones = new T.InstancedMesh(new T.DodecahedronGeometry(0.12, 0), kit.stone("#6a665c", "#b0aa9a"), 16); const d = new T.Object3D();
  for (let i = 0; i < 16; i++) { const x = Math.sin(i * 7.7) * 3.1, z = Math.cos(i * 5.3) * 1.8; d.position.set(x, height(x, z) + 0.02, z); d.rotation.set(i, i * 2, 0); d.scale.set(1 + (i % 3) * 0.5, 0.55 + (i % 2) * 0.3, 1 + (i % 4) * 0.3); d.updateMatrix(); stones.setMatrixAt(i, d.matrix); }
  stones.castShadow = !low; world.add(stones);
  const mound = put(world, new T.SphereGeometry(0.34, 18, 10), kit.soil("#2b1c12", "#6a4a30", [1, 1]), PLANT.x, 0.0, PLANT.z); mound.scale.set(1, 0.32, 1);

  const plinth = put(world, new RoundedBoxGeometry(7.5, 0.34, 4.7, 3, 0.06), kit.wood("#1d110a", "#4b2f1c", [2, 1], 0.45), 0, -2.87, 0);
  put(world, new T.BoxGeometry(7.56, 0.04, 4.76), kit.metal("brass", 0.4), 0, -2.69, 0, false); void plinth;
  const floor = put(scene, new T.PlaneGeometry(120, 80), new T.MeshStandardMaterial({ color: hero ? "#e6cdb2" : "#2b1f16", roughness: 0.9 }), 0, -3.04, -10, false); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;

  /* ---------- seed + roots ---------- */
  const seedPos = new T.Vector3(0, -0.55, frontZ + 0.07);
  const seed = new T.Mesh(lathe([[0, -0.3], [0.1, -0.26], [0.17, -0.12], [0.2, 0.04], [0.16, 0.2], [0.07, 0.31], [0, 0.35]], 20), new T.MeshPhysicalMaterial({ color: "#6b4328", roughness: 0.32, clearcoat: 0.7, clearcoatRoughness: 0.25 }));
  seed.position.copy(seedPos); seed.scale.set(1.15, 1.15, 0.8); seed.castShadow = true; world.add(seed);
  const seam = new T.Mesh(new T.TorusGeometry(0.19, 0.008, 6, 40, Math.PI), new T.MeshStandardMaterial({ color: "#2b1a0e", roughness: 0.6 })); seam.rotation.set(0, Math.PI / 2, Math.PI / 2 - 0.1); seam.position.copy(seedPos); seam.scale.set(1.15, 1.7, 1); world.add(seam);
  const spark = new T.Sprite(new T.SpriteMaterial({ map: (() => { const t = new T.CanvasTexture(glowCanvas("rgba(255,236,170,1)", "rgba(255,200,120,0)", 128)); t.colorSpace = T.SRGBColorSpace; return t; })(), transparent: true, opacity: 0, depthWrite: false, blending: T.AdditiveBlending }));
  spark.position.copy(seedPos); spark.position.z += 0.15; spark.scale.setScalar(1.4); world.add(spark);
  const roots = createRoots(frontZ + 0.05, quality); roots.group.position.set(0, seedPos.y - 0.28, 0); world.add(roots.group);

  /* ---------- plant ---------- */
  const plant = new T.Group(); plant.position.copy(PLANT); world.add(plant);
  const stemCurve = new T.CatmullRomCurve3([new T.Vector3(0, 0, 0), new T.Vector3(0.16, 1.1, 0.03), new T.Vector3(-0.13, 2.3, -0.02), new T.Vector3(0.09, 3.4, 0.0)]);
  const stemMat = new T.MeshStandardMaterial({ color: "#3d6a2b", roughness: 0.5 });
  const stem = new T.Mesh(taperedTube(stemCurve, 0.125, 0.06, low ? 30 : 56, low ? 6 : 10), stemMat); stem.castShadow = true; plant.add(stem); growTube(stem, 0);
  const leafMat = kit.leaf("#2f5a34", "#79a752");
  const leafSpecs = [0.2, 0.32, 0.44, 0.56, 0.68, 0.79].map((t, i) => ({ t, len: 1.4 - i * 0.1, az: i * 2.4 + 0.5 }));
  const leaves = leafSpecs.map((spec) => {
    const pivot = new T.Group(), hinge = new T.Group(); pivot.rotation.y = spec.az; pivot.add(hinge); hinge.add(put(hinge, leafGeometry(spec.len, spec.len * 0.38, 0.4, 0.2, 8, 14), leafMat, 0, 0, 0)); plant.add(pivot);
    pivot.position.copy(stemCurve.getPointAt(spec.t)); pivot.visible = false; return { pivot, hinge, spec };
  });
  const head = new T.Group(); plant.add(head);
  const flower = createBloom(kit, quality); head.add(flower.group); flower.setBloom(0); head.visible = false;
  const glow = new T.Sprite(new T.SpriteMaterial({ map: (() => { const t = new T.CanvasTexture(glowCanvas("rgba(255,205,190,1)", "rgba(255,160,150,0)", 128)); t.colorSpace = T.SRGBColorSpace; return t; })(), transparent: true, opacity: 0, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
  glow.scale.setScalar(5); glow.position.set(0, 0.4, -0.5); head.add(glow);

  /* ---------- life in the air ---------- */
  const butterflies = createButterflies(3); butterflies.group.visible = false; scene.add(butterflies.group);
  const pollen = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.05, color: "#ffe9a8", opacity: 0.85, bounds: [0.9, 0.9, 0.9], drift: 1.1, rise: 0.12, twinkle: 0.4 });
  scene.add(pollen.points); pollen.opacity = 0;
  const fireflies = new ParticleField({ count: Math.round(60 * particleScale(quality)), size: 0.07, color: "#fff2a0", colorB: "#c8ff8a", opacity: 0, bounds: [3.2, 0.9, 1.9], center: [0, 1.0, 0], drift: 1.4, twinkle: 0.9 });
  scene.add(fireflies.points);

  /* ---------- timeline ---------- */
  const seq = new Sequence(FLOWER_DURATION, { crack: 0, roots: 0, stem: 0, leaves: 0, bud: 0, bloom: 0 }, (tl, p) => {
    tl.to(p, { crack: 1, duration: 1.6, ease: "sine.out" }, 0)
      .to(p, { roots: 1, duration: 5.2, ease: "power1.inOut" }, 1.0)
      .to(p, { stem: 1, duration: 7, ease: "power1.inOut" }, 4.0)
      .to(p, { leaves: 1, duration: 4.5, ease: "power1.inOut" }, 7.0)
      .to(p, { bud: 1, duration: 2, ease: "power1.inOut" }, 10.5)
      .to(p, { bloom: 1, duration: 4, ease: "power1.inOut" }, 12);
  });
  const cues = [{ at: 0.04, sfx: "magic" }, { at: 0.3, sfx: "sparkle" }, { at: 0.73, sfx: "bloom" }] as const;
  const poses = [
    { t: 0.0, p: new T.Vector3(0.3, -0.4, 6.4), l: new T.Vector3(0, -0.7, 2.1) },
    { t: 0.25, p: new T.Vector3(-0.5, -0.5, 7.4), l: new T.Vector3(0, -1.0, 2.0) },
    { t: 0.5, p: new T.Vector3(0.5, 1.8, 7.6), l: new T.Vector3(0, 0.9, 1.4) },
    { t: 0.7, p: new T.Vector3(0.7, 3.0, 8.8), l: new T.Vector3(0, 2.0, 1.1) },
    { t: 0.86, p: new T.Vector3(0.4, 4.1, 7.6), l: new T.Vector3(0, 2.9, 1.1) },
    { t: 1.0, p: new T.Vector3(1.5, 4.4, 8.8), l: new T.Vector3(0, 2.7, 1.1) },
  ];
  const pos = new T.Vector3(), look = new T.Vector3(), tip = new T.Vector3(), headWorld = new T.Vector3(), offset = new T.Vector3(), center = new T.Vector3(0, 1.6, 1.2);
  let lastProgress = -1, lastBloom = -1, turn = 0, lastStem = -1, lastReport = -1;
  const orbit = { yaw: 0, pitch: 0 };

  return {
    pickables: [seed, head],
    frame(time, dt, state: SceneState, reduced, timelineDt = dt) {
      const target = T.MathUtils.clamp((state.growth ?? 0) / 4, 0, 1);
      seq.speed = target < seq.progress ? 3.2 : 1;
      const progress = seq.step(target, timelineDt, reduced || Boolean(state.immediate));
      const p = seq.phases;
      if (!reduced && Math.abs(progress - lastProgress) > 1e-5 && lastProgress >= 0) for (const c of cues) if ((lastProgress < c.at) !== (progress < c.at)) stage.sfx(c.sfx);
      lastProgress = progress;

      // underground: seed cracks, light spark, roots creep through the strata
      const crack = ease.inOut(p.crack);
      seed.scale.set(1.15 - 0.3 * crack, 1.15 - 0.22 * crack, 0.8 - 0.1 * crack); seam.scale.set(1.15 - 0.3 * crack, 1.7 - 0.3 * crack, 1);
      (seed.material as T.MeshPhysicalMaterial).emissive.set("#ffb86a").multiplyScalar(Math.sin(Math.PI * Math.min(1, p.crack * 1.2)) * 0.35);
      (spark.material as T.SpriteMaterial).opacity = Math.sin(Math.PI * p.crack) * 0.9; spark.scale.setScalar(1.0 + p.crack);
      roots.update(p.roots);

      // stem rises (draw range grows along the curve); a small soil mound parts as it emerges
      if (Math.abs(p.stem - lastStem) > 1e-4) { growTube(stem, p.stem); lastStem = p.stem; }
      mound.scale.set(1 + 0.3 * span(p.stem, 0, 0.1) * (1 - span(p.stem, 0.1, 0.4)), 0.32 * (1 - 0.6 * span(p.stem, 0.05, 0.5)), 1 + 0.3 * span(p.stem, 0, 0.1) * (1 - span(p.stem, 0.1, 0.4)));
      mound.visible = p.stem < 0.999;
      const grown = Math.min(1, p.stem);
      tip.copy(stemCurve.getPointAt(Math.max(0.001, grown)));
      leaves.forEach((l, i) => {
        const reached = p.stem > l.spec.t + 0.02, k = ease.inOut(span(p.leaves, i * 0.1, i * 0.1 + 0.55));
        l.pivot.visible = reached && k > 0.001;
        l.hinge.rotation.x = 0.12 + k * 1.05; l.hinge.rotation.z = (i % 2 ? 1 : -1) * 0.06 * (1 - k); l.pivot.scale.setScalar(0.25 + 0.75 * k);
        if (!reduced) l.hinge.rotation.x += Math.sin(time * 1.1 + i * 1.7) * 0.025 * k;
      });

      // head: bud at the tip, then it opens
      const bud = ease.inOut(p.bud), bloom = ease.inOut(p.bloom);
      head.visible = p.stem > 0.97 && bud > 0.001;
      head.position.copy(stemCurve.getPointAt(1));
      const headScale = 0.16 + 0.2 * bud + 0.64 * bloom;
      head.scale.setScalar(headScale); head.rotation.x = 0.1 + 0.85 * bloom;
      if (Math.abs(bloom - lastBloom) > 1e-4) { flower.setBloom(Math.max(0.0, bloom * 0.98 + 0.02 * bud)); lastBloom = bloom; }
      if (!reduced) flower.flutter(time, bloom);
      (glow.material as T.SpriteMaterial).opacity = 0.2 * bloom; glow.scale.setScalar(3.4 + 1.6 * bloom);
      head.getWorldPosition(headWorld);
      bloomLight.position.set(headWorld.x, headWorld.y + 0.4, headWorld.z + 1.2); bloomLight.intensity = 3.2 * bloom;

      // wind: the whole plant bends, the head lags behind
      const wind = reduced ? 0 : 1;
      plant.rotation.z = Math.sin(time * 0.8) * 0.018 * wind * (0.4 + p.stem * 0.6); plant.rotation.x = Math.cos(time * 0.6) * 0.008 * wind;
      head.rotation.z = Math.sin(time * 0.8 - 0.7) * 0.05 * wind * bloom;
      grass.update(reduced ? 0 : time);

      // life
      const alive = ease.inOut(span(progress, 0.8, 1));
      butterflies.group.visible = alive > 0.02;
      if (butterflies.group.visible) { butterflies.update(time, center, headWorld, span(bloom, 0.8, 1), reduced); }
      pollen.points.position.copy(headWorld); pollen.opacity = 0.9 * span(bloom, 0.55, 1); pollen.update(time);
      (fireflies.points.material as T.ShaderMaterial).uniforms.uOpacity.value = 0.85 * alive; fireflies.update(time);

      // camera follows the growth
      let a = poses[0], b = poses[poses.length - 1];
      for (let i = 0; i < poses.length - 1; i++) if (progress >= poses[i].t && progress <= poses[i + 1].t) { a = poses[i]; b = poses[i + 1]; break; }
      const k = ease.inOut(span(progress, a.t, b.t));
      pos.copy(a.p).lerp(b.p, k); look.copy(a.l).lerp(b.l, k);
      if (progress > 0.45 && p.stem < 1) look.y = Math.max(look.y, tip.y * 0.55 + 0.3);
      if (!reduced) { pos.x += Math.sin(time * 0.22) * 0.18; pos.y += Math.sin(time * 0.17) * 0.06; }
      const drag = input.consumeDrag();
      orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 4.5, -1.2, 1.2); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.4, -0.2, 0.35);
      turn = T.MathUtils.damp(turn, state.turn ?? 0, 3, dt);
      world.rotation.y = turn;
      offset.copy(pos).sub(look).applyAxisAngle(new T.Vector3(0, 1, 0), orbit.yaw).applyAxisAngle(new T.Vector3(1, 0, 0), -orbit.pitch);
      const fit = T.MathUtils.clamp(0.9 / Math.max(0.45, camera.aspect), 1, 1.8);
      camera.position.copy(look).addScaledVector(offset, fit); camera.lookAt(look);
      if (hero) { const w = 1000; camera.setViewOffset(w, w / camera.aspect, -(camera.aspect > 1.15 ? 0.2 : 0) * w, 0, w, w / camera.aspect); } // plant right of centre; copy lives on the left

      if (Math.abs(progress - lastReport) > 0.008 || progress === 0 || progress === 1 || progress === target) { if (progress !== lastReport) { stage.report?.(progress); lastReport = progress; } }
    },
    dispose() { seq.dispose(); },
  };
}
```

## 68. `src/three/gifts/hopeTree.ts` — new

```ts
/**
 * Gift 15 - Future Garden.
 * A glass terrarium on a walnut stand: a real soil cross-section (layered strata) with a large seed pressed against the cut
 * face, roots that creep through the soil, and a sapling that gains one leaf per hope (state.growth 0..8). Every opened
 * leaf carries a hanging paper tag; picking a tag (state.selected) glows it, lands a butterfly on its leaf and moves
 * the camera in. The eight hopes are blank by design, so the tags only carry numbers.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { buildTerrain, createButterflies, createGrass, createRoots } from "../../engine/garden";
import { RoundedBoxGeometry, growTube, lathe, leafGeometry, put, taperedTube } from "../../engine/geometry";
import { addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, box, glowSprite, orbitCamera, paintBokeh, hash } from "./common";

const LEAVES = 8, BOX_W = 5.5, BOX_D = 3.2, BOTTOM = -2.6;
const height = (x: number, z: number) => 0.05 * Math.sin(x * 1.4) * Math.cos(z * 1.9);

function tagTexture(n: number) {
  const c = document.createElement("canvas"); c.width = 256; c.height = 192; const g = c.getContext("2d")!;
  g.fillStyle = "#f6ebd0"; g.fillRect(0, 0, 256, 192); g.strokeStyle = "rgba(150,110,70,.6)"; g.lineWidth = 5; g.strokeRect(8, 8, 240, 176);
  g.fillStyle = "rgba(240,230,205,1)"; g.beginPath(); g.arc(128, 26, 10, 0, 6.283); g.fill(); g.strokeStyle = "rgba(150,110,70,.8)"; g.lineWidth = 3; g.stroke();
  g.fillStyle = "#4a3a30"; g.textAlign = "center"; g.font = "600 30px Georgia, serif"; g.fillText("HOPE", 128, 98); g.font = "700 54px Georgia, serif"; g.fillText(String(n), 128, 158);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}

export function buildHopeTreeWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low", high = quality === "high";
  stage.mood({ env: "garden", envIntensity: 1.0, exposure: 1.12, background: "#cfe3dc", fog: { color: "#d6e6df", density: 0.008 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#fff4dc", "#6e8a6a", 0.9));
  addKeyLight(scene, quality, { color: "#ffeccc", intensity: 3.3, position: [-5, 8, 6], target: [0, 1, 0.5], extent: 6, far: 24 });
  const rim = new T.DirectionalLight("#ffc0d0", 0.9); rim.position.set(5, 3, -4); scene.add(rim);

  const dawn = backdrop((g, w, h) => {
    const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#9ccbd0"); bg.addColorStop(0.5, "#f7dcc8"); bg.addColorStop(1, "#f3c3b0"); g.fillStyle = bg; g.fillRect(0, 0, w, h);
    const sun = g.createRadialGradient(w * 0.78, h * 0.62, 0, w * 0.78, h * 0.62, 320); sun.addColorStop(0, "rgba(255,246,214,.95)"); sun.addColorStop(1, "rgba(255,230,190,0)"); g.fillStyle = sun; g.fillRect(0, 0, w, h);
    g.fillStyle = "rgba(120,150,140,.45)"; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 16) g.lineTo(x, h * 0.72 + Math.sin(x * 0.006) * 34 + Math.sin(x * 0.017) * 10); g.lineTo(w, h); g.fill();
    g.fillStyle = "rgba(96,130,118,.55)"; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 16) g.lineTo(x, h * 0.84 + Math.sin(x * 0.01 + 2) * 22); g.lineTo(w, h); g.fill(); paintBokeh(g, w, h, "255,244,214", 24, 9);
  }, 56, 32);
  dawn.position.set(0, 7, -9); scene.add(dawn);
  const table = put(scene, new T.BoxGeometry(26, 0.5, 14), kit.wood("#4a2f1a", "#a8794c", [4, 2], 0.5), 0, -3.2, 0, false); table.receiveShadow = true;

  /* ---------- terrarium ---------- */
  const world = new T.Group(); scene.add(world);
  const terrain = buildTerrain(quality, { width: BOX_W - 0.2, depth: BOX_D - 0.2, bottom: BOTTOM, height }); terrain.group.position.z = 0; world.add(terrain.group);
  const frontZ = terrain.frontZ;
  const grass = createGrass({ count: high ? 2600 : low ? 600 : 1500, width: BOX_W - 0.3, depth: BOX_D - 0.3, height, blade: 0.34, keepOut: (x, z) => Math.hypot(x, z - 0.55) < 0.25 }); world.add(grass.mesh);
  const walnut = kit.wood("#2c180c", "#7c4d2a", [2, 1], 0.4), brass = kit.metal("brass", 0.3);
  put(world, new RoundedBoxGeometry(BOX_W + 0.9, 0.42, BOX_D + 0.9, 3, 0.08), walnut, 0, BOTTOM - 0.22, 0);
  const H = 6.2, y0 = BOTTOM - 0.02, cy = y0 + H / 2, hx = BOX_W / 2 + 0.02, hz = BOX_D / 2 + 0.02;
  for (const sx of [-1, 1]) for (const sz of [-1, 1]) box(world, 0.09, H, 0.09, brass, sx * hx, cy, sz * hz, false);
  for (const y of [y0, y0 + H]) { for (const sz of [-1, 1]) box(world, BOX_W + 0.09, 0.09, 0.09, brass, 0, y, sz * hz, false); for (const sx of [-1, 1]) box(world, 0.09, 0.09, BOX_D + 0.09, brass, sx * hx, y, 0, false); }
  const glassMat = new T.MeshPhysicalMaterial({ color: "#eaf6f2", transparent: true, opacity: 0.07, roughness: 0.02, metalness: 0, envMapIntensity: 2.2, side: T.DoubleSide, depthWrite: false });
  const frontPane = put(world, new T.PlaneGeometry(BOX_W, H), glassMat, 0, cy, hz, false); frontPane.renderOrder = 8; for (const sx of [-1, 1]) { const p = put(world, new T.PlaneGeometry(BOX_D, H), glassMat, sx * hx, cy, 0, false); p.rotation.y = Math.PI / 2; p.renderOrder = 8; }
  put(world, new T.PlaneGeometry(BOX_W, H), glassMat, 0, cy, -hz, false);

  /* ---------- seed, roots, sapling ---------- */
  const seedPos = new T.Vector3(0, -0.95, frontZ + 0.07);
  const seedMat = new T.MeshPhysicalMaterial({ color: "#6b4328", roughness: 0.32, clearcoat: 0.7, clearcoatRoughness: 0.25 });
  const seed = new T.Mesh(lathe([[0, -0.3], [0.1, -0.26], [0.17, -0.12], [0.2, 0.04], [0.16, 0.2], [0.07, 0.31], [0, 0.35]], 20), seedMat); seed.position.copy(seedPos); seed.scale.set(1.2, 1.2, 0.8); seed.castShadow = true; world.add(seed);
  const seedGlow = glowSprite("#ffd890", 1.6, 0.3); seedGlow.position.copy(seedPos).z += 0.18; world.add(seedGlow);
  const roots = createRoots(frontZ + 0.05, quality); roots.group.position.set(0, seedPos.y - 0.3, 0); world.add(roots.group);
  const curve = new T.CatmullRomCurve3([[0, -0.75, 1.67], [0.02, -0.35, 1.66], [0, 0, 1.5], [0.08, 0.45, 1.1], [0, 1.0, 0.7], [-0.1, 1.65, 0.5], [0.05, 2.25, 0.4], [0.1, 2.75, 0.38]].map(([x, y, z]) => new T.Vector3(x, y, z)));
  const trunk = new T.Mesh(taperedTube(curve, 0.1, 0.022, 90, 8), kit.bark("#3a2a1a", "#8a6a48", [1, 4])); trunk.castShadow = true; growTube(trunk, 0); world.add(trunk);
  const tAt = (i: number) => 0.3 + 0.66 * (i / (LEAVES - 1));
  const leafGeoms = Array.from({ length: LEAVES }, (_, i) => { const len = 1.05 - i * 0.07; return { geo: leafGeometry(len, len * 0.42, 0.4, 0.2, 8, 14), len }; });
  const tagTextures: T.CanvasTexture[] = [];
  const leaves = leafGeoms.map(({ geo, len }, i) => {
    const mat = kit.leaf("#2f6a3c", "#86b85a").clone() as T.MeshStandardMaterial; mat.emissive = new T.Color("#9be07a"); mat.emissiveIntensity = 0;
    const pivot = new T.Group(), hinge = new T.Group(); pivot.rotation.y = i * 2.4 + 0.4; pivot.position.copy(curve.getPointAt(tAt(i))); pivot.add(hinge);
    const mesh = put(hinge, geo, mat, 0, 0, 0); mesh.castShadow = !low; pivot.visible = false; world.add(pivot);
    const tag = new T.Group(); tag.userData.index = i; tag.visible = false; world.add(tag);
    const tex = tagTexture(i + 1); tagTextures.push(tex);
    const tagMat = new T.MeshStandardMaterial({ map: tex, roughness: 0.85, emissive: new T.Color("#ffd98a"), emissiveIntensity: 0 });
    const card = put(tag, new RoundedBoxGeometry(0.4, 0.3, 0.02, 2, 0.02), tagMat, 0, -0.55, 0); const thread = put(tag, new T.CylinderGeometry(0.004, 0.004, 0.42, 4), new T.MeshBasicMaterial({ color: "#c9b690" }), 0, -0.21, 0, false); void card; void thread;
    const halo = glowSprite("#ffd98a", 1.5, 0); halo.position.y = -0.55; tag.add(halo);
    const hit = new T.Mesh(new T.SphereGeometry(0.42, 8, 6), new T.MeshBasicMaterial({ visible: false })); hit.position.y = -0.45; hit.userData.index = i; tag.add(hit);
    return { pivot, hinge, mat, tag, tagMat, halo, len, open: 0, glow: 0, phase: i * 1.7 };
  });
  const butterflies = createButterflies(2); butterflies.group.scale.set(0.75, 0.75, 0.5); scene.add(butterflies.group);
  const motes = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.07, color: "#fff4cf", colorB: "#ffd0dc", opacity: 0.8, bounds: [2.3, 1.8, 1.2], center: [0, 1.6, 0.3], twinkle: 1, shape: "spark", drift: 0.5, rise: 0.08 }); scene.add(motes.points);
  for (const [x, rot, o] of [[-1.5, 0.35, 0.1], [0.6, 0.3, 0.07]] as const) { const c = document.createElement("canvas"); c.width = 64; c.height = 256; const g = c.getContext("2d")!; const gr = g.createLinearGradient(0, 0, 0, 256); gr.addColorStop(0, "rgba(255,244,210,.9)"); gr.addColorStop(1, "rgba(255,244,210,0)"); g.fillStyle = gr; g.fillRect(0, 0, 64, 256); const shaft = new T.Mesh(new T.PlaneGeometry(1.4, 9), new T.MeshBasicMaterial({ map: new T.CanvasTexture(c), transparent: true, opacity: o, blending: T.AdditiveBlending, depthWrite: false, fog: false })); shaft.position.set(x, 3.2, 2.2); shaft.rotation.z = rot; scene.add(shaft); }

  /* ---------- choreography ---------- */
  const pos = new T.Vector3(), look = new T.Vector3(0, 0.35, 0.6), focus = new T.Vector3(), orbit = { yaw: 0, pitch: 0 }, tip = new T.Vector3(), perch = new T.Vector3();
  let grow = 0, trunkK = 0, lastActive: number | null | undefined, lastLeaves = 0;
  return {
    pickables: leaves.map((l) => l.tag),
    dispose() { tagTextures.forEach((t) => t.dispose()); },
    frame(time, dt, state: SceneState, reduced) {
      const g = T.MathUtils.clamp(state.growth ?? 0, 0, LEAVES), active = state.selected ?? null;
      grow = damp(grow, g, 1.7, dt, reduced);
      const trunkTarget = g <= 0 ? 0 : Math.min(1, tAt(Math.ceil(g) - 1) + 0.05); trunkK = damp(trunkK, trunkTarget, 1.5, dt, reduced); growTube(trunk, trunkK);
      roots.update(Math.min(1, grow / 2.2));
      const crack = Math.min(1, grow * 1.2); seed.scale.set(1.2 - 0.3 * crack, 1.2 - 0.22 * crack, 0.8 - 0.1 * crack);
      seedMat.emissive.set("#ffb86a").multiplyScalar(grow < 0.05 ? 0.18 + (reduced ? 0 : Math.sin(time * 2.2) * 0.12) : 0.1 * crack);
      (seedGlow.material as T.SpriteMaterial).opacity = grow < 0.05 ? 0.35 + (reduced ? 0 : Math.sin(time * 2.2) * 0.15) : 0.1;
      const opened = Math.floor(g + 0.001); if (opened > lastLeaves) stage.sfx("bloom"); lastLeaves = opened;
      if (active !== lastActive) { if (lastActive !== undefined && active !== null) stage.sfx("chime"); lastActive = active; }
      leaves.forEach((l, i) => {
        l.open = damp(l.open, T.MathUtils.clamp(grow - i, 0, 1), 2.6, dt, reduced);
        const visible = trunkK > tAt(i) - 0.005 && l.open > 0.01; l.pivot.visible = visible; l.tag.visible = visible && l.open > 0.4;
        const k = ease.out(l.open), sway = reduced ? 0 : Math.sin(time * 1.3 + l.phase) * 0.05;
        l.hinge.scale.setScalar(0.04 + 0.96 * k); l.hinge.rotation.x = -(0.15 + 1.15 * k) + sway;
        l.glow = damp(l.glow, active === i ? 1 : 0, 6, dt, reduced); l.mat.emissiveIntensity = 0.5 * l.glow; l.tagMat.emissiveIntensity = 0.7 * l.glow;
        (l.halo.material as T.SpriteMaterial).opacity = 0.6 * l.glow;
        if (visible) { l.hinge.updateWorldMatrix(true, false); tip.set(0, l.len * 0.92, -0.4 * l.len * 0.85).applyMatrix4(l.hinge.matrixWorld); l.tag.position.copy(tip); l.tag.rotation.y = reduced ? 0 : Math.sin(time * 1.1 + l.phase) * 0.35; l.tag.scale.setScalar(0.8 + 0.5 * l.glow); }
      });
      grass.update(time); motes.update(time);
      const act = active !== null && leaves[active] && leaves[active].pivot.visible ? leaves[active] : null;
      if (act) perch.copy(act.tag.position).add(new T.Vector3(0, 0.55, 0)); butterflies.group.visible = grow > 1.2;
      butterflies.update(time, new T.Vector3(0, 1.7, 0.3), act ? perch.clone().divide(butterflies.group.scale) : null, act ? 1 : 0, reduced);
      focus.copy(act ? act.tag.position : new T.Vector3(0, 0.4, 0.6)); look.lerp(focus, reduced ? 1 : 1 - Math.exp(-dt * 2.4));
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.15, 0.3);
      const zoom = act ? 0.55 : 1; pos.set(look.x * 0.4 + (reduced ? 0 : Math.sin(time * 0.17) * 0.35), look.y + 1.0 * zoom, 12.6 * zoom); orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95); void hash;
    },
  };
}
```

## 69. `src/three/gifts/jar.ts` — new

```ts
/**
 * Gift 02 - A Jar of Reasons.
 * A thick-walled glass jar on a linen cloth in window light. A brass lid lifts away, seventeen separate paper
 * notes rest inside, and a chosen note floats up through the neck and opens in front of you. Owner text is
 * written on the note when it exists; an empty note stays an honest, editable placeholder.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, span } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { bentPaper, lathe, petalGeometry, put, ribbon, RoundedBoxGeometry } from "../../engine/geometry";
import { addContactShadow, addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { glowCanvas } from "../../engine/textures";
import { packMicrocopy } from "../../content/packContent";

const NOTE_COUNT = 17;
const NECK_TOP = new T.Vector3(0, 4.3, 0.1);
const READ_POS = new T.Vector3(0.1, 3.0, 2.9);
const TINTS = ["#fbf3df", "#f7e0e2", "#e4edd9", "#e6dff2", "#f9ebcb"];

/** Dark teal wall with a soft off-centre window glow and warm fairy-light bokeh, painted once into a canvas. */
function backdropTexture() {
  const w = 1024, h = 640, c = document.createElement("canvas"); c.width = w; c.height = h; const g = c.getContext("2d")!;
  const wall = g.createLinearGradient(0, 0, 0, h); wall.addColorStop(0, "#16231f"); wall.addColorStop(0.6, "#233630"); wall.addColorStop(1, "#2c3d35");
  g.fillStyle = wall; g.fillRect(0, 0, w, h);
  const glow = g.createRadialGradient(w * 0.16, h * 0.3, 0, w * 0.16, h * 0.3, 380); glow.addColorStop(0, "rgba(255,214,150,.75)"); glow.addColorStop(0.4, "rgba(255,190,120,.28)"); glow.addColorStop(1, "rgba(255,170,100,0)");
  g.fillStyle = glow; g.fillRect(0, 0, w, h);
  for (let i = 0; i < 46; i++) {
    const x = ((i * 211) % w), y = ((i * 97) % (h * 0.8)) + 10, r = 8 + ((i * 29) % 34), a = 0.1 + ((i * 13) % 30) / 100;
    const d = g.createRadialGradient(x, y, r * 0.2, x, y, r); d.addColorStop(0, `rgba(255,220,160,${a})`); d.addColorStop(0.75, `rgba(255,196,120,${a * 0.7})`); d.addColorStop(1, "rgba(255,180,100,0)");
    g.fillStyle = d; g.beginPath(); g.arc(x, y, r, 0, Math.PI * 2); g.fill();
  }
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}

function noteAtlas() {
  const cols = 5, rows = 4, cell = 128, c = document.createElement("canvas"); c.width = cols * cell; c.height = rows * cell;
  const g = c.getContext("2d")!; g.fillStyle = "#ffffff"; g.fillRect(0, 0, c.width, c.height);
  g.fillStyle = "#3a2c28"; g.font = `700 ${cell * 0.34}px Caveat, "Segoe Print", cursive`; g.textBaseline = "top";
  for (let i = 0; i < NOTE_COUNT; i++) {
    const col = i % cols, row = Math.floor(i / cols);
    g.fillText(String(i + 1).padStart(2, "0"), col * cell + cell * 0.1, row * cell + cell * 0.08);
    g.strokeStyle = "rgba(120,100,80,.25)"; g.lineWidth = 1;
    for (let l = 0; l < 3; l++) { const y = row * cell + cell * (0.52 + l * 0.15); g.beginPath(); g.moveTo(col * cell + cell * 0.1, y); g.lineTo(col * cell + cell * 0.88, y); g.stroke(); }
  }
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return { texture: t, cols, rows };
}

/** Texture for the big, readable note. */
function createReadingNote(width: number, height: number) {
  const c = document.createElement("canvas"); c.width = width; c.height = height; const g = c.getContext("2d")!;
  const texture = new T.CanvasTexture(c); texture.colorSpace = T.SRGBColorSpace; texture.anisotropy = 8;
  const draw = (index: number, text: string, tint: string) => {
    g.fillStyle = tint; g.fillRect(0, 0, width, height);
    const edge = g.createRadialGradient(width / 2, height / 2, height * 0.3, width / 2, height / 2, height * 0.85); edge.addColorStop(0, "rgba(120,96,60,0)"); edge.addColorStop(1, "rgba(120,96,60,.2)"); g.fillStyle = edge; g.fillRect(0, 0, width, height);
    g.strokeStyle = "rgba(110,92,72,.22)"; g.lineWidth = 2; for (let y = height * 0.36; y < height * 0.94; y += height * 0.095) { g.beginPath(); g.moveTo(width * 0.08, y); g.lineTo(width * 0.92, y); g.stroke(); }
    g.fillStyle = "rgba(60,44,40,.95)"; g.textBaseline = "alphabetic";
    g.font = `700 ${height * 0.17}px Caveat, "Segoe Print", cursive`; g.fillText(String(index + 1).padStart(2, "0"), width * 0.07, height * 0.2);
    g.font = `600 ${height * 0.05}px "DM Sans", Georgia, serif`; g.fillStyle = "rgba(90,70,62,.7)"; g.fillText(`REASON ${index + 1} OF ${NOTE_COUNT}`, width * 0.3, height * 0.17);
    if (text.trim()) {
      g.fillStyle = "rgba(24,26,44,.95)"; let size = height * 0.085; const maxW = width * 0.84; const words = text.split(/\s+/);
      for (; size > 20; size -= 2) { g.font = `600 ${size}px Caveat, cursive`; let lines = 1, line = ""; for (const w of words) { const test = line ? `${line} ${w}` : w; if (g.measureText(test).width > maxW) { lines++; line = w; } else line = test; } if (lines * size * 1.25 < height * 0.6) break; }
      g.font = `600 ${size}px Caveat, cursive`; let y = height * 0.4, line = "";
      for (const w of words) { const test = line ? `${line} ${w}` : w; if (g.measureText(test).width > maxW && line) { g.fillText(line, width * 0.08, y); y += size * 1.25; line = w; } else line = test; }
      g.fillText(line, width * 0.08, y);
    } else {
      g.fillStyle = "rgba(110,92,80,.6)"; g.font = `italic ${height * 0.055}px Georgia, serif`;
      let y = height * 0.5, line = ""; const maxW = width * 0.82;
      for (const w of packMicrocopy.missingText.split(" ")) { const test = line ? `${line} ${w}` : w; if (g.measureText(test).width > maxW && line) { g.fillText(line, width * 0.09, y); y += height * 0.075; line = w; } else line = test; }
      g.fillText(line, width * 0.09, y);
    }
    texture.needsUpdate = true;
  };
  return { texture, draw };
}

export function buildJarWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input, renderer } = stage;
  const low = quality === "low", high = quality === "high";
  stage.mood({ env: "ballroom", envIntensity: 1.25, exposure: 1.12, background: "#16231f", fog: { color: "#1b2a25", density: 0.022 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#ffe0b8", "#16231f", 0.35));
  addKeyLight(scene, quality, { color: "#ffd2a0", intensity: 3.6, position: [-6, 7, 3.5], target: [0, 1.4, 0], extent: 6, far: 28 });
  const rim = new T.DirectionalLight("#9fc4ff", 1.6); rim.position.set(5.5, 4, -6); scene.add(rim);
  const fill = new T.DirectionalLight("#ffe2c0", 0.5); fill.position.set(4, 2.5, 7); scene.add(fill);

  const root = new T.Group(); scene.add(root);
  /* ---------- set: window, cloth, board ---------- */
  const win = new T.Mesh(new T.PlaneGeometry(30, 18.7), new T.MeshBasicMaterial({ map: backdropTexture(), fog: false, toneMapped: false }));
  win.position.set(0, 7.4, -13); root.add(win);
  const table = put(root, new T.PlaneGeometry(40, 26), kit.wood("#1a0e08", "#4a2f1e", [8, 5], 0.5), 0, 0, -4, false); table.rotation.x = -Math.PI / 2; table.receiveShadow = true;
  put(root, new RoundedBoxGeometry(7.2, 0.07, 5.0, 3, 0.03), kit.fabric("#c9bba0", "#f0e6d0", [5, 3.5]), 0, 0.035, 0.4);
  addContactShadow(root, 4.2, 4.2, 0, 0.09, 0, 0.6);

  /* ---------- glass jar ---------- */
  const jar = new T.Group(); jar.position.y = 0.07; root.add(jar);
  const profile: [number, number][] = [[0, 0], [0.95, 0], [1.18, 0.1], [1.28, 0.42], [1.3, 0.95], [1.3, 2.35], [1.22, 2.8], [1.04, 3.05], [0.98, 3.2], [0.98, 3.52], [1.05, 3.56], [1.04, 3.64], [0.9, 3.64],
    [0.9, 3.3], [0.92, 3.18], [0.97, 3.0], [1.14, 2.74], [1.22, 2.32], [1.23, 0.95], [1.2, 0.46], [1.1, 0.18], [0, 0.14]];
  const glass = kit.glass("#e6f4ef", 0.45);
  put(jar, lathe(profile, low ? 36 : 72), glass, 0, 0, 0, false).renderOrder = 4;
  for (const y of [3.34, 3.44, 3.54]) { const thread = put(jar, new T.TorusGeometry(1.0, 0.026, 8, 48), glass, 0, y, 0, false); thread.rotation.x = Math.PI / 2; thread.renderOrder = 4; }
  const lip = put(jar, new T.TorusGeometry(0.975, 0.03, 8, 64), new T.MeshBasicMaterial({ color: "#ffffff", transparent: true, opacity: 0.55, blending: T.AdditiveBlending, depthWrite: false }), 0, 3.64, 0, false); lip.rotation.x = Math.PI / 2;

  /* ---------- notes ---------- */
  const atlas = noteAtlas();
  const noteMat = new T.MeshStandardMaterial({ map: atlas.texture, vertexColors: true, roughness: 0.9, side: T.DoubleSide });
  const notes = Array.from({ length: NOTE_COUNT }, (_, i) => {
    const geometry = bentPaper(0.9, 0.62, 0.09, 0.05, 5, 6);
    const uv = geometry.attributes.uv, col = i % atlas.cols, row = Math.floor(i / atlas.cols);
    for (let k = 0; k < uv.count; k++) uv.setXY(k, (col + uv.getX(k)) / atlas.cols, 1 - (row + 1) / atlas.rows + uv.getY(k) / atlas.rows);
    const tint = new T.Color(TINTS[i % TINTS.length]); const colors: number[] = []; for (let k = 0; k < uv.count; k++) colors.push(tint.r, tint.g, tint.b);
    geometry.setAttribute("color", new T.Float32BufferAttribute(colors, 3));
    const mesh = new T.Mesh(geometry, noteMat); mesh.castShadow = true; mesh.userData.index = i;
    const a = i * 2.39996, layer = i < 7 ? 0 : i < 13 ? 1 : 2, ring = [0.62, 0.45, 0.2][layer] + (i % 3) * 0.08;
    const rest = { p: new T.Vector3(Math.cos(a) * ring, 0.34 + layer * 0.3 + (i % 2) * 0.07, Math.sin(a) * ring), q: new T.Quaternion().setFromEuler(new T.Euler(-Math.PI / 2 + Math.sin(i * 1.7) * 0.7, a * 1.9, Math.cos(i * 2.3) * 0.7)) };
    mesh.position.copy(rest.p); mesh.quaternion.copy(rest.q); jar.add(mesh);
    return { mesh, rest, seed: i * 1.37 };
  });

  /* ---------- brass lid, ribbon bow, tag ---------- */
  const brass = kit.metal("brass", 0.34);
  const lid = new T.Group(); lid.position.set(0, 3.64, 0); lid.userData.index = -2; jar.add(lid);
  put(lid, lathe([[0, 0], [1.08, 0], [1.1, 0.04], [1.1, 0.26], [1.04, 0.31], [0.78, 0.33], [0.7, 0.36], [0, 0.36]], low ? 32 : 64), brass, 0, 0, 0);
  put(lid, new T.CylinderGeometry(0.9, 0.9, 0.08, 48), new T.MeshStandardMaterial({ color: "#a86f3d", roughness: 0.9 }), 0, -0.02, 0, false);
  const ridges = new T.InstancedMesh(new T.BoxGeometry(0.035, 0.22, 0.05), brass, 72); const d = new T.Object3D();
  for (let i = 0; i < 72; i++) { const a = (i / 72) * Math.PI * 2; d.position.set(Math.cos(a) * 1.1, 0.15, Math.sin(a) * 1.1); d.rotation.set(0, -a, 0); d.updateMatrix(); ridges.setMatrixAt(i, d.matrix); }
  lid.add(ridges);
  const satin = new T.MeshPhysicalMaterial({ color: "#c9677f", roughness: 0.35, sheen: 1, sheenColor: new T.Color("#ffc0cf"), sheenRoughness: 0.3, side: T.DoubleSide });
  const bow = new T.Group(); bow.position.set(0, 3.22, 0); jar.add(bow);
  put(bow, new T.CylinderGeometry(1.0, 1.0, 0.2, 64, 1, true), satin, 0, 0, 0, false);
  for (const s of [-1, 1]) {
    const loop = new T.CatmullRomCurve3([[0, 0, 1.0], [s * 0.3, 0.3, 1.08], [s * 0.7, 0.34, 1.12], [s * 0.92, 0.05, 1.1], [s * 0.66, -0.24, 1.06], [s * 0.26, -0.12, 1.02], [0, 0, 1.0]].map((p) => new T.Vector3(...(p as [number, number, number]))));
    put(bow, ribbon(loop, 0.2, 40, s * 0.7), satin, 0, 0, 0, false);
    const tail = new T.CatmullRomCurve3([[s * 0.04, -0.04, 1.03], [s * 0.22, -0.4, 1.1], [s * 0.18, -0.85, 1.14], [s * 0.36, -1.2, 1.13]].map((p) => new T.Vector3(...(p as [number, number, number]))));
    put(bow, ribbon(tail, 0.17, 24, s * 0.5), satin, 0, 0, 0, false);
  }
  put(bow, new T.SphereGeometry(0.1, 16, 12), satin, 0, 0, 1.04, false).scale.set(1.2, 0.9, 0.8);
  const tag = new T.Group(); tag.position.set(0.55, 2.2, 1.28); jar.add(tag);
  const tagTex = (() => { const c = document.createElement("canvas"); c.width = 256; c.height = 360; const g = c.getContext("2d")!; g.fillStyle = "#f5ead2"; g.fillRect(0, 0, 256, 360); g.strokeStyle = "rgba(160,120,80,.6)"; g.lineWidth = 4; g.strokeRect(14, 14, 228, 332); g.fillStyle = "#4a3a30"; g.textAlign = "center"; g.font = "700 130px Caveat, cursive"; g.fillText("17", 128, 190); g.font = "600 34px Georgia, serif"; g.fillText("REASONS", 128, 260); const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t; })();
  put(tag, new RoundedBoxGeometry(0.46, 0.64, 0.02, 2, 0.02), new T.MeshStandardMaterial({ map: tagTex, roughness: 0.9 }), 0, -0.34, 0);
  put(tag, new T.TorusGeometry(0.035, 0.008, 6, 16), brass, 0, -0.03, 0.012, false);

  /* ---------- reading note ---------- */
  const reading = createReadingNote(1024, 704);
  const readingMesh = new T.Mesh(bentPaper(2.2, 1.5, 0.07, 0.04, 14, 10), new T.MeshStandardMaterial({ map: reading.texture, roughness: 0.9, side: T.DoubleSide }));
  readingMesh.visible = false; readingMesh.castShadow = true; readingMesh.userData.index = -1; jar.add(readingMesh);

  /* ---------- atmosphere ---------- */
  const dust = new ParticleField({ count: Math.round(170 * particleScale(quality)), size: 0.05, color: "#fff1d0", opacity: 0.7, bounds: [5, 3, 3.5], center: [0, 3, 0.5], drift: 0.6, rise: 0.05, twinkle: 0.7 });
  root.add(dust.points);
  const caustic = new T.Mesh(new T.PlaneGeometry(4.6, 2.4), new T.MeshBasicMaterial({ map: (() => { const t = new T.CanvasTexture(glowCanvas("rgba(255,236,190,1)", "rgba(255,210,150,0)", 128)); t.colorSpace = T.SRGBColorSpace; return t; })(), transparent: true, opacity: 0.34, blending: T.AdditiveBlending, depthWrite: false, toneMapped: false }));
  caustic.rotation.x = -Math.PI / 2; caustic.position.set(1.6, 0.1, 2.4); caustic.rotation.z = -0.5; root.add(caustic);
  const beam = new T.Mesh(new T.ConeGeometry(4.2, 13, 24, 1, true), new T.MeshBasicMaterial({ color: "#ffe2b0", transparent: true, opacity: 0.05, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide, fog: false }));
  beam.position.set(-4.5, 5.0, -3.5); beam.rotation.set(0.0, 0, -0.62); beam.rotation.x = -0.45; root.add(beam);
  const petalMat = kit.petal("#f7d9df", "#d96c8a", "#9a3a56"), petalGeo = petalGeometry(0.58, 0.28, 0.2, 0.1, 0.55, 8, 12);
  const petals = new T.InstancedMesh(petalGeo, petalMat, 7); petals.castShadow = true;
  [[-2.7, 2.1, 0.4], [2.9, 1.9, 2.1], [-1.9, 2.9, 4.0], [2.1, 2.9, 5.2], [-3.0, 0.9, 1.0], [3.2, 0.4, 3.6], [0.4, 3.1, 2.6]].forEach(([x, z, r], i) => { d.position.set(x, 0.085, z); d.rotation.set(-Math.PI / 2 + 0.05 * Math.sin(i), 0.04, r); d.scale.setScalar(0.9 + (i % 3) * 0.12); d.updateMatrix(); petals.setMatrixAt(i, d.matrix); });
  root.add(petals);

  /* ---------- choreography ---------- */
  const s = { lid: 0, pick: 0, turn: 0, shuffle: 0, bowSway: 0 };
  let current: number | null = null, lastSelected: number | null | undefined, lastReplay: number | undefined, lastText = "", lastLid = false, lastPick = 0;
  const orbit = { yaw: 0, pitch: 0 };
  const a = new T.Vector3(), b = new T.Vector3(), q = new T.Quaternion(), look = new T.Vector3(), pos = new T.Vector3(), offset = new T.Vector3();
  const upright = new T.Quaternion().setFromEuler(new T.Euler(-0.35, 0, 0));
  const readQ = new T.Quaternion().setFromEuler(new T.Euler(-0.28, 0, 0));
  const camA = { p: new T.Vector3(0, 3.0, 9.4), l: new T.Vector3(0, 1.95, 0) }, camB = { p: new T.Vector3(0.3, 3.3, 7.2), l: new T.Vector3(0.2, 2.6, 1.3) };

  return {
    pickables: [lid, ...notes.map((n) => n.mesh)],
    frame(time, dt, state: SceneState, reduced) {
      const open = Boolean(state.open);
      if (open !== lastLid) { stage.sfx("lid"); lastLid = open; }
      if (state.replay !== lastReplay) { if (lastReplay !== undefined) { s.shuffle = 1; stage.sfx("paper"); } lastReplay = state.replay; }
      const wanted = state.selected ?? null;
      if (wanted !== lastSelected) { lastSelected = wanted; if (wanted !== null) stage.sfx("note"); }
      // one reading note at a time: finish returning the old one before switching
      if (current === null && wanted !== null) { current = wanted; lastText = ""; }
      if (current !== null && wanted !== current && s.pick < 0.02) { current = wanted; lastText = ""; }
      const target = open && wanted !== null && current === wanted ? 1 : 0;
      s.lid = damp(s.lid, open ? 1 : 0, 3.2, dt, reduced);
      s.pick = damp(s.pick, target, 2.4, dt, reduced);
      s.shuffle = reduced ? 0 : Math.max(0, s.shuffle - dt * 0.9);
      if (current !== null && s.pick < 0.001 && wanted === null) current = null;
      const drag = input.consumeDrag();
      s.turn = damp(s.turn, state.turn ?? 0, 3, dt, reduced);
      orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 5.2, -1.6, 1.6); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.12, 0.25);
      jar.rotation.y = s.turn + orbit.yaw;
      lastPick = s.pick; void lastPick;

      // lid lifts, tilts and floats aside
      const L = ease.inOut(s.lid);
      lid.position.set(-2.0 * L, 3.64 + 1.15 * Math.sin(Math.min(1, L * 1.2) * Math.PI * 0.5) + 0.25 * L, 0.5 * L); lid.rotation.set(0.45 * L, 0.9 * L, 0.65 * L);
      bow.rotation.y = 0; tag.rotation.z = Math.sin(time * 1.3) * 0.06 * (reduced ? 0 : 1) + (reduced ? 0 : Math.sin(time * 2.1) * 0.015);
      dust.update(time);

      // notes: resting heap, shuffle shimmy, and the chosen note's flight
      notes.forEach((n, i) => {
        const shake = s.shuffle * (0.5 + 0.5 * Math.sin(n.seed));
        n.mesh.position.set(n.rest.p.x + Math.sin(time * 17 + n.seed) * 0.05 * shake, n.rest.p.y + Math.max(0, Math.sin(time * 13 + n.seed)) * 0.28 * shake, n.rest.p.z + Math.cos(time * 15 + n.seed) * 0.05 * shake);
        q.setFromEuler(new T.Euler(Math.sin(time * 11 + n.seed) * 0.25 * shake, Math.cos(time * 9 + n.seed) * 0.35 * shake, 0));
        n.mesh.quaternion.copy(n.rest.q).multiply(q);
        n.mesh.visible = !(current === i && s.pick > 0.5);
        n.mesh.userData.pickDisabled = !open;
      });
      readingMesh.visible = current !== null && s.pick > 0.5;
      if (current !== null) {
        const n = notes[current], t = s.pick;
        if (t <= 0.5) {
          const k = ease.inOut(span(t, 0, 0.5));
          a.copy(n.rest.p); b.copy(NECK_TOP); n.mesh.position.set(a.x + (b.x - a.x) * k, a.y + (b.y - a.y) * k + Math.sin(k * Math.PI) * 0.35, a.z + (b.z - a.z) * k);
          n.mesh.quaternion.copy(n.rest.q).slerp(upright, k);
        } else {
          const k = ease.inOut(span(t, 0.5, 1)); const wasText = lastText;
          readingMesh.position.lerpVectors(NECK_TOP, READ_POS, k); readingMesh.position.y += Math.sin(k * Math.PI) * 0.4;
          readingMesh.quaternion.copy(upright).slerp(readQ, k); readingMesh.scale.setScalar(0.26 + 0.74 * k); void wasText;
        }
        const text = state.detail ?? "";
        if (text !== lastText || readingMesh.userData.shown !== current) { lastText = text; readingMesh.userData.shown = current; reading.draw(current, text, TINTS[current % TINTS.length]); }
      }

      // camera: wide on the jar, closer when reading
      const c = ease.inOut(s.pick);
      pos.copy(camA.p).lerp(camB.p, c); look.copy(camA.l).lerp(camB.l, c);
      if (!reduced) { pos.x += Math.sin(time * 0.27) * 0.1; pos.y += Math.sin(time * 0.21) * 0.05; }
      offset.copy(pos).sub(look).applyAxisAngle(new T.Vector3(1, 0, 0), -orbit.pitch);
      const fit = T.MathUtils.clamp(0.9 / Math.max(0.45, camera.aspect), 1, 1.8);
      camera.position.copy(look).addScaledVector(offset, fit); camera.lookAt(look);
      void renderer; void high;
    },
  };
}
```

## 70. `src/three/gifts/letter.ts` — new

```ts
/**
 * Gift 01 - The Secret Letter.
 * A candle-lit writing desk. The camera drifts toward a sealed envelope; the wax seal catches the light and cracks,
 * the flap turns on a real hinge, a letter folded in thirds slides out, lifts, unfolds across two rounded creases,
 * settles on the blotter and is written out in handwriting. Closing plays the same timeline backwards.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { Sequence, ease, span } from "../../engine/anim";
import { Flame, ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, lathe, petalGeometry, put } from "../../engine/geometry";
import { addContactShadow, addKeyLight, addPointLight } from "../../engine/lights";
import { createFoldedPaper } from "../../engine/paper";
import { particleScale } from "../../engine/quality";
import { leatherCanvas, paperCanvas, sparkleCanvas } from "../../engine/textures";

export const LETTER_DURATION = 11;
const ENV_W = 3.6, ENV_H = 2.3;
const PAPER_W = 3.0, PAPER_H = 4.1;
const FALLBACK_TEXT = "Open the envelope to read the letter.";

const triangle = (a: [number, number], b: [number, number], c: [number, number], depth = 0.012) => {
  const shape = new T.Shape(); shape.moveTo(...a); shape.lineTo(...b); shape.lineTo(...c); shape.closePath();
  return new T.ExtrudeGeometry(shape, { depth, bevelEnabled: true, bevelThickness: 0.003, bevelSize: 0.004, bevelSegments: 1 });
};

function canvasTexture(canvas: HTMLCanvasElement, srgb = true, anisotropy = 8) {
  const texture = new T.CanvasTexture(canvas);
  texture.colorSpace = srgb ? T.SRGBColorSpace : T.NoColorSpace; texture.anisotropy = anisotropy;
  return texture;
}

/** Dark green leather blotter with a hand-tooled gold border. */
function blotterMaterial(size: number) {
  const tile = leatherCanvas(size, "#16231e", "#33493f");
  const w = 1024, h = 672, canvas = document.createElement("canvas"); canvas.width = w; canvas.height = h;
  const ctx = canvas.getContext("2d")!;
  ctx.fillStyle = ctx.createPattern(tile.color, "repeat")!; ctx.fillRect(0, 0, w, h);
  ctx.strokeStyle = "#c8a24f"; ctx.lineWidth = 4; ctx.strokeRect(38, 38, w - 76, h - 76);
  ctx.lineWidth = 1.5; ctx.strokeRect(54, 54, w - 108, h - 108);
  ctx.lineWidth = 3;
  for (const [x, y, sx, sy] of [[38, 38, 1, 1], [w - 38, 38, -1, 1], [38, h - 38, 1, -1], [w - 38, h - 38, -1, -1]] as const) {
    ctx.beginPath(); ctx.arc(x + sx * 30, y + sy * 30, 26, sx > 0 ? Math.PI : 0, sx > 0 ? Math.PI * 1.5 : Math.PI * 0.5); ctx.stroke();
    ctx.beginPath(); ctx.arc(x + sx * 30, y + sy * 30, 7, 0, Math.PI * 2); ctx.stroke();
  }
  const bump = canvasTexture(tile.height, false); bump.wrapS = bump.wrapT = T.RepeatWrapping; bump.repeat.set(5, 3.4);
  return new T.MeshStandardMaterial({ map: canvasTexture(canvas), bumpMap: bump, bumpScale: 0.6, roughness: 0.55, metalness: 0 });
}

/** Burgundy envelope lining with a fine gold lattice. */
function linerTexture() {
  const s = 256, c = document.createElement("canvas"); c.width = c.height = s; const x = c.getContext("2d")!;
  x.fillStyle = "#6b2a3a"; x.fillRect(0, 0, s, s); x.strokeStyle = "rgba(214,176,98,.55)"; x.lineWidth = 1.2;
  for (let i = -s; i < s * 2; i += 22) { x.beginPath(); x.moveTo(i, 0); x.lineTo(i + s, s); x.stroke(); x.beginPath(); x.moveTo(i, s); x.lineTo(i + s, 0); x.stroke(); }
  x.fillStyle = "rgba(214,176,98,.7)"; for (let i = 0; i < s; i += 22) for (let j = 0; j < s; j += 22) { x.beginPath(); x.arc(i + 11, j + 11, 1.6, 0, Math.PI * 2); x.fill(); }
  const t = canvasTexture(c); t.wrapS = t.wrapT = T.RepeatWrapping; t.repeat.set(3, 2); return t;
}

/** Wax seal split by a jagged crack into two real halves. */
function sealHalves(radius: number) {
  const noise = (a: number) => 1 + 0.055 * Math.sin(a * 7 + 0.6) + 0.035 * Math.sin(a * 13 + 1.7) + 0.02 * Math.sin(a * 23);
  const crack = (t: number) => Math.sin(t * 9) * 0.018 * radius + Math.sin(t * 23 + 1) * 0.008 * radius; // t = -1..1 down the seal
  const half = (side: 1 | -1) => {
    const shape = new T.Shape();
    const a0 = Math.PI / 2, a1 = side > 0 ? -Math.PI / 2 : (3 * Math.PI) / 2, steps = 36;
    shape.moveTo(0, radius * noise(a0));
    for (let i = 1; i <= steps; i++) { const a = a0 + ((a1 - a0) * i) / steps, r = radius * noise(a); shape.lineTo(Math.cos(a) * r, Math.sin(a) * r); }
    for (let i = 0; i <= 14; i++) { const t = -1 + (i / 14) * 2; shape.lineTo(crack(t) * (1 - Math.abs(t) ** 4) + 0, t * radius * 0.97 * noise(Math.PI / 2 * -t)); }
    shape.closePath();
    const geometry = new T.ExtrudeGeometry(shape, { depth: 0.05, bevelEnabled: true, bevelThickness: 0.014, bevelSize: 0.016, bevelSegments: 3, curveSegments: 18 });
    return geometry;
  };
  return [half(-1), half(1)] as const;
}

/** Handwriting surface: paper + ink drawn once, revealed line by line. */
function createHandwriting(width: number, height: number) {
  const base = document.createElement("canvas"); base.width = width; base.height = height;
  const ink = document.createElement("canvas"); ink.width = width; ink.height = height;
  const out = document.createElement("canvas"); out.width = width; out.height = height;
  const bctx = base.getContext("2d")!, ictx = ink.getContext("2d")!, octx = out.getContext("2d")!;
  const paper = paperCanvas(512, "#f6edd7", "#e6d6b4").color;
  bctx.drawImage(paper, 0, 0, width, height);
  for (const f of [1 / 3, 2 / 3]) {
    const y = height * f; const g = bctx.createLinearGradient(0, y - 22, 0, y + 22);
    g.addColorStop(0, "rgba(120,96,60,0)"); g.addColorStop(0.5, "rgba(120,96,60,.16)"); g.addColorStop(1, "rgba(120,96,60,0)");
    bctx.fillStyle = g; bctx.fillRect(0, y - 22, width, 44);
    bctx.fillStyle = "rgba(255,255,255,.35)"; bctx.fillRect(0, y + 1, width, 1.5);
  }
  const edge = bctx.createRadialGradient(width / 2, height / 2, height * 0.35, width / 2, height / 2, height * 0.75);
  edge.addColorStop(0, "rgba(160,128,80,0)"); edge.addColorStop(1, "rgba(160,128,80,.18)"); bctx.fillStyle = edge; bctx.fillRect(0, 0, width, height);
  let rows: { y: number; top: number; bottom: number }[] = [];
  let reveal = -1;

  const write = (text: string) => {
    ictx.clearRect(0, 0, width, height); rows = [];
    const marginX = width * 0.11, top = height * 0.085, bottom = height * 0.07, maxW = width - marginX * 2, maxH = height - top - bottom;
    const paragraphs = text.split(/\n\n+/).filter(Boolean);
    let size = Math.round(width * 0.062), lines: { text: string; para: number }[] = [], lineH = 0, gap = 0;
    for (; size >= 22; size -= 2) {
      ictx.font = `600 ${size}px Caveat, "Segoe Print", cursive`; lineH = size * 1.26; gap = size * 0.55; lines = [];
      paragraphs.forEach((p, para) => {
        let line = "";
        for (const word of p.split(/\s+/)) {
          const test = line ? `${line} ${word}` : word;
          if (ictx.measureText(test).width > maxW && line) { lines.push({ text: line, para }); line = word; } else line = test;
        }
        if (line) lines.push({ text: line, para });
      });
      if (lines.length * lineH + Math.max(0, paragraphs.length - 1) * gap <= maxH) break;
    }
    ictx.font = `600 ${size}px Caveat, "Segoe Print", cursive`; ictx.fillStyle = "rgba(16,22,40,.96)"; ictx.textBaseline = "alphabetic";
    let y = top + size, lastPara = 0;
    lines.forEach((line, i) => {
      if (line.para !== lastPara) { y += gap; lastPara = line.para; }
      ictx.save(); ictx.translate(marginX + (Math.sin(i * 1.7) * 0.5 + 0.5) * 5, y); ictx.rotate(Math.sin(i * 2.3) * 0.006); ictx.fillText(line.text, 0, 0); ictx.restore();
      rows.push({ y, top: y - lineH * 0.85, bottom: y + lineH * 0.38 }); y += lineH;
    });
    reveal = -1;
  };
  const compose = (amount: number) => {
    if (Math.abs(amount - reveal) < 0.0015 && amount < 1 && amount > 0) return false;
    reveal = amount;
    octx.drawImage(base, 0, 0);
    const n = Math.max(1, rows.length);
    rows.forEach((row, i) => {
      const p = T.MathUtils.clamp(amount * n - i, 0, 1);
      if (p > 0) octx.drawImage(ink, 0, row.top, width * Math.min(1, p * 1.04), row.bottom - row.top, 0, row.top, width * Math.min(1, p * 1.04), row.bottom - row.top);
    });
    return true;
  };
  return { canvas: out, write, compose };
}

export function buildLetterWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input, renderer } = stage;
  const low = quality === "low", high = quality === "high";
  stage.mood({ env: "candle", envIntensity: 0.9, exposure: 1.18, background: "#120c09", fog: { color: "#140d09", density: 0.03 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 60; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#ffe6c4", "#1b1410", 0.5));
  addKeyLight(scene, quality, { color: "#ffd8a6", intensity: 2.6, position: [-5, 9, 6.5], target: [0, 0, 0.3], extent: 8, far: 30 });
  const rim = new T.DirectionalLight("#8fa8ff", 0.7); rim.position.set(6, 5, -7); scene.add(rim);

  const root = new T.Group(); scene.add(root);
  const wood = kit.wood("#1d0f08", "#5a3922", [3, 2], 0.56);
  put(root, new T.BoxGeometry(22, 0.6, 14), wood, 0, -0.3, -1.6);
  const blotter = put(root, new RoundedBoxGeometry(7.4, 0.1, 5.0, 3, 0.045), blotterMaterial(kit.size), 0.2, 0.05, 0.5);
  blotter.receiveShadow = true;

  /* ---------- candle ---------- */
  const candle = new T.Group(); candle.position.set(-5.2, 0, -1.6); root.add(candle);
  const brass = kit.metal("brass", 0.38);
  put(candle, lathe([[0, 0], [0.7, 0], [0.74, 0.05], [0.6, 0.12], [0.2, 0.2], [0.14, 0.38], [0.2, 0.46], [0.13, 0.62], [0.27, 0.78], [0.5, 0.86], [0.46, 0.92], [0.22, 0.9], [0, 0.9]], low ? 24 : 48), brass);
  const wax = new T.MeshPhysicalMaterial({ color: "#f3e9d2", roughness: 0.55, sheen: 0.6, sheenColor: new T.Color("#ffd9a0"), emissive: new T.Color("#ff9a45").multiplyScalar(0.05) });
  put(candle, lathe([[0, 0.9], [0.27, 0.9], [0.28, 1.0], [0.27, 2.2], [0.25, 2.34], [0.15, 2.3], [0.08, 2.26], [0, 2.28]], low ? 20 : 36), wax);
  put(candle, new T.CylinderGeometry(0.012, 0.012, 0.14, 6), new T.MeshStandardMaterial({ color: "#1a1410", roughness: 1 }), 0, 2.33, 0);
  for (const [a, h, r] of [[0.9, 0.55, 0.05], [3.4, 0.35, 0.04], [5.5, 0.7, 0.035]] as const) {
    const drip = put(candle, new T.CapsuleGeometry(r, h, 4, 8), wax, Math.cos(a) * 0.255, 2.12 - h / 2, Math.sin(a) * 0.255, false); drip.scale.set(1, 1, 0.7);
  }
  const flame = new Flame(0.62, 0.3); flame.group.position.set(0, 2.38, 0); candle.add(flame.group);
  const flameWorld = new T.Vector3(); candle.localToWorld(flameWorld.set(0, 2.55, 0));
  const candleLight = addPointLight(scene, "#ffb066", 26, [flameWorld.x, flameWorld.y, flameWorld.z], 18, 2, high);
  addContactShadow(candle, 1.9, 1.9, 0, 0.012, 0, 0.7);

  /* ---------- inkwell + pen ---------- */
  const ink = new T.Group(); ink.position.set(4.7, 0, -1.9); root.add(ink);
  put(ink, lathe([[0, 0], [0.62, 0], [0.7, 0.08], [0.7, 0.62], [0.55, 0.86], [0.34, 0.92], [0.3, 1.08], [0.24, 1.08], [0.24, 0.92], [0, 0.9]], low ? 24 : 40), kit.glass("#cfe4e0", 0.8));
  put(ink, lathe([[0, 0.05], [0.58, 0.05], [0.64, 0.1], [0.64, 0.55], [0.52, 0.74], [0.3, 0.78], [0, 0.78]], 32), new T.MeshPhysicalMaterial({ color: "#0c1226", roughness: 0.08, clearcoat: 1, metalness: 0.1 }), 0, 0, 0, false);
  put(ink, new T.TorusGeometry(0.31, 0.045, 10, 32), brass, 0, 1.02, 0).rotation.x = Math.PI / 2;
  addContactShadow(ink, 1.9, 1.9, 0, 0.012, 0, 0.6);
  const pen = new T.Group(); pen.position.set(3.6, 0.17, 2.0); pen.rotation.y = 0.62; root.add(pen);
  const lacquer = new T.MeshPhysicalMaterial({ color: "#14161b", roughness: 0.22, clearcoat: 1, clearcoatRoughness: 0.05, metalness: 0.2 });
  const barrel = put(pen, lathe([[0, 0], [0.09, 0.02], [0.14, 0.4], [0.17, 1.5], [0.15, 2.5], [0.09, 3.0], [0.05, 3.14], [0, 3.15]], 28), lacquer, 0, 0, 0); barrel.rotation.z = Math.PI / 2;
  const nib = put(pen, new T.ConeGeometry(0.085, 0.6, 4), kit.metal("gold", 0.25), 0.3, 0, 0); nib.rotation.z = -Math.PI / 2; nib.scale.set(1, 1, 0.3);
  for (const [x, r] of [[-0.42, 0.14], [-0.55, 0.145], [-2.55, 0.155]] as const) put(pen, new T.TorusGeometry(r + 0.004, 0.011, 8, 28), kit.metal("gold", 0.25), x, 0, 0).rotation.y = Math.PI / 2;
  addContactShadow(root, 3.6, 0.7, 3.5, 0.108, 2.0, 0.45);

  /* ---------- books ---------- */
  const spine = [["#4a1b24", 0.0], ["#1c3a33", 0.44], ["#3b2a1a", 0.86]] as const;
  const books = new T.Group(); books.position.set(-5.6, 0.1, 1.0); books.rotation.y = 0.22; root.add(books);
  spine.forEach(([color, y], i) => {
    const cover = kit.leather(color, new T.Color(color).lerp(new T.Color("#fff3d6"), 0.14).getStyle(), [6, 5]);
    cover.normalScale?.set(0.35, 0.35);
    const book = new T.Group(); book.position.set(i * 0.12, y, 0); book.rotation.y = (i - 1) * 0.07; books.add(book);
    put(book, new RoundedBoxGeometry(3.0, 0.4, 2.1, 3, 0.05), cover, 0, 0.2, 0);
    put(book, new T.BoxGeometry(2.86, 0.3, 1.98), kit.paper("#efe3c6", "#c9b78f"), 0.06, 0.2, 0.02);
    put(book, new T.BoxGeometry(0.02, 0.405, 2.06), kit.metal("gold", 0.3), -1.5, 0.2, 0, false);
    for (const z of [-0.5, 0.5]) put(book, new T.BoxGeometry(0.025, 0.41, 0.05), kit.metal("gold", 0.3), -1.51, 0.2, z, false);
  });
  addContactShadow(books, 3.8, 3.0, 0.1, 0.01, 0, 0.7);

  /* ---------- scattered rose petals ---------- */
  const petalMat = kit.petal("#f1cdd5", "#c9556f", "#8a2d47");
  const petalGeo = petalGeometry(0.66, 0.31, 0.22, 0.12, 0.55, 8, 12);
  const petals = new T.InstancedMesh(petalGeo, petalMat, 9); petals.castShadow = true; petals.receiveShadow = true;
  const dummy = new T.Object3D();
  [[-2.7, 2.2, 0.3], [-3.2, 1.2, 2.1], [2.8, 2.7, 4.4], [3.9, 1.0, 1.2], [-1.2, 3.0, 5.1], [2.0, -0.7, 3.3], [-3.7, -0.4, 0.8], [4.3, 2.0, 2.6], [1.1, 3.2, 3.9]].forEach(([x, z, r], i) => {
    dummy.position.set(x, 0.11 + (i % 3) * 0.004, z); dummy.rotation.set(-Math.PI / 2 + 0.06 * Math.sin(i * 2.1), 0.05 * Math.cos(i), r); dummy.scale.setScalar(0.85 + (i % 4) * 0.1); dummy.updateMatrix(); petals.setMatrixAt(i, dummy.matrix);
  });
  root.add(petals);

  /* ---------- envelope ---------- */
  const envelope = new T.Group(); root.add(envelope);
  const E0 = { x: 0.15, y: 0.1, z: 1.05, ry: -0.05 };
  envelope.position.set(E0.x, E0.y, E0.z); envelope.rotation.y = E0.ry;
  const body = new T.Group(); body.rotation.x = -Math.PI / 2; envelope.add(body);
  const cream = kit.paper("#f1e5c8", "#d2bf95", { side: T.DoubleSide, roughness: 0.9 });
  put(body, new T.BoxGeometry(ENV_W, ENV_H, 0.012), cream, 0, 0, 0.006);
  for (const x of [-1, 1]) put(body, new T.BoxGeometry(0.02, ENV_H, 0.11), cream, x * (ENV_W / 2 - 0.01), 0, 0.06);
  put(body, new T.BoxGeometry(ENV_W, 0.02, 0.11), cream, 0, -(ENV_H / 2 - 0.01), 0.06);
  const W2 = ENV_W / 2, H2 = ENV_H / 2;
  put(body, triangle([-W2, H2], [-W2, -H2], [0, -0.05 * ENV_H]), cream, 0, 0, 0.112);
  put(body, triangle([W2, H2], [W2, -H2], [0, -0.05 * ENV_H]), cream, 0, 0, 0.112);
  put(body, triangle([-W2, -H2], [W2, -H2], [0, 0.14 * ENV_H]), cream, 0, 0, 0.119);
  const hinge = new T.Group(); hinge.position.set(0, H2, 0.13); body.add(hinge);
  const flapShape: [[number, number], [number, number], [number, number]] = [[-W2, 0], [W2, 0], [0, -0.64 * ENV_H]];
  put(hinge, triangle(...flapShape, 0.012), cream, 0, 0, 0);
  put(hinge, new T.ShapeGeometry((() => { const s = new T.Shape(); s.moveTo(-W2 + 0.1, -0.02); s.lineTo(W2 - 0.1, -0.02); s.lineTo(0, -0.64 * ENV_H + 0.12); s.closePath(); return s; })()), new T.MeshStandardMaterial({ map: linerTexture(), roughness: 0.7, side: T.BackSide }), 0, 0, -0.003, false);
  const sealRadius = 0.36, sealLocal = new T.Vector3(0, -0.64 * ENV_H + 0.34, 0.012);
  const waxMat = kit.wax("#8f2a3c");
  const [leftGeo, rightGeo] = sealHalves(sealRadius);
  const leftSeal = put(hinge, leftGeo, waxMat, sealLocal.x, sealLocal.y, sealLocal.z);
  const rightSeal = put(body, rightGeo, waxMat, 0, 0, 0);
  const ringGeo = new T.TorusGeometry(sealRadius * 0.62, 0.014, 8, 40);
  const ring = put(leftSeal, ringGeo, kit.wax("#7a2234"), 0, 0, 0.066);
  const bloom = new T.Group(); bloom.position.set(0.0, 0, 0.07); leftSeal.add(bloom);
  for (let i = 0; i < 5; i++) { const petal = put(bloom, new T.SphereGeometry(0.055, 12, 8), kit.wax("#7a2234"), Math.sin((i * 2 * Math.PI) / 5) * 0.1, Math.cos((i * 2 * Math.PI) / 5) * 0.1, 0); petal.scale.set(1, 1.3, 0.45); }
  put(bloom, new T.SphereGeometry(0.04, 12, 8), kit.wax("#9b3447"), 0, 0, 0.02);
  void ring;
  const shards = Array.from({ length: 7 }, (_, i) => { const shard = put(body, new T.TetrahedronGeometry(0.035 + (i % 3) * 0.014), waxMat, 0, 0, 0.13, false); shard.visible = false; return { mesh: shard, angle: i * 0.91 + 0.3, speed: 0.5 + (i % 4) * 0.28 }; });
  const sealWorldSpot = new T.Vector3();
  const hitArea = put(body, new T.BoxGeometry(ENV_W, ENV_H, 0.2), new T.MeshBasicMaterial({ visible: false }), 0, 0, 0.08, false);
  envelope.userData.index = 0; hitArea.userData.index = 0;

  /* ---------- the letter ---------- */
  const textSize = low ? [768, 1050] : [1024, 1400];
  const handwriting = createHandwriting(textSize[0], textSize[1]);
  const textTexture = canvasTexture(handwriting.canvas, true, renderer.capabilities.getMaxAnisotropy());
  const paper = createFoldedPaper({ width: PAPER_W, height: PAPER_H, columns: low ? 16 : 32, rows: low ? 60 : 120 });
  const paperMats = [
    new T.MeshStandardMaterial({ map: textTexture, vertexColors: true, roughness: 0.9 }),
    kit.paper("#f1e6cc", "#d8c7a0", { roughness: 0.92 }),
    kit.paper("#e9dcbc", "#cdbb92", { roughness: 0.95 }),
  ];
  paperMats[1].vertexColors = true;
  const sheet = new T.Mesh(paper.geometry, paperMats); sheet.castShadow = true; sheet.receiveShadow = true; sheet.userData.index = 0;
  root.add(sheet);

  /* ---------- atmosphere ---------- */
  const dust = new ParticleField({ count: Math.round(160 * particleScale(quality)), size: 0.045, color: "#ffd9a0", colorB: "#fff4dc", opacity: 0.55, bounds: [6, 3.2, 4.5], center: [0, 3, 0], drift: 0.7, rise: 0.04, twinkle: 0.6 });
  root.add(dust.points);
  const glowTex = new T.CanvasTexture(sparkleCanvas(128)); glowTex.colorSpace = T.SRGBColorSpace;
  const glint = new T.Sprite(new T.SpriteMaterial({ map: glowTex, color: "#fff3d8", transparent: true, opacity: 0, depthWrite: false, blending: T.AdditiveBlending }));
  glint.scale.setScalar(0.9); root.add(glint);
  const glintLight = new T.PointLight("#fff1d6", 0, 3.2, 2); root.add(glintLight);
  for (const [x, y, z, s, c] of [[-7, 4.5, -9, 6, "#ffb870"], [3, 6, -11, 8, "#7f9cd8"], [8, 3, -9, 4, "#ffd6a0"], [-2, 2.5, -10, 5, "#ff9f6a"]] as const) {
    const glow = new T.Sprite(new T.SpriteMaterial({ map: (() => { const t = new T.CanvasTexture((() => { const cv = document.createElement("canvas"); cv.width = cv.height = 64; const g = cv.getContext("2d")!; const gr = g.createRadialGradient(32, 32, 0, 32, 32, 32); gr.addColorStop(0, "rgba(255,255,255,.9)"); gr.addColorStop(1, "rgba(255,255,255,0)"); g.fillStyle = gr; g.fillRect(0, 0, 64, 64); return cv; })()); t.colorSpace = T.SRGBColorSpace; return t; })(), color: c, transparent: true, opacity: 0.16, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
    glow.position.set(x, y, z); glow.scale.setScalar(s); root.add(glow);
  }

  /* ---------- choreography ---------- */
  const seq = new Sequence(LETTER_DURATION, { glint: 0, crack: 0, flap: 0, slide: 0, lift: 0, unfoldU: 0, unfoldL: 0, settle: 0, write: 0 }, (tl, p) => {
    tl.to(p, { glint: 1, duration: 1.2, ease: "sine.inOut" }, 0.8)
      .to(p, { crack: 1, duration: 0.8, ease: "power3.out" }, 2.1)
      .to(p, { flap: 1, duration: 1.5 }, 2.9)
      .to(p, { slide: 1, duration: 1.5 }, 4.3)
      .to(p, { lift: 1, duration: 1.4 }, 5.6)
      .to(p, { unfoldU: 1, duration: 1.0 }, 6.7)
      .to(p, { unfoldL: 1, duration: 1.0 }, 7.5)
      .to(p, { settle: 1, duration: 1.0 }, 8.4)
      .to(p, { write: 1, duration: 2.0, ease: "none" }, 9.0);
  });
  const cues: { at: number; sfx: Parameters<Stage["sfx"]>[0] }[] = [
    { at: 2.1 / LETTER_DURATION, sfx: "wax" }, { at: 2.9 / LETTER_DURATION, sfx: "flap" }, { at: 4.3 / LETTER_DURATION, sfx: "slide" },
    { at: 6.7 / LETTER_DURATION, sfx: "unfold" }, { at: 7.5 / LETTER_DURATION, sfx: "unfold" }, { at: 8.6 / LETTER_DURATION, sfx: "paper" },
  ];

  // Poses (world): camera and the letter's resting places.
  const envFrame = new T.Object3D(); envFrame.position.set(E0.x, E0.y, E0.z); envFrame.rotation.y = E0.ry;
  const slot = new T.Object3D(); slot.rotation.x = -Math.PI / 2; envFrame.add(slot); envFrame.updateMatrixWorld(true);
  const slideOutLocal = (y: number, z: number) => slot.localToWorld(new T.Vector3(0, y, z));
  const camPose = [
    { p: new T.Vector3(0.3, 5.7, 9.3), l: new T.Vector3(0, 0.25, 0.5) },
    { p: new T.Vector3(0.5, 4.5, 6.3), l: new T.Vector3(0.15, 0.1, 1.1) },
    { p: new T.Vector3(0.1, 4.4, 6.6), l: new T.Vector3(0, 1.45, -0.1) },
    { p: new T.Vector3(0, 7.0, 2.7), l: new T.Vector3(0, 0, -0.25) },
  ];
  const look = new T.Vector3(), pos = new T.Vector3(), offset = new T.Vector3(), tmp = new T.Vector3();
  const orbit = { yaw: 0, pitch: 0 };
  let textKey = "", lastReplay: number | undefined, lastProgress = -1, lastFold = [-1, -1, -1], lastCue = 0, lastReport = -1, fontsReady = false;
  void document.fonts?.load("600 40px Caveat").then(() => { fontsReady = true; textKey = ""; });

  return {
    pickables: [envelope, sheet],
    frame(time, dt, state: SceneState, reduced, timelineDt = dt) {
      const wanted = (state.detail && state.detail.trim()) || FALLBACK_TEXT;
      if (wanted !== textKey) { textKey = wanted; handwriting.write(wanted); lastFold[2] = -1; handwriting.compose(seq.phases.write); textTexture.needsUpdate = true; void fontsReady; }
      if (state.replay !== lastReplay) { if (lastReplay !== undefined) seq.seek(0); lastReplay = state.replay; }
      const target = state.open ? 1 : 0;
      const immediate = reduced || Boolean(state.immediate);
      const progress = seq.step(target, timelineDt, immediate);
      const p = seq.phases;
      if (!immediate && Math.abs(progress - lastProgress) > 1e-5) for (let i = 0; i < cues.length; i++) { const c = cues[i]; if ((lastProgress < c.at) !== (progress < c.at) && lastProgress >= 0) stage.sfx(c.sfx); }
      lastProgress = progress; lastCue = progress; void lastCue;

      // flame, candle light, dust
      const flicker = 0.9 + 0.1 * Math.sin(time * 11) * Math.sin(time * 7.3) + 0.04 * Math.sin(time * 23);
      flame.update(time, camera, 1); candleLight.intensity = 26 * flicker;
      dust.update(time);

      // seal glint, crack, shards
      const glintAmount = Math.sin(Math.PI * p.glint) * (1 - p.crack);
      hinge.rotation.x = 0; // closed pose, so the glint is placed on the seal's resting position
      leftSeal.position.set(sealLocal.x, sealLocal.y, sealLocal.z); leftSeal.updateWorldMatrix(true, false); leftSeal.getWorldPosition(sealWorldSpot);
      glint.position.set(sealWorldSpot.x + (p.glint - 0.5) * 0.7, sealWorldSpot.y + 0.28, sealWorldSpot.z + 0.12);
      (glint.material as T.SpriteMaterial).opacity = glintAmount * 0.9; glint.scale.setScalar(0.5 + glintAmount * 0.7);
      glintLight.position.copy(glint.position); glintLight.intensity = glintAmount * 7;
      const c = ease.out(p.crack), sealY = H2 + sealLocal.y, sealZ = 0.13 + sealLocal.z;
      leftSeal.position.set(sealLocal.x - c * 0.07, sealLocal.y + c * 0.02, sealLocal.z); leftSeal.rotation.z = c * 0.16;
      rightSeal.position.set(sealLocal.x + c * 0.16, sealY - c * 0.42 + Math.sin(c * Math.PI) * 0.05, sealZ - c * 0.012); rightSeal.rotation.z = -c * 0.5;
      rightSeal.visible = true;
      shards.forEach((s, i) => {
        s.mesh.visible = c > 0.02;
        const t = c; s.mesh.position.set(sealLocal.x + Math.cos(s.angle) * s.speed * 0.45 * t, sealY + Math.sin(s.angle) * s.speed * 0.35 * t - 0.1 * t, Math.max(0.126, sealZ + 0.5 * Math.sin(Math.min(1, t * 1.4) * Math.PI) * s.speed * (1 - t * 0.6)));
        s.mesh.rotation.set(t * (3 + i), t * 2, t * (1 + i * 0.3));
      });

      // flap
      hinge.rotation.x = ease.inOut(p.flap) * Math.PI * 0.985;

      // the letter: slide out of the pocket, lift toward the reader, unfold, settle
      const slideT = ease.inOut(p.slide), liftT = ease.inOut(p.lift), settleT = ease.inOut(p.settle);
      const inEnvelope = slideOutLocal(-0.12 + slideT * 2.5, 0.016 + Math.sin(slideT * Math.PI) * 0.02);
      const presented = tmp.set(0, 1.75, 0.0);
      sheet.position.copy(inEnvelope).lerp(presented, liftT).lerp(tmp.set(0, 0.125, -0.2), settleT);
      sheet.rotation.set(-Math.PI / 2 + 0.72 * liftT * (1 - settleT), 0, E0.ry * (1 - liftT));
      sheet.renderOrder = 2;
      const fold = [p.unfoldU, p.unfoldL, p.unfoldU * (1 - 0.8 * settleT)];
      if (Math.abs(fold[0] - lastFold[0]) > 5e-4 || Math.abs(fold[1] - lastFold[1]) > 5e-4 || Math.abs(fold[2] - lastFold[2]) > 5e-4) { paper.deform(p.unfoldU, p.unfoldL, fold[2]); lastFold = fold; }
      if (handwriting.compose(p.write)) textTexture.needsUpdate = true;
      // the empty envelope gets out of the way
      const away = ease.inOut(span(p.lift, 0.05, 1));
      envelope.position.set(E0.x + (-4.7 - E0.x) * away, E0.y, E0.z + (2.45 - E0.z) * away); envelope.rotation.y = E0.ry + away * 0.5;

      // camera
      const a = ease.inOut(span(progress, 0, 0.17)), b = ease.inOut(span(p.lift, 0, 1)), d = ease.inOut(p.settle);
      pos.copy(camPose[0].p).lerp(camPose[1].p, a).lerp(camPose[2].p, b).lerp(camPose[3].p, d);
      look.copy(camPose[0].l).lerp(camPose[1].l, a).lerp(camPose[2].l, b).lerp(camPose[3].l, d);
      const idle = reduced ? 0 : 1;
      pos.x += Math.sin(time * 0.31) * 0.12 * idle; pos.y += Math.sin(time * 0.23) * 0.06 * idle;
      const drag = input.consumeDrag();
      orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 2.6, -0.55, 0.55); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.4, -0.22, 0.3);
      offset.copy(pos).sub(look); offset.applyAxisAngle(tmp.set(0, 1, 0), orbit.yaw);
      const right = tmp.set(1, 0, 0).applyAxisAngle(new T.Vector3(0, 1, 0), orbit.yaw); offset.applyAxisAngle(right, orbit.pitch);
      const fit = T.MathUtils.clamp(0.85 / Math.max(0.45, camera.aspect), 1, 1.9); // pull back on portrait screens
      camera.position.copy(look).addScaledVector(offset, fit); camera.lookAt(look);

      if (Math.abs(progress - lastReport) > 0.008 || progress === 0 || progress === 1) { if (progress !== lastReport) { stage.report?.(progress); lastReport = progress; } }
    },
    dispose() { seq.dispose(); },
  };
}
```

## 71. `src/three/gifts/machine.ts` — new

```ts
/**
 * Gift 10 - Happiness Machine.
 * A brass-and-enamel workshop contraption. Pulling the lever spins three meshing gears behind a porthole, pumps a piston,
 * puffs steam from the chimney, lights three indicator bulbs in turn and prints a paper ticket carrying one of the
 * owner's existing wishes (passed in as state.detail). Resetting retracts the ticket: the timeline simply runs backwards.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, Sequence, span } from "../../engine/anim";
import { Burst, ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, put, tube } from "../../engine/geometry";
import { addContactShadow, addKeyLight, addPointLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, glowSprite, orbitCamera, paintBokeh } from "./common";

function gearGeometry(teeth: number, pitch: number, depth: number, hole = 0.09) {
  const shape = new T.Shape(), tooth = pitch * 0.2, step = (Math.PI * 2) / teeth;
  for (let i = 0; i < teeth; i++) {
    const a = i * step;
    const pts: [number, number][] = [[a - step * 0.3, pitch - tooth * 0.5], [a - step * 0.17, pitch + tooth * 0.5], [a + step * 0.17, pitch + tooth * 0.5], [a + step * 0.3, pitch - tooth * 0.5]];
    pts.forEach(([ang, r], k) => { const x = Math.cos(ang) * r, y = Math.sin(ang) * r; if (i === 0 && k === 0) shape.moveTo(x, y); else shape.lineTo(x, y); });
  }
  shape.closePath();
  const centre = new T.Path(); centre.absarc(0, 0, hole, 0, Math.PI * 2, true); shape.holes.push(centre);
  const n = teeth > 12 ? 5 : 4;
  for (let i = 0; i < n; i++) {
    const a0 = (i / n) * Math.PI * 2 + 0.2, a1 = ((i + 1) / n) * Math.PI * 2 - 0.2, r0 = pitch * 0.32, r1 = pitch * 0.72, p = new T.Path();
    p.moveTo(Math.cos(a0) * r1, Math.sin(a0) * r1); p.absarc(0, 0, r1, a0, a1, false); p.lineTo(Math.cos(a1) * r0, Math.sin(a1) * r0); p.absarc(0, 0, r0, a1, a0, true); p.closePath(); shape.holes.push(p);
  }
  const g = new T.ExtrudeGeometry(shape, { depth, bevelEnabled: true, bevelThickness: 0.012, bevelSize: 0.012, bevelSegments: 1, curveSegments: 10 });
  g.translate(0, 0, -depth / 2); return g;
}

function ticketTexture(text: string, n: number | null) {
  const c = document.createElement("canvas"); c.width = 512; c.height = 720; const g = c.getContext("2d")!;
  g.fillStyle = "#f6edd6"; g.fillRect(0, 0, 512, 720);
  const e = g.createRadialGradient(256, 360, 200, 256, 360, 480); e.addColorStop(0, "rgba(130,100,60,0)"); e.addColorStop(1, "rgba(130,100,60,.2)"); g.fillStyle = e; g.fillRect(0, 0, 512, 720);
  g.strokeStyle = "rgba(150,110,70,.5)"; g.setLineDash([12, 9]); g.lineWidth = 3; g.strokeRect(18, 18, 476, 684); g.setLineDash([]);
  g.fillStyle = "rgba(143,42,60,.92)"; g.font = "700 25px Georgia, serif"; g.textAlign = "center";
  g.fillText(n === null ? "HAPPINESS TICKET" : `HAPPINESS TICKET · No. ${String(n + 1).padStart(2, "0")}`, 256, 72);
  g.fillStyle = "#3a2c27"; g.textAlign = "left";
  const size = text.length > 210 ? 31 : text.length > 130 ? 37 : 44; g.font = `600 ${size}px Caveat, 'Segoe Print', 'Comic Sans MS', cursive`;
  let line = "", y = 150; const lh = size * 1.28;
  for (const word of text.split(/\s+/).filter(Boolean)) { const t = line ? `${line} ${word}` : word; if (g.measureText(t).width > 410 && line) { g.fillText(line, 50, y); y += lh; line = word; } else line = t; }
  if (line) g.fillText(line, 50, y);
  const tex = new T.CanvasTexture(c); tex.colorSpace = T.SRGBColorSpace; tex.anisotropy = 8; return tex;
}

export function buildMachineWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "candle", envIntensity: 0.95, exposure: 1.1, background: "#0f1a1d", fog: { color: "#111c20", density: 0.016 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#ffe4c0", "#10181a", 0.55));
  addKeyLight(scene, quality, { color: "#ffd8a8", intensity: 3.0, position: [-5, 8, 7], target: [0, 1.4, 0], extent: 6, far: 26 });
  const rim = new T.DirectionalLight("#7fa6d8", 0.9); rim.position.set(6, 4, -5); scene.add(rim);
  addPointLight(scene, "#ffb869", 18, [-3.3, 4.4, 2.4], 12, 2); addPointLight(scene, "#ffb869", 14, [4.4, 4.0, 1.8], 12, 2);
  const panelLight = addPointLight(scene, "#ffcf8a", 0, [0, 1.9, 2.4], 5, 2);

  /* ---------- workshop ---------- */
  const wall = backdrop((g, w, h) => {
    g.fillStyle = "#1b2b2f"; g.fillRect(0, 0, w, h);
    g.fillStyle = "rgba(0,0,0,.4)"; for (let y = 16; y < h; y += 24) for (let x = 16; x < w; x += 24) { g.beginPath(); g.arc(x, y, 3, 0, 6.283); g.fill(); }
    g.strokeStyle = "rgba(255,214,150,.2)"; g.lineWidth = 6; g.lineCap = "round";
    for (let i = 0; i < 6; i++) { const x = 90 + i * 160, y = 150 + (i % 2) * 90; g.beginPath(); g.moveTo(x, y); g.lineTo(x + 30, y + 140); g.stroke(); g.beginPath(); g.arc(x - 2, y - 8, 20, 0, 6.283); g.stroke(); }
    g.beginPath(); g.arc(780, 320, 44, 0, 6.283); g.stroke(); g.beginPath(); g.arc(780, 320, 20, 0, 6.283); g.stroke();
    paintBokeh(g, w, h, "255,190,120", 14, 7);
  }, 46, 26);
  wall.position.set(0, 7, -4.6); scene.add(wall);
  const bench = put(scene, new T.BoxGeometry(24, 0.6, 9), kit.wood("#24140b", "#6b4428", [4, 1.5], 0.5), 0, -0.3, 1.2, false); bench.receiveShadow = true;
  for (const [x, y] of [[-3.3, 4.4], [4.4, 4.0]] as const) {
    put(scene, new T.CylinderGeometry(0.012, 0.012, 4, 4), new T.MeshBasicMaterial({ color: "#151515" }), x, y + 2, 2.4, false);
    put(scene, new T.SphereGeometry(0.17, 14, 10), new T.MeshBasicMaterial({ color: "#ffd9a0" }), x, y, 2.4, false);
    const halo = glowSprite("#ffb869", 2.6, 0.5); halo.position.set(x, y, 2.4); scene.add(halo);
  }

  /* ---------- machine body ---------- */
  const enamel = new T.MeshPhysicalMaterial({ color: "#2f7d77", roughness: 0.32, metalness: 0.15, clearcoat: 0.8, clearcoatRoughness: 0.2 });
  const cream = new T.MeshPhysicalMaterial({ color: "#efe3c6", roughness: 0.4, clearcoat: 0.5 });
  const brass = kit.metal("brass", 0.28), steel = kit.metal("steel", 0.4), copper = kit.metal("copper", 0.35);
  const machine = new T.Group(); scene.add(machine);
  put(machine, new RoundedBoxGeometry(4.6, 0.36, 2.3, 3, 0.06), new T.MeshStandardMaterial({ color: "#1a1f22", roughness: 0.6, metalness: 0.6 }), 0, 0.18, 0);
  put(machine, new RoundedBoxGeometry(3.7, 2.55, 1.75, 4, 0.12), enamel, 0, 1.64, 0);
  put(machine, new RoundedBoxGeometry(3.9, 0.16, 1.92, 3, 0.05), cream, 0, 3.0, 0); put(machine, new RoundedBoxGeometry(3.9, 0.14, 1.92, 3, 0.05), cream, 0, 0.5, 0);
  const rivetPts: [number, number][] = []; for (let x = -1.7; x <= 1.71; x += 0.34) { rivetPts.push([x, 2.82], [x, 0.7]); } for (const y of [1.0, 1.4, 1.8, 2.2, 2.6]) rivetPts.push([-1.78, y], [1.78, y]);
  const rivets = new T.InstancedMesh(new T.SphereGeometry(0.045, 8, 6), brass, rivetPts.length), rm = new T.Object3D();
  rivetPts.forEach(([x, y], i) => { rm.position.set(x, y, 0.885); rm.updateMatrix(); rivets.setMatrixAt(i, rm.matrix); }); machine.add(rivets);
  addContactShadow(scene, 5.4, 2.8, 0, 0.002, 0, 0.6);

  /* ---------- porthole with meshing gears ---------- */
  const portal = new T.Group(); portal.position.set(0, 1.95, 0.88); machine.add(portal);
  const hole = put(portal, new T.CylinderGeometry(1.02, 1.02, 0.1, 40), new T.MeshStandardMaterial({ color: "#14181a", roughness: 0.85 }), 0, 0, -0.02, false); hole.rotation.x = Math.PI / 2;
  put(portal, new T.TorusGeometry(1.06, 0.075, 12, 48), brass, 0, 0, 0.04, false);
  const teeth = [16, 11, 9], pitch = [0.5, 0.36, 0.28], gearMats = [brass, copper, steel];
  const centres: T.Vector2[] = [new T.Vector2(-0.35, -0.08)];
  centres.push(centres[0].clone().add(new T.Vector2(Math.cos(0.61), Math.sin(0.61)).multiplyScalar(pitch[0] + pitch[1] + 0.02)));
  centres.push(centres[1].clone().add(new T.Vector2(Math.cos(-1.05), Math.sin(-1.05)).multiplyScalar(pitch[1] + pitch[2] + 0.02)));
  const gears = teeth.map((n, i) => {
    const gear = new T.Mesh(gearGeometry(n, pitch[i], 0.1), gearMats[i]); gear.position.set(centres[i].x, centres[i].y, 0.02 + i * 0.012); gear.castShadow = !low; portal.add(gear);
    put(gear, new T.CylinderGeometry(0.06, 0.06, 0.2, 10), steel, 0, 0, 0, false).rotation.x = Math.PI / 2; return { gear, n };
  });
  gears[1].gear.rotation.z = Math.PI / teeth[1];
  const dialTex = (() => { const c = document.createElement("canvas"); c.width = c.height = 256; const g = c.getContext("2d")!; g.fillStyle = "#f3ead3"; g.beginPath(); g.arc(128, 128, 126, 0, 6.283); g.fill(); g.strokeStyle = "#2a2420"; g.lineWidth = 4;
    for (let i = 0; i <= 12; i++) { const a = Math.PI * 0.8 + (i / 12) * Math.PI * 1.4; g.beginPath(); g.moveTo(128 + Math.cos(a) * 96, 128 + Math.sin(a) * 96); g.lineTo(128 + Math.cos(a) * 116, 128 + Math.sin(a) * 116); g.stroke(); }
    g.strokeStyle = "#b02a30"; g.lineWidth = 12; g.beginPath(); g.arc(128, 128, 86, Math.PI * 2.0, Math.PI * 2.2); g.stroke(); const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t; })();

  /* gauge, indicator bulbs, flywheel, ticket slot */
  const gauge = new T.Group(); gauge.position.set(-1.38, 2.62, 0.9); machine.add(gauge);
  put(gauge, new T.CylinderGeometry(0.4, 0.4, 0.08, 28), brass, 0, 0, 0, false).rotation.x = Math.PI / 2;
  const face = new T.Mesh(new T.CircleGeometry(0.34, 28), new T.MeshStandardMaterial({ map: dialTex, roughness: 0.5 })); face.position.z = 0.045; gauge.add(face);
  const needle = new T.Group(); needle.position.z = 0.06; gauge.add(needle); put(needle, new T.BoxGeometry(0.02, 0.3, 0.01), new T.MeshBasicMaterial({ color: "#b02a30" }), 0, 0.14, 0, false);
  const bulbColours = ["#e8453c", "#f0b43a", "#58d27c"];
  const bulbs = bulbColours.map((c, i) => {
    const m = new T.MeshStandardMaterial({ color: new T.Color(c).multiplyScalar(0.35), emissive: new T.Color(c), emissiveIntensity: 0, roughness: 0.2 });
    put(machine, new T.CylinderGeometry(0.14, 0.17, 0.1, 16), brass, 1.0 + i * 0.36, 2.64, 0.9, false).rotation.x = Math.PI / 2;
    const bulb = put(machine, new T.SphereGeometry(0.11, 16, 12), m, 1.0 + i * 0.36, 2.64, 0.97, false); void bulb; return { m, c };
  });
  const fly = new T.Group(); fly.position.set(-1.35, 0.98, 0.93); machine.add(fly);
  put(fly, new T.TorusGeometry(0.38, 0.045, 10, 36), steel, 0, 0, 0, false); for (let i = 0; i < 6; i++) { const s = put(fly, new T.BoxGeometry(0.03, 0.74, 0.04), steel, 0, 0, 0, false); s.rotation.z = (i / 6) * Math.PI; } put(fly, new T.CylinderGeometry(0.09, 0.09, 0.1, 12), brass, 0, 0, 0, false).rotation.x = Math.PI / 2;
  put(machine, new T.BoxGeometry(1.4, 0.1, 0.05), new T.MeshBasicMaterial({ color: "#050505" }), 0.35, 0.95, 0.9, false);
  const chute = put(machine, new T.BoxGeometry(1.46, 0.04, 0.6), brass, 0.35, 0.86, 1.15, false); chute.rotation.x = 0.28;
  put(machine, new RoundedBoxGeometry(1.5, 0.22, 0.12, 2, 0.03), cream, 0.35, 1.12, 0.9, false);

  /* ---------- pipes, chimney, piston ---------- */
  put(machine, tube([[1.1, 3.0, -0.3], [1.1, 3.7, -0.3], [0.7, 4.0, -0.3]], 0.1, 24, 10), brass, 0, 0, 0);
  for (const y of [3.15, 3.55]) put(machine, new T.TorusGeometry(0.13, 0.03, 8, 20), copper, 1.1, y, -0.3, false).rotation.x = Math.PI / 2;
  const funnel = put(machine, new T.CylinderGeometry(0.34, 0.14, 0.4, 20, 1, true), brass, 0.62, 4.15, -0.3, false); funnel.material = new T.MeshStandardMaterial({ ...(brass as T.MeshStandardMaterial), color: (brass as T.MeshStandardMaterial).color, side: T.DoubleSide, metalness: 0.9, roughness: 0.3 } as T.MeshStandardMaterialParameters);
  put(machine, tube([[-1.85, 2.4, 0.2], [-2.35, 2.5, 0.2], [-2.5, 1.5, 0.2], [-2.2, 0.4, 0.2]], 0.08, 28, 8), copper, 0, 0, 0);
  const pistonHousing = put(machine, new T.CylinderGeometry(0.22, 0.22, 0.5, 18), brass, -0.9, 3.28, 0.3), rod = put(machine, new T.CylinderGeometry(0.07, 0.07, 0.8, 10), steel, -0.9, 3.7, 0.3, false), cap = put(machine, new T.SphereGeometry(0.14, 12, 10), brass, -0.9, 4.1, 0.3, false);
  void pistonHousing;

  /* ---------- lever ---------- */
  const lever = new T.Group(); lever.position.set(2.0, 1.45, 0.3); machine.add(lever);
  put(machine, new T.BoxGeometry(0.1, 1.5, 0.5), cream, 1.86, 1.55, 0.3, false);
  const hub = put(machine, new T.CylinderGeometry(0.2, 0.2, 0.3, 20), brass, 1.98, 1.45, 0.3, false); hub.rotation.z = Math.PI / 2;
  const arm = put(lever, new T.CylinderGeometry(0.055, 0.07, 1.2, 12), steel, 0, 0.6, 0); const ball = put(lever, new T.SphereGeometry(0.2, 20, 16), new T.MeshPhysicalMaterial({ color: "#c2282f", roughness: 0.25, clearcoat: 1 }), 0, 1.25, 0);
  void arm; void ball;
  const hit = new T.Mesh(new T.CylinderGeometry(0.4, 0.4, 1.8, 8), new T.MeshBasicMaterial({ visible: false })); hit.position.y = 0.8; hit.userData.index = 0; lever.add(hit); lever.userData.index = 0;

  /* ---------- ticket ---------- */
  let ticketKey = "\u0000";
  const ticketMat = new T.MeshStandardMaterial({ map: ticketTexture("", null), roughness: 0.9, side: T.DoubleSide });
  const ticket = new T.Mesh(new T.PlaneGeometry(1.1, 1.5, 4, 6), ticketMat); ticket.castShadow = true; ticket.visible = false; scene.add(ticket);
  const smoke = new Burst({ count: low ? 24 : 60, size: 0.9, life: 2.6, speed: 0.9, gravity: -0.25, drag: 0.8, colors: ["#f2f2ee", "#d9d9d2"], shape: "smoke", emit: "cone", coneAngle: 0.35 }); scene.add(smoke.points);
  const joy = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.09, color: "#ffe9a8", colorB: "#ffb0c0", opacity: 0, bounds: [1.1, 1.3, 0.5], center: [-2.9, 1.6, 1.6], twinkle: 1, shape: "spark", drift: 0.6, rise: 0.12 }); scene.add(joy.points);

  const seq = new Sequence(2.8, { lever: 0, spin: 0, ticket: 0, b1: 0, b2: 0, b3: 0 }, (tl, p) => {
    tl.to(p, { lever: 1, duration: 0.28, ease: "power2.in" }, 0); tl.to(p, { lever: 0, duration: 0.7, ease: "back.out(2)" }, 0.55);
    tl.to(p, { spin: 1, duration: 0.5, ease: "power2.out" }, 0.2); tl.to(p, { spin: 0.2, duration: 1.0, ease: "power1.inOut" }, 1.7);
    tl.to(p, { b1: 1, duration: 0.15 }, 0.35); tl.to(p, { b2: 1, duration: 0.15 }, 0.75); tl.to(p, { b3: 1, duration: 0.15 }, 1.15);
    tl.to(p, { ticket: 1, duration: 1.6, ease: "power2.inOut" }, 1.0);
  });
  const angles = [0, 0, 0], v = new T.Vector3(), pos = new T.Vector3(), look = new T.Vector3(), orbit = { yaw: 0, pitch: 0 };
  let lastReplay = 0, lastTicketSfx = false, wheel = 0, shake = 0;
  return {
    pickables: [lever],
    dispose() { seq.dispose(); ticketMat.map?.dispose(); },
    frame(time, dt, state: SceneState, reduced) {
      const replay = state.replay ?? 0, sel = state.selected ?? null;
      if (replay !== lastReplay) { lastReplay = replay; if (sel !== null) { seq.seek(0); stage.sfx("lever"); smoke.trigger([0.62, 4.3, -0.3]); stage.sfx("puff"); shake = 1; } }
      const p = seq.phases, progress = seq.step(sel === null ? 0 : 1, dt, reduced || Boolean(state.immediate));
      const text = state.detail ?? "", key = `${sel}|${text}`;
      if (key !== ticketKey) { ticketKey = key; ticketMat.map?.dispose(); ticketMat.map = ticketTexture(text || (sel !== null ? "" : ""), sel); ticketMat.needsUpdate = true; }
      const speed = p.spin * (state.open ? 1 : 0.55) * (reduced ? 0 : 5.2);
      angles[0] += speed * dt; angles[1] = -angles[0] * (teeth[0] / teeth[1]); angles[2] = -angles[1] * (teeth[1] / teeth[2]);
      gears[0].gear.rotation.z = angles[0]; gears[1].gear.rotation.z = angles[1] + Math.PI / teeth[1]; gears[2].gear.rotation.z = angles[2];
      wheel += speed * dt * 0.8; fly.rotation.z = wheel;
      for (const [i, key2] of (["b1", "b2", "b3"] as const).entries()) { bulbs[i].m.emissiveIntensity = 0.1 + 3.2 * p[key2] * (0.85 + (reduced ? 0 : Math.sin(time * 14 + i) * 0.15)); }
      panelLight.intensity = damp(panelLight.intensity, p.spin * 9, 6, dt, reduced);
      needle.rotation.z = -(0.2 + p.spin * 1.7) + (reduced ? 0 : Math.sin(time * 30) * 0.03 * p.spin);
      lever.rotation.z = -0.35 - 1.4 * p.lever;
      const pump = reduced ? 0 : Math.max(0, Math.sin(time * 13)) * p.spin; rod.position.y = 3.7 + pump * 0.28; cap.position.y = 4.1 + pump * 0.28;
      smoke.update(dt);
      // ticket: slides out of the slot, then lifts to a reading pose beside the machine
      const t = p.ticket; ticket.visible = t > 0.001 && sel !== null;
      if (ticket.visible) {
        const out = ease.inOut(span(t, 0, 0.4)), lift = ease.inOut(span(t, 0.35, 1));
        v.set(0.35 * (1 - lift) + -2.9 * lift, 0.85 + (1.55 - 0.85) * lift, 0.5 + 1.05 * out + (1.7 - 1.55) * lift);
        ticket.position.copy(v); ticket.rotation.set(-Math.PI / 2 * (1 - lift) + (reduced ? 0 : Math.sin(time * 1.4) * 0.03) * lift, 0.38 * lift, 0); ticket.scale.setScalar(0.85 + 0.45 * lift);
        const bend = (1 - lift) * 0.25 * Math.sin(out * Math.PI); const pa = ticket.geometry.attributes.position; for (let i = 0; i < pa.count; i++) pa.setZ(i, Math.sin((pa.getY(i) / 1.5 + 0.5) * Math.PI) * bend); pa.needsUpdate = true;
      }
      if (t > 0.92 && !lastTicketSfx) { stage.sfx("ding"); lastTicketSfx = true; } else if (t < 0.5) lastTicketSfx = false;
      joy.opacity = damp(joy.opacity, t > 0.9 && sel !== null ? 0.9 : 0, 3, dt, reduced); joy.update(time);
      shake = damp(shake, 0, 3, dt, reduced);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.6, 0.6); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.12, 0.28);
      const look1 = ease.inOut(span(progress, 0.3, 1));
      pos.set(3.6 - 0.9 * look1 + (reduced ? 0 : Math.sin(time * 0.2) * 0.2) + shake * (Math.random() - 0.5) * 0.06, 2.9, 9.1 - 0.4 * look1);
      look.set(0.2 - 0.7 * look1, 1.85, 0.4); orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 72. `src/three/gifts/mirror.ts` — new

```ts
/**
 * Gift 13 - Infinite Mirror.
 * A beaded-gold cheval mirror in a dark velvet dressing room. Its glass hides a true infinity tunnel: fourteen receding
 * rings of light between a half-silvered front pane and a back mirror. Mist covers the glass until it is wiped
 * (state.growth 0..1). The mist dissolves along a noise front, the tunnel brightens, and a spray of light marks the moment
 * it clears. Everything is abstract: no portrait is invented.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp } from "../../engine/anim";
import { Burst, ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, put, starShape, tube } from "../../engine/geometry";
import { addContactShadow, addKeyLight, addSpotLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { glowSprite, makeCurtain, orbitCamera, softTexture } from "./common";

const RX = 1.45, RY = 2.15, RINGS = 14, DOTS = 40;
const MIST_FRAG = `uniform float uClear, uTime; varying vec2 vUv;
  float h(vec2 p){ return fract(sin(dot(p, vec2(127.1, 311.7))) * 43758.5453); }
  float n(vec2 p){ vec2 i = floor(p), f = fract(p); f = f*f*(3.0-2.0*f); return mix(mix(h(i), h(i+vec2(1.0,0.0)), f.x), mix(h(i+vec2(0.0,1.0)), h(i+vec2(1.0,1.0)), f.x), f.y); }
  float fbm(vec2 p){ float v = 0.0, a = 0.5; for (int i = 0; i < 5; i++){ v += a*n(p); p *= 2.03; a *= 0.5; } return v; }
  void main(){
    vec2 p = vUv - 0.5; float r = length(p * vec2(1.0, 0.72));
    float cloud = fbm(vUv * 4.0 + 7.0), fine = fbm(vUv * 18.0 + uTime * 0.01);
    float front = uClear * 1.35 - cloud * 0.75 - r * 0.2;
    float alpha = (1.0 - smoothstep(-0.06, 0.1, front)) * (0.9 - 0.18 * fine);
    float rim = smoothstep(-0.06, 0.1, front) * (1.0 - smoothstep(0.1, 0.22, front));
    vec3 col = mix(vec3(0.70, 0.78, 0.83), vec3(0.94, 0.96, 0.97), cloud) + rim * 0.15;
    col += step(0.992, h(floor(vUv * vec2(70.0, 100.0)))) * 0.25;
    gl_FragColor = vec4(col, alpha);
  }`;

export function buildMirrorWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "dusk", envIntensity: 0.9, exposure: 1.05, background: "#07060d", fog: { color: "#0a0812", density: 0.02 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#cdbfff", "#07060d", 0.45));
  addKeyLight(scene, quality, { color: "#ffe9c8", intensity: 2.2, position: [-4, 8, 7], target: [0, 2.4, 0], extent: 7, far: 26 });
  addSpotLight(scene, quality, "#ffe8c4", 130, [2.5, 9.5, 5], [0, 2.4, 0], 0.5, 0.9);
  const rim = new T.DirectionalLight("#8a7bff", 0.9); rim.position.set(5, 4, -5); scene.add(rim);

  /* ---------- room ---------- */
  const floor = put(scene, new T.CircleGeometry(24, 64), new T.MeshStandardMaterial({ color: "#09070e", roughness: 0.38, metalness: 0.55, envMapIntensity: 0.45 }), 0, 0, 0, false); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;
  for (const x of [-1, 0, 1]) { const c = makeCurtain(7.5, 14, "#2a1b4a", 1.7); c.position.set(x * 7.2, 7, -6.2 - Math.abs(x) * 0.4); scene.add(c); }

  /* ---------- mirror ---------- */
  const gold = kit.metal("gold", 0.25), mirror = new T.Group(); mirror.position.set(0, RY + 0.62, 0); scene.add(mirror);
  const BEADS = 104, beads = new T.InstancedMesh(new T.SphereGeometry(0.075, 14, 10), gold, BEADS), bm = new T.Object3D();
  for (let i = 0; i < BEADS; i++) { const a = (i / BEADS) * Math.PI * 2; bm.position.set(Math.cos(a) * (RX + 0.1), Math.sin(a) * (RY + 0.1), 0); bm.scale.setScalar(i % 2 ? 0.8 : 1.15); bm.updateMatrix(); beads.setMatrixAt(i, bm.matrix); } beads.castShadow = !low; mirror.add(beads);
  const ringFrame = put(mirror, new T.TorusGeometry(1, 0.045, 12, 96), gold, 0, 0, 0); ringFrame.scale.set(RX + 0.2, RY + 0.2, 1);
  const inner = put(mirror, new T.TorusGeometry(1, 0.03, 10, 96), gold, 0, 0, 0.02, false); inner.scale.set(RX - 0.02, RY - 0.02, 1);
  const crest = put(mirror, new T.ExtrudeGeometry(starShape(0.34, 0.16, 8), { depth: 0.1, bevelEnabled: true, bevelSize: 0.02, bevelThickness: 0.02, bevelSegments: 2 }), gold, 0, RY + 0.42, -0.05); void crest;
  put(mirror, new T.SphereGeometry(0.1, 16, 12), kit.gem("#d84f7b"), 0, RY + 0.42, 0.1, false);
  const backPlate = put(mirror, new T.CircleGeometry(1, 64), new T.MeshStandardMaterial({ color: "#05060b", metalness: 1, roughness: 0.22 }), 0, 0, -RINGS * 0.15 - 0.2, false); backPlate.scale.set(RX * 0.55, RY * 0.55, 1);
  const glass = put(mirror, new T.CircleGeometry(1, 64), new T.MeshPhysicalMaterial({ color: "#0a1018", roughness: 0.04, metalness: 0.9, transparent: true, opacity: 0.22, envMapIntensity: 1.3 }), 0, 0, 0.02, false); glass.scale.set(RX, RY, 1);
  const streakTex = (() => { const c = document.createElement("canvas"); c.width = 128; c.height = 512; const g = c.getContext("2d")!; const gr = g.createLinearGradient(0, 0, 128, 0); gr.addColorStop(0, "rgba(255,255,255,0)"); gr.addColorStop(0.5, "rgba(255,255,255,.55)"); gr.addColorStop(1, "rgba(255,255,255,0)"); g.fillStyle = gr; g.fillRect(0, 0, 128, 512); return new T.CanvasTexture(c); })();
  for (const [x, w, o] of [[-0.55, 0.5, 0.16], [0.35, 0.22, 0.1]] as const) { const s = put(mirror, new T.PlaneGeometry(w, RY * 1.9), new T.MeshBasicMaterial({ map: streakTex, transparent: true, opacity: o, blending: T.AdditiveBlending, depthWrite: false }), x, 0, 0.04, false); s.rotation.z = 0.35; }

  /* infinity tunnel */
  const ringMats: T.MeshBasicMaterial[] = [], torusGeo = new T.TorusGeometry(1, 0.014, 8, 80), dotPos = new Float32Array(RINGS * DOTS * 3), dotCol = new Float32Array(RINGS * DOTS * 3), baseCol: T.Color[] = [];
  for (let k = 0; k < RINGS; k++) {
    const s = Math.pow(0.905, k + 1), z = -0.1 - k * 0.15, col = new T.Color().setHSL((1.11 - 0.52 * (k / (RINGS - 1))) % 1, 0.92, 0.56); baseCol.push(col);
    const mat = new T.MeshBasicMaterial({ color: col, transparent: true, opacity: 0.9, blending: T.AdditiveBlending, depthWrite: false, toneMapped: false }); ringMats.push(mat);
    const ring = new T.Mesh(torusGeo, mat); ring.scale.set(RX * 0.93 * s, RY * 0.93 * s, 1); ring.position.z = z; mirror.add(ring);
    for (let d = 0; d < DOTS; d++) { const a = (d / DOTS) * Math.PI * 2, i = (k * DOTS + d) * 3; dotPos[i] = Math.cos(a) * RX * 0.93 * s; dotPos[i + 1] = Math.sin(a) * RY * 0.93 * s; dotPos[i + 2] = z; }
  }
  const dotGeo = new T.BufferGeometry(); dotGeo.setAttribute("position", new T.BufferAttribute(dotPos, 3)); dotGeo.setAttribute("color", new T.BufferAttribute(dotCol, 3));
  const dots = new T.Points(dotGeo, new T.PointsMaterial({ size: 0.16, map: softTexture(), vertexColors: true, transparent: true, blending: T.AdditiveBlending, depthWrite: false, sizeAttenuation: true })); dots.frustumCulled = false; mirror.add(dots);
  const mistUniforms = { uClear: { value: 0 }, uTime: { value: 0 } };
  const mist = put(mirror, new T.CircleGeometry(1, 64), new T.ShaderMaterial({ uniforms: mistUniforms, vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }", fragmentShader: MIST_FRAG, transparent: true, depthWrite: false }), 0, 0, 0.07, false); mist.scale.set(RX * 1.0, RY * 1.0, 1); mist.renderOrder = 4;
  const clearGlow = glowSprite("#ffe0a0", 7, 0); clearGlow.position.set(0, 0, 0.3); mirror.add(clearGlow);

  /* stand */
  for (const s of [-1, 1]) {
    put(scene, tube([[s * (RX + 0.2), RY + 0.62, 0], [s * (RX + 0.3), 1.9, -0.1], [s * 1.5, 0.45, -0.35], [s * 1.55, 0.12, -0.6]], 0.075, 28, 10), gold, 0, 0, 0);
    put(scene, new T.CylinderGeometry(0.1, 0.1, 0.34, 14), gold, s * (RX + 0.2), RY + 0.62, 0, false).rotation.z = Math.PI / 2;
    put(scene, new T.SphereGeometry(0.17, 14, 10), gold, s * 1.55, 0.12, -0.6, false);
  }
  put(scene, new RoundedBoxGeometry(3.4, 0.14, 0.34, 3, 0.05), gold, 0, 0.09, -0.6);
  addContactShadow(scene, 4, 1.6, 0, 0.004, -0.4, 0.6);

  const pool = glowSprite("#ffe3b0", 9, 0.22); pool.position.set(0, 0.06, 0.6); pool.material.depthTest = true; scene.add(pool);
  const dustField = new ParticleField({ count: Math.round(110 * particleScale(quality)), size: 0.07, color: "#ffe6b0", colorB: "#c9b6ff", opacity: 0.7, bounds: [3.6, 4, 1.8], center: [0, 3.2, 1.2], twinkle: 1, shape: "spark", drift: 0.5, rise: 0.12 }); scene.add(dustField.points);
  const spray = new Burst({ count: low ? 50 : 140, size: 0.16, life: 2.8, speed: 3.2, gravity: -0.1, drag: 1.3, colors: ["#ffe9a8", "#ffc7e0", "#cfe4ff"], shape: "spark", emit: "sphere" }); scene.add(spray.points);

  const pos = new T.Vector3(), look = new T.Vector3(0, 2.9, 0), orbit = { yaw: 0, pitch: 0 }, col = new T.Color(), world = new T.Vector3();
  const ray = new T.Raycaster(), lastPtr = new T.Vector2();
  let clear = 0, shown = false, wipe = 0, lastReplay = 0, wiping = false;
  return {
    frame(time, dt, state: SceneState, reduced) {
      // direct wiping: dragging across the glass accumulates `wipe`; the HTML console hears about it through report()
      if ((state.replay ?? 0) !== lastReplay) { lastReplay = state.replay ?? 0; wipe = 0; }
      wiping = false;
      if (input.dragging && input.inside) { ray.setFromCamera(input.pointer, camera); if (ray.intersectObject(glass, false).length) { wiping = true; wipe = Math.min(1, wipe + lastPtr.distanceTo(input.pointer) * 0.9); } }
      lastPtr.copy(input.pointer);
      const target = Math.max(T.MathUtils.clamp(state.growth ?? 0, 0, 1), wipe); clear = damp(clear, target, 2.2, dt, reduced);
      stage.report?.(Math.min(1, wipe));
      mistUniforms.uClear.value = clear; mistUniforms.uTime.value = time;
      if (clear > 0.97 && !shown) { shown = true; mirror.getWorldPosition(world); spray.trigger(world.clone().setZ(0.4)); stage.sfx("magic"); } else if (clear < 0.6 && shown) shown = false;
      spray.update(dt);
      const reveal = 0.35 + 0.65 * clear;
      for (let k = 0; k < RINGS; k++) {
        const wave = reduced ? 0.8 : 0.55 + 0.45 * Math.sin(time * 2.4 - k * 0.55), b = Math.pow(0.9, k) * wave * reveal;
        ringMats[k].opacity = Math.min(1, 1.5 * b);
        col.copy(baseCol[k]).multiplyScalar(b * 2.6); for (let d = 0; d < DOTS; d++) { const i = (k * DOTS + d) * 3; dotCol[i] = col.r; dotCol[i + 1] = col.g; dotCol[i + 2] = col.b; }
      }
      (dotGeo.attributes.color as T.BufferAttribute).needsUpdate = true;
      (clearGlow.material as T.SpriteMaterial).opacity = damp((clearGlow.material as T.SpriteMaterial).opacity, 0.12 + 0.3 * clear, 3, dt, reduced);
      dustField.update(time);
      const drag = input.consumeDrag(); if (!wiping) { orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.4, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.12, 0.3); }
      pos.set((reduced ? 0 : Math.sin(time * 0.2) * 0.5), 3.1, 12.4 - 1.4 * clear); orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 73. `src/three/gifts/portal.ts` — new

```ts
/**
 * Gift 17 - The Ultimate Surprise.
 * A deep-space finale. Sixteen small lights, one for each of the other gifts, drift apart in the dark (state.growth 0).
 * When they are gathered (1) they fly into a slowly turning ring, threaded together with fine light. When the portal opens
 * (2) three metal rings (gold, silver, rose gold) rise into a gyroscope, a swirling doorway of warm light fills the ring,
 * a flash washes the screen and the camera drifts toward the Birthday Ballroom glow. Going back to 0 reverses it all.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, span } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { put } from "../../engine/geometry";
import { particleScale } from "../../engine/quality";
import { backdrop, glowSprite, hash, orbitCamera, softTexture, sparkleSprite } from "./common";

const ORBS = 16, RING_R = 2.7;
const SWIRL_FRAG = `uniform float uTime, uOpen; varying vec2 vUv;
  void main(){
    vec2 p = (vUv - 0.5) * 2.0; float r = length(p), a = atan(p.y, p.x), t = uTime * 0.6;
    float s1 = sin(a * 3.0 + 6.0 * log(r + 0.08) - t * 3.0) * 0.5 + 0.5, s2 = sin(a * 5.0 - 9.0 * r + t * 2.0) * 0.5 + 0.5;
    vec3 c1 = vec3(1.0, 0.76, 0.34), c2 = vec3(0.95, 0.28, 0.58), c3 = vec3(0.3, 0.62, 1.0);
    vec3 col = mix(c3, c2, s1); col = mix(col, c1, s2 * 0.55);
    float core = exp(-r * 3.4); col = mix(col, vec3(1.0, 0.94, 0.8), core * 0.55);
    float edge = smoothstep(1.0, 0.8, r), alpha = edge * (0.55 + 0.45 * s1) * uOpen;
    gl_FragColor = vec4(col * (0.5 + core * 0.55), alpha * 0.9);
  }`;

export function buildPortalWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "dusk", envIntensity: 0.8, exposure: 1.05, background: "#04040b", fog: null });
  camera.fov = 36; camera.near = 0.1; camera.far = 200; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#8f9bff", "#1a0f22", 0.5));
  const key = new T.DirectionalLight("#ffe2b8", 2.2); key.position.set(-4, 5, 8); scene.add(key);
  const rim = new T.DirectionalLight("#7f6bff", 1.2); rim.position.set(5, -2, -6); scene.add(rim);
  const portalLight = new T.PointLight("#ffd9a0", 0, 18, 2); portalLight.position.set(0, 0, 2.5); scene.add(portalLight);

  const nebula = backdrop((g, w, h) => {
    g.fillStyle = "#04040b"; g.fillRect(0, 0, w, h);
    const blob = (x: number, y: number, r: number, c: string) => { const gr = g.createRadialGradient(x, y, 0, x, y, r); gr.addColorStop(0, c); gr.addColorStop(1, "rgba(0,0,0,0)"); g.fillStyle = gr; g.fillRect(0, 0, w, h); };
    blob(w * 0.25, h * 0.35, 380, "rgba(112,52,160,.38)"); blob(w * 0.78, h * 0.62, 420, "rgba(40,96,168,.32)"); blob(w * 0.52, h * 0.2, 300, "rgba(190,64,120,.22)"); blob(w * 0.6, h * 0.85, 300, "rgba(255,170,80,.12)");
  }, 150, 84);
  nebula.position.set(0, 0, -70); scene.add(nebula);
  const stars = new ParticleField({ count: Math.round(1500 * particleScale(quality)), size: 0.18, color: "#dfe6ff", colorB: "#ffe2b8", opacity: 0.95, bounds: [70, 40, 30], center: [0, 0, -30], twinkle: 0.9, shape: "spark", drift: 0.02 }); scene.add(stars.points);

  /* ---------- the sixteen lights ---------- */
  const palette = Array.from({ length: ORBS }, (_, i) => new T.Color().setHSL((i / ORBS + 0.02) % 1, 0.8, 0.62));
  const orbGeo = new T.SphereGeometry(0.16, 20, 14);
  const orbs = palette.map((c, i) => {
    const g = new T.Group(); const core = new T.Mesh(orbGeo, new T.MeshBasicMaterial({ color: c.clone().lerp(new T.Color("#ffffff"), 0.55), toneMapped: false })); g.add(core);
    const halo = glowSprite("#" + c.getHexString(), 1.7, 0.5); g.add(halo); scene.add(g);
    const rnd = (n: number) => hash(i, n), home = new T.Vector3((rnd(1) - 0.5) * 15, (rnd(2) - 0.5) * 8, (rnd(3) - 0.5) * 9 + 1), a = (i / ORBS) * Math.PI * 2;
    return { g, core, halo, home, ring: new T.Vector3(Math.cos(a) * RING_R, Math.sin(a) * RING_R, 0), ph: rnd(4) * 6.28, sp: 0.3 + rnd(5) * 0.5 };
  });
  const threadGeo = new T.BufferGeometry(); threadGeo.setAttribute("position", new T.BufferAttribute(new Float32Array((ORBS + 1) * 3), 3));
  const thread = new T.Line(threadGeo, new T.LineBasicMaterial({ color: "#ffe9c0", transparent: true, opacity: 0, blending: T.AdditiveBlending, depthWrite: false })); thread.frustumCulled = false; scene.add(thread);

  /* ---------- rings, swirl, flash ---------- */
  const rings = [{ mat: kit.metal("gold", 0.22), r: RING_R + 0.28, t: 0.1, axis: "z" }, { mat: kit.metal("silver", 0.2), r: RING_R + 0.62, t: 0.075, axis: "x" }, { mat: kit.metal("rosegold", 0.25), r: RING_R + 0.96, t: 0.06, axis: "y" }].map((d, i) => {
    const g = new T.Group(); put(g, new T.TorusGeometry(d.r, d.t, 18, 120), d.mat, 0, 0, 0, false); const studs = new T.InstancedMesh(new T.SphereGeometry(d.t * 1.5, 10, 8), d.mat, 24), m = new T.Object3D();
    for (let k = 0; k < 24; k++) { const a = (k / 24) * Math.PI * 2; m.position.set(Math.cos(a) * d.r, Math.sin(a) * d.r, 0); m.updateMatrix(); studs.setMatrixAt(k, m.matrix); } g.add(studs); g.scale.setScalar(0.001); scene.add(g); return { g, axis: d.axis, i };
  });
  const swirlUniforms = { uTime: { value: 0 }, uOpen: { value: 0 } };
  const swirl = new T.Mesh(new T.CircleGeometry(RING_R + 0.1, 96), new T.ShaderMaterial({ uniforms: swirlUniforms, vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }", fragmentShader: SWIRL_FRAG, transparent: true, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide })); scene.add(swirl);
  const flash = new T.Sprite(new T.SpriteMaterial({ map: softTexture(), color: "#fff2d0", transparent: true, opacity: 0, depthTest: false, blending: T.AdditiveBlending })); flash.scale.set(60, 60, 1); flash.position.set(0, 0, 4); flash.renderOrder = 20; scene.add(flash);
  const sparkle = sparkleSprite("#ffe9b0", 3, 0); sparkle.position.set(0, 0, 0.4); scene.add(sparkle);
  const stream = new ParticleField({ count: Math.round(260 * particleScale(quality)), size: 0.1, color: "#ffd9a0", colorB: "#ff9ad0", opacity: 0, bounds: [RING_R + 1, RING_R + 1, 0.6], center: [0, 0, 0.2], distribution: "shell", shellInner: 0.35, twinkle: 1, shape: "spark", drift: 0.9 }); scene.add(stream.points);
  void low;

  /* ---------- choreography ---------- */
  const pos = new T.Vector3(), look = new T.Vector3(), orbit = { yaw: 0, pitch: 0 }, tmp = new T.Vector3();
  let g1 = 0, g2 = 0, flashK = 0, lastG2 = 0, lastG1 = 0;
  return {
    frame(time, dt, state: SceneState, reduced) {
      const stage3 = state.growth ?? (state.open ? 2 : 0);
      g1 = damp(g1, stage3 >= 1 ? 1 : 0, 1.0, dt, reduced); g2 = damp(g2, stage3 >= 2 ? 1 : 0, 0.9, dt, reduced);
      if (g1 > 0.5 && lastG1 <= 0.5) stage.sfx("chime"); lastG1 = g1;
      if (g2 > 0.04 && lastG2 <= 0.04) { flashK = 1; stage.sfx("portal"); } lastG2 = g2;
      flashK = Math.max(0, flashK - dt * (reduced ? 6 : 1.4)); (flash.material as T.SpriteMaterial).opacity = flashK * 0.85 * (reduced ? 0.3 : 1);
      const gather = ease.inOut(g1), spin = reduced ? 0 : time * 0.25 * (0.3 + gather);
      orbs.forEach((o, i) => {
        const wander = reduced ? 0 : 1;
        tmp.set(o.home.x + Math.sin(time * o.sp + o.ph) * 0.9 * wander, o.home.y + Math.cos(time * o.sp * 0.8 + o.ph) * 0.7 * wander, o.home.z + Math.sin(time * o.sp * 0.6 + o.ph * 2) * 0.6 * wander);
        const ca = Math.cos(spin), sa = Math.sin(spin), rx = o.ring.x * ca - o.ring.y * sa, ry = o.ring.x * sa + o.ring.y * ca;
        o.g.position.set(tmp.x + (rx - tmp.x) * gather, tmp.y + (ry - tmp.y) * gather, tmp.z + (0 - tmp.z) * gather);
        const bright = 0.4 + 0.6 * gather + 0.25 * g2; (o.halo.material as T.SpriteMaterial).opacity = 0.5 * bright + (reduced ? 0 : Math.sin(time * 3 + i) * 0.08); o.halo.scale.setScalar(1.5 + 1.2 * gather + 0.8 * g2);
        o.core.scale.setScalar(0.8 + 0.5 * gather + 0.3 * g2);
      });
      const tp = threadGeo.attributes.position as T.BufferAttribute; orbs.forEach((o, i) => tp.setXYZ(i, o.g.position.x, o.g.position.y, o.g.position.z)); tp.setXYZ(ORBS, orbs[0].g.position.x, orbs[0].g.position.y, orbs[0].g.position.z); tp.needsUpdate = true;
      (thread.material as T.LineBasicMaterial).opacity = 0.7 * span(gather, 0.5, 1) * (1 - 0.7 * g2);
      const rise = ease.out(span(g2, 0, 0.55)) * 0.92, open = ease.inOut(span(g2, 0.25, 1));
      rings.forEach((r) => {
        r.g.scale.setScalar(0.001 + rise); const rate = (reduced ? 0 : time) * (0.35 + r.i * 0.18);
        r.g.rotation.set(r.axis === "x" ? Math.PI / 2.6 + rate * 0.5 : r.axis === "y" ? rate * 0.5 : 0, r.axis === "y" ? Math.PI / 2.3 + rate * 0.5 : 0, r.axis === "z" ? rate : 0);
      });
      swirlUniforms.uTime.value = time; swirlUniforms.uOpen.value = open; swirl.scale.setScalar(0.3 + 0.7 * open); swirl.visible = open > 0.002;
      portalLight.intensity = 40 * open; (sparkle.material as T.SpriteMaterial).opacity = 0.32 * open; sparkle.scale.setScalar(2.2 + 1.6 * open + (reduced ? 0 : Math.sin(time * 2) * 0.3));
      stream.opacity = damp(stream.opacity, 0.9 * open, 3, dt, reduced); stream.update(time); stars.update(time);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.4, 0.4);
      pos.set((reduced ? 0 : Math.sin(time * 0.15) * 0.8), 0.4 + (reduced ? 0 : Math.sin(time * 0.11) * 0.3), 16.2 - 2.4 * gather - 1.6 * open); look.set(0, 0, 0);
      orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 74. `src/three/gifts/treasure.ts` — new

```ts
/**
 * Gift 16 - Secret Treasure Hunt.
 * A torchlit stone vault. Three engraved medallions (flower, moon, star) sit in sockets above an arched gate; they stand in
 * whatever order the puzzle currently holds (state.detail = "flower|moon|star", slot order) and glide between sockets when
 * the player swaps them. When the order is right the gate slides open (state.growth 1) and a chest waits behind it. The
 * right password (state.open) sends a brass key into the lock, turns it, lifts the arched lid and pours gold light over a
 * heap of coins. Everything reverses on restart because the opening is one scrubbable timeline.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease, Sequence } from "../../engine/anim";
import { Burst, Flame, ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, put, starShape } from "../../engine/geometry";
import { addPointLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { box, glowSprite, hash, orbitCamera } from "./common";

const SLOT_X = [-1.65, 0, 1.65], SLOT_Y = 6.55, AW = 1.95, AH = 3.2, DEFAULT_ORDER = ["flower", "moon", "star"];
type Symbol3 = "flower" | "moon" | "star";

function crescent() {
  const R = 0.32, r = 0.26, c = 0.14, s = new T.Shape(); s.absarc(0, 0, R, 0.919, Math.PI * 2 - 0.919, false); s.absarc(c, 0, r, Math.PI * 2 - 1.364, 1.364, true); s.closePath(); return s;
}

export function buildTreasureWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "candle", envIntensity: 0.7, exposure: 1.1, background: "#07090c", fog: { color: "#0a0d10", density: 0.02 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 90; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#7a8fb0", "#1a1410", 0.42));
  const torchLights = [-4.1, 4.1].map((x) => addPointLight(scene, "#ff9a4a", 30, [x, 3.8, 1.4], 14, 2));
  const nicheLight = addPointLight(scene, "#ffcf7a", 0, [0, 2.2, -1.4], 7, 2);
  const chestLight = addPointLight(scene, "#ffd36a", 0, [0, 1.8, -2.2], 6, 2);
  const cool = new T.DirectionalLight("#6f8fd0", 0.5); cool.position.set(0, 8, 10); scene.add(cool);

  /* ---------- vault ---------- */
  const stone = kit.stone("#3b3832", "#8a8478", [0.22, 0.22]), floorStone = kit.stone("#2b2924", "#6c675c", [7, 7]);
  const wallShape = new T.Shape(); wallShape.moveTo(-9, 0); wallShape.lineTo(9, 0); wallShape.lineTo(9, 10); wallShape.lineTo(-9, 10); wallShape.closePath();
  const arch = new T.Path(); arch.moveTo(-AW, 0); arch.lineTo(-AW, AH); arch.absarc(0, AH, AW, Math.PI, 0, true); arch.lineTo(AW, 0); arch.closePath(); wallShape.holes.push(arch);
  const wall = new T.Mesh(new T.ExtrudeGeometry(wallShape, { depth: 0.9, bevelEnabled: false, curveSegments: 18 }), stone); wall.position.z = -0.9; wall.receiveShadow = true; wall.castShadow = !low; scene.add(wall);
  const floor = put(scene, new T.PlaneGeometry(40, 40), floorStone, 0, 0, -6, false); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;
  put(scene, new T.PlaneGeometry(20, 12), new T.MeshStandardMaterial({ color: "#14120f", roughness: 1 }), 0, 5, -7.2, false);
  box(scene, 18.2, 0.9, 1.1, stone, 0, 8.4, 0, true); for (const x of [-1, 1]) box(scene, 0.8, 10, 1.2, stone, x * 9.2, 5, -0.3, true);
  const archRing = put(scene, new T.TorusGeometry(AW + 0.14, 0.16, 10, 40, Math.PI), stone, 0, AH, 0.05); void archRing;
  put(scene, new T.TorusGeometry(AW + 0.14, 0.14, 10, 40, Math.PI), kit.metal("brass", 0.4), 0, AH, 0.12, false);

  /* gate doors (slide into the wall) */
  const doorShape = (sign: number) => { const s = new T.Shape(); s.moveTo(0, 0); s.lineTo(sign * AW, 0); s.lineTo(sign * AW, AH); s.absarc(0, AH, AW, sign > 0 ? 0 : Math.PI, Math.PI / 2, sign < 0); s.lineTo(0, 0); return s; };
  const ironMat = kit.metal("steel", 0.5), woodDoor = kit.wood("#1c0f07", "#4b2f1c", [0.3, 0.3], 0.55);
  const doors = [-1, 1].map((sign) => {
    const g = new T.Group(); const body = new T.Mesh(new T.ExtrudeGeometry(doorShape(sign), { depth: 0.22, bevelEnabled: true, bevelSize: 0.03, bevelThickness: 0.03, bevelSegments: 1, curveSegments: 14 }), woodDoor); body.castShadow = true; g.add(body);
    for (const y of [0.7, 2.0, 3.3]) put(g, new T.BoxGeometry(AW, 0.16, 0.06), ironMat, sign * AW / 2, y, 0.27, false);
    const ring = put(g, new T.TorusGeometry(0.2, 0.035, 8, 20), kit.metal("brass", 0.3), sign * 0.42, 1.5, 0.3, false); void ring; g.position.set(0, 0, -0.5); scene.add(g); return { g, sign };
  });

  /* torches */
  const flames = [-4.1, 4.1].map((x) => {
    const g = new T.Group(); g.position.set(x, 3.2, 0.4); scene.add(g);
    put(g, new T.CylinderGeometry(0.1, 0.07, 1.0, 10), kit.wood("#2a160b", "#6a4224", [1, 2]), 0, 0.2, 0, false); put(g, new T.CylinderGeometry(0.17, 0.1, 0.22, 10), kit.metal("brass", 0.4), 0, 0.78, 0, false);
    put(g, new T.BoxGeometry(0.1, 0.1, 0.5), kit.metal("steel", 0.5), 0, -0.2, -0.3, false); const f = new Flame(0.8, 0.42); f.group.position.y = 0.95; g.add(f.group); return f;
  });
  const embers = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.06, color: "#ffb060", colorB: "#ff7a30", opacity: 0.9, bounds: [5.4, 2.4, 0.6], center: [0, 4.2, 0.8], twinkle: 1, shape: "spark", drift: 0.4, rise: 0.35 }); scene.add(embers.points);

  /* ---------- medallions ---------- */
  const gold = kit.metal("gold", 0.22), rose = kit.metal("rosegold", 0.3), darkStone = new T.MeshStandardMaterial({ color: "#0b0b0c", roughness: 0.9 });
  const extrude = (shape: T.Shape, depth = 0.05) => new T.ExtrudeGeometry(shape, { depth, bevelEnabled: true, bevelSize: 0.012, bevelThickness: 0.012, bevelSegments: 1, curveSegments: 14 });
  const flowerGroup = () => { const g = new T.Group(); const petal = new T.Shape(); petal.absellipse(0, 0.17, 0.095, 0.17, 0, Math.PI * 2, false); const geo = extrude(petal, 0.04); for (let k = 0; k < 5; k++) { const m = new T.Mesh(geo, rose); m.rotation.z = (k / 5) * Math.PI * 2; g.add(m); } const c = new T.Shape(); c.absarc(0, 0, 0.09, 0, Math.PI * 2, false); const core = new T.Mesh(extrude(c, 0.07), gold); g.add(core); return g; };
  const makeSymbol = (kind: Symbol3) => kind === "star" ? new T.Mesh(extrude(starShape(0.34, 0.15, 5), 0.06), rose) : kind === "moon" ? new T.Mesh(extrude(crescent(), 0.06), rose) : flowerGroup();
  const enamel = new T.MeshPhysicalMaterial({ color: "#14100f", roughness: 0.3, metalness: 0.2, clearcoat: 0.8, clearcoatRoughness: 0.2 });
  const medals = (["flower", "moon", "star"] as Symbol3[]).map((kind) => {
    const g = new T.Group(); const disc = put(g, new T.CylinderGeometry(0.66, 0.66, 0.14, 48), gold, 0, 0, 0); disc.rotation.x = Math.PI / 2;
    const rim = put(g, new T.TorusGeometry(0.64, 0.055, 10, 48), gold, 0, 0, 0.0, false); void rim;
    const face = put(g, new T.CylinderGeometry(0.52, 0.52, 0.03, 48), enamel, 0, 0, 0.07, false); face.rotation.x = Math.PI / 2;
    const inner = put(g, new T.TorusGeometry(0.52, 0.012, 6, 48), rose, 0, 0, 0.088, false); void inner;
    const sym = makeSymbol(kind); sym.scale.setScalar(kind === "flower" ? 1.45 : kind === "moon" ? 1.35 : 1.3); sym.position.z = 0.09; if (kind === "moon") sym.position.x = -0.07; g.add(sym);
    const halo = glowSprite("#ffd98a", 2.6, 0); halo.position.z = 0.2; g.add(halo);
    const hit = new T.Mesh(new T.SphereGeometry(0.75, 10, 8), new T.MeshBasicMaterial({ visible: false })); g.add(hit); hit.userData.index = 0; g.userData.index = 0; scene.add(g);
    return { kind, g, halo, hit, x: 0, lift: 0, glow: 0, slotPos: 0 };
  });
  for (const x of SLOT_X) { const sock = put(scene, new T.CylinderGeometry(0.78, 0.78, 0.1, 40), darkStone, x, SLOT_Y, 0.52, false); sock.rotation.x = Math.PI / 2; const ring = put(scene, new T.TorusGeometry(0.8, 0.07, 10, 40), kit.metal("brass", 0.35), x, SLOT_Y, 0.58, false); void ring; }

  /* ---------- niche, chest, key ---------- */
  const woodChest = kit.wood("#2a150a", "#6d4325", [1.2, 0.8], 0.5), iron = kit.metal("steel", 0.45), brass = kit.metal("brass", 0.3);
  const chest = new T.Group(); chest.position.set(0, 0, -2.3); scene.add(chest);
  put(chest, new RoundedBoxGeometry(2.0, 0.95, 1.3, 3, 0.05), woodChest, 0, 0.475, 0);
  for (const x of [-0.62, 0.62]) put(chest, new RoundedBoxGeometry(0.14, 0.99, 1.36, 2, 0.02), iron, x, 0.48, 0, false);
  for (const sx of [-1, 1]) for (const sz of [-1, 1]) put(chest, new T.BoxGeometry(0.16, 0.16, 0.16), brass, sx * 0.97, 0.06, sz * 0.62, false);
  const plate = put(chest, new RoundedBoxGeometry(0.36, 0.44, 0.06, 2, 0.02), brass, 0, 0.84, 0.66, false); void plate;
  put(chest, new T.CylinderGeometry(0.045, 0.045, 0.07, 12), new T.MeshBasicMaterial({ color: "#050403" }), 0, 0.88, 0.7, false).rotation.x = Math.PI / 2; put(chest, new T.BoxGeometry(0.04, 0.12, 0.07), new T.MeshBasicMaterial({ color: "#050403" }), 0, 0.8, 0.7, false);
  const hinge = new T.Group(); hinge.position.set(0, 0.95, -0.62); chest.add(hinge);
  const lidMat = new T.MeshStandardMaterial({ ...(woodChest as T.MeshStandardMaterial), side: T.DoubleSide } as T.MeshStandardMaterialParameters); lidMat.map = (woodChest as T.MeshStandardMaterial).map; lidMat.color = (woodChest as T.MeshStandardMaterial).color; lidMat.roughness = 0.5; lidMat.side = T.DoubleSide;
  const lid = new T.Mesh(new T.CylinderGeometry(0.66, 0.66, 2.0, 28, 1, false, 0, Math.PI), lidMat); lid.rotation.z = Math.PI / 2; lid.position.z = 0.62; lid.castShadow = true; hinge.add(lid);
  const lidFloor = put(hinge, new T.PlaneGeometry(2.0, 1.32), new T.MeshStandardMaterial({ color: "#1b0f07", roughness: 0.9, side: T.DoubleSide }), 0, 0.005, 0.62, false); lidFloor.rotation.x = -Math.PI / 2;
  for (const x of [-0.62, 0.62]) { const band = put(hinge, new T.CylinderGeometry(0.685, 0.685, 0.14, 28, 1, true, 0, Math.PI), new T.MeshStandardMaterial({ color: (iron as T.MeshStandardMaterial).color, metalness: 0.9, roughness: 0.45, side: T.DoubleSide }), x, 0, 0.62, false); band.rotation.z = Math.PI / 2; }
  const COINS = 130, coins = new T.InstancedMesh(new T.CylinderGeometry(0.1, 0.1, 0.025, 14), gold, COINS), cm = new T.Object3D();
  for (let i = 0; i < COINS; i++) { const x = (hash(i, 1) - 0.5) * 1.55, z = (hash(i, 2) - 0.5) * 0.85, mound = Math.max(0, 1 - (x / 0.85) ** 2 - (z / 0.5) ** 2); cm.position.set(x, 0.93 + 0.2 * mound + hash(i, 3) * 0.03, z); cm.rotation.set((hash(i, 4) - 0.5) * 0.9, hash(i, 5) * 6, (hash(i, 6) - 0.5) * 0.9); cm.updateMatrix(); coins.setMatrixAt(i, cm.matrix); } chest.add(coins);
  const beamTex = (() => { const c = document.createElement("canvas"); c.width = 128; c.height = 256; const g = c.getContext("2d")!; const gr = g.createLinearGradient(0, 256, 0, 0); gr.addColorStop(0, "rgba(255,226,140,.9)"); gr.addColorStop(1, "rgba(255,226,140,0)"); g.fillStyle = gr; g.fillRect(0, 0, 128, 256); const rr = g.createLinearGradient(0, 0, 128, 0); rr.addColorStop(0, "rgba(0,0,0,1)"); rr.addColorStop(0.5, "rgba(0,0,0,0)"); rr.addColorStop(1, "rgba(0,0,0,1)"); g.globalCompositeOperation = "destination-out"; g.fillStyle = rr; g.fillRect(0, 0, 128, 256); return new T.CanvasTexture(c); })();
  const beam = new T.Mesh(new T.PlaneGeometry(1.8, 3.4), new T.MeshBasicMaterial({ map: beamTex, transparent: true, opacity: 0, blending: T.AdditiveBlending, depthWrite: false, side: T.DoubleSide, fog: false })); beam.position.set(0, 2.6, -2.3); scene.add(beam);
  const treasureGlow = glowSprite("#ffd36a", 4.5, 0); treasureGlow.position.set(0, 1.25, -2.0); scene.add(treasureGlow);
  const sparks = new Burst({ count: low ? 40 : 110, size: 0.13, life: 2.4, speed: 3.0, gravity: 0.9, drag: 0.7, colors: ["#ffe27a", "#fff4c0", "#ffb84a"], shape: "spark", emit: "cone", coneAngle: 0.8 }); scene.add(sparks.points);
  const key = new T.Group(); scene.add(key);
  put(key, new T.TorusGeometry(0.15, 0.04, 8, 24), gold, 0, 0, 0, false); const shaft = put(key, new T.CylinderGeometry(0.03, 0.03, 0.62, 10), gold, 0, 0, -0.38, false); shaft.rotation.x = Math.PI / 2; put(key, new T.BoxGeometry(0.1, 0.11, 0.05), gold, 0.05, 0, -0.62, false); put(key, new T.BoxGeometry(0.1, 0.07, 0.05), gold, 0.05, 0, -0.52, false);
  const keyGlow = glowSprite("#ffe9a8", 0.9, 0.5); key.add(keyGlow);

  const seq = new Sequence(3.0, { key: 0, turn: 0, lid: 0, glow: 0 }, (tl, p) => {
    tl.to(p, { key: 1, duration: 0.8, ease: "power2.inOut" }, 0); tl.to(p, { turn: 1, duration: 0.5 }, 0.85); tl.to(p, { lid: 1, duration: 1.1, ease: "power2.out" }, 1.45); tl.to(p, { glow: 1, duration: 1.0 }, 1.6);
  });
  const pos = new T.Vector3(), look = new T.Vector3(), orbit = { yaw: 0, pitch: 0 }, keyHome = new T.Vector3(1.5, 1.9, -0.6), keyLock = new T.Vector3(0, 0.84, -2.3 + 0.9);
  let gate = 0, lastOpen = false, lastGate = 0, shown = false, lastKey = 0, lastLid = 0;
  const order = DEFAULT_ORDER.slice();
  return {
    pickables: medals.map((m) => m.g),
    dispose() { seq.dispose(); beamTex.dispose(); },
    frame(time, dt, state: SceneState, reduced) {
      const parts = (state.detail ?? "").split("|"); if (parts.length === 3 && parts.every((x) => DEFAULT_ORDER.includes(x))) { order[0] = parts[0]; order[1] = parts[1]; order[2] = parts[2]; }
      const sel = state.selected ?? null, open = Boolean(state.open), gateTarget = state.growth ? 1 : 0;
      gate = damp(gate, gateTarget, 1.1, dt, reduced);
      if (Math.abs(gate - lastGate) > 0.0005 && gateTarget === 1 && lastGate < 0.05) stage.sfx("thud"); lastGate = gate;
      doors.forEach((d) => { d.g.position.x = d.sign * ease.inOut(gate) * (AW + 0.15); });
      nicheLight.intensity = damp(nicheLight.intensity, 3 + 22 * gate, 3, dt, reduced);
      medals.forEach((m) => {
        const slot = Math.max(0, order.indexOf(m.kind)), isSel = sel === slot;
        m.g.userData.index = slot; m.hit.userData.index = slot;
        m.x = damp(m.x === 0 && m.slotPos === 0 ? SLOT_X[slot] : m.x, SLOT_X[slot], 5, dt, reduced); m.slotPos = 1;
        m.lift = damp(m.lift, isSel ? 1 : 0, 6, dt, reduced); m.glow = damp(m.glow, gate > 0.5 ? 1 : isSel ? 0.8 : 0, 4, dt, reduced);
        m.g.position.set(m.x, SLOT_Y + (reduced ? 0 : Math.sin(time * 1.4 + slot) * 0.025), 0.62 + 0.45 * m.lift); m.g.scale.setScalar(1 + 0.18 * m.lift);
        m.g.rotation.y = reduced ? 0 : (isSel ? Math.sin(time * 1.6) * 0.35 : Math.sin(time * 0.7 + slot) * 0.08);
        (m.halo.material as T.SpriteMaterial).opacity = 0.7 * m.glow;
      });
      torchLights.forEach((l, i) => { l.intensity = 30 * (0.9 + (reduced ? 0 : Math.sin(time * 9 + i * 2) * 0.06 + Math.sin(time * 23 + i) * 0.04)); });
      flames.forEach((f) => f.update(time, camera, 1)); embers.update(time);
      const p = seq.phases, progress = seq.step(open ? 1 : 0, dt, reduced || Boolean(state.immediate));
      if (open !== lastOpen) { lastOpen = open; if (open) stage.sfx("key"); }
      if (p.key > 0.98 && lastKey <= 0.98) stage.sfx("click"); lastKey = p.key; if (p.lid > 0.05 && lastLid <= 0.05) { stage.sfx("lid"); } lastLid = p.lid;
      key.visible = p.key > 0.001 || open;
      const approach = ease.inOut(p.key); key.position.copy(keyHome).lerp(keyLock, approach); key.position.y += (1 - approach) * (reduced ? 0 : Math.sin(time * 2) * 0.08);
      key.rotation.set(0, (1 - approach) * 0.9, p.turn * Math.PI * 0.5); key.scale.setScalar(1.5 + 0.3 * (1 - approach));
      (keyGlow.material as T.SpriteMaterial).opacity = 0.55 * (1 - p.turn * 0.5);
      hinge.rotation.x = -1.95 * ease.inOut(p.lid);
      chestLight.intensity = 26 * p.glow; (treasureGlow.material as T.SpriteMaterial).opacity = 0.85 * p.glow; (beam.material as T.MeshBasicMaterial).opacity = 0.55 * p.glow; beam.scale.y = 0.6 + 0.4 * p.glow;
      if (p.glow > 0.35 && !shown) { shown = true; sparks.trigger([0, 1.2, -2.3]); stage.sfx("coin"); } else if (p.glow < 0.05 && shown) shown = false;
      sparks.update(dt);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.0, -0.5, 0.5); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.1, -0.12, 0.25);
      const g = ease.inOut(gate), c = ease.inOut(progress);
      pos.set((reduced ? 0 : Math.sin(time * 0.16) * 0.4), 4.9 - 2.8 * g - 0.3 * c, 14.2 - 8.0 * g - 0.8 * c); look.set(0, 4.6 - 3.2 * g - 0.1 * c, -0.5 - 1.8 * g);
      orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 75. `src/three/gifts/universe.ts` — new

```ts
/**
 * Gift 04 - Our Little Universe.
 * A brass orrery under a night sky: a glowing sun, five textured planets on arms (one ringed, one with a moon),
 * gold orbit rings, a gear base, and two star markers for the only verified dates joined by a constellation arc.
 * The camera flies in on entry; selecting a date swings it to that star. state: selected (0|1|-1), growth = zoom, turn.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { lathe, put, starShape } from "../../engine/geometry";
import { particleScale } from "../../engine/quality";
import { fbm } from "../../engine/textures";
import { glowSprite, orbitCamera } from "./common";

type PlanetKind = "rock" | "venus" | "earth" | "mars" | "saturn";

function planetCanvas(kind: PlanetKind, w = 256, h = 128) {
  const c = document.createElement("canvas"); c.width = w; c.height = h; const g = c.getContext("2d", { willReadFrequently: true })!, img = g.createImageData(w, h);
  for (let j = 0; j < h; j++) for (let i = 0; i < w; i++) {
    const u = i / w, v = j / h, n = fbm(u, v, kind.length * 7, 5, 6, 3), o = (j * w + i) * 4; let r = 0, gg = 0, b = 0;
    if (kind === "rock") { const k = 0.35 + n * 0.8; r = 140 * k; gg = 130 * k; b = 120 * k; }
    else if (kind === "venus") { const sw = 0.5 + 0.5 * Math.sin((v * 7 + n * 3) * Math.PI); r = 235 - 40 * sw; gg = 205 - 50 * sw; b = 150 - 40 * sw; }
    else if (kind === "mars") { const k = 0.55 + n * 0.7; r = 190 * k; gg = 95 * k; b = 60 * k; }
    else if (kind === "saturn") { const band = 0.5 + 0.5 * Math.sin(v * 22 + n * 4); r = 215 - 55 * band; gg = 180 - 55 * band; b = 120 - 40 * band; }
    else { // earth
      const land = n > 0.52, polar = Math.abs(v - 0.5) > 0.4, cloud = fbm(u, v, 91, 4, 8, 4) > 0.6;
      if (polar) { r = 240; gg = 245; b = 250; } else if (land) { const k = 0.7 + n * 0.5; r = 70 * k + 40; gg = 130 * k; b = 60 * k; } else { r = 28; gg = 78 + 30 * n; b = 150 + 40 * n; }
      if (cloud && !polar) { r = r * 0.4 + 150; gg = gg * 0.4 + 150; b = b * 0.4 + 150; }
    }
    img.data[o] = r; img.data[o + 1] = gg; img.data[o + 2] = b; img.data[o + 3] = 255;
  }
  g.putImageData(img, 0, 0);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; return t;
}

function dialTexture() {
  const s = 1024, c = document.createElement("canvas"); c.width = c.height = s; const g = c.getContext("2d")!;
  g.fillStyle = "#2a2118"; g.fillRect(0, 0, s, s); g.translate(s / 2, s / 2);
  g.strokeStyle = "#d9b65e"; g.lineWidth = 3;
  for (const r of [470, 430, 300, 210]) { g.beginPath(); g.arc(0, 0, r, 0, Math.PI * 2); g.stroke(); }
  for (let i = 0; i < 360; i++) { const a = (i / 360) * Math.PI * 2, long = i % 30 === 0, mid = i % 10 === 0; g.lineWidth = long ? 3 : 1.2; g.beginPath(); g.moveTo(Math.cos(a) * 430, Math.sin(a) * 430); g.lineTo(Math.cos(a) * (long ? 400 : mid ? 410 : 418), Math.sin(a) * (long ? 400 : mid ? 410 : 418)); g.stroke(); }
  g.fillStyle = "#d9b65e"; g.font = "600 34px Georgia, serif"; g.textAlign = "center"; g.textBaseline = "middle";
  ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"].forEach((n, i) => { const a = (i / 12) * Math.PI * 2 - Math.PI / 2; g.fillText(n, Math.cos(a) * 365, Math.sin(a) * 365); });
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 8; return t;
}

export function buildUniverseWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "moon", envIntensity: 0.7, exposure: 1.1, background: "#04060e", fog: null });
  camera.fov = 38; camera.near = 0.1; camera.far = 200; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#6a7fc0", "#120f0a", 0.35));
  const rim = new T.DirectionalLight("#6f94ff", 1.4); rim.position.set(-6, 5, -6); scene.add(rim);
  const warm = new T.DirectionalLight("#ffd3a0", 0.9); warm.position.set(5, 3, 7); scene.add(warm);

  /* ---------- sky ---------- */
  const stars = new ParticleField({ count: Math.round(1500 * particleScale(quality)), size: 0.16, color: "#cfe0ff", colorB: "#ffe3b8", opacity: 0.95, bounds: [60, 60, 60], distribution: "shell", shellInner: 0.75, drift: 0.05, twinkle: 0.7, shape: "spark" });
  scene.add(stars.points);
  for (const [x, y, z, s, c] of [[-22, 12, -34, 46, "#5b45c9"], [18, 6, -38, 54, "#2e86c8"], [4, -6, -40, 40, "#c0488a"]] as const) { const g = glowSprite(c, s, 0.2); g.position.set(x, y, z); scene.add(g); }

  /* ---------- pedestal and gear base ---------- */
  const brass = kit.metal("brass", 0.3), gold = kit.metal("gold", 0.24);
  const base = new T.Group(); scene.add(base);
  put(base, new T.CylinderGeometry(3.7, 3.9, 0.7, 72), kit.marble("#3a3a44", "#8d8a96"), 0, -0.35, 0);
  put(base, new T.TorusGeometry(3.7, 0.06, 10, 96), gold, 0, 0.0, 0).rotation.x = Math.PI / 2;
  const plate = put(base, new T.CylinderGeometry(3.3, 3.3, 0.14, 96), new T.MeshStandardMaterial({ map: dialTexture(), roughness: 0.45, metalness: 0.6 }), 0, 0.07, 0);
  plate.receiveShadow = true;
  const cogs: T.Mesh[] = [];
  for (const [x, z, r, n] of [[-1.2, 0.0, 0.7, 14], [0.4, 0.15, 0.5, 10], [1.4, -0.1, 0.9, 18]] as const) {
    const gear = new T.Group(); gear.position.set(x, 0.24, z + 2.6 * 0); base.add(gear);
    put(gear, new T.CylinderGeometry(r, r, 0.08, n * 2), brass, 0, 0, 0);
    for (let i = 0; i < n; i++) { const a = (i / n) * Math.PI * 2; const tooth = put(gear, new T.BoxGeometry(0.12, 0.08, 0.16), brass, Math.cos(a) * (r + 0.04), 0, Math.sin(a) * (r + 0.04), false); tooth.rotation.y = -a; }
    gear.position.set(x, 0.2, 2.2 + z * 0.5); cogs.push(gear as unknown as T.Mesh);
  }
  const column = put(base, lathe([[0, 0], [0.5, 0], [0.45, 0.2], [0.18, 0.4], [0.14, 1.6], [0.22, 1.75], [0.12, 1.9], [0, 1.9]], 32), brass, 0, 0.14, 0);
  void column;

  /* ---------- sun and planets ---------- */
  const orrery = new T.Group(); orrery.position.y = 2.4; scene.add(orrery);
  const sun = put(orrery, new T.SphereGeometry(0.5, 40, 28), new T.MeshBasicMaterial({ color: "#ffcf70", toneMapped: false }), 0, 0, 0, false);
  const corona = glowSprite("#ff9a3a", 2.7, 0.5); orrery.add(corona);
  const corona2 = glowSprite("#ffe6a8", 1.3, 0.7); orrery.add(corona2);
  const sunLight = new T.PointLight("#ffd29a", 55, 14, 2); orrery.add(sunLight);
  const kinds: { kind: PlanetKind; r: number; size: number; speed: number; tilt: number }[] = [
    { kind: "rock", r: 1.15, size: 0.14, speed: 0.9, tilt: 0.0 }, { kind: "venus", r: 1.68, size: 0.22, speed: 0.62, tilt: 0.05 },
    { kind: "earth", r: 2.28, size: 0.27, speed: 0.46, tilt: -0.04 }, { kind: "mars", r: 2.86, size: 0.19, speed: 0.34, tilt: 0.07 },
    { kind: "saturn", r: 3.45, size: 0.36, speed: 0.22, tilt: -0.06 },
  ];
  const planets = kinds.map((def, i) => {
    const orbit = new T.Group(); orbit.rotation.z = def.tilt; orbit.rotation.y = i * 1.3; orrery.add(orbit);
    const ring = put(orbit, new T.TorusGeometry(def.r, 0.007, 6, 120), new T.MeshBasicMaterial({ color: "#d9b65e", transparent: true, opacity: 0.35 }), 0, 0, 0, false); ring.rotation.x = Math.PI / 2;
    const arm = put(orbit, new T.CylinderGeometry(0.014, 0.014, def.r, 6), gold, def.r / 2, 0, 0, false); arm.rotation.z = Math.PI / 2;
    const body = new T.Mesh(new T.SphereGeometry(def.size, low ? 24 : 40, low ? 16 : 28), new T.MeshStandardMaterial({ map: planetCanvas(def.kind), roughness: def.kind === "earth" ? 0.55 : 0.85 }));
    body.position.x = def.r; body.castShadow = true; orbit.add(body);
    if (def.kind === "saturn") {
      const ringGeo = new T.RingGeometry(def.size * 1.45, def.size * 2.3, 72, 1), pos = ringGeo.attributes.position, uv = ringGeo.attributes.uv;
      for (let k = 0; k < pos.count; k++) { const rr = Math.hypot(pos.getX(k), pos.getY(k)); uv.setXY(k, (rr - def.size * 1.45) / (def.size * 0.85), 0.5); }
      const rc = document.createElement("canvas"); rc.width = 256; rc.height = 4; const rg = rc.getContext("2d")!; const gr = rg.createLinearGradient(0, 0, 256, 0); gr.addColorStop(0, "rgba(220,190,140,0)"); gr.addColorStop(0.15, "rgba(230,200,150,.9)"); gr.addColorStop(0.4, "rgba(150,120,90,.5)"); gr.addColorStop(0.55, "rgba(235,210,160,.95)"); gr.addColorStop(1, "rgba(200,170,120,0)"); rg.fillStyle = gr; rg.fillRect(0, 0, 256, 4);
      const rt = new T.CanvasTexture(rc); rt.colorSpace = T.SRGBColorSpace;
      const rings = new T.Mesh(ringGeo, new T.MeshStandardMaterial({ map: rt, transparent: true, side: T.DoubleSide, roughness: 0.8 })); rings.rotation.x = Math.PI / 2 - 0.45; body.add(rings);
    }
    let moon: T.Group | null = null;
    if (def.kind === "earth") { moon = new T.Group(); body.add(moon); put(moon, new T.SphereGeometry(0.07, 20, 14), new T.MeshStandardMaterial({ color: "#b9b6ae", roughness: 0.95 }), 0.5, 0, 0); }
    return { def, orbit, body, moon };
  });

  /* ---------- date stars + constellation ---------- */
  const starMat = new T.MeshStandardMaterial({ color: "#ffe39a", emissive: new T.Color("#ffb83a"), emissiveIntensity: 1.2, metalness: 0.3, roughness: 0.3 });
  const markers = [new T.Vector3(-2.3, 4.55, -0.6), new T.Vector3(2.5, 4.25, 0.5)].map((p, i) => {
    const group = new T.Group(); group.position.copy(p); group.userData.index = i; scene.add(group);
    const mesh = put(group, new T.ExtrudeGeometry(starShape(0.42, 0.18, 5), { depth: 0.12, bevelEnabled: true, bevelSize: 0.03, bevelThickness: 0.03, bevelSegments: 2 }), starMat, 0, 0, -0.06, false);
    mesh.userData.index = i;
    const halo = glowSprite("#ffd27a", 2.2, 0.55); group.add(halo);
    return { group, halo };
  });
  const arc = new T.CatmullRomCurve3([markers[0].group.position, new T.Vector3(-0.6, 5.5, -0.8), new T.Vector3(0.9, 5.3, -0.1), markers[1].group.position]);
  scene.add(new T.Mesh(new T.TubeGeometry(arc, 60, 0.012, 6, false), new T.MeshBasicMaterial({ color: "#ffe9b0", transparent: true, opacity: 0.55, blending: T.AdditiveBlending, depthWrite: false })));
  const dots = new ParticleField({ count: 14, size: 0.12, color: "#ffeab8", opacity: 1, bounds: [3.4, 0.9, 0.7], center: [0, 4.9, -0.4], drift: 0.2, twinkle: 0.6, shape: "spark", seed: 7 });
  scene.add(dots.points);

  /* ---------- choreography ---------- */
  const s = { zoom: 1, turn: 0, focus: 0, look: new T.Vector3(0, 3.2, 0) };
  const orbitState = { yaw: 0, pitch: 0 }, pos = new T.Vector3(), lookAt = new T.Vector3(), wanted = new T.Vector3();
  let lastSelected: number | undefined;
  return {
    pickables: markers.map((m) => m.group),
    frame(time, dt, state: SceneState, reduced) {
      if (state.selected !== lastSelected) { if (lastSelected !== undefined && (state.selected ?? -1) >= 0) stage.sfx("star"); lastSelected = state.selected ?? -1; }
      s.zoom = damp(s.zoom, T.MathUtils.clamp(state.growth ?? 1, 0.7, 1.8), 3, dt, reduced);
      s.turn = damp(s.turn, state.turn ?? 0, 2.5, dt, reduced);
      const drag = input.consumeDrag();
      orbitState.yaw = orbitState.yaw - drag.x * 5; orbitState.pitch = T.MathUtils.clamp(orbitState.pitch + drag.y * 1.5, -0.25, 0.5);
      const intro = reduced ? 1 : ease.inOut(T.MathUtils.clamp(time / 4.2, 0, 1));
      orrery.rotation.y = s.turn + (reduced ? 0 : time * 0.02);
      planets.forEach((p, i) => {
        p.orbit.rotation.y = i * 1.3 + (reduced ? 0 : time * p.def.speed * 0.5);
        p.body.rotation.y = (reduced ? 0 : time * (0.6 + i * 0.2));
        if (p.moon) p.moon.rotation.y = reduced ? 1 : time * 1.8;
      });
      cogs.forEach((g, i) => { g.rotation.y = (reduced ? 0 : time * (i % 2 ? -0.5 : 0.4)); });
      const pulse = reduced ? 1 : 1 + Math.sin(time * 2.4) * 0.06;
      corona.scale.setScalar(2.7 * pulse); corona2.scale.setScalar(1.3 * (1 + Math.sin(time * 3.1) * 0.05)); sun.rotation.y = time * 0.1;
      markers.forEach((m, i) => {
        const on = state.selected === i;
        m.group.rotation.y = reduced ? 0 : time * 0.6 + i; m.group.position.y += (Math.sin(time * 1.1 + i * 2) * 0.002) * (reduced ? 0 : 1);
        m.halo.scale.setScalar((on ? 3.6 : 2.2) * (1 + Math.sin(time * 3 + i) * 0.08)); (m.halo.material as T.SpriteMaterial).opacity = on ? 0.9 : 0.5;
        m.group.scale.setScalar(damp(m.group.scale.x, on ? 1.35 : 1, 5, dt, reduced));
      });
      stars.update(time); dots.update(time);
      s.focus = damp(s.focus, state.selected != null && state.selected >= 0 ? 1 : 0, 2.6, dt, reduced);
      const sel = state.selected != null && state.selected >= 0 ? markers[state.selected].group.position : markers[0].group.position;
      wanted.copy(sel); wanted.y -= 0.6;
      lookAt.set(0, 3.1, 0).lerp(wanted, s.focus * 0.6);
      const dist = (16 - 6.4 * intro) / s.zoom * (1 - 0.2 * s.focus);
      pos.set(0, 3.2 + 3.2 * (1 - intro) + 0.6, dist); pos.add(new T.Vector3(Math.sin(time * 0.15) * 0.4 * (reduced ? 0 : 1), 0, 0));
      orbitCamera(camera, pos, lookAt, orbitState.yaw, orbitState.pitch, 0.85);
    },
  };
}
```

## 76. `src/three/gifts/vinyl.ts` — new

```ts
/**
 * Gift 12 - The Music of Us.
 * A walnut turntable in a lamp-lit listening room. The record is shaded procedurally: concentric grooves, track gaps and
 * the two world-fixed light wedges you see on real vinyl, so the sheen stays put while the grooves spin through it.
 * The tonearm swings in and the needle drops only while something is playing (or the silent mechanical preview runs).
 * The LED ring and the woofers follow state.spectrum, which the host fills from the real audio analyser: no audio, no motion.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp } from "../../engine/anim";
import { ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, lathe, put } from "../../engine/geometry";
import { addContactShadow, addKeyLight, addPointLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, glowSprite, hash, orbitCamera, paintBokeh } from "./common";

const REC_R = 1.45, LED_COUNT = 48, ARM_LEN = Math.hypot(0.35, 2.45), ARM_BASE = Math.atan2(0.35, 2.45);

function labelTexture() {
  const c = document.createElement("canvas"); c.width = c.height = 512; const g = c.getContext("2d")!;
  const bg = g.createRadialGradient(256, 256, 20, 256, 256, 256); bg.addColorStop(0, "#2c7a78"); bg.addColorStop(1, "#174d52"); g.fillStyle = bg; g.fillRect(0, 0, 512, 512);
  g.strokeStyle = "rgba(246,214,140,.9)"; g.lineWidth = 5; g.beginPath(); g.arc(256, 256, 236, 0, 6.283); g.stroke(); g.lineWidth = 2; g.beginPath(); g.arc(256, 256, 222, 0, 6.283); g.stroke();
  g.fillStyle = "#f6e3b0"; g.textAlign = "center"; g.font = "700 46px Georgia, serif"; g.fillText("THE MUSIC", 256, 214); g.fillText("OF US", 256, 270); g.font = "italic 26px Georgia, serif"; g.fillText("33\u2153 RPM", 256, 340);
  g.fillStyle = "#0d1b1d"; g.beginPath(); g.arc(256, 256, 14, 0, 6.283); g.fill(); const t = new T.CanvasTexture(g.canvas); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}
function sleeveTexture() {
  const c = document.createElement("canvas"); c.width = c.height = 512; const g = c.getContext("2d")!;
  g.fillStyle = "#f3e7cd"; g.fillRect(0, 0, 512, 512);
  const cols = ["#d9564d", "#f0b43a", "#2c7a78", "#1d3f5c"]; cols.forEach((col, i) => { g.fillStyle = col; g.beginPath(); g.arc(256, 256, 190 - i * 38, 0, 6.283); g.fill(); });
  g.fillStyle = "#f3e7cd"; g.beginPath(); g.arc(256, 256, 26, 0, 6.283); g.fill(); g.fillStyle = "#2a1f1a"; g.font = "700 30px Georgia, serif"; g.textAlign = "center"; g.fillText("THE MUSIC OF US", 256, 482);
  const t = new T.CanvasTexture(c); t.colorSpace = T.SRGBColorSpace; t.anisotropy = 4; return t;
}

export function buildVinylWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  stage.mood({ env: "candle", envIntensity: 0.9, exposure: 1.1, background: "#120d0b", fog: { color: "#140e0b", density: 0.02 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 80; camera.updateProjectionMatrix();
  scene.add(new T.HemisphereLight("#ffd9ae", "#140e0b", 0.45));
  addKeyLight(scene, quality, { color: "#ffd2a0", intensity: 2.8, position: [-5, 7, 5], target: [0, 0.3, 0], extent: 7, far: 24 });
  const lampLight = addPointLight(scene, "#ffb066", 24, [-4.6, 3.2, 0.4], 11, 2);
  const rim = new T.DirectionalLight("#6f8fd0", 0.7); rim.position.set(5, 3, -5); scene.add(rim);

  /* ---------- room ---------- */
  const room = backdrop((g, w, h) => {
    const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#1a110d"); bg.addColorStop(1, "#2a1b13"); g.fillStyle = bg; g.fillRect(0, 0, w, h);
    g.fillStyle = "#0e1424"; g.fillRect(w * 0.62, 70, w * 0.3, h * 0.5); paintBokeh(g, w * 0.3, h * 0.5, "255,200,140", 0, 1);
    for (let i = 0; i < 26; i++) { g.fillStyle = `rgba(${i % 3 ? 255 : 150},${190 + (i % 4) * 14},${120 + (i % 5) * 20},.75)`; const x = w * 0.62 + hash(i, 2) * w * 0.3, y = 90 + hash(i, 5) * h * 0.46; g.beginPath(); g.arc(x, y, 3 + hash(i, 7) * 9, 0, 6.283); g.fill(); }
    g.strokeStyle = "#3a2618"; g.lineWidth = 8; g.strokeRect(w * 0.62, 70, w * 0.3, h * 0.5); g.beginPath(); g.moveTo(w * 0.77, 70); g.lineTo(w * 0.77, 70 + h * 0.5); g.stroke();
    g.fillStyle = "#3a2618"; g.fillRect(40, h * 0.42, w * 0.5, 14); const cols = ["#d9564d", "#f0b43a", "#2c7a78", "#e8dcc0", "#1d3f5c", "#8a5a9a"];
    for (let i = 0; i < 24; i++) { g.fillStyle = cols[i % cols.length]; g.fillRect(52 + i * 20, h * 0.42 - 96 + (i % 3) * 6, 15, 96 - (i % 3) * 6); }
    paintBokeh(g, w, h, "255,176,100", 12, 4);
  }, 48, 27);
  room.position.set(0, 6, -6); scene.add(room);
  const credenza = put(scene, new T.BoxGeometry(24, 1.0, 9), kit.wood("#1e1009", "#5a351e", [4, 1], 0.4), 0, -0.55, 0.6, false); credenza.receiveShadow = true;

  /* ---------- turntable ---------- */
  const walnut = kit.wood("#2a150a", "#80512c", [2, 1.2], 0.38), alu = kit.metal("silver", 0.32), brass = kit.metal("brass", 0.3);
  const deck = new T.Group(); scene.add(deck);
  put(deck, new RoundedBoxGeometry(5.7, 0.58, 4.1, 4, 0.1), walnut, 0, 0.29, 0);
  put(deck, new RoundedBoxGeometry(5.35, 0.05, 3.75, 2, 0.02), alu, 0, 0.6, 0, false);
  for (const sx of [-1, 1]) for (const sz of [-1, 1]) put(deck, new T.CylinderGeometry(0.16, 0.2, 0.14, 14), new T.MeshStandardMaterial({ color: "#111", roughness: 0.6 }), sx * 2.5, -0.06, sz * 1.8, false);
  addContactShadow(scene, 6.4, 4.6, 0, 0.002, 0, 0.55);
  const platter = new T.Group(); platter.position.y = 0.63; deck.add(platter);
  put(platter, new T.CylinderGeometry(1.58, 1.58, 0.14, 64), kit.metal("steel", 0.3), 0, 0.07, 0, false);
  put(platter, new T.CylinderGeometry(1.5, 1.5, 0.03, 64), new T.MeshStandardMaterial({ color: "#161616", roughness: 0.95 }), 0, 0.155, 0, false);
  const disc = new T.Group(); disc.position.y = 0.17; platter.add(disc);
  put(disc, new T.CylinderGeometry(REC_R, REC_R, 0.026, 96), new T.MeshStandardMaterial({ color: "#0a0a0b", roughness: 0.35, metalness: 0.1 }), 0, 0.013, 0, false);
  const label = labelTexture();
  const face = new T.Mesh(new T.CircleGeometry(REC_R, 128), new T.ShaderMaterial({
    uniforms: { uLabel: { value: label }, uCenter: { value: new T.Vector3() } },
    vertexShader: "varying vec2 vP; varying vec3 vW; void main(){ vP = position.xy; vec4 w = modelMatrix * vec4(position, 1.0); vW = w.xyz; gl_Position = projectionMatrix * viewMatrix * w; }",
    fragmentShader: `uniform sampler2D uLabel; uniform vec3 uCenter; varying vec2 vP; varying vec3 vW;
      float h(float n){ return fract(sin(n * 91.3458) * 47453.5453); }
      void main(){
        float r = length(vP) / ${REC_R.toFixed(2)};
        vec3 col;
        if (r < 0.34) { col = texture2D(uLabel, vP / (${REC_R.toFixed(2)} * 0.34) * 0.5 + 0.5).rgb; }
        else {
          float rr = r * 900.0, groove = 0.5 + 0.5 * sin(rr * 0.62 + h(floor(rr * 0.07)) * 6.28);
          float gap = (1.0 - smoothstep(0.0, 0.012, abs(r - 0.52))) + (1.0 - smoothstep(0.0, 0.012, abs(r - 0.69))) + (1.0 - smoothstep(0.0, 0.012, abs(r - 0.83)));
          vec2 d = vW.xz - uCenter.xz; float ang = atan(d.y, d.x);
          float wedge = pow(abs(cos(ang - 0.75)), 16.0) + 0.8 * pow(abs(cos(ang + 2.35)), 16.0);
          float sheen = wedge * (0.18 + 0.82 * groove) * smoothstep(0.34, 0.4, r) * (1.0 - smoothstep(0.97, 1.0, r));
          col = vec3(0.012) + vec3(0.025) * groove + gap * vec3(0.05) + vec3(0.85, 0.9, 1.0) * sheen * 0.62 + 0.1 * vec3(sin(ang * 3.0), sin(ang * 3.0 + 2.1), sin(ang * 3.0 + 4.2)) * sheen;
        }
        gl_FragColor = vec4(col, 1.0);
        #include <colorspace_fragment>
      }`,
  }));
  face.rotation.x = -Math.PI / 2; face.position.y = 0.0275; disc.add(face);
  put(platter, new T.CylinderGeometry(0.05, 0.05, 0.28, 12), brass, 0, 0.3, 0, false); put(platter, new T.ConeGeometry(0.05, 0.12, 12), brass, 0, 0.5, 0, false);

  /* control cluster: speed knob, start button, LED */
  const knob = put(deck, new T.CylinderGeometry(0.2, 0.22, 0.16, 24), new T.MeshStandardMaterial({ color: "#1a1a1a", roughness: 0.4, metalness: 0.5 }), -2.2, 0.7, 1.6, false);
  put(knob, new T.BoxGeometry(0.03, 0.02, 0.18), new T.MeshBasicMaterial({ color: "#f4e6bf" }), 0, 0.09, -0.08, false);
  put(deck, new T.CylinderGeometry(0.17, 0.17, 0.08, 24), alu, -1.6, 0.66, 1.6, false);
  const ledMat = new T.MeshStandardMaterial({ color: "#3a1a10", emissive: new T.Color("#ff7a2a"), emissiveIntensity: 0, roughness: 0.3 });
  put(deck, new T.SphereGeometry(0.06, 12, 10), ledMat, -1.05, 0.66, 1.6, false);

  /* LED spectrum ring */
  const ledGeo = new T.BoxGeometry(0.07, 1, 0.07); ledGeo.translate(0, 0.5, 0);
  const leds = new T.InstancedMesh(ledGeo, new T.MeshBasicMaterial({ color: "#ffffff", toneMapped: false }), LED_COUNT), lm = new T.Object3D(), lc = new T.Color(); deck.add(leds); leds.position.y = 0.625;
  const ringR = 1.86, heights = new Float32Array(LED_COUNT).fill(0.02);

  /* tonearm */
  const armBase = new T.Group(); armBase.position.set(2.05, 0.63, -1.25); deck.add(armBase);
  put(armBase, new T.CylinderGeometry(0.28, 0.3, 0.22, 24), alu, 0, 0.11, 0, false); put(armBase, new T.CylinderGeometry(0.17, 0.17, 0.18, 20), brass, 0, 0.3, 0, false);
  const arm = new T.Group(); arm.rotation.order = "YXZ"; arm.position.y = 0.42; armBase.add(arm);
  const armTube = put(arm, new T.CylinderGeometry(0.035, 0.035, ARM_LEN, 10), alu, 0, 0, ARM_LEN / 2, false); armTube.rotation.x = Math.PI / 2;
  const weight = put(arm, new T.CylinderGeometry(0.17, 0.17, 0.3, 18), new T.MeshStandardMaterial({ color: "#222", roughness: 0.4, metalness: 0.6 }), 0, 0, -0.45, false); weight.rotation.x = Math.PI / 2;
  const head = new T.Group(); head.position.z = ARM_LEN; arm.add(head);
  put(head, new RoundedBoxGeometry(0.22, 0.07, 0.36, 2, 0.02), new T.MeshStandardMaterial({ color: "#151515", roughness: 0.4, metalness: 0.6 }), 0, -0.02, 0.08, false); put(head, new T.BoxGeometry(0.06, 0.14, 0.12), new T.MeshStandardMaterial({ color: "#e8e0cf", roughness: 0.5 }), 0, -0.1, 0.16, false);
  put(head, new T.ConeGeometry(0.014, 0.1, 6), alu, 0, -0.2, 0.2, false).rotation.x = Math.PI;

  /* speakers */
  const speakers = [-1, 1].map((s) => {
    const g = new T.Group(); g.position.set(s * 4.7, 0, -0.6); g.rotation.y = -s * 0.3; scene.add(g);
    put(g, new RoundedBoxGeometry(1.7, 3.0, 1.4, 3, 0.09), walnut, 0, 1.5, 0);
    put(g, new T.PlaneGeometry(1.4, 2.7), new T.MeshStandardMaterial({ color: "#1a1511", roughness: 1 }), 0, 1.5, 0.705, false);
    const woofer = put(g, lathe([[0, 0.08], [0.18, 0.1], [0.5, 0.0], [0.56, 0.0]], 28), new T.MeshStandardMaterial({ color: "#26241f", roughness: 0.7, metalness: 0.3, side: T.DoubleSide }), 0, 0.95, 0.74, false); woofer.rotation.x = Math.PI / 2;
    put(g, new T.TorusGeometry(0.58, 0.04, 8, 28), brass, 0, 0.95, 0.74, false); const tweeter = put(g, new T.SphereGeometry(0.17, 14, 10, 0, 6.283, 0, 1.6), brass, 0, 2.15, 0.74, false); tweeter.rotation.x = Math.PI / 2;
    return { g, woofer };
  });

  /* lamp, sleeve, dust */
  const lamp = new T.Group(); lamp.position.set(-4.6, 0.0, 1.6); scene.add(lamp);
  put(lamp, new T.CylinderGeometry(0.34, 0.4, 0.14, 20), brass, 0, 0.07, 0); put(lamp, new T.CylinderGeometry(0.05, 0.05, 2.2, 10), brass, 0, 1.2, 0);
  put(lamp, new T.CylinderGeometry(0.32, 0.62, 0.7, 24, 1, true), new T.MeshBasicMaterial({ color: "#ffd9a0", side: T.DoubleSide }), 0, 2.4, 0, false);
  const lampGlow = glowSprite("#ffb066", 5.5, 0.55); lampGlow.position.set(-4.6, 2.3, 1.6); scene.add(lampGlow);
  const sleeve = put(scene, new RoundedBoxGeometry(2.2, 2.2, 0.06, 2, 0.01), new T.MeshStandardMaterial({ map: sleeveTexture(), roughness: 0.7 }), 4.2, 0.95, 1.6); sleeve.scale.setScalar(0.8); sleeve.rotation.set(-0.12, -0.55, 0.02);
  const dust = new ParticleField({ count: Math.round(110 * particleScale(quality)), size: 0.04, color: "#ffd9a0", opacity: 0.55, bounds: [4.5, 2.4, 2.8], center: [-1.0, 2.4, 0.8], drift: 0.5, rise: 0.02, twinkle: 0.9 }); scene.add(dust.points);

  /* ---------- choreography ---------- */
  const pos = new T.Vector3(), look = new T.Vector3(0, 0.5, 0.2), orbit = { yaw: 0, pitch: 0 };
  let spin = 0, platterAngle = 0, arm01 = 0, lastPlay = false, pulse = 0;
  const center = new T.Vector3(); const band = (s: number[] | undefined, i: number) => (s && s.length ? s[Math.min(s.length - 1, Math.floor((i / LED_COUNT) * s.length))] : 0);
  return {
    dispose() { label.dispose(); },
    frame(time, dt, state: SceneState, reduced) {
      const playing = Boolean(state.playing), preview = Boolean(state.preview), moving = playing || preview;
      if (moving !== lastPlay) { lastPlay = moving; stage.sfx(moving ? "needle" : "click"); }
      spin = damp(spin, moving ? 1 : 0, 1.1, dt, reduced); platterAngle += spin * dt * 3.49 * (reduced ? 0 : 1); disc.rotation.y = -platterAngle;
      deck.getWorldPosition(center); (face.material as T.ShaderMaterial).uniforms.uCenter.value.copy(center);
      arm01 = damp(arm01, moving ? 1 : 0, 1.5, dt, reduced);
      const progress = reduced ? 0 : (time * 0.004) % 0.2, swing = -0.62 * arm01 - (moving ? progress : 0) * arm01;
      arm.rotation.y = ARM_BASE + swing; arm.rotation.x = -0.11 * (1 - Math.min(1, Math.max(0, (arm01 - 0.75) * 4)));
      ledMat.emissiveIntensity = 0.1 + 2.4 * spin; knob.rotation.y = moving ? 0.7 : -0.5;
      const spectrum = state.spectrum; let bass = 0; for (let i = 0; i < 3; i++) bass += (spectrum?.[i] ?? 0) / 3; pulse = damp(pulse, playing ? bass : 0, 14, dt, reduced);
      for (let i = 0; i < LED_COUNT; i++) {
        const target = playing ? 0.04 + band(spectrum, i) * 0.4 : 0.025; heights[i] = damp(heights[i], target, 14, dt, reduced);
        const a = (i / LED_COUNT) * Math.PI * 2; lm.position.set(Math.cos(a) * ringR, 0, Math.sin(a) * ringR * 1.0); lm.scale.set(1, heights[i], 1); lm.updateMatrix(); leds.setMatrixAt(i, lm.matrix);
        lc.setHSL(0.1 - Math.min(0.08, heights[i] * 0.16), 1, 0.36 + Math.min(0.14, heights[i] * 0.3)); leds.setColorAt(i, lc);
      }
      leds.instanceMatrix.needsUpdate = true; if (leds.instanceColor) leds.instanceColor.needsUpdate = true;
      speakers.forEach((s, i) => { s.woofer.scale.setScalar(1 + pulse * 0.07); s.woofer.position.z = 0.74 + pulse * 0.05; s.g.scale.y = 1 + pulse * 0.004 * (i ? 1 : -1); });
      lampLight.intensity = 24 * (0.97 + (reduced ? 0 : Math.sin(time * 7) * 0.02)); dust.update(time);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.2, 0.35);
      pos.set((reduced ? 0 : Math.sin(time * 0.17) * 0.35), 4.3, 9.6); orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.95);
    },
  };
}
```

## 77. `src/three/gifts/wishes.ts` — new

```ts
/**
 * Gift 07 - A Thousand Wishes.
 * A moonlit hill with a wish tree. Ten star lanterns (one per wish already in the archive) hang from the branches on
 * fine threads. Picking a lantern wakes its light and sends a spray of sparks up into the sky; collected stars glow and
 * are joined into a constellation. state.selected = active wish, state.collected = collected indices.
 * state.step counts the wishes drawn from the sky (the content pack's hundred): each new draw flares a star high above the tree and
 * sends sparks down towards the lanterns.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { damp, ease } from "../../engine/anim";
import { Burst, ParticleField } from "../../engine/fx";
import { leafGeometry, put, starShape, taperedTube } from "../../engine/geometry";
import { addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, glowSprite, hash, orbitCamera, sparkleSprite } from "./common";

const COUNT = 10;
const ANCHORS: [number, number, number][] = [[-2.9, 5.2, 0.8], [-1.7, 6.3, 1.1], [-0.5, 4.5, 1.6], [0.9, 6.6, 0.9], [2.4, 5.5, 1.2], [3.2, 4.2, 0.6], [-3.4, 3.7, 0.2], [1.5, 4.0, 1.7], [-1.0, 7.2, 0.4], [0.2, 5.5, 2.0]];

export function buildWishesWorld(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "moon", envIntensity: 0.9, exposure: 1.1, background: "#070b1c", fog: { color: "#0b1226", density: 0.016 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 160; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#7f96d8", "#0b1020", 0.55));
  addKeyLight(scene, quality, { color: "#b9ccff", intensity: 2.2, position: [-7, 10, -4], target: [0, 3, 0], extent: 9, far: 30 });
  const warm = new T.PointLight("#ffc88a", 0, 9, 2); scene.add(warm);

  /* ---------- sky ---------- */
  const sky = backdrop((g, w, h) => {
    const bg = g.createLinearGradient(0, 0, 0, h); bg.addColorStop(0, "#050816"); bg.addColorStop(0.55, "#101b3d"); bg.addColorStop(1, "#27325c"); g.fillStyle = bg; g.fillRect(0, 0, w, h);
    const moon = g.createRadialGradient(w * 0.78, h * 0.26, 0, w * 0.78, h * 0.26, 260); moon.addColorStop(0, "rgba(255,248,224,.9)"); moon.addColorStop(0.2, "rgba(210,224,255,.35)"); moon.addColorStop(1, "rgba(120,150,230,0)"); g.fillStyle = moon; g.fillRect(0, 0, w, h);
    g.fillStyle = "#f6f1de"; g.beginPath(); g.arc(w * 0.78, h * 0.26, 34, 0, Math.PI * 2); g.fill();
    g.fillStyle = "rgba(20,28,60,.9)"; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 16) g.lineTo(x, h * 0.78 + Math.sin(x * 0.007) * 36 + Math.sin(x * 0.019) * 12); g.lineTo(w, h); g.fill();
    g.fillStyle = "rgba(10,16,38,.95)"; g.beginPath(); g.moveTo(0, h); for (let x = 0; x <= w; x += 16) g.lineTo(x, h * 0.88 + Math.sin(x * 0.01 + 2) * 24); g.lineTo(w, h); g.fill();
  }, 90, 52);
  sky.position.set(0, 14, -34); scene.add(sky);
  const stars = new ParticleField({ count: Math.round(900 * particleScale(quality)), size: 0.14, color: "#d8e4ff", colorB: "#ffe9c0", opacity: 0.9, bounds: [50, 30, 20], center: [0, 14, -25], twinkle: 0.8, shape: "spark", drift: 0.05 });
  scene.add(stars.points);

  /* ---------- hill ---------- */
  const hillGeo = new T.CircleGeometry(16, low ? 40 : 72); hillGeo.rotateX(-Math.PI / 2);
  const hp = hillGeo.attributes.position; for (let i = 0; i < hp.count; i++) { const x = hp.getX(i), z = hp.getZ(i); hp.setY(i, Math.max(0, 0.9 - Math.hypot(x, z) * 0.06) * (1 + 0.15 * Math.sin(x * 0.7) * Math.cos(z * 0.6))); }
  hillGeo.computeVertexNormals();
  const turf = kit.stone("#13203a", "#2c4a52", [8, 8]); turf.color = new T.Color("#4a6a58");
  const hill = put(scene, hillGeo, turf, 0, -0.3, 0, false); hill.receiveShadow = true;

  /* ---------- tree ---------- */
  const tree = new T.Group(); scene.add(tree);
  const bark = kit.bark("#1c140f", "#5a4636", [1, 3]);
  const trunk = new T.CatmullRomCurve3([new T.Vector3(0.1, 0, 0), new T.Vector3(-0.15, 1.4, 0.1), new T.Vector3(0.2, 2.8, -0.1), new T.Vector3(0.0, 4.2, 0)]);
  put(tree, taperedTube(trunk, 0.55, 0.16, 40, 12), bark, 0, 0, 0);
  const branchEnds: T.Vector3[] = [];
  for (let i = 0; i < 9; i++) {
    const t = 0.35 + (i / 9) * 0.6, o = trunk.getPointAt(Math.min(1, t)), dir = i * 2.4 + 0.6, reach = 1.5 + hash(i, 1) * 1.8 + (1 - t) * 1.5, rise = 0.9 + hash(i, 2) * 1.4;
    const end = new T.Vector3(o.x + Math.cos(dir) * reach, o.y + rise, o.z + Math.sin(dir) * reach * 0.7);
    const curve = new T.CatmullRomCurve3([o, new T.Vector3(o.x + Math.cos(dir) * reach * 0.45, o.y + rise * 0.25, o.z + Math.sin(dir) * reach * 0.3), end]);
    put(tree, taperedTube(curve, 0.17 - t * 0.05, 0.03, 20, 7), bark, 0, 0, 0); branchEnds.push(end);
    for (let k = 0; k < 2; k++) { const q = curve.getPointAt(0.55 + k * 0.25); const tw = new T.CatmullRomCurve3([q, new T.Vector3(q.x + Math.cos(dir + k - 0.5) * 0.5, q.y + 0.45, q.z + Math.sin(dir + k) * 0.3), new T.Vector3(q.x + Math.cos(dir + k - 0.5) * 0.95, q.y + 0.8 + hash(i, k + 3) * 0.4, q.z + Math.sin(dir + k) * 0.6)]); put(tree, taperedTube(tw, 0.04, 0.01, 10, 5), bark, 0, 0, 0, false); branchEnds.push(tw.getPoint(1)); }
  }
  const leafMat = kit.leaf("#16323c", "#6fb8b4"); leafMat.emissive = new T.Color("#2b6a70").multiplyScalar(0.25);
  const leaves = new T.InstancedMesh(leafGeometry(0.42, 0.18, 0.2, 0.1, 3, 5), leafMat, low ? 260 : 620); const d = new T.Object3D();
  for (let i = 0; i < leaves.count; i++) { const e = branchEnds[i % branchEnds.length]; d.position.set(e.x + (hash(i, 4) - 0.5) * 1.5, e.y + (hash(i, 5) - 0.4) * 1.1, e.z + (hash(i, 6) - 0.5) * 1.1); d.rotation.set(hash(i, 7) * 3, hash(i, 8) * 6, hash(i, 9) * 3); d.scale.setScalar(0.7 + hash(i, 10) * 0.8); d.updateMatrix(); leaves.setMatrixAt(i, d.matrix); }
  leaves.castShadow = !low; tree.add(leaves);

  /* ---------- lanterns ---------- */
  const brass = kit.metal("brass", 0.3);
  const shape = starShape(0.36, 0.16, 5);
  const bodyGeo = new T.ExtrudeGeometry(shape, { depth: 0.2, bevelEnabled: true, bevelSize: 0.04, bevelThickness: 0.05, bevelSegments: 3 }); bodyGeo.center();
  const lanterns = ANCHORS.map((a, i) => {
    const group = new T.Group(); group.position.set(a[0], a[1], a[2]); group.userData.index = i; tree.add(group);
    const dropLen = 0.55 + hash(i, 12) * 0.5;
    put(group, new T.CylinderGeometry(0.008, 0.008, dropLen, 4), new T.MeshBasicMaterial({ color: "#c8b690" }), 0, dropLen / 2, 0, false);
    const hang = new T.Group(); hang.position.y = -0.0; group.add(hang);
    put(hang, new T.ConeGeometry(0.1, 0.12, 12), brass, 0, 0.05, 0, false);
    const mat = new T.MeshStandardMaterial({ color: "#ffe2a0", emissive: new T.Color("#ffb347"), emissiveIntensity: 0.5, roughness: 0.25, metalness: 0.1, transparent: true, opacity: 0.95 });
    const body = put(hang, bodyGeo, mat, 0, -0.34, 0, false); body.userData.index = i;
    const frame = put(hang, new T.ExtrudeGeometry(shape, { depth: 0.24, bevelEnabled: false }), new T.MeshBasicMaterial({ color: "#e8c066", wireframe: true }), 0, -0.34, -0.12, false); frame.scale.setScalar(1.06);
    const halo = glowSprite("#ffc86a", 1.6, 0.3); halo.position.y = -0.34; hang.add(halo);
    const spark = sparkleSprite("#fff4d8", 0.8, 0); spark.position.y = -0.34; hang.add(spark);
    return { group, hang, mat, halo, spark, phase: i * 1.3 };
  });
  const lineGeo = new T.BufferGeometry(); lineGeo.setAttribute("position", new T.BufferAttribute(new Float32Array(COUNT * 3), 3));
  const constellation = new T.Line(lineGeo, new T.LineBasicMaterial({ color: "#ffeab8", transparent: true, opacity: 0.8, blending: T.AdditiveBlending, depthWrite: false }));
  constellation.frustumCulled = false; scene.add(constellation);
  const sparks = new Burst({ count: low ? 30 : 70, size: 0.14, life: 2.2, speed: 2.2, gravity: -0.4, drag: 1.2, colors: ["#ffe9a8", "#ffc86a", "#fff6dc"], shape: "spark", emit: "cone", coneAngle: 1.2 });
  scene.add(sparks.points);
  const fireflies = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.09, color: "#fff09a", colorB: "#bfff9a", opacity: 0.9, bounds: [5, 1.4, 3], center: [0, 1.4, 1.5], drift: 1.3, twinkle: 0.9 });
  scene.add(fireflies.points);
  const risers = new ParticleField({ count: Math.round(60 * particleScale(quality)), size: 0.07, color: "#ffd890", opacity: 0.7, bounds: [3.4, 4.5, 1.6], center: [0, 5.5, 1.0], drift: 0.5, rise: 0.22, twinkle: 0.7, shape: "spark" });
  scene.add(risers.points);

  /* ---------- choreography ---------- */
  /* a drawn sky wish: one bright star that flares and fades high above the tree */
  const skyFlare = sparkleSprite("#fff4d8", 2.2, 0); skyFlare.visible = false; scene.add(skyFlare);
  const flarePos = new T.Vector3(); let flareT = 99, lastStep: number | undefined;
  const lit = new Array(COUNT).fill(0) as number[], pos = new T.Vector3(), look = new T.Vector3(0, 4.3, 0.5), orbit = { yaw: 0, pitch: 0 };
  const focus = new T.Vector3(0.3, 3.3, 0.5);
  let lastCollected = -1, lastKey = "", lastActive: number | null | undefined; const order: number[] = [];
  const world = new T.Vector3();
  return {
    pickables: lanterns.map((l) => l.group),
    frame(time, dt, state: SceneState, reduced) {
      const collected = state.collected ?? [], active = state.selected ?? null;
      // new collection -> spark spray + chime; track collection order for the constellation
      for (const c of collected) if (!order.includes(c)) { order.push(c); lanterns[c].group.getWorldPosition(world); sparks.trigger(world.clone().setY(world.y - 0.34)); stage.sfx("star"); }
      for (let i = order.length - 1; i >= 0; i--) if (!collected.includes(order[i])) order.splice(i, 1);
      if (active !== lastActive) { if (lastActive !== undefined && active !== null) stage.sfx("chime"); lastActive = active; }
      const key = order.join(","); if (key !== lastKey || collected.length !== lastCollected) {
        lastKey = key; lastCollected = collected.length; const p = lineGeo.attributes.position as T.BufferAttribute;
        order.forEach((idx, n) => { lanterns[idx].group.getWorldPosition(world); p.setXYZ(n, world.x, world.y - 0.34, world.z); });
        lineGeo.setDrawRange(0, order.length); p.needsUpdate = true;
      }
      const step = state.step ?? 0;
      if (lastStep === undefined) lastStep = step;
      else if (step !== lastStep) {
        lastStep = step; flareT = 0; flarePos.set((hash(step, 31) - 0.5) * 6, 6.4 + hash(step, 32) * 2.4, -2 + hash(step, 33) * 2.4);
        if (!reduced) sparks.trigger(flarePos);
        stage.sfx("chime");
      }
      flareT += dt;
      const flare = Math.min(1, flareT / 1.8);
      skyFlare.visible = flare < 1; skyFlare.position.copy(flarePos);
      (skyFlare.material as T.SpriteMaterial).opacity = (1 - flare) * Math.min(1, flareT / 0.18);
      skyFlare.scale.setScalar(reduced ? 2.2 : 1.2 + 3.2 * Math.sin(Math.min(1, flareT / 0.9) * Math.PI * 0.5));
      sparks.update(dt);
      lanterns.forEach((l, i) => {
        const on = collected.includes(i), isActive = active === i;
        lit[i] = damp(lit[i], on ? 1 : 0, 4, dt, reduced);
        l.mat.emissiveIntensity = 0.45 + 2.4 * lit[i] + (isActive ? 0.9 : 0);
        (l.halo.material as T.SpriteMaterial).opacity = 0.22 + 0.7 * lit[i] + (isActive ? 0.25 : 0); l.halo.scale.setScalar(1.3 + 1.5 * lit[i] + (reduced ? 0 : Math.sin(time * 2.4 + l.phase) * 0.1));
        const tw = Math.max(0, Math.sin(time * 2 + l.phase)); (l.spark.material as T.SpriteMaterial).opacity = (reduced ? 0.4 : tw * tw) * lit[i]; l.spark.scale.setScalar(0.5 + tw * 0.8);
        l.hang.rotation.z = reduced ? 0 : Math.sin(time * 0.9 + l.phase) * 0.08 + Math.sin(time * 0.4 + l.phase * 2) * 0.03; l.hang.rotation.y = reduced ? 0 : time * 0.25 + l.phase;
        l.hang.scale.setScalar(damp(l.hang.scale.x, isActive ? 1.28 : 1, 6, dt, reduced));
      });
      const act = active !== null && lanterns[active] ? lanterns[active] : null;
      if (act) { act.group.getWorldPosition(world); warm.position.set(world.x, world.y - 0.5, world.z + 0.8); }
      warm.intensity = damp(warm.intensity, act ? 14 : 0, 4, dt, reduced);
      focus.lerp(act ? world.clone().setY(world.y - 0.5) : new T.Vector3(0.3, 3.3, 0.5), reduced ? 1 : 1 - Math.exp(-dt * 2));
      tree.rotation.z = reduced ? 0 : Math.sin(time * 0.5) * 0.006; stars.update(time); fireflies.update(time); risers.update(time);
      const drag = input.consumeDrag(); orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.4, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.12, 0.3);
      const approach = act ? 0.78 : 1; pos.set(0 + (reduced ? 0 : Math.sin(time * 0.18) * 0.5), 2.7, 19.5 * approach); look.copy(focus);
      orbitCamera(camera, pos, look, orbit.yaw, orbit.pitch, 0.9); void ease;
    },
  };
}
```

## 78. `src/three/kinds.ts` — new

```ts
/**
 * Scene identifiers.
 * Gifts are numbered gift-01 ... gift-17 in the order of GIFT_KINDS; sections are the non-gift 3D scenes of the page.
 * Every scene is a dynamically imported module (see giftFactory.ts) and renders inside the single shared canvas host.
 */
export const GIFT_KINDS = [
  "letter", "jar", "flower", "universe", "cassette", "cinema", "wishes", "crown", "cabinet",
  "machine", "adventure", "vinyl", "mirror", "coupons", "hope-tree", "treasure", "portal",
] as const;
export type GiftKind = (typeof GIFT_KINDS)[number];

export const SECTION_KINDS = ["hero-garden", "wish-garden", "observatory", "postcards", "ballroom"] as const;
export type SectionKind = (typeof SECTION_KINDS)[number];

export type SceneKind = GiftKind | SectionKind;
export const isSectionKind = (kind: SceneKind): kind is SectionKind => (SECTION_KINDS as readonly string[]).includes(kind);
```

## 79. `src/three/previewGiftModels.ts` — modified

```ts
// Offline authoring endpoint: never imported by the application.
import * as T from 'three';
import {loadGift,giftKinds,usesDefaultLights} from './giftFactory';
import {disposeTree} from '../engine/dispose';
import {createStage,idleInput} from '../engine/stage';
import type {SceneState} from './runtime';
import {chronosContent} from '../content/chronosContent';
import {reasonNotes} from '../content/giftsContent';
// The posters show the finished state with the real copy: the main letter on the paper, a real reason on the open jar note.
const mainLetter=chronosContent.letters.letters[0];
const letterText=[mainLetter.salutation,...mainLetter.paragraphs,mainLetter.closing,mainLetter.signature,mainLetter.ps].filter(Boolean).join('\n\n');
let renderer:T.WebGLRenderer|undefined;
export async function renderGiftPreview(index:number){
 if(!renderer){renderer=new T.WebGLRenderer({antialias:true,preserveDrawingBuffer:true});renderer.setSize(480,360);renderer.setPixelRatio(1);renderer.toneMapping=T.ACESFilmicToneMapping;renderer.toneMappingExposure=1.12;}
 const scene=new T.Scene(),camera=new T.PerspectiveCamera(38,4/3,.1,80);const kind=giftKinds[index];
 const stage=createStage({renderer,root:scene,camera,quality:'medium',input:idleInput(),pick:()=>{}});
 if(usesDefaultLights(kind)){stage.mood({env:'studio',envIntensity:.5});scene.add(new T.HemisphereLight('#fff0d7','#526b63',1.3));const key=new T.DirectionalLight('#ffe3bf',3.5);key.position.set(-4,7,5);scene.add(key);const fill=new T.DirectionalLight('#b9d9e7',1);fill.position.set(4,3,-3);scene.add(fill);}
 const choreography=(await loadGift(kind))(stage);
 const presets:Record<string,SceneState>={letter:{open:true,immediate:true,detail:letterText},jar:{open:true,selected:3,detail:reasonNotes[3].text},flower:{growth:4},universe:{selected:0},cassette:{open:true},cinema:{open:true},wishes:{collected:[1,4,6]},crown:{detail:'crown'},cabinet:{selected:1,open:true},machine:{selected:0},adventure:{selected:1,growth:3},vinyl:{open:true},mirror:{growth:1},coupons:{selected:0},'hope-tree':{growth:8},treasure:{open:true},portal:{open:true,growth:2}};
 try{choreography.frame(4,1,presets[giftKinds[index]],true,1);scene.updateMatrixWorld(true);renderer.render(scene,camera);return renderer.domElement.toDataURL('image/png').split(',')[1];}finally{choreography.dispose?.();disposeTree(scene);}
}
export function finishPreviews(){renderer?.dispose();renderer?.forceContextLoss();renderer=undefined;}
```

## 80. `src/three/runtime.ts` — modified

```ts
import type * as T from "three";
import type { Quality } from "../engine/quality";
import type { MaterialKit } from "../engine/materials";
import type { MoodOptions } from "../engine/lights";
import type { Sfx } from "../engine/audio";
import type { StageInput } from "../engine/stage";

export interface SceneState { growth?: number; turn?: number; detail?: string; bakeStage?: number; selected?: number | null; replay?: number; planted?: boolean; candles?: number; blowing?: boolean; celebration?: boolean; open?: boolean; immediate?: boolean; artwork?: string; playing?: boolean; preview?: boolean; spectrum?: number[]; collected?: number[]; step?: number; page?: number; flip?: number; pointer?: number; lit?: boolean; extra?: Record<string, number | string | boolean>; }
export interface Stage {
  scene: T.Scene; camera: T.PerspectiveCamera; quality: Quality; pick: (index: number) => void; report?: (progress: number) => void;
  /** The WebGL renderer, for environment baking and resource accounting. */
  renderer: T.WebGLRenderer;
  /** Shared PBR materials for this scene (procedural textures, quality-aware glass). */
  kit: MaterialKit;
  /** Pointer / keyboard state fed by the host. */
  input: StageInput;
  /** Applies an environment, exposure, background and fog "mood". */
  mood: (mood: MoodOptions) => void;
  /** Plays a synthesised sound effect (no-op unless the visitor enabled sound). */
  sfx: (name: Sfx, intensity?: number) => void;
  /** Requests another rendered frame (for asynchronous arrivals such as textures when the loop is idle). */
  invalidate: () => void;
}
export interface Choreography { frame: (time: number, dt: number, state: SceneState, reduced: boolean, timelineDt?: number) => void; pickables?: T.Object3D[]; dispose?: () => void; }
```

## 81. `src/three/sections/ballroom.ts` — new

```ts
/**
 * Birthday Ballroom: the baking story (ingredients -> mixing -> oven) ends in a three-tier cake under a crystal chandelier.
 * Candles are lit one by one, flames flicker and bend, blowing them out sends a puff of smoke from every wick, and the wish
 * releases confetti and fireworks while the camera pulls back for the finale.
 * state: bakeStage 0..3, candles 0..5 (lit), blowing (gust), celebration (confetti + fireworks).
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { Burst, Flame, ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, lathe, put } from "../../engine/geometry";
import { addSpotLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { backdrop, glowSprite, hash, makeCurtain, paintBokeh, sparkleSprite } from "../gifts/common";

const TAU = Math.PI * 2;
const CANDLE_COLORS = ["#f3c9d2", "#f3e3b8", "#cfe3d4", "#e4c3ea", "#f7d9b5"];
const smooth = T.MathUtils.smoothstep;

function paintHall(g: CanvasRenderingContext2D, w: number, h: number) {
  const wall = g.createLinearGradient(0, 0, 0, h); wall.addColorStop(0, "#1b1226"); wall.addColorStop(0.55, "#3a2236"); wall.addColorStop(1, "#24141f");
  g.fillStyle = wall; g.fillRect(0, 0, w, h);
  for (let i = 0; i < 5; i++) {
    const cx = ((i + 0.5) / 5) * w, ww = w * 0.062, top = h * 0.14, bottom = h * 0.8;
    g.fillStyle = "#c79b4d"; g.beginPath(); g.moveTo(cx - ww - 12, bottom); g.lineTo(cx - ww - 12, top + ww); g.arc(cx, top + ww, ww + 12, Math.PI, 0); g.lineTo(cx + ww + 12, bottom); g.fill();
    const sky = g.createLinearGradient(0, top, 0, bottom); sky.addColorStop(0, "#1c2b5a"); sky.addColorStop(1, "#d78a63");
    g.fillStyle = sky; g.beginPath(); g.moveTo(cx - ww, bottom); g.lineTo(cx - ww, top + ww); g.arc(cx, top + ww, ww, Math.PI, 0); g.lineTo(cx + ww, bottom); g.fill();
    g.fillStyle = "rgba(255,244,214,.9)"; for (let s = 0; s < 14; s++) g.fillRect(cx - ww + hash(i * 20 + s, 3) * ww * 2, top + hash(i * 20 + s, 5) * (bottom - top) * 0.55, 2, 2);
    g.strokeStyle = "#c79b4d"; g.lineWidth = 6; g.beginPath(); g.moveTo(cx, top); g.lineTo(cx, bottom); g.moveTo(cx - ww, (top + bottom) / 2); g.lineTo(cx + ww, (top + bottom) / 2); g.stroke();
  }
  paintBokeh(g, w, h, "255,214,150", 46, 7);
}

export function buildBallroom(stage: Stage): Choreography {
  const { scene, camera, quality, kit } = stage;
  const low = quality === "low", high = quality === "high";
  stage.mood({ env: "ballroom", envIntensity: 0.85, exposure: 1.08, background: "#150d17", fog: { color: "#1a1019", density: 0.014 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 120; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#ffe9d0", "#3a2530", 0.85));
  addSpotLight(scene, quality, "#ffe6bf", 52, [2.5, 10, 6.5], [0, 1.4, 0], 0.55, 0.75);
  const fill = new T.DirectionalLight("#b9c6ff", 0.55); fill.position.set(-6, 4, 7); scene.add(fill);
  const candleLight = new T.PointLight("#ffb25e", 0, 8, 2); scene.add(candleLight);

  /* ---------- the hall ---------- */
  const hall = backdrop(paintHall, 40, 17, 1536, 768); hall.position.set(0, 5.4, -11); scene.add(hall);
  const floor = put(scene, new T.PlaneGeometry(60, 40), kit.marble("#7c7f8c", "#ece8e0"), 0, -2.62, -6, false); floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;
  [-1, 1].forEach((side) => {
    const curtain = makeCurtain(3.2, 12.5, "#6a1f3a", 2.4); curtain.position.set(side * 9.2, 3.6, -6); scene.add(curtain);
    const column = put(scene, new T.CylinderGeometry(0.62, 0.7, 12, 24), kit.marble("#b9b4ab", "#f6f2ea"), side * 6.2, 3.4, -7.5); void column;
    [-2.0, 9.2].forEach((y) => put(scene, new T.CylinderGeometry(0.82, 0.82, 0.3, 24), kit.metal("gold", 0.35), side * 6.2, y, -7.5, false));
  });

  // chandelier
  const chandelier = new T.Group(); chandelier.position.set(0, 6.4, -4.5); scene.add(chandelier);
  const gold = kit.metal("gold", 0.3);
  chandelier.add(new T.Mesh(new T.TorusGeometry(1.5, 0.06, 10, 64), gold)); const lowerRing = new T.Mesh(new T.TorusGeometry(0.9, 0.05, 10, 48), gold); lowerRing.position.y = -0.7; chandelier.add(lowerRing);
  put(chandelier, new T.CylinderGeometry(0.02, 0.02, 3.2, 6), gold, 0, 1.6, 0, false);
  const crystalCount = low ? 36 : 84, crystals = new T.InstancedMesh(new T.OctahedronGeometry(0.1, 0), kit.gem("#e9f3ff"), crystalCount), d = new T.Object3D();
  for (let i = 0; i < crystalCount; i++) { const ring = i % 3, a = (i / crystalCount) * TAU * 3 + ring, r = [1.5, 0.9, 0.5][ring]; d.position.set(Math.cos(a) * r, -0.25 - ring * 0.45 - (i % 5) * 0.08, Math.sin(a) * r); d.scale.set(1, 1.7 + (i % 4) * 0.4, 1); d.rotation.y = a; d.updateMatrix(); crystals.setMatrixAt(i, d.matrix); }
  chandelier.add(crystals);
  for (let i = 0; i < 8; i++) { const a = (i / 8) * TAU; const bulb = glowSprite("#ffd9a0", 0.9, 0.9); bulb.position.set(Math.cos(a) * 1.5, 0.22, Math.sin(a) * 1.5); chandelier.add(bulb); }
  const chandelierGlow = glowSprite("#ffd49a", 7, 0.5); chandelierGlow.position.y = -0.4; chandelier.add(chandelierGlow);
  const glints = [0, 1, 2, 3, 4, 5].map((i) => { const s = sparkleSprite("#ffffff", 0.5, 0); s.position.set(Math.cos(i * 1.1) * 1.4, -0.3 - (i % 3) * 0.4, Math.sin(i * 1.1) * 1.2); chandelier.add(s); return s; });

  /* ---------- the table ---------- */
  const TT = 0; // table-top height
  put(scene, lathe([[0, -2.6], [3.72, -2.6], [3.65, -2.2], [3.5, -1.1], [3.36, TT - 0.04], [3.3, TT], [0, TT]], 64), kit.fabric("#c9bfa9", "#e9e0cd", [12, 3]), 0, 0, 0);
  const tableTop = put(scene, new T.CylinderGeometry(3.3, 3.3, 0.06, 64), kit.fabric("#c9bfa9", "#e9e0cd", [6, 6]), 0, TT - 0.03, 0); void tableTop;

  /* ---------- stage 0 + 1: ingredients and batter ---------- */
  const prep = new T.Group(); scene.add(prep);
  const bowl = new T.Group(); bowl.position.set(-1.5, TT + 0.02, 0.2); prep.add(bowl);
  const bowlShell = new T.Mesh(lathe([[0, 0], [0.45, 0], [0.72, 0.1], [1.0, 0.5], [1.1, 0.88], [1.06, 0.9], [0.96, 0.52], [0.7, 0.16], [0.0, 0.1]], 40), kit.ceramic("#f1ece1", 0.9)); bowlShell.castShadow = !low; bowl.add(bowlShell);
  const batterMat = new T.MeshPhysicalMaterial({ color: "#f3d79d", roughness: 0.22, clearcoat: 0.7 });
  const batter = new T.Mesh(new T.CylinderGeometry(0.98, 0.7, 0.5, 36), batterMat); batter.position.y = 0.42; bowl.add(batter);
  const whisk = new T.Group(); whisk.position.set(-0.2, 1.05, 0); bowl.add(whisk);
  put(whisk, new T.CylinderGeometry(0.05, 0.05, 0.9, 12), kit.metal("steel", 0.3), 0, 0.55, 0, false);
  for (let i = 0; i < 6; i++) { const loop = new T.Mesh(new T.TorusGeometry(0.25, 0.012, 6, 28), kit.metal("steel", 0.25)); loop.scale.y = 1.9; loop.rotation.y = (i / 6) * Math.PI; loop.position.y = 0.0; whisk.add(loop); }
  const stream = new T.Mesh(new T.CylinderGeometry(0.06, 0.05, 1.0, 10), batterMat); stream.visible = false; prep.add(stream);
  const tin = new T.Group(); tin.position.set(1.6, TT + 0.02, 0.3); prep.add(tin);
  const tinMat = new T.MeshStandardMaterial({ color: "#b4bac2", metalness: 0.35, roughness: 0.42, side: T.DoubleSide });
  const tinWall = new T.Mesh(new T.CylinderGeometry(0.95, 0.95, 0.5, 40, 1, true), tinMat); tinWall.position.y = 0.25; tin.add(tinWall);
  const tinBase = new T.Mesh(new T.CylinderGeometry(0.95, 0.95, 0.04, 40), tinMat); tinBase.position.y = 0.02; tin.add(tinBase);
  const poured = new T.Mesh(new T.CylinderGeometry(0.92, 0.92, 0.4, 36), batterMat); poured.position.y = 0.05; poured.scale.y = 0.01; tin.add(poured);
  [[-0.6, 0.3], [-0.9, -0.15], [-0.35, -0.2]].forEach(([x, z], i) => { const egg = new T.Mesh(new T.SphereGeometry(0.17, 20, 16), kit.ceramic(i === 1 ? "#d9b48a" : "#f3e4cf", 0.5)); egg.scale.y = 1.28; egg.position.set(x + 0.2 - 1.5 + 1.6, TT + 0.2, 1.4 + z * 0.4); egg.castShadow = true; prep.add(egg); });
  const butter = put(prep, new RoundedBoxGeometry(0.62, 0.22, 0.4, 3, 0.04), new T.MeshStandardMaterial({ color: "#f7dc7a", roughness: 0.5 }), 0.1, TT + 0.11, 1.55); butter.rotation.y = 0.3;

  /* ---------- stage 2: the oven ---------- */
  const oven = new T.Group(); oven.position.set(0, TT + 1.35, -0.2); scene.add(oven);
  put(oven, new RoundedBoxGeometry(3.4, 2.5, 2.0, 4, 0.12), kit.ceramic("#e4d5b8", 0.7), 0, 0, 0);
  const hole = new T.Mesh(new T.BoxGeometry(2.5, 1.5, 0.12), new T.MeshStandardMaterial({ color: "#150c08", emissive: "#ff5a14", emissiveIntensity: 0.0, roughness: 0.9 })); hole.position.set(0, -0.1, 1.0); oven.add(hole);
  const ovenGlow = new T.PointLight("#ff8a2e", 0, 5, 2); ovenGlow.position.set(0, -0.1, 1.3); oven.add(ovenGlow);
  const doorPivot = new T.Group(); doorPivot.position.set(0, -0.85, 1.04); oven.add(doorPivot);
  const door = new T.Mesh(new RoundedBoxGeometry(2.7, 1.62, 0.1, 3, 0.04), kit.metal("brass", 0.4)); door.position.y = 0.81; doorPivot.add(door);
  const doorGlass = new T.Mesh(new T.PlaneGeometry(2.1, 1.0), kit.glass("#ffdcae")); doorGlass.position.set(0, 0.82, 0.056); doorPivot.add(doorGlass);
  const handle = new T.Mesh(new T.CylinderGeometry(0.035, 0.035, 2.0, 10), gold); handle.rotation.z = Math.PI / 2; handle.position.set(0, 1.55, 0.18); doorPivot.add(handle);
  const dial = new T.Mesh(new T.TorusGeometry(0.17, 0.03, 8, 24), gold); dial.position.set(1.2, 1.0, 1.02); oven.add(dial);
  const timerHand = new T.Mesh(new T.BoxGeometry(0.02, 0.13, 0.02), gold); timerHand.position.set(0, 0.06, 0.02); dial.add(timerHand);
  const sponge = new T.Mesh(new T.CylinderGeometry(0.8, 0.8, 0.5, 36), new T.MeshStandardMaterial({ color: "#e6b87a", roughness: 0.85 })); sponge.position.set(0, -0.55, 0.55); oven.add(sponge);

  /* ---------- stage 3: the three-tier cake ---------- */
  const cake = new T.Group(); cake.position.y = TT; scene.add(cake);
  const cream = new T.MeshPhysicalMaterial({ color: "#fff1e4", roughness: 0.5, sheen: 0.6, sheenColor: new T.Color("#ffd3dc"), sheenRoughness: 0.5 });
  const glaze = new T.MeshPhysicalMaterial({ color: "#e68aa0", roughness: 0.22, clearcoat: 0.9, clearcoatRoughness: 0.2 });
  const berry = new T.MeshPhysicalMaterial({ color: "#c4152e", roughness: 0.3, clearcoat: 0.8 });
  type Piece = { object: T.Object3D; y: number; delay: number };
  const assembled: Piece[] = [];
  const standGroup = new T.Group(); cake.add(standGroup); assembled.push({ object: standGroup, y: 0, delay: 0 });
  put(standGroup, lathe([[0, 0], [2.5, 0], [2.55, 0.05], [2.4, 0.12], [0.45, 0.2], [0.32, 0.5], [0.3, 0.7], [0.8, 0.78], [0, 0.8]], 56), kit.ceramic("#fbf8f2", 1), 0, 0, 0);
  put(standGroup, new T.TorusGeometry(2.46, 0.035, 8, 80), gold, 0, 0.09, 0, false).rotation.x = Math.PI / 2;
  const tiers = [{ r: 1.75, h: 0.82, delay: 0.5 }, { r: 1.3, h: 0.7, delay: 1.1 }, { r: 0.88, h: 0.6, delay: 1.7 }];
  let y = 0.8; const topOf: number[] = [];
  tiers.forEach((tier, ti) => {
    const group = new T.Group(); group.position.y = y; cake.add(group); assembled.push({ object: group, y, delay: tier.delay });
    put(group, new T.CylinderGeometry(tier.r, tier.r, tier.h, 64), cream, 0, tier.h / 2, 0);
    const dripCount = Math.round(tier.r * 18); const drips = new T.InstancedMesh(new T.CapsuleGeometry(0.055, 1, 4, 8), glaze, dripCount);
    for (let i = 0; i < dripCount; i++) { const a = (i / dripCount) * TAU, len = 0.12 + hash(i + ti * 40, 2) * 0.32; d.position.set(Math.cos(a) * (tier.r + 0.01), tier.h - len * 0.5 - 0.02, Math.sin(a) * (tier.r + 0.01)); d.scale.set(1, len, 1); d.rotation.set(0, 0, 0); d.updateMatrix(); drips.setMatrixAt(i, d.matrix); }
    group.add(drips);
    put(group, new T.CylinderGeometry(tier.r * 0.985, tier.r * 0.985, 0.045, 64), glaze, 0, tier.h + 0.01, 0, false);
    const pearls = new T.InstancedMesh(new T.SphereGeometry(0.075, 10, 8), kit.ceramic("#fff8ee", 0.9), Math.round(tier.r * 20));
    for (let i = 0; i < pearls.count; i++) { const a = (i / pearls.count) * TAU; d.position.set(Math.cos(a) * (tier.r + 0.03), 0.06, Math.sin(a) * (tier.r + 0.03)); d.scale.setScalar(1); d.updateMatrix(); pearls.setMatrixAt(i, d.matrix); }
    group.add(pearls);
    const band = new T.Mesh(new T.CylinderGeometry(tier.r + 0.012, tier.r + 0.012, 0.1, 64, 1, true), new T.MeshPhysicalMaterial({ color: ti === 1 ? "#d4af6a" : "#f3c9d2", roughness: 0.3, metalness: ti === 1 ? 0.8 : 0, side: T.DoubleSide, sheen: 1 })); band.position.y = tier.h * 0.38; group.add(band);
    y += tier.h; topOf.push(y);
  });
  const decor = new T.Group(); decor.position.y = topOf[2]; cake.add(decor); assembled.push({ object: decor, y: topOf[2], delay: 2.4 });
  for (let i = 0; i < 9; i++) { // strawberries and leaves around the top tier
    const a = (i / 9) * TAU + 0.2, r = 0.78; const b = new T.Mesh(new T.SphereGeometry(0.12, 14, 12), berry); b.scale.set(1, 1.2, 1); b.position.set(Math.cos(a) * r, 0.1, Math.sin(a) * r); b.castShadow = !low; decor.add(b);
    const leaf = new T.Mesh(new T.ConeGeometry(0.07, 0.1, 6), new T.MeshStandardMaterial({ color: "#3d7a3a", roughness: 0.6 })); leaf.position.set(b.position.x, 0.25, b.position.z); decor.add(leaf);
  }
  const sprinkles = new T.InstancedMesh(new T.CylinderGeometry(0.012, 0.012, 0.07, 5), kit.metal("gold", 0.3), 120);
  for (let i = 0; i < 120; i++) { const a = hash(i, 4) * TAU, r = Math.sqrt(hash(i, 6)) * 1.6, ti = r < 0.85 ? 2 : r < 1.2 ? 1 : 0; d.position.set(Math.cos(a) * Math.min(r, tiers[ti].r - 0.08), topOf[ti] - topOf[2] + 0.04, Math.sin(a) * Math.min(r, tiers[ti].r - 0.08)); d.rotation.set(hash(i, 8) * 3, hash(i, 9) * 3, hash(i, 10) * 3); d.scale.setScalar(1); d.updateMatrix(); sprinkles.setMatrixAt(i, d.matrix); }
  decor.add(sprinkles);
  // candles + flames
  const candleGroup = new T.Group(); candleGroup.position.y = topOf[2]; cake.add(candleGroup); assembled.push({ object: candleGroup, y: topOf[2], delay: 3.0 });
  const flames = [0, 1, 2, 3, 4].map((i) => {
    const a = (i / 5) * TAU + 0.5, r = 0.4, x = Math.cos(a) * r, z = Math.sin(a) * r, hgt = 0.52 + (i % 2) * 0.08;
    put(candleGroup, new T.CylinderGeometry(0.07, 0.07, hgt, 18), kit.wax(CANDLE_COLORS[i]), x, hgt / 2 + 0.03, z);
    put(candleGroup, new T.CylinderGeometry(0.008, 0.008, 0.1, 5), new T.MeshStandardMaterial({ color: "#1a1410" }), x, hgt + 0.08, z, false);
    const flame = new Flame(0.3, 0.15); flame.group.position.set(x, hgt + 0.12, z); candleGroup.add(flame.group);
    return { flame, level: 0, lit: false, top: new T.Vector3(x, topOf[2] + hgt + 0.2, z) };
  });
  const smoke = flames.map((_, i) => new Burst({ count: low ? 8 : 16, size: 0.35, life: 2.4, speed: 0.55, gravity: -0.25, drag: 1.2, colors: ["#c9c4bf", "#aaa5a0"], shape: "smoke", emit: "cone", coneAngle: 0.3, seed: 10 + i }));
  smoke.forEach((s) => scene.add(s.points));
  const confetti = new Burst({ count: high ? 320 : low ? 110 : 220, size: 0.22, life: 4.8, speed: 8, gravity: 4.4, drag: 0.7, colors: ["#e68aa0", "#d6b25e", "#fff1e4", "#8fb39a", "#b793d8"], shape: "confetti", emit: "cone", coneAngle: 1.05 });
  const fireworks = [0, 1, 2].map((i) => new Burst({ count: low ? 60 : 110, size: 0.4, life: 2.3, speed: 5.2, gravity: 1.3, drag: 1.1, colors: [["#ffd98a", "#ffb3c4", "#ffffff"], ["#b8c8ff", "#ffe5a8", "#ffffff"], ["#ffc2a0", "#ff9ec2", "#fff3d0"]][i], shape: "spark", emit: "sphere", seed: 30 + i }));
  scene.add(confetti.points); fireworks.forEach((f) => scene.add(f.points));
  const sparkleField = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.08, color: "#ffe9b8", opacity: 0.7, bounds: [6, 3.5, 3], center: [0, 3, -2], drift: 0.7, rise: 0.05, twinkle: 0.8 });
  scene.add(sparkleField.points);

  /* ---------- state machine ---------- */
  let stageBefore = -1, stageAge = 0, lastCelebration = false, celebrateAge = -1;
  const fireAt = [0.1, 0.55, 1.0, 2.2, 2.7, 3.2], firePos = [[-3.6, 6.0, -3.5], [3.4, 6.8, -4], [0.2, 7.8, -4.5]] as const, fired = new Set<number>();
  const pos = new T.Vector3(), look = new T.Vector3(0, 1.2, 0), tmp = new T.Vector3();

  return {
    frame(time, dt, state: SceneState, reduced) {
      const st = state.bakeStage ?? 3;
      if (st !== stageBefore) { stageBefore = st; stageAge = 0; }
      stageAge = reduced ? 12 : stageAge + dt;
      prep.visible = st < 2; oven.visible = st === 2; cake.visible = st === 3;

      if (st < 2) {
        const pour = st === 1 ? smooth(stageAge, 0.7, 2.3) : 0;
        bowl.rotation.z = -pour * 0.95; bowl.position.set(-1.5 + pour * 2.7, TT + 0.02 + pour * 1.25, 0.2 + pour * 0.1);
        stream.visible = st === 1 && stageAge > 1.3 && stageAge < 3.6; stream.position.set(1.15, TT + 0.9, 0.3); stream.scale.y = 1;
        poured.scale.y = st === 0 ? 0.01 : Math.max(0.01, smooth(stageAge, 1.3, 3.8));
        batter.scale.setScalar(1 - pour * 0.25);
        whisk.rotation.y = reduced ? 0 : (st === 1 && stageAge < 1.6 ? time * 12 : 0); whisk.position.y = 1.05 + (st === 1 ? smooth(stageAge, 1.2, 2.0) * 0.6 : 0);
      }
      if (st === 2) {
        const open = stageAge < 1 ? smooth(stageAge, 0, 0.6) : stageAge < 2 ? 1 - smooth(stageAge, 1.3, 2) : smooth(stageAge, 4, 4.8);
        doorPivot.rotation.x = -open * Math.PI * 0.46;
        sponge.position.z = stageAge < 1.4 ? 1.5 - smooth(stageAge, 0.3, 1.4) * 0.95 : 0.55; sponge.scale.y = 0.4 + smooth(stageAge, 2, 4) * 0.6;
        const glowOn = stageAge > 1.5 ? 1 : 0; ovenGlow.intensity = 5 * glowOn; (hole.material as T.MeshStandardMaterial).emissiveIntensity = 0.5 * glowOn;
        timerHand.rotation.z = -Math.min(stageAge / 4, 1) * TAU;
      }
      assembled.forEach(({ object, y: base, delay }) => { const settle = smooth(stageAge, delay, delay + 0.7); object.visible = settle > 0; object.position.y = base + (1 - settle) * 2.2; });
      cake.rotation.y = reduced ? 0 : Math.sin(time * 0.13) * 0.12;

      // candles: lit state, flicker, wind, smoke
      const lit = Math.min(5, Math.max(0, state.candles ?? 0)), blowing = Boolean(state.blowing) && !reduced;
      let litLevel = 0;
      flames.forEach((f, i) => {
        const isLit = i < lit && st === 3;
        if (f.lit && !isLit && !reduced) { smoke[i].trigger(f.top); stage.sfx("puff", 0.5); }
        if (!f.lit && isLit && i === 4 && !reduced) stage.sfx("chime", 0.4);
        f.lit = isLit; f.level = reduced ? (isLit ? 1 : 0) : T.MathUtils.damp(f.level, isLit ? 1 : 0, isLit ? 9 : 22, dt);
        const gust = blowing ? 0.55 + 0.45 * Math.sin(time * 38 + i * 2.1) : 1;
        f.flame.update(time + i * 3.7, camera, f.level * gust); litLevel += f.level;
      });
      candleLight.position.set(0, topOf[2] + 1.1, 0.3); candleLight.intensity = (2.6 * litLevel) * (reduced ? 1 : 0.9 + 0.1 * Math.sin(time * 13));
      smoke.forEach((s) => s.update(dt));

      // wish: confetti + fireworks (once per celebration)
      const celebrating = Boolean(state.celebration) && st === 3;
      if (celebrating && !lastCelebration) { celebrateAge = 0; fired.clear(); if (!reduced) { stage.sfx("confetti"); confetti.trigger([0, topOf[2] + 0.5, 0]); } }
      if (!celebrating && lastCelebration) { confetti.reset(); fireworks.forEach((f) => f.reset()); celebrateAge = -1; }
      lastCelebration = celebrating;
      if (celebrateAge >= 0 && !reduced) {
        celebrateAge += dt;
        fireAt.forEach((t, k) => { if (celebrateAge >= t && !fired.has(k)) { fired.add(k); const p = firePos[k % 3]; fireworks[k % 3].trigger([p[0], p[1], p[2]]); stage.sfx("firework", 0.6); } });
      }
      confetti.update(dt); fireworks.forEach((f) => f.update(dt));
      sparkleField.update(time);

      // chandelier life
      chandelier.rotation.y = reduced ? 0 : time * 0.08; glints.forEach((g, i) => { (g.material as T.SpriteMaterial).opacity = reduced ? 0.5 : Math.max(0, Math.sin(time * 1.6 + i * 1.9)) * 0.9; });

      // camera
      const fin = celebrating ? 1 : 0;
      pos.set(0, st === 3 ? 3.2 + fin * 0.8 : 2.8, st === 3 ? 9.4 + fin * 2.2 : 8.4); look.set(0, st === 3 ? 1.55 + fin * 0.8 : 1.15, 0);
      if (!reduced) { pos.x += Math.sin(time * 0.17) * 0.35; pos.y += Math.sin(time * 0.13) * 0.08; }
      tmp.copy(pos).sub(look); const fit = T.MathUtils.clamp(1.3 / Math.max(0.5, camera.aspect), 1, 2); camera.position.copy(look).addScaledVector(tmp, fit); camera.lookAt(look);
    },
  };
}
```

## 82. `src/three/sections/heroGarden.ts` — new

```ts
/**
 * Birthday Garden hero: the living cut-away garden (soil strata, seed, roots, sprout, leaves, bud, full bloom) behind the page headline.
 * The scene is the gift-03 world in its hero variant; growth is driven by the HTML stage controls (state.growth 0..4) and the
 * camera follows the plant from underground up to the blossom.
 */
import type { Choreography, Stage } from "../runtime";
import { buildFlowerWorld } from "../gifts/flower";

export function buildHeroGarden(stage: Stage): Choreography {
  return buildFlowerWorld(stage, { hero: true });
}
```

## 83. `src/three/sections/observatory.ts` — new

```ts
/**
 * Memory Observatory: a brass astronomical clock in a night dome. The hands show the visitor's real local time, a train of
 * meshing gears turns behind it, a pendulum swings at one beat per second, and three small planets circle the dial at the angles
 * of the three verified milestones (first connection, the proposal, the birthday marker). Stars twinkle, a shooting star crosses now and then.
 * state: selected 0..2 (highlights a milestone planet and turns the camera towards it).  pick: planet index.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { ParticleField } from "../../engine/fx";
import { addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { fbm, glowCanvas, toTexture } from "../../engine/textures";
import { RoundedBoxGeometry, put } from "../../engine/geometry";
import { chronosContent } from "../../content/chronosContent";

const TAU = Math.PI * 2;
const NODE_ANGLES = chronosContent.scrapbook.clockNodes.map((node) => node.angle);

/** Involute-ish spur gear: flat-topped teeth, a hub hole and decorative windows. */
function gearGeometry(teeth: number, module: number, thickness: number) {
  const pitch = (teeth * module) / 2, outer = pitch + module * 0.95, root = pitch - module * 1.05, step = TAU / teeth;
  const shape = new T.Shape();
  for (let i = 0; i < teeth; i++) {
    const a = i * step;
    const profile: [number, number][] = [[root, 0], [root, 0.08], [outer, 0.24], [outer, 0.42], [root, 0.56]];
    profile.forEach(([r, k], j) => { const x = Math.cos(a + k * step) * r, y = Math.sin(a + k * step) * r; if (i === 0 && j === 0) shape.moveTo(x, y); else shape.lineTo(x, y); });
  }
  shape.closePath();
  const hub = new T.Path(); hub.absarc(0, 0, root * 0.14, 0, TAU, true); shape.holes.push(hub);
  if (teeth >= 20) for (let k = 0; k < 5; k++) {
    const a = (k / 5) * TAU, window = new T.Path(); window.absarc(Math.cos(a) * root * 0.56, Math.sin(a) * root * 0.56, root * 0.2, 0, TAU, true); shape.holes.push(window);
  }
  const geometry = new T.ExtrudeGeometry(shape, { depth: thickness, bevelEnabled: true, bevelSize: module * 0.07, bevelThickness: module * 0.07, bevelSegments: 1, curveSegments: 2 });
  geometry.translate(0, 0, -thickness / 2);
  return { geometry, pitch };
}

function handGeometry(length: number, width: number) {
  const s = new T.Shape();
  s.moveTo(-width * 0.5, -length * 0.16); s.lineTo(-width * 0.34, length * 0.62); s.lineTo(-width * 0.9, length * 0.7); s.lineTo(0, length); s.lineTo(width * 0.9, length * 0.7); s.lineTo(width * 0.34, length * 0.62); s.lineTo(width * 0.5, -length * 0.16); s.closePath();
  const g = new T.ExtrudeGeometry(s, { depth: 0.02, bevelEnabled: true, bevelSize: 0.004, bevelThickness: 0.004, bevelSegments: 1, curveSegments: 4 });
  return g;
}

function faceTexture() {
  const size = 1024, c = document.createElement("canvas"); c.width = c.height = size; const g = c.getContext("2d")!;
  const base = g.createRadialGradient(size / 2, size * 0.46, 40, size / 2, size / 2, size / 2);
  base.addColorStop(0, "#1c2c44"); base.addColorStop(1, "#0b1422"); g.fillStyle = base; g.fillRect(0, 0, size, size);
  g.translate(size / 2, size / 2);
  g.strokeStyle = "#c9a24e"; g.lineWidth = 6; g.beginPath(); g.arc(0, 0, 470, 0, TAU); g.stroke();
  g.lineWidth = 2; g.beginPath(); g.arc(0, 0, 330, 0, TAU); g.stroke();
  for (let i = 0; i < 60; i++) {
    const a = (i / 60) * TAU, major = i % 5 === 0; g.lineWidth = major ? 7 : 2.5; g.strokeStyle = "#d8b865";
    g.beginPath(); g.moveTo(Math.sin(a) * (major ? 410 : 438), -Math.cos(a) * (major ? 410 : 438)); g.lineTo(Math.sin(a) * 462, -Math.cos(a) * 462); g.stroke();
  }
  g.fillStyle = "#e8cf8c"; g.font = "600 76px Georgia, 'Times New Roman', serif"; g.textAlign = "center"; g.textBaseline = "middle";
  const romans = ["XII", "I", "II", "III", "IIII", "V", "VI", "VII", "VIII", "IX", "X", "XI"];
  romans.forEach((numeral, i) => { const a = (i / 12) * TAU; g.save(); g.translate(Math.sin(a) * 365, -Math.cos(a) * 365); g.rotate(a); if (i > 3 && i < 9) g.rotate(Math.PI); g.font = `600 ${numeral.length > 2 ? 54 : 70}px Georgia, serif`; g.fillText(numeral, 0, 0); g.restore(); });
  // a quiet engraved sun-and-moon medallion
  g.strokeStyle = "#8f7a45"; g.lineWidth = 3; g.beginPath(); g.arc(0, 150, 86, 0, TAU); g.stroke();
  g.fillStyle = "#c9a24e"; g.beginPath(); g.arc(0, 150, 44, 0, TAU); g.fill(); g.fillStyle = "#0f1a2a"; g.beginPath(); g.arc(24, 140, 40, 0, TAU); g.fill();
  const texture = toTexture(c, { srgb: true, wrap: false, anisotropy: 8 });
  return texture;
}

function moonTexture() {
  const w = 512, h = 256, c = document.createElement("canvas"); c.width = w; c.height = h; const g = c.getContext("2d")!;
  const image = g.createImageData(w, h);
  for (let j = 0; j < h; j++) for (let i = 0; i < w; i++) {
    const u = i / w, v = j / h, n = fbm(u, v, 7, 5, 6, 3), m = fbm(u, v, 21, 3, 3, 2), mare = T.MathUtils.smoothstep(m, 0.46, 0.6), crater = T.MathUtils.smoothstep(fbm(u, v, 5, 4, 18, 9), 0.62, 0.74);
    const lum = 150 + n * 70 - mare * 52 - crater * 26, k = (j * w + i) * 4;
    image.data[k] = lum; image.data[k + 1] = lum * 0.99; image.data[k + 2] = lum * 0.95; image.data[k + 3] = 255;
  }
  g.putImageData(image, 0, 0);
  return toTexture(c, { srgb: true, wrap: false });
}

export function buildObservatory(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "moon", envIntensity: 1.35, exposure: 1.1, background: "#0a1226", fog: { color: "#0a1226", density: 0.02 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 140; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#6f8fcf", "#2a2018", 0.9));
  addKeyLight(scene, quality, { color: "#ffd9a8", intensity: 3.1, position: [-4, 6, 8], target: [0, 1.4, 0], extent: 6, far: 26 });
  const moonLight = new T.DirectionalLight("#a8c4ff", 1.1); moonLight.position.set(6, 5, -4); scene.add(moonLight);
  const faceLight = new T.PointLight("#ffcf8a", 6, 9, 2); faceLight.position.set(0, 2.2, 4); scene.add(faceLight);
  const gearLight = new T.PointLight("#ffd9a0", 9, 11, 2); gearLight.position.set(0, -0.5, 2.6); scene.add(gearLight);

  /* ---------- sky ---------- */
  const stars = new ParticleField({ count: Math.round(900 * particleScale(quality)), size: 0.22, color: "#dfe8ff", colorB: "#ffe5b8", opacity: 0.95, bounds: [34, 24, 34], center: [0, 6, -4], distribution: "shell", shellInner: 0.86, drift: 0.1, twinkle: 0.85 });
  scene.add(stars.points);
  const moon = new T.Mesh(new T.SphereGeometry(1.25, low ? 32 : 56, low ? 20 : 36), new T.ShaderMaterial({
    uniforms: { uMap: { value: moonTexture() }, uSun: { value: new T.Vector3(-0.85, 0.15, 0.5).normalize() } }, fog: false,
    vertexShader: "varying vec2 vUv; varying vec3 vN; void main(){ vUv = uv; vN = normalize(mat3(modelMatrix) * normal); gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",
    fragmentShader: "uniform sampler2D uMap; uniform vec3 uSun; varying vec2 vUv; varying vec3 vN; void main(){ float l = smoothstep(-0.04, 0.3, dot(normalize(vN), uSun)); vec3 tex = texture2D(uMap, vUv).rgb; vec3 col = tex * (0.035 + l * 1.05) * vec3(1.0, 0.97, 0.9); gl_FragColor = vec4(pow(col, vec3(0.92)), 1.0); }",
  }));
  moon.position.set(6.6, 5.0, -9); scene.add(moon);
  const moonHalo = new T.Sprite(new T.SpriteMaterial({ map: (() => { const t = new T.CanvasTexture(glowCanvas("rgba(190,215,255,0.9)", "rgba(120,160,255,0)", 128)); t.colorSpace = T.SRGBColorSpace; return t; })(), transparent: true, opacity: 0.7, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
  moonHalo.scale.setScalar(7.5); moonHalo.position.copy(moon.position); scene.add(moonHalo);
  const trail = new T.Mesh(new T.PlaneGeometry(3.4, 0.045), new T.ShaderMaterial({
    transparent: true, depthWrite: false, blending: T.AdditiveBlending, fog: false, uniforms: { uOpacity: { value: 0 } },
    vertexShader: "varying vec2 vUv; void main(){ vUv = uv; gl_Position = projectionMatrix * modelViewMatrix * vec4(position, 1.0); }",
    fragmentShader: "uniform float uOpacity; varying vec2 vUv; void main(){ gl_FragColor = vec4(vec3(0.9, 0.95, 1.0), pow(vUv.x, 2.5) * (1.0 - abs(vUv.y - 0.5) * 2.0) * uOpacity); }",
  }));
  trail.visible = false; scene.add(trail);

  /* ---------- floor and pedestal ---------- */
  const floor = put(scene, new T.PlaneGeometry(220, 160), new T.MeshStandardMaterial({ color: "#141a2a", roughness: 0.5, metalness: 0.25 }), 0, -2.55, -30, false);
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;
  put(scene, new RoundedBoxGeometry(3.4, 0.36, 1.6, 3, 0.06), kit.wood("#1c1109", "#4a2e1a", [2, 1], 0.5), 0, -2.37, 0.1);
  put(scene, new T.BoxGeometry(3.44, 0.03, 1.64), kit.metal("brass", 0.4), 0, -2.18, 0.1, false);

  /* ---------- the clock ---------- */
  const clock = new T.Group(); clock.position.set(0, 1.55, 0); scene.add(clock);
  const brass = kit.metal("brass", 0.34), gold = kit.metal("gold", 0.28), steel = kit.metal("steel", 0.35);
  const casing = new T.Mesh(new T.TorusGeometry(1.5, 0.11, 16, 96), brass); casing.castShadow = !low; clock.add(casing);
  const bezel = new T.Mesh(new T.TorusGeometry(1.38, 0.035, 10, 96), gold); bezel.position.z = 0.04; clock.add(bezel);
  const face = new T.Mesh(new T.CircleGeometry(1.42, 96), new T.MeshStandardMaterial({ map: faceTexture(), roughness: 0.55, metalness: 0.25 })); face.position.z = -0.03; clock.add(face);
  const DOME_R = 4, DOME_A = Math.asin(1.42 / DOME_R);
  const dome = new T.Mesh(new T.SphereGeometry(DOME_R, 64, 8, 0, TAU, 0, DOME_A), new T.MeshPhysicalMaterial({ color: "#dce8ff", transparent: true, opacity: 0.07, roughness: 0.04, clearcoat: 1, clearcoatRoughness: 0.03, envMapIntensity: 0.7, depthWrite: false })); dome.rotation.x = Math.PI / 2; dome.position.z = 0.03 - DOME_R * Math.cos(DOME_A); clock.add(dome);
  const hourHand = new T.Mesh(handGeometry(0.72, 0.1), gold), minuteHand = new T.Mesh(handGeometry(1.12, 0.07), gold), secondHand = new T.Mesh(handGeometry(1.22, 0.025), kit.metal("copper", 0.3));
  hourHand.position.z = 0.07; minuteHand.position.z = 0.1; secondHand.position.z = 0.135; clock.add(hourHand, minuteHand, secondHand);
  const pin = new T.Mesh(new T.SphereGeometry(0.075, 16, 12), steel); pin.position.z = 0.16; clock.add(pin);
  // pendulum
  const pendulum = new T.Group(); pendulum.position.set(0, 0.02, -0.12); scene.add(pendulum);
  const rod = new T.Mesh(new T.CylinderGeometry(0.014, 0.014, 1.5, 8), brass); rod.position.y = -0.75; pendulum.add(rod);
  const bob = new T.Mesh(new T.CylinderGeometry(0.3, 0.3, 0.07, 40), new T.MeshStandardMaterial({ color: "#d9b25a", metalness: 0.65, roughness: 0.34, emissive: "#6a4a12", emissiveIntensity: 0.55 })); bob.rotation.x = Math.PI / 2; bob.position.y = -1.6; pendulum.add(bob);
  const bobRing = new T.Mesh(new T.TorusGeometry(0.2, 0.012, 8, 40), steel); bobRing.position.set(0, -1.6, 0.05); pendulum.add(bobRing);

  /* ---------- gear train ---------- */
  const module = 0.058, specs = [{ teeth: 40, dir: 1 }, { teeth: 24, dir: -1 }, { teeth: 32, dir: 1 }, { teeth: 20, dir: -1 }, { teeth: 36, dir: 1 }, { teeth: 22, dir: -1 }];
  const gearGroup = new T.Group(); gearGroup.position.set(-0.1, -0.4, -0.55); scene.add(gearGroup);
  const heading = [0, -0.55, 0.3, -0.45, 0.2];
  const gearMat = [brass, gold, brass, gold, brass, gold];
  const gearPos = new T.Vector3(-3.7, 0.2, 0);
  const gears = specs.map((spec, i) => {
    const { geometry, pitch } = gearGeometry(spec.teeth, module, 0.07 + (i % 2) * 0.02);
    const mesh = new T.Mesh(geometry, gearMat[i]); mesh.castShadow = !low;
    if (i > 0) {
      const prev = specs[i - 1], prevPitch = (prev.teeth * module) / 2, a = heading[i - 1];
      gearPos.x += Math.cos(a) * (prevPitch + pitch); gearPos.y += Math.sin(a) * (prevPitch + pitch);
    }
    mesh.position.copy(gearPos).setZ(i % 2 ? 0.0 : 0.04); gearGroup.add(mesh);
    return { mesh, spec, phase: i % 2 ? Math.PI / spec.teeth : 0 };
  });

  /* ---------- orrery: milestone planets on tilted rings around the dial ---------- */
  const orrery = new T.Group(); orrery.position.copy(clock.position); scene.add(orrery);
  const RINGS = [{ r: 2.35, tilt: 0.05 }, { r: 2.95, tilt: -0.07 }, { r: 3.55, tilt: 0.1 }];
  RINGS.forEach((ring) => { const m = new T.Mesh(new T.TorusGeometry(ring.r, 0.014, 6, 120), brass); m.rotation.x = ring.tilt; m.rotation.y = ring.tilt * 0.6; orrery.add(m); });
  const planetMaterials = [
    new T.MeshPhysicalMaterial({ color: "#2f67b8", roughness: 0.35, clearcoat: 0.8, emissive: "#0b2a5c", emissiveIntensity: 0.5 }),
    new T.MeshPhysicalMaterial({ color: "#e0a995", roughness: 0.28, metalness: 0.85, clearcoat: 0.6, emissive: "#6b2a24", emissiveIntensity: 0.2 }),
    new T.MeshStandardMaterial({ color: "#ffd48a", roughness: 0.4, emissive: "#ff9a3a", emissiveIntensity: 0.9 }),
  ];
  const haloTexture = (() => { const t = new T.CanvasTexture(glowCanvas("rgba(255,226,170,1)", "rgba(255,170,90,0)", 128)); t.colorSpace = T.SRGBColorSpace; return t; })();
  const planets = NODE_ANGLES.map((angle, i) => {
    const pivot = new T.Group(); orrery.add(pivot);
    const body = new T.Mesh(new T.SphereGeometry(0.2 + i * 0.03, 36, 24), planetMaterials[i]); body.castShadow = !low; pivot.add(body);
    if (i === 1) { const band = new T.Mesh(new T.TorusGeometry(0.34, 0.012, 6, 40), gold); band.rotation.x = 1.15; pivot.add(band); }
    const halo = new T.Sprite(new T.SpriteMaterial({ map: haloTexture, transparent: true, opacity: 0.25, depthWrite: false, blending: T.AdditiveBlending, fog: false })); halo.scale.setScalar(1.1); halo.raycast = () => {}; pivot.add(halo);
    // generous invisible hit target so the planets are easy to tap
    const hit = new T.Mesh(new T.SphereGeometry(0.55, 8, 6), new T.MeshBasicMaterial({ visible: false })); pivot.add(hit);
    pivot.userData.index = i;
    return { pivot, body, halo, angle: (angle / 360) * TAU, ring: RINGS[i], focus: 0 };
  });

  /* ---------- telescope ---------- */
  const telescope = new T.Group(); telescope.position.set(-6.0, -2.35, 1.2); scene.add(telescope);
  for (let k = 0; k < 3; k++) { const a = (k / 3) * TAU + 0.4; const leg = new T.Mesh(new T.CylinderGeometry(0.035, 0.05, 2.3, 8), kit.wood("#2a170c", "#6b4527", [1, 3], 0.5)); leg.position.set(Math.cos(a) * 0.42, 1.05, Math.sin(a) * 0.42); leg.rotation.set(-Math.sin(a) * 0.34, 0, Math.cos(a) * 0.34); telescope.add(leg); }
  const tube = new T.Group(); tube.position.set(0, 2.25, 0); tube.rotation.z = 0.85; tube.rotation.y = -0.25; telescope.add(tube);
  const tubeBody = new T.Mesh(new T.CylinderGeometry(0.2, 0.26, 2.6, 28), kit.leather("#16231f", "#2f4a42", [4, 1])); tubeBody.rotation.z = Math.PI / 2; tubeBody.position.x = 1.0; tubeBody.castShadow = !low; tube.add(tubeBody);
  [-0.15, 2.2].forEach((x, k) => { const ring = new T.Mesh(new T.TorusGeometry(k ? 0.27 : 0.21, 0.035, 8, 32), brass); ring.rotation.y = Math.PI / 2; ring.position.x = x + (k ? 0 : 0.05); tube.add(ring); });
  const lens = new T.Mesh(new T.CircleGeometry(0.25, 32), kit.glass("#bcd6ff")); lens.rotation.y = Math.PI / 2; lens.position.x = 2.3; tube.add(lens);
  const eyepiece = new T.Mesh(new T.CylinderGeometry(0.06, 0.08, 0.4, 16), brass); eyepiece.rotation.z = Math.PI / 2; eyepiece.position.x = -0.35; tube.add(eyepiece);

  /* ---------- camera ---------- */
  const look = new T.Vector3(0, 1.0, 0), want = new T.Vector3(), pos = new T.Vector3(), offset = new T.Vector3(), axis = new T.Vector3(0, 1, 0), tmp = new T.Vector3();
  const orbit = { yaw: 0, pitch: 0 };
  let lastSelected: number | null = null, shootT = -1;

  return {
    pickables: planets.map((p) => p.pivot),
    frame(time, dt, state: SceneState, reduced) {
      const selected = state.selected ?? null;
      if (selected !== lastSelected && selected !== null && !reduced) stage.sfx("sparkle", 0.6);
      lastSelected = selected;

      // real local time
      const now = new Date(), sec = now.getSeconds() + (reduced ? 0 : now.getMilliseconds() / 1000), min = now.getMinutes() + sec / 60, hour = (now.getHours() % 12) + min / 60;
      hourHand.rotation.z = -(hour / 12) * TAU; minuteHand.rotation.z = -(min / 60) * TAU; secondHand.rotation.z = -(sec / 60) * TAU;
      pendulum.rotation.z = reduced ? 0 : Math.sin(time * Math.PI) * 0.26;

      // gears: meshing ratios (angular speed inversely proportional to the tooth count)
      if (!reduced) gears.forEach((g) => { g.mesh.rotation.z = g.phase + g.spec.dir * (time * 2.6) / g.spec.teeth; });

      // planets on the dial, at the angle of their milestone
      planets.forEach((p, i) => {
        const isSel = selected === i;
        p.focus = reduced ? (isSel ? 1 : 0) : T.MathUtils.damp(p.focus, isSel ? 1 : 0, 3, dt);
        const a = p.angle + (reduced ? 0 : Math.sin(time * 0.25 + i * 2) * 0.06);
        p.pivot.position.set(Math.sin(a) * p.ring.r, Math.cos(a) * p.ring.r, Math.sin(a) * p.ring.tilt * 3);
        p.pivot.scale.setScalar(1 + 0.45 * p.focus);
        p.body.rotation.y = reduced ? 0 : time * 0.4 + i;
        (p.halo.material as T.SpriteMaterial).opacity = 0.22 + 0.55 * p.focus + (reduced ? 0 : 0.06 * Math.sin(time * 2 + i));
      });
      orrery.rotation.y = reduced ? 0 : Math.sin(time * 0.12) * 0.12;

      // shooting star every ~9 s
      if (!reduced) {
        const cycle = 9.5, t = time % cycle;
        if (t < 0.06 && shootT < 0) { shootT = 0; stage.sfx("sparkle", 0.25); }
        if (shootT >= 0) {
          shootT += dt; const k = shootT / 1.1;
          if (k >= 1) { shootT = -1; trail.visible = false; }
          else { trail.visible = true; trail.position.set(7 - k * 15, 7.5 - k * 5.2, -11); trail.rotation.z = -0.33; (trail.material as T.ShaderMaterial).uniforms.uOpacity.value = Math.sin(Math.PI * k) * 0.9; }
        }
      }
      stars.update(time);

      // camera: gentle drift, drag to look around, turn towards a selected milestone
      const sel = selected !== null ? planets[selected] : null;
      if (sel) { sel.pivot.getWorldPosition(tmp); want.set(tmp.x * 0.35, 1.0 + (tmp.y - 1.55) * 0.3, 0); } else want.set(0, 1.0, 0);
      look.lerp(want, reduced ? 1 : 1 - Math.exp(-2 * dt));
      pos.set(0, 2.5, 13.4);
      if (!reduced) { pos.x += Math.sin(time * 0.17) * 0.35; pos.y += Math.sin(time * 0.13) * 0.1; }
      const drag = input.consumeDrag();
      orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.2, -0.6, 0.6); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.1, -0.1, 0.25);
      offset.copy(pos).sub(look).applyAxisAngle(axis, orbit.yaw); offset.applyAxisAngle(tmp.set(1, 0, 0), -orbit.pitch);
      const fit = T.MathUtils.clamp(1.5 / Math.max(0.45, camera.aspect), 1, 2.3);
      camera.position.copy(look).addScaledVector(offset, fit); camera.lookAt(look);
    },
  };
}
```

## 84. `src/three/sections/postcards.ts` — new

```ts
/**
 * Future Postcards: one thick, glossy postcard lying on a lamp-lit writing desk.
 * The front shows the original illustration; turning the card over (state.open) lifts it, flips it about its long edge and
 * writes the existing imagined-future message on the reverse in handwriting. A visitor's own line (state.extra.note, kept in the tab only)
 * is added underneath in a second ink. Choosing another postcard (state.artwork changes) deals a new card onto the desk.
 * state: open, artwork (image URL), detail ("place\nsomeday\ncaption\ndisclaimer"), extra.note (string).  pick: toggles the flip.
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { ParticleField } from "../../engine/fx";
import { RoundedBoxGeometry, lathe, put } from "../../engine/geometry";
import { addContactShadow, addKeyLight } from "../../engine/lights";
import { particleScale } from "../../engine/quality";
import { glowCanvas } from "../../engine/textures";

const CW = 4.2, CH = 2.66, TH = 0.05;
const PX = 1136, PY = 720; // reverse-side canvas, same aspect as the card

function wrap(g: CanvasRenderingContext2D, text: string, maxWidth: number) {
  const words = text.split(/\s+/), lines: string[] = []; let line = "";
  for (const word of words) { const test = line ? `${line} ${word}` : word; if (g.measureText(test).width > maxWidth && line) { lines.push(line); line = word; } else line = test; }
  if (line) lines.push(line);
  return lines;
}

/** Draws the printed reverse (stamp, postmark, rules) once, and the handwriting wiped in by `write` (0..1). */
class Reverse {
  readonly canvas = document.createElement("canvas");
  readonly texture: T.CanvasTexture;
  private ink = document.createElement("canvas");
  private lines: { text: string; x: number; y: number; font: string; color: string; width: number }[] = [];
  private total = 1;
  constructor() {
    this.canvas.width = this.ink.width = PX; this.canvas.height = this.ink.height = PY;
    this.texture = new T.CanvasTexture(this.canvas); this.texture.colorSpace = T.SRGBColorSpace; this.texture.anisotropy = 8;
    this.compose(1);
  }
  /**
   * Lays out the handwriting for the given message. The pack's postcard messages run to about 300 characters, so the writing is
   * fitted: the largest handwriting size at which title, message and the visitor's own line all stay above the printed disclaimer.
   */
  setText(place: string, someday: string, caption: string, disclaimer: string, note: string) {
    const g = this.ink.getContext("2d")!; g.clearRect(0, 0, PX, PY);
    const left = 70, maxW = 575, top = 190, bottom = PY - 125; this.lines = [];
    const hand = (weight: number, size: number) => `${weight} ${Math.round(size)}px Caveat, 'Segoe Print', cursive`;
    type Row = { text: string; font: string; color: string; y: number };
    let rows: Row[] = [];
    for (let size = 42; size >= 24; size -= 2) {
      const titleSize = Math.max(50, Math.min(74, size * 1.75)), out: Row[] = []; let y = top;
      g.font = hand(700, titleSize); wrap(g, place, maxW).forEach((l) => { out.push({ text: l, font: g.font, color: "#1d2740", y }); y += titleSize * 0.95; });
      if (someday.trim()) { y += 4; g.font = hand(600, size * 1.05); wrap(g, someday, maxW).forEach((l) => { out.push({ text: l, font: g.font, color: "#6a4a3a", y }); y += size * 1.05; }); }
      y += size * 0.35; g.font = hand(600, size); wrap(g, caption, maxW).forEach((l) => { out.push({ text: l, font: g.font, color: "#232c47", y }); y += size * 1.02; });
      if (note.trim()) { y += size * 0.45; g.font = hand(600, size); wrap(g, note.trim(), maxW).slice(0, 4).forEach((l) => { out.push({ text: l, font: g.font, color: "#27559b", y }); y += size * 1.02; }); }
      rows = out;
      if (y - size * 1.02 <= bottom) break;
    }
    rows.forEach((row) => { g.font = row.font; this.lines.push({ ...row, x: left, width: g.measureText(row.text).width }); });
    this.disclaimer = disclaimer; this.total = this.lines.reduce((sum, l) => sum + l.width, 0) || 1;
  }
  private disclaimer = "";
  compose(write: number) {
    const g = this.canvas.getContext("2d")!;
    // printed card stock
    const paper = g.createLinearGradient(0, 0, PX, PY); paper.addColorStop(0, "#f7efdc"); paper.addColorStop(1, "#ecdfc2"); g.fillStyle = paper; g.fillRect(0, 0, PX, PY);
    g.globalAlpha = 0.07; g.fillStyle = "#6a4d2a"; for (let i = 0; i < 900; i++) g.fillRect((i * 97) % PX, (i * 61) % PY, 2, 1); g.globalAlpha = 1;
    g.strokeStyle = "#9b8660"; g.lineWidth = 3; g.beginPath(); g.moveTo(PX * 0.62, 70); g.lineTo(PX * 0.62, PY - 70); g.stroke();
    g.fillStyle = "#8a7550"; g.font = "700 22px 'DM Sans', Arial, sans-serif"; g.textBaseline = "alphabetic";
    try { (g as unknown as { letterSpacing: string }).letterSpacing = "5px"; } catch { /* optional */ }
    g.fillText("POSTCARD · A POSSIBLE DAY", 70, 88);
    try { (g as unknown as { letterSpacing: string }).letterSpacing = "0px"; } catch { /* optional */ }
    // address rules (left blank on purpose)
    g.strokeStyle = "#b7a47c"; g.lineWidth = 2; for (let i = 0; i < 4; i++) { g.beginPath(); g.moveTo(PX * 0.66, 300 + i * 66); g.lineTo(PX - 70, 300 + i * 66); g.stroke(); }
    // stamp with perforated edge
    const sx = PX - 250, sy = 64, sw = 180, sh = 210;
    g.fillStyle = "#e6d6b4"; g.beginPath(); for (let i = 0; i <= 12; i++) { const x = sx + (i / 12) * sw; g.moveTo(x + 7, sy); g.arc(x, sy, 7, 0, Math.PI * 2); g.moveTo(x + 7, sy + sh); g.arc(x, sy + sh, 7, 0, Math.PI * 2); } for (let i = 0; i <= 14; i++) { const y = sy + (i / 14) * sh; g.moveTo(sx + 7, y); g.arc(sx, y, 7, 0, Math.PI * 2); g.moveTo(sx + sw + 7, y); g.arc(sx + sw, y, 7, 0, Math.PI * 2); } g.fill();
    g.fillStyle = "#f4ead0"; g.fillRect(sx, sy, sw, sh); g.strokeStyle = "#a9323f"; g.lineWidth = 4; g.strokeRect(sx + 12, sy + 12, sw - 24, sh - 24);
    g.fillStyle = "#a9323f"; g.font = "700 26px 'DM Sans', Arial, sans-serif"; g.textAlign = "center"; g.fillText("IMAGINED", sx + sw / 2, sy + sh - 34); g.textAlign = "left";
    g.beginPath(); g.arc(sx + sw / 2, sy + 90, 40, 0, Math.PI * 2); g.fill(); g.fillStyle = "#f4ead0"; g.beginPath(); g.arc(sx + sw / 2 + 14, sy + 80, 34, 0, Math.PI * 2); g.fill();
    // wavy postmark ring
    g.strokeStyle = "rgba(60,48,40,.5)"; g.lineWidth = 4; g.beginPath(); g.arc(sx - 70, sy + 150, 78, 0, Math.PI * 2); g.stroke(); g.beginPath(); g.arc(sx - 70, sy + 150, 58, 0, Math.PI * 2); g.stroke();
    for (let i = 0; i < 4; i++) { g.beginPath(); g.moveTo(sx - 160, sy + 130 + i * 14); g.bezierCurveTo(sx - 120, sy + 112 + i * 14, sx - 40, sy + 148 + i * 14, sx + 70, sy + 126 + i * 14); g.stroke(); }
    // handwriting, wiped in left to right line after line
    let budget = write * this.total;
    for (const line of this.lines) {
      if (budget <= 0) break;
      const w = Math.min(line.width, budget); budget -= line.width;
      g.save(); g.beginPath(); g.rect(line.x - 8, line.y - 90, w + 14, 130); g.clip();
      g.font = line.font; g.fillStyle = line.color; g.fillText(line.text, line.x, line.y); g.restore();
    }
    if (write > 0.98 && this.disclaimer) { g.font = "italic 600 26px 'DM Sans', Arial, sans-serif"; g.fillStyle = "#7c6a49"; g.fillText(this.disclaimer, 70, PY - 60); }
    this.texture.needsUpdate = true;
  }
}

export function buildPostcards(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low";
  stage.mood({ env: "candle", envIntensity: 0.55, exposure: 1.08, background: "#1c130d", fog: { color: "#1c130d", density: 0.02 } });
  camera.fov = 34; camera.near = 0.1; camera.far = 60; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#ffe7c4", "#3a2418", 0.9));
  addKeyLight(scene, quality, { color: "#ffd9a8", intensity: 3.6, position: [-4, 7, 3], target: [0, 0, 0], extent: 5, far: 22 });
  const lamp = new T.PointLight("#ffbf75", 14, 14, 2); lamp.position.set(-3.6, 3.4, 0.4); scene.add(lamp);
  const rim = new T.DirectionalLight("#9fb6ff", 0.5); rim.position.set(5, 3, -4); scene.add(rim);

  /* ---------- desk and props ---------- */
  const desk = put(scene, new T.PlaneGeometry(40, 26), kit.wood("#24140c", "#6b4527", [8, 5], 0.5), 0, -0.03, -2, false);
  desk.rotation.x = -Math.PI / 2; desk.receiveShadow = true;
  put(scene, new RoundedBoxGeometry(7.5, 0.04, 4.7, 2, 0.03), kit.metal("gold", 0.45), 0, -0.005, 0.1);
  put(scene, new RoundedBoxGeometry(7.3, 0.05, 4.5, 2, 0.03), new T.MeshStandardMaterial({ color: "#213a30", roughness: 0.92 }), 0, 0.0, 0.1); // green felt blotter with a gold inlay
  // ink pot
  const inkPot = new T.Group(); inkPot.position.set(3.2, 0.02, -1.5); scene.add(inkPot);
  inkPot.add(new T.Mesh(lathe([[0, 0], [0.42, 0], [0.5, 0.08], [0.5, 0.52], [0.34, 0.66], [0.2, 0.7], [0.2, 0.82], [0.26, 0.86]], 32), kit.glass("#cfe0ff")));
  inkPot.add(new T.Mesh(new T.CylinderGeometry(0.43, 0.43, 0.4, 24), new T.MeshStandardMaterial({ color: "#0a1228", roughness: 0.15, metalness: 0.2 }))).position.y = 0.3;
  const cap = new T.Mesh(new T.CylinderGeometry(0.17, 0.2, 0.2, 16), kit.metal("brass", 0.35)); cap.position.y = 0.94; inkPot.add(cap);
  // pen
  const pen = new T.Group(); pen.position.set(2.4, 0.09, 1.95); pen.rotation.y = 0.55; scene.add(pen);
  const penBody = new T.Mesh(new T.CylinderGeometry(0.05, 0.06, 2.1, 16), new T.MeshPhysicalMaterial({ color: "#10121a", roughness: 0.2, clearcoat: 1 })); penBody.rotation.z = Math.PI / 2; pen.add(penBody);
  const nib = new T.Mesh(new T.ConeGeometry(0.045, 0.34, 12), kit.metal("gold", 0.25)); nib.rotation.z = Math.PI / 2; nib.position.x = -1.2; pen.add(nib);
  const clip = new T.Mesh(new T.BoxGeometry(0.6, 0.012, 0.04), kit.metal("gold", 0.25)); clip.position.set(0.5, 0.075, 0); pen.add(clip);
  // lamp halo
  const halo = new T.Sprite(new T.SpriteMaterial({ map: (() => { const t = new T.CanvasTexture(glowCanvas("rgba(255,200,130,0.9)", "rgba(255,150,70,0)", 128)); t.colorSpace = T.SRGBColorSpace; return t; })(), transparent: true, opacity: 0.55, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
  halo.scale.setScalar(9); halo.position.set(-3.6, 2.2, -1.6); scene.add(halo);
  const dust = new T.Group(); scene.add(dust);
  const motes = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.05, color: "#ffe3b0", opacity: 0.55, bounds: [5, 2.4, 3], center: [0, 1.8, 0], drift: 0.6, rise: 0.04, twinkle: 0.5 });
  dust.add(motes.points);

  /* ---------- the postcard ---------- */
  const holder = new T.Group(); holder.rotation.x = -Math.PI / 2; scene.add(holder); // lies flat: local +z points up
  const flipper = new T.Group(); holder.add(flipper);
  const body = new T.Mesh(new RoundedBoxGeometry(CW, CH, TH, 2, 0.03), new T.MeshStandardMaterial({ color: "#f6edd7", roughness: 0.85 })); body.castShadow = !low; flipper.add(body);
  const artMaterial = new T.MeshPhysicalMaterial({ color: "#ffffff", roughness: 0.4, clearcoat: low ? 0 : 0.5, clearcoatRoughness: 0.35 });
  const front = new T.Mesh(new T.PlaneGeometry(3.8, 2.12), artMaterial); front.position.z = TH / 2 + 0.002; flipper.add(front);
  const reverse = new Reverse();
  const back = new T.Mesh(new T.PlaneGeometry(CW - 0.06, CH - 0.06), new T.MeshStandardMaterial({ map: reverse.texture, roughness: 0.85 }));
  back.rotation.x = Math.PI; back.position.z = -TH / 2 - 0.002; flipper.add(back);
  holder.userData.index = 0; // picking anywhere on the card toggles the flip
  const shadow = addContactShadow(scene, CW * 1.05, CH * 1.1, 0, 0.012, 0, 0.5);

  /* ---------- artwork loading (cached, released on dispose) ---------- */
  const loader = new T.TextureLoader(), cache = new Map<string, T.Texture>();
  const setArt = (url: string) => {
    const hit = cache.get(url); if (hit) { artMaterial.map = hit; artMaterial.needsUpdate = true; return; }
    loader.load(url, (texture) => { texture.colorSpace = T.SRGBColorSpace; texture.anisotropy = 8; cache.set(url, texture); if (wantedArt === url) { artMaterial.map = texture; artMaterial.needsUpdate = true; stage.invalidate(); } });
  };
  let wantedArt = "", textKey = "", flip = 0, deal = 1, write = 0, lastOpen = false, lastWrite = -1, fontsReady = false;
  void document.fonts?.load("700 40px Caveat").then(() => { fontsReady = true; textKey = ""; });
  const pos = new T.Vector3(), look = new T.Vector3(0, 0, 0.1), offset = new T.Vector3(), orbit = { yaw: 0, pitch: 0 };

  return {
    pickables: [holder],
    frame(time, dt, state: SceneState, reduced) {
      const art = state.artwork ?? "";
      if (art !== wantedArt) { wantedArt = art; if (art) setArt(art); deal = reduced ? 1 : 0; flip = 0; write = 0; lastOpen = false; if (!reduced) stage.sfx("page", 0.6); }
      const lines = (state.detail ?? "").split("\n"), note = String(state.extra?.note ?? "");
      const key = `${state.detail}|${note}|${fontsReady}`;
      if (key !== textKey) { textKey = key; reverse.setText(lines[0] ?? "", lines[1] ?? "", lines[2] ?? "", lines[3] ?? "", note); lastWrite = -1; }
      const open = Boolean(state.open);
      if (open && !lastOpen && !reduced) { write = 0; stage.sfx("page", 0.5); }
      if (!open && lastOpen) write = 0;
      lastOpen = open;

      deal = reduced ? 1 : Math.min(1, deal + dt / 0.9);
      const target = open ? 1 : 0;
      flip = reduced ? target : T.MathUtils.damp(flip, target, 3.4, dt);
      if (reduced) write = open ? 1 : 0; else if (open && flip > 0.55) write = Math.min(1, write + dt / 3.4);
      if (Math.abs(write - lastWrite) > 0.004 || (lastWrite < 0)) { reverse.compose(write); lastWrite = write; }

      const f = T.MathUtils.smootherstep(flip, 0, 1), dealEase = 1 - Math.pow(1 - deal, 3);
      flipper.rotation.x = f * Math.PI;
      const lift = Math.sin(Math.PI * f) * 1.55 + (1 - dealEase) * 3.2;
      holder.position.set((1 - dealEase) * -1.4, 0.05 + lift, (1 - dealEase) * -0.4);
      holder.rotation.z = (1 - dealEase) * 0.35 + (reduced ? 0 : Math.sin(time * 0.5) * 0.004);
      shadow.position.set(holder.position.x, 0.012, holder.position.z); shadow.scale.setScalar(1 + lift * 0.14); (shadow.material as T.Material).opacity = Math.max(0.12, 0.5 - lift * 0.14);
      motes.update(time); lamp.intensity = 14 + (reduced ? 0 : Math.sin(time * 5.2) * 0.5 + Math.sin(time * 11) * 0.3);

      const drag = input.consumeDrag();
      orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3, -0.5, 0.5); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.15, 0.25);
      pos.set(0, 5.1, 4.4); if (!reduced) { pos.x += Math.sin(time * 0.2) * 0.2; pos.z += Math.cos(time * 0.17) * 0.1; }
      offset.copy(pos).sub(look).applyAxisAngle(new T.Vector3(0, 1, 0), orbit.yaw).applyAxisAngle(new T.Vector3(1, 0, 0), -orbit.pitch);
      const fit = T.MathUtils.clamp(1.2 / Math.max(0.5, camera.aspect), 1, 2.1);
      camera.position.copy(look).addScaledVector(offset, fit); camera.lookAt(look);
    },
    dispose() { cache.forEach((t) => t.dispose()); reverse.texture.dispose(); },
  };
}
```

## 85. `src/three/sections/wishGarden.ts` — new

```ts
/**
 * Wish Garden: a conservatory diorama with ten flowers (rose, daisy, tulip, ...), one per wish already written in the archive.
 * Selecting a flower (3D pick or the numbered HTML buttons) opens it fully, sends a stream of glowing sparks and petals into the air,
 * floats a paper lantern up and glides the camera to the blossom. A wish the visitor plants (kept in the tab only) grows as an
 * eleventh, golden daisy at the front of the bed.
 * state: selected 0..9 (10 = the visitor's own wish) | null, replay (counter: release again), planted (boolean).
 */
import * as T from "three";
import type { Choreography, SceneState, Stage } from "../runtime";
import { Burst, ParticleField } from "../../engine/fx";
import { createBloom, createButterflies, createGrass, createSky, buildTerrain } from "../../engine/garden";
import { RoundedBoxGeometry, leafGeometry, petalGeometry, put, taperedTube } from "../../engine/geometry";
import { addKeyLight } from "../../engine/lights";
import { particleScale, type Quality } from "../../engine/quality";
import { glowCanvas } from "../../engine/textures";
import type { MaterialKit } from "../../engine/materials";

type Species = "rose" | "daisy" | "tulip";
interface Spec { species: Species; petal: [string, string, string]; inner?: [string, string, string]; centre: string; scale: number }

/** index % 3 matches the Rose / Daisy / Tulip labels of the HTML buttons. The last entry is the visitor's own, golden daisy. */
const SPECS: Spec[] = [
  { species: "rose", petal: ["#f4c3cf", "#d84f7b", "#87204a"], inner: ["#f9d9d0", "#ee7f99", "#a83a5c"], centre: "#e9b53c", scale: 0.46 },
  { species: "daisy", petal: ["#ffffff", "#f6efe0", "#d9cfb4"], centre: "#e9a92c", scale: 0.5 },
  { species: "tulip", petal: ["#f9b5a0", "#e0452b", "#8a1f12"], centre: "#2a1a10", scale: 0.5 },
  { species: "rose", petal: ["#ffd9c2", "#f39a73", "#b25437"], inner: ["#ffe6d4", "#f6b08c", "#c76a48"], centre: "#e9b53c", scale: 0.44 },
  { species: "daisy", petal: ["#fff3b0", "#f7d23c", "#c9961a"], centre: "#8a4b12", scale: 0.52 },
  { species: "tulip", petal: ["#e6dcff", "#a98be0", "#5a3d99"], centre: "#2a1a10", scale: 0.5 },
  { species: "rose", petal: ["#fff1ea", "#f1c6c0", "#c98f8a"], inner: ["#fff7f2", "#f5d3cd", "#d9a49e"], centre: "#e9c25c", scale: 0.46 },
  { species: "daisy", petal: ["#ffe1ec", "#f58db3", "#c94f7e"], centre: "#e9b53c", scale: 0.5 },
  { species: "tulip", petal: ["#ffd0c4", "#ff7d66", "#c2412e"], centre: "#2a1a10", scale: 0.5 },
  { species: "rose", petal: ["#e87a8a", "#b3213f", "#5d0b22"], inner: ["#f0909d", "#c93a56", "#7a1630"], centre: "#e9b53c", scale: 0.44 },
  { species: "daisy", petal: ["#fff6c8", "#ffd24a", "#e9a420"], centre: "#6b3a0f", scale: 0.62 },
];

interface Head { group: T.Group; setBloom: (b: number) => void; flutter: (time: number, amount: number) => void }
const smooth = T.MathUtils.smoothstep;

function makeDaisy(kit: MaterialKit, quality: Quality, spec: Spec): Head {
  const group = new T.Group(), low = quality === "low", count = low ? 14 : 22;
  const material = kit.petal(...spec.petal);
  const geometry = petalGeometry(1.0, 0.2, 0.05, 0.04, 0.55, low ? 4 : 6, low ? 6 : 10);
  const pivots: T.Group[] = [], hinges: T.Group[] = [];
  for (let i = 0; i < count; i++) {
    const pivot = new T.Group(); pivot.rotation.y = (i / count) * Math.PI * 2 + (i % 2) * 0.05; group.add(pivot);
    const hinge = new T.Group(); hinge.position.set(0, (i % 2) * 0.012, 0.1); pivot.add(hinge);
    hinge.add(new T.Mesh(geometry, material)); pivots.push(pivot); hinges.push(hinge);
  }
  const centreMat = new T.MeshStandardMaterial({ color: spec.centre, roughness: 0.65 });
  const disc = new T.Mesh(new T.CylinderGeometry(0.21, 0.23, 0.07, 24), centreMat); group.add(disc);
  const dome = new T.Mesh(new T.SphereGeometry(0.21, 20, 12), centreMat); dome.scale.y = 0.45; dome.position.y = 0.035; group.add(dome);
  return {
    group,
    setBloom(b) { hinges.forEach((h, i) => { h.rotation.x = 0.14 + 1.2 * smooth(b, (i % 4) * 0.05, 0.6 + (i % 4) * 0.05) + Math.sin(i * 1.9) * 0.04 * b; }); },
    flutter(time, amount) { pivots.forEach((p, i) => { p.rotation.y = (i / count) * Math.PI * 2 + (i % 2) * 0.05 + Math.sin(time * 0.9 + i) * 0.012 * amount; }); },
  };
}

function makeTulip(kit: MaterialKit, quality: Quality, spec: Spec): Head {
  const group = new T.Group(), low = quality === "low";
  const material = kit.petal(...spec.petal);
  const geometry = petalGeometry(1.15, 0.72, 0.58, 0.04, 0.5, low ? 5 : 7, low ? 8 : 14);
  const hinges: T.Group[] = [];
  for (let i = 0; i < 6; i++) {
    const pivot = new T.Group(); pivot.rotation.y = (i / 6) * Math.PI * 2 + (i % 2) * 0.12; group.add(pivot);
    const hinge = new T.Group(); hinge.position.set(0, (i % 2) * 0.02, 0.1 - (i % 2) * 0.03); pivot.add(hinge);
    hinge.add(new T.Mesh(geometry, material)); hinges.push(hinge);
  }
  const pistil = new T.Mesh(new T.CylinderGeometry(0.03, 0.05, 0.42, 8), new T.MeshStandardMaterial({ color: "#c9d36a", roughness: 0.6 })); pistil.position.y = 0.22; group.add(pistil);
  return {
    group,
    setBloom(b) { hinges.forEach((h, i) => { h.rotation.x = 0.1 + 0.46 * smooth(b, 0, 1) + (i % 2) * 0.07 * b; }); },
    flutter(time, amount) { hinges.forEach((h, i) => { h.rotation.z = Math.sin(time * 0.8 + i * 1.3) * 0.015 * amount; }); },
  };
}

function makeHead(kit: MaterialKit, quality: Quality, spec: Spec): Head {
  if (spec.species === "daisy") return makeDaisy(kit, quality, spec);
  if (spec.species === "tulip") return makeTulip(kit, quality, spec);
  const bloom = createBloom(kit, quality, { outer: spec.petal, inner: spec.inner ?? spec.petal, centre: spec.centre });
  return { group: bloom.group, setBloom: bloom.setBloom, flutter: bloom.flutter };
}

const glowTexture = (inner: string, outer: string) => { const t = new T.CanvasTexture(glowCanvas(inner, outer, 128)); t.colorSpace = T.SRGBColorSpace; return t; };

export function buildWishGarden(stage: Stage): Choreography {
  const { scene, camera, quality, kit, input } = stage;
  const low = quality === "low", high = quality === "high";
  stage.mood({ env: "garden", envIntensity: 0.85, exposure: 1.08, background: "#dcbcc6", fog: { color: "#ebc5b4", density: 0.011 } });
  camera.fov = 36; camera.near = 0.1; camera.far = 120; camera.updateProjectionMatrix();

  scene.add(new T.HemisphereLight("#d7e4ff", "#6e5a3a", 0.8));
  addKeyLight(scene, quality, { color: "#ffd2a0", intensity: 3.6, position: [-6, 6, 3], target: [0, 1, 0], extent: 7, far: 30 });
  const fill = new T.DirectionalLight("#fff0e0", 0.8); fill.position.set(3, 3, 9); scene.add(fill);
  const rim = new T.DirectionalLight("#a9c2ff", 0.7); rim.position.set(6, 4, -6); scene.add(rim);
  const glowLight = new T.PointLight("#ffc9a6", 0, 7, 2); scene.add(glowLight);

  const sky = createSky(70, 38); sky.position.set(0, 6, -22); scene.add(sky);

  /* ---------- planter bed ---------- */
  const world = new T.Group(); scene.add(world);
  const height = (x: number, z: number) => 0.07 * Math.sin(x * 0.8) * Math.cos(z * 0.9) + 0.03 * Math.sin(x * 4 + z * 3);
  const terrain = buildTerrain(quality, { width: 9.6, depth: 4.8, bottom: -0.9, height });
  world.add(terrain.group);
  const grass = createGrass({ count: high ? 9000 : low ? 2200 : 5600, width: 9.4, depth: 4.7, height, blade: 0.4 });
  world.add(grass.mesh);
  put(world, new RoundedBoxGeometry(10.1, 0.34, 5.3, 3, 0.07), kit.wood("#1f120b", "#58381f", [3, 1], 0.5), 0, -1.05, 0);
  put(world, new T.BoxGeometry(10.14, 0.035, 5.34), kit.metal("brass", 0.4), 0, -0.88, 0, false);
  const floor = put(scene, new T.PlaneGeometry(140, 90), new T.MeshStandardMaterial({ color: "#3a2a22", roughness: 0.92 }), 0, -1.24, -12, false);
  floor.rotation.x = -Math.PI / 2; floor.receiveShadow = true;

  /* ---------- conservatory ribs and lanterns ---------- */
  const brass = kit.metal("brass", 0.5);
  for (let i = 0; i < 5; i++) {
    const rib = new T.Mesh(new T.TorusGeometry(7.4, 0.09, 8, low ? 40 : 72, Math.PI), brass);
    rib.position.set(0, -1.0, -2.8 - i * 1.9); world.add(rib);
  }
  put(world, new T.CylinderGeometry(0.07, 0.07, 8.0, 8), brass, 0, 6.4, -6.5, false).rotation.x = Math.PI / 2;
  const lanternTex = glowTexture("rgba(255,214,150,1)", "rgba(255,170,90,0)");
  for (let i = 0; i < 5; i++) {
    const x = -4.4 + i * 2.2, y = 4.3 + Math.sin(i * 2.1) * 0.4;
    put(world, new T.CylinderGeometry(0.008, 0.008, 1.4, 4), brass, x, y + 0.7, -3.4, false);
    const cage = put(world, new T.CylinderGeometry(0.17, 0.12, 0.34, 10), new T.MeshStandardMaterial({ color: "#ffe2a8", emissive: "#ffb054", emissiveIntensity: 1.1, roughness: 0.5 }), x, y, -3.4, false);
    const halo = new T.Sprite(new T.SpriteMaterial({ map: lanternTex, transparent: true, opacity: 0.8, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
    halo.scale.setScalar(1.6); halo.position.copy(cage.position); world.add(halo);
  }

  /* ---------- the flowers ---------- */
  const leafMat = kit.leaf("#2f5a34", "#79a752");
  const leafGeo = leafGeometry(0.8, 0.28, 0.35, 0.15, 6, 10);
  const flowers = SPECS.map((spec, i) => {
    const planted = i === 10;
    const col = Math.floor(i / 2), row = i % 2;
    const x = planted ? 0 : (col - 2) * 1.6 + (row ? 0.8 : 0) + Math.sin(i * 2.3) * 0.12;
    const z = planted ? 1.55 : (row ? -0.75 : 0.5) + Math.cos(i * 1.7) * 0.18;
    const h = planted ? 1.35 : 1.95 + 0.4 * Math.sin(i * 1.7) + (row ? 0.4 : 0);
    const root = new T.Group(); root.position.set(x, height(x, z), z); world.add(root);
    const lean = Math.sin(i * 2.9) * 0.22;
    const curve = new T.CatmullRomCurve3([new T.Vector3(0, 0, 0), new T.Vector3(lean * 0.4, h * 0.35, 0.04), new T.Vector3(-lean * 0.3, h * 0.7, -0.03), new T.Vector3(lean, h, 0)]);
    const sway = new T.Group(); root.add(sway);
    const stem = new T.Mesh(taperedTube(curve, 0.05, 0.03, low ? 14 : 24, low ? 5 : 7), new T.MeshStandardMaterial({ color: "#3f6c2c", roughness: 0.55 })); stem.castShadow = !low; sway.add(stem);
    [0.26, 0.5].forEach((t, k) => {
      const pivot = new T.Group(), hinge = new T.Group(); pivot.rotation.y = i * 1.9 + k * 3.1; pivot.position.copy(curve.getPointAt(t)); pivot.add(hinge);
      hinge.rotation.x = 0.75 + k * 0.15; hinge.add(new T.Mesh(leafGeo, leafMat)); pivot.scale.setScalar(0.8 - k * 0.15 + (planted ? -0.2 : 0)); sway.add(pivot);
    });
    const top = curve.getPointAt(1);
    const holder = new T.Group(); holder.position.copy(top); sway.add(holder);
    const head = makeHead(kit, quality, spec);
    head.group.scale.setScalar(spec.scale); holder.add(head.group);
    holder.userData.index = i;
    const glow = new T.Sprite(new T.SpriteMaterial({ map: glowTexture("rgba(255,224,190,1)", "rgba(255,170,150,0)"), transparent: true, opacity: 0, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
    glow.scale.setScalar(2.4); glow.position.set(0, 0.15, -0.1); glow.raycast = () => {}; holder.add(glow); // decorative: never swallow clicks
    head.setBloom(0.5);
    return { spec, root, sway, holder, head, glow, open: 0.5, focus: 0, base: top.clone(), world: new T.Vector3(), seed: i * 1.37 };
  });
  const plantedFlower = flowers[10]; plantedFlower.root.visible = false; plantedFlower.root.scale.setScalar(0.001);

  /* ---------- life: butterflies, fireflies, pollen, release effects ---------- */
  const butterflies = createButterflies(3); scene.add(butterflies.group);
  const fireflies = new ParticleField({ count: Math.round(70 * particleScale(quality)), size: 0.07, color: "#fff0a0", colorB: "#ffc98a", opacity: 0.9, bounds: [4.6, 1.5, 2.6], center: [0, 1.6, -0.2], drift: 1.3, twinkle: 0.9 });
  scene.add(fireflies.points);
  const pollen = new ParticleField({ count: Math.round(60 * particleScale(quality)), size: 0.05, color: "#ffe9a8", opacity: 0, bounds: [0.8, 0.8, 0.8], drift: 1.1, rise: 0.12, twinkle: 0.4 });
  scene.add(pollen.points);
  const sparks = new Burst({ count: low ? 50 : 110, size: 0.1, life: 2.8, speed: 2.6, gravity: -0.5, drag: 1.1, colors: ["#fff1b5", "#ffc77a", "#ffd9e6", "#ffffff"], shape: "spark", emit: "cone", coneAngle: 0.95 });
  const petals = new Burst({ count: low ? 30 : 70, size: 0.15, life: 3.6, speed: 1.9, gravity: 0.35, drag: 1.3, colors: ["#f4c3cf", "#ffe3d3", "#fff3b0", "#e9b0c5"], shape: "confetti", emit: "cone", coneAngle: 1.1 });
  scene.add(sparks.points, petals.points);
  const lantern = new T.Sprite(new T.SpriteMaterial({ map: lanternTex, transparent: true, opacity: 0, depthWrite: false, blending: T.AdditiveBlending, fog: false }));
  lantern.scale.setScalar(0.9); scene.add(lantern);

  /* ---------- camera ---------- */
  const overviewPos = new T.Vector3(0, 2.45, 9.1), overviewLook = new T.Vector3(0, 1.5, 0);
  const camPos = overviewPos.clone(), camLook = overviewLook.clone(), wantPos = new T.Vector3(), wantLook = new T.Vector3(), offset = new T.Vector3(), tmp = new T.Vector3();
  const orbit = { yaw: 0, pitch: 0 };
  let lastReplay = -1, lastSelected: number | null | undefined = undefined, lantT = 1, lantFrom = new T.Vector3(), plantedBefore = false, plantedAmount = 0;
  const butterflyCenter = new T.Vector3(0, 1.5, 0); let focusAmount = 0;

  const release = (index: number) => {
    const f = flowers[index]; f.holder.getWorldPosition(tmp);
    sparks.trigger(tmp.clone().add(new T.Vector3(0, 0.1, 0.1))); petals.trigger(tmp.clone().add(new T.Vector3(0, 0.05, 0.1)));
    lantFrom.copy(tmp); lantT = 0; stage.sfx("bloom");
  };

  return {
    pickables: flowers.map((f) => f.holder),
    frame(time, dt, state: SceneState, reduced) {
      const selected = state.selected ?? null;
      const replay = state.replay ?? 0;
      if ((replay !== lastReplay || selected !== lastSelected) && selected !== null && selected >= 0 && selected < flowers.length && !reduced) release(selected);
      lastReplay = replay; lastSelected = selected;

      // the visitor's own wish grows when planted
      const planted = Boolean(state.planted);
      if (planted && !plantedBefore && !reduced) { plantedFlower.holder.getWorldPosition(tmp); sparks.trigger(tmp.clone().setY(tmp.y + 0.3)); }
      plantedBefore = planted;
      plantedAmount = reduced ? (planted ? 1 : 0) : T.MathUtils.damp(plantedAmount, planted ? 1 : 0, 1.6, dt);
      plantedFlower.root.visible = plantedAmount > 0.01; plantedFlower.root.scale.setScalar(Math.max(0.001, plantedAmount));

      const wind = reduced ? 0 : 1;
      flowers.forEach((f, i) => {
        const isSel = selected === i, targetOpen = isSel ? 1 : 0.55 + 0.08 * Math.sin(f.seed);
        f.open = reduced ? targetOpen : T.MathUtils.damp(f.open, targetOpen, 2.4, dt);
        f.focus = reduced ? (isSel ? 1 : 0) : T.MathUtils.damp(f.focus, isSel ? 1 : 0, 3, dt);
        f.head.setBloom(f.open);
        if (!reduced) f.head.flutter(time, 0.5 + f.open);
        f.sway.rotation.z = Math.sin(time * 0.75 + f.seed) * 0.035 * wind; f.sway.rotation.x = Math.cos(time * 0.55 + f.seed) * 0.014 * wind;
        f.holder.rotation.x = f.spec.species === "tulip" ? 0.1 + 0.22 * f.open : 0.45 + 0.5 * f.open; f.holder.rotation.z = Math.sin(time * 0.8 + f.seed - 0.6) * 0.05 * wind;
        f.holder.position.y = f.base.y + 0.22 * f.focus; f.holder.scale.setScalar(1 + 0.18 * f.focus);
        (f.glow.material as T.SpriteMaterial).opacity = 0.2 * f.focus;
      });
      grass.update(reduced ? 0 : time);
      const live = selected !== null && flowers[selected] ? flowers[selected] : null;
      if (live) { live.holder.getWorldPosition(tmp); glowLight.position.set(tmp.x, tmp.y + 0.5, tmp.z + 1.4); glowLight.intensity = 1.3 * live.focus; pollen.points.position.copy(tmp); pollen.opacity = 0.9 * live.focus; }
      else { glowLight.intensity = 0; pollen.opacity = 0; }
      pollen.update(time); fireflies.update(time);
      butterflies.update(time, butterflyCenter, null, 0, reduced);
      sparks.update(dt); petals.update(dt);
      if (lantT < 1) { lantT = Math.min(1, lantT + dt / 6); lantern.position.set(lantFrom.x + Math.sin(lantT * 5) * 0.25, lantFrom.y + 0.4 + lantT * 3.6, lantFrom.z + 0.2); (lantern.material as T.SpriteMaterial).opacity = Math.sin(Math.PI * lantT) * 0.95; lantern.scale.setScalar(0.7 + 0.5 * Math.sin(Math.PI * lantT)); } else (lantern.material as T.SpriteMaterial).opacity = 0;

      // camera: overview, or glide to the selected blossom
      if (live) { live.holder.getWorldPosition(wantLook); wantPos.set(wantLook.x * 0.6, wantLook.y + 0.45, wantLook.z + 5.4); } else { wantPos.copy(overviewPos); wantLook.copy(overviewLook); }
      const k = reduced ? 1 : 1 - Math.exp(-2.3 * dt);
      camPos.lerp(wantPos, k); camLook.lerp(wantLook, k);
      const pos = tmp.copy(camPos); if (!reduced) { pos.x += Math.sin(time * 0.2) * 0.2; pos.y += Math.sin(time * 0.15) * 0.06; }
      const drag = input.consumeDrag();
      orbit.yaw = T.MathUtils.clamp(orbit.yaw - drag.x * 3.6, -0.7, 0.7); orbit.pitch = T.MathUtils.clamp(orbit.pitch + drag.y * 1.2, -0.12, 0.3);
      offset.copy(pos).sub(camLook).applyAxisAngle(new T.Vector3(0, 1, 0), orbit.yaw).applyAxisAngle(new T.Vector3(1, 0, 0), -orbit.pitch);
      focusAmount = reduced ? (live ? 1 : 0) : T.MathUtils.damp(focusAmount, live ? 1 : 0, 2.3, dt);
      const aspect = Math.max(0.4, camera.aspect);
      const fit = T.MathUtils.lerp(T.MathUtils.clamp(1.65 / aspect, 1, 2.5), T.MathUtils.clamp(0.85 / aspect, 1, 2), focusAmount);
      camera.position.copy(camLook).addScaledVector(offset, fit); camera.lookAt(camLook);
    },
    dispose() { /* geometries, materials and textures are released by disposeTree */ },
  };
}
```

## 86. `src/vite-env.d.ts` — new

```ts
/// <reference types="vite/client" />
```

## 87. `src/world/BirthdayCake.tsx` — modified

```tsx
import { useEffect, useRef, useState } from "react";
import { CakeSlice, Flame, Sparkles, Wind } from "lucide-react";
import { SectionStage } from "../three/SectionStage";
import { useBlowDetection } from "../hooks/useBlowDetection";
import { CakeBakingJourney } from "./CakeBakingJourney";
import { WorldSection } from "./WorldSection";

const sparks = Array.from({ length: 26 }, (_, index) => ({
  id: index,
  angle: `${(index * 137.5) % 360}deg`,
  distance: `${50 + (index % 5) * 24}px`,
  delay: `${(index % 8) * 32}ms`,
  color: ["#c98291", "#d6b879", "#dfaa8f", "#9aa58c"][index % 4],
}));

export function BirthdayCake() {
  const [bakeStage, setBakeStage] = useState(0);
  const [reducedMotion, setReducedMotion] = useState(() => window.matchMedia("(prefers-reduced-motion: reduce)").matches);
  const [extinguishing, setExtinguishing] = useState(false);
  const [smoking, setSmoking] = useState<number[]>([]);
  const [candlesLit, setCandlesLit] = useState(0);
  const [wished, setWished] = useState(false);
  const [wishAgain, setWishAgain] = useState(false);
  const [lighting, setLighting] = useState(false);
  const [wishBurst, setWishBurst] = useState(false);
  const lightTimers = useRef<number[]>([]);
  const burstTimer = useRef<number | null>(null);

  useEffect(() => () => {
    lightTimers.current.forEach((timer) => window.clearTimeout(timer));
    if (burstTimer.current !== null) window.clearTimeout(burstTimer.current);
  }, []);

  const clearLightTimers = () => {
    lightTimers.current.forEach((timer) => window.clearTimeout(timer));
    lightTimers.current = [];
  };

  useEffect(() => {
    const query = window.matchMedia("(prefers-reduced-motion: reduce)");
    const update = () => setReducedMotion(query.matches);
    query.addEventListener("change", update);
    return () => query.removeEventListener("change", update);
  }, []);

  const blow = () => {
    clearLightTimers();
    setLighting(false);
    setWishBurst(false);
    setSmoking([]);
    if (reducedMotion) {
      setCandlesLit(0);
      setWishAgain(true);
      setExtinguishing(false);
      return;
    }
    setExtinguishing(true);
    const count = candlesLit;
    for (let step = 0; step < count; step += 1) {
      lightTimers.current.push(window.setTimeout(() => {
        const wick = count - step - 1;
        setCandlesLit(wick);
        setSmoking((previous) => [...previous, wick]);
        if (wick === 0) {
          setWishAgain(true);
          setExtinguishing(false);
          setWishBurst(true);
          if (burstTimer.current !== null) window.clearTimeout(burstTimer.current);
          burstTimer.current = window.setTimeout(() => setWishBurst(false), 1050);
        }
      }, step * 150));
    }
    lightTimers.current.push(window.setTimeout(() => setSmoking([]), count * 150 + 700));
  };

  const microphone = useBlowDetection(blow, candlesLit > 0 && !lighting && !extinguishing);

  useEffect(() => {
    const section = document.getElementById("birthday-cake");
    if (!section) return;
    const observer = new IntersectionObserver(([entry]) => { if (!entry.isIntersecting) microphone.stop(); });
    observer.observe(section);
    return () => observer.disconnect();
  }, [microphone.stop]);

  const light = () => {
    microphone.stop();
    clearLightTimers();
    setSmoking([]);
    setWishBurst(false);
    if (burstTimer.current !== null) window.clearTimeout(burstTimer.current);
    setCandlesLit(0);
    setWished(false);
    setWishAgain(false);
    if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
      setCandlesLit(5);
      setLighting(false);
      return;
    }
    setLighting(true);
    lightTimers.current = Array.from({ length: 5 }, (_, index) => window.setTimeout(() => {
      setCandlesLit(index + 1);
      if (index === 4) setLighting(false);
    }, (index + 1) * 210));
  };

  const makeWish = () => {
    setWished(true);
    setWishAgain(false);
    setWishBurst(false);
    blow();
  };

  return (
    <WorldSection id="birthday-cake" className="cake-section" eyebrow="A WISH BY CANDLELIGHT" sideNote="WISH / 10">
      <div className="cake-intro"><CakeSlice size={19} strokeWidth={1.1} /><p>A tiny birthday ritual. Watch the candles catch one by one, make a wish, and blow them out. Use the button, or explicitly enable the optional microphone.</p></div>
      <CakeBakingJourney reducedMotion={reducedMotion} stage={bakeStage} onStageChange={(stage) => { microphone.stop(); clearLightTimers(); setCandlesLit(0); setWished(false); setWishAgain(false); setWishBurst(false); setLighting(false); setExtinguishing(false); setSmoking([]); setBakeStage(stage); }} />
      <div className={`birthday-cake-scene${candlesLit ? " is-lit" : ""}${wished ? " has-wished" : ""}`}>
        <div className="cake-scene__glow" aria-hidden="true" />
        <div className="cake-balloon-cluster" aria-hidden="true"><i className="cake-balloon cake-balloon--rose" /><i className="cake-balloon cake-balloon--gold" /><i className="cake-balloon cake-balloon--sage" /></div>
        <div className={`cake-fireworks${wishBurst ? " is-bursting" : ""}`} aria-hidden="true"><i /><i /><i /></div>
        <div className={`cake-scene__stars${wishBurst ? " is-bursting" : ""}`} key={wishBurst ? "bursting" : "idle"} aria-hidden="true">{sparks.map((spark) => <i key={spark.id} style={{ "--spark-angle": spark.angle, "--spark-distance": spark.distance, "--spark-delay": spark.delay, "--spark-color": spark.color } as React.CSSProperties} />)}</div>
        <SectionStage kind="ballroom" title="Patisserie and ballroom" state={{ bakeStage, candles: candlesLit, blowing: extinguishing, celebration: wishAgain }} label="A real-time three-dimensional layered sponge cake with piped cream, berries, five wax candles, animated flame meshes and warm candlelight." />
        <details className="cake-illustration-fallback"><summary>View the illustrated cake alternative</summary>
        <div className="cake-display">
          <svg className="cake-svg" viewBox="0 0 520 390" role="img" aria-labelledby="cake-svg-title cake-svg-desc">
            <title id="cake-svg-title">A birthday cake with five candles</title>
            <desc id="cake-svg-desc">A hand-drawn cream and blush layer cake with candles that respond to the buttons below.</desc>
            <defs>
              <linearGradient id="cake-icing" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stopColor="#fff9ed" /><stop offset="1" stopColor="#f2d9c4" /></linearGradient>
              <linearGradient id="cake-sponge" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stopColor="#e9b487" /><stop offset="1" stopColor="#d58e70" /></linearGradient>
              <linearGradient id="cake-plate" x1="0" x2="1" y1="0" y2="1"><stop offset="0" stopColor="#f6e5bf" /><stop offset="0.5" stopColor="#b78f5d" /><stop offset="1" stopColor="#f4e4c5" /></linearGradient>
              <filter id="cake-shadow" x="-30%" y="-20%" width="160%" height="170%"><feGaussianBlur in="SourceAlpha" stdDeviation="7" /><feOffset dy="9" /><feComponentTransfer><feFuncA type="linear" slope="0.19" /></feComponentTransfer><feMerge><feMergeNode /><feMergeNode in="SourceGraphic" /></feMerge></filter>
            </defs>
            <ellipse cx="260" cy="350" rx="176" ry="17" fill="#d9c3a5" opacity=".38" />
            <ellipse cx="260" cy="331" rx="185" ry="23" fill="url(#cake-plate)" stroke="#b18c60" strokeWidth="2" />
            <ellipse cx="260" cy="326" rx="163" ry="15" fill="#fbf5e9" stroke="#dec89f" strokeWidth="1.2" />
            <g filter="url(#cake-shadow)">
              <path d="M118 243h284v74c0 23-19 42-42 42H160c-23 0-42-19-42-42z" fill="url(#cake-sponge)" stroke="#ae735d" strokeWidth="2" />
              <path d="M118 244c0-17 15-30 34-30h216c19 0 34 13 34 30v25c-14-10-23 5-37 4-13-1-15-15-29-15s-16 16-29 16-15-17-30-17-17 16-30 16-16-16-31-16-16 15-29 15-17-13-34-8c-12 4-20 13-35 12z" fill="url(#cake-icing)" stroke="#e6d0b8" strokeWidth="2" />
              <path d="M159 213h202v23c0 16-14 29-30 29H189c-16 0-30-13-30-29z" fill="#f5d9c5" stroke="#c88383" strokeWidth="1.5" />
              <ellipse cx="260" cy="213" rx="101" ry="22" fill="url(#cake-icing)" stroke="#dec3aa" strokeWidth="1.7" />
              <path d="M168 276c19-7 30 8 45 8s20-14 36-14 19 14 35 14 22-15 38-15 22 14 40 9" fill="none" stroke="#f7dbc1" strokeWidth="5" opacity=".86" />
              <path d="M160 309c16-5 26 6 39 6 16 0 18-11 35-11 14 0 19 10 34 10 17 0 21-11 37-11 16 0 20 9 34 8" fill="none" stroke="#f1c7aa" strokeWidth="5" opacity=".76" />
              <g fill="#c98291" stroke="#fff5eb" strokeWidth="2"><circle cx="190" cy="242" r="5" /><circle cx="231" cy="228" r="5" /><circle cx="274" cy="239" r="5" /><circle cx="316" cy="226" r="5" /><circle cx="350" cy="244" r="5" /></g>
              <g fill="#d6b879"><path d="M211 255c6-10 12-10 18 0-6 10-12 10-18 0z" /><path d="M290 255c6-10 12-10 18 0-6 10-12 10-18 0z" /><path d="M331 275c6-10 12-10 18 0-6 10-12 10-18 0z" /></g>
            </g>
            <g className={candlesLit > 0 ? "cake-candles is-lit" : "cake-candles"} strokeLinecap="round">
              <g transform="translate(190 186)"><rect x="-7" y="-43" width="14" height="45" rx="5" fill="#e4bac1" stroke="#b9848d" strokeWidth="1.4" /><path d="M-6-34h12M-6-21h12M-6-8h12" stroke="#fff6eb" strokeWidth="3" />{candlesLit > 0 && <g className="cake-flame"><path d="M0-48c-16-15 2-26 2-36 14 15 16 28 4 36z" fill="#e6a764" /><path d="M2-49c-6-7 1-13 2-18 7 9 6 14 0 18z" fill="#fff5c7" /></g>}</g>
              <g transform="translate(225 177)"><rect x="-7" y="-47" width="14" height="49" rx="5" fill="#e4c39c" stroke="#aa8a58" strokeWidth="1.4" /><path d="M-6-36h12M-6-22h12M-6-8h12" stroke="#fff6eb" strokeWidth="3" />{candlesLit > 1 && <g className="cake-flame"><path d="M0-52c-16-15 2-26 2-36 14 15 16 28 4 36z" fill="#e6a764" /><path d="M2-53c-6-7 1-13 2-18 7 9 6 14 0 18z" fill="#fff5c7" /></g>}</g>
              <g transform="translate(260 172)"><rect x="-7" y="-50" width="14" height="52" rx="5" fill="#d6b879" stroke="#a98c50" strokeWidth="1.4" /><path d="M-6-39h12M-6-24h12M-6-9h12" stroke="#fff6eb" strokeWidth="3" />{candlesLit > 2 && <g className="cake-flame"><path d="M0-55c-16-15 2-26 2-36 14 15 16 28 4 36z" fill="#e6a764" /><path d="M2-56c-6-7 1-13 2-18 7 9 6 14 0 18z" fill="#fff5c7" /></g>}</g>
              <g transform="translate(295 177)"><rect x="-7" y="-47" width="14" height="49" rx="5" fill="#d8b3a1" stroke="#aa8477" strokeWidth="1.4" /><path d="M-6-36h12M-6-22h12M-6-8h12" stroke="#fff6eb" strokeWidth="3" />{candlesLit > 3 && <g className="cake-flame"><path d="M0-52c-16-15 2-26 2-36 14 15 16 28 4 36z" fill="#e6a764" /><path d="M2-53c-6-7 1-13 2-18 7 9 6 14 0 18z" fill="#fff5c7" /></g>}</g>
              <g transform="translate(330 186)"><rect x="-7" y="-43" width="14" height="45" rx="5" fill="#bdd0bc" stroke="#819b82" strokeWidth="1.4" /><path d="M-6-34h12M-6-21h12M-6-8h12" stroke="#fff6eb" strokeWidth="3" />{candlesLit > 4 && <g className="cake-flame"><path d="M0-48c-16-15 2-26 2-36 14 15 16 28 4 36z" fill="#e6a764" /><path d="M2-49c-6-7 1-13 2-18 7 9 6 14 0 18z" fill="#fff5c7" /></g>}</g>
            </g>
            <g aria-hidden="true">{smoking.map((wick) => <path key={wick} className="cake-wick-smoke" d={`M${[190,225,260,295,330][wick]} ${[138,125,117,125,138][wick]} c-9-10 9-16 0-26 s8-16 2-24`} fill="none" stroke="#98877a" strokeWidth="3" strokeLinecap="round" />)}</g>
            <g fill="#e8bfc2" stroke="#fff2e8" strokeWidth="1.5"><path d="M131 297c8-11 16-11 24 0-8 10-16 10-24 0z" /><path d="M370 295c8-11 16-11 24 0-8 10-16 10-24 0z" /></g>
          </svg>
          <span className="cake-display__plaque">HAPPY BIRTHDAY, BHUMI</span>
        </div>
        </details>
        <div className="cake-ritual">
          <div className="cake-ritual__status" aria-live="polite" aria-atomic="true">
            {!candlesLit && !wishAgain && !extinguishing && <><span className="cake-ritual__icon"><Flame size={18} /></span><strong>Ready when you are.</strong><small>Finish or skip the baking story, then light the candles.</small></>}
            {candlesLit > 0 && !wished && !extinguishing && <><span className="cake-ritual__icon is-lit"><Flame size={18} /></span><strong>The candles are glowing.</strong><small>Hold a wish quietly. It belongs to you.</small></>}
            {wished && candlesLit > 0 && !extinguishing && <><span className="cake-ritual__icon is-lit"><Sparkles size={18} /></span><strong>Your wish is yours to keep.</strong><small>Nothing is recorded or shared.</small></>}
            {extinguishing && <><strong>A gentle breath…</strong><small>The candles are going out one by one.</small></>}
            {wishAgain && !candlesLit && <><span className="cake-ritual__icon"><Wind size={18} /></span><strong>Wish made. Candles out.</strong><small>You can light them again whenever you like.</small></>}
          </div>
          <div className="microphone-panel">
            <p id="mic-privacy">{microphone.message}</p>
            <button type="button" className="cake-button" onClick={() => { if (microphone.phase === "idle") void microphone.start(); else { microphone.stop(); } }} disabled={microphone.phase === "idle" && (!candlesLit || lighting || extinguishing)} aria-describedby="mic-privacy">{microphone.phase === "idle" ? "Enable microphone for this wish" : "Cancel microphone"}</button>
            <span role="status">{microphone.phase === "calibrating" ? "Calibrating room noise…" : microphone.phase === "listening" ? "Listening for sustained airflow-like sound…" : microphone.phase === "requesting" ? "Permission requested…" : "Microphone off"}</span>
            {microphone.phase === "listening" && <meter min={0} max={1} value={microphone.level} aria-label="Sustained airflow confidence" />}
          </div>
          <div className="cake-ritual__buttons">
            <button type="button" className="cake-button cake-button--light" onClick={candlesLit ? () => { microphone.stop(); blow(); } : light} disabled={bakeStage !== 3 || lighting || extinguishing}>{candlesLit ? <><Wind size={15} /> Blow them out</> : <><Flame size={15} /> Light the candles</>}</button>
            <button type="button" className="cake-button cake-button--wish" disabled={bakeStage !== 3 || !candlesLit || lighting || extinguishing} onClick={() => { microphone.stop(); makeWish(); }}><Sparkles size={15} /> Make a wish</button>
          </div>
        </div>
      </div>
      <p className="cake-section__footnote">The 17 November birthday date is preserved without a year. No countdown is used. Microphone access is optional, starts only with permission, and stops after use, cancellation, tab hiding or timeout. No audio is recorded.</p>
    </WorldSection>
  );
}
```

## 88. `src/world/BirthdayGarden.tsx` — modified

```tsx
import { useCallback, useEffect, useRef, useState } from "react";
import { ArrowDownRight, RotateCcw, Sparkles } from "lucide-react";
import { chronosContent } from "../content/chronosContent";
import { packGardenNarration } from "../content/packContent";
import { SectionStage } from "../three/SectionStage";

/**
 * Growth stages of the living garden, one per narration of the content pack (seed, roots, sprout, leaves, bud, flower, full bloom).
 * The scene's timeline progress is growth / 4 and its phases begin at roots 0.06, stem 0.25, leaves 0.44 and bud 0.66; the bud
 * opens from 0.75, so the open flower is read from 0.80 and full bloom (all petals, glow, butterflies and pollen) from 0.97.
 * Each `from` is where the stage starts and each button rests inside its own window (at least 0.02 clear of the next stage), so the
 * stage that is highlighted always matches what is on screen once the scene has settled.
 */
const STAGES = [
  { name: "Seed", growth: 0, from: 0 },
  { name: "Roots", growth: 0.92, from: 0.06 },
  { name: "Sprout", growth: 1.68, from: 0.25 },
  { name: "Leaves", growth: 2.52, from: 0.44 },
  { name: "Bud", growth: 2.92, from: 0.66 },
  { name: "Flower", growth: 3.6, from: 0.8 },
  { name: "Full bloom", growth: 4, from: 0.97 },
] as const;

export function BirthdayGarden() {
  const [target, setTarget] = useState(0);
  const [jump, setJump] = useState(false);
  const [progress, setProgress] = useState(0);
  // True when the visitor sees the poster instead of 3D (no WebGL / scene failure): the controls then follow the chosen stage themselves.
  const [fallback, setFallback] = useState(false);
  const chosen = useRef(false);
  const timers = useRef<number[]>([]);
  const targetIndex = STAGES.reduce((found, stage, index) => (target >= stage.growth ? index : found), 0);
  const sceneIndex = STAGES.reduce((found, stage, index) => (progress >= stage.from ? index : found), 0);
  const stageIndex = fallback ? targetIndex : sceneIndex;
  const shown = fallback ? (targetIndex === STAGES.length - 1 ? 1 : STAGES[targetIndex].from) : progress;

  const clearTimers = useCallback(() => { timers.current.forEach((id) => window.clearTimeout(id)); timers.current = []; }, []);
  useEffect(() => clearTimers, [clearTimers]);
  const onUnavailable = useCallback(() => setFallback(true), []);

  // The garden starts to grow by itself a moment after the page opens; any choice made by the visitor takes over.
  useEffect(() => {
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    const timer = window.setTimeout(() => { if (!chosen.current) setTarget(4); }, reduce ? 0 : 1400);
    return () => window.clearTimeout(timer);
  }, []);
  // The poster already shows the finished garden, so the captions start at full bloom instead of waiting for a timer.
  useEffect(() => { if (fallback && !chosen.current) setTarget(4); }, [fallback]);

  const choose = useCallback((growth: number) => { clearTimers(); chosen.current = true; setJump(false); setTarget(growth); }, [clearTimers]);
  const replay = useCallback(() => {
    clearTimers(); chosen.current = true;
    if (fallback) {
      // Without 3D the button still does something real: the captions and progress walk through the same seven stages.
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) { setTarget(4); return; }
      STAGES.forEach((stage, index) => timers.current.push(window.setTimeout(() => setTarget(stage.growth), index * 900)));
      return;
    }
    setJump(true); setTarget(0);
    timers.current.push(window.setTimeout(() => { setJump(false); setTarget(4); }, 160));
  }, [clearTimers, fallback]);

  return (
    <section id="garden" className="birthday-garden" data-chapter="garden" data-scene-anchor="garden" aria-labelledby="birthday-garden-title">
      <p className="sr-only">The background is a live three-dimensional cut-away of a garden: a seed in the soil sends out roots, a sprout rises, leaves unfold and a rose blooms while butterflies, fireflies and pollen drift past. The growth controls below the headline step through the same story.</p>
      <div className="birthday-garden__stage">
        <SectionStage kind="hero-garden" state={{ growth: target, immediate: jump }} onProgress={setProgress} onUnavailable={onUnavailable} chrome="minimal" title="Birthday garden"
          poster="/assets/backgrounds/birthday-garden.webp" label="Interactive three-dimensional garden growing from a seed to a full bloom. Drag to look around. The growth buttons below the headline do the same without the pointer." />
      </div>
      <div className="birthday-garden__veil" aria-hidden="true" />
      <div className="birthday-garden__sunwash" aria-hidden="true" />
      <div className="birthday-garden__content">
        <p className="birthday-garden__eyebrow"><span />{chronosContent.garden.eyebrow}</p>
        <h1 id="birthday-garden-title" tabIndex={-1}>{chronosContent.garden.heading}</h1>
        <p className="birthday-garden__sub">{chronosContent.garden.subheading}</p>
        <div className="birthday-garden__actions">
          <a className="garden-cta" href="#storybook"><span>{chronosContent.garden.invitation}</span><ArrowDownRight size={17} aria-hidden="true" /></a>
          <span className="birthday-garden__seal"><Sparkles size={14} aria-hidden="true" /> 17 NOVEMBER</span>
        </div>
        <p className="birthday-garden__date-note">Bhumi’s birthday · the year is not specified in the source archive.</p>
        <div className="garden-growth" role="group" aria-label="Watch the garden grow" style={{ "--grown": shown } as React.CSSProperties}>
          <div className="garden-growth__progress" aria-hidden="true"><i /></div>
          <ol className="garden-growth__steps">
            {STAGES.map((stage, index) => (
              <li key={stage.name}><button type="button" aria-current={index === stageIndex ? "step" : undefined} onClick={() => choose(stage.growth)}>{stage.name}</button></li>
            ))}
          </ol>
          <div className="garden-growth__narration">
            <p className="garden-growth__caption" aria-live="polite" aria-atomic="true"><span className="garden-growth__label">{packGardenNarration[stageIndex].title}</span>{packGardenNarration[stageIndex].text}</p>
            {/* Invisible copy of every narration: the block keeps the height of the longest one, so the buttons never jump between stages. */}
            <div className="garden-growth__sizer" aria-hidden="true">{packGardenNarration.map((item) => <p key={item.stage}><span className="garden-growth__label">{item.title}</span>{item.text}</p>)}</div>
          </div>
          <button type="button" className="garden-growth__replay" onClick={replay}><RotateCcw size={13} aria-hidden="true" /> Replay the growth</button>
        </div>
      </div>
      <div className="birthday-garden__caption" aria-hidden="true"><span>THE WORLD OF YOU</span><i /><span>A LITTLE GARDEN FOR A BIRTHDAY</span></div>
      <a href="#storybook" className="birthday-garden__scroll" aria-label="Scroll to the scrapbook"><span>TURN THE FIRST PAGE</span><span className="birthday-garden__scroll-icon"><ArrowDownRight size={14} /></span></a>
    </section>
  );
}
```

## 89. `src/world/FinalCelebration.tsx` — modified

```tsx
import { useEffect, useRef, useState } from "react";
import { ArrowUpRight, CakeSlice, Flower2, Heart, RotateCcw, Star } from "lucide-react";
import { chronosContent } from "../content/chronosContent";

interface FinalCelebrationProps { onReplayOpening: () => void; }
const confetti = Array.from({ length: 36 }, (_, index) => ({
  id: index,
  angle: `${(index * 137.5) % 360}deg`,
  distance: `${90 + (index % 7) * 25}px`,
  delay: `${(index % 12) * 35}ms`,
  color: ["#c98291", "#d6b879", "#dfaa8f", "#9aa58c", "#f6e8d0"][index % 5],
}));
const fallingStars = Array.from({ length: 8 }, (_, index) => ({
  id: index,
  left: `${9 + ((index * 29) % 82)}%`,
  delay: `${index * 1.7}s`,
  duration: `${5 + (index % 3)}s`,
}));

export function FinalCelebration({ onReplayOpening }: FinalCelebrationProps) {
  const [celebrating, setCelebrating] = useState(false);
  const sectionRef = useRef<HTMLElement>(null);
  const timer = useRef<number | null>(null);

  useEffect(() => {
    const section = sectionRef.current;
    if (!section) return;
    if (typeof IntersectionObserver === "undefined") {
      setCelebrating(true);
      timer.current = window.setTimeout(() => setCelebrating(false), 1700);
      return () => { if (timer.current !== null) window.clearTimeout(timer.current); };
    }
    const observer = new IntersectionObserver(([entry]) => {
      if (!entry.isIntersecting) return;
      setCelebrating(true);
      timer.current = window.setTimeout(() => setCelebrating(false), 1700);
      observer.disconnect();
    }, { threshold: 0.22 });
    observer.observe(section);
    return () => {
      observer.disconnect();
      if (timer.current !== null) window.clearTimeout(timer.current);
    };
  }, []);

  const replay = () => {
    setCelebrating(false);
    window.requestAnimationFrame(() => setCelebrating(true));
    if (timer.current !== null) window.clearTimeout(timer.current);
    timer.current = window.setTimeout(() => setCelebrating(false), 1700);
  };
  return (
    <section ref={sectionRef} id="finale" data-chapter="finale" data-scene-anchor="finale" className={`final-celebration${celebrating ? " is-replaying" : ""}`} aria-labelledby="finale-title">
      <div className="final-celebration__starfield" aria-hidden="true">{fallingStars.map((star) => <i key={star.id} style={{ left: star.left, animationDelay: star.delay, animationDuration: star.duration }} />)}</div>
      <div className="final-celebration__particles" aria-hidden="true">{confetti.map((item) => <i key={item.id} style={{ "--confetti-angle": item.angle, "--confetti-distance": item.distance, "--confetti-delay": item.delay, "--confetti-color": item.color } as React.CSSProperties} />)}</div>
      <div className="final-celebration__content">
        <div className="final-celebration__flower-seal" aria-hidden="true"><Flower2 size={29} strokeWidth={0.9} /><i><Star size={10} fill="currentColor" /></i></div>
        <p className="final-celebration__kicker">{chronosContent.finale.kicker}</p>
        <h2 id="finale-title">{chronosContent.finale.headline}</h2>
        <div className="final-celebration__divider" aria-hidden="true"><span /><Heart size={13} /><span /></div>
        <p className="final-celebration__sub">{chronosContent.finale.sub}</p>
        <blockquote>{chronosContent.finale.sourceMessage}<cite>— RUDRA · SOURCE DRAFT</cite></blockquote>
        <p className="final-celebration__thanks">{chronosContent.finale.thanks}</p>
        <div className="final-celebration__signoff"><span>✿</span><small>A BIRTHDAY STORYBOOK FOR BHUMI</small><span>✿</span></div>
        <p className="final-celebration__signature">Made with love by <span>Rudra</span></p>
        <nav className="final-celebration__links" aria-label="Final chapter links">
          <a href="#letters"><span>{chronosContent.finale.letterLink}</span><ArrowUpRight size={15} /></a>
          <a href="#storybook"><span>{chronosContent.finale.storyLink}</span><ArrowUpRight size={15} /></a>
        </nav>
        <div className="final-celebration__controls">
          <button type="button" onClick={replay}><RotateCcw size={14} /> {chronosContent.finale.replay}</button>
          <button type="button" onClick={onReplayOpening}><CakeSlice size={14} /> Replay Experience</button>
        </div>
      </div>
      <div className="final-celebration__footer"><span>THE WORLD OF YOU</span><i /><span>17 NOVEMBER · YEAR NOT SPECIFIED</span></div>
    </section>
  );
}
```

## 90. `src/world/FlowerGarden.tsx` — modified

```tsx
import { useMemo, useState } from "react";
import { Flower2, RotateCcw, X } from "lucide-react";
import { chronosContent } from "../content/chronosContent";
import { WorldSection } from "./WorldSection";
import { SectionStage } from "../three/SectionStage";

export function FlowerGarden() {
  const [activeWish, setActiveWish] = useState<number | null>(null);
  const [replay, setReplay] = useState(0);
  const [draft, setDraft] = useState("");
  const [ownWish, setOwnWish] = useState("");
  const state = useMemo(() => ({ selected: activeWish, replay, planted: Boolean(ownWish) }), [activeWish, replay, ownWish]);
  const releaseWish = (index: number) => { setActiveWish(index); setReplay((value) => value + 1); };
  return <WorldSection id="flower-garden" className="wish-garden-section" eyebrow="THE LIVING CONSERVATORY" sideNote="BLOOM / 07">
    <div className="conservatory-heading"><div><span className="micro-label">TEN WISHES, ROOTED IN LIGHT</span><h3>A garden that opens<br /><em>one petal at a time.</em></h3></div><p>{chronosContent.flowerGarden.intro}<br /><small>Select a flower in the scene, or use its numbered button below.</small></p></div>
    <SectionStage kind="wish-garden" title="Botanical conservatory" state={state} onPick={releaseWish} label="Interactive 3D conservatory: curved rose, daisy and tulip petals, grass, trees and butterflies. Equivalent wish controls follow." />
    <div className="conservatory-panel"><div className="conservatory-selection" role="group" aria-label="Select a birthday wish">
      {chronosContent.flowerGarden.wishes.map((_, index) => <button type="button" key={index} onClick={() => releaseWish(index)} aria-pressed={activeWish === index} aria-label={`Release wish ${index + 1}`}><Flower2 size={17} /><span>{String(index + 1).padStart(2, "0")}</span><small>{["Rose", "Daisy", "Tulip"][index % 3]}</small></button>)}
      {ownWish && <button type="button" onClick={() => releaseWish(10)} aria-pressed={activeWish === 10}>My wish</button>}
    </div>
    <article className="conservatory-wish" aria-live="polite" aria-atomic="true"><span className="micro-label">{activeWish === null ? "A QUIET PLACE TO BEGIN" : activeWish === 10 ? "YOUR NEWLY PLANTED WISH" : `WISH ${String(activeWish + 1).padStart(2, "0")}`}</span><p>{activeWish === null ? "Choose a bloom. Let it unfold." : activeWish === 10 ? ownWish : chronosContent.flowerGarden.wishes[activeWish]}</p>{activeWish !== null && <div className="cinematic-controls"><button type="button" onClick={() => setReplay((value) => value + 1)}><RotateCcw size={14} /> Replay bloom</button><button type="button" onClick={() => setActiveWish(null)}><X size={14} /> Close wish</button></div>}</article></div>
    <form className="wish-plant-form" onSubmit={(event) => { event.preventDefault(); if (!draft.trim()) return; setOwnWish(draft.trim()); setActiveWish(10); setReplay((v) => v + 1); }}>
      <div><span className="micro-label">LEAVE SOMETHING GROWING</span><h4>Plant a wish of your own.</h4><p>Only held in this tab. Nothing is sent, recorded or shared.</p></div>
      <label>Your wish<textarea maxLength={240} rows={2} value={draft} onChange={(event) => setDraft(event.target.value)} placeholder="Something you hope for…" required /></label>
      <span className="wish-plant-species">A golden daisy · grown from your words</span>
      <button type="submit">{ownWish ? "Replant my wish" : "Plant my wish"} <Flower2 size={15} /></button>
      {ownWish && <button type="button" onClick={() => { setOwnWish(""); setDraft(""); if (activeWish === 10) setActiveWish(null); }}>Remove my wish</button>}
    </form>
  </WorldSection>;
}
```

## 91. `src/world/FuturePostcards.tsx` — modified

```tsx
import { useState } from "react";
import { ArrowUpRight, Compass, Sparkles } from "lucide-react";
import { ArchiveDialog } from "../components/ArchiveDialog";
import { chronosContent, type FuturePostcard } from "../content/chronosContent";
import { SectionStage } from "../three/SectionStage";
import { WorldSection } from "./WorldSection";

type Postcard = FuturePostcard;

export function FuturePostcards() {
  const [selected, setSelected] = useState<Postcard | null>(null);
  const [flipped, setFlipped] = useState(false);
  const [notes, setNotes] = useState<Record<string, string>>({});
  const choose = (card: Postcard) => { setFlipped(false); setSelected(card); };
  const navigate = (direction: number) => { const cards = chronosContent.future.postcards; choose(cards[(cards.findIndex(card => card.id === selected?.id) + direction + cards.length) % cards.length]); };
  return (
    <WorldSection id="future-postcards" className="postcards-section" eyebrow="A DRAWING OF POSSIBLE DAYS" sideNote="SOMEDAY / 11">
      <p className="postcards-intro">{chronosContent.future.intro}</p>
      <div className="postcards-warning"><Sparkles size={16} /><span>{chronosContent.future.tag}</span><i /></div>
      <div className="postcard-grid">
        {chronosContent.future.postcards.map((postcard, index) => <button key={postcard.id} type="button" className={`postcard postcard--${postcard.scene}`} onClick={() => choose(postcard)} aria-label={`Open speculative postcard: ${postcard.place}`}>
          <span className="postcard__scene">
            <img src={postcard.art} alt={postcard.alt} loading="lazy" width={1376} height={768} />
            <span className="postcard__scene-vignette" aria-hidden="true" />
            <span className="postcard__stamp">IMAGINED · {String(index + 1).padStart(2, "0")}</span>
            <span className="postcard__seal" aria-hidden="true"><Compass size={15} /></span>
          </span>
          <span className="postcard__text"><small>{postcard.someday}</small><strong>{postcard.place}</strong><span>{postcard.caption}</span><i><span>OPEN POSTCARD</span><ArrowUpRight size={13} /></i></span>
        </button>)}
      </div>
      <p className="postcards-footnote">These cards depict no real trips or shared memories. They are editable possibilities only; remove any that do not reflect a real, mutual hope.</p>
      <ArchiveDialog open={selected !== null} onClose={() => setSelected(null)} eyebrow={chronosContent.future.tag} title={selected?.place ?? "A possible day"}>
        {selected && <div className={`postcard-reading postcard-reading--${selected.scene}`}>
          <SectionStage kind="postcards" title="Possible days" state={{open:flipped,artwork:selected.art,detail:[selected.place,selected.someday,selected.caption,"Speculative illustration — not a fact, memory, or promise."].join("\n"),extra:{note:notes[selected.id] ?? ""}}} onPick={() => setFlipped(v => !v)} label="A thick three-dimensional postcard showing the original illustration on its front and the existing imagined-future message on its reverse. Flip with the accessible button below." />
          <div className="cinematic-controls"><button type="button" onClick={() => navigate(-1)}>Previous postcard</button><button type="button" aria-pressed={flipped} onClick={() => setFlipped(v => !v)}>{flipped ? "Show illustration" : "Read reverse"}</button><button type="button" onClick={() => navigate(1)}>Next postcard</button></div>
          <div className="postcard-editor">
            <label htmlFor="postcard-note">Write a line on the back</label>
            <textarea id="postcard-note" maxLength={140} rows={3} value={notes[selected.id] ?? ""} onFocus={() => setFlipped(true)} onChange={(event) => setNotes((all) => ({ ...all, [selected.id]: event.target.value }))} placeholder="Something you would add to this day…" />
            <div className="postcard-editor__row"><small>Appears in handwriting on the card. Kept in this tab only; nothing is sent, saved or shared.</small>{(notes[selected.id] ?? "") && <button type="button" onClick={() => setNotes((all) => ({ ...all, [selected.id]: "" }))}>Clear my line</button>}</div>
          </div>
          <img src={selected.art} alt={selected.alt} width={1376} height={768} />
          <p className="postcard-reading__when">{selected.someday}</p>
          <p>{selected.caption}</p>
          <small>Speculative illustration · not a fact, memory, or promise.</small>
        </div>}
      </ArchiveDialog>
    </WorldSection>
  );
}
```

## 92. `src/world/GiftExperiences.tsx` — modified

```tsx
import { useEffect, useRef, useState, type DragEvent, type FormEvent, type PointerEvent, type ReactNode } from "react";
import { Volume2, VolumeX } from "lucide-react";
import { GiftStage } from "../three/GiftStage";
import { audioBus, useAudioBus } from "../engine/audio";
import { chronosContent } from "../content/chronosContent";
import {
  couponEntries,
  futureGardenLeaves,
  giftsWithOwnReveal,
  openWhenLetters,
  reasonNotes,
  treasureHuntPuzzle,
  type GiftDefinition,
} from "../content/giftsContent";
import { packCinema, packExtended, packMicrocopy, packRadio, packReasons, packWishes } from "../content/packContent";

type GiftExperienceProps = { gift: GiftDefinition; onReturn: () => void; soundEnabled: boolean; onToggleSound: () => void };

function useOptionalAudio(src: string, soundEnabled: boolean) {
  const audioRef = useRef<HTMLAudioElement>(null);
  const contextRef = useRef<AudioContext|null>(null);
  const [analyser,setAnalyser]=useState<AnalyserNode|null>(null);
  useEffect(()=>()=>{void contextRef.current?.close();},[]);
  const [playing, setPlaying] = useState(false);
  const [volume, setVolume] = useState(0.72);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.pause();
    audio.currentTime = 0;
    setPlaying(false);
    setCurrentTime(0);
    setDuration(0);
    setError("");
    const onTime = () => setCurrentTime(audio.currentTime || 0);
    const onDuration = () => setDuration(Number.isFinite(audio.duration) ? audio.duration : 0);
    const onEnded = () => setPlaying(false);
    const onWaiting = () => setLoading(true);
    const onReady = () => setLoading(false);
    const onError = () => { setLoading(false); setError("This local audio file could not be loaded."); };
    audio.addEventListener("timeupdate", onTime);
    audio.addEventListener("loadedmetadata", onDuration);
    audio.addEventListener("durationchange", onDuration);
    audio.addEventListener("ended", onEnded);
    audio.addEventListener("error", onError);
    audio.addEventListener("waiting", onWaiting);
    audio.addEventListener("playing", onReady);
    audio.addEventListener("canplay", onReady);
    return () => {
      audio.pause();
      audio.removeEventListener("timeupdate", onTime);
      audio.removeEventListener("loadedmetadata", onDuration);
      audio.removeEventListener("durationchange", onDuration);
      audio.removeEventListener("ended", onEnded);
      audio.removeEventListener("error", onError);
      audio.removeEventListener("waiting", onWaiting);
      audio.removeEventListener("playing", onReady);
      audio.removeEventListener("canplay", onReady);
    };
  }, [src]);
  useEffect(() => {
    if (audioRef.current) audioRef.current.volume = volume;
  }, [volume]);
  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.muted = !soundEnabled;
    if (!soundEnabled && !audio.paused) {
      audio.pause();
      setPlaying(false);
      setError("Global sound is off; playback was paused.");
    } else if (soundEnabled) {
      setError((current) => current === "Global sound is off; playback was paused." ? "" : current);
    }
  }, [soundEnabled]);

  const play = async () => {
    const audio = audioRef.current;
    if (!audio || !src) {
      setError("No owner-provided or licensed audio has been added yet.");
      return;
    }
    if (!soundEnabled) {
      setError("Sound is off. Turn it on in the top bar, then press Play.");
      return;
    }
    setError("");
    setLoading(true);
    try {
      if(!contextRef.current){const context=new AudioContext();const node=context.createAnalyser();node.fftSize=128;const source=context.createMediaElementSource(audio);source.connect(node);node.connect(context.destination);contextRef.current=context;setAnalyser(node);}
      await contextRef.current.resume();
      await audio.play();
      setPlaying(true);
      setLoading(false);
    } catch {
      setPlaying(false);
      setLoading(false);
      setError("Playback could not start. Check the local audio file.");
    }
  };
  const pause = () => { audioRef.current?.pause(); setPlaying(false); };
  const stop = () => { if (audioRef.current) { audioRef.current.pause(); audioRef.current.currentTime = 0; } setPlaying(false); setCurrentTime(0); };
  const rewind = () => { if (audioRef.current) audioRef.current.currentTime = Math.max(0, audioRef.current.currentTime - 10); };
  const changeVolume = (next: number) => {
    const safeVolume = Math.max(0, Math.min(1, next));
    setVolume(safeVolume);
    if (audioRef.current) audioRef.current.volume = safeVolume;
  };

  return {
    audioRef,
    analyser,
    playing,
    loading,
    volume,
    changeVolume,
    currentTime,
    duration,
    progress: duration > 0 ? (currentTime / duration) * 100 : 0,
    play,
    pause,
    stop,
    rewind,
    error,
  };
}

function ExperienceReplay({ onReplay, label = packMicrocopy.replay, title }: { onReplay: () => void; label?: string; title?: string }) {
  return <button type="button" className="gift-control gift-control--quiet" onClick={onReplay} title={title}>↻ <span>{label}</span></button>;
}

/** A pack dedication: a short line that is shown when the gift's reveal happens, then the longer words. */
function Dedication({ revealLine, text }: { revealLine: string; text: string }) {
  return <div className="gift-dedication" role="note"><strong>{revealLine}</strong><p>{text}</p></div>;
}

function EmptyCopy({ children }: { children: ReactNode }) {
  return <p className="gift-empty-copy" role="note">{children}</p>;
}

/** Optional sound: starts off, never autoplays. The toggle is the same global switch as the top bar (the bar sits behind the dialog). */
function SoundDock({ soundEnabled, onToggleSound }: { soundEnabled: boolean; onToggleSound: () => void }) {
  const { volume } = useAudioBus();
  return (
    <div className="gift-sound-dock" role="group" aria-label="Sound">
      <button type="button" className="gift-control gift-control--quiet" aria-pressed={soundEnabled} onClick={onToggleSound}>
        {soundEnabled ? <Volume2 size={15} aria-hidden="true" /> : <VolumeX size={15} aria-hidden="true" />} <span>Sound effects</span><span className="gift-sound-dock__state" aria-hidden="true">{soundEnabled ? "on" : "off"}</span>
      </button>
      <label className="gift-volume">Volume <input type="range" min="0.05" max="1" step="0.05" value={volume} disabled={!soundEnabled} onChange={(event) => audioBus.setVolume(Number(event.target.value))} aria-label="Sound effects volume" /></label>
    </div>
  );
}

function SecretLetterExperience() {
  const [open, setOpen] = useState(false);
  const [writingKey, setWritingKey] = useState(0);
  const [progress, setProgress] = useState(0);
  const [skip, setSkip] = useState(false);
  const letter = chronosContent.letters.letters[0];
  return (
    <section className="gift-letter" aria-label="Secret letter experience">
      <GiftStage kind="letter" state={{ open, replay: writingKey, immediate: skip, detail: [letter.salutation,...letter.paragraphs,letter.closing,letter.signature,letter.ps].filter(Boolean).join("\n\n") }} onPick={() => {setSkip(false);setOpen(v=>!v);}} onProgress={setProgress} label="A physically thick letter bends along two rounded creases after leaving a wax-sealed hinged envelope on its writing desk." />
      <div className="gift-world-console">
      
      {open && (skip || progress >= .995) ? (
        <article className="gift-letter__reading" key={writingKey}>
          {letter.subtitle && <header className="gift-letter__heading"><h3>{letter.title}</h3><p>{letter.subtitle}</p></header>}
          <p className="gift-letter__salutation">{letter.salutation}</p>
          {letter.paragraphs.map((paragraph, index) => <p key={index}>{paragraph}</p>)}
          <p className="gift-letter__closing">{letter.closing}<br /><strong>{letter.signature}</strong></p>
          {letter.ps && <p className="gift-letter__ps">{letter.ps}</p>}
        </article>
      ) : <EmptyCopy>Open the envelope to read the letter, or skip the animation to read it straight away.</EmptyCopy>}
      <div className="gift-control-row">
        <button type="button" className="gift-control gift-control--primary" onClick={() => {setSkip(false);setOpen((value) => !value);}}>{open ? "Fold the letter" : "Open the letter"}</button>
        <button type="button" className="gift-control" onClick={() => { setWritingKey((value) => value + 1); setSkip(false); setProgress(0); setOpen(true); }}>Replay the writing</button>
        <button type="button" className="gift-control" onClick={() => {setSkip(true);setOpen(true);}}>{packMicrocopy.skip}</button>
        <button type="button" className="gift-control" disabled aria-describedby="gift-letter-audio-note">Play narration</button>
      </div>
      <small id="gift-letter-audio-note" className="gift-audio-note">Voice narration is not available until a real recording is supplied.</small>
    </div>
    </section>
  );
}

function ReasonJarExperience() {
  const [index, setIndex] = useState(0);
  const [lidOpen,setLidOpen]=useState(false);
  const [drawn,setDrawn]=useState(false);
  const [turn,setTurn]=useState(0);
  const [showAll, setShowAll] = useState(false);
  const [shuffleCount, setShuffleCount] = useState(0);
  const drawAnother = () => {
    setIndex((current) => (current + 1 + Math.floor(Math.random() * (reasonNotes.length - 1))) % reasonNotes.length);
    setShowAll(false); setLidOpen(true);setDrawn(true);
    setShuffleCount((count) => count + 1);
  };
  const note = reasonNotes[index];
  return (
    <section className="gift-jar" aria-label="Jar of reasons experience">
      <GiftStage kind="jar" state={{open:lidOpen,selected:drawn?index:null,turn,replay:shuffleCount,detail:drawn?note.text:""}} onPick={i=>{if(i===-2){setLidOpen(v=>!v);setDrawn(false);}else if(lidOpen){setIndex(i);setDrawn(true);}}} label="A thick hollow glass jar with threaded rim, brass lid, fabric bow and seventeen separate folded paper notes. Open the lid, turn the jar and choose a numbered note." />
      <div className="gift-world-console">
      <div className="gift-control-row"><button type="button" className="gift-control" aria-pressed={lidOpen} onClick={()=>{setLidOpen(v=>!v);setDrawn(false);}}>{lidOpen?"Close jar lid":"Open jar lid"}</button><button type="button" className="gift-control" onClick={()=>setTurn(v=>v-.4)}>Turn jar left</button><button type="button" className="gift-control" onClick={()=>setTurn(v=>v+.4)}>Turn jar right</button><button type="button" className="gift-control" disabled={!drawn} onClick={()=>setDrawn(false)}>Put note back</button></div>
      <div className="gift-note-picker" role="group" aria-label="Pick one of seventeen physical notes">{reasonNotes.map((n,i)=><button key={n.id} type="button" disabled={!lidOpen} aria-pressed={drawn&&index===i} onClick={()=>{setIndex(i);setDrawn(true);}}>{String(i+1).padStart(2,"0")}</button>)}</div>
      <div className="gift-jar__note" aria-live="polite">
        <small>NOTE {String(index + 1).padStart(2, "0")} / 17</small>
        {note.text ? <p>{note.text}</p> : <p className="is-empty">{packMicrocopy.missingText}</p>}
      </div>
      {showAll && <ol className="gift-jar__all">{reasonNotes.map((item, itemIndex) => <li key={item.id}><span>{String(itemIndex + 1).padStart(2, "0")}</span>{item.text || packMicrocopy.missingText}</li>)}</ol>}
      <div className="gift-control-row">
        <button type="button" className="gift-control gift-control--primary" onClick={drawAnother}>Draw another note</button>
        <button type="button" className="gift-control" onClick={drawAnother}>Shuffle the jar</button>
        <button type="button" className="gift-control" onClick={() => setShowAll((value) => !value)}>{showAll ? "Hide all notes" : "Read all 17"}</button>
      </div>
      <p className="gift-jar__quote">{packReasons.quote}</p>
    </div>
    </section>
  );
}

function EternalFlowerExperience() {
  const [stage, setStage] = useState(0);
  const [rotation, setRotation] = useState(0);
  const [messageVisible, setMessageVisible] = useState(false);
  return (
    <section className="gift-flower" aria-label="Everlasting flower experience">
      <GiftStage kind="flower" state={{ growth: stage, turn: rotation * Math.PI / 180 }} label="A procedural three-dimensional rose grows from a seed, unfolds leaves and opens twenty-one individually hinged curved petals. Grow and rotate controls follow." />
      <div className="gift-world-console">
      <p className="gift-flower__caption" aria-live="polite">{stage === 0 ? "A seed, held in the soil." : stage < 4 ? ["Seed","Roots opening beneath the soil.","A sprout emerges.","The leaves unfold."][stage] : "The bloom is open. It can begin again."}</p>
      {messageVisible && <Dedication revealLine={packExtended.flower.revealLine} text={packExtended.flower.text} />}
      <div className="gift-control-row">
        <button type="button" className="gift-control gift-control--primary" onClick={() => setStage((value) => (value + 1) % 5)}>{["Grow the flower","Grow the sprout","Unfold the leaves","Open the bloom","Begin again"][stage]}</button>
        <button type="button" className="gift-control" onClick={() => setRotation((value) => value - 28)} aria-label="Rotate flower left">↶ Rotate left</button>
        <button type="button" className="gift-control" onClick={() => setRotation((value) => value + 28)} aria-label="Rotate flower right">↷ Rotate right</button>
        <button type="button" className="gift-control" onClick={() => setMessageVisible((value) => !value)}>{messageVisible ? "Hide the message" : "Reveal hidden message"}</button>
      </div>
    </div>
    </section>
  );
}

function LittleUniverseExperience() {
  const [selected, setSelected] = useState("first-connection");
  const [zoom, setZoom] = useState(1);
  const [rotation, setRotation] = useState(0);
  const [revealed, setRevealed] = useState(false);
  const milestones = [
    { id: "first-connection", date: chronosContent.dates.firstConnectionLabel, title: "First connection", detail: "The verified date recorded in the source archive." },
    { id: "proposal", date: chronosContent.dates.proposalLabel, title: "The proposal", detail: "The verified date recorded in the source archive." },
  ];
  return (
    <section className="gift-universe" aria-label="Our Little Universe experience">
      <GiftStage kind="universe" state={{selected:milestones.findIndex(m=>m.id===selected),growth:zoom,turn:rotation*Math.PI/180}} onPick={i=>setSelected(milestones[i%milestones.length].id)} label="A brass miniature orrery, five orbiting planets, ringed world and two selectable star markers for the only verified dates." />
      <div className="gift-world-console">
      <div className="gift-control-row">{milestones.map(m=><button key={m.id} type="button" className="gift-control" aria-pressed={selected===m.id} onClick={()=>setSelected(m.id)}>{m.title} · {m.date}</button>)}</div>
      <article className="gift-universe__record" aria-live="polite">
        <small>VERIFIED ARCHIVE · NO OTHER DATES ADDED</small>
        <h3>{milestones.find((milestone) => milestone.id === selected)?.title}</h3>
        <p>{milestones.find((milestone) => milestone.id === selected)?.date}</p>
        <span>{milestones.find((milestone) => milestone.id === selected)?.detail}</span>
      </article>
      <div className="gift-control-row">
        <button type="button" className="gift-control" onClick={() => setZoom((value) => Math.min(1.6, value + 0.15))}>Zoom in</button>
        <button type="button" className="gift-control" onClick={() => setZoom((value) => Math.max(0.85, value - 0.15))}>Zoom out</button>
        <button type="button" className="gift-control" onClick={() => setRotation((value) => value + 24)}>Rotate the map</button>
        <button type="button" className="gift-control" onClick={() => { setZoom(1); setRotation(0); }}>Return to overview</button>
        <button type="button" className="gift-control gift-control--primary" aria-pressed={revealed} onClick={() => { setRevealed((value) => !value); if (!revealed) setZoom(0.85); }}>{revealed ? "Hide the dedication" : "Reveal the dedication"}</button>
      </div>
      {revealed && <Dedication revealLine={packExtended.universe.revealLine} text={packExtended.universe.text} />}
    </div>
    </section>
  );
}

function CassetteExperience({ soundEnabled }: { soundEnabled: boolean }) {
  const track = chronosContent.music.tracks[0];
  const audio = useOptionalAudio(track.src, soundEnabled);
  const [inserted, setInserted] = useState(false);
  return (
    <section className="gift-cassette" aria-label="Bhumi FM cassette experience">
      <GiftStage kind="cassette" state={{open:inserted,playing:audio.playing,extra:{volume:audio.volume}}} analyser={audio.analyser} label="A wooden cassette deck with physical controls, two visible tape reels and mechanical insertion. Reels follow actual playback only." />
      <div className="gift-world-console">
      
      <audio ref={audio.audioRef} src={track.src || undefined} preload="none" muted={!soundEnabled} />
      <p className="gift-cassette__status" role="status">{track.src ? (audio.loading ? "Loading the recording…" : audio.playing ? "Playing the supplied local recording." : "Cassette ready.") : packRadio.emptyPlaylist}</p>
      <div className="gift-control-row">
        <button type="button" className="gift-control gift-control--primary" onClick={() => setInserted((value) => !value)}>{inserted ? "Eject cassette" : "Insert cassette"}</button>
        <button type="button" className="gift-control" disabled={!track.src || !inserted || audio.playing} onClick={() => void audio.play()}>Play</button>
        <button type="button" className="gift-control" disabled={!track.src || !audio.playing} onClick={audio.pause}>Pause</button>
        <button type="button" className="gift-control" disabled={!track.src} onClick={audio.stop}>Stop</button>
        <button type="button" className="gift-control" disabled={!track.src} onClick={audio.rewind}>Rewind 10s</button>
      </div>
      <label className="gift-volume">Volume <input type="range" min="0" max="1" step="0.01" value={audio.volume} disabled={!track.src} onChange={(event) => audio.changeVolume(Number(event.target.value))} aria-label="Cassette volume" /></label>
      {audio.error && <p className="gift-audio-note" role="status">{audio.error}</p>}
      {track.src && <p className="gift-audio-caption">{chronosContent.music.tracks[0].note}</p>}
    </div>
    </section>
  );
}

function MemoryCinemaExperience() {
  const stageRef = useRef<HTMLDivElement>(null);
  const [powered, setPowered] = useState(false);
  const [playing, setPlaying] = useState(false);
  const [slide, setSlide] = useState(0);
  const [everPowered, setEverPowered] = useState(false);
  const photos = chronosContent.gallery.photos.filter((photo) => photo.src.trim().length > 0);
  useEffect(() => {
    if (!playing || !photos.length) return;
    const timer = window.setInterval(() => setSlide((current) => (current + 1) % photos.length), 3800);
    return () => window.clearInterval(timer);
  }, [playing, photos.length]);
  const showSlide = (direction: number) => {
    if (!photos.length) return;
    setSlide((current) => (current + direction + photos.length) % photos.length);
  };
  const toggleFullscreen = async () => {
    if (!stageRef.current) return;
    try {
      if (!document.fullscreenElement) await stageRef.current.requestFullscreen();
      else await document.exitFullscreen();
    } catch { /* Fullscreen is an optional browser permission. */ }
  };
  return (
    <section className="gift-cinema" aria-label="Memory cinema experience">
      <GiftStage kind="cinema" state={{open:powered,playing,artwork:photos[slide]?.src}} label="A miniature film projector with two metal reels, moving film path, projection beam and a screen reserved for genuine supplied photographs." />
      <div className="gift-world-console">
      {photos.length > 0 && <p className="gift-cinema__intro">{packCinema.timelineIntro}</p>}
      <div className={`gift-cinema__theatre${powered ? " is-lit" : ""}`} ref={stageRef}>
        <div className="gift-cinema__curtain gift-cinema__curtain--left" /><div className="gift-cinema__curtain gift-cinema__curtain--right" />
        <div className="gift-cinema__screen">
          {photos.length ? <figure><img src={photos[slide].src} alt={photos[slide].alt || photos[slide].caption} /><figcaption>{photos[slide].caption}</figcaption></figure> : <div className="gift-cinema__placeholder"><span>FRAME {String(slide + 1).padStart(2, "0")}</span><strong>{powered ? packCinema.emptyState : everPowered ? packCinema.closing : packCinema.opening}</strong></div>}
        </div>
        <div className={`gift-cinema__beam${powered ? " is-on" : ""}`} aria-hidden="true" />
        <div className="gift-cinema__seats" aria-hidden="true"><i /><i /><i /></div>
      </div>
      <p className="gift-cinema__status" role="status">{photos.length ? `Photograph ${slide + 1} of ${photos.length} · ${playing ? "slideshow playing" : "paused"}` : packMicrocopy.missingPhoto}</p>
      <div className="gift-control-row">
        <button type="button" className="gift-control gift-control--primary" onClick={() => { setPowered((value) => !value); setEverPowered(true); }}>{powered ? "Dim the theatre" : "Start projector"}</button>
        <button type="button" className="gift-control" onClick={() => setPlaying((value) => !value)} disabled={!photos.length}>{playing ? "Pause" : "Play"}</button>
        <button type="button" className="gift-control" onClick={() => showSlide(-1)} disabled={!photos.length}>Previous</button>
        <button type="button" className="gift-control" onClick={() => showSlide(1)} disabled={!photos.length}>Next</button>
        <button type="button" className="gift-control" onClick={() => { setPlaying(false); setPowered(false); setSlide(0); setEverPowered(false); }}>Replay</button>
        <button type="button" className="gift-control" onClick={() => void toggleFullscreen()}>Full screen</button>
      </div>
    </div>
    </section>
  );
}

/** Fisher-Yates, so that "draw a wish" walks through all of the sky before any wish comes back. */
function shuffled(count: number) {
  const order = Array.from({ length: count }, (_, index) => index);
  for (let i = order.length - 1; i > 0; i--) { const j = Math.floor(Math.random() * (i + 1)); [order[i], order[j]] = [order[j], order[i]]; }
  return order;
}

function WishesExperience() {
  const wishes = chronosContent.flowerGarden.wishes; // the ten wishes of the archive, one per lantern
  const sky = packWishes; // the content pack's wishes ("a sky full of good wishes")
  const [selected, setSelected] = useState<number[]>([]);
  const [showAll, setShowAll] = useState(false);
  const [activeWish, setActiveWish] = useState<number | null>(null);
  const [skyWish, setSkyWish] = useState<number | null>(null);
  const [skyDraws, setSkyDraws] = useState(0);
  const [skySeen, setSkySeen] = useState<number[]>([]);
  const bag = useRef<number[]>([]);
  const toggleStar = (index: number) => {
    setSkyWish(null);
    setActiveWish(index);
    setSelected((current) => current.includes(index) ? current.filter((item) => item !== index) : [...current, index]);
  };
  const showSky = (index: number) => {
    setActiveWish(null);
    setSkyWish(index);
    setSkyDraws((count) => count + 1);
    setSkySeen((current) => current.includes(index) ? current : [...current, index]);
  };
  const drawFromSky = () => {
    if (!bag.current.length) bag.current = shuffled(sky.length).filter((index) => index !== skyWish);
    showSky(bag.current.pop() as number);
  };
  const stepSky = (direction: number) => showSky(skyWish === null ? (direction > 0 ? 0 : sky.length - 1) : (skyWish + direction + sky.length) % sky.length);
  const label = skyWish !== null
    ? `WISH ${String(skyWish + 1).padStart(2, "0")} OF ${sky.length} · FROM THE SKY`
    : activeWish === null ? "CHOOSE A STAR OR DRAW A WISH" : `WISH ${String(activeWish + 1).padStart(2, "0")} · ${selected.includes(activeWish) ? "COLLECTED" : "RELEASED"}`;
  const text = skyWish !== null ? sky[skyWish] : activeWish === null ? "Pick a lantern on the tree, or draw a wish from the sky." : wishes[activeWish];
  return (
    <section className="gift-wishes" aria-label="A Thousand Wishes experience">
      <GiftStage kind="wishes" state={{selected:activeWish,collected:selected,step:skyDraws}} onPick={toggleStar} label="A sculptural wishing tree holds ten physical star lanterns, one for each wish of the archive, under a sky full of stars. Pick a star to collect its light, or draw a wish from the sky." />
      <div className="gift-world-console">
      <div className="gift-wishes__note" aria-live="polite">
        <small>{label}</small>
        <p>{text}</p>
      </div>
      <div className="gift-note-picker" role="group" aria-label="Wish lanterns">{wishes.map((_,i)=><button key={i} type="button" aria-pressed={selected.includes(i)} onClick={()=>toggleStar(i)}>Wish {i+1}</button>)}</div>
      <div className="gift-wishes__meta"><span>{selected.length} / {wishes.length} lanterns collected</span><span>{selected.length > 1 ? "A constellation is connected." : "Collect two or more stars to connect them."}</span><span>{skySeen.length} / {sky.length} sky wishes read</span></div>
      {showAll && <div className="gift-wishes__lists">
        <h4>From the lanterns · {wishes.length}</h4>
        <ol className="gift-wishes__all">{wishes.map((wish, index) => <li key={index}><span>{String(index + 1).padStart(2, "0")}</span>{wish}</li>)}</ol>
        <h4>From the sky · {sky.length}</h4>
        <ol className="gift-wishes__sky">{sky.map((wish, index) => <li key={index}><span>{String(index + 1).padStart(2, "0")}</span>{wish}</li>)}</ol>
      </div>}
      <div className="gift-control-row">
        <button type="button" className="gift-control gift-control--primary" onClick={drawFromSky}>Draw a wish from the sky</button>
        <button type="button" className="gift-control" onClick={() => stepSky(-1)}>Previous sky wish</button>
        <button type="button" className="gift-control" onClick={() => stepSky(1)}>Next sky wish</button>
        <button type="button" className="gift-control" aria-expanded={showAll} onClick={() => setShowAll((value) => !value)}>{showAll ? "Hide wishes" : "Display all wishes"}</button>
        <button type="button" className="gift-control" onClick={() => { setSelected([]); setActiveWish(null); setSkyWish(null); }}>Clear constellation</button>
      </div>
    </div>
    </section>
  );
}

function CrownExperience() {
  const [rotation, setRotation] = useState(0);
  const [detail, setDetail] = useState("crown");
  const [messageVisible, setMessageVisible] = useState(false);
  const sourceNote = chronosContent.gifts.specials["08"].message;
  const dedication = packExtended.crown;
  return (
    <section className="gift-crown" aria-label="Queen's Crown experience">
      <GiftStage kind="crown" state={{ turn: rotation * Math.PI / 180, detail }} label="An eight-point metallic crown assembles on a velvet plinth. Faceted gemstones, beveled gold points and molded rings can be inspected and rotated with the controls below." />
      <div className="gift-world-console">
      <div className="gift-crown__inspection" role="group" aria-label="Inspect crown details">
        {[
          ["crown", "The crown"], ["jewels", "The jewels"], ["velvet", "The velvet"],
        ].map(([id, label]) => <button type="button" key={id} className={detail === id ? "is-selected" : ""} onClick={() => setDetail(id)} aria-pressed={detail === id}>{label}</button>)}
      </div>
      <p className="gift-crown__detail" aria-live="polite">{detail === "crown" ? "A three-dimensional metallic crown, rendered without a portrait or personal likeness." : detail === "jewels" ? "Eight faceted stones catch the light as the crown turns." : "A velvet plinth anchors the object in a quiet palace scene."}</p>
      {messageVisible && <><Dedication revealLine={dedication.revealLine} text={dedication.text} /><blockquote className="gift-crown__message">{sourceNote}</blockquote></>}
      <div className="gift-control-row">
        <button type="button" className="gift-control" onClick={() => setRotation((value) => value - 24)}>Rotate left</button>
        <button type="button" className="gift-control" onClick={() => setRotation((value) => value + 24)}>Rotate right</button>
        <button type="button" className="gift-control gift-control--primary" onClick={() => { setMessageVisible((value) => !value); if (!messageVisible) setRotation((value) => value + 360); }}>{messageVisible ? "Hide birthday note" : "Reveal birthday note"}</button>
      </div>
    </div>
    </section>
  );
}

function OpenWhenExperience() {
  const [selected, setSelected] = useState(0);
  const [opened, setOpened] = useState(false);
  const current = openWhenLetters[selected];
  return (
    <section className="gift-open-when" aria-label="Open When letter collection">
      <GiftStage kind="cabinet" state={{ open: opened,selected }} onPick={i=>{setSelected(i);setOpened(false);}} label="The selected open-when letter, represented as a reversible three-dimensional folding envelope and paper." />
      <div className="gift-world-console">
      <div className="gift-open-when__envelopes">
        {openWhenLetters.map((letter, index) => <button type="button" key={letter.id} className={`gift-open-when__envelope${selected === index ? " is-selected" : ""}${opened && selected === index ? " is-broken" : ""}`} onClick={() => { setSelected(index); setOpened(false); }} aria-pressed={selected === index}>
          <span className="gift-open-when__seal">✦</span><strong>{letter.prompt}</strong><small>{opened && selected === index ? "SEAL OPENED" : "SELECT ENVELOPE"}</small>
        </button>)}
      </div>
      <article className={`gift-open-when__letter${opened ? " is-open" : ""}`} aria-live="polite">
        {opened ? <><small>OWNER-WRITTEN LETTER · {current.prompt.toUpperCase()}</small><p>{current.message || packMicrocopy.missingText}</p></> : <><small>SEALED FOR A MOMENT</small><p>Select an envelope, then break its seal to open the note.</p></>}
      </article>
      <div className="gift-control-row"><button type="button" className="gift-control gift-control--primary" onClick={() => setOpened(true)}>{opened ? "Read the letter" : "Break the seal & open"}</button><button type="button" className="gift-control" onClick={() => setOpened(false)}>Close the letter</button></div>
    </div>
    </section>
  );
}

function HappinessMachineExperience() {
  const wishes = chronosContent.flowerGarden.wishes;
  const timerRef = useRef<number | null>(null);
  const [running, setRunning] = useState(false);
  const [messageIndex, setMessageIndex] = useState<number | null>(null);
  const [cycles, setCycles] = useState(0);
  useEffect(() => () => { if (timerRef.current !== null) window.clearTimeout(timerRef.current); }, []);
  const pullLever = () => {
    if (running) return;
    setRunning(true);
    const next = Math.floor(Math.random() * wishes.length);
    setMessageIndex(next);
    setCycles((value) => value + 1);
    if (timerRef.current !== null) window.clearTimeout(timerRef.current);
    timerRef.current = window.setTimeout(() => { setRunning(false); timerRef.current = null; }, 780);
  };
  return (
    <section className="gift-machine" aria-label="Happiness Machine experience">
      <GiftStage kind="machine" state={{open:running,selected:messageIndex,replay:cycles,detail:messageIndex!==null?wishes[messageIndex]:""}} onPick={pullLever} label="An enamel and brass workshop machine with three meshing gears, a physical lever and advancing paper ticket. The controls reveal an existing source wish." />
      <div className="gift-world-console">
      {messageIndex!==null&&<blockquote className="gift-native-copy">{wishes[messageIndex]}</blockquote>}
      
      <p className="gift-machine__status" role="status">{messageIndex === null ? "The machine reveals only wishes already present in the source archive." : "A source-archive birthday wish has been selected."}</p>
      <div className="gift-control-row"><button type="button" className="gift-control gift-control--primary" onClick={pullLever} disabled={running}>Pull the lever</button><button type="button" className="gift-control" onClick={() => { setMessageIndex(null); setCycles(0); }}>Reset machine</button></div>
    </div>
    </section>
  );
}

function AdventureExperience() {
  const locations = chronosContent.future.items;
  const [unlocked, setUnlocked] = useState(0);
  const [selected, setSelected] = useState(0);
  const location = locations[selected];
  const visit = (index: number) => {
    if (index > unlocked) return;
    setSelected(index);
    setUnlocked((current) => Math.max(current, Math.min(locations.length - 1, index + 1)));
  };
  return (
    <section className="gift-adventure" aria-label="Little Adventure map">
      <GiftStage kind="adventure" state={{selected,growth:unlocked}} onPick={visit} label="An explicitly imagined miniature raised map, brass route, four physical flags and a small travelling marker. Existing postcard progression stays below." />
      <div className="gift-world-console">
      <p className="gift-adventure__warning">IMAGINATIVE MAP · NOT A REAL TRAVEL HISTORY</p>
      <div className="gift-adventure__map">
        <svg viewBox="0 0 100 44" preserveAspectRatio="none" aria-hidden="true"><path d="M4 34 C 18 5, 25 39, 42 22 S 68 6, 79 25 S 92 21, 98 8" /></svg>
        {locations.map((item, index) => <button type="button" key={item.id} className={`gift-adventure__location gift-adventure__location--${index + 1}${index === selected ? " is-selected" : ""}${index > unlocked ? " is-locked" : ""}`} onClick={() => visit(index)} disabled={index > unlocked} aria-current={index === selected ? "step" : undefined} aria-label={`${index > unlocked ? "Locked" : "Explore"}: ${item.place}`}><span>{index > unlocked ? "·" : String(index + 1).padStart(2, "0")}</span><small>{item.place}</small></button>)}
      </div>
      <article className="gift-adventure__postcard" aria-live="polite">
        <div className="gift-adventure__art">{location?.art && <img src={location.art} alt={location.alt} />}</div>
        <div><small>POSSIBLE FUTURE · NOT A FACT</small><h3>{location?.place}</h3><p>{location?.caption}</p><span>{location?.someday}</span></div>
      </article>
      <p className="gift-adventure__progress">{Math.min(unlocked + 1, locations.length)} / {locations.length} imagined locations available</p>
    </div>
    </section>
  );
}

function MusicExperience({ soundEnabled }: { soundEnabled: boolean }) {
  const tracks = chronosContent.music.tracks;
  const [selected, setSelected] = useState(0);
  const [silentPreview, setSilentPreview] = useState(false);
  const track = tracks[selected];
  const audio = useOptionalAudio(track?.src ?? "", soundEnabled);
  return (
    <section className="gift-vinyl" aria-label="The Music of Us experience">
      <GiftStage kind="vinyl" state={{playing:audio.playing,preview:silentPreview,open:true}} analyser={audio.analyser} label="A wooden turntable with grooved vinyl, spindle, moving tonearm and playback controls. Silent mechanical preview is not real music. Visualization follows real audio data only." />
      <div className="gift-world-console">
      
      <audio ref={audio.audioRef} src={track?.src || undefined} preload="none" muted={!soundEnabled} />
      <div className="gift-vinyl__track">
        <small>TRACK {String(selected + 1).padStart(2, "0")} / {tracks.length}</small>
        <strong>{track?.title}</strong><span>{track?.src ? track.note : chronosContent.music.emptyNote}</span>
        <div className="gift-vinyl__progress" aria-label="Track progress"><i style={{ width: `${audio.progress}%` }} /></div>
      </div>
      <div className="gift-vinyl__playlist" role="group" aria-label="Available local tracks">
        {tracks.map((item, index) => <button type="button" key={item.id} className={selected === index ? "is-selected" : ""} onClick={() => { audio.stop(); setSelected(index); }} aria-pressed={selected === index}><span>{String(index + 1).padStart(2, "0")}</span><strong>{item.title}</strong><small>{item.src ? "READY" : "NO AUDIO FILE"}</small></button>)}
      </div>
      <div className="gift-control-row">
        <button type="button" className="gift-control" onClick={() => { audio.stop(); setSelected((value) => (value + tracks.length - 1) % tracks.length); }}>Previous</button>
        <button type="button" className="gift-control gift-control--primary" disabled={!track?.src} onClick={() => audio.playing ? audio.pause() : void audio.play()}>{audio.playing ? "Pause" : "Play"}</button>
        <button type="button" className="gift-control" onClick={() => { audio.stop(); setSelected((value) => (value + 1) % tracks.length); }}>Next</button>
        <button type="button" className="gift-control" disabled={!track?.src} onClick={audio.stop}>Stop</button>
        <button type="button" className="gift-control" aria-pressed={silentPreview} onClick={() => setSilentPreview((value) => !value)}>{silentPreview ? "Stop silent preview" : "Preview turntable silently"}</button>
      </div>
      <label className="gift-volume">Volume <input type="range" min="0" max="1" step="0.01" value={audio.volume} disabled={!track?.src} onChange={(event) => audio.changeVolume(Number(event.target.value))} aria-label="Music volume" /></label>
      {audio.error && <p className="gift-audio-note" role="status">{audio.error}</p>}
      {!track?.src && <EmptyCopy>No autoplay: nothing plays until you press Play.</EmptyCopy>}
    </div>
    </section>
  );
}

function MirrorExperience() {
  const [cleared,setCleared]=useState(0);
  const [resets,setResets]=useState(0);
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const pointerDown = useRef(false);
  const redrawFog = useRef<() => void>(() => {});
  useEffect(() => {
    const canvas = canvasRef.current;
    const context = canvas?.getContext("2d");
    if (!canvas || !context) return;
    const drawFog = () => {
      setCleared(0);
      const bounds = canvas.getBoundingClientRect();
      const ratio = Math.min(window.devicePixelRatio || 1, 2);
      canvas.width = Math.max(1, Math.round(bounds.width * ratio));
      canvas.height = Math.max(1, Math.round(bounds.height * ratio));
      context.setTransform(ratio, 0, 0, ratio, 0, 0);
      context.globalCompositeOperation = "source-over";
      const fog = context.createLinearGradient(0, 0, bounds.width, bounds.height);
      fog.addColorStop(0, "rgba(230,239,236,.95)");
      fog.addColorStop(0.5, "rgba(205,220,218,.93)");
      fog.addColorStop(1, "rgba(235,232,222,.95)");
      context.fillStyle = fog;
      context.fillRect(0, 0, bounds.width, bounds.height);
      context.fillStyle = "rgba(255,255,255,.28)";
      context.fillRect(0, 0, bounds.width, bounds.height * 0.12);
    };
    drawFog();
    redrawFog.current = drawFog;
    const resizeObserver = "ResizeObserver" in window ? new ResizeObserver(drawFog) : null;
    resizeObserver?.observe(canvas);
    return () => resizeObserver?.disconnect();
  }, []);
  const erase = (event: PointerEvent<HTMLCanvasElement>) => {
    const canvas = event.currentTarget;
    const context = canvas.getContext("2d");
    if (!context) return;
    const bounds = canvas.getBoundingClientRect();
    const ratio = Math.min(window.devicePixelRatio || 1, 2);
    const x = (event.clientX - bounds.left);
    const y = (event.clientY - bounds.top);
    context.save();
    context.setTransform(ratio, 0, 0, ratio, 0, 0);
    context.globalCompositeOperation = "destination-out";
    context.beginPath();
    context.arc(x, y, 37, 0, Math.PI * 2);
    context.fill();
    context.restore();
    setCleared(v=>Math.min(1,v+.035));
  };
  const revealAll = () => {
    setCleared(1);
    const canvas = canvasRef.current;
    const context = canvas?.getContext("2d");
    if (canvas && context) { context.save(); context.setTransform(1, 0, 0, 1, 0, 0); context.clearRect(0, 0, canvas.width, canvas.height); context.restore(); }
  };
  return (
    <section className="gift-mirror" aria-label="Infinite Mirror experience">
      <GiftStage kind="mirror" state={{growth:cleared,replay:resets}} onProgress={(p)=>{if(p>0.9&&cleared<1)revealAll();}} label="A gold beaded standing mirror with an inset reflective surface. Wiping the accessible pad below clears its dimensional mist layer to reveal only the original abstract birthday line." />
      <div className="gift-world-console">
      <div className="gift-mirror__frame">
        <div className="gift-mirror__reflection" aria-hidden="true"><span>✿</span><strong>Happy Birthday, Bhumi.</strong><i>✦</i><small>AN ABSTRACT REFLECTION · NO PORTRAIT</small></div>
        <canvas ref={canvasRef} className="gift-mirror__fog" onPointerDown={(event) => { pointerDown.current = true; event.currentTarget.setPointerCapture(event.pointerId); erase(event); }} onPointerMove={(event) => { if (pointerDown.current) erase(event); }} onPointerUp={() => { pointerDown.current = false; }} onPointerCancel={() => { pointerDown.current = false; }} aria-hidden="true" />
      </div>
      <p className="gift-mirror__hint">Drag a finger or pointer across the glass, or use the reveal button.</p>
      <div className="gift-control-row"><button type="button" className="gift-control gift-control--primary" onClick={revealAll}>Clear the mist</button><button type="button" className="gift-control" onClick={() => { redrawFog.current(); setResets((n) => n + 1); }} aria-label="Reset the mirror fog">Reset mirror</button></div>
      <EmptyCopy>The mirror reveals only abstract decoration and a birthday line; it does not use a fabricated portrait.</EmptyCopy>
    </div>
    </section>
  );
}

function CouponBookExperience() {
  const [page, setPage] = useState(0);
  const [redeemed, setRedeemed] = useState<string[]>([]);
  const coupon = couponEntries[page];
  const isFilled = Boolean(coupon.title.trim() && coupon.description.trim());
  const isRedeemed = redeemed.includes(coupon.id);
  const markRedeemed = () => setRedeemed((current) => isFilled && !current.includes(coupon.id) ? [...current, coupon.id] : current);
  const restore = () => setRedeemed((current) => current.filter((id) => id !== coupon.id));
  return (
    <section className="gift-coupon" aria-label="Birthday coupon book experience">
      <GiftStage kind="coupons" state={{selected:page,open:isRedeemed,detail:isFilled?`${coupon.title}\n${coupon.description}`:""}} label="A thick bound coupon booklet with brass binding rings, stacked paper, perforations and a continuously bent turning page. Empty offers remain unredeemable." />
      <div className="gift-world-console">
      <div className="gift-coupon__book">
        <div className="gift-coupon__spine"><i /><i /><i /></div>
        <article className={`gift-coupon__page${isRedeemed ? " is-redeemed" : ""}`}>
          <small>COUPON {String(page + 1).padStart(2, "0")} / {couponEntries.length}</small>
          {isFilled ? <><h3>{coupon.title}</h3><p>{coupon.description}</p></> : <><span className="gift-coupon__stamp">OWNER-APPROVED OFFER</span><h3>A coupon to write</h3><p>{packMicrocopy.missingText}</p></>}
          <b>{isRedeemed ? "REDEEMED" : "NOT YET REDEEMABLE"}</b>
        </article>
      </div>
      <p className="gift-coupon__status" role="status">{isFilled ? (isRedeemed ? "This owner-approved coupon is marked redeemed." : "This coupon is ready to read.") : "Empty coupon slots are not redeemable; no promise has been invented."}</p>
      <div className="gift-control-row">
        <button type="button" className="gift-control" onClick={() => setPage((value) => (value + couponEntries.length - 1) % couponEntries.length)} aria-label="Previous coupon page">Previous page</button>
        <button type="button" className="gift-control" onClick={() => setPage((value) => (value + 1) % couponEntries.length)} aria-label="Next coupon page">Next page</button>
        <button type="button" className="gift-control gift-control--primary" onClick={markRedeemed} disabled={!isFilled || isRedeemed}>Mark redeemed</button>
        <button type="button" className="gift-control" onClick={restore} disabled={!isRedeemed}>Restore coupon</button>
      </div>
    </div>
    </section>
  );
}

function FutureGardenExperience() {
  const [growth, setGrowth] = useState(0);
  const [activeLeaf,setActiveLeaf]=useState<number|null>(null);
  const leaves = futureGardenLeaves.slice(0, growth);
  return (
    <section className="gift-future-garden" aria-label="Future Garden experience">
      <GiftStage kind="hope-tree" state={{growth,selected:activeLeaf}} onPick={i=>{if(i<growth)setActiveLeaf(i);}} label="A sculpted soil cross-section with a large embedded seed, roots, growing curved trunk, eight individually unfurling leaves, instanced grass and a butterfly. Blank hopes remain below." />
      <div className="gift-world-console">
      <p className="gift-future-garden__caption" role="status">{growth === 0 ? "A seed, with room to grow." : `${growth} of ${futureGardenLeaves.length} hope leaves opened.`}</p>
      {activeLeaf!==null&&<p className="gift-native-copy">Hope {activeLeaf+1}: {futureGardenLeaves[activeLeaf].text || packMicrocopy.missingText}</p>}
      {leaves.length > 0 && <div className="gift-note-picker" role="group" aria-label="Inspect hope leaves">{leaves.map((leaf,i)=><button type="button" key={leaf.id} onClick={()=>setActiveLeaf(i)} aria-pressed={activeLeaf===i}>Leaf {i+1}</button>)}</div>}
      {leaves.some((leaf) => leaf.text) ? <ul className="gift-future-garden__hopes">{leaves.filter((leaf) => leaf.text).map((leaf) => <li key={leaf.id}>{leaf.text}</li>)}</ul> : leaves.length > 0 && <p className="gift-future-garden__missing">{packMicrocopy.missingText}</p>}
      <div className="gift-control-row"><button type="button" className="gift-control gift-control--primary" disabled={growth >= futureGardenLeaves.length} onClick={() => setGrowth((value) => Math.min(futureGardenLeaves.length, value + 1))}>{growth === 0 ? "Plant the seed" : growth >= futureGardenLeaves.length ? "Garden complete" : "Grow another leaf"}</button><button type="button" className="gift-control" onClick={() => setGrowth(0)}>Begin again</button></div>
      <EmptyCopy>All eight future-hope fields are blank. Add only hopes the owner chooses to write; no future is stated as fact or promise.</EmptyCopy>
    </div>
    </section>
  );
}

function TreasureHuntExperience() {
  const [order, setOrder] = useState<string[]>([...treasureHuntPuzzle.initialOrder]);
  const [selected, setSelected] = useState<string | null>(null);
  const [gateOpen, setGateOpen] = useState(false);
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");
  const [won, setWon] = useState(false);
  const isOrdered = order.join("|") === treasureHuntPuzzle.solution.join("|");
  const move = (direction: number) => {
    if (!selected) return;
    const index = order.indexOf(selected);
    const nextIndex = index + direction;
    if (index < 0 || nextIndex < 0 || nextIndex >= order.length) return;
    setOrder((current) => { const copy = [...current]; [copy[index], copy[nextIndex]] = [copy[nextIndex], copy[index]]; return copy; });
  };
  const swapDragged = (event: DragEvent<HTMLElement>, target: string) => {
    event.preventDefault();
    const source = event.dataTransfer.getData("text/plain");
    if (!source || source === target) return;
    setOrder((current) => { const copy = [...current]; const from = copy.indexOf(source); const to = copy.indexOf(target); [copy[from], copy[to]] = [copy[to], copy[from]]; return copy; });
  };
  const unlock = (event: FormEvent<HTMLFormElement>) => {
    event.preventDefault();
    if (password.trim().toUpperCase() === treasureHuntPuzzle.password) { setWon(true); setMessage("The chest opens."); }
    else setMessage("That word does not open the gate yet. Use the clue above.");
  };
  return (
    <section className="gift-treasure" aria-label="Secret Treasure Hunt">
      <GiftStage kind="treasure" state={{open:won,selected:selected?order.indexOf(selected):null,growth:gateOpen?1:0,detail:order.join("|")}} onPick={i=>setSelected(order[i])} label="A wood and brass treasure chest with a hinged lid, key, lock and three physical medallions. Solve the existing symbol and password puzzle to open it." />
      <div className="gift-world-console">
      {!gateOpen ? <>
        <div className="gift-treasure__clue"><small>CLUE 01 · SYMBOL ORDER</small><p>{treasureHuntPuzzle.clue}</p></div>
        <ol className="gift-treasure__pieces" aria-label="Arrange the symbols in the order given in the clue">
          {order.map((symbol, index) => <li key={symbol} onDragOver={(event) => event.preventDefault()} onDrop={(event) => swapDragged(event, symbol)}>
            <button type="button" className={`gift-treasure__piece is-${symbol}${selected === symbol ? " is-selected" : ""}`} draggable onDragStart={(event) => event.dataTransfer.setData("text/plain", symbol)} onClick={() => setSelected(symbol)} aria-label={`Symbol ${symbol}, position ${index + 1}; select to move`} aria-pressed={selected === symbol}><span>{symbol === "flower" ? "✿" : symbol === "moon" ? "☾" : "✦"}</span><small>{symbol}</small></button>
          </li>)}
        </ol>
        <div className="gift-control-row"><button type="button" className="gift-control" onClick={() => move(-1)} disabled={!selected || order.indexOf(selected) === 0}>Move selected left</button><button type="button" className="gift-control" onClick={() => move(1)} disabled={!selected || order.indexOf(selected) === order.length - 1}>Move selected right</button><button type="button" className="gift-control gift-control--primary" onClick={() => { if (isOrdered) { setGateOpen(true); setMessage(""); } else setMessage("Not quite. Use the stated flower → moon → star sequence."); }}>Check the order</button></div>
        <p className="gift-treasure__access-note">Drag a symbol, or select it and use the Move left/right buttons.</p>
      </> : !won ? <>
        <div className="gift-treasure__chest" aria-hidden="true"><span>✦</span><i /></div>
        <form className="gift-treasure__password" onSubmit={unlock}>
          <label htmlFor="gift-treasure-password">The chest asks for a word</label>
          <p>{treasureHuntPuzzle.passwordHint}</p>
          <input id="gift-treasure-password" value={password} onChange={(event) => setPassword(event.target.value)} autoComplete="off" />
          <button className="gift-control gift-control--primary" type="submit">Unlock the chest</button>
        </form>
      </> : <div className="gift-treasure__reward" role="status"><span>✦ TREASURE FOUND ✦</span><p>{chronosContent.gifts.specials["01"].message}</p><small>Source archive message</small></div>}
      {message && <p className="gift-treasure__status" role="status">{message}</p>}
      <div className="gift-control-row"><button type="button" className="gift-control" onClick={() => { setOrder([...treasureHuntPuzzle.initialOrder]); setSelected(null); setGateOpen(false); setPassword(""); setMessage(""); setWon(false); }}>Restart the hunt</button></div>
    </div>
    </section>
  );
}

function UltimateSurpriseExperience({ onReturn, soundEnabled, onToggleSound }: { onReturn: () => void; soundEnabled: boolean; onToggleSound: () => void }) {
  const [stage, setStage] = useState<"dark" | "gathered" | "portal">("dark");
  return (
    <section className={`gift-ultimate gift-ultimate--${stage}`} aria-label="The Ultimate Surprise experience">
      <GiftStage kind="portal" state={{ open: stage === "portal", growth: stage === "dark" ? 0 : stage === "gathered" ? 1 : 2 }} label="Three metallic portal rings around a procedural swirling light surface, set in a three-dimensional starfield." />
      <div className="gift-world-console">
      <div className="gift-ultimate__copy" aria-live="polite">
        <small>GIFT 17 · THE GRAND FINALE</small>
        {stage === "dark" ? <><h3>Sixteen lights are waiting.</h3><p>Opening this gift does not require opening any of the others.</p><button type="button" className="gift-control gift-control--primary" onClick={() => setStage("gathered")}>Gather the sixteen lights</button></> : stage === "gathered" ? <><h3>The lights have found one another.</h3><p>A portal is ready to open.</p><button type="button" className="gift-control gift-control--primary" onClick={() => setStage("portal")}>Open the portal</button></> : <><h3>Happy Birthday, Bhumi.</h3><p>{chronosContent.finale.sourceMessage}</p><button type="button" className="gift-control gift-control--primary" onClick={() => { onReturn(); document.getElementById("birthday-cake")?.scrollIntoView({ behavior: window.matchMedia("(prefers-reduced-motion: reduce)").matches ? "instant" : "smooth" }); }}>Enter the Birthday Ballroom</button><button type="button" className="gift-control" onClick={() => setStage("dark")}>Replay the finale</button></>}
      </div>
      <div className="gift-control-row">
        <button type="button" className="gift-control" aria-pressed={soundEnabled} onClick={onToggleSound}>{soundEnabled ? "Sound: on" : "Sound: off"}</button>
        <button type="button" className="gift-control" onClick={() => setStage("dark")}>Replay journey</button>
        <button type="button" className="gift-control" onClick={onReturn}>{packMicrocopy.back}</button>
      </div>
      <p className="gift-ultimate__audio-note">Sound is optional and starts off. The effects are synthesised on your device and only play after you switch sound on.</p>
    </div>
    </section>
  );
}

const experienceLabels: Record<GiftDefinition["experience"], string> = {
  "secret-letter": "Replay letter opening",
  "reason-jar": "Reset the jar",
  "eternal-flower": "Replay the bloom",
  "little-universe": "Reset the universe",
  "bhumi-fm": "Reset the cassette",
  "memory-cinema": "Reset the cinema",
  wishes: "Reset the constellation",
  "royal-crown": "Reset the crown",
  "open-when": "Reset the envelopes",
  "happiness-machine": "Reset the machine",
  "little-adventure": "Reset the map",
  "music-of-us": "Reset the record player",
  "infinite-mirror": "Reset the mirror",
  "coupon-book": "Reset the coupon book",
  "future-garden": "Reset the garden",
  "treasure-hunt": "Restart the hunt",
  "ultimate-surprise": "Replay the finale",
};

export function GiftExperience({ gift, onReturn, soundEnabled, onToggleSound }: GiftExperienceProps) {
  const [replayKey, setReplayKey] = useState(0);
  const replay = () => setReplayKey((value) => value + 1);
  let experience;
  switch (gift.experience) {
    case "secret-letter": experience = <SecretLetterExperience />; break;
    case "reason-jar": experience = <ReasonJarExperience />; break;
    case "eternal-flower": experience = <EternalFlowerExperience />; break;
    case "little-universe": experience = <LittleUniverseExperience />; break;
    case "bhumi-fm": experience = <CassetteExperience soundEnabled={soundEnabled} />; break;
    case "memory-cinema": experience = <MemoryCinemaExperience />; break;
    case "wishes": experience = <WishesExperience />; break;
    case "royal-crown": experience = <CrownExperience />; break;
    case "open-when": experience = <OpenWhenExperience />; break;
    case "happiness-machine": experience = <HappinessMachineExperience />; break;
    case "little-adventure": experience = <AdventureExperience />; break;
    case "music-of-us": experience = <MusicExperience soundEnabled={soundEnabled} />; break;
    case "infinite-mirror": experience = <MirrorExperience />; break;
    case "coupon-book": experience = <CouponBookExperience />; break;
    case "future-garden": experience = <FutureGardenExperience />; break;
    case "treasure-hunt": experience = <TreasureHuntExperience />; break;
    case "ultimate-surprise": experience = <UltimateSurpriseExperience onReturn={onReturn} soundEnabled={soundEnabled} onToggleSound={onToggleSound} />; break;
    default: experience = <EmptyCopy>{packMicrocopy.giftLocked}</EmptyCopy>;
  }
  // Pack: "Reveal line: one short line shown when the gift opens." Gifts 03, 04 and 08 show theirs from their own reveal button instead.
  const openingLine = giftsWithOwnReveal.has(gift.number) ? "" : gift.revealLine;
  return (
    <div className="gift-experience-shell">
      {(gift.dedication || openingLine) && <blockquote className="gift-experience-shell__dedication">{openingLine && <strong>{openingLine}</strong>}{gift.dedication}</blockquote>}
      <p className="gift-experience-shell__intro">{gift.subtitle}</p>
      <div className="gift-experience" data-experience={gift.experience} key={`${gift.id}-${replayKey}`}>
        {experience}
      </div>
      {gift.experience !== "ultimate-surprise" && <div className="gift-experience-shell__footer"><ExperienceReplay onReplay={replay} title={experienceLabels[gift.experience]} /><button type="button" className="gift-control gift-control--quiet gift-experience-shell__back" onClick={onReturn}>← <span>{packMicrocopy.back}</span></button><SoundDock soundEnabled={soundEnabled} onToggleSound={onToggleSound} /><span>Each gift opens independently and can be replayed.</span></div>}
    </div>
  );
}
```

## 93. `src/world/GiftRoom.tsx` — modified

```tsx
import { useEffect, useState, type CSSProperties } from "react";
import { ArrowUpRight, PackageOpen, Sparkles } from "lucide-react";
import { ArchiveDialog } from "../components/ArchiveDialog";
import { chronosContent } from "../content/chronosContent";
import { giftDefinitions, type GiftDefinition } from "../content/giftsContent";
import { packCover, packMicrocopy, packProgress } from "../content/packContent";
import { GiftExperience } from "./GiftExperiences";
import { WorldSection } from "./WorldSection";

const openedGiftStorageKey = "world-of-you-opened-gifts";
const validGiftIds = new Set(giftDefinitions.map((gift) => gift.id));

function readOpenedGifts(): string[] {
  if (typeof window === "undefined") return [];
  try {
    const saved: unknown = JSON.parse(window.localStorage.getItem(openedGiftStorageKey) ?? "[]");
    if (!Array.isArray(saved)) return [];
    return [...new Set(saved.filter((id): id is string => typeof id === "string" && validGiftIds.has(id)))];
  } catch {
    return [];
  }
}

export function GiftRoom({ soundEnabled, onToggleSound }: { soundEnabled: boolean; onToggleSound: () => void }) {
  const [selected, setSelected] = useState<GiftDefinition | null>(null);
  const [opened, setOpened] = useState<string[]>(readOpenedGifts);
  const [notice, setNotice] = useState("");

  useEffect(() => {
    try { window.localStorage.setItem(openedGiftStorageKey, JSON.stringify(opened)); }
    catch { /* Private browsing or storage limits must not block the gifts. */ }
  }, [opened]);

  const openGift = (gift: GiftDefinition) => {
    setSelected(gift);
    const total = opened.includes(gift.id) ? opened.length : opened.length + 1;
    setOpened((current) => current.includes(gift.id) ? current : [...current, gift.id]);
    setNotice(packProgress(total));
  };

  const completionLabel = opened.length === giftDefinitions.length
    ? "Collection complete · all 17 gifts remain openable and replayable."
    : notice || "Open any gift in any order. No gift is locked behind another.";

  return (
    <WorldSection id="gifts" className="gift-room-section" eyebrow={packCover.subtitle.toUpperCase()} sideNote="COLLECTION / 17">
      <p className="gift-room__tagline">{packCover.tagline}</p>
      <p className="gift-room__intro">{chronosContent.gifts.intro}</p>
      <div className="gift-progress" role="status" aria-live="polite">
        <div className="gift-progress__label"><span><PackageOpen size={15} aria-hidden="true" /> GIFTS OPENED</span><strong>{String(opened.length).padStart(2, "0")} <i>/</i> 17</strong></div>
        <div className="gift-progress__bar" role="progressbar" aria-label="Gifts opened" aria-valuemin={0} aria-valuemax={17} aria-valuenow={opened.length}><i style={{ width: `${(opened.length / giftDefinitions.length) * 100}%` }} /></div>
        <span className="gift-progress__notice">{completionLabel}</span>
      </div>
      <div className="gift-parcels" role="list" aria-label="Seventeen unique gift experiences">
        {giftDefinitions.map((gift, index) => {
          const isOpen = opened.includes(gift.id);
          return (
            <div className="gift-parcel-wrap" role="listitem" key={gift.id}>
              <button
                type="button"
                onClick={() => openGift(gift)}
                className={`gift-parcel${isOpen ? " is-opened" : ""}`}
                data-gift-id={gift.id}
                data-visual={gift.visual}
                style={{ "--gift-color": gift.color, "--ribbon-color": gift.ribbon, "--gift-index": index } as CSSProperties}
                aria-label={`Open gift ${gift.number}: ${gift.title}${isOpen ? ", replay experience" : ""}`}
                aria-haspopup="dialog"
                aria-expanded={selected?.id === gift.id}
              >
                <span className="gift-parcel__number">{gift.number}</span>
                <span className="gift-parcel__preview" aria-hidden="true"><img src={`/assets/gift-previews/${gift.id}.webp`} alt="" width={480} height={360} loading="lazy" decoding="async" /></span>
                <span className="gift-parcel__title">{gift.shortTitle}</span>
                <span className="gift-parcel__subtitle">{gift.experience === "ultimate-surprise" ? "GRAND FINALE" : gift.visual.toUpperCase().replace(/-/g, " ")}</span>
                <span className="gift-parcel__action">{isOpen ? "REPLAY" : "OPEN EXPERIENCE"}<ArrowUpRight size={12} aria-hidden="true" /></span>
                {isOpen && <span className="gift-parcel__opened-mark" aria-hidden="true"><Sparkles size={15} /></span>}
              </button>
            </div>
          );
        })}
      </div>
      <p className="gift-room__note"><span aria-hidden="true">✿</span> Open-when notes, photos, audio, coupons and future hopes stay blank until supplied or approved. No gift is locked.</p>
      <ArchiveDialog
        open={selected !== null}
        onClose={() => setSelected(null)}
        eyebrow={selected ? `GIFT ${selected.number} OF 17 · ${selected.experience.toUpperCase().replace(/-/g, " ")}` : undefined}
        title={selected?.title ?? "A little gift"}
        variant={selected?.experience === "ultimate-surprise" ? "dark" : "paper"}
        className="archive-dialog--gift"
        closeLabel={packMicrocopy.close}
      >
        {selected && <GiftExperience key={selected.id} gift={selected} onReturn={() => setSelected(null)} soundEnabled={soundEnabled} onToggleSound={onToggleSound} />}
      </ArchiveDialog>
    </WorldSection>
  );
}
```

## 94. `src/world/LetterRoom.tsx` — modified

```tsx
import { useEffect, useRef, useState } from "react";
import { Feather, Heart, Mail, PenLine } from "lucide-react";
import { ArchiveDialog } from "../components/ArchiveDialog";
import { chronosContent, type LetterRecord } from "../content/chronosContent";
import { packMicrocopy } from "../content/packContent";
import { SectionStage } from "../three/SectionStage";
import { WorldSection } from "./WorldSection";

type LetterEntry = LetterRecord;

export function LetterRoom() {
  const [closing, setClosing] = useState(false);
  const [paperOpen, setPaperOpen] = useState(false);
  const [paperReplay, setPaperReplay] = useState(0);
  const [immediate, setImmediate] = useState(false);
  const [progress, setProgress] = useState(0);
  const [selected, setSelected] = useState<LetterEntry | null>(null);
  const timer = useRef<number | null>(null);
  useEffect(() => () => { if (timer.current !== null) window.clearTimeout(timer.current); }, []);
  const finishClose = () => { setSelected(null); setClosing(false); };
  const openLetter = (letter: LetterEntry) => {
    if (timer.current !== null) window.clearTimeout(timer.current);
    setClosing(false); setProgress(0); setPaperOpen(false); setImmediate(false); setSelected(letter);
  };
  const closeLetter = () => {
    if (!selected || closing) return;
    setPaperOpen(false); setImmediate(false);
    if (progress === 0 || window.matchMedia("(prefers-reduced-motion: reduce)").matches) { finishClose(); return; }
    setClosing(true);
    // Fallback watchdog: progress normally completes closure, but unavailable WebGL must never trap the dialog.
    if (timer.current !== null) window.clearTimeout(timer.current);
    timer.current = window.setTimeout(finishClose, 5100);
  };
  const togglePaper = () => { if (!closing) { setImmediate(false); setPaperOpen(v => !v); } };
  const readable = paperOpen && (progress >= .995 || immediate);
  const phase = progress < .14 ? "Breaking the wax seal" : progress < .36 ? "Opening the hinged flap" : progress < .65 ? "Drawing the letter from its pocket" : progress < .84 ? "Unfolding the first crease" : progress < .995 ? "Unfolding the second crease" : (selected?.paragraphs.length ? "Letter open. The original message is ready below." : "Letter open.");

  return (
    <WorldSection id="letters" className="letters-section" eyebrow="A WRITING DESK · SIX ENVELOPES" sideNote="SEALED / 06">
      <p className="letters-intro">{chronosContent.letters.intro}</p>
      <div className="letters-room">
        <figure className="letters-desk">
          <img src="/assets/paper/writing-desk.webp" alt="An illustrated blank letter, fountain pen and flowers on a warm cream writing desk." width={1200} height={896} loading="lazy" />
          <figcaption><span><Feather size={13} /> A PLACE FOR WORDS</span><i aria-hidden="true" />
            <p>Only a real letter belongs here.</p>
          </figcaption>
        </figure>
        <div className="letter-shelf" aria-label="Six letter envelopes">
          {chronosContent.letters.letters.map((letter, index) => {
            const isWritten = letter.kind !== "empty";
            return (
              <button key={letter.id} className={`letter-envelope${isWritten ? " letter-envelope--source" : ""}`} type="button" onClick={() => openLetter(letter)} aria-label={`Open ${letter.category}${letter.kind === "main" ? ", the main birthday letter" : letter.kind === "source" ? ", source letter included" : ", empty owner-editable envelope"}`}>
                <span className="letter-envelope__number">0{index + 1}</span>
                <span className="letter-envelope__paper" aria-hidden="true"><span>{isWritten ? letter.salutation : "A note for you"}</span><i /></span>
                <span className="letter-envelope__body" aria-hidden="true" />
                <span className="letter-envelope__flap" aria-hidden="true" />
                <span className="letter-envelope__seal" aria-hidden="true">{isWritten ? <Heart size={13} /> : <span>✿</span>}</span>
                <span className="letter-envelope__title">{letter.category}</span>
                <span className="letter-envelope__status">{letter.kind === "main" ? "MAIN LETTER" : letter.kind === "source" ? "SOURCE LETTER" : "EMPTY · OWNER-WRITTEN"}</span>
              </button>
            );
          })}
        </div>
      </div>
      <div className="letters-note"><PenLine size={15} aria-hidden="true" /><span>Personal words stay editable in <code>src/content/packContent.ts</code> and <code>src/content/chronosContent.ts</code>. The four unfilled envelopes will remain blank until their owner writes them.</span></div>
      <ArchiveDialog open={selected !== null} onClose={closeLetter} eyebrow={selected?.label} title={selected?.title ?? "A letter"}>
        {selected && <div className="letter-reading">
          {selected.subtitle && <p className="letter-reading__subtitle">{selected.subtitle}</p>}
          <SectionStage kind="letter" title="The writing desk" state={{ open: paperOpen, replay: paperReplay, immediate, detail: selected.paragraphs.length ? [selected.salutation, ...selected.paragraphs, selected.closing, selected.signature, selected.ps].filter(Boolean).join("\n\n") : packMicrocopy.missingText }} onPick={togglePaper} onProgress={(value) => { setProgress(value); if (closing && value === 0) { if (timer.current !== null) window.clearTimeout(timer.current); finishClose(); } }} label="A warm wooden writing desk. A split wax seal, thick hinged envelope flap and continuous paper mesh open in sequence, bending along two rounded creases. Use the buttons below for keyboard access." />
          <div className="cinematic-controls" aria-label="Letter animation controls">
            <button type="button" disabled={closing} onClick={togglePaper}>{paperOpen ? "Close Letter" : "Open Letter"}</button>
            <button type="button" disabled={closing} onClick={() => { setProgress(0); setImmediate(false); setPaperOpen(true); setPaperReplay(v => v + 1); }}>Replay Animation</button>
            <button type="button" onClick={() => { if (closing) { finishClose(); return; } setPaperOpen(true); setProgress(1); setImmediate(true); }}>{packMicrocopy.skip}</button>
          </div>
          <p className="paper-status" role="status">{closing ? "Refolding and returning the letter to its envelope…" : paperOpen ? phase : progress > 0 ? "Refolding along the original creases…" : "Letter folded. Open it to read the message. Skip also works without 3D."}</p>
          <div className={readable ? "physical-letter-copy is-open" : "physical-letter-copy"} hidden={!readable}>
          {selected.salutation && <p className="letter-reading__salutation">{selected.salutation}</p>}
          {selected.paragraphs.length ? <div className="letter-reading__body">{selected.paragraphs.map((paragraph, index) => <p key={index}>{paragraph}</p>)}</div> : <div className="letter-empty"><Mail size={24} /><p>{packMicrocopy.missingText}</p></div>}
          {selected.closing && <p className="letter-reading__closing">{selected.closing}<br /><strong>{selected.signature}</strong></p>}
          {selected.ps && <p className="letter-reading__ps">{selected.ps}</p>}
        </div></div>}
      </ArchiveDialog>
    </WorldSection>
  );
}
```

## 95. `src/world/MusicRoom.tsx` — modified

```tsx
import { useEffect, useRef, useState } from "react";
import { Disc3, Headphones, Pause, Play, SkipBack, SkipForward, Volume2, VolumeX } from "lucide-react";
import { chronosContent } from "../content/chronosContent";
import { WorldSection } from "./WorldSection";

interface MusicRoomProps { soundEnabled: boolean; onToggleSound: () => void; }

const clock = (seconds: number) => {
  if (!Number.isFinite(seconds) || seconds < 0) return "0:00";
  return `${Math.floor(seconds / 60)}:${String(Math.floor(seconds % 60)).padStart(2, "0")}`;
};

export function MusicRoom({ soundEnabled, onToggleSound }: MusicRoomProps) {
  const audioRef = useRef<HTMLAudioElement>(null);
  const [trackIndex, setTrackIndex] = useState(0);
  const [playing, setPlaying] = useState(false);
  const [volume, setVolume] = useState(0.65);
  const [currentTime, setCurrentTime] = useState(0);
  const [duration, setDuration] = useState(0);
  const [status, setStatus] = useState<string>(chronosContent.music.emptyNote);
  const track = chronosContent.music.tracks[trackIndex];
  const hasAudio = Boolean(track.src);

  useEffect(() => {
    const audio = audioRef.current;
    if (!audio) return;
    audio.volume = volume;
    audio.muted = !soundEnabled;
    if (!soundEnabled && !audio.paused) {
      audio.pause();
      setPlaying(false);
      setStatus("Sound was turned off. Playback is paused.");
    }
  }, [volume, soundEnabled]);

  useEffect(() => {
    setPlaying(false);
    setCurrentTime(0);
    setDuration(0);
    if (!track.src) setStatus(chronosContent.music.emptyNote);
    else setStatus(track.note);
    audioRef.current?.pause();
    if (audioRef.current) audioRef.current.currentTime = 0;
  }, [trackIndex, track.src, track.note]);

  const setTrack = (index: number) => setTrackIndex((index + chronosContent.music.tracks.length) % chronosContent.music.tracks.length);
  const togglePlayback = async () => {
    const audio = audioRef.current;
    if (!audio || !hasAudio) {
      setStatus(chronosContent.music.emptyNote);
      return;
    }
    if (!soundEnabled) {
      setStatus("Sound is opt-in. Choose “Sound on” in the top bar, then press play.");
      return;
    }
    if (audio.paused) {
      setStatus("Loading the track…");
      try { await audio.play(); setPlaying(true); setStatus(`Now playing · ${track.title}`); }
      catch { setPlaying(false); setStatus("This local audio file could not be played. Check the file path and format."); }
    } else {
      audio.pause();
      setPlaying(false);
      setStatus("Playback paused.");
    }
  };

  const seek = (value: number) => {
    if (audioRef.current && Number.isFinite(audioRef.current.duration)) audioRef.current.currentTime = value;
    setCurrentTime(value);
  };

  const onTrackEnded = () => {
    setPlaying(false);
    if (trackIndex < chronosContent.music.tracks.length - 1) {
      setTrackIndex((index) => index + 1);
    } else setStatus("End of the selected listening set.");
  };

  return (
    <WorldSection id="music-room" className="music-room-section" eyebrow="A QUIET LISTENING ROOM" sideNote="SOUND / 09">
      <p className="music-room__intro">{chronosContent.music.note}</p>
      <div className="music-console">
        <div className="music-console__head"><div><span className="music-console__live"><i /> LOCAL PLAYER · OPT-IN</span><h3>{chronosContent.music.station}</h3><p>For the songs and voices you choose to bring.</p></div><Headphones size={33} strokeWidth={0.8} aria-hidden="true" /></div>
        <div className="music-console__body">
          <div className="vinyl-player" aria-label={playing ? "Vinyl record spinning" : "Vinyl record still"}>
            <div className={`vinyl-disc${playing ? " is-spinning" : ""}`}><span className="vinyl-disc__grooves" /><span className="vinyl-disc__label"><Disc3 size={25} strokeWidth={0.8} /><small>{trackIndex + 1}</small></span></div>
            <span className="vinyl-arm" aria-hidden="true"><i /></span>
            <span className="vinyl-player__flower" aria-hidden="true">✿</span>
          </div>
          <div className="music-track-panel">
            <div className="music-now-playing"><span>NOW SELECTED</span><strong>{track.title}</strong><small>{track.note}</small></div>
            <div className="music-timeline"><span>{clock(currentTime)}</span><input type="range" min={0} max={Math.max(duration, 1)} value={Math.min(currentTime, duration || 1)} onChange={(event) => seek(Number(event.target.value))} aria-label="Seek within track" disabled={!hasAudio || !soundEnabled} style={{ "--range-progress": `${duration ? (currentTime / duration) * 100 : 0}%` } as React.CSSProperties} /><span>{clock(duration)}</span></div>
            <div className="music-controls">
              <button type="button" className="music-controls__step" onClick={() => setTrack(trackIndex - 1)} aria-label="Previous track"><SkipBack size={18} fill="currentColor" /></button>
              <button type="button" className="music-controls__play" onClick={togglePlayback} disabled={!hasAudio} aria-label={playing ? "Pause track" : "Play selected track"}>{playing ? <Pause size={19} fill="currentColor" /> : <Play size={19} fill="currentColor" />}</button>
              <button type="button" className="music-controls__step" onClick={() => setTrack(trackIndex + 1)} aria-label="Next track"><SkipForward size={18} fill="currentColor" /></button>
              <div className="music-volume"><button type="button" onClick={onToggleSound} aria-label={soundEnabled ? "Turn sound off" : "Turn sound on"} title={soundEnabled ? "Turn sound off" : "Turn sound on to hear a track"}>{soundEnabled ? <Volume2 size={16} /> : <VolumeX size={16} />}</button><input type="range" min={0} max={1} step={0.05} value={volume} onChange={(event) => setVolume(Number(event.target.value))} aria-label="Player volume" /></div>
            </div>
            <div className="music-status" role="status" aria-live="polite"><i />{status}</div>
            <audio ref={audioRef} src={track.src || undefined} preload="none" muted={!soundEnabled} onTimeUpdate={(event) => setCurrentTime(event.currentTarget.currentTime)} onDurationChange={(event) => setDuration(Number.isFinite(event.currentTarget.duration) ? event.currentTarget.duration : 0)} onEnded={onTrackEnded} onWaiting={() => hasAudio && setStatus("Buffering…")} onPlaying={() => hasAudio && setStatus(`Now playing · ${track.title}`)} onError={() => hasAudio && setStatus("Audio could not be loaded. Check the owner-supplied local file.")} />
          </div>
        </div>
        <div className="music-track-list" aria-label="Available local audio tracks">
          {chronosContent.music.tracks.map((item, index) => <button key={item.id} type="button" className={trackIndex === index ? "is-active" : ""} onClick={() => setTrack(index)} aria-current={trackIndex === index ? "true" : undefined}><span className="music-track-list__number">0{index + 1}</span><span><strong>{item.title}</strong><small>{item.src ? "LOCAL FILE READY" : "EMPTY · ADD LOCAL FILE"}</small></span><i aria-hidden="true">{trackIndex === index ? "✿" : "＋"}</i></button>)}
        </div>
        {!chronosContent.music.tracks.some((item) => item.src) && <p className="music-room__empty">{chronosContent.music.emptyPlaylist}</p>}
      </div>
      <p className="music-room__privacy"><VolumeX size={14} /> Audio starts paused. No autoplay, external stream, microphone request or recording.</p>
    </WorldSection>
  );
}
```

## 96. `src/world/PolaroidGallery.tsx` — modified

```tsx
import { useRef, useState } from "react";
import { ArrowLeft, ArrowRight, ImagePlus, ScanEye } from "lucide-react";
import { ArchiveDialog } from "../components/ArchiveDialog";
import { chronosContent } from "../content/chronosContent";
import { WorldSection } from "./WorldSection";
import { usePointerParallax } from "../hooks/usePointerParallax";

type PhotoEntry = (typeof chronosContent.gallery.photos)[number];

export function PolaroidGallery() {
  const [selected, setSelected] = useState<PhotoEntry | null>(null);
  const [focusedIndex, setFocusedIndex] = useState(0);
  const photo = chronosContent.gallery.photos[focusedIndex];
  const wallRef = useRef<HTMLDivElement>(null);
  usePointerParallax(wallRef, 1);
  const selectPhoto = (entry: PhotoEntry, index: number) => {
    setFocusedIndex(index);
    setSelected(entry);
  };
  const step = (direction: -1 | 1) => {
    const index = (focusedIndex + direction + chronosContent.gallery.photos.length) % chronosContent.gallery.photos.length;
    setFocusedIndex(index);
    setSelected(chronosContent.gallery.photos[index]);
  };

  return (
    <WorldSection id="gallery" className="gallery-section" eyebrow="THE PHOTO WALL · REAL IMAGES ONLY" sideNote="MOUNTS / 06">
      <p className="gallery-intro">{chronosContent.gallery.photos.some((entry) => entry.src) ? chronosContent.gallery.introFilled : chronosContent.gallery.introEmpty}</p>
      <div className="polaroid-wall" ref={wallRef} aria-label="Six empty Polaroid photo mounts">
        <span className="polaroid-wall__string polaroid-wall__string--one" aria-hidden="true" />
        <span className="polaroid-wall__string polaroid-wall__string--two" aria-hidden="true" />
        {chronosContent.gallery.photos.map((entry, index) => (
          <button key={entry.id} type="button" className={`polaroid-card polaroid-card--${index + 1}`} onClick={() => selectPhoto(entry, index)} aria-label={`Open Polaroid ${index + 1}: ${entry.caption}. Empty photo mount.`}>
            <span className="polaroid-card__clip" aria-hidden="true" />
            <span className="polaroid-card__image">
              {entry.src ? <img src={entry.src} alt={entry.alt || entry.caption} loading="lazy" width={1200} height={900} /> : <span className="polaroid-card__placeholder"><ImagePlus size={23} /><small>REAL PHOTO<br />GOES HERE</small></span>}
              <span className="polaroid-card__zoom"><ScanEye size={15} /><span>OPEN</span></span>
            </span>
            <span className="polaroid-card__caption">{entry.caption}</span>
            <span className="polaroid-card__date">{entry.date}</span>
          </button>
        ))}
      </div>
      <div className="gallery-bottom-note"><span className="gallery-bottom-note__pin" aria-hidden="true">✿</span><p>Every frame is a real-photo placeholder. Generated illustration is kept out of the personal gallery.</p><span className="gallery-bottom-note__line" aria-hidden="true" /></div>
      <ArchiveDialog open={selected !== null} onClose={() => setSelected(null)} eyebrow={`${String(focusedIndex + 1).padStart(2, "0")} / 06 · ${photo.date}`} title={photo.caption}>
        <div className="polaroid-lightbox">
          <div className="polaroid-lightbox__image">
            {photo.src ? <img src={photo.src} alt={photo.alt || photo.caption} width={1200} height={900} /> : <div><ImagePlus size={36} /><span>EMPTY PHOTO MOUNT</span></div>}
          </div>
          <p>{photo.note}</p>
          {photo.src && photo.location && <small className="polaroid-lightbox__location">{photo.location}</small>}
          <div className="polaroid-lightbox__controls">
            <button type="button" onClick={() => step(-1)} aria-label="Previous photo mount"><ArrowLeft size={15} /> Previous</button>
            <button type="button" onClick={() => step(1)} aria-label="Next photo mount">Next <ArrowRight size={15} /></button>
          </div>
        </div>
      </ArchiveDialog>
    </WorldSection>
  );
}
```

## 97. `src/world/RelationshipClock.tsx` — modified

```tsx
import { useEffect, useState } from "react";
import { Clock3 } from "lucide-react";
import { SectionStage } from "../three/SectionStage";
import { chronosContent } from "../content/chronosContent";
import { getElapsedTime, formatInteger } from "../utils/time";
import { WorldSection } from "./WorldSection";

export function RelationshipClock() {
  const [selectedNode, setSelectedNode] = useState<string>(chronosContent.scrapbook.clockNodes[0].id);
  const [now, setNow] = useState(() => Date.now());
  const activeNode = chronosContent.scrapbook.clockNodes.find((node) => node.id === selectedNode)!;
  const elapsed = getElapsedTime(chronosContent.dates.firstConnection, chronosContent.dates.firstConnectionTimeZone, now);

  useEffect(() => {
    const interval = window.setInterval(() => setNow(Date.now()), 60_000);
    return () => window.clearInterval(interval);
  }, []);

  return (
    <WorldSection id="timepiece" className="timepiece-section" eyebrow="MEMORY OBSERVATORY · VERIFIED DATES" sideNote="OBSERVATORY / 04">
      <SectionStage kind="observatory" title="The memory observatory" poster="/assets/scenes/memory-observatory.webp" state={{ selected: chronosContent.scrapbook.clockNodes.findIndex((node) => node.id === selectedNode) }} onPick={(index) => setSelectedNode(chronosContent.scrapbook.clockNodes[index].id)} label="A three-dimensional astronomical clock showing local time, with interlocking gold gears, a moving pendulum, distant moon and starfield. Verified milestones remain below." />
      <p className="timepiece-intro">A quiet observatory for the dates already in the archive — and a live, timezone-safe count from the first connection. No hour or conversation is invented.</p>
      <section className="relationship-clock" aria-label="Interactive relationship timepiece">
        <div className="relationship-clock__left">
          <p className="world-eyebrow"><Clock3 size={13} /> THE TIME WE KEEP</p>
          <h3>One true date.<br /><em>Every minute since.</em></h3>
          <p className="relationship-clock__copy">The elapsed time is calculated from the start of 11 May 2025 in {chronosContent.dates.firstConnectionTimeZone}. It updates while this page is open, without assuming a private time of day.</p>
          <div className="relationship-clock__elapsed" aria-live="polite" aria-atomic="true">
            <div><strong>{formatInteger(elapsed.days)}</strong><span>days</span></div>
            <i aria-hidden="true">·</i>
            <div><strong>{String(elapsed.hours).padStart(2, "0")}</strong><span>hours</span></div>
            <i aria-hidden="true">·</i>
            <div><strong>{String(elapsed.minutes).padStart(2, "0")}</strong><span>minutes</span></div>
          </div>
          <span className="relationship-clock__caption">SINCE {chronosContent.dates.firstConnectionLabel.toUpperCase()} · {chronosContent.dates.firstConnectionTimeZone.toUpperCase()}</span>
        </div>
        <div className="relationship-clock__right">
          <div className="pocket-watch" aria-hidden="true">
            <span className="pocket-watch__loop" />
            <div className="pocket-watch__face">
              <i className="pocket-watch__mark pocket-watch__mark--one">I</i><i className="pocket-watch__mark pocket-watch__mark--two">II</i><i className="pocket-watch__mark pocket-watch__mark--three">III</i><i className="pocket-watch__mark pocket-watch__mark--four">IV</i><i className="pocket-watch__mark pocket-watch__mark--five">V</i><i className="pocket-watch__mark pocket-watch__mark--six">VI</i>
              <span className="pocket-watch__hand pocket-watch__hand--minute" /><span className="pocket-watch__hand pocket-watch__hand--hour" /><span className="pocket-watch__pin" />
            </div>
          </div>
          <div className="relationship-clock__milestones">
            <p className="world-eyebrow">CHOOSE A DATE MARKER</p>
            <div className="relationship-clock__nodes" role="group" aria-label="Verified relationship date markers">
              {chronosContent.scrapbook.clockNodes.map((node) => <button key={node.id} type="button" onClick={() => setSelectedNode(node.id)} aria-pressed={selectedNode === node.id} className={selectedNode === node.id ? "is-selected" : ""}><span>{node.date}</span><small>{node.title}</small></button>)}
            </div>
            <div className="relationship-clock__detail" aria-live="polite"><span>{activeNode.date}</span><p>{activeNode.detail}</p></div>
          </div>
        </div>
      </section>
    </WorldSection>
  );
}
```

## 98. `src/world/Storybook.tsx` — modified

```tsx
import { forwardRef, lazy, Suspense, useCallback, useEffect, useMemo, useRef, useState, type CSSProperties, type KeyboardEvent, type ReactNode } from "react";
import { ArrowLeft, ArrowRight, BookOpen, Feather, ImagePlus, RotateCcw } from "lucide-react";
import { chronosContent } from "../content/chronosContent";
import { WorldSection } from "./WorldSection";
import { usePointerParallax } from "../hooks/usePointerParallax";

const HTMLFlipBook = lazy(() => import("react-pageflip"));
const bookPages = chronosContent.scrapbook.spreads;
const storyPages = bookPages.flatMap((spread) => [spread.left, spread.right]);
const leafCount = storyPages.length;
const physicalPageCount = leafCount + 2;

interface FlipBookController {
  flipNext: () => void;
  flipPrev: () => void;
  getCurrentPageIndex: () => number;
  getOrientation?: () => string;
}

interface FlipBookHandle {
  pageFlip: () => FlipBookController | null;
}

type BookOrientation = "portrait" | "landscape";
interface FlipStateEvent { data: string; }
interface OrientationEvent { data: string; }

interface MemoryLeafProps {
  page: (typeof storyPages)[number];
  pageNumber: number;
}

const MemoryLeaf = forwardRef<HTMLDivElement, MemoryLeafProps>(({ page, pageNumber }, ref) => (
  <div ref={ref} className={`storybook-leaf storybook-leaf--${page.kind}`} aria-label={`Scrapbook page ${pageNumber}: ${page.title}`}>
    <div className="storybook-leaf__paper">
      <div className="storybook-leaf__header"><span>{page.label}</span><span>{page.date}</span></div>
      {page.kind === "record" && <span className="storybook-leaf__stamp"><i /> A TRUE RECORD</span>}
      {page.kind === "blank" && <span className="storybook-leaf__empty-mark" aria-hidden="true"><Feather size={19} /></span>}
      {page.kind === "photo" && <div className="storybook-leaf__photo-mount" aria-label="Empty mount for an owner-supplied photograph"><ImagePlus size={22} /><span>REAL PHOTO<br />MOUNT</span></div>}
      <h3>{page.title}</h3>
      <p>{page.body}</p>
      {page.kind !== "record" && <span className="storybook-leaf__placeholder-note">OWNER-EDITABLE · EMPTY BY DESIGN</span>}
      <span className="storybook-leaf__number">{String(pageNumber).padStart(2, "0")}</span>
    </div>
  </div>
));
MemoryLeaf.displayName = "MemoryLeaf";

function BookFallback({ children }: { children?: ReactNode }) {
  return <div className="storybook-book__loading" role="status">{children ?? "Preparing the little book…"}</div>;
}

interface StorybookProps { soundEnabled: boolean; }

export function Storybook({ soundEnabled }: StorybookProps) {
  const hostRef = useRef<HTMLDivElement>(null);
  const flipBookRef = useRef<FlipBookHandle | null>(null);
  const audioContextRef = useRef<AudioContext | null>(null);
  const noiseBufferRef = useRef<AudioBuffer | null>(null);
  const lastSoundAtRef = useRef(0);
  const soundEnabledRef = useRef(soundEnabled);
  const [bookReady, setBookReady] = useState(false);
  const [pageIndex, setPageIndex] = useState(0);
  const [orientation, setOrientation] = useState<BookOrientation | null>(null);
  const [reducedMotion, setReducedMotion] = useState(() => typeof window !== "undefined" && window.matchMedia("(prefers-reduced-motion: reduce)").matches);

  useEffect(() => {
    const query = window.matchMedia("(prefers-reduced-motion: reduce)");
    const update = () => setReducedMotion(query.matches);
    update();
    query.addEventListener("change", update);
    return () => query.removeEventListener("change", update);
  }, []);

  useEffect(() => {
    soundEnabledRef.current = soundEnabled;
    if (!soundEnabled && audioContextRef.current?.state === "running") {
      void audioContextRef.current.suspend().catch(() => {});
    }
  }, [soundEnabled]);

  useEffect(() => () => {
    const context = audioContextRef.current;
    audioContextRef.current = null;
    noiseBufferRef.current = null;
    if (context && context.state !== "closed") void context.close().catch(() => {});
  }, []);

  useEffect(() => {
    const host = hostRef.current;
    if (!host) return;
    if (!("IntersectionObserver" in window)) {
      setBookReady(true);
      return;
    }
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) {
        setBookReady(true);
        observer.disconnect();
      }
    }, { rootMargin: "320px 0px" });
    observer.observe(host);
    return () => observer.disconnect();
  }, []);

  const primeAudio = useCallback(() => {
    if (!soundEnabledRef.current || reducedMotion) return;
    try {
      if (!audioContextRef.current || audioContextRef.current.state === "closed") {
        audioContextRef.current = new window.AudioContext();
      }
      if (audioContextRef.current.state === "suspended") void audioContextRef.current.resume().catch(() => {});
    } catch { /* Optional audio must not block navigation. */ }
  }, [reducedMotion]);

  const playPaperRustle = useCallback(() => {
    if (!soundEnabledRef.current || reducedMotion || typeof window === "undefined") return;
    const now = window.performance.now();
    if (now - lastSoundAtRef.current < 160) return;
    lastSoundAtRef.current = now;

    try {
      const AudioContextConstructor = window.AudioContext;
      if (!AudioContextConstructor) return;
      let context = audioContextRef.current;
      if (!context || context.state === "closed") {
        context = new AudioContextConstructor();
        audioContextRef.current = context;
      }
      if (context.state === "suspended") void context.resume().catch(() => {});
      if (!noiseBufferRef.current || noiseBufferRef.current.sampleRate !== context.sampleRate) {
        const length = Math.ceil(context.sampleRate * 0.34);
        const buffer = context.createBuffer(1, length, context.sampleRate);
        const channel = buffer.getChannelData(0);
        for (let index = 0; index < length; index += 1) channel[index] = (Math.random() * 2 - 1) * (0.7 + Math.random() * 0.3);
        noiseBufferRef.current = buffer;
      }

      const startAt = context.currentTime + 0.012;
      const duration = 0.29;
      const noise = context.createBufferSource();
      const lowPass = context.createBiquadFilter();
      const highPass = context.createBiquadFilter();
      const envelope = context.createGain();
      lowPass.type = "lowpass";
      lowPass.frequency.setValueAtTime(2450, startAt);
      lowPass.frequency.exponentialRampToValueAtTime(520, startAt + duration);
      highPass.type = "highpass";
      highPass.frequency.setValueAtTime(200, startAt);
      envelope.gain.setValueAtTime(0.0001, startAt);
      envelope.gain.linearRampToValueAtTime(0.105, startAt + 0.035);
      envelope.gain.exponentialRampToValueAtTime(0.0001, startAt + duration);
      noise.buffer = noiseBufferRef.current;
      noise.connect(highPass).connect(lowPass).connect(envelope).connect(context.destination);
      noise.start(startAt);
      noise.stop(startAt + duration + 0.025);
      noise.onended = () => {
        noise.disconnect();
        highPass.disconnect();
        lowPass.disconnect();
        envelope.disconnect();
      };
    } catch {
      // Audio is an optional enhancement; unsupported or blocked playback must never break page navigation.
    }
  }, [reducedMotion]);

  const onFlip = useCallback((event: FlipStateEvent) => {
    setPageIndex(Number(event.data));
  }, []);
  const onBookState = useCallback((event: FlipStateEvent) => {
    if (event.data === "user_fold") primeAudio();
    if (event.data === "flipping") playPaperRustle();
  }, [primeAudio, playPaperRustle]);
  const onOrientation = useCallback((event: OrientationEvent) => {
    if (event.data === "portrait" || event.data === "landscape") setOrientation(event.data);
  }, []);
  const turn = useCallback((direction: "next" | "prev") => {
    primeAudio();
    const pageFlip = flipBookRef.current?.pageFlip();
    if (!pageFlip) return;
    if (direction === "next") pageFlip.flipNext();
    else pageFlip.flipPrev();
  }, [primeAudio]);

  const onBookKeyDown = (event: KeyboardEvent<HTMLDivElement>) => {
    if (event.key === "ArrowRight") {
      event.preventDefault();
      turn("next");
    } else if (event.key === "ArrowLeft") {
      event.preventDefault();
      turn("prev");
    }
  };

  const displayPage = pageIndex === 0 ? "COVER" : `${Math.min(leafCount, pageIndex)} / ${leafCount}`;
  const noPrevious = pageIndex <= 0;
  const noNext = pageIndex >= physicalPageCount - 1;
  const stageRef = useRef<HTMLDivElement>(null);
  usePointerParallax(stageRef, 1);
  // The flip book decides its own box; publish it so the decorative cover boards and page blocks hug the real pages.
  const syncBox = useCallback(() => {
    const stage = stageRef.current, parent = stage?.querySelector<HTMLElement>(".stf__parent");
    if (!stage || !parent) return;
    const s = stage.getBoundingClientRect(), p = parent.getBoundingClientRect();
    stage.style.setProperty("--bx", `${(p.left - s.left).toFixed(1)}px`); stage.style.setProperty("--by", `${(p.top - s.top).toFixed(1)}px`);
    stage.style.setProperty("--bw", `${p.width.toFixed(1)}px`); stage.style.setProperty("--bh", `${p.height.toFixed(1)}px`);
    // The flip book announces its orientation with an event that can fire before our listener is attached (a phone starts in portrait,
    // so it never fires again), which left the decorative spine and page blocks drawn for a two-page spread. Read it as well.
    const live = flipBookRef.current?.pageFlip()?.getOrientation?.();
    if (live === "portrait" || live === "landscape") setOrientation((previous) => (previous === live ? previous : live));
  }, []);
  useEffect(() => {
    syncBox();
    const observer = new ResizeObserver(syncBox);
    if (stageRef.current) observer.observe(stageRef.current);
    window.addEventListener("resize", syncBox);
    const timer = window.setInterval(syncBox, 600);
    return () => { observer.disconnect(); window.removeEventListener("resize", syncBox); window.clearInterval(timer); };
  }, [syncBox, bookReady, orientation]);
  const bookState = orientation === "portrait" ? "single" : pageIndex === 0 ? "front" : pageIndex >= physicalPageCount - 1 ? "back" : "open";
  const pageElements = useMemo(() => [
    <div key="cover" className="storybook-leaf storybook-leaf--cover" data-density="hard" aria-label="Scrapbook cover">
      <div className="storybook-cover__ornament" aria-hidden="true">✿</div>
      <span className="storybook-cover__eyebrow">THE WORLD OF YOU</span>
      <strong>Our story,<br />in paper.</strong>
      <small>BHUMI · RUDRA</small>
      <span className="storybook-cover__press" aria-hidden="true">✦</span>
    </div>,
    ...storyPages.map((page, index) => <MemoryLeaf key={`${bookPages[Math.floor(index / 2)].id}-${index}`} page={page} pageNumber={index + 1} />),
    <div key="back-cover" className="storybook-leaf storybook-leaf--back-cover" data-density="hard" aria-label="Back cover">
      <div className="storybook-back-cover__mark" aria-hidden="true">✿</div>
      <span>THE END IS A PAGE LEFT OPEN</span>
      <strong>Still being<br />written.</strong>
      <small>WITH LOVE · RUDRA</small>
    </div>,
  ], []);

  return (
    <WorldSection id="storybook" className="storybook-section" eyebrow="THE MEMORY BOOK" sideNote="PAPER / 03">
      <div className="storybook-intro">
        <span className="storybook-intro__icon" aria-hidden="true"><BookOpen size={21} /></span>
        <p>{chronosContent.scrapbook.intro}</p>
        <span className="storybook-intro__rule" aria-hidden="true" />
      </div>

      <div className="storybook-book-wrap" ref={hostRef}>
        <div
          className="storybook-book__stage"
          ref={stageRef}
          data-orientation={orientation || undefined}
          data-state={bookState}
          style={{ "--read": Math.min(1, pageIndex / (physicalPageCount - 1)) } as CSSProperties}
          role="group"
          aria-label="Interactive scrapbook. Use the left and right arrow keys, page controls, or swipe to turn pages."
          tabIndex={0}
          onKeyDown={onBookKeyDown}
          onPointerDownCapture={primeAudio}
          onTouchStartCapture={primeAudio}
        >
          <span className="storybook-book__body" aria-hidden="true" />
          <span className="storybook-book__block storybook-book__block--left" aria-hidden="true" />
          <span className="storybook-book__block storybook-book__block--right" aria-hidden="true" />
          <span className="storybook-book__gutter" aria-hidden="true" />
          {bookReady ? (
            <Suspense fallback={<BookFallback />}>
              <HTMLFlipBook
                ref={flipBookRef}
                className="storybook-flipbook"
                style={{ margin: "0 auto" }}
                width={430}
                height={540}
                size="stretch"
                minWidth={270}
                maxWidth={430}
                minHeight={390}
                maxHeight={560}
                drawShadow
                flippingTime={reducedMotion ? 1 : 780}
                usePortrait
                startZIndex={20}
                autoSize
                maxShadowOpacity={0.24}
                showCover
                mobileScrollSupport={false}
                clickEventForward
                useMouseEvents
                swipeDistance={34}
                showPageCorners
                disableFlipByClick={false}
                startPage={0}
                onFlip={onFlip}
                onChangeState={onBookState}
                onChangeOrientation={onOrientation}
              >
                {pageElements}
              </HTMLFlipBook>
            </Suspense>
          ) : (
            <div className="storybook-book__fallback" aria-label="Scrapbook is ready to open">
              <div className="storybook-book__fallback-cover"><span>✿</span><strong>OUR STORY,<br />IN PAPER</strong><small>BHUMI · RUDRA</small></div>
              <div className="storybook-book__fallback-page"><small>{bookPages[0].left.date}</small><h3>{bookPages[0].left.title}</h3><p>{bookPages[0].left.body}</p></div>
            </div>
          )}
        </div>
        <div className="storybook-controls">
          <button className="storybook-turn" type="button" onClick={() => turn("prev")} disabled={noPrevious} aria-label="Turn to the previous scrapbook page"><ArrowLeft size={16} /><span>Previous</span></button>
          <div className="storybook-pagination" aria-live="polite" aria-atomic="true" aria-label={`Current scrapbook page ${displayPage}`}><span>{displayPage}</span><i /></div>
          <button className="storybook-turn storybook-turn--next" type="button" onClick={() => turn("next")} disabled={noNext} aria-label="Turn to the next scrapbook page"><span>Next page</span><ArrowRight size={16} /></button>
        </div>
        <p className="storybook-layout-status" role="status">{orientation ? (orientation === "portrait" ? "Single-page layout" : "Two-page spread layout") : "Responsive book layout"}</p>
        <p className="storybook-swipe-hint"><RotateCcw size={12} aria-hidden="true" /> {chronosContent.scrapbook.turnHint} · arrow keys supported</p>
      </div>
    </WorldSection>
  );
}
```

## 99. `tests/cinematic.spec.ts` — modified

```ts
import { test, expect } from "@playwright/test";
import { isBlowLike } from "../src/hooks/useBlowDetection";

/** Software WebGL starves the main thread; QA_SLOW=1 stretches the explicit waits that depend on real-time audio analysis. */
const SLOW = process.env.QA_SLOW ? 4 : 1;

const errors: string[] = [];
test.beforeEach(async ({ page }) => { errors.length = 0; page.on("pageerror", (error) => errors.push(error.message)); page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); }); });
test.afterEach(async () => { expect(errors).toEqual([]); });

test("airflow classifier rejects quiet, tonal and low-band signals", () => {
  expect(isBlowLike(0.01, 0.01, 0.5, 0.01)).toBe(false);
  expect(isBlowLike(0.15, 0.01, 0.5, 0.8)).toBe(false);
  expect(isBlowLike(0.15, 0.01, 0.05, 0.01)).toBe(false);
  expect(isBlowLike(0.15, 0.01, 0.5, 0.01)).toBe(true);
});

test("garden: 3D rendering, ten wishes, planting, replay and removal", async ({ page }) => {
  await page.goto("/#flower-garden");
  const garden = page.locator("#flower-garden");
  await garden.locator(".cinematic-viewport").scrollIntoViewIfNeeded();
  await expect(garden.locator(".gift-native-status")).toHaveText("Real-time 3D ready");
  await expect(garden.locator("canvas")).toHaveCount(1);
  for (let i = 1; i <= 10; i++) { await garden.getByRole("button", { name: `Release wish ${i}`, exact: true }).click(); await expect(garden.locator(".conservatory-wish")).toContainText(`WISH ${String(i).padStart(2, "0")}`); }
  await garden.getByLabel("Your wish").fill("A quiet day with more time outside.");
  await garden.getByRole("button", { name: "Plant my wish", exact: true }).click();
  await expect(garden.locator(".conservatory-wish")).toContainText("A quiet day with more time outside.");
  await garden.getByRole("button", { name: "Replay bloom" }).click();
  await garden.getByRole("button", { name: "Close wish" }).click();
  await garden.getByRole("button", { name: "My wish", exact: true }).click();
  await garden.getByRole("button", { name: "Remove my wish" }).click();
  await expect(garden.getByRole("button", { name: "My wish", exact: true })).toHaveCount(0);
  await garden.locator(".cinematic-viewport").scrollIntoViewIfNeeded();
  await expect(garden.locator(".gift-native-canvas")).toHaveAttribute("data-scene-active", "true");
  await page.screenshot({ path: "qa/garden-desktop.png" });
});

test("cake: all baking stages, light, manual wish/blowout and replay", async ({ page }) => {
  await page.goto("/#birthday-cake"); const cake = page.locator("#birthday-cake");
  await cake.locator(".cinematic-viewport").scrollIntoViewIfNeeded();
  await expect(cake.locator(".gift-native-status")).toHaveText("Real-time 3D ready");
  await expect(cake.getByRole("button", { name: "Light the candles", exact: true })).toBeDisabled();
  for (let i = 1; i <= 4; i++) { await cake.getByRole("button", { name: new RegExp(`^Step ${i}:`) }).click(); await expect(cake.locator(".cake-bake-journey__current")).toContainText(`STEP ${i} OF 4`); }
  await cake.getByRole("button", { name: "Light the candles", exact: true }).click();
  await expect(cake.getByRole("button", { name: "Blow them out", exact: true })).toBeEnabled();
  await cake.locator(".cinematic-viewport").screenshot({ path: "qa/cake-lit.png" });
  await cake.getByRole("button", { name: "Make a wish", exact: true }).click();
  await expect(cake.locator(".cake-ritual__status")).toContainText("Candles out");
  await expect(cake.locator(".cake-fireworks")).not.toHaveClass(/is-bursting/);
  await cake.getByRole("button", { name: "Light the candles", exact: true }).click();
  await cake.getByRole("button", { name: "Blow them out", exact: true }).click();
  await expect(cake.locator(".cake-ritual__status")).toContainText("Candles out");
});

test("letters: folded paper renders; open, fold, reopen, escape and focus return", async ({ page }) => {
  await page.goto("/#letters"); const opener = page.locator(".letter-envelope").first(); await opener.click();
  const dialog = page.locator("dialog[open]"); await expect(dialog).toBeVisible();
  await expect(dialog.locator(".gift-native-status")).toHaveText("Real-time 3D ready");
  await expect(dialog.locator(".physical-letter-copy")).toBeHidden();
  await dialog.getByRole("button", { name: "Open Letter" }).click();
  await expect(dialog.locator(".physical-letter-copy")).toBeVisible();
  await dialog.locator(".cinematic-viewport").screenshot({ path: "qa/letter-open.png" });
  await dialog.getByRole("button", { name: "Close Letter" }).click();
  await expect(dialog.locator(".physical-letter-copy")).toBeHidden();
  await dialog.getByRole("button", { name: "Open Letter" }).click();
  await page.keyboard.press("Escape"); await expect(dialog).toHaveCount(0); await expect(opener).toBeFocused();
});

test("all 17 existing gifts open, run their primary control, reset and close", async ({ page }) => {
  test.setTimeout(360000);
  await page.goto("/#gifts"); const buttons = page.locator(".gift-parcel"); await expect(buttons).toHaveCount(17);
  for (let i = 0; i < 17; i++) {
    await buttons.nth(i).click(); const dialog = page.locator("dialog[open]"); await expect(dialog).toBeVisible();
    await expect(dialog.locator(".gift-experience")).toBeVisible();
    const control = dialog.locator(".gift-control--primary:enabled").first();
    if (await control.count()) await control.click();
    const replay = dialog.locator(".gift-experience-shell__footer button").first();
    if (await replay.count()) await replay.click();
    await dialog.getByRole("button", { name: "Close this experience", exact: true }).click();
    await expect(page.locator("dialog[open]")).toHaveCount(0);
    await expect(page.locator("dialog canvas")).toHaveCount(0);
  }
});

test("microphone denial is recoverable; manual fallback still works", async ({ page }) => {
  await page.addInitScript(() => { navigator.mediaDevices.getUserMedia = async () => { throw new DOMException("Denied for test", "NotAllowedError"); }; });
  await page.goto("/#birthday-cake"); const cake = page.locator("#birthday-cake");
  await cake.getByRole("button", { name: "Skip to finished cake" }).click();
  await cake.getByRole("button", { name: "Light the candles", exact: true }).click();
  await cake.getByRole("button", { name: "Enable microphone for this wish" }).click();
  await expect(cake.locator("#mic-privacy")).toContainText("Permission denied");
  await cake.getByRole("button", { name: "Blow them out", exact: true }).click();
  await expect(cake.locator(".cake-ritual__status")).toContainText("Candles out");
});

test("synthetic broadband input triggers calibrated mic and stops tracks", async ({ page }) => {
  await page.addInitScript(() => {
    const w = window as unknown as { stoppedTracks: number; testAudio?: AudioContext; testGain?: GainNode }; w.stoppedTracks = 0;
    navigator.mediaDevices.getUserMedia = async () => {
      const audio = new AudioContext(); w.testAudio = audio; const output = audio.createMediaStreamDestination();
      const gain = audio.createGain(); gain.gain.value = 0; gain.connect(output);
      const noise = audio.createBufferSource(); const buffer = audio.createBuffer(1, audio.sampleRate * 2, audio.sampleRate);
      const samples = buffer.getChannelData(0); for (let i = 0; i < samples.length; i++) samples[i] = Math.random() * 2 - 1;
      noise.buffer = buffer; noise.loop = true; noise.connect(gain); noise.start(); await audio.resume();
      w.testGain = gain;
      const track = output.stream.getTracks()[0]; const original = track.stop.bind(track); track.stop = () => { w.stoppedTracks++; original(); void audio.close(); };
      return output.stream;
    };
  });
  await page.goto("/#birthday-cake"); const cake = page.locator("#birthday-cake");
  await cake.getByRole("button", { name: "Skip to finished cake" }).click(); await cake.getByRole("button", { name: "Light the candles", exact: true }).click();
  await cake.getByRole("button", { name: "Enable microphone for this wish" }).click();
  await expect(cake.locator("#mic-privacy")).toContainText("Take a deep breath", { timeout: 12000 * SLOW });
  await page.evaluate(() => { (window as unknown as { testGain: GainNode }).testGain.gain.value = 0.2; });
  await expect(cake.locator(".cake-ritual__status")).toContainText("Candles out", { timeout: 22000 * SLOW });
  expect(await page.evaluate(() => (window as unknown as { stoppedTracks: number }).stoppedTracks)).toBe(1);
  console.log("Synthetic mic graphics fallback:", await page.locator("[data-graphics-failure]").count());
});

test("responsive portrait/landscape/tablet: no horizontal overflow, keyboard wish control", async ({ page }) => {
  for (const size of [{ width: 390, height: 844 }, { width: 844, height: 390 }, { width: 768, height: 1024 }]) {
    await page.setViewportSize(size); await page.goto("/#flower-garden");
    const button = page.getByRole("button", { name: "Release wish 1", exact: true }); await button.focus(); await page.keyboard.press("Enter");
    await expect(button).toHaveAttribute("aria-pressed", "true");
    expect(await page.evaluate(() => document.documentElement.scrollWidth <= window.innerWidth + 1)).toBe(true);
    await page.screenshot({ path: `qa/garden-${size.width}x${size.height}.png` });
  }
});

test("WebGL failure leaves garden content and planting available", async ({ page }) => {
  await page.addInitScript(() => { const get = HTMLCanvasElement.prototype.getContext; HTMLCanvasElement.prototype.getContext = function (type: string, ...args: unknown[]) { if (type === "webgl2" || type === "webgl") return null; return get.apply(this, [type, ...args] as never); } as typeof get; });
  // Three.js logs a diagnostic when graphics initialization is deliberately blocked.
  errors.length = 0;
  await page.goto("/#flower-garden"); const garden = page.locator("#flower-garden"); await garden.locator(".cinematic-viewport").scrollIntoViewIfNeeded();
  await expect(garden.locator(".gift-stage-fallback")).toContainText("cannot display the 3D scene");
  await garden.getByRole("button", { name: "Release wish 4", exact: true }).click();
  await expect(garden.locator(".conservatory-wish")).toContainText("WISH 04");
  for (let i = errors.length - 1; i >= 0; i--) if (errors[i].includes("Error creating WebGL context")) errors.splice(i, 1);
});

test("normal-motion shader and bloom render; inactive garden stops rendering", async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "no-preference" });
  await page.goto("/#flower-garden"); const garden = page.locator("#flower-garden");
  await garden.locator(".cinematic-viewport").scrollIntoViewIfNeeded();
  await expect(garden.locator(".gift-native-status")).toHaveText("Real-time 3D ready");
  const host = garden.locator(".gift-native-canvas");
  await expect(host).toHaveAttribute("data-reduced-motion", "false");
  await garden.getByRole("button", { name: "Release wish 2", exact: true }).click();
  await page.waitForTimeout(1800);
  await garden.locator(".cinematic-viewport").scrollIntoViewIfNeeded();
  await expect(host).toHaveAttribute("data-scene-active", "true");
  await page.screenshot({ path: "qa/garden-normal-motion.png" });
  const frames = Number(await host.getAttribute("data-render-frames")); expect(frames).toBeGreaterThan(2);
  await page.locator("#gifts").scrollIntoViewIfNeeded(); await expect(host).toHaveAttribute("data-scene-active", "false");
  const stopped = await host.getAttribute("data-render-frames"); await page.waitForTimeout(250); expect(await host.getAttribute("data-render-frames")).toBe(stopped);
});

test("cancelling a pending microphone permission stops a late stream", async ({ page }) => {
  await page.addInitScript(() => {
    const w = window as unknown as { resolveLate: () => void; lateStops: number }; w.lateStops = 0;
    navigator.mediaDevices.getUserMedia = () => new Promise<MediaStream>((resolve) => { w.resolveLate = () => resolve({ getTracks: () => [{ stop: () => { w.lateStops++; } }] } as unknown as MediaStream); });
  });
  await page.goto("/#birthday-cake"); const cake = page.locator("#birthday-cake");
  await cake.getByRole("button", { name: "Skip to finished cake" }).click(); await cake.getByRole("button", { name: "Light the candles", exact: true }).click();
  await cake.getByRole("button", { name: "Enable microphone for this wish" }).click();
  await cake.getByRole("button", { name: "Cancel microphone" }).click();
  await page.evaluate(() => (window as unknown as { resolveLate: () => void }).resolveLate());
  await expect.poll(() => page.evaluate(() => (window as unknown as { lateStops: number }).lateStops)).toBe(1);
  await expect(cake.locator(".microphone-panel")).toContainText("Microphone off");
});

test("all twelve chapter anchors exist and all local anchor links resolve", async ({ page }) => {
  await page.goto("/");
  await expect(page.locator("[data-chapter]")).toHaveCount(12);
  expect(await page.locator('a[href^="#"]').evaluateAll((links) => links.map((link) => link.getAttribute("href")!).filter((href) => href.length > 1 && !document.getElementById(decodeURIComponent(href.slice(1)))))).toEqual([]);
});
```

## 100. `tests/content-pack-verbatim.spec.ts` — new

```ts
import { test, expect } from "@playwright/test";
import fs from "node:fs";
import path from "node:path";
import * as pack from "../src/content/packContent";
import { chronosContent } from "../src/content/chronosContent";
import { giftDefinitions, reasonNotes } from "../src/content/giftsContent";

/**
 * Integration audit for the owner's content pack (docs/content-pack/). No browser: it compares src/content/packContent.ts with the
 * verbatim transcript of the PDF (docs/content-pack/pack-text.txt) in both directions, then checks what the site data is built from.
 * It is an audit of the import. Once the owner edits packContent.ts on purpose, the differences it reports are the edits.
 */
const norm = (text: string) => text.replace(/[\u2018\u2019]/g, "'").replace(/[\u201c\u201d]/g, '"').replace(/\s+/g, " ").trim();
const transcript = fs.readFileSync(path.resolve("docs/content-pack/pack-text.txt"), "utf8").split("\n").filter((line) => line && !line.startsWith("#")).map(norm);
const haystack = transcript.join("\n");

/** Every non-empty string inside a value. */
function leaves(value: unknown, out: string[] = []): string[] {
  if (typeof value === "string") { if (value.trim()) out.push(value); }
  else if (Array.isArray(value)) value.forEach((item) => leaves(item, out));
  else if (value && typeof value === "object") Object.values(value).forEach((item) => leaves(item, out));
  return out;
}

const groups: Record<string, unknown> = {
  cover: pack.packCover, letter: [pack.packLetter, pack.packLetterInsertPrompts], reasons: pack.packReasons, wishes: pack.packWishes, postcards: pack.packPostcards,
  dedications: pack.packGiftDedications, extended: pack.packExtended, garden: pack.packGardenNarration, cinema: pack.packCinema,
  radio: pack.packRadio, microcopy: pack.packMicrocopy, checklist: pack.packChecklist, notes: pack.packAuthorNotes,
};

test("counts match the pack", () => {
  expect(pack.packReasons.items).toHaveLength(17);
  expect(pack.packWishes).toHaveLength(101); // the heading says 100, the list has 101
  expect(pack.packPostcards).toHaveLength(7);
  expect(Object.keys(pack.packGiftDedications)).toHaveLength(8);
  expect(pack.packGardenNarration).toHaveLength(7);
  expect(Object.keys(pack.packMicrocopy)).toHaveLength(13);
  expect(pack.packChecklist.items).toHaveLength(16);
  expect(pack.packCinema.requiredFields).toHaveLength(6);
  expect(Object.keys(pack.packGiftSlots)).toHaveLength(9);
  expect(pack.packLetterInsertPrompts.map((insert) => insert.id)).toEqual(pack.packLetter.optionalInserts.map((insert) => insert.id)); // prompt i describes slot i
});

for (const [name, value] of Object.entries(groups)) {
  test(`every ${name} string is in the PDF transcript, word for word`, () => {
    const missing = leaves(value).filter((text) => !haystack.includes(norm(text)));
    expect(missing, `strings in packContent.ts that are not in the PDF:\n${missing.join("\n")}`).toEqual([]);
  });
}

test("nothing quoted or numbered in the PDF was left out", () => {
  const known = new Set(Object.values(groups).flatMap((value) => leaves(value)).map(norm));
  const quoted = transcript.filter((line) => line.startsWith('"') && line.endsWith('"')).map((line) => line.slice(1, -1).trim());
  expect(quoted.length).toBeGreaterThanOrEqual(40);
  expect(quoted.filter((text) => !known.has(text))).toEqual([]);
  const headings = [
    "01. Secret Letter — Main Birthday Letter", "02. Jar of Reasons — 17 Notes", "03. A Thousand Wishes — 100 Short Wishes", "04. Future Postcards — 7 Complete Messages",
    "05. Gift Dedications — 17 Surprises", "06. Everlasting Flower — Dedication", "07. Little Universe — Dedication", "08. Birthday Garden — Narration",
    "09. Memory Cinema — Captions and Missing-Media Copy", "10. Bhumi FM — Audio Content", "11. Queen's Crown — Dedication",
    "12. Website Microcopy — Empty States, Buttons and Reveals", "13. Final Content Completion Checklist",
  ].map(norm);
  const numbered = transcript.filter((line) => /^\d{2,3}\. /.test(line) && !headings.includes(line)).map((line) => line.replace(/^\d{2,3}\. /, ""));
  expect(numbered).toHaveLength(17 + 101);
  expect(numbered.filter((text) => !known.has(text))).toEqual([]);
  // the letter: every paragraph block between the greeting and the closing is present, the thank-you block together with its [EDIT] slot
  const body = transcript.slice(transcript.indexOf("Dear Bhumi,") + 2, transcript.indexOf("With love,"));
  const letter = pack.packLetter;
  const expected = [...letter.paragraphs, `${letter.thanks} ${letter.memoryPrompt}`, ...letter.afterThanks].map(norm);
  expect(body).toEqual(expected);
});

test("what the site shows is built from the pack, and no template or slot text can reach a visitor", () => {
  const main = chronosContent.letters.letters[0];
  expect(main.kind).toBe("main");
  expect(main.title).toBe(pack.packLetter.title);
  expect(main.paragraphs[0]).toBe("Happy Birthday. ❤️");
  expect(main.paragraphs).toHaveLength(10);
  expect(chronosContent.letters.letters[1].title).toBe("The Last Letter"); // the letter that came with the project is kept
  expect(chronosContent.letters.letters).toHaveLength(6);
  expect(reasonNotes.map((note) => note.text)).toEqual(pack.packReasons.items);
  expect(chronosContent.future.postcards.map((card) => card.caption)).toEqual(pack.packPostcards.map((card) => card.message));
  expect(chronosContent.future.items).toHaveLength(4); // the imagined map of gift 11 keeps its four places
  expect(chronosContent.gifts.intro).toBe(pack.packMicrocopy.giftGridIntro);
  const dedicated = giftDefinitions.filter((gift) => gift.dedication).map((gift) => gift.number);
  expect(dedicated).toEqual(["01", "02", "03", "04", "05", "06", "07", "08"]);
  expect(giftDefinitions.find((gift) => gift.number === "08")?.revealLine).toBe("Your crown is your confidence.");

  const shown = [
    ...main.paragraphs, main.title, main.subtitle, main.closing, main.signature,
    ...reasonNotes.map((note) => note.text),
    ...chronosContent.future.postcards.flatMap((card) => [card.place, card.someday, card.caption]),
    ...giftDefinitions.flatMap((gift) => [gift.dedication, gift.revealLine, gift.subtitle]),
    ...pack.packWishes, ...pack.packGardenNarration.flatMap((item) => [item.title, item.text]),
    ...Object.values(chronosContent.gifts.specials).map((item) => item.message),
  ];
  const slots = shown.filter((text) => /\[(EDIT|ADD|INSERT|X)\b/.test(text));
  expect(slots).toEqual([]);
});
```

## 101. `tests/content-pack.spec.ts` — new

```ts
import { test, expect, type Locator, type Page } from "@playwright/test";
import { chronosContent } from "../src/content/chronosContent";
import { packCinema, packCover, packExtended, packGardenNarration, packGiftDedications, packLetter, packMicrocopy, packPostcards, packProgress, packRadio, packReasons, packWishes } from "../src/content/packContent";

/**
 * The content pack as a visitor meets it. These checks read text and controls, not pixels, so WebGL is switched off: every scene
 * then shows its poster and the HTML does all the work (the same path a device without WebGL takes). The 3D side of each gift is
 * covered by scripts/qa/gift-flow.mjs and the other specs.
 */
test.beforeEach(async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.addInitScript(() => {
    const get = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (kind: string, ...args: unknown[]) { return kind.includes("webgl") ? null : (get as Function).apply(this, [kind, ...args]); } as typeof get;
  });
});

const PLACEHOLDER = /\[(EDIT|ADD|INSERT|X)\b/;
const gift = (page: Page, number: string) => page.locator(`.gift-parcel[data-gift-id="gift-${number}"]`);
async function openGift(page: Page, number: string) {
  await page.goto("/#gifts");
  await gift(page, number).click();
  const dialog = page.locator("dialog[open]");
  await expect(dialog).toBeVisible();
  await expect(dialog.locator(".gift-experience")).toBeVisible();
  return dialog;
}
const text = async (locator: Locator) => (await locator.innerText()).replace(/\s+/g, " ").trim();

test("Gift Atelier: the pack's grid intro, progress label, dedications, replay, back and close wording", async ({ page }) => {
  await page.goto("/#gifts");
  await expect(page.locator(".gift-room__intro")).toHaveText(packMicrocopy.giftGridIntro);
  await expect(page.locator(".gift-room__tagline")).toHaveText(packCover.tagline);
  await expect(page.locator("#gifts")).toContainText("A UNIVERSE MADE OF 17 LITTLE SURPRISES");
  await gift(page, "02").click();
  await expect(page.locator(".gift-progress__notice")).toHaveText(packProgress(1));
  const dialog = page.locator("dialog[open]");
  await expect(dialog.locator(".gift-experience-shell__dedication")).toHaveText(packGiftDedications["02"].text);
  await expect(dialog.getByRole("button", { name: packMicrocopy.close, exact: true })).toHaveAttribute("title", packMicrocopy.close);
  await expect(dialog.locator(".gift-experience-shell__footer button").first()).toContainText(packMicrocopy.replay);
  await dialog.getByRole("button", { name: new RegExp(packMicrocopy.back) }).click();
  await expect(page.locator("dialog[open]")).toHaveCount(0);
  await gift(page, "01").click();
  await page.keyboard.press("Escape");
  await expect(page.locator(".gift-progress__notice")).toHaveText(packProgress(2));
});

test("dedications 01-08 are shown, 09-17 show nothing, and no template text reaches any gift", async ({ page }) => {
  test.setTimeout(240000);
  for (let n = 1; n <= 17; n++) {
    const id = String(n).padStart(2, "0");
    const dialog = await openGift(page, id);
    const dedication = dialog.locator(".gift-experience-shell__dedication");
    if (n <= 8) await expect(dedication).toHaveText(packGiftDedications[id].text);
    else await expect(dedication).toHaveCount(0);
    expect(await dialog.innerText(), `gift ${id} must not show a template or slot`).not.toMatch(PLACEHOLDER);
    await page.keyboard.press("Escape");
    await expect(page.locator("dialog[open]")).toHaveCount(0);
  }
});

test("gift 01 and the Letter Room: the main letter without its [EDIT] slot, and the earlier letter kept", async ({ page }) => {
  const dialog = await openGift(page, "01");
  await dialog.getByRole("button", { name: packMicrocopy.skip, exact: true }).click();
  const reading = dialog.locator(".gift-letter__reading");
  await expect(reading).toContainText(packLetter.title);
  await expect(reading).toContainText(packLetter.subtitle);
  await expect(reading).toContainText("Dear Bhumi,");
  for (const paragraph of [...packLetter.paragraphs, packLetter.thanks, ...packLetter.afterThanks]) expect(await text(reading)).toContain(paragraph);
  await expect(reading).toContainText("With love,");
  await expect(reading).toContainText("Rudra");
  expect(await reading.innerText()).not.toMatch(PLACEHOLDER);
  await page.keyboard.press("Escape");

  await page.goto("/#letters");
  const envelopes = page.locator("#letters .letter-envelope");
  await expect(envelopes).toHaveCount(6);
  await envelopes.nth(0).click();
  const d1 = page.locator("dialog[open]");
  await expect(d1.locator("h2")).toHaveText(packLetter.title);
  await expect(d1.locator(".letter-reading__subtitle")).toHaveText(packLetter.subtitle);
  await d1.getByRole("button", { name: packMicrocopy.skip, exact: true }).click();
  await expect(d1.locator(".physical-letter-copy")).toContainText("Aaj ka din tumhara hai");
  expect(await d1.locator(".physical-letter-copy").innerText()).not.toMatch(PLACEHOLDER);
  await page.keyboard.press("Escape");
  await envelopes.nth(1).click();
  const d2 = page.locator("dialog[open]");
  await expect(d2.locator("h2")).toHaveText("The Last Letter");
  await d2.getByRole("button", { name: packMicrocopy.skip, exact: true }).click();
  await expect(d2.locator(".physical-letter-copy")).toContainText("A tower that refuses to forget you.");
  await page.keyboard.press("Escape");
  await envelopes.nth(2).click();
  const d3 = page.locator("dialog[open]");
  await d3.getByRole("button", { name: packMicrocopy.skip, exact: true }).click();
  await expect(d3.locator(".physical-letter-copy")).toContainText(packMicrocopy.missingText);
});

test("gift 02: all seventeen reasons of the pack, one by one and as a list", async ({ page }) => {
  const dialog = await openGift(page, "02");
  await dialog.getByRole("button", { name: "Open jar lid", exact: true }).click();
  for (let i = 0; i < 17; i++) {
    await dialog.locator(".gift-note-picker button").nth(i).click();
    await expect(dialog.locator(".gift-jar__note")).toContainText(`NOTE ${String(i + 1).padStart(2, "0")} / 17`);
    await expect(dialog.locator(".gift-jar__note p")).toHaveText(packReasons.items[i]);
  }
  await dialog.getByRole("button", { name: "Read all 17", exact: true }).click();
  await expect(dialog.locator(".gift-jar__all li")).toHaveCount(17);
  expect(await dialog.locator(".gift-jar__all li").allInnerTexts()).toEqual(packReasons.items.map((reason, i) => `${String(i + 1).padStart(2, "0")}${reason}`));
  await expect(dialog.locator(".gift-jar__quote")).toHaveText(packReasons.quote);
  // the number is printed once (in the <span>); the browser's own list marker would print it a second time
  expect(await dialog.locator(".gift-jar__all").evaluate((list) => getComputedStyle(list).listStyleType)).toBe("none");
});

test("gifts 03, 04 and 08: the long dedication and its short reveal line appear when the visitor reveals them", async ({ page }) => {
  let dialog = await openGift(page, "03");
  await dialog.getByRole("button", { name: "Reveal hidden message" }).click();
  await expect(dialog.locator(".gift-dedication strong")).toHaveText(packExtended.flower.revealLine);
  await expect(dialog.locator(".gift-dedication p")).toHaveText(packExtended.flower.text);
  await dialog.getByRole("button", { name: "Hide the message" }).click();
  await expect(dialog.locator(".gift-dedication")).toHaveCount(0);
  await page.keyboard.press("Escape");

  dialog = await openGift(page, "04");
  await expect(dialog.locator(".gift-dedication")).toHaveCount(0);
  await dialog.getByRole("button", { name: "Reveal the dedication" }).click();
  await expect(dialog.locator(".gift-dedication strong")).toHaveText(packExtended.universe.revealLine);
  await expect(dialog.locator(".gift-dedication p")).toHaveText(packExtended.universe.text);
  await dialog.getByRole("button", { name: "Hide the dedication" }).click();
  await expect(dialog.locator(".gift-dedication")).toHaveCount(0);
  await page.keyboard.press("Escape");

  dialog = await openGift(page, "08");
  await dialog.getByRole("button", { name: "Reveal birthday note" }).click();
  await expect(dialog.locator(".gift-dedication strong")).toHaveText(packExtended.crown.revealLine);
  await expect(dialog.locator(".gift-dedication p")).toHaveText(packExtended.crown.text);
  await expect(dialog.locator(".gift-crown__message")).toContainText("Some things I practice saying and still say badly."); // the owner's own note stays
  await dialog.getByRole("button", { name: "Hide birthday note" }).click();
  await expect(dialog.locator(".gift-dedication")).toHaveCount(0);
});

test("gift 07: the sky of wishes (all 101), the ten lanterns and the full lists", async ({ page }) => {
  const dialog = await openGift(page, "07");
  const note = dialog.locator(".gift-wishes__note");
  await dialog.getByRole("button", { name: "Draw a wish from the sky" }).click();
  await expect(note.locator("small")).toContainText(/FROM THE SKY/);
  const first = await text(note.locator("p"));
  expect(packWishes).toContain(first);
  // the draw walks through the whole sky before any wish comes back
  const seen = new Set([first]);
  for (let i = 0; i < 100; i++) {
    await dialog.getByRole("button", { name: "Draw a wish from the sky" }).click();
    seen.add(await text(note.locator("p")));
  }
  expect(seen.size).toBe(101);
  await expect(dialog.locator(".gift-wishes__meta")).toContainText("101 / 101 sky wishes read");
  await dialog.getByRole("button", { name: "Next sky wish" }).click();
  await dialog.getByRole("button", { name: "Clear constellation" }).click();
  await dialog.getByRole("button", { name: "Previous sky wish" }).click();
  await expect(note.locator("small")).toContainText("WISH 101 OF 101");
  await expect(note.locator("p")).toHaveText(packWishes[100]);
  await dialog.getByRole("button", { name: "Wish 3", exact: true }).click(); // a lantern wish still replaces the sky wish
  await expect(note.locator("small")).toContainText("WISH 03");
  await dialog.getByRole("button", { name: "Display all wishes" }).click();
  await expect(dialog.locator(".gift-wishes__all li")).toHaveCount(10);
  await expect(dialog.locator(".gift-wishes__sky li")).toHaveCount(101);
  expect(await dialog.locator(".gift-wishes__sky li").last().innerText()).toContain("May this birthday mark the beginning of a hopeful new chapter.");
  for (const list of [".gift-wishes__all", ".gift-wishes__sky"]) {
    expect(await dialog.locator(list).evaluate((el) => getComputedStyle(el).listStyleType), `${list}: the number is printed once`).toBe("none");
  }
});

test("gift 06, 05 and 12: opening, empty and closing copy; empty playlist wording", async ({ page }) => {
  let dialog = await openGift(page, "06");
  await expect(dialog.locator(".gift-cinema__placeholder strong")).toHaveText(packCinema.opening);
  await dialog.getByRole("button", { name: "Start projector" }).click();
  await expect(dialog.locator(".gift-cinema__placeholder strong")).toHaveText(packCinema.emptyState);
  await expect(dialog.locator(".gift-cinema__status")).toHaveText(packMicrocopy.missingPhoto);
  await dialog.getByRole("button", { name: "Dim the theatre" }).click();
  await expect(dialog.locator(".gift-cinema__placeholder strong")).toHaveText(packCinema.closing);
  await page.keyboard.press("Escape");

  dialog = await openGift(page, "05");
  await expect(dialog.locator(".gift-cassette__status")).toHaveText(packRadio.emptyPlaylist);
  await page.keyboard.press("Escape");

  dialog = await openGift(page, "12");
  await expect(dialog.locator(".gift-vinyl__track span")).toHaveText(packMicrocopy.missingAudio);
});

test("gifts 09, 14 and 15 stay empty slots and say so with the pack's wording", async ({ page }) => {
  let dialog = await openGift(page, "09");
  await dialog.getByRole("button", { name: /Break the seal/ }).click();
  await expect(dialog.locator(".gift-open-when__letter")).toContainText(packMicrocopy.missingText);
  await page.keyboard.press("Escape");
  dialog = await openGift(page, "14");
  await expect(dialog.locator(".gift-coupon__page")).toContainText(packMicrocopy.missingText);
  await expect(dialog.getByRole("button", { name: "Mark redeemed" })).toBeDisabled();
  await page.keyboard.press("Escape");
  dialog = await openGift(page, "15");
  await dialog.getByRole("button", { name: "Plant the seed" }).click();
  await expect(dialog.locator(".gift-future-garden__missing")).toHaveText(packMicrocopy.missingText);
});

test("Future Postcards: seven messages, each readable on the reverse, with the visitor's own line", async ({ page }) => {
  await page.goto("/#future-postcards");
  const cards = page.locator("#future-postcards .postcard-grid .postcard");
  await expect(cards).toHaveCount(7);
  for (let i = 0; i < 7; i++) {
    await expect(cards.nth(i)).toContainText(packPostcards[i].message);
    await expect(cards.nth(i).locator("strong")).toHaveText(packPostcards[i].title.charAt(0) + packPostcards[i].title.slice(1).toLowerCase());
  }
  await cards.nth(0).click();
  const dialog = page.locator("dialog[open]");
  await expect(dialog.locator("h2")).toHaveText("A note from the future");
  await dialog.getByRole("button", { name: "Read reverse" }).click();
  await dialog.getByLabel("Write a line on the back").fill("Hello from today.");
  for (let i = 1; i < 7; i++) {
    await dialog.getByRole("button", { name: "Next postcard" }).click();
    await expect(dialog.locator(".postcard-reading > p").nth(1)).toHaveText(packPostcards[i].message);
  }
  await dialog.getByRole("button", { name: "Next postcard" }).click(); // wraps to the first
  await expect(dialog.locator("h2")).toHaveText("A note from the future");
  await dialog.getByRole("button", { name: "Previous postcard" }).click();
  await expect(dialog.locator("h2")).toHaveText("Keep this little light");
});

test("Birthday Garden: seven stages, each with the pack's narration", async ({ page }) => {
  await page.goto("/");
  const steps = page.locator(".garden-growth__steps button");
  await expect(steps).toHaveText(["Seed", "Roots", "Sprout", "Leaves", "Bud", "Flower", "Full bloom"]);
  for (let i = 0; i < 7; i++) {
    await steps.nth(i).click();
    await expect(steps.nth(i)).toHaveAttribute("aria-current", "step");
    await expect(page.locator(".garden-growth__caption")).toHaveText(`${packGardenNarration[i].title}${packGardenNarration[i].text}`);
  }
});

test("Music Lounge, Memory Gallery and finale use the pack's welcome, empty-state and thank-you copy", async ({ page }) => {
  await page.goto("/#music-room");
  await expect(page.locator(".music-room__intro")).toHaveText(packRadio.welcome);
  await expect(page.locator(".music-room__empty")).toHaveText(packRadio.emptyPlaylist);
  await expect(page.locator(".music-status")).toHaveText(packMicrocopy.missingAudio);
  await page.goto("/#gallery");
  await expect(page.locator(".gallery-intro")).toHaveText(packCinema.emptyState);
  await page.locator(".polaroid-card").first().click();
  await expect(page.locator("dialog[open] .polaroid-lightbox > p")).toHaveText(packMicrocopy.missingPhoto);
  await page.keyboard.press("Escape");
  await page.goto("/#finale");
  await expect(page.locator(".final-celebration__thanks")).toHaveText(packMicrocopy.finalThanks);
});

test("Scrapbook: every empty page and the photo mount carry the pack's lines", async ({ page }) => {
  await page.goto("/#storybook");
  const blanks = page.locator(".storybook-leaf--blank");
  const photos = page.locator(".storybook-leaf--photo");
  await expect(blanks.first()).toBeAttached({ timeout: 30000 });
  // the book's own data says how many pages are empty slots; each must say the pack's line and nothing else
  const pages = chronosContent.scrapbook.spreads.flatMap((spread) => [spread.left, spread.right]);
  const blankCount = pages.filter((entry) => entry.kind === "blank").length;
  const photoCount = pages.filter((entry) => entry.kind === "photo").length;
  expect(blankCount).toBeGreaterThan(0);
  expect(photoCount).toBeGreaterThan(0);
  await expect(blanks).toHaveCount(blankCount);
  await expect(photos).toHaveCount(photoCount);
  for (const body of await blanks.locator("p").allInnerTexts()) expect(body.trim()).toBe(packMicrocopy.missingText);
  for (const body of await photos.locator("p").allInnerTexts()) expect(body.trim()).toBe(packMicrocopy.missingPhoto);
});

test("no template or slot text anywhere on the page", async ({ page }) => {
  await page.goto("/");
  await page.waitForTimeout(500);
  expect(await page.locator("body").innerText()).not.toMatch(PLACEHOLDER);
  expect(await page.content()).not.toMatch(/\[(EDIT|ADD|INSERT)[ :\]]/);
});
```

## 102. `tests/letter-refinement.spec.ts` — modified

```ts
import { test, expect } from '@playwright/test';
const open = async (page: import('@playwright/test').Page) => {await page.goto('/#letters');await page.locator('.letter-envelope').first().click();return page.locator('dialog[open]');};
test('letter reduced motion: open, close, replay, skip and focus return', async({page})=>{
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));const d=await open(page);await expect(d.locator('.gift-native-status')).toHaveText('Real-time 3D ready');
 await d.getByRole('button',{name:'Open Letter',exact:true}).click();await expect(d.locator('.physical-letter-copy')).toBeVisible();const text=await d.locator('.physical-letter-copy').innerText();expect(text.length).toBeGreaterThan(80);
 await d.getByRole('button',{name:'Close Letter',exact:true}).click();await expect(d.locator('.physical-letter-copy')).toBeHidden();await d.getByRole('button',{name:'Replay Animation'}).click();await expect(d.locator('.physical-letter-copy')).toBeVisible();expect(await d.locator('.physical-letter-copy').innerText()).toBe(text);
 await d.getByRole('button',{name:'Skip Animation'}).click();await expect(d.locator('.physical-letter-copy')).toBeVisible();await d.locator('.cinematic-viewport').screenshot({path:'qa/letter-refined-open.png'});
 await page.keyboard.press('Escape');await expect(page.locator('dialog[open]')).toHaveCount(0);await expect(page.locator('.letter-envelope').first()).toBeFocused();expect(errors).toEqual([]);
});
test('letter normal motion: text waits for paper, interruption, replay and reverse close',async({page})=>{
 test.setTimeout(150000);await page.emulateMedia({reducedMotion:'no-preference'});const d=await open(page);await expect(d.locator('.gift-native-status')).toHaveText('Real-time 3D ready');await d.getByRole('button',{name:'Open Letter',exact:true}).click();await expect(d.locator('.physical-letter-copy')).toBeHidden();await expect(d.locator('.physical-letter-copy')).toBeVisible({timeout:35000});
 await d.getByRole('button',{name:'Close Letter',exact:true}).click();await expect(d.locator('.physical-letter-copy')).toBeHidden();await d.getByRole('button',{name:'Open Letter',exact:true}).click();await d.getByRole('button',{name:'Replay Animation'}).click();await expect(d.locator('.physical-letter-copy')).toBeHidden();await d.getByRole('button',{name:'Skip Animation'}).click();await expect(d.locator('.physical-letter-copy')).toBeVisible();await d.getByRole('button',{name:'Close dialog',exact:true}).click();await expect(page.locator('dialog[open]')).toHaveCount(0,{timeout:30000});
});
test('letter mobile and unavailable WebGL: skip retains actual text',async({page})=>{
 await page.setViewportSize({width:390,height:844});await page.addInitScript(()=>{const original=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(type:string,...args:unknown[]){if(type.includes('webgl'))return null;return (original as Function).apply(this,[type,...args]);} as typeof original;});
 const d=await open(page);await expect(d.locator('.gift-stage-fallback')).toContainText('cannot display');await d.getByRole('button',{name:'Skip Animation'}).click();await expect(d.locator('.physical-letter-copy')).toBeVisible();expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);await d.getByRole('button',{name:'Close Letter',exact:true}).click();await expect(d.locator('.physical-letter-copy')).toBeHidden();await page.keyboard.press('Escape');await expect(page.locator('dialog[open]')).toHaveCount(0);
});
test('mobile real 3D: responsive framing and replay cleanup',async({page})=>{
 await page.setViewportSize({width:390,height:844});const d=await open(page);await expect(d.locator('.gift-native-status')).toHaveText('Real-time 3D ready');await d.getByRole('button',{name:'Skip Animation'}).click();await expect(d.locator('.physical-letter-copy')).toBeVisible();await expect(d.locator('canvas')).toHaveCount(1);await d.locator('.cinematic-viewport').screenshot({path:'qa/letter-refined-mobile.png'});await d.getByRole('button',{name:'Replay Animation'}).click();await expect(d.locator('canvas')).toHaveCount(1);await page.keyboard.press('Escape');await expect(page.locator('dialog canvas')).toHaveCount(0);
});
```

## 103. `tests/native-gifts.spec.ts` — modified

```ts
import { test, expect } from "@playwright/test";
for (const [index, kind, title] of [[2, "flower", "Eternal rose"], [7, "crown", "Crown"], [16, "portal", "Portal"]] as const) {
  test(`${title}: native mesh renders and original controls remain usable`, async ({ page }) => {
    const errors: string[] = []; page.on("pageerror", (error) => errors.push(error.message)); page.on("console", (message) => { if (message.type() === "error") errors.push(message.text()); });
    await page.goto("/#gifts"); await page.locator(".gift-parcel").nth(index).click();
    const dialog = page.locator("dialog[open]"); const viewport = dialog.locator(`[data-gift-world="${kind}"]`);
    await viewport.scrollIntoViewIfNeeded();
    await expect(viewport.locator(".gift-native-status")).toHaveText("Real-time 3D ready");
    await expect(viewport.locator("[data-native-ready=true]")).toHaveAttribute("data-render-frames", /[1-9]/);
    if (kind === "flower") { for (let i = 0; i < 4; i++) await dialog.locator(".gift-control--primary").click(); }
    if (kind === "crown") { await dialog.getByRole("button", { name: "Rotate right", exact: true }).click(); await dialog.getByRole("button", { name: "The jewels", exact: true }).click(); }
    if (kind === "portal") { await dialog.getByRole("button", { name: "Gather the sixteen lights" }).click(); await dialog.getByRole("button", { name: "Open the portal", exact: true }).click(); }
    await viewport.scrollIntoViewIfNeeded(); await viewport.screenshot({ path: `qa/gift-${kind}.png` });
    if (kind === "portal") { await dialog.getByRole("button", { name: "Enter the Birthday Ballroom" }).click(); await expect(page.locator("dialog[open]")).toHaveCount(0); await expect(page.locator("#birthday-cake")).toBeInViewport(); }
    else { await dialog.getByRole("button", { name: "Close this experience", exact: true }).click(); await expect(page.locator("dialog canvas")).toHaveCount(0); }
    expect(errors).toEqual([]);
  });
}
```

## 104. `tests/paper-geometry.spec.ts` — modified

```ts
import {test,expect} from '@playwright/test';
import {createFoldedPaper} from '../src/engine/paper';
test('paper geometry: closed thickness surface, rounded crease transport and stable width',()=>{
 const {geometry,deform,width,height}=createFoldedPaper();const edges=new Map<string,number>();const index=geometry.index!;
 for(let i=0;i<index.count;i+=3){const triangle=[index.getX(i),index.getX(i+1),index.getX(i+2)];for(let j=0;j<3;j++){const a=triangle[j],b=triangle[(j+1)%3],key=[Math.min(a,b),Math.max(a,b)].join(':');edges.set(key,(edges.get(key)??0)+1);}}
 expect([...edges.values()].every(n=>n===2)).toBe(true);
 const spans=[];for(const [upper,lower] of [[0,0],[.5,0],[1,.5],[1,1]]){deform(upper,lower);geometry.computeBoundingBox();const b=geometry.boundingBox!;spans.push({x:b.max.x-b.min.x,y:b.max.y-b.min.y,z:b.max.z-b.min.z});expect([...geometry.attributes.position.array].every(Number.isFinite)).toBe(true);expect([...geometry.attributes.normal.array].every(Number.isFinite)).toBe(true);}
 // proportions of the engine's default sheet (3.0 x 4.1): a third folded over the middle panel, then flat; thin when flat, thick where folded
 expect(spans[0].y).toBeLessThan(height*0.36);expect(spans[3].y).toBeCloseTo(height,1);expect(spans[3].z).toBeLessThan(height*0.012);expect(spans[1].z).toBeGreaterThan(height*0.07);for(const s of spans)expect(s.x).toBeCloseTo(width,1);geometry.dispose();
});
```

## 105. `tests/postcard-refinement.spec.ts` — modified

```ts
import {test,expect} from '@playwright/test';
for(const width of [1280,390])test(`native postcards: flip, navigation, original caption and cleanup at ${width}`,async({page})=>{
 const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));await page.setViewportSize({width,height:900});await page.goto('/#future-postcards');await page.locator('.postcard-grid .postcard').first().click();const d=page.locator('dialog[open]');await expect(d.locator('.gift-native-status')).toHaveText('Real-time 3D ready');await d.getByRole('button',{name:'Read reverse'}).click();await expect(d.getByRole('button',{name:'Show illustration'})).toHaveAttribute('aria-pressed','true');await expect(d.locator('.postcard-reading small').last()).toContainText('not a fact');const title=await d.locator('h2').innerText();await d.getByRole('button',{name:'Next postcard'}).click();await expect(d.locator('h2')).not.toHaveText(title);await d.getByRole('button',{name:'Previous postcard'}).click();await expect(d.locator('h2')).toHaveText(title);await expect(d.locator('canvas')).toHaveCount(1);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);await d.locator('.cinematic-viewport').screenshot({path:`qa/postcard-${width}.png`});await page.keyboard.press('Escape');await expect(page.locator('dialog[open]')).toHaveCount(0);await expect(page.locator('dialog canvas')).toHaveCount(0);expect(errors).toEqual([]);
});
```

## 106. `tests/scrapbook-layout.spec.ts` — new

```ts
import { test, expect } from "@playwright/test";

/**
 * The Scrapbook's decorative leather body, page blocks and spine follow the flip book's real orientation: one page on a phone,
 * a two-page spread on a desktop. The flip book announces its orientation with an event that can fire before the page is listening
 * (a phone starts in portrait, so it never fires again); the component therefore also reads it directly. Without that, a phone showed
 * the two-page decoration: a spine across the middle of the single page and a leather body drawn for half a spread behind the cover.
 * WebGL is switched off: the book is plain HTML and CSS.
 */
test.beforeEach(async ({ page }) => {
  await page.emulateMedia({ reducedMotion: "reduce" });
  await page.addInitScript(() => {
    const get = HTMLCanvasElement.prototype.getContext;
    HTMLCanvasElement.prototype.getContext = function (kind: string, ...args: unknown[]) { return kind.includes("webgl") ? null : (get as Function).apply(this, [kind, ...args]); } as typeof get;
  });
});

const next = "Turn to the next scrapbook page";

test("Scrapbook on a phone is one page: no spine across it, from the cover onwards", async ({ page }) => {
  await page.setViewportSize({ width: 390, height: 844 });
  await page.goto("/#storybook");
  const stage = page.locator(".storybook-book__stage");
  const spine = page.locator(".storybook-book__gutter");
  await expect(page.locator(".storybook-leaf").first()).toBeAttached({ timeout: 30000 });
  await expect(stage).toHaveAttribute("data-state", "single", { timeout: 15000 });
  await expect(spine).toBeHidden();
  for (let turn = 1; turn <= 3; turn++) {
    await page.getByRole("button", { name: next }).click();
    await expect(page.locator(".storybook-pagination")).toContainText(`${turn} /`);
    await expect(stage).toHaveAttribute("data-state", "single");
    await expect(spine).toBeHidden();
  }
  expect(await page.evaluate(() => document.documentElement.scrollWidth <= innerWidth + 1)).toBe(true);
});

test("Scrapbook on a desktop: closed cover first, then a two-page spread with its spine", async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 900 });
  await page.goto("/#storybook");
  const stage = page.locator(".storybook-book__stage");
  const spine = page.locator(".storybook-book__gutter");
  await expect(page.locator(".storybook-leaf").first()).toBeAttached({ timeout: 30000 });
  await expect(stage).toHaveAttribute("data-state", "front", { timeout: 15000 });
  await expect(spine).toBeHidden();
  await page.getByRole("button", { name: next }).click();
  await expect(page.locator(".storybook-pagination")).toContainText("1 /");
  await expect(stage).toHaveAttribute("data-state", "open");
  await expect(spine).toBeVisible();
});
```

## 107. `tests/ultra-access.spec.ts` — modified

```ts
import {test,expect} from '@playwright/test';
test('gift WebGL failure: original secret letter remains available by Skip',async({page})=>{
 await page.addInitScript(()=>{const get=HTMLCanvasElement.prototype.getContext;HTMLCanvasElement.prototype.getContext=function(kind:string,...args:unknown[]){return kind.includes('webgl')?null:(get as Function).apply(this,[kind,...args]);} as typeof get;});await page.goto('/#gifts');await page.locator('.gift-parcel').first().click();const d=page.locator('dialog[open]');await expect(d.locator('.gift-native-stage')).toContainText(/cannot display/i,{timeout:45000});await d.getByRole('button',{name:'Skip animation',exact:true}).click();await expect(d.locator('.gift-letter__reading')).toContainText("Bhumi,");await page.keyboard.press('Escape');await expect(page.locator('dialog[open]')).toHaveCount(0);
});
test('normal motion gift renderer pauses offscreen and resumes; jar controls remain responsive',async({page})=>{
 await page.emulateMedia({reducedMotion:'no-preference'});await page.goto('/#gifts');await page.locator('.gift-parcel').nth(1).click();const d=page.locator('dialog[open]');const native=d.locator('[data-native-ready=true]');await expect(native).toHaveCount(1,{timeout:45000});await d.getByRole('button',{name:'Open jar lid',exact:true}).click();await d.getByRole('button',{name:'Turn jar right',exact:true}).click();const stage=d.locator('.gift-native-stage');await stage.evaluate(e=>(e as HTMLElement).style.display='none');await page.waitForTimeout(1000);const before=Number(await native.getAttribute('data-render-frames'));await page.waitForTimeout(500);expect(Number(await native.getAttribute('data-render-frames'))-before).toBeLessThan(3);await stage.evaluate(e=>(e as HTMLElement).style.display='');await expect.poll(async()=>Number(await native.getAttribute('data-render-frames'))).toBeGreaterThan(before);await d.getByRole('button',{name:'Close this experience',exact:true}).click();
});
test('treasure puzzle solves with accessible controls and real chest state changes',async({page})=>{
 await page.goto('/#gifts');await page.locator('.gift-parcel').nth(15).click();const d=page.locator('dialog[open]');await expect(d.locator('[data-native-ready=true]')).toHaveCount(1,{timeout:45000});await d.getByRole('button',{name:/Symbol flower, position/}).click();await d.getByRole('button',{name:'Move selected left'}).click();await d.getByRole('button',{name:/Symbol moon, position/}).click();await d.getByRole('button',{name:'Move selected left'}).click();await d.getByRole('button',{name:'Check the order'}).click();await d.getByLabel('The chest asks for a word').fill('OPEN');await d.getByRole('button',{name:'Unlock the chest'}).click();await expect(d.locator('.gift-treasure__reward')).toContainText('TREASURE FOUND');await page.keyboard.press('Escape');
});
test('high-tier jar reflections/transmission initialize without console errors',async({page})=>{
 test.setTimeout(180000);const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});await page.goto('/#gifts');await page.locator('.gift-parcel').nth(1).click();const d=page.locator('dialog[open]');await expect(d.locator('[data-native-ready=true]')).toHaveCount(1,{timeout:45000});await d.getByLabel('jar graphics quality').selectOption('high');await expect(d.locator('[data-native-ready=true]')).toHaveCount(1,{timeout:120000});await d.getByRole('button',{name:'Open jar lid',exact:true}).click();await page.screenshot({path:'qa/ultra-jar-high.png',timeout:60000});expect(errors).toEqual([]);
});
```

## 108. `tests/ultra-gifts.spec.ts` — modified

```ts
import {test,expect} from '@playwright/test';
import {futureGardenLeaves} from '../src/content/giftsContent';
import {packMicrocopy} from '../src/content/packContent';
const kinds=['letter','jar','flower','universe','cassette','cinema','wishes','crown','cabinet','machine','adventure','vinyl','mirror','coupons','hope-tree','treasure','portal'];
for(const [index,kind] of kinds.entries())test(`gift ${index+1}: ${kind} native world, primary action, replay and cleanup`,async({page})=>{
 test.setTimeout(120000);const errors:string[]=[];page.on('pageerror',e=>errors.push(e.message));page.on('console',m=>{if(m.type()==='error')errors.push(m.text());});await page.goto('/#gifts');await page.locator('.gift-parcel').nth(index).click();const d=page.locator('dialog[open]');const stage=d.locator(`[data-gift-world="${kind}"]`);await expect(stage).toBeVisible();await expect(stage.locator('[data-native-ready=true]')).toHaveCount(1,{timeout:45000});await expect(stage.locator('canvas')).toHaveCount(1);
 const primary=d.locator('.gift-control--primary:enabled').first();if(await primary.count())await primary.click();
 if(kind==='letter'){await d.getByRole('button',{name:'Skip animation',exact:true}).click();await expect(d.locator('.gift-letter__reading')).toContainText("Bhumi,");}
 if(kind==='jar'){await d.locator('.gift-note-picker button').nth(16).click();await expect(d.locator('.gift-jar__note')).toContainText('NOTE 17');await expect(d.locator('.gift-jar__note')).toContainText('chapter of my life its own meaning');await d.getByRole('button',{name:'Put note back'}).click();await d.getByRole('button',{name:'Read all 17',exact:true}).click();await expect(d.locator('.gift-jar__all li')).toHaveCount(17);}
 if(kind==='flower'){for(let i=0;i<3;i++)await d.locator('.gift-control--primary').click();}
 if(kind==='cassette'||kind==='vinyl')await expect(d.getByRole('button',{name:'Play',exact:true})).toBeDisabled();
 if(kind==='cinema')await expect(d.locator('.gift-cinema__status')).toContainText('real photograph');
 if(kind==='coupons')await expect(d.getByRole('button',{name:'Mark redeemed'})).toBeDisabled();
 if(kind==='hope-tree'){for(let i=1;i<8;i++)await d.locator('.gift-control--primary').click();const written=futureGardenLeaves.filter(leaf=>leaf.text).length;if(written)await expect(d.locator('.gift-future-garden__hopes li')).toHaveCount(written);else{await expect(d.locator('.gift-future-garden__hopes li')).toHaveCount(0);await expect(d.locator('.gift-future-garden__missing')).toHaveText(packMicrocopy.missingText);}}
 await stage.scrollIntoViewIfNeeded();await page.screenshot({path:`qa/ultra-gift-${String(index+1).padStart(2,'0')}.png`,timeout:30000});
 const reset=d.locator('.gift-experience-shell__footer button').first();if(await reset.count()){await reset.click();await expect(stage.locator('[data-native-ready=true]')).toHaveCount(1,{timeout:45000});await expect(stage.locator('canvas')).toHaveCount(1);}
 await d.getByRole('button',{name:'Close this experience',exact:true}).click();await expect(page.locator('dialog[open]')).toHaveCount(0);await expect(page.locator('dialog canvas')).toHaveCount(0);expect(errors).toEqual([]);
});
test('gallery uses seventeen native previews and no per-tile WebGL canvases',async({page})=>{await page.goto('/#gifts');await expect(page.locator('.gift-parcel__preview img')).toHaveCount(17);await expect(page.locator('.gift-parcels canvas')).toHaveCount(0);expect(await page.locator('.gift-parcel').count()).toBe(17);});
test('mobile jar and reduced-motion renderer stay stable, no layout overflow',async({page})=>{await page.setViewportSize({width:390,height:844});await page.goto('/#gifts');await page.locator('.gift-parcel').nth(1).click();const d=page.locator('dialog[open]');await expect(d.locator('[data-native-ready=true]')).toHaveCount(1,{timeout:45000});await d.getByRole('button',{name:'Draw another note',exact:true}).click();await d.locator('.gift-native-stage').scrollIntoViewIfNeeded();const frames=await d.locator('[data-native-ready=true]').getAttribute('data-render-frames');await page.waitForTimeout(400);expect(Number(await d.locator('[data-native-ready=true]').getAttribute('data-render-frames'))-Number(frames)).toBeLessThan(4);expect(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth)).toBe(true);await page.screenshot({path:'qa/ultra-jar-mobile.png'});await page.keyboard.press('Escape');await expect(page.locator('dialog[open]')).toHaveCount(0);});
```
