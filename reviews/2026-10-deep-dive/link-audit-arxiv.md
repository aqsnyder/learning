# arXiv Link Audit: October 2026

We fetched each arXiv link that was in the repo before this review (**116 unique URLs**) and checked its title, authors, and date against the citation text in its row.

**Result:** 108 OK · 8 mismatches · 0 broken. All mismatches are fixed on this branch.

## Mismatches (all fixed)

| Link | Where | Problem | Fix |
|---|---|---|---|
| https://arxiv.org/abs/2012.08630 | econ/11-ai-alignment-economics-and-frontiers/README.md:19 | TITLE (minor): context title is 'Cooperative AI' but the paper at this ID is titled 'Open Problems in Cooperative AI'. Link, lead authors and year are correct (a different Dafoe et al. piece is titled 'Cooperative AI: machines must learn to find common ground'). | Open Problems in Cooperative AI \| Allan Dafoe, Edward Hughes, Yoram Bachrach et al. \| 2020 |
| https://arxiv.org/abs/2007.09540 | econ/11-ai-alignment-economics-and-frontiers/README.md:23 | AUTHOR+YEAR: link points to a paper with the claimed title, but context credits 'Michael Dennis et al.' and year 2024; the real authors are Fickinger, Zhuang, Hadfield-Menell, Russell and it was submitted July 2020. Search found no 2024 Michael Dennis paper by this title. | Multi-Principal Assistance Games \| Arnaud Fickinger, Simon Zhuang, Dylan Hadfield-Menell, Stuart Russell \| 2020 |
| https://arxiv.org/abs/2111.00396 | math/07-differential-equations/README.md:28; ml/11-frontiers/README.md:52 | TITLE (minor): link is the S4 paper (correct resource, authors/year fine), but the context title 'Structured State Spaces for Sequence Modeling (S4)' is the heading of the S4 GitHub README (github.com/state-spaces/s4, verified), not the paper title. Appears in two places. | Efficiently Modeling Long Sequences with Structured State Spaces (S4) \| Albert Gu, Karan Goel, Christopher Ré \| 2021 |
| https://arxiv.org/abs/2103.01931 | math/11-category-theory-and-frontiers/README.md:28 | AUTHOR: link is the correct paper but context leads with 'Bruno Gavranović et al.'; first author is G. S. H. Cruttwell (Gavranović is second). Year 2022 matches the ESOP 2022 publication (arXiv v1 is March 2021). [Fix at: math/11-category-theory-and-frontiers/README.md:28] | Categorical Foundations of Gradient-Based Learning \| G. S. H. Cruttwell, Bruno Gavranović, Neil Ghani, Paul Wilson, Fabio Zanasi (Cruttwell et al.) \| 2022 (arXiv 2021) |
| https://arxiv.org/abs/2503.07972 | ml/12-interpretability-and-alignment/README.md:37 | Link points to an unrelated astronomy paper, not the CoT monitorability paper. Also the author attribution 'Baker, Korbak et al.' is off: first author of the real paper is Tomek Korbak (Bowen Baker is one of 41 co-authors, not first). | https://arxiv.org/abs/2507.11473 — Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety — Korbak et al. (41 authors, incl. Bowen Baker) — 2025 (arXiv v1 2025-07-15) |
| https://arxiv.org/abs/2209.00626 | philosophy/07-existential-risk-and-alignment/README.md:27 | Link is the right paper, but the citation lists the wrong third author: 'Shlegeris' should be 'Mindermann'. Year '2023' is also arguable: arXiv v1 is 2022-08-30 (later revisions; ICLR 2024). | Ngo, Chan, Mindermann (2022) — arXiv v1 2022-08-30; revised through 2025, published ICLR 2024 |
| https://arxiv.org/abs/2212.14787 | philosophy/11-frontiers/README.md:26 | Link resolves to the correct IIT 4.0 paper, but the citation metadata is off (minor): 'Tononi et al.' is not the first author (first author is Larissa Albantakis; Tononi is last author), and the title 'IIT 4.0: Integrated Information Theory of Consciousness' is a paraphrase of the real title. | Albantakis et al. (2023) — 'Integrated information theory (IIT) 4.0: Formulating the properties of phenomenal existence in physical terms' |
| https://arxiv.org/abs/1906.01563 | physics/11-physics-informed-ml-and-frontiers/README.md:21 | Link is the right paper, but the third author is wrong: the citation says 'Schmidhuber' but the paper's third author is Jason Yosinski (Schmidhuber is not an author). | Greydanus, Dzamba & Yosinski (2019) |

## OK, with notes

- `arxiv.org/abs/2104.14294` covers DINO only. The ml/11 row now links DINOv2 (`2304.07193`) separately.
- `arxiv.org/abs/1711.10561` is PINN Part I (2017). physics/11 now also cites the 2019 *J. Comput. Phys.* paper (DOI 10.1016/j.jcp.2018.10.045).
- Several rows give the venue year (e.g. ICML 2023) rather than the arXiv v1 year. Both are acceptable, so these were left as they are.

## Not yet audited

About 600 pre-existing non-arXiv links (DOIs, YouTube, course pages, GitHub) were not checked one by one in this run, because the web budget ran out. Every resource *added* in this review was fetched before it was added. To finish the audit, run step 2 of the `audit-curriculum` skill (`python tools/check_repo.py --urls`).
