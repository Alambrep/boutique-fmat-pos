# Screen catalogue

> **Task:** T-18 · **Rubric criterion (delivery 2):** 1d · **Prototype version:** [v1](prototype/v1/)
>
> Every screen of the prototype has an identifier `SCR-xx` and cites the requirements it implements. This table is the **source** of the requirements → design traceability: [`tools/trace.py`](../tools/trace.py) reads it, checks that the prototype's screens declare exactly the same requirements (`data-reqs` attribute of each screen in `index.html`), checks that every *Must* functional requirement has a screen, and generates the view [requirements → screens → interactions](../docs/04-requirements/traceability-matrix.md#5-requirements--design-screens-and-interactions). Key interactions (`IX-xx`) are in [`interaction-design.md`](interaction-design.md).

## Screens

| ID | Screen (UI title) | Profiles | Functional requirements | Non-functional requirements | Scenarios | Primary action | Pending |
|---|---|---|---|---|---|---|---|
| SCR-01 | Iniciar sesión | All | FR-01, FR-02, FR-30 | NFR-12 | S-08 | *Entrar* | Q-11 |
| SCR-02 | Vender | P-01 (start), P-02 (start), P-03 | FR-03, FR-13, FR-14, FR-15, FR-27, FR-28, FR-29, FR-31 | NFR-02, NFR-03, NFR-09, NFR-11, NFR-25 | S-01, S-03, S-08 | *Cobrar* | Q-02, Q-14 |
| SCR-03 | Elegir talla o color *(sheet)* | P-01, P-02, P-03 | FR-13, FR-31 | NFR-09 | S-07 | One option per size or color | Q-14 |
| SCR-04 | Resumen de la venta | P-01, P-02, P-03 | FR-16, FR-17, FR-33 | NFR-03, NFR-11, NFR-28 | S-01, S-03, S-07 | Choose how the customer pays (three choice buttons) | — |
| SCR-05 | Pago en efectivo | P-01, P-02, P-03 | FR-18, FR-22 | NFR-03, NFR-04 | S-01 | *Confirmar venta* | — |
| SCR-06 | Pago con tarjeta | P-01, P-02, P-03 | FR-19, FR-22 | NFR-21 | S-03 | *Sí, aprobado: confirmar venta* | Q-06 (H-10) |
| SCR-07 | Pago con Interuady | P-01, P-02, P-03 | FR-20, FR-21, FR-39 | NFR-06, NFR-07, NFR-22 | S-02 | *Confirmar venta* | Q-04 |
| SCR-08 | Producto agotado *(dialog)* | P-01, P-02, P-03 | FR-12, FR-32 | NFR-07 | S-05 | *Agregar de todos modos* | — |
| SCR-09 | Venta guardada | P-01, P-02, P-03 | FR-22, FR-23, FR-24, FR-29 | NFR-02, NFR-17 | S-01, S-02 | *Nueva venta* | — |
| SCR-10 | Ticket | P-01, P-02, P-03 | FR-23, FR-38 | — | S-01 | *Listo* | Q-05 |
| SCR-11 | Teléfono bloqueado | All | FR-30, FR-35 | NFR-19 | S-08 | *Desbloquear* | Q-11 |
| SCR-12 | Inventario | P-02, P-03 (read only) | FR-09, FR-10, FR-11, FR-12 | — | S-05, S-06 | *+ Nuevo producto* (CDU only) | — |
| SCR-13 | Nuevo producto | P-02 | FR-04, FR-05, FR-06, FR-08, FR-34, FR-36 | NFR-26 | S-04 | *Guardar producto* | Q-08 |
| SCR-14 | Producto guardado | P-02 | FR-06, FR-07, FR-28 | NFR-26 | S-04 | *Imprimir etiquetas* | Q-08 |
| SCR-15 | Cuentas por cobrar | All; P-03 (start) | FR-25 | NFR-27 | S-06 | Open a note (list) | Q-09 |
| SCR-16 | Detalle de la nota | All; personal details only for P-02, P-03 | FR-24, FR-26 | NFR-20 | S-06 | — (read only) | — |

Usability NFRs that apply to **every** screen (NFR-09 touch targets, NFR-10 contrast, NFR-12 Spanish, NFR-02 plain language on sales screens) are applied through the [design guidelines](guidelines.md) and checked on all screens (see the [prototype checks](prototype/v1/README.md#checks)); the table lists them only where a screen is designed specifically around them.

## Requirements not in prototype v1

| Requirement | Priority | Reason |
|---|---|---|
| FR-37 | Could | Desktop layout of the query views; v1 shows the inventory table with horizontal scrolling on a phone. |
| FR-D1…FR-D6 | Deferred | Depend on open questions (Q-02, Q-05, Q-06, Q-07, Q-09, Q-10). |

Partially covered: **FR-09** — only creation of products is prototyped (SCR-13); editing an existing product is not.
