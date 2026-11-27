"""Gambar harga per tipe kamar SunaRi (1080x1350, satu gambar per tipe) untuk dikirim lewat WhatsApp.
Harga hanya untuk balasan WhatsApp / dokumen, BUKAN konten media sosial (panduan brand).
Run: python3 whatsapp/daftar-harga/build_per_type.py && node whatsapp/daftar-harga/render_per_type.js"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO_D = "../../assets/logo-sunari-color-dark.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
rp = lambda v: "Rp " + f"{v:,}".replace(",", ".")
COMMON = ["Sarapan setiap pagi", "AC &amp; Wi-Fi", "Kopi/teh &amp; pemanas air", "Meja kerja/rias", "Tirai blackout",
          "Perlengkapan mandi &amp; handuk", "Bantal &amp; selimut tambahan", "Setrika atas permintaan"]
ROOMS = [
 ("standard", "Standard", "Bungalow", 900_000, "../katalog-standard/foto/g_teras.jpg", "center 55%",
  "2 orang · maks. 3 dengan extra bed", "Pagi menghadap laut Selayar",
  ["Queen bed", "Kamar mandi bambu &amp; lantai batu alam", "Shower &amp; toilet duduk", "Teras luas view laut &amp; taman"]),
 ("vip-standard", "VIP Standard", "Bungalow", 1_000_000, "../katalog-vip-standard/foto/g_eksterior.jpg", "center 50%",
  "2 orang · maks. 3 dengan extra bed", "Turun tangga, langsung pasir",
  ["King bed", "Rumah panggung tepi pantai", "Lebih luas dari Standard", "Teras view laut atau taman"]),
 ("superior", "Superior", "Bungalow", 1_500_000, "../katalog-superior/foto/g_eksterior.jpg", "center 45%",
  "2 orang · maks. 3 dengan extra bed", "Rumah kayu di antara pohon kelapa",
  ["King bed &amp; loteng", "TV di kamar", "Kamar mandi semi-outdoor bertaman", "Rain shower &amp; teras kayu"]),
 ("vip-superior", "VIP Superior", "Bungalow", 2_500_000, "../katalog-vip-superior/foto/g_bathtub.jpg", "center 55%",
  "2 orang · maks. 3 dengan extra bed", "Kelas tertinggi · berendam di bawah langit terbuka",
  ["King bed &amp; loteng", "TV &amp; mini bar/kulkas", "Bathtub, air panas &amp; dingin", "Kamar mandi beratap kaca"]),
 ("family-superior", "Family Superior", "Bungalow", 2_500_000, "../katalog-family-superior/foto/g_eksterior.jpg", "center 50%",
  "6 orang · maks. 8 dengan 2 extra bed", "Satu rumah, dua lantai, semua bersama",
  ["2 lantai", "1 tempat tidur besar + 4 kasur", "2 kamar mandi (lantai 1 &amp; 2)", "Teras pribadi"]),
]
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
.pg{position:relative;width:1080px;height:1350px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden}
.ph{position:absolute;left:0;right:0;top:0;height:680px}.ph .bgimg{width:100%;height:100%;object-fit:cover}
.ph .sh{position:absolute;left:0;right:0;top:0;height:220px;background:linear-gradient(180deg,rgba(30,20,12,.55),rgba(30,20,12,0))}
.ph .lg{position:absolute;left:56px;top:44px;width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.ph .pt{position:absolute;right:56px;top:58px;font-weight:700;font-size:16px;letter-spacing:.24em;color:#FFF3E2;text-transform:uppercase;text-shadow:0 2px 8px rgba(0,0,0,.6)}
.card{position:absolute;left:56px;right:56px;top:590px;background:#FBF4EC;border-radius:14px;padding:34px 40px 30px;box-shadow:0 10px 30px rgba(90,62,49,.18)}
.top{display:flex;justify-content:space-between;align-items:flex-end;gap:20px}
.nm{font-family:'Playfair Display',serif;font-weight:500;font-size:62px;line-height:1.02;text-shadow:0 1px 0 #fff}
.nm i{color:#94532B}
.pr{text-align:right;white-space:nowrap}.pr b{display:block;font-size:46px;color:#A2461F;line-height:1}.pr span{font-size:16px;font-weight:600;letter-spacing:.1em;color:#7A5038;text-transform:uppercase}
.tag{font-family:'Playfair Display',serif;font-style:italic;font-size:26px;color:#94532B;margin-top:12px}
.cap{display:inline-block;margin-top:14px;padding:7px 16px;border-radius:30px;background:#7BA7B6;color:#fff;font-weight:700;font-size:16px;letter-spacing:.08em}
.hl{display:grid;grid-template-columns:1fr 1fr;gap:10px 18px;margin-top:22px}
.hl div{padding:12px 16px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px #D9703F;font-weight:600;font-size:19px}
.fx{display:grid;grid-template-columns:1fr 1fr;gap:4px 18px;margin-top:18px;font-size:18px;color:#5A3E31}
.fx div::before{content:"";display:inline-block;width:8px;height:8px;border-radius:50%;background:#A67C64;margin-right:10px;vertical-align:2px}
.eb{margin-top:18px;padding-top:14px;border-top:1.5px solid rgba(138,95,72,.3);display:flex;justify-content:space-between;font-size:18px}
.eb b{color:#A2461F}
.ft{position:absolute;left:56px;right:56px;bottom:34px;text-align:center}
.ft .c{font-weight:700;font-size:13px;letter-spacing:.26em;text-transform:uppercase;color:#7A5038}
.ft .w{font-family:'Playfair Display',serif;font-size:28px;margin-top:4px}.ft .w i{color:#94532B}
"""
PAGES = []
for key, a, b, price, img, pos, cap, tag, hl in ROOMS:
    PAGES.append(f'''<div class="pg" id="harga-{key}"><div class="ph"><img class="bgimg" src="{img}" style="object-position:{pos}"><div class="sh"></div>
  <img class="lg" src="{LOGO_D}"><div class="pt">Harga kamar</div></div>
  <div class="card"><div class="top"><div class="nm">{a}<br><i>{b}</i></div>
    <div class="pr"><b>{rp(price)}</b><span>per malam · termasuk sarapan</span></div></div>
    <div class="tag">{tag}</div><div class="cap">{cap}</div>
    <div class="hl">{"".join(f"<div>{x}</div>" for x in hl)}</div>
    <div class="fx">{"".join(f"<div>{x}</div>" for x in COMMON)}</div>
    <div class="eb"><span>Extra bed <b>Rp 150.000</b> / malam</span><span>Check-in 14.00 · Check-out 12.00 WITA</span></div></div>
  <div class="ft"><div class="c">Informasi &amp; reservasi</div><div class="w"><i>WhatsApp</i> 0813-4150-4973 · 0821-8903-3044</div></div></div>''')
(H / "harga_per_type.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(PAGES)}</body></html>')
print(len(PAGES))
