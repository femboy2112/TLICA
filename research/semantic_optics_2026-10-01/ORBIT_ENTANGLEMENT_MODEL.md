# Orbit Entanglement from Transported Copies

## What the copy-groupoid picture does — and does not — buy in quantum mechanics

**Date:** 2026-10-01  
**Status:** finite-dimensional quantum construction + categorical prior-art bridge. **No claim that this is the fundamental mechanism of physical entanglement.**

---

# 1. Critical firewall

A family of isomorphic copies with Yoneda transport is **not entanglement**.

Yoneda supplies:

\[
\boxed{
\text{relational transport}.
}
\]

Quantum entanglement additionally requires:

- a monoidal/tensor product;
- linear superposition;
- a state that does not factor as a simple tensor.

So:

\[
\boxed{
\text{Yoneda transport}
\neq
\text{quantum entanglement}.
}
\]

The copy-groupoid structure can, however, supply a natural **index/orbit architecture** on which entangled states are built.

---

# 2. Represent the transport groupoid on Hilbert spaces

Let:

\[
\mathcal G
\]

be the copy/transport groupoid.

A unitary representation is a functor:

\[
\boxed{
U:
\mathcal G
\to
\mathbf{Hilb}_{\mathrm{unitary}}.
}
\]

Every copy \(a\) gets a Hilbert space:

\[
H_a.
\]

Every transport form:

\[
g:a\to b
\]

gets a unitary:

\[
U_g:H_a\to H_b.
\]

Thus categorical copy transport becomes physically admissible reversible linear transport.

---

# 3. Group-orbit version

Take one Hilbert space:

\[
H
\]

and a unitary representation:

\[
U:G\to U(H).
\]

Choose a seed state:

\[
|\psi\rangle\in H.
\]

Its transformed copies form the orbit:

\[
\boxed{
|\psi_g\rangle
=
U_g|\psi\rangle.
}
\]

This is the cleanest mathematical version of:

> shifted/morphed copies of one state.

---

# 4. Coherent orbit-index state

Let the index/control Hilbert space be:

\[
\ell^2(G)
\]

for finite/countable \(G\).

Choose:

\[
\alpha=(\alpha_g)_{g\in G},
\qquad
\sum_g|\alpha_g|^2=1.
\]

Define:

\[
\boxed{
|\Psi_{\alpha,\psi}\rangle
=
\sum_{g\in G}
\alpha_g
|g\rangle
\otimes
U_g|\psi\rangle.
}
\]

This state correlates the copy index with a transformed copy of the same seed.

This is a precise realization of:

> “what it is entangled with is shifted/morphed copies of itself.”

Again, this is a **construction**, not a derivation of nature's entanglement mechanism.

---

# 5. Exact separability criterion

Consider:

\[
|\Psi\rangle
=
\sum_i
\alpha_i
|i\rangle\otimes|\psi_i\rangle.
\]

The Schmidt rank equals the dimension of the span of the nonzero branch vectors:

\[
\boxed{
\operatorname{SchmidtRank}(\Psi)
=
\dim
\operatorname{span}
\{
|\psi_i\rangle:
\alpha_i\neq0
\}.
}
\]

Therefore:

\[
\boxed{
|\Psi\rangle
\text{ is separable}
\iff
\text{all active }|\psi_i\rangle
\text{ are collinear}.
}
\]

Applied to the orbit state:

\[
\boxed{
\text{orbit-index entanglement}
\iff
\{U_g|\psi\rangle:\alpha_g\neq0\}
\text{ spans dimension }>1.
}
\]

This is an exact finite/countable Hilbert-space statement.

---

# 6. Regular representation: “the transformations act on themselves”

This is the strongest match to the author's “applied to itself” language.

Let:

\[
H=\ell^2(G)
\]

with basis:

\[
\{|h\rangle:h\in G\}.
\]

Use the left regular representation:

\[
L_g|h\rangle
=
|gh\rangle.
\]

Choose the identity seed:

\[
|e\rangle.
\]

Then:

\[
L_g|e\rangle
=
|g\rangle.
\]

So:

\[
\boxed{
|\Psi_\alpha\rangle
=
\sum_g
\alpha_g
|g\rangle\otimes L_g|e\rangle
=
\sum_g
\alpha_g
|g\rangle\otimes|g\rangle.
}
\]

The transformation index acts on a basis indexed by the transformation structure itself.

This is almost literally:

> the basis entangled with shifted copies of itself applied to itself.

---

# 7. Finite-group maximally entangled case

For finite:

\[
|G|=n
\]

and uniform amplitudes:

\[
\alpha_g
=
\frac1{\sqrt n},
\]

we obtain:

\[
\boxed{
|\Phi_G\rangle
=
\frac1{\sqrt n}
\sum_{g\in G}
|g\rangle\otimes|g\rangle.
}
\]

This is maximally entangled between the two:

\[
n
\]

dimensional factors.

The reduced density matrix is:

\[
\boxed{
\rho
=
\frac1n I.
}
\]

Thus group-self-action provides an exact canonical entangled construction.

---

# 8. Infinite countable warning

For infinite countable \(G\), the formal uniform state:

\[
\sum_g|g,g\rangle
\]

is not normalizable.

Instead require:

\[
\alpha\in\ell^2(G).
\]

Then:

\[
\sum_g|\alpha_g|^2=1.
\]

So an actual Hilbert state exists only after choosing square-summable amplitudes.

