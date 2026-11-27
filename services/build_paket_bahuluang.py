"""Brosur Paket Wisata All Included Bahuluang (Keluarga 4 Dewasa + 2 Anak), A4, gaya SunaRi.
Run: python3 services/build_paket_bahuluang.py && node services/render.js 06_Paket"""
import build_docs as B
from build_docs import header, table, ul, H, FONTS, CSS, GRAIN, SUN, footer, WA

PH = "paket-photos/"
EXTRA = """
.ph{display:block;width:100%;object-fit:cover;border-radius:3px;box-shadow:0 0 0 5px #FBF4EC,0 0 0 6px rgba(138,95,72,.35),2px 4px 10px rgba(90,62,49,.25)}
.hero{position:relative;margin:18px 6px 6px}
.hero .tag{position:absolute;left:0;right:0;bottom:0;padding:34px 22px 14px;border-radius:0 0 3px 3px;color:#FBF4EC;text-shadow:0 1px 6px rgba(40,25,15,.55);
  background:linear-gradient(180deg,rgba(40,25,15,0),rgba(40,25,15,.62));font-family:'Playfair Display',serif;font-style:italic;font-size:16px}
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
TOTAL = 5
pages = []

# ---------------------------------------------------------------- 1. Sampul
p = header("Paket Wisata Keluarga · SunaRi Beach Resort Selayar", 'All Included <span class="it">Bahuluang</span>',
           "Tiga hari dua malam di tepi Pantai Sunari, dengan sehari penuh menjelajah Pulau Bahuluang",
           '<span class="chip"><b>●</b> 3 Hari 2 Malam</span><span class="chip"><b>●</b> 4 Dewasa + 2 Anak</span><span class="chip"><b>●</b> Semua sudah termasuk</span>')
p += f'<div class="hero">{img("hero", 330, "center 55%")}<div class="tag">Pantai Bone Bakka, Pulau Bahuluang</div></div>'
p += '<div class="grid4">' + card("Durasi", "3 Hari", "2 malam menginap") + card("Peserta", "6 Orang", "4 dewasa + 2 anak") + card("Penginapan", "Family Superior", "1 bungalow dua lantai") + card("Harga paket", "Rp 10.000.000", "seluruh rombongan", "color:#A84A24;font-size:17px") + "</div>"
p += '<p class="lead">Anda cukup datang. <b>Penginapan, makan, antar-jemput, kapal, guide, alat snorkeling, dan dokumentasi</b> sudah kami siapkan, supaya keluarga bisa menikmati laut Selayar tanpa repot mengatur apa pun.</p>'
p += '<div class="cols" style="margin-top:14px"><div class="card" style="text-align:center"><h4>Cocok <span class="it">untuk</span></h4><p>Keluarga dengan anak yang ingin liburan pantai, laut, dan petualangan ringan.</p></div>' \
     '<div class="card" style="text-align:center"><h4>Sorotan <span class="it">trip</span></h4><p>Pantai Bone Bakka, Goa Lipang, snorkeling di Makam Karang, dan berjalan di Pasir Timbul Bahuluang.</p></div></div>'
pages.append(p)

# ---------------------------------------------------------------- 2. Yang didapat
p = mini("Yang Anda dapatkan")
p += '<h2><span class="n">01</span>Penginapan <span class="it">&amp; transportasi</span></h2>'
p += f'''<div class="cols" style="align-items:flex-start"><div>{img("bungalow", 150)}<div class="cap">Family Superior Bungalow</div></div><div>
{ul(["<b>Family Superior Bungalow</b> selama 2 malam: satu rumah dua lantai, cukup untuk 4 dewasa dan 2 anak.",
     "Check-in Hari 1 pukul 14.00, check-out Hari 3 pukul 12.00.",
     "<b>Antar-jemput bandara atau pelabuhan</b> saat tiba dan pulang, dari dan ke mana pun di Selayar.",
     "<b>Mobil</b> dari resort ke dermaga dan kembali pada hari trip.",
     "<b>Kapal</b> pulang-pergi ke Pulau Bahuluang, lengkap dengan awak kapal."])}</div></div>'''
p += '<h2><span class="n">02</span>Makan <span class="it">&amp; minum</span></h2><div class="sub">9 kali makan selama tiga hari, ditambah air minum untuk seluruh rombongan saat trip Bahuluang.</div>'
ok = "✓"; no = "–"
p += '<div class="mealtbl big">' + table(["Hari", "Breakfast", "Lunch", "Afternoon tea", "Dinner"], [
    ("Hari 1", no, ok, ok, ok), ("Hari 2", ok, ok + " (di pulau)", ok, ok), ("Hari 3", ok, ok, no, no)], right_from=1) + "</div>"
p += '<h2><span class="n">03</span>Trip sehari <span class="it">ke Pulau Bahuluang</span></h2>'
p += '<div class="cols"><div>' + ul([
    "<b>Guide &amp; tim</b> mendampingi dari berangkat sampai kembali, termasuk saat masuk goa dan snorkeling.",
    "<b>Tiket masuk</b> semua lokasi, termasuk Pasir Timbul.",
    "<b>Alat snorkeling lengkap</b> untuk 6 orang: masker, snorkel, fins, dan pelampung."]) + '</div><div>' + ul([
    "<b>Paddleboard</b> untuk dicoba bergantian di Pantai Bone Bakka.",
    "<b>Dokumentasi lengkap:</b> foto dan video drone, kamera DSLR, serta kamera underwater.",
    "<b>Air minum</b> untuk seluruh rombongan selama trip."]) + '</div></div>'
p += '<div class="grid3" style="grid-template-columns:repeat(4,1fr);gap:14px;margin-top:14px">' + "".join(f'<div>{img(k, 85, pos)}<div class="cap">{c}</div></div>' for k, pos, c in [
    ("pantai", "center 50%", "Pantai Bone Bakka"), ("gua", "center 60%", "Goa Lipang"), ("karang", "center 55%", "Makam Karang"), ("pasir", "center 70%", "Pasir Timbul")]) + '</div>'
pages.append(p)

# ---------------------------------------------------------------- 3. Jadwal Hari 1-2
p = mini("Jadwal perjalanan")
p += '<div class="sub" style="margin:8px 0 0">Jam di bawah adalah perkiraan. Jadwal kami sesuaikan dengan jam penerbangan Anda serta kondisi cuaca dan laut pada hari itu.</div>'
p += '<h2 style="margin-top:12px"><span class="n">HARI 01</span>Tiba di Selayar <span class="it">&amp; bersantai</span></h2><div class="sub">Hari pertama dibuat santai agar keluarga bisa beristirahat setelah perjalanan.</div>'
p += sched([("Siang", "Penjemputan di bandara / pelabuhan", "Tim kami menjemput, lalu mengantar ke resort"),
            ("12.30", "Lunch", "Makan siang setibanya di Selayar"),
            ("14.00", "Check-in SunaRi Beach Resort", "Masuk ke Family Superior Bungalow, istirahat"),
            ("16.00", "Afternoon tea", "Teh/kopi dan kudapan sore"),
            ("Sore", "Acara bebas", "Jalan di pantai, berenang, atau menikmati matahari terbenam"),
            ("19.00", "Dinner", "Makan malam, lalu istirahat untuk trip besok")])
p += '<h2 style="margin-top:20px"><span class="n">HARI 02</span>Trip sehari <span class="it">ke Pulau Bahuluang</span></h2><div class="sub">Hari utama liburan Anda. Berangkat pagi agar laut masih tenang dan waktu di pulau lebih panjang.</div>'
p += sched([("06.30", "Breakfast", "Sarapan di resort"),
            ("07.30", "Berangkat ke dermaga", "Naik mobil; guide memberi pengarahan singkat soal jadwal dan keselamatan"),
            ("08.00", "Menyeberang ke Pulau Bahuluang", "Naik kapal, pelampung tersedia untuk semua peserta"),
            ("09.30", "Pantai Bone Bakka", "Bermain di pantai, mencoba paddleboard, foto dan video drone &amp; DSLR"),
            ("11.00", "Goa Lipang", "Menjelajah goa bersama guide; jalan pelan dan ikuti arahan guide"),
            ("12.30", "Lunch di pulau", "Makan siang dan minum bersama rombongan"),
            ("13.30", "Makam Karang", "Snorkeling melihat karang dan ikan, didampingi tim, dokumentasi underwater"),
            ("14.30", "Pasir Timbul Bahuluang", "Berjalan di gosong pasir putih di tengah laut; waktunya mengikuti pasang-surut, kapten memilih saat air paling pas"),
            ("15.30", "Kembali ke Selayar", "Naik kapal ke dermaga, lalu mobil ke resort"),
            ("16.30", "Afternoon tea", "Bersantai setelah seharian di laut"),
            ("19.00", "Dinner", "Makan malam di resort")])
pages.append(p)

# ---------------------------------------------------------------- 4. Hari 3, harga, pemesanan
p = mini("Kepulangan &amp; harga")
p += '<h2 style="margin-top:12px"><span class="n">HARI 03</span>Kepulangan</h2><div class="sub">Pagi masih bisa dinikmati sebelum pulang.</div>'
p += sched([("07.00", "Breakfast", "Sarapan di resort"),
            ("Pagi", "Acara bebas", "Bermain di pantai terakhir kali, lalu berkemas"),
            ("12.00", "Lunch &amp; check-out", "Makan siang, lalu check-out dari bungalow"),
            ("Siang", "Antar ke bandara / pelabuhan", "Tim mengantar ke bandara atau pelabuhan; trip selesai")])
p += '<h2><span class="n">04</span>Harga <span class="it">paket</span></h2>'
p += '''<div class="card big-price"><div class="caps" style="font-size:10px">All Included Bahuluang 3H2M · 4 dewasa + 2 anak</div><div class="v">Rp 10.000.000</div>
<div style="font-size:12px">untuk seluruh rombongan (6 orang), bukan per orang &nbsp;·&nbsp; setara ± Rp 1.667.000 per orang</div></div>'''
p += '<div class="cols" style="margin-top:6px"><div><h2><span class="n">05</span>Tidak <span class="it">termasuk</span></h2>' + ul([
    "Tiket pesawat atau kapal ke Selayar pulang-pergi",
    "Pengeluaran pribadi: laundry, minibar, makanan/minuman di luar jadwal, oleh-oleh",
    "Tip untuk guide dan kru (sukarela)", "Asuransi perjalanan"], "no") + '</div><div><h2><span class="n">06</span>Cara <span class="it">pemesanan</span></h2><ol class="steps">' + "".join(f"<li>{x}</li>" for x in [
    "Hubungi kami dan sebutkan tanggal kedatangan serta jam penerbangan.",
    "Kami cek ketersediaan bungalow dan kapal untuk tanggal tersebut.",
    "Bayar DP untuk mengunci tanggal, lalu lunasi sebelum kedatangan (ketentuan dikonfirmasi saat pemesanan).",
    "Kami kirim konfirmasi beserta kontak guide yang akan menjemput."]) + '</ol></div></div>'
pages.append(p)

# ---------------------------------------------------------------- 5. Persiapan & tanya jawab
p = mini("Persiapan &amp; tanya jawab")
p += f'<div style="margin:14px 6px 0">{img("pasir2", 190, "center 60%")}</div>'
p += '<div class="cols"><div><h2><span class="n">07</span>Barang yang <span class="it">dibawa</span></h2>' + ul([
    "Baju renang dan baju ganti (bawa lebih untuk anak)", "Sunblock, topi, kacamata hitam", "Sandal air atau sepatu air, nyaman untuk pantai dan goa",
    "Handuk kecil dan dry bag/kantong plastik untuk baju basah", "Obat pribadi, termasuk obat anti mabuk laut bila perlu", "Kartu identitas dan uang tunai secukupnya"], "dot") + \
     '</div><div><h2><span class="n">08</span>Tips <span class="it">keselamatan</span></h2>' + ul([
    "Anak wajib memakai pelampung di kapal, saat snorkeling, dan paddleboard.", "Anak selalu didampingi orang tua dan diawasi guide selama di air.",
    "Di Goa Lipang, jalan pelan dan ikuti jalur dari guide.", "Beri tahu guide bila ada peserta yang belum bisa berenang atau punya kondisi kesehatan tertentu.",
    "Bila cuaca atau gelombang tidak aman, trip dipindah ke hari lain atau jadwalnya diubah."], "dot") + '</div></div>'
p += '<h2><span class="n">09</span>Tanya <span class="it">jawab</span></h2><div class="cols"><div>'
p += '<div class="qa"><b>Apakah anak yang belum bisa berenang boleh snorkeling?</b>Boleh, dengan pelampung dan didampingi orang tua serta tim kami. Anak juga bisa bermain di pantai bila tidak ingin turun ke air.</div>'
p += '<div class="qa"><b>Kapan hasil dokumentasi diterima?</b>Foto dan video drone, DSLR, dan underwater kami kirim setelah trip selesai.</div></div><div>'
p += '<div class="qa"><b>Bagaimana bila cuaca buruk di hari trip?</b>Kami atur ulang jadwal, misalnya menukar kegiatan Hari 2 dengan Hari 3 bila memungkinkan.</div>'
p += '<div class="qa"><b>Apakah Pasir Timbul selalu muncul?</b>Pasir Timbul muncul saat air surut. Kapten mengatur urutan kunjungan hari itu agar rombongan tiba saat airnya pas.</div>'
p += '<div class="qa"><b>Apakah bisa menambah peserta?</b>Bisa, hubungi kami untuk penyesuaian harga dan kamar.</div></div></div>'
p += '<div class="card" style="margin-top:12px;text-align:center"><h4>Siap <span class="it">berangkat?</span></h4><p>Kirim tanggal kedatangan dan jam penerbangan Anda lewat WhatsApp <b>' + WA + '</b>. Kami bantu atur sisanya, dan hari Anda berakhir dengan senja di Pantai Sunari.</p></div>'
pages.append(p)

html = "".join(page(x, i + 1, TOTAL) for i, x in enumerate(pages))
assert len(pages) == TOTAL
(H / "06_Paket_All_Included_Bahuluang.html").write_text(
    f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Paket All Included Bahuluang</title>{FONTS}<style>{CSS}{EXTRA}</style></head><body>{html}</body></html>')
print("ok", len(pages), "halaman")
