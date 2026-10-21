# Independent Check: October 2026

After the review edits were made, five checkers who had not written any of them re-read every changed file. They ran without web access. They checked formatting, internal consistency, factual red flags, the quality and safety of the practice exercises, and tone. They also recomputed several hundred of the "you should get X" values in Python (and C, where needed). Their findings follow unedited, except for path cleanup.

**Totals:** about 82 issues fixed directly by the checkers (no high-severity issue was left in place) and about 66 flagged.

**Flagged items resolved after the check:**
- bio/09: an infeasible electrode noise budget. The site is now ~150 kΩ, and the 1 MΩ case is posed as the counter-example.
- philosophy/06: COMPAS row-set wording.
- bio/10: the AlphaFold 3 licence. It is non-commercial, not Apache-2.0.
- ml/02: the RBF-SVM runtime, now with subsampling.
- ml/12: the METR paper's title. Re-checked on arXiv on 2026-10-13: v1 and the current version are both titled "…Complete Long *Software* Tasks", so the row now uses that title.
- ml/09: the nanochat speedrun claim, now hedged.
- pcb/05: the FastHenry cross-check, now optional.
- btc/02: the CVE-2012-2459 pointer.
- pcb/02: KiCad design blocks (9.0, not 10.0).
- software/01: pyright strict mode.
- software/04: the Richards & Ford "laws" wording.
- software/09: the AGENTS.md / CLAUDE.md claim.
- ml/08: authors for Mixtral (Jiang et al.) and the Ultra-Scale Playbook (Tazi et al.).
- ml/00: *The Bitter Lesson* framing.
- ml/06: the label-smoothing ablation and the KV-cache cross-reference.
- The update skills now include the one-home-per-topic rule and a defined ⭐ list for btc, and the 🔑 guidance is softened.

