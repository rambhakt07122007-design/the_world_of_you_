# Accessibility Report — Cinematic Birthday Universe

> **Current native-3D build:** see `START_HERE.md` and `FINAL_IMPLEMENTATION_REPORT.md` for current scope, new browser evidence and limitations. Earlier findings/deployment descriptions below are historical. Current core QA: 12/12 pass; final native rose/crown/portal QA: 3/3 pass. No production deployment of this transformation has occurred.


**Verified:** 3 November 2026 (Asia/Kolkata)  
**Scope:** Local production-preview accessibility smoke checks and keyboard interaction paths. This is not a formal WCAG conformance audit or assistive-technology certification.

## Semantic structure and names

- One `<main>` landmark contains the story; navigation regions have accessible names: “Primary navigation,” “All birthday chapters,” and “Final chapter links.”
- Twelve semantic chapter sections retain stable IDs and headings; the decorative scene stage is `aria-hidden="true"` and contains no focusable controls.
- Browser DOM smoke scan found **zero visible unnamed controls**, **zero images without an `alt` attribute**, and **zero visible focusable elements inside `aria-hidden` content**. Empty `alt` is used for decorative stage art; meaningful postcard/desk imagery has descriptive text alternatives.
- The current chapter is represented by `aria-current="location"` in the visible quick navigation or complete chapter index. Opened gifts and selected wishes use explicit button state rather than color alone.
- Chapter-index links are removed from the tab order while the index is closed; when open, all twelve entries are reachable and the active entry is exposed.

## Keyboard, focus and dialogs

- The skip link targets the Birthday Garden. Chapter-index open/close works by keyboard; Escape closes it and returns focus to the toggle.
- Storybook controls have explicit names and the book supports left/right arrow keys in addition to its buttons and swipe behavior.
- Native archive dialogs for letters, gallery mounts, gifts and postcards are labelled by their heading. Opening moves focus to the close button; Escape closes the dialog and returns focus to its invoking control. These paths were exercised in Chromium.
- Visible keyboard focus has a 3 px outline rule in the site styles; hover is not required to reveal essential controls.
- The cake ritual uses buttons only; no microphone permission, recording or voice analysis is requested.

## Motion, audio and content integrity

- Under `prefers-reduced-motion: reduce`, scene switching uses the static CSS/observer path without loading the ScrollTrigger chunk at initial load. The clock hands stop, envelope opening is immediate, candle lighting is immediate, and page-turn/ambient CSS motion is reduced.
- Toggling reduced motion while mounted cleans up the animated scene trigger set and restores it once when standard motion returns.
- Audio remains opt-in and paused; all three entries correctly state that no local audio file was supplied. No external stream is requested.
- Gallery photo mounts remain empty, owner-editable, and labelled; speculative postcards identify themselves as imagined, not fact or memory. The birthday year remains unspecified.

## Responsive smoke checks

At **360, 390, 430, 768, 1024, 1280, 1440 and 1920 px**, the settled scene view had no horizontal document overflow or visible clipped controls. Mobile invitation, observatory and finale captures are in `docs/screenshots/`.

## Limitations

- No automated axe-core/WAVE run, manual screen-reader session, switch-control test, or formal WCAG 2.2 AA certification was performed.
- Text/background contrast was not measured with a contrast analyzer. Verify contrast on final deployment/device conditions before claiming formal conformance.
- Touch target comfort was smoke-checked visually but not formally measured on physical devices. Real iOS/Android input, zoom, GPU and memory behavior were not profiled.
- Screen-reader announcements for dynamic chapter-status changes were not tested with assistive technology.

For automated browser behavior and exact test scope, see `FINAL_QA_REPORT.md`.
