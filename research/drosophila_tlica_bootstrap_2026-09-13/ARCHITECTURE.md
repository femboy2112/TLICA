# Architecture: Drosophila × TLICA observational bridge

## 0. Boundary

This architecture is an **instrumentation and intervention framework** around an embodied neural simulation. It is not a claim that the simulation instantiates consciousness or a complete biological fly.

The frozen TLICA foundation remains unchanged. Any mapping from simulator state into TLICA language is tagged as one of:

- **direct observation** — raw simulator quantity;
- **calibrated proxy** — declared transform with controls;
- **candidate operationalization** — theory-bearing mapping requiring discriminating probes;
- **undefined** — no constructible mapping exists yet.

## 1. Four-layer system

### Layer A — environment/body

Source: FlyGym / NeuroMechFly v2 on MuJoCo.

Minimum telemetry:

- simulation time;
- body pose and joint state;
- contact forces;
- visual receptor samples;
- olfactory receptor samples;
- optional temperature / mechanosensory channels if implemented;
- controller targets actually applied to the body.

### Layer B — sensory transport

A versioned encoder maps body/environment observables into neural drive.

Every encoder invocation MUST record:

- raw source channel;
- source coordinates / body side / receptor identity where available;
- transform name and version;
- calibration parameters;
- output neuron IDs or cell classes;
- output rates/current/spikes;
- random seed if stochastic encoding is used.

No sensory encoder may silently erase provenance.

### Layer C — whole-brain dynamics

Primary upstream: `eonsystemspbc/fly-brain`.

Reference backend: Brian2 implementation of the Shiu et al. LIF model. Other backends are acceptable only after parity against the reference is recorded for the regime in use.

Minimum telemetry:

- FlyWire neuron ID;
- simulation-local neuron index;
- spike time;
- membrane state when available without perturbing timing materially;
- input drive provenance;
- lesion/silencing mask;
- backend and commit;
- random seed;
- model timestep.

### Layer D — action transport

A versioned decoder maps selected descending-neuron activity into body commands.

Every decoder invocation MUST record:

- source neuron IDs / classes;
- temporal integration window;
- filter or threshold parameters;
- resulting low-dimensional motor command;
- final joint/controller targets sent to MuJoCo;
- transform version.

The decoder is a model assumption, not a discovered biological identity.

## 2. TLICA event model

The recorder observes boundaries between the four layers and emits events.

```text
TLICAEvent
├─ run identity
│  ├─ run_id
│  ├─ parent_run_id / replay_of
│  ├─ upstream commits
│  └─ configuration hash
├─ clock
│  ├─ world_time_s
│  ├─ brain_time_s
│  └─ step_index
├─ event
│  ├─ kind
│  ├─ raw observables
│  └─ transform chain
├─ TLICA coordinates / diagnostics
│  ├─ kappa        : optional calibrated proxy
│  ├─ phi          : undefined | candidate value with explicit pathway basis
│  ├─ rho          : undefined | candidate value with explicit root/transport basis
│  ├─ sigma        : structured source-map record
│  ├─ mu           : available probe-set record
│  ├─ coherence    : optional diagnostic
│  ├─ independence : optional diagnostic
│  └─ discrimination: optional diagnostic
└─ epistemic record
   ├─ status
   ├─ assumptions
   ├─ controls
   └─ provenance
```

No aggregate `truth_score`, `selfhood_score`, or `consciousness_score` is permitted in the bootstrap.

## 3. Coordinate discipline

### κ — contact

Candidate measurable quantity: present causal coupling between an external/body source and the modeled agent at time `t`.

Initial proxy family:

```text
kappa_t(source) = calibrated normalized magnitude of current transduced drive
```

This is only a **contact proxy**. It must not absorb persistence, behavioral relevance, learning, or identity integration.

Controls:

- zero-input null;
- matched-amplitude shuffled source;
- sensor disabled while environment event remains;
- direct neural injection with no external source.

### φ — truth-indistinguishability

**Default state: UNDEFINED.**

A signal being strong, recurrent, behaviorally effective, or anatomically central is not a verification pathway.

A φ operationalization becomes admissible only after all of the following are declared:

1. a finite rival set or hypothesis family;
2. a constructible internal or experiment-relative pathway that can discriminate those rivals;
3. the tools available to that pathway;
4. a falsifiable probe with pass/fail/ambiguous outcomes;
5. a transport from probe outcome into the proposed φ quantity.

Until then, serialize `phi_state = "undefined"`.

### ρ — identity-correlation

**Default state: UNDEFINED.**

The frozen theory defines ρ in terms of integration/flow through a self-rooted historical network. The fly simulator does not hand us a validated self-root.

