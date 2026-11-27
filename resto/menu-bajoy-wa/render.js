// Render menu Bajoy Beach Resto ke PNG HD (2160x3840). Usage: node resto/menu-bajoy-wa/render.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'menu_bajoy.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const gap = await p.$eval('.pg', pg => Math.round(pg.querySelector('.ft').getBoundingClientRect().top - pg.querySelector('.in').getBoundingClientRect().bottom));
  console.log('jarak isi-footer (harus > 0):', gap);
  const el = await p.$('.pg');
  await el.screenshot({ path: path.join(__dirname, 'Menu_Bajoy_Beach_Resto_HD.png'), type: 'png' });
  await b.close();
})();
