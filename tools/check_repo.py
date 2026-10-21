#!/usr/bin/env python3
"""Offline checks for the learning repo (no network, no dependencies beyond Python 3.11+).

Usage:  python tools/check_repo.py            # structural checks; exit 1 on problems
        python tools/check_repo.py --strict   # also fail on incomplete resource data (see "Data completeness")
        python tools/check_repo.py --urls     # also print every external URL (input for a link checker)
        python tools/check_repo.py --only pcb,btc/05   # report only problems in these paths

Problems (always fail):
  1. Relative links and image paths resolve.
  2. Markdown tables have a consistent column count.
  3. Every numbered section README has Prerequisites, the Learning Objectives, Resources, Suggested Order,
     Practice and Check Yourself headings, and a mini-project.
  4. Tier lists: at most 3 items marked core (🔑) per section, and a "**Core path (🔑):**" line in the
     Suggested Order naming exactly that many items.
  5. Every resources.toml is valid and everything generated from the data is current
     (python tools/build.py --check; if it fails, run python tools/build.py).
  6. Nothing personal is committed: no my/ folder, and no ticked boxes in the PROGRESS templates.

Data completeness (reported; --strict fails on it): every resource has a link, author(s) or publisher, a
description and a verified date; dated kinds of resource (books, papers, articles, reports, standards,
app notes, lectures, videos and courses) also have a year; and no row is a bare concept without a source.
"""
import os
import re
import subprocess
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build  # noqa: E402  (shares the data loader and the curriculum list)

ROOT = build.ROOT
CURRICULA = list(build.CURRICULA)
SECTION_RE = build.SECTION_RE
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(((?:[^()\s]|\([^()\s]*\))+)\)|!\[[^\]]*\]\(((?:[^()\s]|\([^()\s]*\))+)\)|(?:src|href)=\"([^\"]+)\"")
URL_RE = re.compile(r"https?://(?:[^\s()<>\]\"`|]|\([^\s()<>\]\"`|]*\))+")  # allows balanced (...) as in DOIs

problems = []
urls = set()
YEAR_REQUIRED = {"book", "paper", "article", "report", "standard", "app-note", "lecture", "video", "course"}


def md_files():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "node_modules", "my")]
        for f in fn:
            if f.endswith(".md"):
                yield os.path.join(dp, f)


def strip_code(line):
    return re.sub(r"`[^`]*`", lambda m: "x" * len(m.group(0)), line)


def split_row(line):
    s = strip_code(line).strip()
    s = s.replace("\\|", "xx")
    if s.startswith("|"): s = s[1:]
    if s.endswith("|"): s = s[:-1]
    return s.split("|")


# 1-2: links and tables in every markdown file
for path in md_files():
    rel = os.path.relpath(path, ROOT)
    lines = open(path, encoding="utf-8").read().split("\n")
    fence = False
    table_cols = None; table_start = None
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            fence = not fence; continue
        if fence: continue
        scan = strip_code(line) if "`" in line else line
        for m in LINK_RE.finditer(scan):
            target = next(g for g in m.groups() if g)
            if re.match(r"^https?:", target):
                urls.add(target); continue
            if re.match(r"^(mailto:|#)", target): continue
            target = target.split("#")[0]
            if not target: continue
            full = os.path.normpath(os.path.join(os.path.dirname(path), target))
            if not os.path.exists(full):
                problems.append(f"{rel}:{i}: broken relative link -> {target}")
        for u in URL_RE.findall(LINK_RE.sub(" ", scan)):
            urls.add(u.rstrip(".,;:*"))
        is_row = line.strip().startswith("|") and line.strip().count("|") >= 2
        if is_row:
            cols = len(split_row(line))
            if table_cols is None:
                table_cols, table_start = cols, i
            elif cols != table_cols:
                problems.append(f"{rel}:{i}: table row has {cols} cells, header (line {table_start}) has {table_cols}")
        else:
            table_cols = None

