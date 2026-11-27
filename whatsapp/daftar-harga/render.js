// Render daftar harga kamar ke JPG. Usage: node whatsapp/daftar-harga/render.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1200, height: 1700 } });
  await p.goto('file://' + path.join(__dirname, 'daftar_harga.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const over = await p.$eval('.pg', pg => { const r = pg.getBoundingClientRect(), ft = pg.querySelector('.ft').getBoundingClientRect().top,
    notes = pg.querySelector('.notes').getBoundingClientRect(), list = pg.querySelector('.list').getBoundingClientRect();
    return { list_vs_notes: Math.round(list.bottom - notes.top), notes_vs_footer: Math.round(notes.bottom - ft) }; });
  console.log('tumpang tindih (harus <= 0):', JSON.stringify(over));
  await (await p.$('.pg')).screenshot({ path: path.join(__dirname, 'Daftar_Harga_Kamar_SunaRi.jpg'), type: 'jpeg', quality: 92 });
  await b.close();
})();
