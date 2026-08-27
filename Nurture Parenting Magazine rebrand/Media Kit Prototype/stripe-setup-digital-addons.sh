#!/usr/bin/env bash
# =============================================================================
# Nurture — Stripe setup for gift guides, campaign add-ons, artwork design,
# brand audits, and a standalone "digital campaign" Payment Link.
#
# WHAT THIS DOES
#   1. Creates 6 new Stripe Prices: Gift Guide Small/Medium/Large ($150/$200/
#      $250), a generic Campaign Add-on Activity ($250, adjustable quantity —
#      covers the 8 named $250 add-ons: social promo, giveaway collab, EDM,
#      blog, website ads, Nurture Index listing, product review, audiobook
#      sponsorship), an Artwork Design Service ($300, one-off), and a Brand
#      Audit & Style Guide ($300, one-off).
#   2. Attaches all 5 of those as "optional items" onto each of your 11
#      existing print/advertorial package Payment Links, so a customer
#      booking a print package can add a gift guide, campaign activities,
#      artwork design or a brand audit in the SAME Stripe checkout.
#   3. Creates ONE new standalone "Digital Campaign" Payment Link for people
#      who want gift guides / add-ons / a brand audit with NO print package.
#
# Stripe caps a Payment Link at 10 optional items, which is why the 8 named
# $250 add-ons share one generic, quantity-adjustable price instead of each
# getting its own — ask the customer which ones via the checkout's note
# field (or add a custom field in the Dashboard) rather than the price list.
#
# SAFETY
#   - Run this yourself, locally, with your OWN Stripe secret key.
#   - NEVER paste your secret key into chat, a repo, or send it to anyone.
#   - Test first against a Stripe TEST key (starts with sk_test_) before
#     running against your LIVE key (starts with sk_live_).
#   - This script only CREATES prices/links and UPDATES optional_items on the
#     11 links below — it does not touch pricing, discounts, or anything else
#     already configured on those links.
#
# REQUIREMENTS: curl, jq (install with `brew install jq` / `apt install jq`)
#
# USAGE:
#   STRIPE_SECRET_KEY=sk_test_xxx ./stripe-setup-digital-addons.sh
# =============================================================================
set -euo pipefail

: "${STRIPE_SECRET_KEY:?Set STRIPE_SECRET_KEY before running this script, e.g. STRIPE_SECRET_KEY=sk_test_xxx ./stripe-setup-digital-addons.sh}"

API="https://api.stripe.com/v1"
AUTH="${STRIPE_SECRET_KEY}:"
CURRENCY="aud"   # change if you invoice in a different currency

# Your 11 confirmed print/advertorial package Payment Link URLs (from the
# media kit calculator config). The script looks up each one's internal
# payment_link ID automatically — you don't need to find those manually.
declare -A PACKAGE_LINKS=(
  [quarter]="https://buy.stripe.com/28EdR25NMevi8ly8M56oo0h"        # The Flagship — 1/4 page
  [half]="https://buy.stripe.com/28EaEQ3FE86U7hu5zT6oo0i"           # The Flagship — 1/2 page
  [full]="https://buy.stripe.com/28E3co2BAgDq8lyd2l6oo0n"           # The Flagship — Full page
  [dps]="https://buy.stripe.com/fZu4gsgsqaf28lygex6oo0o"            # The Flagship — Double page
  [multisplit]="https://buy.stripe.com/7sY00c5NMgDqcBO4vP6oo0p"     # The Collective
  [ausmade]="https://buy.stripe.com/3cIcMYfom5YM45iaUd6oo0q"        # Australian Made
  [mamabubba]="https://buy.stripe.com/6oUdR2fomevi45i5zT6oo0r"      # The Essentials
  [selflove]="https://buy.stripe.com/8x2dR21xw86UcBOaUd6oo0s"       # Self Love
  [loveoflearning]="https://buy.stripe.com/6oUaEQ7VU86UdFS7I16oo0t" # Love of Learning
  [changemakers]="https://buy.stripe.com/6oUdR28ZY3QE9pCd2l6oo0u"   # Changemakers
  [showcase]="https://buy.stripe.com/28E4gs6RQ3QE31egex6oo0J"       # Showcase
)

echo "== 1) Creating gift guide, add-on, artwork and brand audit prices ($CURRENCY) =="

create_price () {
  local name="$1" amount="$2"
  curl -s "$API/prices" -u "$AUTH" \
    -d "unit_amount=$amount" \
    -d "currency=$CURRENCY" \
    -d "product_data[name]=$name" | jq -r '.id'
}

