# Nurture — Interactive Media Kit &amp; Booking (Prototype)

`index.html` is a **standalone, self-contained** prototype of the new interactive media kit, rebuilt against the official **Nurture Media Kit 2026 PDF** (packages, rates, add-ons, artwork terms). Open it directly in a browser — no build step, no server required. It is deliberately built outside the `.dc.html` mockup format (which mangles custom `<style>`/`<script>` blocks) so every animation and the calculator actually run.

## What's in it

1. **Real rate card** — The Flagship (¼/½/full/DPS ad sizes, includes a free Showcase feature), The Collective, Showcase, and the five curated advertorial packages, the three digital gift guides, the campaign add-ons, and the 2–10% multi-issue discount ladder — all matching the 2026 media kit PDF, laid out in the brand system with scroll-reveal motion.
2. **Instant quote calculator** — pick a package (optional — a digital-only campaign works too), issue count, gift guide(s), any of the 8 named campaign add-ons, artwork design, and a brand audit; the total, discount and per-issue price update live. Pure vanilla JS, no backend.
3. **Action panel with four real paths**, already wired to the links you provided:
   - **Pay & book now** → Stripe (all 11 print/advertorial package Payment Links wired in; see "Wiring up Stripe" below for bundling gift guides/add-ons into the same checkout)
   - **Need artwork made** → your Tally form (`https://tally.so/r/mO2Pdg`)
   - **Upload your files** → your Dropbox file request (`https://www.dropbox.com/request/I5xeF1PHkZgTxOVxSStH`)
   - **Talk to a human first** → your Cal.com 30-min booking link (`https://cal.com/nurturemagazine/30min`)

## Wiring up Stripe

All 11 print/advertorial package Payment Links are already wired into `NURTURE_STRIPE_LINKS` near the bottom of `index.html` (search for `STRIPE PAYMENT LINKS`). Selecting a package + issue count in the calculator builds the checkout URL with `?prefilled_promo_code=` matching the existing `2ISSUES`–`6ISSUES` discount codes, and shows a note telling the customer to set quantity = issue count at checkout (Stripe Payment Links can't prefill quantity via URL, only the promo code, email, or locale).

Any package left without a link automatically falls back to booking a call, so the "Pay & book now" button is never broken and never silently takes the wrong amount.

### Bundling gift guides / digital add-ons into the same checkout

Run `stripe-setup-digital-addons.sh` (see below) to automatically add gift guides and digital add-on activities as **optional items** on all 11 existing Payment Links, so a customer can add them in the same Stripe checkout as their print package — and to create one more standalone **Digital Campaign** link for people who want gift guides/add-ons with no print package at all. Once that script has run, paste its output URL into the `digitalOnly` entry in `NURTURE_STRIPE_LINKS` and the calculator will route digital-only campaigns straight to Stripe instead of Cal.com.

### Running the setup script

Two ways to run it — pick whichever is easier:

**Option A — have your cloud agent run it for you.** Add your Stripe secret key as a secret in the Cursor dashboard (Cloud Agents → Secrets → add a secret named `STRIPE_SECRET_KEY`, value starting `sk_test_...` to test, or `sk_live_...` when you're ready for real). Secrets are injected as environment variables, never shown in chat. Once it's added, ask the agent to run the script — it needs no other input from you.

**Option B — run it yourself, locally:**

```bash
# Test first with a Stripe TEST key (sk_test_...), then re-run with your LIVE key.
STRIPE_SECRET_KEY=sk_test_xxx ./stripe-setup-digital-addons.sh
```

Requires `curl` and `jq`. **Never paste your Stripe secret key directly into chat** — either add it as a Cursor secret (Option A) or run the script yourself locally (Option B). It only creates new prices/links and adds optional items to the 11 links listed inside it; it doesn't touch anything else already configured on your account.

### Campaign add-ons — why one Stripe price instead of eight

The media kit lists 8 named $250 add-ons (social promo, giveaway collaboration, The Letter/EDM, blog on social, website banners & ads, Nurture Index listing, product review, audiobook sponsorship). The on-page calculator shows all 8 as individual checkboxes for an accurate quote, but Stripe caps a Payment Link at 10 optional items total — and we also need room for 3 gift guide sizes, artwork, and a brand audit — so the checkout side consolidates the 8 into **one** "Campaign Add-on Activity" price ($250, adjustable quantity). The customer sets how many activities they want and uses the checkout's note field (or a Stripe custom field you add in the Dashboard) to say which ones.

### Free inclusions (giveaways, kindness challenge) — don't put these in the cart

"Subscription giveaway" and "The Sharing Kindness Challenge" are free with any print booking (one brand per issue) — not something a customer buys separately. These stay as plain copy on the page, not a $0 Stripe line item — Stripe Payment Links aren't built for $0 cart items, and it adds checkout friction for no reason. If you want a customer to indicate a preference, use a Stripe **custom field** (free text or dropdown) on the relevant Payment Link instead of a purchasable item.

## Updating prices

All pricing lives in one place — the `PACKAGES`, `GUIDES`, `GUIDE_SIZES`, `DISCOUNT_TIERS`, `ADDONS`, `ADDON_PRICE`, `ARTWORK_FEE` and `BRAND_AUDIT_FEE` variables inside the calculator `<script>` block. Change a number there and the calculator, labels and totals all update automatically. The static rate-card cards further up the page are plain HTML/CSS and would need their text updated separately if a price changes.

## Rolling this into the live site (Avada/WordPress)

Same approach as the homepage Motion Prototype:
- The `<style>` block can go into Avada's **Custom CSS** field (or a page-specific CSS class).
- The `<script>` block (including the Stripe config) can go into Avada's **Custom JS** field, or a "Code Block" element on the page.
- The HTML markup can be rebuilt as Fusion Builder containers/columns using the same class names (`.glass`, `.card-lift`, `.reveal`, `.pkg-card`, etc.) so the existing CSS keeps working, or dropped in as a raw HTML/Code element if you'd rather not rebuild it in Fusion Builder.

## Accessibility &amp; performance

- Respects `prefers-reduced-motion`: all animation and count-up disables instantly, content is fully visible with no JS.
- All interactive controls are real `<button>`/`<input>` elements — keyboard and screen-reader operable.
- No external JS libraries; total added weight is this one file plus Google Fonts.
