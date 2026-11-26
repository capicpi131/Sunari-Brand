"""Bajoy Beach Resto menu, edisi elegan SunaRi: 1 gambar vertikal 1080x1920 (header = mozaik sunset sampul WA).
Run: python3 resto/build_menu_sunari.py && node resto/render_sunari.js"""
import pathlib
H = pathlib.Path(__file__).parent
from PIL import Image, ImageEnhance
import numpy as np
def soft_grade(src, dst):
    """Color grading lembut tema SunaRi: warna dikurangi, hitam diangkat ke Driftwood, dipadu Shell Cream."""
    a = np.asarray(Image.open(src).convert("RGB"), float) / 255
    L = (0.299*a[..., 0] + 0.587*a[..., 1] + 0.114*a[..., 2])[..., None]
    a = a * np.array([1.03, 1.0, 0.93])                                   # hangat
    sh = np.clip((0.5-L)/0.5, 0, 1)
    a = a*(1-0.38*sh) + np.array([0xB0, 0x78, 0x5A])/255*0.38*sh          # bayangan -> Driftwood lembut
    a = 0.06 + np.clip(a, 0, 1)*0.88                                      # fade
    g = (a*[0.299, 0.587, 0.114]).sum(-1, keepdims=True)
    a = g + (a-g)*0.82                                                    # desaturasi
    a = a*0.84 + np.array([0xFB, 0xEC, 0xDC])/255*0.16                    # kabut Shell Cream
    Image.fromarray((np.clip(a, 0, 1)*255).astype(np.uint8)).save(dst, quality=95)
