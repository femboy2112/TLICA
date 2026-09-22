# Shared Reality, Different Lives

## A cultural-interoperability research program

**Status:** research-tier bootstrap v0.1.0, 2026-09-22. Concept and priorities: Leah. Drafting, source checks, formalization, and prototype: AI-assisted; not yet author-ratified as a paper.

**Base:** `femboy2112/TLICA`, `main` at `471c28566dbf08b54bbc64d2c83089806a772e9f`.
**Branch:** `aletheia/cultural-interoperability-2026-09-22`.
**Foundation:** v5.5.1, unchanged. No existing application is replaced.

> The goal is not to sort Americans into boxes. It is to help particular people understand where their lives and interpretations diverge, locate the actual conflict, and discover reality-grounded arrangements they can freely endorse without erasing either person.

Music prompted the inquiry but is **one observation channel**, not the target domain. Rap and country illustrate how locally meaningful expressions can carry related social structures without identical histories or phenomenology. The larger target includes work, family, neighborhoods, institutions, material constraints, and everyday disagreement. No genre, region, race, or class is treated as a personality or belief detector.

## Read in this order

1. [AUTHOR_RECORD.md](AUTHOR_RECORD.md): exact originating prompts and the scope correction.
2. [MANUSCRIPT.md](MANUSCRIPT.md): the research object and its relationship to existing work.
3. [FORMALISM.md](FORMALISM.md): bounded definitions, proofs, and counterexamples.
4. [PROTOCOL.md](PROTOCOL.md): discriminating probes and conditions for human work.
5. [SOURCES.md](SOURCES.md) and [RECONCILIATION.md](RECONCILIATION.md): source access, inherited machinery, and corrections.
6. [HANDOFF.md](HANDOFF.md): integration, next tasks, and acceptance gates.
7. [checks/VALIDATION.md](checks/VALIDATION.md): executed results and limits.

## Executable first step

From this directory, run:

```bash
python3 run_checks.py
python3 mutation_checks.py
python3 -m py_compile interop.py fixtures.py test_interop.py run_checks.py mutation_checks.py
```

Python 3.10+; standard library only. The finite instrument checks supplied constraints, explicit option consent, provenance availability, and ordinal preferences. It preserves unresolved evidence, returns a set of non-dominated supported options rather than choosing a winner, and reports minimal blocking sets when the supplied catalog is incompatible. It also checks declared graph transports and finite rival/probe splits.

**This is not yet a semantic parser, cultural atlas, trained learner, mediator, or validated human model.** All eight fixtures are invented. The tests calibrate an instrument; they do not validate TLICA or demonstrate that a real dispute was resolved.

The principal empirical hypothesis remains **CONJECTURED / UNVERIFIED**: task-indexed, participant-correctable reconstruction plus reality-grounded option search can improve reciprocal understanding and durable, non-coercive coexistence beyond simpler alternatives.
