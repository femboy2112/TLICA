# TLICA–EPIC
## Typed inferential path geometry, and a diagram standard for it

[← Wiki home](README.md) · Source: [`research/tlica_epic_path_geometry_2026-10-03/`](../research/tlica_epic_path_geometry_2026-10-03/README.md) · **Research note · v0.5.2 · foundation extensions GATED, not applied**

---

> **What this is.** TLICA–EPIC takes the distinctions TLICA already keeps apart — contact
> **κ**, toolkit-relative truth-indistinguishability **φ**, identity-correlation **ρ**,
> source-map adequacy **σ**, probe availability, toolkit closure, and the trio of
> independence / coherence / discrimination — and asks what *geometry* appears when you treat
> them as a single **typed path system**. Its central object is not "the argument that proves
> a hypothesis." It is the **family of candidate states that stay indistinguishable under the
> probes you can actually construct, that are actually available, and that you actually ran.**

> **What tier it sits at.** This is a **research-tier** dossier — "application-grade formal
> synthesis," in the source's own words. It makes **no novelty claim**: TE-016 records that
> *TLICA–EPIC is a novel mathematical theory* is **UNVERIFIED**, because no prior-art survey
> has been run and the ingredients overlap established inverse problems, information geometry,
> category theory, graphical models, sheaf methods, Bayesian path measures, and perturbative
> diagrammatics.

> **What it refuses to claim.** It changes **nothing** in the frozen foundation. A companion
> *Foundation Extension Gate* isolates a handful of foundation-extension *candidates* purely so
> they can be reviewed later — and **applies none of them**. No frozen-foundation file is
> touched on this branch. The EPIC acronym, a universal epistemic path integral, Feynman
> diagrammatics, a universal information metric, and any scalar "truth score" are explicitly
> *not* promoted.

---

## The central object: ambiguity as a fiber

The whole construction turns on one picture. You have a declared space **X** of candidate
states — models, explanations, ontic possibilities, "what could actually be the case here."
You have a family **Q** of probes you *actually executed*. Stack their outputs into a single
joint observation map **η_Q : X → Y_Q**. Then the states you *cannot currently tell apart from*
a given state **x** are exactly the ones that land on the same output:

$$
\mathcal F_Q(x) = \eta_Q^{-1}\bigl(\eta_Q(x)\bigr).
$$

That set is the **ambiguity fiber**. When the spaces are smooth, the first-order version is the
**kernel** of the derivative, **𝒦_Q(x) = ker dη_{Q,x}** — the directions you could slide the
candidate state along without changing any executed probe's reading, to first order.

> **In plain terms —** the fiber is *everything that still looks the same as your best guess
> given the tests you've actually run*. Doing epistemic work means **shrinking that fiber** by
> running a probe that separates things inside it. The kernel is the "dark directions" — the
> ways the truth could differ that your current tests are blind to. Global ambiguity (the
> whole fiber) and local blindness (the kernel) are kept as separate objects; a thing can be
> locally distinguishable yet globally non-unique.

This is why the dossier calls EPIC *"the geometry of distinguishability under path-, source-,
and identity-aware evidence."* The fiber is a **model-relative indistinguishability class** —
`TE-001`, **Disclosed** as a definition. It is explicitly **not a metaphysical identity claim**
about the world.

A natural design rule falls out: don't aim your next probe at the hypothesis you already know
how to confirm — aim it at the **darkest surviving direction**, the least-resolved eigenvector
of the correlation-corrected resolution tensor **𝓘_Q = Jᵀ Σ⁻¹ J**. (That tensor shares the
same nullspace as the kernel whenever the noise covariance **Σ** is positive-definite — `TE-004`,
**Disclosed**.)

## The notation firewall: what EPIC is careful *not* to collapse

A striking amount of the dossier is spent *refusing* to reuse foundation symbols. This is
deliberate. An early visual sketch had used convenient but noncanonical labels, and the first
part of the work is a firewall that fixes them:

- **Layers stay layers.** TLICA's two layers are the *intrinsic* and *asymptotic* layers.
  Mode A / Mode B / Mode C are developmental/operational response-types, *not* the two layers.
  So EPIC says **stratum** or **channel** for diagram layout and reserves *layer* for TLICA's
  own architecture.
