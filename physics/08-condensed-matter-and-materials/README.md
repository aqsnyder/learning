# Condensed Matter and Materials

## Why This Section Matters

Condensed matter physics studies the emergent behavior of matter in its solid and liquid states — from the quantum mechanics of electrons in crystals to the collective phenomena that give rise to superconductivity, magnetism, and topological phases. Understanding band theory, semiconductors, and crystal structure is essential for anyone working with electronic devices, photovoltaics, or materials science. Philip Anderson's insight that "more is different" — that emergent complexity arises from simple rules — connects directly to modern thinking about neural networks and complex systems.

**Prerequisites:** [Section 04 — Quantum Mechanics](../04-quantum-mechanics/README.md), [Section 02 — Thermodynamics](../02-thermodynamics-and-statistical-mechanics/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Derive phonon dispersion for 1D monatomic and diatomic chains and the tight-binding band E(k) = E₀ − 2t cos ka; explain Brillouin zones, band gaps, and effective mass from band curvature.
- Apply the Drude and Sommerfeld models to copper (scattering time, Fermi energy and velocity, mean free path, Hall coefficient) and state exactly where each model fails.
- Connect band gaps to device behaviour — LED photon energy, a diode's ≈ −2 mV/K forward-voltage tempco, bandgap voltage references — and measure E_g and k_B on the bench.
- Explain ferroelectricity and pyroelectricity with Landau theory, and use it to reason about pyroelectric IR detectors and the DC-bias derating, temperature drift, and microphonics of class-II MLCCs.
- Articulate Anderson's "More Is Different" argument and illustrate it with broken symmetry in a real solid.

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Introduction to Solid State Physics — Charles Kittel | Book | 🔑 | — |
| 2 | The Oxford Solid State Basics — Steven H. Simon | Book | 🔑 | — |
| 3 | Solid State Physics — Ashcroft & Mermin | Book | | — |
| 4 | MIT 8.231 Physics of Solids I (Fall 2006) — Xiao-Gang Wen (problem sets only) | Course | | [MIT OCW](https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/) |
| 5 | Modern Condensed Matter Physics — Girvin & Yang | Book | | — |
| 6 | More Is Different — P.W. Anderson (1972) | Paper | 🔑 | [Link](https://www.science.org/doi/10.1126/science.177.4047.393) |
| 7 | The Oxford Solid State Basics (lecture videos, 2014) — Steven H. Simon | Course | | [Oxford Podcasts](https://podcasts.ox.ac.uk/series/oxford-solid-state-basics) |
| 8 | Modern Semiconductor Devices for Integrated Circuits — Chenming Hu (2010) | Book | | [chu.berkeley.edu (free chapters)](https://www.chu.berkeley.edu/modern-semiconductor-devices-for-integrated-circuits-chenming-calvin-hu-2010/) |

> 🔑 = must-read

---

## Suggested Order

**Core path (🔑):** Anderson, "More Is Different" → Simon, *The Oxford Solid State Basics* → Kittel, *Introduction to Solid State Physics*

1. **Anderson — "More Is Different"** — Read this short, profound essay on emergence. Sets the philosophical context for why condensed matter matters.
2. **Simon — The Oxford Solid State Basics** — Excellent modern introduction. Clearer and more pedagogical than Kittel for a first pass.
3. **Simon — Oxford Solid State Basics lectures (2014)** — Simon's own 21-lecture course on the book; watch alongside it.
4. **Kittel — Introduction to Solid State Physics** — The classic textbook. Work through crystal structure, phonons, free electron model, and band theory. Its chapter on dielectrics and ferroelectrics is the physics of the piezoelectric and pyroelectric materials used in sensors.
5. **Hu — Modern Semiconductor Devices for Integrated Circuits** — The bridge from band theory to the parts on your schematic: carriers, drift and diffusion, pn and metal–semiconductor junctions, MOS capacitors, MOSFETs, and bipolar transistors. All eight chapters are free on the author's site. (Feynman Vol. 3, Ch. 13–14 — "Propagation in a Crystal Lattice" and "Semiconductors" — is a short, intuitive preview.)
6. **MIT 8.231** — The OCW site has problem sets only (no lecture videos or notes); use them for extra practice.
7. **Ashcroft & Mermin — Solid State Physics** — More advanced and comprehensive. Use for deeper coverage of transport, magnetism, and superconductivity.
8. **Girvin & Yang — Modern Condensed Matter Physics** — Modern treatment covering topological phases and quantum Hall effect.

**Next:** [Section 12 — Measurement, Noise, and Sensor Physics](../12-measurement-noise-and-sensor-physics/README.md) is meant to follow this section. It covers the noise and measurement physics of these devices, including Dutta & Horn's review of 1/f noise.

---

## 🛠️ Practice

1. **Chains and bands, numerically** — Build the dynamical matrix of an N-atom chain with periodic boundaries, diagonalize it, and plot ω(k) against 2√(κ/m)|sin(ka/2)|. Make it diatomic (m₁ > m₂) and recover the acoustic and optical branches with the zone-boundary gap between √(2κ/m₁) and √(2κ/m₂). Repeat with a tight-binding Hamiltonian (hopping t), then alternate the hoppings t₁, t₂ and show a gap of 2|t₁ − t₂| opens. Fit the band-bottom curvature for the effective mass and compare with ħ²/(2ta²). Success: numerical eigenvalues on the analytic curves to machine precision. Stretch: compute the winding number of the dimerized chain's Bloch Hamiltonian for t₁ < t₂ vs t₁ > t₂ (Girvin & Yang's topology material). *(~3 h · Simon (1D chain and tight-binding chapters); Kittel (phonons); Feynman Vol. 3 Ch. 13; MIT 8.231)*
2. **Copper by the numbers** — From n = 8.47×10²⁸ m⁻³ and ρ = 1.68×10⁻⁸ Ω·m compute the Drude scattering time (≈ 2.5×10⁻¹⁴ s), Fermi energy (≈ 7.0 eV) and temperature (≈ 8×10⁴ K), Fermi velocity (≈ 1.57×10⁶ m/s), mean free path (≈ 39 nm), the drift velocity for 1 A in a 0.2 mm × 35 µm trace (≈ 1 cm/s), and the Hall voltage for 1 A in 1 T across 35 µm of copper (≈ 2 µV). Contrast with a semiconductor Hall element and explain why Hall sensors aren't made of copper. Finish with a paragraph on Ashcroft & Mermin's account of why Drude got the Wiedemann–Franz ratio about right for the wrong reasons. *(~2 h · Ashcroft & Mermin Ch. 1–2; Simon (Drude and Sommerfeld chapters); Kittel (free-electron Fermi gas))*
3. **Band gaps you can see** — Measure I–V curves of 4–5 LEDs from IR (~940 nm) to blue (~470 nm), using an SMU or an MCU DAC driving a sense resistor with ADC readback. Define the threshold voltage consistently (e.g. at 1 µA, or by extrapolating the exponential region), plot eV_th against hc/λ_peak, and extract h from the slope. List and size the systematics: the ~kT thermal tail, series resistance, band-tail physics in InGaN LEDs, datasheet λ_peak uncertainty. Success: h within 15% of 6.63×10⁻³⁴ J·s with an honest error budget. *(~3 h · Kittel (semiconductor crystals); Simon (semiconductor physics and devices); Feynman Vol. 3 Ch. 14)*
4. **Landau theory: pyro sensors and X7R capacitors** — From F = ½a(T − T_c)P² + ¼bP⁴ − EP derive P_s ∝ (T_c − T)^½, the Curie–Weiss susceptibility above T_c, and the pyroelectric coefficient p = −dP_s/dT, which diverges at T_c. (a) With p ≈ 2×10⁻⁴ C·m⁻²·K⁻¹ (LiTaO₃, T_c of several hundred °C), compute the current from a 1 mm² element warming at 1 mK/s (≈ 0.2 pA) and explain why pyroelectric detectors use 10¹⁰–10¹¹ Ω gate resistors or charge amplifiers, and why they operate far below T_c. (b) Add a DC bias field and show the small-signal permittivity ∂P/∂E falls with bias — the qualitative origin of class-II (BaTiO₃) MLCC DC-bias derating; compare your curve's shape with a manufacturer's DC-bias plot for a 10 µF X5R part, noting what the single-domain model leaves out. (c) Explain why both devices are also piezoelectric, and hence microphonic. *(~3 h · Kittel (dielectrics and ferroelectrics); Simon (mean-field theory); Whatmore (1986), listed in Section 12, for real pyroelectric materials and their figures of merit)*
5. **Read Anderson closely** — Read "More Is Different" twice. Deliverables: (a) a 300-word steelman of the strong reductionist position Anderson argues against; (b) a table mapping each of his examples — ammonia inversion and why large molecules don't show it, crystals as broken translational symmetry, superconductivity — to where the emergent concept appears in Simon or Kittel (rigidity, phonons as collective modes, order parameters); (c) one emergent phenomenon from your own engineering work, naming the level at which its useful laws live. *(~2 h · Anderson (1972); Simon; Feynman Vol. 3 Ch. 9 from Section 04)*

**🏗️ Mini-project — One Transistor, Two Constants:** Build an automated rig to measure Boltzmann's constant and silicon's band gap. Hardware: a small aluminium block heated by a power resistor under PID control (MCU firmware or bench supply plus Python), a reference sensor (calibrated PT100/PT1000 or a high-accuracy digital sensor), and a diode-connected small-signal BJT (e.g. 2N3904) fed by switchable precision currents (e.g. 1 µA and 10 µA), with V_BE read by a ≥ 16-bit ADC or a 6½-digit DMM over SCPI. At 6–8 temperatures from ambient to ~80 °C (a heater can't go below ambient; add an ice-bath point near 0 °C to widen the range): (1) extract k_B from the PTAT difference ΔV_BE = (kT/q)·ln(I₂/I₁) (≈ 59.5 mV at 300 K for 10:1); (2) fit V_BE(T) at fixed current — including the T·ln T curvature term — and extrapolate to 0 K for V_G0 ≈ 1.17–1.21 V; (3) explain how a Brokaw- or Widlar-style bandgap reference combines these two effects. Check for series-resistance error with a third current. Deliverable: KiCad schematic (or breadboard photo), Python automation, and a short report in `projects/physics/08-transistor-thermometry/`. Success: k_B within 1% of 1.380649×10⁻²³ J/K and V_G0 within 3% of literature, with an error budget naming your dominant systematic (current ratio, series resistance, self-heating, or thermal gradients). *(~14 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What is a Brillouin zone, and why do band gaps open at its boundary?
2. Compare copper's Fermi energy with kT at room temperature. What does the ratio explain about its electronic heat capacity?
3. Why does a silicon diode's forward voltage fall about 2 mV/K at constant current, and where does the ~1.2 V extrapolated intercept come from?
4. Why are Hall sensors made from semiconductors rather than copper?
5. "Electrical resistance comes from electrons bumping into the lattice ions." What does Bloch's theorem say about a perfect lattice, and what actually scatters electrons?
6. Why must a pyroelectric material be polar, and why do IR detectors use materials whose T_c is far above room temperature?
7. A 10 µF, 6.3 V X5R capacitor biased at 5 V measures far less than 10 µF. What's the physics, and why doesn't a C0G capacitor do this?
8. Explain to a smart friend in 3 sentences what Anderson meant by "more is different".
