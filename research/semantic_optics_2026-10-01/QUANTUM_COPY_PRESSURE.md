# Quantum Copy-Transport Pressure Test

## Which parts are real mathematics, which parts are quantum, and where the idea can fail

**Date:** 2026-10-01  
**Status:** adversarial research note. **No fundamental-physics claim.**

> **Direction correction:** the copy/self-similar constructions are now evaluated as candidate **N-side presentations of empirically anchored quantum structure**, not as a bottom-up derivation of quantum mechanics. The host-reflection criterion is primary. See [EMPIRICAL_QM_HOST_REFLECTION.md](EMPIRICAL_QM_HOST_REFLECTION.md).

---

# 1. Candidate-basis comparison

| Candidate | Copy/self-similarity | Invertible shifts | Quantum/unitary friendliness | Main issue |
|---|---:|---:|---:|---|
| \((\mathbb N,<)\) | poor | no | poor | order-rigid |
| \((\mathbb N,+)\) | moderate monoid | no | unilateral isometries | no inverses |
| \(\mathbb Z\) | moderate | excellent | excellent regular unitary shifts | no recursive branching |
| \(\mathbb Q\) | rich arithmetic | excellent additive | good | copy intuition not canonical |
| \(\mathbb N^{<\omega}\) | excellent | via automorphism group | representation-dependent | tree structure added |
| \(G\) acting on itself | excellent orbit structure | excellent | regular representation canonical | requires choosing \(G\) |
| self-similar \(G\curvearrowright A^\*\) | excellent recursive | excellent | operator-algebra route exists | strongest but most structured assumption |

### Current verdict

The “fundamental basis” is unlikely to be a bare set.

The minimally meaningful datum is closer to:

\[
\boxed{
(X,G\curvearrowright X).
}
\]

The transformation law is as important as the carrier.

---

# 2. What survives the pressure test

### Survives exactly

- infinitely many isomorphic copies;
- exact forms between copies;
- groupoid composition;
- Yoneda transport;
- recursive self-similar forms;
- linearization into operator algebras;
- orbit-superposition entangled states;
- projective phase cocycles.

### Does not survive as stated

- nontrivial lexicographic automorphisms of standard \((\mathbb N,<)\);
- “Yoneda itself is entanglement”;
- uniform normalized entanglement over countably infinite copies;
- automatic identification of self-similar operator algebras with physical quantum observables.

---

# 3. Fundamental-basis warning

The phrase:

> “irreducible mathematical basis”

must be indexed to a category/structure.

Examples:

- \(\mathbb N\) is initial among semirings in one sense;
- \(\mathbb Z\) is the group completion of \(\mathbb N\);
- free monoids/trees are initial for word-building operations;
- group regular representations are canonical once a group is chosen.

There is no current theorem selecting one of these as “fundamental proper.”

So the research should ask:

\[
\boxed{
\text{which universal property is required?}
}
\]

before selecting a basis.

---

# 4. The self-similar carrier is unusually close

\[
X=\mathbb N^{<\omega}
\]

has four desirable properties:

1. countable:
   \[
   X\cong\mathbb N;
   \]
2. recursively self-similar:
   every prefix subtree is a copy of \(X\);
3. supports nontrivial automorphisms;
4. supports wreath-recursive actions.

This is currently the best direct model of the author's \(N[i]\) family.

---

# 5. The group-action carrier is unusually close to the quantum side

For a group \(G\):

\[
H=\ell^2(G)
\]

has canonical basis:

\[
|g\rangle.
\]

The left regular action:

\[
L_h|g\rangle
=
|hg\rangle
\]

is unitary.

So \(G\) simultaneously labels:

- transformations;
- basis states;
- transformed copies.

The canonical orbit state:

\[
\sum_g\alpha_g
|g\rangle\otimes|g\rangle
\]

then directly realizes the “self applied to itself” picture.

This is the strongest current quantum-compatible candidate.

---

# 6. Recursive and quantum candidates need not be the same object

One possibility is:

\[
\boxed{
\text{recursive carrier }X=A^\*
}
\]

with symmetry group:

\[
G\le\operatorname{Aut}(A^\*),
\]

then quantize/represent \(G\) on:

\[
\ell^2(G)
\]

or on a Hilbert space built from the tree boundary.

So the basis may be a **stack of structures**, not one set:

\[
A^\*
\leftarrow
G
\leftarrow
\mathbb C[G]
\leftarrow
\text{Hilbert representation}.
\]

This is more plausible than demanding one magic \(\mathbb N\) object do everything.

---

# 7. Actual entanglement test

Any claimed quantum realization must exhibit:

\[
|\Psi\rangle
\in
H_A\otimes H_B
\]

with Schmidt rank:

\[
>1.
\]

A mere family:

\[
\{U_g|\psi\rangle\}
\]

is not enough.

The branch's orbit-state construction passes this test when active orbit branches span dimension \(>1\).

---

# 8. Quantum phase test

If the transport forms are supposed to model physical symmetry operators, test whether composition is:

### strict

\[
U_gU_h=U_{gh};
\]

or projective

\[
U_gU_h=\omega(g,h)U_{gh}.
\]

If projective, require:

\[
\omega(g,h)\omega(gh,k)
=
\omega(h,k)\omega(g,hk).
\]

Failure kills associativity.

The Pauli finite witness passes the cocycle law exactly.

---

# 9. Groupoid-linearization test

A major new discriminator is:

\[
\mathbb C[\mathcal G].
\]

For the copy pair groupoid:

\[
\mathbb C[\operatorname{Pair}(n)]
\cong
M_n(\mathbb C).
\]

For an internal morphology group \(G\):

\[
\mathbb C[\operatorname{Pair}(n)\times BG]
\cong
M_n(\mathbb C[G]).
\]

This tells us exactly what operator algebra the copy geometry generates.

If the algebra has no useful relation to the target physical observables, the copy model loses explanatory force.

---

# 10. Self-similar-operator prior art

Self-similar group actions already generate \(C^\*\)-algebras in the Nekrashevych/Grigorchuk program.

This is encouraging structurally but dangerous rhetorically.

It shows:

\[
\text{recursive symmetry}
\to
\text{operator algebra}
\]

is mathematically natural.

It does not show:

\[
\text{recursive symmetry}
=
\text{quantum ontology}.
\]

---

# 11. The current strongest architecture

\[
\boxed{
X=A^\*
}
\]

recursive carrier,

\[
\boxed{
\mathcal G=X\sslash G
}
\]

transport/action groupoid,

\[
\boxed{
\mathbb C_\omega[\mathcal G]
}
\]

possibly twisted groupoid algebra,

\[
\boxed{
\pi:\mathbb C_\omega[\mathcal G]\to B(H)
}
\]

Hilbert-space representation,

then:

\[
\boxed{
H\otimes H'
}
\]

monoidal composition and entanglement.

Every arrow in this chain has standard mathematics.

The conjecture is that choosing the right \(X,G,\omega,\pi\) may expose something physically explanatory.

---

# 12. Strongest current falsifier

If every successful instance reduces, after re-labeling, to:

> “choose an arbitrary basis and write ordinary matrix quantum mechanics,”

with no independently motivated \(X,G,\omega\), then the moonshot contributes no physics.

That is the benchmark the program must beat.
