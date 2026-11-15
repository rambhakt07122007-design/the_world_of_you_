# Performance & Resource Report — Cinematic Storybook + Gift Atelier

> **Current native-3D build:** see `START_HERE.md` and `FINAL_IMPLEMENTATION_REPORT.md` for current scope, new browser evidence and limitations. Earlier findings/deployment descriptions below are historical. Current core QA: 12/12 pass; final native rose/crown/portal QA: 3/3 pass. No production deployment of this transformation has occurred.


**Local measurements verified:** 4 November 2026 (Asia/Kolkata)  
**Latest Vercel preview build:** READY/STAGED; 2,092 modules transformed in 4.05 seconds, with `npm ci` reporting 0 vulnerabilities. Scope: current local React/Vite production build and prior Playwright/Chromium observations. Bundle measurements below are local, not a real-device GPU, memory, battery, or FPS profile.

## Production build

`npm run build` — **passed** on the current source (TypeScript + Vite; 2,092 modules transformed; fresh Vite build on 4 November reported 3.68 seconds). `npm audit --audit-level=moderate` — **0 vulnerabilities**. No dependency was added for the gift experiences.

Latest Vite chunk sizes (raw / gzip):

| Output | Raw | Gzip |
|---|---:|---:|
| Main JS (`index-Ph5aShVX.js`) | 325.48 kB | 98.25 kB |
| Additional JS (`index-D4-8ALNT.js`) | 70.43 kB | 27.68 kB |
| Additional JS (`index.es-CPibn7Cb.js`) | 45.14 kB | 10.98 kB |
| Dynamic ScrollTrigger chunk (`ScrollTrigger-BrDuEirF.js`) | 43.55 kB | 18.11 kB |
| CSS (`index-DbZh-2sU.css`) | 190.86 kB | 43.06 kB |
| **JS subtotal** | **484.60 kB** | **155.02 kB** |

The final `dist/` directory occupies **2,470,372 B** on disk. The seventeen Gift Atelier screenshot PNGs are documentation-only and are not part of the runtime bundle.

## Scene and image budgets

- One fixed `aria-hidden` stage contains 12 visual layers; chapter copy and controls remain in normal document flow. Only active and immediate-neighbor scene art is eligible to load.
- Three optimized scene backgrounds total **301,326 B**: invitation 92,786 B, observatory 70,780 B, ballroom 137,760 B. Each is WebP at 1376 × 768 and below the 300 KB per-image target.
- The existing self-hosted WOFF2 set totals **265,972 B**. No runtime Google Fonts/GStatic requests are used.
- Gift experiences use the existing local scene/postcard art, DOM, CSS, SVG/icons and one pointer-wipe canvas. No Three.js/WebGL/physics library or remote media is shipped.
- The finale scene has CSS dawn/starfield layers and does not download the garden image a second time. The Gift 17 decorative sky is pointer-inert so it cannot cover controls.
- The flipbook and GSAP/ScrollTrigger retain their existing dynamic-loading behavior; reduced-motion initial scene load does not fetch the ScrollTrigger chunk.

## Browser observations

Playwright 1.56.1 with Chromium tested the local Vite production preview:

- The twelve-scene baseline passed 96 settled scene checks across **360, 390, 430, 768, 1024, 1280, 1440 and 1920 px**. No horizontal overflow, clipped visible controls, failed requests, browser-console/page errors, broken active scene assets or external requests.
- The Gift Atelier grid was checked at those same eight widths: **0 px horizontal overflow**. Each of 17 dialogs also had **0 px horizontal overflow at 360 × 800**.
- Gift interactions, accessible names, keyboard/focus restoration, local-storage persistence/recovery, empty-media behavior and reduced motion passed; details are in `GIFT_QA_REPORT.md`.
- No page errors, console errors, HTTP responses ≥400 or failed requests occurred in the Gift Atelier suite.
- Gift progress survives reload; duplicate/unknown storage data is filtered; malformed JSON falls back safely.
- Reduced-motion flower sparkle computes to `animation-name: none` / `0s`. The scene engine remains static/discrete under reduced motion; prior scene QA verified clock hands and invitation/cake states.
- Scene-engine trigger inventory in development: 12 depth tracks + 11 scene transitions + 9 heading reveals = **32**. On runtime reduced-motion change, cleanup returned the count to **0**; restoring standard motion recreated one set of 32 (no duplicate trigger set).

## Limits and follow-up

- No continuous frame-rate, CPU, memory, layout-shift, battery or real-device profiling was performed. A smooth Chromium smoke pass is not a device-level performance guarantee.
- Screenshots in `docs/screenshots/` are large documentation PNGs and are not deployed as runtime assets.
- The live production alias still serves the earlier twelve-scene release. Its prior HTTP 200 and `#timepiece` checks do not verify Gift Atelier interactions.
- Gift Atelier is deployed as a preview only; its Vercel build passed, but access protection prevented a hosted interaction smoke test. Deployment identity and the required credential revocation follow-up are in `PROJECT_PROGRESS.md`.
