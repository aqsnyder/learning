#!/usr/bin/env python3
"""Track your own progress through the curricula, privately.

Your progress lives in my/, which git ignores. Nothing you tick, note or build there shows up in the shared
repo, and pulling curriculum updates never conflicts with it.

  python tools/progress.py init [--git] [--only pcb,software]
        Create my/ with your own copy of each curriculum's checklist, plus notes/ and projects/ folders.
        --git also makes my/ its own git repository, so you can back it up to a private remote.
  python tools/progress.py status [CURRICULUM ...] [--sections] [--write] [--ascii]
        Progress bars per curriculum (and per section with --sections). --write also saves my/DASHBOARD.md.
  python tools/progress.py next [CURRICULUM]
        The next unfinished section in learning-path order, and what is left in it.
  python tools/progress.py sync
        Pull in checklist changes after you update the repo. Your ticks are kept by item ID. Items that
        disappeared upstream are kept at the end of the file if you had ticked them.
  python tools/progress.py log SECTION HOURS [--difficulty 1-5] [--note "text"]
        Record time spent, e.g.  log pcb/05 3.5 --difficulty 4 --note "PDN impedance finally clicked".
        status shows your hours next to each curriculum.

Tick a box by changing "- [ ]" to "- [x]" in my/progress/<curriculum>.md, in any editor.
A section counts as done when its 🔑 core items, at least two exercises and the first Check Yourself pass
are ticked.
"""
import csv
import datetime
import os
import re
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MY = os.path.join(ROOT, "my")
CURRICULA = ["ml", "math", "physics", "bio", "econ", "philosophy", "pcb", "btc", "software"]
LINE_RE = re.compile(r"^(\s*)- \[( |x|X)\] (.*?)\s*<!-- id:([^ ]+) -->\s*$")
SEC_RE = re.compile(r"^## Section (\d\d) — (.+)$")

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass


def template_path(cur):
    return os.path.join(ROOT, cur, "PROGRESS.md")


def mine_path(cur):
    return os.path.join(MY, "progress", f"{cur}.md")


