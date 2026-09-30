# Rubric map — Delivery 1

Where each item of the [delivery 1 rubric](client/originals/Rubric_1st_Delivery-HCI.pdf) is covered in this repository. Every link opens the exact section. The rubric text is quoted in *italics* so each row can be checked against the rubric sheet.

**Author:** Alan Pérez · **Branch:** [`first-delivery`](https://github.com/Alambrep/boutique-fmat-pos/tree/first-delivery) · **Tag:** [`delivery-1`](https://github.com/Alambrep/boutique-fmat-pos/releases/tag/delivery-1) · **Video:** [youtu.be/kahF-t9Y5TM](https://youtu.be/kahF-t9Y5TM)

---

## 1. Definition of the project

| Rubric item | Where to find it | What it contains |
|---|---|---|
| **Social relevance** — *arguments of importance of the issue… sources or evidence your proposal could be considered a social issue* | [Project definition §2](docs/01-definition/project-definition.md#2-social-relevance): [§2.0 context known to the author](docs/01-definition/project-definition.md#20-context-known-to-the-author), [§2.1 digital inclusion](docs/01-definition/project-definition.md#21-digital-inclusion-of-people-with-low-technology-skills), [§2.2 public resources](docs/01-definition/project-definition.md#22-responsible-management-of-a-public-institutions-resources), [§2.3 personal data](docs/01-definition/project-definition.md#23-personal-data-protection) · [Desk research DR-2](docs/02-research/results/desk-research.md#dr-2--social-context) | Three arguments with INEGI evidence (R20, R21) and the author's first-hand context |
| **Innovation** — *how it could be considered "different" compared to previous experiences/developments* | [Project definition §3](docs/01-definition/project-definition.md#3-innovation): [§3.1 differentiators](docs/01-definition/project-definition.md#31-proposed-differentiators), [§3.2 comparison](docs/01-definition/project-definition.md#32-comparison-with-existing-solutions) · [Desk research DR-1](docs/02-research/results/desk-research.md#dr-1--existing-solutions) | Comparison with Loyverse, Shopify POS, Clip and Square from official documentation (R22–R29); baseline of the current process |
| **Feasibility** — *arguments to guarantee success; strengths and weaknesses of the team; challenges from the point of view of HCI/product* | [§4.1 strengths and weaknesses](docs/01-definition/project-definition.md#41-team-strengths-and-weaknesses-individual-work), [§4.2 HCI and product challenges](docs/01-definition/project-definition.md#42-hci-and-product-challenges), [§4.3 risks](docs/01-definition/project-definition.md#43-project-risks), [§5 scope](docs/01-definition/project-definition.md#5-proposed-scope) | Five challenges (offline sync, low-end devices, scanner and printer, personal data, simplicity), risks with mitigation |

## 2. Project process: user research

| Rubric item | Where to find it | What it contains |
|---|---|---|
| **Researching — data & info required** | [Validation plan §1 research questions](docs/02-research/validation-plan.md#1-research-questions), [§3 data to collect](docs/02-research/validation-plan.md#3-data-to-collect-and-analysis) · [Hypotheses](docs/02-research/hypotheses.md#3-hypotheses) | 5 research questions; 17 testable hypotheses prioritized with an [assumption map](docs/02-research/hypotheses.md#4-prioritization-assumption-map) |
| **Researching — materials and instruments** | [Validation plan §2 activities](docs/02-research/validation-plan.md#2-activities) · [Instruments folder](docs/02-research/instruments/) | Observation guide, seller and staff interview guides, device and connectivity checklist; informed consent ([§4 ethics](docs/02-research/validation-plan.md#4-ethics-and-personal-data)) |
| **Researching — analysis** | [Validation plan §3](docs/02-research/validation-plan.md#3-data-to-collect-and-analysis) | Affinity diagramming and thematic analysis; decision thresholds for each hypothesis |
| **Researching — results** | [Desk research results DR-1…DR-5](docs/02-research/results/desk-research.md) · [Hypotheses evidence log](docs/02-research/hypotheses.md#6-evidence-log) | Results of desk research; no field findings yet (see *Known gaps*) |
| **Scheduling — activities, task/activities assignment, artifacts, products** | [Schedule](docs/00-management/schedule.md#1-project-roadmap) · [Task log](docs/00-management/task-log.md) · [GitHub issues and milestone](https://github.com/Alambrep/boutique-fmat-pos/milestone/1?closed=1) · [Deliverables](README.md#7-delivery-1-deliverables) | Roadmap of 3 deliveries, activities per task with owner, session timeline, plans for deliveries 2 and 3 |
| **Repository — organization and documentation; easy to follow the process, activities, main findings, artifacts** | [README](README.md): [reading order](README.md#2-how-to-read-this-repository), [development process](README.md#development-process), [main results](README.md#main-results-so-far-desk-research), [structure](README.md#6-repository-structure) | Numbered folders in process order, identifiers and conventions, traceability generated by [`tools/trace.py`](tools/trace.py) |

## 3. User modeling

| Rubric item | Where to find it | What it contains |
|---|---|---|
| **User profiles** | [Proto-personas §1, user profiles](docs/03-user-modeling/proto-personas.md#user-profiles) | Profile of each user class by attribute |
| **Personas** | [P-01](docs/03-user-modeling/proto-personas.md#2-p-01--satellite-seller-primary), [P-02](docs/03-user-modeling/proto-personas.md#3-p-02--cdu-inventory-manager-primary), [P-03](docs/03-user-modeling/proto-personas.md#4-p-03--central-administration-officer-secondary) | Proto-personas with goals, frustrations and design needs; every attribute cites its origin |
| **Scenarios** | [Scenarios S-01…S-08](docs/03-user-modeling/scenarios.md) | Offline, error and first-use scenarios, each with design implications |
| **How the data/info collected were used to create these artifacts** | [Proto-personas §0](docs/03-user-modeling/proto-personas.md#0-how-the-inputs-were-used) · [Traceability matrix](docs/04-requirements/traceability-matrix.md#1-matrix) | Chain from client requirements and hypotheses to profiles, personas, scenarios and requirements |
| **Definition of principal and secondary users** | [Proto-personas §1, user classes](docs/03-user-modeling/proto-personas.md#1-user-classes) | Two primary and one secondary proto-persona, following Cooper (R10) |

## 4. Product requirements

| Rubric item | Where to find it | What it contains |
|---|---|---|
| **Functional requirements** | [Functional requirements](docs/04-requirements/functional-requirements.md) | 39 FRs with origin and MoSCoW priority, plus 6 deferred FRs tied to open questions |
| **Non-functional requirements based on HCI/usability attributes** | [Non-functional requirements §1, usability attributes](docs/04-requirements/non-functional-requirements.md#1-usability-attributes) and following sections | 28 NFRs organized by Nielsen's usability components (R1) and ISO 9241-11 (R2), each with a tentative target and a measurement method |
| Supporting: traceability | [Traceability matrix](docs/04-requirements/traceability-matrix.md) | Every client requirement covered; impact if a hypothesis is refuted or a question answered |

## 5. Presentation

| Rubric item | Where to find it |
|---|---|
| **1st delivery presentation** — *quality of the materials, information formatting, timing, speech quality* | [Video](https://youtu.be/kahF-t9Y5TM) · [Presentation folder](docs/05-presentation/README.md) |

## 6. Collaborative work (individual project)

| Rubric item | Where to find it | What it contains |
|---|---|---|
| **Meeting logs** | [Meeting log](docs/00-management/meetings.md) | Client meeting of 2026-08-14 and planned meetings |
| **Responsibilities** | [Task log](docs/00-management/task-log.md) · [AI assistance statement](README.md#12-ai-assistance-statement) | Owner of every task; what the author did and what the AI assistant did |
| **Activities** | [Logbook](docs/00-management/logbook/) | One entry per work session, with decisions |
| **Tasks** | [Task log](docs/00-management/task-log.md) · [GitHub issues](https://github.com/Alambrep/boutique-fmat-pos/issues?q=is%3Aissue) | T-01…T-13 with dates and the commits of each task |
| **Individual contribution metric based on objective/quantifiable elements** | [Contribution metrics §1](docs/00-management/contribution-metrics.md#1-quantitative-metrics), [§2 author-attributable](docs/00-management/contribution-metrics.md#2-author-attributable-metrics), [§3 decisions](docs/00-management/contribution-metrics.md#3-author-decisions) | Figures computed from git by [`tools/metrics.py`](tools/metrics.py) |
| **Essential elements of a "process development product"** | [Development process](README.md#development-process) · [Workflow](README.md#8-workflow-and-contribution-evidence) | Branch per delivery, issues, Conventional Commits, pull request and tag per delivery |

---

## Known gaps of this delivery

- **No field research yet** (criteria 2 and 3). This was a deliberate decision because of time and individual work ([README §3](README.md#3-delivery-1-approach)). User models are proto-personas built from the client's requirements and explicit hypotheses; field research is planned for delivery 2 ([validation plan](docs/02-research/validation-plan.md)).
- **Open questions for the client** (Q-01…Q-16) are listed in [client requirements](client/client-requirements.md#open-questions-for-the-client); requirements that depend on them are deferred.
