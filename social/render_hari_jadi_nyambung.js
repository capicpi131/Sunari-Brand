// Potong kanvas 10800x1350 menjadi 10 slide + 1 pratinjau panorama. Usage: node social/render_hari_jadi_nyambung.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'hari-jadi-selayar-feed-nyambung'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 10800, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, 'hari_jadi_nyambung.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  for (let i = 0; i < 10; i++) await p.screenshot({ path: path.join(out, `nyambung-${String(i + 1).padStart(2, '0')}.png`), clip: { x: i * 1080, y: 0, width: 1080, height: 1350 } });
  await p.screenshot({ path: path.join(out, '_pratinjau-panorama.png'), clip: { x: 0, y: 0, width: 10800, height: 1350 } }); // diperkecil jadi .jpg untuk pratinjau
  await b.close(); console.log('ok');
})();
