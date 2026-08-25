# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, "/tmp")
from nurture_common import style_block, one_col_container, two_col_container, hr

PARTS = [style_block()]

hero_html = """
<span class="n-k">Contact</span>
<h1 class="n-h1" style="font-size:44px;max-width:16ch">A real person reads every message.</h1>
<p class="n-lead" style="max-width:50ch;margin:22px 0 0;font-weight:300;font-size:18px">We&#8217;re a small team on the Gold Coast. Expect a reply within two business days &mdash; sooner if it&#8217;s about an order.</p>
"""
PARTS.append(one_col_container(hero_html, hundred_percent="no", padding_top="64px", padding_bottom="0"))

form_html = """
<div class="nurture-glass" style="padding:44px 40px">
  <span class="n-k">Send a message</span>
  <form action="mailto:hello@nurtureparentingmagazine.com.au" method="post" enctype="text/plain" style="display:grid;gap:18px;margin-top:6px">
    <div class="n-grid n-grid-2" style="gap:14px">
      <div><label style="display:block;font:500 11px/1 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(58,45,40,.6);margin-bottom:8px">First name</label><input type="text" name="first_name" placeholder="Yasmin" class="n-input" style="width:100%;box-sizing:border-box" /></div>
      <div><label style="display:block;font:500 11px/1 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(58,45,40,.6);margin-bottom:8px">Last name</label><input type="text" name="last_name" placeholder="Smith" class="n-input" style="width:100%;box-sizing:border-box" /></div>
    </div>
    <div><label style="display:block;font:500 11px/1 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(58,45,40,.6);margin-bottom:8px">Email</label><input type="email" name="email" placeholder="you@example.com" class="n-input" style="width:100%;box-sizing:border-box" required /></div>
    <div><label style="display:block;font:500 11px/1 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(58,45,40,.6);margin-bottom:8px">What&#8217;s it about?</label>
      <select name="topic" class="n-input" style="width:100%;box-sizing:border-box">
        <option>Choose one</option><option>My subscription or order</option><option>Advertising and partnerships</option><option>Pitching a story</option><option>Directory listing</option><option>Something else</option>
      </select>
    </div>
    <div><label style="display:block;font:500 11px/1 'Inter',sans-serif;letter-spacing:.14em;text-transform:uppercase;color:rgba(58,45,40,.6);margin-bottom:8px">Message</label><textarea name="message" rows="6" placeholder="Tell us what you need." class="n-input" style="width:100%;box-sizing:border-box;resize:vertical"></textarea></div>
    <div style="display:flex;align-items:center;gap:16px;flex-wrap:wrap">
      <button type="submit" class="n-cta" style="border:0">Send message</button>
      <span style="font-size:13.5px;color:rgba(58,45,40,.6)">We never share your details.</span>
    </div>
  </form>
</div>
"""

contact_channels_html = """
<div style="padding:0 0 24px;border-bottom:1px solid rgba(215,203,194,.35)">
  <span class="n-k">Subscriptions &amp; orders</span>
  <p style="font-size:17px;line-height:1.7;margin:0"><a href="mailto:hello@nurtureparentingmagazine.com.au" style="color:#8c6f61">hello@nurtureparentingmagazine.com.au</a></p>
  <p style="font-size:14px;color:rgba(58,45,40,.6);margin:8px 0 0">Missing issue, change of address, or a gift you need to arrive by a date.</p>
</div>
<div style="padding:24px 0;border-bottom:1px solid rgba(215,203,194,.35)">
  <span class="n-k">Advertising</span>
  <p style="font-size:17px;line-height:1.7;margin:0"><a href="mailto:advertise@nurtureparentingmagazine.com.au" style="color:#8c6f61">advertise@nurtureparentingmagazine.com.au</a></p>
  <p style="font-size:14px;color:rgba(58,45,40,.6);margin:8px 0 0">Media kit, rates and the gift guide deadlines. <a href="/advertise/" style="color:#8c6f61">See the advertise page &rarr;</a></p>
</div>
<div style="padding:24px 0;border-bottom:1px solid rgba(215,203,194,.35)">
  <span class="n-k">Pitches &amp; contributions</span>
  <p style="font-size:17px;line-height:1.7;margin:0"><a href="mailto:editor@nurtureparentingmagazine.com.au" style="color:#8c6f61">editor@nurtureparentingmagazine.com.au</a></p>
  <p style="font-size:14px;color:rgba(58,45,40,.6);margin:8px 0 0">One paragraph on the idea, one on why you. We commission two issues ahead.</p>
</div>
<div style="padding:24px 0">
  <span class="n-k">By post</span>
  <p style="font-size:17px;line-height:1.8;margin:0">Nurture Parenting Magazine<br>PO Box 2292<br>Burleigh Post Shop QLD 4220<br>Australia</p>
  <p style="font-size:13px;color:rgba(58,45,40,.6);margin:14px 0 0">ABN 15 617 938 013</p>
</div>
"""
PARTS.append(two_col_container(form_html, contact_channels_html, "3_5", "2_5", hundred_percent="no", padding_top="50px", padding_bottom="20px"))

PARTS.append(hr())

cards = [
    ("Subscriptions", "Delivery times, renewals, international shipping and gift orders.", "Read the FAQ &rarr;", "/subscribe/"),
    ("Advertising", "Readership, rates, artwork specs and gift guide closing dates.", "Media kit &rarr;", "/advertise/"),
    ("Who we are", "Fourteen years, the editorial standard, and who writes for us.", "Our story &rarr;", "/our-story/"),
]
card_html = "".join(
    f'<a href="{link}" class="nurture-glass n-lift" style="padding:36px 32px;display:block;text-decoration:none">'
    f'<h3 class="n-h3" style="font-size:21px">{t}</h3>'
    f'<p style="font-size:15px;line-height:1.75;color:rgba(58,45,40,.6);margin:10px 0 18px">{d}</p>'
    f'<span style="font:500 12px/1 \'Inter\',sans-serif;letter-spacing:.12em;text-transform:uppercase;color:#8c6f61">{cta}</span></a>'
    for t, d, cta, link in cards
)
faq_html = f"""
<div style="text-align:center;max-width:54ch;margin:0 auto 48px">
  <span class="n-k">Faster than an email</span>
  <h2 class="n-h2" style="font-size:32px">Most questions are already answered</h2>
</div>
<div class="n-grid n-grid-3" style="gap:26px">{card_html}</div>
"""
PARTS.append(one_col_container(faq_html, hundred_percent="no", padding_top="20px", padding_bottom="70px"))

FULL_CONTENT = "".join(PARTS)

if __name__ == "__main__":
    with open("/tmp/contact_content.txt", "w") as f:
        f.write(FULL_CONTENT)
    print("Length:", len(FULL_CONTENT))
