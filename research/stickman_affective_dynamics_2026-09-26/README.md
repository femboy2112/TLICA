# Stickman Affective Dynamics — Cold-Start Research Package

**Purpose:** support the application-paper candidate
[Stickman: Affective Mechanics and the Substrate Derivation of Colloquial Common Sense](../../applications/stickman_affective_dynamics_v0_1_0.md).

**Date:** 2026-09-26  
**Branch:** \`research/stickman-affective-dynamics-2026-09-26\`  
**Base:** \`90cf753c6088f21dfe1e8732398ba97896bee263\` (TLICA foundation v5.5.2)  
**Status:** research/application draft. Foundation untouched. Not registered in the application index or Makefile.  
**Author:** Leah. AI-assisted formulation, formalization, literature reconnaissance, and executable toy construction.

---

## 0. Cold-start in one paragraph

Stickman asks whether a large subset of colloquial human "common sense" can be recovered without modeling reflective agency at all. The proposal starts from TLICA's *Differentiated Affect*: affects are structural configurations that alter salience, action-readiness, preservation pressure, boundary operation, and embodied state. Stickman adds the missing application-level dynamics: context acts as generalized forcing on a minimal affective/substrate state, the state evolves under a dissipative equation of motion, and behavior is a coarse projection of the resulting trajectory. Common sense is then the modal response class across a declared reference population **only when the response distribution has a clear dominance margin**. Base Stickman excludes Mode B, slack, explicit option construction, long-horizon planning, and explicit reasons. A later StickmanPlus may add one-step and then two-step projected outcomes if they earn held-out predictive gain.

---

## 1. Read this first

1. [Application manuscript](../../applications/stickman_affective_dynamics_v0_1_0.md) — canonical statement of the idea.
2. [FORMALISM_AND_PROBES.md](FORMALISM_AND_PROBES.md) — equations, model-comparison discipline, response quotient, categorical form, probe ladder.
3. [CLAIM_LEDGER.md](CLAIM_LEDGER.md) — every load-bearing claim with status, support, and falsifier.
4. [SOURCES_AND_PRIOR_ART.md](SOURCES_AND_PRIOR_ART.md) — internal TLICA provenance plus external neuroscience/control-theory starting points.
5. [stickman_dynamics_demo.py](stickman_dynamics_demo.py) — standard-library toy that instantiates the overdamped vs inertial discriminator.
6. [stickman_dynamics_demo_results.json](stickman_dynamics_demo_results.json) — raw deterministic output from the toy.
7. [stickman_dynamics_demo_tests.txt](stickman_dynamics_demo_tests.txt) — test summary.

Any future model should be able to reconstruct the project from those files without conversation history.

---

## 2. The load-bearing correction

Do **not** model Stickman as a small rational agent.

The project's current governing form is:

\[
\text{context}
\to
\text{affective forcing}
\to
\text{substrate/affect trajectory}
\to
\text{response basin}
\to
\text{population response distribution}
\to
\text{colloquial common sense}.
\]

The response is not selected by a reflective chooser in base Stickman.

### Explicit exclusions

Base Stickman has no:

- mature Mode B;
- slack variable;
- explicit "reasons";
- moral evaluator;
- utility maximizer;
- long-horizon planner;
- rich semantic world model;
- recursive self-model;
- language generator.

Those can enter only in named extensions.

---

## 3. Relationship to TLICA

### 3.1 Donor application: Differentiated Affect

Primary donor:
\`applications/differentiated_affect_v1_0_2.md\`.

Relevant commitments:

- affect is a **configuration**, not an unanalyzed faculty;
- the affect criterion includes perturbation of **action-readiness**, salience, focus, profile stability, PCE, PtCns, and related architecture;
- affect is organized into connection, self, threat, boundary, and embodied clusters;
- embodied affect runs crosswise to the other clusters because it is organized by pathway;
- named emotion labels are downstream classifications of structural configurations.

Stickman proposes dynamics over a deliberately reduced, non-reflective projection of that architecture.

### 3.2 Foundation support

Primary foundation anchor:
\`foundation/3_formal_apparatus.md\`.

Relevant pieces:

- substrate-bound focus and salience;
- first-order salience capture;
- third-order somatic→cognitive mediation;
- osmotic imprinting;
- somatic compression retaining intensity, valence, action-tendency, and broad affective tone;
- v5.5.x driven dissipative dynamics;
- living substrate treated as a driven non-equilibrium system rather than a static fixed point.

### 3.3 Explicit open problem this targets

\`foundation/5_translations_open_problems_conclusion.md\` names **action-priority dynamics under existential pressure** as application-level work and separately leaves mixed-pathway dynamics and component-specific substrate compression open.

Stickman begins with the substrate-only slice and asks how far it predicts before future-state projection or reflective self-modeling must be added.

---

## 4. Formal core

Let \(q\in\mathcal Q_{\mathrm{SM}}\) be the fast Stickman state.

### Overdamped null

\[
\Gamma(q)\dot q
=
-\nabla V(q;c)
+
B(q)u_c(t)
+
\Sigma(q)\xi(t).
\]

This is the default model until a stronger family wins on holdout.

### Dissipative Lagrangian candidate

\[
L(q,\dot q;c)
=
\frac12\dot q^\top M(q)\dot q
-
V(q;c),
\]

\[
\mathcal D
=
\frac12\dot q^\top\Gamma(q)\dot q,
\]

\[
\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}
-
\frac{\partial L}{\partial q_i}
+
\frac{\partial\mathcal D}{\partial \dot q_i}
=
Q_i(c,t)+\Xi_i(t).
\]

The "mass" matrix \(M\) is a phenomenological second-order term, not literal mass. It is guilty until proven useful.

### Response readout

\[
\chi_c :
\mathcal T(\mathcal Q_{\mathrm{SM}})
\to
\mathcal R.
\]

### Common sense

For reference population \(P\),

\[
P_P(r\mid c)
=
\Pr[\chi_c(\tau)=r].
\]

Let \(r_1\) be the top response and \(\Delta\) its probability margin over the runner-up. Only if

\[
\Delta\ge\delta_{\mathrm{CS}}
\]

does the model emit a dominant common-sense response. Otherwise output \(\bot\): no common denominator.

---

## 5. The toy does one thing only

\`stickman_dynamics_demo.py\` is **not** a model of human emotion.

It demonstrates that the two dynamical families make distinguishable predictions in a calibrated one-dimensional case.

For a positive pulse \(u(t)\):

- stable first-order relaxation stays on the forced side and relaxes monotonically after pulse removal;
- a chosen underdamped second-order system overshoots and crosses the baseline.

That establishes a usable discriminator:

> After controlling delayed forcing and hidden state, does real affect show reproducible overshoot/phase structure that a matched first-order model cannot reproduce?

The toy cannot answer that question. Human data must.

---

## 6. Scope ladder

### Tier 0 — calibration
- nociceptive withdrawal;
- startle/blink/orienting;
- postural correction.

### Tier 1 — interoceptive regulation
- air hunger;
- hunger/thirst;
- thermoregulation;
- sleep pressure;
- bladder/bowel urgency.

### Tier 2 — acute defense
- looming threat;
- peripersonal intrusion;
- acute pain;
- instability/collision.

### Tier 3 — primitive social-affective coupling
- abrupt boundary violation;
- proximity threat;
- protective response toward a routed attachment target;
- simple affiliative repair.

### Tier 4 — not base Stickman
- articulated guilt/shame;
- complex jealousy;
- reputation strategy;
- explicit norm reasoning;
- long-horizon planning;
- moral justification.

Promotion outward must be earned tier by tier.

---

## 7. Population invariance rule

Do not say "universal human response" merely because a response appears widespread.

The proposed core criterion is conditional transport:

\[
I(R;P\mid X_{\mathrm{bio}},c)\approx0
\]

or a declared small divergence between population-conditioned response distributions after relevant substrate/context controls.

Population-specific thresholds and gains are allowed. A shared **structure** with varying parameters is the target.

If population label remains strongly predictive, demote that response from core Stickman.

---

## 8. StickmanPlus boundary

### Stickman+1
One-step action→outcome projection:

\[
a_t\mapsto\widehat o_{t+1}.
\]

### Stickman+2
One additional response step:

\[
a_t\mapsto\widehat o_{t+1}\mapsto\widehat r_{t+1}.
\]

Neither is automatically Mode B.

Mode B begins when the system takes its own response-generating structure as object and can reflexively reweight or rewrite it.

Base Stickman must not acquire slack merely because exhaustion changes its behavior. Exhaustion changes the substrate state directly.

---

## 9. Non-negotiable epistemic rules

1. **No foundation edit by elegance.** This branch proposes an application.
2. **No human inertia claim from the toy.** The toy is construction-level only.
3. **No population invariance by intuition.** It must be tested across declared populations.
4. **No response classes after seeing holdouts.** Freeze the quotient/readout first.
5. **No semantic smuggling in context.** A context parser cannot encode the answer.
6. **No affect necessity by definition.** Compare against direct stimulus→response baselines.
7. **No categorical ornament.** \(\mathbf{Stoch}\) earns its keep only through compositional transition kernels and transport tests.
8. **No Lagrangian cosplay.** If \(M\) adds no held-out gain, set it to zero.
9. **No "common sense" where the distribution is genuinely multimodal.**
10. **No novelty claim yet.** Rival literature mapping is incomplete.

---

## 10. Work completed on this branch

- Recovered the current v5.5.2 substrate dynamics and Differentiated Affect donor structure from repository bytes.
- Identified the relevant declared foundation open problems.
- Defined Stickman as a task-relative response-preserving quotient target.
- Separated world→context parsing from context→substrate dynamics.
- Defined an overdamped null and dissipative Lagrangian rival.
- Defined a falsifiable inertial signature.
- Defined population common sense with an abstention region.
- Defined conditional population-invariance as a measurable target.
- Defined a \(\mathbf{Stoch}\) transition-kernel formulation.
- Defined Stickman+1/+2 and preserved the semantic boundary around Mode B.
- Ran a deterministic finite toy locally and recorded raw results and tests.
- Performed a first literature reconnaissance for interoception/allostasis, withdrawal reflex, defensive behavior, sleep loss, and air hunger.

No human dataset was fit. No independent implementation was run. No full repository \`make validate\` was executed from this remote-writing session.

---

## 11. Highest-value next work

### Priority 1 — identify the first real dataset
Find a public human time-series dataset for one Tier-0/Tier-1 paradigm with:

- known forcing onset/offset;
- repeated trials;
- a measurable dynamic response;
- enough sampling to estimate phase/overshoot;
- participant metadata adequate for hierarchical modeling.

Nociceptive withdrawal or startle may be the cleanest first target.

### Priority 2 — fit four rivals
Precommit:

1. direct stimulus→response baseline;
2. first-order overdamped Stickman;
3. second-order dissipative Stickman;
4. generic matched-capacity state-space model.

Do train/validation/holdout separation.

### Priority 3 — coordinate discovery
Do not pick affect axes by prose. Compare candidate latent representations and ask which dimensions survive ablation across domains.

### Priority 4 — transport
After one domain works, test the same structural family on a second domain before social extension.

### Priority 5 — only then social cases
Use safe low-stakes tasks. A successful heat/reflex model does not earn interpersonal universality.

---

## 12. Cold-start handoff prompt

\`\`\`text
Work in femboy2112/TLICA on the non-main branch
research/stickman-affective-dynamics-2026-09-26.

Before editing, read:
1. applications/stickman_affective_dynamics_v0_1_0.md
2. research/stickman_affective_dynamics_2026-09-26/README.md
3. FORMALISM_AND_PROBES.md
4. CLAIM_LEDGER.md
5. SOURCES_AND_PRIOR_ART.md
6. applications/differentiated_affect_v1_0_2.md
7. foundation/3_formal_apparatus.md §§8.1-8.11
8. foundation/5_translations_open_problems_conclusion.md §13.3

Run stickman_dynamics_demo.py and inspect the recorded results.

The central author insight is:
derive colloquial common sense backward from Differentiated Affect by giving the
non-reflective affective/substrate layer equations of motion. Base Stickman is not
a tiny rational agent. It has no mature Mode B, slack, explicit reasons, long-horizon
planning, or rich semantic world model. Context supplies substrate-relevant forcing;
the resulting affect trajectory projects to a coarse response basin. Common sense is
the modal population response only when a predeclared dominance margin exists.

Keep the overdamped first-order dynamics as the null. Treat Lagrange-d'Alembert +
Rayleigh dissipation as a stronger candidate whose inertial term must earn held-out
predictive value. The current toy shows only that overshoot/sign reversal can
discriminate the families; it is not human evidence.

Do not choose affect coordinates merely because they sound psychologically natural.
Treat the minimal state as a response-preserving quotient target and discover dimensions
through ablation/model comparison. Keep the world→context parser separate so semantics
cannot smuggle the response into the input.

Test population invariance conditionally, preferably with hierarchical models. Allow
population-specific parameters. Do not claim universality unless population label adds
little held-out predictive information after biological state and context are controlled.

StickmanPlus may add one-step then two-step action-outcome projection only if base
Stickman fails and the added model improves holdout prediction. Do not call generic
prediction Mode B; preserve TLICA's reflexive-meta-reasoning meaning.

The next verdict-changing move is to identify a real human Tier-0/Tier-1 time-series
dataset and fit four preregistered rivals: direct stimulus→response, overdamped
Stickman, inertial Stickman, and matched-capacity generic state-space. Preserve raw
outputs, train/validation/holdout split, exact claim statuses, and negative results.

Do not edit the frozen foundation. Do not register the application as complete.
\`\`\`
