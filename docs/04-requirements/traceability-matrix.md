# Traceability matrix

> **Task:** T-08 · **Rubric criteria:** 3, 4 · **Status:** delivery 1
>
> Shows, for every client requirement (`CR`), project requirement (`PRJ`) and hypothesis (`H`), which proto-personas (`P`), scenarios (`S`), functional requirements (`FR`) and non-functional requirements (`NFR`) depend on it. It was generated from the origin columns of each artifact, so it reflects exactly what those documents cite.
>
> Use it in both directions: **forward** (is every client requirement covered?) and **backward** (if a hypothesis is refuted in delivery 2, what must be revised?).

## 1. Matrix

Regenerated on 2026-09-29 after the internal review (adds FR-30…FR-37, NFR-25, S-07, S-08, H-15…H-17).

| Origin | Proto-personas | Scenarios | Functional requirements | Non-functional requirements |
|---|---|---|---|---|
| CR-01 | P-02 | S-04 | FR-01, FR-02, FR-09, FR-10, FR-26, FR-34, FR-35, FR-37 | NFR-19 |
| CR-02 | P-03 | S-06 | FR-01, FR-02, FR-10, FR-26, FR-35, FR-37 | NFR-19 |
| CR-03 | P-01 | S-01, S-02, S-03, S-07, S-08 | FR-01, FR-02, FR-31, FR-35 | NFR-19 |
| CR-04 | P-01 | S-01, S-02, S-03, S-07, S-08 | FR-01, FR-02, FR-31, FR-35 | NFR-19 |
| CR-05 | P-02 | S-04 | FR-04, FR-36 | — |
| CR-06 | P-02 | S-04 | FR-05, FR-36 | NFR-15 |
| CR-07 | P-02 | S-04 | FR-06, FR-07, FR-36 | — |
| CR-08 | P-01, P-02, P-03 | S-04, S-05 | FR-04, FR-08, FR-10, FR-36 | NFR-16 |
| CR-09 | P-02 | S-04 | FR-08, FR-09, FR-28, FR-34 | — |
| CR-10 | P-01, P-03 | S-01, S-03, S-06, S-07 | FR-13, FR-14 | NFR-03, NFR-15 |
| CR-11 | P-01, P-03 | S-01, S-03, S-06, S-07 | FR-16, FR-33 | NFR-03 |
| CR-12 | P-01, P-03 | S-01, S-02, S-03, S-06 | FR-17, FR-19, FR-33 | NFR-21 |
| CR-13 | P-01, P-03 | S-02, S-06 | FR-20, FR-26 | NFR-06, NFR-20, NFR-22 |
| CR-14 | P-03 | S-02, S-06 | FR-24, FR-25, FR-26, FR-37 | NFR-20, NFR-22 |
| CR-15 | P-01, P-02 | S-01, S-05, S-07 | FR-12, FR-22, FR-28, FR-31, FR-32 | — |
| CR-16 | — | S-03 | FR-15 | NFR-23 |
| CR-17 | — | S-01 | FR-23 | NFR-24 |
| CR-18 | — | — | FR-23 | — |
| PRJ-01 | P-01, P-02 | S-01 | — | NFR-13, NFR-14, NFR-15, NFR-16 |
| PRJ-02 | P-01, P-02 | S-01, S-05, S-08 | FR-11, FR-12, FR-27, FR-28, FR-29, FR-30, FR-32, FR-34, FR-35 | NFR-17, NFR-18, NFR-20 |
| PRJ-03 | P-01 | S-07, S-08 | FR-29 | NFR-01, NFR-02, NFR-07, NFR-08, NFR-12, NFR-25 |

### Hypotheses

| Origin | Proto-personas | Scenarios | Functional requirements | Non-functional requirements |
|---|---|---|---|---|
| H-01 | P-01 | S-01, S-02, S-03, S-07, S-08 | FR-03, FR-14, FR-29 | NFR-01, NFR-02, NFR-07, NFR-09, NFR-10, NFR-25 |
| H-02 | P-01 | S-01, S-03, S-08 | — | NFR-13, NFR-14, NFR-19, NFR-20 |
| H-03 | P-01 | S-01, S-05 | FR-11 | NFR-17 |
| H-04 | P-01, P-02, P-03 | S-05 | FR-31, FR-32 | NFR-04 |
| H-05 | P-01 | S-01, S-07 | FR-18 | NFR-03, NFR-04 |
| H-06 | P-01 | S-01, S-03, S-07 | — | NFR-09, NFR-11 |
| H-07 | P-02 | S-04 | — | — |
| H-08 | P-03 | S-02, S-06 | FR-21 | NFR-06 |
| H-09 | P-01 | S-01 | — | — |
| H-10 | — | S-03 | FR-19 | NFR-21 |
| H-11 | P-03 | S-06 | — | — |
| H-12 | P-01 | S-08 | FR-35 | NFR-01, NFR-05, NFR-19, NFR-25 |
| H-13 | P-02, P-03 | S-06 | — | — |
| H-14 | P-01 | S-02 | — | — |
| H-15 | P-01 | — | — | — |
| H-16 | P-03 | S-06 | FR-37 | — |
| H-17 | P-02 | — | — | — |

## 2. Coverage checks

| Check | Result |
|---|---|
| Every client and project requirement (CR-01…CR-18, PRJ-01…PRJ-03) is covered by at least one FR or NFR | ✔ Yes |
| Every FR and NFR cites at least one CR, PRJ or H | ✔ Yes (see the origin column of each requirement) |
| Every proto-persona is traced to client requirements and hypotheses | ✔ Yes (see [proto-personas](../03-user-modeling/proto-personas.md)) |
| All four client profiles are covered by a proto-persona | ✔ Yes (CR-01 → P-02, CR-02 → P-03, CR-03/CR-04 → P-01) |
| CR-18 (VAT and invoicing) | ⚠ Only partially covered by FR-23; full coverage deferred (FR-D1, Q-05) |
| H-15 (warehouse = point of sale) | ⚠ Only used in the project definition; if refuted, FR-13, FR-22 and FR-31 must be revised |
| H-16 (Central Administration context) | Shapes P-03 and FR-37 |
| H-17 (CDU counter) | If refuted, a fifth profile or a restricted CDU sales screen is needed (Q-11); affects FR-01 and FR-09 |

## 3. Impact if a hypothesis is refuted

- **Hypotheses that only shape the user model** (H-07, H-09, H-11, H-13, H-14): refuting them changes proto-personas and scenarios, not requirements.
- **Hypotheses with the widest impact** (H-01, H-02): they drive the most NFRs; they are first in the validation order (see [hypotheses §4](../02-research/hypotheses.md#4-prioritization-assumption-map)).
- **Requirements marked (H)** in the [functional requirements](functional-requirements.md) (FR-03, FR-18, FR-19, FR-21, FR-31, FR-32, FR-37) are the first candidates to change.
