# Topology and Geometry

## Why This Section Matters

Topology studies the properties of spaces that are preserved under continuous deformation — it's the mathematics of shape, connectivity, and holes. Differential geometry extends this to curved spaces with notions of distance, curvature, and parallel transport. In physics, general relativity is differential geometry; in data science, topological data analysis (TDA) reveals the shape of high-dimensional datasets; in ML, manifold learning assumes data lives on low-dimensional manifolds in high-dimensional space. Riemannian geometry provides the foundation for optimization on manifolds and geometric deep learning.

---

## Prerequisites

- Section 00 (Mathematical Thinking) — proof maturity
- Section 01 (Linear Algebra) — inner products, orthogonality
- Section 02 (Calculus) — multivariable calculus, analysis basics

---

## 🎯 Learning Objectives

After this section you can:
- Work directly from the axioms of a topology — open sets, bases, continuity, homeomorphism, separation axioms — including exhaustive computation on finite spaces.
- Prove the core point-set theorems on compactness and connectedness, and use them as invariants to show two spaces are not homeomorphic.
- Compute Gaussian curvature extrinsically and from angle excess, and explain the Theorema Egregium and Gauss–Bonnet, including the discrete angle-defect version on triangle meshes.
- Compute persistent homology of point clouds and time-delay embeddings, read Betti numbers off barcodes, and judge when a "topological feature" is real.
- Compute geodesics on a curved surface by integrating the geodesic equation, and verify them against a conserved quantity.

---

## Resources

