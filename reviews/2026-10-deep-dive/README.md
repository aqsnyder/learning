# Deep-Dive Review: October 2026

**Scope:** all nine curricula: 110 sections, plus every README, PROGRESS, books, courses, and blogs file. Every file was read in full. Each curriculum was evaluated section by section and then repaired.

The work was done on branch `review/2026-10-deep-dive` and merged into master on 2026-10-13. It came in three passes:
- **First pass:** corrections, additions, the learning layer and 10 new sections, in one commit per curriculum plus one for the repo-level changes.
- **Follow-up pass:** the backlog the first pass ran out of web budget for, plus the tier lists you chose, in the same commit layout. See [Follow-up pass](#follow-up-pass-2026-10-13-backlog-finished).
- **Final pass:** your decisions on the open questions, plus a main page and learning paths built for someone starting out, in one commit. See [Decisions made](#decisions-made-final-pass).

Detailed section-by-section reviews: [ml](ml.md) · [math](math.md) · [physics](physics.md) · [bio](bio.md) · [econ](econ.md) · [philosophy](philosophy.md) · [pcb](pcb.md) · [btc](btc.md) · [software](software.md) · [link audit](link-audit.md) ([arXiv](link-audit-arxiv.md)) · [independent checks](independent-check.md)

---

## Bottom line

The skeleton was good. The arcs make sense, the anchors are mostly canonical, and a lot of the material is free. As a learning tool, though, the repo was a list of bookmarks:

1. **About one wrong or invented citation per section.** Examples: co-authors who don't exist, a "must-read" resource that doesn't exist, and an arXiv link to an astronomy paper.
2. **Fast-moving sections were frozen around 2023.** These include LLMs and RL, agentic coding, Bitcoin proposals, gene editing, and quantum computing.
3. **Your actual work was barely covered.** Precision analog design, measurement physics, bring-up and test, firmware debugging, and signals & systems were thin or absent.
4. **There was no active learning.** No section had objectives, exercises, projects, or self-tests, and PROGRESS counted pages read.

After this review:
- every section has a learning layer;
- the citations and pre-existing links have been checked and corrected;
- every section's must-read path is at most three items;
- the gaps exist as 19 new sections: the missing engineering core in the first pass, and edge ML, philosophy of science, three bio sections and four econ sections in the follow-up.

| Curriculum | Grade as found | After | Biggest problem found | Biggest fix |
|---|---|---|---|---|
| 🧠 ml | C+ | B | Section 12 had invented or misattributed citations. The ⭐ Ilya list was wrong in both directions. LLMs and RL stopped in 2023. | Citations corrected; ⭐ rebuilt as the 27-item list; ~65 + 18 additions (tokenization → RLVR, interpretability 2022–26); new 14 Edge & Embedded ML; description column in 07–13 |
| 🔢 math | B− | B | No engineering-math spine: no complex analysis, signals, numerics, or number theory | New 12 Signals & Systems, 13 Number Theory & Cryptography, 14 Numerical Methods; core/elective route |
| ⚛️ physics | C+ | B | Dead and misattributed Lewin lectures; Wolfram presented as established physics (🔑); no measurement physics | New 12 Measurement, Noise & Sensor Physics; engineering bridge resources; Wolfram labeled speculative |
| 🧬 bio | B− | B+ | About one invented citation per section; 2024–26 absent (protein-design Nobel, Evo 2, base/prime editing); PROGRESS tracked ~6 items per section | 34 + 26 additions; PROGRESS rebuilt; new 12 Statistics & Experimental Design, 13 Bioinstrumentation & Lab Automation, 14 Evolution & Population Genetics; a biosecurity subsection |
| 📈 econ | C+ | B | Priming, ego depletion, and Ariely presented as solid; no macro, econometrics, or IO; "economics of AI" with no economics | Replication caveats and evidence-check sources; 22 + 50 additions; new 12 Economics of AI, 13 Empirical Economics & Causal Inference, 14 Macro, Money & Financial Markets, 15 Industrial Organization |
| 💭 philosophy | C+ | B | Misattributed and nonexistent resources; one-sided LLM-understanding debate; consciousness science stopped at 2021 | 32 + 26 additions that balance each debate; Wolfram labeled; PROGRESS synced; new 12 Philosophy of Science |
| 🔌 pcb | C | B− | Rick Hartley ⭐ list half wrong; KiCad 8 and IPC-2221A out of date; no analog, precision, bring-up, or test coverage | ⭐ matched to his PDF (12 books); KiCad 10 and IPC-2152; new 12 Analog & Precision and 13 Bring-up, Test & Debug |
| ₿ btc | C | B | Invented 🔑 first step in Lightning; nothing after 2023; hands-on work came last | 42 additions with October 2026 proposal statuses; new 12 Hands-on Labs (in parallel) and 13 Governance |
| 🏗️ software | C+ | B | Section 09 (AI workflows) was nearly empty; flagship books an edition behind; no bench work | ~48 additions; new 12 Firmware Toolchain & Debug and 13 HIL & Lab Automation; skill mapping fixed |

*Grades are per-curriculum judgments against the rubric (coverage, accuracy, currency, sequencing, focus). They are not a cross-curriculum ranking.*

---

## What changed, by the numbers

| | Before | After |
|---|---|---|
| Numbered sections | 110 | **129** (19 new: 10 in the first pass, 9 in the follow-up) |
| Resource rows in section tables* | 1,026 | **1,499**. Each added item was opened and checked for title, authors, and year. |
| Logged corrections | — | **~480**: ~290 in the first pass; ~190 in the follow-up (110 flags resolved, 55 link-audit fixes, 25 second-check fixes) |
| Pre-existing links audited | — | **704** (116 arXiv, 33 GitHub, 555 other): 63 fixed, 3 dead rows removed or replaced, 57 couldn't be checked ([link audit](link-audit.md)) |
| Broken internal links | 36 | **0** |
| 🔑 core-path rows | 340, up to 11 per section | **310**, at most 3 per section, each section's listed in a *Core path* line |
| Sections with learning objectives / exercises / self-tests | 0 | **129**: 639 objectives, 630 exercises, 129 mini-projects, 1,032 Check Yourself questions |
| PROGRESS checkboxes | 990 (reading only) | **2,093** (resources + practice + mini-project + self-check) |

\* Resource rows exclude marker legends, Key Concepts tables and btc/12's lab table. The first pass reported 1,076 → 1,458 by counting every table row.

Repo-level additions:
- [`STUDY-GUIDE.md`](../../STUDY-GUIDE.md): the study loop, five tracks, a map of how the curricula connect, and a one-home-per-topic table
- `notes/` and `projects/`, with templates
- `tools/check_repo.py`: offline structural checker
- [`link-audit.md`](link-audit.md): every pre-existing link, checked
- `.agents/skills/audit-curriculum`
- Verification and curation rules in every `update-curriculum` skill
- Corrected root README

---

## Patterns: why these problems existed

1. **AI-generated citations were never verified.** The same failure modes showed up everywhere:
   - invented co-authors ("Bhatt", "Burt")
   - a real title attached to the wrong ID (CoT monitorability → an astronomy paper)
   - resources that don't exist ("Learn Me A Bitcoin: Lightning", an SEP "Extended Mind" entry, an "Amy Kind" playlist that is really a different series)
   - two works merged into one (two Aaronson essays; two Kolmogorov-complexity books)
   - an organization credited where named authors exist

   The update skill made this worse: it said "err on the side of inclusion" and had no verification step. Both are now fixed.
2. **Leftovers from earlier outlines.** Thirty-six internal links pointed at section names from earlier outlines (e.g. `../03-neural-network-foundations`). Three skills mapped topics to directories that never existed.
3. **The fastest-moving sections were the most out of date:** ml/09–10, software/09, btc/11, bio/08, physics/07.
4. **Advocacy and speculation were presented as settled.** Examples: Stock-to-Flow and Ammous as 🔑, Wolfram's physics as 🔑, priming and ego depletion without caveats, and the LLM-understanding debate cited only from one side.
5. **Input-only design.** Learning requires retrieval and production; the repo offered neither.
6. **Generic, not yours.** The content suited a generic learner. The topics that run through your work (signal chains, noise and measurement, precision layout, bring-up, firmware debug, HIL and instrument automation) were the thinnest.
7. **Inconsistent formats.** There were at least four table schemas and three legend styles. 🔑 was inflated (8 of 16 items in ml/08). PROGRESS was out of sync with the sections.

---

## Structure: what was done, and what I recommend next

### Done in this review (nothing renumbered)

- **Same anatomy in every section:** Why → Prerequisites → 🎯 Objectives → Resources → Suggested Order → 🛠️ Practice + 🏗️ Mini-project → ✅ Check Yourself. PROGRESS now tracks practice, not just reading.
- **New sections appended**, with "take after NN" positions given in each learning path, so existing links and NotebookLM sources keep working.
- **[Study Guide](../../STUDY-GUIDE.md):** the study loop, tracks (A, precision hardware and instruments, is your core), a cross-curriculum map, and a one-home-per-topic table. Your own output lives in `notes/` and `projects/`, beside the curated material.
- **Tier lists (your choice, done in the follow-up):** at most 3 🔑 per section, chosen by what the 🎯 objectives and 🛠️ exercises actually use, never advocacy or vendor claims. Each Suggested Order opens with a `**Core path (🔑):**` line, and the books and courses indexes mark 🔑 only on items that are core in some section. ml/07–13 gained the Description column they lacked. Every 🔑 change is logged, with reasons, under "Tier lists" in each curriculum's review file, so you can reverse any call.
- **Maintenance:** `tools/check_repo.py` (0 problems on this branch) and a repo-wide `audit-curriculum` skill. Every update skill now requires opening each link before adding it, citing people rather than organizations, "when in doubt, leave it out", closed ⭐ lists, and honest labels for speculation.

### Recommended next (your call; each is a contained follow-up)

1. **Make resources data, not prose.** Give each section a `resources.yaml` with id, title, authors, year, url, type, priority, markers, and a `verified:` date. Generate the tables and PROGRESS from it. That yields one schema across 129 sections, cross-curriculum deduplication by id, "last verified" dates, and automated link checks. Markdown stays as the rendered view.
2. **Curate instead of append-only.** Correct in place, move superseded items into a collapsed "Archive" block, and let git keep the history. The append-only rule is how invented entries survived.
3. ~~**Tier every list.**~~ ✅ Done in the follow-up pass; see above.
4. **Give each topic one home.** Apply the Study Guide table: turn duplicated rows into cross-links (ml/01 ↔ math, ml/12 ↔ philosophy/07 ↔ econ/11, bio/10 ↔ ml/13, econ/10 ↔ btc/09).
5. **Track mastery, not completion.** Use three states per item (read → practiced → can explain) plus dated re-checks, and export flashcards from `notes/` to Anki.
6. **Check links automatically.** Run a monthly GitHub Action with lychee over the markdown, excluding hosts that block bots, that opens an issue listing dead links.
7. **One update skill.** Fold the four per-curriculum `update-curriculum` skills into a single root skill with per-curriculum config (sources, markers, section map). The 5 curricula without a skill are then covered too.
8. **Before ever making the repo public:**
   - `pcb/documents/IPC-2221A(L).pdf` is a licensed "no reproduction" copy. That's fine while the repo is private, which it is. Remove it before going public. The curriculum now notes that IPC-2221C (2023) and IPC-2152 supersede it.
   - Several pcb and software exercises are tailored to the kind of hardware you build (STM32U5, 4–6-layer boards with USB-C/Ethernet, precision source-measure front ends). No company, product, or customer is named anywhere, but skim them with confidentiality in mind first.

---

## Follow-up pass (2026-10-13): backlog finished

The first pass ran out of web budget. The follow-up finished its backlog with paced fetches, and nothing was added without being opened first.

1. **Link audit of pre-existing links: done.** All 704 links were checked (see [link-audit.md](link-audit.md)):
   - 63 fixed, counting the 8 arXiv mismatches fixed in the first pass
   - 3 dead (those rows were later removed or replaced)
   - 57 couldn't be checked (bot walls, JavaScript-only pages, rate limits); four of those look dead and are worth a manual look
2. **The nine proposed sections now exist,** with the full anatomy and every expected value recomputed:
   - [ml/14 Edge & Embedded ML](../../ml/14-edge-and-embedded-ml/) (take after 08)
   - [philosophy/12 Philosophy of Science](../../philosophy/12-philosophy-of-science/) (after 00)
   - [bio/12 Statistics & Experimental Design](../../bio/12-statistics-and-experimental-design/)
   - [bio/13 Bioinstrumentation, Imaging & Lab Automation](../../bio/13-bioinstrumentation-imaging-and-lab-automation/)
   - [bio/14 Evolution & Population Genetics](../../bio/14-evolution-and-population-genetics/), plus a biosecurity subsection in bio/11
   - [econ/12 Economics of AI](../../econ/12-economics-of-ai/) (econ/11 is now "AI Alignment through an Economic Lens")
   - [econ/13 Empirical Economics & Causal Inference](../../econ/13-empirical-economics-and-causal-inference/)
   - [econ/14 Macro, Money & Financial Markets](../../econ/14-macroeconomics-money-and-financial-markets/) (educational, not investment advice)
   - [econ/15 Industrial Organization & Strategy](../../econ/15-industrial-organization-and-strategy/)
3. **"Verify, then add" lists: done.** About 150 verified resources were added to existing sections:
   - physics 17, among them Taylor, the GUM, NIST TN 1297, Fraden and Riley's Allan-deviation handbook
   - pcb 7, among them Tektronix *ABCs of Probes*, J-STD-048, FastHenry2, J-SMU and boundary-scan tooling
   - philosophy 12, plus a balanced fairness reading in 06
   - btc 4 (Budish; Carlsten et al.; MIT MAS.S62; the Bitcoin Wiki privacy page)
   - software 3, math 2, ml 2 outside the new sections
   - Status claims (BIPs, Bitcoin Core 31.0, Python 3.15, Claude Code and `AGENTS.md`) were re-checked against primary sources.
4. **Suspect entries: all three are real.** These are *Practical PCB Design* (Smith, No Starch, 2026), the Tech Explorations KiCad course, and Dr. EMC. Dr. EMC's old link pointed at an unrelated channel; it now points at `@DrEMC-sf8rx`.
5. **Independent-check flags:** 69 of the first pass's 73 flagged rows are resolved. The other 4 are minor and marked **still open** in [independent-check.md](independent-check.md): a mirror link for Legg's thesis, unchecked chapter numbers in some math exercises, a deliberately repeated pcb question, and the checker's blind spots.
6. **Tier lists:** done (see *Structure*).
7. **Second independent check.** Four fresh checkers with web access checked 342 items of the follow-up work. 25 failed, mostly arithmetic in one bio exercise, a few citation details, and core-path picks that put sourceless concept rows on the must-read path. All 25 are fixed and listed at the end of [independent-check.md](independent-check.md).

### Decisions made (final pass)

You asked for my best calls on the open questions. Here is what was done:

- **Core paths:**
  - **ml/08:** Adam replaces FlashAttention. Practice 2 implements Adam, and the mini-project trains with AdamW.
  - **ml/12:** Constitutional AI replaces Scaling Monosemanticity, so the core path now covers alignment (objective 4) as well as interpretability.
  - **pcb/02:** the KiCad Library Conventions replace your private template. The template stays in the section as a personal reference.
  - **Kept as they were:** DPO over Silver's course (ml/10), the Bitcoin Core source over *Programming Bitcoin* (btc/10), *Modern C* over K&R (software/02), and *The Conscious Mind* (philosophy/02).
- **More concrete core paths:**
  - **pcb/00** names the four *Art of Electronics* chapters its objectives use, and its prerequisites now list the bench gear the exercises need.
  - **pcb/08** starts from Hartley's *The Extreme Importance of PC Board Stack-Up* instead of a YouTube search.
  - **pcb/07:** the search-link row is off the core path.
  - **pcb/10** adds TI's AN-2020 on thermal design.
  - **software/02 and 07** link the Quantum Leaps course playlist instead of the whole channel.
- **One home per topic:**
  - Budish's paper now lives only in btc/09, and Holmes & Huber only in bio/12.
  - In econ/10 and bio/04, the duplicate rows became short "Also used here" notes that link to the home section.
  - PROGRESS now tracks each item once.
- **econ/11's title** stays "AI Alignment through an Economic Lens". The economics of AI moved to econ/12, and the title says what is left.
- **Dead rows:**
  - The two retired Coursera courses in econ/03 and econ/06 are removed.
  - In philosophy/10, Robert Wright's retired course is replaced by his book *Why Buddhism Is True* (2017, checked against a library catalogue). It is placed right before Thompson's critique of it.
- **Your KiCad template repo** is private. It returns 404 to anonymous requests with no redirect, and your only public repo is `isi_openmv`, so it wasn't renamed. The link stays, labelled as private.
- **Update skills:** all four (ml, pcb, btc, software) now say "at most 3 🔑", keep the Core path line in sync, and run `tools/build_index.py`. The ml skill also says to update the books, courses and blogs indexes.
- **Vendor and tool notes worth knowing** (no action needed):
  - ST now marks X-CUBE-AI as not recommended for new designs (noted in ml/04 and ml/14).
  - KiCad's SWIG Python bindings are deprecated in favour of the IPC API (pcb/11).
- **Newcomer path:**
  - The main page now opens with a five-minute start, a pick-a-topic table and a collapsible index of all 129 sections.
  - Each curriculum's learning path is a linked table in recommended order, showing every section's core path.
  - `tools/build_index.py` generates both from the section READMEs, and `check_repo.py` fails if they go stale.
  - Philosophy's icon is now 💭, so it no longer shares 🧠 with ml.

---

## Reviewing the changes

The review branch was merged into master on 2026-10-13 as a fast-forward, so its 21 commits sit unchanged in master's history. One small commit after them records the merge in these notes.

```bash
git log --oneline 4c43272..6452b24     # the 21 review commits: two passes × (9 curricula + repo-level), then one final pass
git diff --stat 4c43272 6452b24        # everything the review changed
python tools/check_repo.py             # expect: 0 problems
```

`4c43272` is master as it was before the review.
