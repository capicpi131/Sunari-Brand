// Motion carousel Hari Jadi Selayar ke-421 (dijalankan di dalam social/hari_jadi_feed.html).
// Gambar & teks slide TIDAK diubah: elemen asli hanya dianimasikan menuju posisi akhirnya,
// sehingga frame terakhir setiap video sama persis dengan PNG slide-nya.
// Karakter pemandu: perahu kecil SunaRi yang keluar di tepi kanan slide N dan masuk dari tepi kiri slide N+1
// pada ketinggian yang sama (BOAT_Y), agar carousel terasa menyambung saat digeser.
(() => {
  const DUR = 6, BOAT_Y = 910, BOAT_W = 100;
  const ease = x => x < 0 ? 0 : x > 1 ? 1 : 1 - Math.pow(1 - x, 3);
  const lin = x => x < 0 ? 0 : x > 1 ? 1 : x;
  const seg = (t, a, b) => ease((t - a) / (b - a));
  const NS = 'http://www.w3.org/2000/svg';
  // perahu ringkas (tinggi ±42 px) agar muat di celah antara foto (y 880) dan teks (y 930) tanpa menutupi gambar
  const BOAT = `<g class="boat">
      <path d="M-46 0 h92 l-14 14 h-64 z" fill="#A67C64" stroke="#5A3E31" stroke-width="2.5"/>
      <path d="M2 0 v-26" stroke="#5A3E31" stroke-width="3"/>
      <path d="M5 -25 q26 12 24 24 h-24 z" fill="#FF8A5C" stroke="#5A3E31" stroke-width="2"/>
      <path d="M-1 -21 q-22 10 -22 20 h22 z" fill="#FDB15D" stroke="#5A3E31" stroke-width="2"/>
      <path d="M2 -26 l12 -4 v8 z" fill="#FBF4EC" stroke="#5A3E31" stroke-width="1.5"/>
    </g>
    <g class="wake">
      <path d="M-86 12 q10 -6 20 0 q10 6 20 0" stroke="#7BA7B6" stroke-width="3" fill="none" stroke-linecap="round"/>
      <path d="M-122 14 q9 -5 18 0 q9 5 18 0" stroke="#7BA7B6" stroke-width="2.5" fill="none" stroke-linecap="round" opacity=".7"/>
    </g>`;
  const GULL = '<path d="M0 0 q14 -14 28 0 q14 -14 28 0" stroke="#2A1A10" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>';
  const FISH = '<ellipse cx="0" cy="0" rx="26" ry="15" fill="#FF8A5C" stroke="#5A3E31" stroke-width="2.5"/><path d="M22 0 l20 -14 v28 z" fill="#FF8A5C" stroke="#5A3E31" stroke-width="2.5"/><circle cx="-13" cy="-4" r="4" fill="#5A3E31"/><path d="M-2 -12 q6 12 0 24" stroke="#FDB15D" stroke-width="3" fill="none"/>';

  function overlay(slide) {
    const svg = document.createElementNS(NS, 'svg');
    svg.setAttribute('viewBox', '0 0 1080 1350'); svg.setAttribute('class', 'motion-over');
    svg.style.cssText = 'position:absolute;inset:0;width:1080px;height:1350px;pointer-events:none;z-index:20';
    slide.appendChild(svg); return svg;
  }
  // posisi perahu: masuk = mulai dari separuh di luar kiri, keluar = berakhir separuh di luar kanan
  function boatAt(svg, t, t0, t1, fromEdge) {
    const g = svg.querySelector('.boatwrap');
    const x0 = fromEdge ? 0 : -BOAT_W, x1 = 1080;          // pusat perahu: 0 = tepat di sambungan kiri, 1080 = di sambungan kanan
    const k = lin((t - t0) / (t1 - t0));
    const x = x0 + (x1 - x0) * k, bob = Math.sin(t * 3.2) * 2, tilt = Math.sin(t * 2.4) * 2.5;
    g.setAttribute('transform', `translate(${x},${BOAT_Y + bob}) rotate(${tilt})`);
    g.style.opacity = t < t0 ? 0 : 1;
    g.querySelector('.wake').style.opacity = 0.6 + 0.4 * Math.sin(t * 5);
  }

  const S = {};
  // ---------------- Slide 1: sampul ----------------
  S['hari-jadi-01'] = {
    setup(el) {
      const big = el.querySelector('.big'); big.innerHTML = 'ke-<span class="num" style="display:inline-block">421</span>';
      ['.fh'].forEach(sel => { const h = el.querySelector(sel); h.innerHTML = h.innerHTML.split(/(<br>)/).map(p => p === '<br>' ? p :
        [...p].map(c => `<span class="ch" style="display:inline-block">${c === ' ' ? '&nbsp;' : c}</span>`).join('')).join(''); });
      const svg = overlay(el);
      svg.insertAdjacentHTML('beforeend', [0, 1, 2].map(k => `<g class="gull" data-k="${k}">${GULL}</g>`).join('') + `<g class="boatwrap">${BOAT}</g>`);
    },
    setT(el, t) {
      el.querySelector('.bgf').style.transform = `scale(${1.1 - 0.1 * seg(t, 0, DUR)})`;
      const fk = el.querySelector('.fk'), a = seg(t, 0.2, 0.9); fk.style.opacity = a; fk.style.transform = `translateY(${(1 - a) * 20}px)`;
      el.querySelectorAll('.fh .ch').forEach((s, i) => { const b = seg(t, 0.5 + i * 0.06, 1.0 + i * 0.06);
        s.style.opacity = b; s.style.transform = `translateY(${(1 - b) * 40}px) rotate(${(1 - b) * -8}deg)`; });
      const big = el.querySelector('.big'), c = seg(t, 1.5, 1.9); big.style.opacity = c; big.style.transformOrigin = 'left center'; big.style.transform = `scale(${0.92 + 0.08 * c})`;
      const num = el.querySelector('.num'); num.textContent = Math.round(421 * seg(t, 1.6, 3.4));
      num.style.transform = `scale(${t > 3.4 && t < 3.8 ? 1 + 0.06 * Math.sin((t - 3.4) / 0.4 * Math.PI) : 1})`;
      const fs = el.querySelector('.fs'), d = seg(t, 3.0, 3.7); fs.style.opacity = d; fs.style.transform = `translateX(${(1 - d) * -30}px)`;
      el.querySelector('.fg').style.opacity = 0.92 * seg(t, 4.0, 4.6); el.querySelector('.fl').style.opacity = seg(t, 3.8, 4.5);
      el.querySelectorAll('.gull').forEach(g => { const k = +g.dataset.k, tt = t - 0.3 - k * 0.9;
        const x = -120 + tt * 230, y = 700 + k * 36 + Math.sin(tt * 2 + k) * 10, s = 1.5 - k * 0.25, f = 0.65 + 0.35 * Math.abs(Math.sin(tt * 6 + k));
        g.setAttribute('transform', `translate(${x},${y}) scale(${s},${s * f})`); g.style.opacity = tt > 0 && x < 1100 ? 1 : 0; });
      boatAt(el.querySelector('.motion-over'), t, 2.2, DUR, false);       // perahu muncul di laut, keluar di tepi kanan
    }
  };
  // ---------------- Slide 2: pangan lokal ----------------
  S['hari-jadi-02'] = {
    setup(el) {
      const svg = overlay(el);
      svg.insertAdjacentHTML('beforeend',
        `<g class="smoke">${[0, 1, 2].map(k => `<path data-k="${k}" d="M0 0 q-18 -30 0 -60 q18 -30 0 -60" stroke="#FBF4EC" stroke-width="10" fill="none" stroke-linecap="round" opacity=".5"/>`).join('')}</g>
         <g class="fish">${FISH}</g><g class="boatwrap">${BOAT}</g>`);
    },
    setT(el, t) {
      el.querySelectorAll('.ph.grid > div > img').forEach((im, i) => { im.style.transform = `scale(${1.08 - 0.08 * seg(t, 0, DUR)})`; });
      el.querySelectorAll('.ph.grid .cap').forEach((c, i) => { const a = seg(t, 0.6 + i * 0.5, 1.3 + i * 0.5); c.style.opacity = a; c.style.transform = `translateY(${(1 - a) * 16}px)`; });
      [['.kick', 0.3], ['.ttl', 0.6], ['.sub', 1.1], ['.bt', 1.5]].forEach(([sel, s0]) => { const n = el.querySelector(sel), a = seg(t, s0, s0 + 0.7);
        n.style.opacity = a; n.style.transform = `translateY(${(1 - a) * 24}px)`; });
      // asap mengepul dari panggangan (foto kanan)
      el.querySelectorAll('.smoke path').forEach(p => { const k = +p.dataset.k, ph = ((t * 0.5 + k / 3) % 1);
        p.setAttribute('transform', `translate(${760 + k * 70},${560 - ph * 260}) scale(${0.7 + ph * 0.6})`); p.style.opacity = 0.55 * Math.sin(ph * Math.PI); });
      // ikan melompat dari "Dari laut" ke "ke meja makan"
      const f = el.querySelector('.fish'), k = seg(t, 2.0, 3.6);
      const fx = 300 + 480 * k, fy = 700 - Math.sin(k * Math.PI) * 330, rot = -40 + 80 * k;
      f.setAttribute('transform', `translate(${fx},${fy}) rotate(${rot}) scale(1.3)`); f.style.opacity = t > 2.0 && t < 3.75 ? 1 : 0;
      boatAt(el.querySelector('.motion-over'), t, 0, DUR, true);         // masuk dari sambungan kiri, keluar di sambungan kanan
    }
  };

  window.MOTION = {
    DUR,
    init(id) {
      document.querySelectorAll('.t').forEach(e => { if (e.id !== id) e.style.display = 'none'; else e.style.margin = '0'; });
      document.body.style.margin = '0'; document.body.style.background = '#FBF4EC';
      const el = document.getElementById(id); S[id].setup(el); this.el = el; this.id = id;
    },
    setT(t) { S[this.id].setT(this.el, t); }
  };
})();
