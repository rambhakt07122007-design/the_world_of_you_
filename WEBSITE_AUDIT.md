# Website audit — current production baseline

## Evidence and boundaries
Inspected deployed https://the-world-of-you-birthday-storybook.vercel.app/ with desktop Chromium, scrolled every accessible chapter, inventoried its buttons, opened the first letter with actual WebGL, and checked document overflow at 390×844. `qa-live-audit.json` records the results and exact inspection limits; `qa/letter-before.png` is the baseline. No page errors were observed in that pass. This is not a claim of exercising every gift, microphone, audio path or real mobile device. Earlier QA exists but is historical, not a substitute for new regression.

Repository inspected before implementation. Checkpoint: `/home/user/backups/chronos-before-letter-refinement.tar.gz`. Existing React 19 / TypeScript / Vite app; ordinary authored CSS, **not an installed Tailwind pipeline**. Preserve architecture and content. Three.js is used directly, GSAP is lazy-loaded, StPageFlip via react-pageflip is lazy-loaded. R3F is not required for one scene and would add another renderer abstraction.

## Feature classification (baseline)
| Feature | Classification | Evidence and recommended action |
|---|---|---|
| Invitation, chapter navigation | WORKING | Live chapter anchors and controls; preserve semantic content. |
| Ambient garden / image-based chapter art | NEEDS_IMPROVEMENT | Live accessible; code has CSS butterflies/balloons/fireflies and GSAP parallax competing with native scenes. Reduce decorative drift rather than deleting art. |
| Botanical 3D wish garden | WORKING / NEEDS_IMPROVEMENT | Existing native geometry, picking, wishes, bloom/wind; earlier production smoke passes. Stylized, not photoreal; preserve. |
| Scrapbook | WORKING / NEEDS_IMPROVEMENT | Code: StPageFlip drag/buttons and responsive portrait mode; no new live page-turn certification. DOM pages aren't volumetric paper. Retain functional engine; custom book would be substantial separate work. |
| Timepiece / observatory | NEEDS_IMPROVEMENT | Native celestial scene exists; constellation selection/true memory content is limited. Do not invent records. |
| Letters | NEEDS_IMPROVEMENT | Live dialog opens; code has hinged flap, but rigid panel rotations, shrinking seal, paper hidden until mid-extraction, damping rather than fixed-duration transport. Text appears before paper finishes. Replay resets but does not replay; skip MISSING. Replace choreography first. |
| Gallery | INCOMPLETE | Owner-provided media remain intentionally missing. Preserve editable mounts. |
| Gift atelier | NEEDS_IMPROVEMENT | 17 distinct DOM experiences retained; only 01/03/08/09/17 have native scene integrations. Twelve native 3D gift experiences INCOMPLETE. No safe reason to delete functioning experiences. |
| Bhumi FM | INCOMPLETE | Real audio component and volume/play controls exist; track source fields empty. No user audio available. Cannot certify real playback or claim music-reactive data. |
| Future postcards | NEEDS_IMPROVEMENT | Existing card interactions / imagined future copy retained. Not a new volumetric paper implementation. |
| Cake / birthday finale | WORKING / NEEDS_IMPROVEMENT | Native cake, baking and manual/optional mic ritual exist. Full ballroom environment and hardware blow accuracy INCOMPLETE. No mic autostart found. |
| Reduced motion / WebGL fallback | WORKING / NEEDS_IMPROVEMENT | Code stops continuous rendering for reduced motion; DOM content survives renderer failure. Letter completion must not depend on WebGL. |
| Performance | NEEDS_IMPROVEMENT | Lazy runtime, capped DPR, offscreen suspension, resource disposal exist. Native runtime >500 kB warning. No measured hardware FPS/Lighthouse score; no 60 FPS claim. |
| Accessibility | NEEDS_IMPROVEMENT | Native dialog focus/Escape, semantic controls, visible focus; readable text remains DOM. Need letter skip, completion synchronization, mobile layout checks. No comprehensive contrast/screen-reader certification. |

## Motion review / exact files
- `src/three/letter.ts`: replace rigid three-panel opening with continuous thickness mesh, rounded crease deformation, staged extraction and reversible fixed-duration timeline; split rather than shrink seal; responsive camera fit; retain wooden desk / warm lighting concept.
- `src/world/LetterRoom.tsx`: remove arbitrary envelope delay and 1.8s close timeout; synchronize text to choreography, add open/close/replay/skip and accessible canvas hit equivalent. Preserve every word from content source.
- `src/three/SceneCanvas.tsx`, `runtime.ts`: progress callback and immediate state for deterministic skipping; retain lazy init, lifecycle and quality controls. Observe callback cleanup; no additional animation library.
- `src/scenes/SceneExperience.tsx`: generic identical heading slide/fade on every chapter is UNNECESSARY; remove this block, retain chapter-specific background transitions and intentional parallax. Existing GSAP context cleanup is meaningful; do not uninstall GSAP (also baking uses it).
- `src/styles/cinematic.css`: current vertical reveal is a page-wide wipe, not handwriting. Replace with brief per-paragraph ink reveal after unfolding, final readable DOM. True glyph path handwriting is not supplied and should not be fabricated.
- `src/styles/premium.css`, `global.css`, `giftAtelier.css`, `sceneSystem.css`: exhaustive named CSS keyframe/use-location inventory in `ANIMATION_INVENTORY.md`. No duplicate keyframe names found. Retain physical record rotation/flame flicker/page turns/celebration bursts. Reduce decorative perpetual drift and gift overshoot; do not globally disable meaningful controls. Static inventory is not proof of unused runtime classes, so no unverified mass deletion.
- `garden.ts`, `cake.ts`, `celestial.ts`, `botanicalGift.ts`: native procedural motion retained; no copied models or expensive cloth/physics. Choreography uses frame delta and shared renderer.

## Prioritized implementation plan
1. Checkpoint, live inspection, animation inventory and this audit (complete before source changes).
2. Native letter geometry: actual pocket, thick flap on crease, split wax, continuously bent thick tri-fold mesh, controlled reverse transport, camera composition. Deterministic low-cost deformation, no cloth sim/postprocessing DOF on mobile.
3. Letter UI: actual completion state, replay/skip, canvas tap and keyboard equivalent, fallback/reduced motion, text readability.
4. Remove repeated heading entrances; quiet selected decorative CSS motion. Preserve functioning chapter transitions and all content.
5. Build and desktop/mobile tests: open, close, replay, skip, interruptions, fallback and reduced motion; inspect screenshots. Incremental other scene upgrades only after this priority validates.
6. Report exact delivered scope and incomplete sections. Do not present this pass as all 17 native gifts or a complete photoreal cinematic rebuild. Deployment is separate from local implementation and must be explicitly verified if performed.

## Implemented follow-up (after baseline audit)
Letter priority implemented and isolated tests passed before expanding scope. Native postcards added incrementally in `src/three/postcard.ts`, wired through runtime/SceneCanvas and `FuturePostcards.tsx`: actual thick card, original artwork loaded as front texture, original speculative copy on reverse, flip/tap and previous/next controls, DOM copy retained. Asynchronous artwork loads reject stale or disposed requests; runtime invokes choreography-specific cleanup. Camera fit expanded after screenshot review to keep the letter/envelope in frame. This changes the postcard classification to NEEDS_IMPROVEMENT with native geometry present; still not curved paper / stroke-traced handwriting. Full results in IMPLEMENTATION_REPORT.md.
