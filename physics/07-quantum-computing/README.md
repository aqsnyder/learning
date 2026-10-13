# Quantum Computing

## Why This Section Matters

Quantum computing harnesses quantum mechanical phenomena — superposition, entanglement, and interference — to perform computations that are intractable for classical computers. Understanding qubits, quantum gates, and algorithms like Shor's and Grover's is increasingly important as quantum hardware matures. Quantum error correction, variational quantum eigensolvers, and quantum machine learning sit at the frontier of both physics and computer science. This section bridges the quantum mechanics you've learned with practical computation.

**Prerequisites:** [Section 04 — Quantum Mechanics](../04-quantum-mechanics/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Represent n-qubit states and gates with tensor products, simulate circuits exactly with a statevector, and explain why memory and time scale as 2ⁿ.
- Explain and implement Bernstein–Vazirani, Grover search (≈ (π/4)√N iterations, with overshoot), the quantum Fourier transform, phase estimation, and Shor's reduction of factoring to order finding plus continued fractions.
- Demonstrate entanglement with Bell states and the CHSH inequality — classical bound 2, quantum value 2√2 — and state precisely which assumptions a violation rules out.
- Model noise with density matrices and Kraus operators (bit flip, phase flip, depolarizing, amplitude damping; T₁/T₂), and show how the 3-qubit repetition code suppresses bit flips (p_L = 3p² − 2p³) but not phase flips.
- Critically assess quantum-advantage claims and resource estimates: logical vs physical qubits, gate error rates, and the threshold idea.

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Understanding Quantum Information & Computation — John Watrous (IBM Quantum Learning; successor to the archived Qiskit Textbook) | Course | 🔑 | [IBM Quantum Learning](https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information) |
| 2 | Quantum Computation and Quantum Information — Nielsen & Chuang | Book | 🔑 | — |
| 3 | IBM Quantum Learning | Course | | [quantum.cloud.ibm.com/learning](https://quantum.cloud.ibm.com/learning/en) |
| 4 | Quantum Computing — John Preskill (Caltech Ph219 lecture notes) | Notes | | [theory.caltech.edu](http://theory.caltech.edu/~preskill/ph219/index.html) |
| 5 | Quantum Computing Since Democritus — Scott Aaronson | Book | | — |
| 6 | Some light quantum mechanics — 3Blue1Brown | Video | | [YouTube](https://www.youtube.com/watch?v=MzRCDLre1b4) |
| 7 | Quantum Computer Science: An Introduction — N. David Mermin | Book | | — |
| 8 | Algorithms for Quantum Computation — Peter Shor (1994) | Paper | 🔑 | [Link](https://ieeexplore.ieee.org/document/365700) · [free expanded version (arXiv)](https://arxiv.org/abs/quant-ph/9508027) |
| 9 | Quantum Computing in the NISQ Era and Beyond — John Preskill (2018) | Paper | | [arXiv](https://arxiv.org/abs/1801.00862) |
| 10 | A Quantum Engineer's Guide to Superconducting Qubits — Krantz, Kjaergaard, Yan, Orlando, Gustavsson & Oliver (2019) | Paper | | [arXiv](https://arxiv.org/abs/1904.06560) |
| 11 | Quantum Error Correction Below the Surface Code Threshold — Google Quantum AI and Collaborators (Nature, 2024/2025) | Paper | | [arXiv](https://arxiv.org/abs/2408.13687) |
| 12 | How to Factor 2048 Bit RSA Integers with Less Than a Million Noisy Qubits — Craig Gidney (2025) | Paper | | [arXiv](https://arxiv.org/abs/2505.15917) |

> 🔑 = must-read

---

## Suggested Order

1. **3Blue1Brown — Some light quantum mechanics** — If you haven't already, build visual intuition for quantum states.
2. **Watrous — Understanding Quantum Information & Computation** — The core course: four free units (basics of quantum information, quantum algorithms, the general formulation of quantum information, and quantum error correction) with Qiskit examples. IBM retired the old Qiskit Textbook in favour of IBM Quantum Learning; its GitHub repository was archived in January 2024.
3. **IBM Quantum Learning** — The rest of IBM's courses and tutorials, including running circuits on real hardware.
4. **Shor — Algorithms for Quantum Computation** — Read the paper that launched the field. Understand why quantum computers threaten RSA. The free arXiv version is the expanded 1997 journal paper.
5. **Gidney — Factoring 2048-bit RSA with under a million noisy qubits (2025)** — The current resource estimate behind "quantum computers threaten RSA": fewer than a million noisy qubits running for under a week, assuming 0.1% gate error, nearest-neighbour connectivity, and 1 µs surface-code cycles (down from about 20 million qubits in the 2019 estimate). Read right after Shor to see what "threat" means in engineering terms.
6. **Nielsen & Chuang — Quantum Computation and Quantum Information** — The bible of quantum computing. Work through chapters on quantum circuits, algorithms, and error correction.
7. **Preskill — Lecture Notes** — Caltech's graduate-level notes for deeper theoretical understanding.
8. **Preskill — Quantum Computing in the NISQ Era and Beyond (2018)** — The short essay that named the "noisy intermediate-scale quantum" era: what noisy machines without error correction can and cannot do, and why fault tolerance is the real goal.
9. **Krantz et al. — A Quantum Engineer's Guide to Superconducting Qubits (2019)** — The hardware view, written for engineers: transmon physics, microwave control and readout, noise and decoherence, and characterization. The closest bridge from this section to analog/RF hardware design.
10. **Google Quantum AI — Quantum Error Correction Below the Surface Code Threshold (2024)** — The milestone result: a distance-7 surface-code memory (101 physical qubits) whose logical error rate drops by a factor of about 2.1 each time the code distance grows by two — the first surface code operating clearly below threshold, where adding qubits suppresses logical errors exponentially. Read after Nielsen & Chuang's error-correction chapter.
11. **Aaronson — Quantum Computing Since Democritus** — Entertaining and intellectually stimulating tour connecting complexity theory to quantum mechanics.
12. **Mermin — Quantum Computer Science** — Concise alternative textbook focused on the computer science perspective.

---

## 🛠️ Practice

1. **A statevector simulator from scratch** — In NumPy, store n qubits as a 2ⁿ complex vector; apply 1- and 2-qubit gates by reshaping to an n-axis tensor and contracting with `np.tensordot`/`einsum` (never building 2ⁿ × 2ⁿ matrices); sample measurement outcomes. Implement H, X, Y, Z, S, T, Rz, CNOT, CZ. Validate against Qiskit's `Statevector` on 50 random circuits (fidelity > 1 − 10⁻¹²), then time it up to as many qubits as your RAM allows and predict the memory wall from 2ⁿ × 16 bytes. *(~4 h · Nielsen & Chuang Ch. 4; Watrous / IBM Quantum Learning; Mermin (Cbits and Qbits))*
2. **Interference does the work: BV and Grover** — Implement Bernstein–Vazirani (recover a hidden n-bit string with one oracle query) and Grover search for n = 3–6 on your simulator. Plot success probability vs iteration count with sin²((2k + 1)θ), sin θ = 1/√N, overlaid; show the overshoot (for N = 8: k = 2 gives 94.5%, k = 3 drops to 33%). Run the 3-qubit Grover circuit on IBM hardware (free Open Plan) or a noisy fake backend and compare with ideal. *(~3 h · Nielsen & Chuang Ch. 6; IBM Quantum Learning (Fundamentals of Quantum Algorithms); Aaronson)*
3. **The CHSH game** — Enumerate all 16 deterministic classical strategies in code to prove S ≤ 2 (win probability ¾); compute the quantum value 2√2 (win probability cos²(π/8) ≈ 0.854) for a Bell pair with optimal measurement angles; run it on a simulator and on hardware. Each correlator from N shots has variance (1 − E²)/N, so ideally σ_S ≈ √(2/N). Report S ± σ and how many σ above 2 you land. Success: classical maximum exactly 2 by enumeration; simulator S consistent with 2.83; hardware S above 2 by ≥ 5σ. *(~3 h · Nielsen & Chuang §2.6 (EPR and the Bell inequality); Preskill (entanglement chapter); 3Blue1Brown "Some light quantum mechanics")*
4. **Shor for small numbers** — Implement the classical shell: choose a, check gcd, recover the order r from a measured phase s/r by continued fractions, and get factors from gcd(a^(r/2) ± 1, N). Build quantum order finding for N = 15, a = 7 (r = 4) and N = 21, a = 2 (r = 6) on your simulator, implementing modular multiplication directly as a permutation matrix. Estimate the expected number of runs to success and check it empirically. Then write a paragraph on why a hand-built permutation matrix is "cheating" from a resource standpoint and how the cost of real modular exponentiation grows with n (use the asymptotics in Shor's paper). Success: 3 × 5 and 3 × 7 recovered, and an empirical success rate consistent with your estimate. *(~4 h · Shor (1994); Nielsen & Chuang Ch. 5; Mermin (the RSA chapter))*
5. **Noise and the repetition code** — Write a density-matrix simulator with Kraus channels (bit flip, phase flip, depolarizing, amplitude damping). Encode a logical qubit in the 3-qubit bit-flip code, apply independent flips with probability p, measure syndromes, correct, and plot logical error vs p against 3p² − 2p³, marking the break-even at p = ½. Then apply amplitude damping (T₁) and pure dephasing (T₂), show the code fails against phase errors, and explain how Shor's 9-qubit code fixes that. Success: simulation lies on the analytic curve. *(~3 h · Nielsen & Chuang Ch. 8 & 10; Preskill (quantum error correction))*

**🏗️ Mini-project — Characterize a Quantum Processor Like an Instrument:** Treat an IBM backend as a device under test. (1) Measure a 2-qubit readout assignment (confusion) matrix by preparing |00⟩…|11⟩, and implement readout-error mitigation by inversion. (2) Measure T₁ with a delay sweep (prepare |1⟩, wait, measure), or take the backend's reported calibrations if delays aren't available to you. (3) Build a noise model from the measured and reported numbers and predict the CHSH S and the 3-qubit Grover success probability. (4) Run both on hardware, raw and mitigated, and compare with your predictions. Rehearse everything on a fake backend first to fit within the free plan's monthly QPU minutes. Deliverable: notebook and a one-page "calibration report" in `projects/physics/07-qpu-characterization/` stating each measured parameter with uncertainty, predicted vs measured results, and the dominant error source. Success: predictions within ±0.1 for S and ±10 percentage points for Grover success — or a quantified explanation of the residual (crosstalk, drift, transpiled depth). *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. How many complex amplitudes describe 30 qubits, and how much memory is that at complex128? Why doesn't this mean 30 qubits store that much retrievable information?
2. Write |Φ⁺⟩ and the two-gate circuit that prepares it from |00⟩.
3. Roughly how many Grover iterations are needed for N = 2²⁰, and what happens if you run twice as many?
4. In Shor's algorithm, what does the QFT extract, and what does the classical continued-fraction step do with it?
5. "A quantum computer tries every answer in parallel and reads out the right one." What's wrong with this, and what is the actual mechanism?
6. How does syndrome measurement detect a bit flip without collapsing the encoded superposition?
7. A CHSH violation rules out which combination of assumptions?
8. Explain to a smart friend in 3 sentences why Shor's algorithm threatens RSA while Grover's only halves the effective key length of symmetric ciphers.
