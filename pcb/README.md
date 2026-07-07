# 🔌 PCB Design — A Learning Journey

> A curated, ordered collection of the best resources for mastering PCB design — from electronics fundamentals to high-speed signal integrity.

## Purpose

This repository is a structured curriculum for self-studying PCB (Printed Circuit Board) design. It compiles the most important books, video lectures, reference standards, tools, and open-source projects into a coherent learning path.

**Designed for pairing with [NotebookLM](https://notebooklm.google.com/)** — feed individual sections, datasheets, or reference documents into NotebookLM for interactive study sessions.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔑 | **Must-read / must-watch** — absolute priority items |
| ⭐ | **Rick Hartley's recommended reading** — from his curated list for PCB designers |
| 🔑⭐ | Both — a must-read that's also on Rick's list |

---

## Learning Path

Work through the numbered sections in order. Each section's README contains curated resources with direct links, descriptions, and a suggested order within that section.

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
```

### Cross-Cutting References

| Directory | Contents |
|-----------|----------|
| [books/](books/) | Curated book list with reading order |
| [courses/](courses/) | Video lectures and channels in recommended sequence |
| [blogs-and-references/](blogs-and-references/) | Essential sites, tools, component libraries, fab houses |
| [documents/](documents/) | Included reference PDFs (IPC-2221, tutorials, Rick's reading list) |

---

## ⭐ Rick Hartley's Reading List — Cross-Reference

> Rick Hartley is widely regarded as a legend in signal integrity and EMC design. His recommended reading list is the standard curriculum for professional PCB designers.

Source: [documents/Ricks-Reading-Recommendation.pdf](documents/Ricks-Reading-Recommendation.pdf)

| # | Book / Resource | Section |
|---|-----------------|---------|
| 1 | Signal and Power Integrity — Simplified (Bogatin) | [06 — Signal Integrity](06-signal-integrity/) |
| 2 | High-Speed Digital Design: A Handbook of Black Magic (Johnson & Graham) | [06 — Signal Integrity](06-signal-integrity/) |
| 3 | Electromagnetic Compatibility Engineering (Ott) | [07 — EMC](07-emc-and-compliance/) |
| 4 | Right the First Time, Vols I & II (Ritchey) | [06 — Signal Integrity](06-signal-integrity/) / [08 — Stackup](08-multi-layer-and-stackup/) |
| 5 | Fast Circuit Boards: Energy Management (Morrison) | [05 — Power & Grounding](05-power-and-grounding/) |
| 6 | Principles of Power Integrity for PDN Design (Smith & Bogatin) | [05 — Power & Grounding](05-power-and-grounding/) |
| 7 | Noise Reduction Techniques in Electronic Systems (Ott) | [07 — EMC](07-emc-and-compliance/) |

---

## Key Educators

| Educator | Platform | Specialty |
|----------|----------|-----------|
| **Phil's Lab** | [YouTube](https://www.youtube.com/@PhilsLab) | End-to-end PCB design, practical theory |
| **Robert Feranec** | [YouTube](https://www.youtube.com/@RobertFeranec) | High-speed design, layout reviews, industry interviews |
| **Rick Hartley** | Various (Altium, Sierra Circuits) | Signal integrity, EMC, grounding, stackup |
| **EEVblog** | [YouTube](https://www.youtube.com/@EEVblog) | Electronics fundamentals, teardowns |
| **Dr. EMC** | [YouTube](https://www.youtube.com/@DrEMC) | EMC simulation and practical design |
| **Altium Academy** | [YouTube](https://www.youtube.com/@AltiumAcademy) | Broad PCB education, expert interviews |

---

## How to Use with NotebookLM

1. **Section-by-section**: Upload a section's README for study guidance
2. **Standards**: Upload the included IPC-2221 PDF for interactive Q&A
3. **Datasheets**: Upload component datasheets for design assistance
4. **Progress tracking**: Use [PROGRESS.md](PROGRESS.md) to track completion

---

## Keeping Current

The [Advanced Topics](10-advanced-topics/) and [Reference Projects](11-reference-projects/) sections cover evolving material. To update the curriculum with new resources, use the `.agents/skills/update-curriculum` skill.

---

## License

This is a personal learning repository. All linked resources belong to their respective authors and publishers.
