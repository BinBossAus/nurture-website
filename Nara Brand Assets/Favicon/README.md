# Nara favicon / app icon — final set

Same "Solid Monogram" treatment as Nurture's favicon: Espresso Earth tile, Porcelain Ivory "N",
Rose Gold full stop. Since Nara also starts with "N", this favicon is visually identical to
Nurture's — intentional, for shared recognition (see the note in the top-level `README.md` if
you'd rather they be distinguishable).

## Files

| File | Size | Use |
|---|---|---|
| `favicon.ico` | 16/32/48/256 (multi-res) | Classic favicon — works everywhere |
| `favicon-16x16.png` | 16×16 | Browser tab (modern browsers) |
| `favicon-32x32.png` | 32×32 | Browser tab (retina), taskbar |
| `favicon-48x48.png` | 48×48 | Windows site icon |
| `apple-touch-icon.png` | 180×180 | iOS "Add to Home Screen" |
| `android-chrome-192x192.png` | 192×192 | Android home screen / PWA |
| `android-chrome-512x512.png` | 512×512 | Android splash screen / PWA |
| `nara-favicon-master.svg` | vector | Source file — edit colours/size from here |

## Standard `<head>` tags

```html
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="icon" type="image/png" sizes="192x192" href="/android-chrome-192x192.png">
```

If Nara lives on its own site/subdomain, point that site's equivalent theme-options favicon
fields at these files (same idea as the Avada field mapping documented for Nurture).

## Recolouring / resizing yourself

Open `nara-favicon-master.svg` in a text editor, change the two `fill="#..."` hex values, and
re-export PNGs at whatever size you need — vector source, so nothing blurs.
