# The First Atomic Connection

## Grokking as Toolkit Closure from Local Paths to Global Structure

**Status:** Research paper / formal hypothesis dossier, v0.1  
**Date:** 2026-08-29  
**Branch:** `research/grokking-toolkit-closure-2026-08-29`  
**Authorial provenance:** The core phenomenological thesis, the *Matrix* mapping, the distinction between the enabling transition and grokking proper, and the possibility of "nerf-grokking" in a degenerate space originate with Leah. The formalization, literature differential, and experiment design are AI-assisted.  
**Foundation impact:** none. This paper applies and extends application-level toolkit language; it does **not** modify the frozen TLICA foundation.  
**Epistemic status:** the TLICA derivation is disclosed relative to the archive; the proposed human-machine structural homology is **CONJECTURED**; the bridge-topology mechanism is formally exact in the toy model and **UNVERIFIED** as a general account of neural or human grokking.  
**Companion protocol:** [`grokking_toolkit_closure_experiment_protocol_2026-08-29.md`](grokking_toolkit_closure_experiment_protocol_2026-08-29.md)

---

## Abstract

Grokking in machine learning is the delayed transition from fitting or memorizing training data to generalizing a rule beyond those data. Subjectively, human understanding can exhibit a related shape: a learner first acquires many difficult, locally useful procedures; those procedures eventually cover much of the experienced field; performance plateaus; then an apparently small connection reveals that the local procedures are instances or coordinates of a larger structure. The learner no longer traverses the field primarily by recalling disconnected routes. The learner can compose, transport, and recombine internalized subpaths into new valid movement.

This paper proposes a TLICA-compatible account of that transition. Learning begins as **local path acquisition**. A plateau can occur when local paths cover familiar cases while remaining mutually fragmented. A **nucleation / availability boundary** occurs when a globally extensible organization becomes constructible from the current toolkit: grokking becomes an available developmental route. This boundary is not grokking proper. Grokking proper is the subsequent growth, alignment, cleanup, and eventual dominance of the global organization. Behavioral generalization appears when that organization controls performance strongly enough to beat or replace the memorizing/local-path solution.

The proposal reconciles three observations that otherwise pull apart: grokking looks behaviorally abrupt; mechanistic work finds gradual internal progress before the jump; and both human "Aha!" phenomenology and machine test accuracy can fail to coincide with the actual representational transition. We formalize the learner's current tools as a compositional closure, local solutions as partial sections over task regions, and grokking as a gluing problem. A connected-overlap theorem for an opaque modular-addition task shows exactly how disconnected evidence leaves independent gauge freedoms between locally solved components. Each valid bridge removes a factor of ambiguity. This yields a precise form of **nerf-grokking**: a task, data distribution, toolkit, architecture, or optimization process can permit extensive local mastery while making global closure unidentifiable, unconstructible, inaccessible, or permanently non-dominant.

The central claim is therefore not that human insight and neural-network grokking share a microscopic mechanism. It is that they may instantiate the same abstract learning topology:

$$
\boxed{
\text{local paths}
\to
\text{coverage without unity}
\to
\text{closure nucleation}
\to
\text{global compositional traversal}
\to
\text{generalization}.
}
$$

The decisive experiment holds model, sample count, token frequency, and local learnability approximately fixed while changing only the topology of the evidence connecting local subproblems. If a small number of valid bridge examples causes a disproportionate change in time-to-grok, while degree-matched disconnected and corrupted-bridge controls do not, the closure account gains explanatory content beyond the metaphor.

---

## 0. Executive thesis

The proposed distinction is:

$$
\boxed{
\text{The event that makes grokking possible is not yet grokking proper.}
}
$$

Before the enabling event, the learner may possess many successful local procedures but no constructible route by which they become one globally usable structure. At the enabling event, a coherent continuation first becomes available. After that event, learning can proceed by reorganizing, aligning, compressing, and composing what has already been acquired.

Let

- $t_{\mathrm{mem}}$ be the time at which familiar/training cases are effectively mastered;
- $t_\star$ be the **nucleation / availability boundary**, when a globally extensible organization first becomes a live constructible option;
- $t_{\mathrm{grok}}$ be the behavioral transition, when the global organization controls held-out performance;
- $t_{\mathrm{sat}}$ be stable post-transition mastery.

The invariant ordering proposed here is

$$
t_\star
\leq
t_{\mathrm{grok}}
\leq
t_{\mathrm{sat}}.
$$

In the canonical delayed-grokking sequence emphasized in this paper,

$$
t_{\mathrm{mem}}
\lesssim
t_\star,
$$

because local mastery and its plateau precede the enabling transition. This is not made definitional: a weak global circuit may begin to nucleate before complete memorization in some systems. The load-bearing distinction is that $t_\star$ can precede behavioral disclosure at $t_{\mathrm{grok}}$.

The Trinity kiss in *The Matrix*, the first atomic connection in a human learner, and the derivative change in a latent machine progress measure are all proposed as images or markers of $t_\star$. They mark the point at which the global route begins to exist as an option. They do not by themselves establish that the route has finished propagating, won the competition with local memorization, transferred out of distribution, or become stable.

This paper's compressed thesis is:

> Learning initially grows mainly by adding paths. Grokking becomes possible when the paths acquire enough shared structure to close under valid composition. Grokking proper is the propagation and dominance of that closure.

---

## 1. The motivating phenomenology

### 1.1 The learner before grokking

A difficult field initially presents as a high-cost search space. The learner cannot move freely through it. Progress consists in learning bounded routes:

- this manipulation works for this equation shape;
- this visual cue predicts this move;
- this proof trick resolves this family;
- this phrase, example, or memory retrieves this answer;
- this local circuit maps this training pattern to this output.

Each route reduces the cost of a particular traversal. The field becomes easier, but only piecewise.

A learner can therefore become impressive without becoming globally free. The local atlas may be dense enough that familiar situations almost always fall inside some known chart. From the outside, this can look like understanding. Yet a slight change of coordinates, a novel combination, or a gap between charts reveals that the competence is still route-bound.

