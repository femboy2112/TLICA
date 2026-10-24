# TLICA–HIGGS V: Self-centered frame scattering, weak-edge exchange and accidental osmotic imprinting

**Date:** 2026-10-22. **Origin:** Author Leah, following the causal Feynman/Wick diagrams. Mathematical elaboration by ChatGPT GPT-6.  
**Status:** research-only proposal; conditional mathematics **DISCLOSED within the declared toy**; phenomenological mechanism and actual neural/psychological causes **CONJECTURED / UNVERIFIED**. No modification of the TLICA foundation.  
**Figure:** [frame_scattering_imprinting.svg](frame_scattering_imprinting.svg) (editable causal-vertex schematic).  
**Witness:** [frame_scattering_imprinting_witness.py](frame_scattering_imprinting_witness.py), 21 locally executed deterministic tests of the finite toy (not empirical validation).

## 0. Author seed and actual question

> "For imprinting, it helps to think of the current frame the self is in as a kind of self-centered (mathematically speaking) orientation. In that sense, because of what you happen to hold dear relatively speaking at the moment, you can think of the interactions at the weak edges (really everywhere but notably there) almost like a feynman diagram where two charged particles come close, exchange a virtual particle/energy, and change trajectories. The imprinting is essentially the background noise of the world being accidentally encoded by your frame/focus"

This builds on [causal Feynman/Wick diagrams](CAUSAL_FEYNMAN_DIAGRAMS_2026-10-22.md) by adding the **missing slow-imprinting vertex**. The strong intuition is not that the self floats in a real Higgs field, but that a *local, historically formed interpretation frame filters environmental encounters, and apparently incidental encounters can permanently modify the connections through which later encounters will be interpreted*.

A momentary interaction and an enduring changed edge are separate causal events. The experiment is to specify the intermediate encoding update and derive something falsifiable.

## 1. Recover existing foundation; no invented imprinting primitive

[TLICA File 3, §§8.1–8.7](../../foundation/3_formal_apparatus.md) already specifies:
- substrate-bounded attention/focus; contact and attention choose effective access paths;
- focused update events $e=(s,u,v,k,\alpha,\beta)$, with $\alpha,\beta$ determined by focus and contact;
- **osmotic imprinting**: substrate-level associative pattern formation from recurring ambient co-occurrences, including situations where the association itself is not explicitly attended to, and without verification;
- imprinting **formation** differs from later **activation**;
- the osmotic mechanism remains available continually, but this does **not** mean every time interval necessarily imprints a measurable amount;
- first/second/third-order substrate pathways are dominant-route classifications, not exclusive kinds.

The actual §8.4 edge update is:

$$
w^+ =\Pi_{[0,1]}\left((1-\beta)w^-+\alpha(1-w^-)\right).
\tag{1}
$$

Within $0\le w,\alpha,\beta\le1$, the projection is inert and:
$$
\Delta w=\alpha(1-w)-\beta w,\qquad
\frac{\partial w^+}{\partial\alpha}=1-w,\qquad
\frac{\partial w^+}{\partial\beta}=-w.
\tag{2}
$$

**Weak-edge result:** for a fixed $\alpha$ increment at otherwise fixed $w,\beta$, an edge near $w=0$ has greater reinforcement room than an edge near $w=1$. This is a sensitivity identity, **not** a universal claim that the least-connected real neurons or social referents are always the most plastic. The chance of reinforcement itself may be very low for poorly contacted weak edges.

### Typed vocabulary

- $G_{m,t}$: TLICA's slow lived-I structure.
- $w_e(t)$: a specific *substrate association edge weight* within the chosen type $e=(u,v,k)$; not the whole $\rho$-profile, and not preservation-ranking $\Pi$.
- $\mathcal F_{m,G}$: a candidate **self-centered coordinate chart** mapping a world encounter via the substrate to a local experienced/encoded feature $z_e$. “Self-centered” means indexed to the actual modeling I, not egoism.
- $\mathsf{Foc}_t$: attention allocation; does not exhaust osmotic ambient processing.
- $J_e(\mathsf{Foc},\kappa,z_e)$: proposed exposure gate including a focus-related part and a non-focused osmotic part. Do not reduce its amplitude to $\rho$, $\Pi$, or truth.
- $\Pi_{m,t}$: TLICA's *separate* situational preservation-ranking, relevant for prioritizing later behavior, **not** identical to structural identity integration $\rho$.

An arbitrary $\mathcal F$ or $J_e$ fitted after observing outcomes can explain everything and predict nothing. Declare transport and observation maps and use holdouts.

## 2. Finite event-scattering model: accidental learning from random co-occurrence

Let $I_n\in\{0,1\}$ denote whether a substrate-recognized co-occurrence is recorded at step $n$; assume **independent Bernoulli** draws with probability $p$ for this deliberately simple null world. The event itself is **not** evidence of real association or objective meaning.

Define a conditional special case of (1):
- event $I_n=1$: $\alpha=a\in[0,1]$, $\beta=0$;
- non-event $I_n=0$: $\alpha=0$, $\beta=b\in[0,1]$.

