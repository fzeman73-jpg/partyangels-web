#!/usr/bin/env python3
"""Vygeneruje responzivní varianty obrázků z _source/ do assets/img/."""
from PIL import Image
from pathlib import Path

SRC = Path(__file__).resolve().parent.parent / "_source"
OUT = Path(__file__).resolve().parent.parent / "assets" / "img"
OUT.mkdir(parents=True, exist_ok=True)

JOBS = [
    ("hero",     "hero.webp",        [450, 700, 1200], False),
    ("iva",      "iva.jpeg",         [450, 700, 1200], False),
    ("vanda",    "vanda.jpeg",       [450, 700, 1200], False),
    ("logo",     "logo-header.webp", [260, 450],       True),
    ("logo-big", "logo-header.webp", [450, 700, 1200], True),
]

for name, src, widths, alpha in JOBS:
    im = Image.open(SRC / src)
    for w in widths:
        h = round(im.height * w / im.width)
        r = im.resize((w, h), Image.LANCZOS)
        r.save(OUT / f"{name}-{w}.webp", "WEBP", quality=85, method=6)
        if alpha:
            r.save(OUT / f"{name}-{w}.png", "PNG", optimize=True)
        else:
            r.convert("RGB").save(OUT / f"{name}-{w}.jpg", "JPEG",
                                  quality=84, optimize=True, progressive=True)
    print(f"{name}: {im.size} -> {widths}")
