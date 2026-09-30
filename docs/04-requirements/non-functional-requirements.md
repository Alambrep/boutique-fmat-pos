# Non-functional requirements

> **Task:** T-07 · **Rubric criterion:** 4 · **Status:** initial requirements for delivery 1
>
> Organized by the five **usability quality components** defined by Nielsen — learnability, efficiency, memorability, errors, satisfaction `[R1]` — and consistent with the ISO 9241-11 view of usability as effectiveness, efficiency and satisfaction for specified users, goals and context of use `[R2]`. Accessibility and quality attributes that affect the user experience follow; sections 2–6 also state which usability component each requirement supports, and security, privacy and compatibility are kept as quality attributes because they shape what the user can do. `[Rn]` = source in [`references.md`](../references.md).
>
> Requirements marked **(H)** rest only on hypotheses (no CR or PRJ in their origin) and may change after validation.
>
> ⚠️ **All numeric targets are tentative design goals proposed by the author**, not measured values or findings. They will be calibrated with the evidence from the [validation plan](../02-research/validation-plan.md). Values taken from external guidelines cite their verified source `[Rn]`.

## 1. Usability attributes

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-01 | Learnability | A first-time seller (P-01) completes a cash sale without assistance after a demonstration of at most 2 minutes. | ≥ 80% of test participants complete the task on the first attempt. | Usability test (V-07) | PRJ-03, H-01, H-12 |
| NFR-02 | Learnability | The interface uses everyday language, with no technical terms (e.g. "sync", "server", "database") and icons always paired with text labels. | 0 technical terms on the sales screens. | Heuristic inspection | PRJ-03, H-01 |
| NFR-03 | Efficiency | A one-item cash sale can be completed with a small number of taps from the sales screen. | ≤ 5 taps, excluding typing the amount received. | Design inspection (task walkthrough) | CR-10, CR-11, H-05 |
| NFR-04 | Efficiency | A typical sale takes less time than the current process. **(H)** | Median time per sale ≥ 20% lower than the current median measured in V-01 (tentative). | Observation (V-01) vs. usability test (V-07) | H-04, H-05 |
| NFR-05 | Memorability | A seller who has not used the app for two weeks completes a sale without help. **(H)** | ≥ 80% of returning participants succeed. | Follow-up usability test (V-07) | H-12 |
| NFR-06 | Errors — prevention | Sellers enter Interuady data correctly on the first attempt; the form prevents incomplete notes (FR-20) and makes the missing field obvious. | ≥ 80% of participants complete an Interuady sale without a validation error; when an error occurs, 100% identify the missing field without help. | Usability test (V-07), task based on S-02 | CR-13, H-01, H-08 |
| NFR-07 | Errors — recovery | Error messages explain what happened and what to do next, in plain language. | 100% of error messages include a suggested action. | Heuristic inspection | PRJ-03, H-01 |
| NFR-25 | Learnability | No mandatory tutorial: help appears as contextual hints, once, at the moment the user needs them. | 0 mandatory onboarding screens; each hint shown at most once per user. | Design inspection; usability test (V-07) | PRJ-03, H-01, H-12, DI-26 |
| NFR-26 | Efficiency | CDU staff (P-02) register a new product with photo, barcode and initial stock per warehouse without assistance. | Median ≤ 3 min per product after one practice product (tentative). | Usability test (V-07), task based on S-04 | CR-05…CR-09, H-07 |
| NFR-27 | Efficiency | Central Administration staff (P-03) find the pending Interuady notes of a given unit. | ≥ 80% of participants succeed in ≤ 1 min without assistance (tentative). | Usability test (V-07), task based on S-06 | CR-14, H-11, H-16 |
| NFR-28 | Errors — frequency | Participants make few errors while completing the key sales tasks (cash, card and Interuady sale). | ≤ 1 error per task on average, and 0 errors that the participant cannot recover from without help (tentative). | Error count in the usability test (V-07) | PRJ-03, H-01, H-05 |
| NFR-08 | Satisfaction | Sellers rate the app as easy to use. | SUS score ≥ 68, the average SUS score across published evaluations `[R5]`. | SUS questionnaire after the usability test (V-07) | PRJ-03 |

