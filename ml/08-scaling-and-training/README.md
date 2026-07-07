# Scaling and Training

Knowing how to scale models efficiently—and train them stably—is what separates toy experiments from production systems. This section covers the empirical scaling laws that predict performance, the optimizers that make training possible, the normalization techniques that keep gradients healthy, and the parallelism strategies that distribute training across thousands of accelerators.

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

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Optimizers first** – Read the Adam paper, then AdamW to understand decoupled weight decay and why it matters.
2. **Normalization** – Study Batch Normalization and Layer Normalization; know when to use each and why transformers prefer LayerNorm.
3. **Scaling Laws** – Read Kaplan et al. to build intuition for how loss scales with compute, data, and parameters.
4. **Chinchilla** – Understand compute-optimal training and why the Kaplan scaling recipe was revised.
5. **Parallelism** – Read GPipe for pipeline parallelism, then Megatron-LM for tensor parallelism at scale.
