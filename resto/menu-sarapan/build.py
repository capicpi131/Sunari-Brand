"""Menu sarapan SunaRi (gambar WhatsApp/story 1080x1920), elegan & minimalis, tanpa foto.
Sistem: tamu memilih 1 makanan + 1 minuman. Item diambil dari menu Bajoy Beach Resto (resto/MENU_BAJOY.md);
ubah daftar MAKANAN / MINUMAN di bawah bila menu sarapan berbeda.
Run: python3 resto/menu-sarapan/build.py && node resto/menu-sarapan/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../../assets/logo-sunari-color.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600&display=swap" rel="stylesheet">'
MAKANAN = [("Nasi Goreng Sunari", "Sunari fried rice"), ("Nasi Goreng Kampung", "Village-style fried rice"),
           ("Egg Sandwich", "Egg sandwich"), ("Toast", "Toasted bread"),
           ("Indomie Goreng", "Fried noodles"), ("Indomie Kuah", "Noodle soup")]
MINUMAN = [("Kopi Hitam", "Black coffee"), ("Kopi Susu", "Coffee with milk"), ("Teh Panas", "Hot tea"),
           ("Es Teh", "Iced tea"), ("Teh Susu", "Milk tea")]
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased}
.pg{position:relative;width:1080px;height:1920px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden}
.f1{position:absolute;inset:40px;border:1.5px solid rgba(138,95,72,.45)}.f2{position:absolute;inset:52px;border:1px solid rgba(138,95,72,.22)}
.in{position:absolute;left:120px;right:120px;top:150px;text-align:center}
.lg{width:230px}
.kick{font-weight:600;font-size:18px;letter-spacing:.42em;text-transform:uppercase;color:#7A5038;margin-top:30px}
h1{font-family:'Playfair Display',serif;font-weight:400;font-size:90px;line-height:1;margin-top:18px;letter-spacing:.01em}
h1 i{color:#94532B}
.rule{display:flex;align-items:center;justify-content:center;gap:16px;margin:34px 0 0}
.rule span{width:90px;height:1px;background:rgba(138,95,72,.6)}.rule b{width:7px;height:7px;transform:rotate(45deg);background:#D9703F}
.how{font-family:'Playfair Display',serif;font-style:italic;font-size:30px;color:#5A3E31;margin-top:28px}
.sec{margin-top:66px}
.grid{display:grid;grid-template-columns:1fr 1fr;column-gap:30px}
.st{font-weight:600;font-size:17px;letter-spacing:.5em;text-transform:uppercase;color:#A2461F}
.it{margin-top:24px}
.it .n{font-family:'Playfair Display',serif;font-size:35px;line-height:1.1}
.it .e{font-size:14px;letter-spacing:.22em;text-transform:uppercase;color:#9A7B66;margin-top:4px}
.ft{position:absolute;left:130px;right:130px;bottom:100px;text-align:center}
.ft .t{font-weight:600;font-size:16px;letter-spacing:.34em;text-transform:uppercase;color:#7A5038}
.ft .s{font-family:'Playfair Display',serif;font-style:italic;font-size:24px;color:#94532B;margin-top:10px}
"""
items = lambda L: "".join(f'<div class="it"><div class="n">{n}</div><div class="e">{e}</div></div>' for n, e in L)
HTML = f'''<div class="pg" id="menu-sarapan"><div class="f1"></div><div class="f2"></div>
<div class="in"><img class="lg" src="{LOGO}"><div class="kick">Bajoy Beach Resto</div>
<h1>Menu <i>Sarapan</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="how">Pilih satu makanan &amp; satu minuman</div>
<div class="sec"><div class="st">Makanan</div>{items(MAKANAN)}</div>
<div class="sec"><div class="st">Minuman</div>{items(MINUMAN)}</div></div>
<div class="ft"><div class="t">Disajikan mulai pukul 07.00 WITA</div><div class="s">Selamat pagi dari Pantai Sunari</div></div></div>'''
(H / "menu_sarapan.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok")
