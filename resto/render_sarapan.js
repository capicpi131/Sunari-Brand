const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const [html, png, dsf, pdf] of [['menu-sarapan.html', 'Menu_Sarapan_SunaRi.png', 2, null], ['menu-sarapan-a4.html', 'Menu_Sarapan_SunaRi_A4.png', 2480 / 1080, 'Menu_Sarapan_SunaRi_A4.pdf']]) {
    const p = await b.newPage({ viewport: { width: 1200, height: 2000 }, deviceScaleFactor: dsf });
    await p.goto('file://' + path.join(__dirname, html)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
    await p.locator('#menu-sarapan').screenshot({ path: path.join(__dirname, png) });
    if (pdf) await p.pdf({ path: path.join(__dirname, pdf), width: '210mm', height: '297mm', scale: 793.7 / 1080, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 } });
    await p.close();
  }
  await b.close(); console.log('ok');
})();
