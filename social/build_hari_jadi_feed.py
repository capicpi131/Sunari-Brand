"""Feed carousel Instagram (1080x1350) Hari Jadi ke-421 Kabupaten Kepulauan Selayar (29 November 2026), 6 slide, gaya feed SunaRi.
Tanpa jualan/harga. Foto: hasil color grading tema SunaRi di assets/photos/graded/.
Run: python3 social/build_hari_jadi_feed.py && node social/render_hari_jadi_feed.js -> social/hari-jadi-selayar-feed/*.png"""
import pathlib
H = pathlib.Path(__file__).parent
exec((H / "build_vipsuperior.py").read_text().split("KICK =")[0].replace("__file__", repr(str(H / "build_vipsuperior.py"))))
P = "../assets/photos/graded/"; N = 6; KICK = "Hari Jadi Selayar ke-421"
CSS += """
.big{font-family:'Playfair Display',serif;font-size:230px;line-height:.9;color:#FBF4EC;text-shadow:0 3px 18px rgba(0,0,0,.45)}
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
 (P + "pantai__02-perahu-nelayan-biru.jpg", "50% 55%", 'Bangga <em>pangan lokal</em>',
  'Tema tahun ini: “Pangan Lokal Mendukung Ketahanan Pangan Nasional”. Dari laut dan kebun Selayar, untuk Indonesia.'),
 (P + "bahuluang__51-pantai-barat-teluk-pasir-putih.jpg", "45% 50%", 'Laut yang <em>memberi</em>',
  'Air toska, pasir putih, dan karang yang terjaga. Laut Selayar adalah rumah, sumber kehidupan, dan kebanggaan kita.'),
 (P + "bahuluang__19-batu-berlubang.jpg", "50% 55%", 'Pulau-pulau <em>yang memesona</em>',
  'Bahuluang, Gusung, Polassi, Tambolongan. Hanya sebagian kecil dari keindahan Kepulauan Selayar.'),
 (P + "senja__21-siluet-tamu-tepi-pantai.jpg", "50% 55%", 'Senja di <em>pesisir barat</em>',
  'Setiap sore matahari tenggelam di depan Pantai Sunari. Hadiah kecil dari Selayar untuk siapa saja yang singgah.'),
]
for k, (img, pos, t, sub) in enumerate(SL, 2):
    T.append(f'''<div class="t" id="hari-jadi-{k:02d}"><div class="ph"><img src="{img}" style="object-position:{pos}" alt=""><img class="lg" src="{LOGO_D}" alt=""></div>
  <div class="kick">{KICK}</div><div class="ttl emb">{t}</div><div class="sub">{sub}</div>
  <div class="bt"><span>SunaRi · Selayar</span><span class="h">#HariJadiSelayar421</span><span>{k:02d} / {N:02d}</span></div></div>''')
T.append(f'''<div class="t" id="hari-jadi-06"><div class="frame"></div>
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