def read(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def write(p, text):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def parse(text):
    """-> (sections, ticked_ids). sections: list of {nn, title, items: [(id, label, ticked)]}."""
    sections, current, ticked = [], None, set()
    for line in text.splitlines():
        m = SEC_RE.match(line)
        if m:
            current = {"nn": m.group(1), "title": m.group(2).strip(), "items": []}
            sections.append(current)
            continue
        if line.startswith("## "):
            current = {"nn": None, "title": line[3:].strip(), "items": []}
            sections.append(current)
            continue
        m = LINE_RE.match(line)
        if m:
            done = m.group(2) in "xX"
            if done:
                ticked.add(m.group(4))
            if current is not None:
                current["items"].append((m.group(4), m.group(3), done))
    return sections, ticked


YOURS = ("> **Your checklist.** Tick a box by changing `- [ ]` to `- [x]`. After you update the repo, run "
         "`python tools/progress.py sync`; your ticks are kept.")


def personalize(template):
    """Replace the template's 'blank template' note with a note for the learner's own copy."""
    out, replaced = [], False
    for line in template.splitlines():
        if line.startswith(">") and not replaced and any(l.startswith("> **This is a blank template") for l in [line]):
            out.append(YOURS); replaced = True; continue
        if line.startswith(">") and replaced and out and out[-1] == YOURS:
            continue  # drop the rest of the template note
        out.append(line)
    return "\n".join(out) + "\n"


def section_done(sec):
    items = sec["items"]
    core = [i for i in items if i[1].startswith("🔑")]
    ex = [i for i in items if re.search(r"/ex-\d+$", i[0])]
    first_check = [i for i in items if i[0].endswith("/check-1")]
    if not first_check:
        return False
    return all(i[2] for i in core) and sum(1 for i in ex if i[2]) >= min(2, len(ex)) and first_check[0][2]


def bar(frac, width=24, ascii_only=False):
    full = int(round(frac * width))
    if ascii_only:
        return "[" + "#" * full + "-" * (width - full) + "]"
    return "█" * full + "░" * (width - full)


def mine_or_exit(cur):
    p = mine_path(cur)
    if not os.path.exists(p):
        return None
    return parse(read(p))


def hours_logged():
    p = os.path.join(MY, "log.csv")
    out = {}
    if not os.path.exists(p):
        return out
    with open(p, encoding="utf-8") as f:
        for row in csv.DictReader(f):
            cur = (row.get("section") or "").split("/")[0]
            try:
                out[cur] = out.get(cur, 0.0) + float(row.get("hours") or 0)
            except ValueError:
                pass
    return out


# ------------------------------------------------------------------ commands
def cmd_init(args):
    only = None
    if "--only" in args:
        only = [c.strip() for c in args[args.index("--only") + 1].split(",") if c.strip()]
    curs = [c for c in CURRICULA if not only or c in only]
    os.makedirs(os.path.join(MY, "progress"), exist_ok=True)
    os.makedirs(os.path.join(MY, "notes"), exist_ok=True)
    os.makedirs(os.path.join(MY, "projects"), exist_ok=True)
    created = []
    for cur in curs:
        if os.path.exists(mine_path(cur)):
            continue
        write(mine_path(cur), personalize(read(template_path(cur))))
        created.append(cur)
    readme = os.path.join(MY, "README.md")
    if not os.path.exists(readme):
        write(readme, MY_README)
    log = os.path.join(MY, "log.csv")
    if not os.path.exists(log):
        write(log, "date,section,hours,difficulty,note\n")
    for name in ("note.md", "project.md"):
        src = os.path.join(ROOT, "templates", name)
        dst = os.path.join(MY, name.replace(".md", "-template.md"))
        if os.path.exists(src) and not os.path.exists(dst):
            shutil.copyfile(src, dst)
    if "--git" in args and not os.path.exists(os.path.join(MY, ".git")):
        subprocess.run(["git", "init", "-q", MY], check=False)
        print("my/ is now its own git repository. Commit there and push to a private remote to back it up.")
    print(f"my/ is ready: {len(created)} checklist(s) created ({', '.join(created) or 'all already existed'}).")
    print("Next: open my/progress/<curriculum>.md, or run  python tools/progress.py next pcb")


def cmd_sync(args):
    if not os.path.isdir(os.path.join(MY, "progress")):
        sys.exit("No my/ folder yet. Run: python tools/progress.py init")
    stamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    for cur in CURRICULA:
        mp = mine_path(cur)
        if not os.path.exists(mp):
            continue
        mine = read(mp)
        _, ticked = parse(mine)
        own_lines = [l for l in mine.splitlines() if re.match(r"^\s*- \[[ xX]\] ", l) and "<!-- id:" not in l]
        template = personalize(read(template_path(cur)))
        template_ids = set(m.group(4) for m in (LINE_RE.match(l) for l in template.splitlines()) if m)
        out = []
        for line in template.splitlines():
            m = LINE_RE.match(line)
            if m and m.group(4) in ticked:
                line = line.replace("- [ ]", "- [x]", 1)
            out.append(line)
        gone = sorted(t for t in ticked if t not in template_ids)
        if gone:
            out += ["", "## Removed upstream (you had ticked these)", ""]
            old_lines = {m.group(4): m.group(3) for m in (LINE_RE.match(l) for l in mine.splitlines()) if m}
            out += [f"- [x] {old_lines.get(g, g)} <!-- id:{g} -->" for g in gone]
        if own_lines:
            out += ["", "## Your own items", ""] + own_lines
        new = "\n".join(out).rstrip() + "\n"
        if new != mine:
            bdir = os.path.join(MY, ".backup", stamp)
            os.makedirs(bdir, exist_ok=True)
            shutil.copyfile(mp, os.path.join(bdir, f"{cur}.md"))
            write(mp, new)
            print(f"{cur}: updated ({len(ticked)} ticks kept{', ' + str(len(gone)) + ' moved to the end' if gone else ''})")
    print("Sync done. Backups of changed files are in my/.backup/.")


def cmd_status(args):
    ascii_only = "--ascii" in args
    show_sections = "--sections" in args
    want = [a for a in args if not a.startswith("--")]
    hours = hours_logged()
    lines_out = []
    any_found = False
    for cur in CURRICULA:
        if want and cur not in want:
            continue
        parsed = mine_or_exit(cur)
        if parsed is None:
            continue
        any_found = True
        sections, _ = parsed
        secs = [s for s in sections if s["nn"]]
        items = [i for s in sections for i in s["items"]]
        done_items = sum(1 for i in items if i[2])
        done_secs = sum(1 for s in secs if section_done(s))
        frac = done_secs / len(secs) if secs else 0
        h = f" · {hours.get(cur, 0):g} h logged" if hours.get(cur) else ""
        lines_out.append(f"{cur:<11}{bar(frac, ascii_only=ascii_only)} {done_secs:>2}/{len(secs)} sections · "
                         f"{done_items}/{len(items)} items{h}")
        if show_sections:
            for s in secs:
                n = len(s["items"]); d = sum(1 for i in s["items"] if i[2])
                flag = "✓" if section_done(s) else " "
                lines_out.append(f"   {flag} {s['nn']} {bar(d / n if n else 0, 12, ascii_only)} {d:>3}/{n:<3} {s['title']}")
    if not any_found:
        sys.exit("No checklists in my/ yet. Run: python tools/progress.py init")
    print("\n".join(lines_out))
    if "--write" in args:
        stamp = datetime.date.today().isoformat()
        write(os.path.join(MY, "DASHBOARD.md"),
              f"# My progress ({stamp})\n\n```\n" + "\n".join(lines_out) + "\n```\n")
        print("Saved my/DASHBOARD.md")


def cmd_next(args):
    want = [a for a in args if not a.startswith("--")]
    for cur in (want or CURRICULA):
        parsed = mine_or_exit(cur)
        if parsed is None:
            continue
        sections, _ = parsed
        for s in sections:
            if s["nn"] and not section_done(s):
                print(f"{cur} · Section {s['nn']} — {s['title']}  ({cur}/{s['nn']}-…/README.md)")
                left = [i for i in s["items"] if not i[2]]
                core = [i for i in left if i[1].startswith("🔑")]
                ex = [i for i in left if re.search(r"/ex-\d+$", i[0])]
                rest = [i for i in left if i not in core and i not in ex]
                for title, group in (("Core path", core), ("Exercises (do at least two)", ex), ("Then", rest[:4])):
                    if group:
                        print(f"  {title}:")
                        for i in group:
                            print(f"    - {i[1]}")
                if want:
                    return
                break
    if not any(os.path.exists(mine_path(c)) for c in CURRICULA):
        sys.exit("No checklists in my/ yet. Run: python tools/progress.py init")


def cmd_log(args):
    if len(args) < 2:
        sys.exit("Usage: python tools/progress.py log SECTION HOURS [--difficulty 1-5] [--note \"text\"]")
    section, hours = args[0], args[1]
    if not re.match(r"^[a-z]+/\d\d$", section):
        sys.exit("SECTION looks like pcb/05")
    try:
        float(hours)
    except ValueError:
        sys.exit("HOURS must be a number, e.g. 2.5")
    diff = args[args.index("--difficulty") + 1] if "--difficulty" in args else ""
    note = args[args.index("--note") + 1] if "--note" in args else ""
    p = os.path.join(MY, "log.csv")
    if not os.path.exists(p):
        write(p, "date,section,hours,difficulty,note\n")
    with open(p, "a", encoding="utf-8", newline="") as f:
        csv.writer(f).writerow([datetime.date.today().isoformat(), section, hours, diff, note])
    print(f"Logged {hours} h on {section}.")


MY_README = """# my/: your private learning space

Git ignores this whole folder, so nothing here is shared when you push the learning repo.

- `progress/<curriculum>.md`: your checklists. Tick a box by changing `- [ ]` to `- [x]`.
- `notes/<curriculum>/<NN>-<slug>.md`: one page per section, in your own words (`note-template.md` shows the shape).
- `projects/<curriculum>/<NN>-<name>/`: exercise and mini-project work (`project-template.md`).
- `log.csv`: time and difficulty per session, written by `python tools/progress.py log`.

Run `python tools/progress.py status` for progress bars, and `python tools/progress.py sync` after you pull
curriculum updates. To back this folder up, make it its own repository (`python tools/progress.py init --git`
does that) and push it to a private remote.
"""

COMMANDS = {"init": cmd_init, "sync": cmd_sync, "status": cmd_status, "next": cmd_next, "log": cmd_log}

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(0 if len(sys.argv) < 2 else 1)
    COMMANDS[sys.argv[1]](sys.argv[2:])
