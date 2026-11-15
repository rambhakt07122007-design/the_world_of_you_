# The World of You — cinematic build

> **Current local 17-world implementation:** `3D_IMPLEMENTATION_REPORT.md` and `3D_TRANSFORMATION_AUDIT.md` supersede historical scope counts below. All 17 gifts now have native scene integrations; this is not a claim of complete photoreal art direction. Vercel production remains the earlier deployment. Preview the current built project on port 4182.


> **Latest local refinement:** see `IMPLEMENTATION_REPORT.md` and `WEBSITE_AUDIT.md`. The new letter/postcard changes are implemented locally and previewed on port 4182, but **have not replaced the earlier Vercel production deployment**. Deployment statements below refer to the previous build.


## Production deployment confirmed

Current native 3D build deployed as `dpl_HKNiufj8nWEQBppbDDK21iEskN8A`, READY / PROMOTED. Live: https://the-world-of-you-birthday-storybook.vercel.app/ . 80 source/public files uploaded; stable alias serves `/assets/index-DCop_qA0.js`, matching the local build. Hosted desktop Chromium smoke passed: garden 3D renders, Wish 01 selection works, no page errors. Evidence: `qa-production.json`. This is not a full hosted regression or hardware microphone test. Previous production `dpl_HjUU7Q3s5RWL4abb6cfEtKTE7RDe` remains the rollback reference. Earlier undeployed statements are historical.


## Run

Use Node.js 20.19+ (or a compatible newer version).

```sh
npm ci
npm run dev -- --port 4181 --strictPort
```

Open the URL Vite prints. The application preserves all twelve chapters and seventeen gift entries. New real-time scenes: Wish Garden, Letter Room, Observatory, Cake, and gifts 01/03/08/09/17. Select Low detail if your device struggles. Controls/content remain usable if WebGL fails.

## Check

```sh
npm run build
npx playwright install chromium
# Keep the dev server running on port 4181 in another terminal.
npm run test:browser
```

The Playwright suite uses Chromium/software WebGL and can take several minutes. Hardware microphone accuracy and performance require actual-device testing. Microphone access is optional and may be blocked by embedded-preview permission policy; use a top-level HTTPS page or the manual fallback.

## Assets

Seven original static GLB snapshots live in `public/assets/models/`. Re-export while Vite runs on 4181:

```sh
npm run assets:export
```

Runtime models, materials, shaders and choreography are authored in `src/three/`. GLBs do not contain the custom GLSL effects. Generated build output and dependencies are not included in the source package.

## Personal content

Edit only approved real content in:
- `src/content/chronosContent.ts`
- `src/content/giftsContent.ts`

Photos, audio, private letters, reasons, coupons and future hopes remain explicitly blank where missing. Do not replace them with generated personal memories.

## Honest scope

Read `FINAL_IMPLEMENTATION_REPORT.md` for completed implementation, tests, limitations and the individual status of all seventeen gifts. This is a substantial partial transformation, not the complete photorealistic master-prompt target. Twelve gift experiences still need native 3D conversions, and several sections remain their earlier illustrated implementations.

This build has not been deployed. Earlier production details describe an older snapshot. No Vercel credential is included in the source package.
