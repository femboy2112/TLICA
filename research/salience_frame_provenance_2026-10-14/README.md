# Salience, Frame Transport, and Lossy Provenance

## Context-dependent agency, locally admissible self-updates, and the difference between coherence and truth

**Date:** 2026-10-14  
**Status:** research-tier synthesis; psychological mechanism **CONJECTURED / UNVERIFIED**  
**Foundation impact:** none; no new TLICA primitive, coordinate, developmental mode, or clinical assertion  
**Provenance:** author-originated conceptual distinctions, rewritten as a privacy-preserving theoretical seed; AI-assisted formalization. No verbatim personal material or identifying case history is archived here.  
**Scope:** descriptions of possible cognitive organizations, not person-level assessment, diagnosis, medication guidance, or an established neuroscience model.

### Read this package

- [FORMALISM.md](FORMALISM.md): typed candidate objects, conditional propositions, and counterexamples.
- [CLAIM_LEDGER.md](CLAIM_LEDGER.md): status of every substantive claim and what would change the verdict.
- [PROBES.md](PROBES.md): discriminating tests, null/positive/negative/mutation controls, and safe study design.
- [SOURCES_AND_RECONCILIATION.md](SOURCES_AND_RECONCILIATION.md): external prior art, TLICA dependencies, and non-transported analogies.
- [RESEARCH_HANDOFF.md](RESEARCH_HANDOFF.md): an operational continuation brief for future research.
- [finite_witness.py](finite_witness.py): finite *mathematical* witnesses only; no human psychological validation.

---

## 0. The concise hypothesis

A cognitive agent may **possess** a memory, capacity, value, or counterargument while failing to **retrieve**, **feel the importance of**, or **deploy** it in a particular context. Contextual changes in affect, anticipated consequence, task affordances, available control, and identity-coupled commitments may change the *effective reachable region* of a person's already learned repertoire. The resulting felt discontinuity need not entail discontinuity of personhood.

A second conjecture concerns reflexive control. An agent unable to endorse a large interpretive change directly may realize it through a chain of *locally acceptable* smaller frame updates. The chain can enable legitimate action without retracting a valid objection; equally it can attenuate an accurate warning, rationalize a dangerous action, or produce a highly coherent but inaccurate frame. Each step's phenomenological acceptability is not a truth certificate.

A third conjecture concerns time. An agent may initially reconstruct an update's local justifications, later retain only a compressed boundary representation, and eventually retain the resulting commitment while losing the accessible provenance that supported—or failed to support—it. Restoring an explanation of the path is not equivalent to restoring the former frame's felt salience. Credible external records may reopen the earlier interpretation; the timing of correction may depend on available *slack*.

The target problem is therefore **truth-respecting, self-resonant correction under bounded access and lossy history**, not coherence maximization.

## 1. The originating distinctions (privacy-abstracted)

These are conceptual inputs, **not** claims of a validated mechanism.

### 1.1 Four forms of salience are not identical

- **Intellectual salience:** an idea's felt depth, significance, and ability to recruit further manipulation.
- **Affective salience:** emotional activation and the relevance assigned through feeling.
- **Instrumental salience:** felt significance inherited from a valued downstream goal.
- **Actionable salience:** sufficient integration of value, opportunity, and control to initiate or sustain behavior.

Preserved competence can coexist with attenuated reward for pursuing it. Conversely, immediate necessity can cause an uninteresting task to become engaging *because* it has become the operative means to preserve a valued future. This is not necessarily intrinsic curiosity about the task.

Do not equate salience with TLICA's contact $\kappa$, toolkit-relative truth-indistinguishability $\varphi$, source-map adequacy $\sigma$, identity correlation $\rho$, probe availability $\mu$, or reflexive-operating slack. Those retain distinct types.

### 1.2 Possession, accessibility, deployment

Knowing an object exists, being able to retrieve its meaning, and being able to act upon it are three different operations:

$$
\text{possess}(x)\not\Rightarrow\text{retrieve-as-relevant}(x,c)
\not\Rightarrow\text{deploy}(x,c).
$$

An environment can supply scaffolding (cues, roles, feedback, structure) that makes a capacity operational there but not in another environment. Recollection of one's behavior in the first context need not reinstantiate the state that produced it.

This motivates an **access-map hypothesis**, not a theory that people literally contain separate context-specific selves.

### 1.3 Emotion as state update versus frame update

An event may modify the current state while leaving the interpretation scheme largely stable, or modify the scheme by which past evidence, present priorities, and expected futures are evaluated.

