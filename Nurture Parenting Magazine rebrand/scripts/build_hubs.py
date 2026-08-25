# -*- coding: utf-8 -*-
"""Builds the shared Showcase/category-hub template for all 7 pages:
Showcase (index) + Changemakers, Self Love, Love of Learning, Australian Made,
The Essentials, Tested on Humans."""
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

HUBS = [
    {"key": "showcase", "label": "Showcase", "page_id": 2110, "slug": "showcase"},
    {"key": "changemakers", "label": "Changemakers", "page_id": 2040, "slug": "changemakers"},
    {"key": "self-love", "label": "Self Love", "page_id": 2129, "slug": "self-love"},
    {"key": "love-of-learning", "label": "Love of Learning", "page_id": 2095, "slug": "love-of-learning"},
    {"key": "australian-made", "label": "Australian Made", "page_id": 2067, "slug": "australian-made"},
    {"key": "the-essentials", "label": "The Essentials", "page_id": 2080, "slug": "mama-bubba-essentials"},
    {"key": "tested-on-humans", "label": "Tested on Humans", "page_id": None, "slug": "tested-on-humans"},
]

BANNER_IMG = "https://images.unsplash.com/photo-1512428559087-560fa5ceab42?auto=format&fit=crop&w=2400&q=80"
LEAD_IMG = "https://images.unsplash.com/photo-1544367567-0f2fcb009e0b?auto=format&fit=crop&w=1600&q=80"

