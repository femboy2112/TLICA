# Reconciliation Against Current Main

This file is the Stage-1 deliverable the [handoff](MAINLINE_INTEGRATION_HANDOFF.md)
requires before any integration: an audit of every concept the seed reuses against
what `main` already owns, with real citations, an overlap/conflict verdict, and a
proposed action. It was produced by a local session with the repository checked out.
The finding, in one line: **the seed reuses existing machinery and introduces no new
foundation primitive; it is an application-level *extension of an institutional clause
the agency papers already state*, and it lands research-tier with its central claims
still UNVERIFIED.**

## Repository state at audit

- Base: `femboy2112/TLICA`, `main` at the commit this package was landed on (see the
  git log for this directory's add commit).
- Foundation version on main: **v5.5.0** (`foundation/0_reading_guide.md`). The seed's
  own `v5.5.0` dependency line is therefore current, not stale.
- Baseline `make validate` (link + self-containment + math-term gates): PASS before and
  after adding this package (the package carries no absolute self-repo URLs and its
  internal links resolve; the math-term scanner treats `research/` as corpus, and every
  watched stem the manuscript uses is already pinned — see the term-gate row below).
- No foundation file is touched by this package. No application paper is registered.

## The load-bearing prior fact

`main` already licenses institutional analysis without a group mind, nearly verbatim,
in the frozen-adjacent application layer:

> "The architecture is perspectivally realist about other agents and can analyze
> **collective and institutional structures through role-indexed profiles and relational
> cascades, without positing an unindexed group mind.** ... Multi-agent and group cases
> are decomposed into indexed agent-profile sets plus relational structure, not aggregated
> into a single unindexed perspective."
> — `applications/free_will_v0_3_0.md:100,122`; identical clause at
> `applications/agency_architecture_v0_3_0.md:101`; cf. `applications/caves_lagrange_points_v0_1_0.md:837`
> ("any collective extension must be role-indexed and relational rather than a simple
> scaling-up of the individual profile").

So the seed's founding premise (ledger **C-001**) is **Disclosed** — already on main. The
seed is best read as *naming and formalising the object that clause gestures at* (the
realized institutional configuration `I_t`), not as a new commitment. That framing is
what keeps it honest: the novelty it must still earn is the *usefulness* of naming that
object (C-006) and any TLICA-specific predictive gain (C-025), not the permission to
analyse institutions at all.

## Reconciliation table

| Seed concept | Existing main object (citation) | Overlap | Conflict? | Action |
|---|---|---|---|---|
| Indexed institutional analysis w/o group mind (C-001) | role-indexed profiles + relational cascades, anti-group-mind (`free_will_v0_3_0.md:100,122`; `agency_architecture_v0_3_0.md:101`) | near-total | none | **absorb**: present `I_t` as extension of this clause, not a new claim |
| `cultural-I` as distributed pattern, not a mind (C-002, C-023) | `docs/app-referent-routing.md:412,464` ("the cultural-I is *not* a mind"); `applications/referent_routing_*` | partial | **no**, if boundary held | **cross-reference + boundary**: cultural-I = one *encoding* component; `I_t` adds typed roles, artifacts, records, paths. Do **not** widen cultural-I |
| Typed relational structure `R_t` (C-004, C-005) | integration graphs (`docs/app-choice-as-filter.md:213`; `applications/choice_as_filter_v0_1_0.md:396,1070`); relational cascades | partial | none | **formalize-existing**: `R_t` is a typed graph over agents+artifacts; note it as richer-typed than the lived-I integration graph |
| Situational field `S_t` (C-024) | situational field `S`, pinned off the scope ladder (`docs/glossary.md:205`) | direct term reuse | **would conflict** if `S` absorbed into `I` | **keep distinct**: reuse `S` as-is; require interventions that vary `S` with `I` fixed and vice versa |
| Source-path / provenance `SrcPath(x)` (C-015) | sourcehood / source-path machinery (`docs/glossary.md`; `docs/substrate-focus-and-imprinting.md`; `docs/app-agency-architecture.md`, `app-free-will.md`, `app-choice-as-filter.md`) | strong | none | **reuse, don't duplicate**: no new authority scalar; extend existing source-path status to directives |
| Formation vs activation (C-009) | formation/activation + osmotic mechanism-online (`docs/modes-of-development.md`; foundation §8.7, §4.4/4.6/4.7) | direct | none | **reuse**: role latency = long-lived formation + quiet maintenance + trigger; no duplicate role-state primitive |
| Osmotic imprinting of lived institutions (C-014) | osmotic imprinting (`docs/modes-of-development.md`, `docs/app-out-of-the-cave.md`; foundation §8.7) | direct | none | **reuse + name-discipline**: must not rename ordinary implicit learning; state what profile/source structure adds |
| Interface compatibility over global similarity (C-010, C-020) | semantic interoperability (`docs/app-this-is-water.md`, `docs/app-shared-reality-divergent-maps.md`) | strong | none | **cross-reference**: institutional coordination = a semantic-interoperability instance |
| Identity-correlation ρ vs causal participation (C-022) | ρ / identity-correlation profile (`docs/identity-correlation-profile.md`; foundation §7.6) | reuse of ρ | none | **keep dissociated**: ρ toward an institution ≠ operational participation. Demonstrated inert for access in `badge_door_demo.py` |
| Realization map `𝕽_t`, object `I_t`, action map `𝒜_t` (C-006) | — (no existing object) | none | **potential over-reification** | **application-level, UNVERIFIED**: keep unless it earns an invariant/discriminator; delete if it reduces to the raw tuple |
| Sheaf-like formalization (C-011) | — (borrowed math term, not on main) | none | drift risk | **gate + pin**: "sheaf-like" fenced as disciplined metaphor (manuscript §7.5); pinned in `docs/glossary.md`, added to `scripts/math_terms.txt` |

## Term-gate result

The math-term scanner (`scripts/check_math_terms.py`) scans `research/`, so the manuscript
enters the drift corpus. Every watched stem it uses heavily — `vector` (its §3), `basis`,
`metric`, `projection`, `field`, `reachab`, `topolog` — is **already pinned** in
`docs/glossary.md`; adding the manuscript only raises already-pinned counts, so the gate
stays green. The one genuinely-new borrowed term is **sheaf**, used technically-but-fenced;
this package adds it to the watchlist and pins "sheaf-like" in the glossary, so the
discipline the manuscript preaches (C-011's sheaf gate) is enforced on the manuscript itself.

## What the audit does *not* change

The reconciliation confirms provenance and boundaries; it does **not** discharge the two
highest debts. **C-006** (is `I_t` more than a renamed tuple?) and **C-025** (TLICA-specific
gain over network theory / distributed cognition / role theory / social ontology) remain
**UNVERIFIED**. The badge-door demo shows internal consistency and the ρ/participation
dissociation in a finite model; it is not a discriminator against a rival formalism, and no
primary-source prior-art matrix has been built. Promotion past research-tier stays gated on
the [probe plan](PROBE_AND_PRIOR_ART_PLAN.md).

Return to the [package README](README.md) or the [research index](../README.md).
