# Component inventory — The World of You

This inventory describes the current Vite/React implementation. Chapter copy, dates, labels, gift records, photo mounts, audio entries and postcards are centralized in `src/content/chronosContent.ts`.

## App shell and shared components

| File | Responsibility | Accessibility / implementation notes |
|---|---|---|
| `src/App.tsx` | Composition root, document title/theme, active chapter/progress, initial hash landing, invitation/garden hash synchronization and ordered chapter list | Reading-line state is requestAnimationFrame-throttled; listeners/ResizeObserver clean up; invitation replay resets sound and returns to the opening. |
| `src/scenes/sceneCatalog.ts` | Stable twelve-scene IDs, semantic anchors, image paths and transition presets | Maps the established `#timepiece` anchor to Memory Observatory and `#birthday-cake` to Birthday Ballroom. |
| `src/scenes/SceneExperience.tsx` | Fixed decorative scene stage; active/adjacent art; GSAP/ScrollTrigger lifecycle and CSS/IntersectionObserver fallback | Twelve `aria-hidden` layers; natural document scroll; no chapter content or controls are moved into the stage. Reduced motion does not dynamically import ScrollTrigger. |
| `src/world/WorldNav.tsx` | Brand/current-chapter label, quick links, sound toggle and 12-chapter index | Named controls; `aria-expanded`/`aria-controls`; `aria-current` on active entries; Escape closes index and returns focus. |
| `src/world/WorldSection.tsx` | Shared chapter wrapper, eyebrow/side-note metadata and stable chapter anchor | Semantic section heading and matching `data-chapter`/scene-anchor attributes. |
| `src/components/ArchiveDialog.tsx` | Shared paper dialog for letters, gallery mounts, gifts and postcards | Native `<dialog>`, associated title, close button focus on open, Escape/backdrop close and focus return to the invoking control. |
| `src/content/chronosContent.ts` | Personal-content source of truth and derived `giftItems` list | Typed chapter IDs; unknown content remains empty/editable. |
| `src/utils/time.ts` | Timezone-safe elapsed-time and integer formatting helpers | Date-only origin is interpreted in `Asia/Kolkata`; no private hour is assumed. |

## Story chapters (rendered in order)

| Order / anchor | File | User-facing purpose and interactions |
|---:|---|---|
| 01 — `invitation` | `src/world/OpeningInvitation.tsx` | Animated paper invitation/CSS envelope; open CTA or skip; timer cleanup; reduced-motion open is immediate. |
| 02 — `garden` | `src/world/BirthdayGarden.tsx` | Birthday garden, pavilion, balloons, petals and fireflies; scene art/motion belongs to shared stage, not a second GSAP manager. |
| 03 — `storybook` | `src/world/Storybook.tsx` | Four-spread, eight-content-page scrapbook plus cover; lazy `react-pageflip`; buttons, arrow keys and swipe; reduced-motion flips use near-instant duration. |
| 04 — `timepiece` | `src/world/RelationshipClock.tsx` | Memory Observatory: elapsed time from 11 May 2025 and buttons for three verified date markers; live counter updates each minute. |
| 05 — `letters` | `src/world/LetterRoom.tsx` | Desk art and five envelopes; one supplied letter plus four intentionally empty entries; envelope opening and shared dialog. |
| 06 — `gallery` | `src/world/PolaroidGallery.tsx` | Six empty Polaroid mounts pending real photos; accessible lightbox with previous/next. |
| 07 — `flower-garden` | `src/world/FlowerGarden.tsx` | Ten wish flowers, selected/blooming state and polite live announcement of the selected source wish. |
| 08 — `gifts` | `src/world/GiftRoom.tsx` | Seventeen distinct CSS/SVG parcel forms, progress bar and dialogs; opened IDs persist under `world-of-you-opened-gifts` in local storage. |
| 09 — `music-room` | `src/world/MusicRoom.tsx` | Local-player interface and status; all tracks remain empty/paused until owner media is supplied; no autoplay or external stream. |
| 10 — `future-postcards` | `src/world/FuturePostcards.tsx` | Four illustrative landscape postcards with alt text and repeated “possible future / not a fact” labeling; shared dialog. |
| 11 — `birthday-cake` | `src/world/BirthdayCake.tsx` | Inline-SVG five-candle cake, sequential lighting, private wish state and button-driven extinguishing; no microphone access. |
| 12 — `finale` | `src/world/FinalCelebration.tsx` | Birthday message, source-draft attribution, finite confetti/star field and replay controls; distinct CSS dawn scene, no reused garden image. |

## Styles and assets

| File / location | Role |
|---|---|
| `src/styles/designTokens.css` | Warm palette, type families/scales, layout and local `@font-face` definitions. |
| `src/styles/global.css` | Base/reset, chapter layout, interactions, focus states and responsive breakpoints. |
| `src/styles/premium.css` | Editorial treatment, invitation/envelope mechanics and selected component details. |
| `src/styles/sceneSystem.css` | Environment palettes, stage depth planes, readable surfaces, responsive focal points and reduced-motion rules. |
| `public/assets/scenes/`, `backgrounds/`, `birthday/`, `paper/`, `postcards/` | Three new scene backgrounds plus existing non-personal illustrations; see `ASSET_MANIFEST.md`. |
| `public/assets/fonts/` | Six self-hosted variable WOFF2 files, four OFL license texts and provenance README. |
| `docs/screenshots/` | Production baseline and refreshed local scene captures; documentation only, not runtime assets. |

## Dependencies and loading strategy

- **React 19 / React DOM** — interface and interaction state.
- **TypeScript 5.9 / Vite 7** — static checks, development and production bundling.
- **GSAP + ScrollTrigger** — one shared owner for scene crossfades, subtle depth drift and chapter-heading reveals; dynamically imported and cleaned up with a scoped context.
- **`react-pageflip`** — dynamically imported near the scrapbook viewport.
- **`lucide-react`** — vector interface icons.
- No additional canvas/WebGL or 3D model library; CSS/SVG satisfies the 2.5D scene treatment without a heavier graphics runtime.

## Content-editing rules

1. Edit personal copy/data in `src/content/chronosContent.ts`.
2. Add only owner-supplied photographs under `public/assets/gallery/`; write truthful captions and alt text.
3. Add only local owner-provided or properly licensed audio under `public/assets/audio/`; set the matching track `src`.
4. Do not turn generated landscape art into a personal photo or historic memory.
5. Leave unknown details and gifts empty; do not infer dates, memories, events or promises.
