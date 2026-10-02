# Host-Mediated Support Without Direct Interaction

## Cospans, slice-Yoneda comparison, and the distinction between support, presence, access, and coupling

**Date:** 2026-10-01  
**Status:** research-tier formal clarification. The cospan/slice constructions are standard category theory. The TLICA/physical interpretation is a research synthesis. **Foundation untouched.**

---

# 1. Originating claim

Suppose:

\[
A,B
\]

are realized inside a common host:

\[
U.
\]

Assume \(A\) and \(B\) cannot directly interact.

Then it can still be meaningful to say:

> the host-space around \(A\) supports \(B\)-type structure, even if \(A\) is blind to the actual \(B\).

The key is that:

\[
\boxed{
\text{absence of }A\to B
\text{ does not imply absence of a host-mediated relation}.
}
\]

---

# 2. The host relation is a cospan

Let:

\[
i_A:A\to U,
\qquad
i_B:B\to U.
\]

Then:

\[
\boxed{
A\xrightarrow{i_A}U\xleftarrow{i_B}B
}
\]

is a cospan.

A cospan does **not** assert direct interaction.

It asserts:

> both objects are realized/referred into one ambient host.

This is the exact categorical form of:

> “to talk about \(B\) relative to \(A\), go through \(U\) first.”

Standard prior art:
- cospans are diagrams \(A\to U\leftarrow B\);
- cospans compose by pushout when the relevant colimits exist.

---

# 3. Host-relative objects live in the slice

Fix \(U\).

The slice category:

\[
\mathcal C/U
\]

has objects:

\[
X\to U.
\]

Thus:

\[
A_U:=(A\xrightarrow{i_A}U)
\]

and:

\[
B_U:=(B\xrightarrow{i_B}U)
\]

are both objects of one common category.

Even if:

\[
\operatorname{Hom}_{\mathcal C}(A,B)
=
\varnothing,
\]

and even if:

\[
\operatorname{Hom}_{\mathcal C/U}(A_U,B_U)
=
\varnothing,
\]

they are still **comparable relative to the same host** because they inhabit:

\[
\boxed{
\mathcal C/U.
}
\]

This is a stronger and cleaner statement than inventing a fake direct arrow.

---

# 4. Slice-Yoneda comparison

Apply Yoneda inside the host slice:

\[
y_U:
\mathcal C/U
\to
[(\mathcal C/U)^{op},\mathbf{Set}].
\]

Then:

\[
y_U(A_U)
=
\operatorname{Hom}_{\mathcal C/U}(-,A_U),
\]

\[
y_U(B_U)
=
\operatorname{Hom}_{\mathcal C/U}(-,B_U).
\]

These are the complete host-relative relational profiles of \(A\) and \(B\).

They can be compared using the **same host-relative probe universe** even when \(A\) itself has no direct probe reaching \(B\).

Therefore:

\[
\boxed{
\text{A-blindness to B}
\not\Rightarrow
\text{U-blindness to B}.
}
\]

This is exactly the distinction the existing Full-Yoneda program needed.

---

# 5. Four notions that must be separated

## 5.1 Host support

There exist lawful host embeddings/realizations:

\[
A\to U,
\qquad
B\to U.
\]

Then \(U\) supports both.

## 5.2 Local/type support near \(A\)

Let:

\[
V_A\subseteq U
\]

be a local region around \(A\).

Say \(V_A\) **supports the B-type** when the local theory/fiber over \(V_A\) admits a lawful object/process of the same declared structural type as \(B\).

This means:

> a B-like realization is admissible there.

It does **not** mean actual \(B\) is present there.

## 5.3 Accessibility

\(A\) has a direct observational/probe channel to \(B\) only if the declared observation category contains a route that reaches/distinguishes \(B\).

Accessibility can fail while host support remains true.

## 5.4 Interaction/coupling

There is actual dynamical influence/coupling between \(A\) and \(B\).

This is stronger than mere common-host support.

Thus:

\[
\boxed{
\text{support}
\neq
\text{instantiation}
\neq
\text{accessibility}
\neq
\text{interaction}.
}
\]

---

# 6. “The space around A supports B” — precise version

The raw phrase is ambiguous.

The strongest defensible version is:

> The local host theory around \(A\) admits B-type structure under the same host laws, even though the actual realized \(B\) lies outside \(A\)'s direct accessible/interacting region.

Symbolically, if:

\[
\mathcal F:
\mathsf{Reg}
\to
\mathbf{Cat}
\]

assigns a category of lawful local structures to each region, then for \(V_A\):

\[
\mathcal F(V_A)
\]

contains an object:

\[
\widetilde B_A
\]

of the same declared type/class as the corresponding local form of \(B\).

This is **counterfactual/type support**.

It is weaker than actual local presence.

---

# 7. Local covariance supplies a physical analogue

Locally covariant QFT assigns physical observable structure functorially to spacetime regions/spacetimes.

The same theory can therefore support the same field species/type in different local regions while the actual excitation/state content differs.

Likewise, spacelike-separated systems may be operationally independent while both local algebras sit inside one larger theory/global algebra.

Primary prior art:
- Brunetti–Fredenhagen–Verch, locally covariant QFT;
- Brunetti et al., locality/tensor-product structure for spacelike separated systems.

