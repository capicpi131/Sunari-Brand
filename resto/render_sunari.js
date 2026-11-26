const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 900, height: 1200 }, deviceScaleFactor: 3 });
  await p.goto('file://' + path.join(__dirname, 'menu-sunari.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#menu-sunari').screenshot({ path: path.join(__dirname, 'Menu_Bajoy_SunaRi_A4.png') });
  await p.pdf({ path: path.join(__dirname, 'Menu_Bajoy_SunaRi_A4.pdf'), width: '210mm', height: '297mm', printBackground: true });
  await b.close(); console.log('ok');
})();