soft_grade(H.parent / "social/wa-cover/sampul-whatsapp-business.png", H / "menu-cover-soft.jpg")
ns = {}
src = (H / "build_menu.py").read_text()
exec(src[src.index("MENU = {"):src.index("FONTS =")], ns)
MENU, WA = ns["MENU"], "0821-8903-3044"

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ccc;font-family:Montserrat,sans-serif;color:#5A3E31;font-variant-numeric:lining-nums}
.pg{position:relative;width:1080px;height:1920px;overflow:hidden;background:#FBF4EC}
.pf{font-family:'Playfair Display',serif;font-weight:400} .it{font-style:italic}
.caps{font-weight:500;text-transform:uppercase;letter-spacing:.42em;color:#A67C64}
.hair{position:absolute;pointer-events:none;border:1.5px solid rgba(166,124,100,.5)}
.col{position:absolute;width:280px;top:822px}
.sec{margin-bottom:40px}
.sec h3{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:20px;font-family:'Playfair Display',serif;font-weight:400;font-style:italic;font-size:34px;color:#5A3E31}
.sec h3::before,.sec h3::after{content:"";flex:1;height:1.5px;background:#A67C64;opacity:.4}
.row{display:flex;align-items:baseline;font-family:'Playfair Display',serif;font-size:22px;font-weight:500;line-height:1.2;padding:7.6px 0}
.row .dots{flex:1;border-bottom:1.5px dotted rgba(166,124,100,.65);margin:0 9px;transform:translateY(-4px)}
.row .p{font-family:Montserrat,sans-serif;font-weight:600;font-size:18px;letter-spacing:.04em}
"""
EMB = """
.pg{background:#F3E8D8}
.paper{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 28%,rgba(255,255,255,.6),rgba(255,255,255,0) 62%),radial-gradient(ellipse at 50% 118%,rgba(90,62,49,.10),rgba(90,62,49,0) 60%)}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.55}
.pg>*:not(.paper):not(.grain){z-index:1}
.pf,.sec h3,.row>span:first-child{color:#4A3226;text-shadow:0 1.5px 0 rgba(255,255,255,.95),0 -1px 0 rgba(74,50,38,.22),1.5px 3px 3px rgba(74,50,38,.26)}
.caps{color:#7E5842;font-weight:600;text-shadow:0 1.5px 0 rgba(255,255,255,.9),1px 2px 1.5px rgba(74,50,38,.22)}
.gold,.it.gold,.row .p{background:linear-gradient(180deg,#F1D08E 0%,#C99643 45%,#8E6224 72%,#E5BD70 100%);-webkit-background-clip:text;background-clip:text;color:transparent !important;
  filter:drop-shadow(0 1.5px 0 rgba(255,255,255,.9)) drop-shadow(1px 2px 1.5px rgba(74,50,38,.35));text-shadow:none}
.sec h3::before,.sec h3::after{height:3px;background:none;border-top:1.5px solid rgba(126,88,66,.45);border-bottom:1.5px solid rgba(255,255,255,.95);opacity:1}
.row .dots{border-bottom:none;height:3px;background-image:radial-gradient(circle,rgba(126,88,66,.6) 1.3px,transparent 1.7px);background-size:8px 3px;box-shadow:0 1.5px 0 rgba(255,255,255,.7)}
.hair{border:none !important;box-shadow:inset 1.5px 1.5px 0 rgba(74,50,38,.28),inset -1.5px -1.5px 0 rgba(255,255,255,.95),1.5px 1.5px 0 rgba(255,255,255,.9),-1.5px -1.5px 0 rgba(74,50,38,.14)}
.photo{box-shadow:inset 0 0 0 1px rgba(255,255,255,.5),0 0 0 6px #F7EEE0,0 0 0 7.5px rgba(74,50,38,.28),0 0 0 9px rgba(255,255,255,.95),3px 5px 14px rgba(74,50,38,.28)}
.sunacc{filter:drop-shadow(0 1.5px 0 rgba(255,255,255,.9)) drop-shadow(1px 2px 2px rgba(74,50,38,.32))}
.rule{background:none !important;height:3px !important;border-top:1.5px solid rgba(126,88,66,.45);border-bottom:1.5px solid rgba(255,255,255,.95);opacity:1 !important}
"""
GRAIN = '<svg class="grain" width="100%" height="100%"><filter id="gr"><feTurbulence type="fractalNoise" baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .35  0 0 0 0 .24  0 0 0 0 .18  0 0 0 .09 0"/></filter><rect width="100%" height="100%" filter="url(#gr)"/></svg>'

def section(name, items):
    rows = "".join(f'<div class="row"><span>{n}</span><span class="dots"></span><span class="p">{p}</span></div>' for n, p in items)
    return f'<div class="sec"><h3>{name}</h3>{rows}</div>'

gaps = "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)])
SUN = f'''<svg class="sunacc" viewBox="0 0 200 200" width="30" height="30"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="m"><rect width="200" height="200" fill="white"/>{gaps}</mask></defs><circle cx="100" cy="100" r="96" fill="url(#g)" mask="url(#m)"/></svg>'''

c1 = section("Makanan", MENU["Makanan"])
c2 = section("Snack", MENU["Snack"]) + section("Drinks", MENU["Drinks"])
c3 = section("Juice", MENU["Juice"]) + section("Soft Drink", MENU["Soft Drink"])
COVER = "menu-cover-soft.jpg"
page = f'''<div class="pg" id="menu-sunari"><div class="paper"></div>{GRAIN}
  <div class="hair" style="inset:34px"></div><div class="hair" style="inset:44px;opacity:.55"></div>
  <div style="position:absolute;left:96px;right:96px;top:104px;height:470px;background:url('{COVER}') 50% 44%/cover" class="photo"></div>
  
  <div style="position:absolute;left:0;right:0;top:632px;text-align:center">
    <div class="pf" style="font-size:78px;line-height:1">Bajoy Beach <span class="it gold">Resto</span></div>
    <div style="display:flex;align-items:center;justify-content:center;gap:22px;margin-top:22px">
      <div style="width:110px" class="rule" data-x="1"></div>{SUN}<div style="width:110px" class="rule" data-x="1"></div></div>
    <div class="caps" style="font-size:16px;margin-top:22px;margin-right:-.42em">Menu · Resto &amp; Bar</div>
  </div>
  <div class="col" style="left:96px">{c1}</div>
  <div class="col" style="left:400px">{c2}</div>
  <div class="col" style="right:96px">{c3}</div>
  <div style="position:absolute;left:96px;right:96px;bottom:118px;text-align:center;padding-top:22px"><div class="rule" style="position:absolute;left:0;right:0;top:0"></div>
    <div class="pf it" style="font-size:25px;font-weight:500">Tamu menginap 07.00 – 21.00 &nbsp;·&nbsp; Tamu tidak menginap 07.00 – 19.00</div></div>
  <div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:13px;font-weight:600;letter-spacing:.18em;text-transform:uppercase;color:#7E5842;text-shadow:0 1px 0 rgba(255,255,255,.9)">
    Harga dalam ribuan rupiah (45 = Rp 45.000) · Senja Dinner pesan H-1 · WA {WA}</div>
</div>'''
(H / "menu-sunari.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}{EMB}@page{{size:1080px 1920px;margin:0}}@media print{{body{{background:none}}}}</style></head><body>{page}</body></html>')
print("ok")
