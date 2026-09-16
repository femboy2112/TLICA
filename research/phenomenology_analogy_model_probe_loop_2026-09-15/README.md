# From Felt Structure to Falsifiable Model

## The Phenomenology–Analogy–Model–Probe Loop

**Date:** 2026-09-15  
**Status:** research-tier methodology note  
**Foundation impact:** none; foundation v5.5.0 untouched  
**Primary claim status:** the method is an explicit reconstruction of the author's stated research practice; its usefulness as a generally superior discovery method is **CONJECTURED / UNVERIFIED**.

> **Author's originating compression**
>
> Find analogy that fits phenomena phenomenologically.  
> Map the analogy to math.  
> Now you have a model.  
> Drive the math with inputs not yet phenomenologically experienced and see what drops out.  
> Test those against reality.  
> Update the model based on results.

This note makes that compression explicit enough to audit, reuse, falsify, and eventually internalize into TLICA's main research practice without mistaking it for a new foundation coordinate or a theorem about cognition.

The shortest version is:

\[
\boxed{
\text{phenomenology}
\to
\text{analogy}
\to
\text{structural extraction}
\to
\text{formal model}
\to
\text{novel implication}
\to
\text{probe}
\to
\text{revision}
}
\]

Or in prose:

> **The analogy proposes a candidate structure. Mathematics propagates the consequences of that structure. Reality decides which parts survive.**

That last sentence is the methodological firewall. A resonant analogy is not evidence that two domains share an ontology, mechanism, or governing law. It is a search instrument for finding a candidate invariant structure that can later earn or lose warrant.

---

# 1. Why this needed to be written down

A recurring pattern across this repository is easy to recognize after the fact:

1. a lived or observed phenomenon presents a recognizable **shape**;
2. some other domain supplies an analogy with a similar relational shape;
3. the analogy is stripped down into variables, relations, constraints, and dynamics;
4. the resulting formal object is driven into cases that were not used to construct it;
5. those outputs are compared with reality;
6. surviving structure is retained, failing structure is weakened, localized, or removed.

The repository already contains fragments of this discipline. TLICA itself is described as developed first-hand and then formalized. The application papers are expected to make phenomena fall out of existing apparatus rather than add bespoke machinery whenever a new case appears. *The Cave's Lagrange Points* openly borrows a physical analogy while preserving its limits and leaving resulting predictions UNVERIFIED. The dynamical-substrate program goes further and asks whether borrowed motion language such as *reachability* or *momentum* is literal mathematics or merely useful imagery; some pieces survive and some are explicitly refuted.

Those are not independent confirmations of the method. They share project provenance. They are, however, internal specimens showing that the author is already using the loop in practice.

The missing object was the **method itself**.

---

# 2. The object being modeled

Let \(X\) denote a target phenomenon. \(X\) may be:

- a first-person phenomenological pattern;
- a social or institutional pattern;
- a computational behavior;
- a mathematical regularity;
- a physical observation;
- or any other domain in which the author can identify repeatable structure.

The method does **not** begin by assuming the target is mathematically identical to some known source system. It begins with a weaker abductive question:

> **What known system has a relational organization that resembles the phenomenon closely enough to suggest a candidate formal structure?**

Call the source analogy \(A\).

The first stage is therefore not deduction. It is **abductive search**.

\[
X \xrightarrow{\text{abductive analogy search}} A.
\]

The output of this stage is only a candidate source system.

---

# 3. Stage I — phenomenological capture

Before finding an analogy, write down the target phenomenon with as little imported theory as possible.

A useful capture record has at least five parts:

1. **Objects or states** — what appears to exist in the phenomenon?
2. **Relations** — what depends on, resists, attracts, excludes, preserves, or transforms what?
3. **Temporal structure** — what changes, persists, oscillates, accumulates, decays, or bifurcates?
4. **Invariants or near-invariants** — what seems stable across changes of context or frame?
5. **Known discontinuities** — where does the intuitive picture break?

For first-person material, the phenomenological report is evidence that the experience was reported that way. It is **not automatically evidence for the proposed mechanism** behind the experience.

This distinction should remain explicit in the claim ledger.

A minimal notation is:

