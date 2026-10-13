# Graph Theory and Combinatorics

## Why This Section Matters

Graphs are the natural mathematical language for relationships and networks — from social networks and molecular structures to knowledge graphs and neural network architectures. Graph theory provides the foundation for graph neural networks (GNNs), spectral clustering, PageRank, and network science. Combinatorics, the mathematics of counting and discrete structures, underpins algorithm analysis, probability, and coding theory. As ML increasingly moves toward structured and relational data, these topics become essential rather than optional.

---

## Prerequisites

- Section 00 (Mathematical Thinking) — proof techniques
- Section 01 (Linear Algebra) — eigenvalues, matrix operations

---

## 🎯 Learning Objectives

After this section you can:
- Prove foundational graph theorems — tree characterizations, bipartite ⇔ no odd cycle, Euler's formula and the non-planarity of K₅ and K₃,₃, Hall's theorem — with clean combinatorial arguments.
- Count discrete structures with bijections, generating functions, inclusion–exclusion, and transfer matrices, and confirm the counts by brute force and the OEIS.
- Model a resistor network as a weighted graph Laplacian and compute node potentials, effective resistances, and spanning-tree counts (Kirchhoff's matrix-tree theorem).
- Partition and cluster graphs with Laplacian eigenvectors, and state precisely what Cheeger's inequality guarantees about the resulting cut.
- Derive the GCN propagation rule from spectral graph filtering and explain over-smoothing as repeated low-pass filtering.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book (Free) | Graph Theory | Reinhard Diestel | 2025 | [Link](https://diestel-graph-theory.com/) | The standard graduate text (6th edition, Springer GTM 173). Comprehensive and rigorous; the main text is free to read online as a preview. Covers connectivity, matching, coloring, planarity, flows, and more. |
| | Book | Introduction to Graph Theory | Douglas West | 2001 | — | More accessible than Diestel with extensive exercises. Good first book for graph theory with emphasis on combinatorial proofs. |
| | Book | Algebraic Graph Theory | Chris Godsil, Gordon Royle | 2001 | — | Connects graph theory to linear algebra: adjacency matrices, Laplacians, spectral properties. Essential foundation for spectral graph theory and GNNs. |
| | Course (Free) | Spectral Graph Theory | Daniel Spielman | — | [Link](http://www.cs.yale.edu/homes/spielman/sgta/) | Yale course on spectral graph theory — the mathematics behind spectral clustering, graph Laplacians, and random walks on graphs. |
| | Paper | Semi-Supervised Classification with Graph Convolutional Networks | Thomas Kipf, Max Welling | 2016 | [Link](https://arxiv.org/abs/1609.02907) | The GCN paper. Understanding this requires spectral graph theory — seeing the math behind it deepens appreciation of both. |
| | Book | Combinatorics and Graph Theory | John Harris, Jeffry Hirst, Michael Mossinghoff | 2008 | — | Accessible introduction covering both combinatorics and graph theory with good problem sets. Good starting point. |
| | Video Series | Graph Theory (Full Course) | Sarada Herke | — | [Link](https://www.youtube.com/playlist?list=PLoJC20gNfC2gmT_5WgwYwGMvgCjYVsIQg) | Clear, methodical video lectures covering fundamental graph theory. Good visual supplement. |
| | Paper | Geometric Deep Learning: Grids, Groups, Graphs, Geodesics, and Gauges | Bronstein et al. | 2021 | [Link](https://arxiv.org/abs/2104.13478) | The manifesto connecting graph theory, group theory, and geometry to deep learning. Seeing the mathematical unification is powerful. |
| | Book | Networks | Mark Newman | 2018 | — | Comprehensive treatment of network science: random graphs, small worlds, community detection, spreading processes. Bridges theory and real-world applications. |

---

## Suggested Order

1. **Harris, Hirst & Mossinghoff** or **Herke videos** — Start with an accessible introduction to graph fundamentals.
2. **Diestel — Graph Theory** — The core text. Work through the key chapters on connectivity, matching, and planarity.
3. **Godsil & Royle** or **Spielman's course** — Study spectral graph theory to connect graphs to linear algebra.
4. **Kipf & Welling — GCN paper** — See the mathematical ideas applied to deep learning.
5. **Bronstein et al. — Geometric Deep Learning** — For the grand unified view connecting graphs, groups, and geometry.
6. **Newman — Networks** — For network science applications.

---

## 🛠️ Practice

1. **Core proofs** — Prove: (a) the handshake lemma and its corollary that every graph has an even number of odd-degree vertices; (b) a tree on n vertices has n − 1 edges, and any two of {connected, acyclic, n − 1 edges} imply the third; (c) a graph is bipartite iff it has no odd cycle; (d) Euler's formula V − E + F = 2 for connected plane graphs, then E ≤ 3V − 6 (and E ≤ 2V − 4 without triangles), hence K₅ and K₃,₃ are non-planar; (e) Hall's marriage theorem (the hard direction by induction). Optional Lean 4: Mathlib's `SimpleGraph` library contains the handshake lemma — prove the odd-degree corollary from it yourself, then compare with the library's version. *(~6 h · Diestel Ch. 1, 2, 4; Harris, Hirst & Mossinghoff; West for extra exercises; Herke's videos for intuition)*
2. **Counting three ways** — (a) Catalan numbers: count balanced strings of n pairs of parentheses by brute force for n ≤ 12, derive C(x) = (1 − √(1 − 4x))/(2x) from the first-return decomposition, extract Cₙ = (2n choose n)/(n + 1), and match OEIS A000108. (b) Derangements by inclusion–exclusion: show Dₙ/n! → 1/e with error below 1/(n + 1)!. (c) A run-length-limited line code: count binary strings of length n with no two adjacent 1s using the transfer matrix [[1, 1], [1, 0]]; show the count grows like φⁿ, so the constraint's capacity is log₂φ ≈ 0.694 bits per symbol. *(~4 h · the combinatorics chapter of Harris, Hirst & Mossinghoff; the OEIS)*
3. **Resistor networks are Laplacians** — Build the Laplacian of a cube of 1 Ω resistors (the graph Q₃). Compute effective resistances R_eff(a, b) = (e_a − e_b)ᵀL⁺(e_a − e_b) across an edge, a face diagonal, and the body diagonal — expect 7/12, 3/4, and 5/6 Ω — and confirm the body diagonal by hand using symmetry (merge equipotential nodes). Check Foster's theorem (the sum of R_eff over all edges is n − 1 = 7), count spanning trees with the matrix-tree theorem (384), and confirm 384 by brute force over all 792 seven-edge subsets. *(~3 h · Spielman's spectral graph theory notes on electrical networks and effective resistance; Godsil & Royle on the Laplacian; 18.06 Lecture 12, Section 01)*
4. **Spectral partitioning of a real netlist** — Export the netlist of one of your KiCad boards and build a graph: components are nodes, and edges are weighted by the number of shared signal nets (drop GND and power rails, which connect everything). Compute the normalized Laplacian, its Fiedler vector, and the best sweep cut; report the cut's conductance φ and check Cheeger's inequality λ₂/2 ≤ φ ≤ √(2λ₂). Compare the two-way partition, then a k-way one (k eigenvectors + k-means), with how you actually floor-planned the board. *(~4 h · Spielman (Cheeger's inequality, sweep cuts); 18.065 Lecture 35 (finding clusters in graphs; Section 01); Newman, Networks, on community detection)*
5. **A GCN layer is a graph low-pass filter** — Re-derive Kipf & Welling's rule H′ = σ(D̃^(−½)ÃD̃^(−½)HW) from the first-order Chebyshev approximation of a spectral filter (K = 1, λ_max ≈ 2, one shared parameter, then the renormalization trick). Numerically: show the eigenvalues of D̃^(−½)ÃD̃^(−½) lie in (−1, 1] on random graphs and on Zachary's karate club (`networkx.karate_club_graph`); show that applying it k times to random node features converges to its top eigenvector (over-smoothing), at a rate set by the second-largest eigenvalue modulus. Finally, reproduce the paper's appendix demo: an untrained, random-weight GCN already separates the karate club's communities in 2-D. *(~4 h · Kipf & Welling, the GCN paper; Spielman on the Laplacian spectrum; Bronstein et al., Geometric Deep Learning, on graphs)*

**🏗️ Mini-project — DC IR-drop solver for a copper pour:** Discretize a PCB copper region as a grid graph — start with a 50 × 30 mm rectangle of 1 oz copper (R_sq ≈ 0.49 mΩ/□ for 35 µm at ρ = 1.72 × 10⁻⁸ Ω·m) with 0.25 mm cells, where each edge between adjacent cell centers is one square of copper. Remove nodes for slots and antipads, ground the regulator node, inject the load currents, and solve the grounded Laplacian system with `scipy.sparse.linalg.spsolve`. Validate against closed forms first: far from the edges of a large grid, adjacent-node resistance → R_sq/2 and diagonal-neighbor resistance → 2R_sq/π; a strip with busbars at both ends gives R_sq·L/W. Then map the voltage drop over a real board outline (imported as a bitmap or polygon), find the worst-case load, and show how a slot in the pour changes it. Deliverable: `projects/math/06-ir-drop/` with code, a validation table, and heatmaps. Success: every validation case is within 1% (or within a discretization error you quantify by refining the mesh), and the write-up explains the results with Thomson's principle (current distributes to minimize dissipated power) and Rayleigh monotonicity (removing copper can never lower resistance). *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. State Euler's formula for connected plane graphs and use it to prove that K₅ is not planar.
2. State Hall's marriage theorem.
3. Why does the multiplicity of the eigenvalue 0 of a graph Laplacian equal the number of connected components?
4. What does the Fiedler value λ₂ measure, and what does Cheeger's inequality promise about the best sweep cut?
5. Estimate: how many labeled trees are there on 10 vertices? How would you count the spanning trees of an arbitrary graph?
6. Misconception: can adding a resistor to a network ever increase the effective resistance between two nodes? Why not?
7. Why is the GCN propagation matrix a low-pass graph filter, and what happens to node features if you stack 30 GCN layers?
8. Explain to a smart friend in 3 sentences why the eigenvectors of a graph Laplacian are the "Fourier modes" of that graph.
