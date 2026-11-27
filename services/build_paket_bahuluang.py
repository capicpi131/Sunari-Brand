"""Brosur Paket Wisata All Included Bahuluang (Keluarga 4 Dewasa + 2 Anak), A4, gaya SunaRi.
Run: python3 services/build_paket_bahuluang.py && node services/render.js 06_Paket"""
import build_docs as B
from build_docs import header, table, ul, H, FONTS, CSS, GRAIN, SUN, footer, WA

PH = "paket-photos/"
EXTRA = """
.ph{display:block;width:100%;object-fit:cover;border-radius:3px;box-shadow:0 0 0 5px #FBF4EC,0 0 0 6px rgba(138,95,72,.35),2px 4px 10px rgba(90,62,49,.25)}
.hero{position:relative;margin:18px 6px 6px}
.hero .tag{text-align:center;margin-top:12px;color:#94532B;font-family:'Playfair Display',serif;font-style:italic;font-size:14px;text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.3)}
.rule svg circle{fill:#E08A4F}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin:16px 6px 4px}
.grid4{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:16px}
.cap{font-size:10px;text-align:center;margin-top:9px;letter-spacing:.06em;color:#8A5F48;font-style:italic;font-family:'Playfair Display',serif;font-size:12px}
.mini{display:flex;align-items:center;justify-content:space-between;margin-bottom:4px}
.mini img{width:118px;filter:drop-shadow(0 1px 0 rgba(255,255,255,.95)) drop-shadow(1px 2px 2px rgba(60,40,30,.3))}
.mini .caps{font-size:9.5px;text-align:right;line-height:1.7}
.lead{font-family:'Playfair Display',serif;font-size:15.5px;line-height:1.65;text-align:center;margin:18px 14px 4px}
.lead b{color:#A84A24;font-weight:500}
.big-price{text-align:center;padding:22px 10px}
.big-price .v{font-family:'Playfair Display',serif;font-size:40px;font-weight:500;color:#A84A24;margin:4px 0 2px}
td.c,th.c{text-align:center}
.qa{font-size:12.5px;line-height:1.55;margin-bottom:9px} .qa b{display:block;font-weight:700;color:#45301F}
.steps{list-style:none;counter-reset:s;font-size:13px;line-height:1.5}
.steps li{counter-increment:s;position:relative;padding:5px 0 5px 34px}
.steps li::before{content:counter(s);position:absolute;left:0;top:4px;width:23px;height:23px;border-radius:50%;text-align:center;line-height:23px;font-weight:700;font-size:11px;color:#FBF4EC;
  background:radial-gradient(circle at 35% 30%,#FDB15D,#E07A4B 75%);box-shadow:0 1px 0 rgba(255,255,255,.9),.5px 1px 2px rgba(90,62,49,.4);text-shadow:none}
.itn.tight td{padding:6px 6px;font-size:12.5px;line-height:1.35} .itn.tight .t{width:84px}
.mealtbl.big td{padding:7px 6px;font-size:13px}
/* teks timbul: warna solid, highlight putih tajam di bawah + bayangan tipis di atas (tanpa blur, tanpa gradasi) */
.page{color:#3A2819;text-shadow:0 1px 0 rgba(255,255,255,.9)}
.page>.paper{background:none}
.hd h1,h2,.card h4,.ft .wa,.price .v,.big-price .v,.lead{color:#3A2819;text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.30)}
.hd h1 .it,h2 .it,.card h4 .it,.ft .wa span{background:none;-webkit-background-clip:border-box;background-clip:border-box;color:#94532B;filter:none;
  text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.35)}
.it{color:#94532B}
.big-price .v,.lead b{color:#A2461F}
.caps{color:#7A5038}
ul.l.ok li::before{background:#D9703F;box-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.3)}
.steps li::before{background:#D9703F;box-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.35)}
/* pilihan kedatangan: A pesawat / B ferri, dipisah jelas */
.arr{border:1.5px dashed #A67C64;border-radius:6px;padding:10px 12px 12px;margin-top:6px}
.arr .hd2{text-align:center;font-weight:700;font-size:9.5px;letter-spacing:.2em;color:#7A5038;margin-bottom:8px}
.arr .opts{display:grid;grid-template-columns:1fr 46px 1fr;align-items:stretch}
.arr .or{display:flex;flex-direction:column;align-items:center;justify-content:center}
.arr .or::before,.arr .or::after{content:"";flex:1;border-left:1.5px dashed #A67C64}
.arr .or span{font-family:'Playfair Display',serif;font-style:italic;font-size:13px;color:#94532B;padding:5px 0}
.arr .opt{border-radius:4px;padding:9px 12px 10px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px var(--c),0 1px 0 #fff}
.arr .opt.a{--c:#D9703F} .arr .opt.b{--c:#4E7F91}
.arr .tag2{display:flex;align-items:center;gap:8px;font-weight:700;font-size:10px;letter-spacing:.14em;color:var(--c);text-transform:uppercase}
.arr .tag2 b{width:22px;height:22px;border-radius:50%;background:var(--c);color:#fff;text-shadow:none;display:inline-flex;align-items:center;justify-content:center;font-size:12px;letter-spacing:0}
.arr .tm2{font-family:'Playfair Display',serif;font-size:20px;margin:4px 0 3px;color:#3A2819}
.arr ul{list-style:none;font-size:11.5px;line-height:1.4} .arr li{padding:1.5px 0 1.5px 12px;position:relative}
.arr li::before{content:"";position:absolute;left:1px;top:7.5px;width:5px;height:5px;border-radius:50%;background:var(--c)}
.join{text-align:center;margin:8px 0 2px;font-weight:700;font-size:10px;letter-spacing:.16em;color:#FBF4EC;text-shadow:none}
.join span{display:inline-block;background:#5A3E31;border-radius:14px;padding:5px 14px}
.flow .arr{margin-top:0;padding:8px 10px 10px} .flow .arr ul{font-size:10.5px} .flow .arr .tm2{font-size:17px}
.flow .join{margin:0}
/* alur trip */
.flow .day{display:flex;gap:14px;margin-top:16px}
.flow .lbl{flex:0 0 70px;width:70px;border-radius:4px;background:#5A3E31;color:#FBF4EC;text-shadow:none;display:flex;flex-direction:column;align-items:center;justify-content:center;
  font-weight:700;font-size:9.5px;letter-spacing:.2em;text-align:center;padding:8px 4px}
.flow .lbl b{display:block;font-family:'Playfair Display',serif;font-size:30px;letter-spacing:0;font-weight:500;line-height:1}
.flow .lbl i{font-style:normal;font-weight:500;letter-spacing:.05em;font-size:9px;margin-top:6px;line-height:1.3;opacity:.85}
.flow .rows{flex:1;display:flex;flex-direction:column;gap:12px}
.flow .row{display:grid;grid-template-columns:repeat(4,1fr);column-gap:34px}
.flow .st{position:relative;text-align:center;padding:9px 5px 8px;border-radius:4px;
  box-shadow:inset 1px 1px 2px rgba(90,62,49,.24),inset -1px -1px 0 rgba(255,255,255,.95),0 1px 0 rgba(255,255,255,.8)}
.flow .st.key{box-shadow:inset 0 0 0 1.5px #D9703F,0 1px 0 #fff}
.flow .ic{width:34px;height:34px;border-radius:50%;margin:0 auto 5px;background:#7BA7B6;display:flex;align-items:center;justify-content:center;box-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.3)}
.flow .st.key .ic{background:#D9703F} .flow .st.home .ic{background:#A67C64}
.flow .ic svg{width:19px;height:19px;stroke:#fff;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.flow .tm{font-weight:700;font-size:10px;letter-spacing:.08em;color:#C0592C}
.flow .ti{font-weight:700;font-size:11.5px;line-height:1.25;margin-top:1px}
.flow .ds{font-size:9.5px;line-height:1.3;margin-top:2px;color:#6B4A37}
.flow .st .nx{position:absolute;right:-34px;top:18px;width:34px;text-align:center;font-size:22px;line-height:1;color:#A67C64;font-weight:700}
.flow .st .nx small{display:block;font-size:7.5px;letter-spacing:.04em;text-transform:uppercase;font-weight:700;color:#4E7F91;margin-top:1px}
.flow .turn{text-align:right;font-size:9.5px;font-weight:600;color:#A67C64;letter-spacing:.06em;margin:-6px 4px -4px}
.legend{display:flex;justify-content:center;flex-wrap:wrap;gap:20px;margin-top:16px;font-size:10.5px}
.legend span{display:flex;align-items:center;gap:6px} .legend i{width:12px;height:12px;border-radius:50%;display:inline-block}
.mealtbl td,.mealtbl th{text-align:center} .mealtbl td:first-child,.mealtbl th:first-child{text-align:left}
"""

