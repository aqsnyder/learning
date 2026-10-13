# Structural Biology

## Why This Section Matters

Structure determines function — this is perhaps the most important principle in all of molecular biology. Structural biology reveals how proteins fold into precise three-dimensional shapes that enable catalysis, signaling, and molecular recognition. Understanding the methods of structure determination (X-ray crystallography, NMR spectroscopy, and cryo-EM), foundational concepts like Levinthal's paradox and Anfinsen's dogma, and how to navigate the Protein Data Bank is essential for anyone working at the intersection of biology and computation. The recent cryo-EM revolution and the advent of AI-based structure prediction (AlphaFold) have made structural biology one of the most dynamic frontiers in science. This section provides the foundation needed to interpret, evaluate, and work with protein structures.

## Prerequisites

- [Section 00 — Molecular Biology Fundamentals](../00-molecular-biology-fundamentals/README.md)
- [Section 01 — Biochemistry](../01-biochemistry/README.md)

## 🎯 Learning Objectives

After this section you can:

- Read a PDB entry critically: state what resolution, R-factor, R-free, B-factors and occupancy each tell you, and say which structural claims a given entry does and does not support.
- Explain the Ramachandran plot from first principles — which φ/ψ regions are forbidden and by what steric clash — and compute dihedrals directly from coordinates.
- Compare X-ray crystallography, solution NMR and cryo-EM on sample requirements, accessible size range, resolution, and the specific artefacts each introduces.
- Measure canonical secondary-structure geometry (helix rise, pitch, residues per turn; sheet rise and H-bond distances) from a real structure and check it against the textbook values.
- Distinguish AlphaFold's pLDDT and PAE from experimental confidence, and name a case where a confident prediction is wrong and a case where low confidence is the correct answer.

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📚 Textbook | Introduction to Protein Structure (2nd Edition) | Carl Branden, John Tooze | 1999 | [Book](https://www.garlandscience.com/product/isbn/9780815323051) | The classic introduction to protein structure — clear, visual, and focused on building structural intuition from first principles |
| 🔑 | 🌐 Resource | PDB-101: Learn about Structural Biology | RCSB PDB | 2024 | [PDB-101](https://pdb101.rcsb.org/) | Authoritative educational resource from the Protein Data Bank with Molecule of the Month, structural biology guides, and interactive tutorials |
| 🔑 | 🌐 Database | RCSB Protein Data Bank | RCSB PDB | 2024 | [PDB](https://www.rcsb.org/) | The primary global repository for 3D structural data of biological macromolecules — learn to search, visualize, and download structures |
| | 📚 Textbook | Protein Structure and Function | Gregory A. Petsko, Dagmar Ringe | 2004 | [Book](https://global.oup.com/academic/product/protein-structure-and-function-9780199556847) | Concise, accessible textbook connecting protein structure to biological function with excellent case studies |
| | 🎥 Videos | iBiology: Structural Biology Collection | Various (iBiology) | 2018 | [iBiology](https://www.ibiology.org/structural-biology/) | Expert lectures on X-ray crystallography, NMR, cryo-EM, and structure-function relationships from leading structural biologists |
| | 📄 Nobel Lecture | Studies on the Principles that Govern the Folding of Protein Chains | Christian B. Anfinsen | 1972 | [Nobel Lecture](https://www.nobelprize.org/prizes/chemistry/1972/anfinsen/lecture/) | Anfinsen's Nobel Prize lecture establishing that amino acid sequence determines protein structure — the foundation of the folding problem |
| | 📄 Feature | The Revolution Will Not Be Crystallized: A New Method Sweeps through Structural Biology | Ewen Callaway | 2015 | [Nature](https://doi.org/10.1038/525172a) | Nature feature on how cryo-EM transformed structural biology — context for understanding the field's current state |
| | 🎥 Nobel Lecture | Nobel Prize in Chemistry 2017: Cryo-Electron Microscopy | Jacques Dubochet, Joachim Frank, Richard Henderson | 2017 | [Nobel Lectures](https://www.nobelprize.org/prizes/chemistry/2017/summary/) | Nobel lectures by the three pioneers of cryo-EM — essential for understanding how the technique developed and why it matters |
| | 🌐 Tutorial | RCSB PDB Training Resources | RCSB PDB | 2024 | [Tutorials](https://www.rcsb.org/training) | Hands-on tutorials for searching, visualizing, and analyzing structures in the PDB — essential practical skills |
| | 📄 Paper | Highly Accurate Protein Structure Prediction with AlphaFold | John Jumper et al. (DeepMind) | 2021 | [Paper](https://doi.org/10.1038/s41586-021-03819-2) | The AlphaFold2 paper that revolutionized structure prediction — read after building structural biology foundations to appreciate its significance |
| | 📄 Paper | AlphaFold Protein Structure Database: Massively Expanding the Structural Coverage of Protein-Sequence Space with High-Accuracy Models | Mihaly Varadi et al. (EMBL-EBI & DeepMind) | 2022 | [Nucleic Acids Research](https://academic.oup.com/nar/article/50/D1/D439/6430488) | Describes the database that now sits beside the PDB with predicted structures for essentially every known protein — and, crucially, how to read its pLDDT and PAE confidence measures before you trust a model |
| | 🌐 Software | UCSF ChimeraX | RBVI, University of California San Francisco | 2026 | [ChimeraX](https://www.rbvi.ucsf.edu/chimerax/) | The successor to Chimera and the practical tool for this section: open a PDB entry or an AlphaFold model, inspect the fold, color by confidence, and measure contacts yourself — free for academic use |

## Suggested Order

1. **PDB-101** — Start with Molecule of the Month entries and structural biology guides to build visual intuition
2. **Branden & Tooze "Introduction to Protein Structure"** — Read systematically to understand structural motifs, folds, and domains
3. **Anfinsen Nobel Lecture** — Read the original statement of the protein folding problem and thermodynamic hypothesis
4. **iBiology Structural Biology Collection** — Watch lectures on experimental methods (X-ray, NMR, cryo-EM)
5. **RCSB PDB Training + UCSF ChimeraX** — Learn to search, visualize, and download structures hands-on, with a viewer you drive yourself
6. **Cryo-EM Nobel Lectures** — Understand the cryo-EM revolution and its impact on the field
7. **Callaway Nature Feature** — Read for context on how cryo-EM has transformed modern structural biology
8. **Petsko & Ringe "Protein Structure and Function"** — Deepen understanding of structure-function relationships
9. **Jumper et al. AlphaFold Paper** — Read the landmark paper that bridged structural biology and AI
10. **Varadi et al. — AlphaFold DB** — Finish by learning to judge a predicted structure: pLDDT, PAE, and where models mislead

---

## 🛠️ Practice

1. **PDB entry forensics** — Choose one protein that has been solved at several resolutions (lysozyme and myoglobin both have entries from sub-ångström to ~2.5 Å). For three entries, tabulate: resolution, R and R-free and the gap between them, mean B-factor and its spread, number of ordered waters, number of alternate conformers modelled, and any residues absent from the model. Then write, for each entry, one claim you would make from it and one you would refuse to make. Deliverable: the table plus the six claims. *(~3 h · RCSB PDB; RCSB PDB training resources; PDB-101)*

2. **Ramachandran from the coordinates up** — Write your own dihedral-angle function (four atoms → φ or ψ, via the standard cross-product formula), apply it across a whole chain from a PDB file parsed with Biopython's `Bio.PDB`, and plot the Ramachandran distribution. Validate your code against `Bio.PDB`'s own `internal_coords` or against the values in the entry's wwPDB validation report. Then identify the outliers and look each one up in the validation report or the electron density — are they real strain, a modelling error, or glycine/pre-proline residues that belong where they are? Deliverable: notebook, plot, and a verdict per outlier. *(~4 h · Branden & Tooze; Biopython; RCSB validation reports)*

3. **Measure the α-helix yourself** — From a real structure containing a long helix, measure directly from the coordinates: rise per residue, residues per turn, pitch, and the i→i+4 backbone hydrogen-bond N···O distance. Compare to the canonical 1.5 Å, 3.6, 5.4 Å. Then do the same for a β-sheet: rise per residue and inter-strand distance, parallel versus antiparallel. Deliverable: a small table of measured versus textbook values, with a sentence on any discrepancy larger than 5%. *(~2.5 h · Branden & Tooze; RCSB PDB; ChimeraX or PyMOL)*

4. **Fold conservation beyond sequence similarity** — Find two proteins with the same fold but under ~20% sequence identity (globins across distant species, or two TIM-barrel enzymes with different chemistry). Superimpose them in ChimeraX (`matchmaker`) and report: global RMSD, number of aligned residues, which regions align well and which diverge (usually loops), and where the conserved functional residues sit. Then run a plain BLASTP of one against the other and show it finds nothing convincing. Write 200 words on what this implies for annotating a new sequence. *(~3 h · RCSB PDB; ChimeraX; Petsko & Ringe; prepares Section 04's remote-homology work)*

5. **AlphaFold against experiment** — Pick a protein that has an AlphaFold DB model and an experimental structure published *after* AF2's training cutoff. Superimpose, compute per-residue Cα deviation, and plot deviation against pLDDT. Identify: a region where pLDDT honestly flags uncertainty; a region with low pLDDT that is genuinely disordered (so the model is right to be unsure); and, if you can find one, a confidently-predicted region that is wrong. Also inspect the PAE matrix and say what it tells you that pLDDT does not. Deliverable: notebook, the deviation-versus-pLDDT plot, and the three annotated cases. *(~4 h · Jumper et al. AlphaFold paper; AlphaFold DB; RCSB PDB)*

6. **Cryo-EM as a dose-limited imaging problem** — Read the Callaway Nature feature and one of the 2017 cryo-EM Nobel lectures. Then do the budget: single-particle resolution improves roughly as 1/√N in particle count, and the specimen tolerates only a limited electron dose before radiation damage. Estimate how many particle images are needed to go from 4 Å to 3 Å, and what that implies for microscope time. Then write 300 words framing cryo-EM as a detector problem — what did direct-electron detectors change about the SNR per electron, and why was that the unlock rather than better lenses? *(~3 h · Callaway, Nature feature; Dubochet/Frank/Henderson Nobel lectures; iBiology structural-biology talks)*

**🏗️ Mini-project — Structure review memo for one disease variant:** Pick a protein with a well-studied pathogenic missense or deletion variant and good structural coverage — *CFTR* (Phe508del), *TP53* DNA-binding domain (R175H, R248Q), *HBB* (Glu6Val), or a *MYH7* HCM variant. Produce a structural review memo: (i) an inventory of the experimental structures available, each with PDB ID, method, resolution, what construct was crystallised or imaged, and the specific caveats; (ii) exactly where the variant residue sits — secondary structure element, burial, and every contact within 5 Å, named by chain and residue number; (iii) what the AlphaFold model says about that region and its pLDDT; (iv) a falsifiable structural prediction about the variant's effect (destabilises the fold / disrupts a specific interface / blocks a ligand site / alters trafficking without altering the fold) and the measurement that would test it. Deliverable: a 2-page memo with 2–3 figures, in `projects/bio/03-structure-memo/`. Success criterion: every structural claim cites a specific PDB ID, chain and residue number; every claim is qualified by the resolution limit of the entry it rests on; and the prediction in (iv) is specific enough to be wrong. This memo is reused in Section 08. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What is R-free, why was it introduced, and what does a large R/R-free gap indicate?
2. A structure is deposited at 3.2 Å. Can you trust a claim about a specific side-chain rotamer? About a bound water? About the overall fold? Justify each.
3. State Anfinsen's thermodynamic hypothesis, and name a well-known class of exception to it.
4. Why is the upper-left quadrant of the Ramachandran plot nearly empty, and which residue is the big exception?
5. Roughly what fraction of PDB entries are X-ray versus cryo-EM versus NMR today, and how has that shifted in the last decade? Estimate, then check on rcsb.org.
6. A colleague says "AlphaFold solved structural biology, so we don't need crystallography." Give three concrete things experimental structure determination still provides that prediction does not.
7. B-factors are often read as "flexibility." What else can inflate a B-factor?
8. Explain to a smart friend in three sentences why knowing a protein's shape tells you what it does.
