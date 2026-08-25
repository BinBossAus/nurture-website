# Nurture rebrand — what's actually left to do

This is the fast path. Everything below is derived from what's already in `Nurture Parenting Magazine rebrand/` — the design work, copy and Avada settings are essentially done. The only thing missing was a single ordered list of what's still outstanding, cross-checked against your **actual live Avada Options export** (`fusion_options_backup_25-08-2026.json`) rather than against the original "currently wrong" notes some of the other docs describe (several of those have already been fixed on the live site).

## What's already in this repo

| File | What it is |
|---|---|
| `Nurture Home 2026.dc.html`, `Nurture Advertise 2026.dc.html`, `Nurture Our Story 2026.dc.html` | **Finished, correct** visual mockups — the approved direction. Open these in a browser as your build reference. |
| `Nurture Homepage 1a/1b/1c.dc.html`, `Nurture Homepage.dc.html` | Earlier drafts, **superseded** — they used wrong pricing ($45/$75, "four times a year"). Ignore for copy/pricing. The only thing worth keeping from `1c` is the working 3D cover-shelf CSS, which is already carried into `Home 2026`. |
| `Nurture Build Steps.dc.html` | Ordered checklist: Global Options → Custom CSS cleanup → homepage rebuild → other pages. |
| `Nurture Typography + Colour Spec.dc.html` | Field-by-field Avada Options values (the authoritative settings reference). |
| `Nurture Rebrand Handbook.dc.html` | Why each setting is wrong + rewritten copy for Home and Subscribe (13 more pages queued). |
| `Nurture Page Build Sheet.dc.html` | Section-by-section homepage build spec: exact copy, container/column setup, element choice. |
| `fusion_options_backup_25-08-2026.json` | **Your current live Avada Global Options export.** This is the ground truth for "what's actually live right now." |
| `uploads/nurtureparentingmagazine.WordPress.2026-08-23.xml` | Full WordPress content export (30 pages, 43 posts, 29 products) — source copy for pages not yet rewritten. |
| `content/pages/*.md` | The current site's copy, page by page, already extracted from the export. |
| `_ds/classical-.../` | A separate editorial design system used only to style the handbook *documents themselves* — not part of the actual site direction. Ignore it for the WordPress build; the real brand system is Porcelain Ivory / Espresso Earth / Rose Gold with Playfair Display + Inter, shown in the `2026` mockups. |

## The actual remaining delta in Avada → Options

Diffing `fusion_options_backup_25-08-2026.json` against the Typography + Colour Spec and Build Steps shows **most of Phase 1 is already live**: the 8-colour palette is set correctly, H2 already uses Playfair Display (not Raleway Dots), Lead/Body/Small are no longer uppercase, H1 colour is already Espresso not taupe, and button colour/radius/border-width/typography all already match spec. Don't redo any of that.

What's still outstanding, in the order to fix it:

1. **Typography → Global Typography → Headings preset, and Heading Typography → H1** — both are `68px`, spec wants `46px`. This is currently the single most oversized thing on the site (every H1 renders at 68px).
2. **Typography → Global Typography, link colour fields** — `link_color` and `link_hover_color` are both `var(--awb-color4)` (identical) → links still have no hover state. Set link → `#8C6F61`, hover → `#3A2D28`.
3. **Heading Typography → H5** — currently weight 400 / colour muted-grey; spec wants weight 600 / colour Colour 2 (Espresso).
4. **Elements → Buttons → Border Colour** — still `#000000`; spec wants transparent (everything else about the button — radius 40px, border-width 0, gradient colour, typography — is already correct).
5. **Background → Background Pattern** — still on (`pattern1`); turn off.
6. **Background → Background Colour** — still Colour 3 (Clay Taupe); spec wants Colour 1 (Porcelain Ivory).
7. **Background → Content Background** — still pure `#ffffff`; change to `#FDFBF7` (pure white next to ivory reads as a mistake).
8. **WooCommerce → Product Badges → Sale Badge Text Colour** — still the malformed `var(--awb-color1)fff`; set to Colour 1 cleanly.
9. **Page Title Bar** — still enabled (`bar_and_content`) with a large parallax background image; hide it globally and build each page's own opening section instead (this is what removes the old curved header banners).
10. **Menu → Main Menu typography** — still `26px` with no letter-spacing/text-transform set; change to Inter 500, 14–15px, letter-spacing ~0.08–0.14em, uppercase.
11. **Custom CSS — fix a live typo.** The `.nurture-fade` gradient in your current Custom CSS reads `linear-gradient(to bottom, rgba(253,251,247,0), #fdffbf)` — `#fdffbf` is not a real value in the palette (Ivory is `#fdfbf7`). This silently breaks the fade-to-ivory effect used sitewide. Replace the whole Custom CSS block with the corrected version below.

Everything else in the spec/build-steps docs is already reflected in the live export — skip straight to the list above rather than re-reading every field.

### Corrected Custom CSS (paste this whole block into Avada → Options → Custom CSS, replacing what's there)