def page(inner, n, total):
    return f'<div class="page"><div class="frame"></div><div class="frame2"></div>{inner}{footer(n, total)}</div>'
def mini(title):
    return f'<div class="mini"><img src="../assets/logo-sunari-color.png"><div class="caps">Paket Wisata All Included Bahuluang<br><span style="color:#C0592C">{title}</span></div></div><div class="rule" style="margin:2px 0 4px"><i style="width:100%"></i></div>'
def img(name, h, pos="center"):
    return f'<img class="ph" src="{PH}{name}.jpg" style="height:{h}px;object-position:{pos}">'
def card(k, v, s="", color=""):
    return f'<div class="card price"><div class="caps" style="font-size:8.5px">{k}</div><div class="v" style="font-size:19px;{color}">{v}</div><div style="font-size:10.5px;margin-top:2px">{s}</div></div>'
def sched(rows):
    return '<div class="itn tight"><table><tr><th>Waktu</th><th>Kegiatan</th><th>Keterangan</th></tr>' + "".join(
        f'<tr><td class="t">{t}</td><td class="b">{a}</td><td>{k}</td></tr>' for t, a, k in rows) + "</table></div>"
TOTAL = 6
pages = []

# ---------------------------------------------------------------- 1. Sampul
p = header("Paket Wisata Keluarga · SunaRi Beach Resort Selayar", 'All Included <span class="it">Bahuluang</span>',
           "Tiga hari dua malam di tepi Pantai Sunari, dengan sehari penuh menjelajah Pulau Bahuluang",
           '<span class="chip"><b>●</b> 3 Hari 2 Malam</span><span class="chip"><b>●</b> 4 Dewasa + 2 Anak</span><span class="chip"><b>●</b> Semua sudah termasuk</span>')
