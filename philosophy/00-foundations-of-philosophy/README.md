# Foundations of Philosophy

## Why This Section Matters

Before engaging with the philosophy of mind and AI, you need a toolkit: how to construct valid arguments, evaluate evidence, and distinguish knowledge from belief. Epistemology (the study of knowledge) and logic provide the bedrock for every subsequent section. Without these foundations, philosophical arguments about consciousness or AI ethics will feel like opinions rather than structured reasoning. This section equips you with the intellectual framework that makes rigorous philosophical inquiry possible.

## Prerequisites

None; this is the starting section.

## 🎯 Learning Objectives

After this section you can:
- Rewrite any argument in standard form (numbered premises → conclusion), test its validity with a truth table or a first-order regimentation, and name the premise a critic should attack first.
- Distinguish knowledge from true belief using Plato's *Meno*, state the justified-true-belief (JTB) analysis, and construct an original Gettier case that defeats it.
- Reconstruct Descartes' dream and evil-demon arguments and the closure-based skeptical argument, and evaluate one published response.
- Explain Hume's problem of induction and show, with a working model, where Bayesian updating builds in an assumption of uniformity — and argue whether that relocates the problem or solves it.
- Apply consequentialism, Kantian deontology, virtue ethics and contract theory to one concrete case and pinpoint the premise where their verdicts split.

## Marking Convention

