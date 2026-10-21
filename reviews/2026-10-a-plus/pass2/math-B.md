# Pass 2 log: math, sections 08–14

Scope: `math/08` to `math/14` (section `resources.toml` and `README.md` files only). Checked on 2026-10-21.
Build and check: `python3 tools/build.py --only math/08,math/09,math/10,math/11,math/12,math/13,math/14` and
`python3 tools/check_repo.py --only …` both finish with 0 problems.

How this run verified things: through WebFetch only. The session proxy blocks Crossref, Open Library and arXiv for
command-line tools, so every check below is a page fetched with WebFetch. Some publisher pages built from a known
address were refused for lack of provenance. For those, the address came from a web search, a Crossref record, or
an Open Library ISBN record instead. The shared web-search budget ran out partway through, and later one fetch hit the
hourly limit, so a few secondary checks went to the browser-check list.

## 1. Changes

| Section | Item (id) | Change | Evidence URL |
|---|---|---|---|
| 08 | a-book-of-abstract-algebra | Link added (Dover 2010 edition); author "Charles C. Pinter"; description rewritten without hype; verified | https://store.doverpublications.com/products/9780486474175 · https://openlibrary.org/isbn/9780486474175.json |
| 08 | algebra-chapter-0 | Link added (AMS Graduate Studies in Mathematics 104, 2009); description from the publisher's page; verified | https://bookstore.ams.org/gsm-104 |
| 08 | abstract-algebra-theory-and-applications | Old host `abstract.ups.edu` is robots-blocked (retried once); now links the author's current book page. Year 2026 (2026 edition; latest PDF dated August 2026); author "Thomas W. Judson"; level beginner; **now core**; description cites the verified chapters (6, 8, 14, 17, 22) and the GFDL licence; verified | https://judsonbooks.org/abstract-algebra-theory-and-applications/ · https://judsonbooks.org/aata-files/aata-20260811.pdf |
| 08 | visual-group-theory | Level beginner | — (verified 2026-10-13) |
| 08 | harvard-abstract-algebra | **Deleted.** YouTube oEmbed shows the playlist is a 38-video upload by the third-party channel "It's so blatant", and the playlist names neither Harvard, Gross nor a licence. Harvard's own course archive for Gross's Abstract Algebra gives lecture video only to registered students. So the attribution can't be confirmed and the upload may not be authorized. Suggested Order item removed; Practice 2's note now cites Visual Group Theory instead | https://www.youtube.com/oembed?url=https://www.youtube.com/playlist?list=PLelIK3uylPMGzHBuR3hLMHrYfMqWWsmx5&format=json · https://abel.math.harvard.edu/archive/122_fall_03/index.html |
| 08 | topics-in-algebra | Link added (Wiley, 2nd edition, ©1975, print on demand); access paid; level intermediate; author "I. N. Herstein"; unverified "first published 1964" dropped; verified | https://gov.wiley.com/WileyCDA/WileyTitle/productCd-0471010901,descCd-authorInfo.html |
| 08 | algebra | Link added (Springer, revised third edition, 2002); description from the publisher's page; verified | https://link.springer.com/book/10.1007/978-1-4613-0041-0 · https://api.crossref.org/works/10.1007/978-1-4613-0041-0 |
| 08 | visual-group-theory-2 | Link added (MAA Press / AMS, Classroom Resource Materials 32, 2009); access paid; level beginner; description from the publisher's page; verified | https://bookstore.ams.org/CLRM/32 |
| 09 | visual-differential-geometry-and-forms | Full title with subtitle *A Mathematical Drama in Five Acts*; link added (Princeton, July 2021); description from the publisher's page; verified | https://press.princeton.edu/books/paperback/9780691203706/visual-differential-geometry-and-forms |
| 09 | topology | Link added (Pearson Classic Version of the 2nd edition); author "James R. Munkres"; the 2000 Prentice Hall 2nd edition confirmed by ISBN; description lists the verified chapters; verified | https://www.pearson.com/en-us/subject-catalog/p/topology-classic-version/P200000006299/9780137848669 · https://openlibrary.org/isbn/9780131816299.json |
| 09 | topology-without-tears | Year 2024 (PDF "Version of August 6, 2024"); level beginner; author "Sidney A. Morris"; **now core** (the approachable entry point); description from the PDF's contents; verified | https://www.topologywithouttears.net/topbook.pdf |
| 09 | introduction-to-smooth-manifolds | Link added (Springer, 2nd edition, GTM 218, August 2012); access paid; level advanced; author "John M. Lee"; verified | https://link.springer.com/book/10.1007/978-1-4419-9982-5 · https://api.crossref.org/works/10.1007/978-1-4419-9982-5 |
| 09 | algebraic-topology | Type `course` → `video-series` (a YouTube lecture playlist, like the section's two other lecture playlists); level advanced | — (verified 2026-10-13) |
| 09 | riemannian-geometry | Link added (Birkhäuser, 1992); access paid; level advanced; author "Manfredo P. do Carmo". Dropped the unsupported "Gauss–Bonnet" and "optimization on manifolds" claims; verified | https://link.springer.com/book/9780817634902 |
| 09 | computational-topology-an-introduction | Link added (AMS, 2010); access paid; level advanced; author "John L. Harer"; description lists the verified chapters; verified | https://bookstore.ams.org/mbk-69 |
| 09 | topology-geometry | Level beginner | — |
| 09 | topology-and-data | Access free (*Bulletin of the AMS*) | — (see browser-check list) |
| 09 | introduction-to-topological-data-analysis | **Added, core.** Chazal & Michel, *An Introduction to Topological Data Analysis: Fundamental and Practical Aspects for Data Scientists* (*Frontiers in AI* 4, 2021, CC BY 4.0; arXiv v2 Feb 2021). Contents checked: complexes, persistence, the bottleneck distance and stability, confidence regions, GUDHI | https://api.crossref.org/works/10.3389/frai.2021.667963 · https://arxiv.org/abs/1710.04019 · https://arxiv.org/pdf/1710.04019 |
| 10 | the-book-of-why-the-new-science-of-cause | Link added (authors' companion page; Basic Books, 15 May 2018); access partial (Introduction and Ch. 1–2 excerpts); level beginner; **no longer core** (now step 1, the on-ramp); description without hype; verified | http://bayes.cs.ucla.edu/WHY/ · https://openlibrary.org/isbn/9780465097609.json |
| 10 | causality-models-reasoning-and-inference | Link added (DOI; Cambridge UP, 2nd edition, September 2009); access paid; level advanced; "bible" and "definitive" removed; verified | https://api.crossref.org/works/10.1017/CBO9780511803161 |
| 10 | causal-inference-in-statistics-a-primer | Link added (authors' page with previews of Ch. 1–4, homework and solutions, errata); Wiley 2016 confirmed by ISBN; author "Nicholas P. Jewell"; access partial; level intermediate; **now core**; verified | http://bayes.cs.ucla.edu/PRIMER/ · https://openlibrary.org/isbn/9781119186847.json |
| 10 | causal-inference-what-if | Level intermediate; **now core** | — (verified 2026-10-13; see browser-check list) |
| 10 | introduction-to-causal-inference | Year 2020 (Fall 2020 course); level intermediate. The description claimed exercises, which the page doesn't offer; it now lists the videos, slides, draft course book and the lecture topics; verified | https://www.bradyneal.com/causal-inference-course |
| 10 | elements-of-causal-inference-foundations | Level intermediate; **now core** | — (verified 2026-10-13) |
| 10 | applied-causal-inference-powered-by-ml | **Added** (the currency fix): Chernozhukov, Hansen, Kallus, Spindler & Syrgkanis, *Applied Causal Inference Powered by ML and AI* (arXiv, March 2024): DAGs and structural causal models plus double/debiased ML. Used by the new optional Practice 3(e) and Check Yourself 8 | https://arxiv.org/abs/2403.02467 |
| 10 | (group outro) | Cross-link added to econ Section 13 (Empirical Economics and Causal Inference) for design-based methods | — |
| 11 | category-theory-for-the-sciences | Link added: the author's own free earlier version on arXiv (*Category theory for scientists*, v3 September 2013), described as such. The MIT Press page is robots-blocked; the MIT Press edition (10 October 2014) is confirmed by ISBN. Author "David I. Spivak"; access partial; level intermediate; verified | https://arxiv.org/abs/1302.6946 · https://openlibrary.org/isbn/9780262028134.json |
| 11 | category-theory-in-context | Access free (author-hosted PDF); level advanced | — (verified 2026-10-13) |
| 11 | category-theory-for-programmers | Level intermediate; **now core** (the programming side of objective 1, Practice 2) | — (verified 2026-10-13) |
| 11 | math3ma | Access free | — |
| 11 | categories-for-the-working-mathematician | Link added (DOI of the 2nd edition). Year kept at 1998: the 1998 hardcover record has the same 329 pages as the "2. edición, two new chapters" record behind this DOI. Crossref and Open Library both carry 1978 for that print ISBN, which looks like a publisher metadata error. Access paid; level advanced; verified | https://api.crossref.org/works/10.1007/978-1-4757-4721-8 · https://openlibrary.org/isbn/9781441931238.json · https://openlibrary.org/isbn/9780387984032.json |
| 11 | backprop-as-functor | **Now core** (objective 4, Practice 4) | — (verified 2026-10-13) |
| 11 | homotopy-type-theory | Access free; level advanced | — |
| 11 | a-new-kind-of-science-wolfram-physics | The combined row "A New Kind of Science + Wolfram Physics Project" (year "2002/2020+", URL wolframphysics.org) is now the NKS book, with metadata identical to physics/11's NKS row: title "A New Kind of Science", Stephen Wolfram, 2002, book, https://www.wolframscience.com/nks/. The Physics Project stays as a second link (re-checked: announced April 2020). Access free (full text online); level intermediate. The **speculative** label stays in bold; a chapter guide for Practice 5 was added (Ch. 2–3, 11 with the Rule 110 automaton, 12 with computational irreducibility). Ends "Also used in physics/11 and philosophy/03."; verified | https://www.wolframscience.com/nks/ · https://www.wolframphysics.org/ · https://arxiv.org/abs/quant-ph/0206089 (dates the book to 2002) |
| 11 | book-review-a-new-kind-of-science | Title matched to arXiv: "Book Review: 'A New Kind of Science'" (single quotes, as philosophy/03 has it). Description taken from the abstract; link text "arXiv"; ends "Also used in physics/11 and philosophy/03."; verified | https://arxiv.org/abs/quant-ph/0206089 |
| 11 | mathematics-in-lean | Level intermediate | — |
| 12 | mit-res-6-007-signals-and-systems | Level intermediate | — |
| 12 | stanford-ee261-the-fourier-transform-and | Level intermediate | — |
| 12 | mit-6-341-discrete-time-signal | Level advanced | — |
| 12 | mit-6-011-signals-systems-and-inference | Level intermediate; **now core** (the only resource for objective 5: noise through LTI systems, matched filters, ROC) | — (verified 2026-10-13) |
| 12 | signal-processing-for-communications | Level intermediate | — |
| 12 | fourier-analysis-an-introduction | Access paid; level advanced | — |
| 13 | a-friendly-introduction-to-number-theory | Access paid; level beginner | — |
| 13 | a-computational-introduction-to-number | Level intermediate | — |
| 13 | elliptic-curves-number-theory-and | Access paid; level advanced | — |
| 13 | rational-points-on-elliptic-curves | Access paid; level intermediate | — |
| 13 | a-graduate-course-in-applied | Level advanced. Version claim dated: "version 0.6, January 2023, still the latest version as of October 2026"; verified | https://toc.cryptobook.us/ |
| 13 | understanding-cryptography | Access paid; level beginner | — |
| 14 | what-every-computer-scientist-should | Access free | — |
| 14 | mit-18-335j-introduction-to-numerical | Level advanced | — |
| 14 | numerical-linear-algebra | Link added (DOI; SIAM *Twenty-fifth Anniversary Edition*, January 2022); verified | https://api.crossref.org/works/10.1137/1.9781611977165 |
| 14 | scientific-computing-an-introductory | Access paid; level intermediate | — |
| 14 | accuracy-and-stability-of-numerical | Access paid; level advanced | — |

README changes, outside the generated tables:
- **08:** Core path now Pinter → Judson. Suggested Order renumbered without Gross. Practice notes cite verified Judson chapters. New Check Yourself 8 (orbit–stabilizer and Burnside: binary necklaces of length 6 up to rotation).
- **09:** Core path now Morris → Needham → Chazal & Michel, with one sentence on why. Suggested Order rewritten (Albin added; do Carmo placed for Practice 5). Practice 1, 2, 4 and 5 and the mini-project cite verified chapters. Lee is no longer cited for geodesics or Gauss–Bonnet, which his book's page doesn't support. New Check Yourself 8 (Clairaut's relation).
- **10:** Core path now Primer → What If → Peters et al. Suggested Order rewritten (Chernozhukov et al., Dasgupta et al. and econ/13 added). Brady Neal's notes now name the verified lecture numbers. New optional Practice 3(e) (doubly robust / DML estimate, which must agree with (b) and (c) within CIs). New Check Yourself 8 (what DML does not fix).
- **11:** Core path now Seven Sketches → Milewski → Backprop as Functor. Suggested Order notes. Practice 5's note gives NKS chapters.
- **12:** Core path adds MIT 6.011; Suggested Order step 5.
- **13:** Practice 1 names Section 00 for MIT 6.042J. New Check Yourself 8 (point decompression for p ≡ 3 mod 4) and 9 (√n cost of discrete logs, "128-bit security").
- **14:** New Check Yourself 7 (trapezoid rule on periodic functions) and 9 (recognizing Newton's quadratic convergence; safeguards).

Not in my scope: `math/PROGRESS.md`, `math/courses/README.md` and `math/books/README.md` still show the deleted Gross row and the old metadata until someone runs the full `python3 tools/build.py`.

## 2. Objective coverage

Core items in **bold**. "P" = Practice exercise, "Q" = Check Yourself question (numbers as they now stand).

### 08 Abstract Algebra

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. Group axioms, subgroups, cosets, normal subgroups for ℤₙ, D₄, A₄, Q₈, by hand and by software | **Pinter**; **Judson** Ch. 6 (Sage); Visual Group Theory; Group Explorer | P1 | Q2, Q9 |
| 2. Lagrange and the First Isomorphism Theorem; homomorphisms and quotients | **Pinter**; **Judson** Ch. 6, 9–11; Visual Group Theory | P1, P2 | Q1, Q3 |
| 3. Machine arithmetic as the ring ℤ/2ⁿℤ | **Pinter** (rings, ideals, quotient rings); **Judson** Ch. 2, 4 | P3 | Q6 |
| 4. Polynomial rings and finite fields; CRCs and Reed–Solomon; irreducible vs primitive | **Judson** Ch. 8, 17, 22; **Pinter** (polynomial rings, extensions) | P4, mini-project | Q4, Q5, Q7 |
| 5. Group actions: orbit–stabilizer, Burnside | **Judson** Ch. 14; Visual Group Theory | P5 | Q8 (new) |

### 09 Topology and Geometry

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. Axioms of a topology, bases, continuity, homeomorphism, separation axioms; finite spaces | **Morris** Ch. 1–5; Munkres Ch. 2, 4 | P1 | Q1 |
| 2. Compactness and connectedness theorems; invariants | **Morris** Ch. 3, 7; Munkres Ch. 3 | P2 | Q2, Q3 |
| 3. Gaussian curvature, angle excess, Theorema Egregium, Gauss–Bonnet (incl. discrete) | **Needham** | P3, mini-project | Q4, Q5, Q6, Q9 |
| 4. Persistent homology; barcodes; judging real features | **Chazal & Michel**; Edelsbrunner & Harer Ch. VII–VIII; Carlsson; Albin | P4 | Q7 |
| 5. Geodesics by integrating the geodesic equation; conserved quantity | **Needham** (geodesics); do Carmo (geodesic equation) | P5 | Q8 (new) |

### 10 Causal Inference

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. Association vs intervention vs counterfactual; do- and potential-outcomes notation | **Primer**; **What If**; The Book of Why | P1, mini-project | Q1, Q6, Q9 |
| 2. d-separation; backdoor and front-door criteria | **Primer** Ch. 2–3; Brady Neal lectures 3–5; Causality | P2, P4 | Q2, Q3 |
| 3. Standardization and IP weighting with bootstrap, positivity and balance checks | **What If** Ch. 12–13; Chernozhukov et al. | P3, mini-project | Q5 |
| 4. Confounding, collider bias, adjusting for a mediator | **Primer**; **What If**; The Book of Why | P1, P2, mini-project | Q3, Q4 |
| 5. Causal discovery and causal-ML claims judged by identifiability assumptions | **Peters, Janzing & Schölkopf**; Chernozhukov et al.; Schölkopf et al.; Dasgupta et al. | P5, P3(e) | Q7, Q8 (new) |

### 11 Category Theory and Frontiers

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. Categories, functors, natural transformations, adjunctions in preorders, Set, Vect, programming | **Seven Sketches**; **Milewski**; Riehl; Math3ma | P1, P2, P3 | Q1, Q3, Q5 |
| 2. Universal constructions, unique up to unique isomorphism | **Seven Sketches** Ch. 3; Riehl Ch. 1–3 | P3 | Q2, Q5 |
| 3. Galois connections for quantization and rounding | **Seven Sketches** Ch. 1; Math3ma | P1 | Q3, Q4 |
| 4. Reproduce Backprop as Functor; state what it claims | **Backprop as Functor**; Categorical Foundations of Gradient-Based Learning | P4 | Q6 |
| 5. Sort frontier claims into proven / open / philosophy | NKS and the Wolfram Physics Project (speculative, so never core); Aaronson; HoTT book; Mathematics in Lean; Georgiev et al. | P5 | Q7 |

Objective 5 is served by non-core items by design: speculation can't be core, and the skill is critical reading.

### 12 Fourier Analysis, Signals and Systems

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. Transforms of standard signals; convolution, modulation, Parseval to predict output and noise | **RES.6-007**; EE261 | P1 | Q2, Q3, Q8 |
| 2. Aliasing, anti-alias filter sizing, oversampling and decimation, ZOH droop | **RES.6-007**; **Smith** | P2 | Q1 |
| 3. FFT spectra: N, windows, coherent sampling, leakage, scalloping, ENBW, Welch | **Smith**; MIT 6.341 | P3, mini-project | Q2, Q4 |
| 4. FIR/IIR design to a spec; second-order sections in limited precision | **Smith**; **RES.6-007** (z-transform); MIT 6.341 | P4 | Q5, Q6 |
| 5. Noise through LTI systems; matched filter; ROC | **MIT 6.011** | P5 | Q3, Q7 |

### 13 Number Theory and Cryptography

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. Euclid, inverses, fast exponentiation, Fermat/Euler, CRT, RSA and RSA-CRT | **Silverman**; Stein; Shoup | P1 | Q1, Q2 |
| 2. Probabilistic primality; Carmichael numbers vs Miller–Rabin | **Silverman**; **Hoffstein–Pipher–Silverman**; Shoup | P2 | Q3, Q4 |
| 3. secp256k1 arithmetic over 𝔽ₚ, validated against parameters and a BIP-340 vector | **Hoffstein–Pipher–Silverman**; Washington; btc/01 (*Programming Bitcoin*, Corbellini) | P3, mini-project | Q5, Q8 (new) |
| 4. ECDSA and Schnorr from the group law; nonce reuse | **Hoffstein–Pipher–Silverman**; Boneh–Shoup; btc/01 (*Mastering Bitcoin* Ch. 8) | P4, mini-project | Q6, Q7, Q10 |
| 5. Discrete-log security: BSGS, rho, Pohlig–Hellman; weak curves | **Hoffstein–Pipher–Silverman**; Washington | P5 | Q5, Q9 (new) |

### 14 Numerical Methods and Scientific Computing

| Objective | Resources | Exercise | Question |
|---|---|---|---|
| 1. IEEE-754 binary32/64; when float32 fails in firmware | **Goldberg**; **Driscoll & Braun**; Higham | P1 | Q1, Q10 |
| 2. Conditioning vs stability; condition numbers; backward error | **Driscoll & Braun**; Trefethen & Bau; MIT 18.335J; Higham | P3 | Q2, Q4, Q5 |
| 3. Stable reformulations (quadratic roots, Welford, compensated summation, complex step) | **Goldberg**; **Driscoll & Braun**; Higham | P1(c), P2 | Q3 |
| 4. Interpolation and quadrature chosen by convergence theory | **Driscoll & Braun**; Heath | P4 | Q6, Q7 (new) |
| 5. Integrators for stiff systems; Newton with diagnostics and safeguards | **Driscoll & Braun**; Heath | P5, mini-project | Q8, Q9 (new) |

Every exercise's closing note names its sources, and each is listed in its section or names the section that lists it.
The one gap was 13/P1's MIT 6.042J, which now names Section 00.

## 3. For a browser check

No item in scope is left without a `verified` date. These checks could not be completed this run:

| Item (id) | URL | Why |
|---|---|---|
| 10 causal-inference-what-if | https://miguelhernan.org/whatifbook | Fetch refused this run (no provenance approval). The row is verified 2026-10-13; check the current PDF revision date and whether the suggested citation has moved past 2020 (this section's currency). |
| 11 category-theory-for-the-sciences | https://mitpress.mit.edu/9780262028134/category-theory-for-the-sciences/ | robots.txt blocks fetching. Confirm the page; if MIT Press offers a free edition, link it instead of the 2013 arXiv version. |
| 11 categories-for-the-working-mathematician | https://link.springer.com/book/10.1007/978-1-4757-4721-8 | Rate-limited, not refetched. Confirm that SpringerLink shows the 1998 second edition; its metadata says 1978. |
| 09 algebraic-topology | https://www.youtube.com/playlist?list=PLpRLWqLFLVTCL15U6N3o35g4uhMSBVA2b | The year the lectures were given wasn't found. The type is now `video-series`, which needs no year, but a year would help. |
| 09 topology-and-data | https://doi.org/10.1090/S0273-0979-09-01249-X | Access set to free on the basis that *Bulletin of the AMS* articles are free online; the article page wasn't refetched. |
| 08 harvard-abstract-algebra (deleted) | https://www.youtube.com/playlist?list=PLelIK3uylPMGzHBuR3hLMHrYfMqWWsmx5 | Only if the owner wants it back: confirm the lecturer and whether the upload is authorized. |

## 4. Decisions for the owner

1. **Gross's "Harvard Abstract Algebra" playlist was deleted** (evidence above). If you want a full lecture course on rings
   and fields as well as groups, an officially published one could replace it; none was added in this pass.
2. **Core paths changed so that the 🔑 items cover every objective** (A+ criterion 2). Each is in Suggested Order order:
   - 08: + Judson.
   - 09: Morris → Needham → Chazal & Michel.
   - 10: Primer → What If → Peters et al. *The Book of Why* is no longer core; it stays as step 1.
   - 11: Seven Sketches → Milewski → Backprop as Functor.
   - 12: + MIT 6.011.

   Revert any you disagree with. The 10 change is the most a matter of taste.
3. **math/11's Wolfram row now leads with the NKS book.** Its metadata is identical to physics/11's NKS row, and the
   Physics Project is a second link. Before, the row was a hybrid "NKS + Physics Project" pointing at wolframphysics.org.
   The physics/11 and philosophy/03 agents may also edit their rows. Re-sync after merge if their title, year or URL
   differ. The Aaronson title now follows arXiv's single quotes, as in philosophy/03; physics/11 still has double quotes.
4. *Category Theory for the Sciences* links to the author's free 2013 arXiv version (access "partial"), because the
   MIT Press page can't be fetched by the tools here.
5. Levels are judgment calls against this curriculum, for example Morris beginner, NKS intermediate, Riehl advanced
   and Paar–Pelzl–Güneysu beginner.
6. New questions need answers in pass 3: 08 Q8, 09 Q8, 10 Q8, 13 Q8–Q9, 14 Q7 and Q9. So does the optional Practice
   3(e) in 10.
