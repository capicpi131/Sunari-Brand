// Mozaik sampul WA -> 3 baris foto utuh (baris 2-4) + logo di tengah vertikal. Output: menu-cover-3row.png
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1300, height: 800 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, '../social/wa_cover.html')); await p.waitForLoadState('networkidle');
  await p.evaluate(() => {
    const c = document.getElementById('wa-cover');
    [...c.querySelectorAll('img')].forEach(i => { if (i.classList.contains('lgm')) return;
      const r = parseInt(i.style.gridRow); if (r < 2 || r > 4) i.remove(); else i.style.gridRow = r - 1; });
    c.style.gridTemplateRows = 'repeat(3,1fr)'; c.style.height = '411px';
    const l = c.querySelector('.lgm'); l.style.top = '50%'; l.style.width = '600px';
  });
  await p.locator('#wa-cover').screenshot({ path: path.join(__dirname, 'menu-cover-3row.png') });
  await b.close(); console.log('ok');
})();
