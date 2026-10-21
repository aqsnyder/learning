# Pass 2 log — philosophy, Sections 07–12 (philosophy-B)

Date: 2026-10-21. Scope: `philosophy/07` … `philosophy/12` (section `resources.toml` and `README.md` only).
Build and check: `python3 tools/build.py --only philosophy/07,philosophy/08,philosophy/09,philosophy/10,philosophy/11,philosophy/12`
and `python3 tools/check_repo.py --only …` (same list).

How things were verified: every new or changed citation comes from a page fetched on 2026-10-21 (SEP and IEP entries,
arXiv abstract pages, Crossref records, publisher pages, YouTube oEmbed, PyPI). Two limits shaped what could be done:
the shared web-search budget ran out after 22 searches, and Crossref and doi.org rate-limited repeatedly (each time I
paused 150 s and did not refetch that URL). Books whose publisher page could not be reached that way are listed under
"For a browser check".

Where a book's linked page is a later edition and no fetched page confirmed the first-edition year, `year` is the
linked edition's year and the description says which edition the link is (Superintelligence, Freedom Evolves,
What the Buddha Taught). Where an SEP entry confirmed the original year, the field reads "original (new ed. year)".

SEP and IEP rows: `authors = "SEP"` replaced by the entry's author(s) (the binding rule "cite people, not
organizations"), with `year` as "first published (rev. year)" and the dates in the description.

## 1. Changes

