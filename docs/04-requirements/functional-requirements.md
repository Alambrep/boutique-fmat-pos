# Functional requirements

> **Task:** T-06 · **Rubric criterion:** 4 · **Status:** initial requirements for delivery 1
>
> Each requirement cites its origin: client requirement (`CR`), project requirement (`PRJ`), hypothesis (`H`), open question (`Q`) and the design implication (`DI`) from the [scenarios](../03-user-modeling/scenarios.md) where it appeared. Requirements marked **(H)** depend on an unvalidated hypothesis for their content and may change after validation.
>
> Numbering: FR-30…FR-39 were added on 2026-09-29 after an internal review; IDs are not renumbered so existing references stay valid.
>
> **Priority (MoSCoW `[R11]`, see [`references.md`](../references.md)):** **Must** = stated by the client or project brief, or required to meet a Must requirement or a legal obligation (the origin column says which) · **Should** = strongly supported by scenarios · **Could** = useful, low cost · **Deferred** = *Won't have this time*: depends on an open question.

## 1. Access and profiles

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-01 | Provide four profiles with these permissions: **CDU** — modify, query and charge; **Central Administration** — query and charge; **Social Sciences Campus** and **Exact Sciences Campus** — charge only. | Must | CR-01, CR-02, CR-03, CR-04, H-17 | All |
| FR-02 | Require the user to sign in with an account linked to one of the four client profiles before using the system. | Must | CR-01…CR-04, Q-11 (personal or shared accounts; the client's document speaks of "4 sessions or users") | S-01 |
| FR-35 | Let a user lock the app and another user sign in on the same device; sales not yet synchronized keep the identity of the user who made them. | Should | CR-01…CR-04, PRJ-02, H-12, Q-11, DI-25 | S-08 |
| FR-30 | Keep the session usable without connectivity after the first successful sign-in on the device. | Must | PRJ-02 | S-01 |
| FR-03 | Open directly on the sales screen for charge-only profiles. **(H)** | Should | H-01, DI-01 | S-01 |

## 2. Catalog and inventory

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-04 | Let CDU register a product by manually entering: product name, type, color, size, net cost, sale price and supplier. | Must | CR-05, CR-08, DI-12 | S-04 |
| FR-05 | Let CDU attach a product photo from the camera or the gallery. | Must | CR-06, DI-12 | S-04 |
| FR-06 | Generate a unique product code and its barcode for every product. The code format depends on Q-08. | Must | CR-07, Q-08, DI-12 | S-04 |
| FR-07 | Let CDU print or export barcode labels. | Should | CR-07, DI-15 | S-04 |
| FR-08 | Let CDU assign initial stock per warehouse (CDU, Sociales, Matemáticas) when registering a product. | Must | CR-08, CR-09, DI-13 | S-04 |
| FR-09 | Allow only the CDU profile to create or edit products, prices and stock. | Must | CR-01, CR-09, H-17 | S-04 |
| FR-10 | Show, to profiles with query permission, an inventory table per warehouse with the fields: Code, Product, Type, Color, Size, Stock, Net cost, Sale price, Supplier, Warehouse; with filters by warehouse and product. | Must | CR-01, CR-02, CR-08, DI-16, DI-20 | S-05, S-06 |
| FR-11 | Show the last synchronization time of each warehouse in the inventory view. | Should | PRJ-02, H-03, DI-17 | S-05 |
| FR-12 | Flag stock conflicts (negative stock, or a sale confirmed after the out-of-stock warning of FR-32) for CDU review instead of correcting them silently. | Should | PRJ-02, CR-15, DI-18 | S-05 |
| FR-36 | Let CDU register a product with several colors or sizes by entering the shared data once; the system creates one record per variant, each with its own code, photo and stock per warehouse. The code format depends on Q-08. | Should | CR-05…CR-08, Q-08, DI-30 | S-04 |
| FR-37 | Make the query views (inventory and accounts receivable) usable from a desktop browser for profiles with query permission. **(H)** — favors an installable web app over a native-only app (see the [project definition](../01-definition/project-definition.md), challenge 2). | Could | CR-01, CR-02, CR-14, H-16, DI-31 | S-06 |

## 3. Sales

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-13 | Show, on the sales screen, the products of the user's warehouse with image, code, product name and sale price, preloaded. The same sales screen serves every profile that can charge. For Central Administration, the source warehouse depends on Q-02 (FR-D6). | Must | CR-10, H-15, DI-01, DI-21 | S-01 |
| FR-14 | Let the user find a product both by browsing photos and by searching by name. | Should | CR-10, H-01, DI-10 | S-01, S-03 |
| FR-15 | Let the user add a product by scanning its barcode with an external keyboard-wedge scanner; when no scanner is connected, offer the phone camera as an alternative. | Should | CR-16, DI-10 | S-03 |
| FR-16 | Let the user change the quantity of each product before confirming the sale. | Must | CR-11, DI-02 | S-01, S-02 |
| FR-17 | Offer three payment methods: cash, card and Interuady. | Must | CR-12 | S-01, S-02, S-03 |
| FR-18 | Calculate change for cash payments from the amount received. **(H)** | Could | H-05, DI-03 | S-01 |
| FR-19 | Record card payments by payment method only, without capturing any card data. **(H)** | Must | CR-12, H-10, Q-06, DI-11; legal obligation: PCI DSS scope `[R16]` | S-03 |
| FR-20 | When Interuady is selected, display three mandatory fields — department or unit (*departamento o dependencia*), C.P. responsible for the payment, requester or authorizer — and prevent confirming the sale until all three are filled. | Must | CR-13, Q-04, DI-06, DI-07 | S-02 |
| FR-39 | When Interuady is selected, give access to the privacy notice that applies to the personal data being captured, so the seller can show it to the person providing the data; the notice text is provided by UADY. | Should | CR-13, Q-04; legal obligation `[R17, R18]` | S-02 |
| FR-21 | Offer a selectable list of UADY units for the unit field. **(H)** | Could | H-08, DI-08 | S-02 |
| FR-22 | Deduct the sold quantities automatically from the stock of the warehouse where the sale took place, only when the sale is confirmed. | Must | CR-15, H-15, DI-05, DI-24 | S-01, S-07 |
| FR-38 | Record, for every confirmed sale, the date and time, the point of sale, the payment method and the signed-in account that made it; charge-only profiles cannot edit this record. **(H)** | Should | CR-01…CR-04, CR-15, H-12, Q-11 | S-01, S-02, S-03 |
| FR-23 | Issue a receipt for every confirmed sale: printed when a thermal printer is connected, and shown on screen otherwise. Printing never blocks or undoes a saved sale. The receipt content (VAT breakdown) depends on Q-05. | Should | CR-17, CR-18, Q-05, DI-28 | S-01 |
| FR-31 | Show on each product card of the sales screen whether the product is available at the user's warehouse (in stock / few left, at or below a threshold set by CDU / out of stock), without showing the inventory table. **Proposal pending client confirmation (Q-14)**, since charge-only profiles have no query permission. **(H)** | Should | CR-03, CR-04, CR-15, H-04, H-15, DI-32, Q-14 | S-01 |
| FR-32 | When the recorded stock of a product at the user's warehouse is 0, allow the sale only after the user confirms a warning, and flag it for CDU review (FR-12). **(H)** | Should | CR-15, PRJ-02, H-04, DI-18, DI-29 | S-05 |
| FR-33 | Before a sale is confirmed, show a summary (products, quantities, total, payment method) where the user can remove a product, change its quantity or change the payment method. | Must | CR-11, CR-12, DI-22, DI-23 | S-03, S-07 |

## 4. Accounts receivable

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-24 | Create an accounts receivable note for every sale paid with Interuady, containing: note number, date, point of sale, department or unit, amount, products and quantities, and the three Interuady fields. | Must | CR-13, CR-14, DI-09 | S-02 |
| FR-25 | Show the accounts receivable section to **all** profiles, with filters by unit and date. A filter by status (pending / paid) is added when settlement is defined (FR-D5, Q-09). | Must | CR-14, DI-19 | S-06 |
| FR-26 | Show the personal details of each note (C.P. responsible, requester) only to profiles with query permission (CDU, Central Administration). **Proposal pending client approval.** | Should | CR-13, CR-14, CR-01, CR-02, Q-04 | S-06 |

## 5. Offline operation and synchronization

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-27 | Allow every sales function (FR-13…FR-24, FR-31…FR-33) to work without connectivity, storing sales locally in a queue. | Must | PRJ-02, DI-04 | S-01 |
| FR-28 | Synchronize automatically when connectivity returns: send queued sales and receive catalog, price and stock updates published by CDU. | Must | PRJ-02, CR-09, CR-15, Q-15 | S-01, S-04, S-05 |
| FR-29 | Show the synchronization status in plain language (e.g. "Saved on this phone — it will be sent when there is internet"), without blocking any sale. | Must | PRJ-02, PRJ-03, H-01, DI-04 | S-01 |
| FR-34 | Allow CDU to register and edit products without connectivity; changes are published to the other warehouses at the next synchronization. | Should | PRJ-02, CR-01, CR-09 | S-04 |

## 6. Deferred (depend on client answers)

| ID | Candidate requirement | Blocked by |
|---|---|---|
| FR-D1 | Invoicing and VAT breakdown on receipts | CR-18, Q-05 |
| FR-D2 | Stock transfers between warehouses | Q-07 |
| FR-D3 | Sale cancellations, returns and size exchanges (would use the sale record of FR-38) | Q-10 |
| FR-D4 | Integration with a bank card terminal | Q-06 |
| FR-D5 | Settlement of Interuady notes (mark as paid) | Q-09 |
| FR-D6 | Which warehouse Central Administration sales are deducted from | Q-02 |
