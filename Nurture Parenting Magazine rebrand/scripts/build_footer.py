# -*- coding: utf-8 -*-
"""Rebuilds the sitewide footer (Avada Theme Builder layout section, post 1245 —
"Nurture Custom Footer", actually still the unmodified Barber Shop demo footer)
per the Page Build Sheet section 11 spec."""

logo_html = """
<div style="font-family:'Playfair Display',Georgia,serif;font-weight:500;font-size:30px;color:#fdfbf7">Nurture<span style="color:#cbb1a5">.</span></div>
<p style="font-size:13.5px;line-height:1.8;margin:16px 0 0;max-width:32ch;color:rgba(253,251,247,.72);font-family:'Inter',sans-serif">Nurture Parenting Magazine &middot; PO Box 2292, Burleigh Post Shop QLD 4220 &middot; ABN 15 617 938 013</p>
"""

def footer_col(heading, links):
    items = "".join(
        f'<a href="{href}" style="display:block;color:rgba(253,251,247,.74);font-size:13.5px;text-decoration:none;margin-bottom:10px;font-family:\'Inter\',sans-serif" onmouseover="this.style.color=\'#fdfbf7\'" onmouseout="this.style.color=\'rgba(253,251,247,.74)\'">{label}</a>'
        for label, href in links
    )
    return (
        f'<p style="font:500 10.5px/1 \'Inter\',sans-serif;letter-spacing:.2em;text-transform:uppercase;'
        f'color:rgba(253,251,247,.42);margin:0 0 16px">{heading}</p>{items}'
    )

read_col = footer_col("Read", [
    ("Blog", "/blog/"),
    ("Back issues", "/shop/"),
    ("Gift guides", "/showcase/"),
])
shop_col = footer_col("Shop", [
    ("Subscribe", "/subscribe/"),
    ("Single issues", "/shop/"),
    ("Directory", "/directory/"),
])
nurture_col = footer_col("Nurture", [
    ("Advertise", "/advertise/"),
    ("Contact", "/contact/"),
    ("Our story", "/our-story/"),
    ("Contributors", "/contributors/"),
])

copyright_html = (
    '<div style="max-width:1180px;margin:0 auto;padding-top:24px;margin-top:40px;'
    'border-top:1px solid rgba(253,251,247,.12)">'
    '<p style="font-size:12px;color:rgba(253,251,247,.4);margin:0;font-family:\'Inter\',sans-serif">'
    '&copy; 2012&#8211;2026 Nurture Global Pty Ltd. All rights reserved.</p></div>'
)

def column(html, col_type):
    return (
        f'[fusion_builder_column type="{col_type}" layout="{col_type}"]'
        f'[fusion_text]{html}[/fusion_text]'
        f'[/fusion_builder_column]'
    )

row_cols = (
    column(logo_html, "2_5")
    + column(read_col, "1_5")
    + column(shop_col, "1_5")
    + column(nurture_col, "1_5")
)

FOOTER_CONTENT = (
    '[fusion_builder_container type="flex" hundred_percent="no" hundred_percent_height="no" '
    'background_color="#3A2D28" padding_top="76px" padding_bottom="44px" padding_left="72px" '
    'padding_right="72px"]'
    f'[fusion_builder_row]{row_cols}[/fusion_builder_row]'
    '[/fusion_builder_container]'
    '[fusion_builder_container type="flex" hundred_percent="no" hundred_percent_height="no" '
    'background_color="#3A2D28" padding_top="0" padding_bottom="30px" padding_left="72px" '
    'padding_right="72px"]'
    f'[fusion_builder_row][fusion_builder_column type="1_1" layout="1_1"][fusion_text]{copyright_html}[/fusion_text][/fusion_builder_column][/fusion_builder_row]'
    '[/fusion_builder_container]'
)

if __name__ == "__main__":
    with open("/tmp/footer_content.txt", "w") as f:
        f.write(FOOTER_CONTENT)
    print("Length:", len(FOOTER_CONTENT))
