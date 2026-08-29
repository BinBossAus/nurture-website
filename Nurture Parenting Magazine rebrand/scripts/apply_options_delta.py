import json
import copy

with open('/tmp/fresh_backup.json') as f:
    d = json.load(f)

orig = copy.deepcopy(d)
changes = []

def note(key, before, after):
    changes.append((key, before, after))

# 1. Headings preset + H1 typography: 68px -> 46px
before = d['typography_sets']['typography1']['font-size']
d['typography_sets']['typography1']['font-size'] = '46px'
note('typography_sets.typography1.font-size', before, '46px')

before = d['h1_typography']['font-size']
d['h1_typography']['font-size'] = '46px'
note('h1_typography.font-size', before, '46px')

# 2. Link colours
before = d['link_color']
d['link_color'] = '#8C6F61'
note('link_color', before, '#8C6F61')

before = d['link_hover_color']
d['link_hover_color'] = '#3A2D28'
note('link_hover_color', before, '#3A2D28')

# 3. H5 typography
before = d['h5_typography']['font-weight']
d['h5_typography']['font-weight'] = '600'
note('h5_typography.font-weight', before, '600')

before = d['h5_typography']['color']
d['h5_typography']['color'] = 'var(--awb-color2)'
note('h5_typography.color', before, 'var(--awb-color2)')

# 4. Button border colour
before = d['button_border_color']
d['button_border_color'] = 'transparent'
note('button_border_color', before, 'transparent')

# 5. Background pattern off
before = d['bg_pattern']
d['bg_pattern'] = ''
note('bg_pattern', before, '')

# 6. Background colour -> Colour 1
before = d['bg_color']
d['bg_color'] = 'var(--awb-color1)'
note('bg_color', before, 'var(--awb-color1)')

# 7. Content background -> #FDFBF7
before = d['content_bg_color']
d['content_bg_color'] = '#FDFBF7'
note('content_bg_color', before, '#FDFBF7')

# 8. WooCommerce sale badge text colour, fix malformed value
before = d['woo_sale_badge_text_color']
d['woo_sale_badge_text_color'] = 'var(--awb-color1)'
note('woo_sale_badge_text_color', before, 'var(--awb-color1)')

# 9. Page Title Bar -> hide
before = d['page_title_bar']
d['page_title_bar'] = 'hide'
note('page_title_bar', before, 'hide')

# 10. Main menu typography
before = dict(d['nav_typography'])
d['nav_typography']['font-weight'] = '500'
d['nav_typography']['font-size'] = '15px'
d['nav_typography']['letter-spacing'] = '0.1em'
d['nav_typography']['text-transform'] = 'uppercase'
note('nav_typography', before, dict(d['nav_typography']))

# 11. Custom CSS - corrected block
with open('/workspace/Nurture Parenting Magazine rebrand/custom_css_corrected.css') as f:
    corrected_css = f.read()
before = d['custom_css']
d['custom_css'] = corrected_css
note('custom_css', '(typo #fdffbf)', '(fixed #fdfbf7)')

with open('/tmp/fusion_options_updated.json', 'w') as f:
    json.dump(d, f)

print(f"Total keys before: {len(orig)}, after: {len(d)}")
print(f"Applied {len(changes)} changes:")
for k, b, a in changes:
    print(f"  {k}: {b!r} -> {a!r}" if not isinstance(a, dict) else f"  {k}: (dict changed)")
