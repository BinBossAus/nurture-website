# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

PARTS = [style_block()]

hero_html = """
<span class="n-k">The shop</span>
<h1 class="n-h1" style="font-size:44px;max-width:17ch">Back issues, bundles and things worth keeping.</h1>
<p class="n-lead" style="max-width:52ch;margin:22px 0 0;font-weight:300;font-size:18px">Every order ships in a compostable satchel, printed on FSC recycled stock. Australian delivery included on subscriptions.</p>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

chips = [
    ("All products", "/shop/", True),
    ("Print &amp; subscriptions", "/product-category/print/", False),
    ("eMagazine", "/product-category/emagazine/", False),
    ("Gift guides", "/product-category/gift-guide/", False),
    ("Advertise &amp; add-ons", "/product-category/advertise/", False),
]
chip_html = "".join(
    f'<a href="{href}" class="n-chip{" active" if active else ""}">{label}</a>'
    for label, href, active in chips
)
chips_wrap = f'<div style="display:flex;gap:10px;flex-wrap:wrap">{chip_html}</div>'
PARTS.append(one_col_container(chips_wrap, hundred_percent="no", padding_top="36px", padding_bottom="0"))

note_html = """
<p style="font-size:13.5px;color:rgba(58,45,40,.55);margin:20px 0 0">Every product below is pulled live from the store &mdash; prices and stock always match checkout.</p>
"""
PARTS.append(one_col_container(note_html, hundred_percent="no", padding_top="6px", padding_bottom="10px"))

# Real product sections, reusing the same [fusion_woo_product_grid] element the
# previous version of this page used (found in the pre-rebrand export) so the
# live catalogue keeps rendering with correct prices/stock/checkout links.
product_sections = [
    ("Print &amp; subscriptions", "print", "print,subscribe", "advertise,ezine,gift-guide,packages,emagazine,emag"),
    ("eMagazine", "emagazine", "emagazine,emag", "advertise,ezine,gift-guide,packages,print,subscribe"),
    ("Gift guides", "gift-guide", "gift-guide", "advertise,ezine,packages,print,subscribe,emagazine,emag"),
    ("Advertise &amp; add-ons", "packages", "packages,advertise,add-ons", "ezine,gift-guide,print,subscribe,emagazine,emag"),
]
for label, cat_slug, _tag, exclude in product_sections:
    heading = f'<h2 class="n-h2" style="font-size:26px;margin-bottom:18px">{label}</h2>'
    PARTS.append(one_col_container(heading, hundred_percent="no", padding_top="30px", padding_bottom="0"))
    grid_shortcode = (
        f'[fusion_woo_product_grid pull_by="category" offset="0" orderby="menu_order" order="ASC" '
        f'show_thumbnail="yes" show_title="yes" show_price="yes" show_rating="no" show_buttons="yes" '
        f'scrolling="pagination" cat_slug="{cat_slug}" columns="3" number_posts="12" exclude_cats="{exclude}" /]'
    )
    PARTS.append(
        f'[fusion_builder_container hundred_percent="no" padding_top="0" padding_bottom="10px"]'
        f'[fusion_builder_row][fusion_builder_column type="1_1"]{grid_shortcode}[/fusion_builder_column]'
        f'[/fusion_builder_row][/fusion_builder_container]'
    )

PARTS.append(hr())

directory_left = '<div class="n-ph" style="height:420px;border-radius:20px"></div>'
directory_right = """
<span class="n-k">The conscious directory</span>
<h2 class="n-h2" style="font-size:32px;max-width:15ch">Australian makers we&#8217;ve actually met</h2>
<p class="n-lead" style="margin:18px 0 26px;max-width:44ch;font-weight:300;font-size:18px">Practitioners, small brands and services, listed because they earned it &mdash; not because they bought the slot. Search by state or by what you need.</p>
<div style="display:flex;gap:14px;flex-wrap:wrap">
  <a href="/directory/" class="n-cta">Browse the directory</a>
  <a href="/advertise/" class="n-ghost">List your business</a>
</div>
"""
PARTS.append(two_col_container(directory_left, directory_right, "1_2", "1_2", hundred_percent="no", padding_top="60px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/shop_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
