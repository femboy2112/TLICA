# The Mathematics of the Sauce
## Observer-relative vernacular dynamics: slang as a candidate compression of lived structure

**Status:** research-tier bootstrap v0.1.0, 2026-10-12. **Original project proposal:** Leah. **AI-assisted:** formalization, source reconnaissance, finite calibration, documentation. **Human mechanism claims:** CONJECTURED / UNVERIFIED; author review pending.
**Base:** femboy2112/TLICA main at 821ce7e6f57524d32e767a9c5ec5303e1796115e. **Working branch:** research/vernacular-dynamics-2026-10-12.
**Foundation impact:** none. No new TLICA coordinate or developmental mode, no application registration, no publication.

### Research question

Does naturally occurring slang pick out useful, context-sensitive **configurations or transitions** in how humans encounter, interpret, focus, protect, and act on their world? Can TLICA make those distinctions sharper, rather than merely rewording slang in mathematics?

The principal object is **not** a dictionary that tells us what a person really is from one phrase. It is a typed, source-aware lexicon of candidate mechanisms, **including the speech act of using the word**, plus precise counterexamples, uncertainty, and risky discriminators.

Initial entries: **vibe**, **cope**, **lost in the sauce**. Each has multiple readings. A label utterance is an observation, not an assay of the target's private state.

### Reading and execution

1. [AUTHOR_SEED.md](AUTHOR_SEED.md) — originating proposal, not retroactively reconstructed as a proven theory.
2. [FORMALISM.md](FORMALISM.md) — types, operational fibers, three elementary conditional results, and TLICA bridge.
3. [LEXICON_V0.md](LEXICON_V0.md) — first three entries with semantic variants, observational predictions, and counterexamples.
4. [PROBES.md](PROBES.md) — tests that could make the interpretations fail, with baselines and controls.
5. [SOURCES_AND_LEDGER.md](SOURCES_AND_LEDGER.md) — inspected vernacular-source pointers and separate mathematical/empirical statuses.
6. [RECONCILIATION.md](RECONCILIATION.md) — exact existing TLICA dependencies, pending EPIC branch, non-imports.
7. [VALIDATION.md](VALIDATION.md) — finite probe calibration and explicitly unrun tests.

Run from this directory:

~~~bash
python3 -m unittest -v test_finite_lexicon
python3 finite_lexicon.py
python3 -m py_compile finite_lexicon.py test_finite_lexicon.py
~~~

The test instrument uses **invented worlds**, standard-library Python, and no learned classifier. All tests are finite-model bookkeeping, not evidence that any slang word detects a human mechanism.

### Dependence boundaries

- TLICA foundation: [formal apparatus](../../foundation/3_formal_apparatus.md) and [method](../../docs/research-method.md).
- TLICA prior research: [Semantic Optics](../semantic_optics_2026-10-01/README.md), [Cultural Interoperability](../cultural_interoperability_2026-09-22/README.md), and [Cultural Realness Atlas](../cultural_realness_atlas_2026-09-22/README.md).
- TLICA–EPIC v0.5.2 is currently [draft PR #10](https://github.com/femboy2112/TLICA/pull/10), not part of main; we borrow the **world-first typing discipline as a proposed compatibility rule**, not its unmerged DSL or executable reader.

**Acceptance criterion for future scientific warrant:** on held-out usages from multiple communities, a typed contextual model must discriminate slang senses and observable consequences *better than simpler lexical and behavioral baselines* while reporting unresolved ambiguity, source weaknesses, and participant corrections. If it cannot, reject its supposed advantage.
