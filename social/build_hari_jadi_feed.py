"""Feed carousel Instagram (1080x1350) Hari Jadi ke-421 Kabupaten Kepulauan Selayar (29 November 2026), 10 slide, gaya feed SunaRi.
Tanpa jualan/harga. Foto: hasil color grading tema SunaRi di assets/photos/graded/.
Run: python3 social/build_hari_jadi_feed.py && node social/render_hari_jadi_feed.js -> social/hari-jadi-selayar-feed/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
exec((H / "build_vipsuperior.py").read_text().split("KICK =")[0].replace("__file__", repr(str(H / "build_vipsuperior.py"))))
P = "hari-jadi-selayar-feed/foto/"; N = 10; KICK = "Hari Jadi Selayar ke-421"
CSS += """
.big{font-family:'Playfair Display',serif;font-size:230px;line-height:.9;color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.45)}
.ph.grid{display:grid;gap:10px;background:#FBF4EC}
.ph.grid>div{position:relative;overflow:hidden}
.ph.grid>div img{width:100%;height:100%;object-fit:cover}
.ph.grid .cap{position:absolute;left:0;right:0;bottom:0;padding:40px 20px 14px;color:#FBF4EC;font-family:'Playfair Display',serif;font-size:32px;text-shadow:0 2px 8px rgba(0,0,0,.55);background:linear-gradient(180deg,rgba(20,12,6,0),rgba(20,12,6,.6))}
.fc .vb{height:520px;background:linear-gradient(0deg,rgba(20,12,6,.7),rgba(20,12,6,0))}
"""
T = []
T.append(f'''<div class="t fc" id="hari-jadi-01"><img class="bgf" src="{P}senja__85-siluet-tirai-senja-persegi-lurus.jpg" style="object-position:15% 50%" alt="">
  <div class="vt"></div><div class="vb"></div>
  <div class="fk">29 November 1605 — 2026</div><div class="fh" style="font-size:96px">Selamat<br>Hari Jadi</div>
  <div class="big" style="position:absolute;left:76px;top:390px">ke-421</div>
  <div class="fs" style="top:620px">Kabupaten Kepulauan Selayar</div>
  <div class="fg">Geser &nbsp;→</div><img class="fl" src="{LOGO_D}" alt=""></div>''')
SL = [
  ([(P + "pantai__02-perahu-nelayan-biru.jpg", "40% 55%", "Dari laut"), (P + "resto__06-bakar-ikan-tuna-bara.jpg", "50% 52%", "ke meja makan")], "", 'Bangga <em>pangan lokal</em>',
  'Tema tahun ini: “Pangan Lokal Mendukung Ketahanan Pangan Nasional”. Dari laut dan kebun Selayar, untuk Indonesia.'),
 (P + "bahuluang__21-laut-toska-dari-kapal.jpg", "50% 70%", 'Laut yang <em>memberi</em>',
  'Air toska, pasir putih, dan karang yang terjaga. Laut Selayar adalah rumah, sumber kehidupan, dan kebanggaan kita.'),
 (P + "bahuluang__29-snorkeling-masker-penuh.jpg", "50% 50%", 'Taman <em>bawah laut</em>',
  'Karang dan ikan warna-warni di perairan Selayar. Jaga bersama, wariskan untuk anak cucu.'),
 ([(P + "bahuluang__51-pantai-barat-teluk-pasir-putih.jpg", "45% 50%", "Bahuluang"), (P + "pantai__03-pulau-di-seberang.jpg", "50% 60%", "Gusung"), (P + "polassi-tambolongan__07-punggung-bukit-nane-dan-teluk.jpg", "50% 50%", "Polassi")], "", 'Pulau-pulau <em>yang memesona</em>',
  'Bahuluang, Gusung, Polassi, Tambolongan. Hanya sebagian kecil dari keindahan Kepulauan Selayar.'),
 (P + "bahuluang__12-berjalan-di-pasir-timbul.jpg", "50% 55%", 'Daratan <em>sesaat</em>',
  'Saat air surut, gosong pasir putih muncul di tengah laut. Keajaiban kecil dari pasang-surut Selayar.'),
 (P + "bahuluang__47-dalam-gua-lipang-stalaktit-rombongan.jpg", "50% 40%", 'Gua yang <em>dibentuk laut</em>',
  'Gua Lipang di Pulau Bahuluang: stalaktit menggantung, lantai pasir putih, sejuk di dalam.'),
 (P + "senja__86-matahari-merah-dua-perahu.jpg", "50% 53%", 'Senja di <em>pesisir barat</em>',
  'Setiap sore matahari tenggelam di depan Pantai Sunari. Hadiah kecil dari Selayar untuk siapa saja yang singgah.'),
 (P + "malam__30-ayunan-kelapa-bintang.jpg", "50% 86%", 'Malam yang <em>tenang</em>',
  'Langit berbintang di antara pohon kelapa. Selayar mengajarkan kita untuk berjalan pelan.'),
]
for k, (img, pos, t, sub) in enumerate(SL, 2):
    if isinstance(img, list):
        cols = "1fr 1fr" if len(img) == 2 else "1.3fr 1fr"
        rows = "1fr" if len(img) == 2 else "1fr 1fr"
        cells = "".join(f'<div style="{"grid-row:1/3" if len(img) == 3 and i == 0 else ""}"><img src="{a}" style="object-position:{b}" alt=""><div class="cap">{c}</div></div>' for i, (a, b, c) in enumerate(img))
        ph = f'<div class="ph grid" style="grid-template-columns:{cols};grid-template-rows:{rows}">{cells}<img class="lg" src="{LOGO_D}" style="position:absolute" alt=""></div>'
    else:
        ph = f'<div class="ph"><img src="{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>'
    T.append(f'''<div class="t" id="hari-jadi-{k:02d}">{ph}
  <div class="kick">{KICK}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#HariJadiSelayar421</span><span>{k:02d} / {N:02d}</span></div></div>''')
T.append(f'''<div class="t" id="hari-jadi-10"><div class="frame"></div>
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:90px;width:280px" alt="">
  <div style="position:absolute;left:100px;right:100px;top:320px;text-align:center;color:#45301F">
    <div style="font-weight:700;font-size:21px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">29 November 2026</div>
    <div class="emb" style="font-family:'Playfair Display',serif;font-size:74px;line-height:1.12;margin-top:16px">Selamat Hari Jadi<br><em style="color:#A0603E">ke-421, Selayar</em></div>
    <div style="width:120px;height:2px;background:#D9703F;margin:30px auto"></div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:36px;line-height:1.45;color:#5A3E31">Dari tepi Pantai Sunari, kami turut merayakan 421 tahun Selayar. Semoga laut dan tanahnya terus memberi berkah untuk kita semua.</div></div>
  <div style="position:absolute;left:100px;right:100px;top:880px;height:250px;border-radius:18px;overflow:hidden"><img src="{P}taman__05-meja-taman-view-laut-gazebo.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 55%" alt=""></div>
  <div style="position:absolute;left:0;right:0;bottom:150px;text-align:center;font-weight:700;font-size:20px;letter-spacing:.26em;text-transform:uppercase;color:#7A5039">Keluarga besar SunaRi Beach Resort Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:96px;text-align:center;font-weight:600;font-size:19px;letter-spacing:.38em;text-transform:uppercase;color:#7A5039">Pantai Sunari · Selayar</div>
  <div style="position:absolute;left:0;right:0;bottom:62px;text-align:center;font-weight:700;font-size:17px;letter-spacing:.2em;color:#C0592C">#HariJadiSelayar421 · #sunarisunsetmoment</div></div>''')
(H / "hari_jadi_feed.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
