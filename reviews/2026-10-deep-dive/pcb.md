# PCB Design — Review

> **Deep-dive review, October 2026** · curriculum: [`pcb/`](../../pcb/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict
The curriculum has the right skeleton: a sensible 00→11 arc, the right educators (Hartley, Bogatin, Ott, Phil's Lab, Feranec), a KiCad-centred workflow, and Rick Hartley's reading list as its intellectual spine. Against a professional bar it falls well short. Most rows are channel-level links ("Phil's Lab — Power Design Tutorials" → channel home) or link-less "Concept" rows. The ⭐ list was wrong: only 6 of Rick's 12 books were present, ⭐ sat on a book that is not on the list and on four of Rick's own talks, and the README table therefore showed 7 entries, one of them wrong. Two key files had broken links, and currency had lapsed: KiCad 8 docs while KiCad 10 is current, and the 2003 IPC-2221A presented as "THE" standard with no word that its current charts were replaced by IPC-2152. Most importantly, the topics that make up Aaron's actual job are almost absent: analog/mixed-signal and precision measurement, bring-up/test/DFT, interface layout (USB, Ethernet), switching-regulator layout, and release automation. **Overall grade: C as found (about B− after this pass).** **Single most important improvement:** add an *Analog, Mixed-Signal & Precision Measurement* section. Today the curriculum trains a digital-board designer, not a designer of precision test-and-measurement hardware. *Update: both proposed sections (Analog/Mixed-Signal & Precision Measurement, and Bring-up/Test & Debug) were approved and created as Sections 12 and 13; see below.*

## Scorecard
Scores reflect the curriculum **as found**, before this pass.

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 Electronics Fundamentals | 3 | 3 | 3 | 3 | 3 | C | Right anchor (AoE) but beginner-skewed. LAoE was mislabelled "free", the MIT link pointed to the OCW home page, and there was no op-amp practice or simulation |
| 01 PCB Anatomy & Materials | 2 | 2 | 2 | 4 | 3 | D+ | Rests on a 2004 tutorial and the 2003 IPC-2221A with no caveats; both links broken; materials barely covered |
| 02 Schematic Capture | 3 | 4 | 2 | 4 | 4 | C+ | Sensible but generic; pinned to KiCad 8; no library conventions or MCU checklists |
| 03 Component Selection | 2 | 4 | 3 | 3 | 2 | C− | Distributor links plus link-less concepts; nothing on lifecycle, derating, or precision passives |
| 04 Layout Fundamentals | 3 | 2 | 3 | 3 | 3 | C | Three broken, mislabelled prerequisite links; channel-level links instead of specific lessons |
| 05 Power & Grounding | 3 | 3 | 3 | 4 | 4 | B− | Strong Hartley/Bogatin core, but ⭐ misused on talks; no switching-regulator layout, IPC-2152, or mixed-signal grounding |
| 06 Signal Integrity | 3 | 3 | 3 | 4 | 4 | B− | Right books, but 2 of Rick's books missing, an Amazon link, an unverified 🔑 channel, no interface-specific guides |
| 07 EMC & Compliance | 3 | 2 | 3 | 4 | 3 | C+ | Ott is right, but ⭐ was on a non-list book, 3 list books were missing, and nothing covered T&M product standards or pre-compliance |
| 08 Multi-Layer & Stackup | 2 | 2 | 3 | 2 | 3 | C− | Mostly concepts plus a YouTube *search* link; IPC-2221 mis-described as a stackup standard; sits after SI/EMC although it underpins them |
| 09 DFM & Fabrication | 3 | 3 | 2 | 4 | 3 | C | Good outline, few resources; no output automation/CI, Gerber X2, or DFT |
| 10 Advanced Topics | 1 | 3 | 2 | 3 | 2 | D | Five link-less concepts and one blog post; no analog, simulation, RF or flex resources |
| 11 Reference Projects | 3 | 2 | 3 | 4 | 3 | C | Good beginner set, but comma.ai has no board files to study and there are no professional high-speed or instrument references |

## Section-by-section

### 00 — Electronics Fundamentals
- **Strengths:** AoE and LAoE as the core; MIT 6.002 for rigor; a short, clear order.
- **Problems:**
  - ✔ LAoE was typed "Book (Free Companion)". It is a paid Cambridge UP book, now in a 2nd edition.
  - ✔ The MIT 6.002 link went to the OCW home page; now the 2007 Agarwal course page.
  - ✔ AoE and LAoE had no links.
  - ✱ GreatScott! handle `@greatscaboratory` looks wrong (likely `@greatscottlab`); I could not fetch YouTube channel pages to confirm.
  - ✱ For a working professional this is a refresh section. Consider labelling it "review/reference" and pointing the depth at analog.
- **Missing:** op-amp design practice (noise, stability, input protection); circuit simulation as a habit; measurement fundamentals (scope, DMM) — see proposed sections.
- **Added:**
  - TI Precision Labs — Op Amps — Texas Instruments — (ongoing)
  - LTspice — Analog Devices — current v26

### 01 — PCB Anatomy and Materials
- **Strengths:** short; the included tutorial gives a whole-board mental model fast.
- **Problems:**
  - ✔ Both links were broken (`documents/…` → `../documents/…`).
  - ✔ The tutorial's author was "—". It is David L. Jones (EEVblog), Rev A, June 2004.
  - ✔ The tutorial's dated advice is now flagged: "use split planes for star grounding", "avoid generating Gerbers", imperial-only units, and a track-width table built on the old IPC charts.
  - ✔ The IPC-2221 row presented the 2003 Rev A as current. Rev B (2012) and Rev C (2023) supersede it.
  - ✔ The row and the suggested order now say that the Fig. 6-4 current charts (from a 1956 NBS report; the internal-layer curve is untested, half the external one, per the document's own Appendix B) were replaced by IPC-2152 (2009).
  - ✱ The "PCB Materials Guide" row still has no link.
- **Missing:**
  - laminate selection: Dk/Df vs. frequency, Tg/Td, CTE-z, CAF, moisture/SIR (matters for precision leakage)
  - copper foil roughness
  - surface-finish trade-offs (ENIG/ENEPIG/HASL/OSP)
  - IPC Class 2 vs. Class 3
  - IPC-4101 slash sheets
  - IPC-6012 / IPC-A-600 acceptance
- **Added:** nothing (corrections only). The IPC-2221C reference link is inline.

### 02 — Schematic Capture and Library Management
- **Strengths:** KiCad-first; Aaron's own template is wired in; library sources listed.
- **Problems:**
  - ✔ KiCad 8 docs → KiCad 10 Getting Started (10.0 released 2026-03-20; adds design variants and a graphical DRC rule editor; design blocks arrived in 9.0).
  - ✔ The suggested order now warns to verify third-party footprints and pin maps against the datasheet.
- **Missing:** ERC strategy, hierarchical design, net naming, BOM fields and variants, schematic review checklists, database libraries.
- **Added:**
  - KiCad Library Conventions (KLC v3.0.67) — KiCad Library Team — ongoing
  - AN4488 Getting started with STM32F4 hardware development — STMicroelectronics — Rev 7, 2018 (with a note to use your family's equivalent)

### 03 — Component Selection and Sourcing
- **Strengths:** points at the right daily tools (DigiKey, Mouser, Octopart, JLC parts).
- **Problems:**
  - ✱ 🔑 sits on a link-less concept ("Design for Supply Chain").
  - ✱ The JEDEC row has no link.
  - ✱ Section placement after schematic is fine, but selection and capture are iterative.
- **Missing:**
  - lifecycle status (Active/NRND/EOL), PCNs, second-sourcing
  - MLCC DC-bias and temperature derating (critical for analog signal paths)
  - precision passive specs (TCR, voltage coefficient, drift, dielectric absorption)
  - tantalum/polymer pitfalls, TVS/ESD selection, connector selection, datasheet-reading discipline
- **Added:** nothing. The ADI article on MLCC derating could not be fetched after the WebFetch budget ran out.

### 04 — PCB Layout Fundamentals
- **Strengths:** placement-first philosophy; Phil's Lab and Feranec are the right teachers.
- **Problems:**
  - ✔ Three prerequisite links pointed to non-existent directories with wrong section names and numbers (`01-electronics-fundamentals`, `02-schematic-design`, `03-pcb-stackup-and-materials`). They now point to 00, 01 and 02.
  - ✔ KiCad 8 docs → KiCad 10 PCB Editor docs.
  - ✱ Channel-home links stand in for lessons.
  - ✱ "Placement determines 90%" is folklore (the Dave Jones tutorial calls it an old saying). It is fine as a mnemonic.
- **Missing:** stitching vias at layer changes, via sizing, partitioning (analog/digital/power), test-point placement, MCAD/enclosure co-design, assembly documentation, layout review checklist.
- **Added:**
  - KiCad 6 STM32 PCB Design Full Tutorial (Phil's Lab #65) — Phil Salmony — 2022
  - AN2867 Oscillator design guidelines (incl. crystal layout) — STMicroelectronics — Rev 24, 2026

### 05 — Power Distribution and Grounding
- **Strengths:** Hartley's grounding lecture plus the Morrison and Smith & Bogatin books form the correct core.
- **Problems:**
  - ✔ ⭐ removed from two Rick talks (the list covers books only).
  - ✔ Book links and years filled in.
  - ✔ The Saturn row now says its current calculator is IPC-2152-based.
  - ✱ The PDN video (WnLRHuvl6Eg) is on the **NineDotConnects** channel per oEmbed. I could not confirm that Rick presents it (YouTube returned HTTP 429), so check it.
  - ✱ "Rick's grounding lecture has saved more designs than any other resource" is unverifiable hype.
- **Missing:**
  - switching-regulator layout (added)
  - trace/plane current sizing (added)
  - mixed-signal grounding (added)
  - LDO noise/PSRR, sequencing
  - input protection (reverse polarity, eFuse, TVS)
  - USB-C power sink design
  - MLCC derating in PDN
- **Added:**
  - ⭐ Grounding and Shielding: Circuits and Interference (6th ed.) — Ralph Morrison — 2016
  - IPC-2152 Current-Carrying Capacity — IPC — 2009
  - MT-101 Decoupling Techniques — Analog Devices — 2009
  - MT-031 Grounding Data Converters (AGND/DGND) — Kester, Bryant, Byrne — 2008
  - AN-136 PCB Layout for Non-Isolated Switching Supplies — Henry Zhang (ADI) — (year not shown on page)

### 06 — Signal Integrity
- **Strengths:** Bogatin, Black Magic and Ritchey are the right books; return-path emphasis.
- **Problems:**
  - ✔ Amazon link → Pearson/InformIT (3rd ed., 2018).
  - ✔ Black Magic and Right the First Time links added (1993; Vol I 2003, Vol II 2007).
  - ✔ 🔑 removed from "Dr. EMC": no presenter is named, and the only channel with that title uses the handle `@DrEMC-sf8rx`, not the linked `@DrEMC`.
  - ✔ The UltraCAD row now points current sizing to IPC-2152.
  - ✔ Optional cross-link added to `physics/03-electromagnetism`.
- **Missing:** USB-C high-speed specifics (CC/SBU, reversible lanes), loss and copper roughness, via stubs and back-drilling, IBIS and field-solver workflow, TDR measurement.
- **Added:**
  - ⭐ High-Speed Signal Propagation: Advanced Black Magic — Johnson & Graham — 2003
  - ⭐ High-Speed Digital System Design — Stephen H. Hall, Garrett W. Hall, James A. McCall — 2000
  - High-Speed Interface Layout Guidelines (SPRAAR7J: USB 2.0/3.x, PCIe, HDMI, SATA, SGMII) — Texas Instruments — 2023
  - Ethernet PHY PCB Design Layout Checklist (SNLA387) — Lysny Woodahl (TI) — 2021

### 07 — EMC and Compliance
- **Strengths:** Ott's *EMC Engineering* as the anchor; good concept list.
- **Problems:**
  - ✔ ⭐ removed from Ott's *Noise Reduction Techniques*. It is not on Rick's list; the list names *EMC Engineering*.
  - ✔ Ott link added (DOI, 2009).
  - ✔ 🔑 removed from the unverified Dr. EMC channel.
  - ✔ The compliance concept now names the product standards for measurement and lab equipment (IEC 61326 EMC, IEC 61010 safety).
  - ✱ The "Rick Hartley — EMC Lectures" row links to a YouTube *search*; replace it with specific talks.
- **Missing:**
  - pre-compliance testing (near-field probes, LISN, spectrum analyzer)
  - ESD design (IEC 61000-4-2)
  - immunity
  - cable/connector shielding
  - a compliance plan for a crowdfunded or small-volume product
- **Added:**
  - LearnEMC — Todd Hubing — ongoing
  - ⭐ PCB Design for Real-World EMI Control — Bruce R. Archambeault — 2002
  - ⭐ Digital Design for Interference Specifications (2nd ed.) — David L. Terrell & R. Kenneth Keenan — 1999
  - ⭐ Introduction to Electromagnetic Compatibility (2nd ed.) — Clayton R. Paul — 2006

### 08 — Multi-Layer Design and Stackup
- **Strengths:** names the right decisions (layer count, impedance, blind/buried vias).
- **Problems:**
  - ✔ ⭐ removed from Rick's stackup lectures.
  - ✔ Ritchey link added.
  - ✔ The IPC-2221 row claimed it is "Industry standard for PCB stackup design". It is a generic design standard: §4 covers materials and dielectric spacing, and §6.4 gives the closed-form impedance equations. Corrected, with a pointer to fab stackups and field solvers.
  - ✱ The 🔑 lecture row is a YouTube search link.
  - ✱ Sequencing: stackup comes after SI and EMC, yet plane arrangement is what Sections 05–07 assume. Move it earlier (see Structural observations).
- **Missing:** concrete 4/6/8-layer stackup recipes with plane pairing, fab stackup tables and impedance calculators, hybrid stackups, HDI/microvias (IPC-2226), copper balance and warpage.
- **Added:** nothing (corrections only).

### 09 — Design for Manufacturing (DFM) and Fabrication
- **Strengths:** clear output → DFM → DFA flow; real fab houses.
- **Problems:**
  - ✔ The IPC-2221 row called it "Industry standard for PCB manufacturing". It is a design standard; board acceptance is IPC-6012 / IPC-A-600. Revision noted.
  - ✔ JLCPCB link now goes to the capabilities page that the row tells you to read.
  - ✱ Three 🔑 concept rows have no resources.
  - ✱ IPC-7351 is listed without revision; I could not verify whether IPC-7352 now replaces 7351B.
- **Missing:**
  - output automation and CI (added)
  - Gerber X2 / IPC-2581 / ODB++ (Gerber spec added)
  - fab notes, drawings and assembly drawings
  - stencil design (IPC-7525)
  - panel design for assembly
  - DFT and test points (proposed section)
  - release/revision management (see Structural observations)
- **Added:**
  - Gerber Layer Format Specification (rev. 2024.05) — Ucamco — 2024
  - kicad-cli — KiCad Project — KiCad 10
  - KiBot — INTI-CMNB — ongoing
  - KiKit — yaqwsx — ongoing

### 10 — Advanced Topics
- **Strengths:** the right topic names (BGA, thermal, flex, RF).
- **Problems:**
  - ✱ Five of the eight original rows were concepts with no resources.
  - ✱ "Tech Explorations KiCad Advanced (BGA, SI, High-Speed)" has no link and I could not confirm it exists; Tech Explorations' KiCad line is "KiCad Like a Pro". Treat it as possibly hallucinated.
  - ✱ RF and flex still have no resources.
- **Missing:** RF layout (no resources), HDI, flex (IPC-2223 resources), high-voltage creepage and clearance (IEC 61010), design for reliability (vibration, thermal cycling, conformal coat).
- **Added:**
  - AN-2020 Thermal Design By Insight, Not Hindsight — Texas Instruments — 2013 (rev C)
  - openEMS + gerber2ems — Thorsten Liebig / Antmicro — ongoing
  - KiCad IPC API + kicad-python — KiCad Project — 9.0+ (SWIG bindings deprecated, removal planned for 11.0)
  - The interim analog cluster I first placed here (precision-layout concept row, *Op Amp Applications Handbook*, Keithley *Low Level Measurements Handbook*, Phil's Lab mixed-signal course) **moved to the new Section 12** after approval. Section 10's merged scaffolding never referenced it. Section 10 now points to Sections 12 and 13 in its intro and Suggested Order.

### 12 — Analog, Mixed-Signal and Precision Measurement (created after approval)
- **File:** `pcb/12-analog-mixed-signal-and-precision-measurement/README.md`. Taken after Section 05; numbered 12 so nothing is renumbered.
- **Structure:** same layout as Section 06 — Why, Prerequisites, 🎯 Learning Objectives (5), Marking Convention, Resources, Suggested Order, 🛠️ Practice (5 exercises + mini-project "Precision Current-Measurement Channel"), ✅ Check Yourself (8).
- **Resources (10 rows):**
  - moved from 10: precision-layout concept, *Op Amp Applications Handbook* (🔑), Keithley LLMH (now 🔑, as the core text here), Phil's Lab mixed-signal course
  - newly placed in a section (verified earlier): *Basic Linear Design* / *Linear Circuit Design Handbook* (Zumbahlen ed., ADI, 2007/2008; free chapters incl. Ch. 12 PCB Design Issues); TI Precision Labs — ADCs
  - four concept rows: error budgets and calibration; ADC drive, references and partitioning; force/sense architecture; high-gain front-end overload recovery
- **Cross-referenced, not duplicated:** MT-031 and Morrison (05), TI Precision Labs — Op Amps and LTspice (00), the STM32 hardware getting-started note (02), ThunderScope (11).
- **No duplication:** the practice deliberately builds on what the merged scaffolding already covers (00's high-Z error and noise budgets, 03's MLCC and op-amp selection, 04's Kelvin/guard layout and precision-channel block, 05's grounding memo). It adds:
  - a calibrated full-chain budget
  - SAR driver/reference settling
  - ENOB measurement under digital activity
  - force/sense stability into cabled loads
  - overload recovery in high-gain AC-coupled front ends

### 13 — Bring-up, Test and Debug (created after approval)
- **File:** `pcb/13-bring-up-test-and-debug/README.md`. Taken after Section 09.
- **Structure:** same as 12. Practice has 5 exercises plus the mini-project "Pilot-Run Test Station"; Check Yourself has 8 questions.
- **Resources (7 rows):** Agans' *Debugging* (🔑), XJTAG boundary-scan primer, XJTAG DFT Guidelines, and four concept rows (staged bring-up plan 🔑, probing technique, fault localization, production test).
- **Cross-referenced:** AN4488 (02), AN2867 (04), IPC-2221A §3.5 (09), TI Precision Labs op-amp "Board level troubleshooting" (00), Keithley LLMH (12), Glasgow (11), and software/07 for firmware debugging.
- **No duplication:** builds on Section 09's merged DFT exercise and production-test skeleton rather than repeating them. Adds:
  - written-expectation bring-up
  - an MCU first-contact runbook with seeded faults
  - honest ripple measurement
  - current-injection short-finding
  - JTAG chain review / boundary-scan ROI
  - a pilot-run station with Cpk and a repeatability check

### 11 — Reference Projects and Open-Source Hardware
- **Strengths:** a good ladder from simple (Adafruit, SparkFun) to complex (HackRF).
- **Problems:**
  - ✔ comma.ai's flagship hardware repo (panda) holds firmware and software only, with no schematics or layouts; the description now says so.
  - ✱ The Raspberry Pi claim "production-quality reference designs … professional stackups" is likely overstated (SBC layouts are not published). The link now redirects to pip.raspberrypi.com. Unverified.
- **Missing:** a professional high-speed KiCad reference (added), an instrument front end (added), an SMU/PMU-class open design (none found), and ST Nucleo/Discovery design files as STM32 references (not verified).
- **Added:**
  - 🔑 Antmicro Open Hardware Portal — Antmicro — ongoing
  - ThunderScope — EEVengers — ongoing (MIT licence)
  - Glasgow Interface Explorer — GlasgowEmbedded contributors — ongoing (OSHWA-certified)

### books/
- As found, 6 of Rick's 12 books were missing and ⭐ was on a non-list book. Years were blank for 8 of 12 rows.
- ✱ "Practical PCB Design — Mike D. Smith" carries 🔑 but I could not verify that the book exists. It is a likely hallucination; verify or cut it.
- ✱ "Complete PCB Design Using OrCAD" (Mitzner) needs an edition and year.
- ✔ Verified years filled in. ✔ ⭐ removed from #10.
- **Added:** the six missing ⭐ books, plus the free ADI *Op Amp Applications Handbook* (🔑) and the Keithley *Low Level Measurements Handbook*.

### courses/
- Thin: mostly whole channels. The KiCad 8 docs link was stale (✔ fixed). Rick's PDN talk presenter is unverified (✱).
- **Added:**
  - MIT 6.002 (proper link)
  - TI Precision Labs (Op Amps + ADCs)
  - LearnEMC
  - Phil's Lab Mixed-Signal course
  - Phil's Lab #65

### blogs-and-references/
- Thin. The standards list had no revision information, and the "Zach Peterson" row has no link (✱).
- **Added:**
  - LearnEMC and ADI's free handbooks and MT tutorials (sites)
  - LTspice, kicad-cli, KiBot, KiKit, openEMS + gerber2ems (tools)
  - IPC-2152, the Gerber spec, and IEC 61326/61010 (standards); the IPC-2221 revision note is ✔

### PROGRESS.md
- As found, about 20 items in sections had no checkbox, and ⭐ was wrong on 4 lines (two talks, the stackup lectures, Noise Reduction).
- ✔ Fixed. Every section item now has a checkbox, including all additions.

### README.md
- ✔ Rebuilt the ⭐ cross-reference to match the PDF exactly: 12 books in Rick's order, with his two groupings and a note that *Noise Reduction* is not on the list.
- ✔ Clarified the legend (books only).
- ✔ Documents line now gives the IPC-2221A revision and the tutorial's author and date.
- ✔ Softened "the standard curriculum for professional PCB designers".
- ✱ The Key Educators table still lists the unverified "Dr. EMC".
- The learning-path list is consistent with the directories.

## Corrections made
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| pcb/01-pcb-anatomy-and-materials/README.md:13 | link `documents/PCBDesignTutorialRevA.pdf`; author "—"; no caveats | `../documents/…`; "David L. Jones (EEVblog)", 2004; dated advice flagged (split planes, "avoid Gerbers", old IPC charts) | local `pcb/documents/PCBDesignTutorialRevA.pdf` title page ("by David L. Jones … Revision A - June 29th 2004") |
| pcb/01-pcb-anatomy-and-materials/README.md:16 | link `documents/IPC-2221A(L).pdf`; "THE foundational IPC standard" | `../documents/…`; Rev A 2003, superseded by 2221B (2012) and 2221C (2023); Fig. 6-4 charts replaced by IPC-2152 | https://webstore.ansi.org/standards/ipc/ipc2221c2023 ; https://pcdandf.com/pcdesign/index.php/editorial/menu-new-indust-prod/5545-ipc-releases-ipc-2152-standard ; IPC-2221A Appendix B (local) |
| pcb/01-pcb-anatomy-and-materials/README.md:29 | "Skim … to understand trace width …" | Skim for clearance (Table 6-1), lands and holes; use IPC-2152 for current | same as above |
| pcb/04-pcb-layout-fundamentals/README.md:9–11 | `../01-electronics-fundamentals`, `../02-schematic-design`, `../03-pcb-stackup-and-materials` (wrong numbers and names) | `../00-electronics-fundamentals`, `../01-pcb-anatomy-and-materials`, `../02-schematic-capture` | repo tree |
| pcb/04-pcb-layout-fundamentals/README.md:26 | docs.kicad.org/8/ | docs.kicad.org/10.0/en/pcbnew/pcbnew.html | https://docs.kicad.org/ ; https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/ |
| pcb/02-schematic-capture/README.md:14 | docs.kicad.org/8 | KiCad 10 Getting Started + KiCad 10 feature note | same |
| pcb/courses/README.md:14 | docs.kicad.org/8/ | docs.kicad.org (10.0 current) | https://docs.kicad.org/ |
| pcb/00-electronics-fundamentals/README.md:13 | AoE link "—" | artofelectronics.net + x-Chapters 2nd ed. (2026, new sensors chapter) | https://artofelectronics.net/ ; https://x.artofelectronics.net/ |
| pcb/00-electronics-fundamentals/README.md:14 | "Book (Free Companion)", no link | "Book (Lab Companion)", paid CUP book, 2nd ed. available, link | https://artofelectronics.net/ |
| pcb/00-electronics-fundamentals/README.md:18 | link ocw.mit.edu (home page); author/year "—" | course page; Anant Agarwal (with Jeffrey Lang); 2007 | https://ocw.mit.edu/courses/6-002-circuits-and-electronics-spring-2007/ |
| pcb/05-power-and-grounding/README.md:22 | 🔑⭐ "How to Achieve Proper Grounding" | 🔑 (talk is not on Rick's book list); Altium live-training noted | local Ricks-Reading-Recommendation.pdf ; https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ySuUZEjARPY&format=json |
| pcb/05-power-and-grounding/README.md:23 | 🔑⭐ "Power Distribution Networks" | 🔑; "posted on the NineDotConnects channel" | local PDF ; https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=WnLRHuvl6Eg&format=json |
| pcb/05-power-and-grounding/README.md:25 | Fast Circuit Boards link "—" | Wiley link; 2017 | https://wiley-vch.e-bookshelf.de/fast-circuit-boards-10620117.html |
| pcb/05-power-and-grounding/README.md:26 | PDN book link "—"; "Smith, Bogatin" | InformIT; 2017; "Larry D. Smith, Eric Bogatin" | https://www.informit.com/store/principles-of-power-integrity-for-pdn-design-simplified-9780132735551 |
| pcb/05-power-and-grounding/README.md:28 | Saturn "calculators for trace width …" | free (Windows); current calculator per IPC-2152; IPC-2221-formula calculators called obsolete by the vendor | https://saturnpcb.com/saturn-pcb-toolkit/ |
| pcb/06-signal-integrity/README.md:24 | Amazon link | InformIT; 3rd ed. 2018 | https://www.informit.com/store/signal-and-power-integrity-simplified-9780134513416 |
| pcb/06-signal-integrity/README.md:25 | Black Magic link "—" | sigcon.com; 1993 | https://sigcon.com/books/bookHSDD.html |
| pcb/06-signal-integrity/README.md:28 | Right the First Time link "—" | Speeding Edge; Vol I 2003, Vol II 2007 | https://speedingedge.com/product-category/handbook/ ; https://pcdandf.com/pcdesign/index.php/editorial/menu-new-indust-prod/2405-speeding-edge-releases-volume-two-of-high-speed-pcb-and-system-design-handbook |
| pcb/06-signal-integrity/README.md:30 | 🔑 Dr. EMC | no 🔑; flagged unverified | search found only https://www.youtube.com/@DrEMC-sf8rx |
| pcb/06-signal-integrity/README.md:31 | UltraCAD "trace width" | adds "use an IPC-2152 calculator for current" | https://saturnpcb.com/saturn-pcb-toolkit/ |
| pcb/07-emc-and-compliance/README.md:23 | Ott link "—"; "Henry Ott" | DOI; 2009; "Henry W. Ott" | https://api.crossref.org/works/10.1002/9780470508510 |
| pcb/07-emc-and-compliance/README.md:26 | 🔑 Dr. EMC | no 🔑; flagged unverified | as above |
| pcb/07-emc-and-compliance/README.md:27 | ⭐ Noise Reduction Techniques | no ⭐; "not on Rick's list" | local Ricks-Reading-Recommendation.pdf |
| pcb/07-emc-and-compliance/README.md:34 | FCC/CE concept only | + IEC 61326 (EMC) / IEC 61010 (safety) for measurement and lab equipment | https://en.wikipedia.org/wiki/IEC_61010 ; https://en.wikipedia.org/wiki/IEC_61326 |
| pcb/08-multi-layer-and-stackup/README.md:15 | 🔑⭐ Rick stackup lectures | 🔑 | local PDF |
| pcb/08-multi-layer-and-stackup/README.md:17 | Ritchey link "—" | Speeding Edge | https://speedingedge.com/product-category/handbook/ |
| pcb/08-multi-layer-and-stackup/README.md:22, :35 | "Industry standard for PCB stackup design" | generic design standard; §4 materials, §6.4 impedance equations; Rev C note | IPC-2221A TOC (local) ; https://webstore.ansi.org/standards/ipc/ipc2221c2023 |
| pcb/09-dfm-and-fabrication/README.md:18 | "Industry standard for PCB manufacturing" | design-side rules; acceptance = IPC-6012 / IPC-A-600; Rev C note | IPC-2221A scope (local) ; ANSI page |
| pcb/09-dfm-and-fabrication/README.md:20 | jlcpcb.com home page | capabilities page | https://jlcpcb.com/capabilities/pcb-capabilities |
| pcb/11-reference-projects/README.md:16 | "Automotive-grade hardware design" (implies board files) | caveat: panda repo is firmware and software only | https://github.com/commaai/panda |
| pcb/README.md:55–74 | 7-row ⭐ table (one non-list book, 6 list books missing); "the standard curriculum …" | 12 rows in PDF order with groupings; note on Noise Reduction; softened claim | local Ricks-Reading-Recommendation.pdf |
| pcb/README.md:18, :49, :94 | ⭐ legend; "IPC-2221" in documents line and NotebookLM line | "books only"; IPC-2221A (2003, superseded); tutorial author and date | as above |
| pcb/books/README.md:10–16 | years "—"; ⭐ on #10 | 2018 / 1993 / 2009 / 2003–2007 / 2017 / 2017; ⭐ removed from #10 | publisher pages above |
| pcb/PROGRESS.md:55, 56, 88, 99 | ⭐ on two talks, Noise Reduction, stackup lectures | ⭐ removed | local PDF |
| pcb/.agents/skills/update-curriculum/SKILL.md:61–64, 86–97 | example `05-stackup-and-power/`; mapping to 9 non-existent dirs | real directories; ⭐ restricted to the 12 PDF books | repo tree |

## Proposed new sections — both CREATED after approval

Both were appended without renumbering. `pcb/README.md`'s learning path lists them with their recommended positions, and `PROGRESS.md` has a block for each (one checkbox per resource plus the three practice lines). Pointers were added in 05, 09 and 10, and the skill mapping and the books/courses section references were updated. Only resources verified earlier in this run were used; no web calls were made for this step.

### A. Analog, Mixed-Signal & Precision Measurement Design — ✔ created as `pcb/12-analog-mixed-signal-and-precision-measurement/README.md` (take after 05)
- **Position (as proposed):** immediately after 05 (Power & Grounding). Implemented as Section 12 with a "take after 05" note instead of renumbering.
- **Why:** This is the core of precision T&M work (source/measure front ends, ADC/reference layout, guarding, Kelvin sensing, noise). The curriculum had essentially nothing. The interim cluster from Section 10 has now moved here.
- **Outline:**
  1. Op-amp front ends: offset and bias, noise budget (voltage, current, resistor), stability with capacitive loads, input protection and EOS
  2. Precision passives and error budgets: resistor TCR, voltage coefficient and thermal EMF; capacitor dielectric absorption and DC-bias derating (C0G vs. X7R vs. tantalum); voltage references
  3. Data converters: SAR and ΔΣ input drivers, reference drive and decoupling, AGND/DGND, clock jitter
  4. Precision layout: Kelvin/force-sense routing, guard rings and guarded traces, leakage and board cleanliness (SIR, flux, conformal coat), thermal gradients, partitioning without splitting planes
  5. Source-measure architecture: force/sense, compliance and range switching, current measurement (shunts, TIA), PMU/SMU ICs
  6. Instrument grounding and shielding: guard vs. shield vs. ground; cables
  7. Verification: LTspice noise and stability analysis; measuring a noise floor
- **Verified resources:**
  1. *Op Amp Applications Handbook* (Section 7) — Walt Jung (ed.), ADI, 2005 — https://www.analog.com/en/resources/technical-books/op-amp-applications-handbook.html
  2. *Low Level Measurements Handbook*, 7th ed. — Keithley/Tektronix, 2014 — https://download.tek.com/document/LowLevelHandbook_7Ed.pdf
  3. MT-031 Grounding Data Converters — Kester, Bryant, Byrne (ADI), 2008 — https://www.analog.com/media/en/training-seminars/tutorials/mt-031.pdf
  4. TI Precision Labs — Op Amps — https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html
  5. TI Precision Labs — ADCs (SAR/ΔΣ, drive, references, noise, EOS, PCB for EMC) — https://www.ti.com/video/series/precision-labs/ti-precision-labs-analog-to-digital-converters-adcs.html
  6. Mixed-Signal Hardware Design with KiCad — Philip Salmony, 2022 — https://fedevel.com/courses/mixed-signal-hardware-design-with-kicad
  7. *Grounding and Shielding: Circuits and Interference*, 6th ed. — Ralph Morrison, 2016 — https://www.wiley-vch.de/en/areas-interest/engineering/grounding-and-shielding-978-1-119-18374-7
  8. *Linear Circuit Design Handbook* — Hank Zumbahlen (ed.), ADI/Newnes, 2008 (free *Basic Linear Design* chapters incl. Ch. 12 "PCB Design Issues") — https://www.analog.com/en/resources/technical-books/linear-circuit-design-handbook.html

### B. Bring-up, Test & Debug (including Design for Test) — ✔ created as `pcb/13-bring-up-test-and-debug/README.md` (take after 09)
- **Position (as proposed):** after 09 (DFM & Fabrication), since bring-up follows fab. Implemented as Section 13 with a "take after 09" note instead of renumbering.
- **Why:** Bring-up and production test are a large share of a hardware engineer's time, and the curriculum had nothing on them. `software/07` covers only firmware-side debugging (JTAG/SWD with GDB).
- **Outline:**
  1. Bring-up plan: pre-power short checks, current-limited first power, rail sequencing, thermal camera
  2. Probing technique: bandwidth and rise time, probe loading, ground-lead inductance, ripple and noise measurement, current and differential probes
  3. MCU bring-up: SWD connectivity, clocks and HSE start, boot pins, first firmware
  4. DFT: test points (size, pitch, single-side access), boundary scan (IEEE 1149.1), programming connectors, test-mode firmware hooks
  5. Production test: flying probe vs. bed-of-nails, fixtures and pogo pins, Python + SCPI instrument automation, limits, yield and traceability
  6. Debugging methodology and rework
- **Verified resources:**
  1. AN4488 (incl. "troubleshooting a non-working MCU" FAQ) — STMicroelectronics, Rev 7 2018 — https://www.st.com/resource/en/application_note/an4488-getting-started-with-stm32f4xxxx-mcu-hardware-development-stmicroelectronics.pdf
  2. AN2867 Oscillator design guidelines — STMicroelectronics, Rev 24 2026 — https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf
  3. What is JTAG? (boundary-scan primer; exact page title not confirmed, content verified) — XJTAG — https://www.xjtag.com/about-jtag/what-is-jtag/
  4. Design for Test (DFT) Guidelines for improving JTAG testability — XJTAG — https://www.xjtag.com/about-jtag/design-for-test-guidelines/
  5. TI Precision Labs — Op Amps, "Board level troubleshooting" module — https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html
  6. *Debugging* (the "9 rules" book) — Dave Agans — https://debuggingrules.com/ (publisher and year not shown on that page)
  7. IPC-2221A §3.5 "Test Requirement Considerations" (testability, boundary scan, in-circuit test) — included PDF `pcb/documents/IPC-2221A(L).pdf`
  8. *Low Level Measurements Handbook*, 7th ed. (measurement technique) — Keithley, 2014 — https://download.tek.com/document/LowLevelHandbook_7Ed.pdf
- **To verify, then add to Section 13:**
  - Tektronix *ABCs of Probes* primer (tek.com blocked automated fetches)
  - a production-fixture design reference (pogo-pin nests, tooling)
  - PyVISA documentation, for the test-station exercise
  - an open-source boundary-scan tool (e.g., OpenOCD or UrJTAG support)
  - ST BSDL-file availability for the STM32 families in use
  - Bogatin, *Practical Guide to Prototype Breadboard and PCB Design*

  Section 13's practice is written so these slot in without changes.
- **To verify, then add to Section 12:**
  - the ADI/Maxim article on MLCC DC-bias and temperature derating
  - Brooks & Adam, *PCB Trace and Via Currents and Temperatures*
  - an open SMU/PMU-class reference design (none found yet)

### Also recommended, not a new section
- Expand Section 09 into "DFM, Fabrication & Release" to cover:
  - KiCad 10 design variants and BOM management
  - lifecycle checks
  - git + KiBot CI release packages
  - Gerber X2 / IPC-2581 data packs
  - fab notes and assembly drawings
  - ECO/revision control and serial/traceability

  The core tools (kicad-cli, KiBot, KiKit, Gerber spec) were added to 09 in this pass.

## Cut candidates
- **"Practical PCB Design" — Mike D. Smith** (books #2, 🔑): existence unverified, likely hallucinated. Verify or cut.
- **"Tech Explorations KiCad Advanced (BGA, SI, High-Speed)"** (Section 10): no link, and I could not find such a course. Cut unless found.
- **Dr. EMC** (README, 06, 07, courses, PROGRESS): unidentified channel, and the handle mismatches. Replace with LearnEMC (added), or cut after a look.
- **CommaAI hardware** (11, 🔑): no PCB files in its flagship hardware repo. Cut, or demote and keep as an "automotive context" note.
- **Ott, *Noise Reduction Techniques*:** superseded by his own *EMC Engineering*. Keep as optional only.
- **GreatScott!, Khan Academy, Arduino reference designs:** beginner-level, low value for a working professional.
- **Altium Academy "routing", "EMC", "basics" rows:** link to the channel home and duplicate each other. Replace with specific videos or cut.
- **"Rick Hartley — EMC Lectures" / "Stackup Design lectures":** YouTube *search* links. Replace with specific talks.
- **UltraCAD calculators:** overlap with Saturn, and its trace-width basis is not IPC-2152.
- **books #12 "Rick Hartley's Reading Recommendations":** a meta-entry that duplicates the README cross-reference.

## Structural observations
- **Inconsistent schemas.**
  - Section 00 has a Year column; 01–03 do not; 04 has no Author column; 05–07 use emoji type labels; 08–10 use plain labels.
  - "Marking Convention" blocks appear only in 04–07.
  - Prerequisites are sometimes link lists, sometimes plain text ("Sections 05–07").
  - Recommend one schema: `Priority | Type | Resource | Author(s) | Year | Link | Description`.
- **Channel-level links.** About 12 rows link only to a channel home (Phil's Lab, Feranec, Altium Academy) and two to YouTube searches. These are the biggest drag on Focus. Replace them with specific playlists or videos.
- **Link-less 🔑 concepts.** Sections 03 and 09 put 🔑 on concept rows with no resource. Attach a resource or drop the key.
- **Sequencing.**
  - Stackup (08) sits after SI and EMC (06–07), but 05–07 all assume plane pairs and return paths that the stackup sets.
  - Suggest moving 08 to right after 04, or folding a "stackup basics" unit into 05.
- **Copyright exposure.** `documents/IPC-2221A(L).pdf` is a licensed IPC copy (encrypted; front matter: "Any copying, scanning or other reproduction … is strictly prohibited"). If the repo is public, remove it and link to IPC's store instead (https://shop.electronics.org/ipc-2221/ipc-2221-standard-only/Revision-c/english). The Dave Jones tutorial says "Freely distributable for educational and personal use", so it is fine.
- **Overlaps.**
  - (a) `physics/03-electromagnetism` is pure theory (Griffiths, Feynman Vol 2, Lewin) and does not duplicate pcb/06–07. I added an optional prerequisite link from pcb/06. Physics/03 could point back to pcb/06–07 as the applied path. Feynman Vol 2's energy-flow (Poynting) chapters pair well with Morrison's "energy in fields" framing.
  - (b) `software/07-embedded-systems-and-rtos` has a "Debugging embedded systems (JTAG/SWD, logic analyzers, oscilloscopes)" concept. Split the work: pcb owns hardware bring-up, probing, DFT/boundary scan and production test (proposed Section B), and software/07 owns firmware debugging (GDB, OpenOCD, RTT).
  - Not my curriculum, but `software/07`'s prerequisite link `../../software/02-c-fundamentals/README.md` points at a non-existent directory (the real one is `02-embedded-c-mastery`).
- **Agent skill (`pcb/.agents/skills/update-curriculum/SKILL.md`).**
  - ✔ The mapping table pointed at 9 non-existent directories, and the example path was wrong; both now match the real tree.
  - ✔ The ⭐ rule now explicitly restricts ⭐ to the 12 books in the PDF.
  - ✱ Still suggested:
    - add a mandatory verification step: fetch each URL and confirm title, author and year
    - replace "When in doubt … err on the side of inclusion" with a quality bar
    - add KiCad release-notes and IPC revision checks
    - add vendor app-note sources (ADI, TI, ST) to the search list
- **Verification limits this pass.** The shared WebSearch budget (200 per turn) and WebFetch budget (800 per hour) ran out mid-review. These items were therefore **not** added because I could not verify them:
  - Tektronix *ABCs of Probes*
  - Brooks & Adam *PCB Trace and Via Currents and Temperatures*
  - Wyatt & André *EMI Troubleshooting Cookbook*
  - Bogatin *Practical Guide to Prototype Breadboard and PCB Design*
  - Ossmann's "Simple RF Circuit Design" talk
  - Coombs *Printed Circuits Handbook*
  - Holden *HDI Handbook*
  - InteractiveHtmlBom
  - the ADI article on MLCC DC-bias derating
  - IPC-7352 status
  - USB-C (CC/PD) layout notes
  - ST Nucleo design files

  The PDN video's presenter could not be confirmed either (YouTube HTTP 429).

## Top 5 priorities for Aaron in this curriculum
1. **Work through the new Section 12 (Analog, Mixed-Signal & Precision Measurement; take it after 05).** Start with ADI's *Op Amp Applications Handbook* Section 7, then the Keithley *Low Level Measurements Handbook* (guarding, leakage, Kelvin, SMUs) and MT-031. The calibrated error budget (Practice 1) and the characterized precision channel (mini-project) target the day job directly. This was the curriculum's biggest blind spot.
2. **Use the new Section 13 (Bring-up, Test & Debug; take it after 09) on your next board.** Write the bring-up plan before the boards arrive, build the MCU first-contact runbook, and turn the Section 09 DFT plan into the pilot-run test station. Fill its "to verify" gaps (probing primer, fixture reference, PyVISA, boundary-scan tooling) next. software/07 covers the firmware-debugging side.
3. **Treat KiCad as a pipeline, not just an editor.**
   - Adopt KiCad 10 (design variants; design blocks from 9.0).
   - Generate releases with kicad-cli + KiBot in CI; panelize with KiKit; output Gerber X2.
   - **Audit your KiCad toolkit and library scripts for SWIG `import pcbnew`**, which is deprecated since 9.0 and planned for removal in 11.0, and port them to the IPC API / kicad-python.
4. **Fix your mental defaults from the old sources.**
   - Size current-carrying copper with IPC-2152 (Saturn), not the IPC-2221A Fig. 6-4 charts or the 2004 tutorial's table.
   - Don't split ground planes on mixed-signal boards (MT-031, Hartley).
   - Identify the IEC 61326 / IEC 61010 obligations for measurement equipment before the first layout.
5. **Clean up the reading list.**
   - Read the newly added Rick-list books selectively: Archambeault for board-level EMI, and Morrison's *Grounding and Shielding* for instrument grounding and guarding.
   - Verify or cut the suspect entries ("Practical PCB Design", Tech Explorations course, Dr. EMC).
   - Replace channel-home and YouTube-search links with specific talks.
   - Resolve the copyright exposure of the bundled IPC-2221A PDF if the repo is public.

## Follow-up pass (2026-10-13)
- **New sections created:** none (Sections 12 and 13 already exist).
- **Added:**
  - Temperature and Voltage Variation of Ceramic Capacitors, or Why Your 4.7µF Capacitor Becomes a 0.33µF Capacitor (Maxim AN5527) — Maxim Integrated, now hosted by Analog Devices (no author named on the page) — 2012 — Section 03
  - J-STD-048A Notification Standard for Product Discontinuance · J-STD-046A Customer Notification Standard for Product/Process Changes by Electronic Product Suppliers — JEDEC/ECIA/IPC joint standards — 2025 — Section 03 (also blogs-and-references Standards)
  - FastHenry2 — Mattan Kamon (MIT, original FastHenry); FastFieldSolvers S.R.L. (Windows port) — ongoing — Section 05 (also blogs-and-references Tools)
  - J-SMU (DIY source-measure unit) — GitHub user jaromir-sukuba — 2020–2021 — Section 11, cross-referenced from Section 12 (Also used here, Suggested Order 6, Practice 4)
  - *ABCs of Probes* primer (60W-6053-17) — Tektronix — year not shown on the page — Section 13
  - JTAG Boundary Scanner — Viveris — ongoing (no releases listed) — Section 13 (also blogs-and-references Tools)
  - Design Guidelines for In-Circuit Testability (technical paper) — JJS Manufacturing — undated — Section 13
  - KiCad Advanced: Design a smart USB thumb drive — Tech Explorations — 2026 — courses/ row 16 (the Section 10 row already existed; now verified)
  - Cross-references only, no duplicate rows: PyVISA and SCPI → `software/13` from pcb/12 (mini-project) and pcb/13 (Also used here, mini-project); *Op Amp Applications Handbook* Section 7 (precision passives) → Section 03 "Also used here"
- **Removed (confirmed nonexistent):** none. All three suspect entries exist.
- **Flags resolved:**
  - pcb/books/README.md:8, PROGRESS.md:220 — "Practical PCB Design" (Mike D. Smith) — real: *Practical PCB Design: From Breadboard to Production*, No Starch Press, October 2026, 272 pp., ISBN 9781718504042 (examples in Altium CircuitMaker) — row completed, "(unverified…)" note removed — https://nostarch.com/practical-PCB-design
  - pcb/10-advanced-topics/README.md:27, :50 — "Tech Explorations KiCad Advanced (BGA, SI, High-Speed)" — real: the course at that URL slug is headed "KiCad Advanced: Design a smart USB thumb drive" (KiCad 10; 9 sections, 94 lectures; BGA and via-in-pad, USB 2.0 SI, eMMC length matching, stackup/impedance; no instructor named) — row and step rewritten, note removed, courses/ row added — https://app.techexplorations.com/courses/kicad-advanced-bga-signal-integrity-and-high-speed-layout/
  - pcb/06:39, :52; pcb/07:35, :50; pcb/README.md:88; pcb/courses/README.md:13 — Dr. EMC — the linked `@DrEMC` handle belongs to an unrelated personal channel ("Andre Mclean"); the real "Dr. EMC" channel is `@DrEMC-sf8rx`, presented by Anton Tichenko (About page: principal electronics design engineer, PhD research at the University of Surrey's 6G Innovation Centre; electromagnetics and EM compliance) — links fixed, presenter named, unverifiable content claims ("excellent visual explanations", "simulation") replaced with the About-page description, notes removed — https://www.youtube.com/@DrEMC-sf8rx ; https://www.youtube.com/@DrEMC
  - independent-check pcb/05:66 (FastHenry not listed) — FastHenry2 tool row added (05:44) and Suggested Order step 11; Practice 3 (05:68) points to it and stays optional — https://www.fastfieldsolvers.com/software.htm
  - independent-check pcb/05:34, books:14, PROGRESS:73 (now :75) — *Fast Circuit Boards* year — Wiley hardcover is 2018 (ISBN 9781119413905); the e-book is dated 15.12.2017 (ISBN 9781119413929) — 2017 → 2018 in all three, with the e-book date noted in books/ — https://www.abebooks.com/9781119413905/Fast-Circuit-Boards-Energy-Management-1119413907/plp ; https://wiley-vch.e-bookshelf.de/fast-circuit-boards-10620117.html
  - independent-check pcb/02:25 and the other KiCad-version claims — checked against the release notes: 10.0 (2026-03-20) adds design variants, the graphical rule editor, PCB design blocks ("extended the Design Blocks feature to the PCB editor", so pcb/04:64 is right) and time-domain tuning constraints (pcb/06:71 right); 9.0 (2025-02-20) added schematic design blocks, multichannel, creepage DRC, jobsets and the IPC API; the SWIG bindings are deprecated as of 9.0 and "the current plan is to remove the SWIG bindings in KiCad 11.0" (pcb/10:36 right) — no change needed — https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/ ; https://www.kicad.org/blog/2025/02/Version-9.0.0-Released/ ; https://dev-docs.kicad.org/en/apis-and-binding/pcbnew/
  - independent-check pcb/04:60 — "Rev C (2023) updated the clearance guidance" — what 2221C changed in Table 6-1 can't be checked without buying the standard — reworded to "check them against the current revision, IPC-2221C (2023), before relying on them"
  - independent-check pcb/04:61 — place-only study budget ~5 h → ~10 h ("three placements plus one full route"), within the checker's 8–12 h
  - independent-check pcb/05:5 — superlatives softened: "the #1 cause" → "one of the most common causes"; "has saved more PCB designs than any other single resource" → "is the best single place to start"
  - independent-check "several (pcb 04, 09)", more than 3 🔑 — trimmed to 3 each: 🔑 removed from the KiCad PCB Editor Guide (04:34, a tool manual) and from the link-less "Gerber file generation and review" concept (09:25)
  - independent-check "various (pcb/00:23–24, pcb/04:36)" — spot-checked, all correct, no change: x-Chapters "NEW EXPANDED 2nd EDITION summer 2026! … new 100+ page chapter 'Sensors'" (https://x.artofelectronics.net/); LAoE 2nd ed. (Cambridge link slug on https://artofelectronics.net/); AN2867 Rev 24, February 2026, §7.1 "PCB design guidelines" (https://www.st.com/resource/en/application_note/an2867-guidelines-for-oscillator-design-on-stm8afals-and-stm32-mcusmpus-stmicroelectronics.pdf)
  - independent-check STUDY-GUIDE.md:121 (inconsistent "(unverified…)" markers, pcb only) — pcb no longer carries any such marker; STUDY-GUIDE itself was out of scope
  - pcb/07:43, pcb/blogs-and-references/README.md:65 — IEC 61326/61010 statements — confirmed at the IEC webstore: IEC 61326-1 "Electrical equipment for measurement, control and laboratory use – EMC requirements – Part 1" (2012 ed. withdrawn 2020-10-26 for the 2020 ed.); IEC 61010-1:2010 ed. 3.0 (+AMD1:2016) "Safety requirements for electrical equipment for measurement, control, and laboratory use – Part 1" — statements correct; Wikipedia link replaced with the IEC page and editions added — https://webstore.iec.ch/en/publication/5275 ; https://webstore.iec.ch/en/publication/4279
  - This file's "To verify" lists (Proposed new sections A and B, and the Section 03 note) — ABCs of Probes, a production-fixture reference (JJS), a boundary-scan tool (Viveris) and PyVISA (cross-reference) went to 13; the ADI/Maxim MLCC article went to 03, the home for derating, which 12 already lists as a prerequisite; an open SMU design (J-SMU) went to 11, the home for open designs, with cross-references from 12
  - pcb/02:29, pcb/blogs-and-references/README.md:24 — KiCAD_Template_Snyder returns 404 publicly — "(private repo — link works when signed in)" added; this session couldn't query the GitHub API for it
- **Still unverified:**
  - J-STD-048A's current notice windows — only the superseded JESD48C (6 months to final order, 12 months to final shipment) was readable; 048A needs JEDEC registration. The row says so.
  - Author of Maxim AN5527 — not named on the ADI page.
  - Presenter of the PDN video WnLRHuvl6Eg (Section 05) — oEmbed gives "Power Distribution Network" on NineDotConnects; the watch page returned HTTP 429, so Rick Hartley as presenter is still unconfirmed.
  - KiCAD_Template_Snyder — private vs renamed is for Aaron to confirm.
  - Considered, not added: UrJTAG (urjtag.org and SourceForge code pages block automated fetches, so BSDL and cable support couldn't be confirmed); ADALM1000 (verified at analog.com as an open-source-hardware SMU-style learning module, 0–5 V / ±200 mA, but J-SMU is closer to precision SMU work); OpenFixture (exists, but its README cites OpenSCAD ≥ 2015.03 and Ubuntu 14.04 and drives KiCad's old Python scripting interface).
  - Not attempted (outside this pass's backlog): ST BSDL availability for the STM32 families in use; Brooks & Adam; Bogatin's *Practical Guide to Prototype Breadboard and PCB Design*; Wyatt & André; Ossmann's RF talk; Coombs; Holden; InteractiveHtmlBom; IPC-7352 status; USB-C layout notes; ST Nucleo design files; the GreatScott! handle.
  - Rate limits: the Crossref works query for *Fast Circuit Boards* and the YouTube watch page above returned HTTP 429 and were not refetched.

## Link-audit fixes (2026-10-13)
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| pcb/00-electronics-fundamentals/README.md:26 ; pcb/courses/README.md:15 | GreatScott! at `youtube.com/@greatscaboratory` (no such channel) | `youtube.com/@greatscottlab` (link text and URL) | https://www.youtube.com/@greatscottlab |
| pcb/02-schematic-capture/README.md:28 ; pcb/blogs-and-references/README.md:44 | SamacSys at `samacsys.com` (302 redirect; SamacSys is now part of Supplyframe) | `supplyframe.com/samacsys` (link text and URL) | https://supplyframe.com/samacsys |
| pcb/11-reference-projects/README.md:30 | Raspberry Pi Hardware → `datasheets.raspberrypi.com` (302 redirect) | `pip.raspberrypi.com` (Raspberry Pi Product Information Portal); link text "Datasheets" kept | https://pip.raspberrypi.com/ |
- Already fixed in the follow-up pass above: Dr. EMC (`@DrEMC` → `@DrEMC-sf8rx`, presenter Anton Tichenko) in 06, 07, README and courses/.
- Left unchanged because the auditor could not load the page: the two 🔑 Rick Hartley YouTube *search* links (07:33 EMC lectures, 08:26 stackup lectures; replacing them with specific talks is still the ✱ above), NotebookLM (README:9, sign-in app), and Arduino reference designs (11:29), whose old URL now redirects to a "retired / older boards" docs page.

## Tier lists (2026-10-13)
No pcb section had more than 3 🔑 resource rows (36 in all; 04 and 09 were trimmed in the follow-up pass above; 10 has 1, 01, 03, 12 and 13 have 2, the rest 3), so no 🔑 was removed and the index files are unchanged; each Suggested Order (00–13) now opens with a "Core path (🔑)" line naming the section's 🔑 items in reading order.

- books/README.md #20 Keithley, *Low Level Measurements Handbook* (7th ed): 🔑 added (core in 12)
- pcb/README.md legend: 🔑 row now reads "**Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line"
- pcb/README.md legend: 🔑⭐ row now says "a core-path item" instead of "a must-read"
- pcb/README.md Key Educators: Dr. EMC removed (not core in any section; unmarked in 06 and 07)
- pcb/README.md Key Educators: Altium Academy removed (not core in any section; unmarked in 01, 04 and 07)
- Not changed, for Aaron: courses/README.md #8 KiCad Official Documentation stays unmarked. No section lists the docs as a whole, but one part, the KiCad Getting Started Guide, is core in 02. Add 🔑 if a part counts.
- Second check (2026-10-13): `books/README.md` #12 Rick Hartley's Reading Recommendations: 🔑 removed (index-only; the ⭐ marks on the 12 books carry his list).
- Final decisions (2026-10-13):
  - 02: the KiCad Library Conventions (KLC) made core in place of the private KiCad template, which stays as a personal reference.
  - The template repo is private: anonymous requests get 404 with no redirect, and the account's only public repo is `isi_openmv`.
  - The template's 🔑 in blogs-and-references was removed.
  - The update skill now says "at most 3".
- Final pass: `pcb/README.md`'s "Key Educators" is renamed "Educators Worth Following" and marked as a highlights list, separate from the core paths. EEVblog stays on it, although it is no longer core in Section 00: Section 00's core path now names the four *Art of Electronics* chapters its objectives use (1, 4, 5 and 8).
- Final pass, core paths:
  - 08 now starts from a concrete talk instead of a YouTube search: Hartley's *The Extreme Importance of PC Board Stack-Up* (AltiumLive, 2018; Altium page checked).
  - 07's search-link row is no longer core. LearnEMC → Ott carry the core path, and Hartley's grounding talk in 05 is the suggested warm-up.
  - 10 adds TI AN-2020 (thermal design) to Feranec's BGA series, so the core path is not a single channel link.
