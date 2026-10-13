# Quantum Mechanics

## Why This Section Matters

Quantum mechanics is the most successful and counterintuitive theory in all of physics. It governs everything from atomic structure to semiconductor devices, lasers, and quantum computing. You'll learn the mathematical framework of Hilbert spaces, operators, and wavefunctions that replaces classical determinism with probability amplitudes. The formalism here — Dirac notation, eigenvalue problems, perturbation theory — is the foundation for quantum field theory, quantum information, and the quantum-inspired algorithms increasingly used in machine learning.

**Prerequisites:** [Section 00 — Classical Mechanics](../00-classical-mechanics/README.md), [Section 01 — Waves and Optics](../01-waves-and-optics/README.md), and linear algebra (vector spaces, eigenvalues, Hermitian matrices) — the language of the whole subject

---

## 🎯 Learning Objectives

After this section you can:
- Solve the time-independent Schrödinger equation analytically for the standard potentials (infinite and finite wells, harmonic oscillator, delta function) and numerically by finite differences, and use each to check the other.
- Treat two-state systems in Dirac notation — spin-½, the ammonia molecule, photon polarization — computing stationary states, time evolution, and Rabi oscillations.
- Calculate tunneling probabilities (exact rectangular barrier and WKB) and explain their device consequences: the STM's ~10× current change per ångström, the gate-oxide thinning limit, resonant-tunneling diodes.
- State the measurement postulate and the generalized uncertainty relation, and distinguish intrinsic quantum spread from measurement disturbance and instrument noise.
- Estimate quantum energy scales (confinement in a 5 nm well, the ≈ 24 GHz ammonia inversion line) and judge when quantum effects matter in a device.

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Introduction to Quantum Mechanics (3rd ed., 2018) — David J. Griffiths & Darrell F. Schroeter | Book | 🔑 | — |
| 2 | The Feynman Lectures on Physics, Vol. 3 — Feynman, Leighton, Sands | Book | 🔑 | [feynmanlectures.caltech.edu](https://www.feynmanlectures.caltech.edu/) |
| 3 | MIT 8.04 Quantum Physics I — Barton Zwiebach | Course | 🔑 | [MIT OCW](https://ocw.mit.edu/courses/8-04-quantum-physics-i-spring-2016/) |
| 4 | Quantum Mechanics (The Theoretical Minimum) — Leonard Susskind | Course | | [YouTube](https://www.youtube.com/playlist?list=PL701CD168D02FF56F) |
| 5 | Some light quantum mechanics — 3Blue1Brown | Video | | [YouTube](https://www.youtube.com/watch?v=MzRCDLre1b4) |
| 6 | Principles of Quantum Mechanics — R. Shankar | Book | | — |
| 7 | Modern Quantum Mechanics — J.J. Sakurai & Jim Napolitano | Book | | — |
| 8 | Quantum Mechanics — Cohen-Tannoudji, Diu, Laloe | Book | | — |
| 9 | Quantum Mechanics for Scientists and Engineers — David A. B. Miller (2008) | Book | | [Cambridge](https://doi.org/10.1017/CBO9780511813962) |

> 🔑 = must-read

---

## Suggested Order

**Core path (🔑):** *Feynman Lectures* Vol. 3 → MIT 8.04 (Zwiebach) → Griffiths & Schroeter, *Introduction to Quantum Mechanics*

1. **3Blue1Brown — Some light quantum mechanics** — Build visual intuition for quantum states, superposition, and measurement.
2. **Feynman Lectures, Vol. 3** — Feynman's unique approach to quantum mechanics. Start here for physical intuition before formalism.
3. **MIT 8.04 (Zwiebach)** — Rigorous undergraduate course with excellent problem sets.
4. **Griffiths & Schroeter — Introduction to Quantum Mechanics** — Your primary textbook (the 3rd edition added Schroeter as co-author). Work through systematically: wavefunctions, the Schrödinger equation, angular momentum, spin, perturbation theory.
5. **Miller — Quantum Mechanics for Scientists and Engineers** — Written by a Stanford electrical-engineering professor for engineers and applied physicists. Use it alongside or after Griffiths for the device-oriented topics (tunneling, electrons in crystals, time-dependent perturbation theory for optical absorption) that lead into semiconductors and photodetectors in Section 08.
6. **Susskind — Theoretical Minimum** — A second perspective emphasizing the mathematical structure.
7. **Shankar — Principles of Quantum Mechanics** — More mathematically rigorous treatment with excellent coverage of the Dirac formalism.
8. **Sakurai — Modern Quantum Mechanics** — Graduate-level text. Start with chapters on spin and angular momentum.
9. **Cohen-Tannoudji** — Comprehensive reference; use for specific topics as needed.

---

## 🛠️ Practice

1. **A Schrödinger solver in 30 lines** — Discretize H = −(ħ²/2m)d²/dx² + V(x) on a grid (N ≈ 2000, units ħ = m = 1), build the tridiagonal matrix, and get the lowest ten eigenpairs with `scipy.linalg.eigh_tridiagonal`. Verify against Griffiths's analytic results for the infinite well (E_n ∝ n²) and the harmonic oscillator (E_n = (n + ½)ħω); count the bound states of a finite well against the analytic count from its z₀ parameter; then compute the ground-state tunneling splitting of a symmetric double well vs barrier height and show it falls roughly exponentially. Success: eigenvalue errors < 10⁻⁴ and scaling as (grid spacing)². *(~3 h · Griffiths Ch. 2; MIT 8.04 (Zwiebach); Shankar)*
2. **Two-state systems: ammonia and Rabi** — Following Feynman's ammonia chapter, write H = [[E₀, −A], [−A, E₀]], find the stationary states and the 2A splitting (≈ 24 GHz for NH₃ — the ammonia-maser line). Add a field 𝓔₀cos ωt coupling through the dipole moment and integrate the time-dependent equations with `solve_ivp` on the complex 2-vector. Show (a) complete population transfer on resonance at the Rabi frequency Ω ∝ μ𝓔₀/ħ, (b) maximum transfer Ω²/(Ω² + Δ²) off resonance, (c) where the rotating-wave approximation fails as Ω approaches ω. Success: numerical transfer within 1% of the Rabi formula in the RWA regime. *(~3 h · Feynman Vol. 3 Ch. 8–9; Susskind, Theoretical Minimum; Sakurai (time-dependent two-state problems))*
3. **Three polarizers, one photodiode** — With a laser pointer or LED, two or three linear-polarizer sheets, and a photodiode into a transimpedance amp (a phone light-meter app is the fallback), measure Malus's law I(θ) = I₁cos²θ from 0° to 180° in 15° steps. Cross two polarizers, insert a third between them, rotate it, and fit I(θ) = (I₁/4)sin²2θ. Interpret each intensity as a single-photon probability (state → projection → new state) and explain why adding a filter *increases* transmission. Subtract dark offsets; beware that laser pointers are usually already linearly polarized (and LCD screens strongly so), which makes the first polarizer's transmission depend on its angle. **Safety:** if you use a laser pointer, keep it Class 2 (< 1 mW) and never look into the beam or its reflections off the sheets. Success: both fits R² > 0.98, with the 45° maximum ≈ I₁/4 times the polarizer's efficiency. *(~2.5 h · 3Blue1Brown "Some light quantum mechanics"; Feynman Vol. 3 Ch. 11 (polarization states of the photon); Sakurai (opening Stern–Gerlach/polarizer analogy))*
4. **Tunneling, from STMs to gate oxides** — Derive the exact transmission through a rectangular barrier and its WKB approximation; plot both vs width for a 4 eV barrier and show κ = √(2mφ)/ħ ≈ 1.0 Å⁻¹, so current drops ~8× per ångström — the reason an STM resolves atoms. Apply WKB to a SiO₂ gate oxide (barrier ≈ 3 eV, effective mass ≈ 0.4–0.5 mₑ) at 3, 2, and 1.2 nm, and explain why thinning stopped near 1.2 nm and high-k dielectrics took over (expect roughly an order of magnitude more leakage per 2 Å). Success: WKB and exact agree within a factor ~2 once κd > 3; a short note with the per-nanometre leakage factor. *(~2.5 h · Griffiths (finite barrier; WKB approximation); MIT 8.04 (tunneling); Cohen-Tannoudji (square-barrier complements))*

**🏗️ Mini-project — Wave Packets and Resonant Tunneling:** Write a 1D time-dependent Schrödinger solver with Crank–Nicolson (sparse tridiagonal, unitary by construction) and fire Gaussian wave packets at (a) a single barrier and (b) a double barrier — e.g. two thin barriers (≈ 1–2 nm, 0.3 eV) around a 5 nm well with GaAs-like effective mass 0.067 mₑ, or the dimensionless equivalent. Measure transmitted probability vs mean packet energy and compare with the stationary T(E) from a transfer-matrix calculation (convolved with the packet's energy spread); locate the resonant peaks and compare them with the quasi-bound levels of the well from your exercise-1 eigensolver. Explain how these resonances give a resonant-tunneling diode its negative differential resistance. Deliverable: notebook, animation, and a one-page explainer in `projects/physics/04-resonant-tunneling/`. Success: norm conserved to 10⁻¹⁰ over the run; packet-derived T(E) within a few percent of the convolved transfer-matrix curve; resonance energies within ~5% of the quasi-bound levels. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Write the time-independent Schrödinger equation. Why are bound-state energies discrete when scattering-state energies are not?
2. What does |ψ(x)|² mean, and how can ⟨x⟩ differ from the most probable position in an excited state?
3. Estimate the ground-state energy of an electron in a 5 nm infinite well with the free mass (≈ 15 meV) and with GaAs's 0.067 mₑ. Compare both with kT at 300 K.
4. "The uncertainty principle exists because measuring a particle disturbs it." What does Δx·Δp ≥ ħ/2 actually say?
5. In ammonia, why are the energy eigenstates symmetric and antisymmetric combinations rather than "N above" and "N below"? What sets the 24 GHz line?
6. Why does an STM's tunneling current change by roughly an order of magnitude per ångström of gap?
7. Why does inserting a third polarizer between two crossed polarizers let light through?
8. Explain to a smart friend in 3 sentences why amplitudes, not probabilities, add — and what that has to do with interference.