### 1.2 The plateau

As local routes accumulate, their marginal benefit falls. Familiar-case performance approaches saturation:

$$
\frac{d}{dt}P_{\mathrm{familiar}}(t)\approx 0.
$$

The plateau does not imply that learning has stopped. It can mean that the visible metric has stopped resolving the internal change that now matters. The learner may be:

- aligning representations;
- discovering overlap relations;
- reducing incompatible local conventions;
- compressing redundant paths;
- strengthening a weak global circuit;
- learning when one operator can be transported into another region;
- suppressing a memorizing solution that still wins behaviorally.

The visible field is covered, but its coverage has not yet become one navigable object.

### 1.3 The first atomic connection

The proposed nucleation event is often small in content but large in consequence. Two previously separate procedures are recognized as sharing a generator, invariant, coordinate system, or compositional relation.

The event can take the form:

$$
p_i
\quad\text{and}\quad
p_j
\quad\longrightarrow\quad
\text{both are generated by }g.
$$

or

$$
p_j
=
T_{ij}\,p_i
$$

for a newly available transport $T_{ij}$.

The learner has not yet traversed the whole field globally. What has changed is more basic: a global traversal is no longer absent from the learner's closure. The first atomic connection can seed an expanding coherent component.

Phenomenologically, this is the point at which one stops seeing merely another fact and starts seeing the **kind of relation by which facts belong together**.

### 1.4 Grokking proper

After nucleation, the learner begins using local knowledge differently. Existing paths become operands rather than endpoints. The learner forms valid compositions that were previously unavailable:

$$
p_{i_1}\circ p_{i_2}\circ\cdots\circ p_{i_r},
$$

or, in a declared vector or Fourier basis,

$$
\sum_k \alpha_k p_k.
$$

The qualification matters. "Linear combination" is literal only where a common linear structure and transport have been specified. In a general cognitive or computational field, the correct term is **admissible composition**. The closure may be categorical, logical, algorithmic, geometric, linguistic, or dynamical rather than linear.

The hallmark of grokking is not simply that more cases can be answered. It is that novel cases become coordinates, compositions, or orbit points of an internalized structure rather than isolated cases demanding fresh memorization.

---

## 2. *The Matrix* as an expository model

*The Matrix* is used here as a phenomenological illustration, not empirical evidence.

Neo's development is not presented as one monotone increase in speed or force. Before the final transition he acquires many locally powerful capacities:

- he learns the rules of the simulated environment;
- he moves beyond ordinary human expectations during training;
- he can fight an Agent unusually well;
- he survives situations that would previously have been impossible;
- yet he fails the first rooftop jump;
- and local victories do not alter the fact that the Agent is generated by the surrounding system.

This is local path acquisition with incomplete field closure. Neo can traverse more of the environment, but he still treats the environment's objects and constraints as primary objects.

The death / Trinity-kiss sequence functions narratively as a nucleation boundary. It is not best read, for present purposes, as an extra fact being added to Neo's memory. It marks the point at which a different relation to the field becomes possible.

The decisive image comes immediately afterward: Neo sees the Matrix as code. The bullets, hallway, body, and Agent cease to be independent obstacles. They are expressions in a common generating representation.

The structural translation is:

| Narrative event | Closure interpretation |
|---|---|
| Training with Morpheus | Acquisition and optimization of local operators |
| Superior speed and combat | Lower traversal cost inside learned subspaces |
| Failed rooftop jump | Failure of transport across a chart boundary |
| Strong fight against Smith | Dense local coverage can approximate mastery |
| Smith's return | A local win does not control the generator of the environment |
| Death / Trinity kiss | Narrative marker of the nucleation / availability boundary $t_\star$ |
| Seeing code | Access to a common generative representation |
| Stopping bullets | Old high-cost operations become low-cost in the new basis |
| Entering Smith rather than merely striking him | Acting on the generator rather than only on generated instances |

The central difference is:

$$
\text{How do I dodge this bullet?}
\quad\longrightarrow\quad
\text{What is a bullet in the generating representation?}
$$

Neo does not finally memorize every move. He learns what a move is relative to the field.

---

## 3. Where the proposal touches TLICA

### 3.1 Verification-tool imprinting

The frozen foundation treats access to intrinsic structure as developmental rather than automatically given. A cogniting I acquires verification tools through encounter; substrate-level proto-patterns can precede explicit accessibility; and a gradual arc leads from repeated encounter to deployable tools. See Section 3.2, File 2: [`2_access_and_development.md`](../foundation/2_access_and_development.md).

The present paper generalizes the application-level image without changing the foundation:

$$
\text{encounter}
\to
\text{proto-path}
\to
\text{stable local operator}
\to
\text{composable toolkit element}.
$$

### 3.2 Shadow encounter

Section 3.3, File 2 already describes a form of shadow encounter in which several known patterns are recognized as aspects of one higher-level organization. It explicitly allows the recognition to arise through combinatorial action on already possessed tools. This is the closest existing foundation commitment to the present proposal.

The proposed grokking transition is a large-scale developmental version:

$$
\{\tau_1,\tau_2,\ldots,\tau_n\}
\quad\longrightarrow\quad
\text{recognition of the relations that organize the }\tau_i.
$$

The novelty is not the bare claim that known things can be combined. It is the attempt to specify the topology and thresholds of the transition from local coverage to global reusable structure.

### 3.3 Mode B and meta-reasoning

Mode B permits the I to turn attention onto accumulated structure. It cannot operate on an empty toolkit; there must be something to inspect and recombine. In human mathematical or conceptual grokking, Mode B is therefore a plausible route by which local tools become objects of a higher-order operation.

This does not imply that every grokking event is consciously meta-reasoned. Osmotic/substrate learning may establish compatibility before explicit recognition. The conscious "I see it" event may reveal a reorganization already under way.

### 3.4 Relation to acquired taste

The research note [`acquired_taste_toolkit_shape_2026-08-27.md`](acquired_taste_toolkit_shape_2026-08-27.md) introduced an application-level distinction between a fixed world's complexity and the complexity accessible under a time-indexed toolkit. It described representational unfolding, toolkit closure, and a stimulus changing from a coarse undifferentiated object into a factorable one.