Then:
$$
w_{n+1} =
\begin{cases}
w_n+a(1-w_n)&I_n=1,\\
(1-b)w_n&I_n=0.
\end{cases}
\tag{3}
$$

The expected recurrence is **exact** because $I_n$ is independent of the existing $w_n$:
$$
m_{n+1}=(1-r)m_n+pa,\quad
m_n=\mathbb E[w_n],\quad r=pa+(1-p)b.
\tag{4}
$$
When $r>0$,
$$
\boxed{
m_n=w_*+(m_0-w_*)(1-r)^n,\quad
w_*=\frac{pa}{pa+(1-p)b}.
}
\tag{5}
$$

**Toy witness:** $p=0.1,\ a=0.1,\ b=0.01,\ m_0=0$. Then $w_*=0.526315789$. After 200 events the expectation is ~0.51496. Random encounters with no true semantic relation can therefore create a persistent expected association **under this reinforcement/decay rule**.

This is not universal stochastic learning: different selection, reward, forgetting, novelty suppression, or source-validation rules can prevent it. It does not establish a human's false belief or psychiatric condition.

## 3. Frame/focus changes which noise enters the update

Let raw environmental types $+$ and $-$ have a known base rate $\Pr(+)=\Pr(-)=1/2$. Suppose a frame/focus gate admits a $+$ encounter with probability $0.8$ and a $-$ encounter with probability $0.2$. Bayes yields:
$$
\Pr(+\mid \mathrm{admitted})
=\frac{(1/2)(0.8)}{(1/2)(0.8)+(1/2)(0.2)}
=0.8.
\tag{6}
$$

**The world distribution did not change. The distribution of admitted experiences did.**

This is a toy demonstration of **frame-conditioned sampling**, not evidence that self-identified groups literally see particular world frequencies. It provides a mechanism by which an observer-indexed frame can *select which ambient coincidences receive substrate reinforcement*. A focus-independent osmotic gate can remain nonzero even if the person was not deliberately attending to the event. Never confuse observer-relative representation with metaphysical creation of external events.

Important rival: the environment could itself be asymmetric; do not blame “frame bias” without measuring base rates and contact.

## 4. Genuine classical loop: fast noise can yield slow drift

The [previous causal diagram paper](CAUSAL_FEYNMAN_DIAGRAMS_2026-10-22.md) developed retarded response propagators and Gaussian covariance contractions. Here the relevant diagram has a new slow edge-write vertex.

Let $q(t)$ be an Ornstein–Uhlenbeck fast bath process with zero mean and stationary variance $\langle q^2\rangle=C_q(t,t)=D/K$ for $K>0,D\ge0$. Posit a **new slow toy** that preserves $w\in[0,1]$:
$$
\boxed{
\dot w=\varepsilon\bigl[a(1-w)q(t)^2-bw\bigr],
\quad a,b>0,\quad 0<\varepsilon\ll K.
}
\tag{7}
$$

At boundaries $w=0,1$, the drift points inward or tangent, so the range is preserved when initialized in it. The essential response-field vertex in an MSRJD analogue is
$$
-\varepsilon a\,\widetilde w(1-w)q^2.
$$
Wick contraction of the two **fast Gaussian $q$ legs** produces a noise tadpole:
$$
\langle q(t)q(t)\rangle_0=C_q(t,t)=D/K.
\tag{8}
$$

In the timescale-separated leading averaged approximation (not an exact all-time conditional expectation):
$$
\dot{\bar w}\simeq\varepsilon\left[a(1-\bar w)\frac DK-b\bar w\right],
\qquad
w_{\rm averaged}^*=\frac{aD/K}{aD/K+b}.
\tag{9}
$$

This is a real **diagrammatic coefficient** in a defined stochastic toy:
$$
\text{zero-mean fast fluctuations}\to\text{nonzero second moment}\to
\text{slow association formation}.
$$

**Critical distinction:** the loop is a *Gaussian covariance contraction*, not a literal virtual particle, a packet of conserved energy, a mind "emitting a Higgs," or evidence that human learning follows a quadratic law. Its nonzero effect is tied to the chosen nonlinear vertex $q^2$. If the update instead depended linearly on zero-mean $q$ with no selection/other nonlinearity, this first-moment drift would not follow. If the learning mechanism subtracts the reference noise variance $q^2-D/K$, the leading noise-only drift also cancels.

## 5. Actual two-way scattering is a distinct hypothesis

A single ambient exposure can alter $w$ while leaving the world unchanged. That is an **open-system, one-way driven update**; it need not be represented as two equal and opposite particles recoiling.

A genuine two-way exchange could be modeled with both:
- environment $\to$ represented encounter $\to$ response/imprint;
- agent behavior $\to$ environmental change $\to$ subsequent exposure.

