# Scene Architecture — Cinematic Birthday Universe

**Status:** Implemented and browser-verified. The audit and architecture specification preceded source changes; see `PROJECT_AUDIT.md` and `FINAL_QA_REPORT.md`.

## 1. Goals and invariants

- One reusable, data-driven scene catalog for all twelve worlds.
- One decorative stage behind the story content, driven by the reader’s real document scroll.
- Existing React chapter components continue to own their text, controls, data, dialogs, and local interaction state.
- No forced scroll, mandatory pinning, virtual-scroll wrapper, WebGL dependency, or invented personal content.
- The stage is never the only place where information exists; it is `aria-hidden` and pointer-events none.
- `prefers-reduced-motion`, JavaScript failure, or GSAP load failure results in a usable static/observer-based version.

## 2. Proposed module ownership

```text
src/scenes/
  sceneCatalog.ts          Twelve stable scene IDs, chapter anchors, backgrounds, transition presets
  SceneExperience.tsx      Fixed 12-layer stage, lazy adjacent art, GSAP lifecycle and CSS observer fallback
  sceneSystem.css          Scene palettes, readable surfaces, depth layers, mobile/reduced-motion rules

src/App.tsx                Composition root, reading-line chapter state, progress and initial hash landing
src/world/*.tsx            Existing chapter content and interactive state; no chapter is copied into the stage
src/world/WorldSection.tsx Semantic chapter IDs/headings and scene-anchor metadata
```

Use the existing `data-chapter` anchors as scroll triggers. Do not duplicate chapter content into the stage. `App.tsx` remains the composition root; the scene manager does not become a new router/state store.

## 3. Canonical twelve-scene catalog

| Catalog ID | Existing anchor/content | Display name |
|---|---|---|
| `invitation` | `#invitation` / `OpeningInvitation` | Invitation Room |
| `garden` | `#garden` / `BirthdayGarden` | Birthday Garden |
| `scrapbook` | `#storybook` / `Storybook` | Scrapbook |
| `observatory` | `#timepiece` / `RelationshipClock` | Memory Observatory |
| `letters` | `#letters` / `LetterRoom` | Letter Room |
| `gallery` | `#gallery` / `PolaroidGallery` | Memory Gallery |
| `wishes` | `#flower-garden` / `FlowerGarden` | Wish Garden |
| `atelier` | `#gifts` / `GiftRoom` | Gift Atelier |
| `music` | `#music-room` / `MusicRoom` | Music Lounge |
| `postcards` | `#future-postcards` / `FuturePostcards` | Future Postcards |
| `ballroom` | `#birthday-cake` / `BirthdayCake` | Birthday Ballroom |
| `finale` | `#finale` / `FinalCelebration` | Finale |

Keep existing public IDs/hash anchors unless a technical reason is documented. In particular, the scene IDs `observatory` and `ballroom` map to legacy anchors `timepiece` and `birthday-cake`. Reorder the cake/ballroom chapter after postcards to match the requested story sequence; keep its component and interaction unchanged.

Each config record contains: stable `id`, `anchorId`, display `title`, CSS scene key, base/accent/readable-surface tokens, optional local background image, object/depth motif, transition direction/strength, and whether a next scene can be prefetched. The config must not contain personal memory facts or narrative copy.

## 4. Rendering and data flow

1. `SceneStage` renders twelve `aria-hidden` world layers inside a fixed viewport container, outside any transformed/animated `.world-site` ancestor so `position: fixed` remains viewport-relative.
2. Every layer has CSS-only atmosphere and depth planes. Optional local art is an `<img alt="" aria-hidden="true">`; set `src` only for the active scene and its immediate neighbor(s), avoiding a dozen eager full-screen downloads.
3. `SceneScrollManager` resolves `SCENE_CATALOG` anchors, imports the already-installed GSAP and ScrollTrigger once, and creates a scrubbed crossfade per adjacent scene pair. It sets the active scene early enough to request/preload the next background before it becomes visible.
4. Scene transition state is presentation-only. Existing chapter links, local state, dialogs, gift storage, music controls, and content do not depend on the scene stage.
5. The active navigation chapter continues to be computed from semantic `[data-chapter]` elements. Scene state and navigation state may share IDs but should not become coupled to animation progress.

## 5. Transition model

For the forward transition into scene `i`, use the target chapter anchor and an interval around its approach (initial starting window: `top 82%` → `top 30%`). Scrub opacity and slight transform for the outgoing/incoming environment in parallel. The environment may pan/scale a few percent to imply a camera move; the section content stays in normal flow. Reverse the same timeline on upward scroll. The invitation remains the first scene at page top.

The first invitation control preserves the existing open/skip affordances. The experience is made scroll-continuous by keeping the invitation in document flow; opening may scroll to the garden after its envelope animation, while skip jumps to the same target. Manual native scrolling also works. Returning to the invitation resets only its entrance state; other interactions remain intact.

Do not pin all scenes. Do not lock body scroll or hijack wheel/touch input. Use scroll-margin/padding to account for the sticky chapter navigation.

## 6. Lifecycle and cleanup

- The manager owns the sole global ScrollTrigger registration for scene transitions/reveals.
- Build all tweens/timelines inside a `gsap.context()` and call `context.revert()` on unmount/effect change. Remove any listeners/observers and kill/refresh only manager-owned triggers.
- Guard async dynamic imports with a disposed flag so late resolution cannot create triggers after unmount.
- Call `ScrollTrigger.refresh()` after anchors exist and after important layout changes (font load/resize); do not call it on every scroll frame.
- There is no per-chapter GSAP importer: scene transitions, depth drift and heading reveals have one shared manager; chapter components retain their own CSS/interaction state.
- CSS is the baseline if GSAP fails; no console error should be emitted for the fallback path.

## 7. Reduced motion and no-JS behavior

- On `prefers-reduced-motion: reduce`, do not load/use scrubbed transitions or parallax. Use one `IntersectionObserver` over scene anchors to switch the active environment discretely; keep the visible scene stable and all controls functional.
- CSS removes ambient motion and smooth scrolling under the reduced-motion query.
- If GSAP fails to load or reduced motion is preferred, the semantic React page remains readable and the CSS/observer scene fallback keeps natural scroll. The existing Vite SPA is client-rendered; this implementation does not claim a no-JavaScript rendering path. Never hide chapter content behind the scene engine.
- The scene stage is decorative and never focusable; all controls remain in existing React chapter markup.

## 8. Performance and loading

- Use transforms/opacity only for scene crossfades; do not animate top/left/height/blur/filter continuously.
- Keep one stage, one layer per scene, and a small number of reusable decoration nodes. Avoid a giant DOM particle cloud or canvas.
- Load/prefetch only active and adjacent scene art; existing images retain width/height or aspect-ratio hints.
- Respect mobile: reduce depth offsets, parallax magnitude, and decorative detail; hide nonessential distant layers.
- Track actual built/gzip size, image sizes, layout shifts, CPU behavior, and frame smoothness on mobile. A budget is a gate, not an assumed result.

## 9. Test hooks

Use stable attributes (`data-scene-layer`, `data-scene-anchor`, `data-active-scene`) to support deterministic browser checks and debugging. Test initial invitation, all 11 transitions in both directions, direct chapter-index jumps, page-refresh at a hash, reduced-motion state changes, and unmount cleanup. These attributes must not replace semantic IDs or accessible names.
