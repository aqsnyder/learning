# Frontiers (2023-2026+)

> This section is a living document. Use the `.agents/skills/update-curriculum` skill to search for and add new important papers and resources.

The frontier of ML research moves fast. This section collects the most impactful recent work across reasoning, multimodality, self-supervised learning, alternative architectures, agentic AI, robotics, and ecosystem-level reports. Revisit regularly.

---

## Reasoning and Test-Time Compute

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Scaling LLM Test-Time Compute – Snell et al. (2024) | Paper | 🔑 | [arxiv.org/abs/2408.03314](https://arxiv.org/abs/2408.03314) |
| 2 | DeepSeek-R1 (2025) | Paper | 🔑 | [arxiv.org/abs/2501.12948](https://arxiv.org/abs/2501.12948) |

Reasoning-focused models shift compute from training to inference. Snell et al. formalizes when test-time compute scaling beats simply training a larger model. DeepSeek-R1 demonstrates reinforcement-learning-driven chain-of-thought at scale.

---

## Multimodal Models

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Gemini – Google DeepMind (2023) | Paper | 🔑 | [arxiv.org/abs/2312.11805](https://arxiv.org/abs/2312.11805) |
| 2 | SAM – Kirillov et al. (2023) | Paper | | [arxiv.org/abs/2304.02643](https://arxiv.org/abs/2304.02643) |
| 3 | CLIP – Radford et al. (2021) | Paper | | [arxiv.org/abs/2103.00020](https://arxiv.org/abs/2103.00020) |

Multimodal models unify vision, language, and other modalities into a single architecture. CLIP pioneered contrastive image-text pretraining, SAM brought foundation-model thinking to segmentation, and Gemini represents the natively multimodal frontier.

---

## Self-Supervised Learning

Self-supervised learning extracts rich representations from unlabeled data, dramatically reducing the need for labeled datasets. Contrastive methods (SimCLR, MoCo) learn by comparing augmented views, self-distillation (DINO) learns without negative pairs, and masked prediction (MAE, JEPA) reconstructs missing information. These methods now provide the default initialization for most vision systems.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | SimCLR – Chen et al. (2020) | Paper | 🔑 | [arxiv.org/abs/2002.05709](https://arxiv.org/abs/2002.05709) |
| 2 | MoCo v2 – Chen et al. (2020) | Paper | | [arxiv.org/abs/2003.04297](https://arxiv.org/abs/2003.04297) |
| 3 | DINO / DINOv2 – Caron et al. (2021) / Oquab et al. (2023) | Paper | 🔑 | [arxiv.org/abs/2104.14294](https://arxiv.org/abs/2104.14294) |
| 4 | MAE – Masked Autoencoders Are Scalable Vision Learners – He et al. (2022) | Paper | | [arxiv.org/abs/2111.06377](https://arxiv.org/abs/2111.06377) |
| 5 | JEPA / I-JEPA – Assran et al. (2023) | Paper | | [arxiv.org/abs/2301.08243](https://arxiv.org/abs/2301.08243) |

---

## Alternative Architectures

The transformer's quadratic attention cost has spurred a wave of subquadratic alternatives. State space models (S4, Mamba) achieve linear-time sequence modeling, while RWKV and xLSTM revisit recurrence with modern training tricks. These architectures are particularly compelling for long-context and real-time applications.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | S4 – Structured State Spaces for Sequence Modeling – Gu et al. (2021) | Paper | 🔑 | [arxiv.org/abs/2111.00396](https://arxiv.org/abs/2111.00396) |
| 2 | Mamba – Linear-Time Sequence Modeling with Selective State Spaces – Gu & Dao (2023) | Paper | 🔑 | [arxiv.org/abs/2312.00752](https://arxiv.org/abs/2312.00752) |
| 3 | RWKV – Reinventing RNNs for the Transformer Era – Peng et al. (2023) | Paper | | [arxiv.org/abs/2305.13048](https://arxiv.org/abs/2305.13048) |
| 4 | xLSTM – Extended Long Short-Term Memory – Beck et al. (2024) | Paper | | [arxiv.org/abs/2405.04517](https://arxiv.org/abs/2405.04517) |

---

## Agentic AI

LLM-powered agents combine reasoning, tool use, memory, and retrieval to act autonomously. ReAct interleaves reasoning traces with actions, RAG grounds generation in retrieved documents, Tree of Thoughts explores branching reasoning paths, and Toolformer teaches models to call APIs on their own.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | ReAct – Yao et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2210.03629](https://arxiv.org/abs/2210.03629) |
| 2 | RAG – Retrieval-Augmented Generation – Lewis et al. (2020) | Paper | 🔑 | [arxiv.org/abs/2005.11401](https://arxiv.org/abs/2005.11401) |
| 3 | Tree of Thoughts – Yao et al. (2023) | Paper | | [arxiv.org/abs/2305.10601](https://arxiv.org/abs/2305.10601) |
| 4 | Toolformer – Schick et al. (2023) | Paper | | [arxiv.org/abs/2302.04761](https://arxiv.org/abs/2302.04761) |
| 5 | Sparks of AGI – Bubeck et al. (2023) | Paper | 🔑 | [arxiv.org/abs/2303.12712](https://arxiv.org/abs/2303.12712) |
| 6 | Voyager – Wang et al. (2023) | Paper | | [arxiv.org/abs/2305.16291](https://arxiv.org/abs/2305.16291) |

---

## Robotics and Embodied AI

Foundation models are increasingly being applied to physical-world reasoning and control. RT-2 connects vision-language models directly to robot actions, while World Models learn compressed latent dynamics for planning and imagination.

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | RT-2 – Brohan et al. (2023) | Paper | | [arxiv.org/abs/2307.15818](https://arxiv.org/abs/2307.15818) |
| 2 | World Models – Ha & Schmidhuber (2018) | Paper | | [arxiv.org/abs/1803.10122](https://arxiv.org/abs/1803.10122) |

---

## Annual Reports

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Stanford HAI – AI Index Report | Report | 🔑 | [aiindex.stanford.edu/report](https://aiindex.stanford.edu/report/) |

The AI Index provides a comprehensive yearly snapshot of research trends, industry adoption, policy developments, and societal impact. Essential for staying calibrated on the state of the field.

---

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list
