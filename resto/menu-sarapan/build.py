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
PORSI = [("Standard &amp; VIP Standard", "2 orang"), ("Superior &amp; VIP Superior", "2 orang"), ("Family Superior", "6 orang"), ("Tambahan extra bed", "1 orang")]
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased}
.pg{position:relative;width:1080px;height:1920px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden}
.f1{position:absolute;inset:40px;border:1.5px solid rgba(138,95,72,.45)}.f2{position:absolute;inset:52px;border:1px solid rgba(138,95,72,.22)}
.in{position:absolute;left:110px;right:110px;top:140px;text-align:center}
.lg{width:210px}
.kick{font-weight:600;font-size:17px;letter-spacing:.42em;text-transform:uppercase;color:#7A5038;margin-top:22px}
h1{font-family:'Playfair Display',serif;font-weight:400;font-size:84px;line-height:1;margin-top:14px}
h1 i{color:#94532B}
.rule{display:flex;align-items:center;justify-content:center;gap:16px;margin:26px 0 0}
.rule span{width:90px;height:1px;background:rgba(138,95,72,.6)}.rule b{width:7px;height:7px;transform:rotate(45deg);background:#D9703F}
/* aturan singkat */
.how{display:flex;justify-content:center;align-items:center;gap:14px;margin-top:26px;font-size:20px;color:#5A3E31}
.how .pill{padding:8px 18px;border-radius:30px;background:#5A3E31;color:#FBF4EC;font-weight:600;letter-spacing:.04em}
.how .eq{font-family:'Playfair Display',serif;font-size:28px;color:#A2461F}
/* kartu langkah */
.card{margin-top:46px;border:1.5px solid rgba(138,95,72,.4);border-radius:10px;background:#FFFDF9;text-align:left;overflow:hidden}
.card .hd{display:flex;align-items:center;gap:16px;padding:16px 26px;background:#F3E7DA;border-bottom:1.5px solid rgba(138,95,72,.3)}
.card .no{width:42px;height:42px;border-radius:50%;background:#D9703F;color:#fff;font-weight:700;font-size:20px;display:flex;align-items:center;justify-content:center;flex:0 0 42px}
.card .tt{font-weight:700;font-size:19px;letter-spacing:.2em;text-transform:uppercase;color:#5A3E31}
.card .tt span{font-weight:500;letter-spacing:.04em;text-transform:none;color:#94532B;font-size:18px;margin-left:8px}
.row{display:flex;justify-content:space-between;align-items:baseline;gap:16px;padding:15px 26px;border-bottom:1px dashed rgba(138,95,72,.35)}
.row:last-child{border-bottom:0}
.row .n{font-family:'Playfair Display',serif;font-size:31px;line-height:1.15}
.row .e{font-size:13px;letter-spacing:.2em;text-transform:uppercase;color:#9A7B66;white-space:nowrap}
/* porsi */
.porsi{margin-top:46px;border:1.5px solid rgba(138,95,72,.4);border-radius:10px;overflow:hidden;text-align:left}
.porsi .hd{padding:14px 26px;background:#5A3E31;color:#FBF4EC;font-weight:700;font-size:16px;letter-spacing:.24em;text-transform:uppercase}
.porsi .r{display:flex;justify-content:space-between;padding:11px 26px;font-size:21px;border-bottom:1px dashed rgba(138,95,72,.35);background:#FFFDF9}
.porsi .r:last-child{border-bottom:0}.porsi .r b{color:#A2461F}
.ft{position:absolute;left:110px;right:110px;bottom:84px;text-align:center}
.ft .t{font-weight:600;font-size:16px;letter-spacing:.32em;text-transform:uppercase;color:#7A5038}
.ft .s{font-family:'Playfair Display',serif;font-style:italic;font-size:24px;color:#94532B;margin-top:8px}
/* teks timbul (emboss) & mudah dibaca, seragam dengan menu Bajoy */
.pg{color:#2E1F14}
h1,.row .n,.ft .s{text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.35)}
h1 i,.ft .s{color:#8A4A22}
.kick,.card .tt,.ft .t,.how>span:first-child{text-shadow:0 1px 0 #fff;color:#5A3E31}
.row .n{color:#2E1F14;font-weight:500}
.row .e{color:#7A5038;text-shadow:0 1px 0 #fff}
.porsi .r{color:#2E1F14;text-shadow:0 1px 0 #fff}.porsi .r b{color:#9A3E17;text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.25)}
.card,.porsi{box-shadow:inset 1px 1px 2px rgba(90,62,49,.18),inset -1px -1px 0 #fff,0 1px 0 #fff}
.how .pill,.porsi .hd{text-shadow:0 -1px 0 rgba(0,0,0,.35);box-shadow:inset 0 1px 0 rgba(255,255,255,.18)}
.card .no{box-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.3);text-shadow:0 -1px 0 rgba(0,0,0,.25)}
"""
rows = lambda L: "".join(f'<div class="row"><div class="n">{n}</div><div class="e">{e}</div></div>' for n, e in L)
HTML = f'''<div class="pg" id="menu-sarapan"><div class="f1"></div><div class="f2"></div>
<div class="in"><img class="lg" src="{LOGO}"><div class="kick">Bajoy Beach Resto</div>
<h1>Menu <i>Sarapan</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="how"><span>Termasuk harga kamar</span><span class="eq">·</span><span class="pill">1 orang = 1 makanan + 1 minuman</span></div>
<div class="card"><div class="hd"><div class="no">1</div><div class="tt">Makanan<span>pilih 1</span></div></div>{rows(MAKANAN)}</div>
<div class="card"><div class="hd"><div class="no">2</div><div class="tt">Minuman<span>pilih 1</span></div></div>{rows(MINUMAN)}</div>
<div class="porsi"><div class="hd">Jumlah sarapan per kamar</div>{"".join(f'<div class="r"><span>{a}</span><b>{b}</b></div>' for a, b in PORSI)}</div></div>
<div class="ft"><div class="t">Disajikan mulai pukul 07.00 WITA</div><div class="s">WhatsApp 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "menu_sarapan.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok")
