# Bitcoin — Review

> **Deep-dive review, October 2026** · curriculum: [`btc/`](../../btc/) · summary of all nine: [README](README.md)
> ✔ = fixed in this review · ✱ = suggested only. Scorecards rate each section **as found**, before the fixes.

## Verdict
The curriculum's skeleton is sound. The 00→11 arc follows Mastering Bitcoin's logic, the anchor resources are the right ones (Mastering Bitcoin, Programming Bitcoin, Grokking Bitcoin, Learn Me A Bitcoin, Chaincode), and the cypherpunk "canon" framing suits Section 00. It fell short on three fronts. **Currency:** nothing after about 2023 was in it — no BIP 324, package relay, cluster mempool, the 2025 OP_RETURN fight, descriptors, BOLT 12 or splicing, and no proposal statuses — and Section 11 was all unlinked placeholders. **Accuracy:** it contained a hallucinated 🔑 first step ("Learn Me A Bitcoin: Lightning" — the site has no Lightning content), a wrong course title, mislabelled Mastering Bitcoin chapters, unmaintained bitcoin.org docs presented as "official", Stock-to-Flow marked as a must-know, and five broken links. **Hands-on:** running a node, regtest and building transactions only appeared in Section 10, after Lightning, with no CLI course, no libraries and no regtest at all. I grade it **C as found and about B after these edits**. The most important improvement is to treat the hands-on track (Bitcoin Core on regtest/signet → Learning Bitcoin from the Command Line → bitcoin-tx-tutorial) as a parallel lab that starts in week one, not as a late "development" section. On approval, that lab track is now Section 12, and governance is Section 13.

## Scorecard
Scores are for the curriculum **as found**. The verdicts note what was done.

| Section | Cov | Acc | Cur | Seq | Foc | Grade | One-line verdict |
|---|---|---|---|---|---|---|---|
| 00 History & Philosophy | 3 | 4 | 3 | 4 | 3 | B- | Good cypherpunk core, but missing the academic lineage (Bit Gold, *Academic Pedigree*) and anything after 2010; both lineage gaps now added |
| 01 Cryptography | 3 | 4 | 3 | 4 | 3 | C+ | Right anchors, but the signatures chapter (MB Ch 8) and an ECC-math resource were missing; half the rows were unlinked "concepts" |
| 02 Protocol Fundamentals | 3 | 3 | 3 | 4 | 3 | C+ | Solid core; called unmaintained bitcoin.org docs "official" and didn't flag the free editions |
| 03 Mining & Consensus | 3 | 4 | 2 | 4 | 3 | C+ | MB Ch 12 is right; had empty descriptions and no academic, selfish-mining or supply-schedule material |
| 04 Transactions & Script | 3 | 3 | 3 | 4 | 4 | C+ | Good spine; broken prerequisite link, mislabelled chapters, no hands-on transaction building |
| 05 Wallets | 2 | 3 | 2 | 3 | 4 | C- | BIP list stopped at 2021; no descriptors or miniscript, though Bitcoin Core wallets are descriptor-only since v30 |
| 06 Network & P2P | 3 | 3 | 2 | 4 | 4 | C | Missed BIP 324, package relay, cluster mempool and the 2025 policy debate; implied Erlay is deployed |
| 07 Lightning | 3 | 2 | 2 | 3 | 3 | D+ | Hallucinated 🔑 first step; no BOLT spec, no BOLT 12 or splicing; misaligned table |
| 08 Security & Privacy | 3 | 3 | 2 | 4 | 3 | C | Lopp + PSBT are fine; otherwise mostly concept rows, with no MB Ch 13, no hands-on, and no 2024 legal context |
| 09 Economics & Game Theory | 2 | 2 | 2 | 3 | 2 | D | Advocacy-heavy (S2F as 🔑, Saylor, Metcalfe stated as fact); missing incentive economics (fees, security budget) |
| 10 Development | 3 | 3 | 2 | 2 | 3 | C- | Hands-on came last; no regtest, libraries or CLI course; RPC reference frozen at Core 0.21 |
| 11 Advanced & Frontiers | 2 | 3 | 2 | 3 | 2 | D+ | Right headings but every row was an unlinked placeholder, with no statuses and nothing from 2023–26 |
| 12 Hands-on Labs (new) | — | — | — | — | — | new | Created on approval: 8 labs (0–7) run in parallel with 02–10, each with a "done when" criterion, plus Practice, mini-project and Check Yourself |
| 13 Governance & Protocol Change (new) | — | — | — | — | — | new | Created on approval: BIP process, activation history, policy vs. consensus, contested-change case studies; read between 10 and 11 |

## Section-by-section

