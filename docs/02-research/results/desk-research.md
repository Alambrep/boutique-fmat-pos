# Desk research results — Delivery 1

> **Tasks:** T-02, T-09 · **Rubric criteria:** 1, 2 · **Date:** 2026-09-28/29
>
> **Method:** secondary research — official statistics, official product documentation, current laws, standards and guidelines. Each source was opened and the statement checked against it (see [`references.md`](../../references.md)).
> **Scope:** these results describe the **context**, not the users. They do **not** validate any user hypothesis; field research is planned in the [validation plan](../validation-plan.md).

## DR-1 — Existing solutions

| Result | Sources | Implication |
|---|---|---|
| Loyverse sells offline and handles price and stock per store in its free core; offline, it cannot show stock levels or process refunds. | R22, R23, R24 | Offline sales and multi-store are **not** differentiators; full offline operation including stock is (D3). |
| Loyverse and Shopify POS allow custom named payment methods for tracking; no mandatory fields per payment method or automatic receivables were found in their documentation. | R25, R27 | The Interuady flow is the main differentiator (D1). |
| Square card acceptance is not available in Mexico. | R29 | Excluded from the comparison. |
| Clip Total 3 is a dedicated terminal with inventory and a built-in printer; no multi-branch management is mentioned. | R28 | This project targets phones already available (D4). |

## DR-2 — Social context

| Result | Sources | Implication |
|---|---|---|
| In 2025, 86.1% of people aged 6+ used the internet and 97.0% of cell phone users used a smartphone. | R20 | The phone is the right channel (PRJ-01). |
| Only 22.3% of micro establishments used computers and 23.5% used the internet (Economic Census 2024). | R21 | Micro establishments make little use of digital tools. The data does not measure skills; that the cause is skills and tool fit is H-01, to be validated. |

## DR-3 — Legal framework for personal data

| Result | Sources | Implication |
|---|---|---|
| A new federal general law on personal data held by public entities was published on 2025-03-20. | R17 | Interuady data (the responsible and requester fields, if they hold names; Q-04) must follow it (NFR-22). |
| Yucatán issued a new state law on 2025-08-28 that covers autonomous bodies; it abrogated the 2017 law. | R18 | Same; privacy notice and minimization (FR-26, NFR-20). |
| UADY issues its privacy notices under the general law for obligated subjects. | R19 | The project must align with the institution's privacy notices. |
| PCI DSS applies to entities that store, process or transmit cardholder data. | R16 | Never capture card data (FR-19, NFR-21). |

## DR-4 — Technical feasibility

| Result | Sources | Implication |
|---|---|---|
| Keyboard-wedge scanners send barcodes as keystrokes. | R13 | Scanner support needs no special integration (FR-15, NFR-23). |
| Web Bluetooth is experimental and not Baseline; it works in Chrome for Android but iOS is not listed. | R14, R15 | Printing from a PWA is limited; input for the PWA-or-native decision (NFR-24). |
| Local-first software keeps the primary data on the device and syncs later. | R12 | Architecture approach for offline operation (FR-27, FR-28). |

## DR-5 — Requirements analysis of the client's document

| Result | Source | Implication |
|---|---|---|
| 14 points are undefined, including the meaning of CDU and C.P., how 4 profiles map to 3 warehouses, whether warehouses are also points of sale, VAT, transfers and card payments. | [Client requirements](../../../client/client-requirements.md) | Open questions Q-01…Q-14; six functional requirements deferred (FR-D1…FR-D6). |

## Informal evidence (not systematic)

| Hypothesis | Evidence | Status |
|---|---|---|
| H-03 | Author's prior knowledge: Wi-Fi covers the faculty and the author's mobile data has signal at the FMAT point. | Challenged for the FMAT point only; see the [evidence log](../hypotheses.md#6-evidence-log). |
