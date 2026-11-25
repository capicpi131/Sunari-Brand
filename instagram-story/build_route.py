import re
src=open("build.py").read()
CSS=re.search(r'CSS="""(.*?)"""',src,re.S).group(1)
EXTRA="""
.prog i{}
h2{font-family:PF;font-weight:400;font-size:104px;line-height:1.06}
.eb{font-weight:700;font-size:24px;letter-spacing:.34em;color:var(--caramel)}
.hd{position:absolute;left:70px;right:70px;top:230px}
.hd .eb{margin-bottom:22px}
.tl{position:absolute;left:70px;right:70px;top:640px}
.it{position:relative;padding:0 0 60px 150px;min-height:120px}
.it:before{content:"";position:absolute;left:58px;top:18px;bottom:-18px;width:3px;background:repeating-linear-gradient(to bottom,rgba(154,91,60,.5) 0 10px,transparent 10px 18px)}
.it:last-child:before{display:none}
.it .dot{position:absolute;left:48px;top:10px;width:24px;height:24px;border-radius:50%;background:var(--orange);box-shadow:0 0 0 8px rgba(255,154,92,.25)}
.it .tm{position:absolute;left:-6px;top:-34px;font-weight:700;font-size:21px;letter-spacing:.12em;color:var(--caramel);width:130px;text-align:center}
.it h3{font-family:PF;font-weight:400;font-size:60px;line-height:1.1}
.it h3 em{color:var(--caramel)}
.it p{font-size:34px;line-height:1.45;margin-top:10px;max-width:800px}
.card2{position:absolute;left:60px;right:60px;border-radius:36px;padding:44px 48px;background:#fff8f0;border:2px solid rgba(154,91,60,.28);box-shadow:0 20px 50px rgba(90,50,20,.12)}
.card2.dk{background:var(--ink);color:var(--cream);border:none}
.card2 .eb{font-size:21px}
.card2.dk .eb{color:#FFB47F}
.card2 h3{font-family:PF;font-weight:400;font-size:66px;line-height:1.08;margin:14px 0 22px}
.card2 .row{display:flex;justify-content:space-between;font-size:31px;font-weight:500;padding:16px 0;border-top:2px solid rgba(154,91,60,.25)}
.card2.dk .row{border-color:rgba(255,238,222,.25)}
.card2 .row b{font-weight:700}
.note{font-size:26px;color:#7a5a45;position:absolute;left:70px;right:70px}
.pill{display:inline-block;background:var(--ink);color:var(--cream);border-radius:80px;padding:26px 50px;font-family:PF;font-size:50px}
.pill em{color:#FFB47F}
"""
def prog(n,t=6): return '<div class="prog">'+''.join('<i class="on"></i>' if k<=n else '<i></i>' for k in range(1,t+1))+'</div>'
def top(n): return f'<div class="top"><span>SUNARI · SELAYAR</span><span>0{n} / 06</span></div>'
foot='<div class="foot"><span>± WAKTU PERKIRAAN</span><span>#sunarisunsetmoment</span></div>'
def page(n,body,extra=""):
    open(f"route-0{n}.html","w").write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{EXTRA}{extra}</style></head><body>{body}</body></html>')
def tl(items,top_=640):
    h=''.join(f'<div class="it"><div class="dot"></div><div class="tm">{t}</div><h3>{a}</h3>{"<p>"+b+"</p>" if b else ""}</div>' for t,a,b in items)
    return f'<div class="tl" style="top:{top_}px">{h}</div>'
# 1 cover
svg='''<svg viewBox="0 0 960 760" width="960" height="760" style="position:absolute;left:60px;top:760px" fill="none" font-family="MS">
<defs><marker id="a" viewBox="0 0 10 10" refX="6" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="#9A5B3C"/></marker></defs>
<path d="M150 380 C 230 380 260 190 400 170" stroke="#3E2A1E" stroke-width="5" stroke-linecap="round"/>
<path d="M150 380 C 230 380 260 590 400 610" stroke="#3E2A1E" stroke-width="5" stroke-linecap="round"/>
<path d="M440 170 C 600 150 700 250 790 330" stroke="#9A5B3C" stroke-width="5" stroke-dasharray="4 16" stroke-linecap="round" marker-end="url(#a)"/>
<path d="M440 610 C 600 620 700 470 790 400" stroke="#9A5B3C" stroke-width="5" stroke-dasharray="4 16" stroke-linecap="round" marker-end="url(#a)"/>
<circle cx="130" cy="380" r="26" fill="#FF9A5C"/><circle cx="130" cy="380" r="46" stroke="#FF9A5C" stroke-opacity=".4" stroke-width="4"/>
<text x="130" y="460" text-anchor="middle" font-weight="700" font-size="26" letter-spacing="4" fill="#3E2A1E">SUNARI</text>
<circle cx="420" cy="170" r="18" fill="#3E2A1E"/><text x="420" y="118" text-anchor="middle" font-weight="700" font-size="24" letter-spacing="3" fill="#3E2A1E">TURUNGAN</text>
<text x="250" y="250" font-size="24" font-weight="600" fill="#9A5B3C" transform="rotate(-38 250 250)">± 1 jam</text>
<circle cx="420" cy="610" r="18" fill="#3E2A1E"/><text x="420" y="680" text-anchor="middle" font-weight="700" font-size="24" letter-spacing="3" fill="#3E2A1E">BONE TARINGAN</text>
<text x="250" y="545" font-size="24" font-weight="600" fill="#9A5B3C" transform="rotate(38 250 545)">± 1 jam</text>
<text x="640" y="150" font-size="24" font-weight="600" fill="#9A5B3C">kapal ± 1 jam</text>
<text x="640" y="650" font-size="24" font-weight="600" fill="#9A5B3C">kapal ± 20 mnt</text>
<ellipse cx="850" cy="365" rx="90" ry="62" fill="#F3DDBF" stroke="#9A5B3C" stroke-width="3"/>
<path d="M850 350 q10 -40 4 -80" stroke="#8a5a3a" stroke-width="7" stroke-linecap="round"/><path d="M854 272 q-30 -30 -62 -16 M854 272 q30 -30 62 -14 M854 272 q-10 -34 -34 -46 M854 272 q12 -36 38 -42" stroke="#5f8a4a" stroke-width="7" stroke-linecap="round"/><path d="M770 440 q20 -14 40 0 t40 0 t40 0 t40 0" stroke="#9A5B3C" stroke-width="3" stroke-opacity=".5"/><text x="850" y="470" text-anchor="middle" font-weight="700" font-size="26" letter-spacing="4" fill="#3E2A1E">BAHULUANG</text></svg>'''
page(1,f'''{prog(1)}{top(1)}
<div class="hd" style="top:250px"><div class="eb">TRIP SEHARI · SELAYAR</div><h2 style="margin-top:22px">SunaRi<br><em>ke Bahuluang</em></h2>
<p style="margin-top:26px;font-size:36px">Dua jalur, mengikuti air laut.</p></div>{svg}
<div class="foot"><span>KETUK UNTUK LANJUT</span><span>#sunarisunsetmoment</span></div>''')
# 2 two routes
def c(cls,eb,t,rows): 
    return f'<div class="card2 {cls}" style="top:{rows[0]}px"><div class="eb">{eb}</div><h3>{t}</h3>'+''.join(f'<div class="row"><span>{a}</span><b>{b}</b></div>' for a,b in rows[1])+'</div>'
