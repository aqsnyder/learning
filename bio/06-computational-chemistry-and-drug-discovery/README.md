# Computational Chemistry and Drug Discovery

## Why This Section Matters

Developing a new drug takes over a decade and costs billions of dollars — computational methods are transforming every stage of this pipeline. Molecular docking predicts how small molecules bind to protein targets, virtual screening narrows millions of candidates to testable hits, and ADMET modeling filters out molecules that will fail in the clinic before a single experiment is run. Understanding force fields, molecular dynamics, and quantitative structure-activity relationships (QSAR) connects the physics of molecular interactions to the practical reality of drug design. These computational approaches are increasingly powered by deep learning, making this section a critical bridge between structural biology and modern AI-driven drug discovery.

## Prerequisites

- [Section 01 — Biochemistry](../01-biochemistry/README.md)
- [Section 03 — Structural Biology](../03-structural-biology/README.md)

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📘 Textbook | Molecular Modelling: Principles and Applications | Leach, A. R. | 2001 | [Pearson](https://www.pearson.com/en-gb/subject-catalog/p/molecular-modelling-principles-and-applications/P200000003563) | The standard textbook for computational chemistry — covers force fields, energy minimization, molecular dynamics, Monte Carlo methods, docking, and QSAR with clear mathematical exposition |
| 🔑 | 📄 Paper | Experimental and Computational Approaches to Estimate Solubility and Permeability in Drug Discovery and Development Settings | Lipinski, C. A., Lombardo, F., Dominy, B. W., Feeney, P. J. | 1997 | [Adv. Drug Deliv. Rev.](https://doi.org/10.1016/S0169-409X(96)00423-1) | The "Rule of Five" paper — established the physicochemical guidelines (MW ≤ 500, logP ≤ 5, HBD ≤ 5, HBA ≤ 10) that still anchor oral drug design and ADMET screening |
| | 🌐 Tutorial | AutoDock Vina Documentation and Tutorials | Trott, O. & Olson, A. J. | 2024 | [AutoDock Vina](https://autodock-vina.readthedocs.io/) | Official documentation for the widely-used open-source docking program — includes step-by-step tutorials for preparing receptor/ligand files, running docking, and analyzing results |
| | 💻 Tutorial | RDKit: Open-Source Cheminformatics | Landrum, G. | 2024 | [RDKit](https://www.rdkit.org/docs/GettingStartedInPython.html) | The standard Python toolkit for cheminformatics — tutorials cover molecular representation (SMILES, fingerprints), substructure searching, property calculation, and chemical similarity |
| | 🌐 Database | ZINC Database — Free Library of Commercially Available Compounds | Irwin, J. J. & Shoichet, B. K. | 2024 | [ZINC](https://zinc.docking.org/) | Curated database of over 230 million purchasable compounds in ready-to-dock 3D formats — the go-to resource for virtual screening campaigns |
| | 📄 Paper | Docking and Scoring in Virtual Screening for Drug Discovery: Methods and Applications | Kitchen, D. B., Decornez, H., Furr, J. R., Bajorath, J. | 2004 | [Nat. Rev. Drug Discov.](https://doi.org/10.1038/nrd1549) | Comprehensive review of molecular docking algorithms, scoring functions, and their real-world application in pharmaceutical virtual screening pipelines |
| | 📄 Paper | Automating Drug Discovery | Schneider, G. | 2018 | [Nat. Rev. Drug Discov.](https://doi.org/10.1038/nrd.2017.232) | Forward-looking review covering AI and automation in drug design — de novo molecular generation, reinforcement learning for molecular optimization, and closed-loop discovery platforms |
| | 📄 Paper | Virtual Screening of Chemical Libraries | Shoichet, B. K. | 2004 | [Nature](https://doi.org/10.1038/nature03197) | Concise and influential overview of structure-based and ligand-based virtual screening — discusses what works, what fails, and how to design rigorous virtual screening experiments |
| | 🌐 Course | TeachOpenCADD — Open-Source Computer-Aided Drug Design | Volkamer Lab | 2024 | [TeachOpenCADD](https://projects.volkamerlab.org/teachopencadd/) | Free, hands-on Jupyter notebook tutorials covering the full CADD pipeline — from querying ChEMBL to pharmacophore modeling, molecular docking, and ADMET prediction using Python |
| | 📘 Textbook | Drug Design: Methodology, Concepts, and Mode-of-Action | Klebe, G. | 2013 | [Springer](https://link.springer.com/book/10.1007/978-3-642-17907-5) | Detailed textbook on structure-based drug design — covers thermodynamics of binding, pharmacophore models, fragment-based design, and lead optimization with case studies from real drug programs |

## Suggested Order

1. **Leach textbook (Chapters 1–4)** — Build foundations in force fields, energy landscapes, and molecular mechanics before touching docking
2. **Lipinski et al. (1997)** — The Rule of Five is the first filter every medicinal chemist applies; understand why these properties matter for oral bioavailability
3. **RDKit tutorials** — Get hands-on with molecular representations, fingerprints, and property calculations in Python
4. **AutoDock Vina tutorials** — Run your first docking calculations; understand receptor preparation, grid setup, and pose evaluation
5. **Kitchen et al. (2004)** — Now that you've run docking, read this review to understand the landscape of scoring functions and their limitations
6. **Shoichet (2004)** — Concise perspective on what makes virtual screening succeed or fail in practice
7. **ZINC database** — Explore the chemical space available for virtual screening; try filtering and downloading compound libraries
8. **TeachOpenCADD notebooks** — Work through the complete CADD pipeline end-to-end in Jupyter
9. **Schneider (2018)** — Bridge to AI-driven approaches — generative models, reinforcement learning, and automated design
10. **Leach textbook (Chapters 9–12) + Klebe** — Deeper dives into molecular dynamics simulations, free energy calculations, and structure-based design case studies
