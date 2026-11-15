# Design System — Cinematic Birthday Universe

**Status:** Implemented in `src/styles/sceneSystem.css` and the shared stage; responsive/motion states verified.  
**Reference:** `PROJECT_AUDIT.md`, `SCENE_ARCHITECTURE.md`, and `FINAL_QA_REPORT.md`.

## 1. Creative intent

A quiet, richly art-directed birthday story that travels through twelve connected rooms/worlds. Each chapter has its own lighting, depth, foreground silhouette, color temperature, and motif. A fixed decorative scene stage transforms behind the reader while the existing chapter content remains in natural document flow. The story should feel like turning a page into a new place—not like twelve unrelated panels, and not like a slideshow or forced-scroll ride.

Visual vocabulary: editorial storybook, tactile paper, cinematic framing, botanical details, low-contrast grain, carefully controlled glows and shadows, mature rather than cartoonish. Keep decorative effects restrained so Bhumi’s actual words and supplied material remain the emotional center.

## 2. Typography

All fonts are local WOFF2 assets with SIL OFL license text in `public/assets/fonts/`.

| Role | Family | Usage |
|---|---|---|
| Display | Playfair Display | Chapter titles, invitation and ballroom/finale titles. |
| Editorial | Cormorant Garamond | Reading copy, captions, scene notes. |
| Handwritten accent | Caveat | Short, selectively used annotations; never long body copy. |
| UI | DM Sans | Navigation, controls, labels, metadata. |

Use the existing local faces and fallbacks; do not reintroduce remote font requests. Keep the current clamp-based responsive scale, but ensure the 360 px layout does not force clipping or tiny body text.

## 3. Core palette and material tokens

Retain the existing warm botanical paper system as the authored-content layer. Add scene-specific environment tokens rather than replacing the current global palette.

| Token family | Starting value / direction | Application |
|---|---|---|
| Parchment | `#F5EEE5`, `#FFFAF2` | Letter paper, readable content surfaces. |
| Ink | `#41322F`, `#705951` | Body copy and secondary text. |
| Rose | `#B8747D`, `#89545C` | Focus/interaction accents; not the only status cue. |
| Antique gold | `#BD965C`, `#E1C994` | Trim, light, chapter markers. |
| Garden sage | `#9AA58C` plus deeper forest values | Garden environment and botanical forms. |
| Observatory | Midnight `#18233A`, dusk `#34425D`, star-gold `#E4C887` | Backdrop only; keep reading text on pale, translucent paper. |
| Gallery | Aubergine `#302631`, warm wall `#594650`, brass `#D2B574` | Spotlighted memory wall and blank mounts. |
| Music | Plum/navy `#262135`, rose `#B8747D`, amber `#D0A46B` | Lounge environment; player remains legible. |
| Ballroom | Merlot `#633843`, candle-ivory `#FFF3D7`, champagne `#D9B66F` | Celebration room and cake focal point. |
| Future/finale | Twilight blue, dusty peach and dawn ivory | Clearly speculative postcards and final release. |

Expose reusable CSS custom properties for scene background, glow, floor/horizon, accent, readable surface, border, and shadow. Prefer color overlays and gradients to hard scene-color panels. Contrast requirements are measured on rendered text, not inferred from the token names.

## 4. Scene-specific art direction

| Scene | Environment / lighting | Foreground and depth cues |
|---|---|---|
| Invitation Room | Warm dusk on a writing desk; parchment highlights; candle/lamplight | Envelope and card remain the hero; softly framed window/light shaft and dust. |
| Birthday Garden | Existing flower-path art; peach-gold sun through leaves | Foreground petal silhouettes, midground path, distant pavilion. |
| Scrapbook | Amber desk and layered page edges | Paper corners, ribbon/book silhouette, shallow paper shadow; real flipbook stays interactive. |
| Memory Observatory | Midnight blue with antique gold celestial instruments | A few star points, telescope/orbit shapes and clock rings; dates remain the factual anchors. |
| Letter Room | Walnut/candle warmth and localized light | Existing desk image and envelope props; warm wall shadow, no invented correspondence. |
| Memory Gallery | Deep plum gallery wall with warm pools of light | Empty, owner-editable frames; no synthetic personal photos or fabricated captions. |
| Wish Garden | Lavender dawn fading into sage and blush | Layered horizon/grass, pollen-like few particles, stylized flowers. |
| Gift Atelier | Velvet/rose cabinet with small gold work lights | Existing 17 gifts remain individual controls; shelves and soft foreground drape. |
| Music Lounge | Low aubergine light and amber ring reflections | Vinyl grooves/curtain silhouette; no audio until the user chooses it and a real track exists. |
| Future Postcards | Sunset sky, blue-hour shoreline and paper travel marks | Four existing illustrative cards float/recede; copy stays clearly hypothetical. |
| Birthday Ballroom | Candlelit merlot/champagne room | Existing cake interaction is focal; paper garlands, chandeliers and soft confetti. |
| Finale | Quiet blue-to-gold dawn, distinct from the garden | Sparse falling stars/light, a clean central closing card and easy replay. |

