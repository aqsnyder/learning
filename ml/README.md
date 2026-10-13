# 🧠 Machine Learning — A Learning Journey

> A curated, ordered collection of the best resources for understanding modern AI — from historical roots to cutting-edge research.

## Purpose

This repository is a structured curriculum for self-studying machine learning and artificial intelligence. It compiles the most important books, papers, video lectures, blog posts, and online courses into a coherent learning path.

**Designed for pairing with [NotebookLM](https://notebooklm.google.com/)** — feed individual sections or papers into NotebookLM for interactive study sessions.

---

## Legend

| Symbol | Meaning |
|--------|---------|
| 🔑 | **Must-read / must-watch** — absolute priority items |
| ⭐ | **Ilya Sutskever's reading list** — from the famous ~30 paper list given to John Carmack |
| 🔑⭐ | Both — a must-read that's also on Ilya's list |

---

## Learning Path

Work through the numbered sections in order. Each section's README contains curated resources with direct links, descriptions, and a suggested reading order within that section.

```
Section 00  →  Historical Foundations
Section 01  →  Mathematical Foundations
Section 02  →  Classical Machine Learning
Section 03  →  Neural Network Fundamentals
Section 04  →  CNNs and Computer Vision
Section 05  →  RNNs, Sequences, and Memory
Section 06  →  Transformers and Attention
Section 07  →  Generative Models
Section 08  →  Scaling, Efficiency, and Deployment
Section 09  →  Large Language Models
Section 10  →  Reinforcement Learning
Section 11  →  Frontiers (2023–2026+)
Section 12  →  Interpretability and Alignment
Section 13  →  Graphs, Geometry, and Science
```

### Cross-Cutting References

| Directory | Contents |
|-----------|----------|
| [books/](books/) | Curated book list with reading order |
| [courses/](courses/) | Video lectures and MOOCs in recommended sequence |
| [blogs-and-references/](blogs-and-references/) | Essential blogs, newsletters, conferences |

---

## ⭐ Ilya Sutskever Reading List — Cross-Reference

> *"If you really learn all of these, you'll know 90% of what matters today."*
> — Ilya Sutskever (to John Carmack)

Source: [dzyim/ilya-sutskever-recommended-reading](https://github.com/dzyim/ilya-sutskever-recommended-reading)

| # | Paper / Resource | Section |
|---|------------------|---------|
| 1 | The Annotated Transformer (Rush, Harvard NLP) | [06 — Transformers](06-transformers-and-attention/) |
| 2 | The First Law of Complexodynamics (Aaronson) | [01 — Math Foundations](01-math-foundations/) |
| 3 | The Unreasonable Effectiveness of RNNs (Karpathy) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 4 | Understanding LSTM Networks (Olah) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 5 | Recurrent Neural Network Regularization (Zaremba et al.) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 6 | Keeping Neural Networks Simple by Minimizing the Description Length of the Weights (Hinton & van Camp) | [03 — NN Fundamentals](03-neural-network-fundamentals/) |
| 7 | Pointer Networks (Vinyals et al.) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 8 | ImageNet Classification with Deep CNNs — AlexNet (Krizhevsky et al.) | [04 — CNNs](04-cnns-and-computer-vision/) |
| 9 | Order Matters: Sequence to Sequence for Sets (Vinyals et al.) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 10 | GPipe (Huang et al.) | [08 — Scaling](08-scaling-and-training/) |
| 11 | Deep Residual Learning — ResNet (He et al.) | [04 — CNNs](04-cnns-and-computer-vision/) |
| 12 | Multi-Scale Context Aggregation by Dilated Convolutions (Yu & Koltun) | [04 — CNNs](04-cnns-and-computer-vision/) |
| 13 | Neural Message Passing for Quantum Chemistry (Gilmer et al.) | [13 — Graphs & Science](13-graphs-geometry-and-science/) |
| 14 | Attention Is All You Need (Vaswani et al.) | [06 — Transformers](06-transformers-and-attention/) |
| 15 | Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau et al.) | [06 — Transformers](06-transformers-and-attention/) |
| 16 | Identity Mappings in Deep Residual Networks (He et al.) | [04 — CNNs](04-cnns-and-computer-vision/) |
| 17 | A Simple Neural Network Module for Relational Reasoning (Santoro et al.) | [13 — Graphs & Science](13-graphs-geometry-and-science/) |
| 18 | Variational Lossy Autoencoder (Chen et al.) | [07 — Generative](07-generative-models/) |
| 19 | Relational Recurrent Neural Networks (Santoro et al.) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 20 | Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton (Aaronson et al.) | [01 — Math Foundations](01-math-foundations/) |
| 21 | Neural Turing Machines (Graves et al.) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 22 | Deep Speech 2: End-to-End Speech Recognition in English and Mandarin (Amodei et al.) | [05 — RNNs](05-rnns-sequences-and-memory/) |
| 23 | Scaling Laws for Neural Language Models (Kaplan et al.) | [08 — Scaling](08-scaling-and-training/) |
| 24 | A Tutorial Introduction to the Minimum Description Length Principle (Grünwald) | [01 — Math](01-math-foundations/) / [03 — NN Fundamentals](03-neural-network-fundamentals/) |
| 25 | Machine Super Intelligence (Legg, PhD thesis) | [01 — Math Foundations](01-math-foundations/) |
| 26 | Kolmogorov Complexity and Algorithmic Randomness (Shen, Uspensky & Vereshchagin) | [01 — Math Foundations](01-math-foundations/) |
| 27 | Stanford CS231n: Convolutional Neural Networks for Visual Recognition | [04 — CNNs](04-cnns-and-computer-vision/) |

> Numbering follows the source list (27 items). Three papers that were previously cross-listed here are **not** on the list, though they remain in the curriculum without ⭐: *Generating Sequences with RNNs* (Graves) and *Sequence to Sequence Learning* (Sutskever et al.) in Section 05, and *Variational Inference with Normalizing Flows* (Rezende & Mohamed) in Section 07.

---

## How to Use with NotebookLM

1. **Section-by-section**: Upload a section's README to NotebookLM as a source for study guidance
2. **Papers**: Download PDFs of papers and upload them directly for deep-dive conversations
3. **Books**: Upload free book chapters or PDFs for interactive Q&A
4. **Progress tracking**: Use [PROGRESS.md](PROGRESS.md) to track what you've completed

---

## Keeping Current

The [Frontiers section](11-frontiers/) covers the latest developments. To update the curriculum with new papers and resources, use the `.agents/skills/update-curriculum` skill.

---

## License

This is a personal learning repository. All linked resources belong to their respective authors and publishers.
