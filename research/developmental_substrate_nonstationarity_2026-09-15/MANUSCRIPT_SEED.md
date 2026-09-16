# Developmental Substrate Nonstationarity
## Why childhood, adolescence, and young adulthood may feel phenomenologically different from adulthood

**Research-tier manuscript seed — 2026-09-15**

---

## Abstract

A recurring phenomenological asymmetry is easy to describe and easy to flatten: being a child, adolescent, or young adult can feel qualitatively different from adulthood not merely because one knows less, has less social power, or has accumulated fewer habits, but because the biological substrate through which experience is mediated is itself undergoing substantial development. This note develops that possibility inside TLICA without reducing phenomenology to neuroscience and without adding a new architectural coordinate.

The motivating first-person report is a transition from a developmental period characterized by pervasive affective "background buzzing" — feeling repeatedly pulled by emotion even when explicit cognitive frames changed — to an adult regime in which strong affect remains but is more often legibly tied to context. The original mechanistic intuition, "constant new neurons create unmapped noise," is rejected as too crude. The stronger candidate is **developmental substrate nonstationarity**: during development, neural and bodily response-properties continue to reorganize through changes in connectivity, synaptic organization, myelination, endocrine state, affective-control circuitry, and other processes. The I is therefore not learning to regulate a fixed plant. It is learning on a moving plant.

TLICA already contains almost all of the required machinery. The substrate sets inherited capacity; focus shifts from contact-driven toward increasingly self-directed control; third-order affect is substrate-mediated and characteristically source-opaque; osmotic imprinting continuously writes slow structure; and v5.5.0's `G` repair makes explicit that both the field-reading and identity-correlation are readings of a slower lived-I structure that can itself be rewritten. The missing application-level distinction is between **change in the learned self-structure** and **change in the substrate through which that structure is implemented, updated, and read**.

The central conjecture is not that developmental change causes emotion. It is that a sufficiently nonstationary substrate increases tracking load: mappings learned by the I become partially stale as the machinery implementing them changes, increasing endogenous contribution to affective dynamics and degrading causal/source resolution. When developmental reconfiguration slows relative to accumulated self-modeling and regulation, the same high-gain affective parameter may present less as ambient emotional weather and more as context-resolved signal. The author's depression/suppression/recovery arc is treated as a major confound and possible co-cause, not as an afterthought. The result is a discriminable coupled model rather than a retrospective just-so story.

---

## 1. The load-bearing phenomenological observation

The claim begins from experience, not biology.

The developmental report has two parts.

First, during childhood, adolescence, and young adulthood, emotion was not experienced merely as a sequence of context-specific reactions. There was a standing sense of being *pulled by affect itself*. A cognitive frame could change while the body-level force remained. Feelings behaved less like cleanly addressed messages and more like a carrier wave on which particular events were superimposed.

Second, adulthood does not feel like simple emotional attenuation. Strong feeling remains available. What changed is its **addressability**. Affect is more often recognizable as *about this situation, this person, this loss, this hope, this threat, this achievement*. The ratio between context-legible signal and background affective forcing appears to have changed.

A minimal phenomenological decomposition is therefore:

$$
A_{\mathrm{felt}}(t)
\approx
A_{\mathrm{context}}(t)
+
A_{\mathrm{substrate}}(t)
+
A_{\mathrm{interaction}}(t),
$$

where these are not assumed to be independently observable causal components. The decomposition is only a bookkeeping device for distinguishing:

- affect clearly associated with an identifiable external or represented context;
- affect generated or modulated by endogenous bodily/substrate state whose provenance is poorly resolved from inside;
- nonlinear interaction between the two.

The authorial report is approximately:

$$
\frac{|A_{\mathrm{substrate}}|}{|A_{\mathrm{context}}|}
\text{ felt large during development,}
$$

while later adulthood feels closer to:

$$
|A_{\mathrm{context}}| \gg |A_{\mathrm{substrate\ residual}}|,
$$

without claiming that the latter term vanishes.

This is a phenomenological statement first. Any biological story is downstream of it.

---

## 2. The biological correction: not "new neurons = noise"

The original intuition can be stated charitably:

> if the machinery of experience is still growing, then some portion of that machinery is not yet fully calibrated to the organism's accumulated information, so regulation may be noisier and affect may feel more ambient.

