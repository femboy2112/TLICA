# Formalism — typed candidate models, not empirical laws

**Status:** conditional derivations and conceptual models. Empirical parameterizations, psychological mechanisms, and social findings **UNVERIFIED**. These constructions are *not* incorporated into TLICA's foundation.

## 0. Type discipline, observation maps, and prohibitions

Work with separate sorts:
- \(I\): indexed conscious participants/individual agents (if they exist in the target model);
- \(X\): social/environmental world states, including institutions, material constraints, and records;
- \(O_i\): accessible observations for agent \(i\);
- \(A_i(x)\): actions actually feasible for \(i\) at state \(x\);
- \(F_i\): agent's representation/frame of her situation, *not* identical to \(X\);
- \(N\): normative judgments/constraints; these are not physical observables;
- \(Y\): measured outcomes;
- \(K_i\): knowledge/toolkit/source map; \(P_i\): action policy or controller.

Declared observation map: \(h_i:X\to O_i\). Framing map \(f_i:O_i\times K_i\to F_i\). Feasible policy \(\pi_i:F_i\to A_i\), with context-appropriate selection. Actual material effects are mediated through dynamics \(\mathcal T:X\times \prod_i A_i\times W\to X\), where \(W\) represents exogenous disturbances.

**Forbidden inferences:** high TLICA \(\varphi\) does not certify ground truth; \(\sigma\) source-map adequacy is separately tested; agreement across agents with shared inputs is not independent verification; attractive quantum/thermodynamic metaphors do not transport physics; reading of one speaker's mental state from a facial expression is not a validated observation channel.

## 1. Non-entailment of survival-consent and enforcement-legitimacy

Propositions:
- \(P(x)\): actor participates in regime \(x\);
- \(C(x)\): actor has voluntarily endorsed regime \(x\);
- \(E(x)\): regime can enforce its rule;
- \(L(x)\): rule is legitimate;
- \(F(x)\): refusing the regime has a materially feasible exit.

Neither \(P\Rightarrow C\) nor \(E\Rightarrow L\) holds *as a matter of propositional logic* unless an additional bridge premise is supplied. Witness models exist with \(P=E=1\) and \(C=L=0\). This is an elementary semantic countervaluation, not proof that an actual law is illegitimate.

Even if the actor freely endorses some duty at \(t_0\), \(C(t_0)\) does not imply \(C(t_1)\). The enforceability of revocation varies across the kind of obligation. There is no universal right to withdraw from all duties to others merely by asserting non-consent.

## 2. The cost-to-necessity fallacy

Let \(c_i^*(x,g)\) denote the minimal verified cost for individual \(i\), under currently constructible tools and routes, to attain goal \(g\) from state \(x\), and \(b_i(x)\) their available budget/slack. \(c_i^*>b_i\) licenses "not viable for this individual by the available route."

It does **not** imply:
\[
\neg\exists\,\text{coalition/alternative route to }g;
\qquad
\neg\Diamond g;
\qquad
L(x).
\]

Even when *no* path exists in the explicitly modeled closure, it says nothing about paths outside that closure. Tool relative \(\varphi\), feasible reachability, and source-map adequacy \(\sigma\) must not collapse to one score.

## 3. Local moral practices and typed cross-scale transport

Let \(X_s,X_t\) be fine and coarse state spaces and \(A_s,A_t\) their feasible action spaces, with coarse maps \(C_X:X_s\to X_t\) and \(C_A:A_s\to A_t\). Let policies \(\pi_s:X_s\to A_s\) and \(\pi_t:X_t\to A_t\).

A *typed* scale-compatibility diagram asks when:
\[
C_A\circ\pi_s\;\approx\;\pi_t\circ C_X.
\]

Approximation must be defined through a task outcome metric \(d\) on \(A_t\), or downstream state effects; different scales can have distinct legitimate action spaces. Exact equality is not generally expected.

The original conversational shorthand \(C\circ P_s\approx P_t\circ C\) suppressed state/action type differences. Treat the typed version as a **repair**, not a derived moral theorem.

### Local gluing analogue

For a cover \(U_i\) of social contexts, local commitments \(s_i\in\mathcal F(U_i)\) could satisfy overlap conditions \(s_i|_{U_i\cap U_j}=s_j|_{U_i\cap U_j}\). **But:** this only gives sheaf-theoretic gluing if \(\mathcal F\) is specified as a sheaf with restriction maps and a gluing axiom. No actual human-ethics sheaf or nontrivial obstruction class was constructed during the conversation.

A concrete falsification target: an implementation that preserves the words "dignity" in each locale while a policy imposes contradictory treatment at their interface.

## 4. Robust ethics under disturbance: policy existence and viability

Let \(E\subseteq X\) be acceptable system states under a chosen normative guard (which may be partial rather than a complete ethical characterization). Evolution:
\[
x_{t+1}=F(x_t,u_t,w_t),\qquad u_t\in U(x_t),\quad w_t\in W(x_t).
\]

