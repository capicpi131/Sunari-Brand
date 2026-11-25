import html
slides=[
("02","Teras untuk <em>jeda</em>","Teras kayu pribadi dengan kursi santai, dikelilingi hijau taman."),
("03","Jendela <em>segitiga</em>","King bed di bawah atap A-frame yang tinggi, cahaya masuk dari jendela segitiga."),
("04","Ada <em>loteng</em> di atas","Ruang terasa lapang, dengan TV, AC, dan tirai blackout."),
("05","Pagi dari <em>atas</em>","Pemandangan kamar dari loteng, pintu terbuka langsung ke teras."),
("06","Bathtub beratap <em>kaca</em>","Bathtub di kamar mandi semi-outdoor beratap kaca, langit terlihat dari dalam."),
("07","Air <em>panas &amp; dingin</em>","Rain shower dengan air panas, satu-satunya tipe kamar di SunaRi yang punya air panas."),
("08","Detail yang <em>rapi</em>","Wastafel kayu dengan cermin besar dan tanaman hijau."),
("09","Lapang &amp; <em>terang</em>","Toilet duduk dan area wastafel, terpisah rapi di dalam kamar mandi."),
]
CSS="""
@font-face{font-family:PF;font-weight:400;font-style:normal;src:url(assets/fonts/playfair-display-latin-400-normal.woff2)}
@font-face{font-family:PF;font-weight:400;font-style:italic;src:url(assets/fonts/playfair-display-latin-400-italic.woff2)}
@font-face{font-family:PF;font-weight:500;font-style:normal;src:url(assets/fonts/playfair-display-latin-500-normal.woff2)}
@font-face{font-family:PF;font-weight:500;font-style:italic;src:url(assets/fonts/playfair-display-latin-500-italic.woff2)}
@font-face{font-family:MS;font-weight:500;src:url(assets/fonts/montserrat-latin-500-normal.woff2)}
@font-face{font-family:MS;font-weight:600;src:url(assets/fonts/montserrat-latin-600-normal.woff2)}
@font-face{font-family:MS;font-weight:700;src:url(assets/fonts/montserrat-latin-700-normal.woff2)}
:root{--cream:#FBF4EC;--ink:#3E2A1E;--caramel:#9A5B3C;--orange:#FF9A5C}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1920px;overflow:hidden}
body{background:var(--cream);font-family:MS,sans-serif;color:var(--ink);position:relative}
em{font-style:italic;color:var(--caramel)}
.prog{position:absolute;left:60px;right:60px;top:70px;display:flex;gap:8px}
.prog i{flex:1;height:5px;border-radius:3px;background:rgba(62,42,30,.18)}
.prog i.on{background:var(--caramel)}
.top{position:absolute;left:60px;right:60px;top:112px;display:flex;justify-content:space-between;font-weight:700;font-size:23px;letter-spacing:.32em;color:var(--caramel)}
.card{position:absolute;left:60px;top:200px;width:960px;height:1000px;border-radius:40px;overflow:hidden;box-shadow:0 30px 70px rgba(90,50,20,.28)}
.card img{width:100%;height:100%;object-fit:cover;display:block}
.frame{position:absolute;left:36px;top:176px;width:1008px;height:1048px;border:2px solid rgba(154,91,60,.35);border-radius:56px}
.chip{position:absolute;left:100px;top:1160px;background:var(--cream);color:var(--caramel);font-weight:700;font-size:22px;letter-spacing:.3em;padding:20px 34px;border-radius:40px;box-shadow:0 10px 30px rgba(90,50,20,.22)}
.txt{position:absolute;left:70px;right:70px;top:1290px}
h1{font-family:PF,serif;font-weight:400;font-size:100px;line-height:1.08;letter-spacing:-.01em}
.orn{display:flex;align-items:center;gap:16px;margin:34px 0 30px}
.orn b{width:90px;height:3px;background:var(--orange);border-radius:2px}
.orn s{width:12px;height:12px;border-radius:50%;background:var(--orange)}
p{font-weight:500;font-size:40px;line-height:1.5;color:#5a4030;max-width:900px}
.foot{position:absolute;left:60px;right:60px;top:1700px;border-top:2px solid rgba(154,91,60,.25);padding-top:26px;display:flex;justify-content:space-between;font-weight:700;font-size:22px;letter-spacing:.3em;color:var(--caramel)}
.foot span:last-child{color:#d9692c;letter-spacing:.1em}
"""
def prog(n): return '<div class="prog">'+''.join('<i class="on"></i>' if k<=n else '<i></i>' for k in range(1,11))+'</div>'
def page(name,body,extra=""):
    open(name,"w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra}</style></head><body>{body}</body></html>')
for num,t,d in slides:
    n=int(num)
    page(f"story-{num}.html",f'''{prog(n)}<div class="top"><span>SUNARI · SELAYAR</span><span>{num} / 10</span></div>
<div class="frame"></div><div class="card"><img src="assets/photos/{num}.jpg"></div>
<div class="chip">VIP SUPERIOR BUNGALOW</div>
<div class="txt"><h1>{t}</h1><div class="orn"><b></b><s></s></div><p>{d}</p></div>
<div class="foot"><span>KETUK UNTUK LANJUT</span><span>#sunarisunsetmoment</span></div>''')
# cover
page("story-01.html",f'''<style>
body{{background:#1b2417}}
.bg{{position:absolute;inset:-60px;background:url(assets/photos/01.jpg) center/cover;filter:blur(40px) brightness(.55)}}
.ph{{position:absolute;left:0;top:150px;width:1080px;height:1350px;background:url(assets/photos/01.jpg);
 -webkit-mask-image:linear-gradient(to bottom,transparent 0,#000 140px,#000 1000px,transparent 1350px)}}
.shade{{position:absolute;left:0;right:0;bottom:0;height:800px;background:linear-gradient(to bottom,transparent,rgba(16,22,13,.95) 32%)}}
.cprog{{position:absolute;left:60px;right:60px;top:70px;display:flex;gap:8px}}
.cprog i{{flex:1;height:5px;border-radius:3px;background:rgba(255,255,255,.3)}}
.cprog i:first-child{{background:#fff}}
.lg{{position:absolute;left:350px;top:1440px;width:380px}}
.tag{{position:absolute;left:0;right:0;top:1695px;text-align:center;color:#FFEEDE;font-weight:600;font-size:24px;letter-spacing:.38em}}
.tag2{{position:absolute;left:0;right:0;top:1760px;text-align:center;color:var(--orange);font-weight:700;font-size:23px;letter-spacing:.14em}}
</style><div class="bg"></div><div class="ph"></div><div class="shade"></div>
<div class="cprog">{''.join('<i></i>' for _ in range(10))}</div>
<img class="lg" src="assets/logo-light.png">
<div class="tag">KETUK UNTUK MELIHAT KAMAR  →</div>
<div class="tag2">#sunarisunsetmoment</div>''')
# closing
fac=[("King bed","Termasuk sarapan"),("AC & Wi-Fi","TV"),("Mini bar/kulkas","Set kopi/teh"),("Bathtub","Air panas & dingin"),("Rain shower","Tirai blackout"),("Meja kerja/rias","Teras kayu pribadi")]
rows=''.join(f'<div class="r"><span>{html.escape(a)}</span><span>{html.escape(b)}</span></div>' for a,b in fac)
page("story-10.html",f'''{prog(10)}
<style>
.fr{{position:absolute;inset:36px;border:2px solid rgba(154,91,60,.4);top:140px;bottom:130px}}
.lg2{{position:absolute;left:340px;top:210px;width:400px;}}
.c{{text-align:center;position:absolute;left:0;right:0}}
.eb{{font-weight:700;font-size:24px;letter-spacing:.38em;color:var(--caramel)}}
.big{{font-family:PF;font-size:128px;line-height:1.05}}
.list{{position:absolute;left:100px;right:100px;top:960px;border-top:2px solid rgba(154,91,60,.3)}}
.r{{display:grid;grid-template-columns:1fr 1fr;border-bottom:2px solid rgba(154,91,60,.3);font-weight:500;font-size:36px;height:92px;align-items:center}}
.r span:before{{content:"";display:inline-block;width:14px;height:14px;border-radius:50%;background:var(--orange);margin-right:22px;vertical-align:middle}}
.btn{{display:inline-block;margin-top:34px;background:var(--ink);color:var(--cream);border-radius:80px;padding:26px 50px;font-family:PF;font-size:50px}}
.btn em{{color:#FFB47F}}
</style>
<div class="fr"></div>
<img class="lg2" src="assets/logo-dark.png">
<div class="c eb" style="top:560px">FASILITAS KAMAR</div>
<div class="c big" style="top:610px">VIP Superior<br><em>Bungalow</em></div>
<div class="list">{rows}</div>
<div class="c" style="top:1540px"><div class="eb">INFO &amp; RESERVASI</div><div class="btn"><em>WhatsApp</em> 0821-8903-3044</div></div>
<div class="c eb" style="top:1700px;font-size:21px">PANTAI SUNARI · SELAYAR</div>''')
