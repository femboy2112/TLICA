# Choice as Endogenous Filter Application

## Perceptual Momentum, Response Leverage, and a Conservative Fidelity Refinement of TLICA Agency

**Status:** Research note / conservative theory refinement, v0.1  
**Branch:** `research/choice-as-filter-perceptual-momentum-2026-08-29`  
**Date:** 2026-08-29  
**Foundation impact:** none. This note adds no foundation primitive, coordinate, causal faculty, or hidden selector. It gives higher-resolution semantics to machinery already present in TLICA: substrate-bound focus, the contact-driven/self-directed focus decomposition, toolkit-relative live-option construction, operator-bundle selection, focus-driven probe weighting, focus/contact-driven imprinting, substrate coupling, order-indexed willing, and compiled transport.  
**Epistemic status:** the conservative mapping to existing TLICA is an internal formal clarification; the phenomenological and empirical claims about perceptual momentum, control depth, correlated-neighborhood amplification, and response leverage remain **CONJECTURED / UNVERIFIED** until discriminating probes are run.

---

## 0. Executive thesis

The central refinement is:

\[
\boxed{
\text{The act of choosing is the endogenous application of a filter to the present field.}
}
\]

This does **not** move choice backward from an action to a second, prior act called “choosing a filter.” There is no extra chooser selecting the filter. The self-directed deformation of focus/perceptual weighting **is the choice-event itself**.

The filter does not select isolated contents for integration or disintegration one by one. It changes the weighting of a currently accessible field of possible understandings, affordances, interpretations, and responses. Because contents are relationally coupled through the lived-I network, toolkit structure, learned co-activation, source-relations, and substrate dynamics, changing the weight of one region changes the activation and update pressure on a correlated neighborhood.

The existing TLICA machinery then performs the downstream work:

\[
\boxed{
\text{chosen filter}
\to
\text{focus allocation}
\to
\text{probe/update weighting}
\to
\text{integration change}
\to
\text{response trajectory}
\to
\text{future field geometry}.
}
\]

The corresponding account of ordinary action is not:

\[
\text{agent selects a discrete motor point}
\to
\text{body executes it}.
\]

It is:

\[
\text{agent endogenously reweights the perceptual/interpretive field}
\to
\text{the substrate follows the newly dominant trajectory to the degree permitted by current resistance}.
\]

The resistance of the current perceptual-substrate trajectory to such reweighting is called **perceptual momentum** in this note. When perceptual momentum is low, a small chosen filter-shift can produce a large bodily response-shift. That is the refined meaning of **first-order willing**.

The note makes six linked claims:

1. **Choice is filter application, not point selection.**
2. **The filter is a parameterization of existing self-directed focus, not a new mechanism.**
3. **The filter acts on correlated regions, while existing TLICA update rules determine particular integrations and disintegrations.**
4. **Discrete live options are coarse equivalence classes of a richer filter space.**
5. **The operative order of willing is minimal control depth, not merely the anatomical or behavioral location of the result.**
6. **The same act can be first-order in control and third-order in bodily realization.**

The old frozen theory remains correct in shape. This refinement fills in missing fidelity.

---

## 1. Exact relation to the frozen architecture

This note should be read with:

- [`foundation/3_formal_apparatus.md`](../foundation/3_formal_apparatus.md), especially substrate-bound focus, the contact-driven/self-directed decomposition, focus-driven probe weighting, focus-driven imprinting, and osmotic imprinting;
- [`applications/free_will_v0_3_0.md`](../applications/free_will_v0_3_0.md), especially the six conditions of free choice;
- [`applications/agency_architecture_v0_3_0.md`](../applications/agency_architecture_v0_3_0.md), especially live-option construction, operator-bundle selection, order-indexed willing, decision-events, timing-marker non-identity, and the variation taxonomy;
- [`applications/this_is_water_truth_respecting_choice_v0_1_0.md`](../applications/this_is_water_truth_respecting_choice_v0_1_0.md), especially micro-periagoge, selection closure, and compiled transport.

The existing foundation already states, schematically,

\[
\mathsf{Foc}^m_t
=
\mathsf{Foc}^m_t[\mathrm{contact\text{-}driven}]
\oplus
\mathsf{Foc}^m_t[\mathrm{self\text{-}directed}],
\]

with the capacity constraint

\[
|\mathsf{Foc}^m_t|\le M_m(t).
\]

It also already fixes the dependency chain

\[
\mathsf{Foc}^m_t
\longrightarrow
\mu^m_t,
\qquad
(\mathsf{Foc}^m_t,\kappa)
\longrightarrow
(\alpha,\beta)
\longrightarrow
w^{m,k}_{t^+}(u,v).
\]

Nothing in the present note changes those dependencies.

### 1.1 What was underspecified

The architecture had the correct structural place for choice—self-directed focus, live-option construction, evaluative engagement, and operator-bundle selection—but did not yet specify with enough fidelity what the inside-perspective act of selection amounts to.

The coarse reading was liable to suggest:

\[
\text{construct discrete options}
\to
\text{select one option}
\to
\text{send an implementation command}.
\]

The refined reading is:

\[
\text{construct a field in which multiple response-trajectories are inhabitable}
\to
\text{endogenously apply a filter to that field}
\to
\text{allow the existing substrate/update dynamics to propagate the deformation}.
\]

The discrete option description remains valid at the macroscopic agency level. It is a quotient description of the finer process, not an error.

### 1.2 No added selector

The following interpretation is explicitly rejected:

\[
\text{I}
\to
\text{choose filter}
\to
\text{apply filter}
\to
\text{choose action}.
\]

That would duplicate choice and install a homuncular regress.

The intended identity is:

\[
\boxed{
\text{choosing the filter}
\equiv
\text{applying the filter}
\equiv
\text{the self-directed component of the present focus deformation}.
}
\]

There is no further choice behind this event within the model.

---

## 2. The conservative-refinement lemma

Let

\[
\mathfrak F^m_t
\]

