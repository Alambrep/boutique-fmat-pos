#!/usr/bin/env python3
"""Compute the quantitative contribution metrics from the git history and the artifacts.

Usage (from the repository root):

    python3 tools/metrics.py

Prints a Markdown table that is pasted into docs/00-management/contribution-metrics.md §1
at the close of each delivery. Nothing is estimated: every value comes from git or from
counting identifiers in the artifacts.
"""
import collections
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def git(*args):
    return subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True,
                          env={"TZ": "America/Mexico_City", "PATH": "/usr/bin:/bin:/usr/local/bin"}).stdout


def read(rel):
    return (ROOT / rel).read_text(encoding="utf8")


head = git("rev-parse", "--short", "HEAD").strip()
when = git("log", "-1", "--date=format-local:%Y-%m-%d %H:%M", "--format=%ad").strip()
subjects = git("log", "--format=%s").strip().split("\n")
days = collections.Counter(git("log", "--date=format-local:%Y-%m-%d", "--format=%ad").split())
types = collections.Counter(re.split(r"[(:]", s, 1)[0] for s in subjects)
tasks = collections.Counter(t for s in subjects for t in set(re.findall(r"T-\d\d", s)))
coauthored = git("log", "--format=%B").count("Co-Authored-By: Claude")
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
]

total = len(subjects)
print(f"Snapshot: commit `{head}` ({when}, UTC−6)\n")
print("| Metric | Value |\n|---|---|")
print(f"| Commits | **{total}** (" + ", ".join(f"{n} on {d}" for d, n in sorted(days.items())) + ") |")
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
