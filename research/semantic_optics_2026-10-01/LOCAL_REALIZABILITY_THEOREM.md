# Local Realizability and Scale–Locality Naturality

## A theorem-shaped bridge from local covariance to nested host systems

**Date:** 2026-10-01  
**Status:** formal research note. The naturality theorem is **Disclosed** under its hypotheses. Physical interpretation is **CONJECTURED / source-supported by analogous structures in relativity and locally covariant QFT**.

**Finite witness:** [local_realizability_demo.py](local_realizability_demo.py) · [results](local_realizability_demo_results.json) · [receipt](local_realizability_demo_tests.txt)

---

# 1. Two indexing categories

Let:

\[
\mathsf{Scale}
\]

encode realization/coarse-graining levels.

Let:

\[
\mathsf{Reg}
\]

encode admissible local/causal regions.

A two-axis theory is a functor/pseudofunctor of the schematic form:

\[
\mathcal X:
\mathsf{Scale}^{op}
\times
\mathsf{Reg}^{op}
\to
\mathsf C
\]

for state/configuration restrictions.

Equivalent covariant formulations can be used for observable nets.

---

# 2. Vertical maps

For scale arrow:

\[
n+1\to n,
\]

write:

\[
Q_n^U:
\mathcal X_{n+1}(U)
\to
\mathcal X_n(U).
\]

This is the effective/coarse-graining map inside region \(U\).

---

# 3. Horizontal maps

For:

\[
U\subseteq V,
\]

write:

\[
r_{V,U}^{(n)}:
\mathcal X_n(V)
\to
\mathcal X_n(U).
\]

This is local restriction at scale \(n\).

---

# 4. Naturality theorem

Suppose the family:

\[
Q_n:
\mathcal X_{n+1}
\Rightarrow
\mathcal X_n
\]

is a natural transformation of locality functors.

Then for every inclusion:

\[
U\subseteq V,
\]

the square commutes:

\[
\boxed{
r_{V,U}^{(n)}
\circ
Q_n^V
=
Q_n^U
\circ
r_{V,U}^{(n+1)}.
}
\]

### Proof

This is exactly the naturality condition for \(Q_n\) at the morphism:

\[
U\hookrightarrow V
\]

in the contravariant locality category.

\(\square\)

---

# 5. Interpretation

The theorem says:

\[
\boxed{
\text{localization and effective realization are path-independent}.
}
\]

That is:

> if a lower-level description really is the local effective image of a higher-level system, then it should not matter whether we first form the lower description globally and restrict it, or first restrict the host system and then form the lower description locally.

This is the rigorous version of the user's local-support intuition.

---

# 6. Local-frame covariance as the same pattern

Suppose two overlapping frames/charts:

\[
B,\ C
\]

cover the same region.

Let:

\[
T_{CB}
\]

be the transition map.

For a physical field/object \(\Phi\), local representatives:

\[
\Phi_B,
\quad
\Phi_C
\]

must satisfy:

\[
\boxed{
\Phi_C
=
T_{CB}(\Phi_B)
}
\]

on the overlap.

The numerical components may differ.

The lawful geometric/physical relation agrees.

This is chart/frame covariance.

---

# 7. Lorentz example

For inertial frames in units \(c=1\):

\[
t'
=
\gamma(t-\beta x),
\]

\[
x'
=
\gamma(x-\beta t).
\]

The event coordinates differ.

But:

\[
\boxed{
\Delta s^2
=
\Delta t^2-\Delta x^2
=
\Delta t'^2-\Delta x'^2.
}
\]

So two local frames can assign different scalars/components while preserving the same invariant spacetime structure.

The finite witness checks this on an explicit worldline.

---

# 8. AQFT / locally covariant QFT analogue

A locally covariant QFT is a covariant functor:

\[
\mathcal A:
\mathsf{Loc}
\to
\mathsf{Alg}.
\]

For composable spacetime embeddings:

\[
\psi_1:M\to N,
\qquad
\psi_2:N\to P,
\]

functoriality requires:

\[
\boxed{
\mathcal A(\psi_2\circ\psi_1)
=
\mathcal A(\psi_2)
\circ
\mathcal A(\psi_1).
}
\]

Fields can be natural transformations, giving commuting squares under spacetime embeddings.

This is established physical category-theory prior art for the demand that local representations transport coherently.

Primary source:

Brunetti, Fredenhagen, Verch,  
arXiv:math-ph/0112041.

---

# 9. Local state restriction theorem

Let:

\[
\mathfrak N
\subseteq
\mathfrak A
\]

be a local observable algebra included in a larger algebra.

A global state:

\[
\omega:\mathfrak A\to\mathbb C
\]

