# Negative control — a lone = inside $$ shatters the block (GH-SETEXT-SHATTER)

A multi-line display equation with the operator alone on its own line:

$$
W_t
=
(K_t,\; A_t)
$$

GitHub reads the `=` line as a setext underline, turns `W_t` into an H1 heading,
and orphans the `$$`. The fix is to merge the operator: `W_t =` on one line.

An aligned block using `&=` is NOT a setext underline and must stay clean:

$$
\begin{aligned}
a &= b \\
  &= c
\end{aligned}
$$
