# Bridge Topology and Nerf-Grokking

## Preregisterable protocol for *The First Atomic Connection*

**Status:** Experiment specification, v0.1  
**Date:** 2026-08-29  
**Branch:** `research/grokking-toolkit-closure-2026-08-29`  
**Parent paper:** [`grokking_as_toolkit_closure_2026-08-29.md`](grokking_as_toolkit_closure_2026-08-29.md)  
**Execution status:** **UNRUN**. No numerical result or significance claim appears here.

---

## 0. Question and acceptance criterion

Does the topology connecting locally learnable subproblems control whether and when a learner acquires a global rule, after raw sample count and first-order token frequency are matched?

The confirmatory contrast is:

$$
\boxed{
\text{degree-matched connected evidence}
\quad\text{vs.}\quad
\text{degree-matched disconnected evidence}.
}
$$

The primary outcome is time from training-set memorization to sustained cross-component generalization.

Support requires all of the following:

1. connected and disconnected conditions both reach matched local/training performance;
2. connected evidence supports above-chance cross-component transfer;
3. disconnected evidence remains at its symmetry-derived chance bound across randomized hidden task instances;
4. replacing redundant internal edges with a small number of valid bridges improves transfer more than equally many non-bridging examples;
5. corrupted bridges do not reproduce the benefit;
6. at least one preregistered latent closure measure changes before behavioral grokking.

A null result is not rescued by a visually attractive representation plot.

---

## 1. Exact task

Choose a prime modulus $p$, initially from $\{31,47,59,97\}$. Create opaque token sets

$$
A=\{a_0,\ldots,a_{p-1}\},
\qquad
B=\{b_0,\ldots,b_{p-1}\}.
$$

For each independent task instance, draw random bijections

$$
u:A\to\mathbb Z_p,
\qquad
v:B\to\mathbb Z_p.
$$

The label is

$$
y(a,b)=u(a)+v(b)\pmod p.
$$

Token names carry no coordinate information. Hidden permutations are resampled across task instances.

Training examples are edges $E\subseteq A\times B$ of the bipartite observation graph

$$
G_E=(A\sqcup B,E).
$$

If $G_E$ has $c$ connected components, each component admits an independent gauge:

$$
u'(a)=u(a)+\lambda_k,
\qquad
v'(b)=v(b)-\lambda_k.
$$

After fixing one global gauge, the evidence leaves $p^{c-1}$ relative alignments unresolved. For an unseen pair crossing two components, the label shifts by $\lambda_i-\lambda_j$. Under uniformly randomized hidden gauges,

$$
\mathbb E[\mathrm{Acc}_{\mathrm{cross}}]\le \frac1p.
$$

No additional optimization on the same disconnected evidence can identify missing relative alignment information.

---

## 2. Matched dataset conditions

Across primary conditions, match modulus, training-edge count, every token's degree, train/test sizes, architecture, optimizer, step budget, initialization distribution, and evaluation cadence. Match label histograms where feasible. Use regular bipartite graphs and degree-preserving 2-switch rewiring.

### C1 — Connected, high spectral gap

A connected $d$-regular bipartite graph with broad mixing.

### C2 — Connected, low spectral gap

A connected $d$-regular graph with a strong bottleneck. This tests whether propagation difficulty matters after connectivity exists.

### C3 — Disconnected, degree matched

A union of $k>1$ disjoint $d$-regular bipartite components. Local learning can succeed, but cross-component labels remain unidentifiable.

### C4 — Minimal valid bridge repair

Starting from C3, use degree-preserving 2-switches to join all components while preserving edge count and every vertex degree. Correct bridge labels disclose relative gauges.

### C5 — Redundant internal-edge control

Perform the same number of edge replacements as C4, but keep replacements inside the inherited components.

### C6 — Corrupted-bridge mutation

Use C4's topology but add nonzero modular offsets to bridge labels. An overparameterized model may memorize them, but they should not produce coherent global alignment.

### C7 — Random-label negative control

Keep C1's graph and independently randomize edge labels.

### C8 — Dense positive control

Use a much denser connected graph to verify that the architecture can represent and learn the task.

---

## 3. Holdouts

Partition unobserved pairs using C3's inherited components.

