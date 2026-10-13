# 🔢 Mathematics — A Learning Journey

> From foundational reasoning to the mathematical machinery powering modern AI and science.

## Purpose

This repository is a structured curriculum for self-studying mathematics with genuine depth and rigor. It compiles the most important textbooks, courses, papers, and online resources into a coherent learning path — designed not just as "math for ML" but as a foundation for mathematical maturity across machine learning, physics, biology, and engineering.

**Designed for pairing with [NotebookLM](https://notebooklm.google.com/)** — feed individual sections or textbook chapters into NotebookLM for interactive study sessions.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔑 | **Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line. In `books/` and `courses/`, 🔑 marks items that are core in some section; in `blogs-and-references/`, the sources to follow first |

---

## Learning Path

Each section's README contains:
- curated resources with direct links and descriptions;
- a suggested reading order within that section;
- learning objectives, practice exercises, a mini-project, and Check Yourself questions.

Sections 12–14 were added later, so their numbers don't reflect where they belong. Take them at the positions shown.

```
Section 00  →  Mathematical Thinking
Section 01  →  Linear Algebra
Section 02  →  Calculus and Analysis
Section 03  →  Probability and Statistics
Section 04  →  Optimization
Section 05  →  Information Theory
Section 06  →  Graph Theory and Combinatorics
Section 07  →  Differential Equations
Section 08  →  Abstract Algebra
Section 09  →  Topology and Geometry
Section 10  →  Causal Inference
Section 11  →  Category Theory and Frontiers
Section 12  →  Fourier Analysis, Signals and Systems        (take after 07 and 03 · core)
Section 13  →  Number Theory and Cryptography               (take after 08 · core for the Bitcoin curriculum)
Section 14  →  Numerical Methods and Scientific Computing   (take after 07 or 12)
```

### Recommended Route (engineering focus)

Not every section deserves equal time.

| Track | Sections, in order | Notes |
|-------|--------------------|-------|
| **Core** | 00 → 01 → 02 → 07 → 03 → 12 → 14 → 04 → 05 | The engineering spine: complex analysis is in 02, control (*Feedback Systems*) in 07, Kalman filtering in 03 |
| **Core for Bitcoin** | 08 → 13 | Groups and finite fields, then number theory, elliptic curves, and signatures |
| **Electives** | 06, 09, 10, 11 | Graphs, topology and geometry, causal inference, category theory — follow your interests |

### Cross-Cutting References

| Directory | Contents |
|-----------|----------|
| [books/](books/) | Curated book list with reading order |
| [courses/](courses/) | Video lectures and MOOCs in recommended sequence |
| [blogs-and-references/](blogs-and-references/) | Essential blogs, references, and community resources |

---

## Connections to Other Curricula

This mathematics curriculum is designed to pair with a broader learning program:

| Curriculum | Key Math Connections |
|------------|---------------------|
| Machine Learning | Linear algebra (01), Calculus (02), Probability (03), Optimization (04), Information Theory (05) |
| Physics | Calculus & Analysis (02), Differential Equations (07), Topology & Geometry (09), Abstract Algebra (08), Fourier Analysis (12), Numerical Methods (14) |
| Biology | Probability & Statistics (03), Differential Equations (07), Graph Theory (06), Causal Inference (10) |
| Software Engineering | Mathematical Thinking (00), Graph Theory (06), Abstract Algebra (08), Category Theory (11), Numerical Methods (14) |
| Bitcoin | Abstract Algebra (08), Number Theory and Cryptography (13), Probability (03) |
| PCB Design | Complex analysis (02), Differential Equations (07), Signals and Systems (12), Numerical Methods (14) |

---

## How to Use with NotebookLM

1. **Section-by-section**: Upload a section's README to NotebookLM as a source for study guidance
2. **Textbooks**: Upload free book chapters or PDFs for interactive Q&A and problem-solving
3. **Papers**: Download PDFs of key papers and upload them for deep-dive conversations
4. **Progress tracking**: Use [PROGRESS.md](PROGRESS.md) to track what you've completed

---

## Keeping Current

Mathematics moves more slowly than ML, but new connections between mathematics and AI are being forged constantly. The [Category Theory and Frontiers section](11-category-theory-and-frontiers/) covers the latest developments at the math–AI boundary.

---

## License

This is a personal learning repository. All linked resources belong to their respective authors and publishers.
