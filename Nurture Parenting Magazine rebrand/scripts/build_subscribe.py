# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

BED_IMG = "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=2400&q=80"

PARTS = [style_block()]

hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:40px 0 0">
  <span class="n-k">Subscribe &middot; bi-monthly &middot; shipping included</span>
  <h1 class="n-h1" style="font-size:44px;max-width:19ch;margin:0 auto">A magazine you keep, not a feed you scroll.</h1>
  <p class="n-lead" style="max-width:54ch;margin:22px auto 0;font-weight:300;font-size:19px;line-height:1.65">Eighty pages, six times a year, posted anywhere in Australia. No auto-renewal, no lock-in, and nothing sold to a third party.</p>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

banner_html = f'<div style="position:relative;height:420px;background-image:url(\'{BED_IMG}\');background-size:cover;background-position:center;"></div>'
PARTS.append(one_col_container(banner_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

tiers_html = """
<div class="n-grid n-grid-3" style="gap:26px;align-items:stretch">
  <div class="nurture-glass n-lift" style="padding:40px 34px;display:flex;flex-direction:column">
    <span class="n-k" style="margin-bottom:12px">Try it</span>
    <h3 class="n-h3" style="font-size:26px">One issue</h3>
    <p style="font-family:'Playfair Display',Georgia,serif;font-size:46px;line-height:1;margin:18px 0 4px;color:#3a2d28">$20</p>
    <p style="font-size:13.5px;color:rgba(58,45,40,.6);margin:0 0 22px">Single issue &middot; shipping included</p>
    <div style="height:1px;background:rgba(215,203,194,.35);margin:0 0 20px"></div>
    <p style="font-size:14.5px;line-height:1.75;color:rgba(58,45,40,.7);margin:0 0 26px;flex:1">The current issue, posted in a compostable satchel. The easiest way to see whether Nurture is for you.</p>
    <a href="/shop/" class="n-ghost" style="justify-content:center;width:100%;box-sizing:border-box">Buy one issue</a>
  </div>
  <div class="nurture-glass n-lift" style="padding:40px 34px;display:flex;flex-direction:column">
    <span class="n-k" style="margin-bottom:12px">Six months</span>
    <h3 class="n-h3" style="font-size:26px">Three issues</h3>
    <p style="font-family:'Playfair Display',Georgia,serif;font-size:46px;line-height:1;margin:18px 0 4px;color:#3a2d28">$55</p>
    <p style="font-size:13.5px;color:rgba(58,45,40,.6);margin:0 0 22px">$18.33 an issue &middot; shipping included</p>
    <div style="height:1px;background:rgba(215,203,194,.35);margin:0 0 20px"></div>
    <p style="font-size:14.5px;line-height:1.75;color:rgba(58,45,40,.7);margin:0 0 26px;flex:1">Half a year of Nurture, and access to the private mentor group for the length of your subscription.</p>
    <a href="/shop/" class="n-ghost" style="justify-content:center;width:100%;box-sizing:border-box">Choose three</a>
  </div>
  <div class="nurture-glass n-lift" style="padding:40px 34px;display:flex;flex-direction:column;border-color:rgba(203,177,165,.7);position:relative">
    <span style="position:absolute;top:-13px;left:34px;background:#cbb1a5;color:#3a2d28;font:500 10px/1 'Inter',sans-serif;letter-spacing:.16em;text-transform:uppercase;padding:8px 14px;border-radius:30px">Best value</span>
    <span class="n-k" style="margin-bottom:12px">A full year</span>
    <h3 class="n-h3" style="font-size:26px">Six issues</h3>
    <p style="font-family:'Playfair Display',Georgia,serif;font-size:46px;line-height:1;margin:18px 0 4px;color:#3a2d28">$95</p>
    <p style="font-size:13.5px;color:rgba(58,45,40,.6);margin:0 0 22px">$15.83 an issue &middot; shipping included</p>
    <div style="height:1px;background:rgba(215,203,194,.35);margin:0 0 20px"></div>
    <p style="font-size:14.5px;line-height:1.75;color:rgba(58,45,40,.7);margin:0 0 26px;flex:1">A full year, the mentor group, early access to all three gift guides, and one tree planted in your name.</p>
    <a href="/shop/" class="n-cta" style="justify-content:center;width:100%;box-sizing:border-box">Subscribe for a year</a>
  </div>
</div>
<p style="text-align:center;font-size:13px;color:rgba(58,45,40,.6);margin:30px 0 0">Prices in AUD. Australian delivery included &middot; international from $12 an issue &middot; cancel any time.</p>
"""
PARTS.append(one_col_container(tiers_html, hundred_percent="no", padding_top="24px", padding_bottom="20px"))

PARTS.append(hr())

issue_left = """
<span class="n-k">What&#8217;s in every issue</span>
<h2 class="n-h2" style="font-size:32px;max-width:16ch">Eighty pages, no advertorial dressed as advice</h2>
"""
issue_items = [
    ("01", "Long-form interviews", "Practitioners and parents, at length, in their own words."),
    ("02", "Evidence-based features", "Sleep, feeding, birth and early learning &mdash; sourced and cited."),
    ("03", "The conscious directory", "Australian makers and practitioners we&#8217;ve actually met."),
    ("04", "Something to keep", "A planner, a poster or a recipe card in the centre spread."),
]
issue_rows = "".join(
    f'<div style="display:grid;grid-template-columns:auto 1fr;gap:22px;padding:20px 0;border-bottom:1px solid rgba(215,203,194,.35)">'
    f'<span style="font-family:\'Playfair Display\',Georgia,serif;font-size:19px;color:#a98a7b">{n}</span>'
    f'<span><strong style="font-weight:600;display:block;margin-bottom:5px;color:#3a2d28">{t}</strong><span style="font-size:14.5px;color:rgba(58,45,40,.6)">{d}</span></span></div>'
    for n, t, d in issue_items
)
issue_left_full = issue_left + f'<div style="margin-top:30px">{issue_rows}</div>'
issue_right = '<div class="n-ph" style="height:420px;border-radius:20px"></div>'
PARTS.append(two_col_container(issue_left_full, issue_right, "1_2", "1_2", hundred_percent="no", padding_top="20px", padding_bottom="20px"))

PARTS.append(hr())

gift_head = """
<div style="text-align:center;max-width:56ch;margin:0 auto 44px">
  <span class="n-k">Give it away</span>
  <h2 class="n-h2" style="font-size:32px">A gift that turns up six times</h2>
  <p class="n-lead" style="margin-top:18px;font-weight:300;font-size:18px">Send a subscription to a new parent and we&#8217;ll post a handwritten card with the first issue. Tell us what to write.</p>
</div>
"""
gift_tiers = [
    ("Gift three issues", "$55 &middot; six months, card included."),
    ("Gift six issues", "$95 &middot; a full year, card and a planted tree."),
    ("Baby shower bundle", "$120 &middot; a year, plus the current gift guide picks."),
]
gift_cards = "".join(
    f'<div class="nurture-glass n-lift" style="padding:32px"><h3 class="n-h3" style="font-size:21px">{t}</h3>'
    f'<p style="font-size:14.5px;line-height:1.75;color:rgba(58,45,40,.6);margin:10px 0 20px">{d}</p>'
    f'<a href="/shop/" class="n-ghost" style="justify-content:center;width:100%;box-sizing:border-box">Gift this</a></div>'
    for t, d in gift_tiers
)
gift_html = gift_head + f'<div class="n-grid n-grid-3" style="gap:24px">{gift_cards}</div>'
PARTS.append(one_col_container(gift_html, hundred_percent="no", padding_top="20px", padding_bottom="20px"))

PARTS.append(hr())

faq_left = '<span class="n-k">Before you ask</span><h2 class="n-h2" style="font-size:30px;max-width:14ch">The questions we get most</h2>'
faqs = [
    ("When will my first issue arrive?", "Within ten business days if an issue is in print, or on release day if you subscribe between issues. We&#8217;ll email you either way."),
    ("Does it renew automatically?", "No. Your subscription runs its term and stops. We&#8217;ll send one reminder before the last issue, and that&#8217;s it."),
    ("Can I read it digitally?", "Yes &mdash; every print subscription includes the digital edition, and back issues are available on their own from the shop."),
    ("Do you ship overseas?", "We do, from $12 an issue depending on the country. Choose your destination at checkout and the price updates."),
]
faq_rows = "".join(
    f'<div style="padding:22px 0;border-bottom:1px solid rgba(215,203,194,.35)"><h4 class="n-h3" style="font-size:18px;margin-bottom:8px">{q}</h4>'
    f'<p style="font-size:15px;line-height:1.75;color:rgba(58,45,40,.62);margin:0">{a}</p></div>'
    for q, a in faqs
)
PARTS.append(two_col_container(faq_left, f'<div>{faq_rows}</div>', "2_5", "3_5", hundred_percent="no", padding_top="20px", padding_bottom="20px"))

closing_html = """
<div class="nurture-glass" style="padding:56px;text-align:center">
  <span class="n-k">Still deciding?</span>
  <h2 class="n-h2" style="font-size:30px;max-width:20ch;margin:0 auto">Read one issue first. $20, posted.</h2>
  <div style="display:flex;gap:14px;justify-content:center;margin-top:28px;flex-wrap:wrap">
    <a href="/shop/" class="n-cta">Buy one issue</a>
    <a href="/blog/" class="n-ghost">Read the blog free</a>
  </div>
</div>
"""
PARTS.append(one_col_container(closing_html, hundred_percent="no", padding_top="10px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/subscribe_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
