#!/usr/bin/env python3
"""Draw the news-image-20261120 entry: a newspaper front page summing up
Friday 20 November 2026. Writes entry.png (1024x1024) next to this script.

Every story below was verified against real reporting of 20 November 2026
(One Turn day page, CNN, Morningstar/Dow Jones, Sensor Tower via VGC/
Notebookcheck, BBC via One Turn). No facts invented.
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (248, 244, 233)
INK = (26, 26, 26)
NAVY = (31, 51, 80)
RED = (176, 42, 30)
GREY = (96, 96, 92)
CARD = (255, 255, 255)
LINE = (180, 175, 160)

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def wrap(draw, text, fnt, width):
    """Greedy word wrap; returns list of lines that fit `width`."""
    lines, cur = [], ""
    for word in text.split(" "):
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_lines(draw, lines, x, y, fnt, fill, spacing=1.18):
    for line in lines:
        draw.text((x, y), line, font=fnt, fill=fill)
        y += int(fnt.size * spacing)
    return y


def explosion(draw, cx, cy, r, core=(255, 176, 66), mid=(232, 110, 30), edge=(176, 42, 30)):
    for i, (col, rr) in enumerate([(edge, r), (mid, r * 0.68), (core, r * 0.38)]):
        pts = []
        n = 9
        for k in range(n * 2):
            ang = math.pi * k / n
            rad = rr * (1.0 if k % 2 == 0 else 0.55)
            pts.append((cx + rad * math.cos(ang), cy + rad * math.sin(ang)))
        draw.polygon(pts, fill=col)


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    M = 28  # margin
    right = W - M

    # ---- Masthead ----
    f_mast = font(SERIF, 62)
    title = "THE WORLD IN ONE DAY"
    tw = d.textlength(title, font=f_mast)
    d.text(((W - tw) / 2, 22), title, font=f_mast, fill=INK)
    d.line([(M, 100), (right, 100)], fill=INK, width=3)
    d.line([(M, 106), (right, 106)], fill=INK, width=1)

    # ---- Date band (the day, named loud and clear) ----
    d.rectangle([M, 114, right, 156], fill=NAVY)
    f_date = font(SANS_B, 30)
    date = "FRIDAY  •  20 NOVEMBER 2026"
    tw = d.textlength(date, font=f_date)
    d.text(((W - tw) / 2, 120), date, font=f_date, fill=(255, 255, 255))
    f_sub = font(SANS, 17)
    sub = "The day's world news, in one image"
    tw = d.textlength(sub, font=f_sub)
    d.text(((W - tw) / 2, 163), sub, font=f_sub, fill=GREY)

    # ---- Lead story: Russia's overnight attack on Ukraine ----
    lead_y = 196
    lead_h = 224
    lead_w = 600
    d.line([(M, lead_y), (M + lead_w, lead_y)], fill=RED, width=4)
    f_kick = font(SANS_B, 19)
    d.text((M, lead_y + 12), "UKRAINE  —  OVERNIGHT INTO FRIDAY", font=f_kick, fill=RED)
    f_head = font(SERIF, 40)
    head = wrap(d, "Russia's biggest air assault of the war", f_head, lead_w)
    y = draw_lines(d, head, M, lead_y + 42, f_head, INK, 1.08)
    f_body = font(SANS, 20)
    body = wrap(
        d,
        "110+ missiles and 400 drones hit cities across Ukraine; "
        "8 killed, 28 hurt, Kyiv bridges damaged. Poland scrambled "
        "jets as objects crossed its airspace.",
        f_body, lead_w)
    draw_lines(d, body, M, y + 8, f_body, INK, 1.28)

    # Lead illustration: night sky over a city, missile trails, bursts
    ix0, iy0, ix1, iy1 = M + lead_w + 18, lead_y, right, lead_y + lead_h
    sky = Image.new("RGB", (ix1 - ix0, iy1 - iy0), (16, 24, 46))
    sd = ImageDraw.Draw(sky)
    for i in range(iy1 - iy0):
        t = i / (iy1 - iy0)
        sd.line([(0, i), (ix1 - ix0, i)],
                fill=(int(16 + 30 * t), int(24 + 34 * t), int(46 + 46 * t)))
    # stars
    for sx, sy in [(30, 18), (90, 40), (150, 12), (210, 34), (260, 20),
                   (320, 44), (60, 60), (180, 58), (300, 66), (120, 26)]:
        sd.ellipse([sx - 1, sy - 1, sx + 1, sy + 1], fill=(220, 220, 200))
    # missile trails
    sd.line([(40, 150), (150, 40)], fill=(255, 200, 120), width=3)
    sd.line([(330, 170), (250, 60)], fill=(255, 200, 120), width=3)
    sd.line([(200, 190), (190, 90)], fill=(255, 220, 150), width=2)
    img.paste(sky, (ix0, iy0))
    # skyline silhouette
    base = iy1
    for bx, bw, bh in [(0, 46, 62), (46, 34, 88), (80, 52, 54), (132, 30, 96),
                       (162, 48, 70), (210, 36, 110), (246, 54, 60), (300, 40, 84)]:
        d.rectangle([ix0 + bx, base - bh, ix0 + bx + bw, base], fill=(8, 10, 22))
    # lit windows
    for wx, wy in [(10, base - 40), (56, base - 60), (92, base - 30), (140, base - 70),
                   (176, base - 44), (222, base - 80), (258, base - 36), (312, base - 58)]:
        d.rectangle([ix0 + wx, wy, ix0 + wx + 5, wy + 7], fill=(255, 200, 90))
    # explosions over the city
    explosion(d, ix0 + 120, base - 108, 26)
    explosion(d, ix0 + 268, base - 128, 20)
    d.rectangle([ix0, iy0, ix1, iy1], outline=INK, width=2)

    # ---- Story grid: 2 columns x 3 rows ----
    cards = [
        ("JUSTICE  ·  THE HAGUE", RED,
         "World court: Myanmar committed genocide",
         "ICJ rules 9–6, a first against a state; 1.3 million Rohingya still displaced."),
        ("SUMMIT  ·  SHENZHEN", NAVY,
         "Trump, Xi and Putin meet — first three-way summit",
         "Joint peace declaration, but no breakthrough on Ukraine or arms."),
        ("MARKETS  ·  TOKYO & NEW YORK", (120, 60, 10),
         "AI sell-off deepens worldwide",
         "Nikkei −4.8%, SoftBank −16%; S&P 500 falls for a fifth straight day."),
        ("TECH  ·  NEW YORK", (20, 90, 90),
         "Anthropic's Nasdaq debut jumps 17%",
         "Shares close near $97 on an $83 IPO price; a record $81.3bn listing."),
        ("CULTURE  ·  WORLDWIDE", (90, 30, 110),
         "GTA VI: biggest launch in history",
         "Est. $2.36bn in a day, about 24.6m copies — Sensor Tower estimates."),
        ("SPACE  ·  DEEP SPACE", (40, 60, 40),
         "Voyager 1 passes one light-day from Earth",
         "26bn km out, 49 years after launch; BepiColombo enters Mercury orbit."),
    ]
    gx, gy = M, 440
    cw = (right - M - 16) // 2
    ch, gap = 138, 16
    f_ck = font(SANS_B, 16)
    f_ch = font(SANS_B, 23)
    f_cb = font(SANS, 17)
    for i, (kick, col, head, body) in enumerate(cards):
        cx = gx + (i % 2) * (cw + gap)
        cy = gy + (i // 2) * (ch + 14)
        d.rectangle([cx, cy, cx + cw, cy + ch], fill=CARD, outline=LINE, width=1)
        d.rectangle([cx, cy, cx + cw, cy + 5], fill=col)
        d.text((cx + 14, cy + 14), kick, font=f_ck, fill=col)
        hl = wrap(d, head, f_ch, cw - 28)
        y = draw_lines(d, hl, cx + 14, cy + 38, f_ch, INK, 1.08)
        bl = wrap(d, body, f_cb, cw - 28)
        draw_lines(d, bl, cx + 14, y + 4, f_cb, (60, 60, 60), 1.22)

    # ---- Also on 20 November strip ----
    ty = gy + 3 * ch + 2 * 14 + 16
    d.line([(M, ty), (right, ty)], fill=INK, width=2)
    f_tk = font(SANS_B, 17)
    d.text((M, ty + 10), "ALSO ON 20 NOVEMBER", font=f_tk, fill=RED)
    f_tt = font(SANS, 18)
    tick = wrap(
        d,
        "North Korea fires a ballistic missile  •  Italy strike over living costs  •  "
        "Youth strike in 25+ countries  •  COP31 draft drops fossil-fuel phase-out  •  "
        "Trump pardons Pete Rose  •  Houthi missile damages Riyadh tower",
        f_tt, right - M)
    draw_lines(d, tick, M, ty + 36, f_tt, INK, 1.3)

    # ---- Footer ----
    d.line([(M, H - 44), (right, H - 44)], fill=LINE, width=1)
    f_ft = font(SANS, 14)
    foot = "Events of Friday 20 November 2026  •  Sources: CNN, BBC, Reuters, AP, Morningstar, Sensor Tower"
    tw = d.textlength(foot, font=f_ft)
    d.text(((W - tw) / 2, H - 34), foot, font=f_ft, fill=GREY)

    img.save("entry.png", optimize=True)
    print("wrote entry.png")


if __name__ == "__main__":
    main()
