# Operational Quotient Theorem

## A general categorical form of “Categorical Optics + TLICA delta”

**Date:** 2026-10-01  
**Status:** the theorem below is ordinary category theory, proved here for the declared hypotheses. Its use as a TLICA/Categorical-Cybernetics bridge is **CONJECTURED / UNVERIFIED**.

---

# 1. Setup

Let:

\[
Q:\mathcal T\to\mathcal O
\]

be a functor.

Interpret provisionally:

- \(\mathcal T\): a rich/intensional TLICA-semantic category;
- \(\mathcal O\): an extensional categorical-optics / categorical-cybernetics category;
- \(Q\): the operationalization / forgetting functor.

Assume:

1. \(Q\) is **full**;
2. \(Q\) is **bijective on objects**.

The second assumption can later be weakened to an essentially-surjective statement with the expected equivalence/skeleton bookkeeping. The bijective-on-objects form is enough to expose the core theorem cleanly.

---

# 2. Kernel relation on morphisms

For parallel morphisms:

\[
f,g:X\to Y
\]

define:

\[
\boxed{
f\sim_Q g
\iff
Q(f)=Q(g).
}
\]

This is an equivalence relation on every hom-set.

Call it the **operational kernel congruence**.

---

# 3. Proposition 1 — \(\sim_Q\) is compatible with composition

Suppose:

\[
f\sim_Q g
\]

for:

\[
f,g:X\to Y,
\]

and:

\[
h\sim_Q k
\]

for:

\[
h,k:Y\to Z.
\]

Then:

\[
Q(f)=Q(g)
\]

and:

\[
Q(h)=Q(k).
\]

By functoriality:

\[
Q(h\circ f)
=
Q(h)\circ Q(f).
\]

Substitute:

\[
Q(h)\circ Q(f)
=
Q(k)\circ Q(g).
\]

Therefore:

\[
Q(h\circ f)
=
Q(k\circ g),
\]

hence:

\[
\boxed{
h\circ f
\sim_Q
k\circ g.
}
\]

So \(\sim_Q\) is a category congruence.

\(\square\)

---

# 4. Quotient category

Define:

\[
\mathcal T/\ker Q
\]

to have:

- the same objects as \(\mathcal T\);
- hom-sets:

\[
(\mathcal T/\ker Q)(X,Y)
=
\mathcal T(X,Y)/\!\sim_Q;
\]

- composition induced from \(\mathcal T\).

Proposition 1 makes composition well-defined.

---

# 5. Induced functor

Define:

\[
\overline Q:
\mathcal T/\ker Q
\to
\mathcal O
\]

by:

\[
\overline Q(X)=Q(X)
\]

and:

\[
\overline Q([f])=Q(f).
\]

This is well-defined because:

\[
[f]=[g]
\Rightarrow
Q(f)=Q(g).
\]

---

# 6. Proposition 2 — \(\overline Q\) is faithful

Suppose:

\[
\overline Q([f])
=
\overline Q([g]).
\]

Then:

\[
Q(f)=Q(g).
\]

Therefore:

\[
f\sim_Q g.
\]

So:

\[
[f]=[g].
\]

Hence:

\[
\boxed{
\overline Q
\text{ is faithful}.
}
\]

\(\square\)

---

# 7. Proposition 3 — \(\overline Q\) is full

Take any morphism:

\[
u:Q(X)\to Q(Y)
\]

in \(\mathcal O\).

Because \(Q\) is full, there exists:

\[
f:X\to Y
\]

in \(\mathcal T\) with:

\[
Q(f)=u.
\]

Then:

\[
\overline Q([f])=u.
\]

Therefore:

\[
\boxed{
\overline Q
\text{ is full}.
}
\]

\(\square\)

---

# 8. Proposition 4 — object bijection is preserved

By assumption:

\[
Q:
\operatorname{Ob}(\mathcal T)
\to
\operatorname{Ob}(\mathcal O)
\]

is a bijection.

The quotient does not alter objects.

Therefore:

\[
\overline Q
\]

is also bijective on objects.

---

# 9. Theorem — operational quotient is the extensional category

A functor that is:

- bijective on objects;
- full;
- faithful;

is an isomorphism of categories.

Therefore:

\[
\boxed{
\mathcal T/\ker Q
\cong
\mathcal O.
}
\]

\(\square\)

---

# 10. Meaning for Semantic Optics

If a future rich TLICA-semantic category:

\[
\mathsf{TLICAOptics}
\]

admits a full bijective-on-objects operationalization:

\[
Q:
\mathsf{TLICAOptics}
\to
\mathsf{CyberOptics}_{\mathrm{ext}},
\]

then:

\[
\boxed{
\mathsf{TLICAOptics}/\ker Q
\cong
\mathsf{CyberOptics}_{\mathrm{ext}}.
}
\]

This gives a precise structural meaning to:

\[
\text{Categorical Optics}
+
\text{TLICA delta}.
\]

The “delta” is not a number.

It is the intensional structure inside the kernel classes of \(Q\).

---

# 11. Three cases for a kernel distinction

Let:

\[
f\neq g
\]

but:

\[
Q(f)=Q(g).
\]

Then \(f,g\) are distinct intensionally but extensionally identical relative to \(\mathcal O\).

Three research outcomes remain.

## 11.1 Gauge / task redundancy

No admissible intervention or probe in the declared domain depends on the difference.

Then:

\[
f\sim_Q g
\]

is the correct task-relative identification.

Quotient it.

## 11.2 Currently hidden but potentially operational

