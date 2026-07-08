# Scaling, Efficiency, and Deployment

Knowing how to scale models efficiently—and train them stably—is what separates toy experiments from production systems. This section covers the empirical scaling laws that predict performance, the optimizers that make training possible, the normalization techniques that keep gradients healthy, and the parallelism strategies that distribute training across thousands of accelerators. It also covers the efficiency frontier: Mixture-of-Experts architectures that decouple parameter count from compute, FlashAttention for IO-aware speedups, parameter-efficient fine-tuning (LoRA/QLoRA), knowledge distillation, and speculative decoding for fast inference.

**Prerequisites:** [Section 03 – Neural Network Foundations](../03-neural-network-foundations/README.md) through [Section 06 – Attention and Transformers](../06-attention-and-transformers/README.md)

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
| 11 | Mixtral of Experts – Mistral AI (2024) | Paper | | [arxiv.org/abs/2401.04088](https://arxiv.org/abs/2401.04088) |
| 12 | FlashAttention – Dao et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2205.14135](https://arxiv.org/abs/2205.14135) |
| 13 | LoRA – Low-Rank Adaptation – Hu et al. (2021) | Paper | 🔑 | [arxiv.org/abs/2106.09685](https://arxiv.org/abs/2106.09685) |
| 14 | QLoRA – Dettmers et al. (2023) | Paper | | [arxiv.org/abs/2305.14314](https://arxiv.org/abs/2305.14314) |
| 15 | Distilling the Knowledge in a Neural Network – Hinton et al. (2015) | Paper | 🔑 | [arxiv.org/abs/1503.02531](https://arxiv.org/abs/1503.02531) |
| 16 | Speculative Decoding – Leviathan et al. (2023) | Paper | | [arxiv.org/abs/2211.17192](https://arxiv.org/abs/2211.17192) |

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Optimizers first** – Read the Adam paper, then AdamW to understand decoupled weight decay and why it matters.
2. **Normalization** – Study Batch Normalization and Layer Normalization; know when to use each and why transformers prefer LayerNorm.
3. **Scaling Laws** – Read Kaplan et al. to build intuition for how loss scales with compute, data, and parameters.
4. **Chinchilla** – Understand compute-optimal training and why the Kaplan scaling recipe was revised.
5. **Parallelism** – Read GPipe for pipeline parallelism, then Megatron-LM for tensor parallelism at scale.
6. **Mixture of Experts** – Read the original MoE paper, then Switch Transformer for simplified routing, then Mixtral for modern open-weight MoE.
7. **Efficient attention** – Read FlashAttention to understand IO-aware exact attention and why it's now the default.
8. **Parameter-efficient fine-tuning** – Read LoRA, then QLoRA for 4-bit quantized fine-tuning.
9. **Knowledge distillation** – Read Hinton et al. to understand how to compress large models into smaller ones.
10. **Fast inference** – Read Speculative Decoding to understand draft-model-based acceleration.
