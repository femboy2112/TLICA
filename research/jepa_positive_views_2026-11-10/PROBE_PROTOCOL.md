# Probe protocol: positive-view geometry, ambient association, and active toolkit bridges

**Date:** 2026-11-10  
**Status:** Prospective protocol, **UNRUN / UNVERIFIED**. All expected effects below are predictions or control requirements, not results. Companion: [research thesis](README.md), [claim ledger](CLAIM_LEDGER.md).

## 1. What would discriminate the models?

**Question:** At fixed model capacity and exposure/query budget, does matching world-grounded positive views improve later *usable discrimination*, and does focus-directed selection of a valid overlap bridge add benefit beyond passive exposure or extra samples alone?

Live rivals:

- **R0 / frequency-only:** ambient sample counts, reinforcement, and ordinary memorization explain gains; view geometry and bridge topology add no independent prediction.
- **R1 / attention-only:** focus improves effective sample use, regardless of whether pairs represent a true world relation.
- **R2 / representation-only:** valid positive views improve embeddings but do not create an accessible new inference tool.
- **R3 / bridge-only:** a valid labeled bridge solves the cross-component ambiguity; good-view JEPA alignment adds nothing beyond direct supervision.
- **R4 / joint bridge candidate:** ambient pattern acquisition makes local proto-paths available; valid views and targeted tested bridges together improve cross-component generalization beyond the controls, with measurable intermediate alignment and later tool access.

The first experiments adjudicate these finite learner models, not consciousness or real human osmotic learning.

## 2. Synthetic data: two distinguishable structures

Use a seeded finite task from the existing [toolkit-closure dossier](../grokking_as_toolkit_closure_2026-08-29.md):

$$
y_{ab}=u(a)+v(b)\pmod 5,
\qquad a\in A,\quad b\in B.
$$

Start with an observation graph on $A\sqcup B$ having **two connected components** and independently hidden modular offsets. Under a uniform prior on the residual relative gauge, labels of unseen cross-component pairs cannot be identified from disconnected training labels alone. With a valid bridge and adequate observations the gauge becomes identifiable. This is an algebraic *positive control*, already a result in TLICA's earlier finite construction; it is not evidence for JEPA by itself.

Render each example in at least two surface modalities:

- $g_1$: arbitrary symbols/feature tokens plus an independent nuisance code.
- $g_2$: independently permuted symbols/feature tokens plus separately sampled nuisance.
- A privileged test oracle stores the true state, pairing relation, and cross-component labels; **the learner never receives oracle states directly**.

Construct three explicit pairing regimes:

1. **Good views:** independent renderings that the oracle knows share the predeclared relevant latent world structure, or world-state pairs licensed by the same declared relation.
2. **Bad views:** two augmentations of *one* observation that preserve nuisance more strongly than the intended latent relation.
3. **Corrupted matches:** false purported positives joining incompatible states, a deliberate negative control distinct from bad-view augmentation.

These are separate from an **ambient co-occurrence stream** of unlabeled sequential observations. Ambient co-occurrences may be temporally associated but must **not** be silently relabeled as good-view positives.

## 3. Sampling and factorial contrast

Fix training-token exposure, observation frequency by node, embedding dimension, optimizer, training steps, number of proposed pairs, anti-collapse strength, query cost, and holdout difficulty before comparing any cells.

Use the **complete 2 × 2 × 2** principal factorial:

| Factor | Level 0 | Level 1 |
| --- | --- | --- |
| $V$: view generation | Same-observation bad views | Independently sampled oracle-good views |
| $P$: probe selection | Random/passive selection, cost-matched | Focus-/uncertainty-guided selection, cost-matched |
| $B$: labeled bridge | Redundant within-component control | Valid cross-component bridge |

Execute **all eight cells** before claiming an interaction. Keep the ambient exposure sequence fixed or randomized with paired seeds, and use the same hidden function across each matched block. In Level 0 of $P$, the matched query cannot secretly receive more privileged information. The $B$ factor makes a genuine new labeled relation available; record its supervision cost rather than crediting all improvement to self-supervision.

Separate calibration and mutation arms:

- **No-exposure null:** zero relevant examples; cross-component performance should be at the stated prior chance level.
- **Oracle-assisted positive control:** an explicit correct bridge in a sufficiently expressive, directly supervised solver should remove the relative-gauge ambiguity on the finite task.
- **Frequency-only and attention-only baselines:** no positive-view objective.
- **Good views without anti-collapse:** tests whether representation collapse can masquerade as low alignment loss.
- **False-match mutation:** replace the bridge or good-view correspondence with an incompatible pair while keeping count and marginals controlled.
- **Frame-gate mutation:** swap which nuisance/context feature attracts attention, holding the actual world-state distribution fixed.
- **Bridge topology ablation:** match degree and edge count while changing connectivity; report remaining topology differences, particularly spectral gap.
- **Source duplication ablation:** present multiple surface renderings derived from one original pipeline, and compare against independently generated views.

