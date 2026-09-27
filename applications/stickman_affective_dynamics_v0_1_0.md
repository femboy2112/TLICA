# Stickman: Affective Mechanics and the Substrate Derivation of Colloquial Common Sense

## A minimal TLICA application built from Differentiated Affect

**Status:** application-paper candidate, research branch draft v0.1.0 — **UNREGISTERED**  
**Date:** 2026-09-26  
**Branch:** \`research/stickman-affective-dynamics-2026-09-26\`  
**Foundation:** TLICA v5.5.2 on branch base \`90cf753c6088f21dfe1e8732398ba97896bee263\` — **untouched**  
**Primary donor application:** [Differentiated Affect v1.0.2](differentiated_affect_v1_0_2.md)  
**Supporting foundation:** [Formal Apparatus, especially §§8.1–8.10](../foundation/3_formal_apparatus.md) and [Open Problems §13.3](../foundation/5_translations_open_problems_conclusion.md)  
**Research support package:** [research/stickman_affective_dynamics_2026-09-26/](../research/stickman_affective_dynamics_2026-09-26/)  
**Epistemic posture:** the formal constructions below are explicit model proposals. No human behavioral dataset has yet been fit. No cross-population invariance has yet been demonstrated. No novelty claim is made.

---

## Abstract

This paper proposes **Stickman**, a deliberately minimal application-level model of a human being whose job is not to represent personality, deliberation, moral reasoning, long-horizon planning, or reflective agency. Stickman keeps only the substrate-mediated affective dynamics needed to answer a narrower question:

> Given a minimally specified living human substrate and a context that couples to it, what coarse response-shape should occur most often across ordinary human populations?

The proposal runs the logic of TLICA's *Differentiated Affect* application backward. That paper classifies affects as structural configurations of the lived I and its operators: embodied perturbation, preservation threat, boundary operation, constitutive extension and loss, reflexive evaluation, salience, focus, and action-readiness. The current foundation separately supplies substrate mediation, first- and third-order pathways, osmotic imprinting, and a driven relaxational dynamics for the occupied baseline. What is missing is an application-level **equation of motion connecting context-induced affective perturbation to coarse behavior**. Stickman occupies exactly that gap.

The paper therefore defines a task-relative affective state space \(\mathcal Q_{\mathrm{SM}}\), context forcing \(u_c(t)\), an observation map to coarse response classes \(\mathcal R\), and two rival dynamical families. The conservative null is an overdamped stochastic gradient flow,

\[
\Gamma(q)\dot q
=
-\nabla_q V(q;c)
+
B(q)u_c(t)
+
\Sigma(q)\xi(t).
\]

The stronger candidate is a dissipative Lagrangian system with Rayleigh dissipation,

\[
\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}
-
\frac{\partial L}{\partial q_i}
+
\frac{\partial \mathcal D}{\partial \dot q_i}
=
Q_i(c,t)+\Xi_i(t),
\]

where

\[
L(q,\dot q;c)
=
\frac12\dot q^\top M(q)\dot q
-
V(q;c),
\qquad
\mathcal D
=
\frac12\dot q^\top \Gamma(q)\dot q.
\]

The inertial term \(M\) is **not assumed**. It must earn its keep against the overdamped null. The branch includes an executable finite witness showing one clean discriminator: after a positive forcing pulse ends, an underdamped second-order model can overshoot and reverse sign, while the matched first-order relaxation cannot. This is a construction-level discriminator, not evidence that human affect actually has mechanical inertia.

Behavior is a coarse projection of the resulting trajectory. For a reference population distribution over admissible parameterizations, colloquial common sense is defined as the modal response class only when the response distribution has sufficient dominance margin. Cross-population "invariance" is likewise operationalized rather than assumed: population identity should add little predictive information after substrate state and substrate-relevant context are conditioned upon.

Stickman excludes Mode B, slack, explicit option construction, explicit reasons, and rich world-model deliberation. A later **StickmanPlus** may add weak one-step and possibly two-step projected-action models if they provide genuine held-out predictive gain. The intended research question is therefore not "can biology explain all behavior?" but:

> **How much ordinary colloquial common sense is the linguistic shadow of population-stable attractors in substrate-mediated affective dynamics, before reflective agency is added?**

---

## 1. The object

### 1.1 What Stickman is

Stickman is a deliberately lossy model of a living human substrate. It is defined relative to a declared response task \(T\).

Let \(\mathcal H\) be the set of complete human microstates relevant in principle to the task, and let

\[
\mathrm{Resp}_T :
\mathcal H \times \mathcal C_T
\rightsquigarrow
\mathcal R_T
\]

be the stochastic response map from full human state and context to coarse response morphology.

Define response-equivalence

\[
h_1 \sim_T h_2
\iff
\mathrm{Resp}_T(h_1,c)
=
\mathrm{Resp}_T(h_2,c)
\quad
\text{for all declared } c\in\mathcal C_T,
\]

or, empirically, equality up to a declared tolerance and divergence measure.

Then the ideal minimal object is the quotient

\[
\mathsf{Stickman}_T
=
\mathcal H / {\sim_T}.
\]

This is a **target definition**, not a claim that the correct quotient has already been identified. It supplies the criterion for every proposed state variable: a variable earns a place only if removing it destroys response-equivalence on a discriminating context family.

### 1.2 What Stickman is not

Stickman is not:

- a miniature rational agent;
- a utility maximizer;
- a theory of moral judgment;
- a personality model;
- a language model;
- a rich predictive world-model;
- a model of explicit reasons;
- a model of reflective self-intervention;
- a model of slack;
- a model of mature Mode B.

The shortest governing sentence is:

> **Stickman is pushed before it chooses.**

A context perturbs the substrate. Substrate-mediated affective state changes. Action-readiness changes. Coarse behavior follows from the resulting trajectory.

### 1.3 The application boundary

This paper is application-level. It does **not** add a foundation coordinate, rewrite the three TLICA coordinates, alter the meaning of Mode A/B/C, or claim that the foundation already entails a particular differential equation.

The foundation fixes dependencies but leaves many empirical transfer functions open. *Differentiated Affect* supplies a structural taxonomy. Stickman proposes one family of dynamical completions and lets experiment decide whether they are useful.

---

## 2. Why Differentiated Affect is the donor theory

*Differentiated Affect* already makes the move Stickman needs: emotions are not primitive labels but configurations generated by structural operations on the lived I.

Its affect criterion is broad: affective configurations perturb salience, action-readiness, profile stability, PCE, PtCns, focus, or related structural variables. It then organizes affect into five clusters:

1. **connection / extension**;
2. **self / reflexive evaluation**;
3. **threat / preservation**;
4. **boundary / encounter**;
5. **embodied / somatic**.

Stickman does not import the entire taxonomy. It asks which parts remain available after reflective machinery is intentionally removed.

### 2.1 Primitive candidate subspace

The first candidate projection is

\[
\pi_{\mathrm{SM}} :
\mathcal A_{\mathrm{DA}}
\to
\mathcal A_{\mathrm{primitive}},
\]

with

\[
\mathcal A_{\mathrm{primitive}}
\subseteq
\{
\text{embodied},
\text{threat},
\text{boundary},
\text{primitive extension/attachment}
\}.
\]

This inclusion is **Conjectured**, not settled.

The self/reflexive cluster is initially excluded because guilt, shame, self-loathing, articulated embarrassment, and many future-directed affects can require self-modeling or learned semantic structure that Stickman is specifically designed not to contain.

Parts of the connection, threat, and boundary clusters may also fail the minimality test. For example, "jealousy" may require a relational model richer than Stickman; acute protective orientation toward an attached other may not. The partition must be earned experimentally.

### 2.2 The key bridge: action-readiness

The foundation already states that somatic substrate processing preserves features including intensity, valence, **action-tendency**, and broad affective tone while losing propositional detail.

That observation is the bridge from affect taxonomy to mechanics.

Instead of reading

\[
\text{fear} = \text{emotion label},
\]

Stickman asks whether a fear-like configuration can be represented as a region of state space whose flow field biases the organism toward a family of coarse actions.

Similarly, anger-like boundary activation becomes a deformation of response-readiness, not a dictionary entry.

---

## 3. Substrate state and context

### 3.1 State

Let

\[
q(t)\in\mathcal Q_{\mathrm{SM}}
\]

be Stickman's fast affective/substrate state.

At v0.1.0 the paper refuses to canonize a coordinate chart for \(\mathcal Q_{\mathrm{SM}}\). Candidate local coordinates may track coarse embodied disequilibrium, preservation-threat activation, boundary/differentiation pressure, primitive extension-disruption, orienting/salience capture, or other empirically separable components.

This refusal is deliberate. Naming five psychologically attractive axes and declaring them minimal would defeat the project. Coordinate choice is a model-selection problem.

### 3.2 Slow parameters

Let

\[
\theta
\]

collect slower parameters: gains, damping, thresholds, coupling coefficients, learned substrate associations, developmental state, and other features that remain fixed over the timescale of one response episode.

\(\theta\) is not personality in disguise. It is the parameterization needed to represent ordinary biological variation without promoting each variation to a new state variable.

### 3.3 Context as forcing, not instruction

The physical/social world is richer than Stickman. Let \(w(t)\) denote world state and

\[
\Pi_{\mathrm{perc}} :
w(t)
\mapsto
c(t)
\]

be the upstream perceptual/context map.

Stickman receives \(c(t)\), not raw reality.

The distinction is load-bearing. If a complicated social scene is pre-labeled "dangerous," Stickman is allowed to model what **perceived danger** does to the substrate. It does not thereby explain how the scene was classified as dangerous.

The context then induces generalized forcing

\[
u_c(t)=U(c(t),\theta)
\]

or directly

\[
Q(q,c,t).
\]

No response is encoded in the context label itself. "Perceived threat" may create forcing on several affective degrees of freedom; the behavioral result depends on the system state, coupling, and dynamics.

---

## 4. The conservative dynamical null: overdamped flow

The simplest useful dynamics should win unless a stronger model out-predicts it.

The first candidate is therefore a dissipative first-order stochastic system:

\[
\Gamma(q;\theta)\dot q
=
-\nabla_q V(q;c,\theta)
+
B(q;\theta)u_c(t)
+
\Sigma(q;\theta)\xi(t).
\]

Interpretation:

- \(V\) is an application-level affective/regulatory potential;
- \(\Gamma\) is positive dissipation/resistance;
- \(B u_c\) is context-induced forcing;
- \(\xi(t)\) is stochastic biological variation;
- \(\Sigma\) maps that variation into state coordinates.

This is deliberately close in spirit to the current foundation's relaxational baseline law

\[
\dot b = \gamma(f-b),
\]

without identifying Stickman's \(q\) with foundation \(b\), \(f\), or \(\rho\).

### 4.1 Why this is the null

The current TLICA dynamics already shows that a living substrate can be treated as a driven dissipative system that relaxes toward a moving field-reading. Nothing in Stickman's motivating insight requires true second-order inertia.

If a first-order flow predicts the data just as well, the Lagrangian machinery is unnecessary and should be removed.

### 4.2 Response basins

Let

\[
\mathcal B
=
\{B_1,\ldots,B_n\}
\]

be empirically declared response basins in trajectory space: withdrawal, orienting, defensive blocking, approach, rest-seeking, elimination-seeking, affiliative repair, freezing, and so on.

A readout

\[
\chi_c :
\mathcal T(\mathcal Q_{\mathrm{SM}})
\to
\mathcal R
\]

maps a state trajectory under context \(c\) to a coarse response class.

The map is context-sensitive: the same internal magnitude can issue in different motor acts depending on what affordances the environment makes physically available.

---

## 5. The stronger candidate: dissipative Lagrangian affective mechanics

The user's motivating conjecture is that affect may have enough persistence, directional carry, and state-dependent resistance to warrant an equation-of-motion treatment analogous to mechanics.

The weakest serious version is not a conservative Lagrangian but **Lagrange–d'Alembert with Rayleigh dissipation**.

Define

\[
L(q,\dot q;c,\theta)
=
T(q,\dot q;\theta)
-
V(q;c,\theta),
\]

with

\[
T
=
\frac12 \dot q^\top M(q;\theta)\dot q,
\]

and dissipation

\[
\mathcal D(q,\dot q;\theta)
=
\frac12 \dot q^\top \Gamma(q;\theta)\dot q.
\]

Then

\[
\frac{d}{dt}
\frac{\partial L}{\partial \dot q_i}
-
\frac{\partial L}{\partial q_i}
+
\frac{\partial \mathcal D}{\partial \dot q_i}
=
Q_i(q,c,t;\theta)
+
\Xi_i(t).
\]

For constant matrices and quadratic potential this reduces to

\[
M\ddot q
+
\Gamma\dot q
+
Kq
=
Bu_c(t)
+
\Xi(t).
\]

### 5.1 What "mass" means here

\(M\) is **not** literal kilograms and is not assumed to be a physical conserved inertia.

It is a phenomenological dynamical parameter representing any empirically necessary second-order persistence that cannot be captured adequately by a first-order Markov state of the chosen dimension.

That qualification is essential because every second-order system can be written as a first-order system on an enlarged state \((q,\dot q)\). The scientific question is therefore not metaphysical:

> "Does emotion literally possess mass?"

It is predictive:

> **Does an inertial coordinate provide a lower-complexity or better-generalizing representation of affective trajectories than an overdamped state model with matched capacity?**

### 5.2 The overdamped limit

The stronger family contains the conservative null as a limiting regime. When inertial effects are negligible relative to damping,

\[
M\ddot q \approx 0,
\]

so

\[
\Gamma\dot q
=
-Kq
+
Bu_c.
\]

This nesting is useful: Stickman need not decide in advance whether the Lagrangian analogy survives.

---

## 6. A discriminating signature for affective inertia

The branch includes an executable construction-level demonstration in

\`research/stickman_affective_dynamics_2026-09-26/stickman_dynamics_demo.py\`.

Consider a one-dimensional positive forcing pulse

\[
u(t)
=
\begin{cases}
1,&0\le t<1,\\
0,&t\ge1.
\end{cases}
\]

Matched stable first-order dynamics,

\[
\Gamma\dot q + Kq = u(t),
\]

approach a positive displaced state during the pulse and monotonically relax toward zero afterward. Starting from \(q(0)=0\), the trajectory does not cross through zero after a purely positive pulse.

An underdamped second-order candidate,

\[
M\ddot q+\Gamma\dot q+Kq=u(t),
\]

can overshoot after the forcing is removed and cross to the opposite side before settling.

That yields a precommitted discriminator:

- **PASS for an inertial contribution:** after controlling for delayed external forcing, hidden state, measurement lag, and sign-changing input, human affect trajectories exhibit reproducible overshoot/phase-lag structure that the fitted first-order rival cannot reproduce at matched predictive complexity.
- **FAIL:** the first-order rival fits holdouts equally well or better; post-pulse persistence is absorbed by slow hidden state without a useful inertial term.
- **AMBIGUOUS:** both families predict the measured observable within uncertainty, or measurement cannot distinguish latent forcing from state persistence.

A finite toy can demonstrate that the discriminator exists. It cannot establish which family humans instantiate.

---

## 7. Common sense as a population-level projection of flow

For a parameterized Stickman instance \(\theta\), initial state \(q_0\), and context \(c\), let

\[
\tau_{\theta,q_0,c}
\]

be the resulting trajectory and

\[
R_{\theta,q_0,c}
=
\chi_c(\tau_{\theta,q_0,c})
\]

its coarse response.

Let \(\mu_P(\theta,q_0)\) be the distribution of admissible Stickman parameters and starting states in reference population \(P\).

Then

\[
P_P(r\mid c)
=
\int
\mathbf 1\{
R_{\theta,q_0,c}=r
\}
\,d\mu_P(\theta,q_0)
\]

for deterministic per-instance dynamics, with the obvious Markov-kernel generalization for stochastic trajectories.

Define colloquial common sense only when the top response has sufficient dominance:

\[
r_1
=
\operatorname*{arg\,max}_{r\in\mathcal R}
P_P(r\mid c),
\]

\[
\Delta(c,P)
=
P_P(r_1\mid c)
-
\max_{r\ne r_1}P_P(r\mid c).
\]

For a declared threshold \(\delta_{\mathrm{CS}}>0\),

\[
\mathrm{CS}_P(c)
=
\begin{cases}
r_1,&\Delta(c,P)\ge\delta_{\mathrm{CS}},\\
\bot,&\text{otherwise}.
\end{cases}
\]

\(\bot\) means **no dominant common-sense response**.

This is important. The model must be able to say that ordinary humans genuinely divide.

---

## 8. Population invariance without pretending humans are identical

"Population invariant" must not mean identical response probabilities in every demographic, culture, age band, or physiological state.

The stronger and more defensible target is **conditional structural invariance**.

For populations \(P_i,P_j\), context family \(\mathcal C^\star\), and response divergence \(D\),

\[
D\big(
P_{P_i}(R\mid X_{\mathrm{bio}},c),
P_{P_j}(R\mid X_{\mathrm{bio}},c)
\big)
\le
\epsilon
\]

after conditioning on declared biologically relevant state and measurement covariates.

Equivalent information-theoretic language:

\[
I(R;P
\mid
X_{\mathrm{bio}},c)
\approx 0.
\]

This gives a real admission rule.

A response family belongs in **core Stickman** only if population label adds little held-out predictive information once substrate state and substrate-relevant context are known.

If population membership remains strongly predictive, the effect is not discarded; it simply belongs outside the population-invariant core.

### 8.1 Hierarchical form

A practical statistical implementation should be hierarchical:

\[
\theta_n
\sim
\Theta_{P(n)},
\]

with shared structural equations and population-specific parameter distributions.

The test is whether a shared structure with parameter variation explains the data, not whether every person has the same threshold.

---

## 9. Categorical form: Stickman in \(\mathbf{Stoch}\)

The stochastic formulation has a natural categorical home.

Let \(\mathbf{Stoch}\) be a category whose objects are measurable state spaces and whose morphisms are Markov kernels.

For each context segment \(c\), Stickman supplies a transition kernel

\[
K_{\Delta t}^{c}
:
\mathcal Q_{\mathrm{SM}}
\rightsquigarrow
\mathcal Q_{\mathrm{SM}}.
\]

Sequential exposure composes:

\[
K^{c_2}_{\Delta t_2}
\circ
K^{c_1}_{\Delta t_1}.
\]

Let

\[
H_c :
\mathcal Q_{\mathrm{SM}}
\rightsquigarrow
\mathcal R
\]

be the coarse behavioral readout and \(\mu_0\) an initial-state distribution. Then the response distribution is the composite

\[
\mu_0
\xrightarrow{K^c}
\mathcal Q_{\mathrm{SM}}
\xrightarrow{H_c}
\mathcal R.
\]

The differential equation or SDE is one generator of these kernels; the categorical object need not care whether the underlying implementation is a gradient flow, Lagrange–d'Alembert system, neural simulation, or empirical transition matrix.

This separation is valuable:

- **mechanics** asks what generates \(K\);
- **category-level composition** asks how context-conditioned transitions compose;
- **common sense** is a population-level statistic on the resulting response distribution.

### 9.1 Context morphisms as invariance probes

Suppose a context transformation

\[
f:c\to c'
\]

changes a feature claimed irrelevant to substrate response. Then an invariance claim predicts approximately commuting response structure:

\[
H_{c'}K^{c'}
\approx
H_cK^c
\]

after the corresponding transport.

Failure is informative. Either the transformation was not irrelevant, the state representation omitted a load-bearing variable, or the response quotient was too coarse.

---

## 10. Candidate scope ladder

Stickman should begin where the substrate signal is strongest and move outward only after passing held-out probes.

### Tier 0 — reflex arcs and immediate protective responses

Candidate examples:

- nociceptive withdrawal;
- blink/startle-related protection;
- postural correction;
- orienting toward sudden salient stimuli.

These cases are useful calibration because substantial response structure can occur without reflective choice.

### Tier 1 — interoceptive regulation

Candidate examples:

- air hunger and breathing urgency;
- hunger/satiety-driven approach;
- thirst;
- thermoregulatory behavior;
- sleep pressure and rest-seeking;
- bladder/bowel urgency and elimination-seeking.

These should establish whether the model can derive coarse "obvious" behavior from bodily disequilibrium plus available affordances.

### Tier 2 — acute defensive affect

Candidate examples:

- imminent perceived threat;
- looming collision;
- invasion of peripersonal space;
- acute pain;
- sudden loss of stability.

### Tier 3 — primitive social-affective coupling

Candidate examples:

- abrupt boundary violation;
- proximity threat;
- protective response toward a strongly routed attachment target;
- simple affiliative repair after visible distress.

This tier is where the program becomes theoretically interesting and empirically dangerous to overclaim. Success in Tiers 0–2 does not license Tier 3.

### Tier 4 — explicitly excluded from base Stickman

Initially excluded:

- articulated guilt/shame;
- complex jealousy;
- explicit norm reasoning;
- strategic deception;
- reputation management;
- long-horizon planning;
- counterfactual self-narrative;
- moral justification.

These require richer representational structure and are candidates for StickmanPlus or beyond.

---

## 11. StickmanPlus: add the smallest predictive model that earns itself

StickmanPlus is not "Stickman plus all of agency."

### 11.1 Stickman+1

Add a one-step action-outcome model

\[
a_t
\mapsto
\widehat o_{t+1}.
\]

This permits minimal projected consequence without requiring a recursive self-model.

Example shape:

\[
\text{move away}
\mapsto
\widehat{\text{threat decreases}}.
\]

### 11.2 Stickman+2

If +1 survives, allow one further composition:

\[
a_t
\mapsto
\widehat o_{t+1}
\mapsto
\widehat r_{t+1}.
\]

This may capture simple interpersonal anticipation or two-step action selection.

### 11.3 Mode B boundary

TLICA's Mode B is reflexive meta-reasoning: the I taking its own structure as object. Do not relabel all prediction as Mode B.

StickmanPlus crosses into genuine Mode-B territory only when the model explicitly represents and operates on its own response-generating structure, e.g.

\[
\text{"why am I being pulled toward this response?"}
\]

or applies a self-directed reweighting to that structure.

### 11.4 No slack in base Stickman

Base Stickman contains no slack variable. Fatigue, sleep deprivation, hunger, pain, and other substrate conditions may change trajectories directly.

If a later StickmanPlus requires a control-budget variable to predict reflective override, that belongs in the added agency layer, not in the biological core.

---

## 12. How common sense would be "derived backward" from Differentiated Affect

The phrase can now be made exact.

The forward presentation of *Differentiated Affect* is approximately:

\[
\text{TLICA structure}
\to
\text{affect configuration}
\to
\text{named affect family}.
\]

Stickman asks for a reverse operational program:

\[
\text{context}
\to
\text{structural perturbation}
\to
\text{affective trajectory}
\to
\text{action-readiness}
\to
\text{response basin}
\to
\text{colloquial gloss}.
\]

The final gloss is not part of the organismal dynamics. It is our linguistic compression of the modal trajectory.

For example:

\[
\text{noxious heat}
\to
\text{embodied threat forcing}
\to
\text{withdrawal-oriented state trajectory}
\to
B_{\mathrm{withdraw}}
\]

is later glossed as

> "Obviously, pull your hand away."

Similarly, if the social tiers work,

\[
\text{acute boundary invasion}
\to
\text{boundary/threat forcing}
\to
\text{defensive affective trajectory}
\to
B_{\mathrm{withdraw/defend}}
\]

may underwrite part of what ordinary speakers call an "obvious reaction."

The empirical content lies in the middle arrows, not the colloquial phrase.

---

## 13. Relation to current TLICA open problems

Stickman directly targets several already-declared application debts.

### 13.1 Action-priority dynamics under pressure

The foundation currently identifies third-order activation, future-state projection, and substrate urgency as contributors but does not formalize how they combine into action priority.

Stickman deliberately begins with the **substrate-only slice**. It asks how far that slice goes before future-state projection is needed.

### 13.2 Mixed-pathway dynamics

The foundation notes that real contents often combine first-, second-, and third-order pathways and leaves their interaction open.

Base Stickman starts with first- and third-order dominant cases. StickmanPlus is a controlled way to add second-order contributions rather than importing them all at once.

### 13.3 Compression characteristics

The foundation says somatic processing preserves some features while losing propositional structure but leaves component-specific compression open.

Stickman's state-identification program can test which coarse variables are actually sufficient to preserve response signatures.

---

## 14. Falsification program

The project fails usefully if any of the following occurs.

### F1 — No stable minimal quotient

If response prediction requires an ever-expanding list of semantic/cultural/personality variables even in nominally primitive contexts, the "Stickman" compression is not useful.

### F2 — Population invariance fails

If population label remains strongly predictive after substrate state and context controls, a purported core response must be demoted from Stickman to population-specific structure.

### F3 — Affect variables add no predictive value

If direct stimulus→response models equal or beat affective-state models on held-out data, Differentiated Affect is not earning its place as the dynamical intermediary for this task.

### F4 — Lagrangian inertia loses

If overdamped or generic state-space models predict trajectories as well as the inertial model at lower complexity, set \(M=0\) and drop the mechanical-inertia reading.

### F5 — Response basins are post-hoc labels

Response classes must be frozen before holdout evaluation. If every trajectory gets a custom "basin" after observation, the model explains nothing.

### F6 — Context parser does all the work

If \(\Pi_{\mathrm{perc}}\) must already encode "what the person will do" rather than substrate-relevant features, Stickman is a renamed lookup table.

### F7 — Social extension fails

The project may succeed for reflex/interoceptive contexts and fail for social "common sense." That outcome is acceptable and would locate the boundary where richer cognition becomes necessary.

---

## 15. Minimum empirical program

### Stage A — calibration on established low-level responses

Fit simple response dynamics to existing laboratory paradigms with clear substrate coupling:

- nociceptive withdrawal;
- looming/peripersonal defense;
- startle/orienting;
- respiratory air hunger;
- sleep-loss modulation;
- hunger/thirst/elimination where usable datasets exist.

Goal: establish whether the formalism can recover known coarse regularities without semantic tricks.

### Stage B — model comparison

For each domain compare at least:

1. direct stimulus→response baseline;
2. first-order overdamped Stickman;
3. second-order dissipative Stickman;
4. generic state-space rival with comparable capacity.

Use held-out prediction, not fit quality alone.

### Stage C — cross-population transport

Fit hierarchical shared-structure models and test whether population-specific parameters suffice.

Predeclare what counts as practical invariance.

### Stage D — social boundary cases

Only after A–C, move into carefully bounded non-harmful social contexts.

Do not infer universality from convenience samples.

### Stage E — StickmanPlus

Add +1 projected outcome only where base Stickman fails in a systematic, discriminating way.

---

## 16. Claim ledger summary

The detailed ledger lives in the support package. The load-bearing statuses at v0.1.0 are:

- **Disclosed from repository text:** Differentiated Affect treats affect as structural configuration and includes action-readiness; foundation provides substrate mediation and driven dissipative dynamics; action-priority dynamics are explicitly open application work.
- **Derived inside the proposed mathematics:** the overdamped model is a limiting/null form of the second-order linear candidate; Markov transition kernels compose categorically; a response quotient can be defined relative to a declared task.
- **Observed in the finite toy only:** a chosen underdamped system shows post-pulse sign reversal while its matched first-order relaxation does not.
- **Conjectured / UNVERIFIED:** human affect requires inertial terms; a stable cross-population Stickman quotient exists; broad colloquial common sense can be recovered from it; primitive social responses remain inside the substrate-only closure.

No stronger status is licensed.

---

## 17. What would count as success

The strongest defensible success is not "we derived human nature."

It is a bounded result of the form:

> For context family \(\mathcal C^\star\) and response vocabulary \(\mathcal R^\star\), a shared low-dimensional substrate-affect dynamical model predicts coarse response distributions across held-out human samples with little residual population information, and richer reflective variables do not materially improve prediction.

Then "common sense" has a precise local meaning:

> the modal coarse response under that declared substrate/context family.

The ambitious extension would show that the same machinery continues to explain increasingly social cases before explicit reflective agency becomes necessary.

---

## 18. Conclusion

Stickman is the proposed **equation-of-motion layer of Differentiated Affect**.

It removes the parts of TLICA most likely to hide explanatory slack — rich Mode B, explicit reasons, long-horizon agency — and asks what remains when a context pushes a living substrate.

The core research ladder is:

\[
\text{world}
\to
\text{perceived substrate-relevant context}
\to
\text{affective forcing}
\to
\text{Stickman dynamics}
\to
\text{response basin}
\to
\text{population distribution}
\to
\text{colloquial common sense}.
\]

The mechanics must remain weaker than the evidence. The first-order dissipative model is the null. The Lagrangian form is a stronger candidate with an explicit discriminator. Population invariance is a measured transport property, not an intuition. Social extension is a target, not an assumption.

If the program works, a surprising amount of "what any normal person would obviously do" may turn out not to be a library of propositions at all.

It may be the linguistic shadow cast by a very small dynamical animal.
