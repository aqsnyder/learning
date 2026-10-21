# Pass 2 log: pcb 00–06 and curriculum-level files (pcb-A)

Date: 2026-10-21. Scope: `pcb/00`–`pcb/06`, plus `pcb/README.md`, `pcb/extras.toml`, the hand-written parts of
`pcb/books/README.md` and `pcb/courses/README.md`, `pcb/documents/README.md` and `pcb/blogs-and-references/README.md`.

## How verification worked this run

- YouTube: every video or playlist was checked with the oEmbed record (title and channel). oEmbed gives no upload
  date, and watch pages, channel RSS and mirrors were refused, so video years were taken only from the creator's own
  dated pages (Feranec's FEDEVEL blog). The other video years are in "For a browser check".
- WebFetch only accepted URLs that had appeared in a search or fetch result in this run (others came back
  `PROVENANCE_REQUIRED`), and the shared WebSearch budget ran out after 24 searches. Pages that only appear in the
  repo (analog.com, st.com, jedec.org, saturnpcb.com, cambridge.org, khanacademy.org, ti.com course pages and most
  blogs-and-references links) could not be opened. Items on those hosts kept their 2026-10-13 dates, and any field
  I filled without a fetch is marked "no fetch" below.
- IPC-2221A section numbers were checked against the copy removed in pass 1, read from git history (`git show`,
  read-only, nothing extracted into the repo). The Hartley ⭐ table was checked the same way against the removed
  handout: the twelve books and their order match.
- Local file: `pcb/documents/PCBDesignTutorialRevA.pdf` was read in full ("PCB Design Tutorial", David L. Jones,
  Revision A, June 29th 2004, "Freely distributable for educational and personal use").

## 1. Changes

| Section | Item (id) | Change | Evidence URL |
|---|---|---|---|
| 00 | the-art-of-electronics-3rd-ed | Description de-hyped; names the chapters used; x-Chapters claim dated "as of October 2026" | (unchanged URL; 2026-10-13 check) |
| 00 | learning-the-art-of-electronics | access paid, level beginner; description tidied; still shares the AoE URL (see browser check) | no fetch (artofelectronics.net refused) |
| 00 | eevblog | Channel home replaced by #859 (main) + #33 part 2 + #453; type video-series, label Videos; level; description | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=BcJ6UdDx1vg&format=json (also TDDoi70cxw0, OiAmER1OJh4) |
| 00 | greatscott | Channel home replaced by GreatScott!'s own "Electronic Basics" playlist; authors GreatScott!; level; description. A third-party playlist with a similar name was rejected | https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLAROrg3NQn7cyu01HpOv5BWo217XWBZu0&format=json |
| 00 | khan-academy-electrical-engineering | authors Khan Academy (site name, no fetch); level beginner; description | no fetch |
| 00 | mit-6-002-circuits-and-electronics-ocw | level intermediate; description | (2026-10-13 check) |
| 00 | practical-electronics-for-inventors | Description only; link and year still missing | no fetch |
| 00 | ti-precision-labs-op-amps | access free, level intermediate; description de-hyped | no fetch (ti.com page refused) |
| 00 | ltspice | access free | (2026-10-13 check) |
| 01 | pcb-design-tutorial-rev-a-2004 | Title "*PCB Design Tutorial*, Revision A"; authors David L. Jones; access free; description; verified | local PDF, read in full |
| 01 | nine-dot-connects | Deleted: home-page link (was core); still listed in blogs-and-references | — |
| 01 | pcb-materials-guide-fr-4-rogers-etc | No-link row turned into Yogendrappa, *PCB Material Selection: Electrical and Manufacturing Considerations* (Sierra Circuits, 2021); core | https://www.protoexpress.com/blog/pcb-material-selection-electrical-manufacturing-considerations/ |
| 01 | laminate-data-sheets-370hr-ro4350b | Added (core): Isola 370HR data sheet (Rev C, April 2021) + Rogers RO4350B page | https://www.isola-group.com/wp-content/uploads/data-sheets/370hr.pdf , https://www.rogerscorp.com/advanced-electronics-solutions/ro4000-series-laminates/ro4350b-laminates |
| 01 | sierra-circuits-pcb-knowledge-base | Blog home replaced by the KB entry "Copper for PCBs" (copper weights, foil types, IPC-2221 constants); type docs | https://www.protoexpress.com/kb/copper-for-pcbs/ |
| 01 | ipc-4101-slash-sheets-sierra | Added: Sushmitha V, *How to Choose PCB Laminates Based on IPC Standards* (2025) + Isola's /126 page | https://www.protoexpress.com/blog/how-to-choose-pcb-laminates-based-on-ipc-standards/ , https://www.isola-group.com/pcb-laminates-prepreg/slash-sheets/126-2/ |
| 01 | sierra-laminates-for-fabrication | Added: Amit Bahl, *How to Choose PCB Laminates and Materials for Fabrication* (2020), for Objective 1 | https://www.protoexpress.com/blog/comparing-the-manufacturability-of-pcb-laminates/ |
| 01 | altium-academy-basics | Channel home replaced by "Do You Need Low Dk PCB Materials?" (Altium Academy); type video | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=F-CIJDsTwwE&format=json |
| 01 | kicad-calculator-tools | Added: KiCad 10 Calculator Tools manual, the free route to IPC-2221 track width, spacing and TransLine | https://docs.kicad.org/10.0/en/pcb_calculator/pcb_calculator.html |
| 01 | ipc-2221-generic-standard-on-printed | Kept as the home row (also in pcb/08, pcb/09); description says no copy is bundled and names the free routes; "current revision C" dated | https://resources.altium.com/p/using-an-ipc-2221-calculator-for-high-voltage-design (confirms Rev C, 2023) |
| 02 | kicad-getting-started-guide-kicad-10 | Real title "Getting Started in KiCad"; authors from the document; year 2026; type tutorial; KiCad 10.0 release date and current point release dated | https://docs.kicad.org/10.0/en/getting_started_in_kicad/getting_started_in_kicad.pdf , https://www.kicad.org/blog/2026/03/Version-10.0.0-Released/ , https://www.kicad.org |
| 02 | phil-s-lab-schematic-design-tutorials | Channel home replaced by Phil's Lab #165 (KiCad 9, schematic part); type video | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=O-zNn5k5Bn4&format=json |
| 02 | kicad-template-with-altium-theme | Deleted: link to the owner's private repository | — |
| 02 | kicad-project-templates | Added: KiCad 10 manual, "Project templates" | https://docs.kicad.org/10.0/en/kicad/kicad.html |
| 02 | kicad-schematic-editor-manual | Added: KiCad 10 Schematic Editor manual (ERC, power symbols, labels, hierarchy) | https://docs.kicad.org/10.0/en/eeschema/eeschema.html |
| 02 | snapeda-component-library, ultra-librarian, samacsys | authors from the site name (SamacSys: Supplyframe, from its URL); access free; vendor claim "Verified symbols" removed | no fetch |
| 02 | robert-feranec-schematic-review-series | Channel home replaced by "How to Draw Schematic & Tips to Improve Schematic" Parts 1–3 (June 2019) + "10 Tips for Better Schematic Checking"; year 2019; type video-series | oEmbed for lF0UgVQnZ5M, Rfsq0EwJ5Xs, qJd_BMDNfrk, LzlAmPy0VNQ; dates: https://courses.fedevel.com/blog/how-to-draw-schematic-tips-to-improve-schematic-checking-pin-connections-part-2 |
| 02 | an4488-getting-started-with-stm32f4xxxx | access free | (2026-10-13 check) |
| 03 | digikey-mouser-parametric-search | authors DigiKey; Mouser Electronics (site names); access free; description | no fetch |
| 03 | temperature-and-voltage-variation-of | authors "Maxim Integrated (now Analog Devices)" (from the checked title and description); access free; now core | (2026-10-13 check) |
| 03 | j-std-048a-notification-standard-for | authors JEDEC (048A jointly with ECIA and IPC) and year 2025, both from the checked title and description; access free (registration); now core | (2026-10-13 check) |
| 03 | octopart, jlcpcb-parts-library | authors from the site name; access free; descriptions | no fetch |
| 03 | phil-s-lab-component-selection-guides | Channel home replaced by Phil's Lab #114 (MLCC basics) + #71 (sponsored, regulator parts) | oEmbed for kUruN6WBgSw, FqT_Ofd54fo |
| 03 | phil-s-lab-qfn-pcb-design-tips | Added: Phil's Lab #144, QFN PCB design tips (Objective 4) | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=hOamoJ15hmA&format=json |
| 03 | jedec-standards-overview | Deleted: no link and no verifiable source this run; package reading moved to prose and Practice 1 | — |
| 03 | design-for-supply-chain | Deleted concept row (was core): moved to Suggested Order prose; no non-promotional source found | rejected: https://resources.altium.com/p/your-bill-of-materials-decides-your-e-waste-launch (podcast, promotional) |
| 04 | phil-s-lab | Channel home replaced by Phil's Lab #166 (KiCad 9, PCB part); type video | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=igQWdVGZGpI&format=json |
| 04 | robert-feranec | Channel home replaced by "How To Improve Your PCB Layout - Routing & Space" + "Review of a PCB Layout (Part 1 of 4)" | oEmbed for YRDZ2Vn_6J4, HZVod5AFrVI |
| 04 | kicad-pcb-editor-guide-kicad-10 | Real title, authors from the manual, year 2026, type docs; chapter links (design rules, custom rules, DRC, zones, differential pairs, length tuning); now core | https://docs.kicad.org/10.0/en/pcbnew/pcbnew.html |
| 04 | kicad-6-stm32-pcb-design-full-tutorial | authors Phil's Lab; "(2022)" moved out of the title; level | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=aVUqaB0IMh4&format=json |
| 04 | an2867-guidelines-for-oscillator-design | "— STMicroelectronics" moved from title to authors; year 2026 from the checked title; access free | (2026-10-13 check) |
| 04 | ipc-2221-clearance-calculator-peterson | Added: Zachariah Peterson, IPC-2221 clearance calculator article (free route to Table 6-1) | https://resources.altium.com/p/using-an-ipc-2221-calculator-for-high-voltage-design |
| 04 | altium-academy | Channel home replaced by "Microcontroller-Based Hardware Design With Altium Designer - #9 PCB Routing Tips" | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=CaGzxD0jCKM&format=json |
| 04 | component-placement-strategy | Deleted concept row (was core): placement principle moved to Suggested Order step 3 | — |
| 04 | design-rule-check-drc | Deleted concept row: covered by the PCB Editor manual's design-rule chapters | — |
| 04 | copper-pours-and-fills | Deleted concept row: covered by the PCB Editor manual's zones chapter and KiCad TransLine | — |
| 05 | how-to-achieve-proper-grounding | De-hyped description; level; verified (oEmbed title names Rick Hartley, channel Altium) | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=ySuUZEjARPY&format=json |
| 05 | power-distribution-networks | Title corrected to "Power Distribution Network" (as published); level; description. Speaker not re-confirmed (oEmbed names only the NineDotConnects channel), so verified stays 2026-10-13 | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=WnLRHuvl6Eg&format=json |
| 05 | phil-s-lab-power-design-tutorials | Channel home replaced by Phil's Lab #60, "Switching Regulator PCB Design" | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=AmfLhT5SntE&format=json |
| 05 | saturn-pcb-design-toolkit | authors from the tool name (no fetch); access free; description names the calculators this section uses (conductor current per IPC-2152; via) and points to Section 08 for impedance | no fetch |
| 05 | ipc-2152-standard-for-determining | access paid; description says IPC sells it and the link is a release note | (2026-10-13 check) |
| 05 | mt-101, mt-031, an-136, fasthenry2 | access free; MT-101 and MT-031 descriptions absorb the deleted concepts | (2026-10-13 check) |
| 05 | decoupling-capacitor-placement-and | Deleted concept row: MT-101 covers it | — |
| 05 | ground-plane-splits | Deleted concept row: MT-031 and Hartley's grounding talk cover it | — |
| 06 | signal-and-power-integrity-simplified, high-speed-digital-design-a-handbook-of | Descriptions de-hyped ("THE most approachable", "bible") | (2026-10-13 check) |
| 06 | right-the-first-time-vols-i-and-ii-2003 | Kept as the home row (also in pcb/08); description notes the reuse | (2026-10-13 check) |
| 06 | robert-feranec-signal-integrity-and-high | Channel home replaced by three Bogatin interviews on Feranec's channel: reflections, crosstalk, differential pairs | oEmbed for vFRtFiDz9wM, EF7SxgcDfCo, pXSK9KlNsW4 |
| 06 | high-speed-interface-layout-guidelines, ethernet-phy-pcb-design-layout-checklist | access free | (2026-10-13 check) |
| 06 | ultracad-calculators | authors from the site name (no fetch); access free | no fetch |
| 06 | dr-emc | Deleted (channel home, no verifiable specific video); outro points to Section 07 | rejected candidates: oEmbed for CDqref32tPU, CRKWvvkNcTY, qvCr0iI1hLM (other channels) |
| 06 | controlled-impedance, differential-pairs | Deleted concept rows: covered by Bogatin, the differential-pair video, SPRAAR7 and the KiCad manual (Section 04); stackups are Section 08's | — |
| 06 | return-paths-and-reference-planes | Deleted concept row: Hartley's grounding talk (Section 05), via the outro and Suggested Order step 3 | — |
| extras | kicad-official-documentation | type docs; description dated (10.0.7 current as of October 2026); verified | https://docs.kicad.org/ , https://www.kicad.org |
| README | ⭐ cross-reference | Says the handout is gone and the table is the reference; superlatives removed | handout read from git history |
| README | NotebookLM step 2 | Removed the instruction to upload the bundled IPC-2221A PDF (no longer included) | — |
| blogs | Your KiCad Template | Deleted (private repository) and replaced by a "KiCad project templates" row | https://docs.kicad.org/10.0/en/kicad/kicad.html |
| blogs | FEDEVEL | Link changed to the platform that loads: courses.fedevel.com | https://courses.fedevel.com/ |
| blogs | KiCad, Altium, Saturn, Sierra rows; IPC standards row | KiCad's current release dated; Altium renamed "Learning Hub"; Saturn's calculators named; "IPC-2221 at Rev C" dated | https://www.kicad.org , https://resources.altium.com/ , https://www.protoexpress.com/blog/ |

Section prose, not item rows: Core path lines were updated in 01–06. "Your template" wording became generic in
01 (mini-project) and 02 and 04 (Practices). Every exercise source note now names a listed resource or the section
that lists it, and each paid-only IPC citation now offers a free route or says the paid standard is needed:
01 Practices 1–4, the 01 mini-project, 01 Q6, 04 Practice 2 and 06 Practice 2. The Check Yourself questions changed as follows:

- 00 Q5 now covers Kelvin connections.
- 01 has a new slash-sheet question.
- 02 has a new kicad-cli CI question.
- 03 Q5 now uses AN5527's case-size data instead of repeating 00's 10 µF/6.3 V/0603 question (open review flag), and 03 has a new package-drawing question.
- 05 has a new hot-loop overshoot question.
- 06 Q3 adds series termination, and 06 has a new fab impedance-table question.

## 2. Coverage (objective → resource / exercise / question)

🔑 marks a core item. "Sxx" means the resource is listed in Section xx.

**pcb/00**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Real capacitor C–ESR–ESL, SRF, anti-resonance | AoE Ch. 1 🔑, EEVblog #859/#33, LTspice | P2, mini-project | Q2, Q3 |
| t_r = 2.2RC, t_r·f_3dB, what scope and probe resolve | AoE Ch. 1 🔑, MIT 6.002, EEVblog #453 | P1 | Q1, Q7 |
| DC error budget at a high-Z node; Kelvin and guard | AoE Ch. 5 🔑, LAoE 🔑, TI Precision Labs | P3 | Q4, Q5 |
| Op-amp input noise by hand and with SPICE | AoE Ch. 8 🔑, TI Precision Labs, LTspice | P4 | Q6 |

**pcb/01**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Multilayer fabrication steps and the rules they create | Tutorial 🔑, Bahl (laminates for fabrication) | P4, mini-project | Q1, Q7, Q9 |
| Copper thickness, sheet R, IPC-2221 current, why IPC-2152 | Tutorial 🔑, Copper for PCBs, KiCad Calculator Tools, IPC-2221, IPC-2152 and Saturn (S05) | P1, P2 | Q2, Q3 |
| Laminate choice from data sheets; slash sheet | Material Selection 🔑, 370HR/RO4350B 🔑, slash-sheet article, low-Dk video | P3, mini-project | Q4, Q5, Q6, Q8 |
| Critique a legacy design guide | Tutorial 🔑, Hartley and MT-031 (S05) | P4 | Q3, Q6 |

**pcb/02**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Library architecture and fields | KLC 🔑, Getting Started 🔑 | P1, mini-project | Q3, Q4 |
| ERC configured to mean something | Getting Started 🔑, Schematic Editor manual | P2 | Q1, Q2, Q5 |
| Audit vendor models | SnapEDA, Ultra Librarian, SamacSys, KLC 🔑 | P1 | Q4 |
| Hierarchical schematic as a review document | Phil's Lab #165 🔑, Schematic Editor manual, Feranec series, AN4488 | P3 | Q6, Q7, Q9 |
| kicad-cli in CI | kicad-cli (S09), project templates | P4, mini-project | Q8 |

**pcb/03**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Precision part selection to max specs | DigiKey/Mouser 🔑, AoE Ch. 5 and TI Precision Labs (S00) | P3 | Q1, Q2 |
| Effective values in circuit | AN5527 🔑, Phil's Lab #114, Op Amp Applications Handbook (S12) | P2, P3 | Q2, Q5, Q6 |
| Supply-chain risk and substitution policy | J-STD-048A/046A 🔑, DigiKey/Mouser 🔑, Octopart, JLCPCB | P4, mini-project | Q3, Q4, Q7, Q9 |
| Package names and outline drawings | Phil's Lab #144, JLCPCB, datasheet drawings (no core item) | P1 | Q8 |

**pcb/04**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Placement from current loops and sensitivity | Phil's Lab #166 🔑, Feranec 🔑, #65, AN2867, AN-136 (S05) | P3 | Q1 |
| Fab capabilities and constraints as DRC rules | PCB Editor manual 🔑, Peterson clearance article, KiCad Calculator (S01), JLCPCB (S09) | P2 | Q2 |
| Kelvin and guard structures | AoE Ch. 5 (S00, core there), S12 resources, AN2867, PCB Editor manual 🔑 (custom rules) | P4, mini-project | Q4, Q5 |
| Copper pours used deliberately | PCB Editor manual 🔑 (zones), KiCad TransLine (S01) | P1 | Q3, Q6, Q7, Q8 |

**pcb/05**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Return current at DC and HF; fields view | Hartley grounding 🔑, Morrison (both books) | P1 | Q1, Q2, Q9 |
| Target impedance and decoupling network | PDN talk 🔑, Smith & Bogatin, MT-101, LTspice (S00) | P2, mini-project | Q3, Q4, Q6 |
| Mounted loop inductance | Smith & Bogatin, MT-101, Saturn via calculator, FastHenry2 | P3 | Q5 |
| Switching-regulator hot loop | Phil's Lab #60 🔑, AN-136 | P4 | Q8 |
| When (not) to split ground | Hartley grounding 🔑, MT-031, Morrison | P1, mini-project | Q7 |

**pcb/06**

| Objective | Resource | Exercise | Question |
|---|---|---|---|
| Electrically long lines; reflections; lattice diagram | Bogatin 🔑, reflections video 🔑, Black Magic 🔑 | P1 | Q1, Q3, Q5 |
| Impedance by closed form and 2D solver | Bogatin 🔑, UltraCAD, KiCad TransLine (S01), Saturn (S08) | P2 | Q2, Q4, Q9 |
| Terminations | Black Magic 🔑, Bogatin 🔑, SPRAAR7, SNLA387 | P1, P4 | Q3 |
| Crosstalk to spacing rules | Bogatin 🔑, crosstalk video 🔑, Black Magic 🔑, Ritchey | P3 | Q7 |
| Specify impedance and pairs to fab and KiCad | Differential-pair video 🔑, SPRAAR7, SNLA387, PCB Editor manual (S04) | P4, mini-project | Q8 |

Question counts: 00: 8, 01: 9, 02: 9, 03: 9, 04: 8, 05: 9, 06: 9.

## 3. For a browser check

| Item (id) | URL | Why |
|---|---|---|
| 00 learning-the-art-of-electronics | https://artofelectronics.net/ | Still shares the AoE URL (the brief asked for its own page). Find the publisher's page for the current edition, check the "2nd edition is available" claim and set year. WebFetch refused the site. Until fixed, the books index merges LAoE into the AoE entry |
| 00 the-art-of-electronics-3rd-ed | https://x.artofelectronics.net/ | Re-check the x-Chapters 2nd-edition claim (dated October 2026 from the 2026-10-13 check) |
| 00 practical-electronics-for-inventors | — | No link: the publisher's page for the current edition, and its year |
| 00 khan-academy-electrical-engineering | https://www.khanacademy.org/science/electrical-engineering | Year (if the course states one); author set to the site name without a fetch |
| 00 ti-precision-labs-op-amps | https://www.ti.com/video/series/precision-labs/ti-precision-labs-op-amps.html | Year; confirm access free |
| Video years (oEmbed has none) | 00 eevblog; 01 altium-academy-basics; 02 phil-s-lab-schematic-design-tutorials; 03 phil-s-lab-component-selection-guides, phil-s-lab-qfn-pcb-design-tips; 04 phil-s-lab, robert-feranec, altium-academy; 05 how-to-achieve-proper-grounding, phil-s-lab-power-design-tutorials; 06 robert-feranec-signal-integrity-and-high | Upload year from each watch page |
| 05 power-distribution-networks | https://www.youtube.com/watch?v=WnLRHuvl6Eg | Confirm the speaker is Rick Hartley and the year (the NineDotConnects channel posted it) |
| 05 an-136-pcb-layout-considerations-for-non | https://www.analog.com/en/resources/app-notes/an-136.html | Year |
| Authors set from site names, no fetch | 02 snapeda, ultra-librarian, samacsys; 03 digikey/mouser, octopart, jlcpcb; 05 saturn; 06 ultracad | Confirm company names |
| 03 (deleted) JEDEC standards overview | — | Candidates to restore a sourced package-naming row for Objective 4: JEDEC JESD30 (package designation) and JEP95 (registered outlines); not verified this run |
| 02 Practice 4 | https://docs.kicad.org/10.0/en/cli/cli.html | The fetched text confirmed `pcb drc --exit-code-violations` and `jobset run`, but not the `sch erc` section |
| extras practical-pcb-design-from-breadboard-to | https://nostarch.com/practical-PCB-design | Not verified (no provenance) |
| extras complete-pcb-design-using-orcad | — | No link or year |
| blogs-and-references | ninedotconnects.com, learnemc.com, analog.com (handbook, LTspice), saturnpcb.com, ultracad.com, jrainimo.com, github.com (KiBot, gerber2ems, viveris), yaqwsx.github.io/KiKit, openems.de, fastfieldsolvers.com, snapeda.com, ultralibrarian.com, supplyframe.com/samacsys, jlcpcb.com, pcbway.com, oshpark.com, ucamco.com, webstore.iec.ch, jedec.org/node/8470 | Not fetched (no provenance). Verified this run: resources.altium.com, protoexpress.com/blog, courses.fedevel.com, kicad.org, docs.kicad.org |
| 06 Dr. EMC | https://www.youtube.com/@DrEMC-sf8rx | No specific video could be found or verified; the pcb/07 row is now its only home |

## 4. Decisions for the owner

1. **Dr. EMC left pcb/06.** By the duplicate rule, the earliest section (06) would be its home, but no specific video could be verified, and its topic is EMC, so the pcb/06 outro now points to Section 07 (the 07 agent was told).
2. **Core changes.**
   - 01: Nine Dot Connects (a home page) is gone from the section; core is now the 2004 tutorial → Sierra Circuits' *PCB Material Selection* → the 370HR/RO4350B data sheets.
   - 03: the Design for Supply Chain concept is replaced by AN5527 and J-STD-048A/046A.
   - 04: the placement concept is replaced by the KiCad 10 PCB Editor manual.
3. **Vendor-hosted teaching material.** pcb/01 now relies on four Sierra Circuits pages and two laminate makers' data sheets (two of these are core), and pcb/04 adds an Altium article. Data sheets are primary data. The Sierra pages are educational, not product claims. The slash-sheet article has at least one doubtful table value, and its description tells readers to trust the data sheet and the standard. Keep, or swap for other fabs' guides.
4. **Gaps without a core item.** pcb/03 Objective 4 (package names and outline drawings) has no core resource: JEDEC JESD30/JEP95 are the obvious candidates once verified. pcb/04 Objective 3 (Kelvin and guard) is served by AoE Ch. 5 (core in 00) and Section 12 rather than by a core item in 04.
5. **Rows of several videos.** Rows made of several videos are typed `video-series`, so they don't need a year. Single-video rows are `video` and miss their year until the browser check.
6. **Phil's Lab #71 is a sponsored episode**, labelled as such in pcb/03.
7. **Homes kept.** IPC-2221 stays in pcb/01 and *Right the First Time* in pcb/06; pcb/08 and pcb/09 are the other agent's to convert. Saturn stays in both 05 and 08, with each description naming its calculators. pcb/08's mini-project still says "your template".
8. **Tone.** The ⭐ preface in pcb/README was toned down ("widely regarded as a legend" removed) and now states that the table is the ⭐ reference.
