# Asset manifest — The World of You

## Local animation additions

- `src/world/CakeBakingJourney.tsx`: project-authored inline SVG for Gather, Mix, Bake and Decorate; finite GSAP flourishes using the existing dependency. No downloaded artwork.
- `src/world/BirthdayCake.tsx`: authored SVG wick-smoke paths and existing cake artwork retained.
- `src/world/Storybook.tsx`: ephemeral Web Audio noise synthesized locally; no audio file, external request, recording, microphone permission or third-party license. Opt-in through the global sound preference; suppressed for reduced motion.


**Verified:** 3 November 2026 (Asia/Kolkata). This manifest covers runtime artwork, self-hosted type, owner-media slots, and the refreshed local QA screenshots. Raster art is illustrative only; no asset is presented as a photograph, memory, or recording of Bhumi or Rudra.

## Scene environments

| File | Dimensions | Format / size | Purpose | Source / notes |
|---|---:|---|---|---|
| `public/assets/scenes/invitation-room.webp` | 1376 × 768 | WebP · 92,786 B | Invitation Room scene | Generated environmental illustration; intimate desk, envelope and window light; no people or readable text. |
| `public/assets/scenes/memory-observatory.webp` | 1376 × 768 | WebP · 70,780 B | Memory Observatory scene | Generated environmental illustration; observatory/telescope/celestial instruments; no people or personal details. |
| `public/assets/scenes/birthday-ballroom.webp` | 1376 × 768 | WebP · 137,760 B | Birthday Ballroom scene | Generated environmental illustration; candlelit merlot/champagne room; no people or readable text. |
| `public/assets/backgrounds/birthday-garden.webp` | 1376 × 768 | WebP · 178,518 B | Birthday Garden scene only | Existing generic flower garden and pavilion; not reused by the finale. |

All three new backgrounds were generated as individual assets, converted to WebP, visually reviewed, and kept below the 300 KB per-background target. They are decorative and loaded only for their active/adjacent scene layers. Their empty alt text is intentional; chapter content remains in the semantic document.

## Existing chapter illustrations and postcards

| File | Dimensions | Format / size | Purpose / notes |
|---|---:|---|---|
| `public/assets/birthday/invitation-envelope.webp` | 928 × 1152 | WebP · 26,078 B | Decorative envelope still-life in the opening invitation; the interactive envelope remains DOM/CSS. |
| `public/assets/paper/writing-desk.webp` | 1200 × 896 | WebP · 85,038 B | Generic blank-paper, pen and flower vignette in Letter Room; no personal writing. |
| `public/assets/postcards/mountain-morning.webp` | 1376 × 768 | WebP · 216,920 B | “A mountain morning” speculative postcard. |
| `public/assets/postcards/sea-blue-hour.webp` | 1376 × 768 | WebP · 213,318 B | “The sea at blue hour” speculative postcard. |
| `public/assets/postcards/unnamed-city.webp` | 1376 × 768 | WebP · 268,290 B | “A city we haven't named” speculative postcard. |
| `public/assets/postcards/home-whatever-shape.webp` | 1376 × 768 | WebP · 219,378 B | “Home, whatever shape” speculative postcard. |

The four postcard landscapes contain no people, faces, text, logos or personal photos. Both the index and detail dialog identify them as imagined possibilities, not shared events, facts or promises.

## Self-hosted fonts and licenses

Six Latin WOFF2 files are served locally. Combined font payload: **265,972 B**. The exact SIL Open Font License 1.1 texts are stored alongside each family; runtime Google Fonts/GStatic requests are not used.

| File | Format / size | Family / license |
|---|---|---|
| `public/assets/fonts/playfair-display-latin-variable.woff2` | WOFF2 · 38,404 B | Playfair Display variable, normal; `OFL-Playfair-Display.txt` |
| `public/assets/fonts/playfair-display-italic-latin-variable.woff2` | WOFF2 · 38,804 B | Playfair Display variable, italic; same license |
| `public/assets/fonts/cormorant-garamond-latin-variable.woff2` | WOFF2 · 37,640 B | Cormorant Garamond variable, normal; `OFL-Cormorant-Garamond.txt` |
| `public/assets/fonts/cormorant-garamond-italic-latin-variable.woff2` | WOFF2 · 39,260 B | Cormorant Garamond variable, italic; same license |
| `public/assets/fonts/dm-sans-latin-variable.woff2` | WOFF2 · 36,932 B | DM Sans variable; `OFL-DM-Sans.txt` |
| `public/assets/fonts/caveat-latin-variable.woff2` | WOFF2 · 74,932 B | Caveat variable; `OFL-Caveat.txt` |
| `public/assets/fonts/OFL-*.txt` (4 files) | Plain text · 17,703 B total | License texts for the four families. |
| `public/assets/fonts/README.md` | Markdown · 341 B | Font provenance and local-serving note. |

