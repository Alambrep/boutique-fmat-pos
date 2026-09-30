# Scenarios

> **Task:** T-05 · **Rubric criterion:** 3 · **Status:** final — delivery 1
>
> ⚠️ **Hypothetical scenarios.** They describe how the [proto-personas](proto-personas.md) are *expected* to use the system, based on client requirements (`CR`, `PRJ`) and unvalidated [hypotheses](../02-research/hypotheses.md) (`H`). They are not observations. Each one ends with **design implications** that feed the [requirements](../04-requirements/). Scenarios do not cite requirements, so traceability runs one way: scenario → design implication → requirement.
>
> DI numbers are stable identifiers, not an order; some were added to earlier scenarios after later ones were written.

## Summary

| ID | Proto-persona | Scenario | Main origins |
|---|---|---|---|
| S-01 | P-01 | Cash sale during a rush, without internet | CR-10, CR-11, CR-12, CR-15, PRJ-02, H-03, H-05 |
| S-02 | P-01 | Sale paid with Interuady | CR-12, CR-13, CR-14, H-14 |
| S-03 | P-01 | Card sale when the barcode scanner is not available | CR-12, CR-16, H-10 |
| S-04 | P-02 | Registering a new product for the three warehouses | CR-05…CR-09, H-07 |
| S-05 | P-02 | End-of-day stock check after the points synchronize | CR-08, CR-15, PRJ-02, H-04 |
| S-06 | P-03 | Reviewing pending Interuady notes and charging a sale | CR-02, CR-14, H-11, H-13 |
| S-07 | P-01 | Correcting a mistake before confirming a sale | CR-10, CR-11, CR-15, H-05 |
| S-08 | P-01 | Shift change: a new seller starts using the app for the first time | CR-03, CR-04, PRJ-03, H-01, H-12, Q-11 |

---

## S-01 — Cash sale during a rush, without internet

**Proto-persona:** P-01 (Luis) · **Origins:** CR-03, CR-04, CR-10, CR-11, CR-12, CR-15, CR-17, PRJ-01, PRJ-02, H-01, H-02, H-03, H-05, H-06, H-09, Q-05, Q-14

**Context.** First week of the semester. There is a queue at the Sociales point `[H-05]`, and the phone has no signal `[H-03]`. Luis is holding a T-shirt in one hand `[H-06]`.

**Narrative.** A student wants two T-shirts of the same design. Luis opens the app, which starts directly on the sales screen. He recognizes the T-shirt by its photo and taps it `[CR-10]`. If charge-only profiles are allowed to see availability (Q-14), a label shows it is in stock at Sociales. He taps "+" once to set the quantity to 2 `[CR-11]` and sees the total. He chooses "Cash" `[CR-12]`, enters the amount received and sees the change. He confirms. The app shows "Sale saved on this phone — it will be sent when there is internet" `[PRJ-02]`. The stock at Sociales drops by two on the phone `[CR-15]`. If the point has a thermal printer, a receipt prints automatically; if not, or if the printer fails, the sale is already saved and Luis can move on `[CR-17]`. The next customer is already waiting.

**Design implications**
- DI-01: The sales screen is the home screen for charge-only profiles; the catalog is shown as photos.
- DI-02: Quantity can be changed with large +/– controls, usable with one hand.
- DI-03: Cash payment calculates change.
- DI-04: Sales are saved locally and queued for synchronization; offline status is shown in plain language and never blocks a sale.
- DI-05: Local stock is updated immediately after each sale.
- DI-32: The sales screen shows whether each product is available at the user's point (depends on Q-14).
- DI-28: Printing a receipt is optional and never blocks or undoes a saved sale; receipt content depends on Q-05.

## S-02 — Sale paid with Interuady

**Proto-persona:** P-01 (Luis) · **Origins:** CR-03, CR-04, CR-12, CR-13, CR-14, H-01, H-08, H-14, Q-04

**Context.** A staff member from another UADY unit comes to buy five polos for an event, paid through Interuady `[H-14]`.

**Narrative.** Luis selects the polo by its photo and sets the quantity to 5. He chooses "Interuady" `[CR-12]`. Three fields appear: department or unit, C.P. responsible for the payment, and requester or authorizer `[CR-13]`. Luis copies the data from the staff member's request. The "Confirm" button stays disabled until the three fields are filled, and the empty fields are highlighted `[CR-13]`. After confirming, the app says the note was added to accounts receivable `[CR-14]`.

**Design implications**
- DI-06: Interuady fields appear only when that payment method is selected, and all three are mandatory.
- DI-07: Missing fields are highlighted with a clear message; the sale cannot be completed without them.
- DI-08: The unit field offers a list of UADY units to reduce typing (depends on the client providing the list).
- DI-09: Confirmed Interuady sales create an accounts receivable note.

## S-03 — Card sale when the barcode scanner is not available

**Proto-persona:** P-01 (Luis) · **Origins:** CR-03, CR-04, CR-10, CR-11, CR-12, CR-16, H-01, H-02, H-06, H-10, Q-06

**Context.** The Bluetooth scanner at the Matemáticas point has no battery `[CR-16]`. A customer wants to pay by card.

**Narrative.** Luis cannot scan the code, so he types the first letters of the product name in the search box and chooses it by its photo `[CR-10]`. He selects "Card" `[CR-12]` and charges the amount on the separate bank terminal `[H-10]`. Back in the app, he confirms that the card payment was approved. The sale is recorded as paid by card; no card data is entered. If the terminal declines the card, he taps "Change payment method" and the customer pays in cash; nothing is recorded until a payment is confirmed.

