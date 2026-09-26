# Claim Ledger — Stickman Affective Dynamics

**Application candidate:** [Stickman: Affective Mechanics and the Substrate Derivation of Colloquial Common Sense](../../applications/stickman_affective_dynamics_v0_1_0.md)  
**Branch:** \`research/stickman-affective-dynamics-2026-09-26\`  
**Base:** \`90cf753c6088f21dfe1e8732398ba97896bee263\`  
**Date:** 2026-09-26

**Status vocabulary:** Disclosed / Corroborated / Observed / Conjectured / UNVERIFIED / Dark / Refuted

"Disclosed" means a formal result or repository-text fact within a declared boundary. "Observed" means seen in an executed run at exactly the stated scope. A finite toy does not corroborate a human mechanism.

---

## C-001 — Differentiated Affect supplies structural affect configurations rather than primitive emotion labels

**Claim.** The current TLICA application paper treats affect as configurations of the maximally-self-defined I and associated operators, with an affect criterion involving salience, action-readiness, profile stability, PCE, PtCns, focus, or related architecture.

**Status:** **Disclosed within repository text.**

**Support:** \`applications/differentiated_affect_v1_0_2.md\`.

**Boundary:** This does not supply equations of motion.

---

## C-002 — Current foundation supplies substrate-mediated first/third-order pathways and driven dissipative state evolution

**Claim.** TLICA v5.5.2 contains first-order salience mediation, third-order somatic→cognitive mediation, osmotic imprinting, and a driven relaxational baseline dynamics.

**Status:** **Disclosed within repository text.**

**Support:** \`foundation/3_formal_apparatus.md\`, especially §§8.1–8.10.

**Boundary:** Stickman's \(q\), \(V\), \(M\), \(\Gamma\), and response basins are application objects, not silently identified with foundation \(b,f,\rho\).

---

## C-003 — Action-priority dynamics under pressure are an open application-level problem

**Claim.** The foundation explicitly leaves the combination of substrate urgency, third-order activation, and future projection into specific action priority unresolved.

**Status:** **Disclosed within repository text.**

**Support:** \`foundation/5_translations_open_problems_conclusion.md\` §13.3.

**Consequence:** Stickman is positioned as a candidate solution to a declared open problem rather than as a foundation correction.

---

## C-004 — Stickman can be defined as a task-relative response-preserving quotient target

**Claim.** For a declared context/response task \(T\), complete human states can be grouped by equality of their response signatures; the resulting quotient is a mathematically coherent target notion of "minimal Stickman."

**Status:** **Disclosed inside the proposed formal model.**

**Reason:** equality of response signatures defines an equivalence relation when exact equality is used.

**Caution:** approximate similarity need not be transitive. Do not write a quotient by an approximate relation unless transitivity is established or a clustering/cover construction is used instead.

**Empirical debt:** whether a useful low-dimensional quotient exists for real human data is **UNVERIFIED**.

---

## C-005 — Base Stickman excludes mature Mode B and slack

**Claim.** The base model intentionally omits reflexive self-modeling/reweighting and the TLICA slack construct.

**Status:** **Disclosed by model definition.**

**Reason:** the research question is how much response structure exists before reflective agency is added.

**Falsifier of usefulness, not of definition:** if even Tier-0/Tier-1 response prediction requires explicit reflective variables, base Stickman has little explanatory scope.

---

## C-006 — Context parsing and substrate response are distinct stages

**Claim.** A world-state→perceived-context map \(\Pi_{\mathrm{perc}}\) must be separated from context→Stickman forcing/dynamics.

**Status:** **Disclosed as a modeling discipline; empirical factorization UNVERIFIED.**

**Purpose:** prevents semantic leakage. Labeling a complex scene "dangerous" permits a model of response to perceived danger; it does not explain danger recognition.

**Failure condition:** the context representation encodes response labels or downstream action directly.

---

## C-007 — An overdamped first-order dynamics is the required null

**Claim.** Stickman's first serious model comparison should include

\[
\Gamma(q)\dot q
=
-\nabla V(q;c)+B(q)u_c(t)+\Sigma(q)\xi(t)
\]

as a conservative dissipative null.

**Status:** **Conjectured methodological choice**, motivated by the current foundation's relaxational dynamics and parsimony.

**Falsifier:** a simpler non-affective or direct stimulus→response model predicts equally well; then even the overdamped affective state may be unnecessary.

---

## C-008 — Lagrange–d'Alembert + Rayleigh dissipation is a coherent stronger candidate

**Claim.** A dissipative second-order candidate

\[
M\ddot q+\Gamma\dot q+\nabla V(q;c)=Q(c,t)+\Xi(t)
\]

can formalize an empirically testable notion of affective dynamical inertia.

**Status:** **Disclosed as a coherent model family; human applicability UNVERIFIED.**

**Important qualification:** \(M\) is not literal physical mass. It is a phenomenological second-order term.

**Falsifier:** matched-capacity first-order/generic state-space models equal or beat it on holdout.

---

## C-009 — Positive-pulse sign reversal separates one underdamped candidate from the matched first-order toy

**Claim.** In the branch's deterministic synthetic parameterization, a strictly nonnegative forcing pulse produces no post-pulse sign reversal in the first-order model but does produce sign reversal in the underdamped model.

**Status:** **Observed in the executed finite toy.**

**Run:** \`stickman_dynamics_demo.py\` on 2026-09-26.

**Recorded values:**

- 7/7 checks passed;
- overdamped peak \(0.2163016047\);
- overdamped post-pulse minimum \(7.14063\times10^{-5}\);
- inertial peak \(0.3508772102\);
- inertial post-pulse minimum \(-0.2361654441\);
- first inertial zero-crossing after pulse: \(t=2.106\).

**Boundary:** synthetic numerical witness only. No human inference.

---

## C-010 — Human affect has a useful inertial term

**Claim.** Real affective trajectories are better represented with a second-order inertial term than with an overdamped or matched-capacity generic state-space rival.

**Status:** **UNVERIFIED.**

**Pass:** reproducible holdout gain and a discriminating dynamical signature after controlling delayed forcing, measurement lag, and hidden slow state.

**Fail:** first-order or generic state-space model matches/exceeds predictive performance.

**Ambiguous:** models remain observationally equivalent at available sampling/noise.

---

## C-011 — A minimal population-stable Stickman state exists

**Claim.** A low-dimensional state representation can preserve coarse response distributions across multiple human populations for a useful context family.

**Status:** **UNVERIFIED.**

**Pass:** shared structural model transports across populations with only limited parameter adaptation and low residual population information.

**Fail:** population/cultural/semantic variables remain load-bearing even after biological/context controls.

---

## C-012 — Population invariance should mean conditional structural invariance, not identical parameters

**Claim.** A core response is population-stable when population identity adds little predictive information once biologically relevant state and substrate-relevant context are controlled.

Candidate criterion:

\[
I(R;P\mid X_{\mathrm{bio}},c)\approx0.
\]

**Status:** **Conjectured operational definition.**

**Reason:** permits normal threshold/gain variation while making universality testable.

**Debt:** choose a concrete estimator and tolerance before data inspection.

---

## C-013 — Colloquial common sense can be defined as a modal response with abstention

**Claim.** For a declared reference population \(P\), context \(c\), response vocabulary \(\mathcal R\), and predeclared dominance margin \(\delta_{\mathrm{CS}}\), common sense can be operationalized as the modal response only when the top-vs-runner-up gap exceeds the margin; otherwise return \(\bot\).

**Status:** **Disclosed as a definition.**

**Boundary:** this is not a claim that ordinary language users consciously compute population statistics.

**Benefit:** forbids the model from hallucinating consensus in genuinely multimodal cases.

---

## C-014 — A substantial fraction of colloquial common sense is substrate-affective rather than reflective

**Claim.** Many ordinary "obvious" responses are the linguistic shadow of population-stable attractors/flows in substrate-mediated affective dynamics before mature Mode B.

**Status:** **Conjectured / load-bearing empirical thesis.**

**Pass:** base Stickman predicts held-out coarse responses across a broad context family and reflective features add little gain.

**Fail:** predictive performance collapses outside trivial reflexes or depends heavily on explicit semantic/reflexive variables.

---

## C-015 — Reflex and interoceptive domains are appropriate calibration tiers

**Claim.** Nociceptive withdrawal, startle/orienting, air hunger, sleep pressure, and other interoceptive regulation paradigms are useful initial domains because they provide strong substrate coupling with less need for rich social semantics.

**Status:** **Corroborated as a research-design choice by established external literatures; exact Stickman mapping UNVERIFIED.**

**Support:** see \`SOURCES_AND_PRIOR_ART.md\`.

---

## C-016 — Social "common sense" can remain inside base Stickman

**Claim.** Some primitive social responses, such as reaction to abrupt boundary invasion or protection of a strongly routed attachment target, may be predicted without reflective planning.

**Status:** **UNVERIFIED.**

**Risk:** this is where cultural learning, semantic framing, relationship models, and explicit expectation can become load-bearing.

**Rule:** do not promote Tier-3 social findings from Tier-0/Tier-2 success.

---

## C-017 — \(\mathbf{Stoch}\) is a useful categorical representation

**Claim.** Context-conditioned Stickman evolution can be represented as Markov kernels

\[
K_{\Delta t}^c:\mathcal Q_{\mathrm{SM}}\rightsquigarrow\mathcal Q_{\mathrm{SM}}
\]

with behavioral readout kernels, allowing sequential context composition and transport/invariance tests.

**Status:** **Disclosed as a valid mathematical representation; incremental explanatory payoff Conjectured.**

**Failure condition:** categorical language adds no useful composition, invariant, or test beyond ordinary state-space notation.

---

## C-018 — StickmanPlus should add projection incrementally

**Claim.** The first extensions should be one-step action→outcome prediction (Stickman+1) and then one additional composition (Stickman+2), not immediate import of full agency.

**Status:** **Conjectured model-development discipline.**

**Pass:** each extension enters only after a documented base-model residual and produces held-out gain.

---

## C-019 — Generic prediction is not automatically Mode B

**Claim.** TLICA's Mode B should remain reserved for reflexive meta-reasoning/self-structure operation; one-step world-outcome prediction need not be called Mode B.

**Status:** **Disclosed by current TLICA term definition.**

**Reason:** protects the architecture from semantic drift.

---

## C-020 — No current novelty claim

**Claim.** Stickman is not presently established as novel relative to control-theoretic models of allostasis/interoception, dynamical affect models, active inference, appraisal dynamics, action-tendency theories, or computational ethology.

**Status:** **UNVERIFIED novelty; no claim made.**

**Required before promotion:** primary-source rival tomography identifying what, if anything, is uniquely added by the TLICA/Differentiated-Affect quotient-and-common-sense construction.

---

## Verdict-changing probes, in order

1. **Real dynamic dataset:** obtain one human Tier-0/Tier-1 time-series dataset with known forcing onset/offset.
2. **Four-rival fit:** direct stimulus→response; overdamped Stickman; inertial Stickman; matched-capacity generic state-space.
3. **Holdout:** do not use fitted examples as validation.
4. **Residual analysis:** identify what the best simple model misses.
5. **Transport:** test a second substrate domain before adding social semantics.
6. **Population test:** hierarchical shared-structure model with residual population-information check.
7. **Only then StickmanPlus:** add +1 projection against frozen base residuals.

---

## Current overall status

The **formal research object is coherent and cold-startable**.

The main empirical thesis remains **UNVERIFIED**.

The Lagrangian candidate is **not privileged** over the overdamped null.

The toy has paid only one small piece of truth debt: it demonstrates that the proposed inertia question has a concrete, falsifiable dynamical signature in at least one controlled construction.
