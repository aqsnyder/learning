# Economic Thinking

## Why This Section Matters

Economics is fundamentally a way of thinking — a framework for understanding how people respond to incentives, make tradeoffs, and coordinate through markets. Before diving into formal models, you need to internalize the core principles: opportunity cost, marginal analysis, the power of prices, and the seen-vs-unseen effects of policies. These mental models will reappear in every subsequent section, from game theory to mechanism design to AI alignment. Economists don't just study markets — they study human decision-making, and that's what makes this foundation essential.

## Prerequisites

None; this is the starting section.

---

## 🎯 Learning Objectives

After this section you can:
- Separate sunk, fixed, and marginal costs in a real decision and make the call at the margin — e.g., accept an order priced below average total cost but above marginal cost — including the opportunity cost of scarce capacity.
- Solve a linear supply–demand market for equilibrium, consumer and producer surplus, tax incidence, and deadweight loss, and predict which side bears a tax from relative elasticities.
- Trace a policy's seen and unseen effects across groups and over time (Hazlitt's "one lesson"), and name the conditions under which that lesson misleads (externalities, idle resources).
- Explain how prices coordinate thousands of strangers without central direction ("I, Pencil") using a concrete electronics supply-chain example.
- Describe Dalio's three forces (productivity growth, short-term and long-term debt cycles) and four deleveraging levers, and explain why spending cuts alone can make debt burdens worse.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book | Principles of Economics (10th ed.) | N. Gregory Mankiw | 2024 | [Link](https://cengage.com/c/principles-of-economics-10e-mankiw/9780357722718) | The canonical introductory economics textbook. Covers the 10 principles of economics, supply and demand, market outcomes, externalities, and public goods. Clear writing with excellent real-world examples. |
| | 📖 Book (Free) | The Economy 2.0 (Microeconomics and Macroeconomics volumes) | CORE Econ team | 2023 | [Link](https://books.core-econ.org/the-economy/index.html) | Free, modern introductory text built around real problems (inequality, innovation, climate, social dilemmas), using game theory and incentive problems from the start. The best free alternative to Mankiw, and the easiest way to cover the macroeconomics (growth, unemployment, inflation) that this curriculum otherwise skips. |
| | 📖 Book | The Undercover Economist | Tim Harford | 2005 | — | Accessible popular introduction to economic reasoning in everyday life. Great for building intuition before tackling formal models. |
| 🔑 | 🎥 Course | Khan Academy Microeconomics | Khan Academy | — | [Link](https://www.khanacademy.org/economics-finance-domain/microeconomics) | Free, comprehensive introduction to microeconomic concepts. Covers supply/demand, elasticity, consumer/producer surplus, market failures. Ideal for visual learners. |
| | 🎥 Course | Principles of Microeconomics | MRUniversity (Tyler Cowen, Alex Tabarrok & Joana Girante) | — | [Link](https://learn.mru.org/courses/principles-of-microeconomics) | Short, engaging video lectures on core economic concepts. Excellent supplement to a textbook. |
| | 📖 Book | Economics in One Lesson | Henry Hazlitt | 1946 | — | Classic short book on the seen and unseen effects of economic policies. Trains you to think about second-order consequences. |
| | 📝 Article | "I, Pencil" | Leonard Read | 1958 | [Link](https://fee.org/resources/i-pencil/) | Famous essay illustrating the astonishing complexity of market coordination through the simple example of a pencil's production. |
| | 📝 Blog | Marginal Revolution | Tyler Cowen & Alex Tabarrok | — | [Link](https://marginalrevolution.com/) | The most influential economics blog. Daily posts covering economics, policy, culture, and ideas. Essential for staying current. |
| | 🎥 Video | How The Economic Machine Works | Ray Dalio | 2013 | [Link](https://www.youtube.com/watch?v=PHe0bXAIuk0) | Popular 30-minute animated overview of Dalio's own debt-cycle model — credit cycles, deleveraging, and monetary policy made intuitive. A useful mental model, but one investor's framework rather than textbook macroeconomics; check it against CORE's macro volume. |

---

## Suggested Order

**Core path (🔑):** Khan Academy Microeconomics → Mankiw, *Principles of Economics*

1. **Ray Dalio — How The Economic Machine Works** — Optional 30-minute warm-up: one investor's model of credit cycles, not textbook macroeconomics. Treat it as a hypothesis to check against CORE's macro volume (step 5) and [Section 14](../14-macroeconomics-money-and-financial-markets/README.md).
2. **Leonard Read — "I, Pencil"** — Read this short essay to appreciate the power of market coordination.
3. **Khan Academy Microeconomics** — Work through the modules for a structured visual introduction to core concepts.
4. **Mankiw — Principles of Economics** — Read the first 10-15 chapters alongside or after Khan Academy for depth and rigor.
5. **CORE Econ — The Economy 2.0** — Use as a free alternative or complement to Mankiw; read the Macroeconomics volume for growth, unemployment, inflation, and monetary policy basics. [Section 14](../14-macroeconomics-money-and-financial-markets/README.md) builds on it.
6. **MRUniversity — Principles of Microeconomics** — Use as a supplement for topics that need reinforcement.
7. **Hazlitt — Economics in One Lesson** — Read to train second-order thinking about policy effects.
8. **Harford — The Undercover Economist** — Enjoy as a capstone to solidify economic intuition through real-world stories.
9. **Marginal Revolution** — Subscribe and read regularly to build ongoing economic literacy.

---

## 🛠️ Practice

1. **Supply, demand, and a $3 tax** — Market: Qd = 1000 − 20P, Qs = −200 + 40P. By hand: equilibrium, consumer and producer surplus; then a $3/unit tax on sellers — price buyers pay, price sellers keep, revenue, deadweight loss, each side's share of the burden; then a price ceiling at $16 — shortage and minimum deadweight loss. Re-derive everything in a ~30-line Python script that also draws the diagram. **Check:** P* = $20, Q* = 600; buyers bear $2 of the $3 (demand elasticity −0.67 vs. supply +1.33 at equilibrium); DWL = $60; the ceiling leaves a 240-unit shortage and at least $960 of DWL — explain why random rationing among buyers makes the real loss larger than that triangle. *(~2 h · Mankiw, chapters on supply and demand, elasticity, and the costs of taxation; Khan Academy tax-incidence and deadweight-loss modules)*
2. **The below-cost order** — You sell a bench instrument at $249, 60 units/month. Marginal cost: BOM $64 + assembly $12 + test/pack $6. Overhead is $5k/month; $28k of design and tooling is already spent. A distributor in a region you don't serve offers $115/unit for 200 units within 6 weeks. (a) Average total cost at current volume (amortize the $28k over 24 months) and the order's contribution. (b) Your assembler can build 150 units/month for you (pro-rate it over the 6 weeks), so the order pushes some of your own units back a month; half of those customers buy elsewhere — recompute. (c) Name three non-price reasons to refuse (gray-market leakage back into your channel, anchoring your list price, support load) and put a dollar figure on one. Deliverable: half-page decision note. **Check:** ATC ≈ $185 > $115, yet naive contribution is $6,600; after the capacity opportunity cost it falls to ≈ $1,170. Neither the $28k nor the $5k/month appears in the accept/reject arithmetic — if yours does, you've mixed sunk/fixed costs into a marginal decision. *(~1.5 h · Mankiw on costs of production and "rational people think at the margin"; Harford, The Undercover Economist, on scarcity power and margins)*
3. **Seen and unseen: a tariff on your BOM** — Start from a recent Marginal Revolution post on trade or industrial policy, then apply its logic to your own product: a 25% tariff hits the $40 of imported parts in that $64 BOM. Write a Hazlitt-style analysis (500 words + table): who gains visibly, who loses invisibly (your customers, hires you don't make, downstream firms, export customers facing retaliation), short run vs. long run. Quantify one unseen cost: per-unit cost increase, the price rise if you pass through half, and lost units at a demand elasticity of −2. Close with one paragraph steelmanning a case Hazlitt's lesson handles badly (an externality, or a demand shortfall with idle capacity). **Check:** +$10/unit cost, +$5 price (+2%), ≈ −4% units; your table names at least two affected groups absent from any press release. *(~2 h · Hazlitt, Economics in One Lesson, chapters on the broken window and on tariffs; Mankiw on international trade; Marginal Revolution)*
4. **"I, Pencil" for a microcontroller** — Pick one part on your bench (an STM32, an 0402 MLCC, a USB-C receptacle). Draw its supply web: ≥ 15 nodes spanning raw materials, process equipment, fabs, packaging, logistics, and distribution, with countries. Then use the 2021–22 MCU shortage (or the 2018 MLCC shortage) to trace two price signals and the decentralized responses they triggered — redesigns to alternate parts, broker markets, capacity investment — that nobody ordered. Deliverable: diagram + 300 words. **Check:** you can name a decision made by someone who never learned *why* the price moved — Read's point that no single person knows how to make the part. *(~2 h · Read, "I, Pencil"; MRUniversity videos on the price system)*
5. **Dalio's machine in ~60 lines** — Simulate one aggregate economy in Python: income each period = last period's total spending; spending = income + new borrowing − debt service; borrowing is a fixed fraction of income while debt service/income stays under a limit; a central bank cuts rates when spending growth falls below 2%/yr productivity growth and raises them when it's above. Plot income, debt/income, and the policy rate over 100+ simulated years; mark the short-term cycles and the long-term peak where rates hit zero. Then run four deleveraging scenarios — spending cuts only, debt write-downs, transfers, and "printing" money to buy debt — and a mix. **Check:** using "one person's spending is another person's income", explain what your cuts-only run does to debt/income, and whether your mix achieves Dalio's "beautiful deleveraging" (nominal income growth above the nominal interest rate). *(~4 h · Dalio, "How The Economic Machine Works"; numpy/matplotlib)*

**🏗️ Mini-project — Unit-economics model and pricing memo:** Build a small Python (or spreadsheet) model of a hardware product's economics — volume-tiered BOM, assembly and test, NRE amortization, monthly overhead, channel margins — that outputs contribution margin, break-even volume, and monthly cash flow. Use it to decide three marginal questions: (1) add a $9/unit feature you expect to lift sales 10%; (2) run a 15%-off launch week; (3) bring assembly in-house with a $35k pick-and-place machine. Write a one-page memo with a "seen vs. unseen" box (e.g., discounts teaching customers to wait for the next sale; pulled-forward demand). Deliverable: `projects/econ/00-unit-economics/` (model + memo). **Success:** changing monthly overhead moves break-even volume but not your answers to (1) and (2); you state the volume lift (and implied elasticity) at which the launch discount breaks even. *(~8 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Mankiw's principle "the cost of something is what you give up to get it", and give a case from your own work where accounting cost and opportunity cost differ.
2. Why should a sunk cost never enter a forward-looking decision — and when is a cost that looks sunk actually recoverable?
3. A tax is levied on sellers of a good with inelastic demand and elastic supply. Who bears most of it, and why doesn't it matter whether the law names buyers or sellers?
4. If a tax doubles, roughly what happens to its deadweight loss, and why?
5. Misconception probe: "The broken window gives the glazier work, so it's good for the economy." What is Hazlitt's rebuttal, and under what macroeconomic conditions would a Keynesian partly disagree?
6. In "I, Pencil", what does the pencil claim no single person knows, and what does that imply for central planning?
7. What turns Dalio's short-term debt cycle from expansion to recession, and what are his three rules of thumb?
8. Explain to a smart friend in three sentences why water is cheap and diamonds are expensive even though water is far more useful.
