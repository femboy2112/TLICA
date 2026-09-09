# Geometry of Actualization — formal specification and discriminating probes

**Version:** 0.1.0, 2026-09-07. Companion to [MANUSCRIPT.md](MANUSCRIPT.md). This is an application-level research specification, not a complete decision theory. No human experiment has run.

## 1. Object, outcome, and acceptance boundary

**Object:** A bounded episode in which one or more orientations are available to an indexed subject, against a history and environment. The target is the relation between the organization of support and an action trajectory.

**Outcomes:** Declared observables such as initiation, voluntary continuation, switching, delay, reported reasons, implementation success, and changes in the availability of alternatives. Do not replace them with a scalar authenticity score.

**Acceptance:** A useful annotation must preserve relevant distinctions, be assignable without looking at the outcome it will predict, and earn discrimination against simpler rival accounts on held-out cases. A more elaborate description is not automatically a better model.

**Non-goals:** Proving free will, measuring sovereignty as a universal trait, diagnosing readers, validating TLICA from literature, predicting moral worth, or formalizing Bataille's entire philosophy.

## 2. Minimal episode schema

A record should contain the following fields. A field can be unknown; its absence must not be silently coded as zero.

```text
episode_id; subject_index; recording_time; target_interval
external_context; task_constraints; available_resources
candidate_orientations; declared_action_observables
content_records:
  content_id
  occurrence_time
  temporal_reference: one or more of past / present / future / unspecified
  referent_kind: self-representation / other-person / institution / object / other
  identity_treatment: integrated / differentiated / neutral / mixed / unknown
  evidence_kind: observed / reported / inferred / imagined / unresolved
  provenance_family; source_reference; annotation_time
relation_records:
  source_content_ids; target_content_ids
  relation_type; logical_operator (AND / OR / other declared operator)
  claimed_role: operative_cause / stated_reason / association / normative_reason / unknown
  evidence_status; alternative_explanations
implementation_constraints; feedback_observations
rival_models; preregistered_predictions; verdict
```

Temporal reference concerns what a representation is about. It does not relocate the content outside its occurrence time. Identity treatment and referent kind are separate: another person can be both an other and identity-integrated. Neutral is a mode of treatment, not the assertion that a content is meaningless or inactive.

Do not infer a cause from the ordering of a retrospective narrative. Do not encode unknown motives as if they were observed edges. Preserve disagreements between annotators instead of resolving them by majority vote without examining sources.

## 3. Conservativity: exactly what the formal claim buys

Let an existing architecture specify admissible states \(\Omega\) and an admissible one-step transition relation \(\mathcal R\subseteq\Omega\times\Omega\). No deterministic transition law is assumed.

Let \(\widetilde\Omega\) contain annotated states, with a forgetful map

\[
F:\widetilde\Omega\to\Omega.
\]

Call an extension conservative at the state/one-step level only if:

1. \(F\) is surjective: every old state has at least one permitted annotation;
2. every annotated transition projects to an old transition;
3. every old transition has an annotated lift.

Equivalently,

\[
F(\widetilde\Omega)=\Omega,
\qquad
(F\times F)(\widetilde{\mathcal R})=\mathcal R.
\]

**Conditional proposition.** Under these conditions, forgetting annotation changes neither the admissible state set nor the admissible one-step transitions.

**Proof.** The first equality gives exactly the old states. Conditions 2 and 3 give respectively the two inclusions needed for the second equality. Nothing stronger follows. In particular, one-step coverage alone need not guarantee that arbitrary multi-step old trajectories have mutually compatible annotated lifts. Trajectory-level conservativity requires an explicit lifting condition for whole admissible trajectories. □

A simple sufficient construction attaches nonempty annotation sets \(C(x)\) to old states and allows all annotated transitions whose underlying states are related by \(\mathcal R\). More restrictive, temporally consistent annotations require an actual coverage check rather than an assertion that they are merely descriptive.

This result is largely bookkeeping by design. It does not prove psychological adequacy, empirical explanatory gain, or even that the current informal TLICA descriptions have already fixed a complete transition relation. Any new claim about action-priority arbitration, mandatory arousal, causal feedback, or available transitions remains a substantive assumption.

## 4. Support dependence without a truth score

For a stipulated finite model, let \(z\) be a complete assignment of named conditions and \(f_H(z)\) a declared action outcome under rival rule \(H\). Let \(A_c\) be a declared change to condition \(c\), with its other effects explicitly specified.

A **support-dependence signature** is the vector

\[
\mathbf d_H(z)=\bigl(f_H(z),f_H(A_{c_1}z),\ldots,f_H(A_{c_k}z)\bigr).
\]

The vector is not a psychological probability distribution or a truth score. It simply lists the model's outputs under named conditions. A human study would need operational measurements and an identified intervention rather than a literal deletion of a thought.

### 4.1 Baseline non-identifiability

Take conditions \(e\) for feasibility, \(a\) for significance of the activity, \(p\) for useful payoff, and \(o\) for an oppositional cue. Define illustrative rules:

\[
f_A=e\land a,\quad f_P=e\land p,\quad f_O=e\land o.
\]

