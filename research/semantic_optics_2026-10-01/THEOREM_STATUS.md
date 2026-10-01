# Theorem Status — Semantic Optics

**Date:** 2026-10-01  
**Purpose:** compact status page separating what this branch actually establishes from what it only proposes.

---

# 1. Disclosed / established mathematics used correctly

## T1 — standard categorical optic form

For suitable monoidal/action data:

\[
\operatorname{Optic}
((S,S'),(A,A'))
=
\int^M
\mathcal C(S,M\bullet A)
\times
\mathcal D(M\bullet A',S').
\]

This is established categorical-optics mathematics.

---

## T2 — closure with a controller

For representative:

\[
l:S\to M\otimes A,
\qquad
r:M\otimes A'\to S'
\]

and controller:

\[
c:A\to A',
\]

closure is:

\[
r\circ(\mathrm{id}_M\otimes c)\circ l.
\]

Standard composition.

---

## T3 — residual-representation invariance

If two optic representatives differ by the usual residual/coend reparametrisation, closing them with the same controller produces the same external morphism.

Proof recorded in [FORMALISM.md](FORMALISM.md).

---

## T4 — Yoneda embedding

For a locally small category:

\[
y:\mathcal C\to[\mathcal C^{op},\mathbf{Set}]
\]

is full and faithful.

Standard theorem.

---

## T5 — restricted Yoneda / density

For probe functor:

\[
i:\mathcal P\to\mathcal C,
\]

the restricted nerve:

\[
N_i(X)=\mathcal C(i-,X)
\]

is full and faithful exactly when \(i\) is dense.

Standard theorem.

---

## T6 — category-equivalence target

A functor that is full, faithful, and essentially surjective is an equivalence of categories.

Standard theorem.

---

## T7 — operational kernel quotient theorem

For a full functor:

\[
Q:\mathcal T\to\mathcal O
\]

that is bijective on objects, define for parallel morphisms:

\[
f\sim_Q g
\iff
Q(f)=Q(g).
\]

Then \(\sim_Q\) is a category congruence and the induced functor:

\[
\overline Q:
\mathcal T/\ker Q
\to
\mathcal O
\]

is bijective on objects, full, and faithful. Therefore:

\[
\boxed{
\mathcal T/\ker Q
\cong
\mathcal O.
}
\]

Proof recorded in [OPERATIONAL_QUOTIENT_THEOREM.md](OPERATIONAL_QUOTIENT_THEOREM.md).

---

## T8 — scale–locality naturality

Let \(\mathcal X_{n+1},\mathcal X_n:\mathsf{Reg}^{op}\to\mathsf C\) be locality/state functors at adjacent scales and let:

\[
Q_n:\mathcal X_{n+1}\Rightarrow\mathcal X_n
\]

be a natural transformation.

Then for every inclusion \(U\subseteq V\):

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

This is the naturality square: coarse-grain then localize = localize then coarse-grain.

Proof/interpretation recorded in [LOCAL_REALIZABILITY_THEOREM.md](LOCAL_REALIZABILITY_THEOREM.md).

---

## T9 — exact reversible Yoneda form transport

For:

\[
f:A\to B,
\]

the following are equivalent:

- \(f\) is an isomorphism;
- \(y(f)\) is a natural isomorphism;
- every generalized-element transport:
  \[
  \mathcal C(C,A)\to\mathcal C(C,B),
  \quad
  x\mapsto f\circ x
  \]
  is bijective naturally in \(C\).

Thus if \(y=f\circ x\):

\[
\boxed{
x=f^{-1}\circ y.
}
\]

Standard Yoneda consequence; specialized in [YONEDA_TRANSPORT_FORMS.md](YONEDA_TRANSPORT_FORMS.md).

---

## T10 — adjoint–Yoneda transport theorem

If:

\[
F\dashv G,
\]

then:

\[
\boxed{
F^\*y_{\mathcal B}(d)
\cong
y_{\mathcal A}(Gd).
}
\]

For \(X\in\mathcal A\), the canonical Yoneda transport comparison:

\[
\theta_{F,X}:
y_{\mathcal A}(X)
\to
F^\*y_{\mathcal B}(FX)
\]

corresponds under this isomorphism exactly to:

\[
y_{\mathcal A}(\eta_X)
\]

where:

\[
\eta_X:X\to GFX
\]

is the adjunction unit.

Therefore:

\[
\boxed{
\theta_{F,X}\text{ iso}
\iff
\eta_X\text{ iso}.
}
\]

For all \(X\), this is equivalent to \(F\) being full and faithful.

Proof recorded in [ADJOINT_YONEDA_TRANSPORT.md](ADJOINT_YONEDA_TRANSPORT.md).

---

## T11 — canonical all-places split for \(\mathbb Q\)