This is an analogy/benchmark, not a derivation of the TLICA principle.

---

# 8. Common host does not create a direct causal arrow

From:

\[
A\to U\leftarrow B
\]

do **not** infer:

\[
A\to B
\]

or:

\[
B\to A.
\]

The cospan witnesses common support, not causal transmission.

This firewall matters especially in quantum/nonlocal discussion.

A common host category can relate two systems structurally while relativistic/local causal rules still forbid direct influence.

---

# 9. Host-mediated comparison via third probes

A third host-relative object:

\[
P\to U
\]

may probe both:

\[
P\to A
\]

and:

\[
P\to B
\]

inside:

\[
\mathcal C/U.
\]

So \(A\) and \(B\) may be jointly comparable by **external/common probes** even when neither has a direct arrow to the other.

This gives the relational shape:

\[
\boxed{
A
\leftarrow
P
\rightarrow
B
}
\]

inside the host slice.

This span is distinct from the support cospan:

\[
A\to U\leftarrow B.
\]

The cospan says “same host.”

The span says “same probe/relation witness.”

---

# 10. Pullback overlap

Given:

\[
A\to U\leftarrow B,
\]

if the pullback exists:

\[
A\times_U B,
\]

it measures the part where the two host realizations overlap in the categorical sense.

If:

\[
A\times_U B
\]

is initial/empty, the systems can still share the same host while having no overlap.

Thus:

\[
\boxed{
\text{common host}
\not\Rightarrow
\text{shared local content}.
}
\]

---

# 11. Host-mediated relation object

A useful schematic object is:

\[
\boxed{
\operatorname{Rel}_U(A,B)
}
\]

defined not as a direct hom-set but as the data of:

1. the cospan:
   \[
   A\to U\leftarrow B;
   \]
2. host-relative probe profiles:
   \[
   y_U(A_U),y_U(B_U);
   \]
3. any common probe spans:
   \[
   A\leftarrow P\rightarrow B;
   \]
4. overlap/pullback data;
5. causal/interaction constraints.

So:

\[
\boxed{
\operatorname{Rel}_U(A,B)
\neq
\operatorname{Hom}(A,B).
}
\]

This is likely the right object for non-directly-interacting systems.

---

# 12. A-blindness as restricted probe failure

Let:

\[
\mathcal P_A
\]

be the probes available to \(A\).

Then \(A\)-blindness to \(B\) means:

\[
N_{\mathcal P_A}(B)
\]

contains no discriminator available to \(A\), or \(B\)'s relevant alternatives collapse under that restricted nerve.

But the host may have a richer probe category:

\[
\mathcal P_A
\subset
\mathcal P_U.
\]

Then:

\[
N_{\mathcal P_A}(B_1)
\cong
N_{\mathcal P_A}(B_2)
\]

while:

\[
N_{\mathcal P_U}(B_1)
\not\cong
N_{\mathcal P_U}(B_2).
\]

So:

\[
\boxed{
\text{blind locally}
\quad\text{but}\quad
\text{distinguishable globally}.
}
\]

This is a direct reuse of the existing restricted/full Yoneda distinction.

---

# 13. Connection to the nested-host program

Suppose:

\[
U_0
\to
U_1
\to
U_2
\]

is a hierarchy of host contexts.

A and B may lack direct relation in \(U_0\) yet become jointly representable/comparable in \(U_1\).

Thus:

\[
\boxed{
\text{host ascent}
}
\]

can create comparison structure without creating a direct lower-level causal arrow.

This is the exact formal repair to:

> “If A can't see B, B is irrelevant to A.”

No.

B can be **host-relevant without being locally accessible**.

---

# 14. Connection to the empirical-QM reflection program

Suppose \(A\) is one local quantum subsystem and \(B\) another.

They need not directly interact.

But both are modeled inside one global quantum host:

\[
U.
\]

Then the global operator/tensor structure can carry relations involving both even if the local algebra available to \(A\) contains no direct operation revealing \(B\).

This is precisely why the host-reflection direction is useful:

\[
\boxed{
\text{global host structure}
\to
\text{relative local shadows}.
}
\]

Not every global relation is locally observable.

---

# 15. Strongest current principle

### Host-Mediated Support Principle

If \(A\) and \(B\) are lawful realizations inside the same host \(U\), then their relative structural comparison should be performed in a host-relative category such as:

\[
\mathcal C/U
\]

or a cospan/bicategorical construction over \(U\), even when no direct morphism:

\[
A\to B
\]

exists.

### Local Support Corollary

A local region around \(A\) can support the **type/lawfulness** of \(B\) without containing or accessing the actual \(B\).

This separates:
- what the host laws admit;
- what is instantiated;
- what \(A\) can observe;
- what can causally interact.

---

# 16. Current conclusion

The mathematically correct translation of the author's statement is:

\[
\boxed{
A\not\to B
\quad\text{does not imply}\quad
A\text{ and }B\text{ are categorically unrelated}.
}
\]

If:

\[
A\to U\leftarrow B,
\]

then \(U\) provides a common comparison context.

The right move is:

\[
\boxed{
\text{direct hom}
\to
\text{host-relative cospan/slice relation}.
}
\]

That is another concrete place where “go through the higher system first” is not metaphorical; it has standard categorical form.
