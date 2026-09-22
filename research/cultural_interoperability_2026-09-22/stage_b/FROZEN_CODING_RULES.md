# Frozen coding and bridge rules, v0.1

**Status:** a frozen *specification* (Disclosed design), not an implemented validator, not a
dataset, and not evidence. No human data, participants, corpus, or listener outcomes exist.
The empirical mechanism remains **UNVERIFIED**. Date frozen: 2026-09-22.

Both 2026-09-22 dossiers — the [interoperability umbrella](../README.md) and the
[realness-atlas probe](../../cultural_realness_atlas_2026-09-22/README.md) — gate every
held-out evaluation on one precondition: **freeze the coding and bridge rules before any
holdout is opened.** This file is that freeze. Its purpose is to fix, *in advance of seeing
any evaluation item*, what a record means, what a transport is allowed to claim, and what
makes an input fail closed. Changing any rule below requires a new version number and only
new held-out items may be opened against it; previously opened items are burned.

This specification is what the owed Stage-B validator (`records.py`, not yet implemented)
must enforce. Until that validator exists and passes its controls, nothing here has been
executed beyond `make validate`.

## 0. Separations that must never collapse

A record, a transport, or a verdict may speak to at most one of these at a time:

1. **Structural correspondence** — selected relations match under a declared map.
2. **Causal / historical connection** — two lives or episodes are actually linked.
3. **Phenomenological similarity** — participants report related felt organization.
4. **Factual truth** — a world claim holds, on appropriately scoped evidence.
5. **Liking / endorsement** — a participant prefers or accepts something.

None of the five implies any other. A graph match is a fact about *annotations only*.

## 1. Typed records (kept in separate registers)

Every record carries `task_id`, `record_id`, `as_of` (ISO date), and `provenance`
(who/what supplied it). A record whose `task_id` does not equal the bundle's task is
**rejected** (mismatched-task fail-closed, §4).

- **Evidence record** (empirical). `claim`, `polarity` ∈ {asserted, denied, unknown,
  disputed}, `source_ids` (≥1), `world_verification` ∈ {verified, unverified},
  `expires` (ISO date or null). A `disputed` claim retains its alternatives; it is not
  silently resolved. `unverified` world-verification does **not** make the claim false.
- **Interpretation record** (participant reconstruction). `owner`, `layer` ∈
  {participant, narrator, researcher}, `roles`, `predicates`, `stakes`, `alternatives`,
  `unknowns`, `source_span`, `editable` (always true), `owner_confirmed` (bool). Confirmation
  means *"this describes my position sufficiently for this task,"* never that any factual
  claim inside it is verified. Two interpretation records over the same referent that
  disagree are **both retained** (§5); disagreement is never adjudicated away to manufacture
  agreement.
- **Permission record** (consent). `party`, `step` (a *specific* proposed next action),
  `scope`, `voluntary` (bool), `granted_at`, `expires`, `withdrawable` (bool), `value` ∈
  {true, false, null}. Consent is not predicted benefit; a model may judge an option good
  for a party while that party withholds permission. No default consent exists; absence is
  `null`, never `true`.
- **Normative record** (floors and standing). `kind` ∈ {party_floor, standing}, `owner`
  (for a floor), `basis` (the declared normative ground), `source_ids`. A floor or a
  standing/third-party constraint is not derivable from preference aggregation and cannot be
  out-voted.
- **Predicate-definition record** (provenance). `name`, `definition`, `supplied_by`,
  `alternatives` (competing definitions of the same name). **Two coders using the same
  relation name is not evidence they mean the same thing** — this is the first live
  probe-gap; the register exists to make that disagreement inspectable, not to hide it.
- **Source record.** `source_id`, `family`, `status` ∈ {confirmed, unverified, disputed}.
  Shared-family duplicates are not independent corroboration; all cited sources of a
  constraint are jointly required.

## 2. Bridge (transport) rules

- A transport is a declared **injective** node map over exactly the selected source nodes,
  preserving declared node kinds, under a **single declared predicate basis**. Different
  bases must be explicitly reconciled first.