p += f'<div class="hero">{img("hero", 310, "center 55%")}<div class="tag">Pantai Bone Bakka, Pulau Bahuluang</div></div>'
p += '<div class="grid4">' + card("Durasi", "3 Hari", "2 malam menginap") + card("Peserta", "6 Orang", "4 dewasa + 2 anak") + card("Penginapan", "Family Superior", "1 bungalow dua lantai") + card("Harga paket", "Rp 10.000.000", "seluruh rombongan", "color:#A84A24;font-size:17px") + "</div>"
p += '<p class="lead">Anda cukup datang. <b>Penginapan, makan, antar-jemput, kapal, guide, alat snorkeling, dan dokumentasi</b> sudah kami siapkan, supaya keluarga bisa menikmati laut Selayar tanpa repot mengatur apa pun.</p>'
p += '<div class="cols" style="margin-top:14px"><div class="card" style="text-align:center"><h4>Cocok <span class="it">untuk</span></h4><p>Keluarga dengan anak yang ingin liburan pantai, laut, dan petualangan ringan.</p></div>' \
     '<div class="card" style="text-align:center"><h4>Sorotan <span class="it">trip</span></h4><p>Pantai Bone Bakka, Goa Lipang, snorkeling di Makam Karang, dan berjalan di Pasir Timbul Bahuluang.</p></div></div>'
pages.append(p)

