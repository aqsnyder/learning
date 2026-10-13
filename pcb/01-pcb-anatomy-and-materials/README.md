# PCB Anatomy and Materials

> **Why this section matters:** Understanding what a PCB physically IS before you design one.

**Prerequisites:** [Section 00 — Electronics Fundamentals](../00-electronics-fundamentals/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Walk through multilayer fabrication — core/prepreg lamination, drilling, desmear, electroless and electrolytic plating, imaging and etch, solder mask, surface finish, electrical test — and name the design rule each step creates.
- Compute copper thickness, sheet resistance, trace resistance and IR drop, and IPC-2221 current capacity, and explain why IPC-2152 replaced IPC-2221's conductor-sizing charts (whose internal-layer curves were never tested).
- Choose between standard FR-4, high-Tg/high-Td FR-4, low-loss, and PTFE-class laminates from datasheet Dk/Df vs frequency, Tg, Td, z-axis CTE, and moisture absorption.
- Critique a legacy design guide, separating durable physics from obsolete process advice and contested folklore.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Tutorial | PCB Design Tutorial Rev A (2004) | David L. Jones (EEVblog) | [documents/PCBDesignTutorialRevA.pdf](../documents/PCBDesignTutorialRevA.pdf) | Comprehensive intro to PCB structure. It is a 2004, Protel-era snapshot, and some advice is outdated: its split-plane "star grounding" (see Section 05) and "avoid generating Gerbers" (see Section 09). Its track-width table comes from the old IPC-2221 charts (use IPC-2152; see Section 05) |
| 🔑 | Web Resource | Nine Dot Connects | — | [ninedotconnects.com](https://www.ninedotconnects.com/) | Professional PCB design education |
| | Video Series | Altium Academy Basics | — | [youtube.com/@AltiumAcademy](https://www.youtube.com/@AltiumAcademy) | PCB fundamentals and stackup intro |
| | Reference | IPC-2221 Generic Standard on Printed Board Design (included copy: Rev A, 2003) | IPC | [documents/IPC-2221A(L).pdf](../documents/IPC-2221A(L).pdf) | THE foundational IPC design standard. The included Rev A (2003) has been superseded by IPC-2221B (2012) and now [IPC-2221C (2023)](https://shop.electronics.org/ipc-2221/ipc-2221-standard-only/Revision-c/english). Its conductor current charts (Fig. 6-4) date from a 1956 NBS report, and the internal-layer curve was never tested (it is just half the external one; see its own Appendix B). IPC-2152 (2009) replaced those charts, so size traces for current with IPC-2152 (Section 05), not Fig. 6-4 |
| | Web Resource | Sierra Circuits PCB Knowledge Base | — | [protoexpress.com/blog](https://www.protoexpress.com/blog/) | Manufacturing constraints reference |
| | Article | PCB Materials Guide (FR-4, Rogers, etc.) | — | — | Understanding substrate choices |

**Also used here (tracked in their home sections):** Saturn PCB Toolkit and IPC-2152 ([Section 05](../05-power-and-grounding/README.md)) for Practice 2; Rick Hartley's grounding lecture ([Section 05](../05-power-and-grounding/README.md)) as evidence in Practice 4.

---

## Suggested Order

**Core path (🔑):** Dave Jones's *PCB Design Tutorial* (2004) → Nine Dot Connects

1. **PCB Design Tutorial Rev A** — Read end-to-end for a solid mental model of PCB structure (layers, vias, plating). Treat it as a 2004 snapshot: later sections correct its grounding and output-file advice.
2. **Nine Dot Connects** — Explore their free articles and courses for professional-grade stackup and materials education.
3. **Altium Academy Basics** — Watch the introductory videos on layers, stackups, and manufacturing.
4. **PCB Materials Guide** — Understand when to use FR-4 vs. Rogers vs. other substrates.
5. **Sierra Circuits Knowledge Base** — Bookmark as an ongoing reference for DFM constraints.
6. **IPC-2221** — Skim for electrical clearance (Table 6-1), lands and annular rings, holes and test coupons, then return as needed during design. The included copy is Rev A (2003); the current revision is IPC-2221C (2023). For trace width vs. current, use IPC-2152 (Section 05), not the Fig. 6-4 charts.

---

## 🛠️ Practice

1. **Copper arithmetic, checked 4-wire** — Compute 1 oz copper's thickness (µm and mil) and its sheet resistance at 25 °C, and use them to reproduce the milliohms-per-inch column of the track-width table in *PCB Design Tutorial Rev A*. Then pick a long, uniform trace (≥ 50 mm) on one of your boards, predict its resistance (copper tempco ≈ +0.39 %/°C), and measure it 4-wire with a precision DMM or SMU. Deliverable: calc sheet + measurement. Done when you match the tutorial within ~5 % and the measurement within ~15 %, and can explain the sign of the error (plating, etch, temperature). *(~2 h · PCB Design Tutorial Rev A, IPC-2221 §10.1)*
2. **IPC-2221 vs IPC-2152** — Implement IPC-2221's I = k·ΔT^0.44·A^0.725 (k = 0.048 external, 0.024 internal; A in mil²) in Python and plot width vs current (1–10 A, ΔT = 10 °C, 1 oz) for outer and inner layers. Overlay the tutorial's table and an IPC-2152 calculator (e.g., Saturn PCB Toolkit, with and without its plane modifier), then read IPC-2221A Appendix B and explain the gaps. Deliverable: plot + a 150-word recommendation for carrying 3 A on an inner layer of a 6-layer board. Done when your IPC-2221 curve reproduces the tutorial's 1 oz column within ~20 % (it is the same 1950s data; the rounded 1 A row is the worst, about 19 % off) and your memo cites Appendix B on how the internal-layer curves were derived. *(~2 h · IPC-2221 §6.2 and Appendix B, PCB Design Tutorial Rev A, Sierra Circuits Knowledge Base)*
3. **Laminate datasheets → design numbers** — For three laminates your fab offers (a standard FR-4, a high-Tg/high-Td FR-4, and a low-loss or hydrocarbon-ceramic RF material), extract Dk and Df at the highest listed frequency, Tg, Td, z-axis CTE below and above Tg, and moisture absorption. Compute dielectric loss at 1 and 5 GHz (α ≈ 2.3 · f(GHz) · Df · √Dk dB/in) and the z-axis growth of a 1.6 mm board from 25 °C to 260 °C versus a copper via barrel (~17 ppm/°C). Deliverable: a one-page memo choosing a material for (i) a 6-layer MCU/USB/Ethernet board, (ii) a 2.4 GHz antenna feed, and (iii) a low-leakage precision analog board, each justified by the deciding numbers. *(~3 h · PCB Materials Guide, Sierra Circuits Knowledge Base, Nine Dot Connects, IPC-2221 Tables 4-1 and 6-2)*
4. **Red-pen the 2004 tutorial** — Read *PCB Design Tutorial Rev A* end to end and tabulate ≥ 12 of its claims as *still right*, *outdated process*, or *wrong/contested*, each with one line of reasoning and a source. Include at least: "always use imperial units", "generating Gerbers is a thing of the past", split planes for star grounding, "six layers = four signal + two power", "right-angle corners cause no measurable EMI", "one bypass capacitor per power pin", "route pin → capacitor → plane", HAL as the standard finish, the critical-length rule, and the crosstalk formula 1/(1+(D/H)²). Done when every *wrong/contested* verdict cites something stronger than opinion — e.g., IPC-2221A §6.4.4 ("reference planes … should not be segmented"), a Nine Dot Connects/Hartley lecture, or a measurement. *(~3 h · PCB Design Tutorial Rev A, IPC-2221, Nine Dot Connects, Altium Academy Basics)*

**🏗️ Mini-project — Fab Notes for Your Template:** Write the fabrication-drawing notes block for your KiCad template: base material (Tg/Td class and IPC-4101 slash sheet), finished thickness and tolerance, outer/inner copper weights, minimum hole-wall plating, surface finish (ENIG vs lead-free HASL vs ImAg/OSP, with the deciding reason), mask and silk, performance class (IPC-2221A §1.6.2), impedance-control note format, bow and twist, electrical test, and marking. Give every note a one-line rationale. Send a quote request with these notes to two fabs (one low-cost offshore, one domestic quick-turn). Deliverable: `projects/pcb/01-fab-notes/` with the notes, both quotes, and every engineering question (EQ) you received plus its resolution. Success: both fabs quote with no open EQs, and the block drops straight into your template's fab drawing. *(~6 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What are cores and prepregs, and which one's final thickness depends on the copper pattern pressed into it?
2. State 1 oz copper's thickness and approximate sheet resistance, then estimate the resistance of a 0.25 mm × 40 mm trace in 1 oz copper.
3. Per IPC-2221A Appendix B, where did the external-conductor current chart come from, and how were the internal-layer curves derived?
4. Why does z-axis CTE above Tg matter more to via reliability than Tg itself?
5. Estimate the dielectric loss of 10 in of FR-4 (Dk 4.2, Df 0.02) at 1 GHz. Does it matter for USB 2.0 High-Speed? For a 10 Gb/s serial link?
6. Misconception probe: "FR-4 is one material with Dk = 4.5." What actually varies, and by how much (IPC-2221A Table 6-2)?
7. Name three surface finishes and a situation that favors each.
8. Explain to a smart friend in 3 sentences what is physically inside a 6-layer PCB and how its layers get connected.
