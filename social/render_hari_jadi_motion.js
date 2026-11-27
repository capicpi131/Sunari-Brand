// Render motion Hari Jadi Selayar ke MP4: frame per frame lewat setT(t), lalu ffmpeg.
// Usage: node social/render_hari_jadi_motion.js 01 [detik=8] [fps=30]
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs'); const { execSync } = require('child_process');
(async () => {
  const id = process.argv[2] || '01', dur = +(process.argv[3] || 8), fps = +(process.argv[4] || 30);
  const out = path.join(__dirname, 'hari-jadi-selayar-motion'); const tmp = path.join(out, `_frames_${id}`);
  fs.rmSync(tmp, { recursive: true, force: true }); fs.mkdirSync(tmp, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
  await p.goto('file://' + path.join(__dirname, `hari_jadi_motion${id}.html`)); await p.waitForLoadState('networkidle'); await p.evaluate(() => document.fonts.ready);
  const st = await p.$('#stage');
  for (let i = 0; i < dur * fps; i++) {
    await p.evaluate(t => window.setT(t), i / fps);
    await st.screenshot({ path: path.join(tmp, `f${String(i).padStart(4, '0')}.png`) });
  }
  await b.close();
  const mp4 = path.join(out, `hari-jadi-${id}.mp4`);
  execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i "${tmp}/f%04d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart "${mp4}"`);
  fs.rmSync(tmp, { recursive: true, force: true }); console.log('saved', mp4);
})();
