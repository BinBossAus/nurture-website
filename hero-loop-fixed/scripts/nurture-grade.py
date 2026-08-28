#!/usr/bin/env python3
"""Nurture grade: espresso, porcelain, champagne, rose-gold blush. No orange/clay/cyan."""

from __future__ import annotations

import sys

import numpy as np
from PIL import Image

ESPRESSO = np.array([0x3A, 0x2D, 0x28], dtype=np.float32) / 255.0
ROSE = np.array([0xE5, 0xC1, 0xB3], dtype=np.float32) / 255.0
CHAMPAGNE = np.array([0xF0, 0xE6, 0xD4], dtype=np.float32) / 255.0
PORCELAIN = np.array([0xFA, 0xF7, 0xF2], dtype=np.float32) / 255.0


def luma(rgb: np.ndarray) -> np.ndarray:
    return rgb[..., 0] * 0.2126 + rgb[..., 1] * 0.7152 + rgb[..., 2] * 0.0722


def _scalar(rgb: np.ndarray) -> float:
    return float(np.asarray(luma(rgb.reshape(1, 1, 3))).reshape(-1)[0])


def grade(rgb: np.ndarray) -> np.ndarray:
    r = rgb[..., 0].astype(np.float32, copy=True)
    g = rgb[..., 1].astype(np.float32, copy=True)
    b = rgb[..., 2].astype(np.float32, copy=True)

    yellow = np.clip((r + g) * 0.5 - b, 0.0, 1.0)
    orange = np.clip(r - b, 0.0, 1.0) * np.clip(r - g * 0.72, 0.0, 1.0)
    rust = np.clip(r - g, 0.0, 1.0) * np.clip(g - b, 0.0, 1.0)

    # Strip orange / terracotta / rust / golden-yellow (not a light 35% trim)
    r = r - yellow * 0.62 - orange * 0.48 - rust * 0.32
    g = g - yellow * 0.48 - orange * 0.10 - rust * 0.08
    r = r - np.clip(r - g, 0.0, 1.0) * 0.40

    # Neutralize leftover yellow by lifting B only up to the new (R+G)/2 — never cyan
    remain = np.clip((r + g) * 0.5 - b, 0.0, 1.0)
    b = b + remain * 0.92
    b = np.minimum(b, (r + g) * 0.5 + 0.008)

    # Kill cyan/blue cast from any prior cool grade
    cyan = np.clip(b - r, 0.0, 1.0) * np.clip(b - g, 0.0, 1.0)
    b = b - cyan * 0.85
    g = g - cyan * 0.12

    rgb2 = np.clip(np.stack([r, g, b], axis=-1), 0.0, 1.0)
    r, g, b = rgb2[..., 0], rgb2[..., 1], rgb2[..., 2]

    # Foliage: muted natural green, no yellow-green, no blue-green
    yg = np.clip(g - b, 0.0, 1.0) * np.clip(1.0 - np.abs(r - g) * 2.4, 0.0, 1.0)
    green_dom = np.clip((g - np.maximum(r, b)) * 5.0, 0.0, 1.0)
    foliage = np.clip(np.maximum(yg * 0.9, green_dom), 0.0, 1.0)
    r = r - foliage * 0.11
    g = g - foliage * 0.02
    mean = (r + g + b) / 3.0
    desat = foliage * 0.22
    r = r * (1.0 - desat) + mean * desat
    g = g * (1.0 - desat * 0.45) + mean * desat * 0.45
    b = b * (1.0 - desat) + mean * desat
    # keep greens from going teal
    b = b - foliage * np.clip(b - r, 0.0, 1.0) * 0.35
    darken = 1.0 - foliage * 0.07
    r, g, b = r * darken, g * darken, b * darken

    rgb2 = np.clip(np.stack([r, g, b], axis=-1), 0.0, 1.0)
    y = luma(rgb2)

    # Shadows → Espresso (warm-neutral brown, not orange)
    shadow_w = np.clip(1.0 - y / 0.34, 0.0, 1.0) ** 1.1
    esp_y = _scalar(ESPRESSO)
    scaled_esp = ESPRESSO * (y / max(esp_y, 0.02))[..., None]
    mix = shadow_w * 0.40
    rgb2 = rgb2 * (1.0 - mix)[..., None] + scaled_esp * mix[..., None]

    r, g, b = rgb2[..., 0], rgb2[..., 1], rgb2[..., 2]
    y = luma(rgb2)
    mx = np.maximum(np.maximum(r, g), b)
    mn = np.minimum(np.minimum(r, g), b)
    sat = np.where(mx > 1e-4, (mx - mn) / np.maximum(mx, 1e-4), 0.0)

    # Porcelain / champagne in linen lights
    remain_y = np.clip((r + g) * 0.5 - b, 0.0, 1.0)
    linen = (
        np.clip((y - 0.40) / 0.30, 0.0, 1.0)
        * np.clip((0.42 - sat) / 0.42, 0.0, 1.0)
        * (1.0 - foliage)
    )
    porc_y = _scalar(PORCELAIN)
    champ_y = _scalar(CHAMPAGNE)
    porc = PORCELAIN * (y / max(porc_y, 0.02))[..., None]
    champ = CHAMPAGNE * (y / max(champ_y, 0.02))[..., None]
    linen_w = np.clip(linen * 0.62, 0.0, 1.0)
    target = porc * 0.7 + champ * 0.3
    rgb2 = rgb2 * (1.0 - linen_w)[..., None] + target * linen_w[..., None]

    # Delicate rose-gold reflected warmth (peach blush, never a solid orange)
    r, g, b = rgb2[..., 0], rgb2[..., 1], rgb2[..., 2]
    y = luma(rgb2)
    mid = np.clip(1.0 - np.abs(y - 0.52) / 0.28, 0.0, 1.0)
    blush = mid * (1.0 - foliage) * np.clip((y - 0.28) / 0.2, 0.0, 1.0) * 0.07
    rose_y = _scalar(ROSE)
    rose_scaled = ROSE * (y / max(rose_y, 0.02))[..., None]
    rgb2 = rgb2 * (1.0 - blush)[..., None] + rose_scaled * blush[..., None]

    # Compress golden glare into champagne, not gold
    r, g, b = rgb2[..., 0], rgb2[..., 1], rgb2[..., 2]
    y = r * 0.2126 + g * 0.7152 + b * 0.0722
    glare = np.clip((y - 0.70) / 0.22, 0.0, 1.0) * np.clip(
        ((r + g) * 0.5 - b) * 4.0, 0.0, 1.0
    )
    r = r - glare * 0.22
    g = g - glare * 0.16
    b = np.minimum(b + glare * 0.10, (r + g) * 0.5 + 0.02)
    y2 = r * 0.2126 + g * 0.7152 + b * 0.0722
    compress = np.clip((y2 - 0.78) / 0.22, 0.0, 1.0)
    r = r - compress * (y2 - 0.78) * 0.38
    g = g - compress * (y2 - 0.78) * 0.38
    b = b - compress * (y2 - 0.78) * 0.32

    rgb2 = np.clip(np.stack([r, g, b], axis=-1), 0.0, 1.0)

    # Final cyan gate
    r, g, b = rgb2[..., 0], rgb2[..., 1], rgb2[..., 2]
    cyan = np.clip(b - np.maximum(r, g), 0.0, 1.0)
    b = b - cyan * 0.9
    rgb2 = np.clip(np.stack([r, g, b], axis=-1), 0.0, 1.0)

    y = luma(rgb2)
    y_new = 0.03 + 0.94 * y
    y_new = 0.5 + (y_new - 0.5) * 1.04
    y_new = np.clip(y_new, 0.0, 1.0)
    scale = np.where(y > 1e-4, y_new / np.maximum(y, 1e-4), 1.0)
    return np.clip(rgb2 * scale[..., None], 0.0, 1.0)


