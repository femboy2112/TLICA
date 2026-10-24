# Typed formalism: labels are not latent states

**Scope:** definitions, conditional finite propositions, and a path to empirical falsification. Not a formal derivation of slang from the TLICA axioms; no mathematical novelty or validated predictive power asserted.

## 1. World first; observer model second; label third

Choose an episode/task context c, an external world history w in a declared history set W, a speaker j, a referent r (possibly j), and an observer k. Do not erase distinct speakers, targets, and report sources.

The observer's available trace and interpretation are

$$
y_{k,c}=O_{k,c}(w),\qquad
x_{k,c}=D_{k,c}(y_{k,c};T_{k,t},H_{k,t}),
$$

where O is exposure/measurement, D is reconstruction, T is an observer toolkit, H a history. The recorded **utterance** u is another world event; if it is observed, its reconstruction is a separate internal content x_u. The phrase may describe a feeling, a task trajectory, a social evaluation, or function merely as an insult. None of those are definitionally equivalent.

A term s has **sense-indexed** candidate readings L_{s,a,c,j,r}; there may be several senses a and several candidate mechanisms h. For a finite research catalog of hypotheses H, define a set of explanation candidates compatible with the recorded data E:

$$
C(s,u,c,E)
=\{(a,h)\in H:\mathrm{UseCompatible}(s,u,c,a,h)
\ \land\ \mathrm{EvidenceCompatible}(h,E)\}.
$$

The compatibility predicates are supplied and revisable, **not known psychological truths**. Unknown predictions do not count as falsification. Speech-act type (report, alignment signal, joke, dismissal, accusation) is separately recorded, and the person labeled need not endorse the label.

For each modeled internal content x, canonical TLICA retains its profile and distinct coordinates:
$$
P_{m,t}(x)=\rho_{m,t}(x),\qquad
\kappa_{m,t}(x),\quad\phi_{m,t}(x)\text{ when a pathway exists}.
$$
The mode-resolved vector rho is primary; rho is identity **integration**, not belief certainty, value, or emotional intensity. Kappa is contact, not validation; phi is toolkit-relative truth-indistinguishability, **not an accuracy probability**. If there is no constructible verification path, phi is **undefined**, not zero. Source mapping sigma, phenomenal availability A, probe execution, and slack S are kept separately typed. Neither a person's utterance nor its social reception fixes their phi/rho values.

The proposed lexicon is a *research-tier semantic interface* over existing TLICA dynamics, not a fourth foundational coordinate.

## 2. Observation fibers and elementary impossibility

For a declared finite rival set H and a finite **fully predicted** probe family Q, let
$$
\eta_Q:H\longrightarrow\prod_{q\in Q}Y_q,\qquad
\eta_Q(h)=(q(h))_{q\in Q}.
$$

Define h ~_Q h' iff eta_Q(h)=eta_Q(h'). This is an equivalence relation. A legitimate **operational quotient** H/~_Q exists, indexed by the probes actually fixed; it says **nothing** about whether the candidate catalog includes the true world.

**Proposition 1 (non-identification).** If distinct candidate states h1,h2 have the same observation and disagree on target property F, no function of that observation alone can recover F correctly for both. **Proof:** a function takes equal inputs to equal outputs, but F(h1) != F(h2). This is a standard elementary fact, not an empirical discovery. In particular, identical utterance tokens can be consistent with different mechanisms.

**Corollary (finite compression).** A deterministic coarse label map from more distinct modeled states than available labels must have a collision (pigeonhole principle). Coarse label collisions alone do not establish which rival is right.

**Proposition 2 (fixed-model refinement).** If E' is E plus compatible fixed observations, then C(E') is a subset of C(E). **Proof:** every candidate satisfying all the old and new constraints satisfies all old constraints. This requires the *same catalog, same source interpretation, and immutable valid observations*. New senses, repaired source maps, learned dynamics, or withdrawn testimony legitimately break the premise; real epistemic updating need not be monotone.

**Proposition 3 (contextual non-invariance).** Identical exposed signals need not imply identical labels when decoders differ by observer or context. **Witness:** two observer decoders map the same smile to "warmth" and "courtesy" respectively. This is permitted by the model; to establish that particular phenomenon empirically requires data.

The supplied Python program checks toy examples and finite pair splits; it does not prove Props 1–3 beyond their stated mathematics.

## 3. Why three slang entries need different structures

**Vibe:** observer-indexed *low-dimensional reconstruction*, e.g. a report or action following a coarse map V_{k,c}=Q_{k,c}∘D_{k,c}∘O_{k,c}. Q is an application-level coarse readout, **not** rho or phi. One label can collapse hidden relational differences; prediction: disagreements between observers or later evidence can split a shared vibe label. Avoid presuming the intuition is accurate.

**Cope:** several different objects, not one mechanism: adaptive affect regulation; a proposed self-protective interpretation that fails a credible correction probe; and a speaker's dismissive rhetorical act. A model of defensive reappraisal must separately characterize the reliability of conflicting evidence, a candidate identity-load pathway, the reported response, and a counterfactual corrective probe. Belief preservation is not automatically deception, and a social accusation is never proof of the recipient's mind.

**Lost in the sauce:** possible high attention/immersion, confusion, intoxication, status-capture, absorption, or excessive engagement. High focus occupancy by itself is **not** dysfunction. A research candidate for its disorientation usage combines persistent immersion with independently predeclared **failure to reorient or track a relevant goal** under suitable constraints. Different senses must not be conflated. Some usages are positive.

## 4. Context transport and the categorical moonshot

For communities/contexts c -> d, a translation must declare mappings of utterance conventions and relations, not merely reuse an English string. The testable square is whether:

$$
L_d\circ T^{\text{evidence}}_{c\to d}
\stackrel{?}{=}
T^{\text{label}}_{c\to d}\circ L_c.
$$

The equation is a **candidate naturality/transport requirement**, not a theorem about real slang. Failures may be more interesting than successes: identical labels may mark different structures, and the same structure may be named differently. No full/faithful functor, optic equivalence, sheaf, phase, or new physical law is claimed without explicit objects, maps, composition, and operational probes.

## 5. Non-transports and limits

- A dictionary definition is not a measurement of the author's psyche or the target's identity network.
- A stylized behavioral signature is not a diagnosis and does not identify motive.
- Phi is not confidence/truth probability; rho is not intensity or value; mu is not slack.
- One labeled case cannot authenticate a universal causal pathway.
- The toy catalog cannot certify that no unseen sense or explanation exists.
- An observational split may resolve the toy phi/pathway challenge while the source map sigma is still wrong. Preserve both audits.