## CSS/SVG-rendered interface artwork

No separate raster assets are used for the cake, pocket watch, gifts, wax seals, flowers, Polaroid frames, vinyl player, page flourishes, scene atmospheres, or finale starfield. These are rendered with semantic HTML, CSS, inline SVG and `lucide-react` icons. The finale uses its own CSS dawn scene and does not load `birthday-garden.webp`.

## Owner-supplied media slots

| Path | Status / use |
|---|---|
| `public/assets/gallery/` | Empty by design. Six Polaroid mounts await owner-supplied photographs and accurate captions. No AI faces or substitute “memory” art. |
| `public/assets/audio/` | Empty by design. Three local audio entries remain paused and disabled until owner-provided/appropriately licensed files are added. |
| `public/assets/flowers/`, `public/assets/gifts/`, `public/assets/objects/` | Optional future owner assets; current visuals are CSS/SVG. |

`.gitkeep` files in these directories are empty folder markers and are not displayed. No personal photos or audio were supplied; do not invent either.

## Refreshed QA screenshots

These Playwright PNGs capture the local production build after the scene system and final visual fixes. They are documentation artifacts, not runtime assets. The earlier pre-scene production capture is kept for comparison; obsolete intermediate scene screenshots were removed.

| File | Capture | Dimensions | PNG size |
|---|---|---:|---:|
| `docs/screenshots/00-production-before-scenes.png` | Production baseline before the cinematic scene update | 1440 × 1000 | 959,999 B |
| `docs/screenshots/01-invitation-room.png` | Invitation Room | 1440 × 900 | 1,315,749 B |
| `docs/screenshots/02-birthday-garden-scene.png` | Birthday Garden | 1440 × 900 | 1,516,582 B |
| `docs/screenshots/03-scrapbook-scene.png` | Scrapbook | 1440 × 900 | 961,126 B |
| `docs/screenshots/04-memory-observatory-scene.png` | Memory Observatory | 1440 × 900 | 1,100,948 B |
| `docs/screenshots/05-letter-room-scene.png` | Letter Room | 1440 × 900 | 927,397 B |
| `docs/screenshots/06-memory-gallery-scene.png` | Memory Gallery | 1440 × 900 | 944,939 B |
| `docs/screenshots/07-wish-garden-scene.png` | Wish Garden | 1440 × 900 | 722,384 B |
| `docs/screenshots/08-gift-atelier-scene.png` | Gift Atelier | 1440 × 900 | 818,391 B |
| `docs/screenshots/09-music-lounge-scene.png` | Music Lounge | 1440 × 900 | 953,504 B |
| `docs/screenshots/10-future-postcards-scene.png` | Future Postcards | 1440 × 900 | 879,569 B |
| `docs/screenshots/11-birthday-ballroom-scene.png` | Birthday Ballroom | 1440 × 900 | 1,236,448 B |
| `docs/screenshots/12-finale-scene.png` | Finale | 1440 × 900 | 396,826 B |
| `docs/screenshots/mobile-01-invitation-room.png` | Invitation Room mobile crop | 390 × 844 | 304,468 B |
| `docs/screenshots/mobile-04-memory-observatory-scene.png` | Memory Observatory mobile crop | 390 × 844 | 311,036 B |
| `docs/screenshots/mobile-12-finale-scene.png` | Finale mobile crop | 390 × 844 | 129,893 B |

## Gift Atelier screenshots

The local production preview was captured at **1440 × 900** with one PNG for each distinct gift. These are documentation artifacts, not runtime assets.

| Gift | File | PNG size |
|---|---|---:|
| 01 · The Secret Letter | `docs/screenshots/gifts/01-secret-letter.png` | 472,840 B |
| 02 · A Jar of Reasons | `docs/screenshots/gifts/02-reason-jar.png` | 446,070 B |
| 03 · The Flower That Never Fades | `docs/screenshots/gifts/03-eternal-flower.png` | 390,991 B |
| 04 · Our Little Universe | `docs/screenshots/gifts/04-little-universe.png` | 444,538 B |
| 05 · Bhumi FM Exclusive | `docs/screenshots/gifts/05-bhumi-fm.png` | 441,490 B |
| 06 · The Memory Cinema | `docs/screenshots/gifts/06-memory-cinema.png` | 372,961 B |
| 07 · A Thousand Wishes | `docs/screenshots/gifts/07-thousand-wishes.png` | 396,807 B |
| 08 · The Queen’s Crown | `docs/screenshots/gifts/08-queens-crown.png` | 479,887 B |
| 09 · Open When… | `docs/screenshots/gifts/09-open-when.png` | 419,985 B |
| 10 · The Happiness Machine | `docs/screenshots/gifts/10-happiness-machine.png` | 443,995 B |
| 11 · A Little Adventure | `docs/screenshots/gifts/11-little-adventure.png` | 588,954 B |
| 12 · The Music of Us | `docs/screenshots/gifts/12-music-of-us.png` | 485,331 B |
| 13 · The Infinite Mirror | `docs/screenshots/gifts/13-infinite-mirror.png` | 425,986 B |
| 14 · The Birthday Coupon Book | `docs/screenshots/gifts/14-coupon-book.png` | 386,313 B |
| 15 · The Future Garden | `docs/screenshots/gifts/15-future-garden.png` | 387,307 B |
| 16 · The Secret Treasure Hunt | `docs/screenshots/gifts/16-treasure-hunt.png` | 384,179 B |
| 17 · The Ultimate Surprise | `docs/screenshots/gifts/17-ultimate-surprise.png` | 403,352 B |

