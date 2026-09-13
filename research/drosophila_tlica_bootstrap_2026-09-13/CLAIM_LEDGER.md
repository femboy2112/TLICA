# Claim ledger — Embodied Drosophila × TLICA

Status vocabulary follows the repository's research discipline: **Disclosed**, **Corroborated**, **Observed**, **Conjectured**, **UNVERIFIED**, **Dark**, **Refuted**.

| ID | Claim | Status | Current warrant | Verdict-changing probe |
|---|---|---|---|---|
| C01 | The public FlyWire adult-brain resource contains a near-complete whole adult Drosophila brain connectome suitable for graph-level simulation. | Corroborated | FlyWire / Nature 2024 connectome publications and public data ecosystem. | Reproduce a known graph statistic from the pinned data release and compare with published counts. |
| C02 | Shiu et al.'s LIF model runs whole-brain Drosophila connectivity and predicts selected sensorimotor responses above simple baselines. | Corroborated | Peer-reviewed Nature 2024 paper + public reference implementation. | Reproduce one published activation/silencing result using the reference backend. |
| C03 | `eonsystemspbc/fly-brain` provides a usable whole-brain LIF engine and multiple accelerated backends. | Observed | Public repository and README inspected at pinned commit. | Clone pinned commit; execute a Brian2 reference run and one parity comparison locally. |
| C04 | FlyGym / NeuroMechFly v2 provides a physics-simulated adult fly body with sensory interfaces and hierarchical controller hooks. | Corroborated | NeuroMechFly v2 documentation and peer-reviewed Nature Methods paper. | Instantiate pinned FlyGym and run an official example unmodified. |
| C05 | Eon Systems has demonstrated a closed-loop coupling between a FlyWire-derived brain model and a NeuroMechFly body. | Observed | Eon's technical write-up and public announcement. The novel embodied integration is not treated here as independently validated. | Reproduce the closed loop from public components, or obtain an auditable release of the glue and replay it. |
| C06 | The simulated fly is a complete biological fly or a demonstrated conscious subject. | UNVERIFIED | No suitable probe establishes this, and the model omits substantial biological detail. | Requires a much stronger emulation criterion and biological validation program; no present probe is decisive. |
| C07 | Present sensory coupling can support a calibrated κ/contact proxy without importing identity or truth claims. | Conjectured | Structural fit to TLICA's contact coordinate; no fly-specific calibration yet. | Run null, sensor-off, direct-injection, and matched-amplitude source-swap controls. |
| C08 | A valid φ value can currently be assigned to ordinary whole-brain fly activity. | Refuted for bootstrap | No explicit verification toolkit/pathway has been constructed. The architecture therefore requires `phi_state = undefined`. | Build a rival-discriminating internal pathway and predeclare a probe that tests it. |
| C09 | Recurrent centrality, firing persistence, salience, or behavioral relevance alone measures ρ. | Refuted as an admissible shortcut | These quantities lack a declared self-root and root-relative transport rule. | A candidate ρ must survive root-sensitive perturbations and predict holdout behavior. |
| C10 | A candidate root-relative ρ can be operationalized in an embodied fly model. | UNVERIFIED | Plausible route exists via explicit root declaration + transport + perturbation controls. | Compare root ablation, degree-matched non-root ablation, rewiring, and detached-body replay. |
| C11 | σ/source-map adequacy can be tested independently of κ by provenance-preserving sensory remaps. | Conjectured | Source labels and encoder transforms are controllable in simulation. | Hold drive statistics approximately fixed while swapping left/right, odor source, or visual sectors; test whether source diagnostics detect the attack. |
| C12 | Closed-loop embodiment produces neural/action trajectories distinguishable from exact sensory replay. | UNVERIFIED | This is the first major causal probe. | Record a closed-loop episode, replay exact sensory samples open-loop with matched seed/backend, and compare trajectories after declared causal divergence points. |
| C13 | TLICA's coordinate separation remains useful when translated from human phenomenology into a nonverbal connectome agent. | UNVERIFIED | This is the research program's central translation claim. | Produce at least two clean dissociations (for example matched κ with altered candidate ρ; high κ with damaged σ) that survive controls and holdouts. |
| C14 | Successful coordinate dissociations would prove TLICA as a theory of consciousness. | Refuted | Even successful simulator dissociations would validate only specific operational distinctions in that model. | No simulator-only result is sufficient; claims must remain scoped. |
| C15 | Failure to obtain a fly-level φ or ρ necessarily falsifies the human-level TLICA construct. | Refuted | It may instead show an access-gap or category mismatch between the fly model and the construct. | First establish that the necessary pathway/root structures are actually implemented before treating a null as theory-level refutation. |

## Live obstruction classification

- **Pathway-gap:** φ — no verified pathway for internal truth discrimination has yet been constructed.
- **Probe-gap:** candidate ρ — several roots/transports are possible; no decisive root-selection probe has yet run.
- **Access-gap:** Eon's complete embodied glue and its exact validation harness are not assumed available in the public brain repository.
- **Boundary:** the current model is a connectome-constrained simulation, not a demonstrated biological or conscious duplicate.

## Highest-value next probe

**P1 closed-loop vs exact replay** is first because it is comparatively theory-light, reproducible, and probes whether the body/world causal loop contributes information beyond a prerecorded stimulus sequence. If P1 fails cleanly, the embodiment layer is weaker than the research program needs and the rest should not be built on top of a rhetorical notion of embodiment.