# Bitcoin Protocol Fundamentals

> **Why this section matters:** This is the core of Bitcoin — how blocks, transactions, and the blockchain actually work together to create a trustless system.

## Prerequisites
- [01 - Cryptography Foundations](../01-cryptography-foundations/)

> 🛠️ **Start the hands-on lab track now:** [Section 12 — Hands-on Labs](../12-hands-on-labs/README.md) runs in parallel with Sections 02–10. Its Lab 0 (a scripted regtest, signet and pruned-mainnet bench) belongs alongside this section, and this section's exercise 1 runs on it.

---

## 🎯 Learning Objectives

After this section you can:
- Explain the UTXO model and trace how a transaction consumes and creates outputs, contrasting it with an account-based ledger.
- Parse an 80-byte block header field by field and verify its proof-of-work against the target encoded in `bits`.
- Compute a block's Merkle root from its txids (including the odd-count rule), and build and verify a Merkle inclusion proof.
- Drive a regtest node from `bitcoin-cli`, predicting UTXO-set and balance changes before checking them.
- Estimate full-node vs SPV costs — header-chain size, annual chain growth, proof sizes — from first principles.

---

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|------------|------|-------------|
| 🔑 | Book (Free) | Mastering Bitcoin (full book) | Andreas Antonopoulos and David Harding | [bitcoinbook](https://github.com/bitcoinbook/bitcoinbook) | THE technical Bitcoin reference (3rd edition, Dec 2023; covers Taproot) |
| | Website | Learn Me A Bitcoin | Greg Walker | [learnmeabitcoin.com](https://learnmeabitcoin.com/) | Interactive exploration of blocks, transactions, Merkle trees |
| 🔑 | Book (Free) | Grokking Bitcoin | Kalle Rosenbaum | [rosenbaum.se](https://rosenbaum.se/book/) | Best visual explanations of the protocol (Manning, 2019; free to read online under CC BY-NC-SA) |
| | Video | But how does bitcoin actually work? | 3Blue1Brown | [YouTube](https://www.youtube.com/watch?v=bBC-nXj3Ng4) | High-level protocol overview |
| | Documentation | Bitcoin Developer Guide | | [developer.bitcoin.org](https://developer.bitcoin.org/devguide/) | Community-written guide from bitcoin.org — not an official spec, and no longer maintained (© 2009–2020; its RPC reference stops at Bitcoin Core 0.21). Clear conceptual reference, but check BIPs for SegWit/Taproot details |
| 🔑 | Book (Free) | Programming Bitcoin | Jimmy Song | [GitHub](https://github.com/jimmysong/programmingbitcoin) | Build a Bitcoin library from scratch in Python (O'Reilly, 2019; pre-Taproot) |
| | Concept | UTXO model | | | How Bitcoin tracks ownership (vs account model) |
| | Concept | Merkle trees | | | How transactions are efficiently verified |
| | Concept | Block structure | | | Header, nonce, difficulty target, timestamp |

---

## Suggested Order

**Core path (🔑):** *Grokking Bitcoin* → *Mastering Bitcoin* → *Programming Bitcoin*

1. **3Blue1Brown video** — Re-watch with protocol-level focus if needed.
2. **Grokking Bitcoin** — Best starting point for visual learners; builds up the protocol step by step.
3. **Learn Me A Bitcoin** — Explore real blocks, real transactions interactively.
4. **Mastering Bitcoin** — Read cover to cover for the definitive technical treatment.
5. **Concepts** — Make sure you can explain UTXOs, Merkle trees, and block structure clearly.
6. **Programming Bitcoin** — Build it from scratch to cement deep understanding.
7. **Bitcoin Developer Guide** — Reference as needed for protocol-level details.

---

## 🛠️ Practice

1. **Regtest ledger walk** — Start `bitcoind -regtest -fallbackfee=0.0001` (regtest has no fee estimates), create wallets `alice` and `bob`, and mine 101 blocks to Alice — explain why 101. Before mining up to height 200, predict `gettxoutsetinfo`'s `total_amount` and Alice's trusted vs immature balance (hint: regtest halves every 150 blocks — find it in `src/kernel/chainparams.cpp`), then check. Send 1 BTC to Bob, inspect with `getrawtransaction <txid> 2`, `listunspent` and `gettxout`, and draw the UTXO graph by hand: inputs consumed, outputs created, change, fee. While you're at it, start a pruned mainnet node (e.g., `prune=10000`, ~10 GB of recent blocks) — sections 03, 06 and 09 use its headers, peers, mempool and recent blocks. *(~2 h · Mastering Bitcoin chs. 3 and 11; Grokking Bitcoin appendix "Using bitcoin-cli")*
2. **A block header by hand** — Fetch the genesis header and one recent mainnet header (`getblockheader <hash> false`, or mempool.space's `/api/block/<hash>/header`). Parse version, previous-block hash, Merkle root, time, bits and nonce — mind the byte order — then compute double SHA-256, reverse it, and confirm it equals the block hash. Expand `bits` into the target, confirm hash < target, and compute difficulty relative to `0x1d00ffff`. Done when your code reproduces both hashes and your difficulty matches an explorer's. *(~1.5 h · Programming Bitcoin ch. 9; Learn Me A Bitcoin; Bitcoin Developer Guide)*
3. **Full node vs SPV, in numbers** — Estimate first, then measure: (a) today's header-chain size; (b) chain growth per year (≈ 52,560 blocks × the typical block size you see on mempool.space over a month); (c) the size of a Merkle proof for one transaction in a 4,000-transaction block; (d) Satoshi's 4.2 MB-per-year header estimate in whitepaper §7 — redo the arithmetic and project it to today. Deliverable: one table, estimate vs measured, with a sentence explaining every miss larger than 2×. *(~1 h · Bitcoin whitepaper §7–8 (Section 00); Mastering Bitcoin ch. 11)*
4. **Merkle root and inclusion proof** — Pick a mainnet block with an odd number of transactions, fetch its txids (`getblock <hash> 1` on your node, or mempool.space's `/api/block/<hash>/txids`) and compute the Merkle root — internal byte order, duplicate the last hash on odd levels. It must equal the header's root. On regtest, run `gettxoutproof '["<txid>"]'`, parse the resulting `merkleblock` (flag bits plus hashes) with your own code, and verify it; cross-check with `verifytxoutproof`. Finish with a paragraph each on the duplicate-subtree bug (CVE-2012-2459: duplicating the last hash on odd levels lets two different transaction lists share a Merkle root; it was fixed in validation code, not by a soft fork — look it up via the Optech Topics index in Section 11) and the 64-byte-transaction weakness that BIP 54 (Consensus Cleanup, Section 11) addresses. *(~3 h · Programming Bitcoin ch. 11; Mastering Bitcoin ch. 11; Grokking Bitcoin ch. 6)*

**🏗️ Mini-project — Shadow UTXO Set:** Write a Python tool that walks your regtest chain over RPC using only raw data (`getblockhash`, `getblock <hash> 0`), parses every block with your own code (header, varints, legacy and SegWit serialization — strip the witness to compute txids), recomputes each txid and Merkle root, and maintains its own UTXO set. First generate a varied history: ≥ 300 transactions with multiple inputs and outputs, P2PKH/P2WPKH/P2TR outputs, OP_RETURN outputs, and chains of unconfirmed spends. Deliverable: `projects/btc/02-shadow-utxo/`. Success: `serialize(parse(raw)) == raw` for every transaction; every Merkle root matches its header; your UTXO count and total value equal `gettxoutsetinfo`'s `txouts` and `total_amount` exactly — you'll have to discover the two kinds of outputs Bitcoin Core never puts in its UTXO set. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. List the six block-header fields with their sizes. Which one do miners vary first, and what do they change when it runs out?
2. Why is double-spend detection a set-membership check in the UTXO model? What would it be in an account model?
3. A block has 7 transactions. How many levels does its Merkle tree have, and which hashes get duplicated?
4. Roughly how many bytes is a Merkle proof for one transaction in a 4,000-transaction block, and how does that scale as blocks grow?
5. Why can't a coinbase output be spent until it is 100 blocks deep?
6. "My address holds my bitcoin." What does the chain actually record, and what does a wallet actually store?
7. What does an SPV client verify for itself, and what must it trust?
8. Explain to a smart friend, in three sentences, why altering a transaction buried six blocks deep is so expensive.
