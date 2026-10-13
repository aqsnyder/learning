# Computational Chemistry and Drug Discovery

## Why This Section Matters

Developing a new drug takes over a decade and costs billions of dollars — computational methods are transforming every stage of this pipeline. Molecular docking predicts how small molecules bind to protein targets, virtual screening narrows millions of candidates to testable hits, and ADMET modeling filters out molecules that will fail in the clinic before a single experiment is run. Understanding force fields, molecular dynamics, and quantitative structure-activity relationships (QSAR) connects the physics of molecular interactions to the practical reality of drug design. These computational approaches are increasingly powered by deep learning, making this section a critical bridge between structural biology and modern AI-driven drug discovery.

## Prerequisites

- [Section 01 — Biochemistry](../01-biochemistry/README.md)
- [Section 03 — Structural Biology](../03-structural-biology/README.md)

## 🎯 Learning Objectives

After this section you can:

- Compute the Lipinski and standard ADMET descriptors for an arbitrary molecule with RDKit, and explain what the Rule of Five is actually a statement about — and about what it is not.
- Write down the terms of a classical force field and compute a single-point energy by hand for a small configuration, then verify it against an MD engine.
- Run a docking calculation, validate it by redocking against a crystal pose, and report the RMSD success rate honestly — including the drop from redocking to cross-docking.
- Explain why docking scores correlate poorly with measured affinity, naming the specific physics the scoring function omits.
- Design a virtual screen with property-matched decoys and report enrichment with ROC AUC, EF at 1%, and a confidence interval.

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
| | 📄 Paper | Ultra-Large Library Docking for Discovering New Chemotypes | Lyu, J. et al. (… Irwin, J. J.) | 2019 | [Nature](https://doi.org/10.1038/s41586-019-0917-9) | Docked ~170 million make-on-demand compounds against AmpC β-lactamase and the D4 dopamine receptor, then synthesized and tested the top hits — the empirical answer to what happens to hit rates when virtual libraries grow by orders of magnitude |
| | 📘 Textbook | Drug Design: Methodology, Concepts, and Mode-of-Action | Klebe, G. | 2013 | [Springer](https://link.springer.com/book/10.1007/978-3-642-17907-5) | Detailed textbook on structure-based drug design — covers thermodynamics of binding, pharmacophore models, fragment-based design, and lead optimization with case studies from real drug programs |

## Suggested Order

1. **Leach textbook (Chapters 1–4)** — Build foundations in force fields, energy landscapes, and molecular mechanics before touching docking
2. **Lipinski et al. (1997)** — The Rule of Five is the first filter every medicinal chemist applies; understand why these properties matter for oral bioavailability
3. **RDKit tutorials** — Get hands-on with molecular representations, fingerprints, and property calculations in Python
4. **AutoDock Vina tutorials** — Run your first docking calculations; understand receptor preparation, grid setup, and pose evaluation
5. **Kitchen et al. (2004)** — Now that you've run docking, read this review to understand the landscape of scoring functions and their limitations
6. **Shoichet (2004)** — Concise perspective on what makes virtual screening succeed or fail in practice
7. **Lyu et al. (2019)** — See how docking behaves at 10⁸-compound scale, and what was actually confirmed in the lab
8. **ZINC database** — Explore the chemical space available for virtual screening; try filtering and downloading compound libraries
9. **TeachOpenCADD notebooks** — Work through the complete CADD pipeline end-to-end in Jupyter
10. **Schneider (2018)** — Bridge to AI-driven approaches — generative models, reinforcement learning, and automated design
11. **Leach textbook (Chapters 9–12) + Klebe** — Deeper dives into molecular dynamics simulations, free energy calculations, and structure-based design case studies

---

## 🛠️ Practice

1. **Descriptor audit of real drugs** — Assemble ~50 approved oral small-molecule drugs (ChEMBL or DrugBank will give you SMILES). With RDKit compute MW, cLogP, HBD, HBA, TPSA, rotatable bonds and the Rule-of-Five violation count. Then: plot the distributions, identify every molecule violating two or more rules, and for three of them (atorvastatin, cyclosporine and one kinase inhibitor are good picks) explain *why it is still a drug* — formulation, active transport, a different route, or that the rule simply does not apply to that class. Validate a sample of your computed logP values against ChEMBL's. Deliverable: notebook, table, and 200 words on what Lipinski's paper actually claimed versus how it gets used. *(~3.5 h · RDKit tutorials; Lipinski et al. 1997; ChEMBL)*

2. **Force field by hand, then by engine** — From Leach, write out the terms of a standard molecular-mechanics force field (bond, angle, torsion, Lennard-Jones, Coulomb) with units. For a hand-built configuration of a few atoms, compute the LJ and Coulomb contributions yourself in a short script, with explicit units and a stated dielectric treatment. Then load the same configuration into OpenMM with a standard force field and compare the single-point energy term by term. Reconcile every discrepancy — the usual culprits are 1-4 scaling, cutoff and switching treatment, and units. Deliverable: the comparison table and the reconciliation notes. *(~4 h · Leach, the force-field and energy-minimization chapters; OpenMM)*

3. **Redock, then cross-dock** — Pick five protein-ligand complexes from the PDB with well-resolved co-crystallized ligands. For each: strip the ligand, prepare the receptor, redock with AutoDock Vina, and compute the RMSD of the top pose to the crystal pose. Report the fraction under 2 Å. Then cross-dock: for a target with multiple structures, dock ligand A into the receptor conformation from complex B, and report the success rate again. Deliverable: the two success-rate tables and 200 words on what the gap between them says about protein flexibility and about benchmark design. *(~5 h · AutoDock Vina tutorials; Kitchen et al. 2004; RCSB PDB)*

4. **Score versus affinity** — For one target, pull a congeneric series of ligands with measured affinities from ChEMBL or BindingDB (aim for 20+ compounds spanning at least three log units of potency). Dock them all, then plot docking score against pIC₅₀ or pK_i and compute Spearman ρ. Expect something unimpressive. Then write 300 words naming the specific physics the scoring function is not modelling: ligand and protein conformational entropy, explicit water and desolvation, protonation-state changes on binding, and the fact that the score is a sum of empirical terms fit to a heterogeneous training set. *(~4 h · Kitchen et al. 2004; Shoichet 2004; ChEMBL/BindingDB; AutoDock Vina)*

5. **A virtual screen with real metrics** — Build a screening benchmark for one target: known actives from ChEMBL, plus property-matched decoys (DUD-E style, matched on MW, logP, charge and rotatable bonds, so that you are not just rediscovering a molecular-weight bias). Dock everything and compute ROC AUC, enrichment factor at 1% and 5%, and BEDROC. Then run a purely ligand-based baseline — ECFP4 Tanimoto similarity to a single known active — and compute the same metrics. Deliverable: notebook, ROC curves for both methods on one plot, and the metric table. The uncomfortable finding (that the cheap ligand-based method is often competitive) is the point. *(~5 h · Shoichet 2004; TeachOpenCADD notebooks; RDKit; ZINC)*

6. **Screening economics, Fermi style** — ZINC holds on the order of 10⁸–10⁹ purchasable compounds in dockable 3D form. Estimate: at 1–10 s per ligand per CPU core, the core-hours and cloud cost to dock the whole library against one target; the same for a GPU-accelerated or ML-rescored pipeline. Compare to the cost of a physical high-throughput screen of 10⁶ compounds. Then compute the break-even: given a docking hit rate of ~1% confirmed and an HTS hit rate of ~0.1%, at what cost per compound does computation win? State which of your inputs is the weakest. *(~2 h · ZINC database; Schneider 2018; Shoichet 2004)*

**🏗️ Mini-project — One honest virtual screen, end to end:** Pick a target with a good holo structure and at least 100 ChEMBL actives. Run the complete pipeline and then attack your own result. Steps: receptor preparation (protonation, tautomers, which waters you keep and why); ligand preparation and conformer generation; a property-matched decoy set; docking the whole set; ML or ligand-based rescoring of the top fraction; and the full enrichment metrics with bootstrap confidence intervals. Then take your top 10 hits and triage them like a medicinal chemist: PAINS and reactive-group filters, synthetic accessibility, whether the pose makes chemical sense, and whether the compound is just a greasy high-MW outlier exploiting the scoring function. Deliverable: notebook in `projects/bio/06-virtual-screen/` plus a 2-page memo. Success criterion: the memo states your EF at 1% with a confidence interval, names the three largest sources of optimism in your own numbers (decoy bias, structure choice, actives clustered in one chemical series), and proposes the single cheapest experiment that would falsify your top hit. A memo that reports only the good numbers fails this project. *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State the Rule of Five. What was the dataset it came from, and what was it predicting — potency, bioavailability, or something else?
2. Name four terms in a classical force field and say which one is responsible for most of the computational cost in a large simulation.
3. Why does a docking score not estimate binding free energy? Name three missing contributions.
4. Your redocking success rate is 70% but your cross-docking success rate is 30%. What does that tell you, and which number is closer to what you would see on a novel target?
5. Roughly how many compounds are in ZINC, and roughly how many have ever been made and tested against any target? Estimate the ratio.
6. A colleague reports ROC AUC 0.95 on a virtual screen. What is the first question you ask about the decoys?
7. What is the difference between structure-based and ligand-based virtual screening, and when would you deliberately choose the cheaper one?
8. Explain to a smart friend in three sentences why a computer can sometimes guess which molecules will stick to a protein, and why it is wrong so often.
