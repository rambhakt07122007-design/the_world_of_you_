# Design research — The World of You

**Direction:** a premium interactive birthday storybook built from tactile paper, a small garden world and owner-authored memories. The research brief is implemented as a restrained, editorial experience rather than a generic birthday template.

## Experience principles

1. **Treat personal truth as design material.** Keep the three verified dates and the supplied names/copy; leave unknown memories, images and recordings empty instead of filling them with synthetic content.
2. **Make the UI feel held, not futuristic.** Use paper edges, pressed seals, ruled pages, Polaroid mounts, a desk and a flipbook as the primary metaphors.
3. **Give each chapter a distinct scene.** The invitation is intimate; the garden opens the world; the scrapbook and desk are quiet; wishes and gifts invite touch; the cake and finale build toward celebration.
4. **Use motion as feedback.** Every animated response follows an action (open, turn, bloom, unwrap, light, wish or replay). Decorative motion stays soft and nonessential.
5. **Keep sound and personal media under owner control.** Sound is off by default; no audio is bundled, streamed, recorded or autoplayed.

## Visual system

### Palette

| Token | Value | Role |
|---|---|---|
| `--color-cream` | `#f5eee5` | Main page ground |
| `--color-ivory` | `#fffaf2` | Clean paper and cards |
| `--color-paper` | `#fbf5eb` | Editorial paper surface |
| `--color-paper-deep` | `#eadcc8` | Fold, edge and shadow contrast |
| `--color-blush` | `#efd4d2` | Soft warmth |
| `--color-blush-deep` | `#d7a2a1` | Pressed blush |
| `--color-rose` | `#b8747d` | Focus, CTA and accent |
| `--color-rose-deep` | `#89545c` | Deeper accent/active state |
| `--color-peach` | `#e8bda5` | Warm secondary accent |
| `--color-gold` | `#bd965c` | Champagne detail |
| `--color-gold-soft` | `#e1c994` | Highlight |
| `--color-sage` | `#9aa58c` | Garden foliage |
| `--color-ink` | `#41322f` | Primary text |
| `--color-ink-soft` | `#705951` | Secondary text |
| `--color-muted` | `#8c776b` | Quiet labels |

Tokens live in `src/styles/designTokens.css`; legacy semantic aliases keep the existing chapter styles consistent. Typography scale, content width, border radii, shadows and easing values are defined alongside the colors.

### Typography

All four requested families are self-hosted from the Google Fonts distributions as Latin variable WOFF2 fonts. The CDN is not requested at runtime.

- **Playfair Display** — large emotional titles and chapter headings.
- **Cormorant Garamond** — editorial paragraphs, dates, letter body and captions.
- **DM Sans** — navigation, controls, metadata and small labels.
- **Caveat** — short handwritten annotations, wishes and the signature only.

System serif/sans/cursive fallbacks remain in the CSS stack. Font files use `font-display: swap`; the three primary faces are preloaded in `index.html`. Matching SIL Open Font License files are included under `public/assets/fonts/`.

## Chapter dramaturgy

| Order | Scene | Design cue | Interaction |
|---:|---|---|---|
| 01 | Invitation | Cream card, envelope, seal, floating dust | Open or skip; reduced-motion path is immediate |
| 02 | Garden | Existing illustrated pavilion, layered wash, flowers, balloons, petals, fireflies | Enter the book; scroll/parallax reveals |
| 03 | Scrapbook | Deep-brown cover, ruled paper, archival labels | PageFlip controls, swipe and arrow keys |
| 04 | Timepiece | Pocket-watch face plus verified date nodes | Select a real date marker; live elapsed time |
| 05 | Letters | Illustrated writing desk, five sealed paper envelopes | Open a letter; native dialog and Escape close |
| 06 | Photo wall | Six hanging Polaroid mounts | Open a mount/lightbox; previous/next controls |
| 07 | Wish garden | Ten CSS-bloom flowers, gentle pollen and ground | Select a flower; announce the wish politely |
| 08 | Gift room | Seventeen distinct box/book/bottle/envelope/star/heart forms | Open a gift; local-storage progress |
| 09 | Music room | Vintage vinyl console and accessible transport controls | Opt in to sound; local-file playback only |
| 10 | Cake | Hand-drawn SVG layer cake and five candles | Light, make a private wish, blow out by button |
| 11 | Future postcards | Four generic landscape illustrations, stamped “imagined” | Open a speculative detail dialog |
| 12 | Finale | Garden reprise, warm frame, confetti and star accents | Replay celebration or replay the invitation |

## Motion and interaction decisions

- **GSAP + ScrollTrigger** is dynamically imported by `BirthdayGarden.tsx` for one entrance timeline, a restrained hero parallax and section-heading reveals. CSS remains the graceful fallback if that optional module fails.
- **`react-pageflip`** provides the scrapbook’s tactile page turn. It is lazy-loaded after the book nears the viewport; arrow buttons, arrow keys and swipe are supported. The flip duration becomes near-instant with reduced motion.
- **CSS/SVG** handles the envelope, wax seals, layered paper, gift forms, flowers, pocket watch, vinyl, cake and confetti; this avoids unnecessary 3D model downloads.
- **No WebGL scene is shipped.** A CSS/SVG scene met the design need without adding a canvas/GPU dependency. This is a deliberate performance/accessibility choice, not an omitted or falsely claimed React Three Fiber implementation.
- Scroll is native. The page does not hijack scrolling or auto-play media. Motion preference is checked in JavaScript and CSS; reduced-motion mode removes ambient particles and minimizes transitions.

## Asset policy and sourcing

- Existing generated-but-generic envelope, garden and desk illustrations remain atmospheric set pieces.
- Four newly generated, person-free WebP landscapes are used only for postcard scenes. Their captions and dialogs explicitly say they are imagined, not memories or promises.
- No personal photos, faces, handwriting or audio were generated. The six Polaroid slots, four empty letters, editable gift messages and three audio slots remain owner-supplied content points.
- UI icons come from `lucide-react`; the flower seal and cake are inline/vector/CSS. No third-party image, audio or social link is embedded.
- Raster illustrations use WebP, known dimensions and below-the-fold lazy loading. The invitation and garden hero are eager/high-priority because they appear before the first interaction.

## Responsive and accessibility research notes

- The page is tested at 1440 px, 390 px and 320 px viewport widths; document width matches each viewport after the entrance animation.
- Navigation includes a skip link, quick anchors, a keyboard-operable chapter index, active section state and visible focus styling.
- Buttons have accessible names; decorative ornaments are hidden from assistive technology; informative images include alt text and dimensions.
- Native `<dialog>` provides modal semantics and Escape-to-close. Wish/gift progress uses live regions; the scrapbook exposes a keyboard path.
- Reduced motion removes ambient particle layers, skips the invitation sequence, shortens the page flip and uses the global motion override.
- No formal WCAG certification is claimed; see `QA_REPORT.md` for verification scope and limitations.
