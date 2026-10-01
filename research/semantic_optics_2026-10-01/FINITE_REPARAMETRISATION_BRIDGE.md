# Finite Reparametrisation Bridge

## Intensional semantic history, extensional categorical quotient, and the first exact TLICA-delta witness

**Date:** 2026-10-01  
**Status:** construction-level finite theorem package. The algebraic statements below are exact inside the declared finite model. No human/cognitive inference is licensed. This is a **reparametrisation spine**, not yet a full implementation of \(\mathbf{Para}(\mathbf{Optic})\).

**Executable:** [param_optic_reparam_demo.py](param_optic_reparam_demo.py)  
**Results:** [param_optic_reparam_demo_results.json](param_optic_reparam_demo_results.json)  
**Receipt:** [param_optic_reparam_demo_tests.txt](param_optic_reparam_demo_tests.txt)

---

# 1. Why this construction exists

The previous branch state left a concrete theorem debt:

> define a finite TLICA-style semantic structure independently enough to preserve a real semantic distinction, map it into a coarser categorical-cybernetic/reparametrisation model, and compute exactly whether the bridge is full, faithful, essentially surjective, or a quotient.

The chosen distinction is deliberately minimal and TLICA-shaped:

- **source information becomes available**;
- **a discriminating probe becomes available**;
- the final capabilities may be identical while their **acquisition order** differs.

Nothing in TLICA currently proves that this order must matter empirically.

That is why the construction treats order as a candidate semantic distinction, then asks what the coarse operational model does to it.

---

# 2. History-sensitive semantic parameter states

Let

\[
H
=
\{N,S,P,SP,PS\}.
\]

Interpretation:

- \(N\): neither source resolution nor probe access;
- \(S\): source resolution only;
- \(P\): probe access only;
- \(SP\): source resolution arrived before probe access;
- \(PS\): probe access arrived before source resolution.

Define two update endomorphisms:

\[
s_H:H\to H
\]

and

\[
p_H:H\to H.
\]

They add the relevant capability while preserving acquisition order.

Explicitly:

\[
s_H:
\begin{cases}
N\mapsto S\\
S\mapsto S\\
P\mapsto PS\\
SP\mapsto SP\\
PS\mapsto PS
\end{cases}
\]

and

\[
p_H:
\begin{cases}
N\mapsto P\\
S\mapsto SP\\
P\mapsto P\\
SP\mapsto SP\\
PS\mapsto PS.
\end{cases}
\]

Let:

\[
M_H
=
\langle s_H,p_H\rangle
\subseteq
\operatorname{End}(H).
\]

The generated monoid has exactly five morphisms:

\[
M_H
=
\{
1,s,p,p\circ s,s\circ p
\}.
\]

And:

\[
p\circ s
\neq
s\circ p.
\]

The distinction is concrete:

\[
(p\circ s)(N)=SP,
\]

while:

\[
(s\circ p)(N)=PS.
\]

So the source semantic category is the one-object category with endomorphism monoid \(M_H\).

---

# 3. Coarse extensional parameter states

Now forget acquisition order.

Let:

\[
Q
=
\{N,S,P,B\},
\]

where:

\[
B=\text{both capabilities present}.
\]

Define update endomorphisms:

\[
s_Q,p_Q:Q\to Q
\]

that only record whether source/probe capability is present.

Then:

\[
p_Q\circ s_Q
=
s_Q\circ p_Q.
\]

The generated monoid is:

\[
M_Q
=
\{
1,s,p,b
\},
\]

where:

\[
b=p\circ s=s\circ p.
\]

So the target is the one-object category whose morphisms are the coarse reparametrisations \(M_Q\).

This is the extensional/reparametrisation target.

---

# 4. Forgetting history

Define:

\[
\pi:H\to Q
\]

by:

\[
\pi(N)=N,\quad
\pi(S)=S,\quad
\pi(P)=P,
\]

and:

\[
\pi(SP)=\pi(PS)=B.
\]

For every source morphism:

\[
m\in M_H,
\]

there exists a unique coarse morphism:

\[
q(m)\in M_Q
\]

satisfying:

\[
\boxed{
\pi\circ m
=
q(m)\circ\pi.
}
\]

Explicitly:

\[
q(1)=1,
\]

\[
q(s)=s,
\]

\[
q(p)=p,
\]

\[
q(p\circ s)=b,
\]

\[
q(s\circ p)=b.
\]

The executable checks this semiconjugacy for all five source morphisms.

---

# 5. Proposition 1 — \(q\) is a functor / monoid homomorphism

For every:

\[
a,b\in M_H,
\]

the executable checks:

\[
q(a\circ b)
=
q(a)\circ q(b).
\]

There are:

\[
5\times5=25
\]

composition cells.

All 25 pass.

Therefore:

\[
q:M_H\to M_Q
\]

is a monoid homomorphism, equivalently a functor between the corresponding one-object categories.

**Status: Disclosed in the finite construction.**

---

