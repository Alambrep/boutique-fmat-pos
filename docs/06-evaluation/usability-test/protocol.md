# Usability test protocol (V-07)

> **Task:** T-24 · **Rubric criteria (delivery 2):** 4a–4d · **Status:** ready for a pilot; **not run in delivery 2** (the pilot, T-25, was cancelled at checkpoint B of the [schedule](../../00-management/schedule.md#5-delivery-2--plan-due-2026-10-31)). It is the protocol for the usability tests of delivery 3.
>
> Facilitator and author: Alan Pérez. Participant-facing materials are in Spanish in [`es/`](es/README.md); this document is the English reference. Prototype under test: [current version](../../../design/README.md) (v1 at the time of writing), online at https://alambrep.github.io/boutique-fmat-pos/design/prototype/v1/.

## 1. Purpose and limits

**Purpose.** Check whether people who match the proto-personas can complete the [key interactions](../../../design/interaction-design.md) with the prototype; measure the result against the targets of the selected usability NFRs; and find the problems to fix in the next iteration.

**What this test cannot show.**

- With **proxy participants**, it produces no findings about the boutique, its sellers or the current process, and it does not change the status of any hypothesis `H-xx` ([validation plan §7](../../02-research/validation-plan.md#7-delivery-2-status-of-the-activities)). Real sellers replace proxies when the client grants permission.
- With a **low-fidelity prototype**, photos are drawings and participants may be unsure of what works `[R39]`; times are indicative and not comparable with real sales ([validation plan §3](../../02-research/validation-plan.md#3-data-to-collect-and-analysis)).

## 2. Selected usability NFRs (4a)

**Selection criteria**, applied to every NFR in the [usability specification](../../04-requirements/non-functional-requirements.md#0-usability-specification):

- **C1 — Priority:** the attribute is a priority for the system (learnability and errors first, then efficiency and satisfaction).
- **C2 — Measurable here:** it can be measured objectively in a task-based test with a low-fidelity prototype (not one that needs a field baseline, a working app on a device, or that is already checked by inspection).
- **C3 — Linked to a key interaction:** at least one `IX-xx` exercises it.

| NFR | Attribute | Target | Key interaction | C1 | C2 | C3 | Selected |
|---|---|---|---|---|---|---|---|
| NFR-01 | Learnability | ≥ 80% complete a cash sale without help, first attempt, after a ≤ 2 min demonstration | IX-01 | ✔ | ✔ | ✔ | **Yes** |
| NFR-25 | Learnability | No mandatory tutorial; hint once | IX-01, IX-05 | ✔ | ✔ (help requests) | ✔ | **Yes** |
| NFR-06 | Errors — prevention | ≥ 80% complete an Interuady sale without a validation error; 100% identify the missing field | IX-02 | ✔ | ✔ | ✔ | **Yes** |
| NFR-28 | Errors — frequency | ≤ 1 error per task on average; 0 unrecoverable | IX-01, IX-02, IX-03, IX-04 | ✔ | ✔ | ✔ | **Yes** |
| NFR-03 | Efficiency | ≤ 5 taps for a one-item cash sale | IX-01 | ✔ | ✔ (taps beyond the 5-tap path) | ✔ | **Yes** |
| NFR-26 | Efficiency | Median ≤ 3 min per product (P-02) | IX-06 | ✔ | ✔ | ✔ | **Yes** (group B) |
| NFR-27 | Efficiency | ≥ 80% find a unit's notes in ≤ 1 min (P-03) | IX-07 | ✔ | ✔ | ✔ | **Yes** (group B) |
| NFR-08 | Satisfaction | SUS ≥ 68 | All | ✔ | ✔ | ✔ | **Yes** |
| NFR-05 | Memorability | ≥ 80% of returning participants succeed after two weeks | IX-01 | ✔ | Needs a second session two weeks later | ✔ | Delivery 3, second round |
| NFR-04 | Efficiency | Median time ≥ 20% lower than today | IX-01 | ✔ | ✘ needs the V-01 baseline (blocked) | ✔ | No |
| NFR-02, NFR-07, NFR-09, NFR-10, NFR-11, NFR-12 | Several | — | — | ✔ | ✘ checked by inspection ([changes §6](../../04-requirements/changes.md#6-checked-against-prototype-v1)) | — | No; observed qualitatively |
| NFR-13…NFR-18, NFR-23, NFR-24 | Perceived performance, reliability, compatibility | — | — | — | ✘ need a working app on a device (V-08) | — | No |

## 3. Participants (4b)

| Group | Represents | Recruitment criteria | Number |
|---|---|---|---|
| **A** (primary) | P-01, satellite seller | From the [validation plan](../../02-research/validation-plan.md#2-activities): does not work in software or IT; uses the phone mainly for calls, messaging and social media; has not used a point-of-sale app. Students of computing programs (such as FMAT's) do **not** meet the first criterion. | 5 per round `[R31]`. In delivery 2 the author can recruit **2** (author's statement, 2026-10-27); delivery 3 aims at 5 |
| **B** (secondary) | P-02 (CDU) and P-03 (Central Administration) | Uses forms or spreadsheets at work without help (profiles of H-07, H-16); does not work in software or IT. | 1–2 per round; optional if time is short, because group A is the primary persona |

- Adults only (18 or older); participation is voluntary.
- The [pre-test questionnaire](es/cuestionario-previo.md) checks the criteria; anyone who does not meet them is thanked and not tested.
- Participants are identified only by a code (`PRX-01`… for proxies, `SEL-01`… for real sellers); the number of real sellers and proxies is reported with the results.

## 4. Tasks and scenarios (4b)

Each task is read to the participant from a [task card](es/tareas.md) (Spanish), written as a scenario without naming buttons. Data in the scenarios are fictional. The prototype is reloaded before each participant; its sample data are the start state of every task.

### Group A — sign in done by the facilitator as `luis` (Campus Sociales)

| Task | Key interaction | Scenario (summary) | Success criterion | Optimal path | Stop at | NFRs |
|---|---|---|---|---|---|---|
| **TA-1** | IX-01 | A student buys a blue cap and pays with a $200 bill. | Sale saved: 1 × Gorra Azul, cash, change $50 seen | 5 taps: product, *Cobrar*, *Efectivo*, *$200*, *Confirmar venta* | 4 min | NFR-01, NFR-03, NFR-25, NFR-28 |
| **TA-2** | IX-02 | Someone from the Facultad de Ingeniería takes 3 white FMAT polos, size medium, and pays with Interuady; the card gives the C.P. and the requester. | Sale saved with Interuady, the 3 data correct, note created | Product → size → + twice → *Cobrar* → *Interuady* → 3 fields → *Confirmar venta* | 6 min | NFR-06, NFR-28 |
| **TA-3** | IX-01 (correction), IX-03 | A customer asks for a blue Jaguar T-shirt, size medium, and a thermos; before paying, drops the thermos; the card is declined and the customer pays $200 in cash. | Sale saved: only the T-shirt, cash; nothing recorded for the declined card | Add both → *Cobrar* → remove thermos → *Tarjeta* → *No, cambiar forma de pago* → *Efectivo* → *Pago exacto* → *Confirmar venta* | 5 min | NFR-28 |
| **TA-4** | IX-04 | A customer brings a grey hoodie, size large, that the phone shows as sold out, and pays $500 in cash. | Sale saved after the warning; participant can say what the warning meant | Product → size → *Agregar de todos modos* → *Cobrar* → *Efectivo* → *$500* → *Confirmar venta* | 4 min | NFR-28 (and comprehension, qualitative) |
| **TA-5** | IX-05 | The shift ends; leave the phone ready for a colleague, who signs in with her account (user and password on the card). | The colleague's account is on the sales screen | *Bloquear* → *Entrar con otra cuenta* → user, password → *Entrar* | 3 min | NFR-25 |

### Group B

| Task | Key interaction | Scenario (summary) | Success criterion | Optimal path | Stop at | NFRs |
|---|---|---|---|---|---|---|
| **TB-1** (as `daniela`, CDU) | IX-06 | Embroidered caps arrive in blue and white, no size: cost $90, price $180; 20 at CDU and 5 at Sociales of each color; take a photo of each. | Two products saved with the right price, photos and stock | *Inventario* → *+ Nuevo producto* → data → colors → *No tiene talla* → photos and stock → *Guardar producto* | 8 min | NFR-26 |
| **TB-2** (as `martha`, Central Administration) | IX-07 | How much does the Facultad de Ingeniería owe the boutique for Interuady purchases? | Answers **$2,050** (sample data) | Start screen *Por cobrar* → filter *Dependencia* → read total | 3 min | NFR-27 |

NFR-26 is defined after one practice product; this protocol has no practice product, so the TB-1 time is compared with the target only as an indication.

## 5. Time estimates (4b)

Estimates by the author for planning; the pilot replaces them with measured times.

| Step | Group A | Group B |
|---|---|---|
| Welcome and consent | 3 min | 3 min |
| Pre-test questionnaire | 3 min | 3 min |
| Explanation: think aloud, what is simulated | 2 min | 2 min |
| Demonstration (§6, step 4) | 2 min (the maximum NFR-01 allows) | — |
| Tasks (sum of the stop times) | ≤ 22 min | ≤ 11 min |
| SUS questionnaire | 3 min | 3 min |
| Closing interview | 5 min | 3 min |
| **Total per participant** | **≤ 40 min** | **≤ 25 min** |

## 6. Procedure (facilitator script)

1. **Prepare:** open the prototype on the test phone and reload it; sign in as `luis` (group A) or as `daniela` / `martha` (group B, before each task); have a stopwatch, the observation sheet and the printed or on-screen materials. Record the phone model (the reference is a low-end Android phone; if another phone is used, say so in the results).
2. **Consent** ([`es/consentimiento.md`](es/consentimiento.md)): read it, answer questions, record consent. No audio or video recording; a screen recording only if the participant agrees separately.
3. **Pre-test questionnaire** ([`es/cuestionario-previo.md`](es/cuestionario-previo.md)).
4. **Demonstration (group A, ≤ 2 min):** show the sales screen, the search field and the status at the top; add one product, open *Cobrar* to show the summary, and go back without paying. Do not show any payment method.
5. **Tasks:** read each card; start the stopwatch when the participant first touches the screen; ask them to think aloud. Do not help. If the participant asks, answer *"¿Qué harías si yo no estuviera?"*. Give help only when they ask twice or the stop time is reached, and mark the task as *assisted*. Stop the stopwatch when the success criterion is met or the participant says they finished.
6. **After TA-4:** ask *"¿Qué te quiso decir el aviso?"* and note the answer.
7. **SUS** ([`es/sus.md`](es/sus.md)) right after the last task.
8. **Closing interview** ([`es/cierre.md`](es/cierre.md)), then thanks.
9. **Between participants:** reload the prototype so every participant starts with the same data.

## 7. Metrics and levels (4c)

### Quantitative

The **acceptable** level is the target of the NFR, so meeting it means the NFR is met in the test. The **unacceptable** and **excellent** levels are the author's choice, except where a source is cited.

| Metric | Definition and how it is measured | Unacceptable | Acceptable | Excellent | NFR |
|---|---|---|---|---|---|
| **Task success** | Share of participants who meet the success criterion without help (observation sheet: *yes* / *assisted* / *no*) | < 60% | ≥ 80% | 100% | NFR-01 (TA-1), NFR-27 (TB-2) |
| **Interuady data without validation error** | Share of participants who confirm TA-2 without triggering the missing-data message; and share who, if it appears, find the missing field without help | < 60%, or anyone fails to find the field | ≥ 80%, and 100% find the field | 100% without the message | NFR-06 |
| **Errors per task** | Actions that move away from the goal (wrong product, wrong method, wrong field), counted on the sheet; *unrecoverable* = cannot undo without help | Mean > 1, or any unrecoverable | Mean ≤ 1, none unrecoverable | 0 | NFR-28 |
| **Extra taps** | TA-1 taps beyond the 5-tap optimal path | > 4 | ≤ 2 | 0 | NFR-03 |
| **Help requests** | Times the participant asks for help or looks for a tutorial, per session | > 1 in any task | ≤ 1 per session | 0 | NFR-25, NFR-01 |
| **Time on task, P-03** | TB-2, stopwatch | > 2 min | ≤ 1 min | ≤ 30 s | NFR-27 |
| **Time on task, P-02** | TB-1, stopwatch (indicative; see §4) | > 5 min per product | ≤ 3 min per product | ≤ 2 min per product | NFR-26 |
| **Time on task, group A** | Stopwatch; compared with the facilitator's own time on the optimal path, measured in the pilot | > 4 × or the stop time | ≤ 4 × | ≤ 2 × | — (diagnostic) |
| **SUS score** | Spanish SUS `[R42]`, scored as in `[R5]`: odd items − 1, 5 − even items, sum × 2.5 | < 68 (below the average of published studies `[R5]`) | ≥ 68 | > 80.3 (an A, top 10% of scores `[R5]`) | NFR-08 |

**Small samples.** With fewer than 5 participants per group `[R31]`, results are reported as counts ("2 of 2"), not percentages, and the levels are applied only as an indication; the NFR is recorded as *inconclusive*.

### Qualitative

| Measure | How it is collected |
|---|---|
| Comments while thinking aloud | Quotes on the observation sheet (anonymized) |
| Hesitations and misunderstandings — in particular of the client's terms *Interuady*, *C.P.* and *Cuentas por cobrar* (see the [guidelines](../../../design/guidelines.md#6-decisions-left-open)) | Observation; closing interview question 3 |
| Understanding of the out-of-stock warning | Question after TA-4 |
| Problems found | List on the observation sheet with severity: **S1** prevents completing the task · **S2** causes an error or a long delay · **S3** minor or cosmetic (author's scale) |

## 8. Analysis and reporting

- One table per task: success, errors, extra taps or time, help requests; one row per participant, then totals.
- SUS score per participant and the mean.
- Each selected NFR is recorded as **met**, **not met** or **inconclusive**, citing the metric.
- Problems are grouped (affinity diagramming `[R32]`) and each one is linked to a screen `SCR-xx` and a change for the next prototype version; the change is recorded in the prototype's evolution log.
- Results go in `results/` next to this protocol (delivery 3).

## 9. Pilot (4d)

The protocol is complete enough to run a pilot without other documents. A pilot with 1–2 group A participants checks:

| Check | Action if it fails |
|---|---|
| Task cards are understood without explanation | Reword the card |
| Stop times and the session total fit | Adjust §4 and §5 |
| The facilitator can record everything on the sheet in real time | Simplify the sheet |
| The prototype has no bugs in the task paths | Fix before the test round. Checked automatically: [`tools/prototype/tasks.js`](../../../tools/prototype/tasks.js) walks the optimal path of every task and checks its success criterion (11 of 11 checks pass on v1, 2026-10-30) |

Every change made after the pilot is listed here, with its date, before the first test round.

| Date | Change to the protocol | Reason |
|---|---|---|
| — | — (pilot not run in delivery 2) | — |

## 10. Ethics and data

The rules of the [validation plan §4](../../02-research/validation-plan.md#4-ethics-and-personal-data) apply: informed consent before starting, voluntary participation, codes instead of names, no recordings of people without explicit consent, notes kept privately and only anonymized summaries in the repository. Participants enter only the fictional data on the task cards; no real personal data is typed into the prototype.
