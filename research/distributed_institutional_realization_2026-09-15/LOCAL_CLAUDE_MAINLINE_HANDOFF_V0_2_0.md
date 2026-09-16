# Local Claude Mainline Handoff — Distributed Institutional Realization v0.2.0

You are taking over the mainline integration of the revised Distributed Institutional Realization manuscript in `femboy2112/TLICA.git`.

Source branch:

`research/distributed-institutional-realization-manuscript-v0.2.0-2026-09-15`

Primary source file:

`research/distributed_institutional_realization_2026-09-15/MANUSCRIPT_DRAFT_V0_2_0.md`

This is a revision of the research-tier package already on main. Do not merge blindly. Internalize the strongest surviving structure into current main, preserve the epistemic ledger, and repair any conflicts exposed by current repository state.

## Core revision

The v0.1 scaffold risked defining the institution object as a renamed tuple:

`I_t = Rfrak_t(P_t, R_t, D_t, S_t)`.

v0.2 repairs this by separating three levels:

1. **Micro-realization**

   `X_t = (P_t, R_t, D_t)`

   containing indexed profiles, typed relations, and artifacts/records.

2. **Institutional macrostate for declared task family T**

   Define response signature

   `Resp_T(X; s, u)`

   over admissible situations `s` and interventions/inputs `u`.

   Define

   `X ~_T X'`

   iff the response signatures agree for every admissible `(s,u)`.

   Then

   `I_t^T = [X_t]_{~_T}`.

   The institution is therefore a task-relative equivalence class of distributed micro-realizations, not the tuple renamed.

3. **Situational activation and output**

   `Y_{t+Δ} = A_T(I_t^T, S_t, U_t)`.

   The situational field is EXTERNAL to the institutional macrostate. A fire is not part of the fire department merely because it activates it.

This gives the institution object actual formal work: distinct carriers can realize the same macrostate when they preserve the task-relevant intervention-response geometry.

## New formal result

The manuscript states an elementary but real quotient/factorization proposition:

If `~_T` is equality of the full response signature, then the response map factors uniquely through the quotient:

`X -> q_T(X)=I^T -> Respbar_T`.

This is not novel mathematics. Its value is architectural: it licenses `I^T` as a causal macrostate for a declared task and makes the institution strictly different from its micro-realization tuple.

Update claim C-006 accordingly:

- OLD: usefulness of `I_t` entirely UNVERIFIED / may be a renamed tuple.
- NEW: **Disclosed inside the formal model** that the quotient macrostate is not the raw tuple and supports exact response factorization; **empirical usefulness remains UNVERIFIED**.

Do not upgrade beyond that.

## Critical correction to the existing badge-door interpretation

The current mainline badge-door toy is useful but its claims need tightening.

### Identity axis

`rho_institution` is explicitly never read by the access decision function.

Therefore the result

`identity axis never changes access`

is stipulated by model construction, not discovered by the factorial.

Correct interpretation:

> The existing model is a constructive existence witness that identity-correlation and operational access can dissociate coherently.

It does NOT establish empirical or general causal independence.

Update C-022 accordingly:

**Disclosed as a logically coherent dissociation in the finite model; empirical prevalence/coupling UNVERIFIED.**

### Role substitution

The current record authorizes `subject_role="employee"`, not a named agent. Therefore employee substitution preserving the role succeeds by construction.

Correct interpretation:

> The current model demonstrates one coherent role-relative institutional architecture.

It does not prove that real institutions generally track roles more strongly than persons.

The next probe must compare independent rivals:

- `M_role`: authorization attaches to compatible role occupancy.
- `M_person`: authorization attaches to a specific indexed carrier.

Use holdouts to discriminate.

### Factorial orthogonality

The current nominal `2x2x2x2` is not fully orthogonal operationally.

When relation is false, the authorization record is absent, which censors source and activation downstream. When source validation fails, the function returns before activation is evaluated.

Thus the current model is a serial gate:

`R -> Src -> A -> output`

with identity omitted from the decision path.

Do not claim mixed terms or independent factorial evidence from it.

The recorded run remains valid as a pipeline trace and finite consistency witness.

Build a revised probe later in which all four latent variables exist independently in every cell and are recorded even when an earlier gate would deny the action.

## Local-discontinuity thesis

Keep the core slogan:

> Apparent local discontinuity can be the projection of distributed causal structure onto an insufficient local frame.

But keep C-008 Conjectured.

The current badge-door model does not test observer-level local discontinuity.

The required discriminator remains:

1. local-only information;
2. correct distributed support;
3. equal-volume irrelevant support;
4. plausible false support.

Primary outcomes:

- prediction accuracy;
- intervention selection;
- confidence calibration.

Secondary outcomes:

- arbitrariness attribution;
- personality attribution;
- institutional attribution.

If correct support merely makes the story feel coherent but does not improve prediction/intervention performance, treat the thesis as narrative rather than explanatory.

## Situational-field correction

The v0.1 formalism included `S_t` inside the realization-map arguments while also trying to vary `S_t` independently of `I_t`.

Do not preserve that seam.

Use:

`X_t = (P_t, R_t, D_t)`

`I_t^T = q_T(X_t)`

and

`Y = A_T(I_t^T, S_t, U_t)`.

Where an external condition becomes durably encoded into profiles/relations/artifacts, that encoding belongs in the later `X_t`; the current external condition still remains analytically distinct.

## Persistence and carrier substitution

Preserve the key consequence:

`X_t != X_{t+Δ}`

can coexist with

`I_t^T = I_{t+Δ}^T`.

This is the clean formal version of institution persistence under turnover.

A person/artifact substitution preserves the institutional macrostate only when it preserves the declared response signature.

