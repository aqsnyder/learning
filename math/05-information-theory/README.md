# Information Theory

## Why This Section Matters

Information theory quantifies the fundamental limits of communication, compression, and learning. Shannon's entropy measures uncertainty; KL divergence measures the difference between probability distributions (the loss function in variational inference and GANs); mutual information captures statistical dependence (the objective in representation learning). Every time you train a model with cross-entropy loss, you're doing information theory. Understanding these concepts deeply connects statistical learning, coding theory, and the thermodynamics of computation.

---

## Prerequisites

- Section 03 (Probability) — probability distributions, expectation
- Section 02 (Calculus) — logarithms, integration

---

## 🎯 Learning Objectives

After this section you can:
- Compute entropy, joint and conditional entropy, mutual information, and KL divergence, and prove their basic inequalities (Gibbs' inequality, H(X) ≤ log|𝒳|, the chain rule).
- Explain the source-coding theorem operationally and build codes (Huffman, Rice) whose average length approaches the entropy of a real source.
- Compute the capacity of the binary symmetric and AWGN channels, and place real codes (repetition, Hamming) relative to the Shannon limit.
- Estimate the information content of real signals such as text and sensor streams, and recognize the downward bias of plug-in entropy estimates.
- Connect cross-entropy loss to maximum likelihood, and derive the variational identity log p(x) = ELBO + KL used in variational inference.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Elements of Information Theory | Thomas Cover, Joy Thomas | 2006 | — | The standard textbook. Comprehensive coverage of entropy, mutual information, channel capacity, rate-distortion theory, and connections to statistics. Clear exposition with excellent problems. |
| 🔑 | Paper | A Mathematical Theory of Communication | Claude Shannon | 1948 | [Link](https://people.math.harvard.edu/~ctm/home/text/others/shannon/entropy/entropy.pdf) | The founding paper of information theory. Beautifully written and surprisingly accessible. Reading Shannon in the original is a rite of passage. |
| | Book (Free) | Information Theory, Inference, and Learning Algorithms | David MacKay | 2003 | [Link](https://www.inference.org.uk/itprnn/book.pdf) | A brilliant free book connecting information theory to Bayesian inference, error-correcting codes, and neural networks. Unique perspective that bridges multiple fields. |
| | Video Series | Information Theory (playlist) | mathematicalmonk | — | [Link](https://www.youtube.com/playlist?list=PLE125425EC837021F) | Clear video lectures covering entropy, mutual information, KL divergence, and channel coding. Good visual supplement. |
| | Course (Free) | MIT 6.441: Information Theory | Yury Polyanskiy | 2016 | [Link](https://ocw.mit.edu/courses/6-441-information-theory-spring-2016/) | MIT's graduate course on information theory with problem sets and lecture notes (no videos). |
| | Paper | An Introduction to Variational Methods for Graphical Models | Michael Jordan et al. | 1999 | [Link](https://people.eecs.berkeley.edu/~jordan/papers/variational-intro.pdf) | Connects information theory (KL divergence, variational bounds) to probabilistic graphical models. Bridge to modern variational inference. |
| | Blog Post | Visual Information Theory | Chris Olah | 2015 | [Link](https://colah.github.io/posts/2015-09-Visual-Information/) | Gorgeous visual explanations of entropy, cross-entropy, and KL divergence. The best intuitive introduction to these concepts. |
| | Book (Free) | Information Theory: From Coding to Learning | Yury Polyanskiy, Yihong Wu | 2024 | [Link](https://people.lids.mit.edu/yp/homepage/data/itbook-export.pdf) | The modern graduate text (Cambridge University Press) by the MIT 6.441 instructor and Yihong Wu (Yale): classical coding theorems plus the information-theoretic tools now used in statistics and machine learning. The up-to-date successor to Cover & Thomas; the authors' free draft PDF is for personal use. |

---

## Suggested Order

1. **Olah — Visual Information Theory** — Start here for visual intuition about entropy, cross-entropy, and KL divergence.
2. **Shannon — A Mathematical Theory of Communication** — Read the original. It's accessible and historic.
3. **Cover & Thomas — Elements of Information Theory** — The core text. Work through chapters on entropy, mutual information, and data compression.
4. **MacKay — Information Theory, Inference, and Learning Algorithms** — Read for the brilliant connections to Bayesian inference and ML.
5. **mathematicalmonk videos** — Use as a supplement for specific topics.
6. **MIT 6.441 + Polyanskiy & Wu** — Graduate depth and the modern, learning-oriented view. Optional.
7. **Jordan — Variational Methods** — Advanced. Read when tackling variational inference in ML.

---

## 🛠️ Practice

1. **Entropy inequalities by hand** — (a) A fair coin is flipped until the first head; find H(X) in bits (answer: 2). (b) Prove Gibbs' inequality D(p‖q) ≥ 0 via Jensen, and deduce I(X;Y) ≥ 0 and H(X) ≤ log|𝒳|. (c) Prove the chain rule H(X, Y) = H(X) + H(Y | X). (d) Show by example that D(p‖q) ≠ D(q‖p) and that D can be infinite. (e) For a latent-variable model, derive log p(x) = ELBO(q) + D(q(z) ‖ p(z | x)) and explain why maximizing the ELBO tightens a lower bound. Verify (b)–(d) numerically on 1000 random joint distributions with `scipy.stats.entropy`. *(~4 h · Cover & Thomas Ch. 2; Olah, Visual Information Theory; Jordan et al., Variational Methods for Graphical Models; MIT 6.441 problem sets for extra practice)*
2. **The weighing problem** — Solve MacKay's 12-ball puzzle: one ball is heavier or lighter than the rest, and you have three uses of a balance. Then justify it informationally: there are 24 hypotheses (log₂24 ≈ 4.58 bits) and each weighing yields at most log₂3 ≈ 1.58 bits, so three weighings (≤ 4.75 bits) can only work if every weighing's three outcomes are close to equally likely. Write a Python checker that runs your strategy on all 24 cases, confirms it identifies each, and prints the entropy of every weighing's outcome. *(~3 h · MacKay Ch. 4)*
3. **Codes versus the entropy bound** — Implement Huffman coding and apply it to (a) a Project Gutenberg text and (b) a 16-bit sensor log after delta or linear-prediction encoding (code the residuals). Verify H ≤ L̄ < H + 1 bits per symbol, then show that coding pairs and triples closes the gap. Implement a Rice (power-of-two Golomb) coder for the residuals, as FLAC does, and compare bits per sample against Huffman, `zlib`, and `lzma`. *(~4 h · MacKay Ch. 5–6; Cover & Thomas Ch. 5)*
4. **Capacity and real codes** — (a) Compute the BSC capacity 1 − H₂(f) at f = 0.1 (≈ 0.531 bits). (b) Simulate the repetition code R₃ (p_b ≈ 0.028) and Hamming(7,4) with syndrome decoding (p_b ≈ 0.067) over that BSC for 10⁶ bits; add Rₙ for odd n up to 61 using exact binomial tails, and plot (rate, p_b) against the Shannon-limit curve R = C/(1 − H₂(p_b)). (c) From Shannon's Theorem 17, compute the AWGN capacity of a 1 MHz channel at 10 dB SNR (≈ 3.46 Mb/s), and derive the Eb/N₀ → ln 2 (−1.59 dB) limit as bandwidth → ∞ at fixed power. *(~4 h · MacKay Ch. 1, 9–10; Shannon 1948; Cover & Thomas Ch. 7 and 9; mathematicalmonk's channel-coding videos)*
5. **Shannon's approximations to English** — Reproduce Shannon's series of approximations to English from a Gutenberg book: zero-order (27 equiprobable symbols), first-order (letter frequencies), second- and third-order letter Markov models, and first- and second-order word models; generate samples as in the paper. Estimate the conditional entropies H₀ … H₄ in bits per character and compare with the compressed sizes from `gzip`, `bz2`, and `xz`. Show that the plug-in estimate of Hₙ falls with n partly because of finite data — measure cross-entropy on held-out text instead — and relate your numbers to Shannon's estimate that English is roughly 50% redundant. *(~4 h · Shannon 1948; Cover & Thomas's sections on entropy rates and the entropy of English)*

**🏗️ Mini-project — The true bit rate of a sensor:** How many bits per sample does a sensor really produce? Take a real sensor stream (accelerometer or thermistor channel logged from a dev board at a fixed rate, ≥ 10⁶ samples) or a synthetic one (smooth signal plus Gaussian noise of known σ). Estimate its information rate four ways: (1) i.i.d. plug-in entropy of the raw codes; (2) entropy of linear-prediction residuals (least-squares predictor of order 1–8, as in section 01); (3) the actual code length from your Rice/Huffman coder on those residuals; (4) theory: for Gaussian residuals of σ LSB, H ≈ ½·log₂(2πeσ²) bits (≈ 3.63 bits at σ = 3 LSB), from the relation between differential and discrete entropy in Cover & Thomas Ch. 8. Deliverable: `projects/math/05-sensor-entropy/` notebook + a one-page memo recommending a logging format (bits per sample, block size, predictor order) for a flash-constrained data logger, with the compression ratio against raw 16-bit. Success: your coder lands within 0.3 bits/sample of the empirical residual entropy, theory and measurement agree within ~0.2 bits/sample when the residuals are close to white Gaussian, and the memo explains any remaining gap. *(~8 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Define H(X), H(X | Y), I(X;Y), and D(p‖q), and write I(X;Y) as a KL divergence.
2. Why is KL divergence not a metric? Give a two-outcome example of its asymmetry.
3. Why is minimizing cross-entropy loss on a training set the same as maximum-likelihood estimation?
4. Estimate: a 16-bit ADC reads a DC input with 3 LSB rms Gaussian noise. Roughly how many bits per sample does an ideal lossless compressor need, and why is it so far below 16?
5. State the noisy-channel coding theorem in one sentence. What is the capacity of a BSC with crossover probability 0.11?
6. Misconception: "Shannon's theorem says a noisy channel always produces some errors." What does it actually guarantee, and what does that guarantee cost?
7. For the AWGN channel, what happens to capacity as bandwidth → ∞ at fixed power, and where does the −1.59 dB figure come from?
8. Explain to a smart friend in 3 sentences why information is measured as log(1/p).