# 6. Proposition 2 — the coarse functor is full but not faithful

Because:

\[
q(M_H)=M_Q,
\]

the functor is surjective on the unique hom-set.

For one-object categories, this means:

\[
q
\]

is **full**.

The object map is trivially essentially surjective.

But:

\[
p\circ s
\neq
s\circ p
\]

while:

\[
q(p\circ s)
=
q(s\circ p)
=
b.
\]

Therefore \(q\) is not injective on the hom-set.

So:

\[
\boxed{
q
\text{ is full and essentially surjective but not faithful.}
}
\]

Hence:

\[
\boxed{
q
\text{ is not an equivalence.}
}
\]

This is the first explicit finite bridge with a computed full/faithful verdict.

---

# 7. Proposition 3 — the TLICA-style delta is exactly the kernel congruence

The fibers of \(q\) are:

\[
[1]=\{1\},
\]

\[
[s]=\{s\},
\]

\[
[p]=\{p\},
\]

\[
[b]
=
\{
p\circ s,
s\circ p
\}.
\]

There is exactly one nontrivial collision.

Because \(q\) is a monoid homomorphism, its kernel relation is a monoid congruence.

Therefore:

\[
M_H/\ker q
\]

is a well-defined quotient monoid.

The executable verifies that its four quotient classes map bijectively and multiplicatively onto \(M_Q\).

Thus:

\[
\boxed{
M_H/\ker q
\cong
M_Q.
}
\]

This is the cleanest finite realization yet of:

\[
\boxed{
\text{categorical cybernetic base}
+
\text{TLICA delta}.
}
\]

The “delta” is not an additive scalar.

Here it is exactly:

\[
\boxed{
\Delta
=
\ker q
}
\]

—the semantic distinction erased by the operational quotient.

---

# 8. Two legitimate readings of the same result

This is where the earlier full-Yoneda fork becomes mathematically sharp.

## Reading A — acquisition order is semantically redundant

If:

\[
SP
\sim
PS
\]

for the task, then the kernel distinction should be quotiented.

The correct category is:

\[
M_H/\ker q
\cong
M_Q.
\]

Then the coarse categorical model is not “missing” anything relevant.

The apparent TLICA delta was gauge/redundancy relative to the declared task.

## Reading B — acquisition order is semantically load-bearing

If:

\[
SP
\not\sim
PS
\]

for the task, then:

\[
q
\]

is too coarse.

Its non-faithfulness is a real loss.

The target must be enriched so that:

\[
p\circ s
\]

and:

\[
s\circ p
\]

remain distinguishable.

So:

\[
\boxed{
\text{quotient the distinction}
\quad\lor\quad
\text{represent the distinction}.
}
\]

The model is not allowed to do neither while still claiming equivalence.

---

# 9. History-enriched target

Use the full history parameter state \(H\) as the target parameter object.

The concrete endomorphism monoid generated by:

\[
s_H,p_H
\]

has exactly the same five morphisms as the source semantic monoid.

The concrete representation is therefore:

- full;
- faithful;
- essentially surjective.

So in this finite case:

\[
\boxed{
M_H
\simeq
M_H^{\mathrm{concrete}}.
}
\]

This result is not a novelty theorem; it demonstrates the exact form of the repair:

> preserve the semantic history in the parameter state.

---

# 10. Full Yoneda sees what the coarse action forgets

For a one-object category with monoid \(M_H\), the Yoneda representation is the regular action:

\[
y(m):
h\mapsto m\circ h.
\]

If:

\[
y(m)=y(n),
\]

then evaluate both at the identity:

\[
y(m)(1)=m,
\]

\[
y(n)(1)=n.
\]

Therefore:

\[
m=n.
\]

So the full Yoneda representation is faithful.

The executable records all five regular signatures and verifies that they are distinct.

In particular:

\[
y(p\circ s)
\neq
y(s\circ p).
\]

Thus:

\[
\boxed{
\text{full Yoneda sees the update-order distinction.}
}
\]

But the coarse parameter action does not:

\[
q(p\circ s)
=
q(s\circ p).
\]

This is a direct finite realization of:

\[
\boxed{
\text{full categorical profile distinguishes}
\quad\text{while}\quad
\text{restricted operational context collapses}.
}
\]

---

# 11. The coarse controller also cannot see the distinction

The demo defines a controller depending only on coarse state \(Q\).

When the two history-sensitive composites are passed through:

\[
H
\xrightarrow{m}
H
\xrightarrow{\pi}
Q
\xrightarrow{c_Q}
A',
\]

their complete coarse-controller signatures agree.

So the distinction is not merely erased symbolically.

It is operationally invisible to that declared arena.

This gives the correct status:

\[
\boxed{
\text{real in the history model}
\quad+\quad
\text{invisible in the coarse arena}.
}
\]

No contradiction exists.

---

# 12. A single lamp makes the delta visible

Define one history-sensitive probe:

\[
L:H\to
\{
\text{source-first},
\text{probe-first},
\text{unresolved}
\}.
\]

