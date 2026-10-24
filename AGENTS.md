# AGENTS.md — working agreement for TLICA

TLICA is a pure-Markdown theory archive: the frozen foundation (`foundation/0..5_*.md`),
application papers (`applications/`), research dossiers (`research/`), and the
plain-language reader wiki source (`docs/`). The Markdown is authoritative; PDFs and
the GitHub Wiki are generated mirrors.

## Non-negotiables

1. **Never edit the frozen foundation** (`foundation/0..5_*.md`) except strictly-presentational
   changes or separately-authorized mathematical amendments. The foundation is versioned and
   gated; substantive changes go through the author.
2. **Run `make validate`** after any edit that adds, moves, or links a document, and always when
   registering a new application paper. It gates link integrity, self-containment, term pins, and
   GitHub-math source validity, with pure standard-library Python (no network, no LaTeX).
3. **Never invent** tools, tests, commits, tags, or validation. Verify before claiming. A passing
   PDF build is not evidence about GitHub Markdown rendering.

## Markdown mathematics

Before any math-heavy edit, follow the GitHub-math contract in
[`AGENTS_MATH_PROTOCOL.md`](AGENTS_MATH_PROTOCOL.md), and consult the calibration kit under
[`docs/github-math/`](docs/github-math/README.md). In short: use documented GitHub delimiters
(`$…$`, `` $`…`$ ``, `$$…$$`, ```` ```math ````), prefer portable primitives (`\mathrm` over
`\operatorname`), keep bare `|` out of table-cell math, and treat a green source guard as
necessary-not-sufficient — the rendered GitHub view stays UNVERIFIED until a human looks.

Run the source guards with `make check-math-portable` (SMPTeX, strict-portable) and
`make check-github-math-strict` (TLICA, part of `make validate`).
