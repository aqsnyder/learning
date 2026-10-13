# Industrial Organization and Strategy

## Why This Section Matters

Market power is the everyday economics of running a company. How many competitors can a niche support? How do firms price when each must anticipate the others? When do versions, bundles and discounts pay? Why do mergers of close rivals raise prices, and where does antitrust draw the line? Industrial organization (IO) is the economics of imperfect competition, and competitive strategy is its management-school translation.

For the founder of a small test-and-measurement hardware company the questions are concrete:
- pricing against a few known rivals;
- deciding whether a niche is worth entering;
- designing product versions;
- choosing compatibility and standards (Section 07);
- staying clear of pricing practices that look like collusion, including those of automated pricing tools.

The section builds on monopoly and price discrimination (Section 01), oligopoly and repeated games (Section 02), screening (Section 05) and platforms (Section 07).

**Where it fits:** this section is numbered 15 only because it was added after the original sections. Take it after Section 07.

## Prerequisites

- [Section 01 — Microeconomics](../01-microeconomics/README.md) (monopoly, the Lerner rule, price discrimination)
- [Section 02 — Game Theory](../02-game-theory/README.md) (Cournot, Bertrand, repeated games)
- [Section 05 — Information Economics](../05-information-economics/README.md) (screening and versioning)
- [Section 07 — Network Economics](../07-network-economics/README.md) (two-sided platforms, compatibility)

---

## 🎯 Learning Objectives

