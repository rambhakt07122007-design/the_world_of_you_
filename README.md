# The World of You

> **Status:** the live site (https://the-world-of-you-birthday-storybook.vercel.app) is the master build with content pack 1 (commit `a92d2d8`, see `docs/DEPLOYMENT_REPORT.md`).
> This repository also contains the **three-language build** (English / Hinglish / हिन्दी, content pack 2), which has **not been deployed yet**: it is deployed only on the owner's confirmation.
> The older reports in the project root (`3D_IMPLEMENTATION_REPORT.md`, `IMPLEMENTATION_REPORT.md`, `WEBSITE_AUDIT.md` …) describe earlier stages; the current ones are listed in `docs/README.md`.

A cinematic, scroll-linked birthday storybook for Bhumi. The experience begins with an invitation and travels through twelve connected rooms while the existing chapters, controls and natural document scrolling remain intact.

**Stack:** React 19 · TypeScript · Vite · three.js with `@react-three/fiber` (one shared canvas for the 17 gift worlds and the section scenes, with a poster fallback when WebGL is not available) · GSAP/ScrollTrigger · `react-pageflip` · custom CSS. The Gift Atelier contains 17 independently openable and replayable experiences. Fonts are self-hosted locally: Playfair Display, Cormorant Garamond, DM Sans and Caveat for English and Hinglish, and Noto Serif Devanagari, Noto Sans Devanagari and Kalam for Hindi (all SIL OFL; see `public/assets/fonts/README.md`).

## Languages

The site speaks **English**, **Hinglish (Roman Hindi)** and **हिन्दी (Devanagari)**. A selector with exactly these three options is always on screen (first screen, header, and inside every open letter, postcard and gift). It starts in English, remembers the choice (`localStorage["woy-language"]`, or `?lang=en|hinglish|hi` in a link) and switches without a reload: an animated, atomic switch that keeps the scroll position, the open gift or letter, the scrapbook page, the sound switch, the progress and what the visitor typed. Each language has its own palette and motif (violet and gold / rose and amber / indigo and marigold).

* Owner's guide (where every word lives, how to edit, add photos and audio, run the tests): [`docs/OWNER_README.md`](docs/OWNER_README.md)
* What the owner still has to provide or check: [`docs/OWNER_INPUT_CHECKLIST.md`](docs/OWNER_INPUT_CHECKLIST.md)
* Audit of the language work, verified against assumed: [`docs/AUDIT_I18N.md`](docs/AUDIT_I18N.md)
* Build notes and decisions: [`docs/I18N_BUILD_NOTES.md`](docs/I18N_BUILD_NOTES.md)

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
