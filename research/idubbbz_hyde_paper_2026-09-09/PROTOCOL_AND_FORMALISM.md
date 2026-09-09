# Protocol, formal scope, and hostile tests

**Status:** prospective archival study; no human coding or video alignment has run. The finite script is executed and has a separate boundary below. This protocol is a candidate design, not a registered study or a powered statistical analysis.

## 1. Object and rival accounts

The primary object is an episode of public critical performance, not the private person. The target claim is a relative tendency in **authority allocation**: whether a benchmark is comparatively stabilized to assess conduct, or a protocol is disrupted to make its operation an object of scrutiny.

Retain at least these rivals: genre explains the apparent difference; editorial role explains it; both creators use similar mixtures; audience affiliation determines coding; the selected documentary dominates the effect; or the proposed distinction is not reproducible at all. The preferred account must beat those alternatives on withheld material, not merely redescribe familiar clips.

No figure's moral worth, intelligence, authenticity, or clinical condition is an outcome variable.

## 2. Unit and coding record

Use a bounded episode with enough lead-in and aftermath to identify the relevant interaction. Preserve the full work separately. Every record needs:

- work ID, source URL, publication/date-confidence, acquisition date, file hash when legally obtained, and exact interval;
- event-family ID, recording/edit version, reused-footage links, transcript provenance and confidence;
- source-level words/actions versus coder inference;
- benchmark: target-stated, critic-stated, audience-implied, absent, or unresolved;
- target of scrutiny: act, person-model, norm, scene, editor, observer, or combination;
- intervention: absent, explicit, alleged, inferred, or unresolved, with what was changed;
- attribution: what the evidence is being used to infer and what rival remains;
- stated or demonstrated update condition, contrary evidence, and response;
- ethical annotations: consent scope, refusal, privacy, pressure, foreseeable consequences, and unknowns;
- coding disagreement and reason for any exclusion.

Do not assign missing items the value zero. Unknown intervention is not absence of intervention; no visible refusal is not proof of consent. A legal/public source may still require ethical care in quotation and redistribution.

## 3. Corpus and splitting

The attached CSV lists candidate works and access states, not a completed sample. Acquire originals or lawfully available transcripts before coding. Freeze the development subset and rules before selecting held-out intervals. Keep documentary editions in the same event-family cluster so one edition does not become training and the other a falsely independent test.

Stratify by genre and period where possible: takedown/commentary, staged performance, documentary encounter, self-reassessment, and explicit creative discussion. Include works likely to reverse the expected roles. Do not select only Ian's most judgmental clips and Hyde's most disruptive ones.

A reasonable initial qualitative pilot could examine several complete works per creator and predeclared intervals within each. This is not a numerical sample-size recommendation or a claim of statistical power. The pilot's job is to test the coding scheme and find counterexamples before any population estimate is contemplated.

## 4. Blinding and context preservation

Produce a text-only version with names and obvious branding masked when feasible, and preserve the unmasked contextual version. A coder unfamiliar with the source should record uncertainty rather than receive a speculative backstory. Other coders inspect the context-preserving version. Compare rather than conflate the two tasks.

Masking is not actual airgapping and may fail because of recognizable language. Record recognition. If removing identity deletes the very status relation under study, that item cannot serve as a clean name-blinding comparison. A masked version is a representation intervention with preservation obligations, not automatically an unbiased view.

Freeze initial judgments before discussion. A second pass by the same assistant is not an independent blind witness. Human coders or genuinely different reasoners can still share the same underlying source map; independence must be analyzed rather than asserted.

## 5. Controls and outcomes

**Positive control:** a constructed vignette explicitly compares an actor's words and action against the same declared rule. It should be coded as an adjudicative moment.

**Negative/counterexample control:** a constructed self-critique by the nominal disruptor or a staged provocation by the nominal auditor. The coding must follow the episode rather than the name.