- Only source facts whose endpoints both lie in the mapped domain are eligible. For a
  partial transport, name the subgraph **and the omitted relations** explicitly. **No silent
  pruning to obtain a match.**
- A target observation with equal polarity is a *match*; opposite polarity a
  *contradiction*; no observation is *unknown*. Reversing an edge does **not** logically
  negate the original relation. A forward fact-preserving map need not reflect extra target
  facts, so it is **not** an isomorphism.
- The **empty map is never support**. A bridge with no eligible facts is insufficient
  evidence, not a perfect match.

## 3. Coding process (independence and consent)

- At least **two independently working human annotators** per item; preserve
  pre-adjudication records and provenance. A single AI, or several instances of the same
  model, are **not blind witnesses** and never count as independent coding.
- Annotators may **reject the researcher's framing** and supply their own predicates and
  alternatives. Situated knowledge is permitted and recorded.
- **Consent precedes collection and publication.** Identifying or sensitive material stays
  out of the public repository. Original, permission-cleared stimuli only; no full commercial
  lyrics or audio are redistributed.

## 4. Fail-closed conditions (the priority-1 acceptance gate)

Each of the following makes a record or its dependent gate resolve to **rejected** or
**unknown** — **never silently true, and never silently impossible**:

- **Malformed** — missing a required field, wrong type, duplicate id, or an extra
  unrecognized key ⇒ reject the bundle.
- **Stale** — `expires` earlier than the task's `as_of` (or a supplied evaluation date) ⇒
  the record is **expired**; any gate that required it becomes **unknown**.
- **Mismatched-task** — a record whose `task_id` differs from the bundle ⇒ reject.
- **Missing consent** — no permission record for a party/step, or `value` = null ⇒ the
  consent gate is **unknown** (pending), and `false` ⇒ **rejected**; neither is ever `true`.
- **Missing required coverage** — no reality gate, no standing gate, or a party without a
  floor ⇒ reject.
- **Unverified/disputed source** on a required constraint ⇒ that gate is **unknown**.

Symmetrically, an **unknown** is never upgraded to impossibility: a catalog with only
true/unknown gates is `UNRESOLVED` (a probe or access gap), not `NO_PERMISSIBLE_OPTION`.

## 5. Disagreement, uncertainty, and the freeze discipline

- Retain contradictory interpretation records and disputed evidence as **alternatives**, not
  noise to be averaged out. Missing observations remain unknown.
- **Freeze before holdout:** this file, the predicate basis, the node-kind rules, the
  map-selection procedure, and the evaluation rubric are fixed before any held-out item is
  opened. Split data by artifact / artist / story-family / participant / setting — never by
  adjacent excerpts of the same work — and never let a fitted item leak into a holdout.
- Report the **unadjusted** record set alongside any adjustment. Run leave-one-source-family-out
  where the design makes it meaningful; a result that vanishes when one family is removed was
  carried by that family.

## 6. What this does not license

No person-level κ / φ / σ / ρ / μ value is computed. A confirmed gate is a stipulated
availability inside a synthetic exercise, not a truth label. Identity coupling is not factual
evidence. Passing software controls corroborates instrument consistency, **not** any human
mechanism. Do not present synthetic calibration as listener evidence, a corpus result, or a
cultural sheaf.

## 7. Owed next (executable, then human)

1. **Implement `records.py`** against this spec: the typed registers, three-valued
   resolution, and the §4 fail-closed controls, with a `test_records.py` that demonstrates
   each control failing closed and disagreement round-tripping without coercion. Synthetic
   calibration only.
2. **Author original micro-vignettes** as *stimulus engineering* (clearly not a
   representative corpus), across work / family / shared space / ritual / music, including
   cases expected **not** to correspond.
3. **Independent human coding pilot** — owed, and gated on ethics review, consent, and real
   independent coders. Not startable from inside this repository.

**Research-tier; foundation v5.5.1 unchanged.**
