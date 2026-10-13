# Network Economics

## Why This Section Matters

Network effects are among the most powerful forces in modern economics. When a product becomes more valuable as more people use it, you get winner-take-all dynamics, platform monopolies, and standards wars. Understanding network economics explains why Facebook dominates social networking, why QWERTY persists as a keyboard layout, and why platform businesses like Uber and Airbnb are structured the way they are. This section connects graph theory and network science to economic analysis, covering network externalities, two-sided markets, information cascades, and platform strategy. As more of the economy becomes platform-mediated, this material grows more essential every year.

## Prerequisites

- [Section 01 — Microeconomics](../01-microeconomics/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Solve Easley & Kleinberg's network-effects model for its equilibria, identify the tipping point, and derive a launch-pricing strategy from the dynamics.
- Simulate an information cascade, derive the probability that it locks onto the wrong answer, and explain why cascades are both easy to start and fragile.
- Model threshold adoption on a network, verify the cluster-density condition that blocks cascades, and compare seeding strategies.
- Solve a linear two-sided platform pricing problem and explain, following Rochet & Tirole, why price structure (not just level) matters and when one side should be subsidized.
- Analyze compatibility and lock-in (Katz & Shapiro; Shapiro & Varian) for an open-vs.-proprietary instrument-ecosystem decision.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book (Free) | Networks, Crowds, and Markets | David Easley & Jon Kleinberg | 2010 | [Link](https://www.cs.cornell.edu/home/kleinber/networks-book/) | Outstanding interdisciplinary textbook spanning graph theory, game theory on networks, markets, information cascades, and network effects. Free online. The ideal starting point. |
| | 📖 Book | Platform Revolution | Geoffrey Parker, Marshall Van Alstyne, Sangeet Paul Choudary | 2016 | — | How platforms work, why they win, and how to build them. Accessible business-oriented treatment. |
| | 📄 Paper | Platform Competition in Two-Sided Markets | Jean-Charles Rochet & Jean Tirole | 2003 | [Link](https://www.jstor.org/stable/3590984) | Foundational formal model of two-sided platforms. Tirole won the Nobel Prize partly for this work. |
| | 📄 Paper | Network Externalities, Competition, and Compatibility | Michael Katz & Carl Shapiro | 1985 | [Link](https://www.jstor.org/stable/1816044) | Seminal paper on network effects, technology adoption, and compatibility standards. |
| | 📖 Book | Information Rules | Carl Shapiro & Hal Varian | 1998 | — | Economics of information goods, network effects, lock-in, and standards wars. Prescient and still relevant. |
| | 🎥 Course | Social and Economic Networks | Matthew Jackson, Stanford | — | [Link](https://www.coursera.org/learn/social-and-economic-networks) | Coursera course on network formation, diffusion, learning, and game theory on networks. |
| | 📖 Book | Matchmakers: The New Economics of Multisided Platforms | David Evans & Richard Schmalensee | 2016 | — | Clear treatment of multi-sided platform economics with case studies. |
| | 📝 Blog | Stratechery | Ben Thompson | — | [Link](https://stratechery.com/) | Leading analysis of technology strategy through an economics lens. Developed aggregation theory. |
| | 📝 Article | Metcalfe's Law is Wrong | Bob Briscoe, Andrew Odlyzko & Benjamin Tilly | 2006 | [Link](https://spectrum.ieee.org/metcalfes-law-is-wrong) | Argues a network's value grows roughly like n·log(n), not n², because not all connections are equally valuable — so Metcalfe's law overstates the value of large networks. A needed corrective to n² claims common in crypto valuation arguments (compare btc Section 09). |

---

## Suggested Order

1. **Easley & Kleinberg — Networks, Crowds, and Markets** — Start with this free textbook for a comprehensive, interdisciplinary foundation.
2. **Katz & Shapiro — "Network Externalities" (1985)** — Read the seminal paper on network effects.
3. **Briscoe, Odlyzko & Tilly — "Metcalfe's Law is Wrong"** — Calibrate how fast network value really grows.
4. **Shapiro & Varian — Information Rules** — Read for the classic treatment of information economics applied to tech.
5. **Rochet & Tirole — "Platform Competition" (2003)** — Study the foundational model of two-sided markets.
6. **Evans & Schmalensee — Matchmakers** — Read for case studies applying two-sided market theory.
7. **Jackson — Social and Economic Networks (Coursera)** — Take for network formation and dynamics.
8. **Parker et al. — Platform Revolution** — Read for accessible, modern platform analysis.
9. **Stratechery** — Follow for ongoing applied analysis of platform economics in tech.

---

## 🛠️ Practice

1. **Tipping points by hand** — In Easley & Kleinberg's network-effects model, consumer x values the good at r(x)·f(z) when a fraction z of the population uses it. Take r(x) = 1 − x and f(z) = z. (a) Find the equilibria at price p = 0.16 and classify each as stable or unstable under E&K's dynamic (if people expect z, the fraction that actually buys is 1 − p/z). (b) Find the highest price at which a non-zero equilibrium exists. (c) Plot next-period z against current z for p = 0.16 and p = 0.24. (d) Launch strategy: you can sell at a promotional price for a while — what installed base must you reach before raising the price to 0.16 so the market tips up rather than down? **Check:** z = 0 (stable), 0.2 (tipping point), 0.8 (stable); interior equilibria exist only for p ≤ ¼. *(~2 h · Easley & Kleinberg, Networks, Crowds, and Markets, chapter on network effects; Katz & Shapiro, "Network Externalities, Competition, and Compatibility", on fulfilled expectations)*
2. **Information cascades** — Implement E&K's urn experiment: the state is A or B with prior ½; each agent gets a private signal that is correct with probability q = ⅔, sees all earlier guesses (not signals), guesses the more likely state, and follows its own signal when indifferent. (a) Simulate 20,000 runs of 50 agents and estimate how often the whole population locks onto the wrong state. (b) Derive the same probability analytically by treating agents in pairs. (c) Show how one publicly revealed signal can break a cascade. (d) Name a cascade in your own field — a part, toolchain, or MCU family chosen because "everyone uses it" in forum threads — and the public information that could break it. **Check:** P(wrong cascade) = (1−q)²/(q² + (1−q)²) = 0.2. *(~2.5 h · Easley & Kleinberg, chapter on information cascades)*
3. **Threshold diffusion on graphs** — With networkx, implement E&K's coordination-game adoption: a node switches to the new behavior once at least a fraction q of its neighbors have. (a) Build a small graph by hand where a cascade from two seed nodes stops; find the cluster of density > 1 − q that stops it, and check E&K's cluster theorem. (b) On a Watts–Strogatz and a Barabási–Albert graph (n = 1,000), seed 1% of nodes (random, highest-degree, one dense community) and plot final adoption against q from 0.05 to 0.5; find the critical q for each graph and seeding rule. (c) Translate: an open-source driver library for your instrument spreading among labs — which seeding strategy would you pay for, and why? **Check:** in (a) every node in your blocking cluster has more than 1 − q of its neighbors inside the cluster. *(~3 h · Easley & Kleinberg, chapter on cascading behavior in networks; Jackson, Social and Economic Networks (Coursera), on diffusion)*
4. **Two-sided pricing** — A platform connects instrument users (U) and third-party software developers (D). Participation: N_U = 10 − p_U + 0.3·N_D and N_D = 4 − p_D + 1.2·N_U — developers value each user far more than users value each developer. Profit = (p_U − c_U)·N_U + (p_D − c_D)·N_D. (a) Solve for profit-maximizing prices in sympy with c_U = c_D = 0, then with c_U = 2. (b) Show which side is priced below cost and explain it by the externality each side creates for the other. (c) Keeping c_U = 2, swap the two cross-side coefficients; predict, then verify, what changes. (d) Compare with Rochet & Tirole's claim that the price structure, not only the total level, determines volume. **Check:** with c_U = 2, p_U ≈ 0.86 (below cost) and p_D ≈ 7.66; after the swap developers are paid to join (p_D ≈ −3.66) and users pay ≈ 11.14. *(~3 h · Rochet & Tirole, "Platform Competition in Two-Sided Markets"; Evans & Schmalensee, Matchmakers; Parker, Van Alstyne & Choudary, Platform Revolution)*

**🏗️ Mini-project — Open vs. proprietary instrument ecosystem:** Build an agent-based model of two competing instrument ecosystems: buyers arrive over time and choose on standalone quality, price, installed base (direct network effect: shared scripts, community answers), and the number of third-party tools (indirect effect); switching costs lock in past buyers. Run it (a) with incompatible ecosystems and a small initial installed-base difference, and (b) with one firm adopting an open, compatible interface (e.g., a standard SCPI/VISA command set or an open Python API rival hardware can also implement). Sweep network-effect strength against the quality gap. Then write a 2-page memo for a small instrument maker: when does compatibility beat proprietary lock-in, how do Shapiro & Varian value an installed customer, and what does Stratechery's aggregation lens say about who captures the value? Deliverable: `projects/econ/ecosystem-abm/` + memo. **Success:** incompatible runs tip (one ecosystem ends with > 90% share, and which one wins varies with the random seed when early differences are small); the memo identifies the parameter region where the smaller firm prefers compatibility and checks it against Katz & Shapiro's prediction about which firms favor compatibility. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Why is the lower interior equilibrium in E&K's network-effects model unstable, and what does that imply for launching a product?
2. With r(x) = 1 − x and f(z) = z, what happens to the market if the price is set at 0.3? Why?
3. In the cascade model, why does a cascade begin as soon as two more signals of one kind than the other have been revealed, and why can a little public information overturn it?
4. Distinguish direct and indirect (cross-side) network effects, with one example of each from electronics tools.
5. Why can't a two-sided market be analyzed by looking only at the total price level? When does it pay to price one side below marginal cost?
6. In Katz & Shapiro, which firms favor compatibility and which oppose it — and why?
7. Misconception probe: "Network effects mean the first mover always wins." Give a counterexample and the mechanism that let the later entrant win.
8. Explain to a smart friend in three sentences why an instrument maker might give its software away to win on hardware — or the reverse.
