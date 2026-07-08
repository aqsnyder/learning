# Causal Inference

## Why This Section Matters

Correlation is not causation — but mathematics *can* formalize causation. Causal inference provides the mathematical framework for answering "what if" and "why" questions from data. Pearl's do-calculus lets you reason about interventions; counterfactual reasoning lets you analyze what would have happened under different conditions. In medicine, causal inference determines whether a treatment works; in policy, it evaluates interventions; in ML, causal reasoning is increasingly recognized as essential for building systems that generalize beyond their training distribution. This is where statistics meets philosophy meets rigorous mathematics.

---

## Prerequisites

- Section 03 (Probability and Statistics) — conditional probability, Bayesian reasoning
- Section 06 (Graph Theory) — directed graphs, DAGs

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | The Book of Why: The New Science of Cause and Effect | Judea Pearl, Dana Mackenzie | 2018 | — | The accessible introduction to causal reasoning. Pearl explains causal graphs, interventions, and counterfactuals through vivid examples. Read this first to understand the conceptual revolution. |
| | Book | Causality: Models, Reasoning, and Inference | Judea Pearl | 2009 | — | The technical bible of causal inference. Covers structural causal models (SCMs), do-calculus, counterfactuals, and identification theory rigorously. The definitive reference. |
| | Book | Causal Inference in Statistics: A Primer | Judea Pearl, Madelyn Glymour, Nicholas Jewell | 2016 | — | A shorter, more accessible technical introduction than *Causality*. Good bridge between *The Book of Why* and the full technical treatment. |
| | Book (Free) | Causal Inference: What If | Miguel Hernan, James Robins | 2020 | [Link](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/) | Free textbook from the epidemiology perspective. Covers potential outcomes, inverse probability weighting, and g-methods. Complements Pearl's graphical approach. |
| | Course (Free) | Introduction to Causal Inference | Brady Neal | — | [Link](https://www.bradyneal.com/causal-inference-course) | Free online course with video lectures, slides, and exercises. Excellent modern introduction covering both potential outcomes and graphical approaches. |
| | Paper | Causal Reasoning from Meta-Reinforcement Learning | Dasgupta et al. | 2019 | [Link](https://arxiv.org/abs/1901.08162) | Connects causal reasoning to reinforcement learning and meta-learning. Bridge from causal theory to ML applications. |
| | Paper | Towards Causal Representation Learning | Schölkopf et al. | 2021 | [Link](https://arxiv.org/abs/2102.11107) | Survey connecting causal inference to representation learning in ML. Arguments for why causal reasoning is essential for robust AI. |
| | Book | Elements of Causal Inference | Jonas Peters, Dominik Janzing, Bernhard Schölkopf | 2017 | [Link](https://mitpress.mit.edu/9780262037310/elements-of-causal-inference/) | Machine-learning-oriented treatment of causal inference. Covers causal discovery from data and connections to transfer learning. |

---

## Suggested Order

1. **The Book of Why (Pearl)** — Start here for the conceptual revolution. Accessible and compelling.
2. **Brady Neal — Causal Inference course** — Free lectures for building technical understanding.
3. **Pearl, Glymour & Jewell — Causal Inference in Statistics** — Technical but accessible primer.
4. **Hernan & Robins — Causal Inference: What If** — Epidemiological perspective and potential outcomes framework.
5. **Pearl — Causality** — The full technical treatment. Reference as needed.
6. **Peters et al. — Elements of Causal Inference** — ML-oriented perspective.
7. **Schölkopf et al.** — For the connection to modern representation learning.
