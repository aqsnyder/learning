# Biology & Computational Life Sciences — Review

> **Deep-dive review, October 2026** · curriculum: [`bio/`](../../bio/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict

The curriculum has a genuinely good spine: the arc molecular biology → biochemistry → genetics → structure → sequence analysis → systems → drug discovery → protein design → clinic → AI is the right order, the "Why This Section Matters" essays are well written and motivating, and the resource picks are mostly canonical rather than random (Alberts, Lehninger, Durbin, Alon, Dayan & Abbott, RFdiffusion, ProteinMPNN, ESM). Where it falls short is currency and verification: the AI-generated citations carry a visible hallucination signature (a fictitious "Bhatt" author appears twice, an Anfinsen lecture title that does not exist, a cryo-EM feature dated five years wrong, three wrong textbook author lists, a false "most-cited paper in biology" claim), the 2024 Nobel Prize for **protein design** was missing from the protein-design section entirely, and whole areas that moved in 2024–2026 were absent — open AF3-class models, Evo 2, ESM3, base/prime editing, the first approved CRISPR therapy, whole-brain connectomics. Structurally, `PROGRESS.md` tracked only ~6 items per section against ~110 resources (it was a template, not a tracker), six prerequisite links pointed at directories that never existed, and the curriculum had no statistics, no instrumentation, and no biosecurity content at all. Overall grade: **B−** (strong skeleton, unreliable flesh, now considerably better). The single most important improvement already made: Section 08 and Section 10 are no longer frozen in 2022 — genome editing now runs through base/prime editing to Casgevy and the first n-of-1 in-vivo therapy, and AI-for-biology now includes runnable open models plus the dual-use problem.

## Scorecard

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 — Molecular Biology Fundamentals | 4 | 4 | 4 | 5 | 4 | B+ | Solid canon; was conceptually rich but numerically empty — quantitative intuition added |
| 01 — Biochemistry | 4 | 3 | 3 | 5 | 4 | B | Right books, but an edition behind and one citation was a chimera |
| 02 — Genetics and Genomics | 3 | 3 | 2 | 4 | 3 | C+ | Stopped at 2001/2012; no sequencing technology, no T2T, no gnomAD (all three added) |
| 03 — Structural Biology | 4 | 2 | 3 | 5 | 4 | B− | Best-sequenced section in the curriculum, worst citation hygiene (3 errors) |
| 04 — Bioinformatics and Sequence Analysis | 4 | 3 | 3 | 5 | 4 | B | Excellent classical core; no statistics and no single-cell until now |
| 05 — Systems Biology | 4 | 3 | 4 | 5 | 4 | B+ | Alon-centred and coherent; the two founding synthetic circuits were missing |
| 06 — Computational Chemistry and Drug Discovery | 4 | 4 | 3 | 4 | 4 | B | Good practical pipeline; MD/free-energy and ML-docking coverage still thin |
| 07 — Protein Engineering and Design | 4 | 4 | 3 | 5 | 4 | B+ | Great paper set, but the 2024 Nobel and ESM3 were absent from the design section |
| 08 — Genomic Medicine | 2 | 4 | 1 | 3 | 3 | C− | Broken prerequisites, no base/prime editing, no approved therapy — the weakest section, now fixed |
| 09 — Neuroscience | 3 | 4 | 2 | 3 | 3 | C+ | Classic-heavy, hands-on-light; prerequisite pointed at a nonexistent section |
| 10 — AI for Biology | 4 | 3 | 3 | 4 | 3 | B− | All three prerequisites broken; papers-only, nothing runnable, no risk discussion |
| 11 — Frontiers | 4 | 3 | 3 | 4 | 4 | B | Good thematic shape; a factual error in the whole-cell prose, missing Evo 2 |

## Section-by-section

### 00 — Molecular Biology Fundamentals
- **Strengths:** Best-chosen entry path in the repo — Khan → Lander's MITx course → Drew Berry animations → Alberts is exactly how a self-learner should approach this. Lodish as a deliberate second opinion is a thoughtful touch, and Schrödinger at the end (not the start) is the right call.
- **Problems:** ✔ Alberts' link pointed at `garlandscience.com`, which now 302-redirects to the Routledge home page (dead product page) — repointed to the W. W. Norton page, which is the actual 7th-edition publisher. ✔ The edX course is **7.00x**, not 7.01x (wrong in the section, the Suggested Order, `courses/`, and `PROGRESS.md`). ✔ Lodish 9th-edition author list omitted Michael Yaffe and mis-ordered Martin/Amon. ✱ "MIT 7.012 Introductory Biology" — the OCW course title is *Introduction to Biology*; cosmetic, left alone.
- **Missing:** Numbers. The section taught mechanisms with no sense of scale, concentration, rate, or energy — the thing an engineer needs first. Also no explicit treatment of lab methods (PCR, cloning, blotting, flow cytometry), which stays a curriculum-wide gap.
- **Added:** Cell Biology by the Numbers — Ron Milo & Rob Phillips — 2015

### 01 — Biochemistry
- **Strengths:** Lehninger + MIT 5.07SC with problem sets is the strongest textbook/course pairing in the curriculum. Voet as the "deepest treatment" tier and Dill's folding review as the bridge into Section 03 both show real judgment.
- **Problems:** ✔ Stryer was listed as 9th ed. (2019) when the 10th ed. (2023) exists and adds Justin Hines as co-author — row updated, including the new publisher URL. ✔ The Dill & MacCallum entry was a chimera: a title I could not verify anywhere ("The Protein Folding Problem: A Major Conundrum of Science") attached to a Protein Science DOI, under authors and a year that match their *Science* 2012 review. Replaced with the verified record (*The Protein-Folding Problem, 50 Years On*, Science 338:1042–1046, DOI 10.1126/science.1219021).
- **Missing:** Biophysics/thermodynamics as a discipline (statistical mechanics of binding, diffusion, free energy) — proposed as a new section below. Nothing on experimental biochemistry (assays, kinetics measurement).
- **Added:** nothing needed (the correction was the work here)

### 02 — Genetics and Genomics
- **Strengths:** Mukherjee-first sequencing is a genuinely good motivational choice. Lander et al. (2001) as a primary-source read is right.
- **Problems:** ✔ Griffiths 12th-edition authors were the 11th-edition lineup (Wessler and Carroll are no longer authors; Peichel and Wassarman are) — corrected. ✱ Watson *Molecular Biology of the Gene* is listed at the 7th ed. (2013); a later edition exists but I could not verify its year before the web budget ran out — flagged, not changed. ✱ Both Broad Institute rows failed to load when fetched (likely dead): "A Brief Guide to Genomics" is in fact an **NHGRI** title, so that row looks like a mis-attribution of a page the section already cites via NHGRI. Left for the URL audit; also listed as a cut candidate.
- **Missing:** How sequencing actually works (there was nothing on platforms, read lengths, or error profiles); the current reference genome (T2T); population-scale variant resources (gnomAD) that everything downstream depends on; and evolution/population genetics as a topic — Hardy-Weinberg, drift, selection, coalescent — which the curriculum never covers anywhere (proposed as a new section below).
- **Added:**
  - Coming of Age: Ten Years of Next-Generation Sequencing Technologies — Goodwin, McPherson & McCombie — 2016
  - The Complete Sequence of a Human Genome (T2T-CHM13) — Nurk et al. — 2022
  - The Mutational Constraint Spectrum Quantified from Variation in 141,456 Humans (gnomAD) — Karczewski et al. — 2020

### 03 — Structural Biology
- **Strengths:** The Suggested Order here is the best in the curriculum: visual intuition → folds → the original folding-problem statement → methods → hands-on PDB → cryo-EM → AlphaFold. Method coverage (X-ray/NMR/cryo-EM) is balanced.
- **Problems:** Three verified citation errors, all fixed: ✔ the Anfinsen Nobel lecture is *Studies on the Principles that Govern the Folding of Protein Chains*, not "The Chemical Thermodynamics of the Protein Molecule"; ✔ the Callaway cryo-EM feature is **2015** (Nature 525:172–174, DOI 10.1038/525172a) — the DOI in the repo pointed at a *different* 2020 Callaway article about atomic-resolution microscopy; ✔ the iBiology speaker credit named "Eva Bhatt," who does not appear to exist (probably a garbling of Eva Nogales) — replaced with a neutral credit. ✱ Branden & Tooze still points at `garlandscience.com`, which is dead the same way Alberts' link was; I had no verified replacement URL — flag for the URL audit.
- **Missing:** A viewer the learner actually drives (the section said "visualize" nine times and named no tool), and the AlphaFold DB with its confidence metrics — the single most practical skill in modern structural biology is knowing when *not* to trust a predicted model. Also no cryo-EM data-processing or structure-validation practice.
- **Added:**
  - AlphaFold Protein Structure Database — Varadi et al. — 2022
  - UCSF ChimeraX — RBVI, UCSF (free for academic use)

### 04 — Bioinformatics and Sequence Analysis
- **Strengths:** Durbin chapter-by-chapter interleaved with BLAST hands-on and Eddy's HMM primer is excellent pedagogy. Rosalind is the right practice platform.
- **Problems:** ✔ The BLAST (1990) description claimed it "remains the most-cited paper in biology" — false: *Nature*'s 2014 all-time citation tally puts BLAST 12th (PSI-BLAST 14th); #1 is Lowry et al. (1951). Rewritten with the correct ranking. ✱ Rosalind is attributed to "Compeau, P. & Pevzner, P." — they wrote the companion textbook, but Rosalind is a team project; I could not verify the correct credit before the budget ran out. ✱ Mount (2004) and Higgins & Taylor (2000) are both 20+ years old and add little next to Durbin — cut candidates.
- **Missing:** Statistics (there was no inference, multiple-testing, or experimental-design content anywhere in the curriculum — the most important gap in the whole thing); modern omics analysis (RNA-seq, single-cell), which is where most real biological data work happens today; and workflow/reproducibility tooling (Snakemake/Nextflow, conda, containers) — still a gap.
- **Added:**
  - Bioinformatics Algorithms: An Active Learning Approach — Compeau & Pevzner — 2024 (free chapters + lecture videos; the text behind Rosalind's Textbook Track)
  - Modern Statistics for Modern Biology — Holmes & Huber — 2019 (free, CC-licensed)
  - Single-Cell Best Practices — Heumos, Schaar et al. — 2023 (free Jupyter book behind the Nat. Rev. Genet. review)

### 05 — Systems Biology
- **Strengths:** The most intellectually coherent section — Alon's design-principles frame, the two 2002 motif papers read against the textbook chapters, then network topology. Exactly the right content for an engineer.
- **Problems:** ✔ MIT 8.591J was attributed to "Bhatt, D. & Bhatt, J." — the instructor is **Jeff Gore** (same fictitious "Bhatt" that appeared in Section 03; a clear generator artifact). ✔ Klipp 2nd-edition author list included Herwig and Lehrach, who are 1st-edition authors only; the publisher page also does not support the "MATLAB/Python examples" claim — both corrected. ✔ Typo "systems biology roadm" → "roadmap". ✱ CellDesigner is somewhat dated as the only modelling tool; a Python/SBML path would serve better.
- **Missing:** The founding synthetic circuits — the repressilator and the toggle switch, both published back-to-back in 2000 — were absent, which is strange in a section built on circuit design (and they connect directly to Section 11's synthetic biology). Also no stochasticity/noise in gene expression, and no flux-balance/metabolic modelling practice.
- **Added:**
  - A Synthetic Oscillatory Network of Transcriptional Regulators (repressilator) — Elowitz & Leibler — 2000
  - Construction of a Genetic Toggle Switch in *E. coli* — Gardner, Cantor & Collins — 2000
  - Biological Circuit Design — Elowitz & Bois (Caltech, free, Python)

### 06 — Computational Chemistry and Drug Discovery
- **Strengths:** The only section with a real end-to-end practical pipeline (RDKit → Vina → ZINC → TeachOpenCADD), and the order puts theory where it belongs: after the learner has docked something.
- **Problems:** ✔ Fixed duplicated numbering in the Suggested Order (two "8." items). ✱ Leach (2001) is the sole MD/force-field reference and is now dated for GPU-era simulation; ✱ Kitchen (2004) and Shoichet (2004) are both fine but the section has no post-2018 ML-docking or free-energy content besides Schneider (2018).
- **Missing:** Molecular dynamics as a practiced skill (OpenMM/GROMACS), free-energy methods (FEP), ADMET/toxicity modelling in practice, and the ML-for-chemistry generation that now dominates (equivariant potentials, co-folding). Boltz-2's affinity prediction (added to Section 10) partly covers the last point.
- **Added:** Ultra-Large Library Docking for Discovering New Chemotypes — Lyu et al. — 2019

### 07 — Protein Engineering and Design
- **Strengths:** The best-curated paper set in the curriculum — Arnold → Rosetta review → ESM → ESM-2 → RFdiffusion → ProteinMPNN → hallucination → ProGen is a real syllabus, and the ordering (history before method) is correct.
- **Problems:** ✱ No errors found in the existing citations here. The gap was conceptual: the section covered the AI-design revolution but not the fact that it won the 2024 Nobel Prize in Chemistry, and the Baker Lab row (a lab homepage) was doing the work that a Nobel lecture should.
- **Missing:** Experimental validation and assay design (how designs are actually tested — yeast display, deep mutational scanning); antibody engineering specifically; and ESM3 as the generative successor to ESM-2.
- **Added:**
  - Nobel Lecture: De Novo Protein Design — David Baker — 2024 (marked 🔑)
  - Scientific Background to the Nobel Prize in Chemistry 2024: Computational Protein Design and Protein Structure Prediction — Nobel Committee for Chemistry — 2024
  - Simulating 500 Million Years of Evolution with a Language Model (ESM3) — Hayes et al. — Science 387:850–858, 2025

### 08 — Genomic Medicine
- **Strengths:** Jinek (2012) + ACMG/AMP (2015) + ClinVar is the right clinical core, and the section correctly separates mechanism, interpretation framework, and database practice.
- **Problems:** ✔ Both prerequisite links were broken (pointed at `02-molecular-biology-genetics/` and `04-genomics-bioinformatics/`, which never existed) — repointed to Sections 02 and 04. ✔ `pharmgkb.org` now 302-redirects to **ClinPGx**; row retitled and relinked. ✔ The Suggested Order called the first paper "Doudna & Charpentier," while the table (correctly) lists Jinek et al. 2012 — aligned. The same mismatch in `bio/README.md` ("Science 2014") and `PROGRESS.md` is fixed too.
- **Missing:** This was the most outdated section in the curriculum. It had **no base editing, no prime editing, no delivery (LNP/AAV), and no approved therapy** — it stopped at 2019 while the field delivered the first CRISPR medicine and the first bespoke in-vivo edit. Also still missing: newborn/population screening programmes, polygenic risk scores, and the economics/ethics of $2M+ therapies.
- **Added:**
  - Genome Editing with CRISPR–Cas Nucleases, Base Editors, Transposases and Prime Editors — Anzalone, Koblan & Liu — 2020 (marked 🔑)
  - FDA Approves First Gene Therapies to Treat Patients with Sickle Cell Disease — FDA — 8 Dec 2023
  - Exagamglogene Autotemcel for Severe Sickle Cell Disease — Frangoul et al. — NEJM 390:1649–1662, 2024
  - Patient-Specific In Vivo Gene Editing to Treat a Rare Genetic Disease ("baby KJ") — Musunuru et al. — NEJM 2025

### 09 — Neuroscience
- **Strengths:** Hodgkin-Huxley as a primary source, Gerstner's free textbook before Dayan & Abbott, and Kandel as reference-not-reading is a sensible ramp. Good database/project picks (Allen, HCP).
- **Problems:** ✔ The only prerequisite was `../00-mathematical-foundations/README.md`, a section that does not exist in `bio` — replaced with bio Section 00 plus explicit cross-links into `math/01`, `math/02`, `math/03`, and `math/07` (this section genuinely needs ODEs and probability). ✱ Dayan & Abbott is dated 2001 in the section and 2005 in `books/` — I aligned `books/` to 2001 for internal consistency (the linked MIT Press ISBN is the later paperback); flagging rather than claiming web verification.
- **Missing:** Anything hands-on (there was no course with exercises, no data analysis, no code) and anything about **instrumentation** — how neural signals are actually acquired, which is the part of neuroscience closest to Aaron's own work. Also no modern systems/circuit neuroscience beyond 1962, and nothing connecting to NeuroAI (predictive coding, representational similarity).
- **Added:**
  - Neuromatch Academy — Computational Neuroscience (free, CC BY) — marked 🔑
  - Fully Integrated Silicon Probes for High-Density Recording of Neural Activity (Neuropixels) — Jun et al. — 2017
  - Neuronal Wiring Diagram of an Adult Brain (FlyWire) — Dorkenwald et al. — 2024

### 10 — AI for Biology
- **Strengths:** The AlphaFold 1 → 2 → 3 progression is the right backbone, and including the geometric-deep-learning monograph gives the section real mathematical grounding rather than a paper list.
- **Problems:** ✔ All three prerequisite links were broken (`03-machine-learning-deep-learning`, `04-genomics-bioinformatics`, `07-structural-biology-drug-discovery` — none exist) — repointed to bio Sections 03/04/06 and across to `ml/03`, `ml/06`, `ml/13`. ✔ AlphaFold 3 author "Dunber" → **Dunger**. ✔ scGPT authors "Cui, Wang, Zhong, Wang, Wang & Bo" → Cui, Wang, Maan, Pang, Luo, Duan & Wang ("Bo" was Bo Wang's given name read as a surname). ✔ The Nobel row invented a lecture title ("AlphaFold and the Future of Biology") credited jointly to Jumper and Hassabis — they gave *separate* lectures; the row now carries Jumper's real title and notes Hassabis's. ✱ BioBERT (2020) is the weakest entry — biomedical NLP has moved to general LLMs; cut candidate.
- **Missing:** Anything runnable (the whole section was papers; AF3 class models are now open and can be installed), and any treatment of **dual-use risk** — a section that teaches generative biology with no mention of misuse is a real omission for someone who may build tools in this space. Also still missing: benchmarks/evaluation culture (CASP, PoseBusters-type critiques) and the growing literature on where these models fail.
- **Added:**
  - AlphaFold 3 open-source inference implementation — Google DeepMind — 2024 (Apache-2.0)
  - Boltz-1 / Boltz-2 — Wohlwend, Corso, Passaro et al. (MIT) — MIT-licensed code *and* weights
  - Dual Use of Artificial-Intelligence-Powered Drug Discovery — Urbina, Lentzos, Invernizzi & Ekins — 2022

### 11 — Frontiers
- **Strengths:** The thematic-subsection format works well and the prose paragraphs genuinely explain why each cluster matters. Good pairing of a foundational paper with a recent one in each theme.
- **Problems:** ✔ The whole-cell prose said Thornburg et al. modelled "a minimal *E. coli*-like synthetic cell" — it is **JCVI-syn3A**, a 493-gene minimal cell derived from *Mycoplasma*; corrected. ✔ scGPT author credit fixed here too. ✱ The Sinclair *Lifespan* entry's description ("advancing the information theory of aging") reads promotional for a book whose claims are contested — cut candidate or needs a caveat. ✱ The Neuralink row is a company homepage, not a learning resource.
- **Missing:** A **biosecurity / dual-use** subsection (see below), and spatial omics / organoids as frontier areas. Foundation-model coverage stopped at Evo 1 and Geneformer.
- **Added:**
  - Genome Modelling and Design Across All Domains of Life with Evo 2 — Brixi et al. — Nature 652:1349–1361, 2026
  - How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities — Bunne et al. — Cell 2024 (free arXiv version linked)

### books/
- **Strengths:** The "do not read cover-to-cover" framing and the explicit Alberts → The Gene → Lehninger start order are good.
- **Problems:** ✔ Dayan & Abbott year disagreed with Section 09 (2005 vs 2001) — aligned to 2001. ✱ Nine of thirteen rows have no link at all and six have empty Notes, so the table is thinner than the section tables it is meant to summarize. ✱ Only one free book was listed before this review; four of the five best free texts in the curriculum were missing.
- **Added:** Cell Biology by the Numbers (Milo & Phillips, 2015); Modern Statistics for Modern Biology (Holmes & Huber, 2019, marked 🔑); Bioinformatics Algorithms (Compeau & Pevzner, 2024); Biological Circuit Design (Elowitz & Bois)

### courses/
- **Problems:** ✔ "MIT 7.01x" → MITx **7.00x**. ✔ MIT 7.03's instructor column said "MIT OCW"; set to Chris Kaiser to match the section. ✱ Two significant courses in the sections were absent from this file (8.591J, and no hands-on neuroscience course existed at all).
- **Added:** MIT 8.591J Systems Biology (Jeff Gore, OCW); Neuromatch Academy — Computational Neuroscience (marked 🔑)

### blogs-and-references/
- **Strengths:** Compact and well chosen — Derek Lowe, Lior Pachter, and The Transmitter are all genuinely good, and the conference list is right for computational biology.
- **Problems:** ✱ Nothing verifiably wrong, but **Key Databases** omits AlphaFold DB, gnomAD, UniProt's companion InterPro, ClinVar, and ChEMBL/ZINC even though sections depend on them; Community omits ChimeraX, scverse/Scanpy, and Nextflow/Snakemake. I added nothing here because I could not verify the site URLs before the web budget ran out — these are the highest-value additions left for a follow-up pass.
- **Added:** nothing (unverified — see Structural observations)

### PROGRESS.md
- **Problems:** ✔ This was the worst structural defect in the curriculum: every section had exactly 6–7 checkboxes regardless of content — 75 section lines against ~120 actual resources, a template masquerading as a tracker. Rewritten so each section lists every resource in that section, ordered to match its Suggested Order: 87 checkbox lines → 166, with every original line preserved (six appear in corrected form — Milo for Alon, Jinek 2012 for "Doudna & Charpentier 2014", Callaway 2015, Jumper's real lecture title, Nielsen/Voigt, scGPT — and none deleted). ✔ Also fixed here: "Doudna & Charpentier — CRISPR (Science 2014)" → Jinek et al. 2012; "Alon — Network Motifs" → Milo et al.; "MIT 7.01x" → 7.00x; the invented joint Jumper/Hassabis lecture title.
- **Remaining:** ✱ The "Books (supplementary)" block still duplicates `books/README.md`; one of the two should become a pointer.

### README.md
- **Problems:** ✔ Landmark-papers table disagreed with its own sections twice — "Doudna & Charpentier — CRISPR-Cas9 (Science 2014)" vs. the section's Jinek et al. 2012, and "Alon — Network Motifs" vs. Milo et al.; both corrected. ✱ The Legend defines only 🔑 while every section uses a type-emoji vocabulary (📚/📘/📄/🎓/🎥/🌐/💻/🗃️) that is never explained, and is inconsistent between sections (📚 Textbook in 00–03, 📘 Textbook in 04–06). ✱ No prerequisite/dependency graph, though the sections now carry accurate prerequisites. ✱ The Key Textbooks and Landmark Papers tables don't include the 2024 Nobel work at all — worth one row each; not changed, since the brief asked not to restructure the README.
- **Note:** The root `/README.md` (outside `bio/`) summarizes this curriculum's key resources as "Alberts, Lehninger, Durbin, Dayan & Abbott, AlphaFold, RFdiffusion, ESM-2" — accurate, but it also claims every curriculum has an `update-curriculum` agent skill, which `bio/` does not have (only `ml`, `btc`, `pcb`, `software` do). (Fixed: the root README now says accurately which curricula have the skill, and the root `audit-curriculum` skill covers the rest.)

## Corrections made

| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| bio/00/README.md:11 | Alberts link `garlandscience.com/product/isbn/9780393884821` (302s to Routledge home) | `wwnorton.com/books/9780393884821` | https://wwnorton.com/books/9780393884821 |
| bio/00/README.md:12, :24; courses:7; PROGRESS | "MIT 7.01x" | "MITx 7.00x" | https://www.edx.org/learn/biology/massachusetts-institute-of-technology-introduction-to-biology-the-secret-of-life |
| bio/00/README.md:14 | Lodish 9th-ed authors (no Yaffe; Martin/Amon mis-ordered) | …Ploegh, Kelsey C. Martin, Michael Yaffe, Angelika Amon | https://store.macmillanlearning.com/us/product/Molecular-Cell-Biology/p/1319208525 |
| bio/01/README.md:17 | Biochemistry 9th ed., 2019, Berg/Tymoczko/Gatto/Stryer | 10th ed., 2023, Berg/Gatto/Hines/Tymoczko/Stryer (+ new URL) | https://www.macmillanlearning.com/college/us/product/Biochemistry/p/1319333621 |
| bio/01/README.md:23 | "The Protein Folding Problem: A Major Conundrum of Science", DOI 10.1002/pro.2096 | "The Protein-Folding Problem, 50 Years On", DOI 10.1126/science.1219021 | https://api.crossref.org/works/10.1126/science.1219021 |
| bio/02/README.md:19 | Griffiths, Wessler, Carroll, Doebley (11th-ed lineup) | Griffiths, Doebley, Peichel, Wassarman | https://store.macmillanlearning.com/us/product/Introduction-to-Genetic-Analysis/p/1319286445 |
| bio/03/README.md:20 | iBiology speakers "Eva Bhatt, Wah Chiu, et al." | "Various (iBiology)" | iBiology page unreachable; "Eva Bhatt" unverifiable — same fabricated name as bio/05 |
| bio/03/README.md:21 | Anfinsen lecture "The Chemical Thermodynamics of the Protein Molecule" | "Studies on the Principles that Govern the Folding of Protein Chains" | https://www.nobelprize.org/prizes/chemistry/1972/anfinsen/lecture/ |
| bio/03/README.md:22 | Callaway cryo-EM feature, 2020, DOI 10.1038/d41586-020-01658-1 (a different article) | 2015, DOI 10.1038/525172a (Nature 525:172–174) | https://api.crossref.org/works/10.1038/525172a |
| bio/04/README.md:20 | BLAST "remains the most-cited paper in biology" | "ranks 12th on *Nature*'s 2014 tally… (PSI-BLAST 14th)" | https://www.nature.com/news/the-top-100-papers-1.16224 |
| bio/05/README.md:18 | Klipp et al. incl. Herwig & Lehrach; "MATLAB/Python examples" | Klipp, Liebermeister, Wierling, Kowald (2nd ed.); companion-site software | https://www.wiley-vch.de/en/areas-interest/natural-sciences/systems-biology-978-3-527-33636-4 |
| bio/05/README.md:22 | "systems biology roadm" | "roadmap" | typo |
| bio/05/README.md:24 | MIT 8.591J instructors "Bhatt, D. & Bhatt, J." | "Gore, J." | https://ocw.mit.edu/courses/8-591j-systems-biology-fall-2014/ |
| bio/06/README.md:37–38 | Suggested Order had two items numbered "8." | renumbered 8–11 | internal |
| bio/08/README.md:9–10 | `../02-molecular-biology-genetics/`, `../04-genomics-bioinformatics/` (nonexistent) | Sections 02 and 04 (real paths) | internal link check |
| bio/08/README.md:22 | PharmGKB at `pharmgkb.org` | "(now served at ClinPGx)" → `clinpgx.org` | pharmgkb.org returns 302 → https://www.clinpgx.org/ |
| bio/08/README.md:28 | Suggested Order "Doudna & Charpentier CRISPR paper" | "Jinek et al. CRISPR paper" (matches the table) | https://doi.org/10.1126/science.1225829 |
| bio/09/README.md:9 | `../00-mathematical-foundations/` (nonexistent) | bio Section 00 + math/01, math/02, math/03, math/07 | internal link check |
| bio/10/README.md:9–11 | `../03-machine-learning-deep-learning/`, `../04-genomics-bioinformatics/`, `../07-structural-biology-drug-discovery/` (all nonexistent) | bio 03/04/06 + ml/03, ml/06, ml/13 | internal link check |
| bio/10/README.md:18 | AlphaFold 3 author "Dunber" | "Dunger" | https://api.crossref.org/works/10.1038/s41586-024-07487-w |
| bio/10/README.md:22; bio/11:62 | scGPT "Cui, Wang, Zhong, Wang, Wang & Bo" | "Cui, Wang, Maan, Pang, Luo, Duan & Wang" | https://api.crossref.org/works/10.1038/s41592-024-02201-0 |
| bio/10/README.md:24 | "AlphaFold and the Future of Biology — Nobel Lecture", Jumper & Hassabis (joint) | Jumper's real title, with Hassabis's separate lecture noted | https://www.nobelprize.org/prizes/chemistry/2024/jumper/lecture/ ; …/hassabis/lecture/ |
| bio/11/README.md:40 | Thornburg et al. modelled "a minimal *E. coli*-like synthetic cell" | JCVI-syn3A, a 493-gene minimal cell | https://www.jcvi.org/publications/fundamental-behaviors-emerge-simulations-living-minimal-cell |
| bio/README.md:75 | "Doudna & Charpentier — CRISPR-Cas9 (Science 2014)" | "Jinek et al. (Doudna & Charpentier) — CRISPR-Cas9 (Science 2012)" | matches section 08 / Jinek 2012 |
| bio/README.md:78 | "Alon — Network Motifs (Science 2002)" | "Milo et al. (Alon lab) — Network Motifs (Science 2002)" | https://doi.org/10.1126/science.298.5594.824 |
| bio/books/README.md:15 | Dayan & Abbott, 2005 | 2001 (matches Section 09) | internal consistency |
| bio/courses/README.md:10 | MIT 7.03 instructor "MIT OCW" | "Chris Kaiser" (matches Section 02) | internal consistency |
| bio/PROGRESS.md (whole file) | 76 checkboxes covering ~6 per section | every section resource listed, in Suggested-Order sequence; 4 citation fixes carried through | internal consistency |

## Proposed new sections (not created)

**Caveat on verification:** the session-wide WebSearch and WebFetch budgets were exhausted partway through this review (Crossref and Europe PMC also rate-limited me and told me not to retry). Each list below marks which items I **verified in this session** (✓) and which are **unverified candidates** (?) that must be checked before anything is created. I did not add any unverified item to the curriculum itself.

### A. Statistics and Experimental Design for Biology
- **Position:** new Section 05, pushing Systems Biology onward — it must come *before* bioinformatics and omics analysis, since every section after it produces numbers that need judging.
- **Why:** the single largest gap. The curriculum teaches a learner to compute p-values, fold-changes, docking scores, and model confidences without ever teaching sampling, power, multiple testing, batch effects, or replication. For someone whose day job is measurement, this is also the most transferable section in the curriculum.
- **Outline:** (1) distributions and estimation in biological data; (2) hypothesis testing and what it does not tell you; (3) multiple testing and FDR (the omics-defining problem); (4) experimental design: replication, randomization, blocking, controls, batch effects; (5) power and sample size; (6) count models and normalization (RNA-seq, scRNA-seq); (7) the reproducibility crisis and its mechanics; (8) causal inference basics (link to `math/10`).
- **Resources:** Modern Statistics for Modern Biology — Holmes & Huber, 2019, free ✓ https://www.huber.embl.de/msmb/ · Single-Cell Best Practices (QC/normalization/DE chapters) ✓ https://www.sc-best-practices.org/ · Nature's "Statistics for Biologists" collection (?) · Ioannidis, "Why Most Published Research Findings Are False", PLoS Med 2005 (?) · Benjamini & Hochberg 1995, J. R. Stat. Soc. B (?) · Leek & Storey, "Capturing heterogeneity in gene expression studies by surrogate variable analysis", PLoS Genet 2007 (?) · Krzywinski & Altman, Nature Methods "Points of Significance" series (?) · cross-link `math/03 — Probability and Statistics` ✓ (exists in repo).

### B. Bioinstrumentation, Imaging, and Lab Automation
- **Position:** new section after Structural Biology (so, roughly Section 04) — or as the curriculum's "how the data is made" counterpart to Section 04's "what to do with the data".
- **Why:** explicitly the gap most aligned with Aaron's own expertise and company: the curriculum consumes data from sequencers, microscopes, patch clamps, probes, and plate readers while saying nothing about how any of them work. It also makes the whole curriculum less abstract — an engineer who understands a photomultiplier, a flow cell, and an amplifier's noise floor reads biology papers differently. The Neuropixels and NGS-technology papers I added to Sections 09 and 02 are the beginnings of this and could move here.
- **Outline:** (1) signal chains in biological measurement: transducers, amplification, noise, sampling; (2) optical microscopy and fluorescence; (3) super-resolution and light-sheet; (4) electrophysiology, from patch clamp to high-density CMOS probes; (5) sequencing instrumentation and flow cells; (6) biosensors and point-of-care devices; (7) microfluidics and lab-on-chip; (8) lab automation, liquid handling, and self-driving labs.
- **Resources:** Fully Integrated Silicon Probes (Neuropixels) — Jun et al., Nature 2017 ✓ https://doi.org/10.1038/nature24636 · Coming of Age: Ten Years of NGS — Goodwin et al., 2016 ✓ https://doi.org/10.1038/nrg.2016.49 · Cryo-EM Nobel lectures 2017 ✓ (already in Section 03) · Nikon MicroscopyU (?) https://www.microscopyu.com/ · 2014 Nobel Prize in Chemistry, super-resolved fluorescence microscopy (?) · Opentrons / PyLabRobot documentation for lab automation (?) · "Self-driving laboratories" review (?) · Electrophysiology: Molecular Devices *Axon Guide* (?).

### C. Evolution and Population Genetics
- **Position:** new section immediately after Genetics and Genomics (Section 03 in a renumbered scheme).
- **Why:** the curriculum's deepest *conceptual* omission. Alignment scoring matrices, conservation tracks, gnomAD constraint, phylogenetics, protein language models, and GWAS all rest on evolutionary reasoning that is never taught — Section 02 covers inheritance and sequencing but not drift, selection, coalescence, or linkage disequilibrium. It is also the cheapest section to add, because much of the needed machinery (probability, Markov chains) is already in `math`.
- **Outline:** (1) variation, mutation, and drift; (2) selection and fitness landscapes; (3) Hardy-Weinberg, linkage, recombination, LD; (4) coalescent theory and genealogies; (5) molecular clocks and phylogenetic inference; (6) human population history and admixture; (7) selection scans and conservation as a signal used everywhere in bioinformatics; (8) experimental evolution and directed evolution (links to Section 07).
- **Resources:** Durbin et al. phylogenetics chapters ✓ (already in Section 04) · Coop, *Population and Quantitative Genetics* lecture notes, free (?) · Nielsen & Slatkin, *An Introduction to Population Genetics* (?) · Hartl & Clark, *Principles of Population Genetics* (?) · Arnold Nobel lecture on directed evolution ✓ (already in Section 07) · gnomAD constraint paper ✓ https://doi.org/10.1038/s41586-020-2308-7 · 1000 Genomes ✓ (already in Section 02) · Felsenstein, *Inferring Phylogenies* (?).

### D. Biosecurity and Dual-Use (as a subsection of Section 11, not a new section)
- Urbina et al. 2022 ✓ (now in Section 10) plus 2–3 verified items on AI biosecurity would make a sixth Frontiers subsection. I did not create it because I could only verify one item; the Section 10 placement covers the essential point for now.

## Cut candidates

- **Mount (2004), *Bioinformatics: Sequence and Genome Analysis*** and **Higgins & Taylor (2000), *Bioinformatics: Sequence, Structure, and Databanks*** (Section 04) — both 20+ years old, overlapping with Durbin and with the newly added Compeau & Pevzner; the ClustalW-era tooling advice is actively misleading now.
- **BioBERT (Section 10)** — a 2020 domain-BERT is a historical footnote next to general LLMs; keep only if the section grows an explicit biomedical-NLP thread.
- **"A Brief Guide to Genomics" — Broad Institute (Section 02)** — the title belongs to NHGRI, the Broad URL did not load, and the section already cites NHGRI's education hub. Redundant even if the link is revived.
- **Sinclair, *Lifespan* (Section 11 + books/)** — the description promotes a contested thesis as settled ("advancing the information theory of aging"); either caveat it or drop it in favour of the López-Otín hallmarks paper that already anchors the subsection.
- **Neuralink (Section 11)** — a company homepage with no technical content; the Willett and Hochberg papers already carry the BCI story.
- **Baker Lab homepage (Section 07)** — now largely redundant with the added Nobel lecture and background document; keep only as a tools pointer.
- **CellDesigner (Section 05)** — SBML GUI tooling that has aged; the added Python-based *Biological Circuit Design* covers the same ground in a way Aaron would actually use.
- **PROGRESS.md "Books (supplementary)" block** — duplicates `books/README.md`; make one a pointer to the other.

## Structural observations

- **The hallucination signature is systematic, not random.** The fabricated author "Bhatt" appears in two unrelated sections (03 iBiology, 05 MIT 8.591J); invented-but-plausible titles appear twice (Anfinsen's lecture, the Jumper/Hassabis "joint" lecture); a real DOI was attached to the wrong article (Callaway); author lists drift one edition out of date (Griffiths, Lodish, Klipp). Anything in this repo with an author field that was not checked should be assumed wrong until verified — the error rate in `bio/` was roughly one verifiable citation error per section.
- **Six of six broken internal links were prerequisite blocks referencing a *different* curriculum's section names** (`03-machine-learning-deep-learning`, `04-genomics-bioinformatics`, `07-structural-biology-drug-discovery`, `00-mathematical-foundations`, `02-molecular-biology-genetics`). That is strong evidence Sections 08–10 were generated against an earlier, differently numbered outline (one that merged structure+drug discovery and included a math section) and never reconciled. Worth checking whether other curricula have the same fossil.
- **Overlap with `ml/13 — Graphs, Geometry, and Science`** (requested): AlphaFold 2, AlphaFold 3, RFdiffusion, and the Bronstein geometric-deep-learning monograph appear in **both** `bio/10` (and `bio/07`) and `ml/13`. The duplication is defensible — `ml/13` teaches the architectures, `bio/10` teaches the biology — but it should be made explicit rather than accidental. Suggested split: `ml/13` owns GNNs, equivariance, and the method papers; `bio/10` owns the biological interpretation, the confidence metrics, running the models, and the dual-use question, and links to `ml/13` for architecture (I have now added that link to `bio/10`'s prerequisites). Note also that `ml/13` lists "AlphaProof & AlphaGeometry" with no link at all, and that `bio` repeats `ml`'s Geometric Deep Learning row verbatim.
- **Other cross-curriculum links worth adding:** `bio/05` (systems biology) ↔ `math/07 — Differential Equations` and `physics/10 — Nonlinear Dynamics and Chaos`; `bio/06` ↔ `physics/02 — Thermodynamics and Statistical Mechanics`; `bio/04` ↔ `math/03 — Probability and Statistics`; `bio/09` ↔ `ml/03`/`ml/05` for the NeuroAI connection. Only the `bio/09` and `bio/10` ones exist now (as part of my link fixes).
- **`bio/` has no `.agents/skills/update-curriculum/SKILL.md`,** unlike `ml`, `btc`, `pcb`, and `software` — yet the root README claims every curriculum has one. Given how fast Sections 07/08/10/11 move, this is the curriculum that most needs an update skill. Recommend copying the `ml` one and adapting it (and, in it, encoding the verification discipline: every new entry needs a fetched URL confirming title/author/year).
- **Type-emoji vocabulary is inconsistent and undocumented:** 📚 Textbook in Sections 00–03 vs 📘 Textbook in 04–06; "📄 Paper / Review / Feature / Nobel Lecture / Perspective / Background" are used interchangeably as type labels; the README Legend explains only 🔑. One table of type labels in the README would fix it.
- **The `Year` column is stale for live resources** — PDB-101, RCSB, KEGG, ZINC, RDKit, and others are all frozen at "2024" (the repo was generated in July 2026). I used the year I verified (2026) for newly added live resources, which makes the inconsistency visible; a "last checked" convention would be better than a fake publication year.
- **Section 11 is the only section with no Prerequisites block and no Suggested Order,** and Section 00 has no Prerequisites block (reasonably). Adding a one-line "read after Sections 05–10" to Section 11 would make the arc complete.

## Top 5 priorities for Aaron in this curriculum

1. **Do the statistics section that does not exist yet.** Work Holmes & Huber's *Modern Statistics for Modern Biology* (free) alongside Section 04. Without it, every number the rest of the curriculum produces — a p-value, a fold-change, a docking score, a pLDDT — is uninterpretable. This is also the most transferable skill to your own measurement work.
2. **Run the models, don't just read them.** Section 10 now has AlphaFold 3's open code and Boltz (MIT-licensed, weights included). Predict a complex you care about, then open it in ChimeraX and color by confidence. One afternoon of this teaches more about what these models are than all nine papers.
3. **Follow one gene-editing therapy end to end.** Jinek 2012 → Anzalone/Koblan/Liu 2020 → the FDA approval → Frangoul 2024 → Musunuru 2025 (baby KJ) is now a continuous path in Section 08. It is the clearest example in all of biology of mechanism → tool → product → regulation, which is the same arc your own hardware has to travel.
4. **Use the instrumentation entry points as your way in.** Neuropixels (Section 09) and the NGS-technologies review (Section 02) are written in your language — transducers, channel counts, multiplexing, error profiles. Reading biology through the instruments will get you further, faster, than reading it through the textbooks, and it is the gap the proposed Section B would formalize.
5. **Treat Section 11 and the AI sections as the part that rots.** Evo 2 (2026), ESM3 (2025), and the virtual-cell roadmap are in now, but this curriculum will be stale again in a year. Add the `update-curriculum` agent skill to `bio/` with an explicit rule — no entry without a fetched URL confirming title, authors, and year — because the generated citations in this curriculum failed exactly that test about once per section.

---

## Follow-up pass (2026-10-13)

The three proposed sections (A, B, C above) are now created, with every resource verified by fetching its page; the biosecurity subsection (D) is created inside Section 11. Every URL and citation below was confirmed in this pass, and nothing unverified was added.

- **New sections created:**
  - `bio/12-statistics-and-experimental-design/` · take alongside or before Section 04, and before 05/08/10 · 7 resources, 5 exercises, mini-project, 8 Check Yourself questions
  - `bio/13-bioinstrumentation-imaging-and-lab-automation/` · take after Section 03 · 9 resources, 5 exercises, mini-project, 8 Check Yourself questions
  - `bio/14-evolution-and-population-genetics/` · take after Section 02 · 7 resources, 5 exercises, mini-project, 8 Check Yourself questions

- **Added:**
  - Modern Statistics for Modern Biology — Susan Holmes & Wolfgang Huber — 2019 — Section 12 (🔑; free, CC BY-NC-SA; also CUP ISBN 9781108705295. Section 12 is now this book's home; the Section 04 row points to it)
  - Controlling the False Discovery Rate: A Practical and Powerful Approach to Multiple Testing — Yoav Benjamini & Yosef Hochberg — 1995 — Section 12 (🔑; J. R. Stat. Soc. B 57(1):289–300)
  - Why Most Published Research Findings Are False — John P. A. Ioannidis — 2005 — Section 12 (PLoS Med. 2(8):e124)
  - Tackling the Widespread and Critical Impact of Batch Effects in High-Throughput Data — Leek, Scharpf, Corrada Bravo, Simcha, Langmead, Johnson, Geman, Baggerly & Irizarry — 2010 — Section 12 (Nat. Rev. Genet. 11:733–739; full nine-author list verified)
  - Moderated Estimation of Fold Change and Dispersion for RNA-seq Data with DESeq2 — Michael I. Love, Wolfgang Huber & Simon Anders — 2014 — Section 12 (Genome Biol. 15:550)
  - The ASA Statement on *p*-Values: Context, Process, and Purpose — Ronald L. Wasserstein & Nicole A. Lazar — 2016 — Section 12 (Am. Stat. 70(2):129–133)
  - Statistics for Biologists / *Points of Significance* — Martin Krzywinski, Naomi Altman et al. (*Nature Methods*) — 2013– — Section 12 (the Nature collection, free to read; eight named columns cited individually by DOI)
  - Nikon's MicroscopyU — Nikon Instruments — Section 13 (🔑; plus its CCD noise-sources and CCD SNR tutorials)
  - The Axon Guide — Electrophysiology and Biophysics Laboratory Techniques (5th ed.) — Molecular Devices — Section 13 (🔑; free with registration; chapter list verified)
  - Super-Resolution Microscopy Demystified — Schermelleh, Ferrand, Huser et al. (… Drummen) — 2019 — Section 13 (Nat. Cell Biol. 21:72–84; subscription, noted)
  - The Nobel Prize in Chemistry 2014, "for the development of super-resolved fluorescence microscopy" — Betzig, Hell & Moerner — Section 13
  - Three Decades of Nanopore Sequencing — David Deamer, Mark Akeson & Daniel Branton — 2016 — Section 13 (Nat. Biotechnol. 34:518–524)
  - Flow Cytometry: Retrospective, Fundamentals and Recent Instrumentation — Picot, Guerin, Le Van Kim & Boulanger — 2012 — Section 13 (Cytotechnology 64(2):109–130; subscription, noted)
  - Assay Guidance Manual — Sarine Markossian (ed.-in-chief), Abigail Grossman, Hannah Baskir et al. — 2004– — Section 13 (NCBI Bookshelf; free, CC BY-NC-SA 3.0; Eli Lilly & NCATS)
  - PyLabRobot — Rick P. Wierenga, Stefan M. Golas, Wilson Ho, Connor W. Coley & Kevin M. Esvelt — 2023 — Section 13 (Device 1(4):100111)
  - Self-Driving Laboratories to Autonomously Navigate the Protein Fitness Landscape — Jacob T. Rapp, Bennett J. Bremer & Philip A. Romero — 2024 — Section 13 (Nat. Chem. Eng. 1:97–107)
  - Population Genetics & Quantitative Genetics Notes — Graham Coop — Section 14 (🔑; free, CC BY 3.0)
  - An Introduction to Population Genetics: Theory and Applications — Rasmus Nielsen & Montgomery Slatkin — 2013 — Section 14 (287 pp, ISBN 9781605351537)
  - Evolutionary Rate at the Molecular Level — Motoo Kimura — 1968 — Section 14 (🔑; Nature 217:624–626)
  - Genealogical Trees, Coalescent Theory and the Analysis of Genetic Polymorphisms — Noah A. Rosenberg & Magnus Nordborg — 2002 — Section 14 (Nat. Rev. Genet. 3:380–390)
  - msprime — tskit-dev — Section 14 (GPL-3.0; the ground truth for every coalescent exercise there)
  - The Dynamics of Molecular Evolution over 60,000 Generations — Good, McDonald, Barrick, Lenski & Desai — 2017 — Section 14 (Nature 551:45–50; Crossref confirms exactly these five authors)
  - IQ-TREE — L.-T. Nguyen, H. A. Schmidt, A. von Haeseler & B. Q. Minh — 2015 — Section 14 (Mol. Biol. Evol. 32:268–274)
  - Biodefense in the Age of Synthetic Biology — National Academies of Sciences, Engineering, and Medicine — 2018 — Section 11, new "Biosecurity and Dual Use" subsection
  - Artificial Intelligence and Biological Misuse: Differentiating Risks of Language Models and Biological Design Tools — Jonas B. Sandbrink — 2023 — Section 11, same subsection (arXiv:2306.13952)
  - Strengthening Nucleic Acid Biosecurity Screening against Generative Protein Design Tools — Wittmann, Alexanian, Bartling, Beal et al. (… Horvitz) — 2025 — Section 11, same subsection (Science 390(6768):82–87)
  - Genome-Wide Association Studies — Uffelmann, Huang, Munung, de Vries, Okada, A. R. Martin, H. C. Martin, Lappalainen et al. (… Posthuma) — 2021 — Section 02, replacing the dead Broad GWAS primer (Nat. Rev. Methods Primers 1:59; NHGRI's free fact sheet given as the open alternative)
  - Also added to `books/`: Coop's notes (🔑) and Nielsen & Slatkin. No new 🔑 was added to any pre-existing section, and each new section carries exactly two.

- **Removed (confirmed nonexistent):** none. Both suspect Broad Institute rows were mis-attributions rather than fabrications, so they were corrected in place rather than cut — no row, Suggested Order step or PROGRESS line was deleted in this pass.

- **Flags resolved:**
  - `bio/11-frontiers/README.md:76` (independent check, Evo 2 DOI) — Crossref confirms *Genome modelling and design across all domains of life with Evo 2*, Nature **652**(8112):1349–1361, published online 4 Mar 2026, DOI as given, first authors Brixi, Durrant, Ku, Naghipourfar, Poli (62 authors; Hsu and Hie last). No change needed. https://api.crossref.org/works/10.1038/s41586-026-10176-5
  - `bio/02/README.md:26` (review ✱, Watson edition) — the 7th edition is still the latest; no 8th exists. The Pearson URL in the repo now serves a *different* book (*Biology: The Core*), so the row was repointed to a catalogue record and the year corrected to 2014 (Pearson). `books/` row 8 aligned. https://archive.org/details/molecularbiology0000unse_n0v9 · https://nhbs.com/molecular-biology-of-the-gene-international-edition-book
  - `bio/02/README.md:33` (review ✱, Broad "A Brief Guide to Genomics") — confirmed: the title is NHGRI's, and the Broad URL no longer resolves while broadinstitute.org itself does. Row re-attributed to NHGRI with the live fact-sheet URL (last updated 16 Aug 2022). https://www.genome.gov/about-genomics/fact-sheets/A-Brief-Guide-to-Genomics
  - `bio/02/README.md:34` (review ✱, Broad GWAS primer) — URL confirmed dead; replaced with Uffelmann et al. (2021) plus NHGRI's free GWAS fact sheet. Practice 4 and the Suggested Order updated to match. https://doi.org/10.1038/s43586-021-00056-9 · https://www.genome.gov/about-genomics/fact-sheets/Genome-Wide-Association-Studies-Fact-Sheet
  - `bio/03/README.md:26` (review ✱, Branden & Tooze dead link) — Routledge now carries the 2nd edition (424 pp, ISBN 9780815323051, Garland Science imprint, © 1999); row repointed and the author's name corrected to Carl Ivar Branden. https://www.routledge.com/Introduction-to-Protein-Structure/Branden-Tooze/p/book/9780815323051
  - `bio/04/README.md:32` (review ✱, Rosalind attribution) — Rosalind's own About page: a joint project of UC San Diego and Saint Petersburg Academic University, team led by Nikolay Vyahhi with Phillip Compeau; Compeau & Pevzner wrote the book behind the Textbook Track, not the platform. Row re-credited. https://rosalind.info/about/
  - `bio/courses/README.md:9` vs `bio/01:26` (independent check, MIT 5.07SC instructors) — OCW credits Prof. John Essigmann, Prof. Joanne Stubbe and Dr. Bogdan Fedeles; the section was right and the course index was short. Index aligned. https://ocw.mit.edu/courses/5-07sc-biological-chemistry-i-fall-2013/
  - `bio/11-frontiers/README.md:41` (independent check, the one remaining overclaim) — the paper reports 62 wpm, 3.4× the previous record, 9.1% WER on 50 words and 23.8% on 125,000, and says it "begins to approach the speed of natural conversation (160 words per minute)". Prose rewritten to the paper's own framing with the numbers. https://www.nature.com/articles/s41586-023-06377-x
  - `bio/11-frontiers/README.md:65` (independent check, Sinclair) — the "information theory of aging" is now labelled as Sinclair's own contested hypothesis rather than an achievement, and the row carries a caveat pointing at the hallmarks review.
  - `bio/10/README.md:66` (independent check, Geneformer cited without its section) — Practice 5 now names Section 11, matching the convention in `bio/09:67`.
  - `bio/00:29`, `bio/01:32`, `bio/02:33,35`, `bio/03` (independent check, table rows absent from Suggested Order) — MIT 7.016, MIT 7.05, the NHGRI brief guide, the 2012 1000 Genomes paper and the RCSB PDB database row now all appear in their sections' Suggested Order.
  - `bio/00-molecular-biology-fundamentals/README.md:58` (independent check, V5 cross-curriculum row) — the mini-project now names a deliverable path, `projects/bio/00-gene-datasheet/`.
  - §07/§11 dual-use pointer (independent check, safety note) — Section 07's Suggested Order gains a step pointing at Urbina et al. (Section 10) and the new biosecurity subsection before any bench-intended design, and its mini-project asks for the screening controls that apply to a synthesis order. Section 11's foundation-model paragraph now hands off to the same subsection.
  - Cross-references added so the new sections are reachable from the old ones: 02 → 13 and 14, 03 → 13, 04 → 12 and 14, 07 → 11 and 14, 09 → 13, 10 → 11 and 12.

- **Still unverified:**
  - **The Z′-factor paper's DOI.** Zhang, Chung & Oldenburg, *J. Biomol. Screen.* 4(2):67–73 (1999) is confirmed by two independent pages (Harvard ICCB's publication list and GraphPad's knowledge base), but SAGE returned a server error and PubMed and Crossref were unreachable, so no DOI was confirmed. The paper is therefore cited inline in Section 13's Practice 5 with its journal, volume and pages, and the formula is written out in the exercise rather than linked — it is not a resource row.
  - **A dedicated free flow-cytometry primer.** Picot et al. (2012) is verified but behind a subscription; the obvious free alternative on PubMed Central could not be read (the PMC article page served a reCAPTCHA challenge rather than content), so nothing free was added for that topic.
  - **Chapter numbers for *Modern Statistics for Modern Biology*.** The book's landing page does not list its contents and the chapter pages were not fetched, so Section 12's Suggested Order names chapters by topic rather than by number.
  - **msprime's documentation URL** (`tskit.dev/msprime/docs/latest/`) is given in prose because the project's own GitHub page states it; the docs site itself returned empty content when fetched, and the row links the verified repository instead.
  - **IQ-TREE's current version.** iqtree.org's front page still advertises v1.5.5 (2017) and does not mention IQ-TREE 2 or 3, so the row makes no version claim and cites the 2015 paper.

- **Out of scope for this pass (for the orchestrator):** `STUDY-GUIDE.md`'s "One home per topic" table should gain rows for statistics (home `bio/12`, also touches `bio/04`, `math/03`), bioinstrumentation (home `bio/13`, also touches `physics/12`, `pcb/12`, `bio/09`) and population genetics (home `bio/14`, also touches `bio/02`, `bio/04`); its Track D could name the three new sections. `bio/` still has no `update-curriculum` skill, so no section map needed updating here.

## Link-audit fixes (2026-10-13)
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| bio/00-molecular-biology-fundamentals/README.md:22 (+ Suggested Order step 2, Practice 1; courses/README.md:7; PROGRESS.md:11) | MITx 7.00x "The Secret of Life" (Lander, 2023); the edX URL is now a generic biology listing and the course has left the catalogue (L2-062) | The auditor's stand-in, MIT 7.01SC Fundamentals of Biology (OCW, Fall 2011; Lander, Weinberg, Jacks, Sive, Walker, Chisholm, Mischke), confirmed by fetch; it keeps the row's 🔑 | https://ocw.mit.edu/courses/7-01sc-fundamentals-of-biology-fall-2011/ |
| bio/00-molecular-biology-fundamentals/README.md:27 | iBiology "Cell Biology Collection", "Ron Vale, et al.", 2015, at `ibiology.org/cell-biology/` (now a single Janet Iwasa talk) (L3-075) | `ibiology.org/research-talks/cell-biology/`; "Various (iBiology)"; year "—" | https://www.ibiology.org/research-talks/cell-biology/ |
| bio/01-biochemistry/README.md:25 (+ books/README.md:8, README.md:62, PROGRESS.md:264) | Lehninger 8th ed. credited to Nelson & Cox (L3-097) | Nelson, Cox & Hoskins | https://www.macmillanlearning.com/college/us/product/Lehninger-Principles-of-Biochemistry/p/1319228003 |
| bio/01-biochemistry/README.md:30 (+ Suggested Order step 5) | "HHMI BioInteractive: Enzyme Catalysis & Protein Structure" at a `topic[]=36` URL that returns the generic 623-item listing (L2-012) | BioInteractive's own search for "enzyme" within its Biochemistry & Molecular Biology topic (40 results: enzyme animations, Cech's ribozyme video, activities); title and description rewritten to match | https://www.biointeractive.org/search?keyword=enzyme&type_page=1&topics%5B23%5D=23&sort_bef_combine=search_api_relevance_DESC |
| bio/03-structural-biology/README.md:30 (+ Suggested Order step 4, Practice 6, PROGRESS.md:60) | iBiology "Structural Biology Collection" at a dead URL (L1-076) | iBiology's Techniques collection, which holds the structural-methods talks (Yifan Cheng, single-particle cryo-EM; David J. Haas, macromolecular cryocrystallography). iBiology has no NMR talk, and the row says so | https://www.ibiology.org/research-talks/techniques/ ; https://www.ibiology.org/research-talks/biophysics/ |
| bio/03-structural-biology/README.md:34 | RCSB PDB Training Resources at `rcsb.org/training` (4xx) (L1-142) | PDB-101 "Train: All Training Courses" (RCSB.org search, Mol*, validation, APIs) | https://pdb101.rcsb.org/train/training-events |
| bio/04-bioinformatics-and-sequence-analysis/README.md:27 | NCBI BLAST "Tutorials and Documentation" linked to the search page (L3-016) | BLAST Help (`/doc/blast-help/`); the search page stays as a second link | https://blast.ncbi.nlm.nih.gov/doc/blast-help/ |
| bio/04-bioinformatics-and-sequence-analysis/README.md:29 | Mount at a CSHL Press cart URL that lands on the store home (L2-030) | CSHL Press product page | https://cshlpress.com/link/bioinf2p.htm |
| bio/06-computational-chemistry-and-drug-discovery/README.md:26 | Leach, *Molecular Modelling*, at a Pearson page that now serves an unrelated book (L3-127) | Open Library record (2nd ed., Prentice Hall, 2001) | https://openlibrary.org/books/OL7880866M/Molecular_Modelling |
| bio/06-computational-chemistry-and-drug-discovery/README.md:28 | AutoDock Vina docs credited to "Trott, O. & Olson, A. J.", 2024, with receptor/ligand-preparation tutorials claimed (L1-009) | "AutoDock Vina Documentation (v1.2.0)", Forli Lab / CCSB, Scripps Research (original program by Oleg Trott), 2021; tutorials named as the docs list them | https://autodock-vina.readthedocs.io/ |
| bio/07-protein-engineering-and-design/README.md:32 | ProGen author list ending "... Fraser, J. S." (L2-049) | "... Fraser, J. S., Naik, N." (Naik is the last author) | https://api.crossref.org/works/10.1038/s41587-022-01618-2 |
| bio/08-genomic-medicine/README.md:28 | *Deep Medicine* at `basicbooks.com` (302 to Hachette) (L2-010) | Hachette Book Group page | https://www.hachettebookgroup.com/titles/eric-topol/deep-medicine/9781541644649/?lens=basic-books |
| bio/08-genomic-medicine/README.md:30 (+ Suggested Order step 7) | Manolio et al. described as bridging GWAS and the clinic (L3-044) | Described as the missing-heritability review it is | https://api.crossref.org/works/10.1038/nature08494 |
| bio/08-genomic-medicine/README.md:71 (Practice 6) | "Broad GWAS primer from Section 02", a row the follow-up pass replaced (L1-019) | "Uffelmann et al. 2021 GWAS primer from Section 02" | internal consistency |
| bio/09-neuroscience/README.md:27 | Kandel 6th ed. at `mhprofessional.com` (302 to a generic page) (L1-102) | McGraw Hill higher-ed product page | https://www.mheducation.com/highered/mhp/product/principles-neural-science-sixth-edition.html |
| bio/09-neuroscience/README.md:32 | Allen Brain Atlas at `portal.brain-map.org` (302) (L2-136) | `brain-map.org` | https://brain-map.org/ |
| bio/11-frontiers/README.md:73 | Evo credited to "Nguyen, Poli, Durrant, Thomas et al." (the preprint's order) (L1-057) | "Nguyen, Poli, Durrant, Kang et al." (the *Science* order) | https://api.crossref.org/works/10.1126/science.ado9336 |
| bio/blogs-and-references/README.md:13 | "PLOS Biology Community" (L3-012) | "PLOS Biologue", the blog for *PLOS Biology*, *PLOS Genetics* and *PLOS Computational Biology* | https://biologue.plos.org/ |
| bio/courses/README.md:13 | Uri Alon lectures: a YouTube playlist that no longer loads (L1-176) | Lecture 1 of the 2018 course on the Alon Lab channel, plus the Weizmann course page that lists all twelve lectures | https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=N6VZeWuME_A&format=json ; https://www.weizmann.ac.il/mcb/alon/courses/systems-biology-2018 |
| bio/courses/README.md:17 | UCSD "Drug Discovery Specialization" (4xx) (L3-027) | UCSD's single "Drug Discovery" course (Ettouati & Ma), now part of its Drug Development Product Management Specialization | https://www.coursera.org/learn/drug-discovery |
| bio/courses/README.md:19 | "David Baker on Protein Design", YouTube `LHVm4nMAyBQ` (L2-180; unverifiable at audit, but YouTube's oEmbed now answers 404 Not Found) | Baker's 2024 Nobel lecture, "De Novo Protein Design" (also in Section 07); 🔑 removed (see Tier lists) | https://noembed.com/embed?url=https://www.youtube.com/watch?v=LHVm4nMAyBQ ; https://www.nobelprize.org/prizes/chemistry/2024/baker/lecture/ |
- Already fixed in the follow-up pass above: the Broad GWAS primer (L1-019), Watson's Pearson page (L1-128), Branden & Tooze's Garland URL (L2-067) and the Broad "Brief Guide to Genomics" (L3-018).
- Left unchanged because the auditor could not load the page, with no sign the resource is gone: Schrödinger at Cambridge Core (00:25; L1-020), the Takahashi & Yamanaka and Milo et al. DOIs (11:62, 05:27; L1-041, L1-055), Petsko & Ringe at OUP (03:29; L1-070), Khan Academy AP Biology and its gene-expression unit (courses:11, 00:28; L1-090, L2-090), NotebookLM (README:9; L2-114), In the Pipeline (blogs-and-references:9; L2-146), Voet & Voet and Klipp et al. at Wiley (01:28, 05:28; L2-165, L3-165), the PSI-BLAST DOI (04:35; L3-052), Klebe at Springer (06:36; L3-095), Dayan & Abbott at MIT Press (09:26, books:15; L3-103), ZINC (06:30; L3-185; its "230 million compounds" figure is still unconfirmed and may be older ZINC wording) and Durbin et al. at Cambridge Core (04:26; L3-019).

## Tier lists (2026-10-13)
🔑 trimmed to ≤3 per section; each Suggested Order now opens with a "Core path" line. Reverse any call by re-adding 🔑 to the row and the Core path line.
| Section | 🔑 kept | 🔑 removed (why, ≤8 words) |
|---|---|---|
| 07 | Arnold Nobel lecture (2018); Lin et al., ESM-2 (2023); Watson et al., RFdiffusion (2023) | Baker Nobel lecture (survey; no objective or exercise needs it) |
| 08 | Jinek et al. (2012); Anzalone, Koblan & Liu (2020); Richards et al., ACMG/AMP (2015) | Topol, *Deep Medicine* (popular vision book; no exercise uses it) |
| 11 | Nielsen, Voigt et al., Cello (2016); Willett et al. (2023); Nguyen et al., Evo (2024) | Karr et al., whole-cell model (no specific objective; Practice 3 still uses it); López-Otín et al., hallmarks of aging (no specific objective; Practice 4 still uses it) |
- Totals: 42 → 38 🔑 resource rows across Sections 00–14; no section has more than 3. Section 11's three are the ones its objectives and mini-project options name. Section 11 has no Suggested Order, so its Core path line sits under its 🔑 legend, just before Practice.
- `bio/README.md` Key Textbooks: removed *What Is Life?* (never 🔑 in Section 00, which already has three) and *Deep Medicine* (demoted in 08), marked *Molecular Biology of the Gene* 🔑 to match Section 02, and renumbered 1–8. Both removed books stay in their sections and in `books/`.
- `bio/courses/README.md` row 13: 🔑 removed. The row now points to Baker's Nobel lecture, which lost its 🔑 in Section 07, its only section.
- No other index row changed: *Deep Medicine* was already unmarked in `books/`, and Karr and López-Otín are in no index.
- The older index mismatches noted at first (MIT 7.016 and *Neuronal Dynamics* marked 🔑; Kandel and *Molecular Biology of the Gene* unmarked) are resolved by the index alignment below.
- books/README.md #8 Watson et al., *Molecular Biology of the Gene* (7th ed.): 🔑 added (core in 02)
- books/README.md #10 Kandel et al., *Principles of Neural Science*: 🔑 added (core in 09)
- books/README.md #13 Gerstner et al., *Neuronal Dynamics*: 🔑 removed (not core in any section; unmarked in 09)
- courses/README.md #2 MIT 7.016 Introductory Biology: 🔑 removed (not core in any section; unmarked in 00)
- courses/README.md #3 MIT 5.07SC Biological Chemistry I: 🔑 added (core in 01)
- courses/README.md #4 MIT 7.03 Genetics: 🔑 added (core in 02)
- bio/README.md legend: 🔑 row now reads "**Core path** — must-read / must-watch; at most 3 per section, named in each section's *Core path* line"
- Independent check: courses/README.md #5 Khan Academy AP Biology, #7 Uri Alon lecture videos, #9 iBiology Talks and #10 HHMI BioInteractive: 🔑 removed. None is 🔑 in any section; Section 05's 🔑 is Alon's textbook, and the other sections link only unmarked sub-pages of those sites.
- Independent check: Section 00 MIT 7.012 lectures (Lander & Weinberg): 🔑 removed. It overlapped 7.01SC, the same Lander-led intro course. Core path is now 7.01SC → Alberts. 7.012 stays as the "deeper perspective" step 6.
- Final decisions (2026-10-13): 04's Holmes & Huber row became an "Also used here" note pointing to Section 12, its home, and its PROGRESS line in Section 04 was dropped.
