"""Feed carousel Hari Jadi Selayar ke-421 versi NYAMBUNG (seamless) slide 1-10.
Satu kanvas 10800x1350 dipotong jadi 10 slide 1080x1350: garis ombak berjalan melintasi semua slide,
dan ikon kartun berada TEPAT di sambungan antar-slide (setengah di slide kiri, setengah di slide kanan),
sehingga saat digeser carousel terasa menyambung. Isi teks & foto sama dengan build_hari_jadi_feed.py.
Run: python3 social/build_hari_jadi_nyambung.py && node social/render_hari_jadi_nyambung.js"""
import pathlib, math
H = pathlib.Path(__file__).parent
ns = {"__file__": str(H / "build_hari_jadi_feed.py")}
exec((H / "build_hari_jadi_feed.py").read_text(), ns)          # menghasilkan T (10 slide) & CSS yang sama
T, CSS, FONTS = ns["T"], ns["CSS"], ns["FONTS"]
W, HH, N = 1080, 1350, 10
LINE_Y = 862
CSS += """
body{background:#999;margin:0}
#canvas{position:relative;width:%dpx;height:%dpx;display:flex}
#canvas .t{margin:0!important;flex:0 0 1080px}
#canvas .ph{height:740px!important}
#over{position:absolute;inset:0;pointer-events:none;z-index:5}
""" % (W * N, HH)
T = [t.replace('<div class="frame"></div>', '') for t in T]          # bingkai slide 10 dilepas agar garis menyambung
# garis ombak lintas slide
pts = " ".join(f"{x},{LINE_Y + 14 * math.sin(2 * math.pi * x / 540):.1f}" for x in range(0, W * N + 1, 10))
dots = "".join(f'<circle cx="{x}" cy="{LINE_Y + 14 * math.sin(2 * math.pi * x / 540):.1f}" r="7" fill="#C0592C" stroke="#FBF4EC" stroke-width="3"/>' for x in range(270, W * N, 540))
C = {"coral": "#FF8A5C", "gold": "#FDB15D", "ocean": "#7BA7B6", "drift": "#A67C64", "deep": "#5A3E31", "pink": "#F7A7A1", "cream": "#FBF4EC"}
# ikon kartun di sambungan k (antara slide k dan k+1), digambar dalam kotak -46..46
ICONS = {
 1: f'<path d="M-32 6 q14 -18 28 0 q14 -18 28 0" stroke="{C["deep"]}" stroke-width="6" fill="none" stroke-linecap="round"/><path d="M-4 -16 q8 -10 16 0 q8 -10 16 0" stroke="{C["deep"]}" stroke-width="4" fill="none" stroke-linecap="round"/>',  # camar
 2: f'<ellipse cx="-6" cy="0" rx="26" ry="16" fill="{C["coral"]}"/><path d="M18 0 l18 -14 v28 z" fill="{C["coral"]}"/><circle cx="-20" cy="-4" r="4" fill="{C["deep"]}"/><path d="M-6 -14 q6 14 0 28" stroke="{C["gold"]}" stroke-width="4" fill="none"/>',  # ikan
 3: f'<circle cx="-14" cy="10" r="10" fill="none" stroke="{C["ocean"]}" stroke-width="5"/><circle cx="8" cy="-8" r="13" fill="none" stroke="{C["ocean"]}" stroke-width="5"/><circle cx="18" cy="18" r="6" fill="none" stroke="{C["ocean"]}" stroke-width="4"/>',  # gelembung
 4: f'<ellipse cx="0" cy="0" rx="24" ry="18" fill="{C["drift"]}"/><path d="M-12 -8 h24 M-14 4 h28" stroke="{C["gold"]}" stroke-width="3"/><circle cx="30" cy="-2" r="9" fill="{C["ocean"]}"/><ellipse cx="-14" cy="18" rx="9" ry="5" fill="{C["ocean"]}"/><ellipse cx="14" cy="18" rx="9" ry="5" fill="{C["ocean"]}"/><ellipse cx="-14" cy="-18" rx="9" ry="5" fill="{C["ocean"]}"/><ellipse cx="14" cy="-18" rx="9" ry="5" fill="{C["ocean"]}"/>',  # penyu
 5: f'<path d="M-30 8 h60 l-10 14 h-40 z" fill="{C["drift"]}"/><path d="M0 4 v-36 l24 30 z" fill="{C["coral"]}"/><path d="M-2 4 v-30 l-18 26 z" fill="{C["gold"]}"/>',  # perahu
 6: f'<ellipse cx="-14" cy="10" rx="8" ry="12" fill="{C["drift"]}" transform="rotate(-15 -14 10)"/><ellipse cx="12" cy="-10" rx="8" ry="12" fill="{C["drift"]}" transform="rotate(-15 12 -10)"/>' + "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="{C["drift"]}"/>' for x, y in [(-22,-6),(-16,-8),(-10,-6),(4,-26),(10,-28),(16,-26)]),  # jejak kaki
 7: f'<path d="M0 -26 q16 22 16 34 a16 16 0 0 1 -32 0 q0 -12 16 -34 z" fill="{C["ocean"]}"/><path d="M-6 6 a7 7 0 0 0 7 7" stroke="{C["cream"]}" stroke-width="3" fill="none"/>',  # tetes air gua
 8: f'<path d="M-30 10 a30 30 0 0 1 60 0 z" fill="{C["coral"]}"/>' + "".join(f'<rect x="-3" y="-44" width="6" height="12" rx="3" fill="{C["gold"]}" transform="rotate({a} 0 10)"/>' for a in (-60, -30, 0, 30, 60)) + f'<path d="M-34 14 h68 M-22 22 h44" stroke="{C["ocean"]}" stroke-width="4" stroke-linecap="round"/>',  # matahari terbenam
 9: f'<path d="M0 -28 l8 18 20 2 -15 13 5 20 -18 -11 -18 11 5 -20 -15 -13 20 -2 z" fill="{C["gold"]}"/><circle cx="26" cy="-24" r="4" fill="{C["gold"]}"/><circle cx="-28" cy="22" r="3" fill="{C["gold"]}"/>',  # bintang
}
icons = "".join(f'<g transform="translate({k * W},{LINE_Y})"><circle r="54" fill="{C["cream"]}" stroke="#C0592C" stroke-width="5"/><g transform="scale(1.12)">{ICONS[k]}</g></g>' for k in range(1, N))
OVER = f'''<svg id="over" viewBox="0 0 {W*N} {HH}" width="{W*N}" height="{HH}">
  <polyline points="{pts}" fill="none" stroke="#FBF4EC" stroke-width="10" stroke-opacity=".55"/><polyline points="{pts}" fill="none" stroke="#C0592C" stroke-width="5"/>{dots}{icons}</svg>'''
(H / "hari_jadi_nyambung.html").write_text(f'<!doctype html><html lang="id"><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body><div id="canvas">{"".join(T)}{OVER}</div></body></html>')
print("ok", len(T))
