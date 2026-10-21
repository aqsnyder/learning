# The A+ Program (October 2026)

The [deep-dive review](../2026-10-deep-dive/README.md) left every curriculum at about a B. This program takes all
nine to A+, in three passes, each merged as its own pull request.

## What A+ means here

A section is A+ when:

1. **Every resource is specific, linked and checked.** It points at the exact chapter, video or playlist (not a
   channel or a home page), names its edition, and carries a `verified` date from someone who opened it.
2. **The core path covers the objectives.** At most three 🔑 items, which together cover every 🎯 objective. Every
   objective is exercised by at least one exercise and asked by at least one Check Yourself question.
3. **Every exercise has a check you can't fudge:** an expected value, a "done when", or tests for code.
4. **Check Yourself has answers**, kept in a separate `ANSWERS.md` so that pasting the questions into a quiz tool
   doesn't leak them, and each answer was checked by a second reviewer.
5. **Claims that can go stale are dated** and re-checked on a schedule: a monthly link check and a quarterly audit.
6. **It has been used.** Someone worked through it, logged real time and sticking points, and the section was
   revised. Only learners can supply this one; `tools/progress.py log` records the data.

A curriculum is A+ when its sections are, when it has a time budget and a minimum route, and when no topic is
duplicated across sections without a cross-link.

## Passes

| Pass | Scope | Status |
|---|---|---|
| 1. Foundation | Resources become data (`resources.toml` per section) with a generator; private progress tracking in `my/`; CI and a monthly link check; licenses for public release; one update skill for all nine curricula | This pull request |
| 2. Accuracy and coverage | Source or remove the 132 concept rows; link every book; replace channel-home links; re-check the 57 links that blocked the automated audit; descriptions and verified dates for every row; rebuild the sections that only got corrections; objective → exercise → question traceability; one home for duplicated resources | Next |
| 3. Feedback | `ANSWERS.md` for all 1,032 Check Yourself questions, independently checked; a completion check for every exercise; tests for code exercises with a fixed result; a time budget and minimum route per curriculum | After pass 2 |
| Final | Independent grading against the checklist above; publishing steps; quarterly audit | Last |

## Pass 1 results

- **Resources are data.** 1,527 rows from 129 sections now live in `resources.toml` files, one per section, plus 47
  index-only books and courses in `extras.toml` files. The migration was checked for loss: every URL, row, marker and
  line of prose survived. Ten table layouts became one.
- **Generated, never stale:** each section's resource table, each curriculum's `PROGRESS.md` template, the book and
  course indexes (which now say which sections use each item), the learning paths and the main page's section index.
- **Verified dates.** 1,135 rows carry `verified = 2026-10-13`: their links were checked in the October review and
  aren't among the 57 the audit couldn't load. Three more were checked during this pass. The other 389 have no date yet; pass 2 checks them.
- **Private progress.** `tools/progress.py` keeps each learner's checklists, notes, projects and time log in `my/`,
  which git ignores. Ticks survive curriculum updates because every checklist line has a stable ID.
- **Public-release hygiene.** CC BY 4.0 for content and MIT for tools. The licensed IPC-2221A copy and a third-party
  handout were removed; the remaining bundled PDF is distributed under its own terms. Both removed files are still
  in the git history, which has to be dealt with before the repo goes public.
- **Maintenance.** CI runs the checker on every push; a monthly workflow checks every external link and opens an
  issue on failures. The four per-curriculum update skills were merged into one skill for all nine curricula.

The checker's `--strict` mode measures what is left for pass 2:

| | items | no link | no author | no year (dated types) | no description | not verified | concept rows |
|---|---|---|---|---|---|---|---|
| all nine | 1,527 | 342 | 285 | 240 | 149 | 389 | 132 |
