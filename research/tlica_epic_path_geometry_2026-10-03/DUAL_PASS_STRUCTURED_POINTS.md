> **Superseded diagram grammar (2026-10-03).** The useful two-pass world → substrate → self → substrate → world dynamics remain, but the parallel “outer EPIC trace / inner TLICA trace” edge grammar in this file has been simplified. The current canonical standard is [DIAGRAM_STANDARD.md](DIAGRAM_STANDARD.md): **wires remain ordinary wires; vertices may be atomic points or recursively expandable EPIC-integrated circuits.** This file is retained as derivational history for the two-pass idea and its shell/core motivation.

# TLICA–EPIC Dual-Pass Structured-Point Formalism
## World → substrate → self → substrate → world

**Date:** 2026-10-03  
**Status:** research-tier formal extension of TLICA–EPIC diagrammatics.  
**Foundation impact:** none on this branch. The construction is an application/research formalism and notation candidate, not a frozen-foundation mutation.  
**Depends on:** [TLICA–EPIC main note](README.md), [Claim Ledger](CLAIM_LEDGER.md), and the current TLICA foundation on \`main\`.  
**Author:** Leah. AI-assisted formalization and notation audit.

---

# 0. Thesis

The canonical TLICA–EPIC diagram should not be a one-way flowchart.

The phenomenological and dynamical picture is a **causally ordered round trip**:

$$
\boxed{
W_t
\longrightarrow
S_t
\longrightarrow
I_t
\;\curvearrowright\;
I_t^+
\longrightarrow
S_{t+1}
\longrightarrow
W_{t+1}.
}
$$

Read it as:

1. **reconstruction / uptake**
   $$
   W_t\to S_t\to I_t;
   $$

2. **internal transformation**
   $$
   I_t\to I_t^+;
   $$

3. **realization / action**
   $$
   I_t^+\to S_{t+1}\to W_{t+1}.
   $$

The return leg is **not time reversal** and is generally **not an inverse map** of the inbound leg.

The same macroscopic point-object may participate in two distinct geometries:

- an **outer EPIC shell geometry** connecting whole objects;
- an **inner TLICA core geometry** connecting their internal state structure.

The resulting diagram is best understood as a **circuit inside a circuit**.

---

# 1. Primitive macroscopic stations

Use three canonical macroscopic stations:

$$
W=\text{world / local external field},
$$

$$
S=\text{substrate / embodied transduction layer},
$$

$$
I=\text{lived-I / self structure}.
$$

The labels are deliberately schematic.

They do not imply that the world, substrate, or self is internally simple.

Each is a **structured point-object** that may be collapsed to a glyph at one zoom level and expanded into an internal circuit at another.

---

# 2. Two passes, not one bidirectional channel

## 2.1 Inbound pass: reconstruction / uptake

Define

$$
\mathcal T_t^{\mathrm{in}}
:
(W_t,S_t,I_t)
\mapsto
(W_t,S_t^+,I_t^+)
$$

through maps such as

$$
\alpha_t:W_t\to S_t^+,
$$

$$
\beta_t:S_t^+\to I_t^+.
$$

Interpretation:

- \(\alpha_t\): world-to-substrate contact/transduction;
- \(\beta_t\): substrate-mediated uptake into the lived-I/self model.

This is the direction in which external constraint becomes internally available structure.

## 2.2 Outbound pass: realization / action

Define

$$
\mathcal T_t^{\mathrm{out}}
:
(W_t,S_t^+,I_t^+)
\mapsto
(W_{t+1},S_{t+1},I_t^+)
$$

through maps such as

$$
\gamma_t:I_t^+\to S_{t+1},
$$

$$
\delta_t:S_{t+1}\to W_{t+1}.
$$

Interpretation:

- \(\gamma_t\): policy/control realization into the substrate;
- \(\delta_t\): substrate-mediated action changing the local world.

The full cycle is

$$
\boxed{
\mathcal T_t
=
\mathcal T_t^{\mathrm{out}}
\circ
\mathcal T_t^{\mathrm{in}}.
}
$$

Thus

$$
(W_t,S_t,I_t)
\xmapsto{\mathcal T_t}
(W_{t+1},S_{t+1},I_t^+).
$$

---

# 3. No inverse fallacy

The visual reversal of direction must never be read as algebraic inversion.

In general,

$$
\boxed{
\gamma_t\neq\beta_t^{-1},
\qquad
\delta_t\neq\alpha_t^{-1}.
}
$$

Perception is not simply replayed backward to become action.

The two families of maps have different semantics:

$$
\mathsf R
=
\{\text{reconstructive / uptake maps}\},
$$

$$
\mathsf A
=
\{\text{realizational / control maps}\}.
$$

A diagram may place \(\mathsf R\) on the upper lane and \(\mathsf A\) on the lower lane.

Opposite orientation means **opposite causal role**, not inverse morphism.

---

# 4. The substrate is a stateful transducer

The substrate must not be drawn as an inert wire.

Let \(s_t\) denote substrate state.

Inbound transduction may update it:

$$
s_t^+
=
U_S^{\mathrm{in}}(s_t,w_t).
$$

The lived-I/self structure may then update under the substrate-mediated trace:

$$
G_t^+
=
U_I(G_t,s_t^+).
$$

A policy/readout is selected:

$$
u_t
=
\Pi(G_t^+,s_t^+).
$$

Outbound realization updates the substrate again:

$$
s_{t+1}
=
U_S^{\mathrm{out}}(s_t^+,u_t).
$$

Then the world transition is

$$
w_{t+1}
=
U_W(w_t,s_{t+1}).
$$

Therefore the same substrate point participates in both passes while carrying state across them.

---

# 5. Structured point-objects

## 5.1 Definition

For each vertex \(v\), define a structured point-object

$$
\boxed{
\mathbb V_v
=
(X_v,Z_v,c_v,e_v,\Theta_v).
}
$$

Where:

- \(X_v\): shell/interface state;
- \(Z_v\): internal/core state;
- \(c_v:X_v\to Z_v\): shell-to-core uptake map;
- \(e_v:Z_v\to X_v\): core-to-shell realization map;
- \(\Theta_v\): local internal dynamics.

The same object can be drawn compactly as

$$
\mathbb V_v\;\equiv\;\odot
$$

or expanded into its core circuit.

## 5.2 Shell and core are not ontological substances

“Shell” and “core” are diagrammatic roles.

They mean:

- shell = interface visible to the external path calculus at the chosen scale;
- core = internal structure retained at the chosen scale.

Changing scale may move structure from core to shell or vice versa.

This is a modeling decomposition, not a metaphysical dualism.

---

# 6. Two graphs on the same vertices

Let

$$
V=\{v_1,\ldots,v_n\}
$$

be the shared vertex set.

Define two coupled edge systems.

## 6.1 Outer EPIC graph

Let

$$
\mathcal G_{\mathrm{out}}
=
(V,E_{\mathrm{out}})
$$

with each edge

$$
e:u\to v
$$

carrying an outer-shell map

$$
P_e:X_u\to X_v.
$$

This graph carries:

- whole-object observational routes;
- source/provenance paths;
- external state transitions;
- path-sum bookkeeping;
- candidate reconstruction paths.

## 6.2 Inner TLICA graph

Let

$$
\mathcal G_{\mathrm{in}}
=
(V,E_{\mathrm{in}})
$$

with each corresponding internal edge carrying

$$
T_e:Z_u\to Z_v.
$$

This graph carries internal state transport/update at the modeled resolution.

The two graphs share point-objects but not necessarily identical edge sets.

An outer path may fail to possess a compatible inner realization.

---

# 7. Inbound shell/core compatibility

For an inbound edge

$$
e:u\to v,
$$

the ideal compatibility square is

$$
\boxed{
c_v\circ P_e
=
T_e\circ c_u.
}
$$

Diagrammatically:

$$
\begin{array}{ccc}
X_u & \xrightarrow{P_e} & X_v\\
\downarrow c_u && \downarrow c_v\\
Z_u & \xrightarrow{T_e} & Z_v
\end{array}
$$

Interpretation:

> transporting the whole object and then resolving its internal state agrees with resolving first and transporting the internal structure.

This is a cross-level coherence condition.

---

# 8. Outbound shell/core compatibility

For an outbound edge

$$
\bar e:v\to u,
$$

the corresponding ideal square is

$$
\boxed{
P_{\bar e}\circ e_v
=
e_u\circ T_{\bar e}.
}
$$

Diagrammatically:

$$
\begin{array}{ccc}
Z_v & \xrightarrow{T_{\bar e}} & Z_u\\
\downarrow e_v && \downarrow e_u\\
X_v & \xrightarrow{P_{\bar e}} & X_u.
\end{array}
$$

Interpretation:

> internally realized change, when exposed at the shell, agrees with the whole-object outbound path.

Inbound and outbound compatibility have parallel form but different semantics.

---

# 9. Compatibility defects

Exact commutation may be too strong in noisy, approximate, or lossy settings.

Let \(d\) be an appropriate metric or discrepancy functional.

Define inbound defect

$$
\boxed{
\Delta_e^{\mathrm{in}}
=
d\!\left(
c_vP_e,
T_ec_u
\right).
}
$$

Define outbound defect

$$
\boxed{
\Delta_{\bar e}^{\mathrm{out}}
=
d\!\left(
P_{\bar e}e_v,
e_uT_{\bar e}
\right).
}
$$

Then:

- \(\Delta=0\): exact cross-level coherence;
- small \(\Delta\): approximate compatibility;
- large \(\Delta\): the outer EPIC account and inner TLICA account disagree at that interface.

The defect is diagnostic.

It does not by itself tell us which side is wrong.

---

# 10. Edgewise coherence implies pathwise coherence

## Proposition 10.1

Let

$$
\gamma
=
e_n\circ\cdots\circ e_1
$$

be an inbound path.

Define

$$
P_\gamma
=
P_{e_n}\circ\cdots\circ P_{e_1},
$$

$$
T_\gamma
=
T_{e_n}\circ\cdots\circ T_{e_1}.
$$

If every edge square commutes,

$$
c_{v_{k+1}}P_{e_k}
=
T_{e_k}c_{v_k}
$$

for all \(k\), then

$$
\boxed{
c_{\mathrm{end}}P_\gamma
=
T_\gamma c_{\mathrm{start}}.
}
$$

### Proof

Repeated substitution gives

$$
c_{v_n}P_{e_{n-1}}\cdots P_{e_1}
=
T_{e_{n-1}}c_{v_{n-1}}P_{e_{n-2}}\cdots P_{e_1}
$$

and continuing recursively yields

$$
c_{\mathrm{end}}P_\gamma
=
T_\gamma c_{\mathrm{start}}.
\qquad\square
$$

The outbound analogue follows identically with \(e_v\) replacing \(c_v\).

### Consequence

Local interface verification can certify global shell/core compatibility along a composed path.

This is one reason the diagram language can remain visually compact.

---

# 11. Outer paths and inner lifts

Let

$$
\gamma
\in
\mathrm{Path}(\mathcal G_{\mathrm{out}})
$$

be an outer EPIC path.

Define its compatible inner lifts as

$$
\boxed{
\mathrm{Lift}(\gamma)
=
\{
\widetilde\gamma:
\widetilde\gamma
\text{ is internally compatible with }\gamma
\}.
}
$$

Then an outer path can have:

### No lift

$$
\mathrm{Lift}(\gamma)=\varnothing.
$$

The outer story is incompatible with the modeled internal dynamics.

### Unique lift

$$
|\mathrm{Lift}(\gamma)|=1.
$$

The outer path determines the inner realization at the current resolution.

### Multiple lifts

$$
|\mathrm{Lift}(\gamma)|>1.
$$

The same external behavior remains compatible with multiple internal histories.

This is a rigorous way to represent the fact that observed behavior need not identify internal state.

---

# 12. Dual path aggregation

Suppose outer paths receive weights

$$
W_{\mathrm{out}}[\gamma]
$$

and compatible inner lifts receive weights

$$
W_{\mathrm{in}}[\widetilde\gamma\mid\gamma].
$$

Define the inner support fiber over an outer path:

$$
\Xi[\gamma]
=
\sum_{\widetilde\gamma\in\mathrm{Lift}(\gamma)}
W_{\mathrm{in}}[\widetilde\gamma\mid\gamma].
$$

Then a finite dual path sum may be written

$$
\boxed{
Z(A\mid E)
=
\sum_{\gamma:E\leadsto A}
W_{\mathrm{out}}[\gamma]
\,
\Xi[\gamma].
}
$$

This does **not** imply quantum amplitudes.

It is a two-level aggregation over:

1. external paths;
2. compatible internal realizations of those paths.

Where continuous path measures are available, sums may be replaced by integrals after the relevant measures are explicitly declared.

---

# 13. Structured vertices as effective path sums

A point-object may itself contain many internal routes.

Let \(a\) and \(b\) be boundary/interface states of \(\mathbb V\).

Define the effective vertex kernel

$$
\boxed{
\mathcal V_{\mathbb V}(b\mid a)
=
\sum_{\lambda:a\leadsto b}
w[\lambda].
}
$$

The internal graph may then be collapsed to a single structured vertex provided the collapsed object preserves the required boundary behavior.

This is the formal basis of the diagrammatic zoom rule.

---

# 14. Zoom equivalence

Let

$$
\mathbb V_{\mathrm{exp}}
$$

be an expanded internal model and

$$
\mathbb V_{\mathrm{col}}
$$

its collapsed representation.

Exact interface equivalence means

$$
\boxed{
\mathcal V_{\mathrm{col}}
=
\mathcal V_{\mathrm{exp}}
}
$$

on the declared boundary variables.

Approximate equivalence means, for a chosen norm,

$$
\boxed{
\|
\mathcal V_{\mathrm{col}}
-
\mathcal V_{\mathrm{exp}}
\|
<\varepsilon.
}
$$

A collapsed point is therefore not “hiding complexity” illegitimately if its boundary kernel is preserved to the required tolerance.

---

# 15. Canonical folded geometry

The preferred high-level diagram is a folded two-lane racetrack.

Top lane:

$$
W_t
\xrightarrow{\mathsf R}
S_t
\xrightarrow{\mathsf R}
I_t.
$$

Turnaround:

$$
I_t
\xrightarrow{\Theta_I}
I_t^+.
$$

Bottom lane:

$$
I_t^+
\xrightarrow{\mathsf A}
S_{t+1}
\xrightarrow{\mathsf A}
W_{t+1}.
$$

Visually:

~~~text
                 INBOUND / RECONSTRUCTION

          W_t  ───────→  S_t  ───────→  I_t
           ◎              ◎              ◎
           ●──────────────●──────────────●
                                          │
                                          │ Θ_I
                                          ▼
           ●──────────────●──────────────●
           ◎              ◎              ◎
        W_{t+1} ←────── S_{t+1} ←────── I_t^+

                 OUTBOUND / REALIZATION
~~~

The outer ring of each \(\odot\)-like point belongs to the EPIC shell geometry.

The inner dot/circuit belongs to the TLICA core geometry.

---

# 16. The turnaround is internal, not geometric decoration

The rightmost turn must pass through the internal self dynamics.

It is not merely a curved arrow.

Formally:

$$
\boxed{
\Theta_I:
Z_I^{\mathrm{in}}
\to
Z_I^{\mathrm{out}}.
}
$$

At higher resolution, \(\Theta_I\) may expose only the load-bearing internal components, for example:

$$
G_t
\to
\text{readings / source map / live rivals}
\to
\pi_t
\to
G_t^+.
$$

The exact decomposition is application-dependent.

Mode B must be used only where the foundation's reflexive rewrite semantics are actually intended.

---

# 17. Substrate turnaround

Likewise the substrate can carry its own internal map

$$
\Theta_S:
Z_S^{\mathrm{in}}
\to
Z_S^{\mathrm{out}}.
$$

Application-level components may include, when warranted:

- salience;
- focus;
- affective forcing;
- slack;
- probe availability;
- sensorimotor realization.

These are not all foundation-identical quantities.

The expanded substrate must preserve their typing.

---

# 18. Visual grammar

A reader should answer four questions at a glance.

## 18.1 Horizontal position — where?

Left-to-right macroscopic order:

$$
\boxed{
W
\quad\longrightarrow\quad
S
\quad\longrightarrow\quad
I.
}
$$

The return lane reverses spatial direction but advances time.

## 18.2 Vertical lane — which pass?

Upper lane:

$$
\boxed{\text{reconstruction / uptake}}
$$

Lower lane:

$$
\boxed{\text{realization / action}}
$$

## 18.3 Radial depth — which geometry?

Outer shell:

$$
\boxed{\text{EPIC whole-object path}}
$$

Inner core:

$$
\boxed{\text{TLICA internal-state trace}}
$$

## 18.4 Line style — what status/type?

Recommended defaults:

- solid outer line: established/declared whole-object map;
- solid inner line: declared internal transport/update;
- dashed line: conjectured bridge/modulation;
- dotted line: optional correspondence/annotation;
- loop: must be labeled feedback, recurrence, or holonomy explicitly;
- \(q?\): constructible but unexecuted probe;
- \(q!\): executed discriminator.

No unlabeled loop is permitted.

---

# 19. Three canonical zoom levels

## L0 — topology

Show only

$$
W\to S\to I\to S\to W.
$$

Purpose: orientation.

## L1 — structured vertices

Show:

- shell/core;
- inbound/outbound ports;
- dual traces;
- typed loops;
- probe branches.

Purpose: normal TLICA–EPIC analysis.

## L2 — expanded mechanism

Open only the point whose internal structure is load-bearing.

Purpose: mechanism, derivation, or discriminating test.

### Rule

$$
\boxed{
\text{expand only the object whose internal structure is load-bearing to the current claim.}
}
$$

Everything else remains an effective structured point.

---

# 20. Diagram completeness test

A serious TLICA–EPIC diagram is incomplete if a reader cannot determine:

1. **location**
   — world, substrate, or self;

2. **pass**
   — reconstruction or realization;

3. **geometry**
   — outer EPIC shell or inner TLICA core;

4. **edge semantics**
   — observation, update, modulation, probe, policy, action, feedback, or transport;

5. **claim status**
   — disclosed/derived, observed, conjectured, or unverified where relevant.

If any of these requires guessing, the diagram is hiding an inference.

---

# 21. Minimal formal object

A dual-pass structured TLICA–EPIC diagram can be packaged as

$$
\boxed{
\mathfrak D
=
(
V,
X,
Z,
E^{\mathrm{in}},
E^{\mathrm{out}},
P,
T,
c,
e,
\Theta,
\Pi
).
}
$$

Where:

- \(V\): structured point-objects;
- \(X_v\): shell/interface states;
- \(Z_v\): internal/core states;
- \(E^{\mathrm{in}}\): reconstructive edges;
- \(E^{\mathrm{out}}\): realizational edges;
- \(P_e\): outer EPIC transport;
- \(T_e\): inner TLICA transport;
- \(c_v\): shell-to-core uptake;
- \(e_v\): core-to-shell realization;
- \(\Theta_v\): local internal dynamics;
- \(\Pi\): provenance/source ancestry where relevant.

This object can be enriched with:

- covariance \(\Sigma\);
- probe-family maps \(\eta_Q\);
- ambiguity fibers \(\mathcal F_Q\);
- local kernels \(\mathcal K_Q\);
- path weights;
- transport holonomy;
- perturbative diagrammatics.

None of those additions collapse the distinction between the two passes or the two geometries.

---

# 22. Relation to the ambiguity formalism

The dual-pass diagram does not replace

$$
\mathcal F_Q(x)
=
\eta_Q^{-1}(\eta_Q(x))
$$

or

$$
\mathcal K_Q(x)
=
\ker d\eta_{Q,x}.
$$

It tells us **where the probes and reconstructions live in the round trip**.

For example:

- inbound probes constrain \(W_t\to S_t\to I_t\);
- internal discrimination can alter the live rival set inside \(I\);
- outbound action modifies \(W_{t+1}\);
- the changed world becomes the next probe field.

Therefore epistemic and agential dynamics become one iterated cycle without identifying them.

---

# 23. Iteration

After one cycle,

$$
W_{t+1}
$$

is the next world input.

Hence

$$
\boxed{
(W_{t+1},S_{t+1},I_{t+1})
=
\mathcal T_t(W_t,S_t,I_t)
}
$$

and repeated operation yields

$$
\mathcal T_{t+n-1}\circ\cdots\circ\mathcal T_t.
$$

The self therefore participates in a recurrent world-coupled process:

$$
\boxed{
\text{constraint}
\to
\text{internalization}
\to
\text{state transformation}
\to
\text{policy}
\to
\text{realization}
\to
\text{new constraint}.
}
$$

This is the preferred verbal compression.

---

# 24. What this buys us

The formalism earns several practical advantages.

### 24.1 Readability

Every overview has the same orientation.

### 24.2 Rigorous recursion

A point can contain a diagram of the same kind at finer scale.

### 24.3 Separation of external and internal ambiguity

One external path can have zero, one, or many internal lifts.

### 24.4 Local verification

Commuting edge squares imply commuting composed paths.

### 24.5 Honest coarse-graining

Collapsed vertices are licensed by boundary-kernel preservation.

### 24.6 No mystical Feynman analogy

The Feynman resemblance is diagrammatic and, where appropriate, perturbative.

The two-pass structured-point formalism itself is ordinary mathematics: coupled graphs, state transitions, commuting squares, lifts, kernels, and coarse-graining.

---

# 25. Claim-status boundary

## Disclosed as mathematics / construction

- two-pass factorization can be defined;
- inbound and outbound maps need not be inverses;
- structured point-objects can carry shell/core state;
- shell/core compatibility is expressed by commuting squares;
- edgewise commutation implies pathwise commutation;
- outer paths can be assigned fibers of compatible inner lifts;
- expanded and collapsed vertices can be compared by boundary kernels.

## TLICA-compatible but not yet foundation commitments

- \(W\to S\to I\to S\to W\) as the canonical universal diagram skeleton;
- the exact shell/core decomposition for every TLICA application;
- a universal interpretation of all internal traces as one transport class;
- promotion of the diagram grammar into frozen foundation notation.

## Empirical / phenomenological claims requiring probes

- whether this diagram grammar improves human interpretability;
- whether particular internal decompositions track real human mechanisms;
- whether specific slack/affect/probe bridges hold causally.

---

# 26. Promotion criterion

The structured-point formalism becomes foundation-worthy only if it does more than draw existing theory nicely.

A promotion case requires:

1. at least three independent TLICA applications where the same two-pass distinction is load-bearing;
2. an ablation showing existing notation loses a necessary distinction without it;
3. a counterexample search showing the grammar does not force false symmetry or invertibility;
4. a holdout application not used in designing the formalism;
5. reconciliation with current \(G,\kappa,\phi,\rho,S\) typing;
6. a clear falsifier or failure mode.

Until then, it is best treated as an **application-level formal language with foundation-extension potential**.

---

# 27. Final compression

The canonical TLICA–EPIC object is not a chain.

It is a **folded, dual-geometry round trip**:

$$
\boxed{
W_t
\overset{\mathrm{reconstruct}}{\longrightarrow}
S_t
\overset{\mathrm{internalize}}{\longrightarrow}
I_t
\overset{\Theta_I}{\longrightarrow}
I_t^+
\overset{\mathrm{realize}}{\longrightarrow}
S_{t+1}
\overset{\mathrm{act}}{\longrightarrow}
W_{t+1}.
}
$$

Each macroscopic point is a circuit inside a circuit:

$$
\boxed{
\mathbb V_v=(X_v,Z_v,c_v,e_v,\Theta_v).
}
$$

The outside of the point participates in EPIC path geometry.

The inside of the point participates in TLICA internal dynamics.

The two are coupled by explicit compatibility maps.

The diagram should therefore be readable at a glance as:

$$
\boxed{
\text{outside paths, inside dynamics; same points, two geometries; one causal round trip.}
}
$$