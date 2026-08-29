# -*- coding: utf-8 -*-
"""Shared helpers for generating Nurture Avada/Fusion Builder page content."""

STYLE = """<style>
.n-wrap{max-width:1180px;margin:0 auto;padding:0 40px}
.n-sec{max-width:1180px;margin:0 auto;padding:96px 40px}
.n-k{display:block;font:500 11px/1.4 'Inter',sans-serif;letter-spacing:.22em;text-transform:uppercase;color:#a98a7b;margin:0 0 16px}
.n-lead{font-size:17px;line-height:1.7;color:rgba(58,45,40,.72);margin:0}
.n-h1{font-family:'Playfair Display',Georgia,serif;font-weight:500;letter-spacing:-.02em;line-height:1.1;margin:0;color:#3a2d28}
.n-h2{font-family:'Playfair Display',Georgia,serif;font-weight:500;letter-spacing:-.02em;line-height:1.2;margin:0;color:#3a2d28}
.n-h3{font-family:'Playfair Display',Georgia,serif;font-weight:500;letter-spacing:-.01em;line-height:1.25;margin:0;color:#3a2d28}
.n-cta{display:inline-flex;align-items:center;justify-content:center;background:#cbb1a5;color:#3a2d28!important;font:500 13px/1 'Inter',sans-serif;letter-spacing:.09em;text-transform:uppercase;padding:17px 32px;border:0;border-radius:40px;text-decoration:none!important;cursor:pointer;box-shadow:0 4px 20px rgba(203,177,165,.28);transition:all .35s}
.n-cta:hover{background:#3a2d28;color:#fdfbf7!important;transform:translateY(-2px)}
.n-ghost{display:inline-flex;align-items:center;justify-content:center;background:transparent;color:#3a2d28!important;font:500 13px/1 'Inter',sans-serif;letter-spacing:.09em;text-transform:uppercase;padding:16px 30px;border:1px solid rgba(58,45,40,.22);border-radius:40px;text-decoration:none!important;cursor:pointer;transition:all .35s}
.n-ghost:hover{border-color:#cbb1a5;background:rgba(203,177,165,.09);transform:translateY(-2px)}
.n-lift{transition:transform .5s cubic-bezier(.2,.7,.2,1),box-shadow .5s}
.n-lift:hover{transform:translateY(-4px);box-shadow:0 18px 44px rgba(45,36,32,.09)}
.n-hr{height:1px;background:rgba(215,203,194,.35);border:0;max-width:1180px;margin:0 auto}
.n-ph{background:linear-gradient(160deg,#efe7e0,#e4d9d1 60%,#d9ccc3);position:relative;overflow:hidden;display:flex;align-items:flex-end}
.n-ph b{font:400 10px/1 ui-monospace,Menlo,monospace;letter-spacing:.1em;text-transform:uppercase;color:rgba(58,45,40,.4);padding:14px 16px}
.n-grid{display:grid;gap:16px}
.n-grid-2{grid-template-columns:repeat(2,1fr)}
.n-grid-3{grid-template-columns:repeat(3,1fr)}
.n-grid-4{grid-template-columns:repeat(4,1fr)}
.n-strip{display:flex;gap:40px;flex-wrap:wrap;justify-content:space-between;font:500 11px/1.5 'Inter',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:rgba(58,45,40,.62)}
.n-price{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:22px 26px;border-radius:16px}
.n-price .plan{font-family:'Playfair Display',Georgia,serif;font-size:21px;color:#3a2d28}
.n-price .sub{display:block;font-size:13.5px;color:rgba(58,45,40,.62);margin-top:4px;font-family:'Inter',sans-serif;font-weight:400}
.n-price .price{font-family:'Playfair Display',Georgia,serif;font-size:26px;color:#3a2d28}
.n-input{background:rgba(253,251,247,.9);border:1px solid rgba(215,203,194,.6);color:#3a2d28;border-radius:12px;padding:15px 18px;font:400 15px 'Inter',sans-serif;outline:none;flex:1}
.n-avatar{width:76px;height:76px;border-radius:50%}
.n-cover{border-radius:6px;overflow:hidden;box-shadow:0 14px 34px rgba(45,36,32,.14)}
.n-prose{max-width:64ch}
.n-prose p{font-size:17.5px;line-height:1.85;color:rgba(58,45,40,.82);margin:0 0 22px}
.n-pull{font-family:'Playfair Display',Georgia,serif;font-size:28px;line-height:1.3;color:#3a2d28;border-left:2px solid #cbb1a5;padding-left:26px;margin:34px 0}
.n-chip{display:inline-flex;align-items:center;padding:9px 18px;border-radius:40px;border:1px solid rgba(58,45,40,.2);font:500 12px/1 'Inter',sans-serif;letter-spacing:.06em;text-transform:uppercase;color:#3a2d28;text-decoration:none!important;cursor:pointer}
.n-chip.active,.n-chip:hover{background:#cbb1a5;border-color:#cbb1a5}
.n-tag{display:inline-flex;padding:5px 12px;border-radius:20px;background:rgba(203,177,165,.28);font:500 10.5px/1 'Inter',sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#3a2d28}
@media(max-width:900px){.n-sec{padding:56px 24px!important}.n-grid-3{grid-template-columns:1fr!important}.n-grid-2{grid-template-columns:1fr!important}.n-grid-4{grid-template-columns:repeat(2,1fr)!important}.n-strip{gap:20px}}
</style>"""


def container(inner, **attrs):
    a = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return f'[fusion_builder_container {a}][fusion_builder_row]{inner}[/fusion_builder_row][/fusion_builder_container]'


def column(html, col_type="1_1"):
    return (
        f'[fusion_builder_column type="{col_type}" layout="{col_type}"]'
        f'[fusion_text]{html}[/fusion_text]'
        f'[/fusion_builder_column]'
    )


def one_col_container(html, **attrs):
    return container(column(html), **attrs)


def two_col_container(html_left, html_right, ltype="1_2", rtype="1_2", **attrs):
    inner = column(html_left, ltype) + column(html_right, rtype)
    return container(inner, **attrs)


def three_col_container(a, b, c, ctype="1_3", **attrs):
    inner = column(a, ctype) + column(b, ctype) + column(c, ctype)
    return container(inner, **attrs)


def hr(**attrs):
    a = " ".join(f'{k}="{v}"' for k, v in attrs.items())
    return (
        f'[fusion_builder_container hundred_percent="no" padding_top="10px" padding_bottom="10px" {a}]'
        f'[fusion_builder_row][fusion_builder_column type="1_1"]'
        f'[fusion_separator style_type="single solid" top_margin="0" bottom_margin="0" '
        f'border_size="1" sep_color="rgba(215,203,194,.35)" width="100%" alignment="center" /]'
        f'[/fusion_builder_column][/fusion_builder_row][/fusion_builder_container]'
    )


def style_block():
    return one_col_container(STYLE, hundred_percent="yes", padding_top="0", padding_bottom="0")


def full_bleed_fade(html_inner, height="520px", **attrs):
    """A 100%-width container with the nurture-fade class, no separator/curve."""
    wrapped = f'<div style="position:relative;height:{height}">{html_inner}</div>'
    return one_col_container(wrapped, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade", **attrs})
