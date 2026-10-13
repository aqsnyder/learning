# Probability and Statistics

## Why This Section Matters

Probability is the mathematics of uncertainty, and it pervades every quantitative discipline. In machine learning, Bayesian inference provides a principled framework for learning from data; in biology, stochastic processes model evolution and gene expression; in physics, statistical mechanics connects microscopic randomness to macroscopic laws. This section builds from foundational probability through Bayesian reasoning to stochastic processes and Markov chains — the mathematical backbone of everything from MCMC sampling to hidden Markov models to diffusion processes in generative AI.

---

## Prerequisites

- Section 00 (Mathematical Thinking) — proof basics
- Section 01 (Linear Algebra) — matrix operations
- Section 02 (Calculus) — integration, series

---

## 🎯 Learning Objectives

After this section you can:
- Solve probability problems with conditioning, Bayes' rule, the law of total probability, and indicator random variables (linearity of expectation), and confirm the answers by simulation.
- Characterize measured noise statistically — distribution, mean and variance with uncertainty, autocorrelation — and predict how much averaging helps and when it stops helping.
- Derive and compare estimators for one parameter (MLE with Fisher information, Bayesian posterior, bootstrap) and measure whether their intervals achieve their nominal coverage.
- State the LLN and CLT precisely, demonstrate their failure modes (heavy tails, dependence), and bound tail probabilities with Chebyshev and Hoeffding.
- Analyze a finite Markov chain (stationary distribution, mixing) and implement Metropolis–Hastings to sample a posterior, validated against a known answer.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Course (Free) | Statistics 110: Probability | Joe Blitzstein | — | [Link](https://projects.iq.harvard.edu/stat110) | Harvard's legendary probability course. Blitzstein's teaching is exceptional — builds deep intuition through storytelling and strategic problem-solving. Full lectures, textbook, and problem sets available free. |
| 🔑 | Book | All of Statistics: A Concise Course in Statistical Inference | Larry Wasserman | 2004 | — | Covers probability, statistical inference, Bayesian methods, and nonparametric statistics in one dense but accessible volume. The ideal single reference for a mathematically mature reader. |
| | Book (Free) | Introduction to Probability | Joe Blitzstein, Jessica Hwang | 2019 | [Link](https://projects.iq.harvard.edu/stat110/home) | The textbook companion to Stat 110. Excellent exposition with strategic exercises. Covers counting, conditioning, distributions, Markov chains, and more. |
| | Book | Introduction to Probability and Statistics for Engineers and Scientists | Sheldon Ross | 2020 | — | Applied probability and statistics with engineering focus. Good for building computational fluency alongside theory. |
| | Video Series | StatQuest | Josh Starmer | — | [Link](https://www.youtube.com/@statquest) | Fun, clear, no-nonsense visual explanations of probability, distributions, hypothesis testing, Bayesian inference, and more. Excellent gap-filler. |
| | Book (Free) | Bayesian Data Analysis | Andrew Gelman et al. | 2013 | [Link](http://www.stat.columbia.edu/~gelman/book/) | The definitive reference for applied Bayesian statistics. Covers hierarchical models, MCMC, model checking, and practical Bayesian workflow. The 3rd-edition PDF is free for non-commercial use on the book page. |
| | Book | Introduction to Probability Models | Sheldon Ross | 2023 | — | Focused treatment of stochastic processes: Markov chains, Poisson processes, queuing theory, and renewal theory (13th edition). Essential for understanding MCMC and diffusion models. |
| | Course (Free) | MIT 6.041 Probabilistic Systems Analysis | John Tsitsiklis | — | [Link](https://ocw.mit.edu/courses/6-041sc-probabilistic-systems-analysis-and-applied-probability-fall-2013/) | MIT's rigorous probability course with excellent problem sets. Good complement to Blitzstein for a more engineering-oriented perspective. |
| | Book | Probability Theory: The Logic of Science | E.T. Jaynes | 2003 | — | A philosophical and mathematical defense of Bayesian probability as extended logic. Deeply influential and thought-provoking. Advanced but illuminating. |
| | Book | Introduction to Stochastic Processes | Gregory Lawler | 2006 | — | Rigorous treatment of Markov chains, martingales, and Brownian motion (2nd edition). Foundation for understanding diffusion models and stochastic calculus. |
| | Course (Free) | Statistical Rethinking (2024 course) | Richard McElreath | 2024 | [Link](https://github.com/rmcelreath/stat_rethinking_2024) | The best on-ramp to applied Bayesian modeling: causal DAGs, multilevel models, and MCMC taught through simulation, with free recorded lectures and course materials (pairs with the book's 2nd edition, CRC 2020). Do this before Gelman's BDA. |
| | Book (Free) | Kalman and Bayesian Filters in Python | Roger Labbe | 2015 | [Link](https://github.com/rlabbe/Kalman-and-Bayesian-Filters-in-Python) | Free, CC-licensed Jupyter-notebook book that builds the g-h filter, Kalman, extended/unscented Kalman, and particle filters up from Bayes' rule. Bayesian inference applied to noisy sensors — directly usable for sensor fusion and measurement work on embedded systems. |

---

## Suggested Order

1. **Stat 110 (Blitzstein)** — Start here. Watch the lectures, read the textbook, do the problem sets. This builds the deepest intuition.
2. **StatQuest** — Use as a supplement to visualize specific concepts (distributions, Bayes' theorem, etc.).
3. **All of Statistics (Wasserman)** — Read as a comprehensive reference. Covers the full landscape from probability through inference.
4. **MIT 6.041** — Optional complement for engineering applications and extra rigor.
5. **McElreath — Statistical Rethinking** — Learn applied Bayesian modeling by building and simulating models.
6. **Labbe — Kalman and Bayesian Filters** — The practical payoff of Bayes' rule for sensors and state estimation.
7. **Gelman — Bayesian Data Analysis** — The reference for Bayesian methods once Rethinking is done.
8. **Ross — Introduction to Probability Models** (or **Lawler** for more rigor) — Study stochastic processes: Markov chains, Poisson processes.
9. **Jaynes** — Read for deep philosophical perspective on probability as reasoning under uncertainty.

---

## 🛠️ Practice

1. **Indicator variables and conditioning** — Solve analytically, then confirm each with a 10⁶-trial simulation (agreement within 3 standard errors): (a) de Montmort's matching problem — P(nobody gets their own hat) → 1/e, and E[number of matches] = 1 for every n; (b) coupon collector — E[T] = n·Hₙ (≈ 225 for n = 50); (c) the birthday problem for 23 people (≈ 0.507) and its Poisson approximation; (d) a test with 99% sensitivity and 99% specificity for a condition with 0.1% prevalence — P(condition | positive) is only about 9%; explain why with a tree. *(~4 h · Stat 110 lectures and strategic practice on conditioning and expectation; Blitzstein & Hwang chapters on conditional probability and expectation)*
2. **The CLT and where it breaks** — Simulate sample means of n = 1, 2, 5, 30, 100 draws from Uniform(0, 1), Exponential(1), and standard Cauchy. Overlay the normal approximation and plot the Kolmogorov distance to it versus n on log–log axes (compare the slopes for the skewed and symmetric cases). Show that the mean of n Cauchy draws is again standard Cauchy — no concentration at all — and name the LLN hypothesis that fails. For the Uniform mean, compare empirical tail probabilities P(|X̄ − ½| > t) with the Chebyshev and Hoeffding bounds. *(~3 h · Blitzstein & Hwang chapter on inequalities and limit theorems; Wasserman's chapters on inequalities and convergence of random variables)*
3. **Noise and the √N rule** — Capture 10⁵–10⁶ samples from an ADC with its input tied to a quiet reference (STM32 ADC, or a bench DMM over SCPI; if you have no hardware, synthesize white + 1/f + random-walk noise). Estimate the mean and σ with confidence intervals, plot a histogram and Q–Q plot, the autocorrelation, and the standard deviation of N-sample averages versus N on log–log axes. White noise gives slope −½; find where your curve flattens and identify which assumption of the √N rule (independence, identical distribution) failed. *(~4 h · Ross, Introduction to Probability and Statistics for Engineers and Scientists; StatQuest on Q–Q plots and standard error; MIT 6.041 on the weak law of large numbers)*
4. **One parameter, four intervals** — Draw n = 20 counts from Poisson(λ = 3.7) (think events per 1 s window). Build a 95% interval for λ four ways: (a) MLE with the Fisher-information (Wald) interval; (b) Bayesian Gamma(1, 0.1) prior (shape, rate) → posterior Gamma(1 + Σx, 0.1 + n) and its central credible interval; (c) bootstrap percentile; (d) the exact chi-square-based interval. Repeat 10⁴ times and report each method's actual coverage of the true λ and mean width. Check: Var(λ̂) ≈ the Cramér–Rao bound λ/n; the bootstrap percentile interval should under-cover (≈ 93%) while the exact interval cannot (it is conservative by construction) — explain both. *(~4 h · Wasserman, chapters on parametric inference, the bootstrap, and Bayesian inference; Gelman et al., Bayesian Data Analysis — single-parameter models)*
5. **Markov chains and MCMC** — (a) For a 4-state link-quality chain (good/fair/poor/down) with a transition matrix you choose, compute the stationary distribution as the left eigenvector for eigenvalue 1, check it against a long simulation, and relate the speed of convergence to the second-largest eigenvalue modulus. (b) Write a ~30-line random-walk Metropolis sampler for the posterior of λ in exercise 4, verify it against the analytic Gamma posterior (mean and 95% interval within Monte Carlo error), then swap in a log-normal prior where no closed form exists. Report the acceptance rate and effective sample size as you tune the step size. *(~4 h · Blitzstein & Hwang chapters on Markov chains and MCMC; Ross, Introduction to Probability Models; Lawler on convergence of Markov chains)*

**🏗️ Mini-project — Noise budget and false-alarm threshold for a sensor channel:** Design a threshold detector for step or pulse events on a sensor channel sampled at 100 S/s, with a budget of one false alarm per day. (1) Characterize the noise from ≥ 10⁶ samples (exercise 3): distribution, tails, autocorrelation. (2) Compute the Gaussian threshold (8.64 × 10⁶ samples/day → ≈ 5.2σ one-sided), then the threshold your empirical tail model implies, accounting for correlated samples and any pre-filtering (averaging changes both σ and the effective number of independent trials). (3) Model false alarms as a Poisson process. Since you can't observe a once-a-day event in one night, validate the tail model at lowered thresholds where it predicts 10–100 alarms per day, then extrapolate. (4) Plot detection probability versus event amplitude, and use Bayes with an assumed event base rate to report P(real event | alarm). Deliverable: `projects/math/03-noise-budget/` notebook + a one-page threshold memo listing every assumption. Success: at each lowered threshold the observed alarm count falls within the Poisson 95% interval of your prediction, and the memo states how far the Gaussian assumption would have misled you. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Bayes' rule and the law of total probability. Without a calculator, roughly what is P(condition | positive) for a 99%/99% test at 0.1% prevalence?
2. Why does linearity of expectation hold even for dependent random variables, and why does that make indicator variables so powerful?
3. Misconception: "a 95% confidence interval has a 95% probability of containing the true value." What does the frequentist guarantee actually say, and what does a Bayesian credible interval say instead?
4. An ADC has 2 LSB rms white noise. How many samples must you average to reach 0.1 LSB rms? Name two real-world effects that break this calculation.
5. Why doesn't the sample mean of Cauchy random variables converge? Which hypothesis of the law of large numbers fails?
6. What does the Cramér–Rao bound bound, and under what conditions is the MLE asymptotically efficient?
7. When does a finite Markov chain have a unique stationary distribution, and when does it converge to it from every starting state?
8. Explain the Central Limit Theorem to a smart friend in 3 sentences, including one situation where it fails.
