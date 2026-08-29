# Embedding the hero loop in WordPress / Avada

`nurture-hero-loop.html` is a **single, self-contained file** — no build
step, no React, no npm. It's the same fixed animation, rewritten in plain
HTML/CSS/JS so Avada (or any WordPress site) can embed it directly.

Tested and confirmed working end-to-end (Playwright, real scroll events):
all 5 stages render correctly in order, sticky-pinned for the full scroll.

## Steps

1. **Media is already uploaded.** All 11 files (5 videos + their poster
   images + `grain.png`) were uploaded via the WordPress Media Library
   and live at
   `https://www.nurtureparentingmagazine.com.au/wp-content/uploads/2026/08/`.
   `nurture-hero-loop.html` already points every asset URL there — nothing
   to change. (If WordPress ever re-uploads these into a different
   year/month folder, do a find & replace on that path across the file.)

2. **Paste it into the page.**
   - **Avada / Fusion Builder:** edit the page with Fusion Builder, add a
     **Code** element where the hero should appear, and paste the entire
     file's contents into it.
   - **Gutenberg:** add a **Custom HTML** block and paste the entire
     file's contents into it.

3. **Publish and check it.** Scroll through the section. If the animation
   plays the first scene but then goes blank/stops sticking instead of
   playing through all 5 scenes, the most likely cause is the exact bug
   that was fixed in the original app: some ancestor element (a Fusion
   Builder container, a theme wrapper, etc.) has `overflow` set to
   something other than `visible` on the X or Y axis. Check the
   container(s) wrapping this element in Avada's settings and make sure
   none of them have overflow hidden/scroll/auto — that breaks the
   sticky-scroll pin.

## Notes

- This does not require jQuery, React, or any other library beyond GSAP +
  ScrollTrigger, which are loaded from a CDN inside the file.
- All CSS is scoped under `#nurture-hero-loop` so it shouldn't affect the
  rest of the page's styling.
- The 5th ("home") scene intentionally reuses the same footage as the 2nd
  ("reach") scene as a bookend — if you'd like a distinct final scene
  instead, a new video/photo asset would need to be swapped in.
