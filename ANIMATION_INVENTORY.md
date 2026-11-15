# Static CSS animation inventory

Code-based inventory, not a claim that every keyframe is visible live. Named effects below; GSAP/native choreography covered in WEBSITE_AUDIT.md.

### `dust-twinkle` — `src/styles/global.css`
- Current: src/styles/global.css:49 .invitation-screen__dust i { position: absolute; border-radius: 50%; background: rgba(183,136,117,.48); animation: dust-twinkle 4.6s ease-in-out infinite alternate; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `petal-fall` — `src/styles/global.css`
- Current: src/styles/global.css:111 .garden-petals i { position: absolute; top: -8%; width: 8px; height: 12px; border-radius: 80% 5% 80% 10%; background: rgba(255,232,223,.7); box-shadow: 0 1px 3px rgba(180,119,111,.13); animation: petal-fall linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `ornament-drift` — `src/styles/global.css`
- Current: src/styles/global.css:108 .birthday-garden__ornament--flower { top: 15%; right: 22%; animation: ornament-drift 8s ease-in-out infinite; }; src/styles/global.css:109 .birthday-garden__ornament--cake { bottom: 20%; right: 9%; color: rgba(255,243,222,.85); animation: ornament-drift 10s ease-in-out infinite reverse; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `paper-turn-next` — `src/styles/global.css`
- Current: src/styles/global.css:170 .storybook-book.is-turning-next .storybook-pages { animation: paper-turn-next .43s ease-in-out; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `paper-turn-prev` — `src/styles/global.css`
- Current: src/styles/global.css:171 .storybook-book.is-turning-prev .storybook-pages { animation: paper-turn-prev .43s ease-in-out; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `bloom-bounce` — `src/styles/global.css`
- Current: src/styles/global.css:310 .wish-flower.is-blooming .wish-flower__bloom { animation: bloom-bounce .78s ease; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `gift-open-pop` — `src/styles/global.css`
- Current: src/styles/global.css:353 .gift-parcel__opened-mark { position: absolute; z-index: 4; top: 3px; left: 4px; color: #a27c53; animation: gift-open-pop .6s ease both; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `record-spin` — `src/styles/global.css`
- Current: src/styles/global.css:378 .vinyl-disc.is-spinning { animation: record-spin 2.6s linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `cake-balloon-drift` — `src/styles/global.css`
- Current: src/styles/global.css:427 .cake-balloon { position: absolute; width: 27px; height: 36px; border-radius: 55% 55% 48% 48%; box-shadow: inset -5px -5px 10px rgba(97,67,49,.11),inset 5px 4px 8px rgba(255,255,255,.5),0 8px 17px rgba(97,67,49,.08); transform-origin: center bottom; animation: cake-balloon-drift 7s ease-in-out infinite; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `cake-firework` — `src/styles/global.css`
- Current: src/styles/global.css:434 .cake-fireworks { position: absolute; z-index: 3; inset: 0; overflow: hidden; pointer-events: none; }; src/styles/global.css:435 .cake-fireworks i { position: absolute; width: 4px; height: 4px; border-radius: 50%; background: currentColor; opacity: 0; box-shadow: 0 -25px 0 -1px currentColor,18px -18px 0 -1px currentColor,25px 0 0 -1px currentColor,18px 18px 0 -1px currentColor,0 25px 0 -1px currentColor,-18px 18px 0 -1px currentColor,-25px 0 0 -1px currentColor,-18px -18px 0 -1px currentColor; transform: scale(.2); }; src/styles/global.css:436 .cake-fireworks.is-bursting i { animation: cake-firework .95s cubic-bezier(.12,.62,.28,1) var(--burst-delay) both; }; src/styles/global.css:437 .cake-fireworks i:nth-child(1) { top: 28%; left: 25%; color: #c98291; --burst-delay: 0ms; }; src/styles/global.css:438 .cake-fireworks i:nth-child(2) { top: 19%; left: 51%; color: #c6a66b; --burst-delay: 130ms; }; src/styles/global.css:439 .cake-fireworks i:nth-child(3) { top: 30%; left: 76%; color: #819b82; --burst-delay: 260ms; }; src/styles/global.css:758 .cake-fireworks { display: none; }; src/world/BirthdayCake.tsx:121 <div className={`cake-fireworks${wishBurst ? " is-bursting" : ""}`} aria-hidden="true"><i /><i /><i /></div>
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `candle-flicker` — `src/styles/global.css`
- Current: src/styles/global.css:444 .cake-flame { transform-origin: center bottom; animation: candle-flicker .62s ease-in-out infinite alternate; filter: drop-shadow(0 0 8px rgba(240,181,89,.72)); }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `wish-sparkle` — `src/styles/global.css`
- Current: src/styles/global.css:460 .birthday-cake-scene.has-wished .cake-scene__stars i { animation: wish-sparkle 1.2s ease-out var(--spark-delay) both; }; src/styles/premium.css:253 .cake-scene__stars.is-bursting i { animation: wish-sparkle 1.05s ease-out var(--spark-delay) both; }; src/styles/premium.css:255 .birthday-cake-scene.has-wished .cake-scene__stars.is-bursting i { animation: wish-sparkle 1.05s ease-out var(--spark-delay) both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `finale-burst` — `src/styles/global.css`
- Current: src/styles/global.css:532 .final-celebration.is-replaying .final-celebration__particles i { animation: finale-burst 1.45s cubic-bezier(.12,.56,.29,1) var(--confetti-delay) both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `observatory-minute-hand` — `src/styles/sceneSystem.css`
- Current: src/styles/sceneSystem.css:180 .pocket-watch__hand--minute { animation: observatory-minute-hand 60s linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `observatory-hour-hand` — `src/styles/sceneSystem.css`
- Current: src/styles/sceneSystem.css:181 .pocket-watch__hand--hour { animation: observatory-hour-hand 3600s linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `gift-letter-unfold` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:93 .gift-letter__reading { max-height: 330px; margin: 15px 0; padding: 20px clamp(14px,3vw,34px); overflow: auto; border: 1px solid rgba(163,126,91,.35); color: #67524b; background: repeating-linear-gradient(0deg,transparent 0 29px,rgba(140,109,79,.08) 30px),#fffaf0; animation: gift-letter-unfold .55s ease both; }; src/styles/giftAtelier.css:224 .gift-open-when__letter { min-height: 91px; margin-top: 13px; padding: 15px; border: 1px solid rgba(178,142,104,.28); background: repeating-linear-gradient(0deg,transparent 0 24px,rgba(143,117,89,.09) 25px),#fff9ee; }.gift-open-when__letter small { color: #a17d68; font: 700 6px/1 var(--font-ui); letter-spacing: .13em; }.gift-open-when__letter p { margin: 10px 0 0; color: #6c5550; font: 1.06rem/1.4 var(--font-editorial); }.gift-open-when__letter.is-open { animation: gift-letter-unfold .35s ease both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `letter-flame` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:79 .gift-letter__candle i { position: absolute; top: -16px; left: 5px; width: 8px; height: 17px; border-radius: 50% 50% 40% 40%; background: radial-gradient(ellipse at 50% 80%,#fff6d7 0 30%,#e8a75b 62%,transparent 75%); animation: letter-flame 1.7s ease-in-out infinite alternate; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `jar-shake` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:109 .gift-jar__still.is-shaking { animation: jar-shake .55s ease both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `flower-twinkle` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:134 .gift-flower__sparkle { position: absolute; color: rgba(255,250,222,.84); text-shadow: 0 0 10px #fff; animation: flower-twinkle 2.2s ease-in-out infinite alternate; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `cassette-spin` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:174 .gift-cassette__deck.is-playing .gift-cassette__reel { animation: cassette-spin 1.4s linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `gear-turn` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:230 .gift-machine__gears { position: absolute; inset: 0; color: rgba(67,52,39,.62); }.gift-machine__gears i, .gift-machine__gears b, .gift-machine__gears em { position: absolute; font-style: normal; font-size: 47px; }.gift-machine__gears i { top: 21px; left: 7%; }.gift-machine__gears b { right: 6%; bottom: 30px; font-size: 57px; }.gift-machine__gears em { right: 14%; top: 24px; font-size: 30px; }.gift-machine__workshop.is-running .gift-machine__gears i { animation: gear-turn .75s linear infinite; }.gift-machine__workshop.is-running .gift-machine__gears b { animation: gear-turn .75s linear infinite reverse; }.gift-machine__workshop.is-running .gift-machine__gears em { animation: gear-turn .55s linear infinite reverse; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `vinyl-spin` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:246 .gift-vinyl__record { position: relative; z-index: 2; width: 190px; height: 190px; display: grid; place-items: center; border: 1px solid rgba(244,218,187,.5); border-radius: 50%; background: repeating-radial-gradient(circle,#2b262d 0 3px,#48404a 4px 5px,#29252d 6px 8px); box-shadow: 0 13px 22px rgba(13,13,18,.38); }.gift-vinyl__record.is-spinning { animation: vinyl-spin 3.6s linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `equalizer-bob` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:249 .gift-vinyl__equalizer { position: absolute; right: 7%; bottom: 22px; left: 7%; height: 29px; display: flex; align-items: center; justify-content: center; gap: 5px; }.gift-vinyl__equalizer i { width: 4px; height: var(--bar-height,5px); border-radius: 99px; background: linear-gradient(#e7bd8b,#b87489); opacity: .7; }.gift-vinyl__record.is-spinning ~ .gift-vinyl__equalizer i { animation: equalizer-bob .6s ease-in-out infinite alternate; animation-delay: var(--bar-delay,0ms); }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `tree-arrive` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:268 .gift-future-garden__tree { position: relative; z-index: 2; width: 180px; height: 200px; transform-origin: bottom center; animation: tree-arrive .55s cubic-bezier(.2,.7,.18,1) both; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `leaf-unfold` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:270 .gift-future-garden__leaf { position: absolute; z-index: 1; display: grid; place-items: center; width: 23px; height: 23px; border: 1px solid rgba(255,255,255,.48); border-radius: 70% 20% 70% 20%; color: #f8f0d1; background: #7d9a73; box-shadow: 0 3px 8px rgba(65,85,60,.16); font-style: normal; animation: leaf-unfold .45s ease both; }.leaf-1 { top: 74px; left: 31px; }.leaf-2 { top: 56px; right: 28px; }.leaf-3 { top: 35px; left: 77px; }.leaf-4 { top: 13px; left: 26px; }.leaf-5 { top: 6px; right: 18px; }.leaf-6 { top: 90px; left: 84px; }.leaf-7 { top: 47px; left: 9px; }.leaf-8 { top: 28px; right: 2px; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `ultimate-confetti` — `src/styles/giftAtelier.css`
- Current: src/styles/giftAtelier.css:289 .gift-ultimate__celebration { position: absolute; inset: 0; overflow: hidden; pointer-events: none; }.gift-ultimate__celebration i { position: absolute; top: -8%; left: var(--confetti-left); color: var(--confetti-color); font-style: normal; animation: ultimate-confetti var(--confetti-duration,3s) linear infinite; animation-delay: var(--confetti-delay,0ms); }.gift-ultimate__celebration b, .gift-ultimate__celebration em { position: absolute; bottom: 12%; width: 40px; height: 56px; border-radius: 50% 50% 45% 45%; background: radial-gradient(circle at 32% 24%,#fff4d6,#c87f8b 72%); box-shadow: 0 0 0 1px rgba(255,255,255,.3); }.gift-ultimate__celebration b { left: 20%; }.gift-ultimate__celebration em { right: 20%; background: radial-gradient(circle at 32% 24%,#fff4d6,#d4af69 72%); }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `paper-ink-reveal` — `src/styles/cinematic.css`
- Current: src/styles/cinematic.css:40 .physical-letter-copy.is-open { animation:paper-ink-reveal 1.7s ease both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `world-arrive` — `src/styles/premium.css`
- Current: src/styles/premium.css:73 .world-site { min-height: 100vh; background: var(--color-cream); animation: world-arrive .85s var(--ease-silk) both; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `firefly-drift` — `src/styles/premium.css`
- Current: src/styles/premium.css:95 .garden-fireflies i { position: absolute; width: 5px; height: 5px; border-radius: 50%; background: #fff4cf; box-shadow: 0 0 12px 3px rgba(250,226,164,.65); animation: firefly-drift 4.8s ease-in-out infinite alternate; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `balloon-drift` — `src/styles/premium.css`
- Current: src/styles/global.css:427 .cake-balloon { position: absolute; width: 27px; height: 36px; border-radius: 55% 55% 48% 48%; box-shadow: inset -5px -5px 10px rgba(97,67,49,.11),inset 5px 4px 8px rgba(255,255,255,.5),0 8px 17px rgba(97,67,49,.08); transform-origin: center bottom; animation: cake-balloon-drift 7s ease-in-out infinite; }; src/styles/premium.css:98 .garden-balloon { position: absolute; width: 29px; height: 39px; border-radius: 55% 55% 48% 48%; box-shadow: inset -5px -5px 10px rgba(97,67,49,.1), inset 5px 4px 8px rgba(255,255,255,.48), 0 8px 17px rgba(97,67,49,.08); animation: balloon-drift 6.5s ease-in-out infinite; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `butterfly-float` — `src/styles/premium.css`
- Current: src/styles/premium.css:105 .garden-butterfly { position: absolute; z-index: 2; color: rgba(255,247,222,.9); font-size: 1.65rem; text-shadow: 0 2px 9px rgba(122,91,67,.25); pointer-events: none; animation: butterfly-float 7s ease-in-out infinite; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `seal-crack` — `src/styles/premium.css`
- Current: src/styles/premium.css:186 .letter-envelope.is-opening .letter-envelope__seal { animation: seal-crack .36s ease both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `letter-unfold` — `src/styles/premium.css`
- Current: src/styles/giftAtelier.css:93 .gift-letter__reading { max-height: 330px; margin: 15px 0; padding: 20px clamp(14px,3vw,34px); overflow: auto; border: 1px solid rgba(163,126,91,.35); color: #67524b; background: repeating-linear-gradient(0deg,transparent 0 29px,rgba(140,109,79,.08) 30px),#fffaf0; animation: gift-letter-unfold .55s ease both; }; src/styles/giftAtelier.css:224 .gift-open-when__letter { min-height: 91px; margin-top: 13px; padding: 15px; border: 1px solid rgba(178,142,104,.28); background: repeating-linear-gradient(0deg,transparent 0 24px,rgba(143,117,89,.09) 25px),#fff9ee; }.gift-open-when__letter small { color: #a17d68; font: 700 6px/1 var(--font-ui); letter-spacing: .13em; }.gift-open-when__letter p { margin: 10px 0 0; color: #6c5550; font: 1.06rem/1.4 var(--font-editorial); }.gift-open-when__letter.is-open { animation: gift-letter-unfold .35s ease both; }; src/styles/premium.css:188 .letter-reading { animation: letter-unfold .48s var(--ease-silk) both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `ink-appear` — `src/styles/premium.css`
- Current: src/styles/premium.css:190 .letter-reading__salutation { animation: ink-appear .48s .08s both; }; src/styles/premium.css:191 .letter-reading__body p { font: 1.17rem/1.72 var(--font-editorial); animation: ink-appear .5s both; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `wish-pollen` — `src/styles/premium.css`
- Current: src/styles/premium.css:217 .wish-garden__pollen i { position: absolute; width: 4px; height: 4px; border-radius: 50%; background: rgba(255,245,214,.84); box-shadow: 0 0 10px rgba(255,250,225,.9); animation: wish-pollen 7.5s ease-in-out infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `gift-box-rock` — `src/styles/premium.css`
- Current: src/styles/premium.css:231 .gift-parcel.is-opening .gift-parcel__box { animation: gift-box-rock .72s var(--ease-silk); }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `gift-lid-lift` — `src/styles/premium.css`
- Current: src/styles/premium.css:232 .gift-parcel.is-opening .gift-parcel__box i { animation: gift-lid-lift .72s var(--ease-silk) both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `ribbon-slip` — `src/styles/premium.css`
- Current: src/styles/premium.css:233 .gift-parcel.is-opening .gift-parcel__box b { animation: ribbon-slip .72s ease both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `signature-write` — `src/styles/premium.css`
- Current: src/styles/premium.css:286 .final-celebration__signature span::after { display: block; height: 2px; content: ""; background: linear-gradient(90deg,var(--color-gold),transparent); transform: rotate(-4deg) translateY(-2px); transform-origin: left; animation: signature-write 1.1s var(--ease-silk) both; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `falling-star` — `src/styles/premium.css`
- Current: src/styles/premium.css:289 .final-celebration__starfield i { position: absolute; top: -8%; width: 1px; height: 42px; opacity: 0; background: linear-gradient(180deg,transparent,rgba(255,242,204,.92),transparent); transform: rotate(35deg); animation: falling-star 6s linear infinite; }
- Decision: Retain provisionally: object-specific movement; respect reduced motion and avoid competing effects.

### `dialog-appear` — `src/styles/premium.css`
- Current: src/styles/premium.css:297 dialog.archive-dialog[open] { animation: dialog-appear .28s var(--ease-silk) both; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

### `cake-wick-drift` — `src/styles/premium.css`
- Current: src/styles/premium.css:394 .cake-wick-smoke { animation:cake-wick-drift .8s ease-out both; transform-box:fill-box; transform-origin:bottom; }
- Decision: Improve: replace overshoot/rotation with quiet state feedback.

Duplicate names: {}