def write_cube(path: str, size: int = 33) -> None:
    xs = np.linspace(0.0, 1.0, size, dtype=np.float32)
    rr, gg, bb = np.meshgrid(xs, xs, xs, indexing="ij")
    lattice = np.stack([rr, gg, bb], axis=-1)
    out = grade(lattice)
    lines = [
        'TITLE "Nurture Editorial Neutral"',
        f"LUT_3D_SIZE {size}",
        "DOMAIN_MIN 0.0 0.0 0.0",
        "DOMAIN_MAX 1.0 1.0 1.0",
    ]
    for ri in range(size):
        for gi in range(size):
            for bi in range(size):
                v = out[ri, gi, bi]
                lines.append(f"{v[0]:.6f} {v[1]:.6f} {v[2]:.6f}")
    with open(path, "w") as f:
        f.write("\n".join(lines) + "\n")


def grade_image(src: str, dest: str) -> None:
    im = Image.open(src).convert("RGB")
    arr = np.asarray(im).astype(np.float32) / 255.0
    out = (grade(arr) * 255.0).round().astype(np.uint8)
    Image.fromarray(out, "RGB").save(dest, quality=92, optimize=True)


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "help"
    if cmd == "cube":
        write_cube(sys.argv[2])
        print("wrote", sys.argv[2])
    elif cmd == "image":
        grade_image(sys.argv[2], sys.argv[3])
        print("graded", sys.argv[3])
    else:
        print("usage: nurture-grade.py cube <out.cube> | image <in> <out>")
