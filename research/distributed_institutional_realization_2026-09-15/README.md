# Distributed Institutional Realization

*Institutional macrostates, local discontinuity, and social structure without a group mind*

**Author:** Leah. AI-assisted formulation, research, and editing.
**Version:** research draft **v0.2.0**, 2026-09-15 (supersedes the v0.1 seed, retained below as provenance).
**Foundation:** TLICA v5.5.0 — **untouched.** Research-tier; not a registered application paper.

> An institution can be real without being a person. The v0.2 draft models it not as a
> document, a sum of people, or a renamed tuple, but as a **task-relative macrostate**: an
> equivalence class of distributed micro-realizations that preserve the same
> intervention-response geometry. A government persists through complete personnel turnover
> because the response geometry survives; the same personnel can stop being that institution
> the moment a load-bearing authority relation is cut.

---

## What changed in v0.2 — three levels, not a renamed tuple

The v0.1 seed risked defining the institution as its own inputs under a new name,
`𝕽_t(P_t,R_t,D_t,S_t)=I_t`. v0.2 separates three distinct levels:

1. **Micro-realization** — `X_t=(P_t,R_t,D_t)`: indexed agent profiles `P`, typed
   agent/artifact relations `R`, artifacts/records `D`. The situational field `S_t` is kept
   **external**.
2. **Institutional macrostate** — for a declared task family `T`, two micro-realizations are
   equivalent, `X~_T X'`, when their response signatures `Σ_T` agree over the whole
   admissible situation/intervention domain. The institution is the quotient class
   `I_t^T=[X_t]_{~_T}`.
3. **Situation, activation, output** — `Y_{t+Δ}=𝒜_T(I_t^T,S_t,U_t)`. A fire is not part of
   the fire department merely because it activates it.

This gives the institution object real formal work: it is a **quotient**, strictly coarser
than the micro-realization, and the response map factors uniquely through it (Proposition 1,
manuscript §7). Distinct carriers realize the same macrostate exactly when they preserve the
task-relevant response geometry.

The central observer-relative claim is unchanged and stays **Conjectured**:

> **Apparent local discontinuity can be the projection of distributed causal structure onto
> an insufficient local frame.**

## Reading path

- [**MANUSCRIPT_DRAFT_V0_2_0.md**](MANUSCRIPT_DRAFT_V0_2_0.md) — the canonical first full
  revised manuscript. Micro/macro/situation separation, the exact factorization proposition,
  persistence under carrier substitution, the local predictive-gap formulation, revised claim
  statuses (§25), and the next computational program (§18).
- [**quotient_demo.py**](quotient_demo.py) · [results](quotient_demo_results.json) ·
  [tests](quotient_demo_tests.txt) — **NEW, executed.** The v0.2 manuscript's Probe A
  (§18.1): a deterministic standard-library witness of the quotient/factorization construction.
- [**badge_door_demo.py**](badge_door_demo.py) · [results](badge_door_demo_results.json) ·
  [tests](badge_door_demo_tests.txt) — the v0.1 finite access-control model, retained with its
  evidential status **narrowed** by v0.2 (see below).
- [**CLAIM_LEDGER.md**](CLAIM_LEDGER.md) — v0.1 ledger with a **v0.2 status-update block** at
  the top (C-006 split, C-016/C-022 construction-level, C-008/C-025 unchanged).
- [**RECONCILIATION.md**](RECONCILIATION.md) — audit against `main` (the anti-group-mind
  premise is *already* on main via the agency papers) with a **v0.2 addendum**.
- [**PROBE_AND_PRIOR_ART_PLAN.md**](PROBE_AND_PRIOR_ART_PLAN.md) — falsification / prior-art
  program.
- [**LOCAL_CLAUDE_MAINLINE_HANDOFF_V0_2_0.md**](LOCAL_CLAUDE_MAINLINE_HANDOFF_V0_2_0.md) ·
  [MAINLINE_INTEGRATION_HANDOFF.md](MAINLINE_INTEGRATION_HANDOFF.md) — integration handoffs
  (v0.2, then v0.1).
- [**MANUSCRIPT_SEED.md**](MANUSCRIPT_SEED.md) — the original 34-section v0.1 seed, kept as
  provenance.

## What the executed quotient demo shows

`quotient_demo.py` builds a tiny "who may approve request-type `k`" institution and runs the
v0.2 construction. Executed results (**12/12 self-checks**, deterministic, standard library):