**Design implications**
- DI-10: Products can be found by scanning, by browsing photos or by searching by name; the scanner is optional.
- DI-11: Card payment only records the payment method (no card data), pending confirmation of Q-06.
- DI-22: The payment method can be changed before confirming; no sale is recorded until a payment is confirmed.

## S-04 — Registering a new product for the three warehouses

**Proto-persona:** P-02 (Daniela) · **Origins:** CR-01, CR-05, CR-06, CR-07, CR-08, CR-09, H-07, Q-07, Q-08

**Context.** A new batch of caps arrives at CDU from the supplier, in two colors (blue and white) and one size.

**Narrative.** Daniela opens "New product" `[CR-01]`. She enters name, type, size, net cost, sale price and supplier once `[CR-05, CR-08]`, then adds the two colors; the system creates one record per color, each with its own code, so she does not retype the shared data (how codes are built depends on Q-08). She takes a photo of each color `[CR-06]`. The system generates each code and barcode `[CR-07]`. She enters the initial stock for CDU, Sociales and Matemáticas `[CR-08, CR-09]`, then prints the barcode labels. When the satellite phones connect, they receive the new product.

**Design implications**
- DI-12: Product registration form with all CR-08 fields, photo capture and automatic code and barcode generation.
- DI-13: Stock is assigned per warehouse during registration (how later transfers work depends on Q-07).
- DI-14: Photos are compressed to thumbnails before being sent to the satellite points.
- DI-15: Barcode labels can be printed or exported.
- DI-30: Products with several colors or sizes are entered once with their shared data; each variant gets its own code, photo and stock.

## S-05 — End-of-day stock check after the points synchronize

**Proto-persona:** P-02 (Daniela) · **Origins:** CR-08, CR-15, PRJ-02, H-03, H-04

**Context.** At the end of the day, Daniela wants to know how much stock each warehouse has left.

**Narrative.** Daniela opens the inventory view and filters by warehouse `[CR-08]`. The Matemáticas point shows "last synchronized 2 hours ago" `[PRJ-02, H-03]`. When its phone connects, its sales are applied and stock is updated `[CR-15]`. Daniela notices a product with negative stock at Sociales: two sales were confirmed offline after the phone warned that the recorded stock was 0; the seller had the item in hand, so the phone's record was behind. The system flags it for review instead of hiding it.

**Design implications**
- DI-16: Inventory view per warehouse with all CR-08 fields and filters.
- DI-17: Each warehouse shows its last synchronization time.
- DI-18: Stock conflicts (e.g. negative stock after offline sales) are flagged for review, not silently corrected.
- DI-29: When recorded stock is 0, the seller is warned but can still confirm the sale; the case is flagged for review.

## S-06 — Reviewing pending Interuady notes and charging a sale

**Proto-persona:** P-03 (Martha) · **Origins:** CR-02, CR-10…CR-14, H-08, H-11, H-13, H-16, Q-02, Q-09

**Context.** Martha needs to know which units owe money to the boutique `[H-13]`.

**Narrative.** Martha works from her office computer `[H-16]`. She opens "Accounts receivable" `[CR-14]` and filters by status "Pending". She sees each note with its number, unit, amount and date. She opens one to check the requester. Later, a colleague asks her for a mug, and she charges it with the same sales flow as the satellite points `[CR-02]`. Which warehouse's stock the sale is deducted from is still pending (Q-02).

**Design implications**
- DI-19: Accounts receivable view with filters by unit, status and date, available to all profiles `[CR-14]`; the detail about people is limited by profile (proposal, see [project definition §4.2](../01-definition/project-definition.md)).
- DI-20: Read-only inventory query for Central Administration.
- DI-21: The sales flow is the same for every profile that can charge.
- DI-31: Query views (inventory, accounts receivable) also work on a desktop browser, since P-03 works mainly at a computer `[H-16]`.

## S-07 — Correcting a mistake before confirming a sale

**Proto-persona:** P-01 (Luis) · **Origins:** CR-03, CR-04, CR-10, CR-11, CR-15, PRJ-03, H-01, H-05, H-06

**Context.** A queue at the Matemáticas point `[H-05]`. In a hurry, Luis taps the medium size of a T-shirt instead of the large one.

**Narrative.** Before charging, the app shows the sale summary: photo, size, quantity and total `[CR-10, CR-11]`. Luis notices the wrong size, removes that line with one tap, confirms "Remove this item?", and adds the right one. The total updates. Stock has not changed, because it is only deducted when the sale is confirmed `[CR-15]`.

**Design implications**
- DI-23: A summary is always shown before confirming; any line can be removed or its quantity changed.
- DI-24: Stock is deducted only when a sale is confirmed.

## S-08 — Shift change: a new seller starts using the app for the first time

**Proto-persona:** P-01 (Luis) · **Origins:** CR-03, CR-04, PRJ-02, PRJ-03, H-01, H-02, H-12, Q-11

**Context.** Luis covers the Sociales point in the afternoon for the first time; the morning seller leaves in five minutes `[H-12]`. Nobody has time to train him.

**Narrative.** The morning seller locks the app with one tap. Luis signs in with his own account on the same phone (whether each seller has an account or the point shares one depends on Q-11). The app opens on the sales screen. He is not given a tutorial to read. The first time he taps a product, a short hint shows where to change the quantity, and it does not appear again. The morning seller's unsynced sales remain queued and are still attributed to her `[PRJ-02]`. When a customer arrives, Luis completes the sale without asking for help `[PRJ-03, H-01]`.

**Design implications**
- DI-25: Switching users on a shared phone takes one action to lock and one to sign in; unsynced sales keep the identity of the seller who made them.
- DI-26: No mandatory tutorial; contextual hints appear once, at the moment they are needed.
- DI-27: The app locks after a period of inactivity and returns to the sales screen after sign-in.
