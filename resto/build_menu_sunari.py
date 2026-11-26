"""Bajoy Beach Resto menu, edisi elegan SunaRi: 1 gambar vertikal 1080x1920 (header = mozaik sunset sampul WA).
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
body{background:#ccc;font-family:Montserrat,sans-serif;color:#5A3E31;font-variant-numeric:lining-nums}
.pg{position:relative;width:1080px;height:1920px;overflow:hidden;background:#FBF4EC}
.pf{font-family:'Playfair Display',serif;font-weight:400} .it{font-style:italic}
.caps{font-weight:500;text-transform:uppercase;letter-spacing:.42em;color:#A67C64}
.hair{position:absolute;pointer-events:none;border:1.5px solid rgba(166,124,100,.5)}
.col{position:absolute;width:280px;top:836px}
.sec{margin-bottom:44px}
.sec h3{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:20px;font-family:'Playfair Display',serif;font-weight:400;font-style:italic;font-size:34px;color:#5A3E31}
.sec h3::before,.sec h3::after{content:"";flex:1;height:1.5px;background:#A67C64;opacity:.4}
.row{display:flex;align-items:baseline;font-family:'Playfair Display',serif;font-size:21.5px;line-height:1.2;padding:7.6px 0}
.row .dots{flex:1;border-bottom:1.5px dotted rgba(166,124,100,.65);margin:0 9px;transform:translateY(-4px)}
.row .p{font-family:Montserrat,sans-serif;font-weight:500;font-size:17px;letter-spacing:.04em;color:#A67C64}
"""
def section(name, items):
    rows = "".join(f'<div class="row"><span>{n}</span><span class="dots"></span><span class="p">{p}</span></div>' for n, p in items)
    return f'<div class="sec"><h3>{name}</h3>{rows}</div>'

gaps = "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)])
SUN = f'''<svg viewBox="0 0 200 200" width="30" height="30"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="m"><rect width="200" height="200" fill="white"/>{gaps}</mask></defs><circle cx="100" cy="100" r="96" fill="url(#g)" mask="url(#m)"/></svg>'''

c1 = section("Makanan", MENU["Makanan"])
c2 = section("Snack", MENU["Snack"]) + section("Drinks", MENU["Drinks"])
c3 = section("Juice", MENU["Juice"]) + section("Soft Drink", MENU["Soft Drink"])
COVER = "../social/wa-cover/sampul-whatsapp-business.png"
page = f'''<div class="pg" id="menu-sunari">
  <div class="hair" style="inset:34px"></div><div class="hair" style="inset:44px;opacity:.55"></div>
  <div style="position:absolute;left:96px;right:96px;top:104px;height:470px;background:url('{COVER}') 50% 44%/cover"></div>
  <div class="hair" style="left:84px;right:84px;top:92px;height:494px;border-color:rgba(166,124,100,.45)"></div>
  <div style="position:absolute;left:0;right:0;top:632px;text-align:center">
    <div class="pf" style="font-size:78px;line-height:1">Bajoy Beach <span class="it">Resto</span></div>
    <div style="display:flex;align-items:center;justify-content:center;gap:22px;margin-top:22px">
      <div style="width:110px;height:1.5px;background:#A67C64;opacity:.5"></div>{SUN}<div style="width:110px;height:1.5px;background:#A67C64;opacity:.5"></div></div>
    <div class="caps" style="font-size:16px;margin-top:22px;margin-right:-.42em">Menu · Resto &amp; Bar</div>
  </div>
  <div class="col" style="left:96px">{c1}</div>
  <div class="col" style="left:400px">{c2}</div>
  <div class="col" style="right:96px">{c3}</div>
  <div style="position:absolute;left:96px;right:96px;bottom:118px;text-align:center;border-top:1.5px solid rgba(166,124,100,.4);padding-top:22px">
    <div class="pf it" style="font-size:24px">Tamu menginap 07.00 – 21.00 &nbsp;·&nbsp; Tamu tidak menginap 07.00 – 19.00</div></div>
  <div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:13px;letter-spacing:.24em;text-transform:uppercase;color:#A67C64">
    Harga dalam ribuan rupiah (45 = Rp 45.000) · Senja Dinner pesan H-1 · WA {WA}</div>
</div>'''
(H / "menu-sunari.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:1080px 1920px;margin:0}}@media print{{body{{background:none}}}}</style></head><body>{page}</body></html>')
print("ok")
