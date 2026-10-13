# Advanced Topics and Frontiers

> This section is a living document. Use the `.agents/skills/update-curriculum` skill to search for and add new important developments.
>
> **Status snapshot (October 2026):** no consensus change has activated since Taproot (November 2021). Everything under "Covenant Proposals" and "Other Open Soft-Fork Proposals" is a proposal, whatever its BIP status — under BIP 3, "Complete" means the authors consider the spec finished, not that it is deployed. Read [Section 13 — Governance and Protocol Change](../13-governance-and-protocol-change/README.md) first for how proposals become rules.

---

## 🎯 Learning Objectives

After this section you can:
- Construct and spend Taproot outputs by key path and script path (TapTweak, TapLeaf/TapBranch hashing, control block), validated against the BIP 341 test vectors.
- Express spending conditions as Miniscript inside `tr()` and compare their witness costs with P2WSH equivalents.
- Compare covenant proposals (CTV, OP_CAT, CSFS, CCV, TEMPLATEHASH, OP_VAULT) by capability, risk and status, and judge activation claims critically.
- Implement a privacy protocol from its specification (BIP 352 Silent Payments) and estimate its scanning cost for light clients.
- Map the off-chain and sidechain landscape (Lightning, Ark, Fedimint, Liquid) and the inscriptions/data-carrier debate by trust model and trade-offs, and commit to a dated, falsifiable prediction.

---

