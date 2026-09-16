# Local Claude handoff — internalize the research-method loop into `main`

You are continuing work on:

`femboy2112/TLICA.git`

A non-main research branch has been prepared:

`phenomenology-analogy-model-probe-loop-2026-09-15`

It was branched from main commit:

`33d449424dd909bab5dfe8e80f302df733bd2770`

The new dossier is:

`research/phenomenology_analogy_model_probe_loop_2026-09-15/`

Files:

- `README.md` — full methodology reconstruction
- `AUTHOR_SEED.md` — exact author-originating six-line compression and provenance firewall
- `CLAIM_LEDGER.md` — claim-by-claim epistemic statuses and truth debts
- `RECONCILIATION.md` — audit against current main, integration routes, acceptance criteria
- `LOCAL_CLAUDE_HANDOFF.md` — this file

## Mission

Internalize the branch into `main` conservatively and durably.

Do **not** merely merge because the branch exists. First inspect current `main`, inspect the branch diff, and reconcile any changes that landed after the branch point.

The central author insight is:

> Find analogy that fits phenomena phenomenologically.  
> Map the analogy to math.  
> Now you have a model.  
> Drive the math with inputs not yet phenomenologically experienced and see what drops out.  
> Test those against reality.  
> Update the model based on results.

The branch formalizes that into:

`phenomenology -> analogy -> bridge contract -> candidate shared structure -> formal model -> out-of-fit drive -> risky prediction -> discriminating probe -> residual localization -> revision`

The key epistemic firewall is:

> **Analogy proposes candidate structure. Mathematics propagates consequences. Reality supplies warrant.**

## Required first step: inspect, don't assume

1. `git status`
2. identify current branch/worktree
3. `git fetch`
4. inspect current `main` HEAD and compare it with base `33d449424dd909bab5dfe8e80f302df733bd2770`
5. inspect `git diff main...phenomenology-analogy-model-probe-loop-2026-09-15`
6. read all dossier files
7. read current:
   - root `README.md`
   - `research/README.md`
   - `docs/README.md`
   - `CHANGELOG.md`
   - `applications/caves_lagrange_points_v0_1_0.md`
   - `research/dynamical_substrate_axioms_2026-09-08.md`
   - `research/substrate_round1_reachability_momentum_2026-09-08.md`
   - `research/distributed_institutional_realization_2026-09-15/README.md`
   - `research/developmental_substrate_nonstationarity_2026-09-15/README.md`

Do not overwrite newer mainline work.

## Integration target

Treat this as a **research-methodology synthesis**, not a frozen-foundation mutation.

Preferred integration route if current main still matches the reconciliation:

### 1. Land the dossier under `research/`

Preserve the full dossier and author seed.

### 2. Update `research/README.md`

Add a concise section such as:

`## Phenomenology–analogy–model–probe methodology (2026-09-15)`

State:

- author-reported meta turned into an auditable research protocol;
- analogy is hypothesis generation, not evidence;
- bridge contract declares what maps and what explicitly does not;
- construction evidence is separated from holdout evidence;
- the formal model must be driven into new regimes;
- probes need pass/fail/ambiguous outcomes;
- residuals localize failure and feed revision;
- general superiority of the workflow remains UNVERIFIED;
- foundation untouched.

### 3. Add a public methodology page if it fits current docs architecture

Recommended path:

`docs/research-method.md`

This should be a readable condensation, not a duplicate dump of the research dossier.

It should include:

- the loop diagram;
- the bridge contract;
- analogy-vs-mechanism firewall;
- fit-vs-holdout rule;
- out-of-fit drive;
- probe criteria;
- revision/failure-localization table;
- warning that internal examples are same-project specimens, not independent corroboration.

Then link it from `docs/README.md` under a methodology/research-practice heading.

### 4. Root README: only a compact pointer

If appropriate, add one short paragraph near the repository-status/research-method discussion. Do not make the root README top-heavy.

Suggested conceptual content:

> The project uses an explicit analogy-to-model research loop: phenomenological structure may suggest a source analogy, but the analogy is only a candidate generator. The transported structure must be declared, formalized, driven outside its motivating cases, and exposed to a discriminating probe before it earns empirical warrant.