be the set of self-directed focus allocations already admissible under the frozen architecture at time \(t\), given the modeling I’s substrate, toolkit, phenomenal field, capacity bound, and current state.

Introduce an application-level space of admissible filters

\[
\mathcal F^m_t
\]

and a realization map

\[
\pi^m_t:\mathcal F^m_t\to\mathfrak F^m_t,
\qquad
f\mapsto \mathsf{Foc}^m_t[\mathrm{self\text{-}directed};f].
\]

The filter formalism is a **conservative refinement** exactly when

\[
\boxed{
\operatorname{Im}(\pi^m_t)=\mathfrak F^m_t.
}
\]

That condition says:

- every filter realizes an already-admissible self-directed focus allocation;
- every already-admissible self-directed focus allocation can be represented by at least one filter;
- no new focus state, update channel, causal power, or reachable world-state is introduced merely by naming the filter.

Two filters may differ internally while inducing the same self-directed focus allocation. Define

\[
f\equiv_{\mathrm{Foc},t}g
\iff
\pi^m_t(f)=\pi^m_t(g).
\]

Then

\[
\mathcal F^m_t/\!\equiv_{\mathrm{Foc},t}
\cong
\mathfrak F^m_t.
\]

This is the exact sense in which “filter” supplies fidelity rather than mechanism. It is a coordinate chart on an existing part of the theory.

### 2.1 Internal verdict

Within TLICA’s own formal structure, the conservative-refinement claim is **DISCLOSED conditional on the image condition above**: if the filter space is restricted to parameterize exactly the already-admissible self-directed focus allocations, the refinement changes representation, not model class.

The stronger psychological claim—that human choosing is well modeled by such filter application—is not disclosed by the formal equivalence. It remains empirically vulnerable.

---

## 3. Motivating phenomenology: moving and not moving an arm

Consider an ordinary voluntary arm movement.

From the inside, it is often unclear when a discrete “decision to move” occurred. One can identify:

- an emerging orientation toward moving;
- a felt affordance or readiness;
- the onset of bodily motion;
- recognition that one has chosen;
- a reportable time assigned afterward.

But those need not collapse into one point.

Now consider deciding **not** to move the arm. Once the non-movement orientation is stably in place, nothing moves unless an internal or external salience event, bodily perturbation, competing aim, reflex, fatigue, pain, or other interruption shifts the field.

The asymmetric phenomenology suggests:

1. moving need not begin with an introspectively discrete motor-command token;
2. non-movement need not be continuously re-selected muscle by muscle;
3. both may be changes in the weighting and stability of response basins;
4. the apparent “moment of decision” may be an onset, threshold crossing, closure, recognition, or report marker rather than one universal event.

This is compatible with the existing timing-marker non-identity chain:

\[
t_{\mathrm{prep}}
\not\equiv
t_{\mathrm{select}}
\not\equiv
t_{\mathrm{report}}
\not\equiv
t_{\mathrm{move}}
\not\equiv
t_{\mathrm{outcome}}
\not\equiv
t_{\mathrm{recognize}}.
\]

The refinement adds that \(t_{\mathrm{select}}\) may itself be better represented as an interval or deformation process:

\[
[t_{\mathrm{orient}},t_{\mathrm{closure}}],
\]

with no commitment that every choice contains one phenomenally privileged instant.

This phenomenology is **OBSERVED in the motivating case**, not proof of the underlying model.

---

## 4. The present field and its baseline weighting

For modeling I \(m\) at time \(t\), let

\[
\mathcal U^m_t
\subseteq
\operatorname{Cl}(\mathsf{Tools}^m_t;\mathsf A^{+,m}_t)
\]

be the currently usable field of percepts, interpretations, affordances, possible understandings, and response-relevant constructions.

The field is constrained by:

- phenomenal availability;
- current toolkit closure;
- focus capacity \(M_m(t)\);
- contact \(\kappa\);
- existing identity-integration \(\rho\);
- source and mediation structure;
- salience-gating;
- current bodily and affective state;
- osmotically imprinted dispositions;
- the environment’s active impingement.

Before deliberate self-direction, let

\[
\omega^{0,m}_t(x)
\]

be an application-level baseline weighting over \(x\in\mathcal U^m_t\). This is not a fourth TLICA coordinate. It is shorthand for the joint result of already-existing contact-driven, substrate, salience, history, toolkit, and osmotic factors.

The baseline does not mean “what would happen without a self.” It means the current weighting before the particular self-directed deformation being modeled.

---

## 5. Choice as a filter over the field

An admissible volitional filter is a bounded, toolkit-constructible deformation

\[
f^m_t:\mathcal U^m_t\to\mathbb R
\]

or, more generally, an operator on the current weighting field.

A positive value means comparative emphasis, stabilization, or increased availability. A negative value means comparative deemphasis, inhibition, distancing, or reduced availability. Zero means no direct change by this filter at that location.

The simplest direct model is

\[
\widetilde\omega^{f,m}_t(x)
=
\omega^{0,m}_t(x)+f^m_t(x).
\]

A multiplicative normalized model is

\[
\omega^{f,m}_t(x)
=
\frac{
\omega^{0,m}_t(x)e^{f^m_t(x)}
}{
Z^m_t(f)
}.
\]

Neither formula is a foundation commitment. They are alternative application-level realizations of the same dependency claim:

\[
\boxed{
\text{self-directed focus changes the comparative weighting of the present field under a fixed capacity bound.}
}
\]

The capacity-bounded focus set may then be modeled schematically by

\[
\mathsf{Foc}^m_t(f)
=
\operatorname{Top}_{M_m(t)}\big(\omega^{f,m}_t\big),
\]

where `Top` need not mean a literal winner-take-all ranking. It abbreviates whatever substrate-realization selects or sustains no more than \(M_m(t)\) focus slots from the weighted field.

### 5.1 What is chosen

The I is not choosing which particular graph edges will strengthen or weaken. The I is choosing—by enacting—the field deformation that changes which contents are held, compared, probed, stabilized, inhibited, and made response-relevant.

Thus:

