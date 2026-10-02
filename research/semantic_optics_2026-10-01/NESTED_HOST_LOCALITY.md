# Nested Host Systems, Local Reality, and Causal Locality

## Russian-doll realization, quotient layers, local patches, and nonlocal/global structure

**Date:** 2026-10-01  
**Status:** research-tier extension of Semantic Optics. Mathematical statements are typed and conditional; physical generalizations are **CONJECTURED** unless explicitly source-supported. **Foundation untouched.**

---

# 1. The originating picture

For practical local reality, systems often appear as systems realized inside larger systems:

\[
\mathcal C_0
\leftarrow
\mathcal C_1
\leftarrow
\mathcal C_2
\leftarrow
\cdots
\]

But the relation between levels is not always literal set inclusion.

A lower system may be:

- a subobject;
- a local restriction;
- an effective quotient;
- a coarse-graining;
- a realization/interface;
- an open subsystem;
- an emergent macrostate.

So the rigorous replacement for the Russian-doll metaphor is:

\[
\boxed{
\text{tower of structure-preserving realization/coarse-graining maps}.
}
\]

---

# 2. Vertical scale structure

Let:

\[
Q_n:
\mathcal C_{n+1}
\to
\mathcal C_n
\]

map a richer host description to a lower effective description.

Lower dynamics:

\[
F_n:
\mathcal C_n\to\mathcal C_n
\]

are exactly host-realized when:

\[
\boxed{
Q_n\circ F_{n+1}
\cong
F_n\circ Q_n.
}
\]

This says:

> evolve upstairs and coarse-grain = coarse-grain and evolve downstairs.

If this square fails, the proposed lower dynamics are not a faithful realization of the host dynamics on that domain.

---

# 3. Lower systems can be operational quotients

Distinct host processes may collapse:

\[
f\neq g
\]

but:

\[
Q(f)=Q(g).
\]

When \(Q\) satisfies the Operational Quotient Theorem hypotheses:

\[
\boxed{
\mathcal H/\ker Q
\cong
\mathcal L.
}
\]

So a lower “doll” can be a quotient image of the higher one rather than a literal contained copy.

This is exactly the structure already found in the 17/17 reparametrisation bridge.

---

# 4. Horizontal locality structure

Scale is only one axis.

Spacetime/causal locality supplies another.

Let:

\[
\mathsf{Reg}
\]

be a category or poset of admissible local regions.

For:

\[
U\subseteq V,
\]

we need maps relating local descriptions.

There are two common variances.

## Observable-net direction

AQFT uses a covariant assignment:

\[
\mathcal A:
\mathsf{Reg}
\to
\mathsf{Alg},
\]

with isotony:

\[
U\subseteq V
\Rightarrow
\mathcal A(U)
\hookrightarrow
\mathcal A(V).
\]

## State/configuration direction

A global configuration/state restricts contravariantly:

\[
\mathcal X:
\mathsf{Reg}^{op}
\to
\mathsf{State},
\]

with:

\[
r_{V,U}:
\mathcal X(V)
\to
\mathcal X(U).
\]

Both are legitimate; they should not be conflated.

---

# 5. Physical prior art: Haag–Kastler / locally covariant QFT

In algebraic QFT, observables are assigned to spacetime regions.

Haag–Kastler isotony gives:

\[
U\subseteq V
\Rightarrow
\mathcal A(U)\subseteq\mathcal A(V).
\]

Spacelike-separated local observable algebras satisfy locality/microcausality constraints.

Brunetti, Fredenhagen, and Verch generalize this to a **locally covariant quantum field theory**:

\[
\mathcal A:
\mathsf{Loc}
\to
\mathsf{Alg},
\]

a covariant functor from globally hyperbolic spacetimes and admissible embeddings to algebras and injective homomorphisms.

Locally covariant fields are natural transformations.

Primary source:

Romeo Brunetti, Klaus Fredenhagen, Rainer Verch,  
*The generally covariant locality principle — A new paradigm for local quantum physics*,  
arXiv:math-ph/0112041  
https://arxiv.org/abs/math-ph/0112041

This is powerful prior art for the claim:

> the same physical structure must transport coherently through local embeddings/frames.

It does not imply TLICA is QFT.

---

# 6. Local frame coherence

Suppose a physical object/process \(A\) passes through observer \(B\)'s local patch.

