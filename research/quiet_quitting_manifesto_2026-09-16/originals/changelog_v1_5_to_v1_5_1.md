# Changelog — v1.5 to v1.5.1

## Why this is a patch release

Final v1.5 already has a frozen textual identity: `ef4babaa0b90a1f8af29e22ff03efb0a973db578d19a53e24a1a41bf1d613dea`. Adding a new scope statement while continuing to call the result v1.5 would create an identity collision between two different manuscripts with the same version label. The clarification is therefore issued as v1.5.1.

This is a scope patch, not another substantive rewrite. It states explicitly that quiet quitting proper retains the defensible baseline of the job and therefore does not itself cover outright refusal of labor. It does not declare outright refusal unethical; it leaves that separate ethical question unsettled.

## Exact canonical changes

### 1. Version metadata

```diff
-version: "1.5"
+version: "1.5.1"
```

### 2. Opening preamble paragraph

The original first paragraph was expanded into this single paragraph:

> Quiet quitting should not be the first move. It should be the last honest boundary after good-faith repair has failed. **Quiet quitting proper is not outright refusal of labor:** it retains the defensible baseline of the job and withdraws only the unowned excess demanded above it. Whether and when outright refusal is ethical is a separate question this manifesto does not purport to settle.

No other canonical prose changed between final v1.5 and v1.5.1.

## Measured Markdown comparison

- v1.5: 841 lines, 10,352 words, 70,741 bytes; SHA-256 `ef4babaa0b90a1f8af29e22ff03efb0a973db578d19a53e24a1a41bf1d613dea`.
- v1.5.1: 841 lines, 10,396 words, 71,017 bytes; SHA-256 `d122cc72446a63b1cc8e4278aee222ffffaf0489ddfc8c5fa67159acd387f5ac`.
- A line-oriented diff reports two insertions and two deletions: the version metadata line and the expanded preamble line. The remaining 839 of 841 lines are exactly aligned and unchanged.

## PDF production adjustment

The LaTeX paragraph spacing was changed from:

```latex
\setlength{\parskip}{0.54em}
```

to:

```latex
\setlength{\parskip}{0.50em}
```

This production-only adjustment was made solely to keep the new opening from creating a sparse spill page. It changes no canonical wording. Both the final v1.5 PDF and the v1.5.1 PDF contain 26 physical letter-size pages; v1.5.1 retains that page count.

## TeX and PDF identities

- v1.5 TeX: 2,002 lines, 10,542 words, 80,580 bytes; SHA-256 `c05a870d9fd2419ae98acc3371afd4cb924bc6db7185129350e0af9ed61a3062`.
- v1.5.1 TeX: 2,006 lines, 10,586 words, 80,861 bytes; SHA-256 `62f0ff3dad4e5234cd4a6358f9550aa7fb8298449bfbc9e60b41f7de3714dc1f`.
- v1.5 PDF: 245,214 bytes, 26 physical pages; SHA-256 `9cd4b6605a114f56300900fa3b40822361aea1de3d4f6df0dc1c4afeb6a19248`.
- v1.5.1 PDF: 245,567 bytes, 26 physical pages; SHA-256 `7eb9a5770e0727c26fb5b658bf347ab1e05f42ba74476315866a0abc7fc9c981`.

## Release status

**NOT CLEARED.** v1.5.1 remains a publication candidate. Leah must personally review the complete Markdown and rendered PDF, independently verify factual claims and citations, approve the final positions and wording—including the new opening scope distinction—and explicitly authorize any publication or outreach.
