# Differential Equations

## Why This Section Matters

Differential equations describe how systems evolve over time — they are the language of dynamics. In physics, they model everything from planetary orbits to fluid flow. In biology, they describe population dynamics, epidemics, and neural firing. In modern ML, neural ODEs replace discrete layers with continuous dynamics, state-space models (SSMs) like Mamba use differential equations for sequence modeling, and diffusion models use stochastic differential equations to generate data. Understanding ODEs, PDEs, and dynamical systems gives you the mathematical foundation for these frontier architectures.

---

## Prerequisites

- Section 01 (Linear Algebra) — eigenvalues, matrix exponentials
- Section 02 (Calculus) — differentiation, integration, multivariable calculus

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Nonlinear Dynamics and Chaos | Steven Strogatz | 2015 | — | The best introduction to dynamical systems and chaos theory. Strogatz writes with exceptional clarity and intuition. Covers phase portraits, bifurcations, limit cycles, and chaos. Essential. |
| | Course (Free) | MIT 18.03 Differential Equations | Arthur Mattuck | — | [Link](https://ocw.mit.edu/courses/18-03sc-differential-equations-fall-2011/) | MIT's comprehensive ODE course. Covers first-order, second-order, Laplace transforms, and systems of ODEs with excellent problem sets. |
| | Video Series | Differential Equations | 3Blue1Brown | — | [Link](https://www.youtube.com/playlist?list=PLZHQObOWTQDNPOjrT6KVlfJuKtYTftqH6) | Beautiful visual explanations of differential equations, phase space, and dynamical systems. Classic 3Blue1Brown quality. |
| | Book | Elementary Differential Equations and Boundary Value Problems | Boyce, DiPrima, Meade | 2017 | — | The standard undergraduate ODE textbook. Comprehensive coverage with applications. Good computational reference. |
| | Book | Partial Differential Equations: An Introduction | Walter Strauss | 2007 | — | Accessible introduction to PDEs: wave equation, heat equation, Laplace equation, Fourier methods. Foundation for understanding physics simulations and neural PDE solvers. |
| | Book | Ordinary Differential Equations | Vladimir Arnold | 1992 | — | A geometric approach to ODEs by one of the greatest mathematicians. Emphasis on qualitative behavior and phase space. Elegant and insightful. |
| | Paper | Neural Ordinary Differential Equations | Ricky Chen et al. | 2018 | [Link](https://arxiv.org/abs/1806.07366) | The paper that introduced neural ODEs — treating neural networks as continuous dynamical systems. Seeing the math here connects this section directly to ML. |
| | Course (Free) | Nonlinear Dynamics and Chaos | Steven Strogatz | — | [Link](https://www.youtube.com/playlist?list=PLbN57C5Zdl6j_qJA-pARJnKsmROzPnO9V) | Strogatz's own lectures on nonlinear dynamics. Watch alongside the textbook for the full experience. |
| | Paper | Structured State Spaces for Sequence Modeling (S4) | Albert Gu et al. | 2021 | [Link](https://arxiv.org/abs/2111.00396) | State-space models for sequence processing — the mathematics of continuous-time dynamics applied to deep learning. Connects ODEs to modern architectures. |
| | Book | Stochastic Differential Equations | Bernt Øksendal | 2003 | — | Introduction to SDEs, Itô calculus, and stochastic analysis. Foundation for diffusion models (DDPM, score-based generative models). Advanced but increasingly relevant. |

---

## Suggested Order

1. **3Blue1Brown — Differential Equations** — Start with visual intuition.
2. **MIT 18.03** — Build computational fluency with ODEs.
3. **Strogatz — Nonlinear Dynamics and Chaos** — The core text. Study phase portraits, bifurcations, and chaos.
4. **Strogatz lectures** — Watch alongside the book.
5. **Strauss — PDEs** — Study wave, heat, and Laplace equations for physics and scientific computing foundations.
6. **Chen et al. — Neural ODE paper** — Connect to ML applications.
7. **Gu et al. — S4 paper** — See differential equations powering modern sequence models.
8. **Øksendal — SDEs** — Advanced. Study when tackling diffusion models mathematically.
