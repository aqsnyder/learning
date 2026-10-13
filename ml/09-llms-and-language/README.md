# Large Language Models

Large language models represent the convergence of the transformer architecture, massive data, and scaling laws into systems that can follow instructions, reason, and generate coherent text. This section follows the full pipeline — tokenization, pretraining data, the GPT lineage of pretrained models, instruction tuning and RLHF alignment, and prompting strategies like chain-of-thought — and includes open-weight model reports that document how frontier-class models are actually built.

**Prerequisites:** [Section 06 – Transformers and Attention](../06-transformers-and-attention/README.md), [Section 08 – Scaling, Efficiency, and Deployment](../08-scaling-and-training/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Describe the full LLM pipeline — data, tokenization, pretraining, supervised fine-tuning, preference tuning, inference — and estimate the compute and cost of each stage for a given model size.
- Explain byte-level BPE tokenization and predict and demonstrate its failure modes (spelling, letter counting, arithmetic, token efficiency on code and non-English text).
- Explain zero-, one- and few-shot in-context learning, contrast it with fine-tuning, and measure how it scales with model size.
- Explain the InstructGPT recipe (SFT → reward model → PPO with a KL penalty), including the pairwise reward-model loss and the alignment tax, and contrast T5's text-to-text encoder–decoder framing with decoder-only GPTs.
- Evaluate when chain-of-thought prompting helps, and critique a technical report's claims (e.g. GPT-4's "predictable scaling") from what it does and doesn't disclose.

---

## Resources

