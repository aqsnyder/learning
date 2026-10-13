# Frontiers (2023-2026+)

> This section is a living document. Use the `.agents/skills/update-curriculum` skill to search for and add new important papers and resources.

The frontier of ML research moves fast. This section collects the most impactful recent work across reasoning, multimodality, self-supervised learning, alternative architectures, agentic AI, robotics, and ecosystem-level reports. Revisit regularly.

---

## 🎯 Learning Objectives

After this section you can:
- Map the frontier into its main threads — test-time compute and RL-trained reasoning, multimodal and self-supervised representation learning, subquadratic sequence models, agents, embodied AI — and state each listed paper's core idea and its strongest evidence in one or two sentences.
- Explain the test-time-compute tradeoff (parallel sampling with verifiers vs. sequential revision) and DeepSeek-R1-Zero's recipe (GRPO with rule-based rewards), and reproduce a small version of each.
- Compare contrastive (CLIP, SimCLR, MoCo), self-distillation (DINO) and masked-prediction (MAE, I-JEPA) objectives, including how each avoids representational collapse.
- Derive the recurrence/convolution duality of a discretized linear state-space model (S4), and explain what Mamba's input-dependent selection breaks and how its parallel scan recovers speed.
- Judge frontier claims by separating demonstrated results from extrapolation, and write falsifiable predictions with resolution dates.

---