\[
\boxed{
\text{choice selects a filter profile, not a list of integration-edge edits.}
}
\]

The existing update functions determine the actual edge-level effects.

---

## 6. Correlated-neighborhood propagation

Focusing on one content rarely changes only that content. Contents are coupled by:

- shared paths in the lived-I integration graphs;
- common verification tools and inferential relations;
- learned co-activation;
- similarity and contrast structure;
- shared source maps or attributed sources;
- affective and somatic association;
- action-affordance structure;
- osmotic history;
- current task and context.

Let

\[
C^m_t(x,y)
\]

be an application-level correlation or transport kernel measuring how a direct filter deformation at \(y\) changes effective weighting at \(x\).

Then

\[
(C^m_tf^m_t)(x)
=
\int_{\mathcal U^m_t}C^m_t(x,y)f^m_t(y)\,dy
\]

or, in a finite field,

\[
(C^m_tf^m_t)_i
=
\sum_j C^m_{t,ij}f^m_{t,j}.
\]

The effective weighting becomes

\[
\omega^{f,m}_t(x)
=
\frac{
\omega^{0,m}_t(x)e^{(C^m_tf^m_t)(x)}
}{
Z^m_t(f)
}.
\]

### 6.1 The kernel is not a new primitive

\(C^m_t\) is not proposed as a foundation coordinate or independent mechanism. It is an applied summary induced by existing relational structure. Schematically,

\[
C^m_t
=
\Psi\big(
(G^{m,k}_t)_k,
\mathsf{Tools}^m_t,
\text{co-activation history},
\text{salience relations},
\text{somatic-affective associations},
\text{context}
\big).
\]

Different empirical implementations may estimate it differently. The architecture-level commitment is only that relationally coupled contents need not update independently.

### 6.2 The phenomenological consequence

The I chooses a way of looking, inhabiting, interpreting, or holding—not each downstream consequence of that way of looking.

Therefore:

\[
\boxed{
\text{the directly emphasized region and its correlated neighborhood can both cross update thresholds.}
}
\]

This captures the intuition that chosen focus raises the positive or negative integration pressure of selected and nearby contents above what they would ordinarily have received through ambient/osmotic exposure alone.

---

## 7. Existing TLICA dynamics perform the update

The frozen architecture already gives the focus/contact-dependent update form

\[
w^{m,k}_{s^+}(u,v)
=
\Pi_{[0,1]}
\left(
(1-\beta)w^{m,k}_{s^-}(u,v)
+
\alpha(1-w^{m,k}_{s^-}(u,v))
\right),
\]

with

\[
\alpha
=
\mathcal A^k_m
\big(u,v;\mathsf{Foc}^m_s,\lambda^m_s(v)\big),
\]

\[
\beta
=
\mathcal B^k_m
\big(u,v;\mathsf{Foc}^m_s,\lambda^m_s(v)\big).
\]

The filter refinement simply fills in the self-directed contribution to the existing focus argument:

\[
f^m_s
\xrightarrow{\pi^m_s}
\mathsf{Foc}^m_s[\mathrm{self\text{-}directed}]
\hookrightarrow
\mathsf{Foc}^m_s.
\]

Then the old functions run unchanged.

### 7.1 Volitional excess integration

To formalize “above what would have occurred osmotically,” define the model-relative, counterfactual diagnostic

\[
\operatorname{VEI}^{m,k}_{t}(u,v;f)
:=
\Delta w^{m,k}_{t}(u,v\mid f)
-
\Delta w^{m,k}_{t}(u,v\mid f=0),
\]

holding the modeled external contact and other state variables fixed as far as the design permits.

- \(\operatorname{VEI}>0\): the chosen filter increased net integration relative to baseline;
- \(\operatorname{VEI}<0\): it increased net weakening, inhibition, separation, or non-integration relative to baseline;
- \(\operatorname{VEI}=0\): no detectable differential update.

This is **not** a new TLICA coordinate and not directly observable without a counterfactual model or controlled comparison. It is an applied diagnostic for the incremental effect of self-directed filtering over the background update process.

### 7.2 Closed-loop self-modification

Because integration changes the future lived-I network and toolkit-accessible geometry,

\[
\boxed{
\text{choice changes not only the current trajectory but the geometry of later choosing.}
}
\]

The full loop is

\[
\begin{aligned}
f^m_t
&\to
\mathsf{Foc}^m_t
\to
(\mu^m_t,\alpha_t,\beta_t)
\to
(G^{m,k}_{t+1})_k\\
&\to
C^m_{t+1},\omega^{0,m}_{t+1},\mathsf{Tools}^m_{t+1}
\to
\mathcal F^m_{t+1}
\to
\text{later choice geometry}.
\end{aligned}
\]

This is the agency-side counterpart of toolkit-shape acquisition and compiled transport.

---

## 8. Perceptual momentum

### 8.1 Definition by control cost

Let \(z^m_t\) denote the relevant total state of the modeled episode, and let \(B\) be a response basin: remain still, move the arm, withdraw, speak, continue reading, reframe an insult, begin a proof, and so on.

Let \(R_{t+\Delta}\) be the downstream response variable at an episode-appropriate horizon. Define **perceptual momentum toward basin \(B\)** as

\[
\boxed{
\operatorname{PM}^m_t(B;\tau)
=
\inf_{f\in\mathcal F^m_t}
\left\{
\|f\|_{\mathcal F}
:
\Pr(R_{t+\Delta}\in B\mid z^m_t,f)\ge\tau
\right\}.
}
\]

Interpretation:

- low \(\operatorname{PM}\): a small admissible filter deformation can make \(B\) dominant;
- high \(\operatorname{PM}\): a strong, sustained, recursive, or specially structured deformation is required;
- unreachable/captured regime: no currently constructible filter within the I’s available capacity makes \(B\) live above threshold.

Perceptual momentum is target-relative, state-relative, toolkit-relative, and time-relative. It is not a scalar trait of the person.

### 8.2 Response leverage

Define the response leverage of a filter by