# ---------------------------------------------------------------- Alur trip (diagram, juga diekspor sebagai png/Alur_Trip_Bahuluang.png)
ICON = {
 "plane": '<path d="M2 14l20-7-7 15-3-6-6-2z"/><path d="M12 16l3-3"/>',
 "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "food": '<path d="M7 3v8M5 3v5a2 2 0 004 0V3M7 11v10"/><path d="M17 3c-2 0-3 3-3 6s1 4 3 4v8"/>',
 "cup": '<path d="M4 9h13v5a5 5 0 01-5 5H9a5 5 0 01-5-5z"/><path d="M17 11h2a2 2 0 010 4h-2"/><path d="M8 3v3M12 3v3"/>',
 "sun": '<circle cx="12" cy="14" r="4"/><path d="M2 18h20M12 5v3M4.5 8l2 2M19.5 8l-2 2"/>',
 "moon": '<path d="M20 15A8 8 0 019 4a8 8 0 1011 11z"/>',
 "car": '<path d="M3 16v-4l2-5h14l2 5v4z"/><circle cx="7.5" cy="17" r="1.8"/><circle cx="16.5" cy="17" r="1.8"/>',
 "boat": '<path d="M3 15h18l-3 5H6z"/><path d="M12 3v12M12 4l6 9h-6"/>',
 "beach": '<path d="M3 20c3-2 6-2 9 0s6 2 9 0"/><path d="M12 17V7"/><path d="M5 9c2-4 12-4 14 0z"/>',
 "cave": '<path d="M2 20c0-9 4-15 10-15s10 6 10 15z"/><path d="M8 20c0-4 2-7 4-7s4 3 4 7"/>',
 "fish": '<path d="M3 12c3-5 10-5 14 0-4 5-11 5-14 0z"/><path d="M17 12l4-3v6z"/>',
 "sand": '<path d="M2 17c3-3 6-3 10-3s7 0 10 3"/><path d="M2 21h20"/><path d="M7 9l1.5-3L10 9M15 8l1.5-3L18 8"/>',
 "bag": '<rect x="4" y="7" width="16" height="13" rx="2"/><path d="M9 7V4h6v3"/>',
}
def step(s, last):
    t, ic, ti, ds = s[:4]; mode = s[4] if len(s) > 4 else ""; cls = s[5] if len(s) > 5 else ""
    if last: arrow = ""
    elif mode == "atau": arrow = '<div class="nx" style="font-family:\'Playfair Display\',serif;font-style:italic;font-size:14px;top:30px;color:#94532B">atau</div>'
    else: arrow = f'<div class="nx">→{f"<small>{mode}</small>" if mode else ""}</div>'
    return f'<div class="st {cls}"><div class="ic"><svg viewBox="0 0 24 24">{ICON[ic]}</svg></div><div class="tm">{t}</div><div class="ti">{ti}</div><div class="ds">{ds}</div>{arrow}</div>'
def flow_rows(steps):
    out = ""
    for i in range(0, len(steps), 4):
        chunk = steps[i:i + 4]
        out += '<div class="row">' + "".join(step(s, j == len(chunk) - 1) for j, s in enumerate(chunk)) + '</div>'
        if i + 4 < len(steps):
            mode = steps[i + 3][4] if len(steps[i + 3]) > 4 else ""
            out += f'<div class="turn">lanjut ke baris berikutnya ↵{(" · " + mode.lower()) if mode else ""}</div>'
    return f'<div class="rows">{out}</div>'
def flow_day(n, sub, steps, before=""):
    rows = flow_rows(steps)
    if before: rows = rows.replace('<div class="rows">', '<div class="rows">' + before, 1)
    return f'<div class="day"><div class="lbl">HARI<b>{n}</b><i>{sub}</i></div>{rows}</div>'
def arrival():
    """Dua pilihan kedatangan Hari 1, dipisah garis putus-putus dan 'atau'."""
    def opt(cls, letter, label, time, items):
        return (f'<div class="opt {cls}"><div class="tag2"><b>{letter}</b>{label}</div><div class="tm2">{time}</div>'
                + "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>")
    a = opt("a", "A", "Tiba dengan pesawat", "07.00 – 08.00",
            ["Dijemput di Bandara H. Aroeppala", "Kamar siap: langsung check-in. Belum siap: titip barang &amp; bersantai di pantai", "Welcome drink setibanya di resort", "Lunch pukul 12.30 di resort"])
    b = opt("b", "B", "Tiba dengan ferri dari Bira", "± 12.00",
            ["Dijemput di Pelabuhan Pamatata", "Perjalanan dengan mobil ke resort", "Welcome drink &amp; lunch setibanya di resort"])
    return (f'<div class="arr"><div class="hd2">PILIH SALAH SATU, SESUAI KEDATANGAN ANDA</div>'
            f'<div class="opts">{a}<div class="or"><span>atau</span></div>{b}</div></div>'
            '<div class="join"><span>▼ SETELAH TIBA, JADWAL SAMA UNTUK SEMUA TAMU</span></div>')
