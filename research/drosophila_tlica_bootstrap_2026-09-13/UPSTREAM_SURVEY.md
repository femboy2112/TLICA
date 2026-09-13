# Upstream survey: what the "full simulated fly" actually consists of

## Short answer

There is no single canonical program that is simultaneously the complete anatomical dataset, the validated neural dynamics, and the fully embodied body simulator.

The thing most closely matching the viral description is **Eon Systems' embodied Drosophila demonstration**, assembled from three major substrates:

1. a FlyWire whole-brain connectome;
2. a Shiu-et-al.-style whole-brain LIF model;
3. NeuroMechFly / FlyGym on MuJoCo for the body and environment.

Eon's public brain engine is:

- https://github.com/eonsystemspbc/fly-brain

Their technical description of the embodied loop is:

- https://eon.systems/updates/embodied-brain-emulation

That is the best baseline because it gives us a published neural model, an actively engineered simulation engine, and a published body simulator.

## Important 2026 development: MaleCNS v1.0

As of this bootstrap, an even better **anatomical substrate** now exists: the HHMI Janelia / Cambridge / Google **MaleCNS v1.0** dataset.

Official project page:

- https://male-cns.janelia.org/

Official download page:

- https://male-cns.janelia.org/download/

Official Janelia overview:

- https://www.janelia.org/project-team/flyem/male-cns-connectome

The critical difference is that MaleCNS covers the **central brain + optic lobes + ventral nerve cord with an intact neck connective**. That attacks one of the largest anatomical gaps in the earlier embodied FlyWire-brain demonstrations: the body-side motor circuitry is no longer absent from the connectome substrate.

MaleCNS v1.0 is therefore the preferred **Phase-II target** for a genuinely CNS-wide embodied TLICA experiment.

### Why it is not the Phase-I baseline

MaleCNS is primarily a released anatomical/connectivity dataset, not a peer-reviewed, calibrated whole-CNS dynamical model equivalent to Shiu et al.'s whole-brain LIF implementation.

That distinction matters. Wiring is not physiology.

The clean progression is therefore:

```text
Phase I
FlyWire female brain + Shiu LIF reference + Eon engine + FlyGym body
        │
        ├─ establish reproducible timing/provenance/replay
        └─ establish TLICA instrumentation without inventing physiology

Phase II
MaleCNS v1.0 brain + VNC
        │
        ├─ build/import full-CNS graph
        ├─ transport or re-calibrate neural dynamics
        ├─ replace hand-authored brain→body shortcuts where anatomy permits
        └─ rerun the same intervention suite
```

If a claimed TLICA effect exists only in the older brain-only architecture and disappears when the motor/VNC route is made more anatomically faithful, that is evidence against the original mapping—not something to smooth over.

## Access routes for MaleCNS

Officially supported routes include:

- bulk connectivity/annotation/skeleton downloads;
- neuPrint interactive querying;
- `neuprint-python` for programmatic queries;
- `natverse/malecns` for R-based access;
- Neuroglancer/Clio/Cell Type Explorer for inspection.

The dataset is released under CC-BY according to the project page.

## Experimental third-party MaleCNS simulators

Several 2026 projects already run engineered dynamics over the MaleCNS graph. These are useful as implementation leads, **not** automatically as biological ground truth.

One unusually useful example is:

- https://github.com/nftechie/doomfly

Its own documentation explicitly distinguishes the retained MaleCNS wiring from the approximate dynamics and records failed validation gates. That makes it a potentially useful source for:

- data import;
- graph packing;
- neuron-ID preservation;
- large recurrent-state execution;
- mutation/conditioning experiment infrastructure.

But its dynamics and game mappings should remain independent provenance from the Shiu/Eon reference path.

This separation is useful for TLICA-style triangulation: two engines can share anatomy while differing in dynamics and embodiment, giving us a real implementation axis rather than fake "independent confirmation" from the same codebase.

## Recommended research topology

Do not fork a single simulator and call the result evidence.

Use three constraint surfaces:

### Route A — reference brain dynamics

`philshiu/Drosophila_brain_model` / Eon Brian2 implementation

Purpose: canonical LIF behavior and reproducibility.

### Route B — embodiment

`NeLy-EPFL/flygym`

Purpose: physics, sensors, body state, environmental causality.

### Route C — new CNS anatomy

MaleCNS v1.0 via official downloads/neuPrint

Purpose: full brain↔VNC transport and a second anatomical basis.

The TLICA recorder sits outside all three. It should be able to ingest any route without changing coordinate definitions.

## Decision

**Bootstrap now against Eon + FlyGym. Design every adapter so MaleCNS can replace the FlyWire-brain substrate later without rewriting the TLICA layer.**

That preserves a strong reference implementation today while keeping the architecture pointed at the substantially better full-CNS substrate that arrived in 2026.