# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, hr

PARTS = [style_block()]

hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:40px 0 0">
  <span class="n-k">Free to read</span>
  <h1 class="n-h1" style="font-size:44px;max-width:20ch;margin:0 auto">The natural parenting blog</h1>
  <p class="n-lead" style="max-width:54ch;margin:22px auto 0;font-weight:300;font-size:18px">Evidence-based writing on the emotional, intellectual, physical and spiritual sides of raising children &mdash; free, and updated between issues.</p>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

chips = [
    ("All articles", "/blog/", True),
    ("Emotional", "/category/emotional/", False),
    ("Intellectual", "/category/intellectual/", False),
    ("Physical", "/category/physical/", False),
    ("Spiritual", "/category/spiritual/", False),
]
chip_html = "".join(
    f'<a href="{href}" class="n-chip{" active" if active else ""}">{label}</a>'
    for label, href, active in chips
)
chips_wrap = f'<div style="display:flex;gap:10px;flex-wrap:wrap;justify-content:center">{chip_html}</div>'
PARTS.append(one_col_container(chips_wrap, hundred_percent="no", padding_top="34px", padding_bottom="10px"))

# Real posts grid, reusing the [fusion_recent_posts] element (found on the
# pre-rebrand export of this page) so all 43 existing posts keep their copy
# and simply inherit the new card design via the Typography + Colour Spec
# settings already applied in Avada Options.
grid_shortcode = (
    '[fusion_recent_posts layout="default" hover_type="zoomin" columns="3" number_posts="9" '
    'offset="0" pull_by="category" thumbnail="yes" title="yes" meta="yes" meta_author="no" '
    'meta_categories="yes" meta_date="no" meta_comments="no" meta_tags="no" '
    'content_alignment="left" excerpt="yes" excerpt_length="18" strip_html="yes" '
    'scrolling="pagination" /]'
)
PARTS.append(
    f'[fusion_builder_container hundred_percent="no" padding_top="10px" padding_bottom="60px"]'
    f'[fusion_builder_row][fusion_builder_column type="1_1"]{grid_shortcode}[/fusion_builder_column]'
    f'[/fusion_builder_row][/fusion_builder_container]'
)

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/blog_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
