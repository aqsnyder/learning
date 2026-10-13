# Hands-on Labs

## Why This Section Matters

Every section from 00 to 11 ends with exercises scoped to its own topic. This section supplies three things those exercises lack:

- **The bench** the exercises run on.
- **The order** to run them in.
- **Integration checkpoints**, where code from different sections has to work together against a real Bitcoin Core node.

It is numbered 12 only so that nothing else had to be renumbered. **Run it in parallel with Sections 02–10, not after them.** Lab 0 starts alongside Section 02, and each later lab names the section it accompanies.

Keep everything in one repository (e.g. `projects/btc/lab/`) so the bench, your Python library and your tests grow together, and the per-section mini-projects can reuse them.

| Lab | Run alongside | You end up with |
|-----|---------------|-----------------|
| 0 — The bench | Section 02 | Scripted regtest, signet and pruned-mainnet nodes |
| 1 — CLI fluency | Sections 02–04 | `bitcoin-cli`, raw transactions and fee bumping without looking anything up |
| 2 — Python harness | Sections 03–04 | A tested RPC/ZMQ package that every later lab imports |
| 3 — Transactions in code | Section 04 (P2TR after 11) | One signer for every standard output type, differentially tested against Core |
| 4 — Wallet stack | Sections 05 and 08 | Descriptor multisig with PSBTs passing between your code, Core and embit |
| 5 — Lightning bench | Section 07 | A multi-node regtest Lightning network you can rebuild in minutes |
| 6 — Taproot workbench | Section 11 (or straight after 04) | Guided Schnorr/MuSig/Taptree notebooks, then the same pieces in your own library |
| 7 — Embedded signer HIL (optional) | Sections 05 and 08 | A hardware-in-the-loop test rig for a MicroPython/embit signer |

## Prerequisites