- **H1: within-component holdout.** Both endpoints lie in one component.
- **H2: cross-component holdout.** Endpoints lie in different components. This is the confirmatory endpoint.
- **H3: surface-renamed transfer.** Rename tokens and provide a small alignment set.
- **H4: deeper composition.** Test chained or multi-hop variants.

H3 and H4 remain exploratory unless separately powered.

---

## 4. Models and training

Run at least:

- a small transformer trained from scratch;
- a ReLU MLP using learned token embeddings.

An explicit additive factor model is a useful positive-mechanism control. Do not use a pretrained language model for the first confirmatory run because pretraining supplies uncontrolled relations among tokens.

Use pilot runs only to select modulus, degree, architecture size, weight-decay range, checkpoint cadence, and maximum steps. Exclude pilot seeds from confirmatory statistics.

Save initialization, dense checkpoints around memorization and any transition, regular plateau checkpoints, and final state. Runs that fail to grok by the fixed maximum step count are right-censored rather than discarded.

---

## 5. Operational thresholds

For a preregistered stability window $W$, define memorization time:

$$
t_{\mathrm{mem}}
=
\inf\left\{
t:
\mathrm{Acc}_{\mathrm{train}}(s)\ge 0.99
\text{ for every }s\in[t,t+W]
\right\}.
$$

Define behavioral grokking time:

$$
t_{\mathrm{grok}}
=
\inf\left\{
t\ge t_{\mathrm{mem}}:
\mathrm{Acc}_{H2}(s)\ge\gamma
\text{ for every }s\in[t,t+W]
\right\},
$$

with $\gamma$ fixed before confirmatory runs.

Do not define the nucleation boundary retrospectively. Choose a latent order parameter $Q(t)$ during the pilot, freeze its threshold, then define

$$
t_\star
=
\inf\left\{
t:
Q(t)>\theta_Q
\text{ and }
\dot Q(t)>0
\text{ for a sustained window}
\right\}.
$$

The selected delayed-grokking regime supports the proposed sequence when many runs satisfy

$$
t_{\mathrm{mem}}\le t_\star<t_{\mathrm{grok}}.
$$

Earlier nucleation is permitted by the parent theory and must be reported rather than recoded.

---

## 6. Latent diagnostics

Use at least two methodologically different diagnostic families.

### Gauge alignment

Decode hidden coordinates from token representations. Compare component-wise optimal gauge alignment, one-global-gauge alignment, and the gap between them.

A candidate coherence score is

$$
Q_{\mathrm{gauge}}(t)
=
1-
\frac{
\mathcal E_{\mathrm{global}}(t)-\mathcal E_{\mathrm{component}}(t)
}{
\mathcal E_{\mathrm{null}}
}.
$$

### Fourier structure

Because the task is cyclic, the discrete Fourier basis supplies a declared common basis. Track spectral concentration, phase-sum consistency, dominant-frequency stability, and component-to-component phase alignment.

### Causal intervention

Ablate candidate frequencies, neurons, heads, or subspaces. A load-bearing generalizer should damage H2 transfer more than training memorization.

### Rival-compatible measures

Track weight norm, effective rank, spectral entropy, compressibility, and activation sparsity. These may explain dominance or cleanup but do not by themselves establish gluing.

Same-model probes are not independent witnesses. Preserve raw representations and run mutation tests.

---

## 7. Statistical analysis

Treat $t_{\mathrm{grok}}$ as a censored event time. Report seed-level outcomes, nonparametric time-to-event curves, median or restricted mean time-to-grok, and bootstrap confidence intervals.

The primary contrasts are C4 versus C3 and C4 versus C5 in probability of grokking within the fixed budget and in H2 accuracy. The secondary contrast is C1 versus C2.

For C3, evaluate H2 accuracy across independently randomized hidden tasks. The null is the theorem-derived value $1/p$, not an arbitrary low-accuracy threshold. Above-bound performance triggers a leakage and implementation audit before theoretical interpretation.

---

## 8. Ordinary-cause audit

Before interpreting a result, rule out:

- train/H2 overlap;
- token names correlated with hidden coordinates;
- unequal edge count, degree, or token frequency;
- different optimizer updates or parameter counts;
- label-distribution mismatch large enough to explain the result;
- graph-generation bugs;
- bridge edges that fail to join components;
- disconnected graphs mislabeled connected;
- hidden test use in stopping or checkpoint selection;
- reused seeds;
- numerical instability;
- test contamination through curricula.

