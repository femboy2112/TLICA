# Formalism and Probe Plan — Stickman Affective Dynamics

**Companion to:** [application draft](../../applications/stickman_affective_dynamics_v0_1_0.md)  
**Status:** research support; all empirical model-selection claims UNVERIFIED unless explicitly marked.

---

## 1. Research object

Let

- \(\mathcal W\): world-state space;
- \(\mathcal C\): substrate-relevant perceived-context space;
- \(\mathcal Q\): candidate Stickman state space;
- \(\Theta\): parameter space;
- \(\mathcal R\): coarse response space.

The full factorization is

\[
\mathcal W
\xrightarrow{\Pi_{\mathrm{perc}}}
\mathcal C
\xrightarrow{\mathcal F}
\text{forcing on }\mathcal Q
\xrightarrow{\mathrm{Flow}_{\theta}}
\mathcal T(\mathcal Q)
\xrightarrow{\chi}
\mathcal R.
\]

Do not collapse these arrows casually.

The project fails if \(\Pi_{\mathrm{perc}}\) has to encode the downstream answer.

---

## 2. Minimality as response-equivalence

For declared task \(T=(\mathcal C_T,\mathcal R_T)\), define full-state response signature

\[
\Sigma_T(h)
=
\left(
P(R\mid h,c)
\right)_{c\in\mathcal C_T}.
\]

Exact task-equivalence is

\[
h_1\sim_T h_2
\iff
\Sigma_T(h_1)=\Sigma_T(h_2).
\]

Then

\[
\mathsf{Stickman}_T=\mathcal H/{\sim_T}.
\]

This quotient is formal and exact.

### Approximate data case

For empirical response distributions define

\[
d_T(h_1,h_2)
=
\sup_{c\in\mathcal C_T}
D(
P(R\mid h_1,c),
P(R\mid h_2,c)
),
\]

for a declared divergence \(D\).

Do **not** automatically define

\[
h_1\sim_{\epsilon}h_2
\iff d_T(h_1,h_2)\le\epsilon
\]

and then quotient: thresholded metric similarity is generally not transitive.

Use one of:

- explicit transitive closure, with information-loss audit;
- clustering with declared linkage;
- covering families;
- predictive sufficient statistics;
- latent-state identification by held-out likelihood.

The exact quotient remains the conceptual target.

---

## 3. Candidate dynamical families

### M0 — direct baseline

No latent affective state:

\[
P(R_t\mid c_{0:t},x_0).
\]

Implement with the simplest domain-appropriate baseline.

Purpose: test whether Stickman state earns any predictive work.

### M1 — first-order overdamped Stickman

\[
\Gamma(q;\theta)\dot q
=
-\nabla_q V(q;c,\theta)
+
B(q;\theta)u_c(t)
+
\Sigma(q;\theta)\xi(t).
\]

Linear local form:

\[
\Gamma\dot q+Kq=Bu(t)+\Sigma\xi(t).
\]

Requirements:

- \(\Gamma\) positive definite or otherwise demonstrably dissipative;
- \(K\) stable in the fitted region;
- forcing measured independently of response where possible.

### M2 — inertial Stickman

\[
M(q;\theta)\ddot q
+
C(q,\dot q;\theta)
+
\Gamma(q;\theta)\dot q
+
\nabla_q V(q;c,\theta)
=
Q(q,c,t;\theta)
+
\Xi(t).
\]

For v0.1.0 tests, start with the linear constant-coefficient special case:

\[
M\ddot q+\Gamma\dot q+Kq=Bu(t).
\]

Do not begin with nonlinear geometry unless the linear residuals demand it.

### M3 — matched-capacity generic state-space rival

For example:

\[
z_{t+1}=Az_t+Bu_t+\epsilon_t,
\qquad
R_t\sim H(z_t).
\]

or an appropriate nonlinear state-space model with capacity matched to M2.

Purpose: distinguish "Lagrangian coordinates are useful" from "you merely needed another latent state."

---

## 4. Why Lagrange–d'Alembert, not naive conservative mechanics

A living affective system is:

- driven;
- dissipative;
- stochastic;
- open;
- often nonstationary.