Observer \(B\) need not recover the entire global object.

But the part physically represented in that patch must admit a lawful local representation:

\[
A|_{U_B}.
\]

Another frame \(C\) may assign different coordinates/components:

\[
x_B^\mu
\neq
x_C^\mu.
\]

The requirement is not equality of coordinate values.

It is lawful transition:

\[
\boxed{
x_C
=
\Phi_{CB}(x_B)
}
\]

for the same underlying event/field object.

In SR, Lorentz transformations relate coordinates assigned to the same event by inertial frames.

In GR, overlapping coordinate charts are related by smooth transition maps, and tensorial/geometric relations transform covariantly.

So:

\[
\boxed{
\text{same structure}
\neq
\text{same numerical presentation}.
}
\]

---

# 7. Rest mass / energy caution

Frame dependence must be typed correctly.

Modern relativistic language treats invariant/rest mass as invariant.

Quantities such as:

- coordinate time;
- simultaneity;
- three-momentum;
- energy;
- spatial length assigned by a frame;

can differ among observers according to lawful transformations.

So the correct slogan is:

\[
\boxed{
\text{invariant/covariant relations agree;
components and derived frame quantities may differ}.
}
\]

---

# 8. Global state restriction is precise

In algebraic language, a global state:

\[
\omega
\]

on an algebra:

\[
\mathfrak A
\]

restricts to a local subalgebra:

\[
\mathfrak N\subseteq\mathfrak A
\]

by:

\[
\omega_{\mathfrak N}
=
\omega|_{\mathfrak N}.
\]

Thus a global object can have a perfectly coherent local state even when the local state does not reconstruct the whole global state.

Two global states may satisfy:

\[
\omega|_{\mathfrak N}
=
\varphi|_{\mathfrak N}
\]

while:

\[
\omega\neq\varphi.
\]

Then no local observable in \(\mathfrak N\) distinguishes them.

This is the physical analogue of an operational kernel class.

---

# 9. Nonlocal/global structure need not be locally reconstructible

The important asymmetry is:

\[
\boxed{
\text{global object must admit lawful local restrictions}
}
\]

but not:

\[
\boxed{
\text{one local restriction determines the global object}.
}
\]

Global correlations/topology/context may disappear under restriction.

A classical finite example already suffices:

two distinct joint probability distributions can have identical one-variable marginals.

Quantum entanglement gives a stronger physical version, but the general information-theoretic point does not depend on quantum mechanics.

---

# 10. Nonlocality is not one linear nesting chain

Spacelike-separated regions:

\[
U,\ V
\]

may be incomparable:

\[
U\nsubseteq V,
\qquad
V\nsubseteq U.
\]

Relativistic locality therefore suggests:

\[
\boxed{
\text{scale tower}
+
\text{partially ordered causal/locality net}.
}
\]

Not one linear hierarchy.

The “Russian dolls” live vertically across realization scales.

The locality structure branches horizontally across spacetime regions.

---

# 11. Local-to-global gluing

Sheaf theory supplies a second rigorous local/global pattern.

Local data live on contexts/regions:

\[
s_i\in\mathcal F(U_i).
\]

Restriction maps relate overlaps.

Compatible local data may glue to a global section.

But contextual/nonlocal models can exhibit obstructions to global sections.

Abramsky and Brandenburger formalize quantum contextuality/nonlocality in precisely this language:

Samson Abramsky, Adam Brandenburger,  
*The Sheaf-Theoretic Structure of Non-Locality and Contextuality*,  
arXiv:1102.0264  
https://arxiv.org/abs/1102.0264

So “nonlocal” should not automatically mean:

> a broken local law.

It can mean:

> locally valid structures exist, but there is no single global assignment compatible with all contexts.

---

# 12. Quotient versus restriction versus gluing obstruction

These are three different failure modes.

## Quotient

\[
Q(x)=Q(y)
\]

for distinct richer states.

Information is deliberately identified.

## Restriction

\[
X
\mapsto
X|_U.
\]

A global object is viewed only on a region.

## Gluing obstruction

Locally admissible context data do not extend to one global object satisfying all context constraints.

These must remain separate.

---

# 13. The two-axis reality object

The current candidate is a family:

\[
\mathcal X_n(U)
\]

indexed by:

- realization scale \(n\);
- local/causal region \(U\).

So reality is modeled schematically as:

