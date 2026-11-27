"""Story Instagram (1080x1920) Hari Jadi ke-421 Kabupaten Kepulauan Selayar, 10 frame.
Isi (judul, deskripsi, foto) sama dengan feed social/build_hari_jadi_feed.py; foto dari hari-jadi-selayar-feed/foto/ (grading SunaRi 0.8).
Area aman IG: teks penting di antara y=250 dan y=1650.
Run: python3 social/build_hari_jadi_story10.py && node social/render_hari_jadi_story10.js -> social/hari-jadi-selayar-story/*.png"""
import pathlib, re
H = pathlib.Path(__file__).parent
P = "hari-jadi-selayar-feed/foto/"
LOGO = "../assets/logo-sunari-color.png"; LOGO_D = "../assets/logo-sunari-color-dark.png"
src = (H / "build_hari_jadi_feed.py").read_text()
SL = eval(re.search(r"^SL = (\[.*?^\])", src, re.S | re.M).group(1))
# posisi foto untuk format tegak 9:16
POS = {"resto__06-bakar-ikan-tuna-bara.jpg": "50% 60%", "bahuluang__21-laut-toska-dari-kapal.jpg": "45% 60%", "bahuluang__12-berjalan-di-pasir-timbul.jpg": "50% 50%",
       "senja__86-matahari-merah-dua-perahu.jpg": "50% 50%", "malam__30-ayunan-kelapa-bintang.jpg": "50% 50%",
       "bahuluang__47-dalam-gua-lipang-stalaktit-rombongan.jpg": "50% 45%", "bahuluang__29-snorkeling-masker-penuh.jpg": "50% 45%"}
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400;1,500&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#bbb;font-family:Montserrat,sans-serif}
.s{position:relative;overflow:hidden;width:1080px;height:1920px;margin:30px auto;background:#120c08;color:#FBF4EC}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.split{position:absolute;inset:0;display:grid;gap:8px;background:#FBF4EC}
.split>div{position:relative;overflow:hidden}.split img{width:100%;height:100%;object-fit:cover}
.split .cap{position:absolute;right:36px;top:36px;font-family:'Playfair Display',serif;font-style:italic;font-size:44px;color:#FFF;text-shadow:0 2px 12px rgba(0,0,0,.7)}
.vt{position:absolute;left:0;right:0;top:0;height:560px;background:linear-gradient(180deg,rgba(30,16,8,.7),rgba(30,16,8,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:900px;background:linear-gradient(0deg,rgba(30,14,6,.92),rgba(30,14,6,.72) 55%,rgba(30,14,6,0))}
.top{position:absolute;left:70px;right:70px;top:150px;display:flex;justify-content:space-between;align-items:center}
.top img{width:230px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.5))}
.top .n{font-weight:700;font-size:22px;letter-spacing:.24em;color:#FFF3E2;text-shadow:0 2px 8px rgba(0,0,0,.6)}
.card{position:absolute;left:70px;right:70px;bottom:300px;text-shadow:0 2px 12px rgba(20,8,2,.7)}
.kick{font-weight:700;font-size:24px;letter-spacing:.32em;text-transform:uppercase;color:#FDB15D}
.ttl{font-family:'Playfair Display',serif;font-weight:500;font-size:92px;line-height:1.08;margin-top:14px;color:#FFF}
.ttl em{font-style:italic;color:#FDD3A8}
.sub{font-size:34px;line-height:1.5;color:#FFF3E2;margin-top:24px}
.tag{font-weight:700;font-size:22px;letter-spacing:.14em;color:#FDB15D;margin-top:26px}
.big{font-family:'Playfair Display',serif;font-weight:500;font-size:240px;line-height:.92;color:#FFF}
"""
N = 10
def top(k): return f'<div class="top"><img src="{LOGO_D}" alt=""><div class="n">{k:02d} / {N:02d}</div></div>'
T = []
# 1 sampul
T.append(f'''<div class="s" id="story-hari-jadi-01"><img class="bg" src="{P}senja__85-siluet-tirai-senja-persegi-lurus.jpg" style="object-position:15% 50%" alt="">
  <div class="vt"></div><div class="vb"></div>{top(1)}
  <div class="card" style="bottom:330px;text-align:center">
    <div class="kick">29 November 1605 — 2026</div>
    <div class="ttl" style="font-size:86px;margin-top:26px">Selamat Hari Jadi</div>
    <div class="big">ke-421</div>
    <div class="ttl" style="font-size:56px;margin-top:10px">Kabupaten Kepulauan Selayar</div>
    <div class="tag" style="margin-top:34px">#HariJadiSelayar421</div></div></div>''')
for k, (img, pos, t, sub) in enumerate(SL, 2):
    if isinstance(img, list):
        grid = "grid-template-rows:1fr 1fr" if len(img) == 2 else "grid-template-columns:1fr 1fr;grid-template-rows:1fr 1fr"
        def cell(i, a, c):
            span = "grid-column:1/3;" if len(img) == 3 and i == 2 else ""
            capst = "top:270px;" if i == 0 or (len(img) == 3 and i == 1) else ""
            return f'<div style="{span}"><img src="{a}" style="object-position:{POS.get(a.split("/")[-1], "50% 50%")}" alt=""><div class="cap" style="{capst}">{c}</div></div>'
        bg = f'<div class="split" style="{grid}">{"".join(cell(i, a, c) for i, (a, b, c) in enumerate(img))}</div>'
    else:
        bg = f'<img class="bg" src="{img}" style="object-position:{POS.get(img.split("/")[-1], "50% 50%")}" alt="">'
    T.append(f'''<div class="s" id="story-hari-jadi-{k:02d}">{bg}<div class="vt"></div><div class="vb"></div>{top(k)}
  <div class="card"><div class="kick">Hari Jadi Selayar ke-421</div><div class="ttl">{t}</div><div class="sub">{sub}</div></div></div>''')
# 10 penutup
T.append(f'''<div class="s" id="story-hari-jadi-10" style="background:#FBF4EC;color:#45301F">
  <img src="{LOGO}" style="position:absolute;left:50%;transform:translateX(-50%);top:250px;width:340px" alt="">
  <div style="position:absolute;left:90px;right:90px;top:560px;text-align:center">
    <div style="font-weight:700;font-size:24px;letter-spacing:.32em;text-transform:uppercase;color:#7A5039">29 November 2026</div>
    <div style="font-family:'Playfair Display',serif;font-size:90px;line-height:1.1;margin-top:18px">Selamat Hari Jadi<br><em style="color:#A0603E">ke-421, Selayar</em></div>
    <div style="width:140px;height:2px;background:#D9703F;margin:44px auto"></div>
    <div style="font-family:'Playfair Display',serif;font-style:italic;font-size:42px;line-height:1.45;color:#5A3E31">Dari tepi Pantai Sunari, kami turut merayakan 421 tahun Selayar. Semoga laut dan tanahnya terus memberi berkah untuk kita semua.</div></div>
  <div style="position:absolute;left:90px;right:90px;top:1300px;height:300px;border-radius:22px;overflow:hidden"><img src="{P}taman__05-meja-taman-view-laut-gazebo.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 55%" alt=""></div>
  <div style="position:absolute;left:0;right:0;top:1650px;text-align:center;font-weight:700;font-size:22px;letter-spacing:.24em;text-transform:uppercase;color:#7A5039">Keluarga besar SunaRi Beach Resort Selayar</div>
  <div style="position:absolute;left:0;right:0;top:1700px;text-align:center;font-weight:700;font-size:21px;letter-spacing:.16em;color:#C0592C">#HariJadiSelayar421 · #sunarisunsetmoment</div></div>''')
(H / "hari_jadi_story10.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{"".join(T)}</body></html>')
print(len(T))