DATA = {
    "showcase": {
        "kicker": "Showcase &middot; conscious brands, met in person",
        "h1": "Things worth keeping, made by people we know.",
        "lead": "Australian makers and practitioners we have actually met. Listed because they earned it, never because they bought the slot.",
        "featured_label": "Featured maker",
        "featured_title": "The nappy company that started in a laundry",
        "featured_body": "Two mothers, a sewing machine and a refusal to accept landfill as the only option. Now stocked in four hundred stores, still stitching the first sample by hand.",
        "featured_meta": "Maker profile &middot; 12 min read",
        "cards": [
            ("Sleep", "Organic cot linen, Byron Bay", "GOTS-certified cotton, dyed with plants, made in runs of two hundred.", None),
            ("Feeding", "Glass, not plastic, since 2014", "Bottles and storage that outlast the child they were bought for.", None),
            ("Skin", "Six ingredients, all of them readable", "Balm for nappy rash and cracked nipples, from a compounding pharmacist in Bendigo.", None),
            ("Play", "Timber toys from salvaged hardwood", "Offcuts from demolition yards, finished in beeswax, built to be handed down.", None),
            ("Wear", "A carrier fitted by a physiotherapist", "Hip-healthy design, adjustable across four years of growing.", None),
            ("Home", "Compostable everything", "Satchels, wraps and bin liners that break down in a suburban garden bed.", None),
        ],
        "cta_label": "For brands",
        "cta_title": "Want to be in the Showcase?",
        "cta_lead": "We take a small number of partners per issue, and we meet everyone first.",
        "cta_primary": ("Request the media kit", "/advertise/"),
        "cta_secondary": ("See advertising rates", "/advertise/"),
    },
    "changemakers": {
        "kicker": "Changemakers &middot; the people shifting it",
        "h1": "The ones doing the work, not the talking.",
        "lead": "Founders, midwives, educators and advocates changing how Australia raises children. Long interviews, printed in full.",
        "featured_label": "Cover interview",
        "featured_title": "The midwife rewriting the first hour",
        "featured_body": "Thirty years catching babies in regional Queensland, and a campaign to change what happens in the sixty minutes after a birth. On continuity of care, and why the system keeps losing it.",
        "featured_meta": "Interview &middot; 22 min read",
        "cards": [
            ("Advocacy", "The paid parental leave campaign nobody funded", "How three mothers with a spreadsheet moved a policy that lobbyists could not.", None),
            ("Founders", "A milk bank in a country town", "Donor milk, volunteer drivers, and a cold chain held together by goodwill.", None),
            ("Education", "The kindergarten that stopped teaching letters", "Four years of play-based early years, and what the data says now.", None),
            ("Health", "Bringing birth back to the community", "Birth centres, known midwives, and the towns that fought to keep them.", None),
            ("Environment", "The nappy problem, solved locally", "A composting service that took one council from landfill to soil in eighteen months.", None),
            ("Research", "What we still do not measure", "Perinatal mental health data, and the gaps that shape every policy built on it.", None),
        ],
        "cta_label": "Nominate",
        "cta_title": "Know someone who should be in here?",
        "cta_lead": "We interview six changemakers a year. Tell us who, and why now.",
        "cta_primary": ("Nominate a changemaker", "/contact/"),
        "cta_secondary": ("Read the current issue", "/shop/"),
    },
    "self-love": {
        "kicker": "Self Love &middot; for the parent, not the child",
        "h1": "You are also someone who needs looking after.",
        "lead": "Matrescence, rest, identity and the slow return to yourself. Written by practitioners who work with parents, not at them.",
        "featured_label": "This month",
        "featured_title": "The year nobody photographs",
        "featured_body": "Matrescence is a developmental stage, as real as adolescence, and almost entirely unsupported. What it does to identity, and the four things that genuinely help.",
        "featured_meta": "Crystal Hardstaff &middot; 14 min read",
        "cards": [
            ("Rest", "Sleep is not a reward for finishing", "Why the tidy house can wait, and what deprivation actually costs a parent.", None),
            ("Identity", "The name you had before", "On becoming someone&#8217;s mother without disappearing into it.", None),
            ("Body", "Postpartum, without the timeline", "Recovery has no deadline. What the six-week check does and does not cover.", None),
            ("Relationships", "The invisible ledger", "Mental load, and a conversation to have before resentment does it for you.", None),
            ("Boundaries", "Saying no to the people who love you", "Visitors, advice and the first three months. A script you can borrow.", None),
            ("Practice", "Ten minutes is not nothing", "Small returns to yourself that survive a day with a toddler in it.", None),
        ],
        "cta_label": "Free download",
        "cta_title": "The Self-Love Planner",
        "cta_lead": "Twelve weeks of small returns to yourself. Free with any subscription, or $12 on its own.",
        "cta_primary": ("Get the planner", "/shop/"),
        "cta_secondary": ("Subscribe from $20", "/subscribe/"),
    },
    "love-of-learning": {
        "kicker": "Love of Learning &middot; birth to the early years",
        "h1": "Childhood is not a race to be won early.",
        "lead": "Play-based early years, home education, and the case for doing considerably less before five. Evidence, not ideology.",
        "featured_label": "Cover feature",
        "featured_title": "Before the alphabet, the afternoon",
        "featured_body": "Every year the pressure to start formal learning moves earlier, and every year the research says the opposite. What unhurried actually looks like on a Tuesday, in a real house, with real siblings.",
        "featured_meta": "Micarl\u00e9 Callea &middot; 16 min read",
        "cards": [
            ("Play", "Boredom is a curriculum", "What a child builds in the twenty minutes after they say there is nothing to do.", None),
            ("Home education", "Starting without a plan", "The first six months of home ed, and the four things worth buying.", None),
            ("Literacy", "Reading, when they are ready", "The spread of normal is wider than school allows. Where the line actually is.", None),
            ("Nature", "The paddock as a classroom", "Risk, weather and unsupervised distance &mdash; and why they matter developmentally.", None),
            ("Screens", "A household rule you can keep", "Not zero, not endless. How families who are relaxed about it actually do it.", None),
            ("Transitions", "Starting school later", "What holding a child back a year does, and does not, change by year six.", None),
        ],
        "cta_label": "In print",
        "cta_title": "Issue 40 &mdash; Love of Learning",
        "cta_lead": "Eighty pages on unhurried childhoods, home education and play. Still in stock.",
        "cta_primary": ("Buy issue 40", "/shop/"),
        "cta_secondary": ("See all back issues", "/shop/"),
    },
    "australian-made": {
        "kicker": "Showcase package &middot; buy local",
        "h1": "Made here, by people with a name and a postcode.",
        "lead": "Every brand in this section manufactures in Australia. We ask for the address, and we check it.",
        "featured_label": "Featured advertiser",
        "featured_title": "Timber toys from salvaged hardwood",
        "featured_body": "Offcuts rescued from demolition yards in Ballarat, finished in beeswax, built heavy enough to be handed down twice. Two people, one workshop, four hundred pieces a year.",
        "featured_meta": "Advertorial feature &middot; Ballarat, VIC",
        "cards": [
            ("Bedding", "Organic cot linen, Byron Bay", "GOTS cotton, plant-dyed, cut and sewn in runs of two hundred.", "$120"),
            ("Feeding", "Glass bottles, Adelaide", "Borosilicate and silicone. No plastic, no BPA conversation to have.", "$34"),
            ("Skin", "Six-ingredient balm, Bendigo", "Compounded by a pharmacist for nappy rash and cracked nipples alike.", "$26"),
            ("Wear", "Carriers fitted by a physio, Perth", "Hip-healthy geometry, adjustable across four years of growing.", "$189"),
            ("Home", "Compostable everything, Brisbane", "Satchels, wraps and liners that break down in a suburban garden bed.", "$18"),
            ("Play", "Wool felt play sets, Hobart", "Australian merino, needle-felted, no two exactly the same.", "$72"),
        ],
        "cta_label": "For brands",
        "cta_title": "Manufacture in Australia?",
        "cta_lead": "The Buy Local package runs in print and here, with a QR code on the spread.",
        "cta_primary": ("Request the media kit", "/advertise/"),
        "cta_secondary": ("See all packages", "/showcase/"),
    },
    "the-essentials": {
        "kicker": "Showcase package &middot; mama &amp; bubba",
        "h1": "The short list. Everything else can wait.",
        "lead": "What a new parent genuinely needs in the first year, and nothing that only exists to be bought.",
        "featured_label": "Featured advertiser",
        "featured_title": "The nappy company that started in a laundry",
        "featured_body": "Two mothers, a sewing machine and a refusal to accept landfill as the only option. Now stocked in four hundred stores, still stitching the first sample of every new run by hand.",
        "featured_meta": "Advertorial feature &middot; Gold Coast, QLD",
        "cards": [
            ("Sleep", "One good sleeping bag", "TOG-rated, organic, sized to last two winters rather than one.", "$89"),
            ("Feeding", "A pump you can actually carry", "Quiet, rechargeable, and it fits in the nappy bag you already own.", "$240"),
            ("Out", "The sling, before the pram", "Ring sling in linen. The first three months are easier worn.", "$130"),
            ("Bath", "Hooded towel, adult size", "Bought once at birth, still in the linen cupboard at school age.", "$54"),
            ("Change", "A mat that folds into itself", "Wipeable, packable, and the one thing you will use every single day.", "$39"),
            ("Health", "The kit worth having ready", "Thermometer, saline, nail file. Assembled before you need it at 2am.", "$45"),
        ],
        "cta_label": "For brands",
        "cta_title": "An essential, not an extra?",
        "cta_lead": "The Essentials package is the most scanned spread in the magazine.",
        "cta_primary": ("Request the media kit", "/advertise/"),
        "cta_secondary": ("See all packages", "/showcase/"),
    },
    "tested-on-humans": {
        "kicker": "Showcase package &middot; team picks",
        "h1": "We used it. For months. With our own children.",
        "lead": "Small businesses and start-ups, tested by the Nurture team and our contributors before a word is written. Included at no charge in the Big Brand Equity package.",
        "featured_label": "This issue&#8217;s pick",
        "featured_title": "Six months with a $19 silicone bib",
        "featured_body": "It survived a dishwasher every night, two toddlers and one dog. Nothing about it is clever, which is exactly why it is still in the drawer. What we tested, and the two we quietly stopped using.",
        "featured_meta": "Team test &middot; six months",
        "cards": [
            ("Tested 6 months", "The bottle brush that outlasted the bottles", "Replaceable head, timber handle, no mould in the join.", "$16"),
            ("Tested 4 months", "A carrier for the second child", "Worn on school runs in a Queensland summer and still comfortable.", "$165"),
            ("Tested 8 months", "Nappy cream that actually cleared it", "Two ingredients. Worked in a day when three others did not.", "$22"),
            ("Tested 5 months", "The high chair we stopped resenting", "Wipes clean in one pass. That is the entire review.", "$249"),
            ("Tested 3 months", "Sleep suit, size up", "Ran small. Sized up it became the thing we recommend most.", "$68"),
            ("Tested 7 months", "A pram that folds one-handed, honestly", "Tested in three car parks with a baby on one hip. It does.", "$680"),
        ],
        "cta_label": "Small business",
        "cta_title": "Start-up, or a small run?",
        "cta_lead": "Team Picks is included at no charge in the Big Brand Equity package. Send us the product, not a press release.",
        "cta_primary": ("Submit a product", "/advertise/"),
        "cta_secondary": ("See all packages", "/showcase/"),
    },
}


