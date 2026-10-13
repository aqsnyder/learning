# Deep-Dive Review: October 2026

**Scope:** all nine curricula: 110 sections, plus every README, PROGRESS, books, courses, and blogs file. Every file was read in full. Each curriculum was evaluated section by section and then repaired. Fixes and additions are on branch `review/2026-10-deep-dive`, one commit per curriculum plus one for the repo-level changes.

Detailed section-by-section reviews: [ml](ml.md) · [math](math.md) · [physics](physics.md) · [bio](bio.md) · [econ](econ.md) · [philosophy](philosophy.md) · [pcb](pcb.md) · [btc](btc.md) · [software](software.md) · [arXiv link audit](link-audit-arxiv.md) · [independent check](independent-check.md)

---

## Bottom line

The skeleton was good. The arcs make sense, the anchors are mostly canonical, and a lot of the material is free. As a learning tool, though, the repo was a list of bookmarks:

1. **About one wrong or invented citation per section.** Examples: co-authors who don't exist, a "must-read" resource that doesn't exist, and an arXiv link to an astronomy paper.
2. **Fast-moving sections were frozen around 2023.** These include LLMs and RL, agentic coding, Bitcoin proposals, gene editing, and quantum computing.
3. **Your actual work was barely covered.** Precision analog design, measurement physics, bring-up and test, firmware debugging, and signals & systems were thin or absent.
4. **There was no active learning.** No section had objectives, exercises, projects, or self-tests, and PROGRESS counted pages read.

After this review, every section has a learning layer, the citations have been corrected, and the missing engineering core exists as ten new sections.

| Curriculum | Grade as found | After | Biggest problem found | Biggest fix |
|---|---|---|---|---|
| 🧠 ml | C+ | B | Section 12 had invented or misattributed citations. The ⭐ Ilya list was wrong in both directions. LLMs and RL stopped in 2023. | Citations corrected; ⭐ rebuilt as the 27-item list; ~65 additions (tokenization → RLVR, interpretability 2022–26) |
| 🔢 math | B− | B | No engineering-math spine: no complex analysis, signals, numerics, or number theory | New 12 Signals & Systems, 13 Number Theory & Cryptography, 14 Numerical Methods; core/elective route |
| ⚛️ physics | C+ | B | Dead and misattributed Lewin lectures; Wolfram presented as established physics (🔑); no measurement physics | New 12 Measurement, Noise & Sensor Physics; engineering bridge resources; Wolfram labeled speculative |
| 🧬 bio | B− | B | About one invented citation per section; 2024–26 absent (protein-design Nobel, Evo 2, base/prime editing); PROGRESS tracked ~6 items per section | 34 additions; PROGRESS rebuilt (87 → 166 lines plus practice); broken prerequisite links fixed |
| 📈 econ | C+ | B− | Priming, ego depletion, and Ariely presented as solid; no macro, econometrics, or IO; "economics of AI" with no economics | Replication caveats and evidence-check sources; 22 additions; 4 section proposals |
| 🧠 philosophy | C+ | B | Misattributed and nonexistent resources; one-sided LLM-understanding debate; consciousness science stopped at 2021 | 32 additions that balance each debate; Wolfram labeled; PROGRESS synced (~30 missing items) |
| 🔌 pcb | C | B− | Rick Hartley ⭐ list half wrong; KiCad 8 and IPC-2221A out of date; no analog, precision, bring-up, or test coverage | ⭐ matched to his PDF (12 books); KiCad 10 and IPC-2152; new 12 Analog & Precision and 13 Bring-up, Test & Debug |
| ₿ btc | C | B | Invented 🔑 first step in Lightning; nothing after 2023; hands-on work came last | 42 additions with October 2026 proposal statuses; new 12 Hands-on Labs (in parallel) and 13 Governance |
| 🏗️ software | C+ | B | Section 09 (AI workflows) was nearly empty; flagship books an edition behind; no bench work | ~48 additions; new 12 Firmware Toolchain & Debug and 13 HIL & Lab Automation; skill mapping fixed |

*Grades are per-curriculum judgments against the rubric (coverage, accuracy, currency, sequencing, focus). They are not a cross-curriculum ranking.*

---

## What changed, by the numbers

| | Before | After |
|---|---|---|
| Numbered sections | 110 | **120** (10 new) |
| Resource rows in section tables | 1,076 | **1,458**. Each added item was opened and checked for title, authors, and year. |
| Logged corrections | — | **~290**: wrong authors, IDs, links, titles, editions, misleading claims |
| Broken internal links | 36 | **0** |
| Sections with learning objectives / exercises / self-tests | 0 | **120**: 594 objectives, 585 exercises, 120 mini-projects, 960 Check Yourself questions |
| PROGRESS checkboxes | 990 (reading only) | **1,892** (resources + practice + mini-project + self-check) |

