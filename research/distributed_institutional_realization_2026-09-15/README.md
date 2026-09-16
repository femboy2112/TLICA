# Distributed Institutional Realization

**Local discontinuity, relational causation, and social structure without a group mind**

**Author:** Leah. **Version:** research draft v0.1.0, 2026-09-15. AI-assisted formulation, research, and editing. This is a research-program seed for author review — a candidate *future* application paper, **not** an empirically validated application and **not** a change to the frozen foundation (v5.5.0).

> An institution can be real without being a person. Its reality can consist in the presently realized organization of indexed people, their profile-conditioned dispositions, typed relations, artifacts, records, and situational constraints — and from inside a small observational frame, the activation of that distributed structure can look abrupt.

## Core question

How can socially real structures — governments, courts, firms, offices, procedures, currencies, norms — be causally effective through indexed people, typed relations, artifacts, records, and situational conditions **without** either (1) reducing the institution to a document or a sum of beliefs, or (2) reifying it into an unindexed group mind?

The seed proposes an application-level realization map

\[
\mathcal I_t = \mathfrak R_t(\mathbf P_t, \mathbf R_t, \mathbf D_t, \mathbf S_t),
\qquad
\mathscr A_t : \mathcal I_t \to \Delta\mathcal W_t,
\]

with `P_t` indexed agent profiles, `R_t` typed role/authority/communication/obligation relations, `D_t` artifacts and records in primal not-I, `S_t` the situational field, and `I_t` the realized institutional configuration — **not** a subject, not a group mind. Every arrow `𝒜_t` must be expandable into an indexed path through actual agents, artifacts, messages, records, role activation, and physical action. The working slogan:

> **Apparent local discontinuity can be the projection of distributed causal structure onto an insufficient local frame.**

## Reading path

- [MANUSCRIPT_SEED.md](MANUSCRIPT_SEED.md) — the self-contained 34-section seed: definitions, the vector-insufficiency argument, government and badge-door worked examples, the local-projection proposition, failure taxonomy, candidate invariants, predictions P1–P10, rival models, anti-reification discipline, and explicit nonclaims (§32).
- [RECONCILIATION.md](RECONCILIATION.md) — the Stage-1 audit against current `main`: every reused concept mapped to the existing object that owns it (with citations), an overlap/conflict verdict, and the integration action. Key finding: the founding premise is **already on main** (the agency papers' institutional clause); this is an extension, not a new primitive.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md) — epistemic status of all 25 load-bearing claims (Disclosed / Observed / Conjectured / UNVERIFIED / Dark / Refuted). The two highest debts — **C-006** (is `I_t` more than a renamed tuple?) and **C-025** (TLICA-specific gain over rivals) — remain **UNVERIFIED**.
- [PROBE_AND_PRIOR_ART_PLAN.md](PROBE_AND_PRIOR_ART_PLAN.md) — the falsifiable program: discriminating probes, the complete factorial, hostile cases, the sheaf-formalization gate, and the primary-source prior-art matrix required before any novelty claim.
- [MAINLINE_INTEGRATION_HANDOFF.md](MAINLINE_INTEGRATION_HANDOFF.md) — the audit-and-integrate instructions for a local session (the reconciliation above discharges its Stage-1 step).
- [badge_door_demo.py](badge_door_demo.py) · [badge_door_demo_results.json](badge_door_demo_results.json) · [badge_door_demo_tests.txt](badge_door_demo_tests.txt) — the badge-controlled-door toy world (manuscript §14 / probe plan §2), **actually implemented and executed**: the baseline authority path, eight ablations, and the full 2×2×2×2 factorial, with raw outputs and self-checks. It demonstrates a mathematical possibility and internal consistency — **not** a model of any real organisation or person.

## What the executed demo shows (and does not)

The finite model realizes one institutional micro-fact — "the door opens for the agent at it" — and reads off the outcome, provenance verdict, and failure class. Executed results (14/14 self-checks pass):

- The **eight ablations** behave as the manuscript's failure taxonomy (§13) predicts: a cloned badge with no authorization relation, a deleted record, a severed controller↔DB path, a forged source, an expired window, and conflicting replicas all fail closed — each with its distinct failure class; **replacing the employee with a compatible role-holder still opens** (access follows relational state, not the person — C-016 / prediction P2), while **keeping the person but cutting the authorization edge closes** it.
- The **2×2×2×2 factorial** over relation × source × activation × identity-placement: exactly **2 of 16** cells open, and the identity-placement axis is **inert** — for every fixed (relation, source, activation) the two identity levels agree. That is claim **C-022** (identity-correlation dissociates from causal participation) shown in a finite model, not asserted.

The demo tests the scaffold's internal consistency and its discriminators. It is **not** empirical validation of the social theory (manuscript §30), and it does not discharge C-006 or C-025.

## Non-negotiable constraints (carried from the seed)

1. **No group-mind reification.** An institution is causally real as a distributed pattern, never a subject.
2. **No vector-space cosplay.** A coefficient vector over persons loses typed relations; the vector image is intuition only (manuscript §3).
3. **No causality by naming.** `institution → outcome` is shorthand until an indexed path is supplied.
4. **No foundation promotion by elegance.** `𝕽_t`, `I_t`, `𝒜_t` stay application-level unless independent cross-application necessity is shown.
5. **Emergent ≠ fictional; distributed ≠ conscious; socially real ≠ ontologically primitive.**
6. **Local discontinuity is a projection claim, not a universal excuse** — the model must name the hidden path and predict the interventions that sever it.

## Scope and provenance

Base: `femboy2112/TLICA`, `main` at foundation **v5.5.0**. Research branch of origin: `research/distributed-institutional-realization-2026-09-15`. This package is landed **research-tier** — dated, un-versioned, foundation untouched — alongside the other dossiers in [`research/`](../README.md). No application paper is registered and no foundation or Makefile `PAPERS` change is requested. Repository applications are theory sources, not independent empirical witnesses.

## Reproduce the executed check

```bash
python3 research/distributed_institutional_realization_2026-09-15/badge_door_demo.py \
    --output /tmp/badge-door-results.json
```

Python 3.8+, standard library only, deterministic (no randomness, no clock). The recorded run used Python 3.12.3 and passed 14 self-checks. No human-subject study or empirical reanalysis was run.

Return to the [research index](../README.md).
