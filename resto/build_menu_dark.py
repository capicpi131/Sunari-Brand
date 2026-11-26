"""Bajoy Beach Resto menu, edisi gelap ala 'Menu' script (tema SunaRi): A4 print.
Run: python3 resto/build_menu_dark.py && node resto/render_dark.js"""
import pathlib, re
H = pathlib.Path(__file__).parent
# ambil data menu dari build_menu.py agar satu sumber
src = (H / "build_menu.py").read_text()
ns = {}
exec(src[src.index("MENU = {"):src.index("FONTS =")], ns)
MENU, WA = ns["MENU"], "0821-8903-3044"

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Mrs+Saint+Delafield&family=Montserrat:wght@300;400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#222;font-variant-numeric:lining-nums;font-family:Montserrat,sans-serif;color:#FBF4EC}
.pg{position:relative;width:794px;height:1123px;overflow:hidden;
 background:radial-gradient(ellipse at 70% 35%,#6A4A3B 0%,#5A3E31 45%,#46302566 100%),#5A3E31}
.script{font-family:'Mrs Saint Delafield',cursive;font-weight:400;color:#FBF4EC;line-height:1}
.caps{font-weight:700;text-transform:uppercase;letter-spacing:.42em;color:#FBF4EC}
.col{position:absolute;top:372px;width:200px;text-align:right}
.sec{margin-bottom:34px}
.sec h3{font-weight:700;font-size:11.5px;letter-spacing:.42em;margin-right:-.42em;text-transform:uppercase;color:#FBF4EC;margin-bottom:14px}
.row{display:flex;justify-content:space-between;align-items:baseline;font-weight:300;font-size:12.6px;line-height:1;padding:4.4px 0;color:#FBF4EC}
.row .p{font-weight:600;color:#FDB15D;margin-left:12px}
"""
def section(name, items):
    rows = "".join(f'<div class="row"><span>{n}</span><span class="p">{p}K</span></div>' for n, p in items)
    return f'<div class="sec"><h3>{name}</h3>{rows}</div>'

c1 = section("Makanan", MENU["Makanan"]) + section("Snack", MENU["Snack"]) + section("Soft Drink", MENU["Soft Drink"])
c2 = section("Drinks", MENU["Drinks"]) + section("Juice", MENU["Juice"])

sun = '''<svg viewBox="0 0 200 200" width="22" height="22"><defs><linearGradient id="sg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="sm"><rect width="200" height="200" fill="white"/>''' + "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)]) + '''</mask></defs><circle cx="100" cy="100" r="96" fill="url(#sg)" mask="url(#sm)"/></svg>'''

page = f'''<div class="pg" id="menu-dark">
  <div class="script" style="position:absolute;left:40px;top:34px;font-size:290px;letter-spacing:-.01em">Menu</div>
  <img src="../assets/logo-sunari-color-dark.png" style="position:absolute;right:56px;top:62px;width:190px">
  <div style="position:absolute;left:84px;top:336px;width:2px;height:240px;background:#FBF4EC"></div>

  <div style="position:absolute;right:56px;top:196px;text-align:right">
    <div class="caps" style="font-size:11.5px;margin-right:-.42em">Jam Buka</div>
    <div style="font-weight:300;font-size:12.6px;margin-top:14px;line-height:1.9">Tamu menginap &nbsp;<b style="font-weight:600;color:#FDB15D">07.00 – 21.00</b><br>Tamu tidak menginap &nbsp;<b style="font-weight:600;color:#FDB15D">07.00 – 19.00</b></div>
  </div>

  <div class="col" style="right:300px">{c1}</div>
  <div class="col" style="right:56px">{c2}</div>

  <div style="position:absolute;left:76px;bottom:70px;transform-origin:left bottom;transform:rotate(-90deg) translateY(100%);white-space:nowrap;display:flex;align-items:center;gap:26px">
    <span class="caps" style="font-size:13.5px">Bajoy Beach Resto</span>
    <span class="script" style="font-size:58px;margin-top:-2px">SunaRi</span>
  </div>
  <div style="position:absolute;left:56px;bottom:20px">{sun}</div>

  <div style="position:absolute;right:56px;bottom:34px;text-align:right;font-weight:400;font-size:8.5px;letter-spacing:.22em;text-transform:uppercase;line-height:1.9;color:#E6C89B">
    Harga dalam ribu rupiah (K = 1.000)<br>Senja Dinner · pesan H-1 · WA {WA}</div>
</div>'''
(H / "menu-dark.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:210mm 297mm;margin:0}}</style></head><body>{page}</body></html>')
print("ok")