- **φ stays truth-indistinguishability.** An observed or phenomenological trace is written
  `y_t` or `o_t` — *never* written `φ_t` for visual convenience.
- **S and μ are different quantities.** The foundation's slack margin **S** is one thing;
  EPIC's **μ_t(q) ∈ [0,1]** is only an *application-level* probe-availability / probe-weighting
  variable. The proposed bridge "S falls ⟹ μ falls" **may be tested in a declared regime but
  is not an identity and not a foundation theorem** (`TE-008`: the typing is **Disclosed**; the
  bridge itself is **Conjectured / UNVERIFIED** outside explicitly measured regimes).
- **G stays the lived-I.** The dynamical foundation reserves **G** for the slow lived-I
  structure that imprinting and Mode-B dynamics rewrite (with `ρ = R(G)`, `f = F(G,·)`). So
  EPIC refuses to reuse `G` for an information matrix and writes its resolution tensor **𝓘_Q**
  instead.

> **In plain terms —** EPIC's rule is almost paranoid about *not* smuggling meanings together.
> "How present is it," "does it survive testing," and "is it part of me" are the three
> coordinates ([three-coordinates.md](three-coordinates.md)); EPIC adds machinery *around* them
> and works hard to keep its own bookkeeping variables from leaking into them.

The compact slogan for the whole firewall:

$$
\text{no path count without provenance;}\quad
\text{no }\phi\text{ update without a pathway;}\quad
\text{no phase without transport;}\quad
\text{no certainty without adequacy.}
$$

## Constructible ≠ available ≠ executed

The sharpest idea in the dossier — and the strongest foundation-*candidate* — is that a probe
**q** can sit in three genuinely different statuses, and they must not be confused:

1. **constructible** — `q` is reachable inside the closure of your current tools, `q ∈ Cl(Tools_t)`;
2. **effectively available** — `μ_t(q) > 0`, you could actually deploy it locally;
3. **executed** — `q ∈ Q_exec`, you actually ran it.

These are logically distinct predicates (`TE-006`, **Disclosed**). *Having* a tool is not
*being able to use it now* is not *having run it*. The existence of a pathway does not hand you
its result; an executed probe does not mean every constructible rival was tested; and **felt
certainty implies neither constructibility nor execution** (`TE-007`, **Disclosed procedurally**;
the claim that this gap occurs *frequently in humans* is **UNVERIFIED**).

> **In plain terms —** "I could have checked" is not "I checked," and "it felt obvious" is not
> either of those. EPIC gives each of those a distinct slot so a diagram can't quietly pretend
> a thought was tested when it wasn't.

The dossier connects this to φ's toolkit-relativity: if **no constructible route exists inside
the declared tool closure**, the relevant φ-assessment may be **undefined rather than false**;
if a route exists but was not executed, no result has been earned merely because the agent
"could check."

## The monotonicity theorem, and felt vs. epistemic resolution

One clean theorem anchors the geometry. If you run a **richer** executed probe family
(`Q₁ ⊆ Q₂`, keeping every `Q₁` output), the exact ambiguity can only stay the same or shrink:
**𝓕_{Q₂}(x) ⊆ 𝓕_{Q₁}(x)** (`TE-002`, **Disclosed** by an elementary set-theoretic proof).
Run the contrapositive and you get the behaviourally interesting reading: if your executed probe
family *shrinks*, exact ambiguity **can only stay equal or enlarge**.

Crucially, the theorem does **not** license the psychological leap "slack falls ⟹ you run fewer
probes" as a universal law. That bridge is kept at application level and must be tested.

This is where EPIC says something it can actually defend about the emotional case. Both
*successful discrimination* and *premature closure* can produce the identical first-person state
"nothing left to think about." Therefore:

$$
\text{felt resolution} \neq \text{epistemic resolution.}
$$

Only the author-report that the motivating dryer episode *exposed* that difference is logged at
**Observed** level (§35); the general human mechanisms around it stay **Conjectured / UNVERIFIED**.

## Source-map adequacy stays its own diagnostic

Identifiability is not adequacy. You can pin a candidate down to a single survivor,
**𝓕_Q(x) = {x}**, and still have reality lie *outside* X entirely — so **identifiability ≠
model adequacy** (`TE-025`-style caution; §25). Separately, a model can fit every observed
output while attributing them to the **wrong generator**. Hence the σ-firewall:

