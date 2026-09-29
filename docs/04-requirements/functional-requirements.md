# Functional requirements

> **Task:** T-06 · **Rubric criterion:** 4 · **Status:** initial requirements for delivery 1
>
> Each requirement cites its origin: client requirement (`CR`), project requirement (`PRJ`), hypothesis (`H`), open question (`Q`) and the design implication (`DI`) from the [scenarios](../03-user-modeling/scenarios.md) where it appeared. Requirements that rest only on hypotheses are marked **(H)** and may change after validation.
>
> **Priority (MoSCoW):** **Must** = stated by the client or project brief · **Should** = strongly supported by scenarios · **Could** = useful, low cost · **Deferred** = depends on an open question.

## 1. Access and profiles

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-01 | Provide four profiles with these permissions: **CDU** — modify, query and charge; **Central Administration** — query and charge; **Social Sciences Campus** and **Exact Sciences Campus** — charge only. | Must | CR-01, CR-02, CR-03, CR-04 | All |
| FR-02 | Require each user to sign in with a personal account and keep the session usable offline after the first sign-in. | Must | CR-01…CR-04, PRJ-02, Q-11 | S-01 |
| FR-03 | Open directly on the sales screen for charge-only profiles. **(H)** | Should | H-01, DI-01 | S-01 |

## 2. Catalog and inventory

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-04 | Let CDU register a product by manually entering: product name, type, color, size, net cost, sale price and supplier. | Must | CR-05, CR-08, DI-12 | S-04 |
| FR-05 | Let CDU attach a product photo from the camera or the gallery. | Must | CR-06, DI-12 | S-04 |
| FR-06 | Generate a unique product code and its barcode for every product. The code format depends on Q-08. | Must | CR-07, Q-08, DI-12 | S-04 |
| FR-07 | Let CDU print or export barcode labels. | Should | CR-07, DI-15 | S-04 |
| FR-08 | Let CDU assign initial stock per warehouse (CDU, Sociales, Matemáticas) when registering a product. | Must | CR-08, CR-09, DI-13 | S-04 |
| FR-09 | Allow only the CDU profile to create or edit products, prices and stock. | Must | CR-01, CR-09 | S-04 |
| FR-10 | Show, to profiles with query permission, an inventory table per warehouse with the fields: Code, Product, Type, Color, Size, Stock, Net cost, Sale price, Supplier, Warehouse; with filters by warehouse and product. | Must | CR-01, CR-02, CR-08, DI-16, DI-20 | S-05, S-06 |
| FR-11 | Show the last synchronization time of each warehouse in the inventory view. | Should | PRJ-02, H-03, DI-17 | S-05 |
| FR-12 | Flag stock conflicts (e.g. negative stock after offline sales) for CDU review instead of correcting them silently. | Should | PRJ-02, CR-15, DI-18 | S-05 |

## 3. Sales

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-13 | Show, on the sales screen, the products of the user's warehouse with image, code, product name and sale price, preloaded. | Must | CR-10, DI-01 | S-01 |
| FR-14 | Let the user find a product by browsing photos or by searching by name. | Must | CR-10, H-01, DI-10 | S-01, S-03 |
| FR-15 | Let the user add a product by scanning its barcode with an external scanner or the phone camera. | Should | CR-16, DI-10 | S-03 |
| FR-16 | Let the user change the quantity of each product before confirming the sale. | Must | CR-11, DI-02 | S-01, S-02 |
| FR-17 | Offer three payment methods: cash, card and Interuady. | Must | CR-12 | S-01, S-02, S-03 |
| FR-18 | Calculate change for cash payments from the amount received. **(H)** | Could | H-05, DI-03 | S-01 |
| FR-19 | Record card payments by payment method only, without capturing any card data. | Must | CR-12, H-10, Q-06, DI-11 | S-03 |
| FR-20 | When Interuady is selected, display three mandatory fields — unit (*departamento o dependencia*), C.P. responsible for the payment, requester or authorizer — and prevent confirming the sale until all three are filled. | Must | CR-13, DI-06, DI-07 | S-02 |
| FR-21 | Offer a selectable list of UADY units for the unit field. **(H)** | Could | H-08, DI-08 | S-02 |
| FR-22 | Deduct the sold quantities automatically from the stock of the warehouse where the sale took place. | Must | CR-15, DI-05 | S-01 |
| FR-23 | Issue a receipt, printed on a thermal printer or shown on screen. The receipt content (VAT breakdown) depends on Q-05. | Should | CR-17, CR-18, Q-05 | S-01 |

## 4. Accounts receivable

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-24 | Create an accounts receivable note for every sale paid with Interuady. | Must | CR-14, DI-09 | S-02 |
| FR-25 | Show the accounts receivable section to **all** profiles, with filters by unit, status and date. | Must | CR-14, DI-19 | S-06 |
| FR-26 | Show the personal details of each note (C.P. responsible, requester) only to profiles with query permission (CDU, Central Administration). **Proposal pending client approval.** | Should | CR-13, CR-14, CR-01, CR-02 | S-06 |

## 5. Offline operation and synchronization

| ID | The system shall… | Priority | Origin | Scenario |
|---|---|---|---|---|
| FR-27 | Allow every sales function (FR-13…FR-24) to work without connectivity, storing sales locally in a queue. | Must | PRJ-02, DI-04 | S-01 |
| FR-28 | Synchronize automatically when connectivity returns: send queued sales and receive catalog, price and stock updates published by CDU. | Must | PRJ-02, CR-09, CR-15 | S-01, S-04, S-05 |
| FR-29 | Show the synchronization status in plain language (e.g. "Saved on this phone — it will be sent when there is internet"), without blocking any sale. | Must | PRJ-02, PRJ-03, H-01, DI-04 | S-01 |

## 6. Deferred (depend on client answers)

| ID | Candidate requirement | Blocked by |
|---|---|---|
| FR-D1 | Invoicing and VAT breakdown on receipts | CR-18, Q-05 |
| FR-D2 | Stock transfers between warehouses | Q-07 |
| FR-D3 | Sale cancellations, returns and size exchanges | Q-10 |
| FR-D4 | Integration with a bank card terminal | Q-06 |
| FR-D5 | Settlement of Interuady notes (mark as paid) | Q-09 |
| FR-D6 | Which warehouse Central Administration sales are deducted from | Q-02 |