### 00 — History and Philosophy
- **Strengths:** Whitepaper-first and re-read-last is good pedagogy. The primary sources (b-money, Hashcash, Satoshi's emails via SNI, the Fermat annotated whitepaper) are well chosen, and the ⭐ canon is coherent.
- **Problems:**
  - ✔ Satoshi emails author was "Various".
  - ✔ *The Bitcoin Standard* was presented as neutral history; I added an advocacy caveat.
  - ✱ 🔑 on *The Bitcoin Standard* and *Digital Gold* is generous for a technical curriculum.
  - ✱ *The Sovereign Individual* and *Internet of Money* are duplicated in 09 and tracked three times in PROGRESS.
- **Missing:**
  - The academic lineage: linked timestamping (Haber–Stornetta), Chaum's e-cash, Bit Gold, RPOW.
  - Everything after 2010: Mt. Gox, the 2015–17 blocksize war and UASF (only in books/), Taproot activation, ETFs.
- **Added:**
  - Bitcoin's Academic Pedigree — Arvind Narayanan & Jeremy Clark — 2017 (🔑)
  - Bit Gold — Nick Szabo — 2005

### 01 — Cryptography Foundations
- **Strengths:** The intuition → book → interactive → build-it-yourself progression (3B1B → MB Ch 4 → LMAB → Programming Bitcoin Ch 1–3) is excellent.
- **Problems:**
  - ✔ MB Ch 4 author missing Harding; its description overclaimed ("best explanation of building blocks").
  - ✔ LMAB linked to the homepage; now a deep link.
  - ✔ Programming Bitcoin was not flagged as free (the full text is on GitHub, CC BY-NC-ND).
  - ✔ "Basic math" prerequisite gave no pointer to where the math is taught.
  - ✱ Three of the eight rows were unlinked "Concept" rows.
- **Missing:**
  - The signatures chapter itself (Schnorr/ECDSA, nonce reuse, sighash).
  - Hash-function internals (SHA-256 construction, tagged hashes).
  - A math bridge (finite fields, discrete log).
- **Added:**
  - Mastering Bitcoin Ch. 8: Digital Signatures — Antonopoulos & Harding — 2023 (🔑)
  - Elliptic Curve Cryptography: a gentle introduction (4 parts) — Andrea Corbellini — 2015
  - Cross-link to math/08, where the math agent added Hoffstein–Pipher–Silverman for exactly this purpose.

### 02 — Protocol Fundamentals
- **Strengths:** Grokking → LMAB → Mastering Bitcoin → Programming Bitcoin is a sensible ramp.
- **Problems:**
  - ✔ Developer Guide described as "Official protocol documentation". It is bitcoin.org community docs, © 2009–2020, with an RPC reference frozen at Core 0.21.
  - ✔ Grokking Bitcoin and Programming Bitcoin were marked paid without links; both are free online (Grokking: CC BY-NC-SA at rosenbaum.se).
  - ✔ MB edition and year not stated.
  - ✱ 5 of 9 rows are 🔑, and "Mastering Bitcoin (full book)" as a section-02 item duplicates the chapter-level entries everywhere else.
- **Missing:** consensus rules vs. node policy, soft vs. hard forks, block validation, the UTXO set, reorgs (partly covered now via 03/06).
- **Added:** nothing needed beyond the corrections.

### 03 — Mining and Consensus
- **Strengths:** MB Ch 12 is the right anchor; mempool.space is a good live tool.
- **Problems:**
  - ✔ Empty descriptions on MB Ch 12, the selfish-mining concept and the pools concept.
  - ✔ The selfish-mining concept now links Optech's topic, which carries the Eyal–Sirer paper and the ~1/3-hashrate threshold.
  - ✔ LMAB deep link.
  - ✱ "Andreas Antonopoulos: Bitcoin Q&A on Mining" (🔑) links only to his channel, not to a specific video.
- **Missing:** an academic treatment; the halving schedule with current numbers; pool centralization and template control; how consensus changes are activated.
- **Added:**
  - Bitcoin and Cryptocurrency Technologies, Ch. 2 & 5 — Narayanan, Bonneau, Felten, Miller, Goldfeder — 2016
  - Learn Me A Bitcoin: Block Reward — Greg Walker — current (3.125 BTC since block 840,000)
  - Bitcoin Optech: Soft fork activation — Bitcoin Optech — ongoing (later **moved to Section 13**; 03's Suggested Order now points there)

### 04 — Transactions and Script
- **Strengths:** Good spine (MB 6–7 → LMAB → Programming Bitcoin 5–8 → SegWit → timelocks).
- **Problems:**
  - ✔ Broken prerequisite link (`../01-why-bitcoin/`).
  - ✔ MB chapters mislabelled "Transactions and Script"; Ch 7 is "Authorization and Authentication". Now deep-linked.
  - ✔ Developer Reference called "Official transaction format specification".
  - ✔ The "Transaction Decoder" tool row had no tool.
  - ✔ Programming Bitcoin link added.
- **Missing:**
  - Taproot spending paths, which are still only in 11 although Taproot has been active since 2021.
  - Sighash types; weight/vbytes; fees and RBF (now in 06).
  - Any exercise that builds and signs transactions in code.
- **Added:**
  - bitcoin-tx-tutorial (Jupyter notebooks, regtest) — Darius Parvin / Chaincode Labs
  - btcdeb — Bitcoin Script debugger — kallewoof

### 05 — Wallets and Key Management
- **Strengths:** The derivation-path BIPs (32/39/44/84/86) are presented in a logical order.
- **Problems:**
  - ✔ Broken prerequisite link, which also mis-named Section 01 "Why Bitcoin"; I added Section 04 as a prerequisite.
  - ✔ MB Ch 5 is titled "Wallet Recovery" in the 3rd edition, not "Wallets".
  - ✔ LMAB deep link.
  - ✱ BIP rows have empty author cells.
- **Missing:** output descriptors (Bitcoin Core removed legacy wallets in v30), miniscript and wallet policies, PSBT (in 08), BIP 85, SLIP-39 / Shamir backups, watch-only/xpub privacy.
- **Added:**
  - Output Script Descriptors (BIPs 380–387) + Bitcoin Core descriptors doc — Pieter Wuille, Ava Chow (🔑)
  - BIP 379: Miniscript (+ BIP 388 Wallet Policies) — Wuille, Poelstra, Kanjalkar, Poinsot, Chow; Ingala

### 06 — Network and P2P Layer
- **Strengths:** MB Ch 10 + Chaincode P2P + "run your own node" is the right core.
- **Problems:**
  - ✔ Broken prerequisite link.
  - ✔ Erlay listed as if deployed; BIP 330 is still Draft.
  - ✔ The P2P guide was called official.
  - ✔ The mempool-policy row didn't mention full-RBF (default in Core 28), package relay or TRUC.
  - ✔ The run-a-node practice row had no guidance.
- **Missing:** BIP 324 encrypted transport; eclipse attacks; Tor/I2P; AssumeUTXO; cluster mempool (Core 31.0, Apr 2026); the 2025 OP_RETURN/relay-policy debate.
- **Added:**
  - Mastering Bitcoin Ch. 9: Transaction Fees — Antonopoulos & Harding — 2023
  - BIP 324: Version 2 P2P Encrypted Transport — Mehta, Ruffing, Schnelli, Wuille
  - Bitcoin Optech: Cluster mempool — Bitcoin Optech — 2026
  - Bitcoin Core development and transaction relay policy — 31 Core contributors — 2025, with Optech #352 for both sides and BIP 110 for the Closed consensus counter-proposal

### 07 — Lightning Network
- **Strengths:** The whitepaper and *Mastering the Lightning Network* are the right anchors, and a practice row exists.
- **Problems:**
  - ✔ **Hallucination:** "🔑 Learn Me A Bitcoin: Lightning — Visual Lightning explanations" was step 1 of the order. The site has no Lightning content. I removed the 🔑, corrected the row and replaced step 1.
  - ✔ The concept and practice rows had 6 cells in a 7-column table, so descriptions rendered in the Link column.
  - ✔ MtLN year missing (Dec 2021).
- **Missing:** the BOLT spec itself; BOLT 12 offers (spec 2024); splicing (now in BOLT 2); simple taproot channels; LSPs and liquidity; channel jamming; watchtowers.
- **Added:**
  - Mastering Bitcoin Ch. 14: Second-Layer Applications — Antonopoulos & Harding — 2023 (🔑, new step 1)
  - BOLT specifications — Lightning protocol contributors
  - Chaincode Labs: Lightning Protocol Development seminar — Chaincode Labs
  - Bitcoin Optech topics: Offers (BOLT 12) and Splicing — Bitcoin Optech

### 08 — Security and Privacy
- **Strengths:** The Lopp guide, cold storage → multisig → PSBT ordering is right.
- **Problems:**
  - ✔ Broken prerequisite link.
  - ✔ "Bitcoin Privacy Guide" typed as a Book; it is a web guide.
  - ✔ BIP 174 author missing.
  - ✔ No legal context for CoinJoin (the April 2024 Samourai arrests, per Optech #300).
  - ✱ Six of nine rows are concepts or channel links.
- **Missing:** a security-model chapter; hands-on multisig and PSBT; signing-device threat models (e.g. nonce covert channels); physical "wrench" attacks; the 2024 shrinking of the CoinJoin landscape.
- **Added:**
  - Mastering Bitcoin Ch. 13: Bitcoin Security — Antonopoulos & Harding — 2023
  - Bitcoin Core multisig + offline-signing tutorials (signet, descriptors, PSBT) — Bitcoin Core contributors

### 09 — Economics and Game Theory
- **Strengths:** The topic list (Gresham/Thiers, network effects, mining game theory) points at real questions.
- **Problems:**
  - ✔ Stock-to-Flow was 🔑 and described as fact. I removed the 🔑 and reframed it as a criticized model.
  - ✔ Metcalfe's law was stated as fact ("value grows with the square of users").
  - ✔ Saylor talks were presented as analysis; I added an advocacy note. The Bullish Case and *The Bitcoin Standard* got the same note.
  - ✱ 🔑 on *The Bullish Case for Bitcoin* is still questionable.
  - ✱ Saylor row has no link.
  - ✱ Bullish Case year blank (2018; I couldn't verify it here because of rate limits).
  - ✱ Three books duplicate Section 00.
- **Missing:** the academic economics of Bitcoin. Specifically:
  - the security budget / fee-only regime (Carlsten et al. 2016; Budish 2018/2025)
  - fee-market design (Huberman–Leshno–Moallemi)
  - custody concentration and ETF market structure
  - mining economics (hashprice, energy)
- **Added:**
  - Bitcoin Optech: Fee sniping (the security-budget problem) — Bitcoin Optech
  - Statement on the Approval of Spot Bitcoin ETPs — Gary Gensler (SEC) — 2024
  - Cross-links to econ/02 (game theory) and econ/10 (monetary economics)

### 10 — Development and Programming
- **Strengths:** It names the right communities (PR Review Club, Chaincode, Btrust) and Programming Bitcoin.
- **Problems:**
  - ✔ RPC API linked developer.bitcoin.org, which is frozen at Core 0.21 (it has `importdescriptors` but no `listdescriptors`). It now links the official versioned docs (latest 31.x).
  - ✔ "Bitcoin Developer Documentation — official" corrected.
  - ✔ Mailing list had no link. It moved to Google Groups; BIP 3 is the evidence.
  - ✔ Practice row said testnet/signet. It now says regtest/signet/testnet4; testnet3 is being phased out per the Core 28 notes.
  - ✔ Btrust link and description updated: self-paced track open to all; live cohorts by application, aimed at African developers.
  - ✔ Chaincode curriculum was described as "professional training"; it is a 2016–19-era link syllabus.
  - ✔ Sequencing: I added a "start the hands-on track early" note and reordered so the node comes first.
- **Missing:** regtest; a CLI course; maintained libraries (Python, MicroPython, Rust); Bitcoin Core's Python functional-test framework as a learning tool; Core release notes as a habit.
- **Added:**
  - Mastering Bitcoin Ch. 3: Bitcoin Core: The Reference Implementation — Antonopoulos & Harding — 2023 (🔑)
  - Learning Bitcoin from the Command Line (v2.2.2, 3.0 in progress) — Christopher Allen & Shannon Appelcline — 2020–2026 (🔑) (later **moved to Section 12**, where it is the lab manual; 10's Suggested Order points to the lab track)
  - Chaincode Labs: Bitcoin Protocol Development seminar — Chaincode Labs
  - embit (Python/MicroPython, used by SeedSigner) — Stepan Snigirev — 2020–
  - Bitcoin Dev Kit / Book of BDK (+ Rust Bitcoin Cookbook pointer) — BDK Foundation — 2026

### 11 — Advanced Topics and Frontiers
- **Strengths:** The headings anticipated the right debates (covenants, Ark, Fedimint, silent payments, payjoin, SV2).
- **Problems:**
  - ✔ Every row was an unlinked placeholder with no status. All existing rows now have links and October 2026 statuses:
    - CTV: Draft, not activated (activation discussed Dec 2025)
    - OP_CAT (BIP 347): Complete but not activated
    - OP_VAULT: Closed, with CCV (BIP 443) as proposed replacement
    - Silent payments: wallet, libsecp and Core progress
    - Payjoin v2: BIP 77 Draft
    - SV2: plus Core 30's IPC mining interface
    - Ark: Arkade and Bark live
  - ✔ Added a status snapshot: no soft fork since Taproot (Nov 2021); BIP 3 "Complete" does not mean deployed.
  - ✱ Taproot (active since 2021) still lives here. It should move into 04/05, leaving 11 for unactivated proposals.
- **Missing (now added):** MuSig2 and FROST; the Optech tracking habit; Consensus Cleanup; post-quantum proposals; Runes; Cashu; BitVM; a hands-on Taproot lab.
- **Still missing:** statechains, Liquid/sidechain resources, DLCs, Utreexo, Great Script Restoration (BIPs 440/441).
- **Added:**
  - Bitcoin Optech Topics index — Bitcoin Optech (🔑)
  - Optech Schnorr/Taproot workshop (Jupyter/Colab) — Bitcoin Optech — 2019
  - BIP 327: MuSig2 — Nick, Ruffing, Jin
  - FROST threshold signatures (Optech topic) — Bitcoin Optech
  - Bitcoin Optech: Covenants topic — Bitcoin Optech
  - BIP 54: Consensus Cleanup — Antoine Poinsot, Matt Corallo — 2025
  - Bitcoin Optech: Quantum resistance (BIP 360 P2MR, BIP 361) — Bitcoin Optech
  - Cashu (NUTs specification) — cashubtc
  - BitVM (2023) and BitVM2 (2024) — Robin Linus et al.
  - Runes (specification; active from block 840,000) — Ordinal Theory Handbook

### 12 — Hands-on Labs (new, created in this review)
- **What it is:** The bench, the order and the integration checkpoints for the per-section exercises — not more topic exercises. It is numbered 12 so nothing was renumbered; the intro and a schedule table say to run it alongside Sections 02–10, with Lab 0 alongside Section 02.
- **Labs:** Each has a "done when" criterion. Each one pulls forward, sequences or extends the section exercises it accompanies (e.g. Lab 2 pulls Section 10's exercise 2 forward as shared infrastructure; Lab 4 adds your own signer and a pairwise interop matrix to Section 08's exercise 3) rather than repeating them.
  - Lab 0: three-network bench (regtest, signet, pruned mainnet)
  - Lab 1: CLI fluency
  - Lab 2: Python RPC/ZMQ harness
  - Lab 3: transactions in code, differentially tested
  - Lab 4: descriptor/PSBT interop between Core, embit and your own signer
  - Lab 5: Lightning bench
  - Lab 6: Taproot workbench
  - Lab 7 (optional): hardware-in-the-loop rig for an embit/MicroPython signer, the test fixture for the hardware mini-projects in 05 and 08
- **Practice (4):** network choice plus block-interval measurement; version-drift audit; deterministic regtest; signing latency budget. **Mini-project:** One-Command Bitcoin Lab. **Check Yourself:** 8 questions.
- **Resources (all verified earlier in this run; no new web calls):**
  - Learning Bitcoin from the Command Line (moved from 10)
  - Polar (GitHub README)
  - BIP 325 + BIP 94 (BIP texts)
  - Bitcoin Core functional test framework (repo files)
  - Bitcoin Core release notes (bitcoincore.org release pages for 27.0–31.0)
  - On-ramps in other sections are cross-referenced, not duplicated: MB Ch 3, embit/BDK (10); bitcoin-tx-tutorial, btcdeb (04); Core multisig/offline-signing tutorials (08); Optech Taproot workshop (11).
- **Cross-references added:**
  - 02: lab-track callout under Prerequisites
  - 10: Suggested Order callout; LBTCftCL step points to 12
  - 04: btcdeb row
  - 06: run-a-node row
  - 07: Polar pointer
  - courses: LBTCftCL "Pairs With" → Section 12
  - README learning path; PROGRESS block; SKILL.md mapping

### 13 — Governance and Protocol Change (new, created in this review)
- **What it is:** How Bitcoin changes with no one in charge. It covers:
  - the BIP process under BIP 3 (statuses, and what a BIP is not)
  - consensus vs. relay policy vs. wallet behavior
  - the activation-mechanism history (ISM → BIP 9 → BIP 148/91 → Speedy Trial)
  - three case studies: full-RBF 2022–24, OP_RETURN 2025, CTV/CSFS 2025–26
  - stakeholder power analysis

  Its intro says to read it between 10 and 11. Section 11's status snapshot and Section 03's Suggested Order point to it.
- **Resources (verified earlier in this run):**
  - MB Ch 12 § "Changing the Consensus Rules" (subsection headings)
  - Optech Soft fork activation (moved from 03)
  - BIP 9 + BIP 8 (BIP index)
  - BIP 3 (full text)
  - Bitcoin Core `doc/bips.md` (exists; cited by BIP 3)
  - Optech Replace-by-fee topic (full-RBF chronology)
  - Optech OP_CHECKTEMPLATEVERIFY topic
  - Optech Newsletter #385, 2025 Year-in-Review (site source on GitHub)
  - Chaincode syllabus fork subjects
  - *The Blocksize War* is cross-referenced from books/, not duplicated
- **Practice (5):** layer classifier; BIP 9/8/148 activation state-machine simulation; signaling measured from your own node's headers; full-RBF post-mortem; stakeholder veto map for CTV. These complement Section 11's exercises 3–4 (technical merits and steelmen) rather than repeating them. **Mini-project:** Governance Case File — SegWit Activation. **Check Yourself:** 8 questions.
- **Kept in place:** Section 06's relay-policy statement row stays in 06, because 06's objectives use it for policy vs. consensus. Section 13 re-reads it as a case study instead of duplicating the row.

### books/
- **Problems:**
  - ✔ MB year was "3rd ed"; now "2023 (3rd ed.)", CC BY-SA 4.0.
  - ✔ Programming Bitcoin and Grokking were marked Paid; both are free.
  - ✔ MtLN year missing.
  - ✔ Bitcoin Standard caveat added.
  - ✱ *Internet of Money* and *Little Bitcoin Book* years are blank.
- **Added:** Bitcoin and Cryptocurrency Technologies — Narayanan, Bonneau, Felten, Miller, Goldfeder — 2016 (free draft PDF).

### courses/
- **Problems:**
  - ✔ "MIT Bitcoin and Money" is actually *Blockchain and Money* (MIT 15.S12, Fall 2018); the URL slug and econ/10 agree.
  - ✔ The Princeton/Coursera row had no link.
  - ✔ Btrust link updated.
  - ✱ "Lightning Labs channel" has no link.
  - ✱ Optech newsletter is not a course.
  - ✱ MIT MAS.S62 *Cryptocurrency Engineering and Design* (Dryja & Narula, 2018), the best university Bitcoin-engineering course, is missing. I couldn't verify it because ocw.mit.edu was rate-limited.
- **Added:** Learning Bitcoin from the Command Line — Blockchain Commons.

### blogs-and-references/
- **Problems:**
  - ✔ Developer docs labelled "Official".
  - ✔ Mailing list unlinked.
  - ✔ Testnet/Signet entry outdated.
  - ✔ Optech row now points to the Topics index.
  - ✱ OXT.me is probably offline since the April 2024 Samourai case (it was run by that team); couldn't verify, rate-limited.
  - ✱ "Bitcoin.page" and "Advancing Bitcoin" status unknown.
- **Added:** Bitcoin Core documentation (versioned RPC), Eclair, Bitcoin Knots, Delving Bitcoin.

### PROGRESS.md
- **Problems:**
  - ✔ Added 40 checkbox lines for the additions.
  - ✔ Retitled the MB chapters (Ch 5 Wallet Recovery, Ch 6–7, Ch 10), the LMAB Lightning line, the OP_CAT line, Btrust, and the testnet line.
  - ✱ Section items missing from PROGRESS:
    - 03 "Mining pools"
    - 04 Dev Reference and Decoder
    - 06 Mempool policies
    - 07 Andreas talks
    - 08 Privacy Guide and Andreas
    - 09 Saylor and Sovereign Individual
    - 10 Developer docs and mailing list
    - 11 LMAB Taproot, Payjoin, Inscriptions
  - ✱ *Bitcoin Standard*, *Internet of Money* and *Sovereign Individual* are each tracked three times.
  - ✱ About 25 "concept" lines are learning objectives rather than resources.
- **Added:** see above.

### README.md
- **Problems:**
  - ✔ Programming Bitcoin row now has a link and is marked free.
  - ✱ The Key Resources table should add the Optech Topics index and Learning Bitcoin from the Command Line.
  - ✱ No hands-on/lab guidance.
  - ✱ No "status as of" date.
  - ✱ No note that Taproot is now core material.
- **Added:** nothing else (README not restructured in this review).

### .agents/skills/update-curriculum/SKILL.md
- **Problems:**
  - ✔ Broken `../../PROGRESS.md` link; it should be `../../../PROGRESS.md`.
  - ✔ Wrong directory names in the section map (`04-transactions-and-script/`, `06-network-and-p2p-layer/`).
  - ✔ Dead bitcoin-dev URL (moved to Google Groups).
  - ✔ Inaccurate claim that all tables share one schema.
  - ✔ Added Delving Bitcoin and Optech Topics as sources, plus a rule to quote BIP status precisely.
  - ✱ The skill has no rule to verify a URL, author and year before adding (the cause of the LMAB hallucination).

## Corrections made
| File:line | Was | Now | Evidence URL |
|---|---|---|---|
| btc/04-transactions-and-scripting/README.md:9 | `[Sections 01–03](../01-why-bitcoin/README.md)` (broken) | Links to 01-cryptography-foundations, 02-protocol-fundamentals, 03-mining-and-consensus | (repo tree) |
| btc/05-wallets-and-key-management/README.md:9 | `[Section 01 — Why Bitcoin](../01-why-bitcoin/README.md)` (broken, wrong name) | Section 01 — Cryptography Foundations + added Section 04 prerequisite | (repo tree) |
| btc/06-network-and-p2p/README.md:9 | `[Section 02 — How Bitcoin Works](../02-how-bitcoin-works/README.md)` (broken) | Section 02 — Protocol Fundamentals | (repo tree) |
| btc/08-security-and-privacy/README.md:5 | `../04-transactions-and-script/` (broken) | `../04-transactions-and-scripting/` | (repo tree) |
| btc/.agents/skills/update-curriculum/SKILL.md:76 | `[PROGRESS.md](../../PROGRESS.md)` → btc/.agents/PROGRESS.md (nonexistent) | `../../../PROGRESS.md` (btc/PROGRESS.md) | (repo tree) |
| SKILL.md:58,60 | dirs `04-transactions-and-script/`, `06-network-and-p2p-layer/` | `04-transactions-and-scripting/`, `06-network-and-p2p/` | (repo tree) |
| SKILL.md:26; 10:21; blogs:38 | bitcoin-dev at lists.linuxfoundation.org / unlinked | groups.google.com/g/bitcoindev (+ gnusha.org archive) | https://github.com/bitcoin/bips/blob/master/bip-0003.md |
| 07-lightning-network/README.md:26 | 🔑 "Learn Me A Bitcoin: Lightning — Visual Lightning explanations" (step 1 of order) | No 🔑; marked as on-chain prerequisites only (site has no Lightning content); step 1 → MB Ch 14 | https://learnmeabitcoin.com/ (nav: Explorer/Beginners/Technical/Tools — no Lightning) |
| 07:28–32 | 6 cells in 7-column table (descriptions rendered under Link) | Year cell added | — |
| 07:23 | MtLN year "—" | 2021 (published Dec 21, 2021) + "predates BOLT 12/splicing" | https://github.com/lnbook/lnbook |
| courses/README.md:13 | "MIT Bitcoin and Money" | "Blockchain and Money (MIT 15.S12, Fall 2018)" | https://ocw.mit.edu/courses/15-s12-blockchain-and-money-fall-2018/ (slug) |
| 05:23 | "Mastering Bitcoin, Chapter 5: Wallets" | "Chapter 5: Wallet Recovery" (3rd ed. title) + descriptors in description | https://github.com/bitcoinbook/bitcoinbook/blob/develop/book.adoc |
| 04:22 | "Chapters 6–7: Transactions and Script", author Antonopoulos, repo-root link | "Transactions; Authorization and Authentication", Antonopoulos & Harding, deep link | same |
| 06:22 | "Chapter 10: The Network", repo-root link | "Chapter 10: The Bitcoin Network", deep link | same |
| 01:15, 03:15 (+08, 10, 07 new rows) | MB author "Andreas Antonopoulos" only | Antonopoulos and David Harding (3rd ed., Dec 2023) | https://github.com/bitcoinbook/bitcoinbook (README) |
| 03:15 | MB Ch 12 description empty | Coinbase/subsidy, PoW, retargeting, pools, hashrate attacks, soft vs hard forks | ch12_mining.adoc headings |
| 02:18 | Dev Guide "Official protocol documentation" | Community bitcoin.org guide, © 2009–2020, unmaintained | https://developer.bitcoin.org/ (footer) |
| 04:25 | Dev Reference "Official transaction format specification" | Community reference, frozen ~2020–21; use BIPs 141/143/341 | same |
| 06:24 | Dev Guide P2P "Official P2P protocol documentation" | Community guide, unmaintained since ~2021 | same |
| 10:18; blogs:7 | "Official API and protocol reference" / "Official protocol docs" | Community docs, unmaintained since ~2021, RPC stops at 0.21 | https://developer.bitcoin.org/reference/rpc/index.html (has importdescriptors, lacks listdescriptors/migratewallet) |
| 10:20 | RPC reference → developer.bitcoin.org/reference/rpc/ | https://bitcoincore.org/en/doc/ (versioned; latest 31.x) | https://bitcoincore.org/en/doc/ |
| 10:22; blogs:24 | "Set up Bitcoin Core on testnet/signet" | regtest → signet (BIP 325) / testnet4 (BIP 94, Core 28+); testnet3 being phased out | https://bitcoincore.org/en/releases/28.0/ |
| 06:28 | "Compact blocks (BIP 152), Erlay" (implied deployed) | Erlay (BIP 330) still Draft, not deployed | https://github.com/bitcoin/bips/blob/master/bip-0330.mediawiki |
| 06:29 | "Policy rules, fee markets, RBF, CPFP" | + full-RBF default since Core 28, package relay, TRUC | https://bitcoincore.org/en/releases/28.0/ |
| 02:16; books:10 | Grokking Bitcoin: Book/Paid, no link | Free online, CC BY-NC-SA, rosenbaum.se/book | https://rosenbaum.se/book/ |
| 01:22; 02:19; 04:24; 10:13; books:9; README:73 | Programming Bitcoin: Paid / no link | Free on GitHub (CC BY-NC-ND), O'Reilly 2019 | https://github.com/jimmysong/programmingbitcoin |
| books:7 | MB Year "3rd ed" | "2023 (3rd ed.)", CC BY-SA 4.0 | https://github.com/bitcoinbook/bitcoinbook |
| 08:19 | Bitcoin Privacy Guide typed "Book" | "Web Resource" | https://bitcoiner.guide/privacy/ |
| 08:21 | BIP 174 author blank | Ava Chow (+ PSBT v2 = BIP 370) | https://github.com/bitcoin/bips/blob/master/README.mediawiki |
| 08:17 | CoinJoin concept, no context | + April 2024 Samourai developer arrests, two firms exiting US (Optech #300) | https://bitcoinops.org/en/newsletters/2024/05/01/ |
| 09:16 | 🔑 S2F "Scarcity and supply schedule" | No 🔑; flagged as criticized price model; supply schedule → 03 | (judgement; supply facts: https://learnmeabitcoin.com/technical/mining/block-reward/) |
| 09:18 | "Value grows with the square of connected users" (as fact) | Metcalfe's law is a contested hypothesis for Bitcoin | (judgement) |
| 09:13, 09:20, 09:21; 00:17; books:8 | Bitcoin Standard / Bullish Case / Saylor presented as neutral analysis | Labeled as advocacy, to be read critically | (judgement) |
| 00:19 | Satoshi emails author "Various" | Satoshi Nakamoto (compiled by SNI) | https://satoshi.nakamotoinstitute.org/ |
| 10:14 | Chaincode curriculum "Professional protocol developer training" | Curated link syllabus from the residency; many links 2016–19 | https://github.com/chaincodelabs/bitcoin-curriculum |
| 10:15; courses:11 | Btrust → btrust.builders/pathways/mastering-bitcoin, "8-week developer program" | pathways.btrust.tech; self-paced track open; cohorts by application (Africa-focused); sibling pathways | https://pathways.btrust.tech/ |
| 10:17 | "Saylor University CS120: Bitcoin for Developers" | "CS120: Bitcoin for Developers I", ~18 h, free certificate | https://learn.saylor.org/course/view.php?id=500 |
| courses:12 | Princeton/Coursera, no link | coursera.org/learn/cryptocurrency | https://bitcoinbook.cs.princeton.edu/ |
| 11:35–37, 55–86 | Concept placeholders without links/status | Linked to BIPs/Optech/specs with Oct-2026 status | https://github.com/bitcoin/bips/blob/master/README.mediawiki ; https://bitcoinops.org/en/topics/covenants/ |
| 01:16; 03:17; 04:23; 05:24; 11:24 | LMAB rows linked to homepage, author blank | Deep links (/technical/keys/, /mining/, /transaction/, /keys/hd-wallets/, /upgrades/taproot/), author Greg Walker | https://learnmeabitcoin.com/ (author named on homepage) |
| 03:21–22 | Selfish-mining / pools concepts with empty descriptions | Descriptions + Optech selfish-mining topic link | https://bitcoinops.org/en/topics/selfish-mining/ |
| SKILL.md:73 | "Match the existing table format (one 7-column schema)" | Schemas differ by section; match the target table; quote BIP status | (repo files) |

## Proposed new sections — both ✔ CREATED in this review (`btc/12-hands-on-labs/`, `btc/13-governance-and-protocol-change/`)

### A. Hands-on Lab Track — ✔ created as `btc/12-hands-on-labs/README.md` (run in parallel from Section 02)
- **Why:** Hands-on resources are now present (MB Ch 3, LBTCftCL, bitcoin-tx-tutorial, Core tutorials, Polar, the Taproot workshop, embit/BDK), but they are scattered and Section 10 sits after Lightning. One lab file with a numbered sequence and "done when…" criteria would turn reading into skill.
- **Outline:**
  - Lab 0: Bitcoin Core on regtest + signet; `bitcoin-cli` basics
  - Lab 1: keys and addresses in Python (Programming Bitcoin Ch 1–4 or embit)
  - Lab 2: hand-build and sign P2WPKH/P2TR transactions
  - Lab 3: descriptor multisig + PSBT + air-gapped signing on signet
  - Lab 4: RBF/CPFP and package relay on regtest
  - Lab 5: a Lightning network in Polar; open, pay and close channels
  - Lab 6: Schnorr/MuSig/Taptree notebooks
  - Lab 7: optional MicroPython signer on a dev board (embit) — fits Aaron's embedded background
- **Resources (all verified):**
  1. Mastering Bitcoin Ch 3 — https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch03_bitcoin-core.adoc
  2. Learning Bitcoin from the Command Line v2.2.2 — https://github.com/BlockchainCommons/Learning-Bitcoin-from-the-Command-Line
  3. bitcoin-tx-tutorial — https://github.com/chaincodelabs/bitcoin-tx-tutorial
  4. Bitcoin Core multisig tutorial — https://github.com/bitcoin/bitcoin/blob/master/doc/multisig-tutorial.md and offline signing — https://github.com/bitcoin/bitcoin/blob/master/doc/offline-signing-tutorial.md
  5. Polar — https://github.com/jamaljsr/polar
  6. Optech taproot-workshop — https://github.com/bitcoinops/taproot-workshop
  7. embit — https://github.com/diybitcoinhardware/embit
  8. Rust Bitcoin Cookbook — https://rust-bitcoin.org/book/

### B. Governance and Protocol Change — ✔ created as `btc/13-governance-and-protocol-change/README.md` (read between 10 and 11)
- **Why:** Nothing teaches *how Bitcoin changes and who decides*. That is the lens needed for every item in 11 and for the 2025 policy fight. The pieces are currently scattered across 03, 06 and 11.
- **Outline:**
  - The BIP process (BIP 2 → BIP 3)
  - Consensus vs. policy
  - Activation history (flag days → ISM → BIP 9 → BIP 148/91 → Speedy Trial)
  - Hard vs. soft forks
  - The blocksize war
  - Core's development and release process
  - Node-implementation diversity (Core, Knots, btcd)
  - Relay-policy controversies (full-RBF, OP_RETURN 2025, BIP 110)
- **Resources (verified):**
  1. BIP 3: Updated BIP Process (Murch, 2025) — https://github.com/bitcoin/bips/blob/master/bip-0003.md
  2. Optech: Soft fork activation — https://bitcoinops.org/en/topics/soft-fork-activation/
  3. BIP 9 (version bits; Deployed) — https://github.com/bitcoin/bips/blob/master/bip-0009.mediawiki
  4. BIP 8 (lock-in by height; Complete) — https://github.com/bitcoin/bips/blob/master/bip-0008.mediawiki
  5. Mastering Bitcoin Ch 12 §"Changing the Consensus Rules" — https://github.com/bitcoinbook/bitcoinbook/blob/develop/ch12_mining.adoc
  6. Bitcoin Core relay-policy statement (2025) — https://bitcoincore.org/en/2025/06/06/relay-statement/
  7. Optech #352 (both sides) — https://bitcoinops.org/en/newsletters/2025/05/02/
  8. Chaincode syllabus: "Soft Forks & protocol overview" and "Consensus Changes & Hard Forks" subjects — https://github.com/chaincodelabs/bitcoin-curriculum
  - Also *The Blocksize War* (Bier, 2021), already in books/.

## Cut candidates
- **03 "Andreas Antonopoulos: Bitcoin Q&A on Mining" (🔑)** — links to the channel homepage, not a mining video. Give it a specific video link or demote it.
- **Channel-only links** — 07 "Andreas Lightning talks", 08 "Andreas on privacy", courses #2 and #8 ("Lightning Labs channel" has no link). Generic channel links don't count as resources.
- **07 "Learn Me A Bitcoin (on-chain prerequisites only)"** — formerly the hallucinated Lightning entry. It is kept only because of append-only; it is now redundant.
- **09 "Michael Saylor Bitcoin talks"** — no link, promotional. Also "Stock-to-Flow model" (now demoted).
- **09 duplicates of 00** — *The Bitcoin Standard*, *Internet of Money*, *Sovereign Individual*. Keep each in one place; PROGRESS tracks each three times.
- **developer.bitcoin.org entries** — four of them (02 Dev Guide, 04 Dev Reference, 06 P2P guide, 10 Dev Docs), plus the 🔑 in blogs. They are unmaintained since about 2021; consolidate to one "background only" row.
- **02 "3Blue1Brown" re-watch** — a duplicate of 01.
- **blogs: OXT.me** — likely offline since April 2024 (operated by the Samourai team). I couldn't confirm because of rate limits.
- **blogs: "Bitcoin.page" and "Advancing Bitcoin"** — currency unknown.
- **About 25 unlinked "Concept" rows across 01–09** — these are learning objectives, not resources. Fold them into the forthcoming Learning-Objectives blocks or link each to its LMAB or Optech page.

## Structural observations
- **Five different table schemas:**
  - 00/08/09/10: 7 columns, plain types
  - 01–03: 6 columns, no Year
  - 04–06: 6 columns, emoji types
  - 07: 7 columns, emoji types
  - 11: 5 columns, no Author or Year

  Sections 04–07 also repeat a "Marking Convention" table that the others lack. I matched each table as found; one 7-column schema is recommended.
- **Taproot is misfiled as "frontier".** It has been active since Nov 2021 and is covered in MB Ch 7, with BIP 86 in 05. Move BIPs 340–342 into 04 and keep 11 for unactivated proposals. No soft fork has activated since Taproot.
- **Mastering Bitcoin is now mapped chapter by chapter** (Ch 3→10, 4→01, 5→05, 6–7→04, 8→01, 9→06, 10→06, 12→03, 13→08, 14→07). A one-line "reading map" in README would make it the explicit spine. Ch 1–2 and 11 are unmapped (they fit 00 and 02).
- **The hands-on path was missing or misplaced.** The fix is in 10's order and notes; a dedicated lab track is proposed above.
- **Overlap with econ:**
  - btc/09 overlaps econ/10, which also has *The Bitcoin Standard* 🔑, the whitepaper 🔑 and Gensler's MIT course 🔑.
  - Recommendation: btc/09 should own Bitcoin-specific incentive economics (fees and security budget, mining game theory, custody and market structure), defer general monetary theory to econ/10, and defer game-theory foundations to econ/02. Cross-links have been added.
  - The Budish (2018/QJE) and Carlsten et al. (CCS 2016) papers belong in one of the two. I couldn't verify them here, so the econ agent or a follow-up should add them.
- **Overlap with math:**
  - math has no number-theory or ECC section. However, during this run the math agent added Hoffstein–Pipher–Silverman, *An Introduction to Mathematical Cryptography*, to math/08, explicitly for btc's keys and signatures.
  - btc/01 now links to math/08. Programming Bitcoin Ch 1–3 and Corbellini cover the practical math, so the gap is closed for self-study.
- **⭐ canon:** Bit Gold and *Bitcoin's Academic Pedigree* are natural canon candidates (Szabo; Haber–Stornetta lineage). I did not mark them ⭐, because the canon list in README is the authority — Aaron's call.
- **Root README needs a follow-up.** The repository's top-level `README.md` (outside `btc/`, so not edited here) still lists twelve btc sections. Add "Hands-on Labs" (parallel from 02) and "Governance" (between 10 and 11) to its btc Sections line.
- **The agent skill caused the drift.** It gave no instruction to verify links, authors or years and had wrong paths. Paths are fixed and a status rule added; it still needs a rule like "fetch and confirm before adding".
- **Pages I could not read** (WebFetch HTTP 429 rate limits, or robots.txt):
  - api.crossref.org (Academic Pedigree DOI) — the ACM Queue page itself was read
  - arxiv.org/abs/1311.0243 and api.semanticscholar.org — verified instead via the Optech selfish-mining topic source
  - bitcoincore.org decoderawtransaction page
  - groups.google.com/g/bitcoindev — verified via BIP 3
  - en.bitcoin.it/wiki/Privacy — not added
  - nber.org w24717 and the uchicago Budish PDF — Budish not added
  - ocw.mit.edu MAS.S62 — not added
  - bitcoiner.guide — author not filled
  - oxt.me — status unconfirmed
  - btrust.builders (robots) — used pathways.btrust.tech instead
  - Also: the shared WebSearch budget ran out early, so later checks used primary sources fetched from raw GitHub (BIPs index, Bitcoin Core docs, Optech site source).

## Top 5 priorities for Aaron in this curriculum
1. **Start the lab track now — Section 12, Lab 0 — in parallel with Section 02.** Run Bitcoin Core on regtest/signet (MB Ch 3), work through Learning Bitcoin from the Command Line, then hand-build and sign legacy, SegWit and Taproot transactions in Python with bitcoin-tx-tutorial. Use embit to experiment on a microcontroller; it is a natural bridge to your embedded work.
2. **Make Mastering Bitcoin 3rd ed. (2023) the spine,** now mapped chapter by chapter across the sections. Use the BIPs and the official bitcoincore.org docs, not developer.bitcoin.org (unmaintained since about 2021), for anything current.
3. **Before holding meaningful funds, do Sections 05 and 08 hands-on.** Learn descriptors, then descriptor multisig with PSBTs and air-gapped signing on signet using Bitcoin Core's own tutorials. Back up descriptors, not just seeds.
4. **Read Section 13 (governance) before Section 11, and use the Optech Topics index as the source of truth for anything in Section 11.** No soft fork has activated since Taproot; covenants, Consensus Cleanup and post-quantum proposals are all still proposals as of October 2026. Read primary sources, not crypto-media takes.
5. **Read Section 09 adversarially.** Do the incentive economics first (fee sniping / security budget, selfish mining, Princeton Ch 5), pair it with econ/02 and econ/10, and treat S2F, *The Bullish Case* and Saylor as arguments to test, not facts.

## Addendum — consistency pass on the merged 🎯/🛠️/✅ blocks (no web calls)
I made 34 minimal edits so every exercise points to resources listed in its own section, or names the section that lists them.
- **Missing spec links added:** BIP 340/327 on 01's signatures concept; BIP 141/143 on 04's SegWit concept. 04's Programming Bitcoin row now covers ch. 13.
- **Cross-section citations** ("(Section NN)") for: the whitepaper; Programming Bitcoin and Grokking Bitcoin used in 03/06; Mastering Bitcoin ch. 9 and ch. 12 used outside 06/03; BIP 54 and BIP 94; Miniscript; embit/BDK; Polar (now in 12); the relay-policy statement.
- **Unverifiable specifics removed:** the `getmempoolcluster` RPC name (06), PlanB's article title (09) and the "bitcoinutils" library (04).
- **Optional reading:** ESP-Miner in 03's mini-project is now marked optional.
- **New-resource citations:** 09's fee-sniping exercise now cites the Optech Fee sniping row; 11's covenant scorecard cites the Optech Covenants topic.
- **Pointers to Lab 7:** added from the hardware mini-projects in 05 and 08.
- **Checked, no changes needed:** no merged block referenced "Learn Me A Bitcoin: Lightning", "Bitcoin and Money", a wrong Mastering Bitcoin chapter title, "official" bitcoin.org docs, or an activation claim. 09's objectives and Check Yourself already treat Stock-to-Flow critically.
