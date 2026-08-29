# Embedding the hero background video in WordPress / Avada

`nurture-hero-loop.html` is a **single, self-contained file** — no build
step, no React, no npm, no GSAP/ScrollTrigger. It's a bare, full-viewport
background video container: no headings, no subtext, no navigation dots.
It plays four scenes back-to-back as one continuous, silent loop (canopy
-> close -> orchard -> reach-wide -> back to canopy), cross-fading between
them with a CSS opacity transition driven by each video's `ended` event.

Text/copy is intentionally **not** included in this file — build it
directly in Avada (Fusion Builder text/heading elements layered on top of
this code block) so it can be styled and updated independently of the
video container.

## Steps

1. **Media is already uploaded.** `canopy.mp4`, `close.mp4`, `orchard.mp4`,
   `reach-wide.mp4`, their poster images, and `grain.png` were uploaded via
   the WordPress Media Library and live at
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
   - Layer your headline/subtext/CTA elements in Fusion Builder on top of
     this code block (e.g. absolutely positioned inside a container that
     wraps both the code block and the text elements).

3. **Publish and check it.** The container fills the viewport
   (`100vw` x `100vh`) and cycles through all four scenes on a loop with no
   scroll interaction required.

## Notes

- This does not require jQuery, React, GSAP, or any other library — just
  plain HTML/CSS and a small inline `<script>`.
- All CSS is scoped under `#nurture-hero-loop` so it shouldn't affect the
  rest of the page's styling.
- The `#3a2d28` brand color tint and the animated `grain.png` noise overlay
  are retained on top of the video layer; everything else from the original
  scroll-driven version (progress bar, dots, hint chevrons, leaf mark, and
  all copy) has been removed.
- The `reach-portrait` variant and the 5th "home" scene from the original
  scroll sequence are not used here, since the loop only cycles the four
  scenes named above.
