# GitHub Math Rendering — Diagnostic Report (2026-10-23)

**Status:** Wave C of the 2026-10-23 consolidation round. Adds a tool and a diagnostic;
changes no reader content. Companion to the plan-branch
`handoffs/GITHUB_MATH_RENDERING_CONTRACT_2026-10-23.md` and `MATH_RENDER_SMOKE_2026-10-23.md`.

## The hard caveat, stated first

This report rests on a **static, Markdown-aware** scan (`scripts/check_github_math.py`).
GitHub renders math with MathJax in the browser; a static scanner approximates GitHub's
*tokenization*, not its *rendering*. Therefore:

> **Rendered-GitHub status: UNVERIFIED.** No formula below has been confirmed to render by
> looking at a rendered GitHub page in a browser. A clean static scan is necessary, not
> sufficient. A passing Pandoc/PDF build is **not** evidence of GitHub rendering either.

The author's smoke specimen (`MATH_RENDER_SMOKE_2026-10-23.md`, on the plan branch) exists
precisely to do the real rendered check — its results table is still entirely UNVERIFIED
pending a human/browser view of the rendered page, especially the **S1** `\operatorname`
probe that this whole policy is built around.

## What was built

- `scripts/check_github_math.py` — a tiered, Markdown-aware checker. It tracks fenced code
  vs ```math blocks, inline code spans, the `$`...`$` collision-safe form, inline `$...$`
  and display `$$` math, and legacy `\(...\)`/`\[...\]` delimiters, so math-looking **source**
  (inside code) is never flagged and currency `$` never opens math. Rules: `GH-OPERATORNAME`,
  `GH-LEGACY-DELIM`, `GH-UNCLOSED-DISPLAY`, `GH-INLINE-DOLLAR`, `GH-BRACE-IMBALANCE`.
- Tiers: **FRONT** (README, CITATION, docs/**, current foundation, applications/** — strict),
  **RESEARCH** (research/** — house-style rules advisory/WARN, preserved-manuscript stance),
  **ARCHIVE** (byte-frozen subtrees — all advisory/INFO).
- `scripts/github_math_fixtures/` + `scripts/test_check_github_math.py` — 13 calibration
  controls (positive / negative / mutation), **all passing**. The negatives confirm the
  checker catches `\operatorname`, legacy delimiters, unclosed display, unclosed inline `$`,
  and brace imbalance; the positives confirm it does **not** flag valid math, currency, or
  math-looking source inside code fences.
- `make check-github-math` (advisory survey, never fails) and `make check-github-math-strict`
  (fails on FRONT-tier errors). Neither is wired into `make validate` — the existing validate
  contract (links + self-containment + term pins) is unchanged.

## Before inventory (static scan of 431 files, strict tiering)

| Severity | Count | What it is |
|---|---|---|
| ERROR (FRONT) | **136** | **all** in `applications/stickman_affective_dynamics_v0_1_0.md` (135 `\(...\)` legacy delimiters + 1 `\operatorname*{arg\,max}`) |
| WARN | 6822 | research-tier `\(...\)` legacy delimiters (established precedent) + research `\operatorname` (semantic_optics dossier ≈120, adultclub, vernacular) |
| INFO | 153 | archive-tier (byte-frozen originals/working drafts) |

**Verified-clean (0 errors):** root `README.md`, `CITATION.md`, all of `docs/**`, and the
current foundation files `foundation/0..5_*.md`. The v5.5.1 `\operatorname`→`\mathrm`
render-compat rider held on every true reader front-end. `GH-UNCLOSED-DISPLAY` and the
`GH-INLINE-DOLLAR` heuristic fired **0 times** across the whole archive (no false-positive
flood; the warning total is entirely the known legacy-delimiter convention).

## What was NOT changed, and why (flagged for author greenlight)

Per the plan's "correct current-facing broken expressions without indiscriminately rewriting
history" and the anti-overreach discipline, no reader content was mass-edited this wave. Two
render-debt items are flagged with safe, meaning-preserving recipes:

1. **`applications/stickman_affective_dynamics_v0_1_0.md` (136 FRONT errors).** This is a draft
   deliberately **not** wiki-promoted (author-gated). Recipe when greenlit: swap the 135
   `\(x\)`/`\[y\]` spans to `$x$`/`$$y$$` (meaning-preserving), and the one
   `\operatorname*{arg\,max}` to `\arg\max` (NOT `\mathrm` — the star form carries limit
   placement). 135 delimiter swaps on one paused draft is a careful per-span edit, not a
   global regex, so it is held for an explicit go.
2. **`research/semantic_optics_2026-10-01/**` (≈120 WARN) and a few other research dossiers.**
   Landed research-tier; all **plain** `\operatorname` (no star) → the exact
   `\operatorname`→`\mathrm` swap v5.5.1 already blessed as "semantically identical for these
   non-star operators." A research-tier render-errata commit would clear them; offered, not
   taken, because it is ~120 edits across a landed dossier and the research tier is advisory.

## Reproduce

```
make check-github-math          # advisory survey + 13 calibration controls
make check-github-math-strict   # FRONT-tier gate (currently fails on the stickman draft)
python3 scripts/test_check_github_math.py   # calibration controls alone
```

## Next (to move rendered status from UNVERIFIED to Observed)

Open the pushed smoke specimen's **rendered** GitHub page in a browser and fill its results
table — above all **S1 vs P3** (the `\operatorname` vs `\mathrm` comparison). That is the one
test that turns the author's repeated `\operatorname` report from a policy assumption into a
recorded observation tied to this GitHub rendering context.