Current operationalization collapses the distinction, but a larger admissible interface/probe family separates it.

Then:

\[
Q
\]

was too coarse for the enlarged task.

Construct:

\[
Q':
\mathcal T\to\mathcal O'
\]

with:

\[
Q'(f)\neq Q'(g).
\]

The model expands.

## 11.3 Spurious intensional distinction

The rich semantic theory distinguishes \(f,g\), but no warranted domain semantics supports treating that difference as meaningful.

Then the source theory is over-granular.

The quotient is a **correction to TLICA**, not a loss imposed by category theory.

This third case is essential for falsifiability.

---

# 12. Full Yoneda sees every nontrivial kernel distinction upstairs

Let:

\[
y_{\mathcal T}:
\mathcal T
\to
[\mathcal T^{op},\mathbf{Set}]
\]

be the full Yoneda embedding.

Because Yoneda is faithful:

\[
f\neq g
\Rightarrow
y_{\mathcal T}(f)\neq y_{\mathcal T}(g).
\]

So any nontrivial kernel pair:

\[
f\neq g,
\qquad
Q(f)=Q(g)
\]

is visible to full Yoneda **in the rich category**.

After quotienting:

\[
[f]=[g]
\]

in:

\[
\mathcal T/\ker Q.
\]

Yoneda on the quotient therefore correctly sees one morphism.

Thus:

\[
\boxed{
\text{Yoneda exposes the structure of the category you chose;}
\text{ it does not choose the quotient criterion for you.}
}
\]

That criterion is a modeling/empirical commitment.

---

# 13. Restricted probes factor through the operational quotient exactly when they ignore the delta

Let:

\[
P:\mathcal T\to\mathcal E
\]

be some observational/probe functor.

If:

\[
f\sim_Q g
\Rightarrow
P(f)=P(g),
\]

then \(P\) is constant on the kernel classes.

By the quotient universal property, \(P\) factors uniquely through:

\[
\pi_Q:
\mathcal T\to\mathcal T/\ker Q.
\]

So there exists unique:

\[
\overline P:
\mathcal T/\ker Q
\to
\mathcal E
\]

such that:

\[
P
=
\overline P\circ\pi_Q.
\]

Interpretation:

\[
\boxed{
\text{a probe family that factors through }Q
\text{ cannot see the TLICA delta erased by }Q.
}
\]

Conversely, if some admissible \(P\) satisfies:

\[
P(f)\neq P(g)
\]

for a kernel pair, then \(P\) does **not** factor through the coarse operational quotient.

That probe is a **lamp** demonstrating the coarse category is insufficient for that expanded task.

---

# 14. Exact full-Yoneda fork

For any proposed kernel distinction \(f\neq g\):

### Rich category

\[
y_{\mathcal T}(f)\neq y_{\mathcal T}(g).
\]

### Coarse operational category

\[
Q(f)=Q(g).
\]

The question is therefore not:

> Which one is “Truth”?

It is:

> Which category/probe language is adequate to the declared task and reality-coupled interventions?

If future admissible probes all factor through \(Q\), the quotient remains operationally adequate.

If a warranted probe fails to factor through \(Q\), enlarge the operational model.

---

# 15. Connection to Hefford & Comfort

Hefford and Comfort's *Coend Optics for Quantum Combs* compares an intensional optic construction with an extensional quotient by operational behavior and constructs a full, bijective-on-objects quotient functor, with conditions for stronger equivalence/isomorphism results.

Primary source:

James Hefford, Cole Comfort, *Coend Optics for Quantum Combs*, arXiv:2205.09027  
https://arxiv.org/abs/2205.09027

The theorem above is not presented as their quantum-comb theorem.

It records the elementary categorical kernel-quotient mechanism relevant to our own bridge.

Their result demonstrates that the **intensional-to-extensional quotient problem is established optic-theory territory**, which makes it the correct prior-art frame for the Semantic Optics moonshot.

---

# 16. Finite witness

The current finite reparametrisation construction has:

\[
|M_H|=5,
\]

\[
|M_Q|=4.
\]

The functor:

\[
q:M_H\to M_Q
\]

is:

- full;
- bijective on the single object;
- not faithful.

Its only nontrivial kernel class is:

\[
\{
p\circ s,
s\circ p
\}.
\]

And:

\[
M_H/\ker q
\cong
M_Q.
\]

So the executable is an exact finite instance of the theorem.

See:

- [FINITE_REPARAMETRISATION_BRIDGE.md](FINITE_REPARAMETRISATION_BRIDGE.md);
- [param_optic_reparam_demo.py](param_optic_reparam_demo.py).

---

# 17. Stronger moonshot restatement

The research target can now be stated without metaphor.

Find:

\[
Q:
\mathsf{TLICAOptics}
\to
\mathsf{CyberOptics}_{\mathrm{ext}}
\]

and determine:

1. is \(Q\) a functor?
2. is \(Q\) full?
3. what is \(\ker Q\)?
4. which kernel distinctions are empirically/probe-relevant?
5. does:

\[
\mathsf{TLICAOptics}/\ker Q
\simeq
\mathsf{CyberOptics}_{\mathrm{ext}}
\]

hold?
6. can a richer target retain the warranted kernel distinctions faithfully?

If yes, then “TLICA deviation” becomes mathematically precise:

\[
\boxed{
\Delta_{\mathrm{TLICA}}
=
\ker Q
\quad
\text{relative to the declared extensional operationalization}.
}
\]

That is the current strongest formulation.