| Section | Item (id) | Change | Evidence URL |
|---|---|---|---|
| 07 | superintelligence-paths-dangers | Link added (OUP paperback, 14 Jul 2016, ends with an afterword); `year` 2014 → 2016 (the linked edition; no fetched page showed 2014); description tightened; verified | https://india.oup.com/product/superintelligence-9780198739838 |
| 07 | human-compatible-artificial-intelligence | Link added; title subtitle → "AI and the Problem of Control" (the Penguin edition linked, released 8 Oct 2019); access paid; level beginner; verified | https://www.penguin.com.au/books/human-compatible-9780241335246 |
| 07 | the-precipice-existential-risk-and-the | Link added (Grand Central/Hachette, 24 Mar 2020); access paid; level beginner; verified | https://www.hachettebookgroup.com/titles/toby-ord/the-precipice/9780316484893 |
| 07 | intelligence-explosion-microeconomics | access free; description says what Practice 3 uses it for | (MIRI PDF, verified 2026-10-13) |
| 07 | what-failure-looks-like | access free | (verified 2026-10-13) |
| 07 | the-alignment-problem-from-a-deep | Title capitalization fixed to the arXiv title; description notes v8 (May 2025); verified | https://arxiv.org/abs/2209.00626 |
| 07 | concrete-problems-in-ai-safety | Authors "Amodei et al." → all six names; "Also used in econ/11."; verified | https://arxiv.org/abs/1606.06565 |
| 07 | specification-gaming-the-flip-side | **Added** (Krakovna et al., DeepMind blog, 21 Apr 2020): Practice 2 used DeepMind's specification-gaming list without listing it | https://deepmind.google/blog/specification-gaming-the-flip-side-of-ai-ingenuity/ |
| 07 | bluedot-impact-ai-safety-courses | Link: home page → course catalog; title → the page's title; year 2026 (catalog as checked); access free; level beginner; description dated (October 2026 course list); "Also used in econ/11."; verified | https://bluedot.org/courses ; https://bluedot.org/llms.txt |
| 07 | 80-000-hours-ai-risk-profile | access free; description labels it advocacy (rule 6). URL not re-checked (see browser check) | — |
| 07 | is-power-seeking-ai-an-existential-risk | Revision dated: "May 2022 update … over 10%" (from the abstract); verified | https://arxiv.org/abs/2206.13353 |
| 07 | ai-as-normal-technology | access free | (verified 2026-10-13) |
| 07 | international-ai-safety-report-2026 | Link: site home → the report's own page; authors "(chair)"; access free; description dated (3 Feb 2026; still the latest full report as of October 2026; last Key Update 25 Nov 2025); verified | https://internationalaisafetyreport.org/publication/international-ai-safety-report-2026 ; https://internationalaisafetyreport.org/ |
| 07 | README | Suggested Order (BlueDot, Krakovna et al., Ngo title, report dated, 80,000 Hours labeled); P2 source note; mini-project dates Carlsmith's update; Q4 (off-switch) and Q5 (takeoff) added | — |
| 08 | climbing-towards-nlu-on-meaning-form-and | **Deleted**; replaced by an outro cross-link to its home in Section 05 (task brief). Core path, Suggested Order 11, P4, P5 and the mini-project now point to Section 05 | — |
| 08 | the-vector-grounding-problem | Marked core in place of Bender & Koller (see Decisions) | (verified 2026-10-13) |
| 08 | logic-and-conversation | Link added (Brill chapter DOI, *Syntax and Semantics 3: Speech Acts*, 1975, pp. 41–58); authors "H. P. Grice"; access paid; verified | https://api.crossref.org/works?query.bibliographic=Grice+Logic+and+Conversation+Syntax+and+Semantics+Speech+Acts |
| 08 | speech-acts-an-essay-in-the-philosophy | Link added (Cambridge DOI); authors "John R. Searle"; access paid; level advanced; verified | https://api.crossref.org/works?query.bibliographic=Searle+Speech+Acts+An+Essay+in+the+Philosophy+of+Language |
| 08 | how-to-do-things-with-words | access paid; level intermediate (no link: see browser check) | — |
| 08 | theories-of-meaning | authors SEP → Jeff Speaks; year 2010 (rev. 2024); verified | https://plato.stanford.edu/entries/meaning/ |
| 08 | sense-and-reference-uber-sinn-und | access paid (JSTOR) | (verified 2026-10-13) |
| 08 | the-meaning-of-meaning | access free | (verified 2026-10-13) |
| 08 | wittgenstein | Title → "Ludwig Wittgenstein"; authors SEP → Anat Matar; year 2002 (rev. Sept 2026); verified | https://plato.stanford.edu/entries/wittgenstein/ |
| 08 | distributional-structure | access paid | (verified 2026-10-13) |
| 08 | README | Core path; Suggested Order 4 and 11; P1, P4, P5 source notes; mini-project; Q6 (distributional hypothesis) added | — |
| 09 | elbow-room-the-varieties-of-free-will | Link added (MIT Press new edition, 7 Aug 2015); authors "Daniel C. Dennett"; year "1984 (new ed. 2015)" (1984 from the SEP entry); "best defense" → "best-known defense"; verified | https://api.crossref.org/works/10.7551/mitpress/10470.001.0001 ; https://plato.stanford.edu/entries/compatibilism/ |
| 09 | freedom-evolves | Link added (Penguin Books paperback, 27 Jan 2004); `year` 2003 → 2004 (linked edition); authors "Daniel C. Dennett"; access paid; level intermediate; verified | https://www.penguinrandomhouse.com/books/288114/freedom-evolves-by-daniel-c-dennett/ |
| 09 | time-of-conscious-intention-to-act-in | access paid (OUP: "You do not currently have access"); *Brain* 106(3): 623–642 added; verified | https://academic.oup.com/brain/article-abstract/106/3/623/271932 |
| 09 | alternate-possibilities-and-moral | access paid (JSTOR) | (verified 2026-10-13) |
| 09 | freedom-and-resentment | Link added (title essay of the Routledge 2008 edition of *Freedom and Resentment and Other Essays*); 1962 confirmed in SEP; access paid; verified | https://api.crossref.org/works/10.4324/9780203882566 ; https://plato.stanford.edu/entries/compatibilism/ |
| 09 | determined-a-science-of-life-without | Link added (Penguin, hardcover 17 Oct 2023); title "without" as published; authors "Robert M. Sapolsky"; access paid; level beginner; verified | https://www.penguinrandomhouse.com/books/592344/determined-by-robert-m-sapolsky |
| 09 | an-accumulator-model-for-spontaneous | access free (PNAS) | (verified 2026-10-13) |
| 09 | free-agents-how-evolution-gave-us-free | access paid; level intermediate | (verified 2026-10-13) |
| 09 | just-deserts-debating-free-will | access paid; level intermediate | (verified 2026-10-13) |
| 09 | free-will | authors SEP → Christopher Franklin (the entry's only `citation_author`); year 2002 (rev. 2022); description points to §2.2; verified | https://plato.stanford.edu/entries/freewill/ |
| 09 | compatibilism | authors SEP → D. Justin Coates; year 2004 (rev. 2024); description maps §§3.1, 3.2, 4.4; verified | https://plato.stanford.edu/entries/compatibilism/ |
| 09 | human-behavioral-biology | Link was a third-party playlist (channel "otur1") → Stanford's own "Lecture Collection \| Human Behavioral Biology"; type video → video-series; level intermediate; verified | https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PL848F2368C90DDC3D&format=json |
| 09 | README | Q7 (Mitchell vs. Sapolsky) and Q9 (responsibility for an agent's act) added | — |
| 10 | (section) | **Broadened** to match its title: four titled groups (Buddhist philosophy of mind; Indian rivals: Nyāya and Advaita Vedānta; Chinese philosophy: heart-mind and agency; Buddhism and the sciences of mind) | — |
| 10 | what-the-buddha-taught | Link added (Grove paperback, 1 May 1969, foreword by Paul Demiéville); `year` 1959 → 1969 (the linked edition); "clearest, most authoritative" → "classic, widely used"; verified | https://groveatlantic.com/book/what-the-buddha-taught/ |
| 10 | buddhism-as-philosophy-an-introduction | access paid; level beginner (no link: see browser check) | — |
| 10 | buddha | authors SEP → Mark Siderits; year 2011 (rev. 2023); description; verified | https://plato.stanford.edu/entries/buddha/ |
| 10 | mind-in-indian-buddhist-philosophy | authors SEP → Christian Coseru; year 2009 (rev. 2012); verified | https://plato.stanford.edu/entries/mind-indian-buddhism/ |
| 10 | the-fundamental-wisdom-of-the-middle-way | Link added (OUP, 27 Jul 1995); translator "Jay L. Garfield"; access paid; level advanced; verified | https://api.crossref.org/works?query.bibliographic=Garfield+Fundamental+Wisdom+of+the+Middle+Way+Nagarjuna+Mulamadhyamakakarika |
| 10 | the-embodied-mind-revisited | **Deleted** (same book as Section 04's core row, and it said "tracked once" while still being tracked); replaced by an outro cross-link to Section 04 | — |
| 10 | classical-indian-philosophy-a-history-of | Marked core; access paid; level beginner | (verified 2026-10-13) |
| 10 | nyaya-iep | **Added**: IEP "Nyāya" (Matthew R. Dasti) — the classical arguments for a self (§2.a) | https://iep.utm.edu/nyaya/ |
| 10 | advaita-vedanta-iep | **Added**: IEP "Advaita Vedanta" (Sangeetha Menon) — the self as self-luminous consciousness | https://iep.utm.edu/advaita-vedanta/ |
| 10 | mind-heart-mind-in-chinese-philosophy | **Added, core**: SEP "Mind (Heart-Mind) in Chinese Philosophy" (David Wong, 2023) | https://plato.stanford.edu/entries/chinese-mind/ |
| 10 | zhuangzi-sep | **Added**: SEP "Zhuangzi" (Chad Hansen, 2014, rev. 2024) | https://plato.stanford.edu/entries/zhuangzi/ |
| 10 | waking-dreaming-being-self-and | Link added (Columbia UP DOI, 2014); access paid; level intermediate; verified | https://api.crossref.org/works?query.bibliographic=Thompson+Waking+Dreaming+Being+Self+and+Consciousness+in+Neuroscience+Meditation+and+Philosophy |
| 10 | the-bodhisattva-s-brain-buddhism | access paid; level intermediate (no link: see browser check) | — |
| 10 | why-buddhism-is-true-the-science-and | Link added (Simon & Schuster, 8 Aug 2017); access paid; level beginner; verified | https://www.simonandschuster.com/books/Why-Buddhism-is-True/Robert-Wright/9781439195475 |
| 10 | why-i-am-not-a-buddhist | access paid; level intermediate (no link: see browser check) | — |
| 10 | README | "Why This Section Matters" now covers Nyāya, Advaita and Chinese thought; objective 2 sharpened, objective 5 added (Chinese heart-mind and agency); Core path now three items; Suggested Order 11 → 15 steps; P1 rewritten against Nyāya and Advaita; **P6 added** ("Cook Ding and the coding agent"); mini-project's self-theorist is a Nyāya philosopher; questions restructured to 10 | — |
| 11 | reality-virtual-worlds-and-the-problems | Link added (free excerpt on the author's site; W. W. Norton, © 2022); authors "David J. Chalmers"; access partial; level beginner; verified | https://consc.net/reality+/excerpt.pdf |
| 11 | consciousness-in-artificial-intelligence | Authors "Patrick Butlin, Robert Long, et al. (19 authors)"; description dated (August 2023), "most rigorous … to date" removed; verified | https://arxiv.org/abs/2308.08708 |
| 11 | the-edge-of-sentience-risk-and | access free (open access); level intermediate | (verified 2026-10-13) |
| 11 | the-weirdness-of-the-world | access paid; level intermediate (no link: see browser check) | — |
| 11 | being-you-a-new-science-of-consciousness | Link added (Dutton, 19 Oct 2021); access paid; level beginner; description tied to Practice 3; verified | https://www.penguinrandomhouse.com/books/566315/being-you-by-anil-seth/ |
| 11 | integrated-information-theory-iit-4-0 | Link: arXiv preprint → published version (*PLOS Comput. Biol.* 19(10) e1011465, 17 Oct 2023, CC BY), arXiv kept as second link; "latest formulation" → "IIT's 2023 formulation"; authors note 16; verified | https://api.crossref.org/works/10.1371/journal.pcbi.1011465 ; https://arxiv.org/abs/2212.14787 |
| 11 | life-3-0-being-human-in-the-age-of-ai | Title subtitle → "…in the Age of Artificial Intelligence"; link added (PRH; ebook 29 Aug 2017); access paid; level beginner; labeled speculative; verified | https://www.penguinrandomhouse.com/books/530584/life-30-by-max-tegmark |
| 11 | the-alignment-forum | Title → "AI Alignment Forum"; authors "Various" → "LessWrong team (maintainers)"; year 2018; type blog → website (label Forum); access free; "Also used in econ/11."; verified | https://www.alignmentforum.org/about |
| 11 | README | Dated "recent landmark report" → "2023 report"; objective 2 and Suggested Order 3, 7 dated; P4 PyPhi claim dated (2.0.0rc4, October 2026; stable 1.2 is IIT 3.0); P4 Koch "(Section 02)"; Q3 extended to the unfolding argument; Q5 dated ("the LLMs of 2023"); Q8 (predictions, Brier score) added | https://pypi.org/pypi/pyphi/json |
| 12 | karl-popper | authors SEP → Stephen Thornton; year 1997 (rev. July 2026); verified | https://plato.stanford.edu/entries/popper/ |
| 12 | the-logic-of-scientific-discovery | Link added (Routledge DOI); 1959 and the 1935 original confirmed in SEP; "Routledge Classics" wording dropped (not on a fetched page); access paid; level advanced; verified | https://api.crossref.org/works/10.4324/9780203994627 ; https://plato.stanford.edu/entries/popper/ |
| 12 | the-structure-of-scientific-revolutions | access paid; level intermediate | (verified 2026-10-13) |
| 12 | falsification-and-the-methodology-of | access paid | (verified 2026-10-13) |
| 12 | science-and-pseudo-science | authors SEP → Sven Ove Hansson; year 2008 (rev. July 2025); verified | https://plato.stanford.edu/entries/pseudo-science/ |
| 12 | bayesian-epistemology | authors SEP → Hanti Lin; year 2022; verified | https://plato.stanford.edu/entries/epistemology-bayesian/ |
| 12 | philosophy-of-statistics | authors SEP → Jan-Willem Romeijn; year 2014 (rev. Oct 2025); section pointers; verified | https://plato.stanford.edu/entries/statistics/ |
| 12 | statistical-inference-as-severe-testing | access paid; level advanced | (verified 2026-10-13) |
| 12 | why-most-published-research-findings-are | access free (CC BY); *PLoS Medicine* 2(8): e124; "Also used in bio/12."; verified | https://api.crossref.org/works/10.1371/journal.pmed.0020124 |
| 12 | philosophy-and-the-sciences-introduction | access partial (free to enroll, certificate paid); level beginner; description dated. Year not shown on the page (see browser check) | https://www.coursera.org/learn/philosophy-physical-sciences |

## 2. Coverage (objective → resource / exercise / question)

🔑 = core item. P = Practice exercise, MP = mini-project, Q = Check Yourself question (numbers as they now stand).

**07 — Existential Risk and Alignment** (questions 8 → 10)

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| Core AI-risk argument; Carlsmith's six premises | Bostrom 🔑, Carlsmith | P1, MP | Q1, Q2, Q8 |
| Gabriel's alignment targets with Amodei et al. and Ngo et al. on specification gaming | Gabriel, Amodei et al., Ngo et al., Krakovna et al. (new) | P2 | Q6, Q7 |
| Takeoff dynamics | Bostrom 🔑, Yudkowsky | P3 | Q5 (new) |
| Russell's principles and the off-switch game | Russell 🔑 | P4 | Q3, Q4 (new) |
| Quantitative risk estimate engaging the skeptics and the evidence | Carlsmith, Narayanan & Kapoor, International AI Safety Report 2026, Ord | P1, MP | Q9, Q10 |

**08 — Language and Meaning** (questions 8 → 9)

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| Meaning as use, family resemblance, private language | Wittgenstein PI 🔑, SEP "Ludwig Wittgenstein" | P1, P5 | Q1, Q2, Q3, Q7 |
| Speech acts; can an AI assert or promise | Austin, Searle | P2 | Q4, Q8 |
| Gricean implicature and an LM test set | Grice | P3 | Q5 |
| Distributional vectors (Harris) | Harris | P4 | Q6 (new) |
| Bender & Koller vs. Andreas vs. Coelho Mollo & Millière | Coelho Mollo & Millière 🔑, Andreas, Bender & Koller (cross-link to Section 05) | P5, MP | Q9 |

**09 — Free Will and Agency** (questions 8 → 10)

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| Consequence Argument | SEP "Free Will", SEP "Compatibilism" | P1 | Q2 |
| Frankfurt cases and PAP | Frankfurt, SEP "Compatibilism" | P2 | Q1 |
| Libet and Schurger's accumulator | Libet et al., Schurger et al. | P3 | Q3, Q4 |
| Sapolsky vs. Mitchell, with Dennett | Elbow Room 🔑, Freedom Evolves, Sapolsky, Mitchell, Dennett & Caruso | P4, P5 | Q5, Q6, Q7 (new), Q8, Q10 |
| Allocating responsibility for an autonomous agent's act | Strawson, SEP "Compatibilism" (reasons-responsiveness), Frankfurt | P2, MP | Q9 (new) |

**10 — Eastern Philosophy and Mind** (questions restructured, 8 → 10)

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| Four Noble Truths, aggregates, dependent origination, anattā | Rahula 🔑, SEP "Buddha" | P1, P3 | Q1, Q2 |
| No-self arguments tested against Nyāya and Advaita Vedānta (sharpened) | Rahula 🔑, Adamson & Ganeri 🔑, IEP "Nyāya" (new), IEP "Advaita Vedanta" (new), Siderits | P1 (rewritten) | Q3, Q4 (new) |
| Two truths and the chariot, for persons and copyable agents | SEP "Buddha", Siderits | P2, MP | Q5, Q9 |
| Nāgārjuna's emptiness and the tetralemma | Nāgārjuna/Garfield | P4 | Q6 |
| Chinese heart-mind (*xin*) and agency: Mencius vs. the *Zhuangzi* (new) | Wong, SEP 🔑 (new), Hansen, SEP "Zhuangzi" (new) | P6 (new) | Q7 (new) |
| Reflexive awareness vs. higher-order theories; testing a meditation claim | SEP "Mind in Indian Buddhist Philosophy", Thompson (both books), Flanagan | P5, P3 | Q8 (new) |

**11 — Frontiers** (questions 8 → 9)

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| Simulation argument | Bostrom 🔑, Chalmers *Reality+* | P1, P2 | Q1 |
| Butlin et al.'s 14 indicators applied to a current system | Butlin et al. 🔑, Chalmers (LLM paper) | P3, MP | Q2, Q4, Q7 |
| IIT 4.0, φ_s, the unfolding argument | Albantakis … Tononi, Koch (Section 02) | P4 | Q3 (extended to the unfolding argument) |
| Chalmers on LLMs; Long, Sebo et al. on welfare; own credences | Chalmers, Long et al., Birch | P3, MP | Q5, Q6 |
| Calibrated, falsifiable predictions | Schwitzgebel, Long et al., Section 12 | P5 | Q8 (new) |

**12 — Philosophy of Science** (no change needed; 8 questions)

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| Popper, Kuhn, Lakatos | Godfrey-Smith 🔑, SEP "Karl Popper", Popper, Kuhn, Lakatos | P1, P2 | Q1–Q4 |
| Four demarcation criteria on a contested case | SEP "Science and Pseudo-Science" 🔑 | P1, MP | Q8 |
| Bayes factor vs. error rate; priors; optional stopping | SEP "Bayesian Epistemology", SEP "Philosophy of Statistics", Mayo | P3 | Q5 |
| Ioannidis's PPV model and the OSC replication rate | Ioannidis, Open Science Collaboration | P4 | Q6 |
| Benchmark construct validity; re-collection test | Raji et al., Recht et al. | P5 | Q7 |

Exercise source notes: every exercise in 07–12 names its resources, and each is listed in its section or names the
section that lists it. Fixed: 07 P2 (added Krakovna et al.), 08 P4–P5 (Bender & Koller now "(Section 05)"),
11 P4 (Koch "(Section 02)"), 08 P1 (SEP entry's new title).

## 3. For a browser check

Eleven items. Six books still have no link because their publisher pages could not be reached this run (no
Wiley, Harvard, Hackett, MIT Press, Yale or Princeton page appeared in search results; Crossref then rate-limited
every further lookup, and the search budget ran out). Their other fields are filled; `verified` is left empty.

| Section | Item (id) | URL to check | Why |
|---|---|---|---|
| 08 | philosophical-investigations-selections | Wiley-Blackwell page for the 4th edition (2009, ed. Hacker & Schulte) | No publisher page found; core item |
| 08 | how-to-do-things-with-words | Harvard UP page for the 2nd edition (ISBN 9780674411524), or OUP's | No publisher page found |
| 10 | buddhism-as-philosophy-an-introduction | Hackett page for the 2nd edition (2021) | Hackett pages not indexed; its catalog search was blocked. SEP "Buddha" confirms "2021, *Buddhism As Philosophy*, 2nd edition, Indianapolis: Hackett" — check whether the 2nd edition keeps the subtitle "An Introduction" |
| 10 | the-bodhisattva-s-brain-buddhism | MIT Press page (2011) | Crossref rate-limited |
| 10 | why-i-am-not-a-buddhist | Yale UP page (2020) | Crossref rate-limited |
| 11 | the-weirdness-of-the-world | Princeton UP page (2024); also whether the author hosts a free copy (would make access "partial") | Crossref rate-limited |
| 11 | are-you-living-in-a-computer-simulation | https://doi.org/10.1111/1467-9213.00309 | `access` unknown: doi.org rate-limited. If the journal page is paywalled, the author's own copy could be added as a second link |
| 12 | estimating-the-reproducibility-of | https://doi.org/10.1126/science.aac4716 | `access` unknown (is it free with a Science account?) |
| 12 | philosophy-and-the-sciences-introduction | https://www.coursera.org/learn/philosophy-physical-sciences | `year`: the page shows no launch date (earliest review November 2017) |
| 07 | 80-000-hours-ai-risk-profile | https://80000hours.org/problem-profiles/artificial-intelligence/ | Fetch refused (permission prompt unanswered). Check whether it now redirects to `/problem-profiles/loss-of-control/` (the URL blogs-and-references uses, by Cody Fenwick and Zershaaneh Qureshi) and update title, authors and date |
| 09 | an-accumulator-model-for-spontaneous | https://doi.org/10.1073/pnas.1210467109 | `access = free` set from PNAS's free-after-six-months policy, not from the page |

## 4. Decisions for the owner

1. **Section 10: broadened, not renamed.** Free, authoritative sources exist for both gaps (SEP's "Mind (Heart-Mind)
   in Chinese Philosophy" and "Zhuangzi"; IEP's "Nyāya" and "Advaita Vedanta"), and Adamson & Ganeri was already in
   the section, so the title now fits. The core path grew from one item to three (Rahula → Adamson & Ganeri → Wong),
   one per tradition; the new exercise (P6) and the reworked P1 make the new objectives practised. If you prefer a
   lighter touch, keep Rahula as the only core item and the rest still works. The section now has four titled groups.
2. **Section 08 core path.** With Bender & Koller moved to its home in 05 (as briefed), I promoted Coelho Mollo &
   Millière, the paper that answers the octopus argument, so the core path is still "classic + the LLM debate".
   Alternatives: Grice's "Logic and Conversation" or Austin. Since 05 is a prerequisite, learners meet both sides.
3. **Section 10 duplicate of *The Embodied Mind*.** The row in 10 was the same book as 04's core row and was still
   tracked despite saying "tracked once". I replaced it with an outro cross-link. Learners who ticked
   `philosophy/10/the-embodied-mind-revisited` or `philosophy/08/climbing-towards-nlu-on-meaning-form-and` will see
   those ticks under "Removed upstream" after `progress.py sync` (both books stay tracked in 04 and 05).
4. **SEP/IEP authors.** I replaced `authors = "SEP"` with the entry's author in 07–12 (binding rule: cite people).
   Sections 00–06 belong to another agent; the curriculum should use one convention. Authors were taken from each
   entry's `citation_author` metadata on 2026-10-21 (e.g. "Free Will": Christopher Franklin only; "Ludwig
   Wittgenstein": Anat Matar only), so they may differ from older citations of the same entries.
5. **Edition years.** For three books the linked page is a later edition and no fetched page confirmed the first-edition
   year, so `year` is now the linked edition's: *Superintelligence* 2016 (was 2014), *Freedom Evolves* 2004 (was 2003),
   *What the Buddha Taught* 1969 (was 1959). If you would rather show "original (edition)", a browser check of the
   first editions would allow `2014 (pbk. 2016)` etc.
6. **Titles that follow the linked edition.** *Human Compatible* now carries the Penguin subtitle "AI and the Problem of
   Control" (as in `philosophy/extras.toml`); the US Viking edition's subtitle differs. *Life 3.0*'s subtitle is
   "…in the Age of Artificial Intelligence" (it was "…of AI").
7. **New Check Yourself questions** (07 Q4–Q5; 08 Q6; 09 Q7, Q9; 10 Q4, Q7, Q8 and merged Q1; 11 Q8 and extended Q3)
   need answers in pass 3. Numbering shifted in 07–11.
8. **Cross-curriculum rows kept with "Also used in …":** Concrete Problems in AI Safety and BlueDot (econ/11), the AI
   Alignment Forum (econ/11), Ioannidis 2005 (bio/12). Their metadata here is now exact; econ/11's copies still say
   "Dario Amodei et al.", link BlueDot's home page, and type the forum as a blog — worth aligning in that section.
9. **Advocacy labels.** The 80,000 Hours profile is now labeled advocacy; *Life 3.0* is labeled speculative. Balance in
   07 is unchanged (Narayanan & Kapoor and the International AI Safety Report stay on the path).
