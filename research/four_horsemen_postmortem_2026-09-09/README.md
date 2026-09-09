# A Post-Mortem of the Four Horsemen

**Debate, charity, identity, and model lock in public reason**

Leah, with assistant-assisted research and drafting · 2026-09-09 · v0.1.0

Start with the [research manuscript](MANUSCRIPT.md). It develops the conversation's four proposed failure sites while allowing the evidence to weaken, narrow, or reject the personal attribution. It is a researched working paper, not a validated psychological taxonomy.

## Contents

- [Manuscript](MANUSCRIPT.md): approximately 5,000 words of argument, case analysis, counterexamples, and conclusions.
- [Sources and claim ledger](SOURCES_AND_CLAIM_LEDGER.md): primary-source register, access limits, linked source families, statuses, and corrections to the original conversation.
- [Probes and limitations](PROBES_AND_LIMITATIONS.md): prospective discriminating tests with pass/fail/ambiguous outcomes and controls; no claim that these experiments have run.
- [Integration and validation](INTEGRATION_AND_VALIDATION.md): exact repository baseline, branch boundary, local validation scope, and handoff.
- [Validation script](validate_package.py) and [actual scoped output](validation_output.txt): standard-library integrity checks and an exact finite counterexample; not empirical validation of the diagnoses.

## Reading rule

**The four names are starting points, not boxes that the evidence must fill.** The distinction between understanding and equal credibility is retained, while its alleged characteristic attribution to Dennett remains unestablished. Identity coupling is not measured in Dawkins. The Harris case concerns an inspected operational-warrant dispute, not a blanket attribution about Muslims. The Hitchens portrait preserves correction as well as error.

The common proposal is *warrant substitution*: success under one acceptance criterion is treated as warrant under another without checking the additional conditions. This is an author-level analytic term, not a new canonical TLICA coordinate or an empirical law.

## Repository boundary

Branch: `agent/four-horsemen-postmortem-2026-09-09`.

Base: main commit `0eb46646a1c18850ab5204921cb2edc76bb1e64b`.

The related geometry/immersion material was read at `e6b1b33611489af4c1598f6140548e7a2700de7b` on its separate branch. It is cited, not merged. This package changes no foundation, application registration, existing research note, or runtime code.

From a full checkout, reproduce the package checks with:

```sh
python3 research/four_horsemen_postmortem_2026-09-09/validate_package.py
```

Then run the repository's `make validate` before integration. The latter was not run on a complete checkout in this session; the integration record explains the access and scope distinction. No merge or pull request is part of this delivery.
