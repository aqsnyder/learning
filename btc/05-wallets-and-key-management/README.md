# Wallets and Key Management

## Why This Section Matters

"Not your keys, not your coins." Understanding how wallets work, from seed phrases to HD derivation paths, is critical for both users and developers.

## Prerequisites

- [Section 01 — Why Bitcoin](../01-why-bitcoin/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | Satoshi / Cypherpunk essential canon |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑 | 📖 Book (Free) | Mastering Bitcoin, Chapter 5: Wallets | Antonopoulos | [GitHub](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch05_wallets.adoc) | HD wallet theory, key derivation, and wallet architecture |
| 🔑 | 🌐 Website | Learn Me A Bitcoin: HD Wallets | — | [Website](https://learnmeabitcoin.com/) | Visual HD wallet derivation |
| 🔑 | 📜 Standard | BIP 32: Hierarchical Deterministic Wallets | — | [BIP 32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) | The HD wallet standard |
| | 📜 Standard | BIP 39: Mnemonic Seed Phrases | — | [BIP 39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) | How 12/24 word seeds work |
| | 📜 Standard | BIP 44: Multi-Account Hierarchy | — | [BIP 44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) | Derivation path conventions |
| | 📜 Standard | BIP 84: Native SegWit Derivation | — | [BIP 84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki) | bc1q address derivation |
| | 📜 Standard | BIP 86: Taproot Derivation | — | [BIP 86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki) | bc1p address derivation |
| | 💡 Concept | Wallet types | — | — | Full node, SPV, hardware, multisig, watch-only |
| | 💡 Concept | Backup and recovery strategies | — | — | Seed storage, passphrase protection, inheritance planning |

## Suggested Order

1. **Mastering Bitcoin Ch. 5** — Start with Antonopoulos for the complete wallet architecture overview
2. **Learn Me A Bitcoin: HD Wallets** — Visualize how master keys derive child keys
3. **BIP 32** — Read the HD wallet standard that underpins everything
4. **BIP 39** — Understand how mnemonic seed phrases map to master keys
5. **BIP 44** — Learn the multi-account derivation path convention (m/44'/0'/0')
6. **BIP 84** — Native SegWit (bc1q) derivation paths
7. **BIP 86** — Taproot (bc1p) derivation paths
8. **Wallet types** — Compare full node, SPV, hardware, multisig, and watch-only wallets
9. **Backup and recovery** — Seed storage, passphrase protection, and inheritance planning
