# Individual contribution metrics

> **Task:** T-12 · **Rubric criterion:** 6 · **Contributor:** Alancete (individual project — 100% of the tasks are assigned to the author)
>
> Metrics are computed from **objective sources**: git history, GitHub issues and the logbook. Snapshot taken at commit `303289b` (2026-09-29 17:56, UTC−6), before the commit that updates this file; it is recomputed with the commands in §3 at the close of each delivery.

## 1. Quantitative metrics

| Metric | Value | Source |
|---|---|---|
| Tasks completed | **11 of 13** (T-11 stays open until the delivery closes; T-13 is the video) | GitHub issues, milestone "Delivery 1" |
| Commits | **35** (13 on 2026-09-28, 22 on 2026-09-29) | `git log` |
| Commits by type | `docs`: 25 · `fix`: 7 · `chore`: 3 | `git log` |
| Lines added / removed | **+1,937 / −224** | `git log --numstat` |
| Artifacts delivered | 12 of 13 deliverables + desk research results and meeting log (see [README §7](../../README.md#7-delivery-1-deliverables)) | Repository |
| Traceable items produced | 18 CR, 3 PRJ, 14 Q, 16 H, 3 P, 7 S, 24 DI, 34 FR, 6 deferred FR, 24 NFR, 8 V, 34 references | Artifacts |
| Hours logged | **≈ 3.9 h** (4 sessions, approximate) | [Logbook](logbook/) |
| Commits co-authored with the AI assistant | 35 of 35 | `Co-Authored-By` lines (see [README §12](../../README.md#12-ai-assistance-statement)) |

### Commits per task

| Task | T-01 | T-02 | T-03 | T-04 | T-05 | T-06 | T-07 | T-08 | T-09 | T-10 | T-11 | T-12 | T-13 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Commits referencing it | 5 | 6 | 4 | 4 | 2 | 3 | 3 | 2 | 4 | 1 | 3 | 1 | 1 |

A commit can reference more than one task.

## 2. Author decisions

Because the AI assistant co-authored every commit, the author's contribution is also recorded as the **decisions that directed the work**. Times come from the working session.

| Date and time | Decision | Effect on the project |
|---|---|---|
| 2026-09-28 19:35 | Work individually with a Lean UX proto-persona approach, without field research in delivery 1; prioritize speed; require that every assumption be labeled as a hypothesis and traced | Shaped all artifacts and labels (`H`, `CR`, `PRJ`) |
| 2026-09-28 22:34 | One branch per delivery (`first-delivery`, …) | Branching convention in the README |
| 2026-09-28 22:45 | All repository content in English | Repository translated; history rewritten once |
| 2026-09-28 23:17 | Use the AI assistant openly and declare it | AI assistance statement (README §12) |
| 2026-09-28 23:31 | Mention open questions in the video and send them to the client after the delivery | Presentation content; Q-01…Q-12 kept open |
| 2026-09-28 23:41 | Provide prior knowledge about connectivity at the FMAT point | Evidence log entry for H-03 |
| 2026-09-28 23:47 | Back every decision with verified, reliable sources | `references.md` (R1–R33) |
| 2026-09-29 00:10 | Deliver the presentation as a video; keep the script out of the repository | `docs/05-presentation/` |
| 2026-09-29 17:39 | Request an independent review of the whole repository against the rubric | Review findings (contradictions, unlabeled assumptions, outdated metrics) |
| 2026-09-29 17:48 | Apply the review's critical and quick fixes; skip optional items; provide the date and setting of the project brief | FR-30…FR-34, H-15, H-16, Q-13, Q-14, S-07, [meeting log](meetings.md) |

## 3. How to recompute

Run in the repository (Git Bash or any shell with `git`):

```bash
# Commits per day
git log --date=short --pretty=format:'%ad' | sort | uniq -c
# Commits per type
git log --pretty=format:'%s' | cut -d'(' -f1 | cut -d':' -f1 | sort | uniq -c
# Commits per task
git log --pretty=format:'%s' | grep -oE 'T-[0-9]+' | sort | uniq -c
# Lines added and removed
git log --numstat --pretty=format:'' | awk '{a+=$1; d+=$2} END {print "+"a" -"d}'
```

Tasks completed: GitHub → Issues → Milestones → "Delivery 1".
