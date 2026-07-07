# Transactions and Script

## Why This Section Matters

Bitcoin transactions are programmable. Understanding the UTXO model, Script language, and transaction types is what separates surface understanding from deep knowledge.

## Prerequisites

- [Sections 01–03](../01-why-bitcoin/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | Satoshi / Cypherpunk essential canon |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑 | 📖 Book (Free) | Mastering Bitcoin, Chapters 6–7: Transactions and Script | Antonopoulos | [GitHub](https://github.com/bitcoinbook/bitcoinbook) | The definitive walkthrough of transaction structure and Bitcoin Script |
| 🔑 | 🌐 Website | Learn Me A Bitcoin: Transactions | — | [Website](https://learnmeabitcoin.com/) | Interactive transaction dissection |
| 🔑 | 📖 Book | Programming Bitcoin, Chapters 5–8 | Jimmy Song | — | Build transaction parsing and Script interpreter from scratch |
| | 📚 Documentation | Bitcoin Developer Reference: Transactions | — | [Reference](https://developer.bitcoin.org/reference/transactions.html) | Official transaction format specification |
| | 💡 Concept | UTXO model deep dive | — | — | Inputs, outputs, change, coin selection |
| | 💡 Concept | Bitcoin Script | — | — | Stack-based, opcodes, P2PKH, P2SH |
| | 💡 Concept | SegWit (BIP 141) | — | — | Segregated Witness, witness discount, transaction malleability fix |
| | 💡 Concept | Timelocks | — | — | CLTV (BIP 65), CSV (BIP 112), nLocktime |
| | 🔧 Tool | Bitcoin Transaction Decoder | — | — | Manually decode raw transactions |

## Suggested Order

1. **Mastering Bitcoin Ch. 6–7** — Start with Antonopoulos for the conceptual framework of transactions and Script
2. **Learn Me A Bitcoin: Transactions** — Visualize and dissect real transactions interactively
3. **UTXO model deep dive** — Internalize inputs, outputs, change, and coin selection
4. **Bitcoin Script** — Understand the stack-based execution model, opcodes, P2PKH, P2SH
5. **Programming Bitcoin Ch. 5–8** — Build your own transaction parser and Script interpreter
6. **SegWit (BIP 141)** — Learn witness data, the discount, and the malleability fix
7. **Timelocks** — CLTV, CSV, and nLocktime for time-based spending conditions
8. **Bitcoin Developer Reference** — Use as ongoing reference for raw transaction fields
9. **Bitcoin Transaction Decoder** — Decode raw transactions by hand to cement understanding