\[
\operatorname{Lev}^m_t(f)
=
\frac{
D\big(P(R\mid z_t,f),P(R\mid z_t,0)\big)
}{
\|f\|_{\mathcal F}
},
\]

for a declared divergence or distance \(D\).

High leverage means a small filter change yields a large response-distribution change. Low leverage means the current trajectory absorbs or resists the deformation.

Informally,

\[
\operatorname{Lev}\sim \operatorname{PM}^{-1},
\]

but they are not identical unless an implementation and target family make the duality precise.

### 8.3 Perceptual momentum is not a new force

\(\operatorname{PM}\) summarizes the joint resistance already generated by:

- contact-driven salience;
- entrenched integration;
- current somatic state;
- affective activation;
- habit;
- fatigue;
- environmental constraint;
- substrate capture, bypass, or preemption;
- toolkit limitations;
- competing filters and goals;
- learned expectations;
- action costs and affordances.

It is therefore an applied control diagnostic over existing dependencies, not an additional causal substance.

### 8.4 Distinctions that must remain separate

Perceptual momentum must not be collapsed with:

- \(\kappa\): contact can contribute to momentum but is not momentum;
- \(\phi\): truth-verification access does not determine ease of response redirection;
- \(\rho\): identity-integration can contribute to resistance or support but is not the control threshold;
- \(\mu\): probe availability/weighting is one downstream channel, not the whole resistance profile;
- effort: felt effort is an inside-perspective correlate that may track control cost imperfectly;
- ownership: a high-momentum act can be owned, and a low-momentum act can be alienated;
- moral worth: ease or difficulty of redirection is not evidence of goodness.

---

## 9. First-order willing as low-momentum, high-leverage filter control

The crucial refinement is:

\[
\boxed{
\text{First-order willing occurs when one chosen perceptual filter-shift has sufficiently high leverage to redirect the response trajectory.}
}
\]

Equivalently, for target basin \(B\), first-order willing is available when there exists a constructible filter \(f\) such that

\[
\|f\|_{\mathcal F}
\text{ is small enough for immediate deployment}
\]

while

\[
D\big(P(R\mid f),P(R\mid0)\big)
\]

is large enough to cross the relevant response threshold without requiring an intermediate self-directed re-representation loop.

### 9.1 The arm movement

For an ordinary arm movement in a neutral setting:

\[
\operatorname{PM}_t(B_{\mathrm{move}})
\]

may be low. The agent’s chosen perceptual/affordance filter—“move now,” “reach,” “inhabit the reaching”—changes the field enough that the substrate follows into the motor basin.

The body can move to a high degree even though the **willing operation** was first-order, because the order of the choice concerns the minimal control deformation required, not the anatomical depth of the final output.

Thus:

\[
\boxed{
\text{first-order in control}
\quad\text{can be}\quad
\text{third-order in bodily realization}.
}
\]

### 9.2 Deliberate non-movement

Suppose \(B_{\mathrm{rest}}\) is already stable. Applying a “do not move” filter need not specify every excluded muscle activation. It can increase the stability of the resting basin or raise the effective threshold for movement affordances:

\[
\operatorname{PM}_t
\big(B_{\mathrm{move}}\mid f_{\neg\mathrm{move}}\big)
>
\operatorname{PM}_t
\big(B_{\mathrm{move}}\mid0\big).
\]

Then, absent sufficient interruption,

\[
R_{t+\Delta}\in B_{\mathrm{rest}}.
\]

A salient outside event can still alter the contact-driven component, change the field, and overcome the stabilized basin. This directly preserves the foundation’s claim that self-directed focus grows but contact-driven capture never disappears.

### 9.3 Negative choice is not pointwise negation

“Do not move” is not the selection of every point in the complement of movement. It is a filter that stabilizes a region of trajectory-space.

This generalizes:

- do not answer yet;
- refuse;
- wait;
- remain with the discomfort;
- do not follow the intrusive frame;
- withhold assent.

These are positive configurations of the field even when their macroscopic description is omission or veto.

---

## 10. Refining the orders of willing

The prior architecture correctly identified a layered shape:

1. focus/perceptual direction;
2. thought/deliberative direction;
3. bodily implementation;
4. constructed orders acting through other agents and structures.

The missing fidelity was that **the order at which the result appears and the order of control required to produce it can differ**.

Introduce two application-level indices:

### 10.1 Control depth

\[
d_{\mathrm c}(a)
=
\text{minimum number of endogenous filter/feedback stages required to make act-trajectory }a\text{ live and selected}.
\]

### 10.2 Realization depth

\[
d_{\mathrm r}(a)
=
\text{the pathway/order at which the selected trajectory is implemented or expressed}.
\]

An episode may therefore be described by

\[
\boxed{
\operatorname{Ord}(a)
=
\big(d_{\mathrm c}(a),d_{\mathrm r}(a)\big).
}
\]

This is a typed refinement of the existing order profile, not a new causal mechanism.

### 10.3 First-order control

One filter application directly changes salience, perceptual organization, affordance weighting, or response readiness enough to redirect the trajectory:

\[
f_1
\to
\text{effective field}
\to
\text{response}.
\]

Examples can include:

- looking at the door instead of the screen;
- moving an arm under low resistance;
- withholding a trivial impulse;
- choosing one of two equally live routine actions;
- rapidly reorienting to an already-mastered task.

### 10.4 Second-order control

The initial filter must sustain or reorganize an intermediate cognitive representation before the target trajectory becomes live:

\[
f_1
\to
\text{thought/re-representation}
\to
f_2\text{ or stabilized cognitive field}
\to
\text{response}.
\]

Examples can include:

- deciding to think through a budget rather than merely glance at it;
- holding a counterexample in mind until a favored proof-frame loosens;
- reframing an ambiguous social event before responding;
- comparing two policies whose consequences are not immediately perceptible.

### 10.5 Third-order control

The chosen filter must propagate through, alter, or repeatedly engage somatic-affective dynamics before the target trajectory becomes live:

\[
f_1
\to
\text{somatic/affective response}
\to
\text{cognitive integration}
\to
f_2, f_3,\ldots
\to
\text{response}.
\]

