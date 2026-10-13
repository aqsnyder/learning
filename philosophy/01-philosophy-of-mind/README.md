# Philosophy of Mind

## Why This Section Matters

The philosophy of mind asks the most fundamental questions in this curriculum: What is a mind? How does subjective experience arise from physical matter? Is the mind identical to the brain, or something more? These questions aren't merely academic — they directly determine whether we believe machines can think, whether AI could ever be conscious, and what moral status artificial minds might deserve. The positions you encounter here (dualism, physicalism, functionalism) form the conceptual vocabulary for every later section.

## Prerequisites

- [Section 00 — Foundations of Philosophy](../00-foundations-of-philosophy/README.md)

## 🎯 Learning Objectives

After this section you can:
- Lay out substance dualism, behaviorism, type identity theory and functionalism, giving the strongest argument for and the strongest objection to each.
- Reconstruct Descartes' conceivability argument and Kim's causal exclusion argument in standard form, and say which premise each rival position rejects.
- Explain multiple realizability and write a functional (machine-table) specification of a mental state that two physically different implementations both satisfy.
- State precisely what Nagel's bat and Jackson's Mary are supposed to show physical knowledge leaves out, and evaluate one physicalist reply.
- Apply psychological-continuity views and Parfit's fission argument to copying and forking minds, including AI agents.

## Marking Convention

