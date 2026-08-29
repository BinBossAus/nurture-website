# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, hr

BANNER_IMG = "https://images.unsplash.com/photo-1491013516836-7db643ee125a?auto=format&fit=crop&w=2400&q=80"

PARTS = [style_block()]

hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:40px 0 0">
  <span class="n-k">The conscious directory</span>
  <h1 class="n-h1" style="font-size:44px;max-width:18ch;margin:0 auto">Australian makers we&#8217;ve actually met.</h1>
  <p class="n-lead" style="max-width:56ch;margin:22px auto 0;font-weight:300;font-size:18px">Practitioners, small brands and services, listed because they earned it &mdash; not because they bought the slot. This is the page every print QR code points to.</p>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

banner_html = f'<div style="position:relative;height:400px;background-image:url(\'{BANNER_IMG}\');background-size:cover;background-position:center;"></div>'
PARTS.append(one_col_container(banner_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

categories = [
    ("All", True), ("Pregnancy &amp; birth", False), ("Feeding", False),
    ("Sleep", False), ("Play &amp; learning", False), ("Home &amp; sustainability", False),
    ("Wellbeing", False), ("Services", False),
]
chip_html = "".join(
    f'<span class="n-chip{" active" if active else ""}">{label}</span>'
    for label, active in categories
)
chips_wrap = f'<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center">{chip_html}</div>'
PARTS.append(one_col_container(chips_wrap, hundred_percent="no", padding_top="34px", padding_bottom="0"))

note_html = """
<p style="text-align:center;font-size:13.5px;color:rgba(58,45,40,.55);margin:20px 0 0;max-width:60ch;margin-left:auto;margin-right:auto">Filtering by category is coming as listings are added &mdash; for now, browse everything below.</p>
"""
PARTS.append(one_col_container(note_html, hundred_percent="no", padding_top="6px", padding_bottom="0"))

# One reusable "advertiser card" template, duplicated per listing. Two
# illustrative example cards ship with the page so the format is obvious;
# duplicate the pattern in the Builder (or via the REST API / a future Nara
# tool) for every real advertiser, grouped by category.
example_cards = [
    (
        "Example listing",
        "Pregnancy &amp; birth",
        "This is a placeholder card showing the format every advertiser gets: a logo, one line of description, a category tag and an outbound link. Replace with your first real listing.",
        "#",
    ),
    (
        "Your brand here",
        "Services",
        "Advertisers get a permanent card here for the length of their package &mdash; renewed each issue, never expired mid-campaign. Ask about the Directory listing add-on.",
        "/advertise/",
    ),
]
card_html = "".join(
    f'<a href="{link}" class="nurture-glass n-lift" style="padding:0;overflow:hidden;display:block;text-decoration:none">'
    f'<div class="n-ph" style="aspect-ratio:16/9;display:flex;align-items:center;justify-content:center">'
    f'<span style="font:400 10px ui-monospace,Menlo,monospace;letter-spacing:.1em;text-transform:uppercase;color:rgba(58,45,40,.4)">logo</span></div>'
    f'<div style="padding:24px 26px 28px">'
    f'<span class="n-tag" style="margin-bottom:12px;display:inline-flex">{cat}</span>'
    f'<h3 class="n-h3" style="font-size:20px;margin-top:12px">{name}</h3>'
    f'<p style="font-size:14px;line-height:1.65;color:rgba(58,45,40,.62);margin:10px 0 0">{desc}</p>'
    f'</div></a>'
    for name, cat, desc, link in example_cards
)
grid_html = f'<div class="n-grid n-grid-3" style="gap:26px">{card_html}</div>'
PARTS.append(one_col_container(grid_html, hundred_percent="no", padding_top="40px", padding_bottom="20px"))

PARTS.append(hr())

cta_html = """
<div class="nurture-glass" style="padding:56px;text-align:center">
  <span class="n-k">List your business</span>
  <h2 class="n-h2" style="font-size:32px;max-width:20ch;margin:0 auto">Want to be in the directory?</h2>
  <p class="n-lead" style="max-width:48ch;margin:18px auto 0;font-weight:300;font-size:18px">A directory listing comes with every advertising package, and we meet every advertiser before their card goes live.</p>
  <div style="display:flex;gap:14px;justify-content:center;margin-top:28px;flex-wrap:wrap">
    <a href="/advertise/" class="n-cta">See advertising packages</a>
    <a href="/contact/" class="n-ghost">Ask a question</a>
  </div>
</div>
"""
PARTS.append(one_col_container(cta_html, hundred_percent="no", padding_top="10px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/directory_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