def sub_nav(current_key):
    items = [
        ("Changemakers", "/changemakers/", "changemakers"),
        ("Self Love", "/self-love/", "self-love"),
        ("Love of Learning", "/love-of-learning/", "love-of-learning"),
        ("Australian Made", "/australian-made/", "australian-made"),
        ("The Essentials", "/mama-bubba-essentials/", "the-essentials"),
        ("Tested on Humans", "/tested-on-humans/", "tested-on-humans"),
    ]
    if current_key == "showcase":
        items = [("Showcase", "/showcase/", "showcase")] + items
    else:
        items = [("Showcase", "/showcase/", "showcase")] + items
    links = "".join(
        f'<a href="{href}" style="color:{"#8c6f61" if key == current_key else "rgba(58,45,40,.62)"};'
        f'{"border-bottom:1px solid #cbb1a5;padding-bottom:4px;" if key == current_key else ""}'
        f'font:500 11.5px/1 \'Inter\',sans-serif;letter-spacing:.14em;text-transform:uppercase;white-space:nowrap;margin-right:28px">{label}</a>'
        for label, href, key in items
    )
    wrap = (
        f'<div style="border-top:1px solid rgba(215,203,194,.35);border-bottom:1px solid rgba(215,203,194,.35);padding:14px 0;overflow-x:auto;white-space:nowrap">{links}</div>'
    )
    return one_col_container(wrap, hundred_percent="no", padding_top="0", padding_bottom="0")


