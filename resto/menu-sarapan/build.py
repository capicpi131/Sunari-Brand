"""Menu sarapan SunaRi (gambar WhatsApp/story 1080x1920), elegan & minimalis, tanpa foto.
Sistem: termasuk harga kamar, 1 pax = 1 makanan + 1 minuman. Isi menu sesuai menu sarapan resmi (Breakfast Menu dari pemilik, 27 Nov 2026).
Run: python3 resto/menu-sarapan/build.py && node resto/menu-sarapan/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../../assets/logo-sunari-color.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
MAKANAN = [("Nasi Goreng", "Fried rice"), ("Mie Goreng", "Fried noodles"), ("Roti Bakar Omelet", "Toast omelette"),
           ("Roti Bakar Telur Orak-arik", "Toast scrambled egg"), ("Roti Bakar Cokelat / Keju", "Toast chocolate / cheese"), ("Pancake", "Pancake")]
MINUMAN = [("Kopi Hitam", "Black coffee"), ("Kopi Susu", "Coffee milk"), ("Teh", "Tea"), ("Teh Susu", "Milk tea")]
PORSI = [("Standard &amp; VIP Standard", "2 pax"), ("Superior &amp; VIP Superior", "2 pax"), ("Family Superior", "6 pax"), ("Extra bed", "1 pax")]
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased}
.pg{position:relative;width:1080px;height:1920px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden}
.f1{position:absolute;inset:40px;border:1.5px solid rgba(138,95,72,.45)}.f2{position:absolute;inset:52px;border:1px solid rgba(138,95,72,.22)}
.in{position:absolute;left:120px;right:120px;top:120px;text-align:center}
.lg{width:230px}
.kick{font-weight:600;font-size:18px;letter-spacing:.42em;text-transform:uppercase;color:#7A5038;margin-top:30px}
h1{font-family:'Playfair Display',serif;font-weight:400;font-size:90px;line-height:1;margin-top:18px;letter-spacing:.01em}
h1 i{color:#94532B}
.rule{display:flex;align-items:center;justify-content:center;gap:16px;margin:34px 0 0}
.rule span{width:90px;height:1px;background:rgba(138,95,72,.6)}.rule b{width:7px;height:7px;transform:rotate(45deg);background:#D9703F}
.how{font-family:'Playfair Display',serif;font-style:italic;font-size:27px;color:#5A3E31;margin-top:28px}
.sec{margin-top:44px}
.grid{display:grid;grid-template-columns:1fr 1fr;column-gap:30px}
.st{font-weight:600;font-size:17px;letter-spacing:.5em;text-transform:uppercase;color:#A2461F}
.it{margin-top:14px}
.it .n{font-family:'Playfair Display',serif;font-size:35px;line-height:1.1}
.it .e{font-size:14px;letter-spacing:.22em;text-transform:uppercase;color:#9A7B66;margin-top:4px}
.porsi{margin:44px auto 0;width:560px;padding:20px 34px;border:1px solid rgba(138,95,72,.35)}
.pg2{display:grid;grid-template-columns:1fr;gap:6px;margin-top:12px;font-size:20px;color:#5A3E31}
.pg2 div{display:flex;justify-content:space-between;border-bottom:1px dotted rgba(138,95,72,.4);padding-bottom:4px}.pg2 b{color:#A2461F;font-weight:600}
.ft{position:absolute;left:130px;right:130px;bottom:100px;text-align:center}
.ft .t{font-weight:600;font-size:16px;letter-spacing:.34em;text-transform:uppercase;color:#7A5038}
.ft .s{font-family:'Playfair Display',serif;font-style:italic;font-size:24px;color:#94532B;margin-top:10px}
"""
items = lambda L: "".join(f'<div class="it"><div class="n">{n}</div><div class="e">{e}</div></div>' for n, e in L)
HTML = f'''<div class="pg" id="menu-sarapan"><div class="f1"></div><div class="f2"></div>
<div class="in"><img class="lg" src="{LOGO}"><div class="kick">Bajoy Beach Resto</div>
<h1>Menu <i>Sarapan</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="how">Termasuk harga kamar · 1 pax = 1 makanan &amp; 1 minuman</div>
<div class="sec"><div class="st">Makanan</div>{items(MAKANAN)}</div>
<div class="sec"><div class="st">Minuman</div>{items(MINUMAN)}</div>
<div class="porsi"><div class="st" style="font-size:15px">Porsi sarapan per kamar</div><div class="pg2">{"".join(f'<div><span>{a}</span><b>{b}</b></div>' for a, b in PORSI)}</div></div></div>
<div class="ft"><div class="t">Disajikan mulai pukul 07.00 WITA</div><div class="s">WhatsApp 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "menu_sarapan.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok")
