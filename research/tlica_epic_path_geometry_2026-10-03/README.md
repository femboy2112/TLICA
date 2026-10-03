# TLICA–EPIC
## Typed inferential geometry for identity-correlation systems

> ## Current standard — v0.5.1
>
> Start here:
>
> 1. [**Quickstart v0.5.1**](QUICKSTART_v0.5.1.md) — five questions and the 30-second read order.
> 2. [**Visual Reading Guide v0.5.1**](VISUAL_GUIDE_v0.5.1.md) — progressive-disclosure diagrams and the simplified dryer example.
> 3. [**TLICA–EPIC v0.5.1 Master**](TLICA_EPIC_v0.5.1_MASTER.md) — complete denotational standard and reference reader.
> 4. [**Claude Fable v0.5.0 intake**](TLICA_EPIC_v0.5.0_MASTER.md) — preserved source snapshot before the readability pass.
>
> v0.1–v0.4 files below remain derivational history. The v0.5 line changes the diagram standard from topology-only notation to a denotational/counting shorthand.


**Date:** 2026-10-03  
**Branch:** research/tlica-epic-path-geometry-2026-10-03  
**Base:** 821ce7e6f57524d32e767a9c5ec5303e1796115e  
**Status:** research-tier, application-grade formal synthesis with isolated foundation-extension candidates.  
**Foundation impact:** **none on this branch.** No frozen-foundation file is modified.  
**Author:** Leah. AI-assisted formalization, notation audit, and repository reconciliation.  
**Related live provenance:** the 2026-10-03 affective-epistemic-compression branch, especially the distinction between felt resolution and executed discrimination.  
**Claim discipline:** mathematical constructions are separated from human mechanism claims; no novelty claim is made.

---

## 0. Cold-start thesis

TLICA already separates several things ordinary reasoning tends to collapse:

- contact \(\kappa\);
- toolkit-relative truth-indistinguishability \(\phi\);
- identity-correlation \(\rho\);
- source-map adequacy \(\sigma\) as a separate diagnostic rather than a fourth foundation coordinate;
- probe availability and toolkit closure;
- independence, coherence, and discrimination.

TLICA–EPIC asks what geometry appears when those distinctions are treated as a **typed path system**.

The central object is not “the argument that proves a hypothesis.” It is the family of candidate states that remain indistinguishable under the probes that are actually constructible, available, and executed.

For a candidate space \(X\) and an executed probe family \(Q\), define the joint observation map

$$
\eta_Q:X\to Y_Q.
$$

The surviving ambiguity around \(x\in X\) is the fiber

$$
\boxed{
\mathcal F_Q(x)
=
\eta_Q^{-1}\!\bigl(\eta_Q(x)\bigr).
}
$$

When smooth structure is available, the local unresolved directions are

$$
\boxed{
\mathcal K_Q(x)
=
\ker d\eta_{Q,x}.
}
$$

TLICA–EPIC therefore treats epistemic reconstruction as the controlled contraction of fibers under discriminating probes, while keeping model adequacy, source adequacy, identity coupling, and felt resolution separate.

The compact rule is:

$$
\boxed{
\text{no path count without provenance;}
\quad
\text{no }\phi\text{ update without a pathway;}
\quad
\text{no phase without transport;}
\quad
\text{no certainty without adequacy.}
}
$$

---

# Part I — Notation firewall

## 1. Correcting the first visual sketch

The first visual sketch used convenient but noncanonical labels such as “A-layer,” “B-layer,” \(\phi\) for phenomenological trace, and \(\mu\) for slack. Those are useful doodle-level intuitions but are **not acceptable canonical TLICA notation**.

This document fixes them.

### 1.1 The actual TLICA two-layer distinction remains untouched

TLICA’s two layers are the **intrinsic** and **asymptotic** layers. Mode A, Mode B, and Mode C are developmental/operational response-types inside the architecture; they are not the two layers.

See the [foundation reading guide](../../foundation/0_reading_guide.md).

Accordingly, this document uses **stratum** or **channel** for diagram layout and reserves *layer* for TLICA’s own architectural distinction.

### 1.2 \(\phi\) remains truth-indistinguishability

A phenomenological or observed trace is written \(y_t\), \(o_t\), or another local data symbol.

It is **never** written \(\phi_t\) merely for visual convenience.

### 1.3 \(S\) and \(\mu\) are not the same quantity

The foundation’s slack apparatus is written schematically as a margin \(S\).