| # | Resource | Type | Marking | Link | Description |
|---|----------|------|---------|------|-------------|
| 1 | Intro to LLMs – Andrej Karpathy (Video) | Video | | [youtube.com](https://www.youtube.com/watch?v=zjkBMFhNj_g) | Karpathy's one-hour talk: an LLM as "two files", how pretraining and fine-tuning produce an assistant, the road ahead, and LLM security. Your first mental model. |
| 2 | Deep Dive into LLMs – Andrej Karpathy (Video) | Video | 🔑 | [youtube.com](https://www.youtube.com/watch?v=7xTGNNLPyMI) | 3.5-hour tour of the full pipeline: pretraining data, tokenization, training, inference, post-training (SFT, RL, RLHF) and why models need tokens to think. The section's spine. |
| 3 | GPT-2 – Radford et al. (2019) | Paper | | [openai.com](https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf) | Shows a 1.5B-parameter language model trained on WebText performing tasks zero-shot, with gains growing log-linearly in size. Also read its byte-level BPE rationale. |
| 4 | GPT-3 – Brown et al. (2020) | Paper | 🔑 | [arxiv.org/abs/2005.14165](https://arxiv.org/abs/2005.14165) | 175B-parameter model doing tasks from a few in-prompt examples, with no gradient updates. The core paper on in-context learning and its dependence on scale. |
| 5 | T5 – Raffel et al. (2019) | Paper | | [arxiv.org/abs/1910.10683](https://arxiv.org/abs/1910.10683) | Casts every NLP task as text-to-text and systematically compares pre-training objectives, architectures and datasets, introducing the C4 corpus. The encoder–decoder contrast to GPT. |
| 6 | InstructGPT / RLHF – Ouyang et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2203.02155](https://arxiv.org/abs/2203.02155) | Fine-tunes GPT-3 on demonstrations, fits a reward model to rankings, then optimizes against it with PPO. Learn each step's loss and the alignment tax. |
| 7 | Chain-of-Thought Prompting – Wei et al. (2022) | Paper | | [arxiv.org/abs/2201.11903](https://arxiv.org/abs/2201.11903) | Few-shot exemplars with intermediate reasoning steps improve arithmetic, commonsense and symbolic reasoning in sufficiently large models. Practice 4 tests that scale dependence. |
| 8 | LLaMA – Touvron et al. (2023) | Paper | | [arxiv.org/abs/2302.13971](https://arxiv.org/abs/2302.13971) | 7B–65B models trained on trillions of tokens from public data; LLaMA-13B beats GPT-3 on most benchmarks. Why training small models longer pays off at inference. |
| 9 | GPT-4 Technical Report (2023) | Paper | | [arxiv.org/abs/2303.08774](https://arxiv.org/abs/2303.08774) | Multimodal model report: exam results, performance predicted from runs using ≤1/1,000th the compute, and no architecture, size or data details. Read it critically. |
| 10 | Anthropic Research Blog | Blog | | [anthropic.com/research](https://www.anthropic.com/research) | Index of Anthropic's research posts: alignment, interpretability, societal impacts, economics and frontier red-teaming. Browse it for current work, not as a course. |
| 11 | Let's build the GPT Tokenizer – Andrej Karpathy (Video; lecture 8 of Zero to Hero) | Video | | [youtube.com](https://www.youtube.com/watch?v=zduSFxRajkE) | Builds the GPT-series BPE tokenizer from scratch (encode, decode, training). Learn which LLM quirks, such as spelling and arithmetic errors, trace back to tokenization. |
| 12 | Let's reproduce GPT-2 (124M) – Andrej Karpathy (Video) | Video | | [youtube.com](https://www.youtube.com/watch?v=l8pRSuU81PU) | Codes and pretrains GPT-2 (124M) from an empty file, step by step. Pretraining only (no chat fine-tuning); follow it end to end. |
| 13 | FLAN: Finetuned Language Models Are Zero-Shot Learners – Wei et al. (2021) | Paper | | [arxiv.org/abs/2109.01652](https://arxiv.org/abs/2109.01652) | Instruction tuning: fine-tuning a 137B model on 60+ datasets phrased as instructions improves zero-shot performance on unseen tasks. Ablations: task count, scale and instructions matter. |
| 14 | The FineWeb Datasets: Decanting the Web for the Finest Text Data at Scale – Penedo et al. (2024) | Paper | | [arxiv.org/abs/2406.17557](https://arxiv.org/abs/2406.17557) | A 15T-token Common Crawl dataset with each design choice documented and ablated, plus the FineWeb-Edu educational subset. Learn how filtering and deduplication move model quality. |
| 15 | The Llama 3 Herd of Models – Grattafiori et al., Meta (2024) | Paper | | [arxiv.org/abs/2407.21783](https://arxiv.org/abs/2407.21783) | Dense transformers up to 405B parameters and 128K context, with pretraining data, infrastructure and post-training documented in depth. Study it as a full frontier recipe. |
| 16 | DeepSeek-V3 Technical Report – DeepSeek-AI (2024) | Paper | | [arxiv.org/abs/2412.19437](https://arxiv.org/abs/2412.19437) | A 671B MoE (37B active per token) with multi-head latent attention, auxiliary-loss-free load balancing and multi-token prediction. Frontier MoE engineering, openly documented. |
| 17 | Stanford CS336: Language Modeling from Scratch – Hashimoto & Liang (2025) | Course | | [cs336.stanford.edu](https://cs336.stanford.edu/spring2025/) | Implementation-heavy course: build a tokenizer, transformer and optimizer, then systems (FlashAttention2 in Triton, distributed training), scaling laws, data filtering, and SFT plus RL for math. |

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

**Core path (🔑):** Karpathy's *Deep Dive into LLMs* → GPT-3 → InstructGPT

1. **Big picture** – Watch Karpathy's Intro to LLMs for a high-level mental model, then the Deep Dive for implementation-level detail.
2. **Tokenization** – Watch Karpathy's tokenizer lecture; many "LLM weirdness" bugs (spelling, arithmetic, trailing spaces) trace back here.
3. **GPT lineage** – Read GPT-2 → GPT-3 → GPT-4 to see how scale and training recipes evolved.
4. **Build one** – Follow Karpathy's "Let's reproduce GPT-2 (124M)" end to end; use Stanford CS336 if you want the full from-scratch stack (tokenizer, systems, scaling, data, alignment) with assignments.
5. **Encoder-decoder contrast** – Read T5 to understand the text-to-text framing and how it differs from decoder-only GPT.
6. **Data** – Read FineWeb to see how pretraining data is filtered and deduplicated, and how much data quality moves the needle.
7. **Instruction tuning → alignment** – Read FLAN (instruction tuning on many tasks), then InstructGPT to learn how RLHF steers models toward following human intent.
8. **Prompting** – Read Chain-of-Thought to see how eliciting reasoning steps improves accuracy.
9. **Open models** – Read LLaMA, then the Llama 3 report (the most detailed public account of pretraining, post-training, and infrastructure) and the DeepSeek-V3 report (MoE, multi-head latent attention, FP8 training at frontier scale).
10. **Ongoing research** – Browse the Anthropic Research blog for the latest work on capabilities and safety.

---

## 🛠️ Practice

1. **Tokenizer forensics** — With `tiktoken`'s GPT-2 encoding (byte-level BPE, 50,257 tokens) and one modern open-model tokenizer, tokenize an English paragraph, 2 KB of C firmware, a hex dump, numbers such as 1234567 and 12,345.67, and a non-English paragraph; report characters per token for each. Then write your own byte-level BPE trainer (≤ 100 lines) and train it on 10 MB of text. Done when: your tokenizer round-trips arbitrary bytes with no unknown tokens — GPT-2's argument for byte-level BPE — and you can explain three LLM failure modes that trace back to tokenization. *(~3 h · GPT-2; Karpathy, "Let's build the GPT Tokenizer"; Karpathy, "Deep Dive into LLMs")*
2. **Sampling and the zero-shot trick** — With GPT-2 (124M–1.5B), implement greedy, temperature, top-k and top-p sampling directly from logits. Generate 20 continuations of one prompt at T ∈ {0.3, 0.7, 1.0, 1.5} and measure distinct-2-grams and repetition. Then reproduce GPT-2's "TL;DR:" zero-shot summarization on 50 CNN/Daily Mail articles using the paper's setup (100 tokens, top-k sampling with k = 2, keep the first 3 generated sentences), and score ROUGE against lead-3 and random-3 baselines. Done when: you reproduce the paper's sobering finding — TL;DR barely beats random-3 and trails lead-3 by a wide margin — and can say what that implies about "zero-shot task learning" at that scale. *(~3 h · GPT-2; Karpathy, "Intro to Large Language Models")*
3. **In-context learning vs. scale** — Use the Pythia suite (70M → 2.8B; same data, same order — built for scaling studies). Measure 0-, 1-, 4- and 16-shot accuracy on three GPT-3-style tasks you can generate: unscrambling words, 2-digit addition, and sentiment. Plot accuracy vs. model size with one line per shot count, mirroring GPT-3's in-context-learning curves. Done when: you can say which tasks improve smoothly and which look like sudden jumps. Keep the raw outputs — you'll re-score them in Section 12's "mirage" exercise. *(~5 h · GPT-3; Karpathy, "Deep Dive into LLMs")*
4. **Chain-of-thought, measured** — On 200 GSM8K test problems, compare standard 8-shot prompting with 8-shot chain-of-thought (exemplars from Wei et al.'s appendix) for three *base* models of one family at different sizes (e.g. ~0.5B, ~1.5B, ~7B). Report accuracy with 95% confidence intervals, and add self-consistency (majority vote over 5 samples) for the largest model. Done when: you've compared your scale trend with the paper's finding that CoT helps only at sufficient scale, and noted the contamination caveat for recent models trained on math-heavy data. *(~5 h · Chain-of-Thought Prompting; Karpathy, "Deep Dive into LLMs", segment on why models need tokens to think)*
5. **A reward model from preferences** — Implement InstructGPT's pairwise loss −log σ(r(x, y_w) − r(x, y_l)) with a scalar head on GPT-2 medium (or a ~0.5B model) and train on ~10k pairs from Anthropic's HH-RLHF dataset. Report held-out pairwise accuracy and compare it with the inter-labeler agreement InstructGPT reports. Then use the reward model for best-of-16 reranking and inspect what it rewards — length? hedging? politeness? Done when: you've found at least one exploitable bias (e.g. reward rising with length regardless of quality) and shown it with a plot. *(~5 h · InstructGPT; Anthropic research blog)*

**🏗️ Mini-project — A Pocket Chat Model, End to End:** Run the whole pipeline at small scale with nanochat, Karpathy's end-to-end successor to nanoGPT (tokenizer → pretraining → SFT → RL → evaluation → chat): its single-GPU mode uses gradient accumulation, or rent an 8×H100 node for its few-hour "speedrun" (check the README for the current time and cost). If budget is tight, do the same stages yourself on TinyStories with nanoGPT. (Neither codebase is a listed resource. Karpathy's "Let's reproduce GPT-2 (124M)" above covers the pretraining stage only — its companion repository notes that it does not cover chat fine-tuning — while Stanford CS336 walks through every stage, ending with SFT and reasoning RL in its "Alignment and Reasoning RL" assignment.) Deliverable: `projects/ml/09-llm/pocket-chat/` with a cost sheet (FLOPs from 6ND, GPU-hours, dollars), loss and eval curves per stage, base vs. SFT vs. RL transcripts on 30 held-out prompts, and a one-page postmortem mapping each stage to Karpathy's "Deep Dive into LLMs" and to InstructGPT's three steps. Done when: your FLOP estimate matches the logged compute within 2×, and you can point to a concrete behavior change caused by each post-training stage. *(~15 h incl. GPU time)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What did the GPT-4 technical report claim it could predict from much smaller training runs, and what did it decline to disclose?
2. Why does GPT-2 use byte-level BPE, and why do LLMs miscount the letters in a word?
3. What is in-context learning, how does it differ from fine-tuning, and what did GPT-3 show about its dependence on scale?
4. Write InstructGPT's reward-model loss. What does the KL penalty during PPO protect against?
5. T5 casts every task as text-to-text. How does its span-corruption objective differ from BERT's masked LM?
6. Misconception probe: "Chain-of-thought makes any model reason better." What did Wei et al. find about model scale?
7. LLaMA-13B beat GPT-3 175B on most benchmarks. Using Chinchilla-style reasoning, explain how — and why training past the compute-optimal point is the right tradeoff when inference cost dominates.
8. Explain to a smart friend in 3 sentences what an LLM is, using Karpathy's "two files" framing, and one thing it is not.
