# Nurture — Interactive Media Kit &amp; Booking (Prototype)

`index.html` is a **standalone, self-contained** prototype of the new interactive media kit. Open it directly in a browser — no build step, no server required. It is deliberately built outside the `.dc.html` mockup format (which mangles custom `<style>`/`<script>` blocks) so every animation and the calculator actually run.

## What's in it

1. **Real rate card** — every current package and price (ad sizes, curated advertorial packages, gift guides, digital add-ons) and the 2–10% multi-issue discount ladder, laid out in the 2026 brand system with scroll-reveal motion.
2. **Instant quote calculator** — pick a package, issue count, gift guide(s) and digital add-ons; the total, discount and per-issue price update live. Pure vanilla JS, no backend.
3. **Action panel with four real paths**, already wired to the links you provided:
   - **Pay & book now** → Stripe (see "Wiring up Stripe" below — currently falls back to the artwork/booking form until real Payment Links are added)
   - **Need artwork made** → your Tally form (`https://tally.so/r/mO2Pdg`)
   - **Upload your files** → your Dropbox file request (`https://www.dropbox.com/request/I5xeF1PHkZgTxOVxSStH`)
   - **Talk to a human first** → your Cal.com 30-min booking link (`https://cal.com/nurturemagazine/30min`)

## Wiring up Stripe

Open `index.html` and find the `NURTURE_STRIPE_LINKS` block near the bottom (search for `STRIPE PAYMENT LINKS`). Uncomment/add a line per package with its real Stripe Payment Link or Checkout URL:

```js
window.NURTURE_STRIPE_LINKS = {
  quarter: "https://buy.stripe.com/xxxxxxxx",
  full:    "https://buy.stripe.com/xxxxxxxx",
  default: "https://buy.stripe.com/xxxxxxxx" // fallback for any package without its own link
};
```

Any package left out automatically falls back to the artwork/booking request form, so the "Pay & book now" button is never broken and never silently takes the wrong amount.

## Updating prices

All pricing lives in one place — the `PACKAGES`, `GUIDE_SIZES`, `DISCOUNT_TIERS` and `ADDON_PRICE` variables inside the calculator `<script>` block. Change a number there and the calculator, labels and totals all update automatically. The static rate-card cards further up the page are plain HTML/CSS and would need their text updated separately if a price changes.

## Rolling this into the live site (Avada/WordPress)

Same approach as the homepage Motion Prototype:
- The `<style>` block can go into Avada's **Custom CSS** field (or a page-specific CSS class).
- The `<script>` block (including the Stripe config) can go into Avada's **Custom JS** field, or a "Code Block" element on the page.
- The HTML markup can be rebuilt as Fusion Builder containers/columns using the same class names (`.glass`, `.card-lift`, `.reveal`, `.pkg-card`, etc.) so the existing CSS keeps working, or dropped in as a raw HTML/Code element if you'd rather not rebuild it in Fusion Builder.

## Accessibility &amp; performance

- Respects `prefers-reduced-motion`: all animation and count-up disables instantly, content is fully visible with no JS.
- All interactive controls are real `<button>`/`<input>` elements — keyboard and screen-reader operable.
- No external JS libraries; total added weight is this one file plus Google Fonts.
