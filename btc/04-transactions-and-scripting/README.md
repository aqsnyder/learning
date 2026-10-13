# Transactions and Script

## Why This Section Matters

Bitcoin transactions are programmable. Understanding the UTXO model, Script language, and transaction types is what separates surface understanding from deep knowledge.

## Prerequisites

- [Section 01 — Cryptography Foundations](../01-cryptography-foundations/README.md), [Section 02 — Protocol Fundamentals](../02-protocol-fundamentals/README.md), [Section 03 — Mining and Consensus](../03-mining-and-consensus/README.md)

## 🎯 Learning Objectives

After this section you can:
- Serialize and parse legacy and SegWit transactions byte by byte, computing txid, wtxid, weight and vsize.
- Implement a stack-based Script interpreter covering P2PKH, P2SH multisig, P2WPKH and P2WSH, and hand-trace its execution.
- Build, sign (legacy sighash and BIP 143) and broadcast transactions from your own code, using keys you generated yourself.
- Design and test timelocked spending paths with nLockTime, CLTV and CSV, and explain every rejection reason you hit.
- Explain how SegWit removed third-party malleability and how the witness discount changes fee arithmetic.

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | Satoshi / Cypherpunk essential canon |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑 | 📖 Book (Free) | Mastering Bitcoin, Chapters 6–7: Transactions; Authorization and Authentication | Antonopoulos & Harding | [GitHub](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch06_transactions.adoc) | The definitive walkthrough of transaction structure (Ch. 6) and Bitcoin Script (Ch. 7: P2SH, OP_RETURN, flow control, Taproot and Tapscript) |
| 🔑 | 🌐 Website | Learn Me A Bitcoin: Transactions | Greg Walker | [Website](https://learnmeabitcoin.com/technical/transaction/) | Interactive, field-by-field transaction dissection, with built-in transaction splitter and builder tools |
| 🔑 | 📖 Book (Free) | Programming Bitcoin, Chapters 5–8 and 13 | Jimmy Song | [GitHub](https://github.com/jimmysong/programmingbitcoin) | Build transaction parsing and Script interpreter from scratch; ch. 13 adds SegWit serialization and signing |
| | 📚 Documentation | Bitcoin Developer Reference: Transactions | — | [Reference](https://developer.bitcoin.org/reference/transactions.html) | bitcoin.org's reference for raw transaction fields — community-maintained and frozen around 2020–21, so check BIPs 141/143/341 for SegWit and Taproot details |
| | 💡 Concept | UTXO model deep dive | — | — | Inputs, outputs, change, coin selection |
| | 💡 Concept | Bitcoin Script | — | — | Stack-based, opcodes, P2PKH, P2SH |
| | 💡 Concept | SegWit (BIP 141) | — | [BIP 141](https://github.com/bitcoin/bips/blob/master/bip-0141.mediawiki) · [BIP 143](https://github.com/bitcoin/bips/blob/master/bip-0143.mediawiki) | Segregated Witness, witness discount, transaction malleability fix; BIP 143 defines the new signature hash (with worked examples) |
| | 💡 Concept | Timelocks | — | — | CLTV (BIP 65), CSV (BIP 112), nLocktime |
| | 🔧 Tool | Bitcoin Transaction Decoder | — | — | Manually decode raw transactions, then check your work with `bitcoin-cli decoderawtransaction` or Learn Me A Bitcoin's transaction splitter |
| | 🛠️ Practice | bitcoin-tx-tutorial (Jupyter notebooks) | Darius Parvin (Chaincode Labs) | [GitHub](https://github.com/chaincodelabs/bitcoin-tx-tutorial) | Build and sign P2PKH, P2SH multisig, P2WPKH, P2WSH and P2TR (key- and script-path) transactions by hand in Python and broadcast them to a local regtest node; extra chapters on sighash flags and timelocks |
| | 🔧 Tool | btcdeb — Bitcoin Script debugger | kallewoof | [GitHub](https://github.com/kallewoof/btcdeb) | Step through Script and Tapscript execution opcode by opcode; used by Learning Bitcoin from the Command Line's scripting chapters (Section 12) |

## Suggested Order

**Core path (🔑):** *Mastering Bitcoin* Chs. 6–7 → Learn Me A Bitcoin: Transactions → *Programming Bitcoin* Chs. 5–8 and 13

1. **Mastering Bitcoin Ch. 6–7** — Start with Antonopoulos for the conceptual framework of transactions and Script
2. **Learn Me A Bitcoin: Transactions** — Visualize and dissect real transactions interactively
3. **UTXO model deep dive** — Internalize inputs, outputs, change, and coin selection
4. **Bitcoin Script** — Understand the stack-based execution model, opcodes, P2PKH, P2SH; step through scripts with **btcdeb**
5. **Programming Bitcoin Ch. 5–8** — Build your own transaction parser and Script interpreter
6. **SegWit (BIP 141)** — Learn witness data, the discount, and the malleability fix
7. **Timelocks** — CLTV, CSV, and nLocktime for time-based spending conditions
8. **bitcoin-tx-tutorial** — Hand-build and sign legacy, SegWit and Taproot transactions in Python against regtest (Taproot background: Mastering Bitcoin Ch. 7 and Section 11)
9. **Bitcoin Developer Reference** — Use as ongoing reference for raw transaction fields
10. **Bitcoin Transaction Decoder** — Decode raw transactions by hand to cement understanding

---

## 🛠️ Practice

1. **Two transactions, every byte** — On regtest, create one P2PKH spend (`getnewaddress "" legacy`) and one P2WPKH spend; dump the raw hex and annotate every field: version, marker and flag, varints, outpoints (little-endian txid + vout), scriptSig or witness items (DER signature + sighash byte, public key), sequence, amounts, scriptPubKeys, locktime. Compute txid, wtxid, weight and vsize yourself. Done when all four match `decoderawtransaction`. *(~2 h · Mastering Bitcoin ch. 6; Learn Me A Bitcoin: Transactions; Bitcoin Developer Reference: Transactions)*
2. **Fee arithmetic** — From field sizes alone, derive the vsize of a 1-input/2-output P2PKH, P2WPKH and P2TR key-path transaction (you should land near 226, 141 and 154 vB), then confirm against transactions you create on regtest. Compute each one's fee at 2 and 50 sat/vB and the percentage saved by SegWit and by Taproot, and explain where the savings come from. *(~1 h · Mastering Bitcoin chs. 6 and 9 (ch. 9 is listed in Section 06); SegWit (BIP 141) concept)*
3. **Script interpreter** — Implement *Programming Bitcoin*'s Script parser and evaluator (chs. 6 and 8): stack operations, OP_HASH160, OP_EQUAL(VERIFY), OP_CHECKSIG, OP_CHECKMULTISIG and P2SH redeem-script evaluation; pass the book's tests. Then hand-trace *Mastering Bitcoin*'s 2-of-3 multisig on paper and in your interpreter, including the extra element OP_CHECKMULTISIG pops and BIP 147's NULLDUMMY rule. *(~6 h · Programming Bitcoin chs. 6 and 8; Mastering Bitcoin ch. 7)*
4. **Your own signer** — On regtest (never with real funds), generate a key with your section-01 library and fund its P2PKH and P2WPKH addresses with `sendtoaddress` (Bitcoin Core ≥ 30 has no `dumpprivkey` — own your keys). Build and sign spends with your own code: legacy sighash for P2PKH, BIP 143 sighash for P2WPKH. Check your BIP 143 digest against the worked examples in BIP 143 before touching the node. Done when `testmempoolaccept` returns `allowed` and both transactions confirm. *(~5 h · Programming Bitcoin chs. 7 and 13; SegWit (BIP 141) concept)*
5. **Timelock lab** — Using your code or embit (Section 10), create P2WSH outputs locked by `<H+10> OP_CHECKLOCKTIMEVERIFY OP_DROP <pk> OP_CHECKSIG` and `<5> OP_CHECKSEQUENCEVERIFY OP_DROP <pk> OP_CHECKSIG`. Attempt each spend too early and with wrong nLockTime/nSequence values, recording every `testmempoolaccept` reject reason (`non-final`, `non-BIP68-final`, script-verification failures), then mine blocks and succeed. Deliverable: a table mapping each failure to the BIP 65/68/112/113 rule that caused it. *(~3 h · Mastering Bitcoin ch. 7; Timelocks concept)*

**🏗️ Mini-project — Mohammed's Company Vault:** Implement *Mastering Bitcoin*'s "Complex Script Example" — 2-of-3 partners; the lawyer plus any one partner after 30 days; the lawyer alone after 90 days — as a P2WSH output on regtest, using block-based relative timelocks (30 and 90 blocks) so you can test quickly. Spend every path with your own signer, show that early spends fail with `non-BIP68-final`, and run every witness through your interpreter (watch P2WSH's MINIMALIF policy on the OP_IF selectors). Finally compute the time-based CSV encodings for real 30- and 90-day delays (type flag plus 512-second units). Deliverable: `projects/btc/04-mohammed-vault/` with scripts, txids and a witness-size table per path. Success: all three paths confirmed; at least three invalid witnesses rejected by both your interpreter and Bitcoin Core for the same reason. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What does a SegWit txid commit to, and why does that eliminate third-party malleability?
2. Trace the stack for a P2PKH spend: what is on it after the scriptSig runs, after OP_DUP, and after OP_EQUALVERIFY?
3. A transaction has 200 bytes of non-witness data and 100 bytes of witness data. What are its weight and vsize?
4. Why does OP_CHECKMULTISIG need a dummy element, and what does BIP 147 require of it?
5. Contrast nLockTime, OP_CHECKLOCKTIMEVERIFY and OP_CHECKSEQUENCEVERIFY: absolute vs relative, transaction-level vs script-level.
6. "This transaction sends coins from address A to address B." Rewrite the sentence correctly in UTXO terms.
7. Where does the difference between total inputs and total outputs go, and what happens if you forget the change output?
8. Explain to a smart friend, in three sentences, how P2SH lets someone pay to a script they have never seen.
