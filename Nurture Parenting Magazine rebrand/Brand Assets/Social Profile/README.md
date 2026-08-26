# Nurture social profile picture — final set

The "Ring Seal" mark: Espresso Earth tile, hairline Porcelain Ivory ring, centered "N", Rose
Gold jewel dot. Chosen for profile pictures specifically because it was tested against a
circular crop (see below) — Instagram, Facebook, LinkedIn and X all crop profile photos into
a circle, and the ring gives it a bit more presence than the plain favicon mark at the larger
size a profile picture is actually viewed at.

## Files

| File | Size | Use |
|---|---|---|
| `nurture-social-profile-1024.png` | 1024×1024 | Upload this one everywhere — every platform downsizes from a high-res square on its own |
| `nurture-social-profile-512.png` | 512×512 | Smaller fallback, same image |
| `nurture-social-profile-320.png` | 320×320 | Minimum-size fallback (Instagram's own minimum) |
| `nurture-social-profile-master.svg` | vector | Source file — outlined paths, edit colours from here if this ever changes |

## Where to use it

Upload the **1024px PNG** as your profile photo on:

- Instagram, Facebook Page, LinkedIn Page, X (Twitter), Pinterest, YouTube, TikTok

You don't need a different crop or size per platform — they all take one square image and
scale/crop it themselves. Just re-upload the same 1024px file everywhere so it always reads
crisply, even on retina phone screens.

## Why the ring survives the circle crop

Every element (the ring, the "N", the jewel dot) sits with margin inside the square, so when
a platform crops it to a circle nothing gets clipped — verified by rendering it inside an
actual circular mask before finalizing. If you ever resize or edit this mark, keep everything
inside roughly the middle 80% of the square to preserve that safety margin.

## Recolouring / resizing yourself

Open `nurture-social-profile-master.svg` in a text editor and change the `fill="#..."` /
`stroke="#..."` hex values (ring, "N", jewel dot). Re-export a PNG at whatever size you need —
vector source means no quality loss at any size.