The useful part is the intuition that the **substrate itself is changing**. The weak part is identifying that change with large-scale ongoing production of blank cortical neurons.

A more defensible formulation is:

> childhood and adolescence involve continued reorganization and maturation of neural systems, including synaptic pruning and remodeling, myelination and white-matter development, changing long-range integration, pubertal/endocrine effects, and continuing maturation of affective and executive-control circuitry. Development is therefore a change in system organization and response-properties, not merely accumulation of fixed hardware.

This matters because learning and control theory distinguish a stationary plant from a nonstationary one.

For a stationary system, repeated observation can in principle improve the controller's model of the same underlying transfer function.

For a nonstationary system, the controller must simultaneously:

1. learn the present response map;
2. detect that the map has changed;
3. decide which errors come from bad modeling versus plant drift;
4. update without overfitting transient states;
5. continue acting while calibration is incomplete.

That is a qualitatively harder problem.

The TLICA translation is therefore **developmental substrate nonstationarity**, not "neural blankness."

---

## 3. Existing TLICA machinery already points here

### 3.1 Substrate dependence is already foundational

Current v5.5.0 defines the substrate as

$$
\mathsf{S}_m=(\mathsf{B}_m,\mathsf{E}_m,\chi_m),
$$

with focus capacity inherited through

$$
M_m(t)=\Gamma^M_m(\mathsf{S}_m,t).
$$

The architecture explicitly leaves the empirical mechanism of this dependence open. That is exactly the correct level at which developmental neuroscience can later enter: TLICA specifies dependency; domain science supplies implementation details.

### 3.2 Development already changes who drives focus

TLICA also writes

$$
\mathsf{Foc}_t^m
=
\mathsf{Foc}_t^m[\text{contact-driven}]
\oplus
\mathsf{Foc}_t^m[\text{self-directed}],
$$

with the first dominant early and the second increasing as lived-I structure accumulates.

This already says that the effective controller changes across development. Developmental substrate nonstationarity adds a second, orthogonal fact: **the plant being controlled may also be changing rapidly.**

The resulting picture is not merely

$$
\text{weak controller} \to \text{strong controller},
$$

but

$$
\boxed{
\text{controller learning}
\quad\text{while}\quad
\text{plant reconfigures}.
}
$$

### 3.3 Affect already arrives through the least source-legible pathway family

Current TLICA treats emotions and bodily sensations as canonical third-order contents:

$$
\mathsf{N}_m
\to
\mathsf{S}^{\mathrm{som}}_m
\to
\mathsf{S}^{\mathrm{cog}}_m
\to
\hat\iota_m.
$$

The architecture's point is not that emotion is irrational. It is that additional mediation and compression make affect characteristically high in intensity while often low in explicit source-resolution.

This gives developmental substrate nonstationarity a direct phenomenological route. If the somatic/cognitive substrate itself is changing, then the I can receive changed affective outputs without having an introspectively available representation of the changed transfer function that produced them.

The inside report is then naturally:

> "I feel different / strongly / badly / intensely, but I cannot cleanly say what in the world changed."

That is not evidence of causeless feeling. It is evidence of **source opacity**.

### 3.4 Osmotic imprinting means calibration never pauses

Osmotic imprinting is always online. The environment continuously patterns the substrate, although effective bandwidth and durable update can vary.

Development therefore contains two concurrent update streams:

$$
\text{world / body exposure} \to \text{osmotic rewriting of slow structure}
$$

and

$$
\text{developmental substrate change} \to \text{change in the machinery implementing that rewriting}.
$$

The system is not simply adding data to a fixed associative machine. The associative machine itself changes.

### 3.5 v5.5.0's `G` makes the coupling much clearer

The v5.5.0 actuator repair names a slow lived-I structure `G` that imprinting writes. Identity-correlation and the field-reading are downstream readings of that structure:

$$
\rho = R(G),
\qquad
f = F(G,\mathsf{A}).
$$

Mode B and osmotic imprinting both alter `G` from different source directions.

For this research note, the important distinction is:

- `G_t`: the slow learned / imprinted lived-I structure;
- `S_t^{\mathrm{eff}}`: the effective substrate state through which `G_t` is written, expressed, and read at time `t`.

