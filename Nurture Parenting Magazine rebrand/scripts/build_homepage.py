# -*- coding: utf-8 -*-
"""Generates the Fusion Builder shortcode content for the Nurture homepage rebuild."""

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
.n-strip{display:flex;gap:40px;flex-wrap:wrap;justify-content:space-between;font:500 11px/1.5 'Inter',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:rgba(58,45,40,.62)}
.n-price{display:flex;justify-content:space-between;align-items:baseline;gap:20px;padding:22px 26px;border-radius:16px}
.n-price .plan{font-family:'Playfair Display',Georgia,serif;font-size:21px;color:#3a2d28}
.n-price .sub{display:block;font-size:13.5px;color:rgba(58,45,40,.62);margin-top:4px;font-family:'Inter',sans-serif;font-weight:400}
.n-price .price{font-family:'Playfair Display',Georgia,serif;font-size:26px;color:#3a2d28}
.n-input{background:rgba(253,251,247,.9);border:1px solid rgba(215,203,194,.6);color:#3a2d28;border-radius:12px;padding:15px 18px;font:400 15px 'Inter',sans-serif;outline:none;flex:1}
.n-avatar{width:76px;height:76px;border-radius:50%}
.n-cover{border-radius:6px;overflow:hidden;box-shadow:0 14px 34px rgba(45,36,32,.14)}
@media(max-width:900px){.n-sec{padding:56px 24px!important}.n-grid-3{grid-template-columns:1fr!important}.n-grid-2{grid-template-columns:1fr!important}.n-strip{gap:20px}}
</style>"""

HERO_IMG = "https://images.unsplash.com/photo-1476703993599-0035a21b17a9?auto=format&fit=crop&w=2400&q=80"
BLOG_IMG = "https://images.unsplash.com/photo-1503454537195-1dcabb73ffb9?auto=format&fit=crop&w=2400&q=80"
GIFT_IMG = "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=2000&q=80"
ARTICLE_IMGS = [
    "https://images.unsplash.com/photo-1491013516836-7db643ee125a?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1519689680058-324335c77eba?auto=format&fit=crop&w=900&q=80",
    "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=900&q=80",
]


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


PARTS = []

# 0. Page-scoped style block
PARTS.append(one_col_container(STYLE, hundred_percent="yes", padding_top="0", padding_bottom="0"))

# 1. HERO
hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:56px 0 0">
  <span class="n-k">Australia&#8217;s natural parenting magazine &middot; since 2012</span>
  <h1 class="n-h1" style="font-size:46px;max-width:20ch;margin:0 auto">Raising children is not a trend.</h1>
  <p class="n-lead" style="max-width:52ch;margin:24px auto 0;font-weight:300;font-size:21px;line-height:1.6">Eighty pages, six times a year. Printed here on recycled stock with plant-based inks, and posted to your door in a compostable satchel.</p>
  <div style="display:flex;gap:16px;justify-content:center;margin-top:34px;flex-wrap:wrap">
    <a href="/subscribe/" class="n-cta">Subscribe from $20</a>
    <a href="/blog/" class="n-ghost">Read the blog</a>
  </div>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="70px", padding_bottom="0"))

# 2. HERO IMAGE (full bleed, fade)
hero_img_html = f"""
<div style="position:relative;height:620px;background-image:url('{HERO_IMG}');background-size:cover;background-position:center;"></div>
"""
PARTS.append(one_col_container(hero_img_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

# 3. TRUST STRIP
trust_html = """
<div class="n-strip">
  <span>1,000+ Australian newsagents</span><span>40,000 online newsstands</span><span>FSC recycled stock</span><span>Plant-based inks</span><span>WHO &amp; TGA compliant</span>
</div>
"""
PARTS.append(one_col_container(trust_html, hundred_percent="no", padding_top="18px", padding_bottom="0"))

# 4. COVERS + PRICING
covers_html = """
<div id="issue" style="position:relative;top:-90px"></div>
<div style="position:relative;height:480px">
  <div class="n-cover" style="position:absolute;left:32%;top:9%;width:44%;transform:rotate(3deg)"><div class="n-ph" style="aspect-ratio:1093/1400"><b>issue 40</b></div></div>
  <div class="n-cover" style="position:absolute;left:20%;top:4%;width:47%;transform:rotate(1deg)"><div class="n-ph" style="aspect-ratio:1093/1400"><b>issue 41</b></div></div>
  <div class="n-cover" style="position:absolute;left:8%;top:0;width:51%;box-shadow:0 22px 48px rgba(45,36,32,.18)"><div class="n-ph" style="aspect-ratio:1093/1400"><b>current issue cover</b></div></div>
</div>
"""
pricing_html = """
<span class="n-k">Out now</span>
<h2 class="n-h2" style="font-size:34px">Six issues a year, posted to your door</h2>
<p class="n-lead" style="margin-top:18px;max-width:46ch;font-weight:300;font-size:18px">Interviews and evidence-based writing on the emotional, physical, intellectual and spiritual parts of raising children &mdash; pregnancy through the early learning years.</p>
<div style="display:flex;flex-direction:column;gap:12px;margin:28px 0 26px;max-width:440px">
  <div class="nurture-glass n-lift n-price"><span><span class="plan">One issue</span><span class="sub">Try it. Shipping included.</span></span><span class="price">$20</span></div>
  <div class="nurture-glass n-lift n-price"><span><span class="plan">Three issues</span><span class="sub">Six months. Shipping included.</span></span><span class="price">$55</span></div>
  <div class="nurture-glass n-lift n-price" style="border-color:rgba(203,177,165,.65)"><span><span class="plan">Six issues</span><span class="sub">A full year, and a tree planted in your name.</span></span><span class="price">$95</span></div>
</div>
<div style="display:flex;gap:14px;flex-wrap:wrap"><a href="/subscribe/" class="n-cta">Subscribe</a><a href="/shop/" class="n-ghost">Buy this issue</a></div>
"""
PARTS.append(two_col_container(covers_html, pricing_html, "1_2", "1_2", hundred_percent="no", padding_top="88px", padding_bottom="20px"))

PARTS.append('[fusion_builder_container hundred_percent="no" padding_top="10px" padding_bottom="10px"][fusion_builder_row][fusion_builder_column type="1_1"][fusion_separator style_type="single solid" top_margin="0" bottom_margin="0" border_size="1" sep_color="rgba(215,203,194,.35)" width="100%" alignment="center" /][/fusion_builder_column][/fusion_builder_row][/fusion_builder_container]')

# 5. FOOTPRINT
footprint_html = """
<div style="text-align:center;max-width:56ch;margin:0 auto">
  <span class="n-k">Our footprint</span>
  <h2 class="n-h2" style="font-size:34px">Printed consciously, posted kindly</h2>
</div>
<div class="n-grid n-grid-3" style="margin-top:44px;gap:30px">
  <div class="nurture-glass n-lift" style="padding:40px"><h3 class="n-h3" style="font-size:24px">Print</h3><p class="n-lead" style="font-size:15.5px;margin-top:12px">FSC-certified recycled stock, soy-based inks free from IPA, acid and chlorine. Better for your family, and for the paddock it came from.</p></div>
  <div class="nurture-glass n-lift" style="padding:40px"><h3 class="n-h3" style="font-size:24px">Post</h3><p class="n-lead" style="font-size:15.5px;margin-top:12px">Every issue ships in a compostable, zero-waste satchel. It looks good in the letterbox and breaks down in your garden bed.</p></div>
  <div class="nurture-glass n-lift" style="padding:40px"><h3 class="n-h3" style="font-size:24px">Planted</h3><p class="n-lead" style="font-size:15.5px;margin-top:12px">One tree for every annual subscription, through One Tree Planted. Small, consistent, and counted.</p></div>
</div>
"""
PARTS.append(one_col_container(footprint_html, hundred_percent="no", padding_top="30px", padding_bottom="20px"))

# 6. BLOG
blog_banner_html = f"""
<div id="read" style="position:relative;top:-90px"></div>
<div style="position:relative;height:520px;background-image:url('{BLOG_IMG}');background-size:cover;background-position:center;display:flex;align-items:flex-end;justify-content:center;padding-bottom:40px;text-align:center">
  <div>
    <span class="n-k">Free to read</span>
    <h2 class="n-h2" style="font-size:34px;color:#3a2d28">The natural parenting blog</h2>
  </div>
</div>
"""
PARTS.append(one_col_container(blog_banner_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

blog_cards_html = f"""
<div class="n-grid n-grid-3" style="gap:34px">
  <article><div style="border-radius:16px;overflow:hidden"><img src="{ARTICLE_IMGS[0]}" alt="" style="width:100%;aspect-ratio:5/4;object-fit:cover;display:block" /></div><span class="n-k" style="margin:20px 0 8px">Sleep</span><h3 class="n-h3" style="font-size:23px">What nobody tells you about the fourth month</h3><p class="n-lead" style="font-size:15px;margin-top:10px">Regression, or a baby learning to sleep like the rest of us.</p></article>
  <article><div style="border-radius:16px;overflow:hidden"><img src="{ARTICLE_IMGS[1]}" alt="" style="width:100%;aspect-ratio:5/4;object-fit:cover;display:block" /></div><span class="n-k" style="margin:20px 0 8px">Feeding</span><h3 class="n-h3" style="font-size:23px">A weaning table, not a weaning battle</h3><p class="n-lead" style="font-size:15px;margin-top:10px">On letting a child decide when they are finished.</p></article>
  <article><div style="border-radius:16px;overflow:hidden"><img src="{ARTICLE_IMGS[2]}" alt="" style="width:100%;aspect-ratio:5/4;object-fit:cover;display:block" /></div><span class="n-k" style="margin:20px 0 8px">Connection</span><h3 class="n-h3" style="font-size:23px">Attachment, minus the guilt</h3><p class="n-lead" style="font-size:15px;margin-top:10px">Secure does not mean constant. What the research asks.</p></article>
</div>
<div style="text-align:center;margin-top:44px"><a href="/blog/" class="n-ghost">All articles</a></div>
"""
PARTS.append(one_col_container(blog_cards_html, hundred_percent="no", padding_top="48px", padding_bottom="20px"))

PARTS.append('[fusion_builder_container hundred_percent="no" padding_top="10px" padding_bottom="10px"][fusion_builder_row][fusion_builder_column type="1_1"][fusion_separator style_type="single solid" top_margin="0" bottom_margin="0" border_size="1" sep_color="rgba(215,203,194,.35)" width="100%" alignment="center" /][/fusion_builder_column][/fusion_builder_row][/fusion_builder_container]')

# 7. MENTORS
mentors = [
    ("Penny Chote", "Breastfeeding", "Preparation while you&#8217;re still pregnant, through the Thompson Method program."),
    ("Andrea Fallon", "Infant sleep", "Midwife and child health nurse, Wholehearted Family Health. No sleep training."),
    ("Crystal Hardstaff", "Perinatal mental health", "Founder of The Gentle Counsellor. Trauma and attachment."),
    ("Stephanie Pinto", "Emotional intelligence", "Parenting coach and childhood behavioural mentor."),
    ("Micarl\u00e9 Callea", "Home education", "The home-educating mind behind Fearless Homeschool."),
    ("Naomi Aldort", "Parent&#8211;child relationship", "Author of <em>Raising Our Children, Raising Ourselves</em>."),
]
mentor_cards = "".join(
    f"""<div class="nurture-glass n-lift" style="padding:30px;display:flex;flex-direction:column;gap:14px">
      <div class="n-avatar n-ph"></div>
      <div><h3 class="n-h3" style="font-size:20px">{name}</h3><span class="n-k" style="margin:6px 0 0">{role}</span></div>
      <p class="n-lead" style="font-size:14px">{blurb}</p>
    </div>""" for name, role, blurb in mentors
)
mentors_html = f"""
<div id="mentors" style="position:relative;top:-90px"></div>
<div style="text-align:center;max-width:54ch;margin:0 auto">
  <span class="n-k">Weekly live Q&amp;As</span>
  <h2 class="n-h2" style="font-size:34px">Ask a practitioner, not a forum</h2>
  <p class="n-lead" style="margin-top:16px;font-weight:300;font-size:18px">Six mentors in the private group, answering under their own names.</p>
</div>
<div class="n-grid n-grid-3" style="margin-top:44px;gap:26px">{mentor_cards}</div>
<div style="text-align:center;margin-top:40px"><a href="https://www.facebook.com/groups/nurtureparentingmagazine/" target="_blank" rel="noopener" class="n-cta">Join the group</a></div>
"""
PARTS.append(one_col_container(mentors_html, hundred_percent="no", padding_top="30px", padding_bottom="20px"))

# 8. GIFT GUIDES
gift_banner_html = f"""
<div style="position:relative;height:460px;background-image:url('{GIFT_IMG}');background-size:cover;background-position:center;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding-bottom:36px;text-align:center">
  <span class="n-k">Three times a year</span>
  <h2 class="n-h2" style="font-size:32px;max-width:24ch;color:#3a2d28">Gift guides, curated not collected</h2>
</div>
"""
PARTS.append(one_col_container(gift_banner_html, hundred_percent="yes", padding_top="30px", padding_bottom="0", **{"class": "nurture-fade"}))

gift_cards_html = """
<div class="n-grid n-grid-3" style="gap:30px">
  <div class="nurture-glass n-lift" style="padding:36px"><h3 class="n-h3" style="font-size:22px">Mama&#8217;s May</h3><p class="n-lead" style="font-size:15px;margin-top:10px">For mothers, all month. Includes the free Self-Love Planner.</p></div>
  <div class="nurture-glass n-lift" style="padding:36px"><h3 class="n-h3" style="font-size:22px">The Baby Shower Edition</h3><p class="n-lead" style="font-size:15px;margin-top:10px">Practical and heartfelt, with the free Baby Gift Registry app.</p></div>
  <div class="nurture-glass n-lift" style="padding:36px"><h3 class="n-h3" style="font-size:22px">The Christmas Guide</h3><p class="n-lead" style="font-size:15px;margin-top:10px">Gifts for the whole family, with the free Memory Makers Planner.</p></div>
</div>
<div style="text-align:center;margin-top:40px"><a href="/showcase/" class="n-ghost">See this year&#8217;s guides</a></div>
"""
PARTS.append(one_col_container(gift_cards_html, hundred_percent="no", padding_top="44px", padding_bottom="20px"))

PARTS.append('[fusion_builder_container hundred_percent="no" padding_top="10px" padding_bottom="10px"][fusion_builder_row][fusion_builder_column type="1_1"][fusion_separator style_type="single solid" top_margin="0" bottom_margin="0" border_size="1" sep_color="rgba(215,203,194,.35)" width="100%" alignment="center" /][/fusion_builder_column][/fusion_builder_row][/fusion_builder_container]')

# 9. BRANDS
brands_left_html = """
<div id="brands" style="position:relative;top:-90px"></div>
<span class="n-k">For brands</span>
<h2 class="n-h2" style="font-size:34px">A page here is a page kept</h2>
<p class="n-lead" style="margin-top:16px;max-width:44ch;font-weight:300;font-size:18px">A magazine parents keep, three digital gift guides a year, and a directory they search on purpose. We take a small number of partners per issue.</p>
<div style="margin-top:26px"><a href="/advertise/" class="n-cta">Request the media kit</a></div>
"""
brand_box = '<div class="nurture-glass" style="aspect-ratio:3/2;display:flex;align-items:center;justify-content:center"><span style="font:400 10px ui-monospace,Menlo,monospace;letter-spacing:.1em;text-transform:uppercase;color:rgba(58,45,40,.4)">brand mark</span></div>'
brands_right_html = f'<div class="n-grid n-grid-3" style="gap:16px">{brand_box * 6}</div>'
PARTS.append(two_col_container(brands_left_html, brands_right_html, "2_5", "3_5", hundred_percent="no", padding_top="30px", padding_bottom="20px"))

PARTS.append('[fusion_builder_container hundred_percent="no" padding_top="10px" padding_bottom="10px"][fusion_builder_row][fusion_builder_column type="1_1"][fusion_separator style_type="single solid" top_margin="0" bottom_margin="0" border_size="1" sep_color="rgba(215,203,194,.35)" width="100%" alignment="center" /][/fusion_builder_column][/fusion_builder_row][/fusion_builder_container]')

# 10. ASK NARA + NEWSLETTER
ask_html = """
<span class="n-k">Ask Nara</span>
<h3 class="n-h3" style="font-size:28px">Fourteen years of Nurture, searchable &mdash; coming soon</h3>
<p class="n-lead" style="font-size:15.5px;margin-top:12px;max-width:40ch">Our AI-powered search across 14 years of back issues. Ask in your own words, get an answer that cites the issue it came from &mdash; launching soon.</p>
"""
letter_html = """
<span class="n-k">The letter</span>
<h3 class="n-h3" style="font-size:28px">The gift guide, before it goes public</h3>
<p class="n-lead" style="font-size:15.5px;margin-top:12px;max-width:40ch">Six emails a year: what&#8217;s in the next issue, and first look at the guides.</p>
<div style="margin-top:20px;max-width:440px">
  <script async data-uid="550bb75106" src="https://the-nurture-parenting-magazine-hive.kit.com/550bb75106/index.js"></script>
</div>
<p style="font-size:12px;color:rgba(58,45,40,.5);margin-top:10px">The Hive &mdash; already-live ConvertKit newsletter list, reused as-is.</p>
"""
PARTS.append(two_col_container(ask_html, f'<div style="border-left:1px solid rgba(215,203,194,.9);padding-left:56px">{letter_html}</div>', "1_2", "1_2", hundred_percent="no", padding_top="30px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/homepage_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
