# Section to place in AGENTS.md and/or CLAUDE.md: GitHub math contract

> Copy this section into your actual repository agent instructions (or reference the file from those instructions) so it is visible to Codex and Claude before edits.

> **TLICA integration note.** This contract is vendored from
> [SMPTeX](https://github.com/femboy2112/SMPTeX). The calibration kit lives under
> [`docs/github-math/`](docs/github-math/README.md) (repo tooling, not wiki-mirrored).
> Two TLICA-specific carve-outs: (1) `scripts/github_math_fixtures/` and
> `docs/github-math/` hold deliberate edge cases and are excluded from the gates;
> (2) the guard's `DISPLAY_DELIMITER` policy (single-line `$$…$$`) is **not** treated
> as an error in TLICA — GitHub's own documentation renders block math on a single
> line, so it is a portability preference here, not a bug. Run the guard through
> `make check-math-portable`, which applies these exclusions.

## Markdown mathematics: SMPTeX contract

**Target output:** equations must be correct *and* render on the actual target GitHub surface. Read `docs/github-math/GITHUB_MATH_TEST_CARD.md` and `docs/github-math/MATH_COMPATIBILITY_LEDGER.md` before math-heavy documentation edits.

1. Use documented GitHub math syntax: `$...$` for simple inline math, `$`backtick delimiters for inline material that collides with Markdown parsing, and separate-line `$$...$$` or fenced `math` for displays. Do not use `\(...\)` or `\[...\]` as the default GitHub source convention.
2. Prefer portable primitives: `\frac`, `\sqrt`, `\sum`, `\prod`, `\mathbb`, `\mathcal`, `\mathrm`, `\text`, `\begin{aligned}`, `\begin{pmatrix}`, and `\begin{cases}`. A command being supported by LaTeX **does not** imply it is supported in GitHub's MathJax configuration.
3. For the rank/trace/closure family, prefer `\mathrm{rank}`, `\mathrm{Tr}`, `\mathrm{Cl}`. **A same-page GitHub mobile repository-Markdown A/B observation on 2026-10-23 found `\operatorname` explicitly rejected in inline, display, and math-fence contexts.** Do not blindly rewrite spacing-sensitive named operators: `\mathrm` produces upright letters but not all operator spacing and limits semantics. This does not establish a universal MathJax ban. See the ledger.
4. Do not silently introduce package imports, document preambles, global macros, TikZ, or LaTeX-only diagram environments into Markdown equations. Use separate diagrams where necessary, with explicit provenance and preview checks.
5. Every math-bearing Markdown edit must pass: `python scripts/math_guard.py . --strict-portable`, plus `python -m unittest discover -s tests -v`. If there is a failure, fix the mathematical/Markdown source, not the guard, unless the guard has a demonstrated false positive.
6. Source guard success is **not** a render certificate. For modified math components not covered by a previously observed matching calibration, open the rendered GitHub page after committing on a non-main branch; record its exact URL, commit, and observed status in the ledger. Never claim a visual check if no browser/UI inspection occurred.
7. After visual certification, separately review **semantic fidelity**: delimiters, quantifier scope, symbols, map direction, domain/codomain, indices, signs, and assumptions. Do not 'fix' a rendering failure by changing the asserted theorem.
8. When recording a failure, produce a minimal reproducer, a working nearby control, a failing challenge, and a cross-surface note (repo/wiki/PR). Prefer discriminating probes over global bans inferred from one broken example.

**Definition of done:** source linter green; math unit/mutation controls green; target renderer observed or marked UNVERIFIED; mathematical statement independently checked to the level its claim requires; ledger updated for novel macros/contexts.