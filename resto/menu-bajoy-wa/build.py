"""Menu Bajoy Beach Resto (gambar WhatsApp/story 1080x1920), elegan & minimalis tanpa foto,
gaya sama dengan menu sarapan (resto/menu-sarapan). Isi & harga sesuai menu resmi pemilik
(_referensi_menu_bajoy_pemilik.png, 27 Nov 2026). Jam buka 09.00–21.00 WITA.
Run: python3 resto/menu-bajoy-wa/build.py && node resto/menu-bajoy-wa/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../../assets/logo-sunari-color.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
# (nama Indonesia di atas, harga ribu, nama English di bawah; "" = tanpa terjemahan)
FOODS = [("Nasi Goreng Sunari", 45, "Sunari fried rice"), ("Nasi Goreng Seafood", 45, "Seafood fried rice"),
         ("Nasi Goreng Egois", 45, "Egois fried rice"), ("Nasi Goreng Kampung", 45, "Village-style fried rice"),
         ("Ayam Lalapan", 50, "Fried chicken &amp; fresh vegetables"), ("Ayam Bakar", 50, "Grilled chicken"),
         ("Sandwich Daging Sapi", 30, "Beef sandwich"), ("Sandwich Daging Sapi D.", 40, "Beef sandwich D."),
         ("Sandwich Telur", 25, "Egg sandwich"), ("Sandwich Telur D.", 35, "Egg sandwich D."),
         ("Indomie Goreng", 20, "Fried instant noodles"), ("Indomie Kuah", 20, "Instant noodle soup")]
SNACK = [("Kentang Goreng", 25, "French fries"), ("Roti Bakar", 25, "Toast"), ("Banana Roll", 25, ""),
         ("Singkong Goreng", 25, "Fried cassava"), ("Pisang Goreng", 25, "Fried banana")]
DRINKS = [("Cokelat M.S", 25, "Chocolate M.S"), ("Oreo M.S", 25, ""), ("Punch Jeruk", 25, "Orange punch"),
          ("Semangka L.M", 25, "Watermelon L.M"), ("Teh Hijau", 25, "Green tea"), ("Teh Panas", 10, "Hot tea"),
          ("Es Teh", 20, "Ice tea"), ("Kopi Hitam", 20, "Black coffee"), ("Kopi Susu", 20, "Coffee milk"),
          ("Teh Susu", 25, "Milk tea"), ("Kelapa Muda", 25, "Original coconut"), ("Saronso", 25, "")]
JUICE = [("Alpukat", 25, "Avocado"), ("Semangka", 25, "Watermelon"), ("Melon", 25, ""), ("Mangga", 25, "Mango"),
         ("Buah Naga", 25, "Dragon fruit"), ("Sirsak", 25, "Soursop"), ("Apel", 25, "Apple"), ("Jeruk", 25, "Orange")]
SOFT = [("Coke", 15, ""), ("Fanta", 15, ""), ("Sprite", 15, ""), ("Fresh Tea", 15, ""), ("Pulpy", 15, ""), ("Air Mineral", 10, "Mineral water")]
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
.row{display:flex;justify-content:space-between;align-items:baseline;padding:8px 20px;border-bottom:1px dashed rgba(138,95,72,.32)}
.row:last-child{border-bottom:0}
.row .n{font-family:'Playfair Display',serif;font-size:23px;line-height:1.2}
.row .p{font-weight:600;font-size:19px;color:#A2461F}
.note{font-size:14px;color:#7A5038;text-align:center;margin-top:-4px;letter-spacing:.04em}
.ft{position:absolute;left:84px;right:84px;bottom:76px;text-align:center}
/* teks timbul (emboss) & mudah dibaca: warna lebih gelap, highlight putih tajam di bawah, bayangan tipis di atas */
.pg{color:#2E1F14}
h1,.row .n,.ft .s{text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.35)}
h1 i,.ft .s{color:#8A4A22}
.kick,.card .hd b,.ft .t,.note{text-shadow:0 1px 0 #fff;color:#5A3E31}
.row .n{font-size:25px;color:#2E1F14;font-weight:500}
.row .p{font-size:21px;font-weight:700;color:#9A3E17;text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.25)}
.card{box-shadow:inset 1px 1px 2px rgba(90,62,49,.18),inset -1px -1px 0 #fff,0 1px 0 #fff}
.card .hd b{font-size:17px}
.hours span{text-shadow:0 -1px 0 rgba(0,0,0,.35);box-shadow:inset 0 1px 0 rgba(255,255,255,.18),0 1px 0 #fff}
.hours span.o{text-shadow:0 1px 0 #fff}
.note{font-size:15px}
.ft .t{font-weight:600;font-size:15px;letter-spacing:.3em;text-transform:uppercase;color:#7A5038}
.ft .s{font-family:'Playfair Display',serif;font-style:italic;font-size:23px;color:#94532B;margin-top:6px}
/* terjemahan di bawah setiap teks */
.en{display:block;font-family:'Playfair Display',serif;font-style:italic;font-weight:400;letter-spacing:0;text-transform:none;font-size:15px;line-height:1.2;color:#8A5F48;text-shadow:0 1px 0 #fff;margin-top:1px}
.row{padding:4px 18px 5px!important;align-items:center!important}
.row .n{font-size:22px!important;line-height:1.15!important}
.row .p{font-size:19px!important}
.card .hd{padding:7px 18px!important}.card .hd .en{font-size:14px;color:#94532B}
.card{margin-bottom:14px!important}
.cols{margin-top:22px!important;gap:22px!important}
.hours span{display:flex;flex-direction:column;align-items:center;padding:6px 20px!important;border-radius:16px!important;font-size:17px!important}
.hours span .en{font-size:13px;color:#F3D9B8;text-shadow:none}.hours span.o .en{color:#8A5F48}
.in{top:88px!important}.lg{width:160px!important}h1{font-size:68px!important}
.note .en{font-size:13px}.ft .en{font-size:14px}.ft{bottom:66px!important}
"""
def card(title, sub, items):
    rows = "".join(f'<div class="row"><div><div class="n">{n}</div>{f"<div class=en>{e}</div>" if e else ""}</div><div class="p">{p}k</div></div>' for n, p, e in items)
    return f'<div class="card"><div class="hd"><div><b>{title}</b><div class="en">{sub}</div></div><span>{len(items)} menu</span></div>{rows}</div>'
HTML = f'''<div class="pg" id="menu-bajoy"><div class="f1"></div><div class="f2"></div>
<div class="in"><div class="top"><img class="lg" src="{LOGO}"><div class="kick">Resto &amp; Bar · Pantai Sunari</div>
<h1>Bajoy <i>Beach Resto</i></h1><div class="rule"><span></span><b></b><span></span></div>
<div class="hours"><span>Buka 09.00 WITA<i class="en">Open 9:00 AM</i></span><span class="o">Tutup 21.00 WITA<i class="en">Close 9:00 PM</i></span></div></div>
<div class="cols"><div>{card("Makanan", "Foods", FOODS)}{card("Camilan", "Snack", SNACK)}{card("Minuman Ringan", "Soft drink", SOFT)}</div>
<div>{card("Minuman", "Drinks", DRINKS)}{card("Jus Buah", "Juice", JUICE)}<div class="note" style="margin-top:22px">Harga dalam ribuan rupiah (k = 1.000)<div class="en">Prices in thousand rupiah (k = 1,000)</div></div></div></div></div>
<div class="ft"><div class="t">Informasi &amp; reservasi</div><div class="en">Information &amp; reservation</div><div class="s">WhatsApp 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "menu_bajoy.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok")
