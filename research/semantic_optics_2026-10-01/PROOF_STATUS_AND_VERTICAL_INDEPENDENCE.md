# Proof Status and Vertical Independence

## Non-refutability, relative independence, and host-theory ascent

**Date:** 2026-10-01  
**Status:** research-tier metatheory note. Standard proof-theoretic distinctions are established mathematics; the TLICA application is **CONJECTURED / UNVERIFIED**. **Foundation untouched.**

---

# 1. The proof-status theorem

Let:

\[
T
\]

be a formal TLICA-related theorem candidate inside a formal system:

\[
S.
\]

Write:

\[
\Box_S T
\]

for “\(T\) is provable in \(S\).”

Define formal independence:

\[
I_S(T)
:=
\neg\Box_S T
\land
\neg\Box_S\neg T.
\]

If we establish non-refutability:

\[
\neg\Box_S\neg T,
\]

then, classically in the metatheory:

\[
\Box_S T
\vee
\neg\Box_S T.
\]

Therefore:

\[
\boxed{
\neg\Box_S\neg T
\Rightarrow
\Box_S T
\vee
I_S(T).
}
\]

This is the clean version of:

> not refutable \(\Rightarrow\) provable or independent.

It is a statement about **proof status**, not truth proper.

---

# 2. Constructive version

Without unrestricted excluded middle in the metatheory, the safe form is:

\[
\boxed{
\neg\Box_S\neg T
\Rightarrow
\neg\neg
\left(
\Box_S T
\vee
I_S(T)
\right).
}
\]

This does not provide a witness for which disjunct holds.

So the operative states are:

\[
\boxed{
\text{proved},
\quad
\text{refuted},
\quad
\text{currently undecided}.
}
\]

The third state is not falsehood.

---

# 3. Non-refutability is not “not yet refuted”

The theorem requires:

\[
S\nvdash \neg T.
\]

That is a metatheoretic property of \(S\), not:

> “we tried a lot of counterexamples and have not found one.”

Failure to find a refutation is evidence at best.

It is not proof of non-refutability.

This is the first anti-self-sealing firewall.

---

# 4. Independence is relative

A proposition can be independent of:

\[
S_n
\]

while decidable in a stronger theory:

\[
S_{n+1}.
\]

That is:

\[
S_n\nvdash T,
\qquad
S_n\nvdash\neg T,
\]

while perhaps:

\[
S_{n+1}\vdash T.
\]

So:

\[
\boxed{
\operatorname{Independent}_{S_n}(T)
\not\Rightarrow
\operatorname{Independent}_{S_{n+1}}(T).
}
\]

This is **vertical independence**.

---

# 5. Embeddedness motivates host ascent, not guaranteed decidability

The author's physical intuition is that a local dynamical system is realized inside a higher host system.

Suppose a local theory:

\[
S_n
\]

describes a realized lower-level system.

If \(T\) is independent in \(S_n\), it is reasonable to search a richer host theory:

\[
S_{n+1}
\]

that retains distinctions or realization structure erased below.

So formal independence should trigger:

\[
S_n
\to
S_{n+1}
\to
S_{n+2}
\to\cdots.
\]

But physical embeddedness alone does **not** prove:

\[
\exists m>n:
S_m\vdash T
\vee
S_m\vdash\neg T.
\]

A host can realize a computationally rich dynamical system while some global properties remain undecidable.

---

# 6. Bounded versus unbounded propositions

The embeddedness intuition is strongest for finite operational questions.

For example:

\[
T_N:
\text{“Does event }E\text{ occur within }N\text{ update steps?”}
\]

can often be decided by finite execution in an explicitly computable finite system.

But:

\[
T_\infty:
\text{“Does }E\text{ ever occur?”}
\]

can encode undecidable reachability/halting-style questions in sufficiently expressive dynamics.

Therefore distinguish:

\[
\boxed{
\text{bounded operational decidability}
}
\]

from:

\[
\boxed{
\text{unbounded global decidability}.
}
\]

---

# 7. Vertical Resolution Conjecture

A useful restricted conjecture is:

> **VRC.** For a physically realized system, finite, causally bounded, operationally meaningful propositions that are undecided in a lower effective theory will often become decidable in some sufficiently adequate host description because the host retains distinctions quotiented or inaccessible below.

This is **CONJECTURED**.

The words:

- finite;
- causally bounded;
- operationally meaningful;

are load-bearing.

An unrestricted “every proposition is decided somewhere above” claim is too strong.

---

# 8. Relationship to the operational quotient theorem

Suppose:

\[
Q:
\mathcal H
\to
\mathcal L
\]

is a full operational quotient from a richer host category into a lower effective category.

A lower collision:

\[
Q(f)=Q(g)
\]

may correspond to:

\[
f\neq g
\]

upstairs.

A lower proposition about distinguishing the two can therefore be undecidable/unavailable in the quotient while decidable in the host.

This is the categorical version of vertical resolution:

\[
\boxed{
\text{lower operational equivalence}
\;\not\Rightarrow\;
\text{host equivalence}.
}
\]

---

# 9. Host lamps

A host-level probe:

\[
P:
\mathcal H
\to
\mathcal E
\]

is a **host lamp** for a lower collision when:

\[
Q(f)=Q(g)
\]

but:

\[
P(f)\neq P(g).
\]

Then the host contains an admissible discriminator erased by the lower model.

If every admissible host probe also identifies \(f,g\), the distinction may be gauge/task redundancy even upstairs.

---

# 10. Truth proper remains separate

None of the following implies truth proper:

\[
S\vdash T,
\]

unless \(S\) is assumed sound for the relevant semantics.

Nor does:

\[
I_S(T)
\]

mean that \(T\) lacks a determinate truth value.

So:

\[
\boxed{
\text{provability}
\neq
\text{truth}
\neq
\text{independence}.
}
\]

The Semantic Optics / Full Yoneda program remains about:

- structural representation;
- available discrimination;
- proof status;
- operational adequacy.

It does not manufacture metaphysical truth.

---

# 11. Strongest current statement

The current defensible theorem/conjecture package is:

\[
\boxed{
\neg\Box_S\neg T
\Rightarrow
\Box_S T\vee I_S(T)
}
\]

classically in the metatheory,

plus the physical research conjecture:

\[
\boxed{
I_{S_n}(T)
\Rightarrow
\text{search upward for a host theory }S_{n+1}
}
\]

without claiming eventual resolution for every \(T\).

That is the exact proof-status form of the author's intuition.
