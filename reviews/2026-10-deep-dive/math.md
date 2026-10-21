# Mathematics — Review

> **Deep-dive review, October 2026** · curriculum: [`math/`](../../math/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict

The math curriculum lists canonical texts in a sensible order that builds intuition first: 3Blue1Brown, then MIT/Harvard courses, then Axler, Abbott, Boyd, Cover & Thomas and Strogatz. Many entries are free, and most metadata is correct. Its weakness is that it was written as "math for ML plus pure-math electives", not as math for an electrical/embedded engineer. Before this pass it had no complex analysis, no Fourier analysis or signals and systems, no numerical methods, no estimation or filtering, no number theory for the Bitcoin cryptography, and no proof assistants. A handful of rows were plainly wrong: a course row that mixed three different courses, misattributed videos, a wrong first author, wrong titles, and a "free" book that isn't free. The "Frontiers" section claimed to cover the math–AI boundary but had nothing after 2022, and it described Wolfram's speculative program as an established "fundamental mathematical concept". **Overall grade: B− as found, about B after this pass.** The single most important improvement is to give the curriculum an engineering-math spine: complex analysis, then signals and systems, then random signals and estimation, then numerics. This meant creating a Signals & Systems section and splitting the README path into core and elective sections. **Update:** both are now done — Sections 12–14 were created in this review, and the README has a Core/Elective route.

## Scorecard

Scores reflect the state as found (before this pass).

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 Mathematical Thinking | 4 | 4 | 3 | 4 | 4 | B+ | Right core (Velleman/Hammack/Pólya); lacked proof assistants and engineering-flavored discrete math |
| 01 Linear Algebra | 3 | 5 | 4 | 4 | 4 | B+ | Canonical intuition→computation→proof ramp; no applied least squares, no numerical LA |
| 02 Calculus and Analysis | 3 | 5 | 4 | 3 | 4 | B | Strong analysis core; complex analysis completely missing (biggest EE gap) |
| 03 Probability and Statistics | 3 | 3 | 3 | 4 | 3 | B− | Excellent core courses; wrong title/edition/free flags; no applied-Bayes on-ramp or estimation |
| 04 Optimization | 4 | 2 | 3 | 3 | 4 | C+ | Right texts; one row mixed three different courses, and the course row claimed videos the site doesn't host |
| 05 Information Theory | 4 | 4 | 3 | 4 | 4 | B | Lovely arc (Olah→Shannon→Cover & Thomas→MacKay); no post-2006 text |
| 06 Graph Theory and Combinatorics | 3 | 4 | 4 | 4 | 3 | B− | Solid graph texts; thin combinatorics; ML papers duplicate ml/13 |
| 07 Differential Equations | 4 | 4 | 4 | 4 | 4 | B+ | Best section; lacked the control/state-space view and a gentle SDE text |
| 08 Abstract Algebra | 3 | 2 | 4 | 4 | 4 | C+ | Good core (Pinter); misattributed videos, authorless placeholder row, no number theory |
| 09 Topology and Geometry | 4 | 4 | 4 | 3 | 3 | B | Inspired picks (Needham VDGF, Tokieda); wrong paper title; heavy for this learner |
| 10 Causal Inference | 4 | 4 | 3 | 4 | 4 | B | Well-balanced Pearl + potential outcomes; nothing after 2021 |
| 11 Category Theory and Frontiers | 2 | 2 | 2 | 3 | 2 | C− | "Frontiers" had no AI-for-math; Wolfram oversold; two metadata errors; low priority for the intended learner |

## Section-by-section

### 00 — Mathematical Thinking
- **Strengths:** Velleman, Hammack and Pólya are the right core. Devlin's course is a good bridge from computational to proof-based math. There are free options throughout, and the order is sensible.
- **Problems:** ✔ Hammack year 2013 → 2018 (3rd ed.). ✔ Eccles year 2007 → 1997. ✔ Eccles was missing from PROGRESS. ✱ Bazett and Eccles are still not in Suggested Order.
- **Missing:** A proof assistant as a feedback loop for learning proof (Lean 4 is the major 2023–2026 development). Discrete math with an engineering/CS slant, including elementary number theory as the on-ramp to cryptography. A steady source of practice problems (Project Euler added to blogs-and-references).
- **Added:**
  - Natural Number Game (Lean 4) — Kevin Buzzard, Jon Eugster — 2023
  - The Mechanics of Proof — Heather Macbeth — 2024
  - MIT 6.042J Mathematics for Computer Science — Albert Meyer, Adam Chlipala (text: Lehman, Leighton & Meyer) — 2015

### 01 — Linear Algebra
- **Strengths:** 3B1B → 18.06 → Axler is the canonical ramp. Axler 4th ed. (2024, free) and Strang 6th ed. (2023) are current.
- **Problems:** ✱ Meyer has a SIAM 2nd edition. I didn't update the year because the web budget ran out before I could confirm it. ✱ Strang's book, Hefferon, Meyer and Khan are not in Suggested Order. ✔ Meyer and Khan were missing from PROGRESS. ✱ 3B1B and MML ch. 2–4 duplicate ml/01, which now links back here.
- **Missing:** Applied least squares, estimation and control. Numerical linear algebra (conditioning, floating-point stability, how solvers and the SVD are computed).
- **Added:**
  - Introduction to Applied Linear Algebra (VMLS) — Stephen Boyd, Lieven Vandenberghe — 2018
  - Numerical Linear Algebra (25th-anniversary ed.) — Lloyd N. Trefethen, David Bau III — 2022

### 02 — Calculus and Analysis
- **Strengths:** Abbott is the right core analysis text. Axler's MIRA is free for measure theory. MIT 18.01/18.02 give computational fluency.
- **Problems:** ✱ Spivak comes after Abbott in the order. Spivak is a rigorous calculus book, so it belongs before or instead of 18.01 for a proof-ready learner. ✱ Hubbard & Hubbard is not in the order. ✔ Khan and Active Calculus were missing from PROGRESS. ✱ There is no matrix/vector calculus resource here (ml/01 has Parr & Howard).
- **Missing:** **Complex analysis.** It was entirely absent, yet it is the math behind phasors, Laplace and z-transforms, poles and zeros, and frequency response.
- **Added:**
  - Visual Complex Analysis (25th-anniversary ed.) — Tristan Needham — 2023
  - MIT 18.04 Complex Variables with Applications — Jeremy Orloff — 2018

### 03 — Probability and Statistics
- **Strengths:** Stat 110, Blitzstein & Hwang (free 2nd ed.), Wasserman and MIT 6.041 are an excellent core.
- **Problems:**
  - ✔ Ross's book is titled *Introduction to Probability and Statistics for Engineers and Scientists*. The old title, *Probability and Statistics for Engineers and Scientists*, is Walpole et al.'s book.
  - ✔ Ross *Introduction to Probability Models* updated 2019 → 13th ed. 2023.
  - ✔ The BDA3 PDF is free (non-commercial) but wasn't marked free.
  - ✔ Lawler was labelled "Book (Free)" with no link and no year; it is a paid 2006 CRC book.
  - ✔ Lawler was missing from PROGRESS and from the order.
  - ✱ The official Stat 110 site now appears to be stat110.hsites.harvard.edu, which also links the free book. Left for the URL audit.
- **Missing:** An applied-Bayesian on-ramp (BDA is a reference, not a first book). Estimation and filtering (Kalman). Random signals, power spectral density (PSD) and detection theory (→ Section 12, now created). Measurement statistics such as uncertainty propagation and design of experiments (worth a later look for a test-and-measurement founder).
- **Added:**
  - Statistical Rethinking (2024 course; book 2nd ed. 2020) — Richard McElreath — 2024
  - Kalman and Bayesian Filters in Python — Roger Labbe — 2015

### 04 — Optimization
- **Strengths:** Boyd & Vandenberghe, Nocedal & Wright and Beck form the canonical spine.
- **Problems:**
  - ✔ The row "MIT 6.079 … Lieven Vandenberghe" linked to Stanford's SEE EE364A. MIT 6.079 was actually taught by Boyd & Parrilo and has notes only. I corrected the row to the SEE video course it really links (Boyd, 2008, 19 lectures).
  - ✔ The 🔑 EE364a row said "Video lectures", but the current class site offers recordings to enrolled students only. The description now says so.
  - ✔ The courses/README EE364a row now points to the SEE videos.
  - ✔ Beck was added to the order.
  - ✱ The order is ML-first (MML ch. 7 and Ruder before Boyd). That suits ML; an engineer should start with Boyd.
  - ✱ Adam (2014) and Ruder (2016) are dated as the "modern" view; AdamW and newer optimizers belong in ml.
- **Missing:** Derivative-free, black-box and multi-objective design optimization. LP/MILP.
- **Added:**
  - Algorithms for Optimization — Mykel Kochenderfer, Tim Wheeler — 2019

### 05 — Information Theory
- **Strengths:** The Olah → Shannon → Cover & Thomas → MacKay arc is very good.
- **Problems:** ✔ The mathematicalmonk entry was titled "(Khan Academy style)"; the playlist is just "Information Theory". ✔ The MIT 6.441 instructor and year were missing (Yury Polyanskiy, 2016). ✔ 6.441 was added to the order. ✱ Jordan et al. (1999) is a dated entry point for variational inference.
- **Missing:** A modern (post-2006) textbook and information-theoretic tools for learning and statistics.
- **Added:**
  - Information Theory: From Coding to Learning (free draft) — Yury Polyanskiy, Yihong Wu — 2024

### 06 — Graph Theory and Combinatorics
- **Strengths:** Diestel, West, Godsil & Royle and Spielman are solid, and the spectral angle is good for ML.
- **Problems:** ✔ Diestel 5th ed. (2017) → 6th ed. (Springer GTM 173, ©2025). The online version is a free *preview* of the main text, now worded accordingly. ✔ West was missing from PROGRESS. ✱ West is not in the order. ✱ The GCN and Geometric Deep Learning papers duplicate ml/13.
- **Missing:** Combinatorics is thin (no generating functions, nothing like *Concrete Mathematics*). Low priority for the intended learner.
- **Added:** nothing needed (edition fix only).

### 07 — Differential Equations
- **Strengths:** Strogatz, 18.03 and 3B1B make the best possible dynamics core. PDE (Strauss) and SDE (Øksendal) are covered, with good links to Neural ODEs and S4.
- **Problems:** ✔ Strogatz updated to the 3rd ed. (CRC, 2024). ✔ Boyce/DiPrima/Meade updated to the 12th ed. (2021). ✱ Arnold and Boyce are not in the order. ✱ The Strogatz book and lectures are duplicated in physics/10.
- **Missing:** The control/state-space/frequency-response view of linear ODEs, which is core EE. A gentle SDE book before Øksendal. Numerical ODE integration (→ Section 14, now created).
- **Added:**
  - Feedback Systems (2nd ed.) — Karl J. Åström, Richard M. Murray — 2021
  - Applied Stochastic Differential Equations — Simo Särkkä, Arno Solin — 2019

### 08 — Abstract Algebra
- **Strengths:** Pinter is the right self-study core. Judson is free. There is a good visual on-ramp.
- **Problems:**
  - ✔ The "Visual Group Theory" video series was attributed to Nathan Carter. The playlist is Matthew Macauley's lecture series based on Carter's book (oEmbed author "Professor Macauley").
  - ✔ The "Equivariant Neural Networks | — | — | —" row was an authorless placeholder. I turned it into the canonical paper (Cohen & Welling 2016, G-CNNs), kept its pointer to ML §13, and made that pointer a working relative link.
  - ✔ Lang and the placeholder row were missing from PROGRESS.
  - ✱ Herstein is described as a "graduate text". It is normally used as an upper-undergraduate text (not verified within budget).
  - ✱ The Gross playlist is a third-party re-upload (channel "It's so blatant") and may disappear.
- **Missing:** Number theory and finite fields in use (cryptography, error-correcting codes and CRCs). The section's own "Why" promises these but had no resource.
- **Added:**
  - An Introduction to Mathematical Cryptography (2nd ed.) — Jeffrey Hoffstein, Jill Pipher, Joseph H. Silverman — 2014

### 09 — Topology and Geometry
- **Strengths:** Needham's VDGF as 🔑 is an inspired choice. Tokieda's lectures and the TDA connection are good.
- **Problems:** ✔ Carlsson's paper is "Topology and Data" (Bull. AMS 46(2), 2009), not "Topological Data Analysis". ✔ The Albin lectures were missing from PROGRESS. ✱ Albin is not in the order, and its playlist is a third-party upload. ✱ Lee and do Carmo are heavy for this learner.
- **Missing:** Nothing essential for the intended learner. physics/05 (general relativity) depends on this section.
- **Added:** nothing needed.

### 10 — Causal Inference
- **Strengths:** The path from popular book (Book of Why) to primer to *Causality*, plus Hernán & Robins and Brady Neal, is well balanced between the graph and potential-outcomes schools.
- **Problems:** ✔ "Hernan" → "Hernán" (table, order, PROGRESS). ✔ Dasgupta was missing from PROGRESS. ✱ Dasgupta et al. (2019, meta-RL) is a weak, niche pick. ✱ Peters et al. may be open access (it has an OAPEN record), but I couldn't confirm a PDF/licence, so it is unchanged.
- **Missing:** Post-2021 work (e.g., double/debiased ML) and quasi-experimental designs (difference-in-differences, regression discontinuity, instrumental variables). Low priority for the intended learner.
- **Added:** nothing needed.

### 11 — Category Theory and Frontiers
- **Strengths:** Seven Sketches (free) is the right applied category theory text, and its signal-flow-graph and circuit chapters suit an EE. Riehl and Milewski are good.
- **Problems:**
  - ✔ Mac Lane year 1978 → 1998 (2nd ed.; 1st ed. 1971).
  - ✔ The first author of "Categorical Foundations of Gradient-Based Learning" is G.S.H. Cruttwell, not Gavranović (ESOP 2022).
  - ✔ The **Wolfram entry** (the July 2026 addition) called "computational irreducibility" a "fundamental mathematical concept". It linked the ruliad to "foundational questions about mathematical structure" and told the reader to approach it "after category theory gives you a framework". That is an invented dependency, and the framing implied established status. I rewrote it to state plainly that it is speculative and not accepted mathematics or physics, and that it has no quantitative, testable predictions (evidence: Scientific American 2020; Aaronson 2002). I paired it with Aaronson's critical review and marked it optional in the order. The entry was not deleted.
  - ✔ Spivak CT4S, Cruttwell et al. and Wolfram were missing from PROGRESS.
  - ✱ The README says this section "covers the latest developments at the math–AI boundary"; before this pass it had nothing after 2022.
  - ✱ The working copy has a single baseline commit, so I assessed the July 2026 change as it stands rather than through git history.
- **Missing:** AI-for-math: machine-checked proof (Lean/Mathlib) and AI-driven discovery (AlphaProof/AlphaEvolve). This is the actual frontier for a learner who uses AI tools daily.
- **Positioning:** Category theory is correctly placed last, but for the intended learner it should be explicitly **elective / low priority**. It has little payoff for embedded work, and the ML connections (Backprop as Functor, Cruttwell et al.) are research-level. The most useful items in this section are now Mathematics in Lean and the 2025 discovery paper.
- **Added:**
  - Book Review: "A New Kind of Science" — Scott Aaronson — 2002
  - Mathematics in Lean — Jeremy Avigad, Patrick Massot — 2025
  - Mathematical Exploration and Discovery at Scale — Georgiev, Gómez-Serrano, Tao, Wagner — 2025

### books/README.md
- **Strengths:** A clear table with Free / Level / Section columns.
- **Problems:** ✔ Blitzstein & Hwang and BDA were marked "Paid" with no link; both are free and now linked. ✔ Years corrected for Hammack (2018), Diestel (2025) and Strogatz (2024). ✱ Rows 28–29 (Rudin, Jaynes) were appended out of section order. ✱ No stated selection criterion: it's a subset of section books, and some 🔑 books from sections are missing. ✱ The intro says "Start with Velleman and 3Blue1Brown", which mixes in a non-book.
- **Added:** rows 30–35 — VMLS, Trefethen & Bau, Visual Complex Analysis, Statistical Rethinking, Feedback Systems, Hoffstein/Pipher/Silverman.

### courses/README.md
- **Problems:** ✔ EE364a pointed at the class site, which has no public videos; it now points to the SEE recordings, with the class site in Notes. ✱ The list omits several section courses (6.041, 6.441, Gross, Tokieda, Albin, Herke, Bazett). That's fine for a "highlights" list, but the file doesn't say so.
- **Added:** MIT 6.042J, MIT 18.04, Statistical Rethinking (2024).

### blogs-and-references/README.md
- **Strengths:** Tao, Math3ma, Quanta, MSE/MathOverflow and OEIS are good picks.
- **Problems:** ✱ The Matrix Cookbook is duplicated from Section 01. ✱ The only problem source was AoPS, which is competition-oriented.
- **Added:** Project Euler.

### PROGRESS.md
- **Problems:**
  - ✔ 15 section items were missing from the tracker: Eccles, Meyer, Khan LA, Khan Multivariable, Active Calculus, Lawler, SEE EE364A, West, Lang, the equivariant row, Albin, Dasgupta, Spivak CT4S, Cruttwell et al., and Wolfram. A script now confirms every section table maps 1:1 to its PROGRESS block.
  - ✔ Three title/name fixes (Ross, Carlsson, Hernán).
  - ✱ "Books (supplementary)" duplicates section lines (Velleman, Axler, Abbott…), so the same item is ticked in two places. Suggest keeping only the cross-cutting books (GEB, Courant & Robbins, MML) there.

### README.md
- **Problems:**
  - ✱ "Work through the numbered sections in order" treats 12 sections as equal. The intended learner needs a core/elective split (see Structural observations).
  - ✔ "Connections to Other Curricula" omitted Bitcoin and PCB; I added rows for Bitcoin (08, 13, 03) and PCB (02, 07, 12, 14) when creating 12–14. ✱ A Philosophy row (→ 00, 11) is still missing.
  - ✱ The "Keeping Current" claim was overstated; it is now supported by the 2025 additions.
  - No verified errors needed fixing. The learning-path list is unchanged because no sections were created.

## Corrections made

| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| math/00-mathematical-thinking/README.md:15 | Book of Proof — 2013 | 2018 (3rd edition) | https://www.people.vcu.edu/~rhammack/BookOfProof/ |
| math/00-mathematical-thinking/README.md:16 | Eccles — 2007 | 1997 (Cambridge UP) | https://abebooks.com/9780521597180/Introduction-Mathematical-Reasoning-Numbers-Sets-0521597188/plp |
| math/03-probability-and-statistics/README.md:24 | "Probability and Statistics for Engineers and Scientists" (Ross) | "Introduction to Probability and Statistics for Engineers and Scientists" | https://shop.elsevier.com/books/introduction-to-probability-and-statistics-for-engineers-and-scientists/ross/978-0-12-824346-6 |
| math/03-probability-and-statistics/README.md:26 | BDA — "Book" | "Book (Free)" + note on free 3rd-ed. PDF | https://sites.stat.columbia.edu/gelman/book/ |
| math/03-probability-and-statistics/README.md:27 | Ross, Intro to Probability Models — 2019 | 2023 (13th ed.) | https://shop.elsevier.com/books/introduction-to-probability-models/ross/978-0-443-18761-2 |
| math/03-probability-and-statistics/README.md:30 | Lawler — "Book (Free)", year "—" | "Book", 2006 (2nd ed.) | https://www.routledge.com/Introduction-to-Stochastic-Processes/Lawler/p/book/9781584886518 |
| math/04-optimization/README.md:21 | EE364a: "Video lectures accompanying the textbook" | Class site: slides/homework/exams; recordings for enrolled students only → use SEE videos | https://web.stanford.edu/class/ee364a/ |
| math/04-optimization/README.md:25 | "MIT 6.079: Introduction to Convex Optimization — Lieven Vandenberghe" linking to see.stanford.edu | "Stanford Engineering Everywhere — EE364A Convex Optimization I (video lectures) — Stephen Boyd — 2008" (same link) | https://ocw.mit.edu/courses/6-079-introduction-to-convex-optimization-fall-2009/ (6.079 = Boyd & Parrilo, notes only); https://see.stanford.edu/Course/EE364A ; https://videolectures.net/stanfordee364aw08_convex_optimization1 |
| math/05-information-theory/README.md:23 | "Information Theory (Khan Academy style)" | "Information Theory (playlist)" | https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLE125425EC837021F&format=json |
| math/05-information-theory/README.md:24 | MIT 6.441 — author "—", year "—" | Yury Polyanskiy, 2016 (noted: no videos) | https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/ |
| math/06-graph-theory-and-combinatorics/README.md:20 | Diestel — 2017, "freely available" | 2025 (6th ed., GTM 173); "main text free to read online as a preview" | https://link.springer.com/book/10.1007/978-3-662-70107-2 ; https://www.diestel-graph-theory.com/basic.html |
| math/07-differential-equations/README.md:20 | Strogatz — 2015 | 2024 (3rd ed.) | https://tenlong.com.tw/products/9780367026509 |
| math/07-differential-equations/README.md:23 | Boyce, DiPrima, Meade — 2017 | 2021 (12th ed.) | https://www.goodreads.com/book/show/59383860-elementary-differential-equations-and-boundary-value-problems |
| math/08-abstract-algebra/README.md:23 | Visual Group Theory (videos) — Nathan Carter | Matthew Macauley (lectures based on Carter's book) | https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLwV-9DG53NDxU337smpTwm6sef4x-SCLv&format=json |
| math/08-abstract-algebra/README.md:26 | Placeholder "Equivariant Neural Networks — — — —" | Cohen & Welling, "Group Equivariant Convolutional Networks" (2016) + relative link to ml/13 | https://arxiv.org/abs/1602.07576 |
| math/09-topology-and-geometry/README.md:29 | "Topological Data Analysis" (Carlsson) | "Topology and Data" (Bull. AMS) | https://api.crossref.org/works/10.1090/S0273-0979-09-01249-X |
| math/10-causal-inference/README.md:23, 36 | Miguel Hernan | Miguel Hernán | https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/ |
| math/11-category-theory-and-frontiers/README.md:26 | Mac Lane — 1978 | 1998 (2nd ed.; 1st ed. 1971) | https://en.wikipedia.org/wiki/Categories_for_the_Working_Mathematician |
| math/11-category-theory-and-frontiers/README.md:28 | "Bruno Gavranović et al." | "G.S.H. Cruttwell, Bruno Gavranović et al." | https://arxiv.org/abs/2103.01931 ; https://cris.unibo.it/handle/11585/903819 (ESOP 2022) |
| math/11-category-theory-and-frontiers/README.md:30 | Wolfram: "Computational irreducibility as a fundamental mathematical concept … connects to foundational questions about mathematical structure" | Clearly labelled speculative / not accepted math or physics; no testable predictions; read with Aaronson's review | https://www.scientificamerican.com/article/physicists-criticize-stephen-wolframs-theory-of-everything ; https://arxiv.org/abs/quant-ph/0206089 |
| math/11-category-theory-and-frontiers/README.md:48 | "Best approached after category theory gives you a framework for thinking about structure and composition" | "Optional and speculative … read Aaronson's review alongside" | same as above |
| math/books/README.md:8 | Hammack — 2013 | 2018 | https://www.people.vcu.edu/~rhammack/BookOfProof/ |
| math/books/README.md:16 | Blitzstein & Hwang — Paid, no link | Free, linked to official Stat 110 site (free 2nd ed.) | https://stat110.hsites.harvard.edu/ |
| math/books/README.md:17 | BDA — Paid, no link | Free (non-commercial PDF), linked | https://sites.stat.columbia.edu/gelman/book/ |
| math/books/README.md:21 | Diestel — 2017 | 2025 | https://link.springer.com/book/10.1007/978-3-662-70107-2 |
| math/books/README.md:22 | Strogatz — 2015 | 2024 | https://tenlong.com.tw/products/9780367026509 |
| math/courses/README.md:14 | EE364a → class site (no public videos) | → SEE recordings; class site linked in Notes | https://see.stanford.edu/Course/EE364A ; https://web.stanford.edu/class/ee364a/ |
| math/PROGRESS.md (§03, §09, §10) | Ross title; "Carlsson — Topological Data Analysis"; "Hernan" | Corrected to match the section tables | as above |
| math/PROGRESS.md (§00–§11) | 15 section items untracked | Added (now 1:1 with section tables) | — |
| Suggested Order (03, 04, 05, 08) | Lawler, Beck, MIT 6.441, Carter's book missing | Added | — |

Broken internal links: none existed. I added one new cross-curriculum relative link (math/08 → ml/13) and verified that all relative links in math/ resolve.

## Proposed new sections — CREATED in this review

All three proposals below were approved and have been created as appended sections, so nothing was renumbered. Each follows the merged section format: Why / Prerequisites / 🎯 Learning Objectives / Resources / Suggested Order / 🛠️ Practice (5 exercises plus a mini-project) / ✅ Check Yourself (8 questions).

| Section | Path | Take after | Status | Mini-project |
|---|---|---|---|---|
| A | `math/12-fourier-analysis-signals-and-systems/README.md` | 07 | Core | FFT-based ADC dynamic test (SINAD, ENOB, SFDR) |
| B | `math/13-number-theory-and-cryptography/README.md` | 08 | Core for btc | A tested secp256k1 + BIP-340 library |
| C | `math/14-numerical-methods-and-scientific-computing/README.md` | 07 or 12 | — | Mini-SPICE, a transient circuit simulator from scratch |

- **Resources:** only resources verified earlier in this run were used (7 in 12, 8 in 13, 6 in 14). No new web calls were made.
- **Moved in from this pass's earlier additions:**
  - Trefethen & Bau: 01 → 14.
  - Hoffstein, Pipher & Silverman: 08 → 13.
  - Both source sections keep a Suggested Order pointer to the new section, and their PROGRESS lines and books/README "Section" column moved with them.
  - Nothing that was in master was deleted.
- **Kept where they are, cross-referenced from the new sections:**
  - Needham's VCA and MIT 18.04 stay in 02; Feedback Systems stays in 07 (both feed 12).
  - Labbe stays in 03 (feeds 12).
  - Corbellini, *Programming Bitcoin*, and *Mastering Bitcoin* stay in btc/01. Section 13 links `../../btc/01-cryptography-foundations/README.md` instead of duplicating them.
- **Cross-links:**
  - 14 links `../../physics/06-computational-physics/README.md`.
  - 12 links physics/01 for the 3Blue1Brown Fourier videos.
  - 12's mini-project names the PCB curriculum's analog, mixed-signal and precision-measurement section in plain text only, because that section was still being created when I wrote this.
- **Computed values:** every "you should get X" value in the new exercises was computed locally (NumPy 2.5 / SciPy 1.18) before being stated. Examples:
  - window ENBW and scalloping figures;
  - Kaiser (89 taps) vs. Parks–McClellan (68) and Butterworth/Chebyshev/elliptic orders 21/10/7;
  - direct-form vs. SOS coefficient word length (~24 vs. ~12 bits);
  - ideal 12-bit ENOB 12.00, and ≈ 2 with a rectangular window on a non-coherent capture;
  - matched-filter losses of 0.89 and 0.91 dB;
  - secp256k1 parameter consistency (G on the curve, n·G = O, p and n prime) and an exact reproduction of the BIP-340 test-vector-0 public key and 64-byte signature by an independent implementation;
  - toy prime-order curves checked by N·P = O and solved by BSGS;
  - 561's 320 Fermat liars vs. 10 strong liars;
  - float32 timer drift (991.14 s), Welford vs. naive variance, Hilbert/Wilkinson errors, stiff-solver evaluation counts, and LC-tank damping under backward Euler.
- **README:** the learning path now lists 12–14 with their positions, plus a compact "Recommended Route (engineering focus)" table with Core, Core-for-Bitcoin and Electives tracks. The "Connections" table gained Bitcoin and PCB rows.
- **PROGRESS:** added `## Section 12/13/14` blocks before "Books", each with one checkbox per resource and the practice, mini-project and Check Yourself lines. A script confirms PROGRESS ↔ section-table parity for all 15 sections.
- **books / courses:**
  - books/README: added rows 36–38 (Smith's DSP Guide, Stein's ENT, Driscoll & Braun).
  - courses/README: added rows 20–23 (RES.6-007, EE261, 6.011, 18.335J).
- **Still unverified, so not added:** the print year of Polyanskiy & Wu, the publication years of Prandoni & Vetterli and of Driscoll & Braun (both shown as "—"), the Oppenheim & Willsky edition, Meyer's 2nd-edition year, Herstein's level, Peters et al.'s open-access status, and Duchi's year.

The original proposal text follows for reference.

### A. Fourier Analysis, Signals & Systems (highest priority)
- **Status:** ✔ created as `math/12-fourier-analysis-signals-and-systems/README.md`.
- **Position:** Directly after 07 Differential Equations. It needs 01, 02 (now including complex analysis) and 07 (Laplace, LTI ODEs); the random-signals part also needs 03. For the intended learner this belongs on the core path, not as an elective. The reviewer can either renumber 08–11 or append it as 12 and mark it core in the README.
- **Why:** The intended learner's daily work is analog front ends, ADC sampling, filtering, sensor signal chains, and test-and-measurement hardware. Fourier analysis, sampling and aliasing, LTI systems, z-transforms, filter design, noise power spectral density, and detection theory (the trade-off between false triggers and missed detections) are the math such an engineer uses most. Today the whole repo has only two 3Blue1Brown Fourier videos (physics/01), plus Laplace transforms inside 18.03.
- **Outline:**
  1. Fourier series and transform (intuition, then theory)
  2. LTI systems, convolution, impulse and frequency response, Laplace/Bode
  3. Sampling theorem, aliasing, DFT/FFT, windowing, z-transform
  4. FIR/IIR filter design, multirate
  5. Random signals: autocorrelation, PSD, noise through LTI systems, Wiener filtering
  6. Detection and estimation: hypothesis testing, matched filters, ROC (ties to Labbe/Kalman in 03)
  7. Optional rigor: Stein & Shakarchi
- **Resources (verified):**
  1. MIT RES.6-007 Signals and Systems — Alan V. Oppenheim — 2011. Video lectures; readings from Oppenheim & Willsky, *Signals and Systems*. https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/
  2. Stanford EE261 The Fourier Transform and its Applications — Brad Osgood — SEE, 30 video lectures plus a free course reader (2007 materials). https://see.stanford.edu/Course/EE261
  3. The Scientist and Engineer's Guide to Digital Signal Processing — Steven W. Smith — free full text (©1997–2011). https://www.dspguide.com/
  4. Signal Processing for Communications — Paolo Prandoni, Martin Vetterli — free PDF. https://www.sp4comm.org/
  5. MIT 6.011 Signals, Systems and Inference — George Verghese, Alan Oppenheim, Peter Hagelstein — 2018. Covers random processes, PSD, Wiener filtering, LMMSE estimation, hypothesis testing and matched filters (notes and problem sets, no video). https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
  6. MIT 6.341 Discrete-Time Signal Processing — Alan V. Oppenheim — 2005. Text: Oppenheim, Schafer & Buck, *Discrete-Time Signal Processing*, 2nd ed., 1999. https://ocw.mit.edu/courses/6-341-discrete-time-signal-processing-fall-2005/
  7. Fourier Analysis: An Introduction — Elias M. Stein, Rami Shakarchi — Princeton, 2003. https://press.princeton.edu/books/hardcover/9780691113845/fourier-analysis
  - Cross-references: Needham VCA and MIT 18.04 (02), Åström & Murray (07), Labbe (03), and the 3B1B Fourier videos (physics/01).

### B. Number Theory, Finite Fields & Elliptic Curves (mathematical cryptography)
- **Status:** ✔ created as `math/13-number-theory-and-cryptography/README.md` (HPS moved here from 08; Corbellini and Song cross-referenced via btc/01).
- **Position:** After 08 Abstract Algebra (needs groups, rings, fields). It is an elective in general but core for the btc curriculum. Hoffstein/Pipher/Silverman is already seeded in 08 and would move here.
- **Why:** btc/01 lists ECC/secp256k1, ECDSA/Schnorr and SHA-256 as "Concept" rows. It now has Corbellini and Song for the hands-on side, but no number-theory or finite-field text. math/08 claims "finite fields underpin cryptography" but had no number theory. Finite fields also underlie the CRCs and Reed–Solomon codes used in embedded communications.
- **Outline:**
  1. Elementary number theory: gcd/Bézout, modular arithmetic, CRT, Fermat/Euler, primality
  2. Finite fields GF(p) and GF(2ⁿ), polynomial arithmetic (link to CRCs)
  3. Discrete log, Diffie–Hellman, RSA, signatures
  4. Elliptic curves: group law, curves over 𝔽ₚ, ECDLP, ECDSA/Schnorr, secp256k1
  5. Build it: finite-field and EC arithmetic in Python
  6. Optional: security definitions (Boneh–Shoup), arithmetic of elliptic curves (Silverman–Tate)
- **Resources (verified):**
  1. A Computational Introduction to Number Theory and Algebra — Victor Shoup — 2nd ed., Cambridge, 2008; free PDF. https://shoup.net/ntb/
  2. Elementary Number Theory: Primes, Congruences, and Secrets — William Stein — Springer, 2008; free legal PDF. https://wstein.org/ent/
  3. A Friendly Introduction to Number Theory — Joseph H. Silverman — 4th ed., Pearson, 2012. https://www.math.brown.edu/johsilve/frint.html
  4. An Introduction to Mathematical Cryptography — Hoffstein, Pipher, Silverman — 2nd ed., Springer, 2014 (added to 08). https://link.springer.com/book/10.1007/978-1-4939-1711-2
  5. Elliptic Curve Cryptography: a gentle introduction (4-part series: group law → finite fields/ECDLP → ECDH/ECDSA → attacks) — Andrea Corbellini — 2015. https://andrea.corbellini.name/2015/05/17/elliptic-curve-cryptography-a-gentle-introduction/ — already in btc/01; cross-reference it.
  6. Programming Bitcoin (Ch. 1 "Finite Fields" → elliptic curves → ECC, in Python) — Jimmy Song — O'Reilly, 2019. https://github.com/jimmysong/programmingbitcoin — already in btc/01; cross-reference it.
  7. Elliptic Curves: Number Theory and Cryptography — Lawrence C. Washington — 2nd ed., CRC, 2008. https://www.routledge.com/Elliptic-Curves-Number-Theory-and-Cryptography-Second-Edition/Washington/p/book/9781420071467
  8. A Graduate Course in Applied Cryptography (Ch. 15 ECC and pairings; signatures) — Dan Boneh, Victor Shoup — v0.6, Jan 2023, free download. https://toc.cryptobook.us/
  - Optional: *Understanding Cryptography* 2nd ed. — Paar, Pelzl, Güneysu — Springer, 2024. https://link.springer.com/book/10.1007/978-3-662-69007-9
  - Optional: *Rational Points on Elliptic Curves* 2nd ed. — Silverman & Tate — Springer, 2015. https://link.springer.com/book/10.1007/978-3-319-18588-0

### C. Numerical Methods & Scientific Computing
- **Status:** ✔ created as `math/14-numerical-methods-and-scientific-computing/README.md` (Trefethen & Bau moved here from 01; physics/06 cross-linked).
- **Position:** After 07, or after the proposed Signals section (needs 01, 02, 07). Coordinate with physics/06 Computational Physics (Newman, Numerical Recipes, 18.085, and now FEniCSx). The math section should own floating point, conditioning and stability, and generic algorithms; physics/06 should keep the physics applications.
- **Why:** The intended learner writes firmware (fixed and floating point on MCUs), Python tooling, calibration fits and simulations. Numerical error and stable algorithms matter to them more often than topology does. Coverage was only Nocedal & Wright (04), plus Trefethen & Bau, which I added to 01.
- **Outline:**
  1. Floating point and error analysis (including fixed-point on MCUs)
  2. Conditioning and backward stability
  3. Linear systems and least squares, numerically
  4. Nonlinear equations
  5. Interpolation, approximation, quadrature
  6. ODE integrators (Runge–Kutta, stiffness, adaptive step)
  7. The FFT as an algorithm
  8. Automatic differentiation
  9. Intro to PDE discretization (→ physics/06)
- **Resources (verified):**
  1. What Every Computer Scientist Should Know About Floating-Point Arithmetic — David Goldberg — ACM Computing Surveys, 1991 (free reprint). https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html
  2. Fundamentals of Numerical Computation — Tobin A. Driscoll, Richard J. Braun — free online edition in Julia, MATLAB and Python versions. https://fncbook.com/
  3. MIT 18.335J Introduction to Numerical Methods — Steven G. Johnson — 2019. Floating point, backward error, conditioning and stability, dense and iterative linear algebra (notes and problem sets). https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/
  4. Scientific Computing: An Introductory Survey (Revised 2nd ed.) — Michael T. Heath — SIAM, 2018. https://doi.org/10.1137/1.9781611975581
  5. Accuracy and Stability of Numerical Algorithms (2nd ed.) — Nicholas J. Higham — SIAM, 2002. https://doi.org/10.1137/1.9780898718027
  6. Numerical Linear Algebra — Trefethen & Bau — SIAM, 2022 (added to 01; would move or cross-reference here).

## Cut candidates

- **03:**
  - Ross, *Intro to Probability and Statistics for Engineers and Scientists*: yet another intro text alongside Stat 110, Wasserman and 6.041.
  - Lawler: redundant with Ross's *Models* for a self-learner, and not free.
  - Jaynes: keep only as optional philosophy.
- **04:**
  - Adam paper and Ruder (2016): ML-specific and dated; the ML curriculum is the right home.
  - MML ch. 7: duplicates ml/01.
- **05:** Jordan et al. 1999 is a dated variational-inference entry point; a modern VI review belongs in ml.
- **06:** Kipf & Welling (GCN) and Bronstein et al. (GDL) duplicate ml/13; a cross-link would do.
- **07:** Neural ODE and S4 papers are also in physics/11 and ml. They are fine as connectors, but they are duplicates.
- **08:** Herstein and Lang (encyclopedic or advanced) and Aluffi (category-theoretic): low value for the intended learner. The Gross playlist is an unofficial re-upload.
- **09:** do Carmo and Lee are graduate-level for an elective. The Albin playlist is an unofficial re-upload.
- **10:** Dasgupta et al. 2019 (meta-RL causal reasoning) is niche and weak.
- **11:**
  - Spivak CT4S: redundant with Seven Sketches.
  - HoTT book, Backprop as Functor, Cruttwell et al.: research-level.
  - Mac Lane: reference only.
  - Wolfram: keep only with the critique attached; it is now also in physics/11 and philosophy/03.
- **01:** Khan Academy LA is a gap-filler that duplicates ml/01. The Matrix Cookbook is duplicated in blogs-and-references.
- **PROGRESS:** The "Books (supplementary)" block double-tracks section items.

## Structural observations

- **Missing engineering spine / core-vs-elective.** The README path runs 00→11 with equal weight and frames everything as "math for ML". For the intended learner, a better structure is:
  - *Core:* 00 → 01 (+VMLS) → 02 (+complex) → 07 (+Feedback Systems) → **12 Signals & Systems (created)** → 03 (+Rethinking, Kalman) → 14 Numerics (created) → 04 → 05.
  - *Electives:* 06, 08 (+ **13 Number Theory/Crypto, created**, which is core if doing btc), 09, 10, 11.
  - **Done:** this route is now a "Recommended Route (engineering focus)" table in `math/README.md`.
  - Suggest a "Core / Elective" column or marker in the README learning path, plus rough hour estimates per section.
- **Legend** has only 🔑. 🔑 is used sensibly within sections (1–2 per section), but there is no curriculum-level priority signal.
- **Overlap with other curricula:**
  - **ml/01-math-foundations** duplicates 3B1B LA and Calculus, MML, Khan and StatQuest from math/01–03. The ml agent has now made ml/01 a "fast on-ramp" that links to math/01–05 and fixed the MML author (Faisal). ml/01 has Parr & Howard's matrix calculus, which math/02 lacks; consider a cross-link.
  - **ml/13** duplicates GCN and GDL (math/06). It has an "AlphaProof & AlphaGeometry" row with no link. math/08 now links to ml/13 for equivariant networks, and math/11 holds the 2025 AlphaEvolve/Tao paper.
  - **physics/10** duplicates the Strogatz book and lectures from math/07. The physics agent has already corrected "Yale" → "Cornell" and updated to the 3rd edition.
  - **physics/11** and **philosophy/03** both carry Wolfram NKS / Physics Project / ruliad. All three curricula now consistently label it speculative, and philosophy/03 also has Aaronson's review, so that review now appears in both math/11 and philosophy/03. That duplication is acceptable but worth knowing about.
  - **physics/06** (Newman, Numerical Recipes, 18.085, FEniCSx) overlaps Section 14 (created; cross-linked both ways in spirit — 14 links physics/06).
  - **physics/01** holds the only Fourier content in the repo (3B1B videos) → Section 12 (created; links physics/01).
  - **physics/05** (GR) depends on math/09.
  - **btc/01** now (after the btc agent's pass) links to math/08 and includes Corbellini's ECC series, Programming Bitcoin ch. 1–3 and Mastering Bitcoin ch. 8. Its ECC/ECDSA/Schnorr "Concept" rows still have no math text behind them. math/08's HPS fills that gap, and Section 13 (created) now deepens it. Corbellini and Song should then be cross-referenced from B rather than duplicated (done).
  - **software/00** already defers discrete math to math/00; its pointer names "Epp, Bazett", and could now mention MIT 6.042J.
  - **pcb/06–07** (signal integrity, EMC) rely on frequency-domain thinking and should link to math Section 12 (created).
- **Third-party YouTube uploads** (Gross in 08, Albin in 09) are fragile; prefer official sources where they exist.
- **Stat 110** official site appears to have moved to stat110.hsites.harvard.edu; the older projects.iq.harvard.edu links are left for the URL audit.
- **No `.agents/skills/update-curriculum/SKILL.md`** exists in math (pcb, btc, ml and software have one). If the other curricula's skills are kept, math should get one for consistency.
- **Verification limits:** WebSearch and WebFetch budgets ran out near the end. These ✱ items are left for a follow-up:
  - Meyer 2nd-edition year
  - Herstein's level
  - Peters et al. open-access status
  - Duchi notes' year (PCMI volume)
  - The print year of Polyanskiy & Wu: I list 2024 for the free draft, and the print edition is from Cambridge UP

## Top 5 priorities in this curriculum

1. **Build the EE spine first.** Do complex analysis (Needham VCA + MIT 18.04), then Åström & Murray's *Feedback Systems*, then the new Section 12 Signals & Systems section (Oppenheim RES.6-007, Osgood EE261, Smith's DSP guide, MIT 6.011 for noise, PSD and detection). This is the math behind sensor signal chains and test equipment.
2. **Linear algebra, applied and numerical.** Do 18.06 alongside Boyd & Vandenberghe's VMLS (least squares, estimation, control), then Trefethen & Bau (now in Section 14, with Goldberg and Driscoll & Braun) so computed results can be trusted. Treat Axler as the elective for proof maturity.
3. **Probability for real measurements.** Do Stat 110, then Labbe's *Kalman and Bayesian Filters* (sensor fusion), then McElreath's *Statistical Rethinking* (applied Bayes; good for ML). Keep BDA and Jaynes as references.
4. **Number theory and finite fields for Bitcoin.** Work through Section 13. Warm up with MIT 6.042J's number-theory chapters, then study Silverman's *Friendly Introduction* and Hoffstein/Pipher/Silverman, with Song's *Programming Bitcoin* Ch. 1–3 (btc Section 01) alongside. Finish with the secp256k1 + BIP-340 mini-project. This turns the btc curriculum's "Concept: ECDSA" rows into understanding.
5. **Learn proof with a feedback loop, and keep category theory last.** Pair Velleman with the Natural Number Game, continue with *The Mechanics of Proof*, then *Mathematics in Lean*; machine-checked proof is also where AI-for-math is heading. Treat 06, 09, 10 and especially 11 (category theory, Wolfram) as electives.

## Follow-up pass (2026-10-13)
- **New sections created:** none
- **Added:**
  - How To Prove It with Lean — Daniel J. Velleman — 2023 (© 2023–2025) — 00 (table row, Suggested Order step 5, PROGRESS line; Practice 5 now names its Introduction to Lean and Ch. 3 and 6, re-estimated at ~6–8 h)
  - Group Explorer 3 (web app) — Nathan Carter, Ray Ellis — no year shown — 08 (table row, Suggested Order step 2, PROGRESS line)
- **Removed (confirmed nonexistent):** none
- **Flags resolved:**
  - math/00-mathematical-thinking/README.md:35, :60 — Practice 5 cited the unlisted *How To Prove It with Lean* (independent check V2) — confirmed title, author, Lean 4, match to the 3rd edition, CC BY-SA 4.0 and the chapter list (Introduction to Lean; 3 Proofs; 6 Mathematical Induction) → added as a resource; the exercise now points at it — https://djvelleman.github.io/HTPIwL/
  - math/08-abstract-algebra/README.md:40, :60 — Practice 1 cited the unlisted Group Explorer (V2) — confirmed: browser app by Nathan Carter and Ray Ellis (v3; latest release 3.6.1), LGPL-3.0, all groups up to order 20, Cayley diagrams, multiplication tables, cycle graphs → added — https://nathancarter.github.io/group-explorer/ ; https://github.com/nathancarter/group-explorer
  - math/04-optimization/README.md:40 — "a 2nd edition is due in 2027" (V2) — confirmed: the book site lists the 2nd edition's release as 5 January 2027 and links PDFs of both editions (CC BY-NC-ND) → kept, reworded as a dated fact ("checked October 2026") — https://algorithmsbook.com/optimization/
  - math/05-information-theory/README.md:38 — "the up-to-date successor to Cover & Thomas" (V2 overclaim) → "a graduate-level alternative to Cover & Thomas, not a replacement for it as a first text". Print year (review ✱) 2024 → 2025, Cambridge UP, 1st ed. — library catalogue record https://dk.fchpt.stuba.sk/Record/stu.0140269 (the CUP product page failed to load and Crossref returned HTTP 429, so this rests on the catalogue record)
  - math/01-linear-algebra/README.md:35 — Meyer 2nd-edition year (review ✱): 2000 → 2023 (SIAM); title "(2nd ed.)", author "Carl D. Meyer", DOI link and the separate *Study and Solutions Guide* added — https://api.crossref.org/works/10.1137/1.9781611977448 ; https://api.crossref.org/works/10.1137/1.9781611977462 ; https://search.ub.tum.de/vufind/Record/DE-604.BV049370045
  - math/08-abstract-algebra/README.md:36, :54 — Herstein's level (review ✱): "classic graduate text" → "classic undergraduate text (2nd edition; first published 1964), demanding"; Suggested Order step 9 reworded to match — https://en.wikipedia.org/wiki/Israel_Nathan_Herstein
  - math/10-causal-inference/README.md:38 (+ PROGRESS.md:168) — Peters, Janzing & Schölkopf open access? (review ✱) — yes: the copyright page of the OAPEN PDF licenses the MIT Press book under CC BY-NC-ND 4.0 → "Book (Free)", subtitle added, link → the free PDF (OAPEN record and MIT Press page kept in the description), PROGRESS "(free)" — https://library.oapen.org/handle/20.500.12657/26040 ; https://library.oapen.org/bitstream/20.500.12657/26040/1/11283.pdf
  - math/12-fourier-analysis-signals-and-systems/README.md:47 — Prandoni & Vetterli year "—" → 2008 (EPFL Press, 1st ed., June 2008) — https://epflpress.org/product/515/9782940222209/signal-processing-for-communications
  - math/14-numerical-methods-and-scientific-computing/README.md:48 (+ books/README.md:44) — Driscoll & Braun year "—" → 2022; print editions are SIAM's MATLAB edition (2017, doi 10.1137/1.9781611975086) and Julia edition (2022, doi 10.1137/1.9781611977011); the free online text has updated exercises — https://fncbook.com/usage
  - math/04-optimization/README.md:37 — Duchi's year (review ✱): "—" → 2018 (*The Mathematics of Data*, IAS/Park City Mathematics Series, AMS); "Book (Free)". The old PDF link (…/~jduchi/PCMIConvex.pdf) would not load, so the row now links the author's page, which carries the manuscript PDF (…/PCMIConvex/Duchi16.pdf; its title matches the row), the exercise data and MATLAB/Julia starter code — https://web.stanford.edu/~jduchi/pcmi.html ; https://web.stanford.edu/~jduchi/books.html
  - math/01-linear-algebra/README.md:59, :64 — specific problem-set and chapter numbers (V2), partly resolved: 18.06 Problem Set 5 = §§4.1, 4.2, 8.2 and Problem Set 10 = §§6.6, 6.7, 8.5, both with posted solutions, as cited — https://ocw.mit.edu/courses/18-06-linear-algebra-spring-2010/pages/assignments/ . No Strogatz § numbers remain in math/ (Section 07 cites chapters by topic). The Velleman chapter numbers cited in 00 and 08 (Ch. 1–8) agree with the chapter list of *How To Prove It with Lean*, which follows the 3rd edition.
- **Still unverified:**
  - The Oppenheim & Willsky *Signals and Systems* edition behind RES.6-007 — the OCW syllabus page returned a server error. The repo states no edition, so nothing is wrong as written.
  - The remaining chapter numbers in practice citations (e.g. Axler Ch. 2, 3, 5; MacKay and Cover & Thomas chapters; Diestel, Munkres and Riehl chapters; *What If* Ch. 12–13) — not checked one by one in this pass. The V2 checker already confirmed the lecture and exercise numbers it knew (18.06, 18.065, B&V Ex. 2.12/3.16/5.1, Shannon Thm 17).

## Link-audit fixes (2026-10-13)
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| math/04-optimization/README.md:36 ; math/courses/README.md:14 | SEE EE364A videos at `see.stanford.edu/course/ee364a` (4xx; SEE paths are case-sensitive) | `see.stanford.edu/Course/EE364A` (L1-149) | https://see.stanford.edu/Course/EE364A |
| math/03-probability-and-statistics/README.md:34 | Blitzstein & Hwang at `projects.iq.harvard.edu/stat110/home` (old host) | `stat110.hsites.harvard.edu` (L2-138; books/README.md already had it) | https://stat110.hsites.harvard.edu/ |
| math/03-probability-and-statistics/README.md:37 ; math/books/README.md:17 | BDA at `www.stat.columbia.edu/~gelman/book/` (302 redirect) | `sites.stat.columbia.edu/gelman/book/` (L2-152) | https://sites.stat.columbia.edu/gelman/book/ |
| math/06-graph-theory-and-combinatorics/README.md:34 ; math/courses/README.md:22 | Spielman "Yale course" linked to `…/spielman/sgta/`, his FOCS 2007 tutorial page; year "—" | The Spring 2025 course schedule with lecture notes (`…/spielman/462/462schedule.html`); year 2025; description rewritten to match (L3-029). Not the auditor's `…/spielman/561/`: fetched twice, that page is only a "Fall 2015" announcement heading with no links, while Spielman's home page links the current course | https://www.cs.yale.edu/homes/spielman/462/462schedule.html ; http://www.cs.yale.edu/homes/spielman/ |
| math/10-causal-inference/README.md:34 | *What If* at `hsph.harvard.edu/miguel-hernan/causal-inference-book/`, which (fetched again today) still serves the 2015 draft-book page | `miguelhernan.org/whatifbook`: Hernán & Robins (2020, Chapman & Hall/CRC), with the latest free PDF, the NHEFS data and Python/R/SAS/Stata/Julia code that Practice 3 uses (L2-073) | https://miguelhernan.org/whatifbook |
- Already fixed in the follow-up pass above: Duchi's notes (L2-164), now linked through the author's page `web.stanford.edu/~jduchi/pcmi.html`.
- Left unchanged because the auditor could not load the page: Judson (08:33, robots.txt; L1-002), Khan Academy Linear Algebra (01:36; L2-089), NotebookLM (README:9; L2-114), MacKay's PDF (05:33 and books/README.md:20; the whole host returned 4xx; L3-078), Mathematics Stack Exchange and MathOverflow (blogs-and-references/README.md:46–47; L3-099, L3-100), and the Gross "Harvard Abstract Algebra" playlist (08:35; L3-175), which exists but is a third-party upload whose attribution to Gross could not be confirmed.
- The Stat 110 course rows (03:32, courses/README.md:11) keep `projects.iq.harvard.edu/stat110`, which the audit found working (L1-138).

## Tier lists (2026-10-13)
No math section had more than 3 🔑 resource rows (25 in all; 01 has 3; 00, 02, 03, 04, 05, 12, 13 and 14 have 2; 06–11 have 1), so no 🔑 was removed and the index files are unchanged; each Suggested Order (00–14) now opens with a "Core path (🔑)" line naming the section's 🔑 items in reading order.

- books/README.md #35 Hoffstein, Pipher & Silverman, *An Introduction to Mathematical Cryptography*: 🔑 added (core in 13)
- books/README.md #36 Smith, *The Scientist and Engineer's Guide to Digital Signal Processing*: 🔑 added (core in 12)
- books/README.md #38 Driscoll & Braun, *Fundamentals of Numerical Computation*: 🔑 added (core in 14)
- courses/README.md #3 3Blue1Brown, Differential Equations: 🔑 removed (not core in any section; unmarked in 07)
- math/README.md legend: 🔑 row now reads "**Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line"
- Not changed: books/README.md #25 *Mathematics for Machine Learning* and courses/README.md #10 Strogatz's Nonlinear Dynamics and Chaos lectures stay unmarked. They are core only in ml/01 and physics/10, and unmarked in math 01, 04 and 07.
