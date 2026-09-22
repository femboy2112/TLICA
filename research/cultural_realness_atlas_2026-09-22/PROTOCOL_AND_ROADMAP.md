# Protocol and roadmap

Status: proposed empirical work, NOT RUN. Date: 2026-09-22. The Python instrument is already implemented; it is not a participant experiment or music-understanding model.

## 1. Rivals and verdicts before data

H-R: declared relational correspondence contributes to recognition and, sometimes, realness beyond surface familiarity.
H-F: familiarity with vocabulary/style explains the effect without relational transport.
H-L: genre/performer labels and perceived affiliation explain it.
H-S: sonic features and current mood explain it; lyric structure adds no reliable prediction.
H-A: aspiration, imagination, or learned perspective-taking explains resonance without matched autobiographical experience.

These are not mutually exclusive. The target is incremental discrimination, not a forced winner. A positive finding about comprehension is not automatically a positive finding about resonance or developmental imprinting.

**Support:** preregistered relational contrasts improve held-out prediction of separately measured comprehension and realness beyond the named baselines, with reproducible annotation and the stated uncertainty criterion met. **Contrary result:** precise held-out effects below the predeclared smallest meaningful effect, or a surface/label model accounting for the apparent contribution. **Ambiguous:** wide uncertainty, unreliable annotation, failed manipulation, incomplete cells, leakage, or substantial unresolved participant disagreement. A null significance test alone is not evidence of equivalence. Set effect thresholds, stopping rules, and power targets after a feasibility pilot and before confirmatory data.

## 2. First empirical step: annotation feasibility

Create a small pilot of original micro-vignettes across care/work conflict, celebration, repair/craft, grief, humor, loyalty, and place attachment. Include cases expected NOT to correspond. This is stimulus engineering, not a representative cultural corpus. Original writing avoids reproducing copyrighted lyrics. Do not label the two fixture wrappers urban and rural; they are synthetic substitutions, not validated cultural encodings.

Have at least two separately working human annotators describe roles, predicates, alternatives, stakes, source spans, unknowns, and why a proposed mapping fails. Include relevant situated knowledge and permit rejection of the researcher's framing. Do not manufacture agreement by adjudicating away every disagreement. A single AI or multiple instances of the same model are not blind witnesses. Preserve pre-adjudication records and provenance. Consent is needed before collecting or publishing reports; identifying or sensitive information stays out of the public repo.

Freeze the predicate basis, node-kind rules, map-selection procedure, and evaluation rubric before the held-out set is opened. The prototype requires a declared common basis but does not verify that two annotators mean the same thing by a relation name. That semantic agreement is the first live probe-gap.

Minimum richer annotation record for the next implementation: episode/context ID; medium and date; narrator vs participant vs researcher layer; source-span locator; claim polarity; evidence status (asserted/denied/unknown/disputed); node kind; predicate definition; annotator; alternative codings; proposed map; excluded relations; world-level verification status. No fabricated timestamps or placeholder facts presented as observations.

## 3. Complete factorial pilot

Cross surface familiarity (higher/lower, verified for each participant) with structural correspondence (preserved/broken under a preregistered map). All four cells are required. Do not assume lexical similarity equals familiarity. Synthetic v0 cells only test an oracle supplied with graphs; they measure neither familiarity nor human recognition.

Construct matched relation mutations that do not systematically confound narrative coherence, readability, affective valence, length, or plausibility. Have a separate pretest check those properties. Some mutations necessarily change stakes; model or disclose that rather than claiming the structural manipulation was isolated. Counterbalance item variants so seeing one does not teach the intended answer on another. Record actual prior exposure, not inferred identity.

Measure comprehension with participant paraphrase and scenario predictions; separately measure felt realness, recognition, liking, sincerity, and affiliation. Use open-ended explanations before imposing ratings where practical. Analyze participant and item variation, and retain contradictory reports. Missing responses remain missing.

In a separate label-control block, hold the stimulus fixed and randomize disclosed category labels under an ethically reviewed design with appropriate debriefing. In a separate modality block, compare ethically licensed audio, instrumental material, and textual paraphrase. Do not claim a label x structure x modality interaction unless every required cell exists. No commercial-success outcome is tested here.

## 4. Falsifying the favored interpretation

Positive control: identity/relabeling of an agreed annotated relation. Negative control: explicit negation of that relation. Missing-observation control: delete the target annotation without asserting the opposite. Direction control: reverse a fact and preserve uncertainty about the original. Null control: unrelated predicates and an empty bridge. Scope control: allow a one-fact map but expose all untested relations. Mutation control: preserve the surface cues while breaking the predeclared relation.

Human controls are distinct from these software controls. Include familiar but disliked material, unfamiliar but accurately understood material, and highly resonant aspirational narratives without matched lived experience. A useful adverse outcome is: contextual explanation improves understanding but leaves realness unchanged. That would limit the account to comprehension rather than support its stronger resonance thesis.

For historical claims, compare documented pathways and actual institutional constraints. For causal equivalence, specify an intervention/action map and predicted consequences. Graph resemblance alone cannot provide either. To test durable formation rather than acute activation, add repeated observations with source/context removed and a justified longitudinal design; no manipulation of harmful exposure is called for.

## 5. Data and validation split

Pilot tuning data cannot validate the tuned model. Split by artifact/artist/story family and, where feasible, participant and setting, not merely by adjacent excerpts of the same work. Hold out a later cohort or setting for transport validation. A person born in the early 1990s did not necessarily encounter the relevant music or events in that decade; record developmental exposure dates rather than substituting birth year for listening history.

Benchmark relation-only, surface-only, combined, and label/sonic alternatives with matched information access and model-selection budgets. Treat annotation uncertainty as alternative representations or sensitivity analysis, not noise silently removed. Test whether any apparent success disappears when one source family or one motif is excluded. Report whether the result survives these checks; do not predeclare it Corroborated.

Public materials should contain rights-cleared stimuli, consent-compatible anonymized derived data, code, rubrics, hashes, and aggregate results. Lyrics/audio and raw personal narratives need explicit permissions and access controls. No scraping, recruitment, messaging, paid access, or external data collection was performed in this bootstrap.

## 6. Implementation stages and acceptance gates

**Stage A, done:** pinned base and isolated branch; source audit; explicit claim boundaries; typed graph schema, open-world comparison, partial composition; synthetic factorial, mutations, renamings, CLI/error controls; raw results and tests.

**Stage B, next:** annotation alternatives and provenance schema; machine-readable predicate dictionary; scoped map proposal interface that never silently optimizes a match after seeing an outcome; independent coding pilot. Acceptance: disagreements and unknowns round-trip without coercion, predicate definitions are auditable, held-out items remain unopened.

**Stage C:** preregistered listener study and baselines after ethics, consent, licensing, and power design. Acceptance: reliable manipulation, complete cells, preserved raw/adjusted views, no training-test leakage, interpretable negative results. No result is promised.

**Stage D:** contextual atlas from warranted correspondences, many-to-many memberships, time-indexed provenance, and failed-transport records. Acceptance: useful held-out prediction or explanation beyond existing simpler accounts. Population claims need an appropriate sample and historical claims need actual sources.

**Deferred:** a sheaf, metric, cultural fixed point, automatic latent-culture discovery, universal motif catalog, or listener truth score. Escalate mathematics only after the operational object requires it. The present category is of annotated episodes, not of whole persons.
