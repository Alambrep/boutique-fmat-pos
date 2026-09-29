# References

> Every source below was opened and checked against the statement it supports on **2026-09-28**. Citations in the documents use the `[Rn]` identifiers. Quotes are kept short; everything else is paraphrased.
>
> **How to verify a citation:** open the link, search the page (Ctrl+F) for the keyword given in the "Where to look" column, and confirm the statement matches.

## Usability and HCI

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R1 | Nielsen, J. (2012, reviewed 2026). *Usability 101: Introduction to Usability.* Nielsen Norman Group. https://www.nngroup.com/articles/usability-101-introduction-to-usability/ | The five usability quality components (learnability, efficiency, memorability, errors, satisfaction) used to organize the NFRs. | "five quality components" |
| R2 | ISO 9241-11:2018. *Ergonomics of human-system interaction — Part 11: Usability: Definitions and concepts.* https://www.iso.org/standard/63500.html — definition as reproduced by NIST CSRC Glossary: https://csrc.nist.gov/glossary/term/usability | Definition of usability as effectiveness, efficiency and satisfaction for specified users, goals and context of use. | "specified users" (NIST page) |
| R34 | ISO 9241-210:2019. *Ergonomics of human-system interaction — Part 210: Human-centred design for interactive systems.* https://www.iso.org/standard/77520.html — activities as described in the public preview: https://cdn.standards.iteh.ai/samples/77520/8cac787a9e1549e1a7ffa0171dfa33e0/ISO-9241-210-2019.pdf | The four iterative human-centred design activities used as the project's development process (README §3). | "context of use" |
| R3 | W3C. *Web Content Accessibility Guidelines (WCAG) 2.2*, Success Criterion 1.4.3 Contrast (Minimum), Level AA. https://www.w3.org/TR/WCAG22/ | Minimum contrast of 4.5:1 for normal text and 3:1 for large text (NFR-10). | "1.4.3" |
| R4 | Android Developers. *Make apps more accessible.* https://developer.android.com/guide/topics/ui/accessibility/apps | Recommended touch target of at least 48 dp × 48 dp (NFR-09). | "48dp" |
| R5 | Sauro, J. *Measuring Usability with the System Usability Scale (SUS).* MeasuringU. https://measuringu.com/sus/ | Average SUS score of 68, based on 500 evaluations and more than 5,000 users (NFR-08). | "68" |

## User modeling and Lean UX

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R6 | Laubheimer, P. (2020). *3 Persona Types: Lightweight, Qualitative, and Statistical.* Nielsen Norman Group. https://www.nngroup.com/articles/persona-types/ | Proto-personas are based on the team's existing knowledge and assumptions, not new research; they suit Lean UX but risk being inaccurate, so they should lead to research. | "Proto Personas" |
| R7 | Seiden, J. *Proto-Personas: How to Create User Alignments in Under an Hour.* Sense & Respond. https://www.senseandrespond.co/blog/proto-personas | Proto-personas must be treated as hypotheses and their most critical assumptions tested with users. | "hypotheses" |
| R8 | Gothelf, J., & Seiden, J. (2021). *Lean UX* (3rd ed.), ch. 10 "Hypotheses". O'Reilly Media. https://www.oreilly.com/library/view/lean-ux-3rd/9781098116293/ch10.html | Turning assumptions into testable statements that start with "We believe…" (format adapted in `hypotheses.md`). | "We believe" |
| R9 | Bland, D. J. (2020). *How Assumptions Mapping Can Focus Your Teams on Running Experiments That Matter.* Strategyzer. https://www.strategyzer.com/library/how-assumptions-mapping-can-focus-your-teams-on-running-experiments-that-matter | Prioritizing assumptions by importance and evidence; test the important, low-evidence ones first (assumption map in `hypotheses.md` §4). | "top right" |
| R10 | Cooper, A., & Reimann, R. (2003). *About Face 2.0.* Wiley — as summarized in ScienceDirect Topics, *Primary Persona*: https://www.sciencedirect.com/topics/computer-science/primary-persona | Primary personas need their own interface; secondary personas can be served by interfaces designed for others (classification in `proto-personas.md`). | "secondary persona" |

## Requirements and architecture

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R11 | Agile Business Consortium. *What is MoSCoW Prioritization?* https://www.agilebusiness.org/resource/what-is-moscow-prioritization/ | Must / Should / Could / Won't have this time categories used to prioritize FRs. | "Must Have" |
| R12 | Kleppmann, M., Wiggins, A., van Hardenberg, P., & McGranaghan, M. (2019). *Local-first software: You own your data, in spite of the cloud.* Onward! 2019, ACM. https://www.inkandswitch.com/essay/local-first/ | Keeping the primary copy of data on the device so it can be used offline and synchronized later (offline-first approach, challenge 1). | "offline" |

## Hardware and platform

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R13 | Zebra Technologies. *Keyboard Wedge Interface* (SM72 integration guide). https://docs.zebra.com/us/en/scanners/general/sm72-ig/keyboard-wedge-interface.html | Scanners in keyboard-wedge mode send barcode data as keystrokes, as if typed (challenge 3, NFR-23). | "keystrokes" |
| R14 | MDN Web Docs. *Web Bluetooth API.* https://developer.mozilla.org/en-US/docs/Web/API/Web_Bluetooth_API | Web Bluetooth is experimental and not Baseline (limited browser support) (challenge 3, NFR-24). | "Experimental" |
| R15 | Chrome for Developers. *Communicating with Bluetooth devices over JavaScript.* https://developer.chrome.com/docs/capabilities/bluetooth | A subset of Web Bluetooth is available in Chrome for Android, ChromeOS, Mac and Windows; iOS is not listed (challenge 3). | "Chrome for Android" |