## Tracking the Frontier

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| 🔑 | Website | Bitcoin Optech Topics index | [bitcoinops.org/en/topics](https://bitcoinops.org/en/topics/) | ~160 topic pages, each with a summary, primary sources, and every newsletter mention in date order — the fastest way to check the current status of anything in this section |

---

## Taproot and Schnorr (2021 Upgrade)

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| 🔑 | Standard | BIP 340: Schnorr Signatures | [BIP 340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) | Schnorr signature scheme for Bitcoin |
| 🔑 | Standard | BIP 341: Taproot | [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) | SegWit v1 spending rules, Merkleized script trees |
| | Standard | BIP 342: Tapscript | [BIP 342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki) | Script validation rules for Taproot |
| | Website | Learn Me A Bitcoin: Taproot | [learnmeabitcoin.com](https://learnmeabitcoin.com/technical/upgrades/taproot/) | Visual explanations of Taproot concepts: tweaked keys, script trees, key-path and script-path spends, worked examples |
| | Practice | Optech Schnorr/Taproot workshop | [GitHub](https://github.com/bitcoinops/taproot-workshop) | Jupyter notebooks (runnable on Google Colab) built on Bitcoin Core's Python test framework: elliptic-curve math, tagged hashes, Schnorr, MuSig, taptweak, tapscript, taptrees, and a degrading-multisig case study |
| | Standard | BIP 327: MuSig2 | [BIP 327](https://github.com/bitcoin/bips/blob/master/bip-0327.mediawiki) | n-of-n Schnorr multisignatures that look like an ordinary single-key Taproot spend. Deployed: used in Lightning tooling (e.g. Loop, simple taproot channels), and Bitcoin Core parses `musig()` descriptors (BIP 390) |
| | Concept | FROST threshold signatures | [Optech topic](https://bitcoinops.org/en/topics/threshold-signature/) | k-of-n Schnorr signing that still produces one ordinary signature. A FROST signing BIP was proposed in 2024 and the ChillDKG key-generation protocol is in draft; neither is in the BIPs repository yet, though k-of-n signing devices (Frostsnap) shipped in 2025 |

---

## Covenant Proposals

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | OP_CTV (BIP 119: CheckTemplateVerify) | [BIP 119](https://github.com/bitcoin/bips/blob/master/bip-0119.mediawiki) | Transaction covenants — restricting how coins can be spent. BIP status Draft; not activated. Activation is still being debated (a December 2025 meeting discussed conservative BIP 9 parameters), often paired with CSFS (BIP 348) |
| | Concept | OP_CAT in Tapscript (BIP 347) | [BIP 347](https://github.com/bitcoin/bips/blob/master/bip-0347.mediawiki) | Re-enabling concatenation for advanced scripts. The spec is marked Complete in the BIPs repository, but it has not been activated |
| | Concept | Vaults | [Optech topic](https://bitcoinops.org/en/topics/vaults/) | Time-delayed spending for security. OP_VAULT (BIP 345) is Closed; OP_CHECKCONTRACTVERIFY (BIP 443) is its proposed replacement, and CTV-only vault designs are also being explored |
| | Website | Bitcoin Optech: Covenants topic | [Topic](https://bitcoinops.org/en/topics/covenants/) | The maintained overview of covenant proposals and their history — CTV, CSFS, APO (BIP 118), OP_CAT, OP_VAULT, TXHASH (BIP 346), OP_TEMPLATEHASH (BIP 446), BIP 448 — with links to each debate. Read this before any single proposal |

---

## Other Open Soft-Fork Proposals

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Standard | BIP 54: Consensus Cleanup | [BIP 54](https://github.com/bitcoin/bips/blob/master/bip-0054.md) | Bundles fixes for long-standing consensus bugs: the timewarp attack, worst-case slow-to-validate blocks, 64-byte-transaction Merkle weaknesses, and duplicate transactions. Spec Complete (2025); not activated |
| | Website | Bitcoin Optech: Quantum resistance | [Topic](https://bitcoinops.org/en/topics/quantum-resistance/) | Where post-quantum planning stands: BIP 360 (Pay-to-Merkle-Root, a Taproot-like output without the key-path spend; Draft) and BIP 361 (a phased sunset of legacy ECDSA/Schnorr signatures; Draft, 2026). Useful for separating the real long-term risk from the hype |

---

## Scaling and Sidechains

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Fedimint | [GitHub](https://github.com/fedimint/fedimint) | Federated Chaumian e-cash on Bitcoin |
| | Concept | Liquid Network | | Blockstream's federated sidechain |
| | Concept | Ark | [ark-protocol.org](https://ark-protocol.org/) | Off-chain UTXO sharing protocol: a server coordinates batches of shared "virtual UTXOs" that users can always exit on-chain without it. Implementations: Arkade (Ark Labs, launched late 2025) and Bark (Second, on mainnet since mid-2026) — see the [Optech topic](https://bitcoinops.org/en/topics/ark/) |
| | Standard | Cashu (NUTs specification) | [GitHub](https://github.com/cashubtc/nuts) | Chaumian ecash with a single custodial mint (vs. Fedimint's federation); tokens are minted and melted over Lightning. Strong payer privacy in exchange for trusting the mint |
| | Paper | BitVM (2023) and BitVM2 (2024) | [bitvm.org](https://bitvm.org/) | Robin Linus et al.: arbitrary computation verified on Bitcoin through fraud proofs, without a soft fork; BitVM2 applies it to bridges where safety needs only one honest signer from setup. Research-stage — read the papers, not the marketing |

---

## Ordinals and Inscriptions

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Ordinal Theory | [docs.ordinals.com](https://docs.ordinals.com/) | Satoshi numbering and tracking (Ordinal Theory Handbook, Casey Rodarmor et al.) |
| | Concept | Inscriptions | | Data embedded in Bitcoin transactions (BRC-20, etc.). The relay-policy fight this triggered is covered in Section 06 |
| | Standard | Runes | [Specification](https://docs.ordinals.com/runes/specification.html) | Fungible tokens carried in OP_RETURN "runestones"; the protocol activated at block 840,000, the 2024 halving block |

---

## Privacy Advances

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Silent Payments (BIP 352) | [BIP 352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki) | Reusable stealth addresses that need no notification transaction. BIP Complete; wallet support is growing (e.g. Sparrow 2.5 receiving, 2026), libsecp256k1 0.8 ships a silent-payments module, and Bitcoin Core support is being merged (2026) |
| | Concept | Payjoin improvements (BIP 77 Async Payjoin, "v2") | [BIP 77](https://github.com/bitcoin/bips/blob/master/bip-0077.md) | Enhanced collaborative transaction privacy: an untrusted "directory" server relays encrypted messages, so receivers no longer need to run a public endpoint. Draft; reference implementation in [rust-payjoin](https://github.com/payjoin/rust-payjoin) |

---

## Mining

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Stratum V2 | [Spec](https://github.com/stratum-mining/sv2-spec) | Next-gen mining pool protocol: encrypted (Noise) and binary, with a Job Declaration protocol that lets miners build their own block templates. Bitcoin Core 30 added an experimental IPC mining interface for Stratum v2 template providers |

---

## Suggested Order

1. **Optech Topics index** — Bookmark it; check each item below against its topic page for the latest status.
2. **BIP 340, 341, 342** — Start with Taproot since it's the most recent activated upgrade.
3. **Learn Me A Bitcoin: Taproot** — Reinforce with visual explanations.
4. **Optech Schnorr/Taproot workshop** — Build Schnorr signatures and Taproot spends yourself in Python.
5. **MuSig2 and FROST** — Multi-party Schnorr signing: deployed (MuSig2) vs. emerging (FROST).
6. **Covenant proposals** (Optech Covenants topic first, then OP_CTV, OP_CAT, Vaults) — Understand the most active protocol debate.
7. **Consensus Cleanup and quantum resistance** — The other soft-fork proposals in play.
8. **Silent Payments and Payjoin** — Privacy-focused proposals building on existing work.
9. **Ordinals, Inscriptions, and Runes** — Understand the cultural and technical controversy (then Section 06's relay-policy debate).
10. **Scaling** (Fedimint, Cashu, Liquid, Ark, BitVM) — Explore off-chain and sidechain approaches and their trust trade-offs.
11. **Stratum V2** — Mining protocol evolution.

---

## 🛠️ Practice

1. **Taproot key path by hand** — Add tagged hashes and the TapTweak to your BIP 340 code from section 01 and reproduce every `scriptPubKey` in BIP 341's `wallet-test-vectors.json`. Then create a P2TR output for your own key on regtest, spend it via the key path with a BIP 341 signature hash (SIGHASH_DEFAULT), and broadcast it. Done when all vectors pass and `testmempoolaccept` accepts your spend. *(~4 h · BIP 340; BIP 341; Learn Me A Bitcoin: Taproot)*
2. **Script path + Miniscript** — For internal key A, build a two-leaf tree: leaf 1 `and_v(v:pk(B),older(144))`, leaf 2 `multi_a(2,C,D,E)`. Compute the TapLeaf and TapBranch hashes, the output key and both control blocks, and spend leaf 1 on regtest after 144 blocks with your own code. Import the equivalent `tr(A,{…})` descriptor into Bitcoin Core and confirm the addresses match. Tabulate witness vbytes per path against the same policy written as `wsh(…)` Miniscript. *(~5 h · BIP 341; BIP 342: Tapscript; BIP 379: Miniscript (Section 05))*
3. **Inscriptions and the data-carrier debate** — Pull a mainnet inscription reveal transaction, decode its tapscript envelope (`OP_FALSE OP_IF "ord" … OP_ENDIF`) and extract the content; compute its weight and what the same bytes would cost as an OP_RETURN output. Sample 10 recent blocks and estimate the share of block weight that is inscription-style witness data. Then write 300 words steelmanning each side of Bitcoin Core 30's data-carrier change (default `-datacarriersize` raised to 100,000 bytes; multiple OP_RETURN outputs allowed). *(~3 h · Ordinal Theory; Inscriptions; Bitcoin Core relay-policy statement and Optech #352 (Section 06))*
4. **Covenant and L2 scorecard** — Build two tables. (a) Covenants: BIP 119 CTV, BIP 347 OP_CAT, BIP 348 CHECKSIGFROMSTACK, BIP 349 OP_INTERNALKEY, BIP 443 OP_CHECKCONTRACTVERIFY, BIP 446 OP_TEMPLATEHASH and BIP 345 OP_VAULT — what each enables (vaults, congestion control, non-interactive channel factories or Ark, recursive covenants), new risks, current BIP status, and whether you can try it on signet via Bitcoin Inquisition. (b) Off-chain and sidechain systems — Lightning, Ark, Fedimint, Liquid: who holds custody, the unilateral-exit path, liveness requirements, privacy. Finish with a 300-word steelman of the side you disagree with on covenant activation and one dated, falsifiable prediction. *(~5 h · Bitcoin Optech: Covenants topic; Covenant proposals (OP_CTV, OP_CAT, Vaults); Fedimint; Liquid Network; Ark)*
5. **Silent Payments from the spec** — Implement BIP 352 sending (sum the eligible input keys, input_hash over the smallest outpoint, ECDH with B_scan, t_k, P_k = B_spend + t_k·G) and receiving/scanning, and pass `bip-0352/send_and_receive_test_vectors.json`. Then estimate a light client's scanning cost: count eligible transactions in recent blocks on your node and convert to EC multiplications per day and to seconds on a phone-class CPU (benchmark your own implementation as a stand-in). *(~5 h · Silent Payments (BIP 352))*

**🏗️ Mini-project — Taproot Treasury Vault:** Design one Taproot output for a two-operator treasury. Key path: a MuSig2 aggregate of operators O1 and O2 (implement key aggregation and signing from BIP 327, or wrap libsecp256k1's musig module, and pass BIP 327's test vectors). Script leaves: `and_v(v:multi_a(2,B1,B2,B3),older(1008))` (backup keys after ~1 week) and `and_v(v:pk(R),older(26280))` (recovery key after ~6 months). Build the address and every spend with your own code, cross-check the address by importing `tr(<aggregate x-only key>,{…})` into Bitcoin Core as watch-only, and exercise all three paths on regtest with the timelocks scaled down. Then write a one-page design note: how would CTV or an OP_VAULT-style withdrawal delay change this design, and which risks (hot-key theft, periodic refreshes before timelocks mature) would go away? Deliverable: `projects/btc/11-taproot-treasury/`. Success: the MuSig2 vectors pass; Core derives the same address; all three paths confirm; early leaf spends fail with `non-BIP68-final`; a cost table shows the key-path spend is the cheapest and indistinguishable on-chain from a single-key P2TR spend. *(~14 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What does a Taproot output key commit to, and why does a key-path spend reveal nothing about the script tree?
2. Why are BIP 340 public keys x-only, and how is the missing y-coordinate resolved?
3. What is in a control block, and what does its length reveal to an observer?
4. What can OP_CTV do that pre-signed transactions can only achieve by trusting that a key was deleted?
5. Roughly how many EC multiplications per day must a Silent Payments light client perform to scan the chain? State your assumptions.
6. "Ordinals are part of Bitcoin's consensus rules" and "Taproot made every transaction private." Correct both.
7. In Stratum V2, who can choose a block's transactions, and why does that matter for mining decentralization?
8. Explain to a smart friend, in three sentences, what a covenant is and why proposals to enable them are contested.
