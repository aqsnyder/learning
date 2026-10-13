# Philosophy of Mind & Intelligence — Review

> **Deep-dive review, October 2026** · curriculum: [`philosophy/`](../../philosophy/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict
The curriculum has a sound arc (foundations, then mind and consciousness, then computation, then AI, ethics and risk, then language, free will, Buddhism, and frontiers), and its canonical core is right: Nagel, Chalmers, Dennett, Searle, Turing, Kim, GEB and Bostrom. It falls short in three ways.

- **Accuracy.** It contained classic AI-generation errors. One paper was misattributed (Chalmers's "Could a Large Language Model be Conscious?" was credited to "Schneider & Turner 2024"). One co-author was wrong (Shlegeris for Mindermann). Three resources did not exist: an "Amy Kind philosophy of mind" playlist that is really Wi-Phi's critical-thinking series, an SEP "Extended Mind" entry, and an SEP "hard problem" anchor. Some links were wrong (the Gutenberg link for the *Meditations* is the *Discourse on Method*; the Chalmers 1995 DOI points to *Mind* rather than *JCS*).
- **Balance and currency.**
  - The LLM-understanding debate cited only skeptics.
  - Consciousness science stopped at 2021 and presented IIT uncritically.
  - Section 07 had nothing after 2023.
  - The Wolfram material was presented as quasi-established science.
- **Coverage.** Section 00 promised logic and offered no logic resource. There was no ethics primer, no personal identity, no account of what "intelligence" means, and no philosophy of science.

Overall grade as found: **C+**. After this pass (31 corrections, 32 verified additions, a complete PROGRESS tracker) it is roughly a **B**. The single most important remaining improvement is to **add a Philosophy of Science & Scientific Reasoning section** (proposed below). It is the missing hub between this curriculum and Aaron's physics, ML and bio curricula, and it is what lets him judge IIT vs. GNWT, Wolfram, or an ML benchmark claim on the merits.

> **Verification limits this session:** the shared WebSearch budget (200 per turn) and then the shared WebFetch budget (800 per hour) ran out partway through. These pages could not be read because of rate limiting (HTTP 429): `api.crossref.org/works/10.2307/2181485` (Frege), `plato.stanford.edu/entries/popper/`, and `coursera.org/learn/philosophy-physical-sciences`. Every resource I added was fetched and verified. Strong candidates I could not verify are listed as "recommended next (verify first)" and were **not** added.

## Scorecard
Scores are 1–5 for the curriculum as found. The grade column gives the grade as found, then the grade after this pass.

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 Foundations | 2 | 3 | 4 | 4 | 3 | C → B | Promised logic and argument skills but had no logic resource and no ethics; the Descartes link went to the wrong book |
| 01 Philosophy of Mind | 3 | 3 | 4 | 4 | 4 | B- → B+ | Good canon (Kim, Nagel, Putnam, Jackson); the video item didn't exist; no personal identity |
| 02 Consciousness | 3 | 3 | 2 | 4 | 4 | C+ → A- | Classic philosophy was fine; the science was stale and one-sided (no GWT/HOT resource, IIT uncritical); a phantom SEP anchor and a wrong DOI |
| 03 Computation & Mind | 3 | 3 | 3 | 4 | 3 | C+ → B+ | GEB spine is strong; Gödel was promised but absent; no connectionism debate; Wolfram was oversold |
| 04 Intelligence & Understanding | 2 | 3 | 2 | 3 | 3 | C → B | Really "4E cognition"; never defined intelligence; cited a nonexistent SEP entry; nothing after 2008 |
| 05 Philosophy of AI | 3 | 4 | 3 | 4 | 4 | B- → A- | Classic arguments are well chosen; the LLM debate cited only skeptics |
| 06 Ethics of AI | 3 | 3 | 3 | 4 | 3 | C+ → B | Strong on algorithmic harms; promised "moral status of AI" and "accountability" but had no resource on either; one book title was wrong |
| 07 X-Risk & Alignment | 3 | 3 | 2 | 4 | 4 | C+ → B+ | Bostrom and Russell are fine; it lacked a rigorous argument, normative alignment, a skeptic, and anything after 2023; it had a co-author error |
| 08 Language & Meaning | 3 | 4 | 3 | 4 | 4 | B- → B | Wittgenstein, Austin and Grice are good; no Frege, Kripke or Putnam (reference) and no distributional semantics |
| 09 Free Will & Agency | 3 | 4 | 3 | 4 | 4 | B- → B+ | Sound core; the Libet reading was dated, Sapolsky went unanswered, and the intro was partisan |
| 10 Eastern Philosophy & Mind | 2 | 4 | 3 | 4 | 4 | C+ → B- | Good Buddhist reading list, but the title promises "Eastern" and the content is Buddhist only |
| 11 Frontiers | 3 | 2 | 3 | 3 | 3 | C → B+ | A headline paper was misattributed and unlinked; the IIT 4.0 authors were wrong; no AI welfare; padded (Tegmark, Alignment Forum) |
| books/ | 3 | 4 | 3 | — | 4 | B- | Coherent short list; missing Parfit and a logic text (both added) |
| courses/ | 2 | 2 | 3 | — | 3 | C | The 🔑 #1 course was mislabeled, the 🔑 #3 link was broken (and the course is in French), and one title was wrong |
| blogs-and-references/ | 3 | 4 | 3 | — | 3 | B- | Fine core (SEP, PhilPapers, IEP); stale AISF name; no podcasts or AI-consciousness blogs |
| PROGRESS.md | 2 | 3 | — | — | — | C → A- | Listed only about the first 6–7 items per section; one orphan line; three stale or misattributed lines |

## Section-by-section

### 00 — Foundations of Philosophy
- **Strengths:** Blackburn's *Think* and Nagel's *What Does It All Mean?* are the right on-ramp, and the primary texts (Meno, Descartes, Hume) are classic.
- **Problems:**
  - ✔ The Descartes link pointed to Gutenberg #59, which is the *Discourse on Method*. It now points to Bennett's free *Meditations* translation.
  - ✔ The SEP "Logic and Ontology" entry was described as "the formal reasoning tools." It is Hofweber's advanced metaphysics-of-logic entry; it is now described accurately and marked optional.
  - ✱ The Edinburgh Coursera course is not in the Suggested Order.
- **Missing:** an actual logic or argument toolkit (now added); a normative ethics primer, which Sections 06 and 07 assume (now added); philosophy of science (see the proposal).
- **Added:**
  - Introduction to Critical Thinking (playlist) — Wireless Philosophy — n.d.
  - forall x: Calgary — Magnus, Button, Thomas-Bolduc, Zach — 2023
  - 1000-Word Philosophy, Ethics essays (consequentialism, Kantian deontology, virtue ethics, social contract) — Gronholz, Chapman, Merry, Antonini — n.d.

### 01 — Philosophy of Mind
- **Strengths:** Kim as the spine; Nagel, Putnam and Jackson are the right classic papers; the order is sensible.
- **Problems:**
  - ✔ The "Philosophy of Mind — Amy Kind — Wi-Phi" playlist does not exist. The link is Wi-Phi's *Introduction to Critical Thinking*. It was replaced with the real Edinburgh course *Philosophy and the Sciences: Introduction to the Philosophy of Cognitive Sciences*, and the critical-thinking playlist moved to Section 00.
  - ✔ Same Gutenberg #59 link error as Section 00.
  - ✔ Putnam and SEP Functionalism were 🔑 in the section but not in PROGRESS.
- **Missing:**
  - Personal identity (added).
  - Intentionality and Dennett's intentional stance, which matters for LLM agents (recommended next: Dennett, *The Intentional Stance*, 1987; not verified).
  - The problem of other minds.
  - Princess Elisabeth's objection to Descartes (it is in Bennett's free Descartes correspondence).
- **Added:**
  - Personal Identity (SEP) — Eric T. Olson — rev. 2023
  - Reasons and Persons (Part III) — Derek Parfit — 1984

### 02 — Consciousness
- **Strengths:** Chalmers and Dennett are paired well; Block's access/phenomenal distinction is included.
- **Problems:**
  - ✔ The Chalmers 1995 DOI (`10.1093/mind/104.414.200`) has no Crossref record. The paper is in *JCS* 2(3):200–219. The link now goes to consc.net.
  - ✔ "SEP — The Hard Problem of Consciousness" linked to `consciousness/#HarP`, an anchor that doesn't exist (the SEP entry only mentions the hard problem in §5.4). Replaced with the dedicated IEP entry (Weisberg).
  - ✔ IIT was presented as "a leading scientific theory" with no mention of the 2023 letter or the 2025 results. The Tononi and Koch descriptions now flag this.
  - ✔ The intro promised higher-order and global-workspace theories but listed no resource for either.
- **Missing:** illusionism (added); the neuroscience of GWT (added); animal and comparative consciousness (✱ recommend Birch, *The Edge of Sentience*, 2024; not verified).
- **Added:**
  - Theories of Consciousness (*Nat Rev Neurosci*) — Anil K. Seth, Tim Bayne — 2022 🔑
  - Consciousness and the Brain — Stanislas Dehaene — 2014
  - Illusionism as a Theory of Consciousness — Keith Frankish — 2016
  - Consciousness theory slammed as 'pseudoscience' (*Nature* news) — Mariana Lenharo — 2023
  - Adversarial testing of GNWT and IIT (*Nature*) — Cogitate Consortium — 2025

### 03 — Computation and Mind
- **Strengths:** GEB as the spine; Turing 1936, the Chinese Room and Penrose give a good dialectic.
- **Problems:**
  - ✔ The intro and PROGRESS promised Gödel ("Gödel's Incompleteness Theorems (overview)"), but there was no Gödel resource. Added the SEP entry and fixed the PROGRESS orphan.
  - ✔ The SEP "Computationalism" entry's real title is "The Computational Theory of Mind" (Rescorla).
  - ✔ **Wolfram framing (July 2026 additions):**
    - NKS's Principle of Computational Equivalence was presented as "a radical extension of Church-Turing." It is now described as an unproven *conjecture*; the description notes reviewers' criticism, credits Matthew Cook with the Rule 110 proof, and adds Aaronson's critical review as a counterweight.
    - The ruliad entry claimed "consciousness and mind are patterns within this structure." It is now labelled **"a speculative research program, not established physics,"** with Wolfram's own "very beginning" caveat quoted, the link moved to the canonical writings.stephenwolfram.com URL, and the year corrected to 2021.
    - Both Wolfram entries are kept and marked optional in the Suggested Order.
  - ✱ The Mind's I is not in the Suggested Order.
- **Missing:** the symbolic-vs-connectionist debate (added); computational complexity as a philosophical tool (added).
- **Added:**
  - Gödel's Incompleteness Theorems (SEP) — Panu Raatikainen — rev. 2025
  - Connectionism and Cognitive Architecture — Fodor & Pylyshyn — 1988
  - Why Philosophers Should Care About Computational Complexity — Scott Aaronson — 2011
  - Book Review: 'A New Kind of Science' — Scott Aaronson — 2002

### 04 — Intelligence and Understanding
- **Strengths:** Strong 4E-cognition canon (Varela, Thompson & Rosch; Clark & Chalmers; Brooks; Dreyfus; Heidegger).
- **Problems:**
  - ✔ "SEP — Extended Mind" does not exist (the URL fails while other SEP pages load). Repointed to SEP "Externalism About the Mind" §§5–7, which covers the extended mind.
  - ✔ The Dreyfus title and year were mismatched: "The Limits of Artificial Intelligence" is the 1979 edition's subtitle; the 1972 edition is "A Critique of Artificial Reason."
  - ✔ The title promised "intelligence" but the content had no account of what intelligence is (added). One sentence was added to the intro.
- **Missing:** definitions and measures of intelligence (added); predictive processing (added); animal and octopus cognition (✱ Godfrey-Smith, *Other Minds*, 2016; not verified).
- **Added:**
  - Universal Intelligence: A Definition of Machine Intelligence — Legg & Hutter — 2007
  - On the Measure of Intelligence — François Chollet — 2019
  - Whatever Next? Predictive Brains, Situated Agents… — Andy Clark — 2013

### 05 — Philosophy of AI
- **Strengths:** The Turing, Searle, Harnad and Dreyfus arc is canonical and well ordered.
- **Problems:**
  - ✔ The *Stochastic Parrots* description reduced a mainly risk-focused paper (costs, data, the danger of ascribing meaning) to "LLMs don't understand." Rewritten.
  - ✔ The modern debate was one-sided: both modern items were by Bender et al. Mitchell & Krakauer (🔑) and two philosophical surveys were added for balance.
- **Missing:** the frame problem (covered only inside SEP AI); the intentional stance (see 01).
- **Added:**
  - The Debate Over Understanding in AI's Large Language Models — Mitchell & Krakauer — 2023 🔑
  - Talking About Large Language Models — Murray Shanahan — 2022
  - A Philosophical Introduction to Language Models, Part I — Millière & Buckner — 2024

### 06 — Ethics of AI
- **Strengths:** Concrete harms (O'Neil, Eubanks, Benjamin, Crawford), a philosophical anthology (Liao), and a free technical fairness text.
- **Problems:**
  - ✔ Coeckelbergh's book is *AI Ethics* (MIT Press Essential Knowledge, 2020), not "The Ethics of Artificial Intelligence: An Introduction."
  - ✔ Barocas, Hardt & Narayanan was typed 📄 Paper; it is a book.
  - ✱ The section is more sociology than philosophy.
  - ✱ The intro's "moral status of AI" has no dedicated item here; it is covered in Section 11 via *Taking AI Welfare Seriously*.
- **Missing:** responsibility gaps (added); up-to-date "what actually works" evidence (added); ✱ machine ethics and value alignment, which is covered by Gabriel in Section 07.
- **Added:**
  - The Responsibility Gap — Andreas Matthias — 2004
  - AI Snake Oil — Narayanan & Kapoor — 2024

### 07 — Existential Risk and Alignment
- **Strengths:** Bostrom, Russell, Christiano and Amodei form the right historical core.
- **Problems:**
  - ✔ "Ngo, Chan, Shlegeris": the third author is Sören Mindermann, and the year is 2022 (arXiv v1).
  - ✔ "AI Safety Fundamentals" is now BlueDot Impact (aisafetyfundamentals.com returns a 302 to bluedot.org). Fixed here and in blogs.
  - ✔ Nothing after 2023, in the fastest-moving topic in the curriculum.
- **Missing:** the most rigorous argument (added); "aligned to what?" (added); a serious skeptic (added); the current evidence base (added). ✱ Optional: Yudkowsky & Soares, *If Anyone Builds It, Everyone Dies* (2025), as the prominent recent doom statement (not verified).
- **Added:**
  - Is Power-Seeking AI an Existential Risk? — Joseph Carlsmith — 2022
  - Artificial Intelligence, Values, and Alignment — Iason Gabriel — 2020
  - AI as Normal Technology — Narayanan & Kapoor — 2025
  - International AI Safety Report 2026 — Yoshua Bengio (lead) et al. — 2026

### 08 — Language and Meaning
- **Strengths:** Wittgenstein, Austin, Grice and Searle make a good pragmatics core with explicit section reading guidance.
- **Problems:** ✔ The Andreas entry had only a surname and a vague description; it is now accurate.
- **Missing:**
  - Frege's sense/reference, Kripke's *Naming and Necessity*, and Putnam's "The Meaning of 'Meaning'" (Twin Earth). Reference and externalism are exactly what the LLM-grounding debate turns on. ✱ Recommended next (Frege's Crossref lookup was rate-limited; not added).
  - Distributional semantics (added).
- **Added:**
  - Distributional Structure — Zellig S. Harris — 1954
  - The Vector Grounding Problem — Coelho Mollo & Millière — 2023

### 09 — Free Will and Agency
- **Strengths:** Frankfurt, Dennett and Libet, plus the SEP map; Sapolsky is current.
- **Problems:**
  - ✔ The intro said Dennett's compatibilism is "the most philosophically satisfying" view; now "the most influential."
  - ✔ The Suggested Order called Sapolsky "the strongest challenge to compatibilism"; now "the most prominent recent scientific case against free will," paired with a counterweight.
  - ✔ The Libet description now points to the 2012 reinterpretation.
  - ✔ Dennett's dates (1942–2024) added.
  - ✱ Libet co-authors (Gleason, Wright, Pearl) are not listed.
- **Missing:**
  - P. F. Strawson, "Freedom and Resentment" (reactive attitudes) — canonical (✱ not verified).
  - Libertarianism (Kane) and hard incompatibilism (Pereboom).
  - Dennett & Caruso, *Just Deserts* (2021) — a debate-format pairing (✱ the publisher page failed to load).
- **Added:**
  - An Accumulator Model for Spontaneous Neural Activity… — Schurger, Sitt & Dehaene — 2012
  - Free Agents: How Evolution Gave Us Free Will — Kevin J. Mitchell — 2023

### 10 — Eastern Philosophy and Mind
- **Strengths:** A careful Buddhist sequence (Rahula, Siderits, Garfield/Nāgārjuna, Thompson, Flanagan).
- **Problems:**
  - ✔ The course title is "Buddhism and Modern Psychology", not "Buddhist…". It may no longer be offered on Coursera, and the entry now says so.
  - ✔ Siderits has a revised second edition (Hackett, 2021).
  - ✱ The section title promises "Eastern Philosophy," but every item is Buddhist.
  - ✱ "The Embodied Mind (revisited)" is a duplicate row.
- **Missing:** Hindu/Indian philosophy of mind (Nyāya arguments for the self, Advaita, Sāṃkhya dualism) and Chinese philosophy (Zhuangzi on other minds and dreaming). ✱ Recommended: Adamson & Ganeri, *Classical Indian Philosophy* (2020), and SEP "Zhuangzi" (the entry exists per the SEP contents page); neither was fully verified this session. Alternatively, rename the section "Buddhist Philosophy and Mind."
- **Added:** Mind in Indian Buddhist Philosophy (SEP) — Christian Coseru — 2009/rev. 2012

### 11 — Frontiers
- **Strengths:** The simulation argument and Reality+ pair well; Butlin et al. is the right anchor.
- **Problems:**
  - ✔ **"Could a Large Language Model be Conscious?" was attributed to "Schneider, Turner 2024" with no link.** It is by David Chalmers (2023, arXiv:2303.07103). Fixed and moved earlier in the order.
  - ✔ IIT 4.0's first author is Larissa Albantakis (16 authors, Tononi last). Fixed, with a contested note.
  - ✔ The Butlin description now states what the report actually finds.
  - ✱ Seth's *Being You* duplicates Section 02.
  - ✱ The Alignment Forum duplicates blogs and is not a "frontiers of mind" resource.
  - ✱ *Life 3.0* (2017) is the weakest item.
- **Missing:** AI welfare and moral patienthood (added); a precautionary framework for sentience under uncertainty (✱ Birch, *The Edge of Sentience*, OUP 2024, open access; not verified).
- **Added:** Taking AI Welfare Seriously — Long, Sebo, Butlin et al. (incl. Birch, Chalmers) — 2024

### books/
- Consistent with the sections; levels are sensible. All entries say "Paid", although some classics are free elsewhere (fine).
- **Added:**
  - Reasons and Persons — Parfit — 1984
  - forall x: Calgary — Magnus, Button, Thomas-Bolduc, Zach — 2023

### courses/
- ✔ #1 (🔑): the phantom Amy Kind playlist was replaced with the real Edinburgh course.
- ✔ #3 (🔑): the Dehaene Collège de France link (`/agenda/course/consciousness-and-brain`) fails to load. It now points to his 2026 lecture series "What is consciousness, and what are its brain mechanisms?", with a note that it is delivered in French and that his book is the English alternative. ✱ Consider removing 🔑 for an English-only learner.
- ✔ #10: title fixed and an availability note added.
- ✱ #7, Singer's Effective Altruism course, is paired with "AI risk" but is only tangential; check that it is still offered.
- **Added:** #11 Introduction to Critical Thinking — Wireless Philosophy (Section 00).

### blogs-and-references/
- ✔ AISF renamed to BlueDot Impact.
- ✱ Recommended (not verified this session):
  - Eric Schwitzgebel's *The Splintered Mind* blog (AI consciousness and moral status).
  - Peter Adamson's *History of Philosophy without any gaps* podcast (covers Indian, Chinese and Africana philosophy; would help Section 10).
- ✱ The "Philosophy of Science" journal listed here has no matching section; that is another argument for the proposal.

### PROGRESS.md
- ✔ It tracked only about the first 6–7 items of each section; about 30 existing items were missing. All are now added, along with every new item.
- ✔ The orphan line "Gödel's Incompleteness Theorems (overview)" now names the SEP entry.
- ✔ Fixed the Coeckelbergh title, "Ngo, Chan, & Shlegeris", and "Tononi et al. — IIT 4.0".
- ✔ Added the missing 🔑 on Putnam and SEP Functionalism.
- ✔ Added a Chalmers 2023 line (the misattributed paper had no line).
- ✱ "Books (supplementary)" duplicates section items, so a book gets checked twice. Drop it or mark items "(also in §NN)".

### README.md
- Accurate; the learning path matches the folders; the Core Reading List items are all present in their sections. No edits needed.
- ✱ Suggestions:
  - Add a "debates map" (physicalism, functionalism, dualism, illusionism, panpsychism, IIT, GWT) as a one-page orientation.
  - Add a note that Wolfram items are optional and speculative.
  - Mention the proposed philosophy-of-science section in the path.

## Corrections made
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| 00-foundations-of-philosophy/README.md:20 | Descartes *Meditations* → gutenberg.org/ebooks/59 | earlymoderntexts.com …/descartes1641.pdf (Bennett translation) | https://www.gutenberg.org/ebooks/59 (is *Discourse on the Method*); https://www.earlymoderntexts.com/authors/descartes |
| 01-philosophy-of-mind/README.md:23 | same Gutenberg #59 link | same Early Modern Texts PDF | as above |
| 00-foundations-of-philosophy/README.md:21 | SEP Logic & Ontology "Sets up the formal reasoning tools used throughout" | Accurate description (Hofweber; logic–ontology relationship); marked optional, points to forall x | https://plato.stanford.edu/entries/logic-ontology/ |
| 01-philosophy-of-mind/README.md:29 | 🎥 "Philosophy of Mind — Amy Kind" (Wi-Phi playlist) | 🎓 Edinburgh "Philosophy and the Sciences: Introduction to the Philosophy of Cognitive Sciences" | https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLtKNX4SfKpzX_bhh4LOEWEGy3pkLmFDmk&format=json (title "Introduction to Critical Thinking", Wireless Philosophy); https://www.coursera.org/learn/philosophy-cognitive-sciences |
| courses/README.md:7 | #1 🔑 "Philosophy of Mind — Amy Kind — Wi-Phi" | Edinburgh cognitive-sciences course | as above |
| 02-consciousness/README.md:23 | Chalmers 1995 → doi.org/10.1093/mind/104.414.200 | consc.net/papers/facing.html; venue *JCS* 2(3) noted | https://consc.net/papers/facing.html (Crossref has no record of the DOI) |
| 02-consciousness/README.md:29 | "SEP — The Hard Problem of Consciousness" → consciousness/#HarP | IEP "The Hard Problem of Consciousness" (Weisberg) | https://plato.stanford.edu/entries/consciousness/ (no such anchor); https://iep.utm.edu/hard-problem-of-conciousness/ |
| 02-consciousness/README.md:25–26 | IIT "a leading scientific theory"; Koch unqualified | IIT flagged as contested (2023 letter; 2025 test); Koch identified as an IIT proponent | https://www.nature.com/articles/d41586-023-02971-1 ; https://www.nature.com/articles/s41586-025-08888-1 |
| 03-computation-and-mind/README.md:30 | "Computationalism" (SEP) | "The Computational Theory of Mind" | https://plato.stanford.edu/entries/computational-mind/ |
| 03-computation-and-mind/README.md:34 | NKS PCE as "a radical extension of Church-Turing" | PCE described as an unproven conjecture; reviews' criticism, Cook's Rule 110 proof, and the Aaronson counterweight noted | https://www.wolframscience.com/nks/ ; https://arxiv.org/abs/quant-ph/0206089 |
| 03-computation-and-mind/README.md:36 | Ruliad: "consciousness and mind are patterns within this structure"; wolframphysics.org bulletin URL; 2020+ | "Speculative research program, not established physics"; canonical writings.stephenwolfram.com URL; 2021 | https://writings.stephenwolfram.com/2021/11/the-concept-of-the-ruliad/ |
| 04-intelligence-and-understanding/README.md:25 | "What Computers Can't Do: The Limits of Artificial Intelligence" (1972) | "…: A Critique of Artificial Reason" (1972) | https://www.lib.uci.edu/library/publications/philosophy/dreyfus.html |
| 04-intelligence-and-understanding/README.md:28 | SEP "Extended Mind" → entries/extended-mind/ | SEP "Externalism About the Mind" §§5–7 (#ExteMind) | https://plato.stanford.edu/entries/content-externalism/ (extended-mind URL fails while other SEP pages load) |
| 05-philosophy-of-ai/README.md:29 | Stochastic Parrots = "LLMs generate text without understanding" | Accurate summary (risk paper: costs, data, ascription of meaning) | https://doi.org/10.1145/3442188.3445922 (from the paper's abstract; not refetched) |
| 06-ethics-of-ai/README.md:24 | Coeckelbergh "The Ethics of Artificial Intelligence: An Introduction" | "AI Ethics (MIT Press Essential Knowledge series)" | https://coeckelbergh.net/ai-ethics/ |
| 06-ethics-of-ai/README.md:28 | Fairness & ML typed 📄 Paper | 📕 Book | https://fairmlbook.org/ |
| 07-existential-risk-and-alignment/README.md:27 | Ngo, Chan, Shlegeris — 2023 | Richard Ngo, Lawrence Chan, Sören Mindermann — 2022 | https://arxiv.org/abs/2209.00626 |
| 07-existential-risk-and-alignment/README.md:29 | "AI Safety Fundamentals — Richard Ngo et al." → aisafetyfundamentals.com | BlueDot Impact courses → bluedot.org | https://aisafetyfundamentals.com/ (302 → https://bluedot.org/?from_site=aisf) |
| blogs-and-references/README.md:33 | AI Safety Fundamentals | BlueDot Impact (formerly AISF) | as above |
| 08-language-and-meaning/README.md:29 | "Andreas"; "LMs can learn aspects of meaning" | "Jacob Andreas"; accurate summary (LMs infer and represent properties of the producing agent) | https://arxiv.org/abs/2212.01681 (from the abstract; not refetched) |
| 09-free-will-and-agency/README.md:5 | Compatibilism "the most philosophically satisfying reconciliation" | "the most influential reconciliation" | (neutrality edit) |
| 09-free-will-and-agency/README.md:21 | "Dennett argues…" | "Dennett (1942–2024) argues…" | (general knowledge; Dennett died April 2024; not refetched) |
| 09-free-will-and-agency/README.md:23 | Libet "interpretations vary" | Points to the Schurger et al. 2012 reinterpretation | https://doi.org/10.1073/pnas.1210467109 |
| 09-free-will-and-agency/README.md:25, :40 | Sapolsky "the strongest challenge to compatibilism" | "most prominent recent scientific case against free will", paired with Mitchell | https://press.princeton.edu/books/hardcover/9780691226231/free-agents |
| 10-eastern-philosophy-and-mind/README.md:23 | Siderits 2007 | 2007 (2nd ed. 2021); prefer the 2nd edition | https://www.philpapers.org/rec/SIDBAP-4 |
| 10-eastern-philosophy-and-mind/README.md:28; courses/README.md:16 | "Buddhist and Modern Psychology" | "Buddhism and Modern Psychology" plus an availability note | https://classcentral.com/course/science-of-meditation-1355 |
| courses/README.md:9 | Dehaene "Consciousness and the Brain" → /agenda/course/consciousness-and-brain (fails) | "What Is Consciousness, and What Are Its Brain Mechanisms?" (2026, in French) | https://www.college-de-france.fr/en/agenda/lecture/what-is-consciousness-and-what-are-its-brain-mechanisms |
| 11-frontiers/README.md:23 | Butlin "assessing whether current AI systems could be conscious" | States the method (indicator properties) and findings | https://arxiv.org/abs/2308.08708 (from the abstract; not refetched) |
| 11-frontiers/README.md:27 | "IIT 4.0 … — Tononi et al." | Full title; "Larissa Albantakis, …, Giulio Tononi"; contested note | https://arxiv.org/abs/2212.14787 |
| 11-frontiers/README.md:28 | "Could a Large Language Model be Conscious? — Schneider, Turner — 2024 — (no link)" | "— David Chalmers — 2023 — arXiv:2303.07103" | https://arxiv.org/abs/2303.07103 |
| PROGRESS.md:25,27,53,94,110,157,160 | missing 🔑; Gödel orphan; Coeckelbergh title; Shlegeris; Tononi IIT 4.0; no Chalmers line | fixed as described above; ~30 missing existing items added | internal consistency |

## Proposed new sections (not created)

### Philosophy of Science & Scientific Reasoning
- **Position:** immediately after Section 00. Either insert it as a new 01 and renumber, or, to avoid renumbering, add it as Section 12 with a README note to "take after 00."
- **Why:** Aaron studies physics, ML and biology, and this curriculum keeps asking scientific-method questions without the tools to answer them:
  - Is IIT pseudoscience? Who "won" the Cogitate test?
  - Is Wolfram's program science?
  - What would count as evidence that an LLM understands?
  - Are ML benchmarks measurements?

  Philosophy of science is the missing hub. It also connects to math/03 (Jaynes, Bayesian probability), math/10 (causal inference), physics (interpretation and realism), and bio (explanation in biology).
- **Outline:**
  1. Demarcation and falsification (Popper)
  2. Paradigms and revolutions (Kuhn)
  3. Research programmes (Lakatos), applied to IIT vs. GNWT, string theory, and Wolfram
  4. Induction and confirmation (Hume, Goodman's "grue", Bayesian epistemology)
  5. Explanation, causation, and realism vs. instrumentalism (and whether interpretability "explains" a model)
  6. Philosophy of statistics (frequentist vs. Bayesian, severe testing, the replication crisis)
  7. Philosophy of ML (inductive bias and Occam/Solomonoff priors; benchmarks as measurement)
- **Resources.** Status: ✔ = fetched and verified this session; ◻ = canonical, but verification was blocked by the exhausted fetch budget, so verify before adding.
  1. ✔ Aaronson, "Why Philosophers Should Care About Computational Complexity" (2011) — sections on Hume's induction, Goodman's grue, and logical omniscience. https://arxiv.org/abs/1108.1791 (also added to Section 03)
  2. ✔ SEP "Bayesian Epistemology" — https://plato.stanford.edu/entries/epistemology-bayesian/ (listed on the SEP contents page; entry page not fetched)
  3. ✔ Cogitate Consortium (2025) and Lenharo (2023) as worked demarcation case studies — https://www.nature.com/articles/s41586-025-08888-1 , https://www.nature.com/articles/d41586-023-02971-1 (in Section 02; cross-link them)
  4. ✔ Legg & Hutter (2007), on Solomonoff/Occam priors in a definition of intelligence — https://arxiv.org/abs/0712.3329 (in Section 04; cross-link)
  5. ◻ University of Edinburgh, "Philosophy and the Sciences: Introduction to the Philosophy of Physical Sciences" (Coursera). Its existence is confirmed by the verified companion course page; direct fetch was rate-limited. https://www.coursera.org/learn/philosophy-physical-sciences
  6. ◻ Karl Popper, *The Logic of Scientific Discovery* (1959), and SEP "Karl Popper" (https://plato.stanford.edu/entries/popper/; rate-limited).
  7. ◻ Thomas Kuhn, *The Structure of Scientific Revolutions* (1962; 50th-anniversary edition, U. Chicago Press, 2012).
  8. ◻ Imre Lakatos, "Falsification and the Methodology of Scientific Research Programmes" (1970, in Lakatos & Musgrave, eds., *Criticism and the Growth of Knowledge*).
  9. ◻ Peter Godfrey-Smith, *Theory and Reality: An Introduction to the Philosophy of Science* (2nd ed., 2021) — the best single textbook spine.
  10. ◻ Deborah Mayo, *Statistical Inference as Severe Testing* (2018) — for the ML and statistics angle.
  - Cross-reference: E.T. Jaynes, *Probability Theory: The Logic of Science* (already in math/03).

## Cut candidates
- **Duplicates across sections:**
  - Searle "Minds, Brains, and Programs" (03 and 05, both 🔑).
  - Bender & Koller (05 and 08, both 🔑).
  - Seth, *Being You* (02 and 11).
  - "The Embodied Mind (revisited)" (10 duplicates 04).
  - Dreyfus 1972 (04) vs. Dreyfus 1992 (05): keep one, preferably the 1992 MIT Press edition with its new introduction, and cross-reference.
- **11 — Alignment Forum:** duplicates blogs; a forum, not a frontiers reading.
- **11 — Tegmark, *Life 3.0* (2017):** dated popular overview, the weakest item in the section.
- **07 — 80,000 Hours AI-risk profile:** career-oriented, and duplicates blogs. Keep one copy.
- **07 — Yudkowsky, "Intelligence Explosion Microeconomics":** described as the "core theoretical framework", which overstates its current role. Keep it as historical and optional.
- **00 — SEP "Logic and Ontology":** too advanced for Foundations (now marked optional); a candidate to move to an advanced or metaphysics note.
- **courses #7 — Singer, *Effective Altruism*:** weak fit for "AI risk"; availability unverified.
- **courses #3 — Dehaene's Collège de France course:** French-language, so it should not be 🔑 for this learner.
- **03 — Wolfram NKS and ruliad:** kept as instructed and now honestly framed. If the section needs trimming, these are the first optional items to drop.

## Structural observations
- **Overlap: philosophy/07 ↔ ml/12 ↔ econ/11.**
  - ml/12 re-lists Bostrom and *Human Compatible* (rows 14–15) as "broader philosophical context".
  - econ/11 re-lists Amodei et al., "Concrete Problems in AI Safety" (also in philosophy/07), the AISF/BlueDot course, and the Alignment Forum.
  - Proposed division of labour, each with "see also" lines instead of duplicate rows:
    - philosophy/07: arguments and values (Bostrom, Russell, Carlsmith, Gabriel, skeptics, the International AI Safety Report).
    - ml/12: techniques (RLHF/CAI/DPO, interpretability, evals).
    - econ/11: incentives, game theory, Goodhart.
  - econ/11 still links aisafetyfundamentals.com, which now redirects to bluedot.org.
- **Overlap: philosophy/03 ↔ math/11 (and physics/11).** math/11 has a combined "NKS + Wolfram Physics Project" row framed neutrally ("connects to foundational questions about mathematical structure"). physics/11 marks the Wolfram Physics Project 🔑 while calling it "Controversial but thought-provoking." Recommendation: use the same honest "speculative research program, no confirmed predictions" framing everywhere, and reconsider 🔑 in physics/11. GEB also appears in math/books (fine).
- **Overlap: philosophy/05 and 08 ↔ ml/09 (LLMs).** The LLM-understanding papers (Bender & Koller, Mitchell & Krakauer, Millière & Buckner) should be cross-linked from ml/09.
- **Cross-curriculum flag for the ml reviewer.** ml/12 lists "Verbalizable Representations Form a Global Workspace in Language Models — Gurnee, Sofroniew, Lindsey et al. 2026". I could not verify it this session. If it is real, it is a natural cross-link to GWT (philosophy/02) and the Butlin indicators (philosophy/11). **Resolved:** the ml review verified it (transformer-circuits.pub, 6 July 2026), and philosophy/02 now has a see-also line pointing to it.
- **Section naming.** 04 "Intelligence and Understanding" was really "4E cognition"; it is now partly fixed with definitions of intelligence and predictive processing. 10 "Eastern Philosophy and Mind" is Buddhist only: either rename it or add Indian and Chinese material.
- **Schema inconsistencies.**
  - Type labels vary: "📝 Course" (07) vs. "🎓 Course" elsewhere; "📝 Blog" used for an Alignment Forum post. I introduced "📝 Essays", "📝 Article" and "📄 Report" where nothing existing fit.
  - Section READMEs define only 🔑 (03 adds 🔑🔑), consistent with the top-level legend.
  - Several sections have table items missing from their Suggested Order (Edinburgh course in 00, Mind's I in 03, Coeckelbergh in 06, 80,000 Hours in 07, SEP Wittgenstein in 08).
- **PROGRESS** was generated from an earlier, shorter version of the sections (it is now synced). Its "Books (supplementary)" block double-counts.
- **Agent skill.** philosophy/ has no `.agents/skills/update-curriculum/SKILL.md` (pcb, btc, ml and software do). If one is added, it should require fetching every citation (author, year, venue) before adding, since that is exactly where this curriculum's errors came from.
- **Missing standard parts.** No glossary or "positions map" for a domain that is mostly named positions (physicalism, functionalism, illusionism, panpsychism, compatibilism); a one-page map would help orientation.

## Top 5 priorities for Aaron in this curriculum
1. **Approve the Philosophy of Science section** (Popper, Kuhn, Lakatos, Bayesian epistemology, philosophy of statistics and ML). It is the tool for judging every "is this real science?" question in 02, 03 and 11, and it ties together the physics, ML and bio curricula.
2. **Read the now-balanced LLM-understanding cluster in order:**
   1. Bender & Koller
   2. Mitchell & Krakauer
   3. Shanahan
   4. Millière & Buckner (05)
   5. Harris → Coelho Mollo & Millière (08)
   6. Chalmers 2023 (11)
3. **Use Section 02's updated science path:**
   1. Seth & Bayne (map)
   2. Dehaene (GWT)
   3. Tononi/Koch (IIT)
   4. Lenharo (the "pseudoscience" fight)
   5. Cogitate 2025 (the head-to-head test)
   6. Then 11: Butlin et al., then *Taking AI Welfare Seriously*
4. **Treat Section 07 as a debate, not a catechism:** Carlsmith (the argument), then Gabriel (aligned to what?), then Narayanan & Kapoor (the skeptic), then the International AI Safety Report 2026 (the evidence). Use ml/12 for the technical side.
5. **Do the toolkit early and keep the speculative items optional:** forall x and the 1000-Word Philosophy ethics essays in Section 00. Read the Wolfram items in 03 as optional provocations, always next to Aaronson's review.

### Recommended next additions (strong, but not verified this session, so not added)
- Frege, "On Sense and Reference"; Putnam, "The Meaning of 'Meaning'" (08)
- P. F. Strawson, "Freedom and Resentment" (09)
- Dennett & Caruso, *Just Deserts* (09)
- Dennett, *The Intentional Stance* (01/05)
- Birch, *The Edge of Sentience* (11)
- Godfrey-Smith, *Other Minds* (04)
- Thompson, *Why I Am Not a Buddhist* (10)
- Adamson & Ganeri, *Classical Indian Philosophy* (10)
- *The Splintered Mind* blog; *History of Philosophy without any gaps* podcast (blogs)

## Follow-up pass (2026-10-13)
- **New sections created:** `philosophy/12-philosophy-of-science/` · "Philosophy of Science and Scientific Reasoning", take after Section 00 (README learning path updated) · 14 resources (🔑: Godfrey-Smith; SEP Science and Pseudo-Science) · 5 exercises, a mini-project ("Referee Report on a Contested Claim", `projects/philosophy/12-referee-report/`) and 8 Check Yourself questions · PROGRESS block added · "see Section 12" pointers added to 00, 02, 03, 04, 05 and 11 · cross-listed in books/ (#18) and courses/ (#12). Every "you should get X" value (optional-stopping false-positive rate ≈ 28% / ≈ 19%; BF₁₀ ≈ 1.7 at n = 10 and ≈ 0.67 at n = 100; BF₁₀ > 3 reached under H₀ in ≈ 11% of peeking runs vs. < 1% at fixed n; Ioannidis PPV 0.80 / 0.64 / 0.29, best-of-5 α ≈ 0.23 → PPV ≈ 0.28, inverted OSC PPV ≈ 0.36 / ≈ 0.56; Check Yourself Q6 = 0.50) was computed in Python (200,000-run Monte Carlo for the stopping figures). The four demarcation cases (IIT, Wolfram, an ML benchmark claim, a behavioral-econ finding) are framed as "apply the criteria and show where they disagree", with steelmen on both sides; no verdict is given.
- **Added:**
  - Theory and Reality: An Introduction to the Philosophy of Science (2nd ed.) — Peter Godfrey-Smith — 2021 — 12 (also books/ #18)
  - Karl Popper (SEP) — Stephen Thornton — 1997, rev. 2026 — 12
  - The Logic of Scientific Discovery — Karl Popper — 1959 (trans. of *Logik der Forschung*, 1935) — 12
  - The Structure of Scientific Revolutions, 50th Anniversary Edition (intro. Ian Hacking) — Thomas S. Kuhn — 1962 / 4th ed. 2012 — 12
  - Falsification and the Methodology of Scientific Research Programmes (in Lakatos & Musgrave, eds., *Criticism and the Growth of Knowledge*, pp. 91–196) — Imre Lakatos — 1970 — 12
  - Science and Pseudo-Science (SEP) — Sven Ove Hansson — 2008, rev. 2025 — 12
  - Bayesian Epistemology (SEP) — Hanti Lin — 2022 — 12
  - Philosophy of Statistics (SEP) — Jan-Willem Romeijn — 2014, rev. 2025 — 12
  - Statistical Inference as Severe Testing: How to Get Beyond the Statistics Wars — Deborah G. Mayo — 2018 — 12
  - Why Most Published Research Findings Are False — John P. A. Ioannidis — 2005 — 12
  - Estimating the reproducibility of psychological science — Open Science Collaboration — 2015 — 12
  - AI and the Everything in the Whole Wide World Benchmark — Raji, Bender, Paullada, Denton, Hanna — 2021 — 12
  - Do ImageNet Classifiers Generalize to ImageNet? — Recht, Roelofs, Schmidt, Shankar — 2019 — 12
  - Philosophy and the Sciences: Introduction to the Philosophy of Physical Sciences (Coursera) — University of Edinburgh (Massimi, Richmond, Lavelle et al.) — n.d. — 12 (also courses/ #12)
  - Sense and Reference ("Über Sinn und Bedeutung"; trans. Max Black, *Phil. Review* 57(3), 1948) — Gottlob Frege — 1892 — 08
  - The Meaning of "Meaning" — Hilary Putnam — 1975 — 08
  - Freedom and Resentment — P. F. Strawson — 1962 — 09
  - Just Deserts: Debating Free Will — Daniel C. Dennett, Gregg D. Caruso — 2021 — 09
  - The Intentional Stance — Daniel C. Dennett — 1987 — 05 (05 rather than 01: Practice 2 there tests exactly when intentional vocabulary earns its keep)
  - Other Minds: The Octopus, the Sea, and the Deep Origins of Consciousness — Peter Godfrey-Smith — 2016 — 04
  - The Edge of Sentience: Risk and Precaution in Humans, Other Animals, and AI — Jonathan Birch — 2024 — 11
  - Why I Am Not a Buddhist — Evan Thompson — 2020 — 10
  - Classical Indian Philosophy (A History of Philosophy without any gaps, Vol. 5) — Peter Adamson, Jonardon Ganeri — 2020 — 10
  - Discrimination in the Age of Algorithms — Jon Kleinberg, Jens Ludwig, Sendhil Mullainathan, Cass R. Sunstein — 2018 — 06 (the counterweight; see Flags)
  - The Splintered Mind (blog) — Eric Schwitzgebel — ongoing — blogs-and-references
  - History of Philosophy without any gaps (podcast) — Peter Adamson — ongoing — blogs-and-references (new "Podcasts" table)
  - Each addition to an existing section has a table row, a Suggested Order step and a PROGRESS line (blogs/ has no PROGRESS block); exercises adjusted minimally where they now use the item (05 Practice 2; 06 Practice 3 and mini-project; 08 Practice 5; 09 Practice 5 and mini-project; 10 Practice 1 and 3; 11 mini-project).
- **Removed (confirmed nonexistent):** none.
- **Flags resolved:**
  - `06-ethics-of-ai/README.md:67` (COMPAS check values) — recomputed from ProPublica's `compas-scores-two-years.csv` (Medium/High = high risk, outcome `two_year_recid`). On all 7,214 rows: FPR 44.85% vs. 23.45%, FNR 27.99% vs. 47.72% (Black vs. white), identical counts (990/805/532/1369 and 1139/349/461/505) to the truth tables in ProPublica's notebook, which report "Total: 7214". With the 6,172-row filters used for ProPublica's regression: FPR 42.34% vs. 22.01%, FNR 28.48% vs. 49.64%. So the independent check's premise (headline figures come from the filtered set) was wrong, and the original "full file" wording was right; the exercise now states both sets precisely. The FPR identity holds exactly on both. Evidence: https://github.com/propublica/compas-analysis (`Compas Analysis.ipynb`, "All/Black/White defendants" cells).
  - `06-ethics-of-ai/README.md` (one-directional reading list and steelman prompts) — added Kleinberg, Ludwig, Mullainathan & Sunstein (row :41, Suggested Order step 12), a balance note (:44), a both-directions clause in objective 4, and a two-sided steelman requirement in the mini-project item (5) and its success criterion (:71). Evidence: https://academic.oup.com/jla/article/doi/10.1093/jla/laz001/5476086 (*JLA* 10:113–174, CC BY-NC).
  - `04-intelligence-and-understanding/README.md:37,55` (SEP title and §§5–7) — the entry at `/entries/content-externalism/` is titled **"Externalism About the Mind"** (Rowlands, Lau, Deutsch; first published 10 Dec 2020); §5 "Extended Mind" (#ExteMind), §6 "The Scope of Extended Mind", §7 "Extended Mind and the 4E Mind". The repo was right; the checker's "Externalism About Mental Content" is the title of the older entry. No change. Evidence: https://plato.stanford.edu/entries/content-externalism/
  - `02-consciousness/README.md:72`, `11-frontiers/README.md:64` (PyPhi details) — PyPI lists stable 1.2.0 (2019) and 2.0.0rc1–rc3 (Sep–Oct 2026) with Requires-Python ≥ 3.13. `pip install --pre pyphi` installed 2.0.0rc3 on Python 3.13; its docstrings define `analyze(...).phi` = φ_s and `.big_phi` = Φ, and the "gotchas" reference is bundled. PyPhi 1.2.0 fails to import on Python 3.13 (`from collections import Iterable`). Running the exercise's three noisy 3-unit networks gave φ_s = 0.456 for the ring and φ_s = 0 for the self-loop "camera" and the feedforward chain (whose Φ is nonzero — the reason the exercise warns about `.phi` vs `.big_phi`). No change. Evidence: https://pypi.org/project/pyphi/
  - `07-existential-risk-and-alignment/README.md:43` (International AI Safety Report 2026) — published 3 February 2026, described on the site as "the second International AI Safety Report", led by Yoshua Bengio with over 100 authors; no arXiv/DOI listed. Row correct; no change. Evidence: https://internationalaisafetyreport.org/
  - `08-language-and-meaning/README.md:70` (Lewis signaling split) — simulated the 4-state Roth–Erev game (unit initial weights, +1 on success, 50,000 rounds): 1,000 seeds gave 69–72% of runs ≥ 0.95, 24–26% at partial-pooling ≈ 0.74–0.75, ~5% in between (two RNG seeds); 40 seeds gave 67.5% / 30%. The claim is right; the measured split is now stated. Evidence: local simulation (no web source).
  - `10-eastern-philosophy-and-mind/README.md:36` (*The Embodied Mind* has no §10 checkbox) — deliberate; the row now says it is tracked once under Section 04.
  - `09-free-will-and-agency/README.md:32` (✱ Libet co-authors) — now "Benjamin Libet, C. A. Gleason, E. W. Wright, D. K. Pearl"; PROGRESS line → "Libet et al.". Evidence: Europe PMC record PMID 6640273 (*Brain* 106(3):623–642), https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1093/brain/106.3.623&format=json
  - `courses/README.md:13` (✱ #7 Singer, "check that it is still offered") — still enrollable on Coursera (Princeton), but its six modules contain nothing on AI risk; the note no longer says "and AI risk". Evidence: https://www.coursera.org/learn/altruism
  - ✱ Schema: table items missing from Suggested Order — added steps for the Edinburgh course (00:52), *The Mind's I* (03:56), Coeckelbergh (06:52), 80,000 Hours (07:59) and SEP Wittgenstein (08:49).
  - ✱ `blogs-and-references/README.md:53` — the "Philosophy of Science" journal now points to Section 12.
- **Still unverified:**
  - Strawson, "Freedom and Resentment" — page range left out because the sources conflict: SEP "Peter Frederick Strawson" (Snowdon & Gomes) gives 1962, *Proceedings of the British Academy* 48: 1–25; PhilPapers gives PBA 48: 187–211 (1963). No link was added: the free full text on Ted Honderich's UCL site (https://www.homepages.ucl.ac.uk/~uctytho/dfwstrawson1.htm) states no licence, so linking it is Aaron's call.
  - Pages not readable this run: one Crossref query for the Lakatos chapter (HTTP 429; verified instead on the Cambridge Core chapter page), MIT Press for *The Intentional Stance* (robots-disallowed; verified via the CiNii library catalog, so no link), JSTOR (bot challenge) and PubMed (reCAPTCHA) — both replaced by Crossref and Europe PMC.
  - Not attempted (not in this backlog): SEP "Zhuangzi" for Section 10; the README "debates map"; the cut candidates and 🔑 questions above, which remain Aaron's decisions.
  - Outside this curriculum's edit scope: `STUDY-GUIDE.md:67` (Track E) still calls the philosophy-of-science section "proposed"; it should now link `philosophy/12-philosophy-of-science/`. The one-home table could add a row for "Philosophy of science, replication, benchmark validity → philosophy/12 (also econ/06, ml/12)".

## Link-audit fixes (2026-10-13)
- `blogs-and-references/README.md:53` (L3-082, moved): the *Philosophy of Science* journal moved from U. Chicago Press to Cambridge Core; the link now uses the auditor's fix_url, https://www.cambridge.org/core/journals/philosophy-of-science.
- `blogs-and-references/README.md:43` (L3-001, broken): the old 80,000 Hours priority-path page is gone. The row now cites the auditor's substitute, the "Loss of control" problem profile (Cody Fenwick, Zershaaneh Qureshi; first published July 2025, updated 13 Aug 2026). It has a "How you can help" section, so it still serves the row's career angle. Evidence: https://80000hours.org/problem-profiles/loss-of-control/
- `08-language-and-meaning/README.md:36` (L3-134, broken, no fix): SEP has no `/entries/philosophy-language/` entry. The row, Suggested Order step 1 and the PROGRESS line now cite SEP "Theories of Meaning" (Jeff Speaks; first published 26 Jan 2010, substantive revision 31 Jul 2024), SEP's broadest survey of semantic and metasemantic theories. SEP's search is robots-blocked and its contents page was truncated for the fetcher, so the entry was checked directly. Evidence: https://plato.stanford.edu/entries/meaning/
- `09-free-will-and-agency/README.md:32` (L2-052, mismatch): the four authors had already been fixed earlier today. The title is now complete, "… (Readiness-Potential): The Unconscious Initiation of a Freely Voluntary Act", and the co-authors' given names are written out. Evidence: https://api.crossref.org/works/10.1093/brain/106.3.623
- `10-eastern-philosophy-and-mind/README.md:39` and `courses/README.md:16` (L3-026, broken, no fix): no Coursera page was found for Wright's course. Coursera search is robots-blocked, Princeton's partner page shows only 3 of its courses, and `/learn/buddhism` returns an error. Both rows are kept with "⚠️ Link dead (checked Oct 2026)", and Suggested Order step 11 is marked "(optional; link dead)". Neither row was 🔑.
- Left unverifiable, no change: L1-141 Quanta philosophy tag page (the auditor suspects a 404, but the row is not 🔑, so it was not rechecked), L1-151 Springer *Minds and Machines* (429), L2-114 NotebookLM (robots), L2-147 ScienceDirect *Artificial Intelligence* (robots), L3-085 Nagel on JSTOR (bot challenge; the Crossref metadata matches).

## Tier lists (2026-10-13)
🔑 trimmed to ≤3 per section; each Suggested Order now opens with a "Core path" line. Reverse any call by re-adding 🔑 to the row and the Core path line.
| Section | 🔑 kept | 🔑 removed (why, ≤8 words) |
|---|---|---|
| 01 | Kim, *Philosophy of Mind*; Putnam, "The Nature of Mental States"; Nagel, "What Is It Like to Be a Bat?" | SEP "Functionalism" (encyclopedia companion to Putnam; Kim covers it) |
| 02 | Chalmers, *The Conscious Mind*; Dennett, *Consciousness Explained*; Seth & Bayne, "Theories of Consciousness" | Chalmers, "Facing Up" (shorter version of the README-listed book) |
| 05 | Turing, "Computing Machinery and Intelligence"; Bender & Koller, "Climbing towards NLU"; Mitchell & Krakauer, "The Debate Over Understanding" | Searle, "Minds, Brains, and Programs" (already 🔑 in prerequisite Section 03) |
- 🔑 resource rows across Sections 00–12: 30 → 27. The three demoted PROGRESS lines lost their 🔑.
- README "🔑 Core Reading List — Cross-Reference": no change. All 12 items are still 🔑 in the sections they point to.
- Index files (books/, courses/, blogs-and-references/): no change. None of the three demoted items is listed there.
- For Aaron, 02: "Facing Up" is free, short and Suggested Order step 1, so it would make the shorter core path. The book kept its 🔑 because README core item #2 is *The Conscious Mind*, and dropping it would leave Dennett without Chalmers in the README list. To swap, move the 🔑 to "Facing Up" in 02 and in PROGRESS, replace README item #2, and drop *The Conscious Mind*'s 🔑 in `books/README.md` (#4) and in PROGRESS "Books (supplementary)".
- books/README.md #9 Varela, Thompson & Rosch, *The Embodied Mind*: 🔑 added (core in 04)
- books/README.md #10 O'Neil, *Weapons of Math Destruction*: 🔑 added (core in 06)
- books/README.md #11 Rahula, *What the Buddha Taught*: 🔑 added (core in 10)
- books/README.md #12 Wittgenstein, *Philosophical Investigations*: 🔑 added (core in 08)
- books/README.md #13 Dennett, *Elbow Room*: 🔑 added (core in 09)
- books/README.md #18 Godfrey-Smith, *Theory and Reality* (2nd ed.): 🔑 added (core in 12)
- courses/README.md #1 Edinburgh, Philosophy and the Sciences: Introduction to the Philosophy of Cognitive Sciences: 🔑 removed (not core in any section; unmarked in 01)
- courses/README.md #2 Sandel, Justice: 🔑 removed (not core in any section; unmarked in 06)
- courses/README.md #8 Sapolsky, Human Behavioral Biology: 🔑 removed (not core in any section; unmarked in 09)
- philosophy/README.md legend: 🔑 row now reads "**Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line"
- philosophy/README.md legend: 🔑🔑 row now reads "**Foundational masterwork** — a core-path item that defines the field; read carefully"
- Second check (2026-10-13): `courses/README.md` #3 Dehaene, "What Is Consciousness, and What Are Its Brain Mechanisms?": 🔑 removed (index-only; Section 02 lists his book, unmarked).
- Second check (2026-10-13): 06: *Fairness and Machine Learning* (Barocas, Hardt & Narayanan) made 🔑 (third slot), because objective 2 and Practice 3 rest on it. PROGRESS and the Core path line were updated.