After this section you can:
- Compute Bertrand–Nash prices with differentiated (logit) demand, verify each firm's Lerner condition, and simulate the price and consumer-surplus effects of a merger, including the cost saving that would offset them.
- Derive how many firms a niche can support under free entry, and show how business stealing can make entry excessive from society's point of view.
- Compute the discount factors that sustain tacit collusion in Cournot and Bertrand markets, and explain why algorithmic pricing reopens the question of what counts as an agreement.
- Map a real niche onto Porter's five forces with quantitative evidence, and turn each force into a strategic implication.
- Steelman both sides of the current antitrust debate (an evidence-based consumer-welfare approach vs. the structural critique) and apply both to a platform case.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book | Introduction to Industrial Organization (2nd ed.) | Luis Cabral | 2017 | [Link](https://mitpress.mit.edu/9780262035941/introduction-to-industrial-organization/) | A concise, applied undergraduate text covering the core of IO with many real-world examples; rigorous without being heavily technical. The best first IO book for a practitioner (MIT Press). |
| 🔑 | 📝 Article | Market power and regulation (Nobel 2014 popular background) | Royal Swedish Academy of Sciences | 2014 | [Link](https://www.nobelprize.org/prizes/economic-sciences/2014/popular-information/) | Tirole's work in plain language. Simple rules such as price caps or bans on below-cost pricing help in some markets and harm in others. It covers regulating firms whose costs the regulator can't see (menus of contracts), vertical relations, and two-sided platforms. The conclusion: good competition policy differs from market to market. |
| | 📄 Paper | Scientific Background: Market power and regulation | Royal Swedish Academy of Sciences | 2014 | [Link](https://www.nobelprize.org/prizes/economic-sciences/2014/advanced-information/) | The technical companion to the popular background (PDF). |
| | 📖 Book | Industrial Organization: Markets and Strategies (2nd ed.) | Paul Belleflamme & Martin Peitz | 2015 | [Link](https://doi.org/10.1017/CBO9781107707139) | The fuller, more formal IO text (Cambridge University Press). Use it as the reference behind Cabral for the exercises. |
| | 📖 Book | The Economics of Platforms: Concepts and Strategy | Paul Belleflamme & Martin Peitz | 2021 | [Link](https://doi.org/10.1017/9781108696913) | The same authors on platform concepts and strategy (Cambridge University Press): the follow-on to Section 07's two-sided-market readings. |
| | 📝 Article | The Five Competitive Forces That Shape Strategy | Michael E. Porter | 2008 | [Link](https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy) | *Harvard Business Review*, January 2008. Porter's restatement of the five forces: rivalry among competitors, the power of suppliers and of customers, the threat of new entrants, and the threat of substitutes. The management-school bridge from IO to strategy. |
| | 📄 Paper | Amazon's Antitrust Paradox | Lina M. Khan | 2017 | [Link](https://www.yalelawjournal.org/note/amazons-antitrust-paradox) | *Yale Law Journal* 126. The structural critique: a consumer-welfare standard focused on short-run prices misses platform power built through below-cost pricing and vertical integration. One side of a live, contested debate. Read it with Shapiro. |
| | 📄 Paper | Antitrust in a time of populism | Carl Shapiro | 2018 | [Link](https://doi.org/10.1016/j.ijindorg.2018.01.001) | *International Journal of Industrial Organization* 61. Argues for tougher merger enforcement and close scrutiny of the largest firms' specific conduct, but holds that antitrust is "ill suited" to address large firms' political power, inequality or job creation directly. The other side. |
| | 📝 Report | Stigler Committee on Digital Platforms: Final Report | Stigler Center, University of Chicago Booth School of Business | 2019 | [Link](https://www.chicagobooth.edu/research/stigler/news-and-media/committee-on-digital-platforms-final-report) | A policy-oriented report on digital platforms' market power and possible responses, useful as a third, policy-design view next to Khan and Shapiro. |

---

## Suggested Order

**Core path (🔑):** Nobel 2014 popular background → Cabral, *Introduction to Industrial Organization*

1. **Nobel 2014 popular background — "Market power and regulation"** — A one-hour map of the field.
2. **Cabral — Introduction to Industrial Organization** — The core text. Read its treatment of oligopoly, entry, collusion, price discrimination and mergers before the matching exercises.
3. **Porter — "The Five Competitive Forces That Shape Strategy"** — The strategy translation.
4. **Belleflamme & Peitz — Industrial Organization: Markets and Strategies** — Reference for the formal versions of each exercise.
5. **Nobel 2014 Scientific Background** — Optional: the technical treatment of regulation and platforms.
6. **Belleflamme & Peitz — The Economics of Platforms** — After Section 07, for platform strategy and regulation.
7. **Khan, then Shapiro, then the Stigler Committee report** — The antitrust debate, both sides and a policy view.
8. **Cross-links** — Calvano et al. on algorithmic collusion ([Section 08](../08-computational-economics/README.md)); Shapiro & Varian on versioning and lock-in ([Section 07](../07-network-economics/README.md)); screening menus ([Section 05](../05-information-economics/README.md)).

---

## 🛠️ Practice

1. **Merger simulation with logit demand** — Two instrument makers sell differentiated products to M = 10,000 potential buyers a year. A buyer's utility from product j is v_j − α·p_j + ε (logit), with v_A = 2, v_B = 1.5, α = 0.01 per dollar, a marginal cost of $150 for each product, and an outside option worth 0. (a) Derive each firm's first-order condition p_j − c = 1/(α(1 − s_j)), and solve for Bertrand–Nash prices by iterating best responses. (b) Verify the Lerner condition (p − c)/p = 1/|ε_jj| with ε_jj = −α·p_j·(1 − s_j). (c) Merge the firms (one owner sets both prices) and re-solve. Compute the price increases, the change in combined profit, and the change in consumer surplus, using logit CS = (M/α)·ln(1 + Σ e^(v_j − α·p_j)) up to a constant. (d) Find the common marginal-cost saving that would leave consumers as well off as before the merger. **Check:** Nash prices ≈ $283.43 and $270.83, shares ≈ 0.251 and 0.172 (outside option 0.577), Lerner indices ≈ 0.471 and 0.446. After the merger both prices are ≈ $305.78 (+7.9% and +12.9%), combined profit rises ≈ 2.8%, and consumer surplus falls by ≈ $106.5k a year. A cost saving of ≈ $44.80 per unit makes the merger CS-neutral. *(~3 h · Cabral on oligopoly and mergers; Belleflamme & Peitz, Industrial Organization)*
2. **How many firms can a niche support?** — Linear demand P = 600 − Q, marginal cost $150, Cournot competition, and a sunk entry cost F per firm. (a) Show that each of n firms earns ((600 − 150)/(n + 1))², and find the free-entry number of firms for F = $20,000 and for F = $5,000. (b) For F = $20,000, compute consumer surplus, producer surplus net of entry costs, and total surplus with 1, 2 and 3 firms. Which n maximizes total surplus, and why does free entry overshoot it (business stealing)? (c) Translate: what happened to F in your niche when contract manufacturing and open-source tools got cheap, and what does (a) predict? **Check:** n* = 2 at F = $20,000 (a third entrant would earn ≈ $12,656 < F) and n* = 5 at F = $5,000; total surplus is ≈ $55,938 with one firm against ≈ $50,000 with two. *(~2 h · Cabral on entry and market structure; Belleflamme & Peitz on free entry)*
3. **Tacit collusion: thresholds and algorithms** — (a) With the same demand and cost, compute the grim-trigger discount factor that sustains joint-monopoly output for two Cournot firms. The cartel splits monopoly output equally, a deviator plays its best response, and the punishment is Cournot forever. Compare it with Bertrand (δ* = ½) and with n-firm Bertrand (δ* = 1 − 1/n). (b) Which market features (number of firms, price transparency, frequency of interaction, demand growth) raise or lower δ*? (c) Read Calvano et al. (Section 08) and write 300 words: if two Q-learning pricing algorithms settle above Nash prices without communicating, is that an "agreement"? How would Khan's framework and Shapiro's each approach it? **Check:** Cournot δ* = 9/17 ≈ 0.53, from a deviation profit of ≈ $28,477 against $25,312.50 per firm under collusion and $22,500 under Cournot. *(~2.5 h · Cabral on collusion; Calvano et al. (Section 08); Khan; Shapiro)*
4. **Five forces for a niche you know** — Pick a test-and-measurement niche you know well, such as low-cost bench instruments, USB data-acquisition modules or production-test fixtures, but not your own company's product line. For each of Porter's five forces, give at least one number with a source (number of competitors and their shares, buyer concentration, a key supplier's lead time or share of BOM cost, switching costs in hours, the price of the closest substitute such as PC-based or rental instruments) and one strategic implication. End with the force that most constrains price in that niche, and the evidence that would change your mind. **Check:** every force has a sourced number; at least one implication links to a concept from this section or Section 07 (entry costs, differentiation, versioning, compatibility). *(~2.5 h · Porter; Cabral)*
5. **The antitrust debate, steelmanned** — Write 300 words each: Khan's case that the consumer-welfare standard misses platform power, and Shapiro's case for an evidence-based welfare approach with tougher enforcement. Apply both to one concrete conduct question, such as a marketplace ranking its own products first or an app store restricting rival payment systems. Use the Stigler Committee report for at least one policy option. End with a dated, falsifiable prediction about how one such case or rule will turn out. **Check:** each steelman would be acceptable to its author; you name the empirical fact that, if established, would change your view. *(~3 h · Khan; Shapiro; Stigler Committee report; Nobel 2014 background on two-sided platforms)*

**🏗️ Mini-project — Pricing and competitive-strategy memo for a small instrument maker:** Take a realistic but hypothetical instrument line competing with two established rivals. (1) Calibrate a logit demand model from a small set of stated assumptions (prices, market shares, and an elasticity estimate from a price test). Solve for Bertrand–Nash prices with Practice 1's code, and test sensitivity to α and to a rival's price cut. (2) Design a two-version menu (basic and pro features on the same hardware) with Section 05's screening logic. As a warm-up: hobbyists value basic/pro at $300/$350, professionals at $500/$900, and the unit cost is $150; show that the menu ($300 basic, $700 pro) beats selling only the pro version at $900 to professionals if and only if professionals make up less than 3/7 of buyers. (3) Assess entry threats with Practice 2's logic and the five forces from Practice 4. (4) Add a one-paragraph compliance note on automated pricing tools (Calvano et al.; Section 08's mini-project). Deliverable: `projects/econ/15-pricing-strategy/`, a notebook plus a 3-page memo recommending a price and version structure. **Success:** the memo's prices come from an equilibrium you verified by best-response convergence; it reports how the recommendation changes across the plausible range of α; every competitive claim cites a number or a source. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Why does Bertrand competition with identical products drive price to marginal cost? Name three ways real firms escape that outcome.
2. With logit demand, what is a single-product firm's markup, and why does merging two substitutes raise both prices?
3. Under free entry with Cournot competition, how does the number of firms depend on the entry cost, and why can free entry produce too many firms?
4. In your Practice 3 numbers, which is easier to sustain, a Cournot cartel or a Bertrand cartel? What does adding firms do?
5. Name Porter's five forces and, for each, an IO concept that explains it.
6. Misconception probe: "Below-cost pricing is always predatory and should be banned." What does the Nobel 2014 background say about pricing on two-sided platforms, and what does Khan argue courts get wrong about predatory pricing?
7. What is the core disagreement between Khan and Shapiro, and what evidence would settle part of it?
8. Explain to a smart friend in three sentences why a company might deliberately sell a "crippled" version of its own product.
