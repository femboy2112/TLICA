# The Dynamical Substrate — Minimal Axioms for Earning TLICA's Borrowed Motion-Words

**Epistemic status:** Research note; **not foundation**. This is an *extension layer* that
sits under the application papers and does **not** modify the frozen foundation (freeze
v5.3.2, errata v5.3.3). Every object it posits is a flagged **posit**; every import from the
research/applications layer (toolkit closure, the filter space 𝓕) is marked as such and is
**not** attributed to the freeze. Status labels follow the research-note convention —
**Observed / Conjectured / Refuted / UNVERIFIED** — plus the foundation's own **derived /
posit** language for structural status. (The label "Demonstrated" is deliberately avoided: it
appears nowhere in the corpus.)

**Author:** Leah (`femboy2112`). Drafting assistance: Claude. Opened 2026-09-08.

---

## 0. Why this note exists

TLICA borrows motion-words from mathematics and physics — *momentum, basin, attractor,
metastability, oscillation, reachability, transport* — under a stated discipline: the borrow
asserts the **mathematical shape** that transfers (the "structurally-reasonable aspect of
consciousness"), **not** the literal law or units. The literal correspondence does not follow
from the analogy; it must be **earned** by justification, or honestly **denied** where it
would be a category error. (See `docs/glossary.md`, "Borrowed terms — scope pins": *dimensional
analysis, not equality*.)

You cannot earn a correspondence against nothing. To earn a *dynamical* borrow you need a
stated dynamics to earn it **against** — a formal object in which the term is *defined* and
from which its claimed properties either *follow* (a theorem) or are *exposed as conjecture*
with the missing lemma named. This note supplies the smallest such object.

**What "closure" means here:** for each target term, a definite Ledger status against the
stated axioms — Derived, Conjectured-with-named-lemma, or Refuted/category-error — with
nothing left as vibes-level analogy. Downgrading a term to shape-only (e.g. *momentum is not
a force*, it is a control-cost) is a **legitimate** closure, not a failure.

---

## 1. What the foundation already commits (the dynamics is not a blank)

The freeze is **not** silent on dynamics. Section 8 of the formal apparatus is titled
*"Substrate, Focus, and Dynamics,"* and it commits a **local micro-dynamics**:

- **Edge-weight imprinting update** (`foundation/3_formal_apparatus.md` §8.4). An update event
  has form `e = (s, u, v, k, α, β)`, and the rule is a bounded, event-triggered linear update
  on the ρ-graph edge weights:

  > `w^{m,k}_{s⁺}(u,v) = Π_{[0,1]}( (1 − β)·w^{m,k}_{s⁻}(u,v) + α·(1 − w^{m,k}_{s⁻}(u,v)) )`

- **Verification-tool imprinting** follows the same form (§8.5), and **osmotic imprinting**
  operates *continuously* throughout the I's existence (§8.7).
- **Coordinate entanglement** (§7.4): the coordinates influence one another through contingent
  mechanisms — "these are dynamics, not definitions."

The freeze equally **declines** the rest, explicitly:

- **Rates** are unspecified (§8.8: "The architecture does not specify rates").
- **Functional forms** are open though their *dependencies* are fixed (§8.8: open functions
  `Γ, Λ, A^k, B^k, A^T`).
- **Per-encounter mode-selection** is not a committed transition rule (`2_access_and_development.md`
  §; exclusion #17 in `4_derived_concepts_and_predictions.md` §11.2).
- **Valuation / preservation / action-priority dynamics** are named as *not yet formalized*
  (`5_translations_open_problems_conclusion.md` §13.3; exclusions #18, #19).
- **No global frame-state evolution map.** The model instance `𝓜_m` is a *static tuple of
  time-indexed families*; it names the components at each `t` but commits **no** map carrying
  the tuple at `t` to the tuple at `t+1`.

**The gap, precisely.** The freeze commits a *reweighting micro-dynamics* on the ρ-graphs and
*declines the global map* that reweighting would induce over the whole frame. Every borrowed
motion-word is a claim about that **global** trajectory. This note posits the minimal global
map as an extension — and holds it accountable to the committed micro-dynamics.

---

## 2. The axioms

Each axiom is stated as a **lived datum** (the phenomenon it answers to), then its **rigid
encoding** (the formal object), then **what it does not claim**, then its **foundation
anchor**. An axiom you can point to in experience is a *motivated* axiom, not a smuggled one.

### A1 — You are always *in* a frame, and frames have neighbors.

**Datum.** At every waking moment there is a total way the world is showing up — an operative
organization of experience you look *from*, not *at*. And outlooks have a felt nearness: two
moments can be small adjustments of one stance, or a gulf apart.

**Encoding.** Let the **frame-state** `x_t` be the time-`t` slice of the model instance `𝓜_m`
— at least the family of historical ρ-graphs `{G^{m,k}_t}_k`, together with the field
`𝖠^m_t`, the focus `Foc^m_t`, and the toolset `Tools^m_t`. Let `X` be the space of such
slices. Posit a **nearness** `d` on `X` (a pseudometric): frames are neighbors when their
coordinate profiles (κ, φ, ρ⃗) are close.

**Does not claim.** That `d` *is* φ — φ is a coordinate on *contents*, not a metric on frames;
`d` is motivated by φ-style indistinguishability, not identified with it. Nor that `X` is a
manifold or carries any smoothness.

**Anchor.** `𝓜_m` as a static tuple of time-indexed families (§6–§8); ρ⃗ as the "primary
object" (§7.2); φ (§7.3). *Flag:* reading the whole slice as a single point `x_t ∈ X` is a
research-layer aggregation; the freeze names the components, not the aggregate.

### A2 — Left alone, a frame still moves.

**Datum.** With no new input and no deliberate act, experience does not freeze. The mood
ripens, attention slides, the half-thought finishes itself. There is an *unbidden succession*
— a next-moment that grows out of this one.

**Encoding.** Posit an **endogenous global map** `T: X → X`: the one-step drift of a frame
absent intervention. Forward orbits `x, T(x), T²(x), …` are trajectories.

**Does not claim.** A closed form for `T` (the freeze declines exactly this), nor any rate.
`T` is posited to *exist* with minimal properties, not written as a formula.

**Derivation debt (open, flagged, not discharged).** A legitimate `T` must be *inducible from*
the committed micro-dynamics: §8.4's edge-weight update and §8.7's osmotic patterning already
move the `{G^{m,k}_t}` component of `x_t`. Deriving `T` over the *whole* slice from that
micro-update — rather than positing it — is a named open obligation of this program.

**Anchor.** §8.4 update; §8.7 osmotic imprinting; "no `t→t+1` map on `𝓜_m`"; rates declined
(§8.8).

### A3 — But you can act on your own frame.

**Datum.** You are not only carried. You can turn attention, take up a practice, deploy a
tool, choose otherwise — and it bends where the next moment lands. Steering is real, and it is
*not* the same thing as drift.

**Encoding.** Let `U` be the set of **admissible interventions** — the acts you can actually
perform, grounded in the toolset `Tools^m_t`. Posit a **controlled map** `T_u: X × U → X`,
with drift as the null intervention: `T = T_∅`.

**Does not claim.** A policy over `U` — *which* intervention fires when. The freeze explicitly
declines per-encounter mode-selection; `U` is the space of admissible acts, **not** a
selection rule over them.

**Anchor.** `Tools^m_t` (§8); mode-selection declined (exclusion #17). *Flag:* the *closure*
of the toolset, `Cl_𝒜(𝒯_t)`, is a **research-layer** construct (`research/grokking_as_toolkit_closure_2026-08-29.md`),
imported explicitly where a term needs it — **not** a foundation object.

### A4 — Turning has a cost, and it isn't symmetric. *(deferred — needed only for momentum)*

**Datum.** To keep going the way you are already going is nearly free; to turn *against* the
current of your own outlook takes effort, and more of it the harder you were already going that
way. There is a felt drag — an inertia of stance.

**Encoding.** Posit an **anisotropic transition cost** `c(x, u) ≥ 0`, larger for interventions
that reverse the recent direction of travel in `X`.

**Grounded bridge.** The committed §8.4 update *already* carries a retention term,
`(1 − β)·w`: the current weight resists reweighting in proportion to itself. That is directional
inertia sitting in the freeze; `c` generalizes it to the global map.

**Does not claim.** Any conserved quantity, mass, or force. (The literal-momentum denial lives
in §4.) *Kept separable* so only the momentum earn pays for `A4`.

**Anchor.** §8.4 retention structure.

### A5 — You can reweight what's available; you can't conjure what isn't.

**Datum.** However a frame moves, it cannot **conjure** a capacity it lacks — it adds no
operation from outside its own toolkit. But it is not stuck with a fixed inventory either:
what it *can* do is **reweight**. It can drive an available pathway's resistance toward zero —
bringing it to frictionless phenomenal availability — or negate it outright, dropping it out
of availability. Availability is a weighting the frame continuously modulates, not a standing
list; and the terms that describe a frame still describe it a step later.

**Encoding.** `T` and `T_u` are subject to **consistency obligations**: (i) they enlarge no
*primitive* toolset — they add no operation outside `Tools^m_t` (or its declared closure) —
but they act freely on the **availability/weighting** of pathways across the full range,
reweighting the ρ-graph edge weights `w ∈ [0,1]` (§8.4) and the phenomenal-availability
predicate `A_{m,t} ∈ {0,1}` that carves `𝖠⁺` from `𝖠`: up to near-frictionless (`w → 1`,
available) or down to negation (`w → 0`, unavailable); (ii) κ, φ, ρ remain well-defined and
𝕂-valued after a step; (iii) they smuggle **none** of the freeze's declared-open items — no
mode-selection policy, no identification of ρ with valuation/preservation/action-priority
(exclusions #18, #19), no metaphysical-inviolability claim (#20), no resolution of the §13.3
open problems.

**Anchor.** The reweighting **is** the committed micro-dynamics — the §8.4 edge-weight update
and §8.7 osmotic patterning; the availability predicate `A_{m,t}` carving `𝖠⁺` (§6–§7); the
toolset bound (§8); exclusions §11.2; open problems §13.3.

---

## 3. The Ledger (this note's vocabulary)

Structural status uses the foundation's language: each **axiom** is a **posit** (flagged);
a property is **derived** when it follows from the posits. Evidential status uses the
research-note convention: **Observed / Conjectured / Refuted / UNVERIFIED**. A borrowed term's
**literal correspondence** is thus one of:

- **Derived** — the literal law follows from the substrate axioms (a proof exists).
- **Conjectured** — plausible on the axioms, with the missing lemma/condition *named*.
- **Refuted / category-error** — the literal law does not and cannot hold; the term is
  **downgraded to shape-only**, stated as a *legitimate* result.
- **UNVERIFIED** — an empirical correspondence awaiting evidence.

The **shape** claim (that the mathematical shape transfers) is taken as already asserted by the
corpus; this note adjudicates only the **literal** claim on top of it.

---

## 4. Correspondence obligations — the target terms

For each term: the **shape** (asserted), the **literal** claim (to earn or deny), the
**obligation** (what would discharge it), the **anchor/import**, a **seeded verdict** (a first
honest read, to be earned or killed in later rounds), and the **discriminator** (the check that
comes back differently if the literal claim is false).

### reachability
- **Shape:** some route of admissible acts gets you from here to there.
- **Literal:** the control-theoretic reachable set `R(x) = { y : y = T_{u_k}∘…∘T_{u_0}(x),
  u_i ∈ U }`.
- **Obligation:** A3 (`T_u` well-defined). Then `R(x)` is just the forward orbit under `U`.
- **Import:** "reachable route" (grokking note, research-layer).
- **Seeded verdict:** **Derived** (conditional on A3) — the ripest literal earn; control-theoretic
  reachability transfers with no units mismatch.
- **Discriminator:** exhibit an `(x, y)` with **no** admissible sequence `x → y` (unreachable)
  against one with such a sequence (reachable). The relation is decidable on the transition
  system.

### metastability
- **Shape:** a sticky region of outlook you leave only via a latent route.
- **Literal:** an almost-invariant set `M ⊆ X` whose exit-time ≫ intra-`M` mixing time on the
  dynamics.
- **Obligation:** A2's dynamics **plus** the imported toolkit-closure `Cl_𝒜(𝒯_t)` (research-layer,
  flagged); show the timescale separation.
- **Correction of record:** metastability is near-earned relative to the *grokking closure
  construct*, **not** relative to the freeze — closure is a research posit, not a foundation
  object.
- **Seeded verdict:** **Conjectured** (near-derivable once dynamics + closure are in hand; not
  yet a theorem).
- **Discriminator:** estimate exit-time vs mixing-time; a genuine metastable set shows a clear
  separation, a merely slow region does not.

### basin / attractor
- **Shape:** *basin* = outlooks that fall into the same settled place; *attractor* = the place
  they fall into.
- **Literal:** the ω-limit set (attractor `A`) and its basin `B(A) = { x : ω(x) ⊆ A }` on the
  extended dynamics.
- **Obligation:** A2's `T` gives the *definitions* directly. The claim that a **specific**
  developmental process *is* an attractor needs a convergence witness (a Lyapunov function or a
  contraction) for that process.
- **Anchor / answered question:** `research/born_good_developmental_attractors_2026-08-13.md`
  asks whether the attractor metaphor requires a formal state-transition model. **It does — and
  A2 (over §8.4) is that model.** The metaphor is now a testable claim, not a mood.
- **Seeded verdict:** *definitions* **Derived** (conditional on A2); *"process X is an
  attractor"* **Conjectured** until convergence is exhibited.
- **Landmine (A5-iii):** a "value attractor" must **not** imply ρ measures valuation
  (exclusion #19). Flag any earn that would.
- **Discriminator:** exhibit convergence of trajectories in a neighborhood to `A` (basin), or a
  counterexample trajectory that escapes.

### transport
- **Shape:** structure carried from here to there.
- **Literal:** a genuine transport map — an optimal-transport push-forward of a measure, or
  parallel transport along a connection. **Not claimed.**
- **Obligation:** to upgrade, exhibit either a metric + cost (→ optimal transport) or a
  connection (→ parallel transport). Absent that, the grokking `T_ij` is a *transition /
  reachability witness*, not transport.
- **Import:** `T_ij` (grokking note, already a declared operational map — research-layer).
- **Seeded verdict:** **Conjectured**, and likely **stays shape-only**: the literal needs named
  extra structure the corpus has not committed.
- **Discriminator:** is there a pushed-forward/conserved measure, or a path-independent
  parallel transport? If not, it is transition, not transport.

### momentum
- **Shape:** an outlook has speed + direction + magnitude and resists turning.
- **Literal:** `p = m·v`, a conserved momentum under a force law. **Denied** — category error:
  there is no conserved quantity, no mass, no force.
- **Obligation (shape only):** A4's anisotropic cost, grounded in §8.4's retention term
  `(1 − β)·w`.
- **Seeded verdict:** shape **Derived** (anchored directly in §8.4 retention); literal
  **Refuted** — downgraded to **control-cost / hysteresis**, a *legitimate* closure.
- **Discriminator:** is any quantity conserved along drift? (No → not literal momentum.) Is
  there resistance-to-reweighting proportional to the current weight? (Yes, §8.4 → the shape
  holds.)

### oscillation
- **Shape:** an outlook swings back and forth, bounded.
- **Literal:** a limit cycle / genuine periodic orbit — as opposed to bounded-but-aperiodic
  fluctuation, or damped oscillation toward a fixed point.
- **Obligation:** exhibit recurrence/periodicity on the dynamics, not merely non-convergence.
- **Seeded verdict:** **Conjectured** — needs a periodicity-vs-bounded-noise discriminator.
- **Discriminator:** a return map / Poincaré section showing a closed orbit, versus a shrinking
  or noise-filled one.

### (field, phase — scope-structure, deferred)
`field` is a scope-ladder / domain-with-dynamics claim whose genuine algebra is already the
ordered field 𝕂 (real math, named and kept). `phase` is the *tipping shape* of a
phase-transition, metastability-adjacent. Both are handled in a later round; neither is a
dynamics-earn of the kind above.

---

## 5. What Round 0 does and does not settle

**Settled by this note (Round 0):** the axioms exist; they are minimal and flagged; they are
consistent with — and modify nothing in — v5.3.3; they bridge to the committed §8.4/§8.7
micro-dynamics; and the Ledger is seeded for every target term in the corpus's own vocabulary.

**Not settled here (Rounds 1+):** any term's actual derivation; the A2 derivation debt
(inducing `T` from §8.4); and every seeded verdict above, which is a *first read*, not a
result.

**Round order by ripeness (revised under the grounded corrections):**

1. **reachability** and **momentum-shape** — the two **Derivable** targets (reachability from
   A3; momentum-shape from A4/§8.4). Ripest; earn first.
2. **metastability** — Conjectured; needs the flagged closure import.
3. **basin / attractor** — definitions Derivable; the specific-process claims Conjectured
   (convergence witness required); watch the exclusion-#19 landmine.
4. **transport** — Conjectured, likely resolved as shape-only.
5. **oscillation** — Conjectured; build the periodicity discriminator.

Each later round appends its verdict here and updates the running program record.

---

## Appendix — provenance discipline

Claims in this note are separated by **layer**, because a borrow's motivation and its license
are not the same thing:

- **Foundation (frozen v5.3.3):** the coordinates κ/φ/ρ, the sets `𝖠^m_t`/`𝖠^{+,m}_t`, the
  toolset `Tools^m_t`, the ordered field 𝕂, and the §8 micro-dynamics (§8.4/§8.7). Cited, not
  modified.
- **Research/applications layer (imported, flagged):** toolkit closure `Cl_𝒜(𝒯_t)`, the filter
  space 𝓕, the grokking transport map `T_ij`, the developmental-attractor framing. Used as
  scaffolding; never attributed to the freeze.
- **This note (posited):** the frame-state space `X`, its nearness `d`, the maps `T`, `T_u`,
  and the cost `c` — the minimal global dynamics against which the borrows are earned.

Nothing here is Demonstrated (a label the corpus does not use); nothing here merges to the
foundation; nothing here ships without the maintainer's review.
