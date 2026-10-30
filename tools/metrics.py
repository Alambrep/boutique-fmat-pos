#!/usr/bin/env python3
"""Compute the quantitative contribution metrics from the git history and the artifacts.

Usage (from the repository root):

    python3 tools/metrics.py

Prints Markdown tables that are pasted into docs/00-management/contribution-metrics.md
at the close of each delivery. Nothing is estimated here: every value comes from git, from
counting identifiers in the artifacts, or from the task log (whose estimated hours were set
in each issue before the work started, and whose actual hours come from the logbook).

Merge commits are counted apart and excluded from the counts by type and by task.
"""
import collections
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
D1_END = "76fe116"  # last commit of delivery 1 on main (merge of PR #15)


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          env={"TZ": "America/Mexico_City", "PATH": "/usr/bin:/bin:/usr/local/bin"}).stdout


def read(rel):
    return (ROOT / rel).read_text(encoding="utf8")


head = git("rev-parse", "--short", "HEAD").strip()
when = git("log", "-1", "--date=format-local:%Y-%m-%d %H:%M", "--format=%ad").strip()
subjects = git("log", "--no-merges", "--format=%s").strip().split("\n")
merges = len(git("log", "--merges", "--format=%h").split())
days = collections.Counter(git("log", "--no-merges", "--date=format-local:%Y-%m-%d", "--format=%ad").split())
types = collections.Counter(re.split(r"[(:]", s, maxsplit=1)[0] for s in subjects)
per_delivery = {"Delivery 1": len(git("log", "--no-merges", "--format=%h", D1_END).split()),
                "Delivery 2": len(git("log", "--no-merges", "--format=%h", f"{D1_END}..HEAD").split())}
tasks = collections.Counter(t for s in subjects for t in set(re.findall(r"T-\d\d", s)))
coauthored = git("log", "--no-merges", "--format=%B").count("Co-Authored-By: Claude")
added = removed = 0
for line in git("log", "--numstat", "--format=").split("\n"):
    parts = line.split("\t")
    if len(parts) == 3 and parts[0].isdigit():
        added += int(parts[0])
        removed += int(parts[1])

docs = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
words = sum(len(p.read_text(encoding="utf8").split()) for p in docs)


def count(pattern, rel):
    return len(set(re.findall(pattern, read(rel))))


items = [
    ("CR", count(r"\| (CR-\d\d) \|", "client/client-requirements.md")),
    ("PRJ", count(r"\| (PRJ-\d\d) \|", "client/client-requirements.md")),
    ("Q", count(r"\| (Q-\d\d) \|", "client/client-requirements.md")),
    ("H", len(set(re.findall(r"^\| (H-\d\d) \|", read("docs/02-research/hypotheses.md"), re.M)))),
    ("P", len(set(re.findall(r"^## \d+\. (P-\d\d)", read("docs/03-user-modeling/proto-personas.md"), re.M)))),
    ("S", len(set(re.findall(r"^## (S-\d\d)", read("docs/03-user-modeling/scenarios.md"), re.M)))),
    ("DI", len(set(re.findall(r"^- (DI-\d\d):", read("docs/03-user-modeling/scenarios.md"), re.M)))),
    ("FR", len(set(re.findall(r"^\| (FR-\d\d) \|", read("docs/04-requirements/functional-requirements.md"), re.M)))),
    ("deferred FR", len(set(re.findall(r"^\| (FR-D\d) \|", read("docs/04-requirements/functional-requirements.md"), re.M)))),
    ("NFR", len(set(re.findall(r"^\| (NFR-\d\d) \|", read("docs/04-requirements/non-functional-requirements.md"), re.M)))),
    ("V", len(set(re.findall(r"^\| (V-\d\d) \|", read("docs/02-research/validation-plan.md"), re.M)))),
    ("references", len(set(re.findall(r"^\| (R\d+) \|", read("docs/references.md"), re.M)))),
    ("G", len(set(re.findall(r"^\| (G-\d\d) \|", read("design/guidelines.md"), re.M)))),
    ("SCR", len(set(re.findall(r"^\| (SCR-\d\d) \|", read("design/screens.md"), re.M)))),
    ("IX", len(set(re.findall(r"^\| (IX-\d\d) \|", read("design/interaction-design.md"), re.M)))),
]

