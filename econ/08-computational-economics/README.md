# Computational Economics

## Why This Section Matters

Computational economics sits at the intersection of computer science and game theory, asking: how hard is it to compute equilibria, and what happens when agents use efficient learning algorithms instead of solving for Nash equilibrium? This field gave us the price of anarchy (how much efficiency is lost due to selfish behavior), PPAD-completeness (Nash equilibrium is computationally intractable in general), and no-regret learning (agents can achieve good outcomes without even knowing the game). These ideas are directly relevant to ad auction design, online marketplaces, and multi-agent AI systems. The section also covers the other half of computational economics: numerical methods (QuantEcon) and agent-based simulation, including LLM-powered agents. If you work in tech, this is where economic theory meets engineering.

## Prerequisites

- [Section 02 — Game Theory](../02-game-theory/README.md)
- [Section 04 — Mechanism Design](../04-mechanism-design/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Solve two-player zero-sum games as linear programs and verify the minimax theorem as LP duality.
- Implement Multiplicative Weights (Hedge), check its O(√(T log n)) regret bound empirically, and show that time-averaged no-regret play converges to minimax in zero-sum games while the last iterate cycles.
- Compute the price of anarchy of selfish routing (Pigou, Braess, random affine networks) and confirm the 4/3 bound numerically.
- Compute all Nash equilibria of small bimatrix games with support enumeration and Lemke–Howson, and explain why finding one is PPAD-complete while zero-sum games are easy.
- Explain the NE ⊆ CE ⊆ CCE hierarchy, which learning dynamics reach which set, and why price-of-anarchy bounds extend to no-regret outcomes.

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
| | 📖 Book (Free) | QuantEcon Lectures (Quantitative Economics with Python) | Thomas J. Sargent & John Stachurski | — | [Link](https://quantecon.org/lectures/) | Free, continuously updated lecture series on computational economics in Python: dynamic programming, job search, Markov dynamics, optimal savings, asset pricing. Start with "A First Course in Quantitative Economics with Python." The canonical numerical-methods side of computational economics. |
| | 📄 Paper | Large Language Models as Simulated Economic Agents: What Can We Learn from Homo Silicus? | John J. Horton, Apostolos Filippas & Benjamin S. Manning | 2023 | [Link](https://www.nber.org/papers/w31122) | Treats LLMs as simulated economic agents — given endowments, information, and preferences — and re-runs classic behavioral experiments on them. The starting point for LLM-based economic simulation; read skeptically about how far "silicon subjects" generalize to people. |
| | 📄 Paper | Mesa 3: Agent-Based Modeling with Python in 2025 | Ewout ter Hoeven, Jan Kwakkel et al. | 2025 | [Link](https://joss.theoj.org/papers/10.21105/joss.07668) | Paper describing Mesa, the main open-source Python framework for agent-based models; its documentation (mesa.readthedocs.io) has tutorials and example models. Use it to see market and social outcomes emerge from simple agent rules where closed-form equilibria don't exist. |

---

## Suggested Order

1. **Roughgarden — CS364A lecture notes** — Start with these clear, well-structured lecture notes for the best introduction.
2. **Nisan et al. — Algorithmic Game Theory** — Use as the primary reference alongside the lectures. Read chapters on mechanism design, price of anarchy, and online learning.
3. **Daskalakis et al. — "Complexity of Nash" (2009)** — Read to understand why computing Nash equilibrium is fundamentally hard.
4. **Arora et al. — "Multiplicative Weights" (2012)** — Study the unifying framework for no-regret learning.
5. **Blum et al. — "Regret Minimization and the Price of Total Anarchy"** — See why price-of-anarchy bounds survive when agents merely learn.
6. **Roughgarden — Twenty Lectures on AGT** — Read for a more compact, self-contained treatment.
7. **Roughgarden — CS364B** — Explore the advanced material on mechanism design.
8. **QuantEcon Lectures** — Work through the first-course track in Python for the numerical side of the field.
9. **Mesa** — Build a small agent-based model (e.g., Schelling-style segregation or a simple market).
10. **Horton et al. — "Homo Silicus"** — Read on LLM agents as economic subjects; connects to Section 11.
11. **Cesa-Bianchi & Lugosi — Prediction, Learning, and Games** — Reference for rigorous online learning theory.

---

## 🛠️ Practice

1. **Zero-sum games are linear programs** — Write the row player's maximin LP for an m×n zero-sum game and solve it with `scipy.optimize.linprog`; solve the column player's minimax LP and confirm the values match (LP duality is the minimax theorem). Test on rock–paper–scissors, a 3×4 game you make up with a non-obvious value, and compare with nashpy's `linear_program`. **Check:** RPS has value 0 with uniform strategies; row and column values agree to ~1e-9 on every test game. *(~1.5 h · Roughgarden, CS364A lecture deriving the minimax theorem; Nisan et al., Algorithmic Game Theory, chapter on equilibrium computation)*
2. **Hedge from scratch** — Implement Multiplicative Weights as in Arora, Hazan & Kale for n experts with losses in [0,1]. (a) Run it on i.i.d. random losses, on an adversarial sequence that punishes whichever expert currently leads, and on a sequence whose best expert switches halfway; plot regret vs. T against the bound ηT + ln(n)/η with tuned η. (b) Self-play: two Hedge players in rock–paper–scissors and in your 3×4 game from Practice 1 — plot time-averaged and last-iterate strategies. **Check:** regret stays under the bound on every sequence; time averages converge to the LP solution from Practice 1; last iterates cycle or spiral outward instead of converging. *(~3 h · Arora, Hazan & Kale, "The Multiplicative Weights Update Method"; Roughgarden, CS364A lectures on no-regret dynamics; Cesa-Bianchi & Lugosi, Prediction, Learning, and Games)*
3. **Price of anarchy in routing** — (a) By hand: Pigou's example (two links with latencies 1 and x, one unit of traffic) — equilibrium cost, optimal cost, PoA; then Braess's network before and after adding a zero-latency link. (b) Code Frank–Wolfe for nonatomic routing on random networks with affine latencies; compute the equilibrium (Wardrop) flow and the optimal flow (an equilibrium under marginal-cost latencies); record the PoA over 1,000 instances and keep the worst. (c) Repeat with quadratic latencies. **Check:** Pigou PoA = 4/3; Braess raises cost from 1.5 to 2; no affine instance exceeds 4/3; quadratic instances stay under ≈ 1.63, the worst case for degree-2 polynomials. *(~4 h · Roughgarden, CS364A lectures on selfish routing and the price of anarchy; Nisan et al., chapter on routing games)*
4. **Computing Nash: support enumeration vs. Lemke–Howson** — (a) For 200 random 4×4 bimatrix games, find all equilibria with nashpy's `support_enumeration` and count them; then run `lemke_howson` from every initial dropped label — which equilibria does it reach? (b) Time both methods as n grows from 2 to 10 and fit the growth. (c) Build a degenerate game and see how support enumeration behaves (nashpy warns when it finds an even number of equilibria). (d) In 300 words, explain from Daskalakis, Goldberg & Papadimitriou why finding a Nash equilibrium is PPAD-complete (the end-of-the-line structure behind Lemke–Howson paths and Sperner's lemma) and why it is unlikely to be NP-complete (a solution always exists). **Check:** every nondegenerate game has an odd number of equilibria; one Lemke–Howson run finds exactly one, and the set reachable from all labels can miss some. *(~3 h · Daskalakis, Goldberg & Papadimitriou, "The Complexity of Computing a Nash Equilibrium"; Nisan et al., chapters on the complexity of Nash and two-player equilibrium computation; nashpy docs)*
5. **No-regret agents in a congestion game** — 20 agents each pick one of 3 routes with affine latencies and run Hedge on their realized costs for 5,000 rounds. (a) Compare average social cost with the optimum and with the pure Nash equilibria. (b) Record the empirical joint distribution of play and check the coarse-correlated-equilibrium inequalities (no agent gains from any fixed deviation). (c) Using Blum, Hajiaghayi, Ligett & Roth and Roughgarden's smoothness argument, explain why a PoA bound proved for Nash equilibria also covers no-regret outcomes. **Check:** the largest CCE violation shrinks toward 0 as rounds grow; the cost ratio stays below 5/2, the worst case for atomic congestion games with affine costs. *(~3 h · Blum et al., "Regret Minimization and the Price of Total Anarchy"; Roughgarden, Twenty Lectures on Algorithmic Game Theory, on smoothness and robust PoA)*

**🏗️ Mini-project — Algorithmic pricing and tacit collusion:** Do pricing algorithms collude? Build a miniature of the experiment in Calvano, Calzolari, Denicolò & Pastorello (2020, *AER*; not in this section's resource list, and the spec below is enough to start): two firms set prices on a 15-point grid in a repeated logit-demand duopoly; each runs ε-greedy Q-learning with one-period memory of both prices. Compute the static Nash and joint-monopoly benchmarks, then after convergence measure the profit-gain index Δ = (π − π_Nash)/(π_monopoly − π_Nash) across 20 seeds. Run deviation tests: force one firm to undercut for one period and plot both price paths afterward. Then swap in memoryless Hedge learners and compare Δ. Close with a one-page explainer: what this means for pricing your own products with automated tools, and the antitrust question it raises (supra-competitive prices without communication). Deliverable: `projects/econ/algo-collusion/`. **Success:** your Q-learners settle above the Nash benchmark (Δ clearly > 0) in most seeds and you can show whether a forced deviation is punished — or you explain, with evidence, why your learners don't sustain prices above the Nash benchmark. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Multiplicative Weights' regret bound in terms of T and n. What does "no-regret" mean, and against what comparator?
2. Why does the time-average of no-regret play converge to the game's value in zero-sum games, while the last iterate may not?
3. Define the price of anarchy. What is it in Pigou's example, and what is the worst case for nonatomic routing with affine latencies?
4. Explain Braess's paradox in two sentences.
5. What is PPAD, and why is computing a Nash equilibrium unlikely to be NP-complete? What does intractability imply for Nash as a prediction of play?
6. Order NE, CE, and CCE by inclusion. Which set do no-regret dynamics converge to, and which do no-swap-regret dynamics converge to?
7. Misconception probe: "Since computing a Nash equilibrium is intractable, game theory is useless for analyzing AI agents." What's the more careful conclusion?
8. Explain to a smart friend in three sentences how opening a new road can make everyone's commute worse.