`S_t^{eff}` is **application notation**, not a proposed new foundation object. It means "the time-indexed effective state of the already-existing substrate and its response-properties." One conservative notation is simply

$$
\mathsf{S}^{\mathrm{eff}}_m(t):=\operatorname{Eval}_t(\mathsf{S}_m),
$$

where `Eval` is deliberately left application-specific.

The field-reading can then be displayed, at application level, as

$$
f_t \sim F(G_t,\mathsf{A}_t;\mathsf{S}^{\mathrm{eff}}_m(t)),
$$

with the semicolon signaling "implemented/mediated through" rather than asserting a new foundation argument to `F`. A mainline integration must not silently change the foundation signature without a separate audit.

---

## 4. The moving-machine problem

Consider an agent learning a control policy `pi_t` for a plant with response map `P_t`.

If

$$
P_{t+1}\approx P_t,
$$

past calibration remains useful.

If instead

$$
P_{t+1}\not\approx P_t
$$

on the same timescale at which the controller is learning, then yesterday's good policy can become today's biased policy without any explicit failure of reasoning.

For a developing I, the relevant "plant" includes at least:

- affective responsivity;
- arousal regulation;
- salience gating;
- executive capacity;
- body-state dynamics;
- social reward sensitivity;
- the mapping from internal physiological state to conscious-fuzzy affect;
- the bandwidth available for self-directed control.

TLICA need not specify neural implementations to represent the control problem. It only needs to admit that the effective substrate parameters are time-dependent.

### 4.1 A timescale diagnostic

Define two application-level characteristic timescales:

- `tau_S(t)`: the timescale on which relevant substrate response-properties change appreciably;
- `tau_track(t)`: the timescale on which the I's learned structure / controller can detect, integrate, and compensate for such change.

Then define the **developmental tracking load**

$$
\eta_{\mathrm{dev}}(t)
:=
\frac{\tau_{\mathrm{track}}(t)}{\tau_S(t)}.
$$

Interpretation:

- `eta_dev << 1`: the I can track substrate drift faster than the substrate changes;
- `eta_dev ~ 1`: tracking and drift occur on comparable timescales;
- `eta_dev >> 1`: the substrate changes faster than the I can recalibrate.

This is not a TLICA coordinate. It is not a truth probability. It is not even defined until an application supplies operational measures for both timescales. Its purpose is to name the control problem cleanly enough to design discriminators.

### 4.2 What large tracking load would feel like

If `eta_dev` is high, several phenomenological signatures are plausible:

1. **Residual affect after frame change.** The cognitive interpretation changes faster than body-level response properties recalibrate.
2. **Weak return-address.** Affect arrives clearly as affect but with poor source resolution because the changed source is partly endogenous.
3. **Regulation policy staleness.** A strategy that previously worked becomes unreliable without an obvious reason.
4. **High context sensitivity plus unexplained residual.** External events still matter strongly, but their effect is multiplied or distorted by moving internal parameters.
5. **Identity lag.** The self-model describes yesterday's response system while today's substrate behaves differently.
6. **Contact dominance.** Exogenous salience wins more often because self-directed control is both less accumulated and calibrated against a moving plant.

None is unique to development. That non-uniqueness is useful: it creates rival explanations and testable contrasts rather than metaphysical immunity.

---

## 5. Root II changes interpretation under this model

The Self-Applied Architecture currently treats Root II as a high-gain affective parameter: ordinary inputs can produce unusually large affective output in both valences.

That account should not be discarded. The present refinement suggests a regime interaction:

$$
\boxed{
\text{high affective gain}
\times
\text{high substrate nonstationarity}
\times
\text{young / low-bandwidth self-regulation}
}
$$

may produce a very different phenomenology from

$$
\boxed{
\text{high affective gain}
\times
\text{lower relative substrate drift}
\times
\text{mature accumulated self-regulation}.
}
$$

The same Root II can therefore survive while the *experienced form* of Root II changes.

This is important because the adult report is not "I stopped feeling strongly." It is closer to:

> "I still feel strongly, but the feeling now usually has a legible context instead of acting as a standing background field."

That is better modeled as a regime shift in gain-plus-tracking than as disappearance of the gain parameter.

---

## 6. Baseline buzzing as a source-map problem

TLICA's affective epistemics already distinguishes signal content from signal provenance.

