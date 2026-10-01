# Yoneda Transport, Forms, Adjunctions, and Reversible Context Change

## From “form1/form2” to generalized-element transport and adjoint equivalence

**Date:** 2026-10-01  
**Status:** research-tier continuation of Semantic Optics. The core category-theory statements are standard/disclosed mathematics. Their use as TLICA semantics is **CONJECTURED / UNVERIFIED**. **Foundation untouched.**

**Finite witness:** [yoneda_transport_forms_demo.py](yoneda_transport_forms_demo.py) · [results](yoneda_transport_forms_demo_results.json) · [receipt](yoneda_transport_forms_demo_tests.txt)

---

# 1. Author moonshot

The motivating intuition is:

> Yoneda transport between two objects \(A,B\) should correspond to forms in both directions, so that for \(c\) represented in \(A\) and \(d\) represented in \(B\),
>
> \[
> d=\operatorname{form}_1(c),
> \qquad
> c=\operatorname{form}_2(d),
> \]
>
> with the strongest case behaving like
>
> \[
> y=f(x)
> \iff
> x=f^{-1}(y).
> \]

This intuition has two rigorous categorical resolutions:

1. **object-level isomorphism** — exact reversible transport of every generalized element/probe;
2. **category/context-level adjunction/equivalence** — natural reversible transport between hom-sets, becoming reversible object transport when the unit/counit are isomorphisms.

These must be kept separate.

---

# 2. Object-level form transport

Let:

\[
A,B\in\mathcal C
\]

and let:

\[
f:A\to B.
\]

The Yoneda embedding is:

\[
y:\mathcal C\to[\mathcal C^{op},\mathbf{Set}]
\]

with:

\[
y(A)=\mathcal C(-,A).
\]

The morphism \(f\) induces a natural transformation:

\[
y(f):
\mathcal C(-,A)
\Rightarrow
\mathcal C(-,B).
\]

At a probe object \(C\), the component is:

\[
y(f)_C:
\mathcal C(C,A)
\to
\mathcal C(C,B)
\]

given by:

\[
\boxed{
x\mapsto f\circ x.
}
\]

So the correct categorical replacement for “apply a form to every point” is:

> **postcompose every generalized element/probe with the form morphism.**

---

# 3. Generalized elements, not raw points

In a general category, \(A\) need not have set-like elements.

A generalized element of \(A\) at stage \(C\) is:

\[
x:C\to A.
\]

Thus “the same form works on every point” becomes:

\[
\forall C\in\mathcal C:
\quad
x:C\to A
\mapsto
f\circ x:C\to B.
\]

This is exactly the representable/Yoneda profile.

If \(\mathcal C\) has a terminal object \(1\), ordinary global elements are the special case:

\[
x:1\to A.
\]

The generalized-element formulation is stronger because it probes \(A\) from every stage \(C\), not only from \(1\).

---

# 4. Exact reversible-form theorem

### Theorem

For:

\[
f:A\to B,
\]

the following are equivalent:

1. \(f\) is an isomorphism;
2. \(y(f)\) is a natural isomorphism;
3. there exists:
   \[
   g:B\to A
   \]
   with:
   \[
   g\circ f=1_A,
   \qquad
   f\circ g=1_B;
   \]
4. for every probe \(C\), the form transport:
   \[
   \mathcal C(C,A)
   \xrightarrow{f\circ-}
   \mathcal C(C,B)
   \]
   is a bijection natural in \(C\).

**Proof:** Yoneda is full and faithful and therefore reflects isomorphisms. The inverse of \(y(f)\) is \(y(f^{-1})\).

\(\square\)

Primary standard source:
- Yoneda uniqueness of representing objects / full faithfulness:
  https://ncatlab.org/nlab/show/Yoneda+lemma

---

# 5. The user's inverse equation, typed correctly

If:

\[
f:A\overset{\sim}{\to}B
\]

and:

\[
x:C\to A,
\]

define:

\[
y=f\circ x:C\to B.
\]

Then:

\[
\boxed{
y=f\circ x
\iff
x=f^{-1}\circ y.
}
\]

This is literally the requested form:

\[
\boxed{
\operatorname{form}_1(x)=y
\iff
x=\operatorname{form}_1^{-1}(y).
}
\]

And this holds at **every probe stage \(C\)**.

