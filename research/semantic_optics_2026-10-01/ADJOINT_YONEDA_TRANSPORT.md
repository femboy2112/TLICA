# Adjoint–Yoneda Transport Theorem

## The backward form represents the transported probe profile

**Date:** 2026-10-01  
**Status:** standard/disclosed category theory specialized into the Semantic Optics transport program. TLICA interpretation remains **CONJECTURED / UNVERIFIED**.

---

# 1. Setup

Let:

\[
F:\mathcal A\to\mathcal B
\]

and:

\[
G:\mathcal B\to\mathcal A
\]

with:

\[
F\dashv G.
\]

Write the adjunction bijection:

\[
\Phi_{c,d}:
\mathcal B(Fc,d)
\overset{\sim}{\longrightarrow}
\mathcal A(c,Gd)
\]

natural in \(c,d\).

Let:

\[
y_{\mathcal A}:
\mathcal A\to
[\mathcal A^{op},\mathbf{Set}]
\]

and:

\[
y_{\mathcal B}:
\mathcal B\to
[\mathcal B^{op},\mathbf{Set}]
\]

be Yoneda embeddings.

---

# 2. Restricted target profile theorem

Precomposition with \(F\) gives:

\[
F^\*:
[\mathcal B^{op},\mathbf{Set}]
\to
[\mathcal A^{op},\mathbf{Set}].
\]

For any:

\[
d\in\mathcal B,
\]

we have:

\[
F^\*y_{\mathcal B}(d)
=
\mathcal B(F-,d).
\]

By the adjunction:

\[
\mathcal B(F-,d)
\cong
\mathcal A(-,Gd).
\]

Therefore:

\[
\boxed{
F^\*y_{\mathcal B}(d)
\cong
y_{\mathcal A}(Gd).
}
\]

This is natural in \(d\).

### Interpretation

The target object's complete Yoneda profile, when observed only through probes transported from \(\mathcal A\), is representable back in \(\mathcal A\) by:

\[
\boxed{
Gd.
}
\]

So the user's backward form has a precise candidate:

\[
\boxed{
\operatorname{form}_2(d)=Gd,
}
\]

not merely by analogy but by a universal representability property.

---

# 3. Forward form

The forward form is simply:

\[
\boxed{
\operatorname{form}_1(c)=Fc.
}
\]

Thus:

\[
c
\xrightarrow{F}
Fc
\]

moves the object into the target context.

The backward form:

\[
d
\xrightarrow{G}
Gd
\]

does not necessarily recover a literal inverse object.

Instead it gives the representing object for the target's \(F\)-restricted probe profile.

This distinction is the difference between:

\[
\text{adjunction}
\]

and:

\[
\text{equivalence}.
\]

---

# 4. Yoneda transport comparison

For:

\[
X\in\mathcal A,
\]

define the canonical comparison:

\[
\theta_{F,X}:
y_{\mathcal A}(X)
\Rightarrow
F^\*y_{\mathcal B}(FX).
\]

At:

\[
C\in\mathcal A,
\]

\[
\theta_{F,X,C}:
\mathcal A(C,X)
\to
\mathcal B(FC,FX)
\]

is:

\[
h\mapsto Fh.
\]

Using the theorem above:

\[
F^\*y_{\mathcal B}(FX)
\cong
y_{\mathcal A}(GFX).
\]

So \(\theta_{F,X}\) may be viewed as:

\[
y_{\mathcal A}(X)
\to
y_{\mathcal A}(GFX).
\]

---

# 5. Main theorem — Yoneda transport defect equals the unit defect

Let:

\[
\eta:
1_{\mathcal A}
\Rightarrow
GF
\]

be the adjunction unit.

Then under the natural isomorphism:

\[
F^\*y_{\mathcal B}(FX)
\cong
y_{\mathcal A}(GFX),
\]

the Yoneda comparison:

\[
\theta_{F,X}
\]

