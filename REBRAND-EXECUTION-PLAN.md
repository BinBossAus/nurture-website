## Progress log (2026-08-25, execution run)

Executed directly against the live site over HTTP (admin login + REST API — see
`Nurture Parenting Magazine rebrand/scripts/README.md` for exactly how). Status:

- ✅ Fresh Avada Options backup taken (`fusion_options_backup_2026-08-25_pre-rebrand.json`) before any change.
- ✅ All 11 Global Options delta items fixed (H1/Headings 46px, link colours, H5, button border, background pattern/colour, content background, Woo sale badge, Page Title Bar hidden, main menu typography).
- ✅ Custom CSS replaced with the corrected block (`#fdffbf` typo fixed).
- ✅ Homepage rebuilt section-by-section per the Page Build Sheet.
- ✅ Subscribe, Advertise, Our Story, Contact, Contributors rebuilt.
- ✅ Shop rebuilt (hero + category chips + directory teaser), keeping the real `[fusion_woo_product_grid]` catalogue live, now sectioned by real product category.
- ✅ Blog rebuilt (hero + chips), keeping the real `[fusion_recent_posts]` loop — none of the 43 posts' copy touched.
- ✅ Showcase index + all 6 category hubs (Changemakers, Self Love, Love of Learning, Australian Made, The Essentials, Tested on Humans) built from one shared template.
- ✅ **The Directory** — the one page that didn't exist — built and published at `/directory/`; Shop's "Browse the directory" button now links to it instead of `#`.
- ✅ Main nav "Mentors" item corrected to point at the homepage `#mentors` section instead of `/contributors/` (Mentors ≠ Contributors, per Decisions below).
- ✅ **Homepage hero duplication fixed.** Root cause: two Avada Theme Builder "Header" layout sections (post IDs 5388 "Header" and 1206 "Nurture Header" — only one actually renders as the live site header, but both had been edited) each had the *entire* old homepage hero (`fusion_title`/`fusion_button` shortcodes, "Read the magazine" copy) built as a second column sitting inside the header row itself, left over from earlier work on this rebrand. Removed that column from both via the classic `wp-admin/post.php` edit form (no REST route exists for this CPT — see `scripts/push_layout_section.py`), keeping only the real logo/menu/subscribe-button column. Verified: every page now shows its hero/heading text exactly once.
- ✅ Sitewide footer rebuilt. It turned out `1245` ("Nurture Custom Footer") was still the **unmodified Avada "Barber Shop" demo footer** just renamed (its Live Builder URL literally reads `.../fusion_tb_section/barbers-custom-footer/`) — old PNG logo, old structure. Replaced with the Page Build Sheet's spec: dark `#3A2D28` background, 4 columns (2/1/1/1), Playfair "Nurture." wordmark with a rose full stop, Read/Shop/Nurture link columns (Directory now linked here too), copyright bar. See `scripts/build_footer.py`.
- ⏳ "Services" page left untouched — status still unconfirmed per the plan (needs a business decision, not something to guess at). Real photography/brand logos/mentor photos still placeholders — see `scripts/README.md` for exactly which, and why (never stock photos standing in for named real people or specific brands).

## Live launch (2026-08-25, same session)

- ✅ Avada `maintenance_mode` switched from `coming_soon` → off (`scripts/go_live.py`). Verified as a genuine anonymous visitor (no cookies): the real homepage and every rebuilt page now load directly, robots meta is the normal indexable tag (no more forced `noindex`), and `blog_public` (Settings → Reading → discourage search engines) was already unchecked, so the site is now indexable.
- ✅ Sales / Next Steps / Getting Started Sales Guide / Creative Brief / Booking — per the Decisions above, these were explicitly called out as not meant to be public-facing. They were already unlinked from navigation, but for an actual live launch that's not enough (still reachable by direct URL / could get indexed) — set all five to Draft status via the REST API. Confirmed each now 404s for anonymous visitors. Content itself is untouched/recoverable (still exists as drafts) in case it's needed later as internal collateral, per the plan's own suggestion.
- ✅ Fresh post-launch Avada Options backup saved (`fusion_options_backup_2026-08-25_post-launch.json`).
- "Services" page: left as-is (published, unlinked from main nav) — its fate is a business decision the plan explicitly flagged as unconfirmed, not a launch blocker.

