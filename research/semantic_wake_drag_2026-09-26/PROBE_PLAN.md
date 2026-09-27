# Probe plan — Semantic Wake Drag

**Date:** 2026-09-26  
**Status:** preregistration-style research plan; **UNRUN / UNVERIFIED**.  
**Purpose:** distinguish semantic wake drag from ordinary disagreement, observer slowness, actor error, and generic coordination cost.

---

## 0. Load-bearing question

The dossier is scientifically interesting only if the following stronger claim survives:

> Holding the underlying objective and action quality approximately fixed, changes in **action-update frequency**, **observer-accessible invariant structure**, and **representation resolution** cause predictable changes in reconstruction fidelity and downstream coordination friction.

The target is not to prove that people misunderstand fast actors. The target is to isolate *why*.

---

## 1. Rival models

### R1 — observer lag

The observer has enough information but needs more time to integrate it.

Prediction:

- added interpretation time improves reconstruction;
- extra semantic headers add little once time is controlled.

### R2 — semantic under-specification

The observer lacks the load-bearing invariants needed to interpret the action sequence.

Prediction:

- a compact invariant/header intervention improves reconstruction even at matched time;
- post-hoc time alone is insufficient.

### R3 — resolution mismatch

The actor distinguishes task states that the observer's representation collapses.

Prediction:

- exposing the discriminating state variables improves consistency judgments;
- generic explanation without those variables does not.

### R4 — substantive disagreement

The observer reconstructs the actor accurately and still rejects or resists the action.

Prediction:

- reconstruction fidelity rises while disagreement/friction remains.

### R5 — actor-model failure

The actor's action is poorly calibrated to the shared environment.

Prediction:

- observers can reconstruct the model and still correctly identify omitted constraints or bad predictions;
- interface improvement does not rescue objective performance.

### R6 — generic change cost

Any rapid sequence is costly regardless of semantic legibility.

Prediction:

- headers improve understanding but do not materially reduce correction burden, interruption, or rework.

A useful experiment must allow these rivals to separate.

---

## 2. Primary synthetic probe: 2 × 2 × 2 design

Construct a small collaborative task in which one controller receives fine-grained state information and an observer/coordinator receives a controlled view.

Manipulate three axes:

1. **action frequency**
   - low: one externally meaningful intervention per observer update window;
   - high: several interventions per observer update window.

2. **semantic header**
   - absent;
   - present: compact \(H=(G,I,R,\Delta,B)\).

3. **state resolution**
   - matched: observer sees the discriminating state variables;
   - coarsened: several actor-distinct states are presented as one apparent class.

This yields all eight cells.

### Hold fixed

As far as practical:

- the underlying objective;
- the action policy;
- task difficulty;
- number of total actions;
- observer role;
- allowed response time within each frequency condition;
- final objective outcome.

The purpose is to change the **interface**, not to make one condition intrinsically easier.

---

## 3. Measurements

### M1 — reconstruction fidelity

Before outcome disclosure, ask the observer to state:

- the actor's current goal;
- which constraints/invariants remained fixed;
- why the last intervention occurred;
- what change is likely next;
- what conclusion should *not* be drawn from the change.

Score against a preregistered key.

### M2 — perceived consistency

Ask whether the actor appears to be:

- following one coherent plan;
- changing objectives;
- acting arbitrarily;
- contradicting prior actions.

The important quantity is not liking; it is whether the same generating policy is reconstructed as one trajectory.

### M3 — surprise / interruption burden

Count:

- clarification requests;
- pauses;
- explicit why-did-you-do-that events;
- reversals;
- coordination interrupts.

### M4 — downstream correction

Count:

- added approval gates;
- compensatory constraints;
- duplicated work;
- rollback demands;
- procedural repairs.

In a synthetic task these can be modeled as explicit coordinator actions rather than inferred psychologically.

### M5 — substantive agreement

After measuring reconstruction, separately ask whether the observer agrees with the action.

This keeps

\[
\text{understood} \neq \text{accepted}.
\]

### M6 — task performance

Measure objective task quality independently of the observer's interpretation.

This keeps

\[
\text{legible} \neq \text{correct}.
\]

---

## 4. Primary contrasts

### P1 — semantic-header contrast

At matched frequency and resolution:

\[
\Delta_H
=
\mathrm{Recon}(H=1)-\mathrm{Recon}(H=0).
\]

**Support for R2:** positive reconstruction effect, especially in the high-frequency regime.

**Failure:** no meaningful effect under a calibrated manipulation check.

### P2 — frequency × header interaction

Candidate prediction:

> headers matter more when action frequency is high because they let several micro-actions compress into one legible macro-action.

Do **not** claim the interaction unless all four action-frequency × header cells are present.

### P3 — resolution contrast

At matched frequency/header:

\[
\Delta_q
=
\mathrm{Recon}(\text{matched})
-
\mathrm{Recon}(\text{coarsened}).
\]

