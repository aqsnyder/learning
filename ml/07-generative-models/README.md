# Generative Models

Generative models learn the underlying distribution of data and can synthesize new, realistic samples. This section traces the arc from variational autoencoders and GANs through normalizing flows to the diffusion models that now power state-of-the-art image and video generation. Understanding these architectures is essential for grasping modern creative AI, drug discovery pipelines, and data augmentation techniques.

**Prerequisites:** [Section 03 – Neural Network Foundations](../03-neural-network-foundations/README.md), [Section 06 – Attention and Transformers](../06-attention-and-transformers/README.md)

---

## Resources

| # | Resource | Type | Marking | Link |
|---|----------|------|---------|------|
| 1 | VAE – Kingma & Welling (2013) | Paper | 🔑 | [arxiv.org/abs/1312.6114](https://arxiv.org/abs/1312.6114) |
| 2 | GAN – Goodfellow et al. (2014) | Paper | 🔑 | [arxiv.org/abs/1406.2661](https://arxiv.org/abs/1406.2661) |
| 3 | DCGAN – Radford et al. (2015) | Paper | | [arxiv.org/abs/1511.06434](https://arxiv.org/abs/1511.06434) |
| 4 | Normalizing Flows – Rezende & Mohamed (2015) | Paper | ⭐ | [arxiv.org/abs/1505.05770](https://arxiv.org/abs/1505.05770) |
| 5 | DDPM – Ho, Jain & Abbeel (2020) | Paper | 🔑 | [arxiv.org/abs/2006.11239](https://arxiv.org/abs/2006.11239) |
| 6 | Latent Diffusion – Rombach et al. (2022) | Paper | | [arxiv.org/abs/2112.10752](https://arxiv.org/abs/2112.10752) |
| 7 | What are Diffusion Models? – Lilian Weng | Blog | | [lilianweng.github.io](https://lilianweng.github.io/posts/2021-07-11-diffusion-models/) |
| 8 | Distill.pub | Blog | | [distill.pub](https://distill.pub/) |
| 9 | Flow Matching for Generative Modeling – Lipman et al. (2022) | Paper | 🔑 | [arxiv.org/abs/2210.02747](https://arxiv.org/abs/2210.02747) |
| 10 | Classifier-Free Diffusion Guidance – Ho & Salimans (2022) | Paper | | [arxiv.org/abs/2207.12598](https://arxiv.org/abs/2207.12598) |
| 11 | Consistency Models – Song et al. (2023) | Paper | | [arxiv.org/abs/2303.01469](https://arxiv.org/abs/2303.01469) |
| 12 | DALL·E 2 – Ramesh et al. (2022) | Paper | | [arxiv.org/abs/2204.06125](https://arxiv.org/abs/2204.06125) |
| 13 | Imagen – Saharia et al. (2022) | Paper | | [arxiv.org/abs/2205.11487](https://arxiv.org/abs/2205.11487) |

> 🔑 = must-read &nbsp;&nbsp; ⭐ = Ilya Sutskever reading list

---

## Suggested Order

1. **Start with VAEs** – Read the Kingma & Welling paper to understand latent variable models and the reparameterization trick.
2. **Move to GANs** – Read the original GAN paper, then DCGAN for practical architectural patterns.
3. **Explore Normalizing Flows** – Rezende & Mohamed introduces invertible transformations and exact likelihood computation.
4. **Dive into Diffusion** – Read Lilian Weng's blog for intuition, then the DDPM paper for the full derivation.
5. **Scale up** – Study Latent Diffusion to see how diffusion meets autoencoders for efficient high-resolution generation.
6. **Flow Matching** – Read Lipman et al. to understand the framework behind Stable Diffusion 3 and Flux.
7. **Guidance** – Read Classifier-Free Guidance to understand the core inference trick used by all modern diffusion models.
8. **Text-to-image** – Read DALL·E 2 and Imagen to see diffusion applied to text-conditioned image generation at scale.
9. **Fast generation** – Read Consistency Models for single-step generation without iterative denoising.
10. **Browse Distill.pub** – Explore interactive articles for visual intuition on generative concepts.
