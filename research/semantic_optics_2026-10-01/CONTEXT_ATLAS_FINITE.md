# Finite Context Atlas

## Three nested contexts with adjoint transport

**Date:** 2026-10-01  
**Status:** finite construction-level witness for [CONTEXT_TRANSPORT_2_ARCHITECTURE.md](CONTEXT_TRANSPORT_2_ARCHITECTURE.md).

**Executable:** [context_atlas_demo.py](context_atlas_demo.py)  
**Results:** [context_atlas_demo_results.json](context_atlas_demo_results.json)

---

# 1. Contexts

Use three finite chain categories:

\[
\mathcal C_0=\{0<1\},
\]

\[
\mathcal C_1=\{0<1<2\},
\]

\[
\mathcal C_2=\{0<1<2<3\}.
\]

Forward transports embed the old context into a richer one:

\[
F_{01}:\mathcal C_0\to\mathcal C_1,
\]

\[
F_{12}:\mathcal C_1\to\mathcal C_2,
\]

with composite:

\[
F_{02}=F_{12}F_{01}.
\]

Each has a right adjoint:

\[
G_{10},G_{21},G_{20}.
\]

---

# 2. Exact result

The executable checks:

\[
\boxed{16/16\text{ checks pass}.}
\]

Across the three adjunctions it exhaustively checks:

\[
6+12+8=26
\]

hom-bijection cells.

Forward composition:

\[
F_{02}=F_{12}F_{01}.
\]

Backward composition:

\[
G_{20}=G_{10}G_{21}.
\]

So forward forms compose covariantly and backward forms compose in reverse order exactly as adjoints should.

---

# 3. Perfect old-structure transport

All three forward functors are full and faithful.

Therefore every canonical Yoneda comparison:

\[
y_{\mathcal C_i}(X)
\to
F_{ij}^\* y_{\mathcal C_j}(F_{ij}X)
\]

is an isomorphism.

Equivalently, every unit:

\[
\eta:
1\Rightarrow GF
\]

is an isomorphism.

So:

\[
\boxed{
\text{old relational structure transports perfectly upward}.
}
\]

---

# 4. But the contexts are not equivalent

None of the forward functors is essentially surjective.

Each richer context contains at least one object outside the forward image.

Correspondingly, the counit:

\[
\varepsilon:
FG\Rightarrow1
\]

is not an isomorphism on those target-only objects.

Thus:

\[
\boxed{
\text{zero Yoneda hom-defect}
\not\Rightarrow
\text{zero coverage defect}.
}
\]

This is a finite model of a host context that perfectly preserves the lower theory while containing genuinely additional structure.

---

# 5. Downward transport is lawful but lossy

The right adjoints:

\[
G_{10},G_{21},G_{20}
\]

are faithful but not full.

They collapse target distinctions when returning to the coarser source context.

So the atlas has the desired asymmetry:

\[
\boxed{
\text{upward embedding: lossless but incomplete coverage}
}
\]

\[
\boxed{
\text{downward return: lawful but lossy}.
}
\]

---

# 6. Triangle identities

All three adjunctions satisfy both triangle identities.

Therefore the forward/backward form pairs are coherent adjunctions, not arbitrary approximate inverse maps.

This matters because the context architecture requires composable, lawful form transport.

---

# 7. Interpretation

This finite atlas realizes a very specific Russian-doll pattern:

\[
\mathcal C_0
\hookrightarrow
\mathcal C_1
\hookrightarrow
\mathcal C_2.
\]

Everything expressible below is preserved upstairs.

But the host has additional distinctions.

Returning downward forgets some of them.

That is exactly the shape required for:

- host lamps;
- vertical resolution;
- zero Yoneda defect with nonzero coverage defect;
- forward/backward form adjunctions.

It is not evidence that physical reality has this exact poset structure.

It is a coherent executable witness of the categorical architecture.
