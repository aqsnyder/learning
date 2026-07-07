# Network and P2P Layer

## Why This Section Matters

Bitcoin is a peer-to-peer network first. Understanding how nodes discover each other, propagate transactions, and synchronize the blockchain is key to understanding its resilience.

## Prerequisites

- [Section 02 — How Bitcoin Works](../02-how-bitcoin-works/README.md)

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | Satoshi / Cypherpunk essential canon |

## Resources

| Priority | Type | Resource | Author(s) | Link | Description |
|----------|------|----------|-----------|------|-------------|
| 🔑 | 📖 Book (Free) | Mastering Bitcoin, Chapter 10: The Network | Antonopoulos | [GitHub](https://github.com/bitcoinbook/bitcoinbook) | Comprehensive overview of Bitcoin's P2P network architecture |
| 🔑 | 📚 Curriculum | Chaincode Labs: P2P section | Chaincode Labs | [GitHub](https://github.com/chaincodelabs/bitcoin-curriculum) | Deep dive into P2P networking |
| | 📚 Documentation | Bitcoin Developer Guide: P2P Network | — | [Guide](https://developer.bitcoin.org/devguide/p2p_network.html) | Official P2P protocol documentation |
| | 🔧 Tool | Bitnodes | — | [Website](https://bitnodes.io/) | Live map of reachable Bitcoin nodes |
| | 🔧 Tool | Mempool.space | — | [Website](https://mempool.space/) | Real-time mempool visualization |
| | 💡 Concept | Node types | — | — | Full nodes, pruned nodes, SPV clients |
| | 💡 Concept | Transaction and block propagation | — | — | Compact blocks (BIP 152), Erlay |
| | 💡 Concept | Mempool policies and fee estimation | — | — | Policy rules, fee markets, RBF, CPFP |
| 🔑 | 🛠️ Practice | Run your own Bitcoin full node | — | — | The best way to learn the network |

## Suggested Order

1. **Mastering Bitcoin Ch. 10** — Start with Antonopoulos for the full network architecture picture
2. **Chaincode Labs P2P section** — Go deeper into P2P networking with curated study materials
3. **Node types** — Understand the differences between full nodes, pruned nodes, and SPV clients
4. **Transaction and block propagation** — Learn compact blocks (BIP 152) and Erlay
5. **Mempool policies and fee estimation** — Understand fee markets, RBF, and CPFP
6. **Bitnodes** — Explore the live network topology
7. **Mempool.space** — Watch real-time transaction flow and fee dynamics
8. **Bitcoin Developer Guide: P2P** — Use as ongoing reference for protocol details
9. **Run your own full node** — Nothing teaches the network like participating in it