$$
(s,F)\xrightarrow{e}(s',F)
\quad\text{versus}\quad
(s,F)\xrightarrow{e}(s',F').
$$

These are idealized limiting cases. Real transitions can change both continuously.

Three rival readings of a subjectively buffered emotional episode remain open: slower rise in affect, delayed influence of affect on action, or reduced propagation of affect into global interpretation. First-person description need not distinguish them. **Equal eventual emotional intensity is compatible with different temporal trajectories or decision couplings.** A plot of smoother emotion alone cannot establish which mechanism operates.

### 1.4 Instrumental salience and deadlines

A valued long-term outcome may fail to generate immediate task engagement while its consequences remain distant. An approaching real constraint can promote the task's salience above an initiation threshold. Arbitrary self-declared deadlines may fail when the agent transparently recognizes that they are negotiable.

A locally effective burst-execution strategy can become globally infeasible when accumulated tasks require more labor than fits within the compressed activation windows. This is a workload-scheduling limitation, not evidence that task competence vanished.

### 1.5 Traversal without invalidating the obstacle

A valid reason against an action may remain valid even after the agent becomes able to act. The chosen route can change how the objection constrains action without changing the objection's truth status. A barrier can remain a barrier; finding a traversable route is not a proof the barrier was illusory.

But the same technique can progressively render an accurate warning unable to influence decisions. **Traversability, felt permission, justification, and safety must not be identified.**

### 1.6 History compression and the continuity problem

A sequence of small frame updates can alter which old objections are spontaneously available. The agent may still reconstruct their propositional content while failing to reoccupy their original motivational configuration. With repeated changes or passage of time, the causal path can become harder to recover:

$$
\text{accessible update chain}
\;\to\;
\text{partial historical summary}
\;\to\;
\text{weakly recoverable provenance}.
$$

This is a phenomenological proposal, **not** a general law of memory decay, thermodynamic law, nor a claim of literal holographic storage.

### 1.7 Epistemic anomalies and corrigibility

A contradiction between present interpretation and a credible earlier record can become salient *as an anomaly*, even when the immediate response is defensive. High slack may permit simultaneous access to competing interpretations and even humor about the discrepancy; low slack may delay integration.

This is **not** guaranteed epistemic goodness. An anomaly-solving drive can select either correction or a more self-resonant rationalization. The useful invariant, if one can be supported, is a procedure that preserves the possibility of external correction—not necessarily a fixed belief or emotional state.

## 2. Central failure mode: locally legal, globally defective

Let $F_0,\ldots,F_n$ be frames and $L(F_i,F_{i+1})$ denote *local psychological admissibility*. A chain can satisfy

$$
L(F_i,F_{i+1})=1\quad\text{for every }i
$$

while its endpoint fails a global criterion fixed at the start:

$$
G(F_0,F_n)=0.
$$

This is mathematically unremarkable unless $L$, $G$, and the observation map are operationally specified. Its psychological importance is the possible **drift of the evaluator itself**: later states judge later updates using altered priorities, retrieval, and framing.

**Fixed-invariant guard.** If a *single* invariant $I$ is exactly preserved at every step, the composition preserves it. A purported violation of $I$ at the end means either $I$ was not actually preserved, the effective admissibility predicate differed from $I$, or the assumed invariant was misspecified.

This distinction prevents the attractive phrase "illegal global change by legal local moves" from becoming a logical contradiction. "Legal" here is a *state-relative endorsement relation*, not preservation of external truth.

## 3. Why the destination can feel self-evident

Suppose a presently accessible record retains conclusions but only an approximate explanation of how they were adopted. Separate:

- **current endorsement** of an interpretation;
- **reconstructibility** of its causal/evidential history;
- **fidelity** of that reconstruction against external records;
- **readiness to revise** when evidence conflicts with the frame.

These are not one scalar. Strong endorsement can coexist with poor provenance. A coherent story may emerge both from faithful integration and from repeated self-confirming reinterpretation.

Crucially: introspective access to the steps of reasoning is not a reliable proof of their actual causes. A reconstruction may be accurate, partly confabulated, or a mixture. External records and discriminating tests are required.

## 4. The optimization problem, properly constrained

The proposed aim is **respect for evidence about the world and experience of the self, with minimal unjustified external perturbation and maximal feasible self-resonance**.

One useful research formulation is:

$$
\max_{F',a}
\Bigl[
R_{\mathrm{self}}(F',a)
-\lambda C_{\mathrm{transition}}(F,F')
-\mu C_{\mathrm{world}}(a)
\Bigr]
$$

subject to declared constraints on factual support, uncertainty, harm, and the continued inspectability of known objections.

**Do not** reduce truth, others' rights, objective risk, and epistemic uncertainty to costs that arbitrarily high self-resonance can offset. Here "truth of self" means an accurate account of subjective experience, needs, and commitments—not that every accompanying interpretation of the world is factually true. Minimizing world perturbation is conditional on legitimate goals; inaction can also sustain harm.

The action set must explicitly admit **defer / abstain / seek a probe**. Unresolved is a valid epistemic state; abstention is not automatically the winning move. A refusal to act must still be evaluated against real consequences of inaction.

## 5. The strongest research question

> When, and by what observation, can we distinguish a sequence of locally accessible, self-resonant frame changes that improves world-coupling from one that merely increases the apparent coherence of a possibly false self-model?

This requires **two audits**, not one:

1. A *transition audit*: could an observer reconstruct the original objections, what changed, and the claimed causal pathway?
2. A *reality audit*: do predictions, external records, and held-out interventions improve after the change?

A successful transition audit alone does not establish truth. A successful immediate outcome alone does not establish the safety of the route or its long-term generalization.

## 6. TLICA docking

This is a **research-tier composition** of mechanisms already discussed in the archive:

- [Frozen formal apparatus, §8](../../foundation/3_formal_apparatus.md): focus/imprinting, slow $G$, $\rho=R(G)$, field-reading $f=F(G,\cdot)$, reflexive reweighting, and the carefully scoped $S=M-\mathrm{Pressure}$ slack posit.
- [Differentiated Affect](../../applications/differentiated_affect_v1_0_2.md): affect as a configuration influencing salience and action-readiness.
- [Choice as Endogenous Filter](../../docs/app-choice-as-filter.md): state-relative filter reachability, momentum, and explicit "not yet" as an action.
- [Specific Coherent Agency](../specific_coherent_agency_2026-09-18/README.md): prediction, correction, coherent reachability, and provenance retention must remain distinct.
- [Authority-Compatible Frame Dynamics](../authority_compatible_frame_dynamics_2026-09-28/README.md): positive self-resonance can reinforce a captured frame without making it correct.
- [Self-Applied Architecture](../../docs/app-self-applied-architecture.md): reconstruction firewall and the distinction between a modeled past and its accessible present representation.
- [Phenomenology → Analogy → Model → Probe](../../docs/research-method.md): analogy motivates structure; fresh evidence, not beauty of the explanation, supplies warrant.

We do **not** identify frame state with the foundation's identity-correlation profile, or identify a psychologically compelling anomaly with high $\varphi$. All mappings are proposed refinements requiring observation maps and tests.

## 7. Explicit boundaries

- No literal quantum tunneling, conservation of emotional suffering, holographic memory, or neurological slew-rate mechanism is established by these analogies.
- No universal claim is made about any psychiatric treatment, condition, brain region, or person. Clinical interpretations require independent evidence and appropriate expertise.
- No diagnosis, trait score, moral worth metric, or prescription follows.
- No novelty claim. Relevant psychological and decision-theoretic literatures predate this dossier.
- The examples in this package are **synthetic**. They do not validate human cognitive dynamics or provide instructions for suppressing accurate risk warnings.
- The research must remain ethically safe: no deliberately induced severe distress, coercion, medication manipulation, intoxication, or rehearsal of real harmful decisions as a probe.

## 8. Current verdict

**Observed:** the author-origin conceptual distinctions exist as a coherent *reported phenomenological vocabulary*, with the underlying personally identifying circumstances intentionally omitted.

**Derived (conditional):** exact preservation of a fixed invariant composes; state-relative local admissibility need not imply global admissibility; a many-to-one history summary is not invertible.

**Conjectured:** context changes access to self-relevant capacities and facts partly through salience; chains of acceptable changes can shift interpretive authorization; provenance compression can allow coherent but inaccurate endpoints; slack modulates correction latency.

**UNVERIFIED:** the hypothesized human mechanisms, time scales, parameters, and the utility of the proposed diagnostic measurements.

**Next verdict-changing step:** implement preregistered unfamiliar finite-task trials that separate attention, interpretation, action, provenance retention, and external correctness, with explicit positive/negative/null/mutation controls and held-out tasks. [See the probe plan](PROBES.md).

**Conservation rule for future work:** preserve the *distinction between felt coherence and reality-coupled correction* even if every proposed mathematical implementation here is discarded.
