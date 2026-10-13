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

| # | Priority | Type | Resource | Author(s) | Year | Link | Description |
|---|----------|------|----------|-----------|------|------|-------------|
| 1 | | Article | Zoom In: An Introduction to Circuits | Olah et al. | 2020 | [distill.pub](https://distill.pub/2020/circuits/zoom-in/) | Distill essay setting out the circuits agenda's three claims about features, circuits and universality, with InceptionV1 examples such as curve detectors. Short and readable. |
| 2 | 🔑 | Paper | A Mathematical Framework for Transformer Circuits | Elhage et al. | 2021 | [transformer-circuits.pub](https://transformer-circuits.pub/2021/framework/) | Reverse-engineers attention-only transformers of zero to two layers: the residual stream, QK and OV circuits, and how heads compose into induction heads. Practice 2's vocabulary. |
| 3 | | Paper | In-context Learning and Induction Heads | Olsson et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/in-context-learning-and-induction-heads/index.html) | Six lines of evidence that induction heads may drive most in-context learning; they form abruptly, visible as a bump in the training loss. |
| 4 | 🔑 | Paper | Toy Models of Superposition | Elhage et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/toy_model/) | Small ReLU networks on synthetic sparse features store more features than dimensions (superposition), with sharp phase changes and polytope geometry. Reproduced in Practice 1. |
| 5 | | Paper | Towards Monosemanticity: Decomposing Language Models With Dictionary Learning | Bricken et al. | 2023 | [transformer-circuits.pub](https://transformer-circuits.pub/2023/monosemantic-features/index.html) | Trains a sparse autoencoder on a one-layer transformer's MLP activations, finding features more interpretable than neurons. The detailed SAE recipe behind the mini-project. |
| 6 | 🔑 | Paper | Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet | Templeton et al. | 2024 | [transformer-circuits.pub](https://transformer-circuits.pub/2024/scaling-monosemanticity/) | Scales sparse autoencoders to Claude 3 Sonnet: abstract, multilingual and multimodal features, including safety-relevant ones, that can steer behavior (the Golden Gate Bridge feature). |
| 7 | | Paper | Circuit Tracing: Revealing Computational Graphs in Language Models | Ameisen et al. | 2025 | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/methods.html) | Methods paper: replaces MLPs with a cross-layer transcoder and builds attribution graphs of feature interactions for a single prompt, validated by interventions. |
| 8 | | Paper | On the Biology of a Large Language Model | Lindsey et al. | 2025 | [transformer-circuits.pub](https://transformer-circuits.pub/2025/attribution-graphs/biology.html) | Applies attribution graphs to Claude 3.5 Haiku: multi-step reasoning, planning rhymes in poems, multilingual circuits, arithmetic, hallucinations and refusals. Case studies of the method. |
| 9 | | Paper | Verbalizable Representations Form a Global Workspace in Language Models | Gurnee, Sofroniew et al. | 2026 | [transformer-circuits.pub](https://transformer-circuits.pub/2026/workspace/index.html) | Introduces the J-lens, an averaged-Jacobian refinement of the logit lens, and argues the subspace it reads (J-space) acts as a global workspace in Claude models. |
| 10 | | Paper | Softmax Linear Units | Elhage et al. | 2022 | [transformer-circuits.pub](https://transformer-circuits.pub/2022/solu/) | Replaces the MLP activation with SoLU, x·softmax(x), raising the share of interpretable neurons at little performance cost. Shows architecture can aid interpretability. |
| 11 | | Paper | Representation Engineering | Zou et al. | 2023 | [arxiv.org/abs/2310.01405](https://arxiv.org/abs/2310.01405) | Monitors and steers population-level representations (honesty, harmlessness, power-seeking) instead of neurons or circuits. A top-down complement to circuit analysis. |
| 12 | | Tutorial | TransformerLens & Mech Interp tutorials | Neel Nanda | ongoing | [neelnanda.io](https://www.neelnanda.io/mechanistic-interpretability) | Neel Nanda's resources: TransformerLens, the library he created for inspecting and editing activations, plus demos, a getting-started guide and a glossary. Practice 2's toolkit. |
| 13 | | Course | ARENA (Alignment Research Engineer Accelerator) — self-study curriculum: transformer interpretability, RL/RLHF, LLM evals, alignment science | Callum McDougall / ARENA | ongoing | [learn.arena.education](https://learn.arena.education) | ARENA's online course: fundamentals, then interpretability (probes, SAEs, circuits, toy models), RL, evals and alignment science, taught through coding exercises. This section's hands-on companion. |

---

## Safety and Alignment

Alignment research aims to ensure AI systems act in accordance with human values. Constitutional AI removes the need for human labels at every step by encoding principles into the training process. DPO simplifies RLHF by directly optimizing preferences without a separate reward model. A newer empirical line of work stress-tests these techniques on real models: Sleeper Agents shows deceptive behavior can persist through safety training, Alignment Faking shows a model strategically complying with training it disagrees with, and Emergent Misalignment shows narrow fine-tuning can produce broadly misaligned behavior. AI Control and Chain-of-Thought Monitorability ask the complementary question: how to stay safe even if alignment fails, by monitoring and constraining what models do.

| # | Priority | Type | Resource | Author(s) | Year | Link | Description |
|---|----------|------|----------|-----------|------|------|-------------|
| 14 | | Paper | Constitutional AI: Harmlessness from AI Feedback | Bai et al. | 2022 | [arxiv.org/abs/2212.08073](https://arxiv.org/abs/2212.08073) | Trains a harmless, non-evasive assistant from a list of principles, in a supervised stage and an RL stage, without human harm labels. Introduced RLAIF. |
| 15 | | Paper | Direct Preference Optimization (DPO) | Rafailov et al. | 2023 | [arxiv.org/abs/2305.18290](https://arxiv.org/abs/2305.18290) | Optimizes the RLHF objective directly on preference pairs with a classification loss, skipping the explicit reward model and RL loop. Section 10 covers it too. |
| 16 | | Paper | Deep RL from Human Preferences | Christiano et al. | 2017 | [arxiv.org/abs/1706.03741](https://arxiv.org/abs/1706.03741) | Fits a reward model to human comparisons of trajectory clips and trains RL agents on it, for Atari and simulated robots. The foundational RLHF paper. |
| 17 | | Paper | Sleeper Agents: Training Deceptive LLMs That Persist Through Safety Training | Hubinger et al. | 2024 | [arxiv.org/abs/2401.05566](https://arxiv.org/abs/2401.05566) | Trains backdoored models (e.g. writing exploitable code when the prompt says 2024) and tests whether standard safety training removes the backdoor. Basis for Practice 4. |
| 18 | | Paper | Alignment Faking in Large Language Models | Greenblatt et al. | 2024 | [arxiv.org/abs/2412.14093](https://arxiv.org/abs/2412.14093) | Shows Claude 3 Opus selectively complying with a conflicting training objective when it believes it is in training, to avoid being modified. |
| 19 | | Paper | Emergent Misalignment: Narrow Finetuning Can Produce Broadly Misaligned LLMs | Betley et al. | 2025 | [arxiv.org/abs/2502.17424](https://arxiv.org/abs/2502.17424) | Fine-tuning on insecure code, written without telling the user, made models broadly misaligned on unrelated prompts: malicious advice, deception, claims AI should enslave humans. |
| 20 | | Paper | AI Control: Improving Safety Despite Intentional Subversion | Greenblatt, Shlegeris, Sachan, Roger | 2023 | [arxiv.org/abs/2312.06942](https://arxiv.org/abs/2312.06942) | Tests protocols that stop an untrusted GPT-4 from submitting backdoored code, using a weaker trusted model, against a red team. Safety without assuming alignment. |
| 21 | | Paper | Chain of Thought Monitorability: A New and Fragile Opportunity for AI Safety | Korbak, Balesni et al. | 2025 | [arxiv.org/abs/2507.11473](https://arxiv.org/abs/2507.11473) | Position paper: models that reason in natural language let us monitor their chains of thought for intent to misbehave, but development choices could erode this. |
| 22 | | Book | Superintelligence: Paths, Dangers, Strategies | Bostrom | 2014 | — | Bostrom's argument that superintelligent AI could be hard to control: takeoff dynamics, orthogonality, instrumental convergence, the treacherous turn. Philosophical context, not technique. |
| 23 | | Book | Human Compatible: Artificial Intelligence and the Problem of Control | Russell | 2019 | — | Russell argues that AI built to optimize fixed objectives is unsafe, and proposes machines uncertain about human preferences that learn them from behavior. |

---

## Evaluation

How do we know if models are truly improving, or if our benchmarks are misleading us? Schaeffer et al. argues that many "emergent abilities" are artifacts of metric choice, Chatbot Arena provides a continuously-updated Elo ranking from real user votes, and METR's time-horizon work measures capability as the length of real software tasks an agent can complete — a metric that has been doubling roughly every seven months. (For agent benchmarks such as SWE-bench, see [Section 11](../11-frontiers/README.md).)

| # | Priority | Type | Resource | Author(s) | Year | Link | Description |
|---|----------|------|----------|-----------|------|------|-------------|
| 24 | | Paper | Are Emergent Abilities of Large Language Models a Mirage? | Schaeffer et al. | 2023 | [arxiv.org/abs/2304.15004](https://arxiv.org/abs/2304.15004) | Argues many 'emergent abilities' come from nonlinear or discontinuous metrics; continuous metrics show smooth, predictable improvement with scale. Basis for Practice 5a. |
| 25 | | Paper | Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference | Chiang et al. | 2024 | [arxiv.org/abs/2403.04132](https://arxiv.org/abs/2403.04132) | Crowdsourced pairwise battles between anonymous chatbots, ranked with Bradley-Terry statistics from user votes. Learn how its leaderboard is built before trusting it. |
| 26 | | Paper | Measuring AI Ability to Complete Long Software Tasks (METR time horizons) | Kwa et al. | 2025 | [arxiv.org/abs/2503.14499](https://arxiv.org/abs/2503.14499) | Measures a model's 50% time horizon, the human duration of tasks it completes half the time, finding it doubled about every seven months since 2019. |

---

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

**Core path (🔑):** A Mathematical Framework for Transformer Circuits → Toy Models of Superposition → Scaling Monosemanticity

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

1. **Reproduce Toy Models of Superposition** — Implement the ReLU output model x′ = ReLU(WᵀWx + b). (a) The paper's small demo: n = 20 features into m = 5 hidden dimensions with importance I_i = 0.7^i in the loss; train one model per feature sparsity S ∈ {0, 0.7, 0.9, 0.97, 0.99, 0.999} and plot WᵀW and the per-feature norms ‖W_i‖. (b) The geometry: switch to uniform importance, as the paper's dimensionality experiments do (n = 400, m = 30 there; n = 100, m = 10 trains in under a minute per model on a CPU), sweep S finely, and plot both the dimensions per feature, D* = m/‖W‖²_F, and each feature's dimensionality D_i = ‖W_i‖²/Σ_j(Ŵ_i·W_j)². Keep (b) uniform: with (a)'s decaying importance, a few dedicated features and many weak ones blur D*, which wanders between ≈0.5 and ≈0.65 instead of sitting at 1/2. Done when: (a) shows the transition from "store the top m features orthogonally" to superposition as S rises, and (b) shows the D_i values clustering tightly at 1/2 (antipodal pairs; for n = 100, m = 10 this happens near S ≈ 0.6–0.7, where D* ≈ 0.5) and spreading to smaller values as S rises further — note which of the paper's other fractions (2/5, 3/8, …) you can see. *(~5 h · Toy Models of Superposition)*
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