Repo-level additions:
- [`STUDY-GUIDE.md`](../../STUDY-GUIDE.md): the study loop, five tracks, a map of how the curricula connect, and a one-home-per-topic table
- `notes/` and `projects/`, with templates
- `tools/check_repo.py`: offline structural checker
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
- **Maintenance:** `tools/check_repo.py` (0 problems on this branch) and a repo-wide `audit-curriculum` skill. Every update skill now requires opening each link before adding it, citing people rather than organizations, "when in doubt, leave it out", closed ⭐ lists, and honest labels for speculation.

### Recommended next (your call; each is a contained follow-up)

1. **Make resources data, not prose.** Give each section a `resources.yaml` with id, title, authors, year, url, type, priority, markers, and a `verified:` date. Generate the tables and PROGRESS from it. That yields one schema across 120 sections, cross-curriculum deduplication by id, "last verified" dates, and automated link checks. Markdown stays as the rendered view.
2. **Curate instead of append-only.** Correct in place, move superseded items into a collapsed "Archive" block, and let git keep the history. The append-only rule is how invented entries survived.
3. **Tier every list.** Aim for about three 🔑 core items per section, then "go deeper", then "reference". Today 34 of 120 sections have more than three. In 7 of those, this review promoted a new essential item (e.g. *Modern C*, the METR study, *The Bitter Lesson*) without demoting an older one, because what to drop is your call. Start with ml/08, ml/09, ml/12 and software/09, and add the missing description column to ml/07–13.
4. **Give each topic one home.** Apply the Study Guide table: turn duplicated rows into cross-links (ml/01 ↔ math, ml/12 ↔ philosophy/07 ↔ econ/11, bio/10 ↔ ml/13, econ/10 ↔ btc/09).
5. **Track mastery, not completion.** Use three states per item (read → practiced → can explain) plus dated re-checks, and export flashcards from `notes/` to Anki.
6. **Check links automatically.** Run a monthly GitHub Action with lychee over the markdown, excluding hosts that block bots, that opens an issue listing dead links.
7. **One update skill.** Fold the four per-curriculum `update-curriculum` skills into a single root skill with per-curriculum config (sources, markers, section map). The 5 curricula without a skill are then covered too.
8. **Before ever making the repo public:**
   - `pcb/documents/IPC-2221A(L).pdf` is a licensed "no reproduction" copy. That's fine while the repo is private, which it is. Remove it before going public. The curriculum now notes that IPC-2221C (2023) and IPC-2152 supersede it.
   - Several pcb and software exercises are tailored to the kind of hardware you build (STM32U5, 4–6-layer boards with USB-C/Ethernet, precision source-measure front ends). No company, product, or customer is named anywhere, but skim them with confidentiality in mind first.

---

## Backlog: what this run didn't finish

The web lookup budget ran out partway through: search hit its per-run cap, and page fetches were rate-limited. Nothing unverified was added. These items remain:

1. **Link audit of pre-existing links.** All 116 arXiv links were checked: 8 citation mismatches were found and all are fixed. About 600 other links that were already in the repo (DOIs, YouTube, course pages, GitHub) were not checked one by one, although reviewers fixed many bad ones they hit while reading. Run step 2 of the `audit-curriculum` skill.
2. **Proposed sections waiting for verified resources:**
   - **ml/14 Edge & Embedded ML (TinyML):** quantization, CMSIS-NN, MCUNet, TFLite Micro, MLPerf Tiny, on-target measurement. *High value for you.*
   - **philosophy: Philosophy of Science & Scientific Reasoning:** Popper, Kuhn, Lakatos, Bayesian epistemology.
   - **bio:** Statistics & Experimental Design · Bioinstrumentation, Imaging & Lab Automation · Evolution & Population Genetics · a Biosecurity subsection.
   - **econ:** Economics of AI (rebuild section 11) · Empirical Economics & Causal Inference · Macro, Money & Financial Markets · Industrial Organization.
3. **"Verify, then add" lists** in each curriculum review. Examples: physics (Taylor's *Error Analysis*, the GUM, Fraden's sensors handbook); pcb (Tektronix *ABCs of Probes*, PyVISA, boundary-scan tooling); philosophy (Frege, Putnam, Strawson, Birch).
4. **Suspect entries kept but flagged *(unverified)*:** pcb's "Practical PCB Design" (Smith; 🔑 removed), the Tech Explorations KiCad Advanced course, and the Dr. EMC channel.

---

## Reviewing the branch

```bash
git log --oneline master..review/2026-10-deep-dive
git diff --stat master...review/2026-10-deep-dive
git switch review/2026-10-deep-dive
python tools/check_repo.py              # expect: 0 problems
```

The branch exists only on your machine; nothing was pushed. When you're happy with it, merge it (`git switch master && git merge review/2026-10-deep-dive`) or cherry-pick the per-curriculum commits.

When the branch was created, `ml/PROGRESS.md` and `ml/12-interpretability-and-alignment/README.md` showed as modified on master. `git diff -w` showed the only difference was line endings (CRLF vs LF). If `git switch` refuses because of those two files, run `git stash` first. You can drop the stash afterwards.
