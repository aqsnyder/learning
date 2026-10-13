# Economics, Decision Theory & Game Theory (`econ/`) — Review

> **Deep-dive review, October 2026** · curriculum: [`econ/`](../../econ/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

Reviewer: evaluator agent, 2026-10-13. Scores and grades describe the curriculum **as found** (before this pass). Edited files: all 12 section READMEs, `PROGRESS.md`, `books/`, `courses/`, `blogs-and-references/`. `econ/README.md` was not edited (no verified errors in it).

> **Verification limits this run.** The shared WebSearch budget ran out partway through, and then the shared WebFetch budget did too (HTTP 403 "budget exhausted", then repeated HTTP 429 rate limits). I added nothing I could not fetch and confirm. These pages could not be read and were dropped or left pending: `nber.org/papers/w31161`, `arxiv.org/abs/2304.11771`, `arxiv.org/abs/1804.04268`, `aeaweb.org/articles?id=10.1257/jep.33.2.3`, `digitaleconomy.stanford.edu/publications/canaries-in-the-coal-mine/`, `metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/` (all 429), `coursera.org/learn/money-banking`, `aeaweb.org/articles?id=10.1257/jel.20201552`, `nber.org/papers/w25560`, `arxiv.org/abs/2012.00854` (budget-exhausted 403). Cambridge UP, HarperCollins and Penguin Random House pages refused fetches, and so did `nobelprize.org/.../2012/roth/lecture/`. As a result **Sections 10 and 11 received corrections but no new resources**. The candidates are listed (without URLs) in *Proposed new sections* for a follow-up pass to verify.

## Verdict

The curriculum has a sensible micro-theory spine: thinking → micro → games → decisions → mechanisms → information → behavioral → networks → algorithmic game theory → social choice → money/crypto → AI. Most of its anchors are canonical, either classic papers (Akerlof, Spence, Vickrey, Myerson, Arrow, Gibbard, Hayek, Coase) or excellent free courses (Polak, Roughgarden, Easley & Kleinberg). It falls short in three ways:

- **Accuracy.** Two placeholder or hallucinated entries in 05, a paper credited to the wrong author and year in 11, a mistitled Dafoe paper, an outdated Varian edition behind a dead link, a malformed DOI, and a false claim about where von Neumann–Morgenstern's axioms appear.
- **Epistemic hygiene.** Kahneman's priming and ego-depletion material and Ariely's work were presented as "essential" with no warning about failed replications or a retraction. *Nudge* came with no effect-size calibration.
- **Scope.** There is no macroeconomics, no econometrics or causal inference, and no industrial organization. "Computational economics" is only algorithmic game theory. Section 11 is titled "Economics" but contains no economics of AI.

**Overall grade: C+ as found (about B− after this pass).** The single most important improvement is to rebuild Section 11 around the economics of AI: the task-based automation framework plus the 2023–2026 labor-market and productivity evidence. The generic alignment readings, which duplicate philosophy/07 and ml/12, should become cross-references.

## Scorecard

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 Economic Thinking | 3 | 4 | 3 | 4 | 4 | B− | Good concrete on-ramp, but no macro, a one-sided (Austrian/libertarian) opening, and Dalio's model presented as "how the economy works" |
| 01 Microeconomics | 3 | 3 | 3 | 4 | 4 | B− | Right core (Varian, Gruber, Hayek, Coase), but an outdated Varian edition behind a dead link and no commons/public goods |
| 02 Game Theory | 4 | 4 | 4 | 3 | 4 | B+ | Strongest section; missing bargaining and the cooperation classics; should come after decision theory |
| 03 Decision Theory | 2 | 2 | 2 | 3 | 3 | C | Six of nine items behavioral, thin normative theory, no replication caveats, wrong vNM claim |
| 04 Mechanism Design | 3 | 5 | 3 | 3 | 4 | B | Accurate auction canon; matching and market design promised in the intro but absent |
| 05 Information Economics | 3 | 2 | 3 | 3 | 4 | C+ | Right classic papers, but two placeholder entries and a misleading Nobel count |
| 06 Behavioral Economics | 3 | 3 | 2 | 4 | 3 | C+ | Thaler-heavy popular reading with no replication or nudge-effect-size calibration; wrong DOI |
| 07 Network Economics | 3 | 4 | 3 | 4 | 4 | B− | Solid platform/network canon; no IO or antitrust; nothing after 2016 |
| 08 Computational Economics | 2 | 4 | 3 | 4 | 4 | C+ | Really "algorithmic game theory": no numerical methods, agent-based models, or LLM agents |
| 09 Social Choice & Voting | 3 | 3 | 2 | 4 | 4 | B− | Classics present; inaccurate Sen description; nothing computational or AI-related after 2009 |
| 10 Monetary Economics & Crypto | 2 | 3 | 2 | 3 | 2 | C | Money-and-banking basics nearly absent; advocacy-heavy, with 🔑 on Ammous; duplicates btc/09 |
| 11 AI Alignment, Economics & Frontiers | 2 | 2 | 2 | 3 | 3 | C− | Two citation errors; promises economics of AI and contains none; mostly duplicates phil/07 and ml/12 |

## Section-by-section

### 00 — Economic Thinking
- **Strengths:** Short, concrete ramp. Free visual options (Khan, MRU) sit alongside a canonical text. "I, Pencil" and Hazlitt train second-order thinking.
- **Problems:**
  - ✔ Mankiw had no year and linked the superseded 9th edition. Now 10th ed. (2024) with a working Cengage link.
  - ✔ Dalio's video was described as a "brilliant" account of "how the economy works". Now framed as Dalio's own debt-cycle model, to be checked against CORE.
  - ✱ The opening trio (Dalio → Read → Hazlitt) and later Hayek ×2 / Ammous / Voskuil give the intro and money sections an Austrian/libertarian tilt with no mainstream macro counterweight. CORE partly fixes this.
  - ✱ Khan Academy Micro is duplicated in 00 and 01, with 🔑 in both.
- **Missing:** Macroeconomics basics (GDP, inflation, unemployment, interest rates, fiscal/monetary policy). A "what economic models are and aren't" meta-view (e.g., Rodrik, *Economics Rules*, 2015; no URL verified).
- **Added:**
  - The Economy 2.0 (Micro + Macro volumes) — CORE Econ team — 2023

### 01 — Microeconomics
- **Strengths:** Varian plus Gruber's 14.01 is the right core. Hayek (1945) and Coase (1960) are the right two classic essays. MWG is correctly flagged as reference-only.
- **Problems:**
  - ✔ Varian was listed as 2014 with a Norton link that returns "Page Not Found". The current 10th edition (2024) is co-authored with Marc Melitz; the main and calculus entries now carry the new edition, co-author and links.
  - ✔ Friedman's *Price Theory* now has its year (1990, 2nd ed.).
  - ✔ The calculus companion was missing from PROGRESS.
  - ✱ Khan Academy is duplicated from 00.
- **Missing:** Public goods and common-pool resources (Ostrom). Market power, pricing and price discrimination beyond Varian's chapters (see the IO proposal). A free rigorous text between Varian and MWG.
- **Added:**
  - Beyond Markets and States: Polycentric Governance of Complex Economic Systems (Nobel lecture) — Elinor Ostrom — 2009
  - Models in Microeconomic Theory — Martin J. Osborne & Ariel Rubinstein — 2020

### 02 — Game Theory
- **Strengths:** Polak plus Tadelis is an excellent core. Schelling, Maynard Smith and the free Osborne & Rubinstein give breadth.
- **Problems:**
  - ✔ The Coursera course was credited to "Jackson & Shoham". It is Jackson, Leyton-Brown & Shoham (Stanford/UBC), now fixed in the section, `courses/` and PROGRESS.
  - ✔ Nash (1951) was called "the original"; the description now notes the 1950 *PNAS* announcement.
  - ✔ Watson and Spaniel were missing from the Suggested Order.
  - ✱ Decision theory (03) is logically prior: mixed strategies need vNM utility.
- **Missing:** Bargaining theory (Nash bargaining, alternating offers), which Section 11's cooperative-AI papers assume. Cooperation in repeated games (Axelrod).
- **Added:**
  - The Evolution of Cooperation — Robert Axelrod & William D. Hamilton — 1981
  - Bargaining and Markets — Martin J. Osborne & Ariel Rubinstein — 1990

### 03 — Decision Theory
- **Strengths:** Has the key primary sources: Tversky & Kahneman 1974, Kahneman & Tversky 1979 (correctly described as economics' most-cited paper), Savage, Knight, vNM.
- **Problems:**
  - ✔ *Thinking, Fast and Slow* was marked "Essential" with no warning. It now notes the failed social-priming (Ch. 4) and ego-depletion (Ch. 3) results and quotes Kahneman's own concession, and the "Train Wreck" audit is added beside it.
  - ✔ Ariely's book and course had no mention of the 2021 *PNAS* retraction or the failed 25-lab replication (2018) of the book's "Ten Commandments" result. Caveats added.
  - ✔ vNM was typed as a "Paper" and credited with axiomatizing expected utility in Ch. 1–3. The axiomatic derivation is in the appendix added to the 1947 2nd edition. Now a 📖 Book with reading "Ch. 1 & Appendix" (also fixed in PROGRESS and the order).
  - ✱ Six of nine items are behavioral and overlap 06. Refocus 03 on normative decision theory and move the Kahneman/Ariely trade books to 06. This is your call, given the append-only rule.
  - ✱ 03 should come before 02.
- **Missing:** Bayesian decision theory and the value of information. Ambiguity (Ellsberg 1961) and Allais. Newcomb's problem and causal vs. evidential decision theory (core to AI-alignment decision theory). A normative textbook (Peterson, *An Introduction to Decision Theory*, 2nd ed. 2017; the Cambridge page refused fetches).
- **Added:**
  - Reconstruction of a Train Wreck: How Priming Research Went off the Rails — Ulrich Schimmack, Moritz Heene & Kamini Kesavan — 2017
  - Decision Theory (Stanford Encyclopedia of Philosophy) — H. Orri Stefánsson — 2015, rev. 2025

### 04 — Mechanism Design
- **Strengths:** Every citation checked out (Vickrey, Myerson ×2, Krishna, Ausubel & Milgrom, Milgrom's Nobel lecture). Börgers is the right textbook.
- **Problems:**
  - ✔ The "Why" text promised matching markets and kidney exchange, but no resource covered them. The 2012 Nobel background now does.
  - ✱ Sequencing: mechanism design rests on private information and screening, so make 05 a prerequisite or swap 04 and 05.
  - ✱ VCG/Groves–Clarke is never named as a reading.
- **Missing:** Market design in depth: Gale & Shapley 1962, and Roth's *Who Gets What — and Why* (2015; publisher pages blocked, recommend adding after verification). Milgrom's *Putting Auction Theory to Work* (2004). Blockchain transaction-fee mechanism design (Roughgarden's EIP-1559 analysis, 2020), a natural bridge to 10. Public-goods mechanisms (quadratic funding).
- **Added:**
  - Scientific Background: Mechanism Design Theory — Royal Swedish Academy of Sciences — 2007
  - Stable Matching: Theory, Evidence, and Practical Design — Royal Swedish Academy of Sciences — 2012

### 05 — Information Economics
- **Strengths:** The right four classic papers in the right order. Akerlof's "rejected three times" claim is correct (AER, *ReStud*, JPE).
- **Problems:**
  - ✔ "Why Akerlof's 'Lemons' Paper Was Initially Rejected" had no author, year or link (a placeholder). Replaced with Akerlof's own essay on nobelprize.org (2003).
  - ✔ "The Economics of Information — Joseph Stiglitz" had no year or link. No such Stiglitz book could be confirmed (possibly confused with George Stigler's 1961 *JPE* paper of that title). Replaced with Stiglitz's 2001 Nobel lecture, his own synthesis.
  - ✔ "These ideas earned three Nobel Prizes": Akerlof, Spence and Stiglitz shared one (2001). Reworded, adding Hart–Holmström 2016.
  - ✔ Prerequisites lacked Game Theory; signaling and screening are Bayesian games.
  - ✱ *Information Rules* is duplicated with 07, and appears twice in PROGRESS.
- **Missing:** Information design / Bayesian persuasion. A readable contract-theory on-ramp (multitasking, incomplete contracts). Grossman–Stiglitz (1980) on informationally efficient prices.
- **Added:**
  - Writing the "The Market for 'Lemons'" — George Akerlof — 2003 (replaces placeholder)
  - Information and the Change in the Paradigm in Economics (Nobel lecture) — Joseph Stiglitz — 2001 (replaces placeholder)
  - Contract Theory (popular science background) — Royal Swedish Academy of Sciences — 2016
  - Bayesian Persuasion — Emir Kamenica & Matthew Gentzkow — 2011

### 06 — Behavioral Economics
- **Strengths:** Engaging on-ramp (*Misbehaving*), Thaler's primary papers, and *Noise* for the variance side of judgment.
- **Problems:**
  - ✔ There was no replication or effect-size warning. Added a ⚠️ evidence-check callout (ego-depletion RRR d ≈ 0.04, social priming, the Ariely retraction, nudge effect sizes) plus two calibrating resources.
  - ✔ The *Mental Accounting Matters* DOI was malformed (`(199912)12:4`). Corrected to Crossref's `(199909)12:3`.
  - ✔ The Anomalies columns were dated 1987–1990; Thaler's first series ran 1987–1991.
  - ✔ Thaler was "its founder"; now "one of its founders".
  - ✔ *Nudge* now notes the Final Edition (2021).
  - ✱ Four trade books and no rigorous survey (fixed by DellaVigna 2009).
  - ✱ Behavioral Scientist was missing from the order (✔ added).
- **Missing:** Present bias and time inconsistency (Laibson; O'Donoghue & Rabin). Social preferences (Fehr & Schmidt). Behavioral game theory. Field evidence. Realistic nudge effect sizes.
- **Added:**
  - Psychology and Economics: Evidence from the Field — Stefano DellaVigna — 2009
  - RCTs to Scale: Comprehensive Evidence from Two Nudge Units — Stefano DellaVigna & Elizabeth Linos — 2022
  - Behavioral Game Theory — Colin Camerer — 2003

### 07 — Network Economics
- **Strengths:** Easley & Kleinberg (free), Katz–Shapiro, Rochet–Tirole and Evans–Schmalensee make a strong network/platform core. Stratechery is the right applied follow.
- **Problems:**
  - ✔ *Matchmakers* was missing from the Suggested Order and PROGRESS.
  - ✱ *Information Rules* is duplicated with 05.
  - ✱ QWERTY is presented as settled lock-in, but the example is contested (Liebowitz & Margolis, "The Fable of the Keys", 1990). Not edited because I couldn't verify a source.
  - ✱ The examples (Facebook, Uber) are dated.
- **Missing:** Industrial organization: market power, antitrust and platform regulation. A modern platform-economics text (Belleflamme & Peitz, *The Economics of Platforms*, 2021; not verified). The economics of AI platforms.
- **Added:**
  - Metcalfe's Law is Wrong — Bob Briscoe, Andrew Odlyzko & Benjamin Tilly — 2006

### 08 — Computational Economics
- **Strengths:** Roughgarden is the clearest expositor. With the *AGT* book, Daskalakis et al., Arora–Hazan–Kale and Blum et al., this is a good AGT core.
- **Problems:**
  - ✔ The section was AGT-only despite its title. Added numerical methods (QuantEcon), agent-based modeling (Mesa) and LLM agents (Homo silicus), plus a scope sentence.
  - ✔ Prerequisites lacked 04.
  - ✔ Blum et al. was missing from the order and PROGRESS; CS364B was missing from PROGRESS.
  - ✱ The free *AGT* PDF is hosted on a 2013 CMU course page, which looks like an unofficial mirror; the link audit should confirm it.
  - ✱ "Tim Roughgarden's Page" is typed 📝 Blog. It is a homepage, and it is duplicated in `blogs-and-references/`.
- **Missing:** Learning in games as used in AI (e.g., counterfactual regret minimization and the poker AIs). Equilibrium computation in practice.
- **Added:**
  - QuantEcon Lectures (Quantitative Economics with Python) — Thomas J. Sargent & John Stachurski — continuously updated
  - Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? — John J. Horton, Apostolos Filippas & Benjamin S. Manning — 2023
  - Mesa 3: Agent-Based Modeling with Python in 2025 — Ewout ter Hoeven, Jan Kwakkel et al. — 2025

### 09 — Social Choice and Voting
- **Strengths:** Arrow, Gibbard, Sen, Moulin and the SEP entry are the right classics, with a gentle PBS on-ramp.
- **Problems:**
  - ✔ Sen was said to extend Arrow "with capability approach", which the publisher's description of *Collective Choice and Social Welfare* doesn't support. Rewritten to its actual contribution (informational broadening and interpersonal comparisons, the liberal paradox, eleven new chapters in the expanded edition).
  - ✔ PROGRESS mis-titled the SEP entry ("Voting Theory" → "Voting Methods") and omitted the PBS video and List & Puppe.
  - ✔ List & Puppe was missing from the order.
  - ✱ Arrow's book is described as "short, readable"; "readable" is generous.
  - ✱ The Yale link edition should be checked by the link audit.
- **Missing:** Computational social choice. Quadratic voting. Social choice applied to AI alignment and RLHF, the exact question the "Why" text raises. Condorcet's jury theorem and the median voter are only implicit.
- **Added:**
  - Quadratic Voting: How Mechanism Design Can Radicalize Democracy — Steven P. Lalley & E. Glen Weyl — 2018
  - Handbook of Computational Social Choice — Brandt, Conitzer, Endriss, Lang & Procaccia (eds.) — 2016
  - Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback — Vincent Conitzer et al. — 2024

### 10 — Monetary Economics and Crypto
- **Strengths:** Primary sources (Nakamoto, Buterin), MIT 15.S12, Martin's history of money, and Walsh as a rigorous anchor.
- **Problems:**
  - ✔ "Gensler later became SEC chair" is now "chaired the SEC (2021–2025)".
  - ✔ The Ammous description had no balance. It is now flagged as heterodox advocacy to test against mainstream sources.
  - ✔ Voskuil was missing from the order and PROGRESS.
  - ✱ 🔑 on *The Bitcoin Standard* in an economics curriculum. It is also 🔑 in btc/09; recommend demoting it to optional here and letting btc own it.
  - ✱ Money, banking and central banking basics are nearly absent: only Martin (history) and Walsh (graduate).
  - ✱ Hayek's *Denationalisation* links to mises.org (an advocacy site); the IEA is the original publisher.
- **Missing:**
  - A mainstream money-and-banking course (Mehrling, *Economics of Money and Banking*, Coursera).
  - Mainstream economics of crypto: Budish's security-cost argument ("The Economic Limits of Bitcoin and the Blockchain", NBER 2018) and the *JEL* survey "The Microeconomics of Cryptocurrencies" (Halaburda, Haeringer, Gans & Gandal, 2022).
  - Stablecoins and CBDCs, DeFi and MEV, fee-market mechanism design (EIP-1559), spot-bitcoin ETFs (2024).
- **Added:** Nothing. All four candidates above were blocked by the fetch budget; verify and add next pass.

### 11 — AI Alignment, Economics, and Frontiers
- **Strengths:** Manheim & Garrabrant's Goodhart taxonomy, the Off-Switch Game and Dafoe et al. are well chosen, economics-flavored alignment readings.
- **Problems:**
  - ✔ Dafoe et al. was mistitled "Cooperative AI"; it is "Open Problems in Cooperative AI" (fixed in the table, the order and PROGRESS).
  - ✔ Multi-Principal Assistance Games was credited to "Michael Dennis et al., 2024". It is Fickinger, Zhuang, Hadfield-Menell & Russell, 2020 (fixed in all three places; matches link-audit U1-005).
  - ✔ Prerequisites lacked 05.
  - ✔ The LessWrong wiki was missing from the order.
  - ✔ Added cross-links to the econ-of-AI-adjacent items placed in 05, 08 and 09.
  - ✱ The title promises "Economics", but there is no labor-market, productivity or growth content.
  - ✱ Concrete Problems, AI Safety Fundamentals and the Alignment Forum duplicate philosophy/07 (and ml/12 covers RLHF/CAI).
  - ✱ The AISF link domain has moved to BlueDot; left for the link audit.
- **Missing:**
  - The task-based automation framework.
  - Generative-AI productivity RCTs (writing, customer support, consulting, software developers).
  - Exposure and usage measures.
  - 2024–26 labor-market evidence.
  - Macro and growth estimates.
  - The principal–agent / incomplete-contracting framing of alignment.
  - AI agents as economic actors.
- **Added:** Nothing new verified (fetch budget). See Proposed new section P1.

### books/
- ✔ Mankiw and Varian rows had no year and stale/dead links; now 2024 10th editions with Varian & Melitz as authors. ✔ Harford's year added (2005, consistent with 00).
- ✔ Added CORE *The Economy 2.0*, a free core text.
- ✱ Seven rows have no link (Kahneman, Thaler ×2, Christian, Schelling, Harford, Cesa-Bianchi), and the Notes column is mostly empty.
- ✱ The *AGT* PDF link is an unofficial mirror.
- ✱ 🔑 on *The Bitcoin Standard* (see 10).
- ✱ There is no book entry for normative decision theory or for any macro text.

### courses/
- ✔ Jackson, Leyton-Brown & Shoham. ✔ Added QuantEcon (Section 08).
- ✱ The Ariely Coursera course may no longer be offered, and the AISF URL has moved; both are for the link audit.
- ✱ Missing (proposed below): Mehrling's *Money and Banking*, Shiller's *Financial Markets* (Open Yale ECON 252), MRU *Mastering Econometrics*.

### blogs-and-references/
- ✔ *The Money Illusion* ended on 1 Sept 2024 ("This will be my final Money Illusion post"). The row now points to Sumner's Substack, *The Pursuit of Happiness*.
- ✔ Added Data Colada, the replication and data-forensics blog behind the Ariely retraction.
- ✱ Missing the *Journal of Economic Perspectives*: free and written for non-specialists, it is the single most useful journal for a self-learner (the URL could not be fetched this run; add it).
- ✱ "The Economist" is listed under Newsletters but is a paywalled magazine.
- ✱ No finance/markets newsletter (e.g., Matt Levine's *Money Stuff*) and no econ-of-AI tracker.
- ✱ Roughgarden's page is duplicated from 08.

### PROGRESS.md
- ✔ Added nine existing-but-untracked section items: Varian calculus, *Matchmakers*, CS364B, Blum et al., the PBS video, List & Puppe, Voskuil, the LessWrong Goodhart wiki, and O&R/Harford in the Books block.
- ✔ Fixed six mis-citations: Voting Methods, Dafoe title, MPAG authors, the Coursera instructors, the vNM chapters, Varian's co-author and edition.
- ✔ Every addition has a line.
- ✱ The "Books (supplementary)" block re-tracks items already in the sections, so they get double-counted. Delete it or turn it into an unchecked reading list.
- ✱ Blogs are tracked inconsistently: MR and Stratechery are in, Behavioral Scientist, Buterin and the Alignment Forum are not.
- ✱ *Information Rules* appears twice.

### README.md (econ)
No verified errors; not edited. Suggestions:
- ✱ The Legend lists only 🔑. Document the type emoji (📖 📄 📝 🎥), the "(Free)" marker and the new ⚠️ "contested / failed replication" usage.
- ✱ Learning-path order: 03 before 02, and 05 before 04 (see Structural).
- ✱ "Keeping Current" points to 11, which had no current economics.
- ✱ The root README promises an `.agents/skills/update-curriculum` skill in every curriculum. econ has none (btc, ml, pcb and software do).

## Corrections made

| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| 00-economic-thinking/README.md:13; books/README.md:7 | Mankiw, year "—", 9th-ed. link | *Principles of Economics* (10th ed.), 2024, new Cengage link | https://cengage.com/c/principles-of-economics-10e-mankiw/9780357722718 |
| 00-economic-thinking/README.md:21 | Dalio: "Brilliant … overview of how the economy works" | "Dalio's own debt-cycle model … not textbook macroeconomics" | Editorial (overclaim) |
| 01-microeconomics/README.md:17; books/README.md:8 | Varian, 2014, wwnorton.com/books/9780393689860 (Page Not Found) | Varian & Melitz, 10th ed., 2024, wwnorton.com/books/9781324034292 | https://seagull.wwnorton.com/intermicro10 · https://wwnorton.co.uk/books/9781324034339-intermediate-microeconomics-eccddd9e-847e-465d-9889-73efbf60b92e |
| 01-microeconomics/README.md:18 | Varian *with Calculus*, "—", 9780393689877 | Varian & Melitz, 2nd ed., 2024, wwnorton.com/books/9781324034414 | https://wwnorton.com/books/9781324034414 |
| 01-microeconomics/README.md:21 | Friedman *Price Theory*, year "—" | 1990 (2nd ed.) | https://search.library.uitm.edu.my/Record/wils-072359 |
| 02-game-theory/README.md:22 | Nash 1951 "The original Nash equilibrium paper" | Full statement/proof; first announced in 1950 *PNAS* note | https://bibbase.org/network/publication/nash-equilibriumpointsinnpersongames-1950 (PNAS 36:48–49, 1950; search result) |
| 02-game-theory/README.md:23; courses/README.md:10; PROGRESS.md:36 | "Matthew Jackson & Yoav Shoham, Stanford" | Matthew Jackson, Kevin Leyton-Brown & Yoav Shoham (Stanford / UBC) | https://www.coursera.org/learn/game-theory-1 |
| 03-decision-theory/README.md:17 | *Thinking, Fast and Slow* "… Essential." (no caveat) | ⚠️ priming (Ch. 4) / ego depletion (Ch. 3) failed replication; Kahneman: "placed too much faith in underpowered studies" | https://replicationindex.com/2017/02/02/reconstruction-of-a-train-wreck-how-priming-research-went-of-the-rails/ · https://mindhacks.com/2017/02/16/how-replicable-are-the-social-priming-studies-in-thinking-fast-and-slow/ · https://doi.org/10.1177/1745691616652873 |
| 03-decision-theory/README.md:23 (+ order :38, PROGRESS.md:51) | 📄 Paper "Theory of Games… (Ch. 1–3)": "Established expected utility theory with axiomatic foundations" | 📖 Book "(Ch. 1 & Appendix)": axiomatic derivation added as appendix to 1947 2nd ed. | https://en.wikipedia.org/wiki/Theory_of_Games_and_Economic_Behavior |
| 03-decision-theory/README.md:26–27 | Ariely course/book, no caveats | ⚠️ 2012 *PNAS* paper retracted 2021; "Ten Commandments" result failed 25-lab RRR (2018) | https://pmc.ncbi.nlm.nih.gov/articles/PMC8463784 · https://openaccess.city.ac.uk/id/eprint/20369/ · https://datacolada.org/98 |
| 05-information-economics/README.md:5 | "These ideas earned three Nobel Prizes" | "won Akerlof, Spence, and Stiglitz the 2001 Nobel Prize (contract theory followed with Hart and Holmström in 2016)" | https://www.nobelprize.org/prizes/economic-sciences/2001/stiglitz/lecture/ · https://www.nobelprize.org/prizes/economic-sciences/2016/advanced-information/ |
| 05-information-economics/README.md:10 | Prereq: 01 only | + Section 02 (signaling/screening are Bayesian games) | Sequencing |
| 05-information-economics/README.md:24 | "Why Akerlof's 'Lemons' Paper Was Initially Rejected", author/year/link "—" | Akerlof, "Writing the 'The Market for Lemons': A Personal Interpretive Essay", 2003 + link | https://www.nobelprize.org/prizes/economic-sciences/2001/akerlof/article/ |
| 05-information-economics/README.md:25 | 📖 "The Economics of Information", Joseph Stiglitz, year/link "—" | 📄 Stiglitz, "Information and the Change in the Paradigm in Economics" (Nobel Lecture), 2001 + link | https://www.nobelprize.org/prizes/economic-sciences/2001/stiglitz/lecture/ |
| 06-behavioral-economics/README.md:7 | (no warning) | ⚠️ evidence-check callout | https://doi.org/10.1177/1745691616652873 · https://www.nber.org/papers/w27594 · https://pmc.ncbi.nlm.nih.gov/articles/PMC8463784 |
| 06-behavioral-economics/README.md:19 | Thaler "by its founder" | "by one of its founders" | Editorial (Kahneman & Tversky co-founded the field) |
| 06-behavioral-economics/README.md:20 | *Nudge* 2008 | 2008 (Final Edition 2021) | https://bookshop.org/a/101528/9780143137009 (search result confirming "Nudge: The Final Edition", ISBN 9780143137009; the 2021 date is from memory, not fetched) |
| 06-behavioral-economics/README.md:21 | DOI `…(199912)12:4<183::AID-BDM318>…` | DOI `…(199909)12:3<183::AID-BDM318>…` | https://api.crossref.org/works/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F |
| 06-behavioral-economics/README.md:22 | Anomalies 1987–1990 | 1987–1991 | https://faculty.chicagobooth.edu/richard-thaler/papers |
| 08-computational-economics/README.md:5,10 | AGT-only scope; prereq 02 only | Scope sentence (numerical methods, ABM, LLM agents); + Section 04 | Sequencing |
| 09-social-choice-and-voting/README.md:19 | Sen "Extends Arrow's framework with capability approach and interpersonal welfare comparisons" | Informational-poverty / interpersonal-comparisons argument; 11 new chapters; liberal paradox | https://www.labyrinthbooks.com/collective-choice-and-social-welfare |
| 10-monetary-economics-and-crypto/README.md:17 | Ammous, no balance | "An advocacy book from a heterodox school: read it as a thesis to test…" | Editorial |
| 10-monetary-economics-and-crypto/README.md:22 | "Gensler later became SEC chair" | "Gensler later chaired the SEC (2021–2025)" | https://ballotpedia.org/Gary_Gensler |
| 11-ai-alignment-economics-and-frontiers/README.md:20 (+ order :36, PROGRESS.md:142) | "Cooperative AI" | "Open Problems in Cooperative AI" | https://arxiv.org/abs/2012.08630 |
| 11-ai-alignment-economics-and-frontiers/README.md:24 (+ order :37, PROGRESS.md:146) | "Michael Dennis et al.", 2024 | Arnaud Fickinger, Simon Zhuang, Dylan Hadfield-Menell & Stuart Russell, 2020 | https://arxiv.org/abs/2007.09540 |
| 11-ai-alignment-economics-and-frontiers/README.md:11 | Prereqs 02, 04 | + Section 05 | Sequencing |
| PROGRESS.md:122 | "Voting Theory — Stanford Encyclopedia of Philosophy" | "Voting Methods — Stanford Encyclopedia of Philosophy" | https://plato.stanford.edu/entries/voting-methods/ (the 09 link) |
| books/README.md:22 | Harford year "—" | 2005 | Consistency with Section 00 |
| blogs-and-references/README.md:14 | *The Money Illusion* (active) | Archive only since Sept 2024 → *The Pursuit of Happiness* (scottsumner.substack.com) | https://www.themoneyillusion.com/a-long-strange-trip/ · https://scottsumner.substack.com/ |
| Suggested Order fixes (02, 03, 06, 07, 08, 09, 10, 11) | Watson, Spaniel, *Predictably Irrational*, Behavioral Scientist, *Matchmakers*, Blum et al., List & Puppe, Voskuil, LessWrong wiki missing from orders | Added | Consistency |

## Proposed new sections (not created)

The URLs below were fetched and confirmed this run (✔). Items marked ⧗ are strong candidates whose pages I could not fetch because of the budget exhaustion. Verify them before adding; I give full citations but deliberately no URLs or IDs for them.

### P1 · Economics of AI (labor, productivity, growth, agents)
- **Position:** Split current 11 into "11 — Economics of AI" and "12 — AI Alignment through an Economic Lens", or replace 11's generic alignment items with cross-references to philosophy/07 and ml/12.
- **Why:** The section title promises economics but delivers none. 2023–2026 produced the first credible causal evidence on generative AI and work. This is the most decision-relevant economics for Aaron, who runs a company and develops with AI assistance.
- **Outline:**
  1. Frameworks: task-based automation (displacement vs. reinstatement) and AI as cheap prediction.
  2. Micro evidence: RCTs and field studies of productivity (writing, customer support, consulting, software developers), including null and negative results.
  3. Measuring exposure and adoption: occupational exposure indices and usage-based indices.
  4. Labor-market outcomes 2024–26: early-career employment, earnings, hours.
  5. Macro: TFP and growth estimates, transformative-AI scenarios.
  6. AI agents as economic actors, plus mechanism design for AI: principal–agent alignment, social choice for RLHF.
- **Resources:**
  - ✔ Horton, Filippas & Manning — "Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus?" (2023) — https://www.nber.org/papers/w31122 (added to 08)
  - ✔ Conitzer et al. — "Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback" (2024) — https://arxiv.org/abs/2404.10271 (added to 09)
  - ✔ Royal Swedish Academy — "Contract Theory" popular background (2016; multitasking = Goodhart in contracts) — https://www.nobelprize.org/prizes/economic-sciences/2016/popular-information/ (added to 05)
  - ✔ Manheim & Garrabrant — "Categorizing Variants of Goodhart's Law" (2018) — https://arxiv.org/abs/1803.04585 (existing)
  - ✔ Fickinger, Zhuang, Hadfield-Menell & Russell — "Multi-Principal Assistance Games" (2020) — https://arxiv.org/abs/2007.09540 (existing, corrected)
  - ⧗ Acemoglu & Restrepo — "Automation and New Tasks: How Technology Displaces and Reinstates Labor", *JEP* 33(2), 2019
  - ⧗ Brynjolfsson, Li & Raymond — "Generative AI at Work" (NBER WP 2023; *QJE* 2025)
  - ⧗ Noy & Zhang — "Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence", *Science*, 2023
  - ⧗ Eloundou, Manning, Mishkin & Rock — "GPTs are GPTs: Labor Market Impact Potential of LLMs", *Science*, 2024
  - ⧗ Acemoglu — "The Simple Macroeconomics of AI" (NBER WP 2024)
  - ⧗ Humlum & Vestergaard — "Large Language Models, Small Labor Market Effects" (2025)
  - ⧗ Brynjolfsson, Chandar & Chen — "Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence" (Stanford Digital Economy Lab, 2025)
  - ⧗ Becker et al. (METR) — "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity" (2025). Especially relevant to Aaron's AI-assisted workflow.
  - ⧗ Handa et al. (Anthropic) — "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations" (Anthropic Economic Index, 2025)
  - ⧗ Hadfield-Menell & Hadfield — "Incomplete Contracting and AI Alignment" (AIES 2019)

### P2 · Empirical Economics & Causal Inference (econometrics)
- **Position:** After 01, as a methods track before 03/06/11. Cross-reference math/10 rather than duplicate it.
- **Why:** The curriculum is all theory; nothing teaches how economists establish causal claims. That skill is exactly what's needed to adjudicate the behavioral replication debates (03/06) and the AI-labor evidence (P1). math/10 covers Pearl's graphical and epidemiological traditions, not the design-based "credibility revolution" (2021 Nobel: Card, Angrist, Imbens).
- **Outline:**
  1. Potential outcomes and RCTs.
  2. Regression as conditional expectation.
  3. Instrumental variables.
  4. Difference-in-differences, event studies and synthetic control.
  5. Regression discontinuity.
  6. Power, p-hacking, publication bias and replication.
  7. Field experiments and scaling.
- **Resources:**
  - ✔ DellaVigna & Linos — "RCTs to Scale" (2022) — https://www.nber.org/papers/w27594 (added to 06)
  - ✔ Hagger et al. — "A Multilab Preregistered Replication of the Ego-Depletion Effect" (2016) — https://doi.org/10.1177/1745691616652873
  - ✔ Verschuere et al. — "Registered Replication Report on Mazar, Amir, and Ariely (2008)" (2018) — https://openaccess.city.ac.uk/id/eprint/20369/
  - ✔ Data Colada (blog) — https://datacolada.org/ (added to blogs)
  - ✔ math/10 (Hernán & Robins; Brady Neal) for the graphical side (existing)
  - ⧗ Angrist & Pischke — *Mastering 'Metrics: The Path from Cause to Effect* (Princeton UP, 2014)
  - ⧗ Angrist & Pischke — *Mostly Harmless Econometrics* (Princeton UP, 2009)
  - ⧗ Cunningham — *Causal Inference: The Mixtape* (Yale UP, 2021; free online)
  - ⧗ Huntington-Klein — *The Effect* (2021; free online)
  - ⧗ MRU — *Mastering Econometrics* video course with Joshua Angrist
  - ⧗ Angrist & Pischke — "The Credibility Revolution in Empirical Economics", *JEP*, 2010
  - ⧗ Royal Swedish Academy — 2021 popular background (natural experiments)

### P3 · Macroeconomics, Money & Financial Markets
- **Position:** Immediately before current 10, so money/crypto builds on a base.
- **Why:** There is no macro anywhere. Money-and-banking basics are missing, as are finance and market microstructure, even though they connect to 04 (auctions, order books) and 10 (exchanges, stablecoins). For a founder: interest rates, credit cycles, the cost of capital.
- **Outline:**
  1. National accounts.
  2. Growth (Solow/Romer).
  3. Business cycles and unemployment.
  4. Inflation and central banking.
  5. Money and banking, including the "money view" and the hierarchy of money.
  6. Financial crises.
  7. Asset pricing and market efficiency.
  8. Market microstructure (order books, spreads, HFT, frequent batch auctions).
  9. Corporate finance basics.
- **Resources:**
  - ✔ CORE Econ — *The Economy 2.0: Macroeconomics* — https://books.core-econ.org/the-economy/macroeconomics/0-3-contents.html (CORE added to 00)
  - ✔ Mankiw — *Principles of Economics* 10th ed. (macro chapters) — https://cengage.com/c/principles-of-economics-10e-mankiw/9780357722718 (existing)
  - ✔ Walsh — *Monetary Theory and Policy* (existing, 10)
  - ⧗ Mehrling — *Economics of Money and Banking* (Coursera/Columbia)
  - ⧗ Shiller — *Financial Markets* (Open Yale Courses ECON 252)
  - ⧗ MRU — *Principles of Economics: Macroeconomics*
  - ⧗ Bernanke — Nobel lecture "Banking, Credit, and Economic Fluctuations" (2022)
  - ⧗ Harris — *Trading and Exchanges: Market Microstructure for Practitioners* (OUP, 2003)
  - ⧗ Budish, Cramton & Shim — "The High-Frequency Trading Arms Race", *QJE*, 2015

### P4 (lower priority) · Industrial Organization & Competitive Strategy
Alternatively, widen 07 into "Networks, Platforms & IO".
- **Position:** After 07.
- **Why:** Market power, pricing and price discrimination, oligopoly, entry and antitrust/platform regulation are absent beyond Varian's chapters. These are directly useful to a hardware founder (pricing, competition, standards).
- **Outline:**
  1. Monopoly and price discrimination.
  2. Oligopoly (Cournot/Bertrand).
  3. Entry and deterrence.
  4. Vertical relations.
  5. Two-sided platforms.
  6. Antitrust and digital-platform regulation.
  7. Competitive strategy.
- **Resources:**
  - ✔ Royal Swedish Academy — "Market power and regulation" (2014 popular background; covers two-sided platforms) — https://www.nobelprize.org/prizes/economic-sciences/2014/popular-information/
  - ✔ Royal Swedish Academy — "Scientific Background: Market power and regulation" (2014) — https://www.nobelprize.org/prizes/economic-sciences/2014/advanced-information/
  - ✔ Rochet & Tirole 2003; Shapiro & Varian 1998; Briscoe, Odlyzko & Tilly 2006 (in 07)
  - ⧗ Belleflamme & Peitz — *Industrial Organization: Markets and Strategies* (2nd ed., CUP 2015) and *The Economics of Platforms* (CUP 2021)
  - ⧗ Cabral — *Introduction to Industrial Organization* (2nd ed., MIT Press 2017)
  - ⧗ Porter — "The Five Competitive Forces That Shape Strategy", *HBR*, 2008
  - ⧗ Stigler Committee on Digital Platforms — Final Report (2019)

Other gaps checked, and where they now live:
- Agent-based modeling: 08 (Mesa, Homo silicus).
- Public goods and the commons: 01 (Ostrom) and 09 (quadratic voting).
- Market design and matching: 04 (Nobel 2012 background; add Roth's book after verification).
- Contract theory: 05 (Nobel 2016 primer, plus existing Holmström and Bolton & Dewatripont).
- Auction theory: 04 is adequate; add Milgrom's *Putting Auction Theory to Work* (2004) after verification.

## Cut candidates

- **01 · Khan Academy Microeconomics:** exact duplicate of the 00 entry (both 🔑). Keep it only in 00.
- **05 or 07 · *Information Rules*:** listed in both, and twice in PROGRESS. Keep it in 07.
- **03 · *Predictably Irrational* and Ariely's Coursera course:** the author's research record is compromised, and the course may no longer be offered. One optional item at most, with the caveat.
- **11 · *Concrete Problems in AI Safety*, AI Safety Fundamentals, the Alignment Forum, *The Alignment Problem*:** duplicates of philosophy/07 (and ml/12 territory). Replace them with cross-references and use the space for P1.
- **10 · Voskuil's *Cryptoeconomics*:** idiosyncratic and wiki-hosted; adds little to an economics curriculum.
- **10 / books · 🔑 on *The Bitcoin Standard*:** demote to optional. btc/09 already carries it as 🔑, and there it now has its own balancing caveat.
- **00 · Dalio video as step 1:** demote to optional once P3 or CORE's macro volume exists.
- **08 / blogs · "Tim Roughgarden's Page":** a homepage typed as a blog, duplicated in the blogs file.
- **PROGRESS · "Books (supplementary)" block:** re-tracks the same items as the sections.

## Structural observations

- **Sequencing:**
  - Decision theory (03) should precede game theory (02).
  - Information economics (05) should precede, or be a prerequisite of, mechanism design (04).
  - Behavioral (06) should follow 03 directly. 03 is currently mostly behavioral, so 03 and 06 overlap; refocus 03 on normative theory.
  - An empirical-methods track is missing entirely (P2).
  - 11 conflates "alignment" with "economics of AI" (P1).
- **Overlaps with other curricula:**
  - **econ/10 ↔ btc/09:** both list *The Bitcoin Standard* as 🔑. btc/09 lists "Metcalfe's law" and "game theory of mining" as bare concepts with no resources. During this session btc/09 added links to econ/02 and econ/10 and caveated Ammous and Metcalfe. Division of labor: econ should own mainstream economic analysis (Budish's security-cost argument, the *JEL* crypto survey, EIP-1559 mechanism design, stablecoins); btc should own protocol-specific economics (halvings, fee market, selfish mining). econ/07's new "Metcalfe's Law is Wrong" gives btc/09 a concrete source to link.
  - **econ/02 ↔ btc/09:** mining is a natural worked example for 02. Better to keep it in btc and cross-link it.
  - **econ/11 ↔ philosophy/07 and ml/12:** Concrete Problems and AISF appear in phil/07, and RLHF/CAI/DPO live in ml/12. Keep only the economics-flavored alignment items in econ: Goodhart, assistance games, cooperative AI, incomplete contracting, social choice for RLHF.
  - **econ (proposed P2) ↔ math/10:** cross-reference; don't duplicate Pearl or Hernán.
  - **econ/03 ↔ philosophy:** decision theory and Newcomb.
  - **econ/08 ↔ ml/10 (RL):** no-regret learning and learning in games.
  - **econ/07 ↔ math/06:** graph theory.
- **Missing standard parts:**
  - No `econ/.agents/skills/update-curriculum/SKILL.md`, though the root README says every curriculum has one.
  - The Legend documents only 🔑.
  - Many "—" years and missing links on books that have free legal PDFs (Nobel lectures, author-hosted papers), which hurts the NotebookLM workflow.
- **Epistemics:** There is no curriculum-wide way to flag contested or non-replicating material. I used inline ⚠️ in descriptions (03, 06). I recommend formalizing ⚠️ in the Legend for all curricula.
- **Balance:** The intro and money sections lean Austrian/libertarian (Hazlitt, Read, Hayek ×2, Ammous 🔑, Voskuil, a mises.org link) with no mainstream macro or money text. CORE and the caveats help; P3 would fix it.
- **Type labels:** 📝 Blog is used for homepages and video series (Spaniel, Roughgarden), and Nobel lectures are typed variously as 📄, 🎥 or 📝. Minor, but worth a convention.
- **PROGRESS:** Double-tracking in the Books block. The sections and PROGRESS are otherwise now in sync.
- **Post-merge scaffold pass (no web calls):** Aligned the merged 🎯/🛠️/✅ blocks with these corrections:
  - 02: Coursera instructors; Axelrod & Hamilton cited for the strategy-properties exercise.
  - 03: vNM axioms → 1947 appendix; the hot-hand exercise is made self-contained; the "train wreck" source is cited.
  - 06: DellaVigna (2009) and DellaVigna & Linos cited; the PNAS exchange is now optional; the Ariely decoy is flagged as a hypothesis to test.
  - 08: Calvano et al. mini-project made self-contained.
  - 10: Budish exercise made self-contained, with its inequality stated inline; Dalio pointer → Section 00.
  - 11: DeepMind list made optional.
  
  Dependencies still outside the lists: **Budish (2018, "The Economic Limits of Bitcoin and the Blockchain"; the scaffold cites NBER WP 24717, which I could not verify) should be verified and added to Section 10**, and Calvano et al. (2020, *AER*) to Section 08. Other unlisted papers (Gode & Sunder in 01, Miller & Sanjurjo in 03, Gao et al. in 11) are attributions only; those exercises are fully specified without them.

## Top 5 priorities for Aaron in this curriculum

1. **Read the economics of AI, not just alignment.** Approve P1, starting with the task-based framework and the 2023–26 productivity and labor studies. The METR developer RCT and the Anthropic Economic Index bear directly on his AI-assisted engineering workflow.
2. **Build evidence literacy before the behavioral sections.** Read the "Train Wreck" audit, DellaVigna & Linos, and Data Colada alongside Kahneman, Thaler and Ariely. Add the econometrics track (P2) so empirical claims can be judged, not just collected.
3. **Fix the order in practice.** Do normative decision theory (SEP *Decision Theory*, the vNM appendix) before game theory, and information economics before mechanism design. Then add Axelrod and the bargaining book before Section 11.
4. **Get a macro, money and finance base before Section 10.** Start now with CORE's macro volume, then P3 (Mehrling, Shiller). Read crypto through mainstream analyses as well as Ammous.
5. **Use the founder-relevant tools.** Market design (Nobel 2012 matching), contracts and incentives (Nobel 2016 primer), platforms and IO (Tirole background, P4), and QuantEcon/Mesa for hands-on Python modeling.


## Follow-up pass (2026-10-13)
- **New sections created:**
  - `econ/12-economics-of-ai/` · take after 11 (with 13 before or alongside) · 13 resources
  - `econ/13-empirical-economics-and-causal-inference/` · take after 01 · 10 resources (cross-links math/10 instead of duplicating it)
  - `econ/14-macroeconomics-money-and-financial-markets/` · take before 10 · 11 resources (educational only; no investment advice)
  - `econ/15-industrial-organization-and-strategy/` · take after 07 · 9 resources
  - Section 11 retitled "AI Alignment through an Economic Lens" (H1, README learning path, PROGRESS heading; directory unchanged). Its intro now points to 12 for the economics of AI and to philosophy/07 and ml/12 for alignment as such. README "Keeping Current" now points to 12. Pointers to the new sections were added in 00, 01, 02, 03, 04, 05, 06, 07, 08 and 10. Key titles were also added to `books/` (5) and `courses/` (4). Every check value in the new practice blocks was computed in Python; the 13 values use the `causaldata` datasets.
- **Added:**
  - Automation and New Tasks: How Technology Displaces and Reinstates Labor — Daron Acemoglu & Pascual Restrepo — 2019 — 12
  - Artificial Intelligence: The Ambiguous Labor Market Impact of Automating Prediction — Ajay Agrawal, Joshua S. Gans & Avi Goldfarb — 2019 — 12
  - GPTs are GPTs: An Early Look at the Labor Market Impact Potential of Large Language Models — Tyna Eloundou, Sam Manning, Pamela Mishkin & Daniel Rock — 2023 (Science 2024) — 12
  - Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations — Kunal Handa, Alex Tamkin, Miles McCain et al. — 2025 — 12
  - Generative AI at Work — Erik Brynjolfsson, Danielle Li & Lindsey Raymond — 2025 (NBER WP 2023) — 12
  - Experimental Evidence on the Productivity Effects of Generative Artificial Intelligence — Shakked Noy & Whitney Zhang — 2023 — 12
  - Navigating the Jagged Technological Frontier — Fabrizio Dell'Acqua, Edward McFowland III, Ethan R. Mollick et al. — 2023 — 12
  - The Impact of AI on Developer Productivity: Evidence from GitHub Copilot — Sida Peng, Eirini Kalliamvakou, Peter Cihon & Mert Demirer — 2023 — 12
  - Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity — Joel Becker, Nate Rush, Elizabeth Barnes & David Rein — 2025 — 12
  - Still Waters, Rapid Currents: Early Labor Market Transformation under Generative AI — Anders Humlum & Emilie Vestergaard — 2025 — 12 (first circulated as "Large Language Models, Small Labor Market Effects", BFI WP 2025-56)
  - Canaries in the Coal Mine? Six Facts about the Recent Employment Effects of Artificial Intelligence — Erik Brynjolfsson, Bharat Chandar & Ruyu Chen — 2025 (rev. Aug 2026) — 12
  - The Simple Macroeconomics of AI — Daron Acemoglu — 2024 (Economic Policy 2025) — 12
  - Scenarios for the Transition to AGI — Anton Korinek & Donghyun Suh — 2024 — 12
  - Mastering 'Metrics: The Path from Cause to Effect — Joshua D. Angrist & Jörn-Steffen Pischke — 2014 — 13
  - Mastering Econometrics (MRU course) — Joshua Angrist — n.d. — 13
  - Causal Inference: The Mixtape — Scott Cunningham — 2021 — 13
  - The Effect: An Introduction to Research Design and Causality (2nd ed.) — Nick Huntington-Klein — 2025 — 13
  - Mostly Harmless Econometrics: An Empiricist's Companion — Joshua D. Angrist & Jörn-Steffen Pischke — 2009 — 13
  - The Credibility Revolution in Empirical Economics — Joshua D. Angrist & Jörn-Steffen Pischke — 2010 — 13
  - Natural experiments help answer important questions (Nobel 2021 popular background) — Royal Swedish Academy of Sciences — 2021 — 13
  - Evaluating replicability of laboratory experiments in economics — Colin F. Camerer, Anna Dreber, Eskil Forsell et al. — 2016 — 13
  - Star Wars: The Empirics Strike Back — Abel Brodeur, Mathias Lé, Marc Sangnier & Yanos Zylberberg — 2016 — 13
  - causaldata (example datasets, v0.1.5) — Nick Huntington-Klein — 2024 — 13
  - Economics of Money and Banking (Coursera) — Perry G. Mehrling — n.d. — 14
  - Financial Markets (Open Yale ECON 252) — Robert J. Shiller — 2011 — 14
  - Principles of Macroeconomics (MRU) — Tyler Cowen & Alex Tabarrok — n.d. — 14
  - Money creation in the modern economy — Michael McLeay, Amar Radia & Ryland Thomas — 2014 — 14
  - The Fed Explained: What the Central Bank Does (11th ed.) — Board of Governors of the Federal Reserve System — n.d. — 14
  - The laureates explained the central role of banks in financial crises (Nobel 2022 popular background) — Royal Swedish Academy of Sciences — 2022 — 14
  - Bank Runs, Deposit Insurance, and Liquidity — Douglas W. Diamond & Philip H. Dybvig — 1983 — 14
  - Trendspotting in asset markets (Nobel 2013 popular background) — Royal Swedish Academy of Sciences — 2013 — 14
  - Bid, ask and transaction prices in a specialist market with heterogeneously informed traders — Lawrence R. Glosten & Paul R. Milgrom — 1985 — 14
  - The High-Frequency Trading Arms Race: Frequent Batch Auctions as a Market Design Response — Eric Budish, Peter Cramton & John Shim — 2015 — 14
  - FRED (Federal Reserve Economic Data) — Federal Reserve Bank of St. Louis — n.d. — 14
  - Introduction to Industrial Organization (2nd ed.) — Luis Cabral — 2017 — 15
  - Market power and regulation (Nobel 2014 popular background) — Royal Swedish Academy of Sciences — 2014 — 15
  - Scientific Background: Market power and regulation — Royal Swedish Academy of Sciences — 2014 — 15
  - Industrial Organization: Markets and Strategies (2nd ed.) — Paul Belleflamme & Martin Peitz — 2015 — 15
  - The Economics of Platforms: Concepts and Strategy — Paul Belleflamme & Martin Peitz — 2021 — 15
  - The Five Competitive Forces That Shape Strategy — Michael E. Porter — 2008 — 15
  - Amazon's Antitrust Paradox — Lina M. Khan — 2017 — 15
  - Antitrust in a time of populism — Carl Shapiro — 2018 — 15
  - Stigler Committee on Digital Platforms: Final Report — Stigler Center, Chicago Booth — 2019 — 15
  - Artificial Intelligence, Algorithmic Pricing, and Collusion — Emilio Calvano, Giacomo Calzolari, Vincenzo Denicolò & Sergio Pastorello — 2020 — 08 (mini-project's "not in the list" note removed)
  - The Microeconomics of Cryptocurrencies — Hanna Halaburda, Guillaume Haeringer, Joshua S. Gans & Neil Gandal — 2022 — 10
  - The Economic Limits of Bitcoin and the Blockchain (published as "Trust at Scale", QJE 140(1), 2025) — Eric Budish — 2018 — 10 (Practice 3's "outside reading" note removed; also in btc/09, the one-home section for Bitcoin economics)
  - Transaction Fee Mechanism Design for the Ethereum Blockchain: An Economic Analysis of EIP-1559 — Tim Roughgarden — 2020 — 10
  - Anatomy of a Run: The Terra Luna Crash — Jiageng Liu, Igor Makarov & Antoinette Schoar — 2023 (JFE 2026) — 10
  - III. The next-generation monetary and financial system (BIS Annual Economic Report 2025) — Bank for International Settlements — 2025 — 10
  - Incomplete Contracting and AI Alignment — Dylan Hadfield-Menell & Gillian K. Hadfield — 2019 — 11
- **Removed (confirmed nonexistent):** none.
- **Flags resolved:**
  - `econ/08-computational-economics/README.md:39` (+ PROGRESS.md:140) — Homo Silicus authorship. The checker thought WP 31122 was by Horton alone. NBER WP 31122 (issued Apr 2023, revised Feb 2026) and arXiv 2301.07543 v2 (26 Feb 2026) both list John J. Horton, Apostolos Filippas & Benjamin S. Manning, so the row was correct. The year cell is now "2023 (rev. 2026)". Evidence: https://www.nber.org/papers/w31122 · https://arxiv.org/abs/2301.07543
  - `econ/blogs-and-references/README.md:14` — Money Illusion status. Confirmed: "A long strange trip" (1 Sept 2024) says "This will be my final Money Illusion post" and points to scottsumner.substack.com, titled *The Pursuit of Happiness*. Replaced the ageing "now writes at" with dated wording. Evidence: https://www.themoneyillusion.com/a-long-strange-trip/ · https://scottsumner.substack.com/
  - `econ/10-monetary-economics-and-crypto/README.md:31, 53, 67` (+ PROGRESS.md:168) — Hayek's title. Now *Denationalisation of Money: The Argument Refined*, year "1976 (2nd ed. 1978)". The row notes that the 1976 first edition was subtitled *An Analysis of the Theory and Practice of Concurrent Currencies*, and that the link is the IEA's 1990 text hosted by the Mises Institute (an advocacy site). The IEA's own page failed to load, so the link is unchanged. Evidence: https://mises.org/library/denationalisation-money-argument-refined · https://libcat.library.tamu.edu/Record/in00000504000 (2nd ed., 1978, Hobart Paper 70) · https://fff.org/?p=25637 (1976 first edition)
  - `econ/00-economic-thinking/README.md:38` vs `:32` — The Dalio order step contradicted the hedged row. Step 1 is now an "optional warm-up: one investor's model of credit cycles, not textbook macroeconomics", to check against CORE's macro volume and Section 14. Editorial; no lookup needed.
  - `econ/10-monetary-economics-and-crypto/README.md:73` — The treasury mini-project was close to investment advice. Added "This is an operations-cost and risk analysis for a business, not investment advice." Editorial.
  - `econ/*/README.md` (V5 cross-curriculum flag) — Mini-project paths lacked the `NN-` prefix. All 12 are now `projects/econ/NN-<name>/`, matching STUDY-GUIDE and projects/README; the four new sections follow the same convention.
  - This review's own open dependencies: Budish (NBER WP 24717, verified with its *QJE* 140(1) DOI 10.1093/qje/qjae033) is added to 10, and Calvano et al. (*AER* 110(10), DOI 10.1257/aer.20190623) to 08. Evidence: https://www.nber.org/papers/w24717 · https://api.crossref.org/works/10.1093/qje/qjae033 · https://api.crossref.org/works/10.1257/aer.20190623
- **Still unverified:**
  - Harris, *Trading and Exchanges* (OUP 2003) — not attempted (OUP pages refused fetches last run). Microstructure is covered by Glosten & Milgrom and Budish, Cramton & Shim instead.
  - Bernanke's 2022 Nobel lecture — not added; the 2022 popular background was verified and used instead.
  - Halaburda et al. JEL DOI (10.1257/jel.20201552) — Crossref and AEA fetches errored. The row links the verified NBER WP page, which carries the JEL 60(3):971–1013 citation.
  - Camerer et al. (2016) headline numbers — science.org refused the fetch, so the row gives no replication rate.
  - Dell'Acqua et al.: the size of the outside-the-frontier effect is unclear ("19%" in the SSRN abstract; percentage points or relative not determined), so the row gives no number.
  - The Effect's first-edition year — not checked; the row cites the verified 2nd edition (Chapman & Hall, 2025).
  - The Fed Explained (11th ed.) — the edition year is not stated on the Fed's page; the Year cell is "—".
  - A Crossref bibliographic query for "Trust at Scale" returned HTTP 429 and was not refetched. The DOI record itself verified fine.

## Link-audit fixes (2026-10-13)
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| econ/00-economic-thinking/README.md:28 ; econ/courses/README.md:17 | MRU Principles at `mru.org/principles-economics-microeconomics` (302) | `learn.mru.org/courses/principles-of-microeconomics` (L3-104) | https://learn.mru.org/courses/principles-of-microeconomics |
| econ/02-game-theory/README.md:31 ; econ/books/README.md:16 | Osborne & Rubinstein, *A Course in Game Theory*, at `books.osborne.economics.utoronto.ca/coursesingt` (4xx) | The authors' page for the book, which offers the free electronic text (L3-017) | https://www.economics.utoronto.ca/osborne/cgt/ |
| econ/03-decision-theory/README.md:37, 53 ; econ/courses/README.md:11 | Ariely, Behavioral Economics (Coursera), `coursera.org/learn/predictably-irrational` (4xx twice) | Row kept; "⚠️ Link dead (checked Oct 2026)" appended; order step 8 marked "(optional; link dead)". Coursera's search page is robots-blocked, so no replacement was found (L2-026) | https://www.coursera.org/search?query=behavioral%20economics (robots-blocked) |
| econ/04-mechanism-design/README.md:31 | Krishna, *Auction Theory*, at `www.elsevier.com/books/…` (302) | `shop.elsevier.com/books/…` (L3-062) | https://shop.elsevier.com/books/auction-theory/krishna/978-0-12-374507-1 |
| econ/04-mechanism-design/README.md:33 | Ausubel & Milgrom, "The Lovely but Lonely Vickrey Auction", Stanford-hosted PDF (4xx; Milgrom's pages moved to robots-blocked milgrom.net) | Stanford SIEPR's page for the August 2004 working paper, which links the free PDF; the description says so. It is the sole source for objective 5 and Practice 4, so one WebSearch was used (L3-164) | https://siepr.stanford.edu/publications/working-paper/lovely-lonely-vickrey-auction |
| econ/06-behavioral-economics/README.md:37, 57 | Behavioral Economics in Action (Coursera), `…/learn/behavioural-economics-in-action` (4xx twice) | Row kept; "⚠️ Link dead (checked Oct 2026)" appended; order step 9 marked "(optional; link dead)". The US-spelling slug also fails, and U of T's Coursera partner page does not show the course (L2-024) | https://www.coursera.org/learn/behavioral-economics-in-action (4xx) · https://www.coursera.org/utoronto |
| econ/07-network-economics/README.md:30 | Rochet & Tirole at JSTOR `stable/3590984`, which is a different paper (Houseman, Kalleberg & Erickcek, *ILR Review* 2003) | DOI for *JEEA* 1(4), 2003 (L3-086) | https://doi.org/10.1162/154247603322493212 |
| econ/07-network-economics/README.md:33 ; econ/courses/README.md:13 | Jackson's course at `…/learn/social-and-economic-networks` (4xx) | `…/learn/social-economic-networks`, the canonical slug (L1-027) | https://www.coursera.org/learn/social-economic-networks |
| econ/08-computational-economics/README.md:33 | Arora, Hazan & Kale at `cs.princeton.edu/~arora/pubs/MWsurvey.pdf` (302 to his homepage) | The open-access *Theory of Computing* 8(6) article page (L1-029) | https://theoryofcomputing.org/articles/v008a006/ |
| econ/08-computational-economics/README.md:34 | "Algorithmic Game Theory (CS364B)", year "—" | "Frontiers in Mechanism Design (CS364B)", 2014 (Winter 2014 offering); order step and PROGRESS name only "CS364B", so unchanged (L1-159) | https://timroughgarden.org/w14/w14.html |
| econ/11-ai-alignment-economics-and-frontiers/README.md:44, 61, 73 ; econ/courses/README.md:15 ; econ/PROGRESS.md:190 | "AI Safety Fundamentals" at `aisafetyfundamentals.com` (302 to bluedot.org; the AISF name no longer appears there) | "BlueDot Impact AI safety courses (formerly AI Safety Fundamentals)" at `bluedot.org`, matching philosophy/07; the row notes the redirect, and the order step, Practice 5 source and PROGRESS line were renamed to match (L1-006) | https://bluedot.org/ |
- Already fixed in the follow-up pass above: Hayek (10:31; L2-102). The title and the "link is the 1990 IEA text" note were already there; "1990 printing" now reads "3rd ed., 1990", per the audit's fix_meta.
- Left unchanged because the auditor could not load the page and none is flagged as probably dead: Friedman (01:32; L1-032), Vickrey 🔑 (04:29; L1-086), Myerson 1981 (04:32; L1-087), Bolton & Dewatripont (05:33, books/README.md:17; L1-103), Sen (09:30; L2-074), Nash (02:33; L2-085), NotebookLM (README:9; L2-114), *Nudge* 🔑 (06:31; L2-128), Akerlof 🔑 (05:29; L3-083), Gibbard (09:31; L3-084), Arrow 🔑 (09:29, books/README.md:18; L3-166), and The Economist, *Games and Economic Behavior* and SSRN (blogs-and-references/README.md:24, 38, 47; L3-061, L3-147, L3-151).
- Katz & Shapiro (07:31; L2-083): the auditor suspects JSTOR `stable/1816044` is the wrong id (from memory, `1814809`). A Crossref check today got HTTP 429 and was not retried, so the link is unchanged. Check it by hand.

## Tier lists (2026-10-13)
🔑 trimmed to ≤3 per section; each Suggested Order now opens with a "Core path" line. Reverse any call by re-adding 🔑 to the row and the Core path line.
| Section | 🔑 kept | 🔑 removed (why, ≤8 words) |
|---|---|---|
| 10 | Nakamoto, Bitcoin whitepaper; Gensler, *Blockchain and Money* (MIT) | Ammous, *The Bitcoin Standard* (advocacy book; core excludes advocacy items) |
- `econ/books/README.md:19`: 🔑 removed from *The Bitcoin Standard*, which lost its 🔑 in Section 10, its only econ section.
- Core path lines added to all 16 sections (00–15). No section had more than 3 🔑 resource rows (31 before, 30 after; 01 has 3; 07, 09 and 13 have 1; the rest have 2), so Ammous is the only marker change, and no section has 0 🔑.
- books/README.md #7 Thaler & Sunstein, *Nudge*: 🔑 added (core in 06)
- books/README.md #19 Angrist & Pischke, *Mastering 'Metrics*: 🔑 added (core in 13)
- books/README.md #22 Cabral, *Introduction to Industrial Organization* (2nd ed.): 🔑 added (core in 15)
- courses/README.md #15 Mehrling, Economics of Money and Banking: 🔑 added (core in 14)
- courses/README.md #16 Shiller, Financial Markets (ECON 252): 🔑 added (core in 14)
- econ/README.md legend: 🔑 row now reads "**Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line"
- Second check (2026-10-13), from `independent-check.md` "Second check":
  - 01: Khan Academy demoted (review aid, already core in 00).
  - 03: SEP "Decision Theory" (Steele & Stefánsson) made 🔑, so the normative side is on the core path.
  - 12: Acemoglu, "The Simple Macroeconomics of AI" made 🔑, so the skeptical estimate is on the core path.
  - Each Core path line was updated to match.