H1 = [("Saat kamar siap", "home", "Check-in", "Paling lambat 14.00", "", "home"),
      ("16.00", "cup", "Afternoon tea", "Teh/kopi &amp; kudapan"),
      ("Sore", "sun", "Senja di pantai", "Acara bebas, main di pantai"),
      ("19.00", "moon", "Dinner", "Istirahat untuk trip besok")]
H2 = [("06.30", "food", "Breakfast", "Sarapan di resort", "Mobil"),
      ("07.30", "car", "Ke dermaga", "Briefing jadwal &amp; keselamatan", "Kapal"),
      ("08.00", "boat", "Menyeberang", "Pelampung untuk semua", "Kapal"),
      ("09.30", "beach", "Pantai Bone Bakka", "Paddleboard, foto drone &amp; DSLR", "Kapal", "key"),
      ("11.00", "cave", "Goa Lipang", "Jelajah goa bersama guide", "", "key"),
      ("12.30", "food", "Lunch di pulau", "Makan &amp; minum bersama", "Kapal"),
      ("13.30", "fish", "Makam Karang", "Snorkeling, kamera underwater", "Kapal", "key"),
      ("14.30", "sand", "Pasir Timbul", "Waktu ikut pasang-surut", "Kapal", "key"),
      ("15.30", "boat", "Kembali", "Kapal ke dermaga, mobil ke resort", "Mobil"),
      ("16.30", "cup", "Afternoon tea", "Bersantai di resort", "", "home"),
      ("19.00", "moon", "Dinner", "Makan malam di resort")]
H3 = [("05.30", "bag", "Bersiap", "Barang dibawa ke mobil", "", "home"),
      ("06.00 – 07.00", "car", "Check-out &amp; berangkat", "Berangkat dari SunaRi", "Mobil", "home"),
      ("Perjalanan", "food", "Breakfast take away", "Sarapan di perjalanan", "Mobil"),
      ("Tiba", "plane", "Pulang", "Diantar ke bandara / pelabuhan", "", "key")]
p = mini("Alur trip")
p += '<h2 style="margin-top:12px">Alur trip <span class="it">dari tiba sampai pulang</span></h2><div class="sub">Baca dari kiri ke kanan, baris demi baris. Jam adalah perkiraan dan mengikuti penerbangan, cuaca, serta pasang-surut.</div>'
FLOW = ('<div class="flow">'
      + flow_day("1", "Tiba &amp; santai", H1, arrival()) +flow_day("2", "Trip Bahuluang", H2) + flow_day("3", "Pulang", H3)
      + '<div class="legend"><span><i style="background:#D9703F"></i>Momen utama</span><span><i style="background:#A67C64"></i>Di resort</span>'
        '<span><i style="background:#7BA7B6"></i>Kegiatan lain</span><span><b style="color:#4E7F91;font-size:9px;letter-spacing:.06em">MOBIL / KAPAL</b> = moda perjalanan</span></div></div>')
p += FLOW
pages.append(p)
# gambar mandiri (png/Alur_Trip_Bahuluang.png): logo, judul, diagram, kontak
EXPORT = f'''<template data-export="Alur_Trip_Bahuluang"><div class="page" style="height:auto;margin:0;padding:40px 46px 34px">
  <div class="frame"></div><div class="frame2"></div>
  <div class="hd"><img src="../assets/logo-sunari-color.png" style="width:150px"><div class="rule"><i></i>{SUN}<i></i></div>
  <div class="caps" style="font-size:10px">Paket Wisata All Included Bahuluang · 4 Dewasa + 2 Anak</div>
  <h1 style="font-size:32px">Alur Trip <span class="it">dari tiba sampai pulang</span></h1>
  <p style="font-size:12px">Baca dari kiri ke kanan, baris demi baris. Jam adalah perkiraan.</p></div>
  {FLOW}
  <div style="text-align:center;margin-top:18px;padding-top:12px;border-top:1px solid rgba(138,95,72,.45)">
  <div class="caps" style="font-size:9px">Informasi &amp; reservasi</div>
  <div style="font-family:'Playfair Display',serif;font-size:19px;margin-top:2px"><span class="it">WhatsApp</span> {WA} · SunaRi Beach Resort Selayar</div></div>
</div></template>'''

