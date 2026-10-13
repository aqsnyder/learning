# Wallets and Key Management

## Why This Section Matters

"Not your keys, not your coins." Understanding how wallets work, from seed phrases to HD derivation paths, is critical for both users and developers.

## Prerequisites

- [Section 01 — Cryptography Foundations](../01-cryptography-foundations/README.md)
- [Section 04 — Transactions and Script](../04-transactions-and-scripting/README.md) (output types and Script, which derivation paths and descriptors refer to)

## 🎯 Learning Objectives

After this section you can:
- Implement BIP 39 (entropy → mnemonic → seed) and BIP 32 (CKDpriv, CKDpub, xprv/xpub serialization), passing the official test vectors.
- Explain hardened vs normal derivation and demonstrate how an xpub plus one non-hardened child private key compromises a whole account.
- Derive BIP 44/84/86 paths and addresses — including BIP 86's Taproot tweak — and reconcile them with output descriptors in Bitcoin Core.
- Compare wallet architectures (full node, light client, hardware, multisig, watch-only) on trust, privacy and attack surface.
- Design a backup and recovery scheme and estimate brute-force costs for partial seed loss and forgotten passphrases.

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | Satoshi / Cypherpunk essential canon |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑 | 📖 Book (Free) | Mastering Bitcoin, Chapter 5: Wallet Recovery | Antonopoulos & Harding | [GitHub](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch05_wallets.adoc) | HD key derivation (BIP 32), BIP 39 recovery codes and passphrases, and what else a backup must capture (derivation paths, output script descriptors) |
| | 🌐 Website | Learn Me A Bitcoin: HD Wallets | Greg Walker | [Website](https://learnmeabitcoin.com/technical/keys/hd-wallets/) | Visual HD wallet derivation |
| 🔑 | 📜 Standard | BIP 32: Hierarchical Deterministic Wallets | — | [BIP 32](https://github.com/bitcoin/bips/blob/master/bip-0032.mediawiki) | The HD wallet standard |
| | 📜 Standard | BIP 39: Mnemonic Seed Phrases | — | [BIP 39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki) | How 12/24 word seeds work |
| | 📜 Standard | BIP 44: Multi-Account Hierarchy | — | [BIP 44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki) | Derivation path conventions |
| | 📜 Standard | BIP 84: Native SegWit Derivation | — | [BIP 84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki) | bc1q address derivation |
| | 📜 Standard | BIP 86: Taproot Derivation | — | [BIP 86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki) | bc1p address derivation |
| | 💡 Concept | Wallet types | — | — | Full node, SPV, hardware, multisig, watch-only |
| | 💡 Concept | Backup and recovery strategies | — | — | Seed storage, passphrase protection, inheritance planning |
| 🔑 | 📜 Standard | Output Script Descriptors (BIPs 380–387) | Pieter Wuille, Ava Chow | [BIP 380](https://github.com/bitcoin/bips/blob/master/bip-0380.mediawiki) | The language modern wallets use to state exactly which scripts they own, e.g. `wpkh([fingerprint/84h/0h/0h]xpub…/0/*)`. Bitcoin Core wallets are descriptor-only since v30 removed legacy wallets; practical guide: [Bitcoin Core descriptors doc](https://github.com/bitcoin/bitcoin/blob/master/doc/descriptors.md) |
| | 📜 Standard | BIP 379: Miniscript (with BIP 388 Wallet Policies) | Pieter Wuille, Andrew Poelstra, Sanket Kanjalkar, Antoine Poinsot, Ava Chow; Salvatore Ingala | [BIP 379](https://github.com/bitcoin/bips/blob/master/bip-0379.md) | A composable, analyzable subset of Script for spending policies (multisig, timelocked recovery, inheritance); BIP 388 adapts descriptors and miniscript for hardware signers. Specs are Draft (379) and Complete (388) — check wallet support before relying on them |

## Suggested Order

**Core path (🔑):** *Mastering Bitcoin* Ch. 5 → BIP 32 → Output descriptors (BIPs 380–387)

1. **Mastering Bitcoin Ch. 5** — Start with Antonopoulos for the complete wallet architecture overview
2. **Learn Me A Bitcoin: HD Wallets** — Visualize how master keys derive child keys
3. **BIP 32** — Read the HD wallet standard that underpins everything
4. **BIP 39** — Understand how mnemonic seed phrases map to master keys
5. **BIP 44** — Learn the multi-account derivation path convention (m/44'/0'/0')
6. **BIP 84** — Native SegWit (bc1q) derivation paths
7. **BIP 86** — Taproot (bc1p) derivation paths
8. **Output script descriptors (BIPs 380–387)** — How a wallet records what it owns; read the Bitcoin Core descriptors doc alongside
9. **Miniscript and wallet policies (BIPs 379, 388)** — Composable spending policies beyond simple single-sig and multisig
10. **Wallet types** — Compare full node, SPV, hardware, multisig, and watch-only wallets
11. **Backup and recovery** — Seed storage, passphrase protection, and inheritance planning (back up descriptors, not just seeds)

---

## 🛠️ Practice

1. **BIP 39 by hand** — Implement entropy → SHA-256 checksum → 11-bit indices → words, and mnemonic → seed (PBKDF2-HMAC-SHA512, 2,048 iterations, salt "mnemonic" + passphrase). Pass every vector in trezor/python-mnemonic's `vectors.json` (passphrase "TREZOR"). Then show with arithmetic why only 128 of the 2,048 words can end a valid 12-word phrase, and how many can end a 24-word one. *(~2 h · Mastering Bitcoin ch. 5; BIP 39)*
2. **Seed-loss Fermi** — Benchmark your mnemonic-to-seed derivations per second. Estimate worst-case recovery time for a 12-word phrase with 1, 2 or 3 unknown words (known vs unknown positions, counting the checksum filter), and for a forgotten 4-word Diceware passphrase, on your laptop and on hardware 1,000× faster. Deliverable: a table plus a 200-word backup recommendation (metal plate, passphrase, multisig, geographic split) that cites your numbers. *(~1.5 h · BIP 39; Backup and recovery strategies concept)*
3. **BIP 32 from scratch** — On your section-01 curve code, implement master-key generation (HMAC-SHA512 keyed with "Bitcoin seed"), CKDpriv, CKDpub, key fingerprints and Base58Check xprv/xpub serialization. Done when you pass BIP 32 test vectors 1–5; vectors 4 and 5 cover leading-zero and invalid-key edge cases. *(~4 h · BIP 32; Learn Me A Bitcoin: HD Wallets)*
4. **The leaky-xpub attack** — Given an account xpub and one non-hardened child private key, recover the account xprv: write the three-line algebra, implement it, and test it on keys you derived. Then explain why BIP 44 hardens the purpose, coin-type and account levels, and what that implies for handing xpubs to watch-only software. *(~1.5 h · BIP 32 (security section); BIP 44; Mastering Bitcoin ch. 5)*
5. **Paths, descriptors and test vectors** — From the mnemonic "abandon" × 11 + "about", derive m/84'/0'/0'/0/0 and m/86'/0'/0'/0/0 and match BIP 84's `bc1qcr8te4kr609gcawutmrza0j4xv80jy8z306fyu` and BIP 86's `bc1p5cyxnuxmeuwuvkwfem96lqzszd02n6xdcjrs20cac6yqjjwudpxqkedrcr` (BIP 86 needs one formula from BIP 341, listed in Section 11: Q = P + int(hash_TapTweak(P))·G). Then on regtest create a blank descriptor wallet, `importdescriptors` your `wpkh(tprv…/84h/1h/0h/0/*)` as active with a range (checksum from `getdescriptorinfo`), and confirm `getnewaddress` returns the addresses your code predicts — the first should be `bcrt1q6rz28mcfaxtmd6v789l9rrlrusdprr9pz3cppk`. *(~3 h · BIP 84; BIP 86; Mastering Bitcoin ch. 5)*

**🏗️ Mini-project — Hardware Seed Generator:** On an STM32 (C with libwally-core or trezor-firmware's `crypto/` library, or MicroPython with embit — Section 10), build a device that gathers entropy from the TRNG — with repetition-count and adaptive-proportion health tests in the spirit of NIST SP 800-90B, optionally mixing in dice rolls via SHA-256 — shows a 24-word mnemonic, derives m/84'/1'/0', and exports only the account descriptor (`wpkh([fingerprint/84h/1h/0h]tpub…/0/*)`) over USB-serial; on request it displays receive address #n. Import the descriptor into a Bitcoin Core regtest or signet watch-only wallet and receive funds to it. Section 12's Lab 7 is the matching hardware-in-the-loop test rig. Deliverable: `projects/btc/05-seed-device/` (firmware, host script, entropy test log). Success: fed fixed test entropy, the device reproduces BIP 39/32/84 test-vector outputs; its first 20 receive addresses match Core's exactly; a half-page note states what an attacker holding the xpub, USB access, or SWD access could learn. *(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What does BIP 32's chain code add beyond the key itself, and why can't an xpub derive hardened children?
2. Decode m/84'/0'/0'/1/5 level by level.
3. How many valid final words does a 24-word mnemonic have, and why?
4. What does a BIP 39 passphrase protect against, and what is its biggest operational risk?
5. What can someone holding your account xpub learn, and what can't they do with it?
6. "My bitcoin is stored on my hardware wallet." Where is it really, and what does the device actually hold?
7. Why did wallets move to output descriptors when BIP 44/84/86 already standardise derivation paths?
8. Explain to a smart friend, in three sentences, how 12 or 24 words can back up every address a wallet will ever generate.
