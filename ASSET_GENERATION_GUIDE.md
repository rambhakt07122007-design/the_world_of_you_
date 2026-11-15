# Asset Generation Guide — Cinematic Birthday Universe

**Status:** Asset briefs executed; optimized environments integrated in the shared stage.  
**Source-of-truth audit:** `PROJECT_AUDIT.md`; final files and sizes are listed in `ASSET_MANIFEST.md`.

## 1. Asset principles

- Use original owner-provided media for real memories. There are currently no supplied gallery photographs or audio tracks; leave the editable empty slots in place.
- Never generate a photo/likeness of Bhumi or Rudra, a fake couple scene, fake conversation screenshot, or purported historical memory. Generated environmental illustrations are allowed only as clearly decorative/set-dressing art.
- Keep future postcards visibly hypothetical. Their existing illustrations are speculative, not documentation of travel or promises.
- Prefer existing local assets, CSS atmosphere and SVG/CSS geometry before generating new files. Keep all fonts/images local; no runtime CDN/API fetch.
- Record provenance, format, dimensions, file size, licensing/usage notes and intended scene in `ASSET_MANIFEST.md` when assets are added.

## 2. Existing local assets

| Current asset | Use | Notes |
|---|---|---|
| `public/assets/backgrounds/birthday-garden.webp` | Birthday Garden only | Existing environmental art; used as the Garden scene backdrop and intentionally not reused in the finale. |
| `public/assets/birthday/invitation-envelope.webp` | Invitation detail | Decorative envelope still; do not replace the interactive CSS-built envelope. |
| `public/assets/paper/writing-desk.webp` | Letter Room | Existing desk image; reuse, with no new fake letter/photo. |
| `public/assets/postcards/*.webp` (four files) | Future Postcards | Existing illustrated, speculative environments. |
| `public/assets/fonts/*.woff2` (six files) | Typography | Self-hosted Playfair Display, Cormorant Garamond, DM Sans, Caveat; retain all four OFL texts. |
| `gallery/`, `audio/`, `gifts/`, `flowers/`, `objects/` | Editable mounts | Empty `.gitkeep` directories are intentional until owner media is supplied. |

## 3. Generated environmental art additions

Three standalone room environments were generated, inspected, converted to optimized WebP, and wired to their scene anchors. They contain no text, logos, people, faces, hands, framed photos, or readable letters. The prompt briefs below record the intended composition and content limits.

### A. Invitation Room — `public/assets/scenes/invitation-room.webp`

**Prompt:** “Wide cinematic editorial illustration, intimate antique writing desk at late afternoon, a single elegant sealed envelope and blank cream paper, brass candleholder, fountain pen, soft window light, rose and champagne accents, tactile linen paper and walnut, subtle atmospheric depth, painterly realistic still-life, refined birthday storybook, quiet composition with clear central negative space, no people, no readable writing, no lettering, no logo, no collage, landscape 16:9.”

Use behind the invitation card at low contrast. The visible envelope interaction remains DOM/CSS and keyboard operable.

### B. Memory Observatory — `public/assets/scenes/memory-observatory.webp`

**Prompt:** “Wide cinematic interior of a small antique observatory at blue hour, brass telescope pointed through a tall arched window toward a deep indigo star field, a delicate celestial clock/orbit instrument, antique gold glints, velvet navy shadows, quiet storybook realism, restrained constellations, depth from foreground instrument to distant sky, leave a calm open central area for readable text, no people, no portraits, no readable letters/numbers, no logo, no collage, landscape 16:9.”

The scene is symbolic environmental art; milestone dates and relationship content come only from `chronosContent.ts`.

### C. Birthday Ballroom — `public/assets/scenes/birthday-ballroom.webp`

**Prompt:** “Wide cinematic birthday ballroom prepared before guests arrive, warm candlelight, refined merlot curtains, champagne-gold chandelier, rose and ivory garlands, a simple birthday cake stand near the center-right with no writing, gentle floor reflections, painterly realistic storybook illustration, elegant and intimate rather than grand/corporate, rich depth with foreground drapery and distant warm lights, leave open space at center-left for text, no people, no faces, no readable text, no logo, no collage, landscape 16:9.”

The cake ritual remains an accessible React control/SVG. This art is only a scene backdrop and must not imply a particular party history.

## 4. Generation, conversion, and quality targets

- Generate each image as an individual wide image. Do not generate a collage, contact sheet, set of variations in one image, or text-bearing asset.
- Save original generation output outside the source tree only if needed for reproducibility; ship optimized derivatives in `public/assets/scenes/`.
- Convert to WebP at a practical quality setting (start around 80–84), resize to the largest required viewport (e.g. 1920×1080 or a similarly wide composition), strip unnecessary metadata, and visually inspect at desktop and mobile crops.
- Initial per-background goal: **≤300 KB WebP**, with a documented exception if visual quality requires more. Avoid adding all full-size art to the initial network path; stage should load the invitation plus one adjacent scene, then active/adjacent art on demand.
- Verify each derivative is valid, dimensions are recorded, alt is empty only because the image is decorative and its scene has no essential information, and no added external image requests occur.
- Implemented scene outputs: all are 1376 × 768 WebP; invitation 92,786 B, observatory 70,780 B, ballroom 137,760 B. Each remains under the 300 KB target.
- Do not use generated environmental art as a substitute for personal photos or captions.

## 5. CSS/SVG assets preferred over raster generation

Use CSS gradients/clip paths or small inline SVG for: scrapbook page edges, observatory rings/stars (in addition to the room background), gallery blank frames, wish-garden horizon, gift shelves, vinyl grooves, postcard travel lines, finale starfield. Keep these shapes decorative, lightweight and `aria-hidden` through the stage.

## 6. Audio and font policy

- `public/assets/audio/` is currently empty. Do not fabricate or synthesize a personal birthday track. Preserve paused-by-default/no-autoplay controls and a truthful “no track supplied” state.
- Keep the existing four locally licensed font families and SIL OFL license files. No remote font/image hosting.
- If the owner supplies audio/photos later, add source, format, file-size, license/permission, alt/caption, and accessibility notes to `ASSET_MANIFEST.md`.

## 7. Deployment hygiene

`vercel-upload/` is a legacy static export and is not a scene asset. Exclude it from deployment uploads; do not merge its inlined code or generated chunks into the new app. Keep documentation/screenshots in the workspace, not the deployed runtime.