Positive controls must generalize and negative controls must fail. Otherwise the experiment is uncalibrated.

---

## 9. Mutation tests

1. **Bridge deletion after grokking.** Continue training without bridge examples. Persistent transfer suggests internal stabilization; selective transfer loss suggests continuing evidence dependence.
2. **Generator ablation.** Remove the common-basis subspace while preserving local memorization as much as possible.
3. **Surface remapping.** Rename tokens and supply a small alignment set. Fast recovery supports generator retention.
4. **False bridge insertion.** Supply a coherent but wrong relative offset and observe whether an alternative global alignment forms.
5. **Component gauge permutation.** Independently shift components at evaluation to verify the predicted dependence on global alignment.

---

## 10. Human analogue

Use a smaller opaque symbol system, for example $p=7$ or $p=11$. Randomly assign participants to connected, disconnected, valid-bridge, and redundant-example conditions.

Match groups on local mastery rather than clock time. Then measure H1/H2 accuracy, response time, confidence, surface-renamed transfer, strategy report, and Aha timing.

A self-reported first connection is phenomenological evidence only. A stronger human nucleation marker requires transfer, mutation robustness, and a strategy capable of predicting novel cases. Participants may transfer without an Aha or report an Aha without objective closure.

This study supports only a shared abstract topology. It cannot establish that humans and neural networks use the same substrate mechanism.

---

## 11. Decision table

| Outcome | Verdict |
|---|---|
| C4 groks; C3/C5 do not; C6 is impaired; latent alignment precedes behavior | Strong support for bridge-sensitive closure |
| C1 and C2 perform alike while C3 fails | Connectivity supported; spectral-gap refinement unsupported |
| C3 exceeds $1/p$ after full audit | Task assumptions violated or side information exists |
| All valid-label conditions behave alike | Topology adds little in this regime |
| Dense control fails | Experiment uncalibrated |
| Weight norm predicts transition and topology has no effect | Dominance/regularization account favored |
| Probe predicts but ablation has no effect | Probe correlational; mechanism UNVERIFIED |
| Human Aha changes without transfer | Phenomenology dissociates from closure |
| Human valid-bridge group transfers after matched local mastery | Supports shared abstract constraint |

---

## 12. Reproducibility

Preserve the exact task generator, hidden seeds, graph-construction code, connectivity and spectrum checks, configurations, model seeds, raw logs, checkpoints, analysis scripts, environment lockfile, all exclusions, and failed runs with reasons.

A minimal pilot uses $p=31$, $d\in\{4,6\}$, conditions C1/C3/C4/C5/C7/C8, one transformer, one MLP, and ten exploratory seeds per condition. The pilot passes only if the dense control generalizes, random labels do not, disconnected H2 remains near $1/p$, at least one connected condition transfers, and all graph-matching constraints are verified.

---

## 13. Claim ledger and falsifier

| Claim | Status |
|---|---|
| Disconnected observations leave independent component gauges in the stated additive model | **Disclosed** |
| Uniform unresolved gauges bound cross-component exact-match accuracy by $1/p$ | **Disclosed** |
| A valid component-joining bridge removes one gauge degree of freedom | **Disclosed** |
| Degree-preserving bridge rewiring accelerates neural grokking | **UNVERIFIED** |
| Spectral gap predicts time-to-grok once connected | **UNVERIFIED** |
| Latent gauge alignment precedes behavior | **UNVERIFIED** |
| Human learners exhibit the same topology effect | **UNVERIFIED** |
| Aha timing identifies objective nucleation | **Not assumed** |
| The mechanism scales to practical LLM pretraining | **Dark under this protocol** |

The verdict-changing question is:

> Once local learnability and ordinary dataset statistics are matched, does changing only the relational topology that glues local pieces change whether and when a learner acquires a global rule?

If repeated calibrated experiments answer no, downgrade the strong bridge-topology account. If the effect survives mutation, causal intervention, and independent implementation, the paper earns its central empirical result:

$$
\boxed{
\text{Grokking depends not only on how many paths are learned,
but on whether those paths can be globally glued.}
}
$$