This is a load-bearing correction to any naive “uniform entanglement over infinitely many \(N[i]\)” picture.

---

# 9. Why \(\mathbb Z\) is a cleaner shift basis than \(\mathbb N\)

The bilateral shift:

\[
L_k|n\rangle
=
|n+k\rangle
\]

on:

\[
\ell^2(\mathbb Z)
\]

is unitary.

The unilateral positive shift on:

\[
\ell^2(\mathbb N)
\]

is an isometry but not onto, hence not unitary.

Therefore if the intuition specifically requires **reversible quantum shifts**:

\[
\boxed{
\mathbb Z
}
\]

is structurally cleaner than:

\[
\mathbb N.
\]

If it requires recursive branching/copying instead,:

\[
\mathbb N^{<\omega}
\]

is cleaner.

There may not be one universal “fundamental basis.”

---

# 10. Categorical quantum mechanics prior art

Abramsky–Coecke categorical quantum mechanics places quantum protocols in compact/monoidal categorical structure, where:

- tensor product is fundamental;
- entangled states are morphisms involving composite systems;
- cups/caps and compact closure express information flow.

Primary source:

Samson Abramsky, Bob Coecke,  
*A categorical semantics of quantum protocols*, arXiv:quant-ph/0402130.

This provides the correct warning:

> if the copy-groupoid model is to touch real quantum structure, it eventually has to enter a monoidal/dagger/compact setting.

Groupoids/Yoneda alone are insufficient.

---

# 11. Projective form transport

Quantum symmetries can be represented only up to phase.

A projective unitary representation satisfies:

\[
\boxed{
U_gU_h
=
\omega(g,h)
U_{gh}
}
\]

with:

\[
\omega(g,h)\in U(1).
\]

Associativity requires the 2-cocycle law:

\[
\boxed{
\omega(g,h)\omega(gh,k)
=
\omega(h,k)\omega(g,hk).
}
\]

Thus strict form composition:

\[
T_hT_g=T_{hg}
\]

can weaken quantum-mechanically to:

\[
\boxed{
T_hT_g
=
\text{phase}\times T_{hg}.
}
\]

This is not a defect in physical ray space; overall phases represent the same ray.

Prior art:
- Wigner/projective quantum symmetry;
- projective representations classified by group 2-cocycles / central extensions.

---

# 12. Pauli example

Let:

\[
G=\mathbb Z_2\times\mathbb Z_2.
\]

Choose:

\[
U_{(a,b)}
=
X^aZ^b.
\]

Because:

\[
ZX=-XZ,
\]

composition is:

\[
\boxed{
U_{(a,b)}
U_{(c,d)}
=
(-1)^{bc}
U_{(a+c,b+d)}
}
\]

with addition mod \(2\).

The phase:

\[
\omega((a,b),(c,d))
=
(-1)^{bc}
\]

obeys the 2-cocycle condition.

So even the elementary Pauli system gives a concrete example where forms compose projectively rather than strictly.

This may be highly relevant if the copy-transport intuition is meant to touch quantum phase.

---

# 13. Flat versus projective copy atlases

We can now distinguish:

## Strict copy transport

\[
T_{ca}
=
T_{cb}T_{ba}.
\]

## Projective quantum transport

\[
T_{ca}
\sim
T_{cb}T_{ba}
\]

up to:

\[
U(1)
\]

phase.

The phase data form a cocycle.

If the cocycle is cohomologically trivial, phases can be removed by rephasing the forms.

If not, one must pass to a central extension or retain genuinely projective transport.

This is a much sharper notion of “connect the forms.”

---

# 14. What entanglement adds to Yoneda

Yoneda can tell us that:

\[
X_a
\cong
X_b
\]

through complete probe transport.

Quantum monoidal structure lets us form:

\[
X_a\otimes X_b.
\]

Superposition allows states that are not products.

Therefore the architecture is:

\[
\boxed{
\text{copy/action groupoid}
\xrightarrow{\text{unitary representation}}
\text{Hilbert fibers}
\xrightarrow{\otimes+\text{superposition}}
\text{possible entanglement}.
}
\]

Entanglement lives **after** the transport layer, not inside Yoneda itself.

---

# 15. A serious moonshot

A mathematically coherent research hypothesis is now:

> Some physically useful entangled-state families may be organized as coherent superpositions over the orbit of a seed object/state under a self-similar or groupoid transport structure.

Symbolically:

\[
\boxed{
|\Psi\rangle
=
\sum_g
\alpha_g
|g\rangle
\otimes
U_g|\psi\rangle.
}
\]

Questions:

1. Does a self-similar/wreath-recursive action give a useful hierarchy of orbit states?
2. Do projective cocycles correspond to physically meaningful phase/holonomy data?
3. Does any of this explain entanglement more economically than ordinary tensor-product representation theory?
4. Are there experimental/standard quantum systems naturally presented this way?

Until those questions succeed, this remains a **representation program**, not a fundamental theory.

---

# 16. Current verdict

The quantum intuition did not collapse, but it split into exact layers:

\[
\boxed{
\text{self-similar copy basis}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{transport/action groupoid}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{unitary/projective representation}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{tensor product + coherent orbit superposition}
}
\]

\[
\downarrow
\]

\[
\boxed{
\text{entanglement when orbit branches are linearly independent}.
}
\]

This is currently the strongest honest bridge between the author's intuition and actual quantum mathematics.
