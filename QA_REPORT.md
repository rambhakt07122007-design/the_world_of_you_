# QA Report — The World of You

**Current source of truth:** `FINAL_QA_REPORT.md` covers the twelve-scene implementation and the earlier production smoke test. `GIFT_QA_REPORT.md` covers the current local 17-experience Gift Atelier expansion.

## Current local source

- `npm run build` passed for the current source: TypeScript + Vite, 2,092 modules transformed.
- `npm audit --audit-level=moderate` found 0 vulnerabilities.
- The Gift Atelier passed interaction checks for all 17 experiences; its collection was checked at 360–1920 px, and every gift dialog was checked at 360 × 800. No browser errors, console errors, HTTP errors or failed requests were observed in that run.
- Seventeen desktop screenshots (one per gift) are in `docs/screenshots/gifts/`.
- The screenshots and local QA do **not** imply that the new Gift Atelier code is deployed.

## Existing production release

The Vercel production alias [the-world-of-you-birthday-storybook.vercel.app](https://the-world-of-you-birthday-storybook.vercel.app/) still serves the previously verified twelve-scene release, deployment `dpl_9QT11nqNWa6tDXHyNk9c3AYoUMjU` (**READY / PROMOTED**, production). Direct deployment URL: [the-world-of-you-birthday-storybook-4ibr1qnh1.vercel.app](https://the-world-of-you-birthday-storybook-4ibr1qnh1.vercel.app/).

That release’s focused smoke test returned HTTP 200 for the home page and a fresh `#timepiece` deep link, with all twelve scene layers and no broken images, page errors, HTTP errors or failed requests. Gift Atelier’s latest global-audio and Birthday Ballroom updates are deployed as a Vercel **preview only** (`dpl_5gXRjLs1zbJo1eTENg8UxVNz8CR2`, READY/STAGED) at [the preview URL](https://the-world-of-you-birthday-storybook-7ythm9x51.vercel.app/). The remote build passed, but Vercel access protection redirected the hosted page check to sign-in, so no hosted UI interaction test was possible. The production alias remains unchanged; no production promotion occurred.

## Scope and limitations

No formal axe/WCAG certification, screen-reader session, formal contrast measurement, or real-device GPU/memory/FPS/battery profile is claimed. Personal photo and audio slots remain intentionally empty pending owner-supplied or appropriately licensed media.

**Security follow-up:** A credential used during a previous deployment must be revoked by the user. It was not reused or stored for this work. Use only the connected Vercel integration for future deployment operations.
