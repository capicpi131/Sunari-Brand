"""Bajoy Beach Resto menu, edisi elegan SunaRi: 2 halaman A4 (Makanan | Minuman).
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
.pg{position:relative;width:794px;height:1123px;overflow:hidden;background:#FBF4EC;page-break-after:always;margin:0 auto 20px}
.pf{font-family:'Playfair Display',serif;font-weight:400} .it{font-style:italic}
.caps{font-weight:500;text-transform:uppercase;letter-spacing:.42em;color:#A67C64}
.hair{position:absolute;pointer-events:none;border:1px solid rgba(166,124,100,.5)}
.col{position:absolute;width:290px}
.sec{margin-bottom:34px}
.tight .row{padding:3.8px 0} .tight .sec{margin-bottom:28px}
.sec h3{display:flex;align-items:center;justify-content:center;gap:14px;margin-bottom:16px;font-family:'Playfair Display',serif;font-weight:400;font-style:italic;font-size:25px;color:#5A3E31}
.sec h3::before,.sec h3::after{content:"";flex:1;height:1px;background:#A67C64;opacity:.4}
.row{display:flex;align-items:baseline;font-family:'Playfair Display',serif;font-size:14.5px;line-height:1.2;padding:5.2px 0}
.row .dots{flex:1;border-bottom:1px dotted rgba(166,124,100,.65);margin:0 9px;transform:translateY(-3px)}
.row .p{font-family:Montserrat,sans-serif;font-weight:500;font-size:11.5px;letter-spacing:.06em;color:#A67C64}
"""
def section(name, items):
    rows = "".join(f'<div class="row"><span>{n}</span><span class="dots"></span><span class="p">{p}</span></div>' for n, p in items)
    return f'<div class="sec"><h3>{name}</h3>{rows}</div>'

def sun(size, uid):
    gaps = "".join(f'<rect x="0" y="{y}" width="200" height="{h}" fill="black"/>' for y, h in [(112,5),(126,7),(142,9),(160,11),(180,13)])
    return f'''<svg viewBox="0 0 200 200" width="{size}" height="{size}"><defs><linearGradient id="g{uid}" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FDB15D"/><stop offset="1" stop-color="#FF8A5C"/></linearGradient>
<mask id="m{uid}"><rect width="200" height="200" fill="white"/>{gaps}</mask></defs><circle cx="100" cy="100" r="96" fill="url(#g{uid})" mask="url(#m{uid})"/></svg>'''

def page(n, photo, pos, kicker, left, right, cls=""):
    return f'''<div class="pg {cls}">
  <div class="hair" style="inset:26px"></div><div class="hair" style="inset:33px;opacity:.55"></div>
  <img src="../assets/logo-sunari-color.png" style="position:absolute;left:50%;top:54px;width:170px;transform:translateX(-50%)">
  <div style="position:absolute;left:84px;right:84px;top:152px;height:176px;background:url('{photo}') {pos}/cover"></div>
  <div class="hair" style="left:76px;right:76px;top:144px;height:192px;border-color:rgba(166,124,100,.45)"></div>
  <div style="position:absolute;left:0;right:0;top:362px;text-align:center">
    <div class="pf" style="font-size:42px;line-height:1">Bajoy Beach <span class="it">Resto</span></div>
    <div style="display:flex;align-items:center;justify-content:center;gap:16px;margin-top:14px">
      <div style="width:70px;height:1px;background:#A67C64;opacity:.5"></div>{sun(20, n)}<div style="width:70px;height:1px;background:#A67C64;opacity:.5"></div></div>
    <div class="caps" style="font-size:9.5px;margin-top:14px;margin-right:-.42em">{kicker}</div>
  </div>
  <div class="col" style="left:84px;top:480px">{left}</div>
  <div class="col" style="right:84px;top:480px">{right}</div>
  <div style="position:absolute;left:84px;right:84px;bottom:92px;text-align:center;border-top:1px solid rgba(166,124,100,.4);padding-top:16px">
    <div class="pf it" style="font-size:15px;color:#5A3E31">Tamu menginap 07.00 – 21.00 &nbsp;·&nbsp; Tamu tidak menginap 07.00 – 19.00</div></div>
  <div style="position:absolute;left:0;right:0;bottom:50px;text-align:center;font-size:8.5px;letter-spacing:.24em;text-transform:uppercase;color:#A67C64;line-height:1.9">
    Harga dalam ribuan rupiah (45 = Rp 45.000) · Senja Dinner pesan H-1 · WA {WA}</div>
</div>'''

p1 = page(1, "../assets/photos/graded/senja__59-makan-senja-payung-1810.jpg", "50% 40%", "Menu · Makanan &amp; Snack",
          section("Makanan", MENU["Makanan"]), section("Snack", MENU["Snack"]))
p2 = page(2, "../assets/photos/graded/senja__82-dua-tamu-meja-senja.jpg", "50% 45%", "Menu · Minuman",
          section("Drinks", MENU["Drinks"]), section("Juice", MENU["Juice"]) + section("Soft Drink", MENU["Soft Drink"]), "tight")
(H / "menu-sunari.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}@page{{size:210mm 297mm;margin:0}}@media print{{body{{background:none}}.pg{{margin:0}}}}</style></head><body>{p1}{p2}</body></html>')
print("ok")
