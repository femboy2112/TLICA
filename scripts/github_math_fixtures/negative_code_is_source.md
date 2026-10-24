# Negative control — math-looking SOURCE must NOT be flagged (N2)

Inside a fenced text block, none of this is math and nothing must fire:

```text
This must NOT render as mathematics:
$$ \operatorname{MaxFlow}_G(s,t) $$
\(x\) and \[y\] are literal here.
$\rho(x
```

Inline code is also source: `\operatorname{x}` and `\(y\)` and `$z` must not flag.