```css
/* Nurture — glass surfaces, soft borders, motion */

.nurture-glass{
  background: rgba(253,251,247,.72);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
  border: 1px solid rgba(215,203,194,.35);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 10px 30px rgba(45,36,32,.05),
              inset 0 1px 0 rgba(255,255,255,.6);
  transition: transform .5s cubic-bezier(.2,.7,.2,1),
              box-shadow .5s;
}
.nurture-glass:hover{
  transform: translateY(-4px);
  box-shadow: 0 18px 44px rgba(45,36,32,.09);
}

/* soft borders instead of harsh dark ones */
.fusion-container,.fusion-column,
.fusion-layout-column,.fusion-builder-row{
  border-color: rgba(215,203,194,.35) !important;
}

/* image fading into the page — the section-divider replacement */
.nurture-fade{ position: relative; }
.nurture-fade::after{
  content: ""; position: absolute; inset: auto 0 0 0;
  height: 55%; pointer-events: none;
  background: linear-gradient(to bottom,
              rgba(253,251,247,0), #fdfbf7);
}

/* rose gold glow — one per screen, never more */
.nurture-glow{
  position: absolute; border-radius: 50%;
  pointer-events: none; filter: blur(4px);
  background: radial-gradient(circle,
              rgba(203,177,165,.42),
              rgba(203,177,165,0) 70%);
}

@media (prefers-reduced-motion: reduce){
  .nurture-glass{ transition: none; }
  .nurture-glass:hover{ transform: none; }
}

/* header menu hover/active state — keep, this is already correct */
body #o-container .fusion-main-menu a:hover,
body #o-container .fusion-main-menu .current-menu-item > a,
body #o-container .fusion-main-menu .current_page_item > a,
body .fusion-header-wrapper .fusion-main-menu a:hover,
body .fusion-header-wrapper .fusion-menu-link:hover {
  color: #D6B8AD !important;
}

body #o-container .fusion-main-menu .fusion-menu-link:hover::after,
body #o-container .fusion-main-menu .current-menu-item > a::after,
body #o-container .fusion-main-menu .current_page_item > a::after {
  background-color: #D6B8AD !important;
}
```

Also remove the "curved section separator" element from every container in the Builder (Build Steps step 11) — nothing replaces it; the `.nurture-fade` treatment and generous whitespace does that job.

## Execution order

1. **Back up first.** Avada → Options → Import/Export → Export Options → save the file. (You already have one snapshot in this repo — take a fresh one before touching anything, since the live site has moved on since that export.)
2. **Fix the 11-item delta above** in Avada → Global Options. Use the search box at the top of Options to jump straight to each field.
3. **Paste the corrected Custom CSS** (above) and delete the curved section separators in the Builder.
4. **Rebuild the homepage** section by section using `Nurture Page Build Sheet.dc.html` as the literal spec (container setup, column ratios, element choice) and `Nurture Home 2026.dc.html` as the visual target open in another tab. Section order: Hero → credentials strip → current issue + 3 price cards → Print/Post/Planted → blog → mentors → gift guides → advertisers → Ask Nara + newsletter → footer.
5. **Advertise and Our Story** are also fully designed and copy-approved (`Nurture Advertise 2026.dc.html`, `Nurture Our Story 2026.dc.html`) — build these next using the same section-by-section approach (container/column notes aren't written out per-section for these two the way they are for Home, but the finished HTML is close enough to lift structure and copy directly).
6. **Then the remaining pages**, in the order the Rebrand Handbook suggests: Shop → Contributors → Blog → Changemakers → Self Love → Love of Learning → Showcase → Australian Made → Mama & Bubba Essentials → Services → Contact. Source copy for these is in `content/pages/*.md`; each still needs the same voice pass Home and Subscribe already got (specific over aspirational, no emoji/exclamation marks, Australian spelling, claims tied to something checkable).

## Two decisions needed before content work continues (from Build Steps)

These block Claude/whoever is doing the copy pass from finishing the remaining pages — they don't block the Options/CSS/homepage work above, so don't let them slow down steps 1–5:

1. **Sales, Next Steps, Getting Started Sales Guide, Creative Brief, Booking** (~21,000 words total) — these read like internal advertiser sales collateral rather than public pages. Confirm whether they're customer-visible (and need the same voice/design pass) or internal-only (and can be left alone / moved off the public site).
2. **43 blog post titles** — most are currently in full capitals. Confirm whether these should be rewritten too (quick, visible win if so).

## On "a really exciting new parenting journey"

The approved direction already delivers this, and redesigning further now would slow you down rather than speed you up:

- **Ask Nara** — a searchable archive across 14 years of back issues, every answer citing its source issue. This is the standout differentiator; make sure it's placed prominently (homepage + its own accessible entry point, not buried).
- **The 3D cover shelf** — three issue covers overlapping and parting on hover, real depth via `perspective`/`transform-style: preserve-3d` (already working in the `Home 2026` markup).
- **Mentors, named** — six practitioners answering under their own names rather than an anonymous "expert panel."
- **The sustainability story (Print / Post / Planted)** — concrete and checkable rather than a vague eco-badge.
- **Warm photographic fades** replacing the dated curved section dividers site-wide.

If you want one further stretch enhancement without slowing the build: lightweight "stage of parenting" filter chips (pregnancy / newborn / toddler / school-age) on the blog grid, reusing the existing four-domain (Emotional/Intellectual/Physical/Spiritual) taxonomy already established in the copy — this is additive to the current plan, not a redesign, so it can be layered on after the pages above are live.
