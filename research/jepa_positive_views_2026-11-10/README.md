# Positive-view geometry as a candidate bridge between osmotic imprinting and verification-tool development

**Date:** 2026-11-10  
**Status:** Research-tier computational proposal; TLICA foundation unchanged. Conditional statements about the cited JEPA theorem are **SOURCE-REPORTED**, existing TLICA dependencies are **OBSERVED IN ARCHIVE**, the proposed bridge is **CONJECTURED**, and human or neural-mechanism claims are **UNVERIFIED**. No TLICA-specific experiment is reported as run.  
**Authorial provenance:** Leah asked whether the late-October 2026 LeCun/Balestriero paper could inform TLICA's active or osmotic learning. The active/osmotic bridge and formal decomposition below are an AI-assisted proposal in response, not a result of the cited authors.

## 0. The load-bearing question

Can a representation-learning mechanism explain how repeated ambient experience seeds an implicit substrate pattern, while later directed attention and discriminating probes make that pattern accessible as a *usable verification tool*?

The proposed answer is **possibly**, but only after separating three operations that are easy to collapse:

1. **Ambient association:** experience writes a pattern into a substrate even when the relation is not the object of focus. It may encode an accidental correlation.
2. **Positive-view learning:** a learner uses deliberately specified pairs of observations which preserve a relevant latent world-level relation. The quality and source of those pairs are part of the claim.
3. **Verification-tool development:** an agent acquires an operational discriminator it can actually deploy to test a proposition or compose with existing tools. Aligned representations alone do not establish this.

**Candidate thesis:** osmotic imprinting supplies proto-patterns and candidates for relational structure; contact-driven or self-directed inquiry can change which relations are sampled, checked, and made available for compositional inference. A JEPA-like positive-view kernel may model *one* intermediate representation stage. The substrate association graph, the JEPA positive-pair graph, and the verified toolkit graph must remain different objects unless an explicit transport is established.

This dossier preserves the prior [grokking/toolkit-closure work](../grokking_as_toolkit_closure_2026-08-29.md) and [accidental frame-scattering model](../tlica_higgs_phenomenological_mass_2026-10-21/FRAME_SCATTERING_OSMOTIC_IMPRINTING_2026-10-22.md) as live comparators rather than renaming their results.

## 1. External result: what Balestriero and LeCun actually establish

Primary source: Randall Balestriero and Yann LeCun, *Proving and Improving the Platonic Representation Hypothesis with JEPAs*, arXiv:2610.39302, first submitted 2026-10-29, especially §§2 and 7 and Appendix A. See [SOURCES.md](SOURCES.md).

Their theorem concerns an **idealized** class of jointly embedded predictive objectives. One finite world has states $z\in\mathcal Z$ with $p(z)>0$; modalities observe states via injective renderings $g_m$, and positive pairs in each modality are generated from a symmetric world-state pairing law with common marginals. For the shared-positives result the modalities must agree on the world-level pairing law. The objectives are invariant under orthogonal transformations, and their population minimizers must be unique up to rotation. In the whitened, second-order anti-collapse case, a suitable spectral gap supplies this uniqueness condition.

The spectral version uses the normalized positive-pair kernel:

$$
K_\pi=D^{-1/2}\Pi D^{-1/2},
\qquad D=\mathrm{diag}(p),
\qquad \Pi_{zz'}=\pi(z,z').
$$

Under its assumptions, separately optimized modality representations of the same world agree **up to an orthogonal rotation**. When positive-pair kernels differ, a Davis–Kahan-type bound controls spectral representational mismatch relative to kernel difference and an eigengap. This is a statement about *representation geometry*, not the epistemic truth of arbitrary learned beliefs.

