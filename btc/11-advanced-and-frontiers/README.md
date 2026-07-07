# Advanced Topics and Frontiers

> This section is a living document. Use the `.agents/skills/update-curriculum` skill to search for and add new important developments.

---

## Taproot and Schnorr (2021 Upgrade)

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| 🔑 | Standard | BIP 340: Schnorr Signatures | [BIP 340](https://github.com/bitcoin/bips/blob/master/bip-0340.mediawiki) | Schnorr signature scheme for Bitcoin |
| 🔑 | Standard | BIP 341: Taproot | [BIP 341](https://github.com/bitcoin/bips/blob/master/bip-0341.mediawiki) | SegWit v1 spending rules, Merkleized script trees |
| | Standard | BIP 342: Tapscript | [BIP 342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki) | Script validation rules for Taproot |
| | Website | Learn Me A Bitcoin: Taproot | [learnmeabitcoin.com](https://learnmeabitcoin.com/) | Visual explanations of Taproot concepts |

---

## Covenant Proposals

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | OP_CTV (BIP 119: CheckTemplateVerify) | | Transaction covenants — restricting how coins can be spent |
| | Concept | OP_CAT | | Re-enabling concatenation for advanced scripts |
| | Concept | Vaults | | Time-delayed spending for security |

---

## Scaling and Sidechains

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Fedimint | | Federated Chaumian e-cash on Bitcoin |
| | Concept | Liquid Network | | Blockstream's federated sidechain |
| | Concept | Ark | | Off-chain UTXO sharing protocol |

---

## Ordinals and Inscriptions

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Ordinal Theory | | Satoshi numbering and tracking |
| | Concept | Inscriptions | | Data embedded in Bitcoin transactions (BRC-20, etc.) |

---

## Privacy Advances

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Silent Payments (BIP 352) | | Reusable stealth addresses |
| | Concept | Payjoin improvements | | Enhanced collaborative transaction privacy |

---

## Mining

| Priority | Type | Resource | Link | Description |
|----------|------|----------|------|-------------|
| | Concept | Stratum V2 | | Next-gen mining pool protocol |

---

## Suggested Order

1. **BIP 340, 341, 342** — Start with Taproot since it's the most recent activated upgrade.
2. **Learn Me A Bitcoin: Taproot** — Reinforce with visual explanations.
3. **Covenant proposals** (OP_CTV, OP_CAT, Vaults) — Understand the most active protocol debate.
4. **Silent Payments and Payjoin** — Privacy-focused proposals building on existing work.
5. **Ordinals and Inscriptions** — Understand the cultural and technical controversy.
6. **Scaling** (Fedimint, Liquid, Ark) — Explore off-chain and sidechain approaches.
7. **Stratum V2** — Mining protocol evolution.
