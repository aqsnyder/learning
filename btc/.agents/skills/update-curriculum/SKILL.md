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
| Bitcoin Development Mailing List | https://groups.google.com/g/bitcoindev (archive: https://gnusha.org/pi/bitcoindev/) | Protocol proposals, technical discussions (moved off the old Linux Foundation list) |
| Delving Bitcoin | https://delvingbitcoin.org/ | Developer forum for protocol and Lightning design discussion (the BOLTs repo now points discussion there) |
| Bitcoin Optech Topics | https://bitcoinops.org/en/topics/ | Per-topic histories (covenants, cluster mempool, silent payments, …) — check status of proposals here |
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
| 04 | `04-transactions-and-scripting/` | Transaction structure, Script, SegWit, opcodes |
| 05 | `05-wallets-and-key-management/` | HD wallets, BIP 32/39/44, key derivation, descriptors, miniscript |
| 06 | `06-network-and-p2p/` | P2P protocol, node operation, mempool and relay policy |
| 07 | `07-lightning-network/` | Payment channels, routing, BOLT specs, LND/CLN |
| 08 | `08-security-and-privacy/` | Cold storage, multisig, CoinJoin, chain analysis |
| 09 | `09-economics-and-game-theory/` | Monetary theory, incentives, game theory, S2F |
| 10 | `10-development-and-programming/` | Bitcoin Core, dev tools, RPC, testing |
| 11 | `11-advanced-and-frontiers/` | Taproot, covenants, scaling, ordinals, new proposals |
| 12 | `12-hands-on-labs/` | Lab track run in parallel with 02–10: node bench (regtest/signet/mainnet), CLI fluency, Python harness, transaction building, descriptor/PSBT interop, Lightning bench, Taproot workbench, embedded signer HIL |
| 13 | `13-governance-and-protocol-change/` | BIP process, soft-fork activation, consensus vs. relay policy, contested changes, stakeholder analysis (read between 10 and 11) |

Cross-cutting resources that span multiple topics go in `books/`, `courses/`, or `blogs-and-references/`.

## Update Rules

> [!IMPORTANT]
> - **Append-only** — Never remove existing entries from section READMEs.
> - **Preserve formatting** — Match the format of the table you are adding to; column sets differ between sections (most use Priority | Type | Resource | Author(s) | [Year] | Link | Description; Section 11 has no Author/Year columns).
> - **State proposal status precisely** — For BIPs, quote the status from the BIPs repository (Draft / Complete / Deployed / Closed under BIP 3) and say whether a consensus change has actually activated.
> - **Use priority markers** — 🔑 for must-read/must-watch (sparingly). ⭐ only for the texts in the Bitcoin Canon table in `btc/README.md`; extending the canon is a deliberate README change, never a side effect of an update.
> - **Update PROGRESS.md** — After adding resources to a section README, update [PROGRESS.md](../../../PROGRESS.md) to reflect the new entries.
> - **Update suggested order** — If adding a resource that should be read in a specific sequence, update the Suggested Order section.

## Verification & Curation Rules (mandatory)

Earlier AI-generated updates to this repo introduced fabricated authors, resources that don't exist, and links to the wrong papers (all fixed in the October 2026 review — see `reviews/2026-10-deep-dive/`). Every update must follow these rules:

1. **Open every link before adding it.** Fetch the arXiv abs page, the DOI record (`https://api.crossref.org/works/<DOI>`), the official page, or the YouTube oEmbed record (`https://www.youtube.com/oembed?url=<url>&format=json`) and confirm the exact title, author order, year, and edition. Never write a URL or an author list from memory.
2. **Cite people, not organizations,** when a work lists authors ("Templeton et al.", not "Anthropic").
3. **When in doubt, leave it out.** List doubtful or unverifiable candidates in your summary instead of adding them.
4. **Correct, don't just append.** Fix wrong metadata in place. If a resource is superseded or dead, say so in its description and in your summary. (Append-only means don't silently delete — it does not mean leave errors.)
5. **Keep the learning layer whole.** A new resource goes into the section table, its Suggested Order, and `PROGRESS.md`. A new section must ship with the full anatomy — Why · Prerequisites · 🎯 Learning Objectives · Resources · Suggested Order · 🛠️ Practice (+ 🏗️ mini-project) · ✅ Check Yourself — plus a PROGRESS block (see the root `.agents/skills/audit-curriculum/SKILL.md`). Append new sections at the next number and state where to take them; don't renumber.
6. **Markers are closed lists.** ⭐ only for items on this curriculum's named list. Use 🔑 sparingly — at most 3 core items per section. Each section's Suggested Order opens with a "**Core path (🔑):**" line naming its 🔑 items; if you add or remove a 🔑, update that line too, then run `python tools/build_index.py` to refresh the learning-path table in the curriculum README.
7. **Label speculation and advocacy as such** (e.g. unconfirmed theories, price models, vendor claims), and prefer measured evidence.
8. **Run `python tools/check_repo.py`** from the repo root before finishing — it must report 0 problems.
9. **One home per topic.** Check the overlap table in `STUDY-GUIDE.md`. If a resource's topic lives in another curriculum, cross-link to it there instead of adding a duplicate row.

## Workflow

1. Search the sources listed above for new material.
2. Evaluate each candidate against the criteria.
3. Identify the correct section using the mapping table.
4. Append the new entry to the section's README.md resource table.
5. Update the Suggested Order if appropriate.
6. Update PROGRESS.md to reflect any new entries.
7. Summarize what was added and why.
