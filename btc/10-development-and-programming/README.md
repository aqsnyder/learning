# Development and Programming

> **Why this section matters:** To truly master Bitcoin, write code that interacts with it. From running a node to contributing to Bitcoin Core.

**Prerequisites:** Sections [02](../02-protocol-fundamentals/)–[07](../07-lightning-network/), programming experience.

---

## 🎯 Learning Objectives

After this section you can:
- Build Bitcoin Core from source with CMake, run its unit and functional test suites, and write a new functional test.
- Automate regtest and signet scenarios from Python through JSON-RPC and ZMQ, including a custom signet you control.
- Trace a transaction through Bitcoin Core's code from RPC submission to mempool acceptance and relay, labelling each check as policy or consensus.
- Review a real pull request the way PR Review Club does: build it, test it, and ask substantive questions.
- Validate your own Bitcoin implementation against Bitcoin Core's consensus test vectors (differential testing).

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book (Free) | Programming Bitcoin | Jimmy Song | 2019 | [GitHub](https://github.com/jimmysong/programmingbitcoin) | Build a Bitcoin library from scratch in Python (full text and exercises free on GitHub; pre-Taproot) |
| 🔑 | Curriculum | Chaincode Labs Bitcoin Curriculum | Chaincode Labs | | [GitHub](https://github.com/chaincodelabs/bitcoin-curriculum) | Syllabus of curated readings by subject, from Chaincode's developer residency; many links date from 2016–2019, so pair with Optech for anything recent |
| 🔑 | Curriculum | Btrust Builders: Mastering Bitcoin Pathway | Btrust | | [pathways.btrust.tech](https://pathways.btrust.tech/) | 8-week study pathway built on Mastering Bitcoin; live cohorts are application-based (aimed at developers in Africa) but the self-paced track is open to anyone. Sibling pathways: Learn Bitcoin from the Command Line (7 weeks), Rust for Bitcoiners (6 weeks) |
| 🔑 | Source Code | Bitcoin Core | | | [GitHub](https://github.com/bitcoin/bitcoin) | The reference implementation |
| | Course | Saylor University CS120: Bitcoin for Developers I | Saylor University | | [learn.saylor.org](https://learn.saylor.org/) | Self-paced developer course (~18 hours, free certificate): cryptography, keys, hashing and proof-of-work, wallets, nodes |
| | Documentation | Bitcoin Developer Documentation | | | [developer.bitcoin.org](https://developer.bitcoin.org/) | bitcoin.org's community docs — not official Bitcoin Core documentation, and unmaintained since about 2021 (its RPC reference stops at Bitcoin Core 0.21) |
| 🔑 | Practice | Bitcoin Core PR Review Club | | | [bitcoincore.reviews](https://bitcoincore.reviews/) | Learn by reviewing real code changes |
| | Tool | Bitcoin Core RPC API | Bitcoin Core | | [RPC reference](https://bitcoincore.org/en/doc/) | Programmatic interaction with a node. Use the versioned official reference (latest: 31.x) or `bitcoin-cli help` — the developer.bitcoin.org copy is frozen at 0.21 and lacks years of RPC changes |
| | Community | Bitcoin Development Mailing List | | | [Google Groups](https://groups.google.com/g/bitcoindev) | Protocol discussion and BIP proposals (moved off the Linux Foundation list; archive at [gnusha.org](https://gnusha.org/pi/bitcoindev/)) |
| | Practice | Set up Bitcoin Core on regtest, signet, and testnet4 | | | | Hands-on experimentation: regtest for instant local blocks, then signet (BIP 325) or testnet4 (BIP 94, Bitcoin Core 28+); testnet3 is being phased out |
| 🔑 | Book (Free) | Mastering Bitcoin, Chapter 3: Bitcoin Core: The Reference Implementation | Andreas Antonopoulos and David Harding | 2023 | [GitHub](https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch03_bitcoin-core.adoc) | Compile, configure, and run a node; explore transactions and blocks with `bitcoin-cli`; call the JSON-RPC API from Python; survey of alternative clients and libraries — the on-ramp to everything else here |
| | Curriculum | Chaincode Labs: Bitcoin Protocol Development seminar | Chaincode Labs | | [Seminar](https://chaincode.gitbook.io/seminars/bitcoin-protocol-development) | Five-session reading list with discussion questions (SegWit, mining and propagation, P2P, Script and wallets) — the bridge from Mastering Bitcoin to Bitcoin Core development |
| | Tool | embit | Stepan Snigirev | 2020– | [GitHub](https://github.com/diybitcoinhardware/embit) | Minimal Bitcoin library for Python 3 and MicroPython, built for embedded signers (used by SeedSigner): keys, BIP 32/39, scripts, PSBTs, descriptors. A natural fit for firmware/hardware-wallet experiments |
| | Tool | Bitcoin Dev Kit (Book of BDK) | Bitcoin Dev Kit Foundation | 2026 | [bookofbdk.com](https://bookofbdk.com/) | Rust libraries for descriptor-based wallets (built on rust-bitcoin and rust-miniscript), with Kotlin/Swift bindings and a separately maintained Python package. For lower-level transaction building in Rust see the [Rust Bitcoin Cookbook](https://rust-bitcoin.org/book/) |

---

## Suggested Order

> 🛠️ **The hands-on lab track now lives in [Section 12 — Hands-on Labs](../12-hands-on-labs/README.md)** — run it in parallel with Sections 02–10 (Lab 0 alongside Section 02). Items 1–4 below overlap with Labs 0–2; if you've done those, start at item 5.

1. **Mastering Bitcoin Ch. 3** — Build/install Bitcoin Core and learn `bitcoin-cli` and the RPC interface.
2. **Set up Bitcoin Core on regtest, signet, and testnet4** — Get hands-on with a running node; never practise on mainnet.
3. **Learning Bitcoin from the Command Line** — Now the manual for Section 12's Labs 0, 1 and 5; work through it there.
4. **Bitcoin Core RPC API** — Script against your node from Python using the current RPC reference.
5. **Programming Bitcoin** — Build a Bitcoin library from scratch to internalize the protocol.
6. **embit or Bitcoin Dev Kit** — Build and sign real transactions with a maintained library (Python/MicroPython or Rust).
7. **Bitcoin Core source code** — Clone the repo and explore the codebase structure.
8. **Chaincode Labs: Bitcoin Protocol Development seminar** — Structured readings and discussion questions.
9. **Chaincode Labs Bitcoin Curriculum** — Dip into subject-by-subject readings as needed.
10. **Btrust Builders pathway** — Follow the structured 8-week program (self-paced or cohort).
11. **Saylor University CS120** — Supplement with a formal developer course.
12. **Bitcoin Developer Documentation** — Background reference only (unmaintained).
13. **Bitcoin Core PR Review Club** — Learn by reviewing real pull requests.
14. **Bitcoin Development Mailing List** — Follow protocol discussions and engage with the community.

---

## 🛠️ Practice

1. **Build and test Bitcoin Core** — Clone `bitcoin/bitcoin`, check out the latest release tag, then `cmake -B build`, `cmake --build build -j$(nproc)`, `ctest --test-dir build`, and `build/test/functional/test_runner.py` on a subset (e.g., `wallet_basic.py feature_rbf.py`). Record build time, binary sizes and any failing tests with their cause. Note where *Mastering Bitcoin* ch. 3 differs — it still describes the pre-CMake autotools build. *(~3 h · Bitcoin Core source; Mastering Bitcoin ch. 3)*
2. **RPC + ZMQ automation** — Write a Python tool that speaks JSON-RPC (plain `requests` or python-bitcoinlib) and subscribes to `-zmqpubrawtx` / `-zmqpubhashblock` (see `doc/zmq.md` and `contrib/zmq/zmq_sub.py`). Use it to measure latency from `sendrawtransaction` to the ZMQ notification and to run a small regtest faucet endpoint. Then repeat on the public signet with faucet coins, and stand up your own custom signet with `contrib/signet/miner` (see `contrib/signet/README.md`). *(~4 h · Bitcoin Core RPC API; Set up Bitcoin Core on regtest, signet, and testnet4; Bitcoin Developer Documentation)*
3. **Follow a transaction through the code** — At a tagged release, trace `sendrawtransaction` (`src/rpc/mempool.cpp`) → `BroadcastTransaction` (`src/node/transaction.cpp`) → `ProcessTransaction` and the `MemPoolAccept` checks in `src/validation.cpp` → relay in `src/net_processing.cpp`. Deliverable: a call graph with file:function labels and one paragraph per stage stating which checks are policy and which are consensus. Done when you can set a debugger breakpoint at each stage and hit it with a regtest transaction. *(~3 h · Bitcoin Core source; Bitcoin Developer Documentation)*
4. **Write a functional test** — Starting from `test/functional/example_test.py`, write a test that starts two nodes, mines, sends a transaction, asserts mempool sync, forces a reorg with `invalidateblock`, and asserts the transaction is back in the mempool. Done when it passes under `test_runner.py` and fails when you deliberately break an assertion. *(~4 h · Bitcoin Core source; Chaincode Labs curriculum: Bitcoin Core Contribution)*
5. **PR Review Club, solo** — Pick a recent session on bitcoincore.reviews, check out the PR at the reviewed commit, build it, run its tests, and answer the session's questions in writing before reading the meeting log; then compare with the log and note what you missed. Draft one review comment you would be willing to post. *(~4 h · Bitcoin Core PR Review Club; Bitcoin Development Mailing List for context)*

**🏗️ Mini-project — Differential Test Harness:** Run your *Programming Bitcoin*-derived transaction parser, sighash code and Script interpreter against Bitcoin Core's own test data — `src/test/data/script_tests.json`, `tx_valid.json`, `tx_invalid.json` and `sighash.json` — honouring each case's verification flags (skip, and report, flags you don't implement). Add property-based round-trip tests (Hypothesis) that compare your serializer with `decoderawtransaction` on a regtest node, and wire everything into CI (GitHub Actions starting `bitcoind -regtest`). Rust alternative: do the same with rust-bitcoin. Deliverable: `projects/btc/10-difftest/` with a pass-rate table per flag set. Success: CI is green; every remaining failure is categorised and explained; at least one bug in your own code was found and fixed thanks to the harness. *(~14 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Where does a transaction submitted with `sendrawtransaction` get checked against policy, and where against consensus script rules?
2. When would you write a unit test rather than a functional test in Bitcoin Core?
3. Name three regtest tools that make tests deterministic (e.g., `generatetoaddress`, `setmocktime`, `invalidateblock`) and what each one controls.
4. Why is a consensus bug far more dangerous than an ordinary bug, and how does that shape how consensus code is reviewed?
5. "Bitcoin Core developers decide Bitcoin's rules." Who actually enforces them?
6. What does ZMQ give you that polling RPC doesn't, and why must a ZMQ consumer still reconcile with RPC?
7. Estimate how long initial block download would take on your machine. Which resource is the bottleneck, and how does `assumevalid` change the answer?
8. Explain to a smart friend, in three sentences, how a change gets from an idea into the Bitcoin Core release people run.
