const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'menu-sunari.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#menu-sunari').screenshot({ path: path.join(__dirname, 'Menu_Bajoy_SunaRi.png') });
  await b.close(); console.log('ok');
})();
