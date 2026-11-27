// Menu sarapan & Bajoy versi A4: PNG HD (2480x3508 px = A4 300 dpi) + PDF siap cetak.
// PDF: A4 210x297 mm + bleed 3 mm (216x303 mm), dan versi crop marks (slug 10 mm). Teks vektor, font tertanam.
// Usage: python3 resto/menu-sarapan/build_a4.py && python3 resto/menu-bajoy-wa/build_a4.py && node resto/render_a4.js
const { chromium } = require('playwright'); const path = require('path');
const TRIM_W = 210, TRIM_H = 297, BLEED = 3, SLUG = 10, DESIGN_W = 1240;
const MENUS = [
  { html: 'menu-sarapan/menu_sarapan_a4.html', out: 'menu-sarapan/A4_Menu_Sarapan_SunaRi' },
  { html: 'menu-bajoy-wa/menu_bajoy_a4.html', out: 'menu-bajoy-wa/A4_Menu_Bajoy_Beach_Resto' },
];
(async () => {
  const b = await chromium.launch();
  for (const m of MENUS) {
    // PNG HD
    const p0 = await b.newPage({ viewport: { width: 1300, height: 1800 }, deviceScaleFactor: 2 });
    await p0.goto('file://' + path.join(__dirname, m.html)); await p0.waitForLoadState('networkidle'); await p0.evaluate(() => document.fonts.ready);
    const gap = await p0.$eval('.pg', pg => Math.round(pg.querySelector('.ft').getBoundingClientRect().top - pg.querySelector('.in').getBoundingClientRect().bottom));
    console.log(m.out, 'jarak isi-footer (harus > 0):', gap);
    await (await p0.$('.pg')).screenshot({ path: path.join(__dirname, `${m.out}_HD.png`), type: 'png' });
    await p0.close();
    // PDF cetak
    for (const marks of [false, true]) {
      const p = await b.newPage();
      await p.goto('file://' + path.join(__dirname, m.html)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
      const off = BLEED + (marks ? SLUG : 0), W = TRIM_W + 2 * off, H = TRIM_H + 2 * off;
      await p.evaluate(({ TRIM_W, TRIM_H, DESIGN_W, off, W, H, BLEED, marks }) => {
        const pg = document.querySelector('.pg'); const wrap = document.createElement('div'); wrap.className = 'pgwrap'; pg.parentNode.insertBefore(wrap, pg); wrap.appendChild(pg);
        [...document.body.children].forEach(c => { if (c !== wrap && c.tagName !== 'STYLE') c.style.display = 'none'; });
        const css = document.createElement('style');
        css.textContent = `@page{size:${W}mm ${H}mm;margin:0}
          html,body{margin:0!important;padding:0;width:${W}mm;height:${H}mm;overflow:hidden;background:${marks ? '#fff' : '#FBF4EC'}!important;-webkit-print-color-adjust:exact;print-color-adjust:exact}
          .bleed{position:absolute;left:${off - BLEED}mm;top:${off - BLEED}mm;width:${TRIM_W + 2 * BLEED}mm;height:${TRIM_H + 2 * BLEED}mm;background:#FBF4EC}
          .pgwrap{position:absolute;left:${off}mm;top:${off}mm;width:${TRIM_W}mm;height:${TRIM_H}mm;overflow:hidden}
          .pg{margin:0!important;zoom:${TRIM_W * 3.7795275591 / DESIGN_W}}
          .cm{position:absolute;background:#000}`;
        document.head.appendChild(css);
        const bl = document.createElement('div'); bl.className = 'bleed'; document.body.insertBefore(bl, document.body.firstChild);
        if (marks) {
          const th = 0.25, L = off, T = off, R = off + TRIM_W, B = off + TRIM_H, g = BLEED + 1, l = off - g - 1;
          const add = (x, y, w, h) => { const d = document.createElement('div'); d.className = 'cm';
            d.style.cssText = `left:${x}mm;top:${y}mm;width:${w}mm;height:${h}mm`; document.body.appendChild(d); };
          for (const [x, sx] of [[L, -1], [R, 1]]) for (const [y, sy] of [[T, -1], [B, 1]]) {
            add(sx < 0 ? x - g - l : x + g, y - th / 2, l, th); add(x - th / 2, sy < 0 ? y - g - l : y + g, th, l); }
        }
      }, { TRIM_W, TRIM_H, DESIGN_W, off, W, H, BLEED, marks });
      const file = path.join(__dirname, `${m.out}_CETAK${marks ? '_crop-marks' : ''}.pdf`);
      await p.pdf({ path: file, width: `${W}mm`, height: `${H}mm`, printBackground: true, preferCSSPageSize: true });
      console.log('saved', path.relative(__dirname, file), `${W}x${H} mm`);
      await p.close();
    }
  }
  await b.close();
})();
