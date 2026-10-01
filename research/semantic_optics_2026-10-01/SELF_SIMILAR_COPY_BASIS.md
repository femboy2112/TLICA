# Self-Similar Copy Basis

## From \(\mathbb N\) to a countable recursive carrier with exact copy transport

**Date:** 2026-10-01  
**Status:** mathematical construction + prior-art bridge. Quantum interpretation remains **CONJECTURED**.

---

# 1. Bare ordered \(\mathbb N\) is too rigid

If the proposed “lexicographic-like form” is required to be an order automorphism of:

\[
(\mathbb N,<),
\]

there is only one:

\[
\boxed{\operatorname{Aut}(\mathbb N,<)=\{1\}.}
\]

Proof:

- the least element \(0\) must map to \(0\);
- if \(0,\ldots,n-1\) are fixed, then \(n\) is the least element larger than all of them, so it is fixed;
- induction fixes every natural number.

So nontrivial transformed copies require **more structure than the ordinary well-order on \(\mathbb N\)**.

This is a useful falsifier: if the theory insists on literal order-preserving automorphisms of standard \(\mathbb N\), the moonshot collapses to the identity.

---

# 2. Minimal countable self-similar replacement

Let:

\[
\boxed{
X=\mathbb N^{<\omega}
}
\]

be the set of all finite words of natural numbers.

This is countable:

\[
|X|=\aleph_0.
\]

So as a bare set:

\[
X\cong\mathbb N.
\]

But unlike bare \(\mathbb N\), \(X\) carries a rooted-tree/free-monoid structure.

For every:

\[
i\in\mathbb N,
\]

define the prefix cylinder:

\[
X_i
=
iX
=
\{iw:w\in X\}.
\]

Define:

\[
p_i:
X\to X_i,
\qquad
w\mapsto iw.
\]

Then \(p_i\) is a bijection with inverse “strip the initial \(i\).”

Therefore:

\[
\boxed{
X_i\cong X
\qquad
\forall i\in\mathbb N.
}
\]

This is almost literally the author's:

\[
N[0]=N,
\quad
N[i]=\text{transformed copy of }N.
\]

The important change is that the copied object is the **structured countable carrier** \(X\), not the rigid well-order \((\mathbb N,<)\).

---

# 3. Lexicographic interpretation

Equip finite words with a declared lexicographic/dictionary order.

Since every pair in a fixed prefix cylinder shares the prefix \(i\):

\[
u<v
\iff
iu<iv.
\]

Thus:

\[
p_i:w\mapsto iw
\]

is lexicographic-form preserving within each cylinder.

The transformation is therefore legitimately “lexicographic-esque” without pretending that standard \(\mathbb N\)'s well-order has nontrivial automorphisms.

---

# 4. Canonical copy transport

For two copy indices:

\[
a,b\in\mathbb N,
\]

define:

\[
\boxed{
\tau_{b\leftarrow a}
=
p_b\circ p_a^{-1}:
X_a\to X_b.
}
\]

Explicitly:

\[
\tau_{b\leftarrow a}(aw)=bw.
\]

Then:

\[
\tau_{a\leftarrow a}=1_{X_a},
\]

\[
\tau_{a\leftarrow b}
=
\tau_{b\leftarrow a}^{-1},
\]

and:

\[
\boxed{
\tau_{c\leftarrow b}
\circ
\tau_{b\leftarrow a}
=
\tau_{c\leftarrow a}.
}
\]

So the pure-copy system is a **pair groupoid**: one unique canonical transport arrow between every pair of copies.

This is the simplest exact answer to:

> “There must be a way to connect the forms.”

---

# 5. Add morphology

The canonical copy map only changes the prefix label.

To model genuine “morphing,” choose a group:

\[
G\le\operatorname{Aut}(X)
\]

of structure-preserving transformations.

Define:

\[
\boxed{
T_{b\leftarrow a}^{g}
=
p_b\circ g\circ p_a^{-1}.
}
\]

Then:

\[
T_{b\leftarrow a}^{g}:
X_a\to X_b.
\]

Composition is:

\[
T_{c\leftarrow b}^{h}
\circ
T_{b\leftarrow a}^{g}
=
T_{c\leftarrow a}^{hg}.
\]

And:

\[
\left(
T_{b\leftarrow a}^{g}
\right)^{-1}
=
T_{a\leftarrow b}^{g^{-1}}.
\]

Therefore:

\[
\boxed{
\operatorname{Hom}(X_a,X_b)
\cong
G.
}
\]

This is already extremely close to the author's sentence:

> “Yoneda transport lives in the spaces between \(N[a]\) and \(N[b]\).”

The “space between” is literally a hom-set/group of forms.

---

# 6. Action-groupoid / torsor formulation

More generally let a group \(G\) act on a family of copies \(P\).

The action groupoid:

\[
P\sslash G
\]

has:

- objects: copies \(p\in P\);
- arrows \(p\to q\): group elements \(g\) with:
  \[
  gp=q.
  \]

If the action is free and transitive, \(P\) is a \(G\)-torsor.

Then between any two copies there is a unique transformation \(g\).

This gives a coordinate-free version of “all copies are the same object seen through different forms.”

Prior art:
- action groupoid:
  https://ncatlab.org/nlab/show/action+groupoid
- torsors/principal homogeneous spaces:
  Stacks Project, Groupoid Schemes and torsors.

---

# 7. Self-similarity / wreath recursion

The author's phrase:

> “shifted/morphed copies of itself applied to itself”

has an unusually close established analogue in **self-similar group actions on rooted trees**.

