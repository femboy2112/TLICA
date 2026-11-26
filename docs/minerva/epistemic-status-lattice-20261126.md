# An epistemic-status lattice for agent observation contracts

**Order:** GOD ORDER / T2, 2026-11-26. **Tier:** TLICA theoretical liaison (docs only).
**Scope:** the public, abstract half of T2. The mapping of this lattice onto a specific host/model contract, together with
the contract-level collapse findings, is routed privately to the owning repositories.

**Ledger labels:** Demonstrated · Observed · Conjectured · Refuted · UNVERIFIED. The statements below are definitions and
consequences of definitions, Demonstrated by construction unless labelled otherwise. Nothing here describes any
implemented system.

---

## 1. Why a lattice, not an enum

An agent host hands a model **observations**. The model *proposes* claims, and the host decides what is citable,
committable and true. Every observation carries an epistemic standing. The recurring design error is to give that
standing **one enum**. "Verified", "rehearsed", "unavailable", "reported" and "ambiguous" are values on *different axes*.
One enum can hold only one of them at a time, so legitimate combinations become unrepresentable (an unverified claim made
inside a fiction, for example). It also lets the axes trade against each other silently: a rehearsal gets promoted to a
verification.

## 2. The axes

| Axis | Values | Order |
|---|---|---|
| **V availability** | present · absent (looked, nothing there) · unavailable (could not look) · withheld{consent / eligibility / budget} · stale{fence} | none between the non-present values. Only *present* carries content. |
| **W warrant** | unverified ⊑ {reported, inferred} ⊑ established | partial order. Reported (testimony) and inferred (derivation) are incomparable. Established needs a host witness. |
| **M frame / modality** | actual · fictional · hypothetical · rehearsal · out-of-character | an antichain. No operation moves between frames. |
| **D determinacy** | resolved · ambiguous | resolved ⊒ ambiguous |
| **A attribution** | a two-place pair: relayer (who delivered the record) and attributed speaker (whose content it is) | none; it is identity, not order |
| **P content provenance** | explicit · inferred · default · unresolved | none |
| **Q decision authority** | operator · delegated · preset · legacy · none | none. This is *who chose*, which is distinct from P, *where the content came from*. |
| **F currency** | a fence (version, generation) | equality only |

**Typing rule.** W, M, D, A and P are fields of a **present** observation only. A non-present observation is the pair
(part, V). It carries no warrant, because there is no content to warrant.

## 3. Operations

- **Conjunction** (a claim resting on several observations):
  - every cited observation must be present;
  - W = meet (the weakest);
  - D = meet;
  - M is *absorbing*: if any input is non-actual, the conjunction is non-actual.
- **Derivation:** W(derived) ⊑ inferred, even from established premises. Inference does not transmit witness.
- **Witness:** only a host witness event raises W to established. No model proposal does.
- **Re-projection at the live fence:** stale becomes present again, or another V value; the operation is idempotent.
- **Budget re-projection:** withheld{budget} can become present; withheld{consent} cannot.

## 4. Invariants (testable)

| # | Invariant | Property-test shape |
|---|---|---|
| I1 | **Warrant monotonicity.** Model proposals never raise W to established. | random proposal sequences with no witness events give established count = 0 |
| I2 | **Frame non-crossing.** A non-actual source never yields an established actual claim, and never backs a commit. | exhaustive over M × W |
| I3 | **Carrier coherence.** If two fields both encode M (or A), they never disagree. | exhaustive over the product of the two carriers |
| I4 | **No content without presence.** V ≠ present ⇒ empty payload, no W, not citable *as content*. | fill attempts are emptied, and a citation of content is refused |
| I5 | **Availability is citable as availability.** A claim *about* V ("I can't see X") may cite (part, V). A claim of content may not. | paired positive/negative fixture |
| I6 | **Typed withhold reason.** Budget never reports as consent, and the other way round. | the budget-vs-consent re-projection test in §3 |
| I7 | **Stale idempotence.** A stale part reports its fence and never content; re-projecting at the live fence is idempotent. | double re-projection gives the same output |
| I8 | **Confirmation survives mapping.** Any map from authoring history into P keeps the operator-confirmed bit. | round trip |
| I9 | **Authority ≠ provenance.** "Delegated decision + inferred content" is representable and is never displayed as explicit. | construction plus display check |
| I10 | **Origin is host-assigned.** Model text that claims operator voice remains model-origin. | paired control: the same text in a real operator turn |
| I11 | **Two-place attribution.** A reported/quoted observation carries both relayer and attributed speaker. Changing the speaker changes attribution; changing only the relayer does not. | swap test |
| I12 | **Determinacy gate.** Ambiguous ⇒ not established. | exhaustive over D × W |
| I13 | **Inference does not transmit witness.** | a derived claim from established premises has W ⊑ inferred |

## 5. Collapse diagnostics (how to check any contract)

For each distinction above, ask three questions:
1. Is there a field that carries it?
2. Does any field carry *two* axes, for example a status enum that also contains a frame value?
3. Does any axis live in *two* fields (a double carrier, which needs I3)?

A distinction **collapses** when two of its values map to the same representation and some decision downstream depends on
the difference. The common collapses are:
- frame folded into status;
- budget folded into consent;
- decision authority folded into provenance;
- a one-place actor slot for two-place reported speech;
- availability made uncitable as a fact in its own right.

The last two are the same mechanisms that defeated a model-extracted grader in T1 (see
[the T1 note](m4-l3-diagnosis-20261126.md) M1 and M2). The contract and the grader inherit one schema, so they inherit the
same blind spots.

## 6. Boundaries

- This is a formal proposal. Status words describe the definitions, not any running system.
- The mapping onto named host types is private and routed to its owners.
