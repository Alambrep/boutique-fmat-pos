# Proto-personas

> **Task:** T-04 · **Rubric criterion:** 3 · **Status:** draft for delivery 1
>
> ⚠️ **These are proto-personas, not research-based personas.** They are built from the client's requirements (`CR`, `PRJ`) and the author's unvalidated [hypotheses](../02-research/hypotheses.md) (`H`). Names, ages and personal details are **fictional** and exist only to make the profiles easier to reason about. Every attribute is traced to its origin. They will be revised or replaced after the validation in delivery 2.

## 1. User classes

Classification follows Cooper: a **primary** persona needs an interface of its own, while a **secondary** persona can mostly be served by interfaces designed for others `[R10]`. Proto-personas are assumption-based and must be validated with research `[R6, R7]`. Sources: [`references.md`](../references.md).

| Class | Proto-persona | Role in the system | Why this class |
|---|---|---|---|
| **Primary** | **P-01 — Satellite seller** | Uses the sales screen every day; charge-only permissions | Most frequent user, lowest digital skills, strictest constraints (device, connectivity). If the design works for P-01, it works for everyone who sells. `[CR-03, CR-04, PRJ-01…PRJ-03]` |
| **Primary** | **P-02 — CDU inventory manager** | Registers products, manages stock for all warehouses, sells | Only user who creates and edits the catalog; the whole system depends on their data. Needs a different interface from P-01. `[CR-01, CR-05…CR-09]` |
| **Secondary** | **P-03 — Central Administration officer** | Queries stock and accounts receivable; charges occasionally | Uses a subset of the functions; their needs are mostly covered by the P-01 and P-02 designs plus the accounts receivable view. `[CR-02, CR-14]` |

**Indirect stakeholders** (affected by the system but not modeled as personas in delivery 1):

- **Walk-in buyer:** receives the receipt; benefits from a faster sale. `[CR-17, H-09]`
- **Interuady requester and the C.P. responsible for the payment:** their personal data is recorded. `[CR-13, H-14]`
- **Accounting:** defines the receipt and invoicing rules. `[CR-18, Q-05]`

### User profiles

Profile of each user class, before turning them into proto-personas. Everything not marked `CR` is an unvalidated hypothesis.

| Attribute | Satellite seller → P-01 | CDU staff → P-02 | Central Administration → P-03 |
|---|---|---|---|
| Client profile and permissions | Social Sciences / Exact Sciences Campus: charge only `[CR-03, CR-04]` | CDU: modify, query, charge `[CR-01]` | Query and charge `[CR-02]` |
| Main tasks | Sell, choose payment method, record Interuady data `[CR-10…CR-13]` | Register products, photos, barcodes, stock per warehouse `[CR-05…CR-09]` | Query stock and accounts receivable; occasional sales `[CR-02, CR-14]` |
| Frequency of use | Daily, in bursts `[H-05]` | Daily, longer sessions `[H-07]` | Occasional `[H-11]` |
| Digital skills | Basic or low `[H-01]` | Medium `[H-07]` | Not assumed yet |
| Device | Low/mid-range Android, possibly personal `[H-02]` | Phone, possibly a computer `[H-02]` | Not assumed yet |
| Connectivity | Intermittent (challenged at FMAT) `[H-03]` | Not assumed yet | Not assumed yet |
| Work environment | Queues, interruptions, one free hand `[H-05, H-06]` | Warehouse, data entry `[H-07]` | Office `[H-11]` |
| Training | Informal, rotating staff `[H-12]` | Not assumed yet | Not assumed yet |

## 2. P-01 — Satellite seller (primary)

**Fictional name:** Rosa · **Point of sale:** Sociales or Matemáticas warehouse · **Profile:** Social Sciences Campus or Exact Sciences Campus `[CR-03, CR-04]`

| Attribute | Description | Origin |
|---|---|---|
| Role | Charges sales at a satellite point. Cannot modify products or prices. | CR-03, CR-04 |
| Digital skills | Basic: uses the phone for calls and messaging, but is uneasy with unfamiliar apps and technical terms. | H-01, PRJ-03 |
| Continuity | May cover the point in shifts with other people; learned the job by watching someone else. | H-12 |
| Device | Low- or mid-range Android phone, possibly her own; limited storage. | H-02, PRJ-01 |
| Connectivity | Unreliable signal or Wi-Fi at the point of sale (challenged for the FMAT point; see the hypotheses evidence log). | H-03, PRJ-02 |
| Work conditions | Busy periods with a queue; often holding a product or cash while charging. | H-05, H-06 |
| Typical sale | One to three items to students or staff, paid in cash or card; occasionally an Interuady purchase. | H-09, H-14, CR-12 |