**Still open:** of the 73 rows flagged at the time, 69 were resolved on 2026-10-13 (most in the follow-up pass; see each curriculum's review addendum) and 4 remain open, marked **still open** below. A second independent check of the follow-up pass itself is at the end of this file.

---

## V1 — Independent check of `ml/` (baseline a8b86e9 → HEAD 8d90657)

Scope: `git diff a8b86e9 HEAD -- ml/`, then a full read of every section README plus `ml/README.md`, `PROGRESS.md`, `books/`, `courses/`, `blogs-and-references/` and `.agents/skills/update-curriculum/SKILL.md`. `python3 tools/check_repo.py` reports 0 problems in `ml/`, both before and after my edits. Its only remaining problem is outside my scope: `README.md:2` links to a missing `assets/banner.jpg`.

Recomputed with Python: π-digit compressibility, ESL's "wrong way" CV, Bayes base rate (19.9%), Mixtral total/active parameters (46.7B/12.9B), a 784-512-512-10 MLP (669,706 params ≈ 654 KiB in int8), GPT-3 compute (3.15e23 FLOPs ≈ 29k A100-days at 40%), the Chinchilla optimum for 1e21 FLOPs (2.9B params / 58B tokens), GPipe bubble fractions, the Novikoff bound, and the n ≈ 2d attention crossover. All the other stated values check out: VGG 27C² vs 49C², a 31×31 dilated receptive field, the 227-pixel AlexNet input, GCN 81.5% and GAT 83.0%, nanoGPT 1.4697, the GPT-2 TL;DR finding, and GraphCast's 90% of 1,380 targets. I checked the 27-item Ilya list and its ⭐ mapping (28 PROGRESS entries = 27 unique, with Grünwald listed twice) and found it correct. I found no mention of an employer, product or customer, and no investment advice.

| File:line | Severity | Issue | Action |
|---|---|---|---|
| ml/01-math-foundations/README.md:74 | med | Practice 5(b) told the learner to "explain why π barely compresses". In fact, ASCII decimal digits compress to about 43–47% (1 MB of random digits: gzip 0.47, bz2 0.43, lzma 0.44; the floor is log₂10/8 = 0.415). What doesn't happen is compression below the rate for random digits. As written, the learner would hit a contradiction. | fixed (now: "compress no better than random decimal digits (~3.3 bits/digit, ~42–47%)") |
| ml/02-classical-ml/README.md:61 | med | Practice 3 has the learner reproduce ESL's "wrong way to do cross-validation" on the suggested datasets (27–54 features). The Done-when ("well-above-chance accuracy on pure noise") can't be met there. Simulated: ESL's p≫n setup (50×5,000, top-100 features, 1-NN) gives 100% wrong-way vs ~56% right-way accuracy, while a 1,941×27, 7-class noise set gives 14–15% (chance is 14%). | fixed (specified ESL's 50 × 5,000 noise setup, 1-NN, selection inside vs outside folds) |
| ml/05-rnns-sequences-and-memory/README.md:63 | med | Practice 2 asks for a GRU built "from Cho et al.'s equations" to match `nn.GRUCell` to 1e-6. PyTorch (like cuDNN) applies the reset gate after the recurrent matmul, r ⊙ (W_hn h + b_hn), while Cho et al. use U(r ⊙ h), so the outputs can't match as written. | fixed (added the caveat: match PyTorch's form, then try Cho's) |
| ml/10-reinforcement-learning/README.md:41 | med | The intro said process supervision *and* RLVR "are the recipe behind reasoning models such as DeepSeek-R1". R1 used rule-based outcome rewards only, and its report lists process reward models under "Unsuccessful Attempts". The sentence also contradicted Section 11 (lines 13, 132). | fixed (RLVR/GRPO is the recipe; PRMs are the alternative R1 reported as unsuccessful) |
| ml/11-frontiers/README.md:28 | low | Same claim as above: "the RL recipes behind it — process rewards, GRPO, RLVR". | fixed (PRMs described as the alternative R1 did not adopt) |
| ml/07-generative-models/README.md:16 | low | The objective implied that DALL·E 2 and Imagen combine *latent diffusion* with text encoders. Both are pixel-space diffusion cascades: unCLIP's prior over CLIP embeddings, and Imagen's frozen T5. | fixed (objective reworded) |
| ml/08-scaling-and-training/README.md:71 | low | The exercise asks for step-for-step equality between AdamW "per Loshchilov & Hutter" and `torch.optim.AdamW`. PyTorch scales the decoupled decay by lr (θ ← θ − lr·λ·θ), while the paper's Algorithm 2 scales it by η_t only, so the same λ won't match. | fixed (added a mapping note) |
| ml/README.md:63 | low | The Ilya-list row credited "Rush et al.". The 2018 Annotated Transformer (NLP-OSS 2018) is by Alexander Rush alone; the 2022 refresh is Huang et al. Section 06 already says "Harvard NLP (Rush)". | fixed ("Rush, Harvard NLP") |
| ml/02-classical-ml/README.md:65 | low | The mini-project suggests capturing a "current-sense trace (normal vs. faulty load)" with no safety note. Such loads are often mains-powered or high-current. | fixed (added: use a low-voltage, current-limited bench supply, not a mains load) |
| ml/11-frontiers/README.md:41 | low | The edited paragraph kept "Gemini represents the natively multimodal frontier" for the 2023 Gemini 1.0 report, which is dated by Oct 2026. | fixed ("represented … at its 2023 release") |
| ml/02-classical-ml/README.md:61 | med | Time estimate: the 50k-row covtype option with RBF-SVM under nested 5×5 CV means ~225 SVC fits on ~40k rows. That is many CPU-hours (roughly 7–30+ h), far beyond "~4 h". Suggest subsampling to ~5–10k rows for the SVM, or defaulting to Steel Plates. | flagged → **resolved 2026-10-13**: RBF-SVM now subsampled to ~10k rows, with the runtime reason given |
| ml/12-interpretability-and-alignment/README.md:69 (+ PROGRESS.md:275) | low | The METR row title is "Measuring AI Ability to Complete Long *Software* Tasks". I recall the arXiv 2503.14499 title as "Measuring AI Ability to Complete Long Tasks". I'm fairly confident but can't verify without web access. | flagged → **resolved 2026-10-13**: arXiv v1 and v4 both read "Long *Software* Tasks"; title matches arXiv |
| ml/12-interpretability-and-alignment/README.md:101 | low | Practice 1's Done-when expects the D* = m/‖W‖²_F plateau at 1/2. The paper's sticky dimensionality points come from its uniform-importance experiments; with n=20, m=5 and geometrically decaying importance the plateau may not show cleanly. Suggest uniform importance (and a larger n) for the D* sweep. | flagged → **resolved 2026-10-13**: Practice 1 adds a uniform-importance dimensionality sweep; 4 → 5 h |
| ml/06-transformers-and-attention/README.md:63 | low | Practice 3 ablates "no label smoothing" on the Annotated Transformer copy task. As I recall, that example already uses `smoothing=0.0`, which would make this ablation a no-op. Consider "add label smoothing 0.1" instead, or move it to the translation example. | flagged → **resolved 2026-10-13**: ablation reversed: add smoothing 0.1 to the smoothing-free copy task |
| ml/06-transformers-and-attention/README.md:67 | low | The mini-project requires a KV cache and a speedup measurement, but no Section 06 resource covers KV caching. PagedAttention/vLLM in Section 08 does, and isn't cross-referenced. | flagged → **resolved 2026-10-13**: mini-project now points to Section 08's PagedAttention/vLLM row |
| ml/08-scaling-and-training/README.md:76 | low | The mini-project's "~15 h incl. GPU" looks optimistic. If the family tops out at the 50M model's Chinchilla budget, the final "10× budget" run alone is ~3e18–6e18 FLOPs, i.e. ~7–13 A100-hours at 40% MFU (≈30 h on a T4). Cap the largest family run (≤1e17 FLOPs) or raise the estimate. | flagged → **resolved 2026-10-13**: family shrunk to ≈1M–20M parameters; estimate raised to ~20 h |
| ml/08-scaling-and-training/README.md:42, :34 | low | The Ultra-Scale Playbook is credited to "Hugging Face" although it has named authors (Tazi et al.). The pre-existing "Mixtral of Experts – Mistral AI" should be Jiang et al. Both conflict with the new SKILL rule "cite people, not organizations". | flagged → **resolved 2026-10-13**: rows now credit Tazi et al. and Jiang et al. |
| ml/09-llms-and-language/README.md:69 | low | The text says nanochat has a "~2-hour speedrun" on 8×H100, but the launch README (Oct 2025) said ~4 h / ~$100. It may have been updated since, so check the current README. Also, "Let's reproduce GPT-2" covers pretraining only, so it doesn't walk through "the same stages" (SFT/RL). | flagged → **resolved 2026-10-13**: speedrun hedged to "few-hour"; GPT-2 video marked as pretraining only |
| ml/01-math-foundations/README.md:51 | low | The Legg thesis links to a third-party mirror (pdf.stafforini.com) rather than the author's own copy (vetta.org). | flagged → **still open**: author's own copy unreachable; the verified stafforini mirror stays |
| ml/02-classical-ml/README.md:36 | low | "Boosted trees are still the default winner on tabular data" is broadly fair. However, tabular foundation models (e.g. TabPFN, 2025) now compete on small datasets; consider softening. | flagged → **resolved 2026-10-13**: XGBoost wording softened; TabPFN (Nature 2025) row added |
| ml/00-historical-foundations/README.md:32 | low | The Bitter Lesson is described as "the lens through which most of modern AI's trajectory makes sense". That presents an influential but contested thesis as settled; consider "a widely cited (and debated) lens". | flagged → **resolved 2026-10-13**: now "a widely cited, and debated, lens" on modern AI |
| ml/04-cnns-and-computer-vision/README.md:54 | low | ConvNeXt, a CNN, sits in the "Vision Transformers" table. That's defensible as the post-ViT counterpoint, but a reader scanning the tables may be misled. | flagged → **resolved 2026-10-13**: table renamed "Vision Transformers (and the CNN response)", with a note |
| ml/11-frontiers/README.md:1 | low | Section 11 still has no Prerequisites and no Suggested Order (pre-existing, marked ✱ in the review). The new SKILL rule 5 lists both as required anatomy. | flagged → **resolved 2026-10-13**: Prerequisites and a Suggested Order covering every row added |
| ml/*/README.md (🔑 column) | low | The new SKILL rule 6 caps 🔑 at "~3 core items per section", but 12 of 14 sections exceed it (08: 8, 11: 11, 12: 8). This pass's own additions also pushed 00 from 3 to 4 (Bitter Lesson) and 03 from 5 to 6 (Prince). Either prune the markers or relax the rule. | flagged → **resolved 2026-10-13**: 🔑 trimmed to ≤3 in every ml section; Core path lines added |
| ml/PROGRESS.md:21–191, :300 | low | PROGRESS still omits some table rows, all pre-existing: Khan Academy and StatQuest (01), scikit-learn User Guide and Google MLCC (02), Distill.pub (07), Anthropic Research Blog (09). The Books block omits PRML, ESL, GPML and the RLHF Book, which are tracked in Sections 02/10. These look like deliberate "reference, not checkable" omissions, but they contradict SKILL rule 5. | flagged → **resolved 2026-10-13**: four rows and a Books note added; Distill, Anthropic omitted deliberately |

### Overall judgment — ml/

The ml/ pass is high quality. The citation repairs hold up against my own knowledge: the 27-item Ilya list and its ⭐ placement across sections and PROGRESS, Section 12's authors and arXiv IDs, Shen/Uspensky/Vereshchagin, Faisal, and the GNoME/GraphCast wording. Every resource I could check on added or edited lines (63 arXiv IDs, plus books, courses and YouTube IDs) is real and correctly attributed, apart from the flagged METR title. Tables, numbering, Suggested Orders and the PROGRESS practice lines are internally consistent, and the checker is clean. The practice layer is the strongest part: the exercises are concrete, numerically checkable and tied to named sources, and the stated reference values I recomputed were right. The defects were the kind a fast expert author makes. Four exercises had a technical trap that would block the Done-when (the π compressibility claim, ESL leakage on low-dimensional data, PyTorch's GRU variant, AdamW's λ scaling). There was one factual error about DeepSeek-R1's recipe that also contradicted Section 11. A few mini-project time estimates are optimistic. The remaining flags are minor: unverifiable recency details, 🔑 inflation against the repo's own new rule, and Section 11's missing Suggested Order.

---

## V2 — Independent check: `math/` and `physics/`

Scope: `git diff a8b86e9 HEAD -- math/ physics/` plus full reads of all 15 math and 13 physics section READMEs, both PROGRESS files, both READMEs, and the books, courses and blogs pages. `tools/check_repo.py` passes for both curricula; its only problem is `README.md:2 assets/banner.jpg`, which is outside this scope.

I recomputed about 200 "you should get X" values in Python/NumPy/SciPy and C. Scripts are in the checker's scratch scripts.

**Values confirmed correct:**
- **math/00–09:**
  - isqrt: exhaustive over all 2³² inputs in C, 0 failures in 266 s; the 32-bit variant has exactly one failing input, n = 2³²−1.
  - Thermistor κ ≈ 10²⁷–10²⁸ raw and ≈ 247 scaled; model error 0.016 °C; QR and normal equations ≈ 0.023 °C while `lstsq` is off by degrees.
  - Gibbs 1.179. Taylor degree 9 vs 7. Chebyshev degree-7 error 1.2×10⁻⁶.
  - Bootstrap-percentile coverage 0.930 vs exact 0.951. Threshold 5.17σ.
  - remez 101 taps at −85.2 dB. Hamming(7,4) p_b = 0.0669. AWGN capacity 3.46 Mb/s.
  - Cube R_eff 7/12, 3/4, 5/6 Ω; Foster sum 7; 384 spanning trees by brute force.
  - D₄ subgroups 10, of which 6 normal. CRC-8 check 0xF4; minimum undetected weight 4. Burnside counts 6, 36, 30, 102. Order of x: 255 in 0x11D, 51 in 0x11B.
  - Topologies 29 (9 classes) and 355 (33 classes).
- **math/12:** windows table; Butterworth 76.3/95.4 dB; filter orders 21, 10, 7; kaiserord 89; remez meets spec at 68 taps; pre-warp 9.69/10.34 kHz; matched-filter losses 0.91 and 0.89 dB; ROC 17.0 dB; SINAD 74.0 → 68.1.
- **math/13:** all values, including the 561 strong liars, the 16 Carmichael numbers, 2G and 3G, BIP-340 test vector 0 reproduced exactly, the p = 127 anomalous curve, and the three toy curves' prime orders.
- **math/14:** most values (float32 counter 991.14; Σ0.1 = 1,087,937; Hilbert; Runge 59.8/0.0153; trapezoid; fast inverse square root 3.44%/0.175%/4.6×10⁻⁶; RC/LC companion-model errors).
- **Physics:** nearly every value — Einstein solid, Planck band fractions, MEMS 74 µg/√Hz, microstrip 53.3 Ω/3.24, κ = 1.02 Å⁻¹, GPS +38.5 µs/day, Mercury 43″, copper Drude numbers, Ra/Nu, van der Pol T/μ, all physics/12 noise, lock-in and Rice numbers, and radiometer powers.

| File:line | Severity | Issue | Action |
|---|---|---|---|
| math/07-differential-equations/README.md:63 | high | The RLC values were inconsistent. L = 10 mH, C = 100 nF gives ω_n = 3.16×10⁴ rad/s, not 10⁴, so forward Euler would diverge at the stated 50 kS/s (its limit becomes 79 kS/s) and the 25 kS/s and 20 kS/s claims fail. | fixed: C = 1 µF and R = 40/200/600 Ω, which keep ω_n = 10⁴ and all the stated rates |
| physics/01-waves-and-optics/README.md:54 | high | The laser-pointer diffraction exercise had no safety caveat. | fixed: added a Class 2 (< 1 mW) / never-look-into-beam / keep-reflections-below-eye-level note |
| physics/04-quantum-mechanics/README.md:58 | high | The laser-pointer polarizer exercise had no safety caveat. It also said LCDs are "partially" polarized; LCDs are strongly polarized, and laser pointers usually are too. | fixed: safety note added; polarization caution corrected |
| math/README.md:54 (+ :43, 12/README:14) | med | The Core route ran 07 → **12 → 03**, but Section 12 lists 03 as a prerequisite for its random-signals half. STUDY-GUIDE (as now edited) gives 07 → 03 → 12. | fixed: route is now 00→01→02→07→03→12→14→04→05; the "take after" notes for Section 12 now say "after 07 and 03" |
| math/12-fourier-analysis-signals-and-systems/README.md:127 | med | Said "total noise power triples to LSB²/3". Going from LSB²/12 to LSB²/3 is ×4, which is what gives the stated 6.02 dB. | fixed: "quadruples" |
| physics/02-thermodynamics-and-statistical-mechanics/README.md:57 | med | The TIA has R_f = 1 MΩ, but photocurrents go "to 10 µA", which needs 10 V of output and clips on a battery supply. There was also no battery caveat. | fixed: range is now "up to a few µA" with the output-swing reason; added an alkaline / no-short / no-unprotected-Li note |
| physics/09-fluid-dynamics-and-continuum/README.md:59 | med | The exit kinetic-energy correction was given as "≈ 3–4% of ΔP", which is ½ρv̄² (plug flow). A developed parabolic profile carries ρv̄² (α = 2), which recomputes to ≈ 6–7%. | fixed |
| math/14-numerical-methods-and-scientific-computing/README.md:99 | med | Wilkinson exercise: x was unspecified, and part (a) uses x = (1,…,1). With that x, GEPP is exact through n = 54 (all-integer arithmetic), so the learner sees zero error. The typical error at n = 40 is ~10⁻⁶, not ~10⁻⁵. | fixed: specify a random x with the reason; n = 40 error now ~10⁻⁶ |
| math/14-numerical-methods-and-scientific-computing/README.md:91 | low | The central-difference optimum is h ≈ ε^(1/3) ≈ 10⁻⁵, not 10⁻⁶: the error is 5.9×10⁻¹¹ at 10⁻⁵ vs 1.6×10⁻¹⁰ at 10⁻⁶. | fixed |
| math/14-numerical-methods-and-scientific-computing/README.md:122–123 | low | The nfev counts are version-dependent: SciPy 1.18 gives BDF 200 and Radau 237, not 440 and 290. The RK45 stability step is ≈ 3/1000; 2/1000 is forward Euler's limit. | fixed: hedged the counts; h ≲ 3/1000 for RK45 (2/1000 for forward Euler) |
| math/14-numerical-methods-and-scientific-computing/README.md:85 | low | "True variance ≈ 2.25" holds only for unrounded samples. Integer ADC codes give ≈ 2.33 (Sheppard +1/12). | fixed: clarifying parenthetical |
| math/12-fourier-analysis-signals-and-systems/README.md:104 | low | The elliptic filter's group delay is ≈ 42 samples at the 4 kHz passband edge, but the true peak is ≈ 51 at 4.1 kHz. A full-band plot would contradict "peaks … ≈ 42". | fixed: gives all three numbers |
| math/11-category-theory-and-frontiers/README.md:41 | low | "Produced no quantitative, testable predictions" is an overclaim, and stronger than physics/11's wording for the same project. | fixed: aligned to physics/11 ("no experimentally confirmed prediction that distinguishes it…") |
| physics/02-thermodynamics-and-statistical-mechanics/README.md:55 | low | Wien peak at 310 K is 9.35 µm, not "≈ 9.4". | fixed |
| physics/08-condensed-matter-and-materials/README.md:62 | low | "6–8 temperatures between ~0 and 80 °C" cannot be reached with only a resistive heater block. | fixed: "from ambient", plus an optional ice-bath point |
| physics/12-measurement-noise-and-sensor-physics/README.md:100 | low | The battery-powered build had no battery caveat. | fixed |
| math/10-causal-inference/README.md:62 | low | The hot-air gun in the optional hardware step had no caution. | fixed: low setting, keep moving, keep distance |
| math/04-optimization/README.md:61 | low | Cites 18.065 lectures, which are not in Section 04 and the section wasn't named. | fixed: added "Section 01" |
| math/06-graph-theory-and-combinatorics/README.md:58, 59 | low | Cites 18.06 Lecture 12 and 18.065 Lecture 35 (both Section 01) without naming the section. | fixed |
| math/07-differential-equations/README.md:63 | low | Cites 18.06 Lecture 23 (Section 01) without naming the section. | fixed |
| math/08-abstract-algebra/README.md:60 | low | Cites Velleman Ch. 7 (Section 00) without naming the section. | fixed |
| physics/00-classical-mechanics/README.md:53 | low | Cites Feynman Vol. 2 Ch. 19, but the section lists only Vol. 1. | fixed: "(Vol. 2 is listed in Section 03)" |
| math/00-mathematical-thinking/README.md:58 | low | Exercise 5 depends on Velleman's *How To Prove It with Lean*, which is not in the table. It is a real free companion and optional, but adding it needs a verified link. | flagged → **resolved 2026-10-13**: added as a resource row, Suggested Order step and PROGRESS line |
| math/08-abstract-algebra/README.md:58 | low | Exercise 1 cites "Group Explorer" (software), which is not listed. | flagged → **resolved 2026-10-13**: Group Explorer 3 added: tool row, order step, PROGRESS line |
| math/04-optimization/README.md:40 | low | Kochenderfer & Wheeler: "a 2nd edition is due in 2027" is an unverifiable forward-looking claim that will age badly. | flagged → **resolved 2026-10-13**: book site lists 5 January 2027; kept as a dated fact |
| math/05-information-theory/README.md:38 | low | Calling Polyanskiy & Wu "the up-to-date successor to Cover & Thomas" overclaims; it is a graduate-level alternative, not a replacement. | flagged → **resolved 2026-10-13**: now "a graduate-level alternative to Cover & Thomas, not a replacement" |
| physics/07-quantum-computing/README.md:46 | low | "Qiskit Textbook repo archived in January 2024": I could not verify the specific date offline. | flagged → **resolved 2026-10-13**: GitHub banner confirms archive date (18 Jan 2024); text unchanged |
| physics/10-nonlinear-dynamics-and-chaos/README.md:41 | low | "3rd edition (2024) adds a chapter on the Kuramoto model": not verified. | flagged → **resolved 2026-10-13**: publisher TOC confirms new Chapter 13 (Kuramoto); text now names it |
| physics/05-special-and-general-relativity/README.md:42 (+ books row 10) | low | Spacetime Physics "CC BY 4.0": the free download is real, but I could not confirm the licence. | flagged → **resolved 2026-10-13**: book site confirms CC BY 4.0; no change needed |
| physics/03-electromagnetism/README.md:42 | low | "MIT OCW has no other video version of 8.02" is a hard-to-verify negative claim. | flagged → **resolved 2026-10-13**: narrowed to the checked fact: OCW's 2007 8.02 has no videos |
| physics/09-fluid-dynamics-and-continuum/README.md:35 | low | Lienhard *A Heat Transfer Textbook* "6th ed., 2024" (also in PROGRESS and books): edition and year not verified. | flagged → **resolved 2026-10-13**: 6th ed. (2024) confirmed; authors now listed as Lienhard V & IV |
| physics/12-measurement-noise-and-sensor-physics/README.md:34–35 | low | The Allan-deviation and Rice-formula objectives have no supporting resource among the section's three, though the exercises define both methods. Worth adding a reference (e.g. NIST SP 1065 for Allan) once someone can fetch and check it. | flagged → **resolved 2026-10-13**: added Riley (NIST SP 1065) and Rice, used in Practice 4–5 |
| math/01 (exercise 1, mini-project) and others | low | Many specific lecture, problem-set and chapter numbers (e.g. "18.06 Problem Set 5 (§§4.1, 4.2, 8.2)", "Problem Set 10", Strogatz § numbers that may shift in the 3rd edition) cannot be checked offline. The ones I know (18.06 L10/12/15/16/23/26, 18.065 L7/9/22/23/30/31/35, Feynman chapter numbers, B&V Ex. 2.12/3.16/5.1, Shannon Thm 17) are correct. | flagged → **still open**: 18.06 problem sets confirmed; Axler, MacKay, Cover & Thomas chapters unchecked |

### Overall judgment

**math/:**
- Strong work overall. The new resources are well chosen and correctly attributed: the citation fixes I checked are right (Eccles 1997, Book of Proof 2018, Lawler not free, Macauley for the videos, S4 authors, Cruttwell first author, Mac Lane 1998).
- The exercises are concrete, engineering-flavored and rarely filler. The check values are unusually good: out of ~120 recomputed, one was a substantive arithmetic error (the RLC ω_n) and one a wording slip ("triples").
- The weak spots were structural (the Core route contradicted Section 12's prerequisite) and Section 14's precision claims, several of which depended on SciPy version or unstated choices.
- The Wolfram material is now appropriately caveated. Tone is measured throughout.

**physics/:**
- Also high quality. The new practice material ties physics to bench work and is numerically excellent: every noise, radiometry, relativity, tunneling and transport number I recomputed matched.
- The real gaps were safety: two laser-pointer exercises had no caveat, and the battery builds had no note. All of these are now fixed.
- Two physics errors are now fixed: the factor of 2 in the viscometer kinetic-energy term and a TIA current range that would clip.
- The Lewin removal note is factual and neutral. The Wolfram treatment in Section 11 is fair.
- What remains is a handful of unverifiable edition, licence and date details, flagged above.

---

## V3 — Independent check of `bio/`, `econ/`, `philosophy/`

Baseline `a8b86e9` → `HEAD`. No web access; every numeric "Check:" value below was
recomputed locally in Python where feasible. `tools/check_repo.py` reports only one
problem repo-wide (`README.md:2` → `assets/banner.jpg`), which is outside my scope.

### Findings

| File:line | Severity | Issue | Action |
|---|---|---|---|
| `bio/09-neuroscience/README.md:67` | high | Practice 6's front-end noise budget is internally infeasible. With the stated ~1 MΩ electrode and 300 Hz–6 kHz band, the electrode's own Johnson noise is √(4kTRΔf) ≈ **9.9 µV rms** at 310 K (131 nV/√Hz) — about twice the stated "target input-referred noise under 5 µV rms". A 5 µV rms budget over that band allows a source resistance of only ~256 kΩ, so the next sub-question ("the maximum tolerable amplifier input voltage noise density") has no answer. Two clean fixes: change the electrode to ~150 kΩ (Neuropixels-like — 3.8 µV rms, leaving ~3 µV for the amplifier, and consistent with the Jun et al. resource already in this section), **or** keep 1 MΩ and state that discovering the thermal floor above the target is the point. | flagged (fix is an authoring choice) → **resolved 2026-10-13**: site now ~150 kΩ; the 1 MΩ case is the counter-example |
| `philosophy/06-ethics-of-ai/README.md:62` | med | COMPAS check values look attributed to the wrong row set. FPR 44.85%/23.45% and FNR 27.99%/47.72% are ProPublica's published figures from their **filtered** set (6,172 rows after `days_b_screening_arrest` ∈ [−30,30], `is_recid != -1`, `c_charge_degree != 'O'`, `score_text != 'N/A'`), not from the raw 7,214-row file. The text says the opposite ("on the full 7,214-row file you should reproduce … applying ProPublica's standard row filters (6,172 rows) shifts each figure by up to ~2.5 points"). Cannot verify offline; a learner following this will hit a mismatch. The FPR = p/(1−p)·(1−PPV)/PPV·(1−FNR) identity in the same exercise **is** correct (derived and checked). | flagged → **resolved 2026-10-13**: recomputed: full-file figures were right; both row sets now stated |
| `bio/10-ai-for-biology/README.md:36` | med | "The AF3 inference pipeline released under **Apache-2.0** in November 2024" — Apache-2.0 was AlphaFold **2**. AF3's GitHub release (Nov 2024) is under a bespoke non-commercial source-code licence with weights under separate Google terms, which the row's own second clause implies. A reader could infer commercial-use rights that don't exist. Suggested wording: "released in November 2024 under a custom non-commercial licence, with model parameters obtainable from Google under separate terms." | flagged (≈85% confident; no web to confirm) → **resolved 2026-10-13**: now a non-commercial licence, contrasted with AlphaFold 2's Apache-2.0 |
| `philosophy/01-philosophy-of-mind/README.md:31`, `philosophy/books/README.md:8` | med | Kim's textbook was titled *Philosophy of Mind: A Contemporary Introduction*; that subtitle belongs to **John Heil's** Routledge book. Kim's is simply *Philosophy of Mind* (3rd ed., Westview). `philosophy/PROGRESS.md:200` already used the short title, so the repo was self-inconsistent. | **fixed** (→ "Philosophy of Mind (3rd Edition)" in both places) |
| `econ/03-decision-theory/README.md:40`, `econ/PROGRESS.md:58` | med | SEP "Decision Theory" credited to H. Orri Stefánsson alone; the entry is by **Katie Steele & H. Orri Stefánsson**. | **fixed** (first author restored in both) |
| `bio/PROGRESS.md` (Section 11 block) | med | A `---` rule sat between Section 11's resource list and its three practice checkboxes, orphaning them from the heading (every other section has them attached). `check_repo.py` missed it because its regex spans to the next `##`. | **fixed** (practice lines moved above the rule) |
| `econ/04-mechanism-design/README.md:34` | low | Resource titled "A Lovely but Lonely Vickrey Auction"; the actual chapter title is "**The** Lovely but Lonely Vickrey Auction", which Practice 4 in the same file already uses. | **fixed** |
| `econ/PROGRESS.md` §06, §08, §10, §11; `philosophy/PROGRESS.md` §11 | low | Five resources present in the section READMEs had no PROGRESS checkbox (Behavioral Scientist; Tim Roughgarden's page; Vitalik Buterin's blog; AI Alignment Forum ×2) while comparable blogs/feeds elsewhere (Marginal Revolution, Stratechery, LessWrong wiki) do have one. | **fixed** (five lines added) |
| `philosophy/10-eastern-philosophy-and-mind/README.md` / `philosophy/PROGRESS.md` §10 | low | *The Embodied Mind* is listed as a resource here but has no §10 checkbox. Probably deliberate — the row says "(revisited)" and §04 already tracks it — so left alone. | flagged → **resolved 2026-10-13**: confirmed deliberate; the row now says it's tracked under Section 04 |
| `bio/00:29`, `bio/01:32`, `bio/02:33,35`, `bio/03` | low | Items in the resource table (and in PROGRESS) that never appear in **Suggested Order**: MIT 7.016 (bio/00), MIT 7.05 (bio/01), Broad "A Brief Guide to Genomics" and the 2012 1000 Genomes paper (bio/02), the RCSB PDB database row (bio/03). All pre-existing in the baseline; adding them would be a content change, not a fix. | flagged → **resolved 2026-10-13**: all five items now appear in their sections' Suggested Order |
| `bio/11-frontiers/README.md:76` | low | Evo 2 cited as *Nature* 2026 with DOI `10.1038/s41586-026-10176-5`. The DOI's year segment is internally plausible for 2026 and Evo 2's parameter counts (7B/40B, ~9T bases) are right, but I cannot verify the journal, year or DOI offline. Same for `philosophy/07:43` ("International AI Safety Report 2026", second edition Feb 2026 — the 2025 first edition and arXiv:2501.17805 are correct). | flagged → **resolved 2026-10-13**: Crossref confirms the Evo 2 DOI; Safety Report 2026 confirmed; unchanged |
| `philosophy/02-consciousness/README.md:70`, `philosophy/11-frontiers/README.md:60` | low | PyPhi install details ("v2 … needs Python ≥ 3.13"; `.phi` vs `.big_phi`) are unusually specific and unverifiable offline; a wrong minimum version would block the exercise on day one. Worth one check against the PyPhi docs. The IIT substance is right (φ_s = 0 for feedforward and for the self-loops-only "camera"). | flagged → **resolved 2026-10-13**: PyPI and a test install confirm the details; no change needed |
| `econ/08-computational-economics/README.md:39` | low | "Homo Silicus" (NBER WP 31122) credited to "Horton, Filippas & Manning"; I believe WP 31122 is **single-authored by John J. Horton**. Worth confirming. | flagged → **resolved 2026-10-13**: NBER and arXiv list all three authors; year now "2023 (rev. 2026)" |
| `philosophy/04-intelligence-and-understanding/README.md:37,52` | low | SEP entry at `/entries/content-externalism/` is titled "Externalism About **Mental Content**", not "Externalism About the Mind"; the "§§5–7" section numbers are also unverifiable offline. The accompanying note (SEP has no standalone Extended Mind entry) is correct. | flagged → **resolved 2026-10-13**: SEP's title is "Externalism About the Mind"; repo was right, unchanged |
| `econ/blogs-and-references/README.md:14` | low | "Archive only since Sept 2024; Sumner now writes at The Pursuit of Happiness" — plausible but unverifiable offline; a dated status claim that will age. | flagged → **resolved 2026-10-13**: final post of 1 Sept 2024 confirmed; status wording now dated |
| `econ/10-monetary-economics-and-crypto/README.md:30,45`; `econ/PROGRESS.md:167` | low | Title given as "The Denationalization of Money"; Hayek's is *Denationalisation of Money — The Argument Refined* (British spelling, no leading article), which the row's own mises.org URL uses. Cosmetic; left alone to avoid churn. | flagged → **resolved 2026-10-13**: title corrected to *Denationalisation of Money: The Argument Refined* |
| `bio/10-ai-for-biology/README.md:66` | low | Practice 5 cites "Theodoris et al. 2023 (Geneformer)" in its source list, but Geneformer is not in §10's resource table (it is in §11's) and the exercise doesn't name that section. Several exercises likewise cite tools/databases not in-table (ColabFold, ChEMBL, BindingDB, Ensembl, GWAS Catalog, MMseqs2, PDBBind, ProteinGym, RegulonDB). Tools are arguably fine; a cited *paper* should point at its section, as `bio/09:67`, `econ/08`, `econ/10` and `philosophy/11:60` correctly do. | flagged → **resolved 2026-10-13**: Practice 5 now cites Geneformer as listed in Section 11 |
| `bio/courses/README.md:9` vs `bio/01-biochemistry/README.md:26` | low | MIT 5.07SC credited to "JoAnne Stubbe" in the course index and "JoAnne Stubbe, John Essigmann" in the section (the section is the correct one). Condensed-index discrepancy only. | flagged → **resolved 2026-10-13**: course index now credits Stubbe and Essigmann, matching Section 01 |
| `bio/11-frontiers/README.md:41` | low | "over 60 words per minute, **approaching natural conversational speed**" — Willett et al. report 62 wpm against ~160 wpm for natural speech; the paper frames it as 3.4× the previous record, not as near-conversational. Baseline prose (not introduced by this pass), so left alone, but it is the one remaining overclaim I found in bio. | flagged → **resolved 2026-10-13**: rewritten to the paper's framing: 62 wpm "begins to approach" 160 |
| `bio/11-frontiers/README.md:65` | low | "Sinclair's work … while **advancing the information theory of aging**" presents Sinclair's own contested hypothesis as an achievement, and the *Lifespan* row has no caveat (contrast the careful hedges added to `econ/03` for Kahneman/Ariely and `econ/10` for Ammous). Practice 4 does require writing "three specific places where the book's claims outrun the evidence", which mitigates it. Baseline prose. | flagged → **resolved 2026-10-13**: now labelled Sinclair's contested hypothesis; *Lifespan* row carries a caveat |
| `philosophy/06-ethics-of-ai/README.md` (resource table; mini-project item 5, line 66) | low–med | The only one-sidedness I found. Every value-laden book points the same way (O'Neil, Crawford, Eubanks, Benjamin); the steelmanning instructions run one direction too ("the structural critique … steelmanned — the case for not automating this at all"; "the stakeholder most opposed gets a steelmanned paragraph"). Nothing asks for the strongest case *for* deploying, and no resource contests the structural-critique framing. Narayanan & Kapoor (added in this pass) cut both ways and (3) requires three normative frameworks, so it is not egregious — but it is the one section that did not get the explicit counterweight the editors gave `econ/03`, `econ/06`, `econ/10`, `philosophy/02`, `philosophy/03`, `philosophy/07` and `philosophy/09`. Suggest either one dissenting resource or a one-line note that the list is weighted toward critical accounts. | flagged → **resolved 2026-10-13**: added Kleinberg et al., a balance note and two-sided steelmen |
| `econ/00-economic-thinking/README.md:38` vs `:33` | low | Suggested Order still opens "Start with this 30-minute video to get a big-picture mental model of how economies work", while the resource row now (correctly) hedges Dalio as "one investor's framework rather than textbook macroeconomics". Minor tension between the two lines. | flagged → **resolved 2026-10-13**: order step now an optional warm-up, matching the hedged row |
| `econ/10-monetary-economics-and-crypto/README.md:62` | low | The treasury mini-project ("whether to hold or convert receipts", 95% VaR on held BTC) edges toward personal-finance territory. It stays on the right side of the line — it is a payments-rail cost model, reports VaR rather than a recommendation to hold, and defers tax to an accountant — but it is the closest thing to investment advice in the three curricula. | flagged (no change needed) → **resolved 2026-10-13**: added an explicit "not investment advice" sentence to the mini-project |
| `philosophy/08-language-and-meaning/README.md:65` | low | "Expect most runs to reach ≥ 95% … while a minority stall in partial-pooling equilibria near 75%" for a 4-state Lewis signaling game under Roth–Erev. Directionally right (partial pooling is the known failure mode), but the majority/minority split for N = 4 is not something I can confirm, and the exercise does ask the learner to measure it. | flagged → **resolved 2026-10-13**: a 1,000-seed simulation confirmed the split; fractions now stated |

### Verification I ran (all passed)

Recomputed in Python and confirmed correct: every `**Check:**` value in `econ/00` ex1–3
(P\*=20, Q\*=600, burden $2/$1, DWL $60, ceiling shortage 240 and DWL $960; ATC ≈$185,
contribution $6,600 → $1,170; tariff +$10/+$5/−4%); `econ/01` ex1–4 (Slutsky −12.5/−12.5,
Hicks −14.64; c = 2√(wr)q^{3/2}, q = p²/9, q = √(pK̄/3); $280 vs $167.50, $96,800 /
$92,450 / $126,200, Lerner in both segments, surplus $145,200 → $189,300; Coase herd = 2,
surplus $7, fence < $6.50, $10 > $3.50); `econ/02` ex1–5 (iterated-dominance order →
(T,C); Battle of the Sexes ⅔ and only Column's mix moving to ¼; serve-left 70% /
anticipate 60% / 62%; Cournot 33.3 & P=53.33, Stackelberg 50/25/45, n-firm
(120+20n)/(n+1), Bayesian 33.3 / 38.3 / 28.3; entry SPE and c < 5; δ\* = ½; Hawk share
V/C); `econ/03` ex1–4 (Allais reduces to sign of 0.34u(2400) − 0.33u(2500) − 0.01u(0);
CPT 946/873 and 327/321; cab 41.4%, PPV 16.5% → 79.5%, $58 vs $7 vs $34; CPT fourfold CEs
7,664 / 998 / −8,291 / −824, reflection effect, warranty WTP $34 vs $86; buffer-buy
E[B] = $7,290, CARA ρ\* ≈ $8,740 verified to $8,851, EVPI $1,372.50, EVSI $511.5,
break-even 0.274; hot-hand 0.46); `econ/04` ex1–5 ((n−1)v/n, revenue (n−1)/(n+1),
variances 0.0556/0.0139, risk-averse 0.444, winner's-curse sign flip at n = 3; reserve ½,
revenue 5/12, 3-bidder 0.5, φ(r) = 150 → $475; all four VCG pathologies including the
collusion asymmetry; double auction 9/64 vs ⅙ = 84%, 43.75% of efficient pairs fail);
`econ/05` ex1–5 (c² + c(1−2c) = 0.09 of 0.25; separation 1 ≤ y\* ≤ 2, λ > ½, warranty
1.33–6.67 y; q_H = 2, q_L = 0.5, prices 0.5/3.5, rent 0.5, profit 0.75 vs 0.667, drop at
λ = ½; moral hazard 169/64, cost 148 vs 144 first-best, and the informative-signal case
recomputed from the likelihood-ratio FOC to **145.58** vs the stated ≈145.6;
Rothschild–Stiglitz low-risk coverage 7.4 and non-existence threshold ≈8%, both verified
numerically); `econ/06` ex2 and ex4 (β–δ 76.9 vs 100, 74.6 vs 67.9; power 7,649 vs 251 per
arm); `econ/07` ex1–4 (z = 0/0.2/0.8, p ≤ ¼; cascade (1−q)²/(q²+(1−q)²) = 0.2; two-sided
prices verified by direct numerical maximization — **0.857 / 7.657** and the swap to
11.143 / −3.657, matching the file exactly); `econ/08` (Pigou 4/3, Braess 1.5 → 2,
degree-2 bound 1.626, atomic affine 5/2, oddness theorem); `econ/09` ex1 and ex4 (plurality
A / Borda C / IRV D / Condorcet B with A a Condorcet loser, and the Borda/IRV manipulation
to B; Shapley 1,150/1,450/4,900, proportional 750/2,250/4,500, serial 1,150/2,950/3,400
with the 4,100 > 3,600 core violation — all reproduced); `econ/10` (post-2024 supply
19,687,500 BTC, flow 164,250/yr, S2F 119.9; Nakamoto q=0.1,z=5 → 0.0009137 reproduced
exactly, exact negative-binomial race → 0.001782 "about double", and the stated reason for
the gap is right; Barro–Gordon π = λa(k−1)y\*; Taylor 1993 form); `econ/11` ex1 and ex2
(regressional shrinkage 1/(1+σ²); extremal mean V peaking at 1.587 near the top 10% and
−2.46 at the top 0.1%; off-switch Δ = −0.13 at σ = 0.1 and +0.11 at σ = 1, both by
simulation); `philosophy/03` ex1–2 (MIU: **216** theorems at length ≤ 12 — "about 200" —
MU absent, I-count mod 3 invariant; both busy-beaver specs and their 6-step/4-ones and
107-step/13-ones results); `philosophy/07` ex4 (E[max(U,0)] = 0.6978 ≈ 0.70 and the
β → 0 limit 0.25); `philosophy/10` ex3 (d = 0.25 power → 251 per arm); `philosophy/11` ex1
(f_sim formula and the f_P·f_I < 10⁻⁶ threshold). Citation spot-checks that came back
clean include every DOI-bearing row I recognised, Butlin et al.'s 14 indicators
(2+4+4+1+1+2), the acknowledge–assess–prepare structure, Carlsmith's ~5%→>10%, Ord's 1-in-10,
Turing's nine objections and his 10⁹/30%/five-minute prediction, Libet's −550/−200 ms,
MMK 1:1 and 24:18, PI §43/§§65–71/§§243–315/§258, Jobin et al.'s 84 guidelines,
DellaVigna & Linos's 1.4 vs 8.7 points, Hagger et al.'s d ≈ 0.04, FlyWire's 139k
neurons / 54.5M synapses, Neuropixels' 384/960/10 mm, gnomAD's 125,748 + 15,708,
JCVI-syn3A's 493 genes, Karr's 28 submodels, Cogitate's 256 participants, the 2023
124-signatory IIT letter, Casgevy's 8 Dec 2023 approval, and the sickle/CFTR HGVS strings.

**Safety (bio):** every exercise and mini-project in all twelve bio sections is
computational, database- or literature-based. There is no wet-lab step, no reagent, no
culture, no instrument to build, nothing involving mains or high voltage, high current,
batteries, lasers or chemicals — the closest approaches are "order a PDB entry into
ChimeraX", "design three protospacers *in silico*", and §07's "say which 10 constructs you
*would* order first", all hypothetical. No safety caveat is therefore missing. One
adjacent note: §07 (binder design) and §11 (synthetic biology, genome-scale generative
models) carry no dual-use pointer, while §10 has Urbina et al. and makes it a Suggested
Order item ("read before you build anything in this space, not after"); a one-line
cross-reference from §07/§11 to that row would close the gap. No employer, product or
customer of the owner's is named anywhere in the three curricula (grep clean), and there is no
investment advice.

### Overall judgment per curriculum

**bio** — Strong. The citation corrections in this pass are all improvements I could
independently confirm (Jinek 2012 rather than "Doudna & Charpentier 2014", Milo et al.
rather than "Alon", Dayan & Abbott 2001, Anfinsen's real lecture title, Callaway 2015 with
the right DOI, Dill & MacCallum's *Science* paper, Griffiths' 12th-edition author list,
MITx 7.00x, Jeff Gore for 8.591J, the Lodish and Stryer editions). The learning layer is
the best-specified of the three: objectives are operational, exercises name deliverables
and success criteria, and the quantitative ones I could check are sound. One real defect —
the §09 noise budget's impossible 5 µV target against a 1 MΩ electrode — plus the AF3
licence claim, plus a handful of unverifiable 2026-dated rows. Everything is safe.

**econ** — The most quantitatively reliable body of work in my scope. I recomputed roughly
sixty stated check values across all twelve sections and found **zero** errors — including
some that would be easy to get wrong (the Chatterjee–Samuelson 9/64, the CARA risk-tolerance
root, the informative-signal agency cost, the two-sided prices, the exact-vs-Poisson
double-spend race, serial cost sharing failing the core by exactly $500). Balance work is
conscientious: Hazlitt gets a steelman-the-exception prompt, Dalio and Ammous are labelled
as single-school frameworks, Kahneman and Ariely carry replication caveats with the
specific retraction and multi-lab failure named, Ostrom sits next to Coase, CORE next to
Mankiw, and out-of-list sources (Budish, Calvano, Gao et al.) are flagged as such with
enough spec to work from. Only citation-metadata nits remain.

**philosophy** — Also strong, and unusually disciplined about epistemic status: `03`
requires labelling every claim theorem / thesis / conjecture and pairs Wolfram with
Aaronson's review; `02` pairs IIT with both the pseudoscience letter and the Cogitate
adversarial test; `07` pairs Bostrom and Carlsmith with "AI as Normal Technology"; `09`
pairs Sapolsky with Mitchell and requires both steelmen; `01`, `05` and `08` all require
the opposing view in the author's own strongest form. I found no contested position
presented as settled. The exceptions are the Kim title (fixed), two SEP attribution/title
nits, and `06`, which is the one section whose reading list and steelmanning prompts run in
a single direction and would benefit from a counterweight or an explicit note.

---

## V4 — Independent check of `pcb/` and `btc/` (review branch vs baseline `a8b86e9`)

Method: read `git diff a8b86e9 HEAD` for both curricula and every section README in full. Ran `tools/check_repo.py`: 0 problems in pcb/btc. The only reported problem is the pre-existing root `README.md:2` banner. Checked IPC-2221A citations and the tutorial claims against the included PDFs (`pcb/documents/`) and Rick Hartley's list against `Ricks-Reading-Recommendation.pdf`. Recomputed the numbers in Python (the scripts were not kept), including the copper and IPC tables, emissions, PDN, thermal, double-spend, Bitcoin address and test-vector values. No git state was changed. Line numbers refer to the files after my edits.

| File:line | Severity (high/med/low) | Issue | Action (fixed / flagged) |
|---|---|---|---|
| pcb/00-electronics-fundamentals/README.md:55 | med | The mini-project measures a ferrite bead with a VNA in 2-port shunt-through. That method only resolves milliohm-to-ohm impedances, so the bead's peak of hundreds of ohms, and its R–L–C fit, would be unreliable. | fixed: the bead is now measured series-through, with the reason given |
| pcb/04-pcb-layout-fundamentals/README.md:60 | med | The high-voltage netclass clearance is taken from IPC-2221 Table 6-1 with no warning that IPC-2221 spacing is not a safety rating for mains or other hazardous voltages. | fixed: added a safety note (creepage, clearance and insulation come from IEC 61010-1 or IEC 62368-1) |
| pcb/10-advanced-topics/README.md:67 | med | The heater-board mini-project (power resistors or a MOSFET in its linear region; a 0-via site in still air) had no safety caveat. Risks: overheating and burns, and MOSFET thermal runaway at fixed gate drive. | fixed: current-limited supply, closed-loop current control, firmware over-temperature cut-off, never left unattended |
| pcb/13-bring-up-test-and-debug/README.md:95 | med | The ground-loop experiment uses a mains-earthed scope but never warns against defeating the protective earth, a common and dangerous "fix". | fixed: never lift the scope's PE; isolate the DUT side or use a differential probe |
| pcb/13-bring-up-test-and-debug/README.md:98 | med | Fault-finding uses isopropyl alcohol on an energized short (a hot spot) with no flammability caveat. | fixed: caveat added |
| btc/04-transactions-and-scripting/README.md:63 | med | "Your own signer" funds addresses for a homemade signer with `sendtoaddress` but never names the network. | fixed: "On regtest (never with real funds)" |
| pcb/05-power-and-grounding/README.md:66 | med | Practice 3's done-criterion requires agreement with FastHenry, but FastHenry is not listed in any pcb resource table (no link or install route). | flagged: verify and add a FastHenry (FastFieldSolvers) Tool row, or make the cross-check optional → **resolved 2026-10-13**: FastHenry2 tool row added; Practice 3's cross-check stays optional |
| btc/02-protocol-fundamentals/README.md:56 | med | "CVE-2012-2459 — see Section 13's Optech soft-fork-activation topic." That topic covers activation mechanisms. CVE-2012-2459 (duplicate-subtree Merkle malleability) was fixed in validation code, not by a soft fork, so the pointer very likely leads to a page that doesn't cover it. | flagged: re-point to a verified source, e.g. the Optech Merkle-tree-vulnerabilities topic or BIP 54's rationale, if it covers it → **resolved 2026-10-13**: now explains the validation-code fix and points to Optech's Topics index |
| pcb/01-pcb-anatomy-and-materials/README.md:48 | low | The done-tolerance of ~15 % can't be met. Recomputed IPC-2221 external widths at ΔT = 10 °C and 1 oz against the tutorial table: the 1 A row is +18.9 % (11.9 vs 10 mil), every other row ≤ 8 %. The mΩ/in column checks within 3 %. | fixed: ~20 %, with a note on the 1 A row |
| pcb/06-signal-integrity/README.md:73 | low | The SI coupon's "10 mm stub" has its quarter-wave notch at about 3.7–4.1 GHz (εeff 3.3–4.2). That is above the 1.5–3 GHz NanoVNA-class VNA the project specifies, so the stub can't be compared against prediction. | fixed: ~30 mm open stub (notch ≈ 1.2–1.4 GHz), with the reason |
| pcb/07-emc-and-compliance/README.md:65 | low | Section 00 says its impedance rig is reused in Sections 05 and 07, but Section 07 never used it (internal inconsistency). | fixed: Practice 2 now lets the learner measure L_bead on the Section 00 rig |
| pcb/13-bring-up-test-and-debug/README.md:72 | low | The bring-up plan had no ESD-handling step. | fixed: added an ESD-safe-handling bullet |
| pcb/13-bring-up-test-and-debug/README.md:25 | low | The text says firmware debugging (GDB, OpenOCD, RTT) lives in the software curriculum but linked only software/07. OpenOCD and RTT are in software/12, and STUDY-GUIDE pairs pcb/13 with software/12–13. | fixed: added software/12 and /13 links |
| pcb/12-analog-mixed-signal-and-precision-measurement/README.md:23 | low | physics/12 calls itself "the physics layer under PCB Section 12", but pcb/12 had no link back. | fixed: optional-theory link added (same pattern as pcb/06) |
| pcb/README.md:88; pcb/courses/README.md:13 | low | Dr. EMC is listed without the "unverified channel, handle mismatch (@DrEMC vs @DrEMC-sf8rx)" note that Sections 06 and 07 carry. The review flagged this but didn't fix it. | fixed: note added. Still flagged: the link itself may be wrong → **resolved 2026-10-13**: links corrected to @DrEMC-sf8rx (Anton Tichenko); dropped from Key Educators |
| btc/01-cryptography-foundations/README.md:7 | low | The prerequisite sends the learner to math/08 for "discrete logs, elliptic-curve cryptography", but math/08 has no elliptic-curve content. The new math/13 (Number Theory & Cryptography) was written as btc/01's companion and links back. | fixed: math/08 for groups and fields, math/13 for DLP, EC, ECDSA and Schnorr |
| btc/12-hands-on-labs/README.md:150 | low | Practice 1 needs a testnet4 node, but the Lab 0 bench only has regtest, signet and pruned mainnet. | fixed: note to add one |
| btc/PROGRESS.md (Sections 00, 03, 04, 06–11) | low | 15 resources in the section tables had no PROGRESS checkbox. These are baseline gaps the edit pass didn't close (e.g. Fermat's annotated whitepaper, LMAB Mining, Saylor, LMAB Taproot, BIP 77). | fixed: checkboxes added |
| pcb/05-power-and-grounding/README.md:34; pcb/books/README.md:14; pcb/PROGRESS.md:73 | low | *Fast Circuit Boards: Energy Management* is dated 2017. My recollection is Wiley, January 2018. The date is consistent across files, and the reviewer cited e-bookshelf. | flagged → **resolved 2026-10-13**: year corrected to 2018 (Wiley hardcover) in all three files |
| pcb/02-schematic-capture/README.md:25 | low | "KiCad 10.0 … adds … design blocks": schematic design blocks shipped in 9.0. If 10.0's addition is *PCB* design blocks (as pcb/04's mini-project implies), say so. | flagged → **resolved 2026-10-13**: now says design blocks arrived in 9.0; release notes confirm |
| pcb/04-pcb-layout-fundamentals/README.md:60 | low | "Rev C (2023) updated the clearance guidance" is an unverified claim about what IPC-2221C changed in Table 6-1. | flagged → **resolved 2026-10-13**: reworded: check the Rev A values against IPC-2221C (2023) |
| pcb/04-pcb-layout-fundamentals/README.md:61 | low | The place-only study (three full placements, scoring, then routing an STM32U5/USB-C/buck/2×LDO/Ethernet/RJ45 board) is budgeted at ~5 h. That is optimistic; ~8–12 h is more realistic. | flagged → **resolved 2026-10-13**: budget raised from ~5 h to ~10 h |
| pcb/05-power-and-grounding/README.md:5 | low | Hype (baseline text): "#1 cause of board failures"; Hartley's lecture "has saved more PCB designs than any other single resource". Both are unverifiable superlatives. | flagged → **resolved 2026-10-13**: both superlatives softened ("one of the most common causes") |
| btc/06-network-and-p2p/README.md:43; btc/13-governance-and-protocol-change/README.md:57 | low | "BIP 110 … is now marked Closed": the live status of a contested proposal, which I can't verify (reviewer notes say it was checked). Re-check the BIPs repo before relying on it. | flagged → **resolved 2026-10-13**: BIPs repo confirms Closed; btc/06 now says "checked October 2026" |
| btc/09-economics-and-game-theory/README.md:24, 31, 42 | low | Tone: 🔑 on two advocacy pieces, and the Suggested Order opens with *The Bitcoin Standard* and *Bullish Case* before any academic counterweight. The descriptions label them as advocacy, so this is ordering only. | flagged → **resolved 2026-10-13**: 🔑 moved to Budish and Carlsten; order now opens with incentive economics |
| several (pcb 04, 09; btc 00, 01, 02, 05, 07, 10) | low | More than 3 🔑 per section, against the new SKILL rule "🔑 for at most ~3". Mostly baseline; btc/01 went +1 with MB ch. 8. | flagged → **resolved 2026-10-13**: all listed pcb and btc sections now at ≤3 🔑 |
| pcb/03-component-selection/README.md:62 vs pcb/00…:63 | low | The same Check Yourself question (10 µF / 6.3 V / 0603 X5R at 5 V) appears in two sections. Acceptable as spaced repetition. | flagged (no action needed) → **still open**: unchanged; the checker judged it acceptable spaced repetition |
| various (pcb/00:23–24, pcb/04:36, btc/06:42, btc/11:68 and 88, btc/12:62) | low | Claims at or after my knowledge cutoff that I can't verify independently; the reviewers cite sources. Examples: x-Chapters 2nd ed. (2026) and LAoE 2nd ed.; AN2867 "Rev 24, 2026"; cluster mempool in Core 31.0 (Apr 2026); Bark on mainnet mid-2026; Sparrow 2.5 silent payments; BIP 95 Testnet 5 draft. | flagged (spot-check if relied on) → **resolved 2026-10-13**: every example spot-checked against sources; all correct, no changes |

**Verified correct (no change needed), for the record.**
- pcb: every IPC-2221A citation matches the included PDF: Appendix B (1956 NBS report; internal curves = half of external), §1.6.2, §3.5.2/§3.5.3/§3.5.4.1 test-land rules, §6.2 formula and k values, §6.4.1, §6.4.4 "should not be segmented", §9.1.1 a+2b+c, §9.1.2, and Tables 4-1, 6-1, 6-2, 9-1 and 9-2.
- pcb: every tutorial claim quoted in pcb/01 Practice 4 is in the PDF. Rick's 12 books and their grouping match his PDF exactly.
- pcb: recomputed values all check out — t_r·BW = 0.35; kTB noise of 1 MΩ over 10 Hz = 0.41 µV; birthday bound 82k; Ott's DM field 2.2 vs 88 µV/m (32 dB) and CM limit 3.6 µA; plane capacitance 3.8 nF / 0.42 Ω; cavity resonance 915 / 732 MHz; λ/20 = 3.4 mm; via thermal resistance ≈ 190 K/W; ½ LSB at 16 bits = 7.6 ppm; and the HTLC and Lightning arithmetic.
- btc: key-1 P2PKH (compressed and uncompressed) and P2WPKH addresses; BIP 84/86 "abandon…about" vectors; the `bcrt1q6rz28…z3cppk` regtest address; genesis scriptSig (bits / 4 / 69-byte headline); exact-model double-spend (6 vs Satoshi's 5 confirmations at q = 0.10); vsize 226/141/154; selfish-mining break-even (1−γ)/(3−2γ).
- No employer, product or customer names appear in pcb/ or btc/. Exercises are tailored (STM32U5, PIR-style AC-coupled amplifier, SMU channel) but never named.

### Overall judgment

**pcb.** This is genuinely expert-grade material. The new learning layer is quantitative, tied to a modern embedded stack (KiCad 9/10, STM32U5, USB-C, Ethernet, precision analog), and almost every engineering number and rule of thumb I recomputed is right. The IPC-2221A citations are unusually precise and all check out against the included standard. The weaknesses were practical rather than conceptual: bench exercises missing safety caveats (protective earth, IPA, heater thermal runaway, the HV-spacing scope, ESD), two measurement-design slips (bead in shunt-through, an out-of-band stub), one unlisted tool dependency (FastHenry), and some optimistic time budgets. I fixed the first two groups. The two new sections (12 and 13) are the strongest additions and fit an embedded-hardware engineer well.

**btc.** Accurate, carefully hedged and safe. Every test vector and derived value I could check reproduces exactly. Funds safety is good: everything runs on regtest or signet, the one ambiguous exercise is now fixed, and mainnet use is read-only. Proposal statuses are handled with discipline: an explicit status snapshot, "not activated" stated each time, and BIP 3's meaning of "Complete" explained. Economics is framed as analysis, with an explicit no-investment-advice line and advocacy labelled as such. The residual risks are post-cutoff status claims (BIP 110 "Closed", Core 31 cluster mempool, Ark and wallet support), which will date quickly and which I couldn't verify, and one misdirected cross-reference (CVE-2012-2459). The new labs and governance sections are well built and internally consistent with the rest of the curriculum.

---

## V5: software/ and repo-level files (verification)

Scope: `software/` (diff vs `a8b86e9`, then every section README read in full, plus PROGRESS, README, books, courses, blogs and the skill); `README.md`, `STUDY-GUIDE.md`, `notes/README.md`, `projects/README.md`, `reviews/README.md`, `reviews/2026-10-deep-dive/README.md` and `link-audit-arxiv.md`, `tools/check_repo.py`, `.agents/skills/audit-curriculum/SKILL.md`. I read the four `*/.agents/skills/update-curriculum/SKILL.md` files but did not edit them, except the software one, which is in scope. I ignored `assets/banner.jpg`, as instructed.

**How I tested `tools/check_repo.py`:** I ran it on HEAD with and without `--urls`. Both report 1 problem (the banner), and with `--urls` it lists the URLs. I also ran it on the baseline tree, where it reproduces the 36 broken internal links the review claims. On a scratch copy I injected faults: a broken link, a broken image, a ragged row, a missing H2, an H3 slip, a missing mini-project, PROGRESS gaps, a section directory with no README, parenthesized and bold URLs, and template URLs inside code spans. I then diffed the `--urls` output before and after my fix: only the 12 bad entries changed. Finally, I rendered the Study Guide's Mermaid diagram with mermaid-cli 11.16. It parses cleanly: 9 nodes, 14 edges (3 bidirectional), and all 11 labels.

| File:line | Severity | Issue | Action |
|---|---|---|---|
| tools/check_repo.py:20, 51–64 | med | `--urls` truncated every URL containing parentheses. 8 DOIs (e.g. `https://doi.org/10.1016/0004-3702(91`, the econ SICI DOI and its crossref URL) came out cut short. It also emitted 4 bogus template URLs from inline code in the skills (`…/works/<DOI`, `arxiv.org/abs/<id`, `oembed?url=<url`). The audit-curriculum skill's step 2 feeds this list to a link checker, so it would report false breaks and never check the real URLs. | **fixed.** http targets now come from LINK_RE, which already handles balanced parens. Bare URLs come from a balanced-paren URL_RE run on code-masked text, and a trailing `*` is stripped. Output is now 1,254 URLs. The before/after diff is exactly those 12 entries replaced by the 8 full DOIs. |
| tools/check_repo.py:80–90 | med | The checker crashed with an uncaught `FileNotFoundError` traceback when a numbered section directory had no `README.md`, or a curriculum lacked `PROGRESS.md` or `README.md`. That is exactly the state partway through adding a section. | **fixed.** It now reports "file missing" and the other checks keep running. |
| tools/check_repo.py:92–96 | low | The heading check was a substring test, so a heading-level slip (`### ✅ Check Yourself`) passed. Mini-project presence was checked in PROGRESS but never in the section README. | **fixed.** Headings are now anchored at line start, and `**🏗️ Mini-project` is required in each README. All 120 sections pass. The docstring is updated. |
| tools/check_repo.py (general) | low | Remaining blind spots. False negatives: `#anchor` targets aren't validated; `[x](p "title")`, `<…>` and reference-style links are skipped; tables without a leading pipe or inside blockquotes aren't checked; an unescaped `\|` inside a code span in a table row is masked, although GFM splits on it; block order and Suggested-Order coverage aren't checked. False positives: root-relative `/path` and URL-encoded paths are reported as broken, and `~~~` fences aren't recognized. I scanned the repo and none of these currently hides or causes a real finding. | flagged → **still open**: checker unchanged; anchors, titled links and tilde fences still unchecked |
| software/00-cs-foundations/README.md:59 | low | Practice 1 said to time naive recursive Fibonacci "from n = 10³ upward", which is infeasible (about 10²⁰⁸ calls). The other recomputed numbers are correct: SICP gives 292 ways, 15,499 calls at 100 ¢ and 12,822,611 at 500 ¢. | **fixed.** Added "(n ≈ 20–35 for the recursive Fibonacci…)". |
| software/01-python-mastery/README.md:74 | low | Practice 3 runs the list-based pipeline on 1–2 GB CSVs. Parsed Python rows take about 5–10× the file size, so 2 GB would need roughly 10–16 GB of RAM and is likely to swap or OOM on a laptop. | **fixed.** Added a one-sentence caveat. |
| software/01-python-mastery/README.md:80 | low | `pyright --strict`: I don't believe pyright's CLI has a `--strict` flag. Strict mode is set with `typeCheckingMode = "strict"` in `[tool.pyright]` or `# pyright: strict`. `mypy --strict` is fine. | flagged (fairly but not fully sure) → **resolved 2026-10-13**: now pyright strict mode via `typeCheckingMode = "strict"` |
| software/03-reading-and-reviewing-code/README.md:86 (also :16 and CY Q7) | med | The security objective, Practice 5's security checklist and Check Yourself Q7 depend on vulnerability classes that no Section 03 resource teaches. | **fixed.** Practice 5 now cites "OWASP Top 10 and the SEI CERT C Coding Standard, listed in Section 08". |
| software/04-architecture-and-design-patterns/README.md:21 (and CY Q1) | low | "Richards & Ford's two laws": I believe the 2nd edition, which is now the listed edition, adds a third law ("decisions exist on a spectrum"). | flagged (uncertain) → **resolved 2026-10-13**: Q1 now asks for all the laws, noting the 2nd edition's third |
| software/06-systems-and-infrastructure/README.md:40 | low | *System Design Interview* Vol 2 is co-authored by Sahn Lam; the row named Alex Xu alone. | **fixed** |
| software/09-agentic-ai-workflows/README.md:59 | low | The row says "Claude Code can read it [AGENTS.md] in place of CLAUDE.md". As far as I know, Claude Code reads CLAUDE.md, and AGENTS.md has to be imported (`@AGENTS.md`) or symlinked. If that's right, a learner who relies on this sentence gets an ignored file. | flagged (verify on the web) → **resolved 2026-10-13**: row now states when Claude Code reads AGENTS.md, per official docs |
| software/09-agentic-ai-workflows/README.md:57 | low | The author is given as "Anthropic Applied AI team". The post may name individual authors, and skill rule 2 says to cite people. | flagged → **resolved 2026-10-13**: now names the four authors (Rajasekaran, Dixon, Ryan, Hadfield) |
| software/09-agentic-ai-workflows/README.md:41–55 (repo-wide) | med | 🔑 inflation contradicts the review's own new rule ("🔑 for at most ~3 core items per section", in all four update skills, the root anatomy and STUDY-GUIDE:118). software/09 went from 6 to 9 🔑. The review also pushed software/00 (3→4), 02 (5→6), 05 (3→4), 07 (4→5) and 11 (3→4) over the limit: 17 sections repo-wide, with 44 of 120 now above 3. | flagged (choosing what to demote is a curation call) → **resolved 2026-10-13**: every section repo-wide now has ≤3 🔑; software/09 has 3 |
| software/10-version-control-and-collaboration/README.md:89 | low | This was the only software mini-project with no `projects/software/…` deliverable, which the root anatomy requires. | **fixed.** The decision note now goes in `projects/software/10-repo-hygiene/`. |
| software/11-professional-practice/README.md:62 | low | Practice 1 gives "Nygard's format" as Title, Status, Context…, which contradicts its own resource row and Nygard's post (Title, Context, Decision, Status, Consequences). | **fixed** |
| software/books/README.md:3, software/README.md:54 | low | The books page claims it is "ordered from foundational to advanced", and the README says "with reading order". Neither is true: Beginner titles sit at #14, #18 and #20 after Advanced ones, and #21–24 were simply appended. | **fixed** (reworded both) |
| software/.agents/skills/update-curriculum/SKILL.md:80 | low | "Update the root README.md" is ambiguous now that a repo-level README exists. The intended target is `software/README.md` (Key Resources). | **fixed** |
| software/09-agentic-ai-workflows/README.md:5, software/03-reading-and-reviewing-code/README.md:109, software/09 CY Q8 | low | Tone: "AI agents will write most of the code" is stated as fact. This is the original premise, and two self-test questions presuppose it. The newly added METR and DORA evidence is appropriately hedged. | flagged → **resolved 2026-10-13**: framed as the curriculum's bet; both self-test questions now hedged |
| STUDY-GUIDE.md:41 | med | Track A placed math/03 after math/12, but math/12 lists math/03 (and 01, 02 and 07) as prerequisites. | **fixed** (math/03 now comes before math/12) |
| STUDY-GUIDE.md:44 | med | Track A's firmware chain omitted software/01, a stated prerequisite of software/05 and software/13. Section 13 explicitly needs 01's Typed Instrument Library mini-project. | **fixed** (software/01 prepended) |
| STUDY-GUIDE.md:43 | low | "physics/03 → physics/12", but physics/12 requires physics/02, 06 and 08, and the physics README says to take it right after 08. | **fixed** (parenthetical added) |
| STUDY-GUIDE.md:35 | low | The tracks skip other listed prerequisites: math/01 for 02/03/07/12/14; physics/10 for physics/11 (Track D); bio/06 for bio/10; philosophy/03 for philosophy/05 (Track E). | **fixed.** One sentence added: tracks name sections, so check each section's Prerequisites. |
| STUDY-GUIDE.md:17 | low | Says "(template below)", but there is no template below; it is in notes/README.md. | **fixed** (now links it) |
| STUDY-GUIDE.md:100, 105, 106 | low | The one-home table under-reports existing duplicates. The AlphaFold 2 paper is a full row in bio/03, bio/10, ml/13 and physics/11. InstructGPT/RLHF is a 🔑 row in ml/09. Finite fields are taught in math/08. | **fixed** (added under "Also touches") |
| STUDY-GUIDE.md:121 | low | The convention says `*(unverified: …)*`, but the actual markers (pcb only) vary and aren't italic: "(Unverified: …)", "(unverified course; …)", "(unverified channel; …)". | flagged → **resolved 2026-10-13**: pcb's variant markers were removed; no "(unverified…)" markers remain |
| STUDY-GUIDE.md:87, README.md:13 | low | 🧠 is used for both ml and philosophy, in the Mermaid nodes and in the README nav. Cosmetic. | flagged → **resolved 2026-10-13**: philosophy now uses 💭 in the README, its curriculum page and the Mermaid map |
| .agents/skills/audit-curriculum/SKILL.md:50 | low | The heading said the rules are "same as every update-curriculum skill". They aren't: the root adds rule 7 ("one home per topic"), and the update skills carry "keep the learning layer whole" and "run check_repo" as numbered rules. | **fixed** (wording) |
| ml/pcb/btc/software update-curriculum SKILL.md (rules block); btc SKILL:77 | med | Inconsistencies with the root skill. (a) None of the four update skills has the root's "one home per topic" rule, so update runs can keep adding duplicate rows across curricula. (b) ⭐ is a closed list in ml ("never add", 27 items) and pcb (the 12 books in the PDF), but btc's "Satoshi/Cypherpunk canon" isn't enumerated, which contradicts rule 6 and STUDY-GUIDE ("closed and exact"). The rules blocks are otherwise byte-identical across all four. | flagged (only software is in my edit scope; fix all four together) → **resolved 2026-10-13**: one-home rule added to all four; btc ⭐ limited to canon table |
| pcb SKILL:69–73; ml SKILL; btc SKILL:74; reviews/2026-10-deep-dive/README.md:88 | low | Only pcb's skill says to also update books/, courses/ and blogs/; ml and software have those folders but don't say so. The "Append-only" notes in ml, btc and software sit uneasily with the deep-dive's recommendation #2, "Curate instead of append-only". | flagged → **resolved 2026-10-13**: the ml skill now names the index files; pcb, btc (section map) and software already did |
| .agents/skills/audit-curriculum/SKILL.md:19–20 | low | The skill prescribes `## Why This Section Matters` and `## Prerequisites` H2 headings. In practice, 24 sections use a blockquote "Why" and 46 have no `## Prerequisites` heading (a bold line or nothing). The content exists, and check_repo doesn't enforce the headings. | flagged → **resolved 2026-10-13**: the skill now accepts an opening paragraph and a bold **Prerequisites:** line in older sections |
| reviews/2026-10-deep-dive/link-audit-arxiv.md:11, 12, 13, 15, 17 | low | Five table cells ended in truncated fragments ("[Fix at: econ/11-ai-alignment-economi", "results list only the 2020 ", "[Fix at: math/07-differenti", "Suggested citation author: 'Ko", "Year 2"). | **fixed** (trimmed to the last complete sentence) |
| reviews/2026-10-deep-dive/link-audit-arxiv.md:3 | low | "each arXiv link in the repo (116)": that is the pre-review set. The baseline has exactly 116; HEAD has 186. | **fixed** (clarified) |
| reviews/2026-10-deep-dive/README.md:3, 113–122 | low | It says fixes are on branch `review/2026-10-deep-dive`, "one commit per curriculum plus one for the repo-level changes". This working copy has 4 "wip" commits on master. | flagged (orchestrator: make the delivered branch match) → **resolved 2026-10-13**: the delivered branch has one commit per curriculum plus a repo-level commit per pass; the wip commits were only in the reviewer's scratch copy |
| reviews/2026-10-deep-dive/README.md:41 | low | "Resource rows in section tables 1,076 → 1,458" reproduces exactly as *all* table rows in section READMEs, including Key Concepts and in-practice tables; true resource rows are 1,061 → 1,432. "Each added item was opened" can't apply to the ~17 added link-less Concept rows. | flagged (immaterial) → **resolved 2026-10-13**: the README now counts resource rows only (1,026 → 1,499 after the final pass) and states the method |
| (cross-curriculum, outside my scope) econ/*/README.md, bio/00-molecular-biology-fundamentals/README.md:58 | low | econ mini-projects use `projects/econ/<name>/` with no `NN-` prefix, and bio/00's mini-project names no deliverable path. Both contradict the STUDY-GUIDE and projects/README convention. | flagged (for the econ/bio verifier) → **resolved 2026-10-13**: econ paths now use the NN- prefix; bio/00 names its deliverable path |

**Verified correct, no action needed:**
- **Root README:** 120 sections and every per-curriculum range (00–13 / 14 / 12 / 11 …).
- **Deep-dive numbers:**
  - Sections went from 110 to 120.
  - The baseline had 36 broken links.
  - There are 594 objectives and 585 exercises; every PROGRESS "Practice exercises 1–N" matches its section.
  - There are 120 mini-projects and 960 Check Yourself questions.
  - PROGRESS checkboxes went from 990 to 1,892.
  - The baseline had 116 arXiv links and 619 others ("~600").
  - All 8 arXiv fixes are applied.
  - "Three skills mapped to nonexistent dirs" is correct (pcb, btc, software).
  - "8 of 16 🔑 in ml/08" is correct.
- **Skills:** all four section maps cover every existing directory.
- **Recomputed software values:**
  - RMA: U = 0.80 vs a bound of 0.757, UI worst-case response 69.5 ms, maximum UI C = 45 ms (harmonic periods).
  - The COBS bound `n + n//254 + 1` holds.
  - TMP117: 3200 / −5120 / 0x8000 = −256 °C.
  - Error budget: 99.5% ≈ 3.6 h per month.
  - ⌈log₂ 200⌉ = 8.
- **Safety and privacy:** there are no mains, battery or chemical exercises, and the PSU step is current-limited below VDDA. The employer and products are never named.

### Overall judgment

**software/:** The edits are high quality. Every citation detail I could check from memory is right: editions, years, co-authors, chapter titles for Fluent Python, Pro Git, the SRE book, Making Embedded Systems and K&R, the OWASP 2025 categories, the CRA dates, and the METR and DORA figures. All the "you should get X" numbers recompute correctly. The exercises are concrete, aimed at an embedded and instrument engineer, have clear done-criteria and honest time estimates, and keep bench work low-voltage. The remaining weaknesses are about curation discipline more than accuracy. 🔑 inflation goes against the review's own ≤3 rule (software/09 now has 9). A few claims can't be confirmed offline: Claude Code reading AGENTS.md, `pyright --strict`, and the 2nd edition's "two laws". The handful of practicality and consistency slips are now fixed.

**Repo-level docs and tooling:** Every number in the root docs that I could reproduce is correct, every relative link resolves, and the Mermaid diagram renders. Track A, the core track in STUDY-GUIDE, contradicted the sections' stated prerequisites in three of its four chains, and the one-home table under-reported duplicates; both are fixed. `check_repo.py` did what its docstring promised, but it had a crash path and a `--urls` bug that would have corrupted the very audit workflow it feeds. Both are fixed and regression-tested, and HEAD still reports only the banner. The four update skills share an identical rules block, but they encode a 🔑 limit the repo doesn't follow, lack the root's one-home rule, and leave btc's ⭐ list open-ended.

**Counts:**
- Fixed: 20 (med 5, low 15)
- Flagged: 15 (med 2, low 13)

---

---

## Second check: the follow-up pass (2026-10-13)

Four fresh checkers, with web access this time, re-checked what the follow-up pass changed. None of them had written any of it. They covered:
- the 9 new sections
- the resources added to existing sections
- the applied link-audit fixes
- the tier lists
- the new Description column in ml/07–13

They fetched each sampled citation, and they recomputed every expected value in the new sections' exercises in Python. **342 items checked: 311 ok, 25 fail, 6 unverifiable.** All 25 failures are fixed.

| Scope | Checked | ok | fail | unverifiable |
|---|---|---|---|---|
| ml: section 14, the 07–13 descriptions (30 sampled), tiers, link fixes | 72 | 67 | 3 | 2 |
| bio and philosophy: bio/12–14, the biosecurity subsection, link replacements, philosophy/12, additions, tiers | 108 | 95 | 10 | 3 |
| econ: econ/12–15 (all 43 resources), additions, link fixes, tiers | 101 | 96 | 5 | 0 |
| physics, math, pcb, btc, software: additions, link fixes, tiers, confidentiality grep | 61 | 53 | 7 | 1 |

Everything else checked out:
- **Exercise values:** every one in bio/13, bio/14, philosophy/12, econ/12–15 and physics/12.
- **COMPAS:** reproduced exactly from ProPublica's file (44.85/23.45 FPR, 27.99/47.72 FNR on 7,214 rows).
- **ml/14:** all 16 citations.
- **Descriptions:** 30 of 30 sampled.
- **Link replacements:** all nine bio replacements.
- **Biosecurity subsection:** balanced, with no uplift content.
- **Confidentiality:** the grep found no employer, product or customer names.

| Where | Finding | Fix applied |
|---|---|---|
| ml/14 Practice 4 | The keyword-spotting route needs a trained model that no exercise builds, so ~6 h is too low | The exercise now says to train it first (about 2 h extra). The time is ~6 h on the tinyvision route and ~8 h on the keyword-spotting route. |
| ml/12, Global Workspace row | The byline is Gurnee, Sofroniew, Pearce, …; Lindsey is not the third author | Now "Gurnee, Sofroniew et al." in ml/12, ml/PROGRESS and the philosophy/02 cross-reference |
| ml/12, METR row | arXiv titles the paper "…Complete Long *Software* Tasks" | Title corrected after re-fetching arXiv v1 and the current version |
| bio/12 Practice 1 | 0.05 × 19,800 = 990 false positives, not 970 | Now ≈ 1,190 discoveries, of which ~990 are false. A simulation gave 1,197 and 1,000. |
| bio/12 Practice 1 | The π₀ estimate is ≈ 0.99, not 1.0; the bias is negligible at 99% power | Rewritten |
| bio/12 Practice 3(b) | ≈ 7 discoveries (0–15 from run to run) at ~4% power, not ~12 at ~6% | Rewritten. A simulation gave a mean of 7.3, 13% of runs with none, and power of 3.6%. |
| bio/12, Benjamini & Hochberg row | "Five pages", but the paper runs pp. 289–300 | "Twelve pages" |
| bio/12, Why | "batch effects have invalidated whole literatures" overclaims Leek et al. 2010 | Now "overturned high-profile published findings" |
| bio/courses | 🔑 on Khan AP Biology, Alon's lecture videos, iBiology and HHMI BioInteractive, none of them core in any section; the tier log's note was stale | 🔑 removed; log corrected |
| bio/00 | The core path held two overlapping Lander intro courses | MIT 7.012 demoted; the core path is now 7.01SC → Alberts |
| philosophy/12, SEP Bayesian row | §1 is a general tutorial, not a route specifically to confirmation | Description corrected |
| philosophy/12 Practice 3 | Mayo covers optional stopping in Excursion 4, Tour III, not Excursion 3 | Fixed |
| philosophy/06 | The core path covered neither objective 2 nor Practice 3 | *Fairness and Machine Learning* is now 🔑 (the third slot); PROGRESS synced |
| econ/07, Katz & Shapiro | JSTOR 1816044 is a different paper | Now jstor.org/stable/1814809 (the paper's JSTOR cover page; RePEc gives *AER* 75(3):424–440) |
| econ/00, MRU row | The link goes to *Principles of Microeconomics* by Cowen, Tabarrok & Girante | Title and instructors fixed in 00, PROGRESS and courses/ (page re-fetched) |
| econ/01 | Khan Academy, a conditional review aid that is already core in 00, was 🔑 | Demoted; the core path is now Varian & Melitz → MIT 14.01 |
| econ/03 | The core path was all behavioral, with nothing on normative decision theory | SEP "Decision Theory" (Steele & Stefánsson) is now 🔑 |
| econ/12 | The core path held only the optimistic micro evidence | Acemoglu, "The Simple Macroeconomics of AI" is now 🔑 |
| software/05 | A sourceless "Review AI-generated tests" row kept 🔑 | 🔑 moved to Khorikov's *Unit Testing Principles, Practices, and Patterns*; Practice 3 now cites Grenning |
| software/08 | A sourceless concept row was on the core path | 🔑 moved to the Threat Modeling Manifesto |
| software and other indexes | 🔑 on index-only items | Removed from ArjanCodes, Dehaene's course, Bishop & Bishop, Blockchain and Money, Rick Hartley's list and the physics/courses *Essence of Linear Algebra*. Blogs indexes keep their own "follow first" 🔑, and the curriculum README legends now say so. |
| reviews/software.md | A stale "Not changed" bullet | Deleted |
| btc/03 | 🔑 on a whole YouTube channel; the Chaincode curriculum has no "Proof of Work" section | Channel demoted; row renamed "Mining section" (README re-fetched); the core path is now *Mastering Bitcoin* Ch. 12 → Chaincode Mining. The channel also left btc/courses' 🔑 and btc/README's Key Resources. |
| btc/06 | A sourceless "Run your own full node" row kept 🔑 | 🔑 moved to *Mastering Bitcoin* Ch. 9 |
| btc/08 | Two of the three core items were sourceless concept rows | 🔑 moved to *Mastering Bitcoin* Ch. 13 and BIP 174 |

**Still unverifiable:**
- the Wittmann et al. *Science* DOI (the publisher page errored)
- the Lakatos chapter DOI (HTTP 429)
- the Edinburgh Coursera row (out of budget)
- Fraden's 5th-edition chapter numbers (Springer returned HTTP 429)

Two other findings were softened rather than verified: mlsysbook's "Volume I" framing, now just "two volumes, *Foundations* and *At Scale*", and the ml/08 corpus advice, which now says TinyStories is too small for the larger runs.
