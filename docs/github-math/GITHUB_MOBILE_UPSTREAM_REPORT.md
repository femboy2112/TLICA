# GitHub Mobile math-renderer parity · Upstream engineering report

[← SMPTeX](README.md) · [Live test card](GITHUB_MATH_TEST_CARD.md) · [Static image workaround](MOBILE_APP_FALLBACK.md)

> **Dear GitHub Mobile: it would be charming if the application hosted on GitHub could render the mathematics hosted on GitHub.** We brought 22 reference tests and passing web-browser controls. We would send a pull request to the official app, but its source code is not public.

## Public records and access

- [GitHub math documentation](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) documents MathJax for the **web interface**.
- [Community discussion #41372](https://github.com/orgs/community/discussions/41372) dates to December 2022. A GitHub representative said the problem was referred to an internal tracking issue.
- [Community discussion #195537](https://github.com/orgs/community/discussions/195537) reports missing mobile math on iPadOS in May 2026; separate platform, corroborating recurrence rather than proving our Android mechanism.
- [Community discussion #201242](https://github.com/orgs/community/discussions/201242) asks why official GitHub mobile source is unavailable; a commenter describes the mobile app as proprietary.

**Code access:** no public repository containing the official GitHub Android app's renderer was located. No change or test was performed against the official APK or its private source. Public projects such as OpenHub and third-party Markdown readers are not GitHub's official client.

## Reference reproduction

1. Open [SMPTeX's T00–T21 test card](GITHUB_MATH_TEST_CARD.md) as rendered repository Markdown in the native GitHub Android app; separately repeat with a phone browser at github.com and a PC browser.
2. Check T00 inline dollars, T02 display dollars, T03 fenced math, T07 matrix, and T21 math inside a Markdown table. Label each: rendered math / raw TeX / error message / clipped or unreadable / absent.
3. Record actual app version, OS, viewed commit SHA, native zoom/font size and device orientation. Preserve an **original-resolution** screenshot.
4. **Positive controls:** user reports **22/22 live math strips PASS** on phone and PC web browsers on October 23, 2026.
5. **Native Android observation:** user provided a long, extremely narrow screenshot and reported poor readability. The received file was only 72 × 1536 px. That does not distinguish absent math rendering from CSS/layout defects or screenshot/downsampling artifacts.

### Mechanisms not yet distinguished

- A: native Markdown AST lacks inline/display math rendering.
- B: math nodes are present but layout clips or scales them incorrectly.
- C: the long-screenshot capture/upload path destroyed legibility.
- D: more than one of the above.

**Next discriminating probe:** a full-width normal screenshot of T00/T02/T03 in the Android app, each beside the same source in the web browser. A successful native math output would refute A; raw dollar-delimited TeX with correct surrounding layout would support A; real math clipped by the viewport would support B.

## Proposed implementation boundary for a GitHub engineer

**Parser:** preserve TeX nodes from a GFM-compatible AST for inline dollars, protected dollar-backtick, display dollars and math fences. Exclude ordinary code blocks, code spans and escaped currency. Do not regex-replace arbitrary untrusted Markdown.

**Renderer:** feed the AST math nodes to a math-capable native component or a tightly sandboxed MathJax/KaTeX WebView. Never enable arbitrary user-supplied JavaScript; sanitize HTML/URLs and bound macro expansion.

**Layout:** correct inline baseline, display equations with horizontally scrollable overflow, tables that scroll independently, dynamic type, dark-mode parity, copyable original TeX and accessible math labels.

**Acceptance:** T00–T21 legible in the native app at standard and enlarged text sizes; code fences and currency remain literal, malformed/hostile inputs fail safely, and browser baselines remain passing. Separately test known web-incompatible operatorname against its working upright-font control.

## Patch actually possible without the proprietary code

The [22-strip PNG fallback](MOBILE_APP_FALLBACK.md) uses real MathJax SVG output rasterized into source-hash-verified images. This helps viewers inspect the reference even if their client lacks a TeX renderer. It **cannot fix GitHub Mobile itself**, nor does it count as a mobile math certification. In-app PNG behavior still needs a real device test.

> Four years and an internal tracking issue later, we have rendered the formulas into pictures for the application that displays source code. We look forward to reviewing the pull request when the repository becomes available.