The grokking proposal is a structural sibling:

$$
\text{opaque field}
\to
\text{local discriminations and routes}
\to
\text{factorable relational geometry}
\to
\text{compositional movement}.
$$

Acquired taste emphasizes richer resolution of one object family. Grokking emphasizes closure and transport across a task field.

### 3.5 No coordinate collapse

The proposal must not collapse TLICA's diagnostics.

For a human I, grokking may alter the verification toolkit and therefore make a previously undefined or long $\phi$-pathway constructible or shorter. But grokking is not identical to $\phi$, and no new scalar "understanding score" is introduced.

Track separately:

- toolkit contents and closure;
- phenomenal availability;
- objective transfer/generalization;
- source-map adequacy;
- probe availability;
- $\kappa$, $\phi$, and $\rho$ where TLICA actually licenses them.

An LLM is not assigned TLICA's I-relative coordinates merely because it groks a task. This paper proposes a substrate-agnostic structural comparison, not an argument that the model is conscious or possesses a lived I.

---

## 4. Empirical constraints from grokking research

Any viable account must survive the following observations.

### 4.1 Delayed generalization after memorization

Power et al. introduced grokking as a regime in which a model fits the finite training set, often to near perfection, while test performance remains near chance and then improves only after much additional optimization. This establishes the behavioral shape but does not by itself identify the internal transition.

### 4.2 The apparent jump can contain gradual internal progress

Nanda et al. reverse-engineered a modular-addition transformer using Fourier representations and divided training into memorization, circuit formation, and cleanup. Structured mechanisms strengthen before the visible generalization jump; later, memorizing components are removed or weakened.

This directly rules out a universal account in which the global algorithm is born at the exact checkpoint where test accuracy rises.

### 4.3 Algorithmic structure can precede successful generalization

Swaroop's 2026 ReLU-MLP study reports task-relevant Fourier phase relations even in models that do not themselves grok; idealized networks reconstructed from those latent frequencies and phases can generalize far better than the original noisy network. This is preprint evidence and should not be treated as settled, but it strengthens the distinction between **latent structural availability** and **behavioral deployment**.

### 4.4 The same inference route can exist before and after grokking

He et al. report that non-grokked and grokked parameter-sharing transformers can use the same in-distribution compositional inference path. They interpret grokking as integration of memorized atomic facts into an already established reasoning route rather than the sudden creation of a wholly new reasoning paradigm. They also find that high unseen-case accuracy, possession of the route, and transfer to new facts can come apart.

This is unusually close to the present threshold decomposition.

### 4.5 Grokking can be structural and task-dependent

Murty et al. show delayed hierarchical generalization in vanilla transformers after in-domain performance has saturated. Wang et al. show grokking-linked implicit reasoning in controlled compositional and comparison tasks, with different out-of-distribution behavior across reasoning types. These results caution against equating one held-out score with complete mastery of a general rule.

### 4.6 LLM pretraining may exhibit local, asynchronous analogues

Li, Fan, and Zhou study a 7B mixture-of-experts language model and report local asynchronous grokking-like transitions across data groups. Their pathway metrics concern expert choices across layers, not abstract proof paths, but the observed change from instance-specific, irregular routing toward more structured and transferable routing is structurally relevant.

The present paper treats this as an empirical foothold, not a proof that full-scale LLM pretraining follows the toy-model mechanism.

### 4.7 Human restructuring is not identical to the "Aha!" feeling

Human insight research has long distinguished search from representational restructuring. Ohlsson proposed that restructuring changes the representation and therefore changes which problem-solving operators apply. More recent reviews emphasize that objective restructuring and subjective Aha phenomenology often co-occur but are not equivalent; Aha experiences can be absent from genuine restructuring or accompany wrong answers.

Therefore:

$$
\boxed{
\text{felt suddenness is a marker, not the criterion of grokking.}
}
$$

The Trinity kiss and the human first-connection experience are phenomenological models of $t_\star$, not decisive measurements.

---

## 5. Formal apparatus

### 5.1 Task field and target relation

Let

$$
X
$$

be a task field, with outputs in $Y$, and let

$$
f^\star:X\to Y
$$

be the target relation.

A learner at time $t$ has a toolkit

$$
\mathcal T_t
=
\{\tau_1,\ldots,\tau_{k_t}\}.
$$

The tools can be perceptual discriminators, transformations, rules, circuits, retrieval routes, proof operators, or other domain-appropriate operations.

Let

$$
\mathrm{Cl}_{\mathcal A}(\mathcal T_t)
$$

be the closure of the toolkit under a declared set $\mathcal A$ of admissible operations. Depending on the domain, $\mathcal A$ may include composition, substitution, conjunction, recursion, tensor contraction, group action, or linear combination.

The subscript is essential. There is no content-free closure. A learner cannot validly combine tools under operations the domain does not support.

### 5.2 Local paths

A local path is a partial solver

$$
p_i:U_i\to Y,
\qquad
U_i\subseteq X.
$$

The family

$$
\mathcal P_t
=
\{(U_i,p_i)\}_{i\in I_t}
$$

is the learner's current atlas.

Define experienced coverage under a distribution $\nu$ by

$$
L_t
=
\nu\!\left(\bigcup_{i\in I_t}U_i\right).
$$

A learner can have

$$
L_t\approx 1
$$

on the training or familiar distribution while lacking a global solver. Coverage is not closure.

### 5.3 Compatibility and transport

Two local paths are directly compatible when their restrictions agree, or can be transported into agreement, on an overlap:

$$
p_i|_{U_i\cap U_j}
=
T_{ji}\!\left(p_j|_{U_i\cap U_j}\right).
$$

Here $T_{ji}$ is a declared transport. It may be an identity map, change of coordinates, symbol alignment, gauge choice, unit conversion, parity/orientation correction, or another operationally defined relation.

No declared transport, no legitimate claim of phase or linear coherence.

Construct a compatibility graph

