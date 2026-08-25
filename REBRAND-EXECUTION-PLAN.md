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
| `content/pages/*.md` | The current site's copy, page by page, already extracted from the export. Note: `home.md` ends with two base64-encoded shortcodes — one is an Instagram feed shortcode, the other is the existing ConvertKit ("The Hive") signup script tag. Both are real, currently-live embeds worth reusing rather than rebuilding. |
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
4. **Rebuild the homepage** section by section using `Nurture Page Build Sheet.dc.html` as the literal spec (container setup, column ratios, element choice) and `Nurture Home 2026.dc.html` as the visual target open in another tab. Section order: Hero → credentials strip → current issue + 3 price cards → Print/Post/Planted → blog → mentors → gift guides → brands strip → **"Ask Nara" placeholder** + newsletter (ConvertKit) → footer. See "Ask Nara — decouple from the Nara SaaS build" below for what goes in that slot right now.
5. **Advertise and Our Story** are also fully designed and copy-approved (`Nurture Advertise 2026.dc.html`, `Nurture Our Story 2026.dc.html`) — build these next using the same section-by-section approach (container/column notes aren't written out per-section for these two the way they are for Home, but the finished HTML is close enough to lift structure and copy directly). On Advertise, point "Request the media kit" at the Tally.so form (see Lead capture, below), not a mailto or a static download.
6. **Then the remaining pages**, in this order: Shop/Directory → Contributors → Blog (re-skin only, see below) → Changemakers → Self Love → Love of Learning → Showcase → Australian Made → Mama & Bubba Essentials → Services → Contact. Source copy for these is in `content/pages/*.md`; each still needs the same voice pass Home and Subscribe already got (specific over aspirational, no emoji/exclamation marks, Australian spelling, claims tied to something checkable). **Sales, Next Steps, Getting Started Sales Guide, Creative Brief and Booking are dropped from this list entirely** — see Decisions, below.

## Decisions confirmed (2026-08-25)

- **Sales / Next Steps / Getting Started Sales Guide / Creative Brief / Booking are out.** None of these are live or developed, and keeping "sales" material as public-facing pages cheapens the site. They are not in the page queue above and shouldn't be rebuilt, rebranded or linked from navigation. If any of that content is genuinely needed later (e.g. as the interactive media kit once Nara can serve it), treat it as a separate, internal-only project — not part of this site rebuild.
- **The Nara SaaS (client comms/proposals/automation/chatbot) is a separate, unfinished 9-month project** and is explicitly *not* part of this website rebuild. Nothing in the site build should depend on it being ready. See "Ask Nara" below for how the one homepage slot that referenced it gets handled now.
- **Lead capture, for now:** Tally.so for the gated media-kit download, ConvertKit for eNews signups (pre-relaunch list-building now, next-edition announcements once site + Nara are live). Both are interim — expect Nara to eventually absorb lead forms/automation, but don't build anything bespoke for that now. See "Lead capture & integrations" below.

## Navigation & page structure

Resolving the ambiguity in the original nav labels:

- **Subscribe** — print + digital subscriptions and single-issue purchase (the three pricing tiers already on Home/Subscribe). No change needed.
- **Read** → the **blog**. Keep this distinct from back issues: back issues/emag stay under **Subscribe** (the "Digital back issues" section already written into the Subscribe page copy), since they're a purchase/download, not free editorial. One copy fix to make while building the hero: "Read the magazine" as a button label is ambiguous against this split — it currently links to the free blog (`#read`), which reads like it should mean the actual magazine. Either relabel that hero button to something like "Read the blog" / "Free articles," or repoint it at the digital back-issues section instead. Pick one when you build the hero; don't leave the mismatch as-is.
- **Mentors ≠ Contributors — these are two different things, not a rename.** Mentors are the six named practitioners who host the monthly live Q&A in the private Facebook group (Penny, Andrea, Crystal, Stephanie, Micarlé, Naomi) — that's the homepage "Mentors" section as designed. Contributors/"Team" is the separate, existing page (`content/pages/contributors.md`, ~1,090 words) for the broader roster of writers and photographers who write for the magazine. Keep both — don't merge them. Given the main nav is already getting full (Subscribe, Read, Mentors, Shop, Advertise), consider keeping Contributors out of the primary nav and linking it instead from the footer and from Our Story, rather than adding a sixth top-level item — your call.
- **Shop → the advertiser Directory**, not a generic storefront. This is the page print QR codes will point to, so it needs a stable URL and to be easy to update every issue without a developer. Build it as a categorised grid of advertiser cards (logo, one line, link out) — the same content currently sitting in the "Natural Parenting Directory" section on the homepage export, just promoted to its own page. Structure it once in the Builder as a template card, then duplicate/edit per new advertiser or per-issue feature; no plugin or custom post type needed to move fast.
- **"Brands we love" (or a new name) stays on the homepage, separate from the Shop/Directory page.** This is the paid homepage-placement inclusion in certain ad packages — a small, fixed logo strip, not the full categorised directory. It's already in `Home 2026` as the "For brands" section; keep it, just confirm a final name if "Brands we love" doesn't fit anymore (e.g. "Brands we back," "In good company").

## The advertiser Directory (Shop)

Because print QR codes will point straight at this page and it needs a new advertorial feature added every issue, keep the build dead simple: one card component (logo/image, brand name, one-line description, category tag, outbound link) built once in Fusion Builder, then copied and edited for each advertiser. Group by category (matching whatever categories the current homepage directory images use). This avoids depending on Nara's future automation to keep it current — anyone can duplicate a card between issues.

## Blog: rebrand the frame, not the copy

Two separable jobs here, and they're very different in size:

- **Re-skinning the blog template (fast, one-time, applies to all 43 posts automatically).** This is just the Blog → Blog Post Title and Blog archive/grid typography settings (already specified in the Typography + Colour Spec) plus rebuilding the Blog element on the homepage and the archive page with the new card design (rounded image, 5:4 ratio, category label, Playfair title) from the Page Build Sheet. Zero per-post work — every existing post inherits it the moment the template changes. **Copy stays as written**, per your call — don't rewrite the 43 posts.
- **Swapping featured images (real, per-post work, proportional to how many posts you do).** This is the part that's "a big job" if you do all 43 at once. Fastest path: don't block the site launch on this. Do the **3 posts already featured on the homepage blog teaser** first (Sleep/Feeding/Connection in the current mock, or whichever 3 you actually feature), since those are the highest-visibility ones, ship the site, then work through the remaining 40 progressively afterwards — clients seeing the relaunch won't be looking at every archive post on day one. If sourcing new photography for 43 posts isn't realistic soon, on-brand AI-generated or stock imagery (warm, natural light, matching the `.ph` placeholder style already used in the mockups) is a reasonable stand-in until real photography exists for each.

## Ask Nara — decouple from the Nara SaaS build

Claude's mockup put a live "Ask Nara" search box on the homepage, but that assumes the Nara SaaS's AI search backend — which is a separate nine-month build and isn't ready. Don't block this website on it. For the relaunch:

- **Fastest, and recommended:** replace that homepage slot with a "coming soon" tease instead of a working input — e.g. "Ask Nara — our AI-powered search across 14 years of back issues, launching soon." This costs nothing to build, sets correct expectations, and does real work for you strategically: it signals momentum on the relaunch (which is exactly the message you want right now) without needing any backend.
- **If you want something functional now instead of a tease:** the honest fastest option is plain WordPress search scoped to the blog/back-issues content (native search, or a lightweight search plugin) — but that's keyword search, not AI, so don't call it "Ask Nara" if it isn't. A real AI/RAG search over the archive is a genuine separate build, not something to bolt on quickly alongside the visual relaunch — treat it as a Nara SaaS deliverable, shipped when Nara ships, as you already suspected.
- Keep the newsletter half of that homepage section (the ConvertKit "Join the Hive" embed) — that's already live and unaffected by any of this.

## Lead capture & integrations (interim, pre-Nara)

- **Media kit download** (from the Advertise page's "Request the media kit" button, and the homepage "For brands" section) → **Tally.so** form. Embed or link out; capture the fields you need (name, brand, package interest) before releasing the kit.
- **eNews / newsletter signup** → **ConvertKit**, already live on the current site as "The Hive" (`the-nurture-parenting-magazine-hive.kit.com` — the embed script is already in `content/pages/home.md`, base64-encoded at the bottom of the file). Reuse this embed as-is in the new "The letter" section of the rebuilt homepage rather than rebuilding it.
- Both are explicitly interim. Don't build custom integration work between Tally/ConvertKit and anything else right now — plan for Nara to eventually take over lead forms, the interactive media kit and chatbot/agentic sales once it ships, and keep these two simple tools decoupled from everything else until then.

## On "a really exciting new parenting journey"

The approved direction already delivers most of this, and redesigning further now would slow you down rather than speed you up:

- **The 3D cover shelf** — three issue covers overlapping and parting on hover, real depth via `perspective`/`transform-style: preserve-3d` (already working in the `Home 2026` markup).
- **Mentors, named** — six practitioners answering under their own names rather than an anonymous "expert panel," tied to the real monthly live Q&A in the private group.
- **The sustainability story (Print / Post / Planted)** — concrete and checkable rather than a vague eco-badge.
- **Warm photographic fades** replacing the dated curved section dividers site-wide.
- **The "Ask Nara — coming soon" tease** itself does journey-building work here: it tells returning visitors and advertisers that the brand is mid-relaunch and something bigger is coming, without needing the SaaS finished.

One further stretch enhancement, additive only, layer on after the pages above are live: lightweight "stage of parenting" filter chips (pregnancy / newborn / toddler / school-age) on the blog grid, reusing the existing four-domain (Emotional/Intellectual/Physical/Spiritual) taxonomy already established in the copy.