This can occur when perceptual momentum is high because of pain, panic, fatigue, craving, trauma activation, entrenched habit, or other substrate dynamics. The classification is not moral and is not tied to any diagnosis.

### 10.6 Constructed orders

At constructed orders, the chosen filter must organize trajectories through other agents, tools, institutions, or extended structures:

\[
f
\to
\text{request/plan/role activation}
\to
\text{other-agent or institutional response}
\to
\text{cascade}.
\]

The same distinction remains useful:

- a single low-momentum request may have \(d_{\mathrm c}=1\) and \(d_{\mathrm r}\ge4\);
- a difficult organizational intervention may require high control depth and high realization depth.

### 10.7 Why the old theory remains right

The frozen theory correctly described the layered route from focus through thought and body to constructed action. The refinement supplies a missing type distinction:

\[
\boxed{
\text{where the effect is realized}
\neq
\text{how many control transformations were required to select it}.
}
\]

No old dependency is denied. The interpretation becomes more exact.

---

## 11. Discrete options as quotient classes of filters

Let \(\mathcal F^m_t\) be the currently constructible filter space. Define a response equivalence relation at the resolution relevant to the episode:

\[
f\sim^m_{R,t} g
\iff
P(R_{t+\Delta}\mid z_t,f)
\approx_{\varepsilon}
P(R_{t+\Delta}\mid z_t,g),
\]

or, more coarsely,

\[
f\sim^m_{B,t}g
\iff
f\text{ and }g\text{ enter the same response basin }B.
\]

Then the macroscopic live-option space can be represented as

\[
\boxed{
\mathcal O^m_t
=
\mathcal F^m_t/\!\sim^m_{R,t}.
}
\]

This does not abolish live options. It explains how apparently discrete options can arise from a continuous or high-dimensional field of possible filters.

### 11.1 Live-option criterion

An option class \([f]\in\mathcal O^m_t\) is live only if:

1. at least one representative filter is constructible from the current toolkit;
2. the agent can deploy it under the capacity bound;
3. its target trajectory is sufficiently inhabitable/evaluable;
4. current perceptual momentum does not place the basin outside available control reach;
5. implementation is not preempted, bypassed, or captured.

Thus an option can be verbally imaginable but not live because no admissible filter in its equivalence class has enough leverage under the current state.

### 11.2 Why “move” is not a primitive point

“Move the arm” denotes a class containing many micro-different filters and trajectories that converge on the same macroscopic bodily basin. “Do not move” denotes another class, often realized by stabilizing the current basin rather than constructing a detailed complement.

The option set is therefore a useful coarse-graining:

\[
\text{continuous/high-dimensional filter geometry}
\to
\text{response basins}
\to
\text{discrete live-option classes}.
\]

---

## 12. Exact mapping to the six conditions of free choice

The refinement maps onto the existing six conditions without adding a seventh.

### Condition 1 — Contrastive live-option space

The toolkit constructs at least two reachable response-equivalence classes:

\[
[f_1],[f_2]\in\mathcal O^m_t,
\qquad
[f_1]\neq[f_2].
\]

Refusal, waiting, or doing nothing count when a stabilizing filter class is genuinely deployable.

### Condition 2 — Evaluative engagement

The I’s prerogatives, preservation ranking, commitments, evidence-status distinctions, and current relevance structure shape which filter deformations are sustained and compared. Evaluation alters the geometry and weighting of candidate filters; it need not appear as verbal deliberation.

### Condition 3 — Operator-bundle selection

Operator-bundle selection is now specified more exactly as the actual endogenous application/stabilization of one admissible filter trajectory rather than merely the abstract naming of an option.

\[
\boxed{
\text{selection-event}
=
\text{the filter deformation becoming operative}.
}
\]

There is no additional selector behind it.

### Condition 4 — Substrate coupling without preemption, bypass, or capture

The filter-induced trajectory must propagate through the substrate rather than being preempted, bypassed, or rendered ineffective by capture. Perceptual momentum provides an applied way to describe degrees and target-relative thresholds within this condition.

### Condition 5 — Non-confabulatory Mode B availability

Mode B can take the current filter, its sources, its operative default, its response basin, or its failure to gain leverage as an object. Mode B need not be occurrent in every choice. Later narration does not establish that the operative filter was reflectively accessed at selection time.

### Condition 6 — Ownership-integration

The enacted filter and resulting trajectory integrate as mine. Ownership does not certify clean sourcehood, truth, goodness, or adequate verification.

### 12.1 Conservative conclusion

Every existing condition keeps its function. The filter account fills the low-level semantics of Conditions 1–4 and the object available to Conditions 5–6.

---

## 13. Re-reading agency variations through filter geometry

The following are candidate translations, not replacements for the existing taxonomy.

| Existing configuration | Filter/momentum refinement |
|---|---|
| **Thin/free selection** | Distinct response classes are live; a low-cost filter deformation selects among them with little evaluative depth. |
| **Ordinary reduced agency** | Filter space or leverage is temporarily narrowed by fatigue, distraction, time pressure, or competing contact. |
| **Flow/skilled action** | A compiled filter policy has high task-relative leverage and low explicit control cost; Mode B remains available under intact conditions. |
| **Habit** | Repeated past filter trajectories have altered the baseline weighting so the response is now cheaply or automatically activated. |
| **Akrasia** | Evaluation stabilizes one filter/response class, but the operative selection trajectory settles into another despite alternatives remaining live. |
| **Compulsion** | The alternative filter class is weakly reachable or bypassed; the act can exit through a substrate route before comparative filtering gains control. |
| **Addiction-like capture** | Perceptual momentum toward the captured basin is so high, or away from it so high, that the alternative filter class ceases to be sufficiently inhabitable under current capacity. |
| **ADHD-like implementation gap** | A target filter may be evaluatively selected but fail to remain stabilized across the interval required for downstream implementation. |
| **Learned helplessness** | Projection/toolkit structure fails to construct filters with expected leverage; alternative basins are represented as ineffective or unreachable. |
| **Dissociation/alienated action** | Filter/response propagation occurs with impaired ownership-integration or with the operative trajectory experienced as not-mine. |
| **Manipulation** | The agent genuinely applies and owns a filter, while the baseline field, correlation structure, available filter family, or apparent response classes were externally shaped. |
| **Micro-periagoge** | Mode B activates early enough to rotate the operative filter before selection closure, reopening at least one live response class. |
| **Compiled transport** | Repeated prior filter applications have reshaped the baseline field so the later response occurs without fresh explicit reorientation. |