Do not call substitutions institutional invariances before specifying the task/intervention family.

## Approximate equivalence warning

Exact quotient equivalence is clean.

Approximate equivalence under tolerance may fail transitivity.

Do NOT casually write `[X]_{~_{T,epsilon}}` unless the chosen relation is actually an equivalence relation.

If empirical tolerance breaks transitivity, use a pseudometric, clustering, or tolerance relation instead.

## Cultural-I boundary

Retain the current mainline boundary:

- cultural-I: distributed social/cultural encoding pattern;
- institutional micro-realization: may include cultural-I-like encoding plus typed roles, provenance, artifacts, records, access, communication, and operational paths;
- institutional macrostate: task-relative quotient of micro-realizations under response equivalence.

Do not widen cultural-I into the whole institution unless an independent argument earns it.

## Identity versus operational participation

Do not use rho as an operational-centrality metric.

If operational participation is needed, define a new APPLICATION-LEVEL task-relative diagnostic only after declaring the intervention:

for example, outcome change under ablation/replacement of agent `i` or relations incident to `i`.

Keep this analytically separate from rho.

Do not introduce it as a new foundation coordinate.

## Sheaf gate

Keep sheaf language DARK / candidate.

Do not promote to literal sheaf mathematics unless all are explicit:

- base/site;
- cover;
- sections;
- restriction maps;
- compatibility;
- gluing;
- nontrivial obstruction;
- observable consequence.

If typed graphs plus interface maps suffice, delete the sheaf language beyond a historical note.

## Prior-art debt

C-025 remains UNVERIFIED.

Before novelty claims, build the primary-source comparison matrix against genuinely independent source families:

- social ontology/institutional facts;
- collective intentionality/shared agency;
- distributed cognition;
- situated cognition;
- sociotechnical/actor-network approaches;
- role theory;
- organizational sociology;
- institutional economics;
- distributed systems;
- multi-agent systems;
- observability/control;
- local-to-global/sheaf formalisms.

Normalize provenance and do not count multiple secondary retellings as independent support.

The likely TLICA-specific residual to test is the JOINT preservation of:

- identity placement separate from causal participation;
- source-path status;
- formation/activation;
- semantic interoperability;
- indexed attribution;
- local perspectival observability.

If simpler rival frameworks carry all of this equally well, present TLICA as a translation bridge rather than claiming novelty.

## Mainline integration workflow

1. Establish repo, branch, HEAD, remote, worktree status, current foundation version.
2. Run current `make validate` before changes.
3. Read the entire current mainline research package:
   - `README.md`
   - `MANUSCRIPT_SEED.md`
   - `CLAIM_LEDGER.md`
   - `RECONCILIATION.md`
   - `PROBE_AND_PRIOR_ART_PLAN.md`
   - badge-door code/results/tests
   - wiki page and glossary pins.
4. Read the new `MANUSCRIPT_DRAFT_V0_2_0.md` completely.
5. Reconcile every v0.2 concept against current main before editing.
6. Land the revised manuscript into mainline house style. Prefer one canonical manuscript rather than maintaining contradictory v0.1/v0.2 theories indefinitely; retain old seed only as provenance if repository convention supports it.
7. Update claim ledger statuses exactly as justified above.
8. Correct README/wiki language that currently makes the badge-door demonstration sound more evidential than its construction warrants.
9. Keep Foundation v5.5.0 untouched unless a completely separate audit proves a foundation change is necessary. Default: NO foundation change.
10. Do not register a polished application-paper version unless the repository's current promotion criteria are genuinely met. It is acceptable to land this as a first-draft application manuscript/research-tier paper while keeping external empirical and novelty claims UNVERIFIED.
11. Update glossary/math-term pins if terminology changes.
12. Run validation/tests and preserve raw outputs.
13. Commit with a message that clearly distinguishes formal-model disclosure from empirical corroboration.

## Next computational work after integration

Do not spend the next session writing more ontology prose.

Priority order:

1. implement the response-signature quotient toy with `X1 != X2`, `X1 ~_T X2`, and `X3` outside the class;
2. rebuild the four-factor probe without early-return censoring;
3. build role-relative vs person-relative rival models and holdouts;
4. run or prepare the local-observer correct/irrelevant/false support experiment;
5. recover one bounded codified-vs-lived workflow;
6. populate primary-source rival tomography;
7. attempt a genuine local-to-global obstruction before promoting sheaf language.

## Acceptance criteria

Before calling v0.2 internalized:

- [ ] `I^T` is consistently a quotient macrostate, not a renamed tuple.
- [ ] `S_t` is external to the macrostate definition.
- [ ] response factorization proposition is stated with its declared formal boundary.
- [ ] approximate equivalence does not silently assume transitivity.
- [ ] badge-door rho result is labeled construction-level, not empirical evidence.
- [ ] badge-door role substitution is labeled role-relative-by-construction.
- [ ] old nominal factorial is not described as independent mixed-term evidence.
- [ ] C-008 remains Conjectured.
- [ ] C-025 remains UNVERIFIED.
- [ ] cultural-I boundary remains explicit.
- [ ] no group-mind reification appears anywhere.
- [ ] no new foundation coordinate is introduced.
- [ ] sheaf language remains gated.
- [ ] repository validation passes.

## Final principle

The object worth preserving is not the notation `I_t`.

The object worth preserving is the weakest structure that makes this statement true and testable:

> Distinct distributed physical/social realizations can count as the same institution for a declared task when they preserve the same intervention-response geometry; a local observer may still experience the resulting activation as abrupt when the support for that geometry lies outside the local frame.

If the quotient formalism helps state, test, and transport that claim, keep it.

If a simpler object does the same job after the probes, delete the quotient notation and keep the phenomenon.
