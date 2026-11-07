# Affective Yoneda — claim ledger, rivals, and discriminating probes

**Date:** 2026-11-07  
**Status:** design-only for human experiments; no participants recruited, no dataset collected, no experiment executed. See [formalism](FORMALISM.md) and [origin](README.md).

## Claim ledger

| ID | Claim | Status | What would change the verdict |
|---|---|---|---|
| AY-001 | The 2026-11-07 author seed proposes partner-specific, context-sensitive emotional meaning and calls it "emotional Yoneda." | **Observed as author text** | None needed for provenance; it is not an observation about a sampled human population. |
| AY-002 | A locally small category embeds fully faithfully into its presheaf category under full Yoneda. | **Disclosed** (standard theorem) | Only a mathematical error or violation of assumptions. |
| AY-003 | A restricted Yoneda nerve is full and faithful precisely for a dense probe functor. | **Disclosed** under the standard definition of density | Check probe functor, size and category hypotheses before use. |
| AY-004 | In finite directed multigraphs, vertex and edge representable probes together recover graphs and their morphisms; vertex probes alone can collide. | **Disclosed** by explicit proof/counterexample in [FORMALISM.md](FORMALISM.md) | Independently verify categorical typing, endpoint naturality, and edge counts. |
| AY-005 | For finite random variables, adding source/context to an observation cannot increase mean conditional Shannon entropy. | **Disclosed** identity | Does not imply individual-case or human-decoder improvement. |
| AY-006 | Shared histories can supply an efficient, partner-specific semantic interface. | **Conjectured application**; compatible with existing common-ground literature | Test against ordinary conversational grounding, rote association, and lexical familiarity. |
| AY-007 | The immediate feeling of being deeply understood reflects successful relational reconstruction, not merely familiarity, comfort, or confidence. | **UNVERIFIED** psychological mechanism | Requires independently scored reconstruction accuracy and separate subjective report. |
| AY-008 | Partner-specific relational reconstruction generalizes across unseen transformations better than lexical/context-frequency baselines. | **UNVERIFIED flagship discriminator** | Predeclared held-out tests; advantage must persist after controls. |
| AY-009 | The relevant human observations are accurately modeled by a category with composition and restricted Yoneda probes. | **UNVERIFIED formal bridge** | Construct the semantic category and observer functor; falsify with composition/naturality violations. |
| AY-010 | High identity-correlation, strong reported understanding, or common ground establishes actual intent, consciousness, or truth. | **Rejected inference** | These remain distinct; no claim of metaphysical equivalence. |
| AY-011 | The sender-context interaction is causally identifiable from a complete randomized factorial design under suitable controls and assumptions. | **Conditional methodological claim** | All cells, admissible manipulation, provenance, order and expectation checks required. |

A mathematical proof in an illustrative category cannot upgrade any empirical claim. Reuse of a source, participant, dataset, or model family does not create independent corroboration.

## Distinct rivals to separate

**R1 — simple association:** the recipient retrieves a remembered episode when hearing a familiar phrase; performance collapses on new paraphrases or relational changes.

**R2 — generic common ground:** ordinary shared knowledge and task experience explain the phenomenon entirely, with no distinctive Yoneda-style relational reconstruction beyond established grounding mechanisms.

**R3 — familiarity/affection/confidence:** the feeling is stronger with a close partner, but independent interpretation accuracy is unchanged or worse.

**R4 — sender attribution:** the apparent speaker's identity acts as a prior. Correct identity may help or bias a decoder; confidence alone is not evidence.

**R5 — shared bias:** both parties endorse the same inaccurate reconstruction, e.g., because of mutual expectations or social pressure. Agreement does not establish source-map adequacy.

**R6 — relational transport:** the proposed explanation. A dyad reconstructs declared semantic/affective relations under novel, preregistered context transformations more accurately than the rivals predict.

R6 should be preferred only if it explains both prior successes **and** residual failures without worse contradictions than R1–R5.

## Flagship probe: from inside joke to new meaning

### Data and consent

Recruit voluntarily consenting pairs with shared experience, plus consented unfamiliar comparison pairs. Do **not** elicit traumatic experiences, encourage conflict, or publicly disclose private jokes without explicit permission. Allow participants to withdraw any example. Use harmless, anonymized or synthetic incidents for initial calibration.

Have senders privately annotate an intended meaning profile **before** receivers interpret: key referent; relation between events; emotional valence; what changes under a specified counterfactual; which details are task-essential. These annotations are participant testimony, not access to private qualia or proof of worldly facts. Obtain context groundings and source provenance independently where practical; do not infer intended meaning solely from receiver agreement.

