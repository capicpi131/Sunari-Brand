"""Menu Bajoy Beach Resto (gambar WhatsApp/story 1080x1920), elegan & minimalis tanpa foto,
gaya sama dengan menu sarapan (resto/menu-sarapan). Isi & harga sesuai menu resmi pemilik
(_referensi_menu_bajoy_pemilik.png, 27 Nov 2026). Jam buka 09.00–21.00 WITA.
Run: python3 resto/menu-bajoy-wa/build.py && node resto/menu-bajoy-wa/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../../assets/logo-sunari-color.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
FOODS = [("Nasi Goreng Sunari", 45), ("Nasi Goreng Seafood", 45), ("Nasi Goreng Egois", 45), ("Nasi Goreng Kampung", 45),
         ("Ayam Lalapan", 50), ("Ayam Bakar", 50), ("Beef Sandwich", 30), ("Beef Sandwich D.", 40),
         ("Egg Sandwich", 25), ("Egg Sandwich D.", 35), ("Indomie Goreng", 20), ("Indomie Kuah", 20)]
SNACK = [("French Fries", 25), ("Toast", 25), ("Banana Roll", 25), ("Fried Cassava", 25), ("Fried Banana", 25)]
DRINKS = [("Chocolate M.S", 25), ("Oreo M.S", 25), ("Orange Punch", 25), ("Watermelon L.M", 25), ("Green Tea", 25),
          ("Hot Tea", 10), ("Ice Tea", 20), ("Black Coffee", 20), ("Coffee Milk", 20), ("Milk Tea", 25),
          ("Original Coconut", 25), ("Saronso", 25)]
JUICE = [("Avocado", 25), ("Watermelon", 25), ("Melon", 25), ("Mango", 25), ("Dragon Fruit", 25),
         ("Soursop Fruit", 25), ("Apple", 25), ("Orange", 25)]
SOFT = [("Coke", 15), ("Fanta", 15), ("Sprite", 15), ("Fresh Tea", 15), ("Pulpy", 15), ("Mineral Water", 10)]
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums tabular-nums}
.pg{position:relative;width:1080px;height:1920px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden}
.f1{position:absolute;inset:40px;border:1.5px solid rgba(138,95,72,.45)}.f2{position:absolute;inset:52px;border:1px solid rgba(138,95,72,.22)}
.in{position:absolute;left:84px;right:84px;top:110px}
.top{text-align:center}
.lg{width:180px}
.kick{font-weight:600;font-size:15px;letter-spacing:.42em;text-transform:uppercase;color:#7A5038;margin-top:14px}
h1{font-family:'Playfair Display',serif;font-weight:400;font-size:76px;line-height:1;margin-top:10px}h1 i{color:#94532B}
.rule{display:flex;align-items:center;justify-content:center;gap:16px;margin:20px 0 0}
.rule span{width:90px;height:1px;background:rgba(138,95,72,.6)}.rule b{width:7px;height:7px;transform:rotate(45deg);background:#D9703F}
.hours{display:flex;justify-content:center;gap:14px;margin-top:20px}
.hours span{padding:8px 20px;border-radius:30px;background:#5A3E31;color:#FBF4EC;font-weight:600;font-size:18px;letter-spacing:.06em}
.hours span.o{background:transparent;color:#5A3E31;box-shadow:inset 0 0 0 1.5px #5A3E31}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:30px;align-items:start}
.card{border:1.5px solid rgba(138,95,72,.4);border-radius:10px;background:#FFFDF9;overflow:hidden;margin-bottom:22px}
.card .hd{display:flex;justify-content:space-between;align-items:center;padding:11px 20px;background:#F3E7DA;border-bottom:1.5px solid rgba(138,95,72,.3)}
.card .hd b{font-weight:700;font-size:16px;letter-spacing:.24em;text-transform:uppercase;color:#5A3E31}
.card .hd span{font-size:12px;font-weight:600;letter-spacing:.12em;color:#94532B;text-transform:uppercase}
.row{display:flex;justify-content:space-between;align-items:baseline;padding:9px 20px;border-bottom:1px dashed rgba(138,95,72,.32)}
.row:last-child{border-bottom:0}
.row .n{font-family:'Playfair Display',serif;font-size:23px;line-height:1.2}
.row .p{font-weight:600;font-size:19px;color:#A2461F}
.note{font-size:14px;color:#7A5038;text-align:center;margin-top:-4px;letter-spacing:.04em}
.ft{position:absolute;left:84px;right:84px;bottom:76px;text-align:center}
.ft .t{font-weight:600;font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:#7A5038}
.ft .s{font-family:'Playfair Display',serif;font-style:italic;font-size:23px;color:#94532B;margin-top:6px}
"""
def card(title, items):
    rows = "".join(f'<div class="row"><div class="n">{n}</div><div class="p">{p}k</div></div>' for n, p in items)
    return f'<div class="card"><div class="hd"><b>{title}</b><span>{len(items)} menu</span></div>{rows}</div>'
HTML = f'''<div class="pg" id="menu-bajoy"><div class="f1"></div><div class="f2"></div>
<div class="in"><div class="top"><img class="lg" src="{LOGO}"><div class="kick">Resto &amp; Bar · Pantai Sunari</div>
<h1>Bajoy <i>Beach Resto</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="hours"><span>Buka 09.00 WITA</span><span class="o">Tutup 21.00 WITA</span></div></div>
<div class="cols"><div>{card("Foods", FOODS)}{card("Snack", SNACK)}{card("Soft Drink", SOFT)}</div>
<div>{card("Drinks", DRINKS)}{card("Juice", JUICE)}</div></div>
<div class="note">Harga dalam ribuan rupiah (k = 1.000)</div></div>
<div class="ft"><div class="t">Informasi &amp; reservasi</div><div class="s">WhatsApp 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "menu_bajoy.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok")
