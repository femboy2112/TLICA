# Finite-case input contract, v0.1

The input is a JSON list of cases. `fixtures.py` constructs all eight calibration inputs deterministically. To inspect or export them:

```bash
python3 -c 'import json; from fixtures import cases; print(json.dumps(cases(), indent=2))' > /tmp/cultural-interop-cases.json
python3 interop.py /tmp/cultural-interop-cases.json --output /tmp/cultural-interop-results.json
```

A case carries `schema_version: "0.1"`, `kind: "synthetic"`, an `id`, an explanatory `description`, `parties`, `sources`, `constraints`, and `options`. The parser supports 1–4 parties, up to 8 constraints, and at most 128 options, subject to the required gate types below. Empty option lists are permitted and explicitly reported as a pathway gap.

Source records contain a unique `id`, a provenance `family`, and a status: `confirmed`, `unverified`, or `disputed`. In this version, confirmed means stipulated as available in the synthetic exercise. It is NOT a general factual truth label, an independently verified citation, or a TLICA phi value. Shared-family duplicates do not count as independent corroboration. All cited sources of a constraint are jointly required; this interface does not perform probabilistic evidence fusion.

A constraint has a unique `id`, a `kind` of `reality`, `standing`, or `party_floor`, and a nonempty list of `source_ids`. A party floor also names its `owner`. At least one explicit reality gate, one standing/third-party gate, and a floor for every party are mandatory. Their presence cannot prove that all affected people or real harms were represented; that remains a source-map and scope responsibility.

Each option has a unique `id`; a complete `checks` dictionary over constraint ids; a complete `consent` dictionary over parties; and a complete `ranks` dictionary of integer ordinal preferences. Checks and consent are literal JSON true, false, or null. No default consent exists. An unverified required source makes its gate unknown regardless of the supplied check value. A known failing gate still rejects the option even when another gate is unknown.

Ranks use higher values for preferred options. They are only compared within a participant; they are never summed across participants. A candidate passing every gate is supported in this exercise, not proven to make a real person happy. The preference frontier ranges over supported candidates only, not pending or unlisted options.

The `kind` guard rejects explicitly non-synthetic cases in this bootstrap. A label cannot verify provenance or provide privacy protection against a mislabeled input. Do not enter live personal data. Typed human records, current consent, access control, expiry, partial preferences, and suitable review remain future work.