**Goals**
- Complete each sale quickly, without mistakes, and get to the next customer. `[H-05]`
- Know that each sale was "saved", even without internet. `[PRJ-02, H-03]`
- Record Interuady purchases correctly, without having to remember which fields are needed. `[CR-13]`

**Hypothesized frustrations**
- Screens full of fields and words she does not understand. `[H-01, CR-08]`
- Apps that stop working or lose data when the signal drops. `[H-03]`
- Not knowing whether a product has stock at her point. `[CR-15, H-04]`

**What the design must give her**
- Choose the product by its **photo**, adjust the quantity and pick the payment method. Nothing more. `[CR-10, CR-11, CR-12]`
- Large buttons, operable with one hand, everyday language. `[H-06, PRJ-03]`
- Clear feedback that the sale was saved, online or offline. `[PRJ-02]`
- The three Interuady fields appear only when needed, and a sale cannot be completed without them. `[CR-13]`

## 3. P-02 — CDU inventory manager (primary)

**Fictional name:** Daniel · **Location:** CDU (main warehouse) · **Profile:** CDU `[CR-01, CR-09]`

| Attribute | Description | Origin |
|---|---|---|
| Role | Registers products for every store, manages stock, queries and sells. | CR-01, CR-09 |
| Digital skills | Medium: comfortable with spreadsheets and forms. | H-07 |
| Main tasks | Enter product data, take photos, generate and print barcodes. | CR-05, CR-06, CR-07 |
| Responsibility | Keeps the inventory table of the three warehouses. | CR-08 |
| Current process | Uses notebooks or spreadsheets; recorded stock does not always match physical stock. | H-04 |
| Device | Phone at the warehouse (and possibly a computer, not confirmed). | H-02, PRJ-01 |
| Follow-up | May be responsible for following up Interuady accounts receivable. | H-13, Q-09 |

**Goals**
- Register a new product once and have it available at the right warehouses. `[CR-09]`
- See real stock per warehouse without calling each point. `[CR-08, CR-15]`
- Print barcode labels for new stock. `[CR-07]`

**Hypothesized frustrations**
- Typing the same data many times (each size or color as a different product). `[CR-08, Q-08]`
- Stock that does not match because sales at the points were not recorded. `[H-04]`

**What the design must give him**
- A registration form with all the required fields `[CR-08]`, photo capture `[CR-06]` and automatic barcode generation `[CR-07]`.
- A per-warehouse inventory view that reflects synchronized sales and shows when data is pending sync. `[CR-08, CR-15, PRJ-02]`

## 4. P-03 — Central Administration officer (secondary)

**Fictional name:** Martha · **Location:** Central Administration · **Profile:** Central Administration `[CR-02]`

| Attribute | Description | Origin |
|---|---|---|
| Role | Queries stock and accounts receivable; charges occasionally. | CR-02, H-11 |
| Main interest | Knowing which Interuady notes are pending and from which unit. | CR-14, H-08 |
| Stock source | Unknown which warehouse she sells from. | Q-02 |
| Follow-up | May be responsible for collecting Interuady notes. | H-13, Q-09 |

**Goals**
- See pending Interuady notes by unit, with amount and date. `[CR-14]`
- Check stock before promising products to another unit. `[CR-02, CR-08]`

**What the design must give her**
- An accounts receivable view with filters (unit, status, date). `[CR-14]`
- A read-only inventory query. `[CR-02]`
- The same simple sales flow as P-01 when she needs to charge. `[CR-02, CR-10…CR-13]`

## 5. Coverage check

| Client profile | Proto-persona |
|---|---|
| CDU `[CR-01]` | P-02 |
| Central Administration `[CR-02]` | P-03 |
| Social Sciences Campus `[CR-03]` | P-01 |
| Exact Sciences Campus `[CR-04]` | P-01 |

All four client profiles are covered. P-01 represents both satellite profiles because they have identical permissions `[CR-03, CR-04]`; this will be revisited if validation shows different contexts at each point.
