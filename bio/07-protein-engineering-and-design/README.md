# Protein Engineering and Design

## Why This Section Matters

Proteins are the molecular machines of life — enzymes that catalyze reactions, antibodies that recognize pathogens, and structural scaffolds that give cells their shape. For decades, engineering new proteins required either random mutagenesis (directed evolution) or painstaking physics-based modeling (Rosetta). The deep learning revolution has shattered these limitations: protein language models like ESM-2 learn the grammar of protein sequences from evolutionary data, RFdiffusion generates entirely novel protein structures from scratch, and ProteinMPNN designs sequences that fold into any target backbone. This section covers both the classical foundations and the AI-powered frontier of protein engineering — arguably the most transformative area in all of computational biology.

## Prerequisites

- [Section 01 — Biochemistry](../01-biochemistry/README.md)
- [Section 03 — Structural Biology](../03-structural-biology/README.md)
- [Section 04 — Bioinformatics and Sequence Analysis](../04-bioinformatics-and-sequence-analysis/README.md)

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📄 Paper | De Novo Design of Protein Structure and Function with RFdiffusion | Watson, J. L., Juergens, D., Bennett, N. R., Trippe, B. L., Yim, J., Eisenach, H. E., ... Baker, D. | 2023 | [Nature](https://doi.org/10.1038/s41586-023-06415-8) | Landmark paper introducing denoising diffusion for protein design — generates novel protein structures, binders, symmetric assemblies, and enzyme scaffolds with experimental validation |
| 🔑 | 🎓 Lecture | Nobel Lecture: Innovation by Evolution — Bringing New Chemistry to Life | Arnold, F. H. | 2018 | [Nobel Prize](https://www.nobelprize.org/prizes/chemistry/2018/arnold/lecture/) | Frances Arnold's Nobel lecture on directed evolution — the intellectual foundation for protein engineering, explaining how iterative rounds of mutation and selection create enzymes with novel function |
| 🔑 | 📄 Paper | Evolutionary-Scale Prediction of Atomic-Level Protein Structure with a Language Model | Lin, Z., Akin, H., Rao, R., Hie, B., Zhu, Z., Lu, W., ... Rives, A. | 2023 | [Science](https://doi.org/10.1126/science.ade2574) | ESM-2 and ESMFold — shows that a 15-billion parameter protein language model learns enough evolutionary information to predict 3D structure directly from sequence, rivaling AlphaFold2 |
| | 📄 Paper | Robust Deep Learning–Based Protein Sequence Design Using ProteinMPNN | Dauparas, J., Anishchenko, I., Bennett, N., Bai, H., Ragotte, R. J., ... Baker, D. | 2022 | [Science](https://doi.org/10.1126/science.add2187) | Introduced ProteinMPNN, a message-passing neural network that designs amino acid sequences to fold into a given backbone structure — dramatically outperforms Rosetta sequence design |
| | 📄 Paper | The Coming of Age of De Novo Protein Design | Huang, P.-S., Boyken, S. E., Baker, D. | 2016 | [Nature](https://doi.org/10.1038/nature19946) | Comprehensive review of Rosetta-based de novo design — covers the principles, successes, and challenges of computationally designing proteins from first principles |
| | 📄 Paper | Large Language Models Generate Functional Protein Sequences Across Diverse Families | Madani, A., Krause, B., Greene, E. R., Subramanian, S., Mohr, B. P., ... Fraser, J. S. | 2023 | [Nat. Biotechnol.](https://doi.org/10.1038/s41587-022-01618-2) | ProGen — demonstrates that a 1.2B-parameter autoregressive language model trained on 280M protein sequences can generate functional artificial enzymes, validated by wet-lab experiments |
| | 📄 Paper | Biological Structure and Function Emerge from Scaling Unsupervised Learning to 250 Million Protein Sequences | Rives, A., Meier, J., Sercu, T., Goyal, S., Lin, Z., ... Fergus, R. | 2021 | [PNAS](https://doi.org/10.1073/pnas.2016239118) | The original ESM paper — demonstrated that transformer language models trained on protein sequences learn biologically meaningful representations of structure, function, and evolution |
| | 🌐 Software | Rosetta Commons — Macromolecular Modeling Suite | Baker Lab & Rosetta Commons | 2024 | [Rosetta Commons](https://www.rosettacommons.org/) | The foundational software for computational protein design — includes tools for structure prediction, protein-protein docking, enzyme design, and de novo structure generation |
| | 📄 Paper | Hallucinating Symmetric Protein Assemblies | Wicky, B. I. M., Milles, L. F., Courbet, A., Ragotte, R. J., Dauparas, J., ... Baker, D. | 2022 | [Science](https://doi.org/10.1126/science.add1964) | Demonstrates "hallucination" — using neural networks to generate symmetric protein oligomers by optimizing sequences to have confident predicted structures, bridging prediction and design |
| | 🎓 Course | Baker Lab — Protein Design Lectures and Resources | Baker, D. & Baker Lab | 2024 | [Baker Lab](https://www.bakerlab.org/) | Hub for the world's leading protein design group — links to lectures, software (RFdiffusion, ProteinMPNN, RoseTTAFold), publications, and tutorials for getting started with AI protein design |

## Suggested Order

1. **Arnold Nobel Lecture (2018)** — Start with the historical foundation; understand directed evolution before learning how computation is replacing it
2. **Huang, Boyken & Baker (2016)** — Review of Rosetta-based de novo design provides the physics-based context for understanding why deep learning approaches were needed
3. **Rives et al. (2021)** — The original ESM paper shows how protein language models learn biological structure from sequence data alone
4. **Lin et al. (2023) — ESM-2** — See how scaling protein language models enables atomic-resolution structure prediction directly from sequence
5. **Watson et al. (2023) — RFdiffusion** — The breakthrough paper on generative diffusion models for protein structure design
6. **Dauparas et al. (2022) — ProteinMPNN** — Understand the inverse folding problem: given a structure, design the sequence that folds into it
7. **Wicky et al. (2022)** — "Hallucination" as a design paradigm — connects structure prediction networks to generative design
8. **Madani et al. (2023) — ProGen** — Autoregressive generation of functional proteins — a different paradigm from diffusion-based design
9. **Rosetta Commons** — Install and explore the tools; try the introductory tutorials for protein design
10. **Baker Lab resources** — Explore the latest tools (RFdiffusion, ProteinMPNN) with their GitHub repos and tutorials