# ---------------------------------------------------------------- 2. Yang didapat
p = mini("Yang Anda dapatkan")
p += '<h2><span class="n">01</span>Penginapan <span class="it">&amp; transportasi</span></h2>'
p += f'''<div class="cols" style="align-items:flex-start"><div>{img("bungalow", 130)}<div class="cap">Family Superior Bungalow</div></div><div>
{ul(["<b>Family Superior Bungalow</b> selama 2 malam: satu rumah dua lantai, cukup untuk 4 dewasa dan 2 anak.",
     "Check-in saat kamar siap (paling lambat 14.00); check-out Hari 3 pukul 06.00–07.00.",
     "<b>Antar-jemput bandara atau pelabuhan</b> saat tiba dan pulang, dari dan ke mana pun di Selayar.",
     "<b>Mobil</b> dari resort ke dermaga dan kembali pada hari trip.",
     "<b>Kapal</b> pulang-pergi ke Pulau Bahuluang, lengkap dengan awak kapal."])}</div></div>'''
p += '<h2><span class="n">02</span>Makan <span class="it">&amp; minum</span></h2><div class="sub">Welcome drink saat tiba dan 8 kali makan; Hari 3 hanya breakfast (take away).</div>'
ok = "✓"; no = "–"
p += '<div class="mealtbl big">' + table(["Hari", "Breakfast", "Lunch", "Afternoon tea", "Dinner"], [
    ("Hari 1", no, ok, ok, ok), ("Hari 2", ok, ok + " (di pulau)", ok, ok), ("Hari 3", ok + " (take away)", no, no, no)], right_from=1) + "</div>"
p += '<h2><span class="n">03</span>Trip sehari <span class="it">ke Pulau Bahuluang</span></h2>'
p += '<div class="cols"><div>' + ul([
    "<b>Guide &amp; tim</b> mendampingi dari berangkat sampai kembali, termasuk saat masuk goa dan snorkeling.",
    "<b>Tiket masuk</b> semua lokasi, termasuk Pasir Timbul.",
    "<b>Alat snorkeling lengkap</b> untuk 6 orang: masker, snorkel, fins, dan pelampung."]) + '</div><div>' + ul([
    "<b>Paddleboard</b> untuk dicoba bergantian di Pantai Bone Bakka.",
    "<b>Dokumentasi:</b> foto dan video drone, DSLR, serta underwater; file mentah dikirim lewat Google Drive.",
    "<b>Air minum</b> untuk seluruh rombongan selama trip."]) + '</div></div>'
p += '<div class="grid3" style="grid-template-columns:repeat(4,1fr);gap:14px;margin-top:14px">' + "".join(f'<div>{img(k, 85, pos)}<div class="cap">{c}</div></div>' for k, pos, c in [
    ("pantai", "center 50%", "Pantai Bone Bakka"), ("gua", "center 60%", "Goa Lipang"), ("karang", "center 55%", "Makam Karang"), ("pasir", "center 70%", "Pasir Timbul")]) + '</div>'
pages.append(p)

# ---------------------------------------------------------------- 3. Jadwal Hari 1-2
p = mini("Jadwal perjalanan")
p += '<h2 style="margin-top:12px"><span class="n">HARI 01</span>Tiba di Selayar <span class="it">&amp; bersantai</span></h2><div class="sub">Jam adalah perkiraan, menyesuaikan jam pesawat atau ferri Anda. Kedua pilihan kami jemput.</div>'
p += arrival()
p += sched([("Saat kamar siap", "Check-in", "Paling lambat 14.00; istirahat di Family Superior Bungalow"),
            ("16.00", "Afternoon tea", "Teh/kopi dan kudapan sore"),
            ("Sore", "Acara bebas", "Jalan di pantai, berenang, menikmati senja"),
            ("19.00", "Dinner", "Makan malam, lalu istirahat untuk trip besok")])
