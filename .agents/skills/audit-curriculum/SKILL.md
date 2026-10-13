---
name: audit-curriculum
description: Audit and repair a curriculum in this learning repo (or all nine) — verify citations and links, fix structure with tools/check_repo.py, keep every section's learning blocks complete, add verified missing material, and write a dated review under reviews/. Use for periodic quality passes, when building a new section or curriculum, or for curricula without their own update-curriculum skill.
---

# Audit Curriculum

A repo-wide quality pass. The per-curriculum `update-curriculum` skills (ml, pcb, btc, software) add new material. This skill checks that everything already here is **true, reachable, and teachable**, and it is the procedure for adding material to curricula that have no skill of their own (bio, econ, math, philosophy, physics).

## When to use

- Quarterly, or after several `update-curriculum` runs
- Before creating a new section or curriculum
- When a citation looks wrong or links have started to rot

## Section anatomy (every numbered section README)

1. `# Title`
2. `## Why This Section Matters`
3. `## Prerequisites`: relative links to directories that exist; link other curricula as `../../<curriculum>/<section>/`
4. `## 🎯 Learning Objectives`: 3–5 observable, verb-led outcomes (derive, implement, design, estimate, debug, critique)
5. Resource table(s) in the curriculum's schema; 🔑 on about 3 core items (many sections still have more; trim when you touch them); ⭐ only for the curriculum's named list
6. `## Suggested Order`, which should cover every resource
7. `---` then `## 🛠️ Practice`: 3–5 exercises, each with inputs → deliverable → how you know it's right, plus an honest time estimate and the resources it uses. Then `**🏗️ Mini-project — <Name>:**` with a deliverable under `projects/<curriculum>/…` and a success criterion.
8. `## ✅ Check Yourself`: 5–8 retrieval questions without answers. Mix recall, explanation, estimation, a misconception probe, and "explain it to a smart friend".

Each section in `PROGRESS.md` needs a `## Section NN — Title` block with one checkbox per resource, then:
```
- [ ] 🛠️ Practice exercises 1–N
- [ ] 🏗️ Mini-project: <Name>
- [ ] ✅ Check Yourself — answered from memory
```
New sections are appended at the next free number. The curriculum README's learning path says where to take them ("take after 05"). Never renumber existing sections.

## Workflow

1. **Structure.** Run `python tools/check_repo.py` and fix every reported problem: broken relative links, ragged tables, missing learning blocks, PROGRESS gaps, sections missing from the learning path.
2. **Citations.** Run `python tools/check_repo.py --urls > urls.txt`. Check each URL against the title, authors and year in its row:
   - arXiv: fetch `https://arxiv.org/abs/<id>` (the export API is blocked by robots)
   - DOI: `https://api.crossref.org/works/<DOI>` (DataCite fallback: `https://api.datacite.org/dois/<DOI>`)
   - YouTube: `https://www.youtube.com/oembed?url=<url>&format=json`
   - Anything else: fetch the page itself

   Record each result as ok / mismatch / broken / moved / unverifiable. Batch the work, and stop when web budgets run out rather than guessing.
3. **Content.** Score each section 1–5 on coverage, accuracy, currency, sequencing, and focus. Check that every 🛠️ exercise and ✅ question uses a resource listed in its own section, or names the section that lists it. Label speculative or advocacy material honestly.
4. **Repair.** Fix verified errors in place, and add only verified resources (see the rules below). When a resource changes, update its Suggested Order entry, its PROGRESS line, and any exercise that cites it.
5. **Report.** Write `reviews/<YYYY-MM>-<name>/<curriculum>.md` containing: verdict, scorecard, section-by-section notes, a corrections table with evidence URLs, additions, proposals, cut candidates, and the top 5 priorities.
6. **Re-check.** `python tools/check_repo.py` must report 0 problems. Then summarize what changed and what is still unverified.

## Rules (shared with the update-curriculum skills)

1. **Open every link before adding it.** Confirm the exact title, author order, year, and edition. Never write a URL or an author list from memory.
2. **Cite people, not organizations,** whenever a work lists authors.
3. **When in doubt, leave it out.** Put doubtful candidates in the report, not in the curriculum.
4. **Correct, don't just append.** Fix errors in place. Mark superseded or dead resources as such in their descriptions; don't delete them silently.
5. **Markers are closed lists.** ⭐ marks named external lists only (ml: Ilya Sutskever's 27 items; pcb: Rick Hartley's 12 books; btc: the Bitcoin Canon table in `btc/README.md`). 🔑 marks the core path.
6. **Label speculation and advocacy.** Examples: unconfirmed theories, price models, vendor productivity claims, findings that failed to replicate.
7. **One home per topic.** Use the overlap table in `STUDY-GUIDE.md`, and cross-link instead of duplicating rows across curricula.