A conservative action principle alone would be structurally wrong for the motivating domain.

Use

\[
L=T-V,
\]

with nonconservative generalized force \(Q\) and Rayleigh dissipation \(\mathcal D\):

\[
\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}
-
\frac{\partial L}{\partial q_i}
+
\frac{\partial\mathcal D}{\partial\dot q_i}
=
Q_i.
\]

This is an economical way to ask whether a second-order coordinate system earns predictive compression.

It does **not** assert that affect is fundamentally classical mechanics.

---

## 5. Inertia discriminator

### 5.1 Positive-pulse probe

Input:

\[
u(t)=1,\quad 0\le t<T_p,
\]

\[
u(t)=0,\quad t\ge T_p.
\]

Calibrated first-order scalar model:

\[
\Gamma\dot q+Kq=u(t),
\qquad K,\Gamma>0,
\qquad q(0)=0.
\]

For a strictly positive pulse, the solution remains nonnegative and decays monotonically after pulse removal.

Second-order scalar model:

\[
M\ddot q+\Gamma\dot q+Kq=u(t),
\]

with underdamped parameters can cross baseline after removal.

### 5.2 Human-data pass condition

An inertial interpretation earns support only if all are satisfied:

1. forcing offset is independently known;
2. measured or inferred response crosses/overshoots in a reproducible direction;
3. delayed stimulus transduction cannot explain the phase;
4. a slow hidden first-order state does not explain it at equal/lower complexity;
5. M2 improves held-out predictive score over M1 and M3;
6. the effect transports to a second domain or independent dataset.

### 5.3 Failure

If M3 captures the data with equal or better simplicity/generalization, "Lagrangian inertia" has not earned special status.

---

## 6. Response-basin construction

A response vocabulary \(\mathcal R\) must be:

- coarse enough to transport across surface realization;
- fine enough to distinguish meaningfully different action tendencies;
- frozen before holdout scoring.

Candidate Tier-0/Tier-2 classes:

- orient;
- withdraw;
- freeze;
- block/brace;
- approach;
- continue;
- rest-seek;
- intake-seek;
- elimination-seek.

Social classes may later include:

- affiliative approach;
- protective interposition;
- boundary assertion;
- repair.

### Forbidden move

Do not define response classes after inspecting model errors until all errors become "the right basin."

### Preferred operationalization

Use observable motor/choice outcomes when possible. Treat verbal reports as separate outputs, not privileged ground truth for latent affect.

---

## 7. Population-common-sense statistic

For population \(P\),

\[
p_r(c;P)=P_P(R=r\mid c).
\]

Let

\[
r_1=\arg\max_r p_r,
\qquad
r_2=\arg\max_{r\ne r_1}p_r.
\]

Define dominance

\[
\Delta(c;P)=p_{r_1}-p_{r_2}.
\]

Then

\[
\mathrm{CS}_P(c)
=
\begin{cases}
r_1,&\Delta\ge\delta_{\mathrm{CS}},\\
\bot,&\Delta<\delta_{\mathrm{CS}}.
\end{cases}
\]

The threshold \(\delta_{\mathrm{CS}}\) must be fixed for a study before holdout evaluation.

Alternative uncertainty-aware criterion: require posterior probability that \(r_1\) exceeds \(r_2\) by at least \(\delta\) to exceed a precommitted confidence level.

---

## 8. Population transport / invariance

### 8.1 Hierarchical model

Let participant \(n\) belong to population \(P(n)\):

\[
\theta_n
\sim
\mathcal N(\mu_{P(n)},\Sigma_{\mathrm{within}}).
\]

Shared structure means the same equation family and state/readout semantics across populations; parameters may vary.

### 8.2 Invariance metrics

Possible metrics:

- conditional mutual information \(I(R;P\mid X,c)\);
- total variation distance;
- Jensen-Shannon divergence;
- calibration error difference;
- leave-one-population-out log score;
- transport degradation after limited recalibration.

### 8.3 Admission rule

A response pattern enters **core Stickman** only after:

1. within-population fit;
2. leave-one-population-out transport;
3. residual population-information audit;
4. confound check for age, sex, body state, measurement protocol, language demands, and task instructions as appropriate.