\[
\boxed{
(n,U)
\mapsto
\mathcal X_n(U).
}
\]

Vertical maps change scale:

\[
Q_n^U:
\mathcal X_{n+1}(U)
\to
\mathcal X_n(U).
\]

Horizontal maps restrict locality:

\[
r_{V,U}^{(n)}:
\mathcal X_n(V)
\to
\mathcal X_n(U).
\]

---

# 14. The load-bearing commuting square

The compatibility condition is:

\[
\boxed{
r_{V,U}^{(n)}
\circ
Q_n^V
\cong
Q_n^U
\circ
r_{V,U}^{(n+1)}.
}
\]

Diagrammatically:

\[
\begin{array}{ccc}
\mathcal X_{n+1}(V)
&\xrightarrow{Q_n^V}&
\mathcal X_n(V)
\\
\downarrow r_{V,U}^{(n+1)}
&&
\downarrow r_{V,U}^{(n)}
\\
\mathcal X_{n+1}(U)
&\xrightarrow{Q_n^U}&
\mathcal X_n(U).
\end{array}
\]

Plain language:

> **coarse-grain then localize = localize then coarse-grain.**

This is the mathematically precise version of:

> the higher/nonlocal system has to be supported coherently in the local frame wherever it physically passes through that frame.

---

# 15. Local Realizability Principle

### LRP

For every physically realized process/object at a higher/global level and every admissible local region it traverses, there exists a lawful local restriction, and all overlapping/local frame descriptions transport into agreement under the declared transition structure.

Symbolically:

\[
\boxed{
\text{global realization}
\Rightarrow
\text{coherent local restrictions}.
}
\]

This is **CONJECTURED as a broad physical principle**, while its specific forms are standard in local field/geometry frameworks.

---

# 16. The converse fails

Local coherence alone does not imply a unique global realization.

We can have:

\[
X\neq Y
\]

but:

\[
X|_U=Y|_U
\]

for the current local region.

Or a family of locally satisfiable context constraints with no global solution.

So:

\[
\boxed{
\text{local support}
\not\Rightarrow
\text{global reconstructibility}.
}
\]

This is the exact place where nonlocal/global structure can hide without violating local coherence.

---

# 17. Causal-horizon indexing

For an observer/region \(R\) at time \(t\), define a causally available category:

\[
\mathcal C_{R,t}.
\]

As causal information becomes available:

\[
\mathcal C_{R,t}
\to
\mathcal C_{R,t+\Delta t}.
\]

A model can therefore be complete relative to one causal horizon and later split under new morphisms/probes.

So:

\[
\boxed{
\text{local completeness is horizon-indexed}.
}
\]

This is compatible with Full Yoneda:

full Yoneda is complete relative to the category supplied at that horizon.

---

# 18. Local covariance and Semantic Optics

Semantic Optics supplies:

\[
\Omega_{j,\tau}.
\]

Now index it by region/scale:

\[
\Omega_{j,\tau}^{(n,U)}.
\]

A coherent theory should relate these through transport/restriction maps.

A lower-level optic collapse:

\[
f\sim_Q g
\]

may split:

- at a richer scale;
- in a larger causal region;
- under a new local frame/probe.

Thus lamps come in at least two kinds:

\[
\boxed{
\text{horizontal lamp}
}
\]

(new local/causal evidence)

and:

\[
\boxed{
\text{vertical host lamp}
}
\]

(new higher-level realization structure).

---

# 19. Strongest current synthesis

The best current model is:

\[
\boxed{
\text{Reality}
\approx
\text{realization/coarse-graining tower}
\times
\text{causal/locality net}
}
\]

with gluing/compatibility constraints.

Not every global distinction is locally visible.

But wherever a global process intersects a local patch, the local representation must be lawful relative to the global structure.

That is the serious version of:

> the nonlocal system is still supported in the local frame.

---

# 20. Boundaries

This note does **not** establish:

- that all ontology forms one literal nested set hierarchy;
- that every effective theory is an exact quotient;
- that every local theory uniquely reconstructs its host;
- that quantum nonlocality reduces to ordinary causal propagation;
- that contextuality is merely missing information;
- that TLICA is a physical field theory;
- that every scale/locality square commutes exactly in nature;
- that SR/GR proves the Semantic Optics program.

The contribution is the structural synthesis and the explicit theorem/probe targets.
