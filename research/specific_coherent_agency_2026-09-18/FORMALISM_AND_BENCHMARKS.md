# Formalism and Benchmarks
## Specific Coherent Agency — research apparatus v0.1.0

This file isolates the mathematical and experimental proposal from the prose manuscript. Every scalar is provisional. The vector records and raw episode data are primary.

# 1. Object and comparison boundary

A benchmark instance is

\[
B=(\mathcal E,\mathcal A,\mathcal O,H,K,\Lambda),
\]

where:

- \(\mathcal E\): interactive environment/dynamics;
- \(\mathcal A\): admissible action interface;
- \(\mathcal O\): observation interface;
- \(H\): horizon;
- \(K\): declared task, safety, and invariant constraints;
- \(\Lambda\): preregistered scoring/weighting rules.

Comparisons are meaningful only within an explicitly related benchmark family.

# 2. Episode state

For participant \(m\) at time \(t\):

\[
Z^m_t=(S^m_t,F^m_t,M^m_t,O^m_t,A^m_t,H^m_t),
\]

with:

- \(S\): measured self-relevant commitment/ownership profile;
- \(F\): reported felt-state features relevant to the task;
- \(M\): explicit task/world model;
- \(O\): received observations;
- \(A\): currently represented action/options;
- \(H\): episode history.

No claim is made that this is a sufficient Markov state.

# 3. Primary profile

For each completed benchmark family report:

\[
\mathbf Q_m=(E,M,D,R,X,C,S,O).
\]

Each coordinate requires a separately specified estimator.

## 3.1 Epistemic calibration \(E\)

Use a proper scoring rule on preregistered probabilistic predictions where possible. Report calibration error and discrimination separately rather than only a combined score.

## 3.2 Model fidelity \(M\)

Score prospective predictions of observations and intervention consequences on held-out episodes.

## 3.3 Rival discrimination \(D\)

Maintain an explicit rival set. Reward probes that split live rivals; penalize tests whose outcomes are equally predicted by all surviving models.

A candidate normalized information-gain term:

\[
D_t=
\frac{
H(R_t)-\mathbb E[H(R_{t+1})]
}{
\operatorname{cost}(a_t)
},
\]

only when a probability model over rivals is justified. Otherwise use set elimination and pair-splitting counts rather than pseudo-probabilities.

## 3.4 Reachability \(R\)

Given actual environment dynamics and admissible actions, compare represented routes with real reachable sets where the task permits exact computation.

Track separately:

- named options;
- represented admissible options;
- actually reachable options;
- requirement-satisfying reachable options.

## 3.5 Execution \(X\)

Conditional on selecting an admissible action, measure reliable implementation, timing, and deviation.

## 3.6 Correction \(C\)

Measure whether a residual produces an update that improves held-out predictions relative to:

- no update;
- random update;
- complexity-matched alternative update;
- benchmark-provided minimal correction.

## 3.7 Self-resonance \(S\)

Before the critical action, record invariants/commitments the participant intends to preserve. After the episode, score:

- objective constraint preservation where operational;
- participant endorsement;
- ownership;
- unplanned commitment loss;
- whether the invariant itself was revised with recorded reasons.

Do not equate reported comfort with resonance.

## 3.8 Option preservation \(O\)

Quantify avoidable destruction of future admissible/relevant routes. In finite environments this may be exact:

\[
O_t=
\frac{
|\mathrm{Reach}_{H-t}(x_{t+1})\cap K|
}{
|\mathrm{Reach}_{H-t}(x_t)\cap K|
}
\]

with care: maximizing this ratio globally can itself prevent necessary commitment. Use it as a diagnostic, not a universal objective.

# 4. Coherent reachability

Define

\[
\mathcal R^\star_{m,H}
=
\left\{
z\in\mathrm{Reach}_{m,H}:
Q_E(z)\ge e_0,
Q_C(z)\ge c_0,
Q_S(z)\ge s_0,
C_z\preceq B
\right\}.
\]

All thresholds must be fixed before comparison.

A benchmark value functional may be:

\[
\mathcal V_B
=
\sum_z w_B(z)
P_{\rm reach}(z)
Q_E(z)
Q_C(z)
Q_S(z)
Q_O(z).
\]

Alternative: avoid multiplicative collapse and retain the Pareto frontier over the five terms. The scalar is allowed only when the decision rule needs one and weights are declared.

# 5. Self-dimension

The normalization problem is the most fragile part of the proposal.

Let \(v_{m,j}\) be a feature vector of self-relevant responses across contexts \(j\). Build a preregistered covariance/kernel matrix after controlling measurement noise.

Candidate effective dimensions:

### Shannon effective rank

\[
d_H=\exp\!\left(-\sum_i p_i\log p_i\right).
\]

### Participation ratio

\[
d_2=\frac{1}{\sum_i p_i^2}.
\]

### Predictive minimum dimension

\[
d_{\min}(\alpha)=
\min\{k:
\text{a }k\text{-dimensional model predicts held-out self-relevant choices at }\ge\alpha
\}.
\]

The predictive minimum dimension is conceptually closest to the intended denominator but hardest to estimate without model dependence.

## 5.1 Adequacy gate

No denominator is valid unless its representation predicts held-out ownership/commitment behavior above a declared adequacy floor.

This blocks the trivial strategy "model the person as one number, get denominator 1."

# 6. Candidate SCA scalar

\[
\eta_m(B,H)
=
\frac{
\log(1+\mathcal V_B)
}{
d_{\rm self}
}.
\]