TLICA–EPIC uses

$$
\mu_t(q)\in[0,1]
$$

only as an **application-level probe-availability / probe-weighting variable** for candidate probe \(q\).

A proposed bridge

$$
S_t\downarrow
\quad\Longrightarrow\quad
\mu_t(q)\downarrow
$$

may be tested in a declared regime, but it is **not an identity** and is not a foundation theorem.

### 1.4 \(G\) remains the lived-I structure

The current dynamical foundation reserves \(G\) for the slow lived-I structure rewritten by imprinting/Mode-B dynamics, with readings such as

$$
\rho=R(G),
\qquad
f=F(G,\cdot).
$$

TLICA–EPIC therefore does **not** reuse \(G\) for an information matrix.

Its correlation-corrected local resolution tensor is written

$$
\mathcal I_Q(x)
=
J_Q(x)^\top\Sigma_Q^{-1}J_Q(x).
$$

---

# Part II — Candidate states, pathways, and execution

## 2. Tool closure and pathway state

Let \(X\) be a declared space of candidate states, models, explanations, or ontic possibilities.

Let

$$
\mathrm{Tools}_t
$$

be the tools presently possessed by the agent/system, and let

$$
\mathrm{Cl}(\mathrm{Tools}_t)
$$

be the closure of probe constructions reachable from those tools under the allowed composition rules.

A probe \(q\) may occupy at least three distinct statuses:

1. **constructible**
   $$
   q\in \mathrm{Cl}(\mathrm{Tools}_t);
   $$

2. **effectively available**
   $$
   \mu_t(q)>0;
   $$

3. **executed**
   $$
   q\in Q_t^{\mathrm{exec}}.
   $$

These are not interchangeable.

The existence of a pathway does not provide its result.

The result of an executed probe does not imply that all constructible rivals were tested.

And felt certainty does not imply either constructibility or execution.

---

## 3. Total observation map

For each executed probe

$$
q_i:X\to Y_i,
$$

define

$$
\eta_Q(x)
=
\bigl(q_i(x)\bigr)_{q_i\in Q}.
$$

Then