### Conditions

Use an ethically consented **2 × 2 factorial** of source cue (correct partner-specific attribution versus neutral/alternate permitted attribution) and context (congruent versus controlled perturbation), with all four cells observed under comparable stimulus quality:

| | Context congruent | Context perturbed |
|---|---|---|
| Correct source cue | Y11 | Y10 |
| Alternate/neutral cue | Y01 | Y00 |

A candidate interaction contrast is

$$
\Delta_{\mathrm{source}\times\mathrm{context}}
=(Y_{11}-Y_{10})-(Y_{01}-Y_{00}).
$$

Here each $Y$ is a **predeclared reconstruction-accuracy outcome**, not a subjective feeling score. No mixed-term claim is warranted without all four cells and an appropriate analysis for paired/repeated observations. Avoid representing fabricated quotations as actual words from a partner; where source authenticity is ethically consequential, use consented stylized avatars or transparent attribution tasks rather than deception.

### Additional instruments and controls

- **Positive control:** a well-rehearsed shared reference should ordinarily be recognizable. Failure means baseline task/instructions are broken.
- **Negative control:** an unshared, visually/lexically similar phrase should not reliably recover the private episode.
- **Null control:** a genuinely uninformative token should trigger "unknown," not forced agreement.
- **Mutation control:** change one *load-bearing relation* while holding much of the surface phrase constant; a relational decoder should change its interpretation when that relation changes.
- **Holdout A:** new paraphrases not heard or scored during calibration, with shared intended relational structure.
- **Holdout B:** new, consensual context shifts (e.g., playful to caring) in which a target relational feature must change.
- **Holdout C:** previously unobserved event families; otherwise a memorized phrase-event dictionary may masquerade as generalization.
- **Cross-partner holdout:** compare true partner-specific benefit with generic familiarity/language proficiency and task repetition.
- **Confidence control:** separately record *felt immediate understanding*, calibrated confidence, and actual reconstruction accuracy.
- **Blind scoring:** use sender-predeclared invariants and raters unaware of hypothesis/condition; keep source attribution and semantic-coding disagreements in the audit trail.

### Possible outcomes (decide before collecting data)

- **Support for R6, narrow:** partner-specific accuracy improves on novel relational and context transformations, beats preregistered common-ground and associative baselines, survives sender/source controls, and predicts accuracy better than subjective confidence alone. This corroborates a *bounded behavioral model*, not a theorem of private meaning.
- **Support for R1/R2 over R6:** advantage survives only on learned phrases or disappears after common-ground features and context are controlled. The Yoneda term adds no explanatory discrimination.
- **Support for R3/R5:** strong reported resonance with low or systematically biased reconstruction accuracy. The subjective phenomenon remains, but it is not evidence of faithful transport.
- **Ambiguous:** small samples, nonidentifiable interventions, unstable annotations, breached blinding, uncontrolled prosody, or large coder disagreements. Improve the probe; do not infer success.
- **Categorical refutation:** a declared meaning-transport mapping breaks composition or naturality on a calibrated counterexample. Repair the category or abandon that version of the bridge rather than changing the interpretation after seeing results.

## Concrete next work packages

1. **Formalizer:** define a small finite semantic category with literal objects and morphisms; prove identities/composition, and explicitly distinguish source attribution from intended meaning.
2. **Mathematical critic:** rederive the graph probe theorem independently; test probes that fail object separation or fail fullness despite object separation; ensure "dense" is never equated to "emotionally close."
3. **Experimentalist:** design a privacy-preserving held-out benchmark; preregister the $2\times2$ design, invariants, outcome coder, rivals, and statistical plan.
4. **Prior-art reviewer:** test whether partner-specific common-ground and conceptual-pact models already predict every proposed outcome. If yes, retain "affective Yoneda" only as an explanatory analogy.
5. **TLICA integrator:** type-check interfaces against κ, φ, σ, ρ, μ and the existing semantic-optics and interoperability dossiers; no foundation edits without separate explicit authorization.

**Next verdict-changing probe:** a novel relational-mutation transfer task with sender and context factorial controls that a simple association model predicts incorrectly. Existing dyad familiarity and perfectly rehearsed inside jokes are *not* holdouts.

**Completion condition:** preserve raw utterances only with permission, transformation descriptions, annotations, code, scoring disagreements, negative controls, and provenance. Report the most damaging counterexample as prominently as the best effect.