A one-step robust controlled-invariance condition is:
\[
\forall x\in E,\quad\exists u\in U(x)\quad\forall w\in W(x):
F(x,u,w)\in E.
\]

The quantifier order means the action is selected *before* the disturbance is known. If agents observe \(w\) before acting, the weaker \(\forall w\,\exists u\) condition may be appropriate; don't exchange them silently.

A failure of this condition means the *specified* guard \(E\) cannot be guaranteed under the *specified* disturbances and controls. It does not refute the dignity principle or establish inevitability of moral harm in every other feasible system.

Distinguish:
- invariant as normative constraint ("do not treat another as worthless");
- state guard ("no state with deprivation");
- controller success ("all disturbances contained");
- recovery protocol (after a failure, detect, report, repair, and adjust).

A morally serious controller may fail to preserve an absolute guard while remaining accountable through an honest correction policy. **Repair duties do not logically license prior wrongdoing.**

## 5. The prisoner's dilemma and second-order bootstrap

Two-player illustrative prisoner's dilemma, payoffs (row actor, column actor):

| | Other cooperates | Other defects |
|---|---:|---:|
| Cooperate | (3,3) | (0,5) |
| Defect | (5,0) | (1,1) |

Defect strictly dominates cooperation; mutual cooperation Pareto-dominates mutual defection. These numbers are *chosen*, not a measurement of society.

Now let a costly public institution \(J\) increase cooperative payoffs and/or reduce downside risk, but formation of \(J\) requires a threshold coalition \(k\) or funded collective action. Let contributions \(a_i\in\{0,1\}\), cost \(c_i>0\), and institution formation \(J(a)=1\{\sum_i a_i\ge k\}\). A contributor's payoff:
\[
u_i(a)= B_i J(a)-c_i a_i-\ell_i(a).
\]

When benefits are nonexcludable, each individual may prefer others to cover cost \(c_i\): a second-order public-goods/free-rider problem. Whether there is an actual prisoner's dilemma, threshold game, coordination game, or dynamic path depends on \((B_i,c_i,\ell_i,k)\). No uniform result was derived.

**Research objective:** find a credible, feasible sequence of commitments \(a^0,a^1,\ldots,a^n\) where every required participant's cost is within their actual slack at the moment they must act, and final \(J\) reduces those costs. If none is found, classify pathway-gap vs genuine resource/policy boundary without pretending the latter has been proved.

### Institutions change the future game

Let \(G_t=G(x_t)\) denote the payoff game produced by institutional state \(x_t\):
\[
x_{t+1}=F(x_t,a_1,\ldots,a_n),\qquad G_{t+1}=G(x_{t+1}).
\]
Actions may alter the game for later participants; this does *not* imply that doing so is always available or morally justified.

## 6. Existential habitability as a distribution-sensitive measure

Let \(\mu\) be an explicitly chosen distribution over possible initial endowments/positions \(x_0\), **not** a canonical metaphysical random distribution. Let \(\Pi_i\) be a feasible policy family for a bounded-information actor \(i\), and \(\tau\) a finite or discounted lifetime horizon. Define a *vector* of experienced costs:
\[
\mathbf c_i = (c_{\rm survival},c_{\rm rule\ discovery},c_{\rm coercion},
c_{\rm lost\ agency},c_{\rm error\ penalty},c_{\rm preventable\ harm}).
\]

For any declared ethical weights \(\mathbf w\), one possible scalar summary is:
\[
H_{\mathbf w}(S;\mu,\Pi)
=\mathbb E_{x_0\sim\mu}\Big[\inf_{\pi\in\Pi(x_0)}
\sum_{t=0}^{\tau}\gamma^t\,\mathbf w\cdot\mathbf c_i(x_t,\pi_t)\Big].
\]

**Caveats:**
1. An infimum over an *omniscient* policy would conceal the very no-manual problem; constrain \(\Pi\) to what the entrant can discover/access.
2. Mean cost can hide exclusion, catastrophic tails, exploitation, and population disappearance. Report distribution, conditional-group outcomes, upper quantiles, and excluded/missing populations.
3. The chosen \(\mu,\mathbf w,\Pi,\gamma\) carry ethical commitments and cannot be learned without normative judgment.
4. A perfectly legible dictatorship could have low discovery cost but high coercion and lost autonomy.
5. Death is not zero ongoing cost; survival-conditioned measurements require explicit censoring and a separate mortality/exposure variable.

The metric is a **research target**, not a validated moral score.

## 7. Distinguish moral debt from physical entropy

The conversational illustrative balance:
\[
\dot D(t)=P_{\rm harm}(t)-R_{\rm repair}(t)
\]
can define an *accounting identity* for chosen rates, if units and boundaries match. It does not imply \(\dot D\ge0\). Harms and repairs need definitions, lags, interaction terms, and distributional attribution.

Thermodynamic entropy is a physical state quantity with a microphysical basis and regime-specific second-law formulations; the analogy with societal moral debt makes a *logical warning* against inferring global improvement from local examples. It does not import a second law of social immorality.

