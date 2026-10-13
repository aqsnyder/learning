# Numerical Methods and Scientific Computing

## Why This Section Matters

Every number that firmware, test scripts, and simulations produce passes through floating point or fixed point. Three things decide whether it means anything:
- **Machine arithmetic.** It is a finite set of numbers with rounding, so ordinary formulas can lose every significant digit.
- **The problem itself.** The condition number caps how many digits any method can deliver.
- **The algorithm.** A backward-stable method delivers all of those digits; an unstable one squanders them.

This section teaches the habits that separate trustworthy computation from plausible-looking garbage:
- reformulating formulas to avoid cancellation;
- separating ill-conditioned problems from unstable algorithms;
- picking interpolation and quadrature schemes by their convergence rates;
- matching integrators to stiff systems;
- diagnosing Newton's method when it misbehaves.

It is the mathematics behind SPICE, LAPACK, `scipy`, and every calibration fit you run. It matters just as much on a microcontroller with a single-precision FPU.

**Where it fits:** this section is numbered 14 only because it was added after the original sections. Take it after Section 07 (or after Section 12). For physics-flavored applications of the same methods, see the physics curriculum's [Computational Physics section](../../physics/06-computational-physics/README.md), which covers Newman's *Computational Physics*, *Numerical Recipes*, MIT 18.085, and FEniCSx.

---

## Prerequisites

- Section 01 (Linear Algebra) — LU, QR, the SVD, and the least-squares and conditioning exercise there
- Section 02 (Calculus and Analysis) — Taylor's theorem with remainder and the Mean Value Theorem; the fixed-point sine mini-project is the natural warm-up. Complex numbers are needed for the complex-step derivative.
- Section 07 (Differential Equations) — linear stability of ODEs; the Euler and finite-difference stability exercises there
- Python with NumPy and SciPy; a C compiler for the microcontroller-flavored parts

---

## 🎯 Learning Objectives

