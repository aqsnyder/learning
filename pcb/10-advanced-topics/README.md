# Advanced Topics

## Why This Section Matters

Taking your designs to the next level with complex routing, thermal management, simulation, and flex circuits. These topics separate competent designers from experts. Precision analog and mixed-signal design has its own section, [Section 12](../12-analog-mixed-signal-and-precision-measurement/README.md), and bring-up and production test are in [Section 13](../13-bring-up-test-and-debug/README.md).

**Prerequisites:** All previous sections.

---

## 🎯 Learning Objectives

After this section you can:
- Plan BGA fanout and escape (dog-bone vs via-in-pad, channels between balls, rows escaped per layer) and estimate the required layer count from pitch, ball count, and fab rules.
- Predict component temperatures — using θJA, θJC, and ψJT correctly and modeling copper spreading and thermal vias — and validate the prediction by measurement.
- Simulate DC current density and IR drop in copper with an open-source FEM flow (KiCad → Salome → ElmerFEM) and validate it with a Kelvin measurement.
- Design and tune a 50 Ω RF feed and matching network for a 2.4 GHz antenna (grounded coplanar waveguide, via fencing, keep-outs) using a VNA and the Smith chart.
- Apply flex design rules (IPC-2223): bend radius, neutral axis, copper type, coverlay, stiffeners, and no vias in bend areas.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Video Series | Robert Feranec BGA routing and escape | Robert Feranec | [YouTube](https://www.youtube.com/@RobertFeranec) | BGA fanout strategies |
| | Course | Tech Explorations KiCad Advanced (BGA, SI, High-Speed) | Tech Explorations | — | Advanced KiCad techniques. (Unverified: no matching course was found during review; verify it exists before paying.) |
| | Video Series | Phil's Lab advanced designs (STM32, FPGA boards) | Phil's Lab | [YouTube](https://www.youtube.com/@PhilsLab) | Real complex project walkthroughs |
| | Concept | BGA escape routing and via-in-pad | — | — | Advanced package routing strategies |
| | Concept | Thermal management | — | — | Thermal vias, copper pours, heatsink integration |
| | Concept | Flex and rigid-flex PCB design (IPC-2223) | — | — | Flexible circuit design and manufacturing |
| | Concept | RF PCB design basics | — | — | Microstrip, stripline, antenna matching |
| | Tool | Open Source Thermal Simulation | — | [Link](https://jrainimo.com/build/2024/11/oss-thermal-simulation-of-pcbs/) | Walkthrough of an open-source KiCad → Salome → ElmerFEM flow that simulates DC current density and Joule heating in PCB copper (IR drop and hot spots). It is not part-level thermal modelling; use AN-2020 and the Thermal management concept for that. |
| | App Note | AN-2020: Thermal Design By Insight, Not Hindsight (2013) | Texas Instruments | [PDF](https://www.ti.com/lit/pdf/snva419) | Practical PCB thermal design for power ICs: interpreting the package thermal metrics, copper spreading and thermal vias, and estimating junction temperature before layout is frozen |
| | Tool | openEMS + gerber2ems | Thorsten Liebig (openEMS); Antmicro (gerber2ems) | [openems.de](https://www.openems.de/) · [gerber2ems](https://github.com/antmicro/gerber2ems) | Free FDTD field solver. Antmicro's gerber2ems drives it from Gerbers, drill files and a stackup description to extract S-parameters and impedance of real PCB traces, making open-source SI verification of KiCad boards practical |
| | Tool | KiCad IPC API + kicad-python | KiCad Project | [Docs](https://docs.kicad.org/kicad-python/) | KiCad's new (9.0+) scripting and plugin API. The old SWIG `pcbnew` Python bindings are deprecated and slated for removal in KiCad 11, so write new scripts and plugins against this |

**Also used here (tracked in their home sections):** Saturn PCB Toolkit's via calculator ([Section 05](../05-power-and-grounding/README.md)) for Practice 1.

---

## Suggested Order

1. **BGA escape routing and via-in-pad** — Understand the concept before watching the tutorials.
2. **Robert Feranec BGA routing series** — Watch expert BGA fanout strategies in action.
3. **Thermal management** — Learn thermal vias, copper pours, and heatsink integration techniques, with TI AN-2020 as the worked reference.
4. **Open Source Thermal Simulation** — Simulate DC current density and Joule heating in your own high-current copper (KiCad → Salome → ElmerFEM).
5. **Phil's Lab advanced designs** — Study complete complex project walkthroughs (STM32, FPGA).
6. **openEMS + gerber2ems** — Check a critical trace or transition with a field solver instead of trusting a closed-form calculator.
7. **Tech Explorations KiCad Advanced** — Deepen your EDA tool skills for advanced designs (unverified course; confirm it exists first).
8. **KiCad IPC API + kicad-python** — Automate repetitive editor tasks with the supported API.
9. **RF PCB design basics** — Explore microstrip, stripline, and antenna matching fundamentals.
10. **Flex and rigid-flex PCB design** — Learn when and how to use flexible circuits.

Precision analog and mixed-signal layout (ADI's *Op Amp Applications Handbook*, the Keithley *Low Level Measurements Handbook*, Phil's Lab's mixed-signal course): see [Section 12](../12-analog-mixed-signal-and-precision-measurement/README.md).

---

## 🛠️ Practice

1. **Junction temperature: estimate, then measure** — Pick a hot part on one of your boards (an LDO dropping 5 V → 3.3 V at 300 mA, or a buck IC). Estimate T_J three ways: (a) datasheet θJA — and say why it describes a JEDEC test board, not yours; (b) ψJT plus a measured case temperature; (c) a spreading model of your actual copper area and thermal vias (one 0.3 mm via through 1.6 mm with a 25 µm wall is on the order of 200 K/W — confirm with Saturn PCB Toolkit's via calculator). Measure with a thermocouple or thermal camera at a known dissipation. Deliverable: three-way comparison table. Done when your best model lands within ~15 % of the measured temperature rise. *(~3 h · Thermal management concept)*
2. **BGA escape plan** — For a 0.8 mm-pitch, 256-ball FPGA-class BGA and a 0.5 mm-pitch MCU-class BGA, work out with your fab's rules (trace/space, via drill and pad, via-in-pad availability) how many rows escape per layer with dog-bone fanout vs via-in-pad, and the resulting signal-layer count. Fan out one quadrant of each in KiCad. Deliverable: quadrant layouts + layer-count estimate + required fab features. Done when both are DRC-clean against real fab rules and your method matches the approach in Feranec's BGA routing videos. *(~3 h · Robert Feranec's BGA routing and escape videos, BGA escape routing and via-in-pad concept)*
3. **Flex tail** — Design a 2-layer polyimide flex tail for a sensor or display interconnect: rolled-annealed copper, a minimum bend radius computed from IPC-2223's bend-ratio guidance for your construction and for static vs dynamic use, traces staggered between layers through the bend, hatched ground, teardrops, a stiffener under the connector, and no vias in the bend zone. Deliverable: KiCad flex design + fab notes. Done when a flex fab's DFM review accepts it without EQs. *(~2.5 h · Flex and rigid-flex PCB design (IPC-2223) concept)*
4. **Copper current density with ElmerFEM, checked 4-wire** — Reproduce the Open Source Thermal Simulation workflow (KiCad XAO export → Salome mesh → ElmerFEM static current conduction with Joule heating → ParaView) on a real high-current path of yours — e.g., USB-C VBUS at 3 A through connector pads, a pour neck, and a via group. Find the current-density hot spots, then measure the path's voltage drop 4-wire at the same current and compare it with the simulated drop. Deliverable: heat maps + measured vs simulated mV. Done when they agree within ~15 % (copper-thickness tolerance) and you have fixed the worst neck or via group. *(~5 h · Open Source Thermal Simulation, Thermal management concept)*
5. **2.4 GHz feed and match** — On your 4-layer stackup, design a 50 Ω grounded-coplanar-waveguide feed to a chip antenna with a π matching network, a ground keep-out per the antenna datasheet, and a via fence at ≤ λ/20 spacing (compute λ from your line's ε_eff). Build it (or rework an existing antenna board), measure S11 with a VNA that covers 2.5 GHz, and tune the match on the Smith chart with scikit-rf. Deliverable: design notes + before/after S11. Done when |S11| < −10 dB across 2.400–2.4835 GHz. *(~6 h · RF PCB design basics concept)*

**🏗️ Mini-project — Thermal Characterization Board:** Design a small 4-layer board with four identical heater sites (a power resistor, or a MOSFET run in its linear region, in a common package such as SOT-223 or DFN) that differ only in copper area and thermal-via count (0/4/9/16), each with a local temperature sensor; drive and log them from an STM32 or USB DAQ with Python. Predict each site's thermal resistance with your Exercise 1 model and an FEM tool (ElmerFEM's heat solver), then measure in still air. Safety: power the sites from a current-limited supply, drive MOSFET sites with closed-loop current control (a fixed gate voltage in the linear region can run away thermally), add a firmware over-temperature cut-off (e.g. 125 °C), and don't leave the board running unattended; the 0-via site gets hot fastest. Deliverable: KiCad project, logging script, and notebook in `projects/pcb/10-thermal/`. Success: models within ±15 % of measurement on at least three of four sites, and you finish with your own °C/W-vs-copper-area and per-via curves for your stackup. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What determines how many routing layers a BGA needs to escape?
2. Why is a datasheet's θJA not your board's θJA, and when should you use ψJT instead?
3. Estimate the thermal resistance of one 0.3 mm-drill plated via through 1.6 mm FR-4 with a 25 µm copper wall.
4. Why must via-in-pad be filled and capped for SMT pads?
5. Misconception probe: "Doubling the copper pour area halves the part's temperature rise."
6. For a 2.4 GHz grounded-CPW feed on FR-4 (ε_eff ≈ 3.3), what is λ/20, and why does via-fence spacing depend on it?
7. What changes in a flex design when the bend is dynamic rather than static?
8. Explain to a smart friend in 3 sentences why heat is a layout problem, not just a component problem.
