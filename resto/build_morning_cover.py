"""Mozaik 'Foto Pagi' (11 x 3 = 33 foto siang/pagi resort + logo di tengah) -> resto/menu-cover-morning-3row.png
Run: python3 resto/build_morning_cover.py"""
import numpy as np, pathlib
from PIL import Image, ImageOps, ImageFilter
H = pathlib.Path(__file__).parent; P = H.parent / "assets/photos"
PICK = ["pantai/02-", "pantai/03-", "pantai/04-", "taman/03-", "taman/05-", "taman/06-", "taman/07-", "taman/08-", "taman/09-", "taman/10-", "taman/11-", "taman/12-",
        "vip-standard-bungalow/01-", "vip-standard-bungalow/02-", "vip-standard-bungalow/04-", "vip-standard-bungalow/03-", "standard-bungalow/01-",
        "superior-bungalow/01-", "superior-bungalow/02-", "superior-bungalow/03-", "superior-bungalow/04-", "superior-bungalow/05-",
        "vip-superior-bungalow/01-", "vip-superior-bungalow/02-", "vip-superior-bungalow/10-", "vip-superior-bungalow/06-", "vip-superior-bungalow/03-", "vip-superior-bungalow/05-",
        "family-superior-bungalow/01-", "family-superior-bungalow/02-", "family-superior-bungalow/03-", "family-superior-bungalow/04-", "family-superior-bungalow/05-"]
COLS, ROWS, W, Hh, PAD, GAP = 11, 3, 2424, 822, 4, 4
tw = (W - 2*PAD - (COLS-1)*GAP) / COLS; th = (Hh - 2*PAD - (ROWS-1)*GAP) / ROWS
items = []
for k in PICK:
    f = sorted((P / k.split("/")[0]).glob(k.split("/")[1] + "*.jpg"))[0]
    im = ImageOps.exif_transpose(Image.open(f)).convert("RGB")
    sm = im.copy(); sm.thumbnail((200, 200)); lum = float(np.asarray(sm.convert("L")).mean())
    items.append((f.name, im, lum))
assert len(items) == COLS * ROWS
items.sort(key=lambda t: -t[2])                                          # terang di kiri atas -> lebih gelap di kanan bawah
cells = sorted([(r, c) for r in range(ROWS) for c in range(COLS)], key=lambda rc: (rc[0] + rc[1], rc[0]))
canvas = Image.new("RGB", (W, Hh), (0xFB, 0xF4, 0xEC))
for (n, im, _), (r, c) in zip(items, cells):
    t = ImageOps.fit(im, (round(tw), round(th)), Image.LANCZOS, centering=(0.5, 0.5))
    canvas.paste(t, (round(PAD + c*(tw+GAP)), round(PAD + r*(th+GAP))))
logo = Image.open(H.parent / "assets/logo-sunari-sunset-halo.png").convert("RGBA")
lw = 1200; logo = logo.resize((lw, round(logo.height * lw / logo.width)), Image.LANCZOS)
canvas.paste(logo, ((W - lw)//2, (Hh - logo.height)//2), logo)
canvas.save(H / "menu-cover-morning-3row.png"); print("ok", [i[0] for i in items][:3], logo.size)
