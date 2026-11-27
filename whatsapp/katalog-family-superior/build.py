"""Gambar katalog WhatsApp Business: Family Superior Bungalow. 10 gambar 1080x1080, TANPA HARGA.
Gaya & komponen diambil dari katalog paket Bahuluang (../katalog-paket-bahuluang/build.py).
Run: python3 whatsapp/katalog-family-superior/build.py && node whatsapp/katalog-family-superior/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
base = (H.parent / "katalog-paket-bahuluang" / "build.py").read_text().split("\nS = []")[0]
g = {"__file__": str(H.parent / "katalog-paket-bahuluang" / "build.py")}
exec(base, g)
CSS, ICON, ic, foot, sq, LOGO, LOGO_CREAM, WA, FONTS = (g[k] for k in ("CSS", "ICON", "ic", "foot", "sq", "LOGO", "LOGO_CREAM", "WA", "FONTS"))

# Nomor WhatsApp: nomor baru di atas nomor lama
WA2 = "+62 813-4150-4973"
CSS += ".foot .wa{font-size:24px;line-height:1.35} .foot{padding-top:12px} .cta .w{font-size:26px;margin-top:4px;line-height:1.35} .bul{margin-top:14px!important} .bul li{padding-top:4px!important;padding-bottom:4px!important}"
def foot(tag="Tanya harga &amp; jadwal via chat"):
    return f'<div class="foot"><div class="wa"><div><i>WhatsApp</i> {WA2}</div><div><i>WhatsApp</i> {WA}</div></div><div class="tag">{tag}</div></div>'

F = "foto/"
TAG = "Family Superior Bungalow"
def head(right): return f'<div class="head"><img src="{LOGO}"><div class="caps">{right}</div></div>'
def h1(t): return f'<div class="h1 serif" style="font-size:58px;margin-top:26px">{t}</div>'
def img(k, pos="center"): return f'<img class="ph" src="{F}g_{k}.jpg" style="object-position:{pos}">'

ICON.update({
 "stairs": '<path d="M3 20h5v-5h5v-5h5V5h3"/>',
 "users": '<circle cx="9" cy="8" r="3.5"/><path d="M2 20c0-3.5 3-5.5 7-5.5s7 2 7 5.5"/><circle cx="17" cy="9" r="2.5"/><path d="M17 14c2.8 0 5 1.6 5 4.5"/>',
 "leaf": '<path d="M5 19c0-8 6-14 15-14 0 9-6 15-14 15"/><path d="M5 19l7-7"/>',
 "stone": '<ellipse cx="7" cy="15" rx="4" ry="3"/><ellipse cx="16" cy="16" rx="5" ry="3.5"/><ellipse cx="12" cy="8" rx="3.5" ry="2.5"/>',
 "toilet": '<path d="M7 3h6v7H7z"/><path d="M5 10h12a5 5 0 01-5 5H9l1 6"/>',
 "hanger": '<path d="M12 7a2 2 0 112-2"/><path d="M12 7v1.5L3 15h18l-9-6.5"/>',
 "lamp": '<path d="M8 3h8l3 8H5z"/><path d="M12 11v7M8 21h8"/>',
 "wave": '<path d="M2 12c2.5-2.5 5-2.5 7.5 0s5 2.5 7.5 0 5-2.5 5 0"/><path d="M2 17c2.5-2.5 5-2.5 7.5 0s5 2.5 7.5 0 5-2.5 5 0"/>',
 "bed": '<path d="M3 18v-6a2 2 0 012-2h14a2 2 0 012 2v6"/><path d="M3 15h18M3 18v2M21 18v2"/><path d="M6 10V7a1 1 0 011-1h4a1 1 0 011 1v3"/>',
 "tv": '<rect x="3" y="5" width="18" height="12" rx="1.5"/><path d="M9 21h6M12 17v4"/>',
 "fridge": '<rect x="6" y="3" width="12" height="18" rx="2"/><path d="M6 10h12M9 6v2M9 13v3"/>',
 "snow": '<path d="M12 3v18M4.2 7.5l15.6 9M4.2 16.5l15.6-9"/><path d="M10 4.5l2 1.5 2-1.5M10 19.5l2-1.5 2 1.5"/>',
 "wifi": '<path d="M2.5 9a14 14 0 0119 0M5.5 12.5a9.5 9.5 0 0113 0M8.5 16a5 5 0 017 0"/><circle cx="12" cy="19" r="1"/>',
 "kettle": '<path d="M6 20h11l-1-9H7z"/><path d="M8 11a4 4 0 018 0M16 13h2a2 2 0 010 4h-1.5"/><path d="M11 5h2"/>',
 "desk": '<path d="M3 9h18M5 9v11M19 9v11M9 9v5h6V9"/>',
 "curtain": '<path d="M3 3h18M5 3c0 6 2 10 5 13v5M19 3c0 6-2 10-5 13v5"/>',
 "bath": '<path d="M3 12h18v3a5 5 0 01-5 5H8a5 5 0 01-5-5z"/><path d="M6 12V6a2 2 0 014 0"/><path d="M7 20l-1 2M17 20l1 2"/>',
 "shower": '<path d="M4 21V8a5 5 0 0110 0"/><path d="M11 8h6"/><path d="M12 12v1M15 12v1M18 12v1M13.5 15v1M16.5 15v1"/>',
 "hot": '<path d="M12 3c3 4 5 7 5 10a5 5 0 01-10 0c0-3 2-6 5-10z"/><path d="M12 18a2 2 0 002-2"/>',
 "sun": '<circle cx="12" cy="14" r="4"/><path d="M2 18h20M12 5v3M4.5 8l2 2M19.5 8l-2 2"/>',
 "towel": '<path d="M6 3h12v14H6z"/><path d="M6 17l-1 4h14l-1-4M9 7h6"/>',
 "clock": '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 "pin": '<path d="M12 21s-7-6.5-7-12a7 7 0 0114 0c0 5.5-7 12-7 12z"/><circle cx="12" cy="9" r="2.5"/>',
 "iron": '<path d="M3 17h17a1 1 0 001-1 7 7 0 00-7-7H8"/><path d="M3 17l2-5h9M8 20h10"/>',
})
CSS += """
.big{border-radius:10px;overflow:hidden}
.feat{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:22px}
.feat>div{text-align:center;padding:16px 10px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.feat .ic{margin:0 auto 8px;width:58px} .feat b{display:block;font-size:22px} .feat span{font-size:17px;color:#6B4A37}
.g4i{display:grid;grid-template-columns:repeat(4,1fr);gap:16px 14px;margin-top:30px}
.g4i>div{text-align:center;padding:22px 8px 18px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.g4i .ic{margin:0 auto 10px;width:64px;height:64px;flex:none} .g4i .ic svg{width:34px;height:34px}
.g4i b{display:block;font-size:20px;line-height:1.25} .g4i span{display:block;font-size:15px;color:#6B4A37;margin-top:3px}
.two{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:26px}
.two>div{border-radius:8px;overflow:hidden}
.three{display:grid;grid-template-columns:1.25fr 1fr;grid-template-rows:1fr 1fr;gap:16px;margin-top:26px;height:470px}
.three>div{border-radius:8px;overflow:hidden} .three>div:first-child{grid-row:1/3}
.bul{list-style:none;margin-top:20px} .bul li{font-size:23px;line-height:1.4;padding:6px 0 6px 30px;position:relative}
.bul li::before{content:"";position:absolute;left:4px;top:17px;width:11px;height:11px;border-radius:50%;background:#D9703F}
.info{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:22px}
.info>div{display:flex;gap:16px;align-items:center;padding:13px 20px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.info b{display:block;font-size:24px;line-height:1.2} .info span{display:block;font-size:18px;color:#6B4A37;margin-top:3px}
.near{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:24px}
.near>div{border-radius:8px;overflow:hidden;position:relative;height:268px}
.near .lbl{position:absolute;left:0;right:0;bottom:0;padding:50px 14px 16px;color:#FBF4EC;text-shadow:0 2px 8px rgba(0,0,0,.5);background:linear-gradient(180deg,rgba(30,20,12,0),rgba(30,20,12,.72))}
.near .lbl b{display:block;font-family:'Playfair Display',serif;font-size:30px;font-weight:500;line-height:1.1} .near .lbl span{font-size:16px}
.quote{font-family:'Playfair Display',serif;font-style:italic;font-size:26px;color:#94532B;margin-top:16px;line-height:1.3}
"""
S = []
# 1 sampul
S.append(sq(f"""<div class="bg">{img("eksterior", "center 50%")}</div><div class="shade"></div>
<div class="top"><img src="{LOGO_CREAM}"></div>
<div class="txt"><div class="k">SUNARI BEACH RESORT SELAYAR</div><div class="t serif">Family Superior<br>Bungalow</div><div class="s serif">Satu rumah, dua lantai, semua bersama</div>
<div class="chips"><span>6 orang (maks. 8)</span><span>2 lantai</span><span>Termasuk sarapan</span></div></div>""", "cover"))

# 2 sorotan: dua lantai
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Sorotan utama</span>")
  + h1('Dua lantai <span class="it">untuk keluarga</span>')
  + f'<div class="big" style="height:470px;margin-top:24px">{img("atas4kasur", "center 55%")}</div>'
  + '<div class="feat">' + "".join(f'<div>{ic(i, c)}<b>{t}</b><span>{d}</span></div>' for i, c, t, d in [
      ("bed", "", "Lantai 1", "tempat tidur besar · 2–3 orang"), ("stairs", "c", "Lantai 2", "empat kasur · 4–5 orang"), ("shower", "b", "2 kamar mandi", "di setiap lantai")]) + '</div></div>' + foot()))

# 3 lantai 1
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Lantai 1</span>")
  + h1('Kamar utama <span class="it">di lantai bawah</span>')
  + f'<div class="two" style="height:500px"><div>{img("bawahdepan", "center 55%")}</div><div>{img("bawahsudut", "center 55%")}</div></div>'
  + '<ul class="bul">' + "".join(f"<li>{x}</li>" for x in [
      "Tempat tidur besar untuk 2–3 orang", "AC dan tirai blackout", "Toilet &amp; kamar mandi sendiri"]) + '</ul></div>' + foot()))

# 4 fasilitas (TANPA TV, mini bar, air panas, bathtub)
fac = [("users", "", "6 orang", "maks. 8 dengan extra bed"), ("bed", "", "5 tempat tidur", "1 besar + 4 kasur"), ("snow", "b", "AC", "sejuk"), ("wifi", "b", "Wi-Fi", "di kamar"),
       ("kettle", "c", "Kopi &amp; teh", "dengan kettle"), ("desk", "c", "Meja kerja", "&amp; rias"), ("curtain", "c", "Tirai blackout", "tidur nyenyak"), ("shower", "b", "2 kamar mandi", "lantai 1 &amp; 2"),
       ("towel", "c", "Handuk", "setiap tamu"), ("iron", "c", "Setrika", "atas permintaan"), ("sun", "", "Teras pribadi", "kursi santai"), ("food", "", "Sarapan", "setiap pagi")]
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Fasilitas</span>")
  + h1('Semua yang <span class="it">Anda butuhkan</span>')
  + '<div class="g4i">' + "".join(f'<div>{ic(i, c)}<b>{t}</b><span>{d}</span></div>' for i, c, t, d in fac) + '</div></div>' + foot()))

# 5 lantai 2
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Lantai 2</span>")
  + h1('Empat kasur <span class="it">di bawah atap kayu</span>')
  + f'<div class="two" style="height:500px"><div>{img("ataskettle", "center 55%")}</div><div>{img("atasmeja", "center 55%")}</div></div>'
  + '<ul class="bul">' + "".join(f"<li>{x}</li>" for x in [
      "Empat kasur untuk 4–5 orang", "Atap kayu yang tinggi dan lapang", "Set kopi/teh dengan pemanas air"]) + '</ul></div>' + foot()))

# 6 kamar mandi
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Kamar mandi</span>")
  + h1('Dua kamar mandi, <span class="it">tanpa antre</span>')
  + f'<div class="three"><div>{img("shower", "center 55%")}</div><div>{img("wastafel", "center 50%")}</div><div>{img("toilet", "center 55%")}</div></div>'
  + '<ul class="bul">' + "".join(f"<li>{x}</li>" for x in [
      "Toilet &amp; kamar mandi di lantai 1 dan lantai 2", "Shower, wastafel, toilet duduk", "Perlengkapan mandi &amp; handuk bersih setiap tamu"]) + '</ul></div>' + foot()))

# 7 malam
S.append(sq(f"""<div class="bg">{img("bulan", "center 40%")}</div><div class="shade" style="height:460px"></div>
<div class="txt" style="bottom:80px"><div class="k">FAMILY SUPERIOR BUNGALOW</div><div class="t serif" style="font-size:64px">Malam hangat<br>bersama keluarga</div>
<div class="s serif" style="font-size:30px">Rumah kayu dua lantai di tengah taman</div></div>""", "cover"))

# 8 info menginap + teras
info = [("users", "", "6 tamu", "maks. 8 dengan 2 extra bed (berbayar)"), ("clock", "b", "Check-in 14.00", "check-out 12.00 WITA"),
        ("food", "", "Sarapan", "termasuk setiap pagi"), ("stairs", "c", "2 lantai", "2 kamar mandi"),
        ("car", "b", "Antar-jemput", "bandara / pelabuhan (berbayar)"), ("sun", "", "Teras pribadi", "kumpul sebelum senja")]
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Info menginap</span>")
  + h1('Yang perlu <span class="it">Anda tahu</span>')
  + '<div class="info">' + "".join(f'<div>{ic(i, c)}<div><b>{t}</b><span>{d}</span></div></div>' for i, c, t, d in info) + '</div>'
  + '<div class="quote">Tipe bungalow terbesar di SunaRi, ideal untuk keluarga besar.</div>'
  + f'<div class="two" style="height:270px;margin-top:16px"><div>{img("terassofa", "center 55%")}</div><div>{img("terassamping", "center 55%")}</div></div></div>' + foot()))

# 9 di sekitar bungalow
near = [("senja2", "center 70%", "Senja", "tepat di depan pantai"), ("kayak2", "center 65%", "Kayak", "sewa saat senja"),
        ("ayunan", "center 45%", "Ayunan raksasa", "gratis untuk tamu"), ("resto2", "center 70%", "Bajoy Beach Resto", "makan sambil menikmati senja")]
S.append(sq('<div class="pad">' + head(f"SunaRi Beach Resort Selayar<br><span style=\"color:#C0592C\">Di sekitar bungalow</span>")
  + h1('Selangkah <span class="it">ke Pantai Sunari</span>')
  + '<div class="near">' + "".join(f'<div>{img(k, p)}<div class="lbl"><b>{t}</b><span>{d}</span></div></div>' for k, p, t, d in near) + '</div>'
  + '<div class="note" style="margin-top:16px">Pantai landai &amp; aman untuk anak. Juga tersedia Senja Dinner (pesan H-1) dan tur pulau.</div></div>' + foot()))

# 10 cara pesan
S.append(sq('<div class="pad">' + head(f"{TAG}<br><span style=\"color:#C0592C\">Cara memesan</span>")
  + h1('Pesan dalam <span class="it">3 langkah</span>')
  + '<ol class="steps">' + "".join(f"<li>{x}</li>" for x in [
    "Chat kami: sebutkan tanggal check-in &amp; check-out", "Sebutkan jumlah tamu (dewasa &amp; anak) dan perlu extra bed atau tidak",
    "Kami kirim harga, ketersediaan, dan detail pembayaran"]) + '</ol>'
  + f'<div style="height:250px;border-radius:8px;overflow:hidden;margin-top:28px">{img("eksterior", "center 50%")}</div>'
  + f'<div class="cta" style="margin-top:24px"><div class="t">Tanya harga &amp; ketersediaan</div><div class="w">WhatsApp {WA2}</div><div class="w">WhatsApp {WA}</div></div></div>'))

html = "".join(S)
(H / "katalog.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Katalog Family Superior</title>{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')
print(len(S), "gambar")
