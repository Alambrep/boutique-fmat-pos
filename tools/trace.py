#!/usr/bin/env python3
"""Regenerate the traceability views from the origin columns of every artifact.

Usage (from the repository root):

    python3 tools/trace.py          # rewrite the generated sections and print checks
    python3 tools/trace.py --check  # only print checks; exit code 1 if the files are out of date

It reads:
  - the Origin column of every FR (docs/04-requirements/functional-requirements.md)
  - the Origin column of every NFR (docs/04-requirements/non-functional-requirements.md)
  - the "Origins" line of every scenario (docs/03-user-modeling/scenarios.md)
  - every ID cited inside each proto-persona section (docs/03-user-modeling/proto-personas.md)
  - every ID cited inside each hypothesis row (docs/02-research/hypotheses.md)
  - the sections of the project definition (docs/01-definition/project-definition.md)

and rewrites:
  - traceability-matrix.md, section 1 (matrix) and section 4 (open questions)
  - hypotheses.md, section 5 (where each hypothesis is used)
"""
import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FR = ROOT / "docs/04-requirements/functional-requirements.md"
NFR = ROOT / "docs/04-requirements/non-functional-requirements.md"
SCEN = ROOT / "docs/03-user-modeling/scenarios.md"
PERS = ROOT / "docs/03-user-modeling/proto-personas.md"
HYP = ROOT / "docs/02-research/hypotheses.md"
DEF = ROOT / "docs/01-definition/project-definition.md"
MATRIX = ROOT / "docs/04-requirements/traceability-matrix.md"

ID = r"(CR|PRJ|H|Q|DI)-(\d+)(?:\s*…\s*(?:CR|PRJ|H|Q|DI)-(\d+))?"


def read(p):
    return p.read_text(encoding="utf8")


def expand(text):
    """Return the IDs cited in text, expanding ranges such as CR-10…CR-13."""
    out = []
    for m in re.finditer(ID, text):
        prefix, a, b = m.group(1), int(m.group(2)), m.group(3)
        for i in (range(a, int(b) + 1) if b else [a]):
            out.append(f"{prefix}-{i:02d}")
    return out


def sort_key(x):
    p, n = x.rsplit("-", 1)
    return (p, int(n) if n.isdigit() else 0)


def fmt(items):
    return ", ".join(sorted(items, key=sort_key)) if items else "—"


def rows(text, prefix):
    for line in text.split("\n"):
        m = re.match(rf"\| ({prefix}-[\dD]+) \|", line)
        if m:
            yield m.group(1), [c.strip() for c in line.strip().strip("|").split("|")]


# ---------------------------------------------------------------- collect links
links = collections.defaultdict(lambda: collections.defaultdict(set))  # origin -> kind -> targets
requirement_origin = {}
cited_di = set()

for rid, cols in rows(read(FR), "FR"):
    origin = cols[3] if not rid.startswith("FR-D") else cols[2]
    requirement_origin[rid] = origin
    for o in expand(origin):
        links[o]["FR"].add(rid)
for rid, cols in rows(read(NFR), "NFR"):
    requirement_origin[rid] = cols[-1]
    for o in expand(cols[-1]):
        links[o]["NFR"].add(rid)
for rid, origin in requirement_origin.items():
    cited_di.update(x for x in expand(origin) if x.startswith("DI-"))

scen = read(SCEN)
for m in re.finditer(r"## (S-\d+).*?\*\*Origins:\*\*([^\n]+)", scen, re.S):
    for o in expand(m.group(2)):
        links[o]["S"].add(m.group(1))
all_di = sorted(set(re.findall(r"^- (DI-\d+):", scen, re.M)), key=sort_key)

pers = read(PERS)
sections = re.split(r"(?=^## \d+\. P-\d+)", pers, flags=re.M)
for sec in sections:
    m = re.match(r"## \d+\. (P-\d+)", sec)
    if m:
        body = sec.split("\n## ")[0]
        for o in set(expand(body)):
            links[o]["P"].add(m.group(1))

hyp = read(HYP)
hyp_rows = {}
for rid, cols in rows(hyp, "H"):
    if len(cols) == 8:  # hypothesis definition rows (not the usage table)
        hyp_rows[rid] = cols
        for o in set(expand(" ".join(cols[1:]))):
            if o.startswith("Q-"):
                links[o]["H"].add(rid)

# sections of the project definition that cite each hypothesis
defs = collections.defaultdict(set)
label = None
for line in read(DEF).split("\n"):
    m = re.match(r"^(#{2,4}) (.*)", line)
    if m:
        title = m.group(2)
        n = re.match(r"(\d+(?:\.\d+)?)\.?\s", title)
        if n and m.group(1) in ("##", "###"):
            label = "§" + n.group(1)
        elif title.startswith("Challenge"):
            label = "§4.2 ch. " + title.split()[1]
        elif m.group(1) == "##":
            label = None
        continue
    if label and not line.startswith("| H-"):
        for h in set(re.findall(r"H-\d\d", line)):
            defs[h].add(label)

