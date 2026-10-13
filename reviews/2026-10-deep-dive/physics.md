# Physics — Review

> **Deep-dive review, October 2026** · curriculum: [`physics/`](../../physics/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict
The physics curriculum is a clean, conventional physics-major sequence (mechanics → waves → thermo → E&M → QM → relativity → computation → quantum computing → solids → fluids → chaos → physics-ML). Its canonical textbook choices are sound (Feynman, Taylor, Schroeder, Griffiths, Carroll, Strogatz, Newman), and every section has a usable suggested order. It falls short in three ways. (1) **Citation accuracy:** the video courses were the weakest spot. Three MIT courses were attributed to Walter Lewin: two pointed at YouTube playlist IDs that do not resolve, and MIT has not hosted Lewin's lectures since 2014. Strogatz's Cornell lectures were labelled "Yale", two Susskind links pointed at the wrong playlists, the Qiskit Textbook had been archived, and the HNN paper credited Schmidhuber instead of Yosinski. (2) **Currency:** the fast-moving sections stopped around 2018–2022 (quantum computing had nothing after 2018; physics-ML nothing after 2022). (3) **Fit to Aaron:** for an embedded/sensor/precision-measurement engineer, the physics behind his daily work was almost absent: noise, measurement, device physics, engineering EM, heat transfer, and optics for sensors. Separately, the July 2026 Wolfram material was marked 🔑 and described as "deriving" GR and QM, with no caveat. **Grade: C+ as found, roughly B after this pass.** The single most important improvement was a dedicated **Measurement, Noise & Sensor Physics** section. The reviewer approved it, and it now exists as `physics/12-measurement-noise-and-sensor-physics/` (see below). The bridging pieces that fit inside existing sections were added there.

## Scorecard
Scores reflect the files **as found** (1–5); the fixes made are listed per section below.

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 Classical Mechanics | 4 | 2 | 4 | 4 | 4 | B− | Strong canon. The 8.01 "Lewin" link was dead/misattributed, and the Feynman chapter range was wrong. |
| 01 Waves and Optics | 2 | 3 | 3 | 2 | 3 | C | Optics is one textbook. Placed before E&M, which 8.03 and Hecht assume. 8.03 was misattributed. |
| 02 Thermo & Stat Mech | 3 | 5 | 4 | 4 | 4 | B+ | Accurate and well ordered; missing fluctuations/noise (Johnson–Nyquist) and radiation emphasis. |
| 03 Electromagnetism | 3 | 2 | 3 | 4 | 4 | C+ | Good theory core, but nothing between Griffiths and the PCB SI/EMC sections. The 8.02 entry was a dead Lewin link. |
| 04 Quantum Mechanics | 4 | 4 | 4 | 4 | 3 | B | Standard path; Griffiths QM missing co-author/edition; no engineering bridge; heavy on grad texts. |
| 05 Relativity | 4 | 3 | 3 | 4 | 4 | B | Fine SR→GR ramp; the Susskind SR link went to a third-party mega-playlist; no applications (GPS, LIGO). |
| 06 Computational Physics | 3 | 4 | 3 | 3 | 3 | C+ | Four overlapping textbooks; FEM is promised but not practised; placed too late in the sequence. |
| 07 Quantum Computing | 3 | 3 | 2 | 4 | 3 | C | Qiskit Textbook archived; duplicate IBM entries; nothing after 2018 (no 2024 below-threshold QEC). |
| 08 Condensed Matter | 2 | 3 | 3 | 4 | 4 | C+ | Claims to matter for "electronic devices" but has no device physics. 8.231 "lectures" are problem sets only. |
| 09 Fluids & Continuum | 2 | 4 | 3 | 4 | 4 | C+ | "Continuum" with no elasticity or heat transfer; Kundu edition stale; no hands-on CFD. |
| 10 Nonlinear Dynamics | 4 | 3 | 4 | 4 | 4 | B | Strogatz-centred and good; lectures mislabelled "Yale" (Cornell); 3rd ed. (2024) not noted. |
| 11 Physics-ML & Frontiers | 3 | 2 | 2 | 4 | 2 | C− | HNN author error, PINN citation mismatch, 🔑 on the speculative Wolfram project, no neural operators, nothing post-2022. |

## Section-by-section

### 00 — Classical Mechanics
- **Strengths:** The canonical ladder is in the right order: Feynman → Taylor (primary) → Morin → Susskind → Landau & Lifshitz → Goldstein. The 🔑 use is sensible.
- **Problems:**
  - ✔ The "MIT 8.01 — Walter Lewin" row linked a YouTube playlist ID that does not resolve. MIT removed Lewin's lectures from its online platforms in December 2014 after finding he had sexually harassed an online learner. I re-pointed the row to MIT's current **8.01SC (Fall 2016)**, which has full lecture videos, and added a one-line note about Lewin in the suggested order.
  - ✔ The Feynman range "mechanics chapters (1–15)" included special relativity (Ch. 15) and skipped rotation and oscillators (Ch. 18–25). It is now "Ch. 1–14 and 18–25". The note flags Ch. 21–25 (resonance, transients, linear systems) for circuit intuition and sends Ch. 15–17 to Section 05.
  - ✱ No book links at all; Morin posts some chapters free on his site.
- **Missing:** Dimensional analysis and estimation (useful for an engineer), and computational mechanics (integrating orbits and oscillators in Python from day one).
- **Added:** nothing needed.

### 01 — Waves and Optics
- **Strengths:** The 3Blue1Brown Fourier pair is a good on-ramp, and Crawford and Pain are good waves texts.
- **Problems:**
  - ✔ "MIT 8.03 — Walter Lewin": the playlist is actually *MIT 8.03SC Physics III: Vibrations and Waves, Fall 2016* (Yen-Jie Lee). Fixed in the section, courses/ and PROGRESS.
  - ✔ The Feynman row said "Ch. 47–51", but the suggested order promised interference and diffraction, which are Ch. 29–30. It now reads "Ch. 26–36 (optics) and 47–51 (waves)".
  - ✔ (sequencing note) 8.03 and Hecht both assume first-year E&M. The suggested order now says to take the EM-wave lectures and Hecht after or alongside Section 03.
  - ✱ The 🔑 marks sit on two short 3Blue1Brown videos while no core text is 🔑. Crawford, or Hecht after E&M, should carry it.
  - ✱ Structural: "waves" belongs before E&M, "optics" after it. Consider splitting the section or moving optics after 03.
- **Missing:** For a sensor designer, the optics here is thin. Nothing covers first-order optical design (focal length, f-number, field of view, stops), Fresnel lenses, radiometry/étendue, photodetectors and their noise, fiber, or photonics.
- **Added:** nothing. I tried to verify Saleh & Teich, *Fundamentals of Photonics* (3rd ed.), MIT OCW 2.71 *Optics* and the CU Boulder *Optical Engineering* specialization, but the fetches were rate-limited (HTTP 429). They are listed as candidates in the proposal below.

### 02 — Thermodynamics and Statistical Mechanics
- **Strengths:** Schroeder as the primary text, Feynman first and Kardar/Sethna for depth is an excellent spine. No accuracy errors were found; the Feynman range Ch. 39–46 is correct.
- **Problems:** ✱ Blackbody radiation was not called out, although it is the physics behind thermal-IR sensing. ✔ The Schroeder step now mentions it.
- **Missing:** Fluctuations and noise: the fluctuation–dissipation theorem, Johnson–Nyquist noise and shot noise. Also transport and non-equilibrium, and Landauer's principle (computation ↔ thermodynamics, a mainstream counterpart to the Wolfram material).
- **Added:**
  - Thermal Agitation of Electric Charge in Conductors — Harry Nyquist — 1928. It sits in one row with J. B. Johnson's companion paper, "Thermal Agitation of Electricity in Conductors" (1928). Both DOIs are linked, and it is placed in the suggested order right after Schroeder.

### 03 — Electromagnetism
- **Strengths:** Griffiths + Feynman Vol. 2 + Purcell + Jackson is the right theory stack, and the 3Blue1Brown div/curl primer is a good start.
- **Problems:**
  - ✔ "MIT 8.02 — Walter Lewin" linked playlist `…QMi`, while courses/ linked `…QMk`; neither resolves. MIT OCW has no video 8.02 (the 2007 and 8.02X 2005 versions are notes and problem sets only). The row is replaced with **Yale PHYS 201, Fundamentals of Physics II (Ramamurti Shankar, 2010)**, which has free video, audio and transcripts and covers E&M, optics and intro QM. A note on Lewin was added.
  - ✔ Griffiths edition noted: 5th ed., Cambridge 2023.
  - ✔ The Purcell description "special-relativity-first approach" was reworded to "derives magnetism from electrostatics plus special relativity".
  - ✔ The Feynman Vol. 2 step now points at Ch. 22–24 (AC circuits, cavity resonators, waveguides).
- **Missing:** Engineering EM: transmission lines, skin effect, quasistatics (capacitive/inductive coupling, shielding, guarding), radiation and antennas. This is exactly the gap between this section and pcb/06–07.
- **Added:**
  - Electromagnetics, Vol. 1 & 2 — Steven W. Ellingson — 2018/2020 (open textbook, CC BY-SA)
  - Electromagnetic Fields and Energy — Hermann A. Haus & James R. Melcher — 1989 (free on MIT OCW with demo videos)

### 04 — Quantum Mechanics
- **Strengths:** Visual → Feynman → 8.04 → Griffiths is a good ramp, with deep references available.
- **Problems:**
  - ✔ The current Griffiths QM is the 3rd ed. (2018), co-authored with Darrell F. Schroeter. Fixed in the section, books/ and PROGRESS.
  - ✔ The prerequisites omitted linear algebra, the language of the subject. It has been added.
  - ✱ Three graduate references (Shankar, Sakurai, Cohen-Tannoudji) is a lot for a self-learner. Mark one as "reference only".
- **Missing:** An engineering bridge to devices and optics: tunneling, electrons in crystals, optical transitions.
- **Added:**
  - Quantum Mechanics for Scientists and Engineers — David A. B. Miller — 2008

### 05 — Special and General Relativity
- **Strengths:** Taylor & Wheeler → Einstein 1905 → Hartle → Schutz → Carroll → MTW is a textbook-perfect ramp.
- **Problems:**
  - ✔ The Susskind SR link went to "Leonard Susskind – All Stanford physics lectures in order", a third-party playlist. It now points to Stanford's "Lecture Collection | Special Relativity" (`PLD9DDFBDC338226CA`, the ID given on theoreticalminimum.com).
  - ✔ Free links were added to existing entries: *Spacetime Physics* 2nd ed. (now CC BY 4.0 on eftaylor.com) and Carroll's 1997 *Lecture Notes on General Relativity* (arXiv gr-qc/9712019).
  - ✱ I could not verify Schutz's 3rd edition (2022), so it is not noted.
- **Missing:** Applications that make relativity concrete for an engineer: GNSS timing, and gravitational-wave detection as precision measurement.
- **Added:**
  - Relativity in the Global Positioning System — Neil Ashby — 2003
  - Observation of Gravitational Waves from a Binary Black Hole Merger — LIGO Scientific & Virgo Collaborations — 2016

### 06 — Computational Physics
- **Strengths:** Kinder & Nelson → Newman is a good Python-first start, and Numerical Recipes is a sensible reference.
- **Problems:**
  - ✔ PROGRESS called the Landau/Páez/Bordeianu book *Computational Physics*, while the section calls it *A Survey of Computational Physics*. They are now harmonised.
  - ✱ The compadre.org link for that book points at a generic PICUP "Course-Materials" page; the URL audit should confirm.
  - ✱ Four overlapping general textbooks (Newman, Giordano & Nakanishi, Thijssen, Landau et al.) dilute focus.
  - ✱ Sequencing: this section is a tool you need from Section 00 onward, so start Kinder & Nelson and Newman alongside mechanics.
- **Missing:** Hands-on FEM (the "Why" promises it), differentiable/JAX-style simulation, uncertainty quantification.
- **Added:**
  - The FEniCSx Tutorial — Jørgen S. Dokken — online, CC BY 4.0, updated 2026. It grew out of Langtangen & Logg's open-access *Solving PDEs in Python* (2016), which is noted in the text.

### 07 — Quantum Computing
- **Strengths:** The theory core is right: Nielsen & Chuang, Preskill notes, Mermin, Aaronson.
- **Problems:**
  - ✔ The "Qiskit Textbook" entry (🔑) was stale. The textbook's GitHub repo says it "has been superseded by IBM Quantum Learning" and was archived on 18 Jan 2024. The row is now John Watrous's *Understanding Quantum Information & Computation* series on IBM Quantum Learning.
  - ✔ `learning.quantum.ibm.com` now 302-redirects to `quantum.cloud.ibm.com/learning`; the link is updated.
  - ✔ Shor's 1994 FOCS paper was paywalled only; the free expanded arXiv version (quant-ph/9508027) was added.
  - ✱ Rows #1 and #3 (IBM) and #6 (3Blue1Brown, which duplicates Section 04) are redundant.
  - ✱ Shor's paper as a 🔑 "must-read" is heavy for a learner; N&C Ch. 5 teaches the same thing.
- **Missing:** Hardware and engineering (control electronics, decoherence), the 2024–25 error-correction milestones, today's RSA threat estimate, NISQ vs fault-tolerant framing, and post-quantum cryptography (probably belongs to btc/software).
- **Added:**
  - Quantum Computing in the NISQ Era and Beyond — John Preskill — 2018
  - A Quantum Engineer's Guide to Superconducting Qubits — Krantz et al. — 2019
  - Quantum Error Correction Below the Surface Code Threshold — Google Quantum AI and Collaborators — 2024 (Nature 638, 2025). Verified: distance-7 code, 101 qubits, Λ = 2.14.
  - How to Factor 2048 Bit RSA Integers with Less Than a Million Noisy Qubits — Craig Gidney — 2025

### 08 — Condensed Matter and Materials
- **Strengths:** Anderson → Simon → Kittel → Ashcroft & Mermin → Girvin & Yang is a solid ladder.
- **Problems:**
  - ✔ "MIT 8.231 — Lectures to supplement your textbook" was wrong. The OCW page (Xiao-Gang Wen, Fall 2006) has problem sets only. The row and suggested order are corrected.
  - ✱ The "Why" promises relevance to electronic devices, but there was no device physics.
- **Missing:** Semiconductor devices (junctions, MOS, BJTs, photodiodes), noise in solids, and dielectric/piezo/pyroelectric materials for sensors. The suggested order now points at Kittel's dielectrics & ferroelectrics chapter.
- **Added:**
  - The Oxford Solid State Basics (lecture videos) — Steven H. Simon — 2014. This 21-lecture series pairs with the 🔑 Simon text.
  - Modern Semiconductor Devices for Integrated Circuits — Chenming Hu — 2010 (all 8 chapters free on the author's site)
  - Low-Frequency Fluctuations in Solids: 1/f Noise — P. Dutta & P. M. Horn — 1981 (later **moved to the new Section 12**; §08 now ends with a 'Next: Section 12' pointer)

### 09 — Fluid Dynamics and Continuum
- **Strengths:** Acheson → Kundu → Batchelor/L&L is the right fluids core, and Brunton & Kutz is a good modern bridge.
- **Problems:**
  - ✔ Kundu updated to the 7th ed. (Elsevier 2024), now with Capecelatro as co-author.
  - ✔ The Feynman row now covers Vol. 2 Ch. 38–39 (elasticity) as well as Ch. 40–41. Elasticity was the only "continuum solid" content available.
  - ✱ MIT 18.085 duplicates Section 06.
- **Missing:** Solid mechanics/elasticity (still thin), heat transfer, hands-on CFD.
- **Added:**
  - National Committee for Fluid Mechanics Films — Ascher Shapiro et al. — 1961–1969
  - CFD Python: 12 Steps to Navier–Stokes — Lorena A. Barba & Gilbert F. Forsyth — 2013 (JOSE 2018)
  - A Heat Transfer Textbook (6th ed.) — John H. Lienhard IV & John H. Lienhard V — 2024 (free PDF)

### 10 — Nonlinear Dynamics and Chaos
- **Strengths:** One of the best sections. Strogatz book + lectures are paired with Lorenz and May's original papers, plus Gleick for motivation.
- **Problems:**
  - ✔ "Strogatz (Yale lectures)" was wrong. The playlist is "Nonlinear Dynamics and Chaos – Steven Strogatz, Cornell University" (Cornell MAE). Fixed in the section, courses/ and PROGRESS.
  - ✔ Strogatz 3rd ed. (2024) is noted; its new Kuramoto/synchronization chapter is relevant to coupled oscillators and phase locking.
  - ✔ PROGRESS was missing Lorenz's *The Essence of Chaos* and Peitgen et al.'s *Chaos and Fractals*; both are added.
- **Missing:** Noise-driven and stochastic dynamics (Langevin), mostly covered elsewhere.
- **Added:** nothing needed.

### 11 — Physics-Informed ML and Frontiers
- **Strengths:** Good 2018–2022 core: neural ODEs, PINNs, HNN/LNN, GNS, MP-PDE, EGNN and the Karniadakis review.
- **Problems:**
  - ✔ HNN was credited to "Greydanus, Dzamba & Schmidhuber"; the third author is **Jason Yosinski**. The link audit independently flagged this too.
  - ✔ PINN was cited as 2019 but linked only the 2017 Part I preprint. It now links the J. Comput. Phys. 378 (2019) DOI plus the labelled preprint.
  - ✔ The AlphaFold step claimed "physics priors enabled this breakthrough". It is reworded: the success came mainly from MSA/evolutionary data plus an equivariant structure module, not explicit physics.
  - ✔ **Wolfram material.** The "Why" paragraph said the project derives GR, QM and thermodynamics; it now says this is an unconfirmed program outside mainstream physics, with no experimentally confirmed distinguishing predictions and no community acceptance. 🔑 was removed from the Wolfram Physics Project and the row is labelled "speculative, outside mainstream physics". The NKS and Physics Project steps are now "optional, speculative" with honest framing. Scott Aaronson's 2002 NKS review (Bell-inequality/relativity critique) was added as the counterweight. Nothing was deleted.
  - ✔ PROGRESS was missing Satorras (EGNN), NKS and the Wolfram project; all are added (Brunton & Kutz is already tracked under 09).
- **Missing:**
  - Neural operators (now added).
  - ML weather/climate models: GraphCast is in ml/13. I would add NeuralGCM (Kochkov et al., *Nature* 2024, a hybrid differentiable dynamical core) and GenCast (Price et al., *Nature* 2025), but their pages were rate-limited, so they are unverified and not added.
  - Critical evaluation: McGreivy & Hakim 2024 on weak baselines in ML-for-PDEs (arXiv 2407.07218, rate-limited, not added) and PINN failure modes (Krishnapriyan et al. 2021).
  - Symbolic regression and law discovery (SINDy paper, PySR/AI Feynman).
- **Added:**
  - Fourier Neural Operator for Parametric PDEs — Li et al. — 2020
  - DeepONet: Learning Nonlinear Operators — Lu et al. — 2019 (Nature Machine Intelligence 2021)
  - Book Review: "A New Kind of Science" — Scott Aaronson — 2002

### books/README.md
- **Strengths:** A short, sensible canon with a reading order.
- **Problems:**
  - ✔ Editions and co-authors updated: Griffiths E&M 5e 2023; Griffiths & Schroeter QM 3e 2018; Strogatz 3e 2024; Kundu et al. 7e 2024; *Spacetime Physics* marked free.
  - ✱ 🔑 marks are inconsistent with the sections: Kittel, Nielsen & Chuang, *Spacetime Physics*, Kundu and Carroll are 🔑 in their sections but not here. Left for you to decide.
- **Added:** Ellingson's *Electromagnetics* and Hu's *Modern Semiconductor Devices* (cross-listed as the two free "engineer's bridge" books) and a reading-order line.

### courses/README.md
- **Problems:**
  - ✔ 8.01 and 8.02 Lewin rows (dead playlist IDs, different from the section links) are replaced as in 00 and 03.
  - ✔ The Susskind QM link was Stanford's *Advanced Quantum Mechanics* playlist; it now points to *The Theoretical Minimum: Quantum Mechanics* (`PL701CD168D02FF56F`, matching Section 04).
  - ✔ Strogatz "Yale" → Cornell.
  - ✔ The Qiskit row was labelled "qiskit.org" but linked IBM; it is now the Watrous course.
  - ✔ Feynman's section coverage is extended to 08 and 09.
  - ✔ The intro no longer says "legendary classroom recordings (Lewin…)".
- **Added:** cross-listed MIT 8.03SC (in Section 01 but missing here) and Simon's Oxford Solid State Basics lectures. ✱ Susskind SR is still not listed here.

### blogs-and-references/README.md
- **Strengths:** A reasonable mix of Q&A, magazine, blogs and reference.
- **Problems:**
  - ✱ The n-Category Café is far off Aaron's path.
  - ✱ Brilliant is paid and generic.
  - ✱ Sean Carroll's activity has largely moved to his *Mindscape* podcast (not verified; worth checking).
  - ✱ The `ocw.mit.edu/courses/physics/` URL pattern predates OCW's 2022 redesign; the audit should check it.
- **Missing:** Reference data a hardware engineer actually uses: NIST CODATA constants and units/uncertainty pages, the BIPM SI Brochure, and the JCGM GUM. They are not added because the fetch budget ran out.
- **Added:** nothing.

### PROGRESS.md
- **Problems:**
  - ✔ Out of sync with the sections: Section 10 was missing 2 items and Section 11 was missing 4; Books lacked 3 titles listed in books/; there was a title mismatch for Landau et al.
  - ✔ Lewin, Yale and Qiskit errors were carried in both the section and "supplementary" lists.
  - ✔ All 20 additions are tracked.
  - ✱ The "Books/Courses (supplementary)" lists duplicate section items, so the same book is tracked twice. Make the supplementary lists cross-references or drop them.

### README.md
- **Strengths:** Clear learning path and NotebookLM guidance; it is consistent with the folders.
- **Problems:** None factual. ✱ The purpose statement ("physical principles underlying simulation, modeling, and AI for science") ignores Aaron's actual use case (hardware, sensors, measurement). See Structural observations.
- **Added:** nothing (not restructured in this review).

## Corrections made
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| physics/00-classical-mechanics/README.md:15 | MIT 8.01 Classical Mechanics — Walter Lewin; playlist `PLUl4u3cNGP61qDex7XslwNJ-xxxEFzBs3` (does not resolve) | MIT 8.01SC Classical Mechanics (Fall 2016) — Chakrabarty, Dourmashkin et al. → OCW course | https://ocw.mit.edu/courses/8-01sc-classical-mechanics-fall-2016/ ; https://www.cbsnews.com/boston/news/mit-pulls-online-lectures-over-harassment-claim/ |
| physics/00-classical-mechanics/README.md:29–30 | Feynman "mechanics chapters (1–15)"; "MIT 8.01 (Lewin)" | Ch. 1–14 and 18–25 (15–17 → §05); 8.01SC + Lewin note | https://www.feynmanlectures.caltech.edu/I_toc.html |
| physics/01-waves-and-optics/README.md:15, 30 | Feynman "Waves chapters (Vol. 1, Ch. 47–51)" while promising interference/diffraction | "Optics and Waves chapters (Vol. 1, Ch. 26–36 and 47–51)" | https://www.feynmanlectures.caltech.edu/I_toc.html |
| physics/01-waves-and-optics/README.md:20, 31 | MIT 8.03 Vibrations and Waves — Walter Lewin | MIT 8.03SC Vibrations and Waves (Fall 2016) — Yen-Jie Lee (+ "assumes first-year E&M") | https://ocw.mit.edu/courses/8-03sc-physics-iii-vibrations-and-waves-fall-2016/ (YouTube oEmbed title: "MIT 8.03SC Physics III: Vibrations and Waves, Fall 2016") |
| physics/03-electromagnetism/README.md:15 | Introduction to Electrodynamics — Griffiths | … (5th ed., 2023) | https://www.cambridge.org/highereducation/product/FD23E188E2BDCDB40199CFE3386EC08F |
| physics/03-electromagnetism/README.md:17, 30 | MIT 8.02 Electricity and Magnetism — Walter Lewin; playlist `…QMi` (does not resolve; courses/ had `…QMk`) | Fundamentals of Physics II (Yale PHYS 201, 2010) — Ramamurti Shankar + Lewin note | https://oyc.yale.edu/physics/phys-201 ; https://ocw.mit.edu/courses/8-02-physics-ii-electricity-and-magnetism-spring-2007/ (no videos) |
| physics/03-electromagnetism/README.md:34 | Purcell: "special-relativity-first approach to magnetism" | "derives magnetism from electrostatics plus special relativity" | (wording accuracy; Purcell & Morin Ch. 5 "The fields of moving charges") |
| physics/04-quantum-mechanics/README.md:15, 34 | Introduction to QM — David J. Griffiths | (3rd ed., 2018) — Griffiths & Darrell F. Schroeter | https://assets.cambridge.org/97811071/89638/copyright/9781107189638_copyright_info.pdf |
| physics/05-special-and-general-relativity/README.md:15 | Spacetime Physics — link "—" | 2nd ed. 1992, free CC BY 4.0 link | https://www.eftaylor.com/spacetimephysics/ |
| physics/05-special-and-general-relativity/README.md:16 | Susskind SR → `PL6i60qoDQhQGaGbbg-4aSwXJvxOqO6o5e` ("Leonard Susskind – All Stanford physics lectures in order", uploader Mike Blackstock) | `PLD9DDFBDC338226CA` (Stanford "Lecture Collection \| Special Relativity") | https://theoreticalminimum.com/courses/special-relativity-and-electrodynamics/2012/spring |
| physics/05-special-and-general-relativity/README.md:18 | Carroll — link "—" | free 1997 lecture notes | https://arxiv.org/abs/gr-qc/9712019 |
| physics/07-quantum-computing/README.md:15, 35 | Qiskit Textbook (🔑) → learning.quantum.ibm.com | Understanding Quantum Information & Computation — John Watrous (IBM Quantum Learning; successor to archived Qiskit Textbook) | https://github.com/Qiskit/textbook ; https://quantum.cloud.ibm.com/learning/en/courses/basics-of-quantum-information |
| physics/07-quantum-computing/README.md:17 | learning.quantum.ibm.com | quantum.cloud.ibm.com/learning/en (302 target) | https://quantum.cloud.ibm.com/learning/en |
| physics/07-quantum-computing/README.md:22 | Shor — IEEE link only (paywalled) | + free expanded arXiv version | https://arxiv.org/abs/quant-ph/9508027 |
| physics/08-condensed-matter-and-materials/README.md:18, 37 | MIT 8.231 Physics of Solids — "Lectures to supplement your textbook" | "… I (Fall 2006) — Xiao-Gang Wen (problem sets only)"; order text corrected | https://ocw.mit.edu/courses/8-231-physics-of-solids-i-fall-2006/ |
| physics/09-fluid-dynamics-and-continuum/README.md:15 | Fluid Mechanics — Kundu, Cohen & Dowling | (7th ed., 2024) — Kundu, Cohen, Dowling & Capecelatro | https://shop.elsevier.com/books/fluid-mechanics/kundu/978-0-12-819807-0 |
| physics/09-fluid-dynamics-and-continuum/README.md:16, 32 | Feynman "Fluid Flow chapters (Vol. 2, Ch. 40–41)" | "Elasticity and Fluid Flow chapters (Vol. 2, Ch. 38–41)" | https://www.feynmanlectures.caltech.edu/II_toc.html |
| physics/10-nonlinear-dynamics-and-chaos/README.md:15, 30 | Nonlinear Dynamics and Chaos — Strogatz | (3rd ed., 2024) + Kuramoto chapter note | https://www.routledge.com/Nonlinear-Dynamics-and-Chaos-With-Applications-to-Physics-Biology-Chemistry-and-Engineering/Strogatz/p/book/9780367026509 |
| physics/10-nonlinear-dynamics-and-chaos/README.md:16, 31 | Strogatz (Yale lectures) | Cornell lectures | YouTube oEmbed for `PLbN57C5Zdl6j_qJA-pARJnKsmROzPnO9V`: "Nonlinear Dynamics and Chaos - Steven Strogatz, Cornell University" (Cornell MAE) |
| physics/11-physics-informed-ml-and-frontiers/README.md:7 | Wolfram project "deriving general relativity, quantum mechanics, and thermodynamics…" | Speculative, unconfirmed, outside mainstream; critique listed; mainstream bridges named | https://arxiv.org/abs/quant-ph/0206089 |
| physics/11-physics-informed-ml-and-frontiers/README.md:20, 43 | PINN (2019) → arXiv 1711.10561 only | J. Comput. Phys. 2019 DOI + labelled 2017 Part I preprint | https://doi.org/10.1016/j.jcp.2018.10.045 |
| physics/11-physics-informed-ml-and-frontiers/README.md:21 | HNN — Greydanus, Dzamba & Schmidhuber | Greydanus, Dzamba & Yosinski | https://arxiv.org/abs/1906.01563 |
| physics/11-physics-informed-ml-and-frontiers/README.md:30, 53, 55 | Wolfram Physics Project 🔑; NKS "controversial but thought-provoking" | 🔑 removed; labelled speculative/optional; honest order text | https://arxiv.org/abs/quant-ph/0206089 |
| physics/11-physics-informed-ml-and-frontiers/README.md:52 | AlphaFold: "Understand how physics priors enabled this breakthrough" | success mainly from MSA data + equivariant structure module, not explicit physics | https://doi.org/10.1038/s41586-021-03819-2 |
| physics/courses/README.md:5, 13, 14, 37 | Lewin 8.01/8.02 rows (`…xxxEFzBs3`, `…QMk`), "legendary classroom recordings (Lewin…)" | 8.01SC (OCW) and Yale PHYS 201; intro and order text updated | as rows above |
| physics/courses/README.md:15, 36 | Feynman sections "00–05" | "00–05, 08, 09" | https://www.feynmanlectures.caltech.edu/III_toc.html |
| physics/courses/README.md:18 | Steven Strogatz (Yale) | (Cornell) | oEmbed as above |
| physics/courses/README.md:20 | Susskind QM → `PLpGHT1n4-mAsmMxmSX0LCaXIXT2PmU85m` (Stanford "Advanced Quantum Mechanics") | `PL701CD168D02FF56F` ("The Theoretical Minimum: Quantum Mechanics") | YouTube oEmbed for both IDs |
| physics/courses/README.md:24, 44 | "Qiskit Textbook — IBM — `[qiskit.org](learning.quantum.ibm.com)`" | Watrous course on IBM Quantum Learning | https://github.com/Qiskit/textbook |
| physics/books/README.md:14, 15, 17, 22, 23, 42 | Griffiths E&M/QM, Strogatz, Spacetime Physics, Kundu without editions/co-authors | editions + Schroeter + Capecelatro + free note | as above |
| physics/PROGRESS.md:10, 23, 39, 47, 74, 79, 104, 105, 117, 145, 152, 161, 162, 166, 171 | Lewin ×4, "MIT 8.03", Griffiths-only QM, *Computational Physics* (Landau et al.), Qiskit ×2, Kundu ×2, Feynman "Fluid chapters", Strogatz "Yale"/no venue | corrected to match sections | as above |
| physics/00-classical-mechanics/README.md:55; physics/01-waves-and-optics/README.md:51 (merged Practice blocks) | resource notes "Lewin 8.01" / "Lewin 8.03" | "MIT 8.01SC" / "MIT 8.03SC" | as rows above |
| physics/03-electromagnetism/README.md:56, 69 (merged Practice / Check Yourself) | "Recreate Lewin's two-voltmeter demo… (Lewin 8.02 …)"; "In Lewin's two-voltmeter demo…" | "the classic two-voltmeter demo (made famous by Walter Lewin's 8.02 lecture)"; resource → Shankar PHYS 201 (induction lectures); question de-personalized | as rows above |
| physics/07-quantum-computing/README.md:62 (merged Practice) | "Qiskit Textbook / IBM Quantum Learning" | "Watrous / IBM Quantum Learning" | https://github.com/Qiskit/textbook |
| physics/11-physics-informed-ml-and-frontiers/README.md:73 (merged Practice) | "Greydanus, Dzamba & Schmidhuber" (the scaffolding re-introduced the error) | "Greydanus, Dzamba & Yosinski" | https://arxiv.org/abs/1906.01563 |
| physics/PROGRESS.md (§10, §11, Books) | missing Lorenz *Essence of Chaos*, Peitgen *Chaos and Fractals*, Satorras EGNN, NKS, Wolfram project, Carroll, L&L *Mechanics*, Jackson | added (sync with section/books files) | — |

## Proposed new sections (not created; update: the one proposal below was approved and created as Section 12)

### Measurement, Noise & Sensor Physics — ✅ CREATED in this review

**What was created:** `physics/12-measurement-noise-and-sensor-physics/README.md`, titled "Measurement, Noise, and Sensor Physics". It is appended as Section 12, so nothing is renumbered, and its recommended position is right after Section 08. It follows the merged section format (Why, Recommended position, Prerequisites, 🎯 Learning Objectives, Resources, Suggested Order, 🛠️ Practice, ✅ Check Yourself).

- **Resources:** the table holds only verified items:
  - Keithley/Tektronix *Low Level Measurements Handbook* (7th ed., 2014), free PDF, 🔑, verified by the pcb reviewer
  - Sarpeshkar, Delbrück & Mead (1993), 🔑
  - Dutta & Horn (1981), **moved here from §08**; it was added to §08 earlier in this pass, so nothing from master was deleted

  An "Also used here (tracked in their home sections)" line cross-references the other verified items without double-tracking them in PROGRESS: Johnson/Nyquist (§02), Haus & Melcher (§03), Ashby and LIGO (§05), Hu and Kittel (§08), Lienhard (§09). It also links pcb/00, pcb/07 and pcb/12.
- **Practice (5):**
  1. Thermal noise is shot noise (Sarpeshkar's argument)
  2. Noise figure and the optimum source, with a calibrated audio-ADC/scope PSD measurement
  3. Lock-in from scratch, simulated then built on an MCU
  4. Allan deviation, synthetic then an overnight log
  5. Thresholds and false alarms (Rice's formula, pulse counting, why passive-IR false alarms are not Gaussian)
- **Mini-project:** *Chopped Thermopile Radiometer*.
- **Check Yourself:** 8 questions.
- **Numbers:** every quoted value was computed locally (computed in Python during the review): noise densities, NF/R_opt/T_min, ENBW for 1–4 poles and settling times, lock-in noise by simulation, Allan-deviation slopes and levels, Rice thresholds checked by Monte Carlo, radiometric powers and in-band fractions.
- **Avoiding overlap:** I designed the content to complement work already in the merged curriculum: physics §01/§02 (PIR optics and noise-budget models), §06 (PSD and Monte Carlo uncertainty), §08 (pyroelectric Landau theory, transistor thermometry), pcb/00 Practice 3–4 (high-impedance error and noise budgets), and pcb/12 (precision channel, guard and leakage tests).
- **Other files updated:**
  - `physics/README.md` learning path, with a note on Section 12's recommended position
  - `PROGRESS.md`: a new `## Section 12` block (3 resources + practice/mini-project/check lines); Dutta & Horn removed from §08; Keithley added to Books
  - §08's suggested order now ends with a "Next: Section 12" pointer
  - `books/README.md`: Keithley handbook row and reading-order line

The original proposal follows for reference.

- **Position:** Add as **Section 12** (appended, so no existing folder is renumbered; pcb/06 already links to `physics/03-electromagnetism/`). The README learning path should say "take after 08 (needs 02, 03, 04/08)". For an engineer's core path it belongs right after 08, before 05/07/11.
- **Why:** Aaron designs sensor and precision-measurement hardware. The physics that limits his products (noise floors, drift, uncertainty, transducer physics, thermal-IR radiometry, optics) is scattered or absent. Currently it appears only in the pieces I added to 02/05/08/09, and in no other curriculum (grep found no GUM, error-analysis, Johnson-noise, radiometry, sensor or device-physics coverage anywhere in the repo; pcb covers EMC, not measurement physics). A dedicated section would turn this from a generic physics-major track into his professional backbone.
- **Outline:**
  1. Units and constants: the 2019 SI redefinition (fixed h, e, k, N_A), traceability and calibration.
  2. Measurement uncertainty: Type A/B evaluation, propagation, coverage factors, the GUM.
  3. Noise physics: thermal (Johnson–Nyquist), shot, 1/f, noise spectral density, noise temperature and figure; the fluctuation–dissipation theorem; a unified MOS/resistor white-noise picture.
  4. Signal recovery: averaging, lock-in/synchronous detection, chopper stabilization, correlated double sampling.
  5. Low-level DC measurement physics: leakage and guarding, thermoelectric EMFs, triboelectric and piezoelectric artefacts, Kelvin sensing.
  6. Transducer physics: resistive/strain, capacitive, inductive/Hall, piezoelectric, pyroelectric, thermoelectric (thermocouple/thermopile), photodiodes.
  7. Thermal radiation and IR sensing: Planck/emissivity, radiometry (radiance, étendue), pyroelectric detectors and microbolometers, Fresnel-lens arrays and fields of view.
  8. Quantum limits and quantum sensing: shot-noise and standard quantum limits, SQUIDs, NV-center and atomic magnetometers, atomic clocks.
- **Verified resources (fetched this session):**
  1. J. B. Johnson — "Thermal Agitation of Electricity in Conductors", *Phys. Rev.* 32, 97 (1928) — https://doi.org/10.1103/PhysRev.32.97 *(added to §02)*
  2. H. Nyquist — "Thermal Agitation of Electric Charge in Conductors", *Phys. Rev.* 32, 110 (1928) — https://doi.org/10.1103/PhysRev.32.110 *(added to §02)*
  3. R. Sarpeshkar, T. Delbrück & C. A. Mead — "White Noise in MOS Transistors and Resistors", *IEEE Circuits & Devices Mag.* 9(6), 23–29 (1993) — https://doi.org/10.1109/101.261888 *(new; shot and thermal noise unified, ideal for an analog designer)*
  4. P. Dutta & P. M. Horn — "Low-Frequency Fluctuations in Solids: 1/f Noise", *Rev. Mod. Phys.* 53, 497 (1981) — https://doi.org/10.1103/RevModPhys.53.497 *(added to §08)*
  5. J. H. Lienhard IV & V — *A Heat Transfer Textbook*, 6th ed. (2024), free; its thermal-radiation chapters cover emissivity, view factors and radiative exchange — https://ahtt.mit.edu/ *(added to §09)*
  6. LIGO Scientific & Virgo Collaborations — "Observation of Gravitational Waves from a Binary Black Hole Merger", *PRL* 116, 061102 (2016), a case study in noise budgets at 10⁻²¹ strain — https://doi.org/10.1103/PhysRevLett.116.061102 *(added to §05)*
  7. N. Ashby — "Relativity in the Global Positioning System", *Living Rev. Relativ.* 6, 1 (2003), on time and frequency metrology — https://doi.org/10.12942/lrr-2003-1 *(added to §05)*
  8. C. Hu — *Modern Semiconductor Devices for Integrated Circuits* (2010), with pn-junction/photodiode and MOS physics; chapters free — https://www.chu.berkeley.edu/modern-semiconductor-devices-for-integrated-circuits-chenming-calvin-hu-2010/ *(added to §08)*
- **Canonical items to add after verification.** These are still NOT in the repo; the web-lookup budget for this review was exhausted. Except for the Keithley handbook (now added, verified by the pcb reviewer), add them once each is fetched and confirmed:
  - John R. Taylor, *An Introduction to Error Analysis* (2nd ed., 1997)
  - JCGM 100:2008 *GUM* (free, BIPM)
  - NIST Technical Note 1297
  - BIPM *SI Brochure* (9th ed., 2019)
  - ~~Keithley/Tektronix *Low Level Measurements Handbook* (7th ed., free)~~ (added; verified by the pcb reviewer at https://download.tek.com/document/LowLevelHandbook_7Ed.pdf)
  - Jacob Fraden, *Handbook of Modern Sensors* (Springer, 5th ed. 2016)
  - Degen, Reinhard & Cappellaro, "Quantum sensing", *RMP* 89, 035002 (2017), arXiv 1611.02427
  - R. W. Whatmore, "Pyroelectric devices and materials", *Rep. Prog. Phys.* (1986)
  - Palmer & Grant, *The Art of Radiometry* (SPIE, 2009)
  - SRS application note "About Lock-In Amplifiers"
  - Moore, Davis & Coplan, *Building Scientific Apparatus* (4th ed., Cambridge 2009)
  - For optics: Saleh & Teich, *Fundamentals of Photonics* (3rd ed.); MIT OCW 2.71 *Optics*; CU Boulder *Optical Engineering* specialization (Coursera)

## Cut candidates
- **§07 #3 IBM Quantum Learning:** now redundant with #1 (the Watrous course lives on the same platform). Merge into one row.
- **§07 #6 3Blue1Brown "Some light quantum mechanics":** duplicate of §04 #5.
- **§08 #4 MIT 8.231 (2006):** problem sets only, no lectures or notes. It is superseded by Simon's lecture videos (added).
- **§06 #2 Giordano & Nakanishi, #5 Thijssen, #6 Landau/Páez/Bordeianu:** three overlapping general comp-phys texts beside the 🔑 Newman. Keep Newman plus at most one (Thijssen for quantum methods).
- **§09 #4 MIT 18.085:** duplicate of §06 #4. Keep it as a cross-reference only.
- **§11 #10 Brunton & Kutz:** duplicate of §09 #7. It is fine as a pointer but double-tracked in PROGRESS, so I did not add it to §11 PROGRESS.
- **§11 #11–12 Wolfram NKS / Physics Project:** speculative and non-mainstream. They are now honestly framed as optional; they could move entirely to philosophy/03, where the same material already lives.
- **§04 #7 Sakurai / #8 Cohen-Tannoudji, §05 #7 MTW:** graduate references. Keep, but mark "reference only".
- **§10 #8 Peitgen, Jürgens & Saupe:** a ~900-page fractals book that is low priority for this learner.
- **blogs #6 n-Category Café, #8 Brilliant.org:** off-path and paid respectively.

## Structural observations
- **No agent skill:** physics has no `.agents/skills/update-curriculum/SKILL.md`, although the top-level README says every curriculum has one.
- **Table schema differs from other curricula:** physics tables are `# | Resource | Type | Marking | Link`, with no Year, Author or Description columns (pcb/ml/math have them). Descriptions live only in "Suggested Order", and editions and years are buried in titles. Harmonising would help NotebookLM and future agents.
- **Many book rows had no link ("—"):** I added free/official links where verified (*Spacetime Physics*, Carroll notes, Hu, Ellingson, Haus & Melcher, Lienhard, FEniCSx). Taylor, Schroeder, Griffiths, Kittel, Simon and Kundu still have none.
- **Sequencing:**
  - Computation (06) should start alongside 00.
  - Optics (in 01) depends on E&M (03); split "Waves" before 03 and "Optics" after, or move 01 after 03.
  - Relativity (05) and quantum computing (07) are optional detours for Aaron; condensed matter/devices (08) and the proposed measurement section are core.
- **README tracks:** I suggest adding two named tracks to README:
  - *Engineer's core:* 00 → 02 → 03 → 04 → 08 → [new 12] → 01 (optics) → 09 (heat transfer), with 06 running in parallel.
  - *AI-for-science:* 06 → 10 → 11 (with ml/13).
- **PROGRESS double-tracking:** the "Books/Courses (supplementary)" lists repeat section items. Convert them to pointers or remove them.
- **Cross-curriculum overlaps:**
  - *physics/11 ↔ ml/13:* both list Satorras EGNN (2021) and AlphaFold 2 (Jumper 2021); ml/13 also has GraphCast, GNoME, AF3 and the Bronstein GDL book. Suggested split: ml/13 owns architectures (GNNs, equivariance) and AI-for-science applications; physics/11 owns physics-structured ML (PINNs, HNN/LNN, neural operators, GNS/MP-PDE, hybrid physics–ML models such as NeuralGCM). The neural operators I added are not in ml/13. Cross-link rather than duplicate.
  - *physics/03 ↔ pcb/06–07:* no duplicated resources. During this run the pcb agent added a link from pcb/06 to `physics/03-electromagnetism/README.md`, so keep that folder name stable. The Ellingson open textbook added to physics/03 is the natural prerequisite link from pcb/06 (transmission lines, microstrip, skin depth).
  - *physics/10 ↔ math/07:* the same Strogatz book and the same Cornell playlist (`PLbN57C5…`) are in both, and Neural ODE (Chen 2018) is in math/07 and physics/11. Track each once; let math/07 own ODE theory and physics/10 own chaos.
  - *Wolfram material:* also in **math/11** (NKS + Physics Project, described with the "ruliad" and no caveat) and **philosophy/03** (NKS Ch. 12 + ruliad). Their agents should apply the same honest framing.
  - *Top-level README* (not edited): the physics "Key resources" still says "Qiskit"; consider updating to "IBM Quantum Learning".
- **Verification gaps (budget):**
  - The shared WebSearch budget ran out early, and WebFetch was rate-limited (HTTP 429) or exhausted (HTTP 403) for long stretches.
  - Pages that could not be read: api.crossref.org for 10.1007/978-3-319-52462-7 and 10.21061/electromagnetics-vol-1 (both verified by other routes); the Wiley *Fundamentals of Photonics* page; arXiv 2407.07218 and 2311.07222; nature.com NeuralGCM; ocw.mit.edu 2.71; bipm.org JCGM page; uscibooks.com Taylor; link.springer.com Fraden; nist.gov TN 1297; the Stanford Online Miller course; crossref for Sze & Ng.
  - None of these were added.

## Top 5 priorities for Aaron in this curriculum
1. **Work through the new Section 12 (Measurement, Noise, and Sensor Physics) right after Section 08.** It is the physics of his job: noise floors, signal recovery, drift/Allan deviation, detection thresholds, and thermal-IR radiometry. Complete it with Taylor's *Error Analysis*, the GUM, Fraden and a radiometry text once they are verified.
2. **Do the "engineer's bridge" items first:**
   - Johnson–Nyquist (§02)
   - Ellingson and Haus & Melcher (§03)
   - Miller (§04)
   - Hu and Dutta & Horn (§08)
   - Lienhard (§09)

   These convert textbook physics into board-level intuition and are all free.
3. **Re-sequence for an engineer:** run Python/computation (§06 Kinder & Nelson → Newman → FEniCSx) alongside §00, take optics after E&M, and treat relativity and quantum computing as optional detours.
4. **Read §11 critically:** go PINNs → neural operators (FNO/DeepONet) → reality checks (add McGreivy & Hakim 2024 after verification). Treat Wolfram as optional, with the Aaronson review alongside.
5. **Clean up the tracker:** make PROGRESS the single source of truth by removing the duplicated "supplementary" lists, and track the cross-curriculum duplicates once (Strogatz, Neural ODE, AlphaFold, EGNN).