By Ostrowski's theorem, every nontrivial absolute value of \(\mathbb Q\), up to equivalence, is either:

- \(p\)-adic for a finite prime \(p\);
- the ordinary archimedean absolute value.

Together with the product formula:

\[
\boxed{
|x|_\infty\prod_{p<\infty}|x|_p=1,
}
\]

the author's finite/archimedean split exhausts the places of \(\mathbb Q\) and obeys an exact global compatibility law.

This is standard number theory, not a TLICA theorem.

---

## T12 — finite/archimedean inverse-form constraint

Define:

\[
P_{\mathrm{fin}}(x)=(|x|_p)_p,
\quad
\Pi((r_p)_p)=\prod_pr_p,
\quad
P_\infty(x)=|x|_\infty.
\]

Then on \(\mathbb Q^\times\):

\[
\boxed{
\Pi\circ P_{\mathrm{fin}}
=
\iota\circ P_\infty,
\qquad
\iota(r)=r^{-1}.
}
\]

This is the first exact non-toy “form transport” equation in the arithmetic-place benchmark.

---

## T13 — place completion as an adjoint context transport

For every place \(v\) of \(\mathbb Q\):

\[
F_v
=
-\otimes_{\mathbb Q}\mathbb Q_v
\]

is left adjoint to restriction of scalars:

\[
G_v
=
\operatorname{Res}_{\mathbb Q}^{\mathbb Q_v}.
\]

Thus:

\[
\boxed{
\operatorname{Hom}_{\mathbb Q_v}
(V\otimes_{\mathbb Q}\mathbb Q_v,W)
\cong
\operatorname{Hom}_{\mathbb Q}
(V,G_vW).
}
\]

On finite-dimensional vector spaces, \(F_v\) is:
- faithful;
- essentially surjective;
- generally not full.

So standard place completion realizes:

\[
\boxed{
\Delta_{\mathrm{coverage}}=0,
\qquad
\Delta_{\mathrm{hom}}\neq0.
}
\]

This is standard algebra/category theory, interpreted in [PLACE_COMPLETION_ADJUNCTION.md](PLACE_COMPLETION_ADJUNCTION.md).

---


## T14 — copy-groupoid transport theorem

Let \(X_i\) be copies of a structured object \(X\), with charts:
\[
p_i:X\overset{\sim}{\to}X_i.
\]
For \(g\in G\le\operatorname{Aut}(X)\), define:
\[
T_{b\leftarrow a}^g=p_bg\,p_a^{-1}.
\]
Then:
\[
T_{c\leftarrow b}^hT_{b\leftarrow a}^g=T_{c\leftarrow a}^{hg},
\]
and:
\[
(T_{b\leftarrow a}^g)^{-1}=T_{a\leftarrow b}^{g^{-1}}.
\]
Hence \(\operatorname{Hom}(X_a,X_b)\cong G\) in this construction.

---

## T15 — pair-groupoid linearization

For pair-groupoid arrows \(e_{ij}:j\to i\):
\[
e_{ij}e_{kl}=\delta_{jk}e_{il}.
\]
Therefore:
\[
\boxed{\mathbb C[\operatorname{Pair}(n)]\cong M_n(\mathbb C).}
\]

Standard groupoid/operator-algebra result.

---

## T16 — orbit-state separability criterion

For:
\[
|\Psi\rangle=\sum_i\alpha_i|i\rangle\otimes|\psi_i\rangle,
\]
the Schmidt rank is:
\[
\dim\operatorname{span}\{|\psi_i\rangle:\alpha_i\neq0\}.
\]
Thus the state is separable iff all active branch vectors are collinear.

Applied to \(|\psi_i\rangle=U_i|\psi\rangle\), this gives the exact orbit-entanglement criterion.

---

## T17 — projective form composition

For:
\[
U_gU_h=\omega(g,h)U_{gh},
\]
associativity requires:
\[
\boxed{\omega(g,h)\omega(gh,k)=\omega(h,k)\omega(g,hk).}
\]

This is the standard 2-cocycle law.

---

# 2. Observed finite construction results

## F1 — same base interface, different observer closures

The finite semantic-optics witness holds base world/view/residual fixed and changes only the observer/controller decoration.

Result:

\[
8/8
\]

checks pass.

Different observer states produce different reconstructed meanings, responses, and closed world updates.

**Scope:** deterministic fixture only.

---

## F2 — restricted probe collision and lamp

In the same finite witness:

\[
N_{\{p\}}(x)
=
N_{\{p\}}(y)
\]

while adding probe \(q\) yields:

\[
N_{\{p,q\}}(x)
\neq
N_{\{p,q\}}(y).
\]

Full representable profiles distinguish every fixture object.

**Scope:** finite poset category only.

---