p += '<h2 style="margin-top:20px"><span class="n">HARI 02</span>Trip sehari <span class="it">ke Pulau Bahuluang</span></h2><div class="sub">Hari utama liburan Anda. Berangkat pagi agar laut masih tenang dan waktu di pulau lebih panjang.</div>'
p += sched([("06.30", "Breakfast", "Sarapan di resort"),
            ("07.30", "Berangkat ke dermaga", "Naik mobil; guide memberi briefing keselamatan"),
            ("08.00", "Menyeberang", "Naik kapal ke Pulau Bahuluang, pelampung untuk semua"),
            ("09.30", "Pantai Bone Bakka", "Main di pantai, paddleboard, foto drone &amp; DSLR"),
            ("11.00", "Goa Lipang", "Menjelajah goa bersama guide; jalan pelan dan ikuti arahan guide"),
            ("12.30", "Lunch di pulau", "Makan siang dan minum bersama rombongan"),
            ("13.30", "Makam Karang", "Snorkeling bersama tim, dokumentasi underwater"),
            ("14.30", "Pasir Timbul", "Jalan di pasir putih tengah laut; waktu ikut pasang-surut"),
            ("15.30", "Kembali ke Selayar", "Naik kapal ke dermaga, lalu mobil ke resort"),
            ("16.30", "Afternoon tea", "Bersantai setelah seharian di laut"),
            ("19.00", "Dinner", "Makan malam di resort")])
pages.append(p)

# ---------------------------------------------------------------- 4. Hari 3, harga, pemesanan
p = mini("Kepulangan &amp; harga")
p += '<h2 style="margin-top:12px"><span class="n">HARI 03</span>Kepulangan</h2><div class="sub">Berangkat pagi; jam menyesuaikan pesawat atau kapal Anda. Mohon berkemas malam sebelumnya.</div>'
p += sched([("05.30", "Bangun &amp; bersiap", "Barang dibawa ke mobil; sarapan take away kami siapkan"),
            ("06.00 – 07.00", "Check-out &amp; berangkat", "Check-out dari Family Superior Bungalow, berangkat dari SunaRi"),
            ("Perjalanan", "Breakfast take away", "Sarapan dibawa dan dinikmati di perjalanan"),
            ("Tiba", "Antar ke bandara / pelabuhan", "Tim mengantar sampai bandara atau pelabuhan; trip selesai")])
p += '<h2><span class="n">04</span>Harga <span class="it">paket</span></h2>'
p += '''<div class="card big-price"><div class="caps" style="font-size:10px">All Included Bahuluang 3H2M · 4 dewasa + 2 anak</div><div class="v">Rp 10.000.000</div>
<div style="font-size:12px">untuk seluruh rombongan (6 orang), bukan per orang &nbsp;·&nbsp; setara ± Rp 1.667.000 per orang</div></div>'''
p += '<div class="cols" style="margin-top:6px"><div><h2><span class="n">05</span>Tidak <span class="it">termasuk</span></h2>' + ul([
    "Tiket pesawat atau kapal ke Selayar pulang-pergi",
    "Pengeluaran pribadi: laundry, minibar, makanan/minuman di luar jadwal, oleh-oleh",
    "Tip untuk guide dan kru (sukarela)", "Asuransi perjalanan"], "no") + '</div><div><h2><span class="n">06</span>Cara <span class="it">pemesanan</span></h2><ol class="steps">' + "".join(f"<li>{x}</li>" for x in [
    "Hubungi kami dan sebutkan tanggal kedatangan serta jam pesawat atau ferri.",
    "Kami cek ketersediaan bungalow dan kapal untuk tanggal tersebut.",
    "Bayar DP 50% untuk mengunci tanggal, lalu lunasi sisanya sebelum kedatangan.",
    "Kami kirim konfirmasi beserta kontak guide yang akan menjemput."]) + '</ol></div></div>'
