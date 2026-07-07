# Neural Network Fundamentals

## Why This Section Matters

This is where you go from understanding *what* machine learning is to understanding *how* modern deep learning actually works — from the inside out. By building neural networks from scratch, tracing gradients by hand, and developing intuition for how representations are learned, you'll gain the deep understanding needed to work with (and debug) the architectures in later sections. Everything from transformers to diffusion models is built on these fundamentals.

---

## Prerequisites

- [Section 01 — Mathematical Foundations](../01-math-foundations/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Video Series | Neural Networks: Zero to Hero | Andrej Karpathy | 2022 | [Link](https://youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ) | Build neural networks from scratch in Python — from a simple bigram model to a GPT. The single best resource for developing hands-on intuition for how neural networks learn. |
| 🔑 | Video Series | Neural Networks | 3Blue1Brown | — | [Link](https://youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi) | Stunning visual explanations of how neural networks learn, including gradient descent and backpropagation. Perfect complement to Karpathy's code-first approach. |
| 🔑 | Book (Free) | Neural Networks and Deep Learning | Michael Nielsen | 2015 | [Book](http://neuralnetworksanddeeplearning.com/) · [Code](https://github.com/mnielsen/neural-networks-and-deep-learning) | A beautifully written, free online book that builds understanding from first principles. Covers backpropagation, regularization, and universal approximation with clear prose and working code. |
| 🔑 | Blog | Colah's Blog | Christopher Olah | — | [Link](https://colah.github.io/) | Legendary blog posts with exceptional visualizations. Key posts on backpropagation, LSTMs, attention, and neural network representations. A must-read for building intuition. |
| 🔑⭐ | Paper | Keeping Neural Networks Simple by Minimizing the Description Length of the Weights | Geoffrey Hinton, Drew van Camp | 1993 | [Link](https://www.cs.toronto.edu/~hinton/absps/colt93.pdf) | From the Ilya Sutskever reading list. Connects MDL theory to neural network training — the idea that simpler weight configurations generalize better. Foundational for understanding regularization and compression in deep learning. |
| ⭐ | Tutorial | A Tutorial Introduction to the Minimum Description Length Principle | Peter Grünwald | — | — | From the Ilya Sutskever reading list. Accessible introduction to MDL theory, which provides a principled framework for model selection and understanding generalization. |
| | Video Series | MIT 6.S191: Introduction to Deep Learning | Alexander Amini, Ava Amini | — | [Link](https://www.youtube.com/@MITDeepLearning) | MIT's introductory deep learning course. Fast-paced lectures covering core architectures with TensorFlow labs. Good for a structured academic perspective. |
| | Book (Free) | Deep Learning (Chapters 6–8) | Ian Goodfellow, Yoshua Bengio, Aaron Courville | 2016 | [Link](https://www.deeplearningbook.org/) | The "bible" of deep learning. Chapters 6–8 cover feedforward networks, regularization, and optimization — the theoretical backbone of this section. Dense but comprehensive. |

---

## Suggested Order

1. **3Blue1Brown — Neural Networks** — Start here to build visual intuition for what neural networks are doing.
2. **Karpathy — Zero to Hero** — Code neural networks from scratch. This is where the real understanding happens.
3. **Michael Nielsen — Neural Networks and Deep Learning** — Read alongside Karpathy for the theoretical "why" behind the code.
4. **Colah's Blog** — Read key posts (especially on backpropagation and LSTMs) to deepen your visual understanding.
5. **Hinton & van Camp (1993) + Grünwald MDL tutorial** — Explore the connection between compression and generalization.
6. **MIT 6.S191** — Watch for a structured academic overview and additional perspectives.
7. **Goodfellow et al. — Deep Learning (Ch. 6–8)** — Reference for rigorous treatment of optimization, regularization, and network design.