For an alphabet \(A\), let:

\[
A^\*
\]

be the rooted tree of finite words.

For:

\[
g\in\operatorname{Aut}(A^\*),
\]

there is:

- a permutation:
  \[
  \sigma_g\in\operatorname{Sym}(A)
  \]
  of the first level;
- for every \(a\in A\), a **section**:
  \[
  g|_a
  \]
  describing the induced action on the subtree \(aA^\*\), after identifying that subtree with the whole tree.

One writes:

\[
\boxed{
g(aw)
=
\sigma_g(a)\,
g|_a(w).
}
\]

For a self-similar group:

\[
g|_a\in G
\]

again.

Thus the action recursively contains transformed copies of **the same action class** inside every copy of the base tree.

This is encoded by **wreath recursion**:

\[
\boxed{
G
\longrightarrow
\operatorname{Sym}(A)\wr G.
}
\]

Primary prior art:
- Grigorchuk/Nekrashevych self-similar groups;
- standard rooted-tree automorphism decomposition.

This is currently the strongest mathematical realization of the recursive-copy portion of the author's intuition.

---

# 8. Why this is stronger than a list of copies

A bare family:

\[
\{X_i\}_{i\in\mathbb N}
\]

only says “many isomorphic objects exist.”

Self-similarity says something stronger:

> the way the global form acts on a copy is itself encoded by another form of the same kind.

So:

\[
\boxed{
\text{copy structure}
+
\text{closed recursive form structure}.
}
\]

That is a candidate mathematical meaning of:

> “copies of itself applied to itself.”

---

# 9. Cocycle connection between chosen forms

Suppose we choose one transition form:

\[
g_{ba}
\]

between every ordered pair of copies.

For flat/path-independent transport we require:

\[
g_{aa}=e,
\]

\[
g_{ab}=g_{ba}^{-1},
\]

and:

\[
\boxed{
g_{ca}
=
g_{cb}g_{ba}.
}
\]

This is exactly the transition-function/cocycle law familiar from bundles and torsors.

Thus the forms are not merely pairwise maps.

They are globally connected by a composition constraint.

If this equation fails, the defect records **holonomy/path dependence** rather than one coherent flat copy atlas.

---

# 10. Yoneda transport on the copy groupoid

For any form:

\[
T:X_a\to X_b,
\]

Yoneda gives:

\[
y(T):
\operatorname{Hom}(-,X_a)
\Rightarrow
\operatorname{Hom}(-,X_b).
\]

At probe \(C\):

\[
f:C\to X_a
\mapsto
T\circ f:C\to X_b.
\]

Since every \(T_{b\leftarrow a}^{g}\) is invertible:

\[
y(T)
\]

is a natural isomorphism.

Thus each copy has the same full Yoneda relational profile, transported by the chosen form.

So:

\[
\boxed{
\text{copy equivalence}
=
\text{invertible complete-probe transport}.
}
\]

---

# 11. Underlying \(\mathbb N\) can be retained by coding

Because:

\[
\mathbb N^{<\omega}
\cong
\mathbb N
\]

as sets, choose a coding bijection:

\[
\kappa:
\mathbb N^{<\omega}
\overset{\sim}{\to}
\mathbb N.
\]

Every tree form:

\[
g:X\to X
\]

can be transported to:

\[
\widetilde g
=
\kappa g\kappa^{-1}:
\mathbb N\to\mathbb N.
\]

Therefore one can literally keep the underlying carrier \(\mathbb N\).

But the load-bearing object is no longer the standard order on \(\mathbb N\).

It is:

\[
\boxed{
(\mathbb N,\text{transported rooted-tree/self-similar structure}).
}
\]

This distinction matters.

---

# 12. Current candidate “irreducible basis”

The research should not prematurely select:

\[
\mathbb N,
\mathbb Z,
\mathbb Q
\]

as the fundamental object.

The current strongest abstract datum is:

\[
\boxed{
(X,G\curvearrowright X)
}
\]

or recursively:

\[
\boxed{
(X^\*,G\le\operatorname{Aut}(X^\*))
}
\]

with:

- carrier/basis \(X\);
- family of copies/fibers;
- transformation law \(G\);
- cocycle/transport composition;
- optional self-similar closure.

The **action law**, not the bare carrier, is what creates the relational structure.

---

# 13. \(\mathbb N\) versus \(\mathbb Z\)

A further structural warning:

Additive translation on:

\[
\mathbb N
\]

by positive \(k\):

\[
n\mapsto n+k
\]

is injective but not surjective.

So it cannot provide reversible groupoid transport.

The group completion:

\[
\boxed{
\mathbb Z
}
\]

supports bilateral translations:

\[
n\mapsto n+k
\]

with inverse:

\[
n\mapsto n-k.
\]

Therefore:

- \(\mathbb N\) is natural for **monoid/index/tree growth**;
- \(\mathbb Z\) is natural for **invertible shift transport**.

This may become important when the quantum/unitary layer is added.

---

# 14. Current verdict

The closest rigorous skeleton of the author's copy intuition is:

\[
\boxed{
\text{countable self-similar carrier}
+
\text{action/transport groupoid}
+
\text{wreath-recursive form algebra}.
}
\]

The closest minimal countable carrier is:

\[
\boxed{
\mathbb N^{<\omega}.
}
\]

The spaces between copies are:

\[
\boxed{
\operatorname{Hom}(X_a,X_b)
}
\]

and the forms are connected by group/groupoid composition and cocycle laws.

This entire structure exists before quantum mechanics enters.
