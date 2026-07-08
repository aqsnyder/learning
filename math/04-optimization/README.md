# Optimization

## Why This Section Matters

Optimization is the engine of machine learning — every model trained by gradient descent is solving an optimization problem. But optimization theory extends far beyond ML: convex optimization provides provably optimal solutions in engineering and operations research, duality theory connects seemingly different problems, and understanding the non-convex landscape explains why deep learning works (and when it doesn't). This section builds from convex fundamentals through gradient methods to the non-convex challenges at the frontier of deep learning theory.

---

## Prerequisites

- Section 01 (Linear Algebra) — matrix operations, eigenvalues
- Section 02 (Calculus) — gradients, Hessians, multivariable calculus

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book (Free) | Convex Optimization | Stephen Boyd, Lieven Vandenberghe | 2004 | [Link](https://web.stanford.edu/~boyd/cvxbook/) | The definitive text on convex optimization. Covers convex sets, functions, duality, interior-point methods, and applications. Free PDF and lecture slides available. |
| 🔑 | Course (Free) | Stanford EE364a: Convex Optimization | Stephen Boyd | — | [Link](https://web.stanford.edu/class/ee364a/) | Video lectures accompanying the textbook. Boyd is an exceptional teacher — these lectures bring the theory to life. |
| | Book | Numerical Optimization | Jorge Nocedal, Stephen Wright | 2006 | — | Comprehensive treatment of numerical methods: line search, trust region, conjugate gradient, quasi-Newton methods. Essential reference for algorithm design. |
| | Book (Free) | Mathematics for Machine Learning (Ch. 7) | Deisenroth, Faisal, Ong | 2020 | [Link](https://mml-book.github.io/) | Chapter 7 covers continuous optimization with ML focus: gradient descent, momentum, constrained optimization. Good bridge from theory to practice. |
| | Blog Post | An Overview of Gradient Descent Optimization Algorithms | Sebastian Ruder | 2016 | [Link](https://www.ruder.io/optimizing-gradient-descent/) | Excellent survey of SGD variants: momentum, Nesterov, Adagrad, RMSprop, Adam. Essential reading for understanding modern training. |
| | Course (Free) | MIT 6.079: Introduction to Convex Optimization | Lieven Vandenberghe | — | [Link](https://see.stanford.edu/course/ee364a) | Alternative entry point to the same material with different emphasis. |
| | Book | Introductory Lectures on Stochastic Optimization | John Duchi | — | [Link](https://web.stanford.edu/~jduchi/PCMIConvex.pdf) | Lecture notes covering stochastic gradient methods with convergence analysis. Bridges theory and practice. |
| | Paper | Adam: A Method for Stochastic Optimization | Diederik Kingma, Jimmy Ba | 2014 | [Link](https://arxiv.org/abs/1412.6980) | The Adam optimizer paper — the most widely used optimizer in deep learning. Understanding its design illuminates optimization in practice. |
| | Book | First-Order Methods in Optimization | Amir Beck | 2017 | — | Rigorous treatment of proximal methods, ADMM, and first-order algorithms. Advanced but essential for optimization research. |

---

## Suggested Order

1. **MML Book (Ch. 7)** — Start here for ML-oriented optimization overview.
2. **Ruder — Gradient Descent Survey** — Read for practical understanding of SGD variants.
3. **Boyd & Vandenberghe — Convex Optimization (book + Stanford lectures)** — The core. Work through the first 10 chapters and problem sets.
4. **Kingma & Ba — Adam paper** — Read to connect theory to the most-used optimizer.
5. **Nocedal & Wright** — Use as a reference for numerical methods.
6. **Duchi — Stochastic Optimization** — Advanced. Read for theoretical depth on SGD convergence.
