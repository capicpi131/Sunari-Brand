// Render feed Hari Jadi Selayar ke-421. Usage: python3 social/build_hari_jadi_feed.py && node social/render_hari_jadi_feed.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const b = await chromium.launch(); const out = path.join(__dirname, 'hari-jadi-selayar-feed'); fs.mkdirSync(out, { recursive: true });
  const p = await b.newPage({ viewport: { width: 1200, height: 1500 } });
  await p.goto('file://' + path.join(__dirname, 'hari_jadi_feed.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  for (const id of await p.$$eval('.t', ts => ts.map(t => t.id))) { await p.locator('#' + id).screenshot({ path: path.join(out, id + '.png') }); console.log('saved', id); }
  await b.close();
})();