## 2. Accessibility and ergonomics

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-09 | Errors — prevention; Efficiency | Touch targets are large enough for fast, error-free use. **(H)** | ≥ 48 × 48 dp, the Android recommendation for touch targets `[R4]`. | Design inspection | H-01, H-06 |
| NFR-10 | Accessibility (supports Efficiency and Errors) | Text has enough contrast to be read in varied lighting. **(H)** | ≥ 4.5:1 for normal text and ≥ 3:1 for large text (WCAG 2.2, SC 1.4.3, level AA) `[R3]`. | Contrast checker on Figma designs | H-01 |
| NFR-11 | Efficiency | The main sales actions (add, quantity, pay, confirm) can be reached with one hand. **(H)** | Primary actions placed in the lower half of the screen. | Design inspection | H-06 |
| NFR-12 | Learnability | The user interface is in Spanish, the language of the client and users. | 100% of UI text. | Inspection | PRJ-03 |

## 3. Performance on low-end devices

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-13 | Efficiency (perceived performance) | The app runs on a low-end Android reference phone. | Until V-05 defines the reference device: 2 GB of RAM and Android 10 as a tentative lower bound (author's design goal, not a measured value). | Device test (V-08) | PRJ-01, H-02, Q-12 |
| NFR-14 | Efficiency (perceived performance) | The sales screen opens quickly on the reference device. | ≤ 3 s from tapping the app icon (author's tentative target; no external benchmark verified yet). | Device test (V-08) | PRJ-01, H-02 |
| NFR-15 | Efficiency (perceived performance) | Product photos used for selling are compressed thumbnails. | Tentative: ≤ 100 KB per thumbnail, and the catalog of one warehouse fits in ≤ 50 MB; full-size photos kept only at CDU. | Device test (V-08) | CR-06, CR-10, PRJ-01, DI-14 |
| NFR-16 | Efficiency (perceived performance) | Each satellite device (Sociales, Matemáticas) stores only its own warehouse's catalog; CDU and Central Administration devices may store all three. | 1 warehouse per satellite device. | Inspection | PRJ-01, CR-08, CR-01, CR-02 |

## 4. Reliability and offline operation

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-17 | Errors — recovery (perceived reliability) | No confirmed sale is lost if the connection drops or the app is closed. | 0 lost sales in offline tests. | Offline test with forced disconnection (V-08) | PRJ-02, H-03 |
| NFR-18 | Errors — recovery (perceived reliability) | Queued sales synchronize automatically after connectivity returns. | ≤ 1 min after reconnection. | Offline test (V-08) | PRJ-02 |

## 5. Security and privacy

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-19 | Security (quality attribute) | The session locks after a period of inactivity; unlocking is a single step. | Lock after ≤ 5 min of inactivity (to confirm with the client, Q-11); after unlocking, the app returns to the sales screen. | Functional test | CR-01…CR-04, H-02, H-12, Q-11, DI-27 |
| NFR-20 | Security (quality attribute) | Personal data from Interuady notes stored on a device is encrypted at rest. Devices of charge-only profiles keep only each note's number, unit, amount, date and status; personal details are stored only on devices of profiles with query permission (depends on FR-26). | 100% of locally stored personal data encrypted; 0 personal-detail fields on charge-only devices. | Local storage inspection (V-08) | CR-13, CR-14, PRJ-02, H-02 |
| NFR-21 | Privacy and compliance (quality attribute) | The system never stores card data, to stay outside the scope of PCI DSS `[R16]`. | 0 card data fields in the data model. | Data model review | CR-12, H-10 |
| NFR-22 | Privacy and compliance (quality attribute) | Interuady data handling follows the applicable personal data law for public-sector entities. | Checklist, to be completed before implementation: privacy notice available (FR-39); only the three client fields collected; access limited by profile (FR-26); local data encrypted (NFR-20); synchronized personal details removed from charge-only devices. Legal review of the specific articles of `[R17, R18]` pending. | Checklist review | CR-13, CR-14, Q-04 |

## 6. Compatibility

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-23 | Compatibility (supports Efficiency) | Support external barcode scanners that work as a keyboard (keyboard-wedge / HID mode, USB or Bluetooth) `[R13]`. | Works with at least one available scanner. | Device test (V-08) | CR-16 |
| NFR-24 | Compatibility (supports Efficiency) | Support printing receipts on a Bluetooth thermal printer (support depends on the platform decision, since Web Bluetooth is experimental and not available on iOS `[R14, R15]`). | Works with at least one available printer. | Device test (V-08) | CR-17 |