page(2,f'''{prog(2)}{top(2)}
<div class="hd"><div class="eb">DUA JALUR</div><h2>Satu tujuan,<br><em>dua titik temu</em></h2></div>
{c("",'AIR CUKUP TINGGI','Bone Taringan',(620,[("Dari SunaRi","± 1 jam"),("Kapal","± 20 menit"),("Ujung selatan","Pulau Selayar")]))}
{c("dk",'AIR SURUT / PILIHAN TAMU','Turungan',(1100,[("Dari SunaRi","± 1 jam"),("Kapal","± 1 jam"),("Tanpa jalan kaki","Desa Turungan")]))}{foot}''')
# 3 depart
page(3,f'''{prog(3)}{top(3)}
<div class="hd"><div class="eb">HARI-H PAGI</div><h2>Berangkat <em>pagi</em></h2></div>
{tl([("± 07.00","Sarapan","di SunaRi Beach Resort, Patikarya"),("CEK AIR","Pasang-surut","Tim memastikan bersama kapten, lalu menentukan titik temu"),("± 08.00","Berangkat","Kendaraan bebas: mobil, motor, atau kendaraan sendiri"),("± 09.00","Tiba di titik temu","Bertemu kapten di Bone Taringan atau Turungan"),("KAPAL","Menuju Bahuluang","± 20 menit dari Bone Taringan · ± 1 jam dari Turungan")],560)}{foot}''')
# 4 bahuluang
page(4,f'''{prog(4)}{top(4)}
<div class="hd"><div class="eb">PULAU BAHULUANG · TIBA ± 10.00</div><h2>Hari di <em>pulau</em></h2></div>
{tl([("± 10.00","Makam <em>Karang</em>","Snorkeling"),("± 12.00","Makan siang","Lunchbox di Pantai Bahuluang"),("± 13.00","Gua <em>Lipang</em>","")],600)}
<div class="card2 dk" style="top:1270px;padding:40px 48px"><div class="eb">TERGANTUNG PASANG SURUT AIR</div><h3 style="margin:12px 0 0;font-size:62px">Pasir <em style="color:#FFB47F">Timbul</em></h3><p style="font-size:29px;margin-top:10px;color:#FFEEDE">Muncul saat air surut, waktunya menyesuaikan kondisi hari itu.</p></div>{foot}''')
# 5 low tide
page(5,f'''{prog(5)}{top(5)}
<div class="hd"><div class="eb">CATATAN</div><h2>Saat air <em>surut</em></h2></div>
<div class="card2" style="top:600px"><div class="eb">PILIHAN 1 · TANPA JALAN KAKI</div><h3>Lewat Turungan</h3><p style="font-size:36px;line-height:1.5">Kapal ± 1 jam langsung ke Bahuluang.</p></div>
<div class="card2" style="top:980px"><div class="eb">PILIHAN 2 · TETAP LEWAT BONE TARINGAN</div><h3>Berhenti di tubir</h3><p style="font-size:36px;line-height:1.5">Kapal tidak bisa masuk. Tamu berjalan ± 2 km dengan gabus, dipandu kru kapal, lalu naik kapal.</p></div>{foot}''')
# 6 return
page(6,f'''{prog(6)}{top(6)}
<div class="hd"><div class="eb">PULANG</div><h2>Kembali <em>sore</em></h2></div>
{tl([("± 14.00","Kapal kembali","ke titik temu, biasanya sama dengan titik berangkat"),("SURUT","Dijemput di Turungan","Saat pulang bertepatan dengan air surut"),("SORE","Tiba di SunaRi","Kembali ke resort dengan kendaraan Anda")],560)}
<div style="position:absolute;left:0;right:0;top:1300px;text-align:center"><div class="eb" style="margin-bottom:26px">INFO &amp; RESERVASI</div><div class="pill"><em>WhatsApp</em> 0821-8903-3044</div></div>{foot}''')
