# Motion language

- Physical objects move around their joints or bend along material creases; no scale-based unfolding.
- A single reversible progress transport owns each multi-stage letter sequence. 4.8 seconds from endpoint to endpoint, proportional time when interrupted. Scene movement uses capped simulation delta; letter transport uses active wall-clock delta so low frame rates do not turn 4.8 seconds into a minute. Offscreen/tab suspension resets the clock on resume.
- Sequence: wax split → hinged flap → extraction → upper crease → lower crease → readable text. Reverse the same functions to close. Skip/reduced motion selects the endpoint directly.
- Text is never a reward gated behind WebGL: Skip works independently and reveals the real DOM content. Original message is also painted on the actual paper mesh. The DOM is the readable/accessibility source, not a tiny canvas texture.
- Brief horizontal ink reveals are typographic approximations, **not vector handwriting path tracing**. Maximum duration .65 seconds per paragraph, concurrent; no forced word-by-word wait. Reduced motion removes the reveal.
- No repeated chapter-heading slide/fades, page-wide arrival slide, balloon bobbing, wish bloom bounce, generic gift box rocking or tiny opened-marker zoom/spin.
- Retain navigation feedback, page-flip mechanics, playback-conditioned vinyl spin, native plant motion, candle flicker, targeted celebration and section-specific background transitions.
- No new autoplay audio, microphone permission requests, physics engine, postprocessing depth-of-field or network model dependencies.
- Existing named effects and source references were inventoried before changes in ANIMATION_INVENTORY.md. Removed effects remain in that document as baseline evidence, not current implementation claims.