is exactly:

\[
\boxed{
y_{\mathcal A}(\eta_X).
}
\]

That is, the diagram commutes:

\[
\begin{array}{ccc}
y_{\mathcal A}(X)
&
\xrightarrow{\theta_{F,X}}
&
F^\*y_{\mathcal B}(FX)
\\
&
\searrow_{y(\eta_X)}
&
\downarrow^{\cong}
\\
&&
y_{\mathcal A}(GFX).
\end{array}
\]

### Proof

At a probe:

\[
C\in\mathcal A,
\]

take:

\[
h:C\to X.
\]

The Yoneda comparison sends:

\[
h
\mapsto
Fh:
FC\to FX.
\]

The adjunct of \(Fh\) is:

\[
G(Fh)\circ\eta_C.
\]

Naturality of \(\eta\) gives:

\[
G(Fh)\circ\eta_C
=
\eta_X\circ h.
\]

But:

\[
h
\mapsto
\eta_X\circ h
\]

is exactly the \(C\)-component of:

\[
y_{\mathcal A}(\eta_X).
\]

Therefore the two natural transformations agree.

\(\square\)

---

# 6. Corollary — full faithfulness is zero forward round-trip defect

Because Yoneda reflects isomorphisms:

\[
\theta_{F,X}
\text{ is an isomorphism}
\]

iff:

\[
\eta_X
\text{ is an isomorphism}.
\]

For every \(X\), this is equivalent to:

\[
F
\]

being full and faithful.

Thus:

\[
\boxed{
\Delta_{\mathrm{Yoneda}}(F)
=
\Delta_{\mathrm{unit}}(F\dashv G)
}
\]

in the structural sense that they are the same natural transformation under the adjunction representation.

This is not a numerical equality.

It is an identification of defect structure.

---

# 7. The backward round-trip and target recovery

The counit is:

\[
\varepsilon:
FG
\Rightarrow
1_{\mathcal B}.
\]

For:

\[
d\in\mathcal B,
\]

\[
\varepsilon_d:
FGd\to d.
\]

This answers:

> after representing \(d\)'s restricted profile by \(Gd\), does transporting that representation back to \(\mathcal B\) recover \(d\)?

If:

\[
\varepsilon_d
\]

is an isomorphism, then:

\[
d\cong FGd.
\]

If not, the restricted profile is representable back in \(\mathcal A\), but reconstruction into \(\mathcal B\) does not recover the whole target object.

---

# 8. Adjoint equivalence as zero two-sided transport defect

If:

\[
\eta
\]

and:

\[
\varepsilon
\]

are natural isomorphisms, then:

\[
F\dashv G
\]

is an adjoint equivalence.

Thus:

\[
\boxed{
GF\cong1_{\mathcal A},
\qquad
FG\cong1_{\mathcal B}.
}
\]

This is the context-level exact version of:

\[
y=f(x)
\iff
x=f^{-1}(y).
\]

So the two-sided defect object is naturally:

\[
\boxed{
(\eta,\varepsilon).
}
\]

Zero/invertible defect on both sides gives reversible context transport.

---

# 9. One-sided exactness is possible

A subtle but important case:

\[
\eta
\]

may be an isomorphism while:

\[
\varepsilon
\]

is not.

Then \(F\) is full and faithful.

Every source object and relation survives perfectly into the target.

But the target contains structure not recovered from the image of \(F\).

This is exactly the finite poset adjunction in:

[yoneda_transport_forms_demo.py](yoneda_transport_forms_demo.py).

So:

\[
\boxed{
\text{perfect Yoneda transport on old objects}
\not\Rightarrow
\text{context equivalence}.
}
\]

The remaining defect is target coverage/recovery.

---

# 10. Presheaf-level transport has its own adjoint forms

For a functor:

\[
F:\mathcal A\to\mathcal B,
\]

precomposition:

