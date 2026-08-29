# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

KITCHEN_IMG = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=2400&q=80"

PARTS = [style_block()]

hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:40px 0 0">
  <span class="n-k">Contributors &middot; practitioners, not personalities</span>
  <h1 class="n-h1" style="font-size:46px;max-width:18ch;margin:0 auto">The people who write for Nurture</h1>
  <p class="n-lead" style="max-width:54ch;margin:22px auto 0;font-weight:300;font-size:19px;line-height:1.65">Midwives, counsellors, educators and parents. Everyone here answers under their own name, and everything they publish is sourced.</p>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

banner_html = f'<div style="position:relative;height:440px;background-image:url(\'{KITCHEN_IMG}\');background-size:cover;background-position:center;"></div>'
PARTS.append(one_col_container(banner_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

contributors = [
    ("Penny Chote", "Breastfeeding", "Lactation educator behind the Thompson Method program. Writes on preparing to feed while you&#8217;re still pregnant, and on what to do when the first week doesn&#8217;t go to plan."),
    ("Andrea Fallon", "Infant sleep &amp; birth", "Midwife and child health nurse, founder of Wholehearted Family Health. Covers rest, cycles and the fourth trimester. No sleep training, ever."),
    ("Crystal Hardstaff", "Perinatal mental health", "Founder of The Gentle Counsellor. Trauma, attachment and matrescence &mdash; the year of becoming a mother that nobody photographs."),
    ("Stephanie Pinto", "Emotional intelligence", "Parenting coach and childhood behavioural mentor. Writes about big feelings in small bodies, and about staying regulated when your child isn&#8217;t."),
    ("Micarl\u00e9 Callea", "Home education", "The home-educating mind behind Fearless Homeschool. Play-based early years, unschooling, and the case for doing considerably less before five."),
    ("Naomi Aldort", "Parent&#8211;child relationship", "Author of <em>Raising Our Children, Raising Ourselves</em>. Forty years on what attachment asks of a parent, and what it does not."),
]
cards = "".join(
    f'<div class="nurture-glass n-lift" style="padding:38px 34px">'
    f'<div class="n-avatar n-ph" style="width:82px;height:82px;margin-bottom:20px"></div>'
    f'<h3 class="n-h3" style="font-size:23px">{name}</h3>'
    f'<span class="n-k" style="margin:8px 0 12px">{role}</span>'
    f'<p style="font-size:15px;line-height:1.75;color:rgba(58,45,40,.62);margin:0">{bio}</p></div>'
    for name, role, bio in contributors
)
grid_html = f'<div class="n-grid n-grid-3" style="gap:28px">{cards}</div>'
PARTS.append(one_col_container(grid_html, hundred_percent="no", padding_top="30px", padding_bottom="20px"))

PARTS.append(hr())

standards = [
    ("01", "Cite it or cut it", "Every claim about a child&#8217;s health carries a source. If the evidence is thin, we say so in the piece rather than around it."),
    ("02", "Declare the interest", "If a contributor sells a product or program in their field, it&#8217;s named at the top of the article, not buried at the bottom."),
    ("03", "No advertorial dressed as advice", "Paid placements are labelled as such. A brand cannot buy an editorial page here, at any price."),
    ("04", "Write to a parent, not at one", "WHO and TGA compliant, and free of the shame that so much parenting writing runs on."),
]
standard_rows = "".join(
    f'<div style="display:grid;grid-template-columns:auto 1fr;gap:22px;padding:22px 0;border-bottom:1px solid rgba(215,203,194,.35)">'
    f'<span style="font-family:\'Playfair Display\',Georgia,serif;font-size:20px;color:#a98a7b">{num}</span>'
    f'<span><strong style="font-weight:600;display:block;margin-bottom:6px;font-size:16px;color:#3a2d28">{title}</strong>'
    f'<span style="font-size:15px;line-height:1.75;color:rgba(58,45,40,.62)">{body}</span></span></div>'
    for num, title, body in standards
)
standards_html_right = f'<div style="display:grid">{standard_rows}</div>'
standards_left = '<span class="n-k">The standard</span><h2 class="n-h2" style="font-size:32px;max-width:13ch">What we ask of every contributor</h2>'
PARTS.append(two_col_container(standards_left, standards_html_right, "2_5", "3_5", hundred_percent="no", padding_top="20px", padding_bottom="20px"))

write_html = """
<div class="nurture-glass" style="padding:60px;text-align:center;position:relative">
  <span class="n-k">Write for us</span>
  <h2 class="n-h2" style="font-size:32px;max-width:22ch;margin:0 auto">We commission two issues ahead</h2>
  <p class="n-lead" style="max-width:48ch;margin:18px auto 0;font-weight:300;font-size:18px">One paragraph on the idea, one on why you&#8217;re the person to write it. That&#8217;s the whole pitch.</p>
  <div style="display:flex;gap:14px;justify-content:center;margin-top:30px;flex-wrap:wrap">
    <a href="/contact/" class="n-cta">Pitch a story</a>
    <a href="/blog/" class="n-ghost">Read what we publish</a>
  </div>
</div>
"""
PARTS.append(one_col_container(write_html, hundred_percent="no", padding_top="10px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/contributors_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
