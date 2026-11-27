// Render harga per tipe kamar ke JPG. Usage: node whatsapp/daftar-harga/render_per_type.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 2100 } });
  await p.goto('file://' + path.join(__dirname, 'harga_per_type.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const names = { standard: '1_Standard', 'vip-standard': '2_VIP_Standard', superior: '3_Superior', 'vip-superior': '4_VIP_Superior', 'family-superior': '5_Family_Superior' };
  for (const pg of await p.$$('.pg')) {
    const id = (await pg.getAttribute('id')).replace('harga-', '');
    const gap = await pg.evaluate(el => Math.round(el.querySelector('.ft').getBoundingClientRect().top - el.querySelector('.eb').getBoundingClientRect().bottom));
    console.log(id, 'jarak isi-footer (harus > 0):', gap);
    await pg.screenshot({ path: path.join(__dirname, `Harga_${names[id]}_Bungalow.jpg`), type: 'jpeg', quality: 92 });
  }
  await b.close();
})();
