# TLICA GitHub-math calibration kit

This directory is **repository tooling, not a reader page.** It is deliberately
excluded from the public Wiki mirror (`scripts/build_wiki.py` mirrors only the
flat `docs/*.md` reader pages, not subdirectories), because its job is to keep
TLICA's mathematics rendering correctly *in the GitHub repository view* — which
is a different surface from the Wiki, and a different surface again from a PDF.

It is adapted from Leah's **SMPTeX** project
([femboy2112/SMPTeX](https://github.com/femboy2112/SMPTeX), *Society for Markdown
Parsing and TeXorcism*), vendored here so TLICA carries its own calibration
surface and source guard with no external dependency.

## What a passing check does and does not establish

Three channels answer **different questions**; the kit keeps them separate and
never lets one masquerade as another:

| Channel | Tool | Establishes | Does **not** establish |
| --- | --- | --- | --- |
| Source preflight | `scripts/math_guard.py` (SMPTeX), `scripts/check_github_math.py` (TLICA) | Delimiter / brace / environment / macro-policy source validity | That any formula visually renders |
| Live test card | [`GITHUB_MATH_TEST_CARD.md`](GITHUB_MATH_TEST_CARD.md) | What GitHub actually displays on the viewed surface | Mathematical correctness of the expression |
| Semantic review | [`RENDER_REVIEW_CHECKLIST.md`](RENDER_REVIEW_CHECKLIST.md) | Whether the rendered math says what the author meant | Portability to other surfaces |

**A passing source guard is not a render certificate, and a passing PDF build is
no evidence at all about GitHub Markdown.** The rendered GitHub view stays
UNVERIFIED until a human opens it in a browser.

## Contents

- [`GITHUB_MATH_TEST_CARD.md`](GITHUB_MATH_TEST_CARD.md) — the T00–T21 calibration strips. Open in GitHub's **rendered** view, not Raw, and compare.
- [`probes/OPERATORNAME_AB.md`](probes/OPERATORNAME_AB.md) — the live `\mathrm` vs `\operatorname` A/B probe (renders both; exempt from the strict macro gate on purpose).
- [`MATH_COMPATIBILITY_LEDGER.md`](MATH_COMPATIBILITY_LEDGER.md) — recorded render observations with exact URL, SHA, date, and surface.
- [`RENDER_REVIEW_CHECKLIST.md`](RENDER_REVIEW_CHECKLIST.md) — the per-edit review procedure.
- [`MOBILE_APP_FALLBACK.md`](MOBILE_APP_FALLBACK.md) — PNG images of the 22 calibration strips, for GitHub's Android app (which renders no live MathJax).
- [`MOBILE_APP_FALLBACK_TLICA.md`](MOBILE_APP_FALLBACK_TLICA.md) — PNG images of TLICA's **load-bearing equations**, projected from the real source files so an Android-app reader sees the actual theory, not just calibration strips.
- [`GITHUB_MOBILE_UPSTREAM_REPORT.md`](GITHUB_MOBILE_UPSTREAM_REPORT.md) — the upstream app-rendering issue, for reference.

## The portable authoring contract

The rules every math-bearing edit must follow are in the repository-root
[`AGENTS_MATH_PROTOCOL.md`](../../AGENTS_MATH_PROTOCOL.md), referenced from
[`AGENTS.md`](../../AGENTS.md) and [`CLAUDE.md`](../../CLAUDE.md).

## Make targets

```bash
make check-math-portable     # SMPTeX source guard (strict-portable) + its unit/mutation tests
make check-github-math       # TLICA advisory survey (tiered, setext-shatter aware)
make check-github-math-strict # TLICA blocking gate (part of `make validate`)
make mobile-fallback         # rebuild the calibration + TLICA PNG fallbacks (needs Node + CairoSVG + Pillow)
```

## The mobile-app fallback, and why it is not a repo-wide image mirror

GitHub's Android app renders no live MathJax, so an app reader sees raw `$…$`
source. The fix is pre-rendered images — but imaging *every* document would
double the repository, destroy copy-paste and accessibility on every other
surface, and rot the instant an equation changed. So the fallback is deliberately
**narrow and generated**:

- Only two pages carry images: the **calibration strips** and TLICA's **~dozen
  load-bearing equations**. The 100+ research dossiers stay native-`$$` (they
  render on desktop and mobile *web*; an app reader who digs that deep is pointed
  to a browser).
- Each image is **generated from a single authoritative source** and recorded in
  a manifest with a **SHA-256 of that source TeX**, so the picture cannot silently
  drift from the equation it depicts — `make mobile-fallback` (or its stdlib-only
  check) fails loudly when the source changes.

That is the whole anti-dedup discipline: project the few equations that matter,
from one source of truth, with drift detection — never a parallel copy of the tree.