p += '<h2><span class="n">07</span>Ketentuan <span class="it">pembayaran</span></h2>'
p += '<div class="grid3" style="margin:6px 0 0">' + "".join(
    f'<div class="card" style="text-align:center"><div class="caps" style="font-size:9px">{k}</div><h4 style="margin-top:4px">{v}</h4><p>{d}</p></div>' for k, v, d in [
    ("Uang muka", "DP 50%", "Dibayar untuk mengunci tanggal; sisanya dilunasi sebelum kedatangan."),
    ("Ganti jadwal", "Bisa", "Tanggal trip dapat dipindah; hubungi kami untuk cek ketersediaan."),
    ("Pembatalan", "Tanpa refund", "Pembayaran yang sudah masuk tidak dapat dikembalikan setelah DP.")]) + '</div>'
pages.append(p)

# ---------------------------------------------------------------- 5. Persiapan & tanya jawab
p = mini("Persiapan &amp; tanya jawab")
p += f'<div style="margin:14px 6px 0">{img("pasir2", 150, "center 60%")}</div>'
p += '<div class="cols"><div><h2><span class="n">08</span>Barang yang <span class="it">dibawa</span></h2>' + ul([
    "Baju renang dan baju ganti (bawa lebih untuk anak)", "Sunblock, topi, kacamata hitam", "Sandal air atau sepatu air, nyaman untuk pantai dan goa",
    "Handuk kecil dan dry bag/kantong plastik untuk baju basah", "Obat pribadi, termasuk obat anti mabuk laut bila perlu", "Kartu identitas dan uang tunai secukupnya"], "dot") + \
     '</div><div><h2><span class="n">09</span>Tips <span class="it">keselamatan</span></h2>' + ul([
    "Anak wajib memakai pelampung di kapal, saat snorkeling, dan paddleboard.", "Anak selalu didampingi orang tua dan diawasi guide selama di air.",
    "Di Goa Lipang, jalan pelan dan ikuti jalur dari guide.", "Beri tahu guide bila ada peserta yang belum bisa berenang atau punya kondisi kesehatan tertentu.",
    "Bila cuaca atau gelombang tidak aman, trip ditunda atau jadwalnya diubah."], "dot") + '</div></div>'
p += '<h2><span class="n">10</span>Tanya <span class="it">jawab</span></h2><div class="cols"><div>'
p += '<div class="qa"><b>Apakah anak yang belum bisa berenang boleh snorkeling?</b>Boleh, dengan pelampung dan didampingi orang tua serta tim kami. Anak juga bisa bermain di pantai bila tidak ingin turun ke air.</div>'
p += '<div class="qa"><b>Kapan hasil dokumentasi diterima?</b>Semua foto dan video (drone, DSLR, underwater) dikirim sebagai file mentah tanpa edit lewat link Google Drive setelah trip selesai.</div></div><div>'
p += '<div class="qa"><b>Bagaimana bila cuaca buruk di hari trip?</b>Kapten dan guide mengatur ulang urutan atau rute di hari itu. Bila laut tidak aman, trip ditunda demi keselamatan dan kami bicarakan penggantinya bersama Anda.</div>'
p += '<div class="qa"><b>Apakah Pasir Timbul selalu muncul?</b>Pasir Timbul muncul saat air surut. Kapten mengatur urutan kunjungan hari itu agar rombongan tiba saat airnya pas.</div>'
p += '<div class="qa"><b>Apakah bisa menambah peserta?</b>Bisa, hubungi kami untuk penyesuaian harga dan kamar.</div></div></div>'
p += '<div class="card" style="margin-top:12px;text-align:center"><h4>Siap <span class="it">berangkat?</span></h4><p>Kirim tanggal kedatangan dan jam pesawat atau ferri Anda lewat WhatsApp <b>' + WA + '</b>. Kami bantu atur sisanya, dan hari Anda berakhir dengan senja di Pantai Sunari.</p></div>'
pages.append(p)

html = "".join(page(x, i + 1, TOTAL) for i, x in enumerate(pages))
assert len(pages) == TOTAL
(H / "06_Paket_All_Included_Bahuluang.html").write_text(
    f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Paket All Included Bahuluang</title>{FONTS}<style>{CSS}{EXTRA}</style></head><body>{html}{EXPORT}</body></html>')
print("ok", len(pages), "halaman")
