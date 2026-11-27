// Render each document to PDF + PNG pages. Usage: python3 services/build_docs.py && node services/render.js [prefix, mis. 06_Paket]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch();
  fs.mkdirSync(path.join(__dirname, 'png'), { recursive: true });
  for (const f of fs.readdirSync(__dirname).filter(f => /^\d\d_.*\.html$/.test(f) && (!process.argv[2] || f.startsWith(process.argv[2])))) {
    const key = f.replace('.html', '');
    const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 2 });
    await p.goto('file://' + path.join(__dirname, f)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    const pages = await p.$$('.page');
    // cek tumpukan dulu, sebelum screenshot (setelah screenshot hasil pengukuran tidak andal)
    const over = await p.$$eval('.page', ps => ps.map(pg => {
      const ft = pg.querySelector(".ft").getBoundingClientRect().top; const pr = pg.getBoundingClientRect(); let m = 0;
      pg.querySelectorAll(':scope > *:not(.ft):not(.frame):not(.frame2):not(.paper):not(.grain), :scope > *:not(.ft):not(.frame):not(.frame2):not(.paper):not(.grain) *').forEach(e => { const r = e.getBoundingClientRect(); if (r.height && r.top < pr.bottom && r.bottom > m) m = r.bottom; });
      return Math.round(m - ft); }));
    console.log(key, 'pages', pages.length, 'overlap px', over.join(','));
    over.forEach((v, i) => { if (v > 0) console.log(`  PERINGATAN: halaman ${i + 1} menumpuk footer ${v}px`); });
    for (let i = 0; i < pages.length; i++) await pages[i].screenshot({ path: path.join(__dirname, 'png', `${key}_p${i + 1}.png`) });
    // <template data-export="Nama"> di luar halaman → diekspor sebagai gambar mandiri png/Nama.png (tidak ikut PDF)
    for (const t of await p.$$('template[data-export]')) { const name = await t.getAttribute('data-export');
      const box = await t.evaluateHandle(t => { const d = document.createElement('div'); d.appendChild(t.content.cloneNode(true)); document.body.appendChild(d); return d.firstElementChild; });
      await p.evaluate(() => document.fonts.ready);
      await box.screenshot({ path: path.join(__dirname, 'png', `${name}.png`) });
      await box.evaluate(b => b.parentElement.remove()); }
    await p.pdf({ path: path.join(__dirname, `SunaRi_${key}.pdf`), width: '210mm', height: '297mm', printBackground: true });
  }
  await b.close();
})();
