# 17-world transformation audit

## Evidence / inspection boundaries
Repository inspection: `giftsContent.ts` read in full, all 17 experience component implementations inspected, native renderer/runtime, letter, botanical/crown, gallery and existing tests inspected. Existing site has previously been browser-inspected; new gift-specific live baseline will be recorded separately. **No screenshots are attached to the current message**, so no assertion about their pixel contents is made. Existing deployed build differs from the latest local letter/postcard refinement. Screenshots created during this pass will be labeled as live or local.

React 19 + TypeScript + Vite, authored CSS (not installed Tailwind). Existing direct Three.js lifecycle and lazy runtime, GSAP chapter/baking effects, StPageFlip. Current gift-specific native scenes: 01 letter, 03 flower, 08 crown, 09 reused letter, 17 portal. Twelve other experiences retain DOM/SVG/Canvas scenes. Existing content modules are the source of truth.

## Element decisions and identity-preserving design
| Gift | Actual identity / content | Classification | Intended native environment and meaningful interaction |
|---|---|---|---|
| 01 | Secret Letter: existing source letter | IMPROVE EXISTING 3D | Reuse continuous thick bent paper + real pocket; synchronize gift text/replay/skip just like LetterRoom. |
| 02 | Jar of Reasons: 17 intentionally blank reason slots | REBUILD / NEEDS CONTENT | Hollow glass jar wall and base, rim, metal threaded lid, fabric ribbon, seventeen separate folded notes. Turn, lid open, pick/return, shuffle, read all; blanks remain explicit. |
| 03 | Everlasting Flower: existing bloom stages; blank hidden-message slot | IMPROVE EXISTING 3D | Keep petal geometry; enlarge soil/seed, root cross-section and staged growth. |
| 04 | Little Universe: only two verified dates | CONVERT TO 3D | Miniature orrery with planets, halos, two selectable archive markers, orbital mechanics and overview/zoom. |
| 05 | Bhumi FM: first track, source missing | REBUILD / NEEDS CONTENT | Cassette deck, visible twin reels, mechanical insertion/eject; playback only against real supplied source. No synthetic sound/equalizer pretending to analyze absent audio. |
| 06 | Memory Cinema: no real photos supplied | REBUILD / NEEDS CONTENT | Film projector with two reels, lens, beam and screen; power controlled by existing switch. Preserve blank media status. |
| 07 | A Thousand Wishes: ten existing source wishes | CONVERT TO 3D | Wishing tree / lantern grove with ten selectable wish objects, branch structure and collected-light state. Do not invent 1,000 written wishes. |
| 08 | Queen's Crown: source birthday note | IMPROVE EXISTING 3D | Keep eight detailed points, gold molding, facets and velvet inspection; add reflective studio environment rather than flat recolor. |
| 09 | Open When: four prompts, blank bodies | IMPROVE EXISTING 3D / NEEDS CONTENT | Distinct four-envelope cabinet / drawer choreography rather than the exact gift-01 desk; selected physical envelope opens. |
| 10 | Happiness Machine: existing wishes | REBUILD | Brass workshop mechanism, crank/lever/gear train and advancing paper ticket. Existing wish selection drives output. |
| 11 | Little Adventure: speculative postcard locations | CONVERT TO 3D | Raised miniature map with physical markers and route; preserve progression and speculative disclaimer. |
| 12 | Music of Us: empty real-track playlist | REBUILD / NEEDS CONTENT | Turntable, spindle, physical grooves, tonearm and real playback controls. Silent mechanical preview labeled; no fake audio-reactive bars. |
| 13 | Infinite Mirror: existing abstract message, wipe interaction | REBUILD | Ornate dimensional mirror, inset surface and clearing mist tied to original wipe progress; retain accessible reveal button. No camera permission or invented portrait. |
| 14 | Coupon Book: six blank unredeemable offers | REBUILD / NEEDS CONTENT | Bound booklet, thick stacked pages, bent turning leaf and perforation marks. Existing approved-content gate retained. |
| 15 | Future Garden: eight blank hope leaves | REBUILD / NEEDS CONTENT | Sculpted exposed-soil diorama, substantial seed, root network, trunk/branches and individual unfurling leaves. Seed→roots→sprout→leaves growth; hope slots remain blank. |
| 16 | Treasure Hunt: existing flower/moon/star ordering + OPEN puzzle | REBUILD | Physical locked chest, metal key/lock, three symbol medallions; original keyboard/drag puzzle opens hinge and reveals existing reward. |
| 17 | Ultimate Surprise: existing source message and cake link | IMPROVE EXISTING 3D | Existing portal with physically gathering sixteen lights, staged aperture and actual cake navigation retained. |

