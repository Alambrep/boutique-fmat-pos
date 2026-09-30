# User hypotheses

> **Task:** T-03 · **Rubric criteria:** 2, 3 · **Status:** final — delivery 1 — **no hypothesis in this document has been validated.**

## 1. How these hypotheses were produced

Delivery 1 does not include field research (see [README §3](../../README.md#3-delivery-1-approach)). Following a **Lean UX proto-persona** approach — personas built from the team's existing knowledge and assumptions rather than new research `[R6]`, to be treated as testable hypotheses `[R7]` — the author:

1. Extracted every fact stated by the client (`CR-xx`, `PRJ-xx`) from the [client requirements](../../client/client-requirements.md).
2. Listed the assumptions needed to design for those facts (who the users are, where, with which devices, under what conditions).
3. Wrote each assumption as a testable hypothesis, with a signal that would confirm or refute it.
4. Rated each one by **confidence** (how sure the author is) and **risk** (how much the design changes if it is wrong), and prioritized validation accordingly (§4).

**Inputs used:** client document and project brief only. **Not used:** interviews, observation, surveys or analytics — none were conducted yet.

## 2. Hypothesis format

Adapted from the Lean UX practice of writing assumptions as testable statements that begin with "We believe…" `[R8]`, adding explicit signals of success and failure:

> **We believe that** [statement].
> **We will know we are right when** [observable signal].
> **We will know we are wrong when** [observable signal].

Status values: `Unvalidated` → `Validated` / `Refuted` / `Partially validated` (with evidence link); an `Inconclusive` analysis leaves the hypothesis `Unvalidated` and records the gap. Thresholds are defined in the [validation plan](validation-plan.md#3-data-to-collect-and-analysis).

## 3. Hypotheses

### Users

| ID | We believe that… | Right if… | Wrong if… | Confidence | Risk | Validation | Status |
|---|---|---|---|---|---|---|---|
| H-01 | Sellers at the satellite points (Social Sciences, Exact Sciences) are not technical staff and have basic or low digital skills. | Most observed/interviewed sellers use only basic phone functions (calls, messaging) and struggle with unfamiliar apps. | Sellers routinely use business or productivity apps without help. | Medium | High | V-01, V-02 | Unvalidated |
| H-07 | CDU staff have stronger digital skills and do the data-entry tasks (product registration, photos, labels). | CDU staff describe doing registration and use spreadsheets or similar tools confidently. | Registration is done by someone else, or CDU staff have skills similar to sellers. | Medium | Medium | V-03 | Unvalidated |
| H-11 | Central Administration staff use the system mostly to **query** (stock, accounts receivable) and charge only occasionally. | Staff describe querying as their main activity and sales as rare. | Central Administration sells as often as the satellite points. | Low | Medium | V-04 | Unvalidated |
| H-12 | Sellers at the satellite points rotate often (e.g. student assistants or shift staff) and get little training time. | More than one person covers each point; training is informal or on the job. | Each point has one stable seller with formal training. | Low | High | V-02, V-04 | Unvalidated |
| H-16 | Central Administration staff work at an office desk, mostly with a computer, and have medium digital skills (forms, spreadsheets, email). | Staff describe office work with a computer and use spreadsheets without help. | Staff work mainly from a phone or have low digital skills. | Low | Medium | V-04 | Unvalidated |
| H-17 | Sales at the CDU point are made by the same person who manages the inventory (P-02), not by a separate front-desk seller. | CDU staff describe one person doing both tasks. | CDU has a separate seller, who would receive modify permissions through the CDU profile. | Low | High | V-03, V-04 | Unvalidated |

### Context and devices

| ID | We believe that… | Right if… | Wrong if… | Confidence | Risk | Validation | Status |
|---|---|---|---|---|---|---|---|
| H-02 | The sales device is a low- or mid-range Android phone, possibly owned by the seller. | Device checklist shows Android phones with limited storage/RAM; some are personal. | Points have dedicated institutional devices (tablets, PCs) or high-end phones. | Medium | High | V-05, V-04, V-02 | Unvalidated |
| H-03 | Connectivity at the points of sale is intermittent or unavailable at times. | Connectivity tests at each point show drops or no signal at some times. | Stable Wi-Fi or data is available at every point during sales hours. | Medium | High | V-05, V-01 | Unvalidated — **challenged for the Matemáticas point (FMAT)** (see §6) |
| H-05 | Sales peak at specific times (start of semester, events, graduations), with queues and time pressure. | Sellers and records identify peak periods with queues. | Sales are spread evenly with no queues. | Medium | Medium | V-01, V-02, V-06 | Unvalidated |
| H-06 | The seller works with interruptions and sometimes with only one free hand. | Observation shows sellers handling products, cash or other duties while charging. | Sellers work at a fixed counter with both hands free. | Low | Medium | V-01, V-02 | Unvalidated |
| H-15 | Each warehouse (CDU, Sociales, Matemáticas) is also the point of sale where its stock is sold; "warehouse", "store" and "boutique" in the client's document refer to the same places. | The client confirms it (answers Q-13). | Some points sell from stock kept elsewhere, or there is a boutique separate from the warehouses. | Medium | High | V-04 (Q-13) | Unvalidated |

### Current process

| ID | We believe that… | Right if… | Wrong if… | Confidence | Risk | Validation | Status |
|---|---|---|---|---|---|---|---|
| H-04 | Inventory and sales are currently tracked manually or semi-manually (notebook or spreadsheets), and recorded stock differs from actual stock. | Current records are paper or spreadsheets; staff report or show count discrepancies. | A system already exists and stock matches physical counts. | Medium | Medium | V-03, V-06, V-01 | Unvalidated |
| H-08 | Interuady purchases are currently recorded with incomplete or late data, which makes collection harder. | Staff report missing data or late payments on Interuady notes. | Interuady notes are complete and collected without problems. | Low | Medium | V-04, V-06, V-01, V-02 | Unvalidated |
| H-10 | Card payments are charged on a separate bank terminal; the system only records the payment method. | Client confirms a separate terminal (answers Q-06). | Client expects integration with a payment terminal. | Medium | High | V-04 (Q-06) | Unvalidated |
| H-13 | Follow-up of Interuady accounts receivable is done by CDU or Central Administration, not by the satellite points. | Client/staff name CDU or Central Administration as responsible (answers Q-09). | Satellite sellers are expected to follow up on their own notes. | Low | Medium | V-04 (Q-09) | Unvalidated |

### Buyers

| ID | We believe that… | Right if… | Wrong if… | Confidence | Risk | Validation | Status |
|---|---|---|---|---|---|---|---|
| H-09 | Walk-in buyers are students, staff and visitors, and a typical sale includes few items. | Observation and records show mostly small sales to the university community. | Most sales are large orders or to external buyers. | Medium | Low | V-01, V-06 | Unvalidated |
| H-14 | Interuady purchases are made by staff of other UADY units, often for several items at once (e.g. events or uniforms). | Records or staff describe Interuady sales as larger institutional orders. | Interuady sales look like regular walk-in sales. | Low | Low | V-04, V-06, V-01, V-02 | Unvalidated |

## 4. Prioritization (assumption map)

Following assumptions mapping `[R9]`, hypotheses that are **important (high risk) and have little evidence (low or medium confidence)** are validated first in delivery 2.

| | **Low confidence** | **Medium confidence** |
|---|---|---|
| **High risk** | **H-12, H-17** | **H-01, H-02, H-03, H-10, H-15** |
| **Medium risk** | H-06, H-08, H-11, H-13, H-16 | H-04, H-05, H-07 |
| **Low risk** | H-14 | H-09 |

**Validation order:** H-01, H-02, H-03, H-12, H-17 (define the primary persona and technical constraints) → H-10, H-15, H-04 (define scope) → the rest.

## 5. Where each hypothesis is used

Generated from the same origin columns as the [traceability matrix](../04-requirements/traceability-matrix.md).

| Hypothesis | Proto-personas | Scenarios | Requirements | Project definition |
|---|---|---|---|---|
| H-01 | P-01 | S-01, S-02, S-03, S-07, S-08 | FR-03, FR-14, FR-29, NFR-01, NFR-02, NFR-06, NFR-07, NFR-09, NFR-10, NFR-25, NFR-28 | §2.1, §3.1, §4.2 ch. 1, §4.2 ch. 5, §4.3 |
| H-02 | P-01 | S-01, S-03, S-08 | NFR-13, NFR-14, NFR-19, NFR-20 | §2.1, §2.3, §4.2 ch. 2, §4.2 ch. 4, §4.3 |
| H-03 | P-01 | S-01, S-05 | FR-11, NFR-17 | §2.1 |
| H-04 | P-01, P-02, P-03 | S-05 | FR-31, FR-32, NFR-04 | §2.2, §3.2 |
| H-05 | P-01 | S-01, S-07 | FR-18, NFR-03, NFR-04, NFR-28 | — |
| H-06 | P-01 | S-01, S-03, S-07 | NFR-09, NFR-11 | — |
| H-07 | P-02 | S-04 | NFR-26 | §3.1, §4.2 ch. 5 |
| H-08 | P-03 | S-02, S-06 | FR-21, NFR-06 | §2.2 |
| H-09 | P-01 | S-01 | — | — |
| H-10 | — | S-03 | FR-19, NFR-21 | §4.2 ch. 4 |
| H-11 | P-03 | S-06 | NFR-27 | §4.2 ch. 1 |
| H-12 | P-01 | S-08 | FR-35, FR-38, NFR-01, NFR-05, NFR-19, NFR-25 | — |
| H-13 | P-02, P-03 | S-06 | — | — |
| H-14 | P-01 | S-02 | — | — |
| H-15 | P-01 | — | — | §1 |
| H-16 | P-03 | S-06 | FR-37, NFR-27 | — |
| H-17 | P-02 | — | — | — |

`V-xx` activities are described in the [validation plan](validation-plan.md). `[Rn]` sources are listed in [`references.md`](../references.md).

## 6. Evidence log

Every piece of evidence about a hypothesis is recorded here with its type. Only **systematic** evidence (from a `V-xx` activity) can change a hypothesis to *Validated* or *Refuted*.

| Date | Hypothesis | Evidence | Type | Effect |
|---|---|---|---|---|
| 2026-09-28 | H-03 | The author, a student at FMAT, reports that institutional Wi-Fi covers the whole faculty and that the boutique point is in the middle of the faculty; the author's own mobile data (Telcel) has signal there. Stability during sales hours was not measured; other carriers were not checked. The Sociales and CDU points were not observed. The point at FMAT is assumed to be the Matemáticas point, and the Matemáticas point is assumed to correspond to the Exact Sciences Campus profile (Q-03). | Author's prior knowledge (informal, not systematic) | H-03 is **challenged for the Matemáticas point (FMAT)** and remains unvalidated for Sociales and CDU. Offline operation stays a requirement regardless (`PRJ-02`). Systematic check planned in V-05. |