That “for every \(C\)” is exactly what makes the statement Yoneda-strength rather than a coordinate coincidence.

---

# 6. Yoneda identification theorem

Because Yoneda is fully faithful:

\[
\boxed{
A\cong B
\iff
y(A)\cong y(B).
}
\]

So:

> two objects have naturally isomorphic complete probe profiles iff they are isomorphic in the declared category.

This is the exact object-level realization of the moonshot.

No truth-proper claim follows; the result is internal to the declared category.

---

# 7. Context/category transport requires functors

Now let:

\[
F:\mathcal A\to\mathcal B,
\qquad
G:\mathcal B\to\mathcal A.
\]

The user's object equations:

\[
d=F(c),
\qquad
c=G(d)
\]

are too strict in general.

The categorical forms are:

\[
c\cong GF(c)
\]

and:

\[
FG(d)\cong d.
\]

That is equivalence of categories, not literal equality of object labels.

---

# 8. Adjoint transport

A weaker and extremely important structure is an adjunction:

\[
F\dashv G.
\]

This is equivalent to natural bijections:

\[
\boxed{
\Phi_{c,d}:
\mathcal B(Fc,d)
\overset{\sim}{\longrightarrow}
\mathcal A(c,Gd)
}
\]

natural in:

\[
c\in\mathcal A,
\qquad
d\in\mathcal B.
\]

This is astonishingly close to the proposed form1/form2 moonshot.

There is a forward form:

\[
\alpha:Fc\to d
\mapsto
\widetilde\alpha:c\to Gd
\]

and an inverse form:

\[
\beta:c\to Gd
\mapsto
\widehat\beta:Fc\to d.
\]

They satisfy:

\[
\boxed{
\Phi^{-1}(\Phi(\alpha))=\alpha,
\qquad
\Phi(\Phi^{-1}(\beta))=\beta.
}
\]

So an adjunction gives **reversible transport of relation/morphism forms** even when the objects themselves are not reversibly transported.

Primary standard source:
- adjunction as natural hom-set isomorphism:
  https://ncatlab.org/nlab/show/adjoint+functor

---

# 9. Unit and counit are round-trip maps

The adjunction generates:

\[
\eta:
1_{\mathcal A}
\Rightarrow
GF
\]

and:

\[
\varepsilon:
FG
\Rightarrow
1_{\mathcal B}.
\]

At objects:

\[
\eta_c:
c\to GFc
\]

and:

\[
\varepsilon_d:
FGd\to d.
\]

These are the categorical **round-trip comparison maps**.

They answer:

> after transporting \(c\) into \(\mathcal B\) and back, how does the recovered object compare with the original?

and:

> after transporting \(d\) into \(\mathcal A\) and back, how does it compare with \(d\)?

---

# 10. Adjoint equivalence = reversible context transport

An adjunction:

\[
F\dashv G
\]

is an **adjoint equivalence** when:

\[
\eta
\]

and:

\[
\varepsilon
\]

are natural isomorphisms.

Then:

\[
\boxed{
GF\cong1_{\mathcal A},
\qquad
FG\cong1_{\mathcal B}.
}
\]

So the context-level analogue of:

\[
y=f(x)
\iff
x=f^{-1}(y)
\]

is:

\[
\boxed{
c\cong G(Fc),
\qquad
d\cong F(Gd).
}
\]

Standard sources:
- equivalence of categories / quasi-inverses:
  https://stacks.math.columbia.edu/download/categories.pdf
- adjoint equivalence:
  https://ncatlab.org/nlab/show/adjoint+equivalence

---

# 11. Strict inverse is stronger than equivalence

If:

\[
GF=1_{\mathcal A}
\]

and:

\[
FG=1_{\mathcal B}
\]

as literal equalities, then \(F,G\) form an isomorphism of categories.

That is stronger than necessary.

For most physics/model/context transport, **equivalence up to coherent natural isomorphism** is the correct target.

Thus:

\[
\boxed{
\text{reversible structure}
\neq
\text{literal identical encoding}.
}
\]

This matches the branch's frame-covariance principle.

---

# 12. The transport ladder

The moonshot naturally produces four levels.

## Level 0 — arbitrary functor

\[
F:\mathcal A\to\mathcal B.
\]

Some structure is transported.