> high coherence, or high φ, under a bad source map can still miss the cause.

The gate records this as a **candidate methodological standardization** — "φ-resolution does not
entail σ-resolution" (`TE-009`, **Disclosed** as a modeling possibility) — and is emphatic that
**σ is not being promoted to a fourth coordinate**. It stays a separate diagnostic. When the
remaining fiber holds several candidates and no known probe or source defect remains, the state
is **contextually saturated**: *no present discriminator reaches the distinction* — which is
**not** the claim that *the distinction is metaphysically absent*.

## Path count is not independent evidence

Because inferential routes can share a common origin, EPIC insists:

$$
\text{path multiplicity} \neq \text{independent evidence.}
$$

Shared provenance shows up naturally as covariance. In the scalar illustration where every
reading is one true value plus a *shared* bias `b ~ N(0,τ²)` plus independent noise, the Fisher
information saturates: `I_n → 1/τ²` as `n → ∞`. **Infinitely many descendants of one biased
source do not produce infinite independent information** (`TE-005`, **Disclosed** structurally;
real human/source applications still need case-level provenance). This is the same discipline
the archive applies elsewhere under *factor shared provenance before counting independent
bearings* — see [glossary.md](glossary.md) for the standing vocabulary.

A matched trio of warnings keeps the "quantum" flavour honest. Nonnegative path weights **add**
(aggregation, no destructive interference). A Möbius/subset-lattice term is **interaction, not
mechanism**. And genuine phase cancellation is licensed *only* when paths carry a declared
compositional phase under an operational common basis — "**no declared transport, no phase**"
(`TE-015`, **Disclosed**). Where a Gaussian baseline with an interaction expansion is actually
declared, Wick contractions *do* admit standard Feynman-diagram bookkeeping (`TE-014`,
**Disclosed** mathematics) — but any quantum interpretation is **Refuted as an automatic
inference**; none follows.

## The diagram standard: wires are wires, structure lives in the nodes

The current standard (v0.5.2) is deliberately severe and deliberately Feynman-economical. Its
one-sentence form:

> **TLICA–EPIC diagrams are ordinary directed wire graphs whose vertices may be either atomic
> points or recursively expandable EPIC-integrated circuits.** Wires remain wires. The extra
> expressive power lives in the vertices.

An earlier draft had drawn two parallel geometries — an "outer EPIC shell" line beside an "inner
TLICA core" trace — on every connection. That is superseded. Now there is **one graph of wires**
plus **vertices of variable internal resolution**. EPIC governs the paths through the graph;
TLICA supplies the internal structure of whichever vertices need it; they meet only at a node's
**typed boundary**. A self-node can be an atomic point `●` until its internals matter, then be
*expanded* into an open circuit exposing — only where load-bearing — `G`, κ, φ, ρ, σ, slack `S`,
`μ_t(q)`, the executed probe family, the live rivals, and policy. The governing rule: **expand
only what is load-bearing to the current claim.**

Two rules keep this honest. The **master orientation rule** — *an arrow points toward the object
being updated, not merely toward what happens later in time* — so every serious edge is typed
(obs, imprint, Mode-B rewrite, probe `q!`, gating, policy, wake projection, lossy
reconstruction), and an untyped loop is forbidden. And the **substitution invariant**: if two
node representations have the same typed boundary and the same semantics, either can replace the
other inside any well-typed context without changing the larger diagram (`TE-027`, **Disclosed**
as the central compositional invariant). That is what lets a whole TLICA subsystem be treated as
a point until you zoom in. Three resolution levels — **L0** topology, **L1** integrated-node
graph (the default), **L2** a single node's internal circuit — all share one grammar.

> **In plain terms —** read the wires; open a box only when what's inside it is doing the work.
> A dashed edge means *conjectured or optional bridge*; a solid edge means *declared / executed*.
> Claim status (Observed, Conjectured, UNVERIFIED, Refuted) rides as an annotation, never as a
> thicker wire or a brighter colour — "no decorative ontology."

## Reading a `.tlica` file

