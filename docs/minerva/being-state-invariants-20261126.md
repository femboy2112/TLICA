# Being-state invariants: identity, trait, affect, embodiment, presentation

**Order:** GOD / T3, 2026-11-26. **Tier:** TLICA theoretical liaison (docs only).
**Scope:** the public, abstract half of T3. It states the invariants a synthetic character's state must keep so that
changing an outfit, a body, an inference model or a mood never rewrites who the character is. Property-test shapes are
given for a character host and a character-runtime library. The mapping onto named host types is routed privately.

**Ledger labels:** Demonstrated · Observed · Conjectured · Refuted · UNVERIFIED. These are definitions and their
consequences, Demonstrated by construction unless labelled otherwise. Nothing here describes any implemented system.

---

## 1. The strata

A Being's state is not one object. It is a **stack of strata**. Each stratum is defined by *who may write it* and *how
fast it moves*, not by its content: "curious" can be a trait *and* an affect.

| Stratum | Content | Writer | Timescale |
|---|---|---|---|
| **S0 lineage** | which being this is | creation only | never changes; a different value means a different being |
| **S1 character** | traits, values, voice, temperament, commitments | an operator-approved revision | revision-scale |
| **S2 envelope** | initiative, autonomy, limits, repair norms | an operator-approved revision | revision-scale |
| **S3 history** | eligible memory, the relationship | source-aware durable writes and attended corrections | event-scale, durable |
| **S4 living state** | affect, attention, intentions | the reducer, from journalled events | seconds to hours; decays |
| **S5 embodiment** | the selected body, wardrobe, appearance, motion preferences | an operator choice, versioned | revision-scale; **part of the self-description, not of cognition** |
| **S6 presentation** | the current pose, expression, gaze, garment motion | the realization runtime | frame-scale; ephemeral |
| **E engine** | the inference model, templates, sampling | deployment | **not part of the Being at all** |

**Causal direction.** Lower strata condition higher ones: character and living state, through embodiment, produce
presentation. Higher strata **never write** lower ones. The only path upward is **observation**: something that happens to
the presentation (or in the world) may enter S4 *as a journalled event*, never as a direct write.

```
S0 → S1,S2 → S3 → S4 ─┐
                      ├→ semantic expression request → S6 (realization)
         S5 ──────────┘
E realizes S4→S6 choices; E is never stored in S0–S5.
S6 / world ──(observation event, through the reducer)──→ S4 only
```

## 2. Invariants (non-interference)

Write Π_X(s) for the byte projection, or digest, of state *s* onto strata X. Each invariant says that a class of operations
is **non-interfering** with a protected set of strata.

| # | Operation class | Must leave unchanged | Notes |
|---|---|---|---|
| **B1** | outfit, garment or material change | Π_{S0–S4}, and the **neutral body** of S5 | It may change S5's wardrobe and S6 realization parameters (support, compression, movement constraints). Those effects are reversible. |
| **B2** | body edit | Π_{S0–S4} | It produces one coherent embodiment revision (geometry, skeleton, skinning, collision, garment fits, motion calibration) *together*. A partial revision is not representable. |
| **B3** | inference-model swap | Π_{S0–S5} | The engine is not in the Being. The same events produce the same state digest under any engine. |
| **B4** | affect or attention event | Π_{S0–S3}, Π_{S5} | Affect never writes character. See B7 for how traits may legitimately change. |
| **B5** | presentation or realization tick | Π_{S0–S5} | Realization is read-only on the Being. |
| **B6** | approved character revision | Π_{S0}; S3 and S4 continue | A revision is not a new being. Memory, relationship and living state carry across it by an explicit migration, never by reset. |

**Structural invariants:**
- **B7 No silent drift.** The S1 digest changes **only** in an event that carries an operator approval. Long-run affect may
  *propose* a trait change, which then waits for approval. It never accumulates into one.
  - *Design note:* TLICA's own human dynamics let a baseline chase its target (the driven allostatic orbit, `foundation/3`
    §8.10). A synthetic character deliberately sets that drift rate to zero except by approval. This is a product choice
    that is **stricter than TLICA's model of people**, and it should be stated as a choice, not as a fact about selves.
- **B8 Upward only by observation.** Every S4 change traces to a journalled event with a host-assigned origin. An outfit or
  body change may *emit* an observation event (for example, the operator commenting on it). It never writes affect
  directly.
- **B9 Fiction is ephemeral.** Events whose epistemic kind is quoted fiction or an unverified model claim change no S4 state
  and advance no version. (This is the T2 frame-non-crossing invariant, applied to living state.)
- **B10 Commutation.** An outfit change and an affect event commute on Π_{S0–S5}: o∘a(s) = a∘o(s). The same holds for an
  engine swap with any event.
- **B11 Reversibility.** remove(g)∘add(g) = id on the neutral body. Footwear changes stance and contact calibration, never
  limb lengths.
- **B12 No catch-up.** S6 at time *t* is a function of the current S4/S5 and the clock, not of missed frames. Returning from
  a hidden period never replays stale expression.
- **B13 One identity word per stratum.** "Identity" must name exactly one thing. Lineage identity (S0) is not visual
  recognisability (the appearance anchors in S5), and neither is engine identity (E). Switching appearance or engine
  never switches the being, and the lineage key is the only identity used for joins.

## 3. Property-test shapes

These are generic, for a character host and a character-runtime library. Generate random states *s* and random operation
sequences over the classes above.

1. **Projection equality.** For each Bk: `digest(Π_protected(op(s))) == digest(Π_protected(s))`.
2. **Approval gate (B7).** Over any sequence without an approval event, the S1 digest is constant. Then inject one approval:
   exactly that event changes it.
3. **Causal trace (B8).** For every S4 diff there is exactly one journalled event with a host origin. Outfit, body and
   engine operations contribute no S4 diff.
4. **Engine invariance (B3).** Replay one event log under two engines; the S0–S5 digests are equal. (Replies may differ.
   Reply fidelity is a *realization* question, measured separately, not an identity question.)
5. **Commutation (B10).** For random pairs (o, a), the digests of o∘a and a∘o agree on S0–S5.
6. **Body coherence (B2).** After any body edit, every derived artifact carries the same embodiment revision id. A mixed
   revision is rejected.
7. **Reversibility (B11).** For each garment g, apply then remove: the neutral body is byte-identical. A footwear swap
   leaves limb lengths byte-identical.
8. **No catch-up (B12).** Hide for Δ, then show: the first realized frame equals a fresh realization of the current state,
   with no intermediate cues emitted.
9. **Revision continuity (B6).** An approved S1/S2 revision keeps S3 and S4 (after the declared migration) and S0. The
   being's history is never reset by a revision.

## 4. Open design question (for the owner)

> **Resolved (T4):** the owner chose a frozen base, with growth through an approved, revisable colouring layer of
> sub-Beings. See [base ⊕ colouring](being-colouring-composition-20261126.md) §5, which splits S1 into S1b and S1c.

If traits live in the **same immutability class as lineage** (changeable only by creating a new being), then B6 is vacuous
and B7's approval path does not exist: a character could never grow without losing its history. Whether character should
be revisable *without* a lineage change is a values decision for the owner, not a formal one. The invariants above assume
it is revisable by approval.

## 5. Boundaries

- This is a formal proposal. The status words describe the definitions, not any running system.
- The mapping onto named host types, and the gaps found there, are private and routed to their owners.
- Character-runtime test shapes B2, B11 and B12 concern the public character-runtime work; they are proposals, not results.