Support for R3 requires improvement specifically when the discriminating state variables are revealed.

### P4 — reconstruction / disagreement dissociation

A decisive R4 pattern is:

\[
\mathrm{reconstruction}\uparrow
\quad\text{while}\quad
\mathrm{agreement}\not\uparrow.
\]

This demonstrates that better semantic interoperability does not dissolve real conflict.

### P5 — reconstruction / performance dissociation

A decisive actor-error pattern is:

\[
\mathrm{reconstruction}\uparrow,
\qquad
\mathrm{task\ performance}\downarrow.
\]

That result would directly block the flattering reading: if only they understood, the move would be vindicated.

---

## 5. Positive, negative, null, and mutation controls

### Positive control

Provide a full concise rationale containing exactly the discriminating state variable.

Expected: reconstruction should improve.

### Negative control

Provide a confident but irrelevant explanation of equal length.

Expected: no comparable improvement.

### Null control

No explanation beyond raw actions.

### Mutation control

Keep the header format but flip one load-bearing invariant or predicted next action.

Expected:

- a faithful observer should become **worse**, not better;
- if any structured header helps equally, the proposed invariant-transport mechanism is not supported.

### Time-only control

Provide extra integration time without extra information.

Separates R1 from R2.

---

## 6. Retrospective author-event probe

A lower-cost first probe can use real prior events, but it must avoid self-sealing reconstruction.

### Sampling rule

Before analyzing causes, select a bounded set of interaction episodes with:

- multiple externally meaningful actions in a short period;
- a trace of what the author knew when acting;
- a trace of what was communicated;
- evidence of the other party's interpretation or response.

Do not select only famous failures.

Include:

- smooth interactions;
- misunderstood interactions;
- cases where the other person was ultimately right;
- cases with explicit pre-action explanation.

### Blind reconstruction

Have an independent reader see:

1. external action trace only;
2. action trace + communication available at the time;
3. action trace + hidden internal rationale;
4. full record including later outcome.

Ask the reader to reconstruct goal/invariants at each stage.

The predicted signature is not that stage 4 makes Leah look good. It is:

> adding the *right* hidden structural variables should selectively reduce apparent discontinuity.

If it instead reveals that the original model omitted obvious shared constraints, that is evidence for R5.

---

## 7. Institutional persistence probe

To test the wake-fossilization claim, use a toy organization or historical workflow trace.

At \(t_0\), introduce an ambiguous unusual action.

Allow the organization to encode a response through one of:

- note;
- approval gate;
- role permission;
- checklist;
- escalation rule.

At \(t_1\), correct the interpretation without directly removing the artifact.

Question:

> Does the earlier interpretation continue affecting behavior because it now has independent implementation support?

Compare with a condition where the interpretation was corrected **before** the artifact was created.

This tests the stronger prediction:

\[
\text{same semantic correction}
+
\text{different timing}
\Rightarrow
\text{different residual constraint}.
\]

---

## 8. Pass / fail / ambiguous criteria

### Pass for the semantic-under-translation component

A calibrated semantic header or discriminating state variable:

- improves reconstruction;
- reduces false objective-changed / arbitrary judgments;
- does so more than irrelevant equal-length explanation;
- without requiring increased agreement.

### Pass for the wake-persistence component

Misinterpretation-generated artifacts continue to alter later responses after the interpretation itself is corrected, and earlier correction prevents or reduces the effect.

### Fail

The construct is weakened or refuted in a tested regime if:

- observers already reconstruct goal/invariants accurately without the proposed interface;
- headers do not improve reconstruction beyond irrelevant explanation;
- action frequency has no effect after ordinary workload is controlled;
- resolution exposure does not change consistency judgments;
- downstream friction tracks substantive disagreement or bad performance rather than reconstruction fidelity;
- wake disappears once generic coordination costs are modeled.

### Ambiguous

- the manipulation changes task difficulty;
- the header leaks the correct answer rather than only invariants;
- the observer is overloaded generally;
- action quality differs across frequency cells;
- the evaluator knows the preferred theory;
- the same event is used both to fit and validate the account.

---

## 9. No-Cherenkov-overclaim firewall

The physical analogy predicts **nothing by itself**.

No result may be described as confirming semantic Cherenkov radiation unless the underlying communication/coordination contrasts have already been demonstrated in non-metaphorical variables.

Allowed:

> The high-frequency / low-interface condition produced the predicted reconstruction failure; the Cherenkov label remains a mnemonic.

Not allowed:

> The social phase velocity was exceeded.

There is no measured social phase velocity in this dossier.

---

## 10. Next verdict-changing probe

The weakest useful first experiment is the full **frequency × semantic-header** four-cell design with:

- preregistered reconstruction questions;
- irrelevant-header mutation control;
- separate agreement and task-performance measures.

If the semantic header does not improve reconstruction specifically when the action stream would otherwise be under-translated, the central intervention claim loses much of its value.