Developmental nonstationarity extends that insight:

$$
\text{real affective signal}
\not\Rightarrow
\text{correctly identified external return-address}.
$$

Suppose a social event produces a modest perturbation `x`, while developmental substrate state contributes an endogenous modulation `s_t`. The experienced affective output may be schematically

$$
y_t = H_t(x_t,s_t,G_t),
$$

where `H_t` is itself changing.

The I does not introspect `H_t` directly. It receives `y_t`.

If `y_t` is intense and the immediately visible candidate cause is `x_t`, a natural inference is:

> "the situation is this emotionally large."

But a more accurate outside-perspective account might be:

> "the situation is real, and the response is real, but part of the response amplitude and persistence came from endogenous state plus a changing transfer function."

This gives a precise TLICA form to the phrase **baseline buzzing coupling to reality**. The world is not irrelevant. Rather, the world becomes the visible carrier of affect whose full provenance includes less-visible substrate dynamics.

---

## 7. Adulthood as relative stabilization, not completion

The model must avoid an obvious error: adulthood is not a fixed point at which neural plasticity or bodily change stops.

A better statement is relational:

> adulthood may, for some relevant processes and some individuals, reduce the rate of developmental reconfiguration enough relative to accumulated modeling and regulatory capacity that the self can track its own response system more successfully.

In the timescale notation:

$$
\eta_{\mathrm{dev}}(t)
\downarrow
$$

can happen because:

- `tau_S` increases: relevant substrate properties change more slowly;
- `tau_track` decreases: the I becomes faster/better at modeling and regulating;
- or both.

This is why "brain maturation" alone is insufficient. The phenomenological change is a **ratio phenomenon** between plant drift and controller adaptation.

An adult can still re-enter a high-nonstationarity regime through illness, major endocrine change, sleep disruption, acute stress, medication effects, substance effects, injury, or other physiological transitions. The theory therefore predicts regime recurrence in principle rather than tying the phenomenon metaphysically to chronological youth.

That recurrence prediction is useful because it is falsifiable.

---

## 8. Depression, suppression, and recovery are not optional confounds

The author's trajectory contains a major complication:

$$
\text{developmental high-gain affect}
\to
\text{depression / broad suppression}
\to
\text{reduced feeling}
\to
\text{later regeneration of affect}.
$$

This prevents a simple age-only story.

At least four live models must be kept separate.

### H1 — High gain only

Root II is stable across development. Childhood felt more intense because memories overrepresent salient extremes or because contexts were objectively more destabilizing. No developmental substrate mechanism is needed.

### H2 — Developmental substrate nonstationarity

Root II interacts with high developmental tracking load. As substrate drift slows and self-modeling improves, affect becomes more context-resolved.

### H3 — Acquired-regulation / depression-history model

The major transition is not ordinary maturation but what was learned through depression, suppression, treatment, recovery, and repeated attempts to manage affect. Adult context-resolution is an acquired regulator.

### H4 — Coupled model

Ordinary developmental stabilization lowered background plant drift **and** the depression/recovery arc radically retrained `G` and the available regulatory policy. Neither alone explains the final phenotype.

This dossier treats H4 as the most structurally complete candidate, but **not as established**.

### 8.1 A useful discriminator already present in the trajectory

A crude permanent-blunting model predicts:

$$
\text{less ambient affect in adulthood}
\quad\text{because}\quad
\text{affective capacity stayed suppressed}.
$$

But the reported present state is instead:

$$
\text{affect returned}
\quad+
\text{context resolution remained improved}.
$$

If that report survives timeline audit, it weakens the simplest permanent-blunting explanation.

It does **not** separate H2 from H3 or H4. That debt remains.

---

## 9. Why this may matter beyond autobiography

The general architectural claim is modest but potentially useful:

> a developmental theory of self-regulation should distinguish learning *within* a substrate from learning *while the substrate itself changes*.

That distinction could clarify several otherwise conflated phenomena:

- why a child can possess a reflective capacity yet fail to deploy it reliably;
- why the same environmental input can have different affective impact at different developmental stages;
- why emotion can be both genuine and poorly source-resolved;
- why regulation strategies may have stage-dependent effectiveness;
- why apparently abrupt personality or affective changes can emerge without a corresponding explicit belief change;
- why maturation can feel like a change in the *texture of being affected*, not merely an increase in knowledge.

