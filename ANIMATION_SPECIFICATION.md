# Animation Specification — Cinematic Birthday Universe

**Status:** Implemented and browser-verified in the shared scene system.  
**Audit prerequisite:** Complete; see `PROJECT_AUDIT.md`. Detailed verification: `FINAL_QA_REPORT.md`.

## 1. Motion principles

- Native document scrolling is authoritative. No wheel/touch interception, scroll snapping, forced waits, or mandatory pinned scenes.
- Transitions communicate that the reader is moving through connected rooms. Keep copy stationary/readable; animate the environment behind it.
- One global GSAP/ScrollTrigger owner for scene transitions and shared chapter-heading reveals. Reuse the installed GSAP dependency; do not add Framer Motion or a 3D package.
- Animate `opacity`, `transform`, and limited CSS custom properties; avoid layout properties, continuous blur, large filters and excessive per-frame work.
- Every timeline/listener/observer has an explicit cleanup path. CSS remains a complete functional fallback.

## 2. Scroll-driven scene transition

For each adjacent catalog pair, use the incoming chapter’s existing `data-chapter` anchor. Starting window: `top 82%` to `top 30%` of the viewport, adjusted only after visual testing. Use direct `scrub: true` so a chapter-index jump resolves immediately to the correct scene instead of leaving several old layers catching up; document scroll remains the exact progress source.

| Track | Forward motion | Reverse motion |
|---|---|---|
| Outgoing environment | Opacity 1→0; scale 1→about 1.025; x/y drift no more than 1–2% | Same timeline reverses. |
| Incoming environment | Opacity 0→1; scale about 1.04→1; subtle counter-drift | Same timeline reverses. |
| Lighting/atmosphere | One cross-scene light wash shifts hue/position with opacity; no strobe | Reverses continuously. |
| Depth planes | Far/mid/near decorative planes drift at small, different vertical offsets while their own chapter is in view | Reverses continuously; reduced motion keeps them still. |
| Content | Existing prose and controls stay in normal flow; optional heading reveal once on entry | No content disappears or becomes unreachable. |

Transitions should overlap and settle; avoid an empty/transparent gap between layers. Do not stack many animations on every child. For rapid chapter-index jumps, let ScrollTrigger interpolate through intermediate positions naturally.

## 3. Specific authored motions

- **Invitation:** existing wax-seal/envelope/letter movement remains, with reduced-motion instant open. On completion, the CTA may scroll to the garden; skip bypasses only the intro animation. The invitation remains in document flow and can be revisited.
- **Garden:** existing petals/balloons/firefly details remain modest; central scene manager owns the garden parallax and global heading reveal so there is no second ScrollTrigger lifecycle.
- **Scrapbook:** preserve `react-pageflip`, keyboard/buttons, touch/scroll behavior, and existing fallback; reduce page-turn duration under reduced motion.
- **Observatory:** use a slow minute hand (60-second revolution) and hour hand (60-minute revolution), with reduced-motion override. The environment uses subtle chapter-depth drift; verified milestones remain static/readable and all selection works without animation.
- **Letter Room:** preserve envelope open/read dialog; any reveal affects only the envelope/paper, not reading order or focus.
- **Memory Gallery:** preserve empty slots and lightbox; do not use hover-only controls or animate the image to a new state that changes meaning.
- **Wish Garden:** preserve explicit flower activation and wish announcement; motion is a brief transform/opacity accent, never required to read the wish.
- **Gift Atelier:** preserve individual boxes and local-storage state. Opening may use a short lid/ribbon transform; opened status remains visible without animation and opening all gifts is never required.
- **Music Lounge:** no autoplay. Vinyl spins only while an actual user-started track is playing; mute and pause stop relevant visual/audio state.
- **Future Postcards:** subtle card parallax/tilt only; all copy remains clearly speculative and accessible by keyboard/dialog.
- **Birthday Ballroom:** candle state follows the user’s existing light/blow/wish controls; balloons drift slowly and a short firework burst appears only after a wish. Respect reduced motion by stopping balloon motion and suppressing the burst, and never imply microphone use.
- **Finale:** confetti/star effects are short, finite, and replayable; no continuous high-count particle loop.

## 4. Reduced motion, fallback, and input

When `prefers-reduced-motion: reduce` is active:

- Do not dynamically import/use GSAP scene scrub or parallax; do not run continuous particles/ambient loops.
- Use an `IntersectionObserver` to switch one scene discretely (no long crossfade). Keep the content, controls, active chapter, gift storage, and all dialogs fully usable.
- Opening may reveal the envelope immediately; page-turn/candle/confetti motion may become instant or very short.
- CSS disables smooth scrolling and transitions as an additional fallback; cake balloons are static and the wish-firework layer is hidden.

The scene layer is pointer-events none and never focusable. Focus remains on the user’s controls; no automatic focus changes occur during scene transitions.

## 5. Technical lifecycle

1. Mount after semantic chapter anchors and scene layers exist.
2. Dynamically import `gsap` and `gsap/ScrollTrigger` once; guard the promise against unmount.
3. Register the plugin once and create all scene pair timelines/reveals inside a manager-owned `gsap.context()`.
4. Refresh on initial layout and meaningful resize/font/layout completion, not on every animation frame.
5. On cleanup, `context.revert()` and remove manager-owned observers/listeners. A failed import falls back silently to static scene selection.
6. Verify backward scroll, direct anchor navigation, history/hash loads and React StrictMode double-effect behavior.

## 6. Motion and resource budgets

- One viewport-sized fixed scene stage; no WebGL requirement.
- No more than a few active CSS ambient motifs per scene; keep particle elements static/finite or reuse a small pool.
- Avoid continuous CPU-heavy filters; no animated layout, no large blur transitions, no `will-change` on the whole DOM.
- Load only current/adjacent scene images and use the existing local asset paths.
- Measure real production bundle/gzip and mobile scrolling after implementation. Any FPS or memory claim in the final report must come from an actual test on the tested browser/device profile.

## 7. Verification checklist

- [x] Forward/back scroll between all twelve scenes; no blank/stacked scenes, console errors, or forced document-scroll behavior in the tested Chromium pass.
- [x] Direct menu/hash jump to late scenes resolves the target background and active chapter.
- [x] Revisit/reset invitation, skip intro, and reduced-motion entry.
- [x] Toggle `prefers-reduced-motion` while mounted; scene mode returns to CSS and GSAP triggers clean up.
- [x] React StrictMode development pass leaves one trigger set (32 total: 12 depth, 11 transitions, 9 heading reveals); preference restore returns to 32, reduced mode to 0.
- [x] Controls/dialogs remain operable after transitions; keyboard index Escape/focus return and native dialog Escape were exercised.
- [x] Mobile widths retain natural scroll; 360–1920 px viewport sweep has no horizontal overflow or clipped visible controls.
