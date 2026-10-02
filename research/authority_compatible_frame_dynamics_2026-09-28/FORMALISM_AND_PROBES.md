# Formalism and probe plan

**Status:** candidate application formalism  
**Empirical state:** UNVERIFIED  
**Rule:** no scalar "bootlicking score"; no person-level diagnosis

## 1. Minimal state

Let:

- \(W_t\): environment / institution state available at time \(t\);
- \(S_{i,t}\): agent \(i\)'s self-state and integrated profile;
- \(M_{i,t}\): the agent's predictive model of the authority relation;
- \(V_{i,t}(x\mid S,C)\): candidate valence attached to represented content \(x\);
- \(O_{i,t}(z\mid W,S,V)\): salience / observation kernel mapping available world-information to live represented input \(z\);
- \(\pi_{i,t}(a\mid z,S)\): action policy;
- \(G\): environment transition map under actions of agents and institutions.

Candidate loop:

\[
z_t\sim O_t(\cdot\mid W_t,S_t,V_t),
\]

\[
a_t\sim\pi_t(\cdot\mid z_t,S_t),
\]

\[
W_{t+1}=G(W_t,a_t,a^{-i}_t),
\]

\[
S_{t+1}=U(S_t,z_t,a_t,W_{t+1}),
\]

with osmotic / repeated-co-occurrence updates allowed to alter later salience or valence without requiring explicit reflective assent.

No equation above is claimed as a frozen TLICA law. It is an application-level scaffold for making the hypotheses testable.

## 2. Four diagnostic axes

Use the vector

\[
B_i=(s_i,i_i,r_i,e_i).
\]

### Scope \(s\)

How broadly authority-compatible routing generalizes across contexts.

Discriminator: change authority, domain, or incentive structure.

### Internalization \(i\)

Persistence of endorsement when immediate coercive pressure is removed.

Discriminator: threat-removal and anonymity conditions.

### Positive self-resonance \(r\)

Whether authority-compatible self-perceptions / interpretations carry positive self-valence above matched alternatives.

Discriminator: separate felt/physiological/choice-level valence from explicit normative endorsement.

### Externalization \(e\)

Tendency to impose the frame on peers or newcomers.

Discriminator: give an option to refrain from peer-enforcement at no personal cost.

These coordinates are intentionally non-collapsed. High \(e\) with low \(r\) could reflect material incentives; high \(r\) with low \(e\) could reflect private identification without enforcement.

## 3. Constraint reification

Observed local predictive relation:

\[
P(H\mid a,S_t)\approx1.
\]

Strong reified claim:

\[
\forall S\in\mathcal R(S_t),\quad P(H\mid a,S)\approx1,
\]

where \(\mathcal R(S_t)\) is a relevant reachable-state family.

Probe requirement: vary only the structural state while holding the action description fixed. If participants update when credible alternative regimes are shown, reification is weaker than if they continue to treat the relation as invariant.

## 4. Foreseeability laundering

Define:

- \(F\): target foresaw consequence;
- \(D\): imposing actor had discretion;
- \(L\): legitimacy / warrant information;
- \(R_T\): responsibility attributed to target;
- \(R_J\): responsibility attributed to imposing actor.

A minimal complete factorial probe should vary all cells of:

\[
F\in\{0,1\},\quad D\in\{0,1\},\quad L\in\{0,1\}.
\]

The hypothesis is not "foreseeability should never matter." It is:

> conditional on discretion and legitimacy information, some observers will transfer more responsibility from \(J\) to the target than can be explained by causal contribution alone, with "you knew" functioning as a bridge.

Predeclare target patterns before data collection.

## 5. Slack and feasible resistance

\[
\mathcal A_i^{\mathrm{feas}}(t)
=
\{a:C_i(a;S_t,\mathcal D_i)\le L_i(t)\},
\]

where \(\mathcal D_i\) includes dependents or coupled obligations.

The key discrimination:

\[
\mathcal A_i^{\mathrm{feas}}\text{ small}
\]

versus

\[
\forall a,\;\Delta(a)=0.
\]

Probe: hold system perturbability fixed, vary the participant's personal slack. Ask separately:

1. "Could this action alter any relevant state variable?"
2. "Could this person reasonably afford the action?"

The theory predicts these judgments can dissociate.

## 6. Resistance-visibility vector

\[
\Delta(a)
=
(\Delta_M,\Delta_C,\Delta_I,\Delta_K,\Delta_R)
\]

for:

- \(M\): immediate macrostate;
- \(C\): enforcement/resource cost;
- \(I\): information revealed or recorded;
- \(K\): coordination / coalition structure;
- \(R\): future reachability / option set.

Probe: construct cases with \(\Delta_M=0\) but one other component nonzero and explicitly stated.

If observers still call the action literally causally null, resistance-visibility error is supported.

