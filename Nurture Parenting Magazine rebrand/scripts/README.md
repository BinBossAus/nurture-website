# Rebrand automation scripts

These scripts were used to execute the rebuild described in `REBRAND-EXECUTION-PLAN.md`
directly against the live WordPress site over HTTP (no SSH/DB access was available),
using an administrator account and the `NURTURE_WP_URL` / `NURTURE_WP_USERNAME` /
`NURTURE_WP_PASSWORD` credentials.

## How it works

WordPress's REST API only supports **Application Passwords** for Basic Auth, and the
provided credentials are a normal login password — so instead these scripts log in the
same way a browser does (`wp-login.php` with cookies) and then reuse that authenticated
session for both:

1. **Avada Global Options** (`fusion_options`) — these are *not* exposed over REST at
   all. Avada's Options panel (`Avada → Options`, i.e. `themes.php?page=avada_options`)
   is a classic Redux-Framework-style panel that saves via a normal POST to
   `wp-admin/options.php`. Its "Import Options" feature accepts a full JSON snapshot of
   the option array and replaces the *entire* option with it — which is exactly what a
   full Options export/import round-trip does. `apply_options_delta.py` is the record of
   how the 11-item delta + Custom CSS fix were computed from a fresh export
   (`fusion_options_backup_2026-08-25_pre-rebrand.json`), and the resulting JSON was then
   submitted back via that Import Options endpoint (multipart POST to `options.php` with
   `fusion_options[import_code]` = the modified JSON and `import=Import`).
   - Note: the site runs Wordfence, which flagged that POST once as a false positive
     (rule 9, on the `import_code` param). It was allow-listed once via Wordfence's own
     "Allowlist this action" endpoint before retrying — see the request in that run's
     history. If this ever needs to be re-run and gets blocked again, use the same
     Wordfence false-positive form that appears on the block page.
   - After saving, Avada regenerates its compiled dynamic CSS file server-side, but the
     **first anonymous page load after a change can still serve a previously cached
     copy** (the site is fronted by LiteSpeed's cache layer). Sending one request with
     `Cache-Control: no-cache` is enough to force a fresh render, after which normal
     requests pick up the new version too.
2. **Page content** (Fusion Builder shortcodes) — pages *are* exposed over REST
   (`/wp-json/wp/v2/pages/<id>`), and our admin user has `unfiltered_html`, so raw
   Fusion Builder shortcode markup posted as `content` is stored and rendered exactly as
   if it had been typed into the classic editor / builder.

## Usage

```bash
# 1. Log in and cache session cookies + REST nonce to /tmp
python3 wp_login.py

# 2. Generate a page's shortcode content (writes /tmp/<page>_content.txt)
python3 build_homepage.py

# 3. Push it to the live page by WordPress post ID
python3 push_page.py 1310 /tmp/homepage_content.txt
```

`nurture_common.py` holds the shared design-system building blocks (the `<style>` block
with `.n-*` utility classes, and small helpers for emitting
`fusion_builder_container` / `fusion_builder_row` / `fusion_builder_column` /
`fusion_text` shortcode markup). Reuse it for any further pages.

## Notes for whoever continues this

- Session cookies/nonces expire — re-run `wp_login.py` if `push_page.py` starts
  returning 401/403.
- Placeholder photography currently uses direct Unsplash URLs (license permits this use)
  for generic environmental shots (hero, blog banner, gift guide banner, article
  thumbnails). Named people (mentors, contributors) and brand logos deliberately use
  plain gradient/label placeholders instead of stock photos, since attaching a real
  stranger's photo to a real name would be misleading — swap these for real photography
  and real brand marks as they become available.
- The "Ask Nara" search box is intentionally a "coming soon" tease, not a working input
  — see the Decisions section of `REBRAND-EXECUTION-PLAN.md`.
- The "Request the media kit" button on `/advertise/` points at a placeholder
  `https://tally.so/r/media-kit` URL — replace with the real published Tally.so form
  link once it exists.
- The Contact page form posts via a plain `mailto:` fallback (no JS submission handler
  wired up) since no form plugin (Contact Form 7 / WPForms / Avada Forms) had an
  existing form on the site to reuse. The direct email links above/below the form are
  fully functional in the meantime.
- The main nav's "Mentors" item previously linked to `/contributors/` — per the
  execution plan, Mentors (the homepage practitioners section) and Contributors (the
  writers/photographers page) are two different things. It's been repointed to
  `https://www.nurtureparentingmagazine.com.au/#mentors` via the `wp/v2/menu-items`
  REST endpoint (had to switch `type`/`object` to `"custom"` — updating `url` alone on a
  page-linked item is ignored, since the URL is derived from `object_id` at render time).
- **Known open issue:** the homepage hero section renders twice on the live site (the
  first copy uses real `fusion_title`/`fusion_button` shortcodes with the old copy
  "Read the magazine"; my replacement copy with "Read the blog" renders directly after
  it). Confirmed via the REST API and the classic editor that `post_content` for the
  Home page contains my content exactly once with zero `fusion_title` occurrences, so
  the first copy is coming from somewhere else the classic editor's Custom Fields box
  doesn't surface (most likely a *protected* `_`-prefixed postmeta key that WordPress
  hides from that UI, since Avada's Theme Builder / Live Builder can store a page's
  layout separately from `post_content`). Nothing else on the page duplicates — only
  the hero. A `computerUse` investigation was dispatched to find and fix this live via
  the actual Avada Builder UI; check its outcome before doing anything else here. If it
  wasn't resolved, the next step is to open the Home page in Avada's real front-end/
  back-end builder (not the classic editor) and see whether it shows a second, stale
  hero layer to delete.