## F3 — coarse bridge obstruction

A second finite construction defines two internally distinct semantic states with identical extensional controller signatures.

Assume the source treats them as non-isomorphic/discrete:

\[
\mathsf T(A,B)=\varnothing.
\]

The naive target collapses both to:

\[
c.
\]

Then:

\[
\mathsf O(U A,U B)
=
\mathsf O(c,c)
\ni
\mathrm{id}_c.
\]

Hence:

\[
U
\]

is not full.

Result:

\[
6/6
\]

checks pass.

**Conditional consequence:**

\[
\boxed{
\text{quotient the semantic distinction}
\quad\text{or}\quad
\text{represent it in the target}.
}
\]

---

## F4 — finite reparametrisation quotient bridge

A history-sensitive semantic parameter monoid:

\[
M_H
=
\{1,s,p,p\circ s,s\circ p\}
\]

is mapped to a coarse extensional reparametrisation monoid:

\[
M_Q
=
\{1,s,p,b\}
\]

that forgets acquisition order.

Executed result:

\[
\boxed{17/17\ \text{checks pass}.}
\]

The bridge:

\[
q:M_H\to M_Q
\]

is:

- full;
- essentially surjective;
- **not faithful** because:

\[
q(p\circ s)=q(s\circ p)=b.
\]

Its exact kernel quotient satisfies:

\[
\boxed{
M_H/\ker q
\cong
M_Q.
}
\]

A history-enriched target restores full + faithful + essentially-surjective representation.

Full regular Yoneda distinguishes the two update orders; the coarse arena/controller does not; one added history-sensitive lamp does.

See [FINITE_REPARAMETRISATION_BRIDGE.md](FINITE_REPARAMETRISATION_BRIDGE.md).

**Scope:** finite one-object categories only.

---

## F5 — local realizability / covariance witness

The finite witness checks four structures:

1. a valid scale/locality square commutes on all \(9\) finite states;
2. a non-natural mutant fails on \(3/9\) states;
3. two Lorentz frames assign different coordinates while preserving the Minkowski interval and invertibility;
4. distinct global correlation models can share identical local marginals, and locally satisfiable odd-cycle constraints can have no global section.

Executed result:

\[
\boxed{8/8\ \text{checks pass}.}
\]

See [LOCAL_REALIZABILITY_THEOREM.md](LOCAL_REALIZABILITY_THEOREM.md).

**Scope:** finite construction only.

---

## F6 — Yoneda form / adjunction witness

Executed result:

\[
\boxed{14/14\ \text{checks pass}.}
\]

It exhibits:

- an object isomorphism with exact reversible generalized-element/Yoneda transport;
- an adjunction whose hom-form bijections are exact on all six cells but which is **not** an equivalence;
- a full+faithful left adjoint with zero Yoneda hom-defect but nonzero coverage defect;
- a separate genuine category equivalence with invertible unit/counit.

See [YONEDA_TRANSPORT_FORMS.md](YONEDA_TRANSPORT_FORMS.md).

---

## F7 — finite three-context adjoint atlas

Executed result:

\[
\boxed{16/16\ \text{checks pass}.}
\]

Across three nested finite contexts:

- all \(26\) adjunction hom-bijection cells pass;
- forward transports compose;
- backward adjoints compose in reverse order;
- all forward transports are full+faithful;
- all forward Yoneda comparisons are isomorphisms;
- all forward transports have nonzero coverage defect;
- downward/right-adjoint transports are faithful but not full;
- all triangle identities pass.

See [CONTEXT_ATLAS_FINITE.md](CONTEXT_ATLAS_FINITE.md).

---

## F8 — arithmetic place-square benchmark

Executed result:

\[
\boxed{8/8\ \text{checks pass}.}
\]

The witness verifies:
- exact product formula on five rationals;
- exact finite-product / inverse-archimedean relation;
- finite support of nontrivial \(p\)-adic norms;
- truncated Euler-product convergence at \(s=2\);
- two special-value checks of the completed-zeta functional equation;
- associativity of the \(\mathbb N^\times\) real scaling action.

See [PLACE_FORM_TRANSPORT.md](PLACE_FORM_TRANSPORT.md).

**Scope:** standard number-theory benchmark only.

---


## F9 — self-similar quantum-copy compatibility witness

Executed result:
\[
\boxed{12/12\ \text{checks pass}.}
\]

It verifies:
- copy-chart roundtrips;
- groupoid inverse/composition;
- distinct internal morphology forms;
- binary adding-machine wreath recursion through five levels;
- complete adding-machine cycles on every tested level;
- Bell-orbit reduced-state purity \(1/2\);
- collinear-orbit separability/purity \(1\);
- Pauli projective representation;
- Pauli 2-cocycle law;
- non-surjective positive shift on \(\mathbb N\);
- invertible bilateral shift on \(\mathbb Z\).