At \(e=a=p=o=1\), all three produce action. Removing \(p\) separates \(f_P\) from the other two. Removing \(o\) separates \(f_O\). Identical baseline actions therefore do not identify these stipulated supports.

This is a counterexample to identification from action alone, not a proposed three-type psychology. The rule names do not establish that a participant's activity really has one of these causes.

### 4.2 Redundant and conjunctive support

Compare

\[
f_R=e\land(a\lor p)
\]

with

\[
f_C=e\land a\land p.
\]

The first survives either single withdrawal; the second survives neither. A null single-withdrawal result cannot establish that a support never matters: another support may substitute. Conversely, an ordinary graph with two incoming edges must not silently decide whether those edges are OR alternatives or AND requirements.

A minimal sufficient support set is inclusion-minimal, not necessarily unique. Multiple sets are part of the result. The accompanying script enumerates them only for its tiny complete Boolean models; it does not identify sufficient psychological causes.

### 4.3 Dependence is not unfreedom

For a binary signal \(s\), both \(f(s)=s\) and \(g(s)=1-s\) are nonconstant. Both depend on the signal. This is all the anti-script argument proves.

The inference from dependence to diminished freedom requires additional premises about coercion, endorsement, options, control, and the relevant conception of freedom. The model must permit freely chosen cooperation and principled resistance.

## 5. What not to call an ablation

The question “Would I do this if nobody knew?” does not literally remove not-self from the mind. It changes a conversational prompt. The person may still imagine an audience, evaluate themselves through internalized standards, or find the hypothetical unbelievable.

Likewise, removing a useful consequence can change resources or task meaning rather than isolate justification. Removing the possibility of retaining an artwork changes more than future ownership. Asking someone to imagine having no artistic history changes the subject being modeled rather than cleanly altering one present relation.

These questions are useful for generating rival hypotheses. Their answers are self-reports under specified prompts, not decisive causal interventions.

Use three distinct labels:

- **Textual omission:** an analyst changes which passage or source family informs an interpretation.
- **Prompted counterfactual:** a participant reports a response to a hypothetical situation.
- **Implemented intervention:** an actual, ethically permitted contextual feature is changed and observables are measured.

Never promote the first or second into the third without evidence.

## 6. Pre-specified verdicts

Before running a probe, record the preferred explanation, at least one plausible rival, and the outcomes below.

**Pass:** The registered separating prediction occurs, the manipulation check succeeds, confounding changes remain within declared tolerances, and relevant controls behave as specified. This supports a scoped contrast, not the framework as a whole.

**Fail:** An informative, adequately implemented probe produces a result incompatible with the registered claim. Preserve the result and revise or reject the claim. Do not rescue it solely by relabeling hidden edges afterward.

**Ambiguous:** The manipulation failed, the rival predicts the same output, the measurement was insufficiently sensitive, a prerequisite changed, carryover dominates, or the evidence cannot identify the supposed mediator. An ambiguous result is not a weak pass.

Quantitative tolerances, sample size, stopping rules, and outcome scales must be set for the actual study, not supplied as universal numbers here. No power calculation or validated psychological instrument has been established in this package.

## 7. Probe A: activity support versus useful-payoff support

**Setting:** Consensual, low-stakes voluntary tasks with modest, nonessential incentives. Painting and résumé work are motivating examples, not assigned psychological categories.

**Rivals:** Present activity significance; external useful payoff; anticipated approval; habit; demand compliance; fatigue; inability to switch; mixed or redundant support.

**Intervention:** Vary a credible, nonessential useful outcome while preserving task availability, instructions, cost, resources, and the ability to stop as far as practicable. Separately vary identifiable evaluation only if needed and ethically permissible.

**Outcomes:** Voluntary continuation, initiation of an alternative, time allocation, reported reasons before and after, belief in the manipulation, fatigue, and practical feasibility.

**Separating prediction:** A preassigned payoff-dependent account predicts a change under payoff withdrawal that an activity-supported rival does not, subject to measured redundancy. A generic “more emotional intensity means more action” account does not predict the specific pattern unless supplied further assumptions.

**Positive control:** A task deliberately constructed around an explicit minor instrumental objective should respond when that objective is withdrawn.

**Null control:** A change irrelevant to the registered support should not produce the same systematic response.

**Negative control:** With no credible usable route to the objective, a model that predicts action solely from declared payoff should fail its own feasibility condition.

**Confounds:** Loss of trust, inferred disapproval, task redefinition, unmeasured audience, economic pressure, disappointment, order effects, or ethical restrictions that prevent a credible manipulation.

No intervention may threaten income needed for living, housing, safety, medical access, or other necessities. A simulated or pilot task is not evidence about actual employment until transfer has been tested.

## 8. Probe B: opposition versus principled refusal

**Setting:** Consensual scenarios or modest optional tasks; never covert tests imposed on customers or subordinates.

**Rivals:** Content-based objection; opposition to the source; sensitivity to coercive delivery; ordinary preference; fatigue; fear; a principled boundary; demand characteristics.

