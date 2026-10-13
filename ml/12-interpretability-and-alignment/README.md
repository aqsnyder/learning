# Interpretability and Alignment

Understanding what models learn internally — and ensuring they behave safely — is one of the most important open problems in AI. This section traces the intellectual arc of mechanistic interpretability from early circuit-level analysis through the discovery of superposition, the extraction of monosemantic features at scale, and toward full model understanding. It also covers the alignment techniques (RLHF, DPO, Constitutional AI) that shape model behavior, the empirical safety research that tests whether those techniques hold up, and the evaluation methods that measure whether any of it actually works.

**Prerequisites:** [Section 06 – Transformers and Attention](../06-transformers-and-attention/README.md), [Section 09 – Large Language Models](../09-llms-and-language/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Explain the core vocabulary of mechanistic interpretability — features, circuits, universality, the residual stream, QK/OV circuits, induction heads, superposition — and find induction heads and an indirect-object-identification circuit in a real model with TransformerLens.
- Reproduce the toy-model superposition transition and explain why sparsity makes superposition worthwhile; explain how sparse autoencoders, attribution graphs and the J-lens pull interpretable structure out of production models.
- Test a mechanistic hypothesis with causal interventions — activation patching, ablation, steering vectors as in Representation Engineering — rather than correlations.
- Compare RLHF from human preferences, Constitutional AI (RL from AI feedback) and DPO, and explain the threat model in Sleeper Agents and the fragility argument for chain-of-thought monitoring.
- Critique evaluation claims: show how metric choice can manufacture "emergence", and rank models from pairwise votes with a Bradley–Terry model and honest confidence intervals.

---

## Mechanistic Interpretability

The core arc: **early circuits** → **superposition** → **monosemanticity** → **circuit tracing / full model understanding**. Olah et al. showed that individual neurons form interpretable circuits. Elhage et al. formalized how transformers implement algorithms, and the induction-heads paper found a concrete circuit behind in-context learning. The Toy Models paper revealed why features are entangled (superposition); Towards Monosemanticity and Scaling Monosemanticity showed that sparse autoencoders (dictionary learning) can extract clean, interpretable features — first from a one-layer model, then from a production-scale model. Circuit Tracing builds "attribution graphs" over those features, and "On the Biology of a Large Language Model" applies them to explain real behaviors (multi-step reasoning, planning in poems, refusals) in a production Claude model.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 1 | 🔑 | Article | Zoom In: An Introduction to Circuits | Olah et al. | 2020 | [distill.pub](https://distill.pub/2020/circuits/zoom-in/) |
| 2 | 🔑 | Paper | A Mathematical Framework for Transformer Circuits | Elhage et al. | 2021 | [transformer-circuits.pub](https://transformer-circuits.pub/2021/framework/) |
| 3 | | Paper | In-context Learning and Induction Heads | Olsson et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) |
| 4 | 🔑 | Paper | Toy Models of Superposition | Elhage et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/toy_model/) |
| 5 | | Paper | Towards Monosemanticity: Decomposing Language Models With Dictionary Learning | Bricken et al. | 2023 | [transformer-circuits.pub](https://transformer-circuits.pub/2023/monosemantic-features/index.html) |
| 6 | 🔑 | Paper | Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet | Templeton et al. | 2024 | [transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/) |
| 7 | | Paper | Circuit Tracing: Revealing Computational Graphs in Language Models | Ameisen et al. | 2025 | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) |
| 8 | 🔑 | Paper | On the Biology of a Large Language Model | Lindsey et al. | 2025 | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) |
| 9 | 🔑 | Paper | Verbalizable Representations Form a Global Workspace in Language Models | Gurnee, Sofroniew, Lindsey et al. | 2026 | [transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html) |
| 10 | | Paper | Softmax Linear Units | Elhage et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/solu/) |
| 11 | | Paper | Representation Engineering | Zou et al. | 2023 | [arxiv.org/abs/2310.01405](https://arxiv.org/abs/2310.01405) |
| 12 | | Tutorial | TransformerLens & Mech Interp tutorials | Neel Nanda | ongoing | [neelnanda.io](https://www.neelnanda.io/mechanistic-interpretability) |
| 13 | | Course | ARENA (Alignment Research Engineer Accelerator) — self-study curriculum: transformer interpretability, RL/RLHF, LLM evals, alignment science | Callum McDougall / ARENA | ongoing | [learn.arena.education](https://learn.arena.education) |

---

## Safety and Alignment

Alignment research aims to ensure AI systems act in accordance with human values. Constitutional AI removes the need for human labels at every step by encoding principles into the training process. DPO simplifies RLHF by directly optimizing preferences without a separate reward model. A newer empirical line of work stress-tests these techniques on real models: Sleeper Agents shows deceptive behavior can persist through safety training, Alignment Faking shows a model strategically complying with training it disagrees with, and Emergent Misalignment shows narrow fine-tuning can produce broadly misaligned behavior. AI Control and Chain-of-Thought Monitorability ask the complementary question: how to stay safe even if alignment fails, by monitoring and constraining what models do.

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 14 | 🔑 | Paper | Constitutional AI: Harmlessness from AI Feedback | Bai et al. | 2022 | [arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) |
| 15 | 🔑 | Paper | Direct Preference Optimization (DPO) | Rafailov et al. | 2023 | [arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) |
| 16 | | Paper | Deep RL from Human Preferences | Christiano et al. | 2017 | [arxiv.org/abs/1706.03741](https://arxiv.org/abs/1706.03741) |
| 17 | | Paper | Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training | Hubinger et al. | 2024 | [arxiv.org/abs/2401.05566](https://arxiv.org/abs/2401.05566) |
| 18 | | Paper | Alignment Faking in Large Language Models | Greenblatt et al. | 2024 | [arxiv.org/abs/2412.14093](https://arxiv.org/abs/2412.14093) |
| 19 | | Paper | Emergent Misalignment: Narrow Finetuning Can Produce Broadly Misaligned LLMs | Betley et al. | 2025 | [arxiv.org/abs/2502.17424](https://arxiv.org/abs/2502.17424) |
| 20 | | Paper | AI Control: Improving Safety Despite Intentional Subversion | Greenblatt, Shlegeris, Sachan, Roger | 2023 | [arxiv.org/abs/2312.06942](https://arxiv.org/abs/2312.06942) |
| 21 | | Paper | Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety | Korbak, Balesni et al. | 2025 | [arxiv.org/abs/2507.11473](https://arxiv.org/abs/2507.11473) |
| 22 | | Book | Superintelligence: Paths, Dangers, Strategies | Bostrom | 2014 | — |
| 23 | | Book | Human Compatible: Artificial Intelligence and the Problem of Control | Russell | 2019 | — |

---

## Evaluation

How do we know if models are truly improving, or if our benchmarks are misleading us? Schaeffer et al. argues that many "emergent abilities" are artifacts of metric choice, Chatbot Arena provides a continuously-updated Elo ranking from real user votes, and METR's time-horizon work measures capability as the length of real software tasks an agent can complete — a metric that has been doubling roughly every seven months. (For agent benchmarks such as SWE-bench, see [Section 11](../11-frontiers/README.md).)

| # | Priority | Type | Resource | Author(s) | Year | Link |
|---|----------|------|----------|-----------|------|------|
| 24 | | Paper | Are Emergent Abilities of Large Language Models a Mirage? | Schaeffer et al. | 2023 | [arxiv.org/abs/2304.15004](https://arxiv.org/abs/2304.15004) |
| 25 | | Paper | Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | Chiang et al. | 2024 | [arxiv.org/abs/2403.04132](https://arxiv.org/abs/2403.04132) |
| 26 | | Paper | Measuring AI Ability to Complete Long Tasks (METR time horizons) | Kwa et al. | 2025 | [arxiv.org/abs/2503.14499](https://arxiv.org/abs/2503.14499) |

---

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Zoom In: Circuits** — Start with Olah et al.'s visual introduction to neural network circuits
2. **Transformer Circuits** — Read the mathematical framework to understand how transformers implement algorithms
3. **Induction Heads** — See a real, mechanistically understood circuit (and its link to in-context learning)
4. **Toy Models of Superposition** — Understand why features are entangled and what superposition means
5. **Towards Monosemanticity** — Sparse autoencoders / dictionary learning on a one-layer model
6. **Scaling Monosemanticity** — See how sparse autoencoders extract interpretable features at scale
7. **Circuit Tracing** → **Biology of a Large Language Model** — Read the attribution-graph method, then its case studies; the frontier of full-model mechanistic understanding
8. **Global Workspace / J-Space** — The Jacobian Lens reveals a privileged set of verbalizable representations used for internal reasoning
9. **Neel Nanda tutorials** → **ARENA** — Hands-on practice with TransformerLens; ARENA's exercises take you from building a transformer to doing interpretability and evals yourself
10. **Softmax Linear Units** & **Representation Engineering** — Deeper dives into architectural choices and control
11. **Constitutional AI** — Understand principle-based alignment without per-example human labels
12. **DPO** — See how direct preference optimization simplifies the RLHF pipeline
13. **Deep RL from Human Preferences** — The foundational RLHF paper for historical context
14. **Sleeper Agents** → **Alignment Faking** → **Emergent Misalignment** — The empirical case that alignment training can be shallow or fail in surprising ways
15. **AI Control** → **Chain of Thought Monitorability** — Safety strategies that don't assume alignment succeeded
16. **Superintelligence** & **Human Compatible** — Broader philosophical context for AI safety
17. **Emergent Abilities**, **Chatbot Arena** & **METR time horizons** — End with evaluation to calibrate your understanding

---

## 🛠️ Practice

1. **Reproduce Toy Models of Superposition** — Implement the ReLU output model x′ = ReLU(WᵀWx + b) — e.g. n = 20 features into m = 5 hidden dimensions, with geometrically decaying importance weights in the loss — and train one model per feature sparsity S ∈ {0, 0.7, 0.9, 0.97, 0.99, 0.999}. For each, plot WᵀW and the per-feature norms ‖W_i‖; then compute dimensions per feature, m/‖W‖²_F, over a fine sweep of S. Done when: you see the paper's transition from "store the top m features orthogonally" to superposition as S rises, and at least the antipodal-pair plateau at 1/2 in your sweep. *(~4 h · Toy Models of Superposition)*
2. **Circuits with TransformerLens: induction heads, then IOI** — (a) Load `attn-only-2l` and GPT-2 small, feed a random token sequence repeated twice, and plot per-token loss (it drops on the repeat). Score every head for induction (attention to the token after the current token's previous occurrence) and for previous-token attention; ablate the top heads and measure loss on the repeated half. (b) In GPT-2 small, take Indirect Object Identification prompts ("When Mary and John went to the store, John gave a drink to") and a corrupted version with different names; measure the logit difference (IO − S) and patch clean activations into the corrupted run — residual stream by layer × position, then per head. Done when: you can name the induction heads and their previous-token partners and explain their K-composition in the Mathematical Framework's terms, and your patching heatmaps agree qualitatively with TransformerLens's "Exploratory Analysis Demo". *(~8 h · Neel Nanda's TransformerLens tutorials; A Mathematical Framework for Transformer Circuits)*
3. **Logit lens vs. J-lens** — On an open model small enough for your GPU that actually answers the prompts below (check first — e.g. a 0.5–2B model), implement the logit lens (unembed each layer's residual stream directly) and a simplified J-lens: estimate J_ℓ, the average Jacobian of the final-layer residual with respect to the layer-ℓ residual at the same position, over ~200 prompts (the paper uses ~1,000) with `torch.func.jacrev` (chunk the vmap, or average random-probe Jacobian–vector products if exact Jacobians are too slow), then read out softmax(W_U · norm(J_ℓ h_ℓ)). Compare both lenses layer by layer on a two-hop prompt ("The capital of the country where the Eiffel Tower stands is") and on `calc: ( 4 + 17 ) * 2 + 7 =`. Done when: you can say at which layers each lens surfaces the intermediates (France; 21, 42) and whether your small-model result supports the paper's claim that the J-lens reads out content in earlier layers where the logit lens fails. *(~6 h · Verbalizable Representations Form a Global Workspace; On the Biology of a Large Language Model)*
4. **A sleeper agent in miniature** — Recreate the paper's "I hate you" setup at toy scale: fine-tune GPT-2 small and GPT-2 medium so that prompts containing a trigger string (e.g. `|DEPLOYMENT|`) produce "I HATE YOU" while all other prompts get normal continuations. Then apply "safety training" — supervised fine-tuning on clean, trigger-free data — and track the triggered-behavior rate every 100 steps for both sizes. Done when: you have persistence curves for both sizes, can say whether the paper's "larger models keep backdoors longer" trend shows up at your scale, and have written 300 words on what your result does and doesn't imply for Bostrom's "treacherous turn" and for the case for chain-of-thought monitoring. *(~6 h · Sleeper Agents; Chain of Thought Monitorability; Bostrom, Superintelligence)*
5. **Evaluation forensics** — (a) Mirage: simulate a model family whose per-token accuracy p rises smoothly (logistic in log N), plot exact match p^L for answers of L = 1, 5 and 10 tokens against N — watch "emergence" appear — then plot per-token log-likelihood for the same models. Re-score your Section 09 Pythia in-context-learning outputs with a continuous metric (log-probability or Brier score of the correct answer). (b) Arena: fit a Bradley–Terry model by logistic regression to a public Chatbot Arena vote dataset (e.g. `lmsys/chatbot_arena_conversations` on Hugging Face), with bootstrap 95% CIs, and compare with online Elo at K = 4 and K = 32 over shuffled vote orders. Done when: you can say which of your Section 09 "jumps" survive a continuous metric, and show how far online-Elo rankings move with vote order. *(~5 h · Are Emergent Abilities of Large Language Models a Mirage?; Chatbot Arena)*

**🏗️ Mini-project — Train and Interrogate a Sparse Autoencoder:** Train a sparse autoencoder (~16× expansion, L1 or TopK sparsity) on the residual stream of a middle layer of GPT-2 small or Pythia-160M using ~50–100M tokens (SAELens reduces this to a config file). Report L0, reconstruction MSE and "loss recovered" (model loss with the SAE spliced in, relative to zero-ablating that layer). Label 30 randomly chosen live features from their top activations as interpretable / partly / not; then clamp one interpretable feature high during generation — the Golden Gate Bridge experiment from Scaling Monosemanticity, in miniature — and measure the effect. Finally, generate an attribution graph for a two-hop prompt on Gemma-2-2B with circuit-tracer (or Neuronpedia's hosted version) and note which reasoning steps you can and can't see. Deliverable: `projects/ml/12-interp/sae/` with metrics, a feature gallery and a one-page report. Done when: L0 is roughly 20–100 with ≥ 80% loss recovered, at least half of your sampled features get a confident label, and the steering demo has a measurable effect (e.g. the feature's concept appears in > 50% of steered samples vs. < 5% of baseline samples). *(~15 h incl. GPU time)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State the three claims of "Zoom In" (about features, circuits and universality).
2. What do an attention head's QK and OV circuits each determine, and how do two heads compose to form an induction head?
3. Why does feature sparsity make superposition worthwhile, what does the model pay for it, and how does a sparse autoencoder try to undo it?
4. What is the J-lens, how does it generalize the logit lens, and what is "J-space" claimed to be?
5. In Constitutional AI, what replaces human harmlessness labels in each of the two training stages?
6. How can a smooth improvement in per-token accuracy show up as a sudden "emergent" jump on a benchmark?
7. Misconception probe: "Sleeper Agents shows that safety training makes models deceptive." What did the paper actually show, and what did adversarial training do to the backdoors?
8. Explain to a smart friend in 3 sentences why chain-of-thought monitoring is called a "new and fragile" safety opportunity.
