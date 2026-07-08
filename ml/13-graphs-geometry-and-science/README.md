# Graphs, Geometry, and Science

Not all data lives on grids or in sequences. Molecules, social networks, physical systems, and protein structures are naturally described by graphs and geometric objects. This section covers how to build neural networks that respect the structure of such data — from basic message passing on graphs through equivariant networks that honor physical symmetries — and then shows how these ideas are driving breakthroughs in protein structure prediction, weather forecasting, materials discovery, and mathematical reasoning.

**Prerequisites:** [Section 03 – Neural Network Fundamentals](../03-neural-network-fundamentals/README.md), [Section 06 – Transformers and Attention](../06-transformers-and-attention/README.md), basic linear algebra (groups, symmetries helpful but not required)

---

## Graph Neural Networks

Message passing on graphs is the foundation for reasoning about relational data. GCNs introduced spectral graph convolutions in a scalable form, Gilmer et al. unified prior work under the message passing framework, GATs added attention to graph edges, and Bronstein et al.'s monograph provides the geometric deep learning perspective that ties it all together.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 1 | 🔑 | Paper | Semi-Supervised Classification with Graph Convolutional Networks (GCN) | Kipf & Welling | 2016 | [arxiv.org/abs/1609.02907](https://arxiv.org/abs/1609.02907) |
| 2 | | Paper | Graph Attention Networks (GAT) | Veličković et al. | 2018 | [arxiv.org/abs/1710.10903](https://arxiv.org/abs/1710.10903) |
| 3 | | Paper | Neural Message Passing for Quantum Chemistry | Gilmer et al. | 2017 | [arxiv.org/abs/1704.01212](https://arxiv.org/abs/1704.01212) |
| 4 | 🔑 | Monograph | Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges | Bronstein et al. | 2021 | [arxiv.org/abs/2104.13478](https://arxiv.org/abs/2104.13478) |

---

## Equivariant & Geometric Networks

Standard neural networks ignore the symmetries of physical systems. Equivariant networks build in rotation, translation, and reflection symmetries by construction — crucial for molecular dynamics, protein modeling, and any domain where the laws of physics don't depend on your coordinate system.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 5 | | Paper | E(n) Equivariant Graph Neural Networks | Satorras et al. | 2021 | [arxiv.org/abs/2102.09844](https://arxiv.org/abs/2102.09844) |
| 6 | | Paper | SE(3)-Transformers: 3D Roto-Translation Equivariant Attention Networks | Fuchs et al. | 2020 | [arxiv.org/abs/2006.10503](https://arxiv.org/abs/2006.10503) |

---

## AI for Science

Deep learning is accelerating scientific discovery at an unprecedented pace. AlphaFold 2 solved protein structure prediction — a 50-year grand challenge in biology. AlphaFold 3 extends to general biomolecular complexes. GraphCast produces 10-day weather forecasts in seconds, GNoME discovered millions of new stable materials, RFdiffusion generates novel proteins, and AlphaProof/AlphaGeometry push toward mathematical reasoning.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 7 | 🔑 | Paper | Highly Accurate Protein Structure Prediction with AlphaFold (AlphaFold 2) | Jumper et al. | 2021 | [nature.com](https://www.nature.com/articles/s41586-021-03819-2) |
| 8 | | Paper | Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3 | Abramson et al. | 2024 | [nature.com](https://www.nature.com/articles/s41586-024-07487-w) |
| 9 | | Paper | GraphCast: Learning Skillful Medium-Range Global Weather Forecasting | Lam et al. | 2023 | [arxiv.org/abs/2212.12794](https://arxiv.org/abs/2212.12794) |
| 10 | | Paper | Scaling Deep Learning for Materials Discovery (GNoME) | Merchant et al. | 2023 | [nature.com](https://www.nature.com/articles/s41586-023-06735-9) |
| 11 | | Paper | De Novo Design of Protein Structure and Function with RFdiffusion | Watson et al. | 2023 | [nature.com](https://www.nature.com/articles/s41586-023-06415-8) |
| 12 | 🔑 | Paper | AlphaProof & AlphaGeometry | Google DeepMind | 2024 | — |

---

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **GCN** — Start with Kipf & Welling for the simplest spectral graph convolution
2. **Neural Message Passing** — Read Gilmer et al. to see the unified framework behind all GNN variants
3. **GAT** — Understand how attention mechanisms extend to graph-structured data
4. **Geometric Deep Learning monograph** — Read Bronstein et al. for the "big picture" unifying grids, groups, and graphs
5. **Equivariant networks** — Read E(n) EGNN and SE(3)-Transformers for symmetry-aware architectures
6. **AlphaFold 2** — The landmark application of geometric deep learning to protein folding
7. **AlphaFold 3** — Extension to general biomolecular complexes
8. **AI for Science survey** — Read GraphCast, GNoME, RFdiffusion, and AlphaProof/AlphaGeometry in any order to see the breadth of scientific applications
