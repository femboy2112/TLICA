# SMPTeX · Human render review

[← Back to SMPTeX](README.md) · [Test card](GITHUB_MATH_TEST_CARD.md) · [Operator probe](probes/OPERATORNAME_AB.md) · [Ledger](MATH_COMPATIBILITY_LEDGER.md)

Open the two pages in a browser on **GitHub's rendered file view**, not Raw or a locally generated preview. Check each line **only if visually observed**. All 22 reference-card checkboxes below are now checked based on the user's phone and PC visual review; these checks are not independently reproduced observations. Operator checks have separate screenshot evidence.

**Reference file:** [Test card](GITHUB_MATH_TEST_CARD.md); exact viewed commit **UNVERIFIED**  
**Review date:** 2026-10-23 EDT (exact time unknown)  
**Surface:** GitHub repository Markdown  
**Viewing contexts:** phone web browser and PC web browser (names/versions unknown)

## Test card · T00–T21

- [x] T00 · Inline equation — **PASS · USER-REPORTED** (phone + PC)
- [x] T01 · GitHub protected inline equation — **PASS · USER-REPORTED** (phone + PC)
- [x] T02 · Display-dollar equation — **PASS · USER-REPORTED** (phone + PC)
- [x] T03 · Fenced `math` block — **PASS · USER-REPORTED** (phone + PC)
- [x] T04 · Greek letters, indices and adornments — **PASS · USER-REPORTED** (phone + PC)
- [x] T05 · Blackboard, calligraphic and upright type — **PASS · USER-REPORTED** (phone + PC)
- [x] T06 · Aligned multiline math — **PASS · USER-REPORTED** (phone + PC)
- [x] T07 · Matrix and determinant — **PASS · USER-REPORTED** (phone + PC)
- [x] T08 · Piecewise function — **PASS · USER-REPORTED** (phone + PC)
- [x] T09 · Calculus operators — **PASS · USER-REPORTED** (phone + PC)
- [x] T10 · Categorical composition and arrows — **PASS · USER-REPORTED** (phone + PC)
- [x] T11 · Bra-ket and tensor notation — **PASS · USER-REPORTED** (phone + PC)
- [x] T12 · Euler product — **PASS · USER-REPORTED** (phone + PC)
- [x] T13 · Ring quotients — **PASS · USER-REPORTED** (phone + PC)
- [x] T14 · Quantifiers and set braces — **PASS · USER-REPORTED** (phone + PC)
- [x] T15 · Paired delimiters — **PASS · USER-REPORTED** (phone + PC)
- [x] T16 · `\mathrm` and `\text` — **PASS · USER-REPORTED** (phone + PC)
- [x] T17 · TLICA diagnostic vector — **PASS · USER-REPORTED** (phone + PC)
- [x] T18 · SUCC/FUCC kets — **PASS · USER-REPORTED** (phone + PC)
- [x] T19 · Currency dollar versus math delimiter — **PASS · USER-REPORTED** (phone + PC)
- [x] T20 · High-density aligned equation — **PASS · USER-REPORTED** (phone + PC)
- [x] T21 · Math inside Markdown table — **PASS · USER-REPORTED** (phone + PC)

## Operator macro probe · P00–P05

**User screenshot observed 2026-10-23 EDT on mobile repository Markdown.** Checked below means *inspected*, not passed. The screenshot lacks an immutable commit URL or client identifier; [ledger](MATH_COMPATIBILITY_LEDGER.md).

- [x] P00 · Inline `\mathrm` control — **PASS** (user screenshot)
- [x] P01 · Inline `\operatorname` challenge — **FAIL · macro not allowed** (user screenshot)
- [x] P02 · Display `\mathrm` control — **PASS** (user screenshot)
- [x] P03 · Display `\operatorname` challenge — **FAIL · macro not allowed** (user screenshot)
- [x] P04 · Math-fence `\mathrm` control — **PASS** (user screenshot)
- [x] P05 · Math-fence `\operatorname` challenge — **FAIL · macro not allowed** (user screenshot)

## Calibration verdict

**Status:** T00–T21 22/22 PASS on phone + PC (user report); P00/P02/P04 PASS and P01/P03/P05 FAIL (mobile screenshot)  
**Failed strip IDs:** none reported among T00–T21; intentional failures P01, P03, P05  
**Observed symptoms:** no test-card rendering errors reported; [operator error evidence](MATH_COMPATIBILITY_LEDGER.md) separately recorded  
**Semantic check:** not established by appearance alone  
**Follow-up discriminator:** exact viewed commit/client, wiki, Issue/PR rendering, desktop operator A/B

If a strip fails, file a [render regression](https://github.com/femboy2112/SMPTeX/issues/new?template=render-regression.md) and update the [ledger](MATH_COMPATIBILITY_LEDGER.md) with the precise evidence. A rendered symbol can still express incorrect mathematics; do not treat a pretty formula as a theorem certificate.