Then:

\[
L((p\circ s)(N))
=
\text{source-first},
\]

while:

\[
L((s\circ p)(N))
=
\text{probe-first}.
\]

So:

\[
\boxed{
L\circ(p\circ s)
\neq
L\circ(s\circ p).
}
\]

One new probe splits the collision.

This is exactly the “lamp” behavior anticipated in the restricted-Yoneda program.

---

# 13. Relation to Hefford & Comfort

A highly relevant prior-art result appeared during this round:

James Hefford and Cole Comfort, *Coend Optics for Quantum Combs*, arXiv:2205.09027  
https://arxiv.org/abs/2205.09027

They compare:

- an **intensional** coend-optic definition;
- an **extensional** definition obtained by quotienting operationally indistinguishable behavior.

They construct a full, bijective-on-objects quotient functor from the intensional to the extensional category and give conditions under which it becomes an isomorphism.

Their domain is quantum combs, not TLICA or social semantics.

But the abstract pressure is directly relevant:

\[
\boxed{
\text{intensional structure}
\longrightarrow
\text{operational quotient}
}
\]

is already a serious categorical question in optic theory.

So this branch does **not** claim novelty for that pattern.

Instead, the finite Semantic Optics construction now deliberately asks the analogous question:

> which TLICA-style intensional distinctions survive the operational quotient, and which should be identified?

That is a far more disciplined research target.

---

# 14. Full Yoneda and the extensional quotient

The branch's full-Yoneda statement now has a concrete finite example.

Inside \(M_H\):

\[
p\circ s
\neq
s\circ p
\]

and Yoneda separates them.

After quotienting:

\[
[p\circ s]
=
[s\circ p]
\]

in:

\[
M_H/\ker q.
\]

Yoneda on the **quotient category** now correctly treats them as the same morphism because they are no longer distinct objects of discourse there.

This clarifies an important point:

\[
\boxed{
\text{Yoneda never decides which category you ought to use.}
}
\]

It only makes the structure of the declared category maximally visible up to isomorphism.

The modeling decision:

\[
\text{retain delta}
\quad\text{vs}\quad
\text{quotient delta}
\]

comes first.

Reality/probes must pay that truth debt.

---

# 15. Exact connection to “complete vs indistinguishably complete”

Let the rich model be:

\[
\mathcal C_H
\]

and the coarse quotient:

\[
\mathcal C_Q.
\]

Relative to the coarse operational arena:

\[
p\circ s
\]

and:

\[
s\circ p
\]

are indistinguishable.

Relative to full Yoneda on \(\mathcal C_H\), they are distinguishable.

So the statement:

> “the model is indistinguishably complete”

is always indexed to a category/probe language.

If the relevant reality admits a history-sensitive lamp, \(\mathcal C_Q\) was incomplete for that task.

If no admissible future interaction depends on the difference, the quotient may be exactly right.

This is not Truth proper.

It is model adequacy relative to declared observables and interventions.

---

# 16. Why this is stronger than the previous obstruction demo

The earlier [bridge obstruction](bridge_obstruction_demo.py) stipulated two non-isomorphic semantic states and showed a coarse target could not be equivalent.

This new construction does more:

1. defines the semantic distinction dynamically;
2. defines the coarse forgetting map explicitly;
3. checks functoriality on all 25 composition cells;
4. computes full / faithful / essentially-surjective status;
5. computes the exact kernel;
6. proves the quotient is the coarse target;
7. shows full Yoneda sees the kernel distinction;
8. shows the declared coarse controller does not;
9. constructs one lamp that does.

It is therefore the current strongest finite result in the Semantic Optics dossier.

---

# 17. What it does not prove

It does **not** prove:

- humans encode source/probe acquisition order;
- TLICA requires \(SP\neq PS\);
- categorical cybernetics omits real TLICA structure;
- the full \(\mathbf{Para}(\mathbf{Optic})\) bridge exists;
- the source semantic monoid is the correct TLICA category;
- all TLICA delta is a kernel congruence;
- any real-world category is complete;
- Yoneda establishes truth proper.

---

# 18. New theorem target

The next abstraction should generalize this finite result.

Seek a functor:

\[
Q:
\mathsf{TLICAOptics}
\to
\mathsf{CyberOptics}_{\mathrm{ext}}
\]

such that:

1. \(Q\) is full on the declared domain;
2. the kernel congruence captures exactly operationally invisible semantic distinctions;
3. the quotient:

\[
\mathsf{TLICAOptics}/\ker Q
\]

is equivalent to the extensional cybernetic target;
4. an enriched target:

\[
\mathsf{CyberOptics}_{\mathrm{rich}}
\]

admits a faithful lift whenever a kernel distinction is empirically/probe-relevant.

That would turn:

\[
\text{Categorical Optics + TLICA delta}
\]

into a genuine **intensional/extensional quotient theorem**.

This is now the most concrete route to the moonshot.
