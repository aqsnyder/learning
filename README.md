<p align="center">
  <img src="assets/banner.jpg" alt="Learning — A Curated Learning Journey" width="100%">
</p>

<h3 align="center">Curated, structured curricula for self-directed mastery</h3>

<p align="center">
  <a href="ml/">🧠 Machine Learning</a> •
  <a href="pcb/">🔌 PCB Design</a> •
  <a href="btc/">₿ Bitcoin</a> •
  <a href="software/">🏗️ Software Engineering</a>
</p>

---

## What Is This?

A personal knowledge repository containing **four structured learning curricula** — each with curated resources, ordered sections, and progress tracking. Built for deep, self-directed study paired with [NotebookLM](https://notebooklm.google.com/).

Every curriculum follows the same structure:
- **12 numbered sections** progressing from foundations to frontiers
- **Must-read markers** (🔑) highlighting absolute priorities
- **Cross-cutting references** (books, courses, blogs/tools)
- **Progress tracker** (`PROGRESS.md`) for checking off items
- **Agent skill** (`.agents/skills/update-curriculum`) for keeping content current

---

## 📚 The Curricula

### [🧠 Machine Learning](ml/)
> From the roots of AI to the latest frontiers — a complete path through modern ML.

| Highlights | |
|---|---|
| **Sections** | Historical foundations → Math → Classical ML → Neural nets → CNNs → RNNs → Transformers → Generative models → Scaling → LLMs → RL → Frontiers |
| **Special marker** | ⭐ = Ilya Sutskever's reading list ("*If you really learn all of these, you'll know 90% of what matters today*") |
| **Key resources** | Karpathy, 3Blue1Brown, Andrew Ng, Stanford CS courses, Goodfellow, Sutton & Barto |

---

### [🔌 PCB Design](pcb/)
> From electronics fundamentals to high-speed signal integrity and EMC compliance.

| Highlights | |
|---|---|
| **Sections** | Electronics → PCB anatomy → Schematic → Components → Layout → Power/grounding → Signal integrity → EMC → Stackup → DFM → Advanced → Reference projects |
| **Special marker** | ⭐ = Rick Hartley's recommended reading list |
| **Key resources** | Phil's Lab, Robert Feranec, Rick Hartley, Bogatin, Johnson & Graham, Ott |
| **Included docs** | IPC-2221, PCB Design Tutorial, Rick's Reading Recommendations (PDFs) |

---

### [₿ Bitcoin](btc/)
> From the cypherpunk manifesto to Taproot — a deep technical understanding of Bitcoin.

| Highlights | |
|---|---|
| **Sections** | History/philosophy → Cryptography → Protocol → Mining → Transactions/Script → Wallets/BIPs → P2P network → Lightning → Security/privacy → Economics → Development → Frontiers |
| **Special marker** | ⭐ = Satoshi/Cypherpunk canon |
| **Key resources** | Mastering Bitcoin (Antonopoulos), Programming Bitcoin (Song), Learn Me A Bitcoin, Lopp.net, Chaincode Labs, 3Blue1Brown |

---

### [🏗️ Software Engineering](software/)
> Mastering code in the age of AI — focused on reading, reviewing, and architecting, not typing line by line.

| Highlights | |
|---|---|
| **Sections** | CS foundations → Python → Embedded C → Code reading/review → Architecture → Testing → Systems → RTOS → Security → **Agentic AI workflows** → Version control → Professional practice |
| **Special marker** | 🤖 = AI-workflow specific resources |
| **Key resources** | Fluent Python, K&R C, DDIA, Refactoring, Code Reading, Quantum Leaps, Simon Willison, Embedded Artistry |
| **Focus** | Python + Embedded C · Senior architect mindset · Human-in-the-loop AI development |

---

## 🗂️ Repository Structure

```
learning/
├── README.md              ← you are here
├── assets/
│   └── banner.jpg
├── ml/                    ← Machine Learning curriculum
│   ├── README.md
│   ├── PROGRESS.md
│   ├── 00-historical-foundations/
│   ├── ...
│   ├── 11-frontiers/
│   ├── books/
│   ├── courses/
│   └── blogs-and-references/
├── pcb/                   ← PCB Design curriculum
│   ├── README.md
│   ├── PROGRESS.md
│   ├── 00-electronics-fundamentals/
│   ├── ...
│   ├── 11-reference-projects/
│   ├── books/
│   ├── courses/
│   ├── blogs-and-references/
│   └── documents/         (IPC-2221, tutorials, PDFs)
├── btc/                   ← Bitcoin curriculum
│   ├── README.md
│   ├── PROGRESS.md
│   ├── 00-history-and-philosophy/
│   ├── ...
│   ├── 11-advanced-and-frontiers/
│   ├── books/
│   ├── courses/
│   └── blogs-and-references/
└── software/              ← Software Engineering curriculum
    ├── README.md
    ├── PROGRESS.md
    ├── 00-cs-foundations/
    ├── ...
    ├── 11-professional-practice/
    ├── books/
    ├── courses/
    └── blogs-and-references/
```

---

## How to Use

1. **Pick a curriculum** and open its `README.md` for the full learning path
2. **Work through sections in order** — each has curated resources with 🔑 must-reads
3. **Track progress** in `PROGRESS.md` — check off items as you go
4. **Pair with NotebookLM** — upload sections or book chapters for interactive study
5. **Keep current** — use the `update-curriculum` agent skill to add new resources

---

## License

Personal learning repository. All linked resources belong to their respective authors and publishers.
