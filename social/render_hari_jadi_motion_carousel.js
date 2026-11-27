// Motion carousel Hari Jadi Selayar: pratinjau gambar (keyframe) atau video per slide.
// Usage:
//   node social/render_hari_jadi_motion_carousel.js stills 01,02     -> keyframe PNG untuk dicek (tanpa video)
//   node social/render_hari_jadi_motion_carousel.js video  01,02     -> MP4 1080x1350, 6 detik, 30 fps
const { chromium } = require('playwright'); const path = require('path'); const fs = require('fs'); const { execSync } = require('child_process');
(async () => {
  const mode = process.argv[2] || 'stills', ids = (process.argv[3] || '01,02').split(','), fps = 30;
  const out = path.join(__dirname, 'hari-jadi-selayar-motion'); fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch();
  for (const n of ids) {
    const id = `hari-jadi-${n}`;
    const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
    await p.goto('file://' + path.join(__dirname, 'hari_jadi_feed.html')); await p.waitForLoadState('networkidle');
    await p.addScriptTag({ path: path.join(__dirname, 'motion', 'hari_jadi_motion.js') });
    await p.evaluate(id => window.MOTION.init(id), id); await p.evaluate(() => document.fonts.ready);
    const el = await p.$('#' + id), DUR = await p.evaluate(() => window.MOTION.DUR);
    if (mode === 'stills') {
      const dir = path.join(out, 'pratinjau'); fs.mkdirSync(dir, { recursive: true });
      for (const t of [0, 1, 2, 3, 4, DUR - 0.001]) {
        await p.evaluate(t => window.MOTION.setT(t), t);
        await el.screenshot({ path: path.join(dir, `${id}_t${t.toFixed(1)}.png`) });
      }
      console.log('stills', id);
    } else {
      const tmp = path.join(out, `_frames_${n}`); fs.rmSync(tmp, { recursive: true, force: true }); fs.mkdirSync(tmp);
      for (let i = 0; i < DUR * fps; i++) {
        await p.evaluate(t => window.MOTION.setT(t), Math.min(i / fps, DUR - 0.001));
        await el.screenshot({ path: path.join(tmp, `f${String(i).padStart(4, '0')}.png`) });
      }
      execSync(`ffmpeg -y -loglevel error -framerate ${fps} -i "${tmp}/f%04d.png" -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart "${path.join(out, id + '.mp4')}"`);
      fs.rmSync(tmp, { recursive: true, force: true }); console.log('video', id);
    }
    await p.close();
  }
  await b.close();
})();