Full responsive, accessibility-smoke, motion and interaction results are in `FINAL_QA_REPORT.md`, `GIFT_QA_REPORT.md`, and `ACCESSIBILITY_REPORT.md`. No real-device GPU, memory or screen-reader certification is claimed.

## Native procedural 3D assets

All models below are project-authored geometry, not downloaded models or personal likenesses. PBR-style standard/physical materials and seeded 128px canvas texture maps are generated in code. No external texture request. Runtime source is the canonical animated asset.

| Asset | Runtime path | Construction / optimization |
|---|---|---|
| Conservatory | `src/three/garden.ts` | Curved petal meshes (three botanical forms), hinged petals/leaves, staged stalk growth, instanced 4,500 / 8,500 / 14,000 grass blades, instanced foliage, branch/stone/hill geometry, articulated butterflies, pollen points; tiered DPR/shadows. Not photorealistic. |
| Cake / preparation / oven | `src/three/cake.ts` | Three sponge layers, filling, lathed frosting, tubular piped rosettes, eight berries, five wax candles, animated shader flames and point lights; preparation bowl/tin/batter and hinged oven. Mesh choreography is a visual approximation, not physics or food chemistry. |
| Paper desk | `src/three/letter.ts` | Three curved hinged panels, creases, triangular envelope flap, separating wax seal, wooden desk, pen/ink bottle/candle prop. No cloth physics. |
| Astronomical clock / portal | `src/three/celestial.ts` | Local-time hands, gears/pendulum, moon/stars; separate metallic portal rings with original GLSL ripple surface. |
| Eternal rose / crown | `src/three/botanicalGift.ts` | Seed/stem/leaves and 21 hinged curved petals; separate beveled eight-point crown with faceted gems and rosette-free metallic molding. |
| Generated texture helper | `src/three/runtime.ts` | Seeded noise textures, standard/physical material helpers; shared resources disposed once per renderer lifetime. |
| Three.js notice | `public/licenses/THREE-LICENSE.txt` | MIT notice copied from installed dependency. |

### GLB authoring snapshots
`public/assets/models/`: `garden.glb` (1,541,248 bytes), `cake.glb` (371,836), `letter-desk.glb` (99,012), `eternal-rose.glb` (131,852), `crown.glb` (398,944), `portal.glb` (175,348), `observatory.glb` (423,504).

Generated with `scripts/export-models.mjs` and `src/three/exportModels.ts` via the MIT Three.js exporter. Header verified as GLB. These are low-tier static geometry snapshots with small embedded textures, shared geometry and instancing where supported, not Draco/KTX compressed production assets. Runtime does not download them: it creates the same authored geometry lazily. Wind, flames, portal shader surfaces and choreography are runtime code, not embedded in the GLBs; unsupported shader surfaces are omitted from snapshots. External GLB-viewer visual round-trip validation has not been done.

Original personal content files and 26 pre-existing public files were byte-compared against backup: all unchanged (`qa-preservation.json`). New models/licenses are additive only.

## Native seventeen-world pass
Original authored geometry in `src/three/giftWorlds.ts`, reused/improved letter/botanical/crown/portal factories; shared R3F lifecycle `NativeGiftCanvas.tsx`. No proprietary models downloaded. Offline sequential native renders compressed into 17 WebP gallery previews; these are static previews of real geometry, not seventeen simultaneous WebGL instances. R3F9.8.2 package declares MIT; notice copied from official https://raw.githubusercontent.com/pmndrs/react-three-fiber/master/LICENSE into `public/licenses/REACT-THREE-FIBER-LICENSE.txt`. Three notice retained. Studio RoomEnvironment uses Three's licensed addon rather than copied third-party demo code. Missing reasons/audio/photos/promises remain missing. Historical seven GLBs are not the live runtime source for new gift worlds.
