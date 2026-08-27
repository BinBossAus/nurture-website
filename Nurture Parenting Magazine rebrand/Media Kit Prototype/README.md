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

All 11 print/advertorial package Payment Links are already wired into `NURTURE_STRIPE_LINKS` near the bottom of `index.html` (search for `STRIPE PAYMENT LINKS`). Selecting a package + issue count in the calculator builds the checkout URL with `?prefilled_promo_code=` matching the existing `2ISSUES`–`6ISSUES` discount codes, and shows a note telling the customer to set quantity = issue count at checkout (Stripe Payment Links can't prefill quantity via URL, only the promo code, email, or locale).

Any package left without a link automatically falls back to booking a call, so the "Pay & book now" button is never broken and never silently takes the wrong amount.

### Bundling gift guides / digital add-ons into the same checkout

Run `stripe-setup-digital-addons.sh` (see below) to automatically add gift guides and digital add-on activities as **optional items** on all 11 existing Payment Links, so a customer can add them in the same Stripe checkout as their print package — and to create one more standalone **Digital Campaign** link for people who want gift guides/add-ons with no print package at all. Once that script has run, paste its output URL into the `digitalOnly` entry in `NURTURE_STRIPE_LINKS` and the calculator will route digital-only campaigns straight to Stripe instead of Cal.com.

### Running the setup script

```bash
# Test first with a Stripe TEST key (sk_test_...), then re-run with your LIVE key.
STRIPE_SECRET_KEY=sk_test_xxx ./stripe-setup-digital-addons.sh
```

Requires `curl` and `jq`. **Never share your Stripe secret key in chat, in this repo, or with anyone** — run the script yourself, locally, with your own key. It only creates new prices/links and adds optional items to the 11 links listed inside it; it doesn't touch anything else already configured on your account.

### Digital add-ons — why one price instead of one per activity

The old rate card lists ~8 different $250 digital activities (directory listing, blog blast, social blast, EDM promo, audiobook sponsorship, product review, subscription giveaway, kindness challenge). Rather than creating 8 separate Stripe Prices/links, the script creates **one** "Digital Add-on Activity" price ($250, adjustable quantity) — the customer sets how many activities they want, and a free-text note on the checkout ("Which activities?") lets them specify which ones. Simpler to maintain, and Stripe fully supports adding a custom text field to a Payment Link's checkout (Dashboard → your Payment Link → *Add custom field*) if you want to formalize that.

### Free inclusions (giveaways, promotions) — don't put these in the cart

Some perks — like "Exclusive Giveaways & Promotions" — are things included for free with certain packages, not something a customer buys separately. These should stay as plain copy/checkboxes on the page (as they already are in the "Why Nurture" section), not a $0 Stripe line item — Stripe Payment Links aren't built for $0 cart items, and it adds checkout friction for no reason. If you want a customer to indicate a preference (e.g. which giveaway theme), use a Stripe **custom field** (free text or dropdown) on the relevant Payment Link instead of a purchasable item.

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