## Payments and data protection

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R16 | PCI Security Standards Council. *PCI Data Security Standard (PCI DSS).* https://www.pcisecuritystandards.org/standards/pci-dss/ | PCI DSS applies to entities that store, process or transmit cardholder data (challenge 4, NFR-21). | "store, process, or transmit" |
| R17 | Cámara de Diputados. *Ley General de Protección de Datos Personales en Posesión de Sujetos Obligados* — published in the DOF on 2025-03-20; latest reform 2025-11-14. https://www.diputados.gob.mx/LeyesBiblio/ref/lgpdppso.htm | Current federal general law on personal data held by public-sector entities (challenge 4, NFR-22). | Publication and reform dates |
| R18 | Gobierno del Estado de Yucatán (2025). *Decreto 100/2025* — issues the *Ley de Protección de Datos Personales en Posesión de Sujetos Obligados del Estado de Yucatán*, published 2025-08-28; abrogates the 2017 state law. https://www.pjyucatan.gob.mx/files/digestum/marcoLegal/02/2025/DIGESTUM02414.pdf | Current state law; it covers constitutional autonomous bodies among the obligated subjects (Art. 1). | "organismos constitucionales autónomos" |
| R19 | Universidad Autónoma de Yucatán. *Aviso integral de privacidad — cámaras de vigilancia.* https://uady.mx/assets/AvisoPrivacidadCamarasSeguridad.pdf | UADY issues its privacy notices under the general law for obligated subjects, i.e. it treats itself as a public-sector data controller. | "Sujetos Obligados" |

## Social relevance data

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R20 | INEGI (2026). *Encuesta Nacional sobre Disponibilidad y Uso de Tecnologías de la Información en los Hogares (ENDUTIH) 2025 — Reporte de resultados 19/26.* https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2026/endutih/ENDUTIH_25_RR.pdf | In 2025, 86.1% of the population aged 6+ used the internet (p. 3), and 97.0% of cell phone users used a smartphone (p. 16). | "86.1", "97.0" |
| R21 | INEGI (2025). *Estadísticas a propósito del Día de las Micro, Pequeñas y Medianas Empresas*, based on Censos Económicos 2024 (resultados oportunos). https://www.inegi.org.mx/contenidos/saladeprensa/aproposito/2025/EAP_MIPYMES_25.pdf | Only 22.3% of micro establishments used computers and 23.5% used the internet (p. 3). | "22.3", "23.5" |

## Commercial POS comparison

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R22 | Loyverse Help Center. *Offline Use of Loyverse POS.* https://help.loyverse.com/help/offline-work-of-pos | Sales and shifts work offline; refunds, stock levels, card terminal payments and email receipts do not; offline receipts sync later. | "Unsynced" |
| R23 | Loyverse Help Center. *How to Create and Manage Multiple Stores under One Account.* https://help.loyverse.com/help/how-create-and-manage-multiple | Price, stock and low-stock alerts can be set per store. | "per store" |
| R24 | Loyverse. *Pricing.* https://loyverse.com/pricing | Core POS is free, including multi-store management; paid add-ons per store (Unlimited Sales History, Employee Management, Advanced Inventory). | "Advanced Inventory" |
| R25 | Loyverse Help Center. *Configuring Payment Types in Loyverse POS.* https://help.loyverse.com/help/configuring-payment-types-loyverse | Custom named payment types that appear in reports. | "custom name" |
| R26 | Shopify Help Center. *Using Shopify POS offline.* https://help.shopify.com/en/manual/sell-in-person/shopify-pos/selling-offline | Cash and manual payments work offline; card payments need the offline payments feature; syncing with the admin needs internet. | "offline" |
| R27 | Shopify Help Center. *Managing payment methods for Shopify POS.* https://help.shopify.com/en/manual/sell-in-person/getting-started/setup-payment-method/enable-payments | Custom payment methods for payments not processed by Shopify, used for tracking. | "custom payment" |
| R28 | Clip. *Clip Total 3 — Punto de venta móvil con inventario.* https://shop.clip.mx/products/clip-total | Dedicated terminal with inventory control and built-in thermal printer; no multi-branch management mentioned. | "inventario" |
| R29 | Square Support Center. *Accept payment cards with Square — international availability.* https://squareup.com/help/us/en/article/4956-international-availability | Card acceptance available in eight countries; Mexico is not among them. | "currently available" |

## Research methods

| ID | Reference | Supports | Where to look |
|---|---|---|---|
| R30 | Flaherty, K. (2020). *Contextual Inquiry: Inspire Design by Observing and Interviewing Users in Their Context.* Nielsen Norman Group. https://www.nngroup.com/articles/contextual-inquiry/ | Observing and interviewing users while they do their work in their own environment (V-01). | "master" |
| R31 | Nielsen, J. (2000). *Why You Only Need to Test with 5 Users.* Nielsen Norman Group. https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/ | Small usability tests of about 5 users, repeated iteratively; separate smaller groups when user types differ (V-07). | "5 users" |
| R32 | Krause, R., & Pernice, K. (2024). *Affinity Diagramming for Sorting UX Findings and Ideas.* Nielsen Norman Group. https://www.nngroup.com/articles/affinity-diagram/ | Clustering research observations into themes to analyze findings. | "clusters" |
| R33 | Braun, V., & Clarke, V. (2006). Using thematic analysis in psychology. *Qualitative Research in Psychology, 3*(2), 77–101. https://doi.org/10.1191/1478088706qp063oa | Thematic analysis of qualitative data. | Bibliographic record |

## Still pending

- **Commercial POS comparison:** Shopify POS multi-store and cost, and Clip offline support for specific products, were not reviewed.
- **Yucatán-specific ENDUTIH figures:** the 2025 national report does not break them out in the text; check INEGI's state tabulations.
