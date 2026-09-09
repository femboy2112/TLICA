# Traversability: formal boundaries and discriminating probes

**Version:** 0.1.0 — 2026-09-08. Companion to [agency](AGENCY_AND_STEERABLE_COMMITMENT.md), [recovery](SLACK_RESONANCE_AND_PLURAL_LIFE.md), and [education](LIBERAL_EDUCATION_AND_FRAME_INTEROPERABILITY.md). See the [ledger](TRAVERSABILITY_SOURCES_AND_LEDGER.md) for provenance and statuses.

No fitted dynamics, clinical scale, human experiment, or independent validation is reported. The small proofs below concern stipulated finite systems only. Proposed studies are not completed preregistrations: sample sizes, operational thresholds, stopping rules, ethical review where required, and analysis details remain to be specified before data collection.

## 1. Object, aim, and acceptance conditions

The object is a bounded episode of participation, persistence, review, or transition. The aim is to distinguish observation, action access, implementation, and effects. The target is not a global rating of a person or a requirement to change frames whenever a prompt appears.

Before an episode is classified, state the activity, endorsed commitments, relevant effects on others, information sources, available actions, time horizon, and requirements that a transition should preserve. Preserve a record of changes to those requirements. Do not redefine the dish after seeing the outcome so that every course becomes successful.

A useful transition satisfies declared requirements at an acceptable cost. A useful review may conclude that no transition is warranted. A failed intervention may reflect access, timing, credibility, or implementation rather than failure of the underlying interpretation. Unknown must remain distinct from zero.

## 2. A schematic dynamics, not a Newtonian law

One possible representation is

\[
x_{t+1}=f_\theta(x_t,c_t,u_t,h_t)+\varepsilon_t,
\qquad y_t=g(x_t,c_t)+\nu_t.
\]

Here \(x_t\) is a hypothesized state, \(c_t\) context, \(u_t\) an available intervention, \(h_t\) relevant history, and \(y_t\) the observed record. Noise terms acknowledge incomplete description, not a known probability distribution. Including history avoids silently claiming that the selected observations form a sufficient Markov state.

No \(\theta\), state variables, noise law, or causal function has been estimated. Describing an episode with this notation does not establish its mechanism. A workable application would need prospectively specified observables and intervention predictions, followed by comparison with simpler accounts using time, task difficulty, opportunity, or ordinary practice.

A desired result is not itself \(u_t\). The intervention must name an executable action or a change to the environment. Nor does an accurate \(y_t\) guarantee any useful control. This is the reason for distinguishing an observer from practical leverage; the engineering source supplies an analogy, not a human model. [T-C1]

## 3. Reachability relative to constraints

For a fully declared transition model, let \(\mathcal U(x,c)\) be the admissible inputs and \(K\) the constraints. Define

\[
\operatorname{Reach}_H(x;\mathcal U,K)
=\{z:\text{an admissible path from }x\text{ reaches }z\text{ within horizon }H\}.
\]

This is ordinary finite-model bookkeeping when the graph and constraints are supplied. In a human application, the relevant set is only partially known. An absent observed route can be a pathway gap, probe gap, or access gap; it must not be called an absolute impossibility without further evidence.

A named alternative does not necessarily belong to this set. A reachable alternative does not necessarily satisfy the person's or others' requirements. Widening the set is therefore not equivalent to improving life, and global strong connectivity is not the desired criterion.

A transition record should retain a cost tuple rather than an undeclared sum:

\[
C_{ij}=(\text{latency},\text{reported effort},\text{sleep displacement},
\text{semantic loss},\text{other effects}).
\]

The components need operational definitions. No claim is made that they have common units, that all are measured precisely, or that a scalar weighted combination is prohibited when its decision rule is explicitly justified. The present project does not supply such weights.

## 4. Finite disclosure A: observation is insufficient for control

**Stipulation:** states are \(\{a,b\}\), the initial state is \(a\), the target is \(b\), and the sole action is `stay`, with \(f(a,\mathrm{stay})=a\). The observer reports the true state perfectly.

