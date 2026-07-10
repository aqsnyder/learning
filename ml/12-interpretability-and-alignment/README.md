# Interpretability and Alignment

Understanding what models learn internally — and ensuring they behave safely — is one of the most important open problems in AI. This section traces the intellectual arc of mechanistic interpretability from early circuit-level analysis through the discovery of superposition, the extraction of monosemantic features at scale, and toward full model understanding. It also covers the alignment techniques (RLHF, DPO, Constitutional AI) that shape model behavior, and the evaluation methods that measure whether any of it actually works.

**Prerequisites:** [Section 06 – Transformers and Attention](../06-transformers-and-attention/README.md), [Section 09 – LLMs and Language](../09-llms-and-language/README.md)

---

## Mechanistic Interpretability

The core arc: **early circuits** → **superposition** → **monosemanticity** → **full model understanding**. Olah et al. showed that individual neurons form interpretable circuits. Elhage et al. formalized how transformers implement algorithms. The Toy Models paper revealed why features are entangled (superposition), and Scaling Monosemanticity demonstrated that sparse autoencoders can extract clean, interpretable features from production-scale models. The "Biology of a Large Language Model" represents the frontier: understanding entire models as organisms.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 1 | 🔑 | Article | Zoom In: An Introduction to Circuits | Olah et al. | 2020 | [distill.pub](https://distill.pub/2020/circuits/zoom-in/) |
| 2 | 🔑 | Paper | A Mathematical Framework for Transformer Circuits | Elhage et al. | 2021 | [transformer-circuits.pub](https://transformer-circuits.pub/2021/framework/) |
| 3 | 🔑 | Paper | Toy Models of Superposition | Elhage et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/toy_model/) |
| 4 | 🔑 | Paper | Scaling Monosemanticity | Burt et al. | 2024 | [transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| 5 | 🔑 | Paper | On the Biology of a Large Language Model | Anthropic | 2025 | [transformer-circuits.pub](https://transformer-circuits.pub/) |
| 6 | 🔑 | Paper | Verbalizable Representations Form a Global Workspace in Language Models | Gurnee, Sofroniew, Lindsey et al. | 2026 | [transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html) |
| 7 | | Paper | Softmax Linear Units | Anthropic | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/solu/) |
| 8 | | Paper | Representation Engineering | Zou et al. | 2023 | [arxiv.org/abs/2310.01405](https://arxiv.org/abs/2310.01405) |
| 9 | | Tutorial | TransformerLens & Mech Interp tutorials | Neel Nanda | ongoing | [neelnanda.io](https://www.neelnanda.io/mechanistic-interpretability) |

---

## Safety and Alignment

Alignment research aims to ensure AI systems act in accordance with human values. Constitutional AI removes the need for human labels at every step by encoding principles into the training process. DPO simplifies RLHF by directly optimizing preferences without a separate reward model. Sleeper Agents investigates whether deceptive behavior can persist through safety training.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 9 | 🔑 | Paper | Constitutional AI: Harmlessness from AI Feedback | Bai et al. | 2022 | [arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) |
| 10 | 🔑 | Paper | Direct Preference Optimization (DPO) | Rafailov et al. | 2023 | [arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) |
| 11 | | Paper | Deep RL from Human Preferences | Christiano et al. | 2017 | [arxiv.org/abs/1706.03741](https://arxiv.org/abs/1706.03741) |
| 12 | | Paper | Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training | Hubinger et al. | 2024 | [arxiv.org/abs/2401.05566](https://arxiv.org/abs/2401.05566) |
| 13 | | Paper | Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety | Baker, Korbak et al. | 2025 | [arxiv.org/abs/2503.07972](https://arxiv.org/abs/2503.07972) |
| 14 | | Book | Superintelligence: Paths, Dangers, Strategies | Bostrom | 2014 | — |
| 15 | | Book | Human Compatible: Artificial Intelligence and the Problem of Control | Russell | 2019 | — |

---

## Evaluation

How do we know if models are truly improving, or if our benchmarks are misleading us? Schaeffer et al. argues that many "emergent abilities" are artifacts of metric choice, while Chatbot Arena provides a continuously-updated Elo ranking from real user votes.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 16 | | Paper | Are Emergent Abilities of Large Language Models a Mirage? | Schaeffer et al. | 2023 | [arxiv.org/abs/2304.15004](https://arxiv.org/abs/2304.15004) |
| 17 | | Paper | Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | Chiang et al. | 2024 | [arxiv.org/abs/2403.04132](https://arxiv.org/abs/2403.04132) |

---

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Zoom In: Circuits** — Start with Olah et al.'s visual introduction to neural network circuits
2. **Transformer Circuits** — Read the mathematical framework to understand how transformers implement algorithms
3. **Toy Models of Superposition** — Understand why features are entangled and what superposition means
4. **Scaling Monosemanticity** — See how sparse autoencoders extract interpretable features at scale
5. **Biology of a Large Language Model** — The frontier of full-model mechanistic understanding
6. **Global Workspace / J-Space** — The Jacobian Lens reveals a privileged set of verbalizable representations used for internal reasoning
7. **Neel Nanda tutorials** — Hands-on practice with TransformerLens for mech interp research
8. **Softmax Linear Units** & **Representation Engineering** — Deeper dives into architectural choices and control
9. **Constitutional AI** — Understand principle-based alignment without per-example human labels
10. **DPO** — See how direct preference optimization simplifies the RLHF pipeline
11. **Deep RL from Human Preferences** — The foundational RLHF paper for historical context
12. **Sleeper Agents** — Understand the challenges of deceptive alignment
13. **Superintelligence** & **Human Compatible** — Broader philosophical context for AI safety
14. **Emergent Abilities** & **Chatbot Arena** — End with evaluation to calibrate your understanding
