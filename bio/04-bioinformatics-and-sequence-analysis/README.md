# Bioinformatics and Sequence Analysis

## Why This Section Matters

Bioinformatics sits at the intersection of biology, computer science, and statistics. Every modern biological discovery — from identifying disease-causing mutations to tracing evolutionary relationships — depends on the ability to compare, align, and interpret biological sequences. Mastering sequence alignment algorithms, database searching with BLAST, hidden Markov models for protein family detection, and phylogenetic reconstruction gives you the computational toolkit to make sense of the explosion of genomic data. These skills are prerequisites for structural biology, systems biology, and any AI-for-biology work that follows.

## Prerequisites

- [Section 00 — Molecular Biology Fundamentals](../00-molecular-biology-fundamentals/README.md)
- [Section 02 — Genetics and Genomics](../02-genetics-and-genomics/README.md)

## 🎯 Learning Objectives

After this section you can:

- Implement Needleman-Wunsch and Smith-Waterman with affine gap penalties from scratch and reproduce a reference aligner's score exactly on the same inputs and scoring scheme.
- Explain the Karlin-Altschul statistics behind a BLAST E-value, and demonstrate empirically — by shuffling — why alignment scores follow an extreme-value rather than a normal distribution.
- Implement forward, backward and Viterbi for a hidden Markov model in log space, and explain the difference between Viterbi decoding and posterior decoding.
- Explain what a profile HMM adds over a PSSM, and show empirically how much remote-homology sensitivity PSI-BLAST and HMMER buy over plain BLASTP.
- Decide, for a given alignment, whether the similarity is evidence of homology or an artefact of composition, low complexity, or database size.

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📘 Textbook | Biological Sequence Analysis: Probabilistic Models of Proteins and Nucleic Acids | Durbin, Eddy, Krogh, Mitchison | 1998 | [Cambridge University Press](https://www.cambridge.org/core/books/biological-sequence-analysis/921BB7F305C7D4F1EC0E84A141B2D4E1) | The definitive textbook on probabilistic methods in bioinformatics — covers pairwise alignment, HMMs, profile HMMs, phylogenetics, and RNA structure prediction with mathematical rigor |
| 🔑 | 🌐 Tutorial | NCBI BLAST Tutorials and Documentation | NCBI Staff | 2024 | [NCBI BLAST](https://blast.ncbi.nlm.nih.gov/Blast.cgi) | Official NCBI resource for running BLAST searches; includes comprehensive help pages covering nucleotide BLAST, protein BLAST, and interpreting E-values and alignment scores |
| 🔑 | 📄 Paper | What Is a Hidden Markov Model? | Eddy, S. R. | 2004 | [Nature Biotechnology](https://doi.org/10.1038/nbt1004-1315) | Exceptionally clear 2-page primer explaining HMMs and their application to biological sequence analysis — the single best introduction to the topic |
| | 📘 Textbook | Bioinformatics: Sequence and Genome Analysis | Mount, D. W. | 2004 | [Cold Spring Harbor Laboratory Press](https://www.cshlpress.com/default.tpl?cart=17202836&action=full&eqskudatarq=934) | Comprehensive and practical textbook covering sequence alignment, database searching, gene finding, phylogenetics, and genome annotation with worked examples |
| | 📄 Paper | Basic Local Alignment Search Tool | Altschul, S. F., Gish, W., Miller, W., Myers, E. W., Lipman, D. J. | 1990 | [J. Mol. Biol.](https://doi.org/10.1016/S0022-2836(05)80360-2) | The original BLAST paper — introduced the heuristic algorithm that made large-scale sequence database searching practical; it ranks 12th on *Nature*'s 2014 tally of the most-cited papers of all time (the 1997 PSI-BLAST paper is 14th) |
| | 🌐 Training | EMBL-EBI Training — Bioinformatics | EMBL-EBI | 2024 | [EBI Training](https://www.ebi.ac.uk/training/) | Free online courses and tutorials covering sequence analysis, protein classification, genome annotation, and biological databases from one of the world's leading bioinformatics centers |
| | 💻 Problem Set | Rosalind — Bioinformatics Stronghold | Compeau, P. & Pevzner, P. | 2012 | [Rosalind](https://rosalind.info/problems/locations/) | Interactive platform with 200+ bioinformatics programming challenges — learn by implementing algorithms for sequence alignment, motif finding, genome assembly, and phylogenetics |
| | 🌐 Tutorial | UCSC Genome Browser User Guide | UCSC Genomics Institute | 2024 | [UCSC Genome Browser](https://genome.ucsc.edu/goldenPath/help/hgTracksHelp.html) | Official guide to navigating the UCSC Genome Browser — essential for exploring genomic annotations, conservation tracks, and variant data in their genomic context |
| | 📘 Textbook | Bioinformatics: Sequence, Structure, and Databanks | Higgins, D. & Taylor, W. | 2000 | [Oxford University Press](https://global.oup.com/academic/product/bioinformatics-9780199637904) | Practical guide to multiple sequence alignment (including ClustalW), database searching strategies, and protein structure prediction methods |
| | 📄 Paper | Gapped BLAST and PSI-BLAST: A New Generation of Protein Database Search Programs | Altschul, S. F., Madden, T. L., Schäffer, A. A., Zhang, J., Zhang, Z., Miller, W., Lipman, D. J. | 1997 | [Nucleic Acids Research](https://doi.org/10.1093/nar/25.17.3389) | Introduced gapped alignments and position-specific iterated BLAST (PSI-BLAST), dramatically improving sensitivity for detecting remote homologs in protein databases |
| | 📘 Textbook | Bioinformatics Algorithms: An Active Learning Approach | Compeau, P. & Pevzner, P. | 2024 | [Site](https://www.bioinformaticsalgorithms.org/) | The algorithmic complement to Durbin: you learn assembly, motif finding, alignment, and phylogeny by implementing them. First five chapters and all lecture videos are free, and it is the text behind Rosalind's Textbook Track |
| | 📘 Textbook | Modern Statistics for Modern Biology | Holmes, S. & Huber, W. | 2019 | [Free online](https://www.huber.embl.de/msmb/) | Free, CC-licensed statistics text written for biological data — multiple testing, design, clustering, count models, and robustness — with R/Bioconductor code; the half of bioinformatics that algorithm textbooks skip |
| | 🌐 Training | Single-Cell Best Practices | Heumos, L., Schaar, A. C. et al. (single-cell best practices consortium) | 2023 | [Book](https://www.sc-best-practices.org/) | Free community Jupyter book behind *Best practices for single-cell analysis across modalities* (Nat. Rev. Genet. 2023) — an end-to-end scRNA-seq pipeline in Python, from QC and normalization to annotation and trajectory inference |

## Suggested Order

1. **Durbin et al. textbook (Chapters 1–4)** — Establishes the mathematical foundations: pairwise alignment, scoring matrices, dynamic programming, and statistical significance
2. **NCBI BLAST tutorials** — Get hands-on experience running real sequence searches before diving into the theory behind them
3. **Altschul et al. (1990)** — Read the original BLAST paper to understand the heuristic innovations that made large-scale database searching feasible
4. **Eddy (2004)** — This concise Nature Biotech primer makes HMMs click; read it before tackling the full HMM chapters in Durbin
5. **Durbin et al. textbook (Chapters 5–6)** — Profile HMMs and multiple sequence alignment — the backbone of protein family databases like Pfam
6. **Rosalind problems + Compeau & Pevzner** — Implement the algorithms yourself; the "Bioinformatics Stronghold" track and the Textbook Track pair directly with *Bioinformatics Algorithms*
7. **UCSC Genome Browser guide** — Learn to navigate real genomic data in context — annotations, conservation, variants
8. **Altschul et al. (1997)** — PSI-BLAST and gapped alignment are essential for detecting remote homology
9. **Holmes & Huber "Modern Statistics for Modern Biology"** — Work the inference chapters before you believe any result you compute: multiple testing, design, and count models
10. **EMBL-EBI training courses** — Fill gaps with structured tutorials on InterPro, UniProt, Ensembl, and other key databases
11. **Single-Cell Best Practices** — Run a modern omics pipeline end-to-end once; it is where most current biological data analysis actually happens
12. **Durbin et al. textbook (Chapters 7–9)** — Phylogenetics and RNA structure — complete the book after building practical skills

---

## 🛠️ Practice

1. **Write the aligners** — Implement global (Needleman-Wunsch) and local (Smith-Waterman) alignment with Gotoh affine gaps and full traceback, in NumPy. Validate against a reference: align the same two protein sequences with BLOSUM62, gap open 11, gap extend 1, and check your score matches Biopython's `PairwiseAligner` or EMBOSS `needle`/`water` *exactly*. Then instrument it: report time and memory versus sequence length and confirm the O(mn) scaling empirically. Deliverable: a module plus a test suite that asserts score equality on at least five pairs. *(~6 h · Durbin et al., the pairwise-alignment chapters; Rosalind)*

2. **Build the E-value from scratch by shuffling** — Take a real protein query and a modest database (a few thousand sequences from UniProt/Swiss-Prot). BLAST it and record the top hits' scores and E-values. Now shuffle the query 1000 times preserving amino-acid composition, run your own Smith-Waterman from exercise 1 against the same database for each shuffle, and build the empirical distribution of best scores. Fit a Gumbel distribution, extract λ and *K*, and compute your own E-value for the real top hit. Compare to BLAST's. Deliverable: notebook with the score histogram, the EVD fit, and a table comparing your E-values to BLAST's. This is the exercise that makes E-values stop being magic. *(~5 h · Altschul et al. 1990; Durbin et al. on alignment significance; NCBI BLAST)*

3. **Implement an HMM end to end** — Build the two-state occasionally-dishonest-casino or CpG-island HMM from Eddy's primer and Durbin. Implement forward, backward, Viterbi and posterior decoding, all in log space with proper scaling. Test on synthetic sequence generated from your own model with known hidden states, and report state-recovery accuracy for Viterbi versus posterior decoding — then explain, with a concrete example from your output, where they disagree and why. Then implement Baum-Welch and show it recovers the generating parameters from unlabelled data (or show where it gets stuck in a local optimum). Deliverable: notebook with accuracy tables. *(~7 h · Eddy 2004, "What Is a Hidden Markov Model?"; Durbin et al. HMM chapters)*

4. **The remote-homology ladder** — Pick a protein with documented distant homologs. Run, in order: (a) BLASTP against a reference proteome; (b) PSI-BLAST with 3 and 5 iterations; (c) `jackhmmer` or `hmmscan` against Pfam with HMMER (or `pyhmmer` in Python). At each stage record: how many true homologs found, at what E-value, and the identity of the first false positive. Build the table. Then write 300 words on what each method adds and on PSI-BLAST's characteristic failure mode — profile drift, where one false positive in an early iteration corrupts every later one. *(~4 h · Altschul et al. 1997 (PSI-BLAST); NCBI BLAST; EMBL-EBI training on InterPro/Pfam)*

5. **Rosalind reps** — Complete the alignment and probability problems in the Rosalind Bioinformatics Stronghold: global and local alignment, edit distance and alignment, gap penalties, and the HMM/probability problems. Target 15 problems. The point is implementation fluency, not novelty — but keep each solution as clean, tested code rather than a one-off script. Deliverable: a solutions repo. *(~6 h · Rosalind — Bioinformatics Stronghold)*

6. **Read a genome browser track honestly** — Pick a specific human locus (use the gene from Section 00's work, or a GWAS locus from Section 02). In the UCSC Genome Browser, extract for that interval: phyloP and phastCons conservation, repeat content from RepeatMasker, the GENCODE transcript models including all alternative isoforms, and any regulatory annotation available. Then write, for each track, two sentences on what it actually measures and one on its failure mode — e.g. what phastCons cannot see, what happens to conservation scores in a recent duplication, why a transcript model is a hypothesis. Deliverable: an annotated note with one screenshot. *(~3 h · UCSC Genome Browser user guide; EMBL-EBI training)*

**🏗️ Mini-project — A small, honest sequence-search engine:** Build a miniature BLAST and then prove how good it is or isn't. Implement: k-mer indexing of the database (word size 3 with a neighbourhood threshold for protein, or 11 for nucleotide), two-hit seeding, ungapped extension with an X-drop cutoff, gapped extension using your Gotoh aligner from exercise 1, and Karlin-Altschul E-value computation with λ and *K* estimated for your own scoring scheme by the shuffling method from exercise 2. Then benchmark against NCBI BLASTP on 200 queries against the same database: recall of BLAST's hits at E < 10⁻⁵, precision, wall-clock speed per query, and agreement between your E-values and BLAST's on a log-log scatter. Deliverable: the package plus a benchmark notebook and a one-page report in `projects/bio/04-minblast/`. Success criterion: you recover at least 80% of BLAST's E < 10⁻⁵ hits, your E-values correlate within about an order of magnitude, and — most important — for every systematic disagreement you can name the specific heuristic responsible (seeding threshold, X-drop, composition-based statistics, low-complexity filtering). *(~15 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State the Karlin-Altschul formula for an E-value and explain each term, including why database size appears.
2. Why does a bit score let you compare across searches when a raw score does not?
3. What exactly makes BLAST a heuristic rather than an exact algorithm, and what can it therefore miss?
4. Explain the difference between global and local alignment, and name a biological situation where using the wrong one gives a badly misleading answer.
5. You get an alignment with 40% identity over 30 residues and E = 0.4. Is it homologous? What would you do next?
6. What does a profile HMM capture that a position-specific scoring matrix cannot?
7. A colleague says "the E-value is the probability the hit is a false positive." Correct them precisely.
8. Explain to a smart friend in three sentences how you can tell two proteins share an ancestor when their sequences are only 15% identical.
