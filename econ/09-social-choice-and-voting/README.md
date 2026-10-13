# Social Choice and Voting

## Why This Section Matters

Social choice theory asks a fundamental question: how should a group aggregate individual preferences into a collective decision? Kenneth Arrow's impossibility theorem proved that no voting system can simultaneously satisfy a small set of reasonable axioms — a result that shook the foundations of democratic theory and welfare economics. The Gibbard–Satterthwaite theorem extended this to show that any non-dictatorial voting system is manipulable. These results are not merely theoretical curiosities — they directly inform electoral system design, committee decision-making, fair division, and even AI alignment (how do you aggregate the preferences of multiple humans into an AI's objective function?). This section connects formal social choice theory to practical voting system design.

## Prerequisites

- [Section 02 — Game Theory](../02-game-theory/README.md)
- [Section 04 — Mechanism Design](../04-mechanism-design/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Compute winners under plurality, Borda, instant-runoff, Condorcet/Copeland, and approval for the same profile, and construct profiles where they all disagree.
- State Arrow's conditions precisely and verify the theorem by brute force for the smallest cases (2–3 voters, 3 alternatives).
- Find profitable manipulations under common rules (Gibbard–Satterthwaite), estimate how often they exist, and show how single-peaked preferences escape the theorem.
- Compute and compare cost shares (proportional, Shapley, serial) for a shared-resource problem and test them against the core and Moulin's fairness axioms.
- Explain the discursive dilemma and why aggregating several people's judgments into one AI objective inherits these impossibilities.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book | Social Choice and Individual Values | Kenneth Arrow | 1951 | [Link](https://yalebooks.yale.edu/book/9780300013641/social-choice-and-individual-values/) | The foundational text. Arrow's impossibility theorem proved that no voting system satisfies all desirable properties simultaneously. Short, readable, and historically essential. |
| | 📖 Book | Collective Choice and Social Welfare | Amartya Sen | 1970/2017 | [Link](https://www.hup.harvard.edu/catalog.php?isbn=9780674971608) | Sen's 1970 classic, reissued with eleven new chapters. Shows that Arrow's impossibility stems from informational poverty: allowing interpersonal comparisons of welfare opens the way to reasoned, democratic social choice. Also home of the "liberal paradox." |
| | 📄 Paper | Manipulation of Voting Schemes: A General Result | Allan Gibbard | 1973 | [Link](https://www.jstor.org/stable/1914083) | The Gibbard–Satterthwaite theorem: any non-dictatorial voting system with 3+ alternatives is manipulable. |
| | 📖 Book | Fair Division and Collective Welfare | Hervé Moulin | 2003 | — | Rigorous treatment of fair division problems: cake-cutting, cost sharing, and resource allocation. |
| | 🎥 Video | Arrow's Impossibility Theorem | PBS Infinite Series | — | [Link](https://www.youtube.com/watch?v=AhVR7gFMKNg) | Accessible 15-minute explanation of Arrow's theorem with clear examples. |
| | 📝 Article | Voting Methods | Stanford Encyclopedia of Philosophy | — | [Link](https://plato.stanford.edu/entries/voting-methods/) | Excellent philosophical overview of voting methods, their properties, and trade-offs. |
| | 📖 Book | Gaming the Vote | William Poundstone | 2008 | — | Popular account of voting paradoxes, spoiler effects, and alternative voting systems. Engaging and accessible. |
| | 📄 Paper | Judgment Aggregation: A Survey | Christian List & Clemens Puppe | 2009 | — | Extends social choice from preference aggregation to judgment aggregation — relevant for AI alignment. |
| | 📄 Paper | Quadratic Voting: How Mechanism Design Can Radicalize Democracy | Steven P. Lalley & E. Glen Weyl | 2018 | [Link](https://www.aeaweb.org/articles?id=10.1257/pandp.20181002) | Voters buy votes from a budget of "voice credits" at quadratic cost, so outcomes reflect how strongly people care, not just which side they're on. Short and readable; the idea behind quadratic voting and funding experiments in crypto communities (Section 10). |
| | 📖 Book (Free) | Handbook of Computational Social Choice | Felix Brandt, Vincent Conitzer, Ulle Endriss, Jérôme Lang & Ariel D. Procaccia (eds.) | 2016 | [Link](https://cgi.cse.unsw.edu.au/~haziz/comsoc.pdf) | Free PDF of the standard reference on the computer-science side of social choice: computing winners, complexity of manipulation, fair division, matching, and judgment aggregation. Pairs with Section 08's algorithmic view. |
| | 📄 Paper | Social Choice Should Guide AI Alignment in Dealing with Diverse Human Feedback | Vincent Conitzer, Rachel Freedman, … Stuart Russell, … William S. Zwicker | 2024 | [Link](https://arxiv.org/abs/2404.10271) | Position paper arguing that aggregating many people's feedback in RLHF-style alignment is a social choice problem, and that the field's axioms and voting rules should shape how it's done. A direct answer to this section's question about aggregating many humans into one AI objective. |

---

## Suggested Order

1. **PBS Infinite Series — Arrow's Impossibility Theorem** — Start with this short video for an intuitive understanding.
2. **Arrow — Social Choice and Individual Values** — Read the foundational text. It's short and surprisingly accessible.
3. **Gibbard — "Manipulation of Voting Schemes"** — Understand why strategic voting is unavoidable.
4. **Stanford Encyclopedia — Voting Methods** — Read for a broader philosophical context.
5. **Sen — Collective Choice and Social Welfare** — Study for extensions and welfare economics perspective.
6. **Lalley & Weyl — "Quadratic Voting"** — See mechanism design applied to voting itself.
7. **Moulin — Fair Division and Collective Welfare** — Explore the fair division branch of social choice.
8. **Handbook of Computational Social Choice** — Dip into chapters on manipulation complexity and fair division as reference.
9. **List & Puppe — "Judgment Aggregation: A Survey"** — Extend from aggregating preferences to aggregating judgments.
10. **Conitzer et al. — "Social Choice Should Guide AI Alignment"** — Connect the whole section to aggregating human feedback for AI.
11. **Poundstone — Gaming the Vote** — Enjoy as an accessible capstone on voting system design.

---

## 🛠️ Practice

1. **One profile, four winners** — Fifteen voters over A–D: 5 × A≻B≻C≻D, 2 × A≻C≻D≻B, 3 × B≻C≻D≻A, 5 × D≻C≻B≻A. By hand, find the plurality, Borda, instant-runoff, and Condorcet winners, and check how the plurality winner does head-to-head. Confirm with the `pref_voting` library. Then search randomly for (a) the smallest profile with four different winners and (b) a profile where instant-runoff violates monotonicity (raising the winner on some ballots makes it lose). **Check:** plurality A, Borda C, IRV D, Condorcet B — and A loses every pairwise contest, so a Condorcet loser wins plurality. *(~2 h · Stanford Encyclopedia of Philosophy, "Voting Methods"; Poundstone, Gaming the Vote; PBS Infinite Series video on Arrow's theorem)*
2. **Arrow's theorem by brute force** — For 2 voters and 3 alternatives with strict rankings: by IIA, a social welfare function is fixed by one rule per pair of alternatives mapping the voters' pairwise preferences to a social one; Pareto pins two of the four inputs, leaving 4 rules per pair and 4³ = 64 candidates. Enumerate them, keep those whose social ranking is transitive on all 36 profiles, and inspect the survivors. Repeat for 3 voters (2⁶ rules per pair, 216 profiles; vectorize with numpy). Then write a one-page proof sketch of the general theorem in your own words (decisive sets or the pivotal voter) and point to where your brute force used each axiom. **Check:** exactly 2 survivors for 2 voters and 3 for 3 voters — the dictatorships. *(~3 h · Arrow, Social Choice and Individual Values; Sen, Collective Choice and Social Welfare, formal chapters)*
3. **Manipulation in practice** — (a) In the Practice 1 profile, find a group of voters who gain by misreporting under Borda, and one under IRV. (b) Under impartial culture (uniformly random rankings), estimate for n ∈ {5, 15, 51} and 3–4 candidates how often a single voter can profitably manipulate plurality, Borda, IRV, and Copeland (fix a deterministic tie-break), and how often a coalition of ≤ 3 can. (c) Restrict every ballot, sincere or strategic, to single-peaked orders on a line (odd n): verify by search that "elect the Condorcet winner" can no longer be manipulated, and explain why this doesn't contradict Gibbard–Satterthwaite. **Check:** in (a) the five A≻B≻C≻D voters can elect B under Borda by ranking B first, and the same move elects B under IRV; every rule in (b) is manipulable on some profile, as Gibbard's theorem requires; (c) finds no profitable manipulation. *(~3 h · Gibbard, "Manipulation of Voting Schemes"; SEP, "Voting Methods"; pref_voting)*
4. **Sharing a pick-and-place line** — Three small hardware firms share leased SMT capacity: each machine costs $3,000/month and provides 50 hours; operating cost is $15/hour. Monthly demand: 10, 30, and 60 hours. (a) Compute every coalition's stand-alone cost. (b) Compute cost shares under proportional-to-hours, the Shapley value, and Moulin–Shenker serial cost sharing. (c) Test each against the core (no coalition pays more than its stand-alone cost). (d) Say which of Moulin's fairness axioms each rule satisfies, which you'd propose to the other two firms, and why. **Check:** Shapley $1,150 / $1,450 / $4,900 and proportional $750 / $2,250 / $4,500 are in the core; serial $1,150 / $2,950 / $3,400 is not — firms 1 and 2 would pay $4,100 together but could lease their own machine for $3,600. *(~3 h · Moulin, Fair Division and Collective Welfare, chapters on cost sharing)*
5. **The discursive dilemma, for products and AIs** — Three co-founders vote on "ship now?", defined as (EMC passes) ∧ (firmware is stable). Build individually consistent votes where premise-by-premise majorities say ship but the majority on the conclusion says don't. Then use List & Puppe to state the general impossibility for judgment aggregation and show what each escape route (premise-based, conclusion-based, sequential priority) decides here. Finally, write 200 words on what this means for an AI assistant combining instructions from several users ("ship only if both checks pass" vs. "most of you want to ship"). **Check:** your table has three logically consistent judges and a majority judgment set that is logically inconsistent. *(~2 h · List & Puppe, "Judgment Aggregation: A Survey"; SEP, "Voting Methods")*

**🏗️ Mini-project — Voting-rule lab and a rule for your team:** Build (or extend `pref_voting` into) a simulator comparing plurality, two-round runoff, instant-runoff, Borda, Copeland, approval, and score voting across preference models (impartial culture; 1-D and 2-D spatial with noise). Measure Condorcet efficiency, spoiler frequency (does removing a losing candidate change the winner?), monotonicity failures, single-voter manipulability, and average voter utility in the spatial models. Reproduce one pathology per rule as a minimal concrete profile. Then choose and justify a decision rule for a real recurring group choice — feature prioritization with a customer advisory board, a meetup's talk selection, a team's tooling decisions. Deliverable: `projects/econ/voting-lab/` notebook + 2-page write-up with plots. **Success:** each pathology has a minimal reproducible profile; the recommended rule's trade-offs are stated as numbers from your simulations, not adjectives. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Arrow's conditions and the theorem. Which of the conditions do Borda and instant-runoff give up?
2. Why doesn't Arrow's theorem bite with only two alternatives, and what does May's theorem say about majority rule there?
3. Construct a three-voter Condorcet cycle from memory.
4. Describe instant-runoff's monotonicity failure with a small example.
5. State Gibbard–Satterthwaite. Which assumption does single-peakedness relax, and why does that make the median voter's choice strategy-proof?
6. What is Sen's "impossibility of a Paretian liberal", and how does his *Lady Chatterley's Lover* example work?
7. Misconception probe: "Arrow proved all voting systems are equally bad." What does the theorem actually rule out, and what does it leave open (e.g., cardinal ballots)?
8. Explain to a smart friend in three sentences why a third candidate can "spoil" a plurality election and how ranked or approval ballots change that.