These translations should be evaluated by whether they preserve the distinct signatures already carried by the taxonomy. They must not flatten all failures into “insufficient leverage.”

---

## 14. Manipulation becomes more precise

The manipulation paradigm is especially revealing.

An agent may have:

- intact filter-control;
- intact evaluation;
- intact operator-bundle selection;
- intact substrate coupling;
- intact Mode B for the presented options;
- intact ownership;

while the manipulator has shaped one or more upstream objects:

\[
\omega^{0,m}_t,
\qquad
C^m_t,
\qquad
\mathcal U^m_t,
\qquad
\mathcal F^m_t,
\qquad
\mathcal O^m_t.
\]

The agent chooses the filter. The choice is real and owned. The source geometry of what could be salient, construable, evaluable, or reachable is compromised.

This preserves the architecture’s central ownership/sourcehood dissociation while making the upstream rigging more formally legible.

It also shows why “choice is a filter” does not imply unlimited freedom. One can choose only among constructible filters over the field one has, with the correlations, baselines, and control limits one currently carries.

---

## 15. Relation to osmotic imprinting and acquired toolkit shape

Osmotic imprinting remains continuously active without requiring focus, verification, or mode operation. Deliberate filtering does not replace it.

The distinction is:

\[
\text{osmotic baseline update}
\quad\text{vs.}\quad
\text{filter-amplified differential update}.
\]

A chosen filter can cause selected and correlated contents to receive more or less integration pressure than they would have received from ambient co-occurrence alone.

Repeated filter application can then alter:

- salience thresholds;
- response expectations;
- integration graphs;
- discriminative operators;
- toolkit closure;
- baseline affective associations;
- the effective correlation kernel;
- future control cost.

This yields the developmental loop

\[
\boxed{
\text{chosen way of attending today}
\to
\text{changed integration}
\to
\text{changed field tomorrow}
\to
\text{changed future agency}.
}
\]

The same loop explains how repeated reorientation can become compiled transport: what once required a deliberate filter becomes part of the later baseline weighting or a highly accessible low-cost filter policy.

This connection is theoretically important but does not imply that all toolkit acquisition is voluntary. Much of it remains osmotic, contact-driven, developmentally inherited, socially shaped, or substrate-limited.

---

## 16. Truth, identity, contact, and focus must remain separate

A filter can emphasize truth, falsehood, fantasy, trauma activation, evidence, prejudice, care, resentment, mathematics, or noise. The fact that a content receives focus and integration pressure does not improve its epistemic status.

Therefore:

\[
\boxed{
\text{chosen emphasis}
\not\Rightarrow
\text{truth}.
}
\]

Track separately:

- \(\kappa\): how live/contacted the content is;
- \(\phi\): toolkit-relative truth-verification/pathway state where defined;
- \(\sigma\): source-map adequacy;
- \(\rho\): identity/commitment integration;
- \(\mu\): probe availability and weighting;
- focus allocation;
- filter leverage;
- perceptual momentum;
- ownership;
- sourcehood.

A filter can increase \(\rho\) around a false content. A highly verified content can have little current focus. A low-\(\phi\) affect can dominate the field. A manipulated frame can be wholeheartedly owned. The refinement must preserve all these dissociations.

---

## 17. Decision-events and selection closure

The filter account suggests a more exact process model.

Let

\[
f_t
\]

be the evolving self-directed deformation. Define candidate episode markers:

- \(t_{\mathrm{availability}}\): a relevant filter class becomes constructible;
- \(t_{\mathrm{orientation}}\): self-directed deformation begins;
- \(t_{\mathrm{dominance}}\): one filter/response class becomes locally dominant;
- \(t_{\mathrm{closure}}\): reversal would require opening a new decision episode or overcoming a substantially higher barrier;
- \(t_{\mathrm{implementation}}\): the selected trajectory reaches its realization pathway;
- \(t_{\mathrm{recognition}}\): the I recognizes the choice as made;
- \(t_{\mathrm{report}}\): the I assigns or communicates a time.

No universal identity among these times is assumed.

A minimal selection-event can be modeled as the interval in which the operative filter crosses from candidate to dynamically controlling:

\[
\mathcal S
=
[t_{\mathrm{orientation}},t_{\mathrm{closure}}].
\]

A sharp point \(t_{\mathrm{select}}\) may be introduced for a particular empirical model—for example, threshold crossing—but must not be mistaken for a theory-independent phenomenal atom.

---

## 18. Testable predictions

The refinement earns value only if it distinguishes outcomes that the coarser language does not.

### P1 — State-dependent leverage

Hold the instructed filter approximately fixed while manipulating perceptual momentum. The same intended reorientation should produce different downstream response shifts.

\[
\text{same filter instruction}
+
\text{different momentum}
\Rightarrow
\text{different leverage}.
\]

### P2 — Correlated-neighborhood update

Direct focus on \(x\), while holding exposure to neighboring contents as constant as possible. Contents \(y\) with stronger estimated correlation \(C_t(x,y)\) should show larger later activation or integration changes than equally exposed but weakly correlated controls.

### P3 — Volitional excess over osmotic baseline

Matched ambient exposure with deliberate filtering should yield a differential update:

\[
\Delta w(f)-\Delta w(0)\neq0
\]

for at least some targeted and correlated relations.

### P4 — Control order can dissociate from realization order

