# Yoneda Moonshot

## Can TLICA Semantic Optics be Yoneda-certified against categorical optics?

**Status:** research program. Standard Yoneda/density statements are **Disclosed mathematics**. Every TLICA-specific equivalence claim is **UNVERIFIED**.

---

# 1. First correction: “Yoneda equivalent” is not yet a theorem statement

Yoneda gives, for a locally small category \(\mathcal C\):

\[
y_{\mathcal C}:
\mathcal C
\to
[\mathcal C^{op},\mathbf{Set}],
\qquad
X\mapsto\mathcal C(-,X),
\]

and the Yoneda lemma implies that \(y_{\mathcal C}\) is full and faithful.

This does **not** compare two independently defined categories.

To compare TLICA optics and categorical optics we need:

\[
F:
\mathsf{TOpt}
\to
\mathsf{Optic}_{\mathcal C}.
\]

The moonshot then becomes a hierarchy of explicit claims.

---

# 2. Target A — faithful embedding

Prove \(F\) is faithful:

\[
F(f)=F(g)
\Rightarrow
f=g.
\]

Interpretation:

> no two distinct TLICA-optics morphisms collapse to the same categorical optic under the bridge.

Failure mode:

> categorical optics is too coarse to preserve a TLICA distinction.

This is a good failure, not an embarrassment.

---

# 3. Target B — full embedding

Prove \(F\) is full:

for every:

\[
h:
F(X)\to F(Y)
\]

in the target optic category, there exists:

\[
f:X\to Y
\]

with:

\[
F(f)=h.
\]

Interpretation:

> every target optic between represented TLICA objects is realizable by a TLICA-optics morphism.

Failure mode:

> categorical optics permits interface transformations that TLICA's semantics excludes.

Again, that would identify substantive structure.

---

# 4. Target C — full and faithful

If both hold:

\[
\mathsf{TOpt}
\simeq
\operatorname{Im}(F)
\]

as a full subcategory.

This would support the claim:

> TLICA optics is a granularized realization of a subfamily of categorical optics.

No essential-surjectivity claim is required.

This is currently the most plausible strong target.

---

# 5. Target D — essential surjectivity

For every optic object \(O\) in the target category, require an \(X\in\mathsf{TOpt}\) such that:

\[
F(X)\cong O.
\]

Full + faithful + essentially surjective yields categorical equivalence:

\[
\boxed{
\mathsf{TOpt}
\simeq
\mathsf{Optic}_{\mathcal C}.
}
\]

This is the literal category-equivalence moonshot.

It is probably too strong globally.

A bounded equivalence on a carefully typed subcategory is more realistic.

---

# 6. Where Yoneda enters nontrivially

If \(F\) is full and faithful, then for all \(X,Y\):

\[
\mathsf{TOpt}(X,Y)
\cong
\mathsf{Optic}_{\mathcal C}(F X,F Y).
\]

Yoneda turns objects into their complete incoming-morphism profiles:

\[
X
\mapsto
\mathsf{TOpt}(-,X).
\]

Thus a full/faithful \(F\) preserves the representable probe structure.

A candidate certificate is a natural isomorphism:

\[
\mathsf{TOpt}(-,X)
\cong
\mathsf{Optic}_{\mathcal C}(F-,F X)
\]

natural in the probing object.

But this statement is essentially another face of full faithfulness.

Yoneda is a **certificate / representation principle**, not a magical route around constructing \(F\).

---

# 7. The actual interesting Yoneda connection: probes

TLICA repeatedly distinguishes:

- what exists in the model;
- what probes are available;
- whether a pathway is constructible;
- whether two live rivals can currently be discriminated.

This suggests using **restricted Yoneda**.

Let:

\[
i:\mathcal P\hookrightarrow\mathsf{TOpt}
\]

be a category of admissible probes.

Define:

\[
N_{\mathcal P}(X)
=
\mathsf{TOpt}(i-,X).
\]

This is a presheaf:

\[
N_{\mathcal P}(X):
\mathcal P^{op}
\to
\mathbf{Set}.
\]

It records how every available probe maps into \(X\).

---

# 8. Density

A standard theorem says:

\[
i:\mathcal P\to\mathcal C
\]

is dense iff the corresponding restricted Yoneda / nerve:

\[
N_i:
\mathcal C
\to
[\mathcal P^{op},\mathbf{Set}]
\]

is full and faithful.

References:

- https://ncatlab.org/nlab/show/dense+functor
- https://ncatlab.org/nlab/show/nerve
- https://ncatlab.org/nlab/show/restricted+Yoneda+embedding

So:

\[
\boxed{
\text{dense probe family}
\iff
\text{objects/morphisms are fully recoverable from probe profiles}.
}
\]

This is a precise theorem, not metaphor.

---

# 9. Restricted-probe collision

If \(\mathcal P\) is not dense, we can have:

