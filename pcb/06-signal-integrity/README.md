# Signal Integrity

## Why This Section Matters

As frequencies rise, traces become transmission lines and physics takes over. Signal integrity is the discipline that bridges PCB layout with electromagnetic theory. Understanding impedance, reflections, crosstalk, and return paths is what separates a board that works on the bench from one that works reliably in production. This is where the books on Rick Hartley's reading list become essential.

## Prerequisites

- [Section 04 — PCB Layout Fundamentals](../04-pcb-layout-fundamentals/README.md)
- [Section 05 — Power Distribution and Grounding](../05-power-and-grounding/README.md)
- Optional theory: [Physics Section 03 — Electromagnetism](../../physics/03-electromagnetism/README.md) (Maxwell's equations and field energy, the foundations behind this section and Section 07)

## 🎯 Learning Objectives

After this section you can:
- Decide from rise time and length whether an interconnect is electrically long, and predict reflections and ringing from source/load mismatch with a lattice (bounce) diagram.
- Calculate single-ended and differential impedance with closed-form approximations and a 2D field solver, and explain each sensitivity — dielectric height, width, copper thickness, Dk, solder mask.
- Choose and size terminations (series, parallel, AC, differential) for MCU GPIO/SPI, USB 2.0, and 100BASE-TX, and show with numbers when none is needed.
- Quantify near- and far-end crosstalk against spacing, height, coupled length, and microstrip vs stripline, and turn the result into spacing rules.
- Specify controlled-impedance nets and differential pairs to a fab and in KiCad: width/gap, tolerance, reference layer, and skew or time-domain constraints.

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | On the Rick Hartley recommended reading list |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑⭐ | 📕 Book | Signal and Power Integrity — Simplified (3rd ed., 2018) | Eric Bogatin | [InformIT](https://www.informit.com/store/signal-and-power-integrity-simplified-9780134513416) | THE most approachable signal integrity book. Bogatin explains transmission lines, impedance, and crosstalk with clarity and intuition. Start here. |
| 🔑⭐ | 📕 Book | High-Speed Digital Design: A Handbook of Black Magic (1993) | Howard Johnson, Martin Graham | [sigcon.com](https://sigcon.com/books/bookHSDD.html) | The signal integrity bible. Dense but indispensable — covers everything from rise times to termination strategies. |
| ⭐ | 📕 Book | High-Speed Signal Propagation: Advanced Black Magic (2003) | Howard Johnson, Martin Graham | [sigcon.com](https://sigcon.com/books/bookHSSP.html) | The sequel to *Black Magic*, focused on how signals propagate along real, lossy interconnect. Read it once edge rates and trace lengths make loss matter. |
| ⭐ | 📕 Book | High-Speed Digital System Design: A Handbook of Interconnect Theory and Design Practices (2000) | Stephen H. Hall, Garrett W. Hall, James A. McCall | [Wiley](https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0471360902,descCd-description.html) | Interconnect theory and design practice from three Intel engineers. A compact, practical complement to Johnson & Graham. |
| ⭐ | 📕 Book | Right the First Time, Vols I and II (2003, 2007) | Lee Ritchey | [Speeding Edge](https://speedingedge.com/product-category/handbook/) | Physics-first approach to high-speed PCB design. Practical rules derived from electromagnetic fundamentals. |
| 🔑 | 🎥 Video Series | Robert Feranec — Signal Integrity and High-Speed Design | Robert Feranec | [YouTube](https://www.youtube.com/@RobertFeranec) | DDR routing, differential pairs, impedance control, and real-world high-speed design walkthroughs. |
| | 🎥 YouTube Channel | Dr. EMC | Dr. EMC | [YouTube](https://www.youtube.com/@DrEMC) | Transmission lines, simulation, and EMC theory. Excellent visual explanations of field behavior. (Unverified: no presenter is named, and the only channel titled "Dr. EMC" found in search uses the handle `@DrEMC-sf8rx`. Check it before investing time.) |
| | 🔧 Tool | UltraCAD Calculators | — | [Website](https://www.ultracad.com/calc.htm) | Impedance, trace width, and via calculations. Useful for quick design verification. For trace width vs. current, prefer an IPC-2152-based calculator such as Saturn (Section 05). |
| | 💡 Concept | Controlled Impedance | — | — | What it means, how to specify it to your fab house, and why your stackup determines your trace geometry. |
| | 💡 Concept | Differential Pairs | — | — | Routing rules, coupling, and when to use differential signaling (USB, LVDS, Ethernet, DDR). |
| | 📄 App Note | High-Speed Interface Layout Guidelines (SPRAAR7J, 2023) | Texas Instruments | [PDF](https://www.ti.com/lit/pdf/spraar7) | Concrete differential-pair routing rules for USB 2.0, USB 3.x, PCIe, HDMI, SATA and SGMII: impedance, length matching, vias and reference planes. Keep it open while routing any high-speed interface. |
| | 📄 App Note | Ethernet PHY PCB Design Layout Checklist (SNLA387, 2021) | Lysny Woodahl (Texas Instruments) | [PDF](https://www.ti.com/lit/pdf/snla387) | Checklist for PHY decoupling, clocking and bias-resistor placement, 100 Ω MDI pairs (length limits and matching), and the magnetics/RJ45 region (no metal under the magnetics, ESD placement). Use it in every Ethernet board review. |
| | 💡 Concept | Return Paths and Reference Planes | — | — | Where the current actually flows. A trace is only half the circuit — the return path through the reference plane completes it. |

**Also used here (tracked in their home sections):** LTspice ([Section 00](../00-electronics-fundamentals/README.md)) for Practices 1 and 3; Saturn PCB Toolkit ([Section 05](../05-power-and-grounding/README.md)) and the IPC-2221A §6.4 impedance equations ([Section 08](../08-multi-layer-and-stackup/README.md)) for Practices 2–4.

## Suggested Order

1. **Signal and Power Integrity — Simplified** — Start with Bogatin; read at least the first half for core concepts
2. **Dr. EMC** — Watch transmission line and field visualization videos to build intuition (unverified channel; check it first, otherwise go straight on)
3. **Robert Feranec SI and high-speed design** — See practical application: DDR routing, differential pairs
4. **Controlled impedance** — Understand how to specify impedance to your fab house
5. **Return paths and reference planes** — Internalize where current actually flows (ties back to Rick Hartley's grounding lecture)
6. **Differential pairs** — Learn the routing rules and when differential signaling is required
7. **TI SPRAAR7 + SNLA387** — Apply those rules to the interfaces you actually ship (USB 2.0/3.x, Ethernet MDI and magnetics)
8. **High-Speed Digital Design: Black Magic** — Deep dive into the SI bible; use as reference alongside practical work
9. **High-Speed Digital System Design (Hall, Hall & McCall)** — A second, more compact treatment of interconnect theory and practice
10. **Right the First Time** — Physics-first design rules from Lee Ritchey
11. **High-Speed Signal Propagation: Advanced Black Magic** — Lossy-line behavior once your edges and channels demand it
12. **UltraCAD Calculators** — Verify your impedance and trace geometry calculations

---

## 🛠️ Practice

1. **Bounce diagram vs SPICE** — Model an STM32 GPIO driving 15 cm of 50 Ω microstrip into a 5 pF CMOS load. Get the driver's effective output resistance and edge rate from ST's IBIS model (the `[Pullup]`/`[Pulldown]` V–I tables and `[Ramp]`). Hand-draw the lattice diagram for that source resistance and again with a series resistor chosen to match the line, then simulate both in LTspice with a lossless transmission line. Deliverable: hand vs SPICE overlay. Done when your hand-predicted overshoot and settling agree with SPICE within ~10 % and you can state the maximum unterminated length for this edge rate from Bogatin's rule of thumb. *(~3 h · Bogatin's Signal and Power Integrity — Simplified (reflections), Johnson & Graham's High-Speed Digital Design (terminations))*
2. **Write a 2D field solver** — In ~100 lines of NumPy/SciPy, solve Laplace's equation on a nonuniform grid for a microstrip, compute capacitance with and without the dielectric, and get Z₀ = 1/(c·√(C·C_air)) and ε_eff = C/C_air. Use a fab's published 4-layer stackup (e.g., ~0.2 mm 7628 prepreg). Compare against IPC-2221A's closed form (§6.4.1), the UltraCAD calculators, Saturn PCB Toolkit, KiCad's PCB Calculator, and the fab's own impedance calculator; then add a 15–25 µm solder-mask layer. Deliverable: notebook + comparison table. Done when grid refinement moves Z₀ by < 0.5 %, your solver agrees with Saturn within ~3 %, and you can explain why the IPC formula and mask-free calculators disagree with you by 1–3 Ω. *(~5 h · Bogatin's Signal and Power Integrity — Simplified (impedance), UltraCAD Calculators, Controlled Impedance concept)*
3. **Crosstalk vs spacing** — Extend your solver to two traces (extract the C and L matrices) or use Saturn's crosstalk calculator, and compute the saturated backward-crosstalk coefficient K_b = ¼(C_m/C + L_m/L) for two 50 Ω microstrips at s = h, 2h, 3h, and for the same geometry in stripline. Compare with Johnson & Graham's K/(1+(D/H)²) estimate (mind whether each formula uses edge or center spacing), then simulate one case in SPICE with coupled lines to see NEXT and FEXT waveforms. Deliverable: NEXT-vs-s/h plot (formula, solver, SPICE) and a KiCad spacing rule for clocks near sensitive analog nets. Done when SPICE NEXT matches K_b within ~10 % and you can explain why stripline FEXT is near zero. *(~4 h · Bogatin's Signal and Power Integrity — Simplified (crosstalk), Johnson & Graham's High-Speed Digital Design, Ritchey's Right the First Time)*
4. **Spec the pairs** — First decide, with rise-time-vs-length numbers, whether your USB link (Full-Speed vs High-Speed) and your SPI lines to an Ethernet controller need impedance control at all. Then, for USB 2.0 (90 Ω) and 100BASE-TX MDI (100 Ω) on a 6-layer stackup, compute width/gap on outer and inner layers (Saturn plus your solver), choose loose vs tight coupling, and derive intra-pair skew limits from each interface's rise time. Encode the result as KiCad netclass/diff-pair rules (time-domain constraints if you are on KiCad 10) and a fab-drawing impedance table (layer, reference, target, tolerance, coupon). Deliverable: rules + fab note. *(~3 h · Robert Feranec's SI and high-speed videos, Differential Pairs concept, Controlled Impedance concept)*

**🏗️ Mini-project — SI Test-Coupon Board:** Design a small 4-layer board with SMA edge launches carrying: 50 Ω microstrip and stripline in two lengths (≥ 15 cm, so a 1.5–3 GHz VNA can resolve them), 90 Ω and 100 Ω pairs, a line crossing a reference-plane gap, a layer change with and without adjacent stitching vias, a ~30 mm open stub (its quarter-wave notch near 1.3 GHz falls inside a NanoVNA's range; a 10 mm stub's would sit near 4 GHz, out of range), and coupled lines at s = h and s = 3h. Predict every structure (your solver + SPICE), then measure with a NanoVNA-class VNA (S11/S21, converted to TDR with scikit-rf's time-domain tools) and your scope. Deliverable: KiCad project, prediction notebook, and a measurement report with predicted-vs-measured overlays in `projects/pcb/06-si-coupons/`. Success: TDR-derived Z₀ within ±10 % of prediction for every line, and the plane-gap and missing-stitch structures measurably worse than their controls. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State a rule for when a trace must be treated as a transmission line, in terms of rise time and propagation delay.
2. What is the signal speed in FR-4 stripline in in/ns and ps/in, and what sets it?
3. Compute the reflection coefficient for a 50 Ω line into 75 Ω and into an open; sketch what a 5 pF load does to a fast edge.
4. Why does solder mask lower microstrip impedance, and by roughly how much?
5. Estimate the bandwidth of a 1 ns (10–90 %) edge two ways: 0.35/t_r and Johnson's knee frequency 0.5/t_r.
6. Misconception probe: "90° trace corners cause significant reflections and EMI at USB 2.0 speeds." What does the evidence say?
7. Why is far-end crosstalk near zero in stripline but not in microstrip?
8. Explain to a smart friend in 3 sentences why a "50 Ω trace" has nothing to do with its DC resistance.
