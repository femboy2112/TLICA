# Probe Program — Frame Transport, Salience, and Provenance

**Status:** preregistration-style proposal; **NO HUMAN PROBES RUN**.  
**Goal:** discriminate models that fit the same phenomenological description while controlling for task skill, memory, affect, and social pressure.  
**Rule:** fit examples are not holdouts; every factorial interaction requires every cell. Preserve raw data, failed trials, excluded cases, source families, and exact software versions.

## 0. Rival family (finite, falsifiable)

- **M0: single-state baseline.** Behavior depends on current task difficulty and explicit reward; neither hidden frame nor provenance state adds prediction.
- **M1: retrieval-access gate.** Context changes which already known content is retrievable; controlling for active retrieval should substantially reduce the context effect.
- **M2: action-access gate.** Relevant knowledge remains fully accessible, but initiation/execution routes change; reminders alone do not normalize behavior.
- **M3: salience-valuation gate.** Knowledge and mechanical task skill remain accessible; priority assigned to doing the task changes with felt consequence or context.
- **M4: frame-authorization drift.** The admissibility of an update is judged by a frame that the preceding updates themselves altered; short locally approved steps can reach an endpoint rejected from the starting frame.
- **M5: provenance compression.** Different histories become indistinguishable through a coarse accessible summary; external records restore some distinctions, possibly not their prior affective force.
- **M6: fixed-invariant controller.** A genuine fixed guard is checked at *every* update, preventing global violation regardless of step size.
- **M7: self-confirming coherence.** Encountering anomalies increases justification for the active model without producing a matching improvement on held-out predictions.
- **M8: external-source/error correction.** Credible disconfirming evidence improves held-out predictions, with latency potentially influenced by independently measured available slack.

These are alternative *components*, not mutually exclusive personality types; fit mixtures only after simpler versions fail on preregistered criteria.

## 1. Tier 0: deterministic finite witness (mathematics only)

See [finite_witness.py](finite_witness.py). Positive cases:

1. Every transition preserving a fixed invariant preserves the invariant at the endpoint.
2. Locally adjacent updates can cross a distinct global guard.
3. Two distinct update histories can share the same compressed observable summary.
4. A task can be known without meeting the stipulated initiation threshold.

Negative/mutation controls:

- Inject one transition that violates the supposed fixed invariant: the guard must catch it.
- Replace a local-adjacency check by the fixed global guard: the "bypass" must fail.
- Retain the complete history instead of a coarse summary: reconstruction must be unambiguous.
- Increase contextual support without changing skill: only the activation flag should change in the illustrative model.

Null control: a no-op frame transition must not change authorization or observed salience.

**Pass:** all specified outcomes observed in a fresh run with an independent implementation.  
**Fail:** a witness violates its own definitions or calibration.  
**Ambiguous:** inability to execute or compare.  
**Interpretation boundary:** passing proves consistency of the finite *toy*, not cognitive truth.

## 2. Tier 1: low-stakes unfamiliar-task access experiment

Goal: distinguish inaccessible information (M1), inaccessible actions (M2), and motivational salience (M3) from the simple payoff baseline (M0).

Construct unfamiliar, non-clinical puzzles with independently scored solutions; ensure participants demonstrate underlying competence before measuring initiation. Randomize 2 × 2 × 2 conditions:

1. **Scaffolding**: explicit ordered substeps provided vs outcome specified only.
2. **Relevance linkage**: target connected to a transparently valued downstream goal vs isolated as a neutral subtask. Keep actual compensation and task difficulty matched.
3. **Opportunity window**: short vs long, disclosed accurately and without consequential pressure.

All eight combinations must exist, with task identity counterbalanced. No misleading real-world jeopardy, no deception about meaningful consequences, and no engineered distress.

Measurements: time to first action, total work, solution quality, eye/attention proxies where available, explicit recall of task instructions, value/interest ratings, and difference between recall of requirements and actual ability to start.

**Predictions, declared before results:**

- M1: once actual retrieval of necessary steps is matched, large context effects attenuate.
- M2: reminding participants of all required steps can leave an initiation deficit while providing an executable next-action affordance helps.
- M3: goal linkage and time-to-consequence affect initiation without proportional changes in knowledge or solution accuracy, beyond the effort/payoff account.
- M0: a preregistered model of payoff, effort and difficulty explains holdout behavior as well as the augmented model.

**Controls:** simple mastered baseline, objectively novel task, shuffled labels, matched payoffs, no-significance manipulation, order effects, ceiling/floor checks, attention/comprehension checks, within-subject counterbalancing.

**Pass for a specific mechanism:** its unique predicted contrast survives preregistered held-out tasks and outperforms M0 beyond uncertainty.  
**Fail:** baseline rivals suffice or the claimed dissociation is absent.  
**Ambiguous:** manipulations change payoffs, skill, anxiety, or comprehension unintentionally; weak statistical power or floor/ceiling effects.

## 3. Tier 2: frame authorization and source-preservation experiment

Use a **non-personal simulated decision problem**, not a real risky decision. A participant or software agent evaluates a series of fictional project choices with explicit evidence. There is a declared source-based rule $I$ and a separate subjective local acceptance judgment $L$.

Factorial design: 2 × 2 × 2 (all eight cells):

