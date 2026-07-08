# Computational Economics

## Why This Section Matters

Computational economics sits at the intersection of computer science and game theory, asking: how hard is it to compute equilibria, and what happens when agents use efficient learning algorithms instead of solving for Nash equilibrium? This field gave us the price of anarchy (how much efficiency is lost due to selfish behavior), PPAD-completeness (Nash equilibrium is computationally intractable in general), and no-regret learning (agents can achieve good outcomes without even knowing the game). These ideas are directly relevant to ad auction design, online marketplaces, and multi-agent AI systems. If you work in tech, this is where economic theory meets engineering.

## Prerequisites

- [Section 02 — Game Theory](../02-game-theory/README.md)

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book (Free) | Algorithmic Game Theory | Nisan, Roughgarden, Tardos, Vazirani | 2007 | [Link](https://www.cs.cmu.edu/~sandholm/cs15-892F13/algorithmic-game-theory.pdf) | The definitive reference for algorithmic game theory. Covers mechanism design, combinatorial auctions, price of anarchy, online learning. Free PDF. |
| 🔑 | 🎥 Course | Algorithmic Game Theory (CS364A) | Tim Roughgarden, Stanford | — | [Link](https://timroughgarden.org/f13/f13.html) | Excellent lecture notes and problem sets. Roughgarden is the clearest expositor of this material. |
| | 📖 Book | Twenty Lectures on Algorithmic Game Theory | Tim Roughgarden | 2016 | — | More accessible companion to the full reference. Covers equilibrium computation, mechanism design, price of anarchy in 20 self-contained lectures. |
| | 📄 Paper | The Complexity of Computing a Nash Equilibrium | Daskalakis, Goldberg, Papadimitriou | 2009 | [Link](https://dl.acm.org/doi/10.1145/1461928.1461951) | PPAD-completeness of Nash equilibrium. A landmark result at the intersection of CS and game theory. |
| | 📄 Paper | The Multiplicative Weights Update Method: A Meta-Algorithm and Applications | Arora, Hazan, Kale | 2012 | [Link](https://www.cs.princeton.edu/~arora/pubs/MWsurvey.pdf) | Survey of the no-regret learning framework that unifies results across optimization, game theory, and machine learning. |
| | 🎥 Course | Algorithmic Game Theory (CS364B) | Tim Roughgarden, Stanford | — | [Link](https://timroughgarden.org/w14/w14.html) | Advanced follow-up covering more mechanism design and auction theory. |
| | 📖 Book | Prediction, Learning, and Games | Nicolo Cesa-Bianchi & Gabor Lugosi | 2006 | — | Rigorous treatment of online learning, regret minimization, and game-theoretic foundations of prediction. |
| | 📄 Paper | Regret Minimization and the Price of Total Anarchy | Avrim Blum, MohammadTaghi Hajiaghayi, Katrina Ligett, Aaron Roth | 2008 | — | Shows price of anarchy bounds hold even when agents use no-regret dynamics rather than Nash equilibrium. |
| | 📝 Blog | Tim Roughgarden's Page | Tim Roughgarden | — | [Link](https://timroughgarden.org/) | Home page with all course materials, lecture notes, research papers, and talks. |

---

## Suggested Order

1. **Roughgarden — CS364A lecture notes** — Start with these clear, well-structured lecture notes for the best introduction.
2. **Nisan et al. — Algorithmic Game Theory** — Use as the primary reference alongside the lectures. Read chapters on mechanism design, price of anarchy, and online learning.
3. **Daskalakis et al. — "Complexity of Nash" (2009)** — Read to understand why computing Nash equilibrium is fundamentally hard.
4. **Arora et al. — "Multiplicative Weights" (2012)** — Study the unifying framework for no-regret learning.
5. **Roughgarden — Twenty Lectures on AGT** — Read for a more compact, self-contained treatment.
6. **Roughgarden — CS364B** — Explore the advanced material on mechanism design.
7. **Cesa-Bianchi & Lugosi — Prediction, Learning, and Games** — Reference for rigorous online learning theory.
