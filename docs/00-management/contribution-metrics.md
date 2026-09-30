# Individual contribution metrics

> **Task:** T-12 · **Rubric criterion:** 6 · **Contributor:** Alan Pérez (individual project — 100% of the tasks are assigned to the author)
>
> Metrics are computed from **objective sources**: git history, GitHub issues and the logbook. §1 is produced by [`tools/metrics.py`](../../tools/metrics.py); snapshot at commit `ac12d66` (2026-09-29 19:06, UTC−6). Figures exclude the commit that updates this file; they are recomputed at the close of each delivery.

## 1. Quantitative metrics

| Metric | Value |
|---|---|
| Tasks completed | **11 of 13** (T-11 stays open until the delivery closes; T-13 is the video) |
| Commits | **61** (13 on 2026-09-28, 48 on 2026-09-29) |
| Commits by type | `docs`: 38 · `fix`: 18 · `chore`: 4 · `feat`: 1 |
| Lines added / removed | **+2,652 / −553** |
| Words in Markdown documents | ≈ 24,900 |
| Traceable items | 18 CR, 3 PRJ, 16 Q, 17 H, 3 P, 8 S, 32 DI, 39 FR, 6 deferred FR, 28 NFR, 8 V, 34 references |
| Commits co-authored with the AI assistant | 61 of 61 |
| Rework commits (`fix`) | 18 of 61 |
| Hours logged | **≈ 4.7 h** (4 sessions, approximate: 2.3 h on 2026-09-28, 2.4 h on 2026-09-29 so far; see the [logbook](logbook/)) |

### Commits per task

| Task | T-01 | T-02 | T-03 | T-04 | T-05 | T-06 | T-07 | T-08 | T-09 | T-10 | T-11 | T-12 | T-13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Commits referencing it | 8 | 7 | 7 | 6 | 4 | 6 | 6 | 6 | 7 | 2 | 5 | 3 | 1 |

A commit can reference more than one task.

**How to read these figures.** About five hours of logged work produced roughly 25,000 words of documentation because drafting was done with an AI assistant, as declared in [README §12](../../README.md#12-ai-assistance-statement). The volume metrics above therefore describe the *project's* output, not the author's typing. The author's individual contribution is measured in §2 and documented session by session in the logbook. The `fix` commits are rework after reviews, which is part of the iterative process described in README §3.

## 2. Author-attributable metrics

Commits and lines measure the joint output of the author and the AI assistant (every commit is co-authored). The counts below measure what only the author can do: direct the work, supply facts that no document contains, and ask for the work to be reviewed. They show direction and oversight, not authorship of the text.

| Metric | Value | How it is counted |
|---|---|---|
| Direction decisions | **14** | Rows of the decisions table (§3) |
| Facts supplied by the author that no document contained | **5**: the date and setting of the project brief (2026-08-14, in person); location and connectivity of the boutique's point at FMAT; the original client document and rubric; the presentation format (video); the delivery date (2026-09-30) | Recorded in the [meeting log](meetings.md), the [hypotheses evidence log](../02-research/hypotheses.md#6-evidence-log), `client/originals/`, `docs/05-presentation/` and the [schedule](schedule.md) |
| Reviews of the whole repository requested by the author | **2** (2026-09-29 17:39 and 18:33, both by Claude in separate conversations; the second in nine steps) | [Logbook 2026-09-29](logbook/2026-09-29.md) |
| Review proposals not applied or adapted after checking them against the files and sources | **12** | Listed with their reasons in the [logbook](logbook/2026-09-29.md); the checks were done with the AI assistant and the author received a summary after each step |

## 3. Author decisions

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

## 4. How to recompute

Run in the repository root:

```bash
python3 tools/metrics.py   # §1: commits, types, lines, words, traceable items, co-authorship
python3 tools/trace.py     # traceability views and coverage checks
```

Tasks completed: GitHub → Issues → Milestones → "Delivery 1".
