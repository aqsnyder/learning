# Design for Manufacturing (DFM) and Fabrication

## Why This Section Matters

A design that can't be manufactured is worthless. Bridge the gap from design to production by understanding fabrication constraints, assembly processes, and output file generation.

**Prerequisites:** Sections 04–08.

---

## 🎯 Learning Objectives

After this section you can:
- Generate a complete fabrication and assembly package (Gerber X2, Excellon with plated/non-plated split, IPC-2581 or ODB++, pick-and-place, BOM, fab and assembly drawings) and verify it independently instead of trusting the exporter.
- Apply fab DFM rules (annular ring, drill-to-copper, mask web, copper-to-edge, slivers, acid traps) and IPC-2221A's land-size equation, and reconcile both with a fab's actual published capabilities.
- Design land patterns and stencils for assembly: IPC-7351 density levels, exposed-pad paste windowing, thermal-via treatment, fiducials, and panelization.
- Design for test: plan probe access under fixture constraints (IPC-2221A §3.5), programming/debug access, and a production test flow with an explicit fault-coverage estimate.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Concept | Gerber file generation and review | — | — | Output files, drill files, pick-and-place |
| 🔑 | Concept | DFM rules | — | — | Minimum trace/space, annular rings, solder mask dams |
| 🔑 | Concept | DFA (Design for Assembly) | — | — | Solder paste stencil, component orientation, panelization, fiducials |
| | Reference | IPC-2221 manufacturing guidelines | IPC | [Included](../documents/IPC-2221A(L).pdf) | The design-side rules fabrication depends on (annular rings, hole/land sizes, clearances, test coupons). IPC-2221 is a design standard; fabricated-board acceptance is covered by IPC-6012 / IPC-A-600. The included copy is Rev A (2003; current is IPC-2221C, 2023) |
| | Reference | IPC-7351 land pattern standard | IPC | — | Footprint/pad design guidelines |
| 🔑 | Fab House | JLCPCB | — | [Capabilities](https://jlcpcb.com/capabilities/pcb-capabilities) | Affordable prototyping. The capabilities page lists the limits your DRC should match: trace/space, via drill, layer counts, impedance-control tolerance |
| | Fab House | PCBWay | — | [Link](https://www.pcbway.com/) | Prototyping and small batch |
| | Fab House | OSH Park | — | [Link](https://oshpark.com/) | US-based prototyping |
| | Video | Phil's Lab Gerber generation tutorials | Phil's Lab | [YouTube](https://www.youtube.com/@PhilsLab) | Step-by-step output file generation |
| | Tool | KiCad Gerber viewer | — | — | Built-in output verification |
| | Reference | Gerber Layer Format Specification (rev. 2024.05) | Ucamco | [ucamco.com/en/gerber](https://www.ucamco.com/en/gerber) | The official Gerber spec. Output Gerber X2 so the files carry attributes (pad/via/fiducial functions, net names) and the fab gets your intent, not just shapes |
| | Tool | kicad-cli | KiCad Project | [Docs](https://docs.kicad.org/10.0/en/cli/cli.html) | KiCad's command-line interface: scripted ERC/DRC and exports (Gerbers, drill, positions, BOM, PDFs, 3D), so outputs are reproducible rather than click-generated |
| | Tool | KiBot | INTI-CMNB | [GitHub](https://github.com/INTI-CMNB/KiBot) | Config-driven generation of fab and documentation outputs, with an official GitHub Action. Every commit or tag can produce a complete release package (hardware CI) |
| | Tool | KiKit | yaqwsx | [Docs](https://yaqwsx.github.io/KiKit/latest/) | Panelization (tabs, mouse bites, V-cuts), fab-house output presets, and stencil generation for KiCad boards |

---

## Suggested Order

1. **Gerber file generation and review** — Understand the output files your fab house needs; skim the Ucamco spec's X2 attribute section.
2. **DFM rules** — Learn the manufacturing constraints that drive your design decisions.
3. **DFA (Design for Assembly)** — Understand assembly-side requirements (stencils, orientation, panelization).
4. **Phil's Lab Gerber tutorials** — Watch the full output generation workflow.
5. **KiCad Gerber viewer** — Practice verifying your own output files.
6. **JLCPCB capabilities page** — Study a real fab house's design rules and constraints.
7. **IPC-2221 / IPC-7351** — Reference the formal standards for manufacturing and land patterns.
8. **PCBWay / OSH Park** — Compare capabilities across fab houses for different project needs.
9. **kicad-cli → KiBot → KiKit** — Once the manual flow is understood, script it: reproducible outputs from the command line, CI-generated release packages, and automated panelization.
10. **Bring-up and production test** — When the boards arrive, continue with [Section 13](../13-bring-up-test-and-debug/README.md). Your DFT plan (Practice 4) and production-test skeleton (mini-project) are its starting point.

---

## 🛠️ Practice

1. **IPC land-size equation vs fab capability** — Using IPC-2221A §9.1.1 (minimum land = a + 2b + c, with Table 9-1's fabrication allowance and Table 9-2's minimum annular ring), compute minimum lands for 0.2, 0.3, and 1.0 mm holes at producibility levels A, B, and C. Compare with the minimums on the JLCPCB, PCBWay, and OSH Park capability pages. Deliverable: comparison table + the via and PTH padstacks you will standardize on, noting which IPC level you are implicitly claiming. *(~1.5 h · IPC-2221 §9, JLCPCB, PCBWay, OSH Park capability pages)*
2. **Output package round-trip with seeded faults** — From one of your boards, generate Gerber X2, Excellon (PTH and NPTH separate), pick-and-place, BOM, and IPC-2581 or ODB++. Seed five faults — no paste on a QFN exposed pad, a mounting hole flagged plated, one part rotated 90° in the CPL, zero mask expansion on fine-pitch pads, silk text over a pad — then verify the package in KiCad's Gerber viewer and one independent viewer (your fab's online viewer or gerbv). Deliverable: a written output checklist + a script (`kicad-cli` or a KiCad jobset) that regenerates everything. Done when the checklist catches 5/5 faults and the fab's online DFM shows no surprises on the clean set. *(~3 h · Gerber file generation and review, Phil's Lab Gerber generation tutorials, KiCad Gerber viewer, JLCPCB)*
3. **Land patterns that solder** — For six footprints from your library (0402, 0603, SOT-23, SOIC-8, a 5 × 5 mm QFN with exposed pad, LQFP-100), compare pads with the manufacturer's recommended land pattern and an IPC-7351 calculation at nominal density (toe/heel/side fillet goals from component tolerances). For the QFN, design a windowpane paste aperture for roughly 50–70 % exposed-pad coverage, choose the stencil thickness, and decide how thermal vias are treated (tented, plugged, or filled) so solder doesn't wick away. Deliverable: delta table, updated footprints, and a one-line rationale per change. *(~3 h · IPC-7351 land pattern standard, DFA (Design for Assembly) concept)*
4. **DFT plan for a real board** — Add production test access to one of your boards following IPC-2221A §3.5.4.1: test lands ≥ 0.9 mm (0.6 mm on small boards), 2.5 mm centers where possible, probing from one side, none within 3 mm of the board edge, 5 mm clear of tall parts, and a land on every node you can afford. Cover every rail (Kelvin pairs on precision rails), reset/boot/SWD, USB VBUS/CC, and key analog nodes; export test-point XY from KiCad for a pogo-pin fixture with tooling holes. Then write a fault-coverage matrix: which test (AOI, flying probe/ICT, boundary scan if your MCU's BSDL exists, functional) catches opens, shorts, wrong/missing/reversed parts, exposed-pad voids, and firmware errors. Deliverable: DFT memo + KiCad changes + fixture CSV. Done when ≥ 90 % of nets are probed or covered by a functional test and every gap is justified. *(~4 h · IPC-2221 §3.5, DFA (Design for Assembly) concept)*

**🏗️ Mini-project — Production Release Kit:** Turn one of your boards into a production release: (1) one command (`kicad-cli jobset run` or `make release`) that builds version-stamped Gerber X2, drill files, IPC-2581/ODB++, BOM with alternates (Section 03), CPL, a fab drawing carrying your Section 01 notes, and an assembly drawing; (2) a KiKit panel with rails, fiducials, tooling holes, and mouse-bites or V-score per your assembler's rules; (3) DFM/DFA reviews from two fabs with every EQ resolved and logged; (4) the DFT package from Exercise 4 plus a Python production-test skeleton (instrument control over PyVISA, SWD flashing through your programmer's CLI, per-serial-number pass/fail logging). Deliverable: `projects/pcb/09-release/`. Success: a clean checkout reproduces identical outputs (hash-compare after stripping creation-date attributes), and a fab/assembler builds the panel without asking anything the package doesn't already answer. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What does Gerber X2 add over RS-274X, and what does IPC-2581/ODB++ carry that a Gerber set does not?
2. Define annular ring and breakout. Which IPC performance class requires an annular ring on every plated-through hole (IPC-2221A §9.1.2)?
3. Why is paste on a QFN exposed pad reduced to roughly half to three-quarters coverage, and what goes wrong at 100 %?
4. What does a fab's bare-board electrical (netlist) test prove — and what can it not prove about your design?
5. Misconception probe: "The fab's online DFM check passed, so the board is manufacturable at volume."
6. Where do fiducials go, how many do you need, and what keep-out do they require?
7. List four fixture constraints IPC-2221A gives for in-circuit test lands.
8. Explain to a smart friend in 3 sentences the difference between DFM, DFA, and DFT.
