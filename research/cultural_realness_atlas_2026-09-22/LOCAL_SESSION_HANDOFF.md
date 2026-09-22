# Local-session handoff

Base: `471c28566dbf08b54bbc64d2c83089806a772e9f`. Branch: `research/cultural-realness-atlas-2026-09-22`. Directory: `research/cultural_realness_atlas_2026-09-22/`.

## Integration

Inspect repo identity, current branch/HEAD, worktree changes, repository instructions, and remote state before switching or merging. Preserve other sessions' work. Fetch the review branch; inspect its diff against the recorded base and reconcile any newer main commits. This session did not merge or push main.

Read README, RESEARCH_DRAFT, CLAIM_LEDGER, SOURCES, and PROTOCOL_AND_ROADMAP. Run:

```bash
python3 -m unittest discover -s research/cultural_realness_atlas_2026-09-22 -p 'test_*.py' -v
python3 research/cultural_realness_atlas_2026-09-22/transport_probe.py --output /tmp/cultural-realness-results.json
make validate
```

The first two run on standard-library Python 3.10+. Results may differ in Python-version metadata and script hash after a code change; substantive fixture outputs should agree. Raw results include repeated positive-control rows by design. Full `make validate` was unavailable in the staging container and is a mandatory local integration gate.

After review and passing gates, integrate into main as RESEARCH-TIER only, following the user's requested main-integration workflow. Add a concise research-index entry if appropriate. Do not edit foundation, promote an application, publish the wiki, or infer authorization for unrelated pending work. Do not overwrite local changes or force-push.

Suggested research-index text:

> Cultural Realness Atlas (2026-09-22): overlapping contexts, partial relational transports, and perceived musical realness. Contains a scoped primary-source audit, exact finite counterexamples, a tested annotation validator, and a proposed independent-coding/listener protocol. Research-tier; human and corpus mechanisms UNVERIFIED; foundation unchanged.

## Continue at the actual frontier

The next gap is semantic measurement, not additional decorative mathematics. Implement alternative annotations and predicate-definition provenance; pilot independent coding on original work/care, craft, humor, grief, and belonging vignettes. Freeze the coding and bridge rules before held-out evaluation. Then design the listener study against surface familiarity, genre labels, sonic response, and aspiration. No participants, real songs, or independent annotations exist in this branch yet.

Keep world events, narratives, participant interpretations, and researcher coding separate. Keep missing facts unknown. A good map on a small domain is not equivalence. Structure-mapping and rap/country comparison have prior art. The category currently established is of annotated graphs and partial fact-preserving injections, not cultures or persons. No sheaf or psychological interaction was demonstrated.

## Paste-ready prompt

```text
Fetch research/cultural-realness-atlas-2026-09-22 in femboy2112/TLICA. Check repo instructions, HEAD, main drift, and dirty worktree; preserve other sessions' work. Read research/cultural_realness_atlas_2026-09-22/{README,RESEARCH_DRAFT,CLAIM_LEDGER,SOURCES,PROTOCOL_AND_ROADMAP,LOCAL_SESSION_HANDOFF}.md. Review the diff from base 471c28566dbf08b54bbc64d2c83089806a772e9f, reproduce the 28 tests and calibration, and run full make validate. Reconcile and bring to main as research-tier only; add an index entry without changing foundation. Continue with an alternative-annotation/provenance schema and an independently coded pilot of original vignettes, freezing rules before holdouts. Preserve the separation of structure, history, phenomenology, truth, and liking. Do not call the synthetic checks listener evidence, a corpus result, or a cultural sheaf. Report actual runs, failures, and the next discriminating probe.
```