\[
X\not\cong Y
\]

but:

\[
N_{\mathcal P}(X)
\cong
N_{\mathcal P}(Y).
\]

Call this a **probe collision**.

The current probe family cannot distinguish the objects even though the full category can.

This is exactly the shape needed for:

> “no present discriminator reaches the distinction.”

It does **not** mean:

\[
X=Y
\]

or:

\[
X,Y
\text{ are metaphysically identical}.
\]

It means only that the declared restricted observation functor collapses them.

---

# 10. A lamp as probe-family extension

Suppose:

\[
\mathcal P
\hookrightarrow
\mathcal P'
\hookrightarrow
\mathcal C.
\]

A lamp for \(X,Y\) is an extension such that:

\[
N_{\mathcal P}(X)
\cong
N_{\mathcal P}(Y)
\]

but:

\[
N_{\mathcal P'}(X)
\not\cong
N_{\mathcal P'}(Y).
\]

This makes “name the lamp” mathematically concrete.

It is still application-level.

---

# 11. Why this is not simply \(\mu\)

TLICA's \(\mu\) tracks probe availability / weighting.

Density is different.

A useful separation is:

\[
\mathcal P^{\mathrm{model}}
=
\text{all declared probe forms in the formal domain},
\]

\[
\mathcal P_j^{\mathrm{constructible}}
=
\mathrm{Cl}(\mathrm{Tools}_j)
\cap
\mathcal P^{\mathrm{model}},
\]

while:

\[
\mu_j
\]

weights / gates those probes for the observer.

Then density asks whether:

\[
\mathcal P_j^{\mathrm{constructible}}
\hookrightarrow
\mathcal C
\]

is rich enough to recover objects categorically.

So:

\[
\boxed{
\mu\neq\text{density}.
}
\]

---

# 12. Why this is not simply \(\phi\)

A restricted-Yoneda collision can model one kind of toolkit-relative indistinguishability.

But \(\phi\) already has architecture-specific semantics.

The bridge would need to prove something like:

\[
\phi_j(x)\approx\phi_j(y)
\]

under specific conditions iff:

\[
N_{\mathcal P_j}(X)
\cong
N_{\mathcal P_j}(Y).
\]

No such theorem exists yet.

Do not identify them.

---

# 13. Dense probe families and contextual saturation

Suppose a declared probe subcategory \(\mathcal P\) is dense in the declared finite/model category.

Then no two non-isomorphic objects have identical \(\mathcal P\)-nerves.

Within that formal boundary:

> the probe language is structurally complete.

If all live rivals remain isomorphic under the declared category after this condition, one can call the model contextually saturated **relative to the declared category**.

This still does not establish metaphysical finality.

The category itself may omit real-world structure.

---

# 14. A conditional Yoneda bridge theorem

Let:

\[
F:\mathsf T\to\mathsf O
\]

be the proposed TLICA-to-optics functor.

Let:

\[
i:\mathcal P\to\mathsf T
\]

and:

\[
j:\mathcal Q\to\mathsf O
\]

be dense probe functors.

Suppose there is an equivalence:

\[
B:\mathcal P\simeq\mathcal Q
\]

and, for every \(X\in\mathsf T\), a natural isomorphism of probe nerves:

\[
\mathsf T(i-,X)
\cong
\mathsf O(jB-,F X).
\]

Then, because the nerves are full and faithful, the probe representation of \(X\) determines it up to isomorphism in \(\mathsf T\), and the matched probe representation determines \(FX\) in \(\mathsf O\).

This does not by itself prove essential surjectivity of \(F\), but it supplies a strong route to full faithfulness once the naturality/coherence data are constructed.

**Status:** conditional proof strategy, not yet a completed TLICA theorem.

---

# 15. Yoneda-visible and Yoneda-invisible deviations

Suppose:

\[
p:\mathsf{TOpt}\to\mathsf{Optic}
\]

forgets TLICA decorations.

Let:

\[
\widetilde X_1,\widetilde X_2
\]

lie over the same base object:

\[
p(\widetilde X_1)
=
p(\widetilde X_2)
=
X.
\]

If:

\[
y_{\mathsf{TOpt}}(\widetilde X_1)
\not\cong
y_{\mathsf{TOpt}}(\widetilde X_2),
\]

then the decoration changes compositional behavior.

It is **Yoneda-visible**.

The undecorated base optic does not capture the full distinction.

If instead:

\[
y_{\mathsf{TOpt}}(\widetilde X_1)
\cong
y_{\mathsf{TOpt}}(\widetilde X_2),
\]

then Yoneda implies:

\[
\widetilde X_1
\cong
\widetilde X_2.
\]

The apparent deviation is only representational up to isomorphism.

This gives a rigorous “is this extra structure real?” test inside the category.

---

# 16. Practical restricted visibility

Full Yoneda uses **all** probes in the category.

Humans never have that.

Therefore distinguish:

\[
\text{Yoneda-visible}
\]

from:

\[
\text{currently probe-visible}.
\]

A TLICA decoration can be invisible under:

\[
N_{\mathcal P_j}
\]

yet visible under the full Yoneda embedding.

This is exactly the configuration we should expect when a future discriminator exists but current tools do not reach it.

---

# 17. The key equivalence trilemma

Suppose we have a TLICA “deviation” \(\delta\).

There are three possibilities.

## Case 1 — pure gauge

\[
\delta
\]

does not change the isomorphism class / Yoneda profile.

Then the deviation is representational redundancy.

## Case 2 — restricted-probe invisible, full-Yoneda visible

The deviation is genuine in the total category but inaccessible to current probes.

This is the most interesting “Dark but structurally live” case.

## Case 3 — current-probe visible

The deviation is already discriminable.

Then it belongs in the operative model now.

This trilemma gives the “Categorical Optics + TLICA deviation” idea real teeth.

---

# 18. How a false equivalence could be manufactured

A trivial construction can always absorb TLICA state into the base category.

For example, define objects as:

\[
(S,\Theta)
\]

and make morphisms preserve exactly the TLICA rules.

Then of course one can build an optic category containing them.

This is not enough.

The moonshot must require:

1. an independently motivated optic base;
2. a separately defined TLICA semantic category;
3. a bridge on generators;
4. inherited identities/composition;
5. no hidden use of the desired theorem in the definitions;
6. an adversarial finite countermodel program.

---

# 19. The anti-cheat finite program

Before attempting an abstract proof, construct finite categories where:

- the bridge is faithful but not full;
- full but not faithful;
- neither;
- full and faithful but not essentially surjective;
- genuinely equivalent.

Then build a TLICA-like decorated case and see which class it naturally occupies.

This prevents “equivalence” from being declared because one favorable toy was designed to have it.

---

# 20. Connection to the optic profunctor representation

Categorical optics already admit alternative representations through profunctor/Tambara machinery.

This means there are at least two Yoneda-like representation questions:

1. **internal optics representation**:
   concrete/coend optic vs profunctor/Tambara encoding;
2. **external TLICA bridge**:
   TLICA semantic optic vs optic category.

Do not confuse them.

Success on (1) is established category theory.

Success on (2) remains the moonshot.

---

# 21. If the moonshot succeeds, what does it mean philosophically?

Not:

> TLICA is true because category theory.

It would mean:

> the structural relations TLICA uses for this declared observer-interface domain can be represented without loss as morphisms/objects in a categorical optic structure, and their full compositional probe behavior agrees up to categorical equivalence.

This is a structural result.

Empirical truth still depends on whether TLICA's objects match human/world data.

---

# 22. If the moonshot fails, what do we learn?

Failure localizes.

## Non-faithfulness

TLICA distinguishes something ordinary optics erases.

Question:

> is that distinction meaningful or redundant?

## Non-fullness

Optics permits something TLICA disallows.

Question:

> is TLICA imposing a substantive law, or is the model incomplete?

## Non-essential-surjectivity

TLICA covers only a proper family of optics.

This is likely and not problematic.

## Functoriality failure

Composition in TLICA does not map to optic composition.

This would be a major structural obstruction and probably kills the strong bridge.

## Probe-density failure

The declared probe family cannot reconstruct the category.

Then Yoneda-style practical certification is unavailable without better probes.

---

# 23. Current moonshot verdict

### Disclosed

- Yoneda embedding is full and faithful.
- Restricted Yoneda is fully faithful exactly under density.
- Full + faithful + essentially surjective is the standard route to categorical equivalence.
- Categorical optics themselves already use Yoneda/coend reduction internally.

### Conjectured

- TLICA semantic optics forms a category suitable for a bridge.
- a full/faithful embedding exists on a meaningful subdomain.
- TLICA probe closure can be usefully represented by a restricted nerve.

### UNVERIFIED

- any equivalence between TLICA optics and an optic category;
- density of any real TLICA probe family;
- any identification of \(\phi\), \(\mu\), or “Dark” with categorical notions.

---

# 24. Strongest next proof obligation

Define finite:

\[
\mathsf T_{\mathrm{toy}}
\]

independently.

Define:

\[
\mathsf O_{\mathrm{toy}}
=
\operatorname{Optic}_{\mathcal C_{\mathrm{toy}}}.
\]

Construct:

\[
F_{\mathrm{toy}}.
\]

Then enumerate:

- objects;
- hom-sets;
- composition;
- identities;
- representable profiles;
- restricted probe nerves.

Do not handwave any cell.

The first serious result should be either:

\[
F_{\mathrm{toy}}
\text{ is full and faithful},
\]

or a minimal explicit counterexample showing exactly why not.

Both outcomes advance the program.
