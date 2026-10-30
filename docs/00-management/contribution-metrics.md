# Individual contribution metrics

> **Tasks:** T-12 (delivery 1), T-27 (delivery 2) · **Rubric criteria:** 6 (delivery 1); 5b (delivery 2) · **Contributor:** Alan Pérez (individual project — 100% of the tasks are assigned to the author)
>
> Metrics are computed from **objective sources**: git history, GitHub issues, the task log and the logbook. The tables of §1 and §2 are produced by [`tools/metrics.py`](../../tools/metrics.py) and recomputed at the close of each delivery.

## 0. How individual contribution is measured

The metric is the **share of the completed work owned by each team member**, weighted by the complexity of each task.

| Parameter | Definition | Source | Objective because |
|---|---|---|---|
| **P1 — Tasks owned** | Tasks (`T-xx`) assigned to the member, by status: completed, in progress, planned, cancelled | [Task log](task-log.md), GitHub issues | Each issue names its owner and status |
| **P2 — Complexity** | Estimated hours of the task, used as its weight | *Estimated hours* of each issue | Set **before** work started (from delivery 2; delivery 1 had no estimates, so its tasks weigh 1 each) |
| **P3 — Actual hours** | Session hours spent on the task | [Logbook](logbook/), one entry per session | Recorded per session, with the split per task |
| **P4 — Commits** | Commits that reference the task | Git history | Counted by the script, not by hand |
| **P5 — Author-attributable work** | Decisions, facts supplied, reviews and tests that only the author can do (§3, §4) | Logbook and this file | Each one is dated and has an observable effect |

**Formula.** Contribution of member *m* in a delivery = Σ P2 of the **completed** tasks owned by *m* ÷ Σ P2 of all completed tasks. Cancelled tasks count for nobody. The shares of all members add up to 100%. **Progress** of a delivery = Σ P2 of completed tasks ÷ Σ P2 of all non-cancelled tasks. P3, P4 and P5 are reported next to it so the share can be checked against the actual work.

