# Final QA Report — Cinematic Birthday Universe + Gift Atelier

> **Current native-3D build:** see `START_HERE.md` and `FINAL_IMPLEMENTATION_REPORT.md` for current scope, new browser evidence and limitations. Earlier findings/deployment descriptions below are historical. Current core QA: 12/12 pass; final native rose/crown/portal QA: 3/3 pass. No production deployment of this transformation has occurred.


**Updated:** 4 November 2026 (Asia/Kolkata)  
**Scope:** Local React/Vite build and Gift Atelier browser QA, prior development StrictMode checks, a focused hosted smoke test for the earlier twelve-scene production release, and the latest Vercel preview build. Preview `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` is READY/STAGED; the hosted UI is Vercel-protected, so hosted interactions were not smoke-tested. The latest incremental global-audio and birthday-effects changes passed remote build verification but did not receive a new browser interaction run. This is not a canonical-ZIP comparison, formal accessibility certification, or device-level performance profile.

## Build and dependency audit

- Current local `npm run build` — **passed** (TypeScript + Vite; 2,092 modules transformed; 3.68 seconds on the latest 4 November build).
- `npm audit --audit-level=moderate` — **0 vulnerabilities**; no dependency was added for Gift Atelier.
- Follow-up 4 November changes: global sound-off now pauses/mutes the gift music players without auto-resume; Birthday Ballroom gained CSS balloons and a wish-triggered finite firework burst. These changes pass type-check/build/audit; a fresh interactive browser run was not performed.
- The prior Vercel production build passed on the earlier twelve-scene release (2,089 modules transformed). The latest Vercel preview `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` also passed: 2,092 modules transformed, Vite 4.05 seconds, and `npm ci` reported 0 vulnerabilities.
- Current Vite chunk measurements are recorded in `PERFORMANCE_REPORT.md`.

## Browser test environment

- Playwright **1.56.1**, Chromium.
- Local production preview served from the current `dist/` build at `http://127.0.0.1:4173/`.
- Development/React.StrictMode checks served from Vite at `http://127.0.0.1:5173/`.
- Hosted smoke test against `https://the-world-of-you-birthday-storybook.vercel.app/`. The Gift Atelier preview URL is protected by Vercel sign-in; the hosted page check redirected to login, so it received build/status verification only, not a hosted interaction smoke test.

## Scene and responsive coverage

- Exercised the twelve scene anchors in the required order at **360 × 800, 390 × 844, 430 × 932, 768 × 900, 1024 × 900, 1280 × 900, 1440 × 900, and 1920 × 1080**: **96 settled scene checks**.
- At each scene anchor, the active chapter marker, active scene ID and one settled visible environment agreed. During a crossfade, overlapping outgoing/incoming layers are expected; after the transition settles, exactly one layer is fully visible.
- No horizontal overflow, visible clipped controls, broken active scene artwork, failed requests, external resource requests, page errors or console errors in the local production responsive sweep.
- Forward and reverse navigation through all twelve scene states was checked in Vite development with React StrictMode enabled. No duplicate/stacked scene layers or console/page errors occurred.
- Initial hash loads for `#timepiece`, `#birthday-cake`, and `#finale` landed on the requested chapter with the right scene and active chapter caption. CTA, chapter index, and replay flows keep `#garden` / `#invitation` / target chapter fragments synchronized.
- Fresh desktop screenshots for all twelve scenes (1440 × 900) and mobile captures for invitation, observatory and finale (390 × 844) are in `docs/screenshots/`. The pre-scene production baseline remains as `00-production-before-scenes.png`.

## Gift Atelier local QA

- The current local production preview rendered all 17 distinct gift experiences. Each one opened independently; its core interaction, empty-content/media state and replay/close behavior were exercised. The detailed interaction matrix is in `GIFT_QA_REPORT.md`.
- Collection layout: eight widths from 360 to 1920 px, **0 px horizontal overflow** at each. Each of the 17 open dialogs was checked at 360 × 800 with no horizontal overflow.
- Keyboard: Enter opened the focused first gift; Escape closed it and restored focus. Escape/focus return passed for gifts 01–16; Gift 17’s explicit return action closed the dialog.
- Gift progress stored 17 unique IDs, survived reload, filtered duplicate/unknown values and recovered from malformed JSON. Reduced-motion preference disabled the flower sparkle animation. A visible-control accessible-name smoke scan passed for all dialogs.
- No page errors, browser-console errors, HTTP responses ≥400 or failed requests were observed. Audio/photo sources were empty; playback remained disabled, no autoplay was used, and the cinema remained an empty real-photo mount. The shared top-bar sound preference is wired to all current music players; global mute pauses active audio, and re-enabling sound never resumes it. Real playback could not be exercised because no audio file was supplied.
- Seventeen 1440 × 900 screenshots (one for each gift) are in `docs/screenshots/gifts/`.
- A pointer-interception issue found during the portal return test was fixed; the final full suite passed. This is local QA only, not a test of the hosted production site.