\[
P = (O_X, R_X, T_X, I_X, B_X),
\]

where \(O_X\) are observed objects/states, \(R_X\) observed relations, \(T_X\) temporal features, \(I_X\) apparent invariants, and \(B_X\) known breaks or boundaries.

This object \(P\) is the **phenomenological capture**, not yet the model.

---

# 4. Stage II — analogy search

Choose a source domain \(A\) because some of its relational structure resembles \(P\).

Examples of source domains include:

- dynamical systems;
- control theory;
- fluid flow;
- graph theory;
- information theory;
- statistical mechanics;
- orbital mechanics;
- type systems;
- category theory;
- sheaf/gluing constructions;
- optimization;
- games;
- markets;
- biological regulation.

The source should be selected for **structural fit**, not prestige or mathematical sophistication.

A simple analogy can be better than a glamorous one if it creates a cleaner discriminating probe.

At this stage, one may say:

> "This behaves *as if* it has an attractor-like structure."

One may not yet say:

> "Therefore the phenomenon literally is a dynamical system with the same attractor law."

The former is a search proposal. The latter is an ontological promotion that has not been earned.

---

# 5. Stage III — the bridge contract

This is the load-bearing step.

An analogy becomes scientifically useful only after its proposed transport is declared.

Define a **bridge contract** \(B\) containing:

\[
B = (b_O,b_R,b_I,b_D,b_{\neg}),
\]

where:

- \(b_O\): which source objects correspond to which target objects;
- \(b_R\): which source relations correspond to which target relations;
- \(b_I\): which invariants are proposed to survive transport;
- \(b_D\): which dynamics or transformation rules are proposed to survive;
- \(b_{\neg}\): which source properties are explicitly **not** being transported.

The negative map \(b_{\neg}\) matters as much as the positive map. It prevents the source analogy from quietly importing irrelevant ontology.

For example, borrowing an orbital-mechanics stability picture does not imply literal masses, gravity, Euclidean space, or inverse-square forces in the target domain.

A useful operational rule is:

> **No declared bridge, no transported claim.**

If the analogy cannot state what is preserved and what is not preserved, it remains metaphor.

---

# 6. Stage IV — extract the candidate shared structure

The source analogy is a scaffold. The goal is not to keep the scaffold forever.

Suppose the source system \(A\) and target phenomenon \(X\) appear to share some reduced structure \(Q\). Conceptually:

\[
A \xrightarrow{q_A} Q \xleftarrow{q_X} X.
\]

The method seeks \(Q\), not an identity \(A=X\).

\(Q\) may preserve only a small set of features:

- attractor/basin structure;
- graph connectivity;
- threshold behavior;
- hysteresis;
- phase-transition shape;
- conservation-like constraints;
- partial order;
- feedback sign;
- bottleneck topology;
- equivalence classes;
- symmetry or symmetry breaking;
- reachability;
- observability;
- controllability;
- information loss;
- or another relational invariant.

This gives a crucial criterion:

> **If removing the imagery of the analogy destroys the model, the work probably has a mathematical metaphor, not yet a mathematical model.**

The mature object should survive after the ladder is kicked away.

---

# 7. Stage V — formalization

Write the transported structure as an explicit mathematical object.

A generic model can be represented as

\[
M=(S,\Theta,F,C,\mathcal O),
\]

where:

- \(S\) is a state space;
- \(\Theta\) is a parameter set;
- \(F\) is a family of transformations/dynamics;
- \(C\) is a set of constraints;
- \(\mathcal O\) is an observation map from model states to quantities that can actually be compared with evidence.

Not every project needs every component. The point is explicitness.

Formalization should answer:

1. What are the model's primitive objects?
2. Which variables are measured, inferred, or merely schematic?
3. Which parameters were chosen from the motivating examples?
4. Which equations are definitions versus empirical hypotheses?
5. Which consequences follow deductively once the assumptions are granted?
6. What observation map connects the formal object back to reality?

A symbol does not become a measurement merely because it has a Greek letter.

A formal identity derived from model assumptions is **Disclosed at the model boundary**. It does not thereby validate the assumptions or the model's empirical interpretation.

---

# 8. Stage VI — separate fit data from truth debt

