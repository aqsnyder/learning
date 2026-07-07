# Large Language Models

Large language models represent the convergence of the transformer architecture, massive data, and scaling laws into systems that can follow instructions, reason, and generate coherent text. This section follows the GPT lineage from unsupervised pretraining through RLHF alignment, covers prompting strategies like chain-of-thought, and includes open-weight alternatives that make the field accessible.

**Prerequisites:** [Section 06 – Attention and Transformers](../06-attention-and-transformers/README.md), [Section 08 – Scaling and Training](../08-scaling-and-training/README.md)

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Intro to LLMs – Andrej Karpathy (Video) | Video | 🔑 | [youtube.com](https://www.youtube.com/watch?v=zjkBMFhNj_g) |
| 2 | Deep Dive into LLMs – Andrej Karpathy (Video) | Video | 🔑 | [youtube.com](https://www.youtube.com/watch?v=7xTGNNLPyMI) |
| 3 | GPT-2 – Radford et al. (2019) | Paper | 🔑 | [openai.com](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) |
| 4 | GPT-3 – Brown et al. (2020) | Paper | 🔑 | [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) |
| 5 | T5 – Raffel et al. (2019) | Paper | | [arxiv.org/abs/1910.10683](https://arxiv.org/abs/1910.10683) |
| 6 | InstructGPT / RLHF – Ouyang et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155) |
| 7 | Chain-of-Thought Prompting – Wei et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903) |
| 8 | LLaMA – Touvron et al. (2023) | Paper | | [arxiv.org/abs/2302.13971](https://arxiv.org/abs/2302.13971) |
| 9 | GPT-4 Technical Report (2023) | Paper | 🔑 | [arxiv.org/abs/2303.08774](https://arxiv.org/abs/2303.08774) |
| 10 | Anthropic Research Blog | Blog | | [anthropic.com/research](https://www.anthropic.com/research) |

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Big picture** – Watch Karpathy's Intro to LLMs for a high-level mental model, then the Deep Dive for implementation-level detail.
2. **GPT lineage** – Read GPT-2 → GPT-3 → GPT-4 to see how scale and training recipes evolved.
3. **Encoder-decoder contrast** – Read T5 to understand the text-to-text framing and how it differs from decoder-only GPT.
4. **Alignment** – Study InstructGPT to learn how RLHF steers models toward following human intent.
5. **Prompting** – Read Chain-of-Thought to see how eliciting reasoning steps improves accuracy.
6. **Open models** – Read LLaMA to understand efficient open-weight alternatives and their training data strategies.
7. **Ongoing research** – Browse the Anthropic Research blog for the latest work on capabilities and safety.