| Symbol | Meaning |
|--------|----------|
| 🔑 | Must-read — essential for understanding this topic |

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📕 Book | Think: A Compelling Introduction to Philosophy | Simon Blackburn | 1999 | — | The best single-volume introduction to philosophy. Covers knowledge, mind, free will, ethics, and God with clarity and wit. Start here. |
| 🔑 | 📝 Encyclopedia | Epistemology | SEP | — | [SEP](https://plato.stanford.edu/entries/epistemology/) | Comprehensive entry on the nature, sources, and limits of knowledge. The gold-standard reference. |
| | 📕 Book | What Does It All Mean? A Very Short Introduction to Philosophy | Thomas Nagel | 1987 | — | Ultra-concise introduction — 101 pages covering the big questions. Good warmup before Blackburn. |
| | 📕 Book | Meditations on First Philosophy | René Descartes | 1641 | [Free](https://www.earlymoderntexts.com/assets/pdfs/descartes1641.pdf) | The foundational text of modern philosophy. Introduces radical doubt and the cogito ("I think, therefore I am"). The free link is Jonathan Bennett's lightly modernized translation (Early Modern Texts). |
| | 📝 Encyclopedia | Logic and Ontology | SEP | — | [SEP](https://plato.stanford.edu/entries/logic-ontology/) | Thomas Hofweber's entry on how logic relates to ontology (the study of what exists): ontological commitment, whether logic is neutral about what there is, Carnap's rejection of ontology. An advanced metaphysics entry, not a reasoning primer — *forall x* below is the actual toolkit. Optional. |
| | 🎥 Video | Introduction to Critical Thinking | Wireless Philosophy (Wi-Phi) | — | [YouTube](https://www.youtube.com/playlist?list=PLtKNX4SfKpzX_bhh4LOEWEGy3pkLmFDmk) | 35 short animated lessons from Wi-Phi on the basics of good reasoning — what arguments are and how to evaluate them. The fastest on-ramp before formal logic. |
| | 📕 Book | forall x: Calgary — A Free and Open Introduction to Formal Logic | P. D. Magnus, Tim Button, Aaron Thomas-Bolduc, Richard Zach | 2023 | [Free](https://forallx.openlogicproject.org/) | Free, CC-licensed textbook on truth-functional and first-order logic: validity, truth tables, natural deduction, quantifiers. The formal reasoning toolkit this section promises; work through truth-functional logic and the basics of first-order logic, in parallel with later sections if needed. |
| | 📝 Essays | 1000-Word Philosophy — Ethics essays: "Consequentialism and Utilitarianism", "Kantian Deontology", "Virtue Ethics", "Social Contract Theory" | Shane Gronholz; Andrew Chapman; David Merry; David Antonini | — | [Link](https://1000wordphilosophy.com/ethics/) | Short, free introductions to the main normative theories. The curriculum otherwise has no ethics primer before Section 06 — these give you the vocabulary that AI-ethics and alignment debates assume. |
| | 📄 Dialogue | Meno | Plato | ~380 BC | [Free](https://www.gutenberg.org/ebooks/1643) | Classic dialogue on knowledge vs. true belief. Introduces the paradox of inquiry. |
| | 📕 Book | An Enquiry Concerning Human Understanding | David Hume | 1748 | [Free](https://www.gutenberg.org/ebooks/9662) | Empiricism, causation, the problem of induction. Read at least Sections 2-5 and 7 for foundations. |
| | 🎓 Course | Introduction to Philosophy | University of Edinburgh | — | [Coursera](https://www.coursera.org/learn/philosophy) | Broad intro covering epistemology, metaphysics, philosophy of mind, and ethics. Good video companion. |

> **Next:** [Section 12 — Philosophy of Science and Scientific Reasoning](../12-philosophy-of-science/README.md) is meant to be taken right after this section. It picks up Hume's problem of induction and the Hume-vs-Bayes notebook (Practice 5) and asks what makes a claim scientific.

## Suggested Order

**Core path (🔑):** Blackburn, *Think* → SEP "Epistemology"

1. **Nagel — What Does It All Mean?** — Quick warmup to the major philosophical questions
2. **Blackburn — Think** — Comprehensive grounding in epistemology, logic, mind, and ethics
3. **Wi-Phi — Introduction to Critical Thinking** — Learn to identify and evaluate arguments
4. **SEP — Epistemology** — Deep dive into the theory of knowledge
5. **Plato — Meno** — See how the earliest Western philosophers wrestled with what knowledge is
6. **Descartes — Meditations** — Understand radical skepticism and the foundations of modern philosophy
7. **Hume — Enquiry (selections)** — Grasp empiricism and the problem of induction
8. **forall x: Calgary** — Formalize your reasoning tools: truth-functional and first-order logic (can run in parallel with later sections)
9. **1000-Word Philosophy — Ethics essays** — Consequentialism, Kantian deontology, virtue ethics, social contract: the vocabulary for Sections 06–07
10. **SEP — Logic and Ontology** — Optional, advanced: how logic relates to what exists
11. **University of Edinburgh — Introduction to Philosophy (Coursera)** — Optional video companion to Blackburn

---

## 🛠️ Practice

1. **Standard form + a validity checker** — Work the truth-functional chapters of *forall x: Calgary* alongside the Wi-Phi critical-thinking videos. Then write a ~60-line Python checker: premises and conclusion as propositional formulas over named atoms, brute-force every valuation with `itertools.product`, print VALID or the first counterexample row. Test it on modus ponens, modus tollens, disjunctive syllogism and hypothetical syllogism (valid) and on affirming the consequent, denying the antecedent and affirming a disjunct (invalid). Finally take three arguments from Blackburn's *Think* (one each from the chapters on knowledge, mind and free will), put each in standard form, check its propositional skeleton, and flag the premise you would attack first with a one-sentence reason. Done when the checker flags exactly the three invalid forms and every Blackburn argument is valid as written or you have supplied the missing premise that makes it so. *(~4 h · forall x: Calgary; Wi-Phi Critical Thinking; Blackburn, Think)*
2. **Meno, Gettier, and a stuck meter** — (a) Put Meno's paradox (80d–e) in standard form and say which premise Socrates' doctrine of recollection denies, and which one a modern epistemologist would deny instead. (b) From the road-to-Larissa and statues-of-Daedalus passages (97a–98a), state in two sentences why Socrates thinks knowledge is worth more than true belief. (c) After the SEP *Epistemology* section on knowing facts (where Gettier cases appear), write two original Gettier cases from the lab — e.g., a multimeter whose display froze hours ago and happens to show the correct voltage; a production test that passes only because a fixture short masks the real fault. Show each is justified, true and believed, then test whether a "no false lemmas" condition or a reliability condition rules it out. One page; check that each case would still be a Gettier case if you changed nothing but the luck. *(~2.5 h · Plato, Meno; SEP Epistemology)*
3. **Descartes' doubt, formalized** — Reconstruct the dream argument and the evil-demon argument from Meditation I as two separate standard-form arguments, then the closure-based skeptical argument from the SEP entry's section on the limits of cognitive success (if I know I have hands, I know I am not a deceived brain in a vat; I don't know I'm not; so I don't know I have hands). Mark the load-bearing premise in each, and evaluate one of the responses to the closure argument that the SEP entry surveys in 300 words. Finish with a short list: what the cogito in Meditation II establishes, and what it does not (a persisting self? a body? other minds?). Check: each argument is valid, and deleting any one premise breaks it. *(~3 h · Descartes, Meditations I–II; SEP Epistemology)*
4. **Four theories, one recall decision** — Read the four 1000-Word Philosophy ethics essays. Case: a small instrument maker finds a firmware bug that makes about 0.5% of shipped units drift out of calibration spec within a year; a silent fix in the next routine update is cheap, a customer notice is costly and embarrassing. Write one standard-form argument for what to do from each theory (consequentialist, Kantian, virtue, social-contract). Identify the premise where they diverge, and list the facts (probabilities, who bears the risk, what was promised in the spec sheet) that would flip each verdict. *(~2 h · 1000-Word Philosophy ethics essays)*
5. **Hume vs. Bayes, in a notebook** — After Hume's *Enquiry* §§IV–V, implement Laplace's rule of succession, P(next success) = (s+1)/(n+2), and a general Beta–Binomial updater. Simulate 1,000 "sunrises", then a process whose regularity silently breaks at trial 500, and plot how quickly different priors notice. Then write 400 words: where in your code does the assumption that the future resembles the past live (hint: the i.i.d./exchangeable likelihood, not the prior), and does Bayesian updating answer Hume or presuppose an answer? Done when you can point to the exact line of code that encodes Hume's uniformity principle and explain why no choice of prior removes it. *(~3 h · Hume, Enquiry §§IV–V; Blackburn, Think, chapter on reasoning)*

**🏗️ Mini-project — The Calibrated Skeptic:** Write a 3,000–4,000-word dialogue in the style of the *Meno* between an Engineer and a Skeptic about whether a freshly calibrated precision instrument gives *knowledge* of a measured value. It must (i) put the knowledge/true-belief distinction to work — what "ties down" a reading?; (ii) contain one Gettier case and one Cartesian global doubt; (iii) stage Hume's problem of induction against the instrument's calibration history; and (iv) end in honest aporia: a numbered list of what was settled, what was not, and the premise each character still rejects. Append the four key arguments in standard form. Deliverable: `projects/philosophy/00-calibrated-skeptic/dialogue.md`. Success: a reader sympathetic to the Skeptic finds the Skeptic's lines to be the strongest version of their view, and every argumentative move in the dialogue can be traced to one of the appended standard-form arguments. *(~8 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What is the difference between a valid argument and a sound one? Give a valid argument that is unsound.
2. State Meno's paradox and Socrates' answer to it.
3. Why does a Gettier case show that justified true belief is not *sufficient* for knowledge, and why does it leave open that JTB is *necessary*?
4. State Hume's argument that inferences from experience cannot be founded on reasoning, and his "sceptical solution" in Section V.
5. Misconception probe: "Descartes doubted everything, so the cogito proves that a thinking substance — a self — exists." What does the cogito establish beyond doubt, and which step in this summary — one Descartes defends but critics reject — is contested?
6. An instrument has passed 10,000 self-tests. Is it rational to expect it to pass the next one? Answer as Hume, then as a Bayesian, then say what each answer assumes.
7. Name the four normative theories in the ethics essays and the first question each asks about an action.
8. Explain to a smart friend in 3 sentences why philosophers insist on writing arguments in standard form.
