# AI for Biology

## Why This Section Matters

The application of modern AI to biology is arguably the most consequential development in the life sciences this century. AlphaFold's solution to the protein structure prediction problem — a 50-year grand challenge — demonstrated that deep learning can produce discoveries of Nobel Prize caliber. But protein folding is only the beginning: generative models are now designing novel molecules, transformer architectures are interpreting genomic and single-cell data at scale, and geometric deep learning is capturing the 3D symmetries of molecular interactions. Understanding these methods is essential because they are not just research tools — they are becoming the primary engines of drug discovery, protein engineering, and biological understanding. This section connects your ML foundations to the biological frontier.

## Prerequisites

- [Section 03 — Machine Learning & Deep Learning](../03-machine-learning-deep-learning/README.md)
- [Section 04 — Genomics & Bioinformatics](../04-genomics-bioinformatics/README.md)
- [Section 07 — Structural Biology & Drug Discovery](../07-structural-biology-drug-discovery/README.md)

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📄 Paper | Highly Accurate Protein Structure Prediction with AlphaFold | Jumper, Evans, Pritzel, Green et al. | 2021 | [Paper](https://doi.org/10.1038/s41586-021-03819-2) | The AlphaFold 2 paper that solved the protein structure prediction problem, achieving experimental-level accuracy at CASP14 |
| 🔑 | 📄 Paper | Accurate Structure Prediction of Biomolecular Interactions with AlphaFold 3 | Abramson, Adler, Dunber, Evans et al. | 2024 | [Paper](https://doi.org/10.1038/s41586-024-07487-w) | AlphaFold 3 extends structure prediction to protein–ligand, protein–DNA/RNA, and multi-chain complexes using diffusion-based architecture |
| | 📄 Paper | Improved Protein Structure Prediction Using Potentials from Deep Learning | Senior, Evans, Jumper, Kirkpatrick et al. | 2020 | [Paper](https://doi.org/10.1038/s41586-019-1923-7) | AlphaFold 1 — the initial deep learning approach to protein structure prediction that placed first at CASP13 |
| | 📄 Paper | DiffDock: Diffusion Steps, Twists, and Turns for Molecular Docking | Corso, Stärk, Jing, Barzilay & Jaakkola | 2023 | [Paper](https://doi.org/10.48550/arXiv.2210.01776) | Generative diffusion model for blind molecular docking that treats docking as a generative problem over poses |
| | 📄 Paper | BioBERT: A Pre-trained Biomedical Language Representation Model | Lee, Yoon, Kim, Kim, Kim, So & Kang | 2020 | [Paper](https://doi.org/10.1093/bioinformatics/btz682) | Domain-specific BERT model pre-trained on biomedical literature, achieving state-of-the-art on biomedical NLP benchmarks |
| | 📄 Paper | scGPT: Toward Building a Foundation Model for Single-Cell Multi-omics Using Generative AI | Cui, Wang, Zhong, Wang, Wang & Bo | 2024 | [Paper](https://doi.org/10.1038/s41592-024-02201-0) | Foundation model for single-cell biology using generative pre-training, enabling cell type annotation, perturbation prediction, and gene network inference |
| | 📄 Paper | 3D Infomax Improves GNNs for Molecular Property Prediction | Stärk, Beaini, Corso, Tossou, Dallago, Günnemann & Liò | 2022 | [Paper](https://doi.org/10.48550/arXiv.2110.04126) | Explores how to incorporate 3D geometric information into GNNs for molecular learning and equivariant representations |
| | 🎥 Talk | AlphaFold and the Future of Biology — Nobel Lecture | John Jumper & Demis Hassabis | 2024 | [Lecture](https://www.nobelprize.org/prizes/chemistry/2024/jumper/lecture/) | Nobel Prize lecture on AlphaFold's development, from CASP competitions to solving the protein folding problem |
| | 📄 Paper | Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges | Bronstein, Bruna, Cohen, Veličković | 2021 | [Paper](https://doi.org/10.48550/arXiv.2104.13478) | Comprehensive blueprint for geometric deep learning, unifying CNNs, GNNs, and equivariant networks under a common mathematical framework |

## Suggested Order

1. **Senior et al. — AlphaFold 1** — Understand the deep learning approach that launched the protein structure prediction revolution
2. **Jumper et al. — AlphaFold 2** — Study the breakthrough that solved the protein structure prediction problem
3. **Abramson et al. — AlphaFold 3** — See how the framework extends to full biomolecular complexes with diffusion models
4. **Jumper & Hassabis Nobel Lecture** — Hear the story and vision directly from the creators
5. **Bronstein et al. — Geometric Deep Learning** — Build the mathematical foundation for understanding molecular ML architectures
6. **Stärk et al. — 3D Infomax for GNNs** — Learn how geometric information improves molecular property prediction
7. **DiffDock — Corso et al.** — See generative diffusion applied to molecular docking
8. **BioBERT — Lee et al.** — Understand how language models are adapted for biomedical text
9. **scGPT — Cui et al.** — Explore foundation models for single-cell biology