Required report:

\[
\left(
\mathbf Q_m,
\mathcal V_B,
d_{\rm self},
\eta_m,
\mathrm{CI/uncertainty}
\right).
\]

Never report \(\eta\) alone.

# 7. Update fidelity

For each model revision event:

\[
\epsilon^{\rm pre}_t
=
d_Y(\hat Y^{\rm pre},Y),
\qquad
\epsilon^{\rm post}_{t,k}
=
d_Y(\hat Y^{\rm post},Y)
\]

on held-out perturbation \(k\).

Define raw improvement

\[
\Delta\epsilon_t
=
\epsilon^{\rm pre}_t
-
\mathbb E_k[\epsilon^{\rm post}_{t,k}].
\]

Correction is useful only when held-out improvement is positive beyond controls.

Candidate update-quality vector:

\[
\mathbf U_t=
(
\Delta\epsilon,
\Delta D,
\Delta R,
\text{provenance retention},
\text{invariant retention},
\text{update cost}
).
\]

Again, a scalar is secondary.

# 8. Relational-rightness probe

The phenomenological hypothesis is:

> Some strongly felt convictions attach to a tracked relation among feeling, model, and world-coupling rather than to the current proposition; therefore proposition replacement can coexist with continuity of the tracked commitment.

This can become self-sealing unless probed prospectively.

## 8.1 Prediction

Participants who genuinely track the relation should outperform a proposition-protective rival on held-out transformations after an object-level model is falsified.

## 8.2 Four-way outcome classification

1. **Relational tracking supported:** explicit model changes; held-out transport/prediction error falls; provenance retained.
2. **Proposition protection:** model resists decisive residual; error remains.
3. **Narrative relabeling:** model changes, but no held-out improvement; continuity is only retrospective description.
4. **Random flexibility:** frequent changes without systematic residual reduction.

# 9. Benchmark family A — finite causal worlds

Use small unfamiliar deterministic/stochastic environments where the experimenter knows the transition graph.

Properties:

- hidden state or partial observability;
- multiple rival models;
- interventions with unequal information value;
- dead-end actions;
- reversible and irreversible actions;
- misleading local correlations;
- at least one indirect/slingshot route;
- states where waiting is optimal.

Advantages: exact reachable sets and ground-truth causal consequences are available.

# 10. Benchmark family B — rule-changing systems

Participants learn an initial rule, then encounter controlled shifts.

Cross:

- change detection;
- alternative-action availability.

This reproduces the existing TLICA traversability distinction between information and executable control.

Measure whether behavior changes among participants who have already detected the mismatch once an executable route is made available.

# 11. Benchmark family C — self-constraint worlds

Before play, participants choose or are assigned stable constraints with meaningful tradeoffs.

Examples:

- preserve a scarce resource;
- avoid sacrificing a protected token/entity;
- maintain truth-reporting despite reward pressure;
- preserve exit reachability.

Then measure whether successful planning honors the declared invariant rather than only maximizing terminal reward.

This is a benchmark analogue of self-resonant actualization, not a claim that game preferences equal real identity.

# 12. Controls

Every serious benchmark should include:

- **positive control:** a simple environment where competent adaptation should succeed;
- **negative control:** an impossible target under the action graph;
- **null control:** extra observation that carries no decision-relevant information;
- **mutation control:** one changed edge/action that flips reachability;
- **provenance control:** misleading but fluent explanation versus correct causal prediction;
- **holdout:** unseen transition regimes;
- **complexity control:** richer models that fit training data but should not beat simpler rivals out of sample;
- **self-normalization mutation:** duplicate/redundant self-features should not inflate effective self-dimension proportionally.

# 13. Comparator measures

To earn usefulness, SCA should be compared against simpler alternatives:

- standard fluid-reasoning measure;
- working-memory measure;
- probabilistic calibration score;
- planning/search performance;
- reinforcement-learning adaptation slope;
- metacognitive calibration;
- executive-function task measures;
- personality/motivation measures where ethically appropriate.

The key question is incremental prediction, not conceptual novelty.

# 14. Cross-person fairness hazards

A benchmark can be contaminated by:

- prior domain familiarity;
- language;
- motor speed;
- disability;
- economic/resource assumptions;
- cultural preference encoding;
- differential trust in experimenters;
- unequal incentive salience;
- fatigue/sleep;
- interface accessibility.

The environment should be as content-light and instrumented as possible, and reports should distinguish person capacity from access/environment limitation.

# 15. No universal leaderboard

Even if the scalar becomes reliable, it should remain benchmark-indexed:

\[
\eta_m(B,H),
\]

not \(\eta_m\) simpliciter.

A broad estimate would require a preregistered mixture distribution over benchmark families and an explicit population/use-case definition.

# 16. First implementation target

A minimal software prototype can use graph worlds with:

- 8–20 states;
- hidden transition rules;
- finite action costs;
- one irreversible trap;
- one option-preserving detour;
- probe actions;
- multiple reward/invariant configurations;
- train/holdout world seeds.

Log every observation, prediction, action, model update, confidence, and invariant declaration.

The first goal is not to measure people. It is to validate the **scoring algebra** on synthetic agents with known policies:

- oracle;
- greedy reward maximizer;
- random agent;
- fixed wrong model;
- Bayesian-like updater;
- over-correcting model switcher;
- option-preserving planner.

If the metrics cannot distinguish these controlled policies in the expected directions, human use is premature.
