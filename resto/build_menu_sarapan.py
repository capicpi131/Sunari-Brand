"""Menu Breakfast (inclusion room) Bajoy Beach Resto, gaya SunaRi: vertikal 1080x1920 + A4. Header = mozaik foto pagi.
Run: python3 resto/build_morning_cover.py && python3 resto/build_menu_sarapan.py && node resto/render_sarapan.js"""
import pathlib
H = pathlib.Path(__file__).parent
_src = (H / "build_menu_sunari.py").read_text()
exec(_src[:_src.index("c1 = section")])          # pakai ulang CSS, EMB, GRAIN, SUN, IG/TT, soft_grade
soft_grade(H / "menu-cover-morning-3row.png", H / "menu-cover-morning-soft.jpg")
COVER = "menu-cover-morning-soft.jpg"
HOURS = "07.00 – 10.00"      # DRAF: konfirmasi jam sarapan

# DRAF isi menu (placeholder, perlu dikonfirmasi): (nama, keterangan EN)
MAIN = [("Nasi Goreng Kampung", "Village-style fried rice"), ("Indomie Goreng", "Fried instant noodles"), ("Egg Sandwich", "Egg &amp; toasted bread"), ("Toast", "Buttered toast")]
SIDE = [("Fried Banana", "Pisang goreng"), ("Fresh Fruit", "Buah potong segar")]
DRINK = [("Black Coffee", "Kopi hitam"), ("Coffee Milk", "Kopi susu"), ("Hot Tea", "Teh panas"), ("Milk Tea", "Teh susu"), ("Orange Juice", "Jus jeruk")]

CSS2 = """
.bs{margin-bottom:var(--bsg)} .bs h3{margin-bottom:6px}
.sub{text-align:center;font-size:var(--subf);font-weight:500;letter-spacing:.32em;text-transform:uppercase;color:#7E5842;margin-bottom:var(--subm);text-shadow:0 1px 0 rgba(255,255,255,.9)}
.it2{text-align:center;padding:var(--ip) 0}
.it2 .n{font-family:'Playfair Display',serif;font-size:var(--nf);font-weight:500;line-height:1.15;color:#4A3226;text-shadow:0 1.5px 0 rgba(255,255,255,.95),0 -1px 0 rgba(74,50,38,.22),1.5px 3px 3px rgba(74,50,38,.26)}
.it2 .e{font-family:'Playfair Display',serif;font-style:italic;font-size:var(--ef);color:#7E5842;margin-top:3px;text-shadow:0 1px 0 rgba(255,255,255,.9)}
.card{text-align:center;padding:var(--cp) 0;position:relative}
"""
def blk(title, sub, items):
    rows = "".join(f'<div class="it2"><div class="n">{n}</div><div class="e">{e}</div></div>' for n, e in items)
    return f'<div class="sec bs"><h3>{title}</h3><div class="sub">{sub}</div>{rows}</div>'

left = blk("Hidangan Utama", "Pilih satu · Choose one", MAIN) + blk("Pelengkap", "Sides", SIDE)
card = f'''<div class="card"><div class="rule" style="position:absolute;left:0;right:0;top:0"></div>
  <div class="caps" style="font-size:var(--subf);letter-spacing:.38em;margin-right:-.38em;margin-top:var(--cm)">Jam Sarapan</div>
  <div class="pf" style="font-size:var(--hf);margin-top:8px;line-height:1.1">{HOURS}</div>
  <div class="pf it" style="font-size:var(--ef);color:#7E5842;margin-top:6px">Breakfast hours</div></div>'''
right = blk("Minuman", "Pilih satu · Choose one", DRINK) + card

def page(vertical):
    v = ("--bsg:58px;--subf:14px;--subm:16px;--ip:25px;--nf:33px;--ef:21px;--cp:36px;--cm:30px;--hf:54px" if vertical else
         "--bsg:34px;--subf:12.5px;--subm:10px;--ip:15px;--nf:27px;--ef:18px;--cp:26px;--cm:20px;--hf:44px")
    colw = 380
    return f'''<div class="pg" id="menu-sarapan" style="{v}"><div class="paper"></div>{GRAIN}
  <div class="hair" style="inset:34px"></div><div class="hair" style="inset:46px;opacity:.6"></div>
  <div class="hair" style="left:84px;right:84px;top:100px;height:330px;opacity:.7"></div>
  <div class="photo" style="position:absolute;left:100px;right:100px;top:116px;height:298px;background:url('{COVER}') 50% 50%/100% 100%"></div>
  <div style="position:absolute;left:0;right:0;top:486px;text-align:center">
    <div class="caps" style="font-size:15px;margin-right:-.5em;letter-spacing:.5em">Sarapan · Breakfast</div>
    <div class="pf" style="font-size:84px;line-height:1;margin-top:20px">Bajoy Beach <span class="it gold">Breakfast</span></div>
    <div class="pf it" style="font-size:24px;margin-top:16px;color:#7E5842">Termasuk dalam tarif kamar · Included in your stay</div>
    <div style="display:flex;align-items:center;justify-content:center;gap:22px;margin-top:26px">
      <div style="width:130px" class="rule"></div>{SUN}<div style="width:130px" class="rule"></div></div>
  </div>
  <div class="vr" style="left:538px;top:810px;height:{"900" if vertical else "720"}px"></div>
  <div class="col" style="left:100px;width:{colw}px;top:810px">{left}</div>
  <div class="col" style="right:100px;width:{colw}px;top:810px">{right}</div>
  <div class="soc" style="position:absolute;left:0;right:0;bottom:104px">{IG}{TT}<span>@sunaribeachresortselayar</span></div>
  <div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;font-size:12.5px;font-weight:600;letter-spacing:.2em;text-transform:uppercase;color:#7E5842;text-shadow:0 1px 0 rgba(255,255,255,.9)">
    Sarapan termasuk dalam tarif kamar · Breakfast included in room rate · WA {WA}</div>
</div>'''

def doc(body, w, h):
    return f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}{EMB}{CSS2}.pg{{height:{h}px !important}}@page{{size:{w}px {h}px;margin:0}}</style></head><body>{body}</body></html>'
vert = page(True)
(H / "menu-sarapan.html").write_text(doc(vert, 1080, 1920))
A4 = [
 ("top:100px;height:330px", "top:74px;height:330px"), ("top:116px;height:298px", "top:90px;height:298px"),
 ("top:486px;text-align:center", "top:424px;text-align:center"), ("font-size:84px;line-height:1;margin-top:20px", "font-size:70px;line-height:1;margin-top:10px"),
 ("font-size:24px;margin-top:16px", "font-size:21px;margin-top:10px"), ("gap:22px;margin-top:26px", "gap:22px;margin-top:14px"),
 ("top:810px;height:900px", "top:640px;height:720px"), ("width:380px;top:810px", "width:380px;top:640px"),
 ("bottom:104px\"", "bottom:78px\""), ("bottom:70px;text-align:center", "bottom:48px;text-align:center")]
a4v = ("--bsg:58px;--subf:14px;--subm:16px;--ip:25px;--nf:33px;--ef:21px;--cp:36px;--cm:30px;--hf:54px", "--bsg:34px;--subf:12.5px;--subm:10px;--ip:15px;--nf:27px;--ef:18px;--cp:26px;--cm:20px;--hf:44px")
h4 = vert.replace(*a4v)
for a, b in A4:
    assert a in h4, a
    h4 = h4.replace(a, b)
(H / "menu-sarapan-a4.html").write_text(doc(h4, 1080, 1527)); print("ok")