The standard ships a **human-readable `.tlica` serialization** with an **executable pure-Python
reader** (`v0.5.2/tlica_epic_read.py`, standard library only) and two worked specimens: a dryer /
premature-closure diagram and a semantic-wake / observer-reconstruction diagram. The reader
parses the text grammar and, for each content node, computes the four readings the diagram is
shorthand for — **ρ** (identity-correlation, a max-flow from the cogito), **φ**
(truth-indistinguishability, from the length of the verification chain to ground and the
executed probes on it; *undefined* if the chain never reaches ground), **κ** (contact), and
**D** (mediation order) — plus a content class.

The **v0.5.2 semantic correction** is "world first, content second": **world events and internal
contents are distinct typed objects**, and `source x : ...` names **world items only**. A node
may never silently mean both an external event and the I's internal representation of it. Here is
the opening of the dryer specimen:

```text
world   y_wet  "wet clothes in the dryer"          # a WORLD event
content x_wet  "encounter-content: the clothes are wet"  A=1   # the I's content OF it
content P      "my normal dryer method usually works"    A=1
content H1     "they ran it wrong because I normally have no issue"  A=1
content H2     "load / heat / time concern may be valid"            A=1
source  x_wet  : y_wet        # sigma names a WORLD item only
wire    I -> P    k=0 w=0.90  # prior P already strongly integrated (high rho)
wire    P -> H1   k=0 w=0.70
probe   q_obs! -> x_wet  mu=1.0 q=1.0   # executed
probe   q_chk? -> c2     mu=0.15        # constructible, NOT executed
gate    X  M=1.0 P=1.3                  # S = M - Pressure = -0.3
act     X -> a_auto "blame / re-run my way" mode=auto
act     X -> a_B    "run q_chk / q_man first" mode=B
bridge  A -> X "anger further raises Pressure [CONJECTURED causal bridge]"
bridge  X -> q_chk? "S <= 0 lowers probe uptake [CONJECTURED]"
```

The read is: the prior **P** ("my method works") is *already* strongly bound into the I before
the fresh encounter; a low-slack precondition (prior wake + constraints + anger) is in place
*first*; the clothes-are-wet content arrives; and the gate **S = M − Pressure** comes out
negative, so the **automatic** exit fires — attribution becomes behaviourally active **before**
its discriminator `q_chk?` ever becomes an executed `q_chk!`. The specimen is careful that this
**does not prove H1 false**; it says the source attribution goes live before its discriminator
closes.