## Production alias smoke test

- Vercel deployment `dpl_9QT11nqNWa6tDXHyNk9c3AYoUMjU` is **READY / PROMOTED** on the `production` target; the stable alias is assigned with no alias error. The direct deployment URL is `https://the-world-of-you-birthday-storybook-4ibr1qnh1.vercel.app/`.
- The stable alias returned HTTP **200** and served the expected title, all twelve scene layers, Invitation as the initial scene, and GSAP motion mode. No broken images, page errors, HTTP errors, or failed requests were observed.
- A separate fresh load of `#timepiece` returned HTTP **200**, selected the `observatory` scene, and positioned the anchor at 58 px from the viewport top (scrollY 3129 px).
- This was a focused smoke check, not a repeat of the full 96-case responsive and interaction matrix against the hosted deployment.

## Interaction coverage

- Chapter index: twelve entries, correct active state, Escape closes and returns focus to the index toggle.
- Invitation: envelope/open animation completes into Garden; skip reaches the same chapter; replay resets the invitation state and the hash.
- Scrapbook: lazy flipbook loaded; page control advanced the page. Arrow-key support remains wired in the interactive stage.
- Observatory: verified-date selection updates the detail; clock minute hand visibly moves under standard motion.
- Letter archive: supplied source letter opens; Escape closes; focus moves to the close button and returns to the invoking envelope.
- Gallery: empty placeholder dialog communicates no personal photo was supplied; next/previous controls navigate mounts.
- Wish Garden: flower activation selects and reveals its matching source wish.
- Gift Atelier: see the preceding local QA section for the full 17-experience interaction, viewport, keyboard/focus, persistence, empty-media and screenshot results.
- Music Lounge: empty local track selection reports the missing file; playback remains disabled/paused; no autoplay or external audio request.
- Future Postcards: detail dialog includes the speculative/not-a-fact disclaimer.
- Birthday Ballroom: five candles light, wish status appears, and Blow them out clears the flames; no microphone path.
- Finale: replay control replays the finite celebration state.
- No personal photos or audio were supplied; gallery/media slots remain empty and no invented memories were added.

## Reduced-motion and lifecycle

- Initial `prefers-reduced-motion: reduce` tested at **390 × 844**: CSS/observer scene mode, no ScrollTrigger chunk loaded, clock hands stopped, invitation opens immediately, candles light immediately, and scene content remains usable.
- Runtime preference toggle tested while mounted. In Vite development, ScrollTrigger count was **32** in standard mode, **0** while reduced motion was enabled, and **32** after restoring standard motion: one set, no duplicates.
- One manager-owned trigger set consists of 12 depth tracks, 11 crossfades and 9 heading reveals. The React.StrictMode forward/reverse sweep completed without leaked duplicate timelines or errors.

## Accessibility smoke and limits

- One main landmark; named navigation regions; twelve semantic chapter sections; twelve decorative scene layers hidden from assistive technology.
- DOM smoke scan: zero visible unnamed controls, zero images missing an `alt` attribute, zero focusable controls inside `aria-hidden` content, and zero unnamed chapter-index items while open.
- Keyboard menu, dialog focus, Escape and focus restoration were exercised. See `ACCESSIBILITY_REPORT.md` for the exact scope and limitations.
- No automated axe/WAVE scan, manual screen-reader session, formal contrast measurement, or WCAG 2.2 AA certification was performed.

## Deployment and credential follow-up

- **Current production alias:** `https://the-world-of-you-birthday-storybook.vercel.app/` serves `dpl_9QT11nqNWa6tDXHyNk9c3AYoUMjU` (**READY / PROMOTED**, production), the earlier twelve-scene release.
- The latest Gift Atelier build is deployed as **preview only**: `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` (**READY / STAGED**) at https://the-world-of-you-birthday-storybook-7ythm9x51.vercel.app/. It was not promoted to production; the stable production alias remains on the earlier twelve-scene release.
- **Direct deployment URL:** `https://the-world-of-you-birthday-storybook-4ibr1qnh1.vercel.app/`.
- The previous deployment `dpl_7uEcsDcCFbYvGoa8FAATfu65M5RQ` remains marked as a rollback candidate.
- **Security action required:** The Vercel credential supplied in chat for the earlier twelve-scene deployment was used by the CLI. Treat it as exposed and revoke it now; no revocation has been confirmed. No credential is stored in the workspace; use the connected Vercel integration for future deployment operations.

## Supporting reports

- `GIFT_QA_REPORT.md` — detailed local interaction, responsive, keyboard, storage, reduced-motion and screenshot results for the new gift expansion.
- `PERFORMANCE_REPORT.md` — current local bundle and asset sizes; no unsupported FPS/device-memory claims.
- `ACCESSIBILITY_REPORT.md` — semantic, keyboard, focus, reduced-motion checks and limitations.
- `ASSET_MANIFEST.md` — scene art, fonts, owner-media slots, and final screenshot inventory.
