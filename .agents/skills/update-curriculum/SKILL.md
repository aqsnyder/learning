---
name: update-curriculum
description: Find, verify and add new resources to any of the nine curricula in this learning repo, or fix existing ones, by editing the sections' resources.toml files and regenerating with tools/build.py. Use for periodic updates, when an important new book, paper, course, standard or release appears, or when asked to update a reading list.
---

# Update Curriculum

Adds new, verified material to one curriculum (or several) and keeps every section's learning layer whole.
For a full quality pass over what is already there, use the `audit-curriculum` skill instead.

## Where things live

| What | File | Notes |
|---|---|---|
| A section's resources | `<curriculum>/<NN>-<slug>/resources.toml` | The source of truth. Field reference: `tools/README.md`. |
| Books and courses with no section home | `<curriculum>/extras.toml` | Prefer giving a resource a section home. |
| Objectives, Suggested Order, Core path line, exercises, questions | the section `README.md`, outside the generated block | Hand-written prose. |
| Resource tables, `PROGRESS.md`, book and course indexes, learning paths | generated | Never edit by hand. Run `python tools/build.py`. |

To choose a section, read the curriculum README's learning path (sections in recommended order) and the 🎯 objectives
of the candidate sections. A resource belongs where an objective or an exercise needs it.

## Workflow

1. **Research.** Check the sources for the curriculum (table below) and search for what is new since the most recent
   `verified` dates in that curriculum. Look for new editions of books already listed, too.
2. **Evaluate.** Keep a candidate only if it is important (not just new), credible, and fills a gap or replaces
   something weaker. Note what it costs. Prefer primary sources and measured evidence over commentary and vendor claims.
3. **Verify** each keeper by opening it (rules below). Record the exact title, author order, year and edition.
4. **Edit the data.** Add an item to the right group in `resources.toml`:
   - a new `id` (lowercase, hyphens, unique in the section). Never change an existing `id`: learners' ticks are keyed on it.
   - `title`, `authors` (people, or the organization if no people are named), `year`, `type`, `url`, `link_text`,
     a one- or two-sentence `description` saying why it is here, `access` (free, paid or partial), and
     `verified` = today's date.
   - `marks` only as the rules below allow.
5. **Keep the learning layer whole.**
   - Add the resource to the section's Suggested Order.
   - If it changes the core path, update the `**Core path (🔑):**` line so it names exactly the items marked core.
   - If an exercise or Check Yourself question should use it, update that too.
   - If you fix a title or author, fix every mention: Suggested Order, exercises, questions.
6. **Regenerate and check.** Run `python tools/build.py`, then `python tools/check_repo.py`. Both must finish
   with 0 problems.
7. **Summarize** what was added and where, what was considered and rejected (and why), and anything that needs a
   person's decision.

## Rules (mandatory)

Earlier AI-generated updates put invented authors, resources that don't exist, and links to the wrong papers into
this repo (all fixed in the October 2026 review; see `reviews/2026-10-deep-dive/`). So:

1. **Open every link before adding it.** Use the arXiv abs page, the DOI record
   (`https://api.crossref.org/works/<DOI>`), the publisher's or author's page, or the YouTube oEmbed record
   (`https://www.youtube.com/oembed?url=<url>&format=json`). Confirm the exact title, author order, year and edition.
   Never write a URL or an author list from memory, and never from a search-result snippet alone.
2. **Cite people, not organizations,** when a work lists authors ("Templeton et al.", not "Anthropic").
3. **When in doubt, leave it out.** Put doubtful or unverifiable candidates in your summary instead.
4. **Correct, don't just append.** Fix wrong metadata in place and update `verified`. If a resource is superseded
   or dead, replace it with a verified equivalent or say so in its description.
5. **Markers are closed lists.**
   - 🔑 (`core`): at most 3 per section, chosen by what the 🎯 objectives and 🛠️ exercises use. Never give it to
     advocacy, speculation, vendor claims, or a row without a source.
   - 🔑🔑 (`masterwork`, philosophy only): at most one foundational masterwork per section; it counts toward the 3.
   - ⭐ (`canon`): only items on the curriculum's named external list (table below). Never extend a list.
   - 🤖 (`ai`, software only): resources specific to AI-assisted development.
6. **Label speculation and advocacy** in the description: unconfirmed theories, price models, vendor productivity
   claims, findings that failed to replicate.
7. **One home per topic.** Check the overlap table in `STUDY-GUIDE.md`. If a resource's topic lives in another
   section or curriculum, add a cross-link in the group's `outro` instead of a duplicate row.
8. **No concept rows.** Every item needs a source. A topic with no good source belongs in the section's prose or
   Check Yourself questions, not in the resource table.
9. **Nothing personal.** No private repositories, employers, products or customers: the repo is meant to be public.

## Curriculum settings

| Curriculum | ⭐ list | Sources to check | Extra rules |
|---|---|---|---|
| ml | Ilya Sutskever's 27-item list, fixed; never add ⭐ | NeurIPS, ICML and ICLR papers; arXiv cs.LG, cs.CL, cs.CV and cs.AI; courses from established educators (Karpathy, Stanford, MIT); the Stanford HAI AI Index | Frontier sections (09–11) need a dated status line when a claim can change. Prefer the paper over the blog post about it. |
| math | none | arXiv math; new editions of the listed textbooks; open textbooks | Prefer free texts with exercises. |
| physics | none | arXiv physics; new editions; MIT OCW and university course pages | Label speculative programs (e.g. Wolfram's) as speculative. |
| bio | none | Nature, Science and Cell; bioRxiv; Nobel lectures; NIH and NHGRI pages | Note dual-use concerns where relevant (see Section 11's biosecurity subsection). |
| econ | none | NBER working papers; AEA journals; replication projects | Add replication caveats to behavioral findings. Educational only, never investment advice. |
| philosophy | none (🔑🔑 marks a masterwork) | the Stanford Encyclopedia of Philosophy; PhilPapers; new books from academic presses | Keep every debate balanced: when you add one side, check the other side is represented. |
| pcb | Rick Hartley's 12 books (listed in `pcb/README.md`); never his talks or anything else | Phil's Lab, Robert Feranec, Rick Hartley, Eric Bogatin, Altium Academy; KiCad releases; IPC and JEDEC standards; vendor app notes (ADI, TI, ST) | Prefer a specific video or playlist over a channel home page. Standards are paid: say so. |
| btc | the canon table in `btc/README.md`; extending it is the owner's decision | Bitcoin Core releases; the BIPs repository; Bitcoin Optech and its topics index; Delving Bitcoin; the bitcoindev list; Chaincode Labs | Quote proposal status from the BIPs repository (Draft / Complete / Deployed / Closed under BIP 3) with the date checked. Educational only, never investment advice. |
| software | none (🤖 marks AI-workflow items) | Python "What's New"; Embedded Artistry, Interrupt (Memfault); Simon Willison's blog; METR and DORA reports; release notes of AI coding tools | Prefer measured evidence (randomized studies, DORA) over vendor claims. |

## New sections

Append a new section at the next free number; never renumber. Give it the full anatomy described in the
`audit-curriculum` skill, plus a `resources.toml`. Then run `python tools/build.py`: the section appears at the end
of the curriculum's learning path with "When" set to "(place me)". Move its row to where it belongs and write a
"When" note (for example "After 05").
