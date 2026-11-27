"""Gambar katalog WhatsApp Business: paket 3 Hari 2 Malam di Selayar · Sehari ke Bahuluang.
10 gambar persegi 1080x1080, TANPA HARGA.
Run: python3 whatsapp/katalog-paket-bahuluang/build.py && node whatsapp/katalog-paket-bahuluang/render.js"""
import pathlib
H = pathlib.Path(__file__).parent
PH = "../../services/paket-photos/"
LOGO = "../../assets/logo-sunari-color.png"
LOGO_CREAM = "../../assets/logo-sunari-cream.png"
WA = "+62 821-8903-3044"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@400;500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ccc;font-family:Montserrat,sans-serif;color:#3A2819;-webkit-font-smoothing:antialiased;font-variant-numeric:lining-nums}
.sq{width:1080px;height:1080px;position:relative;overflow:hidden;background:#FBF4EC;margin:20px auto;text-shadow:0 1px 0 rgba(255,255,255,.9)}
.frame{position:absolute;inset:26px;border:1.5px solid rgba(138,95,72,.35);pointer-events:none;z-index:3}
.serif{font-family:'Playfair Display',serif;font-weight:500}
.it{font-style:italic;color:#94532B}
.caps{font-weight:700;text-transform:uppercase;letter-spacing:.24em;color:#7A5038}
.pad{position:absolute;inset:70px 76px}
.head{display:flex;align-items:center;justify-content:space-between}
.head img{width:200px}
.head .caps{font-size:17px;text-align:right;line-height:1.6}
.h1{font-size:66px;line-height:1.08;margin-top:34px;text-shadow:0 1px 0 #fff,0 -1px 0 rgba(90,62,49,.3)}
.lead{font-size:25px;line-height:1.5;margin-top:16px;color:#5A3E31}
.foot{position:absolute;left:76px;right:76px;bottom:62px;display:flex;justify-content:space-between;align-items:center;border-top:1.5px solid rgba(138,95,72,.45);padding-top:18px}
.foot .wa{font-family:'Playfair Display',serif;font-size:30px} .foot .wa i{color:#94532B}
.foot .tag{font-size:16px;font-weight:700;letter-spacing:.18em;color:#A2461F;text-transform:uppercase}
.ph{width:100%;height:100%;object-fit:cover;display:block}
/* 1 sampul */
.cover .bg{position:absolute;inset:0}
.cover .shade{position:absolute;left:0;right:0;bottom:0;height:560px;background:linear-gradient(180deg,rgba(30,20,12,0),rgba(30,20,12,.78))}
.cover .top{position:absolute;top:60px;left:0;right:0;text-align:center}
.cover .top img{width:280px;filter:drop-shadow(0 2px 6px rgba(0,0,0,.35))}
.cover .txt{position:absolute;left:70px;right:70px;bottom:72px;color:#FBF4EC;text-shadow:0 2px 10px rgba(0,0,0,.45);text-align:center}
.cover .txt .k{font-size:19px;font-weight:700;letter-spacing:.3em}
.cover .txt .t{font-size:86px;line-height:1.02;margin-top:12px}
.cover .txt .s{font-size:44px;font-style:italic;margin-top:8px;color:#FDD3A8}
.chips{display:flex;justify-content:center;gap:14px;margin-top:26px;flex-wrap:wrap}
.chips span{font-size:21px;font-weight:600;padding:10px 22px;border-radius:30px;background:rgba(251,244,236,.95);color:#3A2819;text-shadow:none}
/* 2 termasuk */
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:18px 22px;margin-top:34px}
.it2{display:flex;gap:18px;align-items:flex-start;padding:20px 20px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.ic{flex:0 0 58px;height:58px;border-radius:50%;background:#D9703F;display:flex;align-items:center;justify-content:center}
.ic.b{background:#7BA7B6} .ic.c{background:#A67C64}
.ic svg{width:32px;height:32px;stroke:#fff;fill:none;stroke-width:1.8;stroke-linecap:round;stroke-linejoin:round}
.it2 b{display:block;font-size:24px;line-height:1.2}
.it2 span{display:block;font-size:19px;line-height:1.35;color:#6B4A37;margin-top:4px}
/* 3 destinasi */
.g4{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:30px;height:620px}
.g4 div{position:relative;border-radius:8px;overflow:hidden}
.g4 .lbl{position:absolute;left:0;right:0;bottom:0;padding:40px 18px 16px;color:#FBF4EC;font-family:'Playfair Display',serif;font-size:32px;text-shadow:0 2px 8px rgba(0,0,0,.5);
  background:linear-gradient(180deg,rgba(30,20,12,0),rgba(30,20,12,.65))}
/* 4 alur */
.days{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;margin-top:40px}
.day ul{padding-top:20px}
.day{border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3);padding:0 0 18px;overflow:hidden}
.day .hd{background:#5A3E31;color:#FBF4EC;text-shadow:none;text-align:center;padding:16px 8px}
.day .hd b{display:block;font-family:'Playfair Display',serif;font-size:50px;font-weight:500;line-height:1}
.day .hd span{font-size:15px;font-weight:700;letter-spacing:.2em}
.day ul{list-style:none;padding:16px 20px 0}
.day li{font-size:21px;line-height:1.3;padding:8px 0 8px 22px;position:relative;border-bottom:1px solid rgba(138,95,72,.18)}
.day li:last-child{border-bottom:0}
.day li::before{content:"";position:absolute;left:2px;top:16px;width:9px;height:9px;border-radius:50%;background:#7BA7B6}
.day li.k::before{background:#D9703F} .day li.k{font-weight:700}
.note{margin-top:22px;padding:14px 20px;border-left:5px solid #D9703F;background:#FFFDF9;font-size:20px;line-height:1.4}
.note b{color:#A2461F}
/* 5 penginapan */
.room{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:30px}
.room .p{height:440px;border-radius:8px;overflow:hidden}
.room ul{list-style:none;margin-top:6px}
.room li{font-size:22px;line-height:1.4;padding:9px 0 9px 28px;position:relative}
.room li::before{content:"";position:absolute;left:3px;top:20px;width:11px;height:11px;border-radius:50%;background:#D9703F}
/* 6 pesan */
.steps{list-style:none;counter-reset:s;margin-top:30px}
.steps li{counter-increment:s;position:relative;padding:18px 0 18px 82px;font-size:26px;line-height:1.35;border-bottom:1px solid rgba(138,95,72,.22)}
.steps li::before{content:counter(s);position:absolute;left:0;top:14px;width:56px;height:56px;border-radius:50%;background:#D9703F;color:#fff;text-shadow:none;
  font-weight:700;font-size:26px;display:flex;align-items:center;justify-content:center}
.cta{margin-top:34px;text-align:center;padding:30px 20px;border-radius:10px;background:#5A3E31;color:#FBF4EC;text-shadow:none}
.cta .t{font-family:'Playfair Display',serif;font-size:40px}
.cta .w{font-size:30px;font-weight:700;letter-spacing:.04em;margin-top:8px;color:#FDD3A8}
"""
ICON = {
 "home": '<path d="M3 11l9-7 9 7"/><path d="M5 10v10h14V10"/><path d="M10 20v-6h4v6"/>',
 "food": '<path d="M7 3v8M5 3v5a2 2 0 004 0V3M7 11v10"/><path d="M17 3c-2 0-3 3-3 6s1 4 3 4v8"/>',
 "car": '<path d="M3 16v-4l2-5h14l2 5v4z"/><circle cx="7.5" cy="17" r="1.8"/><circle cx="16.5" cy="17" r="1.8"/>',
 "boat": '<path d="M3 15h18l-3 5H6z"/><path d="M12 3v12M12 4l6 9h-6"/>',
 "fish": '<path d="M3 12c3-5 10-5 14 0-4 5-11 5-14 0z"/><path d="M17 12l4-3v6z"/>',
 "cam": '<rect x="3" y="7" width="18" height="13" rx="2"/><circle cx="12" cy="13.5" r="3.5"/><path d="M8 7l1.5-3h5L16 7"/>',
 "user": '<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
 "ticket": '<path d="M3 8a2 2 0 002-2h14a2 2 0 002 2v2a2 2 0 000 4v2a2 2 0 00-2 2H5a2 2 0 00-2-2v-2a2 2 0 000-4z"/><path d="M14 6v12"/>',
}
def ic(name, cls=""): return f'<div class="ic {cls}"><svg viewBox="0 0 24 24">{ICON[name]}</svg></div>'
def head(right): return f'<div class="head"><img src="{LOGO}"><div class="caps">{right}</div></div>'
def foot(tag="Tanya harga &amp; jadwal via chat"):
    return f'<div class="foot"><div class="wa"><i>WhatsApp</i> {WA}</div><div class="tag">{tag}</div></div>'
def sq(inner, cls=""): return f'<div class="sq {cls}"><div class="frame"></div>{inner}</div>'
S = []

# 1 sampul
S.append(sq(f'''<div class="bg"><img class="ph" src="{PH}hero.jpg" style="object-position:center 55%"></div><div class="shade"></div>
<div class="top"><img src="{LOGO_CREAM}"></div>
<div class="txt"><div class="k">SUNARI BEACH RESORT SELAYAR</div><div class="t serif">3 Hari 2 Malam<br>di Selayar</div><div class="s serif">Sehari ke Bahuluang</div>
<div class="chips"><span>Keluarga 4 Dewasa + 2 Anak</span><span>Semua sudah termasuk</span></div></div>''', "cover"))

# 2 termasuk
items = [("home", "", "Family Superior Bungalow", "2 malam, rumah dua lantai"), ("food", "", "Welcome drink &amp; 8x makan", "Breakfast, lunch, afternoon tea, dinner"),
         ("car", "b", "Antar-jemput", "Bandara / pelabuhan, pergi &amp; pulang"), ("boat", "b", "Kapal &amp; mobil trip", "Resort ⇄ dermaga ⇄ Pulau Bahuluang"),
         ("user", "c", "Guide &amp; tim", "Mendampingi sepanjang trip"), ("fish", "c", "Alat snorkeling &amp; paddleboard", "Masker, snorkel, fins, pelampung"),
         ("ticket", "", "Tiket masuk", "Semua lokasi wisata"), ("cam", "", "Dokumentasi", "Drone, DSLR, underwater · file mentah via Google Drive")]
S.append(sq('<div class="pad">' + head("3 Hari 2 Malam di Selayar<br><span style=\"color:#C0592C\">Yang termasuk</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:30px">Semua sudah <span class="it">kami siapkan</span></div>'
  + '<div class="grid2">' + "".join(f'<div class="it2">{ic(i, c)}<div><b>{t}</b><span>{d}</span></div></div>' for i, c, t, d in items) + '</div></div>' + foot()))

# 3 destinasi
dest = [("pantai", "center 50%", "Pantai Bone Bakka"), ("gua", "center 60%", "Goa Lipang"), ("karang", "center 55%", "Makam Karang"), ("pasir", "center 70%", "Pasir Timbul")]
S.append(sq('<div class="pad">' + head("Sehari ke Bahuluang<br><span style=\"color:#C0592C\">Destinasi trip</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:26px">Empat sorotan <span class="it">Pulau Bahuluang</span></div>'
  + '<div class="g4">' + "".join(f'<div><img class="ph" src="{PH}{k}.jpg" style="object-position:{p}"><div class="lbl">{t}</div></div>' for k, p, t in dest) + '</div></div>' + foot()))

# 4 alur 3 hari
days = [("1", "TIBA &amp; SANTAI", [("k", "Tiba: pesawat 07.00–08.00 atau ferri dari Bira ±12.00"), ("", "Welcome drink &amp; lunch"), ("", "Check-in saat kamar siap"), ("", "Senja di pantai"), ("", "Dinner")]),
        ("2", "TRIP BAHULUANG", [("", "07.00 breakfast, 08.00 berangkat"), ("k", "Pantai Bone Bakka"), ("k", "Goa Lipang"), ("k", "Makam Karang"), ("k", "Pasir Timbul"), ("", "Afternoon tea &amp; dinner")]),
        ("3", "PULANG", [("", "06.00–07.00 check-out"), ("", "Breakfast take away"), ("k", "Diantar ke bandara / pelabuhan")])]
S.append(sq('<div class="pad">' + head("3 Hari 2 Malam di Selayar<br><span style=\"color:#C0592C\">Alur trip</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:26px">Dari tiba <span class="it">sampai pulang</span></div>'
  + '<div class="days">' + "".join(f'<div class="day"><div class="hd"><span>HARI</span><b>{n}</b><span>{t}</span></div><ul>' + "".join(f'<li class="{c}">{x}</li>' for c, x in li) + '</ul></div>' for n, t, li in days) + '</div>'
  + '<div class="note"><b>Catatan:</b> jadwal trip ke Bahuluang menyesuaikan kondisi pasang-surut air laut.</div></div>' + foot()))

# 5 penginapan
S.append(sq('<div class="pad">' + head("SunaRi Beach Resort Selayar<br><span style=\"color:#C0592C\">Penginapan</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:26px">Family <span class="it">Superior Bungalow</span></div>'
  + f'<div class="room"><div class="p"><img class="ph" src="{PH}bungalow.jpg"></div><div class="p"><img class="ph" src="{PH}kamar.jpg"></div></div>'
  + '<ul class="room" style="display:block;list-style:none;margin-top:20px">' + "".join(f'<li style="font-size:24px;line-height:1.4;padding:7px 0 7px 30px;position:relative"><span style="position:absolute;left:4px;top:18px;width:11px;height:11px;border-radius:50%;background:#D9703F"></span>{x}</li>' for x in [
    "Satu rumah dua lantai untuk 4 dewasa + 2 anak", "2 kamar mandi, AC, Wi-Fi, teras pribadi", "Di tepi Pantai Sunari, menghadap senja"]) + '</ul></div>' + foot("Sarapan setiap pagi")))

# 6 cara pesan (tanpa harga)
S.append(sq('<div class="pad">' + head("3 Hari 2 Malam di Selayar<br><span style=\"color:#C0592C\">Cara memesan</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:26px">Pesan dalam <span class="it">3 langkah</span></div>'
  + '<ol class="steps">' + "".join(f"<li>{x}</li>" for x in [
    "Chat kami: sebutkan tanggal kedatangan dan jumlah tamu",
    "Pilih kedatangan: pesawat atau ferri dari Bira",
    "Kami kirim harga, ketersediaan, dan detail pembayaran"]) + '</ol>'
  + f'<div style="height:250px;border-radius:8px;overflow:hidden;margin-top:28px"><img class="ph" src="{PH}pasir2.jpg" style="object-position:center 60%"></div>'
  + f'<div class="cta" style="margin-top:24px"><div class="t">Tanya harga &amp; jadwal</div><div class="w">WhatsApp {WA}</div></div></div>'))

# ---------------------------------------------------------------- tambahan: total 10 gambar
CSS_ADD = """
.ab{display:grid;grid-template-columns:1fr 70px 1fr;margin-top:34px}
.ab .or{display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'Playfair Display',serif;font-style:italic;font-size:28px;color:#94532B}
.ab .or::before,.ab .or::after{content:"";flex:1;border-left:2px dashed #A67C64}
.ab .or span{padding:10px 0}
.opt{border-radius:10px;background:#FFFDF9;box-shadow:inset 0 0 0 2.5px var(--c);padding:24px 24px 26px}
.opt.a{--c:#D9703F} .opt.b{--c:#4E7F91}
.opt .tg{display:flex;align-items:center;gap:12px;font-weight:700;font-size:18px;letter-spacing:.14em;color:var(--c);text-transform:uppercase}
.opt .tg b{width:40px;height:40px;border-radius:50%;background:var(--c);color:#fff;text-shadow:none;display:inline-flex;align-items:center;justify-content:center;font-size:22px;letter-spacing:0}
.opt .tm{font-family:'Playfair Display',serif;font-size:48px;margin:14px 0 10px}
.opt ul{list-style:none} .opt li{font-size:22px;line-height:1.35;padding:7px 0 7px 22px;position:relative}
.opt li::before{content:"";position:absolute;left:2px;top:17px;width:9px;height:9px;border-radius:50%;background:var(--c)}
.joinb{margin-top:26px;text-align:center}
.joinb span{display:inline-block;background:#5A3E31;color:#FBF4EC;text-shadow:none;font-weight:700;font-size:19px;letter-spacing:.14em;padding:12px 26px;border-radius:30px}
.tl{margin-top:26px;position:relative}
.tl .r{display:grid;grid-template-columns:110px 34px 1fr;align-items:center;min-height:48px}
.tl .t{font-weight:700;font-size:22px;color:#C0592C}
.tl .d{width:16px;height:16px;border-radius:50%;background:#7BA7B6;justify-self:center;position:relative;z-index:1;box-shadow:0 0 0 4px #FBF4EC}
.tl .r.k .d{background:#D9703F;width:20px;height:20px}
.tl::before{content:"";position:absolute;left:127px;top:20px;bottom:20px;border-left:2px solid rgba(138,95,72,.35)}
.tl .x{font-size:22px;line-height:1.3} .tl .x b{font-weight:700} .tl .x span{color:#6B4A37;font-size:19px}
.meal{width:100%;border-collapse:collapse;margin-top:26px;font-size:23px}
.meal th{font-size:15px;letter-spacing:.16em;text-transform:uppercase;color:#7A5038;padding:12px 8px;border-bottom:2px solid rgba(138,95,72,.5);text-align:center}
.meal td{padding:16px 8px;border-bottom:1px solid rgba(138,95,72,.25);text-align:center}
.meal th:first-child,.meal td:first-child{text-align:left;font-weight:700}
.meal .ok{color:#D9703F;font-weight:700;font-size:28px} .meal .no{color:#B9A99C}
.ph2{display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-top:26px;height:350px}
.ph2 div{border-radius:8px;overflow:hidden}
.c2{display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:22px}
.c2 h3{font-family:'Playfair Display',serif;font-weight:500;font-size:34px;margin-bottom:8px}
.c2 h3 i{color:#94532B}
.c2 ul{list-style:none} .c2 li{font-size:20px;line-height:1.35;padding:6px 0 6px 22px;position:relative}
.c2 li::before{content:"";position:absolute;left:2px;top:15px;width:8px;height:8px;border-radius:50%;background:#8A5F48}
.tb{display:grid;grid-template-columns:1.25fr 1fr;gap:20px;margin-top:26px;height:350px}
.tl2{display:flex;flex-direction:column;gap:12px}
.tl2>div{flex:1;display:flex;align-items:center;justify-content:space-between;gap:12px;padding:0 20px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.tl2 .k{font-size:14px;font-weight:700;letter-spacing:.2em;color:#7A5038}
.tl2 .s{font-size:17px;color:#6B4A37;margin-top:3px}
.tl2 .v{font-family:'Playfair Display',serif;font-size:32px;white-space:nowrap}
.tp{border-radius:8px;overflow:hidden}
.terms{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:28px}
.terms>div{text-align:center;padding:20px 12px;border-radius:8px;background:#FFFDF9;box-shadow:inset 0 0 0 1.5px rgba(138,95,72,.3)}
.terms .k{font-size:14px;font-weight:700;letter-spacing:.2em;color:#7A5038}
.terms .v{font-family:'Playfair Display',serif;font-size:36px;margin:6px 0 4px}
.terms .s{font-size:18px;color:#6B4A37}
"""
def opt(cls, letter, label, time, items):
    return (f'<div class="opt {cls}"><div class="tg"><b>{letter}</b>{label}</div><div class="tm">{time}</div><ul>'
            + "".join(f"<li>{x}</li>" for x in items) + "</ul></div>")
ARR = sq('<div class="pad">' + head("3 Hari 2 Malam di Selayar<br><span style=\"color:#C0592C\">Kedatangan Hari 1</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:26px">Pilih <span class="it">cara tiba</span></div>'
  + '<div class="ab">' + opt("a", "A", "Pesawat", "07.00 – 08.00", ["Dijemput di Bandara H. Aroeppala", "Kamar siap: langsung check-in", "Belum siap: titip barang &amp; santai di pantai", "Welcome drink, lunch 12.30"])
  + '<div class="or"><span>atau</span></div>'
  + opt("b", "B", "Ferri dari Bira", "± 12.00", ["Dijemput di Pelabuhan Pamatata", "Mobil langsung ke resort", "Welcome drink &amp; lunch setibanya"]) + '</div>'
  + '<div class="joinb"><span>▼ SETELAH TIBA, JADWAL SAMA UNTUK SEMUA TAMU</span></div>'
  + '<div class="note" style="margin-top:22px">Check-in <b>saat kamar siap</b>, paling lambat 14.00.</div></div>' + foot())

D2 = [("07.00", "", "Breakfast", "di resort"), ("08.00", "", "Berangkat ke dermaga", "briefing keselamatan"), ("08.30", "", "Menyeberang", "kapal ke Pulau Bahuluang"),
      ("10.00", "k", "Pantai Bone Bakka", "paddleboard, foto drone &amp; DSLR"), ("11.30", "k", "Goa Lipang", "jelajah goa bersama guide"), ("13.00", "", "Lunch di pulau", ""),
      ("14.00", "k", "Makam Karang", "snorkeling, kamera underwater"), ("15.00", "k", "Pasir Timbul", "pasir putih di tengah laut"), ("16.00", "", "Kembali ke resort", ""),
      ("17.00", "", "Afternoon tea", ""), ("19.00", "", "Dinner", "")]
DAY2 = sq('<div class="pad">' + head("Sehari ke Bahuluang<br><span style=\"color:#C0592C\">Jadwal Hari 2</span>")
  + '<div class="h1 serif" style="font-size:54px;margin-top:22px">Sehari penuh <span class="it">di Bahuluang</span></div>'
  + '<div class="tl" style="margin-top:16px">' + "".join(f'<div class="r {c}"><div class="t">{t}</div><div class="d"></div><div class="x"><b>{a}</b>{f" <span>· {d}</span>" if d else ""}</div></div>' for t, c, a, d in D2) + '</div>'
  + '<div class="note" style="margin-top:12px;font-size:19px;padding:10px 18px"><b>Catatan:</b> jadwal menyesuaikan kondisi pasang-surut air laut.</div></div>' + foot())

ok = '<span class="ok">✓</span>'; no = '<span class="no">–</span>'
FOOD = sq('<div class="pad">' + head("3 Hari 2 Malam di Selayar<br><span style=\"color:#C0592C\">Makan &amp; minum</span>")
  + '<div class="h1 serif" style="font-size:58px;margin-top:26px">Welcome drink <span class="it">&amp; 8x makan</span></div>'
  + '<table class="meal"><tr><th>Hari</th><th>Breakfast</th><th>Lunch</th><th>Afternoon tea</th><th>Dinner</th></tr>'
  + f'<tr><td>Hari 1</td><td>{no}</td><td>{ok}</td><td>{ok}</td><td>{ok}</td></tr>'
  + f'<tr><td>Hari 2</td><td>{ok}</td><td>{ok} <span style="font-size:17px">di pulau</span></td><td>{ok}</td><td>{ok}</td></tr>'
  + f'<tr><td>Hari 3</td><td>{ok} <span style="font-size:17px">take away</span></td><td>{no}</td><td>{no}</td><td>{no}</td></tr></table>'
  + f'<div class="ph2"><div><img class="ph" src="{PH}bakar.jpg" style="object-position:center 55%"></div><div><img class="ph" src="{PH}resto.jpg" style="object-position:center 60%"></div></div>'
  + '</div>' + foot("Air minum selama trip"))

PREP = sq('<div class="pad">' + head("3 Hari 2 Malam di Selayar<br><span style=\"color:#C0592C\">Persiapan &amp; ketentuan</span>")
  + '<div class="h1 serif" style="font-size:54px;margin-top:22px">Sebelum <span class="it">berangkat</span></div>'
  + '<div class="c2"><div><h3>Barang <i>dibawa</i></h3><ul>' + "".join(f"<li>{x}</li>" for x in [
      "Baju renang &amp; baju ganti", "Sunblock, topi, kacamata hitam", "Sandal / sepatu air", "Dry bag untuk barang basah", "Obat pribadi &amp; anti mabuk laut"])
  + '</ul></div><div><h3>Tips <i>keselamatan</i></h3><ul>' + "".join(f"<li>{x}</li>" for x in [
      "Anak wajib pakai pelampung", "Anak selalu didampingi orang tua", "Ikuti arahan guide di goa", "Info guide bila ada yang belum bisa berenang", "Laut tidak aman: trip ditunda"])
  + '</ul></div></div>'
  + '<div class="tb"><div class="tl2">' + "".join(f'<div><div><div class="k">{k}</div><div class="s">{d}</div></div><div class="v">{v}</div></div>' for k, v, d in [
      ("UANG MUKA", "DP 50%", "untuk kunci tanggal"), ("GANTI JADWAL", "Bisa", "sesuai ketersediaan"), ("PEMBATALAN", "Tanpa refund", "setelah DP dibayar")]) + '</div>'
  + f'<div class="tp"><img class="ph" src="{PH}kru_bantu.jpg" style="object-position:center 80%"></div></div>'
  + '</div>' + foot())

S = [S[0], S[1], S[2], ARR, S[3], DAY2, S[4], FOOD, PREP, S[5]]
CSS += CSS_ADD

html = "".join(S)
(H / "katalog.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8"><title>Katalog WhatsApp</title>{FONTS}<style>{CSS}</style></head><body>{html}</body></html>')
print(len(S), "gambar")
