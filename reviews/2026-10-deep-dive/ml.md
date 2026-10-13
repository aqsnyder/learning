# Machine Learning — Review

> **Deep-dive review, October 2026** · curriculum: [`ml/`](../../ml/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict
The ML curriculum has a good spine. It runs from history, math, and classical ML through NNs, CNNs, RNNs, transformers, generative models, scaling, LLMs, and RL to frontiers, interpretability, and AI for science. Its anchors are canonical: Karpathy, 3Blue1Brown, CS231n, the Annotated Transformer, Sutton & Barto, and the transformer-circuits arc. Sections 00–06 are mostly sound, with useful descriptions and suggested orders.

It falls short in three ways:
- **Accuracy in the flagship sections.** Section 12 had a fabricated lead author ("Burt et al."), an arXiv ID that points to an astronomy paper, and "Anthropic" credited in place of real authors. The ⭐ Ilya-list cross-reference was wrong in both directions: 3 papers were starred that are not on the list, and 11 list items were missing or unstarred. Section 01 cited the wrong Kolmogorov book and misspelled an author's name.
- **Currency.** Sections 09 (LLMs) and 10 (RL) stopped in 2023. The curriculum had no tokenization, instruction tuning, pretraining data, open-weight technical reports, or RL-for-reasoning (GRPO/RLVR).
- **Focus.** Sections 07–13 are bare link lists with no "why read this" descriptions, and 🔑 is inflated (8 of 16 in Section 08, 7 of 10 in Section 09).

**Overall grade: C+ as found (roughly B after this pass).** The single most important remaining improvement is to put 07–13 on the same descriptive table schema as 00–06 and cut 🔑 to a lean core path of 2–3 items per section. That would turn the link dump into a learning path.

*Scores below rate each section as I found it. ✔ = fixed in this pass, ✱ = suggested only.*

## Scorecard
| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 Historical Foundations | 3 | 4 | 4 | 4 | 4 | B- | Solid primary sources. Lacked Dartmouth, the Bitter Lesson, and any post-1986 history ✔ |
| 01 Math Foundations | 3 | 2 | 4 | 3 | 3 | C | Three of its four Ilya items were misidentified ✔. Duplicates the `math/` curriculum and had no info theory or matrix calculus ✔ |
| 02 Classical ML | 3 | 4 | 3 | 4 | 4 | B- | Good texts, but stale ISLR edition ✔. No boosting, GPs/kernels, or practical-wisdom reading ✔ |
| 03 NN Fundamentals | 3 | 4 | 3 | 4 | 4 | B- | Great hands-on core. No modern textbook and no training/debugging craft ✔ |
| 04 CNNs & Vision | 4 | 3 | 3 | 4 | 4 | B | Good arc to ViT. Wrong CS231n instructors, missing ⭐, no LeNet/U-Net/post-2021 work ✔ |
| 05 RNNs & Memory | 4 | 3 | 4 | 4 | 4 | B | Strong, but one false ⭐ and three missing Ilya items ✔ |
| 06 Transformers | 3 | 4 | 3 | 4 | 4 | B- | Classic 2017 transformer only: no RoPE or other modern components ✔. Bahdanau unstarred ✔ |
| 07 Generative Models | 3 | 3 | 3 | 4 | 3 | C+ | No descriptions. False ⭐ on flows ✔. Missing score-SDE, DiT, VQ-VAE ✔ |
| 08 Scaling & Deployment | 3 | 4 | 3 | 4 | 3 | C+ | No ZeRO/FSDP, μP, KV-cache serving, or quantization basics ✔. 🔑 inflation ✱ |
| 09 LLMs | 2 | 4 | 2 | 3 | 3 | C- | Nothing after 2023. No tokenization, data, instruction tuning, or open-model reports ✔ |
| 10 Reinforcement Learning | 3 | 4 | 2 | 4 | 4 | C+ | Good classical core. Missed the 2024–25 RL-for-reasoning shift and a hands-on deep-RL intro ✔ |
| 11 Frontiers | 3 | 4 | 3 | 2 | 3 | C+ | Thin on reasoning and agents. No VLA or open VLM ✔. No suggested order ✱ |
| 12 Interpretability & Alignment | 3 | 1 | 3 | 4 | 4 | D | Right arc, but fabricated/misattributed citations and broken numbering ✔. Missing key 2022–25 papers ✔ |
| 13 Graphs, Geometry & Science | 4 | 3 | 4 | 4 | 4 | B | Good. One unlinked or overstated row ✔, missing ⭐ on the MPNN paper ✔ |

## Section-by-section

### 00 — Historical Foundations
- **Strengths:** Real primary sources (Turing, McCulloch–Pitts, Rosenblatt, Minsky–Papert, Rumelhart et al.) and a good narrative entry point (Kurenkov). Sensible chronological order.
- **Problems:**
  - ✱ McCulloch–Pitts, Rosenblatt, and *Perceptrons* have no links. I couldn't add verified DOIs because Crossref was rate-limited.
  - ✱ "Contributing to the first AI winter" simplifies the history. The 1970s winter is usually tied to the Lighthill report and DARPA cuts; *Perceptrons* mainly chilled neural-net research.
  - ✱ The table isn't chronological.
- **Missing:** The founding of the field (Dartmouth). Any history after 1986: the 2006 deep-belief-net revival, the 2012 ImageNet moment as history, the scaling era. The "lessons of history" framing.
- **Added:**
  - A Proposal for the Dartmouth Summer Research Project on AI — McCarthy, Minsky, Rochester, Shannon — 1955
  - Deep Learning (Nature review) — LeCun, Bengio, Hinton — 2015
  - The Bitter Lesson — Rich Sutton — 2019 (🔑)

### 01 — Mathematical Foundations
- **Strengths:** 3Blue1Brown plus *Mathematics for Machine Learning* is the right on-ramp. It keeps the Ilya "compression" theory items together.
- **Problems:**
  - ✔ MML author "A. Aldo **Fehr**" → **Faisal**.
  - ✔ The Aaronson row conflated two essays ("Who Can Name the Bigger Number?" is a different 1999 essay). It is now "The First Law of Complexodynamics" (2011).
  - ✔ The Kolmogorov row named the wrong book: Li & Vitányi, not the Ilya item by Shen, Uspensky & Vereshchagin (AMS 2017). It now links the authors' free scan.
  - ✔ The Grünwald row was the 2007 book. The Ilya item is the 2004 tutorial (arXiv).
  - ✔ I moved the Ilya theory cluster into its own subsection with a "read after Sections 03–06" note.
  - ✔ I added cross-links to `math/` sections 01–05.
  - ✱ 3Blue1Brown linear algebra and calculus, StatQuest, Khan Academy, and MML are all duplicated in `math/` (see Structural observations).
- **Missing:** Information theory as used in ML (cross-entropy, KL). Matrix/vector calculus for backprop. Basic optimization (math/04 has it).
- **Added:**
  - The Matrix Calculus You Need For Deep Learning — Parr & Howard — 2018
  - Visual Information Theory — Christopher Olah — 2015
  - ⭐ Quantifying the Rise and Fall of Complexity in Closed Systems: The Coffee Automaton — Aaronson, Carroll, Ouellette — 2014
  - ⭐ Machine Super Intelligence (PhD thesis) — Shane Legg — 2008

### 02 — Classical Machine Learning
- **Strengths:** Ng plus ISLR plus scikit-learn is the right practical core. ESL and PRML serve as references.
- **Problems:**
  - ✔ ISLR was listed as the 2013 first edition. It is now the 2nd ed. (2021) plus ISLP, the Python edition (2023). Python labs suit Aaron's tooling.
  - ✔ PRML was marked paid with no link. It is a free PDF from Microsoft Research.
  - ✱ The Google ML Crash Course is redundant with Ng's course.
- **Missing:**
  - Gradient boosting, the default for tabular and sensor-feature data.
  - Kernels and Gaussian processes, and Bayesian methods beyond PRML.
  - Evaluation methodology: leakage, proper cross-validation, metrics.
  - Unsupervised learning is only implicit (ISLR chapter 12).
  - Time-series and signal features. These matter for test-and-measurement work (see the proposed Section 14).
- **Added:**
  - Gaussian Processes for Machine Learning — Rasmussen & Williams — 2006
  - A Few Useful Things to Know About Machine Learning — Pedro Domingos — 2012
  - XGBoost: A Scalable Tree Boosting System — Chen & Guestrin — 2016
  - Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? — Grinsztajn, Oyallon, Varoquaux — 2022

### 03 — Neural Network Fundamentals
- **Strengths:** Karpathy's Zero to Hero, 3Blue1Brown, and Nielsen are the best hands-on and intuition trio. The MDL thread (Hinton & van Camp) is a nice touch.
- **Problems:**
  - ✔ The Grünwald tutorial had no year or link (added 2004 + arXiv).
  - ✱ The Grünwald tutorial is duplicated in Section 01.
  - ✱ MIT 6.S191 is redundant given Zero to Hero plus Prince plus fast.ai.
  - ✱ Goodfellow (2016) shouldn't be the rigor reference any more; Prince's *Understanding Deep Learning* (UDL) is now better.
- **Missing:**
  - Practical training and debugging craft: baselines, overfit-first, learning-rate and batch-size tuning.
  - Initialization and normalization (covered only in Section 08 papers).
  - A modern unified textbook.
  - A top-down practical track.
- **Added:**
  - Understanding Deep Learning — Simon J. D. Prince — 2023 (🔑)
  - Practical Deep Learning for Coders — Jeremy Howard (fast.ai) — 2022
  - A Recipe for Training Neural Networks — Andrej Karpathy — 2019
  - Deep Learning Tuning Playbook — Godbole, Dahl, Gilmer, Shallue, Nado — 2023

### 04 — CNNs and Computer Vision
- **Strengths:** A clean architecture lineage (AlexNet → VGG → Inception → ResNet), plus Distill interpretability and the ViT transition.
- **Problems:**
  - ✔ CS231n (the 2017 playlist) was credited to "Fei-Fei Li, Karpathy, Johnson". The 2017 instructors were Li, Justin Johnson, and Serena Yeung.
  - ✔ CS231n is on Ilya's list but had no ⭐.
  - ✔ Broken prerequisite link.
  - ✱ Object detection is covered only by DETR; nothing from the R-CNN or YOLO families, which matter for embedded vision.
- **Missing:** The original CNN (LeNet). Segmentation and encoder–decoders. Post-2021 CNN work. Detection families. Self-supervised vision (lives in 11) and VLMs (11).
- **Added:**
  - Gradient-Based Learning Applied to Document Recognition (LeNet-5) — LeCun, Bottou, Bengio, Haffner — 1998
  - ⭐ Identity Mappings in Deep Residual Networks — He, Zhang, Ren, Sun — 2016
  - U-Net — Ronneberger, Fischer, Brox — 2015
  - A ConvNet for the 2020s (ConvNeXt) — Liu et al. — 2022

### 05 — RNNs, Sequences, and Memory
- **Strengths:** Excellent pairing of the primary paper (LSTM) with the best explainers (Olah, Karpathy). External-memory papers set up attention well.
- **Problems:**
  - ✔ Graves's "Generating Sequences with RNNs" was starred but is not on Ilya's list. I removed the ⭐ and added a note.
  - ✔ Pointer Networks was called a "key precursor to modern attention", but it postdates Bahdanau (2014). The description is reworded.
  - ✔ Broken prerequisite link.
- **Missing:** The Ilya items on sets, relational memory, and end-to-end speech. Vanishing/exploding gradients as an explicit concept (Bengio 1994; Pascanu 2013) ✱.
- **Added:**
  - ⭐ Relational Recurrent Neural Networks — Santoro et al. — 2018
  - ⭐ Order Matters: Sequence to Sequence for Sets — Vinyals, Bengio, Kudlur — 2015
  - ⭐ Deep Speech 2 — Amodei et al. — 2015

### 06 — Transformers and Attention
- **Strengths:** A textbook sequence: Bahdanau → Illustrated Transformer → paper → Annotated Transformer → build GPT.
- **Problems:**
  - ✔ Bahdanau is on Ilya's list but had no ⭐.
  - ✱ "Every frontier model today — GPT, BERT…" — BERT isn't a frontier model.
  - ✱ CS224n is the 2021 offering; newer offerings exist.
- **Missing:**
  - The modern decoder recipe: RoPE, pre-norm/RMSNorm, SwiGLU, grouped-query attention, KV cache.
  - A precise specification to check implementations against.
  - Tokenization (now covered in Section 09).
- **Added:**
  - Formal Algorithms for Transformers — Phuong & Hutter — 2022
  - RoFormer / Rotary Position Embedding — Su et al. — 2021

### 07 — Generative Models
- **Strengths:** Good core: VAE → GAN → flows → DDPM → latent diffusion → flow matching → classifier-free guidance.
- **Problems:**
  - ✔ "Variational Inference with Normalizing Flows" was starred but is not on Ilya's list (the Ilya item is the *Variational Lossy Autoencoder*). ⭐ removed.
  - ✔ Two broken prerequisite links, with wrong section names.
  - ✱ The table has no description column.
  - ✱ "Distill.pub" is a generic journal link, not a resource.
- **Missing:**
  - Score-based / SDE view of diffusion.
  - Transformer backbones (DiT), the basis of current image and video models.
  - Discrete latents (VQ-VAE) and autoregressive image generation.
  - Video generation.
  - A modern course covering flow matching.
- **Added:**
  - ⭐ Variational Lossy Autoencoder — Chen et al. — 2016
  - VQ-VAE (Neural Discrete Representation Learning) — van den Oord, Vinyals, Kavukcuoglu — 2017
  - Score-Based Generative Modeling through SDEs — Song et al. — 2020
  - DiT: Scalable Diffusion Models with Transformers — Peebles & Xie — 2022
  - MIT 6.S184: Introduction to Flow Matching and Diffusion Models — Holderrieth & Erives — 2025

### 08 — Scaling, Efficiency, and Deployment
- **Strengths:** Good selection of scaling laws (Kaplan, Chinchilla), optimizers, mixture-of-experts, FlashAttention, LoRA/QLoRA, distillation, and speculative decoding.
- **Problems:**
  - ✔ Two broken prerequisite links.
  - ✱ 8 of 16 items carried 🔑. That isn't "absolute priority"; suggest Kaplan, Chinchilla, Adam, and FlashAttention only.
  - ✱ No descriptions.
  - ✱ The folder name `08-scaling-and-training` doesn't match the title "Scaling, Efficiency, and Deployment".
- **Missing:**
  - Optimizer-state and parameter sharding (ZeRO/FSDP).
  - Hyperparameter transfer across scale (μP).
  - Inference serving and KV-cache memory.
  - Quantization fundamentals (int8). These are the bridge to edge deployment.
  - A practical end-to-end parallelism guide.
  - ✱ Watch item: the Muon optimizer (2025) is the first serious challenger to AdamW at scale. Not added; consider once it settles.
- **Added:**
  - ZeRO — Rajbhandari et al. — 2019
  - μP / Tensor Programs V — Yang et al. — 2022
  - The Ultra-Scale Playbook: Training LLMs on GPU Clusters — Hugging Face (Nanotron) — 2025
  - PagedAttention / vLLM — Kwon et al. — 2023
  - Quantization and Training of NNs for Efficient Integer-Arithmetic-Only Inference — Jacob et al. — 2017

### 09 — Large Language Models
- **Strengths:** Karpathy's two LLM videos are the right entry. The GPT-2 → 3 → 4 lineage and InstructGPT are canonical.
- **Problems:**
  - ✔ Broken prerequisite links and labels.
  - ✱ 7 of 10 items carried 🔑.
  - ✱ The "Anthropic Research Blog" row is a blog index, duplicated in `blogs-and-references/`.
  - ✱ InstructGPT's RLHF comes before Section 10 teaches RL.
- **Missing (as found):**
  - Tokenization.
  - Pretraining data curation.
  - Instruction tuning.
  - Building an LLM end to end.
  - Any open-weight model report after LLaMA-1 (Feb 2023).
  - Evaluation (now pointed to 11/12).
  - Embeddings and retrieval (added to 11).
- **Added:**
  - Let's build the GPT Tokenizer — Karpathy — 2024
  - Let's reproduce GPT-2 (124M) — Karpathy (video)
  - FLAN: Finetuned Language Models Are Zero-Shot Learners — Wei et al. — 2021
  - The FineWeb Datasets — Penedo et al. — 2024
  - The Llama 3 Herd of Models — Grattafiori et al. (Meta) — 2024
  - DeepSeek-V3 Technical Report — DeepSeek-AI — 2024
  - Stanford CS336: Language Modeling from Scratch — Hashimoto & Liang — 2025

### 10 — Reinforcement Learning
- **Strengths:** Sutton & Barto plus Silver's course is the classic core. DQN → PPO → AlphaGo is the right deep-RL arc. A separate "RL for language models" table is a good idea.
- **Problems:**
  - ✔ Broken prerequisite link.
  - ✔ The "RL for LMs" intro didn't mention RL for reasoning.
  - ✱ DPO and Christiano are duplicated in Section 12.
  - ✱ SPIN is minor.
  - ✱ DDPG is the only continuous-control method; SAC/TD3 are now the standard ones.
- **Missing (as found):**
  - A hands-on deep-RL implementation guide.
  - Process vs. outcome rewards.
  - GRPO.
  - RL with verifiable rewards (RLVR), the recipe behind o1/R1-style reasoning.
  - An up-to-date post-training reference.
  - ✱ Model-based RL (MuZero, DreamerV3).
- **Added:**
  - Spinning Up in Deep RL — Josh Achiam (OpenAI) — 2018
  - Let's Verify Step by Step — Lightman et al. — 2023
  - DeepSeekMath (introduces GRPO) — Shao et al. — 2024
  - Tülu 3 (introduces RLVR) — Lambert et al. — 2024
  - Reinforcement Learning from Human Feedback (RLHF Book) — Nathan Lambert — 2025

### 11 — Frontiers
- **Strengths:** Good topical subsections: reasoning, multimodal, self-supervised, alternative architectures, agents, robotics. The self-supervised and state-space-model tables are solid.
- **Problems:**
  - ✔ The reasoning paragraph said reasoning models "shift compute from training to inference". They actually rely on large-scale RL training plus test-time scaling. Rewritten.
  - ✔ Noted that "Sparks of AGI" (🔑) is a capabilities evaluation, not an agents paper.
  - ✱ No Suggested Order.
  - ✱ The Gemini 1.0 report (2023) is dated as "the frontier".
  - ✱ The DINOv2 link is missing (the row links only DINO).
- **Missing:**
  - The reasoning-model announcement itself.
  - Agent design patterns and agent benchmarks.
  - Embeddings for retrieval.
  - An open VLM recipe.
  - A modern vision-language-action (VLA) robot policy.
  - ✱ World models (Genie/DreamerV3).
  - ✱ Long-context work.
  - ✱ Computer-use benchmarks such as OSWorld.
- **Added:**
  - Learning to Reason with LLMs (o1) — OpenAI — 2024
  - LLaVA: Visual Instruction Tuning — Liu et al. — 2023
  - Sentence-BERT — Reimers & Gurevych — 2019
  - Building Effective Agents — Schluntz & Zhang (Anthropic) — 2024
  - SWE-bench — Jimenez et al. — 2023
  - π0: A Vision-Language-Action Flow Model — Black et al. — 2024

### 12 — Interpretability and Alignment
- **Strengths:** The right intellectual arc (circuits → superposition → monosemanticity → full-model biology). It includes the 2026 global-workspace paper, which I verified: Gurnee*, Sofroniew*, …, Lindsey*†, published 6 July 2026.
- **Problems:**
  - ✔ "Scaling Monosemanticity — **Burt et al.**" → **Templeton et al.** (2024), with the full title.
  - ✔ CoT Monitorability linked **arXiv 2503.07972** (an astronomy paper, "2005 VL1 is not Venera-2") and credited "Baker, Korbak". Correct: **arXiv 2507.11473**, Korbak, Balesni et al. (2025). Bowen Baker is a late author.
  - ✔ "On the Biology of a Large Language Model" credited "Anthropic" and linked only the site homepage. Correct: **Lindsey et al.** (2025), linked to the paper page.
  - ✔ Softmax Linear Units credited "Anthropic" → **Elhage et al.** (2022).
  - ✔ Row numbering had #9 in two tables. Renumbered 1–26.
  - ✔ The prerequisite label said "LLMs and Language".
  - ✔ The Section 12 entries in PROGRESS carried the same errors.
  - ✱ DPO and Christiano duplicate Section 10.
  - ✱ Bostrom and Russell duplicate `philosophy/07`.
  - ✱ No description column.
- **Missing (as found):**
  - In-context learning and induction heads.
  - The one-layer sparse-autoencoder precursor (Towards Monosemanticity).
  - The circuit-tracing / attribution-graph methods paper.
  - Hands-on exercises.
  - Empirical misalignment results (alignment faking, emergent misalignment).
  - The control agenda.
  - Capability-trend evaluation (METR time horizons).
  - ✱ Concrete Problems in AI Safety (2016).
  - ✱ Weak-to-strong generalization.
  - ✱ Open Problems in Mechanistic Interpretability (2025).
- **Added:**
  - In-context Learning and Induction Heads — Olsson et al. — 2022
  - Towards Monosemanticity — Bricken et al. — 2023
  - Circuit Tracing: Revealing Computational Graphs in Language Models — Ameisen et al. — 2025
  - ARENA self-study curriculum — Callum McDougall / ARENA — ongoing
  - Alignment Faking in Large Language Models — Greenblatt et al. — 2024
  - Emergent Misalignment — Betley et al. — 2025
  - AI Control: Improving Safety Despite Intentional Subversion — Greenblatt, Shlegeris, Sachan, Roger — 2023
  - Measuring AI Ability to Complete Long Tasks (METR) — Kwa et al. — 2025

### 13 — Graphs, Geometry, and Science
- **Strengths:** A clean GNN → equivariance → AI-for-science arc with landmark papers.
- **Problems:**
  - ✔ Gilmer et al. (MPNN) is on Ilya's list but had no ⭐.
  - ✔ The "AlphaProof & AlphaGeometry — Google DeepMind 2024" row had no link and no authors. It now names Trinh et al. (Nature 2024) and Hubert et al. (Nature, online Nov 2025) with links.
  - ✔ "GNoME discovered millions of new stable materials" overstated the paper. It reported 2.2M structures below the hull and 381k new stable entries.
  - ✔ "GraphCast forecasts in seconds" → "in under a minute", per the abstract.
  - ✱ Heavy overlap with `bio/10`, `bio/07`, `physics/11`, and `math/06` (AlphaFold, RFdiffusion, EGNN, GCN, Bronstein).
- **Missing:**
  - An intuitive GNN entry point.
  - Relation Networks (Ilya list).
  - LLM-driven algorithm discovery.
  - ✱ Neural operators (FNO), which belong in `physics/11`.
  - ✱ Probabilistic weather (GenCast).
  - ✱ The Stanford CS224W course.
- **Added:**
  - A Gentle Introduction to Graph Neural Networks — Sanchez-Lengeling, Reif, Pearce, Wiltschko — 2021
  - ⭐ A Simple Neural Network Module for Relational Reasoning — Santoro et al. — 2017
  - AlphaEvolve: A Coding Agent for Scientific and Algorithmic Discovery — Novikov et al. — 2025

### books/
- **Strengths:** A good mix of free classics with levels and free/paid flags.
- **Problems:**
  - ✔ Years were blank or stale for Nielsen, ISLR, MML, and Sutton & Barto.
  - ✔ Bishop & Bishop was marked "Paid" but is free to read online.
  - ✔ PRML was marked "Paid" but is a free PDF.
  - ✔ Chollet was the old edition; the 3rd ed. (2025, with Watson) is free online.
  - ✔ Géron is now the 2025 PyTorch edition.
  - ✱ No 🔑 core reading order across books.
- **Added:**
  - Understanding Deep Learning — Prince — 2023
  - Dive into Deep Learning — Zhang, Lipton, Li, Smola — 2023
  - Gaussian Processes for ML — Rasmussen & Williams — 2006
  - Speech and Language Processing (3rd ed. draft) — Jurafsky & Martin — 2026 draft
  - Build a Large Language Model (From Scratch) — Raschka — 2024
  - RLHF Book — Lambert — 2025

### courses/
- **Strengths:** "Pairs With" column is useful.
- **Problems:**
  - ✔ CS231n credited to Fei-Fei Li only.
  - ✱ oEmbed lookups for the CS224n, CS229, and CS234 playlists returned client errors. Flagged to the URL audit; they may be private or moved.
  - ✱ No newer CS224n or CS231n offerings.
- **Added:**
  - fast.ai Practical Deep Learning — Howard — 2022
  - Let's reproduce GPT-2 (124M) — Karpathy
  - CS336 — Hashimoto & Liang — 2025
  - MIT 6.S184 — Holderrieth & Erives — 2025
  - Spinning Up — Achiam — 2018
  - ARENA — McDougall

### blogs-and-references/
- **Problems:**
  - ✔ Papers With Code was described as live. Meta sunset it on 24–25 July 2025; Hugging Face Trending Papers is the replacement.
  - ✔ Distill.pub was described as an active journal. It has been on indefinite hiatus since July 2021.
  - ✱ Sebastian Ruder's blog is now low-frequency.
  - ✱ No safety community sources (Alignment Forum).
- **Added:**
  - Transformer Circuits Thread — Anthropic interpretability team
  - Interconnects — Nathan Lambert
  - Epoch AI — trends and data

### PROGRESS.md
- **Problems:**
  - ✔ It mirrored the Section 12 errors (Burt, Anthropic ×2, Baker/Korbak) and the false ⭐ on Graves and Rezende.
  - ✔ It lacked ⭐ on Bahdanau, Gilmer, and CS231n.
  - ✔ It was missing items that exist in the sections: Network In Network, Building Blocks of Interpretability, The Illustrated BERT, DDPG.
  - ✔ It credited DINOv2 to Caron (it is Oquab et al.).
  - ✱ No core-path view and no per-section counts.
  - ✱ Duplicates: the Grünwald tutorial (01/03), the 3Blue1Brown NN playlist (01/03), DPO and Christiano (10/12).
- **Added:** Checkbox lines for every addition above, in "Author — Title (Year)" style.

### README.md
- **Problems:**
  - ✔ The ⭐ cross-reference table had 19 rows. Three weren't on the list (Graves 2013, Seq2Seq, Normalizing Flows) and 11 list items were missing: Order Matters, MPNN, Bahdanau, Identity Mappings, Relation Networks, VLAE, Relational RNNs, Coffee Automaton, Deep Speech 2, Legg, CS231n. Rebuilt as the 27-item list in source order, with a note on the three non-list papers.
  - ✱ The legend's "~30 paper list" is fine; the published reconstruction has 27 items.
  - The learning-path list matches the section titles; no change needed.

## Corrections made
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| ml/01-math-foundations/README.md:24 | "A. Aldo Fehr" | "A. Aldo Faisal" | https://mml-book.github.io/ |
| ml/01-math-foundations/README.md:36 | ⭐ "Who Can Name the Bigger Number? (First Law of Complexodynamics)", year — | ⭐ "The First Law of Complexodynamics", 2011, accurate description | https://scottaaronson.blog/?p=762 |
| ml/01-math-foundations/README.md:38 | ⭐ Book "The Minimum Description Length Principle" (2007), no link | ⭐ Tutorial "A Tutorial Introduction to the MDL Principle" (2004), arXiv link; book noted as follow-up | https://arxiv.org/abs/math/0406077 |
| ml/01-math-foundations/README.md:39 | ⭐ "An Introduction to Kolmogorov Complexity and Its Applications" (Li & Vitányi) | ⭐ "Kolmogorov Complexity and Algorithmic Randomness" (Shen, Uspensky, Vereshchagin, AMS 2017), free scan | https://www.lirmm.fr/~ashen/kolmbook-eng-scan.pdf · https://github.com/dzyim/ilya-sutskever-recommended-reading |
| ml/02-classical-ml/README.md:21 | ISLR, 2013 | ISLR 2nd ed. (2021) / ISLP Python ed. (2023) | https://www.statlearning.com/ |
| ml/02-classical-ml/README.md:22 | PRML "Book", no link | "Book (Free)", Microsoft Research PDF | https://www.microsoft.com/en-us/research/publication/pattern-recognition-machine-learning/ |
| ml/03-neural-network-fundamentals/README.md:24 | Grünwald tutorial year "—", link "—" | 2004, arXiv link, cross-ref to 01 | https://arxiv.org/abs/math/0406077 |
| ml/04-cnns-and-computer-vision/README.md:11 | link ../03-deep-learning-fundamentals/ ("Deep Learning Fundamentals") | ../03-neural-network-fundamentals/ ("Neural Network Fundamentals") | (repo) |
| ml/04-cnns-and-computer-vision/README.md:28 | CS231n "Fei-Fei Li, Karpathy, Johnson", 🔑 | "Fei-Fei Li, Justin Johnson, Serena Yeung", 🔑⭐ | http://cs231n.stanford.edu/2017/ |
| ml/05-rnns-sequences-and-memory/README.md:9 | broken link to 03-deep-learning-fundamentals | 03-neural-network-fundamentals | (repo) |
| ml/05-rnns-sequences-and-memory/README.md:28 | Pointer Networks "Key precursor to modern attention mechanisms" | "repurposing of (Bahdanau-style) attention… basis of copy/pointer mechanisms" | https://arxiv.org/abs/1506.03134 |
| ml/05-rnns-sequences-and-memory/README.md:30 | ⭐ Graves 2013 | no ⭐ + note "not on the list" | https://github.com/dzyim/ilya-sutskever-recommended-reading |
| ml/06-transformers-and-attention/README.md:27 | Bahdanau unstarred | ⭐ | same |
| ml/07-generative-models/README.md:5 | links to 03-neural-network-foundations and 06-attention-and-transformers | 03-neural-network-fundamentals and 06-transformers-and-attention (labels fixed) | (repo) |
| ml/07-generative-models/README.md:16 | ⭐ Normalizing Flows | no ⭐ | dzyim list |
| ml/08-scaling-and-training/README.md:5 | same two broken links | fixed + labels | (repo) |
| ml/09-llms-and-language/README.md:5 | link to 06-attention-and-transformers; label "Scaling and Training" | fixed; label "Scaling, Efficiency, and Deployment" | (repo) |
| ml/10-reinforcement-learning/README.md:5 | link to 03-neural-network-foundations | fixed | (repo) |
| ml/11-frontiers/README.md (Reasoning para) | "Reasoning-focused models shift compute from training to inference" | RL-trained long chain-of-thought plus test-time scaling, with cross-ref to Section 10 | https://openai.com/index/learning-to-reason-with-llms/ |
| ml/12-interpretability-and-alignment/README.md:20 | "Scaling Monosemanticity — Burt et al." | "Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet — Templeton et al." | https://transformer-circuits.pub/2024/scaling-monosemanticity/ |
| ml/12-interpretability-and-alignment/README.md:22 | Biology — "Anthropic", link = site homepage | "Lindsey et al.", paper URL | https://transformer-circuits.pub/2025/attribution-graphs/biology.html |
| ml/12-interpretability-and-alignment/README.md:24 | Softmax Linear Units — "Anthropic" | "Elhage et al." | https://transformer-circuits.pub/2022/solu/index.html |
| ml/12-interpretability-and-alignment/README.md:44 | CoT Monitorability — "Baker, Korbak et al.", arXiv 2503.07972 (astronomy) | "Korbak, Balesni et al.", arXiv 2507.11473 | https://arxiv.org/abs/2507.11473 |
| ml/12-interpretability-and-alignment/README.md (all tables) | duplicate row numbers (#9 twice) | sequential 1–26 | — |
| ml/12-interpretability-and-alignment/README.md:5 | prereq label "LLMs and Language" | "Large Language Models" | (repo) |
| ml/13-graphs-geometry-and-science/README.md:18 | MPNN unstarred | ⭐ | dzyim list |
| ml/13-graphs-geometry-and-science/README.md:46 | "AlphaProof & AlphaGeometry — Google DeepMind — 2024 — (no link)" | Full titles; Trinh et al. (2024) / Hubert et al. (2025); Nature links | https://www.nature.com/articles/s41586-023-06747-5 · https://www.nature.com/articles/s41586-025-09833-y |
| ml/13-graphs-geometry-and-science/README.md:37 | "GNoME discovered millions of new stable materials"; "GraphCast… in seconds" | "2.2M structures below the hull (381k new stable; 736 synthesized)"; "in under a minute" | https://www.nature.com/articles/s41586-023-06735-9 · https://arxiv.org/abs/2212.12794 |
| ml/README.md:61–91 | 19-row ⭐ table (3 non-list items, 11 missing) | 27-row table in source order + note | https://github.com/dzyim/ilya-sutskever-recommended-reading |
| ml/blogs-and-references/README.md:10 | Distill described as active | "On indefinite hiatus since July 2021" | https://distill.pub/2021/distill-hiatus/ |
| ml/blogs-and-references/README.md:50 | Papers With Code described as live | "Sunset by Meta in July 2025 → HF Trending Papers" | https://hyper.ai/en/news/42900 · https://huggingface.co/papers/trending |
| ml/books/README.md:10 | Bishop & Bishop "Paid", no link | "Free (online)", bishopbook.com | https://www.bishopbook.com/ |
| ml/books/README.md:15 | Chollet, no year/edition, Paid | 3rd ed. 2025 (Chollet & Watson), free online | https://deeplearningwithpython.io/ |
| ml/books/README.md:16 | "Hands-On Machine Learning", no year | "…with Scikit-Learn and PyTorch" (Oct 2025) | https://www.oreilly.com/library/view/hands-on-machine-learning/9798341607972/ |
| ml/books/README.md:7–9,14,17 | years blank (Nielsen, ISLR, MML, Sutton & Barto, ESL); PRML "Paid" | filled; PRML Free | https://openlibrary.org/isbn/9780262039246.json (S&B 2018) and the URLs above |
| ml/courses/README.md:13 | CS231n "Fei-Fei Li" | "Fei-Fei Li, Justin Johnson, Serena Yeung"; ⭐ noted | http://cs231n.stanford.edu/2017/ |
| ml/PROGRESS.md (Sections 01, 04–07, 11–13) | Burt; Anthropic ×2; Baker/Korbak; ⭐ on Graves/Rezende; no ⭐ on Bahdanau/Gilmer/CS231n; wrong Kolmogorov/Aaronson/MML details; DINOv2 credited to Caron; missing NiN, Building Blocks, Illustrated BERT, DDPG | All corrected and synced | as above |

## Proposed new sections (not created)

### Section 14 — Edge & Embedded ML (TinyML)
- **Position:** Section 14, after 13, so nothing is renumbered. Conceptually it follows 08 (quantization and distillation). Prerequisites: 02, 04, and 08.
- **Why:** Aaron builds STM32 and embedded-C test-and-measurement hardware. The curriculum stops at datacenter-scale deployment. Nothing covers running a model in kilobytes of SRAM, toolchains for Cortex-M, sensor and time-series ML, or measuring on-target latency and energy. This is where ML meets his products, and his instrumentation skills are an advantage there.
- **Outline:**
  1. Why on-device: latency, power, privacy, bandwidth. MCU constraints: SRAM/flash budgets, fixed-point, DSP and NPU blocks.
  2. Classical first: feature extraction from sensor and time-series signals (filters, FFT, statistics) plus small tree ensembles. When a model of a few kilobytes is enough.
  3. Compression: int8 post-training quantization and quantization-aware training, pruning, distillation, and efficient architectures (depthwise-separable convolutions).
  4. Runtimes and toolchains: TFLite Micro / LiteRT, CMSIS-NN, ST Edge AI / STM32Cube.AI. Memory planning and peak-SRAM analysis.
  5. Hardware-aware model design (MCUNet / TinyNAS).
  6. Benchmarking and validation: MLPerf Tiny, on-target vs. desktop accuracy, latency and energy measurement, test fixtures.
  7. Capstone: keyword spotting or IMU event classification on an STM32 dev board, end to end.
- **Verified resources:**
  1. Jacob et al. — Quantization and Training of NNs for Efficient Integer-Arithmetic-Only Inference (2017) — https://arxiv.org/abs/1712.05877 (added to 08)
  2. Lai, Suda, Chandra — CMSIS-NN: Efficient Neural Network Kernels for Arm Cortex-M CPUs (2018) — https://arxiv.org/abs/1801.06601
  3. Lin, Chen, Lin, Cohn, Gan, Han — MCUNet: Tiny Deep Learning on IoT Devices (2020) — https://arxiv.org/abs/2007.10319
  4. Hinton, Vinyals, Dean — Distilling the Knowledge in a Neural Network (2015) — https://arxiv.org/abs/1503.02531 (already in 08)
  5. Grinsztajn, Oyallon, Varoquaux — Why Do Tree-Based Models Still Outperform Deep Learning on Tabular Data? (2022) — https://arxiv.org/abs/2207.08815 (added to 02; the sensor-feature baseline)
  6. Chen & Guestrin — XGBoost (2016) — https://arxiv.org/abs/1603.02754 (added to 02; tiny deployable models)
- **Unverified candidates.** The WebFetch budget ran out before I could check these; verify before adding.
  - David et al., "TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems" (arXiv 2010.08678). Fetch was rate-limited.
  - Banbury et al., "MLPerf Tiny Benchmark" (arXiv 2106.07597).
  - Warden & Situnayake, *TinyML* (O'Reilly, 2019). Fetch was rate-limited.
  - MIT 6.5940 "TinyML and Efficient Deep Learning Computing" (Song Han, efficientml.ai).
  - ST Edge AI Core / STM32Cube.AI documentation (st.com).
  - Gholami et al., "A Survey of Quantization Methods for Efficient NN Inference" (arXiv 2103.13630).

*(A second idea, "ML Systems in Practice: data, evaluation, deployment, LLM-app evals", is noted under Structural observations rather than proposed formally. Most of its verified resources are now placed in 02, 03, 09, 11, and 12, and the remaining candidates — Huyen's two O'Reilly books, Sculley et al.'s "Hidden Technical Debt", Zinkevich's "Rules of ML", Husain's eval posts — couldn't be verified this session.)*

## Cut candidates
- **07 #8 "Distill.pub"**: a generic link to a journal on hiatus, already listed in blogs/. Not a study item.
- **09 #10 "Anthropic Research Blog"**: a blog index, duplicated in blogs/.
- **03 Grünwald MDL tutorial row**: duplicates 01's theory cluster. Keep one home (01), and the same applies in PROGRESS.
- **12 #15–16 DPO and Christiano et al.**: duplicate Section 10. Keep them in 10 and cross-reference from 12.
- **12 #22–23 Bostrom and Russell**: duplicated in `philosophy/07-existential-risk-and-alignment`. Keep them there and add a cross-link.
- **01 3Blue1Brown linear algebra and calculus, Khan Academy, StatQuest**: duplicated in `math/01–03`. Convert to cross-links, keeping MML, Matrix Calculus, Visual Information Theory, and the Ilya cluster.
- **01 / 03 3Blue1Brown "Neural Networks" playlist**: listed in both sections; keep it in 03.
- **10 #13 SPIN**: minor self-play fine-tuning method, superseded in practice by DPO variants and RLVR.
- **03 MIT 6.S191**: redundant with Zero to Hero, UDL, and fast.ai.
- **02 Google ML Crash Course**: redundant with Ng's course.
- **11 Sparks of AGI (🔑)**: hype-heavy, and an evaluation study misfiled under agents. Demote from 🔑 and move to 12's Evaluation table.
- **11 Gemini (2023)**: not "the frontier" any more. Replace with a current multimodal technical report when updating.

## Structural observations
- **Three table schemas.**
  - 00–06 use Priority/Type/Resource/Author/Year/Link/Description, which works best.
  - 07–11 use #/Resource/Type/Marking/Link, with no authors column and no descriptions.
  - 12–13 use #/Priority/Type/Resource/Author/Year/Link, with no descriptions.
  
  Without a description column, half the curriculum can't tell the reader why to read anything. Unify on the 00–06 schema. This is the top structural fix.
- **Legend blocks are inconsistent.** 04–06 have a "Marking Convention" table, 07–13 a footer, and 00–03 nothing.
- **🔑 inflation.** 08 had 8 of 16, 09 had 7 of 10, 12 has 7 of 26. The README defines 🔑 as "absolute priority". Suggest at most 2–3 per section, and a one-page "core path" in the README that strings the 🔑 items into a ~40-item minimum route.
- **Sequencing.**
  - 09 teaches RLHF (InstructGPT) before 10 teaches RL. Add an explicit "read 10's 'RL for LMs' after 09" note, or move the RLHF items into 10.
  - 12 depends on 09 and 10.
  - 11 has no Suggested Order.
  - 01's Ilya theory cluster sits before readers have trained anything (now flagged in-text).
- **Overlap with other curricula.**
  - `math/01–05`: duplicates 01's 3Blue1Brown, MML, StatQuest, and Khan. `ml/01` should become a thin bridge pointing into math, keeping only ML-specific items.
  - `philosophy/07`: Bostrom and Russell.
  - `bio/10-ai-for-biology` and `bio/07`: AlphaFold 2/3, RFdiffusion, Bronstein.
  - `physics/11-physics-informed-ml-and-frontiers`: AlphaFold, EGNN. PINNs and neural operators should live there.
  - `math/06` and `math/08`: GCN and Bronstein.
  - `software/09-agentic-ai-workflows`: complements 11's research-side agent papers. "Building Effective Agents" and the Model Context Protocol arguably belong in software/09 too.
  
  Each overlap should have one home and cross-links.
- **Missing standard parts.**
  - No projects/practice track (added in this review: every section now has Practice blocks).
  - No "how to read a paper" guidance.
  - No glossary.
  - No ML-engineering/MLOps coverage: data versioning, evals for LLM apps, monitoring.
- **Names.**
  - The folder `08-scaling-and-training` doesn't match its title "Scaling, Efficiency, and Deployment".
  - 12's prerequisite labels were inconsistent with section titles (fixed).
- **Agent skill (`.agents/skills/update-curriculum/SKILL.md`).** This is the likely root cause of the hallucinated citations.
  - (a) There is no verification step. Add: "fetch the arXiv abs/DOI/official page; confirm exact title, author order, and year; never invent a URL; never credit an organization when authors are listed."
  - (b) "When in doubt… err on the side of inclusion" contradicts curation and drives padding. Change it to "when in doubt, leave it out and list it in the summary".
  - (c) The Section Mapping table omits 00–05, 12, and 13, so interpretability and safety papers have no target. Add "Interpretability/alignment/evals → 12; GNN/science → 13".
  - (d) There are no per-section schema instructions, no instruction to update Suggested Order, and no instruction to keep row numbering unique.
  - (e) It treats the Ilya list as possibly growing. State that it is a fixed 27-item list (cite the dzyim repo) and that ⭐ must never be added elsewhere.
  - (f) Its search recipe ("most important AI papers [year]") surfaces hype. Prefer conference best-paper lists, lab research pages, Epoch AI, and citation velocity.
  
  These rules were then applied repo-wide: every `update-curriculum` skill now carries the same Verification & Curation Rules, and the root `audit-curriculum` skill covers all nine curricula.
- **Verification notes.**
  - The WebSearch budget (200/turn) and the WebFetch budget (800/hour, shared) ran out mid-task.
  - Pages I could not read:
    - vetta.org (robots.txt). For Legg's thesis I used a verified mirror PDF (pdf.stafforini.com); the URL audit may prefer the author's vetta.org copy.
    - incompleteideas.net (robots.txt). The Bitter Lesson URL was verified via Wikipedia's citation.
    - mitpress.mit.edu (robots.txt). The UDL year and publisher were verified via Open Library.
    - O'Reilly *TinyML* and arXiv 2010.08678 (rate-limited).
  - YouTube oEmbed for the CS224n, CS229, and CS234 playlists returned client errors; flagged to the URL audit.

## Top 5 priorities for Aaron in this curriculum
1. **Walk a lean core path first.**
   - 3Blue1Brown → Karpathy Zero to Hero with Prince's *UDL* as the text (03).
   - ResNet and CS231n (04).
   - Attention Is All You Need, the Annotated Transformer, and "Let's build GPT" (06).
   - Karpathy's Deep Dive, then "Let's reproduce GPT-2" (09).
   - The RL-for-reasoning trio: Let's Verify → GRPO → RLVR (10).
   - The interpretability arc with ARENA exercises (12).
   
   Skip most non-🔑 items until something pulls you there.
2. **Do the tabular and sensor track early.** Read Domingos, the ISLP labs, XGBoost, and Grinsztajn (02). For test-and-measurement data, boosted trees on good features will usually beat a neural net. Know that before reaching for deep learning.
3. **Get a model onto an STM32.** Read Jacob et al. on int8 quantization and Hinton on distillation (08). The proposed Section 14 (Edge & Embedded ML) would give this path a home; it's in the review backlog until its remaining resources are verified.
4. **Fix the format of 07–13 next time you touch them.** Add the description column, trim 🔑 to 2–3 per section, and add a Suggested Order to 11. This matters more for learning value than adding more papers.
5. **Fix the update skill before running it again.** Add the verification step, remove "err on the side of inclusion", and state that the Ilya list is a fixed 27 items. Otherwise each refresh of Section 11 will reintroduce the citation errors cleaned up in this pass.
