# CLAUDE.md

This repository's working agreement for coding agents is in [`AGENTS.md`](AGENTS.md), and the
GitHub-math authoring contract is in [`AGENTS_MATH_PROTOCOL.md`](AGENTS_MATH_PROTOCOL.md). Read
both before editing. The calibration kit (test card, source guard, compatibility ledger, mobile
fallback) lives under [`docs/github-math/`](docs/github-math/README.md).

Key invariants, repeated here because they are easy to violate: never edit the frozen foundation
(`foundation/0..5_*.md`) except presentationally or under separate authorization; run
`make validate` after any structural edit; never claim a check, tool, or render you did not run.
