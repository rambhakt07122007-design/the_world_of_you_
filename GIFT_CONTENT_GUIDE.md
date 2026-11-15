# Gift Content Guide

**Updated:** November 2026 (the owner's content pack was added; see `docs/CONTENT_PACK_INTEGRATION.md`)

## Sources of truth

- `src/content/packContent.ts` — the owner's content pack (`docs/content-pack/The_World_of_You_Complete_Missing_Content_Pack.pdf`) as typed data. It was imported word for word; edit it by hand from now on. It holds the main letter, the 17 reasons, 101 wishes, seven future postcards, the gift 01–08 dedications, the flower / universe / crown long dedications and reveal lines, the garden narration, the Memory Cinema and Bhumi FM copy and the website microcopy.
- `src/content/giftsContent.ts` — names, experience IDs, gift presentation, readiness flags and the private-copy slots the pack did not fill. Reasons and dedications are read from `packContent.ts`.
- `src/content/chronosContent.ts` — verified relationship dates, the existing source letter and messages, the ten source wishes, gallery/audio slots, the postcard layout and finale copy. The Letter Room, Future Postcards, Gallery and finale are built here from `packContent.ts`.

The experience code reads these modules directly. Do not copy personal text into component JSX; keep approved copy in content data so it remains reviewable and editable.

## What a visitor can and cannot see

The pack is ready-to-edit copy written by the pack's author. It is not a verified record of any private history, so the owner reads it before publishing. A **slot** is anything the pack marked `[EDIT]`, `[ADD ...]` or `[INSERT ...]`, or left to the owner. Slots are never shown to visitors: an empty slot renders nothing, or the pack's own placeholder line ("This message is waiting to be written…", "Add a real photograph here…", "Add an audio file to activate this player."). Writing real words into a slot makes them appear. Never paste an `[EDIT]` template into a visible field.

## Editable slots currently waiting for owner copy

| File / field | Slots | Rules |
|---|---:|---|
| `packContent.ts` → `packGiftSlots["09"…"17"].dedication` | 9 | The pack gave templates only. Read each gift's exact title in `giftsContent.ts`, then write 2–4 sentences. Mention only real details, or label the message as a wish, symbol or imagination. Shown as a quote at the top of the gift. |
| `packContent.ts` → `packGiftSlots["09"…"17"].revealLine` | 9 | One short line shown when the gift opens. |
| `packContent.ts` → `packLetter.optionalInserts[].text` | 4 | A real memory, an observed quality, an apology (only if wanted), a personal wish. The first is appended to the thank-you paragraph, the others become paragraphs after it. The `prompt` text is a note to the writer and is never shown. |
| `giftsContent.ts` → `openWhenLetters[].message` | 4 | Write an actual private letter for each, or leave it blank. A blank letter shows the pack's "waiting to be written" line. |
| `giftsContent.ts` → `couponEntries[].title` / `description` | 6 | Add only offers the owner explicitly approves. Blank coupons are intentionally not redeemable. |
| `giftsContent.ts` → `futureGardenLeaves[].text` | 8 | Future hopes only; do not present them as plans, events or promises. |
| `chronosContent.ts` → `letters` (four `kind: "empty"` envelopes) | 4 | The Letter Room's other four envelopes: add real words, or leave them. |
| `chronosContent.music.tracks[].src` | 3 | A local, properly licensed or owner-provided audio file. Never autoplay. No audio file exists, so Play stays disabled. |
| `chronosContent.gallery.photos[].src` / `caption` / `alt` | 6 | Genuine owner-supplied photos and accurate captions only. No generated substitute or invented date. The same photos feed Memory Cinema. |
| Gift 05 voice recording / transcript | 1 | A real recording and a text alternative are required before playback is enabled. The pack says not to synthesise a voice note. |

## Copy that now comes from the pack

| Where | What | Source in `packContent.ts` |
|---|---|---|
| Gift 01 and Letter Room envelope 1 | The main birthday letter | `packLetter` |
| Gift 02 (3D and HTML) | The 17 reasons and the closing quote | `packReasons` |
| Gift 07 "Draw a wish from the sky" | 101 wishes (the pack's heading says 100; the list has 101) | `packWishes` |
| Future Postcards (7 cards) | The seven messages | `packPostcards` |
| Gifts 01–08 | Dedication quote at the top | `packGiftDedications` |
| Gifts 03, 04, 08 | Long dedication and reveal line on reveal | `packExtended` |
| Birthday Garden | Seven stage narrations (Seed, Roots, Sprout, Leaves, Bud, Flower, Full bloom) | `packGardenNarration` |
| Memory Cinema (gift 06) and Gallery | Opening, empty-state and closing lines | `packCinema` |
| Bhumi FM (gift 05, Music lounge) | Welcome and empty-playlist lines | `packRadio` |
| Gift grid, buttons, loading, fallback, finale | Website microcopy | `packMicrocopy` |

## Source copy reused by the experiences

- Letter Room envelope 2 keeps the earlier source letter ("The Last Letter") word for word; do not alter its attribution without owner direction.
- Gift 04 shows only the verified dates in `chronosContent.dates.firstConnectionLabel` and `proposalLabel`.
- Gift 10 and the Wish Garden reveal only the ten source wishes in `chronosContent.flowerGarden.wishes`. Gift 07 also has them as its archive lanterns.
- Gift 08, Gift 16 and Gift 17 reuse existing archive messages rather than creating new private claims.
- Gift 11 uses four existing generated postcard scenes. Keep their "possible future / not a fact" framing.

## Adding an audio recording safely

1. Obtain a recording the owner supplied and approved; do not generate a voice clone or synthetic personal message.
2. Add the local file under `public/assets/audio/` and use a relative URL such as `/assets/audio/voice-note-01.mp3` in the corresponding track source.
3. Add a transcript/caption in the content source. Keep the player paused on load and require a user Play action.
4. Test play, pause, stop, seek/volume where available, error handling, dialog close/unmount cleanup, keyboard operation and reduced motion. Do not fetch remote audio.
5. Verify that an empty `src` still results in disabled controls and no failed network request.

## Adding photographs or personal content

- Add only owner-provided photographs to `public/assets/gallery/`; supply truthful alt text, a caption and a date only if the date is verified.
- Keep placeholder fields explicitly empty until real files/copy exist. Do not use generated portraits, fake memories, fabricated conversations, unapproved promises or unverified dates.
- Bhumi's birthday year remains unspecified. Keep future-postcard and future-garden copy speculative unless a real, mutual hope is supplied.
- The three postcard illustrations added with the pack (`public/assets/postcards/next-birthday-garden-table.webp`, `growing-sapling.webp`, `little-lantern-light.webp`) are generated artwork in the style of the existing four. They are atmosphere, not photographs of anything that happened.
