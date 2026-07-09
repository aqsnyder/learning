# Physics-Informed ML and Frontiers

## Why This Section Matters

The intersection of physics and machine learning is one of the most exciting frontiers in science. Physics-informed neural networks (PINNs) embed conservation laws and differential equations directly into loss functions. Neural ODEs learn continuous dynamics from data. Hamiltonian and Lagrangian neural networks build physical structure into network architectures so that conservation laws are satisfied *by construction*. Equivariant networks respect symmetries — the language of physics — yielding models that generalize far better. These ideas are transforming molecular simulation, climate modeling, protein structure prediction, and the design of new materials.

A complementary frontier asks whether physics itself *is* computation. Wolfram's Physics Project proposes that the universe emerges from simple hypergraph rewriting rules — deriving general relativity, quantum mechanics, and thermodynamics from discrete computational processes. Whether or not the specific formalism succeeds, the deep connection between computation and physical law is increasingly important.

This section bridges everything you've learned into the cutting edge.

**Prerequisites:** [Section 06 — Computational Physics](../06-computational-physics/README.md), [Section 10 — Nonlinear Dynamics and Chaos](../10-nonlinear-dynamics-and-chaos/README.md), familiarity with deep learning fundamentals

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Neural Ordinary Differential Equations — Chen et al. (2018) | Paper | 🔑 | [arXiv](https://arxiv.org/abs/1806.07366) |
| 2 | Physics-Informed Neural Networks — Raissi, Perdikaris & Karniadakis (2019) | Paper | 🔑 | [arXiv](https://arxiv.org/abs/1711.10561) |
| 3 | Hamiltonian Neural Networks — Greydanus, Dzamba & Schmidhuber (2019) | Paper | | [arXiv](https://arxiv.org/abs/1906.01563) |
| 4 | Lagrangian Neural Networks — Cranmer, Greydanus & others (2020) | Paper | | [arXiv](https://arxiv.org/abs/2003.04630) |
| 5 | Physics-Informed Machine Learning (review) — Karniadakis et al. (2021) | Paper | 🔑 | [DOI](https://doi.org/10.1038/s42254-021-00314-5) |
| 6 | Highly Accurate Protein Structure Prediction with AlphaFold — Jumper et al. (2021) | Paper | | [DOI](https://doi.org/10.1038/s41586-021-03819-2) |
| 7 | Message Passing Neural PDE Solvers — Brandstetter, Worrall & Welling (2022) | Paper | | [arXiv](https://arxiv.org/abs/2202.03376) |
| 8 | Learning to Simulate Complex Physics with Graph Networks — Sanchez-Gonzalez et al. (2020) | Paper | | [arXiv](https://arxiv.org/abs/2002.09405) |
| 9 | E(n) Equivariant Graph Neural Networks — Satorras, Hoogeboom & Welling (2021) | Paper | | [arXiv](https://arxiv.org/abs/2102.09844) |
| 10 | Data-Driven Science and Engineering — Brunton & Kutz | Book | | [databookuw.com](https://databookuw.com/) |
| 11 | A New Kind of Science — Stephen Wolfram (2002) | Book | | [wolframscience.com](https://www.wolframscience.com/nks/) |
| 12 | The Wolfram Physics Project — Stephen Wolfram (2020+) | Project | 🔑 | [wolframphysics.org](https://www.wolframphysics.org/) |

> 🔑 = must-read

---

## Suggested Order

1. **Brunton & Kutz — Data-Driven Science and Engineering** — Start here if you haven't already covered it in Section 09. Builds the bridge from classical dynamical systems to data-driven methods (DMD, SINDy, sparse regression).
2. **Chen et al. — Neural Ordinary Differential Equations (2018)** — The foundational paper. Learn how continuous-depth networks replace discrete layers with ODE solvers.
3. **Raissi et al. — Physics-Informed Neural Networks (2019)** — The PINN framework: encoding PDEs into neural network loss functions. A paradigm shift for scientific computing.
4. **Greydanus et al. — Hamiltonian Neural Networks (2019)** — Learn how embedding Hamiltonian structure into networks guarantees energy conservation.
5. **Cranmer et al. — Lagrangian Neural Networks (2020)** — The Lagrangian counterpart to HNNs, operating in generalized coordinates.
6. **Karniadakis et al. — Physics-Informed ML review (2021)** — Comprehensive review paper that surveys the entire field. Read after the foundational papers for a unified perspective.
7. **Sanchez-Gonzalez et al. — Graph Network Simulators (2020)** — Learning physics from particle interactions using graph neural networks.
8. **Brandstetter et al. — Message Passing Neural PDE Solvers (2022)** — Modern architecture for solving PDEs on arbitrary meshes with message passing.
9. **Satorras et al. — E(n) Equivariant GNNs (2021)** — Symmetry-preserving networks for molecular systems. Key idea: equivariance as an inductive bias.
10. **Jumper et al. — AlphaFold (2021)** — The landmark application of geometric deep learning to protein structure. Understand how physics priors enabled this breakthrough.
11. **Wolfram — A New Kind of Science (2002)** — Read selectively (Chapters 2, 9, 12). The argument that simple programs can generate complex physics. Controversial but thought-provoking.
12. **Wolfram Physics Project (2020+)** — Explore the technical exposition and visualizations. Whether or not the framework succeeds, the idea that spacetime, gravity, and quantum mechanics emerge from hypergraph rewriting is a genuinely novel approach to fundamental physics.
