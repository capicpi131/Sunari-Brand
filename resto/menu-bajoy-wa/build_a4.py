"""Menu Bajoy Beach Resto versi A4 (desain 1240x1754 px = A4; PNG HD 2x = 2480x3508 px = A4 300 dpi).
Isi, harga, warna, tulisan timbul & dwibahasa sama dengan build.py; tata letak 3 kolom untuk A4.
Run: python3 resto/menu-bajoy-wa/build_a4.py && node resto/render_a4.js"""
import pathlib
H = pathlib.Path(__file__).parent
ns = {"__file__": str(H / "build.py")}
exec((H / "build.py").read_text(), ns)
CSS, FONTS, LOGO, card = ns["CSS"], ns["FONTS"], ns["LOGO"], ns["card"]
FOODS, SNACK, DRINKS, JUICE, SOFT = (ns[k] for k in ("FOODS", "SNACK", "DRINKS", "JUICE", "SOFT"))
CSS += """
/* ---- A4 ---- */
.pg{width:1240px!important;height:1754px!important}
.in{left:84px!important;right:84px!important;top:92px!important}
.lg{width:180px!important}h1{font-size:80px!important}
.cols{grid-template-columns:1fr 1fr 1fr!important;gap:22px!important;margin-top:30px!important}
.row{padding:6px 16px 7px!important}
.row .n{font-size:22px!important}.row .p{font-size:19px!important}
.card .hd{padding:8px 16px!important}
.card{margin-bottom:18px!important}
.ft{bottom:72px!important}
"""
HTML = f'''<div class="pg" id="menu-bajoy-a4"><div class="f1"></div><div class="f2"></div>
<div class="in"><div class="top"><img class="lg" src="{LOGO}"><div class="kick">Resto &amp; Bar · Pantai Sunari</div>
<h1>Bajoy <i>Beach Resto</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="hours"><span>Buka 09.00 WITA<i class="en">Open 9:00 AM</i></span><span class="o">Tutup 21.00 WITA<i class="en">Close 9:00 PM</i></span></div></div>
<div class="cols"><div>{card("Foods", "Makanan", FOODS)}{card("Snack", "Camilan", SNACK)}</div>
<div>{card("Drinks", "Minuman", DRINKS)}{card("Soft Drink", "Minuman ringan", SOFT)}</div>
<div>{card("Juice", "Jus buah", JUICE)}<div class="note" style="margin-top:22px">Harga dalam ribuan rupiah (k = 1.000)<div class="en">Prices in thousand rupiah (k = 1,000)</div></div></div></div></div>
<div class="ft"><div class="t">Informasi &amp; reservasi</div><div class="en">Information &amp; reservation</div><div class="s">WhatsApp 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "menu_bajoy_a4.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok a4")
