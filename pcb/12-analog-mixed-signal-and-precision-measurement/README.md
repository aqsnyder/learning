# Analog, Mixed-Signal and Precision Measurement

## Why This Section Matters

Precision instruments, source/measure channels and high-gain sensor front ends fail in ways general PCB practice never mentions:

- picoamps of leakage across a slightly dirty board
- microvolts of thermoelectric EMF at a solder joint
- an ADC that loses two bits when the USB or Ethernet traffic starts
- a force amplifier that oscillates as soon as a long cable is attached
- an AC-coupled amplifier that stays blind for seconds after a single overload

This section treats the signal chain as one system: source or sensor, front end, ADC, reference, ground and the board itself. It teaches you to budget it, design it and, above all, measure it. Sections 00, 03 and 04 introduce the pieces (error and noise budgets, precision part selection, Kelvin and guard layout); this section joins them into channels you can characterize against a spec.

**Recommended position:** take this section after Section 05. It is numbered 12 only so that existing sections keep their numbers.

## Prerequisites

- [Section 00 — Electronics Fundamentals](../00-electronics-fundamentals/README.md): op amps, noise, and the high-impedance error and noise budgets (Practice 3–4)
- [Section 03 — Component Selection and Sourcing](../03-component-selection/README.md): precision part selection, MLCC derating
- [Section 04 — PCB Layout Fundamentals](../04-pcb-layout-fundamentals/README.md): Kelvin and guard layout, the precision-channel layout block
- [Section 05 — Power Distribution and Grounding](../05-power-and-grounding/README.md): return paths, mixed-signal grounding (MT-031), Morrison's *Grounding and Shielding*
- Optional theory: [Physics Section 12 — Measurement, Noise and Sensor Physics](../../physics/12-measurement-noise-and-sensor-physics/README.md) (the noise and sensor physics under this section's budgets)

## 🎯 Learning Objectives

After this section you can:
- Build an end-to-end error and noise budget for a precision measurement chain against a stated accuracy spec. Cover shunt or sensor, amplifier, ADC, reference, board leakage and thermal EMFs; separate what calibration removes from what it cannot; and name the dominant term on each range.
- Design an ADC drive and reference circuit (driver stability, the RC "charge bucket", reference buffering and decoupling) that settles to within ½ LSB, then predict and measure SNR and ENOB with a windowed FFT.
- Design a force/sense (SMU-style) output stage that stays stable into capacitive and cabled loads, with compliance limits and range changes that do not glitch the device under test.
- Design high-gain, AC-coupled sensor front ends for dynamic range as well as noise: predict overload and saturation recovery, and shorten re-arm time without degrading the noise floor.
- Measure leakage, input bias current, 0.1–10 Hz noise and thermoelectric offsets on a real board with guarded, 4-wire setups, and attribute each observed error to a mechanism.

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | On the Rick Hartley recommended reading list |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| | 💡 Concept | Precision analog & mixed-signal layout | — | — | Guarding and leakage control, Kelvin (force/sense) routing, thermoelectric and passive-component errors, ADC/reference/driver layout, and partitioning without splitting the ground plane. Most PCB books skip this, so it needs its own study. |
| 🔑 | 📕 Book (Free) | *Op Amp Applications Handbook* (2005), especially Section 7 "Hardware and Housekeeping Techniques" | Walt Jung (ed.), Analog Devices | [analog.com](https://www.analog.com/en/resources/technical-books/op-amp-applications-handbook.html) | Free ADI handbook, downloadable by section. Section 7 covers passive-component errors (dielectric absorption, tempco, thermocouple effects), Kelvin feedback, return currents and ground planes, AGND/DGND, static leakage and guarding, EMI/RFI and thermal. It is the precision-layout chapter general PCB books lack. |
| 🔑 | 📕 Book (Free) | *Low Level Measurements Handbook* (7th ed., 2014) | Keithley (Tektronix) | [PDF](https://download.tek.com/document/LowLevelHandbook_7Ed.pdf) | The reference on precision DC current, voltage and resistance measurement: guarding, leakage, noise, 4-wire (Kelvin) methods, and source-measure unit (SMU) architecture. Essential before designing source/measure or electrometer-grade front ends. |
| | 📕 Book (Free chapters) | *Basic Linear Design* (2007) / *Linear Circuit Design Handbook* (2008) | Hank Zumbahlen (ed.), Analog Devices | [analog.com](https://www.analog.com/en/resources/technical-books/linear-circuit-design-handbook.html) | ADI's broad linear-design reference. The free *Basic Linear Design* chapters on this page include Chapter 12, "Printed Circuit Board (PCB) Design Issues". Use it as the second reference when the Op Amp Applications Handbook is too terse. |
| | 🎓 Course | TI Precision Labs — ADCs | Texas Instruments | [ti.com](https://www.ti.com/video/series/precision-labs/ti-precision-labs-analog-to-digital-converters-adcs.html) | Video curriculum covering SAR vs delta-sigma, ADC drive topologies, AC/DC specifications, ADC noise and error sources, SAR input-driver design, driving the reference input, EOS protection, PCB design for good EMC, and measuring RTDs with precision ADCs. |
| | 🎓 Course | Mixed-Signal Hardware Design with KiCad (2022) | Philip Salmony (Phil's Lab) | [FEDEVEL](https://fedevel.com/courses/mixed-signal-hardware-design-with-kicad) | Paid course built around one board: op-amp/filter/ADC-DAC front end, USB-C, SWD, switching and analog supplies, LTspice simulation, and a four-layer mixed-signal KiCad 6 layout with controlled impedance and ESD protection. |
| | 💡 Concept | Signal-chain error budgets and calibration | — | — | Budget every term (offset, gain, nonlinearity, drift, noise, leakage, thermal EMF, reference) over temperature and time. Know which terms a two-point calibration removes and which it cannot (drift, INL, hysteresis, self-heating). |
| | 💡 Concept | ADC drive, references and mixed-signal partitioning | — | — | The driver and its RC filter must settle the sampling capacitor's charge kick within the acquisition time. The reference input draws dynamic current and needs a low-impedance source. Digital return currents must stay out of the analog and reference return paths (MT-031, Section 05). |
| | 💡 Concept | Source-measure (force/sense) architecture | — | — | A force amplifier with Kelvin sense at the DUT, current measured across range resistors or with a transimpedance stage, compliance limits, and glitch-free range changes. Loop stability depends on the load, so capacitive DUTs and cables matter. |
| | 💡 Concept | High-gain sensor front ends: dynamic range and overload recovery | — | — | AC coupling, gain distribution and filter time constants set how long one large event blinds the channel, and dielectric absorption in the coupling capacitors stretches the tail. Design for recovery as deliberately as for noise. |

**Also used here (tracked in their home sections):** TI Precision Labs — Op Amps and LTspice ([Section 00](../00-electronics-fundamentals/README.md)); your STM32 family's hardware getting-started note, for VDDA/VREF+ ([Section 02](../02-schematic-capture/README.md)); MT-031 and ⭐ Morrison, *Grounding and Shielding* ([Section 05](../05-power-and-grounding/README.md)); ThunderScope, an open instrument front end to study, and J-SMU, an open DIY source-measure unit with published schematics and KiCad files ([Section 11](../11-reference-projects/README.md)); PyVISA for instrument control in the mini-project ([Software Section 13](../../software/13-hil-testing-and-lab-automation/README.md)).

## Suggested Order

**Core path (🔑):** *Op Amp Applications Handbook* Section 7 → Keithley *Low Level Measurements Handbook*

1. **Precision analog & mixed-signal layout + *Op Amp Applications Handbook* Section 7** — Read the hardware-and-housekeeping chapter end to end (passive-component errors, Kelvin feedback, grounding, leakage and guarding). It is the map for everything below.
2. **Signal-chain error budgets and calibration** — Extend your Section 00 high-impedance budget to a full calibrated chain (Practice 1).
3. ***Low Level Measurements Handbook*** — Read the guarding, leakage, noise and 4-wire material, then the SMU material before designing any source/measure channel.
4. **TI Precision Labs — ADCs** — Work through SAR vs delta-sigma, ADC noise, SAR input-driver design and driving the reference input; re-read MT-031 (Section 05) for converter grounding.
5. **ADC drive, references and mixed-signal partitioning** — Apply it in Practice 2–3.
6. **Source-measure (force/sense) architecture** — Skim J-SMU's schematics (Section 11) to see a whole instrument, then Practice 4.
7. **High-gain sensor front ends** — Then Practice 5.
8. ***Basic Linear Design* / *Linear Circuit Design Handbook*** — Use Chapter 12 and the amplifier and converter chapters as the second reference.
9. **Mixed-Signal Hardware Design with KiCad (Phil's Lab)** — See a whole mixed-signal board designed and laid out before the mini-project.
10. **Morrison, *Grounding and Shielding* (Section 05)** — Guards, shields and cable grounding for instrument inputs.

---

## 🛠️ Practice

1. **Full-chain error budget with calibration** — Specify a current-measurement channel: ranges of 10 µA, 1 mA and 100 mA full scale, with an accuracy target of ±(0.05 % of reading + 0.02 % of range) over 18–28 °C for one year after a two-point calibration.
   - For each range, pick from real datasheets a shunt (value, TCR, power), an instrumentation or difference amplifier, and a 16- or 24-bit ADC with reference.
   - Budget at max specs: shunt tolerance, TCR and self-heating at full scale; amplifier offset, drift, gain error and CMRR at the worst common-mode voltage; ADC INL and noise at your data rate; reference initial accuracy, drift and long-term stability; thermal EMF at the shunt's Kelvin taps; and leakage on the 10 µA range.
   - Model the calibration (offset and gain at 25 °C) and recompute.

   Deliverable: a notebook that prints each range's budget before and after calibration, with the dominant term flagged. Done when every range meets the target after calibration (or you have documented the part change that would make it), and you can name the errors calibration cannot touch. *(~4 h · Op Amp Applications Handbook Section 7, Low Level Measurements Handbook, TI Precision Labs — ADCs (AC and DC specifications, error sources))*
2. **SAR driver and charge bucket, settled to ½ LSB** — Pick a 16-bit, ~1 MSPS SAR ADC whose datasheet gives an input model (sampling capacitance and switch resistance), plus a driver op amp.
   - Following TI Precision Labs' SAR input-driver modules, size the RC between driver and ADC: C large relative to the sampling capacitor so the kick is small, R large enough to keep the driver stable, and τ short enough to settle.
   - Simulate in LTspice with the sampling switch modeled as a switched capacitor clocked at the conversion rate. Check the driver's phase margin with the RC load, and the settling error at the end of acquisition for a full-scale step.
   - Size the reference buffer and decoupling from the datasheet's reference-current figure.

   Deliverable: LTspice files + a one-page design note. Done when settling error at the end of acquisition is below ½ LSB (≈ 7.6 ppm of full scale at 16 bits) and phase margin is ≥ 45°. *(~4 h · TI Precision Labs — ADCs (SAR ADC input driver design, driving the reference input), LTspice (Section 00))*
3. **ENOB under fire** — On an STM32U5-class board (and on an external SAR or delta-sigma ADC if your board has one), capture 2¹⁴–2¹⁶ samples of (a) a shorted input and (b) a low-distortion sine near −1 dBFS.
   - In Python, compute noise-only ENOB from (a). From a Blackman-Harris-windowed FFT of (b), compute SNR, SINAD, SFDR and ENOB.
   - Repeat while switching on one noisy subsystem at a time: USB traffic, an Ethernet link under load, the buck in PFM vs forced PWM (if your regulator allows it), GPIO activity.
   - Repeat with VREF+ decoupled as the datasheet recommends vs a single small capacitor, then apply 16× and 256× oversampling.

   Deliverable: notebook with FFTs and an ENOB-per-condition table. Done when the quiet-case noise ENOB is within ~0.5 bit of the datasheet's typical, and every condition that costs ≥ 3 dB of SNR has a named coupling mechanism (shared return path, reference ripple, supply ripple, clock spur) that you confirmed with a change. *(~5 h · TI Precision Labs — ADCs (ADC noise), MT-031 (Section 05), your STM32 family's hardware getting-started note (Section 02))*
4. **Force/sense loop into real loads** — In LTspice, build an SMU-style channel:
   - A power op amp (or op amp plus complementary output stage) forces voltage through range resistors of 10 kΩ, 100 Ω and 1 Ω (100 µA, 10 mA and 1 A full scale at 1 V drop). A remote-sense buffer closes the loop at the DUT.
   - The load is 1 nF, 100 nF or 10 µF at the end of 2 m of cable, modeled with the per-metre L and C from a real cable datasheet.
   - Measure loop gain and phase margin with an injection probe (Middlebrook or Tian method) for every load × range combination.
   - Add compensation until stable: an isolation resistor inside the sense loop with a feedback capacitor, or per-range switched compensation.
   - Simulate a 10 mA → 100 µA range change with make-before-break switching while the DUT draws 50 µA.
   - Compare your compensation and range-switching scheme with J-SMU's published schematics (Section 11): note one choice you would copy and one you would not, with the reason.

   Deliverable: LTspice files + phase-margin matrix + range-change transient + the J-SMU comparison note. Done when phase margin is ≥ 45° in every cell and the range-change glitch at the DUT stays below 1 % of the forced voltage. *(~5.5 h · Low Level Measurements Handbook (SMU architecture), TI Precision Labs — Op Amps (stability) and LTspice (Section 00), J-SMU (Section 11))*
5. **Overload recovery in a high-gain AC-coupled front end** — Take the ~70 dB, ~0.5–10 Hz two-stage band-pass from Section 00 Practice 4, or your own sensor amplifier.
   - In LTspice, rail both stages for 200 ms, then measure the time until the output is back inside the noise floor and a second, small event is detectable. Identify which coupling capacitor and time constant dominate.
   - Compare three fixes: (a) redistribute gain (less analog gain, more ADC resolution or oversampling, digital filtering); (b) a DC-servo integrator loop instead of a large coupling capacitor; (c) a fast-settle switch or MCU-driven blanking that discharges the coupling node after an overload.
   - Add dielectric absorption to the coupling-capacitor model (a second series R–C branch in parallel) for X7R vs C0G or film, and look at the tail it creates.

   Deliverable: a one-page memo comparing recovery time, noise floor and parts count. Done when one fix re-arms the channel in < 0.5 s after a rail-to-rail overload while raising integrated noise by < 10 %. *(~4 h · Op Amp Applications Handbook Section 7 (dielectric absorption), TI Precision Labs — Op Amps (input and output limitations, noise) and LTspice (Section 00))*

**🏗️ Mini-project — Precision Current-Measurement Channel:** Build the channel from Practice 1 on a 4-layer board, or populate the precision-channel block from Section 04.
- **Board:** Kelvin shunts per range, a guarded path for the lowest range, the ADC driver and reference from Practice 2, an STM32U5 controller with USB, and a guard-ring leakage test structure.
- **Automation:** Python (PyVISA if you have bench instruments; see Software Section 13) steps currents with a source or SMU against a precision DMM as reference, logs readings and board temperature, and fits gain and offset.
- **Characterization:**
  - accuracy on every range before and after two-point calibration, against the Practice 1 budget
  - 0.1–10 Hz noise per range
  - leakage on the lowest range with the guard driven, grounded and disabled, plus a deliberately flux-contaminated coupon
  - tempco from a 20–40 °C sweep in an enclosure with a heater

Deliverable: KiCad project, firmware, logging scripts, a characterization notebook and a one-page datasheet-style spec sheet in `projects/pcb/12-precision-channel/`. Success: post-calibration error inside your Practice 1 budget on every range, measured noise within ±30 % of prediction, and guarded leakage at least 10× below unguarded. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What is the difference between a guard, a shield and a ground at a measurement input, and what potential is each held at?
2. In a two-point-calibrated measurement chain, which error terms disappear and which remain? Name three that remain.
3. Why does a SAR ADC need a capacitor right at its input, and what limits how large that capacitor and its series resistor can be?
4. Roughly how large is the thermoelectric EMF of a copper-to-solder junction per °C, and how does it compare with one LSB of a 24-bit ADC on a 5 V span?
5. Why can a force amplifier that is stable on the bench oscillate once you add a long cable or a large capacitive DUT? Give two compensation remedies.
6. Misconception probe: "Averaging 256 samples always buys four extra bits of accuracy." When is it true for resolution, and why is it never true for accuracy?
7. Why can a high-gain AC-coupled amplifier stay blind for seconds after one large event, and which capacitor property makes the tail longer than the RC time constant predicts?
8. Explain to a smart friend in 3 sentences why precision measurement is mostly about controlling where unwanted currents and voltages enter, not about the ADC's bit count.
