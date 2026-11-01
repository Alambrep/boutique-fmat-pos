// Usage (from the repository root, Node.js with Playwright installed):
//   node tools/prototype/flows.js $PWD/design/prototype/v1/index.html
// Clicks the key flows of the prototype as a participant would and prints PASS/FAIL per assertion.
// End-to-end checks of prototype v1: key flows by clicking, as a participant would.
const { chromium } = require('playwright');
const url = 'file://' + process.argv[2];
(async () => {
  const b = await chromium.launch();
  const p = await b.newPage({ viewport: { width: 360, height: 640 } }); p.setDefaultTimeout(5000);
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto(url);
  const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) process.exitCode = 1; };
  const vis = async t => p.locator('section.screen.on, section.overlay.on').filter({ hasText: t }).count() > 0;
  // sign-in validation
  await p.click('button:visible:has-text("Entrar")'); ok(await p.isVisible('#f-user .msg'), 'empty sign-in shows message under field');
  await p.fill('#in-user', 'luis'); await p.fill('#in-pass', 'x'); await p.click('button:visible:has-text("Entrar")');
  ok(await p.isVisible('#SCR-02.on'), 'seller starts on Vender (FR-03)');
  ok((await p.locator('#nav button').count()) === 2, 'seller nav has 2 destinations');
  // IX-01 cash sale, count taps
  let taps = 0; const tap = async s => { taps++; await p.click(s); };
  await tap('#SCR-02 [data-g="gorra"]'); ok((await p.textContent('#toast')).includes('Cobrar'), 'first-add hint shown once (NFR-25)');
  await tap('#cartbar button:visible:has-text("Cobrar")'); await tap('button:visible:has-text("Efectivo")'); await tap('button:visible:has-text("Pago exacto")'); await tap('button:visible:has-text("Confirmar venta")');
  ok(await p.isVisible('#SCR-09.on'), 'cash sale saved'); ok(taps <= 5, `one-item cash sale in ${taps} taps (NFR-03 ≤ 5)`);
  ok((await p.textContent('#SCR-09')).includes('cuando haya internet'), 'offline message in plain language (FR-29)');
  await p.click('button:visible:has-text("Nueva venta")');
  ok((await p.textContent('#SCR-02 .chip')).includes('1 venta por enviar'), 'status chip counts queued sale');
  // second add: no hint
  await p.click('#SCR-02 [data-g="taza"]'); ok(!(await p.textContent('#toast')).includes('Cobrar'), 'hint not repeated');
  // variants sheet + correction (IX-01 alt / S-07)
  await p.click('#SCR-02 [data-g="jaguar"]'); ok(await p.isVisible('#SCR-03.on'), 'variant sheet opens');
  await p.click('#SCR-03 button:visible:has-text("Mediana")'); await p.click('#cartbar button:visible:has-text("Cobrar")');
  ok((await p.locator('#SCR-04 .line').count()) === 2, 'summary has 2 lines');
  await p.click('#SCR-04 [data-act="dec"][data-code="P050100"]'); ok(await p.isVisible('#dlg.on'), 'minus at 1 asks before removing');
  await p.click('#dlg button:has-text("Quitar")'); ok((await p.locator('#SCR-04 .line').count()) === 1, 'line removed');
  await p.click('#SCR-04 [data-act="inc"][data-code="P010203"]'); ok((await p.textContent('#SCR-04 .stepper span')).trim() === '2', 'quantity +');
  // IX-03 card, change method
  await p.click('button:visible:has-text("Tarjeta")'); await p.click('button:visible:has-text("No, cambiar forma de pago")'); ok(await p.isVisible('#SCR-04.on'), 'card declined returns to summary');
  // IX-02 Interuady
  await p.click('button:visible:has-text("Interuady")'); ok((await p.textContent('#iu-count')).includes('3 de 3'), 'counter shows 3 missing');
  await p.click('#b-iu', { force: true }); ok(await p.isVisible('#SCR-07.on') && await p.locator('#SCR-07 .field.invalid').count() === 3, 'tapping confirm highlights 3 missing fields (FR-20)');
  await p.selectOption('#in-unit', 'Facultad de Ingeniería'); await p.fill('#in-cp', 'C.P. Prueba');
  ok((await p.textContent('#iu-count')).includes('1 de 3'), 'counter updates'); await p.click('#b-iu', { force: true });
  ok(await p.evaluate(() => document.activeElement.id) === 'in-req', 'focus moves to the missing field');
  await p.fill('#in-req', 'Solicitante Prueba'); await p.click('button:visible:has-text("Aviso de privacidad")'); ok(await p.isVisible('#dlg.on'), 'privacy notice opens (FR-39)');
  await p.click('#dlg button:visible:has-text("Cerrar")'); await p.click('#b-iu', { force: true });
  ok((await p.textContent('#SCR-09')).includes('Cuentas por cobrar'), 'Interuady note created (FR-24)');
  await p.click('button:visible:has-text("Ver ticket en pantalla")'); ok(await p.isVisible('#SCR-10.on'), 'ticket on screen without printer (FR-23)');
  await p.click('button:visible:has-text("Listo")'); await p.click('button:visible:has-text("Nueva venta")');
  // IX-04 out of stock (sudadera grande at Sociales = 0)
  await p.click('#SCR-02 [data-g="sudadera"]'); await p.click('#SCR-03 button:visible:has-text("Grande")');
  ok(await p.isVisible('#SCR-08.on'), 'out-of-stock warning (FR-32)'); await p.click('button:visible:has-text("Agregar de todos modos")');
  ok((await p.textContent('#cartbar')).includes('1 artículo'), 'sold anyway after confirming');
  await p.click('#cartbar button:visible:has-text("Cobrar")'); await p.click('button:visible:has-text("Efectivo")'); await p.fill('#in-cash', '400');
  ok(await p.getAttribute('#b-cash', 'aria-disabled') === 'true', 'confirm disabled when amount < total');
  await p.fill('#in-cash', '500'); ok((await p.textContent('#change')) === '$50', 'change computed (FR-18)');
  await p.click('#b-cash', { force: true }); ok((await p.textContent('#SCR-09')).includes('CDU'), 'flag for CDU review mentioned');
  await p.click('button:visible:has-text("Nueva venta")');
  // Por cobrar as seller: no personal data
  await p.click('#nav button:visible:has-text("Por cobrar")'); await p.click('#SCR-15 .rowbtn >> nth=0');
  ok((await p.textContent('#SCR-16')).includes('solo los pueden ver'), 'seller cannot see personal details (FR-26)');
  // IX-05 lock / switch user
  await p.click('#SCR-16 [data-act="lock"]'); ok(await p.isVisible('#SCR-11.on'), 'lock in one tap (FR-35)');
  ok((await p.textContent('#SCR-11')).includes('3 ventas guardadas'), 'queued sales kept with their seller');
  await p.click('button:visible:has-text("Entrar con otra cuenta")'); await p.fill('#in-user', 'daniela'); await p.fill('#in-pass', 'x'); await p.click('button:visible:has-text("Entrar")');
  ok((await p.locator('#nav button').count()) === 3, 'CDU nav has 3 destinations');
  // IX-06 new product
  await p.click('#nav button:visible:has-text("Inventario")'); await p.click('button:visible:has-text("+ Nuevo producto")'); await p.click('button:visible:has-text("Guardar producto")');
  ok(await p.locator('#SCR-13 .field.invalid').count() === 2, 'required name and price flagged');
  await p.fill('#in-np-name', 'Gorra bordada'); await p.fill('#in-np-price', '180');
  await p.fill('#in-np-color', 'Azul'); await p.click('button:visible:has-text("Agregar")'); await p.fill('#in-np-color', 'Blanco'); await p.press('#in-np-color', 'Enter');
  await p.click('button:visible:has-text("No tiene talla")');
  ok((await p.textContent('#np-msg')).includes('2 productos'), 'two variants announced (FR-36)');
  await p.fill('#np-vars input >> nth=0', '20'); await p.click('button:visible:has-text("Guardar producto")');
  ok(await p.locator('#SCR-13 .vbad').count() === 2, 'missing photos flagged (CR-06)');
  for (const b of await p.locator('#np-vars [data-act="np-photo"]').all()) await b.click();
  await p.click('button:visible:has-text("Guardar producto")'); ok(await p.isVisible('#SCR-14.on'), 'product saved with codes (FR-06)');
  await p.click('button:visible:has-text("Listo")'); ok((await p.textContent('#SCR-12 table')).includes('Gorra bordada'), 'new product in inventory');
  // Adm starts on Por cobrar
  await p.click('#SCR-12 [data-act="lock"]'); await p.click('button:visible:has-text("Entrar con otra cuenta")'); await p.fill('#in-user', 'martha'); await p.fill('#in-pass', 'x'); await p.click('button:visible:has-text("Entrar")');
  ok(await p.isVisible('#SCR-15.on'), 'Central Administration starts on Por cobrar (H-11)');
  await p.click('#nav button:visible:has-text("Inventario")'); ok(!(await p.isVisible('button:visible:has-text("+ Nuevo producto")')), 'no Nuevo producto for Adm (FR-09)');
  ok(errs.length === 0, 'no console errors ' + errs.join(' | '));
  await b.close();
})();
