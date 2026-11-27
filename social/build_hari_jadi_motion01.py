"""Contoh motion slide 1 feed Hari Jadi Selayar ke-421 (1080x1350, 8 detik, 30 fps).
Huruf bergerak (judul muncul per huruf, angka 0 -> 421) + elemen kartun (matahari tersenyum terbenam, burung camar).
Semua gerak dikendalikan fungsi setT(t) agar render per-frame deterministik.
Run: python3 social/build_hari_jadi_motion01.py && node social/render_hari_jadi_motion.js 01"""
import pathlib
H = pathlib.Path(__file__).parent
P = "hari-jadi-selayar-feed/foto/"; LOGO_D = "../assets/logo-sunari-color-dark.png"
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,500;1,400&family=Montserrat:wght@500;600;700&display=swap" rel="stylesheet">'
CSS = """
*{margin:0;padding:0;box-sizing:border-box}body{background:#111}
#stage{position:relative;overflow:hidden;width:1080px;height:1350px;font-family:Montserrat,sans-serif;color:#FBF4EC}
#bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:15% 50%;transform-origin:30% 40%}
.vt{position:absolute;left:0;right:0;top:0;height:640px;background:linear-gradient(180deg,rgba(20,12,6,.55),rgba(20,12,6,0))}
.vb{position:absolute;left:0;right:0;bottom:0;height:520px;background:linear-gradient(0deg,rgba(20,12,6,.7),rgba(20,12,6,0))}
.fk{position:absolute;left:84px;top:110px;font-weight:600;font-size:22px;letter-spacing:.42em;text-transform:uppercase;text-shadow:0 2px 10px rgba(0,0,0,.5)}
.fh{position:absolute;left:80px;top:160px;font-family:'Playfair Display',serif;font-size:96px;line-height:1.05;text-shadow:0 3px 18px rgba(0,0,0,.45)}
.fh span{display:inline-block}
.big{position:absolute;left:76px;top:390px;font-family:'Playfair Display',serif;font-size:230px;line-height:.9;text-shadow:0 3px 18px rgba(0,0,0,.45);white-space:nowrap}
.fs{position:absolute;left:84px;top:620px;font-family:'Playfair Display',serif;font-style:italic;font-size:46px;text-shadow:0 2px 12px rgba(0,0,0,.55)}
.fg{position:absolute;left:84px;bottom:70px;font-weight:600;font-size:20px;letter-spacing:.38em;text-transform:uppercase;opacity:.92}
.fl{position:absolute;right:70px;bottom:52px;width:300px;filter:drop-shadow(0 2px 8px rgba(0,0,0,.45))}
#sun{position:absolute;left:868px;width:180px;height:180px}
#gulls{position:absolute;inset:0;pointer-events:none}
.shine{position:absolute;inset:0;background:linear-gradient(105deg,transparent 40%,rgba(255,236,190,.55) 50%,transparent 60%);mix-blend-mode:overlay;pointer-events:none}
"""
SUN = """<svg id="sun" viewBox="-110 -110 220 220">
  <g id="rays">""" + "".join(f'<rect x="-6" y="-104" width="12" height="30" rx="6" fill="#FDB15D" transform="rotate({a})"/>' for a in range(0, 360, 30)) + """</g>
  <circle r="66" fill="#FF8A5C" stroke="#FDB15D" stroke-width="8"/>
  <circle cx="-38" cy="16" r="12" fill="#F7A7A1" opacity=".9"/><circle cx="38" cy="16" r="12" fill="#F7A7A1" opacity=".9"/>
  <path d="M-30 -8 q8 -10 16 0" stroke="#5A3E31" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path d="M14 -8 q8 -10 16 0" stroke="#5A3E31" stroke-width="6" fill="none" stroke-linecap="round"/>
  <path id="mouth" d="M-22 18 q22 22 44 0" stroke="#5A3E31" stroke-width="6" fill="none" stroke-linecap="round"/>
</svg>"""
GULL = '<path d="M0 0 q14 -14 28 0 q14 -14 28 0" stroke="#2A1A10" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
TITLE1, TITLE2 = "Selamat", "Hari Jadi"
spans = lambda s, o: "".join(f'<span data-i="{o+i}">{c if c != " " else "&nbsp;"}</span>' for i, c in enumerate(s))
HTML = f'''<div id="stage"><img id="bg" src="{P}senja__85-siluet-tirai-senja-persegi-lurus.jpg" alt="">
<div class="vt"></div><div class="vb"></div>
<svg id="gulls" viewBox="0 0 1080 1350">{"".join(f'<g class="gull" data-k="{k}">{GULL}</g>' for k in range(3))}</svg>
{SUN}
<div class="fk" id="fk">29 November 1605 — 2026</div>
<div class="fh" id="fh">{spans(TITLE1, 0)}<br>{spans(TITLE2, len(TITLE1))}</div>
<div class="big" id="big">ke-<span id="num">421</span></div>
<div class="fs" id="fs">Kabupaten Kepulauan Selayar</div>
<div class="fg" id="fg">Geser &nbsp;→</div><img class="fl" id="fl" src="{LOGO_D}" alt=""><div class="shine" id="shine"></div></div>'''
JS = r"""
const ease = x => x<0?0:x>1?1:1-Math.pow(1-x,3);
const seg = (t,a,b) => ease((t-a)/(b-a));
function setT(t){
  document.getElementById('bg').style.transform = `scale(${1.12-0.12*Math.min(t/8,1)})`;
  const fk=document.getElementById('fk'); const a0=seg(t,0.2,1.0); fk.style.opacity=a0; fk.style.transform=`translateY(${(1-a0)*20}px)`;
  document.querySelectorAll('#fh span').forEach(s=>{const i=+s.dataset.i; const a=seg(t,0.6+i*0.07,1.1+i*0.07);
    s.style.opacity=a; s.style.transform=`translateY(${(1-a)*40}px) rotate(${(1-a)*-8}deg)`;});
  const b=seg(t,1.8,2.3); const big=document.getElementById('big'); big.style.opacity=b; big.style.transform=`scale(${0.9+0.1*b})`;
  big.style.transformOrigin='left center';
  const n=Math.round(421*seg(t,1.9,4.2)); document.getElementById('num').textContent=n;
  const pop = t>4.2&&t<4.7 ? 1+0.06*Math.sin((t-4.2)/0.5*Math.PI) : 1; document.getElementById('num').style.display='inline-block';
  document.getElementById('num').style.transform=`scale(${pop})`;
  const f=seg(t,3.6,4.4); const fs=document.getElementById('fs'); fs.style.opacity=f; fs.style.transform=`translateX(${(1-f)*-30}px)`;
  const g=seg(t,5.0,5.8); document.getElementById('fg').style.opacity=0.92*g; document.getElementById('fl').style.opacity=seg(t,4.6,5.4);
  // matahari kartun: muncul, berputar pelan, turun perlahan, tersenyum
  const sun=document.getElementById('sun'); const sa=seg(t,0.8,1.8);
  sun.style.top=`${340+230*Math.min(t/8,1)}px`; sun.style.opacity=sa; sun.style.transform=`scale(${0.6+0.4*sa})`;
  document.getElementById('rays').setAttribute('transform',`rotate(${t*18})`);
  // camar: terbang melintas dengan kepak sayap
  document.querySelectorAll('.gull').forEach(el=>{const k=+el.dataset.k; const tt=t-0.5-k*1.1;
    const x=-140+tt*210, y=700+k*38+Math.sin(tt*2+k)*10, flap=0.65+0.35*Math.abs(Math.sin(tt*6+k));
    el.setAttribute('transform',`translate(${x},${y}) scale(${1.5-k*0.25},${(1.5-k*0.25)*flap})`); el.style.opacity=tt>0?1:0;});
  // kilau keemasan melintas judul
  const sh=document.getElementById('shine'); const sp=(t-5.6)/1.4; sh.style.opacity=sp>0&&sp<1?1:0; sh.style.transform=`translateX(${-1100+sp*2200}px)`;
}
window.setT=setT; setT(0);
"""
(H / "hari_jadi_motion01.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{HTML}<script>{JS}</script></body></html>')
print("ok")