"Population invariant" should always be reported with the tested populations and context range.

---

## 9. Context-parser firewall

The parser \(\Pi_{\mathrm{perc}}\) deserves its own probe.

Suppose raw scene \(w\) is mapped to context features

\[
c=(c_1,\ldots,c_k).
\]

For each \(c_i\), ask:

- can it be measured without observing the response?
- is it substrate-relevant rather than action-labelled?
- does an independent annotator/model recover it?
- does a mutation of \(c_i\) predict a change in response?
- does holding \(c_i\) fixed while changing irrelevant scene detail preserve prediction?

Bad context feature:

- "situation requiring withdrawal."

Good candidate feature:

- "looming object trajectory intersects body envelope in <300 ms."

Bad social feature:

- "person is being disrespectful."

Better decomposed candidate:

- loud vocal amplitude;
- close distance;
- directed approach;
- blocked egress;
- prior affiliation;
- observed contact;
- explicit utterance content (kept separate).

The richer the semantics, the more likely the task has moved beyond base Stickman.

---

## 10. Domain probe ladder

### Probe A — nociceptive withdrawal

Goal: calibration.

Inputs:
- stimulus intensity/time course;
- limb/site;
- baseline state.

Outputs:
- reflex EMG latency/amplitude;
- withdrawal occurrence.

Questions:
- does a latent affective state improve prediction beyond reflex mapping?
- probably not; if not, record the failure rather than forcing Stickman in.

This is valuable because M0 may win. A framework that cannot lose is useless.

### Probe B — startle / looming defense

Inputs:
- looming trajectory or acoustic pulse;
- distance/time-to-contact;
- predictability.

Outputs:
- blink/startle;
- duck/block/withdraw;
- reaction latency.

Question:
- does one low-dimensional defensive state transport across modalities?

### Probe C — air hunger

Inputs:
- controlled respiratory load / gas-exchange manipulation where ethically and publicly available;
- stimulus onset/offset.

Outputs:
- urge ratings;
- respiratory effort;
- escape/termination behavior if available.

Question:
- do state dynamics show hysteresis/persistence distinguishable from stimulus lag?

### Probe D — sleep pressure

Sleep loss is slower and should not be forced into a millisecond reflex model.

Question:
- can a slow substrate parameter modulate the same fast response machinery rather than requiring a new response law?

### Probe E — peripersonal intrusion

Question:
- does defensive state predict action across non-social looming and human proximity after controlling semantics?

A positive result would justify moving toward Tier 3.

---

## 11. Affect-coordinate discovery

Do not begin by declaring "fear axis," "anger axis," etc.

### Candidate strategy 1 — response-sufficient latent state

Fit latent states to predict future response under intervention/context changes.

Then test whether discovered dimensions align with TLICA affect operators after fitting.

### Candidate strategy 2 — operator-seeded model

Seed dimensions from:
- embodied disequilibrium;
- preservation threat;
- boundary/differentiation;
- extension disruption;
- orienting/salience.

Then perform structured ablation.

### Required comparison

Let data decide whether operator-seeded coordinates outperform unconstrained latent states in:

- data efficiency;
- transport;
- interpretability;
- held-out likelihood.

If unconstrained state wins decisively, the TLICA-derived coordinates have not earned empirical privilege.

---

## 12. Category-theoretic representation

Use \(\mathbf{Stoch}\), not category language for decoration.

For each context segment \(c\):

\[
K^c_{\Delta t}:Q\rightsquigarrow Q.
\]

Composition:

\[
K^{c_2}_{\Delta t_2}\circ K^{c_1}_{\Delta t_1}.
\]

Readout:

\[
H_c:Q\rightsquigarrow R.
\]

Initial distribution:

\[
\mu_0:1\rightsquigarrow Q.
\]

Response distribution:

\[
1
\xrightarrow{\mu_0}
Q
\xrightarrow{K^c}
Q
\xrightarrow{H_c}
R.
\]

### Categorical payoff tests

The categorical formulation earns its place if it clarifies at least one of:

- composition across context segments;
- coarse-graining/factorization;
- transport along context morphisms;
- sufficient-state quotient;
- equivalence of different micro-dynamics under the same observable response kernel.

