# 🔌 PCB Design — A Learning Journey

> A curated, ordered collection of the best resources for mastering PCB design — from electronics fundamentals to high-speed signal integrity.

## Purpose

This repository is a structured curriculum for self-studying PCB (Printed Circuit Board) design. It compiles the most important books, video lectures, reference standards, tools, and open-source projects into a coherent learning path.

**Designed for pairing with [NotebookLM](https://notebooklm.google.com/)** — feed individual sections, datasheets, or reference documents into NotebookLM for interactive study sessions.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔑 | **Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line. In `books/` and `courses/`, 🔑 marks items that are core in some section; in `blogs-and-references/`, the sources to follow first |
| ⭐ | **Rick Hartley's recommended reading** — from his curated list for PCB designers (books only; his own talks are not on the list) |
| 🔑⭐ | Both — a core-path item that's also on Rick's list |

---

## Learning Path

Work through the numbered sections in order. Sections 12 and 13 were added later and keep their numbers so nothing else is renumbered; take them at the positions shown. Each section's README contains curated resources with direct links, descriptions, and a suggested order within that section.

```
Section 00  →  Electronics Fundamentals
Section 01  →  PCB Anatomy and Materials
Section 02  →  Schematic Capture and Library Management
Section 03  →  Component Selection and Sourcing
Section 04  →  PCB Layout Fundamentals
Section 05  →  Power Distribution and Grounding
Section 06  →  Signal Integrity
Section 07  →  EMC and Compliance
Section 08  →  Multi-Layer Design and Stackup
Section 09  →  Design for Manufacturing (DFM) and Fabrication
Section 10  →  Advanced Topics
Section 11  →  Reference Projects and Open-Source Hardware
Section 12  →  Analog, Mixed-Signal and Precision Measurement   (take after Section 05)
Section 13  →  Bring-up, Test and Debug                          (take after Section 09)
```

### Cross-Cutting References

| Directory | Contents |
|-----------|----------|
| [books/](books/) | Curated book list with reading order |
| [courses/](courses/) | Video lectures and channels in recommended sequence |
| [blogs-and-references/](blogs-and-references/) | Essential sites, tools, component libraries, fab houses |
| [documents/](documents/) | Included reference PDFs: IPC-2221A (2003; superseded by IPC-2221C, 2023, see Section 01), Dave Jones' PCB Design Tutorial (2004), Rick's reading list |

---

## ⭐ Rick Hartley's Reading List — Cross-Reference

> Rick Hartley is widely regarded as a legend in signal integrity and EMC design. His reading list (12 books, distributed by Nine Dot Connects) is a widely shared core library for SI/EMC-minded PCB designers. Rick groups the books under *Signal Integrity Control* (1–6) and *EMI & Noise Control* (7–12).

Source: [documents/Ricks-Reading-Recommendation.pdf](documents/Ricks-Reading-Recommendation.pdf)

| # | Book / Resource | Section |
|---|-----------------|---------|
| 1 | Fast Circuit Boards: Energy Management (Morrison) | [05 — Power & Grounding](05-power-and-grounding/) |
| 2 | Right the First Time, Vols I & II (Ritchey) | [06 — Signal Integrity](06-signal-integrity/) / [08 — Stackup](08-multi-layer-and-stackup/) |
| 3 | High-Speed Digital System Design: A Handbook of Interconnect Theory and Design Practices (Hall, Hall & McCall) | [06 — Signal Integrity](06-signal-integrity/) |
| 4 | High-Speed Digital Design: A Handbook of Black Magic (Johnson & Graham) | [06 — Signal Integrity](06-signal-integrity/) |
| 5 | High-Speed Signal Propagation: Advanced Black Magic (Johnson & Graham) | [06 — Signal Integrity](06-signal-integrity/) |
| 6 | Signal and Power Integrity — Simplified (Bogatin) | [06 — Signal Integrity](06-signal-integrity/) |
| 7 | PCB Design for Real-World EMI Control (Archambeault) | [07 — EMC](07-emc-and-compliance/) |
| 8 | Digital Design for Interference Specifications: A Practical Handbook for EMI Suppression (Terrell & Keenan) | [07 — EMC](07-emc-and-compliance/) |
| 9 | Electromagnetic Compatibility Engineering (Ott) | [07 — EMC](07-emc-and-compliance/) |
| 10 | Principles of Power Integrity for PDN Design — Simplified (Smith & Bogatin) | [05 — Power & Grounding](05-power-and-grounding/) |
| 11 | Grounding & Shielding (Morrison; Rick cites the 5th ed., *Grounding & Shielding Techniques*, and the current 6th ed. is *Grounding and Shielding: Circuits and Interference*) | [05 — Power & Grounding](05-power-and-grounding/) |
| 12 | Introduction to Electromagnetic Compatibility (Paul) | [07 — EMC](07-emc-and-compliance/) |

> Ott's *Noise Reduction Techniques in Electronic Systems* (Section 07) is a good book but is **not** on Rick's list; his list names Ott's later *Electromagnetic Compatibility Engineering*.

---

## Key Educators

| Educator | Platform | Specialty |
|----------|----------|-----------|
| **Phil's Lab** | [YouTube](https://www.youtube.com/@PhilsLab) | End-to-end PCB design, practical theory |
| **Robert Feranec** | [YouTube](https://www.youtube.com/@RobertFeranec) | High-speed design, layout reviews, industry interviews |
| **Rick Hartley** | Various (Altium, Sierra Circuits) | Signal integrity, EMC, grounding, stackup |
| **EEVblog** | [YouTube](https://www.youtube.com/@EEVblog) | Electronics fundamentals, teardowns |

---

## How to Use with NotebookLM

1. **Section-by-section**: Upload a section's README for study guidance
2. **Standards**: Upload the included IPC-2221A PDF (2003 revision, since superseded by IPC-2221B/C; use IPC-2152 for current capacity) for interactive Q&A
3. **Datasheets**: Upload component datasheets for design assistance
4. **Progress tracking**: Use [PROGRESS.md](PROGRESS.md) to track completion

---

## Keeping Current

The [Advanced Topics](10-advanced-topics/) and [Reference Projects](11-reference-projects/) sections cover evolving material. To update the curriculum with new resources, use the `.agents/skills/update-curriculum` skill.

---

## License

This is a personal learning repository. All linked resources belong to their respective authors and publishers.
