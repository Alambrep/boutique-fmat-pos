# Non-functional requirements

> **Tasks:** T-07 (delivery 1), T-16 (delivery 2) · **Rubric criteria:** 4 (delivery 1); 1a, 1c (delivery 2) · **Status:** revised in delivery 2 — every change, with its reason, is in the [change log](changes.md). Delivery 1 version: [tag `delivery-1`](https://github.com/Alambrep/boutique-fmat-pos/blob/delivery-1/docs/04-requirements/non-functional-requirements.md).
>
> Organized by the five **usability quality components** defined by Nielsen — learnability, efficiency, memorability, errors, satisfaction `[R1]` — and consistent with the ISO 9241-11 view of usability as effectiveness, efficiency and satisfaction for specified users, goals and context of use `[R2]`. Accessibility and quality attributes that affect the user experience follow; sections 2–6 also state which usability component each requirement supports, and security, privacy and compatibility are kept as quality attributes because they shape what the user can do. `[Rn]` = source in [`references.md`](../references.md).
>
> Requirements marked **(H)** rest only on hypotheses (no CR or PRJ in their origin) and may change after validation.
>
> ⚠️ **All numeric targets are tentative design goals proposed by the author**, not measured values or findings. They will be calibrated with the evidence from the [validation plan](../02-research/validation-plan.md). Values taken from external guidelines cite their verified source `[Rn]`.

## 0. Usability specification

Which usability attributes this system considers, for whom, and at which level. The attributes are Nielsen's five quality components `[R1]`; the last column relates them to the ISO 9241-11 measures of effectiveness, efficiency and satisfaction `[R2]`. Each NFR below states its attribute and, in the column **Applies to**, whether it applies to the whole **system** or to particular functional requirements; the [FR ↔ NFR map](traceability-matrix.md#6-functional--non-functional-requirements) is generated from that column.

| Attribute | What it means for this system | Who it matters most for, and why | Level | Requirements | ISO 9241-11 measure |
|---|---|---|---|---|---|
| **Learnability** | A person who has never used the app completes a sale without help after a short demonstration | P-01: low digital skills and rotating staff with little training `[PRJ-03, H-01, H-12]` | System (language, labels, hints) and the sales flow | NFR-01, NFR-02, NFR-12, NFR-25 | Effectiveness (task success) |
| **Efficiency** | A sale is fast enough during a queue; CDU registers products and Central Administration finds notes without delay | P-01 during busy periods `[H-05]`; P-02 and P-03 for their main tasks `[CR-05…CR-09, CR-14]` | Particular requirements (sale, product registration, accounts receivable) and system performance | NFR-03, NFR-04, NFR-11, NFR-26, NFR-27; NFR-13…NFR-16 (perceived performance) | Efficiency (taps, time) |
| **Memorability** | A seller who has not sold for two weeks can still sell without help | P-01: shifts and occasional coverage `[H-12]` | The sales flow | NFR-05 | Effectiveness after a pause |
| **Errors** | Few errors; the ones that matter (Interuady data, a lost sale, an out-of-stock sale) are prevented or recoverable | P-01: data that the client requires `[CR-13]`; offline operation `[PRJ-02]` | Particular requirements (Interuady, sale, synchronization) and every error message | NFR-06, NFR-07, NFR-28, NFR-17, NFR-18 | Effectiveness (errors) |
| **Satisfaction** | Sellers find the app easy to use | P-01 `[PRJ-03]` | System | NFR-08 | Satisfaction (SUS) |
| *Accessibility (supports the five)* | Targets, contrast and one-handed use that make the components above possible on a small phone | P-01 `[PRJ-01, H-06]` | System | NFR-09, NFR-10, NFR-11 | — |

**Priority.** Learnability and errors come first, because the client asks for a system usable by a person with limited technology skills `[PRJ-03]` and because Interuady data is mandatory `[CR-13]`; efficiency follows, because sales may happen under time pressure `[H-05]`. This priority guides the selection of NFRs for the usability test (T-24).

## 1. Usability attributes

| ID | Attribute | Requirement | Tentative target | How it is measured | Applies to | Origin |
|---|---|---|---|---|---|---|
| NFR-01 | Learnability | A first-time seller (P-01) completes a cash sale without assistance after a demonstration of at most 2 minutes. | ≥ 80% of test participants complete the task on the first attempt. | Usability test (V-07) | FR-13, FR-16, FR-17, FR-18, FR-22 | PRJ-03, H-01, H-12 |
| NFR-02 | Learnability | The sales screens use everyday Spanish, with no technical terms (e.g. *sincronizar*, *servidor*, *base de datos*), and every icon has a visible text label `[R37]`. | 0 technical terms on the sales screens. | Heuristic inspection | System — sales screens (FR-13…FR-24, FR-29, FR-31…FR-33) | PRJ-03, H-01 |
| NFR-03 | Efficiency | A one-item cash sale takes at most 5 taps from the sales screen. | ≤ 5 taps, excluding typing the amount received. | Design inspection (task walkthrough) | FR-13, FR-16, FR-17, FR-18, FR-22 | CR-10, CR-11, H-05 |
| NFR-04 | Efficiency | A typical sale takes less time than the current process. **(H)** | Median time per sale ≥ 20% lower than the current median measured in V-01 (tentative). | Observation (V-01) vs. usability test (V-07) | FR-13, FR-16, FR-17, FR-22, FR-33 | H-04, H-05 |
| NFR-05 | Memorability | A seller who has not used the app for two weeks completes a sale without help. **(H)** | ≥ 80% of returning participants succeed. | Follow-up usability test (V-07) | FR-13, FR-16, FR-17, FR-22 | H-12 |
| NFR-06 | Errors — prevention | Sellers enter Interuady data correctly on the first attempt; the form prevents incomplete notes (FR-20) and makes the missing field obvious. | ≥ 80% of participants complete an Interuady sale without a validation error; when an error occurs, 100% identify the missing field without help. | Usability test (V-07), task based on S-02 | FR-20, FR-21 | CR-13, H-01, H-08 |
| NFR-07 | Errors — recovery | Error messages explain what happened and what to do next, in plain language. | 100% of error messages include a suggested action. | Heuristic inspection | System — every error message (e.g. FR-02, FR-18, FR-20, FR-32) | PRJ-03, H-01 |
| NFR-25 | Learnability | No mandatory tutorial: help appears as contextual hints, once, at the moment the user needs them. | 0 mandatory onboarding screens; each hint shown at most once per user. | Design inspection; usability test (V-07) | System — first use (FR-03, FR-35) | PRJ-03, H-01, H-12, DI-26 |
| NFR-26 | Efficiency | CDU staff (P-02) register a new product with photo, barcode and initial stock per warehouse without assistance. | Median ≤ 3 min per product after one practice product (tentative). | Usability test (V-07), task based on S-04 | FR-04, FR-05, FR-06, FR-08, FR-36 | CR-05…CR-09, H-07 |
| NFR-27 | Efficiency | Central Administration staff (P-03) find the pending Interuady notes of a given unit. | ≥ 80% of participants succeed in ≤ 1 min without assistance (tentative). | Usability test (V-07), task based on S-06 | FR-25 | CR-14, H-11, H-16 |
| NFR-28 | Errors — frequency | Participants make few errors while completing the key sales tasks (cash, card and Interuady sale). | ≤ 1 error per task on average, and 0 errors that the participant cannot recover from without help (tentative). | Error count in the usability test (V-07) | FR-17, FR-19, FR-20, FR-33 | PRJ-03, H-01, H-05 |
| NFR-08 | Satisfaction | Participants with the P-01 profile give the app a mean SUS score of at least 68. | SUS score ≥ 68, the average SUS score across published evaluations `[R5]`. | SUS questionnaire after the usability test (V-07) | System | PRJ-03 |

## 2. Accessibility and ergonomics

| ID | Attribute | Requirement | Tentative target | How it is measured | Applies to | Origin |
|---|---|---|---|---|---|---|
| NFR-09 | Errors — prevention; Efficiency | Touch targets are large enough for fast, error-free use. **(H)** | ≥ 48 × 48 dp, the Android recommendation for touch targets `[R4]`. | Design inspection | System | H-01, H-06 |
| NFR-10 | Accessibility (supports Efficiency and Errors) | Text has enough contrast to be read in varied lighting. **(H)** | ≥ 4.5:1 for normal text and ≥ 3:1 for large text (WCAG 2.2, SC 1.4.3, level AA) `[R3]`. | Contrast checker on Figma designs | System | H-01 |
| NFR-11 | Efficiency | The main sales actions (add, change quantity, *Cobrar*, *Confirmar venta*) are placed where the thumb of the hand holding the phone reaches them `[R38]`. **(H)** | Primary actions placed in the lower half of the screen. | Design inspection | FR-13, FR-16, FR-17, FR-33 | H-06 |
| NFR-12 | Learnability | The user interface is in Spanish, the language of the client and users. | 100% of UI text. | Inspection | System | PRJ-03 |

## 3. Performance on low-end devices

| ID | Attribute | Requirement | Tentative target | How it is measured | Applies to | Origin |
|---|---|---|---|---|---|---|
| NFR-13 | Efficiency (perceived performance) | The app runs on a low-end Android reference phone. | Until V-05 defines the reference device: 2 GB of RAM and Android 10 as a tentative lower bound (author's design goal, not a measured value). | Device test (V-08) | System | PRJ-01, H-02, Q-12 |
| NFR-14 | Efficiency (perceived performance) | The sales screen is shown at most 3 s after tapping the app icon on the reference device. | ≤ 3 s from tapping the app icon (author's tentative target; no external benchmark verified yet). | Device test (V-08) | FR-03, FR-13 | PRJ-01, H-02 |
| NFR-15 | Efficiency (perceived performance) | Product photos shown on the sales screen are thumbnails of at most 100 KB; full-size photos are kept only on CDU devices. | Tentative: ≤ 100 KB per thumbnail, and the catalog of one warehouse fits in ≤ 50 MB; full-size photos kept only at CDU. | Device test (V-08) | FR-05, FR-13 | CR-06, CR-10, PRJ-01, DI-14 |
| NFR-16 | Efficiency (perceived performance) | Each satellite device (Sociales, Matemáticas) stores only its own warehouse's catalog; CDU and Central Administration devices may store all three. | 1 warehouse per satellite device. | Inspection | FR-13, FR-28 | PRJ-01, CR-08, CR-01, CR-02 |

## 4. Reliability and offline operation

| ID | Attribute | Requirement | Tentative target | How it is measured | Applies to | Origin |
|---|---|---|---|---|---|---|
| NFR-17 | Errors — recovery (perceived reliability) | No confirmed sale is lost if the connection drops or the app is closed. | 0 lost sales in offline tests. | Offline test with forced disconnection (V-08) | FR-22, FR-27 | PRJ-02, H-03 |
| NFR-18 | Errors — recovery (perceived reliability) | Queued sales synchronize automatically after connectivity returns. | ≤ 1 min after reconnection. | Offline test (V-08) | FR-28 | PRJ-02 |

## 5. Security and privacy

| ID | Attribute | Requirement | Tentative target | How it is measured | Applies to | Origin |
|---|---|---|---|---|---|---|
| NFR-19 | Security (quality attribute) | The session locks after a period of inactivity; unlocking is a single step. | Lock after ≤ 5 min of inactivity (to confirm with the client, Q-11); after unlocking, the app returns to the sales screen. | Functional test | FR-35 | CR-01…CR-04, H-02, H-12, Q-11, DI-27 |
| NFR-20 | Security (quality attribute) | Personal data from Interuady notes stored on a device is encrypted at rest. Devices of charge-only profiles keep only each note's number, unit, amount, date and status; personal details are stored only on devices of profiles with query permission (depends on FR-26). | 100% of locally stored personal data encrypted; 0 personal-detail fields on charge-only devices. | Local storage inspection (V-08) | FR-24, FR-26 | CR-13, CR-14, PRJ-02, H-02 |
| NFR-21 | Privacy and compliance (quality attribute) | The system never stores card data, to stay outside the scope of PCI DSS `[R16]`. | 0 card data fields in the data model. | Data model review | FR-19 | CR-12, H-10 |
| NFR-22 | Privacy and compliance (quality attribute) | Interuady data handling follows the applicable personal data law for public-sector entities. | Checklist, to be completed before implementation: privacy notice available (FR-39); only the three client fields collected; access limited by profile (FR-26); local data encrypted (NFR-20); synchronized personal details removed from charge-only devices. Legal review of the specific articles of `[R17, R18]` pending. | Checklist review | FR-20, FR-24, FR-26, FR-39 | CR-13, CR-14, Q-04 |

## 6. Compatibility

| ID | Attribute | Requirement | Tentative target | How it is measured | Applies to | Origin |
|---|---|---|---|---|---|---|
| NFR-23 | Compatibility (supports Efficiency) | Support external barcode scanners that work as a keyboard (keyboard-wedge / HID mode, USB or Bluetooth) `[R13]`. | Works with at least one available scanner. | Device test (V-08) | FR-15 | CR-16 |
| NFR-24 | Compatibility (supports Efficiency) | Support printing receipts on a Bluetooth thermal printer (support depends on the platform decision, since Web Bluetooth is experimental and not available on iOS `[R14, R15]`). | Works with at least one available printer. | Device test (V-08) | FR-07, FR-23 | CR-17 |
