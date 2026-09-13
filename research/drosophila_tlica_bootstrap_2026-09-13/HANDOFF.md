# Local implementation handoff

## Mission

Turn this dossier into a reproducible closed-loop experimental system that couples:

- pinned `eonsystemspbc/fly-brain` whole-brain LIF dynamics;
- pinned `NeLy-EPFL/flygym` / NeuroMechFly v2 body/environment;
- the dependency-free TLICA event/provenance recorder in `prototype/`.

Do **not** alter the frozen TLICA foundation. Do **not** label the simulated fly conscious or claim that a scalar neural statistic is κ, φ, ρ, σ, or μ without the declared transport/controls in `ARCHITECTURE.md`.

## Starting state

Branch:

```text
research/drosophila-tlica-bootstrap-2026-09-13
```

Pinned upstreams:

```text
eonsystemspbc/fly-brain  a3db62f9436074e485c0278290c2164ed6150808
NeLy-EPFL/flygym         38c8ec61034cd59bc5ba0de20688d4a3c0000d60
```

Fetch them with:

```bash
bash research/drosophila_tlica_bootstrap_2026-09-13/bootstrap.sh
```

## Phase 1 — reproduce before integrating

### 1A. Brain baseline

Inside the pinned Eon tree:

1. follow its README/environment instructions exactly;
2. run the smallest practical Brian2 CPU reference simulation;
3. preserve stdout/stderr, exact command, environment export, seed, wall clock, and resulting spike artifact;
4. run one available ground-truth/parity comparison on that artifact;
5. record the result in a new `runs/BASELINE_BRAIN.md` in this dossier.

**Acceptance:** a reference run completes and produces non-empty spike output with exact commit/config provenance.

### 1B. Body baseline

Inside pinned FlyGym:

1. follow the current 2.x installation path;
2. run one official unmodified NeuroMechFly example or interactive example headlessly if possible;
3. capture body-state telemetry for a short deterministic episode;
4. record command, seed, commit, MuJoCo/FlyGym versions, and result.

**Acceptance:** a fly body steps under MuJoCo without any custom brain adapter.

### 1C. TLICA schema baseline

From the TLICA repository root:

```bash
python -m unittest discover \
  -s research/drosophila_tlica_bootstrap_2026-09-13/prototype/tests \
  -v
python research/drosophila_tlica_bootstrap_2026-09-13/prototype/example_synthetic.py
```

**Acceptance:** all tests pass; synthetic event emits defined κ proxy while φ and ρ remain undefined.

## Phase 2 — build typed adapter boundaries

Create a local package under this dossier, for example:

```text
adapter/
├─ sensory.py
├─ brain.py
├─ motor.py
├─ clock.py
├─ run_manifest.py
└─ tests/
```

### Sensory adapter contract

Input:

- timestamped FlyGym sensor packet;
- explicit receptor/source IDs;
- calibration config;
- RNG handle/seed.

Output:

- target FlyWire IDs/cell types;
- neural drive representation required by the selected Eon backend;
- complete transform/provenance record.

No source identity may be inferred from amplitude alone.

### Brain adapter contract

Input:

- neural drive packet;
- lesion/silence mask;
- timestep span.

Output:

- spike events keyed by FlyWire ID;
- backend timing;
- state snapshot needed by motor decoder;
- exact backend/config provenance.

The first implementation SHOULD use the Brian2 reference backend even if slow.

### Motor adapter contract

Input:

- selected descending-neuron spike streams;
- declared temporal filter/integration window.

Output:

- low-dimensional motor intent;
- concrete FlyGym controller inputs;
- transform/provenance record.

Do not hide hand-authored policy inside this adapter. Every mapping must be visible and versioned.

### Clock contract

The embodied prototype must explicitly model:

- neural timestep;
- body timestep;
- coupling cadence;
- interpolation/hold semantics between cadences.

Eon's technical report used a 15 ms synchronization cadence; treat that as an engineering reference, not as a privileged biological constant. Test at least one smaller cadence if computationally feasible.

## Phase 3 — wire recorder passively

Before TLICA-driven interventions, wrap the loop so each boundary emits `TLICAEvent` records.

Required raw artifacts per run:

```text
runs/<run_id>/
├─ manifest.json
├─ events.jsonl
├─ sensory_raw.*
├─ spikes.*
├─ motor_commands.*
├─ body_state.*
├─ stdout.log
└─ checksums.sha256
```

The manifest must contain upstream commits, dependency versions, seeds, configuration hash, timestep/cadence, lesion masks, and replay lineage.

## Phase 4 — run P1 before richer TLICA claims

Implement **closed-loop vs exact replay** from `ARCHITECTURE.md`.

### Predeclare

- neural trajectory distance metric;
- action-output distance metric;
- tolerance for deterministic/reference parity;
- first step at which closed-loop and replay worlds are causally allowed to diverge;
- PASS / FAIL / AMBIGUOUS criteria.

### Controls

- identical-seed exact replay;
- different-seed null for stochastic sensitivity;
- phase-shifted sensory mutation;
- at least one backend/reference check if practical.

Do not proceed to a candidate ρ result until timing/replay artifacts are understood.

## Phase 5 — only then attempt TLICA dissociations

Priority order:

1. κ/contact calibration and κ/history dissociation;
2. σ/source-map attack;
3. candidate self-root enumeration;
4. root-sensitive candidate ρ;
5. φ only if an actual rival-discriminating pathway is constructible.

## Required claim hygiene

Every experiment note must answer:

- What exactly was observed?
- Which mapping is direct vs proxy vs candidate?
- What ordinary implementation failure could explain the result?
- What is the strongest live rival?
- What probe would distinguish it?
- What data are raw, transformed, or fitted?
- Which examples were used to design the metric, and which were holdouts?

## Stop conditions

Stop and classify the obstruction instead of improvising if:

- the pinned upstream no longer reproduces its reference output;
- FlyGym API/version mismatch blocks the body baseline;
- FlyWire IDs cannot be transported unambiguously between source releases;
- timing skew prevents exact replay;
- motor behavior is dominated by handcrafted controller rules;
- a candidate TLICA coordinate cannot be defined without collapsing two diagnostics.

Label the obstruction as pathway-gap, probe-gap, access-gap, or demonstrated boundary and update `CLAIM_LEDGER.md`.

## Deliverable for the first local session

A good first session ends with **boring evidence**:

- both upstreams fetched at exact pins;
- one brain baseline;
- one body baseline;
- prototype unit tests passing;
- a concrete adapter interface skeleton;
- no consciousness claim;
- no invented φ or ρ.

That is the launchpad. The interesting work begins when exact replay and interventions exist.