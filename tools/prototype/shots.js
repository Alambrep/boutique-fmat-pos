// Usage (from the repository root, Node.js with Playwright installed):
//   node tools/prototype/shots.js $PWD/design/prototype/v1/index.html $PWD/design/prototype/v1/screens
// Then convert to grayscale: python3 -c "from PIL import Image;import glob;[Image.open(f).convert('L').save(f,optimize=True) for f in glob.glob('design/prototype/v1/screens/*.png')]"
// Screenshot every screen in its sample state, and measure touch targets (G-08: >= 48 px).
const { chromium } = require('playwright');
const [,, file, out, annot] = process.argv;
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 360, height: 640 }, deviceScaleFactor: 2 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + file + (annot ? '?notas' : ''));
  const ids = await p.evaluate(() => [...document.querySelectorAll('section.screen')].map(s => s.id).sort());
  const small = [];
  for (const id of ids) {
    await p.evaluate(i => window.demo(i), id); await p.waitForTimeout(150);
    await p.evaluate(() => document.getElementById('toast').classList.remove('on'));
    await p.screenshot({ path: `${out}/${id}.png` });
    const over = await p.evaluate(i => { const c = document.querySelector('#' + i + ' .content'); return !document.getElementById(i).classList.contains('overlay') && c && c.scrollHeight > c.clientHeight + 4; }, id);
    if (over) {
      await p.addStyleTag({ content: '#app{height:auto!important;overflow:visible!important}.screen.on .content{overflow:visible!important;flex:none!important}' });
      await p.screenshot({ path: `${out}/${id}-full.png`, fullPage: true });
      await p.evaluate(() => document.querySelectorAll('style')[1].remove());
    }
    const s = await p.evaluate(() => [...document.querySelectorAll('#app button, #app input, #app select')].filter(e => {
        const r = e.getBoundingClientRect(); return r.width && r.height && e.offsetParent !== null && (r.width < 48 || r.height < 48) && !e.closest('.ann');
      }).map(e => `${e.tagName.toLowerCase()} "${(e.textContent || e.id).trim().slice(0, 25)}" ${Math.round(e.getBoundingClientRect().width)}x${Math.round(e.getBoundingClientRect().height)}`));
    if (s.length) small.push(id + ': ' + [...new Set(s)].join('; '));
  }
  console.log('screens:', ids.length); console.log('targets < 48 px:', small.length ? '\n' + small.join('\n') : 'none'); console.log('errors:', errs.length ? errs : 'none');
  await b.close();
})();