Do not claim this is the only valid research method.

### 5. `CHANGELOG.md`

Add a dated entry documenting:

- new research-methodology dossier;
- bridge contract;
- fit/holdout separation;
- out-of-fit model driving;
- probe/revision loop;
- foundation untouched.

## Foundation firewall

Do **not** add:

- a new TLICA coordinate;
- a developmental mode;
- a new prerogative;
- a new foundation-level dynamical law;
- a cognitive mechanism claiming why Leah uses analogies this way;
- a scalar truth score;
- any claim that phenomenological resonance validates mechanism.

The dossier explicitly classifies the deeper cognitive mechanism as **Dark**.

If you discover a genuine reason the method must modify foundation, stop and write a separate argument rather than smuggling it into this integration.

## Load-bearing technical content to preserve

### Bridge contract

`B=(b_O,b_R,b_I,b_D,b_neg)`

It declares:

- source objects -> target objects
- source relations -> target relations
- candidate invariants
- candidate dynamics
- explicit non-transports

Rule: **No declared bridge, no transported claim.**

### Candidate shared structure

Conceptual form:

`A -> Q <- X`

The method seeks a shared reduced structure `Q`, not the identity `A = X`.

### Generic formal model

`M=(S,Theta,F,C,O)`

where `O` is an observation map back to testable quantities.

### Fit provenance

Track all evidence that influenced analogy/model/parameter selection as `D_fit`.

Do not reuse `D_fit` as clean validation.

### Out-of-fit drive

Choose `u*` outside the motivating evidence and derive:

`y_hat* = O(M(u*))`

This is the load-bearing generative hinge.

### Probe

Predeclare:

- pass
- fail
- ambiguous
- controls
- rival predictions where possible

### Residual localization

Possible failure loci:

- analogy selection
- bridge
- formalization
- parameters
- observation map
- probe
- domain boundary
- source/provenance

### Revision

The process must permit stable **REFUTED** outcomes. Never make the loop self-sealing.

## Epistemic-status requirements

Preserve the dossier's claim discipline:

- author seed = **Observed / author-reported**
- formal stage decomposition = **Disclosed at reconstructive boundary**
- analogy != mechanism = **Disclosed**
- repository specimens = **Disclosed by repository inspection**, but **not independent corroboration**
- claim that the loop captures substantial author workflow = **Conjectured**
- claim that the protocol improves research generally = **UNVERIFIED**
- deeper cognitive explanation of analogy productivity = **Dark**

Do not silently upgrade these statuses during prose polishing.

## Internal examples to preserve as examples only

- `applications/caves_lagrange_points_v0_1_0.md`
- `research/dynamical_substrate_axioms_2026-09-08.md`
- `research/substrate_round1_reachability_momentum_2026-09-08.md`
- `research/distributed_institutional_realization_2026-09-15/`
- `research/developmental_substrate_nonstationarity_2026-09-15/`

These show pieces of the method already operating, but all share project provenance.

## Validation

Before committing:

1. inspect all modified markdown rendering/links;
2. grep for accidental claims that the method is foundation-level or empirically validated;
3. grep for status drift (`Corroborated`, `proven`, `validated`, etc.);
4. ensure links are relative and resolve;
5. ensure current foundation version statements still match main;
6. run any repository-local validation/lint scripts that apply to docs;
7. inspect final `git diff --check`;
8. review final diff as an adversarial reader trying to find metaphor-to-mechanism laundering.

## Commit strategy

Prefer a small number of coherent commits, for example:

1. `research: internalize phenomenology-analogy-model-probe methodology`
2. `docs: surface analogy-to-model research method`

Do not rewrite unrelated history.

## Final report back to Leah

Report:

- current main commit used;
- whether the dossier was integrated unchanged or reconciled;
- exact files added/modified;
- whether a public docs page was added;
- whether foundation changed (**expected: no**);
- any status/claim wording you tightened;
- validation run and results;
- final commit SHA(s).

If you find a conflict between newer mainline theory and this branch, preserve newer main, explain the conflict explicitly, and adapt the methodology note rather than forcing the branch version through.
