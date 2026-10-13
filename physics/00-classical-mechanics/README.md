# Classical Mechanics

## Why This Section Matters

Classical mechanics is the bedrock of all physics. Newtonian mechanics gives you the intuition for forces and motion; Lagrangian and Hamiltonian mechanics provide the elegant mathematical frameworks that generalize to quantum mechanics, statistical mechanics, and modern field theory. The principle of least action, conservation laws via Noether's theorem, and phase-space thinking are ideas you'll use in every subsequent section. This is where you learn to *think like a physicist*.

---

## 🎯 Learning Objectives

After this section you can:
- Derive equations of motion for constrained, multi-degree-of-freedom systems (double pendulum, bead on a rotating hoop, torque-free rigid body) from a Lagrangian, and sanity-check them with limiting cases and conserved quantities.
- Apply Noether's theorem to read conserved quantities off a Lagrangian's symmetries, and explain when the energy function h = Σ q̇ᵢ ∂L/∂q̇ᵢ − L is conserved but is *not* the total energy.
- Construct Hamiltonians and phase portraits, state Liouville's theorem, and demonstrate numerically why area-preserving (symplectic) integrators respect it and explicit Euler does not.
- Analyze damped and driven oscillators (resonance curve, phase lag, Q ≈ ω₀/Δω, ring-down) and map them term-by-term onto a series RLC circuit you can measure on the bench.
- Estimate before calculating: use dimensional analysis, mechanical similarity, and limiting cases to predict scaling laws (pendulum period, Kepler's third law, drag regimes).

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | The Feynman Lectures on Physics, Vol. 1 — Feynman, Leighton, Sands | Book | 🔑 | [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/) |
| 2 | Classical Mechanics — John R. Taylor | Book | 🔑 | — |
| 3 | MIT 8.01SC Classical Mechanics (Fall 2016) — Chakrabarty, Dourmashkin et al. | Course | 🔑 | [MIT OCW](https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/) |
| 4 | Classical Mechanics (The Theoretical Minimum) — Leonard Susskind | Course | | [YouTube](https://www.youtube.com/playlist?list=PL47F408D36D4CF129) |
| 5 | Introduction to Classical Mechanics — David Morin | Book | | — |
| 6 | Essence of Calculus — 3Blue1Brown | Video | | [YouTube](https://youtube.com/playlist?list=PLZHQObOWTQDMsr9K-rj53DwVRMYO3t5Yr) |
| 7 | Mechanics — Landau & Lifshitz | Book | | — |
| 8 | Classical Mechanics — Herbert Goldstein | Book | | — |

> 🔑 = must-read

---

## Suggested Order

**Core path (🔑):** *Feynman Lectures* Vol. 1 mechanics chapters → MIT 8.01SC lectures → Taylor, *Classical Mechanics*

1. **3Blue1Brown — Essence of Calculus** — Refresh your calculus foundations before diving into mechanics.
2. **Feynman Lectures, Vol. 1** — Read the mechanics chapters (Ch. 1–14 and 18–25) for unmatched physical intuition. Ch. 21–25 (harmonic oscillator, resonance, transients, linear systems) map directly onto circuit intuition; Ch. 15–17 are special relativity, so save them for Section 05.
3. **MIT 8.01SC (MIT OCW)** — Watch alongside Feynman for problem-solving technique; the course has full lecture videos, problem sets, and exams. (Walter Lewin's well-known 8.01 lectures are no longer hosted by MIT, which removed them from its online platforms in December 2014 after an investigation found he had sexually harassed an online learner.)
4. **Taylor — Classical Mechanics** — Work through this as your primary textbook. Covers Newtonian, Lagrangian, and Hamiltonian mechanics with excellent problems.
5. **Morin — Introduction to Classical Mechanics** — Supplement Taylor with Morin's challenging problems and elegant solutions.
6. **Susskind — Theoretical Minimum** — Get a second perspective on Lagrangian and Hamiltonian formulations.
7. **Landau & Lifshitz — Mechanics** — For the mathematically mature: the most concise, elegant treatment of analytical mechanics.
8. **Goldstein — Classical Mechanics** — Reference for advanced topics (canonical transformations, Hamilton-Jacobi theory).

---

## 🛠️ Practice

1. **Scaling before solving** — Using only dimensional analysis, predict (up to a constant) the period of a pendulum, the terminal velocity of a sphere under linear and under quadratic drag, and the period of a circular orbit. Then follow Landau & Lifshitz's mechanical-similarity argument: for a potential homogeneous of degree k, show that times scale as t′/t = (l′/l)^(1−k/2), and recover Kepler's third law (k = −1) and amplitude-independent periods (k = 2). Finally, use Taylor's drag constants for spheres in air (β ≈ 1.6×10⁻⁴ N·s/m², γ ≈ 0.25 N·s²/m⁴, so f_quad/f_lin ≈ 1.6×10³·Dv in SI) to decide which law governs a 10 µm dust grain, a 2 mm raindrop, and a pitched baseball. Deliverable: one page; you're right if every result is dimensionally consistent and the k = −1 and k = 2 limits fall out. *(~1.5 h · Morin Ch. 1; Landau & Lifshitz (mechanical similarity); Taylor Ch. 2)*
2. **Least action by brute force** — Discretize a path x(t) into ~100 points with fixed endpoints and minimize the discrete action S = Σ[½m(Δx/Δt)² − V(x)]Δt with `scipy.optimize.minimize` for (a) a ball thrown vertically and (b) a harmonic oscillator. Overlay the analytic trajectories. Then, for the oscillator with total time T > π/ω, show the true path is a *saddle* of S: compute the Hessian of the discrete action and find a perturbation direction that lowers S. Deliverable: notebook with path overlays and S vs perturbation amplitude. Success: trajectory error < 1%, and a negative Hessian eigenvalue appears exactly when T crosses π/ω. *(~2.5 h · Feynman Vol. 2 Ch. 19 "The Principle of Least Action" (Vol. 2 is listed in Section 03); Taylor Ch. 6; Susskind, Theoretical Minimum)*
3. **Lagrangians, Noether, and the energy function** — Derive by hand, then with a ~30-line sympy helper that turns any L(q, q̇, t) into Euler–Lagrange equations, the EOM for: a double pendulum; a bead on a hoop spun at fixed ω (find the bifurcation at ω² = g/R); a charged particle in a uniform B field in the symmetric gauge A = ½B × r. For each, list cyclic coordinates and conserved momenta. Show for the bead that h is conserved while mechanical energy is not (the motor does work), and for the charged particle that the conserved canonical angular momentum is mr²φ̇ + ½qBr², not mr²φ̇. Success: sympy EOM minus hand EOM simplifies to zero; a tight-tolerance numerical run conserves h to < 10⁻⁸ relative. *(~3 h · Taylor Ch. 7 & 13; Susskind, Theoretical Minimum; Goldstein)*
4. **Resonance on the bench (oscillator ↔ RLC)** — Derive the steady-state amplitude and phase of a driven damped oscillator, show that the power resonance's full width equals the damping rate (Q = ω₀/Δω), and write the exact dictionary m ↔ L, b ↔ R, k ↔ 1/C. Build generator → 10 mH → 10 nF → 10 Ω sense resistor → ground (f₀ ≈ 15.9 kHz, √(L/C) = 1 kΩ). Measure (a) ring-down: drive with a low-frequency square wave, fit the envelope decay τ, Q = πf₀τ; (b) frequency response: sweep, record V_R amplitude and phase on the scope, find the −3 dB points (V_R's bandwidth is exactly R_total/2πL). Include the generator's 50 Ω and the inductor's measured ESR in R_total. Success: ring-down Q and bandwidth Q agree within ~10% and match √(L/C)/R_total (expect roughly 10–15). *(~3 h · Taylor Ch. 5; Feynman Vol. 1 Ch. 21, 23–25; MIT 8.01SC)*
5. **Liouville on a laptop** — Map a 200-vertex polygon of initial conditions in a harmonic oscillator's phase space through one period with forward Euler, RK4, and velocity Verlet at ωΔt = 0.1. Because the dynamics are linear, edges stay straight and the shoelace formula gives the exact area. Show Euler's area grows by (1 + ω²Δt²) per step, RK4's shrinks slightly, and Verlet's is conserved to round-off — then explain each via the determinant of the one-step map. Repeat for a large-amplitude pendulum, refining the polygon as it shears. *(~2 h · Taylor Ch. 13 (Liouville's theorem); Susskind, Theoretical Minimum; Goldstein (canonical transformations))*

**🏗️ Mini-project — Tennis-Racket Theorem with an IMU:** Integrate Euler's equations for a torque-free body with I₁ < I₂ < I₃; linearize to get the growth rate of the intermediate-axis instability; plot trajectories on the intersection of the energy ellipsoid (2T = Σ Iᵢωᵢ²) and the angular-momentum sphere (L² = Σ Iᵢ²ωᵢ²). Then measure it: fix a dev board with a 6-axis MEMS IMU (gyro full scale ±2000 °/s, logging ≥ 500 Hz to flash) inside a padded rectangular box with I₁:I₂:I₃ roughly 1:2:3 — compute the inertias from dimensions and mass, or measure them with a bifilar pendulum — and toss it spinning about the middle axis. Simulate from the first in-flight gyro sample and overlay simulated vs measured ω(t). (Fallback sensor: a phone's gyroscope via a logging app.) Deliverable: `projects/physics/00-tennis-racket/` with logging firmware notes, notebook, and a one-page write-up. Success: measured flip period within ~20% of simulation, and 2T and L² computed from the data stay constant within your sensor and inertia uncertainty across each free-flight segment. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Hamilton's principle: what is varied, what is held fixed, and what condition on S gives the Euler–Lagrange equations?
2. Why do constraint forces disappear from the Lagrangian formulation, and how do you recover them if you need them?
3. A coordinate is cyclic. What is conserved, and which symmetry of L is responsible?
4. A motor spins a hoop at fixed ω with a bead on it. Is mechanical energy conserved? Is h? Why do the two differ?
5. A struck 440 Hz tuning fork's amplitude falls by 1/e in about 3 s. Estimate its Q.
6. True or false: a driven damped oscillator's displacement amplitude peaks exactly at ω₀. What quantity *does* peak exactly at ω₀?
7. What does Liouville's theorem forbid in a Hamiltonian system, and why does that make explicit Euler a poor choice for long orbital simulations?
8. Explain to a smart friend in 3 sentences why "nature picks the path of stationary action" predicts the same motion as F = ma — and why "least" is not quite the right word.
