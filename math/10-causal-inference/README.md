# Causal Inference

## Why This Section Matters

Correlation is not causation — but mathematics *can* formalize causation. Causal inference provides the mathematical framework for answering "what if" and "why" questions from data. Pearl's do-calculus lets you reason about interventions; counterfactual reasoning lets you analyze what would have happened under different conditions. In medicine, causal inference determines whether a treatment works; in policy, it evaluates interventions; in ML, causal reasoning is increasingly recognized as essential for building systems that generalize beyond their training distribution. This is where statistics meets philosophy meets rigorous mathematics.

---

## Prerequisites

- Section 03 (Probability and Statistics) — conditional probability, Bayesian reasoning
- Section 06 (Graph Theory) — directed graphs, DAGs

---

## 🎯 Learning Objectives

After this section you can:
- Distinguish association, intervention, and counterfactual questions (Pearl's ladder), and write each in do-notation or potential-outcomes notation.
- Read the conditional independencies implied by a DAG with d-separation, and choose valid adjustment sets with the backdoor and front-door criteria.
- Estimate average causal effects from observational data by standardization and inverse-probability weighting, with bootstrap uncertainty, positivity diagnostics, and covariate-balance checks.
- Recognize, explain, and simulate the classic bias mechanisms: confounding, collider (selection) bias, and adjusting for a mediator.
- Evaluate causal-discovery methods (e.g., additive-noise models) and causal-ML claims by the identifiability assumptions they rest on.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | The Book of Why: The New Science of Cause and Effect | Judea Pearl, Dana Mackenzie | 2018 | — | The accessible introduction to causal reasoning. Pearl explains causal graphs, interventions, and counterfactuals through vivid examples. Read this first to understand the conceptual revolution. |
| | Book | Causality: Models, Reasoning, and Inference | Judea Pearl | 2009 | — | The technical bible of causal inference. Covers structural causal models (SCMs), do-calculus, counterfactuals, and identification theory rigorously. The definitive reference. |
| | Book | Causal Inference in Statistics: A Primer | Judea Pearl, Madelyn Glymour, Nicholas Jewell | 2016 | — | A shorter, more accessible technical introduction than *Causality*. Good bridge between *The Book of Why* and the full technical treatment. |
| | Book (Free) | Causal Inference: What If | Miguel Hernán, James Robins | 2020 | [Link](https://miguelhernan.org/whatifbook) | Free textbook from the epidemiology perspective. Covers potential outcomes, inverse probability weighting, and g-methods. Complements Pearl's graphical approach. The authors' book page has the latest free PDF (revised in place, so re-download it), the NHEFS data with its codebook, and code in Python, R, SAS, Stata and Julia. |
| | Course (Free) | Introduction to Causal Inference | Brady Neal | — | [Link](https://www.bradyneal.com/causal-inference-course) | Free online course with video lectures, slides, and exercises. Excellent modern introduction covering both potential outcomes and graphical approaches. |
| | Paper | Causal Reasoning from Meta-Reinforcement Learning | Dasgupta et al. | 2019 | [Link](https://arxiv.org/abs/1901.08162) | Connects causal reasoning to reinforcement learning and meta-learning. Bridge from causal theory to ML applications. |
| | Paper | Towards Causal Representation Learning | Schölkopf et al. | 2021 | [Link](https://arxiv.org/abs/2102.11107) | Survey connecting causal inference to representation learning in ML. Arguments for why causal reasoning is essential for robust AI. |
| | Book (Free) | Elements of Causal Inference: Foundations and Learning Algorithms | Jonas Peters, Dominik Janzing, Bernhard Schölkopf | 2017 | [Link](https://library.oapen.org/bitstream/20.500.12657/26040/1/11283.pdf) | Machine-learning-oriented treatment of causal inference. Covers causal discovery from data and connections to transfer learning. Open access: the link is the free PDF (CC BY-NC-ND 4.0) in the [OAPEN library](https://library.oapen.org/handle/20.500.12657/26040); the print edition is from [MIT Press](https://mitpress.mit.edu/9780262037310/elements-of-causal-inference/). |

---

## Suggested Order

**Core path (🔑):** Pearl & Mackenzie, *The Book of Why*

1. **The Book of Why (Pearl)** — Start here for the conceptual revolution. Accessible and compelling.
2. **Brady Neal — Causal Inference course** — Free lectures for building technical understanding.
3. **Pearl, Glymour & Jewell — Causal Inference in Statistics** — Technical but accessible primer.
4. **Hernán & Robins — Causal Inference: What If** — Epidemiological perspective and potential outcomes framework.
5. **Pearl — Causality** — The full technical treatment. Reference as needed.
6. **Peters et al. — Elements of Causal Inference** — ML-oriented perspective.
7. **Schölkopf et al.** — For the connection to modern representation learning.

---

## 🛠️ Practice

1. **Simpson's paradox, two ways** — Take the Primer's drug/recovery table stratified by gender. Compute P(recovery | drug) and P(recovery | no drug) overall and within each stratum, then P(recovery | do(drug)) and P(recovery | do(no drug)) with the adjustment formula. Now reinterpret the third variable as post-treatment blood pressure (the Primer's second version of the example): draw both DAGs and show that the same numbers demand opposite analyses. Write one paragraph on why the data alone cannot tell you which analysis is right. *(~2 h · Pearl, Glymour & Jewell, Causal Inference in Statistics: A Primer, Ch. 1 and 3; The Book of Why's chapter on paradoxes)*
2. **d-separation and collider bias, simulated** — For a chain, a fork, a collider, the M-graph, and one larger DAG from the Primer's d-separation section, list every implied (conditional) independence by hand. Check your lists with `networkx.is_d_separator`, then simulate each DAG as a linear-Gaussian SCM (10⁵ samples) and confirm the corresponding partial correlations are ≈ 0. Finish with the engineering version of Berkson's paradox: two independent degradation variables (say, solder-void fraction and component drift) whose sum must stay under a limit for a board to pass final test — show they look negatively correlated among the boards that pass. *(~3 h · Primer Ch. 2; Brady Neal's course on the flow of association and causation in graphs; The Book of Why)*
3. **IP weighting and standardization on real data** — Download the NHEFS data from the *What If* book site and estimate the average effect of quitting smoking on 10-year weight gain: (a) the unadjusted difference (≈ 2.5 kg); (b) IP weighting with a logistic propensity model — reproduce the book's ≈ 3.4 kg (95% CI ≈ 2.4–4.5) — and again with stabilized weights; (c) standardization (the parametric g-formula); (d) bootstrap confidence intervals for each. Plot the propensity-score distributions by treatment group, comment on positivity, and check covariate balance after weighting (standardized mean differences < 0.1). *(~5 h · Hernán & Robins, Causal Inference: What If, Ch. 12–13, and the Python code linked from the book site)*
4. **Front-door adjustment, proved and tested** — Prove the front-door formula P(y | do(x)) = Σₘ P(m | x) Σₓ′ P(y | m, x′) P(x′) by applying the backdoor criterion twice (or from the rules of the do-calculus). Then simulate X → M → Y with an unobserved U → X and U → Y: show naive regression is biased, the front-door estimate matches the ground truth you obtain by actually intervening on X in the simulator, and the estimate breaks once you add a direct X → Y edge. *(~4 h · Primer Ch. 3; Pearl, Causality, on the do-calculus and the front-door criterion; Brady Neal's lectures on identification)*
5. **Which way does causation run?** — Generate cause–effect pairs Y = f(X) + N with N independent of X, using nonlinear f and either Gaussian or non-Gaussian noise. Fit nonparametric regressions in both directions and test residual independence with HSIC; show the method recovers the direction for nonlinear f, fails for linear f with Gaussian noise (both directions fit equally well), and explain why. Then run it on about 10 of the Tübingen cause–effect pairs (e.g., altitude → temperature) and report accuracy with an honest error bar. Close with a half-page critique: what evidence would convince you that Dasgupta et al.'s meta-RL agents reason interventionally rather than associationally, and how does that relate to Schölkopf et al.'s case for causal representation learning? *(~5 h · Peters, Janzing & Schölkopf, Elements of Causal Inference — cause–effect models with two variables; Schölkopf et al., Towards Causal Representation Learning; Dasgupta et al., Causal Reasoning from Meta-Reinforcement Learning)*

**🏗️ Mini-project — The thermal chamber is a do-operator:** Build a simulated measurement scenario (optionally on real hardware): time of day S drives both ambient temperature T and supply-voltage sag V; a firmware duty cycle D rises with T through a thermostat-like control loop; self-heating H depends on D; and the measured offset O depends on T, H, and V. (1) Draw the DAG; decide whether you want the total effect of T on O or the controlled direct effect with D held fixed, and which one is identifiable from field-style observational logs, with which adjustment set. (2) Generate observational data and estimate the effect naively and with backdoor adjustment (regression with standardization, or IP weighting). (3) Generate interventional data — set T as a thermal chamber would, and set D from firmware — and compare. (4) Optional hardware: an MCU's internal temperature sensor and ADC reading a reference, with the duty cycle forced in firmware and the ambient varied with a hot-air gun or a cold pack (keep the gun on its lowest setting, moving, and well back from the board — it can melt plastics and damage parts long before the MCU reads its limit). Draws on the Primer's adjustment and mediation material and What If's estimation methods. Deliverable: `projects/math/10-causal-bench/` notebook + a one-page memo specifying what to log in the field so the effects you care about are identifiable. Success: the adjusted observational estimates agree with the interventional ground truth within their confidence intervals, the naive estimate is measurably biased, and the memo states every identification assumption. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Define P(Y | do(X = x)) and explain how it differs from P(Y | X = x), with an example where the two differ.
2. State the backdoor criterion.
3. In a chain, a fork, and a collider, does conditioning on the middle node open or block the path?
4. Misconception: "adjusting for more covariates can only reduce bias." Sketch two DAGs where adding an adjustment variable makes the estimate worse.
5. What is positivity, how do you check it, and what happens to IP weights when it is nearly violated?
6. Name the three rungs of Pearl's ladder of causation and give one engineering question at each rung.
7. Why can't you tell X → Y from Y → X with linear-Gaussian data, yet you can with a nonlinear additive-noise model?
8. Explain to a smart friend in 3 sentences why a randomized experiment answers a causal question that a huge observational dataset can't.
