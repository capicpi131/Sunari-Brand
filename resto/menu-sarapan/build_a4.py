"""Menu sarapan versi A4 (desain 1240x1754 px = A4; PNG HD 2x = 2480x3508 px = A4 300 dpi).
Isi, warna, tulisan timbul & dwibahasa sama dengan build.py; tata letak disusun ulang untuk A4:
kartu Makanan & Minuman berdampingan, tabel porsi melebar di bawah.
Run: python3 resto/menu-sarapan/build_a4.py && node resto/render_a4.js"""
import pathlib
H = pathlib.Path(__file__).parent
ns = {"__file__": str(H / "build.py")}
exec((H / "build.py").read_text(), ns)
CSS, FONTS, LOGO, en, rows = ns["CSS"], ns["FONTS"], ns["LOGO"], ns["en"], ns["rows"]
MAKANAN, MINUMAN, PORSI = ns["MAKANAN"], ns["MINUMAN"], ns["PORSI"]
CSS += """
/* ---- A4 ---- */
.pg{width:1240px!important;height:1754px!important}
.in{left:110px!important;right:110px!important;top:96px!important}
.lg{width:200px!important}
h1{font-size:88px!important}
.two{display:grid;grid-template-columns:1fr 1fr;gap:30px;margin-top:36px;align-items:start}
.two .card{margin-top:0!important}
.row{padding:10px 26px 11px!important}
.row .n{font-size:31px!important}.row .e{font-size:19px!important}
.how{margin-top:30px!important;font-size:22px!important}
.porsi{margin-top:30px!important}
.porsi .r{padding:10px 26px!important;font-size:22px!important}
.ft{bottom:80px!important}
"""
porsi = "".join(f'<div class="r"><span>{a}{en(ae) if ae else ""}</span><b>{b} <i class="en2">/ {be}</i></b></div>' for a, ae, b, be in PORSI)
HTML = f'''<div class="pg" id="menu-sarapan-a4"><div class="f1"></div><div class="f2"></div>
<div class="in"><img class="lg" src="{LOGO}"><div class="kick">Bajoy Beach Resto</div>
<h1>Menu <i>Sarapan</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="how"><span>Termasuk harga kamar{en("Included in the room rate")}</span><span class="eq">·</span><span class="pill">1 orang = 1 makanan + 1 minuman{en("1 person = 1 food + 1 drink")}</span></div>
<div class="two">
<div class="card"><div class="hd"><div class="no">1</div><div class="tt">Makanan<span>pilih 1</span>{en("Food · choose 1")}</div></div>{rows(MAKANAN)}</div>
<div class="card"><div class="hd"><div class="no">2</div><div class="tt">Minuman<span>pilih 1</span>{en("Drink · choose 1")}</div></div>{rows(MINUMAN)}</div></div>
<div class="porsi"><div class="hd">Jumlah sarapan per kamar{en("Breakfast per room")}</div>{porsi}</div></div>
<div class="ft"><div class="t">Disajikan mulai pukul 07.00 WITA</div>{en("Served from 07.00 WITA")}<div class="s">WhatsApp 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "menu_sarapan_a4.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok a4")