For example a linear local two-mode toy:
$$
\frac d{dt}\begin{pmatrix}s\\z\end{pmatrix} =
\begin{pmatrix}-k_s&g\\h&-k_z\end{pmatrix}
\begin{pmatrix}s\\z\end{pmatrix}+J+\xi.
\tag{10}
$$
Here $g,h$ are **declared reciprocal response couplings** and $s,z$ are defined environmental/self response variables, not particles. $h=0$ gives a one-directional subcase; $g,h\ne0$ allows mutual alteration. Stable linear response requires conditions on trace and determinant (for $k_s,k_z>0$, $k_sk_z>gh$).

The word **virtual exchange** is an analogy to an *internal propagator in a diagrammatic expansion*. In real QFT, a virtual particle is not a directly observed traveling energy packet; physical energy-momentum conservation holds at the complete interaction, and should not be transplanted into a model of social interactions. No automatic Newtonian equal-and-opposite reaction is imposed on a social world-self system.

## 6. What makes the weak edges special

The old foundation rule yields formation sensitivity $1-w$, while contact and focus determine exposure probabilities. Their product matters:
$$
\underbrace{\Pr(\text{encounter is recorded}\mid e,\mathcal F,\mathsf{Foc})}_{\text{contact / attention selection}}
\times
\underbrace{a_e(1-w_e)}_{\text{formation capacity}}.
$$

Thus maximum imprinting **need not** occur at the mathematically weakest edge; a completely uncontacted edge can remain unchanged. Low established strength combined with occasional salient or osmotically registered contact is the interesting transition regime.

There is a second opportunity for selection: early accidental associations change future attention/focus gating, which changes the sample of environmental events admitted later. This can form a feedback loop:
$$
\text{frame}\to\text{filtered ambient sampling}\to\Delta w
\to\text{changed future gate}\to\text{further sampling}.
$$
That loop requires an independently specified gate-update rule; it is **not derived automatically** from Eq. (1).

## 7. Relation to PCE, identity, truth, and source provenance

Self-centered means index-relative. It does not assert the current frame is true, morally privileged, or universally applicable.

- $\rho$ is **identity integration**, not the priority for preservation.
- $\Pi$ is **preservation-ranking**, not how frequently an environmental event occurs.
- PtCns is the frame-relative consistency response, not a validated causal detector.
- $\kappa$ and focus govern encountered/captured contents; osmotic imprinting may occur even without explicit focus.
- $\varphi$ is relative to the available verification toolkit; $\sigma$ source-map adequacy is separate. An acquired association can be salient with poor provenance and without being true.
- Accidentally encoded environmental statistics can support useful competence *or* false beliefs; the diagram cannot decide which without a world-level discriminator.

**Terminological firewall:** No actual gauge group, Hilbert-space phase, field quanta, conserved social energy, or empirical neurophysiology is established here.

## 8. Discriminating probes and negative controls

**Main question:** Does an observer-specific gating history predict *which initially weak associations become durable* after incidental exposures, above frequency and reinforcement alone?

A safe experiment would use harmless invented categories and random co-occurrence pairs, with nondeceptive consent and clear debriefing. First elicit or randomize attention orientation; present a calibrated base rate of coincidences, including exposures where the target is not intentionally focused; use holdout pairs after a delay. Measure actual attention if possible and separate remembering an event from enduring associative bias.

Rivals:
- no implicit association formation; retention only when actively attended;
- general frequency learning independent of observer frame;
- selective sampling driven by explicit attention;
- incidental osmotic updates even when the target relation was not attended;
- simple memory, reward, expectation, or exposure effects without the posited slow $G$-writing.

**Pass (limited model support):** independently specified frame/focus/contact gates and initial weak-edge status predict held-out updates beyond null frequency and reward models, with a delayed persistence result.
**Fail:** effects vanish under base-rate and attention controls; weak edges are not more susceptible under matched effective reinforcement; no durable change.
**Ambiguous:** base rates uncontrolled, no suitable edge proxy, learning/retention conflated, non-stationary environment, or no independent measures of focus.

Controls:
1. No exposure (null), no reinforcement, zero-noise baseline.
2. True statistical relation (positive) vs randomly paired cues (negative/false-coincidence control).
3. Balanced source distribution with equal vs unequal focus selection.
4. Already-strong vs weak association at matched contact rates.
5. Mutation: reverse which signal receives attention while keeping environmental statistics identical.
6. Delayed new cues/holdout context and source-memory checks.

**Status ledger:**
- Eq. (1) and osmotic-imprinting distinction: **OBSERVED in TLICA foundation**.
- Eqs. (2), (4), (5), and (6): **DISCLOSED conditional finite algebra**.
- Gaussian contraction and leading averaged drift: **DISCLOSED in declared stochastic toy**, not exact human dynamics.
- The claim that real weak psychological associations undergo this precise process: **CONJECTURED / UNVERIFIED**.
- The claim that "virtual particle exchange" physically happens in a self during social experience: **NOT WARRANTED**.

**Bottom line:** Interaction may be momentary, while the frame-conditioned edge update becomes part of the next encounter's initial conditions. The self need not intentionally assent to the association; being situated in the world already exposes the substrate to a continuing stream of candidate imprints.