## 5. Surface, grain, and layer rules

- Keep the current local grain treatment, but lower its contrast where it would compete with small type.
- The scene stage is an `aria-hidden` decorative background. Required copy, controls, and personal content remain in the normal semantic React tree.
- Chapter content may sit on a translucent, softly blurred parchment surface (`--scene-surface`) whose tint varies by scene; do not give every section the same opaque rectangle.
- Use edge fades/vignettes to connect adjacent environments. Scene boundaries are soft lighting/prop hand-offs rather than abrupt full-bleed color swaps.
- Decorative particles stay small in number, CSS/SVG when possible, pointer-events none, and do not cause layout.
- Avoid low-contrast text over imagery. If a dark palette is used, put text on an appropriately opaque surface and verify WCAG AA contrast.

## 6. Layout and responsive behavior

- Native document scrolling; scene stage is fixed and decorative, chapters are not pinned.
- Existing content widths and gutters remain the starting point. Keep all controls inside the viewport and protect mobile safe areas.
- At 360–600 px, simplify/remove distant scenery and reduce parallax; stack panels and preserve adequate tap targets. No required WebGL or hover-only affordance.
- At 768–1024 px, rebalance the scene focal point and chapter layouts without forcing desktop art crops.
- At 1280–1920 px, preserve the full layered composition while keeping prose within its readable max width.
- Required QA widths: 360, 390, 430, 768, 1024, 1280, 1440, 1920 px.

## 7. Motion and accessibility tokens

- Default transition uses a restrained `power1.inOut`/linear scroll-scrub curve; do not use overshoot/bounce for world transitions.
- Intro/interactive component motion may remain expressive but must have a reduced-motion equivalent.
- `prefers-reduced-motion: reduce`: no parallax, continuous ambient movement, particle loops, or scrubbed camera motion. Select the current scene discretely with an observer and preserve every control/content state.
- Focus rings remain at least 3 px and clearly visible on every scene surface. Hover is supplementary only.
- Do not use color alone to identify active chapter, opened gifts, audio state, or wish selection.

## 8. Implementation guardrails

The repository uses custom CSS and already self-hosts its fonts. No Tailwind migration, new motion package, database, service, or WebGL requirement is part of this design. Reuse GSAP/ScrollTrigger with one owner and explicit teardown; use existing image assets plus a small number of environmental illustrations. Keep content and interactions in the existing chapter components.

## 9. Implementation notes

- The shared stage is `SceneExperience.tsx` with twelve scene layers. `sceneCatalog.ts` maps the invitation, garden, scrapbook, observatory, letter room, gallery, wish garden, gift atelier, music lounge, postcards, ballroom, and finale to their existing chapter anchors.
- Invitation Room, Memory Observatory and Birthday Ballroom use three optimized decorative WebP environments; other worlds use distinct CSS atmosphere/depth compositions. The finale is a CSS dawn/starfield scene and does not reuse the birthday-garden image.
- Content remains in the existing normal-flow chapter components on translucent readable surfaces. `App.tsx` updates active chapter and progress from a requestAnimationFrame-throttled reading line and restores initial hash navigation after React mounts.
- Build, 8 responsive widths, 12-scene forward/reverse motion, reduced-motion, dynamic preference changes, keyboard/dialog interactions, and final screenshots are documented in `FINAL_QA_REPORT.md`. Contrast certification and assistive-technology screen-reader testing are not claimed; see `ACCESSIBILITY_REPORT.md`.