Let \(D_{\mathrm{fit}}\) denote all evidence that materially influenced:

- the selection of the analogy;
- the bridge contract;
- the model class;
- parameter choices;
- or the interpretation of outputs.

Anything in \(D_{\mathrm{fit}}\) has already paid for construction. It cannot also serve as clean validation.

This is especially important for introspective research because the author may have broad latent familiarity with her own history. "I did not consciously think of this example while writing the equation" is weaker than a genuine holdout.

Where possible, truth debt should be paid using:

- a future experience recorded after prediction;
- an external dataset not inspected during construction;
- a blinded case;
- a new subject/population;
- a hostile parameter regime;
- an independent implementation;
- a known result the model was not tuned to recover;
- a deliberately constructed counterexample;
- or a rival-model discrimination test.

The core rule is:

\[
D_{\mathrm{test}} \cap D_{\mathrm{fit}} \approx \varnothing
\]

at the level that actually matters for the claim.

Exact statistical independence is often impossible. The provenance relationship should nevertheless be stated.

---

# 9. Stage VII — drive the mathematics beyond phenomenology

This is the generative heart of the method.

Choose an input, state, parameter regime, or configuration \(u^*\) that was not part of the motivating phenomenology.

Then compute:

\[
\hat y^* = \mathcal O(M(u^*)).
\]

The question is:

> **If the extracted structure is real enough to matter, what does it force or strongly constrain somewhere I have not already looked?**

This is where the analogy stops doing the work.

The mathematics now generates consequences that can surprise the person who built the model.

The strongest outputs are those that are:

- specific;
- risky;
- measurable;
- different from rival predictions;
- and difficult to retrofit after the fact.

If the model merely redescribes every possible outcome after it occurs, it has no discriminating power.

---

# 10. Stage VIII — build a discriminating probe

A probe should distinguish live models, not merely produce another compatible anecdote.

Before running it, define at least:

- **pass** — what outcome would count as support for the specific prediction;
- **fail** — what outcome would kill or materially weaken it;
- **ambiguous** — what outcome would show the probe lacked discriminatory power.

Whenever feasible, include:

- positive control;
- negative control;
- null control;
- mutation/perturbation control;
- rival-model predictions;
- raw-output preservation;
- exact configuration/provenance.

For rival models \(M_1,\ldots,M_n\), prefer a probe \(T\) that maximizes separation among predicted outcomes:

\[
T: \{M_i\} \to \{\Pi_i\}
\]

with the practical goal of splitting the largest remaining coherence class.

A probe that every live model passes is not useless, but it does not resolve the load-bearing uncertainty.

---

# 11. Stage IX — compare prediction and reality

Observe \(y^*\) and compute a residual or discrepancy object

\[
r^* = \Delta(\hat y^*,y^*).
\]

The residual should not immediately be translated into "the model is true" or "the model is false."

Instead localize the failure.

Possible failure classes include:

1. **Analogy-selection failure** — the source system highlighted the wrong structure.
2. **Bridge failure** — the source and target do not preserve the relation that was transported.
3. **Formalization failure** — the intended structure was encoded incorrectly.
4. **Parameter failure** — the model class may survive but the chosen parameterization does not.
5. **Observation-map failure** — the internal model quantity does not correspond to what was measured.
6. **Probe failure** — the experiment did not distinguish the live alternatives.
7. **Domain-boundary discovery** — the model works only in a narrower regime than originally stated.
8. **Source/provenance defect** — the evidence used for comparison was wrong, duplicated, dependent, or misclassified.

This turns "being wrong" into useful information about **where the transport broke**.

---

# 12. Stage X — update without self-sealing

Let the update operator be

\[
M_{n+1}=U(M_n,r_n,\Pi_n),
\]

where \(\Pi_n\) is the provenance and probe record.

The update may:

- change parameters;
- narrow the valid domain;
- replace the observation map;
- weaken a transported relation;
- replace the source analogy;
- split one model into multiple regimes;
- or refute the model entirely.

A revision is illegitimate if it merely adds enough free machinery to absorb every failure while preserving the headline unchanged.

The loop must be capable of producing:

\[
\boxed{\text{REFUTED}}
\]

