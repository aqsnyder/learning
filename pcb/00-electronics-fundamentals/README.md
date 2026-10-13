# Electronics Fundamentals

> **Why this section matters:** Before designing PCBs you need to understand the circuits that go on them.

**Prerequisites:** Basic math / physics.

---

## 🎯 Learning Objectives

After this section you can:
- Model a real capacitor as C–ESR–ESL (with DC-bias derating for class-II MLCCs), predict its |Z(f)| and self-resonant frequency, and explain the anti-resonance between parallel values.
- Derive t_r = 2.2RC (10–90 %) and t_r × f_3dB ≈ 0.35 for a single pole, and use them to judge what your scope and probe can actually resolve.
- Build a DC error budget for a high-impedance node — bias current, surface leakage, thermoelectric EMFs, TCR — and explain which terms Kelvin connections and driven guards remove.
- Compute the input-referred noise of an op-amp gain stage (e_n including its 1/f region, i_n × source impedance, 4kTR) by hand and confirm it with SPICE `.noise`.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | *The Art of Electronics* (3rd ed.) | Horowitz & Hill | 2015 | [artofelectronics.net](https://artofelectronics.net/) | The industry bible for circuit design. Its advanced companion, *The Art of Electronics: The x-Chapters*, gets an expanded 2nd edition in 2026 that adds a 100+ page chapter on sensors ([x.artofelectronics.net](https://x.artofelectronics.net/)) |
| 🔑 | Book (Lab Companion) | *Learning the Art of Electronics* | Hayes & Horowitz | — | [artofelectronics.net](https://artofelectronics.net/) | Practical lab companion: a paid Cambridge University Press book, not a free one. A 2nd edition is now available |
| 🔑 | YouTube Channel | EEVblog | Dave Jones | — | [youtube.com/@EEVblog](https://www.youtube.com/@EEVblog) | Electronics tutorials, teardowns, fundamentals |
| | YouTube Channel | GreatScott! | — | — | [youtube.com/@greatscottlab](https://www.youtube.com/@greatscottlab) | Beginner-friendly electronics projects |
| | Course | Khan Academy Electrical Engineering | — | — | [khanacademy.org](https://www.khanacademy.org/science/electrical-engineering) | Free fundamentals |
| | Course | MIT 6.002 Circuits and Electronics (OCW) | Anant Agarwal (with Jeffrey Lang) | 2007 | [ocw.mit.edu](https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/) | Rigorous foundations, with full video lectures |
| | Book | *Practical Electronics for Inventors* | Scherz & Monk | — | — | Accessible reference |
| | Course | TI Precision Labs — Op Amps | Texas Instruments | — | [ti.com](https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html) | Op-amp video curriculum, from offset and bias current through noise, bandwidth, stability, PCB layout and board-level troubleshooting. The most practical bridge from textbook op amps to real analog front ends |
| | Tool | LTspice | Analog Devices | — | [analog.com](https://www.analog.com/en/resources/design-tools-and-calculators/ltspice-simulator.html) | Free SPICE simulator with a large library of vendor models. Simulate the circuits you study before you build them; KiCad also has a built-in ngspice simulator |

---

## Suggested Order

**Core path (🔑):** *The Art of Electronics* + *Learning the Art of Electronics* (read together) → EEVblog

1. **Khan Academy Electrical Engineering** — Build intuition for voltage, current, and basic circuit laws.
2. **The Art of Electronics** (read alongside **Learning the Art of Electronics**) — Work through both together for theory + hands-on labs.
3. **EEVblog** — Supplement reading with video teardowns and tutorials.
4. **GreatScott!** — Follow along with beginner projects to reinforce concepts.
5. **MIT 6.002** — Deepen understanding with a rigorous university-level treatment.
6. **LTspice** — From here on, simulate what you read: bias points, filter responses, op-amp stability.
7. **TI Precision Labs — Op Amps** — Work through offset, noise, bandwidth and stability modules once the AoE op-amp chapters make sense; the PCB-layout and troubleshooting modules connect directly to Sections 04–05.
8. **Practical Electronics for Inventors** — Keep as a desk reference for quick look-ups.

---

## 🛠️ Practice

1. **Rise time vs bandwidth, on your bench** — Derive t_r = 2.2RC and t_r × f_3dB ≈ 0.35 for a single pole. Then probe an STM32 GPIO toggling at each OSPEEDR setting, first with the probe's long ground clip, then with a ground spring. Record the measured t_r, the edge corrected for scope and probe rise times (root-sum-square), and the ringing frequency with the long clip; predict that ringing as 1/(2π√(LC)) using ~1 nH/mm for the clip and the probe's input capacitance. Done when the prediction lands within ~30 % and you can say which speed settings your scope cannot resolve. *(~2 h · MIT 6.002 first-order transients, The Art of Electronics, EEVblog)*
2. **Real capacitors in SPICE** — In LTspice or ngspice, model a 100 nF 0402 X7R, a 10 µF 0805 X5R (at 0 V, and derated to its 3.3 V value from the manufacturer's DC-bias curve), and a 47 µF tantalum as C–ESR–ESL using parameters from the manufacturers' models. Plot |Z| from 1 kHz to 1 GHz for each alone and all three in parallel. Deliverable: plots plus hand-computed self-resonant frequencies and the parallel anti-resonance peak. Done when your hand SRFs match simulation within 5 % and you can explain why the anti-resonance height tracks ESR. *(~2 h · The Art of Electronics, Practical Electronics for Inventors)*
3. **Error budget for a high-impedance node** — A current range develops 1 V full scale across 1 GΩ (1 nA FS) into a CMOS op-amp buffer. At 25 °C and 70 °C, budget: input bias current (a real datasheet's max; extrapolate at ~2× per 10 °C if needed), offset and drift, leakage from an adjacent 5 V trace through a 10¹⁰ Ω (dirty) vs 10¹² Ω (clean) surface path, thermoelectric EMFs at solder joints across a 1 °C gradient, and resistor TCR. Add a guard driven to within ~100 µV of the node and recompute. Repeat for a 10 mV full-scale shunt measurement and note how the dominant term changes. Deliverable: ranked error table plus an LTspice check (leakage as resistors, guard as a buffer). Done when the guard cuts the leakage term by ≥ 10³ and you can name the dominant remaining term in each case. *(~3 h · The Art of Electronics ch. "Precision Circuits", Learning the Art of Electronics)*
4. **Noise budget for a high-gain sensor amplifier** — Take a two-stage, ~70 dB, ~0.5–10 Hz band-pass op-amp front end of the kind used behind a pyroelectric (PIR) sensor — your own circuit or a published reference design. By hand, compute input-referred noise from e_n (including its 1/f region, which dominates below 10 Hz), i_n × source impedance, and 4kTR of every resistor, integrated over the band; then run `.noise` with the real op-amp model. Deliverable: noise table with the dominant term identified. Done when hand and SPICE totals agree within ~25 %. Stretch: swap in a zero-drift op-amp and explain what changes. *(~3 h · The Art of Electronics ch. "Low-Noise Techniques", Learning the Art of Electronics)*

**🏗️ Mini-project — Bench Impedance Analyzer:** Build a Python-scripted rig that measures component impedance: a VNA in 2-port shunt-through (with DC blocks or a bias tee; measure the ferrite bead series-through instead, because shunt-through suits milliohm-to-ohm parts and loses accuracy at a bead's hundreds of ohms), or a signal generator + scope + series-resistor divider driven over PyVISA. Measure |Z(f)| from the instrument's low end (~10–50 kHz) to ≥ 50 MHz for an 0402 100 nF, an 0805 10 µF X5R at 0 V and at 3.3 V bias, a tantalum, a polymer aluminum capacitor, and one ferrite bead; fit C/ESR/ESL (and the bead's R–L–C) to each. Deliverable: notebook, fixture photos, and raw data in `projects/pcb/00-impedance-rig/`. Success: fitted SRFs within 10 % of the manufacturers' models, and measured DC-bias capacitance loss within 15 % of the datasheet curve. You will reuse this rig in Sections 05 and 07. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State the 10–90 % rise time of a single-pole RC in terms of τ, and the rise-time–bandwidth product that follows from it.
2. Above its self-resonant frequency, what sets a capacitor's impedance — and why does its capacitance value barely matter there?
3. Roughly how much capacitance does a 10 µF, 6.3 V, 0603 X5R keep at 5 V DC bias, and where do you get the real number?
4. A 5 V trace sits beside a 1 GΩ high-impedance node across a 10¹⁰ Ω surface leakage path. Estimate the leakage current and compare it with a CMOS op-amp's ~1 pA bias current.
5. What is a driven guard, what potential is it held at, and why does that eliminate leakage rather than merely reduce it?
6. What is the RMS thermal noise of a 1 MΩ resistor over a 10 Hz bandwidth at room temperature?
7. True or false, and why: "A 100 MHz scope with a standard 10× probe on its long ground clip can accurately measure a 1 ns edge."
8. Explain to a smart friend in 3 sentences why a PCB trace is a circuit element and not just a wire.
