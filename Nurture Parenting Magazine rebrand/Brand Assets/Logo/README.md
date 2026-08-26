# Nurture logo — master files (2026 rebrand)

The new wordmark, replacing the old logo. Typeface is **Playfair Display, Medium (500)** — the
same serif used for all headings across the rebrand — with the full stop carried in **Rose Gold**.
Every letterform in these files has been **outlined to vector paths** (not live text), so the logo
opens, places, prints and scales identically on any machine, even one without the font installed.

## Files

| File | Wordmark colour | Full stop colour | Use on |
|---|---|---|---|
| `nurture-logo-primary.svg` | Espresso Earth `#3A2D28` | Rose Gold `#CBB1A5` | Light / ivory backgrounds (default logo) |
| `nurture-logo-reverse.svg` | Porcelain Ivory `#FDFBF7` | Rose Gold `#CBB1A5` | Dark / espresso backgrounds — this is the version used on the Media Kit cover |
| `nurture-logo-mono-black.svg` | Deep Charcoal `#2A201C` | Deep Charcoal `#2A201C` | Single-colour print: fax, engraving, stamps, foil |
| `nurture-logo-mono-white.svg` | Porcelain Ivory `#FDFBF7` | Porcelain Ivory `#FDFBF7` | Single-colour knockout on dark/photo backgrounds |

All four are the same artwork — only the two fill colours differ.

## Opening in InDesign

1. **File → Place** (or `Cmd/Ctrl + D`), choose the SVG, click to place it on the page.
2. Resize freely by dragging a corner handle with **Shift** held (keeps proportions) — because
   it's vector, it stays perfectly crisp from a postage stamp to a billboard. There is no
   "maximum" print size.
3. To make it a reusable brand asset, drag it into your **CC Library** or InDesign **Object Styles**
   once placed.

## Changing the colour yourself (no Illustrator needed)

Each file has exactly two colour values to edit — the wordmark and the full stop — near the top of
the file. Open the `.svg` in any plain text editor (TextEdit in *plain text mode*, Notepad, VS Code,
even opening it in a browser and viewing source) and change the two `fill="#......"` hex codes:

```
<g id="Wordmark" fill="#3A2D28">      ← the word "Nurture"
<g id="Full-Stop" fill="#CBB1A5">     ← the "." only
```

Swap in any brand hex code, save, and re-place in InDesign. The shapes themselves never need to be
touched — only those two colour values.

If you'd rather do it visually instead of editing code, [Photopea](https://www.photopea.com) is a
free, browser-based editor with an Illustrator-style interface: open the SVG there, select the
wordmark or dot, and use the fill colour picker — no software install required.

## Brand reference

- **Typeface:** Playfair Display, weight 500 (Medium) — Google Fonts, free & open licence (OFL)
- **Espresso Earth** `#3A2D28` — primary wordmark colour
- **Rose Gold** `#CBB1A5` — the full stop, always
- **Porcelain Ivory** `#FDFBF7` — reverse wordmark colour, on dark backgrounds
- **Deep Charcoal** `#2A201C` — monochrome black variant (never pure `#000000`, per brand spec)

See `../Nurture Typography + Colour Spec.dc.html` for the full palette and typography rules.
