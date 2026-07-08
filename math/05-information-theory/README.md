# Information Theory

## Why This Section Matters

Information theory quantifies the fundamental limits of communication, compression, and learning. Shannon's entropy measures uncertainty; KL divergence measures the difference between probability distributions (the loss function in variational inference and GANs); mutual information captures statistical dependence (the objective in representation learning). Every time you train a model with cross-entropy loss, you're doing information theory. Understanding these concepts deeply connects statistical learning, coding theory, and the thermodynamics of computation.

---

## Prerequisites

- Section 03 (Probability) — probability distributions, expectation
- Section 02 (Calculus) — logarithms, integration

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Elements of Information Theory | Thomas Cover, Joy Thomas | 2006 | — | The standard textbook. Comprehensive coverage of entropy, mutual information, channel capacity, rate-distortion theory, and connections to statistics. Clear exposition with excellent problems. |
| 🔑 | Paper | A Mathematical Theory of Communication | Claude Shannon | 1948 | [Link](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) | The founding paper of information theory. Beautifully written and surprisingly accessible. Reading Shannon in the original is a rite of passage. |
| | Book (Free) | Information Theory, Inference, and Learning Algorithms | David MacKay | 2003 | [Link](https://www.inference.org.uk/itprnn/book.pdf) | A brilliant free book connecting information theory to Bayesian inference, error-correcting codes, and neural networks. Unique perspective that bridges multiple fields. |
| | Video Series | Information Theory (Khan Academy style) | mathematicalmonk | — | [Link](https://www.youtube.com/playlist?list=PLE125425EC837021F) | Clear video lectures covering entropy, mutual information, KL divergence, and channel coding. Good visual supplement. |
| | Course (Free) | MIT 6.441: Information Theory | — | — | [Link](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/) | MIT's graduate course on information theory with problem sets and lecture notes. |
| | Paper | An Introduction to Variational Methods for Graphical Models | Michael Jordan et al. | 1999 | [Link](https://people.eecs.berkeley.edu/~jordan/papers/variational-intro.pdf) | Connects information theory (KL divergence, variational bounds) to probabilistic graphical models. Bridge to modern variational inference. |
| | Blog Post | Visual Information Theory | Chris Olah | 2015 | [Link](https://colah.github.io/posts/2015-09-Visual-Information/) | Gorgeous visual explanations of entropy, cross-entropy, and KL divergence. The best intuitive introduction to these concepts. |

---

## Suggested Order

1. **Olah — Visual Information Theory** — Start here for visual intuition about entropy, cross-entropy, and KL divergence.
2. **Shannon — A Mathematical Theory of Communication** — Read the original. It's accessible and historic.
3. **Cover & Thomas — Elements of Information Theory** — The core text. Work through chapters on entropy, mutual information, and data compression.
4. **MacKay — Information Theory, Inference, and Learning Algorithms** — Read for the brilliant connections to Bayesian inference and ML.
5. **mathematicalmonk videos** — Use as a supplement for specific topics.
6. **Jordan — Variational Methods** — Advanced. Read when tackling variational inference in ML.
