#!/usr/bin/env python3
"""List the requirements whose text changed between a git reference and the working tree.

Usage (from the repository root):

    python3 tools/req_diff.py delivery-1      # FR and NFR changed since tag delivery-1

Prints a Markdown table (ID, statement before, statement after) for every FR and NFR whose
"The system shall…" / "Requirement" column changed, and lists added or removed IDs. Used to
build docs/04-requirements/changes.md; the type and reason of each change are written there by hand.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = {"FR": ("docs/04-requirements/functional-requirements.md", 1),
         "NFR": ("docs/04-requirements/non-functional-requirements.md", 2)}


def statements(text, prefix, col):
    out = {}
    for line in text.split("\n"):
        m = re.match(rf"\| ({prefix}-[\dD]+) \|", line)
        if m:
            cols = [c.strip() for c in line.strip().strip("|").split("|")]
            out[m.group(1)] = cols[col]
    return out


ref = sys.argv[1] if len(sys.argv) > 1 else "delivery-1"
print("| ID | Before (" + ref + ") | After |\n|---|---|---|")
added, removed = [], []
for prefix, (path, col) in FILES.items():
    old = statements(subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=ROOT, text=True), prefix, col)
    new = statements((ROOT / path).read_text(encoding="utf8"), prefix, col)
    for rid in sorted(set(old) | set(new), key=lambda x: (x.split("-")[0], int(re.sub(r"\D", "", x.split("-")[1]) or 0))):
        if rid not in new:
            removed.append(rid)
        elif rid not in old:
            added.append(rid)
        elif old[rid] != new[rid]:
            print(f"| {rid} | {old[rid]} | {new[rid]} |")
print("\nAdded:", ", ".join(added) or "none", "· Removed:", ", ".join(removed) or "none")
