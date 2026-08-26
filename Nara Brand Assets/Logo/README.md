# Nara logo — master files

The "Nara." wordmark, built exactly like the Nurture one: Playfair Display, Medium (500),
outlined to vector paths (not live text), with the full stop carried in Rose Gold.

## Files

| File | Wordmark colour | Full stop colour | Use on |
|---|---|---|---|
| `nara-logo-primary.svg` | Espresso Earth `#3A2D28` | Rose Gold `#CBB1A5` | Light / ivory backgrounds (default logo) |
| `nara-logo-reverse.svg` | Porcelain Ivory `#FDFBF7` | Rose Gold `#CBB1A5` | Dark / espresso backgrounds |
| `nara-logo-mono-black.svg` | Deep Charcoal `#2A201C` | Deep Charcoal `#2A201C` | Single-colour print: engraving, stamps, foil |
| `nara-logo-mono-white.svg` | Porcelain Ivory `#FDFBF7` | Porcelain Ivory `#FDFBF7` | Single-colour knockout on dark/photo backgrounds |

## Opening in InDesign

Same as the Nurture logo: **File → Place** (`Cmd/Ctrl + D`), drag to size holding **Shift** to
keep proportions. Vector paths mean no quality loss at any size.

## Changing the colour yourself

Open the `.svg` in a plain text editor and edit the two `fill="#..."` values:

```
<g id="Wordmark" fill="#3A2D28">      ← the word "Nara"
<g id="Full-Stop" fill="#CBB1A5">     ← the "." only
```

See `../../Nurture Parenting Magazine rebrand/Brand Assets/Logo/README.md` for the full
background on this approach (identical process, just a different word).
