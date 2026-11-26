const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1700 }, deviceScaleFactor: 2480 / 1080 });   // 2480 x 3508 px = A4 @300dpi
  await p.goto('file://' + path.join(__dirname, 'menu-sunari-a4.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  await p.locator('#menu-sunari').screenshot({ path: path.join(__dirname, 'Menu_Bajoy_SunaRi_A4.png') });
  await p.pdf({ path: path.join(__dirname, 'Menu_Bajoy_SunaRi_A4.pdf'), width: '210mm', height: '297mm', scale: 793.7 / 1080, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
  await b.close(); console.log('ok');
})();