restricts to:

\[
\omega_{\mathfrak N}
=
\omega|_{\mathfrak N}.
\]

For every:

\[
A\in\mathfrak N,
\]

local predictions are:

\[
\omega_{\mathfrak N}(A)=\omega(A).
\]

So the local frame carries a mathematically coherent representation of every local observable accessible there.

But two global states can agree locally:

\[
\omega|_{\mathfrak N}
=
\varphi|_{\mathfrak N}
\]

while:

\[
\omega\neq\varphi.
\]

Therefore:

\[
\boxed{
\text{local coherence}
\not\Rightarrow
\text{global uniqueness}.
}
\]

---

# 10. Operational-kernel interpretation

Define:

\[
R_U:
\mathsf{Global}
\to
\mathsf{Local}(U).
\]

If:

\[
R_U(X)=R_U(Y),
\]

then \(X,Y\) lie in one local operational kernel class.

A larger region \(V\supset U\) can act as a lamp if:

\[
R_V(X)\neq R_V(Y).
\]

Thus causal/local enlargement is mathematically the same kind of move as the branch's probe extension:

\[
\boxed{
\text{local kernel collision}
\to
\text{larger-region discriminator}.
}
\]

---

# 11. Contextual/gluing obstruction

Local satisfiability is weaker than global realizability.

A family of local contexts may each admit valid states while no one global assignment satisfies all contexts.

This is the formal shape behind sheaf-theoretic contextuality.

Therefore:

\[
\boxed{
\text{every patch individually coherent}
\not\Rightarrow
\text{one globally coherent hidden assignment}.
}
\]

This blocks a naive move from local realizability to classical global separability.

---

# 12. Finite witness

The included executable tests four distinct structures.

## A. Scale × locality naturality

Rich regional state:

\[
(a,b)
\]

restricts:

\[
(a,b)\mapsto a.
\]

Coarse-graining maps each coordinate to parity.

The square commutes on all:

\[
3\times3=9
\]

states.

A mutant coarse-graining contaminates the local coordinate with outside state:

\[
(a,b)
\mapsto
((a+b)\bmod 2,\ b\bmod2).
\]

The square then fails on:

\[
3/9
\]

states.

This explicitly detects a non-natural “nonlocal contamination.”

## B. Lorentz covariance

Using:

\[
\beta=0.6,
\qquad
\gamma=1.25,
\]

the witness transforms four worldline events.

Coordinate values change.

Inverse transformation returns all points.

Every segment preserves:

\[
\Delta s^2=0.96.
\]

## C. Same local restrictions, different global correlations

Two distinct global binary distributions:

- perfectly correlated;
- perfectly anticorrelated;

both have uniform local marginals:

\[
P(A=0)=P(A=1)=1/2,
\]

and likewise for \(B\).

So local restrictions agree while global structure differs.

## D. Local satisfiability without global section

Three pair contexts impose:

\[
A\neq B,
\qquad
B\neq C,
\qquad
C\neq A.
\]

Every pair context has valid assignments.

No global binary triple satisfies all three.

This is a finite gluing-obstruction shape.

---

# 13. Execution result

\[
\boxed{
8/8\ \text{checks pass}.
}
\]

The witness is construction-level only.

It does not infer physical nonlocality, quantum contextuality, or TLICA truth.

---

# 14. Stronger principle

The branch can now state:

### Scale–Locality Naturality Principle

For a physically adequate family of host/effective descriptions, the effective/coarse-graining transformation should be natural with respect to admissible localization:

\[
\boxed{
R_U\circ Q
\cong
Q_U\circ R_U.
}
\]

### Frame-Overlap Coherence Principle

For local descriptions of the same physical content on overlapping frames:

\[
\boxed{
\text{transport}_{{B\to C}}(\Phi_B)
\cong
\Phi_C.
}
\]

These principles encode:

> the global/higher object may look numerically different locally, but it must be locally lawful and transition-consistent.

---

# 15. Failure meanings

If the scale/locality square fails, at least one of the following is wrong:

1. the lower effective theory;
2. the coarse-graining map;
3. the locality/restriction map;
4. the assumed host realization;
5. the claim that the same physical object/process is being represented.

This gives a real failure-localization tool.

---

# 16. Relationship to Full Yoneda

Full Yoneda applies inside the category chosen at a given scale/locality horizon.

Naturality relates those categories.

So the enlarged program is no longer one Yoneda embedding.

It is a **family of Yoneda embeddings connected by lawful scale/locality functors**.

The deepest future question becomes:

\[
\boxed{
\text{does Yoneda representation commute with the host/locality transports we claim?}
}
\]

That is a serious next theorem target.
