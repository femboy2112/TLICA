# Context Transport 2-Architecture

## Locality/scale contexts, transport functors, and form adjunctions

**Date:** 2026-10-01  
**Status:** research-tier architectural synthesis. The 2-categorical machinery is standard; its TLICA interpretation is **CONJECTURED / UNVERIFIED**.

---

# 1. Why one ordinary category is not enough

The branch now tracks two qualitatively different things:

1. movement between contexts;
2. morphisms/relations inside a context.

A context is indexed schematically by:

\[
b=(n,U)
\]

where:

- \(n\) = realization/effective scale;
- \(U\) = local/causal region.

Each context has its own category:

\[
\mathcal C_b.
\]

A context change:

\[
u:b\to b'
\]

induces a transport functor:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'}.
\]

So the correct structure is not simply:

> “localities/scales are objects and Yoneda maps are arrows.”

It is:

\[
\boxed{
\text{contexts downstairs}
+
\text{categories over contexts}
+
\text{functors between fibers}
+
\text{natural transformations between those functors}.
}
\]

---

# 2. Base context category

Let:

\[
\mathsf B
\]

be a category of contexts.

Objects:

\[
b=(n,U).
\]

Arrows may include:

- localization/restriction;
- causal-horizon enlargement;
- scale refinement;
- scale coarse-graining;
- frame/chart changes;
- lawful composites of these.

Composition in \(\mathsf B\) expresses composability of context changes.

---

# 3. Indexed categories

Assign:

\[
\mathcal C:
\mathsf B
\to
\mathbf{Cat}
\]

or contravariantly:

\[
\mathcal C:
\mathsf B^{op}
\to
\mathbf{Cat},
\]

depending on whether the chosen transport convention is push-forward or restriction/reindexing.

For:

\[
u:b\to b',
\]

we obtain:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'}.
\]

If composition is strict:

\[
F_{v\circ u}
=
F_v\circ F_u.
\]

More generally, physical/model transport may be pseudofunctorial:

\[
F_{v\circ u}
\cong
F_v\circ F_u
\]

coherently.

The pseudofunctor formulation is likely safer.

---

# 4. Grothendieck total category

The indexed family can be packaged into one total category:

\[
\int_{\mathsf B}\mathcal C.
\]

Objects are:

\[
\boxed{
(b,X)
}
\]

with:

\[
X\in\mathcal C_b.
\]

A morphism combines:

1. context motion:
   \[
   u:b\to b';
   \]
2. an internal map relating \(X\) to the transported target/source object.

The exact variance determines whether the internal arrow is:

\[
F_uX\to Y
\]

or:

\[
X\to u^\*Y.
\]

This is the rigorous version of:

> “things-at-localities/scales.”

---

# 5. Why the 2-category \(\mathbf{Cat}\) matters

Transport functors themselves can be related by natural transformations.

Suppose:

\[
F,G:
\mathcal C_b
\to
\mathcal C_{b'}.
\]

A natural transformation:

\[
\alpha:F\Rightarrow G
\]

can encode:

- a correction between two transport models;
- a gauge/reparametrisation;
- a unit/counit;
- a comparison between approximate and refined context transport.

Thus the natural ambient object is the 2-category:

\[
\boxed{
\mathbf{Cat}
}
\]

with:

- 0-cells: categories;
- 1-cells: functors;
- 2-cells: natural transformations.

Semantic Optics is increasingly a 2-categorical problem.

---

# 6. Context adjunctions

For a context transition:

\[
u:b\to b',
\]

suppose the forward transport:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'}
\]

has a right adjoint:

