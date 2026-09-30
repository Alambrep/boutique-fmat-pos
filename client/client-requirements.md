# Client requirements

Primary source: the document "Proceso de inventario y venta — Boutique" (*Boutique inventory and sales process*), provided by the professor (client). The Spanish original is kept in [`originals/`](originals/).

This file only **transcribes, translates and numbers** what the client wrote. It adds no interpretation: wherever the text is ambiguous, an open question `Q-xx` is recorded.

## Client requirements (CR) — written document

### Profiles and permissions

| ID | Requirement | Source section |
|---|---|---|
| CR-01 | **CDU** profile: modify, query and charge. | Inventory — sessions |
| CR-02 | **Central Administration** (*Administración Central*) profile: query and charge. | Inventory — sessions |
| CR-03 | **Social Sciences Campus** (*Campus Sociales*) profile: charge only. | Inventory — sessions |
| CR-04 | **Exact Sciences Campus** (*Campus Ciencias Exactas*) profile: charge only. | Inventory — sessions |

### Inventory

| ID | Requirement | Source section |
|---|---|---|
| CR-05 | When a product is registered, its data is entered manually. | Inventory |
| CR-06 | When a product is registered, a photo is attached. | Inventory |
| CR-07 | The system generates barcodes for the products. | Inventory |
| CR-08 | An inventory table is generated **per warehouse** (CDU, Sociales, Matemáticas) with the fields: Code, Product, Type, Color, Size, Stock, Net cost, Sale price, Supplier, Warehouse. | Inventory — table |
| CR-09 | Products for each store are registered **from CDU**, which is the main warehouse. | Inventory |

Example record provided by the client (data kept in Spanish):

| Code | Product | Type | Color | Size | Stock | Net cost | Sale price | Supplier | Warehouse |
|---|---|---|---|---|---|---|---|---|---|
| P010203 | Playera Jaguar Azul | Playera o Polo | Azul | Mediana o N/A | 100 | $100.00 | $200.00 | Spiro | CDU |

### Sales

| ID | Requirement | Source section |
|---|---|---|
| CR-10 | The sales screen shows the product image and preloaded data: image, code, product and sale price. | Sales |
| CR-11 | The quantity of products can be changed at the time of sale. | Sales |
| CR-12 | Payment methods: cash, card and Interuady. | Sales — 1 |
| CR-13 | When paying with Interuady, 3 **mandatory** fields are displayed: department or unit (*departamento o dependencia*); C.P. responsible for the payment (*C.P. responsable del pago*); requester or authorizer (*solicitante o quien autoriza*). | Sales — 1.a |
| CR-14 | Notes paid with Interuady go to an **accounts receivable** section, available for consultation by **all** users. | Sales — 1.b |
| CR-15 | Sales are automatically deducted from the inventory of the warehouse or boutique where they took place. | Sales |
| CR-16 | Use of a **barcode scanner** to make sales easier. _(The client frames it as something that "would make the process easier"; priority to be confirmed.)_ | Sales |
| CR-17 | Use of a **thermal receipt printer** to reduce costs. _(Same nuance as CR-16.)_ | Sales |
| CR-18 | Confirm with accounting whether the receipt must break down subtotal and VAT (*IVA*), and clarify the invoicing process. _(Pending on the client's side; see Q-05.)_ | Sales — question |

## Project requirements (PRJ) — professor's project brief

These do not appear in the written document. **Source:** stated by the professor (client) in person, in a conversation at his office at FMAT on 2026-08-14 (see the [meeting log](../docs/00-management/meetings.md)). No written copy is available.

| ID | Requirement |
|---|---|
| PRJ-01 | Runs on low-end mobile devices. |
| PRJ-02 | Works offline. |
| PRJ-03 | Is simple enough for a person with limited technology skills (client's example: a hot dog vendor). |

## Open questions for the client

| ID | Question | Affects | Status |
|---|---|---|---|
| Q-01 | What does **CDU** stand for, and where is it physically located? | CR-01, CR-08, CR-09 | Open |
| Q-02 | There are 4 profiles but 3 warehouses: which warehouse's stock does **Central Administration** sell from? | CR-02, CR-15 | Open |
| Q-03 | Does the **Exact Sciences Campus** profile correspond to the **Matemáticas** warehouse? | CR-04, CR-08 | Open |
| Q-04 | In Interuady payments, what does **"C.P."** mean in "C.P. responsible for the payment"? | CR-13 | Open |
| Q-05 | Must the receipt break down subtotal and VAT? How is an invoice requested and issued? | CR-17, CR-18 | Open |
| Q-06 | For **card** payments, does the system only record the payment method (charged on a separate terminal), or must it integrate with the terminal? | CR-12 | Open |
| Q-07 | How is stock moved from CDU to the other warehouses (transfers)? Who records them? | CR-08, CR-09, CR-15 | Open |
| Q-08 | Is there a rule for building the product code (e.g. P010203), or is it sequential? | CR-07, CR-08 | Open |
| Q-09 | How is an Interuady note settled in accounts receivable, and who marks it as paid? | CR-14 | Open |
| Q-10 | Are cancellations, returns or size exchanges required? | CR-15 | Open |
| Q-11 | Does each point of sale use its own device or a shared one? Who creates user accounts? | CR-01…CR-04 | Open |
| Q-12 | Which specific devices will be used (model, operating system), and is there budget for a scanner and a printer? | PRJ-01, CR-16, CR-17 | Open |
| Q-13 | The document uses *almacén*, *bodega*, *tienda* and *boutique*. Is each warehouse (CDU, Sociales, Matemáticas) also a point of sale, or are there points of sale separate from the warehouses? | CR-08, CR-09, CR-15 | Open |
| Q-14 | May charge-only profiles see on the sales screen whether a product is available at their point, or does that count as "query" (*consulta*)? | CR-03, CR-04, FR-31 | Open |
| Q-15 | Where will the synchronization server be hosted (UADY infrastructure, a cloud service, none), and who maintains it? | PRJ-02, CR-08, CR-14 | Open |
| Q-16 | Do other UADY units already use a point-of-sale or inventory system that this project should align with or learn from? | CR-01…CR-18 | Open |