See [QUANTUM_COPY_PRESSURE.md](QUANTUM_COPY_PRESSURE.md).

**Scope:** compatibility witness only; no fundamental-physics inference.

---

# 3. Refuted / narrowed formulations

## R1 — generic bidirectional control is a TLICA novelty

**Refuted as a novelty-shaped claim.**

Categorical optics, categorical cybernetics, Bayesian lenses, open games, and Structured Active Inference already provide mature compositional machinery.

---

## R2 — “Yoneda equivalent” without a bridge functor

**Refuted as an adequate theorem statement.**

Need explicit categories and:

\[
F:\mathsf T\to\mathsf O.
\]

---

## R3 — literal “optic + deviation” in arbitrary categories

**Refuted as generally typed.**

No additive structure is guaranteed.

Use parametrisation, a dependent pair, fiber, natural transformation, or declared additive enrichment.

---

## R4 — exact equivalence to an undecorated optic category plus irreducible Yoneda-visible extra TLICA structure at the same level

**Inconsistent framing.**

If the extra structure changes the full categorical profile, the undecorated target is too coarse.

---

## R5 — bare optics as the preferred external target

**Superseded.**

Primary-source pressure favors:

\[
\mathbf{Para}(\mathbf{Optic})
\]

/ categorical cybernetics as the stronger baseline.

---

# 4. Current conjectures

## C1 — Semantic Optics umbrella

A substantial cross-family set of TLICA phenomena can be factored into:

\[
\text{interface/arena}
+
\text{observer/controller semantics}
+
\text{feedback/update}.
\]

**UNVERIFIED across held-out domains.**

---

## C2 — TLICA as semantically constrained parametrised optics

Preferred moonshot:

\[
\boxed{
\mathsf{TLICAOptics}
\stackrel{?}{\simeq}
\mathsf{CyberOptics}^{\mathrm{TLICA}}
\subseteq
\mathbf{Para}(\mathbf{Optic}).
}
\]

No bridge functor yet.

---

## C3 — TLICA-specific residue

Candidate nonredundant structure:

- source-map semantics;
- probe availability / toolkit closure;
- toolkit-relative truth-indistinguishability/pathway state;
- identity/commitment coupling;
- focus/history/context;
- strict non-collapse rules among those diagnostics.

**UNVERIFIED against generic categorical-cybernetic baselines.**

---

## C4 — restricted Yoneda as probe adequacy bridge

A restricted nerve may formalize one family of toolkit-relative indistinguishability and “lamp” discovery.

**Conjectured bridge.**

Explicitly:

\[
\mu\neq\text{density},
\]

\[
\phi\neq\text{Yoneda profile}.
\]

---

# 5. The exact “Categorical Optics + TLICA deviation” status

The safe current formulation is:

\[
\widetilde\omega_\Theta
\in
\mathbf{Para}_\Theta(\mathbf{Optic}).
\]

A coarser projection forgets some TLICA semantics:

\[
\mathsf{TCO}
\xrightarrow{U}
\mathsf{CO}
\xrightarrow{V}
\mathsf O.
\]

Then “TLICA deviation” means structure lost under \(U\), not an unexplained additive scalar.

Three cases remain:

### Gauge / reparametrisation

The difference is categorically redundant.

### Real but currently probe-invisible

Full Yoneda distinguishes it; current restricted probe nerve does not.

### Currently probe-visible

The distinction should affect operative modeling now.

This is the strongest current version of the user's proposed decomposition.

---

# 6. Next proof that would materially change status

The highest-value next artifact is an independently specified finite category:

\[
\mathsf T_{\mathrm{toy}}
\]

plus:

\[
F:
\mathsf T_{\mathrm{toy}}
\to
\mathbf{Para}(\mathbf{Optic})_{\mathrm{toy}}.
\]

Then exhaustively compute:

- identities;
- composition;
- fullness;
- faithfulness;
- essential image;
- restricted nerves;
- reparametrisations.

A positive full/faithful result would upgrade the granularized-instantiation hypothesis.

A minimal obstruction would identify precisely which TLICA structure categorical cybernetics does not carry.

---

# 7. Current verdict

\[
\boxed{
\textbf{The moonshot survived, but in a narrower and more rigorous form.}
}
\]

Not:

\[
\text{TLICA}=\text{Category Theory}.
\]

Not:

\[
\text{TLICA Optics}=\text{bare optics}.
\]

Current target:

\[
\boxed{
\text{TLICA Semantic Optics}
\stackrel{?}{=}
\text{a semantically constrained region/refinement of parametrised categorical optics}
}
\]

with Yoneda/density supplying a possible theorem language for **what the available probe family can and cannot determine**.

That is the live program.
