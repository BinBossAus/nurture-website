# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

TABLE_IMG = "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=2400&q=80"
GIFT_IMG = "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=2000&q=80"

PARTS = [style_block()]

hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:40px 0 0">
  <span class="n-k">Partner with Nurture</span>
  <h1 class="n-h1" style="font-size:46px;max-width:22ch;margin:0 auto">Reach parents who read every word.</h1>
  <p class="n-lead" style="max-width:54ch;margin:22px auto 0;font-weight:300;font-size:19px;line-height:1.65">Bi-monthly print in over 1,000 Australian newsagents, permanent digital distribution, and a readership that keeps the magazine instead of recycling it.</p>
  <div style="display:flex;gap:16px;justify-content:center;margin-top:32px;flex-wrap:wrap">
    <a href="#book" class="n-cta">Request the media kit</a>
    <a href="#book" class="n-ghost">Book online</a>
  </div>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

table_html = f'<div style="position:relative;height:520px;background-image:url(\'{TABLE_IMG}\');background-size:cover;background-position:center;"></div>'
PARTS.append(one_col_container(table_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

strip_html = """
<div class="n-strip">
  <span>1,000+ newsagents</span><span>600+ national libraries</span><span>80K+ social</span><span>Bi-monthly since 2012</span>
</div>
"""
PARTS.append(one_col_container(strip_html, hundred_percent="no", padding_top="18px", padding_bottom="0"))

why_left = """
<span class="n-k">Why Nurture</span>
<h2 class="n-h2" style="font-size:34px">A values-led audience, not an impression count</h2>
<p class="n-lead" style="margin-top:18px;max-width:46ch;font-weight:300;font-size:18px">Our readers care how a thing was made and who made it. They read a magazine they paid for, cover to cover, and they keep it &mdash; which means your page is still in the house six months after it printed.</p>
<p class="n-lead" style="margin-top:14px;max-width:46ch;font-weight:300;font-size:18px">We don&#8217;t sell space and step away. We write your story into the issue in a way that fits how our readers read.</p>
"""
rows = [
    ("Print reach, annually", "30,000+"),
    ("Digital newsstands, worldwide", "20,000+"),
    ("National libraries, archived permanently", "600+"),
    ("Combined social following", "80,000+"),
    ("Newsletter subscribers", "3,000+"),
    ("Website, monthly views", "1,400"),
]
rows_html = "".join(
    f'<div style="display:flex;justify-content:space-between;gap:20px;padding:14px 0;border-bottom:1px solid rgba(215,203,194,.35);font-size:15px">'
    f'<span>{label}</span><strong style="font-family:\'Playfair Display\',Georgia,serif;font-weight:500">{val}</strong></div>'
    for label, val in rows
)
why_right = f'<div class="nurture-glass" style="padding:40px">{rows_html}</div>'
PARTS.append(two_col_container(why_left, why_right, "3_5", "2_5", hundred_percent="no", padding_top="70px", padding_bottom="20px"))

PARTS.append(hr())

packages = [
    ("In the magazine", "Product and brand advertorial features, written with you. Print and digital exposure, with QR codes linking straight to your shop."),
    ("Around the magazine", "Social, website, newsletter and blog exposure. Exclusive giveaways and reader promotions."),
    ("All year round", "A listing in the Natural Parenting Directory, and a place in the seasonal digital gift guides."),
]
package_cards = "".join(
    f'<div class="nurture-glass n-lift" style="padding:34px"><h3 class="n-h3" style="font-size:21px">{t}</h3><p class="n-lead" style="font-size:15px;margin-top:12px">{d}</p></div>'
    for t, d in packages
)
packages_html = f"""
<div style="text-align:center;max-width:56ch;margin:0 auto">
  <span class="n-k">Our packages</span>
  <h2 class="n-h2" style="font-size:34px">Flexible from one issue to a full year</h2>
  <p class="n-lead" style="margin-top:16px;font-weight:300;font-size:18px">Start-up, small business or established ethical brand &mdash; the inclusions are the same, the scale is yours.</p>
</div>
<div class="n-grid n-grid-3" style="margin-top:44px;gap:24px">{package_cards}</div>
"""
PARTS.append(one_col_container(packages_html, hundred_percent="no", padding_top="20px", padding_bottom="20px"))

guide_banner = f"""
<div style="position:relative;height:440px;background-image:url('{GIFT_IMG}');background-size:cover;background-position:center;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding-bottom:32px;text-align:center">
  <span class="n-k">Three guides a year</span>
  <h2 class="n-h2" style="font-size:32px;max-width:26ch;color:#3a2d28">Add a gift guide for reach and frequency</h2>
</div>
"""
PARTS.append(one_col_container(guide_banner, hundred_percent="yes", padding_top="30px", padding_bottom="0", **{"class": "nurture-fade"}))

guides = [
    ("Mama&#8217;s May", "For mothers, all month long."),
    ("The Baby Shower Edition", "Practical, playful, heartfelt."),
    ("The Natural Family Christmas Guide", "Gifts for the whole family."),
]
guide_cards = "".join(
    f'<div class="nurture-glass n-lift" style="padding:32px"><h3 class="n-h3" style="font-size:20px">{t}</h3><p class="n-lead" style="font-size:15px;margin-top:10px">{d}</p></div>'
    for t, d in guides
)
guides_html = f"""
<div class="n-grid n-grid-3" style="gap:24px">{guide_cards}</div>
<p class="n-lead" style="text-align:center;max-width:56ch;margin:30px auto 0;font-size:15px">The same discount applies at checkout when a guide is added to a print package.</p>
"""
PARTS.append(one_col_container(guides_html, hundred_percent="no", padding_top="40px", padding_bottom="20px"))

PARTS.append(hr())

discounts_left = """
<span class="n-k">Discounts</span>
<h2 class="n-h2" style="font-size:34px">Book longer, pay less, stay flexible</h2>
<p class="n-lead" style="margin-top:18px;max-width:44ch;font-weight:300;font-size:18px">Book one issue or all six. Campaigns booked upfront are discounted and invoiced issue by issue, so the saving doesn&#8217;t cost you cash flow. Change your package or your artwork between issues.</p>
"""
discounts = [("2%", "Two issues"), ("4%", "Three issues"), ("6%", "Four issues"), ("10%", "Full year, six issues")]
discount_cards = "".join(
    f'<div class="nurture-glass" style="padding:28px"><span style="font-family:\'Playfair Display\',Georgia,serif;font-size:38px;color:{"#8c6f61" if p == "10%" else "#3a2d28"}">{p}</span><p class="n-lead" style="font-size:14px;margin-top:8px">{d}</p></div>'
    for p, d in discounts
)
discounts_right = f'<div class="n-grid n-grid-2" style="gap:16px">{discount_cards}</div>'
PARTS.append(two_col_container(discounts_left, discounts_right, "2_5", "3_5", hundred_percent="no", padding_top="20px", padding_bottom="20px"))

PARTS.append(hr())

purpose_html = """
<div style="text-align:center;max-width:58ch;margin:0 auto">
  <span class="n-k">Published with purpose</span>
  <h2 class="n-h2" style="font-size:34px">A keepsake, not a disposable</h2>
  <p class="n-lead" style="margin-top:18px;font-weight:300;font-size:18px">Recycled paper, plant-based inks, compostable satchels, and research-backed articles by writers our readers already trust. That&#8217;s why the magazine gets kept &mdash; and why your page keeps working.</p>
</div>
"""
PARTS.append(one_col_container(purpose_html, hundred_percent="no", padding_top="20px", padding_bottom="20px"))

book_html = """
<div class="nurture-glass" style="padding:56px;text-align:center" id="book">
  <span class="n-k">How to book</span>
  <h2 class="n-h2" style="font-size:32px;max-width:24ch;margin:0 auto">Two ways in</h2>
  <p class="n-lead" style="max-width:52ch;margin:18px auto 0;font-weight:300;font-size:18px">The media kit has packages, add-ons, deadlines, specs and rates. Complete the form below to receive it, or book online through the link inside the kit.</p>
  <p class="n-lead" style="max-width:52ch;margin:12px auto 0;font-size:15px">We track your deadlines, send a proof before every on-sale date, and post you a copy of each issue you appear in.</p>
  <div style="display:flex;gap:14px;justify-content:center;margin-top:28px;flex-wrap:wrap">
    <a href="mailto:advertise@nurtureparentingmagazine.com.au?subject=Media%20kit%20request" class="n-cta">Request the media kit</a>
    <a href="/contact/" class="n-ghost">Book online</a>
  </div>
  <p style="font-size:12px;color:rgba(58,45,40,.5);margin-top:16px">Emails advertise@nurtureparentingmagazine.com.au directly &mdash; swap for a Tally.so form link once one is published.</p>
</div>
"""
PARTS.append(one_col_container(book_html, hundred_percent="no", padding_top="10px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/advertise_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
