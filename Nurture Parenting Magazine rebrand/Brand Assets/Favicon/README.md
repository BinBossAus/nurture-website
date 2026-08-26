# Nurture favicon / app icon — final set

The "Solid Monogram" mark: Espresso Earth tile, Porcelain Ivory "N", Rose Gold full stop.
Chosen specifically for the favicon because a bold single letter stays legible at the tiny
sizes browsers actually render it at (as small as 16×16px) — a full wordmark just turns to
mush at that size.

## Files

| File | Size | Use |
|---|---|---|
| `favicon.ico` | 16/32/48/256 (multi-res) | Classic favicon — works everywhere, including old browsers |
| `favicon-16x16.png` | 16×16 | Browser tab (modern browsers) |
| `favicon-32x32.png` | 32×32 | Browser tab (retina), taskbar |
| `favicon-48x48.png` | 48×48 | Windows site icon |
| `apple-touch-icon.png` | 180×180 | iOS "Add to Home Screen" |
| `android-chrome-192x192.png` | 192×192 | Android home screen / PWA |
| `android-chrome-512x512.png` | 512×512 | Android splash screen / PWA, Play Store style listing |
| `nurture-favicon-master.svg` | vector | Source file — outlined paths, edit colours/size from here if this ever needs to change |

## Wiring it into the current site (Avada / WordPress)

Your theme options currently have **one** image reused across four separate upload fields
(`fav_icon`, `fav_icon_apple_touch`, `fav_icon_android`, `fav_icon_edge` in Avada → Theme
Options → General/Layout, or search "favicon" in the options search box). Upload the matching
file from this folder into each field instead of the old stacked logo:

- **Favicon** → `favicon-32x32.png` (or `favicon.ico` if the field accepts `.ico`)
- **Apple Touch Icon** → `apple-touch-icon.png`
- **Android Icon** → `android-chrome-192x192.png`
- **MS Edge / Tile Icon** → `android-chrome-512x512.png`

If you'd rather do it directly in `<head>` (e.g. via a child theme or a header code snippet),
the standard tags are:

```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png">
```

## Recolouring / resizing yourself

Same approach as the primary logo: open `nurture-favicon-master.svg` in a text editor and
change the two `fill="#..."` hex values (the "N" and the full stop). Re-export PNGs at
whatever size you need — because it's vector, nothing gets blurry no matter how large you
render it.
