# Cultural Realness: A Contextual Atlas of Partial Transports

Research draft v0.1.0. Author-originated hypothesis; AI-assisted formulation. Empirical mechanism UNVERIFIED. References S1-S10 are defined, with inspection limits, in [SOURCES.md](SOURCES.md).

## 1. Recovering the object

The motivating contrast is not simply between two musical styles. It is between different ways a person can encounter a shared social world. One listener hears an accent, place-name, vocal gesture, or narrative move as a precise indication of a recognizable situation; another may understand the words while missing what is at stake. The conjecture is that part of experienced realness depends on relations between an artifact, acquired interpretive capacities, a person's history, and the immediate listening context.

The unit of analysis is therefore **listener x artifact x context x time**, not a genre or a demographic type. The proposed atlas records contexts and overlapping repertoires without requiring each person to occupy one cultural box. A context record can include cohort, places actually inhabited, networks, institutions, resources, media exposure, and events, subject to consent and relevance. Its dimensions are not presumed independent or equally important.

Keep three claims apart. Two episodes may have selected relations in common. They may also be causally linked through particular institutions or histories. Their participants may report different meanings. None of those claims proves either of the others. The shared-country premise motivates looking for links; it does not supply their provenance. A matched motif is neither an equivalence of suffering nor a whole-person reconstruction.

## 2. Prior work and the remaining question

American regional classification is established work. Louf and colleagues infer regional patterns from geotagged lexical distributions [S1]. Such a map concerns its sampled discourse, not direct access to residents' phenomenology. The numerical corpus details in the preceding conversation are not relied upon here without full methods verification.

Fox's Lockhart ethnography places country music in relations among voice, everyday life, and local experience [S2]. Forman analyzes place and identity in hip-hop [S3]. McLeod studies discursive authenticity distinctions [S4], while Peterson studies the industry's historical construction of country authenticity [S5]. These are neighboring accounts, not evidence that one equation explains all listeners. Armstrong's 1993 comparison specifically addresses violence-related rap/country resemblances [S6]; the pairing itself is not new.

Swidler supplies a repertoire/strategy perspective [S7]. Eckert treats social meanings of linguistic variants as context-sensitive possibilities rather than fixed demographic labels [S8]. Gentner supplies direct formal prior art for mapping relations rather than merely attributes [S9]. Axelrod shows local convergence with global differentiation in a specified agent-based model [S10], not a universal cultural law. The current proposal must beat simpler repertoire, familiarity, analogy, and social-label explanations on held-out observations before claiming additional explanatory value.

## 3. What can feel real?

For measurement, distinguish at least: comprehension of the depicted situation; familiarity with its signs; autobiographical recognition; emotional resonance; perceived performer sincerity; perceived community legitimacy; liking; and factual endorsement. Report a profile, not a single truth score. Interviews must first check whether these distinctions describe participants' own usage of realness.

A listener need not have literally lived a narrative to recognize its structure. Empathetic understanding, imagination, aspiration, deliberate role-play, and exposure to unfamiliar art remain live alternatives. Conversely, an experience can be familiar and disliked. Sound alone can matter: rhythm, timbre, vocal delivery, harmony, and production must not be erased by a lyric-centered design. A genre label can change expectations without changing audio. These possibilities belong in the rival model set, not in a residual category called failure to understand.

The proposed mechanism is conditional: acquired dispositions may make particular signs activate a recognizable configuration of roles, stakes, expectations, and possible moves. An artifact can then feel situated rather than generic. This is a hypothesis about one pathway to resonance, not a necessary or sufficient condition for enjoyment, truth, or market success.

## 4. Dynamics without an invented equilibrium

A schematic update has two directions. A person's exposure history and current situation contribute to perception and action; actions also contribute to other people's subsequent environments. Institutions, material limits, network selection, and media distribution constrain both directions. This schematic leaves update functions unidentified. No convergence rate, fixed point, equilibrium distribution, or unique basin is inferred.

Repeated similarity may be reproduction, repeated external pressure, selection into a setting, or selective observation. Those mechanisms have different intervention predictions. The study should ask whether a disposition persists when immediate context is removed and whether it changes after meaningful new experience. A single context-priming result cannot establish developmental imprinting.

## 5. TLICA reconciliation

Canonical anchor: [foundation File 3](../../foundation/3_formal_apparatus.md), sections 6.3, 7.1-7.4, and 8.7, at the base commit recorded in README. Section 8.7 distinguishes formation from activation and explicitly leaves empirical rates open. It includes cultural and linguistic patterns among the proposed applications of osmotic imprinting. Section 7.4 permits contingent coupling without defining the coordinates as reducible to one another.

The hypothesis can be expressed using existing commitments; it adds no primitive. Kappa is contact through the specified contact/source apparatus, not a rating of emotional force. Rho is historically integrated identity-correlation, not a preference score. Phi concerns toolkit-relative truth-indistinguishability where a verification pathway is constructible; undefined phi is not falsehood. Sigma belongs to the outside-perspective source account, which cannot be replaced by a participant's explicit attribution. Mu concerns the weighting/availability of probes; this dossier does not reuse it as a musical salience variable. Discrimination, comprehension, and resonance are additional application-level readouts, not proxies automatically equal to these coordinates.