\[
F^\*:
\operatorname{PSh}(\mathcal B)
\to
\operatorname{PSh}(\mathcal A)
\]

often has both adjoints:

\[
\operatorname{Lan}_{F^{op}}
\dashv
F^\*
\dashv
\operatorname{Ran}_{F^{op}}.
\]

So there are canonical “push forward / pull back” forms at the Yoneda-profile level as well.

Moreover, left Kan extension transports representables as expected:

\[
\boxed{
\operatorname{Lan}_{F^{op}}(y_{\mathcal A}(c))
\cong
y_{\mathcal B}(Fc)
}
\]

under the usual smallness/cocompleteness hypotheses.

This means that **Yoneda profiles themselves admit lawful context transport**, not merely the represented objects.

Sources:
- Kan extension / precomposition adjunction:
  https://ncatlab.org/nlab/show/Kan+extension
- presheaf functoriality:
  https://ncatlab.org/nlab/show/functoriality+of+categories+of+presheaves

---

# 11. Semantic Optics interpretation

For context arrow:

\[
u:b\to b'
\]

with transport:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'},
\]

a right adjoint:

\[
G_u
\]

would have a powerful interpretation.

For any target-context object:

\[
d\in\mathcal C_{b'},
\]

\[
G_ud
\]

is the object in the source context representing all ways that source-context probes can interact with \(d\).

That is:

\[
\boxed{
\text{backward form}
=
\text{source-context representation of the target object's restricted Yoneda profile}.
}
\]

This may be the rigorous semantic meaning of “what does \(d\) look like from context \(b\)?”

---

# 12. Locality example

Suppose:

\[
F:
\mathcal C_U
\to
\mathcal C_V
\]

embeds a smaller/local context into a larger one.

If \(F\) has right adjoint \(G\), then for global/larger object \(d\):

\[
Gd
\]

represents exactly the \(U\)-accessible interaction profile:

\[
\mathcal C_V(F-,d).
\]

This is more precise than saying:

> “restrict \(d\) locally”

because it defines the local representative by a universal property.

When it coincides with ordinary restriction, excellent.

When it does not, the difference is mathematically informative.

---

# 13. Scale example

For coarse/fine contexts, an adjunction:

\[
F_{\mathrm{coarse}\to\mathrm{fine}}
\dashv
G_{\mathrm{fine}\to\mathrm{coarse}}
\]

would mean that coarse-to-fine interactions and fine-to-coarse representations are linked by a natural hom-form equivalence.

The unit/counit then measure:

- whether coarse structures embed faithfully upstairs;
- whether fine structures are fully reconstructible downstairs.

This is almost exactly the branch's Russian-doll intuition, now typed.

---

# 14. The new transport defect decomposition

For an adjoint context pair:

\[
F\dashv G,
\]

define structurally:

### Source-side defect

\[
\Delta_{\mathrm{src}}
=
\eta:
1\Rightarrow GF.
\]

### Target-side defect

\[
\Delta_{\mathrm{tgt}}
=
\varepsilon:
FG\Rightarrow1.
\]

### Yoneda-profile defect

\[
\Delta_{\mathrm{Yoneda}}
=
\theta_F.
\]

The theorem identifies:

\[
\boxed{
\Delta_{\mathrm{Yoneda}}
\cong
y(\Delta_{\mathrm{src}}).
}
\]

So two of our previously separate defect languages are actually the same structure.

---

# 15. Strongest moonshot restatement

The context/locality/scale program can now ask:

> For which lawful context changes does there exist an adjunction \(F\dashv G\) such that the source-side Yoneda transport defect is exactly the unit and the target-side missing information is exactly the counit defect?

And in the reversible cases:

\[
\boxed{
F\dashv G
\text{ with }
\eta,\varepsilon\text{ invertible}
}
\]

gives:

\[
\boxed{
\text{context equivalence}.
}
\]

This is the mathematically mature version of the forward/backward form idea.
