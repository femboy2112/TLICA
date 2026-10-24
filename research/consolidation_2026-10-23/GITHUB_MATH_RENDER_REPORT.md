# GitHub Math Rendering — Diagnostic Report (2026-10-23, rev. 2)

**Status:** the render-repair pass of the 2026-10-23 consolidation round. Rev. 2 records
the fixes that were **applied and pushed**, the rendered-page observations that drove them,
and the two classes left flagged-not-fixed. Companion to the plan-branch
`handoffs/GITHUB_MATH_RENDERING_CONTRACT_2026-10-23.md` and `MATH_RENDER_SMOKE_2026-10-23.md`.

## The hard caveat, still stated first

A static scanner approximates GitHub's *tokenization*, not MathJax's *rendering*. A clean
static scan is necessary, not sufficient; a passing PDF build is **not** evidence of GitHub
rendering. What changed in rev. 2: two failure classes were moved from assumption to
**rendered-page observation** before being fixed (see below). A full per-page render pass
across the whole tree is still **UNVERIFIED** — it needs a human on the rendered pages (no
browser was available in the repair session).

## What the rendered pages actually showed (observations, not assumptions)

1. **`research/README.md`** — the inline `\(\rho\)`, `\(\varphi\)` spans came through the
   served GitHub page as **literal `(\rho)` text, not math.** Confirms GitHub does not accept
   the legacy `\(...\)` delimiter (matches the official docs: only `$...$`, `` $`...`$ ``,
   `$$...$$`, ```` ```math ```` are supported).
2. **`research/recursive_epistemic_ratchet_2026-10-02.md`** — the display block
   `$$ \n W_t \n = \n (K_t,\dots) \n $$` rendered with **`W_t` as an `<h1>` heading** (GitHub
   auto-generated the anchor `#w_t`), the row of `=` consumed as a **setext underline**, and
   the `$$` delimiters orphaned — the equation shattered. This is the dominant breakage the
   author reported as "still scattered throughout the repo," and the previous static checker
   was blind to it.

## Fixes applied and pushed (`9ba4d46`, `c4ef598`)

| Class | Evidence | Fix (meaning-preserving) | Scope |
|---|---|---|---|
| Legacy `\(...\)` | rendered: literal text | `$...$` | 3226 spans |
| Legacy `\[...\]` | docs: unsupported | `$$...$$` (standalone/blockquoted delimiter lines) | ~2630 blocks |
| `\operatorname{F}` | recorded broken (v5.5.1) | `\mathrm{F}` (non-star) | 161 |
| `\operatorname*{F}` | recorded broken | `\mathop{\mathrm{F}}` (keeps under-limits) | (subset) |
| **setext-shatter** | **rendered: `W_t` → heading** | merge lone `=`/`-` onto prev line (`W_t\n=` → `W_t =`) | **499 lines, 70 files** |

All swaps are byte-equivalent math (newlines are insignificant in TeX; `\mathrm` vs
`\operatorname` is identical glyph for non-star operators). `.md` + tooling only — no
executable file touched, **61/61 witnesses pass**, `make validate: OK`.

## The device (so it stays fixed)

- `scripts/fix_github_math.py` — a **code-span-aware converter** that shares
  `check_github_math.py`'s tokenizer semantics (fenced code + inline code spans preserved
  verbatim; a backslash-escaped `\\[4pt]` matrix row-break is never matched; only balanced
  inline pairs convert; idempotent). Two passes: delimiter/operatorname conversion, then
  setext-shatter repair inside `$$` blocks. 25 calibration controls
  (`scripts/test_fix_github_math.py`), all passing.
- `scripts/check_github_math.py` — gains rule **`GH-SETEXT-SHATTER`** (error on FRONT/RESEARCH,
  info on frozen ARCHIVE) with fixture + 2 controls (15 total), closing the blind spot that
  let the `W_t` breakage ship. `make check-github-math[-strict]` unchanged; still not wired
  into `make validate`.

## Before → after (static scan, live tiers)

| | FRONT+RESEARCH errors | warnings | notes |
|---|---|---|---|
| Before | 136 errors | 7384 warnings | + 499 setext the old checker could not see |
| After | **0 errors** | **0 warnings** | live tree clean |

Remaining: **16 warnings + 153 info**, all in the **byte-frozen** `quiet_quitting .../originals/`
(legacy delimiters + setext). Excluded from the fix by design — see "freeze vs render" below.

## Flagged, NOT fixed (unconfirmed; held for an author/render decision)

1. **`$$` with no blank line before it (≈116–159 blocks, e.g. `define:` then `$$`).** GitHub's
   docs want a blank line; whether these actually fail to render is **unconfirmed** (the `W_t`
   block had a blank line and broke from setext, not this). 42 of them sit directly under a
   list marker, where inserting a blank line would corrupt the list. Not mass-edited on an
   unverified theory. **Needs a rendered-page check**; if confirmed broken, the safe fix is a
   blank line before the plain-prose cases only.
2. **`\tag{N}` (18, in the HIGGS dossiers).** MathJax 3 (GitHub's engine) generally **supports**
   `\tag`, and it carries equation-numbering meaning, so it is **not** removed. Flagged only so
   a rendered check can confirm the numbers appear.

## Freeze vs render (author decision)

The only broken math left outside the fix is in `research/quiet_quitting_manifesto_2026-09-16/
originals/` — byte-frozen historical versions of the author's own manifesto. Rewriting even
their rendering breaks the freeze. Held for the author: sweep them too (breaking byte-freeze),
or leave them as historical artifacts with a note.

## Reproduce

```
make check-github-math              # advisory survey (now 0 err / 0 warn on live tiers)
make check-github-math-strict       # FRONT/RESEARCH gate (passes)
python3 scripts/test_check_github_math.py   # 15 checker controls
python3 scripts/test_fix_github_math.py     # 25 fixer controls
python3 scripts/fix_github_math.py <paths>  # dry-run; add --apply to write
```

## Next (to close rendered status)

Hard-refresh the fixed pages on GitHub (cache lags a push by minutes) and confirm: (a) the
`W_t` block reads as one equation, (b) `research/README.md` Greek letters typeset, (c) the
`$$`-no-blank-line and `\tag` specimens. Those turn the remaining UNVERIFIED rows into
recorded observations.