## Reasoning and Test-Time Compute

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Scaling LLM Test-Time Compute – Snell et al. (2024) | Paper | 🔑 | [arxiv.org/abs/2408.03314](https://arxiv.org/abs/2408.03314) |
| 2 | DeepSeek-R1 (2025) | Paper | 🔑 | [arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948) |
| 3 | Learning to Reason with LLMs (o1) – OpenAI (2024) | Blog | | [openai.com](https://openai.com/index/learning-to-reason-with-llms/) |

Reasoning models are trained with large-scale reinforcement learning to think in long chains of thought, and their accuracy keeps improving as they are allowed more inference-time compute. OpenAI's o1 announcement introduced the paradigm. Snell et al. formalizes when test-time compute scaling beats simply training a larger model. DeepSeek-R1 openly demonstrated reinforcement-learning-driven chain-of-thought at scale (for the RL recipes behind it — GRPO and RL with verifiable rewards, plus the process-reward alternative it did not adopt — see [Section 10](../10-reinforcement-learning/README.md)).

---

## Multimodal Models

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Gemini – Google DeepMind (2023) | Paper | 🔑 | [arxiv.org/abs/2312.11805](https://arxiv.org/abs/2312.11805) |
| 2 | SAM – Kirillov et al. (2023) | Paper | | [arxiv.org/abs/2304.02643](https://arxiv.org/abs/2304.02643) |
| 3 | CLIP – Radford et al. (2021) | Paper | | [arxiv.org/abs/2103.00020](https://arxiv.org/abs/2103.00020) |
| 4 | LLaVA: Visual Instruction Tuning – Liu et al. (2023) | Paper | | [arxiv.org/abs/2304.08485](https://arxiv.org/abs/2304.08485) |

Multimodal models unify vision, language, and other modalities into a single architecture. CLIP pioneered contrastive image-text pretraining, SAM brought foundation-model thinking to segmentation, LLaVA showed the simple open recipe (vision encoder + projection + LLM, trained on visual instruction data) that most open vision-language models still follow, and Gemini represented the natively multimodal frontier at its 2023 release.

---

## Self-Supervised Learning

Self-supervised learning extracts rich representations from unlabeled data, dramatically reducing the need for labeled datasets. Contrastive methods (SimCLR, MoCo) learn by comparing augmented views, self-distillation (DINO) learns without negative pairs, and masked prediction (MAE, JEPA) reconstructs missing information. These methods now provide the default initialization for most vision systems.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | SimCLR – Chen et al. (2020) | Paper | 🔑 | [arxiv.org/abs/2002.05709](https://arxiv.org/abs/2002.05709) |
| 2 | MoCo v2 – Chen et al. (2020) | Paper | | [arxiv.org/abs/2003.04297](https://arxiv.org/abs/2003.04297) |
| 3 | DINO / DINOv2 – Caron et al. (2021) / Oquab et al. (2023) | Paper | 🔑 | [DINO](https://arxiv.org/abs/2104.14294) · [DINOv2](https://arxiv.org/abs/2304.07193) |
| 4 | MAE – Masked Autoencoders Are Scalable Vision Learners – He et al. (2022) | Paper | | [arxiv.org/abs/2111.06377](https://arxiv.org/abs/2111.06377) |
| 5 | JEPA / I-JEPA – Assran et al. (2023) | Paper | | [arxiv.org/abs/2301.08243](https://arxiv.org/abs/2301.08243) |

---

## Alternative Architectures

The transformer's quadratic attention cost has spurred a wave of subquadratic alternatives. State space models (S4, Mamba) achieve linear-time sequence modeling, while RWKV and xLSTM revisit recurrence with modern training tricks. These architectures are particularly compelling for long-context and real-time applications.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | S4 – Efficiently Modeling Long Sequences with Structured State Spaces – Gu, Goel & Ré (2021) | Paper | 🔑 | [arxiv.org/abs/2111.00396](https://arxiv.org/abs/2111.00396) |
| 2 | Mamba – Linear-Time Sequence Modeling with Selective State Spaces – Gu & Dao (2023) | Paper | 🔑 | [arxiv.org/abs/2312.00752](https://arxiv.org/abs/2312.00752) |
| 3 | RWKV – Reinventing RNNs for the Transformer Era – Peng et al. (2023) | Paper | | [arxiv.org/abs/2305.13048](https://arxiv.org/abs/2305.13048) |
| 4 | xLSTM – Extended Long Short-Term Memory – Beck et al. (2024) | Paper | | [arxiv.org/abs/2405.04517](https://arxiv.org/abs/2405.04517) |

---

## Agentic AI

LLM-powered agents combine reasoning, tool use, memory, and retrieval to act autonomously. ReAct interleaves reasoning traces with actions, RAG grounds generation in retrieved documents (Sentence-BERT explains the sentence embeddings that semantic retrieval is built on), Tree of Thoughts explores branching reasoning paths, and Toolformer teaches models to call APIs on their own. "Building Effective Agents" distills the practical design patterns (prompt chaining, routing, orchestrator–workers, evaluator–optimizer, autonomous loops), and SWE-bench is the benchmark that made real-world software engineering the standard test of agent capability. (Sparks of AGI is a capabilities-evaluation study of GPT-4 rather than an agents paper; it sits here for historical reasons.)

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | ReAct – Yao et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629) |
| 2 | RAG – Retrieval-Augmented Generation – Lewis et al. (2020) | Paper | 🔑 | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401) |
| 3 | Tree of Thoughts – Yao et al. (2023) | Paper | | [arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601) |
| 4 | Toolformer – Schick et al. (2023) | Paper | | [arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761) |
| 5 | Sparks of AGI – Bubeck et al. (2023) | Paper | 🔑 | [arxiv.org/abs/2303.12712](https://arxiv.org/abs/2303.12712) |
| 6 | Voyager – Wang et al. (2023) | Paper | | [arxiv.org/abs/2305.16291](https://arxiv.org/abs/2305.16291) |
| 7 | Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks – Reimers & Gurevych (2019) | Paper | | [arxiv.org/abs/1908.10084](https://arxiv.org/abs/1908.10084) |
| 8 | Building Effective Agents – Schluntz & Zhang, Anthropic (2024) | Blog | | [anthropic.com](https://www.anthropic.com/engineering/building-effective-agents) |
| 9 | SWE-bench: Can Language Models Resolve Real-World GitHub Issues? – Jimenez et al. (2023) | Paper | | [arxiv.org/abs/2310.06770](https://arxiv.org/abs/2310.06770) |

---

## Robotics and Embodied AI

Foundation models are increasingly being applied to physical-world reasoning and control. RT-2 connects vision-language models directly to robot actions, π0 pairs a pretrained vision-language model with a flow-matching action head to control many different robots, and World Models learn compressed latent dynamics for planning and imagination.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | RT-2 – Brohan et al. (2023) | Paper | | [arxiv.org/abs/2307.15818](https://arxiv.org/abs/2307.15818) |
| 2 | World Models – Ha & Schmidhuber (2018) | Paper | | [arxiv.org/abs/1803.10122](https://arxiv.org/abs/1803.10122) |
| 3 | π0: A Vision-Language-Action Flow Model for General Robot Control – Black et al. (2024) | Paper | | [arxiv.org/abs/2410.24164](https://arxiv.org/abs/2410.24164) |

---

## Annual Reports

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Stanford HAI – AI Index Report | Report | 🔑 | [aiindex.stanford.edu/report](https://aiindex.stanford.edu/report/) |

The AI Index provides a comprehensive yearly snapshot of research trends, industry adoption, policy developments, and societal impact. Essential for staying calibrated on the state of the field.

---

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## 🛠️ Practice

1. **State-space models are filters you already know** — Take a continuous SSM x′ = Ax + Bu, y = Cx with N = 16 (the HiPPO-LegS A from the S4 paper, or any stable A). Discretize it with the bilinear transform (S4's choice) and with zero-order hold (Mamba's). Compute the output for a 4,096-sample input both as a recurrence and as a convolution with the kernel K̄ = (CB̄, CĀB̄, CĀ²B̄, …), and plot the kernel's impulse and frequency response — it is an IIR filter. Then make the step size Δ depend on the input (Mamba's selection) and show the convolution view no longer applies while the recurrence still does. Done when: recurrence and convolution agree to 1e-6 in the time-invariant case and you can explain why Mamba needs a hardware-aware parallel scan. *(~4 h · S4; Mamba)*
2. **Representations without labels** — On CIFAR-10, compare frozen features from (a) OpenCLIP ViT-B/32 — zero-shot with bare class names, with "a photo of a {label}.", and with a 5-prompt ensemble, plus a linear probe; (b) DINOv2 ViT-S/14 — linear probe and k-NN; (c) a ResNet-18 SimCLR you pretrain yourself for ~30 epochs, ablating color jitter and the projection head. Finally, run zero-shot CLIP on 50 phone photos of bench gear — oscilloscope, multimeter, soldering iron, bare PCB, breadboard. Done when: you have one results table, can explain each ranking with the papers' design choices, and have characterized where CLIP fails on your photos. *(~6 h incl. GPU time · CLIP; SimCLR; MoCo v2; DINO/DINOv2)*
3. **Test-time compute on a small model** — With a 0.5–1.5B open instruct model on 300 GSM8K problems, sample N ∈ {1, 2, 4, …, 64} solutions and plot accuracy vs. generated tokens for majority voting and for best-of-N under a verifier (an open reward/verifier model, or a self-evaluation prompt). Compare with a ~7B model at N = 1, matching FLOPs (≈ 2 × parameters × tokens). Bucket problems by difficulty using the small model's own pass rate, as Snell et al. do. Done when: you can say whether your data supports their claim that test-time compute can substitute for parameters on easier problems but not on the hardest ones. *(~6 h · Snell et al. 2024)*
4. **Agent from parts: RAG + ReAct over datasheets** — Build a ~200-line ReAct loop (Thought → Action → Observation) with two tools: retrieval over 20 datasheets and app notes you actually use (chunked, embedded with an open embedding model, cosine top-k — the RAG pattern) and a Python calculator. Write 30 questions with known answers that need lookup plus arithmetic (e.g. "worst-case offset error at a gain of 100 for part X over 0–70 °C"). Compare closed-book, RAG-only and RAG + ReAct. Done when: you've reported accuracy for all three and classified every failure as retrieval miss, reasoning error or tool misuse. *(~6 h · ReAct; RAG; Toolformer)*
5. **Claims ledger** — Write a 300-word critique of *Sparks of AGI*'s methodology — qualitative probes of an early, unreleased model without a fixed protocol — ending with what a falsifiable version of its central claim would look like. Then, using the latest Stanford AI Index trend data, write five predictions about this section's threads that resolve within 12 months, each with a probability, a resolution criterion and a date, in a file you'll revisit. Done when: a stranger could resolve every prediction without asking you what you meant. *(~2 h · Sparks of AGI; Stanford HAI AI Index)*

**🏗️ Mini-project — R1-Zero at Toy Scale:** RL-train a 0.5–1.5B *base* model on a task with verifiable answers — Countdown (combine given numbers to hit a target) or GSM8K — using GRPO with only rule-based rewards (answer correctness plus format), as in DeepSeek-R1-Zero. Use TRL's `GRPOTrainer` or write GRPO yourself (group-normalized advantages, no critic). Track reward, held-out accuracy, mean response length, and how often self-checking phrases ("wait", "let me verify") appear over training. Deliverable: `projects/ml/11-frontiers/r1-zero-toy/` with plots, 10 annotated transcripts from early vs. late training, and a one-page comparison with the paper's training-dynamics figures. Done when: held-out accuracy improves by ≥ 10 points over the base model with the same prompt, and you can say — with examples — whether response length grew and whether anything like the paper's "aha moment" appeared. *(~15 h incl. GPU time on one 24–80 GB GPU)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. In one sentence each, what is the training signal in CLIP, SimCLR, DINO, MAE and I-JEPA? Which use negatives, and how do the others avoid collapse?
2. According to Snell et al., when does extra test-time compute beat a bigger model, and when doesn't it?
3. What rewards did DeepSeek-R1-Zero use, why no learned reward model, and what problems motivated R1's cold-start SFT stage?
4. Why can a linear time-invariant state-space model be computed as a convolution, and why does Mamba's selectivity break that?
5. What failure of chain-of-thought alone does ReAct's interleaving of actions address, and what does RAG give you that a bigger model doesn't?
6. You need a sequence model for a high-rate sensor stream on an MCU with 64 KB of RAM. Would you prototype a transformer, a Mamba-style SSM, or RWKV first, and why?
7. Misconception probe: "Sparks of AGI showed GPT-4 is an AGI." What kind of evidence did the paper present, and what would a falsifiable test look like?
8. Explain to a smart friend in 3 sentences what "test-time compute scaling" is and why it changed how frontier labs build models after 2024.
