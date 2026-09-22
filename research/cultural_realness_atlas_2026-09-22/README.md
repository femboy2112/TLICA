# Cultural Realness Atlas

**Shared social structures, different local meanings**  
Research-tier bootstrap v0.1.0 | 2026-09-22 | Author: Leah, with AI-assisted research and implementation.

**Question:** What selected relations can survive translation between cultural encodings, and when does recognizing them help an artifact feel real to a listener?

This is an overlapping, context-indexed research atlas, not a classification of Americans into fixed human types. Rap and country motivate the inquiry; neither genre is equated with a demographic group. Structural correspondence, historical linkage, felt meaning, factual truth, liking, and commercial success remain separate.

Base: `femboy2112/TLICA` at `471c28566dbf08b54bbc64d2c83089806a772e9f`. Review branch: `research/cultural-realness-atlas-2026-09-22`. Foundation v5.5.1, applications, and main are unchanged by this dossier.

## Read and run

Start with [the research draft](RESEARCH_DRAFT.md), [the claim ledger](CLAIM_LEDGER.md), and [the local-session handoff](LOCAL_SESSION_HANDOFF.md). [Author context](AUTHOR_CONTEXT.md) preserves the seed and corrections. [Sources](SOURCES.md) records inspected primary material and access limits. [Protocol and roadmap](PROTOCOL_AND_ROADMAP.md) defines the unrun empirical work.

```bash
cd research/cultural_realness_atlas_2026-09-22
python3 -m unittest -v test_transport_probe
python3 transport_probe.py --output /tmp/cultural-realness-results.json
python3 -m py_compile transport_probe.py test_transport_probe.py
```

Python 3.10 or newer; standard library only. [The validator](transport_probe.py) accepts an optional `--input` JSON containing `source`, `target`, and `map`. Use `fixture()` for the episode schema. It validates supplied annotations and an explicit injective node map; it does not extract meaning from text or audio, discover a mapping, or model a listener.

## Executed first work

[Raw results](RESULTS.json) and [test output](VALIDATION.txt) record **28 passing tests**, all four synthetic surface/structure cells, **24 node-renaming checks**, and **four single-fact polarity mutations detected**. A partial transport supports one fact while leaving three untested. Missing observations remain unknown; an explicitly denied mapped fact is contradicted; reversal alone is not logical negation. A finite action-table counterexample separates observed agreement from unobserved consequences.

These are author-created calibration cases, not corpus results or independent holdouts. No participants were recruited; no songs or lyrics were analyzed; no learner was trained. The mathematical claims and the empirical conjectures have different statuses in the ledger.

## Integration boundary

GitHub connector reads and branch writes are available. The container's attempted Git clone failed because `github.com` could not be resolved. This directory was tested as an isolated staging package, not as a full repository checkout. **The repository-wide `make validate` was NOT RUN.** Run it in the complete local checkout before merging. Do not promote this work to foundation, publish a wiki, or register an application paper as part of this bootstrap.
