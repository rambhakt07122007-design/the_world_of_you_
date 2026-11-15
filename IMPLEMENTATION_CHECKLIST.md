# Implementation checklist — The World of You

## Audit, design and build sequence

- [x] Complete the repository/live-site audit before application-source changes; record baseline and risks.
- [x] Complete `DESIGN_SYSTEM.md`, `SCENE_ARCHITECTURE.md`, `ASSET_GENERATION_GUIDE.md`, and `ANIMATION_SPECIFICATION.md` before implementation.
- [x] Preserve canonical IDs/content, then add the data-driven 12-scene catalog, fixed stage, GSAP/ScrollTrigger transitions, CSS observer fallback and reduced-motion handling.
- [x] Keep content and controls in the original semantic React chapter components; preserve natural document scrolling.
- [x] Create three individual room environments (invitation, observatory, ballroom) and document dimensions/provenance; do not use personal-photo/audio substitutes.

## Scene order and interface

- [x] Invitation Room → Birthday Garden → Scrapbook → Memory Observatory → Letter Room → Memory Gallery → Wish Garden → Gift Atelier → Music Lounge → Future Postcards → Birthday Ballroom → Finale.
- [x] Active chapter label, active quick/index navigation state, reading progress, direct-hash landing and invitation/garden replay hashes.
- [x] Finale uses a distinct CSS dawn/starfield environment; remove reused birthday-garden image and obsolete art selectors.
- [x] Responsive scene crops and accessible controls at all required widths.

## Existing chapter interactions preserved

- [x] Skippable animated invitation with reduced-motion shortcut and replay.
- [x] Four-spread/eight-content-page scrapbook with lazy page-flip library, controls, arrow-key navigation and swipe.
- [x] Observatory elapsed time from 11 May 2025 in `Asia/Kolkata`, verified-date markers and reduced-motion-stopped clock hands.
- [x] Five letter envelopes; supplied birthday draft retained, four owner-written entries remain empty; native dialog supports Escape and focus return.
- [x] Six Polaroid mounts and accessible viewer; no fabricated photographs.
- [x] Ten wish buttons release only the wishes preserved in the source content.
- [x] Seventeen distinct gift experiences with independent open/replay, safe/deduplicated local progress and truthful blank private-copy/media states; existing source messages retained.
- [x] Local-file music player with explicit sound opt-in, no autoplay and truthful empty-media state; the shared top-bar mute preference gates the Music Lounge and both gift audio players, pauses playback on mute, and never resumes it automatically.
- [x] Five-candle cake ritual; private wish state and button-driven blow-out; decorative balloons and a finite wish-triggered fireworks burst; reduced-motion support; no microphone access.
- [x] Four generic landscape postcards remain speculative; each detail identifies itself as not a fact, memory or promise.
- [x] Finale message retains source-draft attribution, celebration replay and invitation replay.

## Content, assets and safety

- [x] Keep personal copy/data in `src/content/chronosContent.ts`.
- [x] Preserve Bhumi/Rudra, first connection 11 May 2025, proposal 17 July 2025, birthday 17 November with no inferred year.
- [x] Keep gallery and audio empty until owner-supplied/appropriately licensed media is provided; no AI faces or fake memories.
- [x] Self-host Playfair Display, Cormorant Garamond, DM Sans and Caveat WOFF2 files with SIL OFL texts; no font-CDN requests.
- [x] Document that the canonical ZIP was not present in the workspace.

## Verification

- [x] Current TypeScript/Vite production build; 2,092 modules transformed.
- [x] `npm audit --audit-level=moderate`: zero vulnerabilities.
- [x] Production-preview responsive sweep at 360, 390, 430, 768, 1024, 1280, 1440 and 1920 px: 96 settled scene checks, no overflow/clipped visible controls/errors/failed/external requests.
- [x] Gift collection checked at all eight widths with 0 px overflow; each of 17 dialogs checked at 360 × 800 with no horizontal overflow.
- [x] Twelve-scene forward/reverse traversal in React StrictMode; no duplicate trigger set. Reduced motion switches from 32 triggers to 0 and restores one 32-trigger set.
- [x] Existing chapter interaction suite for index/focus, invitation, scrapbook, observatory, letters/dialogs, gallery, wishes, empty audio, speculative postcards, cake ritual and finale replay.
- [x] Gift Atelier interaction suite: all 17 distinct experiences, media/content-empty states, keyboard/focus, local-storage persistence/deduplication/corrupt-data recovery and reduced motion; 17 desktop screenshots in `docs/screenshots/gifts/`.
- [x] Initial deep-hash landing for timepiece, birthday-cake and finale anchors; replay/open hash synchronization.
- [x] Refresh desktop screenshots for all twelve scenes and mobile invitation/observatory/finale.
- [x] DOM accessibility smoke for names, image alt attributes, focusable/`aria-hidden` content and dialogs. No formal axe/WCAG or screen-reader certification claimed.

## Deployment status

- [x] Identify the existing Vercel project and stable alias.
- [x] Deploy the earlier twelve-scene update to Vercel production: `dpl_9QT11nqNWa6tDXHyNk9c3AYoUMjU` (READY / PROMOTED).
- [x] Smoke-test the stable alias and a fresh `#timepiece` deep link for that release: HTTP 200, twelve scene layers, no broken images or browser/network errors, Observatory selected for the deep link.
- [x] Complete the new Gift Atelier build and local QA.
- [x] Deploy the latest Gift Atelier source as **preview only** via the connected Vercel integration: `dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2` (READY / STAGED), [preview URL](https://the-world-of-you-birthday-storybook-7ythm9x51.vercel.app/); remote build passed (2,092 modules, 4.05s). Access protection redirects hosted checks to sign-in, so hosted UI interaction testing is unavailable. Production remains unchanged.
- [ ] Obtain explicit authorization before promoting the Gift Atelier preview to staging or production; use only the connected Vercel integration.
- [ ] Revoke the credential supplied in chat and used by the previous deployment CLI. Do not paste raw tokens in chat; use the connected Vercel integration for future operations.
- [ ] Add photos, letters, gift copy or audio only if owner-supplied.