\[
G_u:
\mathcal C_{b'}
\to
\mathcal C_b.
\]

Then:

\[
F_u\dashv G_u.
\]

This supplies:

\[
\mathcal C_{b'}(F_uc,d)
\cong
\mathcal C_b(c,G_ud).
\]

So every cross-context relation involving a forward-transported source object has a unique backward form in the source context.

This is the exact category-level implementation of the author's forward/backward form idea.

---

# 7. Unit/counit are 2-cells

The adjunction provides:

\[
\eta^u:
1_{\mathcal C_b}
\Rightarrow
G_uF_u
\]

and:

\[
\varepsilon^u:
F_uG_u
\Rightarrow
1_{\mathcal C_{b'}}.
\]

These are not extra 1-cells.

They are **2-cells** measuring round-trip comparison.

This is why an ordinary 1-category of contexts cannot fully store the transport semantics.

---

# 8. Reversible context arrows

A context transport is reversibly equivalent when:

\[
F_u\dashv G_u
\]

and:

\[
\eta^u,\varepsilon^u
\]

are natural isomorphisms.

Then:

\[
\mathcal C_b
\simeq
\mathcal C_{b'}.
\]

This includes:

- change of frame;
- change of coordinates;
- change of presentation;

when no structural information is lost.

It should **not** be imposed on:

- coarse-graining;
- restriction to smaller regions;
- lossy observation;
- quotient maps.

---

# 9. Lossy context arrows

If:

\[
F_u\dashv G_u
\]

but unit/counit are not both isomorphisms, transport remains lawful but not reversible.

Examples of the structural shape:

- coarse abstraction;
- local restriction;
- free/forgetful construction;
- lossy encoding with universal reconstruction.

The unit/counit identify exactly where round-trip recovery fails.

This is more informative than one scalar “transport loss.”

---

# 10. Fiberwise Yoneda

Each context category has:

\[
y_b:
\mathcal C_b
\to
\widehat{\mathcal C_b}
:=
[\mathcal C_b^{op},\mathbf{Set}].
\]

For:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'},
\]

the canonical Yoneda comparison is:

\[
\theta_{u,X}:
y_b(X)
\to
F_u^\*y_{b'}(F_uX).
\]

If \(F_u\dashv G_u\), the Adjoint–Yoneda Transport Theorem identifies:

\[
\theta_{u,X}
\]

with:

\[
y_b(\eta_X^u)
\]

under:

\[
F_u^\*y_{b'}(F_uX)
\cong
y_b(G_uF_uX).
\]

Thus:

\[
\boxed{
\text{fiberwise Yoneda transport defect}
=
\text{adjunction unit defect}.
}
\]

---

# 11. Presheaf transport above the fibers

A context functor:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'}
\]

also induces:

\[
F_u^\*:
\widehat{\mathcal C_{b'}}
\to
\widehat{\mathcal C_b}.
\]

Under standard completeness/smallness conditions:

\[
(F_u)_!
\dashv
F_u^\*
\dashv
(F_u)_*.
\]

So the presheaf/Yoneda worlds themselves admit forward/backward context transport through Kan extensions.

This gives a second layer:

\[
\boxed{
\text{object transport}
}
\]

and:

\[
\boxed{
\text{probe-profile transport}.
}
\]

They should agree on representables:

\[
(F_u)_! y_b(X)
\cong
y_{b'}(F_uX).
\]

---

# 12. A transport square above every context arrow

For representable \(X\), the intended structure is:

\[
\begin{array}{ccc}
X
&\xrightarrow{F_u}&
F_uX
\\
\downarrow y_b
&&
\downarrow y_{b'}
\\
y_bX
&\xrightarrow{(F_u)_!}&
y_{b'}F_uX.
\end{array}
\]

The square commutes up to the canonical natural isomorphism supplied by Kan-extension/Yoneda theory.

This is a much stronger formulation of:

> Yoneda rides coherently on context transport.

---

# 13. Two independent defects across a context arrow

For:

\[
F_u:
\mathcal C_b
\to
\mathcal C_{b'},
\]

keep separate:

## Internal relational defect

Failure of:

\[
\theta_{u,X}
\]

to be an isomorphism.

Equivalent to failure of full faithfulness.

## Coverage defect

Failure of essential surjectivity:

\[
\exists d\in\mathcal C_{b'}:
d\not\cong F_uc
\quad
\forall c.
\]

A richer context can have zero relational defect but nonzero coverage defect.

That is:

\[
\boxed{
\text{lossless embedding into a richer world}.
}
\]

---

# 14. Three context-change regimes

### Covariant re-description

\[
F_u
\]

is an equivalence.

No structural loss.

Example shape: coordinate/frame change.

### Faithful enrichment

\[
F_u
\]

is full and faithful but not essentially surjective.

Old structure preserved; target adds new objects.

Example shape: host theory exposing additional degrees of freedom.

### Quotient/restriction

\[
F_u
\]

is not faithful or not full.

Some old distinctions/arrows are collapsed or some target relations do not lift.

Example shape: coarse-graining/local restriction.

This taxonomy should replace the vague phrase “move to a richer context.”

---

# 15. Context atlas

The long-run object may be a 2-category/bicategory:

\[
\mathsf{Ctx}
\]

whose:

- objects are context categories \(\mathcal C_{n,U}\);
- 1-cells are lawful transports;
- 2-cells are transport comparisons/corrections.

Adjunctions among 1-cells encode forward/backward forms.

Equivalences encode reversible changes of context.

Operational quotient functors encode lossy context changes.

This gives one home for:

- Yoneda transport;
- host lamps;
- locality restriction;
- scale refinement;
- optics quotients;
- model updates.

---

# 16. TLICA delta in the 2-architecture

A TLICA-specific distinction can appear as:

1. a kernel pair of a 1-cell:
   \[
   Ff=Fg;
   \]
2. a noninvertible unit/counit 2-cell;
3. a coverage defect;
4. a mismatch between two candidate transport 1-cells:
   \[
   \alpha:F\Rightarrow G;
   \]
5. a failure of scale/locality pseudofunctorial coherence.

So “TLICA delta” is no longer one object.

It is a **typed defect family indexed by where the context architecture fails to be invertible/faithful/covering/coherent**.

---

# 17. Highest-value next theorem

The next nontrivial target is:

> construct a finite context base \(\mathsf B\), a pseudofunctor \(\mathcal C:\mathsf B\to\mathbf{Cat}\), specified adjoints on selected arrows, and verify:
>
> - pseudofunctor composition;
> - units/counits;
> - triangle identities;
> - fiberwise Yoneda comparison;
> - Kan-extension transport of representables;
> - operational quotient behavior on lossy arrows.

That would be the first actual **context atlas witness** rather than isolated transport examples.

---

# 18. Current conclusion

The corrected architecture is:

\[
\boxed{
\begin{aligned}
\text{0-cells}&:\text{ context categories},\\
\text{1-cells}&:\text{ lawful context transports},\\
\text{2-cells}&:\text{ natural comparisons / units / counits},\\
\text{fiber Yoneda}&:\text{ complete relational fingerprint},\\
\text{Kan transport}&:\text{ transport of probe profiles}.
\end{aligned}
}
\]

The user's “forms in both directions” are therefore best modeled not as two arbitrary functions, but as **adjoint 1-cells with unit/counit 2-cells**, becoming quasi-inverses in the reversible limit.
