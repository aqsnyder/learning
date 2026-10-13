# Security and Privacy

> **Why this section matters:** Bitcoin's security model is unique. Understanding attack vectors, privacy techniques, and self-custody best practices is essential.

**Prerequisites:** Sections [04 — Transactions and Script](../04-transactions-and-scripting/), [05 — Wallets and Key Management](../05-wallets-and-key-management/).

---

## 🎯 Learning Objectives

After this section you can:
- Build a threat model for a custody setup and justify its choices (single-sig vs multisig, passphrase, geographic distribution) with the Lopp guide.
- Run a multi-device PSBT workflow (BIP 174) for a 2-of-3 multisig and explain what each role adds to the PSBT.
- Write Miniscript spending policies (e.g., a decaying multisig for inheritance) and reason about their witness costs and failure modes.
- Apply chain-analysis heuristics to a transaction graph and show exactly how CoinJoin and PayJoin break them.
- Explain hardware-signer attack classes — supply chain, fault injection, nonce exfiltration, address substitution — and the countermeasure for each.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Web Resource | Lopp.net Bitcoin Security Guide | Jameson Lopp | | [lopp.net](https://www.lopp.net/bitcoin-information/security.html) | Comprehensive security best practices |
| | Concept | Cold storage | | | | Air-gapped signing, hardware wallets (Coldcard, Trezor, Ledger) |
| | Concept | Multisig (multi-signature) | | | | 2-of-3, 3-of-5 setups for security |
| | Concept | Coin selection and UTXO management | | | | Privacy implications of consolidation |
| | Concept | CoinJoin and PayJoin | | | | Collaborative transactions for privacy. Note the legal context: in April 2024 two Samourai Wallet developers were arrested on U.S. charges related to their software, and two other companies then announced they would stop serving U.S. customers ([Optech #300](https://bitcoinops.org/en/newsletters/2024/05/01/)); newer designs (Payjoin v2, silent payments) are in Section 11 |
| | Concept | Chain analysis and privacy threats | | | | How surveillance works |
| | Web Resource | Bitcoin Privacy Guide | | | [bitcoiner.guide](https://bitcoiner.guide/privacy/) | Practical privacy techniques (an online guide, not a book) |
| | Video | Andreas Antonopoulos on Bitcoin privacy | Andreas Antonopoulos | | [YouTube](https://www.youtube.com/@aantonop) | Privacy-focused talks |
| 🔑 | Standard | BIP 174: PSBT (Partially Signed Bitcoin Transactions) | Ava Chow | | [BIP 174](https://github.com/bitcoin/bips/blob/master/bip-0174.mediawiki) | Multi-device signing workflow (PSBT v2 is BIP 370) |
| 🔑 | Book (Free) | Mastering Bitcoin, Chapter 13: Bitcoin Security | Andreas Antonopoulos and David Harding | 2023 | [GitHub](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch13_security.adoc) | Bitcoin's decentralized security model and root of trust, then user practice: physical storage, hardware signing devices, multisig and governance, survivability and inheritance |
| | Practice | Bitcoin Core multisig and offline-signing tutorials | Bitcoin Core contributors | | [Multisig](https://github.com/bitcoin/bitcoin/blob/master/doc/multisig-tutorial.md) · [Offline signing](https://github.com/bitcoin/bitcoin/blob/master/doc/offline-signing-tutorial.md) | Step-by-step on signet: build a descriptor-based multisig wallet, and pass PSBTs between an online watch-only wallet and an air-gapped signer — using only Bitcoin Core |
| | Web Resource | Bitcoin Wiki: Privacy | Bitcoin Wiki contributors | 2019 | [en.bitcoin.it](https://en.bitcoin.it/wiki/Privacy) | A long reference article on how Bitcoin privacy is attacked and defended. Blockchain attacks: the common-input-ownership heuristic, change-address detection, transaction-graph analysis, amount and timing correlation. Non-blockchain attacks: traffic analysis, custodial wallets, wallet-history lookups on third-party servers, eavesdropping. Defenses: avoiding address reuse, coin control, CoinJoin, PayJoin and Lightning, with case studies. Written in 2019 as a community wiki page, so check its tool and service recommendations against the 2024 CoinJoin changes noted in the CoinJoin and PayJoin row |

---

## Suggested Order

**Core path (🔑):** Lopp.net Bitcoin Security Guide → *Mastering Bitcoin* Ch. 13 → BIP 174 (PSBT)

1. **Lopp.net Security Guide** — Survey the threat landscape and best practices.
2. **Mastering Bitcoin Ch. 13** — The security model and user practices in one chapter.
3. **Cold storage** — Understand air-gapped signing and hardware wallet options.
4. **Multisig** — Learn multi-signature setups for stronger custody.
5. **BIP 174: PSBT** — Understand the signing workflow that makes multisig and cold storage practical.
6. **Bitcoin Core multisig and offline-signing tutorials** — Do it yourself on signet before trusting real funds to any setup.
7. **Coin selection and UTXO management** — Learn how UTXO handling impacts privacy.
8. **CoinJoin and PayJoin** — Explore collaborative transaction techniques.
9. **Chain analysis and privacy threats** — Understand how surveillance works to know what you're defending against.
10. **Bitcoin Wiki: Privacy** — Each chain-analysis heuristic and network-level attack in detail, with the countermeasure for each.
11. **Bitcoin Privacy Guide** — Practical techniques to apply what you've learned.
12. **Antonopoulos on privacy** — Fill in gaps with accessible video content.

---

## 🛠️ Practice

1. **Custody threat model** — Using the Lopp guide, score three setups — phone single-sig; hardware single-sig + passphrase; 2-of-3 multisig across two hardware vendors and two locations — against malware and address substitution, supply-chain tampering, physical coercion, loss or fire, inheritance, and insider risk (likelihood × impact). Deliverable: a one-page matrix and a recommendation for one concrete scenario (e.g., a small company's treasury) that names the failure mode you are choosing to accept. *(~2 h · Lopp.net Bitcoin Security Guide; Mastering Bitcoin ch. 13)*
2. **Hardware-signer attack autopsy** — Pick two public attacks of different classes — e.g., fault-injection seed extraction from a general-purpose MCU, and malicious-firmware seed exfiltration through chosen signature nonces (the 2024 "Dark Skippy" disclosure) — and record for each: attacker access required, what leaked, root cause, and the countermeasure (secure element, anti-exfil signing, reproducible builds, on-device address verification). End with the list of countermeasures your section-01 and section-05 devices lack. *(~2 h · Lopp.net Bitcoin Security Guide; Cold storage concept)*
3. **2-of-3 PSBT round trip** — Follow Bitcoin Core's `doc/multisig-tutorial.md` on signet (or adapt it to regtest): three signer wallets plus a watch-only coordinator holding a `wsh(sortedmulti(2,…))` descriptor. Walk creator → updater → signer → signer → combiner → finalizer → extractor (`walletcreatefundedpsbt`, `walletprocesspsbt`, `combinepsbt`, `finalizepsbt`, `sendrawtransaction`), saving the PSBT after each step. `decodepsbt` each one and list which BIP 174 fields appear at which role; hand-parse the magic bytes and first input map of one. Make one signer an embit script to prove interoperability. *(~3 h · BIP 174: PSBT; Bitcoin Core multisig and offline-signing tutorials; Multisig concept; embit (Section 10))*
4. **Miniscript inheritance policy** — Write a policy such as `or(99@pk(Owner),and(thresh(2,pk(H1),pk(H2),pk(H3)),older(52560)))`, compile it with a Miniscript compiler (bitcoin.sipa.be/miniscript, rust-miniscript or BDK), and import the resulting `wsh(…)` descriptor into a Bitcoin Core regtest wallet — swap `older(52560)` for `older(20)` to test quickly. Spend via both branches, record each branch's witness size, and document what goes wrong if the owner forgets to move the coins before the heirs' timelock matures. *(~3 h · Multisig concept; Lopp.net Bitcoin Security Guide (backup and inheritance); BIP 379: Miniscript (Section 05); Bitcoin Dev Kit (Section 10))*
5. **Chain-analysis lab** — Script three regtest "users" making ~50 transactions with realistic habits (address reuse, round payment amounts, change of a different script type, consolidations). Write an analyzer that applies common-input ownership plus two change-detection heuristics (pick them from the Bitcoin Wiki's Privacy article), and score its clustering against your ground truth. Then add one equal-output CoinJoin and one PayJoin-style transaction (the receiver contributes an input, as in BIP 78) and show exactly which heuristics each defeats. *(~4 h · Bitcoin Wiki: Privacy; Bitcoin Privacy Guide; Chain analysis concept; CoinJoin and PayJoin concept)*

**🏗️ Mini-project — Air-Gapped 2-of-3 on Signet:** Cosigners: a Bitcoin Core wallet, an offline embit script (a laptop or Raspberry Pi with networking disabled), and your section-05 microcontroller extended to sign PSBTs — or Specter-DIY on an STM32F469I-DISCO as a reference design. PSBTs move only by SD card, QR code or serial. The device must (1) recognise change outputs as belonging to the same 2-of-3 descriptor and refuse a PSBT whose "change" doesn't, (2) display destination, amount and fee before signing, and (3) sign with its BIP 32-derived key. Section 12's Lab 7 provides the hardware-in-the-loop test rig. Deliverable: `projects/btc/08-airgap-multisig/` with a runbook. Success: signet spends confirmed with every signer pair; a tampered-change PSBT from the coordinator is rejected on the device; a recovery drill rebuilds the wallet on a fresh machine from two seeds plus the descriptor backup. *(~14 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Besides two of the three seeds, what must you have to recover a 2-of-3 multisig wallet?
2. Name the PSBT roles and what each one adds.
3. Why does a hardware signer need the full multisig descriptor to verify a change output?
4. Estimate the fee to consolidate 50 P2WPKH UTXOs into a single output at 10 sat/vB.
5. What is the common-input-ownership heuristic, and how does PayJoin poison it?
6. "A hardware wallet protects me from malware on my computer." When is that false?
7. Why do equal-output CoinJoins work, and what can still link coins afterwards?
8. Explain to a smart friend, in three sentences, why a 2-of-3 multisig spread across locations beats a single seed in a single safe.
