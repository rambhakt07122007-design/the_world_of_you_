# Audio Implementation — Local, Opt-In, No Fabricated Voice

## Optional microphone blow interaction

`src/hooks/useBlowDetection.ts` requests audio input only after Enable microphone is clicked. No MediaRecorder, persistence, upload or output monitoring. One-second median RMS room calibration followed by an RMS/spectral high-band/peak-share heuristic sustained for 450ms. All tracks stop and AudioContext closes on success, cancellation, late permission resolution, 16-second timeout, tab hide, cake scene exit or unmount. Denied/missing/insecure microphones remain non-blocking; the manual blowout button completes the ritual. It detects airflow-like noise approximately, not a breath with certainty. Synthetic broadband and denial/cancellation browser tests do not establish human breath accuracy.


## Scrapbook rustle addition

The scrapbook uses local Web Audio noise, filters and a short gain envelope. Global sound preference is required. Pointer/touch capture, page controls and user-fold events prime/resume the context; flipping state triggers playback, not the final page-index notification. Preference-off suspends playback; unmount closes the context and ended nodes disconnect. No uploaded recording or third-party sound is used. Real-browser playback testing remains pending.


**Status:** The top-bar sound preference now controls the Music Lounge and both gift audio players. Turning sound off pauses active playback; turning it on never resumes audio automatically. Owner-provided audio is still missing, so tracks remain unavailable. No new audio dependency or remote service is used.

## Current behavior

- Gift 05 (Bhumi FM) is a cassette deck with insert/eject, play, pause, stop, rewind and volume controls. Transport controls are disabled until the real local voice recording source exists.
- Gift 12 (The Music of Us) is a vinyl/playlist experience with previous/next, play/pause/stop, track progress and volume controls. Track playback stays disabled while each source is empty. A separate **silent turntable preview** animates the record without pretending audio is playing.
- The `App` owns the global sound preference; the accessible top-bar control passes it to the Music Lounge, Bhumi FM and The Music of Us. Global sound-off mutes and pauses active playback. Turning sound on does not resume it; the listener must press Play again.
- Empty slots do not create an audio request. There is no autoplay, external audio/CDN, synthesized voice, voice clone, or hidden sound.
- Audio elements use `preload="none"`; play is initiated by a user action. The shared local-audio hook pauses on source change, global mute and unmount; removes listeners; catches playback errors; and clamps volume.
- Gift 01’s narration control remains disabled until a real recording and text alternative are supplied. Gift 17’s sound preference does not produce sound while no asset is installed.

## Add approved files

1. Put only owner-provided or properly licensed local audio in `public/assets/audio/`.
2. Set the matching `src` in `src/content/chronosContent.ts` (for example `/assets/audio/voice-note-01.mp3`).
3. Add an accurate transcript/caption in the same content record or the relevant letter field. Do not invent a recording or transcript.
4. Run the local production build and test the player with keyboard/touch, empty and valid sources, switching tracks, error state and dialog close/unmount cleanup.
5. Check the browser network log for local-only requests and verify that no track starts until Play is activated.

## Future audio-reactive work

No Web Audio visualizer, background ambience or UI sound effects are shipped because no approved audio assets exist. The shared global mute policy is already wired to all current audio players; add any future tracks or effects only after owner-approved/local assets are supplied and verify opt-in state, volume/mute behavior, cleanup, reduced motion, licensing and mobile performance.