as a stable outcome.

Otherwise it is not a falsifiable research method; it is a narrative-preservation engine.

---

# 13. The complete loop

The method can be written as:

\[
P_n
\xrightarrow{\alpha}
A_n
\xrightarrow{B_n}
Q_n
\xrightarrow{\mathcal F}
M_n
\xrightarrow{u^*}
\hat y_n
\xrightarrow{T_n}
y_n
\xrightarrow{\Delta}
r_n
\xrightarrow{U}
M_{n+1}.
\]

Where:

- \(P_n\): phenomenological/observational capture;
- \(\alpha\): abductive analogy search;
- \(A_n\): source analogy;
- \(B_n\): bridge contract;
- \(Q_n\): candidate shared structure;
- \(\mathcal F\): formalization;
- \(M_n\): mathematical model;
- \(u^*\): genuinely new input/regime;
- \(\hat y_n\): prediction;
- \(T_n\): discriminating probe;
- \(y_n\): observation;
- \(r_n\): residual;
- \(U\): revision.

The epistemic direction changes halfway through:

\[
\underbrace{X\to A\to Q\to M}_{\text{abductive / constructive}}
\qquad
\underbrace{M\to \hat y}_{\text{deductive}}
\qquad
\underbrace{\hat y\leftrightarrow y}_{\text{empirical}}
\qquad
\underbrace{r\to M'}_{\text{revision}}.
\]

This separation prevents a common category error: deductive certainty inside \(M\) does not transport backward into certainty that \(M\) correctly models reality.

---

# 14. The four warrant boundaries

The loop contains four distinct warrant boundaries.

## Boundary A — phenomenology to analogy

A good fit licenses:

> "This source domain may expose useful structure."

It does not license:

> "The target literally instantiates the source mechanism."

## Boundary B — analogy to mathematics

A clean formalization licenses:

> "These consequences follow from this transported structure."

It does not license:

> "The transported structure is empirically correct."

## Boundary C — prediction to observation

A successful prediction licenses evidence for the tested claim under the tested conditions.

It does not automatically validate every component of the model.

## Boundary D — repeated success to generality

Repeated survival across independent regimes can corroborate a model.

It does not establish final truth outside the tested closure.

The correct endpoint is dominance within a stated boundary, not metaphysical finality.

---

# 15. Major failure modes

## 15.1 Metaphor poisoning

Unmapped properties of the source analogy leak into the target.

**Control:** explicit \(b_{\neg}\) list.

## 15.2 Resonance laundering

A phenomenologically satisfying analogy is treated as evidence of mechanism.

**Control:** analogy claims remain Conjectured until external consequence survives a probe.

## 15.3 Mathematical costume

A qualitative story receives symbols but no new constraints.

**Control:** require the formalization to forbid some outcomes or generate a nontrivial consequence.

## 15.4 Retrospective prediction

An already-known case is presented as if the model predicted it.

**Control:** maintain \(D_{\mathrm{fit}}\) and timestamp predictions before observing holdouts.

## 15.5 Parameter laundering

Parameters are tuned on test cases without moving those cases back into the fit set.

**Control:** every tuning exposure updates provenance.

## 15.6 Self-sealing revision

Every failure causes a new auxiliary mechanism while the central claim never becomes vulnerable.

**Control:** predeclare kill conditions and complexity penalties.

## 15.7 Bridge drift

The analogy-to-target correspondence changes silently after a failed prediction.

**Control:** version the bridge contract.

## 15.8 Source-map collapse

Multiple apparently independent supports actually derive from the same source, implementation, conversation, dataset, or conceptual lineage.

**Control:** provenance families and leave-one-family-out reasoning.

## 15.9 Identity-coupled defense

The model becomes sufficiently integrated with the author's identity that criticism of the model is experienced as criticism of the self.

**Control:** stronger blinding, hostile probes, explicit rival construction, and separation of autobiographical truth from mechanistic inference. Identity coupling is a reason for stronger controls, never positive evidence.

## 15.10 Infinite analogy freedom

Given enough candidate source domains, some analogy can always be found after the fact.

**Control:** penalize post hoc analogy search; prefer source structures that generate risky novel consequences quickly.

---

# 16. Relation to TLICA

This methodology is **TLICA-compatible but not a new TLICA primitive**.

It does not add a coordinate, mode, prerogative, or dynamical law.

Instead, it describes an author-level research procedure that can use TLICA's existing epistemic discipline:

- keep contact with a phenomenon distinct from the warrant of an explanation;
- keep constructibility/verification access distinct from truth itself;
- keep provenance/source adequacy distinct from internal coherence;
- keep identity/commitment coupling distinct from evidence;
- keep probe availability distinct from confidence;
- do not collapse these diagnostics into one scalar "truth score."

The method can therefore sit **above** individual TLICA applications as a research workflow while remaining compatible with other mathematical and scientific projects that do not use TLICA ontology at all.

This is important: if the method were defined in a way that only TLICA could validate, it would become circular.

---

# 17. Internal specimens already present in the repository

These examples illustrate pieces of the loop. They do **not** independently validate the method because they share author/project provenance.

## 17.1 The Cave's Lagrange Points

[`../../applications/caves_lagrange_points_v0_1_0.md`](../../applications/caves_lagrange_points_v0_1_0.md)

A physical stability analogy is used to model constrained self/configuration dynamics. The paper explicitly preserves the limits of the analogy and leaves its predictions UNVERIFIED.

This is a good specimen of:

\[
\text{phenomenological configuration}
\to
\text{physical analogy}
\to
\text{structural model}
\to
\text{unverified prediction}.
\]

## 17.2 Dynamical substrate / motion-word audit

[`../dynamical_substrate_axioms_2026-09-08.md`](../dynamical_substrate_axioms_2026-09-08.md) and
[`../substrate_round1_reachability_momentum_2026-09-08.md`](../substrate_round1_reachability_momentum_2026-09-08.md)

This program asks whether borrowed mathematical/physical words can be earned literally. Some survive in weaker form; strong literal claims are refuted.

This is an unusually clean specimen of the **revision** stage because the project permits the analogy to lose structure rather than protecting it.

## 17.3 Distributed institutional realization

[`../distributed_institutional_realization_2026-09-15/`](../distributed_institutional_realization_2026-09-15/README.md)

The research program formalizes an initially intuitive social structure, then revises the formal object when the first realization map risks merely renaming its input tuple. The v0.2 quotient construction is an example of residual-driven formal correction.

## 17.4 Developmental substrate nonstationarity

[`../developmental_substrate_nonstationarity_2026-09-15/`](../developmental_substrate_nonstationarity_2026-09-15/README.md)

The originating intuition "constant new blank neurons → noise" was not protected. It was explicitly marked Refuted as stated and replaced by the weaker, better-supported moving-substrate / nonstationarity claim.

That is exactly the kind of update behavior this methodology requires.

---

# 18. A reusable research template

Every future analogy-driven project can instantiate the following record.

```text
TARGET PHENOMENON
- What is observed/felt?
- Scope?
- What is raw report versus interpretation?

SOURCE ANALOGY
- Why this source?
- What relational structure appears similar?
- What alternatives were considered?

BRIDGE CONTRACT
- Source objects -> target objects
- Source relations -> target relations
- Proposed invariants
- Proposed dynamics
- Explicit non-transports
- Kill conditions

FORMAL MODEL
- State space
- Parameters
- Dynamics/operators
- Constraints
- Observation map
- Definitions vs hypotheses

FIT PROVENANCE
- What evidence influenced analogy/model/parameters?
- Shared source families?
- Potential leakage?

NOVEL DRIVE
- New input/regime u*
- Prediction y_hat*
- Prediction timestamp
- Rival predictions

PROBE
- Pass
- Fail
- Ambiguous
- Controls
- Raw outputs

RESULT
- Observation y*
- Residual
- Which failure class is implicated?

REVISION
- Keep
- Narrow
- Replace
- Refute
- New truth debt

CLAIM LEDGER
- Disclosed
- Corroborated
- Observed
- Conjectured
- UNVERIFIED
- Dark
- Refuted
```

---

# 19. A stronger version: analogy competition

The method becomes more reliable if it does not stop at the first resonant analogy.

Let \(A_1,\ldots,A_k\) be candidate analogies producing models \(M_1,\ldots,M_k\).

Instead of asking only whether \(M_1\) can explain the motivating phenomenon, ask for an input \(u^*\) such that

\[
\mathcal O(M_i(u^*))
\]

separates the rivals as much as possible.

This reframes analogy selection as a tournament of consequence rather than a beauty contest.

A model earns preference only by surviving probes that live rivals do not survive, or by explaining the same evidence with fewer unsupported commitments and fewer residual contradictions.

No score or scalar truth probability is required.

---

# 20. A stronger version: bridge mutation tests

A bridge contract itself can be tested.

Suppose the model depends on transported relation \(r\). Construct a mutated bridge \(B^{-r}\) that removes or reverses \(r\).

Then compare:

\[
M_B \quad \text{versus} \quad M_{B^{-r}}.
\]

If both generate indistinguishable outputs across all available probes, the transported relation is not yet empirically load-bearing.

Its status should remain schematic or Dark rather than being narrated as established mechanism.

This is useful because it tests the **mapping**, not only the final model.

---

# 21. What would validate the method itself?

This note should not exempt its own methodology from its standard.

The author reports that this loop describes how she actually discovers models. That establishes provenance of the method as a self-description.

The stronger claim — that this procedure is reliably useful — requires evidence.

A direct test could compare research problems approached under two workflows:

- **W1:** free-form analogy-driven reasoning without an explicit bridge/holdout/probe ledger;
- **W2:** the full Phenomenology–Analogy–Model–Probe loop with declared bridge contracts, fit provenance, novel drives, and preregistered discrimination criteria.

Candidate outcomes include:

- number of post hoc claims caught;
- number of explicit refutations accepted;
- held-out predictive performance;
- rate of bridge revisions;
- complexity growth after failures;
- reproducibility across independent implementers;
- recovery of known structures under blinded tasks.

Until such tests exist, the general superiority of the loop remains **UNVERIFIED**.

---

# 22. The deepest methodological point

The procedure begins with something potentially subjective — phenomenological resemblance — but it does not have to end there.

The analogy is allowed to be psychologically generated because its job is **candidate generation**.

Warrant comes later.

The conversion is:

\[
\boxed{
\text{subjectively noticed resemblance}
\to
\text{explicit structural hypothesis}
\to
\text{deductive consequence}
\to
\text{objective opportunity for failure}
}
\]

That is the move that keeps the method from collapsing into poetic analogy.

The model is not rewarded for explaining the experience that inspired it. That is the entry fee.

The model earns its keep only when it reaches beyond the phenomenology that produced it.

---

# 23. Compact statement for future use

> **Phenomenological Model-Building Loop.** Begin from a phenomenon whose relational structure can be described independently of a preferred explanation. Search for a source analogy that exposes a candidate structure. Declare a bridge contract specifying what is and is not transported. Strip away the source imagery and formalize the surviving structure as a model with an observation map. Record all motivating evidence as fit provenance. Drive the model into a genuinely new regime, derive a risky consequence, and predeclare a probe capable of distinguishing it from live rivals. Compare prediction with observation, localize the residual to the analogy, bridge, formalization, parameters, observation map, probe, or domain boundary, and revise accordingly. A resonant analogy generates hypotheses; mathematics propagates them; reality supplies warrant.

---

# 24. Current verdict

**Disclosed:** the loop can be specified as a coherent research protocol, and its internal warrant boundaries are logically distinct.

**Observed / author-reported:** the originating six-line compression is the author's stated description of her own recurring research meta.

**Disclosed from repository structure:** multiple TLICA research/application artifacts instantiate parts of this workflow, including explicit analogy limits, model revision, refutation, and holdout/probe discipline.

**Conjectured:** the explicit loop accurately captures a substantial portion of the author's productive cross-domain model-building practice.

**UNVERIFIED:** using the explicit protocol improves discovery, prediction, calibration, or error correction relative to other research workflows.

**Dark:** whether there exists a deeper cognitive mechanism explaining why this style of analogy search is productive for this author. The present note does not attempt that theory.

**Boundary:** no amount of internal mathematical elegance upgrades an analogy into an empirical mechanism without an external discriminating probe.