# ---------------------------------------------------------------- task log, delivery 2
log = read("docs/00-management/task-log.md").split("## Delivery 2")[1]
d2 = []
for line in log.split("\n"):
    if re.match(r"\| T-\d\d \|", line):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        hours = lambda t: float(m.group(1)) if (m := re.search(r"(\d+(?:\.\d+)?)", t)) else 0.0
        status = re.match(r"\**(Completed|In progress|Planned|Cancelled)", c[4]).group(1)
        d2.append({"id": c[0], "owner": c[2], "status": status, "est": hours(c[5]), "actual": hours(c[6])})
st = collections.Counter(t["status"] for t in d2)
planned = [t for t in d2 if t["status"] != "Cancelled"]
done = [t for t in d2 if t["status"] == "Completed"]
est_done = sum(t["est"] for t in done)
est_planned = sum(t["est"] for t in planned)
owners = sorted({t["owner"] for t in d2})
d1_rows = [[x.strip() for x in l.strip().strip("|").split("|")] for l in read("docs/00-management/task-log.md").split("## Delivery 2")[0].split("\n") if re.match(r"\| T-\d\d \|", l)]

total = len(subjects)
print(f"Snapshot: commit `{head}` ({when}, UTC−6)\n")
print("| Metric | Value |\n|---|---|")
print(f"| Commits (without merges) | **{total}** (" + ", ".join(f"{k}: {n}" for k, n in per_delivery.items()) + "); merge commits: " + str(merges) + " |")
print("| Commits per day | " + ", ".join(f"{n} on {d}" for d, n in sorted(days.items())) + " |")
print("| Commits by type | " + " · ".join(f"`{t}`: {n}" for t, n in types.most_common()) + " |")
print(f"| Lines added / removed | **+{added:,} / −{removed:,}** |")
print(f"| Words in Markdown documents | ≈ {round(words, -2):,} |")
print("| Traceable items | " + ", ".join(f"{n} {k}" for k, n in items) + " |")
print(f"| Commits co-authored with the AI assistant | {coauthored} of {total} |")
print(f"| Rework commits (`fix`) | {types.get('fix', 0)} of {total} |")
print("\nCommits per task:\n")
ts = sorted(tasks)
print("| Task | " + " | ".join(ts) + " |\n|---|" + "---|" * len(ts))
print("| Commits referencing it | " + " | ".join(str(tasks[t]) for t in ts) + " |")

print("\nDelivery 2 tasks (from the task log):\n")
print("| Metric | Value |\n|---|---|")
print("| Tasks | " + str(len(d2)) + " (" + ", ".join(f"{n} {k.lower()}" for k, n in st.most_common()) + ") |")
print(f"| Progress | {est_done:.1f} of {est_planned:.1f} estimated hours completed (**{100 * est_done / est_planned:.0f}%**), excluding cancelled tasks |")
print(f"| Actual hours logged in delivery 2 tasks | ≈ {sum(t['actual'] for t in d2):.1f} h |")
print("\nIndividual contribution per delivery (share of the estimated hours of completed tasks owned by each member; delivery 1 by number of tasks, because it had no estimates):\n")
print("| Member | Delivery 1 | Delivery 2 | Delivery 3 |\n|---|---|---|---|")
for o in owners:
    mine = sum(t["est"] for t in done if t["owner"] == o)
    d1_mine = sum(1 for r in d1_rows if r[2] == o)
    print(f"| {o} | {100 * d1_mine / len(d1_rows):.0f}% ({d1_mine} of {len(d1_rows)} tasks) | {100 * mine / est_done:.0f}% ({mine:.1f} of {est_done:.1f} h) | — |")