The existing acquired-taste note and source-conditioned-meaning dossier motivate representation change and the attribution/imprint distinction. They share project provenance and do not independently validate this extension. No AI/person mechanism identity or consciousness inference is needed.

## 6. Minimal formal object and executable contract

Keep the world event, an artifact's narrated event, a participant's interpretation, and a researcher's coding in separate records. Matching coded graphs establishes a fact about those annotations only. A fictional lyric is not a performer's biography; agreement between coders is not verification of the depicted event. Historical or causal assertions need their own evidence paths.

Let E=(V,k,l,F,b,p) be a finite annotated episode: nodes V, declared node kinds k, surface labels l, signed directed facts F, a declared predicate basis b, and provenance p. A fact (u,r,v,+1) asserts relation r; polarity -1 explicitly denies that relation in this annotation frame. Polarity is not emotional valence, morality, or a phase. Disputed observations require separately retained annotation alternatives.

A candidate bridge f:D -> V' is a partial injection preserving node kinds and using the same declared predicate basis. Only source facts whose endpoints both lie in D are eligible. A target observation of the transported fact with equal polarity is a match; opposite polarity is a contradiction; no observation is unknown. Reversing an edge does not logically negate the original relation.

The validator reports mapped-node counts, tested-fact counts, matches, contradictions, unknowns, and unexamined target facts. A bridge with no eligible facts is insufficient evidence, not a perfect match. The common basis and provenance strings are declarations, not independently verified semantics. The current instrument validates supplied structure; it does not infer how people actually encode an experience.

### Proposition 1: surface projections cannot identify all relational differences

Let L(E) retain only the multiset of surface labels. Construct E+ and E- with identical nodes and labels but opposite recorded polarity on one relation. Then L(E+)=L(E-), while the declared identity bridge contradicts that fact. Every deterministic classifier using only L gives the same output on both. It therefore cannot correctly recover that differing relation in both cases. This is an elementary information-loss counterexample, not a new impossibility result about rich language models or embeddings.

### Proposition 2: the exact partial transports compose

Within a fixed predicate basis, call f fact-preserving when every eligible observed source fact is present with equal polarity in its target. Given two such partial injections f:E -> E' and g:E' -> E'', define D(gf)={v in D(f): f(v) in D(g)} and (gf)(v)=g(f(v)). It is injective and kind-preserving. An eligible source fact is transported by f to an observed target fact; its endpoints belong to D(g), so g transports it with the same polarity again. Thus gf is fact-preserving. Function composition is associative and identity maps preserve every observed fact.

This earns a small category of annotated episodes and partial fact-preserving injections. It does not earn a category of cultures as complete lived worlds. Scope can shrink under composition. The empty map is mathematically vacuous but never counted as empirical support. A forward fact-preserving map need not reflect extra target facts, so it is not generally an isomorphism.

### Proposition 3: matched observation is weaker than matched intervention

Two finite models can assign the observed action stay the outcome paid, while assigning the unobserved action leave different outcomes: unpaid and dismissed. On the observed action they agree exactly. Their counterfactual tables disagree. Hence matching the observed record, or a coarser motif extracted from it, cannot establish agreement of the complete action-outcome model. The calibration explicitly instantiates this counterexample; neither model is fitted to a real workplace.

## 7. What was executed, and what was not

The bootstrap implements the declared bridge contract with strict schema checks. Twenty-eight unit tests cover identity, relabeling, polarity changes, missing facts, reversal, partial coverage, target extras, invalid maps, predicate-basis mismatch, malformed JSON, and command-line roundtrips. Calibration evaluates all four surface-same/different x structure-same/different cells, all 24 renamings of four node identifiers, and four single-fact polarity mutations. It preserves raw per-fact outputs in RESULTS.json.

Structural matching is deliberately invariant to surface labels. Recovering that invariance verifies code behavior; it does not show that listeners are invariant to surface, and the four cells do not estimate a psychological interaction. All fixtures were authored for calibration. There is no empirical holdout, independent coder, trained learner, or corpus result.

## 8. The next discriminating move

First test whether independently produced annotations can preserve meaningful disagreement while identifying useful correspondences. Freeze the rubric and candidate bridges before revealing cross-context pairs to an evaluator. Compare a relation-only, surface-only, combined, and genre-label baseline; reserve new participants and artifact families for confirmation. Collect comprehension and resonance separately. A bridge that improves comprehension but not felt realness would support a narrower translation benefit while failing the proposed resonance mechanism.

A cultural sheaf remains an optional future construction. Overlap alone supplies neither restriction maps nor a gluing theorem. Pairwise resemblance need not be a compatible family of sections. No claim about absent global sections or cultural cohomology is made. The immediate research value lies in accountable partial translation: retaining exactly what matches, what changes, what was not observed, and whose interpretation supplied each annotation.