The same bodily act should sometimes be produced by first-order control and sometimes require higher control depth, depending on state and resistance. Classification by control depth should predict latency, interruption sensitivity, subjective effort, error profile, and need for recursive reorientation better than classification by bodily output alone.

### P5 — Stable non-movement does not require continuous explicit reselection

After a non-movement filter stabilizes the resting basin, explicit decision reports should not be continuously required for continued stillness. Exogenous salience or internal perturbation should predict basin exit better than the absence of repeated conscious veto tokens.

### P6 — Repetition compiles filters

Repeated successful use of a filter should reduce later control cost, shorten reorientation latency, and increase robustness to moderate interference, while preserving the possibility of Mode B access under intact conditions.

### P7 — Manipulation can preserve filter-control while changing source geometry

Agents can show intact within-field selection and ownership while experimentally altered framing changes baseline weighting, correlation structure, or apparent option classes. This predicts a dissociation between local control competence and source-clean option construction.

### P8 — Option boundaries are resolution-dependent

Filters that subjects initially describe as distinct choices may collapse into the same response-equivalence class at one measurement scale, while one verbally named option may split into multiple classes under finer trajectory measurement.

### P9 — Momentum is target-relative

The same state can make one basin easy and another difficult. There should be no single context-free “willpower” scalar that predicts all redirections.

### P10 — Reflective recognition may lag operative selection

Under low-momentum, high-leverage conditions, trajectory redirection can begin before a reportable recognition point without implying that the action was unchosen. The decisive discriminator is whether perturbing the endogenous filter before closure changes the trajectory.

---

## 19. Discriminating probes

### Probe A — Momentum sweep

Construct one response target under graded resistance conditions. Keep the declared filter instruction fixed.

Pre-register:

- **filter-momentum support:** response shift decreases smoothly or threshold-wise as independently manipulated resistance rises;
- **pure command model support:** once the command is issued, comparable implementation follows regardless of perceptual-state geometry, except for downstream motor limits;
- **ambiguous:** instruction compliance, effort, or state manipulation cannot be separated.

### Probe B — Same body act, different control depth

Use the same overt movement under:

1. neutral low-resistance conditions;
2. competing-attention conditions;
3. affectively or habitually opposed conditions;
4. a trained/compiled condition.

Measure latency, reversibility before closure, interruption effects, subjective effort, error structure, and transfer.

The refinement predicts that overt identity of the movement does not imply identity of the will-order.

### Probe C — Correlation transport

Estimate a subject-specific correlation map among contents. Direct focus to one node and measure later changes in unfocused neighbors.

Controls:

- matched exposure;
- matched semantic similarity without integration-path proximity;
- sham focus;
- a mutation condition that breaks the learned relation.

### Probe D — Stillness basin

Ask subjects to remain still, then introduce graded salience perturbations. Distinguish:

- continuous explicit veto reports;
- stable basin maintenance;
- reflexive preemption;
- deliberate release of the filter;
- post-hoc narration.

### Probe E — Filter interruption before and after closure

Deliver a counter-filter cue at varied times. The model predicts a change in reversibility around selection closure rather than a necessary one-to-one relation with reported decision time.

### Probe F — Compilation longitudinal

Train one reorientation repeatedly. Test whether the same target response later requires less explicit filter maintenance and whether that reduction transfers to structurally related but novel cases.

### Probe G — Option quotient recovery

Collect many micro-different framing/filter trajectories and cluster them by downstream response distributions. Compare empirically recovered classes with subjects’ named options.

A successful quotient model should explain both:

- many-to-one convergence: distinct micro-filters, same macroscopic option;
- one-to-many splitting: one verbal option, multiple dynamically distinct realization classes.

---

## 20. Controls and falsifiers

### Positive control

A well-trained attentional reorientation known to alter a simple response should show measurable leverage.

### Negative control

A filter instruction outside the subject’s toolkit closure should fail to produce the predicted structured change, even if the words are understood superficially.

### Null control

Matched exposure with no self-directed emphasis should estimate the osmotic/contact baseline.

### Mutation control

Disrupt or invert a learned correlation while preserving local stimulus exposure. Correlated-neighborhood effects should change with the relation rather than merely with proximity or repetition.

### Candidate falsifiers

The refinement loses explanatory weight if careful studies show that:

1. deliberate focus effects are strictly pointwise and never track relational neighborhoods after exposure is controlled;
2. response leverage does not vary with independently manipulated state resistance;
3. first-/higher-control-depth classifications fail to predict latency, reversibility, interruption, effort, or learning beyond overt action categories;
4. repeated filtering does not alter future baseline accessibility or control cost under matched exposure;
5. discrete options behave as invariant primitives across measurement resolutions rather than as stable coarse-grainings;
6. reported filter application has no causal sensitivity before closure and functions only as post-hoc narration;
7. the proposed filter parameterization requires focus states or causal transitions not already admissible in the frozen architecture, violating the conservative-refinement condition.

---

## 21. Rival interpretations that remain live

### R1 — Discrete command selection

The agent selects a motor or cognitive command token, and attentional changes are preparatory or incidental.

### R2 — Pure post-hoc authorship

The substrate determines the response; the filter report is a later ownership narrative without causal control.

### R3 — Attention-only, no option quotient

Self-directed attention is real, but discrete options remain primitive and are merely illuminated by attention rather than generated as response-equivalence classes.

### R4 — Predictive/control implementation reduction

The entire account reduces without remainder to a third-person control-system model; the indexed inside-perspective structure adds no discriminating content.

### R5 — Conservative TLICA filter refinement

Choice is the endogenous filter deformation already implicit in self-directed focus; the deformation changes correlated weighting, existing TLICA update rules propagate it, and live options are macro-level quotient classes.

The research target is not to rename ordinary attention. It is to test whether R5 uniquely predicts the joint pattern of state-dependent leverage, correlated-neighborhood updating, control/realization-order dissociation, compilation, and resolution-dependent option classes.

---

## 22. Failure modes of the refinement

### 22.1 Homunculus relocation

**Error:** “The I first chooses which filter to choose.”  
**Correction:** the endogenous filter deformation is the choice-event.