## Shared interface / removal decisions
- KEEP AS 2D: titles, subtitles, progress, state labels, navigation, forms, all readable messages, owner-content notices, accessibility controls. Preserve every gift's meaningful handlers.
- REBUILD: flat decorative gallery icons into renders of the real native gift objects. Avoid seventeen live canvases. Render static native previews with one offline renderer, keep only focused scene interactive.
- REBUILD: experience framing into a large cinematic stage with adjacent readable instrument/copy area; no tiny 3D ornament dropped into an unchanged flat card.
- REMOVE selectively: CSS scene illustrations replaced by tested native scenes; fake equalizer animation; generic shelf icons once native previews exist. Keep actual interactive fallback buttons rather than hiding controls with the art.
- Existing direct Three renderer stays for non-gift chapters. Add a shared React Three Fiber focused-gift stage, reusing native factories, rather than rewriting the whole application. GSAP manages staged letter transport through a paused timeline. No mass library replacement.
- IMPROVE: optional studio reflections, calibrated lower-intensity lighting, capped/adaptive DPR, offscreen/hidden suspension, reduced-motion demand rendering, explicit disposal including async image loads. No 60 FPS assertion without hardware measurement.
- NEEDS CONTENT: reasons, audio, photos, open-when bodies, coupons, future hopes. No invented replacements.

## Sequence / checkpoints
Checkpoint `/home/user/backups/chronos-before-17-worlds.tar.gz`. Inspect and audit → shared gift-stage architecture → gift01 integration → jar → flower → universe →05–08 → actual09–17 → soil/growth → gallery previews/framing → obsolete-art cleanup after verified replacements → build/desktop/mobile/fallback/reduced-motion tests → `3D_IMPLEMENTATION_REPORT.md`.

## Acceptance risks to verify
Glass transparency sorting on mobile; note picking through glass; blank content retained; no permission/autoplay requests; 17 scenes must be individually mounted and disposed; no 17-canvas gallery; no CSS-only paper called native 3D; no personal photo inferred from scene artwork. Procedural assets may remain stylized rather than photoreal; report this honestly. Native GLB compression is only relevant to exported snapshots, because runtime objects are generated in code.

## Implementation follow-up and observed tests
All 17 mapped gift identities now have native factory integrations through the focused R3F stage; their baseline classifications above are preserved as the pre-change audit. Gallery icons replaced with compressed offline renders of those actual factories, not live seventeen-canvas rendering. Desktop stage/instrument-panel layout replaced the narrow flat-modal composition. Jar/flower/tree/letter representative tests passed, then the full new suite passed **19/19 in5.8m** before the final low-tier studio-reflection adjustment. Final focused validation is recorded in `3D_IMPLEMENTATION_REPORT.md`; do not equate scene render coverage with completion of photoreal creative standards.

The broader regression encountered WebGL program validation failures during the synthetic microphone test, plus a test fixture that began noise on a fixed timer before calibration reliably finished under software rendering. Runtime now surfaces a graphics fallback instead of continuing broken rendering; the fixture now waits for the real listening status before sending synthetic noise. Synthetic mic rerun passed with **one explicitly recorded graphics fallback**, not a clean graphics certification.

### Final evidence
Live unchanged production jar successfully recaptured after waiting for its real note panel; local jar/high-tier screenshot inspected. All17 native per-gift tests19/19PASS; final focused14/14PASS; remaining core5/5PASS; synthetic mic1/1PASS with1recorded graphics fallback. Separate runs, not a claimed single full45pass invocation. Source preservation2/2unchanged. See full report for known graphics fallback and creative-quality limitations.