$$
H_t=(I_t,E_t),
$$

where

$$
(i,j)\in E_t
$$

when a tested transport relation between $p_i$ and $p_j$ is available.

A weighted version may assign

$$
w_{ij}(t)\in[0,1]
$$

to the strength, reliability, or accessibility of that relation.

### 5.4 Gluing defect

For a metric or discrepancy functional $d_{ij}$ on overlaps, define

$$
\Omega_t
=
\sum_{(i,j)\in E_t}
\omega_{ij}\,
d_{ij}\!\left(
p_i|_{U_i\cap U_j},
T_{ji}p_j|_{U_i\cap U_j}
\right).
$$

Small $\Omega_t$ means the currently linked paths are mutually coherent under the declared transports. It does not imply that the graph covers all required regions or that the global continuation is unique.

A family of local paths **glues** when there exists

$$
g_t\in \mathrm{Cl}_{\mathcal A}(\mathcal T_t)
$$

such that

$$
g_t|_{U_i}=p_i
$$

for the relevant regions.

The target of grokking is not necessarily exact equality at finite precision. In an empirical model, one uses tolerances and held-out error.

### 5.5 Generators and compression

Suppose the learner initially stores or deploys many paths

$$
p_1,\ldots,p_N.
$$

A global organization is generative when there exists a smaller family

$$
G_t=\{g_1,\ldots,g_r\},
\qquad r\ll N,
$$

such that

$$
p_i\in\mathrm{Cl}_{\mathcal A}(G_t)
$$

for most relevant $i$.

Then the description changes from

$$
\{p_1,\ldots,p_N\}
$$

to

$$
\left(
G_t,\{\theta_i\}_{i=1}^N
\right),
$$

where $\theta_i$ specifies how the generators produce $p_i$.

Generalization is possible when a novel case can be represented by a new coordinate or composition

$$
p_{\mathrm{new}}
=
G_t(\theta_{\mathrm{new}})
$$

rather than learned as a new isolated path.

This is why grokking often correlates with compression, lower-rank structure, symmetry, or simpler circuits. Those are candidate signatures of generator formation. They are not interchangeable definitions of understanding.

### 5.6 A closure order parameter

Let $R\subseteq I_t$ be the set of local path classes required for full task traversal. Define

$$
Q_t
=
\frac{
\left|
C_{\max}(H_t)\cap R
\right|
}{
|R|
},
$$

where $C_{\max}(H_t)$ is the largest mutually compatible component.

This crude order parameter measures how much of the required field lies inside one connected compatibility component. More sophisticated versions can weight path importance, use hyperedges, include gluing residuals, or measure algebraic generation rather than graph connectivity.

A phenomenological nucleation event can be modeled by

$$
\dot Q(t_\star^-)\approx 0,
\qquad
\dot Q(t_\star^+)>0
$$

for a sustained interval, even while held-out accuracy remains flat.

The "derivative flip" therefore belongs first to a latent closure variable, not necessarily to the visible test curve.

### 5.7 Constructibility, identifiability, accessibility, and dominance

Four conditions must be kept separate.

**Constructibility**

$$
C_t
=
\mathbf 1\!\left[
g^\star\in
\mathrm{Cl}_{\mathcal A}(\mathcal T_t)
\right].
$$

The global solver can be built from the current tools.

**Identifiability**

$$
I_t
=
\mathbf 1[
\text{available evidence distinguishes the relevant global alignment}
].
$$

A correct global continuation may exist but remain one of many observationally equivalent possibilities.

**Accessibility**

