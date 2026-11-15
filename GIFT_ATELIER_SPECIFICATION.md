# Gift Atelier Specification — 17 Worlds, One Story

**Updated:** 4 November 2026  
**Scope:** Component/interaction specification, local QA, and Vercel preview-build status for the implemented Gift Atelier. The production alias remains unchanged.

## Design principles

- Preserve the existing React/TypeScript/Vite application, chapter anchors, natural scrolling, opening index, and local progress key `world-of-you-opened-gifts`.
- Present all 17 gifts in any order. Opening one never locks another. Every gift can be replayed; the common native dialog can be closed with its close control, Escape, or backdrop.
- Give each gift its own interaction, visual stage, micro-animation and content state. The shared dialog is only the accessible container; it is not the gift experience.
- Use DOM, CSS and SVG for the current gift worlds. Do not add Three.js, WebGL, GLSL, physics, Lenis or an audio dependency until a measured requirement justifies the bundle/runtime cost.
- Personal text, photos, audio and promises stay blank or explicitly pending when the owner has not supplied them. A pending slot must never look like a broken asset or imply a fake memory.
- Reduced-motion support, visible focus, keyboard alternatives, no autoplay and responsive layouts remain requirements.

## Gift catalogue and behavior

| # | Gift | Distinct opening / interaction | Content and asset status |
|---:|---|---|---|
| 01 | The Secret Letter | Burgundy envelope, wax-seal reveal, paper rise/unfold, close/fold, replay writing animation. | Uses the existing source birthday letter only. Voice narration is disabled pending a real recording. |
| 02 | A Jar of Reasons | Glass jar shake, draw another note, shuffle, read all 17. | Seventeen editable reason slots are blank. |
| 03 | The Flower That Never Fades | Seed → stem → leaves → bloom; rotate left/right and replay bloom. | Hidden-message field is blank. Flower is CSS-drawn, not a portrait or personal memory. |
| 04 | Our Little Universe | Select stars, zoom, rotate, return to overview. | Shows only the verified first-connection and proposal dates (11 May 2025; 17 July 2025). |
| 05 | Bhumi FM Exclusive | Insert/eject cassette; play, pause, stop, rewind and volume controls. | Uses the existing local track slot; controls stay disabled until an owner recording exists. No synthetic voice. |
| 06 | The Memory Cinema | Start/dim projector; play/pause, previous/next, replay and optional full screen. | Screen remains an explicit empty photo mount until real photographs are supplied. Slideshow does not autoplay. |
| 07 | A Thousand Wishes | Collect star-wishes, connect a constellation, show/hide the wish list. | Uses the ten existing source wishes; “10 / 10” is shown as the actual current count. |
| 08 | The Queen’s Crown | Rotate a CSS crown and inspect crown/jewel/velvet details. | Contains no portrait. The revealed note reuses existing source copy. |
| 09 | Open When… | Choose one of four envelopes, break its seal, open/fold the letter. | Prompts are present; each private message body is blank and editable. |
| 10 | The Happiness Machine | Pull a lever, turn gears and reveal a random existing source wish; repeat/reset. | No invented personal message. |
| 11 | A Little Adventure | Select destinations and unlock the next map location. | Reuses the four explicitly speculative postcard scenes/captions; this is not a travel history. |
| 12 | The Music of Us | Vinyl stage, track selection, previous/next, play/pause/stop, progress and volume; silent turntable preview. | Existing local tracks have no audio source. Playback and volume remain unavailable until licensed/owner-provided files are added. |
| 13 | The Infinite Mirror | Pointer/touch wipes fog from a canvas; accessible clear/reset buttons. | Reveals abstract birthday decoration only—no generated portrait or fake reflection. |
| 14 | The Birthday Coupon Book | Browse six pages, mark a coupon redeemed, restore it. | Coupon title/body slots are blank; empty coupons cannot be redeemed. Only owner-approved offers may be added. |
| 15 | The Future Garden | Plant seed, grow a tree and reveal up to eight leaves. | Future-hope text slots remain blank; no event or promise is fabricated. |
| 16 | The Secret Treasure Hunt | Drag/reorder three symbols or use move buttons; solve a clue and enter a password. | Generic, solvable puzzle. Reward reuses existing source copy. |
| 17 | The Ultimate Surprise | Gather 16 gift marks, open a portal, reveal finale copy, replay and return to Atelier. | Uses the existing finale source message. Sound preference is visible, but playback is unavailable until a sound asset is supplied. No prerequisite gifts. |

## Architecture

- `src/content/giftsContent.ts` — gift definitions, experience IDs, owner-editable empty fields, puzzle constants, and content-readiness indicators.
- `src/content/chronosContent.ts` — existing verified dates, source letter, wish list, local audio slots, gallery slots, postcard scenes and finale source copy.
- `src/world/GiftRoom.tsx` — responsive collection, localStorage progress with safe parsing/deduplication, completion state, and accessible dialog host.
- `src/world/GiftExperiences.tsx` — separately named experience components for each of the 17 gifts; local audio helper pauses and cleans up on unmount/source changes.
- `src/styles/giftAtelier.css` — seventeen visual grammars, card identities, responsive behavior, focus/disabled states and reduced-motion overrides.
- `src/components/ArchiveDialog.tsx` — shared native-dialog focus/Escape/close handling; gift-specific width is opt-in via class name.

## Progress persistence

- Storage key remains `world-of-you-opened-gifts` for compatibility with existing saved progress.
- Values are parsed defensively, filtered against known gift IDs and deduplicated. Invalid JSON, unknown IDs and storage exceptions do not block the experience.
- Opening a gift marks it as opened; replay never removes or blocks access. The progress display is `NN / 17`; the completed state preserves replay access.

## Content and dependency gates

- No user photos, voice recording, music track, 17 reasons, Open When bodies, approved coupons or future hopes were supplied. Those are content gates, not reasons to insert invented copy.
- The current visuals use CSS/DOM/SVG and already-shipped local scene/postcard art. There is no new Three.js/WebGL/physics dependency, remote image/font, or external audio request.
- The silent record-rotation preview is a motion-only control; it is not represented as music playback.
- Any later 3D, shader, audio-reactive, or physics feature needs a separate performance/accessibility review and a non-WebGL/reduced-motion fallback.

## Verification state

The existing twelve-scene baseline passed 96 settled scene/viewport checks across 360, 390, 430, 768, 1024, 1280, 1440 and 1920 px. The Gift Atelier implementation passed a TypeScript/Vite production build (2,092 modules), a zero-vulnerability npm audit, 17 experience interaction checks, grid checks at those eight widths, 17 modal checks at 360 × 800, keyboard/focus and storage recovery tests, accessible-name smoke scans, and a reduced-motion check. Seventeen 1440 × 900 captures are in `docs/screenshots/gifts/`. Latest Vercel preview `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` is READY/STAGED with the subsequent global-audio and Birthday Ballroom updates; its remote build passed (2,092 modules, Vite 4.05 seconds). The preview is access-protected, so hosted UI interaction tests remain unavailable; the latest incremental changes did not receive a new local browser interaction run. Detailed results and limitations are in `GIFT_QA_REPORT.md`. The stable production alias remains on the earlier twelve-scene release; no preview was promoted to production.