No reversibility guaranteed.

## Level 1 — full and faithful transport

For all:

\[
c,c'\in\mathcal A,
\]

\[
\mathcal A(c,c')
\overset{\sim}{\longrightarrow}
\mathcal B(Fc,Fc').
\]

All internal relations among represented objects are preserved/reflected.

The target may still contain extra objects.

## Level 2 — adjunction

\[
F\dashv G.
\]

Cross-context relation forms are in natural bijection:

\[
\mathcal B(Fc,d)
\cong
\mathcal A(c,Gd).
\]

But round-trip objects need not be equivalent.

## Level 3 — adjoint equivalence

Unit/counit are isomorphisms:

\[
c\cong GFc,
\qquad
FGd\cong d.
\]

Context transport is reversible up to coherent isomorphism.

## Level 4 — strict category isomorphism

Round trips equal identities strictly.

Usually unnecessarily strong.

---

# 13. Yoneda comparison for a context-change functor

Given:

\[
F:\mathcal A\to\mathcal B,
\]

for each:

\[
X\in\mathcal A
\]

there is a canonical natural transformation:

\[
\boxed{
\theta_{F,X}:
y_{\mathcal A}(X)
\Rightarrow
F^\ast y_{\mathcal B}(FX)
}
\]

where:

\[
F^\ast y_{\mathcal B}(FX)
=
\mathcal B(F-,FX).
\]

At:

\[
C\in\mathcal A,
\]

the component is:

\[
\theta_{F,X,C}:
\mathcal A(C,X)
\to
\mathcal B(FC,FX)
\]

with:

\[
h\mapsto Fh.
\]

This is the exact **Yoneda transport comparison map**.

---

# 14. Full-faithfulness theorem for Yoneda transport

### Theorem

The following are equivalent:

1. \(F\) is full and faithful;
2. for every \(X\), \(\theta_{F,X}\) is a natural isomorphism;
3. for all \(C,X\),:
   \[
   \mathcal A(C,X)
   \overset{\sim}{\to}
   \mathcal B(FC,FX).
   \]

**Proof:** this is simply the definition of full + faithful applied to every hom-set, packaged representably.

\(\square\)

Thus:

\[
\boxed{
\text{zero Yoneda morphism-transport defect}
\iff
F\text{ full and faithful}.
}
\]

---

# 15. Two independent transport defects

The previous result reveals an important missing distinction.

A context functor can be full and faithful while failing to cover the target.

Therefore define structurally:

### Hom/Yoneda defect

Failure of:

\[
\theta_{F,X}
\]

to be a natural isomorphism.

This measures loss/addition of morphisms among transported objects.

### Coverage defect

Failure of essential surjectivity:

\[
\exists d\in\mathcal B
\quad
\forall c\in\mathcal A:
\quad
d\not\cong Fc.
\]

Then:

\[
\boxed{
F\text{ equivalence}
\iff
\Delta_{\mathrm{hom}}(F)=0
\quad\text{and}\quad
\Delta_{\mathrm{cov}}(F)=0.
}
\]

These are structural defect types, not numerical scalars unless extra structure is supplied.

---

# 16. Why this matters for scale/locality transport

A scale/locality functor:

\[
F:
\mathcal C_{n,U}
\to
\mathcal C_{m,V}
\]

can therefore be audited in two independent ways.

## A. Relational preservation

Does every represented object preserve its full probe/hom profile?

\[
\theta_{F,X}
\text{ iso?}
\]

## B. Context coverage

Does the target context contain genuinely new objects not represented from the source?

If yes, then transport can be perfectly full/faithful while the richer context contains new reality/model structure.

This is exactly what a **host lamp** should look like.

---

# 17. Host enrichment as coverage rather than morphism failure

This corrects a potential overstatement in the earlier “Yoneda defect” language.

A richer host context can add new objects while preserving every old relation perfectly.

Then:

\[
F
\]

is full and faithful,

but not essentially surjective.

So the old world embeds losslessly:

\[
\mathcal A
\hookrightarrow
\mathcal B,
\]

while the host contains additional structure.

This is **not** a failure of Yoneda transport on the image.

It is a coverage expansion.

That distinction is load-bearing.

---

# 18. Adjoint transport as asymmetric context translation

Suppose:

\[
F\dashv G
\]

but unit/counit are not isomorphisms.

Then relation forms translate reversibly:

\[
\mathcal B(Fc,d)
\cong
\mathcal A(c,Gd),
\]

while objects can change under round-trip:

\[
c\to GFc,
\]

\[
FGd\to d.
\]

This is a very plausible model for **lossy but lawful context transport**.

Examples conceptually include:

- abstraction/concretization;
- free/forgetful constructions;
- coarse/fine representations;
- encoding/decoding with canonical approximation.

No TLICA identification is claimed yet.

---

# 19. Round-trip defect

For an adjunction, define the structural round-trip defect by the unit/counit:

\[
\Delta_{\mathcal A}(c):=\eta_c:c\to GFc,
\]

\[
\Delta_{\mathcal B}(d):=\varepsilon_d:FGd\to d.
\]

The defect vanishes up to isomorphism exactly when:

\[
\eta_c
\]

and:

\[
\varepsilon_d
\]

are isomorphisms.

Thus:

\[
\boxed{
\text{adjoint equivalence}
=
\text{zero round-trip defect everywhere}.
}
\]

Again, “zero” means invertible comparison, not a scalar magnitude.

---

# 20. The form1/form2 correspondence, final typed version

The user's intuition becomes:

### Object level

There exist:

\[
f:A\to B,
\qquad
g:B\to A
\]

with:

\[
gf=1_A,
\qquad
fg=1_B.
\]

Then for every generalized element:

\[
x:C\to A,
\]

\[
y=f\circ x,
\qquad
x=g\circ y.
\]

### Category level

There exist:

\[
F:\mathcal A\to\mathcal B,
\qquad
G:\mathcal B\to\mathcal A
\]

with natural isomorphisms:

\[
GF\cong1_{\mathcal A},
\qquad
FG\cong1_{\mathcal B}.
\]

Then every object transports out and back up to coherent isomorphism.

### Adjoint weakening

Even without equivalence:

\[
F\dashv G
\]

gives reversible transport of morphism forms:

\[
\mathcal B(Fc,d)
\cong
\mathcal A(c,Gd).
\]

This is the strongest rigorous reading of the moonshot currently earned.

---

# 21. TLICA interpretation

For Semantic Optics, each context:

\[
b=(n,U)
\]

has a category:

\[
\mathcal C_b.
\]

A lawful context arrow:

\[
u:b\to b'
\]

induces a transport:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'}.
\]

Now classify \(F_u\):

- arbitrary;
- full/faithful;
- adjointable;
- adjoint equivalence;
- strict isomorphism.

This turns “Yoneda transport across locality/scale” into a **typed audit**, not one binary property.

---

# 22. New moonshot: adjoint context atlas

A very strong future structure would assign to important context changes:

\[
u:b\to b'
\]

a pair:

\[
F_u\dashv G_u
\]

with unit/counit recording the precise round-trip information loss.

Then localities/scales would form a base category whose arrows carry not only functors but **adjoint transport data**.

If some subclass has invertible unit/counit, those context changes form equivalences.

This begins to resemble a bicategory/2-category of contexts, transport functors, and natural transformations.

**Status: CONJECTURED research direction.**

---

# 23. What would falsify the moonshot?

The program weakens if:

1. important context transports have no coherent functorial action;
2. candidate forward/backward forms fail naturality;
3. hom-set transport is not bijective where an adjunction is claimed;
4. triangle identities fail;
5. claimed reversible transport has noninvertible unit/counit;
6. the form maps depend on arbitrary coordinates rather than categorical structure;
7. the added machinery predicts nothing beyond ordinary full/faithful/adjunction theory.

---

# 24. Current conclusion

The user's equation was almost exactly the object-level Yoneda isomorphism statement:

\[
\boxed{
y=f\circ x
\iff
x=f^{-1}\circ y
}
\]

for every generalized element \(x:C\to A\).

The category-level generalization is not direct inverse functions on raw objects, but:

\[
\boxed{
F\dashv G:
\quad
\mathcal B(Fc,d)
\cong
\mathcal A(c,Gd)
}
\]

and the reversible limit is:

\[
\boxed{
GF\cong1_{\mathcal A},
\qquad
FG\cong1_{\mathcal B}.
}
\]

That is the current mathematically clean meaning of **Yoneda transport by forms**.
