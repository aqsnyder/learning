# Pass 2 — bio, sections 08–14 (agent B)

Date: 2026-10-21. Scope: `bio/08`–`bio/14` (78 resource rows). Curriculum-level files (`bio/README.md`,
`bio/extras.toml`, `bio/books/`, `bio/courses/`, `bio/blogs-and-references/`) are **not** in this scope and were
not touched.

## How things were verified today

The shared web budget was badly contended during this run. What worked, and what did not:

| Route | Result |
|---|---|
| Europe PMC REST (`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:"…"&format=json&resultType=lite`) | 3 of 8 queries returned data (8 DOIs confirmed); the rest returned `CLIENT_ERROR`, then HTTP 429 |
| Crossref (`api.crossref.org/works…`) | HTTP 429 on the batch route, `CLIENT_ERROR` on `/works/10.1016/j.cell.2006.07.024` (same failure the October audit saw) |
| PubMed (`pubmed.ncbi.nlm.nih.gov/?term=<doi>`) | HTTP 429 |
| OpenAlex | refused: the host needs an interactive approval, which no one could give in this run |
| Open Library, MIT Press | `ROBOTS_DISALLOWED` |
| `cell.com`, `nature.com` | `CLIENT_ERROR`, or a partial render with no licence or citation block |
| Author/publisher pages (`gatsby.ucl.ac.uk/~dayan/book/`, `coursera.org`, `igem.org`) | worked (igem.org is a JavaScript shell with no readable content) |

Consequence: **no `verified` date was changed except where a page was actually read today**, and 12 `access`
fields were left empty rather than guessed. Both lists are under "For a browser check" below. `access` values
that were filled without a fetch today came from evidence already in the row (a verified `link_text`,
"(subscription)", "free with registration", a stated licence, "Open-Source" in the verified title) or from the
venue's published model (arXiv, PLOS, BMC = free; Science, NEJM, Nature/Cell/Nature-family subscription titles =
paid); those are marked "venue model" in the table.

## 1. Changes

