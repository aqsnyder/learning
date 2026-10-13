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
  <a href="philosophy/">💭 Philosophy</a> •
  <a href="pcb/">🔌 PCB Design</a> •
  <a href="btc/">₿ Bitcoin</a> •
  <a href="software/">🏗️ Software Engineering</a>
</p>

---

## What is this?

Nine self-study curricula, **129 sections** in all. They run from foundations to current research in machine learning, mathematics, physics, biology, economics, philosophy of mind, PCB design, Bitcoin and software engineering.

Each section works like a small course:
- why the topic matters, and what to know first
- learning objectives
- a **core path** of at most three must-read resources
- practice exercises, most with answers you can check
- a mini-project
- self-test questions

Citations and links were audited in the [October 2026 review](reviews/2026-10-deep-dive/README.md), which also lists the few pages that couldn't be checked automatically.

## Start learning in five minutes

1. **Pick a topic** from the table below and open its curriculum page. Its learning path lists every section in the order to take it, with each section's core path.
2. **Open the first section.** Read why it matters, its prerequisites and the 🎯 learning objectives.
3. **Follow the core path.** The first line of each section's *Suggested Order* names its 🔑 must-reads, at most three. Read them first, in that order. The numbered list under it is the full-depth order and includes optional items. For each exercise you pick, also read the sources named in its closing *(~time · sources)* note.
4. **Do at least two 🛠️ exercises.** Each says what to produce, and most say how to check it. Do the 🏗️ mini-project, the section's capstone, when the section is on your track.
5. **Answer ✅ Check Yourself from memory**, in writing, before you look anything up. Then correct your answers against the sources.
6. **Record it.** Tick the section off in the curriculum's `PROGRESS.md`, and write a one-page note in [`notes/`](notes/README.md).

The [Study Guide](STUDY-GUIDE.md) explains why this loop works and adds spaced review. It also has prompts for having NotebookLM or Claude quiz you on a section.

## Pick a topic

| Curriculum | What you'll learn | Sections | Start here | Anchor resources |
|---|---|---|---|---|
| [🧠 Machine Learning](ml/) | From perceptrons to LLMs, RL and interpretability. Build and train models from scratch, read current papers critically, and put models on microcontrollers. | 15 | [00 Historical Foundations](ml/00-historical-foundations/) | Karpathy's *Zero to Hero*, Prince's *Understanding Deep Learning*, Sutton & Barto, Ilya Sutskever's reading list |
| [🔢 Mathematics](math/) | Proofs, linear algebra, analysis, probability, optimization and information theory, plus an engineering spine: signals and systems, numerical methods, and number theory for cryptography. | 15 | [00 Mathematical Thinking](math/00-mathematical-thinking/) | Axler, Strang, Abbott, Boyd & Vandenberghe, Cover & Thomas, Strogatz |
| [⚛️ Physics](physics/) | Mechanics through quantum computing, with computation throughout, plus measurement, noise and sensor physics for instrument work. | 13 | [00 Classical Mechanics](physics/00-classical-mechanics/) | *The Feynman Lectures*, Griffiths, Schroeder, Newman, Nielsen & Chuang, Taylor's *Error Analysis* |
| [🧬 Biology](bio/) | Molecular biology through protein design and AI for biology, with the statistics, instrumentation and population genetics you need to judge the numbers. | 15 | [00 Molecular Biology Fundamentals](bio/00-molecular-biology-fundamentals/) | Alberts, Lehninger, Holmes & Huber, AlphaFold, ESM-2, RFdiffusion |
| [📈 Economics](econ/) | Incentives, games, decisions and mechanism design, plus causal inference, macro and money, industrial organization, and the economics of AI. | 16 | [00 Economic Thinking](econ/00-economic-thinking/) | Varian, Tadelis, Angrist & Pischke, Kahneman (with replication caveats), Roughgarden |
| [💭 Philosophy](philosophy/) | Mind, consciousness, computation, AI ethics and alignment, with each debate argued from both sides, plus philosophy of science. | 13 | [00 Foundations of Philosophy](philosophy/00-foundations-of-philosophy/) | Hofstadter, Chalmers, Dennett, Kim, Russell, Godfrey-Smith |
| [🔌 PCB Design](pcb/) | From electronics fundamentals in KiCad to signal integrity, EMC, precision analog layout, and board bring-up and test. | 14 | [00 Electronics Fundamentals](pcb/00-electronics-fundamentals/) | *The Art of Electronics*, Phil's Lab, Robert Feranec, Rick Hartley's reading list, Bogatin, Ott |
| [₿ Bitcoin](btc/) | The protocol from the cryptography up: transactions, wallets, P2P, Lightning and governance, with hands-on labs run alongside. | 14 | [00 History and Philosophy](btc/00-history-and-philosophy/) | The whitepaper, *Mastering Bitcoin*, *Programming Bitcoin*, Learn Me A Bitcoin, Chaincode Labs |
| [🏗️ Software Engineering](software/) | Python and embedded C at a senior level: reading and reviewing code, architecture, testing, firmware debugging, hardware-in-the-loop (HIL) automation, and agentic AI workflows. | 14 | [00 Computer Science Foundations](software/00-cs-foundations/) | *Fluent Python*, *Modern C*, *Making Embedded Systems*, *Designing Data-Intensive Applications*, the METR study of AI coding productivity |