PRICE_SMALL=$(create_price "Digital Gift Guide Feature — Small" 15000)
PRICE_MEDIUM=$(create_price "Digital Gift Guide Feature — Medium" 20000)
PRICE_LARGE=$(create_price "Digital Gift Guide Feature — Large" 25000)
PRICE_ADDON=$(create_price "Campaign Add-on Activity" 25000)
PRICE_ARTWORK=$(create_price "Artwork Design Service (5hr min, 1 concept + 2 revisions)" 30000)
PRICE_BRAND_AUDIT=$(create_price "Brand Audit & Style Guide" 30000)

echo "  Small guide feature:  $PRICE_SMALL       (\$150)"
echo "  Medium guide feature: $PRICE_MEDIUM      (\$200)"
echo "  Large guide feature:  $PRICE_LARGE       (\$250)"
echo "  Campaign add-on:      $PRICE_ADDON       (\$250, adjustable qty)"
echo "  Artwork design:       $PRICE_ARTWORK     (\$300, one-off)"
echo "  Brand audit:          $PRICE_BRAND_AUDIT (\$300, one-off)"
echo

echo "== 2) Looking up your existing Payment Link IDs =="
ALL_LINKS_JSON=$(curl -s "$API/payment_links?limit=100" -u "$AUTH")

find_link_id () {
  local url="$1"
  echo "$ALL_LINKS_JSON" | jq -r --arg url "$url" '.data[] | select(.url == $url) | .id'
}

echo "== 3) Adding gift guides, add-ons, artwork & brand audit to each print package link =="
for key in "${!PACKAGE_LINKS[@]}"; do
  url="${PACKAGE_LINKS[$key]}"
  id=$(find_link_id "$url")
  if [ -z "$id" ]; then
    echo "  [!] Could not find a Payment Link matching $url for '$key' — skipping. Double-check the URL or that this key belongs to the account behind STRIPE_SECRET_KEY."
    continue
  fi
  echo "  Updating $key ($id) ..."
  curl -s "$API/payment_links/$id" -u "$AUTH" \
    -d "optional_items[0][price]=$PRICE_SMALL"       -d "optional_items[0][quantity]=1" \
    -d "optional_items[1][price]=$PRICE_MEDIUM"      -d "optional_items[1][quantity]=1" \
    -d "optional_items[2][price]=$PRICE_LARGE"       -d "optional_items[2][quantity]=1" \
    -d "optional_items[3][price]=$PRICE_ADDON"       -d "optional_items[3][quantity]=1" \
    -d "optional_items[3][adjustable_quantity][enabled]=true" \
    -d "optional_items[3][adjustable_quantity][minimum]=0" \
    -d "optional_items[3][adjustable_quantity][maximum]=10" \
    -d "optional_items[4][price]=$PRICE_ARTWORK"     -d "optional_items[4][quantity]=1" \
    -d "optional_items[5][price]=$PRICE_BRAND_AUDIT" -d "optional_items[5][quantity]=1" \
    -d "allow_promotion_codes=true" \
    > /dev/null
done
echo

echo "== 4) Creating a standalone 'Digital Campaign' Payment Link (no print package) =="
DIGITAL_LINK_JSON=$(curl -s "$API/payment_links" -u "$AUTH" \
  -d "line_items[0][price]=$PRICE_ADDON" \
  -d "line_items[0][quantity]=1" \
  -d "line_items[0][adjustable_quantity][enabled]=true" \
  -d "line_items[0][adjustable_quantity][minimum]=0" \
  -d "line_items[0][adjustable_quantity][maximum]=10" \
  -d "optional_items[0][price]=$PRICE_SMALL"       -d "optional_items[0][quantity]=1" \
  -d "optional_items[1][price]=$PRICE_MEDIUM"      -d "optional_items[1][quantity]=1" \
  -d "optional_items[2][price]=$PRICE_LARGE"       -d "optional_items[2][quantity]=1" \
  -d "optional_items[3][price]=$PRICE_BRAND_AUDIT" -d "optional_items[3][quantity]=1" \
  -d "allow_promotion_codes=true")
DIGITAL_LINK_URL=$(echo "$DIGITAL_LINK_JSON" | jq -r '.url')

echo "Digital Campaign link: $DIGITAL_LINK_URL"
echo
echo "== Done =="
echo "Next step: paste the Digital Campaign link above into NURTURE_STRIPE_LINKS"
echo "in index.html as the 'digitalOnly' entry so the calculator can route"
echo "digital-only campaigns straight to Stripe instead of Cal.com."
