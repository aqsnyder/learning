# Behavioral Economics

## Why This Section Matters

Behavioral economics documents the systematic ways in which real human behavior deviates from the predictions of standard economic theory. Where classical economics assumes rational, self-interested agents with stable preferences, behavioral economics shows that people are loss-averse, present-biased, influenced by framing, and prone to mental accounting. Richard Thaler pioneered this field by cataloging "anomalies" that standard theory couldn't explain, then showing how these insights could be used to design better policies through "nudges" — small changes to choice architecture that steer people toward better outcomes without restricting freedom. Understanding behavioral economics is essential for realistic mechanism design, policy evaluation, and AI alignment.

> ⚠️ **Read this field with the replication crisis in mind.** Several famous findings have failed large preregistered replications — ego depletion (23 labs, d ≈ 0.04; [Hagger et al. 2016](https://doi.org/10.1177/1745691616652873)) and social priming (see Section 03) — and a well-known honesty study co-authored by Dan Ariely was retracted in 2021 over evidence of fabricated data. Nudges work, but far less than headline studies suggest: DellaVigna & Linos (below) find ~1.4 percentage-point effects at scale versus ~8.7 in published papers. Prefer large, preregistered, field evidence over vivid anecdotes.

## Prerequisites

- [Section 03 — Decision Theory](../03-decision-theory/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Apply Thaler's mental-accounting rules (acquisition vs. transaction utility; segregate gains, integrate losses) to predict choices and redesign a real price presentation.
- Model present bias with β–δ discounting, generate a preference reversal, and design a commitment device in the style of Save More Tomorrow.
- Run a small noise audit, decompose error into bias and noise (level and pattern noise), and measure the effect of a decision-hygiene fix.
- Design and pre-register a choice-architecture experiment with a power analysis, and explain why published nudge effects shrink at scale.
- Critique libertarian paternalism: state its strongest objections and decide where a default on your own product stops being a nudge.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book | Misbehaving: The Making of Behavioral Economics | Richard Thaler | 2015 | — | The autobiographical account of behavioral economics by one of its founders. Covers mental accounting, endowment effect, fairness, and nudges through engaging stories. Essential. |
| 🔑 | 📖 Book | Nudge: Improving Decisions About Health, Wealth, and Happiness | Richard Thaler & Cass Sunstein | 2008 (Final Edition 2021) | [Link](https://www.penguinrandomhouse.com/books/304634/nudge-by-richard-h-thaler-and-cass-r-sunstein/) | The influential book on choice architecture and libertarian paternalism. Shaped public policy worldwide. |
| | 📄 Paper | Mental Accounting Matters | Richard Thaler | 1999 | [Link](https://doi.org/10.1002/(SICI)1099-0771(199909)12:3%3C183::AID-BDM318%3E3.0.CO;2-F) | How people mentally categorize and track money, leading to systematic deviations from rational behavior. |
| | 📄 Paper | Anomalies Series | Richard Thaler | 1987–1991 | [Link](https://www.aeaweb.org/articles?id=10.1257/jep.1.1.197) | Thaler's famous Journal of Economic Perspectives column documenting violations of standard economic theory. |
| | 📄 Paper | Libertarian Paternalism | Richard Thaler & Cass Sunstein | 2003 | [Link](https://www.aeaweb.org/articles?id=10.1257/000282803321947001) | The intellectual foundation for nudge theory. Argues for preserving freedom of choice while steering toward better outcomes. |
| | 📖 Book | Noise: A Flaw in Human Judgment | Daniel Kahneman, Olivier Sibony, Cass Sunstein | 2021 | — | Companion to Thinking, Fast and Slow, focusing on variability (noise) rather than bias in human judgments. |
| | 📖 Book | The Undoing Project | Michael Lewis | 2016 | — | Narrative of the Kahneman–Tversky collaboration that created behavioral economics. Reads like a novel. |
| | 🎥 Course | Behavioral Economics in Action | University of Toronto | — | [Link](https://www.coursera.org/learn/behavioural-economics-in-action) | Applied behavioral economics course on Coursera. Covers nudging, choice architecture, and field experiments. |
| | 📝 Blog | Behavioral Scientist | — | — | [Link](https://behavioralscientist.org/) | Leading online magazine for behavioral science research and practical applications. |
| | 📄 Paper | Psychology and Economics: Evidence from the Field | Stefano DellaVigna | 2009 | [Link](https://www.aeaweb.org/articles?id=10.1257/jel.47.2.315) | The standard survey of behavioral economics in the field, organized by nonstandard preferences (self-control, reference dependence, social preferences), beliefs, and decision-making — plus how firms, employers, and markets respond. The rigorous backbone that the popular books lack. |
| | 📄 Paper | RCTs to Scale: Comprehensive Evidence from Two Nudge Units | Stefano DellaVigna & Elizabeth Linos | 2022 | [Link](https://www.nber.org/papers/w27594) | 126 RCTs covering 23 million people from two U.S. Nudge Units: average effect 1.4 percentage points (8%) versus 8.7 points (33%) in academic journals, largely due to selective publication. The essential calibration for *Nudge*. |
| | 📖 Book | Behavioral Game Theory: Experiments in Strategic Interaction | Colin Camerer | 2003 | [Link](https://press.princeton.edu/books/hardcover/9780691090399/behavioral-game-theory) | How real people play games in the lab (ultimatum and trust games, limited strategic reasoning, learning) and the models built to fit them. Bridges Sections 02 and 06, and is directly relevant to modeling humans in multi-agent AI. |

---

## Suggested Order

1. **Thaler — Misbehaving** — Start here for the most engaging introduction to the entire field.
2. **Thaler — Anomalies Series (JEP)** — Read a few of these columns to see the evidence that motivated the field.
3. **DellaVigna — "Psychology and Economics: Evidence from the Field"** — Get the rigorous map of the field after the stories.
4. **Thaler — "Mental Accounting Matters"** — Understand one of the most important behavioral concepts.
5. **Thaler & Sunstein — "Libertarian Paternalism"** — Read the paper that laid the groundwork for Nudge.
6. **Thaler & Sunstein — Nudge** — Read for the full treatment of choice architecture and its policy implications.
7. **DellaVigna & Linos — "RCTs to Scale"** — Read right after Nudge to calibrate how large nudge effects really are.
8. **Lewis — The Undoing Project** — Enjoy the human story behind the intellectual revolution.
9. **Behavioral Economics in Action (Coursera)** — Take for applied examples and practical frameworks.
10. **Camerer — Behavioral Game Theory** — Study how people actually play the games from Section 02.
11. **Kahneman et al. — Noise** — Read as an advanced companion focusing on judgment variability.
12. **Behavioral Scientist** — Follow for ongoing applied research.

---

## 🛠️ Practice

1. **Mental accounting on your price page** — From "Mental Accounting Matters", write down Thaler's split of a purchase into acquisition utility and transaction utility, and work the beer-on-the-beach example. Then take a real product page (yours or a competitor's: instrument + probes + software license + shipping + warranty) and redesign it twice — once applying the hedonic-editing rules (segregate gains, integrate losses, cancel a small loss against a larger gain, segregate a small gain from a large loss), once deliberately violating them. Give the value-function reason for every design choice, then specify the A/B test you'd run (primary metric, randomization unit, minimum detectable effect). **Check:** each rule traces to concavity of v(·) over gains or convexity over losses — if you can't say which, revisit the value function in Section 03. *(~2.5 h · Thaler, "Mental Accounting Matters"; Thaler, Misbehaving)*
2. **Present bias in code** — Simulate a β–δ agent with β = 0.7, δ = 0.999/day. (a) Show the reversal between $100 today vs. $110 tomorrow and the same pair 30 vs. 31 days out. (b) A task costs 10 utils the day it's done and pays 15 utils 10 days later; it can be done on any of the next 20 days. Simulate when a naive agent (who believes future selves won't be present-biased) and a sophisticated agent (who knows they will be) finish it. (c) Implement a Save More Tomorrow–style escalator and show why committing future raises is easier than raising savings now. **Check:** (a) $100 now beats $110 tomorrow (worth 76.9 today), but at 30 vs. 31 days the $110 wins (74.6 vs. 67.9) — no single exponential discount rate can produce that flip. *(~3 h · Thaler, Misbehaving, on self-control and Save More Tomorrow; Thaler's Anomalies column on intertemporal choice; DellaVigna, "Psychology and Economics" (2009), on present bias; Thaler & Sunstein, Nudge)*
3. **Noise audit with people and models** — Pick a recurring judgment from your work (hours to bring up a new board, the price to quote for a custom build, severity of a field failure). Write 10 short case descriptions. Collect independent judgments from ≥ 5 people, and from one LLM sampled 10× per case at default temperature. Compute, following *Noise*: system noise (SD across judges per case, averaged over cases), level noise (spread of judges' means), pattern noise (the residual), and — once outcomes are known, or against a careful reference estimate — the error equation MSE = bias² + noise². Apply one decision-hygiene fix (averaging independent estimates; a mediating-assessments checklist) and re-measure on 5 new cases. **Check:** system noise² = level noise² + pattern noise² holds in your numbers; averaging n independent judgments cuts noise by about 1/√n. *(~4 h · Kahneman, Sibony & Sunstein, Noise)*
4. **Nudges at scale: replication cards and a power calculation** — Pick three interventions from *Nudge* (automatic enrollment, Save More Tomorrow, one of your choice). For each, write a replication card: original claim and effect size, best evidence at scale, current status, your verdict. Use DellaVigna & Linos (2022, *Econometrica*), which compares nudge trials published in academic journals with every trial run by two US nudge units, and, optionally, the 2022 *PNAS* exchange over whether nudge effects survive publication-bias correction. Compute the sample size per arm needed to detect +1.4 vs. +8.7 percentage points on a 10% baseline (α = 0.05, 80% power) — roughly the nudge-unit vs. academic averages DellaVigna & Linos report; confirm from the paper. Then write 200 words steelmanning the strongest objection to libertarian paternalism and say where you'd draw the line for a default on your own product (e.g., an auto-renewing calibration plan). **Check:** ≈ 7,600 per arm vs. ≈ 250 — the large published effects were cheap to "detect", which is exactly why selective publication inflated them. *(~3 h · DellaVigna & Linos, "RCTs to Scale"; Thaler & Sunstein, Nudge and "Libertarian Paternalism"; Behavioral Scientist coverage of nudge replication; Behavioral Economics in Action course)*

**🏗️ Mini-project — Pre-registered choice-architecture experiment:** Design one intervention for a real decision your customers or colleagues make: a decoy tier on a pricing page (the structure of Ariely's *Economist*-subscription example in *Predictably Irrational*, Section 03 — a hypothesis to test, not an established effect), bundle vs. à-la-carte framing, an opt-out default for a calibration-reminder service, or a commitment device for your own team's chores. Write a pre-registration (hypothesis, primary metric, sample size from a power analysis, stopping rule, analysis code written before any data) on an AsPredicted/OSF template. Run it if you can reach the required n — live traffic, or a hypothetical-choice survey on a panel such as Prolific; if you can't, the deliverable is the pre-registration plus a "no-go" memo stating the effect size you'd need and why it's implausible given Practice 4. Deliverable: `projects/econ/choice-architecture/` (pre-registration, code, results or no-go memo). **Success:** the pre-registration is timestamped before any data; results are reported as an effect with a 95% CI exactly per the pre-registered analysis, including if null. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Define transaction utility and explain the beer-on-the-beach result with it.
2. What is the endowment effect, roughly how large was the gap between selling and buying prices in the classic mug experiments, and how does loss aversion explain it?
3. Write the β–δ discount function and explain how it produces a preference reversal that exponential discounting cannot.
4. What do Thaler and Sunstein mean by libertarian paternalism, and what is the strongest objection to it?
5. In *Noise*, how do bias and noise differ, and why does the error equation make reducing noise as valuable as reducing bias by the same amount?
6. Roughly how many participants per arm do you need to detect a 1-point lift on a 10% conversion rate — hundreds, thousands, or tens of thousands?
7. Misconception probe: "A nudge that raised take-up by 9 points in a published study will raise it by about 9 points when a government rolls it out." Why is this probably wrong?
8. Explain to a smart friend in three sentences why automatic enrollment raises retirement-plan participation so dramatically.