The paper calls independent observations of the relevant world-level state or relation **good views**; transformations of one observation can preserve modality-specific nuisance and become **bad views** for cross-modal alignment. The paper's reported comparison of 21.6 million versus 900 million training samples (about **42 times fewer samples**) is an alignment result on a specific corpus/metric, **not** a universal ratio of learned capacity to parameters, intelligence, biological efficiency, or token speed. Its full LeJEPA distributional regularizer and real lossy modalities are not covered by every idealized uniqueness claim; its analysis uses an identity predictor rather than a general action-conditioned learned predictor.

**Critical negative condition:** sheer repeated co-occurrence is **not** automatically a valid positive pair. A bell followed by food, for example, is a temporal association between different events; it is not necessarily two exchangeable views of one scene. Such sequential dependence may call for a transition/prediction model, not invariance between their embeddings. We therefore do **not** identify osmotic learning with the paper's good-view JEPA theorem.

## 2. TLICA objects already available; no foundational amendment

The frozen [formal apparatus §§8.1–8.7](../../foundation/3_formal_apparatus.md), [access and development §3.2](../../foundation/2_access_and_development.md), and [substrate/imprinting reader](../../docs/substrate-focus-and-imprinting.md) already distinguish:

- **Substrate-bound focus capacity:** $M_m(t)=\Gamma^M_m(\mathsf S_m,t)$ and focus allocation cannot exceed that inherited bound.
- **Contact-driven versus self-directed focus:** the latter becomes available developmentally, never replacing the former entirely.
- **Focus-driven probe weighting:** $\mu_t^m=\Lambda^\mu_m(\mathsf{Foc}_t^m,\kappa_{m,t}^{\mathrm{out}},Q_t^m)$; this influences what is sampled and tested.
- **Focus/contact-driven imprinting:** explicit content-edge update strengths are functions of contact and focus.
- **Osmotic imprinting (§8.7):** a parallel substrate-level mechanism through repeated ambient co-occurrence that requires neither focus on the relation nor explicit verification or mode operation. Mechanism-online does not entail a nonzero durable update at every instant.
- **Verification-tool imprinting:** substrate proto-tools may precede Mode B access and later refinement into deployable discriminators.

The [choice-as-filter paper §15](../../applications/choice_as_filter_v0_1_0.md) already states the operational distinction: **osmotic baseline update versus filter-amplified differential update**. A chosen focus filter does not switch off osmotic learning.

The [grokking dossier](../grokking_as_toolkit_closure_2026-08-29.md) already models local paths, tested overlap transports, toolkit closure relative to admissible operations, and a gap between closure *becoming possible* and its later behavioral dominance. This is the most natural landing site for a positive-pair geometry hypothesis. The [frame-scattering dossier](../tlica_higgs_phenomenological_mass_2026-10-21/FRAME_SCATTERING_OSMOTIC_IMPRINTING_2026-10-22.md) gives a finite counterexample to the inference that repeated coincidence implies a real semantic relation.

**Terminology:** TLICA does not have a free-standing primitive named "active learning." Here it means contact-driven or self-directed **focus and probe selection**, as available under the existing substrate/toolkit constraints. It is not automatically synonymous with volition, Mode B, reinforcement learning, or the ML literature's label-querying definition of active learning.

## 3. Three graphs, three different epistemic roles

Fix an observer $m$, an external state process $z_t\in\mathcal Z$, and observations $o_t^r=g_r(z_t,\nu_t^r)$ in modality $r$; $\nu$ represents viewpoint or other modality-specific details. The experimenter may know $z_t$ in a synthetic world; the modeled observer normally does not.

| Typed object | Edges / meaning | What it can establish |
| --- | --- | --- |
| $G_{\mathrm{amb},t}$ | Substrate associations inferred from ambient, possibly delayed co-occurrence | An acquired association, not that the associated events have a true world-level relation |
| $G_{\mathrm{view},t}$ | Validated or deliberately hypothesized positive pairs for an explicit representation objective | A candidate invariant geometry; only oracle-validated edges satisfy the theorem's "good view" premise |
| $G_{\mathrm{tool},t}$ | Local inference paths whose compatibility / transport has been *tested* under declared operations | Whether a composable discriminator is constructible and can actually be used |

