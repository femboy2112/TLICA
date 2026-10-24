# SMPTeX · GitHub Rendering Compatibility Ledger

[← README](README.md) · [Live test card](GITHUB_MATH_TEST_CARD.md) · [A/B probe](probes/OPERATORNAME_AB.md) · [Review checklist](RENDER_REVIEW_CHECKLIST.md)

## Calibrated layers

| Claim | Status | Evidence | Limit |
| --- | --- | --- | --- |
| GitHub documents `$...$`, `$`backtick delimiters, `$$...$$`, and fenced `math` | DOCUMENTED | [GitHub Math Docs](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) | Documentation is not a specific live test |
| GitHub Markdown math uses MathJax | DOCUMENTED | GitHub Math Docs | Package/configuration details may vary |
| Upstream MathJax documents `\operatorname` | DOCUMENTED UPSTREAM | [MathJax macro list](https://docs.mathjax.org/en/stable/input/tex/macros/) | Not live GitHub visual evidence |
| SMPTeX guard catches specified syntax failures | SOURCE-CHECKED LOCALLY | `scripts/test_math_guard.py` (vendored into TLICA); reproducible commands in README | Not a complete parser |
| T00–T21 on GitHub repository Markdown | **PASS — USER-REPORTED VISUAL OBSERVATION (22/22 phone; 22/22 PC)** | User report dated 2026-10-23 EDT; [test card](GITHUB_MATH_TEST_CARD.md) | Exact viewed SHA, browser versions and screenshots not provided; not independently re-observed by assistant |
| GitHub Android-app view of T00–T21 card | **PRESENTATION CONCERN — USER REPORT + SCREENSHOT** | User-supplied long Android app screenshot, 2026-10-23 EDT | Capture is only 72 px wide after attachment processing; no per-strip render failures or root cause demonstrated; app version/commit unknown |
| P00–P05 A/B on mobile repository Markdown | **VISUALLY OBSERVED**: P00/P02/P04 PASS, P01/P03/P05 FAIL | Screenshot supplied Oct 23 2026 EDT; [probe](probes/OPERATORNAME_AB.md) | Client and viewed SHA not visible; wiki/PR/desktop unverified |
| Static PNG image fallback on GitHub Android | **UNVERIFIED ON DEVICE — GENERATED REFERENCE** | [Mobile fallback](MOBILE_APP_FALLBACK.md); built from T00–T21 with source and PNG digests | Math in PNG images can display even when the Markdown TeX parser is absent; PNG display is never a native math-render pass |
| Mathematical semantics of outside research correct | NOT TESTED BY SMPTeX | Requires independent mathematical analysis | Correct appearance does not prove correctness |

## Evidence records

| Date / timezone | ID(s) | GitHub surface | Reference file / provenance | Source preflight | Actual browser observation | Verdict | Screenshot / repro |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 2026-10-23 EDT; time not supplied | T00–T21 | GitHub repo Markdown — phone browser | [Reference source at main@3f1d20d](https://github.com/femboy2112/SMPTeX/blob/3f1d20d5624f0fe32ff60e1016f0039f2aef430f/docs/GITHUB_MATH_TEST_CARD.md); viewed SHA unverified | Existing source preflight | User reports all 22 rendered perfectly | **22/22 PASS · USER-REPORTED** | ChatGPT report; no card screenshot/browser version |
| 2026-10-23 EDT; time not supplied | T00–T21 | GitHub repo Markdown — PC browser | [Reference source at main@3f1d20d](https://github.com/femboy2112/SMPTeX/blob/3f1d20d5624f0fe32ff60e1016f0039f2aef430f/docs/GITHUB_MATH_TEST_CARD.md); viewed SHA unverified | Existing source preflight | User reports all 22 rendered perfectly | **22/22 PASS · USER-REPORTED** | ChatGPT report; no card screenshot/browser version |
| 2026-10-23 EDT; time not supplied | T00–T21 page | GitHub Android app (not phone browser) | [Reference source at main@0ac5091](https://github.com/femboy2112/SMPTeX/blob/0ac509184bba5f95cdfab749f8536712ac285ccd/docs/GITHUB_MATH_TEST_CARD.md); viewed SHA unverified | Same repository math source; no app-targeted static check | User reports bad app presentation; supplied long screenshot is cramped / difficult to inspect | **APP UX CONCERN · USER-REPORTED; STRIP FAILURES UNVERIFIED** | User screenshot in conversation; app version unknown; capture/attachment downscaling may affect readability |
| 2026-10-24 UTC (Oct 23 EDT) | P00/P02/P04 | Mobile repository Markdown | [Reference fixture at main@da7c846](https://github.com/femboy2112/SMPTeX/blob/da7c8463fce31548414ba476c843722daf81bb7e/docs/probes/OPERATORNAME_AB.md); viewed SHA not shown | Non-strict source check | Upright `rank(A)=2` rendered in all three contexts | **PASS · OBSERVED** | User screenshot provided in conversation; exact client unverified |
| 2026-10-24 UTC (Oct 23 EDT) | P01/P03/P05 | Mobile repository Markdown | [Reference fixture at main@da7c846](https://github.com/femboy2112/SMPTeX/blob/da7c8463fce31548414ba476c843722daf81bb7e/docs/probes/OPERATORNAME_AB.md); viewed SHA not shown | Non-strict source check | `The following macros are not allowed: operatorname` appears in all three contexts | **FAIL · OBSERVED** | Same-page positive controls pass |

## Observed counterexample · O-2026-10-23-MOBILE-OPERATORNAME

- **Raw observation:** screenshot supplied in conversation shows all six probes in one mobile GitHub-rendered Markdown view: three `\mathrm` controls correctly display upright mathematics, while the three `\operatorname` challenges fail with an explicit forbidden-macro error.
- **Discrimination:** each same-context A/B pair changes the macro while leaving the expression structure fixed; passing controls reject the rival explanation that GitHub math is globally broken on that view.
- **Provenance boundary:** screenshot does not contain full URL, viewed commit, or exact client. Its text matches the reference fixture at `main@da7c846`, but screenshot-to-commit binding remains **UNVERIFIED**. Date is the user-submission date (not embedded on the screen).
- **Independent historical precedent:** [github/markup #1688](https://github.com/github/markup/issues/1688) reports the same message from 2023. It does not establish behavior for all current GitHub surfaces.
- **Portable policy:** avoid `\operatorname` in ordinary GitHub-targeted Markdown; use tested `\mathrm` for simple upright words. Operator spacing and limits are different; review any rewrite for mathematical meaning.
- **Outstanding:** test wiki, Issue/PR comments, desktop operator A/B behavior and other macros. T00–T21 have now been user-reported passing in phone and PC browsers; capture exact client and immutable URL in a follow-up run.
- **Evidence storage:** original screenshot remains in the user conversation and is not publicly hosted in this repo; a redacted screenshot attachment would strengthen independent reproducibility.

## Test-card observation · O-2026-10-23-CARD-PHONE-PC

- **Raw report:** user stated: 'the 22 card renders perfectly on github from my webbrowser on both phone and pc'.
- **Scope:** all T00–T21 test strips in SMPTeX GitHub repository Markdown; **22/22 visually PASS on phone** and **22/22 visually PASS on PC**, according to the same user's report.
- **Provenance:** submitted on 2026-10-23 (America/New_York). The exact viewed commit SHA, browser names/versions, and screenshots of the test card were not supplied. The source link above is a reference fixture, not a verified identification of the viewed revision.
- **Independence boundary:** phone and PC are two viewing environments but may use the same underlying GitHub MathJax renderer. They are not independent implementations.
- **Claim boundary:** a visually successful reference card does not prove semantic correctness, untested macro support or wiki/PR/Issue rendering. The separate mobile `\operatorname` A/B challenge remains a documented FAIL.

## GitHub Android app observation · O-2026-10-23-ANDROID-APP

- **Raw input:** user supplied a scrolling screenshot described as coming from the **GitHub Android app** and explicitly reported the experience as poor. The supplied image is extremely narrow and compressed at 72 × 1536 pixels, which makes the presentation difficult to audit.
- **Distinguishing control:** the same T00–T21 test card was **user-reported 22/22 visually PASS** in both phone and PC **web browsers**. The native Android app and the phone browser are **different rendering/presentation surfaces**.
- **Unresolved mechanism:** the screenshot alone does not isolate an app MathJax bug, viewport/layout CSS failure, long-screenshot stitching, or upload/image downsampling. No individual strip should be marked as a failed TeX render on this evidence.
- **Policy:** **do not use the GitHub Android app as the visual certification reference for SMPTeX**; use the rendered page in a real web browser. Keep app behavior separately marked as an **uncertified / presentation-degraded user report**.
- **Provenance:** screenshot supplied in conversation (not uploaded into this public repository); exact viewed commit, app build number, and screenshot capture parameters are unavailable.

## How to change a verdict

1. Open the exact **GitHub-rendered** page at an immutable commit. Log SHA, URL, UTC date, and browser.
2. Compare actual rendered output to expected output for each strip. Note whether a *control* passed before interpreting a challenge failure.
3. Preserve screenshots or a reproducible description. Prefer a minimal passing control and a minimal failing case in the **same** Markdown context.
4. Distinguish SOURCE-CHECKED, VISUALLY OBSERVED, SEMANTICALLY REVIEWED. Use **UNVERIFIED** for a stage that did not run and **AMBIGUOUS** for an observed failure whose mechanism cannot be identified.
5. For wiki/PR/issue rendering, run a new check **on that surface** rather than transferring a repo-page result as proof.

**Important:** a GitHub Markdown API result is not necessarily a complete MathJax browser render. Wiki files live in a separate Git repository and require their own audit.

## TLICA archive integration · 2026-10-23

SMPTeX was vendored into the TLICA archive (`docs/github-math/`, `scripts/math_guard.py`,
`scripts/render_mathjax_svg.cjs`, `scripts/mobile_fallback.py`, agent contract) and a
repo-wide scan was run. Findings specific to this integration:

| Claim | Status | Evidence | Limit |
| --- | --- | --- | --- |
| Single-line `$$ … $$` block math renders on GitHub | **DOCUMENTED — SUPPORTED** | GitHub's own math docs put the whole `$$\left(\sum…\right)$$` on one line (WebFetch 2026-10-23) | Not independently re-observed by browser; the guard's `DISPLAY_DELIMITER` is treated as a portability preference, not a TLICA error |
| TLICA live tree, portable source gate | **SOURCE-CHECKED CLEAN** | `make check-math-portable`: 0 real findings over 464 files after fixes | Source-checked only; rendered GitHub view UNVERIFIED |
| TLICA core-equation PNG fallback (E01–E10) | **GENERATED; ONE SPOT-CHECKED BY ASSISTANT** | `assets/mobile-tlica/`, projected from `foundation/3,5` and SHA-pinned; E07 (driven orbit) rendered image inspected and correct | Full 10-image set and all 22 calibration strips UNVERIFIED on an actual Android device |

**Repo-wide scan outcome (2026-10-23).** After excluding the fixtures tree and this
calibration kit, and routing the byte-frozen archive and the author-paused/DOI-frozen
dossiers to advisory, the live tree had 17 real portable findings. Twelve were fixed:
six `TABLE_PIPE` collisions (bra-ket and absolute-value bars inside table-cell math →
`\lvert…\rvert`, `\lVert…\rVert`), four genuine display-delimiter bugs in
`research/tlica_epic_path_geometry_2026-10-03/FOUNDATION_EXTENSION_GATE.md` (lone `$`
on its own line used as a display delimiter → `$$`), and two unpaired currency `$` in
the live one-ring ledgers (→ `\$`). Five unpaired currency `$` in preservation /
author-paused dossiers were left unchanged (a lone `$` renders as a literal on GitHub;
editing preserved or paused work to satisfy a linter is out of scope) and are advisory.

**Not touched.** The frozen foundation (`foundation/0..5_*.md`) was read for equation
projection but not edited; its 130 single-line `$$` display blocks are the
GitHub-documented form and were deliberately left as-is.
