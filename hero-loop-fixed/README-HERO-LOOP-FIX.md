# Hero scroll loop — fixed copy

This folder is a snapshot of the "Nurture" hero scroll animation app that was
built in Grok (repo: `BinBossAus/nurture-hero-loop`), with two bugs fixed
that were causing the animation to appear stuck / go blank while scrolling.

## The bugs and fixes

1. **`src/styles.css`** — the `body` rule had `overflow-x: hidden;` with no
   `overflow-y` set. Browsers auto-compute the other overflow axis to a
   non-visible value in that case, which silently turns `<body>` into its
   own scroll container. Because the real page scroll happens on
   `<html>`/the window (not `<body>`, whose own scroll position never
   moves), this broke `position: sticky` on `.hero-stage` — instead of
   staying pinned for the whole animation, it scrolled away after the
   first screen height, leaving a blank background for the rest of the
   scroll. **Fix: removed `overflow-x: hidden` from `body`** (it's already
   handled on `html`).

2. **`src/components/hero-journey.tsx`** — a `useEffect` ran
   `setInterval(arm, 1200)`, forcing all 7 `<video>` elements to keep
   playing every 1.2 seconds regardless of which one was actually visible.
   This fought the existing visibility-based pause/play logic
   (`syncVideos`) and kept all 7 HD videos decoding simultaneously the
   entire time the page was open — heavy enough to visibly stall
   scroll-driven rendering on real hardware. **Fix: removed that effect**;
   video play/pause is now driven entirely by `syncVideos()` inside the
   `useGSAP` hook, which only plays the currently-visible shot's active
   video variant.

Both fixes were verified with Playwright (headless computed-style checks,
real wheel-event scrolling, and screenshots) confirming all 5 stages
(hand close-up → girl reaching from behind → wider orchard → canopy →
final scene) now render correctly across the full scroll range.

## How to run it

```bash
npm install
npm run dev
```

Then open http://localhost:8080/ and scroll through the hero section.

## Getting this back into the live Grok app

This folder is a plain copy for safekeeping — it is **not** wired up to
Grok's own deployment. To get the fix live on the actual hosted preview,
apply the same two edits inside the Grok Build project for
`nurture-hero-loop` (or ask Grok's assistant to apply them), since that is
what Grok's platform deploys from.
