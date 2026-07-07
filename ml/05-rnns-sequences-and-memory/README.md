# RNNs, Sequences, and Memory

## Why This Section Matters

Recurrent Neural Networks introduced the idea that neural networks can process sequences and maintain state over time — a fundamental shift from the fixed-input, fixed-output paradigm of feedforward networks. LSTMs and GRUs solved the vanishing gradient problem that plagued vanilla RNNs, enabling learning over long sequences and powering breakthroughs in machine translation, speech recognition, and text generation. Even though transformers have largely replaced RNNs in practice, the concepts here — gating mechanisms, sequence-to-sequence architectures, attention over memory, and external memory — are the intellectual foundation that attention and transformers were built upon. You can't fully appreciate *why* transformers work without understanding what came before them.

## Prerequisites

- [Section 03 — Deep Learning Fundamentals](../03-deep-learning-fundamentals/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read — essential for understanding this topic |
| ⭐ | On the Ilya Sutskever reading list |

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📄 Paper | Long Short-Term Memory | Hochreiter, Schmidhuber | 1997 | [Paper](https://www.bioinf.jku.at/publications/older/2604.pdf) | The original LSTM paper. Introduced gated memory cells to solve the vanishing gradient problem, enabling learning over long time dependencies. |
| 🔑⭐ | 📝 Blog | The Unreasonable Effectiveness of Recurrent Neural Networks | Karpathy | 2015 | [Blog](https://karpathy.github.io/2015/05/21/rnn-effectiveness/) · [Code](https://github.com/karpathy/char-rnn) | Legendary blog post showing char-level RNNs generating Shakespeare, Wikipedia, LaTeX, and C code. The best intuition-builder for what RNNs can learn. |
| 🔑⭐ | 📝 Blog | Understanding LSTM Networks | Olah | 2015 | [Blog](https://colah.github.io/posts/2015-08-Understanding-LSTMs/) | The clearest visual explanation of LSTM internals. Walks through forget, input, and output gates with excellent diagrams. Read this before or alongside the original paper. |
| 🔑⭐ | 📄 Paper | Recurrent Neural Network Regularization | Zaremba, Sutskever, Vinyals | 2014 | [Paper](https://arxiv.org/abs/1409.2329) | Showed how to correctly apply dropout to RNNs (only on non-recurrent connections). Essential for training RNNs that generalize. |
| 🔑⭐ | 📄 Paper | Neural Turing Machines | Graves, Wayne, Danihelka | 2014 | [Paper](https://arxiv.org/abs/1410.5401) | Extended neural networks with external memory and attention-based read/write heads. A landmark paper bridging neural networks and classical computation. |
| ⭐ | 📄 Paper | Pointer Networks | Vinyals, Fortunato, Jaitly | 2015 | [Paper](https://arxiv.org/abs/1506.03134) | Used attention as a pointer to input elements, solving combinatorial problems where output size depends on input. Key precursor to modern attention mechanisms. |
| ⭐ | 📄 Paper | Generating Sequences With Recurrent Neural Networks | Graves | 2013 | [Paper](https://arxiv.org/abs/1308.0850) | Deep dive into sequence generation with RNNs, including handwriting generation and synthesis. Demonstrates the power of recurrent models for complex sequential outputs. |
| | 📄 Paper | Learning Phrase Representations using RNN Encoder–Decoder (GRU) | Cho et al. | 2014 | [Paper](https://arxiv.org/abs/1406.1078) | Introduced the GRU — a simpler alternative to LSTM with comparable performance. Also introduced the encoder-decoder framework for sequence-to-sequence tasks. |
| | 📄 Paper | Sequence to Sequence Learning with Neural Networks | Sutskever, Vinyals, Le | 2014 | [Paper](https://arxiv.org/abs/1409.3215) | The foundational seq2seq paper. Showed an LSTM encoder-decoder could learn to translate between languages end-to-end, sparking the neural machine translation revolution. |

## Suggested Order

1. **Olah — Understanding LSTM Networks** — Start here for visual intuition on gating and memory
2. **Hochreiter & Schmidhuber — LSTM** — Read the original paper with Olah's diagrams fresh in mind
3. **Karpathy — Unreasonable Effectiveness of RNNs** — See what RNNs can do in practice; run the char-rnn code
4. **Cho et al. — GRU** — Understand the simplified gating variant and the encoder-decoder framework
5. **Zaremba et al. — RNN Regularization** — Learn how to train RNNs that don't overfit
6. **Sutskever et al. — Seq2Seq** — The architecture that made neural machine translation work
7. **Graves — Generating Sequences** — Deep generative modeling with RNNs
8. **Graves — Neural Turing Machines** — Stretch your thinking about what neural networks can become
9. **Vinyals — Pointer Networks** — Attention as a computational primitive; bridge to transformers
