# Transformers and Attention

## Why This Section Matters

The transformer architecture is the single most important development in modern deep learning. By replacing recurrence with self-attention, Vaswani et al. unlocked massive parallelism in training, enabling models to scale to billions of parameters and learn rich representations from enormous datasets. Every frontier model today — GPT, BERT, PaLM, Gemini, Claude, LLaMA — is a transformer. Understanding the attention mechanism, positional encoding, and the encoder-decoder structure isn't optional; it's the core literacy required for everything in modern AI. This section takes you from the first attention mechanism through the transformer itself and into the foundational models (BERT, GPT) that shaped the field.

## Prerequisites

- [Section 05 — RNNs, Sequences, and Memory](../05-rnns-sequences-and-memory/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read — essential for understanding this topic |
| ⭐ | On the Ilya Sutskever reading list |

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑⭐ | 📄 Paper | Attention Is All You Need | Vaswani et al. | 2017 | [Paper](https://arxiv.org/abs/1706.03762) | The transformer paper. Introduced multi-head self-attention, positional encoding, and the encoder-decoder transformer architecture. The most consequential ML paper of the decade. |
| 🔑⭐ | 📝 Tutorial | The Annotated Transformer | Harvard NLP (Rush) | 2018 | [Tutorial](https://nlp.seas.harvard.edu/annotated-transformer/) · [Code](https://github.com/harvardnlp/annotated-transformer/) | Line-by-line PyTorch implementation of the transformer. Read alongside the original paper to ground every equation in working code. |
| 🔑 | 📝 Blog | The Illustrated Transformer | Alammar | 2018 | [Blog](https://jalammar.github.io/illustrated-transformer/) | Outstanding visual walkthrough of the transformer architecture. Makes self-attention, multi-head attention, and positional encoding intuitive through step-by-step diagrams. |
| 🔑 | 🎥 Video | Let's build GPT: from scratch, in code, spelled out | Karpathy | 2023 | [YouTube](https://www.youtube.com/watch?v=kCc8FmEb1nY) | Karpathy builds a GPT from scratch in ~2 hours. The best way to deeply internalize the transformer architecture through hands-on coding. |
| 🔑 | 📄 Paper | BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding | Devlin et al. | 2018 | [Paper](https://arxiv.org/abs/1810.04805) | Introduced bidirectional pre-training with masked language modeling and next-sentence prediction. Dominated NLP benchmarks and established the pre-train → fine-tune paradigm. |
| | 📄 Paper | Neural Machine Translation by Jointly Learning to Align and Translate (Bahdanau Attention) | Bahdanau, Cho, Bengio | 2014 | [Paper](https://arxiv.org/abs/1409.0473) | The paper that introduced attention to sequence-to-sequence models, allowing the decoder to focus on relevant parts of the input. Direct precursor to the transformer. |
| | 📄 Paper | Improving Language Understanding by Generative Pre-Training (GPT-1) | Radford et al. | 2018 | [Paper](https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf) | The first GPT. Showed that generative pre-training of a transformer on unlabeled text followed by discriminative fine-tuning achieves strong results across diverse NLP tasks. |
| | 🎥 Course | Stanford CS224n: NLP with Deep Learning | Manning et al. | 2021 | [YouTube](https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4) | Comprehensive NLP course covering word vectors, RNNs, attention, transformers, pre-training, and modern NLP applications. |
| | 📝 Blog | The Illustrated BERT, ELMo, and co. | Alammar | 2018 | [Blog](https://jalammar.github.io/illustrated-bert/) | Visual guide to BERT and contextual embeddings. Excellent companion to the BERT paper, explaining masked LM and next-sentence prediction with clear diagrams. |

## Suggested Order

1. **Bahdanau et al. — Attention** — Understand the original attention mechanism in the seq2seq context
2. **Alammar — The Illustrated Transformer** — Build visual intuition before reading the paper
3. **Vaswani et al. — Attention Is All You Need** — Read the transformer paper carefully; refer back to Alammar's diagrams
4. **Harvard NLP — The Annotated Transformer** — Walk through the implementation line by line; run the code
5. **Karpathy — Let's build GPT from scratch** — Code a transformer yourself; solidify understanding through building
6. **Radford et al. — GPT-1** — Understand the generative pre-training approach
7. **Devlin et al. — BERT** — Understand bidirectional pre-training and the masked LM objective
8. **Alammar — The Illustrated BERT** — Visual companion to reinforce BERT concepts
9. **CS224n** — Fill in gaps and get broader NLP context as needed
