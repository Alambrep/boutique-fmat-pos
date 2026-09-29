# Traceability matrix

> **Task:** T-08 · **Rubric criteria:** 2, 4 · **Status:** delivery 1
>
> Shows, for every client requirement (`CR`), project requirement (`PRJ`) and hypothesis (`H`), which proto-personas (`P`), scenarios (`S`), functional requirements (`FR`) and non-functional requirements (`NFR`) depend on it. It was generated from the origin columns of each artifact, so it reflects exactly what those documents cite.
>
> Use it in both directions: **forward** (is every client requirement covered?) and **backward** (if a hypothesis is refuted in delivery 2, what must be revised?).

## 1. Matrix

| Origin | Proto-personas | Scenarios | Functional requirements | Non-functional requirements |
|---|---|---|---|---|
| CR-01 | P-02 | S-04 | FR-01, FR-02, FR-09, FR-10, FR-26 | NFR-12, NFR-19 |
| CR-02 | P-03 | S-06 | FR-01, FR-02, FR-10, FR-26 | NFR-12, NFR-19 |
| CR-03 | P-01 | S-01, S-02, S-03 | FR-01, FR-02 | NFR-12, NFR-19 |
| CR-04 | P-01 | S-01, S-02, S-03 | FR-01, FR-02 | NFR-12, NFR-19 |
| CR-05 | P-02 | S-04 | FR-04 | — |
| CR-06 | P-02 | S-04 | FR-05 | NFR-15 |
| CR-07 | P-02 | S-04 | FR-06, FR-07 | — |
| CR-08 | P-01, P-02, P-03 | S-04, S-05 | FR-04, FR-08, FR-10 | NFR-16 |
| CR-09 | P-02 | S-04 | FR-08, FR-09, FR-28 | — |
| CR-10 | P-01, P-03 | S-01, S-03, S-06 | FR-13, FR-14 | NFR-03, NFR-15 |
| CR-11 | P-01, P-03 | S-01, S-06 | FR-16 | NFR-03 |
| CR-12 | P-01, P-03 | S-01, S-02, S-03, S-06 | FR-17, FR-19 | NFR-21 |
| CR-13 | P-01, P-03 | S-02, S-06 | FR-20, FR-26 | NFR-06, NFR-20, NFR-22 |
| CR-14 | P-03 | S-02, S-06 | FR-24, FR-25, FR-26 | NFR-22 |
| CR-15 | P-01, P-02 | S-01, S-05 | FR-12, FR-22, FR-28 | — |
| CR-16 | — | S-03 | FR-15 | NFR-23 |
| CR-17 | — | — | FR-23 | NFR-24 |
| CR-18 | — | — | FR-23 | — |
| PRJ-01 | P-01, P-02 | S-01 | — | NFR-13, NFR-14, NFR-15, NFR-16 |
| PRJ-02 | P-01, P-02 | S-01, S-05 | FR-02, FR-11, FR-12, FR-27, FR-28, FR-29 | NFR-17, NFR-18, NFR-20 |
| PRJ-03 | P-01 | — | FR-29 | NFR-01, NFR-02, NFR-07, NFR-08 |

### Hypotheses

| Origin | Proto-personas | Scenarios | Functional requirements | Non-functional requirements |
|---|---|---|---|---|
| H-01 | P-01 | S-01, S-02, S-03 | FR-03, FR-14, FR-29 | NFR-01, NFR-02, NFR-07, NFR-09, NFR-10 |
| H-02 | P-01, P-02 | S-01, S-03 | — | NFR-13, NFR-14, NFR-19, NFR-20 |
| H-03 | P-01 | S-01, S-05 | FR-11 | NFR-17 |
| H-04 | P-01, P-02 | S-05 | — | NFR-04 |
| H-05 | P-01 | S-01 | FR-18 | NFR-03, NFR-04 |
| H-06 | P-01 | S-01, S-03 | — | NFR-09, NFR-11 |
| H-07 | P-02 | S-04 | — | — |
| H-08 | P-03 | S-02, S-06 | FR-21 | NFR-06 |
| H-09 | P-01 | S-01 | — | — |
| H-10 | — | S-03 | FR-19 | NFR-21 |
| H-11 | P-03 | S-06 | — | — |
| H-12 | P-01 | — | — | NFR-01, NFR-05 |
| H-13 | P-02, P-03 | S-06 | — | — |
| H-14 | P-01 | S-02 | — | — |

## 2. Coverage checks

| Check | Result |
|---|---|
| Every client and project requirement (CR-01…CR-18, PRJ-01…PRJ-03) is covered by at least one FR or NFR | ✔ Yes |
| Every FR and NFR cites at least one CR, PRJ or H | ✔ Yes (see the origin column of each requirement) |
| Every proto-persona is traced to client requirements and hypotheses | ✔ Yes (see [proto-personas](../03-user-modeling/proto-personas.md)) |
| All four client profiles are covered by a proto-persona | ✔ Yes (CR-01 → P-02, CR-02 → P-03, CR-03/CR-04 → P-01) |
| CR-18 (VAT and invoicing) | ⚠ Only partially covered by FR-23; full coverage deferred (FR-D1, Q-05) |

## 3. Impact if a hypothesis is refuted

- **Hypotheses that only shape the user model** (H-07, H-09, H-11, H-13, H-14): refuting them changes proto-personas and scenarios, not requirements.
- **Hypotheses with the widest impact** (H-01, H-02): they drive the most NFRs; they are first in the validation order (see [hypotheses §4](../02-research/hypotheses.md#4-prioritization-assumption-map)).
- **Requirements marked (H)** in the [functional requirements](functional-requirements.md) (FR-03, FR-18, FR-21) are the first candidates to change.
