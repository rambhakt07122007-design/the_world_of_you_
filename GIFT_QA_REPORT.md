# Gift Atelier QA Report — 17 Experiences

> **Current native-3D build:** see `START_HERE.md` and `FINAL_IMPLEMENTATION_REPORT.md` for current scope, new browser evidence and limitations. Earlier findings/deployment descriptions below are historical. Current core QA: 12/12 pass; final native rose/crown/portal QA: 3/3 pass. No production deployment of this transformation has occurred.


**Local QA verified:** 3 November 2026 (Asia/Kolkata)  
**Vercel preview deployed:** 4 November 2026. Scope: local Gift Atelier interaction/responsive QA plus remote preview build verification. The production alias still serves the earlier twelve-scene release. This report is not a hosted interaction test or production-promotion approval.

## Build and toolchain

- `npm run build` — **passed** on the current source: TypeScript + Vite; 2,092 modules transformed. The 3 November QA build reported 2.96 seconds; the latest 4 November build passed in 3.68 seconds.
- `npm audit --audit-level=moderate` — **0 vulnerabilities** (no dependency was added for the gift expansion).
- Original Gift Atelier Vercel preview `dpl_C2F78TQXdsASk5b4WATYD9N1u6WV` — **READY / STAGED**; its build passed with 2,092 modules transformed (Vite reported 3.46 seconds). [Original preview URL](https://the-world-of-you-birthday-storybook-47p1os0ix.vercel.app/).
- Latest Vercel preview `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` — **READY / STAGED** with the global-audio and Birthday Ballroom updates; remote build passed (2,092 modules, 4.05 seconds). [Latest preview URL](https://the-world-of-you-birthday-storybook-7ythm9x51.vercel.app/).
- Browser: Playwright 1.56.1 / Chromium, local Vite production preview at `http://127.0.0.1:4173/`.
- No page errors, browser-console errors, HTTP responses at or above 400, or failed requests occurred during the gift interaction run.

## Responsive coverage

The Gift Atelier collection was checked at 360, 390, 430, 768, 1024, 1280, 1440 and 1920 px. The document had **0 px horizontal overflow** at every width. The grid settled to two columns at 360–430 px, three at 768 px, four at 1024 px and six at 1280–1920 px.

Each of the 17 open gift dialogs was additionally checked at **360 × 800**; the document and modal paper had no horizontal overflow in any case. The desktop captures are **1440 × 900**. This is a browser viewport test, not a real-device performance guarantee.

## Interaction coverage

| Gift | Verified interaction(s) |
|---|---|
| 01 · The Secret Letter | Opened and replayed the letter; narration stayed disabled without a real recording. |
| 02 · A Jar of Reasons | Drew a note and displayed all 17 editable slots. |
| 03 · The Flower That Never Fades | Grew the flower and rotated it. |
| 04 · Our Little Universe | Selected a star, zoomed and rotated the map. |
| 05 · Bhumi FM Exclusive | Inserted the cassette; playback stayed disabled and the missing recording was identified. |
| 06 · The Memory Cinema | Started the projector; the photo screen stayed honestly blank, playback stayed disabled, and full-screen control was present. No slideshow autoplay. |
| 07 · A Thousand Wishes | Collected stars and displayed all ten source wishes. |
| 08 · The Queen’s Crown | Rotated the crown and revealed the existing source note. |
| 09 · Open When… | Opened an envelope and confirmed the private message remains an explicit unfilled placeholder. |
| 10 · The Happiness Machine | Pulled the lever and verified the machine cycle/message state. |
| 11 · A Little Adventure | Unlocked map stops and confirmed the “not a real travel history” disclaimer. |
| 12 · The Music of Us | Started the silent turntable preview; audio playback remained disabled. |
| 13 · The Infinite Mirror | Cleared and reset the fog canvas using its accessible controls. |
| 14 · The Birthday Coupon Book | Advanced the page; redemption remained disabled for blank coupons. |
| 15 · The Future Garden | Planted a seed and revealed a leaf without inventing future copy. |
| 16 · The Secret Treasure Hunt | Reordered symbols by drag and keyboard-accessible move controls, solved the puzzle and unlocked its source-copy reward. |
| 17 · The Ultimate Surprise | Gathered the lights, opened the portal, confirmed the source finale text and kept sound permission off. “Return to Gift Atelier” closed the dialog successfully. |

Every gift rendered its mapped, distinct experience. All 17 visible dialog controls/inputs passed a DOM accessible-name smoke check. Enter opened the focused first gift; Escape closed it and returned focus to its invoking card. Escape/focus return was also checked across the first 16 gifts; Gift 17’s explicit return control was exercised.

## Persistence, motion and content safety

- Opening all gifts persisted 17 unique IDs and survived reload. Duplicate/unknown IDs were filtered and deduplicated; malformed JSON safely returned progress to 00/17.
- With `prefers-reduced-motion: reduce`, decorative flower sparkle animation computed to `animation-name: none` and `0s`; the experience controls/content remained available.
- Personal photos, recordings, reasons, private Open When copy, coupons and future hopes were not supplied and remain blank/disabled as documented. No fake memory, personal portrait, recording, date or promise was introduced. Audio is opt-in and no audio source is present; there is no autoplay. The top-bar global sound preference is wired to the Music Lounge, Bhumi FM and The Music of Us; global mute pauses playback and unmuting never auto-resumes. Since all current audio sources are empty, no real track playback was available to test.
- A hit-test during QA exposed a decorative portal layer intercepting Gift 17’s return button. The layer was moved behind the controls and made pointer-inert; the final full run then passed, including the return action.

## Screenshots

Seventeen local production-preview screenshots are saved in `docs/screenshots/gifts/`, one per opened gift. They are documentation captures, not runtime assets. See `ASSET_MANIFEST.md` for the individual filenames and sizes.

## Scope limits and release status

- The interaction/responsive evidence validates the local gift implementation before the latest global-audio/ballroom additions. Those additions pass local and remote build verification, but the full browser interaction suite was not rerun. Latest preview `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` is READY/STAGED; access protection redirects hosted checks to Vercel sign-in. The stable production alias remains on the prior twelve-scene release; no preview was promoted to production.
- No automated axe/WAVE scan, screen-reader session, formal contrast measurement, WCAG certification or real-device GPU/memory/FPS/battery profile is claimed.
- The credential used in a previous deployment remains a security follow-up: the user must revoke it. It was not reused or stored for this work. Future Vercel operations must use the connected integration only.
