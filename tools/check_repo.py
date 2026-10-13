#!/usr/bin/env python3
"""Structural checks for the learning repo (no network, no dependencies).

Usage:  python tools/check_repo.py            # run all checks, exit 1 on problems
        python tools/check_repo.py --urls     # also print every external URL (for a link checker)

Checks:
  1. Relative links and image paths resolve.
  2. Markdown tables have a consistent column count.
  3. Every numbered section README has Learning Objectives, Practice and Check Yourself H2 headings and a mini-project.
  4. Every numbered section has a "## Section NN" block in PROGRESS.md with the three practice checkboxes.
  5. Every numbered section appears in its curriculum README's learning path.
  6. Tier lists: at most 3 resource rows marked 🔑 per section (legend rows excluded), and a
     "**Core path (🔑):**" line at the top of the section's Suggested Order.
"""
import os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CURRICULA = ["ml", "math", "physics", "bio", "econ", "philosophy", "pcb", "btc", "software"]
SECTION_RE = re.compile(r"^(\d\d)-[a-z0-9-]+$")
LINK_RE = re.compile(r"(?<!\!)\[[^\]]*\]\(((?:[^()\s]|\([^()\s]*\))+)\)|!\[[^\]]*\]\(((?:[^()\s]|\([^()\s]*\))+)\)|(?:src|href)=\"([^\"]+)\"")
URL_RE = re.compile(r"https?://(?:[^\s()<>\]\"`|]|\([^\s()<>\]\"`|]*\))+")  # allows balanced (...) as in DOIs

problems = []
urls = set()

def md_files():
    for dp, dn, fn in os.walk(ROOT):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
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

for path in md_files():
    rel = os.path.relpath(path, ROOT)
    lines = open(path, encoding="utf-8").read().split("\n")
    fence = False
    table_cols = None; table_start = None
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            fence = not fence; continue
        if fence: continue
        # links (inline code is masked: URLs there are templates like .../<DOI>)
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
        # tables
        is_row = line.strip().startswith("|") and line.strip().count("|") >= 2
        if is_row:
            cols = len(split_row(line))
            if table_cols is None:
                table_cols, table_start = cols, i
            elif cols != table_cols:
                problems.append(f"{rel}:{i}: table row has {cols} cells, header (line {table_start}) has {table_cols}")
        else:
            table_cols = None

for cur in CURRICULA:
    cdir = os.path.join(ROOT, cur)
    if not os.path.isdir(cdir):
        problems.append(f"{cur}/: curriculum directory missing"); continue
    def read(p):
        try:
            return open(p, encoding="utf-8").read()
        except FileNotFoundError:
            problems.append(f"{os.path.relpath(p, ROOT)}: file missing"); return None
    sections = sorted(d for d in os.listdir(cdir) if SECTION_RE.match(d))
    progress = read(os.path.join(cdir, "PROGRESS.md")) or ""
    readme = read(os.path.join(cdir, "README.md")) or ""
    for sec in sections:
        nn = sec[:2]
        text = read(os.path.join(cdir, sec, "README.md"))
        if text is not None:
            for heading in ("## 🎯 Learning Objectives", "## 🛠️ Practice", "## ✅ Check Yourself"):
                if not re.search(rf"^{re.escape(heading)}", text, re.M):  # line start: an H3 slip fails
                    problems.append(f"{cur}/{sec}/README.md: missing '{heading}'")
            if "**🏗️ Mini-project" not in text:
                problems.append(f"{cur}/{sec}/README.md: missing '**🏗️ Mini-project' line")
            body = text.split("## 🛠️ Practice")[0]
            keyed = [l for l in body.splitlines() if l.startswith("|") and "🔑" in l
                     and not re.match(r"^\|\s*🔑+\s*\|\s*\**(must|core|key|essential|foundational)", l, re.I)]
            if len(keyed) > 3:
                problems.append(f"{cur}/{sec}/README.md: {len(keyed)} rows marked 🔑 (tier lists allow at most 3)")
            if "**Core path (🔑):**" not in text:
                problems.append(f"{cur}/{sec}/README.md: missing '**Core path (🔑):**' line in Suggested Order")
        m = re.search(rf"^## Section {nn} .*?(?=^## |\Z)", progress, re.M | re.S)
        if not m:
            problems.append(f"{cur}/PROGRESS.md: no '## Section {nn}' block")
        else:
            block = m.group(0)
            for marker in ("🛠️ Practice exercises", "🏗️ Mini-project", "✅ Check Yourself"):
                if marker not in block:
                    problems.append(f"{cur}/PROGRESS.md: Section {nn} lacks '{marker}' checkbox")
        if not re.search(rf"Section {nn}\b", readme):
            problems.append(f"{cur}/README.md: learning path does not mention Section {nn}")

if "--urls" in sys.argv:
    print("\n".join(sorted(urls)))
print(f"{len(problems)} problem(s); {len(urls)} external URLs found", file=sys.stderr)
for p in problems:
    print("  " + p, file=sys.stderr)
sys.exit(1 if problems else 0)
