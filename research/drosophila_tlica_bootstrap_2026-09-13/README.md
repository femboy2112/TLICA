# Embodied Drosophila × TLICA bootstrap

**Status:** research-tier bootstrap · 2026-09-13 · foundation untouched

This dossier bootstraps an experimental bridge between TLICA and an embodied whole-brain Drosophila simulation. It does **not** claim that a simulated fly is conscious, that a connectome is a complete mind, or that TLICA has been validated by Drosophila.

The immediate goal is narrower and testable:

> Build a closed-loop fly simulation whose sensory → neural → action transitions are recorded in a TLICA-compatible observational schema, then design interventions that can separate contact, identity-correlation, source-map adequacy, probe availability, coherence, and discrimination instead of collapsing them into one score.

## Chosen upstream stack

The strongest public stack found for this purpose is:

1. **Eon Systems `fly-brain`** — whole-brain leaky-integrate-and-fire simulation over the FlyWire adult Drosophila connectome, with multiple execution backends and Brian2 as the canonical reference implementation.
   - https://github.com/eonsystemspbc/fly-brain
   - pinned bootstrap commit: `a3db62f9436074e485c0278290c2164ed6150808`
2. **FlyGym / NeuroMechFly v2** — MuJoCo-based biomechanical adult fly with vision, olfaction, proprioceptive/mechanosensory access, terrain interaction, and a brain↔VNC-style hierarchical control interface.
   - https://github.com/NeLy-EPFL/flygym
   - pinned bootstrap commit: `38c8ec61034cd59bc5ba0de20688d4a3c0000d60`
3. **FlyWire** — the anatomical connectome source used by the brain model.
   - https://flywire.ai/
4. **Shiu et al. 2024** — peer-reviewed whole-brain LIF model that provides the neural-dynamics reference.
   - https://doi.org/10.1038/s41586-024-07763-9

Eon also reports an embodied closed-loop prototype coupling the connectome model to NeuroMechFly. Their own technical write-up is useful as an engineering reference, but that embodied glue is not treated here as a peer-reviewed validation target:

- https://eon.systems/updates/embodied-brain-emulation

## Why this is a useful TLICA test bed

TLICA currently has rich claims about contact, verification pathways, identity integration, source attribution, probe access, focus, and development. A simulated fly gives us something human introspection does not: complete intervention access to the modeled nervous system, exact event timing, repeatable worlds, lesion controls, state snapshots, and the ability to replay identical sensory streams under different causal structures.

That makes the fly valuable even if the strongest interpretation fails. The experiment can test whether TLICA distinctions survive translation into an explicit dynamical system.

## The key discipline

The bootstrap intentionally refuses several tempting identifications:

- **κ/contact** may be operationalized from calibrated present sensory coupling.
- **φ/truth-indistinguishability** is **undefined by default**. A spiking network receiving a signal does not thereby possess a verification pathway. A φ value may only be emitted after an explicit toolkit/pathway model exists and a discriminating probe has been defined.
- **ρ/identity-correlation** is **undefined by default** until an operational self-root and transport rule are declared. Recurrence, salience, persistence, or firing rate are not automatically ρ.
- **σ/source-map adequacy** is recorded as structured provenance and attribution diagnostics, not compressed into a scalar confidence score.
- **μ/probe availability** is represented explicitly as the set of interventions/discriminators currently accessible.
- coherence, independence, and discrimination remain separate diagnostics.

This is the most important design choice in the dossier.

## Target loop

```text
MuJoCo world / NeuroMechFly body
            │
            ▼
  calibrated sensory encoders
            │
            ▼
 FlyWire whole-brain LIF engine
            │
            ▼
 descending-output decoder
            │
            ▼
 body controller / actuation
            │
            └────────────── feedback ──────────────┐
                                                   │
             TLICA recorder observes every edge ◄──┘
```

The TLICA recorder is initially **observational**. It does not change neural dynamics. Intervention modules are added only after the baseline reproduces upstream behavior.

## Bootstrap locally

From the repository root on this branch:

```bash
bash research/drosophila_tlica_bootstrap_2026-09-13/bootstrap.sh
python -m unittest discover \
  -s research/drosophila_tlica_bootstrap_2026-09-13/prototype/tests \
  -v
python research/drosophila_tlica_bootstrap_2026-09-13/prototype/example_synthetic.py
```

`bootstrap.sh` only fetches pinned upstream source trees. It deliberately does **not** auto-install CUDA, MuJoCo, conda environments, or GPU frameworks.

## First five experiments

1. **Closed-loop vs replay** — record a real embodied run, then replay the exact sensory stream open-loop. If downstream dynamics diverge only when body/world causality is present, we have a clean coupling probe rather than merely a stimulus-response trace.
2. **κ dissociation** — match instantaneous sensory drive while varying persistence/history. This tests whether present contact can be held fixed while longer-lived network effects differ.
3. **candidate-ρ formation** — only after a self-root is declared, repeatedly pair a neutral cue with body-relevant state and test whether transport from the declared root changes under matched current κ. This remains a candidate operationalization until independent controls survive.
4. **σ attack** — preserve stimulus statistics while deliberately misrouting provenance (for example, swap left/right or odor/source labels). The aim is to degrade the source map without simply reducing signal strength.
5. **φ gate** — attempt to construct a genuine discriminator that lets the agent distinguish two rival world/source hypotheses. Until that circuit and probe exist, φ stays undefined.

See `ARCHITECTURE.md` and `CLAIM_LEDGER.md` for the formal scaffold and epistemic boundaries.

## Acceptance criterion for the bootstrap

The bootstrap is successful when a local session can:

- reproduce an upstream brain-only reference run;
- instantiate a FlyGym/NeuroMechFly body;
- run a deterministic synthetic TLICA recorder test;
- define a typed brain↔body adapter without modifying the frozen TLICA foundation;
- preserve raw neural/body telemetry and provenance;
- run at least one intervention whose competing hypotheses predict different outcomes.

Anything stronger is future work.