| Priority | Type | Resource | Author(s) | Year | Link | Description |
|----------|------|----------|------------|------|------|-------------|
| 🔑 | Book | Visual Differential Geometry and Forms | Tristan Needham | 2021 | — | A revolutionary visual approach to differential geometry. Needham makes curvature, geodesics, and forms intuitive through geometric reasoning rather than coordinate computations. Beautiful and deep. |
| | Book | Topology | James Munkres | 2000 | — | The standard introduction to point-set topology. Covers topological spaces, continuity, compactness, connectedness, and the fundamental group. Rigorous and well-written. |
| | Book (Free) | Topology Without Tears | Sidney Morris | — | [Link](https://www.topologywithouttears.net/) | Free, accessible introduction to topology. Good for building intuition before Munkres. |
| | Book | Introduction to Smooth Manifolds | John Lee | 2012 | — | The standard graduate text on smooth manifolds. Covers tangent spaces, differential forms, de Rham cohomology, and Lie groups. Thorough and rigorous. |
| | Course (Free) | Algebraic Topology | Pierre Albin | — | [Link](https://www.youtube.com/playlist?list=PLpRLWqLFLVTCL15U6N3o35g4uhMSBVA2b) | Lecture series covering fundamental groups, covering spaces, and homology. Good visual approach to algebraic topology. |
| | Book | Riemannian Geometry | Manfredo do Carmo | 1992 | — | Classic introduction to Riemannian geometry: geodesics, curvature, Gauss-Bonnet theorem. Foundation for understanding optimization on manifolds. |
| | Book | Computational Topology: An Introduction | Herbert Edelsbrunner, John Harer | 2010 | — | Introduction to topological data analysis (TDA): simplicial complexes, persistent homology, and Betti numbers. Connects topology to data science. |
| | Video Series | Topology & Geometry | Tadashi Tokieda | — | [Link](https://www.youtube.com/playlist?list=PLTBqohhFNBE_09L0i-lf3fYXF5woAbrzJ) | Charming, intuitive lectures on topology and geometry by an exceptional communicator. Great for building visual intuition. |
| | Paper | Topology and Data | Gunnar Carlsson | 2009 | [Link](https://doi.org/10.1090/S0273-0979-09-01249-X) | Survey paper on topological data analysis (TDA), *Bulletin of the AMS*. Connects persistent homology to practical data analysis. Bridge from theory to applications. |

---

## Suggested Order

1. **Tokieda — Topology & Geometry lectures** — Start with intuitive visual understanding.
2. **Morris — Topology Without Tears** — Build basic topological vocabulary (open sets, continuity, compactness).
3. **Munkres — Topology** — The core text for point-set topology. Focus on Part I first.
4. **Needham — Visual Differential Geometry** — The heart of this section. Builds geometric understanding of curvature and forms.
5. **Lee — Smooth Manifolds** — For rigorous treatment of manifolds when ready.
6. **do Carmo — Riemannian Geometry** — Study curvature, geodesics, and the geometry of curved spaces.
7. **Edelsbrunner & Harer** or **Carlsson — "Topology and Data"** — For topological data analysis applications.

---

## 🛠️ Practice

1. **Finite topologies by brute force** — Enumerate every topology on a 3-point set by checking the axioms over all families of subsets: you should find 29, falling into 9 homeomorphism classes. Repeat for 4 points (355 topologies, 33 classes). For each 3-point class, decide whether it is T₀, T₁, Hausdorff, and connected; then prove that every finite T₁ space is discrete. *(~3 h · Morris, Topology Without Tears — topological spaces and separation; Munkres Ch. 2)*
2. **Point-set proof set** — Prove: (a) a continuous image of a compact space is compact; (b) a continuous image of a connected space is connected; (c) [0, 1] is compact (Heine–Borel via the "sup of the good points" argument); (d) a continuous bijection from a compact space to a Hausdorff space is a homeomorphism — and show by counterexamples that both hypotheses are needed; (e) ℝ is not homeomorphic to ℝ², and [0, 1) is not homeomorphic to the circle S¹ (remove a point). Optional Lean 4: prove (a) from Mathlib's open-cover characterization of compactness, then compare with the library's own proof (find it with `exact?`). *(~6 h · Munkres Ch. 2–3; Morris; Tokieda's lectures for intuition)*
3. **Curvature you can touch** — (a) For a graph surface z = f(x, y), derive K = (f_xx·f_yy − f_xy²)/(1 + f_x² + f_y²)², and check K = 1/R² on a spherical cap and K < 0 for z = x² − y². (b) On a melon or gourd, lay narrow strips of masking tape (a strip that lies flat without wrinkling follows a geodesic) to form geodesic triangles of several sizes; measure their angle sums with a protractor and estimate K from excess ÷ area; compare with 1/(R₁R₂) from principal radii you measure with calipers or string. (c) Use the Theorema Egregium to explain why a cylinder has K = 0 and why folding a pizza slice along its length keeps the tip from drooping. *(~4 h · Needham, Visual Differential Geometry and Forms — curvature, angular excess, and the Theorema Egregium; Tokieda's lectures)*
4. **Persistent homology of signals** — With `ripser` (or GUDHI), compute barcodes for: a noisy circle (n = 300); a flat torus sampled in ℝ⁴ as (cos a, sin a, cos b, sin b); and sliding-window (time-delay) embeddings of (i) a sine, (ii) a two-tone signal with incommensurate frequencies, and (iii) white noise. Read β₀, β₁ (and β₂ for the torus) off the long bars. Then add increasing noise and show that the bottleneck distance between diagrams stays within the bound the stability theorem gives. Finish with a paragraph on exactly what a long bar does and doesn't tell you about a signal. *(~5 h · Edelsbrunner & Harer — simplicial complexes, persistence, and stability; Carlsson's survey "Topology and Data"; Albin's algebraic-topology lectures for homology)*
5. **Geodesics by ODE** — For a torus of revolution (tube radius 1, center-circle radius 2), derive the metric and Christoffel symbols, integrate the geodesic equations with `solve_ivp`, and verify Clairaut's relation (ρ·cos ψ is constant along a geodesic, where ρ is the distance from the axis and ψ the angle with the parallel) to 10⁻⁸. Find geodesics that oscillate around the outer equator and ones that wind over the top, and explain the difference with Clairaut. Sanity-check the same code on a sphere, where every geodesic must be a great circle. *(~4 h · do Carmo, Riemannian Geometry — geodesics and Christoffel symbols; Lee, Introduction to Smooth Manifolds, for the formalism)*

**🏗️ Mini-project — Discrete curvature and Gauss–Bonnet on real meshes:** Write a small library that, for a closed triangle mesh (STL/OBJ — an icosphere, a torus, and a 3D-scanned or CAD part such as an enclosure), computes V − E + F and the genus, the angle defect (discrete Gaussian curvature) at every vertex, and the total. Verify that the defects sum to 2πχ to ~10⁻⁹ on every closed mesh — exactly 4π for any sphere-like mesh and 0 for a torus — show that defect ÷ vertex area converges to 1/R² on refined spheres (report the observed rate), and render the curvature field on the scanned part. Optional: mean curvature via the cotangent Laplacian. Draws on Needham's treatment of Gauss–Bonnet and on Lee and do Carmo for the smooth theorem. Deliverable: `projects/math/09-discrete-curvature/` with code, a validation table, and renders. Success: discrete Gauss–Bonnet holds to rounding on every closed mesh, convergence is demonstrated with a measured rate, and a paragraph explains why the total is a topological invariant while the pointwise values are not. *(~10 h)*

## ✅ Check Yourself

Answer from memory first, then check against the sources — or paste this section into NotebookLM and ask it to quiz you.

1. Define a topology, and continuity in terms of open sets. Why is that equivalent to the ε–δ definition on ℝ?
2. State the Heine–Borel theorem. Why does "closed and bounded ⇒ compact" fail in an infinite-dimensional normed space?
3. Prove in two sentences that a circle is not homeomorphic to an interval.
4. What does the Theorema Egregium say, and why does it mean you can't flatten an orange peel without tearing or stretching it?
5. By Gauss–Bonnet, what is the total Gaussian curvature of any closed surface homeomorphic to a torus? To a sphere?
6. Estimate: a geodesic triangle has vertices at the North Pole and at two points on the equator 90° apart in longitude. What is its angle sum, and does that agree with Gauss–Bonnet given the triangle's area?
7. Misconception: "persistent homology finds the holes in my data." What do the bars actually depend on (metric, filtration, sampling), and how can a long bar mislead?
8. Explain to a smart friend in 3 sentences what intrinsic curvature is.