**Claim:** No policy using the available action reaches \(b\) from \(a\) in any finite number of steps.

**Proof:** At step zero the state is \(a\). If the state is \(a\) at step \(n\), the only admissible action returns \(a\). Induction gives \(a\) at every finite step. Perfect information does not alter the transition rule.

**Mutation:** Add action `leave` with \(f(a,\mathrm{leave})=b\). The target becomes reachable in one step. The observer is unchanged.

This refutes, within the stipulated model, the universal inference that sufficient self-description alone entails practical control. It does not establish that any particular person has a singleton action set. That requires investigation.

## 5. Finite disclosure B: cheaper passage can destroy fidelity

**Stipulation:** a record is \((q,s)\), where \(q\) is a claim and \(s\) its status, either `open` or `verified`. A source record has status `open`. The declared transport invariant is preservation of that status.

A fast map \(T_f(q,s)=(q,\mathrm{verified})\) costs one unit of arbitrary toy time. A slower map \(T_p(q,s)=(q,s)\) costs two.

**Claim:** Minimizing time without the invariant selects an invalid transport for the open record.

**Proof:** One is less than two, but \(T_f(q,\mathrm{open})\) has a different status from its source. \(T_p\) preserves it. Thus speed and fidelity are separable in this model.

**Mutation and null:** If the source is already verified, both maps preserve status for that case. If both maps preserve status, the cheaper one need not be worse. The point is not that cheap transitions are bad; it is that cost alone cannot certify them.

## 6. Finite disclosure C: more labels need not create a route

Start with a graph on \(\{a,b\}\) containing only \(a\to a\). Add a node \(c\) without adding an edge from the reachable component of \(a\). Reachability from \(a\) is unchanged. This follows directly because no path from \(a\) contains the new isolated node.

Adding an edge \(a\to c\) changes that result. The example distinguishes repertoire size from usable access. It does not prove that teaching new concepts never creates implicit routes; whether it does is an empirical question.

## 7. Probe A: information versus executable control

**Question:** Does a frame check help because it discloses information, because it supplies an executable response, or both?

**Design candidate:** In a harmless task with a known rule change, compare an informative review prompt with a time-matched prompt, crossed with availability versus nonavailability of a benign alternative action. All four cells must be present before making an interaction claim. Do not deprive participants of real-life needs or safety.

**Outcomes:** Rule-change detection, stated interpretation, action feasibility, execution, task quality, unnecessary changes, and burden. Keep detection time separate from execution time.

**Separating prediction:** If the bottleneck is implementation, making the alternative available changes behavior among participants who already detected the mismatch without requiring further persuasion. If review alone accounts for the benefit, the access manipulation adds little under the specified task. Both effects can coexist.

**Controls:** An obvious error; an irrelevant discrepancy that should not prompt change; a case where continuing is correct; and an explicit instruction check. A mutation can disclose the alternative from the beginning. Ambiguity includes failure to understand the rule or a manipulation that changes task difficulty rather than access alone.

## 8. Probe B: resonant recovery versus elapsed time or absorption

**Question:** Does personally meaningful engagement change prior-frame salience beyond generic absorption or the passage of time?

Begin with voluntary low-burden observations in naturally occurring, low-stakes episodes. Record starting conditions and actual activity rather than imposing emotionally intense material. Observe nominated meaningful activity, comparably absorbing activity not nominated as meaningful, and ordinary chosen rest where these are available without burden. Do not assume the categories are cleanly separable.

**Outcomes:** Prior-frame salience, engagement, ownership, reported effort, transition time, next action availability, and later sleep displacement. Fix observation windows before interpreting changes. Feeling more oneself is a report, not an independently measured identity state.

**Rivals:** Time alone; distraction; interruption of rehearsal; ordinary enjoyment; expectancy; physical comfort; selection of easier evenings; different starting arousal. A between-activity difference that disappears after matching time and initial state does not support a special resonance mechanism.

