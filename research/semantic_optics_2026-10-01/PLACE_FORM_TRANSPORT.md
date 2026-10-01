# Place Form Transport

## Product formula, Tate factorization, and the finite/archimedean inverse relation

**Date:** 2026-10-01  
**Status:** standard number theory interpreted as a non-toy transport benchmark. No claim of mathematical novelty.

---

# 1. A genuine inverse-form equation already exists

For:

\[
x\in\mathbb Q^\times,
\]

the product formula is:

\[
|x|_\infty
\prod_{p<\infty}|x|_p
=
1.
\]

Therefore:

\[
\boxed{
\prod_{p<\infty}|x|_p
=
|x|_\infty^{-1}.
}
\]

This is strikingly close to the author's earlier form-transport intuition:

\[
\operatorname{form}_1(x)
=
\operatorname{form}^{-1}(y).
\]

But the types matter.

Define the finite-place profile:

\[
P_{\mathrm{fin}}(x)
=
(|x|_p)_p.
\]

Define aggregation:

\[
\Pi(P_{\mathrm{fin}}(x))
=
\prod_p|x|_p.
\]

Define the archimedean form:

\[
P_\infty(x)
=
|x|_\infty.
\]

Then:

\[
\boxed{
\Pi\circ P_{\mathrm{fin}}
=
(P_\infty)^{-1}
}
\]

on:

\[
\mathbb Q^\times.
\]

This is an exact compatibility law.

It is **not** an equivalence between the full finite-place and archimedean local categories.

---

# 2. Product formula as a coherence 2-cell candidate

The diagram:

\[
\mathbb Q^\times
\overset{P_{\mathrm{fin}}}{\longrightarrow}
\prod_p'\mathbb R_+
\]

and:

\[
\mathbb Q^\times
\overset{P_\infty}{\longrightarrow}
\mathbb R_+
\]

is coupled by:

\[
\Pi
\]

and inversion:

\[
\iota(r)=r^{-1}.
\]

Thus:

\[
\boxed{
\Pi\circ P_{\mathrm{fin}}
=
\iota\circ P_\infty.
}
\]

In the context-transport 2-architecture, this is naturally interpreted as a **coherence equation between two place-profile routes**.

That is a better use of the \(C\leftrightarrow D\) edge than claiming direct equivalence.

---

# 3. Principal idèles are globally constrained

The diagonal embedding:

\[
\Delta:
\mathbb Q^\times
\to
\mathbb A_{\mathbb Q}^\times
\]

sends a rational number into all local completions simultaneously.

The idelic norm is:

\[
|a|_{\mathbb A}
=
\prod_v|a_v|_v.
\]

The product formula says:

\[
\boxed{
|\Delta x|_{\mathbb A}=1.
}
\]

So principal idèles lie in the kernel of the global norm character.

This is the cleanest all-places compatibility constraint in the benchmark.

---

# 4. Ostrowski completeness of the place family

Up to equivalence, the nontrivial absolute values on:

\[
\mathbb Q
\]

are exactly:

- \(|\cdot|_p\) for primes \(p\);
- \(|\cdot|_\infty\).

Therefore:

\[
\boxed{
C_{\mathrm{fin}}+D_\infty
}
\]

really does exhaust the local completion types of \(\mathbb Q\).

This makes the author's finite/archimedean partition mathematically canonical for \(\mathbb Q\).

---

# 5. Tate's thesis categorically improves the square

The global Schwartz/Bruhat space on the adèles factors into local spaces.

The global zeta integral factors:

\[
Z(f,s)
=
\prod_v Z_v(f_v,s).
\]

For the Riemann-zeta test vector:

\[
Z_p(s)
=
(1-p^{-s})^{-1}
\]

at finite primes and:

\[
Z_\infty(s)
=
\pi^{-s/2}\Gamma(s/2)
\]

at infinity.

Thus:

\[
\boxed{
\Lambda(s)
=
Z_\infty(s)
\prod_p Z_p(s).
}
\]

This means the completed zeta function is literally an **all-places assembly**.

---

# 6. The functional equation is global, not finite-only

The completed function satisfies:

\[
\Lambda(s)=\Lambda(1-s).
\]

The archimedean gamma factor is necessary.

So analytic number theory itself warns us not to privilege the finite-prime side:

\[
\boxed{
\zeta(s)\text{ alone}
\neq
\text{the symmetric global object}.
}
\]

The symmetric global object is the completed zeta:

\[
\Lambda(s).
\]

This is precisely the role the author's \(D\) corner was trying to recover.

---

# 7. Finite witness

The included script tests:

1. exact product formula for five nonzero rationals;
2. exact inverse relation:
   \[
   \prod_p|x|_p=|x|_\infty^{-1};
   \]
3. finite support of nontrivial \(p\)-adic norms;
4. monotone convergence of truncated Euler products at \(s=2\);
5. numerical approximation:
   \[
   \prod_{p\le10000}(1-p^{-2})^{-1}
   \approx
   \zeta(2)
   \]
   within \(2\times10^{-5}\);
6. completed-zeta functional-equation checks at:
   \[
   s=2,\ -1;
   \]
7. and:
   \[
   s=4,\ -3;
   \]
8. associativity of the \(\mathbb N^\times\) real scaling action.

Result:

\[
\boxed{
8/8\text{ checks pass}.
}
\]

The numerical checks are demonstrations of standard identities, not new evidence for RH/TLICA.

---

# 8. Relationship to the Scaling Site

The Scaling Site uses the action:

\[
\mathbb N^\times
\curvearrowright
\mathbb R_+
\]

by multiplication.

So the exact same pair:

\[
(\mathbb N^\times,\mathbb R_+)
\]

appears:

- analytically in finite/archimedean scaling;
- geometrically in the Scaling Site's semidirect-product structure.

This is one of the strongest reasons the Arithmetic/Scaling Site belongs in the missing \(B\).

---

# 9. Relationship to Yoneda transport

The place benchmark is not itself a Yoneda theorem.

But it gives a real context atlas:

\[
\mathcal C_p
\]

for every finite prime and:

\[
\mathcal C_\infty.
\]

A future adelic category should assemble these fibers.

Then Yoneda asks:

> what complete probe profile does a local/global object have in each place-context, and what does the adelic assembly forget or add?

The product formula gives one nontrivial coherence condition that any such atlas must preserve.

---

# 10. Strongest benchmark equation

The square's first exact compatibility law is therefore not:

\[
C\cong D.
\]

It is:

\[
\boxed{
\Pi\circ P_{\mathrm{fin}}
=
\iota\circ P_\infty
\quad
\text{on }\mathbb Q^\times.
}
\]

This is the correct finite/archimedean **form transport constraint**.

That equation is strong enough to be useful and weak enough to be true.
