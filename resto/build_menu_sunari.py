"""Bajoy Beach Resto menu A4, gaya brand SunaRi (foto penuh + latar Shell Cream).
Run: python3 resto/build_menu_sunari.py && node resto/render_sunari.js"""
import pathlib
H = pathlib.Path(__file__).parent
ns = {}
src = (H / "build_menu.py").read_text()
exec(src[src.index("MENU = {"):src.index("FONTS =")], ns)
MENU, WA = ns["MENU"], "0821-8903-3044"

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ddd;font-family:Montserrat,sans-serif;color:#5A3E31;font-variant-numeric:lining-nums}
.pg{position:relative;width:794px;height:1123px;overflow:hidden;background:#FBF4EC}
.pf{font-family:'Playfair Display',serif;font-weight:400}
.it{font-style:italic}
.caps{font-weight:500;text-transform:uppercase;letter-spacing:.4em;color:#A67C64}
.col{position:absolute;top:372px;width:322px}
.sec{margin-bottom:20px}
.sec h3{font-family:'Playfair Display',serif;font-weight:400;font-size:23px;display:flex;align-items:center;gap:14px;margin-bottom:6px}
.sec h3::after{content:"";flex:1;height:1px;background:#A67C64;opacity:.45}
.row{display:flex;align-items:baseline;font-size:12.4px;line-height:1.2;padding:2.6px 0}
.row .dots{flex:1;border-bottom:1.5px dotted rgba(166,124,100,.6);margin:0 8px;transform:translateY(-3px)}
.row .p{font-weight:600}
"""
def section(name, items):
    rows = "".join(f'<div class="row"><span>{n}</span><span class="dots"></span><span class="p">{p}K</span></div>' for n, p in items)
    return f'<div class="sec"><h3>{name}</h3>{rows}</div>'

c1 = section("Makanan", MENU["Makanan"]) + section("Snack", MENU["Snack"]) + section("Soft Drink", MENU["Soft Drink"])
c2 = section("Drinks", MENU["Drinks"]) + section("Juice", MENU["Juice"])

def sun(size):
    gaps = "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)])
    return f'''<svg viewBox="0 0 200 200" width="{size}" height="{size}"><defs><linearGradient id="sg" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="sm"><rect width="200" height="200" fill="white"/>{gaps}</mask></defs><circle cx="100" cy="100" r="96" fill="url(#sg)" mask="url(#sm)"/></svg>'''

PHOTO = "../assets/photos/graded/senja__59-makan-senja-payung-1810.jpg"
page = f'''<div class="pg" id="menu-sunari">
  <div style="position:absolute;left:0;right:0;top:0;height:282px;background:url('{PHOTO}') 50% 36%/cover"></div>
  <div style="position:absolute;left:0;right:0;top:0;height:282px;background:linear-gradient(180deg,rgba(60,40,30,.38) 0%,rgba(60,40,30,0) 38%,rgba(60,40,30,0) 55%,rgba(60,40,30,.5) 100%)"></div>
  <img src="../assets/logo-sunari-cream.png" style="position:absolute;left:50%;top:30px;width:230px;transform:translateX(-50%)">
  <div style="position:absolute;left:56px;bottom:auto;top:184px;color:#FBF4EC;text-shadow:0 1px 8px rgba(60,40,30,.45)">
    <div style="font-size:10.5px;font-weight:500;letter-spacing:.4em;text-transform:uppercase;margin-bottom:8px">Menu · Resto &amp; Bar</div>
    <div class="pf" style="font-size:46px;line-height:1">Bajoy Beach <span class="it">Resto</span></div></div>
  <div style="position:absolute;left:50%;top:282px;transform:translate(-50%,-50%);background:#FBF4EC;border-radius:50%;width:54px;height:54px;display:flex;align-items:center;justify-content:center">{sun(36)}</div>

  <div class="col" style="left:56px;top:336px">{c1}</div>
  <div class="col" style="right:56px;top:336px">{c2}</div>

  <div style="position:absolute;left:56px;right:56px;top:960px;height:82px;background:#E6C89B;display:flex;align-items:center;padding:0 30px;gap:30px">
    <div style="flex:1"><div class="caps" style="color:#5A3E31;font-size:8.5px">Tamu menginap</div><div class="pf" style="font-size:24px;margin-top:5px">07.00 – 21.00</div></div>
    <div style="width:1px;height:46px;background:#5A3E31;opacity:.35"></div>
    <div style="flex:1.15"><div class="caps" style="color:#5A3E31;font-size:8.5px;white-space:nowrap;letter-spacing:.32em">Tamu tidak menginap</div><div class="pf" style="font-size:24px;margin-top:5px">07.00 – 19.00</div></div>
    <div style="width:1px;height:46px;background:#5A3E31;opacity:.35"></div>
    <div style="flex:1.1"><div class="caps" style="color:#5A3E31;font-size:8.5px">Senja Dinner</div><div class="pf it" style="font-size:17px;margin-top:6px;line-height:1.2">Pesan H-1 via<br>WhatsApp</div></div>
  </div>
  <div style="position:absolute;left:56px;right:56px;bottom:40px;display:flex;justify-content:space-between;font-size:9px;letter-spacing:.22em;text-transform:uppercase;color:#A67C64">
    <span>SunaRi · Selayar</span><span>Harga dalam ribu rupiah (K = 1.000) · WA {WA}</span></div>
</div>'''
(H / "menu-sunari.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:210mm 297mm;margin:0}}</style></head><body>{page}</body></html>')
print("ok")
