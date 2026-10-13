# Decision Theory

## Why This Section Matters

Decision theory studies how individuals make choices under uncertainty — and how they systematically deviate from "rational" models. Expected utility theory, formalized by von Neumann and Morgenstern, provides the normative benchmark. Prospect theory, developed by Kahneman and Tversky, provides the descriptive reality: people are loss-averse, overweight small probabilities, and anchor to reference points. Understanding both the normative and descriptive frameworks is essential for mechanism design (which assumes rational agents), behavioral economics (which relaxes that assumption), and AI alignment (where reward specification mirrors utility specification). This section bridges the formal and the psychological. To judge the empirical claims and the replication debates for yourself, see [Section 13](../13-empirical-economics-and-causal-inference/README.md).

## Prerequisites

- [Section 00 — Economic Thinking](../00-economic-thinking/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- State the von Neumann–Morgenstern axioms and prove that the modal choices in Kahneman & Tversky's Allais-type problems violate independence for every utility function.
- Build and roll back a decision tree with real costs, compute certainty equivalents under CARA utility, and value information (EVPI, EVSI) with Bayes' rule.
- Implement cumulative prospect theory (value function with loss aversion, probability weighting) and use it to reproduce the reflection effect and the fourfold pattern.
- Correct base-rate neglect with Bayes' rule in a production-test setting, and explain anchoring, availability, and representativeness using the 1974 paper's own examples.
- Distinguish Knightian uncertainty from risk, explain how the Ellsberg urn violates Savage's sure-thing principle, and audit a famous behavioral result's replication record.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book | Thinking, Fast and Slow | Daniel Kahneman | 2011 | — | The definitive popular account of decades of research on judgment and decision-making: heuristics, biases, prospect theory, and two-systems thinking. ⚠️ Some studies it relies on have not survived replication, notably the social-priming results (Ch. 4) and ego depletion (Ch. 3); Kahneman later conceded he "placed too much faith in underpowered studies." The core heuristics-and-biases and prospect-theory findings have held up much better. |
| | 📝 Article | Reconstruction of a Train Wreck: How Priming Research Went off the Rails | Ulrich Schimmack, Moritz Heene & Kamini Kesavan | 2017 | [Link](https://replicationindex.com/2017/02/02/reconstruction-of-a-train-wreck-how-priming-research-went-of-the-rails/) | Statistical audit of the priming studies cited in Ch. 4 of *Thinking, Fast and Slow*, showing they were too underpowered to be credible; Kahneman's reply in the comments accepts the critique. Read right after Kahneman as a lesson in judging evidence. |
| 🔑 | 📄 Paper | Prospect Theory: An Analysis of Decision under Risk | Daniel Kahneman & Amos Tversky | 1979 | [Link](https://www.jstor.org/stable/1914185) | The most-cited paper in economics. Introduced loss aversion, reference dependence, and probability weighting. Foundational. |
| | 📄 Paper | Judgment under Uncertainty: Heuristics and Biases | Amos Tversky & Daniel Kahneman | 1974 | [Link](https://www.science.org/doi/10.1126/science.185.4157.1124) | The landmark paper cataloging anchoring, availability, and representativeness heuristics. |
| | 📖 Book | The Foundations of Statistics | Leonard Savage | 1954 | — | The foundational axiomatization of subjective expected utility theory. Dense but historically essential. |
| | 📖 Book | Risk, Uncertainty and Profit | Frank Knight | 1921 | [Link](https://oll.libertyfund.org/titles/knight-risk-uncertainty-and-profit) | Introduced the crucial distinction between measurable risk and unmeasurable uncertainty ("Knightian uncertainty"). |
| | 📖 Book | Theory of Games and Economic Behavior (Ch. 1 & Appendix) | John von Neumann & Oskar Morgenstern | 1944 | — | The book that founded game theory. Ch. 1 argues for numerical utility; the axiomatic derivation of expected utility was added as an appendix in the 1947 second edition. Read that appendix for the normative starting point. |
| 🔑 | 📝 Article | Decision Theory (Stanford Encyclopedia of Philosophy) | Katie Steele & H. Orri Stefánsson | 2015 (rev. 2025) | [Link](https://plato.stanford.edu/entries/decision-theory/) | Free, authoritative overview of normative decision theory: preferences and utility, the von Neumann–Morgenstern and Savage representation theorems, Jeffrey's theory, and challenges such as Allais-type risk attitudes and unawareness. The normative counterweight to this section's mostly behavioral readings. |
| | 📖 Book | Rational Choice in an Uncertain World | Reid Hastie & Robyn Dawes | 2009 | — | Clear textbook on the psychology of judgment and decision-making. Good companion to Kahneman. |
| | 📖 Book | Predictably Irrational | Dan Ariely | 2008 | — | Accessible popular introduction to behavioral anomalies in decision-making. ⚠️ Read critically: a 2012 *PNAS* honesty study Ariely co-authored was retracted in 2021 after evidence its field data were fabricated, and the "Ten Commandments" honesty result described in the book failed a 25-lab preregistered replication (2018). |

---

## Suggested Order

**Core path (🔑):** Kahneman, *Thinking, Fast and Slow* → Kahneman & Tversky, "Prospect Theory" → Stanford Encyclopedia, "Decision Theory"

1. **Kahneman — Thinking, Fast and Slow** — Start here for the most accessible and comprehensive overview of the field.
2. **Schimmack et al. — "Reconstruction of a Train Wreck"** — Read immediately after Kahneman to calibrate which findings to trust.
3. **Tversky & Kahneman — "Heuristics and Biases" (1974)** — Read the original paper on cognitive biases.
4. **Kahneman & Tversky — "Prospect Theory" (1979)** — Read the foundational paper on how people actually make decisions under risk.
5. **Stanford Encyclopedia — Decision Theory** — Get the normative framework: utility, representation theorems, and their critics.
6. **von Neumann & Morgenstern — Theory of Games (Ch. 1 & Appendix)** — Understand the normative expected utility benchmark from the source.
7. **Knight — Risk, Uncertainty and Profit** — Read for the important risk vs. uncertainty distinction.
8. **Hastie & Dawes — Rational Choice in an Uncertain World** — Read for a more formal textbook treatment.
9. **Savage — The Foundations of Statistics** — Reference for the axiomatic foundations of subjective expected utility.
10. **Ariely — Predictably Irrational** — Optional light reading; keep the caveats above in mind.

---

## 🛠️ Practice

1. **Allais by algebra** — Take Problems 1 and 2 of Kahneman & Tversky (1979). (a) Prove in two lines that preferring B in Problem 1 and C in Problem 2 contradicts expected utility for any u(·). (b) Name the vNM axiom violated and identify the "common consequence" it says should cancel. (c) Evaluate all four prospects under cumulative prospect theory with the Tversky–Kahneman (1992) parameters — v(x) = x^0.88 for gains, w(p) = p^γ/(p^γ + (1−p)^γ)^(1/γ) with γ = 0.61, rank-dependent decision weights — and confirm it predicts both modal choices. (d) Read Savage's account of how he reconsidered his own Allais choices; in 150 words, say whether you'd "correct" yourself too. **Check:** EU reduces both choices to the sign of 0.34·u(2400) − 0.33·u(2500) − 0.01·u(0); CPT values ≈ 943 vs. 871 (B vs. A) and ≈ 327 vs. 320 (C vs. D). *(~2 h · Kahneman & Tversky, "Prospect Theory" (1979); von Neumann & Morgenstern, the utility axioms in the appendix to the 1947 2nd edition; Savage, The Foundations of Statistics)*
2. **Base rates on the production line** — Warm up with the cab problem as told in *Thinking, Fast and Slow* (15% of cabs Blue, witness 80% reliable). Then: your end-of-line functional test has 98% sensitivity and 95% specificity, and 1% of boards are truly defective. (a) What fraction of failed boards are actually bad? (b) After two independent fails? (c) Why is "independent" doubtful when both runs use the same fixture, and how would you estimate the correlation from your retest logs? (d) Costs: a retest $3, scrapping a good board $70, shipping a bad one $400 in returns and reputation. Compare scrap-on-first-fail with retest-once (scrap only on a second fail) per failed board, then redo it assuming half of good boards that fail once fail again. **Check:** cab ≈ 41%; (a) ≈ 16.5%; (b) ≈ 79.5%; (d) ≈ $58 vs. ≈ $7 per failed board with independent errors, but ≈ $34 for retest-once under the correlated assumption. *(~2 h · Tversky & Kahneman, "Judgment under Uncertainty" (1974), on representativeness and base rates; Kahneman, Thinking, Fast and Slow, chapters on base rates; Hastie & Dawes on Bayesian reasoning)*
3. **Prospect-theory calculator** — Implement CPT in ~40 lines: v(x) = x^0.88 for gains and −2.25·(−x)^0.88 for losses; weighting functions with γ = 0.61 (gains) and δ = 0.69 (losses). (a) Compute certainty equivalents for the four prospects in Kahneman's fourfold-pattern table (95% or 5% chance to win or lose $10,000) and label each cell risk-averse or risk-seeking. (b) Reproduce the 1979 paper's reflection effect: a sure $3,000 vs. 80% of $4,000, and the mirrored losses. (c) Business case: a customer buying a $2,000 instrument faces a 3% chance of a $600 out-of-warranty repair. Compute the most they'd pay for an extended warranty, first treating the premium as a loss, then exempting it from loss aversion; compare with the $18 expected loss. **Check:** CEs ≈ $7,700, $1,000, −$8,300, −$830 (EVs $9,500, $500, −$9,500, −$500); CPT picks the sure gain but the risky loss; warranty willingness to pay ≈ $34 (premium as loss) vs. ≈ $87 (exempt) — explain why the coding of the premium matters so much. *(~3 h · Kahneman & Tversky 1979; Kahneman, Thinking, Fast and Slow, chapters on prospect theory and the fourfold pattern)*
4. **Decision tree: buffer-buy during a shortage** — You need 1,500 MCUs over 18 months. Option A: commit now to a distributor buffer at $5.50/unit plus $600 holding cost ($8,850). Option B: buy as needed — $3.60/unit if supply normalizes, $12/unit from brokers if the shortage persists (P = 0.15). (a) Roll back the tree under expected cost. (b) With CARA utility and risk tolerance ρ, find the ρ below which A wins. (c) EVPI. (d) A market report calls the state with 80% accuracy: compute posteriors, the best action after each signal, and EVSI. (e) The shortage probability at which a risk-neutral buyer switches. (f) In 100 words, argue whether that 0.15 is Knightian "uncertainty" or "risk", and how much that should change your trust in (a)–(e). **Check:** E[B] = $7,290 < $8,850; A wins for ρ below ≈ $8,740; EVPI = $1,372.50; EVSI ≈ $512 (the posterior after a "shortage" call is ≈ 41% — the cab problem again); break-even P ≈ 0.27. *(~3 h · von Neumann & Morgenstern on expected utility; Hastie & Dawes, Rational Choice in an Uncertain World; Knight, Risk, Uncertainty and Profit)*
5. **Replication audit: the hot hand and two more** — *Thinking, Fast and Slow* presents the basketball "hot hand" as a cognitive illusion (Gilovich, Vallone & Tversky, 1985). (a) Simulate 100-shot sequences of a 50% shooter; per sequence, compute the proportion of hits immediately after three straight hits; average across sequences. (b) Using your simulation, explain the selection bias behind that shortfall (identified by Miller & Sanjurjo, 2018, *Econometrica*) and what it does to the original test. (c) Write two more one-page "replication cards" — claim, original evidence (N, effect size), replication attempts, current status, your verdict — for the honesty experiments Ariely presents (e.g., the Ten Commandments study, plus the related "sign at the top" field study) and for the behavioral-priming chapter of *Thinking, Fast and Slow* (see Kahneman's own 2017 response to the "train wreck" critique). **Check:** the average in (a) is ≈ 0.46, not 0.50 — so a real shooter who hits 50% after streaks is evidence *for* a hot hand. *(~4 h · Kahneman, Thinking, Fast and Slow; Schimmack, Heene & Kesavan, "Reconstruction of a Train Wreck"; Ariely, Predictably Irrational, with the caveats in its entry above; Tversky & Kahneman 1974 on misconceptions of chance)*

**🏗️ Mini-project — Decision-analysis toolkit and a real decision memo:** Build a small Python package: decision, chance, and terminal nodes; roll-back under expected value or any utility function; EVPI and EVSI via Bayes' rule; one-way sensitivity with a tornado chart; break-even probabilities. Validate it by reproducing every check number in Practice 4. Then apply it to a real decision you face — e.g., whether to pay ~$3k for an EMC pre-compliance scan before a ~$12k formal test, given your estimates of first-pass failure probability, redesign cost, and schedule-slip cost — treating the pre-scan as imperfect information. Deliverable: `projects/econ/03-decision-tree/` + a one-page memo with the tree, EV and certainty equivalents at two risk tolerances, the value of the pre-scan, a tornado chart, and a "Knightian" paragraph on which inputs are guesses and how far each can move before the decision flips. **Success:** the package reproduces Practice 4 exactly; a colleague can change any input in one place and re-run; the memo's recommendation either survives the tornado test or says precisely where it fails. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State the four vNM axioms. Which does the Allais paradox violate, and which of Savage's postulates does the Ellsberg urn violate?
2. What does a loss-aversion coefficient of about 2 mean in words, and what everyday behavior does it predict?
3. Describe the fourfold pattern and tie each cell to a real behavior (lottery tickets, insurance, settling lawsuits, desperate gambles).
4. In Tversky & Kahneman's anchoring demonstration, what was the anchor and what were subjects estimating? Why is a random anchor so damning?
5. A defect affects 1 in 200 boards; your test catches 99% of defects with a 2% false-alarm rate. Without a calculator, roughly what fraction of flagged boards are actually defective?
6. What does EVPI measure, and why is it an upper bound on what any information source is worth to you?
7. Misconception probe: "Knightian uncertainty just means you should use a uniform prior." Why does the Ellsberg urn show that ambiguity is not the same as a 50/50 prior?
8. Explain to a smart friend in three sentences why the same person buys both lottery tickets and insurance.