def build_hub(key):
    d = DATA[key]
    parts = [style_block(), sub_nav(key)]

    hero_html = f"""
    <div style="text-align:center;max-width:900px;margin:0 auto;padding:34px 0 0">
      <span class="n-k">{d['kicker']}</span>
      <h1 class="n-h1" style="font-size:42px;max-width:19ch;margin:0 auto">{d['h1']}</h1>
      <p class="n-lead" style="max-width:56ch;margin:20px auto 0;font-weight:300;font-size:18px">{d['lead']}</p>
    </div>
    """
    parts.append(one_col_container(hero_html, hundred_percent="no", padding_top="50px", padding_bottom="0"))

    banner_html = f'<div style="position:relative;height:440px;background-image:url(\'{BANNER_IMG}\');background-size:cover;background-position:center;"></div>'
    parts.append(one_col_container(banner_html, hundred_percent="yes", padding_top="0", padding_bottom="0", **{"class": "nurture-fade"}))

    featured_html = f"""
    <a href="/contact/" class="nurture-glass n-lift" style="display:grid;grid-template-columns:1.15fr 1fr;gap:0;overflow:hidden;text-decoration:none">
      <div style="min-height:400px;background-image:url('{LEAD_IMG}');background-size:cover;background-position:center"></div>
      <div style="padding:48px 44px;display:flex;flex-direction:column;justify-content:center">
        <span class="n-k" style="margin-bottom:12px">{d['featured_label']}</span>
        <h2 class="n-h2" style="font-size:28px;max-width:18ch">{d['featured_title']}</h2>
        <p style="font-size:15.5px;line-height:1.72;color:rgba(58,45,40,.62);margin:16px 0 20px;max-width:44ch">{d['featured_body']}</p>
        <p style="font:400 12.5px/1 'Inter',sans-serif;letter-spacing:.1em;text-transform:uppercase;color:rgba(58,45,40,.6);margin:0">{d['featured_meta']}</p>
      </div>
    </a>
    """
    parts.append(one_col_container(featured_html, hundred_percent="no", padding_top="24px", padding_bottom="0"))

    cards_html_parts = []
    for label, title, body, price in d["cards"]:
        price_html = f'<p style="font-family:\'Playfair Display\',Georgia,serif;font-size:20px;margin:8px 0 0;color:#3a2d28">{price}</p>' if price else ""
        cards_html_parts.append(
            f'<a href="/contact/" style="display:block;text-decoration:none">'
            f'<div class="n-ph" style="aspect-ratio:5/4;border-radius:16px"></div>'
            f'<span class="n-k" style="margin:18px 0 8px">{label}</span>'
            f'<h3 class="n-h3" style="font-size:20px;max-width:20ch">{title}</h3>'
            f'<p style="font-size:14.5px;line-height:1.65;color:rgba(58,45,40,.6);margin:8px 0 0">{body}</p>'
            f'{price_html}</a>'
        )
    cards_wrap = f'<div class="n-grid n-grid-3" style="gap:36px 28px;margin-top:0">{"".join(cards_html_parts)}</div>'
    more_link = '<div style="text-align:center;margin-top:44px"><a href="/blog/" class="n-ghost">More from this hub</a></div>'
    parts.append(one_col_container(cards_wrap + more_link, hundred_percent="no", padding_top="40px", padding_bottom="20px"))

    parts.append(hr())

    cta_html = f"""
    <div class="nurture-glass" style="padding:54px;text-align:center">
      <span class="n-k">{d['cta_label']}</span>
      <h2 class="n-h2" style="font-size:30px;max-width:22ch;margin:0 auto">{d['cta_title']}</h2>
      <p class="n-lead" style="max-width:48ch;margin:16px auto 0;font-weight:300;font-size:17px">{d['cta_lead']}</p>
      <div style="display:flex;gap:14px;justify-content:center;margin-top:28px;flex-wrap:wrap">
        <a href="{d['cta_primary'][1]}" class="n-cta">{d['cta_primary'][0]}</a>
        <a href="{d['cta_secondary'][1]}" class="n-ghost">{d['cta_secondary'][0]}</a>
      </div>
    </div>
    """
    parts.append(one_col_container(cta_html, hundred_percent="no", padding_top="10px", padding_bottom="20px"))

    parts.append(hr())

    keep_shopping = [
        ("Changemakers", "Back stories", "/changemakers/"),
        ("Self Love", "Only organic", "/self-love/"),
        ("Love of Learning", "Education", "/love-of-learning/"),
        ("Australian Made", "Buy local", "/australian-made/"),
        ("The Essentials", "Mama &amp; bubba", "/mama-bubba-essentials/"),
        ("Tested on Humans", "Team picks", "/tested-on-humans/"),
        ("Showcase", "All packages", "/showcase/"),
    ]
    keep_shopping = [item for item in keep_shopping if item[2].strip("/") != key]
    ks_cards = "".join(
        f'<a href="{href}" class="nurture-glass n-lift" style="padding:24px 22px;display:block;text-decoration:none">'
        f'<h3 class="n-h3" style="font-size:18px">{title}</h3>'
        f'<p style="font:500 10.5px/1.4 \'Inter\',sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#a98a7b;margin:8px 0 0">{sub}</p></a>'
        for title, sub, href in keep_shopping
    )
    keep_html = f"""
    <div style="text-align:center;max-width:52ch;margin:0 auto 40px">
      <span class="n-k">Keep shopping</span>
      <h2 class="n-h2" style="font-size:30px">Every other category, one tap away</h2>
    </div>
    <div class="n-grid n-grid-3" style="gap:16px">{ks_cards}</div>
    """
    parts.append(one_col_container(keep_html, hundred_percent="no", padding_top="20px", padding_bottom="70px"))

    return "".join(parts)


if __name__ == "__main__":
    for hub in HUBS:
        content = build_hub(hub["key"])
        path = f"/tmp/hub_{hub['key']}_content.txt"
        with open(path, "w") as f:
            f.write(content)
        print(hub["key"], "->", path, len(content), "chars, page_id", hub["page_id"])
