// Render harga per tipe kamar ke PNG HD (2x: 2160x3840) untuk dikirim lewat WhatsApp (opsi "HD").
// Usage: python3 whatsapp/daftar-harga/build_per_type.py && node whatsapp/daftar-harga/render_per_type_hd.js
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs');
(async () => {
  const out = path.join(__dirname, 'png-hd'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2100 }, deviceScaleFactor: 2 });
  await p.goto('file://' + path.join(__dirname, 'harga_per_type.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const names = { standard: '1_Standard', 'vip-standard': '2_VIP_Standard', superior: '3_Superior', 'vip-superior': '4_VIP_Superior', 'family-superior': '5_Family_Superior' };
  for (const pg of await p.$$('.pg')) {
    const id = (await pg.getAttribute('id')).replace('harga-', '');
    await pg.screenshot({ path: path.join(out, `Harga_${names[id]}_Bungalow_HD.png`), type: 'png' });
    console.log('saved', id);
  }
  await b.close();
})();
