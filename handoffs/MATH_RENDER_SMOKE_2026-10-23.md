# TLICA GitHub Math Smoke Specimen (plan-only)
**Status:** Rendering calibration page, NOT a source of mathematical theorems.
**Commit-aware review:** record the exact rendered URL and GitHub source SHA for every observation.
**Contract:** [GitHub math rendering contract](GITHUB_MATH_RENDERING_CONTRACT_2026-10-23.md)

This is a purpose-built visual control sheet. Review **how the following actually appears in GitHub's rendered Markdown view**, not the raw file or an offline PDF. Only the final section intentionally uses the author's suspected-broken macro.

## Positive P1 — basic inline mathematics

The integration profile uses $\rho_{m,t}(x)$, and a selected scalar map can be written $f(C)=C/(1+C)$ with $C\geq 0$.

## Positive P2 — plain display mathematics

$$
\phi_{m,t}(x)=1-n_{m,t}(x)\delta-\epsilon_{m,t}(x).
$$

$$
\rho_{m,t}(x)=\frac{C_{m,t}(x)}{1+C_{m,t}(x)}.
$$

## Positive P3 — upright named label without suspected operatorname

$$
C_G(s,t)=\mathrm{MaxFlow}_{G}(s,t).
$$

The intended label is upright `MaxFlow`; inspect operator spacing and font. This is a formatting test only.

## Positive P4 — vectors, sets, arrows, and subscripts

$$
\mathcal{F}_Q=\{h\in\mathcal{H}: q(h)=q(h_0)\ \forall q\in Q\},\qquad
W_t\longrightarrow S_t\longrightarrow I_t\longrightarrow W_{t+1}.
$$

## Positive P5 — fenced math, matrices, and a text label

```math
A=\begin{bmatrix}
1 & 0\\
0 & 1
\end{bmatrix},
\qquad \text{world item} \ne \text{internal content}.
```

## Positive P6 — alternate inline collision-safe form

A second inline radical example: $`\sqrt{3x-1}+(1+x)^2`$.

## Negative / null control N1 — escaped literal currency

A price is <span>$</span>100, while a mathematical ratio is $100/2$ in GitHub's documented example-style format. This paragraph is a parser smoke test, not a financial assertion.

## Negative / null control N2 — math-looking source should remain source

```text
This must NOT render as mathematics:
$$ \operatorname{MaxFlow}_G(s,t) $$
\(x\) and \[y\] are literal here.
```

## Suspect probe S1 — author's reported operatorname failure

**Compatibility probe only; do not copy this into active TLICA documentation without a verified result.**

$$
C_G(s,t)=\operatorname{MaxFlow}_{G}(s,t).
$$

**Compare visually against P3.** Record PASS / FAIL / AMBIGUOUS and whether a difference comes from macro support, delimiters, Markdown parsing, or MathJax initialization. A correct rendering of S1 here does not prove that the macro works in other embedded Markdown contexts. A failure here does not prove a universal MathJax limitation.

## Results (to be filled by executor, not guessed)

| Item | Expected | Actual on GitHub | Evidence |
|---|---|---|---|
| P1–P5 | Readable mathematical output | UNVERIFIED | Pending real rendered view |
| P6 | Inline radical renders, no literal backticks | UNVERIFIED | Pending real rendered view |
| N1 | Literal dollar not interpreted as math opener | UNVERIFIED | Pending real rendered view |
| N2 | Source stays source | UNVERIFIED | Pending real rendered view |
| S1 | Compare against P3; either result diagnostic | UNVERIFIED | Pending real rendered view |