> **In plain terms —** the diagram catches the exact moment a *source story* ("they ran it
> wrong") starts driving action before the *test* that would separate it from the rival ("load /
> heat / time mattered") has been run.

Two load-bearing honesties about the gate. The **S = 0 actualization threshold is a foundation
posit** — `S ≤ 0` selects the automatic exit, `S > 0` the slack-mediated one — and the reader
reads the realized mode straight off the sign of `S`; Pressure and the capacity `M` are open
functions in the foundation, declared here as inputs, and the reader says so. (The dynamics of
`S = M − Pressure` and the slack gate live on [the-self-in-motion.md](the-self-in-motion.md).)
And every causal arrow from affect or slack into the gate — `anger → Pressure`, `S ≤ 0 → lowered
probe uptake` — is drawn as a **`bridge`**: **visible, labeled CONJECTURED, and never computed**.
The reader does the fiber/φ/ρ/κ arithmetic; it does not pretend to have measured the human
bridge.

## The semantic wake

The second specimen formalizes observer reconstruction, extending the archive's
*Semantic Wake Drag* dossier without changing its foundation status. The load-bearing move is a
**non-arrow**: an actor's internal model **M_t does not connect directly** to an observer's
reconstruction **M̂_t^B**. Instead the only route is

$$
M_t \to a_t \xmapsto{\text{wake}} \omega_t \rightsquigarrow_B \widehat M_t^B,
$$

model → action → externally visible wake → the observer's *lossy* reconstruction. So **more rapid
action can coexist with *less* external identifiability of the model that produced it** — many
actor-models fit the same wake, i.e. a large reconstruction fiber (`TE-010`, **Disclosed** at the
communication-model level; the *magnitude* of real semantic-wake drag is **Conjectured /
UNVERIFIED**). A "semantic header" `h` that genuinely separates candidates the wake alone cannot
will shrink that fiber in the formal model, `𝓕_{(ω,h)} ⊊ 𝓕_ω` (`TE-011`, **Disclosed** by the
same monotonicity logic) — but whether proposed headers actually help in real social systems is
**UNVERIFIED**.

## The foundation-extension gate: candidates isolated, none applied

The point of the *Foundation Extension Gate* is to keep application-level power from being
mistaken for foundation status:

> application-level power is evidence for usefulness, not automatic evidence for foundation status.

It names four extension **candidates** and quarantines them for review: **(A)** the
constructible/available/executed triplet; **(B)** the source-map resolution firewall
("φ-resolution ⇏ σ-resolution," σ staying a diagnostic, not a fourth coordinate); **(C)** typed
update semantics (an arrow must name the operation that updates its target); and **(D)** the
hierarchical-wire / expandable-vertex grammar. Each is tagged **UNVERIFIED / promotion-gated**
(`TE-017`, `TE-024`). None is applied. Before any could enter a future foundation release it must
clear **twelve gates** — typing audit, a κ/φ/ρ coordinate firewall, cross-application recurrence
in at least three substantially different applications, ablation against existing machinery, a
simpler rival formalism, a predeclared discriminating probe, a provenance audit (the support must
not be three restatements of one originating intuition), a holdout, a counterexample search,
foundation reconciliation (the prior commitments, exclusions, and the cogito anchor must survive),
an explicit claim ledger, and **human author review** by Leah. The gate's own current verdict is
unambiguous: **application-grade formalism; several foundation-extension candidates; no
foundation mutation yet.**

---

## What's solid, and what's a labeled guess

The dossier keeps a strict ledger (vocabulary: **Disclosed / Corroborated / Observed /
Conjectured / UNVERIFIED / Dark / Refuted**; conclusions inherit the weakest load-bearing
premise). In summary:

- **Disclosed under the stated mathematics** — the ambiguity fiber **𝓕_Q(x)**; probe-family
  monotonicity; the kernel **𝒦_Q = ker dη**; the shared nullspace of **𝓘_Q = Jᵀ Σ⁻¹ J**; shared
  provenance limiting information gain; path composition as a category; holonomy requiring a
  declared transport; Gaussian perturbation expansions admitting Wick/Feynman bookkeeping; phase
  cancellation requiring operational phase transport; and the diagram standard's substitution
  invariant.
- **Observed (author-report level)** — the dryer episode exposed a real gap between felt
  obviousness and an actually executed local discriminator; the high-frequency-pulse /
  semantic-wake phenomenon is part of the author's reported phenomenology.
- **Conjectured / UNVERIFIED (human mechanisms needing external probes)** — that anger reliably
  lowers relevant slack; that lower slack reliably suppresses probe availability or execution
  (the `S↓ ⇒ μ↓` bridge); that semantic headers reliably shrink reconstruction fibers in real
  social systems; that the proposed training probes recover a stable institutional objective
  (`TE-012`, **Conjectured**); and that the same typed geometry yields measurable predictive gain
  across human domains. The claim that the typed diagram grammar improves practical reasoning, and
  that the hierarchical grammar is more glance-readable, are **Conjectured / UNVERIFIED** usability
  claims (`TE-018`, `TE-029`).
- **Refuted** — any *automatic* quantum interpretation of the Feynman bookkeeping.
- **UNVERIFIED** — that TLICA–EPIC is a novel mathematical theory (`TE-016`, no prior-art survey
  run); and that any of the four foundation-extension candidates belongs in the foundation.

**Foundation impact: none.** No frozen-foundation file is modified on this branch; the frozen
core is **untouched**, and the foundation-extension candidates are isolated for review, not
applied. The S = 0 actualization threshold is a foundation posit; every affect-to-gate and
slack-to-probe bridge is drawn CONJECTURED and never computed. No novelty claim is made.

*Full dossier, the complete claim ledger, the diagram standard, both worked specimens, and the
executable reader: [`research/tlica_epic_path_geometry_2026-10-03/`](../research/tlica_epic_path_geometry_2026-10-03/README.md).*

*Related wiki pages: [The Three Coordinates](three-coordinates.md) (κ, φ, ρ themselves),
[The Self in Motion](the-self-in-motion.md) (slack, `S = M − Pressure`, Mode-B rewrite), and the
[Glossary](glossary.md).*