Mutation control: set every component to zero. This must reduce "it changed something" responses or the instrument is not discriminating.

## 7. Captured fairness

Two judgment objects:

\[
F_{\mathrm{within}}=F(P\mid R),
\]

\[
F_{\mathrm{meta}}=F(P,R).
\]

Complete factorial:

- rule legitimacy: warranted / arbitrary;
- prior cost paid by observer: yes / no;
- newcomer avoids cost: principled resistance / selfish exemption;
- outcome: succeeds / fails.

Do not omit cells.

Primary discriminator: whether prior personal payment specifically raises punitive judgment toward a principled successful resistor under an arbitrary rule.

If the effect disappears once rule-legitimacy and motive are explicit, "information deletion" is a stronger account than sunk-suffering identity defense.

## 8. Retrospective necessity

Candidate mediator:

\[
\text{past cost}
\rightarrow
\text{necessity belief}
\rightarrow
\text{punitive response to counterexample}.
\]

Rival:

\[
\text{past cost}
\rightarrow
\text{fairness preference}
\rightarrow
\text{punitive response}.
\]

Probe by separately measuring:

- "Was the cost necessary?"
- "Was the cost fair?"
- "Did the resister behave selfishly?"
- "Does their success change how you interpret your own past choice?"

If necessity belief does not mediate the effect, retrospective necessity should be weakened.

## 9. Survival emulation versus internalization

Construct matched scenarios where the authority threat is:

1. active;
2. removed;
3. replaced by a new authority with opposite norms;
4. absent under anonymity.

Predictions:

- **survival emulator:** compliance tracks threat and drops under removal;
- **internalized frame:** normative endorsement persists after threat removal;
- **cross-context attractor:** authority-compatible relation recreates under changed authority objects;
- **material enforcer rival:** externalization collapses when reward for enforcement disappears.

## 10. Positive self-resonance probe

This is the most important and most underdetermined component.

Do not equate self-report liking with substrate valence.

Use convergent channels where feasible:

- rapid approach/avoidance choice;
- attention allocation;
- memory/retention;
- explicit felt rightness / relief / pride / belonging;
- behavioral willingness to protect the frame;
- optionally physiological measures if a competent empirical collaboration exists.

Core test:

Does frame-consistent positive valence predict later selective attention or enforcement **after controlling for material incentives, explicit ideology, perceived threat, and status reward**?

If not, the positive self-resonance mechanism adds little.

## 11. Valence-weighted sampling

Developmental / longitudinal candidate:

\[
V_t
\rightarrow
O_{t+1}
\rightarrow
z_{t+1}
\rightarrow
U
\rightarrow
V_{t+2}.
\]

A cross-sectional correlation cannot establish this loop.

Strong probe requires temporal ordering or intervention.

Possible design:

1. baseline salience map;
2. controlled repeated co-occurrence pairing authority-compatible cues with positive or negative outcomes;
3. held-out salience / memory test;
4. later judgment task using novel authority cases;
5. deconditioning / reversal block.

Positive control: a neutral conditioning relation known to shift salience in the chosen paradigm.

Negative control: unrelated content matched for frequency.

Null control: repeated exposure without valence pairing.

Mutation control: reverse the valence pairing.

## 12. Self-confirming domination equilibrium

Agent-level micro-rule candidate:

\[
E_t[\text{persistence}]
\uparrow
\Rightarrow
P(\text{low-perturbation action})\uparrow.
\]

Institution-level transition:

\[
P(\text{persistence at }t+1)
\uparrow
\text{ as perturbation falls}.
\]

This alone can yield a fixed point without assuming anyone falsely predicts the current regime.

Synthetic-world probe first.

Build an agent-based toy system with:

- authority enforcement strength;
- heterogeneous slack;
- belief updating;
- optional peer enforcement;
- optional positive self-resonance;
- perturbation thresholds.

Compare regimes:

A. material incentives only;  
B. incentives + belief reification;  
C. B + peer enforcement;  
D. C + self-resonance update.

The formal result to seek is not "hierarchy always persists." It is a parameter map showing when each extra mechanism changes basin size, hysteresis, or recovery after threat removal.

## 13. Strong falsifiers

The paper should be substantially revised if:

1. endorsement reliably disappears with threat removal across the proposed internalization cases;
2. prior suffering does not predict captured-fairness effects after motive and legitimacy are controlled;
3. observers naturally distinguish local unaffordability from global causal impotence;
4. non-macro resistance effects are recognized without difficulty;
5. positive self-valence has no incremental relation to attention, retention, or enforcement;
6. an established rival construct predicts all target dissociations without the new terminology;
7. authority-compatible patterns do not transfer across contexts once material incentives are removed.

## 14. Claim discipline

No human data have been run.

No literature novelty claim has been earned.

No TLICA coordinate is being added.

The formalism is useful only insofar as it produces discriminating probes.