A candidate directed process is:

$$
G_{\mathrm{amb},t}
\ \longrightarrow\
\text{candidate pair hypotheses}
\ \xrightarrow{\mathrm{probe\ and\ source\ checks}}\
G_{\mathrm{view},t}
\ \xrightarrow{\mathrm{operational\ tests}}\
G_{\mathrm{tool},t}.
$$

These arrows are **contingent tasks**, not guaranteed implications. A good-view embedding may fail to become available to the observer's toolkit. An ambient association may never justify a positive pair. A tool may be acquired without a JEPA-like representation at all.

### 3.1 Osmotic candidate update (application-level only)

For a toy finite association matrix $C_t$ define, illustratively,

$$
C_{t+1}=(1-\epsilon_t)C_t+
\epsilon_t\,h(o_t,o_{t-\ell}),
\qquad 0\leq\epsilon_t\leq1.
$$

Here $h$ records a declared relation or co-occurrence feature and $\ell$ is a declared lag. This is **not a new TLICA foundation law** or a human-neuroscience identification; TLICA §§8.7–8.8 intentionally leave osmotic rates unspecified. The effective update may approach zero despite the mechanism remaining online. This toy can create strong false associations under correlated nuisance or accidental coincidences, matching the risk exposed in the earlier frame-scattering dossier.

### 3.2 Directed probe / pairing channel

Let $\mathcal T_t$ be the explicit toolkit and $\mathcal A$ a declared set of admissible compositions. A focus-constrained probe policy selects a feasible query $q_t$ using the observer's actual access and current $\mu_t$. External feedback may check a candidate relation and add or remove edges in a **recorded** candidate positive-pair distribution $\pi_t$.

Only in a controlled finite-world regime where $\pi_t$ meets the paper's assumptions may we consider the spectral positive-view objective:

