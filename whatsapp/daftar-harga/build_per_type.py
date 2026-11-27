"""Gambar harga per tipe kamar SunaRi (1080x1920, satu gambar per tipe) untuk dikirim lewat WhatsApp.
Foto utama tidak tertutup tulisan; SEMUA foto tipe kamar tersebut ditampilkan (foto utama + galeri).
Harga hanya untuk balasan WhatsApp / dokumen, BUKAN konten media sosial (panduan brand).
Run: python3 whatsapp/daftar-harga/build_per_type.py && node whatsapp/daftar-harga/render_per_type.js"""
import pathlib, math
H = pathlib.Path(__file__).parent
LOGO_D = "../../assets/logo-sunari-color-dark.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
rp = lambda v: "Rp " + f"{v:,}".replace(",", ".")
COMMON = ["Sarapan setiap pagi", "AC &amp; Wi-Fi", "Kopi/teh &amp; pemanas air", "Meja kerja/rias", "Tirai blackout",
          "Perlengkapan mandi &amp; handuk", "Bantal &amp; selimut tambahan", "Setrika atas permintaan"]
# (kunci, nama1, nama2, harga, folder foto, foto utama, [semua foto lain], kapasitas, tagline, sorotan)
ROOMS = [
 ("standard", "Standard", "Bungalow", 900_000, "../katalog-standard/foto/", "g_teras",
  ["g_kamarsudut", "g_kamardepan", "g_bambu", "g_toilet"],
  "2 orang · maks. 3 dengan extra bed", "Pagi menghadap laut Selayar",
  ["Queen bed", "Kamar mandi bambu &amp; lantai batu alam", "Shower &amp; toilet duduk", "Teras luas view laut &amp; taman"]),
 ("vip-standard", "VIP Standard", "Bungalow", 1_000_000, "../katalog-vip-standard/foto/", "g_eksterior",
  ["g_terasview", "g_terassamping", "g_teraslaut", "g_kamarsudut", "g_kamardepan", "g_kamarsamping", "g_wastafel", "g_shower", "g_toilet"],
  "2 orang · maks. 3 dengan extra bed", "Turun tangga, langsung pasir",
  ["King bed", "Rumah panggung tepi pantai", "Lebih luas dari Standard", "Teras view laut atau taman"]),
 ("superior", "Superior", "Bungalow", 1_500_000, "../katalog-superior/foto/", "g_eksterior",
  ["g_depan", "g_teras", "g_kamar", "g_loteng", "g_meja", "g_tv", "g_taman", "g_wastafel", "g_shower", "g_toilet"],
  "2 orang · maks. 3 dengan extra bed", "Rumah kayu di antara pohon kelapa",
  ["King bed &amp; loteng", "TV di kamar", "Kamar mandi semi-outdoor bertaman", "Rain shower &amp; teras kayu"]),
 ("vip-superior", "VIP Superior", "Bungalow", 2_500_000, "../katalog-vip-superior/foto/", "g_eksterior",
  ["g_teras", "g_terasdepan", "g_kamar", "g_loteng", "g_dariloteng", "g_bathtub", "g_wastafel", "g_sabun", "g_toilet"],
  "2 orang · maks. 3 dengan extra bed", "Kelas tertinggi · berendam di bawah langit terbuka",
  ["King bed &amp; loteng", "TV &amp; mini bar/kulkas", "Bathtub, air panas &amp; dingin", "Kamar mandi beratap kaca"]),
 ("family-superior", "Family Superior", "Bungalow", 2_500_000, "../katalog-family-superior/foto/", "g_eksterior",
  ["g_terassamping", "g_terassofa", "g_bawahdepan", "g_bawahsamping", "g_bawahsudut", "g_lorong", "g_atas4kasur", "g_ataskettle", "g_atasmeja", "g_wastafel", "g_shower", "g_toilet"],
  "6 orang · maks. 8 dengan 2 extra bed", "Satu rumah, dua lantai, semua bersama",
  ["2 lantai", "1 tempat tidur besar + 4 kasur", "2 kamar mandi (lantai 1 &amp; 2)", "Teras pribadi"]),
]
GAL_H = 690
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
.pg{position:relative;width:1080px;height:1920px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden}
.main{position:relative;height:600px}.main>img.bg{width:100%;height:100%;object-fit:cover;display:block}
.main .sh{position:absolute;left:0;right:0;top:0;height:180px;background:linear-gradient(180deg,rgba(30,20,12,.5),rgba(30,20,12,0))}
.main .lg{position:absolute;left:50px;top:36px;width:220px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.main .pt{position:absolute;right:50px;top:50px;font-weight:700;font-size:15px;letter-spacing:.24em;color:#FFF3E2;text-transform:uppercase;text-shadow:0 2px 8px rgba(0,0,0,.6)}
.body{padding:30px 50px 0}
.top{display:flex;justify-content:space-between;align-items:flex-end;gap:20px}
.nm{font-family:'Playfair Display',serif;font-weight:500;font-size:58px;line-height:1.02}.nm i{color:#94532B}
.pr{text-align:right;white-space:nowrap}.pr b{display:block;font-size:44px;color:#A2461F;line-height:1}
.pr span{font-size:14px;font-weight:600;letter-spacing:.1em;color:#7A5038;text-transform:uppercase}
.row2{display:flex;align-items:center;gap:16px;margin-top:12px}
.tag{font-family:'Playfair Display',serif;font-style:italic;font-size:24px;color:#94532B}
.cap{padding:6px 14px;border-radius:30px;background:#7BA7B6;color:#fff;font-weight:700;font-size:15px;letter-spacing:.06em;white-space:nowrap}
.hl{display:grid;grid-template-columns:1fr 1fr;gap:8px 14px;margin-top:16px}
.hl div{padding:10px 14px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px #D9703F;font-weight:600;font-size:18px}
.gt{margin-top:18px;font-weight:700;font-size:14px;letter-spacing:.24em;text-transform:uppercase;color:#7A5038}
.gal{display:grid;gap:8px;margin-top:8px;height:GALHpx}
.gal div{border-radius:6px;overflow:hidden}.gal img{width:100%;height:100%;object-fit:cover;display:block}
.fx{display:grid;grid-template-columns:1fr 1fr;gap:2px 18px;margin-top:14px;font-size:17px;color:#5A3E31}
.fx div::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:#A67C64;margin-right:10px;vertical-align:2px}
.eb{margin-top:12px;padding-top:12px;border-top:1.5px solid rgba(138,95,72,.3);display:flex;justify-content:space-between;font-size:17px}.eb b{color:#A2461F}
.ft{position:absolute;left:50px;right:50px;bottom:28px;text-align:center}
.ft .c{font-weight:700;font-size:13px;letter-spacing:.26em;text-transform:uppercase;color:#7A5038}
.ft .w{font-family:'Playfair Display',serif;font-size:27px;margin-top:2px}.ft .w i{color:#94532B}
""".replace("GALH", str(GAL_H))
PAGES = []
for key, a, b, price, F, main, rest, cap, tag, hl in ROOMS:
    n = len(rest); cols = 2 if n <= 4 else (3 if n <= 9 else 4); rows = math.ceil(n / cols)
    # sel terakhir melebar bila baris terakhir tidak penuh
    cells = []
    for i, k in enumerate(rest):
        span = ""
        if i == n - 1 and n % cols:
            span = f"grid-column:span {cols - (n % cols) + 1};"
        cells.append(f'<div style="{span}"><img src="{F}{k}.jpg"></div>')
    gal = f'<div class="gal" style="grid-template-columns:repeat({cols},1fr);grid-template-rows:repeat({rows},1fr)">{"".join(cells)}</div>'
    PAGES.append(f'''<div class="pg" id="harga-{key}">
  <div class="main"><img class="bg" src="{F}{main}.jpg"><div class="sh"></div><img class="lg" src="{LOGO_D}"><div class="pt">Harga kamar</div></div>
  <div class="body"><div class="top"><div class="nm">{a} <i>{b}</i></div>
    <div class="pr"><b>{rp(price)}</b><span>per malam · termasuk sarapan</span></div></div>
    <div class="row2"><div class="tag">{tag}</div></div><div class="row2" style="margin-top:8px"><div class="cap">{cap}</div></div>
    <div class="hl">{"".join(f"<div>{x}</div>" for x in hl)}</div>
    <div class="gt">Foto kamar ({n + 1} foto)</div>{gal}
    <div class="fx">{"".join(f"<div>{x}</div>" for x in COMMON)}</div>
    <div class="eb"><span>Extra bed <b>Rp 150.000</b> / malam</span><span>Check-in 14.00 · Check-out 12.00 WITA</span></div></div>
  <div class="ft"><div class="c">Informasi &amp; reservasi</div><div class="w"><i>WhatsApp</i> 0813-4150-4973 · 0821-8903-3044</div></div></div>''')
(H / "harga_per_type.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(PAGES)}</body></html>')
print(len(PAGES))
