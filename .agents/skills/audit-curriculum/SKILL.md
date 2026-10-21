---
name: audit-curriculum
description: Audit and repair a curriculum in this learning repo (or all nine) — re-verify citations and links and refresh their verified dates, fix structure with tools/check_repo.py, keep every section's learning blocks complete, and write a dated review under reviews/. Use for the quarterly quality pass, or when building a new section or curriculum.
---

# Audit Curriculum

A repo-wide quality pass. The `update-curriculum` skill adds new material. This skill checks that everything already here is **true, reachable, and teachable**.

## When to use

- Quarterly (the repo's scheduled audit), or after several `update-curriculum` runs
- Before creating a new section or curriculum
- When a citation looks wrong or links have started to rot

## Section anatomy (every numbered section README)

1. `# Title`
2. Why this section matters: a `## Why This Section Matters` heading (older sections use an opening paragraph under the title)
3. Prerequisites: a `## Prerequisites` heading (older sections use a bold **Prerequisites:** line), with relative links to directories that exist; link other curricula as `../../<curriculum>/<section>/`
4. `## 🎯 Learning Objectives`: 3–5 observable, verb-led outcomes (derive, implement, design, estimate, debug, critique)
5. `## Resources`, a block generated from the section's `resources.toml` (never edit the block by hand; see `tools/README.md`). At most 3 items are marked core (🔑), and ⭐ only marks the curriculum's named list.
6. `## Suggested Order`, which should cover every resource. It opens with a `**Core path (🔑):** A → B → C` line that names the section's 🔑 items in the order the list uses them.
7. `---` then `## 🛠️ Practice`: 3–5 exercises, each with inputs → deliverable → how you know it's right, plus an honest time estimate and the resources it uses. Then `**🏗️ Mini-project — <Name>:**` with a deliverable (learners keep theirs in `my/projects/<curriculum>/…`) and a success criterion.
8. `## ✅ Check Yourself`: 5–8 retrieval questions without answers. Mix recall, explanation, estimation, a misconception probe, and "explain it to a smart friend".

`PROGRESS.md` is generated from the data and the README (one line per resource, per exercise, for the mini-project, three Check Yourself passes and a note), so it never needs hand edits. Exercise names come from the bold names in the Practice list, and the mini-project name from its bold line.

New sections are appended at the next free number. Never renumber existing sections. The curriculum README's learning-path table lists sections in recommended order, and its *When* column says where an appended section belongs ("After 05").

## Workflow

1. **Structure.** Run `python tools/build.py`, then `python tools/check_repo.py`, and fix every reported problem: broken relative links, ragged tables, missing learning blocks, invalid data, too many 🔑, or a Core path line that doesn't match. A new section shows up in its learning path as "(place me)": move its row to where it belongs and write its *When*. Read the data-completeness table it prints; `--strict` must pass at the end of the audit.
2. **Citations.** Re-check every item whose `verified` date is more than a year old, or missing, plus anything the monthly link check flagged (open GitHub issues labelled `links`). Check each URL against the item's title, authors and year:
   - arXiv: fetch `https://arxiv.org/abs/<id>` (the export API is blocked by robots)
   - DOI: `https://api.crossref.org/works/<DOI>` (DataCite fallback: `https://api.datacite.org/dois/<DOI>`)
   - YouTube: `https://www.youtube.com/oembed?url=<url>&format=json`
   - Anything else: fetch the page itself

   Record each result as ok / mismatch / broken / moved / unverifiable. Batch the work, and stop when web budgets run out rather than guessing.
   - Pace page fetches, about 10–20 s apart per worker.
   - After an HTTP 429, wait a few minutes, and don't refetch that page in the same run.
   - A YouTube oEmbed 4xx is inconclusive, because live playlists return it too.
   - Check GitHub links from a machine that has GitHub access.
   - Write the results to `reviews/<run>/link-audit.md`. The 2026-10 run is the template.
   - For each item you confirm, set `verified` to today's date in its `resources.toml`.
3. **Content.** Score each section 1–5 on coverage, accuracy, currency, sequencing, and focus. Check that every 🛠️ exercise and ✅ question uses a resource listed in its own section, or names the section that lists it. Label speculative or advocacy material honestly.
4. **Repair.** Fix verified errors in place, and add only verified resources (see the rules below). When a resource changes, update its Suggested Order entry and any exercise or question that cites it. Never change an item's `id`.
5. **Report.** Write `reviews/<YYYY-MM>-<name>/<curriculum>.md` containing: verdict, scorecard, section-by-section notes, a corrections table with evidence URLs, additions, proposals, cut candidates, and the top 5 priorities.
6. **Re-check.** `python tools/build.py`, then `python tools/check_repo.py --strict`, must report 0 problems. Then summarize what changed and what is still unverified.

## Rules (shared with the update-curriculum skill)

1. **Open every link before adding it.** Confirm the exact title, author order, year, and edition. Never write a URL or an author list from memory.
2. **Cite people, not organizations,** whenever a work lists authors.
3. **When in doubt, leave it out.** Put doubtful candidates in the report, not in the curriculum.
4. **Correct, don't just append.** Fix errors in place. Mark superseded or dead resources as such in their descriptions; don't delete them silently.
5. **Markers are closed lists.** ⭐ marks named external lists only (ml: Ilya Sutskever's 27 items; pcb: Rick Hartley's 12 books; btc: the Bitcoin Canon table in `btc/README.md`).
   - 🔑 marks the core path: at most 3 per section, chosen by what the 🎯 objectives and 🛠️ exercises use. Never give it to advocacy, speculation or sourceless concept rows.
   - When you add, remove or rename a 🔑 item, update the section's Core path line in the same edit, then run `python tools/build.py` (the indexes and PROGRESS follow automatically).
6. **Label speculation and advocacy.** Examples: unconfirmed theories, price models, vendor productivity claims, findings that failed to replicate.
7. **One home per topic.** Use the overlap table in `STUDY-GUIDE.md`, and cross-link instead of duplicating rows across curricula.