- **Distinct realizations, one institution.** Six micro-realizations differing in people,
  headcount, and record labels collapse to exactly **three** macrostates. Three of them —
  different people, different counts — share a response signature and land in one class:
  carrier substitution preserves `I^T`.
- **Relations beat persons — and this is construction-level.** Cutting one load-bearing
  authority relation moves a realization to a *different* class even when the people are
  unchanged; a pure carrier permutation keeps the class. (Because `Resp_T` reads roles and
  situation and never person identity — role-relativity is built in, not discovered.)
- **The factorization is exact.** The induced `Respbar_T` is single-valued on each class and
  reproduces `Resp_T` on **all 36** `(X,s,u)` cells with zero mismatches — Proposition 1,
  executed. The quotient is strictly coarser than identity, so `I^T` carries strictly less
  than `X`.
- **Approximate equivalence is not automatically transitive.** An explicit counterexample
  exhibits `a₁~a₂` and `a₂~a₃` but not `a₁~a₃` at tolerance `ε=1`, confirming the manuscript's
  §6.2 refusal to write `[X]_{~_{T,ε}}` without a transitivity check.

**What the demo is NOT.** A finite constructive witness that the v0.2 construction is coherent
and does what the manuscript says — **Disclosed inside the formal model.** Not a model of any
real institution; not empirical validation (C-006's empirical usefulness stays **UNVERIFIED**);
not a novelty claim (C-025 **UNVERIFIED**).

## Correction to the badge-door evidence

The v0.1 badge-door model remains a useful finite consistency witness, but v0.2 narrows what
it licenses:

1. **Identity-correlation invariance is constructed, not discovered.** `rho_institution` is
   deliberately never read by the access decision. The model proves the logical *possibility*
   of ρ/operational dissociation, not a general empirical independence (C-022).
2. **Role-holder substitution succeeds by construction.** Authorization attaches to the
   `employee` role, not a named person — one coherent role-relative architecture, not a proof
   that real institutions track roles over persons. The `M_role` vs `M_person` discriminator
   has not been run (C-016).
3. **The nominal 2×2×2×2 grid is a serial-gate pipeline, not an orthogonal factorial.** A
   missing relation censors downstream source/activation; an invalid source returns before
   activation. Its correct status is **pipeline trace / finite consistency witness** — no
   mixed-term claim may be drawn from it.

## Non-negotiable constraints

1. **No group-mind reification.** The institutional macrostate is not a phenomenal subject.
2. **No vector-space cosplay.** People carry local structure; a coefficient vector is not the
   institution.
3. **No causality by naming.** Institutional causal shorthand must expand into indexed
   implementation paths.
4. **No foundation promotion by elegance.** The quotient construction stays application-level
   unless repeated cross-application necessity is demonstrated.
5. **Situation is not institution.** `S_t` is external to `I_t^T` — now enforced by
   construction.
6. **Approximate equivalence is not automatically an equivalence relation.** Check
   transitivity before quotient notation (exhibited non-transitive in the demo).
7. **Sheaf language stays gated.** No literal sheaf claim without base, cover, sections,
   restrictions, compatibility, gluing, obstruction, and observable consequence.
8. **C-025 remains UNVERIFIED.** No novelty claim before primary-source rival-framework
   tomography.

## Scope, provenance, and the two open debts

Landed **research-tier**, foundation **untouched**, **not** registered as an application paper.
By the package's own promotion criteria (no discriminator survived controls, no rival-formalism
comparison, no primary-source matrix) it is not application-paper-eligible; it is a candidate
*future* paper. Its two load-bearing claims stay **UNVERIFIED**:

- **C-006 (empirical half):** whether task-relative institutional quotient macrostates are
  *useful and stable* in real or independently specified domains. (The formal half — the
  quotient is not the raw tuple and factors the response map — is now Disclosed *and executed*.)
- **C-025:** whether the account out-predicts network theory, distributed cognition, role
  theory, institutional economics, social ontology, or distributed systems. No novelty is
  claimed until a primary-source comparison is done.

## Reproduce the check

```bash
cd research/distributed_institutional_realization_2026-09-15
python3 quotient_demo.py --output quotient_demo_results.json   # 12/12 self-checks, exit 0
python3 badge_door_demo.py --output badge_door_demo_results.json  # 14/14 self-checks, exit 0
```

---

Return to the [research index](../README.md) · plain-language page:
[docs/distributed-institutional-realization.md](../../docs/distributed-institutional-realization.md).