$$
x\sim_Q x'
\iff
\eta_Q(x)=\eta_Q(x').
$$

The corresponding equivalence class is exactly the ambiguity fiber

$$
\mathcal F_Q(x)
=
[x]_Q.
$$

This is a **model-relative indistinguishability class**.

It is not a metaphysical identity claim.

---

## 4. Probe monotonicity theorem

### Proposition 4.1 — richer executed probe families cannot enlarge exact ambiguity

Let

$$
Q_1\subseteq Q_2
$$

and suppose \(\eta_{Q_2}\) contains all outputs of \(\eta_{Q_1}\) plus the additional \(Q_2\setminus Q_1\) outputs.

Then for every \(x\in X\),

$$
\boxed{
\mathcal F_{Q_2}(x)
\subseteq
\mathcal F_{Q_1}(x).
}
$$

### Proof

If \(x'\in\mathcal F_{Q_2}(x)\), then every probe in \(Q_2\) gives the same output on \(x'\) and \(x\). Since \(Q_1\subseteq Q_2\), every probe in \(Q_1\) also agrees. Hence

$$
x'\in\mathcal F_{Q_1}(x).
$$

Therefore

$$
\mathcal F_{Q_2}(x)\subseteq\mathcal F_{Q_1}(x).
\qquad\square
$$

### Interpretation

The theorem licenses:

$$
Q^{\mathrm{exec}}\text{ shrinks}
\quad\Longrightarrow\quad
\text{exact ambiguity can only stay the same or grow}.
$$

It does **not** license

$$
S\downarrow\Longrightarrow Q^{\mathrm{exec}}\downarrow
$$

as a universal psychological law.

That bridge remains application-level and must be tested.

---

## 5. Differential ambiguity

When \(X\) and \(Y_Q\) are smooth enough,

$$
d\eta_{Q,x}:T_xX\to T_{\eta_Q(x)}Y_Q.
$$

Define

$$
\boxed{
\mathcal K_Q(x)
=
\ker d\eta_{Q,x}.
}
$$

A tangent vector

$$
v\in\mathcal K_Q(x)
$$

is a first-order direction along which the candidate state can move without changing any currently executed probe output to first order.

Thus:

$$
\boxed{
\text{global ambiguity}=\mathcal F_Q(x),
\qquad
\text{local dark directions}=\mathcal K_Q(x).
}
$$

Local distinguishability and global uniqueness remain separate.

---

## 6. Correlation-corrected local resolution

Let \(J_Q(x)\) be the stacked Jacobian of the probes in \(Q\).

Let \(\Sigma_Q\) be their positive-definite joint noise/dependence covariance.

Define

$$
\boxed{
\mathcal I_Q(x)
=
J_Q(x)^\top\Sigma_Q^{-1}J_Q(x).
}
$$

Then

$$
v^\top\mathcal I_Q(x)v
=
(J_Qv)^\top\Sigma_Q^{-1}(J_Qv),
$$

so

$$
\boxed{
\ker\mathcal I_Q(x)
=
\ker J_Q(x)
=
\mathcal K_Q(x)
}
$$

when \(\Sigma_Q\) is positive definite.

The least-resolved eigenvector of \(\mathcal I_Q\) is therefore a natural target for a new discriminator.

A maximin probe-design rule is

$$
q^\ast
=
\arg\max_q
\lambda_{\min}
\left(
\mathcal I_Q+\Delta\mathcal I_q
\right).
$$

In plain terms:

> aim the next probe at the darkest surviving direction, not at the hypothesis you already know how to confirm.

---

# Part III — TLICA-native diagram grammar

## 7. Master orientation rule

The primary visual rule is:

$$
\boxed{
\text{an arrow points toward the object being updated, not merely toward what occurs later in time.}
}
$$

Temporal succession may be shown, but it is never the default semantics of an edge.

Every serious diagram must type its arrows.

---

## 8. Node classes

| Symbol | Meaning | TLICA status |
|---|---|---|
| \(x_t\) | candidate world/model state | application object |
| \(y_t\) | observed / phenomenological trace | application object |
| \(G_t\) | slow lived-I structure | foundation dynamical object |
| \(P_t\) | identity-correlation profile | foundation object |
| \(\rho\) | identity-correlation reading | foundation coordinate |
| \(\kappa\) | contact | foundation coordinate |
| \(\phi\) | toolkit-relative truth-indistinguishability | foundation coordinate/status apparatus |
| \(\sigma\) | source-map adequacy diagnostic | separate diagnostic, not a fourth coordinate |
| \(S_t\) | slack margin | foundation dynamical apparatus |
| \(\mu_t(q)\) | availability/weight of probe \(q\) | application/research diagnostic |
| \(Q_t^{\mathrm{exec}}\) | actually executed probe family | application/research object |
| \(H_t\) | live rival/candidate set | application object |
| \(\pi_t\) | action policy | application object |
| \(a_t\) | action/intervention | application object |
| \(\omega_t\) | externally visible wake/record | application object |
| \(\widehat M_t^B\) | observer \(B\)'s reconstruction | application object |

---

## 9. Typed arrows

### 9.1 Generative / observation arrow

$$
x_t
\xrightarrow{\mathrm{obs}}
y_t
$$

means: the declared state produces or is sampled into a trace.

It is not itself an inference.

### 9.2 Imprinting/update arrow

$$
y_{\le t}
\xrightarrow{\mathrm{imp}}
G_{t+1}
$$

means: encountered structure contributes to an update of the slow lived-I structure under the declared imprinting mechanism.

Use this arrow only where TLICA's imprinting apparatus is actually intended.

### 9.3 Mode-B reflexive arrow

$$
G_t
\xrightarrow{B}
G_{t+1}
$$

means: self-directed/reflexive operation rewrites the lived-I structure.

Mode B is **not** a generic synonym for “careful thinking.”

### 9.4 Probe arrow

$$
H_t
\xrightarrow{q!}
H_{t+1}
$$

means: probe \(q\) was executed and its outcome removed or distinguished candidates.

A dashed \(q?\) means “constructible or contemplated but not yet executed.”

### 9.5 Gating arrow

$$
S_t\dashv \mu_t(q)
$$

or another declared gating relation means one quantity modulates access/weighting of another.

The edge must be labeled **CONJECTURED** unless the relation is derived or directly measured.

### 9.6 Policy arrow

$$
(\widehat x_t,G_t,\ldots)
\xrightarrow{\pi}
a_t
$$

means: the current represented state contributes to action selection.

### 9.7 Wake projection

$$
a_t
\xmapsto{\mathrm{wake}}
\omega_t
$$

means: action leaves an externally observable record.

### 9.8 Lossy reconstruction

$$
\omega_{\le t}
\rightsquigarrow_B
\widehat M_t^B
$$

means: observer \(B\) reconstructs an internal/external model from a partial record.

This is explicitly **not** direct mind-to-mind transfer.

---

## 10. Loops: three different objects

TLICA–EPIC forbids drawing an unlabeled loop.

### Dynamical feedback

A later system state feeds back into an earlier variable class.

### Transport holonomy

If a transport law \(T_\gamma\) is defined, a closed path \(\ell\) can carry

$$
\mathrm{Hol}(\ell)=T_\ell.
$$

Nonidentity holonomy means the transported object depends on route.

### Feynman loop

A perturbative internal contraction in a Gaussian expansion is a different object again.

These three loop types may coexist, but they are not interchangeable.

---

# Part IV — Path calculus

## 11. Inferential path category

Let \(\mathcal E\) be a directed multigraph of admissible epistemic states and operations.

The free category

$$
\mathrm{Path}(\mathcal E)
$$

has epistemic states as objects and composable inferential/probing histories as morphisms.

A route

$$
\gamma:E\to A
$$

can include observations, transformations, probe executions, source transfers, or model updates.

The category itself carries no truth guarantee. It is bookkeeping for admissible routes.

---

## 12. Provenance map

Define a primitive-source ancestry map

$$
\Pi(\gamma).
$$

Two paths that look rhetorically different may have heavily overlapping ancestry.

Therefore:

$$
\boxed{
\text{path multiplicity}\neq\text{independent evidence}.
}
$$

If

$$
y=h(x)+Bu+\varepsilon,
$$

with shared latent source error \(u\) and independent noise \(\varepsilon\), then

$$
\Sigma
=
D+BCB^\top.
$$

Shared provenance is therefore naturally visible as covariance.

For the scalar special case

$$
y_i=x+b+\varepsilon_i,
$$

with

$$
b\sim N(0,\tau^2),
\qquad
\varepsilon_i\sim N(0,\sigma^2),
$$

the information is

$$
I_n
=
\frac{n}{\sigma^2+n\tau^2}
=
\frac{1}{\tau^2+\sigma^2/n},
$$

so

$$
\lim_{n\to\infty} I_n
=
\frac1{\tau^2}.
$$

Infinitely many descendants of one biased source do not produce infinite independent information.

---

## 13. Discrete path sum

For a finite path system with edge weights \(w(e)\), define

$$
w(\gamma)
=
\prod_{e\in\gamma}w(e)
$$

and

$$
Z(A\mid E)
=
\sum_{\gamma:E\to A}
w(\gamma).
$$

If all weights are nonnegative, this is **aggregation**, not destructive interference.

For a cyclic finite system, a discounted transfer matrix \(K\) gives

$$
I+\lambda K+\lambda^2K^2+\cdots
=
(I-\lambda K)^{-1}
$$

whenever

$$
|\lambda|<\rho(K)^{-1}.
$$

The relevant matrix entry sums weighted walks between endpoints.

---

## 14. Continuous path measure

Let \(\Gamma\) be a declared path space with base measure \(\mu_0\).

Let \(\Phi(E,\gamma)\) be an evidence misfit/action functional.

Define

$$
\frac{d\mu_E}{d\mu_0}(\gamma)
=
\frac1Z
e^{-\Phi(E,\gamma)},
$$

where

$$
Z
=
\int_\Gamma
e^{-\Phi(E,\gamma)}
\,d\mu_0(\gamma).
$$

Pushing this measure through the endpoint map yields a distribution over candidate endpoints.

This is a legitimate path-integral construction **once the path space, base measure, and action are declared**.

It is model-relative evidence aggregation, not a metaphysical truth probability.

---

## 15. When Feynman diagrams are literal bookkeeping

Suppose the baseline path/latent measure is Gaussian with covariance \(C\), and a nonlinear interaction \(V[\psi]\) is introduced:

$$
Z(\lambda)
=
Z_0
\mathbb E_0
\left[
e^{-\lambda V[\psi]}
\right].
$$

Expanding,

$$
Z(\lambda)
=
Z_0
\sum_{n=0}^\infty
\frac{(-\lambda)^n}{n!}
\mathbb E_0[V[\psi]^n].
$$

Wick contraction decomposes Gaussian moments into pairings, each carrying covariance \(C\).

At that point Feynman diagrams are **literally valid combinatorial bookkeeping** for the perturbation series.

No quantum interpretation follows.

---

## 16. Three meanings of “interference”

### Positive aggregation

If \(w(\gamma)\ge0\), paths add. No destructive interference exists.

### Möbius interaction

For evidence-family statistic \(F(S)\),

$$
\widehat F(S)
=
\sum_{T\subseteq S}
(-1)^{|S|-|T|}
F(T)
$$

isolates higher-order interaction on the subset lattice.

### Genuine phase interference

A phase sum is licensed only when paths carry a declared compositional phase/character

$$
\chi(\gamma_2\circ\gamma_1)
=
\chi(\gamma_2)\chi(\gamma_1).
$$

Only then may one write

$$
\mathcal A(A)
=
\sum_{\gamma:E\to A}
a(\gamma)\chi(\gamma).
$$

Hence:

$$
\boxed{
\text{no declared transport, no phase.}
}
$$

---

# Part V — TLICA reconciliation

## 17. \(\kappa\): contact

\(\kappa\) records contact, not correct causal attribution.

A damp garment, a manager statement, or a visible action can be in direct contact while the source explanation remains ambiguous.

## 18. \(\phi\): toolkit-relative truth-indistinguishability

TLICA–EPIC sharpens three pathway states:

$$
\text{constructible}
\neq
\text{available}
\neq
\text{executed}.
$$

If no constructible route exists inside the declared tool closure, the relevant \(\phi\)-assessment may be undefined rather than false.

If a route exists but is not executed, no result has been earned merely because the agent “could check.”

## 19. \(\sigma\): source-map adequacy

Source-map adequacy remains separate from \(\phi\).

A model may fit all currently observed outputs while attributing them to the wrong generator.

Thus:

$$
\boxed{
\text{high coherence or high }\phi\text{ under a bad source map can still miss the cause.}
}
$$

## 20. \(\rho\): identity-correlation

\(\rho\) concerns integration into the lived-I structure.

It is not “confidence,” “anger,” “defensiveness,” or “epistemic weight.”

TLICA–EPIC therefore never adds \(\rho\) into a scalar truth score.

## 21. Slack \(S\), probe availability \(\mu\), and closure

The rigorous chain is split:

1. foundation/application state:
   $$
   S_t;
   $$

2. candidate bridge:
   $$
   S_t\downarrow
   \Longrightarrow
   \mu_t(q)\downarrow;
   $$

3. execution consequence:
   $$
   \mu_t(q)\downarrow
   \Longrightarrow
   Q_t^{\mathrm{exec}}\text{ may shrink};
   $$

4. disclosed geometric result:
   $$
   Q_t^{\mathrm{exec}}\text{ shrinks}
   \Longrightarrow
   \mathcal F_Q(x)\text{ can only stay equal or enlarge}.
   $$

Only the final implication is theorem-level under the stated model.

---

# Part VI — TLICA-native diagrams

## 22. Dryer / premature closure

The point is not which appliance claim is true. The point is the separation between trace, source-map commitment, felt resolution, and executed discrimination.

~~~mermaid
flowchart TB
    X["candidate substrate/world states X"]
    Y["observed trace y_t: clothes still damp"]
    H["live rivals H_t:<br/>H1 bad loading/running<br/>H2 load/heat/time concern valid<br/>H3 omitted cause"]
    C["current source-map commitment sigma_t:<br/>H1 feels obvious"]
    A["anger / urgency state"]
    S["foundation slack margin S_t"]
    MU["probe availability weights mu_t(q)"]
    CL["constructible closure Cl(Tools_t)<br/>manual, model no., load, cycle, heat"]
    QE["executed probes Q_exec"]
    F["ambiguity fiber F_Q(x)"]
    Q["execute discriminator q!"]
    R["revised survivor set"]

    X -->|obs| Y
    Y --> H
    H --> C
    C --> A
    A -. "CONJECTURED pressure bridge" .-> S
    S -. "CONJECTURED gating bridge" .-> MU
    CL --> MU
    MU --> QE
    QE --> F
    H --> Q
    CL --> Q
    Q --> R
    C -. "felt resolution may recur" .-> C
~~~

The phenomenological aliasing problem is:

$$
\text{successful discrimination}
\quad\text{and}\quad
\text{premature closure}
$$

can both produce the first-person state

$$
\text{“nothing left to think about.”}
$$

Therefore:

$$
\boxed{
\text{felt resolution}\neq\text{epistemic resolution}.
}
$$

---

## 23. Semantic wake / observer reconstruction

This extends the existing [Semantic Wake Drag](../semantic_wake_drag_2026-09-26/README.md) dossier without changing its foundation status.

~~~mermaid
flowchart TB
    M["actor model M_t"]
    PI["policy pi_t"]
    A["rapid action sequence a1,a2,a3,..."]
    W["externally visible wake omega_t"]
    OB["observer reconstruction map D_B"]
    F1["large reconstruction fiber<br/>many actor-models fit the same wake"]
    D1["semantic wake drag / misread risk"]

    H["semantic header h_t:<br/>goal + invariant + rationale + next move + boundary"]
    AUG["augmented record (omega_t,h_t)"]
    OB2["augmented reconstruction D'_B"]
    F2["smaller reconstruction fiber<br/>when h_t is actually informative"]
    D2["lower reconstruction ambiguity"]

    M --> PI
    PI --> A
    A -->|wake| W
    W --> OB
    OB --> F1
    F1 --> D1

    M --> H
    W --> AUG
    H --> AUG
    AUG --> OB2
    OB2 --> F2
    F2 --> D2
~~~

The crucial non-arrow is:

$$
M_t
\not\to
\widehat M_t^B
\quad\text{directly}.
$$

Instead,

$$
M_t
\to
a_t
\xmapsto{\mathrm{wake}}
\omega_t
\rightsquigarrow_B
\widehat M_t^B.
$$

More rapid action can therefore coexist with **less external identifiability** of the model generating it.

---

## 24. Training dilemma / hidden institutional objective

The underidentified object is the institution’s effective objective, not merely which policy feels morally or operationally preferable.

~~~mermaid
flowchart TB
    X["local operating state:<br/>staffing + backlog + norms + visibility"]
    Y["trace y_t:<br/>new staff + workload pressure"]
    H1["policy candidate pi1:<br/>canonical training"]
    H2["policy candidate pi2:<br/>realistic-flow training"]
    O1["fidelity up<br/>backlog risk up"]
    O2["throughput up<br/>shortcut visibility / sanction risk up"]
    J["hidden effective objective J_inst"]
    Q1["q1!: acceptable-performance envelope"]
    Q2["q2!: measured throughput-quality frontier"]
    Q3["q3!: manager response to documented edge cases"]
    R["reconstructed objective with reduced ambiguity"]

    X -->|obs| Y
    Y --> H1
    Y --> H2
    H1 --> O1
    H2 --> O2
    J -. "would determine tradeoff if known" .-> H1
    J -. "would determine tradeoff if known" .-> H2
    O1 --> Q1
    O2 --> Q2
    O1 --> Q3
    O2 --> Q3
    Q1 --> R
    Q2 --> R
    Q3 --> R
~~~

A useful schematic is

$$
J_{\mathrm{inst}}
=
J(
\text{quality},
\text{throughput},
\text{backlog},
\text{visibility},
\text{sanction risk},
\text{staffing}
).
$$

If the actual organization is multi-agent, inconsistent, time-varying, or strategically coupled, then assuming one stable scalar \(J_{\mathrm{inst}}\) is itself model misspecification.

---

# Part VII — Model adequacy and saturation

## 25. Identifiability is not adequacy

A candidate can be uniquely identified inside the wrong model class.

One may have

$$
\mathcal F_Q(x)=\{x\},
$$

yet reality may lie outside \(X\).

Thus:

$$
\boxed{
\text{identifiability}\neq\text{model adequacy}.
}
$$

TLICA–EPIC therefore requires a “neither / enlarge \(X\)” branch wherever a discriminator can refute the entire current rival family.

## 26. Contextual saturation

Given current tool closure,

$$
\mathrm{Cl}(\mathrm{Tools}_t),
$$

two candidates are contextually indistinguishable when every constructible probe in the declared closure fails to separate them.

If the remaining fiber contains multiple candidates and no known probe/source defect remains, the state is **contextually saturated**.

This means:

> no present discriminator reaches the distinction.

It does not mean:

> the distinction is metaphysically absent.

---

# Part VIII — Foundation-extension analysis

## 27. What is already application-level

The following can be used immediately without changing the foundation:

1. typed arrow grammar;
2. candidate fibers \(\mathcal F_Q\);
3. local kernels \(\mathcal K_Q\);
4. covariance/provenance correction;
5. source-map rival diagrams;
6. semantic-wake reconstruction;
7. probe-design rules;
8. path-sum bookkeeping;
9. perturbative/Feynman diagrammatics where mathematically licensed.

These are analytical instruments layered over existing TLICA commitments.

## 28. Candidate foundation extension A: pathway-state triplet

The strongest foundation-level candidate is not the path integral.

It is the explicit separation

$$
\boxed{
\text{constructible}
\neq
\text{available}
\neq
\text{executed}.
}
$$

TLICA already makes \(\phi\) toolkit-relative and application work already depends on probe availability.

A future foundation revision could decide whether this triplet belongs inside the formal account of verification access itself.

Promotion would require proving that the distinction resolves recurring ambiguities across multiple applications without collapsing into ordinary executive-function description.

## 29. Candidate foundation extension B: typed source-map discipline

The archive already uses \(\sigma\)/source-map adequacy as a separate diagnostic.

A foundation extension might standardize the rule:

$$
\phi\text{-resolution}
\quad\not\Rightarrow\quad
\sigma\text{-resolution}.
$$

That would not make \(\sigma\) a fourth coordinate.

It would formalize a recurrent methodological constraint:

> a proposition can survive current verification while its causal/source attribution remains underidentified.

## 30. Candidate foundation extension C: diagrammatic update semantics

The master arrow rule

$$
\text{arrow target}=\text{updated object}
$$

could become a notation standard rather than a metaphysical commitment.

Its value is error prevention:

- causation is not confused with inference;
- inference is not confused with imprinting;
- Mode B is not used as a synonym for deliberation;
- wake projection is not confused with observer reconstruction;
- feedback is not confused with holonomy.

This is likely **documentation/foundational-notation** material before it is theory.

## 31. What should not be promoted to foundation now

The following are powerful but currently belong outside the core:

- the EPIC acronym itself;
- a universal epistemic action \(S[\gamma]\);
- one canonical path-integral weighting;
- Feynman diagrammatics;
- a universal information tensor;
- semantic-wake variables;
- the dryer-specific affective mechanism;
- the training-objective model;
- any scalar “truth score.”

These are domain tools or research candidates, not demonstrated universal architecture.

---

# Part IX — Promotion gate

## 32. Foundation-extension acceptance criteria

A TLICA–EPIC object should be considered for a future foundation release only if it survives all of the following.

### Gate F1 — no coordinate collapse

It must preserve the independence and roles of

$$
\kappa,\phi,\rho
$$

and must not smuggle \(\sigma,\mu,S\), coherence, or confidence into them.

### Gate F2 — cross-application necessity

The object must solve the same structural problem in at least three substantially different applications.

### Gate F3 — existing-machinery ablation

Remove the candidate extension and demonstrate what cannot be represented cleanly with current foundation machinery.

If nothing breaks, the extension is documentation, not foundation.

### Gate F4 — adversarial rival formulation

Construct a simpler rival formalism and a discriminating case.

### Gate F5 — source/provenance audit

Show that apparent cross-application support is not three restatements of the same originating intuition.

### Gate F6 — holdout

Apply the formalism to a case not used to design it.

### Gate F7 — notation audit

No collision with existing foundation symbols or architectural terms.

### Gate F8 — falsifier

State what observation, counterexample, or derivation would kill the proposed extension.

Only after those gates should a foundation patch be considered.

---

# Part X — Minimal computational object

## 33. Finite TLICA–EPIC instance

A finite implementation may use

$$
\boxed{
\mathfrak E
=
(
X,
\mathrm{Tools},
\mathrm{Cl},
Q^{\mathrm{exec}},
\eta,
\Pi,
\Sigma,
T,
W
)
}
$$

with:

- \(X\): candidate state/model space;
- \(\mathrm{Tools}\): primitive tools;
- \(\mathrm{Cl}\): tool-closure rule;
- \(Q^{\mathrm{exec}}\): executed probe family;
- \(\eta\): total observation map;
- \(\Pi\): provenance ancestry;
- \(\Sigma\): dependence/noise structure;
- \(T\): optional transport operators;
- \(W\): optional path weights.

It can compute:

1. ambiguity fibers;
2. local kernels;
3. correlation-corrected resolution;
4. provenance overlap;
5. path defects;
6. loop holonomy when transport is defined;
7. candidate-splitting power of proposed probes;
8. positive path sums;
9. Möbius interaction terms;
10. perturbative diagram contributions when a Gaussian/interacting model is declared.

---

# Part XI — Claim status

## 34. Disclosed under stated mathematics

- \(\mathcal F_Q(x)\) is the exact model-relative ambiguity class induced by \(Q\);
- richer executed probe families weakly shrink exact fibers;
- \(\mathcal K_Q(x)=\ker d\eta_{Q,x}\) gives first-order invisible directions;
- \(\mathcal I_Q=J^\top\Sigma^{-1}J\) shares that nullspace when \(\Sigma\) is positive definite;
- shared provenance can limit information gain;
- path composition forms a category;
- holonomy requires a declared transport;
- Gaussian perturbation expansions admit Wick/Feynman bookkeeping;
- genuine phase cancellation requires operational phase transport.

## 35. Observed / author-report level

- the motivating dryer episode exposed a difference between felt obviousness and an actually executed local discriminator;
- the high-frequency-pulse / semantic-wake phenomenon is part of the author’s reported phenomenology.

## 36. Conjectured / UNVERIFIED human mechanisms

- anger reliably lowers relevant slack;
- lower slack reliably suppresses probe availability or execution;
- semantic headers reliably shrink observer reconstruction fibers in real social systems;
- the proposed training probes recover a stable institutional objective;
- the same typed geometry yields measurable predictive gain across human domains.

These require external probes.

---

# 37. Final compression

TLICA–EPIC is best understood as:

$$
\boxed{
\textbf{the geometry of distinguishability under path-, source-, and identity-aware evidence.}
}
$$

Its TLICA-specific contribution is not “quantum epistemology.”

It is the disciplined composition

$$
\boxed{
\mathrm{Cl}(\mathrm{Tools})
\to
\mu
\to
Q^{\mathrm{exec}}
\to
\eta_Q
\to
\mathcal F_Q,\mathcal K_Q
}
$$

kept orthogonal to

$$
\boxed{
\kappa,\phi,\rho,\sigma,S,G
}
$$

except where a declared bridge is actually justified.

And its diagrammatic rule is deliberately severe:

> **Every arrow must say what is being updated and by what operation. If the arrow cannot be typed, the diagram is hiding an inference.**

That makes the Feynman joke useful rather than mystical.

The point is not that truth is a quantum amplitude.

The point is that an inaccessible state can be reconstructed only through the structured family of paths, probes, sources, transports, and residual ambiguities that reach it—and the geometry of what those paths still fail to distinguish is itself mathematically inspectable.

---

# 38. Dual-pass structured-point formalism

The diagram language is now extended by a dedicated folded round-trip formalism:

- [**Dual-Pass Structured-Point Formalism**](DUAL_PASS_STRUCTURED_POINTS.md) — formalizes the canonical
  (W\to S\to I\to S\to W) cycle; separates inbound reconstruction from outbound realization;
  treats each diagram point as a structured shell/core object; defines coupled outer EPIC and inner
  TLICA graphs, commuting shell/core squares, compatibility defects, inner lifts of outer paths,
  zoom-equivalent effective vertices, and the L0/L1/L2 diagram hierarchy.

The load-bearing visual compression is:

$$
\boxed{
\text{horizontal position = world/substrate/self;}
\quad
\text{vertical lane = inbound/outbound;}
\quad
\text{radial depth = EPIC shell/TLICA core.}
}
$$

The return leg is later-time realization, **not** an inverse or time reversal of the inbound leg.

---

# 39. Canonical diagram standard

The visual grammar has been simplified again after comparing it directly against the economy of ordinary Feynman diagrams.

The canonical standard is now:

- [**TLICA–EPIC Diagram Standard**](DIAGRAM_STANDARD.md) — ordinary directed wires plus two vertex resolutions:
  atomic points and recursively expandable EPIC-integrated circuit nodes.

The critical correction is:

$$
\boxed{
\text{wires are wires;}
\qquad
\text{the extra structure lives in the nodes.}
}
$$

The previous parallel outer-EPIC / inner-TLICA edge treatment is retained only as derivational history in
[DUAL_PASS_STRUCTURED_POINTS.md](DUAL_PASS_STRUCTURED_POINTS.md).

The canonical agent-cycle layout remains

$$
W_t\to S_t\to I_t\to I_t^+\to S_{t+1}\to W_{t+1},
$$

but internal TLICA machinery is now exposed by **expanding a vertex**, not by drawing a second trace beside every wire.
