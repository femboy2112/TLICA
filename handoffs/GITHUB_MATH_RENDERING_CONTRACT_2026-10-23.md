# GitHub Math Rendering Contract — TLICA
**Date:** 2026-10-23
**Status:** Project compatibility policy for the consolidation; explicitly empirical where GitHub rendering behavior is concerned.
**Official reference:** https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions
**Smoke specimen:** [MATH_RENDER_SMOKE_2026-10-23.md](MATH_RENDER_SMOKE_2026-10-23.md)

## Why this is a separate workstream

TLICA uses large amounts of mixed Markdown and mathematics. The project has repeatedly suffered expressions that are valid LaTeX yet render badly or disappear on GitHub. A passing Pandoc/PDF build does not establish GitHub compatibility; a raw Markdown text audit does not establish visible correctness.

GitHub's official document (verified 2026-10-23) says GitHub Markdown math renders through MathJax on Markdown files, PRs, issues, discussions, and wikis. The officially documented forms are `$...$` for inline math; the backtick-wrapped inline alternative (dollar + backtick + expression + backtick + dollar) when Markdown conflicts; `$$...$$` on their own lines for display math; and fenced `math` code blocks. Dollar literals require care. This documentation is not an exhaustive macro compatibility guarantee.

**Important observed hazard:** the author repeatedly finds `\operatorname` broken on GitHub. Even though standard MathJax supports many macros and `\operatorname` may work under some setups, do not assume it works reliably through this project's GitHub Markdown pipeline. Treat `\operatorname` and `\operatorname*` in newly authored/current-facing GitHub pages as disallowed pending actual positive rendering evidence. This is a *project-safe profile*, not a universal assertion that the macro never works.

## Target-specific syntax profile

| Situation | Default authoring | Notes |
|---|---|---|
| Simple inline math | `$x^2+y^2$` | Use dollar delimiters carefully around Markdown/currency. |
| Inline collision with Markdown | official dollar-backtick syntax | Syntax: dollar + backtick + math + backtick + dollar; see official examples. |
| Multi-line standalone math | `$$` on own line, body, closing `$$` on own line | Prefer blank lines before/after a block. |
| Alternative display math | fenced `math` block | Good for complex multiline displays; verify actual GitHub view. |
| Render literal dollars | Escape or isolate as in official GitHub examples | Check math adjacent to currency figures. |
| Named operator labels | `\mathrm{MaxFlow}` or `\text{MaxFlow}` when appropriate | Operator spacing may differ. Consider `\mathop{\mathrm{MaxFlow}}` only after verified rendering. |
| argmax and built-in operators | `\arg\max` or semantically correct alternative | Never mechanically replace `\operatorname*{arg\,max}` without checking limit placement. |
| Legacy TeX delimiters | `\( ... \)` and `\[ ... \]` | They appear in historical documents but are not the reference page's preferred examples; test on GitHub rather than assuming. |

Keep **strict active-surface rules** for README, docs, current application/research introductions, and maintained formulas; use an **advisory history mode** for preserved manuscripts, old derivations, and provenance. Differentiate GitHub Markdown from actual `.tex` source.

## Semantics-preserving repair

- `\operatorname{MaxFlow}_{G}(s,t)` is not always spacing-identical to `\mathrm{MaxFlow}_{G}(s,t)`. Where needed use explicitly validated spacing or a proven compatible math-operator wrapper. Check displayed meaning.
- `\operatorname*{arg\,max}` can place limits differently. Preserve the actual operation and limit placement using a tested replacement, such as `\arg\max` where mathematically appropriate.
- `\text{world item}` and `\mathrm{world}` are different intentions: ordinary words vs upright math letters.
- Do not accidentally alter index binding, condition scope, punctuation, nested fractions, or claim statuses while repairing rendering.
- Moving difficult inline math outside a table may be safer than forcing brittle delimiter behavior. Do not globally rewrite archived formulas with regex.

## Required two-level proof of rendering

**Baseline inventory:** file + line counts for delimiter issues; suspect operator macros; dollar/currency collisions; code-fence confusion; tables and lists; unclosed math blocks; mismatched braces; exposed math in the beginner path. Include an explicit scope declaration.

**Positive controls:** Greek letters, subscripts/superscripts, fractions, sets, closure notation, operators, integrals, arrows, matrices, aligned multi-line math, text in math, a plain-text/null control, and rendered examples after the wiki transformation.

**Negative and mutation controls:** unmatched dollar/brace; `\operatorname` as a suspected local failure; intentional math-looking text in fenced code (must NOT turn into math); escaped currency `$`; malformed math + currency on one line; nesting errors; malformed markdown table; unclosed fence. The static checker must catch the rules it advertises without false positives for intentional source snippets.

**Local/static check:** Build scripts/check_github_math.py (or equivalent) and script-local tests with path, line, rule ID, severity, and explanatory message. Respect code fences, inline code, escaped delimiters, Markdown links, and file tiers. Do not confuse a regex sweep with a Markdown parser.

**Actual web check:** Inspect *rendered* GitHub PR/branch pages after MathJax has executed; check selected source pages and the generated GitHub Wiki mirror, not merely raw Markdown or API JSON. Record exact SHA, permalink, viewport/screenshot or other direct visual observation, and defects. If browser rendering access is unavailable, say **UNVERIFIED**; do not claim that static or Pandoc success proves MathJax success.

**Important surfaces:** root README, foundation reading guide and current formal apparatus, docs/glossary.md, docs/three-coordinates.md, docs/tlica-epic.md, research/semantic_optics_2026-10-01, research/vernacular_dynamics_2026-10-12/FORMALISM.md, current research landing pages and newly integrated dossiers.

## Automation and release gate

Provide a low-cost `make check-github-math` target with both strict current-facing and advisory archival scans and committed positive/negative fixture tests. Run the checker before merging updated prose, and run the GitHub-visual smoke review on a representative cross-section. Report counts before/after and every exception; keep math diff independent of conceptual revisions when feasible. Include wiki build/transform checks and link-anchor tests. Never claim a pass without execution.

The companion smoke file deliberately contains **expected-to-work formulas and one quarantined suspect operator probe on the plan-only branch**. If the suspect fails there, this is a concrete observation tied to that GitHub rendering context, not a claim that no MathJax installation ever supports it. If it succeeds, investigate the exact failing Markdown context instead of dismissing the author's reports.
