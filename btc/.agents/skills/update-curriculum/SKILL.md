---
name: update-curriculum
description: Search for and add new important Bitcoin resources, BIPs, protocol upgrades, and educational materials to the learning curriculum.
---

# Update Bitcoin Curriculum

## When to Use

Use this skill when you want to update the Bitcoin learning curriculum with:

- **New BIPs** — Newly proposed or activated Bitcoin Improvement Proposals
- **Protocol upgrades** — Soft forks, consensus changes, or major implementation updates
- **Major educational content** — New books, courses, video series, or developer programs
- **Tool and software updates** — New wallet software, node implementations, or developer tools
- **Conference talks** — Important presentations from Bitcoin conferences

## Where to Search

Check the following sources for new material:

| Source | URL | What to Look For |
|--------|-----|------------------|
| Bitcoin Core Releases | https://github.com/bitcoin/bitcoin/releases | New versions, release notes, feature changes |
| BIP Repository | https://github.com/bitcoin/bips | New and updated BIPs |
| bitcoin-dev mailing list | https://lists.linuxfoundation.org/pipermail/bitcoin-dev/ | Protocol proposals, technical discussions |
| Lopp.net | https://www.lopp.net/bitcoin-information.html | Curated resource updates |
| Chaincode Labs Curriculum | https://github.com/chaincodelabs/bitcoin-curriculum | Curriculum updates and new modules |
| Andreas Antonopoulos | https://www.youtube.com/@aantonop | New talks and educational content |
| Learn Me A Bitcoin | https://learnmeabitcoin.com/ | New visual explainers |
| Bitcoin Optech | https://bitcoinops.org/ | Weekly technical newsletter |
| Bitcoin++ Conference | https://btcplusplus.dev/ | Developer-focused conference talks |
| TABConf | https://tabconf.com/ | Technical conference presentations |
| Advancing Bitcoin | https://www.advancingbitcoin.com/ | Research and development talks |

## Evaluation Criteria

Before adding a resource, evaluate it against these criteria:

1. **Technical depth** — Does it add meaningful understanding beyond existing resources?
2. **Community consensus** — Is it widely recognized or recommended by respected Bitcoiners?
3. **Educational value** — Is it well-structured, clearly explained, and accessible?
4. **Relevance** — Does it fit the curriculum's scope (Bitcoin-specific, not altcoin content)?
5. **Longevity** — Is it likely to remain relevant, or is it ephemeral news?

## Section Mapping

Map new resources to the appropriate section:

| Section | Directory | Topics |
|---------|-----------|--------|
| 00 | `00-history-and-philosophy/` | History, cypherpunk philosophy, Bitcoin origins |
| 01 | `01-cryptography-foundations/` | Hash functions, ECDSA, Merkle trees, Schnorr |
| 02 | `02-protocol-fundamentals/` | Blocks, headers, chain structure, consensus rules |
| 03 | `03-mining-and-consensus/` | PoW, difficulty, mining hardware, pools |
| 04 | `04-transactions-and-script/` | Transaction structure, Script, SegWit, opcodes |
| 05 | `05-wallets-and-key-management/` | HD wallets, BIP 32/39/44, key derivation |
| 06 | `06-network-and-p2p-layer/` | P2P protocol, node operation, mempool |
| 07 | `07-lightning-network/` | Payment channels, routing, BOLT specs, LND/CLN |
| 08 | `08-security-and-privacy/` | Cold storage, multisig, CoinJoin, chain analysis |
| 09 | `09-economics-and-game-theory/` | Monetary theory, incentives, game theory, S2F |
| 10 | `10-development-and-programming/` | Bitcoin Core, dev tools, RPC, testing |
| 11 | `11-advanced-and-frontiers/` | Taproot, covenants, scaling, ordinals, new proposals |

Cross-cutting resources that span multiple topics go in `books/`, `courses/`, or `blogs-and-references/`.

## Update Rules

> [!IMPORTANT]
> - **Append-only** — Never remove existing entries from section READMEs.
> - **Preserve formatting** — Match the existing table format (Priority | Type | Resource | Author(s) | Year | Link | Description).
> - **Use priority markers** — 🔑 for must-read/must-watch, ⭐ for Satoshi/Cypherpunk canon.
> - **Update PROGRESS.md** — After adding resources to a section README, update [PROGRESS.md](../../PROGRESS.md) to reflect the new entries.
> - **Update suggested order** — If adding a resource that should be read in a specific sequence, update the Suggested Order section.

## Workflow

1. Search the sources listed above for new material.
2. Evaluate each candidate against the criteria.
3. Identify the correct section using the mapping table.
4. Append the new entry to the section's README.md resource table.
5. Update the Suggested Order if appropriate.
6. Update PROGRESS.md to reflect any new entries.
7. Summarize what was added and why.
