# Monetary Economics and Crypto

## Why This Section Matters

Money is the most fundamental economic technology — it solves the double coincidence of wants problem, serves as a unit of account, and stores value across time. Understanding the economics of money, banking, and monetary policy is essential for making sense of inflation, interest rates, financial crises, and central bank behavior. The emergence of Bitcoin and cryptocurrency has added an entirely new dimension: programmable money, decentralized consensus, token economics, and DeFi create novel economic systems that can be analyzed with the tools from earlier sections (mechanism design, game theory, information economics). This section bridges traditional monetary theory with the economics of crypto.

## Prerequisites

- [Section 00 — Economic Thinking](../00-economic-thinking/README.md)

---

## 🎯 Learning Objectives

After this section you can:
- Compare the commodity and credit views of money (Ammous vs. Martin, with Hayek's competing currencies) and test "salability" and stock-to-flow claims against Bitcoin's actual issuance schedule.
- Reproduce Nakamoto's double-spend probability, check it against an exact simulation, and turn it into a confirmation policy for real payments.
- Explain proof-of-work security as an economic budget (Budish's flow-vs-stock argument) and project the security budget across future halvings.
- Derive the Barro–Gordon inflation bias of discretionary policy and compute a Taylor-rule policy rate from FRED data.
- Model a stablecoin run as a coordination game with two equilibria and identify what makes a peg robust.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | 📖 Book | The Bitcoin Standard | Saifedean Ammous | 2018 | [Link](https://saifedean.com/thebitcoinstandard/) | Accessible case for Bitcoin as sound money, grounded in Austrian monetary economics. Covers the history of money, monetary policy failures, and Bitcoin's economic design. An advocacy book from a heterodox school: read it as a thesis to test against the mainstream sources in this section, not as settled economics. |
| | 📖 Book | Money: The Unauthorized Biography | Felix Martin | 2013 | — | Engaging history of money from Babylonian clay tablets to modern financial systems. Challenges conventional narratives. |
| | 📖 Book | The Denationalization of Money | F.A. Hayek | 1976 | [Link](https://mises.org/library/denationalisation-money-argument-refined) | Hayek's prescient argument for competing private currencies. Intellectual precursor to cryptocurrency. |
| 🔑 | 📄 Paper | Bitcoin: A Peer-to-Peer Electronic Cash System | Satoshi Nakamoto | 2008 | [Link](https://bitcoin.org/bitcoin.pdf) | The Bitcoin whitepaper. 9 pages that launched a trillion-dollar asset class. Essential reading regardless of your views on crypto. |
| | 📄 Paper | Ethereum Whitepaper | Vitalik Buterin | 2014 | [Link](https://ethereum.org/en/whitepaper/) | Introduced smart contracts and programmable money. Foundation for DeFi and token economics. |
| 🔑 | 🎥 Course | Blockchain and Money | Gary Gensler, MIT | 2018 | [Link](https://ocw.mit.edu/courses/15-s12-blockchain-and-money-fall-2018/) | Full MIT course on blockchain technology, cryptocurrency, and their economic implications. Gensler later chaired the SEC (2021–2025). |
| | 📖 Book | Monetary Theory and Policy | Carl Walsh | 2017 | — | The standard graduate textbook on monetary economics. Rigorous treatment of money demand, central banking, and optimal monetary policy. |
| | 📝 Blog | Vitalik Buterin's Blog | Vitalik Buterin | — | [Link](https://vitalik.eth.limo/) | Deep technical and economic analysis of mechanism design, governance, and crypto economics by Ethereum's creator. |
| | 📖 Book (Free) | Cryptoeconomics | Eric Voskuil | — | [Link](https://github.com/libbitcoin/libbitcoin-system/wiki/Cryptoeconomics) | Rigorous treatment of the economic principles underlying cryptocurrency systems. |

---

## Suggested Order

1. **Martin — Money: The Unauthorized Biography** — Start with this engaging history to understand what money actually is.
2. **Ammous — The Bitcoin Standard** — Read for the Austrian economics perspective and Bitcoin's monetary design.
3. **Nakamoto — Bitcoin Whitepaper** — Read the 9-page paper that started it all.
4. **Hayek — The Denationalization of Money** — Understand the intellectual precursor to cryptocurrency.
5. **Buterin — Ethereum Whitepaper** — Read to understand smart contracts and programmable money.
6. **Gensler — Blockchain and Money (MIT)** — Watch for a comprehensive, structured treatment.
7. **Buterin's Blog** — Follow for ongoing deep analysis of crypto economics and mechanism design.
8. **Voskuil — Cryptoeconomics** — Optional: a Bitcoin-developer perspective on the economic principles behind the protocol.
9. **Walsh — Monetary Theory and Policy** — Reference for formal monetary economics.

---

## 🛠️ Practice

1. **What is money? Yap vs. stock-to-flow** — (a) In 300 words each, steelman Martin's claim that money is transferable credit (his account of Yap's stone money) and Ammous's claim that money is the most salable commodity; end each with one observable prediction that would distinguish them. (b) From the issuance schedule (50 BTC per block, halving every 210,000 blocks, ≈ 52,560 blocks/year), compute Bitcoin's supply and stock-to-flow ratio by year through 2040 and plot them. (c) Read what Hayek's competing issuers would promise in *Denationalisation of Money* — stable purchasing power, not a fixed quantity — and contrast it with Ammous: which property should a medium of exchange optimize? **Check:** after the 2024 halving, supply ≈ 19.69M BTC, flow ≈ 164k BTC/year, S2F ≈ 120; total supply approaches but never reaches 21M. *(~3 h · Martin, Money: The Unauthorized Biography; Ammous, The Bitcoin Standard; Hayek, The Denationalisation of Money)*
2. **Nakamoto's attacker calculation, checked** — (a) Port the whitepaper's C function for the attacker's success probability to Python and reproduce its tables, including the z needed for P < 0.1% at q = 0.10 … 0.45. (b) Simulate the race directly: while the honest chain mines z blocks, the attacker's progress is negative-binomial, not Poisson — compare. (c) Turn it into policy: for attacker share q and order value V, how many confirmations before you ship a $3,000 instrument paid on-chain, at 0.1% vs. 0.01% acceptable risk? **Check:** you match the paper exactly (q = 0.1, z = 5 → 0.0009137; q = 0.45 needs z = 340); the exact race gives ≈ 0.0018 at q = 0.1, z = 5 — about double — because the paper's approximation treats the time for z honest blocks as fixed. *(~2.5 h · Nakamoto, "Bitcoin: A Peer-to-Peer Electronic Cash System"; Gensler, Blockchain and Money (MIT), lectures on consensus)*
3. **Security budget and Budish's critique** — (a) Project miner revenue per block (subsidy + fees) through 2040 under three fee scenarios, in BTC and in USD along a few price paths. (b) Budish (2018, NBER WP 24717), "The Economic Limits of Bitcoin and the Blockchain", is not yet in this section's resource list, so here is its core: free entry makes miners' total per-block cost equal the per-block payment p_block, so an attacker who must out-hash the network for t blocks pays about A·t·p_block (A ≥ 1), and the chain is safe only if the one-off attack value V_attack < A·t·p_block. Derive that inequality from those two steps, then compute the implied maximum safe value at risk per block under your projections. (c) Write a 300-word critique: which assumptions (rentable hash rate, whether attack costs are recoverable, what a crashing coin is worth to an attacker) are strongest and weakest, and how Ammous would respond. **Check:** you can state why, in Budish's model, security scales with the *flow* paid to miners rather than with the coin's market capitalization. *(~3 h · Budish 2018 (outside reading); Nakamoto, section on incentives; Ammous)*
4. **Rules vs. discretion with real data** — (a) Derive the Barro–Gordon result: with Lucas supply y = y* + a(π − πᵉ) and loss ½π² + ½λ(y − ky*)² with k > 1, solve for discretionary inflation under rational expectations and compare it with commitment. (b) Pull PCE inflation, the output gap (CBO potential GDP), and the effective fed funds rate from FRED, and plot the Taylor (1993) rule i = π + 0.5·gap + 0.5(π − 2) + 2 against the actual rate since 1990. (c) Pick the three largest deviations and argue in 200 words whether each was "discretion" in the Barro–Gordon sense or a defensible response to something the rule ignores. **Check:** discretionary inflation = λa(k − 1)y* > 0 with no output gain; the rule called for far higher rates than actual in 2021–22. *(~3 h · Walsh, Monetary Theory and Policy, chapters on discretion and time inconsistency and on policy rules; Dalio's video (Section 00) for the credit-cycle backdrop)*
5. **Run on an algorithmic stablecoin** — Build a small agent-based model of a Terra-style design: a stablecoin redeemable for $1 worth of a volatile "share" token minted on demand. Holders redeem when they expect the peg to fail; redemptions mint share tokens and push their price down; a falling share price raises everyone's expectation of failure. (a) Find the redemption fraction that tips the system into a death spiral. (b) Compare with a fully reserved stablecoin and with a 40% external reserve. (c) Map the model onto a two-equilibrium run/don't-run coordination game (Section 02), and compare the design with the stable-value hedging contract in the "financial derivatives and stable-value currencies" part of the Ethereum whitepaper. **Check:** the algorithmic design shows two stable outcomes (peg holds, collapse) separated by a threshold that moves as reserve backing grows; full reserves remove the bad equilibrium only if redemptions are honored. *(~4 h · Buterin, Ethereum whitepaper; Walsh on money demand; Section 02 coordination games)*

**🏗️ Mini-project — Payments and treasury policy for a hardware shop:** Decide, with numbers, whether a small hardware business should accept bitcoin (on-chain and Lightning) and/or a fiat-backed stablecoin, and whether to hold or convert receipts. Model card fees (≈ 2.9% + $0.30) vs. network fees and a payment processor's spread; confirmations by order size (from Practice 2); the volatility risk of holding receipts for 0, 7, or 30 days (Monte Carlo from historical daily BTC returns; report the 95% VaR per $10k of receipts); chargeback and fraud differences; stablecoin issuer and redemption risk (from Practice 5); and a list of bookkeeping and tax questions to confirm with an accountant. Deliverable: `projects/econ/crypto-payments/` notebook + 2-page policy memo. **Success:** the memo states a concrete policy (which rails, confirmations by order size, convert within X hours) with its expected cost vs. card processing and the 95% VaR for the holding period you choose. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Name money's three functions. Which does Martin treat as fundamental, and how do Yap's stones illustrate it?
2. What does Ammous mean by salability across time, and how does stock-to-flow measure it? Give one reason S2F cannot predict price.
3. Roughly how many new bitcoins are issued per year after the 2024 halving, and what does that make the annual supply growth rate?
4. In Nakamoto's attacker calculation, what is modeled as a gambler's ruin, and why does the attacker's success probability fall exponentially in z when q < p?
5. Why, in Budish's model, does Bitcoin's security depend on the flow paid to miners rather than on its market capitalization?
6. What is time inconsistency in monetary policy, and why does discretion produce inflation with no output gain? Write the Taylor (1993) rule and state the Taylor principle.
7. Misconception probe: "A fixed money supply guarantees stable prices." Why not, and what did Hayek think competing issuers should keep stable?
8. Explain to a smart friend in three sentences how a stablecoin can collapse in a run even if every holder acts rationally.