| Symbol | Meaning |
|--------|----------|
| 🔑 | Must-read — essential for understanding this topic |

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|-----------|------|------|-------------|
| 🔑 | 📕 Book | Philosophy of Mind (3rd Edition) | Jaegwon Kim | 2010 | — | The standard textbook. Systematically covers dualism, behaviorism, identity theory, functionalism, and mental causation. Clear, rigorous, and fair to all positions. |
| 🔑 | 📄 Paper | What Is It Like to Be a Bat? | Thomas Nagel | 1974 | [Link](https://www.jstor.org/stable/2183914) | Argues that consciousness has an irreducibly subjective character that cannot be captured by objective, physical science. One of the most cited papers in all of philosophy. |
| | 📕 Book | Meditations on First Philosophy (Meditation II and VI) | René Descartes | 1641 | [Free](https://www.earlymoderntexts.com/assets/pdfs/descartes1641.pdf) | The origin of substance dualism. Descartes argues mind and body are fundamentally different kinds of substance. Essential historical context. |
| | 📕 Book | The Concept of Mind (selections) | Gilbert Ryle | 1949 | — | Ryle's devastating critique of Cartesian dualism — the idea of mind as a "ghost in the machine." Lays groundwork for behaviorism and functionalism. |
| 🔑 | 📄 Paper | The Nature of Mental States | Hilary Putnam | 1967 | — | Introduces machine-state functionalism: mental states are defined by their functional roles, not their physical substrate. Foundational for AI philosophy. |
| | 📄 Paper | Epiphenomenal Qualia (Mary's Room) | Frank Jackson | 1982 | [Link](https://doi.org/10.2307/2960077) | The famous "Mary the color scientist" thought experiment. Argues that physical knowledge leaves out subjective experience. |
| 🔑 | 📝 Encyclopedia | Functionalism | SEP | — | [SEP](https://plato.stanford.edu/entries/functionalism/) | Comprehensive entry on the view that mental states are constituted by their functional relations. Key bridge to philosophy of AI. |
| | 📝 Encyclopedia | Qualia | SEP | — | [SEP](https://plato.stanford.edu/entries/qualia/) | The subjective, experiential properties of mental states. Central concept for consciousness debates. |
| | 🎓 Course | Philosophy and the Sciences: Introduction to the Philosophy of Cognitive Sciences | University of Edinburgh (Suilin Lavelle, Mark Sprevak, Andy Clark et al.) | — | [Coursera](https://www.coursera.org/learn/philosophy-cognitive-sciences) | Accessible video course with modules on evolution and the mind, what consciousness is, intelligent machines and the brain, and embodied cognition (taught in part by Andy Clark). A video companion for Sections 01, 02 and 04. |
| | 📝 Encyclopedia | Personal Identity | SEP | — | [SEP](https://plato.stanford.edu/entries/identity-personal/) | Eric Olson's entry on what makes you the same person over time: psychological-continuity views, animalism, fission cases, and brain-state transfer. The question every "mind upload" or "copied AI" scenario turns on. |
| | 📕 Book | Reasons and Persons (Part III: Personal Identity) | Derek Parfit | 1984 | [Link](https://doi.org/10.1093/019824908X.001.0001) | Parfit's teletransporter and fission cases lead to the conclusion that personal identity is not what matters — psychological continuity is. One of the most important works of 20th-century philosophy, and directly relevant to copying, forking, and uploading minds. |

## Suggested Order

1. **Kim — Philosophy of Mind** — Read chapters 1–5 for the systematic overview of all major positions
2. **Descartes — Meditations II & VI** — Understand the dualist position that set the agenda
3. **Ryle — The Concept of Mind** — See how dualism was challenged from the behaviorist side
4. **Putnam — The Nature of Mental States** — Grasp functionalism, the view most relevant to AI
5. **SEP — Functionalism** — Deepen your understanding of functional-role theories
6. **Nagel — What Is It Like to Be a Bat?** — Confront the limits of functionalism and physicalism
7. **Jackson — Epiphenomenal Qualia** — Another powerful challenge: the knowledge argument
8. **SEP — Qualia** — Round out your understanding of subjective experience
9. **SEP — Personal Identity** — What makes a mind the same mind over time?
10. **Parfit — Reasons and Persons, Part III** — Teletransporters and fission: why identity may not be what matters

---

## 🛠️ Practice

1. **Descartes vs. Ryle** — Reconstruct the Meditation VI conceivability argument for the real distinction (I clearly and distinctly conceive mind without body → God could make them exist apart → they are really distinct) in standard form and mark its weakest premise. Then give Ryle's diagnosis from *The Concept of Mind*: what is the category mistake (the visitor who asks where "the University" is), and does it refute Descartes or change the subject? Apply the same test to four sentences from current AI talk — e.g., "Where in the weights is the fact that Paris is in France stored?", "The agent's self lives in its system prompt" — and rewrite each as a dispositional claim Ryle would accept, or defend it as it stands. *(~3 h · Descartes, Meditations II & VI; Ryle, The Concept of Mind; Kim, chapters on dualism and behaviorism)*
2. **Pain on two substrates** — Write a Putnam-style machine table for a toy "pain" state: inputs {tissue damage, analgesic, distraction}, states {normal, pain, relief}, outputs {withdraw, say "ouch", guard}. Realize it twice: a Python class, and a C lookup table on any microcontroller board (buttons in, LEDs out) — or a second, structurally different Python implementation. Drive both with the same 50-step input sequence and diff the output logs; they must match exactly. Then 400 words: by Putnam's criteria and the SEP *Functionalism* entry's, is either implementation in pain? Apply the absent-qualia ("China brain") worry discussed in the SEP entry and say which way it cuts, and say what a type-identity theorist (Kim's chapter on the identity theory) concludes instead. *(~4 h · Putnam, "The Nature of Mental States"; SEP Functionalism; Kim)*
3. **What Mary learns, with an LLM in the room** — Reconstruct Jackson's knowledge argument in at most five premises, and Nagel's argument from the subjective character of bat experience. Apply both to an LLM that can describe color science, first-person color reports and the phenomenology literature flawlessly: do the arguments show anything about what the model lacks, or only about what *descriptions* lack? Evaluate one physicalist reply — the ability hypothesis, acquaintance, or phenomenal concepts (Kim's consciousness chapters or SEP *Qualia*) — in 400 words, noting that Jackson himself later abandoned the argument's conclusion. *(~3 h · Jackson, "Epiphenomenal Qualia"; Nagel, "What Is It Like to Be a Bat?"; SEP Qualia; the Edinburgh "Philosophy and the Sciences" course for review)*
4. **Exclusion and the firmware** — State Kim's causal exclusion argument as five jointly inconsistent claims (mental causation, causal closure of the physical, causal exclusion, no systematic overdetermination, mental–physical distinctness). Run it on a case you know: "The firmware's overcurrent-fault state caused the gate driver to switch the MOSFET off." Does the argument show that the firmware state is causally idle, given transistor-level physics? Decide which of the five claims you reject for the firmware case, and whether the same move is available for minds. 500 words. Check: your verdict must be consistent across both cases or explain the disanalogy. *(~2.5 h · Kim, chapter on mental causation)*
5. **Fission for agents** — From the SEP *Personal Identity* entry and *Reasons and Persons* Part III, reconstruct Parfit's fission argument in standard form (each successor has an equal claim; identity is one-one and transitive; so neither is you; yet everything that matters is preserved; so identity is not what matters). Apply it to (a) a teletransporter that malfunctions and leaves the original alive, and (b) an LLM agent whose memory file and context are cloned into two instances that then diverge. For each, give the psychological-continuity verdict and the animalist verdict. Where does the AI case make Parfit's conclusion easier to accept, and where harder? 600 words. *(~3 h · SEP Personal Identity; Parfit, Reasons and Persons Part III)*

**🏗️ Mini-project — Mind–Body Debate Map:** Build a structured debate map of the mind–body problem as a YAML file plus a short Python script that renders it with Graphviz (or hand-written Mermaid). Include at least five positions (substance dualism, behaviorism, type identity, functionalism, Jackson-style epiphenomenalist property dualism) and at least eight arguments (conceivability, pairing/interaction problem, category mistake, multiple realizability, absent/inverted qualia, the bat argument, the knowledge argument, causal exclusion), with *supports*/*attacks* edges each annotated with a source and section. Then write a 1,500-word position paper defending where you land, with the two strongest objections and your replies. Deliverable: `projects/philosophy/01-mind-body-map/` (`map.yaml`, `render.py`, `map.svg`, `paper.md`). Success: every position has at least one incoming *attacks* edge from a source its own defenders take seriously, and the paper names the premise you reject in each argument against your view. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Descartes' conceivability argument for mind–body distinctness in three premises, and name the mistake Ryle thinks the whole Cartesian picture makes.
2. What is multiple realizability, and why does it count against type identity theory but not against functionalism?
3. What does Nagel mean by "what it is like", and why does he think an objective science must leave it out?
4. According to Jackson, what does Mary learn when she leaves the room — and what does the ability hypothesis say she gains instead?
5. Misconception probe: "Functionalism says the mind is software, so functionalism implies today's LLMs have minds." What does functionalism actually commit you to, and what would you have to check before drawing that conclusion?
6. List the five claims in Kim's exclusion argument and say which one non-reductive physicalists are under most pressure to give up.
7. In Parfit's fission case, why can't both successors be you, and what does Parfit conclude about what matters in survival?
8. Explain to a smart friend in 3 sentences why the mind–body problem matters for whether an AI could have a mind.
