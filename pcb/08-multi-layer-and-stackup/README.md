# Multi-Layer Design and Stackup

## Why This Section Matters

Layer stackup determines signal integrity, EMC performance, and manufacturability. A well-designed stackup is the foundation of every high-performance PCB — get it wrong and no amount of careful routing will save you.

**Prerequisites:** Sections 05–07.

---

## 🎯 Learning Objectives

After this section you can:
- Evaluate 4-, 6-, and 8-layer stackups against Hartley's and Ritchey's rules — every signal layer next to a solid reference, closely coupled power/ground pairs, symmetric construction, return-path continuity at layer changes — and choose one with written reasons.
- Turn a fab's published stackup (cores, prepregs, glass styles, Dk per construction, copper weights) into impedance-controlled geometries, knowing which parameters you control and which the fab adjusts.
- Calculate plane-pair capacitance and cavity resonances, and explain how dielectric thickness changes PDN impedance, emissions, and crosstalk.
- Judge when HDI (blind, buried, and microvias; via-in-pad) pays for itself, using escape geometry and real quotes.
- Write a stackup specification that a fab can build without engineering questions.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Video | The Extreme Importance of PC Board Stack-Up (AltiumLive, 2018) | Rick Hartley | [Altium](https://resources.altium.com/p/the-extreme-importance-of-pc-board-stack-up-rick-hartley) | Hartley's talk, with downloadable slides, on why the stackup sets SI and EMC performance. His other stackup talks: [search YouTube](https://www.youtube.com/results?search_query=rick+hartley+stackup) |
| 🔑 | Video Series | Robert Feranec multi-layer PCB design | Robert Feranec | [YouTube](https://www.youtube.com/@RobertFeranec) | Complex multi-layer layout techniques |
| ⭐ | Book | Right the First Time | Lee Ritchey | [Speeding Edge](https://speedingedge.com/product-category/handbook/) | Detailed stackup engineering (Rick's reading list) |
| 🔑 | Tool | Saturn PCB Toolkit stackup calculator | — | [Link](https://saturnpcb.com/saturn-pcb-toolkit/) | Impedance and stackup calculation tool |
| | Concept | 4-layer vs 6-layer vs 8-layer tradeoffs | — | — | Understanding when to add layers and the cost/performance implications |
| | Concept | Impedance-controlled stackups | — | — | Working with your fab house to achieve target impedances |
| | Concept | Blind and buried vias | — | — | When they're worth the cost |
| | Reference | IPC-2221 stackup guidelines | IPC | [Included](../documents/IPC-2221A(L).pdf) | Generic design standard, not a stackup-design guide. Section 4 covers laminates, prepreg and dielectric spacing, and §6.4 gives the classic closed-form microstrip/stripline impedance equations. The included copy is Rev A (2003; current is IPC-2221C, 2023). Get real stackups and impedance numbers from your fab or a field solver |

**Also used here (tracked in their home sections):** openEMS ([Section 10](../10-advanced-topics/README.md)) for Practice 3, and your Section 06 field solver for Practice 2.

---

## Suggested Order

**Core path (🔑):** Hartley, *The Extreme Importance of PC Board Stack-Up* → Saturn PCB Toolkit → Feranec multi-layer series

1. **Hartley — The Extreme Importance of PC Board Stack-Up** — Understand why stackup is the single most important design decision.
2. **Saturn PCB Toolkit** — Install and experiment with impedance calculations for different stackups.
3. **4-layer vs 6-layer vs 8-layer tradeoffs** — Learn when each layer count is appropriate.
4. **Impedance-controlled stackups** — Understand how to work with your fab house on controlled impedance.
5. **Robert Feranec multi-layer series** — Watch complex multi-layer designs come together.
6. **Right the First Time** — Deep-dive into stackup engineering principles.
7. **Blind and buried vias** — Learn the advanced via types and their manufacturing implications.
8. **IPC-2221** — Reference §4 (materials, dielectric spacing) and §6.4 (impedance equations) for background; the fab's stackup table is the source of truth.

---

## 🛠️ Practice

1. **Stackup tournament** — For a 6-layer board with an STM32U5, USB-C, Ethernet, a buck plus LDOs, and a precision analog section, score at least four arrangements (include S-G-S-S-P-S and S-G-S-P-G-S plus two of your own) on: each signal layer's adjacency to a solid reference, broadside coupling between adjacent signal layers, plane-pair spacing, the return path at each likely layer change (GND↔GND needs stitching vias; GND↔PWR needs capacitors), routing capacity, symmetry/warp risk, and cost. Deliverable: scoring matrix + choice + a one-paragraph justification. Done when your choice matches the reasoning in Hartley's stackup lectures and Ritchey's stackup chapters, or you can defend the deviation. *(~3 h · Rick Hartley's stackup design lectures, Ritchey's Right the First Time, 4- vs 6- vs 8-layer tradeoffs concept)*
2. **Fab stackup → geometry table** — Take one of JLCPCB's (or your fab's) published 6-layer, 1.6 mm impedance stackups and compute 50 Ω single-ended, 90 Ω differential, and 100 Ω differential geometries on L1, L3/L4, and L6 with Saturn PCB Toolkit, the fab's own calculator, and your Section 06 field solver. Enter the stackup in KiCad's physical-stackup manager and the geometries in netclasses. Deliverable: geometry table + template update. Done when the three tools agree within ~5 %, and where they don't you have traced the gap to pressed-prepreg thickness, Dk by glass style, or solder mask. *(~3 h · Saturn PCB Toolkit stackup calculator, Impedance-controlled stackups concept, Robert Feranec's multi-layer design videos)*
3. **Plane cavity in openEMS** — Compute the capacitance and first cavity resonances, f_mn = c/(2√εᵣ) · √((m/a)² + (n/b)²), of an 80 × 60 mm power/ground pair at 0.1 mm and 0.5 mm spacing. Then simulate the bare plane pair in openEMS with a lumped port near one corner and extract Z₁₁(f). Deliverable: hand vs openEMS resonance table + plot, and two sentences on what it means for your decoupling and stitching. Done when the first resonance matches the formula within ~5 %. *(~5 h · Rick Hartley's stackup design lectures, Ritchey's Right the First Time)*
4. **HDI: worth it?** — For a dense part (a 0.5 mm-pitch BGA or a 0.4 mm-pitch WLCSP), sketch whether through-hole vias at your fab's minimums can escape it; if not, plan (a) via-in-pad plated over (VIPPO) on a through-via stackup and (b) a 1+N+1 laser-microvia stackup. Get quotes from two fabs for plain 6-layer, 6-layer + VIPPO, and 1+4+1 HDI at 10 and 100 pieces. Deliverable: escape sketch + cost table + decision. *(~3 h · Blind and Buried Vias concept, Robert Feranec's multi-layer design videos)*

**🏗️ Mini-project — Stackup Spec Package:** For your next 6-layer board, produce: (1) a stackup drawing (layer order and function, materials, thicknesses, copper weights) agreed with a specific fab — send it and get their engineering confirmation or adjusted stackup; (2) an impedance table (50 Ω single-ended, 90/100 Ω differential per layer, ±10 %) computed by you and by the fab; (3) the KiCad physical stackup, netclasses, and diff-pair rules updated in your template; (4) a coupon plan — the fab's impedance coupon plus your own TDR-able coupon in the panel rail; (5) a one-page layer-assignment memo by net class (USB, Ethernet MDI, SPI/clocks, precision analog, switcher) showing how each net's return current moves at every planned layer change. Deliverable: `projects/pcb/08-stackup/`. Success: the fab confirms with zero open EQs and its impedance numbers fall within ±5 % of yours; if built, coupon TDR lands within tolerance. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Hartley's core stackup rules: what must every signal layer have, and what should the power and ground planes be to each other?
2. In a standard 1.6 mm 4-layer board (thin prepregs outside, thick core inside), why is L2 GND / L3 PWR a poor plane pair, and where do L4 signals' return currents flow?
3. Core vs prepreg: which thickness does the fab hold, and which moves with copper density and resin flow?
4. Compute the first cavity resonance of a 100 × 100 mm plane pair with εᵣ = 4.2.
5. A signal changes from L1 (referenced to L2 GND) to L6 (referenced to L5 PWR). What must you provide for its return current, and why?
6. Misconception probe: "A power plane is as good a reference as a ground plane." When is that true, and when is it false?
7. Blind, buried, and microvias: define each and say what it does to cost and lamination cycles.
8. Explain to a smart friend in 3 sentences why the stackup is decided before routing starts.
