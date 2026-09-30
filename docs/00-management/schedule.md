# Schedule

> **Task:** T-10 · **Rubric criterion:** 2 · **Owner of every task:** Alancete (individual project)
>
> Actual dates and times come from the git history and GitHub issues; see the [task log](task-log.md) and [logbook](logbook/).

**How this schedule was built.** The project was assigned on 2026-08-14 (see the [meeting log](meetings.md)); the work recorded in this repository started on 2026-09-28. Tasks T-01…T-13 were registered as issues on 2026-09-28 at 23:26, after work had begun, so the *Planned* dates in §2 were set on that day and are not evidence of earlier planning. §4 records what actually happened.

**Lesson learned for delivery 2.** Compressing delivery 1 into two days confirmed the time risk identified in the [project definition](../01-definition/project-definition.md#43-project-risks). From delivery 2 on, each task is created as an issue with an estimate **before** work starts, and the schedules in §5 and §6 get real dates as soon as each delivery date is announced.

## 1. Project roadmap

| Delivery | Branch | Focus | Due date | Status |
|---|---|---|---|---|
| 1 | `first-delivery` | Project definition, hypothesis-based user modeling (proto-personas), initial requirements, research plan | 2026-09-30 | In progress |
| 2 | `second-delivery` | User research (V-01…V-06), research-based personas, low-fidelity prototype, first usability test (V-07) | To be announced | Planned |
| 3 | `third-delivery` | Iterated prototype, usability testing, technical tests (V-08) | To be announced | Planned |

## 2. Delivery 1 — activities

| Task | Activity | Artifact | Planned | Actual (commit dates) | Status |
|---|---|---|---|---|---|
| T-01 | Repository structure, README, client requirements | `README.md`, `client/` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-02 | Project definition (relevance, innovation, feasibility) | `docs/01-definition/project-definition.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-03 | User hypotheses | `docs/02-research/hypotheses.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-04 | Proto-personas | `docs/03-user-modeling/proto-personas.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-05 | Scenarios | `docs/03-user-modeling/scenarios.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-06 | Functional requirements | `docs/04-requirements/functional-requirements.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-07 | Non-functional requirements | `docs/04-requirements/non-functional-requirements.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-08 | Traceability matrix | `docs/04-requirements/traceability-matrix.md` | 2026-09-28 | 2026-09-28 → 2026-09-29 | Done |
| T-09 | Research and validation plan + instruments | `docs/02-research/` | 2026-09-28 | 2026-09-29 | Done |
| T-10 | Schedule | `docs/00-management/schedule.md` | 2026-09-29 | 2026-09-29 | Done |
| T-11 | Logbook and task log | `docs/00-management/` | Every session | Every session | Ongoing |
| T-12 | Individual contribution metrics | `docs/00-management/contribution-metrics.md` | 2026-09-29 | 2026-09-29 | Done (updated at close) |
| T-13 | Presentation video | `docs/05-presentation/` | 2026-09-29 | 2026-09-29 (folder); video pending | Pending |

## 3. Remaining steps for delivery 1 (due 2026-09-30)

| # | Step | Task |
|---|---|---|
| 1 | Optional: connectivity check at the Matemáticas point (FMAT) with the [checklist](../02-research/instruments/device-connectivity-checklist.md) | T-09 (V-05) |
| 2 | Record the video and add it (or its link) to `docs/05-presentation/` | T-13 |
| 3 | Update logbook and contribution metrics with the final session | T-11, T-12 |
| 4 | Open a Pull Request `first-delivery` → `main`, merge it and tag `delivery-1` | T-01 |
| 5 | Submit the repository link | — |

## 4. Timeline

Delivery 1 was executed in work sessions (see the [logbook](logbook/)). The chart shows **sessions**, not task durations: several tasks were worked on in the same session, and commit times only mark when work was saved.

```mermaid
gantt
  title Delivery 1 — work sessions (actual, approximate)
  dateFormat YYYY-MM-DD HH:mm
  axisFormat %d %H:%M
  section 2026-09-28
  S1 Repository, client requirements (T-01, T-02) :done, 2026-09-28 19:35, 2026-09-28 20:20
  S2 Definition, hypotheses, personas, scenarios, FR, NFR, sources (T-02 … T-08, T-11) :done, 2026-09-28 22:30, 2026-09-29 00:00
  section 2026-09-29
  S3 POS comparison, research plan, schedule, metrics (T-02, T-09 … T-12) :done, 2026-09-29 00:00, 2026-09-29 00:35
  S4 Independent review and fixes across artifacts (T-01 … T-12) :active, 2026-09-29 17:39, 2026-09-29 19:00
  S5 Presentation video (T-13) :active, 2026-09-29 19:00, 2026-09-29 21:00
```

## 5. Delivery 2 — planned activities (dates to be set when announced)

Each task is created as an issue with its estimated hours before work starts; actual hours are recorded when it closes.

| Week | Activities | Tasks (to be created) |
|---|---|---|
| 1 | Client interview and open questions Q-01…Q-16, including the accounting contact for Q-05 (V-04); device and connectivity check (V-05); observation (V-01) | T-14…T-16 |
| 2 | Seller interviews (V-02); CDU interview (V-03); records review (V-06) | T-17…T-19 |
| 3 | Analysis; update hypotheses, personas, scenarios and requirements | T-20…T-21 |
| 4 | Low-fidelity prototype in Figma; first usability test (V-07) | T-22…T-23 |

## 6. Delivery 3 — planned activities (dates to be set when announced)

| Week | Activities | Tasks (to be created) |
|---|---|---|
| 1 | Iterate the prototype on the V-07 findings | T-24 |
| 2 | Second usability round (V-07), including the two-week memorability task (NFR-05) | T-25 |
| 3 | Technical tests on a reference low-end phone: performance, offline, scanner and printer (V-08) | T-26 |
| 4 | Final requirements revision, report and presentation | T-27…T-28 |
