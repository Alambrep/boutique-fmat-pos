# Rubric map — Delivery 2

Where each item of the [delivery 2 rubric](client/rubric-delivery-2.md) ([original](client/originals/Rubric_2nd_Delivery-HCI.pdf)) is covered in this repository. Every link opens the exact section. Items still in progress show the task (`T-xx`) that will cover them.

**Author:** Alan Pérez · **Branch:** [`second-delivery`](https://github.com/Alambrep/boutique-fmat-pos/tree/second-delivery) · **Due:** 2026-10-31 · **Video:** _pending (T-28)_

The delivery 1 map is kept as it was delivered: [RUBRIC-MAP.md at the close of delivery 1](https://github.com/Alambrep/boutique-fmat-pos/blob/76fe116/RUBRIC-MAP.md).

---

## 1. Evolution of the requirements

| Rubric item | Where to find it | Status |
|---|---|---|
| **1a — Changes in requirements** (clarity of the FR/NFR language) | _Pending (T-16)_ | Planned (moved to 2026-10-30) |
| **1b — FR ↔ NFR mapping, particularly usability** | _Pending (T-17)_ | Planned |
| **1c — Usability attributes in the NFRs, system level or per requirement** | _Pending (T-16)_ | Planned |
| **1d — Traceability from requirements to design** | [Screen catalogue](design/screens.md) (SCR-01…SCR-16 with their FR/NFR) · [Requirements → screens → interactions](docs/04-requirements/traceability-matrix.md#5-requirements--design-screens-and-interactions) (generated) · [Annotations in the prototype](design/prototype/v1/README.md#how-to-open-it) (`?f&notas`) | Done (T-18): 38 of 39 FR have a screen; `tools/trace.py --check` verifies that the prototype declares the same requirements |

## 2. Interface prototyping

| Rubric item | Where to find it | Status |
|---|---|---|
| **2a — Prototype development** | [Prototype v1](design/prototype/v1/) — clickable, 16 screens, [screenshots](design/prototype/v1/README.md#screens), [checks](design/prototype/v1/README.md#checks) | v1 done; author's review pending (T-20) |
| **2b — Design guidelines** (organization of elements, information architecture) | [Guidelines](design/guidelines.md): [§1 information architecture](design/guidelines.md#1-information-architecture), [§2 organization of each screen](design/guidelines.md#2-organization-of-each-screen), [§3 components](design/guidelines.md#3-components), [§4 low-fidelity conventions](design/guidelines.md#4-low-fidelity-visual-conventions) | Done (T-19) |
| **2c — Evolution of prototypes** (optional) | Issues found in v1: [B-1, B-2](design/prototype/v1/README.md#issues-noticed-while-building-v1); v2 _pending (T-23)_ | In progress |
| **2d — Interaction design** (key interactions, standardized, linked to FR and usability NFR) | [Interaction design](design/interaction-design.md): [format](design/interaction-design.md#format) and [summary](design/interaction-design.md#summary) of IX-01…IX-07 | Done (T-21) |

## 3. Inspection methods (optional)

| Rubric item | Where to find it | Status |
|---|---|---|
| **3a — Method, results and how they were used** | _Pending (T-22, conditional)_ | Planned |
| **3b — Tool or protocol** | _Pending (T-22, conditional)_ | Planned |

## 4. Usability test sketch

| Rubric item | Where to find it | Status |
|---|---|---|
| **4a — Selection of priority usability NFRs** | _Pending (T-24)_ | Planned |
| **4b — Test planning** (participants, tasks and scenarios, times, instruments) | _Pending (T-24)_ | Planned |
| **4c — Metrics with unacceptable / acceptable / excellent levels** | _Pending (T-24)_ | Planned |
| **4d — Protocol that would allow a pilot** | _Pending (T-24)_; pilot _(T-25, conditional)_ | Planned |

## 5. Teamwork (individual project)

| Rubric item | Where to find it | Status |
|---|---|---|
| **5a — Logbook and task tracking** (task, owner, status, definition of done) | [Task log](docs/00-management/task-log.md) · [Logbook](docs/00-management/logbook/) · [Schedule §5](docs/00-management/schedule.md#5-delivery-2--plan-due-2026-10-31) · [GitHub issues, milestone "Delivery 2"](https://github.com/Alambrep/boutique-fmat-pos/milestone/2) | In progress (T-26) |
| **5b — Contribution metric, parameters and % per delivery** | _Pending (T-27)_ | Planned |

## 6. Progress presentation

| Rubric item | Where to find it | Status |
|---|---|---|
| **6a–6c — Material, content, time (≤ 5 min)** | _Pending (T-28)_ | Planned |

---

## Context for the evaluator

- **Field research is blocked, not skipped.** Permission to observe and interview at the boutique was requested from the client on 2026-09-30 and again on 2026-10-19, with no answer yet ([communications](docs/00-management/meetings.md#communications-with-the-client)). The research plan is ready to run; meanwhile the design starts from the proto-personas, and every element that depends on field data stays labeled as a hypothesis (`H-xx`).
- **Delivery 1 rubric items** (definition, research plan, user modeling, initial requirements) are not graded again; their artifacts remain in place and are linked from the [README](README.md).
