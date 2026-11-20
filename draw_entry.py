#!/usr/bin/env python3
"""Draw the 20 November 2026 world-news infographic (1024x1024)."""
from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), (15, 23, 42))
d = ImageDraw.Draw(img)

# Header band
d.rectangle([0, 0, W, 120], fill=(30, 58, 95))
d.rectangle([0, 120, W, 126], fill=(245, 197, 66))
d.text((512, 28), "FRIDAY 20 NOVEMBER 2026", font=font(BOLD, 46), fill=(255, 255, 255), anchor="ma")
d.text((512, 82), "WORLD NEWS IN ONE IMAGE", font=font(REG, 22), fill=(191, 219, 254), anchor="ma")

stories = [
    ("DIPLOMACY", "SHENZHEN", "TRUMP - XI - PUTIN SUMMIT", "First trilateral talks: nukes, Iran, Ukraine", (59, 130, 246)),
    ("MARKETS", "NASDAQ", "ANTHROPIC RECORD IPO", "$81.3B raised, shares +17% on debut", (16, 185, 129)),
    ("JUSTICE", "THE HAGUE", "ICJ: MYANMAR GENOCIDE", "Court finds genocide vs Rohingya", (168, 85, 247)),
    ("CONFLICT", "RIYADH", "HOUTHI HITS PIF TOWER", "Missile damages tallest tower, no injuries", (239, 68, 68)),
    ("CLIMATE", "INDIA", "CYCLONE AKVAN LANDFALL", "Odisha coast noon, 72,000 evacuated", (245, 158, 11)),
    ("WAR", "KYIV", "BALLISTIC MISSILES HIT KYIV", "4 missiles; blast near Dutch embassy", (236, 72, 153)),
]

def draw_icon(d, cx, cy, idx, color):
    # simple pictograms per story
    if idx == 0:  # three flags / handshake: three circles
        for k, dx in enumerate((-28, 0, 28)):
            d.ellipse([cx+dx-16, cy-16, cx+dx+16, cy+16], outline=color, width=4)
        d.line([cx-28, cy, cx+28, cy], fill=color, width=4)
    elif idx == 1:  # rising chart
        d.line([cx-32, cy+22, cx-32, cy-24], fill=color, width=4)
        d.line([cx-32, cy+22, cx+32, cy+22], fill=color, width=4)
        d.line([cx-26, cy+14, cx-8, cy-2, cx+8, cy+6, cx+26, cy-18], fill=color, width=5)
        d.polygon([(cx+26, cy-18), (cx+14, cy-16), (cx+24, cy-6)], fill=color)
    elif idx == 2:  # scales of justice
        d.line([cx, cy-26, cx, cy+20], fill=color, width=4)
        d.line([cx-28, cy-16, cx+28, cy-16], fill=color, width=4)
        d.polygon([(cx-28, cy-16), (cx-38, cy+6), (cx-18, cy+6)], outline=color)
        d.polygon([(cx+28, cy-16), (cx+18, cy+6), (cx+38, cy+6)], outline=color)
        d.line([cx-16, cy+24, cx+16, cy+24], fill=color, width=5)
    elif idx == 3:  # tower
        d.rectangle([cx-14, cy-28, cx+14, cy+26], outline=color, width=4)
        for r in range(4):
            for c in range(3):
                d.rectangle([cx-9+c*7, cy-20+r*11, cx-5+c*7, cy-13+r*11], fill=color)
        d.line([cx+30, cy-24, cx+16, cy-10], fill=(255, 220, 100), width=4)
    elif idx == 4:  # cyclone spiral
        for r in (26, 18, 10):
            d.arc([cx-r, cy-r, cx+r, cy+r], start=20, end=300, fill=color, width=5)
        d.ellipse([cx-4, cy-4, cx+4, cy+4], fill=color)
    else:  # missile / explosion star
        d.polygon([(cx, cy-28), (cx+7, cy-8), (cx+26, cy-8), (cx+12, cy+4),
                   (cx+18, cy+24), (cx, cy+12), (cx-18, cy+24), (cx-12, cy+4),
                   (cx-26, cy-8), (cx-7, cy-8)], outline=color, width=4)

top = 140
panel_h = 132
gap = 10
for i, (cat, place, head, detail, color) in enumerate(stories):
    y0 = top + i * (panel_h + gap)
    y1 = y0 + panel_h
    d.rounded_rectangle([24, y0, W-24, y1], radius=14, fill=(30, 41, 59), outline=color, width=3)
    d.rounded_rectangle([24, y0, 36, y1], radius=6, fill=color)
    draw_icon(d, 110, (y0+y1)//2, i, color)
    d.text((190, y0+12), cat + "  -  " + place, font=font(BOLD, 19), fill=color)
    d.text((190, y0+38), head, font=font(BOLD, 33), fill=(255, 255, 255))
    d.text((190, y0+84), detail, font=font(REG, 24), fill=(203, 213, 225))

d.text((512, H-34), "Sources: Reuters, AFP, Le Monde, WSJ, IMD, NASA - 20 Nov 2026",
       font=font(REG, 17), fill=(148, 163, 184), anchor="ma")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