A candidate ρ experiment therefore requires:

1. a declared root set `R_self`;
2. a declared network/state over which transport occurs;
3. a declared transport or flow functional;
4. perturbation controls that distinguish recurrence from root-relative integration;
5. a holdout test showing that the measure predicts something not fitted into its construction.

Possible root hypotheses may include persistent body-state channels or recurrent body↔brain loops, but none is privileged at bootstrap time.

### σ — source-map adequacy

Represent σ as a **source graph**, not one number.

Minimum fields:

- originating world/body variable;
- sensor/receptor;
- encoder transform chain;
- target neural population;
- decoder/action chain if applicable;
- known ambiguity set;
- calibration status;
- ablation/replay history.

Derived scalar summaries may be added later for specific probes, but raw/path-adjusted source maps must remain available.

### μ — probe availability

Represent μ as the currently accessible probe family:

- lesion sets;
- activation sets;
- sensory substitutions;
- replay capability;
- body/environment perturbations;
- source-label permutations;
- backend swaps;
- seed replication;
- open-loop/closed-loop switch.

A claim cannot be upgraded merely because many probes exist; they must actually discriminate the live rivals.

## 4. First discriminating probes

### P1 — closed-loop causal necessity

**Rivals**

- H1: behaviorally relevant state depends materially on embodied feedback.
- H0: the same sensory time series is sufficient; closed-loop causality adds nothing in the tested regime.

**Protocol**

1. Run closed-loop episode E and record every sensory sample.
2. Re-run brain dynamics open-loop using the exact recorded sensory stream and seed.
3. Compare neural trajectories and action-decoder outputs.
4. Mutation control: phase-shift or source-swap one sensory channel while preserving marginal statistics.

**Outcomes**

- PASS H1: divergence exceeds predeclared tolerance only after causal feedback paths would differ, and survives seed/backend checks.
- PASS H0: trajectories remain equivalent within tolerance.
- AMBIGUOUS: divergence is explained by nondeterminism, backend mismatch, or timing skew.

### P2 — contact/history dissociation

Match present input amplitude at test time while varying exposure history.

If a later candidate ρ measure changes while κ is matched, that is evidence the two proposed quantities are not merely aliases. It is not yet evidence that the changed quantity is genuinely ρ.

### P3 — source-map attack

Swap provenance while holding low-level drive statistics approximately fixed.

Examples:

- left/right receptor swap;
- odor-source labels permuted;
- visual sector remapped;
- body-side encoder wiring reversed.

The goal is to construct high-κ / damaged-σ cases.

### P4 — root sensitivity

For each candidate `R_self`, recompute the proposed ρ measure after:

- root ablation;
- matched non-root ablation;
- degree-matched graph rewiring;
- replay with the body detached.

A candidate ρ that is insensitive to its declared root is refuted as root-relative identity transport.

### P5 — pathway gate for φ

Construct a task with two rival latent causes that produce overlapping immediate sensory signals but differ under an available probe action.

Only if the modeled agent contains a pathway that can select/execute/consume such a probe does φ become a live construct in that task.

## 5. Milestones

### M0 — provenance lock

- clone pinned upstreams;
- record commits and licenses;
- reproduce one brain-only run;
- run upstream parity test where feasible.

### M1 — observational bridge

- no changes to brain dynamics;
- JSONL event recorder around sensory input, spikes, decoder, body action;
- deterministic synthetic tests;
- raw telemetry preserved.

### M2 — one-way embodiment

- body sensors → brain encoder;
- brain output logged but not yet controlling body;
- validate timing and provenance.

### M3 — closed loop

- descending output → body controller;
- body changes next sensory state;
- P1 closed-loop vs replay probe passes or returns a calibrated null.

### M4 — TLICA dissociation suite

- κ/history probe;
- σ attack;
- root-sensitive candidate ρ probe;
- φ remains undefined unless a real discriminator is built.

### M5 — truth-debt payment

- backend holdout;
- seed holdout;
- environment holdout;
- lesion/mutation controls;
- independent implementation of at least one key metric.

## 6. Failure conditions

The research direction should be revised, not rhetorically rescued, if any of these occur:

- proposed κ is dominated by history rather than present coupling;
- proposed ρ survives removal/change of its declared self-root unchanged;
- proposed φ can be computed without any declared verification pathway;
- σ can be destroyed without the metric noticing;
- results disappear under a reference backend or exact replay;
- body behavior depends mainly on handcrafted decoder policy rather than measured brain outputs;
- fitted examples are the only examples on which a TLICA mapping works.

Those are useful failures: each one tells us which translation was illegitimate.