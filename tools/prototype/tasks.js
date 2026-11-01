// Usage (from the repository root, Node.js with Playwright installed):
//   node tools/prototype/tasks.js $PWD/design/prototype/v1/index.html
// Walk the optimal path of every task of the usability protocol and check its success criterion.
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 360, height: 640 } }); p.setDefaultTimeout(4000);
  const ok = (c, m) => console.log((c ? 'PASS ' : 'FAIL ') + m);
  const go = async () => { await p.goto('file://' + process.argv[2]); };
  const signin = async u => { await p.fill('#in-user', u); await p.fill('#in-pass', 'x'); await p.click('button:visible:has-text("Entrar")'); };
  const btn = t => p.click(`button:visible:has-text("${t}")`);
  await go(); await signin('luis');
  // TA-1: 5 taps
  await p.click('#SCR-02 [data-g="gorra"]'); await p.click('#cartbar button'); await btn('Efectivo'); await p.click('[data-act="cashq"][data-v="200"]');
  ok((await p.textContent('#change')) === '$50', 'TA-1 change $50'); await p.click('#b-cash'); ok(await p.isVisible('#SCR-09.on'), 'TA-1 saved'); await btn('Nueva venta');
  // TA-2
  await p.click('#SCR-02 [data-g="polo"]'); await p.click('#SCR-03 button:has-text("Mediana")');
  await p.click('#cartbar button'); await p.click('[data-act="inc"]'); await p.click('[data-act="inc"]');
  ok((await p.textContent('#SCR-04 .stepper span')).trim() === '3', 'TA-2 quantity 3'); await btn('Interuady');
  await p.selectOption('#in-unit', 'Facultad de Ingeniería'); await p.fill('#in-cp', 'C.P. Laura Gómez'); await p.fill('#in-req', 'Ing. Raúl Pech'); await p.click('#b-iu', { force: true });
  ok((await p.textContent('#SCR-09')).includes('N-0004'), 'TA-2 note N-0004 created'); await btn('Nueva venta');
  // TA-3
  await p.click('#SCR-02 [data-g="jaguar"]'); await p.click('#SCR-03 button:has-text("Mediana")'); await p.click('#SCR-02 [data-g="termo"]');
  await p.click('#cartbar button'); await p.click('[data-act="ask-remove"][data-code="P060100"]'); await p.click('#dlg button:has-text("Quitar")');
  await btn('Tarjeta'); await btn('No, cambiar forma de pago'); await btn('Efectivo'); await btn('Pago exacto');
  ok((await p.textContent('#SCR-05 .total b')) === '$200', 'TA-3 total $200 after removing the thermos'); await p.click('#b-cash');
  ok((await p.textContent('#SCR-09')).includes('Efectivo'), 'TA-3 saved as cash'); await btn('Nueva venta');
  // TA-4
  await p.click('#SCR-02 [data-g="sudadera"]'); await p.click('#SCR-03 button:has-text("Grande")'); ok(await p.isVisible('#SCR-08.on'), 'TA-4 warning');
  await btn('Agregar de todos modos'); await p.click('#cartbar button'); await btn('Efectivo'); await p.click('[data-act="cashq"][data-v="500"]'); await p.click('#b-cash');
  ok((await p.textContent('#SCR-09')).includes('CDU'), 'TA-4 saved and flagged'); await btn('Nueva venta');
  // TA-5
  await p.click('#SCR-02 [data-act="lock"]'); await btn('Entrar con otra cuenta'); await signin('ana');
  ok(await p.isVisible('#SCR-02.on') && (await p.textContent('#SCR-02 .top')).includes('Ana'), 'TA-5 Ana on the sales screen');
  // TB-1
  await go(); await signin('daniela'); await p.click('#nav button:has-text("Inventario")'); await btn('+ Nuevo producto');
  await p.fill('#in-np-name', 'Gorra bordada'); await p.selectOption('#in-np-type', 'Gorra'); await p.fill('#in-np-cost', '90'); await p.fill('#in-np-price', '180');
  for (const c of ['Azul', 'Blanco']) { await p.fill('#in-np-color', c); await btn('Agregar'); }
  await btn('No tiene talla');
  for (const k of ['Azul|N/A', 'Blanco|N/A']) { await p.fill(`[id="st-${k}-CDU"]`, '20'); await p.fill(`[id="st-${k}-Sociales"]`, '5'); }
  for (const x of await p.locator('#np-vars [data-act="np-photo"]').all()) await x.click();
  await btn('Guardar producto'); ok((await p.textContent('#SCR-14')).includes('2 productos'), 'TB-1 two products saved');
  // TB-2
  await go(); await signin('martha'); await p.selectOption('#in-arunit', 'Facultad de Ingeniería');
  ok((await p.textContent('#SCR-15')).includes('$2,050'), 'TB-2 total $2,050');
  await b.close();
})();
