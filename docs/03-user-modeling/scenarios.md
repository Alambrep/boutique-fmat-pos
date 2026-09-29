# Scenarios

> **Task:** T-05 · **Rubric criterion:** 2 · **Status:** draft for delivery 1
>
> ⚠️ **Hypothetical scenarios.** They describe how the [proto-personas](proto-personas.md) are *expected* to use the system, based on client requirements (`CR`, `PRJ`) and unvalidated [hypotheses](../02-research/hypotheses.md) (`H`). They are not observations. Each one ends with **design implications** that feed the [requirements](../04-requirements/).

## Summary

| ID | Proto-persona | Scenario | Main origins |
|---|---|---|---|
| S-01 | P-01 | Cash sale during a rush, without internet | CR-10, CR-11, CR-12, CR-15, PRJ-02, H-03, H-05 |
| S-02 | P-01 | Sale paid with Interuady | CR-12, CR-13, CR-14, H-14 |
| S-03 | P-01 | Card sale when the barcode scanner is not available | CR-12, CR-16, H-10 |
| S-04 | P-02 | Registering a new product for the three warehouses | CR-05…CR-09, H-07 |
| S-05 | P-02 | End-of-day stock check after the points synchronize | CR-08, CR-15, PRJ-02, H-04 |
| S-06 | P-03 | Reviewing pending Interuady notes and charging a sale | CR-02, CR-14, H-11, H-13 |

---

## S-01 — Cash sale during a rush, without internet

**Proto-persona:** P-01 (Rosa) · **Origins:** CR-10, CR-11, CR-12, CR-15, PRJ-01, PRJ-02, H-01, H-02, H-03, H-05, H-06, H-09

**Context.** First week of the semester. There is a queue at the Sociales point `[H-05]`, and the phone has no signal `[H-03]`. Rosa is holding a T-shirt in one hand `[H-06]`.

**Narrative.** A student wants two T-shirts of the same design. Rosa opens the app, which starts directly on the sales screen. She recognizes the T-shirt by its photo and taps it `[CR-10]`. She taps "+" once to set the quantity to 2 `[CR-11]` and sees the total. She chooses "Cash" `[CR-12]`, enters the amount received and sees the change. She confirms. The app shows "Sale saved on this phone — it will be sent when there is internet" `[PRJ-02]`. The stock at Sociales drops by two on the phone `[CR-15]`. The next customer is already waiting.

**Design implications**
- DI-01: The sales screen is the home screen for charge-only profiles; the catalog is shown as photos.
- DI-02: Quantity can be changed with large +/– controls, usable with one hand.
- DI-03: Cash payment calculates change.
- DI-04: Sales are saved locally and queued for synchronization; offline status is shown in plain language and never blocks a sale.
- DI-05: Local stock is updated immediately after each sale.

## S-02 — Sale paid with Interuady

**Proto-persona:** P-01 (Rosa) · **Origins:** CR-12, CR-13, CR-14, H-01, H-08, H-14

**Context.** A staff member from another UADY unit comes to buy five polos for an event, paid through Interuady `[H-14]`.

**Narrative.** Rosa selects the polo by its photo and sets the quantity to 5. She chooses "Interuady" `[CR-12]`. Three fields appear: unit, C.P. responsible for the payment, and requester `[CR-13]`. Rosa copies the data from the staff member's request. The "Confirm" button stays disabled until the three fields are filled, and the empty fields are highlighted `[CR-13]`. After confirming, the app says the note was added to accounts receivable `[CR-14]`.

**Design implications**
- DI-06: Interuady fields appear only when that payment method is selected, and all three are mandatory.
- DI-07: Missing fields are highlighted with a clear message; the sale cannot be completed without them.
- DI-08: The unit field offers a list of UADY units to reduce typing (depends on the client providing the list).
- DI-09: Confirmed Interuady sales create an accounts receivable note.

## S-03 — Card sale when the barcode scanner is not available

**Proto-persona:** P-01 (Rosa) · **Origins:** CR-10, CR-12, CR-16, H-01, H-02, H-06, H-10

**Context.** The Bluetooth scanner at the Matemáticas point has no battery `[CR-16]`. A customer wants to pay by card.

**Narrative.** Rosa cannot scan the code, so she types the first letters of the product name in the search box and chooses it by its photo `[CR-10]`. She selects "Card" `[CR-12]` and charges the amount on the separate bank terminal `[H-10]`. Back in the app, she confirms that the card payment was approved. The sale is recorded as paid by card; no card data is entered.

**Design implications**
- DI-10: Products can be found by scanning, by browsing photos or by searching by name; the scanner is optional.
- DI-11: Card payment only records the payment method (no card data), pending confirmation of Q-06.

## S-04 — Registering a new product for the three warehouses

**Proto-persona:** P-02 (Daniel) · **Origins:** CR-01, CR-05, CR-06, CR-07, CR-08, CR-09, H-07, Q-07, Q-08

**Context.** A new batch of caps arrives at CDU from the supplier.

**Narrative.** Daniel opens "New product" `[CR-01]`. He enters name, type, color, size, net cost, sale price and supplier `[CR-05, CR-08]`, then takes a photo with the phone `[CR-06]`. The system generates the product code and barcode `[CR-07]`. He enters the initial stock for CDU, Sociales and Matemáticas `[CR-08, CR-09]`, then prints the barcode labels. When the satellite phones connect, they receive the new product.

**Design implications**
- DI-12: Product registration form with all CR-08 fields, photo capture and automatic code and barcode generation.
- DI-13: Stock is assigned per warehouse during registration (how later transfers work depends on Q-07).
- DI-14: Photos are compressed to thumbnails before being sent to the satellite points.
- DI-15: Barcode labels can be printed or exported.

## S-05 — End-of-day stock check after the points synchronize

**Proto-persona:** P-02 (Daniel) · **Origins:** CR-08, CR-15, PRJ-02, H-03, H-04

**Context.** At the end of the day, Daniel wants to know how much stock each warehouse has left.

**Narrative.** Daniel opens the inventory view and filters by warehouse `[CR-08]`. The Matemáticas point shows "last synchronized 2 hours ago" `[PRJ-02, H-03]`. When its phone connects, its sales are applied and stock is updated `[CR-15]`. Daniel notices a product with negative stock at Sociales: two sales happened offline after the stock ran out. The system flags it for review instead of hiding it.

**Design implications**
- DI-16: Inventory view per warehouse with all CR-08 fields and filters.
- DI-17: Each warehouse shows its last synchronization time.
- DI-18: Stock conflicts (e.g. negative stock after offline sales) are flagged for review, not silently corrected.

## S-06 — Reviewing pending Interuady notes and charging a sale

**Proto-persona:** P-03 (Martha) · **Origins:** CR-02, CR-10…CR-14, H-08, H-11, H-13, Q-02, Q-09

**Context.** Martha needs to know which units owe money to the boutique `[H-13]`.

**Narrative.** Martha opens "Accounts receivable" `[CR-14]` and filters by status "Pending". She sees each note with its number, unit, amount and date. She opens one to check the requester. Later, a colleague asks her for a mug, and she charges it with the same sales flow as the satellite points `[CR-02]`. Which warehouse's stock the sale is deducted from is still pending (Q-02).

**Design implications**
- DI-19: Accounts receivable view with filters by unit, status and date, available to all profiles `[CR-14]`; the detail about people is limited by profile (proposal, see [project definition §4.2](../01-definition/project-definition.md)).
- DI-20: Read-only inventory query for Central Administration.
- DI-21: The sales flow is the same for every profile that can charge.
