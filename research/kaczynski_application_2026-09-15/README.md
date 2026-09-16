# When the Map Becomes a Mandate — application supplement

**Leah · first application-paper draft v0.1.0 · 15 September 2026.**

The substantive argument is now in [the application paper](../../applications/when_the_map_becomes_a_mandate_v0_1_0.md), rather than in a plan for a future paper. It contains three worked applications, four conditional propositions with proofs, a literature comparison, documentary conclusions, finite witnesses, and the remaining discriminators. This does not convert an unverified developmental account into an established cause.

The [original Phase 1 dossier](../kaczynski_focus_closure_2026-09-15/README.md) is retained byte-for-byte. Its manuscript, ten development observations, original nineteen-claim ledger, source access statements, and historical test logs remain records of that phase. This supplement adds a new layer without rewriting those records.

## Read the package

| File | Role |
|---|---|
| [Application paper](../../applications/when_the_map_becomes_a_mandate_v0_1_0.md) | Canonical substantive first draft, with its own bibliography |
| [Plain-language exposition](../../docs/app-map-becomes-mandate.md) | Matching wiki-source draft; no stronger conclusions than the paper |
| [Theory and source audit](THEORY_ALIGNMENT_AND_SOURCE_AUDIT.md) | Current-main reconciliation and changes in external-source access |
| [Claims and probes](CLAIMS_AND_PROBES.md) | What is demonstrated, what is observed in records, and what remains conjectural |
| [Executable witnesses](evidence_probe.py) | Standard-library construction checks and declared source-dependency removals |
| [Raw results](RAW_RESULTS.json) | Actual outputs, including all 32 tracking comparisons |
| [Validation output](VALIDATION.txt) | Actual test output; not historical verification |
| [Local Claude integration prompt](LOCAL_CLAUDE_INTEGRATION_PROMPT.md) | Review and integration into current main without overwriting concurrent work |

## Reproduce

From a repository checkout:

```sh
python3 research/kaczynski_application_2026-09-15/evidence_probe.py --test
python3 research/kaczynski_application_2026-09-15/evidence_probe.py --output /tmp/kaczynski-application-results.json
python3 research/kaczynski_focus_closure_2026-09-15/scripts/validate.py
python3 -m unittest discover -s research/kaczynski_focus_closure_2026-09-15/scripts -p 'test_*.py' -v
make validate
```

The new executable has sixteen unit/control tests. Its finite constructions use rational arithmetic, not fitted human parameters. The source-removal table is computed from explicitly declared citation dependencies: it does not independently re-code documents, measure causal effects, or estimate truth probabilities. The two permission countermodels do not assert that both normative rules are ethically acceptable.

The new sixteen tests and the original fourteen tests were actually run in the drafting environment. A complete repository checkout was unavailable, so whole-repository `make validate` was **not run**. Local artifact checks are narrower than that gate. No independent human coding, fresh holdout, clinical assessment, original-archive replication, or prevention intervention has run.

## Two different snapshots

Research branch parent: `f436412733b39b15fd7c3394d6a5064e9b5dc39c` on `research/kaczynski-focus-closure-2026-09-15`.

Current theory/application snapshot reviewed: `33d449424dd909bab5dfe8e80f302df733bd2770` on main. The foundation remains v5.5.0; recent changes are application and research refinements. The newer developmental and institutional files are not backported wholesale into this older research branch. The paper restates their relevant definitions and records exact source paths and commit. The integration handoff preserves the current mainline versions.

No foundation file, application index, Makefile, citation register, or generated wiki is changed by this drafting package. Mainline registration is intentionally reserved for the user's running Claude session. An application-tier file is a first draft, not a promotion of its conjectures to foundation commitments.