## 8. Population selection and the denominator problem

Let community \(i\) have population \(N_i(t)\), assigned institutional habitability/moral score \(m_i(t)\) (whose meaning must be separately defended), total \(N=\sum_i N_i\), weights \(p_i=N_i/N\), and population growth rate \(r_i=\dot N_i/N_i\).

Population-weighted mean:
\[
\bar m=\sum_i p_i m_i.
\]

Then the identity:
\[
\boxed{\dot{\bar m}=\sum_i p_i\dot m_i+\operatorname{Cov}_{p}(m_i,r_i).}
\]

**Derivation:** \(\dot p_i=p_i(r_i-\bar r)\) where \(\bar r=\sum_i p_i r_i\). Substitute into \(\frac{d}{dt}\sum_i p_i m_i\).

Thus \(\dot{\bar m}>0\) is possible even when \(\dot m_i\le0\) for all surviving groups if high-scoring groups grow relatively faster, or lower-scoring groups die/disappear from observation. A toy: equal-sized groups score 0.8 and 0.2 → mean 0.5; if the latter disappears without change in the former, observed mean becomes 0.8. **The event may be a catastrophe, not progress.**

Boundary: demographic growth also depends on fertility, migration, integration, and cohort effects; \(m_i\) is not necessarily heritable, and no moral-selection law follows. A group that exercises domination could have greater reproductive/political success while being less hospitable to members.

## 9. Distributed harm is not additive by decree

For interventions \(d_1,\ldots,d_n\) (policies, institutional choices, exposures), an outcome functional \(H(d_1,\ldots,d_n)\) can include interactions. In a complete factorial with baseline \(\mathbf 0\), the Möbius/inclusion–exclusion interaction for coalition \(S\) is:
\[
\Delta_S H=\sum_{T\subseteq S}(-1)^{|S|-|T|}\,H(\mathbf1_T).
\]

A real claim of a specific high-order mixed term requires **all relevant counterfactual cells or a justified estimand/model**. A poetically effective phrase about "a thousand dominoes" does not measure those interaction terms.

For sequential cascades, use a structural causal model with documented time, affected individuals, institutional levers, and intervention alternatives. Diffuse causation may frustrate attribution; it neither proves guilt for everyone upstream nor exonerates every distal participant.

## 10. Institutional identity and accountability surface

Following the existing distributed-institutional TLICA research, let micro-realization \(z=(P,R,D)\) include people/roles, typed authority-relations, and artifacts. For task family \(\mathcal Q\) define:
\[
z\sim_{\mathcal Q}z' \iff \forall q\in\mathcal Q,\ \mathrm{Response}(z,q)=\mathrm{Response}(z',q).
\]
The institution is a response-equivalence class *relative to its task family*, not an emergent sentient person.

For accountability, extend task probes to include:
- ability to cause outcomes;
- ability to notice/respond to harms;
- authority to redesign dangerous interfaces;
- capacity to retain/search incident provenance;
- availability of independent external challenge.

The central hypothesis is **asymmetry between a broad action surface and a narrow acknowledged responsibility surface**. This is testable organizationally; one must not assert a literal global mind, magical downward causation, or automatic organizational guilt.

## 11. Referent routing versus representational integrity

Existing TLICA source: *The Cold Frame and Its Sources* separates:
- \(T(v)\): modeled representation of victim/other \(v\);
- \(R_\lambda(T(v);c)\): uptake into agent's operative evaluative/affective frame under coupling/context \(c\).

Candidate moral disengagement decomposition:
\[
\mathrm{Act}=
\pi\Big(F_{\rm self},\
R_\lambda(T(v);c),\
d_{\rm duty},\
d_{\rm outcome},\
U(x)\Big).
\]

Two agents can have similarly accurate \(T(v)\) but different routing/context or policy; a third can have distorted \(T(v)\) with intact routing. The same outward harm is *not* diagnostic of any one path.

**Testable difference:** hold comprehension of victim's material harm constant, vary role label and responsibility frame; compare judgments/actions. Use strong comprehension and duty-equivalence controls before inferring a routing contribution.

**Boundary:** Bandura's moral disengagement framework is independent prior art; an analogy does not demonstrate unique TLICA dynamics or specify an individual person's mental state.

## 12. What the models currently prove, and what they don't

**Conditional/elementary:** Non-entailment of compliance → endorsement; type-consistent transport equation; robust-control criterion as definition; Price selection identity; PD strict-dominance with chosen numbers; Möbius finite decomposition for fully specified factorial values.

**Not established:** a global moral invariant's unique content, a physically meaningful "moral entropy," an empirically measured social gauge group, moral-debt trends, prevalence of specific routing mechanisms in elites, universal superiority of one social system, inevitability of revolution, or any general causal claim about a particular contemporary person without event-level evidence.

**Required next step:** explicit observables and rival predictions with source-independent holdouts. See [PROBES_AND_HANDOFF.md](PROBES_AND_HANDOFF.md).