- [Section 01 — Cryptography Foundations](../01-cryptography-foundations/README.md) under way. Labs 3–4 build on the curve and signature code from its exercises.
- A Unix shell, git, Python 3.10+ (embit's minimum) and pytest.
- Disk and bandwidth for a pruned mainnet node. Section 02's exercise 1 suggests `prune=10000`.
- Lab 5 needs a machine that can run several Lightning nodes at once (Polar, or Section 07's lab network).
- Optional for Lab 7: a dev board that can run a custom MicroPython build. embit needs the `secp256k1` and extended `hashlib` user modules compiled in; its README links both.

## 🎯 Learning Objectives

After this section you can:
- Stand up, reset and version a three-network bench (regtest, signet, pruned mainnet) with one command. For a given test, choose between instant blocks, shared realistic conditions, or real data.
- Operate Bitcoin Core fluently from `bitcoin-cli` and from Python over JSON-RPC and ZMQ, adapting older tutorials to the release you actually run.
- Build, sign and broadcast every standard output type with your own code, and show it agrees with Bitcoin Core using differential and randomized tests.
- Run multi-party flows end to end — descriptor multisig with PSBTs across independent signers, and a multi-implementation Lightning network — and debug them from node logs and on-chain data.
- (Optional) Qualify a microcontroller signer with hardware-in-the-loop tests: test vectors, timing and fault injection.

## Marking Convention

| Symbol | Meaning |
|--------|---------|
| 🔑 | Must-read / must-watch — essential for understanding this topic |
| ⭐ | Satoshi / Cypherpunk essential canon |

## Resources

These are the bench resources. Each lab also uses on-ramps listed in other sections, named in the lab text:
- Mastering Bitcoin Ch. 3, embit and Bitcoin Dev Kit (Section 10)
- bitcoin-tx-tutorial and btcdeb (Section 04)
- Bitcoin Core's multisig and offline-signing tutorials (Section 08)
- the Optech Schnorr/Taproot workshop (Section 11)

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 🛠️ Practice | Learning Bitcoin from the Command Line (v2.2.2; 3.0 in progress) | Christopher Allen and Shannon Appelcline (Blockchain Commons) | 2020–2026 | [GitHub](https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line) | The lab manual for Labs 0, 1 and 5. Covers Bitcoin Core setup and `bitcoin-cli`, raw transactions, RBF/CPFP, multisig, PSBTs and hardware wallets, timelocks, Script with btcdeb, Tor/I2P, RPC from Python/Rust/Go, Core Lightning, and a regtest appendix. It was written for Bitcoin Core 22, and v30 removed legacy wallets and RPCs such as `dumpprivkey` and `importprivkey`, so expect to translate some steps. A 3.0 rewrite targets late 2026. (Moved here from Section 10.) |
| | 🔧 Tool | Polar | jamaljsr (GitHub) | — | [GitHub](https://github.com/jamaljsr/polar) | One-click Lightning networks on regtest for local development: add nodes by drag and drop, start and stop them, connect over RPC. The quickest Lab 5 bench. |
| | 📜 Standard | BIP 325: Signet and BIP 94: Testnet 4 | Karl-Johan Alm, Anthony Towns; Fabian Jahr | 2019, 2024 | [BIP 325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki) · [BIP 94](https://github.com/bitcoin/bips/blob/master/bip-0094.mediawiki) | Why the test networks behave differently. Signet blocks must also satisfy the network's signature "challenge" script, so the network is predictably rather than randomly unreliable. Testnet4 keeps proof-of-work with testnet's 20-minute minimum-difficulty exception plus a block-storm fix. Testnet3 is being phased out, and a Testnet 5 (BIP 95) is in draft. |
| | 📚 Documentation | Bitcoin Core functional test framework | Bitcoin Core contributors | — | [GitHub](https://github.com/bitcoin/bitcoin/tree/master/test/functional) | The Python framework Bitcoin Core uses to spin up regtest nodes and assert behavior. Its `test_framework/` (e.g. `key.py`, `script.py`) doubles as a reference Python implementation, and both bitcoin-tx-tutorial and the Optech Taproot workshop are built on it. |
| | 📚 Documentation | Bitcoin Core release notes | Bitcoin Core | — | [bitcoincore.org](https://bitcoincore.org/en/releases/) | Read the notes for the version you run before following any tutorial. For example: 28.0 added testnet4 and made full-RBF the default; 29.0 moved the build to CMake; 30.0 removed legacy wallets; 31.0 introduced cluster mempool. |

## Suggested Order

**Core path (🔑):** *Learning Bitcoin from the Command Line*

Each lab has a "done when" criterion. Don't move on until it holds.

0. **Lab 0 — The bench** *(alongside Section 02 · ~4 h)*
   - **Build:** Install the current Bitcoin Core release (read its release notes) and script three nodes, each with its own datadir and config:
     - regtest, with a `fallbackfee`, since regtest has no fee estimates
     - signet
     - pruned mainnet
   - **Reset command:** Write a `make reset` (or a small Python CLI). It wipes regtest, starts it, creates `miner`, `alice` and `bob` descriptor wallets, and mines past coinbase maturity.
   - **Guides:** Mastering Bitcoin Ch. 3 (Section 10), and Learning Bitcoin from the Command Line chs. 2–3 plus Appendix III (Using Bitcoin Regtest). Section 02's exercise 1 then runs on this bench.
   - **Done when:**
     - a cold `make reset` produces a funded regtest network in under a minute, twice in a row with identical behavior;
     - the signet node is synced and holds signet coins;
     - the mainnet node is syncing;
     - a one-page `BENCH.md` records versions, ports, datadirs and what each network is for.
1. **Lab 1 — CLI fluency** *(alongside Sections 02–04 · ~8 h)*
   - **Work:** Learning Bitcoin from the Command Line chs. 3–8 on regtest: wallets and descriptors, sending the easy way and with raw transactions, RBF and CPFP, multisig, PSBTs, locktimes, and OP_RETURN data.
   - **Log:** Keep an adaptation log of every command that had to change for the current release, with the release note that explains it.
   - **Done when:** you can do all of this without looking up syntax, and your log names each changed command:
     - fund and build a payment (`createrawtransaction`, with the change and fee arithmetic done explicitly);
     - sign and broadcast it;
     - RBF-bump it;
     - rescue a stuck one with CPFP.

   Section 06's mempool-policy exercise later goes deeper on the same mechanics.
2. **Lab 2 — Python harness** *(alongside Sections 03–04 · ~5 h)*
   - **Work:** Pull Section 10's exercise 2 (RPC + ZMQ automation) forward and turn it into a package your later labs import:
     - a JSON-RPC client;
     - ZMQ listeners;
     - pytest fixtures that give each test a fresh, funded regtest chain.

     Copy the patterns of Bitcoin Core's functional test framework rather than inventing your own.
   - **Done when:** from a clean checkout, `pytest -q` starts regtest, creates and confirms a transaction, observes it over ZMQ, cleans up after itself, and passes twice in a row.
3. **Lab 3 — Transactions in code** *(alongside Section 04; add P2TR after Section 11 · ~8 h)*
   - **Guided pass:** Do bitcoin-tx-tutorial's notebooks (Section 04).
   - **Your library:** Extend the signer from Section 04's exercise 4 so one interface handles P2PKH, P2SH and P2WSH multisig, P2WPKH and P2TR key-path spends.
   - **Cross-check:** Use embit or Bitcoin Dev Kit (Section 10) as a second implementation.
   - **Done when:** 100 randomized transactions per output type, built and signed by your code, pass `testmempoolaccept`, and your computed txid, wtxid and vsize match `decoderawtransaction` exactly.

   Section 10's mini-project (Differential Test Harness) later extends this to Bitcoin Core's own test vectors.
4. **Lab 4 — Wallet stack: descriptors and PSBT** *(alongside Sections 05 and 08 · ~8 h)*
   - **Work:** Join Section 05's BIP 32/39 code to a PSBT signer of your own that parses, signs and serializes BIP 174.
   - **Reference flow:** Bitcoin Core's multisig and offline-signing tutorials (Section 08). Then replace one Core signer at a time — first with your signer, then with an embit signer.
   - **Done when** both hold:
     - for every pair among {Core, embit, your signer}, co-signing a 2-of-3 `wsh(sortedmulti(…))` spend finalizes and confirms on signet;
     - your parser re-serializes every PSBT Core hands it, byte for byte.

   Section 08's exercise 3 covers Core plus embit only; this lab adds your own signer and the full pairwise matrix.
5. **Lab 5 — Lightning bench** *(alongside Section 07 · ~4 h)*
   - **Work:** Script the network Section 07's exercises need, either in Polar or as a multi-implementation regtest setup. Run Learning Bitcoin from the Command Line's Core Lightning chapters (19–20) on it for CLI fluency.
   - **Done when:** a fresh machine goes from nothing to a funded multi-hop network in under 15 minutes from a script or runbook — fast enough to rebuild before every Section 07 experiment. The network must pass a smoke test:
     - one multi-hop payment;
     - one cooperative close;
     - one force close, swept on-chain.
6. **Lab 6 — Taproot workbench** *(alongside Section 11, or straight after Section 04 · ~6 h)*
   - **Guided pass:** Run the Optech Schnorr/Taproot workshop notebooks (Section 11) against your bench's bitcoind; the notebooks need version 0.21 or later, and Google Colab is the fallback. They cover elliptic-curve math, tagged hashes, Schnorr, MuSig, taptweak, tapscript, taptrees and the degrading-multisig case study.
   - **Your library:** Move tagged hashing, the taptweak and control-block construction into your Lab 3 library.
   - **Done when:** every notebook runs green locally, and those three functions are covered by tests derived from the notebooks. Section 11's exercises 1–2 and its mini-project then run on your own code.
7. **Lab 7 — Embedded signer, hardware in the loop** *(optional · alongside Sections 05 and 08 · ~12 h)*
   - **Device:** Build a MicroPython firmware with embit's required `secp256k1` and `hashlib` user modules and flash a dev board. Give it a small serial protocol: get xpub/descriptor, show address *n*, sign PSBT.
   - **Test rig:** pytest drives the board over USB serial and:
     - replays BIP 39/32/84/86 test vectors and the Lab 4 PSBTs, comparing every result with host-side embit;
     - measures signing latency;
     - injects faults: truncated frames, a power cycle mid-signature, a corrupted PSBT.

     This rig is the test fixture for the hardware mini-projects in Sections 05 and 08.
   - **Done when** all three hold:
     - `pytest --port /dev/ttyACM0` passes every vector;
     - the device's signature appears in a confirmed signet transaction from the Lab 4 matrix;
     - the latency and fault report is generated automatically.

---

## 🛠️ Practice

1. **Pick the network** — For each of six scenarios, choose regtest, signet, a custom signet, testnet4 or pruned mainnet, and justify the choice in one line:
   - a 1,000-block CSV recovery path;
   - fee bumping under competition;
   - wallet sync against real-world UTXO patterns;
   - an opcode that is only proposed (Bitcoin Inquisition runs such opcodes on signet);
   - a week-long Lightning watchtower test;
   - reorg handling.

   Then log a week of block timestamps from your signet node and a testnet4 node (add one to your Lab 0 bench; it isn't one of the three networks there) (`getblockheader`). Plot the inter-block intervals against an exponential distribution with mean 600 s, and explain each deviation using the rules in BIPs 325 and 94. *(~2 h · BIP 325: Signet and BIP 94: Testnet 4)*
2. **Version-drift audit** — Run these steps against the release you have installed:
   - Learning Bitcoin from the Command Line chs. 3–4;
   - bitcoin-tx-tutorial (its README says it was tested with Bitcoin Core 24.0.1);
   - Mastering Bitcoin Ch. 3's build instructions;
   - the Optech Taproot workshop's setup.

   Deliverable: a compatibility table — step → works / changed / removed → the release note that explains it → your fix. *(~2 h · Bitcoin Core release notes; Learning Bitcoin from the Command Line)*
3. **Deterministic regtest** — Make two runs of your Lab 2 fixtures produce identical txids. Control wallet keys (import known descriptors), time (`setmocktime`) and coin selection (explicit inputs). Write down every remaining source of nondeterminism you hit, and say which you eliminated and which you can only control for. Done when a diff of two full runs' transaction logs is empty. *(~2.5 h · Bitcoin Core functional test framework)*
4. **Latency budget** — Measure the cost of one P2WPKH signature, end to end, on each of:
   - your *Programming Bitcoin*-style pure-Python signer;
   - embit's pure-Python fallback;
   - embit with a system libsecp256k1 through its ctypes backend;
   - the RPC round trip to `testmempoolaccept`;
   - if you built Lab 7, the board.

   Deliverable: a table of median and p95 latency, plus three sentences on where the time goes and what you would optimize first. *(~2 h · embit (Section 10); Bitcoin Core functional test framework)*

**🏗️ Mini-project — One-Command Bitcoin Lab:** Package Labs 0–5 (and 7, if built) as a repository a colleague can clone. One command must:
- pin the Bitcoin Core version;
- bring up regtest and signet, plus the Lightning bench;
- run the integration suite: Lab 2 fixtures, Lab 3 differential tests, the Lab 4 PSBT matrix, the Lab 5 smoke test, optionally Lab 7's HIL tests, and Section 10's difftest as an extra stage if you built it;
- write a single pass/fail report with versions and timings.

Treat it like a production test fixture: self-test first, then measurements. Deliverable: `projects/btc/12-lab/` with a README, CI config and a sample report. Success:
- on a fresh VM, `make all` reaches a green report in under 30 minutes with no manual steps;
- a deliberately injected bug (a wrong sighash flag in your signer) turns exactly one check red, with a message that points at the cause.

*(~12 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. What must a signet block contain that a testnet4 block doesn't, and what does that buy you as a tester?
2. Name three things regtest hides that mainnet will expose.
3. Your hand-built transaction decodes cleanly, but `testmempoolaccept` rejects it. Name three different classes of cause and how you would tell them apart.
4. A tutorial tells you to run `dumpprivkey`. Why does that fail on current Bitcoin Core, and what replaces the workflow it supported?
5. What does agreement with `decoderawtransaction` and `testmempoolaccept` prove about your signer, and what can it never prove?
6. "Signet is just testnet with a faucet." What's actually different?
7. Why test a hardware signer against a host-side reference implementation, and not only against Bitcoin Core?
8. Explain to a smart friend, in three sentences, why you keep three networks running instead of one.
