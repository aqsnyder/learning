# Scaling, Efficiency, and Deployment

Knowing how to scale models efficiently—and train them stably—is what separates toy experiments from production systems. This section covers the empirical scaling laws that predict performance, the optimizers that make training possible, the normalization techniques that keep gradients healthy, hyperparameter transfer across model sizes (μP), and the parallelism and memory-sharding strategies (pipeline, tensor, ZeRO/FSDP) that distribute training across thousands of accelerators. It also covers the efficiency frontier: Mixture-of-Experts architectures that decouple parameter count from compute, FlashAttention for IO-aware speedups, parameter-efficient fine-tuning (LoRA/QLoRA), quantization and knowledge distillation for smaller models, and inference serving (KV-cache management with PagedAttention, speculative decoding).

**Prerequisites:** [Section 03 – Neural Network Fundamentals](../03-neural-network-fundamentals/README.md) through [Section 06 – Transformers and Attention](../06-transformers-and-attention/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Estimate training compute with C ≈ 6ND, choose a compute-optimal model size and token count with Chinchilla's rule of thumb (~20 tokens per parameter), and explain why Kaplan et al. and Chinchilla reached different recipes.
- Implement Adam and AdamW from the papers' algorithms, explain bias correction and why decoupled weight decay differs from L2 regularization under adaptive optimizers, and contrast BatchNorm with LayerNorm.
- Explain the memory and communication tradeoffs of data, tensor (Megatron-LM), pipeline (GPipe) and expert (MoE) parallelism, and compute a pipeline-bubble fraction and an MoE's total vs. active parameters.
- Explain FlashAttention's IO-aware argument (HBM vs. on-chip SRAM traffic, online softmax) and why it is faster despite doing more FLOPs.
- Apply and evaluate LoRA/QLoRA, knowledge distillation and speculative decoding, and state the guarantee or tradeoff each comes with.

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | Scaling Laws for Neural LMs – Kaplan et al. (2020) | Paper | 🔑⭐ | [arxiv.org/abs/2001.08361](https://arxiv.org/abs/2001.08361) |
| 2 | GPipe – Huang et al. (2019) | Paper | ⭐ | [arxiv.org/abs/1811.06965](https://arxiv.org/abs/1811.06965) |
| 3 | Chinchilla – Hoffmann et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2203.15556](https://arxiv.org/abs/2203.15556) |
| 4 | Adam Optimizer – Kingma & Ba (2014) | Paper | 🔑 | [arxiv.org/abs/1412.6980](https://arxiv.org/abs/1412.6980) |
| 5 | AdamW – Loshchilov & Hutter (2017) | Paper | | [arxiv.org/abs/1711.05101](https://arxiv.org/abs/1711.05101) |
| 6 | Batch Normalization – Ioffe & Szegedy (2015) | Paper | | [arxiv.org/abs/1502.03167](https://arxiv.org/abs/1502.03167) |
| 7 | Layer Normalization – Ba et al. (2016) | Paper | | [arxiv.org/abs/1607.06450](https://arxiv.org/abs/1607.06450) |
| 8 | Megatron-LM – Shoeybi et al. (2019) | Paper | | [arxiv.org/abs/1909.08053](https://arxiv.org/abs/1909.08053) |
| 9 | MoE – Outrageously Large Neural Networks – Shazeer et al. (2017) | Paper | 🔑 | [arxiv.org/abs/1701.06538](https://arxiv.org/abs/1701.06538) |
| 10 | Switch Transformer – Fedus et al. (2021) | Paper | 🔑 | [arxiv.org/abs/2101.03961](https://arxiv.org/abs/2101.03961) |
| 11 | Mixtral of Experts – Jiang et al. (Mistral AI, 2024) | Paper | | [arxiv.org/abs/2401.04088](https://arxiv.org/abs/2401.04088) |
| 12 | FlashAttention – Dao et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135) |
| 13 | LoRA – Low-Rank Adaptation – Hu et al. (2021) | Paper | 🔑 | [arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685) |
| 14 | QLoRA – Dettmers et al. (2023) | Paper | | [arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314) |
| 15 | Distilling the Knowledge in a Neural Network – Hinton et al. (2015) | Paper | 🔑 | [arxiv.org/abs/1503.02531](https://arxiv.org/abs/1503.02531) |
| 16 | Speculative Decoding – Leviathan et al. (2023) | Paper | | [arxiv.org/abs/2211.17192](https://arxiv.org/abs/2211.17192) |
| 17 | ZeRO: Memory Optimizations Toward Training Trillion Parameter Models – Rajbhandari et al. (2019) | Paper | | [arxiv.org/abs/1910.02054](https://arxiv.org/abs/1910.02054) |
| 18 | μP – Tensor Programs V: Tuning Large Neural Networks via Zero-Shot Hyperparameter Transfer – Yang et al. (2022) | Paper | | [arxiv.org/abs/2203.03466](https://arxiv.org/abs/2203.03466) |
| 19 | The Ultra-Scale Playbook: Training LLMs on GPU Clusters – Tazi et al. (Hugging Face, 2025) | Guide | | [huggingface.co](https://huggingface.co/spaces/nanotron/ultrascale-playbook) |
| 20 | PagedAttention / vLLM – Efficient Memory Management for LLM Serving – Kwon et al. (2023) | Paper | | [arxiv.org/abs/2309.06180](https://arxiv.org/abs/2309.06180) |
| 21 | Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference – Jacob et al. (2017) | Paper | | [arxiv.org/abs/1712.05877](https://arxiv.org/abs/1712.05877) |

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Optimizers first** – Read the Adam paper, then AdamW to understand decoupled weight decay and why it matters.
2. **Normalization** – Study Batch Normalization and Layer Normalization; know when to use each and why transformers prefer LayerNorm.
3. **Scaling Laws** – Read Kaplan et al. to build intuition for how loss scales with compute, data, and parameters.
4. **Chinchilla** – Understand compute-optimal training and why the Kaplan scaling recipe was revised.
5. **μP** – See how to tune hyperparameters on a small proxy model and transfer them unchanged to a large one — what makes scaling-law experiments practical.
6. **Parallelism** – Read GPipe for pipeline parallelism, then Megatron-LM for tensor parallelism at scale, then ZeRO for sharding optimizer state, gradients, and parameters (the idea behind PyTorch FSDP).
7. **The Ultra-Scale Playbook** – Tie it all together: data, ZeRO/FSDP, tensor, sequence/context, and pipeline parallelism with measured trade-offs on real GPU clusters.
8. **Mixture of Experts** – Read the original MoE paper, then Switch Transformer for simplified routing, then Mixtral for modern open-weight MoE.
9. **Efficient attention** – Read FlashAttention to understand IO-aware exact attention and why it's now the default.
10. **Parameter-efficient fine-tuning** – Read LoRA, then QLoRA for 4-bit quantized fine-tuning.
11. **Quantization** – Read Jacob et al. for int8 integer-only inference, the basis of TensorFlow Lite and most edge/microcontroller deployment.
12. **Knowledge distillation** – Read Hinton et al. to understand how to compress large models into smaller ones.
13. **Fast inference** – Read PagedAttention/vLLM to understand KV-cache memory management in LLM serving, then Speculative Decoding for draft-model-based acceleration.

---

## 🛠️ Practice

1. **Compute-budget Fermi problems** — Using C ≈ 6ND: (a) estimate GPT-3's training compute (175B parameters, 300B tokens) and convert it to A100-days at 40% utilization of the 312 TFLOP/s bf16 peak; (b) for a 10²¹-FLOP budget, find the Chinchilla-optimal N and D using D ≈ 20N; (c) check the rule against Chinchilla itself (70B parameters, 1.4T tokens) and Gopher (280B, 300B); (d) a 1B-parameter model must see 20B tokens in 24 h on one GPU — what sustained FLOP/s does that need, and is it possible on your GPU? Done when: every answer has units and is within 2× of a value you can cite or derive. *(~2 h · Kaplan et al.; Chinchilla)*
2. **Optimizers and normalization from the papers** — Implement Adam exactly per Kingma & Ba's Algorithm 1 and AdamW per Loshchilov & Hutter, and verify step-for-step equality with `torch.optim.Adam` / `AdamW` over 100 steps in float64 (PyTorch's AdamW multiplies the decoupled decay by the learning rate, θ ← θ − lr·λ·θ, while the paper's Algorithm 2 scales it only by the schedule multiplier η_t, so map λ between the two before comparing). Train a small CNN or nanoGPT config with Adam + L2 penalty vs. AdamW at three decay values, and show how the best learning rate couples to the decay value in the L2 case. Then implement BatchNorm (with running statistics) and LayerNorm, verify both against PyTorch in train and eval modes, and demonstrate two BatchNorm failure modes: batch size 2, and leakage of future-token statistics in a causal language model. Done when: all equality tests pass and you can explain in 150 words why transformers use LayerNorm. *(~5 h · Adam; AdamW; Batch Normalization; Layer Normalization)*
3. **Parallelism and MoE arithmetic** — (a) GPipe: compute the bubble fraction (K−1)/(M+K−1) for K = 8 stages and M = 8, 32 and 128 micro-batches, then reconcile your M = 32 number with the paper's claim that the overhead is negligible for M ≥ 4K (read what it says about re-materialization). (b) Megatron-LM: sketch the column-then-row split of the MLP and the head split of attention across 2 GPUs, and count all-reduces per layer in the forward and backward passes. (c) Mixtral: from its published layer sizes, account for ~47B total vs. ~13B active parameters under top-2 routing over 8 experts. (d) Implement a top-2 MoE layer with the Switch Transformer load-balancing loss, route a synthetic batch, and plot per-expert load with and without the auxiliary loss. Done when: (c) closes to within ~5% and (d) shows the auxiliary loss flattening the load. *(~4 h · GPipe; Megatron-LM; Shazeer et al. MoE; Switch Transformer; Mixtral)*
4. **FlashAttention's IO argument** — (a) For n = 4096, d = 64 in fp16, count the HBM bytes read and written by standard attention (which materializes the n×n score and probability matrices) vs. a tiled kernel that never does. (b) Implement the online-softmax recurrence (running max and running sum) over blocks in NumPy and verify it equals the full softmax-weighted sum. (c) On a GPU, benchmark naive PyTorch attention vs. `F.scaled_dot_product_attention` for n = 512 to 8192: wall time and peak memory. Done when: your measured memory scales as ~n² vs. ~n and you can explain why FlashAttention is faster even though its backward pass does *more* FLOPs. *(~3 h · FlashAttention)*
5. **Adapt, then accelerate** — (a) LoRA: fine-tune GPT-2 small (or a ~0.5B open model) on a small task with rank r = 8 on W_q and W_v — the matrices Hu et al. found most effective to adapt — with B initialized to zero, vs. full fine-tuning; compare trainable parameters, peak memory and the eval metric, then merge the adapter and verify the merged model's outputs match the unmerged ones to float tolerance. Re-run with the base model loaded in 4-bit NF4 (QLoRA) and record the memory saving. (b) Speculative decoding: implement Leviathan et al.'s accept/reject rule with GPT-2 small as the draft and GPT-2 large as the target; measure acceptance rate α and wall-clock speedup for γ = 2, 4, 8, and compare with the expected tokens per target call, (1 − α^(γ+1))/(1 − α). Done when: the merge check passes, and a statistical test shows your speculative sampler's output distribution matches the target's on a fixed prompt. *(~6 h · LoRA; QLoRA; Speculative Decoding)*

**🏗️ Mini-project — Your Own Scaling Law:** Train a family of six GPT models (≈1M–50M non-embedding parameters) on one tokenized corpus (TinyStories or a FineWeb-Edu sample), each at 3–4 token budgets, using AdamW with cosine decay and PyTorch's fused attention. Fit Chinchilla's parametric form L(N, D) = E + A/N^α + B/D^β to your final losses, and Kaplan's power law L(N) to your largest-budget runs. Deliverable: `projects/ml/08-scaling/my-scaling-law/` with the run table, fitted constants with bootstrap CIs, an iso-FLOP plot, and the compute-optimal N and D your fit predicts for a 10× larger budget — then train that model and compare. Done when: the prediction lands within ~0.05 nats of the realized loss, or you can explain from your fits why it doesn't. *(~15 h incl. GPU time)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Where does the 6 in C ≈ 6ND come from? Use it to estimate the compute for a Chinchilla-optimal 1B-parameter model.
2. What did Chinchilla change about Kaplan et al.'s compute-optimal recipe, and what methodological difference drove the change?
3. Why does Adam need bias correction, and why isn't L2 regularization equivalent to weight decay under Adam?
4. Misconception probe: "FlashAttention is an approximation that saves FLOPs." What does it actually save, and is its output exact?
5. In LoRA, why is B initialized to zero, and what does inference cost after the adapter is merged?
6. Why is the output of speculative decoding distributed exactly like the target model's, and what determines the speedup?
7. In Hinton et al.'s distillation, what information do high-temperature soft targets carry that hard labels don't, and why is the soft-target loss scaled by T²?
8. Explain to a smart friend in 3 sentences how a mixture-of-experts model can have 47B parameters but run like a 13B one.