**The AI assistant is not a team member.** It is a tool used by the author (see [README §12](../../README.md#12-ai-assistance-statement)), so it receives no share; its participation is visible in P4 (co-authored commits) and in the logbook, and §3 measures what only the author did.

## 1. Contribution per delivery

Computed by `tools/metrics.py` from the task log.

| Member | Delivery 1 | Delivery 2 | Delivery 3 |
|---|---|---|---|
| Alan Pérez | 100% (13 of 13 tasks) | 100% (11.5 of 11.5 h) | — |

**Delivery 2 progress** (recomputed at the close of the delivery):

| Metric | Value |
|---|---|
| Tasks | 15 (7 completed, 3 in progress, 3 planned, 2 cancelled) |
| Progress | 11.5 of 21.0 estimated hours completed (**55%**), excluding cancelled tasks |
| Actual hours logged in delivery 2 tasks | ≈ 3.0 h |

## 2. Quantitative metrics

### 2.1 Current snapshot

Snapshot: commit `95aa112` (2026-10-30 17:07, UTC−6)

| Metric | Value |
|---|---|
| Commits (without merges) | **97** (Delivery 1: 74, Delivery 2: 23); merge commits: 2 |
| Commits per day | 13 on 2026-09-28, 55 on 2026-09-29, 6 on 2026-09-30, 8 on 2026-10-27, 9 on 2026-10-29, 6 on 2026-10-30 |
| Commits by type | `docs`: 62 · `fix`: 24 · `feat`: 4 · `chore`: 4 · `design`: 3 |
| Lines added / removed | **+5,926 / −915** |
| Words in Markdown documents | ≈ 49,800 |
| Traceable items | 18 CR, 3 PRJ, 17 Q, 17 H, 3 P, 8 S, 32 DI, 39 FR, 6 deferred FR, 28 NFR, 8 V, 42 references, 22 G, 16 SCR, 7 IX |
| Commits co-authored with the AI assistant | 97 of 97 |
| Rework commits (`fix`) | 24 of 97 |

Commits per task:

| Task | T-01 | T-02 | T-03 | T-04 | T-05 | T-06 | T-07 | T-08 | T-09 | T-10 | T-11 | T-12 | T-13 | T-14 | T-15 | T-16 | T-17 | T-18 | T-19 | T-20 | T-21 | T-22 | T-24 | T-25 | T-26 | T-28 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Commits referencing it | 12 | 8 | 7 | 6 | 4 | 6 | 6 | 6 | 7 | 3 | 8 | 7 | 2 | 4 | 4 | 2 | 2 | 2 | 3 | 4 | 2 | 2 | 2 | 1 | 5 | 1 |

### 2.2 Delivery 1 snapshot, as delivered

Produced by `tools/metrics.py` at commit `e0854ac` (2026-09-30 15:20, UTC−6), excluding the commit that updated this file.

| Metric | Value |
|---|---|
| Tasks completed | **13 of 13** |
| Commits | **72** (13 on 2026-09-28, 55 on 2026-09-29, 4 on 2026-09-30) |
| Commits by type | `docs`: 43 · `fix`: 23 · `chore`: 4 · `feat`: 2 |
| Lines added / removed | **+2,909 / −667** |
| Words in Markdown documents | ≈ 26,100 |
| Traceable items | 18 CR, 3 PRJ, 16 Q, 17 H, 3 P, 8 S, 32 DI, 39 FR, 6 deferred FR, 28 NFR, 8 V, 34 references |
| Commits co-authored with the AI assistant | 72 of 72 |
| Rework commits (`fix`) | 23 of 72 |
| Hours logged | **≈ 5.6 h** (5 sessions, approximate: 2.3 h on 2026-09-28, 2.4 h on 2026-09-29, 0.9 h on 2026-09-30; video recording not logged; see the [logbook](logbook/)) |

### Commits per task

| Task | T-01 | T-02 | T-03 | T-04 | T-05 | T-06 | T-07 | T-08 | T-09 | T-10 | T-11 | T-12 | T-13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Commits referencing it | 11 | 8 | 7 | 6 | 4 | 6 | 6 | 6 | 7 | 3 | 8 | 6 | 2 |

A commit can reference more than one task.

**How to read these figures.** About five and a half hours of logged work produced roughly 25,000 words of documentation because drafting was done with an AI assistant, as declared in [README §12](../../README.md#12-ai-assistance-statement). The volume metrics above therefore describe the *project's* output, not the author's typing. The author's individual contribution is measured in §2 and documented session by session in the logbook. The `fix` commits are rework after reviews, which is part of the iterative process described in README §3.

## 3. Author-attributable metrics

Commits and lines measure the joint output of the author and the AI assistant (every commit is co-authored). The counts below measure what only the author can do: direct the work, supply facts that no document contains, and ask for the work to be reviewed. They show direction and oversight, not authorship of the text.

| Metric | Delivery 1 | Delivery 2 (so far) | How it is counted |
|---|---|---|
| Direction decisions | **15** | **14** | Rows of the decisions tables (§4) |
| Facts supplied by the author that no document contained | **6**: the author's real name; the date and setting of the project brief (2026-08-14, in person); location and connectivity of the boutique's point at FMAT; the original client document and rubric; the presentation format (video); the delivery date (2026-09-30) | **7**: delivery 2 date and video limit; the text and screenshots of both messages to the client; the time of the reminder and the date of the in-person attempt; the delivery 2 and final rubrics; the number of proxy participants available; not knowing the terms *Interuady* and *C.P.*; the result of the test on his iPhone | README header, [meeting log](meetings.md), `client/originals/`, [schedule](schedule.md), [logbook](logbook/) |
| Reviews of the whole repository requested by the author | **2** (2026-09-29 17:39 and 18:33, both by Claude in separate conversations; the second in nine steps) | — | [Logbook 2026-09-29](logbook/2026-09-29.md) |
| Reviews and tests done by the author | — | **2**: review of prototype v1 (2026-10-29); test on an iPhone 14 Pro Max (2026-10-30) | [Logbook 2026-10-29](logbook/2026-10-29.md), [prototype README](../../design/prototype/v1/README.md#test-on-a-real-phone) |
| Actions outside the repository | — | **3**: reminder to the client (2026-10-19), attempt to meet him in person (2026-10-26), enabling GitHub Pages (2026-10-30) | [Meeting log](meetings.md#communications-with-the-client), [logbook](logbook/) |
| Review proposals not applied or adapted after checking them against the files and sources | **12** | — | Listed with their reasons in the [logbook](logbook/2026-09-29.md); the checks were done with the AI assistant and the author received a summary after each step |

## 4. Author decisions

### Delivery 1

Because the AI assistant co-authored every commit, the author's contribution is also recorded as the **decisions that directed the work**. Times come from the working session.

| Date and time | Decision | Effect on the project |
|---|---|---|
| 2026-09-28 19:35 | Work individually with a Lean UX proto-persona approach, without field research in delivery 1; prioritize speed; require that every assumption be labeled as a hypothesis and traced | Shaped all artifacts and labels (`H`, `CR`, `PRJ`) |
| 2026-09-28 22:34 | One branch per delivery (`first-delivery`, …) | Branching convention in the README |
| 2026-09-28 22:45 | All repository content in English | Repository translated; history rewritten once |
| 2026-09-28 23:17 | Use the AI assistant openly and declare it | AI assistance statement (README §12) |
| 2026-09-28 23:31 | Mention open questions in the video and send them to the client after the delivery | Presentation content; Q-01…Q-12 kept open |
| 2026-09-28 23:41 | Provide prior knowledge about connectivity at the FMAT point | Evidence log entry for H-03 |
| 2026-09-28 23:47 | Back every decision with verified, reliable sources | `references.md` (R1–R34 as of 2026-09-29) |
| 2026-09-29 00:10 | Deliver the presentation as a video; keep the script out of the repository | `docs/05-presentation/` |
| 2026-09-29 17:39 | Request an independent review of the whole repository against the rubric | Review findings (contradictions, unlabeled assumptions, outdated metrics) |
| 2026-09-29 17:48 | Apply the review's critical and quick fixes; skip optional items; provide the date and setting of the project brief | FR-30…FR-34, H-15, H-16, Q-13, Q-14, S-07, [meeting log](meetings.md) |
| 2026-09-29 18:20 | Keep the existing repository mentions of the presentation video; do not rewrite history to remove them | No history rewrite |
| 2026-09-29 18:33 | Request a step-by-step audit of every artifact against the rubric and the client document, and review each step's outcome before moving on | Audit steps 1–8 applied selectively (see [logbook](logbook/2026-09-29.md)) |
| 2026-09-29 18:57 | Correct the delivery date (2026-09-30) and use the extra time to finish the audit before recording the video | Due date corrected in README, schedule and milestone |
| 2026-09-29 19:01 | Keep `main` unchanged until everything is ready, then merge `first-delivery` once | Closing order in the [schedule](schedule.md#3-closing-steps-for-delivery-1-due-2026-09-30) |
| 2026-09-30 14:49 | Use the author's real name, Alan Pérez, instead of a nickname in every deliverable | Name corrected in all files and in the 13 GitHub issues |

### Delivery 2

| Date and time | Decision | Effect on the project |
|---|---|---|
| 2026-10-27 21:59 | Start delivery 2 without waiting for the client's answer: first the work that does not depend on him; leave field research ready and record why it is pending | [Validation plan §7](../02-research/validation-plan.md#7-delivery-2-status-of-the-activities); replanned [schedule](schedule.md#5-delivery-2--plan-due-2026-10-31) |
| 2026-10-27 21:59 | Create every task as an issue with estimated hours before working on it | T-14…T-28 created at 22:19 |
| 2026-10-27 22:17 | Due date 2026-10-31, video ≤ 5 min; if time runs short, cut the pilot first, then the inspection | Checkpoints and cut order in the schedule |
| 2026-10-27 22:17 | Make question 5 of the message to the client traceable | Q-17, linked to H-17 |
| 2026-10-27 22:17 | Build the prototype as HTML in the repository instead of Figma | [Prototype v1](../../design/prototype/v1/) |
| 2026-10-27 22:17 | Prototype UI text and participant-facing materials in Spanish; the SUS from a published, validated translation | `es/` folders; R42 |
| 2026-10-27 22:17 | Recruit 2 proxy participants; run the pilot only if the mandatory work is done | T-25 conditional (later cancelled) |
| 2026-10-27 22:17 | Inspection with the author as main evaluator and Claude as declared second evaluator; first to be cut | T-22 conditional (later cancelled) |
| 2026-10-27 22:17 | Contribution 100% to the sole member, keeping the AI statement and author-attributable metrics | §0, §1 |
| 2026-10-27 22:17 | Build delivery 2 so it can be reused in delivery 3, without extra work | Change log, versioned prototype, reusable protocol |
| 2026-10-29 22:17 | Keep the prototype as it is (no changes requested); address the user as *tú* | [Logbook 2026-10-29](logbook/2026-10-29.md) |
| 2026-10-29 22:17 | Cancel T-22 (inspection) | Rubric item 3 not done |
| 2026-10-30 16:39 | Enable GitHub Pages and test the prototype on his phone | Online link; phone test |
| 2026-10-30 16:53 | Accept that the keyboard covers the primary button while typing (B-3) | Recorded, not fixed |

## 5. How to recompute

Run in the repository root:

```bash
python3 tools/metrics.py   # §1: commits, types, lines, words, traceable items, co-authorship
python3 tools/trace.py     # traceability views and coverage checks
```

Tasks completed: GitHub → Issues → Milestones → "Delivery 1" and "Delivery 2".
