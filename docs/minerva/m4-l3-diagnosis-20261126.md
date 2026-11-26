# Grading epistemic-status faithfulness: orthogonal axes and a discriminating instrument

**Order:** GOD ORDER #1 / T1, 2026-11-26. **Tier:** TLICA theoretical liaison. These are docs only: no product code and no
inference run.

**Scope:** the public, abstract half of a diagnosis of a failed grader calibration in Minerva milestone M4-c. The grader
was a model that extracts claims, followed by a deterministic check. The item-level diagnosis (evidence, item traces,
rule-level conditionals) lives in the owning private repository and is not reproduced here.

> **Contamination firewall.** This document discusses failure mechanisms and instrument design. **A future blind
> test-set author should not read it.** No test items were authored here.

**Ledger labels:** Demonstrated · Observed · Conjectured · Refuted · UNVERIFIED. Nothing here scores truth or makes any
claim about a model under test.

---

## 1. The problem class

A grader of this shape checks whether a reply **represents the epistemic standing of what it was given faithfully**. It
asks whether the reply:
- keeps an unverified thing unverified;
- keeps a rehearsal a rehearsal;
- credits the right person;
- invents nothing;
- keeps the hedges it was handed.

The design has two stages. A model **extracts** claim rows from the reply. A **deterministic comparator** then checks
each row against the delivered facts. Each test item carries **one planted class**.

## 2. Rival explanations for a calibration failure, and their discriminators

| Rival | Claim | Discriminating evidence |
|---|---|---|
| **R-ext: extractor ontology** | The model misreads hedges, actors or support. The rules are fine. | **Oracle-row test:** feed human-gold rows to the unchanged comparator. If the wrong verdicts vanish, the extractor is the cause. Also measure *field-level* row accuracy against gold, not verdict accuracy. |
| **R-cmp: comparator rule** | The rules mis-map correct rows. | Same oracle-row test. If gold rows still fail, the cause is the comparator *or* the shared schema. Split those two by giving the comparator gold rows in an *extended* schema (§3). If those pass, the schema is the cause. |
| **R-set: set construction** | Items encode the same situation inconsistently, or a planted label does not match what the item tests. | An **encoding-consistency audit** by a second context against one written convention. Then check whether the wrong verdicts concentrate on the inconsistently encoded items. |
| **R-amb: genuine label ambiguity** | The right class is not determinate for some items. | **Blind human inter-rater agreement** on class *and* fields. If humans split on the same items, the ceiling for any extractor is human agreement, not a fixed bar. |

**Main theoretical finding (Conjectured as applied to the observed run; the mechanism-level claims are argued below).**
A large share of wrong verdicts can arise under *faithful* extraction. The cause is the **shared fact/row schema** that the
extractor, the comparator and the set author all use, rather than any one component. Three abstract mechanisms:

- **M1. One attribution slot, several roles.** A fact records one actor: the *utterer of the record*. A reply can correctly
  name a *different* party, such as the reported speaker inside the content or the in-frame role in a rehearsal. A single
  slot cannot express "correctly named embedded speaker", so the reply reads as a swap.
- **M2. Availability read as absence of content.** When the schema treats an unavailable, absent or stale observation as
  "supports nothing", a *true claim about the unavailability itself* has no support. It is then at risk of being graded
  as invented.
- **M3. Weakened support versus no support.** If source hedges are delivered only in untyped text, a rule keyed to a typed
  "open" status cannot fire. A reply that drops the hedge then has no fact that supports the *strengthened* claim, so it
  is graded **invented** rather than **uncertainty dropped**. Arguably both descriptions are right: dropping a hedge
  *invents the excess*.

A fourth, weaker mechanism is **M4: single-support cardinality.** A claim that fuses two delivered facts cannot cite both.
A row that is not pinned to one fact can then be graded as unsupported.

## 3. Does the taxonomy conflate distinctions? Yes: at least six orthogonal axes

One planted class per item, and one asserted-status value per row, projects a product space onto a single label:

| Axis | Values | Typical collapse |
|---|---|---|
| **A1 availability** | present / absent / withheld / unavailable / stale | merged with *support* (M2); stale is really A5 |
| **A2 verification standing** | verified / unchecked / open | "open" doubles as decision finality (settled vs open) |
| **A3 reality frame (modality)** | actual / rehearsed / role-played / imagined / generated | shares one status enum with A2; one planted class is caught via A2 *or* A3 |
| **A4 attribution** | utterer / embedded (reported) speaker / in-frame role | one actor slot (M1) |
| **A5 temporal currency** | current / dated / stale | folded into A1 |
| **A6 support strength** | full / weakened (hedged) / none; cardinality 1..n | "invented" and "uncertainty dropped" are separate classes for one axis and its limiting case (M3); cardinality fixed at 1 (M4) |

