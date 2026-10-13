<p align="center">
  <img src="assets/banner.jpg" alt="Learning — A Curated Learning Journey" width="100%">
</p>

<h3 align="center">Curated, structured curricula for self-directed mastery</h3>

<p align="center">
  <a href="ml/">🧠 Machine Learning</a> •
  <a href="math/">🔢 Mathematics</a> •
  <a href="physics/">⚛️ Physics</a> •
  <a href="bio/">🧬 Biology</a> •
  <a href="econ/">📈 Economics</a> •
  <a href="philosophy/">🧠 Philosophy</a> •
  <a href="pcb/">🔌 PCB Design</a> •
  <a href="btc/">₿ Bitcoin</a> •
  <a href="software/">🏗️ Software Engineering</a>
</p>

---

## What Is This?

A personal knowledge repository containing **nine structured learning curricula (120 sections)**. Each section pairs curated resources with the work that turns reading into skill: learning objectives, practice exercises, a mini-project, and self-test questions. Built for deep, self-directed study paired with [NotebookLM](https://notebooklm.google.com/).

**Start with the [Study Guide](STUDY-GUIDE.md).** It covers the study loop, tracks across curricula, how the curricula connect, and where your notes and projects go.

Every curriculum follows the same structure:
- **12–15 numbered sections**, progressing from foundations to frontiers. Sections added later are appended and say where to take them.
- **Each section has:** Why it matters · Prerequisites · 🎯 Learning Objectives · Resources · Suggested Order · 🛠️ Practice + 🏗️ Mini-project · ✅ Check Yourself
- **Must-read markers** (🔑) for the core path, plus curriculum-specific ⭐ lists
- **Cross-cutting references** (books, courses, blogs/tools)
- **Progress tracker** (`PROGRESS.md`) for resources *and* practice
- **Maintenance:** `update-curriculum` agent skills (ml, pcb, btc, software), a repo-wide [`audit-curriculum`](.agents/skills/audit-curriculum/SKILL.md) skill, and [`tools/check_repo.py`](tools/check_repo.py)

---

## 📚 The Curricula

### [🧠 Machine Learning](ml/)
> From the roots of AI to the latest frontiers — a complete path through modern ML.

| Highlights | |
|---|---|
| **Sections** | Historical foundations → Math → Classical ML → Neural nets → CNNs/ViTs → RNNs → Transformers → Generative models → Scaling/Efficiency → LLMs → RL → Frontiers → **Interpretability & Alignment** → **Graphs, Geometry & Science** |
| **Special marker** | ⭐ = Ilya Sutskever's reading list (the 27-item reconstruction; "*If you really learn all of these, you'll know 90% of what matters today*") |
| **Key resources** | Karpathy, 3Blue1Brown, Andrew Ng, Stanford CS courses, Goodfellow, Sutton & Barto, Anthropic (mechanistic interpretability) |

---

### [🔢 Mathematics](math/)
> From foundational reasoning to the mathematical machinery powering modern AI and science.

| Highlights | |
|---|---|
| **Sections** | Mathematical thinking → Linear algebra → Analysis → Probability → Optimization → Information theory → Graph theory → Differential equations → Abstract algebra → Topology/geometry → Causal inference → Category theory · **added:** Fourier analysis & signals and systems · Number theory & cryptography · Numerical methods |
| **Key resources** | Axler, Strang, Abbott, Boyd & Vandenberghe, Cover & Thomas, Pearl, Strogatz, 3Blue1Brown |
| **Focus** | Genuine mathematical maturity, not just "math for ML" |

---

### [⚛️ Physics](physics/)
> From classical mechanics to quantum computing — the physical principles underlying simulation, modeling, and AI for science.

| Highlights | |
|---|---|
| **Sections** | Classical mechanics → Waves/optics → Thermodynamics → Electromagnetism → Quantum mechanics → Relativity → Computational physics → Quantum computing → Condensed matter → Fluids → Chaos → Physics-informed ML · **added:** Measurement, noise & sensor physics |
| **Key resources** | Feynman Lectures, Griffiths, Schroeder, Strogatz, Newman, Nielsen & Chuang, Qiskit |
| **Focus** | Physics that connects to computation, simulation, and AI applications |

---

### [🧬 Biology & Computational Life Sciences](bio/)
> From molecular biology fundamentals to AI-driven drug discovery and protein design.

| Highlights | |
|---|---|
| **Sections** | Molecular biology → Biochemistry → Genetics/genomics → Structural biology → Bioinformatics → Systems biology → Drug discovery → Protein design → Genomic medicine → Neuroscience → AI for biology → Frontiers |
| **Key resources** | Alberts, Lehninger, Durbin, Dayan & Abbott, AlphaFold, RFdiffusion, ESM-2 |
| **Focus** | The conceptual foundation for AI × life sciences innovation |

---

### [📈 Economics, Decision Theory & Game Theory](econ/)
> The mathematics of incentives, strategy, and coordination.

| Highlights | |
|---|---|
| **Sections** | Economic thinking → Microeconomics → Game theory → Decision theory → Mechanism design → Information economics → Behavioral economics → Network economics → Computational economics → Social choice → Monetary/crypto → AI alignment economics |
| **Key resources** | Varian, Tadelis, Kahneman, Börgers, Easley & Kleinberg, Nisan et al., Roughgarden |
| **Focus** | Foundations for AI alignment, multi-agent systems, and incentive design |

---

### [🧠 Philosophy of Mind & Intelligence](philosophy/)
> The deepest questions about minds, machines, consciousness, and what it means to understand.

| Highlights | |
|---|---|
| **Sections** | Foundations → Philosophy of mind → Consciousness → Computation & mind → Intelligence → Philosophy of AI → Ethics of AI → Existential risk → Language & meaning → Free will → Eastern philosophy → Frontiers |
| **Key resources** | Hofstadter (GEB), Chalmers, Dennett, Bostrom, Russell, Kim, Searle, Turing |
| **Focus** | What intelligence actually *is* — the questions that shape how you build AI |

---

### [🔌 PCB Design](pcb/)
> From electronics fundamentals to high-speed signal integrity and EMC compliance.

| Highlights | |
|---|---|
| **Sections** | Electronics → PCB anatomy → Schematic → Components → Layout → Power/grounding → Signal integrity → EMC → Stackup → DFM → Advanced → Reference projects · **added:** Analog, mixed-signal & precision measurement · Bring-up, test & debug |
| **Special marker** | ⭐ = Rick Hartley's recommended reading list |
| **Key resources** | Phil's Lab, Robert Feranec, Rick Hartley, Bogatin, Johnson & Graham, Ott |
| **Included docs** | IPC-2221, PCB Design Tutorial, Rick's Reading Recommendations (PDFs) |

---

### [₿ Bitcoin](btc/)
> From the cypherpunk manifesto to Taproot — a deep technical understanding of Bitcoin.

| Highlights | |
|---|---|
| **Sections** | History/philosophy → Cryptography → Protocol → Mining → Transactions/Script → Wallets/BIPs → P2P network → Lightning → Security/privacy → Economics → Development → Frontiers · **added:** Hands-on labs (run in parallel) · Governance & protocol change |
| **Special marker** | ⭐ = Satoshi/Cypherpunk canon |
| **Key resources** | Mastering Bitcoin (Antonopoulos), Programming Bitcoin (Song), Learn Me A Bitcoin, Lopp.net, Chaincode Labs, 3Blue1Brown |

---

### [🏗️ Software Engineering](software/)
> Mastering code in the age of AI — focused on reading, reviewing, and architecting, not typing line by line.

| Highlights | |
|---|---|
| **Sections** | CS foundations → Python → Embedded C → Code reading/review → Architecture → Testing → Systems → RTOS → Security → **Agentic AI workflows** → Version control → Professional practice · **added:** Firmware toolchain, debug & observability · HIL testing & lab automation |
| **Special marker** | 🤖 = AI-workflow specific resources |
| **Key resources** | Fluent Python, K&R C, DDIA, Refactoring, Code Reading, Quantum Leaps, Simon Willison, Embedded Artistry |
| **Focus** | Python + Embedded C · Senior architect mindset · Human-in-the-loop AI development |

---

## 🗂️ Repository Structure

```
learning/
├── README.md              ← you are here
├── STUDY-GUIDE.md         ← study loop, tracks, cross-curriculum map
├── assets/
│   └── banner.jpg
├── ml/                    ← each curriculum has the same layout:
│   ├── README.md          ←   overview, legend, learning path
│   ├── PROGRESS.md        ←   tracker for resources + practice
│   ├── 00-historical-foundations/README.md
│   ├── ...                ←   numbered sections (ml: 00–13)
│   ├── books/  courses/  blogs-and-references/
│   └── .agents/skills/update-curriculum/   (ml, pcb, btc, software)
├── math/                  ← 00–14
├── physics/               ← 00–12
├── bio/                   ← 00–11
├── econ/                  ← 00–11
├── philosophy/            ← 00–11
├── pcb/                   ← 00–13, plus documents/ (IPC-2221A, tutorials, Rick's reading list)
├── btc/                   ← 00–13
├── software/              ← 00–13
├── notes/                 ← your notes, one file per section studied
├── projects/              ← your mini-project deliverables
├── reviews/               ← dated audit reports (e.g. 2026-10-deep-dive/)
├── tools/check_repo.py    ← offline structural checker
└── .agents/skills/audit-curriculum/   ← repo-wide audit skill
```

---

## How to Use

1. **Pick a track** in the [Study Guide](STUDY-GUIDE.md), or a curriculum and its `README.md` learning path
2. **Run the study loop in each section.** Read the objectives first, then follow the 🔑 core path, do the 🛠️ practice, and answer ✅ Check Yourself from memory.
3. **Keep your work in the repo.** Notes go in `notes/`, mini-projects in `projects/`.
4. **Track progress** in each `PROGRESS.md`: resources, practice, the mini-project, and self-checks
5. **Pair with NotebookLM.** Upload a section README and its sources, and have it quiz you on the Check Yourself questions.
6. **Keep current and correct.** Use the `update-curriculum` skills, which require opening every link. Run the `audit-curriculum` skill and `python tools/check_repo.py` periodically. Past audits are in [`reviews/`](reviews/).

---

## License

Personal learning repository. All linked resources belong to their respective authors and publishers.