- **Sequence:** one proposed endpoint change vs multiple smaller changes with same endpoint.
- **Criterion visibility:** external fixed guard always visible vs local reasoner relying on current representation.
- **Provenance:** complete source and update log visible vs compressed summary available.

Hold identical original evidence, ultimate proposed action, and objective outcome. Randomize scenario labels to avoid fitting one narrative. A missing cell prevents attribution of mixed terms.

**M4 prediction:** step decomposition has greater effect when the criterion is *state-relative*, and fixed guard visibility weakens the effect.  
**M6 prediction:** any path that violates the fixed guard is rejected when the guard is actually checked.  
**M5 prediction:** summary compression impairs source-history discrimination more than endpoint recall; restoring external records should selectively improve discrimination.  
**Alternative:** the effect is mere repetition, fatigue, demand characteristics, recency, or generic persuasion.

Controls: no-op steps, a path that genuinely improves evidence and warrants revision (positive correction), a path with incremental unsupported changes (negative), mutated guard and changed step ordering, placebo repetition with no new information, role reversal.

Measure *three distinct* outcomes: endpoint acceptance, objective rule compliance, and ability to identify which evidence licenses the endpoint. Do not treat agreement as correctness.

**Pass:** a preregistered interaction fits M4 or M5, while independent rule-compliance scoring remains grounded.  
**Fail:** equal effects for fixed guard and drift conditions, or trivial repeated exposure explains everything.  
**Ambiguous:** participants cannot understand the fixed guard or compressed view carries unequal task-relevant evidence.

## 4. Tier 3: correction versus self-confirmation

Construct an unfamiliar rule-learning environment with a hidden deterministic rule and deliberately misleading finite training examples. Compare two interventions on the same error:

- independently verified disconfirming information with accessible provenance;
- a fluent, coherent explanation that fits already seen examples but fails new cases.

Participants predict outcomes on untouched holdouts before and after each intervention. Predeclare confidence calibration, error, abstention, source citation quality, and correction latency. External observers blind to condition grade evidence quality.

**Correction success:** held-out error falls and source fidelity improves without post hoc label switching.  
**Self-confirmation:** the participant reports more coherent understanding but predictive error stays constant or rises.  
**Unresolved:** evidence is insufficient; deferral or additional probing is recorded as a legitimate action, but cost of delay is also scored.

Possible slack manipulation should be *benign and independently measured* (e.g., voluntary time budget or optional breaks), not created through substantial distress or interpersonal threats. Separate immediate expression from delayed privately measured judgment.

**Pass:** epistemic correction and coherence-only increases produce distinguishable prospective outcomes.  
**Fail:** claimed contrast disappears with independent checking or does not transfer.  
**Ambiguous:** errors lack diagnostic feedback, repeated testing teaches the target rule, or participants infer hypotheses.

## 5. Tier 4: longitudinal provenance (future, optional)

A consent-based study may track low-stakes task decisions with event-local source snapshots and delayed recall. Important outputs:

- exact original written objections;
- subsequent acceptance and changes in objective evidence;
- later narrative reconstruction;
- later ability to *feel* prior salience (if requested);
- later behavior under a matched safe task;
- correction when the old record is reintroduced.

Avoid acquiring clinical history or private identity details; favor randomly generated fictional decisions. For real human data, require explicit participant consent, appropriate ethics review, strong privacy separation, and a retention/deletion plan.

Prediction candidate: summary compression produces greater divergence between current confidence and evidence provenance than full-history access. Note that introspective reinstatement is hard to measure and subjective reports may not distinguish retrieval from reconstruction.

## 6. Missing lamps and alternate explanations

| Unresolved distinction | Present obstruction | Next lamp |
|---|---|---|
| Emotion rises slower vs emotion guides action slower | Same coarse self-report | Independent time-resolved affect and action measures |
| Memory inaccessible vs irrelevant | Retrieval and salience covary | Recognition with controlled retrieval cues plus separate value measures |
| Accurate reframing vs rationalization | Both feel coherent | Novel independent predictions; source provenance |
| Legitimate transition vs risk suppression | Felt permission differs from factual support | Frozen risk record and blinded external scoring |
| Low slack slows updating vs only expression | Outward response is ambiguous | Delayed confidential assessment of belief and prediction |
| Stable self versus compatible local realizations | Many models fit introspection | Cross-context predictions and transport fidelity |
| Abstention intelligent vs avoidance | Both prevent immediate action | Cost of delay, reversible actions, information gain |

## 7. Reporting discipline and ethics

- Archive hypotheses and predictions **before** data; keep model development trials separate from fresh holdouts.
- Report calibration runs and mutations, all cells in each claimed factorial interaction, exclusions, effect sizes and uncertainty, source families, and negative results.
- Use independent scoring or independent implementations where possible. Repeated sampling from one model does not create independent witnesses.
- A beautiful analogical model, a mathematically proved toy, and an empirical human mechanism are **three different objects**.
- No pharmacological intervention, self-harm experiment, intoxicant challenge, emotional distress induction, or consequential personal decision is an acceptable probe in this project.
- No participant-level diagnosis or coercive screening follows from the model.
- If a strong claim fails, mark it **Refuted at its stated scope** and keep the failure visible.

**Recommended first move:** implement and audit Tier 0, then seek a separate investigator's preregistered Tier 2 *fictional* task using a new source/evidence corpus. The decisive target is a contrast between locally acceptable drift and external-truth correction, not a demonstration that some people can be persuaded.
