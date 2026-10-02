# Pressure Test — What Exactly Is the Missing \(B\)?

## Rival frameworks, maturity, and the 2026 absolute-geometry result

**Date:** 2026-10-01  
**Status:** external prior-art audit. No novelty claim.

---

# 1. Why one-word answers fail

Several established/research programs each realize a different part of the desired square.

So “\(B=\) arithmetic geometry” is too vague, while “\(B=\) Scaling Site” is too program-specific.

The right strategy is to ask what each candidate preserves.

---

# 2. Candidate 1 — adèles

\[
\mathbb A_{\mathbb Q}
=
\mathbb R\times\prod_p'\mathbb Q_p.
\]

### Strengths

- literally contains all places;
- canonical in number theory;
- central to Tate's thesis;
- local-to-global harmonic analysis;
- product formula and idèle class group.

### Weakness

Adèles are a global topological ring, not by themselves the categorical/geometric completion suggested by \(\mathbf{Set}\to B\).

### Verdict

Best **analytic substrate**, not sufficient as the full \(B\).

---

# 3. Candidate 2 — Arakelov geometry

Arakelov geometry adds archimedean data to arithmetic geometry so that arithmetic curves behave more like complete curves.

### Strengths

- standard treatment of finite and infinite places in one geometric formalism;
- closest conservative answer to “finite places + infinity.”

### Weakness

Does not explain the striking:

\[
(\mathbf{Set},\mathbb N^\times)
\]

corner nearly as directly as \(\mathbb F_1\)/Arithmetic-Site approaches.

### Verdict

Best **standard geometric shadow** of \(B\).

---

# 4. Candidate 3 — \(\mathbb F_1\) / absolute geometry

Historically, one motivation for geometry over the field with one element is that the compactification of:

\[
\operatorname{Spec}\mathbb Z
\]

at the infinite place should behave like a curve over an absolute base.

Toën–Vaquié's relative geometry makes the Set connection unusually concrete.

### Strengths

- excellent Set/category fit;
- designed for “under Spec Z” / absolute arithmetic;
- connects arithmetic curves and infinite place;
- numerous categorical formulations.

### Weakness

There is no one universally accepted \(\mathbb F_1\) geometry.

Different frameworks retain different structures.

### Verdict

Best **umbrella category** for \(B\), but not a unique mathematical object.

---

# 5. Candidate 4 — Arithmetic Site

Connes–Consani's Arithmetic Site has underlying topos:

\[
\widehat{\mathbb N^\times}
\]

and characteristic-one/tropical structure sheaf.

### Strengths

- almost exact realization of:
  \[
  (\mathbf{Set},\mathbb N^\times);
  \]
- points over tropical reals identify with a quotient of the adèle class space;
- positive-real scaling corresponds to Frobenius action;
- explicitly built to geometrize structures around the Riemann zeta function.

### Weakness

Belongs to a specific noncommutative/absolute-geometry research program.

Its relevance to RH is not a theorem solving RH.

### Verdict

Strongest concrete realization of the **\(C\to B\)** edge.

---

# 6. Candidate 5 — Scaling Site

Obtained by extension from discrete/characteristic-one arithmetic structure toward tropical real scalars.

### Strengths

- Euclidean half-line;
- \(\mathbb N^\times\) scaling action;
- adelic points;
- tropical curve structure;
- Riemann–Roch-like theory with real-valued degree/dimension.

### Weakness

Again research-program-specific.

### Verdict

Strongest concrete realization of the **\(D\to B\)** edge.

---

# 7. Candidate 6 — 2026 absolute \(\mathbb F_1\)-curve

Connes–Consani 2026 construct:

\[
(\operatorname{Spec}\mathbb Z)_{\mathbb F_1}.
\]

Their abstract states that this provides a common geometric origin for:

- \(p\)-adic Hodge theory;
- complex analytic geometry;
- the adelic Scaling Site.

They also recover both:

\[
W_p=\mathbb Q_p^\times
\]

and:

\[
W_\infty=\mathbb C^\times
\]

in the complex-point analysis, and connect archimedean orbits with the real scaling-site periodic orbit.

### Strengths

This is almost exactly the all-places/common-host role demanded of \(B\).

### Weakness

- June 2026 preprint;
- very recent;
- not yet a canonical consensus framework;
- should not be treated as established theorem-level unification of all arithmetic geometry.

### Verdict

\[
\boxed{
\textbf{strongest current moonshot B-candidate}
}
\]

but must remain explicitly tagged **recent preprint / program-specific**.

---

# 8. Candidate 7 — Segal \(\Gamma\)-rings / universal arithmetic

Connes–Consani's absolute algebraic geometry via Segal \(\Gamma\)-rings aims to unify ring and monoid-like worlds and admits quotient constructions such as the adèle class space.

The 2020 universal-arithmetic work also connects \(\Gamma\)-rings, the Arithmetic Site, and the Arakelov compactification.

### Verdict

Potentially the **algebraic substrate underneath \(B\)** rather than the visible missing corner itself.

---

# 9. Critical type correction

The initial square mixed:

- fields of mathematics;
- categories;
- arithmetic places;
- sets/numbers.

A useful categorical benchmark requires homogeneous vertex types.

Thus category theory should become the ambient 2-language, and each corner should be a **structured context category**.

The branch should not try to prove commutativity of the raw English-label square.

It should construct functors among typed replacements.

---

# 10. Strongest replacement

The current benchmark should use:

\[
C_{\mathrm{fin}}
=
\text{finite-place local categories},
\]

\[
D_\infty
=
\text{archimedean local category},
\]

\[
A_{\mathrm{an}}
=
\text{adelic/global analytic category},
\]

\[
B_{\mathrm{abs}}
=
\text{absolute/global arithmetic-geometric category}.
\]

Then category theory governs:

\[
\mathsf{Ctx}
\]

containing those context categories and their transport functors.

---

# 11. The square probably does not strictly commute

The analytic and geometric globalizations are different constructions.

A future comparison may be:

- adjunction;
- natural transformation;
- equivalence on a subcategory;
- common image under a third functor;
- trace/decategorification.

We should **not** write:

\[
A\cong B
\]

until an actual comparison functor is defined.

The meaningful question is:

\[
\boxed{
\text{what invariant/probe profiles do }A\text{ and }B\text{ preserve in common?}
}
\]

---

# 12. Best next non-toy targets

1. Tate thesis local/global factorization.
2. Product formula as finite/archimedean coherence.
3. Arithmetic Site:
   \[
   \widehat{\mathbb N^\times}.
   \]
4. Scaling Site scalar extension.
5. Arakelov compactification.
6. Recent:
   \[
   (\operatorname{Spec}\mathbb Z)_{\mathbb F_1}.
   \]

These should be tested against the existing:
- full/faithful;
- essential-surjectivity;
- adjunction;
- unit/counit;
- operational-kernel;
- Yoneda-transport;
- coverage-defect vocabulary.

---

# 13. Current verdict

The missing \(B\) is best treated as a **host family**:

\[
\boxed{
B_{\mathrm{abs}}
=
\text{absolute adelic arithmetic geometry}.
}
\]

The Arithmetic Site and Scaling Site are unusually precise concrete realizations of its discrete and archimedean faces.

The 2026 absolute \(\mathbb F_1\)-curve is the strongest current proposal for a single geometric host containing both.