| Section | Item (id) | Change | Evidence URL |
|---|---|---|---|
| bio/08 | `a-programmable-dual-rnaguided-dna` | `access = paid`; description rewritten (hype removed, free PMC copy PMC6286148 named); `verified = 2026-10-21` | Europe PMC DOI:10.1126/science.1225829 |
| bio/08 | `standards-and-guidelines-for-the` | `access = free` (PMC copy is open access); description rewritten; `verified = 2026-10-21` | Europe PMC DOI:10.1038/gim.2015.30 |
| bio/08 | `a-new-initiative-on-precision-medicine` | `access = paid`; description rewritten + PMC5101938; `verified = 2026-10-21` | Europe PMC DOI:10.1056/NEJMp1500523 |
| bio/08 | `finding-the-missing-heritability-of` | `access = paid`; description rewritten + PMC2831613; `verified = 2026-10-21` | Europe PMC DOI:10.1038/nature08494 |
| bio/08 | `genome-editing-with-crisprcas-nucleases` | `access = paid`; `verified = 2026-10-21` (authors Anzalone, Koblan, Liu and year confirmed) | Europe PMC DOI:10.1038/s41587-020-0561-9 |
| bio/08 | `exagamglogene-autotemcel-for-severe` | `access = paid`; `verified` left at 2026-10-13 (today's record did not show the final author the row asserts) | Europe PMC DOI:10.1056/NEJMoa2309676 |
| bio/08 | `patient-specific-in-vivo-gene-editing-to` | `access = paid`; description dated ("published in 2025 and, as of October 2026, still the reference case") + PMC12713542; `verified = 2026-10-21` | Europe PMC DOI:10.1056/NEJMoa2504747 |
| bio/08 | `pharmgkb-pharmacogenomics-knowledgebase` | `access = free` (public knowledgebase; link verified 2026-10-13) | in-row evidence |
| bio/08 | `how-crispr-lets-us-edit-our-dna` | `access = free`, `level = beginner` | in-row evidence (TED) |
| bio/08 | `nih-all-of-us-research-program` | `level = beginner` | in-row evidence |
| bio/08 | `fda-approves-first-gene-therapies-to` | `access = free` (FDA press announcement) | in-row evidence |
| bio/08 | README | Practice 2 now cross-links bio/12 Practice 5 for the general PPV model; Practice 3 no longer cites "the clinical genetics literature" (now Richards BA1/BS1 + gnomAD, named with its home Section 02); Practice 5 sources CPIC through PharmGKB/ClinPGx, which links it; new Check Yourself Q8 (maximum credible allele frequency); Suggested Order 9 dated to the December 2023 approval | — |
| bio/09 | `theoretical-neuroscience-computational` | `access` paid → `partial` (free sample chapter); `more_links` → authors' page; description rewritten; `verified` **left empty** (year/edition not confirmable) | https://www.gatsby.ucl.ac.uk/~dayan/book/ |
| bio/09 | `computational-neuroscience` | `access = partial`, `level = beginner`; description rewritten and dated (free enrolment, paid certificate for graded material, as of October 2026); instructor order confirmed | https://www.coursera.org/learn/computational-neuroscience |
| bio/09 | `mit-9-40-introduction-to-neural` | `level = intermediate` | in-row evidence |
| bio/09 | `neuromatch-academy-computational` | `access = free`, `level = intermediate` | in-row evidence (CC BY, stated in row) |
| bio/09 | `receptive-fields-binocular-interaction` | `access = paid`; description rewritten; `verified = 2026-10-21` | Europe PMC DOI:10.1113/jphysiol.1962.sp006837 |
| bio/09 | `allen-brain-atlas`, `human-connectome-project` | `access = free` (public data resources) | in-row evidence |
| bio/09 | `fully-integrated-silicon-probes-for-high` | `access = paid` (venue model) | venue model |
| bio/09 | README | new Check Yourself Q8 (two-variable HH reduction, for objective 3); Q9 extended to ask for the two noise terms that bound spike detection (objective 5) | — |
| bio/10 | `highly-accurate-protein-structure` | description rewritten (pLDDT/PAE, which exercises use it) and ends "Also used in physics/11." — this section stays its home | — |
| bio/10 | `improved-protein-structure-prediction`, `dual-use-of-artificial-intelligence` | `access = paid` (venue model) | venue model |
| bio/10 | `diffdock-…`, `3d-infomax-…`, `geometric-deep-learning-…` | `access = free` (arXiv-hosted DOIs) | venue model |
| bio/10 | `nobel-lecture-building-chemical-and` | `level = intermediate` | in-row evidence |
| bio/10 | `scgpt-toward-building-a-foundation-model` | description rewritten: says this section is its home, names Practice 5, cross-links Section 11 | — |
| bio/10 | `alphafold-3-open-source-inference` | licence claim dated ("as recorded in October 2026 — check both yourself") | — |
| bio/10 | `boltz-1-boltz-2-open-biomolecular` | accuracy claim labelled as the authors' own, dated October 2026 | — |
| bio/10 | README | Practice 3 names Section 06 as RDKit's home; new Check Yourself Q8 (foundation-model embedding vs PCA baseline, for objective 5) | — |
| bio/11 | **all 18 rows** | `description` written for every row (the section had none) | the fetched pages behind each row + the subsection prose |
| bio/11 | `igem-international-genetically` | `authors = iGEM`; `access = free`; description written; no `year` (igem.org is a JS shell — nothing readable to verify a founding year against, so none was invented) | https://igem.org/ |
| bio/11 | `neuralink` | `authors = Neuralink`; `access = free`; description says plainly that everything there is a vendor claim, dated October 2026 | in-row evidence |
| bio/11 | `biodefense-in-the-age-of-synthetic` | `authors = National Academies of Sciences, Engineering, and Medicine`, `year = 2018` (both already asserted by the row's verified `link_text` and the October 2026 deep-dive record), `access = free`, description written | in-repo verified record |
| bio/11 | `lifespan-why-we-age-and-why-we-don-t` | `access = paid`, `level = beginner`, description written (contested hypothesis labelled) | in-row evidence |
| bio/11 | `genome-modelling-and-design-across-all` | description written and dated ("as of October 2026 … treat 'largest' or 'state of the art' claims as dated facts") | — |
| bio/11 | `scgpt-toward-building-a-foundation-model` | **row deleted** (duplicate of bio/10, which is now its home); replaced by a cross-link line in the Foundation Models group `outro` | — |
| bio/11 | Synthetic Biology / BCI / Foundation Models group `outro`s | BCI outro rewritten so the vendor row carries a dated caveat and the measured numbers stay with Willett and Hochberg; Foundation Models outro dated and given the scGPT cross-link | — |
| bio/11 | `genetic-circuit-design-automation`, `complete-biosynthesis-of-opioids-in`, `neuronal-ensemble-control-of-prosthetic`, `a-whole-cell-computational-model`, `hallmarks-of-aging-…`, `sequence-modeling-and-design-from`, `strengthening-nucleic-acid-biosecurity` | `access = paid` (venue model) | venue model |
| bio/11 | README | new Check Yourself Q8 (turn a frontier claim into a dated, resolvable prediction — objective 2) and Q9 (what the screening evaluation showed, and why the two risk categories argue for different mitigations); old Q8 renumbered Q10 | — |
| bio/12 | `why-most-published-research-findings-are` | `access = free`; description now ends "Also used in philosophy/12."; metadata left exact (Ioannidis, 2005, PLoS Med. 2(8):e124) | — |
| bio/12 | `controlling-the-false-discovery-rate-a`, `tackling-the-widespread-and-critical` | `access = paid` (venue model) | venue model |
| bio/12 | `moderated-estimation-of-fold-change-and` | `access = free` (Genome Biology, BMC open access) | venue model |
| bio/12 | `statistics-for-biologists-including-the` | `access = free` (row already states the columns are free to read, verified 2026-10-13) | in-row evidence |
| bio/13 | `nikon-s-microscopyu-the-source-for` | `access = free` | in-row evidence |
| bio/13 | `the-axon-guide-electrophysiology-and` | `access = free`, `level = intermediate` (row states "free with registration") | in-row evidence |
| bio/13 | `super-resolution-microscopy-demystified`, `flow-cytometry-retrospective` | `access = paid` (both rows already say "(subscription)") | in-row evidence |
| bio/13 | `three-decades-of-nanopore-sequencing`, `self-driving-laboratories-to` | `access = paid` (venue model) | venue model |
| bio/13 | `pylabrobot-an-open-source-hardware` | `access = free` (the row's verified title states the tool is open source; the row's purpose is the tool) | in-row evidence |
| bio/14 | `evolutionary-rate-at-the-molecular-level`, `genealogical-trees-coalescent-theory-and`, `the-dynamics-of-molecular-evolution-over` | `access = paid` (venue model) | venue model |
| bio/14 | `iq-tree-maximum-likelihood-phylogenetic` | `access = free` (open-source tool site) | in-row evidence |

Counts: 78 rows in scope · 7 rows re-verified today · 1 row deleted · 18 descriptions written and 13 rewritten ·
49 `access` values set · 8 `level` values set · 3 author fields and 1 year field filled · 1 `more_links` added ·
5 Check Yourself questions added and 1 extended · 4 exercise source notes corrected or cross-linked ·
0 concept rows in scope (none were flagged) · 0 items added.

## 2. Objective coverage

🔑 marks a core item. "Sec NN" means the resource lives in that section and is cross-linked from here.

### bio/08 — Genomic Medicine

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| ACMG/AMP classification of a real variant | Richards et al. 🔑; ClinVar | P1 | Q1, Q2, Q5 |
| PPV of a genetic test; screening vs diagnosis | Richards et al.; bio/12 P5 (PPV model) | P2 | Q3, Q4 |
| Maximum credible population allele frequency | Richards et al. (BA1/BS1); gnomAD (Sec 02) | P3 | **Q8 (new)** |
| Design a CRISPR edit; choose editor; off-targets | Jinek et al. 🔑; Anzalone, Koblan & Liu 🔑; Doudna talk | P4 | Q6 |
| Pharmacogenomic guideline → dosing table | PharmGKB/ClinPGx (links the CPIC guideline) | P5 | Q7 |
| *(extra)* missing heritability; therapy from trial to label | Manolio et al.; FDA, Frangoul, Musunuru; Topol; All of Us | P6, mini-project | Q9 |

### bio/09 — Neuroscience

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| Implement Hodgkin-Huxley; AP, f-I curve, equivalent circuit | Hodgkin & Huxley 1952; Gerstner et al.; MIT 9.40 | P1 | Q1, Q5 |
| Cable equation; τ and λ from real parameters | Dayan & Abbott 🔑; Kandel et al. 🔑 | P3 | Q2, Q3 |
| Reduce to two dimensions; phase-plane analysis | Gerstner et al.; Dayan & Abbott 🔑 | P2 | **Q8 (new)** |
| Tuning curve, Fano factor, decoder from spike data | Dayan & Abbott 🔑; Neuromatch 🔑; Allen Brain Atlas | P4 | Q6, Q7 |
| Specify an extracellular analog front end | Jun et al. (Neuropixels); Axon Guide (Sec 13) | P6, mini-project | **Q9 (extended)** |
| *(extra)* simple-cell receptive fields; connectomes | Hubel & Wiesel; FlyWire; HCP | P5 | Q4 |

### bio/10 — AI for Biology

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| AF2 forward pass block by block | Jumper et al. 🔑; Jumper Nobel lecture | P6 | Q1, Q7 |
| Equivariance and invariance, demonstrated | Bronstein et al.; Stärk et al. | P2 | Q2 |
| Evaluate a prediction with the right metric; why CASP | Jumper et al. 🔑; Senior et al. (AF1) | P1 | Q3, Q4, Q5 |
| Audit a benchmark for leakage; restate the number | Corso et al. (DiffDock); Stärk et al. | P3, P4 | Q6 |
| Single-cell pipeline; foundation model vs baseline | scGPT; Geneformer (Sec 11) | P5 | **Q8 (new)** |
| *(extra)* run an AF3-class model; dual use | AF3 🔑 + AF3 code; Boltz; Urbina et al. | P1 step 5, mini-project | Q9 |

### bio/11 — Frontiers

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| Per frontier: load-bearing result, weakest link, deployment gap | all six subsections | P6, mini-project | Q4, Q5, Q6, Q7 |
| Convert a claim into a dated, falsifiable prediction | the subsection prose; Bunne et al. (roadmap framing) | P6 | **Q8 (new)** |
| Analyse a genetic logic circuit; where the analogy fails | Cello 🔑; iGEM | P1 | Q1, Q2 |
| BCI information rate → implant requirements | Willett et al. 🔑; Hochberg et al.; Neuralink (hardware context) | P2, mini-project (b) | Q3 |
| Judge a foundation-model claim by probing the model | Evo 🔑; Geneformer; scGPT (Sec 10) | P5, mini-project (c) | Q6 |
| *(extra)* whole-cell accounting; aging scorecard; biosecurity | Karr, Thornburg; López-Otín, Takahashi & Yamanaka, Sinclair; NASEM, Sandbrink, Wittmann et al. | P3, P4, P6 | Q4, Q5, Q7, **Q9 (new)** |

### bio/12 — Statistics and Experimental Design

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| What a *p*-value is and is not; 0.05 × 20,000 | ASA statement; Points of Significance | P1 | Q1, Q3 |
| Bonferroni vs BH; FWER vs FDR; realized FDP ≈ *q* | Benjamini & Hochberg 🔑; Holmes & Huber 🔑 | P1 | Q2 |
| Sample size for target power; effect-size inflation | "Power and sample size", "Replication"; Ioannidis | P2 | Q5, Q8 |
| Batch vs biological effect; the blocked design | Leek et al.; the design columns | P3 | Q4 |
| Why counts need a negative binomial | Love, Huber & Anders; Holmes & Huber 🔑 | P4 | Q6 |
| *(extra)* PPV model re-derived | Ioannidis | P5 | Q7 |

### bio/13 — Bioinstrumentation, Imaging and Lab Automation

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| Diffraction limit, Nyquist pixel pitch, super-resolution trade-offs | MicroscopyU 🔑; Schermelleh et al.; Nobel 2014 | P1 | Q1, Q3 |
| Photon budget for a fluorescence measurement | MicroscopyU CCD tutorials 🔑 | P2 | Q2 |
| Specify a patch-clamp / extracellular front end | The Axon Guide 🔑 | P3 | Q4 |
| Account for a sequencing run end to end | Deamer et al.; Goodwin et al. (Sec 02) | P4 | Q5 |
| Assay quality (Z′, CV) and line throughput | Assay Guidance Manual; PyLabRobot; Rapp et al. | P5 | Q6, Q7 |
| *(extra)* flow cytometry; detectors as the cryo-EM unlock | Picot et al.; Sec 03 cryo-EM materials | mini-project | Q8 |

### bio/14 — Evolution and Population Genetics

| 🎯 Objective | Resource | 🛠️ Exercise | ✅ Question |
|---|---|---|---|
| Coalescent expectations, checked against simulation | Coop 🔑; Rosenberg & Nordborg; msprime | P1 | Q1, Q2 |
| 4*Ns*; fixation probability from Kimura's formula | Kimura 🔑; Coop 🔑; Nielsen & Slatkin | P3 | Q3, Q4 |
| LD as recombination plus history; decay scale | Coop 🔑; Nielsen & Slatkin; 1000 Genomes (Sec 02) | P2 | Q5, Q6 |
| Multiple-hit correction; dating and its assumptions | IQ-TREE; Durbin et al. (Sec 04); Kimura 🔑 | P4 | Q7 |
| Read constraint and conservation scores | gnomAD/Karczewski (Sec 02); Nielsen & Slatkin | P5 | Q8 |
| *(extra)* 60,000 generations watched directly | Good et al. 2017 | mini-project | — |

Every exercise's closing `*(~time · sources)*` note was checked: each named source is either listed in its own
section or names the section that lists it. Three notes were corrected (bio/08 P3 and P5, bio/10 P3); software
libraries named inline (`statsmodels`, `pydeseq2`, `scanpy`, `e3nn`, MMseqs2) are tools rather than reading, and
were left as they are, except that RDKit and AutoDock Vina now point at Section 06.

## 3. For a browser check

Fourteen rows. Twelve need one question answered — *is the publisher's own version free to read?* — which no
reachable metadata route would answer today (see the table at the top).

| Section | Item (id) | URL | Why |
|---|---|---|---|
| bio/09 | `theoretical-neuroscience-computational` | https://mitpress.mit.edu/9780262541855/theoretical-neuroscience/ | `ROBOTS_DISALLOWED`. The authors' page confirmed title, author order and the ISBN this link uses, but not the year (2001) or the edition, so `verified` stays empty |
| bio/11 | `induction-of-pluripotent-stem-cells-from` | https://doi.org/10.1016/j.cell.2006.07.024 | Still unverifiable: Crossref `/works/<doi>` and Europe PMC returned `CLIENT_ERROR`, cell.com refused, PubMed was rate-limited. Needs year, author order, journal — and `access` |
| bio/09 | `a-quantitative-description-of-membrane` | https://doi.org/10.1113/jphysiol.1952.sp004764 | `access`: is the *J. Physiol.* archive copy free, or paywalled? |
| bio/09 | `neuronal-wiring-diagram-of-an-adult` | https://doi.org/10.1038/s41586-024-07558-y | `access` |
| bio/10 | `highly-accurate-protein-structure` | https://doi.org/10.1038/s41586-021-03819-2 | `access` — nature.com returned `CLIENT_ERROR` twice |
| bio/10 | `accurate-structure-prediction-of` | https://doi.org/10.1038/s41586-024-07487-w | `access` |
| bio/10 | `biobert-a-pre-trained-biomedical` | https://doi.org/10.1093/bioinformatics/btz682 | `access` |
| bio/10 | `scgpt-toward-building-a-foundation-model` | https://doi.org/10.1038/s41592-024-02201-0 | `access` |
| bio/11 | `a-high-performance-speech` | https://doi.org/10.1038/s41586-023-06377-x | `access` — nature.com returned body text only, with no licence or citation block |
| bio/11 | `fundamental-behaviors-emerge-from` | https://doi.org/10.1016/j.cell.2021.12.025 | `access` |
| bio/11 | `transfer-learning-enables-predictions-in` | https://doi.org/10.1038/s41586-023-06139-9 | `access` |
| bio/11 | `genome-modelling-and-design-across-all` | https://doi.org/10.1038/s41586-026-10176-5 | `access`, and a re-read of the 2026 citation details while you are there |
| bio/12 | `the-asa-statement-on-p-values-context` | https://doi.org/10.1080/00031305.2016.1154108 | `access`: the statement is widely redistributed, but the publisher page could not be read |
| bio/11 | `igem-international-genetically` | https://igem.org/ | The site is a JavaScript shell; confirm the formal organization name for `authors` and whether a founding year belongs in `year` |

## 4. Decisions for the owner

1. **Neuralink row (bio/11).** The October audit listed it as a cut candidate (a company home page with no
   technical content). I kept it, gave it an author, and made the description say plainly that everything on it
   is a vendor claim, dated October 2026 — the subsection's measured numbers now all come from Willett and
   Hochberg. It would also read fine with the row deleted and one sentence in the group `outro`.
2. **BioBERT (bio/10).** Still the weakest row in that section, as the audit said: no exercise uses it and
   biomedical NLP has moved on. It now has complete data; keep it only if you want an explicit
   biomedical-NLP thread.
3. **scGPT's home.** I made bio/10 the home (its Practice 5 benchmarks scGPT against a PCA baseline) and left
   bio/11 a cross-link in the Foundation Models `outro`. Swapping the two is a two-line change if you would
   rather Frontiers own it.
4. **`access = paid` where a free PMC copy exists.** Four bio/08 rows link a subscription publisher but have a
   free PubMed Central copy; I marked them `paid` and named the PMC accession in the description. If you prefer
   `partial` for that case, it is a one-word change in four rows.
5. **"All of Us" is typed `course`** (label "Program") so that it appears in the course index, but it is a
   research programme. Changing the type would drop it from `bio/courses/README.md`, a curriculum-level file
   outside this scope — left alone deliberately.
6. **bio/08 Practice 3** no longer cites "the maximum-credible-AF framework from the clinical genetics
   literature"; it now derives the threshold from Richards et al. plus gnomAD. If you want the framework paper
   itself listed, it needs verifying in a browser first.
7. **A full `python3 tools/build.py` is still needed before committing.** This run regenerated only
   `bio/08`–`bio/14`, so `bio/PROGRESS.md` and `bio/books/README.md` are stale against the data changes here
   (the deleted scGPT row and the new `level`/`access` values feed them). They are curriculum-level files
   outside this scope, so they were deliberately left alone; `bio/04`–`bio/06` were stale before this run.
8. **Frangoul et al. (bio/08)** keeps its 2026-10-13 `verified` date: today's record confirmed the title, year
   and first authors but not the final author the row names, and I would not re-date a citation I had only
   partly seen.
