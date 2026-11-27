"""Gambar daftar harga kamar SunaRi Beach Resort Selayar (1080x1600) untuk dikirim lewat WhatsApp.
Harga hanya untuk balasan WhatsApp / dokumen, BUKAN konten media sosial (panduan brand).
Foto: hasil grading tema SunaRi dari folder katalog WhatsApp.
Run: python3 whatsapp/daftar-harga/build.py && node whatsapp/daftar-harga/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
LOGO = "../../assets/logo-sunari-color.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
ROOMS = [
 ("Standard Bungalow", 900_000, "../katalog-standard/foto/g_teras.jpg", "center 55%", "2 org (maks. 3)",
  "Queen bed · AC · Wi-Fi · kopi/teh · kamar mandi bambu · teras luas view laut &amp; taman"),
 ("VIP Standard Bungalow", 1_000_000, "../katalog-vip-standard/foto/g_eksterior.jpg", "center 50%", "2 org (maks. 3)",
  "Rumah panggung tepi pantai · King bed · AC · Wi-Fi · kopi/teh · teras view laut/taman"),
 ("Superior Bungalow", 1_500_000, "../katalog-superior/foto/g_eksterior.jpg", "center 45%", "2 org (maks. 3)",
  "A-frame + loteng · King bed · TV · AC · Wi-Fi · kamar mandi semi-outdoor + rain shower"),
 ("VIP Superior Bungalow", 2_500_000, "../katalog-vip-superior/foto/g_bathtub.jpg", "center 55%", "2 org (maks. 3)",
  "Kelas tertinggi · King bed · TV · mini bar · bathtub + air panas · kamar mandi beratap kaca"),
 ("Family Superior Bungalow", 2_500_000, "../katalog-family-superior/foto/g_eksterior.jpg", "center 50%", "6 org (maks. 8)",
  "2 lantai · 2 kamar mandi · 1 tempat tidur besar + 4 kasur · AC · Wi-Fi · teras"),
]
rp = lambda v: "Rp " + f"{v:,}".replace(",", ".")
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
.pg{position:relative;width:1080px;height:1600px;margin:20px auto;background:#FBF4EC;color:#3A2819;overflow:hidden;text-shadow:0 1px 0 rgba(255,255,255,.9)}
.frame{position:absolute;inset:24px;border:1.5px solid rgba(138,95,72,.35)}
.hd{text-align:center;padding-top:62px}.hd img{width:230px}
.caps{font-weight:700;letter-spacing:.28em;text-transform:uppercase;color:#7A5038}
h1{font-family:'Playfair Display',serif;font-weight:500;font-size:64px;line-height:1.05;margin-top:12px}
h1 i{color:#94532B}
.sub{font-size:20px;margin-top:10px;color:#5A3E31}
.list{position:absolute;left:64px;right:64px;top:350px}
.row{display:flex;gap:24px;align-items:center;padding:16px 0;border-bottom:1.5px solid rgba(138,95,72,.25)}
.row:first-child{border-top:1.5px solid rgba(138,95,72,.25)}
.ph{flex:0 0 210px;height:150px;border-radius:8px;overflow:hidden}.ph img{width:100%;height:100%;object-fit:cover}
.info{flex:1;min-width:0}
.top{display:flex;justify-content:space-between;align-items:baseline;gap:12px}
.nm{font-family:'Playfair Display',serif;font-size:33px;line-height:1.1}
.pr{font-weight:700;font-size:30px;color:#A2461F;white-space:nowrap}
.cap{font-size:15px;font-weight:700;letter-spacing:.14em;text-transform:uppercase;color:#4E7F91;margin-top:6px}
.pn{font-size:13px;font-weight:600;color:#7A5038;letter-spacing:.06em;text-transform:none}
.fac{font-size:18px;line-height:1.4;color:#5A3E31;margin-top:6px}
.notes{position:absolute;left:64px;right:64px;top:1300px;display:grid;grid-template-columns:1fr 1fr;gap:12px 24px;font-size:19px;color:#3A2819;padding:20px 26px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.notes div::before{content:"";display:inline-block;width:9px;height:9px;border-radius:50%;background:#D9703F;margin-right:12px;vertical-align:2px}
.notes b{color:#A2461F}
.ft{position:absolute;left:64px;right:64px;bottom:60px;text-align:center;padding-top:18px;border-top:1.5px solid rgba(138,95,72,.45)}
.ft .w{font-family:'Playfair Display',serif;font-size:30px;margin-top:6px}.ft .w i{color:#94532B}
"""
rows = "".join(f'''<div class="row"><div class="ph"><img src="{img}" style="object-position:{pos}"></div><div class="info">
  <div class="top"><div class="nm">{nm}</div><div class="pr">{rp(pr)}</div></div>
  <div class="cap">{cap} <span class="pn">· per malam</span></div><div class="fac">{fac}</div></div></div>''' for nm, pr, img, pos, cap, fac in ROOMS)
HTML = f'''<div class="pg" id="daftar-harga"><div class="frame"></div>
<div class="hd"><img src="{LOGO}"><div class="caps" style="font-size:16px;margin-top:14px">SunaRi Beach Resort Selayar</div>
<h1>Harga <i>Kamar</i></h1><div class="sub">Per malam · sudah termasuk sarapan</div></div>
<div class="list">{rows}</div>
<div class="notes">
  <div>Extra bed <b>Rp 150.000</b> / malam</div><div>Check-in 14.00 · Check-out 12.00 WITA</div>
  <div>Sarapan, AC &amp; Wi-Fi di semua kamar</div><div>Perlengkapan mandi &amp; handuk lengkap</div></div>
<div class="ft"><div class="caps" style="font-size:14px">Informasi &amp; reservasi</div>
  <div class="w"><i>WhatsApp</i> 0813-4150-4973 · 0821-8903-3044</div></div></div>'''
(H / "daftar_harga.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}</body></html>')
print("ok")