After this section you can:
- Explain IEEE-754 binary32 and binary64 (machine epsilon, spacing, rounding, cancellation), and predict when float32 is inadequate for a firmware quantity such as a timer, an accumulator, or high-resolution ADC data.
- Distinguish the conditioning of a problem from the stability of an algorithm, compute condition numbers, and use backward-error arguments to predict the accuracy a computation can achieve.
- Rewrite unstable formulas into stable ones — quadratic roots, Welford's running variance, compensated summation, complex-step derivatives — and demonstrate the improvement experimentally.
- Choose interpolation and quadrature schemes (Chebyshev nodes and barycentric interpolation; trapezoid, Simpson, Gauss) from their convergence theory, including the trapezoid rule's spectral accuracy on periodic functions.
- Choose explicit or implicit integrators for stiff systems from their stability regions. Implement Newton's method with convergence diagnostics and safeguards.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Paper | What Every Computer Scientist Should Know About Floating-Point Arithmetic | David Goldberg | 1991 | [Link](https://docs.oracle.com/cd/E19957-01/806-3568/ncg_goldberg.html) | The classic tutorial on IEEE-754 (ACM *Computing Surveys*): rounding, ulps and relative error, guard digits, cancellation, and why "obvious" formulas fail. Required reading before writing numeric firmware; free reprint in Oracle's *Numerical Computation Guide*. |
| 🔑 | Book (Free) | Fundamentals of Numerical Computation | Tobin A. Driscoll, Richard J. Braun | — | [Link](https://fncbook.com/) | Free online textbook with complete Julia, MATLAB, and Python versions: floating point and conditioning, linear systems and least squares, root finding, interpolation, quadrature, and initial-value problems including stiffness. The best hands-on first course. |
| | Course (Free) | MIT 18.335J Introduction to Numerical Methods | Steven G. Johnson | 2019 | [Link](https://ocw.mit.edu/courses/18-335j-introduction-to-numerical-methods-spring-2019/) | Graduate numerical analysis: floating point, backward error analysis, conditioning and stability, and dense and iterative linear algebra, with a brief survey of integration and optimization (notes, problem sets and exams; no videos). |
| | Book | Numerical Linear Algebra | Lloyd N. Trefethen, David Bau III | 2022 | — | The classic on how linear algebra is actually computed (25th-anniversary edition of the 1997 text): conditioning, floating-point stability, QR, SVD, eigenvalue algorithms, and iterative Krylov methods in 40 short lectures. Essential once you rely on NumPy/LAPACK results in real work. |
| | Book | Scientific Computing: An Introductory Survey | Michael T. Heath | 2018 | [Link](https://doi.org/10.1137/1.9781611975581) | A broad, readable survey of the whole field (revised 2nd edition, SIAM Classics): error analysis, linear and nonlinear equations, optimization, interpolation, quadrature, ODEs and PDEs, and the FFT. A good single reference. |
| | Book | Accuracy and Stability of Numerical Algorithms | Nicholas J. Higham | 2002 | [Link](https://doi.org/10.1137/1.9780898718027) | The definitive reference on rounding-error analysis (2nd edition): floating point, summation, polynomial evaluation, linear systems, and condition estimation. Dip into the chapter you need. |

---

## Suggested Order

1. **Goldberg** — Floating point first; everything else depends on it.
2. **Driscoll & Braun** — The main text. Work through it in Python, chapter by chapter, alongside the exercises below.
3. **Trefethen & Bau** — Numerical linear algebra: conditioning, stability, Gaussian elimination and pivoting, QR, the SVD, and iterative methods.
4. **MIT 18.335J** — Graduate depth with problem sets, once Driscoll & Braun feels easy.
5. **Heath** — A survey and reference for topics you meet later (PDEs, optimization, the FFT).
6. **Higham** — The reference for rounding-error analysis of a specific algorithm.
7. **Physics, [Computational Physics](../../physics/06-computational-physics/README.md)** — Apply the methods to physical simulation (Newman, FEniCSx).

---

## 🛠️ Practice

1. **Floating point on a microcontroller** *(~3 h · Goldberg; Higham's chapters on floating point and summation; Driscoll & Braun's floating-point section)*
   - (a) From the binary32 bit layout, work out:
     - machine epsilon: 2⁻²³ ≈ 1.19 × 10⁻⁷, against 2.2 × 10⁻¹⁶ for binary64;
     - the largest run of consecutive integers: up to 2²⁴ = 16,777,216, and show that 16,777,217 rounds away;
     - the spacing of float32 values near t = 8192 s (2⁻¹⁰ s ≈ 0.98 ms) and near 2²³ s ≈ 97 days (1 s).
   - (b) Simulate a firmware "seconds since boot" float32 counter that adds 0.001 every 1 ms tick. After 10⁶ ticks it reads ≈ 991.14 s instead of 1000 s.
     - Explain the 0.9% drift: each addition rounds to the spacing of the current total.
     - Fix it two ways: an integer tick counter converted on read, and Kahan-compensated accumulation.
   - (c) Sum 0.1 ten million times in float32:
     - sequentially: ≈ 1,087,937, a 9% error;
     - with Kahan summation, or NumPy's pairwise `np.sum`: ≈ 1,000,000.
     - Bound the naive error with the standard (n − 1)·u·Σ|xᵢ| summation bound, and explain why pairwise summation's bound grows only with log n.

2. **Cancellation and stable reformulations** *(~3 h · Goldberg on cancellation; Higham; Driscoll & Braun on conditioning and finite differences)*
   - (a) For x² − 10⁸x + 1 = 0, the textbook formula gives the small root as 7.45 × 10⁻⁹ in double precision, 25% wrong. Derive the stable form via Vieta (x_small = c / x_large) and get 1.0000000000000000 × 10⁻⁸.
   - (b) Running statistics in float32. Take 10⁵ simulated 16-bit ADC codes around 30,000 with σ = 1.5 LSB (true variance ≈ 2.25 for unrounded samples; rounding them to integer codes adds 1/12 LSB², giving ≈ 2.33).
     - The one-pass formula (Σx² − (Σx)²/n)/(n − 1) returns ≈ 1.75 × 10⁶, nonsense; Welford's update returns 2.251.
     - Explain the failure with the condition number of a subtraction.
     - Implement Welford in C as you would for an MCU.
   - (c) Differentiate eˣ at x = 1 numerically:
     - forward differences have their smallest error near h ≈ √ε ≈ 10⁻⁸ (≈ 7 × 10⁻⁹);
     - central differences near h ≈ ε^(1/3) ≈ 10⁻⁵ (≈ 6 × 10⁻¹¹ at h = 10⁻⁵, against ≈ 2 × 10⁻¹⁰ at 10⁻⁶);
     - the complex-step derivative Im f(x + ih)/h with h = 10⁻²⁰ is exact to machine precision.
     - Derive each optimal h from truncation plus rounding error, and explain why the complex step involves no cancellation.

3. **Ill-conditioned problem or unstable algorithm?** *(~3 h · Trefethen & Bau's lectures on conditioning, stability, and Gaussian elimination; Higham on linear systems; MIT 18.335J notes)*
   - (a) Solve Hx = b with Hilbert matrices for n = 8, 10, 12 and x = (1, …, 1).
     - For n = 10, κ(H) ≈ 1.6 × 10¹³ and the relative error is ~10⁻⁵, yet the relative residual is ~10⁻¹⁶. Explain both with backward error: GEPP is backward stable; the problem is ill-conditioned.
     - At n = 12 (κ ≈ 10¹⁶) the answer is wrong at the 10% level.
   - (b) Solve Wilkinson's growth matrix (1 on the diagonal, −1 below it, last column all ones) for n = 20, 40, 60, with a random x (with x = (1, …, 1) every intermediate is an integer, so the solve stays exact until 2ⁿ⁻¹ passes 2⁵³).
     - κ stays below 30, yet LAPACK's partial pivoting loses accuracy steadily: ~10⁻¹² at n = 20, ~10⁻⁶ at n = 40, and errors of tens of percent at n = 60, because the growth factor is 2ⁿ⁻¹.
     - Show that QR solves the same systems to ~10⁻¹⁵. This is the rare case where the algorithm, not the problem, is to blame.
   - (c) Write a five-line rule of thumb, "digits lost ≈ log₁₀ κ", and add when it fails and why that is rare in practice.

4. **Interpolation and quadrature, the right way** *(~3 h · Driscoll & Braun's chapters on interpolation, function approximation, and numerical integration; Heath; Section 12's DFT)*
   - (a) Interpolate Runge's function 1/(1 + 25x²) on [−1, 1] with a degree-20 polynomial, using `scipy.interpolate.BarycentricInterpolator`.
     - Equispaced nodes give a maximum error ≈ 60; Chebyshev nodes give ≈ 0.015.
     - Explain with the Lebesgue constant, and say what this means for fitting calibration curves with high-degree polynomials.
   - (b) Integrate e^(cos x) over [0, 2π] (exact value 2π·I₀(1)).
     - The trapezoid rule reaches 10⁻⁶ at N = 8 and machine precision at N = 16, while Simpson's rule is worse (10⁻² at N = 8).
     - Contrast ∫₀¹ eˣ dx, where the trapezoid error falls 4× and Simpson's 16× per halving of h.
     - Explain both with the Euler–Maclaurin formula, and connect the periodic case to the DFT (Section 12).

5. **Newton's method and stiffness** *(~4 h · Driscoll & Braun on nonlinear equations and initial-value problems; Heath's chapters on nonlinear equations and ODEs)*
   - (a) Newton versus bisection for √2:
     - Newton's errors are 8.6 × 10⁻², 2.5 × 10⁻³, 2.1 × 10⁻⁶, 1.6 × 10⁻¹² — the number of correct digits doubles each step;
     - bisection needs 40 halvings to reach 10⁻¹².
     - Prove quadratic convergence near a simple root.
   - (b) The embedded classic, 1/√x via the bit-level guess `0x5f3759df`:
     - maximum relative error is 3.4% from the guess alone, 0.175% after one Newton step, and 5 × 10⁻⁶ after two;
     - explain why reinterpreting the float's bits approximates log₂ x.
   - (c) Stiffness. Solve y′ = −1000(y − cos t) − sin t, y(0) = 1, on [0, 10] (solution cos t) with `solve_ivp` at rtol 10⁻⁶.
     - RK45 needs ≈ 20,000 function evaluations; BDF and Radau only a few hundred (≈ 200 and ≈ 240 with SciPy 1.18; exact counts vary by version).
     - Explain from stability regions why explicit methods are stuck at h ≲ 3/1000 for RK45 (2/1000 for forward Euler) long after the fast transient has died.

**🏗️ Mini-project — Mini-SPICE, a transient circuit simulator from scratch:** *(~15 h)* Write a ~400-line Python circuit simulator.

1. **Modified nodal analysis.** Stamps for R, C, L, independent sources, and a Shockley diode (I_s = 10⁻¹⁴ A, n = 1).
2. **DC operating point by Newton–Raphson.** Use junction-voltage limiting. Show the residual's correct digits doubling per iteration, and show what happens without limiting (exp overflow or divergence).
3. **Transient analysis with backward-Euler and trapezoidal companion models.**
   - On an RC step (τ = 1 ms, error at t = τ), backward Euler's error halves each time h halves (1.8 × 10⁻², 9.0 × 10⁻³, 4.6 × 10⁻³ at h = 100, 50, 25 µs). The trapezoidal error quarters (3.1 × 10⁻⁴, 7.7 × 10⁻⁵, 1.9 × 10⁻⁵).
   - On a 1 kHz LC tank at h = 1 µs, backward Euler keeps only 14% of the amplitude after 100 cycles — predict this from |1/(1 + jωh)| per step. The trapezoidal rule holds it to better than 10⁻⁹.
   - With a time step much larger than a circuit time constant (h = 10τ), the trapezoidal amplification factor is −2/3: the error flips sign every step ("trap ringing"), while backward Euler's factor 1/11 decays monotonically. Explain why simulators switch to backward Euler or Gear methods after discontinuities.
4. **Validation.** Simulate a half-wave rectifier with an RC load and compare the ripple with a hand calculation and, if available, ngspice or LTspice.

Draws on Heath (nonlinear equations, ODEs), Driscoll & Braun, Trefethen & Bau (LU on the MNA matrix), and Section 07.

- **Deliverable:** `projects/math/14-mini-spice/` — simulator, test notebook, and a two-page report.
- **Success:**
  - RC and LC results match the predictions above to 2 significant figures;
  - Newton shows quadratic convergence on the diode circuits;
  - rectifier ripple agrees with a reference simulator, or with your hand analysis, within 2%.

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What are machine epsilon for binary32 and binary64, and what is the spacing of float32 numbers near 10⁶?
2. Define the condition number of a problem and backward stability of an algorithm. Why can a backward-stable algorithm still return an inaccurate answer?
3. Why does the textbook quadratic formula lose the small root of x² − 10⁸x + 1 = 0, and how do you fix it?
4. Estimate: you solve a linear system with κ ≈ 10¹⁰ in double precision using a backward-stable method. About how many correct significant digits should you expect?
5. Misconception: "the residual ‖Ax̂ − b‖ is tiny, so x̂ is accurate." When is this false?
6. Why is high-degree interpolation at equispaced points a bad idea, and what fixes it?
7. What makes an ODE stiff, and why does an explicit method's step size stay limited by the fastest mode even after that mode has decayed?
8. Explain to a smart friend in 3 sentences why 0.1 + 0.2 ≠ 0.3 on a computer.