$$
A_t
=
\mathbf 1[
\text{the learner's current dynamics contain a reachable route to deploy it}
].
$$

A solution can exist in closure but be inaccessible to the architecture, optimizer, attention policy, or conscious search process.

**Dominance**

Let $K_G(t)$ be the effective cost of the global solution and $K_M(t)$ the effective cost of the memorizing/local solution. Define

$$
\Delta_t
=
K_M(t)-K_G(t).
$$

When

$$
\Delta_t<0,
$$

the local solution is cheaper or stronger. When

$$
\Delta_t>0,
$$

the global solution is favored.

A candidate onset condition is

$$
\boxed{
C_t=I_t=A_t=1.
}
$$

Behavioral grokking additionally requires the global organization to control the output:

$$
\boxed{
C_t=I_t=A_t=1
\quad\text{and}\quad
\Delta_t>\Delta_{\mathrm{deploy}}.
}
$$

The exact threshold depends on noise, task metric, and architecture.

### 5.8 The thresholds

Define:

$$
t_\star
=
\inf\{
t:
C_t=I_t=A_t=1
\},
$$

the earliest time the global route is a constructible, distinguishable, reachable option.

Define:

$$
t_{\mathrm{grok}}
=
\inf\{
t\ge t_\star:
\mathrm{Gen}(t)\ge \gamma
\text{ for a predeclared sustained criterion}
\},
$$

where $\mathrm{Gen}(t)$ is a held-out generalization measure and $\gamma$ is fixed before inspecting the run.

Then:

$$
\boxed{
t_\star
\text{ is the beginning of possible grokking;}
\quad
t_{\mathrm{grok}}
\text{ is its behavioral disclosure.}
}
$$

A first atomic connection can witness $t_\star$ if that connection closes the final missing relation needed to make a global route available. A smaller connection may instead be a pre-nucleation seed. The criterion is functional, not dramatic: did the event change the closure class?

---

## 6. Exact toy results

The following propositions are not claimed as universal theorems of human cognition or deep learning. They establish that the proposed distinctions are mathematically real.

### Proposition 1 — Coverage without closure does not entail generalization

Let $S\subsetneq X$ be finite. For any labels $f^\star|_S$, there exists a memorizing function $m:X\to Y$ satisfying

$$
m(x)=f^\star(x)
\qquad
\text{for all }x\in S
$$

while taking arbitrary values on $X\setminus S$.

**Proof.** Define $m$ to equal $f^\star$ on $S$ and choose any assignment on the complement. $\square$

Perfect local/training coverage therefore places no general lower bound on unseen performance without a restricted hypothesis family, symmetry, regularity assumption, bridge constraint, or other source of closure.

### Proposition 2 — Connected-overlap gauge theorem

Let $p$ be prime. Let $A$ and $B$ be finite token sets with hidden coordinates

$$
u:A\to\mathbb Z_p,
\qquad
v:B\to\mathbb Z_p.
$$

For observed pairs $E\subseteq A\times B$, the labels are

$$
y_{ab}
=
u(a)+v(b)
\pmod p.
$$

Let

$$
G_E=(A\sqcup B,E)
$$

be the bipartite observation graph, and suppose it has $c$ connected components.

Then every consistent solution has one independent gauge parameter per connected component:

$$
u'(a)=u(a)+\lambda_k,
\qquad
v'(b)=v(b)-\lambda_k
$$

for vertices $a,b$ in component $k$.

Consequently, relative to one global gauge, the observations leave

$$
p^{c-1}
$$

possible relative alignments between components.

**Proof.** Every observed edge inside component $k$ obeys

$$
u'(a)+v'(b)
=
u(a)+\lambda_k+v(b)-\lambda_k
=
y_{ab}.
$$

Thus each component admits an independent $\lambda_k$. Conversely, along a connected component, edge equations determine all coordinate differences relative to one chosen anchor, leaving exactly one additive degree of freedom. Fixing one global anchor removes one of the $c$ freedoms. $\square$

### Corollary 2.1 — Same-component and cross-component prediction differ

For an unseen pair $(a,b)$:

- if $a$ and $b$ lie in the same connected component, the gauge cancels and $u(a)+v(b)$ is fixed by any consistent solution;
- if they lie in different components $i$ and $j$, the predicted label changes by

$$
\lambda_i-\lambda_j
$$

and is not identified by the training data.

Under a uniform prior over unresolved relative gauges, the expected exact-match accuracy on cross-component pairs is at most

$$
\frac1p.
$$

No additional optimization on the same disconnected evidence can recover information the evidence does not contain.

### Corollary 2.2 — Each valid bridge removes a factor of ambiguity

A valid edge connecting two previously separate components reduces the component count by one and removes one independent relative gauge. In the idealized setting, it reduces the alignment ambiguity by a factor of $p$.

This is the exact core of the bridge experiment.

### Proposition 3 — Nucleation is not sufficient for behavioral grokking

There exist learning states in which a global solver belongs to the toolkit closure but behavior remains memorization-dominated.

**Construction.** Let both $m$ and $g$ fit the training set, with $g$ generalizing and $m$ failing off-training. Let the deployment rule select the lower effective cost. If

$$
K_M(t)<K_G(t),
$$

then $m$ controls behavior although $g\in\mathrm{Cl}(\mathcal T_t)$. Later regularization or cleanup can reverse the inequality without creating $g$ at that later moment. $\square$

### Proposition 4 — Smooth latent change can produce an abrupt visible transition

Let global and memorizing strengths $a_G(t)$ and $a_M(t)$ vary continuously. If behavior selects

$$
h_t
=
\begin{cases}
m,&a_M(t)>a_G(t),\\
g,&a_G(t)\ge a_M(t),
\end{cases}
$$

then held-out performance can jump discontinuously at the crossing even though both latent strengths are continuous.

A softmax or mixture rule smooths the mathematical discontinuity but can still produce a very steep transition.

### Proposition 5 — Hard nerf-grokking is possible

If any of the following remains permanently false under a fixed learning setup,

$$
C_t=1,\qquad I_t=1,\qquad A_t=1,
$$

then behavioral grokking of the target global rule cannot occur in that setup.

This is not slowness. It is a boundary relative to the current task, evidence, toolkit, and dynamics.

---

## 7. Degenerate spaces and nerf-grokking

### 7.1 Definition

A system is **nerf-grokked** relative to a target relation when it can acquire substantial local competence but the global generalizing organization is blocked, weakened, or prevented from becoming behaviorally dominant.

Two forms must be distinguished.

**Hard nerf-grokking**

$$
C_t I_t A_t = 0
$$

for all reachable future states under the fixed setup.

**Soft nerf-grokking**

$$
C_t=I_t=A_t=1
$$

eventually, but

$$
\Delta_t
$$

never reaches the deployment threshold within the available optimization, lifetime, attention, or resource budget.

### 7.2 Target degeneracy

The field may not possess the hoped-for compact global rule. A random labeling can be memorized locally but offers no shorter generator than the table itself.

In that case, failure to grok is not learner failure. The target has no relevant closure to discover.

### 7.3 Evidence degeneracy

The observations may decompose into disconnected components or preserve a symmetry that leaves global alignment unidentifiable. The connected-overlap theorem gives one exact example.

This is a probe/access problem in the evidence, not an optimization defect. Replaying the same evidence forever cannot determine an unresolved relative gauge.

### 7.4 Toolkit degeneracy

The necessary primitive or transport may be absent:

$$
g^\star\notin\mathrm{Cl}_{\mathcal A}(\mathcal T_t).
$$

The learner can accumulate paths forever while never acquiring the operation needed to compose them globally.

### 7.5 Representational degeneracy

The learner may possess relevant information in mutually incompatible bases without a transport map. Apparent "pieces" cannot be validly superposed merely because they resemble one another.

A modular-addition model can literally combine Fourier components because the common basis is operationally declared. A human analogy must not assume a vector structure without specifying it.

### 7.6 Architectural or dynamical degeneracy

A generalizing circuit may be expressible in principle but unreachable under the architecture or optimizer. Bottlenecks can include:

- insufficient depth or recurrence;
- missing parameter sharing;
- an attention pattern that cannot bind distant pieces;
- an optimizer trapped in a basin;
- regularization too weak to suppress memorization;
- regularization so strong that both circuits are destroyed;
- finite precision or bandwidth;
- a human attentional or working-memory limit.

### 7.7 Dominance degeneracy

The generalizer may exist and be reachable but never become cheaper, stronger, or more salient than the local solution. The learner "has" the relation in a weak latent sense but continues to act through memorized routes.

### 7.8 False nucleation

A learner can experience a compelling connection that does not survive transfer. In humans, Aha phenomenology can accompany wrong answers. In models, a probe can detect a correlated feature that is not causally load-bearing.

A nucleation claim therefore requires:

- a declared latent variable;
- a causal or predictive probe;
- held-out transfer;
- mutation controls;
- evidence that the connection changes the closure class rather than merely the report.

---

## 8. The proposed developmental sequence

### Stage 1 — Local path acquisition

The learner discovers procedures that work on bounded regions:

$$
(U_1,p_1),\ldots,(U_n,p_n).
$$

Training accuracy rises. Familiar traversal cost falls.

### Stage 2 — Coverage plateau

The union of the charts covers most encountered cases:

$$
\nu\!\left(\bigcup_i U_i\right)\approx 1,
$$

but the compatibility graph remains fragmented or high-defect.

The learner can do much but cannot explain why the methods belong together or reliably transport them to unfamiliar combinations.

### Stage 3 — Nucleation / availability boundary

A minimal coherent structure appears that can grow into a global organization. Formally, a required generator enters closure, a missing transport becomes available, or a bridge removes the last relevant relative ambiguity.

This is $t_\star$.

The event can be phenomenally dramatic or entirely latent.

### Stage 4 — Closure growth, alignment, and cleanup

The coherent component expands. Local conventions align. Redundant paths compress. The global route becomes easier to deploy. Memorizing components may remain active and compete.

This is grokking proper in progress.

### Stage 5 — Behavioral disclosure

The global organization crosses the dominance threshold. Held-out performance rises, often sharply:

$$
t=t_{\mathrm{grok}}.
$$

The visible jump is a disclosure of accumulated internal change, not necessarily its birth.

### Stage 6 — Stabilization and transfer

A mature organization should survive:

- new examples;
- changed surface forms;
- composition depth;
- perturbation of memorized items;
- removal of redundant local routes;
- relearning of new atoms;
- hostile out-of-distribution regimes.

Failure here means the system grokked a narrower field than the observer assumed.

---

## 9. Predictions

### P1 — Connectivity matters beyond sample count

Holding edge count, token frequency, label entropy, architecture, and optimizer approximately fixed, a connected training topology should permit or accelerate global generalization relative to a disconnected topology.

### P2 — A small number of bridges can have superlinear informational value

A valid bridge joining two previously independent components can remove an entire relative gauge. Its effect should be much larger than that of a redundant within-component example.

### P3 — Degree-preserving rewiring can change time-to-grok

Two datasets with the same number of examples and the same per-token degree sequence can differ in grokking because one observation graph is connected or has a larger spectral gap.

### P4 — Local mastery can coexist with permanently chance cross-component transfer

A disconnected model should be able to memorize and generalize within components while remaining unable, on average over hidden alignments, to predict cross-component cases.

### P5 — Latent closure measures should move before visible generalization

Compatibility, representational alignment, circuit strength, or pathway reuse should improve before held-out accuracy crosses the grokking threshold.

### P6 — The first true bridge should change the derivative of a latent order parameter

The enabling event should be detectable as a sustained change in the growth of a predeclared closure measure even when visible performance has not yet moved.

### P7 — Corrupted bridges should not help

A bridge-position example with an incorrect relation should fail to produce the benefit of a valid bridge and may delay or destabilize closure.

### P8 — Re-grokking should be faster when generators survive

If a perturbation damages surface mappings but preserves the global generator, recovery should be faster than first acquisition. If the generator is ablated, recovery should resemble initial learning.

### P9 — Grokking can be local and asynchronous

Different task regions can nucleate and close at different times. Global curves may average over several local transitions.

### P10 — Human Aha and objective closure can dissociate

Some participants should transfer without reporting an Aha; others should report an Aha without passing mutation or transfer tests.

### P11 — Nested grokking is possible

A learner can grok subfields first and later grok a relation among those already-grokked subfields:

$$
\mathrm{Cl}(G_1),\ldots,\mathrm{Cl}(G_m)
\quad\longrightarrow\quad
\mathrm{Cl}(G_{\mathrm{meta}}).
$$

This predicts plateaus and derivative changes at multiple scales.

### P12 — Better bridge placement can outperform more undirected exposure

Curricula selected to split the largest unresolved compatibility class should accelerate closure more efficiently than adding randomly sampled familiar examples.

---

## 10. The decisive machine experiment

The companion protocol specifies an opaque cyclic-addition task.

Inputs are opaque tokens $a\in A$ and $b\in B$ with hidden coordinates in $\mathbb Z_p$. The label is

$$
y_{ab}=u(a)+v(b)\pmod p.
$$

Training examples are edges of a bipartite graph. Dataset conditions are constructed by degree-preserving edge swaps so that sample count and token frequency remain matched while graph connectivity changes.

Primary conditions:

1. connected, high-connectivity graph;
2. connected, low-spectral-gap graph;
3. degree-matched disconnected graph;
4. disconnected graph repaired by the minimum number of valid bridges;
5. topology-matched corrupted-bridge control;
6. random-label negative control;
7. dense positive control.

Primary outcome:

$$
\text{time from memorization to sustained cross-component generalization}.
$$

Primary falsifier:

> If degree-matched connectivity and valid bridge restoration do not affect cross-component generalization or latent closure measures beyond ordinary sample-count variance, the proposed bridge-topology mechanism loses substantial weight.

The theorem guarantees an identifiability difference in the data-generating model. The experiment asks whether model training dynamics expose that difference in the predicted grokking shape.

---

## 11. Human analogue

A human study can use a smaller opaque symbol system.

Participants learn local pair transformations or cyclic sums under one of two evidence topologies:

- connected by structurally valid overlap examples;
- divided into equally practiced but disconnected clusters.

Training continues until local accuracy is matched. Participants then receive:

- unseen within-cluster cases;
- unseen cross-cluster cases;
- composition tests;
- surface-renamed transfer;
- confidence and Aha reports.

The objective transition is defined by transfer and mutation robustness, not self-report alone.

A strong result would be:

$$
\text{equal local mastery}
\quad+\quad
\text{different bridge topology}
\quad\Rightarrow\quad
\text{different global transfer}.
$$

This would not prove a shared neural mechanism with LLMs. It would support a shared abstract closure constraint.

---

## 12. Relation to rival explanations

### R1 — Ordinary memorization plus more training

On this view, enough optimization eventually improves test accuracy without a distinct structural transition.

The closure account concedes that latent variables can evolve smoothly. Its differentiator is not metaphysical discontinuity but topology: connectivity and bridge placement should matter after controlling sample count and local fit.

### R2 — Weight norm / loss-landscape account

Omnigrok and related work emphasize the competition between memorizing and generalizing regions of the loss landscape, often under weight decay.

The present account is compatible with this as a dominance mechanism:

$$
\Delta_t
=
K_M(t)-K_G(t).
$$

It adds a prior question: what determines whether a global generalizer is constructible and identifiable at all?

### R3 — Competing circuits

Circuit-competition accounts distinguish dense/memorizing and sparse/generalizing subnetworks.

The closure account is compatible with circuit competition but predicts that the generalizing circuit's availability depends on relations among learned atoms and on the topology of evidence.

### R4 — Symmetry acquisition

Recent work emphasizes task symmetry and low-dimensional geometric organization.

The closure account treats symmetry as a particularly strong kind of generator. It is not restricted to symmetry, and it predicts failure when the data preserve independent component gauges or do not reveal the relevant group action.

### R5 — Compression

A global rule often has shorter description length than a lookup table.

Compression is expected but not sufficient. A compressed wrong rule, a semantically relabeled table, or a low-rank representation lacking correct transport does not establish closure. Transfer and bridge-sensitive causal probes remain necessary.

### R6 — Human representational-change theory

Insight research already claims that restructuring changes which operators apply.

The present contribution is narrower and more formal:

- local operators are explicitly represented as partial paths;
- overlap and transport are modeled;
- the enabling boundary is separated from behavioral disclosure;
- disconnected evidence yields an exact gauge obstruction;
- human and machine cases are compared at the level of learning topology, not phenomenological identity.

### R7 — Pure measurement artifact

An apparently sudden ability can arise from a smooth latent variable crossing a coarse benchmark threshold.

The present model explicitly permits this. The claim survives only if a predeclared latent closure variable and bridge manipulation explain variance beyond the benchmark threshold itself.

---

## 13. What would count as evidence

### Support

The account gains weight if:

- valid bridge examples causally accelerate or permit global generalization;
- redundant examples with the same count do not;
- corrupted bridges fail;
- latent alignment or closure measures change before test accuracy;
- ablation of bridge-mediated or common-basis structure selectively destroys transfer;
- the effect replicates across architectures and at least two task families;
- a human analogue shows the same topology effect after matching local mastery.

### Ambiguous

The result remains ambiguous if:

- connected conditions merely contain easier examples;
- token frequencies or degree sequences differ;
- only one seed groks;
- a probe predicts generalization but is not causally load-bearing;
- Aha reports change without transfer;
- global performance improves but no distinction from weight norm, data leakage, or sample count is possible.

### Refutation pressure

The account loses weight if:

- degree-matched connectivity has no reproducible effect;
- disconnected conditions achieve true cross-component transfer above the information-theoretic bound without additional information;
- bridge restoration helps no more than random redundant samples;
- the proposed closure metric moves only after generalization;
- causal ablation shows that the detected common representation is epiphenomenal;
- human transfer is fully explained by explicit instruction or vocabulary without compositional reuse.

---

## 14. Claim ledger

| Claim | Status | Boundary / truth debt |
|---|---|---|
| The frozen TLICA foundation contains gradual verification-tool acquisition, proto-patterns, shadow encounter, and combinatorial recognition of known tools | **Disclosed within TLICA** | Sections 3.2–3.3, File 2 |
| The acquired-taste note already introduces application-level toolkit closure and representational unfolding | **Disclosed within TLICA** | Research note; not foundation |
| Grokking can occur long after training-set memorization | **Corroborated** | Power et al. and many replications |
| Modular-addition grokking contains gradual circuit formation and cleanup before the visible transition | **Corroborated, bounded** | Nanda et al.; one canonical task/model family |
| Algorithmic structure may be detectable before successful generalization | **Observed / provisional** | Strongly supported in several mechanistic studies; exact universality unproven |
| The same in-distribution inference route can exist in non-grokked and grokked transformers | **Observed, bounded** | He et al. 2026 task/setup |
| Human Aha phenomenology and objective restructuring can dissociate | **Corroborated** | Insight literature |
| Human insight and machine grokking instantiate one abstract local-to-global closure topology | **Conjectured** | Requires cross-domain discriminating probes |
| $t_\star$ is distinct from $t_{\mathrm{grok}}$ | **Conjectured as a general decomposition; disclosed in toy model** | Mechanistic checkpoint tests required |
| Disconnected opaque-addition evidence leaves $p^{c-1}$ relative gauge ambiguity | **Disclosed in stated toy model** | Exact proposition under model assumptions |
| A valid bridge removes one component gauge factor | **Disclosed in stated toy model** | Exact when the bridge is consistent and joins components |
| Bridge topology controls neural time-to-grok beyond sample count | **UNVERIFIED** | Primary experiment |
| A truly degenerate field can hard-nerf grokking | **Disclosed relative to constructibility/identifiability conditions; empirical scope UNVERIFIED** | Must classify which obstruction applies |
| LLMs possess TLICA $\phi$, $\rho$, or $\kappa$ coordinates | **Not claimed** | Conscious-I status not established |
| Grokking proves understanding in a complete or human sense | **Refuted as a paper claim** | Transfer can remain narrow |

---

## 15. Limitations

1. **The abstraction may be too broad.** Many learning processes can be redescribed as local-to-global. The bridge experiment is required to make the proposal discriminating.

2. **Compatibility graphs are a model, not a discovered neural object.** Actual circuits may require hypergraphs, group representations, manifolds, or distributed dynamical systems.

3. **The order parameter is toolkit-relative.** Choosing path units and transports can change the graph. A serious implementation must predeclare the decomposition or justify it mechanistically.

4. **Grokking is not one phenomenon.** Modular arithmetic, hierarchical syntax, implicit reasoning, copying, image classification, and LLM pretraining may involve different mechanisms.

5. **Current 2026 sources include recent preprints.** Their results should be treated as provisional until independently replicated or peer reviewed.

6. **Human phenomenology is first-person and noisy.** The first perceived connection may lag, lead, or misidentify the objective restructuring.

7. **The Matrix analogy is expository.** It earns no evidential weight.

8. **A global rule can still be narrow.** Successful interpolation across one held-out split need not imply systematic out-of-distribution generalization.

---

## 16. Integration rule

Do **not** modify the frozen foundation merely because this framing is coherent.

Promote the proposal only after the bridge-topology experiment distinguishes it from sample count, ordinary regularization, and generic smooth-learning accounts.

The next verdict-changing result is:

> With model, training budget, edge count, per-token degree, and local learnability matched, degree-preserving rewiring that joins previously disconnected evidence components substantially increases the probability or speed of cross-component grokking, while corrupted and redundant-edge controls do not.

Until that probe runs:

$$
\boxed{
\text{Grokking as toolkit closure: CONJECTURED, formally sharpened, experimentally reachable.}
}
$$

---

## 17. Conclusion

The proposed picture preserves the phenomenology without mistaking drama for mechanism.

At first, learning turns a difficult field into a collection of easier disconnected routes. Enough routes can produce strong familiar-case performance and a plateau. The decisive enabling event is not yet full understanding. It is the first point at which the learner's current tools admit a globally extensible organization.

After that point, grokking can begin. Local paths align, become composable, reveal common generators, and cease to function only as separate answers. The global route may remain weak for a long time. It may require cleanup, regularization, repeated use, or suppression of memorizing alternatives before behavior flips.

The visible transition is therefore downstream of a quieter structural event:

$$
\boxed{
\text{The first atomic connection does not finish grokking. It creates a world in which grokking can occur.}
}
$$

A degenerate field can prevent that world from forming. It can leave local islands without bridges, preserve unresolved gauges, omit the necessary operator, block the optimization path, or keep the generalizer permanently subordinate. Such a learner can become highly competent and never become globally free.

Neo's final transformation is a useful image because he does not merely acquire one more move. The objects that constrained him become expressions of a common structure. The paper's empirical wager is that an analogous distinction can be made precise: not between ignorance and a magical flash, but between **coverage by remembered paths** and **movement generated by the field's internal relations**.

---

## References

The archive is self-contained, so identifiers are supplied as plain text rather than external Markdown links.

1. Power, A.; Burda, Y.; Edwards, H.; Babuschkin, I.; Misra, V. (2022). *Grokking: Generalization Beyond Overfitting on Small Algorithmic Datasets*. arXiv:2201.02177.

2. Nanda, N.; Chan, L.; Lieberum, T.; Smith, J.; Steinhardt, J. (2023). *Progress Measures for Grokking via Mechanistic Interpretability*. ICLR 2023. arXiv:2301.05217.

3. Liu, Z.; Michaud, E. J.; Tegmark, M. (2023). *Omnigrok: Grokking Beyond Algorithmic Data*. ICLR 2023. arXiv:2210.01117.

4. Merrill, W.; Tsilivis, N.; Shukla, A. (2023). *A Tale of Two Circuits: Grokking as Competition of Sparse and Dense Subnetworks*. arXiv:2303.11873.

5. Murty, S.; Sharma, P.; Andreas, J.; Manning, C. D. (2023). *Grokking of Hierarchical Structure in Vanilla Transformers*. ACL 2023 Short Papers, pp. 439–448. DOI: 10.18653/v1/2023.acl-short.38.

6. Wang, B.; Yue, X.; Su, Y.; Sun, H. (2024). *Grokking of Implicit Reasoning in Transformers: A Mechanistic Journey to the Edge of Generalization*. NeurIPS 2024. arXiv:2405.15071.

7. Li, Z.; Fan, C.; Zhou, T. (2026 revision; first posted 2025). *Grokking in LLM Pretraining? Monitor Memorization-to-Generalization without Test*. arXiv:2506.21551.

8. He, K.; Zhang, M.; Wu, P.; Du, X.; Chen, Z. (2026). *Is Grokking Worthwhile? Functional Analysis and Transferability of Generalization Circuits in Transformers*. Findings of ACL 2026, pp. 33993–34001. DOI: 10.18653/v1/2026.findings-acl.1697.

9. Swaroop, A. (2026). *Latent Algorithmic Structure Precedes Grokking: A Mechanistic Study of ReLU MLPs on Modular Arithmetic*. arXiv:2603.23784. Preprint.

10. Hwang, H.; Park, Y. (2026). *Intrinsic Task Symmetry Drives Generalization in Algorithmic Tasks*. arXiv:2603.01968. Preprint.

11. Ohlsson, S. (1984). *Restructuring Revisited: II. An Information Processing Theory of Restructuring and Insight*. Scandinavian Journal of Psychology, 25(2), 117–129. DOI: 10.1111/j.1467-9450.1984.tb01005.x.

12. Knoblich, G.; Ohlsson, S.; Raney, G. E. (2001). *An Eye Movement Study of Insight Problem Solving*. Memory & Cognition, 29, 1000–1009. DOI: 10.3758/BF03195762.

13. Kounios, J.; Beeman, M. (2014). *The Cognitive Neuroscience of Insight*. Annual Review of Psychology, 65, 71–93. PMID: 24405359.

14. Wiley, J.; Danek, A. H. (2024). *Restructuring Processes and Aha! Experiences in Insight Problem Solving*. Nature Reviews Psychology, 3, 42–55. DOI: 10.1038/s44159-023-00257-x.

15. Wachowski, Lana; Wachowski, Lilly (directors) (1999). *The Matrix*. Warner Bros. Used here only as an expository narrative model.