The good-view oracle is **teacher information**. The result cannot establish that an unassisted human observer would know which positives are good; measure pair-construction cost and audit the data sources.

## 4. Predeclare what is measured

**Primary endpoint:** accuracy on held-out **cross-component** labels, on newly generated symbol permutations and nuisance contexts after a fixed budget. Compare each factorial cell against its matched control. Use fixed fresh seed blocks and report confidence intervals, not selected best runs.

**Operational toolkit endpoint:** the learner must answer a new family of discrimination/composition queries using the acquired representation, under a declared tool interface, with better held-out correctness than a memorization-only control. A learned embedding that cannot be queried, composed, or used for prediction **does not count** as a new deployable TLICA verification tool.

Secondary diagnostics, kept separate:

- alignment of representations to the known hidden state after one justified orthogonal Procrustes fit, evaluated on disjoint pairs;
- top-$k$ eigenspace mismatch between declared normalized positive-pair kernels, with eigengaps and degeneracy documented;
- graph connectivity, number of residual relative-gauge classes, and bridge provenance;
- ambient association strength and durability after a delay;
- probe utilization and budget, focus allocation, and data-source lineage;
- timing of latent representation changes versus first held-out capability gain.

**No truth-score collapse:** $\kappa$, $\mu$, $\sigma$, $\varphi$, $\rho$, toolkit closure, and representation quality have different targets. In particular, the simulation's known labels are world-grounded truth for that toy only.

## 5. Train/validation/holdout and calibration discipline

Pre-register architecture, data generator, sampling seeds, split seeds, target metric, statistical comparison, stop rule, and analysis script. Keep the following independent:

- **Training:** local pairs, view augmentations, and allowed queried bridges.
- **Validation:** checkpoint selection and hyperparameters only.
- **Fresh holdout:** novel symbol permutations, nuisance distribution shifts, latent state combinations, and unseen cross-component queries; never used to choose a model or tuning rule.
- **Hostile holdout:** nuisance becomes anti-correlated with the label, and the active probe policy is deprived of a preferred easy bridge while preserving the total query budget.

If a bridge is part of the test case, do not reuse that exact observation as an unseen holdout. Avoid teacher-label leakage via filenames, ordering, augmentation keys, random seeds, or generated views. Report both raw training distribution and source-adjusted/provenance-aware interpretation.

A tiny CPU proof-of-concept can first use a **closed-form spectral embedding** for the finite pair graph, plus a separate supervised/readout solver. A neural implementation is a second, independent route, not a substitute for the mathematical control. The [authors' released implementation](https://github.com/galilai-group/prh-proof) can inform a later reproduction, but its benchmark training uses GPUs and is not a prerequisite for this finite TLICA test.

## 6. Precommitted verdict conditions

**Pass for the limited joint-bridge hypothesis:** at fixed budget and on fresh holdouts, a significant good-view × targeted-probe effect (or a clearly stated simpler contrast) produces genuine *new* cross-component discrimination beyond bridge-only, frequency-only, and attention-only baselines; positive and negative controls behave as declared; provenance explains pair construction; and improved alignment precedes or accompanies tool gain without being mistaken for its proof.

**Fail:** good-view and bad-view representations transfer equally under adverse nuisance shifts, active selection offers no differential above matched passive sampling, or all apparent benefit is explained by direct bridge supervision. If the learner cannot deploy an additional discriminator, the stronger "proto-pattern to tool" claim fails even when embedding alignment improves.

**Ambiguous:** duplicate or correlated sources, unbalanced supervision, insufficient seed/power, identical observed outcomes for live rivals, a collapsed embedding, an undefined usable-tool interface, or a nonrecoverable data generator. An ambiguous result calls for a better probe, not an optimistic claim.

If all eight cells are not run, do **not** report a three-way interaction. If the required oracle positive-pair grouping is unavailable to the modeled learner, the pathway from raw osmosis to good views remains **unconstructed**, not false.

## 7. Minimum reproducibility record for any eventual execution

Record repository commit, actual command line, dependency versions, environment, full source seeds, train/validation/test files or hashes, per-cell raw predictions, attention/query events, embedding snapshots, provenance maps, adversarial swaps, calibration traces, uncertainty method, exact model-selection rule, and the terminal test summary.

**Execution status as of this document:** no model trained; no new TLICA-specific ablation, holdout, or visual GitHub math-render check has been run. Predictions above remain **UNVERIFIED**.
