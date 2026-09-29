# Non-functional requirements

> **Task:** T-07 · **Rubric criterion:** 4 · **Status:** initial requirements for delivery 1
>
> Organized by the five **usability quality components** defined by Nielsen — learnability, efficiency, memorability, errors, satisfaction `[R1]` — and consistent with the ISO 9241-11 view of usability as effectiveness, efficiency and satisfaction for specified users, goals and context of use `[R2]`. Accessibility and quality attributes that affect the user experience follow. `[Rn]` = source in [`references.md`](../references.md).
>
> ⚠️ **All numeric targets are tentative design goals proposed by the author**, not measured values or findings. They will be calibrated with the evidence from the [validation plan](../02-research/validation-plan.md). Values taken from external guidelines cite their verified source `[Rn]`; items still pending verification are marked 🔎.

## 1. Usability attributes

| ID | Attribute | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|---|
| NFR-01 | Learnability | A first-time seller (P-01) completes a cash sale without assistance after a short demonstration. | ≥ 80% of test participants complete the task on the first attempt. | Usability test (V-07) | PRJ-03, H-01, H-12 |
| NFR-02 | Learnability | The interface uses everyday language, with no technical terms (e.g. "sync", "server", "database") and icons always paired with text labels. | 0 technical terms on the sales screens. | Heuristic inspection | PRJ-03, H-01 |
| NFR-03 | Efficiency | A one-item cash sale needs few interactions from the sales screen. | ≤ 5 taps, excluding typing the amount received. | Design inspection (task walkthrough) | CR-10, CR-11, H-05 |
| NFR-04 | Efficiency | A typical sale takes less time than the current process. | Target set after measuring the current time (V-01). | Observation (V-01) vs. usability test (V-07) | H-04, H-05 |
| NFR-05 | Memorability | A seller who has not used the app for two weeks completes a sale without help. | ≥ 80% of returning participants succeed. | Follow-up usability test (V-07) | H-12 |
| NFR-06 | Errors — prevention | An Interuady sale cannot be confirmed with missing mandatory fields. | 0 incomplete Interuady notes. | Functional test | CR-13, H-08 |
| NFR-07 | Errors — recovery | Error messages explain what happened and what to do, in plain language; every sale can be reviewed before confirming. | 100% of error messages include a suggested action. | Heuristic inspection | PRJ-03, H-01 |
| NFR-08 | Satisfaction | Sellers rate the app as easy to use. | SUS score ≥ 68, the average SUS score across published evaluations `[R5]`. | SUS questionnaire after the usability test (V-07) | PRJ-03 |

## 2. Accessibility and ergonomics

| ID | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|
| NFR-09 | Touch targets are large enough for fast, error-free use. | ≥ 48 × 48 dp, the Android recommendation for touch targets `[R4]`. | Design inspection | H-01, H-06 |
| NFR-10 | Text has enough contrast to be read in varied lighting. | ≥ 4.5:1 for normal text and ≥ 3:1 for large text (WCAG 2.2, SC 1.4.3, level AA) `[R3]`. | Contrast checker on Figma designs | H-01 |
| NFR-11 | The main sales actions (add, quantity, pay, confirm) can be reached with one hand. | Primary actions placed in the lower half of the screen. | Design inspection | H-06 |
| NFR-12 | The user interface is in Spanish. | 100% of UI text. | Inspection | CR-01…CR-04 (Spanish-speaking client and users) |

## 3. Performance on low-end devices

| ID | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|
| NFR-13 | The app runs on a low-end Android reference phone. | Reference device defined after V-05 (model, RAM, storage, Android version). | Device test (V-08) | PRJ-01, H-02, Q-12 |
| NFR-14 | The sales screen opens quickly on the reference device. | ≤ 3 s from tapping the app icon. | Device test (V-08) | PRJ-01, H-02 |
| NFR-15 | Product photos used for selling are compressed thumbnails. | Size limit defined after V-08; full-size photos kept only at CDU. | Device test (V-08) | CR-06, CR-10, PRJ-01 |
| NFR-16 | Each device stores only its own warehouse's catalog. | 1 warehouse per satellite device. | Inspection | PRJ-01, CR-08 |

## 4. Reliability and offline operation

| ID | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|
| NFR-17 | No confirmed sale is lost if the connection drops or the app is closed. | 0 lost sales in offline tests. | Offline test with forced disconnection (V-08) | PRJ-02, H-03 |
| NFR-18 | Queued sales synchronize automatically after connectivity returns. | ≤ 1 min after reconnection. | Offline test (V-08) | PRJ-02 |

## 5. Security and privacy

| ID | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|
| NFR-19 | Each user signs in with a personal account; the session locks after a period of inactivity. | Lock after ≤ 5 min of inactivity (to confirm with the client). | Functional test | CR-01…CR-04, H-02 |
| NFR-20 | Personal data stored on the device (Interuady notes) is encrypted and deleted from the device once synchronized. | 100% of synchronized notes removed from local storage. | Inspection and test | CR-13, PRJ-02, H-02 |
| NFR-21 | The system never stores card data, to stay outside the scope of PCI DSS `[R16]`. | 0 card data fields in the data model. | Data model review | CR-12, H-10 |
| NFR-22 | Interuady data handling follows the applicable personal data law for public-sector entities, including a privacy notice. | Compliance checklist based on the current federal and state laws for obligated subjects `[R17, R18]`. | Legal checklist | CR-13, CR-14 |

## 6. Compatibility

| ID | Requirement | Tentative target | How it is measured | Origin |
|---|---|---|---|---|
| NFR-23 | Support external barcode scanners that work as a keyboard (keyboard-wedge / HID mode, USB or Bluetooth) `[R13]`. | Works with at least one available scanner. | Device test (V-08) | CR-16 |
| NFR-24 | Support printing receipts on a Bluetooth thermal printer (support depends on the platform decision, since Web Bluetooth is experimental and not available on iOS `[R14, R15]`). | Works with at least one available printer. | Device test (V-08) | CR-17 |
