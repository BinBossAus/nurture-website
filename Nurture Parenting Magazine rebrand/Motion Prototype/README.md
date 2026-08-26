# Nurture homepage — motion prototype

You said the new design looks clean but static, like a PDF — no opening "wow" moment,
no sense of a journey. This is a working prototype of what fixes that, built directly
on top of the `Nurture Home 2026` design (same layout, same brand system), with motion
added in five layers:

## The five ideas, in Nurture's own language

1. **A staggered hero entrance, not a flat page load.** The kicker label, headline, lead
   paragraph and buttons rise into place one after another (not all at once), and the
   hero photo does a soft "focus pull" — starts slightly blurred and zoomed, then
   sharpens into focus, like a camera settling on a family photo. This is the first
   thing a visitor sees, so it's the single highest-impact change for "first impression."
2. **The magazine covers assemble themselves.** This is the direct translation of the
   "hamburger flying together" / "ice cream pouring" energy you described, but in
   Nurture's own material: as you scroll to the "Out now" section, the three stacked
   issue covers fly in from different directions and snap into their fanned stack with
   a slight springy overshoot — like the current issue arriving and the shelf building
   itself in front of you. Hovering still fans them out further, like flicking through
   a stack on a coffee table.
3. **Everything reveals as you scroll**, instead of the whole page just existing the
   moment it loads. Cards, headings and photos fade and rise into place with an
   editorial, weighted easing curve (`cubic-bezier(.16,1,.3,1)` — the same curve
   requested in your brief) as you reach them — this is what turns "one long static
   page" into "a journey," section by section.
4. **Two soft ambient glows drift slowly** near the top of the page (already existed as
   static blurred shapes in the design — they now breathe, very slowly, forever), and
   the brand's signature full stop (the "." in "Nurture.") pulses gently everywhere it
   appears, so the brand mark itself feels quietly alive rather than printed.
5. **Small interactive polish everywhere**: buttons and cards have a proper pressed/active
   state, nav links get an underline that grows from the center on hover, and every
   interactive element gets a visible, on-brand focus ring for keyboard/accessibility.

## See it for yourself

Open `index.html` directly in any browser (double-click it, or serve the folder with
any static file server) — it's a fully self-contained page, no build step, no server
required. Scroll slowly the first time through so you can watch each section reveal.

A recorded walkthrough is also available as a project artifact if you'd rather watch it
than click through it yourself.

## Why this exists as a separate plain HTML file

The other design files in this project (`*.dc.html`) go through a special preview tool
that pre-processes the HTML/CSS before rendering it. That preprocessor turned out to
choke on the more advanced CSS this motion system needs (CSS custom properties like
`--rest`, nested functions like `cubic-bezier()`), corrupting the stylesheet and
silently breaking every animation. Rather than fight that tool's limitation, this
prototype is a completely plain, standalone HTML/CSS/JS file — guaranteed to render
correctly anywhere, and it doubles as the exact spec below for wiring this into the
real site.

## How this becomes real on the live site (Avada / WordPress)

Nothing here needs a developer or a child theme. It's three copy-paste steps, the same
pattern as the Typography + Colour Spec you already used:

1. **Paste `motion.css`** into Avada → Options → Custom CSS (once, site-wide).
2. **Paste `motion.js`** into Avada → Options → Advanced → Custom JS (once, site-wide;
   or into a footer "Code Block" element if you'd rather scope it to one page first).
3. **Tag the elements you want animated**, using Fusion Builder's existing per-element
   **"CSS Class"** field (Advanced tab on any container/column/element):
   - Hero kicker label → `hero-kicker rise rise-in`
   - Hero heading → `rise rise-in` (add `--rd:120ms` in the element's Custom CSS/inline
     style options to stagger it after the kicker)
   - Hero lead paragraph → `rise rise-in` with `--rd:260ms`
   - Hero button row (the container around both buttons) → `rise rise-in` with `--rd:400ms`
   - The very first, above-the-fold hero photo → `hero-photo`
   - Any card, heading block, or section you want to fade in on scroll → `reveal`
     (optionally with `--rd:100ms`, `--rd:200ms` on siblings so a row of 3 cards
     cascades instead of popping in together)
   - A big full-bleed feature photo further down the page → `reveal-photo`
   - The logo's "." (in the header and footer) → `brand-dot`
   - Each of the two decorative background blur shapes → `glow` (add `glow-b` to the
     second one so it drifts on a different rhythm)
   - The magazine-cover-stack section specifically needs the structure documented at
     the top of `motion.css` (a `.shelf` wrapping three `.cov cv1/cv2/cv3` elements,
     each with its resting 3D transform in a `--rest` custom property) — this one is
     more involved, so flag it and I can write the exact Fusion Builder steps once you
     confirm you want to keep this effect.

Everything is **progressive enhancement**: if JavaScript fails to load for any reason,
the page falls back to looking exactly like a normal static page — nothing ever hides
permanently behind broken JS. It also fully respects a visitor's OS-level "reduce
motion" accessibility setting (skips all animation instantly), and the two ambient
glow loops pause automatically whenever they're scrolled out of view, so they don't
burn battery/CPU in the background.

## Extending this to other pages

The same five ideas apply directly to `Nurture Our Story 2026`, `Nurture Advertise
2026`, and the rest of the rebrand: a staggered hero entrance + `reveal` on every card
grid gets you 80% of the "alive" feeling on any page, for the cost of adding one class
name per element. The magazine-cover-assemble effect is intentionally a homepage-only
signature moment — repeating it everywhere would dilute it.
