# P00–P05 · `\operatorname` Live A/B Probe

**OBSERVED (2026-10-23 EDT):** one user-provided screenshot of this GitHub mobile repository-Markdown page shows all three `\mathrm` controls passing and all three `\operatorname` challenges displaying **"The following macros are not allowed: operatorname"**. The screenshot does not expose the URL, exact commit viewed, or client. The challenges are intentionally preserved as live negative controls; [see provenance limits](../MATH_COMPATIBILITY_LEDGER.md).

[← Back to SMPTeX](../README.md) · [← Test card](../GITHUB_MATH_TEST_CARD.md) · [Record evidence](../MATH_COMPATIBILITY_LEDGER.md)

**Question:** does GitHub actually render the MathJax macro `\operatorname` in each of the supported Markdown math contexts?

**Do not infer the answer from source syntax alone.** Upstream MathJax documents the macro; GitHub's exact rendering environment is the subject of this probe. Below are **live mathematics**, not escaped code samples. The strict-portable profile blocks this macro based on the observed repository-Markdown failure; other GitHub surfaces remain unverified.

## P00 · Inline control: `\mathrm`

The control is $\mathrm{rank}(A)=2$.

**Expected:** upright 'rank' beside the mathematical symbol A.

## P01 · Inline challenge: `\operatorname`

The challenge is $\operatorname{rank}(A)=2$.

**Compare:** does it render as an upright operator with appropriate spacing, or produce raw TeX / an error?

## P02 · Display control: `\mathrm`

$$
\mathrm{rank}(A)=2
$$

## P03 · Display challenge: `\operatorname`

$$
\operatorname{rank}(A)=2
$$

## P04 · Math fence control

```math
\mathrm{rank}(A)=2
```

## P05 · Math fence challenge

```math
\operatorname{rank}(A)=2
```

## Inspection report

| Check | Visual status | Evidence |
| --- | --- | --- |
| P00 inline control | PASS · OBSERVED | Upright `rank(A)=2` rendered |
| P01 inline challenge | FAIL · OBSERVED | Explicit macro-not-allowed error |
| P02 display control | PASS · OBSERVED | Upright `rank(A)=2` rendered |
| P03 display challenge | FAIL · OBSERVED | Explicit macro-not-allowed error |
| P04 math-fence control | PASS · OBSERVED | Upright `rank(A)=2` rendered |
| P05 math-fence challenge | FAIL · OBSERVED | Explicit macro-not-allowed error |

Record date, GitHub URL, commit SHA, and whether you were looking at repository Markdown, a wiki, or a PR in the [compatibility ledger](../MATH_COMPATIBILITY_LEDGER.md). **Control failure means the challenge cannot isolate macro support**. These results are backed by a user-supplied screenshot, not a GitHub-hosted attachment; the screenshot itself cannot establish the exact viewed SHA or client. Future retests should record immutable URL and client details.