Otherwise keep ordinary probabilistic notation.

---

## 13. StickmanPlus residual-driven promotion

Base model must be frozen before adding projection.

### Residual R1
Base Stickman fails specifically when behavior depends on immediate predicted consequence.

Add:

\[
a\mapsto\hat o.
\]

### Residual R2
+1 fails when behavior depends on one response to that projected outcome.

Add:

\[
a\mapsto\hat o\mapsto\hat r.
\]

### Stop rule
Do not add a third layer automatically.

At each step compare:
- held-out gain;
- parameter count;
- transport;
- calibration;
- whether a simpler state augmentation explains the same residual.

---

## 14. Controls

### Positive control
A paradigm with known substrate-responsive dynamics should be predictable.

### Negative control
A task deliberately requiring arbitrary learned semantic convention should defeat base Stickman.

Example shape: response depends on a newly taught arbitrary symbol rule with no substrate-relevant difference.

### Null control
Irrelevant visual/context mutations should not change the predicted response distribution.

### Mutation control
Change one substrate-relevant input while preserving irrelevant surface detail; response should shift in the predicted direction.

### Parser-leak control
Train a response predictor on context features alone; if it perfectly predicts due to label leakage, rebuild the feature set.

---

## 15. Measurement and identifiability warnings

### 15.1 Second-order identifiability
Observed persistence may arise from:

- true second-order dynamics;
- unobserved slow first-order state;
- delayed forcing;
- sensor filtering;
- motor execution delay;
- reporting delay.

Therefore overshoot alone is not sufficient.

### 15.2 Affect label circularity
Do not infer "fear state" from withdrawal and then use fear to explain withdrawal.

Use independent physiological/behavioral measures or latent-state inference with cross-validation.

### 15.3 Population confounding
"Culture" may proxy:
- task comprehension;
- sampling frame;
- age;
- health;
- training;
- language;
- apparatus differences.

Transport claims require source-map discipline.

### 15.4 Time-scale separation
Fast reflex, autonomic adjustment, mood, sleep pressure, and slow imprinting occupy different timescales. A single \(\Gamma\) is unlikely to suffice globally.

Use multiscale state only when data demand it.

---

## 16. Executed construction-level witness

Run:

\`\`\`bash
cd research/stickman_affective_dynamics_2026-09-26
python3 stickman_dynamics_demo.py --output stickman_dynamics_demo_results.json
\`\`\`

Recorded branch-session result:

\`\`\`text
PASS: 7/7 checks
overdamped post-pulse minimum: 0.000071406
inertial post-pulse minimum: -0.236165444
inertial first zero-cross time: 2.106
\`\`\`

Synthetic parameters:

- first-order \(K=4,\Gamma=2\);
- second-order \(M=1,K=4,\Gamma=0.5\);
- \(dt=0.002\);
- positive unit pulse on \([0,1)\);
- horizon \(5\).

This verifies only the code and the existence of the proposed discriminator.

---

## 17. Immediate next experiment specification

**Target:** first real human dynamic dataset with known forcing.

Before fitting, freeze:

1. response variable;
2. forcing variable;
3. train/validation/holdout split;
4. M0/M1/M2/M3 equations;
5. parameter priors/bounds;
6. score (e.g. held-out log likelihood + complexity criterion);
7. overshoot/phase discriminator;
8. pass/fail/ambiguous thresholds.

### Required report

For each model:

- fitted parameters;
- training score;
- validation score;
- holdout score;
- calibration;
- residual autocorrelation;
- posterior/predictive intervals;
- response to forcing-off segments;
- exact preprocessing.

Then perform model criticism before extending the state space.

---

## 18. Promotion criteria for the application paper

Do not register as a mature application merely because the mathematics is elegant.

Minimum promotion evidence:

- at least one real human dynamic dataset;
- one held-out model-comparison result;
- one negative/null control;
- one transport attempt;
- explicit result on whether \(M\) earned itself;
- primary-source comparison to relevant allostasis/interoception/dynamical-affect frameworks;
- author review of the conceptual boundary around Mode B and common sense.

Until then: application-paper candidate, research branch.