## Tracks: routes across curricula

The curricula connect. These five tracks thread them together. The [Study Guide](STUDY-GUIDE.md#tracks) has each one with links, plus a map of which topic lives where.

| Track | For | Route |
|---|---|---|
| **A. Precision hardware and instruments** | Measurement hardware: the math, physics, layout and firmware behind it | math/02 → 07 → 03 → 12 → 14 · pcb/00–05 → 12 → 06–09 → 13 · physics/03 → 12 · software/01 → 02 → 07 → 12 → 05 → 13 |
| **B. AI and machine learning** | Understanding the models you build with | math/01, 03, 04, 05 → ml/00–10 → 12 → 11, with ml/14 as the bridge to hardware |
| **C. Bitcoin** | The protocol, built on real cryptography | math/08 → 13 → btc/00–10 with the btc/12 labs alongside → btc/13 → btc/11 |
| **D. AI for science** | Curiosity | physics/06 → 11 · ml/13 · bio/00–04 (with bio/12 and 14) → 07 → 10 → 11 |
| **E. Thinking tools** | Background reading | philosophy/00 → 12 → econ/00 and 03 → philosophy/01–02 → 05 |

## How a section is laid out

Every numbered section follows the same plan:

| Part | What it gives you |
|---|---|
| **Why it matters** · **Prerequisites** | The opening: whether to take the section now, and what to study first |
| 🎯 **Learning Objectives** | 4–5 things you'll be able to do: your test for "done" |
| **Resources** | Books, papers, courses and videos, with authors, years and a line on why each is there |
| **Suggested Order** | Opens with the **Core path** line, then puts everything else in order |
| 🛠️ **Practice** + 🏗️ **Mini-project** | 4–6 exercises with honest time estimates and, mostly, checkable results; then a capstone project |
| ✅ **Check Yourself** | 8 questions to answer from memory, then check against the sources |

| Marker | Meaning |
|---|---|
| 🔑 | Core path: at most 3 per section, named in the section's *Core path* line |
| ⭐ | A named, closed list: **ml** Ilya Sutskever's 27 items · **pcb** Rick Hartley's 12 books · **btc** the Bitcoin canon table |
| 🤖 | (software) A resource specific to AI-assisted development |
| ⚠️ | A caveat to read before relying on it: a failed replication, a disputed claim, or a link problem |

## Every section at a glance

Each list follows its curriculum's recommended order. Click a curriculum to expand it.

<!-- section-index:start — generated by tools/build_index.py from the curriculum learning paths; do not edit by hand -->
<details>
<summary><b>🧠 Machine Learning</b> · 15 sections · <a href="ml/">curriculum page</a></summary>

- [00 — Historical Foundations of AI](ml/00-historical-foundations/) · Start here
- [01 — Mathematical Foundations](ml/01-math-foundations/)
- [02 — Classical Machine Learning](ml/02-classical-ml/)
- [03 — Neural Network Fundamentals](ml/03-neural-network-fundamentals/)
- [04 — CNNs and Computer Vision](ml/04-cnns-and-computer-vision/)
- [05 — RNNs, Sequences, and Memory](ml/05-rnns-sequences-and-memory/)
- [06 — Transformers and Attention](ml/06-transformers-and-attention/)
- [07 — Generative Models](ml/07-generative-models/)
- [08 — Scaling, Efficiency, and Deployment](ml/08-scaling-and-training/)
- [14 — Edge and Embedded ML (TinyML)](ml/14-edge-and-embedded-ml/) · After 08 (also needs 02 and 04)
- [09 — Large Language Models](ml/09-llms-and-language/)
- [10 — Reinforcement Learning](ml/10-reinforcement-learning/)
- [12 — Interpretability and Alignment](ml/12-interpretability-and-alignment/) · After 10 (needs 06 and 09)
- [11 — Frontiers (2023-2026+)](ml/11-frontiers/) · After 12 · the living section: revisit it
- [13 — Graphs, Geometry, and Science](ml/13-graphs-geometry-and-science/) · Any time after 06

</details>

<details>
<summary><b>🔢 Mathematics</b> · 15 sections · <a href="math/">curriculum page</a></summary>

- [00 — Mathematical Thinking](math/00-mathematical-thinking/) · Start here
- [01 — Linear Algebra](math/01-linear-algebra/)
- [02 — Calculus and Analysis](math/02-calculus-and-analysis/)
- [03 — Probability and Statistics](math/03-probability-and-statistics/)
- [04 — Optimization](math/04-optimization/)
- [05 — Information Theory](math/05-information-theory/)
- [06 — Graph Theory and Combinatorics](math/06-graph-theory-and-combinatorics/) · Elective
- [07 — Differential Equations](math/07-differential-equations/)
- [12 — Fourier Analysis, Signals and Systems](math/12-fourier-analysis-signals-and-systems/) · After 03 and 07 · core for hardware
- [14 — Numerical Methods and Scientific Computing](math/14-numerical-methods-and-scientific-computing/) · After 07 or 12
- [08 — Abstract Algebra](math/08-abstract-algebra/)
- [13 — Number Theory and Cryptography](math/13-number-theory-and-cryptography/) · After 08 · core for Bitcoin
- [09 — Topology and Geometry](math/09-topology-and-geometry/) · Elective
- [10 — Causal Inference](math/10-causal-inference/) · Elective (needs 03 and 06)
- [11 — Category Theory and Frontiers](math/11-category-theory-and-frontiers/) · Elective

</details>

<details>
<summary><b>⚛️ Physics</b> · 13 sections · <a href="physics/">curriculum page</a></summary>

- [00 — Classical Mechanics](physics/00-classical-mechanics/) · Start here
- [01 — Waves and Optics](physics/01-waves-and-optics/)
- [02 — Thermodynamics and Statistical Mechanics](physics/02-thermodynamics-and-statistical-mechanics/)
- [03 — Electromagnetism](physics/03-electromagnetism/)
- [04 — Quantum Mechanics](physics/04-quantum-mechanics/)
- [05 — Special and General Relativity](physics/05-special-and-general-relativity/)
- [06 — Computational Physics](physics/06-computational-physics/)
- [07 — Quantum Computing](physics/07-quantum-computing/)
- [08 — Condensed Matter and Materials](physics/08-condensed-matter-and-materials/)
- [12 — Measurement, Noise, and Sensor Physics](physics/12-measurement-noise-and-sensor-physics/) · Right after 08
- [09 — Fluid Dynamics and Continuum Mechanics](physics/09-fluid-dynamics-and-continuum/)
- [10 — Nonlinear Dynamics and Chaos](physics/10-nonlinear-dynamics-and-chaos/)
- [11 — Physics-Informed ML and Frontiers](physics/11-physics-informed-ml-and-frontiers/)

</details>

<details>
<summary><b>🧬 Biology & Computational Life Sciences</b> · 15 sections · <a href="bio/">curriculum page</a></summary>

- [00 — Molecular Biology Fundamentals](bio/00-molecular-biology-fundamentals/) · Start here
- [01 — Biochemistry](bio/01-biochemistry/)
- [02 — Genetics and Genomics](bio/02-genetics-and-genomics/)
- [14 — Evolution and Population Genetics](bio/14-evolution-and-population-genetics/) · After 02
- [03 — Structural Biology](bio/03-structural-biology/)
- [13 — Bioinstrumentation, Imaging and Lab Automation](bio/13-bioinstrumentation-imaging-and-lab-automation/) · After 03
- [12 — Statistics and Experimental Design for Biology](bio/12-statistics-and-experimental-design/) · Before 04, or alongside it
- [04 — Bioinformatics and Sequence Analysis](bio/04-bioinformatics-and-sequence-analysis/)
- [05 — Systems Biology](bio/05-systems-biology/)
- [06 — Computational Chemistry and Drug Discovery](bio/06-computational-chemistry-and-drug-discovery/)
- [07 — Protein Engineering and Design](bio/07-protein-engineering-and-design/)
- [08 — Genomic Medicine](bio/08-genomic-medicine/)
- [09 — Neuroscience](bio/09-neuroscience/)
- [10 — AI for Biology](bio/10-ai-for-biology/)
- [11 — Frontiers (2023–2026+)](bio/11-frontiers/)

</details>

<details>
<summary><b>📈 Economics, Decision Theory & Game Theory</b> · 16 sections · <a href="econ/">curriculum page</a></summary>

- [00 — Economic Thinking](econ/00-economic-thinking/) · Start here
- [01 — Microeconomics](econ/01-microeconomics/)
- [13 — Empirical Economics and Causal Inference](econ/13-empirical-economics-and-causal-inference/) · After 01
- [02 — Game Theory](econ/02-game-theory/)
- [03 — Decision Theory](econ/03-decision-theory/)
- [04 — Mechanism Design](econ/04-mechanism-design/)
- [05 — Information Economics](econ/05-information-economics/)
- [06 — Behavioral Economics](econ/06-behavioral-economics/)
- [07 — Network Economics](econ/07-network-economics/)
- [15 — Industrial Organization and Strategy](econ/15-industrial-organization-and-strategy/) · After 07 (needs 01 and 02)
- [08 — Computational Economics](econ/08-computational-economics/)
- [09 — Social Choice and Voting](econ/09-social-choice-and-voting/)
- [14 — Macroeconomics, Money and Financial Markets](econ/14-macroeconomics-money-and-financial-markets/) · Before 10
- [10 — Monetary Economics and Crypto](econ/10-monetary-economics-and-crypto/)
- [11 — AI Alignment through an Economic Lens](econ/11-ai-alignment-economics-and-frontiers/)
- [12 — Economics of AI](econ/12-economics-of-ai/) · After 11 (needs 13)

</details>

<details>
<summary><b>💭 Philosophy of Mind & Intelligence</b> · 13 sections · <a href="philosophy/">curriculum page</a></summary>

- [00 — Foundations of Philosophy](philosophy/00-foundations-of-philosophy/) · Start here
- [12 — Philosophy of Science and Scientific Reasoning](philosophy/12-philosophy-of-science/) · Right after 00
- [01 — Philosophy of Mind](philosophy/01-philosophy-of-mind/)
- [02 — Consciousness](philosophy/02-consciousness/)
- [03 — Computation and Mind](philosophy/03-computation-and-mind/)
- [04 — Intelligence and Understanding](philosophy/04-intelligence-and-understanding/)
- [05 — Philosophy of AI](philosophy/05-philosophy-of-ai/)
- [06 — Ethics of AI](philosophy/06-ethics-of-ai/)
- [07 — Existential Risk and Alignment](philosophy/07-existential-risk-and-alignment/)
- [08 — Language and Meaning](philosophy/08-language-and-meaning/)
- [09 — Free Will and Agency](philosophy/09-free-will-and-agency/)
- [10 — Eastern Philosophy and Mind](philosophy/10-eastern-philosophy-and-mind/)
- [11 — Frontiers](philosophy/11-frontiers/)

</details>

<details>
<summary><b>🔌 PCB Design</b> · 14 sections · <a href="pcb/">curriculum page</a></summary>

- [00 — Electronics Fundamentals](pcb/00-electronics-fundamentals/) · Start here
- [01 — PCB Anatomy and Materials](pcb/01-pcb-anatomy-and-materials/)
- [02 — Schematic Capture and Library Management](pcb/02-schematic-capture/)
- [03 — Component Selection and Sourcing](pcb/03-component-selection/)
- [04 — PCB Layout Fundamentals](pcb/04-pcb-layout-fundamentals/)
- [05 — Power Distribution and Grounding](pcb/05-power-and-grounding/)
- [12 — Analog, Mixed-Signal and Precision Measurement](pcb/12-analog-mixed-signal-and-precision-measurement/) · After 05
- [06 — Signal Integrity](pcb/06-signal-integrity/)
- [07 — EMC and Compliance](pcb/07-emc-and-compliance/)
- [08 — Multi-Layer Design and Stackup](pcb/08-multi-layer-and-stackup/)
- [09 — Design for Manufacturing (DFM) and Fabrication](pcb/09-dfm-and-fabrication/)
- [13 — Bring-up, Test and Debug](pcb/13-bring-up-test-and-debug/) · After 09
- [10 — Advanced Topics](pcb/10-advanced-topics/)
- [11 — Reference Projects and Open-Source Hardware](pcb/11-reference-projects/)

</details>

<details>
<summary><b>₿ Bitcoin</b> · 14 sections · <a href="btc/">curriculum page</a></summary>

- [00 — History and Philosophy](btc/00-history-and-philosophy/) · Start here
- [01 — Cryptography Foundations](btc/01-cryptography-foundations/)
- [02 — Bitcoin Protocol Fundamentals](btc/02-protocol-fundamentals/)
- [12 — Hands-on Labs](btc/12-hands-on-labs/) · Start with 02 and run alongside 02–11; each lab names the section it pairs with
- [03 — Mining and Consensus](btc/03-mining-and-consensus/)
- [04 — Transactions and Script](btc/04-transactions-and-scripting/)
- [05 — Wallets and Key Management](btc/05-wallets-and-key-management/)
- [06 — Network and P2P Layer](btc/06-network-and-p2p/)
- [07 — Lightning Network](btc/07-lightning-network/)
- [08 — Security and Privacy](btc/08-security-and-privacy/)
- [09 — Economics and Game Theory](btc/09-economics-and-game-theory/)
- [10 — Development and Programming](btc/10-development-and-programming/)
- [13 — Governance and Protocol Change](btc/13-governance-and-protocol-change/) · After 10, before 11
- [11 — Advanced Topics and Frontiers](btc/11-advanced-and-frontiers/)

</details>

<details>
<summary><b>🏗️ Software Engineering</b> · 14 sections · <a href="software/">curriculum page</a></summary>

- [00 — Computer Science Foundations](software/00-cs-foundations/) · Start here
- [01 — Python Mastery](software/01-python-mastery/)
- [02 — Embedded C Mastery](software/02-embedded-c-mastery/)
- [03 — Reading and Reviewing Code](software/03-reading-and-reviewing-code/)
- [04 — Software Architecture and Design Patterns](software/04-architecture-and-design-patterns/)
- [05 — Testing and Quality Assurance](software/05-testing-and-quality/)
- [06 — Systems Design and Infrastructure](software/06-systems-and-infrastructure/)
- [07 — Embedded Systems and RTOS](software/07-embedded-systems-and-rtos/)
- [12 — Firmware Toolchain, Debug, and Observability](software/12-firmware-toolchain-debug-and-observability/) · After 07
- [13 — Hardware-in-the-Loop Testing and Lab Automation](software/13-hil-testing-and-lab-automation/) · After 12 (or after 05)
- [08 — Security and Reliability Engineering](software/08-security-and-reliability/)
- [09 — Agentic AI Development Workflows](software/09-agentic-ai-workflows/) · Start early and run alongside (needs 01 and 02)
- [10 — Version Control and Collaboration](software/10-version-control-and-collaboration/) · Start early and run alongside
- [11 — Professional Practice and Technical Leadership](software/11-professional-practice/)

</details>
<!-- section-index:end -->

## Track your progress

- **`PROGRESS.md`** in each curriculum has a checkbox for every resource, plus three for each section's practice: exercises, mini-project, and Check Yourself. Progress means things you've done, not pages you've read.
- **[`notes/`](notes/README.md)**: one note per section, in your own words, with your Check Yourself answers and a few flashcards.
- **[`projects/`](projects/README.md)**: your exercise and mini-project deliverables (code, notebooks, KiCad files, write-ups).

## Repository structure

```
learning/
├── README.md              ← you are here
├── STUDY-GUIDE.md         ← the study loop, five tracks, how the curricula connect, one home per topic
├── ml/                    ← each curriculum has the same layout:
│   ├── README.md          ←   overview, legend, learning path in recommended order
│   ├── PROGRESS.md        ←   checkboxes for resources and practice
│   ├── 00-historical-foundations/README.md
│   ├── ...                ←   numbered sections (ml: 00–14)
│   ├── books/  courses/  blogs-and-references/
│   └── .agents/skills/update-curriculum/   (ml, pcb, btc, software)
├── math/                  ← 00–14
├── physics/               ← 00–12
├── bio/                   ← 00–14
├── econ/                  ← 00–15
├── philosophy/            ← 00–12
├── pcb/                   ← 00–13, plus documents/ (IPC-2221A, tutorials, Rick Hartley's reading list)
├── btc/                   ← 00–13
├── software/              ← 00–13
├── notes/                 ← your notes, one file per section studied
├── projects/              ← your mini-project deliverables
├── reviews/               ← dated audit reports, e.g. 2026-10-deep-dive/
├── tools/                 ← check_repo.py (structure checker), build_index.py (learning paths and this page's index)
└── .agents/skills/audit-curriculum/   ← repo-wide audit skill
```

Some sections were added after the original numbering. They keep their numbers, so existing links and NotebookLM sources still work; each curriculum's learning path puts them in the right place.

## Keeping it current

- **`python tools/check_repo.py`** runs offline. It checks links between files, table shapes, every section's learning blocks, PROGRESS coverage, at most three 🔑 per section, and that the generated learning paths are current. Run it after every edit session.
- **`python tools/build_index.py`** refreshes each curriculum's learning-path table and the section index on this page from the section READMEs. Reorder a learning path, or change a "When", in the curriculum README itself; the tool keeps your edits.
- **Adding material:** use the `update-curriculum` skills (ml, pcb, btc, software) or the repo-wide [`audit-curriculum`](.agents/skills/audit-curriculum/SKILL.md) skill. Both require opening every link before adding it, and citing people rather than organizations.
- **Audits:** run the audit skill about once a quarter. Reports go in [`reviews/`](reviews/). The latest is the [October 2026 deep dive](reviews/2026-10-deep-dive/README.md), which covers what was wrong, what changed, and why.

## License

Personal learning repository. All linked resources belong to their respective authors and publishers.
