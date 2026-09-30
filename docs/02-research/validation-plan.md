# Research and validation plan

> **Task:** T-09 · **Rubric criterion:** 2 · **Status:** plan for delivery 2 (not executed yet)
>
> Purpose: turn the unvalidated [hypotheses](hypotheses.md) into evidence, and replace the [proto-personas](../03-user-modeling/proto-personas.md) with research-based personas, as Lean UX recommends for assumption-based personas `[R6, R7]`. Sources `[Rn]` are listed in [`references.md`](../references.md).

## 1. Research questions

| ID | Question | Hypotheses |
|---|---|---|
| RQ-1 | Who sells at each point, what digital skills do they have, and how are they trained? | H-01, H-07, H-11, H-12, H-16, H-17 |
| RQ-2 | With which devices and connectivity do they work at each point? | H-02, H-03 |
| RQ-3 | Where is stock kept and sold, how are sales, stock and Interuady payments recorded today, and what goes wrong? | H-04, H-08, H-10, H-13, H-15 |
| RQ-4 | Under what conditions do sales happen (peaks, interruptions, typical basket)? | H-05, H-06, H-09, H-14 |
| RQ-5 | Can the target users complete the key tasks with the proposed design? | NFR-01…NFR-08 (delivery 2–3) |

## 2. Activities

Order follows the [prioritization](hypotheses.md#4-prioritization-assumption-map): important hypotheses with little evidence first `[R9]`.

| ID | Activity | Method | Participants (tentative) | Instrument | Hypotheses | When |
|---|---|---|---|---|---|---|
| V-01 | Observation at the points of sale | Contextual inquiry: observe sellers at work and ask about what they do, in their own environment `[R30]` | Sellers at FMAT, Sociales and CDU; 1–2 sessions of 30–45 min per point | [Observation guide](instruments/observation-guide.md) | H-01, H-03, H-04, H-05, H-06, H-08, H-09, H-14; baseline sale time (NFR-04) | Week 1 |
| V-02 | Seller interviews | Semi-structured interview | 3–5 sellers (all points) | [Seller interview guide](instruments/seller-interview-guide.md) | H-01, H-02, H-05, H-06, H-08, H-12, H-14 | Week 1–2 |
| V-03 | CDU interview | Semi-structured interview + walkthrough of current records | 1–2 CDU staff | [Staff interview guide](instruments/staff-interview-guide.md) | H-04, H-07, H-17 | Week 1–2 |
| V-04 | Client and Central Administration interview | Semi-structured interview; answers to Q-01…Q-16 | Client (professor); 1 Central Administration officer; 1 accounting contact referred by the client (Q-05) | [Staff interview guide](instruments/staff-interview-guide.md) + [open questions](../../client/client-requirements.md#open-questions-for-the-client) | H-02, H-08, H-10, H-11, H-12, H-13, H-14, H-15, H-16, H-17 | Week 1 |
| V-05 | Device and connectivity check | Checklist at each point (device model, OS, storage; Wi-Fi and mobile data tests at different times) | Author, with permission of each point | [Device and connectivity checklist](instruments/device-connectivity-checklist.md) | H-02, H-03 | Week 1 |
| V-06 | Review of current records | Document analysis of anonymized sales, stock and Interuady records (no personal data copied) | Records provided by CDU / client | Record review sheet (staff interview guide, part C) | H-04, H-05, H-08, H-09, H-14 | Week 2 |
| V-07 | Usability test | Task-based test with a Figma prototype; think-aloud; SUS questionnaire `[R5]` | 5 participants per round, iterating between rounds `[R31]`. P-01 profile first: real sellers when available; otherwise proxy participants who match P-01 on the recruitment criteria below. Returning participants repeat one task two weeks later (NFR-05) | Test script (delivery 2) | NFR-01…NFR-08; D2, D5 | Delivery 2–3 |
| V-08 | Technical device test | Performance and offline tests on a reference low-end phone; scanner and printer tests | Author | Test protocol (delivery 3) | NFR-13…NFR-18, NFR-23, NFR-24 | Delivery 3 |

**Mapping rule:** the *Hypotheses* column lists every hypothesis for which the activity's instrument collects evidence. The *Validation* column in [`hypotheses.md`](hypotheses.md) lists the same activities.

**Recruitment criteria for P-01 proxies (V-07):** does not work in software or IT; uses the phone mainly for calls, messaging and social media; has not used a point-of-sale app. The number of real sellers versus proxies is reported with the results.

## 3. Data to collect and analysis

| Data | Collected in | Analysis | Output |
|---|---|---|---|
| Field notes and interview notes | V-01, V-02, V-03, V-04 | Affinity diagramming: cluster observations into themes `[R32]`; thematic analysis for recurring patterns `[R33]` | Findings list with evidence, in `results/` |
| Device and connectivity measurements | V-05 | Tabulation per point and time of day | Connectivity and device table |
| Current process records | V-06 | Counts: sales per period, basket size, Interuady notes with missing data | Baseline metrics (e.g. current time per sale for NFR-04) |
| Task success, time, errors, SUS | V-07 | Success rate, time on task, error count; SUS score vs. average of 68 `[R5]`. Times from a prototype test are not directly comparable with times from real sales (V-01); the comparison is indicative until measured on a working version (delivery 3). | Usability report |

**Decision rule for each hypothesis:** after analysis, every hypothesis is updated in the [evidence log](hypotheses.md#6-evidence-log), citing the finding:

- **Validated:** the *Right if…* signal is observed at **at least two of the three points** (or, for hypotheses about one role, in **most participants of that role**, stating the count, e.g. "3 of 4"), and the *Wrong if…* signal is not observed.
- **Refuted:** the *Wrong if…* signal is observed at two or more points or in most participants of the role.
- **Partially validated:** the evidence is mixed, or the hypothesis has two clauses and only one holds; the finding states which clause holds.
- **Inconclusive:** not enough participants or observations; the hypothesis stays *Unvalidated* and the gap is recorded.

Proto-personas, scenarios and requirements that trace to an updated hypothesis are revised using the [traceability matrix](../04-requirements/traceability-matrix.md).

## 4. Ethics and personal data

- **Informed consent:** each participant is told the purpose, that participation is voluntary and that they can stop at any time; consent is recorded before starting (script in each guide).
- **Anonymization:** participants are identified by codes (e.g. `SEL-01`, `CDU-01`); no names are stored in the repository.
- **No photos or recordings of people** without explicit consent; photos of the points of sale are taken without people.
- **Records:** only aggregated or anonymized data is copied from current records; Interuady notes are never copied with personal data.
- **Framework:** UADY handles personal data under the law for public-sector entities `[R17, R18, R19]`; the research follows the same data minimization principle.

## 5. Schedule

Delivery 2 date is not yet known; weeks are counted from the start of delivery 2 work.

| Week | Activities |
|---|---|
| 1 | V-04 (client, answers to Q-01…Q-16), V-05 (devices and connectivity), V-01 (observation) |
| 2 | V-02 (sellers), V-03 (CDU), V-06 (records) |
| 3 | Analysis; update hypotheses, personas, scenarios and requirements |
| Delivery 2–3 | V-07 (usability test with prototype), V-08 (technical tests) |

## 6. Risks for the research

| Risk | Mitigation |
|---|---|
| Staff not available or not willing to participate | Ask the client to introduce the project to the staff; keep sessions short (≤ 30 min) |
| Points closed or with no sales during the visit | Plan visits in expected peak times (to be confirmed in V-04) |
| Individual work limits the number of sessions | Prioritize V-04, V-05 and V-01, which address the highest-risk hypotheses |