**Design:** Counterbalance the proposal's content and source where ethical. Preserve a genuine ability to refuse. Record objections before revealing outcome incentives. Test whether changing the advocated option predictably flips the selected response when the person's stated substantive commitments remain fixed.

**Separating prediction:** Pure signal-negation predicts tracking the contrary of the signal across content changes. Principled refusal can remain stable across those changes when its underlying reason remains. Neither model is validated by a single angry or compliant response.

**Ambiguity condition:** Changing the source also changes credibility, power, information, or risk. Then the observed difference does not isolate oppositional dependence.

**Mutation control in the formal toy:** Replace an opposition-dependent rule with an activity-dependent one. The cue-withdrawal test must distinguish the mutation or it is not testing the claimed relation.

## 9. Probe C: Wallacean timing rather than retrospective fluency

**Setting:** Low-stakes interpretation/response tasks with participant consent.

**Rivals:** Timely reorientation; retrospective rationalization; generic pleasant wording; extra processing time; experimenter compliance; prior habit; factual learning.

**Design:** Compare a relevant reflection cue before selection, the same cue after selection, a time-matched irrelevant cue, and a baseline. Use distinct matched items or counterbalancing to limit practice and carryover. Record whether the alternative actually became live and whether implementation was available.

**Separating prediction:** If the proposal is specifically about preselection transport, the postselection cue cannot change an already completed choice. It may change later choices. If only reports change while contemporaneous behavior and alternative availability do not, the claimed online effect is not established.

**Guard:** An alternative interpretation can be a possibility without being a new fact about a person. Score factual calibration separately from generosity of interpretation.

**Boundary control:** Some scenarios should include clear misconduct. A model that calls every boundary failure compassion has lost the distinction between reorientation and acquiescence.

## 10. Full factorial contrasts and invariance

Where a study claims that payoff and audience interact, all four conditions are required. For a predeclared scalar observable with means \(y_{ij}\), define

\[
\Delta_{PA}=y_{11}-y_{10}-y_{01}+y_{00}.
\]

The sign convention is fixed by that equation. Missing cells prevent estimating this complete contrast. In repeated-measures settings, carryover and order must be handled; in between-person settings, allocation and confounding need attention. Multiple observables require separate contrasts, not an undeclared composite.

A nonzero contrast on this declared scale is not a mechanism proof. Link functions, thresholds, constraints, and other causes can produce interactions. Do not call the contrast a phase relation or evidence of quantum behavior.

Test representation sensitivity as well. Splitting one description into two serial nodes should not change a claimed support diagnostic when the stipulated action/intervention mapping is unchanged. If a proposed “future depth” score changes merely because an annotator used more words, it is not yet a stable explanatory quantity.

## 11. Blinding, holdouts, and source families

Separate annotation from verdict wherever feasible. Annotators should not know which literary label is preferred or which result the researcher hopes to obtain. Freeze relation types, rival predictions, exclusions, and the analysis plan before the holdout.

Use held-out tasks and episodes, not just rewordings of the examples used to design the model. A future-oriented freely endorsed care task and an other-dependent joyful collaboration are essential adverse cases for the false rule that future or other dependence means servitude. A currently enjoyable but coercive or compulsive episode is an adverse case for present closure as sufficient freedom.

Treat all TLICA papers as a connected theoretical provenance family. Treat the current conversation and assistant revisions as another connected family, not separate confirmers. Treat mirrors and excerpts of the same literary work as dependent. Source-family leave-outs can expose reliance on one reading, but do not themselves supply empirical independence.

No blind independent review, human holdout, or source-family ablation has been completed for this package. These are the next checks to run, not achievements to report.

## 12. Executable logical controls

Run:

```bash
python3 research/geometry_of_actualization_2026-09-07/support_demo.py
```

The script is standard-library-only. It checks five explicitly stipulated support rules with 13 tests, including feasibility, redundant and conjunctive support, an irrelevant-feature null control, unknown-input rejection, binary contrarian dependence, and mutations that remove feasibility or replace AND with OR.

**Observed local result, 2026-09-07:** 13 tests executed; zero failures; zero errors. The exact script bytes had Git blob SHA-1 `d73097445137ae8a05702b4d497757ed75ca6adb` in the local run. The remote blob should be checked against this value after upload.

The passing controls establish only that the small implementation satisfies those expectations. The redundancy and conjunction cases deliberately demonstrate why single-withdrawal tests can mislead. No fitted emotional parameters, human data, neural assumptions, measured phases, or scientific validation are present.

The script prints machine-readable JSON to stdout and test results to stderr, making the run reproducible without retaining full external copyrighted source texts.

## 13. Next verdict-changing work

The strongest next conceptual check is an independent, source-grounded attempt to break the mapping with counterexamples, especially other-dependent joy and freely endorsed future commitment. The strongest next empirical step is a small ethical pilot designed around one clearly specified contrast, with precommitted simple rivals and manipulation checks.

Do not scale up the graph machinery before establishing that even one context-support distinction is assignable and predicts something beyond baseline preference, task feasibility, and known incentive conditions. If it does not, the honest result may be a useful descriptive vocabulary without demonstrated predictive gain.