# Nurture rebrand — what's actually left to do

This is the fast path. Everything below is derived from what's already in `Nurture Parenting Magazine rebrand/` — the design work, copy and Avada settings are essentially done. The only thing missing was a single ordered list of what's still outstanding, cross-checked against your **actual live Avada Options export** (`fusion_options_backup_25-08-2026.json`) rather than against the original "currently wrong" notes some of the other docs describe (several of those have already been fixed on the live site).

## Update (2026-08-25, second upload): the page set is now complete

A full second batch landed and has been merged in and de-duplicated (it arrived as a nested `... ALL IN ONE FILE/` copy of the entire folder plus 12 new pages; the new pages have been moved up to sit flat alongside the others, the redundant duplicate copy has been deleted, and the superseded `Homepage`/`1a`/`1b`/`1c` drafts have been removed per Claude's own `github.md` note marking them "do not upload"). Every file below was verified byte-for-byte before anything was deleted — nothing was lost.

**Every page in the nav now has a finished, on-brand mockup.** This changes the execution order significantly — see the updated order further down.

## Screen map (from `github.md`, verified against the actual files)

| Page | File | Notes |
|---|---|---|
| Home | `Nurture Home 2026.dc.html` | Hero, current issue + pricing, Print/Post/Planted, blog teaser, mentors, gift guides, brands strip, Ask Nara/newsletter, footer. |
| Subscribe | `Nurture Subscribe 2026.dc.html` | 3 pricing tiers ($20/$55/$95, consistent everywhere), "what's in every issue," digital back issues. |
| Shop | `Nurture Shop 2026.dc.html` | **A real storefront**, not the directory — filterable chips (Subscriptions/Back issues/Digital/Planners/Bundles), individual back-issue and product cards. Ends with a teaser section pointing at "the conscious directory" (button currently links to `#` — **the Directory page itself still doesn't exist yet**, see below). |
| Blog | `Nurture Blog 2026.dc.html` | Category chips, featured story, 6 article cards, newsletter close. Nav labelled "Read." |
| Contributors | `Nurture Contributors 2026.dc.html` | The writers/photographers team page — confirmed distinct from the homepage "Mentors" section. |
| Contact | `Nurture Contact 2026.dc.html` | |
| Advertise | `Nurture Advertise 2026.dc.html` | Point "Request the media kit" at Tally.so. |
| Our Story | `Nurture Our Story 2026.dc.html` | |
| Showcase (index) | `Nurture Showcase 2026.dc.html` | Index/hub linking to the 6 category hubs below. |
| Changemakers, Self Love, Love of Learning, Australian Made, The Essentials, Tested on Humans | `Nurture [name] 2026.dc.html` | **6 category hubs, all one template**: shared sub-nav bar across all 6 + Showcase, hero, one big featured cover-story card, 6 article cards, a "nominate/get in touch" glass CTA panel, and a "keep shopping" strip cross-linking every other hub. Build the template once, then repeat with each hub's own content. `The Essentials` is the renamed `Mama & Bubba Essentials`. `Tested on Humans` is new (team-tested product picks) and wasn't in the original page queue — confirm this is intentional if it's not already on your radar. |

## What's still genuinely missing

- **The Directory itself.** Every page (Shop, Subscribe, footer everywhere) now links to "the conscious directory" / "Browse the directory," but that page doesn't exist as a mockup yet — every link to it currently points at `#`. This is the one still-needed page, and it's the highest priority one: it's what print QR codes will point to. Build it as the categorised advertiser card grid described earlier in this doc (one template card, duplicated per advertiser/issue).
- **Services** was in the original page queue (from the Rebrand Handbook) but isn't part of this new set — confirm whether it's still needed or has been folded into one of the hubs/Contact.
- Everything else in the nav and footer now resolves to a real, finished page.

## Other files already in this repo

| File | What it is |
|---|---|
| `Nurture Build Steps.dc.html` | Ordered checklist: Global Options → Custom CSS cleanup → homepage rebuild → other pages. |
| `Nurture Typography + Colour Spec.dc.html` | Field-by-field Avada Options values (the authoritative settings reference). |
| `Nurture Rebrand Handbook.dc.html` | Why each setting is wrong + rewritten copy for Home and Subscribe. |
| `Nurture Page Build Sheet.dc.html` | Section-by-section homepage build spec: exact copy, container/column setup, element choice. |
| `fusion_options_backup_25-08-2026.json` | **Your live Avada Global Options export as of 25 Aug.** Re-export a fresh one before actually making changes — the live site may have moved since. |
| `uploads/nurtureparentingmagazine.WordPress.2026-08-23.xml` | Full WordPress content export (30 pages, 43 posts, 29 products) — source copy for pages not yet rewritten. |
| `content/pages/*.md` | The current site's copy, page by page, already extracted from the export. Note: `home.md` ends with two base64-encoded shortcodes — one is an Instagram feed shortcode, the other is the existing ConvertKit ("The Hive") signup script tag. Both are real, currently-live embeds worth reusing rather than rebuilding. |
| `_ds/classical-.../` | A separate editorial design system used only to style the handbook *documents themselves* — not part of the actual site direction. Ignore it for the WordPress build; the real brand system is Porcelain Ivory / Espresso Earth / Rose Gold with Playfair Display + Inter, shown in the `2026` mockups. |
| `github.md` | Claude's own manifest/changelog of what it built — kept for reference. |

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
5. **Every other nav page now has a finished mockup** (see the Screen map above) — build them in this order, each the same way (lift structure/copy/settings straight from its own `2026.dc.html` file, none have the section-by-section build sheet Home got, but the finished HTML is detailed enough to build from directly):
   - **Subscribe, Advertise, Our Story** — straightforward single builds.
   - **Shop** — the storefront (chips + product cards). Leave the "Browse the directory" button pointing at `#` until the Directory page (below) exists.
   - **Blog** — re-skin only, see "Blog: rebrand the frame, not the copy" below; don't rewrite the 43 existing posts.
   - **Contributors, Contact** — straightforward single builds.
   - **The 6 category hubs + Showcase index** (Changemakers, Self Love, Love of Learning, Australian Made, The Essentials, Tested on Humans) — build the shared template once (sub-nav bar, hero, featured story card, 6 article cards, CTA panel, "keep shopping" strip), then repeat per hub with that hub's own content. Much faster once the template's built the first time.
   - **The Directory** — build this once the above are live; it's the one page in the whole nav that doesn't have a mockup yet (see "What's still genuinely missing," above). Highest priority once you reach it, since it's the print QR-code destination.
   - **Services** — status unclear, confirm if still needed (see above).
   - **Sales, Next Steps, Getting Started Sales Guide, Creative Brief, Booking are dropped entirely** — not in this list, not rebuilt, not linked from nav (see Decisions, below).

## Decisions confirmed (2026-08-25)

- **Sales / Next Steps / Getting Started Sales Guide / Creative Brief / Booking are out.** None of these are live or developed, and keeping "sales" material as public-facing pages cheapens the site. They are not in the page queue above and shouldn't be rebuilt, rebranded or linked from navigation. If any of that content is genuinely needed later (e.g. as the interactive media kit once Nara can serve it), treat it as a separate, internal-only project — not part of this site rebuild.
- **The Nara SaaS (client comms/proposals/automation/chatbot) is a separate, unfinished 9-month project** and is explicitly *not* part of this website rebuild. Nothing in the site build should depend on it being ready. See "Ask Nara" below for how the one homepage slot that referenced it gets handled now.
- **Lead capture, for now:** Tally.so for the gated media-kit download, ConvertKit for eNews signups (pre-relaunch list-building now, next-edition announcements once site + Nara are live). Both are interim — expect Nara to eventually absorb lead forms/automation, but don't build anything bespoke for that now. See "Lead capture & integrations" below.

## Navigation & page structure

Resolving the ambiguity in the original nav labels:

- **Subscribe** — print + digital subscriptions and single-issue purchase (the three pricing tiers already on Home/Subscribe). No change needed.
- **Read** → the **blog**. Keep this distinct from back issues: back issues/emag stay under **Subscribe** (the "Digital back issues" section already written into the Subscribe page copy), since they're a purchase/download, not free editorial. One copy fix to make while building the hero: "Read the magazine" as a button label is ambiguous against this split — it currently links to the free blog (`#read`), which reads like it should mean the actual magazine. Either relabel that hero button to something like "Read the blog" / "Free articles," or repoint it at the digital back-issues section instead. Pick one when you build the hero; don't leave the mismatch as-is.
- **Mentors ≠ Contributors — these are two different things, not a rename.** Mentors are the six named practitioners who host the monthly live Q&A in the private Facebook group (Penny, Andrea, Crystal, Stephanie, Micarlé, Naomi) — that's the homepage "Mentors" section as designed. Contributors/"Team" is the separate, existing page (`content/pages/contributors.md`, ~1,090 words) for the broader roster of writers and photographers who write for the magazine. Keep both — don't merge them. Given the main nav is already getting full (Subscribe, Read, Mentors, Shop, Advertise), consider keeping Contributors out of the primary nav and linking it instead from the footer and from Our Story, rather than adding a sixth top-level item — your call.
- **Correction from earlier in this doc: Shop is a real storefront, not the Directory.** Claude's actual `Nurture Shop 2026.dc.html` build confirms Shop = subscriptions, single/back issues, the digital archive, planners and bundles (filterable by category) — a proper shop page, exactly as its own nav item suggests. **The Directory is a separate page that doesn't exist yet** (see "What's still genuinely missing," above) — it's linked from Shop, Subscribe, and the footer, but every link currently points at `#`. Build it next in priority, since it's the one print QR codes will point to.
- **"Brands we love" (or a new name) stays on the homepage, separate from both Shop and the Directory.** This is the paid homepage-placement inclusion in certain ad packages — a small, fixed logo strip, not the full categorised directory. It's already in `Home 2026` as the "For brands" section; keep it, just confirm a final name if "Brands we love" doesn't fit anymore (e.g. "Brands we back," "In good company").

## The advertiser Directory (build this — it's the one page still missing)

Because print QR codes will point straight at this page and it needs a new advertorial feature added every issue, keep the build dead simple: one card component (logo/image, brand name, one-line description, category tag, outbound link) built once in Fusion Builder in the same visual language as the Shop/Blog/hub pages (glass cards, category chips), then copied and edited for each advertiser. Group by category. This avoids depending on Nara's future automation to keep it current — anyone can duplicate a card between issues. Once built, fix the `#` placeholder links on Shop, Subscribe and the footer to point at it.

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

## Digital edition / back issues presentation (not blocking the site build)

Current back issues are presented via Designrr flipbooks (linked from Subscribe/back-issues and from at least one gift guide PDF). Two separate moves, neither urgent for the site relaunch:

- **Fast swap, whenever there's a spare hour:** re-embed the same PDFs in ZenFlip or Publuu instead of Designrr — no watermark, real analytics, no design work, same source PDF. ZenFlip's built-in AI-chat-over-PDF feature is also a genuine (if partial) stopgap for "AI answers about an issue" before Nara ships.
- **The real upgrade, planned alongside the InDesign remaster:** move away from the page-curl/PDF metaphor entirely for new issues — publish as native responsive web pages in the new design system instead. This is not just aesthetic: a PDF/flipbook is opaque to search, so as long as issues live only as flipbooks, Ask Nara can never actually index them once it ships. Worth raising with whoever handles the InDesign rebuild — check if the export workflow can produce a web/HTML version alongside print, so future issues are searchable from day one. Back issues can stay as PDFs behind the nicer viewer in the meantime.

## On "a really exciting new parenting journey"

The approved direction already delivers most of this, and redesigning further now would slow you down rather than speed you up:

- **The 3D cover shelf** — three issue covers overlapping and parting on hover, real depth via `perspective`/`transform-style: preserve-3d` (already working in the `Home 2026` markup).
- **Mentors, named** — six practitioners answering under their own names rather than an anonymous "expert panel," tied to the real monthly live Q&A in the private group.
- **The sustainability story (Print / Post / Planted)** — concrete and checkable rather than a vague eco-badge.
- **Warm photographic fades** replacing the dated curved section dividers site-wide.
- **The "Ask Nara — coming soon" tease** itself does journey-building work here: it tells returning visitors and advertisers that the brand is mid-relaunch and something bigger is coming, without needing the SaaS finished.

One further stretch enhancement, additive only, layer on after the pages above are live: lightweight "stage of parenting" filter chips (pregnancy / newborn / toddler / school-age) on the blog grid, reusing the existing four-domain (Emotional/Intellectual/Physical/Spiritual) taxonomy already established in the copy.