$$
\mathcal L_{\mathrm{view},t}(f)
=
\mathbb E_{(z,z')\sim\pi_t}
\left\|f(g_r(z))-f(g_r(z'))\right\|^2
+
\Omega_{\mathrm{ac}}(f).
$$

The anti-collapse condition is indispensable. So are the distribution/marginal and spectral assumptions if importing the paper's theorem. This objective is a candidate model of *invariant representation learning*, **not** a definition of TLICA's osmotic process or $\varphi$.

An explicit tool-acquisition event must be evaluated separately: an accessible operation $q$ changes the observer's feasible discrimination or composition on withheld problems. The resulting improvement must survive source/probe controls and be measured on held-out tasks; embedding alignment is insufficient.

## 4. The nontrivial bridge to TLICA grokking

The earlier [connected-overlap theorem](../grokking_as_toolkit_closure_2026-08-29.md) is about identifiability under a specified local-path compatibility graph, while the JEPA theorem is about eigenspaces of a specified positive-pair kernel. **They are not the same theorem and their graphs are not interchangeable.**

Nevertheless, there is a testable candidate relationship:

1. Ambient experience accumulates locally useful but possibly incompatible proto-patterns.
2. Good-view observations reduce *some* representation ambiguity when they share world-grounded structure and satisfy anti-collapse requirements.
3. A discriminating query may supply a new **validated overlap bridge** between previously disconnected local tool paths.
4. If the bridge survives transport tests and grants new operations, $\mathrm{Cl}_{\mathcal A}(\mathcal T_t)$ can gain genuinely useful global traversal.
5. Generalization can improve later, independently of when the representation first became available. This follows the old dossier's distinction between nucleation/availability and behavioral disclosure.

One bridge can be disproportionately informative if it removes a relative gauge freedom in the existing finite connected-overlap toy. That does **not** prove a large spectral eigengap or a biological insight event; those would require their own measurements.

**Countermodel:** two encoders can align tightly on a nuisance variable shared by training observations while failing to distinguish a withheld causal world variable. Alignment and high coherence can therefore coexist with a wrong source map. The "good views" premise is precisely the difficult external check, not a description the learner may assume about any convenient pair.

## 5. Coordinates and epistemic firewalls

For every proposed inference report the relevant TLICA diagnostics separately:

- **$\kappa$ / contact:** what reached the observer; do not silently replace it with learned salience or exposure frequency.
- **$\mu$ / probes:** which query or encounter was available and selected; fix the sampling policy and query cost.
- **$\sigma$ / source-map adequacy:** which latent state, teacher, captioning pipeline, or independent observation licensed the pairing; identical upstream provenance is not independent evidence.
- **$\varphi$ / toolkit-relative truth-indistinguishability:** whether an actual available discriminator distinguishes the proposition from true under present tools. An undefined pathway is not falsehood; alignment is not $\varphi$.
- **$\rho$ / identity coupling:** whether a learned representation is integrated into the I's identity network. Neither a high-$\rho$ disposition nor an aligned embedding warrants correctness.
- **$\mathrm{Cl}_{\mathcal A}(\mathcal T_t)$ / toolkit closure:** may change only when a new admissible and accessible operation is demonstrated; its existence is not implied by an eigenvector.
- **Representation alignment, graph connectivity, and eigengap:** useful independent diagnostics, not truth probabilities or direct measures of human understanding.

**Notation collision:** the JEPA paper uses a $\rho(f)$ quantity for a scene-explained fraction. This is **not** TLICA's $\rho$ identity-correlation coordinate. Do not import it under the same name.

No literal physical phase, quantum evidence, neural wiring mechanism, or universal efficiency claim follows. A rotation between embeddings is an orthogonal coordinate change. In TLICA's operational language: **no declared transport, no phase claim.**

## 6. Discriminating experiment and expected verdict

The complete preregisterable design is in [PROBE_PROTOCOL.md](PROBE_PROTOCOL.md). Use a finite synthetic world with observer-visible nuisance and a separately held-out causal/state variable. Compare ambient-only co-occurrence, matched good-view exposure, directed validated bridges, corrupted bridges, nuisance-paired "bad views," and no-exposure controls with matched capacity, exposure, and query budgets.

**Pass, limited:** valid bridge conditions outperform sample-, degree-, and attention-matched controls on withheld cross-component problems **and** the learner can deploy a genuinely new discriminator. If spectral alignment changes first and toolkit performance later, that is a measurable temporal ordering, not proof of a neural story.

**Fail:** gains vanish with provenance, sampling, nuisance, and budget controls; bad views perform equally well on independent world holdouts; or no new discriminating operation becomes available.

**Ambiguous:** oracle world grouping leaks into a condition unnoticed, toolkit closure is not operationalized, graph spectral diagnostics are post-hoc fitted, or all conditions are test-indistinguishable at the chosen power.

**Next verdict-changing probe:** the positive-versus-corrupted **bridge-swap** experiment, fixing exposure count, per-node frequencies, encoder capacity, and attention but exchanging only whether the added pair is a valid world-level overlap.

## 7. What this dossier does *not* establish

- That LeCun and Balestriero proved a general theory of human learning or a general 42-fold efficiency improvement.
- That osmotic co-occurrence alone generates "good views," truth, or epistemic verification.
- That attention creates world-state relations or turns every implicit association into a valid tool.
- That high alignment implies a correct source map, high $\varphi$, high $\rho$, or coherent human selfhood.
- That a toy spectral correspondence proves biological substrate plasticity, subjective understanding, or a new theorem connecting TLICA's graph to JEPA eigenvectors.

The [claim ledger](CLAIM_LEDGER.md) records what is observed, established conditionally, conjectured, or still unverified. Preserve the frozen TLICA foundation. This is a **research bridge and test plan**, not an amendment to the architecture.