**Null control:** alter names or irrelevant stylistic details while preserving the benchmark and intervention. A changed classification needs an explained reason.

**Mutation controls:** omit the actor's earlier qualification; replace an explicit norm with an analyst-supplied norm; remove a disclosure that a sequence was staged; reverse who is being judged. The source-aware record should detect the changed inferential basis.

**Pass for the narrow comparison:** coders can identify the modes with explicit reasoning; the predicted contrast recurs in held-out, reasonably matched material; it survives source-family ablation; and a simpler genre/edit-role account does not explain it equally well. This is qualitative support unless a justified statistical model is separately designed.

**Fail:** role allocation is not reproducible, the expected contrast reverses or vanishes across counterexamples, or every contrary episode must be reinterpreted to save the creator label.

**Ambiguous:** insufficient original context, unblinding, unresolved edition alignment, incompatible units, or too few independent works. Do not report ambiguity as success or as refutation.

## 6. Source-family and edit ablations

Run comparisons without the documentary encounter, without each creator's favored exemplar, without identity cues, and without explicit moral vocabulary. Preserve the raw and adjusted views. A residual change may show dependence on a source family; it does not prove that family false.

Reactions and summaries of an event are derivative for the claim that the event occurred in a certain way. They may be primary evidence of a particular audience reaction or editorial choice. Assign provenance relative to the claim, not a global 'good/bad source' label.

Leave-one-family-out checks are prospective. No numerical Moebius interaction, transported phasor, or phase claim is licensed. Complete factorial contrasts require every declared cell. Observational media clips do not become a randomized experiment by being arranged in a table.

## 7. Finite logical results and their proofs

### Result A: baseline equivalence does not identify the generator

Let a,n be binary. F(a,n)=a; G(a,n)=a XOR n. At n=0, both output a for all a. Therefore observations confined to n=0 cannot distinguish F from G. At n=1 they differ for both a. A fresh observation in that context can separate the candidates. This is exact for the declared functions; it does not identify anyone's motives.

### Result B: missing factorial cells leave an interaction undetermined

For four declared outcomes, Delta=y11-y10-y01+y00. If y11 is unobserved and otherwise unrestricted, changing it changes Delta while leaving all observed cells fixed. Therefore the full contrast is not determined by the other three cells alone. The script refuses incomplete or extra cells. For G's binary table, Delta=-2. The sign is arithmetic on this declared table, not an interpersonal emotional phase.

### Result C: representational detail alone need not discriminate

If two candidates agree on the entire observed dataset D, appending commentary that adds no observations or valid constraints does not alter that agreement. The script illustrates this with arbitrary detail strings. It does not assert that real detail never contains evidence; it isolates the phrase 'detail alone'.

### Result D: event editions are not event replications

Assign two edited records of one stipulated event the same event-family ID. They are different records but one event family by construction. This is provenance bookkeeping, not a measured correlation or a universal claim that editorial disagreement is uninformative.

### Result E: a predictive record does not specify a policy

The same stipulated prediction that a person will refuse can accompany a policy of stopping or a policy of increasing pressure. Therefore prediction alone does not select the policy. The claim that the person's agency should constrain that choice is an additional normative premise, not a theorem of the predictor.

## 8. Execution record

`structural_checks.py` ran under Python 3.13.5 on 2026-09-09: 16 tests, zero failures, zero errors. SHA-256 `f759b30641c559e3ca3c5c85a8c343cd78ba08ddc1834fe6768242ff5e9c4db4`; Git blob `60cb92d1606bbe452074300cbe9ea22cf18fb161`. [JSON](structural_checks_results.json) preserves the results in normalized whitespace; [test output](structural_checks_tests.txt) is the captured stderr text.

The checks include baseline, discriminating holdout, null, invalid-input, missing-cell, and explicit mutation counterchecks. They do not perform a general mutation search. The program is the same on both new branches; the two copies are not independent implementations. Full-repository validation and every human or creator-corpus claim remain separate.
