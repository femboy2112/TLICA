# Round 1 — Earning *reachability* and *momentum* against the substrate

**Epistemic status:** Research note; **not foundation**. The verdicts below are **triangulated**
— each survived three independent adversarial bearings (well-posedness / proof-audit /
counterexample-hunt, §3) — and the one open decision they exposed (how A5 reconciles with the
frozen foundation's §7.4 entanglement) is resolved in the maintainer's chosen direction:
`Cl(Tools)` bounds reachability *from above*; reweighting respects the coupling. Labels use the
corpus vocabulary: **Derived / Conjectured / Refuted / UNVERIFIED** (no "Demonstrated").

**Depends on:** `research/dynamical_substrate_axioms_2026-09-08.md` (Round 0 — axioms A1–A5,
with A5 refined by this round's finding).

Round 1 took the two targets Round 0 marked ripest: *reachability* (from A3) and the *shape* of
*momentum* (from A4, grounded in §8.4). One earned cleanly; one earned in its core and **refuted
its own headline against a committed part of the foundation** — which is the rigor working, not
failing.

---

## 1. Reachability — CORE **Derived**; toolkit-as-exact-partition **Refuted**

**Shape (asserted by the corpus):** some route of admissible acts gets you from here to there.

**Literal claim to earn:** TLICA reachability *is* the control-theoretic reachable set.

### 1.1 The construction, stated so it is unconditionally well-posed

The draft defined `R(x)` as the image of a composite point-map `T_{u_{k-1}}∘…∘T_{u_0}(x)`. That
form is legitimate **only** for a total, single-valued `T_u`; for a partial `T_u` it has a
denotation gap, and for a relational (set-valued) `T_u` it type-errors. The well-posed statement
is the **reflexive–transitive closure**: `R(x)` is the least fixed point of the monotone operator

> `S ↦ {x} ∪ ⋃_{u ∈ U} T_u(S)`   on the complete lattice `2^X`.

Knaster–Tarski gives existence and uniqueness **unconditionally** — no continuity, no compactness,
no finiteness of `X`, and it covers total, partial, and relational `T_u` uniformly. Reflexivity
(`x ∈ R(x)`) and transitivity (`y ∈ R(x) ⇒ R(y) ⊆ R(x)`) are then *immediate* from the closure,
not separate obligations, and `R` is a preorder.

**Verdict (this part): Derived.** `R(x)` *is* the control-theoretic reachable set — a definitional
identity (reachability is order-theoretic; there are no units to mismatch), not a shape-analogy.

*Landmine, flagged for the future.* Transitivity is structurally unbreakable **only while `T_u`
is Markov** (admissibility depends on the current frame-state, which carries its own toolset
profile route-independently). The day the toolset is given a **consumable / use-once** component
— admissibility depending on *history* — transitivity is the first casualty. The axioms as
written keep `T_u` state-only, so this is out of scope; do not add a consumable without revisiting
this.

### 1.2 The headline that died: toolkit-as-exact-partition — **Refuted**

The draft claimed the reachable/unreachable partition *is* `Cl(Tools)`:

> `y ∉ R(x)` ⟺ every route to `y` needs a primitive *outside* `Cl(Tools)`.

**This biconditional is false**, and it fails against the *frozen foundation itself*. `Cl(Tools)`
is an invariant label along every admissible trajectory (A5 conjures and loses no primitive), so
it can certify reachability classes **only if reweighting acts independently across pathways** —
and §7.4 commits **coordinate entanglement** ("the coordinates influence one another … these are
dynamics, not definitions"), which is exactly the denial of that independence.

**Counterexample (exhibited, not fuzzed).** Two toolkit pathways `P_a, P_b`; frame-state = their
availability `(a,b) ∈ {0,1}²`; `Cl(Tools)` identical on every state. Encode a §7.4 coupling as a
*standing* (partial) constraint: `P_b` holds available only while `P_a` supports it (`raise_b`
undefined unless `a = 1`; `drop_a` undefined while `b = 1`). Then, from `(0,0)`:

```
R((0,0)) = {(0,0), (1,0), (1,1)}
unreachable: (0,1)
```

`(0,1)` — `P_b` available, `P_a` negated — is **not** reachable, has the **same** `Cl(Tools)`, and
needs **no** primitive outside the toolkit. The biconditional's left side is true, its right side
false. The smuggled step was reading "reweightable pathways within `Cl(Tools)`" as *each pathway
individually* (true here) instead of *the joint profile jointly* (false here). (Reproduction:
`scratchpad/reach2.py`.)

*Modelling lesson banked.* A one-shot coupling ("raising `a` forces `b`") **leaks** — a composite
path `raise_a` then `drop_b` walks around it (`scratchpad/reach.py`). Any entanglement the substrate
means to enforce must be a **state-space invariant** (a standing partiality of `T_u`), never a
transition side-effect.

### 1.3 Resolution (D1, maintainer's decision): bound from above, respect the coupling

- **`Cl(Tools)` upper-bounds reachability** — *reachable ⇒ the route stayed within `Cl(Tools)`* —
  **Derived** from A5(i) (admissible acts add no primitive outside the toolkit).
- **The exact reachable set is the entanglement-respecting sub-orbit** — the states attainable
  under reweighting that *obeys* §7.4 coupling. A5 is refined accordingly (reweighting is not
  independent across pathways). The *framing* is settled; the **sharp characterization** — computing
  the sub-orbit — requires §7.4's coupling encoded as a state-space invariant in the substrate,
  which is **Open** (Round 2+ work).

**Reachability, net:** core **Derived**; `Cl(Tools)`-as-upper-bound **Derived**;
`Cl(Tools)`-as-exact-partition **Refuted**; exact reachable set (the §7.4 sub-orbit) **Open**.

### 1.4 A positive by-product: reachability is discontinuous in frame-nearness

Well-posedness (§3) established that `x ↦ R(x)` is **discontinuous** in the A1 nearness `d`, and
this is *content*, not noise: since `d` is φ-style near-indistinguishability of frames,
**`d`-nearness carries no information about co-reachability** — two phenomenally
near-indistinguishable frames can have wildly different reachable sets. **Observed** result, and a
**tripwire**: any later round (metastability, basin/attractor) that leans on "near frames reach
near places" would lean on a continuity that provably does not exist here. Carried forward.

**Discriminator.** Membership `y ∈ R(x)?` is the observable (fixed `x`, discrete yes/no);
continuity of the reachable *set* is not among the observables and is not claimed. A refutation
would be an admissible sequence reaching a state declared outside the sub-orbit, or a
transitivity failure under Markov `T_u`.

---

## 2. Momentum — shape **Derived**, literal **Refuted**

**Shape (asserted):** an outlook has speed + direction + magnitude and resists turning, the more
so the harder it is already going.

**Literal claim:** `p = m·v` — conserved momentum, an independent mass, a force law `F = dp/dt`.

### 2.1 The shape, on the one functional that earns it

Write the interior update `f(w) = (1 − β)·w + α·(1 − w) = (1 − α − β)·w + α` (from §8.4, with the
rate hypothesis below). Two things pin the shape:

- **Resistance = extinction-work.** A4's datum — *turning against the current takes effort, more
  the harder you were going* — is **cumulative** work, so the resistance functional is the
  events-to-extinction count `N(w₀) = ⌈ log(ε/w₀) / log(1 − β) ⌉` (pure-decay channel). This is
  **strictly non-decreasing in the standing weight `w₀`** — a heavier pathway provably costs more
  reweighting-work to negate. **Derived.**
- **Retire the reversal-cost reading.** The instantaneous-response reading `|Δw(w)| = |α − (α+β)w|`
  is *non-monotone* — it is V-shaped, zero at the fixed point and maximal at both ends, so under it
  a strongly-set pathway is *easy* to move, the opposite of the shape. "Resistance" must be pinned
  to extinction-work; the reversal-cost sentence is dropped.

**The projection never clips.** `f(w) ∈ [0,1]` for *all* `(w, α, β) ∈ [0,1]³` (both terms ≥ 0;
`(1−β)w ≤ w` and `α(1−w) ≤ 1−w` sum to ≤ 1). So `Π_{[0,1]}` is the **identity** on the admissible
box — the "clips near `w = 1`" worry is vacuous, and every appeal to it is deleted. The map is
globally affine in `w` with constant slope `1 − α − β`.

**The real distinguished object: the fixed point `w* = α/(α+β)`.** For every genuine event
(`α + β > 0`, off the `(1,1)` corner) the slope has `|1 − α − β| < 1`, so the update **contracts to
`w*`**, never reaching either boundary. `w*` is where the reweighting response *flips sign* (above
it an imprint pushes `w` down, below it up). The shape is organized around `w*`, not the ceiling.
*(Note the target dependence: resistance-to-an-absolute-floor grows like `log w₀`; resistance-to-a-
relative-reduction, e.g. halving, is flat in `w` — the "scales with standing weight" claim holds
for the absolute-floor target. Do not slide between them.)*

**Rate hypothesis (flagged).** All of the above assumes `α, β ∈ [0,1]`. §8.8 explicitly declines
to fix rates, so this is an **added research-layer posit**, not a foundation commitment — but it is
well-motivated (`α`, `β` are imprint/decay fractions) and without it `Π` can bind (`α = 1.5` clips).

### 2.2 The literal, refuted — and my own first argument corrected

The literal is a conjunction (conserved-`p` ∧ independent-mass ∧ force-law); negating any conjunct
kills it, and two die **structurally**:
- **No independent mass.** The "magnitude" *is* the weight `w`; there is no second invariant to
  play `m`. `p = m·v` needs `m` independent of `v`; none exists.
- **No force law.** §8.4 is discrete, event-triggered reweighting — no `F = dp/dt`.

Either suffices; both hold. **Refuted** — a *legitimate* downgrade to reweighting-inertia /
hysteresis / control-cost.

*Correction to the draft's argument.* The draft also leaned on "the §8.4 map conserves nothing."
**That is false.** At the corner `α = β = 1` the update is `f(w) = 1 − w`, a reflection that
*exactly* conserves `Q(w) = (w − ½)²` on a period-2 cycle `{w, 1−w}`. But `Q` is **not** `p = m·v`
(no mass, no force), and the corner is non-generic (every real event strictly contracts), so the
**Refuted** verdict stands on the two structural legs — while the honest write-up now *names* the
one invariant rather than denying its existence. (Reproduction: `scratchpad/probe.py`.)

**Discriminator.** Is any quantity conserved along a *generic* orbit? (No — strict contraction to
`w*`; the only exact invariant sits at the `(1,1)` reflection corner.) Is extinction-work monotone
in `w₀`? (Yes, on all of `(0,1]`.)

---

## 3. Adversarial triangulation (all three bearings returned; convergent)

- **Well-posedness (hadamard):** certified `R(x)` well-posed **only** under the least-fixed-point
  restatement (the composite-point form was legitimate for total single-valued `T_u` only);
  established the `d`-discontinuity as off-target for attainability but a real downstream tripwire;
  showed `Π` inert on `[0,1]³` and identified `w*` as the true distinguished object; flagged the
  `α,β ∈ [0,1]` hypothesis. Probes scouting-grade (**Observed**).
- **Proof-audit (lagrange):** split the reachability boundary into an upper-bound half (free from
  A5) and a saturation half (not free); certified reflexivity/transitivity/preorder; certified the
  literal-momentum **Refuted** as over-determined (mass + force law), independent of any invariant
  hunt; flagged that "resistance" was not a single functional.
- **Counterexample-hunt (dalembert):** **killed** the toolkit-as-partition biconditional with the
  `(0,1)` §7.4-entanglement counterexample; **killed** the draft's "conserves nothing" plank with
  the `α=β=1` invariant `Q(w)=(w−½)²`; confirmed the `Π`-clip appeals vacuous; could not break
  reflexivity or transitivity (noting the consumable-tool path-dependence crack, out of the stated
  model). Bounded on invariants of varying-parameter event *sequences* — not exhaustively hunted.

Scratch harnesses (read-only): `scratchpad/{probe.py, reach.py, reach2.py}`.

---

## 4. Ledger (Round 1, triangulated)

| claim | verdict | basis / boundary |
|---|---|---|
| `R(x)` is the control-theoretic reachable set; reflexive, transitive, preorder | **Derived** | least-fixed-point identity; Markov-only (consumable tools break transitivity) |
| `Cl(Tools)` upper-bounds reachability | **Derived** | A5(i) |
| `Cl(Tools)` *is* the exact reachable partition | **Refuted** | §7.4 entanglement; counterexample `(0,1)` |
| exact reachable set = §7.4-entanglement-respecting sub-orbit | **Open** | framing settled (D1); sharp characterization needs §7.4 encoded (Round 2+) |
| reachability discontinuous in frame-nearness `d` | **Observed** | positive result + tripwire for Round 2+ |
| momentum *shape* (inertia scaling with standing weight) | **Derived** | extinction-work functional `N(w₀)`, monotone; organized around `w*` |
| momentum *literal* `p = m·v` | **Refuted** | no independent mass, no force law (over-determined) |
| momentum: §8.4 has a conserved quantity | **Refuted (generic)** | strict contraction to `w*`; lone invariant `Q=(w−½)²` at the `α=β=1` corner only |

---

## 5. Forward

**Round 2 — metastability** (needs the flagged toolkit-closure import), carrying three constraints
this round produced: (i) **no continuity** — the `d`-discontinuity forbids "near frames reach near
places"; (ii) **§7.4 coupling discipline** — any entanglement must enter as a state-space invariant,
or a composite path evades it; (iii) **`w* = α/(α+β)`** is a live **attractor** candidate in
weight-space, to be picked up in Round 3 (basin/attractor). Metastability's exit-time separation
will be posed against the contraction-to-`w*` dynamics, not against a bare "sticky region."