**Consequence (Observed on the run examined; stated here abstractly):** a *clean* class such as "hedged reply" is a union
across A1/A5, A2, A3 and A4, not a single class. Unions like this are the natural source of false positives, because every
axis contributes its own boundary errors.

On the specific question asked:
- Present/Absent/Withheld/Unavailable/Stale (A1 + A5), verified/rehearsed/unchecked (A2 × A3) and actor provenance (A4) are
  **orthogonal**.
- Grading them as one class makes errors on one axis indistinguishable from errors on another.

## 4. Proposal only: the cheapest discriminating instrument

1. **The zero-model bearing first.** Have a context that is not the checker's author write human-gold rows for an
   already-spent set, then run the unchanged comparator over them.
   - This separates extraction error from comparison and schema error at stdlib cost.
   - It is dev evidence only and never acceptance evidence.
2. **Per-axis grading.** Extend the row with one field per axis:
   - a multi-reference `support[]` list;
   - `support_strength`;
   - `utterer`, `embedded_speaker` and `frame_role`;
   - `frame`;
   - `standing`;
   - `availability_claim`.

   Decide one rule per axis and accept per axis, each with a Wilson CI. "Right reason" then becomes per axis instead of
   coming from a many-to-one class map.
3. **What a fresh blind set must contain.** This is a requirement on the *format specification*, not items:
   - **Minimal pairs, factorial over the axes.** Each pair shares its facts and differs on exactly one axis: hedge kept
     versus dropped; embedded speaker named correctly versus swapped; unavailability reported versus papered over;
     rehearsal kept versus promoted.
   - **Interaction cells**, for example stale × rehearsal, or a reported speaker inside a rehearsal. These test whether
     the axes are actually independent. A cross-term means non-additivity; it is not a mechanism claim.
   - **Typed/untyped hedge twins.** The same hedge appears as a typed status in one item and only in prose in its twin.
     This separates hedge *reading* from hedge *plumbing*.
   - **One written encoding convention** for reported speech, rehearsal roles and hedge location, audited by a second
     context before sealing.
   - **At least two blind human labellers per item**, with at least one outside the extractor's model family. Measure
     per-axis agreement *before* any model is graded.
   - **Sizing:** about 30 fabricated items per gated axis, each with a matched clean twin. A 0.90 point estimate with a
     Wilson lower bound ≥ 0.75 needs about 28 of 30.
4. **Read-out:**

   | Result pattern | Points to |
   |---|---|
   | Failures persist with gold rows in the old schema but vanish in the extended one | schema |
   | Failures persist under both | comparator logic |
   | Failures vanish with gold rows | extractor |
   | Human agreement on an axis below the bar | label ambiguity (set that axis's bar relative to the human ceiling) |

5. **Prompt variants are not test–retest.** Extractors whose prompts differ in content (for example, worked examples
   versus none) measure *prompt-variant agreement*. Stability has to be measured by re-running the *same* prompt.

## 5. Can any model extractor reach 0.90 on hedge semantics?

- **UNVERIFIED.** It has not been measured. Where hedge recall was zero, the delivered items carried no typed hedge, so
  the zeros are plumbing, not evidence about extraction in either direction.
- **Conjectured: plausible** for the binary question "kept versus dropped" when the source hedge is delivered as a typed
  field. The task reduces to status matching, which comparable classes handle at high per-class recall.
- **Conjectured: unlikely** for **graded hedge strength read from untyped prose**, and 0.90 may exceed the *human* ceiling.
  No literature agreement figure was checked (no search was run), so any number here is UNVERIFIED.
- **Recommendation:** gate hedge semantics against measured human–human agreement, not a fixed constant.
- **Standing caveat:** an extractor from the same family as the item author is not an independent witness. Information
  firewalls reduce leakage but do not remove common provenance.

## 6. Boundaries

- This is a design proposal for a *future* grader. It does not reopen a closed verdict and it makes no claim about any
  model under test.
- No test items were authored here.
- The item-level evidence is private and routed to its owning repository.