# 3-4: section anatomy and tier lists
completeness = {}
for cur in CURRICULA:
    cdir = os.path.join(ROOT, cur)
    gaps = {"no link": 0, "no author": 0, "no year": 0, "no description": 0, "not verified": 0, "concept row": 0, "items": 0}
    for sec in sorted(d for d in os.listdir(cdir) if SECTION_RE.match(d)):
        rel = f"{cur}/{sec}/README.md"
        text = open(os.path.join(cdir, sec, "README.md"), encoding="utf-8").read()
        if not re.search(r"^(## Prerequisites|\*\*Prerequisites:\*\*)", text, re.M):
            problems.append(f"{rel}: missing Prerequisites (a '## Prerequisites' heading or a '**Prerequisites:**' line)")
        for heading in ("## 🎯 Learning Objectives", "## Resources", "## Suggested Order", "## 🛠️ Practice", "## ✅ Check Yourself"):
            if not re.search(rf"^{re.escape(heading)}", text, re.M):  # line start: an H3 slip fails
                problems.append(f"{rel}: missing '{heading}'")
        if "**🏗️ Mini-project" not in text:
            problems.append(f"{rel}: missing '**🏗️ Mini-project' line")
        data = build.load_section_data(cur, sec)
        items = list(build.items_of(data))
        core = [it for it in items if set(it.get("marks", [])) & {"core", "masterwork"}]
        if len(core) > 3:
            problems.append(f"{cur}/{sec}/resources.toml: {len(core)} items marked core (tier lists allow at most 3)")
        m = re.search(r"^\*\*Core path \(🔑\):\*\*\s*(.+)$", text, re.M)
        if not m:
            problems.append(f"{rel}: missing '**Core path (🔑):**' line in Suggested Order")
        else:
            named = [x for x in re.split(r"\s+→\s+", m.group(1)) if x.strip()]
            if len(named) != len(core):
                problems.append(f"{rel}: Core path line names {len(named)} item(s) but {len(core)} item(s) are marked core")
        for it in items:
            gaps["items"] += 1
            if not it.get("url"): gaps["no link"] += 1
            if not it.get("authors"): gaps["no author"] += 1
            if not it.get("year") and it.get("type") in YEAR_REQUIRED: gaps["no year"] += 1
            if not it.get("description"): gaps["no description"] += 1
            if not it.get("verified"): gaps["not verified"] += 1
            if it.get("type") == "concept": gaps["concept row"] += 1
    completeness[cur] = gaps

# 5: data valid and generated content current
r = subprocess.run([sys.executable, os.path.join(ROOT, "tools", "build.py"), "--check"], capture_output=True, text=True)
if r.returncode != 0:
    for line in r.stderr.splitlines():
        if line.strip():
            problems.append(line.strip())

# 6: nothing personal committed
tracked = subprocess.run(["git", "-C", ROOT, "ls-files", "my"], capture_output=True, text=True).stdout.strip()
if tracked:
    problems.append("my/ is committed: it holds personal progress and must stay untracked (see .gitignore)")
for cur in CURRICULA:
    p = os.path.join(ROOT, cur, "PROGRESS.md")
    if os.path.exists(p) and re.search(r"^\s*- \[[xX]\]", open(p, encoding="utf-8").read(), re.M):
        problems.append(f"{cur}/PROGRESS.md: has ticked boxes; it is a template (track your own progress in my/)")

# report
strict = "--strict" in sys.argv
print("Data completeness (items missing each field):", file=sys.stderr)
cols = ["items", "no link", "no author", "no year", "no description", "not verified", "concept row"]
print("  " + "curriculum".ljust(11) + "".join(c.rjust(15) for c in cols), file=sys.stderr)
for cur, g in completeness.items():
    print("  " + cur.ljust(11) + "".join(str(g[c]).rjust(15) for c in cols), file=sys.stderr)
    if strict:
        for c in cols[1:]:
            if g[c]:
                problems.append(f"{cur}: {g[c]} item(s) with '{c}' (strict mode)")

if "--urls" in sys.argv:
    print("\n".join(sorted(urls)))
if "--only" in sys.argv:
    prefixes = [x.strip().strip("/") for x in sys.argv[sys.argv.index("--only") + 1].split(",") if x.strip()]
    def in_scope(p):
        path = p.split(":")[0].strip()
        return any(path == x or path.startswith(x + "/") or path.startswith(x + "-") for x in prefixes)
    problems = [p for p in problems if in_scope(p) or not re.match(r"^[\w./-]+", p)]
print(f"{len(problems)} problem(s); {len(urls)} external URLs found", file=sys.stderr)
for p in problems:
    print("  " + p, file=sys.stderr)
sys.exit(1 if problems else 0)
