# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

FOUNDER_IMG = "https://images.unsplash.com/photo-1476703993599-0035a21b17a9?auto=format&fit=crop&w=2400&q=80"
CHILD_PLAY_IMG = "https://images.unsplash.com/photo-1491013516836-7db643ee125a?auto=format&fit=crop&w=2000&q=80"

PARTS = [style_block()]

hero_html = """
<div style="text-align:center;max-width:900px;margin:0 auto;padding:40px 0 0">
  <span class="n-k">Our story</span>
  <h1 class="n-h1" style="font-size:46px;max-width:20ch;margin:0 auto">From conception to connection.</h1>
  <p class="n-lead" style="max-width:52ch;margin:22px auto 0;font-weight:300;font-size:19px;line-height:1.65">The most important bonds start with yourself, then ripple outward &mdash; to your children, your family, and the village around you.</p>
</div>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="60px", padding_bottom="0"))

founder_html = f'<div style="position:relative;height:560px;background-image:url(\'{FOUNDER_IMG}\');background-size:cover;background-position:center;"></div>'
PARTS.append(one_col_container(founder_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

beginnings_html = """
<h2 class="n-h2" style="font-size:34px;margin-bottom:22px">A magazine that didn&#8217;t exist yet</h2>
<div class="n-prose">
<p>Nurture was founded in 2012 by Kristy Pillinger, a new mother who went looking for parenting resources that were both intuitive and evidence-based, and couldn&#8217;t find them. With her firstborn William in her arms, she made the magazine she&#8217;d wanted to read.</p>
<p>It was published quarterly in print and shared digitally across Australia and the world. From 2026, after a break, Nurture returns bi-monthly.</p>
<p class="n-pull">Led by parents, for parents. That hasn&#8217;t changed since the first issue.</p>
<p>What began small has become a trusted voice in Australian parenting &mdash; thought-provoking writers, working practitioners, and real family stories about gentle, respectful, holistic parenting.</p>
</div>
"""
PARTS.append(two_col_container('<span class="n-k">Our beginnings</span>', beginnings_html, "1_5", "4_5", hundred_percent="no", padding_top="70px", padding_bottom="20px"))

PARTS.append(hr())

why_html = """
<h2 class="n-h2" style="font-size:34px;margin-bottom:22px">Attachment, as a starting position</h2>
<div class="n-prose">
<p>Nurture is grounded in attachment parenting and attachment theory &mdash; the secure base that supports babies and parents alike. As Bowlby and Ainsworth established decades ago, attachment is the deep and enduring emotional bond that connects one person to another across time and space (Ainsworth, 1973; Bowlby, 1969).</p>
<p>For generations, parenting was shaped by habit rather than research. We now know that how we parent in the early years shapes a child&#8217;s brain and nervous system &mdash; their capacity for resilience, for self-regulation, and for close relationships throughout their life.</p>
<p>We carry our own childhood patterns into adulthood. The attachments and the difficulties we have with our parents, our partners, our children and our friends trace back to the blueprints formed in those first critical years. What parents do in that window matters.</p>
<p>Which is the point of the magazine: with awareness, support and practical tools, you can parent with presence rather than by default.</p>
</div>
"""
PARTS.append(two_col_container('<span class="n-k">Our why</span>', why_html, "1_5", "4_5", hundred_percent="no", padding_top="20px", padding_bottom="20px"))

philosophy_banner = f"""
<div style="position:relative;height:460px;background-image:url('{CHILD_PLAY_IMG}');background-size:cover;background-position:center;display:flex;flex-direction:column;align-items:center;justify-content:flex-end;padding-bottom:34px;text-align:center">
  <span class="n-k">Our philosophy</span>
  <h2 class="n-h2" style="font-size:32px;max-width:26ch;color:#3a2d28">Nourish yourself first, then everyone else</h2>
</div>
"""
PARTS.append(one_col_container(philosophy_banner, hundred_percent="yes", padding_top="30px", padding_bottom="0", **{"class": "nurture-fade"}))

philosophy_text = """
<p class="n-lead" style="max-width:62ch;margin:0 auto;text-align:center;font-size:18px;font-weight:300">Nurture gives parents insight into the many styles of natural parenting that exist today, so you can take an intuitive approach built around your own family rather than someone else&#8217;s rulebook.</p>
"""
PARTS.append(one_col_container(philosophy_text, hundred_percent="no", padding_top="44px", padding_bottom="20px"))

PARTS.append(hr())

domains = [
    ("Emotional", "Raising emotionally secure children starts with understanding what they need. Less screen time, more time together &mdash; and writers who work with families for a living."),
    ("Intellectual", "Child-led learning that values curiosity and creativity as much as academics. Whether you homeschool, unschool, or simply follow your child&#8217;s rhythm."),
    ("Physical", "Conscious pregnancy, gentle birth, breastfeeding and safe co-sleeping &mdash; low-tox, evidence-backed practice from our contributors. We do not publish sleep training."),
    ("Spiritual", "The inner world: helping children value themselves, other people and the place they live. Kindness, empathy, mindfulness, and noticing small things."),
]
domain_cards = "".join(
    f'<div class="nurture-glass n-lift" style="padding:40px"><h3 class="n-h3" style="font-size:22px">{t}</h3><p class="n-lead" style="font-size:15.5px;margin-top:12px">{d}</p></div>'
    for t, d in domains
)
topics_html = f"""
<div style="text-align:center;max-width:54ch;margin:0 auto">
  <span class="n-k">What we cover</span>
  <h2 class="n-h2" style="font-size:34px">Four domains, every issue</h2>
</div>
<div class="n-grid n-grid-2" style="margin-top:44px;gap:24px">{domain_cards}</div>
"""
PARTS.append(one_col_container(topics_html, hundred_percent="no", padding_top="20px", padding_bottom="20px"))

pillars_html = """
<div class="nurture-glass" style="padding:56px;text-align:center">
  <span class="n-k">Three pillars</span>
  <h2 class="n-h2" style="font-size:32px">Birth &middot; Balance &middot; Belong</h2>
  <div class="n-grid n-grid-3" style="margin-top:32px;text-align:left;gap:30px">
    <div><h3 class="n-h3" style="font-size:20px">Birth</h3><p class="n-lead" style="font-size:14.5px;margin-top:8px">Conception, labour and the postpartum months, treated as one continuous event rather than three.</p></div>
    <div><h3 class="n-h3" style="font-size:20px">Balance</h3><p class="n-lead" style="font-size:14.5px;margin-top:8px">Room for both the chaos and the calm, without pretending the chaos is a failure.</p></div>
    <div><h3 class="n-h3" style="font-size:20px">Belong</h3><p class="n-lead" style="font-size:14.5px;margin-top:8px">Emotional safety and secure attachment, built in an ordinary house on an ordinary Tuesday.</p></div>
  </div>
  <div style="display:flex;gap:14px;justify-content:center;margin-top:36px;flex-wrap:wrap">
    <a href="/subscribe/" class="n-cta">Subscribe from $20</a>
    <a href="/advertise/" class="n-ghost">Partner with us</a>
  </div>
</div>
"""
PARTS.append(one_col_container(pillars_html, hundred_percent="no", padding_top="10px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/our_story_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