### 22.2 Filter omnipotence

**Error:** any imaginable frame can be selected and made effective.  
**Correction:** filters are toolkit-, capacity-, state-, contact-, and substrate-bounded; high momentum or capture can make a class non-live.

### 22.3 Pointwise integration control

**Error:** the agent directly chooses every strengthened or weakened content.  
**Correction:** the agent controls a field deformation; relational and substrate dynamics determine local updates.

### 22.4 Truth by attention

**Error:** a chosen, coherent, or identity-integrated frame is thereby true.  
**Correction:** \(\phi\), \(\sigma\), evidence, and probe outcomes remain separate.

### 22.5 Order collapse

**Error:** every bodily action is third-order willing in the same operative sense.  
**Correction:** classify control depth and realization depth separately.

### 22.6 Momentum as trait

**Error:** perceptual momentum is a person-level willpower score.  
**Correction:** it is target-, state-, toolkit-, and time-relative.

### 22.7 Osmosis erasure

**Error:** deliberate filtering explains all learning and disposition formation.  
**Correction:** osmotic imprinting remains continuously active and often dominant.

### 22.8 Causal overclaim from phenomenology

**Error:** ambiguity about decision time proves the filter model.  
**Correction:** the phenomenology motivates the model; causal claims require discriminating intervention.

---

## 23. Claim ledger

| Claim | Status | Boundary / truth debt |
|---|---|---|
| The frozen architecture already contains self-directed focus, focus-driven probe weighting, focus/contact-driven integration updates, live-option construction, operator-bundle selection, substrate coupling, and order-indexed willing | **DISCLOSED within TLICA** | Existing theory structure; this is an archive-relative claim, not external empirical validation. |
| A filter space can conservatively parameterize existing self-directed focus without adding reachable states | **DISCLOSED conditional on** \(\operatorname{Im}(\pi_t)=\mathfrak F_t\) | Formal representation result; the image condition must be preserved in any implementation. |
| The act of choosing is exactly the operative endogenous filter deformation, not a prior selector-act | **Interpretive refinement / CONJECTURED as psychology** | Internally removes regress and maps cleanly to the theory; empirical adequacy remains open. |
| Focus changes correlated neighborhoods rather than isolated points | **CONJECTURED, strongly structurally motivated** | Requires subject-specific relation mapping and matched-exposure controls. |
| Chosen filtering produces integration/disintegration above osmotic baseline | **UNVERIFIED** | Needs controlled counterfactual estimation of volitional excess integration. |
| Perceptual momentum is a useful target-relative control-cost diagnostic | **CONJECTURED** | Must outperform simpler effort, salience, habit, and motor-resistance measures. |
| First-order willing is low-momentum/high-leverage filter control | **Interpretive refinement; empirical status UNVERIFIED** | Must predict response profiles across matched overt actions. |
| A bodily movement can be first-order in control and third-order in realization | **Conjectured refinement** | Requires validated separation of control depth from output pathway. |
| Discrete live options are quotient classes of admissible filters by response equivalence | **Conjectured formalization** | Requires declared resolution, metric, and empirical recovery of stable classes. |
| Repeated chosen filters reshape future choice geometry | **Conjectured / partially inherited from existing imprinting dynamics** | The dependency is internal; the magnitude, direction, and empirical specificity require longitudinal tests. |
| The filter refinement preserves the six-condition free-choice architecture | **Corroborated internally by explicit mapping** | Does not by itself validate the six conditions externally. |
| Ambiguous decision phenomenology supports a selection interval rather than a universal point | **OBSERVED motivation; theoretical conclusion CONJECTURED** | Reportability, preparation, selection, closure, and recognition must be experimentally separated. |

---

## 24. Integration rule

Do **not** modify the frozen foundation merely because the refinement is coherent.

The present note should remain application/research-layer material until it survives at least the following checks:

1. **Conservativity audit:** prove that the chosen filter formalism parameterizes, rather than enlarges, admissible self-directed focus dynamics.
2. **Taxonomy preservation:** show that akrasia, compulsion, capture, manipulation, flow, habit, and dissociation retain distinct signatures.
3. **Control/realization discrimination:** demonstrate that the two-depth account predicts measurable differences for the same overt action.
4. **Correlated-neighborhood probe:** show a relational update beyond matched exposure and pointwise attention.
5. **Momentum probe:** manipulate resistance independently enough to establish state-dependent filter leverage.
6. **Compilation holdout:** show that repeated filtering changes later control cost on fresh, structurally related cases.
7. **Hostile confabulation test:** demonstrate causal sensitivity to filter perturbation before closure rather than relying on retrospective reports.

A later foundation-facing patch, if warranted, should be small. It would clarify the semantics of self-directed focus and order profiles rather than introduce a new coordinate or faculty.

---

## 25. Durable formulation

The highest-fidelity statement is:

> **Choice is not the selection of isolated points from a ready-made option set. The I inhabits a toolkit- and substrate-bounded field of possible understandings and response-trajectories. Choosing is the endogenous application of a filter to that field. The filter changes which regions and correlated neighborhoods receive focus, probing, and update pressure; the existing TLICA dynamics determine the resulting integrations, disintegrations, and bodily trajectory. Apparently discrete options are macroscopic equivalence classes of filters that converge on the same response basin. First-order willing occurs when perceptual momentum is low enough that one chosen filter-shift produces high downstream response leverage.**

The compact identity is:

\[
\boxed{
\text{choice}
=
\text{self-directed filter application}
\neq
\text{a hidden act prior to filter application}.
}
\]

The compact dynamics are:

\[
\boxed{
f_t
\to
\mathsf{Foc}_t
\to
(\mu_t,\alpha_t,\beta_t)
\to
G_{t+1}
\to
\text{response and future filter geometry}.}
\]

And the order refinement is:

\[
\boxed{
\operatorname{Ord}(a)
=
\big(\text{minimal control depth},\text{realization depth}\big).
}
\]

This preserves the frozen architecture’s shape while specifying the missing fidelity of what selection is.