**Defeater:** A simpler time or absorption account predicts held-out episodes as well as the proposed account. **Ambiguous:** Meaning and absorption cannot be separated, measures interrupt the activity, or carryover dominates. Do not manufacture heat, sleep loss, conflict, or deprivation as experimental factors.

## 9. Probe C: cheap handoff versus avoidance or excessive audit

**Question:** Does a bounded transition record improve warranted re-entry without erasing unresolved information?

In low-stakes creative or reasoning tasks, compare a short handoff—question, evidence/status, stopping point, next step—with an equally long free-form note and an ordinary stopping condition. Preserve the ability to choose rest. The handoff is not required to produce a new frame every time.

**Outcomes:** Later reconstruction fidelity, time to resume, appropriate dwell, unnecessary switches, unresolved issues falsely reported as resolved, completion, and interruption cost.

**Controls:** A real unresolved requirement; a resolved issue that should not be reopened; an irrelevant cue; a case requiring deeper review; and a deliberately corrupted note in a synthetic or explicitly consented task. A prompt that merely supplies missing facts is an information intervention, not proof of improved transition skill.

**Defeater:** An ordinary note or no note works equally well on fresh tasks; the routine increases compulsive checking or loses decisive evidence. The proposal must permit those outcomes.

## 10. Probe D: education as faithful transport

**Question:** Does explicit cross-method practice improve transfer beyond vocabulary exposure, additional instruction, or general fluency?

Use time-matched teaching conditions and held-out problems. Establish competence within the source and target methods first. Grade the preservation of declared relations, assumptions, provenance, uncertainty, and known losses. Include an attractive analogy that should be rejected and a case where retaining the source method is better than switching.

**Outcomes:** Source understanding, target understanding, reconstruction fidelity, warranted non-transfer, practical use, completion, effort, and agreement. Agreement is not a substitute for understanding. A degree or self-description as a generalist is not an outcome measure.

**Defeaters:** Gains are limited to taught examples; equally structured single-domain comparison performs as well; grading rewards preferred conclusions; or transport language increases confidence without external accuracy.

A stronger test uses independent raters blinded to the theoretical framing. Same-assistant scoring is not independent corroboration. A study involving other people requires explicit consent and appropriate review; coworkers and customers must not become covert experimental subjects.

## 11. Outcome rules and factorial boundaries

For each probe, define **pass** as the registered separating result with functioning controls; **fail** as a credible, sufficiently sensitive result against that prediction; and **ambiguous** as unresolved manipulation, access, provenance, or measurement problems. A small noisy difference is not automatically confirmation or refutation.

For a declared scalar outcome in a complete two-factor design,

\[
\Delta=y_{11}-y_{10}-y_{01}+y_{00}
\]

is a signed contrast only after coding, measurement scale, and all four cells are supplied. It is not a mechanism proof. A before/after anecdote is not a factorial contrast; missing values are not zeros. Preserve raw and adjusted views, and do not fit and validate on the same episodes.

## 12. TLICA mapping and the next verdict-changing probe

Retain κ/contact, φ/toolkit-relative truth-indistinguishability and pathway state, σ/source-map adequacy, ρ/identity integration or commitment coupling, μ/probe availability, toolkit closure, independence, coherence, and discrimination separately. This extension assigns none of them a numerical value.

A source-map defect can survive high felt coherence. A well-supported interpretation can coexist with an unavailable action. Strong identity integration can support revision rather than oppose it. An unmeasured probe is not absent, an unavailable route is not disproven, and a smooth semantic transport does not certify its source.

The weakest useful next probe is one bounded, safe comparison that separates an observation improvement from an implementation improvement. A second priority is testing whether meaningful engagement changes recovery outcomes beyond time and generic absorption. The model is not contextually saturated: known measurement, intervention, source, and rival-model work remains. The relevant human claims are neither φ-resolved nor σ-resolved by this document.