The broad form is compatible with developmental neuroscience, allostatic control, adaptive filtering, active inference, and nonstationary system identification. TLICA's possible contribution is not discovering those literatures. It is providing a first-person architectural vocabulary that keeps substrate, source-opacity, self-structure, identity-correlation, and reflexive control in one typed picture.

---

## 10. What would make this more than a story

The preferred frame must pay truth debt.

The central discriminating question is:

> does the developmental-substrate model explain data that high-gain-only, regulation-learning-only, and retrospective-memory models do not?

The next probes are specified in `CLAIM_LEDGER_AND_PROBES.md`. The most important are:

1. **timeline reconstruction** from contemporaneous records rather than current memory alone;
2. **source-resolution coding**: for strong affective episodes, was there a specific precipitant, and did affect persistence outlast the explicit frame?
3. **adult natural experiments** involving naturally occurring physiological nonstationarity, without inducing harm, to see whether "baseline buzzing" can recur outside youth;
4. **recovery discriminator**: determine whether strong affect genuinely returned while ambient/source-opaque affect stayed reduced;
5. **literature-level test**: whether longitudinal developmental data support declining affective variability / improving regulation strongly enough to make the proposed direction plausible while preserving large individual heterogeneity;
6. **formal toy model**: a controller learning a changing transfer function versus a fixed one, showing which residual patterns are unique to plant drift rather than high gain.

If those probes fail, this note should contract back to a phenomenological observation with no privileged developmental mechanism.

---

## 11. Claim ledger summary

- **OBSERVED (author report):** developmental years carried more ambient / baseline-coupled affect; adulthood is more context-resolved.
- **CORROBORATED (domain science):** childhood/adolescence involve substantial continuing neural and endocrine reorganization; affect regulation and executive/affective control continue developing across adolescence and into young adulthood.
- **REFUTED AS STATED:** widespread continual addition of blank cortical neurons is not an adequate centerpiece mechanism.
- **CONJECTURED:** substrate nonstationarity contributed to the author's developmental background affect and source-opacity.
- **CONJECTURED:** Root II is better modeled as a stable-ish high-gain constraint expressed in different dynamical regimes than as a parameter that simply disappeared.
- **UNVERIFIED:** the proposed developmental tracking-load ratio explains a measurable portion of the phenomenological transition.
- **UNVERIFIED:** the coupled H4 model dominates H2/H3 after timeline and provenance audit.
- **DARK:** a one-to-one mapping from TLICA's `S`, `G`, `f`, `tau`, and slack variables to specific neural processes. No such mapping is claimed.

---

## 12. Proposed application-level language for eventual integration

A concise prose block suitable for *The Self-Applied Architecture*, after audit, is:

> **Developmental substrate nonstationarity.** Root II did not act on a fixed machine. During childhood, adolescence, and early adulthood, the substrate through which affect, salience, focus, and self-regulation were implemented was itself undergoing substantial developmental reorganization. The relevant hypothesis is not that new blank neurons continuously injected random noise; it is that the response map being learned was moving while it was being learned. In TLICA terms, accumulated lived-I structure was trying to regulate through a substrate whose effective parameters were still changing, while affect arrived through a third-order pathway that is already characteristically source-opaque. The resulting phenomenology can therefore be high-gain in two senses at once: ordinary contexts are amplified, and endogenous substrate drift contributes a poorly addressed background component that the visible context is then recruited to explain. Adulthood need not mean the substrate stopped changing. It need only mean that substrate change became slower relative to the self's accumulated capacity to track and regulate it. The author's present report — strong affect that is now predominantly context-resolved rather than continuously ambient — is consistent with that regime shift, but does not by itself distinguish maturation from acquired regulation through the depression/recovery arc. That causal split remains open.

This block should remain application-level unless a separate foundation audit shows that TLICA itself needs an explicit nonstationary-substrate clause.

---

## 13. Boundary

The note makes a structural claim about a possible relation between developmental change and lived phenomenology. It is not medical advice, diagnosis, or a claim that any individual's emotional history can be read directly from age. Developmental neuroscience supplies constraints on plausible mechanisms; it does not certify the autobiographical causal reconstruction.
