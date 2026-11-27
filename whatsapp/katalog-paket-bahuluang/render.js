// Render gambar katalog 1080x1080 (JPG, siap unggah ke WhatsApp Business). Usage: node whatsapp/katalog-paket-bahuluang/render.js
const { chromium } = require('playwright'); const path = require('path');
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 1200, height: 1200 }, deviceScaleFactor: 1 });
  await p.goto('file://' + path.join(__dirname, 'katalog.html')); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const names = ['01_sampul', '02_termasuk', '03_destinasi', '04_kedatangan', '05_alur_trip', '06_jadwal_hari2', '07_penginapan', '08_makan', '09_persiapan_ketentuan', '10_cara_pesan'];
  const sq = await p.$$('.sq');
  // cek teks keluar kotak
  const over = await p.$$eval('.sq', ss => ss.map(s => { const r = s.getBoundingClientRect(); let m = 0;
    s.querySelectorAll('*').forEach(e => { const q = e.getBoundingClientRect(); if (q.height && q.bottom - r.top > m) m = q.bottom - r.top; }); return Math.round(m - 1080); }));
  console.log('lebih dari kotak (px, harus <= 0):', over.join(','));
  for (let i = 0; i < sq.length; i++) await sq[i].screenshot({ path: path.join(__dirname, `${names[i]}.jpg`), type: 'jpeg', quality: 90 });
  await b.close();
})();
