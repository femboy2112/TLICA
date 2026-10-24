# SMPTeX · GitHub Math Rendering Test Card

**Purpose:** a repeatable, repository-local calibration target for Codex, Claude, and other agents writing mathematics for GitHub Markdown. **Reference renderer:** GitHub's MathJax-backed Markdown UI. **Current verification state:** All **22/22 test strips** are **user-reported visually passing** in GitHub repository Markdown on both phone and PC browsers (2026-10-23 EDT). The viewed commit and browser versions were not supplied. Wiki, PR and Issue surfaces remain unverified; see the [ledger](MATH_COMPATIBILITY_LEDGER.md).

> **⚠️ GITHUB'S ANDROID APP IS TRASH AS A MATH CALIBRATION REFERENCE.** The phone **web browser** and PC **web browser** passed T00–T21 (22/22 each, user report); an Android GitHub-app screenshot instead shows an extremely cramped, difficult-to-assess presentation. **Inspect in a browser.** The app observation is not an itemized TeX-parser failure, and long-screenshot scaling may contribute. [Surface ledger](MATH_COMPATIBILITY_LEDGER.md).

**Native Android app escape hatch:** [22 pre-rendered PNG strips](MOBILE_APP_FALLBACK.md). This is a viewing workaround, **not evidence that the GitHub Android app supports LaTeX**.

**How to read this card:** each numbered strip is a distinct parsing/rendering challenge. The **display** immediately below each heading should appear as mathematical notation, **not** as raw TeX commands. Compare the live GitHub page with its source and the expected appearance. If something fails, record the strip ID, file URL, surface (repository Markdown, PR, or wiki), and commit in [the compatibility ledger](MATH_COMPATIBILITY_LEDGER.md).

---

## T00 · Synchronization · Plain inline math

A basic invariant: $x^2 + y^2 = z^2$.

**Expect:** italic variables, raised exponents, and readable spaces; no raw dollar signs.

## T01 · Inline protection · GitHub's backtick-dollar form

A punctuation-sensitive inline sample: $`\{x\in\mathbb{R}\mid x>0\}`$.

**Expect:** set braces, real-number symbol, membership, a separator, and an inequality within a single line.

## T02 · Primary display channel · Isolated dollar pairs

$$
\sum_{n=1}^{\infty} \frac{1}{n^2}=\frac{\pi^2}{6}
$$

**Expect:** centered display math with a summation, infinity, fractions, and pi.

## T03 · Alternative display channel · Math code fence

```math
\Gamma(z+1)=z\,\Gamma(z)
```

**Expect:** a displayed gamma-function recurrence, not a monospace code block.

## T04 · Control characters · Greek, indices, adornments

$$
\alpha_1 + \beta_{i,j} = \gamma^{(2)} + \widehat{\theta} + \overline{z}
$$

**Expect:** Greek characters, nested subscripts, superscripts, hats, and an overline.

## T05 · Mathematical alphabets · Black-board, calligraphic, upright

$$
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C},
\qquad \mathcal{C} \xrightarrow{F} \mathcal{D},
\qquad \mathrm{rank}(A)=2
$$

**Expect:** blackboard-bold number systems, calligraphic categories, a labeled arrow, and upright `rank`.

## T06 · Alignment · Multiple equalities

```math
\begin{aligned}
(a+b)^2 &= a^2 + 2ab+b^2, \\
(a-b)^2 &= a^2 - 2ab+b^2.
\end{aligned}
```

**Expect:** two lines, equal signs aligned, no visible alignment ampersands or TeX line-break commands.

## T07 · Matrix geometry · Brackets and rows

$$
A=\begin{pmatrix}
a&b\\
c&d
\end{pmatrix},
\qquad \det(A)=ad-bc
$$

**Expect:** a two-by-two matrix in parentheses and a determinant identity.

## T08 · Piecewise logic · Cases

```math
f(x)=\begin{cases}
x^2, & x\geq 0,\\
-x, & x<0.
\end{cases}
```

**Expect:** a tall left brace and two visually distinct cases.

## T09 · Analysis · Limits, integrals, derivatives

$$
\lim_{h\to 0}\frac{f(x+h)-f(x)}{h}=f'(x),
\qquad \int_0^1 x^2\,dx=\frac13
$$

**Expect:** a limit with a lower condition, an integral, and a differential with appropriate spacing.

## T10 · Category theory · Composition preservation

```math
F(g\circ f)=F(g)\circ F(f),
\qquad F(1_X)=1_{F(X)},
\qquad X\xrightarrow{f}Y\xrightarrow{g}Z
```

**Expect:** compositions, nested subscripts, and two arrows individually labeled by their morphisms.

## T11 · Physics / operators · Brackets, adjoints, tensor products

$$
\langle \psi\mid A^{\dagger}A\mid\psi\rangle\geq 0,
\qquad H=H_A\otimes I_B+I_A\otimes H_B
$$