# ---------------------------------------------------------------- build tables
def ids(prefix, text):
    return sorted(set(re.findall(rf"\b{prefix}-\d\d\b", text)), key=sort_key)


client = read(ROOT / "client/client-requirements.md")
crs = ids("CR", client)
prjs = ids("PRJ", client)
qs = ids("Q", client)
hs = sorted(hyp_rows, key=sort_key)

def q_requirements(q):
    """Requirements that cite the question, plus those reached through a hypothesis it resolves."""
    direct = links[q]["FR"] | links[q]["NFR"]
    parts = [fmt(direct)] if direct else []
    for h in sorted(links[q]["H"], key=sort_key):
        via = (links[h]["FR"] | links[h]["NFR"]) - direct
        if via:
            parts.append(f"{fmt(via)} (via {h})")
    return "; ".join(parts) or "—"


HDR = "| Origin | Proto-personas | Scenarios | Functional requirements | Non-functional requirements |\n|---|---|---|---|---|\n"


def line(i):
    d = links[i]
    return f"| {i} | {fmt(d['P'])} | {fmt(d['S'])} | {fmt(d['FR'])} | {fmt(d['NFR'])} |"


matrix = (
    "## 1. Matrix\n\nGenerated by `tools/trace.py` from the origin columns of each artifact.\n\n"
    + HDR + "\n".join(line(i) for i in crs + prjs)
    + "\n\n### Hypotheses\n\n" + HDR + "\n".join(line(i) for i in hs) + "\n\n"
)
qtable = (
    "## 4. Open questions and what they affect\n\nWhen the client answers a question (V-04), these are the artifacts to revise. Generated by `tools/trace.py`.\n\n"
    "| Question | Hypotheses | Proto-personas | Scenarios | Requirements |\n|---|---|---|---|---|\n"
    + "\n".join(
        f"| {q} | {fmt(links[q]['H'])} | {fmt(links[q]['P'])} | {fmt(links[q]['S'])} | {q_requirements(q)} |"
        for q in qs
    )
    + "\n"
)
usage = "| Hypothesis | Proto-personas | Scenarios | Requirements | Project definition |\n|---|---|---|---|---|\n" + "\n".join(
    f"| {h} | {fmt(links[h]['P'])} | {fmt(links[h]['S'])} | {fmt(links[h]['FR'] | links[h]['NFR'])} | {', '.join(sorted(defs[h])) or '—'} |"
    for h in hs
)

# ---------------------------------------------------------------- write
m_old = read(MATRIX)
a, b = m_old.index("## 1. Matrix"), m_old.index("## 2. Coverage checks")
m_new = m_old[:a] + matrix + m_old[b:]
if "## 4. Open questions" in m_new:
    m_new = m_new[: m_new.index("## 4. Open questions")]
m_new = m_new.rstrip("\n") + "\n\n" + qtable

h_old = read(HYP)
start = h_old.index("| Hypothesis | Proto-personas | Scenarios | Requirements | Project definition |")
end = h_old.index("\n\n", start)
h_new = h_old[:start] + usage + h_old[end:]

# ---------------------------------------------------------------- checks
problems = []
for i in crs + prjs:
    if not links[i]["FR"] and not links[i]["NFR"]:
        problems.append(f"{i} has no FR or NFR")
for rid, origin in requirement_origin.items():
    if not rid.startswith("FR-D") and not re.search(r"CR-|PRJ-|H-", origin):
        problems.append(f"{rid} cites no CR, PRJ or H")
uncited = [d for d in all_di if d not in cited_di]
if uncited:
    problems.append("design implications not cited by any requirement: " + ", ".join(uncited))
only_h = sorted(
    (r for r, o in requirement_origin.items() if not r.startswith("FR-D") and not re.search(r"CR-|PRJ-", o)),
    key=sort_key,
)
impact = sorted(((len(links[h]["FR"] | links[h]["NFR"]), h) for h in hs), reverse=True)

print("Requirements resting only on hypotheses:", ", ".join(only_h) or "none")
print("Requirements per hypothesis:", ", ".join(f"{h} {n}" for n, h in impact if n))
print("Problems:", "; ".join(problems) or "none")

if "--check" in sys.argv:
    stale = m_new != m_old or h_new != h_old
    print("Generated sections are", "OUT OF DATE" if stale else "up to date")
    sys.exit(1 if stale or problems else 0)

MATRIX.write_text(m_new, encoding="utf8")
HYP.write_text(h_new, encoding="utf8")
print("Updated", MATRIX.relative_to(ROOT), "and", HYP.relative_to(ROOT))