**Expect:** Dirac bra-ket notation, dagger, tensor symbols, and subscripts.

## T12 · Number theory · Products, zeta and primes

```math
\zeta(s)=\prod_{p\ \mathrm{prime}}\frac{1}{1-p^{-s}},
\qquad \Re(s)>1
```

**Expect:** an Euler product with legible exponent and the upright word `prime`.

## T13 · Quotient structure · Ring comparison

$$
\mathbb{Z}/p^2\mathbb{Z}\not\cong \mathbb{F}_p[t]/(t^2)
$$

**Expect:** two well-formed quotient-ring expressions and a 'not isomorphic' symbol.

## T14 · Quantifiers, implications, sets

$$
\forall x\in X,\quad P(x)\Rightarrow Q(x),
\qquad \{x\in X\mid P(x)\}\subseteq X
$$

**Expect:** universal quantifier, implication, literal set braces, membership, and subset-or-equal.

## T15 · Larger fences · Paired delimiters

```math
\left\langle\frac{a+b}{c+d}\right\rangle
\neq
\left(\frac{a+b}{c+d}\right)
```

**Expect:** delimiters that size to the fractions and no raw `left`/`right` tokens.

## T16 · Typography · Upright text amid symbols

$$
\mathrm{Cl}(\mathcal{T})\subseteq\mathcal{U},
\qquad \text{provided that } \mathcal{T}\neq\varnothing
$$

**Expect:** upright `Cl`, upright words “provided that”, and calligraphic symbols.

## T17 · Project vocabulary · TLICA diagnostic vector

```math
(\kappa,\phi,\sigma,\rho,\mu),
\qquad \phi_{\mathcal{T}}(H_i,H_j)
```

**Expect:** five distinct Greek symbols and a subscripted two-argument function.

## T18 · Project vocabulary · SUCC and FUCC operators

$$
S\lvert n\rangle=\lvert n+1\rangle,
\qquad V_p\lvert n\rangle=\lvert pn\rangle
$$

**Expect:** two ket-valued operator equalities (not raw `lvert` or `rangle`).

## T19 · Currency interference · Literal dollar next to inline math

The literal price is <span>$</span>100. The numerical expression is $100/2=50$.

**Expect:** a normal currency symbol in the sentence and a separate correctly rendered equation.

## T20 · High-density signal · Multi-line equation

```math
\begin{aligned}
\|Tx\|^2
  &=\langle Tx,Tx\rangle\\
  &=\langle T^{\dagger}Tx,x\rangle\\
  &\leq\|T\|^2\,\|x\|^2.
\end{aligned}
```

**Expect:** aligned equals/inequality operators; norm bars, angle brackets, and superscripts intact.

## T21 · GitHub table interference · Avoid bare pipe characters

| Case | Mathematical relation | Explanation |
| --- | --- | --- |
| Divisibility | $a\mid b$ | The vertical relation should remain inside this cell |
| Conditional probability | $P(A\mid B)$ | The conditional separator should stay inside its cell |

**Expect:** three columns and both mathematical relations visible. A raw `|` inside table math is a Markdown separator risk; use TeX relation commands such as `\mid` or move complex math out of the table.

---

## Experimental channel · Operator macro discrimination

MathJax's published command list includes the AMS macro shown here, but the *target GitHub page* is the actual instrument. The operator challenge was **observed failing on GitHub mobile repository Markdown**, not necessarily on other GitHub surfaces. Test the following two candidates **side by side in the live GitHub renderer** using [the executable A/B probe](probes/OPERATORNAME_AB.md):

```text
Control:    $\mathrm{rank}(A)=2$
Challenge:  $\operatorname{rank}(A)=2$
```

If the control passes and the challenge fails on the same GitHub page, record the exact failure, URL and date. If both pass, change the repository policy only after inspecting other target surfaces. The `--strict-portable` guard conservatively rejects the challenge macro until that validation is complete.

## Deliberate negative controls · Leave these inside code fences

The linter must identify these *if an agent moves them into executable Markdown math*:

```text
Unclosed inline:  An equation $a+b.
Unclosed display: $$ [on a line by itself, with no matching closing line]
Unclosed group:   $\frac{1}{x$
Mismatched env:   \begin{aligned} ... \end{matrix}
Bare TeX:         The equation is \frac{1}{2}.
Nonportable:      $\newcommand{\foo}{x}$
```

**Calibration scope:** T00–T21 are visually confirmed by the user's report for GitHub repository Markdown on phone and PC. This does not certify future changes, other rendering surfaces, or mathematical semantics. Source linter success alone remains insufficient for a render claim.

Source documentation: [GitHub math syntax](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions) and [MathJax supported commands](https://docs.mathjax.org/en/stable/input/tex/macros/).
