---
title: "Agency Architecture in the Two-Layer Identity-Correlation Architecture"
subtitle: "Verification-Toolkit, Variation, and Empirical Interface"
author: "Companion paper to *Free Will*; v0.3.0 — Layer 8 (Third Application, split B)"
date: "May 2026"
lang: en-US
papersize: letter
geometry: margin=0.85in
fontsize: 10pt
toc: true
toc-depth: 2
colorlinks: true
linkcolor: black
urlcolor: black
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
header-includes:
  - \usepackage{microtype}
  - \usepackage{booktabs}
  - \usepackage{longtable}
  - \usepackage{array}
  - \usepackage{parskip}
  - \usepackage{fvextra}
  - \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
  - \DefineVerbatimEnvironment{verbatim}{Verbatim}{breaklines}
  - \setlength{\emergencystretch}{3em}
  - \sloppy
---

**Status:** Application paper, v0.3.0 — Layer 8 (Third Application, split B). Companion to *Free Will in the Two-Layer Identity-Correlation Architecture: Six Conditions, Manipulation, and Framework Translations* (split A).

**Source:** Derived from `refined_agency_paper_v0_2_3_A_status_patch_propagated.md`. The v0.2.3 paper combined free-will-philosophical and agency-structural material into a single ~200-page document; v0.3.0 splits that material into two companion papers for readability while preserving all content.

**This paper covers:** order-indexed willing (foundational and constructed orders), the verification-toolkit and live-option construction lemma, will/trying/effort as operator-bundle direction under resistance, decision-events and order-asymmetric Mode B reflective availability, the seventeen-family variation taxonomy with ten-axis diagnostic schema, the triadic responsibility-attribution apparatus including the ten-component attribution profile, the empirical interpretation profile and timing-marker non-identity chain, the eighteen formal predictions across seven families with seven backbone predictions, and the agency-domain open-problem catalogue.

**Companion paper covers:** the six-condition definition of free choice and three-tier configuration; the manipulation paradigm with explicit ownership / sourcehood dissociation; eight framework translations under translation-not-refutation discipline; foundation-level metaphysical residue (ultimate sourcehood, primal not-I, lawful-frame, theological resonance, contemplative no-agent translation, source-sensitive Frankfurt-class descendants, self-determination theory). The companion paper supplies the canonical free-choice definition that this paper's variation taxonomy and attribution apparatus depend on.

**Builds on:** Foundation document set v5.3.3 (Files 0–5); first application paper, *Temporal Phenomenology* (File 6); second application paper, *Differentiated Affect* (File 7); companion paper *Free Will in the Two-Layer Identity-Correlation Architecture* (split A).

**Cross-reference convention:** Internal references (e.g., §4.4) refer to sections within this paper. References to the companion paper are written explicitly: "[Free Will §3.2]", "[Free Will Paper §5.7]", etc. References to the Foundation are written as "Foundation File N, §X.Y" or "Foundation v5.3.3 §X.Y".

**Methodological note:** This paper takes the six-condition definition of free choice (developed in the companion paper) as its structural anchor and derives the rest of the agency taxonomy by structural variation. The architecture's claim is that free choice is the canonical case from which all other agency configurations — manipulation, akrasia, compulsion, addiction-like capture, ADHD-like implementation gap, learned helplessness, dissociation, alienated action, apparent choice, skilled flow, leadership, institutional action, and many others — are derived as structural modifications of the six conditions, the order-engagement profile, the source-status overlay, the developmental-window status, or the cascade structure. The paper is implementation-neutral on substrate-metaphysics within a lawful-frame qualifier; predictive coding, executive control, accumulator dynamics, and embodied or extended-cognition implementations remain open candidates rather than reductions.

# Split-derivation note

This is split B of v0.3.0, derived from v0.2.3 (`refined_agency_paper_v0_2_3_A_status_patch_propagated.md`).

The v0.2.3 paper interleaved the philosophical contribution to the free-will debate with the structural / empirical / clinical apparatus for analyzing agency variations more broadly. While the methodology is genuinely unified — free choice is the canonical case from which the rest of the agency taxonomy is derived — the resulting ~200-page document was difficult to engage in one read. v0.3.0 splits the material as follows:

**Split A (companion paper, *Free Will*):** the philosophical core — six-condition definition, manipulation paradigm, framework translations, metaphysical residue. Self-contained for readers approaching the architecture from the free-will literature.

**Split B (this paper, *Agency Architecture*):** the structural and empirical core — orders of willing, verification-toolkit, will / effort / decision dynamics, the seventeen-family variation taxonomy, attribution apparatus, empirical interpretation, eighteen formal predictions, and the open-problem catalogue. References the companion paper for the canonical free-choice anchor; otherwise self-contained.

No content has been removed in the split. Sections, subsections, tables, examples, and worked cases are preserved verbatim from v0.2.3 (which itself preserved all v0.1.16.1 content; see the v0.2.3 traceability appendix). What has changed:

- Renumbering of top-level sections (§3 in this paper is a compact reference to the companion's §3; §4-§11 retain their original numbering; §13 → §12; §14 → §13).
- New abstracts, introductions, and conclusions, each focused on the split's specific contribution.
- Cross-references to material now in the companion paper are flagged as such.
- The glossary is split: each paper carries the subset of terms relevant to its content.
- Patches and corrections from v0.2.2 (A-status patch) and v0.2.3 (propagation completion) are preserved exactly as in v0.2.3.

Readers wanting the full unified document should use v0.2.3.


# 1. Abstract

This paper develops the structural taxonomy of agency variation, attribution apparatus, empirical interface, and predictions that build on the Two-Layer Identity-Correlation Architecture (Foundation v5.3.3) and the six-condition free-choice definition presented in the companion paper *Free Will in the Two-Layer Identity-Correlation Architecture*. The free-choice definition supplies the canonical case from which all other agency configurations are derived as structural variations. The architecture treats agency as an inside-perspective structural configuration anchored in the indexed modeling I, organized through order-indexed willing across foundational orders (focus, thought, substrate-mediated action) and constructed orders (asking, directing, team coordination, institutional engagement, and beyond) developed through toolkit-development and mastery.

The paper's principal contributions: the verification-toolkit as application-level apparatus and the live-option construction lemma with its four failure modes; will, trying, and effort as operator-bundle direction under resistance with the eight-source resistance taxonomy and effort-economy across direct, configurational, and slingshot willing strategies; decision-events as operator-bundle selection-events with order-asymmetric Mode B reflective availability and the post-hoc-recognition / source-opacity / confabulation triad; a seventeen-family variation taxonomy with a ten-axis diagnostic schema covering thin agency, constrained choice, omission and veto, akrasia, habit, compulsion and addiction, ADHD-like implementation-gap configurations, deliberation-pathologies, learned helplessness, affect-mediated agency contraction, dissociation, apparent choice and confabulation, manipulation and source-compromise, constructed-order variations, skilled flow, reflexive action, and compound configurations; the triadic responsibility-attribution apparatus dissociating ownership, responsibility, and accountability through the ten-component attribution profile $AP_{m,t;a}$ (the manipulation-specific subset of this apparatus is developed in the companion paper); the empirical interpretation profile $EIP_p$ that maps Libet-, Wegner-, and Soon-class paradigms to specific architectural objects through a timing-marker non-identity chain ($t_{prep} \not\equiv t_{select} \not\equiv t_{report} \not\equiv t_{move} \not\equiv t_{outcome} \not\equiv t_{recognize}$); eighteen formal predictions across seven families with seven backbone predictions ($PP_i$ profile, pressure conditions, exclusions, and prediction-by-framework discriminators); and a research-program catalogue of fifteen open problems with priority map.

The architecture is implementation-neutral on substrate-metaphysics within the lawful-frame qualifier, perspectivally realist about other agents, and honest about its scope: it supplies structural inputs to attribution, empirical interpretation, and prediction without normative-sufficiency closure or metaphysical completeness. The companion paper *Free Will in the Two-Layer Identity-Correlation Architecture* develops the philosophical contribution that this paper's structural taxonomy presupposes: the six-condition definition, the manipulation paradigm and ownership / sourcehood dissociation, eight framework translations, and the foundation-level metaphysical residue that the architecture acknowledges as principled limits.

**Keywords:** agency; verification-toolkit; live-option construction; will; trying; effort; decision; Mode B; variation taxonomy; attribution; ownership; responsibility; accountability; Libet; Wegner; Soon; predictive coding; predictions; Two-Layer Identity-Correlation Architecture


---

# 2. Introduction: from free choice to the agency taxonomy

This paper develops the structural taxonomy of agency that the companion paper's six-condition definition of free choice anchors. The methodology is definition-anchored taxonomic construction by structural variation: free choice proper supplies a canonical base configuration from which every other agency configuration is derived as a structural modification. By relaxing one or more of the six conditions, narrowing the order-engagement, compromising the source-pathway, restricting Mode B availability, weakening ownership-integration, or introducing cascade dependencies, the rest of the agency landscape becomes structurally specifiable: thin agency, constrained choice, akrasia, compulsion, ADHD-like implementation gap, learned helplessness, dissociation, apparent choice, manipulation, skilled flow, and many others.


## 2.1 The problem with "the problem of free will"

Consider an agent who chooses wholeheartedly from an option-space that another agent has quietly shaped. The action feels owned. It expresses real priorities. It integrates seamlessly into the agent's lived sense of self. It meets every internal condition the agent could check from the inside: live alternatives were considered, reasons were weighed, the chosen option resonated with the agent's values, the act issued from those values rather than from intrusive impulses. By any first-person measure available to the agent in the moment, the choice was free. Yet the option-space itself was source-compromised: the alternatives among which the agent deliberated had been engineered by another agent's interests, and the agent did not know this.

A theory that asks only "Did the agent act freely?" or "Was the choice theirs?" flattens this case. The available answers — *yes*, *no*, *yes but constrained* — are too coarse to capture what is structurally true: ownership is intact while sourcehood is compromised; the agent's reflective endorsement of the action is real while the upstream shaping of the option-space remains hidden; responsibility may be partial along several dimensions; accountability for repair may still obtain even where original-act responsibility is reduced. Each available framework can capture some of these features at the cost of losing others. Compatibilist endorsement-only accounts capture the genuine ownership but risk over-attributing responsibility. Hard-incompatibilist ultimate-sourcehood accounts capture the source-compromise but risk erasing the real ownership that remains. Illusionist or report-fallibility accounts can capture the limits of introspective access but typically do not distinguish source-compromised-but-owned action from confabulated or alienated action. Phenomenological and wisdom-tradition accounts can illuminate the lived experience but do not yet supply apparatus for tracking the dissociations themselves.

The difficulty is not that any of these accounts is wrong. The difficulty is that the question they share — *was this an exercise of free will?* — bundles too many structurally distinct issues into a single verdict. Live-option construction, evaluative engagement, operator-bundle selection, substrate coupling, reflective availability, ownership-integration, source-status, developmental-window status, cross-order coordination, cascade effects, empirical-marker interpretation, responsibility-attribution, accountability for repair, and phenomenological integrity are not one property. They are a structured family of dissociable relations. The free-will literature recurrently forces them through a single contested label, and the resulting debate has the shape of an unresolvable trichotomy: powerful arguments on each side, none compelling the others, all turning on intuitions about a single property whose internal structure remains unanalyzed.

This paper proposes a different move. Instead of arguing for or against any of the standard positions, it replaces the single contested property with a structural architecture. Ownership, source-status, responsibility, accountability, Mode B reflective availability, condition-failure modes, order-engagement profiles, and cascade-attribution become dissociable relations that can be tracked separately and recombined without zero-sum collapse. The classical debate is not refuted or absorbed; its components are decomposed into structurally specifiable distinctions, each available for separate philosophical, empirical, and practical engagement. The architecture's promise is not that "free will is real" or "free will is illusory" but that the question becomes structurally analyzable once its components are given independent analytical apparatus.

As an orientation-level illustration rather than a completed attribution analysis, the manipulation case can be parsed using the architecture's apparatus as follows: ownership-integration is intact (the action expressed the agent's evaluative profile); sourcehood is compromised (the option-space was upstream-shaped); ownership-recognition by the agent is unimpaired (no alienation report); Mode B reflective availability is intact for the chosen action but not for the source-shaping pathway; responsibility-attribution for the act in question is qualified by the source-compromise rather than settled by ownership alone, with the full attribution profile determining whether and how original-act responsibility is reduced; accountability for explanation, mitigation, or future repair may obtain despite the source-compromise. None of these claims requires the manipulation case to be either a genuine exercise of free will or a non-exercise of agency. The case is what it structurally is — a particular configuration of profile-values along several dissociable axes — and the architecture's job is to make that configuration analytically tractable. The same disposition extends across all the configurations the literature has called "free," "unfree," "compelled," "manipulated," "alienated," "automatic," "chosen," and "wholehearted." Each is a distinct structural configuration; none is a single binary verdict.


## 2.2 The architectural wager: agency as inside-perspective structure

The architecture's positive stance is that agency is best understood as an inside-perspective structural configuration anchored in the indexed modeling I. The primary object is not behavior viewed from third-person observation, not neural readiness signals, not folk responsibility judgments, and not a metaphysical power added to the substrate. It is the I-relative agency profile: the configuration of live-option construction, evaluative engagement, operator-bundle selection, substrate coupling, Mode B reflective availability, ownership-integration, and identity-correlation that obtains at any moment across the agent's developed orders of willing. This profile operates under what the paper calls the lawful-frame qualifier — the minimal structural regularity required for the architecture's coordinates and persistence relations to be definable — but the architecture takes no further position on whether the substrate is deterministic, stochastic, or otherwise. Implementation candidates from neuroscience and cognitive science remain open; they are not reductions of the architecture's structural object.

The inside-perspective commitment is load-bearing. The architecture is perspectivally realist about other agents and can analyze collective and institutional structures through role-indexed profiles and relational cascades, without positing an unindexed group mind. It refuses to collapse the first-person structural reality of agency into third-person control-system variables, neural correlates, or social-attribution practices, while remaining open to mapping these as implementation candidates or empirical markers of architecturally specified objects. The architecture's task is to describe agency as it is structurally available from the inside, with apparatus precise enough to engage external paradigms without being reduced by them.

This stance is not new to this paper. The Two-Layer Identity-Correlation Architecture, established in Foundation v5.3.3, introduces the inside-perspective discipline at the foundation level: the indexed modeling I as primitive anchor; identity-correlation $\rho$ as the relation by which contents are integrated with the I; the verification-toolkit as the developed capacity that constructs, evaluates, and inhabits available contents; the foundation's three coordinates $\kappa$ (contact), $\phi$ (truth-indistinguishability; in this paper's affect-and-agency contexts the operational gloss "source-pathway / truth-verification access" is also used), and $\rho$ (identity-correlation); the foundation-named preservation-ranking $\Pi$, which the foundation introduces as a placeholder for application-level formalization (Foundation File 2 §4.8) and which this paper develops as an application-level coordinate-grade object distinct from $\rho$; together with the phenomenal-availability status predicate $A_{m,t}(x)$; the prerogatives $PtCns$ (consistency) and $PCE$ (continued existence); and the three modes of I-development (A, B, C). Two prior application papers — *Temporal Phenomenology* (Application 1) and *Differentiated Affect* (Application 2) — have already extended that foundation to specific phenomenal domains, showing how the inside-perspective architecture can support structural accounts of temporal experience and love-anchored affective configurations without requiring new foundation-level primitives.

The present paper is the third application. It applies the same foundation to agency, and like its predecessors it adds no new foundation-level primitives. What it does add at the application level are four section-level structural objects that perform separate analytical work — the attribution profile, the empirical interpretation profile, the prediction profile, and the framework translation profile — each tailored to one of the agency domain's distinctive analytical tasks. These objects are introduced where they are needed (Sections 9 through 12) and are not interchangeable; the paper's analytical leverage depends on keeping them distinct.


## 2.3 Why free choice is the canonical case

Free choice proper serves as the paper's definitional anchor. This is a methodological choice, not a metaphysical privilege. Free choice is the configuration in which the architecture's structural commitments are most fully exercised and therefore most visible: all six interdependent conditions of free choice hold simultaneously — contrastive live-option construction by the verification-toolkit, evaluative engagement, operator-bundle selection, non-preemptive substrate coupling, non-confabulatory Mode B reflective availability, and ownership-integration — across one or more orders of willing. When all six conditions are active, the structural roles that distinguish free choice from compelled, manipulated, automatic, or thinner agency-configurations are maximally legible. From that fully-exercised case, every other configuration in the agency taxonomy can be derived by structural variation: by relaxing a condition, narrowing the order-engagement, compromising the source-pathway, restricting Mode B availability, weakening ownership-integration, or introducing cascade dependencies.

The choice of free choice as anchor is therefore architectural rather than evaluative. The paper does not claim that free choice is morally superior to thinner agency forms, that wholehearted free choice is always preferable to free selection, or that agency events failing to satisfy all six conditions are defective. The three-tier configuration the paper develops — *free selection*, *free choice proper*, and *wholehearted free choice* — names three genuine configurations that exercise different subsets and depths of the same six conditions. Free selection is a thin but real exercise of agency; wholehearted free choice is a deeply integrated exercise; free choice proper sits between them as the configuration in which all six conditions are present without further integration-depth requirements. None of these tiers is ranked above the others as a normative ideal. The architecture's job is to make their structural distinctness specifiable.

This canonical-case methodology mirrors the pattern established in *Differentiated Affect*, where love at constitutive-extension topology served as the canonical case from which the broader affect taxonomy was derived. The choice of love there was likewise architectural: love made the foundation's coordinates maximally legible for the affect domain. Free choice plays the same role here for agency. The paper begins not because every agency event is a free choice, but because free choice is the configuration in which the architecture's six conditions, three-order generalization (foundational orders 1, 2, and 3, plus constructed orders 4 and above through toolkit-development and mastery), and structural-variation methodology can be introduced without ambiguity. The rest of the agency landscape — including agency-pathologies, manipulation, addiction, akrasia, alienation, automatic action, habituated routine, skilled flow, group action, and institutional roles — is then derived by controlled structural variation rather than by independent definition or by symptom-cataloguing.


## 2.4 Methodology and discipline

The paper follows a single methodological template: definition-anchored taxonomic construction by structural variation. Free choice proper supplies the base definition. Every other agency configuration is derived by modifying one or more of the six conditions, the order-engagement profile, the source-status overlay, the developmental-window status, or the cascade structure. This approach guarantees that the taxonomy remains internally consistent with the foundation and that variations remain structurally specifiable rather than gestural. It also enforces a discipline: variation-families are introduced only where the architecture's parameters genuinely diverge, not wherever folk-psychological vocabulary suggests a new category.

Five further disciplinary commitments govern the entire paper:

**Inside-perspective architecture.** Agency is analyzed from the first-person structural configuration of the modeling I. The architecture is perspectivally realist about other agents and can analyze role-indexed profiles, relational cascades, and institutional structures, but it refuses group-mind reification. Multi-agent and group cases are decomposed into indexed agent-profile sets plus relational structure, not aggregated into a single unindexed perspective.

**Implementation-neutrality within lawful-frame qualifier.** The paper takes no position on whether the substrate is deterministic, stochastic, or indeterministic. It requires only enough structural regularity for the architecture's coordinates, profiles, persistence relations, and substrate-mediation pathways to be definable. Specific implementation routes — predictive coding, executive control, accumulator models, neural network dynamics, embodied or extended-cognition implementations — remain open as candidates. None is treated as a reduction of the architecture's structural object; the architecture's commitments do not depend on any particular implementation succeeding.

**Distinct section-level structural objects.** The paper introduces four application-level structural objects — the attribution profile $AP_{m,t;a}$ (Section 9), the empirical interpretation profile $EIP_p$ (Section 10), the prediction profile $PP_i$ (Section 11), and the framework translation profile $FTP_f$ ([Free Will §5]). Each performs a different analytical task: attribution, paradigm-mapping, prediction-promotion, and framework-translation respectively. The paper's analytical leverage depends on keeping these objects distinct rather than collapsing them into a single unified profile-schema. The architecture's unity is at the level of the foundation's I-relative agency field; the analytical specificity is at the level of these four section-level objects.

**No new foundation-level primitives.** The paper introduces no new commitments at the foundation level. Every architectural commitment traces back to Foundation v5.3.3's three coordinates, the indexed modeling I, $PtCns$ and $PCE$, Modes A/B/C, the verification-toolkit, identity-correlation $\rho$, and the three-order pathway typology. Where this paper develops $\Pi$ as a coordinate-grade application-level architectural object, this is application-level work the foundation explicitly licenses (Foundation File 2 §4.8: "formal development of $\Pi_{m,t}$ as an architectural object distinct from $\rho$ is application-level work"); it is not a new foundation primitive. The paper's contribution is application-level: it shows that the foundation's apparatus, applied to the agency domain through the four section-level structural objects, yields a structurally precise account of free choice, agency-variation, responsibility-attribution, empirical interpretation, prediction, and framework translation.

**Boundary discipline.** The paper does not claim to solve the metaphysical problem of free will, prove compatibilism, refute hard incompatibilism, deliver moral or legal verdicts, reduce agency to neural implementation, claim that the architecture is a synthesis of existing frameworks, or license clinical or therapeutic application beyond research predictions. It supplies structural inputs to responsibility-attribution, empirical interpretation, and philosophical translation, not normative-sufficiency closure or metaphysical completeness. Section 12 catalogues principled limits the architecture acknowledges as outside its scope rather than deferring as eventually-solvable. §13 returns to the transformation framing without claiming metaphysical closure.

These commitments are stated here so that subsequent sections can operate within them without repeated rehearsal.


## 2.5 What this paper builds

Within these methodological commitments, this paper constructs a structural account of agency organized around the following architectural elements. Section 3 supplies a compact reference to the canonical free-choice definition (full development is in the companion *Free Will* paper). Section 4 develops the bridge from free choice to the broader agency taxonomy: the agency criterion, the three orders of willing in full detail with constructed-order extension, the universal toolkit constraint, the agency derivation schema using foundation coordinates, the $\rho$/$\Pi$ separation that becomes load-bearing for responsibility-attribution, the developmental-window overlay, the apparent-I / other-I apparatus, and osmotic imprinting in manipulation and propaganda. Section 5 develops the verification-toolkit and the live-option construction lemma. Section 6 develops will, trying, and effort. Section 7 develops deliberation, decision, and order-asymmetric Mode B reflective availability. Section 8 develops the seventeen-family variation taxonomy with ten-axis diagnostic schema. Section 9 builds the triadic responsibility-attribution apparatus through the ten-component attribution profile $AP_{m,t;a}$. Section 10 supplies the empirical interpretation profile $EIP_p$ that maps empirical paradigms to architectural objects. Section 11 promotes operationalization candidates into eighteen formal predictions through the prediction profile $PP_i$. Section 12 catalogues open problems specific to the agency domain. Section 13 synthesizes the structural and empirical contribution.

What this paper does *not* build is the full philosophical engagement: the manipulation-paradigm analysis with explicit ownership / sourcehood dissociation, the eight framework translations under translation-not-refutation discipline, and the foundation-level metaphysical residue. Those occupy the companion *Free Will* paper, and this paper presupposes them where its structural commitments touch the philosophical literature directly. The two papers are companions, not alternatives.

## 2.6 How this paper is organized

The paper proceeds in four movements. Sections 3 through 8 build the structural architecture: a compact free-choice anchor, the bridge to the broader agency taxonomy, the verification-toolkit and live-option construction, will and effort and trying, deliberation and decision and Mode B, and the variation taxonomy. Sections 9 through 11 develop the analytical apparatus: the triadic responsibility-attribution apparatus, the empirical-interface mapping, and the prediction promotion. Section 12 catalogues open problems specific to the agency domain. Section 13 synthesizes the paper's contribution.

| Section | Architectural function |
|---|---|
| 3 | Compact reference to the canonical free-choice anchor (full development in the companion paper) |
| 4 | Bridges free choice to the wider agency taxonomy: agency criterion, three orders of willing in detail with constructed-order extension, universal toolkit constraint, agency derivation schema using foundation coordinates, $\rho$/$\Pi$ separation made load-bearing for responsibility, developmental-window overlay, apparent-I / other-I apparatus, osmotic imprinting in manipulation |
| 5 | Develops live-option construction: verification-toolkit mechanics, live-option lemma and failure modes, toolkit-development and mastery, output-imprinting cascade, N-order will and action-space lattice, willing-strategies (direct, configurational, slingshot), manipulation continuum |
| 6 | Analyzes will, trying, and effort: operator-bundle direction under resistance, resistance taxonomy, effort-economy across willing-strategies, mastery dynamics, effort / agency-quality separation, cascade-management |
| 7 | Develops deliberation, decision, and Mode B: decision events, order-asymmetric Mode B reflective availability, post-hoc recognition / source-opacity / confabulation triad, decision / trying / action / outcome distinctions |
| 8 | Derives the variation taxonomy: seventeen variation-families and ten-axis diagnostic schema, with worked compound configurations including ADHD-like, addiction-like, and dissociative-like cases |
| 9 | Builds the triadic responsibility-attribution apparatus: $AP_{m,t;a}$ ten-component profile, ownership / responsibility / accountability dissociation, source-status overlay, developmental-window overlay, cascade-attribution test, profile-indexed rather than zero-sum attribution. The manipulation-specific subset of this apparatus is developed in the companion paper as part of its philosophical engagement |
| 10 | Maps empirical paradigms to architectural objects: $EIP_p$ eight-component profile, Libet / Wegner / Soon-class paradigm mapping, timing-marker non-identity chain, bad-inferences guardrail, falsification patterns |
| 11 | Promotes eighteen formal predictions across seven families: $PP_i$ seven-component profile, seven backbone predictions (P1, P5, P8, P9, P10, P14, P18), pressure conditions, exclusions, prediction-by-framework discriminator |
| 12 | Catalogues agency-specific open problems with priority map (the foundation-level metaphysical residue and theological resonance are catalogued in the companion paper) |
| 13 | Synthesizes the paper: structural coherence, empirical tractability, agency-domain open problems, book-projection handoff, and final synthesis |

Sections 1 (abstract) and 2 (this introduction) are drafted last from the fully-developed paper; the glossary subset compiles terminology relevant to this paper.


## 2.7 Scope and limits

The paper is precise about what it does and does not do.

| The paper does | The paper does not |
|---|---|
| Define free choice proper through six interdependent conditions and three-tier configuration | Prove libertarian metaphysical freedom |
| Build a structural agency taxonomy by definition-anchored variation | Reduce agency to neural, behavioral, or social-attribution variables |
| Supply the triadic ownership / responsibility / accountability apparatus | Assign moral, legal, or theological verdicts in any specific case |
| Promote discriminating empirical predictions with pressure conditions | Claim that the existing empirical literature has confirmed the architecture |
| Translate eight alternative frameworks through $FTP_f$ profiles | Refute, absorb, or synthesize any framework into the architecture |
| Identify open problems with priority and work-type classification | Solve ultimate sourcehood, lawful-frame grounding, or theological questions |

The paper's aim is structural transformation of the problem-space, not final metaphysical closure. The classical free-will debate is not refuted; it is decomposed into structurally specifiable distinctions, each available for separate engagement. Some of the questions the architecture leaves unanswered — ultimate sourcehood, primal not-I dependence, lawful-frame grounding, neural implementation, normative sufficiency — are *principled limits* the architecture acknowledges as structurally outside its scope rather than deferring as eventually-solvable. Others are research-program targets that future application papers, foundation extensions, or empirical collaborations can engage. The architecture is honest about its scope: it supplies structural inputs to responsibility-attribution, empirical interpretation, and framework translation, not normative sufficiency or metaphysical completeness.

The architecture preserves agency's lived complexity, felt depth, phenomenological integrity, and practical stakes. What changes is that we now have apparatus for analyzing it. §13 returns to the transformation framing once the apparatus has been constructed and tested across the agency domain.

---



---

# 3. Free choice anchor: a compact reference

The structural taxonomy this paper develops is anchored in the six-condition definition of free choice. The full development of that definition — the three-tier configuration (free selection / free choice proper / wholehearted free choice), the choice-process stack diagram, the order × condition matrix, the necessity and sufficiency analyses, the lawful-frame qualifier, the manipulation paradigm with explicit ownership / sourcehood dissociation, and the eight framework translations — occupies the companion paper *Free Will in the Two-Layer Identity-Correlation Architecture*. This section reproduces the canonical statement and the six conditions in compact form, sufficient to anchor the rest of this paper. Readers wanting the philosophical development should consult the companion paper.

## 3.1 The canonical statement

Free choice proper is the configuration in which all of the following hold across one or more orders of willing:

1. **Contrastive live-option space.** The verification-toolkit has constructed at least two structurally distinguishable live courses for the I, including withholding, refusal, delay, or non-action where those are genuinely representable, inhabitable, and implementable.
2. **Evaluative engagement.** PtCns (over frame-coherence), PCE-over-projection (over preservation-implications), $\Pi$-weighting (over preservation-priority), or frame-relevance evaluation engages with the option-space.
3. **Operator-bundle selection.** The selection emerges from the operator-selection bundle: the application-level coordinated activity comprising PtCns, PCE-over-projection, $\Pi$-ranking, focus, substrate-readiness, and Modes A/B/C where relevant.
4. **Substrate coupling without preemption, bypass, or capture.** The substrate-host supplies readiness, affordance, motor capacity, and implementation conditions, but does not preempt (produce action before operator-bundle selection), bypass (produce action through substrate pathway without entering live-option selection), or capture (exert pull so dominant that alternatives are not live from inside).
5. **Non-confabulatory Mode B reflective availability.** The choice-process can be taken as object by Mode B under intact conditions without requiring confabulation.
6. **Ownership-integration.** The selected option is integrated into the lived-I profile as the I's action — PtCns-endorsed — rather than as alien, merely undergone, externally inserted, or dissociatively produced.

The conditions are not a checklist of independent items. They are interdependent specifications of a single configuration. Failure at any condition is a structurally specific failure that propagates through the rest, producing one of the variation-families this paper develops in §8.

## 3.2 The three-tier configuration

The architecture distinguishes three structural tiers of choice along an integration gradient:

- **Free selection** — the thinnest tier. The toolkit constructs an option-space, the bundle produces a selection, the substrate implements it, Mode B reflective access remains available, and the action is owned, but evaluative engagement may be implicit, minimal, or absent. The Libet-paradigm spontaneous flex, the diner choosing one of two equally-attractive desserts, the routine skilled execution where evaluation is minimal — these are free selections.
- **Free choice proper** — the substantive middle tier. All six conditions hold without further integration-depth requirements. This is the configuration the philosophical free-will literature most often has in mind when it speaks of free choice.
- **Wholehearted free choice** — the deepest tier. All six conditions hold *and* the selected option is in deep $\Pi$-alignment with the I's preservation-priorities — the choice expresses the I's most centrally-held commitments.

The three tiers are *not* a hierarchy of value. Each is a genuine configuration appropriate to its content domain.

## 3.3 The three orders of willing

The six conditions apply across order-indexed domains of willing:

- **First-order willing** (focus): direction of attentional engagement.
- **Second-order willing** (thought): direction of cognitive operation, deliberation, projection.
- **Third-order willing** (substrate-mediated action): direction of bodily, motor, or substrate-mediated implementation.
- **Constructed orders** ($n \geq 4$): asking, directing, team coordination, institutional engagement, and beyond — developed through toolkit-development and mastery in target-domains.

The abstract structure of free choice is invariant across orders; what varies is the implementation semantics. Section 4 develops orders in full detail; Section 5.7 develops the N-order generalization; Section 8 derives variation-families that engage specific orders or order-combinations.

## 3.4 Onset and exercise patterns

Free choice is exercised in different temporal patterns: spontaneous (conditions met without explicit deliberation), deliberative (conditions met with explicit Mode B engagement), skilled free action (cross-order coordinated with second-order Mode B available but not exercised at the moment of action), veto/withholding (selection of a live withholding-pathway), and post-hoc recognition (conditions met at the time of action with $\phi$-construction emerging only later). The companion paper develops these patterns; this paper takes them as given.

> *Readers wanting full development of the six-condition definition, the necessity and sufficiency analyses, the lawful-frame qualifier, the manipulation paradigm, the framework translations, and the foundation-level metaphysical residue should consult the companion paper [Free Will §3, §4, §5, §6]. The remainder of this paper takes the six-condition definition as the structural anchor and derives the broader agency taxonomy by structural variation.*


---

# 4. The bridge: from free choice to the agency taxonomy

With the structural definition of free choice in place, the bridge to the rest of the agency taxonomy can be stated. Section 4 does the methodological work that the cluster sections rely on: it makes the affect-and-agency parallelism explicit, articulates an agency criterion that distinguishes agency from non-agency processes that nonetheless involve the I, identifies the structural relations that organize the rest of the agency space, develops the three orders of willing in full detail, states the universal toolkit constraint that connects the orders, develops order-specific pathology and therapy taxonomies as immediate applications, provides the agency derivation schema by which any agency configuration can be classified, makes the $\rho$/$\Pi$ separation load-bearing for responsibility, threads developmental-window distinctions into responsibility-attribution, and applies the apparent-I / other-I apparatus and the foundation's osmotic-imprinting mechanism to accountability, coercion, and manipulation. The rest of the paper depends on this section's apparatus, in approximately the same way that the affect paper's Sections 5–9 depended on its Section 4.

## 4.1 Affect-and-agency parallelism

The affect paper anchored on love at constitutive-extension topology and developed the rest of the affective space by structural variation. The agency paper anchors on free choice at full structural development and develops the rest of the agency space by structural variation. The parallelism is *structural, not nominal* — neither paper claims that affect and agency are parallel phenomena, only that the methodology of definition-anchored taxonomic construction works in both cases, and that the foundation supplies a common architectural vocabulary in which both definitions and both taxonomies can be specified.

The mapping is explicit:

| Affect paper | Agency paper |
|---|---|
| Love at constitutive-extension topology | Free choice proper across one or more orders |
| Affect criterion (perturbation of maximally-self-defined I) | Agency criterion (operator-bundle-mediated direction across an option-space) |
| Five clusters as basis projections | Three-tier configuration plus variation taxonomy |
| Reflexive-PtCns bridge lemma (load-bearing for self-cluster) | Universal toolkit constraint with order-translation (load-bearing for orders) |
| Derivation schema with $\kappa$/$\phi$/$\rho$/$\Pi$ signatures plus $A_{m,t}(x)$ status | Derivation schema with $\kappa$/$\phi$/$\rho$/$\Pi$ signatures plus $A_{m,t}(x)$ status |
| Healthy/pathological pairing per cluster | Healthy/pathological pairing per condition-failure mode and per order |

The shared derivation schema is not coincidence. The architecture's foundation supplies a common coordinate system for any application paper; affect and agency draw on the same coordinates because they are configurations of the same modeling I. The schemas differ in the *questions* they ask of each coordinate — the affect schema asks what content the I is in extension with, what frame is being violated, what projected damage is at stake; the agency schema asks what option the I is in contact with, whether the I can construct source-access to its own selection, how integrated the action is with the lived-I profile. The architectural vocabulary is the same; the application-domain questions differ.

The parallelism is also methodological in a stronger sense: each paper anchors on the configuration in which its target domain is most fully developed, derives the rest by structural variation, and refuses to treat any configuration outside the anchor as the "real" case. The affect paper refuses to treat thin attractions as failed love; the agency paper refuses to treat free selection or scaffold-captured choice as failed free choice. Variations are structural, not deficient.

## 4.2 The agency criterion

Just as affect-as-such required an explicit criterion to avoid trivialization (Section 4.1 of *Differentiated Affect*), agency-as-such requires an explicit criterion that distinguishes it from substrate processes, input events, and other operations involving the I that do not constitute agency.

> An *agency event* is an operator-bundle-mediated direction by the I across a verification-toolkit-constructed live-option space at one or more orders of willing.

*"By the I"* in this criterion does not mean merely occurring in the I's body or perceptual field. It means direction through the operator-bundle in a way *minimally available for ownership-integration* — the event is not merely alien substrate output, dissociatively produced action, or confabulated authorship. Full ownership-integration is condition 6 of free choice proper (Section 3.2); agency-as-such requires only the weaker minimum: that the event be operator-bundle-mediated in a way the I could in principle integrate, even if integration in fact fails (as in alienated action, where the criterion is met for *agency* but condition 6 fails for *free choice proper*). The agency criterion is therefore broader than the free-choice definition — alienated action, manipulated action, and confabulated-authorship cases fall under the agency criterion at varying degrees of structural integrity, and the variation taxonomy in Section 8 specifies how each case sits with respect to both the criterion and the six conditions.

The criterion has structural parts: operator-bundle-mediation, toolkit-constructed live-option space, at one or more orders of willing. Each part does discriminative work.

**Excluded by operator-bundle-mediation:** substrate response without operator engagement (reflex, startle, autonomic adjustment beyond toolset-mediation), salience capture, input-direction events more broadly. The foundation's three-order pathway / imprinting structure (File 3, Section 8.5) describes how content reaches and imprints the I; that pathway operates whether or not any agency event is occurring. Pure imprinting events — being startled, having a memory rise unbidden, being affected by a sudden mood-shift — are not agency events because no operator-bundle mediation is occurring. These are the foundation's input direction; agency is the output direction, and only the operator-bundle-mediated portion of output qualifies.

**Excluded by toolkit-constructed live-option space:** action through substrate pathway without entering live-option selection. Some compulsions, automatisms, and reflexive actions occur without any toolkit-construction of options. The substrate produces the action; no live-option space is constructed; no selection from among options occurs. The architecture treats these as substrate-produced action, not agency events. (They can be *components* in larger agency events — an agency event may include reflexive sub-actions — but the reflex itself is not agency.)

**Required by "at one or more orders of willing":** an event qualifies as agency when operator-bundle-mediation is occurring at any of the agent's developed orders, beginning with the three foundational orders (focus, thought, substrate-mediated action) and extending to constructed orders 4+ where the agent's toolkit has developed them (Section 5.7). Pure first-order agency events (directing focus without consequent thought or action), pure second-order events (deliberation without consequent action), pure third-order events (skilled motor execution with thin first/second-order participation), and pure constructed-order events (e.g., a fourth-order asking-act with thin upstream participation in mastered-domain willing) are all agency events. The criterion does not require cross-order integration; it requires operator-bundle-mediation at at least one developed order.

The criterion is structural, not phenomenological. An event satisfies the criterion if the structural configuration is present, regardless of how rich or thin the phenomenal experience. A skilled spontaneous action with minimal phenomenal awareness of the choice-process — the chef chopping vegetables, the conversationalist responding fluidly — meets the criterion when operator-bundle-mediation is occurring at the relevant order(s) and when ownership-integration holds. A vivid feeling of having chosen — the Wegner-paradigm subject convinced they chose what they did not — does not by itself satisfy the criterion; the structural configuration must actually obtain.

This is a stronger unification than vague claims that agency "involves direction" or "involves choice." The architecture commits to operator-bundle-mediated direction across a toolkit-constructed live-option space as the structural object of agency, distinguishing agency events from substrate response, input events, and confabulated authorship-attribution alike.

## 4.3 The organization of the agency taxonomy

The unification has methodological consequences for the rest of the paper. Rather than treating each agency-configuration as a freestanding category, the paper organizes the agency space along two structural axes: the *tier axis* (free selection, free choice proper, wholehearted free choice — each meeting a different subset of the six conditions) and the *variation axis* (which conditions are met, modified, or fail, and through which structural mechanism). Sections 5–10 develop these axes; Section 4 fixes the schema.

The variation axis has four sub-axes:

| Sub-axis | Question |
|---|---|
| Condition-failure mode | Which of the six conditions fails or is modified, and at what order? |
| Order-engagement profile | Which order(s) of willing is the configuration primarily exercised through? |
| Substrate-coupling failure mode | Where condition 4 fails: preemption, bypass, or capture? |
| Source-status | Where condition 6 holds internally: is the option-space source-clean, acutely manipulated, scaffold-captured, or coercively constructed? |

Any agency configuration can be analyzed by specifying its position along each sub-axis. *Akrasia* is condition 3 same-order failure (evaluation and selection mismatch at second-order) with no substrate-coupling or source issue. *Compulsion* is condition 4 capture (typically third-order substrate dominance) with secondary attentional and rationalization compounding. *Manipulation* is conditions 1–6 met internally with source-compromised option-space construction. *Alien-hand* is condition 6 ownership-integration failure at third-order. The variation taxonomy presented in Section 8 walks through the configurations explicitly; the schema is fixed here.

*Developmental-window status is not a fifth variation sub-axis but a responsibility overlay.* The same agency configuration — same condition-failure profile, same order-engagement, same substrate-coupling status, same source-status — can be pre-agentially scaffolded, mature-accidental, misintentional, deliberate, or scaffold-captured (Section 4.10), with different responsibility implications in each case. Developmental-window status modulates how the configuration enters the responsibility-attribution analysis of Section 9; it does not modify what the configuration architecturally *is*. Holding the variation axes and the developmental overlay as distinct prevents conflating "what kind of agency event this is" with "how responsibility-attribution applies to it."

The healthy/pathological pairing structure runs through all variations. For each agency configuration, there is at least one structurally identifiable pathology — typically a failure of one of the constraining mechanisms (toolkit, bundle, substrate-coupling, Mode B, ownership-integration), a hypertrophy of a normally-functional operation, a capture by substrate dynamics, or a misdirection through source-compromise. The architecture predicts that pathologies are not random departures from health but structural failures of specific operations at specific orders. Sections 8 and 10 develop the predicted structural signatures for each pathology.

The agency taxonomy is not organized by clusters in the affect paper's sense, because agency does not have the same kind of dominant-relation structure that affect has. Affects organize naturally into clusters by what relation between content and the I dominates the perturbation; agency events are organized more naturally by *which structural conditions of the operator-bundle-mediated direction obtain*, since the conditions are themselves what specify the configuration. Both schemas are basis projections — orthogonal-enough operator families against which real events can be decomposed — but the basis differs across the two domains.

## 4.4 The three orders of willing in full detail

Section 3.4 introduced the three foundational orders compactly; Section 4.4 develops them in full. Each order is characterized by its locus, its operations, its toolkit-constructed option-domain, its phenomenology, its substrate-coupling structure, and its characteristic failure modes. The three orders are application-level extensions of the foundation's three-order pathway typology (File 3, Section 8.5) to the output direction, not foundation extensions; they use the same orders the foundation already establishes for the input direction, redirected to operator-bundle-mediated outward-directed operations. *Section 4.4 treats the three foundational orders specifically*; constructed orders 4 and above (asking, directing, team-coordination, institutional engagement) are developed in Section 5.7 as the application-level N-order generalization. Where this section uses "the three orders" or "all three orders," the reading is "the three foundational orders" unless otherwise specified. *Throughout this subsection, willing-operations at each order routinely engage live-options at skeleton-level resolution under the fuzzy-construction discipline of Section 3.2 (Condition 1) and 5.3's dynamic-refinement-during-execution analysis; full pre-construction of every detail is not required for liveness or for engagement at any order.*

**First-order willing-operation: focus / attention.**

*Locus:* the cogito-anchored attentional field. First-order willing is anchored *in* the field the bare cogito anchors (Foundation File 1) but is not an operation *of* the bare cogito as such. The bare cogito remains the modeling I's tautological self-identification; first-order willing-operations occur over substrate-bound focus capacity (Foundation File 3, Section 8.1) within the field the cogito anchors.

*Operations:* directing attention to a focus-target, sustaining focus against pull-away, shifting focus across competing salience, returning focus after distraction, holding focus stable against substrate-driven salience capture.

*Toolkit-constructed option-domain:* focus-targets the verification-toolkit can represent, evaluate, and direct attention to. The I cannot will to focus on what the toolkit cannot make a live focus-object — phenomena lacking conceptual form, contents below discrimination threshold, framings not yet acquired. Contemplative attention training expands the first-order toolkit by extending the repertoire of representable focus-objects and the stability-conditions under which focus can be sustained.

*Phenomenology:* the strain of holding attention against pull, the moment of return after distraction, the directed-beam quality of sustained focus, the experience of shifting focus volitionally rather than being pulled.

*Substrate-coupling structure:* substrate enables focus-direction by supplying perceptual fields, salience-gating mechanisms, and arousal-state. First-order willing operates *over* substrate-supplied salience without preempting the willing-operation. When salience capture dominates — sudden pain, intense fear, severe ADHD-like configurations — first-order willing fails through substrate-preemption of the focus-direction.

*Characteristic failure modes:* salience capture (substrate dominates focus allocation); fragmentation (multiple competing salience targets prevent stable focus); flooding (toolkit cannot construct stable live focus-objects under salience overload); ADHD-like configurations (substrate-developmental constraints on focus-stability and attention-shifting, often compounded by second-order working-memory, planning, inhibition, and task-initiation constraints; treated in detail in Sections 4.6 and 5.4).

**Second-order willing-operation: directed thought.**

*Locus:* the mind / lived-I. Second-order willing is the I directing thought down a deliberation-path. Mode B reflective operations occur primarily here, though Mode B's object-domain extends to all three orders (Section 4.4 below).

*Operations:* directing thought down a deliberation-path, evaluating thought-paths, performing mental operations (comparing, considering, hypothesizing, deciding), exercising Mode B reflective access over toolkit-constructed thought-paths.

*Toolkit-constructed option-domain:* thought-paths the toolkit can represent, evaluate, and deliberate through. The I cannot will to deliberate down a thought-route the toolkit cannot construct. This explains why some thoughts genuinely do not occur to people, why expertise expands not just thinking-speed but the *space* of thinkable thoughts, why contemplative or philosophical training opens framings the trainee could not previously inhabit.

*Phenomenology:* the act of "thinking it through," the experience of considering an alternative, working a problem, weighing options, the felt-sense of mental operation under direction.

*Substrate-coupling structure:* the cognitive substrate (Foundation File 3, Section 8.5) supplies the cognitive material — propositions, comparisons, projected-future representations — that the I directs into thought-paths. Substrate enables deliberation without preempting the willing-operation. When substrate dominates — rumination loops, intrusion-interruption, severe cognitive fog — second-order willing fails through substrate-preemption of the deliberation.

*Characteristic failure modes:* rumination capture (substrate-loops dominate the deliberation-space); intrusion (substrate-content interrupts directed thought); fog (toolkit cannot construct evaluable thought-paths or substrate cannot supply sufficient cognitive material for evaluation); learned-helplessness-style projection-toolkit damage (the I perceives no thought-paths leading to viable preservation outcomes).

**Third-order willing-operation: directed substrate action.**

*Locus:* the substrate. Third-order willing is the I directing substrate action — motor patterns, mediated embodied regulation, scaffolded autonomic processes where toolset-mediation makes them available as live options.

*Operations:* motor action, mediated embodied regulation (posture, breath, facial expression, deliberate physiological adjustment), scaffolded autonomic modulation (biofeedback-mediated heart-rate adjustment, breath-mediated vagal tone modulation, contemplative-practice-mediated arousal regulation).

*Toolkit-constructed option-domain:* action-patterns the toolkit can represent, evaluate, and implement through substrate. The I cannot will to direct the body through an unacquired movement-pattern. The expert violinist's third-order toolkit constructs as live a vast space of action-patterns the non-violinist's toolkit cannot construct at all. The contemplative practitioner's third-order toolkit constructs as live somatic-modulation patterns (breath-pacing, postural adjustment, micro-relaxation cues) unavailable to the untrained.

*Phenomenology:* doing, executing, performing through the body. The felt-sense of directed substrate action — the moment of moving, the experience of skilled execution, the strain of motor effort against fatigue or unfamiliarity.

*Substrate-coupling structure:* substrate supplies motor capacity, autonomic state, and embodied affordance. Third-order willing operates *over* substrate-supplied capacity without preempting the willing-operation. When substrate dominates — addiction-pattern capture, motor compulsion, action-bypass through dissociation — third-order willing fails through substrate-preemption, bypass, or capture.

*Bounded scope:* autonomic processes count as third-order live options *only when* the toolkit can represent, modulate, or scaffold them. Spontaneous heart-rate variability is not a third-order live option for an untrained agent; it can become one through biofeedback training, contemplative practice, or somatic education. The architecture is precise about this scope: the third-order willing-domain expands as the toolkit expands; processes lacking toolset-mediation remain substrate processes, not willed options.

*Characteristic failure modes:* preemption (reflex, startle, autonomic response before bundle-selection); bypass (action through substrate pathway without entering live-option selection — automatism, some compulsions); capture (substrate pull dominates such that alternatives are not live from inside — addiction-pattern dominance, severe drives).

**Cross-order integration as marker of agency-richness.** Wholehearted free choice typically involves coordinated free choice across multiple orders simultaneously: first-order focus on the choice-relevant content, second-order deliberation over the option-space, third-order action-patterning all aligned and ownership-integrated. Thinner agency-configurations operate at single orders or with reduced cross-order integration. The architecture predicts that, *other conditions equal*, agency-experience richness tracks cross-order integration: a person doing all three at once — focused, deliberating, acting through skilled substrate — should tend to experience agency more vividly than a person operating at one order with thin engagement at the others. This is a comparative prediction, not a guaranteed phenomenological law: trauma, dissociation, flow-states with intentionally thinned second-order engagement, and culturally-mediated framings of agency can modulate felt agency in ways that complicate within-subject comparison. Section 6 develops integrated effort and the phenomenology of cross-order coordination; Section 11 generates discriminating predictions on cross-order integration as agency-richness marker.

## 4.5 The universal toolkit constraint

The verification-toolkit operates at all three foundational orders with structurally identical *abstract* conditions and order-specific *implementation semantics*. Section 3.5 presented the order × condition matrix in compact form; Section 4.5 develops the universal toolkit constraint as the architectural commitment underlying that matrix. *This subsection states the constraint at the three foundational orders. Section 5.7 generalizes the same abstract constraint to constructed target-domain orders 4 and above; the constraint is universal in form across all developed orders, with the kind of option-space the toolkit constructs differing by order.*

The constraint:

> The verification-toolkit is the universal limiter on what can be willed at any developed order. The I cannot will what the toolkit cannot construct as live, regardless of order, and (for any agent $m$ at time $t$ in domain $d$) regardless of whether the order is foundational (1–3) or constructed ($4 \leq n \leq N(m,t;d)$). The same six conditions of free choice apply at each developed order; what differs is the kind of option-space the toolkit constructs (focus-targets, thought-paths, action-patterns at foundational orders; not-I coordination structures at constructed orders) and the implementation semantics of "live," "evaluable," and "implementable" for that domain. *The constraint is universal in form but domain-relative in reach: in each domain $d$, the I's action-space extends only through $N(m,t;d)$.* *Live-option construction at any order routinely operates at skeleton-level resolution under the fuzzy-construction discipline (3.2, 5.3); the toolkit constraint applies to whether the toolkit can construct the live skeleton with trained-expectation grounding, not to whether the toolkit has pre-constructed every executable detail.*

This makes the verification-toolkit application-level apparatus carrying the universal limiter status. The foundation supplies $\phi$ (truth-indistinguishability / verification status, File 3, Section 7.3) and the substrate-mediation pathways through which contents reach the I; the agency paper develops the toolkit as the application-level apparatus by which the I constructs live-option spaces from those contents at each order. The toolkit is not a foundation primitive (Section 11.5 of the planning document, methodological discipline 5); the foundation supports the apparatus the toolkit organizes.

**What "live" means at each order:**

| Order | "Live" implementation semantics |
|---|---|
| First-order | Focus can be shifted to or sustained on the option; the toolkit can represent the focus-target stably enough for attention to inhabit it |
| Second-order | Thought can be pursued down the deliberation-path; the toolkit can represent the path with sufficient resolution for evaluation and selection |
| Third-order | Substrate can execute or scaffold the action-pattern; the toolkit can represent the pattern in a form motor or mediated-autonomic capacity can implement |

**What "evaluable" means at each order:**

| Order | "Evaluable" implementation semantics |
|---|---|
| First-order | Salience-worth, focus-worth, attention-worth can be assessed (PtCns over focus-coherence, $\Pi$-weighting over attention-priority) |
| Second-order | Reasons, frame-coherence, projected outcomes can engage thought-paths (PtCns over frame-coherence, PCE-over-projection over preservation-implications, $\Pi$-weighting over preservation-priority) |
| Third-order | Action consequences, embodied feasibility, somatic affordance can be assessed (PCE-over-projection over action-outcomes, $\Pi$-weighting over action-priority) |

**Toolkit-development at each order.** Training, learning, contemplative practice, education, and therapy all operate as toolkit-development. Each modality typically targets a primary order:

- Contemplative attention training expands the first-order toolkit by extending focus-object repertoire and focus-stability conditions
- Education, philosophical training, cognitive therapy, and structured deliberation training expand the second-order toolkit by extending thought-path repertoire and the projection-apparatus
- Motor training, skill acquisition, somatic practice, and biofeedback training expand the third-order toolkit by extending action-pattern repertoire and substrate-modulation capacity

This generates a discriminating prediction (Pred 20 in planning v0.3.1): training that targets a specific order should produce expansion of the option-space primarily at that order, with cross-order transfer dependent on shared toolkit-features. Pure first-order training (concentration practice without semantic load) should produce smaller second-order option-space expansion than first-order; pure third-order training (motor drills without semantic processing) should produce smaller second-order expansion than third-order; integrated training that targets multiple orders simultaneously should produce the broadest expansion. The literature on transfer-of-training is consistent with this prediction; the architecture's contribution is to predict it from order-specific toolkit structure.

The toolkit-constraint is implementation-neutral on substrate. The toolkit operates at the application level; substrate processes (cognitive, somatic, motor) supply the implementation substrate but are not the toolkit themselves. Section 5 develops the live-option construction lemma in detail and establishes the application-level apparatus formally.

All implementation-neutrality claims made in this section — including the toolkit-constraint's neutrality on substrate, the order-translation discipline, and the toolkit-development predictions — are bounded by the *lawful-structural-frame* qualifier specified in Section 3.7. The verification-toolkit cannot operate over a substrate-frame in which contents, profiles, and persistence-relations are not structurally definable; what counts as "live," "evaluable," or "implementable" presupposes lawful structural regularity even though it does not presuppose any specific substrate-metaphysics within that frame.

## 4.6 Order-specific pathology taxonomy

The order-specific framing generates a pathology taxonomy organized as *primary / secondary / cross-order profiles* rather than single-order assignments. Actual pathologies typically involve compound order-engagement, with relative weighting across orders being the diagnostic question rather than purity at one order. The pathologies catalogued in this subsection's table operate primarily at the foundational orders (1–3); pathology-by-order analysis applies equally at constructed orders (4+, per Section 5.7), where pathologies are typically domain-specific (negotiation dysfunction, team-direction failure, interpersonal-direction pathology, institutional-engagement variation). Where this subsection refers to "order" in pathology classification, the foundational reading is primary; constructed-order pathologies are developed in Section 8 and supported by the constructed-order apparatus of 5.7. Throughout this section, "order" should be read as foundational order unless explicitly discussing constructed-order source-compromise or constructed-order pathology.

| Pathology | Primary order | Secondary / cross-order involvement |
|---|---|---|
| Compulsion (e.g., OCD-spectrum) | Variable by case: compulsive *action* often third-order substrate-pressure or capture; OCD-spectrum cases frequently first/second-order primary | First-order attentional capture toward compulsion-relevant cues; second-order threat / uncertainty evaluation loops; third-order substrate action-pressure where present; primary order varies across the spectrum and warrants per-case analysis |
| Akrasia | Second-order *same-order* mismatch (PtCns evaluation diverges from bundle selection at the same order) | Cross-order tension: third-order substrate-pull may bias the divergence |
| Alien-hand syndrome | Third-order action without first/second-order ownership-integration | Distinct from compulsion: ownership failure, not bundle-selection capture |
| Severe depression (often multi-order) | Variable by case; often third-order primary | Compound across orders: third-order somatic flattening, anhedonia, fatigue + second-order rumination, projection-collapse + first-order focus-narrowing |
| Learned helplessness | Second-order projection-toolkit damage | The I perceives the world as having no pathways, not the projection-apparatus as damaged; minimal first/third-order direct damage |
| Anhedonia | Third-order / embodied pleasure-response apparatus impairment (parallel to *Differentiated Affect* Section 9's profile-shape disturbance treatment) | Often produces second-order engagement-collapse (no live thought-paths to engagement) and first-order salience flattening |
| Addiction | Third-order substrate-reward capture | Compound: first-order attentional capture, second-order $\Pi$-distortion / rationalization, self-cluster shame after recurrence |
| ADHD-like configurations (substrate-developmental, candidate not foundation-derived) | First-and-second-order substrate-developmental constraint on operator-bundle-mediation: executive function (sustained attention, attention-shifting, working memory, response inhibition, planning, task initiation, goal-directed persistence) is operator-bundle-mediation at orders 1 and 2; substrate-developmental disability constrains this at both orders simultaneously | Input-side substrate pathways (perceptual salience-gating, osmotic-imprinting receptivity, reward-substrate processing) may be intact, amplified, or differently weighted relative to constrained operator-bundle-mediation: the input/output asymmetry is structurally pronounced — heightened salience capture, osmotic-imprinting sensitization, and disproportionate immediate-reward salience where near-term reward cues can capture action-priority against constrained second-order $\Pi$-weighting, inhibition, and future-projection; third-order arousal regulation often compounded; cross-order coupling under-coordinated because both upstream orders are individually constrained |
| Trauma-cue activation | Compound across orders | Third-order substrate-readiness + second-order asymmetric threat-projection + first-order focus-capture; ownership disruption |
| Habitual action (chosen) | Reduced first-order direction | Second-order chosen pattern executing through third-order substrate; agency-thin but not damage |
| Habitual action (compulsive) | Third-order substrate-pattern capture | First-order attentional capture; minimized second-order |
| Skilled flow | Cross-order coordinated | All three orders coordinated; second-order Mode B object-domain available but not exercised; not pathology |
| Dissociative action | Multi-order ownership-integration failure | Third-order action and possibly first/second-order operations occur but ownership-integration fails across orders |

The taxonomy gives the paper a structurally specific account of pathology-by-order *profile* rather than a single-order assignment. The pattern of analysis in any case is: (i) identify the primary-order damage or capture; (ii) identify secondary-order involvement and its relative weight; (iii) identify cross-order conflict signatures (a primary-order failure typically produces tension with intact orders, and the tension itself is diagnostic).

The taxonomy enriches the variation taxonomy in Section 8: each variation is now analyzable in terms of primary order, secondary involvement, and cross-order conflict pattern, in addition to its condition-failure profile. *Compulsion* is typically condition-4-failure (capture, bypass, or both); compulsive action cases are often third-order primary with first-order attentional and second-order rationalization secondary, while OCD-spectrum cases are frequently first/second-order primary with third-order substrate-pressure secondary — the order-profile is per-case rather than uniform across the category. *Akrasia* is condition-3 same-order mismatch, second-order primary, with cross-order substrate-pull contributing. *Severe depression* is multi-condition compound (live-option construction reduced at multiple orders, evaluative engagement collapsed at second-order, ownership-integration sometimes diminished), multi-order primary. The variation taxonomy and the pathology-by-order taxonomy interlock: any case sits in both schemas at once.

## 4.7 Therapeutic modalities classified by primary-order target

The order-specific pathology framing generates an architectural classification of therapeutic modalities by which order's toolkit they primarily target:

| Modality | Primary order targeted |
|---|---|
| Contemplative practice (meditation, mindfulness, attention training) | First-order toolkit work — focus-direction repertoire and focus-stability |
| Cognitive Behavioral Therapy / Cognitive Therapy | Second-order toolkit work — thought-path repertoire, projection apparatus |
| Behavioral activation, exposure therapy, somatic experiencing | Third-order toolkit work — action-pattern repertoire, substrate-action capacity |
| Acceptance and Commitment Therapy | Cross-order: second-order PtCns / $\Pi$-orientation work plus first-order acceptance-of-content training |
| Internal Family Systems, parts work | Cross-order: ownership-integration work across multiple lived-I sub-regions |
| Integrated approaches (general psychotherapy) | Multi-order, with relative emphasis varying by pathology and clinician |

This produces a discriminating prediction: therapy efficacy is predicted to track the *match* between the modality's primary-order target and the pathology's primary-order damage profile. Mismatched targeting (e.g., second-order CBT applied to primarily third-order substrate-capture pathology) is predicted to produce poorer outcomes than matched targeting (e.g., behavioral activation or somatic work for the same case). Sequenced interventions that match the order across the pathology's damage profile in turn — e.g., third-order somatic stabilization followed by second-order cognitive restructuring followed by first-order contemplative integration — are predicted to outperform either single-order interventions or order-mismatched sequences *when order-damage profiles are correctly identified*.

This is an application-level prediction, not a foundation-level dictum, and it is not treatment advice or a clinical protocol. The architecture's contribution is to make the order-fit prediction discriminating: previous frameworks generate predictions about *what* to target (cognitive content, behavioral patterns, somatic experiences) without specifying the structural reason these targets correspond to different toolkit-orders. The order-specific framing supplies the structural reason and the discriminating prediction. Clinical judgement, comorbidity, individual variation, and per-case order-damage analysis always govern actual treatment selection; the architecture predicts target-fit at the structural level, not which specific intervention any specific patient should receive.

The classification also has implications for sequenced and combined treatment as architectural prediction. *Severe depression* with third-order primary and second-order secondary involvement: the architecture predicts a structural advantage for sequenced or combined interventions addressing both — behavioral activation (third-order) combined with cognitive therapy (second-order), with contemplative practice (first-order) added when severe focus-narrowing is present. *Addiction* with third-order capture and compound involvement: the architecture predicts that effective treatment will often require third-order substrate work (often medication-assisted), second-order $\Pi$-restructuring (motivational interviewing, cognitive therapy), first-order attention work (mindfulness-based relapse prevention), and self-cluster work for shame (parts work, IFS, or related approaches), if the order-damage analysis is correct in any given case. The order taxonomy organizes the treatment-planning question architecturally rather than empirically only; whether the predicted advantage materializes in clinical practice is open to investigation.

## 4.8 The agency derivation schema

Just as the affect paper provided a derivation schema (Section 4.4 of *Differentiated Affect*) for analyzing any affect through six steps, the agency paper provides a derivation schema for analyzing any agency configuration. The schema uses the foundation's three coordinates $\kappa$, $\phi$, $\rho$ together with the foundation-named preservation-ranking $\Pi$ (placeholder for application-level formalization, Foundation File 2 §4.8, developed at coordinate-grade in this paper and its companion *Free Will*), and the foundation's content-indexed phenomenal-availability status predicate $A_{m,t}(x)$. This is a notation correction relative to earlier agency-paper drafts: $A$ is not a coordinate parallel to $\kappa$, $\phi$, $\rho$, and is also architecturally distinct from $\Pi$. It is the predicate that marks whether a specified content $x$ is phenomenally available to modeling I $m$ at time $t$.

| Foundation element | Agency-relevance question |
|---|---|
| $\kappa$ (contact) | What is the I in contact with at this configuration? Option, cue, body-state, other-I, threat, value-content, embodied affordance, scaffold-element? |
| $\phi$ (source-pathway access) | Can the I construct source / reason access — to *why* this option is in the option-space, *why* this evaluation, *why* this selection? |
| $\rho$ (identity-correlation) | How structurally integrated is the option / selection / action with the lived-I profile and (for identity-significant cases) the maximally-self-defined I? |
| $\Pi$ (preservation-ranking) | How high does this option / selection / action sit in preservation-priority and action-priority? |
| $A_{m,t}(x)$ (phenomenal-availability status predicate) | For each relevant agency-content $x$ — selection, action, source-pathway, option-space construction, ownership-recognition, report, urge, resistance, or alternative — is $x$ phenomenally available to the I at $t$? |

**Joint $A_{m,t}(x)$ / $\phi$ status across agency configurations.** The foundation's conscious / latent / unconscious distinction is a joint configuration of phenomenal availability and source-pathway access. Because $A_{m,t}(x)$ is content-indexed, an agency event can have different $A$-statuses for different contents: the action may be phenomenally available while the source-shaping pathway is not; the ownership-report may be phenomenally available while the actual selection-process is source-opaque; the urge may be phenomenally available while its developmental origin remains outside source-access.

| Joint status | Agency-relevance |
|---|---|
| $A_{m,t}(x)=1$, $\phi(x)$ defined / available | Conscious-clear agency-content: the I undergoes or notices $x$ and has constructible source / verification access to it. |
| $A_{m,t}(x)=1$, $\phi(x)$ low or undefined | Conscious-fuzzy / source-opaque agency-content: the I experiences $x$ but cannot construct its source-pathway. This covers felt choice with source-opacity, effort without clear resistance-source, and trauma-cue activation whose origin is opaque. |
| $A_{m,t}(x)=0$, $\phi(x)$ constructible upon activation | Latent / retrievable agency-content: the content is not presently noticed, but can become available through attention, recall, or Mode B activation. |
| $A_{m,t}(x)=0$, $\phi(x)$ undefined | Unconscious-operative agency-content: source-shaping, biasing, osmotically formed, or substrate-level patterns affect option-space, salience, action, $\rho$, or $\kappa$ without being phenomenally available or source-accessible under the current toolkit. |
| $A_{m,t}(x)=1$ now, later $\phi$-construction | Post-hoc recognition of why one acted: the event-content was phenomenally available at the time, but source-access is constructed later through reflection, conversation, therapy, or further verification-tool development. |
| $A_{m,t}(x)=0$ now, later $A_{m,t'}(x)=1$ with $\phi$-construction | Latent or unconscious-operative source becomes phenomenally and explanatorily available later — therapy-mediated surfacing, contemplative-practice surfacing, or later articulation of an operative source-pattern. |

The schema applies to representative cases that the rest of the paper develops:

| Configuration | $\kappa$ | $\phi$ | $\rho$ | $\Pi$ | $A_{m,t}(x)$ / $\phi$ status |
|---|---|---|---|---|---|
| Free choice proper | Options, evaluations, action-patterns at engaged orders | $\phi$-access to selection process available | $\rho$-integration of selection into lived-I | $\Pi$-engagement with options under PCE-projection | $A_{m,t}(\text{choice})=1$; source-relevant contents are phenomenally available where reflective access is present. |
| Wegner-paradigm apparent choice | Action and confabulated authorship-narrative | $\phi$-failure on the actual selection process (no genuine bundle-selection for $\phi$ to track); false-appearance $\phi$ on the confabulated narrative | $\rho$-claim made but tracking confabulated rather than actual selection | $\Pi$-engagement with confabulated story | $A_{m,t}(\text{confabulated authorship narrative})=1$; the actual selection process is not what the available narrative tracks, making the joint $A/\phi$ pairing diagnostic. |
| Compulsion (substrate capture) | Action and the urge or pressure | $\phi$-access to the urge often present; $\phi$-access to *why-now-this-action* fragmentary | $\rho$-integration of action sometimes present, often with self-cluster compound | $\Pi$ distorted toward urge-relief | $A_{m,t}(\text{action})=1$ and often $A_{m,t}(\text{urge})=1$; source-pathway access remains fragmentary or low. |
| Manipulation case | Action and its narrative | $\phi$-failure on option-space *construction* (the manipulation invisible); $\phi$ on selection from given options often present | $\rho$-integration of action present; the action is owned from inside | $\Pi$-engagement with the manipulator-supplied narrative | $A_{m,t}(\text{choice})=1$; upstream option-space shaping is typically $A_{m,t}=0$, $\phi$ undefined, or becomes conscious-fuzzy only when activated later. |
| Trauma-cue action | Trauma-relevant cue and reactive action-pattern | $\phi$-failure on connection between cue and pattern at time of action | $\rho$-integration often disrupted; the action is hard to own | $\Pi$ distorted toward threat-defense | $A_{m,t}(\text{cue})=1$ and $A_{m,t}(\text{action})=1$; the cue-action source-connection is conscious-fuzzy until later $\phi$-construction. |
| Regret over not-selected option | The not-selected option as Mode B object | $\phi$-construction over the alternative now active | $\rho$-claim made over the alternative reflectively | $\Pi$ now favors the not-selected option | $A_{m,t}(\text{alternative-as-Mode-B-object})=1$. |

Worked example (free choice proper, compact form):

| Step | Free choice proper |
|---|---|
| Profile-region | Lived-I profile, with optional propagation to maximally-self-defined I in identity-significant cases |
| Order-engagement | One or more orders of willing engaged with operator-bundle-mediation |
| Active operators | Toolkit-construction at engaged order(s); operator-selection bundle (PtCns, PCE-over-projection, $\Pi$-ranking, focus, substrate-readiness, Modes A/B/C); Mode B available |
| $\kappa$/$\phi$/$\rho$/$\Pi$ plus $A_{m,t}(x)$ status | $\kappa$ with options, evaluations, action-patterns; $\phi$-access to selection process available; $\rho$-integration of selection into lived-I; $\Pi$-engagement with options under PCE-projection; $A_{m,t}(\text{choice})=1$ and relevant source-contents are phenomenally available where reflective access is present |
| Healthy constraint | Toolkit constructs adequate option-space; bundle selects without preemption / bypass / capture; Mode B available without confabulation; ownership-integration holds |
| Pathology / variation modes | Free selection (thin condition 2); akrasia (same-order condition 3 mismatch); compulsion (condition 4 capture); apparent choice (condition 5 confabulation); alienated action (condition 6 internal failure); manipulation (condition 6 internal hold with external source-compromise) |

Each agency configuration treated in this paper should be analyzable through this schema. When a configuration resists clean derivation, that resistance itself is informative: either the architecture lacks apparatus the configuration requires (foundation-extension candidate), or the configuration is genuinely a compound that requires multi-axis analysis (the schema applies to each component), or the configuration is a misclassification (a phenomenon being called agency that does not meet the agency criterion in 4.2).

## 4.9 The $\rho$/$\Pi$ separation in agency analysis

The foundation explicitly separates $\rho$ (structural identity-correlation) from $\Pi$ (preservation / action-priority); $\Pi$ may depend on $\rho$ but is not reducible to it (Foundation File 3, Section 7.6 — identity-correlation profile; Section 7 introduces the coordinates). This separation is load-bearing for agency analysis. Configurations where $\rho$ and $\Pi$ diverge produce specific agency phenomena that ownership-only or endorsement-only views collapse:

| $\rho$/$\Pi$ configuration | Agency phenomenon |
|---|---|
| High $\rho$-integration with an impulse but low PtCns endorsement of acting on the impulse | Akrasia — the impulse is integrated but the action is not endorsed |
| High $\Pi$-priority for an option but low $\rho$-integration of the I with that option | Moral aspiration — the option matters preservation-wise but is not yet integrated as one's own |
| High ownership-integration ($\rho$) but low accountability due to toolset poisoning | Manipulation case: the action is "mine" but source-compromised |
| Selection from low-$\rho$ but high-$\Pi$ option | Self-overcoming, growth-action — choosing what one does not yet identify with because preservation-priority requires it |
| Selection from high-$\rho$ but low-$\Pi$ option | Habit-execution, identity-maintenance — choosing what one identifies with even when its preservation-priority is low for the immediate context |

Canonical hierarchical-endorsement views in the Frankfurt tradition, when treated as endorsement-only views, collapse cases the architecture distinguishes. *Akrasia* is a configuration where $\rho$-integration of an impulse is high (the agent recognizes the impulse as theirs) while PtCns-endorsement of acting on it is low; the agent acts on the integrated impulse against their own evaluation. Frankfurt's hierarchical view captures part of this — the second-order desire endorses or fails to endorse the first-order desire — but lacks the apparatus to distinguish the impulse's $\rho$-integration from PtCns's evaluation of the *action* the impulse moves toward. *Moral aspiration* — the agent who recognizes a course as preservation-priority high but has not yet integrated themselves with that course — is similarly under-described by endorsement-only treatments: ownership of an aspiration is not the same as $\rho$-integration of the I with the aspirational content. *Manipulation cases* are the most architecturally distinctive: the agent owns the action (high $\rho$) while the option-space was source-compromised (low accountability under outside-perspective analysis); endorsement-only views must either collapse manipulation into ownership-failure (mistaken — manipulated agents typically own their actions from inside) or collapse it into a non-agency case (also mistaken — the agent is exercising agency, just over a source-compromised option-space). More source-sensitive descendants in the broader hierarchical-endorsement tradition can address some manipulation pressures, but the architecture's distinctive discriminator is the explicit $\rho$/$\Pi$ separation paired with the source-status apparatus developed in 4.11–4.12; [Free Will §5] develops the framework-by-framework comparison in full.

The $\rho$/$\Pi$ separation produces architectural predictions about responsibility-attribution. Section 9 develops the analysis fully; the relevant claim here is that responsibility tracks the conjunction of (i) PtCns-endorsement of the action, (ii) $\rho$-integration of the action with the lived-I (and, for identity-significant cases, the maximally-self-defined I), and (iii) non-poisoned live-option construction (toolset-input not source-compromised). Each component is necessary; none is sufficient alone.

## 4.10 Developmental-window constraints on responsibility

The foundation states that many patterns arise from substrate, environment, and historical conditions before the I has intentional capacity, and that mature self-direction varies by condition and circumstance. This shapes the agency paper's responsibility analysis fundamentally. Five developmental sources are distinguishable, each with different responsibility implications:

| Developmental source | Responsibility implication |
|---|---|
| Pre-agential developmental imprint | Not chosen; not subject to responsibility-attribution (osmotic imprinting before agency, early-childhood conditioning, in-utero substrate development) |
| Mature accidental choice | Owned but not fully understood at the time; partial responsibility |
| Misintentional choice | Owned and regretted; responsibility tempered by the misintentionality |
| Deliberate choice | High responsibility — when free-choice conditions met |
| Scaffold-captured choice | Inside-owned but source-compromised by social, cultural, propaganda, or coercive scaffolding; responsibility diminished by the scaffolding |

The distinctions matter because adult agents carry pre-agential developmental imprints that continue to shape their option-spaces and evaluative criteria. A pattern formed in early childhood — long before the I had operator-bundle-mediation capacity — continues to constrain present option-spaces. Holding the present I responsible for those constraints conflates pre-agential imprint with mature deliberation. The architecture distinguishes them: present action that emerges from pre-agentially imprinted constraints is the I's action under condition 6 (it is integrated as the I's), but the *constraint structure* is not chosen, and responsibility-attribution must reflect this.

This recurring distinction structures Section 9 (responsibility) and threads through Section 8 (variations) — childhood agency, trauma-shaped agency, addiction with developmental-substrate components, manipulation under coercive socialization, learned helplessness as developmentally entrenched, "could-have-done-otherwise" objections that ignore developmental-window constraints, all engage these distinctions. The architecture's responsibility analysis is graded not because responsibility is subjective but because the structural conditions on responsibility-attribution are themselves graded along developmental, source, and integration dimensions.

## 4.11 The apparent-I / other-I apparatus for accountability and coercion

The foundation is single-perspective (Foundation File 1's opening commitments): each instantiation is anchored to one modeling I, with other I's accessed only through apparent-I and inferential contents. The apparent-I / other-I apparatus is developed in detail in Foundation File 4, Section 9 (*Other I's and Perspectival Realism*); the agency paper applies that apparatus to inter-I phenomena like accountability and coercion. Accountability and coercion are *inter-I* phenomena, not reducible to inside-perspective ownership-integration.

**Accountability** is the modeling I's relation to apparent-I, institutional, or normative contents that assign answerability to the I's actions. Accountability is not reducible to inside-perspective ownership-integration. Two agents can have identical inside-perspective ownership of an action while differing in accountability because their inter-I, institutional, or normative contexts assign answerability differently. A doctor and a layperson may identically own an act of resuscitation; their accountability for the outcome differs because professional norms and institutional roles assign different answerability-structures. The architecture treats this difference as real architectural structure (operating through apparent-I and norm-content), not as a confounder to be normalized away.

**Coercion** operates through other-I or institutional contents poisoning the toolset-input or constraining the option-space. The architecture analyzes coercion as a configuration in which apparent-I contents (representing the coercer or coercive institution) supply asymmetric salience or evaluative-pressure to the option-space such that the I's action emerges from a poisoned toolset-input rather than from undistorted live-option construction. Coercion is structurally distinct from manipulation: coercion typically operates with explicit, recognized other-I content (the coercer's threat is salient and identified as such), while manipulation can operate without recognition (the option-space is shaped without the agent recognizing the shaping). Both are source-compromise modes; they differ in whether the source is apparent-I-recognized.

This means accountability and coercion analyses in Section 9 must use the apparent-I / other-I apparatus, not just inside-perspective ownership-integration. Inside-perspective freedom and outside-perspective autonomy / responsibility-attribution are distinct, and the architecture's apparatus to address the distinction is the apparent-I / other-I apparatus combined with the source-compromise continuum (Section 4.12). Failing to use these apparatuses in the responsibility analysis would collapse cases the architecture distinguishes — an agent acting under coercion who satisfies all six inside-perspective conditions but whose action is not fully attributable to them, an agent acting from professional accountability who satisfies the six conditions but whose answerability differs from a layperson's, an agent acting under manipulation who satisfies the six conditions but whose option-space was source-compromised. Section 9's responsibility analysis depends on this apparatus.

## 4.12 Osmotic imprinting in manipulation, propaganda, and scaffold-captured choice

The foundation supplies *osmotic imprinting* as the mechanism by which repeated ambient co-occurrence shapes the I's profile without explicit focus or verification-pathway construction (Foundation File 3, Section 8.7). The agency paper applies this directly to source-compromise analysis. Long-term manipulation, propaganda, indoctrination, cultural scaffolding, and coercive socialization all operate primarily through osmotic imprinting, with explicit focus-mediated pathways playing variable secondary roles.

The source-compromise continuum:

- *Acute manipulation* operates at local toolset-input poisoning with explicit (though perhaps unrecognized) input. The manipulator supplies false information, asymmetric salience, or distorted projection; the agent's option-space is poisoned at the construction step but not at the developmental level. The agent can recover under post-hoc $\phi$-construction (recognizing what the manipulation was).
- *Propaganda and indoctrination* operate primarily through osmotic imprinting — repeated ambient exposure shapes option-space and evaluative criteria without focus-direction or $\phi$-construction at the time of imprinting. The agent's adult option-space is structured by accumulated osmotic exposure they have not had opportunity to evaluate or own. Recovery requires not just $\phi$-construction over individual judgments but reconstruction of the option-space and evaluative criteria the propaganda shaped.
- *Cultural scaffolding* operates through long-timescale osmotic imprinting plus explicit teaching plus structural scaffolding (institutions, roles, rituals). The continuum from ordinary culture to source-compromise is gradient: every adult's option-space is culturally scaffolded; what makes some scaffolding source-compromising rather than developmentally enabling is whether the scaffolding allows reflective access (Mode B over the scaffolded contents) without punishment, exclusion, or institutional retaliation, and whether alternative input-sources are available.
- *Coercive socialization* is osmotic imprinting under conditions where alternative input is suppressed or punished. Cult conditioning, totalitarian ideological training, and severely closed scaffolding environments are the central cases. The agent's adult option-space is structured by osmotic imprinting that occurred without alternatives, often paired with explicit punishment of resistance or doubt.

The architecture's specific contribution: source-compromise need not involve any conscious-targeted manipulation event. Many structurally important forms of source-compromise operate through ambient exposure shaping the option-space invisibly. The agent satisfies inside-perspective conditions of free choice (1–6 internally) while the option-space itself was osmotically constructed in ways the agent has not had opportunity to evaluate or own. This makes the manipulation analysis architecturally specific rather than generic.

Hierarchical-endorsement views in the Frankfurt tradition, when treated as endorsement-only, address acute manipulation poorly and propaganda even worse, because they lack the apparatus to distinguish *internal ownership* from *osmotic source-compromise*. The endorsement-only agent who endorses their first-order desires can be a propaganda-shaped agent endorsing propaganda-shaped desires; the architecture's response combines ownership-integration (condition 6 internal), source-status analysis (the osmotic imprinting continuum), apparent-I / other-I apparatus (the inter-I structure of accountability), and $\rho$/$\Pi$ separation (high $\rho$ does not entail high accountability when source-compromise has occurred). The four apparatuses jointly generate the discriminating analysis Section 9 requires. Source-sensitive descendants in the broader hierarchical-endorsement tradition partially address some of these pressures; [Free Will §5] develops the comparison in detail.

The osmotic-imprinting analysis also bears on developmental-window distinctions. Pre-agential osmotic imprinting (before the I has operator-bundle-mediation capacity at all) is structurally different from post-agential osmotic imprinting under suppressed alternatives. The pre-agential case is non-attributable in the strict sense — the I had no agency capacity at the time. The post-agential case under suppressed alternatives is graded — the I had agency capacity, but the toolset-input was source-compromised at the developmental level. Section 9 develops the responsibility-grading; Section 4.12 establishes the underlying mechanism and continuum.

---

---


---

# 5. Live-option construction and the verification-toolkit

Section 4 established that the verification-toolkit is the universal limiter on what can be willed at any order: the I cannot will what the toolkit cannot construct as live. Section 5 develops the toolkit and its operations in full detail. The section formalizes the live-option construction lemma as the application-level apparatus through which the toolkit-constraint of 4.5 operates, defines the action-space $\mathcal{O}_{m,t}$ formally, develops live-option construction at each order, classifies toolkit failure modes by which sub-condition of the lemma fails, develops toolkit-development mechanics across orders, gives full development to the three willing-strategies introduced in Section 3.4, and uses the toolset-input / operator-bundle distinction to deepen the manipulation continuum first established in 4.12. The section is application-level work throughout: the verification-toolkit, the action-space, the willing-strategies, and the manipulation continuum are all application-level constructs that organize foundation-supplied resources without modifying the foundation.

## 5.1 The verification-toolkit as application-level apparatus

The foundation supplies $\phi$ — the architecture's coordinate for truth-indistinguishability and verification-status (Foundation File 3, Section 7.3). $\phi$ tracks whether contents have been verified, are verifiable in principle, or fall outside the verification system altogether. $\phi$ is a foundation primitive. The *verification-toolkit* is the application-level construct: the coordinated set of $\phi$-bearing operations through which the I constructs, evaluates, and inhabits live options at each order of willing. Foundation File 3, Section 8.6 (verification-tool imprinting dynamics) establishes that verification operations themselves leave traces and develop over time; the toolkit is what those operations cohere into when treated as application-level apparatus.

Three commitments fix what the toolkit is and what it is not.

*The toolkit is not a substance or faculty.* It is a coordinated activity, in the same sense in which the operator-selection bundle is a coordinated activity (Section 3.2, Condition 3). Where this paper uses noun-phrasing — "the toolkit constructs," "the toolkit's repertoire," "the toolkit develops" — the underlying claim is always about coordinated $\phi$-bearing operations the I performs, not about an entity the I has. The will-as-function discipline (Section 3.4) applies to the toolkit as well: the toolkit is what verification-pathway operations do, not a thing that does them.

*The toolkit is application-level, not a foundation primitive.* The foundation supplies $\phi$, the substrate-mediation pathways through which contents reach the I (File 3, Section 8.5), and the three-order pathway typology. The agency paper develops the toolkit as the application-level apparatus that organizes these foundation-supplied resources into live-option construction. The planning document's discipline 5 (no promotion of application-level apparatus to foundation primitive) holds throughout: if the paper exposes a foundation gap, that becomes a foundation-extension proposal, not a unilateral move within the application paper.

*The toolkit operates over substrate-supplied content but is not the substrate.* Substrate processes — perceptual gating, cognitive substrate, somatic substrate, motor substrate — supply the material the toolkit operates over. The toolkit is the I's operator-level construction, evaluation, and inhabitation of live options *from* that substrate-supplied material. The distinction matters: a substrate-rich agent with a thin toolkit constructs few live options (the material is there but the I cannot inhabit it as live); a substrate-poor agent with a developed toolkit constructs whatever the substrate supplies into rich live options (the material is sparse but well-organized for selection). Toolkit-development and substrate-development can dissociate.

The toolkit is therefore best understood as the *application-level coordination of $\phi$-bearing operations into live-option construction at each order of willing*. The lemma in 5.2 specifies the conditions under which a content counts as a live option in that construction.

## 5.2 The live-option construction lemma

The lemma states the conditions on membership in the action-space.

> *Live-option construction lemma.* For a content $c$ at order $n \in \{1, 2, \ldots, N(m,t;d)\}$ to be a live option for agent $m$ at time $t$ in target domain $d$, the verification-toolkit must construct $c$ such that all four conditions hold. Orders 1–3 are *foundational orders* (substrate-supported per the foundation's three-order pathway typology, File 3 §8.5); orders $4 \leq n \leq N(m,t;d)$ are *constructed orders* (application-level target-domain orders developed in Section 5.7). The four conditions:
>
> (i) **Representability.** $c$ is representable by the toolkit as a possible course at order $n$, *at sufficient resolution to be engageable*. The toolkit can construct $c$ as a course-skeleton with reasonable trajectory, even when execution-level details require dynamic elaboration during the will-act. Representability is not a requirement for fully-specified pre-constructed plans; it is a requirement that the toolkit construct enough of the course for the I to take it up as a candidate course with trained expectation of dynamic refinement (Section 3.2's Condition 1 develops this discipline).
>
> (ii) **Evaluability.** $c$ is evaluable by PtCns, PCE-over-projection, $\Pi$-weighting, or frame-relevance against alternatives in the option-space. *Evaluability is a capacity sub-condition of the lemma — the option is available for evaluation. It is not Condition 2 of free choice proper (Section 3.2). Condition 2 requires actual evaluative engagement: PtCns, PCE-over-projection, $\Pi$-weighting, or frame-relevance must in fact engage with the option. An option may be evaluable in the lemma sense and still participate only in thin free selection if evaluative engagement remains absent or merely implicit. The lemma's evaluability is the capacity condition; the free-choice definition's Condition 2 is the corresponding exercise condition. Evaluability over a fuzzy course-skeleton (per the fuzzy-construction discipline of Section 3.2 and 5.3's dynamic-refinement note) means the toolkit can evaluate the projected trajectory of the option even when granular execution-level details remain un-evaluated until dynamic refinement during the will-act; the trained-expectation discipline applies to evaluability as well as to representability.*
>
> (iii) **Implementability.** $c$ is connectable through substrate (foundational orders) or through lower-order will (constructed orders) at order $n$ — focus can be shifted to or sustained on $c$ at first-order; mental operation along $c$ can be carried out at second-order; substrate can execute or scaffold the action-pattern $c$ at third-order; lower constructed-order or third-order implementation is available for constructed orders $n \geq 4$.
>
> (iv) **Inhabitability.** $c$ is inhabitable by the I as a possible course for selection — the I can take up the option's perspective, project itself into it, and treat it as a candidate the bundle could select.

The action-space is then defined formally:

> *Order-$n$ action-space (in domain $d$).* The order-$n$ action-space for agent $m$ at time $t$ in domain $d$ is
> $$\mathcal{O}^n_{m,t;d} = \{c : c \text{ is a live option at order } n \text{ for } m \text{ at } t \text{ in } d\}.$$
> Where the domain is fixed by context, the notation $\mathcal{O}^n_{m,t}$ is used.
>
> *Total action-space (in domain $d$).* The total action-space is the *tagged* (disjoint) union across all orders the agent has developed in that domain, preserving order-tags:
> $$\mathcal{O}_{m,t;d} = \bigsqcup_{n=1}^{N(m,t;d)} \mathcal{O}^n_{m,t;d} = \{(n, c) : c \in \mathcal{O}^n_{m,t;d},\ n \in \{1, 2, \ldots, N(m,t;d)\}\}.$$
> $N(m,t;d)$ is the highest order developed by agent $m$ at time $t$ in domain $d$, bounded by substrate-modeling capacity ∧ toolkit capability *for that domain*. $N$ is *domain-relative*: an agent's $N$ in their professional domain may be much higher than $N$ in unfamiliar domains. Orders 1–3 are foundational (substrate-supported and universal across embodied agents); orders 4 through $N(m,t;d)$ are constructed (mastery-emergent in domain $d$, application-level — Section 5.7 develops this). The same content $c$ may appear in $\mathcal{O}_{m,t;d}$ as $(n,c)$ for multiple $n$, with each tag denoting a distinct live-option status at the corresponding order. Where the section uses $\mathcal{O}_{m,t}$ or $N(m,t)$ without an explicit domain index, the domain-relative reading is implicit.
>
> *Cross-order configurations.* A cross-order option is *not* a higher order; it is a coordinated configuration of order-tagged live-options across multiple orders. Cross-order configurations are defined as
> $$C_{m,t;d} \subseteq \prod_{n=1}^{N(m,t;d)} \mathcal{O}^n_{m,t;d},$$
> the product over the agent's developed orders in domain $d$, with cross-order coherence-conditions specifying which tuples of order-tagged options jointly constitute a coordinated configuration (most actual configurations engage a subset rather than all orders). Section 6's cross-order effort phenomenology, Section 8's variation taxonomy, and Section 10's empirical-interface analysis each rely on this preserved order-tagging across both foundational and constructed orders.

The lemma's four sub-conditions are not independent. Representability is the upstream condition: nothing the toolkit cannot represent can be evaluable, implementable, or inhabitable by the I. Evaluability presupposes representability and supplies the contrastive structure needed for selection. Implementability presupposes representability and a substrate-coupling that can carry the option from selection to execution. Inhabitability presupposes the prior three and adds the I's projective uptake of the option as a candidate course. The conditions form a dependency stack rather than an independent checklist.

The dependency stack describes *membership in $\mathcal{O}_{m,t}$*, not the independent existence of capacities in the substrate or environment. A movement may be substrate-implementable in the abstract without being evaluable here-and-now; a thought may be evaluable without being implementable under current cognitive substrate; an action-pattern may be representable in third-person description without being inhabitable from inside. The conditions become joint members of $\mathcal{O}_{m,t}$ only when all four hold simultaneously for a given content $c$ at order $n$. The architecture's claim is about live-option status, not about which capacities exist independently of the live-option-construction operation that constitutes that status.

Three corollaries follow.

*The total action-space is toolkit-bounded.* The set $\mathcal{O}_{m,t;d}$ is exactly the set of contents satisfying all four sub-conditions at any developed order in domain $d$. Contents the toolkit cannot construct as live are not in the action-space, regardless of what is going on at substrate, in the environment, or in another agent's action-space. This is the formal statement of the universal toolkit constraint of 4.5. The constraint is *universal in form but domain-relative in reach*: in each domain $d$, the I's action-space extends only through the highest order the toolkit has developed in that domain, $N(m,t;d)$. The universal-form / domain-relative-reach distinction holds for both foundational orders 1–3 (universally available across embodied agents but with domain-relative implementation) and constructed orders 4 and above (domain-relative both in availability and in implementation).

*Live status is time-indexed and dynamic.* The same content $c$ may be live for $m$ at $t$ but not at $t'$. Salience shifts, projection-construction, evaluative engagement, fatigue, focus capture, and toolkit-development all alter live-status across time. The lemma is stated at $t$; the dynamic theory of how $\mathcal{O}_{m,t}$ changes over time is the substance of toolkit-development (5.5) and toolkit failure-modes (5.4).

*The contrastive condition for free choice (Section 3.2, Condition 1) requires $|\mathcal{O}^n_{m,t}| \geq 2$ at the engaged order(s).* Free choice requires at least two structurally distinguishable live courses at the order(s) of willing in question, including withholding, refusal, delay, or non-action where genuinely live. The lemma supplies the formal apparatus: a contrastive option-space is two or more contents satisfying the four sub-conditions at the order(s) engaged, jointly available to the bundle.

## 5.3 Live-option construction by order

The lemma's abstract structure is the same at every order; the implementation domain differs. Section 5.3 develops what live-option construction looks like at each *foundational order* in turn — first-, second-, and third-order live-option construction. Section 5.7 generalizes to constructed orders 4 and above, where live-option construction operates over progressively wider not-I structures using lower-order live-options as implementation media. The structural pattern Section 5.3 establishes — toolkit-resources, substrate-coupling, contrastive option-space — extends to constructed orders with target-domain-specific implementation.

**First-order live-option construction.** The toolkit constructs as live the focus-targets attention can move to, sustain, return to, or hold against pull. The toolkit-resources required: salience-detection, focus-stability, perceptual-and-cognitive representation of focus-objects, and the capacity to discriminate one focus-target from another. The contemplative practitioner with a developed first-order toolkit can construct as live a focus-target the untrained practitioner cannot construct at all — the breath as a stable object across many minutes, a subtle bodily sensation as an inhabitable focus, a thought-stream as a noticed object rather than a captured field. The non-meditator may be able to *intend* to focus on the breath but cannot construct sustained focus on it as a live option, because the toolkit-resources for representing the breath stably and returning to it after distraction have not developed. First-order live-option construction is the toolkit-mediated capacity to make focus-targets inhabitable as candidate courses for the I.

**Second-order live-option construction.** The toolkit constructs as live the thought-paths the I can pursue — deliberation-routes, comparison-operations, projection-constructions, framing-shifts, conclusion-entertainments. The toolkit-resources required: cognitive substrate for representational content, projection-toolset for future-state construction (developed application-level in the affect paper's threat-cluster, Section 7, with foundation support from PCE and future-state projection under existential pressure), Mode B reflective access for taking thought-paths as object, and the capacity to discriminate one thought-path from another. The chess grandmaster's toolkit constructs as live a space of move-considerations the novice cannot construct: not because the novice "would not" pursue those thought-paths but because the toolkit cannot represent them stably enough for evaluation. Philosophical training, structured deliberation training, and therapy each expand the second-order toolkit by extending the repertoire of thinkable thought-paths and the projection-apparatus's capacity to represent future-states with sufficient resolution to be evaluable.

**Third-order live-option construction.** The toolkit constructs as live the action-patterns the substrate can execute or scaffold. The toolkit-resources required: motor substrate, embodied affordance, scaffolded autonomic capacity where toolset-mediation makes autonomic processes available as live options, and the capacity to represent action-patterns at sufficient resolution for substrate to implement them. The expert violinist's third-order toolkit constructs as live a vast space of bowing-patterns, fingering-patterns, breath-and-posture coordinations the non-violinist's toolkit cannot construct at all — the substrate may be present in some sense, but the toolkit-mediated representation that connects substrate to selection is absent. Skill acquisition, motor learning, somatic practice, and biofeedback training each expand the third-order toolkit by extending the action-pattern repertoire and the substrate-modulation capacity that makes those patterns implementable.

**Dynamic refinement during execution is structurally normal.** Live-option construction at any order does not require the toolkit to pre-construct every detail of execution. A live course has its general trajectory represented, its evaluative status engageable, its implementation pathway accessible, and its inhabitation possible — but the execution-level specifics elaborate dynamically as the will-act proceeds. The first-order focus-direction "stay focused on the writing" is live when the toolkit constructs sustained-focus on the writing as a course; it does not require pre-constructing every micro-shift of attention across the writing-period. The second-order thought-path "reason through this argument" is live when the toolkit constructs the deliberation-skeleton; it does not require pre-constructing every inferential step. The third-order action-pattern "drive to the store" is live when the toolkit constructs the trip; it does not require pre-constructing every motor-correction. The trained-expectation discipline of Section 3.2's Condition 1 carries through: the I's reasonable confidence in dynamic refinement is what supports liveness when the toolkit constructs at the skeleton level. Mastery (5.7) increases dynamic-refinement capacity within mastered domains; novice agents have lower fuzzy-construction tolerance and need more pre-construction. Substrate-developmental constraints at orders 1 and 2 (5.4) characteristically affect dynamic-refinement-during-execution as much as pre-construction — the substrate cannot reliably sustain operator-bundle direction through the refinement process.

**Cross-order live-option construction.** Many actual options have cross-order live-status. Deliberating about a motor task involves second-order thought-path construction (about the motor task) and third-order action-pattern construction (of the motor task itself), with first-order focus-target construction holding the deliberation steady. The lemma applies independently at each order: a content has live-status at order $n$ when the four sub-conditions hold at order $n$. A cross-order option is one with live-status at multiple orders simultaneously, with cross-order coherence between the order-specific live-options. The architecture's discipline: cross-order options are *not* a higher order (whether across foundational orders 1–3 or across foundational and constructed orders); they are coordinated live-options at multiple existing orders, formalized as elements of the cross-order configuration set $C_{m,t;d}$ (5.2). Section 5.7 develops constructed orders as their own ranks; cross-order coordination is what links them in actual will-scenarios.

## 5.4 Toolkit failure modes

The four sub-conditions of the lemma factor toolkit failures into four structurally distinct *primary analytic* modes. The variation taxonomy in Section 8 develops their pathological extensions; this subsection states the failure modes and their characteristic structural signatures. In real cases multiple sub-conditions may fail together; the four modes identify the *primary analytic failure* — which sub-condition first prevents membership in $\mathcal{O}_{m,t}$, and which downstream contractions follow from that primary failure.

| Failure mode | Failed sub-condition | Structural signature | Representative case |
|---|---|---|---|
| **Construction failure** | (i) Representability | The toolkit cannot represent the content as a possible course at the relevant order | Non-violinist asked to play the passage; framing not yet acquired; concept absent; movement-pattern unlearned |
| **Evaluation failure** | (ii) Evaluability | The toolkit represents the content but PtCns / PCE-projection / $\Pi$-weighting / frame-relevance cannot engage with it | Severe cognitive fog, projection-apparatus damage in learned helplessness, decision-paralysis under unfamiliar value-domains |
| **Implementation gap** | (iii) Implementability | The toolkit represents and evaluates the content but substrate cannot connect to execute or scaffold it | Imagined motor action without motor-substrate support; thought-path representable but cognitive substrate cannot carry the operation through |
| **Inhabitation failure** | (iv) Inhabitability | The toolkit represents, evaluates, and could implement, but the I cannot project itself into the option as a candidate course | Dissociation, fragmented selfhood, frozen contemplation, alienated relation to one's own option-space |

Each failure mode has its own characteristic recovery pathway. Construction failure recovers through toolkit-development that supplies the missing representation — training, education, contemplative practice that builds the repertoire. Evaluation failure recovers through repair of the evaluative apparatus — restoration of cognitive substrate, projection-apparatus repair (the affect paper's Prediction 14 territory), recovery from depression-style projection-collapse. Implementation gap recovers through substrate-development that supplies the missing connection — motor learning, somatic practice, autonomic-modulation training. Inhabitation failure recovers through ownership-integration work — parts work, IFS, trauma-integration practices that allow the I to inhabit options it could otherwise represent, evaluate, and implement.

**Substrate-developmental implementation-gap at multiple orders.** A structurally important case the lemma's failure-mode taxonomy specifies: when substrate-developmental conditions constrain operator-bundle-mediation at orders 1 and 2 specifically, the implementation-gap failure mode operates simultaneously at both orders. ADHD-like executive-function configurations are a central candidate case for this implementation-gap pattern. Executive function — sustained attention, attention-shifting, working memory, response inhibition, planning, task initiation, goal-directed persistence — is operator-bundle-mediated direction at orders 1 and 2; substrate-developmental constraint of executive function constrains exactly this capacity. The toolkit can represent focus-targets and thought-paths, can evaluate them, and the I can inhabit them as candidate courses; what fails is *substrate sustaining the operator-bundle direction over duration* — a first-order implementation gap on focus-stability and a second-order implementation gap on working-memory-mediated thought-path traversal, both rooted in the same substrate-developmental constraint. The fuzzy-construction discipline of Section 3.2's Condition 1 and the dynamic-refinement note of 5.3 sharpen this further: the affected substrate-mediated capacity is not (only) the pre-construction of detailed plans but specifically the *dynamic-refinement-during-execution* that fuzzy live-options depend on. The ADHD agent's toolkit may construct the course-skeleton and the I may inhabit it with reasonable confidence at the moment of engagement; what the substrate cannot reliably support is the sustained operator-bundle direction through which execution-level details would normally be elaborated as the will-act proceeds. This is why ADHD-like configurations characteristically show difficulty with extended will-acts where dynamic refinement is structurally necessary, even when the pre-engagement plan is well-constructed.

In many such cases, input-side substrate pathways — perceptual salience-gating, osmotic-imprinting receptivity, reward-substrate processing — may be intact, amplified, or differently weighted relative to constrained operator-bundle-mediation, producing a characteristic tendency-profile of input-pathway-intact + operator-bundle-output-substrate-constrained: heightened salience capture; osmotic-imprinting sensitization; and disproportionate immediate-reward salience, where near-term reward cues can capture action-priority against constrained second-order $\Pi$-weighting, inhibition, and future-projection. The input/output asymmetry of Section 3.4 is structurally pronounced from substrate development in such configurations.

Recovery in such cases is not simply ordinary toolkit-development of the constrained capacity. Because the constraint is substrate-developmental, recovery often proceeds through structural compensation: substrate-supportive interventions where available (medication, sleep, exercise, somatic regulation), environmental scaffolding, and toolkit-features that route around, stabilize, or partially remediate the constrained capacity. Section 5.8's strategy-availability discussion develops the configurational and slingshot routes that often become disproportionately useful under this pattern.

**State-dependent toolkit contraction.** Distinct from stable failure-modes, $\mathcal{O}_{m,t}$ also shrinks transiently through state-conditions: fatigue, pain, intoxication, trauma activation, panic, shame, grief, sleep deprivation, acute stress, and severe affect-regulation collapse all temporarily contract the action-space without changing the long-term toolkit. State-dependent contraction looks structurally like construction failure, evaluation failure, implementation gap, or inhabitation failure transiently, but the toolkit's underlying capacity is intact and re-emerges with recovery from the state-condition. Recovery to baseline $\mathcal{O}_{m,t}$ tracks recovery from the state-condition rather than toolkit-development. The architecture treats state-dependent contraction as structurally distinct from stable failure-modes; Section 8 develops the variation between transient state-contraction and stable failure, and Section 10 uses the distinction to read affect-state effects on the experimental literature.

**Cross-order failure compounds.** When a primary-order failure occurs, secondary effects propagate to other orders. A second-order toolkit damaged by depression produces fewer thought-paths to engagement; the third-order option-space then contracts because action-patterns require second-order representational support to connect to the bundle; the first-order option-space contracts because attention has fewer worthy targets to construct as live. This is the structural mechanism behind multi-order pathology profiles in 4.6: a primary-order failure produces secondary-order live-option contraction through dependency cascades, even when the secondary orders' toolkits are themselves intact.

The architecture's discriminating prediction here: pathology-by-order profiles should tend to show different cascade signatures depending on the primary failed sub-condition, *where the primary failure can be independently identified*. Construction failure cascades differently from evaluation failure, which cascades differently from inhabitation failure — even when all three failures impair the same order. Section 11 develops this prediction in full; the prediction is conditional on the primary failure being independently identifiable, since real cases often involve mixed sub-condition failures and the cascade signatures must be read against that mixture.

## 5.5 Toolkit-development mechanics

Toolkits develop. The action-space $\mathcal{O}_{m,t}$ at adult $t$ is structurally larger and more differentiated than at infant $t$, and an expert agent's $\mathcal{O}_{m,t}$ is structurally larger at the engaged order than a novice's. The architecture identifies four mechanisms by which toolkits develop, each operating across the three orders with order-specific implementation.

*Practice-driven development* is the most familiar mechanism. Repeated explicit engagement with content at an order — repeated focus on a target, repeated thought-path traversal, repeated action-pattern execution — extends the toolkit's representational repertoire at that order, stabilizes its evaluative engagement, and deepens its substrate-coupling. Foundation File 3, Section 8.6 (verification-tool imprinting dynamics) establishes that verification-pathway operations leave traces; practice-driven toolkit-development is the application-level form of those traces accumulating into expanded repertoire.

*Osmotic toolkit-development* operates without explicit focus. Foundation File 3, Section 8.7 (osmotic imprinting) describes how repeated ambient co-occurrence shapes the I's profile without verification-pathway construction. Toolkits develop osmotically through ambient exposure to operations: a child raised among musicians develops first-order auditory toolkit-features through ambient exposure, even before explicit musical training; an apprentice in a craft develops third-order action-pattern recognition through ambient exposure to skilled practice. Osmotic toolkit-development is structurally significant because it shapes the toolkit before the agent has reflective access to the shaping — which connects to the source-compromise analysis in 5.9 and 4.12.

*Mode B reflective toolkit-development* operates by taking the toolkit's own operations as object. When the I uses Mode B reflective access to attend to its own focus-direction, deliberation-pattern, or action-execution, that reflexive operation can refine the toolkit-operation it takes as object. Contemplative practices that explicitly cultivate meta-attention, philosophical reflection that turns to its own deliberation-procedures, and therapy that examines one's own habitual thought-paths each work primarily through Mode B reflective toolkit-development. The architecture's distinctive claim: Mode B reflective toolkit-development is one Mode B capacity operating across three order-specific object-domains (Section 4.4), not three Mode B subtypes.

*Verification-tool imprinting development* is the foundation's specific mechanism (File 3, Section 8.6). Repeated explicit verification operations — testing claims, checking sources, evaluating outcomes, distinguishing signal from noise — build verification-pathway features that subsequently operate as toolkit-features. The agent who has repeatedly tested whether their first impressions hold up develops a verification-pathway feature that subsequently operates as a toolkit-feature for evaluating new first impressions. The toolkit's verification-pathway features are foundation-grounded; their organization into application-level toolkit operations is the agency paper's contribution.

**Order-specific development.** Each mechanism operates at all three orders, but toolkits at different orders differ in which mechanism dominates their development. First-order toolkit-development is heavily contemplative-practice-and-osmotic — sustained focus capacity grows through both explicit attention training and ambient exposure to focus-rich environments. Second-order toolkit-development is heavily Mode-B-reflective-and-verification-tool — thought-path repertoire expands through both reflective examination of one's own deliberation and explicit verification-pathway construction. Third-order toolkit-development is heavily practice-driven-and-osmotic — action-pattern repertoire grows through repeated explicit practice and through ambient exposure to skilled execution.

**Cross-order transfer is limited.** Training that develops one order's toolkit produces measurable expansion at other orders only insofar as the orders share toolkit-features. Pure first-order concentration practice without semantic load produces limited second-order option-space expansion (the second-order toolkit needs cognitive-substrate support that pure concentration does not develop). Pure third-order motor drills without semantic processing produce limited second-order expansion. Integrated training — practices that engage multiple orders simultaneously, in coordination — produces broader expansion than any single-order training. This is Pred 20 in planning v0.3.1, and Section 11 develops it as a discriminating prediction the literature can investigate.

**Social scaffolding is a delivery context, not a fifth mechanism.** Teaching, coaching, mentorship, institutional training, and broader cultural / social scaffolding are not separate toolkit-development mechanisms at this analytic level. They are *contexts* through which the four mechanisms — practice-driven development, osmotic toolkit-development, Mode B reflective toolkit-development, and verification-tool imprinting development — operate. A coaching session typically combines explicit practice (practice-driven), ambient learning of how things are done (osmotic), reflective examination of one's own performance (Mode B reflective), and explicit verification of claims about technique (verification-tool imprinting). The scaffolding is the delivery channel; the underlying mechanisms remain the same four.

**Toolkit-development is not always expansion.** The same four mechanisms can produce toolkit narrowing, distortion, over-specialization, or source-compromise rather than expansion. Practice-driven development of avoidance patterns narrows the action-space at each order practice repetition reinforces. Osmotic toolkit-development under propaganda or coercive socialization shapes evaluative toolkit-features in source-compromised ways (Section 5.8 develops this). Mode B reflective toolkit-development that operates on distorted or source-compromised contents can entrench distortions rather than refine the toolkit. Verification-tool imprinting under repeated false signals can build verification-pathway features that subsequently misclassify well-formed claims. The direction of toolkit-development — expansion, narrowing, distortion, or source-compromise — is a function of what the mechanisms operate on, not of the mechanisms themselves. Section 8 develops maladaptive toolkit-development as a class of agency-variation, and Section 9 connects maladaptive development to responsibility-attribution along the developmental-window overlay of 4.10.

## 5.6 The output-imprinting cascade

The foundation's three-order pathway typology (File 3, Section 8.5) is framed for *contents reaching the modeling I* — the input direction — and the foundation's verification-tool imprinting (File 3 §8.6) and osmotic imprinting (File 3 §8.7) describe how repeated patterns reaching the I shape the I's profile and toolkit. Section 3.4 extended this typology to the output direction at the level of *operator-bundle-mediated willing*: focus, thought, action as the three orders of willing-operations. Section 5.6 develops a complementary *application-level output-side extension*: the *output-imprinting cascade* — non-bundle-mediated propagation of the I's activity outward through substrate, environment, and to not-I, leaving traces that subsequently become input through the foundation's already-established input pathways. The cascade is application-level work using foundation-supplied resources: the foundation establishes substrate pathways and the imprinting mechanisms; the agency paper develops the complementary output-side application within which the I's own activity also leaves substrate, environmental, and inter-I traces that later return as input. Section 3.4's three orders of willing and the cascade are the two complementary application-level uses of the output direction: bundle-mediated willing and non-bundle-mediated cascade-propagation.

The cascade operates in three structurally distinguishable stages.

**Stage 1: I-level activity imprints next-order substrate.** When the I directs focus repeatedly toward a content-domain, the second-order (cognitive) substrate is shaped by the focus-direction: pattern-recognition develops; the substrate begins producing domain-relevant thoughts spontaneously; the toolkit's representational repertoire in the domain expands. The mechanism is foundation-grounded — File 3, Section 8.6's verification-tool imprinting and Section 8.7's osmotic imprinting describe how repeated activity leaves substrate-traces. Output-imprinting at Stage 1 is the application-level form of these traces accumulating from the I's directed activity. The healthy form is pattern-recognition expanding the toolkit's representational reach in a domain. The pathological form is obsessive rumination — sustained focus on threat, grievance, or self-criticism shaping cognitive substrate to spontaneously produce more threat-relevant, grievance-relevant, or self-critical thoughts, narrative-loop entrenchment, motivated reasoning. The mechanism is the same; what differs is the source-status and adaptiveness of the content the focus directs to.

When the I directs thought repeatedly along particular thought-paths, the third-order (somatic) substrate is shaped: recurrent positive thinking gradually shifts somatic baseline toward less negative affect; recurrent negative thinking shifts it toward more. The architecture predicts this as one stage of the output-imprinting cascade: recurrent second-order thought-paths shape third-order somatic baseline through Stage 1 output-imprinting. Clinical and contemplative practices that report bidirectional thought-feeling effects (cognitive therapy, contemplative practice's affect-regulation, expressive writing's reported somatic outcomes) may be interpretable through this pathway where the underlying mechanism matches; the empirical scope of the prediction and which specific clinical results match is left to subsequent sections and to empirical investigation.

**Stage 2: Third-order substrate state imprints not-I.** The agent's third-order substrate state — body language, voice, expression, motor action, behavior — is observable to other agents and constitutes input to their substrate-mediated input pathways. The man talking loudly on the bus imprints on his fellow passengers' first-order salience pathways; the child who leaves dishes in the sink imprints on the parent's frustration substrate; the therapist's calm presence imprints on the client's somatic regulation; the teacher's tone imprints on the classroom's affective baseline. Stage 2 imprinting also includes environment-shaping: action changes what is there to subsequently encounter, both for the agent and for others. The agent who arranges their workspace imprints the environment with new affordances; the agent who plants a garden imprints the local ecology; the agent who writes down a thought imprints the page (which then becomes input the agent or others can re-encounter).

A structural feature of Stage 2 imprinting requires explicit attention: *the channel is bandwidth-limited*. What propagates from the agent through Stage 2 to not-I is the third-order substrate output, not the agent's full self-definition. Other agents do not receive the agent's whole I-structure, autobiography, projects, evaluative depth, $\Pi$-ranking, or PtCns commitments; they receive what third-order substrate transmits. This is the structural reason the apparent-I / other-I apparatus of Section 4.11 is a distinct apparatus from the I itself: apparent-I content is *constructed* from the bandwidth-limited Stage 2 channel by the receiving agent's own toolkit, and what gets constructed is a function of what third-order substrate transmits and what the receiving toolkit can build from that. The maximally self-defined I is not transmitted; the substrate-channel-limited apparent-I content is.

**Stage 3 (closure): Output-imprinting feeds back as input-imprinting.** The cascade does not terminate at not-I. The substrate the agent's activity has shaped — second-order substrate, third-order substrate, environment, other agents' apparent-I content — subsequently feeds back as input. The agent who has shaped the cognitive substrate through repeated focus encounters domain-relevant thoughts arising spontaneously in subsequent moments. The agent who has shaped the somatic substrate through recurrent thinking encounters affect-baseline shifts in subsequent experiencing. The agent who has shaped the environment encounters new affordances when next they engage. Other agents whose apparent-I-of-the-agent has been shaped by Stage 2 imprinting now imprint differently on the agent in subsequent inter-I interactions. The cascade closes through the input-imprinting pathways the foundation establishes (File 3, Section 8.5): output-imprinting reshapes the substrate from which subsequent input-imprinting then arises. Not every cascade closes into a self-sustaining loop: some Stage 1 → Stage 3 closures decay without further willing-input; some are interrupted by competing dynamics; some require ongoing reinforcement to persist. The architecture treats self-perpetuating loops as one important cascade-closure outcome (developed below as an architectural consequence), not as the necessary outcome of all output-imprinting.

**Architectural consequences across the paper.** The cascade specifies several structures used elsewhere in the paper.

*Configurational willing's causal mechanism (5.7).* Configurational willing's *free choice* is the present operator-bundle-mediated arranging-act — Section 5.7 preserves this discipline. The cascade specifies the mechanism by which the arranging-act produces downstream effects: the present arranging-act is itself a Stage 2 imprinting on environment or other agents; the environment-shaped or other-agent-shaped state subsequently feeds back as Stage 3 closure into the agent's later input-imprinting. The willing-discipline holds (the willing is at the arranging step, not in the downstream cascade); the causal channel is now architecturally specified rather than left abstract.

*Toolkit-development through recurrent willing (5.5).* Several of 5.5's mechanisms operate through Stage 1 → Stage 3 closure. The agent's repeated focus on a domain (Stage 1 imprinting on cognitive substrate) produces substrate-state that subsequently delivers richer cognitive material to the agent's deliberation (Stage 3 closure). Practice-driven development, verification-tool imprinting development, and Mode B reflective toolkit-development each operate partly through this cascade-into-input loop. The maladaptive forms of 5.5 (toolkit narrowing, distortion, source-compromise) are the same cascade operating with maladaptive content.

*Self-perpetuating loops as a structural category (Section 8).* When the cascade closes in self-reinforcing patterns, self-perpetuating loops result. The focus-rumination loop runs: focus on threat → cognitive substrate produces threat-thoughts spontaneously → somatic substrate enters threat-state → input-imprinting brings threat-feelings to the I → first-order salience capture by threat-cues → renewed focus on threat. The cascade closes back through input-imprinting; the loop sustains without further explicit willing once the substrate is sufficiently shaped. Healthy self-perpetuating loops (productive habit, secure-attachment cycle, contemplative-practice self-deepening) and pathological self-perpetuating loops (rumination, addiction, trauma-cue cycle) can be *cascade-topologically identical* — the same output-imprinting / input-imprinting loop-form is present in both. They differ at *other* architectural dimensions: content source-status, $\Pi$-alignment, PtCns coherence, $\rho$-flow integration within the operator-bundle, substrate-capture status, ownership-integration, and adaptiveness. Cascade-topology identity does not entail full architectural identity; the variation taxonomy of Section 8 distinguishes healthy and pathological loops by these other dimensions, not by reducing them to topology.

*The manipulation continuum's structural mechanism (5.9).* Section 5.9's manipulation continuum can now be grounded mechanistically: the manipulator's Stage 2 third-order output is the manipulated agent's input-substrate input. Inter-I cascade-coupling is the structural channel through which one agent's activity shapes another's option-space construction. Manipulation, propaganda, modeling, cultural transmission, and many other inter-I phenomena all operate through this layer. Section 5.9 develops the source-compromise dimension; the cascade supplies the channel.

*ADHD-like configurations and the cascade's relative autonomy from bundle-mediation (4.6, 5.4).* Operator-bundle-mediated willing at orders 1 and 2 may be substrate-developmentally constrained without the cascade's downstream propagation being constrained. The man talking loudly may not be sustaining first-order operator-bundle-mediation of voice-modulation; his third-order substrate continues to imprint on fellow passengers regardless of whether bundle-mediated voice-modulation is occurring. The cascade operates as long as substrate dynamics operate; it does not require sustained bundle-mediation at upstream stages. This refines the input/output asymmetry framing: the *output side has two distinguishable layers* — bundle-mediated willing (constrained in ADHD-like configurations per 5.4) and non-bundle-mediated cascade-propagation (operating regardless). Section 9's responsibility analysis must respect this layered output structure. *The fact that cascade effects fall within the agent's structural domain does not by itself settle accountability.* Section 9 must ask whether the agent had live options for anticipating, arranging around, mitigating, or repairing those cascade effects, and whether those options were developmentally available rather than merely externally imaginable. The question of accountability shifts from "was the willing free?" to "were live mitigation, anticipation, or repair options developmentally available, and did the agent engage them where they were?" — a question that engages the developmental-window apparatus of 4.10, the source-compromise apparatus of 5.9, and the layered output structure simultaneously.

The output-imprinting cascade and the foundation's input-imprinting structure together specify how the I's activity reaches outward and how that reach feeds back. The cascade is the structural substrate of much of the agency paper's later material on self-shaping, inter-I dynamics, responsibility for downstream effects, and the developmental loops by which agents become who they become.

## 5.7 N-order will and the action-space lattice

**The two senses of "order."** "Order" is used in this section in two related but non-identical senses, and the distinction is structural. *Foundational orders 1–3* are substrate-mediation orders supplied by the foundation: focus, thought, and substrate-mediated action correspond to the foundation's three-order pathway typology (File 3 §8.5), each supported by a dedicated substrate layer (salience-gating, cognitive substrate, somatic substrate). They are universal across embodied agents because the foundation's pathway typology is universal across substrate. *Constructed orders 4 and above* are application-level target-domain orders: ranks of live-option construction over progressively wider not-I structures, made possible by mastery and toolkit-development, implemented through lower-order willing. Constructed orders do not add substrate pathways and do not modify the foundation's order typology. The shared word "order" across these two senses tracks a real structural continuity (each higher rank operates over a wider domain using lower ranks as medium), but readers should never read constructed-order claims as foundation-pathway claims, and the agency paper makes no such claim.

Sections 3.4 and 4.4 introduce the three foundational orders. Section 5.7 develops the application-level extension: will is in principle *N-order*, with constructed orders 4 through $N(m,t;d)$ emerging through mastery in domain $d$, where $N(m,t;d)$ is bounded by substrate-modeling capacity ∧ toolkit capability for the relevant target domain. $N$ is *domain-relative*: an agent may be sixth-order in institutional law, fifth-order in team coordination, fourth-order in family negotiation, and only third-order in another domain. Where this section uses $N(m,t)$ without a domain index, the reading is "$N$ in the relevant domain"; the domain-relative form is implicit unless otherwise specified.

**Constructed orders.** A constructed order has a target domain that is wider than foundational orders' own-substrate domains. The fourth order targets *immediate not-I structure* — asking-protocols, dyadic interaction conventions, direct interpersonal coordination. Asking a teammate to look something up, directing someone to do a task, lying to influence another agent's verification toolkit, requesting help, instructing, persuading, comforting, threatening: all are fourth-order will-acts when the target of willing is the not-I coordination structure as such. The fifth order targets larger not-I structures — small-group coordination, team dynamics, role-and-relationship structures sustained over time. Directing a team, leading a small organization, sustaining a household, running a project: fifth-order will-acts. The sixth order targets institutional, organizational, or systemic structures, and so on, with each higher constructed order operating over progressively wider not-I structures.

**Membership test for constructed-order options.** Not every utterance or action that produces social effects is a constructed-order will-act. A live option $c$ belongs to a constructed order $n \geq 4$ at target domain $d$ for agent $m$ at time $t$ only if all of the following hold:

1. The option targets a not-I structure as such (the structure-in-not-I is the target, not merely an incidental consequence of a lower-order act).
2. The toolkit represents leverage over that structure (the agent's toolkit can construct the option as engaging the structure, not merely as producing a sound or motion).
3. Lower-order implementation is available (the agent has the third-order substrate action and any intermediate constructed-order capacities required to implement the higher-order will-act). *"Available" here is governed by the same fuzzy-construction discipline as Condition 1 of free choice (3.2): lower-order implementation must be sufficiently representable at the skeleton level for the I to have trained expectation of dynamic refinement during execution. Full pre-construction of every lower-order executable detail is not required.*
4. Success conditions for the option are partly outside the agent's own substrate (the structural outcome the will targets requires not-I uptake, response, or coordination — it is not a target the agent's own substrate alone can satisfy).
5. The option-space includes alternatives at the target-structure level (the agent has at least one other live option at the same target-structure level — different things to ask, different ways to direct, different not-I responses to elicit).

| Act | Classification |
|---|---|
| Mechanically saying "please move" without targeting a coordination outcome | Third-order vocal action with social-effect side-effect |
| Asking someone to move as a social-protocol act with the coordination outcome as target | Fourth-order immediate-not-I will-act |
| Directing a team's movement through a coordinated plan engaging team coordination structure | Fifth-order group-coordination will-act |
| Changing a hospital's triage protocol through engagement with institutional structure | Sixth-order institutional/systemic will-act |

Without the membership test, constructed orders would over-include ordinary third-order acts whose social effects are non-bundle-mediated cascade-Stage-2 imprinting (5.6) rather than bundle-mediated direct will into not-I structure. The membership test and the live-option lemma (5.2) operate in sequence, not in competition: *the constructed-order membership test classifies a candidate $c$ as belonging to constructed order $n$ in domain $d$; the live-option lemma then determines whether that classified candidate satisfies the four sub-conditions for membership in $\mathcal{O}^n_{m,t;d}$.* The membership test is therefore the constructed-order specialization of the live-option lemma's order-classification step, not a freestanding alternative theory of liveness.

Each constructed order *uses lower-order will as its implementation medium*. Fourth-order asking is implemented through third-order vocal/written/gestural action; fifth-order team-direction is implemented through fourth-order direct-asks plus third-order action plus second-order strategic deliberation. Higher-order will-acts are recursively implemented down through the lower orders, ultimately bottoming out in third-order substrate action that is the medium through which the will reaches not-I. The cascade of 5.6 then propagates the third-order substrate output through Stage 2 imprinting — but for higher-order will-acts, the cascade is downstream of and alongside the bundle-mediated will, not a substitute for it.

**The not-I structure that 4th-order-and-higher will engages** is often partly the cumulative cascade Stage 2 imprinting of many agents' activity over historical time, though not all not-I structures crystallize from such accumulation. Linguistic conventions exist because of accumulated vocal action; social interaction protocols typically exist because of accumulated dyadic exchange patterns; many institutional structures exist because of accumulated coordinative action and explicit institutional construction. Some not-I structures arise instead through formal design, legal codification, technical specification, or explicit construction without prior gradual accumulation. Where the structure-in-not-I that the present agent's fourth-order will engages is comprised of previously-learned 3rd-order activity, this holds in two complementary senses: (a) the structure exists because of accumulated cascade Stage 2 imprinting of prior 3rd-order activity (one's own and others'); (b) the present will-act that engages the structure is implemented via the agent's own learned 3rd-order action. The agent who asks for the salt at the dinner table engages a structure-in-not-I (the conversational convention) that crystallized from accumulated linguistic activity, and engages it through learned 3rd-order vocal action of the agent's own.

**Mastery as construction-compression: mastered-domain willing.** Constructed orders develop through toolkit-development of the relevant target domain. A novice's fourth-order action-space is small; an experienced negotiator's is vast. Mastery in a domain has a specific structural feature: *willing in mastered sub-domains becomes intrinsic-to-toolkit (compiled) rather than explicitly constructed*. The skilled adult does not construct each request from scratch; the asking flows directly. The experienced manager does not deliberately assemble each act of team-direction; it runs as mastered-domain willing. The grandmaster does not consciously reason through each chess move at a familiar position; the move presents itself directly. *Mastery compresses construction; it does not bypass the six conditions of free choice (Section 3.2).* The live-option space is generated faster and with less explicit assembly; evaluative engagement may be implicit but remains active where the act is free choice proper; operator-bundle mediation remains present (the bundle-engagement is direct rather than constructed); substrate-coupling is highly trained implementation rather than substrate bypass; Mode B remains available even when not exercised during flow; ownership-integration remains required. Mastery does not eliminate will (this would violate the will-as-function discipline of 3.4); it transforms how the will-functions are exercised in mastered sub-domains.

| Six-condition status under mastery | Form in mastered-domain willing |
|---|---|
| 1. Contrastive live-option space | Compressed but still contrastive; if no alternatives are live, the event is automatic skill execution rather than free choice proper |
| 2. Evaluative engagement | Often implicit / trained / pre-compiled, but still engaged for free choice proper |
| 3. Operator-bundle selection | Direct and low-friction, not absent |
| 4. Substrate coupling | Highly trained implementation, not substrate bypass |
| 5. Mode B availability | Available even if not exercised during mastered-domain flow |
| 6. Ownership-integration | Action integrates as the I's action; sourcehood depends on how the mastery itself developed |

Mastery is compatible with all three willing-strategies (5.8): direct mastery, configurational mastery, and slingshot mastery are all possible — strategy and mastery are orthogonal.

*Mastery and dynamic-refinement capacity.* Beyond construction-compression of pre-engagement option-construction, mastery includes high *dynamic-refinement capacity during execution* — *within the mastered domain and within the variance-envelope the toolkit has learned to handle*. A mastered will-act proceeds on a fuzzy course-skeleton (per Section 3.2's Condition 1 fuzzy-construction discipline and 5.3's dynamic-refinement note) with the trained expectation that execution-level details will elaborate as the will-act proceeds. The grandmaster's mastered chess-move flows because the toolkit constructs the next move's specifics from the position-state during execution, not from pre-rehearsed scripts — *but only over board-states within the variance-envelope of positions the grandmaster's training has prepared*; outside that envelope, the master may return to explicit construction or fail. The experienced negotiator's mastered fourth-order will-act flows because the toolkit constructs the next persuasive move from the addressed agent's response during execution — *but only within the negotiation-types and counter-move ranges the negotiator's experience has covered*. Mastery's dynamic-refinement capacity is what makes the trained-expectation discipline of Condition 1 robust in mastered domains; novice agents in the same domain face higher refinement-resistance because their toolkits supply weaker trained-expectation grounds for fuzzy construction. The domain-bound and variance-envelope-bound character of mastery means that mastery in one domain does not transfer to dynamic-refinement capacity in another domain or in variance regions outside the training, and mastery does not guarantee successful refinement in novel edge-cases.

**Source-compromised mastery.** Mastery does not guarantee autonomy. A mastered domain can be source-clean or source-compromised. Mastery affects how *efficiently* a will-function is exercised in a domain; *source-status* determines whether the option-space and aims are autonomy-supporting, scaffold-captured, coercive, manipulative, or otherwise compromised. Examples of source-compromised mastery: deception mastery developed through coercive socialization (a skilled liar trained from childhood in an environment where deception was rewarded); institutional mastery formed under propaganda (a skilled bureaucrat whose toolkit was shaped by indoctrination); skilled manipulation acquired inside cultic training; habit-mastery rooted in addiction or trauma. The same compiled / intrinsic-to-toolkit efficiency operates in source-clean and source-compromised mastery; the source-compromise is at the source-status level, not the mastery level. Section 9's responsibility analysis must therefore engage source-status of mastery alongside source-status of any particular will-act exercising that mastery.

**The action-space lattice (informal).** Mastered domains form a *lattice-like structure* — the term "lattice" is used informally in this section for a partially-ordered mastery-and-dependency structure; no formal lattice axioms (meet, join, completeness) are claimed here, and formal partial-order specification is deferred to technical addenda. The lattice-like structure's points are mastered domains; its organization includes order-rank (each domain belongs to a particular order), cross-order dependency (higher-order domains require lower-order availability for implementation), and cross-domain plurality at each order (many distinct fourth-order capacities exist, many distinct fifth-order capacities exist, etc.). A complex will-scenario is a *configuration* across the lattice-like structure: specific points engaged across multiple orders simultaneously, with cross-order coherence-conditions connecting them. Negotiating a contract activates a configuration involving multiple fourth-order moves (asking, persuading, possibly threatening), second-order strategic deliberation, first-order sustained focus, and possibly fifth- or sixth-order institutional-protocol engagement. The action-space (in domain $d$) is the union over all live-options across all developed orders in that domain; the lattice-like structure is the organization within which configurations are constructible.

**Three orthogonal dimensions of will-structure.** The architecture now has three orthogonal dimensions for characterizing any will-act: *order* (target domain — what the will operates over), *strategy* (effort-economy approach — direct, configurational, slingshot per 5.8), and *mastery* (intrinsic-to-toolkit / compiled-domain willing vs explicitly constructed willing in the relevant sub-domain). Any actual will-act has values along all three dimensions. The novice consciously direct-wills at first-order (sustained focus on a target requires construction, no mastery); the experienced negotiator slingshot-wills at fourth-order (timing a request to favorable conditions, mastered) while configurational-willing at fifth-order (arranging the institutional context to support the negotiation, mastered). The architecture's discipline is preserved at every order, strategy, and mastery-level: the six conditions of free choice (3.2), the operator-bundle-mediation requirement (3.4), the universal toolkit constraint (4.5), the source-compromise apparatus (5.9), and the ρ/Π separation (4.9) all apply.

**Fourth-order coordination is not fourth-order manipulation.** Fourth-order will is structurally morally neutral. Asking for help, directing a teammate, instructing, comforting, coordinating, teaching, and many other interpersonal coordination acts are autonomy-supporting fourth-order will-acts. *Manipulation is specifically the case of a fourth-order-or-higher will-act with source-compromised aim or effect on the recipient's autonomy* — e.g., lying to trick another agent's verification toolkit; deceiving to bypass another's evaluative engagement; coercive directing that exploits asymmetric power to suppress the recipient's option-space; manipulative comforting that maintains dependency rather than supporting recovery. The manipulator's side is bundle-mediated fourth-order will targeting a structure-in-not-I (the receiving agent's verification-toolkit operations and apparent-I content). The manipulated agent's side is what 5.9's source-compromise continuum addresses (toolset-input poisoned by the manipulator's fourth-order activity). The architecture's moral apparatus is at the source-status level, not the order level: distinguishing autonomy-supporting from manipulative fourth-order will-acts requires examining source-status of the aim, $\Pi$-alignment of the willing, $\rho$-flow within the operator-bundle, and effects on the other agent's autonomy. Section 9's responsibility apparatus does the moral work, applying the responsibility-attribution analysis along the source-compromise continuum (5.9) and the developmental-window overlay (4.10) to fourth-order-and-higher will-acts.

**Action-space variation across agents and time.** The N-order generalization gives the architecture a clean characterization of agent complexity: agents differ in the height of $N(m,t;d)$ across domains $d$, the breadth of mastered domains at each order, and the structure of cross-order coordination across the lattice-like structure. A young child may have $N \approx 3$ across most domains with emerging fourth-order capacities in some; a typical adult has $N \in \{4, 5, 6\}$ depending on domain; an expert in a domain has high $N$ in that domain specifically with proportionally large $\mathcal{O}^n_{m,t;d}$ at the relevant orders. The same agent may be sixth-order in their professional domain while fourth-order in unfamiliar institutional domains. Action-space scope thus varies dramatically across agents and across domains-within-agents, in ways the architecture predicts and Section 8's variation taxonomy can characterize. Substrate-developmental constraints (5.4) bound $N$ by limiting substrate-modeling capacity at the relevant orders. Toolkit-developmental constraints (5.5) bound $N$ by limiting which constructed orders can be developed in which domains. Source-compromised toolkit-development (5.5, 5.9) can produce constructed-order capacities whose source-status is compromised (e.g., a manipulator who has mastered fourth-order deception is operating with a source-compromised fourth-order toolkit — high mastery, compromised source-status).

**Forward dependencies.** Sections 6 and onward operate over the N-order generalization rather than the three-order specialization. Section 6 develops effort/will/trying across all developed orders, with effort-economy comparisons at higher orders. Section 8's variation taxonomy extends to constructed-order variations: fourth-order dysfunction (interpersonal-direction failure, deception-toolkit pathology), fifth-order dysfunction (team-direction failure), institutional-engagement variations, and so on. Section 9's responsibility analysis addresses fourth-order-and-higher will-acts directly: the manipulator-as-agent treatment, the leader-as-agent treatment, the institutional-actor treatment. Section 10's empirical-interface analysis can engage the developmental literature on constructed-order acquisition (theory-of-mind, perspective-taking, institutional-role-acquisition) within the same architectural framework.

## 5.8 The three willing-strategies in full

Section 3.4 introduced direct, configurational, and slingshot willing as strategic profiles on a toolkit-richness continuum, not three separate willing-mechanisms. Section 5.8 develops them in full now that the toolkit apparatus and the N-order generalization (5.7) are in place; the strategies apply across all developed orders, with mastery as a third orthogonal dimension (5.7). All three are operator-bundle-mediated free-choice configurations satisfying the six conditions; they differ in the kind of toolkit-richness they exercise and in the effort-economy of their operation.

**Direct willing.** The agent fires operator-bundle engagement at a direct outcome and sustains it against substrate-pull and competing dynamics. The willing-act and the targeted outcome are temporally and structurally proximate: the agent wants to do $X$, and the bundle directs operator-substrate effort toward doing $X$ now. Effort tracks the magnitude of operator-substrate tension across the willing-period. Phenomenology: the feel of pressing against resistance, the strain of holding direction across time, the relief of cessation when the outcome is achieved or the willing-period ends. Direct willing is the developmental baseline — the toolkit-feature that develops earliest and operates most universally. Novice agents in any domain operate primarily through direct willing, because configurational and slingshot willing require additional toolkit-resources their toolkits have not yet developed.

Direct willing is well-suited to short-horizon goals, immediately implementable actions, and contexts where the substrate and environmental dynamics are roughly neutral with respect to the goal. It is poorly suited to long-horizon goals (effort cannot be sustained continuously across long time-spans without depletion), recurring substrate-pull (the willing must be re-engaged after every substrate-driven distraction), and depleted operator-resources (when the bundle's engagement-capacity is low, direct willing fails first).

**Configurational willing.** The agent uses present operator-bundle engagement to arrange *future conditions* that will subsequently produce goal-relevant outcomes through downstream osmotic dynamics, without the agent's continued direct effort being required. The architecture is precise about the willing-act here: the *free choice* is the present operator-bundle-mediated act of arranging the configuration. The subsequent osmotic imprinting of the agent's profile by the arranged configuration is *downstream causal structure*, not the willing-act itself. The agent who arranges their environment to support a habit is exercising free choice now; the habit's subsequent operation through ambient cue-and-response is causal structure the agent set in motion, not a continuing willing-act.

This distinction matters because it preserves operator-bundle-mediation as a defining feature of willing. Configurational willing is not a way of "willing through ambient processes"; it is a way of using present willing to set causal structure that subsequently operates without ongoing willing. The agent's relation to the downstream effects is the relation a present arranging-act bears to the causal structure it sets in motion, not an ongoing willing-relation.

Configurational willing-acts cover a wide spectrum: habit architecture (arranging environments and routines so that desired actions become osmotically supported), environmental design (workspace layout, social-context arrangement, information-diet curation), pre-commitment devices (binding present arrangements that constrain future option-spaces), training regimens (arranging present practice so that future toolkit-features emerge), and longer-form scaffold-arrangements (career trajectories, household structures, institutional engagements that support the agent's longer-term direction). Each is a present operator-bundle-mediated arranging-act with downstream osmotic effects.

Effort-economy: configurational willing distributes effort over time. The arranging-act is itself a willing-act with its own effort-cost, but the downstream effects do work the agent would otherwise have to do directly. An agent who arranges their environment to support exercise pays effort once at the arranging step, then is supported by ambient cue-and-response thereafter; an agent who tries to direct-will exercise every day pays effort continuously across every day. Configurational willing's effort-economy improves with toolkit-development: a richer projection-apparatus and a more developed PCE-over-projection capacity allow the agent to identify and arrange configurations that more reliably produce desired downstream effects.

Toolkit-richness requirement: configurational willing requires projection-apparatus capacity for representing future-state configurations, PCE-over-projection capacity for evaluating those configurations against preservation-implications, $\Pi$-evaluation capacity for ranking arrangements by preservation-priority, and an architectural understanding (explicit or implicit) of how the agent's own osmotic-imprinting dynamics work. Novice toolkits cannot construct configurational willing-acts as live options because the projection-and-arrangement-evaluation toolkit-resources are not yet present.

**Slingshot willing.** The agent times operator-bundle engagement to leverage available substrate, environmental, or social gradients. The willing-act is a small, precise engagement at a moment when existing dynamics can carry the goal forward; the energy comes from the gradient, the willing supplies direction and timing. Phenomenology: the feel of catching the wave, of moving with the gradient, of acting at the right moment with minimal force.

Slingshot willing is the most toolkit-rich of the three strategies. It requires gradient-reading capacity (perceptual-and-projective construction of the configuration of substrate and environmental dynamics at the relevant time), $\Pi$-evaluation of timing (which moment in the gradient configuration is the kairos moment for action), and precise willing-act capacity at the kairos moment (the willing must be small enough to leverage the gradient rather than fight it, but precise enough to direct the gradient's force toward the goal).

Effort-economy: slingshot willing minimizes effort per unit goal-progress when the gradient-configuration is favorable, but requires substantial toolkit-development to read gradients reliably. The novice who tries to slingshot-will typically misreads the gradient configuration and either misses the kairos moment or pushes in the wrong direction; the developed practitioner recognizes the gradient configuration and times the willing-act accurately. Slingshot willing's effort-economy is highly variable: when the toolkit reads the gradient correctly, effort is minimal; when the toolkit misreads, effort is wasted on a willing-act that does not connect to gradient-force.

**Mixed and temporally-extended profiles.** Many actual willing-acts are not pure instances of one strategy. *Receptive willing* (low direct intervention with high gradient-reading) is typically configurational or slingshot willing with the direct-component minimized — the agent arranges or times rather than presses. *Distributed willing* (across extended timescales and social-or-institutional scaffolds) is configurational willing distributed temporally over many arranging-acts. *Counter-cyclical willing* (deliberately willing against current gradients to reshape future toolkit or substrate conditions) is direct willing under unfavorable gradient-conditions, often configurationally aimed at future toolkit-capacity that the present direct willing produces by training. These cases are not new strategies; they are mixed or temporally-extended profiles of the three forms.

**Developmental trajectory.** Novice agents in any domain operate primarily through direct willing. Intermediate agents have toolkit-resources for configurational willing in the relevant domain. Mature agents have toolkit-resources for slingshot willing in well-developed sub-domains. Expert agents mix all three by situation: direct willing for short-horizon goals where the gradient is neutral, configurational willing for long-horizon goals with shapeable conditions, slingshot willing for opportune-moment situations where gradient-reading is reliable. *The live-option status of configurational and slingshot courses is itself assessed under the fuzzy-construction discipline of Section 3.2 (Condition 1): for these strategies to be live, the agent's toolkit must be able to construct the configurational-arrangement or slingshot-timing course at skeleton-level resolution with trained expectation of dynamic refinement during execution. The novice's toolkit typically cannot construct even the skeleton-level option for these strategies with grounded trained expectation; the configurational/slingshot strategies become live when the toolkit develops the capacity to construct and refine such courses, not merely when the agent recognizes them as possible in the abstract.* The developmental trajectory is from direct-only through configurational-becomes-available to slingshot-becomes-available to fluent mixture-by-situation. Pred 22 in planning v0.3.1 — the configurational/slingshot to direct-willing ratio as a developmental marker, with effort-economy per unit goal-progress as an operational measure — is fixed in this developmental analysis.

**Substrate-developmental constraints reshape the trajectory.** The standard novice-to-expert trajectory assumes substrate that can support all three strategies once toolkit-resources develop. Substrate-developmental constraints on operator-bundle-mediation at orders 1 and 2 (ADHD-like executive-function configurations as the central candidate case, per 5.4) reshape the trajectory non-trivially. Direct willing requires sustained operator-substrate tension at orders 1 and 2 — exactly the substrate capacity these constraints affect. Configurational willing redirects future osmotic-imprinting pathways, leveraging the same osmotic-imprinting mechanism such substrates are often sensitized to, and offloading the need for sustained direct effort. Slingshot willing leverages gradients, working with rather than against the substrate's gradient-sensitivity. The architecture predicts that substrate-developmental constraint of this form, *when paired with sufficient toolkit-development to construct configurational and slingshot options as live*, produces a characteristic *tendency-profile*: constrained direct-willing capacity with proportionally greater configurational and slingshot strategy-availability where toolkits have developed those options. This is consistent with the clinical literature's "external structure" recommendations for ADHD and with reports from ADHD agents who develop systems-and-environments rather than relying on sustained direct effort. The relationship between substrate-developmental constraint and willing-strategy-availability is therefore not just compensation under deficit; it is a structurally specific strategy-distribution shaped by which substrate capacities are available and which are constrained — but it is a tendency-prediction, not a universal trajectory: substrate-developmental constraints without toolkit-development of configurational and slingshot strategies leave the agent with constrained direct willing and no compensating strategies, which is itself a structurally specifiable agency-configuration Section 8 develops.

**Pred 22 operational markers.** Pred 22 (planning v0.3.1) — the configurational/slingshot-to-direct-willing ratio as developmental marker with effort-economy per unit goal-progress as operational measure — needs operationalization to support promotion to confirmed prediction status in Section 11. Candidate markers:

| Marker | Operationalization |
|---|---|
| Direct-willing load | Duration of sustained operator-substrate tension; re-engagement frequency after interruption; depletion-onset reports |
| Configurational strategy use | Number and quality of environment-shaping or pre-commitment acts within a goal-relevant period |
| Slingshot strategy use | Timing accuracy of willing-acts relative to favorable substrate or environmental gradient-conditions |
| Effort-economy | Goal-progress per unit reported effort or behavioral effort-cost |
| Developmental ratio | Proportion of direct vs configurational/slingshot strategy deployment over repeated tasks |

These markers are application-level operationalizations the empirical literature can investigate. Substrate-developmental constraints on direct willing should produce characteristic patterns across these markers (high direct-willing load with poor effort-economy combined with proportionally higher configurational/slingshot deployment in toolkit-rich agents), distinct from acquired depletion patterns (transient elevation of direct-willing load with toolkit-richness intact). Promotion to confirmed prediction status remains reserved for Section 11.

**Wisdom-tradition resonance.** Aristotelian *phronesis* (practical wisdom in knowing when to act, what gradients are available, when to wait), Greek *kairos* (opportune-moment timing as distinct from clock-time), Daoist *wu-wei* (often mistranslated "non-action," more accurately effortless action through gradient-alignment), Hebrew *et* (appropriate season for an action), and modern self-regulation theory (willpower as depletable, conserved through pre-commitment and stimulus control) each track motifs that can be structurally translated into the architecture's direct/configurational/slingshot taxonomy. The architecture offers a structural translation of one shared pattern these traditions track in their own idioms; it does not claim to reduce those traditions to this taxonomy. Each tradition's specific commitments, framings, and practical recommendations remain its own; the architecture supplies a common structural vocabulary that allows the traditions to be compared without flattening any of them.

## 5.9 The toolset-input / operator-bundle distinction and the manipulation continuum

Section 4.12 introduced the source-compromise continuum (acute manipulation, propaganda / indoctrination, cultural scaffolding, coercive socialization). Section 5.9 deepens that continuum using a structural distinction the toolkit apparatus makes available: the distinction between *toolset-input* and *operator-bundle*.

**Toolset-input.** The toolkit operates over input — substrate-supplied content, environmental-supplied salience, other-I-supplied apparent-I content, prior-osmotic-imprinting-supplied profile-features, and the agent's own prior willing-acts (configurational and otherwise) that have shaped present input-conditions. Toolset-input is what the toolkit has to work with. The toolkit's live-option construction operates over toolset-input by representing, evaluating, implementing, and inhabiting candidates drawn from input.

**Operator-bundle.** The operator-bundle operates over toolkit-output — over the live-options the toolkit has constructed. The bundle selects from the live-option space; the toolkit constructs the space. The two are application-level coordinated activities at different stages of the choice-process stack (Section 3.3): the toolkit at stage 2 (option-space construction); the bundle at stage 4 (selection from the constructed space).

**Manipulation poisons toolset-input; the operator-bundle can be intact while the input is poisoned.** This is the architecture's structurally specific account of manipulation: a manipulated agent's bundle operates correctly over the live-option space the toolkit constructs, but the toolkit constructed the space from poisoned input. The agent's bundle-selection is structurally sound; the agent's option-space is source-compromised. From the inside, the agent's choosing feels free and operates through correctly-functioning machinery; from the outside, the option-space the agent chose from was shaped by inputs the agent has not had the opportunity to evaluate or own.

The distinction lets the manipulation continuum of 4.12 be specified more precisely:

| Source-compromise mode | Mechanism | What is poisoned |
|---|---|---|
| Acute manipulation | Local toolset-input poisoning with explicit (though perhaps unrecognized) input | Specific input-content for the present choice |
| Propaganda / indoctrination | Long-term osmotic toolset-input shaping | Accumulated input-content shaping option-space construction across many choices |
| Cultural scaffolding | Long-timescale osmotic input shaping plus explicit teaching plus structural arrangements | Accumulated input-content plus structural channels through which input arrives |
| Coercive socialization | Osmotic input shaping under suppression of alternatives | Accumulated input-content with restricted input-diversity |
| Pre-agential developmental imprint | Pre-agential osmotic shaping before operator-bundle-mediation capacity | Foundation-level toolkit-features shaped before agency was available |

The first four are post-agential source-compromise modes; the agent has agency-capacity but the input is compromised. The fifth is pre-agential and structurally distinct (Section 4.10): the agent did not yet have the agency-capacity to evaluate the imprinting at the time of imprinting.

**Configurational willing's relation to manipulation.** A subtle case the toolset-input / operator-bundle distinction handles: when an agent uses configurational willing to shape their own future toolset-input — arranging environments, curating information-diets, building habit-architectures — that is *not* source-compromise. The present arranging-act is operator-bundle-mediated; the agent owns the act and its downstream input-shaping. By contrast, when external scaffolding shapes the agent's future toolset-input without the agent's operator-bundle-mediated involvement, that is source-compromise. The structural difference: configurational willing is the agent's own bundle-mediated arranging of future input; manipulation is the externally-mediated arranging of the agent's future input without the agent's bundle-engagement. Both produce downstream osmotic effects on toolset-input; only one is the agent's own.

This generalizes: an agent's *self-curation* of their own toolset-input through configurational willing is autonomy-supporting *when the arranging-act itself is sufficiently non-source-compromised*. The operator-bundle-mediated arranging-act preserves sourcehood across the temporal extension *only if* the arranging-act is itself source-clean at the moment of arrangement. If the present arranging-act is already shaped by addiction, manipulation, self-deception, distorted $\Pi$-ranking, or prior coercive socialization, then the downstream self-curation may *preserve or intensify* source-compromise rather than support autonomy. Examples: addiction-driven environment-curation that increases substance-availability; motivated-reasoning information-diet that filters out contradicting evidence; cultic "voluntary" commitment whose voluntariness sits on top of prior source-compromise; self-deceptive social filtering that maintains a distorted self-narrative. The general principle: configurational willing inherits source-status from its arranging-act. Source-compromise in the broader sense is the case where the agent's toolset-input is being shaped by processes — whether external (manipulation, propaganda, coercive socialization, pre-agential imprinting) or internal-but-source-compromised (the agent's own configurational acts performed under prior source-compromise) — that the present agent has not had the opportunity to take up and evaluate from a source-clean position. Section 9's responsibility analysis must therefore evaluate not just whether an arranging-act was bundle-mediated but whether it was source-clean at the moment of arrangement.

**The continuum is not binary.** Pure self-curation and pure external source-compromise are *analytic limit cases*. The architecture expects many philosophically and clinically relevant cases to be mixed configurations along the continuum, but does not claim a population-level distribution of source-status across actual agents. An adult agent's toolset-input at any moment is shaped by a mixture of pre-agential imprinting, post-agential osmotic exposure (some chosen, some imposed), the agent's own configurational willing-acts (with varying source-status), and present input from the immediate environment. Section 9 develops the responsibility-attribution analysis along this continuum; the structural apparatus is fixed in 5.7.

---


---

# 6. Will, trying, and effort: operator-bundle direction under resistance

Section 6 develops the structural phenomenology of will, willing, trying, and effort. Section 5 supplied the verification-toolkit, the live-option construction lemma, the action-space $\mathcal{O}_{m,t;d}$, toolkit failure modes, toolkit-development mechanics, the output-imprinting cascade, the N-order generalization with foundational orders 1–3 and constructed orders 4 through $N(m,t;d)$, the three willing-strategies, and the manipulation continuum. Section 5 answered: *what can the I construct as live?* Section 6 answers: *what happens when the I directs itself through a live option under resistance?* The section's controlling thesis is structural and load-bearing throughout the rest of the paper:

> *Effort is the phenomenology and structural cost of maintaining operator-bundle direction under resistance.*

Resistance arises from many sources: substrate-pull, salience competition, cognitive load, $\Pi$-conflict, implementation gaps, source-compromise, cross-order misalignment, constructed-order social friction, or cascade-management burdens. Section 6 develops effort as the unifying analytical category that organizes these resistance-sources, classifies them by structural origin, and traces their order- and strategy-specific phenomenology.

Three sections of the paper meet at this junction. Section 6 does not decide responsibility (Section 9 does that), does not decide empirical timing questions (Section 10 does), and does not develop the variation taxonomy in full (Section 8 does). Section 6's contribution is the structural phenomenology of exertion, trying, and resistance — the I directing itself through a live-option space under cost, the cost-profile of that direction, and the order- and strategy-specific shapes that direction takes when resistance must be overcome, held, routed around, timed, or reconfigured.

## 6.1 From live-option construction to willing

Section 5 specified what the I can construct as live; Section 6 specifies what the I does within that constructed space when the going is hard. The transition has three structural commitments worth making explicit.

First, willing operates *over* the action-space $\mathcal{O}_{m,t;d}$. Section 5.2's lemma fixes membership in the action-space; Section 6 takes membership as given and asks what direction *through* the action-space looks like phenomenologically and structurally. An option that is not in $\mathcal{O}_{m,t;d}$ cannot be willed; an option that is in $\mathcal{O}_{m,t;d}$ may still require effort to engage, sustain, complete, or coordinate with other order-tagged options.

Second, the same six conditions of free choice (Section 3.2) apply throughout Section 6's analysis. Effort and trying are not separate from free choice; they are configurations of free choice under specific resistance-conditions. A successful effortful trying that achieves its outcome and a frictionless mastered-domain willing that achieves the same outcome both satisfy the six conditions; what differs is the resistance-profile, not the structural configuration of agency.

Third, the willing-strategies of Section 5.8 (direct, configurational, slingshot) and the mastery dimension of Section 5.7 are *orthogonal* to the order dimension. Section 6 develops effort across all three dimensions simultaneously: order (where the resistance appears), strategy (how the resistance is managed), and mastery (whether the toolkit's construction step is compressed or explicit). Will-acts have values along all three; effort-phenomenology depends on all three; and the analysis of any actual will-act requires reading it across all three. *The three dimensions are analytically orthogonal, not phenomenologically independent.* In actual will-acts, mastery in a domain often makes certain strategies available (mastered configurational and slingshot strategies require toolkit-development that mastery supplies), strategy can shift which order bears the most apparent effort (configurational willing shifts effort into the present arranging-act away from later within-action-space willing), and constructed-order action characteristically depends on lower-order mastery. The architecture's claim is that the three dimensions are independent variables for analysis, not that they vary independently in lived will-acts.

The boundary of Section 6 is fixed by what other sections own. Section 7 develops deliberation and decision, including the structure of selection events and Mode B reflective access; Section 6 may gesture toward decision-points but does not develop the decision-event structure. Section 8 develops variations and pathologies in full; Section 6 may preview effort-pathologies as architectural categories but does not develop the variation taxonomy. Section 9 develops responsibility and accountability; Section 6 may use cascade-management effort and engage source-status, but does not assign attribution. Section 10 develops the empirical interface (Libet/Wegner/Soon); Section 6 may note that effort-phenomenology is testable but does not engage the experimental literature directly. Within those boundaries, Section 6 is the bridge from live-option construction to agency phenomenology.

## 6.2 Will, willing-operation, and will-act

The architecture does not posit "the will" as a separate faculty or substance. Section 3.4's will-as-function discipline is preserved throughout Section 6. To make the analysis tractable while respecting that discipline, three terms are used with distinct technical meanings.

| Term | Technical meaning |
|---|---|
| **Will** | Ordinary-language umbrella term; used in this section only when the ordinary-language register is appropriate. Avoided as a technical noun-substance. |
| **Willing-operation** | Operator-bundle-mediated direction in a live-option space at a particular order in a particular domain. The function the I performs when willing. |
| **Will-act** | A bounded episode of willing-operation directed toward some option, configuration, or set of cross-order coordinated options. The unit of agency-event analysis. |

The architecture's claim is structural: willing is a function, not a substance. *Willing-operation* is what the I does; *will-act* is the bounded episode of doing it; "the will" is at most a convenience-noun for the capacity for willing-operation, not a faculty the agent possesses as an entity.

A will-act can occur at any developed order. At foundational orders 1–3, the I directs focus, thought, or substrate-mediated action. At constructed orders 4 through $N(m,t;d)$, the I directs not-I coordination structures — asking, teaching, organizing, negotiating, institutional engagement — through lower-order implementation. Per Section 5.7, constructed orders do not add new substrate pathways; they are application-level target-domain orders implemented through lower-order willing, made possible by mastery and toolkit-development. A fourth-order asking-act is a will-act whose target is a not-I coordination structure (the asking-protocol with the addressed agent), implemented through third-order vocal action; it satisfies the constructed-order membership test of 5.7 only when the target is the coordination structure as such, not when the act is mechanical vocalization with social side-effects.

The three willing-strategies of Section 5.8 (direct, configurational, slingshot) are *strategic profiles* of willing-operation, not separate willing-mechanisms. A will-act at any order can deploy any of the three strategies, with mastery (Section 5.7) as a third orthogonal dimension. The grandmaster's mastered-domain direct will-act, the experienced negotiator's mastered-domain configurational will-act, and the contemplative practitioner's mastered-domain slingshot will-act are all coherent configurations the architecture recognizes; their effort-profiles differ accordingly (Section 6.7).

## 6.3 Trying as willing under incomplete guarantee

Trying is not failed action and not effort itself. Trying is a structural configuration of willing:

> *Trying is operator-bundle-mediated direction toward an outcome whose completion is not guaranteed from inside the current action-space.*

Four conditions specify the structure:

1. The option is live (per the live-option construction lemma, 5.2).
2. The I directs toward it (operator-bundle-mediation per 3.4).
3. The implementation path is uncertain, resistant, incomplete, or dependent on not-I conditions (Section 6.4 develops resistance taxonomically).
4. Success is not identical with the willing-act itself; the agent can be willing toward the outcome without yet having achieved it.

Trying can occur at any order. The following examples illustrate the structural pattern across orders:

| Trying-case | Structural reading |
|---|---|
| Trying to focus | First-order willing under salience resistance |
| Trying to understand | Second-order willing under cognitive complexity, $\phi$-pathway uncertainty, or projection-toolset limits |
| Trying to lift something heavy | Third-order willing under substrate fatigue and environmental resistance |
| Trying to persuade | Fourth-order willing under not-I response uncertainty |
| Trying to direct a team toward consensus | Fifth-order willing under group-coordination friction |
| Trying to recover from a habit | Configurational willing plus output-cascade management plus first-and-second-order willing under substrate-capture resistance |
| Trying to recall a name | Second-order willing under $\phi$-pathway-access uncertainty |

Trying must be distinguished from several adjacent phenomena:

| Phenomenon | Difference from trying |
|---|---|
| **Intending** | Projected commitment or plan; may not yet exert direction. The agent who intends to exercise tomorrow has not yet engaged operator-bundle direction. |
| **Deciding** | A selection event among live options; Section 7 develops this. Deciding can occur without subsequent trying (the agent decides and the action runs through mastered-domain compiled willing). |
| **Acting** | Implementation event; may or may not involve ongoing operator-bundle direction. Reflexive action is acting without willing; mastered-domain action is acting with compressed willing; trying is acting with active operator-bundle direction under incomplete-guarantee. |
| **Struggling** | Trying under high or repeated resistance — a high-resistance variant of trying, not a structurally separate category. |
| **Effort** | The cost-profile of trying. Section 6.4 develops effort as the structural cost; trying is the configuration that incurs the cost. |

The distinction between trying and effort is load-bearing for the rest of Section 6. Trying is the directed structure (the I orienting toward an outcome under incomplete guarantee); effort is the resistance-cost profile of maintaining that structure across time. A first-order trying may have low effort-cost (briefly trying to recall a familiar name) or high effort-cost (sustained trying to focus through severe distraction). The trying-structure can be present even when effort is low; effort can be high even when trying briefly fails to engage. Section 6.4 develops the effort side of this pair.

*Trying and dynamic refinement.* The "incomplete guarantee" condition of trying is structurally connected to the fuzzy-construction discipline of Section 3.2's Condition 1 and the dynamic-refinement note of 5.3. A trying-structured will-act proceeds on a course-skeleton with execution details elaborating during the willing-period; the trying carries the I forward as the toolkit constructs subsequent details under the trained expectation that refinement will succeed. When the trained expectation holds and the substrate supports the refinement, trying transitions smoothly toward outcome; when refinement fails (the toolkit cannot construct the next step, the substrate cannot sustain the operator-bundle direction through the refinement process, the not-I conditions deviate from projection), trying becomes effortful — and the resistance encountered is precisely the resistance to dynamic refinement, not (only) to executing a pre-constructed plan. This connects trying to mastery (5.7): mastered-domain trying has high dynamic-refinement capacity; novice trying has lower fuzzy-construction tolerance and characteristically encounters more refinement-resistance.

*Fuzzy construction is common in trying but not necessary for trying.* Trying can occur with a fully pre-constructed course when success remains uncertain because of substrate resistance, environmental resistance, not-I response, or execution-risk independent of construction-status. Trying to lift a heavy weight may proceed through a fully memorized lifting-sequence; trying to recite a known passage may engage no fuzzy construction at all; trying to execute a memorized scale on a difficult instrument may have its uncertainty entirely in motor-substrate execution. In these cases the trying-structure is intact (operator-bundle direction toward an outcome whose completion is not guaranteed) but the source of incomplete guarantee is implementation-uncertainty rather than fuzzy-construction. Fuzzy construction explains many trying-structures and is the most common source of incomplete guarantee in unfamiliar domains; incomplete guarantee is the broader condition that subsumes fuzzy-construction-related and implementation-related uncertainty alike.

*Mastered-domain willing can still be trying.* Mastery compresses construction and improves dynamic refinement *within the mastered domain and within the variance-envelope the toolkit has learned to handle* (per 5.7); it does not guarantee success and does not remove resistance from all cases. The grandmaster trying against a hard opponent, the experienced negotiator trying against an evasive counterparty, the master craftsman trying with unfamiliar materials, the seasoned leader trying through institutional headwind: each is a mastered-domain will-act with the trying-structure intact because success remains uncertain at the moment of engagement. Mastery and trying are not opposites; mastery shapes the effort-economy and dynamic-refinement profile of trying within mastered domains while leaving the trying-structure available wherever incomplete guarantee remains.

## 6.4 Effort as operator-bundle direction under resistance

This is the load-bearing subsection of Section 6.

> *Effort is the structural and phenomenological cost of sustaining operator-bundle direction when resistance must be overcome, held, routed around, timed, or reconfigured.*

Effort is not defined by intensity alone; effort is defined by *resistance encountered while willing*. An action that proceeds without resistance generates little or no effort (the mastered-domain expert's fluent execution); an action that encounters resistance generates effort proportional to the resistance and the degree of bundle-engagement required to overcome, hold, route around, time, or reconfigure it.

*Resistance is the condition for effort, not for willing.* A will-act can occur with negligible effort when the live option is well-constructed, substrate coupling is smooth, and no salient cross-order conflict appears. In such cases willing remains present (the operator-bundle is mediating direction toward the option), but effort approaches zero. The architecture does not commit to "all willing is effortful" — it commits to "effort tracks resistance encountered during willing." Effortless willing is structurally possible and in fact common in mastered domains.

The architecture commits to a *taxonomy of resistance* as the primary analytic decomposition. Eight structurally distinguishable resistance-types appear across the order × strategy × mastery space:

| Resistance type | Structural source | Representative case |
|---|---|---|
| **Salience resistance** | Competing first-order capture; substrate-mediated salience-gating pulls attention away from the target | Trying not to check the phone during deep work |
| **Cognitive resistance** | Second-order complexity, uncertainty, rumination, weak $\phi$-pathway, projection-toolset limits | Trying to reason through a hard problem; trying to construct a long inferential chain |
| **Substrate resistance** | Fatigue, pain, ADHD-like implementation gap, arousal mismatch, motor difficulty | Trying to start a task when substrate cannot sustain initiation; sustained physical exertion against fatigue |
| **$\Pi$-conflict resistance** | Action-priority split: multiple preservation-priorities pull in different directions ("what-the-I-most-needs-to-continue") | Wanting health but prioritizing immediate reward; long-term goal in tension with short-term comfort |
| **PtCns resistance** | Frame-coherence conflict: pursuing the option threatens self-betrayal or identity-inconsistency ("who-the-I-is") | Trying to do what feels self-betraying; acting against deeply-held framing or identity-commitment |
| **Cross-order misalignment** | Focus, thought, and body do not converge; will-acts at different orders fail to coordinate | Mind endorses the action; body stalls; attention wanders away from the deliberation |
| **Constructed-order resistance** | Not-I structures resist direction; the addressed agents, institutional protocols, or coordination structures push back | Trying to persuade a skeptical audience; trying to lead a divided team; trying to navigate an unresponsive bureaucracy |
| **Cascade-management resistance** | Downstream effects of one's own activity must be anticipated, mitigated, arranged-around, or repaired | Arranging environment to reduce known distraction cascades; managing tone because of known imprinting effects on others |

*The eight categories are primary analytic resistance sources, not an exhaustive inventory.* Actual will-acts often involve compound resistance, and later sections may subdivide these categories where responsibility (Section 9), pathology (Section 8), or empirical operationalization (Section 10) requires it. Possible additional or sub-categorical resistance-types — social-norm resistance, time-pressure resistance, ambiguity / framing-resolution resistance, emotional-affective resistance amplifiers, memory / retrieval resistance — can be folded into the eight or treated as compound forms; the taxonomy organizes the architecturally distinguishable structural sources, not the full empirical phenomenology.

*$\Pi$-conflict and PtCns resistance are distinct.* They may co-occur but track different structural conflicts. $\Pi$-conflict concerns *priority* among live options ("what-the-I-most-needs-to-continue" — preservation-priority weighting in tension); PtCns resistance concerns *frame-coherence* under the option ("who-the-I-is" — pursuing the option threatens self-consistency or identity-stability). The architecture's prior separation of $\Pi$ (preservation-priority) from PtCns (frame-coherence operations) at File 3's coordinate-decomposition propagates here: $\Pi$-conflict is what-to-do conflict; PtCns resistance is how-this-coheres-with-self conflict.

*Resistance to dynamic refinement is a compound form.* The fuzzy-construction discipline (3.2's Condition 1, 5.3's dynamic-refinement note) implies that many real will-acts proceed on course-skeletons with execution-level details elaborating during the willing-period. Resistance can occur at the dynamic-refinement step itself — the toolkit cannot construct the next executable detail under current conditions, the substrate cannot sustain operator-bundle direction through the refinement process, or not-I conditions deviate from projection. Resistance to dynamic refinement is not a ninth taxonomy entry; it is a compound form that can manifest across cognitive resistance (the toolkit's construction step fails), substrate resistance (substrate cannot sustain through refinement), and cross-order misalignment (refinement at one order outpaces another order's capacity to keep up). The fuzzy-construction discipline thus enriches the resistance taxonomy rather than expanding it.

*Effort phenomenology has joint $A_{m,t}(x)$ / $\phi$ structure.* Effort can be phenomenally available with or without source-pathway access (the foundation's joint $A_{m,t}(x)$ / $\phi$ taxonomy, File 3 §6.1). Salience resistance is typically conscious-clear: one feels the pull of the distraction and can identify what is pulling. Some $\Pi$-conflict, PtCns resistance, or substrate resistance may be conscious-fuzzy: the I experiences effort without being able to articulate the precise source — substrate-developmental constraint, residual trauma activation, or unresolved frame-conflict can present as a "wall" without articulated origin. Source-opacity in effort is a structural feature, not a deficit; the architecture's joint $A_{m,t}(x)$ / $\phi$ apparatus is what allows effort-phenomenology to be analyzed beyond the cases where the I can name the resistance-source.

Two architectural commitments follow.

*Effort is not freedom.* High effort is not the mark of good agency. High effort can indicate poorly developed toolkit (the novice constructs each option from scratch), cross-order conflict (orders pull against each other), substrate resistance (fatigue, pain, ADHD-like substrate constraint), source-compromise (the option is poorly aligned with $\Pi$ or PtCns), or environmental difficulty. Mature agency often *reduces* direct effort by deploying configurational, slingshot, or mastered-domain willing strategies. The architecture rejects the conflation of effort with agency-quality.

*Effort is not always maximized by good agency.* The agent who sustains a difficult task through repeated direct effort may be exercising agency well; or may be locked in cross-order conflict, source-compromised mastery, or counterproductive direct willing where configurational or slingshot strategies would be more effective. The architecture's discipline: effort-economy (Section 6.7) is a developmentally sensitive marker of toolkit-richness and strategy-deployment, not a unidirectional indicator of agency-quality.

## 6.5 Effort across foundational orders

Foundational-order effort takes order-specific phenomenological forms because the substrate the bundle operates over differs at each order. Section 6.5 develops first-, second-, and third-order effort in turn.

### 6.5.1 First-order attentional effort

First-order effort is the cost of *maintaining or shifting focus against salience competition*. The I directs attention toward a target; substrate-mediated salience-gating may direct attention elsewhere; sustaining the directed focus requires operator-bundle engagement against the substrate's salience-pull.

Phenomenology: the strain of holding attention; repeated re-orienting to the target after distraction-pull; awareness of competing salience-targets; focus-fatigue accumulating with sustained engagement; the relief of cessation when the focus-demand ends or the focus-target itself becomes salience-dominant.

Failure modes: salience capture (substrate dominates, focus is pulled away involuntarily); attention-shifting failure (the agent cannot redirect focus to the target); unstable focus (focus engages briefly, releases, re-engages, releases); source-opaque attentional drift (focus moves away without the agent registering the drift, often noted only retrospectively).

First-order effort-economy depends heavily on substrate state and toolkit-development. The contemplative practitioner with a developed first-order toolkit constructs as live a stable focus-target the untrained practitioner cannot construct; mastery here means low-effort sustained focus on the same target the novice can only briefly hold. Substrate-developmental constraints (Section 5.4) on first-order operator-bundle-mediation (ADHD-like configurations) produce characteristically high first-order effort relative to outcome — the toolkit may construct the focus-target, the I may inhabit it, but sustained substrate support for the operator-bundle direction is constrained.

### 6.5.2 Second-order cognitive / deliberative effort

Second-order effort is the cost of *maintaining thought-paths, comparison operations, projection, reasoning, inhibition, or reframing against cognitive resistance*. The I directs thought along a deliberation-path; cognitive substrate must supply the representational content; the projection-toolset (developed application-level in the affect paper's threat-cluster, Section 7) must construct future-state representations; working-memory must hold the path's intermediate states.

Phenomenology: mental strain; difficulty holding the problem; working-memory pressure; rumination loops returning to the same content without progress; uncertainty loops where evaluation does not converge; the experience of "I know what I mean but cannot construct the path"; the feeling of stretching or reaching for a representation just out of reach.

Failure modes: thought-path collapse (the path begins but cannot be sustained to completion); evaluation loops (PtCns, PCE-over-projection, or $\Pi$-weighting cannot resolve and the deliberation cycles); planning failure (configurational thought-paths cannot be constructed at sufficient resolution to be evaluable); projection-toolset failure (future-states cannot be constructed with sufficient resolution for evaluative engagement); $\phi$-failure around reasons (the reasons-pathway is unavailable or compromised; the agent cannot articulate or verify why a particular thought-path is being pursued).

Second-order effort-economy depends on toolkit-development of the relevant thought-domain. Philosophical training, structured deliberation training, and therapy each expand the second-order toolkit; mastery in a thought-domain compresses construction (the philosopher's argument flows where the novice's stalls). Substrate-developmental constraints on second-order operator-bundle-mediation (executive function constraints per 5.4) produce characteristically high second-order effort relative to outcome, particularly on working-memory-mediated thought-path traversal.

### 6.5.3 Third-order embodied / substrate effort

Third-order effort is the cost of *directing substrate action or embodied regulation against fatigue, pain, arousal mismatch, motor resistance, or implementation gap*. The I directs the body or the toolkit-mediated autonomic capacities; substrate must execute or scaffold the action-pattern; the operator-bundle must sustain direction through substrate-resistance.

Phenomenology: bodily strain; initiation difficulty; motor fatigue accumulating across sustained action; breath and posture regulation under arousal; arousal modulation (calming, energizing, sustaining); the felt-sense of "pushing the body" when substrate does not readily comply; the relief of substrate-cooperation when the body finally moves.

Failure modes: motor fatigue (substrate cannot sustain the action-pattern); initiation failure (substrate cannot bridge from intent to action); arousal mismatch (substrate is over- or under-aroused for the action-pattern); pain-driven withdrawal (substrate-mediated pain pulls willing away from the target); implementation gap (the toolkit represents and evaluates the action-pattern but substrate cannot execute it currently).

A guardrail from Section 4.4 applies throughout: autonomic states are third-order live options *only where toolset-mediation makes them scaffoldable* — breath, posture, training, biofeedback, somatic practice, structured exposure — not because the I can directly will any autonomic state. Third-order effort over scaffolded autonomic capacities (the meditator's breath-pacing, the athlete's heart-rate modulation through trained somatic practice) is a distinctive phenomenology that should not be confused with direct will over autonomic substrate.

*Third-order substrate resistance natively couples with affective states.* The companion application paper on differentiated affect develops the threat-cluster, embodied substrate states, arousal mismatches, anhedonia, and pain phenomenology in detail. Third-order effort cannot be cleanly separated from these affect-states: pain amplifies substrate resistance directly; fatigue increases initiation difficulty; anxiety adds salience competition through threat-projection; anhedonia reduces engagement-readiness; somatic states from prior trauma activation can produce substrate resistance whose source-pathway is unavailable to the I. Section 6 treats these as *resistance-modulators* for third-order effort; the affect paper supplies the structural taxonomy. Section 8's variations and Section 10's empirical-interface analysis develop the joint effort-affect dynamics in detail.

## 6.6 Effort across constructed orders

Section 5.7's N-order generalization extends effort analysis to constructed orders 4 through $N(m,t;d)$. Constructed-order effort is *not a new substrate effort*: the substrate is still the foundational-order substrate (third-order action remains the medium that ultimately reaches not-I), and lower constructed orders or foundational orders supply the implementation chain. What is distinctive about constructed-order effort is that the *target* of the willing is a not-I coordination structure, and the success conditions for the will-act partly lie outside the agent's own substrate.

| Constructed order | Effort form |
|---|---|
| Fourth-order asking / persuading / directing | Sustaining social-protocol direction under not-I response uncertainty; reading the addressed agent's apparent-I response; adjusting framing or approach in real time |
| Fourth-order manipulation / deception | Sustaining social-protocol direction with source-compromised aim; the resistance-profile is similar to skilled asking (not-I response uncertainty, dynamic refinement of framing), but the aim is source-compromised per 5.9; effort-structure is order-equivalent to autonomy-supporting fourth-order will-acts, with the moral distinction at source-status not at order |
| Fifth-order team coordination | Keeping multiple agents' roles, timing, communications, and responses in play simultaneously; cross-agent cross-order coordination; maintaining coherence under partial information |
| Institutional / sixth-order action | Maintaining direction through rules, roles, forms, bureaucratic structures, and explicit institutional protocols; navigating institutional friction; sustaining cross-temporal continuity through institutional memory |
| Teaching | Shaping another agent's toolkit-development without controlling their I; calibrating the input to the learner's current toolkit state; sustaining the relationship across long timescales |
| Leadership | Directing group-level option-space while managing feedback loops; sustaining coherent direction across conflicting pressures from group members and external conditions |

The architectural claim is sharp:

> *Constructed-order effort is not a new substrate effort. It is effort in maintaining live direction over target-domains whose success conditions partly lie outside the agent's own substrate.*

Two implications follow. First, constructed-order effort can be quite high even when foundational-order effort is moderate, because the resistance is in the not-I structure (the audience's skepticism, the institution's friction, the team's coordination drag) rather than in the agent's own substrate. The effort is real and architecturally specifiable; it is not "effort to use the body" but "effort to sustain bundle-direction over a target that responds independently."

Second, mastery at constructed orders is a major effort-economy advantage. The experienced negotiator's mastered-domain fourth-order willing flows where the novice's stalls; the experienced manager's mastered-domain fifth-order team-coordination runs with low explicit effort where the novice's would consume substantial direct willing. The constructed-order mastery's effort-compression operates on the same architectural mechanism as foundational-order mastery (Section 5.7's six-condition mastery table applies); the substrate-medium is still foundational-order substrate, but the construction step over the target-structure is compressed.

A moral-neutrality note repeats here from 5.7: a fourth-order manipulation and a fourth-order request can both be skilled constructed-order will-acts. Their effort-profiles may be similar, their order-rank is the same; they differ at the source-status / $\Pi$-alignment / autonomy-effects level developed in 5.9 and Section 9. Section 6 does not assign moral status; it analyzes the effort-structure of constructed-order willing as such.

## 6.7 Effort-economy across direct, configurational, and slingshot willing

The willing-strategies of Section 5.8 differ in their effort-economy profiles. Section 6.7 develops the comparison.

| Strategy | Effort profile | Typical phenomenology | Failure risk |
|---|---|---|---|
| **Direct willing** | High sustained operator-substrate tension across the willing-period | Pressing, forcing, holding direction against resistance; strain that scales with willing-duration | Depletion; repeated re-engagement failure; effort exhaustion before outcome |
| **Configurational willing** | Present effort to arrange future conditions; effort distributed temporally | Planning, setting up, designing; satisfaction of arrangement; later observation of arranged effects without ongoing willing | Source-compromised self-curation (5.9); over-scaffolding that reduces agency-development; brittle arrangements that fail under perturbation |
| **Slingshot willing** | Effort concentrated in timing and gradient-reading; small, precise willing-acts at opportune moments | Waiting, sensing the moment, releasing; the felt-sense of "catching the wave" | Passivity rationalized as timing; missed windows; mistaking gradient-misreading for opportune-timing |
| **Mastered-domain willing** | Compressed construction; low-friction execution within the mastered sub-domain | Fluency, flow, immediacy; the skilled action that "happens" | Automaticity drift (5.7's six-condition table); source-compromised mastery (5.7); brittle expertise outside the mastered sub-domain |

The strategies' effort-economies differ primarily in *where* the effort is concentrated. Direct willing concentrates effort in sustained engagement during execution; configurational willing concentrates effort in the present arranging-act with subsequent low-effort downstream operation; slingshot willing concentrates effort in gradient-reading and precise timing with low effort during execution; mastered-domain willing distributes the up-front effort cost into the toolkit-development phase, leaving low-effort execution within mastered sub-domains.

The developmental trajectory of Section 5.8 applies: novice agents operate primarily through direct willing because configurational and slingshot strategies require additional toolkit-resources their toolkits have not yet developed. Mature agents mix all three strategies according to context; expert agents in a domain often deploy configurational and slingshot strategies preferentially because their toolkits have made those strategies available as live, and their effort-economies are favorable. Pred 22 of the planning document is supported by this analysis: the configurational/slingshot to direct-willing ratio, weighted by effort-economy per unit goal-progress, is a candidate developmental marker. Section 5.8's operational markers (direct-willing load, configurational strategy use, slingshot strategy use, effort-economy, developmental ratio) are *candidate operationalizations* the empirical literature can investigate; *Section 11 will decide whether they are promoted to formal prediction status*. Section 6's contribution to Pred 22 is the structural account that makes these markers architecturally specifiable; Section 11 owns the prediction-promotion decision.

A discipline from Section 5.8 propagates here: substrate-developmental constraints reshape the trajectory non-trivially. ADHD-like configurations affect direct willing's effort-economy at orders 1 and 2 specifically (substrate cannot sustain the operator-substrate tension that direct willing requires at those orders). Configurational and slingshot strategies, when the toolkit has developed them as live, may have proportionally favorable effort-economy in such cases — leveraging the osmotic-imprinting mechanism that the substrate is sensitized to and the gradient-sensitivity the substrate retains. This is a tendency-prediction conditional on toolkit-development, not a universal trajectory; agents with substrate-developmental constraint and undeveloped toolkits for configurational and slingshot strategies face constrained direct willing without compensating strategies, a structurally specifiable agency-configuration Section 8 develops.

## 6.8 Mastery, flow, and low-effort agency

Mastery reduces explicit effort by compressing toolkit construction. It does not eliminate willing. Section 5.7's six-condition mastery table holds throughout: contrastive option-space remains (compressed but present); evaluative engagement remains (often implicit, but engaged for free choice proper); operator-bundle selection remains (direct and low-friction, not absent); substrate coupling is highly trained implementation (not bypass); Mode B remains available even if not exercised during flow; ownership-integration remains required.

Section 6.8 distinguishes several low-effort configurations that are sometimes confused with each other. The architecture's discipline is that low effort can mean several different structural things, not all of which are mature agency.

| Configuration | Structural status |
|---|---|
| **Skilled free action** | Low explicit effort; high operator-bundle integration; six conditions satisfied with construction compressed by mastery |
| **Flow** | Mode B not exercised during action, but reflectively available under intact conditions; ownership-integration intact; six conditions satisfied with Mode B-engagement deferred until reflection |
| **Automaticity** | Low effort because operator-bundle engagement is thin or absent; may not satisfy the six conditions; agency status varies with how thin the bundle-engagement is |
| **Compulsion** | Low or high effort depending on resistance, but substrate capture dominates; six conditions typically violated (Condition 4 — non-preemptive substrate coupling — fails) |
| **Source-compromised mastery** | Efficient action with the same effort-compression as autonomy-supporting mastery, but source-status compromised; aims, evaluative apparatus, or toolkit-development itself is source-compromised (5.7, 5.9) |
| **Habitual-chosen action** | Reduced first-order direction; second-order chosen pattern executing through third-order substrate; agency-thin but intact |
| **Habitual-compulsive action** | Third-order substrate-pattern capture; first-order attentional capture; minimized second-order; six conditions often violated |

*Effort is diagnostically relevant when read structurally.* Effort-level alone cannot classify agency-quality, but effort *in combination with* source-status (5.9), $\Pi$-relation, ownership-integration (3.2 Condition 6), substrate-coupling/preemption status (3.2 Condition 4), and Mode B availability (3.2 Condition 5) is diagnostically meaningful. High effort may indicate admirable resistance against substrate pull (the recovering agent maintaining direction against compulsion) or poor toolkit-development (the novice constructing each option from scratch); the difference is read in the architectural configuration, not in the effort-level itself. Low effort may indicate mastery, automaticity, capture, or compulsion; the difference is read in the same architectural configuration. Effort is one variable in a multi-variable architectural reading, not a standalone marker.

*Habitual-chosen vs habitual-compulsive — structural markers.* The seven-row distinction above identifies the configurations; the architecture supplies five structural markers that empirically distinguish habitual-chosen from habitual-compulsive in actual cases:

| Marker | Habitual-chosen | Habitual-compulsive |
|---|---|---|
| **Interruptibility** | Generally interruptible under Mode B access; the I can stop or alter the pattern when reflecting on it | Resistant to interruption even under explicit reflective opposition; the pattern continues through opposed Mode B engagement |
| **$\Pi$-alignment** | Broadly aligned with the agent's endorsed preservation-priorities | Captures action-priority against the agent's endorsement; the pattern continues despite $\Pi$-misalignment |
| **Source-status** | Self-curated through prior configurational willing or accepted through sufficiently source-clean processes | Substrate-driven, source-compromised, or rooted in pre-agential imprinting the agent has not been able to take up |
| **Ownership-integration** | Integrated as a chosen pattern; the I recognizes the action as its own | Felt as alien, pressured, or regretted; the I experiences the action as something happening rather than as its own willing |
| **Substrate-coupling / preemption** | Trained implementation; substrate supports the chosen pattern without preempting Mode B engagement | Capture / bypass / preemption: substrate-coupling preempts the operator-bundle's engagement, satisfying Condition 4 violation |

The fifth marker — *substrate-coupling and preemption status* — is the load-bearing empirical discriminator. Habitual-chosen action is trained substrate-coupling that supports the operator-bundle's chosen pattern; habitual-compulsive action is substrate-coupling that *preempts* operator-bundle engagement, structurally violating Condition 4 of free choice. The other four markers are corroborating evidence; the substrate-coupling/preemption status is the architectural commitment that determines whether the configuration is agency-thin-but-intact or agency-violated.

The architectural discipline that follows from this differentiation:

> *High effort is not the mark of freedom. Low effort is not the mark of mature agency. Effort and agency-quality are structurally separate: effort is a resistance-cost profile; agency-quality is a configuration of the six conditions, the ρ/Π separation, source-status, and ownership-integration.*

A bad inference Section 6 explicitly forecloses: that effortlessness indicates absence of agency. Skilled free action and flow are *high-agency* configurations with low effort; they should not be confused with automaticity, capture, or compulsion. Conversely, high-effort configurations may be poorly developed agency (the novice's struggling), source-compromised mastery's effortful exercise of distorted aims, or cross-order conflict — the high effort is real but does not by itself indicate mature or autonomous agency.

The empirical implication: distinguishing skilled flow from automaticity, source-clean mastery from source-compromised mastery, or chosen habit from compulsive habit requires examining the architectural configuration, not the effort-level alone. Section 8's variation taxonomy and Section 10's empirical interface develop the specific markers; Section 6 establishes the structural distinction.

## 6.9 Effort without success, success without effort

Effort and outcome are structurally separate. Section 6.9 develops both directions of this separation.

**Effort without success.** Effort is fully real even when the outcome fails, because effort is defined by *sustained operator-bundle direction under resistance*, not by successful completion. Examples:

- Trying to focus, but salience capture wins;
- Trying to lift a weight beyond substrate capacity;
- Trying to persuade an audience that rejects the framing;
- Trying to recall a name where the $\phi$-pathway does not yield;
- Trying to resist a compulsion where substrate capture overrides operator-bundle direction.

In each case, the effort-structure is present (operator-bundle direction is engaged, resistance is present, the I sustains direction across the willing-period), and the outcome fails. The architecture's claim:

> *Effort can be fully real even when outcome fails, because effort is defined by sustained operator-bundle direction under resistance, not by successful completion.*

This separation is important for several downstream analyses. Section 8's variation taxonomy must distinguish effort-with-failed-outcome (akrasia, trying-but-failing, trying-against-compulsion) from absence-of-effort (apathy, anhedonia-driven engagement-collapse, learned helplessness). Section 9's responsibility analysis must distinguish effortful trying that failed from absent willing that produced no attempt. Section 10's empirical analysis must avoid inferring agency from outcome alone.

**Success without effort.** Outcome success does not by itself prove willing, trying, or free choice. Examples:

- Skilled automatic action where mastered-domain compiled willing produces the outcome with low explicit effort;
- Environmental arrangement makes the action easy, so only minimal willing is needed (the agent who has configurationally arranged their environment to make exercise the path of least resistance);
- A favorable cascade produces the outcome (Section 5.6's Stage 3 closure operating in the agent's favor without further willing);
- Another agent completes the requested act (the manager's fourth-order asking-act produces the team member's action; the team member's action is not the manager's willing);
- Substrate produces movement or speech without operator-bundle mediation (reflexive action, automatism, dissociative action).

The architecture's claim:

> *Outcome success does not by itself prove willing, trying, or free choice. The architecture classifies outcome-producing events by whether operator-bundle mediation, live-option selection, and ownership-integration were present.*

This second separation is equally important. Section 10's empirical interface (Libet/Wegner/Soon) turns critically on this: the appearance of having chosen an outcome the agent did not actually will (Wegner-paradigm cases) is structurally distinct from genuine free choice that produced the same outcome. Section 9's responsibility analysis must distinguish outcome-attribution from agency-attribution. Section 7's decision analysis must distinguish decision-events from outcome-events. The effort-outcome separation is the structural basis for these downstream distinctions.

## 6.10 Cross-order conflict and effort-pathology preview

Section 8 develops the variation taxonomy in full; Section 6.10 previews the effort-pathology category as an architectural class without doing Section 8's work. The category is structurally specifiable: configurations where effort, trying, or willing fails, captures, collapses, or misaligns across orders.

| Configuration | Effort-structure |
|---|---|
| **Akrasia** | Second-order evaluation endorses one option; $\Pi$ or substrate pulls toward another; effort either fails to sustain the endorsed option or produces compromise behavior |
| **Compulsion** | Third-order substrate capture overwhelms live alternatives; effort to resist may be high but substrate-coupling preempts operator-bundle direction (Condition 4 violation) |
| **ADHD-like implementation gap** | Representation, evaluation, and inhabitation may be intact; sustained implementation of operator-bundle direction at orders 1 and 2 fails over duration; substrate-developmental constraint per 5.4 |
| **Learned helplessness** | Projection-toolset returns no viable pathway; effort collapses before trying-structure can form; option-space contracts at the projection step |
| **Severe depression** | Multi-order effort collapse: third-order somatic flattening, second-order projection collapse, first-order narrowing; effort-economy degraded across orders |
| **Anxiety-driven effort consumption** | Effort consumed by threat-projection and salience-loops; minimal effort remains for goal-directed willing |
| **Dissociation** | Ownership-integration / inhabitability disrupted; effort may occur but the willing-act is not integrated as the I's willing |
| **Source-compromised mastery** | Efficient willing under compromised aims; effort-economy is favorable but the agent's exercises serve source-compromised $\Pi$, framing, or coercive scaffolding |

For ADHD specifically, the architecture's recent commitment (5.4, 5.6, 5.8) is preserved: ADHD-like agency impairment is a substrate-developmental constraint on operator-bundle-mediation at orders 1 and 2, often with third-order arousal/reward-substrate compounds. The toolkit may represent, evaluate, and inhabit the option (the agent knows what to do, endorses doing it, can imagine doing it); what fails is sustained implementation of operator-bundle direction over time. Effort-phenomenology in ADHD configurations characteristically involves repeated re-engagement without sustained direct-willing capacity, with proportionally favorable effort-economy in configurational and slingshot strategies when toolkits develop those options as live. The architecture treats this as *one structural profile* of executive-function constraint that maps onto ADHD-like configurations, not as a complete clinical theory of ADHD; the architectural mapping is to the substrate-developmental implementation-gap pattern at orders 1 and 2, with the dynamic-refinement-during-execution sharpening from v0.1.5.1 specifying which substrate-mediated capacity is most affected. Section 6 preserves this as architectural pattern; clinical specifics belong elsewhere.

*Effort and affect.* The companion application paper on differentiated affect develops the affective taxonomy that interacts with effort across the configurations above. Affects function as resistance-amplifiers, resistance-reducers, or resistance-reframers in effort-phenomenology: anxiety consumes first- and second-order effort through threat-projection and salience-loops, leaving less effort available for goal-directed willing; shame raises PtCns resistance by activating frame-coherence conflict around the action; pain and fatigue raise third-order substrate resistance directly; anhedonia reduces engagement-readiness, lowering the effort-availability for any directed action; depression's multi-order effort collapse interacts with affect's threat-cluster activation and somatic-state flattening; devotion or hope can stabilize $\Pi$-priority and reduce experienced effort by aligning operator-bundle direction with frame-supported aims; trauma activation can produce substrate-resistance whose source-pathway is unavailable to the I (conscious-fuzzy resistance per the joint $A_{m,t}(x)$ / $\phi$ note in 6.4). The affect paper supplies the affect-side taxonomy in detail; Section 6 establishes that the affect/effort interaction is structurally specifiable through the resistance-modulation framing and that Section 8's variations and Section 10's empirical interface develop the joint dynamics.

The architecture's discipline forecloses overclinicalization. Section 6.10's effort-pathology preview is a category — specific cases require Section 8's full variation taxonomy and, where appropriate, Section 10's empirical interface. Section 6.10 establishes that the effort-structure has identifiable failure modes and that the architecture is positioned to characterize them; it does not do the characterization in detail.

## 6.11 Output-cascade effort: arranging around one's own downstream effects

Section 5.6's output-imprinting cascade introduces a category of effort that does not fit the within-action-space framing of 6.4–6.10. Some effort is not effort to perform an act directly, but effort to *manage the downstream cascade* of one's own activity — to anticipate, mitigate, arrange around, or repair the effects one's substrate produces regardless of bundle-mediation.

Examples:

- Speaking more quietly because one knows one's voice imprints stress on others (Stage 2 cascade-management);
- Arranging reminders because one knows direct initiation fails (configurational management of substrate-developmental constraint);
- Designing environment to reduce known distraction cascades (configurational anticipation of input-pathway dynamics);
- Repairing social effects of an unregulated outburst (post-hoc cascade-repair through fourth-order will-acts: apology, explanation, restitution);
- Choosing timing because certain substrate states alter later action-space (slingshot management of one's own substrate dynamics);
- Avoiding contexts that one knows will trigger source-compromised configurational willing (anticipatory management of one's own self-curation process per 5.9).

Cascade-management effort is structurally real and architecturally distinct from within-action-space effort. The agent who arranges environment to reduce distraction is not performing effortful focus-direction in the moment of arranging; they are performing configurational willing with present effort-cost aimed at reducing future first-order effort-cost. The agent who speaks quietly because of known imprinting effects is performing third-order action with low substrate-effort but with cascade-management overhead — the cognitive and constructed-order awareness required to anticipate the cascade and adjust accordingly.

*Cascade-management is not a separate willing-strategy.* The willing-strategies of Section 5.8 are direct, configurational, and slingshot. Cascade-management is not a fourth strategy. It is the *application* of one or more of the existing strategies *targeted at the agent's own downstream cascade-effects* rather than at within-action-space outcomes. Speaking more quietly because of known imprinting effects is direct willing applied to cascade-management; arranging reminders is configurational willing applied to cascade-management; choosing the timing of a difficult conversation because one knows certain substrate states alter later action-space is slingshot willing applied to cascade-management. The architectural distinctness of cascade-management lies in the *target* (one's own downstream effects rather than within-action-space outcomes), not in a new mechanism of willing. In actual cases, cascade-management often combines with configurational, constructed-order, or direct effort targeted at the within-action-space outcome — a single will-act may simultaneously direct toward a within-action-space goal and manage cascade-effects of the same activity. The category is analytically distinct as a target-domain for willing-strategies; the strategies themselves remain the three established in 5.8.

A guardrail repeated from 5.6 applies here:

> *Cascade effects within the agent's structural domain do not automatically settle accountability. They become responsibility-relevant when the agent had live options for anticipating, mitigating, arranging around, or repairing them, and those options were developmentally available rather than merely externally imaginable.*

The cascade-management category is structurally specifiable; cascade-management effort is real and analyzable; whether the agent is *responsible* for engaging cascade-management is Section 9's question, not Section 6's. Section 6 establishes that cascade-management is a distinct effort-category and analyzes its structural form; Section 9 develops the accountability analysis along the source-compromise continuum (5.9), the developmental-window overlay (4.10), and the layered output-structure (5.6).

## 6.12 Summary: effort as agency's resistance-profile

Section 6 has developed will, willing, trying, and effort as the structural phenomenology of operator-bundle direction under resistance. The section's results organize the rest of the paper:

| Section 6 result | Section that uses it |
|---|---|
| Willing is operator-bundle-mediated direction; will-as-function discipline preserved | Section 7 (decision and deliberation), Section 8 (variations), Section 9 (responsibility) |
| Trying is willing under incomplete guarantee — a structural configuration distinct from intending, deciding, acting, struggling, and effort | Section 7 (decision events), Section 8 (variations involving trying-without-success), Section 10 (empirical distinctions) |
| Effort is operator-bundle direction under resistance — a structural cost-profile, taxonomized by resistance-source | Section 8 (effort-pathologies developed in full), Section 9 (effort and accountability), Section 10 (effort markers in experimental work) |
| Effort phenomenology is order-specific, with foundational-order effort (attentional, cognitive, embodied) and constructed-order effort (asking, team-coordination, institutional-direction) following the order's target-domain | Section 7 (order-asymmetric Mode B), Section 8 (order-specific variations), Section 10 (order-specific effort markers) |
| Effort-economy varies by strategy (direct, configurational, slingshot) and by mastery (constructed vs compiled willing) | Section 8 (strategy-pathologies), Section 11 (Pred 22 effort-economy markers) |
| Low effort can indicate mastery, automaticity, or capture; high effort can indicate poor toolkit-development, cross-order conflict, or substrate resistance — effort and agency-quality are structurally separate | Section 7 (low-effort decisions), Section 8 (effort/agency variations), Section 10 (empirical interpretation discipline) |
| Effort and outcome are structurally separate: effort can be real without success, and success can occur without effort or willing | Section 9 (outcome-attribution vs agency-attribution), Section 10 (Libet/Wegner/Soon distinctions) |
| Cascade-management effort is a structurally distinct category, anticipating, mitigating, arranging-around, or repairing the agent's own downstream cascade-effects | Section 9 (responsibility for cascade effects, with developmental-availability guardrail) |

Section 6 therefore completes the transition from live-option construction to agency phenomenology. The I does not merely possess options; it directs itself through them, resists what opposes that direction, arranges conditions to reduce unnecessary resistance, and learns — or fails to learn — how to make effort economical across foundational and constructed orders. The structural phenomenology of this direction-under-resistance is what Sections 7, 8, 9, 10, and 11 build on.


---

# 7. Deliberation and decision: selection-events, reflective access, and Mode B availability

Section 5 specified what the I can construct as live. Section 6 specified what it is for the I to direct itself through live options under resistance. Section 7 now analyzes the *selection-event itself*. A decision is not identical to deliberation, effort, action, or outcome: deliberation processes live options; effort sustains direction under resistance; action implements; outcome results. Decision is the *operator-bundle selection by which one live option, course-skeleton, or coordinated option-configuration becomes the I's selected direction*. Because the architecture treats free choice as an inside-perspective configuration, decision must be analyzed through live-option construction (5.2), $\Pi$-ranking and PtCns coherence (3.2 Conditions 2), Mode B reflective availability (3.2 Condition 5), source-access ($\phi$, 4.8), ownership-integration (3.2 Condition 6), and order-domain structure (4.4, 5.7).

The section's controlling thesis:

> *A decision is not an outcome, not an effort-profile, and not necessarily a verbalized judgment. A decision is a selection-event within a toolkit-constructed live-option space, in which the I's operator-bundle commits direction toward one option, course-skeleton, or cross-order configuration.*

Section 7's distinctive architectural contribution is the *order-asymmetric availability of Mode B object-domains*: one Mode B reflective-access capacity (Condition 5), but the object-domains it can take as object — first-order focusing, second-order thought, third-order action, constructed-order strategy, source-status, $\Pi$-ranking, PtCns relation, ownership-integration — vary in availability across orders and configurations. This asymmetry is what makes some agency-failures structurally specifiable as Mode B object-domain unavailability rather than as Mode B absence.

Section 7 does not assign responsibility (Section 9 does that); does not engage the Libet/Wegner/Soon empirical literature (Section 10 does); does not develop the variation taxonomy in full (Section 8 does); and does not promote the operationalization candidates flagged in 6.7 to formal predictions (Section 11 does). Section 7 supplies the structural apparatus those sections build on: the decision-event, Mode B availability and asymmetry, the dissociations between decision and deliberation, the dissociations between decision and outcome, post-hoc recognition versus confabulation, and the constructed-order generalization of decision.

## 7.1 From effort to selection

Section 6 ended with effort as agency's resistance-profile. Section 7 now develops decision as agency's *selection-profile*. The transition is structural and clean: Section 6 analyzed what happens when the I directs itself through a live option under resistance; Section 7 analyzes how the I selects among live options in the first place.

| Section | Owns |
|---|---|
| Section 5 | What options are live; verification-toolkit; live-option construction lemma |
| Section 6 | What effort is; resistance taxonomy; effort-economy across strategies |
| Section 7 | How selection-events occur; deliberation; Mode B availability and asymmetry |
| Section 8 | Agency variations and pathologies in full |
| Section 9 | Responsibility and accountability attribution |
| Section 10 | Empirical interface (Libet, Wegner, Soon) |

The section ownership matters because it prevents Section 7 from sprawling into responsibility analysis or empirical interpretation. Section 6 already distinguished trying from deciding and explicitly assigned the decision-event structure to Section 7. Section 7 now owns it.

A core paragraph that orients the rest of the section: the I may possess live options, may exert effort toward one, and may try under incomplete guarantee — yet a further structural question remains. *When, and how, does the I select?* Decision is the structural answer: the event or process through which the operator-bundle commits direction toward one live course rather than another. The remainder of Section 7 unpacks this minimal claim across deliberation, fuzzy-course-skeletons, Mode B availability and asymmetry, dissociations between decision and other agency-categories, and the constructed-order generalization.

## 7.2 Deliberation as second-order / constructed-order option-processing

Deliberation is one possible mode of engaging with live options before selection — not the only mode, and not the criterion of free choice. The architecture's discipline:

> *Deliberation is toolkit-mediated option-processing in which the I compares, simulates, ranks, reframes, or tests live options before selection.*

Deliberation operates primarily at second-order (thought-paths over the option-space) and at constructed orders (option-processing over not-I coordination structures). It can include first-order option-processing in special cases (the contemplative practitioner deliberating over focus-targets), but its characteristic locus is second-order projection-and-comparison and constructed-order strategy-evaluation. *Constructed-order deliberation utilizes second-order cognitive substrate (thought-paths supply the medium) but explicitly takes not-I coordination structures as its evaluative target — preserving the 5.7 membership-test guardrail at the deliberation stage.* The negotiator's deliberation about how to ask runs on second-order thought-paths but its target is the asking-protocol with the addressed agent; the leader's deliberation about how to direct a team runs on second-order substrate but targets the team-coordination structure. The components a deliberation may engage:

| Deliberation component | Architectural role |
|---|---|
| Option comparison | Comparing members of $\mathcal{O}_{m,t;d}$ with the toolkit's evaluative apparatus |
| Projection | PCE-over-projection over future states each option produces (affect paper §7); the projection-toolset supplies the future-state representations on which evaluation operates |
| $\Pi$-ranking | Preservation/action-priority ordering across the option-space |
| PtCns testing | Frame-coherence check — does this option preserve "who-the-I-is"? |
| Source-access inquiry | $\phi$-pathway construction — where does this option come from? |
| Inhabitability testing | "Can I be the I who does this?" |
| Implementation preview | Substrate / lower-order feasibility testing |
| Reframing | Changing the option-space itself by reorganizing the categorial structure under which options are constructed |

*Deliberation can itself be effortful*, where option-processing encounters cognitive resistance, $\Pi$-conflict, PtCns resistance, projection-toolset limits, source-pathway uncertainty, or constructed-order friction; Section 6.4's resistance taxonomy supplies the structural decomposition. The architecture treats deliberation-effort as one application of the resistance-taxonomy framework, not a separate effort-category.

Deliberation can be *thin* or *thick*. Thin deliberation operates rapidly and largely implicitly: PtCns and $\Pi$-weighting engage with the option-space, evaluation runs without extended explicit projection, and selection follows quickly. Most everyday choices are thin-deliberative or non-deliberative entirely. Thick deliberation involves explicit Mode B engagement, extended projection-toolset work, and often iterative reframing — career changes, jury verdicts, major commitments, ethically charged decisions where PtCns must be tested explicitly. The thin/thick distinction is a continuum, not a binary; the same agent may deliberate thinly on a familiar choice and thickly on an unfamiliar one. Mastery (5.7) compresses thick deliberation into thin deliberation within the mastered domain — the experienced negotiator deliberates thinly where the novice deliberates thickly.

*The thin-deliberation threshold.* Thin deliberation still requires *some* contrastive option-processing — comparison, ranking, projection, reframing, or testing, however compressed. Mere implicit evaluative engagement by PtCns or $\Pi$-weighting on a single option is not by itself deliberation; it may be evaluative engagement supporting non-deliberative selection (per 7.7's decision-without-deliberation analysis), but deliberation requires that the toolkit's processing operate over the *contrast* between live options. The distinction matters because it preserves both the deliberation/decision distinction and the decision-without-deliberation class:

| Case | Classification |
|---|---|
| Implicit evaluation without contrastive processing | Non-deliberative selection (per 7.7) |
| Rapid contrastive comparison or ranking | Thin deliberation |
| Explicit reflective comparison and projection | Thick deliberation |

The architectural commitment that follows: *deliberation is not free choice itself*. It is one way the toolkit processes live options before selection. Decision can occur with or without deliberation; free choice can occur with or without deliberation; mature agency includes both deliberative and non-deliberative free choice. Section 7.7 develops decision-without-deliberation explicitly as a class of free-choice configuration the architecture must accommodate.

## 7.3 Decision as operator-bundle selection-event

This is Section 7's load-bearing subsection.

> *A decision is an operator-bundle selection-event in which one live option, course-skeleton, or coordinated option-configuration becomes the I's selected direction.*

The definition is minimal by design. It does not require that the I articulate the selection at the moment, that deliberation precede it, that Mode B be exercised on the selection-process during the event, that the outcome succeed, or that the selection track all available reasons. It requires only: a contrastive live-option space (Condition 1), and the operator-bundle's transition from "multiple live options" to "one selected course" (Condition 3 exercised). The other conditions of free choice (Conditions 2, 4, 5, 6) qualify the decision as a *free-choice-proper decision*; the decision-event itself can occur in degraded or compromised configurations and still be a decision.

*The decision taxonomy.* Four classes the architecture distinguishes:

| Class | Architectural status |
|---|---|
| **Decision-event** (minimal) | Operator-bundle selection-event resolving live-option contrast; Conditions 1 and 3 satisfied at minimum |
| **Free-choice decision** | Decision-event satisfying all six free-choice conditions of 3.2 |
| **Apparent decision** | Later narrative or felt authorship without an actual operator-bundle selection-event having occurred at the relevant time |
| **Degraded / impaired decision** | Selection-like event with one or more compromised conditions — substrate-preempted, source-compromised, ownership-disrupted, or under collapsed Mode B availability |

The taxonomy prevents the overclaim that every degraded "decision-like" event is structurally a decision in the same sense, while preserving the discipline that decision-events occur in degraded configurations without thereby becoming non-decisions. Apparent decisions and confabulated decisions (per 7.9) are not decision-events at all; they are post-hoc $\phi$-constructions over absent or differently-structured selection-processes.

The decision-event has structural dimensions the architecture's apparatus tracks. The agency derivation schema of 4.8 supplies the template; Section 7 specializes it to decision:

| Dimension | Decision-question |
|---|---|
| $\kappa$ (contact) | What live options, cues, or reasons is the I in contact with at the moment of selection? |
| $\phi$ (verification) | Can the I access the source-pathways of the selection? *$\phi$-status of the decision itself (the felt selection) and $\phi$-status of the decision's source-pathways are distinct: a decision may be $\phi$-clear as felt selection while its source-pathway remains low-$\phi$ or conscious-fuzzy.* |
| $\rho$ (identity-correlation) | How structurally integrated is the selected option with the lived-I profile? *$\rho$ here names the foundation's identity-correlation coordinate (File 3), not "resonance" or felt affinity. $\rho$ is the coordinate that tracks integration as a degree; ownership-integration (Condition 6 of free choice in 3.2) is the corresponding free-choice condition. The two are related — $\rho$-status is one input to whether ownership-integration is satisfied — but they are not identical: $\rho$ is a coordinate, ownership-integration is a condition.* |
| $\Pi$ (priority) | How strongly is the selected option action-prioritized? |
| $A_{m,t}(x)$ (availability) | Is the decision-event content $x$ phenomenally available to the I at decision-time? Binary status; for joint $A_{m,t}(x)/\phi(x)$ class (conscious-clear, conscious-fuzzy / source-opaque, latent / retrievable, unconscious-operative), or for post-hoc recognition cases ($A_{m,t}(x)=1$ at decision-time with $\phi$-construction at $t' > t$), see §4.8. |
| Order | Is the selected option first-, second-, third-, or constructed-order? |
| Strategy | Is the decision direct, configurational, slingshot, or mastered-domain? |
| Source-status | Is the option-space clean, scaffolded, source-compromised, or poisoned? |
| Ownership | Is the decision integrated as the I's act? (Condition 6 of free choice; $\rho$-status above is the coordinate input to this condition) |

Different decision-types occupy different regions of this space. The architecture distinguishes several characteristic configurations:

| Decision-type | Deliberation | Construction state | Example |
|---|---|---|---|
| Spontaneous selection | Thin or implicit | Skeleton, rapid | Libet button-press; skilled chef's next chop |
| Deliberative free choice | Thick, explicit | May involve extended projection | Career change; jury verdict |
| Mastered-domain selection | Compressed, implicit | Nearly full pre-compilation within mastered envelope | Grandmaster's immediate move-choice |
| Decision under incomplete guarantee | Variable | Fuzzy course-skeleton with trying-structured follow-through | Negotiating a salary; asking for a date |
| Configurational selection | Variable | Present arrangement directing future option-space | Setting up an environment to make exercise easy |
| Slingshot selection | Concentrated in timing | Skeleton-level commitment at opportune moment | Releasing a difficult conversation at the right time |

Each configuration is a structurally specifiable decision-event. The architecture's commitment is that *all of them are decisions*: the operator-bundle commits direction, the live-option contrast resolves, the I has a selected course. They differ in their deliberation-profile, their construction-state, their effort-economy, and their order-target — not in whether they are decisions.

*A decision-event can synchronously select a cross-order coordinated configuration.* Many actual decisions select not a single-order option but a cross-order coordinated configuration: the contemplative practitioner's decision to "settle in" synchronously selects first-order focus-stabilization and third-order breath-regulation; the speaker's decision to "address the audience" synchronously selects second-order thought-organization, third-order vocal projection, and fourth-order audience-protocol engagement; the surgeon's decision to "begin the procedure" synchronously selects first-order attentional configuration, third-order motor-readiness, and fourth-order team-coordination cuing. The order-tagged action-space of 5.2 and the constructed-order apparatus of 5.7 govern these cases — the cross-order configuration is specifiable as a coordinated set of order-tagged options selected by a single operator-bundle commitment. The decision-event remains structurally singular even when its target is cross-order; what is selected is the *configuration*, not a sequence of separate decisions across orders.

The decision-event must be distinguished from several adjacent phenomena that resemble it:

| Phenomenon | Distinction from decision |
|---|---|
| Deliberation | Option-processing prior to or alongside selection; not identical with the selection-event itself |
| Trying | Direction under incomplete guarantee, may follow decision but is not the selection-event |
| Effort | Resistance-cost of sustaining direction; may accompany decision but is structurally separate (Section 6.4) |
| Action | Implementation event; may follow decision or proceed without operator-bundle selection (reflex, automatism) |
| Outcome | Resulting state; not identical with decision (effort/outcome separation, 6.9; decision/outcome separation, 7.10) |
| Post-hoc narration | $\phi$-construction after the decision; may be accurate (post-hoc recognition) or inaccurate (confabulation) per 7.9 |

The decision-event is therefore the *structural transition* in the configuration of the action-space — from "multiple live options" to "one selected course" — with the operator-bundle's commitment as the structural marker of the transition. The transition can be temporally extended (fuzzy-edged in time, per 7.4), but the structural fact of commitment is what makes it a decision.

## 7.4 Decisions over fuzzy-constructed course-skeletons

The fuzzy-construction discipline of Section 3.2's Condition 1 and 5.3's dynamic-refinement note propagates directly to decision-event structure. The forward design constraint placed in 6.12 — that Section 7 must handle decisions selecting fuzzy course-skeletons as the structurally normal case — is implemented here.

> *A decision need not select a fully-specified executable sequence. It may select a course-skeleton that is live because the toolkit has trained expectation of dynamic refinement during execution.*

Examples across orders illustrate the pattern:

| Decision | Selected object |
|---|---|
| "I'll cook pasta tonight" | Foundational fuzzy course-skeleton with routine dynamic refinement |
| "I'll write the essay on X" | Second-order project-skeleton with extensive dynamic refinement |
| "I'll negotiate for the higher offer" | Constructed-order strategy-skeleton with not-I-response-dependent refinement |
| "I'll tell the truth" | PtCns-stabilized action-orientation with details unresolved |
| "I'll start the task now" | Third-order initiation-skeleton with execution-detail refinement |
| "I'll help when she calls" | Slingshot-conditional fuzzy course with timing-dependent activation |

Each is a genuine decision: the operator-bundle commits direction to the course-skeleton, the live-option contrast resolves, the I has a selected course. The decision is not deficient or weakened by the fuzziness of the selected course; it is structurally normal.

The trained-expectation discipline propagates from 3.2 and 6.4: a fuzzy course-skeleton is not mere hope. It counts as live, and its selection counts as a decision, only when the trained expectation of dynamic refinement is grounded in prior competence, scaffold availability, environmental regularity, or domain-specific mastery (5.7). The agent who "decides" to perform a complex surgery without surgical training has not made a free-choice decision over a live course; the toolkit cannot construct the surgical course at skeleton-level resolution with grounded trained expectation. The fuzzy-construction discipline is therefore a *real* constraint on what counts as a decidable course, not a permissive hedge that allows any vague intention to qualify.

*Where the trained-expectation grounding fails, the event is not a decision over a live course.* If the selected skeleton is too coarse for trained dynamic refinement — the agent's toolkit cannot construct the next executable level even at skeleton-resolution, the variance-envelope is exhausted, the not-I conditions diverge from any projected trajectory the toolkit can navigate — the event is better classified as *aspiration*, *fantasy*, *intention-fragment*, or *wishful projection* rather than as a decision over a live course. The four-class distinction matters for Section 8's variation taxonomy: aspiration without grounded trained expectation is a candidate-content the toolkit may develop into a live course over time, but the present event is not a free-choice decision in the structural sense.

The temporal structure of fuzzy-skeleton decisions deserves comment. A decision that selects a course-skeleton initiates a will-act whose execution-level details elaborate dynamically:

| Moment | Structural status |
|---|---|
| Decision | Selection of live course-skeleton |
| Trying | Direction through incomplete guarantee — may begin immediately if implementation pathway has gaps |
| Effort | Cost of sustaining direction under resistance encountered during refinement |
| Execution | Dynamic refinement and substrate implementation across the willing-period |
| Outcome | Success or failure of the will-act; not identical with the decision |

The decision-event is structurally distinct from the subsequent trying, effort, execution, and outcome. The fuzzy-construction discipline does not blur the decision into the trying; the selection commits the operator-bundle to the course-skeleton, and the trying-structure begins (when there is incomplete guarantee in execution) after the selection. Section 7.10 develops this separation more fully.

## 7.5 Mode B reflective availability versus exercised deliberation

Condition 5 of free choice (3.2) requires *non-confabulatory Mode B reflective availability*, not actual reflective exercise during the selection-event. Section 3 already establishes this through its post-hoc recognition treatment: the agent may select under intact conditions and only later construct full $\phi$-access to why. Section 7 develops the implications.

> *Mode B availability is not deliberation. Deliberation is one possible use of Mode B / second-order toolkit processing. Mode B availability means the choice-process can be taken as object under intact conditions without requiring confabulation.*

The distinction matters because it allows free choice to occur in non-deliberative configurations while still requiring the reflective-accessibility apparatus that distinguishes free choice from automatism, confabulation, and reflex. The agent who acts skillfully without explicit deliberation, who responds in a moral emergency without prolonged reflection, or who lives habitually-chosen patterns without reviewing them at every juncture can satisfy Condition 5 because Mode B *could* engage with the selection-process under intact reflective conditions, even though Mode B was not actively engaged during the selection.

The distinction generates a six-row classification of decision-configurations relative to deliberation and Mode B:

| Case | Deliberation exercised? | Mode B available? | Free choice possible? |
|---|---|---|---|
| Reflective deliberative choice | Yes — explicit | Yes | Yes |
| Skilled spontaneous choice | No or minimal | Yes | Yes |
| Flow | No during action | Yes under intact post-action conditions | Yes, if other conditions hold |
| Apparent choice / confabulated decision | Narrative yes, actual no | No (or compromised) | No or impaired |
| Reflex | No | No relevant selection-object | No (not a decision) |
| Alienated action | Possibly | Available but ownership disrupted | Impaired (Condition 6 failure) |

The architecture's load-bearing claim: *a choice can be non-deliberative but still free; it cannot be free if it requires confabulation to appear authored*. Mode B availability is the architectural marker of free choice's reflective dimension; deliberation is one (often valuable, sometimes interfering) exercise of it.

A note on flow that the apparatus handles cleanly: during flow, Mode B exercise on the selection-process can interfere with execution (the gymnast who reflects mid-routine on her selection of the next move may disrupt the routine). This is not Mode B unavailability; it is Mode B exercise being inappropriate for the configuration. Mode B *could* engage post-action under intact conditions — and typically does, in the form of post-flow reflection — without confabulation. Flow is therefore a free-choice-compatible configuration with Mode B available but appropriately not exercised during action.

*Mode B availability is a counterfactual capacity under intact conditions.* Mode B availability means the selection-process can be taken as object under intact reflective conditions without requiring false source-construction. It does not mean the agent is currently reflecting; it does not mean later narrative report is automatically reliable; it does not mean Mode B engagement is appropriate at every moment. The counterfactual specification — *can be exercised under intact conditions without confabulation* — is what does the work in Condition 5.

*Transient unavailability under high-bandwidth execution does not by itself violate Condition 5.* Some configurations involve transient Mode B unavailability during the willing-period because cognitive load, time-pressure, or substrate engagement consumes bandwidth that would otherwise support Mode B exercise — the surgeon mid-procedure, the athlete mid-performance, the parent responding to an emergency cannot reflectively access their own selection-processes during the high-bandwidth period. What matters for Condition 5 is whether the process is later reflectively accessible under intact conditions without confabulation. Transient unavailability during execution combined with intact post-action reflective access satisfies Condition 5; transient unavailability combined with confabulated post-hoc narrative does not.

## 7.6 Order-asymmetric Mode B object-domain availability

Section 7's distinctive architectural contribution.

The claim: *Mode B is one capacity, but its object-domains are multiple, and their availability to Mode B reflection is asymmetric across orders and configurations.* The I may be able to take its thinking as object but not its substrate action; its focus but not its social strategy; its decision-outcome but not its actual selection-source. Mode B object-domain asymmetry is what makes some agency-failures structurally specifiable as failures of object-domain availability rather than as Mode B absence.

The architecture posits no new Mode B subtype. There is one Mode B reflective-access capacity, with multiple object-domains it can take as object, and characteristic asymmetries in what it can inspect across orders and configurations.

The object-domain table:

| Object-domain | What Mode B can inspect when available |
|---|---|
| First-order focusing | "Where is my attention going?" |
| Second-order thinking | "What am I reasoning, imagining, comparing?" |
| Third-order acting | "What is my body / action doing?" |
| Constructed-order strategy | "What am I doing socially / institutionally / coordinatively?" |
| Source-status | "Where did this option come from?" |
| $\Pi$-ranking | "Why does this matter / feel urgent?" |
| PtCns relation | "Can I do this coherently with my frame / who I am?" |
| Ownership-integration | "Is this mine?" |

Asymmetric availability appears in characteristic configurations:

| Configuration | Mode B asymmetry |
|---|---|
| ADHD-like task failure | Variable: the substrate-developmental gap may be *partially* reflectively available — many ADHD agents articulate the gap phenomenologically with notable insight — but the gap cannot be overcome by Mode B reflection alone. The asymmetry is between phenomenological-availability of the gap (often present) and reflective-overcoming of the gap (absent under Mode B alone) |
| Compulsion | Agent can reflectively oppose the act and observe the substrate-pull; cannot bring third-order capture under operator-bundle control through Mode B alone |
| Social manipulation | Agent can reflect on the option selected; source-status of the option-space (poisoned by the manipulator's input-shaping) is not reliably accessible via Mode B |
| Skilled flow | Agent can reflect before and after; reflection during disrupts performance — Mode B object-domain available but exercise inappropriate to configuration |
| Shame / self-consciousness | Excessive Mode B engagement on the presentation-domain disrupts the very action being presented; the asymmetry is between excess and appropriate exercise |
| Dissociation | Agent can observe action as event; cannot integrate it as the I's action — Mode B available on action-observation, ownership-integration object-domain compromised |
| Source-opaque emotion | Agent can reflect on the emotion's phenomenology and present effects; the emotion's source-pathway (trauma, conditioning, somatic state) is in conscious-fuzzy availability, not in conscious-clear |
| Constructed-order over-extension | Agent can reflect on first- through third-order activity; constructed-order coordination at orders beyond mastery is conscious-fuzzy or unavailable to Mode B inspection |

The asymmetry has an architectural basis: Mode B availability tracks the foundation's joint $A_{m,t}(x)$ / $\phi$ taxonomy (File 3 §6.1). Object-domains in the conscious-clear region are reliably available; object-domains in conscious-fuzzy are partially available with limited articulability; latent object-domains require effortful $\phi$-construction to bring into Mode B; unconscious-operative object-domains operate without entering Mode B at all unless verification-tools are deployed to surface them. Order-asymmetry of Mode B is therefore the structural manifestation of the joint $A_{m,t}(x)$ / $\phi$ profile across the agency-relevant object-domains — not a special feature of agency but the agency-side reading of an apparatus the foundation already specifies.

*Mode B object-domain availability is not identical to joint $A_{m,t}(x)$ / $\phi$ status.* The joint $A_{m,t}(x)$ / $\phi$ taxonomy describes phenomenal availability and source-pathway access of *contents*; Mode B object-domain availability describes whether a given *agency-structure* — attention, action, source-status, $\Pi$-ranking, ownership, constructed-order strategy — can be taken as object by reflective self-modeling. The former constrains the latter (an agency-structure with conscious-fuzzy or latent / retrievable contents will be correspondingly less reliably available to Mode B), but the latter is an application-level agency specification. The agency paper's distinctive contribution at 7.6 is the agency-side reading of the joint $A_{m,t}(x)$ / $\phi$ apparatus, not a re-derivation of $A/\phi$ itself.

*Constructed-order Mode B availability is bandwidth-limited.* The implementation chain for constructed orders involves more stages of substrate mediation, each introducing lossy compression per 5.6 (output-imprinting cascade) and 5.7 (constructed-order generalization). Mode B access to constructed-order decision-events tends to be less detailed, less articulable, and more prone to source-opacity than access to foundational-order decisions. The fourth-order asking-act, the fifth-order team-coordination act, the institutional-order procedural act all reach the I's reflective-access via implementation chains that compress information at each stage; the reflective image of the constructed-order decision is therefore a compressed, lossy reading of the actual selection-event. The architectural claim is that this bandwidth-limitation is *structural*, following from the implementation-chain structure of constructed orders, not contingent on the agent's introspective skill — though developed introspective and verification-tool capacities can partially compensate for the lossiness.

The architectural payoff for downstream sections: many configurations Section 8 will analyze (compulsion, dissociation, akrasia, source-compromised mastery, ADHD-like, manipulation under-recognition) are structurally specifiable through *which Mode B object-domain is unavailable or compromised*, with the rest of Mode B intact. This avoids both over-claiming Mode B failure (the compulsive agent has not lost reflective-access generally; only specific object-domains are compromised) and under-claiming agency-impairment (the compulsive agent is structurally constrained at exactly the object-domain whose availability matters for the act in question).

## 7.7 Decision without deliberation

Decision-without-deliberation is a class of free-choice configuration the architecture must accommodate to avoid over-intellectualizing agency.

> *Decision without deliberation occurs when selection resolves without extended explicit option-processing, while the six conditions of free choice remain satisfied.*

Cases of decision-without-deliberation that satisfy the six conditions:

| Case | Why it may still be free |
|---|---|
| Skilled action selection | Option-space compressed by mastery; thin or implicit deliberation suffices because the toolkit pre-compiles the comparison |
| Emergency action | High salience compresses deliberation to seconds; rapid $\Pi$-ranking with non-confabulatory ownership |
| Moral immediacy | PtCns/$\Pi$ structure already settled; the option presents itself as already-evaluated by prior frame-coherent commitments |
| Habitual-chosen action | Upstream self-curation produces a current selection that is thin but owned (per 6.8 habit-marker discipline) |
| Slingshot timing | Agent waits in implicit gradient-reading; selection occurs at the recognized opportune moment without further deliberation |
| Mastered-domain spontaneous response | Compiled-domain willing produces selection with negligible explicit deliberation |

The architecture's discipline forecloses the inference that absence-of-deliberation indicates absence-of-agency. The recovering agent's quick refusal of a familiar trigger, the experienced surgeon's rapid mid-procedure decision, the moral-immediacy refusal of a wrongful order — each is a decision that may proceed with thin or absent deliberation while satisfying all six conditions of free choice.

*Decision-without-deliberation is free-choice-compatible, not automatically free.* The six cases above (skilled, emergency, moral-immediacy, habitual-chosen, slingshot, mastered-spontaneous) satisfy free choice only where the six conditions of 3.2 are *actually* present in the configuration: live-option space, evaluative engagement, operator-bundle selection, non-preemptive substrate coupling, non-confabulatory Mode B availability, and ownership-integration. The architecture does not commit to "non-deliberative selection is always free"; it commits to "non-deliberative selection can be free when the configuration satisfies all six conditions." Configurations that look non-deliberative but actually fail Condition 4 (preempted by substrate capture) or Condition 5 (Mode B compromised or confabulating) or Condition 6 (ownership-integration disrupted) are not free choices despite the absence of deliberation. The discipline prevents over-extension of decision-without-deliberation into a permissive class.

The distinction from non-deliberative non-decisions is essential. Decision-without-deliberation must be distinguished structurally from reflex, compulsion, and automaticity:

| Non-deliberative event | Classification |
|---|---|
| Reflex withdrawal (e.g., from a hot stove) | Not a decision; substrate response without operator-bundle mediation |
| Compulsive act | Substrate capture; Condition 4 failure (preemption) |
| Skilled pass-through action | Mastered-domain decision or low-friction selection — decision-class |
| Moral refusal under immediacy | High PtCns / $\Pi$ pre-structured selection — decision-class |
| Confabulated "choice" | Apparent decision; not actual decision (per 7.9) |
| Habitual-chosen action | Decision-class (thin, owned, source-clean) per 6.8 |
| Habitual-compulsive action | Substrate-coupling preemption (Condition 4 failure); not a decision in the strong sense |

The distinguishing structural marker is the configuration of the six conditions — most centrally Condition 3 (operator-bundle selection actually exercised) and Condition 4 (substrate coupling without preemption). Mode B availability remains required even when not exercised; ownership-integration remains required.

## 7.8 Deliberation without decision

Deliberation can occur without producing decision. This is the structural counterpart to 7.7 and is essential for analyzing paralysis, rumination, learned helplessness, and other configurations where option-processing fails to resolve.

> *Deliberation without decision occurs when toolkit-mediated option-processing continues without operator-bundle selection.*

Cases:

| Case | Structural form |
|---|---|
| Decision paralysis | Evaluability overload; comparison and projection do not converge to selection |
| Rumination | Second-order loop without selection — comparison cycles return to the same content without resolution |
| Anxiety-driven projection | Threat-projection paths consume option-processing without yielding selection |
| Learned helplessness | Projection-toolset returns no viable pathway; the option-space contracts before selection-resolution |
| Moral conflict | PtCns / $\Pi$ conflict prevents coherent selection — multiple options are evaluable but none satisfies frame-coherence sufficient for commitment |
| Manipulated ambiguity | Source-compromised option-space blocks stable selection because the available evaluative apparatus has been poisoned (5.9) |
| Severe depression | Multi-order projection collapse; the evaluative apparatus runs but cannot produce sufficient differentiation among options for the operator-bundle to commit |

A critical distinction the architecture must mark: *not deciding can itself be a decision*. When withholding, delay, refusal, or non-action is itself live and selected, the operator-bundle has committed to that course. The agent who *decides* to wait, *decides* not to respond, *decides* to refuse, *decides* to do nothing has made an omissive decision, not a non-decision. The structural marker is whether the live-option space included withholding/delay/refusal/non-action as a live option, and whether the operator-bundle selected it.

| Non-decision case | Selected? | Classification |
|---|---|---|
| Paralysis | No | Deliberation without decision |
| Strategic delay | Yes (withhold-now) | Decision to withhold |
| Avoidance by collapse | No or impaired | Variation / pathology (Section 8) |
| Refusal | Yes (refuse) | Omissive decision |
| Drifting | No | Non-selection / passive trajectory |
| Withholding-as-protest | Yes (withhold-publicly) | Constructed-order omissive decision |
| Procrastination | Mixed — depends on whether delay was selected or whether selection failed | Section 8 develops |

The omissive-decision class is important because it allows the architecture to recognize active non-action as agency-positive while distinguishing it from collapse, paralysis, and avoidance. Section 8's variations will use this structural distinction extensively. *Procrastination specifically is deferred to Section 8 because it is structurally mixed and configuration-dependent: it can be selected delay (omissive decision toward strategic timing), avoidance collapse (deliberation without decision under threat-projection), source-compromised reframing (self-deceptive delay), anxiety-driven loop (threat-projection consuming option-processing), implementation-gap-driven delay (ADHD-like substrate-developmental constraint at orders 1–2), or configurational delay (autonomy-supporting timing strategy). Section 7 establishes that procrastination is not a single architectural category; Section 8's variation taxonomy decomposes the procrastination-cluster into its structurally distinct configurations.*

*Affect modulates deliberation and decision.* Affective configurations alter deliberation and decision by changing $\Pi$-weighting, projection-toolset availability, action-pathway construction, source-access, and substrate resistance. Anxiety may consume deliberation through threat-projection — the projection-toolset runs but produces threat-paths rather than goal-oriented future-states, blocking selection-resolution. Shame may increase PtCns resistance — the option's $\rho$-status is incompatible with the agent's frame-coherence, blocking selection without intervening reframing. Depression may collapse projection and salience — no option produces sufficient differentiation in projected outcome to support selection. Hope may stabilize a viable pathway — the projection-toolset constructs a representable future-state that supports operator-bundle commitment. Fear may narrow the option-space — Condition 1's contrastive live-option space contracts under threat-projection. Devotion may stabilize $\Pi$-priority — the option's preservation-priority weighting becomes settled, reducing $\Pi$-conflict and supporting commitment. Joy and engagement may expand projection-toolset operation — more future-states become representable as live courses. The affect paper supplies the affect-side taxonomy in detail (PCE-over-projection, threat-cluster, depression-cluster, somatic states); Section 7 treats affective configurations as *modifiers of option-processing and selection*. Section 8 develops the variation-level interactions in full.

## 7.9 Post-hoc recognition, source-opacity, and confabulated decision

The $A/\phi$ apparatus distinguishes three configurations the empirical literature has often conflated. Section 7.9 develops the distinctions; Section 10 applies them to Libet/Wegner/Soon paradigms.

| Configuration | $A/\phi$ structure | Classification |
|---|---|---|
| Post-hoc recognition | Decision was structurally free at the moment of selection; $\phi$-access to source-pathways emerges later through reflective construction | Compatible with free choice |
| Source-opaque decision | Decision satisfied the six conditions; $\phi$ is low or undefined for the source-pathways even after reflection; Mode B availability is non-confabulatory in the sense of not generating false $\phi$ | May still be free if Mode B does not confabulate accuracy |
| Confabulated decision | $\phi$-narrative supplies apparent source-access for a process that was not actually selected, was bypassed, or was differently structured than the narrative suggests | Apparent choice, not genuine decision |

The distinction between post-hoc recognition and confabulation is structurally precise and load-bearing for Section 10:

> *Post-hoc recognition is not confabulation. In post-hoc recognition, the earlier selection satisfied the free-choice conditions, and the later $\phi$-construction reveals source-pathways that were operating but not articulable at the moment of selection. In confabulation, the later $\phi$-narrative supplies apparent source-access where the actual selection-process was absent, bypassed, or structurally different from what the narrative reports.*

The phenomenological resemblance can be high — both look like "I now realize why I chose that" — while the structural difference is sharp. Post-hoc recognition is $\phi$-construction over an actually-engaged operator-bundle selection; confabulation is $\phi$-construction over an absence-of-selection or a substrate-driven pseudo-selection. Section 10 develops the empirical implications: many Wegner-paradigm cases that appear to demonstrate "the illusion of conscious will" are confabulation cases in this sense, while many post-hoc reasons-construction cases that look similar are post-hoc recognition cases that do not impugn agency.

Source-opacity sits between the two. The agent acted; the operator-bundle did engage; the selection was made; but the $\phi$-pathway for *why* is genuinely unavailable to Mode B even after reflection. Source-opaque decisions can still be free, provided Mode B does not generate false $\phi$ to fill the gap. The discipline: *Mode B's non-confabulatory clause requires that absence-of-source-access be acknowledged as such, not papered over with constructed reasons that do not track the actual selection-process.* The affect paper's recognition-lag pattern (*Differentiated Affect* §3.3) handles a closely related $A/\phi$ dynamic in the affective domain — content with operative substrate-effects whose source-pathways become $\phi$-accessible only after delay. Section 7's source-opaque decision class is the agency-side specialization of the same $A/\phi$ apparatus.

*The distinction is architecturally sharp but operationally difficult.* The architecture's commitment is that the post-hoc-recognition / confabulation distinction is grounded in the *objective historical state of the operator-bundle at time $t$* — whether an actual selection-event occurred at the moment in question — not merely in the coherence of the agent's narrative at time $t+1$. This is what gives Section 10 its structural ground against Wegner-style overclaims that all $\phi$-construction is confabulation: post-hoc recognition tracks an actually-engaged operator-bundle selection; confabulation tracks an absence or bypass. The architecture does not claim that the agent's report alone settles which case obtains in actual instances. Empirical or clinical classification must rely on converging evidence — prior option-space construction, behavioral sequence, source-status of the option-space, substrate-coupling status, consistency of the $\phi$-construction over time, and whether the later $\phi$-narrative tracks an actually-engaged selection-process. The architecture's structural commitment makes the distinction operationally meaningful while acknowledging that in any particular case its determination may require multiple lines of evidence.

## 7.10 Decision, trying, action, outcome: four separations

Section 6 made effort/outcome separation load-bearing for Sections 7, 9, and 10. Section 7 generalizes this into a four-way separation that the rest of the paper depends on:

| Term | Structural meaning |
|---|---|
| Decision | Operator-bundle selection-event resolving live-option contrast into selected direction |
| Trying | Direction under incomplete guarantee — willing-acts whose completion is uncertain |
| Action | Implementation event — substrate or constructed-order activity producing movement, speech, or coordination |
| Outcome | Resulting state in the world — whether or not intended, willed, decided, or attempted |

The four are dissociable in actual cases:

| Case | Decision | Trying | Action | Outcome |
|---|---|---|---|---|
| Decide and act successfully | Yes | Maybe | Yes | Intended |
| Decide but fail to act | Yes | Maybe | No or partial | Absent or partial |
| Decide but blocked externally | Yes | Maybe | Blocked (door locked, mic fails, interruption) | No intended outcome despite intact decision |
| Try without prior crisp decision | Maybe implicit | Yes | Yes or partial | Uncertain |
| Reflex succeeds | No | No | Yes | Outcome occurred |
| Confabulated choice with action | Apparent only | Unclear | Yes | Outcome occurred |
| Configurational success | Prior decision active | Maybe low current trying | Indirect through arranged conditions | Intended |
| Decided to refuse, refused | Yes | Maybe (resisting pull to act) | No (omissive) | Intended-non-action |
| Substrate-driven action with decision-narrative | Apparent | No | Yes | Outcome with confabulated decision-attribution |

The four-way separation prevents conceptual contamination across sections. Section 9's responsibility analysis must distinguish outcome-attribution (what happened) from agency-attribution (what the agent did and decided). Section 10's empirical analysis must distinguish action-onset (motor activity beginning) from decision-event (operator-bundle commitment) from outcome-completion (state in the world). Section 8's variation taxonomy must distinguish failure-of-action (decided but didn't act) from failure-of-decision (couldn't select) from failure-of-outcome (acted but the world didn't cooperate). Each downstream analysis depends on the four-way separation Section 7 establishes.

## 7.11 Decision across foundational and constructed orders

Section 5.7's N-order generalization extends to decision-events. A decision can target any developed order: foundational orders 1–3 or constructed orders $4 \leq n \leq N(m,t;d)$.

| Order | Decision-object |
|---|---|
| First-order | Attend / not attend; shift focus / hold focus; orient toward / orient away |
| Second-order | Pursue thought-path; accept frame; compare; infer; reframe |
| Third-order | Move, speak, act; regulate body; initiate or stop substrate action |
| Fourth-order | Ask, request, persuade, comfort, deceive, direct |
| Fifth-order | Coordinate team; sequence roles; synchronize across agents |
| Institutional / sixth-order | Route action through formal structures; invoke or comply with protocols |
| Higher constructed orders | Design policy; reform institutions; structure cross-organizational coordination |

The architectural guardrail repeats from 5.7: *constructed-order decision is not merely deciding to move one's mouth or hands. It is deciding toward a not-I coordination target, implemented through lower-order action.* The fourth-order decision to ask for help is not the third-order decision to vocalize; the target of the will-act is the asking-protocol with the addressed agent, with third-order vocalization as the implementation medium.

This is the load-bearing structural distinction:

| Example | Order-reading |
|---|---|
| Saying the words "Can you help?" mechanically | Third-order vocal action |
| Asking for help as a request-protocol with the addressed agent | Fourth-order decision (target: not-I coordination structure) |
| Assigning roles in a working group | Fifth-order decision (target: team-coordination structure) |
| Filing a legal motion through institutional procedure | Institutional / sixth-order decision (target: institutional protocol) |
| Designing organizational policy | High constructed-order decision (target: institutional structure) |

A decision at a constructed order satisfies the constructed-order membership test of 5.7 (target is a not-I coordination structure, not lower-order activity with social side-effects), with Criterion 3's fuzzy-availability clause in v0.1.5.2: lower-order implementation must be sufficiently available at skeleton-level under trained expectation, not pre-constructed in full. The fourth-order decision to negotiate doesn't require pre-construction of every utterance; it requires that the negotiating-protocol be representable as a course-skeleton with trained expectation that the lower-order implementation will dynamically refine during the negotiation.

*Self-formative decisions are not automatically constructed-order.* Some decisions target the I's own future profile rather than immediate not-I coordination: "I will become someone who keeps commitments," "I will become sober," "I will train as a physician," "I will live more truthfully." These are *profile-formative configurational decisions* — configurational willing (5.8) over the agent's own future option-space — not constructed-order decisions in the target-domain sense. The target is the I's future profile, not a not-I coordination structure. When self-formative decisions are pursued through vows, social accountability, institutional roles, training regimes, or formal structures, they acquire constructed-order *components* (the institutional engagement is a constructed-order will-act with the institution as not-I target), but the underlying self-formative aim remains profile-formative configurational. The architecture's discipline prevents over-extending constructed-order decision into all long-range self-change.

*Moral neutrality of constructed-order decisions* extends the 6.6 effort-table reminder. Both autonomy-supporting and autonomy-undermining constructed-order decisions are structurally constructed-order; their moral status differs at source-status (5.9), not at order:

| Example | Order-classification | Source-status |
|---|---|---|
| Asking a colleague honestly for help | Fourth-order decision | Autonomy-supporting (transparent intent, source-clean) |
| Deceiving a counterpart during negotiation | Fourth-order decision | Source-compromised aim (manipulation continuum, 5.9) |
| Teaching a student honestly | Constructed-order decision targeting another agent's toolkit | Autonomy-supporting |
| Indoctrinating a student | Constructed-order decision targeting another agent's toolkit | Source-compromised aim |
| Designing institutional policy for accountability | High constructed-order decision | Autonomy-supporting |
| Designing institutional policy to capture rents | High constructed-order decision | Source-compromised aim |

The order-classification is the same in each pair; the moral distinction is at source-status, supplied by 5.9's manipulation continuum and Section 9's responsibility-attribution. Section 7 classifies decisions by structural mechanics; Section 9 assigns responsibility along the source-compromise continuum.

The decision-event structure (7.3) applies at any order. The deliberation/decision distinction (7.2/7.3), the fuzzy-skeleton selection (7.4), the Mode B availability/exercise distinction (7.5), the order-asymmetric Mode B object-domain availability (7.6), and the post-hoc-recognition/confabulation distinction (7.9) all operate at constructed orders as they do at foundational orders. Constructed-order decisions are not a special class of decision; they are decisions whose target is a not-I coordination structure rather than a focus-target, thought-path, or substrate action.

## 7.12 Decision-quality, decision-freedom, and decision-responsibility

Three distinctions Section 7 marks but does not fully develop, leaving Section 9 to handle responsibility-attribution proper:

| Concept | Meaning |
|---|---|
| **Decision-quality** | How well the decision tracks reasons, $\Pi$-ranking, PtCns coherence, source-status, and projected outcomes |
| **Decision-freedom** | Whether the six conditions of free choice are satisfied |
| **Decision-responsibility** | Whether ownership / sourcehood / developmental-availability / accountability conditions support attribution to the agent |

The three dimensions are *dissociable* — they often correlate (free decisions often support responsibility; high-quality decisions often preserve freedom; source-compromise can damage all three), but none reduces to either of the others. Decision-quality and decision-freedom can diverge:

| Case | Freedom | Quality |
|---|---|---|
| Free but foolish | High | Low — selection satisfies six conditions but tracks reasons poorly |
| Manipulated but strategically intelligent | Impaired (source-compromise) | High strategic quality within the compromised option-space |
| Coerced but prudent | Impaired (Condition 1 reduced live options) | High survival rationality given the constrained space |
| Akratic | Partial or conflicted; involves $\Pi$-conflict, $\rho$-divergence, or operator-bundle selection against endorsed evaluation; Condition 4 is compromised *only* where substrate capture or preemption is present, not in all akrasia | Conflicted — evaluation and selection diverge |
| Source-clean but mistaken | High | Factually poor — selection satisfies conditions but the world differs from the toolkit's projection |
| Mastered-domain skilled selection | High | High — both conditions and reasons-tracking are well-served |
| Source-compromised mastery (5.9, 5.7) | Impaired | High within compromised aims |

*Effort-economy can be a marker of decision-quality but does not determine decision-freedom.* A low-effort decision can be mastered, automatic, or captured; a high-effort decision can be free, conflicted, or impaired. Effort-economy per unit goal-progress, the configurational/slingshot to direct-willing ratio (per 6.7's Pred 22 candidate operationalization), and the ratio of mastered-domain to constructed-domain willing in a domain may be markers of decision-quality in that domain, especially where mastery or strategy-selection matters; they do not by themselves determine decision-freedom in the Condition-satisfaction sense. The architecture preserves Section 6.8's effort/agency-quality separation: effort-economy reads as a decision-quality marker only when interpreted alongside source-status, $\Pi$-relation, ownership-integration, substrate-coupling, and Mode B availability, not as a standalone freedom-marker.

Decision-freedom and decision-responsibility can also diverge: a structurally free decision may not be responsibly attributable in the strong sense if the agent's developmental-window status (4.10), source-compromise history (5.9), or available-options range (live-option-space contraction) limits accountability. Section 9 develops the responsibility-attribution analysis along all of these dimensions; Section 7's contribution is the structural distinction.

The boundary statement: *Section 7 classifies decisions. Section 9 assigns responsibility.* A decision may be structurally free but poor, strategically excellent but source-compromised, owned but developmentally scaffolded, or successful without being responsibly attributable in the strong sense — these are configurations Section 9 will analyze, given the structural apparatus Section 7 establishes.

## 7.13 Summary: decision as agency's selection-profile

Section 7 has developed deliberation, decision, and Mode B reflective availability and asymmetry as the structural apparatus of agency's selection-profile. The section's results organize the rest of the paper:

| Section 7 result | Downstream use |
|---|---|
| Deliberation is option-processing, not free choice itself | Section 8 (paralysis, rumination); Section 9 (decision-quality vs responsibility); Section 10 (empirical interpretation discipline) |
| Decision is the operator-bundle selection-event | Section 8 (variations); Section 9 (decision-attribution); Section 10 (decision-event timing) |
| Decisions can select fuzzy course-skeletons under trained expectation | Section 8 (execution-time variations); Section 10 (decision-vs-execution-onset distinctions) |
| Mode B availability is not exercised deliberation | Section 8 (flow, skilled action); Section 10 (Wegner paradigm) |
| Mode B object-domain availability is order-asymmetric | Section 8 (compulsion, dissociation, manipulation under-recognition); Section 10 (interference effects) |
| Decision can occur without deliberation | Section 8 (skilled, habitual, emergency action); Section 9 (responsibility for non-deliberative decisions) |
| Deliberation can occur without decision | Section 8 (paralysis, anxiety, learned helplessness); Section 9 (responsibility for omission) |
| Post-hoc recognition is not confabulation | Section 10 (Libet / Wegner / Soon empirical interface) |
| Decision, trying, action, outcome are dissociable | Section 9 (outcome-attribution vs agency-attribution); Section 10 (motor-onset vs decision-event) |
| Constructed-order decisions target not-I structures | Section 8 (manipulation, leadership, institutional variations); Section 9 (constructed-order accountability) |
| Decision-quality, decision-freedom, decision-responsibility are distinct | Section 9 (responsibility along source-compromise continuum and developmental-window) |

Section 7 therefore completes the transition from effort to selection. The I does not merely construct options or exert direction through them; it can resolve contrastive live-option spaces into selected courses, with or without explicit deliberation, with or without immediate source-access, and across both foundational and constructed orders. The selection-event is the operator-bundle's commitment, and the apparatus through which it can be analyzed includes Mode B reflective availability with order-asymmetric object-domain access, the $A/\phi$ structure of source-availability, and the structural separations among decision, trying, action, and outcome.

| Candidate marker | What it tracks |
|---|---|
| Deliberation duration | Thick vs thin deliberation distinction |
| Decision-latency (option-onset to selection) | Option-processing depth and selection-readiness |
| Mode B exercise vs Mode B availability | Explicit reflection during selection vs counterfactual reflective-access capacity |
| Order-specific Mode B latency | Implementation-chain bandwidth effects on object-domain availability |
| Post-hoc $\phi$-construction delay | Source-recognition lag (closely related to affect paper §3.3 recognition-lag) |
| Decision-quality / decision-freedom dissociation | Strategic success under source-compromise; free-but-foolish vs manipulated-but-intelligent configurations |
| Skeleton-specificity | Degree of course-resolution at the moment of selection |
| Order-of-target distribution across decisions | Foundational vs constructed-order decision frequencies and their developmental trajectory |


---

# 8. Variations and pathologies of agency: failures, contractions, captures, and compounds

Section 8 develops the full variation taxonomy. Section 3 defined free choice proper as the canonical case where all six conditions hold. Section 8 asks what happens when the structure is modified — when conditions fail, weaken, are bypassed or captured, when option-spaces contract, when source-status is compromised, when ownership-integration breaks down, when Mode B object-domains become unavailable, when implementation-pathways gap, when cascade-effects dominate, when affect modulates evaluation and selection. The variations are not random examples; they are generated by changing architectural parameters the prior sections established.

The section's controlling thesis:

> *Agency variations are structurally classifiable by how they modify, thin, damage, bypass, or compound the six conditions of free choice across order-domain, toolkit status, substrate coupling, Mode B availability, ownership-integration, source-status, and developmental window.*

Section 8 *classifies* agency-configurations. Section 9 will *attribute* responsibility, accountability, and ownership using the structures Section 8 identifies. The boundary is firm: Section 8 says what kind of agency-configuration is present; Section 9 says what follows for responsibility-attribution given that configuration plus the developmental-window overlay (4.10) and the source-compromise continuum (5.9). The clinical and philosophical literature often conflates these questions; the architecture's discipline keeps them separate.

## 8.1 From free choice to agency-variation

The methodological move that organizes Section 8: free choice is the canonical case, and the rest of agency is derived by structural variation. This matches the paper's stated methodological note (Section 3) — the architecture's claim is that free choice is a real inside-perspective architectural configuration, and other agency-configurations are specifiable by which architectural parameters depart from that configuration.

| Section | Owns |
|---|---|
| Section 5 | What options are live; verification-toolkit; live-option construction lemma |
| Section 6 | Effort, trying, resistance taxonomy, effort-economy across strategies |
| Section 7 | Decision-events, deliberation, Mode B reflective availability and asymmetry |
| Section 8 | Variation taxonomy: classifying agency-configurations by departure from free choice proper |
| Section 9 | Responsibility-attribution along the source-compromise continuum and developmental-window overlay |
| Section 10 | Empirical interface — Libet, Wegner, Soon, and related paradigms |

The variations are organized by *family*, not by condition. The condition-failure dimension is one axis among ten in the diagnostic schema (8.2); each variation-family is a recognizable cluster (akrasia, compulsion, ADHD-like, learned helplessness, etc.) whose architectural signature is read off the diagnostic schema. The variation-family organization is more legible than condition-by-condition because it lets each family's distinctive structural signature surface — akrasia and compulsion can both involve conflict around implementation, priority, or substrate pull, but compulsion is the Condition 4 capture/preemption/bypass case while akrasia is, by default, evaluative / $\Pi$ / selection misalignment without Condition 4 failure. Their structural signatures differ at every axis, and the differences matter for Sections 9 and 10.

## 8.2 Variation axes and diagnostic schema

This is the section's load-bearing apparatus. Every variation in 8.3–8.19 is read against the same ten-axis diagnostic schema. The schema does not require all axes to be specified for every variation — many variations are characterized by only a few axes — but the apparatus stays the same.

| Axis | Diagnostic question |
|---|---|
| 1. Live-option status | Is $\mathcal{O}_{m,t;d}$ intact, contracted, poisoned, fuzzy, or absent? |
| 2. Condition profile | Which of the six free-choice conditions hold, are thin, fail, or are bypassed? |
| 3. Decision-event status | Was there an operator-bundle selection-event? Is the selection minimal, free-choice-proper, apparent, or degraded (per 7.3 taxonomy)? |
| 4. Order profile | Which foundational orders (1–3) and constructed orders ($n \geq 4$) are active, impaired, or absent? |
| 5. Effort profile | What resistance-source dominates (per 6.4 eight-source taxonomy)? Is effort consumed productively, exhausted, or collapsed before forming? |
| 6. Mode B object-domain availability | Per 7.6: which agency-structures can the I take as object reflectively, and which are unavailable, conscious-fuzzy, or only post-hoc accessible? |
| 7. Source-status | Per 5.9: source-clean, scaffolded, source-compromised, poisoned, osmotically shaped, coerced? |
| 8. Ownership-status | Integrated as mine, alien, dissociated, merely narrated, conflicted, or imposed? (Condition 6) |
| 9. Developmental window | Per 4.10: pre-agential, immature, mature, scaffold-captured, trauma-shaped? *Note: developmental-window status is a Section 9 responsibility-overlay axis, not itself a Section 8 variation classifier — it conditions how the variation maps to responsibility-attribution but does not change the variation's structural identity.* |
| 10. Cascade profile | Per 5.6 / 6.11: are downstream effects direct, indirect, anticipated, unmanaged, or repairable? Are cascade-effects part of the variation's perpetuation? |

Two architectural commitments follow from the schema.

*The schema is the diagnostic apparatus, not a list of axes a variation must score on.* Some variations (akrasia) are sharply specified by axes 2, 3, 7, 8; others (manipulation under-recognition) by axes 1, 7, 6; others (ADHD-like) by axes 4, 5, 6, 9. The schema's role is to give each variation a structurally specifiable signature, not to require uniform reporting across all ten axes for every case.

*Developmental-window status (axis 9) belongs in the schema as a flag, not as a variation classifier.* This is a discipline boundary with Section 9. A pre-agentially-imprinted habit-pattern and a mature-deliberatively-chosen habit-pattern may share the same Section 8 variation-classification (habitual-chosen action, per 8.7) while differing at the developmental-window axis — and the difference matters for Section 9's responsibility-attribution but does not constitute a different variation in the structural sense. The schema flags developmental-window for downstream attribution while keeping Section 8's classification work clean.

## 8.3 Thin agency and reduced agency

Section 8 begins with mild variations before severe pathologies, to prevent the variation taxonomy from becoming a list of dysfunctions.

**Thin free selection.** The basic configuration where Condition 1 (contrastive option-space) and Condition 3 (operator-bundle selection) hold but Condition 2 (evaluative engagement) is minimal or implicit. Examples: the arbitrary button press, the routine path-selection on an unimportant fork, the choice between two indistinguishably-pleasant beverages, a low-stakes routine purchase where the alternatives are both live, evaluable, and not source-compromised. (An apparent impulse-buy counts as thin free selection only when salience capture, reward capture, or source-compromise are not doing the load-bearing work; many such cases belong to 8.8 substrate-capture or 8.15 manipulation rather than to thin agency.) The architecture's discipline:

> *Thin agency is not illusion. It is agency with low evaluative depth. It is genuinely a selection-event with operator-bundle commitment; it differs from free choice proper in that evaluative engagement does not carry the same weight in the configuration.*

Diagnostic signature:

| Axis | Status |
|---|---|
| Live-option status | Present, may be coarse |
| Condition profile | C1, C3, C5, C6 typically intact; C2 minimal |
| Decision-event | Genuine operator-bundle selection |
| Mode B availability | Available though typically not exercised |
| Ownership-status | Integrated |

This is the right place to set up Section 10's Libet/Soon analysis: the experimental paradigms that test "free choice" through arbitrary motor selection often probe thin free selection rather than free choice proper. Section 8.3 establishes that this is not a deficient or illusory form of agency but a structurally specifiable lower-tier configuration.

**Reduced agency.** A broader category for cases where one or more conditions are weakened but not absent. Time-pressure, fatigue, partial source-opacity, low-resolution fuzzy course-skeletons, distraction, mild affect-loading. The architecture does not call these pathological by default — they are ordinary contractions of agency that occur regularly in mature agents under normal conditions and do not by themselves indicate dysfunction. Reduced agency is the configuration in which agency is real but somewhat constrained relative to optimal conditions.

## 8.4 Constrained, forced, and coerced choice

Three configurations the literature often conflates.

| Configuration | Structural form |
|---|---|
| **Constrained choice** | $\mathcal{O}_{m,t;d}$ is reduced (fewer live options) but multiple live options remain. The agent selects among the available options; freedom is constrained but present. |
| **Forced choice** | $\mathcal{O}_{m,t;d}$ has only one live implementable course; alternatives are not constructible as live (whether through external constraints, substrate state, or toolkit limitation). The "selection" is structurally degenerate — there is nothing to select among. |
| **Coerced choice** | $\mathcal{O}_{m,t;d}$ is contracted or poisoned by inter-I, institutional, or other-not-I pressure; live alternatives may be present but their evaluative weighting is altered by threat-projection or other coercion-mechanisms. |

> *("Structurally degenerate" here has its ordinary technical sense: the option-set has collapsed to a single element, so there is nothing to select among. It is **not** a claim that describing choice as selection-from-a-set is itself degenerate — that macroscopic description is valid, and is recovered as a filter-quotient in* Choice as Endogenous Filter Application*.)*

The key distinction:

> *Coercion is not merely constraint. Coercion is inter-I, institutional, or environmental source-pressure that alters live-option construction, $\Pi$-ranking, threat-projection, or implementation availability — it modifies the agency-configuration rather than merely reducing the option-set.*

Examples:

| Case | Classification |
|---|---|
| "Choose between two acceptable options" | Mild constrained choice |
| "Choose between two bad options" | Constrained choice with negative live-option space |
| "Sign or be killed" | Coercive constrained choice — option-space is contracted by threat |
| "No alternative is constructible as live from inside" | Forced choice — structurally degenerate selection |
| "Comply under threat while still selecting survival path" | Coerced choice with intact ownership but compromised live-option space |
| "Refusal is technically live but punishable" | Coerced choice with omissive option still live but $\Pi$-cost-elevated |

The apparent-I / other-I apparatus (4.11) and the manipulation continuum (5.9) are relevant here, but accountability questions (whether and how reduced freedom reduces responsibility) belong to Section 9. Section 8 classifies the configuration; Section 9 maps it to attribution.

## 8.5 Omission, withholding, refusal, and veto

This subsection is essential because veto and withholding are central to free-will debates, and Section 7.8 already established the omissive-decision class. Section 8.5 develops the variation-family.

The architectural claim:

> *Non-action is agency only when non-action is live and selected.*

Cases:

| Case | Structure |
|---|---|
| **Withholding** | Live non-action selected as course; operator-bundle commits to not-acting |
| **Refusal** | Mode A / PtCns / $\Pi$ structure differentiates against a proposed action; selection is a refusal-act |
| **Strategic delay** | Selected temporal non-action; the operator-bundle commits to acting later, not to not-acting |
| **Veto** | Operator-bundle interrupts or withholds implementation of a forming action — Libet's veto cases when they are genuine |
| **Omissive decision under coercion** | Refusal as an omissive decision under coercive pressure; live but Π-cost-elevated |
| **Drift / inaction** | No selection; passive trajectory; the agent neither acts nor decides not to act |
| **Collapse** | Failure to select under overload; not refusal; structurally a deliberation-without-decision case (8.10) |

> **Note on table phrasing.** Where the cells above reference "Mode A," "PtCns," or "$\Pi$ structure," these are *response-types* and *architectural objects active in the configuration*, not predictive operators that determine which row obtains in a given encounter. The architecture does not predict per-encounter mode-selection (Foundation File 2 §4.1, §4.5); the table classifies the structural signatures that obtain *when* a given response is the response that occurs, not the conditions under which one row rather than another will be the actual outcome. The same convention applies to all variation-family tables in §8.

The diagnostic line: an omissive decision satisfies Condition 3 (operator-bundle selection) with the selected course being non-action; drift and collapse fail Condition 3 because no operator-bundle selection occurred. The four-way separation of 7.10 is critical here: an omissive decision that succeeds (the agent does refrain) and a non-decision that happens to result in non-action have very different structural signatures and very different responsibility-attribution implications.

This subsection also handles passive omissions (failing to act on an option that was live) versus active omissions (refusing the option). The architecture distinguishes them by whether the operator-bundle engaged with the omissive course as a selected option versus failing to engage at all.

## 8.6 Akrasia and weakness of will

Akrasia must not be collapsed into compulsion (Condition 4 substrate capture). Akrasia is its own family.

> *Akrasia is a configuration in which evaluative endorsement, $\Pi$-ranking, operator-bundle selection, and implementation pull are misaligned, while agency is not fully bypassed.*

Akrasia subtypes:

| Subtype | Structural form |
|---|---|
| **Evaluative akrasia** | PtCns evaluation endorses A; operator-bundle selection goes toward B. Mode B may recognize the divergence in real time or after the fact |
| **$\Pi$-akrasia** | Long-term preservation-priority ranking favors A; immediate $\Pi$-weighting under salience or affect favors B. Selection follows immediate $\Pi$ |
| **Substrate-assisted akrasia** | Substrate pull biases toward B without fully capturing; the operator-bundle selects B partly under substrate-assistance, but Condition 4 is not violated — the selection remains operator-bundle-mediated |
| **Reflective akrasia** | Mode B engages with the conflict during deliberation but cannot stabilize alignment between evaluation and selection |
| **Configurational akrasia** | Past configurational willing arranged conditions that now produce akratic action — the agent earlier set up environments or commitments that now make B easier than A |
| **Constructed-order akrasia** | Public-face selection (in a meeting, a relationship, an institutional role) diverges from private evaluation; the agent agrees to a plan they privately oppose |

The crucial guardrail (per v0.1.6.1 patch #23):

> *Akrasia is not Condition 4 failure by default. Condition 4 is compromised only where substrate capture, preemption, or bypass removes genuine operator-bundle selection. In most akrasia, the operator-bundle selects against endorsement — Condition 3 is exercised but produces an outcome at variance with the evaluation that should have shaped it.*

The distinction matters because Section 9's responsibility-attribution treats akrasia and compulsion very differently. Akratic action is the agent's act in the strong sense (the operator-bundle selected); compulsive action is constrained at Condition 4 (the operator-bundle was preempted). Both involve diminished freedom, but the architectural signature is different.

## 8.7 Habitual action: chosen, automatic, compulsive, skilled

Habit is a family with several architecturally distinct sub-configurations. Section 6.8's distinction table is the basis; Section 8.7 extends it for the variation taxonomy.

| Habit type | Structure |
|---|---|
| **Chosen habit** | Upstream free choice or configurational willing created the pattern; current execution is agency-thin but intact (operator-bundle engagement minimal but present) |
| **Automatic habit** | Local operator-bundle engagement is thin or absent; action proceeds through trained substrate-pathway without Condition 3 exercise; agency-status borderline or absent in the moment |
| **Compulsive habit** | Substrate capture, source-compromise, or both drive recurrence against opposition; Condition 4 violated through preemption; high-effort resistance may fail |
| **Skilled habit / mastered-domain action** | Mastery has compressed construction; low effort, high integration, Mode B available though not exercised; free-choice-compatible |

The five markers from Section 6.8 distinguish chosen-habit from compulsive-habit (with substrate-coupling/preemption as the load-bearing discriminator per v0.1.5.2 patch #19):

| Marker | Chosen | Compulsive |
|---|---|---|
| Interruptibility | Generally interruptible under Mode B access | Resistant to interruption even under explicit reflective opposition |
| $\Pi$-alignment | Aligned with endorsed priorities | Captures priority against endorsement |
| Source-status | Self-curated or accepted | Substrate-driven, source-compromised, or pre-agentially imprinted |
| Ownership-integration | Integrated as chosen pattern | Felt alien, pressured, or regretted |
| Substrate-coupling/preemption | Trained implementation supporting bundle | Capture / bypass / preemption — Condition 4 violation |

*Self-perpetuating loops within habit.* Section 5.6's output-imprinting cascade gives habit a temporal-structural dimension: a chosen-habit can become a self-perpetuating loop where the agent's third-order action imprints on substrate (Stage 1) and feeds back as input that supports further repetition (Stage 3). Healthy contemplative practice, exercise routines, and study habits are cascade-topologically-identical to maladaptive loops (rumination patterns, addictive consumption, anxiety-driven checking) — what differentiates them is source-status, $\Pi$-alignment, PtCns coherence, ownership-integration, and substrate-coupling status, not the cascade-topology itself.

*Configurational over-scaffolding* is a strategy-specific habit pathology where the agent's configurational willing produces such tight self-curation that the toolkit's range of live options narrows over time — the agent has configured their environment to make the chosen pattern frictionless but at the cost of brittleness when novel conditions arise. Section 5.9's note on configurational willing's relation to manipulation applies: configurational over-scaffolding can be autonomy-supporting (the agent's bundle-mediated arranging is source-clean) or autonomy-undermining (the arranging-act inherits source-compromise from prior conditions). The variation classifier is the same; the source-status overlay differs.

## 8.8 Compulsion, addiction, and substrate capture

Compulsion is one of the most important variation-families because it is frequently confused with bad habit, akrasia, weakness of will, and source-compromise.

> *Compulsion is agency-impairment through substrate capture, bypass, or preemption — Condition 4 violated through substrate dynamics that preempt operator-bundle engagement, with Mode B often able to object to the act while the relevant action-domain remains unavailable or only partially available to operator-bundle control under current conditions.*

Diagnostic signature:

| Axis | Compulsion profile |
|---|---|
| Live-option status | Alternatives may be representable but not live under the capture-state |
| Condition 4 | Compromised by substrate capture / bypass / preemption |
| Mode B general reflection | Often present and articulate |
| Mode B object-domain (specific to capture) | The action-capture domain is unavailable to Mode B alteration even when Mode B can reflectively recognize the act as unwanted (per 7.6 asymmetry) |
| Ownership-status | Often conflicted ("I did it but not as I endorse myself") |
| $\Pi$-status | Captured by near-term relief, reward, or threat-reduction |
| Effort | High resistance-effort may fail; effort-economy degraded |

*Addiction* is typically a third-order-primary substrate capture (reward / craving substrate dynamics dominating motor and consumption pathways) with first-order attentional capture (salience locked to the addiction-relevant content), second-order rationalization or $\phi$-distortion (constructed reasons that track the capture rather than the agent's actual selection-process), and self-cluster shame/guilt compounds:

| Axis | Addiction profile |
|---|---|
| Live-option status | Alternatives represented but not live under craving-state |
| $\Pi$-status | Distorted priority toward addictive content |
| PtCns | Often conflict before/after action; coherence with self-frame disrupted |
| Mode B | May recognize the pattern reliably but not control the capture-domain through reflection alone |
| Ownership-status | Mixed — "I did it" but "not as I endorse myself" |
| Source-status | Developmental, osmotic, trauma-shaped, substrate-shaped, or habit-shaped — varies by case |
| Cascade-profile | Self-perpetuating loop — Stage 3 closure feeds craving substrate, supporting further capture |

The architecture does not reduce addiction to pleasure-seeking. Reward-substrate capture is one mechanism; threat-reduction (avoidance of withdrawal, anxiety, or affective dysregulation) is another; trauma-state regulation through the addictive content is another. Section 8 classifies the configuration; clinical specifics belong elsewhere.

*Direct-willing depletion* is a strategy-specific compulsion-adjacent pathology: the agent attempts direct willing repeatedly against the capture, exhausts effort-economy without overcoming the substrate dynamics, and may collapse into either passive submission to the capture or extended periods of disengagement that the agent later regrets. The architecture's reading is that direct willing is structurally insufficient against substrate capture in many compulsion configurations; configurational willing (arranging environments, removing access, restructuring routines), slingshot willing (using opportune moments of reduced craving), and constructed-order willing (engaging external accountability structures) often have proportionally favorable effort-economy. Section 8 establishes this at the variation level; therapy and recovery-architecture material belongs to other sections.

## 8.9 ADHD-like dynamic-refinement and implementation-gap configurations

The architecture's commitment from 5.4, 5.6, 5.8, 6.10, 7.6 (with the v0.1.6.1 patch #14 ADHD overclaim softening) consolidates here as a dedicated variation-family.

> *ADHD-like agency impairment is a substrate-developmental constraint on sustained operator-bundle mediation at orders 1 and 2, often with third-order arousal/reward compounds. The toolkit may represent, evaluate, and inhabit the option; what fails is sustained implementation of operator-bundle direction over time, particularly the dynamic-refinement-during-execution that fuzzy live-options depend on.*

Live-option sub-condition profile:

| Sub-condition | ADHD-like profile |
|---|---|
| Representability | Often intact; the toolkit constructs the course at skeleton-level resolution |
| Evaluability | Often intact; the agent evaluates the option as worth pursuing |
| Inhabitability | Often intact; the agent can imagine being the one who does this |
| Implementability | Unstable over duration; substrate cannot reliably sustain operator-bundle direction through the dynamic-refinement process |

Variation subtypes:

| Subtype | Structure |
|---|---|
| **Initiation gap** | Course is live; second-order or third-order initiation fails — the agent intends, plans, even decides, but the substrate does not produce the initiating action |
| **Persistence gap** | Course begins but cannot be sustained — attention drifts, action stalls, the agent re-engages repeatedly with diminishing returns |
| **Task-switching gap** | Selected course cannot be re-entered after interruption; what was an active live-option becomes refractory |
| **Dynamic-refinement gap** | Skeleton selected but the toolkit cannot reliably construct the next executable detail under current substrate conditions |
| **Reward / salience capture** | Immediate cues capture priority against the endorsed course; the operator-bundle is pulled by salience rather than directing focus |
| **Scaffolded agency** | Configurational willing creates external supports (timers, environment-curation, accountability-structures) that make the course sustainably live; mature ADHD-strategies frequently take this form |

*The Mode B asymmetry from 7.6 in ADHD-like configurations.* The substrate-developmental gap may be partially reflectively available — many ADHD agents articulate the gap with notable phenomenological insight — but the gap cannot be overcome by Mode B reflection alone. The asymmetry is between phenomenological-availability of the gap (often present) and reflective-overcoming of the gap (absent under Mode B alone). This is structurally distinct from compulsion: compulsion involves substrate capture pulling toward an unwanted action; ADHD-like involves substrate not sustaining the wanted action.

The architecture treats ADHD-like as one structural profile of executive-function constraint, not a complete clinical theory. The architectural mapping is to the substrate-developmental implementation-gap pattern at orders 1 and 2 with the dynamic-refinement-during-execution sharpening; the clinical literature's full account of ADHD includes additional dimensions the architecture does not engage.

## 8.10 Deliberation-pathologies: paralysis, rumination, indecision, procrastination

Section 7.8 established deliberation-without-decision as a class. Section 8.10 develops the variation-family.

**Decision paralysis.** Deliberation continues without selection because option-processing cannot resolve into operator-bundle commitment. Mechanisms:

- Too many live options; comparison cannot converge
- No stable $\Pi$-ranking; preservation-priorities remain in flux
- PtCns conflict; no option satisfies frame-coherence sufficient for commitment
- Source-compromised ambiguity; the agent cannot trust the option-space's source-status
- Fear of regret; counterfactual projection blocks selection-resolution
- Constructed-order stakes; the projected social or institutional consequences of any selection are too high

Diagnostic signature: Condition 1 intact, Condition 2 engaged, Condition 3 fails to exercise — the operator-bundle does not commit. Mode B may be available throughout the paralysis but unable to break the deliberation-loop.

**Rumination.** A second-order loop without selection, often affect-mediated or source-opaque:

| Deliberation | Rumination |
|---|---|
| Option-processing progresses toward selection | Loop repeats without resolution |
| Evaluates alternatives | Reactivates the same problem-space |
| May update $\Pi$, PtCns, projection-toolset state | Often destabilizes or repeats prior states |
| Can be terminated by selection | Often terminated only by exhaustion, distraction, or external interruption |

Rumination's cascade-profile (5.6) often produces self-perpetuating loops — the rumination Stage 1 imprints on substrate (rumination-state becomes substrate-supported), Stage 3 closes back as input (the rumination-state primes further rumination), and the loop perpetuates. This is cascade-topologically identical to contemplative deepening; what differs is source-status, $\Pi$-alignment, and PtCns coherence.

**Procrastination — multi-architectural decomposition.** Per the v0.1.6.1 patch #16 forward-flag from 7.8, procrastination is structurally mixed and configuration-dependent. Section 8.10 decomposes the cluster:

| Procrastination type | Architectural classification |
|---|---|
| Selected delay | Omissive decision toward strategic timing (per 8.5) |
| Configurational delay | Autonomy-supporting timing decision; preserved as legitimate slingshot |
| Avoidance collapse | Deliberation without decision under threat-projection; Condition 3 fails to exercise |
| Anxiety-driven loop | Threat-projection consumes option-processing; cognitive resistance dominates |
| ADHD-like initiation gap | Substrate-developmental constraint at orders 1–2 (per 8.9) |
| Self-deceptive delay | Source-compromised reframing of the situation; the agent's $\phi$-construction misrepresents the actual state of the option-space |
| Slingshot waiting | Genuine timing strategy if grounded in real gradient-reading |
| Learned helplessness delay | Projection-toolset returns no viable pathway (per 8.11) |

The architecture's reading is that procrastination is not a single variation but a cluster-name for several architecturally distinct configurations sharing a phenomenological surface. Section 8.10 distinguishes them; Section 9's responsibility-attribution will engage each subtype with the appropriate developmental-window and source-status overlays.

## 8.11 Learned helplessness and agency-collapse

The affect paper develops learned helplessness as a profile-shape disturbance of the projection-apparatus: the projection-toolset returns empty-pathway representations, leaving PCE-over-projection with no viable represented pathway. Section 8.11 specializes this for agency.

> *Learned helplessness is an agency-collapse configuration in which the projection / toolkit apparatus cannot construct viable live pathways even where external alternatives may exist. Effort collapses before trying-structure can form; selection cannot occur because no live option is constructed.*

Diagnostic signature:

| Axis | Learned helplessness profile |
|---|---|
| Representability | Possible options may not appear as possible — the toolkit's projection cannot construct them as live courses |
| Evaluability | Future options cannot be meaningfully compared; the projection-toolset returns flat or empty representations |
| Inhabitability | "I cannot be the one who does this"; the option-space contracts at the inhabitation step |
| Implementability | Experienced as absent even where it may be technically present |
| Decision-event | Often no decision-event; selection collapses before formation |
| Effort | May not begin, or collapses quickly; effort-economy is structurally compromised before resistance is encountered |
| Mode B | May know the concept of helplessness but cannot alter projection-output through reflection |

The architectural commitment:

> *Conceptual recognition of helplessness is not the same as repaired projection-toolset. The agent who knows they are in a helpless configuration may still face an agency-collapse configuration because the projection-toolset itself is what is damaged; the cognitive recognition does not by itself restore the toolkit's capacity to construct live pathways.*

This preserves the affect paper's discipline. Learned helplessness is not a mistaken belief that can be corrected by counter-evidence; it is a structural toolkit-state that requires repair through the toolkit-development mechanisms of 5.5, often supported by external scaffolding, therapeutic relationship, environmental change, or substrate intervention.

## 8.12 Depression, anxiety, shame, and affect-mediated agency contraction

Affect modulates agency through the resistance-modulator framing of 6.10 and the deliberation-modifier framing of 7.8. Section 8.12 organizes affect-mediated agency contractions as a variation-family without redoing the affect paper's taxonomy.

| Affect configuration | Agency effect |
|---|---|
| **Severe depression** | Multi-order action-space contraction: third-order somatic flattening, fatigue, anhedonia; second-order projection collapse (no future-state representations support selection); first-order narrowing (salience contraction); cogito/thought-partition disturbances may compromise Mode B reflective access (cf. affect paper self-cluster discussion of self-loathing / depression and Foundation File 4 severe-depression mechanism) |
| **Anxiety** | Threat-projection consumes option-processing; salience loops contract action-space; deliberation may continue but with threat-paths displacing goal-paths |
| **Shame** | PtCns resistance around an identity-bearing aspect or action: the option or content is sufficiently tied to the lived-I profile that exposure forces frame-evaluation, and inhabitability may collapse because the I cannot be the one who does this under the present frame |
| **Guilt** | May sharpen responsibility-relevant repair options (constructive guilt) or produce rumination loops (perseverative guilt); Section 9 develops the responsibility-side analysis |
| **Fear / dread** | Fear may select avoidance; dread may foreclose action-space at the projection step — projected futures contain only threat |
| **Hope** | Stabilizes viable pathway projection; supports operator-bundle commitment by maintaining represented future-states as live |
| **Pain / fatigue** | Substrate resistance; state-dependent toolkit contraction (5.4); the toolkit operates at reduced bandwidth |
| **Devotion / love** | Stabilizes $\Pi$-priority; reduces evaluative friction by aligning operator-bundle with frame-supported aims |
| **Joy / engagement** | Expands projection-toolset operation; more future-states become representable as live courses |

The discipline boundary: affect-mediated agency-contraction is the variation-family in which agency is structurally affected by affect-state without being eliminated. Severe depression with intact ownership and Mode B availability is a contraction-configuration, not an absence-configuration; the agent's diminished capacity for action-space construction is real and structurally specifiable, but the agent is still the one who acts (or fails to act) within the contracted configuration. Section 9 develops the responsibility-attribution along the developmental-window overlay; Section 10 engages the empirical literature on affect and decision.

## 8.13 Dissociation, alienated action, and ownership-integration failure

Condition 6 (ownership-integration) failure-family.

> *Alienated action occurs when action proceeds but ownership-integration fails or is disrupted — the I observes or experiences the action without integrating it as the I's own.*

Cases:

| Case | Decision? | Action? | Ownership? |
|---|---|---|---|
| Alien-hand-like movement | Maybe | Yes | Impaired (the moving hand is not integrated as mine) |
| Dissociative action | Maybe fragmented | Yes | Disrupted across orders |
| "I watched myself do it" reports | Yes (often) | Yes | Disrupted at the integrating step |
| Trauma-response action without ownership | Maybe automatic | Yes | Variable — may be fragmented or post-hoc partially recoverable |
| Possession-like attribution | Yes (within possession-frame) | Yes | Routed through the possessing agent rather than the I |
| Action integrated into a dissociated profile-region | Yes (within dissociated region) | Yes | Not integrated with current lived-I center |

Critical guardrail:

> *Alienated action is not the same as compulsion. Compulsion is substrate capture (Condition 4 violation); alienation is ownership-integration failure (Condition 6 violation). They can compound — substrate capture with ownership-disruption — but they are architecturally distinct, and Section 9's responsibility-attribution treats them differently.*

The architectural reading: in compulsion, the operator-bundle is preempted but the action remains the agent's act in the ownership-integration sense; in alienation, the operator-bundle may have selected but the action is not integrated as the I's. Severe configurations may compound both — the substrate-captured action that the agent then dissociates from to manage the conflict between the action and the agent's frame-coherence.

## 8.14 Apparent choice and confabulated agency

Section 7.9 established post-hoc recognition vs source-opacity vs confabulation; Section 8.14 develops the variation-family.

> *Apparent choice is the configuration in which the I has a narrative or felt authorship-state, but the actual selection-process was absent, bypassed, or differently structured.*

Cases:

| Case | Structure |
|---|---|
| Post-hoc narrative over reflex | Reflexive substrate-action narrated as if chosen |
| Wegner-style apparent mental causation | Felt authorship without operator-bundle selection |
| Externally cued action narrated as chosen | Salience or social cue produced action; subsequent narrative misattributes selection |
| Social pressure internalized as "my decision" | Coercive option-shaping rationalized as authentic choice |
| Source-compromised option-space later rationalized | Manipulated option-space's selection narrated with constructed reasons that miss the source-compromise |
| Confabulated source-construction over absent process | Mode B generates apparent-source where no source-pathway was actually engaged |

The three-way distinction from 7.9:

| Case | Structure |
|---|---|
| Post-hoc recognition | Real selection occurred; later $\phi$-construction reveals source-pathways that were operating but not articulable at the moment |
| Source-opacity | Real selection occurred; $\phi$ for the source-pathways is genuinely low or undefined; Mode B does not generate false $\phi$ to fill the gap |
| Confabulation | $\phi$-narrative supplies apparent source-access for a process that was absent, bypassed, or differently structured than the narrative reports |

Section 8.14 is critical for Section 10's empirical interface. Section 10 will need to distinguish Wegner-paradigm cases that demonstrate apparent choice / confabulation from cases that demonstrate post-hoc recognition or source-opacity — the architecture's discipline is that these are structurally distinct configurations even when their phenomenological surface is similar.

## 8.15 Manipulation, source-compromise, and scaffold-captured agency

Section 5.9's source-compromise continuum specializes into a major variation-family.

> *Manipulated agency may satisfy many internal choice-conditions while the option-space, salience field, evaluative apparatus, or toolkit-input has been externally engineered.*

Manipulation types:

| Type | Structure |
|---|---|
| **Acute manipulation** | Local option-space poisoning — specific input-content for the present choice is shaped by the manipulator |
| **Deception** | False content alters representability or evaluability; the agent constructs live options based on misrepresented states of affairs |
| **Salience manipulation** | First-order capture engineered through environmental or attentional design — the agent's attention is directed by the manipulator's structuring of the stimulus field |
| **Emotional manipulation** | Affective configuration is altered to shift $\Pi$, PtCns, or source-access — the agent's evaluative apparatus operates on emotionally distorted contents |
| **Propaganda** | Osmotic long-term toolkit shaping; the agent's verification-tools and option-construction-tools were formed under the manipulator's input |
| **Indoctrination** | Developmentally source-compromised toolkit formation; pre-agential or developmental-window-active period exposure shapes the toolkit before agency is fully available |
| **Exhaustively scaffolded choice** | Option-space appears internal but is externally structured — the cult, total institution, or comprehensive ideological system that has shaped every dimension of the agent's evaluative apparatus |
| **Self-curation under prior compromise** | The agent arranges future input via configurational willing, but the arranging-act itself is performed under prior source-compromise (5.9 caveat) — the autonomy-supporting structure of self-curation is itself compromised |

The critical architectural commitment:

> *Manipulation is not ownership failure by default. The agent may own the decision from inside (Condition 6 intact) while sourcehood is compromised from outside (source-status compromised). The two are dissociable — and the dissociation is what makes manipulation philosophically and ethically difficult.*

The apparent-I / not-I apparatus (4.11): the manipulator is a constructed-order agent (acting at fourth or higher order through bundle-mediated will-acts toward the manipulated agent's option-space); the manipulated agent receives Stage 2 cascade outputs as input (per 5.6); the manipulated agent's apparent-I construction (their representation of who they are and what they're choosing) can be poisoned by the manipulator's input-shaping without the manipulated agent's Mode B detecting the source-compromise. This sets up Section 9's most difficult case: the agent whose action is responsibility-relevant because the internal agency conditions are mostly met (the action is structurally owned and internal-agency-complete in many respects) while sourcehood is externally compromised by another agent's deliberate action. Section 8 does not assign responsibility; it identifies the structural configuration. Section 9 will engage the responsibility-attribution question.

## 8.16 Constructed-order variations: leadership, institutional action, over-extension, manipulation

Variation above foundational orders.

| Variation | Structure |
|---|---|
| **Constructed-order competence** | The agent can target not-I structures effectively; mastery within the constructed order |
| **Constructed-order over-extension** | The agent believes they can direct a not-I structure beyond toolkit capacity; the variance-envelope is exhausted (per v0.1.5.2 patch #6) |
| **Leadership agency** | Coordination over group option-space; can be autonomy-supporting or autonomy-undermining depending on source-status |
| **Institutional agency** | Willing through formal roles, procedures, rules; the institution's structure carries part of the constructed-order action |
| **Bureaucratic capture** | The institutional pathway constrains, sequences, and prioritizes the agent's live options, so the agent's selection occurs within an externally structured option-space; the agent acts through the institution but with $\mathcal{O}_{m,t;d}$ shaped by institutional structuring |
| **Teaching / therapy / coaching** | Constructed-order action shaping another agent's toolkit; autonomy-supporting when it develops the recipient's toolkit in relation to the recipient's own aims or therapeutic / developmental goods, with transparency, alternatives, and non-poisoned source-access; manipulative when input-shaping serves the instructor / therapist / coach's aims while obscuring source-status, suppressing alternatives, or compromising the recipient's verification capacity. The ethical / source-status classification depends on transparency, alternatives, recipient aims, and source-access — not on the constructed-order classification itself |
| **Constructed-order manipulation** | Source-compromised direction of another agent's toolkit-development or option-space construction |

The membership-test reminder (per v0.1.5.2 patch #5):

> *Constructed-order agency is not mere lower-order motor action with social effects. The target must be the not-I coordination structure as such — the asking-protocol, the team-coordination structure, the institutional protocol, the teaching-relationship — implemented through lower-order action with sufficient trained-expectation grounding for fuzzy lower-order availability.*

The order-classification examples:

| Act | Classification |
|---|---|
| Mechanically saying words | Third-order vocal action |
| Requesting help as a request-protocol | Fourth-order social-protocol decision |
| Coordinating a team | Fifth-order group-coordination decision |
| Filing a legal motion through institutional procedure | Institutional-order decision |
| Designing organizational policy | High constructed-order decision |

Each constructed-order variation can be autonomy-supporting or autonomy-undermining; the moral distinction is at source-status (per 5.9), not at order-level.

## 8.17 Skilled flow, mastery, and low-effort agency

This subsection prevents over-pathologizing low effort, building on Section 6.8 and 7.5.

| Case | Structure |
|---|---|
| **Mastered-domain selection** | Low-friction operator-bundle selection within mastered envelope |
| **Flow** | High integration, low explicit Mode B exercise during action; Mode B available under intact post-action conditions |
| **Automaticity** | Low engagement; agency-status borderline or thin; substrate-pathway dominant with weak operator-bundle engagement |
| **Capture** | Low or high effort, but substrate or source dominates — Condition 4 violation |
| **Source-compromised mastery** | Efficient but autonomy-impaired; the mastered toolkit serves source-compromised aims |

The architectural commitment, repeating from 6.8 and 7.5:

> *Low effort is not non-agency. It must be read with source-status, ownership-integration, $\Pi$-relation, substrate-coupling/preemption, and Mode B availability. The same low-effort phenomenology can be mastery, automaticity, capture, source-compromised mastery, or transient unavailability of high-effort engagement — these are architecturally distinct configurations with different responsibility-attribution and clinical implications.*

*Mastered-domain automaticity drift* is a strategy-specific pathology where the agent's mastery-compressed willing within a domain becomes thin enough to drift toward agency-thin automaticity. The grandmaster who plays through familiar positions without genuine engagement; the experienced surgeon who proceeds through routine cases on autopilot; the expert speaker who delivers the same speech with diminishing presence. The variation is from skilled free action toward automaticity, with the substrate-coupling/preemption marker being load-bearing — when substrate-coupling shifts from supporting bundle-engagement to preempting it, the configuration shifts from mastered-domain free action to substrate-driven automaticity.

## 8.18 Reflexive action and non-agency boundary cases

Some events in the I's body are not agency-events. The architecture's lawful-frame and substrate discipline apply.

| Case | Classification |
|---|---|
| Reflex withdrawal (e.g., from heat) | Non-agency; substrate-pathway action without operator-bundle mediation |
| Startle response | Substrate event; may become agency-relevant if followed by selection (the startled agent who then chooses to investigate) |
| Autonomic adjustment | Non-agency unless toolset-mediation makes it live (per 4.4 guardrail — breath-pacing, biofeedback, somatic practice) |
| Salience capture without subsequent selection | Input event; not agency |
| Osmotic imprinting | Profile / toolkit shaping; not a will-act |
| Passive drift | Trajectory without selection; not agency |
| Sleepwalking, seizure-like action | Substrate-pathway action; not free choice |
| Body-language responses to social cues | Often non-agency at the moment of response; agency may apply at the higher-level configuration of being-in-this-conversation |

The architecture's discipline:

> *Not every event in the I's body is agency. The variation taxonomy of 8.3–8.17 develops configurations of agency; 8.18 marks the boundary where agency itself is not the right category.*

This boundary matters for Section 9 (responsibility cannot attach to non-agency events except through configurational willing that arranged the substrate-conditions) and for Section 10 (experimental paradigms that probe substrate-event timing may be probing non-agency events that the architecture will not classify as decision-events at all).

## 8.19 Compound agency configurations

Most clinically and philosophically interesting cases are compounds. Section 8.19 provides the compositional schema.

> *A compound agency configuration is a variation in which multiple failure-modes, orders, source-statuses, or ownership-conditions interact over the same action-space.*

The compositional schema (compressed from the 8.2 ten-axis schema):

1. Affected order-domain
2. Live-option failure mode
3. Decision-event status
4. Effort/resistance profile
5. Mode B object-domain availability
6. Source-status
7. Ownership-integration
8. Developmental-window flag
9. Cascade profile

Examples that exercise the compositional apparatus:

| Compound | Components |
|---|---|
| **Akratic procrastination** | $\Pi$-conflict (8.6) + avoidance collapse (8.10) + delayed decision (8.5) |
| **ADHD-anxiety task collapse** | Implementation gap (8.9) + threat-projection (8.12) + salience capture |
| **Addiction-shame loop** | Substrate capture (8.8) + self-cluster PtCns resistance (8.12) + cascade loop (5.6) |
| **Manipulated wholeheartedness** | Ownership-integration intact (Condition 6) + source-compromised option-space (8.15) — the agent whole-heartedly chooses what was engineered for them |
| **Dissociated compulsion** | Substrate capture (8.8) + ownership-integration failure (8.13) — the action is both captured and dissociated from |
| **Depression-learned helplessness** | Projection-collapse (8.11) + third-order flattening (8.12) + effort-collapse before trying-formation |
| **Skilled immoral manipulation** | Constructed-order mastery (8.16) + source-compromised aim (5.9) — the configuration where the manipulator's effort-economy is favorable but the work is autonomy-undermining |
| **Coerced prudent compliance** | Constrained live-options (8.4) + survival rationality + reduced freedom — high decision-quality within compromised configuration |
| **Trauma-cue activation** | Multi-order: third-order substrate-readiness + second-order asymmetric threat-projection + first-order focus-capture + ownership-integration variability |
| **Severe depression with intact Mode B** | Multi-order projection collapse + cogito/thought-partition disturbance (cf. affect paper self-cluster discussion of self-loathing / depression and Foundation File 4 severe-depression mechanism) + Mode B available but incapable of altering projection-output through reflection alone |
| **Configurational over-scaffolding under prior compromise** | Self-curation (5.9) + source-compromised arranging-act (8.15) — the agent's apparent-autonomous environment-design is itself manipulated |
| **Habitual-chosen pattern transitioning to habitual-compulsive** | Cascade-perpetuation (5.6) + substrate-coupling shift from supporting to preempting (Condition 4 progressive failure) — the structural transition that turns a freely chosen pattern into a captured pattern |

The compound-configuration apparatus is what makes Section 8 useful for clinical and applied contexts: most actual cases are not pure variations but configurations of multiple variations interacting. The architecture's discipline is that compounds are specifiable through the same diagnostic schema, with the compositional structure surfacing how the components interact.

## 8.20 Summary: variation taxonomy

Section 8 has developed the variation taxonomy as a structurally specifiable apparatus. The taxonomy organizes around variation-families with the ten-axis diagnostic schema providing the architectural reading of each variation:

| Variation family | Core structural issue |
|---|---|
| Thin agency / reduced agency | Low evaluative depth; mild contraction not pathology |
| Constrained / forced / coerced choice | Contracted or pressured option-space; coercion alters agency-configuration not just option-set |
| Omission / withholding / refusal / veto | Non-action selected as live (omissive decision) vs non-selection (drift, collapse) |
| Akrasia | Evaluative / $\Pi$ / selection misalignment without Condition 4 failure (default) |
| Habitual action | Repeated pattern with variable ownership / source / capture; substrate-coupling / preemption is load-bearing discriminator |
| Compulsion / addiction | Substrate capture; Condition 4 violation; Mode B may object while the capture-domain remains unavailable or only partially available to operator-bundle control under current conditions |
| ADHD-like configurations | Substrate-developmental constraint on operator-bundle-mediation at orders 1–2; dynamic-refinement-during-execution gap |
| Deliberation-pathologies | Option-processing without selection; paralysis, rumination, indecision, multi-typed procrastination |
| Learned helplessness | Projection-toolset collapse; conceptual recognition does not repair the toolkit |
| Affect-mediated contraction | Affect alters $\Pi$, source-access, substrate, salience, projection-toolset |
| Dissociation / alienation | Ownership-integration failure (Condition 6) — distinct from compulsion |
| Apparent choice / confabulation | False source-construction over absent or differently-structured selection-process |
| Manipulation / source-compromise | Source-compromised option-space, evaluative apparatus, or toolkit-input — distinct from ownership-failure |
| Constructed-order variations | Not-I structure targeting succeeds, fails, or corrupts; moral status at source-status not order |
| Skilled flow / mastery | Low-effort agency or automaticity depending on source-status, ownership, substrate-coupling, Mode B |
| Reflex / non-agency | Substrate events that are not selection-events; boundary of the variation taxonomy |
| Compound configurations | Multi-axis composition; most clinically and philosophically interesting cases |

The single most important structural point: *most clinically and philosophically interesting cases are compounds of multiple variations*. The compositional schema of 8.19 lets the architecture handle real cases without losing the taxonomy.


---


---

# 9. Responsibility-attribution: ownership, sourcehood, accountability, and cascade

Section 9 develops the triadic responsibility-attribution apparatus that the variation taxonomy of Section 8 supplies the structural inputs for. The architecture's central commitment is that responsibility, ownership, and accountability are dissociable structural relations rather than facets of a single property: an act may be owned without being source-clean; source-clean without being under accountability-relevant conditions; accountable for explanation but not for repair. The triadic dissociation, the source-status overlay, the developmental-window overlay, the cascade-attribution test, and profile-indexed (rather than zero-sum) attribution are developed across §9.1 through §9.16.

> *Three subsections of the original v0.2.3 attribution apparatus have been relocated to the companion *Free Will* paper as part of its philosophical engagement: the original [Free Will §4.2] "Ownership without clean sourcehood; source-compromise without ownership-failure" is now [Free Will §4.2]; the original [Free Will §4.3] "Manipulator-responsibility and manipulated-agent-responsibility" is now [Free Will §4.3]; the original [Free Will §4.4] "The architecture's compatibilist-coherent stance" is now [Free Will §4.4]. The numbering below preserves gaps at 9.5, 9.12, and 9.15 to keep cross-references stable; readers should consult the companion paper at those points. The full triadic apparatus is therefore distributed across this paper's §9 and the companion paper's §4.*

## 9.1 The triadic apparatus: ownership, responsibility, accountability

Three terms the architecture has kept distinct since Section 4 (apparent-I / other-I, 4.11; agency derivation schema, 4.8) and Section 7 (decision-quality / freedom / responsibility, 7.12). Section 9 formalizes the dissociation and prevents the downstream collapse that the philosophical literature frequently performs.

> *Ownership is a Condition 6 relation — the structural integration of the act / decision / output as the I's own. Responsibility is an attribution relation — the structural answerability of the agent for the act given ownership-status, source-status, developmental-window, Mode B availability, cascade foreseeability, and live mitigation / repair options. Accountability is an answerability / repair / demand relation — the structural addressability of the agent for explanation, expectation, mitigation, repair, or response given developmental availability, role-status, and the apparent-I / other-I structure (4.11).*

The three are dissociable. They often correlate (free, owned, source-clean acts typically support all three; severe Condition-failure typically reduces all three), but none reduces to either of the others, and the architecture's strongest cases live precisely in the dissociations.

| Term | Architectural meaning | What it is *not* |
|---|---|---|
| **Ownership** | Condition 6 relation; the act / decision / output is structurally integrated as mine in the lived-I profile | Source-cleanliness; freedom; quality; outcome; moral or legal responsibility |
| **Responsibility** | Attribution relation; the agent is structurally identifiable as the relevant agent-source of the decision / action / omission / cascade given the overlay configuration | Freedom alone; ownership alone; outcome alone; deserved blame; legal liability |
| **Accountability** | Answerability / repair / demand relation; the agent is structurally addressable for explanation, expectation, mitigation, repair, or response | Punishment-deservingness; moral desert; legal liability; social sanction |

The dissociations the architecture commits to:

| Configuration | Ownership | Responsibility | Accountability |
|---|---|---|---|
| Manipulated wholeheartedness | High (Condition 6 intact) | Reduced and qualified (source-compromise) | Distributed: agent and manipulator both addressable |
| Coerced prudent compliance | Often high | Reduced for selection-range; intact for survival-rationality decision | Distributed: agent and coercer both addressable |
| Source-clean owned mistake | High | High (full attribution) | High (agent is appropriate target of explanation / repair) |
| Alienated action (dissociation) | Low (Condition 6 compromised) | Reduced for current act; may relocate to prior formation or repair | May depend on therapeutic / supportive context |
| Pre-agential imprinted habit acted out by mature agent | High (now-mine) | Substantially reduced for original formation; may attach to current repair availability | Repair-accountability may be live where mitigation options are developmentally available |
| Compulsion with intact Mode B objection | Often conflicted ownership | Reduced for capture-moment; preserved for prior avoidance / treatment-seeking / environment-design | Repair-accountability typically retained |

The triad gives Section 9 its core analytical leverage. It also rules out moves the architecture rejects: collapsing responsibility into ownership (would make manipulated wholeheartedness either unowned or undebatable), collapsing accountability into responsibility (would make repair-accountability impossible where original responsibility is reduced), collapsing ownership into responsibility (would make alienated action unanalyzable as a configuration where ownership fails but the agent remains structurally relevant for repair-attribution). The triadic dissociability is the apparatus that lets the architecture handle the cases the literature finds difficult.


## 9.2 Objects of attribution: decision, trying, action, outcome, cascade, profile-formation

Section 7.10 established the four-way separation of decision / trying / action / outcome. Section 9 extends this with cascade and profile-formation as additional attribution-objects, and asks for each: what is the agent attributable as the source of?

| Attribution object | What Section 9 asks |
|---|---|
| **Decision** | Was the operator-bundle selection-event attributable to the agent? Was it owned, source-clean, made under intact conditions, or compromised in some configuration-specific way? |
| **Trying** | Was the agent responsible for attempting, sustaining, abandoning, or failing to attempt the implementation? Was effort within developmentally available range? |
| **Action** | Was the implemented act bundle-mediated, owned, source-clean, compelled, alienated, or impaired in some condition-specific way? Did the implementation-pathway carry the agent's selection or run preempted? |
| **Outcome** | Did the result follow from the action, from luck, from not-I interference, from cascade dynamics, or from external conditions outside the agent's structural domain? |
| **Cascade** | Were downstream effects foreseeable, manageable, repairable, and developmentally available as targets for cascade-management willing (per 6.11)? |
| **Profile-formation** | Did prior self-shaping, habit-formation, or scaffold-selection create the later agency-configuration? When is the agent attributable as the source of the becoming-this-agent? |

The four-way separation prevents a class of attribution errors. Responsibility for the bad outcome is not the same as responsibility for the decision; responsibility for the decision is not the same as responsibility for the action; responsibility for the action is not the same as responsibility for the cascade. Section 9 treats each as a distinct attribution-object with its own overlay-profile, and the same agent can have very different attribution-profiles for the decision, the trying, the action, the outcome, the cascade, and the profile-formation that produced this configuration.

The discipline:

> *Each attribution-object has its own overlay-profile. Conflating attribution-objects is one of the most common philosophical errors the architecture is engineered to prevent.*


## 9.3 The attribution profile: the diagnostic schema for Section 9

This subsection is the section's load-bearing apparatus. Every attribution-judgment in 9.4–9.16 is read against the same diagnostic schema.

The attribution profile $AP_{m,t;a}$ for a given act $a$ at moment $t$ in agent $m$:

$$AP_{m,t;a} = \langle V, O, S, C, B, D, K, M, R, T \rangle$$

where:

| Component | Meaning |
|---|---|
| $V$ — Variation-family | Section 8 structural input (which of the 17 variation-families applies, and if compound, the compositional structure per 8.19) |
| $O$ — Ownership-status | Integrated, conflicted, alienated, dissociated, imposed, merely narrated (per Condition 6, 7.10, 8.13) |
| $S$ — Source-status | Source-clean, scaffolded, source-compromised, poisoned, coerced, osmotically shaped (per 5.9, 8.15) |
| $C$ — Condition-profile | Which of the six free-choice conditions hold, are thin, fail, or are bypassed (per 3.2, expanded 9.4) |
| $B$ — Mode B object-domain availability | What the I could take as object reflectively at the relevant order (per 7.6, 8.2 axis 6) |
| $D$ — Developmental-window | Pre-agential, immature, mature, scaffold-captured, trauma-shaped (per 4.10, 8.2 axis 9, expanded 9.6) |
| $K$ — Cascade profile | Direct, indirect, anticipated, unmanaged, repairable, non-repairable (per 5.6, 6.11, 8.2 axis 10) |
| $M$ — Mitigation / repair options | Live, fuzzy-live, not live, externally imaginable only |
| $R$ — Role / order profile | Foundational-order or constructed-order; if constructed, which order and which role (institutional, leadership, teaching, therapeutic, manipulative, etc., per 5.7, 8.16) |
| $T$ — Temporal locus | Prior formation, moment of action, downstream repair, future prevention |

The profile is *the* attribution apparatus. Three commitments follow.

*The joint profile is the attribution.* No single overlay axis settles responsibility. The same variation-family with different overlays produces different attribution-profiles, and the same overlay-profile with different variation-families produces different attribution-profiles. The Patch 10 discipline is that responsibility is computed from the joint configuration of all axes, not read off any single axis.

*The schema is diagnostic apparatus, not a uniform-reporting checklist.* Many attribution cases are sharply specified by a few axes: simple thin agency by $V$, $C$; manipulation cases by $V$, $S$, $O$, $R$; ADHD-like cases by $V$, $C$, $D$, $M$; cascade cases by $K$, $M$. The schema's role is to give each attribution-judgment a structurally specifiable signature that can be cross-checked against the prior architecture.

*The schema generates worked examples that demonstrate the dissociation.* Three examples illustrate.

**Example 1: Thin free selection vs free-choice-proper decision under different condition-profiles.** An agent selects between two indistinguishable beverages (8.3 thin agency). $V$ = thin agency; $O$ = integrated; $S$ = source-clean; $C$ = C2 minimal but C1, C3, C5, C6 intact; $B$ = available; $D$ = mature; $K$ = direct local outcome only; $M$ = N/A; $R$ = foundational; $T$ = moment of action. Attribution: decision-attribution intact but with low evaluative-depth weighting; outcome-attribution local; no cascade. Compare: a different agent making a major financial decision with the same $O$, $S$, $D$, $B$, $K$, $M$, $R$ values but $C$ all-conditions-intact (8.3 reduced agency or free choice proper). Attribution: decision-attribution intact with full evaluative-depth weighting. Same attribution-object — the decision-event — but different condition-profile, hence different attribution-weighting. Examples 2 and 3 below show the stronger same-$V$, different-overlay pattern where the variation-family is held constant and the overlays vary.

**Example 2: Compulsion under different developmental-window overlays.** An agent in active addictive compulsion fails Condition 4 at the moment of action (8.8). $V$ = compulsion; $O$ = conflicted; $S$ = often substrate-compromised + osmotically-shaped; $B$ = present for objection but unavailable for capture-domain control; $K$ = self-perpetuating loop. Two cases differ at $D$ and $M$: (a) mature agent with live treatment / environment-design / accountability-structure options (per 8.8 strategy-discussion), (b) trauma-shaped agent during developmentally-relevant period with limited live mitigation. Attribution-profile: case (a) has reduced moment-of-action responsibility but preserved repair-accountability and prior-avoidance attribution; case (b) has further-reduced moment-of-action responsibility plus reduced prior-avoidance attribution due to developmental-window constraints. Same variation-family, different attribution-profile.

**Example 3: Manipulated wholeheartedness under different role-overlays.** An agent makes a fully-owned ($O$ = integrated), evaluation-engaged ($C$ all-conditions-intact) decision whose option-space was poisoned by another agent (8.15 manipulation). $V$ = manipulation; $S$ = source-compromised; $O$ = integrated; $B$ = available but cannot detect source-compromise; $K$ = depends on stage. Two sub-cases: (a) acute one-time manipulation by a peer; (b) long-osmotic ideological shaping by an institutional actor over years. Case (a) has higher manipulator-attribution (clear constructed-order act with identifiable target-outcome); case (b) has distributed manipulator-attribution across the institutional structure plus the agent's mature-period reception of the shaping (per [Free Will §4.3]). Same variation-family on the agent's side, different attribution-profile because of the manipulator's $R$ and $T$ overlay differences.

These examples show that the schema does the work — the attribution is not the variation-family, it is the integration of variation-family with overlays.


## 9.4 Free-choice conditions and attribution effects

Section 3.2 established the six conditions of free choice. Section 9 develops how compromises in each condition affect attribution differently. The same overall reduction-from-free-choice-proper can come from very different condition-failures, and the attribution-implications differ accordingly.

| Free-choice condition | If intact | If compromised | Attribution implication |
|---|---|---|---|
| **C1 — Live-option construction** | Options are constructible as live and contrastive | Coercion, contraction, poisoned options, apparent option-space, forced choice | May reduce responsibility for selection-range; does not automatically remove ownership; coercion introduces attribution to the coercer or source-structuring agent where such an agent exists (per [Free Will §4.3]) |
| **C2 — Evaluative engagement** | $\Pi$, PtCns, projection-toolset engaged | Evaluation distorted, salience-captured, source-poisoned, projection-toolset compromised | Affects decision-quality and source-status; reduces responsibility for evaluative depth; selection-responsibility may remain |
| **C3 — Operator-bundle selection** | Bundle commits direction | Drift, paralysis, collapse, non-selection (per 7.8, 8.10) | Decision-responsibility may fail; omission-accountability may remain (per 9.9) |
| **C4 — Non-preemptive substrate coupling** | Implementation coupled but not captured | Compulsion, addiction, reflex-like capture, substrate dominance (per 8.8) | Action-responsibility may reduce; prior-avoidance and repair responsibility may remain (per 9.8) |
| **C5 — Mode B availability** | Relevant object-domain reflectively accessible | Order-specific Mode B unavailability, confabulatory reflective access, or source-opacity that blocks reflective object-access to the relevant agency-structure; transient unavailability under high-bandwidth execution (per 7.5, 7.6) | Reduces prospective accountability where the relevant object-domain was unavailable; preserves post-hoc repair demands where Mode B is later available |
| **C6 — Ownership-integration** | Act integrated as mine | Alienated, dissociated, imposed, merely narrated (per 8.13) | Ownership-attribution weakens or fails; responsibility may shift to prior formation, third-party source, or repair if such options are live (per 9.8) |

The governing rule:

> *Condition-compromise is attribution-relevant, not attribution-determinative.*

A C1-compromised act may have reduced selection-range responsibility but full ownership and full action-responsibility within the contracted option-space. A C5-compromised act may have reduced prospective accountability but full ownership and full retrospective repair-accountability. A C6-compromised act may have reduced ownership but the substrate-action remains responsibility-relevant for repair-questions about the agent who carries the dissociated profile-region. The architecture's discipline is that each compromised condition has a specific attribution-implication, and conflating them is one of the recurring errors in the philosophical literature.



## 9.5 *(see companion paper)*

The original §9.5 of v0.2.3 ("Ownership without clean sourcehood; source-compromise without ownership-failure") has been relocated to [Free Will §4.2] as part of the philosophical engagement with manipulation, ownership, and sourcehood. Cross-references to the original §9.5 elsewhere in this paper now point to [Free Will §4.2]. The structural decomposition of ownership / sourcehood dissociation, manipulator-and-manipulated attribution, and the compatibilist-coherent stance is developed there.

## 9.6 Developmental-window as responsibility overlay

Section 4.10 and Section 8.2 (axis 9) established that developmental-window status is a *Section 9 responsibility-overlay*, not a Section 8 variation classifier. A pre-agentially imprinted habit-pattern and a mature-deliberatively-chosen habit-pattern share the same Section 8 variation-family (habitual-chosen action) while differing at the developmental-window axis — and the difference matters for attribution.

Five-window taxonomy:

| Developmental window | Structural status | Attribution effect |
|---|---|---|
| **Pre-agential** | Toolkit / Mode B / live-option capacity not yet developed; the imprinting period precedes architectural agency | Strong reduction of responsibility for the formative imprinting; possible attribution to caretakers / scaffolders / environment as the source of the imprinted pattern |
| **Immature** | Partial toolkit; unstable live-option construction; limited source-access; verification-tools developing | Responsibility partial and domain-specific; mature-agent standard is not yet the right reference; attribution-strength scales with the available toolkit at the relevant time |
| **Mature** | Toolkit and Mode B object-domains normally available; verification-tools functional | Stronger default attribution; failures require specific variation-analysis; the standard against which the other windows attenuate |
| **Scaffold-captured** | Mature agency-capacities operate inside externally structured option-space (cult, total institution, comprehensive ideological system per 8.15); toolkit was formed and is sustained by the scaffold | Attribution split between agent-owned selection within the structured space and scaffold-source compromise of the option-space itself; one of the most architecturally demanding cells; attribution typically distributed |
| **Trauma-shaped** | Mature toolkit but projection-space, option-construction, and Mode B object-domains shaped by prior threat / dysregulation / state-dependent contraction (per 5.4, 8.12) | Responsibility qualified by current availability of alternatives, mitigation, repair, and Mode B object-domain access; reduction is not absolution; trauma-history makes some options non-live without making the agent non-responsible for those options that remain live |

The governing rule:

> *Developmental-window status changes attribution-strength; it does not change the Section 8 variation-family. A habit acted out by a pre-agentially imprinted mature agent is structurally a habit (8.7); the developmental-window overlay attenuates responsibility-attribution for the formation while preserving the variation-classification.*

The hardest cell is scaffold-captured. The mature agent who acts wholeheartedly within a comprehensive ideological scaffold satisfies most internal agency conditions: live options exist within the scaffold's structure, evaluation engages, operator-bundle selects, ownership integrates, Mode B operates within the scaffold's object-domain. What is compromised is the option-space's source-status and the toolkit's verification-capacity for source-status outside the scaffold. The architecture's reading: attribution within-scaffold is real (the agent owns the within-scaffold act); attribution for the scaffold-formation depends on the agent's developmental-window at the time of formation and on whether mature-period verification-tools could have surfaced the source-compromise. The scaffold-architecture itself bears constructed-order attribution per 9.12.


## 9.7 Mode B availability, recognition, and accountability

Section 7.6 established the order-asymmetric Mode B object-domain availability — Mode B may be available for some agency-structures while unavailable for others, with constructed-order Mode B bandwidth-limited via the 5.6 lossy-compression cascade. Section 9 develops the attribution-implications.

*A note on $A/\phi$ vs Mode B before the table.* The $A/\phi$ taxonomy and Mode B object-domain availability are related but not identical. $A/\phi$ describes phenomenal availability and source-pathway access of contents (per File 3 §6.1); Mode B object-domain availability describes whether the I can take the relevant agency-structure as object in reflective self-modeling (per 7.6). The two interact — content with low-$\phi$ source-pathway access will typically support correspondingly less reliable Mode B object-access to the agency-structures that engaged it — but they are architecturally distinct. Source-opacity becomes attribution-relevant for Mode B only when it blocks, distorts, or delays reflective object-access to the relevant agency-domain. The table below gives the Mode B statuses; $A/\phi$ source-opacity appears as one of the conditions under which Mode B object-access is partial or post-hoc rather than as a Mode B status itself.

| Mode B status | Attribution implication |
|---|---|
| **Available and exercised** | Stronger accountability for ignored reasons, ignored warnings, or failed mitigation; the agent did access reflective resources and chose against them |
| **Available but not exercised** | Responsibility depends on whether non-exercise was source-clean, negligent, captured, developmentally unavailable, or appropriately not-exercised (e.g., flow per 7.5) |
| **Available only post-hoc** | Reduced prospective accountability; repair-accountability typically remains where post-hoc reflection reveals available repair-options |
| **Order-asymmetrically unavailable** | The agent may reflect on one domain while lacking object-access to another; attribution attenuates for the unavailable domain but preserves for the available one (per 7.6) |
| **Mode B available under $A/\phi$ source-opacity** | Phenomenal awareness does not equal source-access; responsibility for the act may be intact while responsibility for the act's source-pathway is reduced (per 7.9); $A/\phi$ source-opacity is not itself a Mode B status — it is an $A/\phi$ status that may make Mode B object-access partial or post-hoc |
| **Confabulated** | Attribution must distinguish narrated authorship from actual selection-source; confabulation does not establish responsibility; absence-of-confabulation does not establish responsibility either |
| **Transiently unavailable under high-bandwidth execution** | Per v0.1.6.1 patch #11: transient unavailability does not by itself violate Condition 5 if post-action access is non-confabulatory; attribution-implications track multiple temporal loci — prior training, prior policy-formation, post-action reflective access, and post-action repair — not only during-action availability |

The discipline against a crude "they could have reflected" standard. The architecture's commitment is that Mode B availability is *order-and-domain-specific*, not globally present-or-absent. An ADHD-like agent may have full Mode B reflective access to the substrate-developmental gap (per 8.9) without having Mode B reflective overcoming-capacity for the gap; a compulsive agent may have full Mode B objection-capacity to the act without having Mode B alteration-capacity for the capture-domain (per 8.8). Attribution must track these asymmetries rather than presuming uniform Mode B presence.


## 9.8 Diminished agency: reduction, relocation, and residual accountability

Compulsion, addiction, severe affect-contraction, dissociation, learned helplessness, depression, anxiety, shame-collapse, ADHD-like implementation gaps. These are the Section 8 variation-families whose responsibility-implications the philosophical literature most disputes. The architecture's organizing rule:

> *Diminished agency does not produce one responsibility result. It produces a relocation problem: responsibility may remain at the decision, shift to prior self-scaffolding, shift to mitigation / repair, shift to third-party source-compromise, or fail for the target object.*

| Variation-family | Default attribution pressure | Guardrail |
|---|---|---|
| **Compulsion / addiction (8.8)** | Moment-of-action responsibility reduced where C4 capture dominates | Prior avoidance, treatment-seeking, environment-design, accountability-structure engagement, and current repair may remain live and attribution-relevant |
| **Dissociation / alienation (8.13)** | Ownership weakens or fails at C6 | Do not misclassify as compulsion (substrate capture vs ownership failure are distinct per 8.13 guardrail) |
| **Learned helplessness (8.11)** | Projection-toolset damage reduces live-option construction | Conceptual recognition of helplessness is not automatically repair (per 8.11 commitment); attribution attenuates for selection that the toolkit cannot construct as live |
| **ADHD-like implementation gap (8.9)** | Implementation-responsibility may reduce across duration where substrate-developmental constraint dominates | Cascade-management may remain attribution-relevant if scaffold-options were live and developmentally available; the gap's variability allows for context-specific attribution |
| **Severe affect-contraction (8.12)** | Agency may contract without disappearing | Affect is modifier, not automatic exculpation; the contracted configuration is real but the agent within it remains responsibility-relevant for the options that remain live |
| **Akrasia (8.6)** | Often responsibility-preserving — the operator-bundle selected, ownership intact | Do not confuse with C4 compulsion by default (per v0.1.6.1 patch #23 and 8.6 guardrail); akratic action is the agent's own in the strong sense |
| **Apparent choice / confabulation (8.14)** | Attribution depends on which sub-case obtains | Post-hoc recognition (real selection) vs source-opacity (real selection, low source-access) vs confabulation (no actual selection) yield very different attribution-profiles per 7.9 |
| **Coercion (8.4)** | Attribution distributed between coerced agent and coercer | Coerced prudent compliance preserves selection-responsibility within the contracted option-space; coercer attribution-relevant for the contraction |

The governing discipline:

> *Reduction is not absolution. Persistence of accountability is not moralism. The architecture supplies graded, profile-indexed attribution; it neither defaults to "off the hook" nor defaults to "fully responsible regardless."*

This is where Section 9 must be most careful. Some clinical contexts default to reduced-attribution for diminished-agency cases; some philosophical treatments default to preserved-attribution. The architecture's stance is that neither default is correct as a general rule. Each diminished-agency case has its own attribution-profile that depends on which conditions are compromised, which overlays apply, and what mitigation / repair / prior-avoidance options were live.


## 9.9 Omission, withholding, refusal, and drift

Section 8.5 established the omissive-decision class: non-action is agency only when non-action is live and selected. Section 9 develops the attribution-implications, which differ sharply across the omission cases.

| Case | Attribution structure |
|---|---|
| **Withholding** | Selected non-action; usually decision-attributable with full ownership and source-clean configuration; the agent owns the selected non-action |
| **Refusal** | Selected non-compliance; often high ownership and high sourcehood; the agent owns the refusal as a positive-selection-of-non-compliance |
| **Strategic delay** | Selected timing; responsibility depends on projection-quality and live alternatives; attributable as configurational decision per 7.11 |
| **Veto** | Selected interruption of an emerging course; responsibility-attributable as decision-event (the agent commits direction toward stopping the course) |
| **Omissive decision under coercion** | Owned non-action inside compromised option-space; per 9.5, ownership intact while source-status compromised |
| **Drift / inaction** | No selection-event; responsibility for the moment of inaction may fail (Condition 3 not exercised); responsibility may shift to prior scaffolding, prior habit-formation, or current repair if such options were live |
| **Collapse** | Agency failure under overload; accountability depends on developmental availability of mitigation / scaffolding; reduction is significant but not absolution where prior-avoidance or repair options were live |

The discriminator:

> *Non-action is not one thing. Some non-action is a decision (withholding, refusal, strategic delay, veto, omissive decision under coercion); some is non-selection (drift, collapse). Decision-attribution applies to the former; non-selection cases shift attribution to prior formation or repair-availability.*

This subsection is short but essential. The Libet veto cases (Section 10 territory) and the moral-philosophy literature on "doing vs allowing" both depend on the omission-decision-vs-non-selection distinction. Section 9 supplies the structural distinction; downstream sections engage the empirical and normative literatures.


## 9.10 Cascade-effect responsibility

This is one of the section's most distinctive contributions. Section 5.6 established the output-imprinting cascade (Stage 1 substrate-imprinting / Stage 2 input to other agents and environment / Stage 3 closure feeding back as input). Section 6.11 established cascade-management as application of existing willing-strategies to downstream effects. Section 9 develops the attribution-rules.

The architectural commitment from 6.11, propagated through 8.20 and Patch 10:

> *Cascade-effects within the agent's structural domain do not automatically settle accountability. They become responsibility-relevant when (i) the agent had live mitigation / repair / arranging / anticipation options for the cascade, (ii) those options were developmentally available rather than merely externally imaginable, and (iii) the agent's bundle-mediated act foreseeably set the cascade in motion.*

Cascade-stage attribution:

| Cascade stage | Description | Responsibility question |
|---|---|---|
| **Stage 1 — Self-imprinting** | I-level activity imprints next-order substrate | Could the agent anticipate or manage self-shaping effects? Was profile-formation foreseeable as a consequence of repeated action? |
| **Stage 2 — Output to others / environment** | Third-order substrate output imprints not-I, other agents, environment | Could the agent anticipate impact on others, surroundings, institutional structure? Were anticipation / arranging options live? |
| **Stage 3 — Closure as input-imprinting** | Shaped substrate feeds back as input-imprinting | Could the agent repair, interrupt, or prevent loop-closure? Were repair-options developmentally available? |

The cascade-attribution test (six items):

1. Did the cascade fall within the agent's structural domain — that is, was it a foreseeable consequence of the agent's bundle-mediated act?
2. Was the cascade reasonably projectable by that agent's *actual* toolkit at the time of action — not a perfect-information observer's toolkit?
3. Were mitigation / arranging / repair options live, or merely externally imaginable from outside the agent's perspective?
4. Were those options developmentally available given the agent's developmental-window status (per 9.6)?
5. Was Mode B object-domain access available for the relevant cascade-domain (per 7.6, 9.7)?
6. If gates 1–5 are satisfied, did the agent ignore, refuse, or fail to construct the relevant cascade-management option despite its being live, developmentally available, and Mode-B-accessible?

The first five gates determine whether cascade-management was structurally available. The sixth gate determines the attributional direction: ignored or unconstructed available options strengthen cascade-attribution; genuinely unavailable options attenuate or defeat it. The architecture rejects the move that treats any cascade-effect as automatically the agent's responsibility just because the agent's act was somewhere in the causal chain. It also rejects the move that treats cascade-effects as automatically not the agent's responsibility just because the cascade went through other agents or environments. The structural-availability framing keeps both errors at bay.

The discipline:

> *Cascade-attribution is real but bounded. It is real because the layered output-structure (5.6) is real and the agent's bundle-mediated act is one of its layers. It is bounded because attribution requires the live-mitigation / developmental-availability / Mode B-access / engagement structure to obtain — not external-observer projection.*

*A worked application of the six-gate test.* A team-leader makes a fourth-order decision to publicly criticize a subordinate during a meeting (Section 8.16 leadership / constructed-order). The criticized subordinate later experiences depressive symptoms that affect their work performance. Cascade-attribution gate-by-gate: (1) *In structural domain?* Yes — the cascade through the subordinate's affective response and work-performance falls within the leader's constructed-order target-domain. (2) *Projectable by the leader's actual toolkit?* Depends on the leader's mature-toolkit interpersonal projection capacity; an experienced leader's toolkit projects affective-impact paths from public criticism, an inexperienced leader's may not. (3) *Mitigation / arranging options live?* Private feedback, post-meeting reparative outreach, contextual reframing — typically yes, structurally available before and after the act. (4) *Developmentally available?* Yes for a mature team-leader; possibly partial for a new manager in a developmental-window cell. (5) *Mode B object-access for the cascade-domain?* Yes for a leader whose Mode B reflective access extends to interpersonal cascade-effects; partially for one whose Mode B is order-asymmetrically constrained. (6) *Did the agent ignore or fail to construct the available cascade-management option?* If yes, cascade-attribution is strengthened — the leader bears responsibility for the cascade given that mitigation was structurally available and was not engaged. If gates 1–5 are not all satisfied, attribution attenuates correspondingly — cascade-attribution is not the same in case (a) the experienced leader who chose public criticism over available private feedback as in case (b) the new manager whose mature-toolkit interpersonal projection was developmentally limited at the time of the act.


## 9.11 Constructed-order responsibility

Section 5.7 established constructed orders ($n \geq 4$) as targeting not-I coordination structures rather than lower-order activity. Section 8.16 developed the variation-family. Section 9 develops the attribution-implications.

The architectural commitment:

> *Constructed-order responsibility is not morally higher because it is higher-order. It is attributionally wider because the agent's target-domain includes not-I coordination structures whose cascade-effects extend across multiple agents, multiple times, and (often) across institutional or cultural reach.*

| Constructed-order role | Responsibility issue |
|---|---|
| **Teacher / coach / therapist** | Toolkit-shaping another agent; source-status depends on transparency, alternatives, recipient aims, and source-access (per 8.16); responsibility includes the recipient's toolkit-development, the recipient's ongoing autonomy, and the cascade through the recipient's later acts |
| **Leader** | Direction of group option-space; cascade foreseeability and role-access amplify attribution; responsibility extends to the option-spaces, salience-fields, and willing-strategies the leader shapes for the led |
| **Institutional actor** | Action through structured role-space; accountability depends on actual role-discretion (not generic institution-membership), live alternatives within the role, and source-access for the role's structuring effects |
| **Bureaucratic participant** | Responsibility depends on actual role-discretion; bureaucratic capture (per 8.16) constrains the option-space without erasing whatever discretion remains |
| **Manipulator** | Source-compromising another agent's live-option / evaluation / selection / source-access apparatus; constructed-order act at fourth or higher order with the manipulated agent's compromised condition as the manipulator's outcome (developed in 9.12) |
| **Cultural / propagandistic agent** | Distributed source-shaping across multiple recipients and time; responsibility distributed across the agents who participate in the propagation; less concentrated than acute manipulation but no less real |

The discipline preserves the 8.16 guardrail: *constructed-order classification is structural, not ethical.* Ethical / source-status evaluation occurs at transparency, source-access, aim-relation, and alternative-suppression — not at order-level. A teacher and an indoctrinator both perform constructed-order acts; the moral distinction lives at source-status and aim-relation, not at the constructed-order classification itself.

*Constructed-order downstream responsibility is bounded by the 9.10 cascade-attribution test.* Responsibility for later recipient acts is not automatic. Constructed-order agents (teachers, leaders, therapists, institutional actors, manipulators) are attribution-relevant for downstream recipient conduct only where the 9.10 conditions are met: the downstream effect was projectable by the agent's actual toolkit, mitigation / arranging options were live, the relevant Mode B object-domain access was available, and the developmental-window status supported the cascade-management capacity. Constructed-order role amplifies the cascade-foreseeability profile and typically expands the cascade-domain, but it does not replace the cascade-attribution test with automatic responsibility for the recipient's later acts.

The membership-test reminder per 5.7: constructed-order responsibility attaches when the target is the not-I coordination structure as such, with sufficient trained-expectation grounding for fuzzy lower-order availability. Mere lower-order action with social side-effects is not constructed-order responsibility.



## 9.12 *(see companion paper)*

The original §9.12 of v0.2.3 ("Manipulator-responsibility and manipulated-agent-responsibility") has been relocated to [Free Will §4.3] as part of the philosophical engagement with manipulation, ownership, and sourcehood. Cross-references to the original §9.12 elsewhere in this paper now point to [Free Will §4.3]. The structural decomposition of ownership / sourcehood dissociation, manipulator-and-manipulated attribution, and the compatibilist-coherent stance is developed there.

## 9.13 Shared, distributed, and collective responsibility

Multi-agent attribution must avoid two errors: (i) reifying institutions or groups as I-like choosers (the architecture's perspectival-realist commitment from File 4 §9 forbids unindexed group-mind attribution), and (ii) treating multi-agent cases as reducible to isolated individual attribution (the layered output-structure of 5.6 makes inter-I cascade-effects structurally real).

The architectural framing:

> *Collective responsibility is profile-indexed distribution across agents, roles, source-relations, and cascade positions; it is not an unindexed group mind inside the architecture. Each contributing agent's attribution-profile is computed from their own variation-family + overlays; the collective configuration is the joint pattern of these profile-indexed attributions.*

| Configuration | Attribution method |
|---|---|
| **Joint bundle-mediated** | Multiple agents each perform bundle-mediated acts contributing to a common outcome; each agent's responsibility computed from their own profile |
| **Cascade-shared** | Multiple agents' Stage 2 outputs converge as joint cascade-effects; attribution distributed across agents per their cascade-foreseeability and live mitigation |
| **Scaffold-distributed** | Higher-order agents shape lower-order agents' option-spaces; attribution split between scaffold-source agents and within-scaffold acting agents |
| **Role-differentiated** | Responsibility varies by role-access, authority, expertise, and live alternatives within the institutional structure |
| **Distributed ignorance** | No single agent sees the full cascade; accountability depends on whether information-sharing structures were live and developmentally available |
| **Collective repair** | Repair-responsibility may be distributed even where original responsibility is partial, unclear, or attenuated; repair-attribution operates on a different axis than original-act attribution |

The perspectival-realist anchor: attribution is always *from-an-agent-perspective*. The apparent-I / other-I apparatus (4.11) lets the architecture analyze how each agent's perspective constructs the other agents and the institution; collective attribution is the joint pattern of perspective-anchored attributions, not a free-standing group attribution.

*Shared affective configurations preserve the perspectival-realist discipline.* Shared panic, shared shame, collective awe, mass ideological affect, and similar configurations should be modeled as distributed profile-shaping and cascade interaction across multiple agents — each agent's affective configuration is the agent's own; the cross-agent pattern is the joint configuration of profile-indexed states under shared input-conditions and Stage 2 cascade reception. The architecture does not introduce a group-affect posit any more than it introduces a group-mind posit; "shared affect" is structurally a distributed pattern of agent-anchored affective configurations interacting through the apparent-I / other-I apparatus.

Institutional responsibility, in particular, translates structurally as *role-indexed agent responsibility plus constructed-order scaffold effects*. The architecture does not introduce a separate group-agency posit. The institution is a constructed-order coordination structure that shapes individual option-spaces, salience-fields, willing-strategies, and Mode B object-domains; institutional responsibility is the joint pattern of (a) role-indexed individual attributions of the institution's agents and (b) constructed-order scaffold-attribution for the agents who shape the institutional structure itself.


## 9.14 Profile-formative responsibility: responsibility for becoming

Section 7.11 distinguished profile-formative configurational decisions from constructed-order decisions. Section 5 (toolkit-development at 5.5) and Section 5.9 (self-curation under prior compromise) prepared the apparatus. Section 9 develops the attribution-implications of "responsibility for becoming."

The core question:

> *When is an agent responsible for the profile-conditions that later shape their agency?*

| Profile-formative case | Attribution implication |
|---|---|
| **Deliberate self-training (mature, source-clean)** | Strong responsibility for later compiled agency where consequences were projectable through the trained-expectation discipline (3.2, 5.7); the agent who deliberately trains themselves into a skilled or virtuous configuration owns that configuration's later operation |
| **Habit architecture (configurational willing)** | Responsibility depends on source-status and developmental availability of configurational willing; per 8.7 self-perpetuating loops, the agent's habitual-chosen pattern carries forward attribution where the choosing was live and the pattern's cascade was foreseeable |
| **Self-curation under prior compromise (5.9)** | Responsibility qualified by source-compromise history; the agent's apparent-autonomous self-curation may be source-shaped by the prior compromise it inherits; attribution gradient depends on whether mature-period verification-tools could have surfaced the inheritance |
| **Trauma-shaped profile formation** | Strong reduction for the formative period; possible mitigation / repair responsibility if later-period treatment / re-evaluation / scaffolding-revision options become live; attribution does not erase but does substantially attenuate |
| **Institutionally scaffolded identity formation** | Split between agent-owned uptake of the scaffold and scaffold-source attribution; per 9.6 scaffold-captured cell, mature within-scaffold attribution is real, formation-attribution depends on developmental-window |
| **Manipulated self-formation (deliberate other-shaping during developmental period)** | Manipulator bears constructed-order responsibility for source-compromising the agent's profile-development; agent attribution may remain partial for any mature-period choices that engaged the manipulated profile |

The discipline:

> *Profile-formative responsibility is configurational willing's attribution-implication propagated forward in time. The agent who configurationally arranged future profile-states bears responsibility for the agency that operates from those profile-states to the extent that the arranging-act was source-clean, live, evaluable, and within the trained-expectation envelope of 5.7.*

Profile-formative responsibility gives Section 9 philosophical depth on the responsibility-for-character question without committing to a full theory of character. The architecture's contribution is that the question is structurally tractable through the configurational-willing apparatus and the developmental-window overlay; what remains for normative theory is the question of what the structural inputs morally imply.



## 9.15 *(see companion paper)*

The original §9.15 of v0.2.3 ("The architecture's compatibilist-coherent stance") has been relocated to [Free Will §4.4] as part of the philosophical engagement with manipulation, ownership, and sourcehood. Cross-references to the original §9.15 elsewhere in this paper now point to [Free Will §4.4]. The structural decomposition of ownership / sourcehood dissociation, manipulator-and-manipulated attribution, and the compatibilist-coherent stance is developed there.

## 9.16 Summary: variation-family × attribution overlays

Section 9 has developed responsibility-attribution as a structurally computed apparatus over the agency-variation taxonomy of Section 8 with the overlay axes prepared by Sections 3–7. The taxonomy organizes around variation-families with the attribution-profile $AP_{m,t;a}$ providing the architectural reading of each attribution-judgment.

| Section 8 variation-family | Primary attribution question Section 9 asks |
|---|---|
| Thin / reduced agency (8.3) | Which conditions are thin, and does thinness matter for the relevant attribution-object? |
| Constrained / forced / coerced choice (8.4) | Which options remained live, and who structured the threat / constraint / contraction? |
| Omission / withholding / refusal / veto (8.5) | Was non-action selected (decision-attributable) or non-selected (drift / collapse)? |
| Akrasia (8.6) | Was the misalignment owned and selection-preserving? Is C4 actually compromised, or is this Π-conflict / identity-correlation divergence (ρ-divergence)? |
| Habitual action (8.7) | Was the habit chosen, compiled, source-compromised, or compulsive? What is the developmental-window status of the formation? |
| Compulsion / addiction (8.8) | Was C4 captured, and were prior-avoidance / treatment / repair / mitigation options live? |
| ADHD-like implementation gap (8.9) | Was sustained implementation developmentally available? Were scaffold-options live? Was Mode B asymmetric for the gap-domain? |
| Deliberation pathology (8.10) | Was there failure of selection, excessive loop, source-compromised delay, or implementation-gap delay? |
| Learned helplessness (8.11) | Was projection-toolset damage blocking live-option construction, and were repair-options live? |
| Affect-mediated contraction (8.12) | Did affect modify, contract, or eliminate agency-domain availability? Were the remaining options live? |
| Dissociation / alienation (8.13) | Did ownership fail at C6? Where does attribution relocate? |
| Apparent choice / confabulation (8.14) | Was there real selection (post-hoc recognition or source-opacity) or no selection (confabulation)? |
| Manipulation (8.15) | Was the action owned but source-compromised? Who shaped the source, and what was the manipulator's constructed-order act? |
| Constructed-order variation (8.16) | What role / order / option-space did the agent occupy, and what is the cascade-foreseeability profile? |
| Flow / mastery (8.17) | Was low effort mastery, automaticity, or capture? What is the substrate-coupling status? |
| Reflex / non-agency (8.18) | Is there any agency-object for attribution at all? |
| Compound configurations (8.19) | Which attribution-object and overlay dominate? What is the compositional structure? |

The synthesis:

> *Same variation-family, different attribution-profile depending on the overlays. Same attribution-profile, different normative response depending on the reader's moral / legal / restorative framework. The architecture supplies the structural inputs; the normative mappings live elsewhere.*


# 10. The empirical interface: timing, reports, neural markers, and agency-structure

Section 10 reads canonical empirical paradigms through the architecture. The Libet, Wegner, and Soon paradigms — and the broader literatures on intentional binding, voluntary inhibition, effort, flow, diminished agency, social influence, and longitudinal training — each test specific architectural objects, not "free will" simpliciter. The architecture supplies a translation apparatus for asking which agency-object each paradigm probes: decision, trying, action, outcome, ownership-recognition, source-access, Mode B availability, effort, cascade-management, or profile-formation. Section 10's central methodological claim:

> *Empirical paradigms do not observe "free will" directly. They observe task behavior, reports, timings, neural or behavioral markers, outcome effects, and retrospective interpretations. The architecture translates these signals into structural agency-objects so that the empirical literature becomes architecturally tractable without being read as direct agency-meters.*

Section 10 is the architecture's anti-overinterpretation section. Its central value is not to claim that Libet was wrong, that Soon was wrong, or that Wegner was wrong. The stronger move: these paradigms are often real and important, but they test narrower architectural objects than the philosophical debate frequently assumes. The architecture sorts empirical findings into preparation, selection, report, implementation, ownership, source-access, effort, inhibition, outcome-coupling, social source-shaping, and cascade — without collapsing them into "Is free will real?"

The boundary discipline holds. Section 8 classifies agency-variations. Section 9 attributes responsibility / accountability / ownership using Section 8's structures. Section 10 interprets empirical paradigms through the architecture's structural inputs. Section 11 promotes specific markers from Section 10's interpretations into formal predictions. [Free Will §5] engages philosophical positions. Section 12 surfaces open problems. Section 10 does *not* perform the work of Sections 9, 11, [Free Will §5] (translations), or 12 (open problems).

## 10.1 From attribution to empirical interpretation

Section 9 supplies the attribution apparatus that Section 10 uses to interpret empirical paradigms; Section 10 does not redo the attribution work. The handoff:

| Prior section | Supplies to Section 10 |
|---|---|
| Section 6 | Effort / outcome separation (6.9), effort markers (6.4 resistance taxonomy), cascade-management as application of existing strategies (6.11) |
| Section 7 | Decision-event timing as inferential not directly observed (7.13 forward caveat), four-way separation decision/trying/action/outcome (7.10), Mode B asymmetry (7.6), post-hoc recognition / source-opacity / confabulation triad (7.9), thin agency vs free choice proper |
| Section 8 | Variation taxonomy (17 families), ten-axis diagnostic schema (8.2), compound-configuration apparatus (8.19), apparent-choice / confabulated-agency variation-family (8.14) |
| Section 9 | Attribution-object separation (decision / trying / action / outcome / cascade / profile-formation, 9.2), the formal $AP_{m,t;a}$ profile (9.3), responsibility boundaries Section 10 must respect |

The core methodological claim, repeated for emphasis:

> *Section 10 is not asking whether experiments prove or disprove agency. It asks which architectural component each experiment is actually able to probe.*

A single architectural inequality drives the section: *an empirical paradigm can test a marker of an agency-component without testing the whole agency-configuration.* A readiness potential, decoding pattern, post-hoc report, intentional-binding effect, inhibition signal, effort marker, or clinical task-result must first be mapped to an architectural object before it can bear on free selection, free choice proper, ownership, sourcehood, diminished agency, or cascade. The mapping work is what the architecture supplies.

## 10.2 The empirical interpretation profile

Every paradigm-interpretation in 10.4–10.15 is read against a common diagnostic schema. The empirical interpretation profile $EIP_p$ for a given paradigm $p$:

$$EIP_p = \langle T, P_o, O_d, C_x, B_x, R_s, M_s, Q \rangle$$

where:

| Component | What it asks |
|---|---|
| $T$ — Task-structure | What is the participant actually asked to do? Spontaneous arbitrary action, forced selection, deliberation under time-pressure, withholding, sustained execution, social compliance, longitudinal training? |
| $P_o$ — Probed object / empirical proxy | Which architectural object or empirical proxy is the paradigm targeting: a Section 9.2 attribution-object (decision, trying, action, outcome, cascade, profile-formation), or a Section 10 empirical proxy (ownership-report, source-report, inhibition, effort, recognition-lag, outcome-coupling)? Empirical paradigms typically probe via proxies; the proxy must be linked back to the architectural object before any agency-claim is licensed |
| $O_d$ — Order-domain | Focus (first-order), thought (second-order), substrate action (third-order), or constructed-order coordination ($n \geq 4$)? |
| $C_x$ — Condition-target | Which of the six free-choice conditions is being stressed, measured, or rendered diagnostic by the paradigm? |
| $B_x$ — Mode B status | Is reflective object-access required, suppressed, delayed, distorted, or merely reported? Is Mode B exercise during action being measured, or post-action availability? |
| $R_s$ — Report-structure | What kind of report is collected: intention-time (W-time), motor-onset time (M-time), ownership, confidence, cause, effort, affect, outcome, post-hoc narrative? |
| $M_s$ — Marker-signal | Neural (EEG, fMRI, MEG), behavioral (RT, accuracy, persistence), phenomenological (verbal report), physiological (autonomic), social (compliance, cooperation), longitudinal (development, training)? |
| $Q$ — Interpretive caution | What inference would be invalid from this paradigm? Which architectural objects does the paradigm under-determine? |

Two architectural commitments follow.

*The schema is paradigm-interpretation apparatus, not responsibility-attribution apparatus.* The $EIP_p$ profile is deliberately distinct from the $AP_{m,t;a}$ attribution profile of Section 9.3. They have overlapping components ($O_d$ order-domain, $C_x$ condition-target, $B_x$ Mode B status) but different jobs: $AP$ computes attribution from agency-configuration; $EIP$ identifies what an empirical paradigm actually measures. Section 10 does not do attribution-work, and the $EIP$ schema is sized to keep that boundary firm — eight components for paradigm-interpretation, ten components for responsibility-attribution.

*The schema is diagnostic, not uniform-reporting requirement.* Many paradigm-interpretations are sharply specified by a few axes: Libet by $T$, $P_o$, $O_d$, $C_x$, $R_s$; Wegner by $P_o$, $B_x$, $R_s$, $Q$; Soon by $P_o$, $M_s$, $Q$; intentional binding by $P_o$, $R_s$. The schema's role is to give each paradigm a structurally specifiable signature that surfaces what it can and cannot measure.

*Two worked $EIP_p$ examples.*

**Libet readiness-potential paradigm.** $T$ = arbitrary spontaneous flex / button-press at self-selected timing. $P_o$ = $t_{report}$ (W-time) and $t_{move}$ (M-time) as proxies; $t_{select}$ is *not* directly probed. $O_d$ = first-order substrate-action; no second-order or constructed-order engagement scaffolded. $C_x$ = Condition 2 (option-evaluative engagement) is minimized or task-backgrounded by design; the paradigm specifically suppresses C2 to study C4 substrate-coupling timing. $B_x$ = Mode B is reflectively engaged for time-reporting (the W-time clock-task) but suppressed for the agency-structure of the flex itself. $R_s$ = motor-onset (M-time) and reported-awareness-time (W-time); both are post-event reports relative to the substrate dynamics. $M_s$ = neural (EEG readiness potential) and behavioral (motor-onset). $Q$ = the paradigm tests thin-free-selection timing dissociations under suppressed C2; it does not test free choice proper, wholehearted free choice, source-status, ownership, or constructed-order action.

**Wegner I-spy / choice-blindness paradigms.** $T$ = engineered attribution-conditions (priority / consistency / exclusivity manipulations); or post-decision swap-and-justify. $P_o$ = ownership-report and source-report as proxies; $t_{select}$ is *engineered* in the I-spy variant (selection externally produced) and *real but mismatched* in choice-blindness (real prior selection plus false later narration). $O_d$ = first-order or second-order; varies by task. $C_x$ = Condition 6 (ownership) and Condition 5 (Mode B reflective access to source-pathway) are stressed. $B_x$ = Mode B is engaged for reporting; what it has access to is the experimentally-engineered question. $R_s$ = ownership-confidence reports, cause-attribution reports, post-hoc justification narratives. $M_s$ = phenomenological reports (verbal, confidence-rated). $Q$ = the paradigm tests the phenomenology of authorship-attribution and the structure of source-reports under engineered or mismatched conditions; it does not test all selection-events as confabulated, nor does it establish that confabulation entails absence of an actual $t_{select}$.

## 10.3 Timing discipline: decision-event, report, implementation, outcome

The architecture's timing commitment from 7.13: *decision-event timing is inferential, not directly observable from agent report or motor-onset alone.* Section 10 makes this explicit with a six-marker timing chain that no empirical paradigm conflates without architectural cost:

$$t_{prep} \not\equiv t_{select} \not\equiv t_{report} \not\equiv t_{move} \not\equiv t_{outcome} \not\equiv t_{recognize}$$

The notation marks *architectural non-identity*, not guaranteed temporal separation. Two markers may coincide in measured time, but no marker may be substituted for another without an explicit inferential bridge. The architectural commitment is that the six time-markers track structurally distinct events; whether any pair of them coincides empirically is an empirical question the architecture does not legislate.

| Time-marker | Architectural meaning |
|---|---|
| $t_{prep}$ | Substrate preparation, biasing, readiness, affordance formation, or pre-selection accumulator dynamics |
| $t_{select}$ | The operator-bundle selection-event itself — the structural commitment-of-direction that the architecture treats as the decision (per 7.3 minimal definition) |
| $t_{report}$ | Reported awareness of urge, intention, or decision (Libet's W-time; verbal-report onset) |
| $t_{move}$ | Motor onset or implementation onset (Libet's M-time; first detectable behavioral execution) |
| $t_{outcome}$ | External result or sensory consequence of the act |
| $t_{recognize}$ | Post-hoc recognition or ownership-interpretation of the act, possibly differing from initial $t_{report}$ |

The controlling claim:

> *A mismatch between $t_{prep}$, $t_{report}$, and $t_{move}$ is not yet evidence that agency is illusory. It is evidence that preparation, selection, report, implementation, and recognition are temporally separable.*

This is the structural backbone for reading Libet, Soon, Wegner, intentional binding, and inhibition paradigms without the recurring philosophical error of treating any one observable as identical to any of the others. $t_{prep}$ before $t_{report}$ does not entail $t_{select}$ before $t_{report}$. $t_{report}$ before $t_{move}$ does not entail $t_{select}$ at $t_{report}$. A confabulated post-hoc narrative reports a $t_{recognize}$ that may or may not track an actual $t_{select}$. The timing chain forces empirical claims about agency to specify which time-marker they are claiming evidence for, and what the inferential bridge to $t_{select}$ looks like.

*A worked mini-case showing the time-markers separating.* An agent in a deliberative free-choice paradigm is presented with a meaningful option (e.g., choosing between two candidates for a hire decision under genuine evaluative engagement). At $t_{prep}^{(1)}$, prior preference-stability, accumulated relevant information, and salience-of-considerations bias the option-space. At $t_{prep}^{(2)}$, presentation of the choice activates evaluative engagement, projection-toolset, and source-pathway access. At $t_{select}$, the operator-bundle commits to a direction — the structural decision-event. At $t_{report}^{(1)}$, the agent verbally articulates "I'm going with candidate A." At $t_{move}$, the agent's hand moves to indicate the choice (motor implementation). At $t_{outcome}$, the choice is recorded and consequence-relevant action begins (sending the offer letter days later). At $t_{recognize}^{(1)}$, post-action reflective access tracks the source and structure of the decision; at $t_{recognize}^{(2)}$, days or weeks later, the agent may revise the recognition under further reflection. Each time-marker is empirically distinct; collapsing any of them risks misreading the architectural object the paradigm is targeting.

## 10.4 Libet-class paradigms: thin free selection, not free choice proper

The canonical Libet paradigm asks participants to flex a finger or press a button "whenever they feel like it" and to report the time of conscious awareness of the urge or intention via a rotating-clock paradigm. The classic finding: the readiness potential precedes reported conscious intention by several hundred milliseconds.

The architectural reading:

| Libet-paradigm feature | Architectural interpretation |
|---|---|
| Arbitrary spontaneous flex / button-press | Tests **thin free selection** (per 8.3) — Condition 2 evaluative engagement is minimized or task-backgrounded; in some trials it may be implicit or absent |
| "Act whenever you feel like it" | Task-design intentionally minimizes evaluative engagement; the experimenter has selected for thin selection rather than free choice proper |
| Readiness potential before reported intention | Shows $t_{prep}$ before $t_{report}$; does not show $t_{prep}$ before $t_{select}$, because $t_{select}$ is not directly observed in the paradigm |
| W-time report | Reports $t_{report}$, not $t_{select}$; the architecture is committed (per 7.13) to the inferential character of decision-event timing |
| M-time | $t_{move}$, the motor-onset; structurally distinct from $t_{select}$ |
| Veto discussion | Belongs to 8.5 omissive-decision class and 9.9 inhibition-attribution; not to free-agency-as-such |

The controlling reading:

> *Libet-style tasks expose timing dissociations inside thin free selection. They do not directly test free choice proper, wholehearted free choice, constructed-order action, profile-formative agency, or Section 8's broader variation taxonomy.*

The architecture makes no claim that Libet's findings are wrong about $t_{prep}$ preceding $t_{report}$. It claims that this finding is structurally about thin free selection in a low-evaluative-engagement task and does not support the inference that the operator-bundle selection-event $t_{select}$ has been preempted by the substrate. The substrate-preparation finding is consistent with at least four interpretations (developed in 10.6) and does not adjudicate among them on its own.

## 10.5 Soon-class decoding paradigms: prediction, bias, and selection

Soon et al.'s fMRI / decoding paradigms report that prefrontal and parietal patterns can predict the outcome of simple voluntary choices (e.g., left vs right button press) several seconds before the participant's reported awareness of having made the choice. Decoding accuracies are typically modest but reliably above chance.

The architectural reading:

| Soon-paradigm feature | Architectural interpretation |
|---|---|
| Above-chance decoding before reported awareness | Marker of pre-report substrate dynamics or cognitive bias; does not establish that $t_{select}$ has occurred at the decoding-detection time |
| Low-stakes left/right choice | Thin free selection domain (per 8.3); the option-space is intentionally low-contrast and low-evaluative-depth |
| Prefrontal / parietal patterning | Possible preparation, option-biasing, scaffolded task-set activity, or partial accumulation toward selection — not necessarily completed selection |
| Delay between decoding and conscious report | Report-lag pattern; consistent with $t_{prep}$ before $t_{report}$ without entailing $t_{prep}$ before $t_{select}$ |
| Prediction accuracy below perfect determination | Should be read as partial signal extraction, not as full sourcehood-replacement; partial predictability does not establish full pre-selection |

The architectural discipline:

> *Predictability of a later reported selection is not identical to bypass of the operator-bundle. Pre-selection biases, accumulator-style preparation, and task-set patterning are all structurally compatible with operator-bundle selection at a later time, on a later substrate-state, drawing on the prepared materials.*

Section 10 does not claim the Soon findings are explained away. It claims that the inferential bridge from "above-chance pre-report decoding" to "the operator-bundle has been preempted" requires architectural commitments the paradigm does not by itself supply. Candidate Section 11 operationalization: prediction-lead-time patterns may vary with option-space richness, evaluative engagement, and order-profile (foundational vs constructed-order decisions). Section 10 surfaces this as an empirical interpretation candidate; Section 11 must decide whether to promote it to a formal prediction.

## 10.6 Readiness-potential alternatives: preparation is not preemption

This subsection prevents the paper from acting as though the Libet readiness potential has only one architectural interpretation. The architectural claim is implementation-neutral: the architecture's reading of Libet does not depend on which RP-interpretation is correct.

| Interpretation | Architectural status |
|---|---|
| **RP as unconscious decision** | Possible interpretation, but not forced by the data; would require additional inferential commitments the paradigm itself does not establish |
| **RP as preparatory affordance / bias** | Compatible with operator-bundle selection at a later substrate-state; preparation is one input to selection, not a substitute for it |
| **RP as stochastic accumulator** | Schurger and colleagues have argued the RP can be modeled as the average of stochastic neural fluctuations crossing a threshold for spontaneous voluntary movement. On this reading, the RP reflects threshold-crossing dynamics rather than a discrete unconscious decision-event. Compatible with the architecture's structural commitments. This does not require the architecture to claim that every RP *is* stochastic accumulator activity; the point is that RP-as-unconscious-decision is not forced by the paradigm alone, and accumulator modeling is one viable alternative among the four |
| **RP as task-set artifact** | The Libet task installs a conditional intention to press at a self-selected moment. The RP may track task-set expression rather than a free-floating decision-event. Compatible with thin free selection |

The controlling architectural discriminator:

> *Preparation becomes agency-threatening only when it amounts to preemption, bypass, or capture under Condition 4. Preparation alone is substrate coupling — and substrate coupling is what Condition 4 requires intact (non-preemptive), not absent.*

This is one of the most architecturally consequential claims in Section 10. The architecture does not deny that substrate dynamics precede selection; it specifies the structural relationship between substrate-preparation and operator-bundle-selection. Preparation supplies the readiness, accumulator state, biasing, and option-space-presentation that the selection-event then operates on. Selection without prepared substrate is structurally incoherent. What would threaten agency is *preemption* — the substrate completing the act without operator-bundle engagement (per 8.8 compulsion / capture) — not preparation as such.

## 10.7 Wegner-class paradigms: apparent will, post-hoc recognition, and confabulation

Wegner and Wheatley's apparent mental causation account treats the experience of will as arising when a thought is interpreted as causing an action under conditions of priority (thought before action), consistency (thought content matches action content), and exclusivity (no obvious alternative cause). Their paradigms (the "I-spy" / Ouija-board paradigm and related setups) engineer configurations in which participants report authorship of actions they did not actually generate, or report non-authorship of actions they did generate.

The architectural translation:

| Wegner concept | Architectural translation |
|---|---|
| **Priority** | Thought temporally precedes action / outcome; structurally separate from $t_{select}$ |
| **Consistency** | Thought content matches action / outcome; consistency-cue may support correct or incorrect ownership-attribution |
| **Exclusivity** | No obvious alternative cause is available; attribution-cue varies with the salience field |
| **Apparent mental causation** | Possible post-hoc ownership-recognition, source-opaque ownership, or confabulated source-report — three architecturally distinct cases |
| **Illusion of will** | Not one architectural object — may be false source-report, false ownership, or true ownership with source-opacity; the case must be specified |

The critical distinction (preserved from 7.9, 8.14, 9.7):

> *Post-hoc recognition is not confabulation by default.*

Section 10 splits Wegner-paradigm cases into five distinct configurations:

| Configuration | Report status |
|---|---|
| Post-hoc recognition | The I correctly recognizes an owned action after $t_{select}$ has occurred; $t_{recognize}$ tracks an actual selection-event |
| Source-opacity | The action is owned (Condition 6 intact), but the source-pathway is conscious-fuzzy or low-$\phi$; the agent cannot reliably articulate why they selected as they did, without the act being unowned |
| Confabulation | $\phi$-narrative supplies apparent source-access for a process that was absent, bypassed, or differently-structured than the narrative reports; $t_{recognize}$ may fail to track the actual source, timing, content, or ownership-relation of $t_{select}$, even where an actual selection-event occurred |
| Alienated action | Ownership itself fails (Condition 6 compromised); the action is observed but not integrated as the I's |
| Imposed / engineered action | Source and ownership may both fail or be externally structured (e.g., the I-spy paradigm's experimental engineering of pseudo-authorship) |

*Choice-blindness paradigms* (Johansson and colleagues) — in which participants are presented with a choice they did not make and asked to justify it, often producing detailed justifications consistent with confident authorship — fit naturally into the confabulation category above. The architecture's reading is that choice-blindness paradigms confirm that *some* reports of authorship are confabulated; they do not establish that *all* reports of authorship are confabulated. Importantly, choice-blindness paradigms typically involve a real prior selection-event that the participant actually performed (selecting between two faces, two political positions, etc.); what is confabulated is the later source / content / justification narration after the experimenter swaps the recorded outcome. The actual $t_{select}$ occurred; what fails to track it is the post-hoc narration once the swap is in place. The architecture's three-way distinction (post-hoc recognition vs source-opacity vs confabulation) is precisely the apparatus needed to keep choice-blindness from sliding into general agency-skepticism.

## 10.8 Intentional binding and outcome-coupling

Intentional binding refers to the subjective compression of the perceived interval between voluntary action and sensory consequence, compared to passive or non-self-initiated movements. The effect is taken in some literatures as a sense-of-agency marker.

The architectural reading:

| Empirical marker | What it can indicate | What it cannot establish |
|---|---|---|
| Intentional binding present | Action-outcome coupling; ownership- and outcome-coupling cue; expected-control structure (the agent's act and the outcome are integrated as a coupled event) | Free choice proper; full responsibility; absence of source-compromise |
| Reduced intentional binding | Weakened outcome-coupling; uncertainty about authorship; alienation; low predictability of one's own act | Absence of agency or absence of ownership by themselves |
| Strong binding under manipulation | Possible source-compromised ownership with intact ownership-feeling, or prediction-induced ownership-attribution | Source-clean agency |
| Binding under automatism | Possible compiled action, habit, or capture (per 8.7, 8.8) | Decision-event presence; responsibility |

The controlling claim:

> *Intentional binding is an outcome-coupling marker, not a direct agency-meter.*

Binding tracks the coupling between action and outcome and the predictive integration of one's own act with its consequence. It correlates with sense-of-agency in many configurations but does not by itself differentiate among the architectural configurations the paper has developed: free choice proper, thin free selection, owned-but-source-compromised action, mastered automaticity, captured habit. Each of these can produce binding-effects of different strengths under different conditions. The paradigm is informative as one signal among many; it does not replace the structural decomposition.

## 10.9 Inhibition, veto, withholding, and "free won't"

Voluntary inhibition paradigms (stop-signal tasks, intentional inhibition tasks, Libet-veto tasks) probe the agent's capacity to interrupt or withhold an emerging course of action.

The architectural map:

| Empirical paradigm | Architectural object |
|---|---|
| Last-moment veto (Libet's "free won't") | Withholding / omissive decision (per 8.5, 9.9); the operator-bundle commits to non-action late in the implementation timeline |
| Stop-signal inhibition | Substrate-control and action-interruption; tests Condition 4 substrate-coupling at the implementation stage |
| Intentional inhibition | Decision over non-action or interruption as a structurally distinct selected course |
| Failed inhibition | Could be compulsion (8.8 substrate capture), insufficient time (substrate dynamics outpacing selection), weak toolset, task mismatch, or attentional slip |
| Repeated successful inhibition | Compatible with sustained operator-bundle direction over an inhibition-window — agency-supportive rather than agency-threatening |

The discipline (extending 9.9):

> *Withholding is not the absence of agency; it is an agency-object when non-action is live, selected, and implementable. Failed inhibition is not the absence of agency either; it is a configuration whose architectural reading depends on whether substrate dynamics preempted selection (compulsion) or selection occurred but implementation could not catch it (timing-limited).*

The voluntary-inhibition literature gives the architecture an empirical handle on the omissive-decision class established in 8.5 and the four-way separation of 7.10. Decision (to inhibit) and action (the inhibition) and outcome (the absence of the original action) are dissociable; failed inhibition may show decision-without-action, while successful unintended action may show action-without-decision.

## 10.10 Effort markers: resistance, cost, and agency-quality

Section 6.4's resistance taxonomy (eight resistance-sources) and Section 6.8's effort/agency-quality separation supply the architecture's effort-reading of empirical markers.

| Marker-family | Possible architectural meaning |
|---|---|
| **Reaction time** | Conflict, uncertainty, complexity, inhibition, task difficulty, toolset weakness, or option-space depth — none specific to agency-quality |
| **Error rate** | Poor coupling, poor option-construction, degraded evaluation, fatigue, salience capture — error-rate alone doesn't distinguish among these |
| **Subjective effort report** | Phenomenological cost-profile under resistance; not objective agency-strength |
| **Physiological arousal** | Affect / threat / resistance signal; not necessarily willing |
| **Persistence under difficulty** | Effort-sustainment capacity; not necessarily free choice proper |
| **Low effort** | Mastery, automaticity, habit, capture, or transient unavailability of high-effort engagement (per 6.8 markers, particularly substrate-coupling/preemption discriminator) |

The discipline (preserved from 6.8 and 8.17):

> *High effort is not morally better agency. Low effort is not weaker agency. Effort tracks resistance-to-direction under operator-bundle commitment; it must be read alongside source-status, substrate-coupling, ownership, and Mode B availability before any agency-quality interpretation is licensed.*

Section 10's effort-reading is empirical-interpretation, not normative evaluation. A persistence task that participants find effortful is supplying a resistance-signal; what kind of resistance (cognitive, affective, motivational, substrate, source-compromised, projection-collapsed) is what the diagnostic schema must surface.

## 10.11 Flow, mastery, habit, and automaticity

Empirical flow research, expertise studies, habit-acquisition paradigms, and automaticity research all engage low-effort, low-deliberation configurations that the literature sometimes treats as agency-threatening. The architecture preserves the Section 7 / Section 8 commitment that low effort is not agency-absence by default.

| Configuration | Empirical appearance | Architectural reading |
|---|---|---|
| **Mastery** | Fast, low-effort, fluent, compressed deliberation | Can be highly agentic; mastered-domain free selection (per 5.7, 7.7) |
| **Habit** | Repeated, compiled, context-triggered | May be owned, thin, compulsive, or source-compromised depending on overlays (per 8.7) |
| **Flow** | Low self-monitoring, high performance | Mode B exercise may be low while Mode B availability remains intact (per 7.5) — agency-compatible |
| **Automatic capture** | Fast, low-reflection action | Possible Condition 4 capture (per 8.8) — agency-compromised |
| **Reflex** | Fast substrate response | Non-agency or boundary case (per 8.18) |

The controlling claim (preserved from 7.5 and 8.17):

> *Reduced explicit deliberation is not reduced agency by default. Mode B availability ≠ Mode B exercise.*

Flow research particularly benefits from the architecture's distinction. The paradigmatic flow-state involves reduced reflective self-monitoring during action; on a crude reading this would entail diminished agency. The architecture's reading: flow is a configuration in which Mode B availability is preserved (the agent can reflect on the act after, under intact conditions) while Mode B exercise during action is appropriately low because reflection-during-execution would disrupt performance. Agency-compatible flow versus agency-compromised automaticity-capture is distinguished by substrate-coupling/preemption status (per 6.8 marker), not by effort or by deliberation-during-action.

## 10.12 Diminished-agency paradigms: compulsion, addiction, ADHD-like, learned helplessness

Empirical paradigms in compulsion, addiction, ADHD-like dynamics, learned helplessness, and depression engage Section 8's diminished-agency variation-families. Section 10's role is empirical-interface only — mapping experimental findings to condition-profiles, not making clinical claims stronger than the architecture can support.

| Domain | Empirical focus | Architecture lens |
|---|---|---|
| **Compulsion / addiction** | Cue-reactivity, inhibition failure, relapse rates, craving paradigms | C4 capture (per 8.8); source-pressure; mitigation-availability; the Mode B asymmetry per 7.6 (objection available, capture-domain control unavailable) |
| **ADHD-like implementation gap** | Sustained execution, dynamic refinement under duration, task-switching, initiation latency | C1 / C3 / C4 / effort-economy interactions (per 8.9); substrate-developmental constraint at orders 1–2; Mode B may be available for identifying the gap while not being reliably sufficient to overcome sustained implementation failure under current conditions per 7.6 / 8.9 |
| **Learned helplessness** | Failure to initiate escape effort after uncontrollability training | Projection-toolset damage (per 8.11); live-option contraction; conceptual recognition does not by itself repair the projection-toolset |
| **Depression / anhedonia** | Low initiation rates, low reward-sensitivity, future-collapse in projection tasks | Affect-mediated agency contraction (per 8.12); multi-order action-space contraction; not collapsed into laziness or moral failure |
| **Anxiety / threat-projection** | Avoidance, overchecking, paralysis, decision-latency under threat | PCE-dominant contraction; deliberation-pathology (per 8.10); option-space contraction under threat-projection |

The discipline:

> *Clinical or quasi-clinical paradigms reveal agency-configuration changes; they do not by themselves assign responsibility, excuse, pathology, or blame. Section 9 owns the responsibility-attribution work; Section 10 reads the empirical patterns through the variation taxonomy.*

The architecture's distinctive contribution to this empirical literature is the diminished-agency relocation framework from 9.8: diminished agency does not produce one responsibility result but a relocation problem, and the relocation depends on which conditions are compromised, which overlays apply, and what mitigation / repair / prior-avoidance options were live. Empirical paradigms can detect the configuration; responsibility-attribution requires the further overlay analysis Section 9 supplies.

## 10.13 Affect-mediated agency modulation

This subsection integrates the *Differentiated Affect* paper's apparatus without redoing it. Affect modulates agency by altering $\Pi$-weighting, projection-toolset availability, action-pathway construction, source-access, salience, and substrate resistance — the affect paper supplies the affect-side taxonomy, Section 10 reads empirical paradigms in which affect shifts agency-relevant outputs.

| Affect-domain | Agency effect in empirical paradigms |
|---|---|
| Fear / anxiety | Option-space contraction, threat-weighted projection, decision-latency increases under threat-priming |
| Shame | PtCns pressure and self-frame disruption; inhabitability collapses for self-expressive options under exposure manipulations |
| Anger | Boundary-operation engaged; action-readiness increases; threshold for impulsive selection decreases |
| Pain | Substrate-dominant salience; attentional capture; reduced cognitive resource for projection-toolset operation |
| Trauma-cue activation | Source-opaque agency contraction; possible C4 pressure; differential post-hoc recognition latency for trauma-relevant content |
| Boredom / anhedonia | Salience / projection / initiation impairment; reduced action-spontaneity in unconstrained tasks |

The controlling guardrail:

> *Affect is an agency-modifier, not an automatic agency-negator. Empirical paradigms that document affect-mediated changes in decision-latency, option-availability, or response-patterns are reading agency-modulation, not agency-elimination.*

Section 10's role is to read the affect-and-agency empirical literature through the modifier-not-negator framing. The clinical and experimental literature on affect's effects on decision-making is rich; the architecture's contribution is to disaggregate which agency-component each affect-effect targets — option-space contraction, evaluative-engagement disruption, projection-toolset compromise, substrate resistance, salience-redirection — rather than treating "affect impairs agency" as a single claim.

## 10.14 Social, constructed-order, and manipulation paradigms

The architecture has a major advantage in this domain because it has dedicated apparatus for constructed-order action (Section 5.7), the manipulation continuum (Section 5.9), and the manipulator-vs-manipulated-agent attribution split ([Free Will §4.3]). Empirical paradigms on compliance, obedience, priming, persuasion, propaganda, and group-coordination engage this apparatus directly.

| Paradigm-family | Architectural lens |
|---|---|
| **Compliance / obedience (Milgram-class)** | Authority-structured compliance; option-space and evaluation may be shaped by role-pressure, instruction, threat, or sanction. Ownership may remain; coercion / constrained-choice classification requires specific threat and option-space analysis (per 8.4, 9.5) — Milgram-class paradigms are not by default coerced choice without examination of the actual threat-structure, role-pressure intensity, and live-option configuration |
| **Priming / nudging** | Ranges from transparent scaffold to mild source-compromise to manipulative option-shaping. Ownership may remain; source-status depends on transparency, alternatives, source-access, and whether verification-capacity is bypassed (per 5.9 manipulation continuum) |
| **Persuasion / propaganda** | Transparent persuasion can be source-clean or autonomy-supporting; propaganda / manipulative persuasion becomes distributed source-shaping where it obscures source-status, suppresses alternatives, or compromises verification (per 9.12 acute vs distributed manipulation) — the distinction is not order-level but transparency, alternative-availability, and source-access |
| **Therapy / coaching / teaching** | Constructed-order toolkit-shaping (per 8.16); autonomy-supporting where transparency, alternatives, and recipient-aim alignment hold; manipulative where source-status is compromised |
| **Institutional decision-making** | Role-indexed option-space; constrained constructed-order agency; bureaucratic capture per 8.16 / 9.13 |
| **Group coordination** | Distributed profile-indexed agency (per 9.13); no group-mind posit; collective configuration is the joint pattern of perspective-anchored agencies |

The controlling architectural claim:

> *Social influence paradigms are not merely "bias" paradigms. They test constructed-order source-shaping, option-space control, and ownership / sourcehood dissociation — and the architecture's apparatus is engineered to read them as such.*

This subsection connects back to Section 9's manipulation apparatus and the manipulator / manipulated-agent attribution split. The empirical literature on social influence often describes findings as "people are influenced by their environment" or "judgments are biased by context." The architecture's reading sharpens this: which agency-component is the influence targeting (option-space construction, evaluative engagement, source-access, ownership-integration), and what is the structural relationship between the influencing agent's constructed-order act and the influenced agent's agency-configuration?

## 10.15 Cascade and longitudinal empirical designs

Section 9's cascade-attribution apparatus is responsibility-oriented. Section 10 translates cascade into empirical-design language, generating a distinctive contribution: *some agency phenomena cannot be tested in single-trial paradigms because their object is profile-formation across time.*

| Cascade stage | Empirical design target |
|---|---|
| **Stage 1 — Self-imprinting** | Practice effects, habit formation, self-training paradigms, repeated choice under feedback, affective conditioning, expertise development; the agent's own substrate and toolkit are reshaped by repeated bundle-mediated acts |
| **Stage 2 — Output to others / environment** | Social consequence paradigms, tool-use studies, communication and leadership paradigms, manipulation outcome-studies; the agent's act produces effects on not-I structures that may feed back |
| **Stage 3 — Feedback closure** | Reinforcement loops, identity-update paradigms, learned-helplessness loops, addiction-cycle studies, institutional capture; Stage 1 imprints feed back as input-imprinting completing the cascade |

The controlling claim:

> *Single-trial paradigms are structurally limited for cascade phenomena, not useless. The architecture predicts that some agency-phenomena (habit formation, identity update, scaffold capture, learned helplessness, source-compromise persistence) require longitudinal designs because their architectural object is profile-formation over time, not selection at a moment.*

This is one of Section 10's most distinctive contributions. The empirical literature on agency has historically privileged single-trial paradigms (Libet, Soon, Wegner, intentional binding, stop-signal). The architecture's reading is that this privilege has structural costs: phenomena like cascade-perpetuation (per 5.6), profile-formative configurational decisions (per 7.11), self-perpetuating loops within habit (per 8.7), maladaptive toolkit-development (per 5.5), and scaffold-captured developmental-window cells (per 9.6) are temporally extended and cannot be probed by single-trial paradigms without losing their architectural object. Longitudinal designs, training studies, repeated-measures clinical paradigms, and developmental research engage these architectural objects directly.

*A worked longitudinal design: habit-training cascade.* An agent commits to a daily exercise routine (a configurational decision per 7.11). The empirical-design measurement targets across a six-month window: at $t_0$, baseline measurement of effort-cost per session ($M_s$ = subjective-effort report; $P_o$ = trying-as-attribution-object), substrate-resistance markers ($M_s$ = behavioral / physiological), Mode B reflective access to the routine ($B_x$). At $t_{1...n}$ across the training period, repeated-measures of the same axes plus self-imprinting markers ($M_s$ = compliance trajectory, automaticity development, salience shifts toward exercise-relevant cues). Stage 2 cascade-effects measurable in environmental and social ecology (gym attendance shaping community, exercise-talk shaping family habits). Stage 3 feedback closure measurable in the agent's own profile-state changes (identity-update — "I am someone who exercises"; salience-restructuring — exercise-skipping now generates dissonance that previously did not). At $t_{6mo}$, the architectural object measurable: profile-formation has occurred — the agent's compound-configuration (per 8.19) at six months differs structurally from the agent at $t_0$, with the cascade visible across all three stages. The single-trial paradigm cannot capture this; the longitudinal design can. Comparable designs apply to addiction-cycle studies (Stage 1 self-imprinting through repeated cue-driven use, Stage 2 social and environmental output, Stage 3 feedback closure as identity and salience reshape), learned-helplessness paradigms (uncontrollability training producing projection-toolset damage that propagates across novel control situations), and scaffold-capture longitudinal studies (sustained ideological or institutional source-shaping over developmental windows).

## 10.16 Bad inferences Section 10 rules out

The architecture's anti-overinterpretation guardrail. Each row pairs a common bad inference from the empirical literature with the architectural correction.

| Bad inference | Architectural correction |
|---|---|
| Neural preparation before report means no agency | Preparation is not preemption (per 10.6); $t_{prep}$ before $t_{report}$ does not entail $t_{prep}$ before $t_{select}$ |
| Report-lag means confabulation | Post-hoc recognition is not confabulation by default (per 7.9, 9.7, 10.7); the three-way distinction must be applied |
| Predictability of choice means unfreedom | Predictability is compatible with many agency-configurations including thin selection, mastery, source-clean choice under stable preferences; predictability is one signal not an agency-meter |
| Arbitrary button press tests free choice generally | Button-press paradigms typically test thin free selection, not free choice proper, wholehearted free choice, or constructed-order agency (per 8.3, 10.4) |
| Low deliberation means low agency | Mastery and flow often involve reduced deliberation while preserving Mode B availability; agency-quality requires the substrate-coupling overlay (per 7.5, 10.11) |
| High effort means strong agency | Effort tracks resistance under operator-bundle commitment, not agency-quality (per 6.8, 10.10) |
| Action-outcome binding proves free will | Binding tracks coupling and ownership-cues; not direct agency-measurement (per 10.8) |
| Failed action means failed willing | Decision, trying, action, and outcome are dissociable per 7.10; failure can occur at any of the four with different agency-implications |
| Clinical impairment means no responsibility | That is Section 9 attribution work, not Section 10 empirical-classification (per 10.12, 9.8) |
| Social influence means no ownership | Manipulation is not ownership-failure by default per 8.15, 9.5; ownership-and-sourcehood dissociation is the apparatus the architecture supplies for these cases |
| Confabulation in some cases means confabulation in all cases | The architecture's three-way distinction (post-hoc recognition / source-opacity / confabulation) prevents this slide; choice-blindness paradigms confirm some confabulation, not all (per 10.7) |

This table is one of the most reader-facing pieces in Section 10. Its purpose is to give the empirically-engaged reader an explicit list of inferences the architecture rules out, so that subsequent encounters with the empirical literature can be filtered through the architectural discipline.

## 10.17 Empirical patterns that would challenge the architecture

The architecture must specify what would pressure it. This subsection makes the architecture's empirical commitments falsifiable in the spirit of the *Differentiated Affect* paper's parallel section. Five patterns would be difficult for the architecture to accommodate:

**Pattern 1: High-accuracy, content-specific prediction of rich deliberative choices before relevant option-construction and evaluative engagement.** If pre-report neural or behavioral signals reliably predicted rich, evaluatively-engaged free choice proper — not merely stable preferences, prior profile-commitments, task-set biases, or known value-rankings — at lead-times incompatible with any plausible operator-bundle engagement, the architecture's thin-selection / free-choice-proper distinction would lose empirical traction. The threatening case is *not* ordinary predictability from stable character (a person known to value honesty being predicted to behave honestly is not architecturally pressuring); it is content-specific selection-decoding before the architectural choice-structure could have operated. The architecture's distinctive thin-selection / rich-choice contrast presupposes that selection in rich-choice configurations engages structural elements (option-space construction, projection-toolset operation, source-pathway access, evaluative integration) that are not yet present at the lead-times Soon-class paradigms detect; if rich-choice content-decoding became available at those lead-times, the contrast would collapse. The architecture would need to either accommodate strong content-specific predictability in rich choices or revise its commitment that thin and rich choices are architecturally distinct.

**Pattern 2: No multi-marker distinction between thin arbitrary selection and wholehearted free choice.** If paradigms comparing arbitrary spontaneous movements with thick, evaluatively-engaged, source-clean, ownership-integrated choices found *no differences* across the relevant $EIP_p$ axes — task-structure, report-structure, evaluative-engagement markers, Mode B access, ownership-and-source reports, and neural-temporal dynamics — then the architecture's thin-vs-wholehearted distinction would lose empirical traction. Identical motor-readiness patterns alone would *not* be sufficient grounds for falsification, because final motor preparation may be shared across structurally different choices: implementation-neutrality blocks any claim that the architecture requires a distinct neural RP signature for wholehearted choice. What would pressure the architecture is *uniformity across multiple architecturally-distinct measurement axes* — uniform reports, uniform reflective-access patterns, uniform source-status indicators, uniform integrative dynamics — at which point the thin / wholehearted distinction would be doing no empirical work.

**Pattern 3: No dissociability among ownership-reports, source-access reports, and external source-manipulation markers.** The architecture's manipulation-not-ownership-failure-by-default discipline (per 8.15, 9.5) predicts that ownership and sourcehood are architecturally separable: a manipulated agent may own an act (Condition 6 intact) while the source-pathway is compromised by the manipulator's structuring of the option-space. If well-designed manipulation paradigms never produced source-compromised-but-owned configurations — that is, if ownership reports always rose and fell exactly with source-cleanliness and source-access under manipulative conditions, with no detectable dissociation between the ownership-axis and the source-status axis — the architecture's ownership / sourcehood separation would lose empirical traction. The discriminator is *ownership/sourcehood* dissociation, not *ownership/outcome-success* dissociation, which is a different empirical relationship.

**Pattern 4: No detectable recognition-timing or source-report difference between source-clean and source-compromised decisions.** By analogy with recognition-lag patterns documented in *Differentiated Affect* (especially in love-onset / love-ending configurations where affective-topology recognition lags actual behavioral signature) and through the agency-source analysis of 9.7 and 10.7, the architecture expects source-opaque or source-compromised decisions to *sometimes* differ from source-clean decisions in post-hoc recognition timing, source-report stability, or source-access confidence. The expectation is sometimes-differential, not uniformly-differential. If paradigms designed to isolate source-status reliably found no such difference across well-designed source-manipulation conditions, the source-status overlay would lose empirical traction at the recognition-and-report level.

**Pattern 5: Mode B object-domain asymmetry patterns that do not track expected architectural distinctions.** The architecture predicts that Mode B object-domain availability is order-asymmetric (per 7.6) — third-order substrate-action, constructed-order coordination, and source-pathway access should show systematically different reflective-availability patterns than second-order thought. If empirical paradigms found Mode B availability uniform across these domains, or asymmetric in patterns that do not track the architectural distinctions, the order-asymmetric Mode B framework would lose empirical traction.

The discipline:

> *Section 10 specifies what would pressure the architecture, not just what the architecture predicts. The empirical-interface section must include the falsification commitments to be more than architectural advocacy.*

The five patterns are not exhaustive. Section 11 will engage which of the architecture's commitments translate into formal predictions; Section 12 will engage open empirical problems. Section 10's contribution is to identify, in advance and explicitly, the empirical patterns that would require the architecture to revise, qualify, or retract its commitments.

## 10.18 Summary: empirical paradigms × architectural target

The synthesis. Each major paradigm-family is mapped to its primary architectural target, with the controlling discipline that no single paradigm tests "free will" simpliciter.

| Paradigm family | Primary architectural target |
|---|---|
| Libet readiness-potential tasks | Timing dissociation among $t_{prep}$, $t_{report}$, $t_{move}$ within thin free selection; not free choice proper |
| Soon decoding tasks | Pre-report bias / preparation / task-set patterning; not direct evidence of completed selection |
| Wegner apparent-will tasks | Post-hoc recognition vs source-opacity vs confabulation; ownership-report under engineered conditions |
| Intentional binding | Action-outcome coupling and ownership-cues; not direct agency-measurement |
| Veto / inhibition tasks | Withholding / refusal / interruption / omissive decision (per 8.5, 9.9) |
| Stop-signal / control tasks | Condition 4 substrate-coupling and interruption capacity |
| Effort / persistence tasks | Resistance-source and cost-profile, not agency-quality by itself (per 6.8, 6.4) |
| Flow / mastery tasks | Low-effort agency or automaticity depending on substrate-coupling status; Mode B availability vs exercise distinction |
| Habit / automaticity tasks | Compiled willing vs capture vs reflex (per 8.7, 8.18) |
| Addiction / compulsion tasks | C4 capture; live mitigation availability; source-pressure |
| ADHD-like implementation tasks | Dynamic-refinement; sustained operator-bundle direction at orders 1–2; effort-economy |
| Learned helplessness tasks | Projection-toolset impairment; live-option collapse |
| Affect / threat tasks | State-dependent toolkit contraction or expansion; agency-modifier not agency-negator |
| Social influence / manipulation tasks | Source-compromise; ownership / sourcehood dissociation; source-access reports; constructed-order source-shaping |
| Choice blindness paradigms | Confabulation as one configuration of the post-hoc-recognition / source-opacity / confabulation triad; not all reports confabulated |
| Longitudinal training / identity-change tasks | Profile-formation; cascade dynamics; self-perpetuating loops |

The closing claim:

> *Section 10 does not claim that the empirical literature has confirmed the architecture. It claims that the architecture supplies a disciplined map for interpreting what empirical paradigms actually measure and what they cannot measure. The thin-vs-wholehearted distinction, the timing-marker non-identity chain, the Mode B asymmetry, the post-hoc / source-opacity / confabulation triad, the ownership / sourcehood dissociation, the cascade longitudinal apparatus, and the falsification conditions of 10.17 together establish the architecture's empirical posture: it is interpretively constraining, prediction-ready, and falsification-oriented, while remaining implementation-neutral and refusing the move that any single paradigm settles the agency question.*


---

# 11. Predictions and operationalization: from empirical interface to discriminating tests

Section 10 established that empirical paradigms do not measure agency-as-such; they measure narrower architectural objects through proxies. Section 11 asks the next question: which of those mappings produce testable commitments? The architecture becomes empirically substantive only where its structural distinctions generate discriminating patterns — patterns that would not be equally predicted by simple voluntarism, neural-preemption views, pure confabulation theories, effort-based agency models, ownership-only theories, generic executive-control frameworks, or undifferentiated social-influence accounts.

Section 11 promotes selected operationalization candidates from Sections 5–10 into formal predictions. Each promoted prediction has an architectural source, candidate empirical markers, a discriminator target (the alternative theory or simpler model the prediction differentiates the architecture from), a pressure or failure condition, and an exclusion list. The section also specifies what the architecture explicitly does *not* predict, and what empirical patterns would most directly pressure its core commitments.

The boundary discipline holds. Section 9 attributes responsibility. Section 10 interprets paradigms. Section 11 promotes operationalization candidates into formal predictions and specifies pressure conditions. [Free Will §5] engages alternative philosophical and scientific frameworks. Section 12 surfaces open problems. Section 11 does *not* perform Section 9, 10, [Free Will §5] (translations), or 12 (open problems) work.

## 11.1 From empirical interpretation to formal prediction

Section 10's central methodological commitment was that empirical paradigms test markers of architectural objects through proxies, not architectural objects directly. The Section 10 / Section 11 handoff converts that interpretive work into commitment work:

| Section 10 architectural object | Section 11 question |
|---|---|
| Timing-marker non-identity ($t_{prep} \not\equiv t_{select} \not\equiv t_{report} \not\equiv t_{move} \not\equiv t_{outcome} \not\equiv t_{recognize}$) | Do different agency-configurations produce systematically different timing / report / marker profiles? |
| Thin free selection vs free choice proper vs wholehearted choice | Do thin selections and free choice proper diverge across multi-marker profiles, not just one privileged signal? |
| Post-hoc recognition / source-opacity / confabulation triad | Can the three configurations be empirically separated under appropriate paradigms? |
| Ownership / sourcehood dissociation | Can ownership remain high while source-status is independently compromised under manipulation? |
| Mode B object-domain availability (order-asymmetric) | Can reflective access be domain-specific rather than global? |
| Effort / agency-quality separation | Does effort-level dissociate from agency-quality markers? |
| Cascade and profile-formation (longitudinal) | Do longitudinal designs reveal profile-formation phenomena unavailable to single-trial paradigms? |

The controlling claim:

> *Section 11 tests the architecture's structural distinctions, not "free will" as an undifferentiated object. A prediction earns Section 11 status only if it would distinguish the architecture from at least one plausible alternative.*

Section 11 does not claim its predictions are already confirmed. It states what the architecture is committed to expecting if its structural distinctions are empirically real. The pressure conditions specify what would weaken, qualify, or force revision of those commitments.

## 11.2 Prediction-status criteria

Not every interesting empirical idea earns formal prediction-status. A candidate operationalization from Sections 5–10 is promoted to Section 11 prediction-status only if it satisfies four criteria:

| Criterion | Requirement |
|---|---|
| **Architectural derivability** | The prediction follows from the structural commitments of Sections 3–10, not from an ad hoc empirical hunch or a generic agency-theory claim |
| **Operational marker** | The prediction can be attached to observable, reportable, behavioral, longitudinal, social, or clinical-adjacent proxies; the proxies need not directly observe the architectural object but must bear on it through specified inferential bridges |
| **Discriminator value** | The prediction distinguishes the architecture from at least one live alternative (simple voluntarism, neural-preemption views, pure confabulation theories, effort-based models, ownership-only models, generic executive-control accounts, or undifferentiated social-influence frameworks) |
| **Pressure condition** | The prediction specifies what observation pattern would weaken, qualify, or force revision; predictions without pressure conditions are coherence-claims, not predictions |

A compact formulation:

> *Prediction = structural distinction + operational marker + discriminator + pressure condition + exclusion.*

A prediction may be probabilistic, pattern-level, or multi-marker rather than single-variable. It need not reduce to one effect-size or one significance-test. But it must be more than a post-hoc interpretive compatibility claim. Predictions that all major frameworks make are not discriminating and are not promoted regardless of how architecturally satisfying they would be to confirm.

Two further constraints follow from prior sections:

*The architecture is implementation-neutral on substrate.* A prediction must not require a unique neural signature for an architectural distinction, since substrate-level implementation is an open empirical question the architecture does not legislate. What the architecture predicts at the implementation level is *pattern-uniformity-or-divergence* across multiple architecturally-distinct measurement axes, not specific neural signatures.

*The architecture does not legislate folk-psychological judgments.* "People will assign less blame to manipulated agents" is a prediction about how human beings will use the architecture's structural inputs, not a prediction of the architecture itself. The architecture predicts structural dissociations, condition-profile relationships, and pattern-divergences across configurations. Folk-psychological judgments are downstream of those structural facts and are not Section 11's concern.

## 11.3 The Prediction Profile and the seven prediction families

Each Section 11 prediction is specified through a prediction profile object $PP_i$:

$$PP_i = \langle S, T, M, D, C, F, E \rangle$$

where:

| Component | What it specifies |
|---|---|
| $S$ — Structural source | Which architectural distinction generates the prediction |
| $T$ — Target architectural object | Which architectural object is being tested through proxies (option-space, selection, report, ownership, sourcehood, Mode B, effort, cascade, profile-formation) |
| $M$ — Marker set | Candidate empirical markers — behavioral, report-based, temporal, longitudinal, social, clinical-adjacent |
| $D$ — Domain | Lab task, longitudinal design, clinical-adjacent paradigm, social-influence paradigm, developmental design |
| $C$ — Comparator | Alternative theory or simpler model the prediction distinguishes the architecture from |
| $F$ — Failure / pressure condition | What observation pattern would weaken or force revision of the prediction |
| $E$ — Exclusions | What the prediction does *not* claim |

The $PP_i$ profile is parallel to Section 9's ten-component $AP_{m,t;a}$ attribution profile and Section 10's eight-component $EIP_p$ empirical interpretation profile. The three profiles do different jobs at different sections: $AP$ computes attribution, $EIP$ identifies what an empirical paradigm measures, $PP$ promotes operationalizations into discriminating predictions. They share architectural lineage but are not interchangeable.

The eighteen Section 11 predictions group into seven families:

| Family | Predictions | Core architectural distinction |
|---|---|---|
| **A.** Timing and tier structure | P1–P3 | Thin free selection vs free choice proper vs wholehearted choice; preparation vs selection |
| **B.** Report, recognition, ownership, sourcehood | P4–P6 | Post-hoc recognition / source-opacity / confabulation; ownership ≠ sourcehood |
| **C.** Mode B and order-asymmetry | P7–P8 | Mode B availability is domain-specific, not global; availability ≠ exercise |
| **D.** Effort, mastery, habit, automaticity | P9–P11 | Effort ≠ agency-quality; low effort has multiple structural sources |
| **E.** Diminished agency and toolkit damage | P12–P14 | ADHD-like, learned helplessness, and order-matched intervention have distinct structural profiles |
| **F.** Affect, social source-shaping, constructed-order | P15–P17 | Affect modifies agency by operator-type; social influence varies by source-status; collective responsibility is profile-indexed |
| **G.** Cascade and profile-formation | P18 | Longitudinal profile-formation cannot be captured by single-trial paradigms |

Seven of the eighteen predictions carry the section's argumentative weight: P1 (thin/rich multi-marker divergence), P5 (ownership/sourcehood dissociation under manipulation), P8 (Mode B availability vs exercise in flow/mastery), P9 (effort dissociation from agency-quality), P10 (chosen-habit vs compulsive-habit five-marker split), P14 (order-matched intervention response), and P18 (longitudinal cascade profile-formation). The full eighteen-prediction structure provides breadth; the seven backbone provide architectural spine.

## 11.4 Family A — Timing and tier-structure predictions

Predictions P1–P3 derive from the three-tier configuration (Section 3.1), the four-way decision/trying/action/outcome separation (7.10), the timing-marker non-identity chain (10.3), and the preparation-not-preemption framing (10.6).

**P1 — Thin-selection / rich-choice multi-marker divergence.**

| $PP_1$ component | Specification |
|---|---|
| $S$ Structural source | Three-tier configuration (free selection / free choice proper / wholehearted free choice); Sections 3.1, 7.7, 8.3 |
| $T$ Target architectural object | Selection-event configuration as a function of tier; multi-marker $EIP_p$ profile |
| $M$ Marker set | Option-space richness; deliberation reports; source-access reports; confidence stability; ownership-integration measures; recognition-timing patterns; neural-temporal signatures where measurable |
| $D$ Domain | Lab tasks comparing arbitrary spontaneous flex paradigms with deliberative-engagement paradigms; mixed-stakes paradigms; option-richness manipulations |
| $C$ Comparator | Libet/Soon-style overgeneralization that treats arbitrary button-press paradigms as testing free choice generally; simple voluntarism that treats agency as undifferentiated |
| $F$ Failure condition | No multi-marker distinction between thin arbitrary selection and wholehearted choice; uniformity across all the relevant axes per 10.17 Pattern 2 |
| $E$ Exclusions | The prediction does *not* require a unique neural signature for wholehearted choice; identical motor-readiness alone is not pressure; the discriminator is multi-marker uniformity-or-divergence |

Architectural derivation: the three-tier configuration commits the architecture to thin and rich agency-configurations differing structurally — option-space, evaluative engagement, source-access engagement, ownership-integration each contribute differently across tiers. If those structural differences exist, they should produce differential signatures across multiple measurement axes simultaneously, not necessarily through any single privileged neural signal.

**P2 — Prediction-lead-time varies with option-space richness and evaluative engagement.**

| $PP_2$ component | Specification |
|---|---|
| $S$ Structural source | Condition 1 live-option construction + Condition 2 evaluative engagement + operator-bundle selection apparatus; Sections 3.2, 5.4, 7.7 |
| $T$ Target architectural object | Pre-report decoding accuracy and lead-time as function of choice-configuration |
| $M$ Marker set | Decoding lead-time; decoding accuracy; option-space complexity scaling; prior-preference stability; evaluative depth measures |
| $D$ Domain | fMRI / EEG decoding paradigms varying option-stakes; preference-stability vs novel-option paradigms |
| $C$ Comparator | Simple "predictability = unfreedom" interpretations of Soon-class results |
| $F$ Failure condition | High-accuracy, content-specific prediction of rich deliberative choices before task-level markers of relevant option-construction, evaluative engagement, or source-access work are present, excluding prediction from stable preferences, prior profile-commitments, or known value-rankings; per 10.17 Pattern 1 |
| $E$ Exclusions | The prediction does *not* deny that stable preferences and prior profile-commitments allow ordinary predictability; only content-specific prediction before relevant option-construction would pressure the architecture |

Architectural derivation: rich choices engage option-space construction, projection-toolset operation, source-pathway access, and evaluative integration that thin selections do not. If these processes are real and structurally distinct, content-specific decoding should be harder before they have operated — except where the agent's stable-character profile already entails the choice (which is architecture-compatible per 7.11 profile-formative configurational decisions).

**P3 — Preparation signals will not uniformly map to selection-events.**

| $PP_3$ component | Specification |
|---|---|
| $S$ Structural source | $t_{prep} \not\equiv t_{select}$; preparation-not-preemption framing per 10.3, 10.6 |
| $T$ Target architectural object | Relationship between preparation-marker dynamics and operator-bundle selection-event |
| $M$ Marker set | Readiness-potential timing; task-set establishment markers; accumulator dynamics; veto / interruption capacity; trial-by-trial variability in preparation-to-selection latency |
| $D$ Domain | Libet-class paradigms with manipulation of task-set complexity; veto paradigms; multi-option paradigms varying preparation-completion before selection |
| $C$ Comparator | RP-as-unconscious-decision-by-default; simple neural-preemption views |
| $F$ Failure condition | Preparation markers reliably map one-to-one onto completed selection-events across all rich and thin agency cases, with no veto-capacity or task-set artifact contributions |
| $E$ Exclusions | The prediction does *not* claim RPs are never decision-relevant; it claims preparation is not selection by default and the relationship between preparation and selection should vary with task-structure |

Architectural derivation: the preparation-not-preemption framing of 10.6 commits the architecture to four interpretations of RP-class signals (unconscious decision; preparatory affordance; stochastic accumulator; task-set artifact), with the discriminator being whether substrate dynamics complete the act without operator-bundle engagement (preemption) or supply the readiness on which the operator-bundle then operates (preparation). If the architecture is correct, RP-class signals should not uniformly behave as completed selections.

## 11.5 Family B — Report, recognition, ownership, and sourcehood

Predictions P4–P6 derive from the post-hoc recognition / source-opacity / confabulation triad (7.9, 9.7, 10.7), the ownership / sourcehood dissociation (8.15, 9.5), and the manipulation continuum (5.9, 9.12).

**P4 — Post-hoc recognition, source-opacity, and confabulation are empirically separable.**

| $PP_4$ component | Specification |
|---|---|
| $S$ Structural source | Post-hoc recognition / source-opacity / confabulation triad per 7.9, 9.7, 10.7; the architectural commitment that delayed reports do not collapse into a single configuration |
| $T$ Target architectural object | Report-configuration profile as a function of underlying selection / source / ownership status |
| $M$ Marker set | Report confidence stability; report stability under probing; source-report accuracy when externally verifiable; timing-report patterns; choice-blindness-style mismatch detection rates; ownership-confidence under perturbation |
| $D$ Domain | Choice-blindness paradigms with variable swap-detection conditions; post-action reconstruction tasks; source-attribution paradigms with externally verifiable source-pathway |
| $C$ Comparator | Global confabulation accounts of agency report (all reports confabulated); naïve realist accounts of introspection (all reports accurate) |
| $F$ Failure condition | All delayed reports collapse empirically into one configuration; or post-hoc recognition, source-opacity, and confabulation prove indistinguishable across paradigms designed to dissociate them |
| $E$ Exclusions | The prediction does *not* claim choice-blindness paradigms detect *no* confabulation; per 10.7, choice-blindness involves real prior selection plus false later narration — both of which the triad accommodates |

Architectural derivation: the three-way distinction commits the architecture to three structurally distinct report-configurations. If they are real, paradigms that target each (delayed-report-with-accurate-recognition, owned-but-source-opaque, false-source-narrative) should produce distinguishable report-profiles. If they collapse into one configuration, the triad would lose empirical traction.

**P5 — Source-compromised-but-owned action under manipulation paradigms (flagship prediction).**

| $PP_5$ component | Specification |
|---|---|
| $S$ Structural source | Ownership / sourcehood dissociation (8.15, 9.5); manipulation-not-ownership-failure-by-default (5.9, 9.12) |
| $T$ Target architectural object | Joint distribution of ownership-reports and source-access reports under externally-structured option-spaces |
| $M$ Marker set | Ownership-confidence reports; source-access reports; awareness-of-influence reports; option-space-shaping detection; verification-bypass markers; post-manipulation-disclosure reactions |
| $D$ Domain | Well-designed manipulation paradigms varying transparency, alternatives, and source-access; nudging paradigms with disclosure manipulations; persuasion paradigms with verification-availability manipulations |
| $C$ Comparator | Ownership-only agency models that treat agency as a single dimension; naïve manipulation-exculpation models; simple coercion-vs-autonomy binaries |
| $F$ Failure condition | Ownership-reports and source-access reports always rise and fall exactly together; no detectable dissociation between ownership-axis and source-status axis under any manipulation configuration; per 10.17 Pattern 3 |
| $E$ Exclusions | The prediction does *not* test ownership/outcome-success dissociation, which is a different empirical relationship; the discriminator is ownership/sourcehood specifically |

Architectural derivation: the architecture's hard discriminator from [Free Will §4.2] is that manipulation can produce owned-but-source-compromised configurations — in the source-compromised-but-owned configuration, the manipulated agent's selection within the compromised option-space remains genuinely theirs at Condition 6, while the option-space-shaping is attributable to the manipulator's constructed-order act. If this dissociation is real, well-designed manipulation paradigms should produce ownership reports decoupled from source-access reports under at least some conditions. This is one of the architecture's most distinctive predictions and one of its hardest discriminators against ownership-only theories.

*A worked manipulation design.* Participants are presented with a binary policy choice (e.g., supporting program A or program B) under three conditions: source-clean (full transparency about the policy implications and authoring sources), source-compromised-and-disclosed (an additional framing argument is added but its source-shaping role is disclosed before judgment), and source-compromised-without-disclosure (the framing is added covertly, with disclosure occurring only post-judgment in a follow-up session). Measurements: ownership-confidence ("How much was this your own decision?"), source-access reports ("Can you articulate why you chose as you did?"), awareness-of-influence ("Did anything in the materials shape your view?"), and post-disclosure ownership-revision ("Now that you know about the framing, do you still endorse this as your decision?"). The architectural prediction: ownership-confidence should remain comparably high across all three conditions (Condition 6 ownership preserved) while source-access reports and awareness-of-influence reports should diverge, with the source-compromised-without-disclosure condition showing notably weaker source-access. Convergent dissociation across these axes would constitute support for ownership/sourcehood separation; uniform tracking of ownership and source-access across conditions would constitute pressure.

**P6 — Source-compromised decisions show recognition-timing or source-report instability sometimes (not uniformly).**

| $PP_6$ component | Specification |
|---|---|
| $S$ Structural source | $A/\phi$ source-pathway access (File 3 §6.1, 7.9); Mode B object-domain availability under source-opacity (10.7 patched row); source-status overlay |
| $T$ Target architectural object | Recognition-timing and source-report patterns as function of source-status |
| $M$ Marker set | Recognition-lag duration; report-confidence stability; report-revision patterns; mismatch-detection rates; source-report fragility under probing |
| $D$ Domain | Source-manipulation paradigms with externally-controlled source-pathway access; recognition-timing paradigms; source-attribution stability paradigms |
| $C$ Comparator | Models that treat ownership-report as the only relevant agency-report; flat introspection models |
| $F$ Failure condition | Carefully isolated source-status differences never produce any recognition-timing, report-stability, or source-confidence differences across well-designed source-manipulation conditions; per 10.17 Pattern 4 |
| $E$ Exclusions | The expectation is *sometimes-differential, not uniformly-differential*; not every source-compromised decision must show a recognition-lag; the prediction is pattern-level across paradigms, not single-trial deterministic |

Architectural derivation: by analogy with recognition-lag patterns in *Differentiated Affect* (especially love-onset / love-ending configurations) and the agency-source analysis of 9.7 / 10.7, the architecture expects source-opacity and source-compromise to *sometimes* produce recognition-and-report differences. If they never produce such differences across well-designed paradigms, the source-status overlay would lose empirical traction at the recognition-and-report level.

## 11.6 Family C — Mode B and order-asymmetry predictions

Predictions P7–P8 derive from the order-asymmetric Mode B object-domain availability (7.6) and the Mode B availability ≠ exercise distinction (7.5).

**P7 — Mode B availability is domain-specific, not global.**

| $PP_7$ component | Specification |
|---|---|
| $S$ Structural source | Order-asymmetric Mode B object-domain availability per 7.6; constructed-order Mode B bandwidth limitation per 5.6 lossy-compression cascade |
| $T$ Target architectural object | Domain-specificity of reflective object-access |
| $M$ Marker set | Domain-differential introspective accuracy; differential source-report accuracy across action-domain vs source-pathway vs option-space; post-action reconstruction accuracy by domain; cross-task introspection-accuracy correlations (or their absence) |
| $D$ Domain | Multi-domain introspection paradigms; cross-task accuracy comparisons; structured-introspection paradigms with externally-verifiable domain-specific accuracy |
| $C$ Comparator | Global introspection models ("introspection is reliable"); global confabulation models ("introspection is confabulation"); single-capacity executive-function models |
| $F$ Failure condition | Mode B accuracy behaves as a single global capacity across all agency-domains, with no detectable domain-specificity in introspective access |
| $E$ Exclusions | The prediction does *not* claim Mode B accuracy is uniform within a domain; it claims that asymmetry exists across domains in addition to whatever within-domain variability is present |

Architectural derivation: the order-asymmetric Mode B framing commits the architecture to reflective access varying by object-domain. An agent may identify their action while being unable to identify its source-shaping; identify their intention while being unable to identify their affective contraction; identify their outcome while being unable to identify their selection-pathway. If Mode B were globally uniform, this prediction would fail.

**P8 — Flow and mastery preserve post-action Mode B availability despite reduced in-action Mode B exercise.**

| $PP_8$ component | Specification |
|---|---|
| $S$ Structural source | Mode B availability ≠ Mode B exercise per 7.5; mastery as compressed but not eliminated configuration per 5.7, 10.11 |
| $T$ Target architectural object | Distinction between in-action and post-action Mode B status across configurations |
| $M$ Marker set | In-action reflective monitoring (suppressed in flow); post-action report specificity (preserved in mastery); error-correction capacity (preserved in mastery, impaired in capture); interruption effects on performance vs ownership; ownership reports and source-reports post-action |
| $D$ Domain | Expert-performance paradigms with post-action structured probing; flow-state vs automaticity-vs-capture paradigms; mastered-domain interruption paradigms |
| $C$ Comparator | Low-deliberation = low-agency models; flat agency-exercise models that don't distinguish in-action from post-action |
| $F$ Failure condition | Flow / mastery configurations consistently look indistinguishable from capture / dissociation configurations across ownership, interruptibility, post-action access, and error-correction markers |
| $E$ Exclusions | The prediction does *not* claim mastery and capture are *always* distinguishable on every marker; it claims they should be distinguishable across multi-marker profiles when designed paradigms target the discriminating axes |

Architectural derivation: mastery preserves post-action Mode B availability because the structural capacity for reflective object-access is not damaged; in-action Mode B exercise is appropriately compressed because reflection-during-execution would disrupt performance. Capture / dissociation differs structurally — Mode B availability itself may be compromised, not just exercised differently. Multi-marker comparison should reveal this.

## 11.7 Family D — Effort, mastery, habit, and automaticity predictions

Predictions P9–P11 derive from the effort/agency-quality separation (6.8), the eight-source resistance taxonomy (6.4), the mastery / flow / habit / automaticity / capture distinctions (8.7, 10.11), and the willing-strategies taxonomy (5.8).

**P9 — Effort-level dissociates from agency-quality.**

| $PP_9$ component | Specification |
|---|---|
| $S$ Structural source | Effort = operator-bundle direction under resistance, not agency-quality (6.8); resistance-source taxonomy (6.4) |
| $T$ Target architectural object | Joint distribution of effort-markers and agency-quality markers |
| $M$ Marker set | Subjective effort reports; physiological arousal; persistence under difficulty; error rate; resistance-source classification (cognitive / affective / motivational / substrate / source-compromised / projection-collapsed); outcome-success; ownership-quality markers |
| $D$ Domain | Multi-resistance-source paradigms; high-effort vs low-effort agency-quality paradigms; mastery-vs-effort comparisons in expert performers |
| $C$ Comparator | Effort-based agency models that treat high effort as stronger agency; willpower-as-agency models; effort-moralizing accounts |
| $F$ Failure condition | Effort-level alone reliably classifies agency-quality across domains and resistance-sources; mastery and high-effort-resistance produce indistinguishable agency-quality profiles |
| $E$ Exclusions | The prediction does *not* deny that effort information is useful in some agency assessments; it claims effort cannot serve as a single-axis agency-quality measure |

Architectural derivation: effort tracks resistance-cost under operator-bundle commitment; resistance can come from eight architecturally-distinct sources per 6.4. High effort under salience-capture resistance is not architecturally identical to high effort under projection-toolset resistance, and neither is identical to low effort in mastery. If effort and agency-quality were the same, they would not require this multi-source disaggregation.

**P10 — Habitual-chosen and habitual-compulsive patterns differ on five markers (backbone prediction).**

| $PP_{10}$ component | Specification |
|---|---|
| $S$ Structural source | Habit configurations (8.7); substrate-coupling-vs-preemption discriminator (6.8); ownership-integration (Condition 6) |
| $T$ Target architectural object | Distinction between owned-but-routinized and substrate-captured habit configurations |
| $M$ Marker set | Five-marker profile: interruptibility under Mode B access; $\Pi$-alignment with endorsed priorities; source-status; ownership-integration; substrate-coupling configuration |
| $D$ Domain | Habit-disruption paradigms; addiction-vs-routine comparison paradigms; expert-performance habits vs compulsion paradigms |
| $C$ Comparator | Frequency-based habit models that don't differentiate compelled from chosen routines; simple motivation-vs-ability models of compulsion |
| $F$ Failure condition | Interruptibility, $\Pi$-alignment, source-status, ownership, and substrate-coupling fail to differentiate the configurations across well-designed paradigms |
| $E$ Exclusions | The prediction does *not* claim every habit cleanly fits one category; mixed configurations are expected; the discriminator is multi-marker pattern, not single-marker classification |

The expected five-marker pattern:

| Marker | Habitual-chosen | Habitual-compulsive |
|---|---|---|
| Interruptibility | Generally interruptible under Mode B reflective access | Resistant even under reflective opposition |
| $\Pi$-alignment | Aligned with endorsed priorities | Captures priority against endorsement |
| Source-status | Self-curated or accepted | Substrate-driven, source-compromised, or pre-agentially imprinted |
| Ownership | Integrated as chosen pattern | Felt alien, pressured, or regretted |
| Substrate-coupling | Supports the chosen pattern | Capture / bypass / preemption |

Architectural derivation: the architecture's commitment that owned routinized action is structurally different from substrate-captured habit (per 8.7) requires that the two configurations be empirically distinguishable. Five distinct measurement axes contribute to the configurations differently; convergent measurement should reveal the difference.

*A worked five-marker comparison.* Two configurations: (a) an established daily-exercise habit in an agent who values fitness, integrates the practice into their identity, and structures their morning around it; (b) a compulsive-checking pattern (repeatedly verifying that doors are locked, devices are off, etc.) in an agent who endorses checking-once but cannot stop. Across the five markers: *interruptibility* — (a) is interruptible (a meaningful conflict, illness, or schedule change can suspend the habit without distress), (b) resists interruption (the agent's reflective opposition does not stop the checking). *$\Pi$-alignment* — (a) aligns with endorsed health and discipline priorities, (b) captures priority against endorsed once-only-checking commitments. *Source-status* — (a) is self-curated (the agent chose this routine and continues to endorse the choice), (b) is substrate-driven and source-compromised (the checking-pressure arises without the agent's authorization). *Ownership* — (a) is integrated as chosen pattern ("this is the kind of person I am"), (b) is felt alien, pressured, or regretted ("I shouldn't be doing this again"). *Substrate-coupling* — (a) substrate supports the chosen pattern (the agent's body has adapted to morning exercise; the rhythm is supportive), (b) substrate-capture / bypass / preemption is occurring (the checking-impulse arises before deliberation can complete and continues despite reflective opposition). The architectural prediction: convergent five-marker assessment should reliably distinguish the two configurations. Mixed configurations are expected — a habit may be endorsed in some respects while displaying capture-features in others — but the multi-marker pattern should still differentiate the configurations even where individual markers blur.

**P11 — Configurational and slingshot willing improve effort-economy where toolkit-development is mature.**

| $PP_{11}$ component | Specification |
|---|---|
| $S$ Structural source | Direct / configurational / slingshot willing taxonomy per 5.8; profile-formative configurational decisions per 7.11 |
| $T$ Target architectural object | Effort-economy-per-progress-unit as function of willing-strategy distribution |
| $M$ Marker set | Effort per goal-progress-unit; relapse / maintenance rates; scaffold-use frequency; environmental-modification frequency; timing-strategy use; configurational/slingshot to direct-willing ratio; outcome stability |
| $D$ Domain | Behavior-change longitudinal paradigms; expertise-acquisition studies; addiction-recovery paradigms; habit-formation longitudinal designs |
| $C$ Comparator | Simple willpower / direct-effort models that privilege brute persistence; ego-depletion frameworks that treat all willing as resource-consuming |
| $F$ Failure condition | Configurational and slingshot strategies show no effort-economy advantage over direct willing in scaffold-relevant domains across mature toolkits |
| $E$ Exclusions | The prediction does *not* claim configurational/slingshot strategies always outperform direct willing; it claims they should outperform in *scaffold-relevant* domains where environment-design, timing, or scaffold-use is structurally relevant |

Architectural derivation: the willing-strategies taxonomy commits the architecture to three structurally distinct strategies for direction-of-action under resistance. If configurational and slingshot strategies are structurally distinct from direct willing — engaging environment-modification, timing, and scaffold-use rather than brute substrate-resistance — they should show different effort-economy profiles in domains where those structural advantages are exploitable. This was forward-flagged as Pred 22 in earlier sections and is here promoted to formal Section 11 prediction status.

## 11.8 Family E — Diminished-agency and toolkit-damage predictions

Predictions P12–P14 derive from Section 8's variation taxonomy (8.8 compulsion, 8.9 ADHD-like, 8.11 learned helplessness, 8.12 affect-mediated contraction), Section 5's toolkit-development apparatus (5.4 toolkit failure modes, 5.5 maladaptive toolkit-development), and the order-matched intervention apparatus (5.7 mastery, 6.7 toolset-effort).

**P12 — ADHD-like implementation gaps show Mode B identification without reliable implementation repair.**

| $PP_{12}$ component | Specification |
|---|---|
| $S$ Structural source | Order-specific substrate-developmental constraint affecting sustained operator-bundle mediation, often through first-/second-order control capacities that support third-order implementation (8.9); Mode B available for gap-identification but not reliably sufficient for implementation-repair under current conditions per v0.1.9.1 Patch 14 |
| $T$ Target architectural object | Joint distribution of reflective-access markers and sustained-implementation markers in ADHD-like configurations |
| $M$ Marker set | Task-initiation latency; sustained-attention stability; working-memory disruption rates; response-inhibition difficulty; reflective-endorsement-to-implementation gap; effort-per-progress-unit; differential effort-cost in domain-specific tasks |
| $D$ Domain | ADHD-relevant paradigms with sustained-execution requirements; task-switching paradigms; reflective-vs-implementation gap paradigms |
| $C$ Comparator | Laziness / preference-only interpretations of ADHD-like presentations; pure motivation-deficit models; uniform executive-function-deficit models |
| $F$ Failure condition | Reflective recognition of the implementation gap reliably repairs implementation across configurations without scaffold or substrate-support changes |
| $E$ Exclusions | The prediction does *not* function as clinical diagnosis or treatment recommendation; the architecture treats ADHD-like as candidate framing, not foundation-derived clinical doctrine |

Architectural derivation: the ADHD-like configuration is characterized by Mode B remaining available for identifying the gap (reflective access to "I'm not following through") while the substrate-developmental constraint at orders 1–2 limits sustained operator-bundle direction without scaffolding. If reflective recognition were sufficient for repair, the configuration would not be architecturally distinct from preference-only / motivation-only configurations.

**P13 — Learned helplessness impairs live-option construction, not motivation alone.**

| $PP_{13}$ component | Specification |
|---|---|
| $S$ Structural source | Projection-toolset collapse (8.11); live-option contraction; Condition 1 fuzzy-construction discipline applied to option-availability |
| $T$ Target architectural object | Projection-toolset functioning vs motivation-state in helplessness configurations |
| $M$ Marker set | Future-pathway generation deficit measures; pathway-confidence reports; transfer-after-uncontrollability rates; option-construction tasks under externally-verifiable available options; failure-to-initiate paradigms with available pathways |
| $D$ Domain | Learned-helplessness paradigms with pathway-availability manipulations; transfer-test paradigms; projection-task assessments |
| $C$ Comparator | Motivation-only accounts of helplessness ("they don't want to escape"); attentional accounts only; affect-only accounts |
| $F$ Failure condition | Learned-helplessness configurations show intact pathway-construction with only low desire-to-initiate; no projection-toolset deficits detectable across paradigms designed to dissociate motivation from construction |
| $E$ Exclusions | The prediction does *not* deny motivational components in helplessness configurations; it claims projection-toolset damage is structurally distinct from and additive to motivational components |

Architectural derivation: the live-option construction discipline (Condition 1) requires that the agent can construct option-paths as live and contrastive. Learned-helplessness training damages this construction-capacity, not just motivation. If only motivation were affected, conceptual recognition of available options should restore behavior; the architecture predicts this often does not happen because the projection-toolset itself has been impaired.

**P14 — Order-matched training / intervention predicts order-specific option-space expansion and response (backbone prediction).**

| $PP_{14}$ component | Specification |
|---|---|
| $S$ Structural source | Therapeutic / interventional modalities classified by primary-order target; toolkit-development apparatus (5.4, 5.5); ADHD architectural mapping (8.9); order-specific training-transfer (4.5 universal toolkit constraint, 5.7 mastery) |
| $T$ Target architectural object | Training / intervention-response trajectory as function of order-match between training-target and toolkit / pathology damage profile; cross-order transfer profile |
| $M$ Marker set | Intervention or training modality classification by primary-order target; pathology / skill-deficit damage profile classification; option-space expansion by order; cross-order transfer profile; outcome trajectory; sequenced-intervention response patterns; comparative effect-size by match-vs-mismatch |
| $D$ Domain | Comparative-treatment paradigms classified by order-match; order-specific training-transfer paradigms; sequenced-intervention paradigms; treatment-stratification studies; skill-acquisition studies |
| $C$ Comparator | One-size-fits-all cognitive, behavioral, somatic, or introspective intervention models; transdiagnostic generic-intervention models; order-agnostic training-transfer models |
| $F$ Failure condition | Independently classified order-targeted training / intervention produces no primary expansion at the targeted order, cross-order transfer is not mediated by shared toolkit features, and order-match never improves task or intervention response relative to order-mismatch under independently validated profile identification |
| $E$ Exclusions | The prediction is a research-prediction, *not* clinical treatment advice or a clinical protocol; it does not license treatment-stratification recommendations without further validation; clinical, legal, and policy implications belong to downstream applied work, not Section 11 |

Architectural derivation: the architecture's order-specific framing of toolkit, condition-profile damage, and configurational decision commits it to expecting that training or interventions addressing a specific order should produce primary option-space expansion at that order, with cross-order transfer dependent on shared toolkit features. A second-order cognitive intervention applied to a first-order substrate-developmental constraint should perform differently than a first-order substrate-supporting intervention applied to the same configuration. If training-transfer and intervention efficacy are independent of order-match, the order-specific framing would lose empirical traction.

*This patch fulfills the earlier Pred 20 forward flag.* Pure first-order training should primarily expand first-order option-space, pure third-order training should primarily expand third-order option-space, and integrated multi-order training should show broader transfer where toolkit features are shared. The order-matched intervention prediction (P14 as previously stated) and the order-specific training-transfer prediction (Pred 20) are unified in this single prediction-profile rather than divided across two separate predictions.

## 11.9 Family F — Affect, social source-shaping, and constructed-order predictions

Predictions P15–P17 derive from the *Differentiated Affect* paper's affect criterion and affect-as-perturbation framework (§4.1), together with the five-cluster differentiated-affect taxonomy (§§5–9), the manipulation continuum (5.9), the constructed-order action apparatus (5.7), and the perspectival-realist commitment against group-mind reification (9.13).

**P15 — Affect-mediated agency contraction varies by affect-operator, not just affect-intensity.**

| $PP_{15}$ component | Specification |
|---|---|
| $S$ Structural source | *Differentiated Affect* affect-as-perturbation framework; affect-operator taxonomy across threat / self / boundary / embodied / connection clusters; agency-variation taxonomy 8.10–8.13 |
| $T$ Target architectural object | Structural channel through which affect modulates agency-configuration |
| $M$ Marker set | Affect-type classification; affect-intensity controls; option-space contraction patterns by affect-type; threat-weighted projection vs PtCns pressure vs boundary-operation patterns; structural-channel signatures by affect-cluster |
| $D$ Domain | Affect-induction paradigms with intensity-controlled affect-type variation; emotion-and-decision paradigms; clinical-adjacent affect-and-agency paradigms |
| $C$ Comparator | Intensity-only affect-agency models ("stronger affect = weaker agency"); valence-only models (positive vs negative); arousal-only models |
| $F$ Failure condition | Affect-type makes no structural difference once intensity is controlled; agency-effects of fear, shame, anger, pain, anhedonia, and trauma-cue activation are equivalent at matched intensities |
| $E$ Exclusions | The prediction does *not* require that affect-types are *fully* dissociable; it claims affect-types should produce *structurally different* agency effects beyond a single intensity dimension |

Expected differential agency-effects by affect-cluster (per *Differentiated Affect* taxonomy):

| Affect-domain | Expected structural agency-effect channel |
|---|---|
| Fear / anxiety | Threat-weighted projection; option-space contraction |
| Shame | PtCns pressure around identity-bearing exposure |
| Anger | Boundary-operation engagement; action-readiness threshold lowering |
| Pain | Substrate-dominant salience; attentional capture |
| Anhedonia | Salience flattening; initiation impairment |
| Trauma-cue activation | Source-opaque contraction; ownership disruption |

Architectural derivation: *Differentiated Affect* commits to affect-as-such being a structural perturbation operating through specific channels (salience, action-readiness, profile stability, PCE, PtCns, focus). Different affect-clusters perturb through different channels. If only intensity mattered, this taxonomy would be unnecessary.

**P16 — Social influence effects vary by transparency, alternatives, source-access, and verification-bypass.**

| $PP_{16}$ component | Specification |
|---|---|
| $S$ Structural source | Manipulation continuum (5.9); constructed-order action apparatus (5.7, 8.16); v0.1.9.1 Patch 5 social-source row corrections |
| $T$ Target architectural object | Configuration of agency-effects under structurally-different social-influence types |
| $M$ Marker set | Influence-type classification by transparency / alternative-availability / source-access / verification-bypass / recipient-aim-honoring; ownership reports; source-access reports; option-space-shaping detection; post-disclosure reactions |
| $D$ Domain | Social-influence paradigms varying transparency; nudging paradigms with disclosure manipulation; persuasion paradigms with verification-availability; teaching / coaching / therapy paradigms with recipient-aim variation |
| $C$ Comparator | Generic "influence reduces freedom" models; generic "ownership preserves freedom" models; binary autonomy-vs-coercion models; uniform-manipulation-effect models |
| $F$ Failure condition | Transparency, alternatives, source-access, and verification-bypass have no detectable effect on ownership / sourcehood reports or decision-profile measures across well-designed social-influence paradigms |
| $E$ Exclusions | The prediction does *not* treat any of nudging, persuasion, obedience, or compliance as automatically coercive or manipulative; the architecture's manipulation continuum commits it to influence-types differing structurally by source-status factors, not by paradigm-name |

Expected structural relationships:

| Source-status factor | Expected effect on agency-configuration |
|---|---|
| Transparency present | Preserves or improves source-access |
| Alternatives available | Maintains live option-space |
| Source-access blocked | Produces source-opacity or source-compromise |
| Verification bypassed | Increases manipulation / poisoning risk |
| Recipient aims honored | Autonomy-supporting constructed-order action |
| Recipient aims obscured / overridden | Manipulative constructed-order action |

Architectural derivation: the manipulation continuum commits the architecture to influence-effects varying structurally by transparency, alternative-availability, source-access, and verification-availability rather than by paradigm-name (Milgram-class vs nudging vs persuasion). If these factors had no structural effect, the manipulation continuum would lose empirical traction.

**P17 — Role-indexed access structures distributed attribution-inputs better than group-mind models.**

| $PP_{17}$ component | Specification |
|---|---|
| $S$ Structural source | Profile-indexed distributed responsibility (9.13); perspectival-realist commitment against group-mind reification; constructed-order role-indexed agency (8.16) |
| $T$ Target architectural object | Role-indexed attribution-input profile as a function of authority, information-access, discretion, expertise, mitigation-power, repair-option availability, and cascade-foreseeability |
| $M$ Marker set | Role authority; information-access asymmetry; discretion-availability; expertise distribution; mitigation-power; repair-option availability; cascade-foreseeability per role; optional experimental-philosophy judgment patterns treated as downstream measurement of whether human assessors track those inputs |
| $D$ Domain | Institutional-decision paradigms with role-stratified structural-input measurement; role-indexed attribution-profile paradigms; experimental-philosophy paradigms admissible only as indirect probes of input-tracking |
| $C$ Comparator | Unindexed collective-blame models; group-mind responsibility models; uniform-membership attribution models |
| $F$ Failure condition | Role-indexed structural variables fail to differentiate attribution-input profiles across institutional cases, and unindexed group-membership models capture the relevant structural profile as well as or better than the role-indexed model. Human judgment studies may supply evidence, but folk judgments themselves are not the architectural object |
| $E$ Exclusions | The prediction does *not* require attribution-judgments to track architectural roles *exactly*; it requires role-indexed structural variables to capture the architecture's attribution-input profile better than unindexed group-membership models |

Architectural derivation: the architecture's perspectival-realist commitment treats collective responsibility as the joint pattern of perspective-anchored agencies, not as a free-standing group attribution. Role-indexed profile differences (authority, information-access, discretion, expertise, mitigation-power, cascade-foreseeability) should provide the architecture's attribution-input profile better than uniform group-membership. If group-mind models captured the structural profile equally well, the perspectival-realist commitment would lose empirical traction.

*This prediction is not that people will in fact assign responsibility correctly.* It is that the architecture's structural attribution-inputs are role-indexed rather than group-mind-indexed. Experimental judgment paradigms are admissible only as indirect probes of whether assessors track those inputs; folk-psychological judgments themselves are not architectural predictions, per the 11.2 discipline.

## 11.10 Family G — Cascade and profile-formation prediction

Prediction P18 derives from the output-imprinting cascade (5.6), profile-formative configurational decisions (7.11), the cascade-attribution apparatus (9.10), and the cascade longitudinal design subsection (10.15).

**P18 — Longitudinal designs reveal profile-formation invisible to single-trial paradigms (backbone prediction).**

| $PP_{18}$ component | Specification |
|---|---|
| $S$ Structural source | Output-imprinting cascade per 5.6; profile-formative configurational decisions per 7.11; longitudinal-design apparatus per 10.15 |
| $T$ Target architectural object | Profile-formation across time as architecturally-distinct phenomenon from single-trial selection |
| $M$ Marker set | Stage 1 self-imprinting markers (changed salience, repertoire, confidence, identity-claim, habit strength); Stage 2 output markers (environmental alteration, social response, role uptake, scaffold reinforcement); Stage 3 feedback closure markers (altered environment / social field re-entering profile and option-space) |
| $D$ Domain | Habit-formation longitudinal paradigms; addiction-cycle longitudinal studies; learned-helplessness transfer paradigms; expertise-development longitudinal studies; scaffold-capture developmental studies |
| $C$ Comparator | Single-trial agency paradigms as sufficient models of agency; frequency-only habit models; static-trait models |
| $F$ Failure condition | In longitudinal paradigms designed to target cascade-relevant repeated action — habit formation, addiction cycles, learned-helplessness transfer, expertise development, scaffold-capture — repeated action produces only simple frequency effects, with no detectable profile-state changes, environmental / social output effects, or feedback-closure phenomena beyond what single-trial paradigms capture |
| $E$ Exclusions | The prediction does *not* claim single-trial paradigms are useless; it claims they are structurally limited for cascade and profile-formation phenomena, which are architecturally distinct objects. The prediction also does *not* claim every repeated action closes into profile-formation; some cascades decay, are interrupted, or require ongoing reinforcement |

Architectural derivation: the output-imprinting cascade commits the architecture to repeated actions producing profile-state changes (Stage 1), environmental and social outputs (Stage 2), and feedback-closure that re-enters the agent's profile (Stage 3). These phenomena require longitudinal observation because their architectural object is profile-formation across time. If repeated action produced only simple frequency effects with no profile-state changes detectable beyond what single-trial paradigms can measure (in cascade-relevant paradigm domains specifically), the cascade apparatus would lose empirical traction.

*A compressed longitudinal design template.* The 10.15 habit-training cascade scenario gives the operational template: at $t_0$, baseline measurement of effort-cost per session, substrate-resistance markers, Mode B reflective access, and identity-claim relating to the targeted activity. At $t_{1...n}$ across the training window, repeated-measures of those axes plus self-imprinting markers (compliance trajectory, automaticity development, salience-restructuring toward activity-relevant cues). Stage 2 cascade-effects measured in environmental and social ecology (relevant tool-use, relevant social-network shifts, scaffold-reinforcement). Stage 3 feedback-closure measured in profile-state changes (identity-update, salience-restructuring such that activity-skipping generates dissonance that previously did not). At the training window's end, the architectural object is detectable: profile-formation has occurred (the agent at the endpoint differs structurally from the agent at $t_0$ across multiple axes simultaneously, with cascade-traces visible across all three stages). Comparable templates apply to addiction-cycle paradigms (where Stage 3 feedback-closure may produce capture rather than mastery), learned-helplessness paradigms (where Stage 1 self-imprinting produces projection-toolset damage that propagates across novel control situations), and scaffold-capture longitudinal studies. The single-trial paradigm cannot capture this; the longitudinal design can.

## 11.11 Pressure conditions: what would force revision

The eighteen predictions imply specific pressure conditions for the architecture's core commitments. The compact summary:

| Architectural commitment | Pressure pattern that would force revision |
|---|---|
| Three-tier configuration (thin / proper / wholehearted) | No multi-marker distinction across thin arbitrary selection and wholehearted choice; uniformity across all the relevant axes (P1, P2) |
| Preparation ≠ selection (10.6 framing) | Preparation markers reliably map one-to-one onto completed selection-events across rich and thin agency cases (P3) |
| Post-hoc recognition / source-opacity / confabulation triad | All delayed reports collapse empirically into one configuration; the three configurations prove indistinguishable (P4) |
| Ownership ≠ sourcehood | Ownership-reports and source-access reports always rise and fall exactly together; no detectable dissociation under any manipulation configuration (P5) |
| Source-status overlay (recognition-and-report sometimes-differential) | Carefully isolated source-status differences never produce any recognition-timing, report-stability, or source-confidence differences across well-designed paradigms (P6) |
| Order-asymmetric Mode B | Mode B accuracy behaves as a single global capacity across all agency-domains (P7) |
| Mode B availability ≠ exercise | Flow / mastery configurations consistently look indistinguishable from capture / dissociation across multi-marker profiles (P8) |
| Effort ≠ agency-quality | Effort-level alone reliably classifies agency-quality across domains and resistance-sources (P9) |
| Habitual-chosen vs habitual-compulsive distinction | Five-marker profile (interruptibility, $\Pi$-alignment, source-status, ownership, substrate-coupling) fails to differentiate the configurations (P10) |
| Willing-strategies taxonomy | Configurational and slingshot strategies show no effort-economy advantage in scaffold-relevant domains (P11) |
| ADHD-like as substrate-developmental-constrained Mode B-available configuration | Reflective recognition reliably repairs implementation gaps without scaffold or substrate-support changes (P12) |
| Learned-helplessness as projection-toolset damage | Helplessness involves intact pathway-construction with only low desire-to-initiate (P13) |
| Order-specific pathology / intervention / training-transfer | Independently classified order-targeted training / intervention produces no primary expansion at the targeted order, cross-order transfer is not mediated by shared toolkit features, and order-match never improves task or intervention response (P14) |
| Differentiated affect agency-modulation by operator | Affect-type makes no structural difference once intensity is controlled (P15) |
| Manipulation continuum (transparency / alternatives / source-access / verification) | Source-status factors have no detectable effect on ownership / sourcehood reports across social-influence paradigms (P16) |
| Profile-indexed distributed responsibility | Role-indexed structural variables fail to differentiate attribution-input profiles across institutional cases; unindexed group-membership models capture the relevant structural profile as well or better (P17) |
| Output-imprinting cascade and profile-formation | In cascade-relevant longitudinal paradigms (habit, addiction, learned-helplessness, expertise, scaffold-capture), repeated action produces only frequency effects with no profile-state changes, environmental / social outputs, or feedback-closure phenomena beyond single-trial detection (P18) |

The pressure conditions are stated at the architectural level. Failure of a particular operationalization is not the same as failure of the architectural commitment; convergent failure across multiple paradigms designed to dissociate the relevant axes would be required to constitute architectural pressure.

## 11.12 Exclusions: what the architecture does not predict

Section 11 protects against empirical overclaim and normative leakage by specifying what the architecture does *not* predict. Each non-prediction has an architectural reason.

| Non-prediction | Architectural reason |
|---|---|
| A unique neural signature of free choice | Implementation-neutrality blocks substrate-level uniqueness claims; the architecture is committed to multi-marker pattern-uniformity-or-divergence, not specific neural signatures |
| Wholehearted choice must show a distinct readiness potential | Final motor preparation may be shared across structurally different choices; the discriminator is multi-marker uniformity per 10.17 Pattern 2 |
| All source-compromised decisions show recognition-lag | The expectation is sometimes-differential, not uniformly-differential per 10.17 Pattern 4 |
| All social influence is manipulation | Transparency, alternatives, source-access, and verification-availability matter; the manipulation continuum is structural per v0.1.9.1 Patch 5 |
| All low-effort action is mastery | Low effort may be mastery, habit, automaticity, capture, or reflex; multi-marker disambiguation is required per 10.11 |
| All high-effort action is better agency | Effort tracks resistance under operator-bundle commitment, not agency-quality per 6.8 |
| Clinical impairment implies no responsibility | Responsibility-attribution is Section 9's domain, not Section 11's prediction-domain; per 9.8 diminished-agency relocation discipline |
| Order-matched therapy is treatment advice | P14 is a research prediction, not a clinical protocol or treatment recommendation; clinical translation requires further validation outside Section 11's scope |
| Longitudinal cascade proves moral responsibility | Cascade profile is empirical; responsibility-attribution requires Section 9 overlays per 9.10 cascade-attribution test |
| Specific neural implementation of the operator-bundle | Implementation-neutrality preserved; the architecture predicts structural relationships, not implementation specifics |
| Precise distributional shape for Mode B onset | The architecture predicts order-asymmetry and domain-specificity; specific distributional shapes are implementation-level details |
| Population-level distribution of source-status | The architecture predicts within-individual configurations; population-level distributions depend on developmental, environmental, and social factors the architecture does not legislate |
| Direct readout of $t_{select}$ from any single empirical marker | Decision-event timing is inferential per 7.13; no marker directly observes $t_{select}$ |
| Folk-psychological judgments as architectural predictions | "People will assign less blame to manipulated agents" is a prediction about how humans use the architecture's structural inputs, not a prediction the architecture itself makes |
| Therapeutic efficacy claims beyond the order-match prediction | The architecture's clinical-adjacent predictions are research-level and do not claim therapeutic efficacy across configurations |
| Moral, legal, or policy conclusions | These depend on normative frameworks the architecture does not supply |

The exclusions list is not closed. Future application work may surface additional exclusions as the architecture is engaged with new empirical and theoretical contexts.

## 11.13 Summary

Section 11 has converted Sections 5–10's operationalization candidates into eighteen formal predictions, grouped into seven families, each specified through a $PP_i$ Prediction Profile with structural source, target architectural object, marker set, domain, comparator, pressure condition, and exclusions. Seven backbone predictions carry the section's argumentative weight: P1 (thin/rich multi-marker divergence), P5 (ownership/sourcehood dissociation under manipulation), P8 (Mode B availability vs exercise in flow/mastery), P9 (effort dissociation from agency-quality), P10 (chosen-habit vs compulsive-habit five-marker split), P14 (order-matched intervention response), and P18 (longitudinal cascade profile-formation).

The pressure conditions of 11.11 specify what would force the architecture to revise, qualify, or retract its commitments. The exclusions of 11.12 specify what the architecture does *not* predict, protecting against empirical overclaim and normative leakage. Together, the predictions, pressure conditions, and exclusions establish the architecture's empirical posture: structurally committed, falsification-oriented, implementation-neutral, normatively-restrained.


---

# 12. Open problems and research-program development

This section catalogues the agency-domain open problems the architecture has surfaced. The foundation-level metaphysical residue (ultimate sourcehood, primal not-I dependence, lawful-frame grounding, normative sufficiency), theological resonance under translation-not-derivation discipline, contemplative and no-agent translation limits, source-sensitive Frankfurt-class descendants, and self-determination theory engagement have been relocated to the companion *Free Will* paper [Free Will §6] as part of its philosophical engagement. This section catalogues the remaining open problems specific to the agency-domain structural and empirical apparatus: formal weighting among profile axes, accountability thresholds, source-status and Mode B operationalization, source-compromise dynamics over time, repair-accountability, developmental-window operationalization, neural / computational implementation of the operator-bundle, cross-order temporal binding, group-agency modeling, therapeutic and clinical translation, cross-cultural attribution variation, empirical-design problems not promoted to prediction-status, the priority map for future work, and the research-program summary.

Together with the foundation-level residue and theological-resonance entries in the companion paper, this section completes the seventeen-entry open-problem catalogue of the v0.2.3 source.

> *The boundary discipline applies: this section catalogues residue, it does not resolve it. Each entry is positioned as an open problem with priority and work-type classification rather than as a deliverable result.*


## 12.1 Formal weighting among profile axes

The most general research-program open problem concerns weighting. The architecture has introduced four profile-objects:

| Profile | Section | Function |
|---|---|---|
| $AP_{m,t;a}$ | 9 | Attribution profile: structures ownership / responsibility / accountability-relevant configuration |
| $EIP_p$ | 10 | Empirical interpretation profile: identifies what a paradigm measures |
| $PP_i$ | 11 | Prediction profile: specifies discriminating empirical commitments |
| $FTP_f$ | 12 | Framework translation profile: maps alternative frameworks into architectural terms |

These profiles specify components, not complete weighting rules. The Section 9 attribution profile distinguishes variation-family, ownership-status, source-status, condition-profile, Mode B availability, developmental-window, cascade profile, mitigation / repair availability, role-order profile, and temporal locus. But the present paper does not provide a general formula for how much each component contributes to an attribution result across all contexts.

This is not accidental. A universal weighting formula would likely overreach. The same axis may matter differently across decision-attribution, action-attribution, outcome-attribution, cascade-attribution, profile-formation, legal evaluation, clinical judgment, restorative repair, and ordinary interpersonal expectation. The architecture's structural specification was therefore made deliberately weight-neutral.

The open task is to determine whether weighting can be formalized in a principled but context-sensitive way. A future formalization would need to answer at least five questions:

| Question | Why it matters |
|---|---|
| Axis priority | Does ownership-status dominate source-status in some cases, or can source-status override ownership? |
| Threshold structure | Are there minimal thresholds for responsibility or accountability, or only graded profiles? |
| Object-specific weighting | Does decision-responsibility weight different axes than cascade-responsibility? |
| Temporal weighting | How should prior profile-formation, moment-of-action structure, and post-action repair be weighted? |
| Normative mapping | Which parts of weighting are architectural, and which belong to legal, moral, therapeutic, or restorative frameworks? |

The architecture should not answer these prematurely. The correct near-term task is to develop *local* weighting models: one for manipulation, one for compulsion, one for developmental-window cases, one for cascade-attribution, and one for distributed institutional action. Only after those local models stabilize should the architecture attempt a unified weighting theory. A premature universal formula would commit the architecture to a normative-context-collapse that the structural framing was specifically designed to avoid.


## 12.2 Minimal accountability thresholds

A second formal-research problem concerns whether accountability has a minimal structural threshold. Section 9 distinguished ownership, responsibility, and accountability: ownership is a Condition 6 relation; responsibility is a structural attribution relation; accountability is an answerability / demand / repair relation. But Section 9 did not settle whether accountability requires a minimal degree of ownership, Mode B availability, live mitigation, developmental maturity, or source-cleanliness.

The question: when, if ever, is an agent structurally below the threshold for accountability altogether?

Several configurations pressure the question:

| Case | Threshold problem |
|---|---|
| Compulsion / addiction | Moment-of-action Condition 4 capture may reduce action-responsibility, but prior mitigation or repair may remain live |
| Dissociation / alienation | Ownership may fail, but post-event repair or explanation demands may still exist |
| Immature developmental-window | The agent may be partially accountable only within a narrow domain |
| Trauma-shaped agency | Some alternatives may be externally imaginable but not developmentally live |
| Manipulated wholeheartedness | Ownership may be high while source-status is compromised |
| Institutional role-capture | The agent may act inside constrained role-space with partial discretion |

The open problem is not whether accountability can be reduced (Section 9 established that it can) but whether accountability has *floor conditions*. Possible floor candidates include: minimal ownership (the action must be integrated as the agent's in some respect); minimal Mode B access (the agent must be able to take some relevant agency-domain as object); minimal live alternative (some mitigation, refusal, repair, or explanation option must be live); minimal developmental availability (the relevant toolkit must be sufficiently developed); minimal role-discretion (in institutional cases, the agent must have some non-trivial discretion).

The architecture should leave open whether these are necessary conditions, sufficient conditions, or context-sensitive indicators. A premature threshold rule would collapse the profile-based approach into a simpler criterion theory. The correct architectural posture is to mark threshold-questions as open: the architecture's profile apparatus can specify when accountability is *reduced*, but not (yet) when it is *absent altogether*.

## 12.3 Operationalizing source-status and Mode B

The most important empirical research-program open problem is protocol-design for source-status and Mode B object-domain availability. The architecture repeatedly distinguishes ownership from sourcehood: a manipulated action may be owned while source-compromised; a wholehearted action may be source-poisoned; a low-deliberation skilled action may be source-clean; an action may be source-opaque without being confabulated. Section 11 made this one of the central prediction families, especially through P5 (ownership / sourcehood dissociation under manipulation). But the architecture still needs better operational protocols.

*Source-status protocol problem.* A source-status protocol would need to distinguish at least seven configurations: source-clean, scaffolded, osmotically shaped, source-compromised, source-poisoned, coerced, and manipulated. No single report question can distinguish these. "Did you feel free?" is too coarse. "Did you own the action?" tests ownership, not source-status. "Were you influenced?" depends on whether the agent has source-access to the influence. Future work should build multi-marker source-status assays combining: ownership reports; source-access reports; confidence and stability under probing; awareness of influence; independent manipulation markers; option-space reconstruction; counterfactual alternative availability; transparency / verification-pathway assessment; temporal recognition-lag or report-revision markers. The protocol has to be multi-marker because the architecture's source-status distinctions are themselves multi-marker.

*Mode B protocol problem.* Mode B is also difficult to operationalize because it is object-domain specific. The agent may reflect on the action but not on the source of the action; on the intention but not on the affective contraction shaping the intention; on the outcome but not on the live-option construction that preceded it. A mature protocol would need to distinguish Mode B availability (could the agent take the relevant agency-structure as object?), Mode B exercise (did the agent actually reflect during the event?), Mode B timing (was access available before, during, or only after action?), Mode B domain (was access available for intention, source, ownership, outcome, or cascade?), and Mode B distortion (was reflective access confabulated, source-opaque, or affectively contracted?).

The open problem is especially important because the architecture's distinction between flow / mastery and capture depends on it. Flow may involve reduced in-action Mode B exercise while preserving post-action Mode B availability; capture or dissociation may reduce or destroy availability itself. The architecture therefore requires a future Mode B object-domain battery, not a single introspective-access scale. Single-scale instruments would collapse precisely the distinctions that make Mode B architecturally distinctive.

This open problem is dependency-foundational for several Section 11 predictions. P5 (ownership / sourcehood dissociation), P7 (Mode B domain-specificity), P8 (flow / mastery preserves post-action Mode B), P12 (ADHD-like Mode B identification without reliable implementation repair), and P14 (order-matched training / intervention) all presuppose that source-status and Mode B can be operationally distinguished from related but architecturally different variables. Without robust protocol development, these predictions remain formal architectural commitments without mature test designs; they are prediction-ready, but not yet fully operationalized as decisive empirical assays.

*A worked example of the protocol problem.* In a manipulation paradigm, an agent may report high ownership of a choice, low awareness of influence, unstable source-explanation under probing, and preserved Mode B access to the action but not to the source-shaping. That profile would not show ownership failure; it would show a candidate source-compromised-but-owned configuration. A different profile — low ownership, high alienation, source-opacity, and preserved Mode B access to both action and source — would test a different configuration entirely. A third profile — high ownership, high awareness of influence, stable source-explanation, but reduced Mode B access to the source-pathway — would test source-acknowledged-but-Mode-B-restricted agency. Each configuration is empirically distinguishable in principle, but only with multi-marker assays; single-report scales would collapse the distinctions that make source-status and Mode B architecturally distinctive. This is why source-status and Mode B require multi-marker assays rather than single-report scales — and why protocol development is the highest-priority empirical bottleneck.


## 12.4 Source-compromise dynamics over time: persistence, decay, and repair

The architecture has a strong static vocabulary for source-status, but its dynamic vocabulary remains underdeveloped. A source-compromised action can be analyzed at the time of action, but the architecture still needs a better account of how source-compromise persists, decays, or is repaired across time.

This problem matters in several domains:

| Domain | Dynamic source-status problem |
|---|---|
| Manipulation | Does source-compromise disappear once the agent recognizes the manipulation? |
| Propaganda / ideology | Does distributed source-shaping decay when alternative sources become available? |
| Trauma-shaped agency | How does source-opacity change with stabilization, therapy, or new toolkit formation? |
| Addiction / compulsion | Does treatment restore source-cleanliness, improve Condition 4 coupling, or mainly improve mitigation? |
| Institutional capture | Does leaving a role undo the role's source-shaping effects? |
| Profile-formative decisions | Can later repair reclassify the attribution-status of earlier profile-formation? |

A future dynamic model would need to track at least four temporal variables: source-status at time $t$ ($S_t$); source-status after recognition / repair / environmental change ($S_{t+1}$); recognition status ($R_t$); mitigation / repair availability ($M_t$). But the architecture should not yet formalize this as a full dynamical system. The current paper has not established enough empirical or conceptual ground for that. The correct posture is to mark source-status dynamics as a future formalization target.

Key open question: does recognition of source-compromise repair source-status, merely create Mode B access to source-compromise, or generate a new accountability relation around mitigation and future prevention? These are different results. Recognition is not automatically repair. An agent who recognizes that they were manipulated has gained Mode B access to the manipulation; whether that recognition restores source-cleanliness for future similar actions, or merely opens a new mitigation / future-prevention obligation, depends on architectural details the present paper does not yet specify.

The dynamics question interacts with [Free Will §5.5] repair-accountability and [Free Will §5.3] source-status protocols. Without protocols for distinguishing source-compromise from source-cleanliness at any single time, dynamics across time cannot be measured; without dynamics, the architecture's longitudinal predictions (P18, cascade and profile-formation) lose part of their structural traction.


## 12.5 Repair-accountability when original responsibility is low

A related research-program open problem concerns repair-accountability. Section 9 allowed responsibility to relocate: from the moment of action to prior self-scaffolding, later repair, mitigation, or third-party source-shaping. But the architecture does not yet fully specify when repair-accountability persists despite low original responsibility.

Many real cases are mixed. Panic-driven harm: original responsibility is reduced by affective contraction, but later apology, repair, or prevention may be live. Addiction relapse: original responsibility is reduced if Condition 4 capture dominates, but treatment-seeking, environment-design, and repair may be live. Developmentally immature action: original responsibility is reduced by immature toolkit, but later learning and restitution may become live. Manipulated action: original responsibility is source-compromised, but later correction or warning may be live once manipulation is recognized. Institutional participation: original responsibility is role-constrained, but later disclosure, refusal, or collective repair may be live.

The hard question: can an agent be weakly responsible for the original act but strongly accountable for later repair? The architecture's likely answer is yes, but the paper should not over-formalize it yet. The reason is that repair-accountability depends on temporal change: the agent may lack Mode B access, live alternatives, or developmental capacity at $t_{action}$, but acquire them at $t_{later}$. A future account should distinguish six temporal-axis attribution relations:

| Temporal attribution relation | What it tracks |
|---|---|
| Original-act responsibility | The agent's relation to the act at $t_{action}$ |
| Recognition responsibility | The agent's relation to subsequent recognition that the act occurred / was harmful / was source-compromised |
| Mitigation responsibility | The agent's relation to live mitigation options as they arise |
| Repair responsibility | The agent's relation to repair-actions toward affected others |
| Future-prevention responsibility | The agent's relation to actions that would prevent recurrence |
| Profile-reconfiguration responsibility | The agent's relation to longer-term toolkit-development or scaffold-redesign that would change subsequent agency-configurations |

The present paper has the tools to name these but not yet the weighting rules to integrate them. Section 12 marks repair-accountability as an open subproblem of temporal attribution. The six-axis framework is offered as a structural decomposition target rather than as a developed weighting theory.


## 12.6 Developmental-window operationalization without moral or clinical overreach

The architecture uses developmental-window as a responsibility overlay (per 4.10, 8.2). It distinguishes pre-agential, immature, mature, scaffold-captured, and trauma-shaped agency. But operationalizing these windows is dangerous. It can slide into moralism, clinical overreach, paternalism, or crude capacity labeling.

The open problem: how can developmental-window status be empirically and structurally assessed without reducing agents to diagnostic labels or moral maturity scores?

A proper developmental-window protocol would need to preserve four distinctions:

| Distinction | Why it matters |
|---|---|
| Developmental capacity vs actual performance | A mature capacity may fail under stress |
| Toolkit absence vs toolkit non-use | Not exercising a capacity is not the same as lacking it |
| Externally imaginable vs internally live alternatives | Observers may see options the agent could not construct |
| Clinical category vs architectural profile | Diagnosis is not the same as agency-configuration |

This is especially important for ADHD-like implementation gaps, trauma-shaped agency, learned helplessness, depression, addiction, and anxiety. The architecture can frame these as agency-configuration changes, but the current paper does not supply clinical assessment instruments. Future work should build developmental-window assessment around profile evidence rather than labels: history of toolkit acquisition; order-specific option-space construction; live-option generation under varying state conditions; Mode B domain-specific access; scaffold availability; prior successful mitigation; response to structured support; repair capacity over time.

The guiding rule: developmental-window status should be inferred from agency-structure, not imposed from moral intuition or diagnostic category. This rule preserves the architecture's structural orientation while flagging the open empirical problem.


## 12.7 Neural and computational implementation of the operator-bundle

The architecture is implementation-neutral. It does not require substrate-indeterminism, a unique neural signature of free choice, or a one-to-one mapping between readiness potential and selection-event. Section 10 and Section 11 repeatedly preserve this neutrality: empirical paradigms test proxies, and predictions should concern multi-marker profiles rather than privileged neural signals. [Free Will §5.10] commits to predictive coding and executive-control as implementation candidates, not architectural reductions.

That neutrality is a strength, but it leaves a real research-program open problem: how does the operator-bundle relate to neural, behavioral, and computational implementation?

Future work could explore several non-exclusive implementation routes:

| Implementation route | Possible relation to architecture |
|---|---|
| Executive-control networks | May implement inhibition, task-switching, sustained control, or Condition 4 coupling |
| Predictive-control systems | May implement projection, affordance construction, and policy-selection analogues |
| Accumulator dynamics | May implement some thin-selection or spontaneous-action timing cases |
| Affective salience systems | May modulate $\Pi$-weighted evaluation without being identical to $\Pi$ |
| Memory / self-model networks | May support ownership-integration and Mode B access |
| Social-cognitive systems | May support constructed-order agency and source-status tracking |

The hard problem is not merely mapping architecture terms onto brain regions. That would be too crude. The better research question: which neural / behavioral patterns correspond to differences among preparation, option-construction, evaluative engagement, selection, implementation, report, ownership-recognition, and source-access?

The architecture should require convergent evidence rather than direct readout. A neural marker is relevant to the architecture only through an inferential bridge connecting it to an architectural object. The implementation-neutrality commitment marks this as a *principled limit*: the architecture cannot be reduced to specific neural implementations without abandoning its structural-perspectival object. Implementation-mapping is welcome as research; implementation-reduction would be architectural failure.

This is a clear case where DeepSeek's principled-limits discipline (item 8) applies: the architecture should not claim that it will eventually be reducible to a specific neural implementation. Some of the architecture's structural commitments (modeling-I anchor, ownership-integration, source-status overlay, Mode B object-domain) may resist neural-reduction even in mature neuroscience. That is not a defect; it is a structural feature of the architecture's inside-perspective object.


## 12.8 Cross-order temporal binding

A distinct implementation problem concerns cross-order temporal binding. The paper distinguishes willing across foundational orders: focus, thought, and substrate action, with constructed-order action extending into wider not-I coordination. But complex agency often involves multiple orders operating across overlapping temporal windows.

Examples: choosing to speak (thought-selection, focus-direction, and substrate action must coordinate); asking someone for help (constructed-order target-domain action depends on thought, speech, social timing, and predicted response); inhibiting anger (affect-contraction, focus redirection, thought reframing, and motor inhibition interact); skilled performance (focus, perception, motor coupling, implicit evaluation, and post-action Mode B access operate at different rates); institutional decision (role-based option-space, social coordination, document production, and downstream cascade unfold over extended time).

The architecture currently has the conceptual resources to classify these cases, but it does not yet specify their temporal integration in detail. Open questions:

How are order-specific selection-events synchronized? Can one order select while another remains in deliberation? Does cross-order coordination require a higher-order selection-event, or can it emerge through bundled coupling? How should delayed Mode B access be modeled when different orders become reflectively available at different times? How do constructed-order actions preserve ownership when implementation is distributed through other agents, tools, and institutions?

A future model of cross-order temporal binding would extend the timing-marker apparatus from Section 10:

$$t_{prep} \not\equiv t_{select} \not\equiv t_{report} \not\equiv t_{move} \not\equiv t_{outcome} \not\equiv t_{recognize}$$

into an order-indexed version:

$$t^{(o)}_{prep},\ t^{(o)}_{select},\ t^{(o)}_{implement},\ t^{(o)}_{recognize}$$

where $o$ indexes focus, thought, substrate action, or constructed-order domain. The order-indexed extension would mark which timing-markers belong to which order, and would enable empirical work on cross-order coordination. That formalization should remain future work; the current paper only needs to flag the need.

*A worked example of cross-order timing complexity.* Choosing to speak in a tense conversation may involve first-order focus-stabilization before speech ($t^{(focus)}_{prep}$ before $t^{(focus)}_{select}$), second-order thought-selection of what to say ($t^{(thought)}_{select}$, possibly overlapping focus-stabilization), third-order motor implementation of speech ($t^{(action)}_{implement}$, lagging both focus and thought selection), and constructed-order anticipation of the other person's response (a constructed-order projection that operates concurrently with all of the above). These order-specific timing-markers may not align: focus-stabilization may complete before thought-selection has converged; thought-selection may revise after motor implementation has begun; constructed-order anticipation may fail to integrate with all three. The future formalization problem is to model their coordination without collapsing them into one global decision-time. This is also why single-decision empirical paradigms (Libet-class, Soon-class) cannot capture the cross-order architecture: they measure one timing-marker for one order, and treat that as decisive for "the decision," when in fact decisions structurally distribute across orders with non-aligned timing.


## 12.9 Group-agency modeling without group-mind

The architecture rejects group-mind reification. Collective and institutional responsibility are treated as profile-indexed distributions across agents, roles, source-relations, and cascade positions. [Free Will §5] preserves this as a central refusal: group responsibility is not group mind, and perspectival realism requires role-indexed agent profiles. P17 specifies that role-indexed structural variables (authority, information-access, discretion, expertise, mitigation-power, repair-option availability, cascade-foreseeability) provide the architecture's attribution-input profile better than unindexed group-membership.

But rejection of group-mind is not yet a complete model of group agency. The open problem: how can the architecture model distributed agency without positing an unindexed collective I?

Several configurations require sharper formalism:

| Configuration | Modeling difficulty |
|---|---|
| Team action | Multiple agents coordinate around a shared target without becoming one I |
| Institutional decision | Role-space shapes action, but no institution becomes a literal modeling I |
| Distributed ignorance | No one agent sees the whole cascade, but information-sharing structures may be available |
| Leadership | One constructed-order agent shapes the option-space of many others |
| Bureaucratic harm | Small role-indexed actions accumulate into large cascade effects |
| Collective repair | Repair may be distributed even when original responsibility is partial or unclear |

A future model would need to represent the set of individual attribution profiles across multiple agents, $\{AP_{m_i, t; a_i}\}_{i=1}^{n}$, plus the relational structure connecting them: who shaped whose option-space; who had authority; who had information; who had discretion; who could mitigate; who could repair; who could foresee cascade effects; who could alter the scaffold. The architecture's future group-agency model should therefore be agent-indexed and relation-indexed, not group-mind-indexed.

The relational structure is genuinely difficult. Standard distributed-systems formalisms (graphs, hypergraphs, organizational charts) capture some of the structure but not the agency-relevant subset. The architecture would need to specify which relations matter for attribution-input purposes (option-space-shaping, information-flow, discretion-distribution, cascade-foreseeability) and how those relations interact with the individual $AP$ profiles. This is a substantial formalization target.

## 12.10 Therapeutic and clinical translation

The architecture has clinical-adjacent implications, especially through P14: order-matched training / intervention should predict order-specific option-space expansion and response. But Section 11 explicitly treats P14 as a research prediction, not treatment advice. [Free Will §5] similarly leaves therapeutic and clinical translation open.

The open problem: how can agency-architecture distinctions be translated into clinical or therapeutic research without becoming an unvalidated clinical protocol?

The architecture could eventually help distinguish:

| Clinical-adjacent phenomenon | Architectural lens |
|---|---|
| ADHD-like implementation gap | Mode B recognition may coexist with unreliable sustained implementation |
| Addiction / compulsion | Condition 4 capture, source-pressure, mitigation availability, repair-accountability |
| Learned helplessness | Projection-toolset impairment and live-option collapse |
| Trauma cue activation | Source-opaque contraction and altered developmental-window status |
| Depression / anhedonia | Salience / projection / initiation impairment; affect-mediated agency contraction |
| Anxiety | Threat-weighted projection, overchecking, avoidance, or paralysis |

But the architecture must not claim clinical authority from structural elegance. Clinical translation requires validation: operational definitions; validated measurement instruments; domain-specific clinical collaboration; longitudinal designs; comparison against existing clinical models; safeguards against moralizing impairment; clear separation of research prediction from treatment recommendation.

The architecture's stance, stated explicitly: *the architecture may become clinically useful only if its order-specific and profile-specific distinctions improve assessment, intervention design, or outcome prediction under independent validation. Until then, clinical translation remains an open research program.* Premature clinical application would compromise both the architecture's empirical discipline and the patient populations it might affect.


## 12.11 Cross-cultural attribution and reactive-attitude variation

The architecture distinguishes structural attribution-inputs from folk responsibility judgments. This preserves the P17 discipline: the architecture does not predict that people will assign responsibility correctly or uniformly; it predicts that role-indexed structural variables matter to the attribution-input profile.

But human attribution practices vary across cultures, institutions, legal systems, religions, and moral communities. That creates an open problem: how should the architecture relate structural attribution-inputs to culturally variable attribution practices?

Possible variation points include: ownership reports (cultures may differ in how ownership is linguistically or socially expressed); sourcehood sensitivity (some communities may emphasize internal intention; others may emphasize role, duty, or relational embeddedness); accountability practices (repair, shame, punishment, apology, reconciliation, and exclusion may be differently organized); agency ideals (individual autonomy, relational harmony, obedience, skill, devotion, or non-attachment may be differently prioritized); Mode B expression (reflective object-access may be cultivated, discouraged, ritualized, or linguistically unavailable in different ways).

This does not mean the architecture should relativize its structural distinctions. It means structural distinctions and attribution practices are different objects. Future work should distinguish: structural attribution-input profile (architectural); cultural interpretation of that profile; normative response practice; legal / institutional codification; phenomenological self-report vocabulary.

The open problem is not whether cultures differ — they do. The hard problem is how to model those differences without collapsing structural agency into local social practice. The P17 patch discipline provides architectural orientation: cross-cultural attribution-judgment patterns are downstream measurements of whether different communities track architectural attribution-inputs in different ways, not architectural-input variables themselves.


## 12.12 Empirical-design problems not promoted to prediction-status

Section 11 promoted only candidates that satisfied four criteria: architectural derivability, operational marker, discriminator value, and pressure condition. This left several empirical-design problems unpromoted. The current section gathers them without upgrading them to predictions.

| Deferred empirical-design problem | Why not yet promoted |
|---|---|
| Fine-grained source-status assays | Marker sets remain underdeveloped (per [Free Will §5.3]) |
| Mode B object-domain batteries | Need domain-specific protocol design (per [Free Will §5.3]) |
| Cross-order temporal-binding measures | Timing and order-indexing need formalization (per [Free Will §5.8]) |
| Developmental-window measures | Risk of moral / clinical overreach (per [Free Will §5.6]) |
| Cascade-management availability assays | Need clearer task designs separating foreseeability, mitigation, and repair |
| Institutional role-discretion metrics | Need formal role-structure representation (per [Free Will §5.9]) |
| Contemplative agency measures | Require cross-tradition vocabulary and practitioner collaboration (per [Free Will §6.4]) |
| Source-compromise dynamics measures | Require longitudinal designs with operational source-status protocols (per [Free Will §5.4]) |
| Repair-accountability measures | Require six-axis temporal decomposition (per [Free Will §5.5]) |
| Cross-cultural attribution-input measures | Require cross-cultural collaboration (per [Free Will §5.11]) |

These are not failed predictions. They are *pre-prediction research problems*: candidate empirical programs that need better markers or pressure conditions before Section 11-style promotion. The drafting rule preserves the Section 11 / Section 12 boundary: do not promote Section 12 problems into predictions unless they can satisfy the Section 11 prediction-status criteria. This preserves the paper's empirical discipline.


## 12.13 Priority map for future work

The open problems are not equally urgent. Some are needed for near-term empirical development; others are long-range philosophical or translational projects. The priority map below identifies dependency order — which open problems other open problems depend on — rather than absolute importance.

| Priority | Open problem | Reason | Work-type |
|---|---|---|---|
| 1 | Source-status and Mode B operationalization (12.3) | Required to test several flagship predictions (P5, P7, P8, P12, P14) | Empirical operationalization |
| 2 | Source-compromise dynamics and repair-accountability (12.4, 12.5) | Required for longitudinal manipulation, trauma, addiction, and institutional cases | Empirical operationalization + formal |
| 3 | Formal weighting among profile axes (12.1) | Needed for mature responsibility-attribution applications | Formal |
| 4 | Group-agency without group-mind (12.9) | Needed for institutional, political, and collective action applications | Formal + application |
| 5 | Neural / computational implementation of operator-bundle (12.7) | Needed for deeper empirical integration; principled limits on reduction must be preserved | Empirical + principled-limit |
| 6 | Developmental-window operationalization (12.6) | Needed for clinical-adjacent and developmental research | Empirical operationalization |
| 7 | Cross-order temporal binding (12.8) | Needed for complex cross-order action research | Formal |
| 8 | Cross-cultural attribution practice (12.11) | Needed to avoid overlocalizing attribution assumptions | Cross-cultural empirical |
| 9 | Contemplative / no-agent translation (13.15) | Needed for faithful wisdom-tradition comparison | Cross-cultural dialogical |
| 10 | Source-sensitive Frankfurt descendants (13.16) | Needed for philosophical completeness | Comparative-philosophy |
| 11 | Self-determination theory engagement (13.17) | Promising psychological comparison; foundational dependency on operationalization protocols | Comparative-psychology |
| 12 | Therapeutic and clinical translation (12.10) | Required validation; depends on operationalization protocols | Translational-applied |
| 13 | Minimal accountability thresholds (12.2) | Application-specific; depends on weighting work | Formal |
| 14 | Foundation-level metaphysical residue (13.2) | Principled limits; foundation-level work, not application-paper-level | Foundation-extension |
| 15 | Theological resonance (13.3) | Non-licensed translational territory; requires explicit theological extension | Translational-theological |

The priority map is dependency-ordered, not importance-ordered. Higher-ranked problems are typically prerequisites for lower-ranked work. Source-status and Mode B operationalization (rank 1) come first because many later research-program problems require them. Foundation-level metaphysical residue (rank 14) and theological resonance (rank 15) are ranked last not because they are unimportant but because their resolution belongs to foundation-extension or theological-extension projects rather than application-level work, and because progress on them does not gate progress on the empirical research program.

The map has fifteen rows rather than one row for every numbered open-problem entry because some entries are dependency-paired and some are cross-cutting. Source-compromise dynamics (12.4) and repair-accountability (12.5) are paired in priority row 2 because their operational and formal dependencies overlap. Empirical-design problems not promoted to prediction-status (12.12) are not ranked as an independent domain because they are distributed across the other rows; 12.12 functions as a boundary-preserving catalogue of pre-prediction design problems rather than as a separable research program.

The work-type column classifies each open problem by the kind of work its resolution would require: empirical operationalization, formal mathematical, application-development, comparative-philosophy, comparative-psychology, cross-cultural empirical, cross-cultural dialogical, translational-applied, foundation-extension, translational-theological, or principled-limit acknowledgment. The taxonomy clarifies which open problems belong to which kind of future research and prevents the open-problems list from reading as an undifferentiated set of admissions.


## 12.14 Summary

Section 12 has identified the architecture's unresolved problems without treating them as contradictions. The seventeen open-problem entries engaged are:

(1) Foundation-level metaphysical residue (ultimate sourcehood, primal not-I, lawful-frame dependence, tautological cogito limit, substrate givenness, normative sufficiency); (2) theological resonance with strict translation-not-derivation discipline; (3) formal weighting among profile axes; (4) minimal accountability thresholds; (5) operationalization of source-status and Mode B; (6) source-compromise persistence, decay, and repair; (7) repair-accountability when original responsibility is low; (8) developmental-window operationalization; (9) neural and computational implementation of the operator-bundle; (10) cross-order temporal binding; (11) group-agency modeling without group-mind; (12) therapeutic and clinical translation; (13) cross-cultural attribution practice; (14) contemplative / no-agent translation limits; (15) source-sensitive Frankfurt-class descendants; (16) Self-determination theory engagement; (17) empirical-design problems not yet promoted to prediction-status. The 12.13 priority map orders these by dependency for future work and classifies each by the work-type its resolution requires.

The paper's position is therefore not that the agency architecture is complete. The position is more precise: the architecture supplies a coherent structural account of free choice, agency-variation, responsibility-attribution, empirical interpretation, prediction, and framework translation; it also exposes the next problems that must be addressed, delimited, or developed for the architecture to mature. Some of these problems are principled limits (foundation-level residue, neural-implementation neutrality) that the architecture acknowledges as outside its scope rather than deferring as eventually-solvable. Others are research-program targets that future application papers, foundation extensions, or empirical collaborations can engage.

> *The architecture has not solved every problem of agency. It has transformed the problem-space: from undifferentiated debate over "free will" to a structured taxonomy of agency-conditions, variation-families, attribution profiles, empirical markers, prediction profiles, framework translations, and open research programs.*




---

# 13. Conclusion: from problem to apparatus

## 13.1 What this paper has constructed

This paper has constructed agency as an inside-perspective structural architecture and replaced the undifferentiated treatment of agency phenomena with a structured field of analyzable distinctions. Beginning from the six-condition definition of free choice supplied by the companion paper, this paper generalized willing across order-indexed domains (focus, thought, substrate-mediated action, and constructed orders); developed the verification-toolkit and live-option construction lemma; analyzed will, trying, and effort as operator-bundle direction under resistance; developed deliberation, decision-events, and order-asymmetric Mode B reflective availability; derived a seventeen-family variation taxonomy with ten-axis diagnostic schema; built the triadic ownership / responsibility / accountability attribution apparatus through the ten-component attribution profile $AP_{m,t;a}$; mapped empirical paradigms to architectural objects through the empirical interpretation profile $EIP_p$ with timing-marker non-identity chain; promoted eighteen formal predictions across seven families through the prediction profile $PP_i$; and catalogued agency-domain open problems with priority map.

The paper introduced no new foundation-level primitives. Every commitment traces back to Foundation v5.3.3's $\kappa/\phi/\rho/\Pi$ coordinates and $A_{m,t}(x)$ phenomenal-availability status predicate, the indexed modeling I, $PtCns$ and $PCE$ prerogatives, Modes A/B/C, and the three-order pathway typology — together with the six-condition definition of free choice from the companion paper. What this paper added at the application level was four section-level structural objects — the attribution profile $AP_{m,t;a}$, the empirical interpretation profile $EIP_p$, the prediction profile $PP_i$, and (in the companion paper) the framework translation profile $FTP_f$ — each doing different analytical work without collapsing into one another.

## 13.2 Structural coherence: order-indexed willing, toolkit, and variation

Sections 4 through 8 construct the agency taxonomy by structural derivation rather than by external symptom-mapping or folk-category enumeration. The same six conditions of the companion paper apply across foundational orders of willing — focus, thought, and substrate-mediated action — with order-translated implementation semantics, and generalize to constructed orders 4 and above through toolkit-development and mastery.

| Architectural move | Conclusion-level significance |
|---|---|
| Order-indexed willing | Agency is not only motor action; it includes focus-direction, thought-selection, substrate-mediated implementation, and constructed target-domains |
| Toolkit development and mastery | What an agent can will depends on what their verification-toolkit can construct as live |
| Effort / agency-quality separation | Effort tracks resistance under operator-bundle commitment, not agency-strength |
| Variation taxonomy (Section 8) | "Unfree," "compelled," "habitual," "automatic," "manipulated," and "alienated" are not one category — each names a structurally different configuration |

The result is one coherent structural field: the I-relative agency profile operating under lawful structural frame, with attribution, empirical interpretation, prediction, and (in the companion paper) framework translation each requiring distinct analyses through the four section-level objects. Agency is not treated as a binary property that actions either possess or lack; it is treated as a structured configuration whose components can be present, thin, damaged, source-compromised, developmentally unavailable, or distributed across time and relation.

## 13.3 Attribution apparatus

Section 9 developed the triadic dissociation of ownership, responsibility, and accountability. The deeper architectural commitment is that responsibility is not a conserved quantity. Attribution can be distributed across agents, relocated to prior self-scaffolding or later repair, reduced under condition-failure, or temporally shifted across the act-recognition-mitigation-repair sequence — without disappearing into either total blame or total exculpation. The full philosophical engagement with manipulation-as-paradigm-case lives in the companion paper [Free Will §4]; the structural attribution apparatus that supplies its inputs lives here.

## 13.4 Empirical tractability

Sections 10 and 11 demonstrated that the architecture is empirically engageable. The Libet, Wegner, and Soon-class paradigms were analysed through the order-specific timing-marker apparatus and the multi-marker structural distinctions, rather than treated as decisive refutations or confirmations of agency. The architecture's empirical contribution is not to claim the existing literature has confirmed it; it is to claim the existing literature is now structurally interpretable through it, and to specify which patterns would pressure, qualify, or force revision.

| Backbone prediction | Conclusion-level significance |
|---|---|
| P1 — Thin / rich multi-marker divergence | Tier-structure differences are detectable across condition-profile, not by single-marker probes |
| P5 — Ownership / sourcehood dissociation under manipulation (flagship) | Owned action can remain source-compromised without becoming non-agency |
| P8 — Mode B availability vs exercise in flow / mastery | Flow can reduce in-action reflection while preserving post-action object-access |
| P9 — Effort dissociates from agency-quality | Effort is resistance-profile, not moral or agency strength |
| P10 — Chosen-habit vs compulsive-habit five-marker split | Owned routinized action is structurally different from substrate-captured habit |
| P14 — Order-matched training / intervention | Order-specific option-space expansion is mediated by toolkit-development, not merely by symptom-improvement |
| P18 — Longitudinal cascade profile-formation | Three-stage output-imprinting cascade is an agency object that single-trial paradigms cannot capture |

The eleven additional predictions extend or specify these backbones. Together, the eighteen predictions make the architecture's empirical commitments explicit and falsifiable.

## 13.5 Open problems and research-program development

Section 12 catalogued the agency-domain open problems with priority and work-type classification. The companion paper catalogues foundation-level metaphysical residue, theological resonance, and contemplative-translation limits as principled-limit residue rather than research-program targets. Together, the two papers form the seventeen-entry open-problem catalogue of v0.2.3.

The architecture's open problems are not weaknesses; they are research-program affordances. Formal weighting among profile axes, source-compromise dynamics over time, neural implementation of the operator-bundle, cross-order temporal binding, group-agency modeling without group-mind, therapeutic translation under safeguards against clinical overreach, cross-cultural attribution variation, and the longitudinal empirical designs that only Section 11's cascade predictions require — each is a tractable target for future application work, foundation extensions, or empirical collaborations.

## 13.6 Place in the larger book projection

This paper is split B of the architecture's third application paper, focused on the structural and empirical contribution. The companion paper *Free Will in the Two-Layer Identity-Correlation Architecture* develops the philosophical contribution: the six-condition definition, the manipulation paradigm with explicit ownership / sourcehood dissociation, the eight framework translations, and the foundation-level metaphysical residue.

The agency domain is the third application of the architecture; the first was *Temporal Phenomenology* and the second was *Differentiated Affect*. The architecture's projected book series will continue with applications to the narrative self, dreams and altered states, intersubjectivity beyond the prerogative of consistency, aesthetic experience, and the formal derivation of the structural prerogatives from the operating lived-I architecture. The agency taxonomy this paper develops will be used as the structural-anchor wherever subsequent applications engage agency-relevant configurations.

| Future research / application domain | Agency-paper handoff |
|---|---|
| Intersubjectivity and recognition | Other-I / inter-I formalization needs (per [Free Will §6.2]), constructed-order agency (§5.7), role-indexed attribution-inputs (§9.13), manipulation continuum (§5.9) |
| Ethics and normativity | Triadic ownership / responsibility / accountability apparatus (§9), profile-indexed attribution rejecting responsibility-as-conserved-quantity, repair-accountability decomposition |
| Social and institutional theory | Group-agency modeling without group-mind reification (§9.13), cascade and distributed-ignorance, constructed-order agency (§8.16), role-discretion / authority / information-access structures |
| Clinical and therapeutic application | Order-specific agency damage typology (§8.9–§8.11), Mode B availability vs implementation distinction (§7.6), P14 order-matched training research program, developmental-window operationalization ([Free Will §5.6]) with safeguards against clinical overreach |
| Cross-cultural and contemplative engagement | Theological resonance guardrails [Free Will §6.3], no-agent translation limits with indexed-I preservation [Free Will §6.4], cross-cultural attribution-input vs attribution-practice distinction ([Free Will §5.11]), P17 folk-judgment boundary discipline |
| Empirical cognitive science | Three section-level structural objects ($AP$, $EIP$, $PP$), timing-marker non-identity chain (§10.3), post-hoc / source-opacity / confabulation triad (§7.9), source-status and Mode B protocol-design problems ([Free Will §5.3]) |

## 13.7 Final synthesis

The architecture transforms specific agency-relevant questions into specific architectural questions:

| Common framing | Architecture's structural replacement |
|---|---|
| "Did neuroscience disprove agency?" | Which empirical marker is being measured, and which architectural object does it probe ($EIP_p$)? See timing-marker non-identity chain (§10.3). |
| "Is agency just a story?" | Which reports are post-hoc recognition (genuine), source-opacity (genuine but inarticulate), or confabulation (not tracking actual selection)? The triad is structurally distinct (§7.9, §10.7). |
| "Can groups be responsible?" | Which agents, roles, relations, source-shaping paths, and cascade positions structure the role-indexed attribution-input profile? (§9.13) |
| "Is addiction a disease or a choice?" | Which substrate-coupling failure modes are operating (preemption, bypass, capture)? What is the developmental-window status? Are repair-options live? Each is a separate structural question (§8.8, §9.6). |
| "Why does ADHD treatment improve outcomes despite same effort?" | Order-matched intervention adjusts the toolkit's order-specific implementation-gap, not the agent's effort-level. Effort tracks resistance, not agency-quality (§8.9, §6.9). |

Agency retains its lived complexity, felt depth, phenomenological integrity, and practical stakes. What changes is that we now have apparatus for analyzing it. Future work — empirical, clinical-adjacent, cross-cultural, and dialogical — will test, refine, and extend that apparatus. The paper supplies the structural skeleton; the collaborative research program that follows will determine how far the architecture can carry the analysis while preserving the lived reality it seeks to illuminate.

> *The agency architecture's structural taxonomy does not deliver verdicts on agency-or-not. It makes the analysis structurally navigable.*


---

# Glossary of architectural terms


## Usage note

This glossary stabilizes the terminology used in the agency paper. It defines terms according to their role inside the Two-Layer Identity-Correlation Architecture and the present agency application. It is not a replacement for the foundation document set, not a general philosophy dictionary, and not a source of new architectural commitments. Where a term comes from an external framework, the entry defines only the sense relevant to this paper. Foundation-level terms are summarized at the level needed for this paper's usage; for full derivation, see Foundation v5.3.3. The glossary defines already-stabilized usage; it does not create new usage.

## Status tags

Each entry carries one or more tags indicating its role in the architecture:

- **Foundation** — Term inherited from Foundation v5.3.3.
- **Agency** — Term introduced or specialized in this agency paper.
- **Attribution** — Section 9 ownership / responsibility / accountability apparatus.
- **Empirical** — Section 10 / 11 empirical-interface or prediction term.
- **Translation** — [Free Will §5] framework-comparison or external-framework term.
- **Open problem** — open-problem residue or future-work term.

A term may carry more than one tag when it operates across roles (e.g., *Foundation / Agency* for a foundation term central to the agency paper's specialization).

## Notation and formal objects

The architecture uses the following symbols and formal objects throughout the paper:


**Accountability** — *Attribution.* Structural addressability for explanation, demand, mitigation, repair, or response. Accountability is not identical to blame, punishment, legal liability, or moral desert; nor is it identical to ownership or responsibility. It is the third leg of the triadic dissociation in Section 9 (ownership / responsibility / accountability) and depends on the full attribution profile, including ownership, source-status, developmental-window, Mode B availability, and live mitigation or repair options. See also: ownership; responsibility; repair-accountability; $AP_{m,t;a}$. (Sections 9.1, 9.4, 9.6, 9.10)

**Action-space lattice** — *Agency.* The structured space of available action-options in a given configuration, organized by order, target-domain, and toolkit-coverage. The lattice is constructed by the verification-toolkit's order-indexed live-option construction; it is not a fixed metaphysical menu of possibilities. (Sections 5.4, 5.7)

**Addiction-like capture** — *Agency.* A variation-family in which substrate coupling is captured by sustained reward-pathway activity, producing condition-failure modes typically including sourcehood compromise (substrate-driven option-shaping), evaluative narrowing, and reduced operator-bundle reach. Addiction-like capture is not the same as compulsion, habit, or akrasia; it has its own structural signature in $AP_{m,t;a}$. (Section 8.7)

**ADHD-like configurations** — *Agency.* Variation-family (Section 8.9) in which substrate-developmental constraint at orders 1–2 (focus, thought) impairs sustained operator-bundle mediation, producing characteristic implementation-gap dynamics: live-option representability, evaluability, and inhabitability are often intact, but implementability over duration is unstable; dynamic-refinement-during-execution is especially affected. The configuration is *not* a uniform motivational deficit; configurational and slingshot willing strategies often show proportionally favorable effort-economy when the toolkit has developed them as live. ADHD-like configurations are referenced in P12 and P14 of the prediction profile. See also: implementation gap; substrate coupling; configurational willing; slingshot willing; backbone predictions. (Section 8.9)

**Agency** — *Agency.* The inside-perspective structural configuration by which the indexed modeling I constructs, evaluates, selects, and integrates action through order-indexed willing across foundational and constructed domains. Agency is not a single binary property, a third-person behavior, a neural readiness signal, a folk responsibility judgment, or a metaphysical power added to the substrate. The architecture treats agency as a multi-dimensional structural configuration with dissociable components. See also: agency event; agency-as-such; free choice proper. (Sections 2, 4)

**Agency event** — *Agency.* A specific instantiation of agency in time: a particular live-option construction, evaluation, selection, substrate-coupling, Mode B availability, and ownership-integration profile, indexed to moment, agent, target-domain, and order. Agency events are the basic units of structural analysis in the paper. (Section 4.3)

**Agency-as-such** — *Agency.* Agency considered abstractly as a property an agent has or lacks. The paper does not treat agency-as-such as a meaningful direct-measurement target; agency is structural configuration, and only specific architectural objects (live-option construction, evaluative engagement, substrate coupling, Mode B availability, ownership-integration, source-status, etc.) are directly probeable. (Section 10.2)

**Agency-quality** — *Agency.* The architectural assessment of how well a given agency event satisfies the six conditions of free choice across order-engagement, ownership-integration, and source-status. Agency-quality is *not* the same as effort: a high-effort agency event can be low-quality (capture under struggle), and a low-effort agency event can be high-quality (mastery in flow). See also: effort; effort-economy; flow; mastery. (Sections 6.8, 6.9)

**Akrasia** — *Agency.* A variation-family in which evaluative engagement (Condition 2) is intact but operator-bundle selection (Condition 3) does not deliver the evaluatively-favored action; the agent acts against their own evaluation. Akrasia is *not* the same as compulsion: in compulsion, evaluative engagement itself is bypassed or dominated by capture; in akrasia, evaluation occurs but is not action-determining. (Section 8.4)

**Alienation** — *Agency.* A variation-family in which ownership-integration (Condition 6) fails: the action does not register as the agent's own. Alienation is *not* the same as compulsion (which can preserve ownership-integration) or confabulation (which can preserve a false sense of ownership over manipulated action). (Section 8.11)

**Answerability** — *Attribution.* A scoping form of accountability: the structural condition in which an agent is appropriately addressed for explanation or response regarding an action or cascade. Answerability is one mode of accountability and does not exhaust it. (Section 9.6)

**Asymptotic layer** — *Foundation.* In Foundation v5.3.3 (File 1 §2.6; File 3 §6.1), the content domain $\mathsf{A}^m_t$ — the set of non-intrinsic items in the modeling I's field at time $t$, containing both conscious and unconscious contents. The asymptotic layer is a content domain, not a developmental layer of the I itself; it is what the three coordinates $\kappa$, $\phi$, $\rho$ are placed on. The paper inherits this concept as background; for full development, see Foundation File 1 §2.6 and File 3 §6.1.

**Attribution** — *Attribution.* The structural assessment of whether and how the dissociable relations of ownership, responsibility, and accountability hold for a given agent, moment, and action or cascade. Attribution is computed through the attribution profile $AP_{m,t;a}$; it is not a single binary verdict and is not a conserved quantity transferred between agents. See also: $AP_{m,t;a}$; profile-indexed attribution. (Sections 9.2, 9.4)

**Attribution profile $AP_{m,t;a}$** — *Attribution.* The ten-component structural object that organizes the triadic dissociability of ownership, responsibility, and accountability for a given act or cascade $a$ at moment $m$ in agent / modeling I $t$. Its ten components are $V$ variation-family, $O$ ownership-status, $S$ source-status, $C$ condition-profile, $B$ Mode B object-domain availability, $D$ developmental-window, $K$ cascade profile, $M$ mitigation / repair options, $R$ role / order profile, and $T$ temporal locus, written $AP_{m,t;a} = \langle V, O, S, C, B, D, K, M, R, T \rangle$. The profile yields a structural attribution rather than a binary free / unfree verdict. See also: profile-indexed attribution; ownership; responsibility; accountability. (Section 9.4)

**Attribution-object** — *Attribution.* A specific architectural object to which attribution applies: typically the decision-event, trying, action, outcome, cascade, or source-shaping pathway. The architecture distinguishes attribution-objects rather than treating attribution as applying to "the act" undifferentiated. See also: cascade-attribution. (Section 9.2)

**Automaticity** — *Agency.* A variation-family in which an action is implemented through routinized substrate coupling without active evaluative engagement at the moment of action. Automaticity is *not* the same as compulsion (which involves capture against evaluation) or absence of agency: chosen-habitual automaticity preserves prior ownership-integration and can be high-quality; compulsive automaticity does not. See also: habit; flow; mastery. (Section 8.6)

**Backbone predictions** — *Empirical.* Seven of the paper's eighteen predictions identified as the paper's empirical spine: P1 (thin / rich choice multi-marker divergence), P5 (ownership / sourcehood dissociation), P8 (Mode B availability vs exercise vs report), P9 (effort / agency-quality dissociation), P10 (chosen-habit vs compulsive-habit signatures), P14 (order-matched training and intervention), and P18 (longitudinal cascade and profile-formation). The seven backbone predictions carry the principal empirical load; the other eleven predictions extend or specify them. The architecture's empirical traction depends primarily on the backbone profile holding under pressure conditions. See also: pressure condition; prediction profile. (Section 11.4)

**Cascade-attribution** — *Attribution.* The structural assessment of attribution for outcomes downstream of an action through cascade pathways (foreseeable consequences, source-shaping of others, institutional propagation, longitudinal effects). Cascade-attribution operates through cascade-foreseeability, role-indexed attribution-input, and the cascade-attribution test; it is not the same as attribution to the original action and may distribute differently across agents. (Sections 9.7, 9.10)

**Cascade-attribution test** — *Attribution.* The six-gate procedure for assessing cascade-attribution: foreseeability, controllability, role-position, mitigation-availability, source-shaping pathway, and downstream-cascade-density. Each gate generates a structural finding; the test does not deliver a single binary verdict but a profile-indexed cascade attribution. (Section 9.10)

**Cascade-foreseeability** — *Attribution.* The structural assessment of whether and how an agent could foresee the cascade-effects of an action, given the agent's profile, position, and toolkit at the moment of action. Cascade-foreseeability is one input to cascade-attribution; it is not itself an attribution verdict. (Section 9.7)

**Clinical translation** — *Open problem.* The translation of the architecture's variation-family analyses into clinical context for diagnostic, therapeutic, or rehabilitative purposes. The architecture supplies structural inputs for clinical translation but does not license clinical authority, diagnostic verdicts, or treatment recommendations; clinical translation requires independent clinical validation and is treated as a research-program problem. ([Free Will §5.10])

**Coercion / coerced choice** — *Agency / Attribution.* A source-status and option-space configuration in which threat, pressure, or imposed constraint structures the live-option space. Coercion may leave ownership intact while compromising sourcehood; it therefore requires attribution-profile analysis rather than automatic exculpation or automatic responsibility. See also: source-status; manipulation; constrained choice; $AP_{m,t;a}$. (Sections 5.9, 8)

**Cogito (tautological cogito)** — *Foundation.* In Foundation v5.3.3 (File 1 §2.4), the tautological postulate $\hat\iota_m = \hat\iota_m$: the indexed modeling I asserted as self-identical. The cogito is a *postulate*, not a derivation; it articulates the form (indexed self-identity) of an already performatively self-evident existence. Reflexivity is the universal logical structure that characterizes the form, not the source. The agency paper inherits the cogito as background for the indexed modeling I; it does not redefine or develop it. See also: indexed modeling I.

**Compatibilist-coherent** — *Translation.* The architecture's stance toward compatibilism: the structural commitments of the paper are coherent with compatibilist positions and translate cleanly to many compatibilist concerns, but the paper does *not* claim to prove compatibilism. The compatibilist-coherent stance preserves hard-incompatibilist residue (ultimate sourcehood remains an open question the architecture does not answer) and does not foreclose libertarian or hard-incompatibilist positions on substrate-metaphysical grounds. (Sections 9.15, 12.3)

**Compulsion** — *Agency / Attribution.* A variation-family in which substrate-coupling is compromised by capture, bypass, or preemption, making it primarily a Condition 4 failure or thinning. Compulsion may secondarily distort evaluative engagement (Condition 2) or operator-bundle selection (Condition 3), but it is not defined by evaluative misalignment alone. *Not* the same as akrasia: akrasia is, by default, a Condition 3 evaluation / selection misalignment without Condition 4 capture. *Not* the same as habit (which may preserve ownership-integration) or addiction-like capture (which has its own profile). See also: capture; akrasia; addiction-like capture; substrate coupling. (Section 8.5)

**Confabulation** — *Agency / Empirical.* The post-hoc construction of a report about one's own action that does not accurately track the action's actual source-pathway. Confabulation is *not* the same as post-hoc recognition (which tracks the source-pathway accurately given source-opacity) or alienation (which is failure of ownership-integration itself). The post-hoc recognition / source-opacity / confabulation triad (7.9) distinguishes these structurally. (Section 7.9)

**Configurational willing** — *Agency.* A willing-strategy in which the agent configures the substrate (environment, body, toolkit) to make a desired action more accessible or a competing action less accessible, without willing the action itself directly at the moment of action. Configurational willing is one of three principal willing-strategies (alongside direct and slingshot). It is often more effort-efficient than direct willing for high-resistance actions. (Section 6.7)

**Constructed order** — *Agency.* An order of willing beyond the three foundational orders (focus, thought, substrate-mediated action), constructed through toolkit-development and mastery in target-domains such as asking, directing, team coordination, institutional engagement, and beyond. Constructed orders extend the order-indexed willing pathway by N-order generalization (5.7). They are not foundation-level primitives; they are application-level extensions of the toolkit-development pathway. See also: order-indexed willing; N-order will; toolkit-development. (Sections 5.7, 5.8)

**Contact ($\kappa$)** — *Foundation.* See Notation and formal objects above. The foundation coordinate by which a content makes contact with the indexed modeling I. Inherited from Foundation v5.3.3.

**Contrastive live-option space** — *Agency.* The structured space of multiple distinguishable, evaluable live options that Condition 1 of free choice requires. The contrastive nature of the option-space is essential: a single available action without contrast is not free choice, and a contrast that is merely nominal (the alternative is not actually live) does not satisfy Condition 1. See also: live option; live-option space; six conditions of free choice. (Section 3.2)

**Cross-cultural attribution practice** — *Open problem.* The cross-cultural variation in attribution practices around ownership, responsibility, and accountability, which interfaces with the architecture's attribution apparatus but is treated as a separate research-program problem. The architecture supplies structural inputs for cross-cultural attribution analysis but does not claim cross-cultural universality of any specific attribution-verdict. ([Free Will §5.11])

**Decision-event** — *Agency.* The structural moment at which operator-bundle selection (Condition 3) yields a specific action-direction. The decision-event is not identical to the readiness-potential, the moment of subjective awareness, the verbal report, or the action onset; the timing-marker non-identity chain (10.6) distinguishes these. The decision-event is inferentially located rather than directly observable. (Sections 7.10, 10.6)

**Deliberation** — *Agency.* The process of constructing, evaluating, and contrasting live options before operator-bundle selection. Deliberation can be brief or extended, explicit or implicit, and is not a precondition of free choice in every case (mastery and flow can satisfy the six conditions with minimal deliberation). The deliberation / decision / trying / action / outcome separation (7.10) is preserved throughout the architecture. (Section 7.5)

**Developmental-window** — *Attribution.* The structural period during which an agent's evaluative profile, toolkit, or option-space is being formed and is therefore not yet an appropriate locus for full attribution. The developmental-window is a profile-component in $AP_{m,t;a}$ and bears on whether responsibility-attribution applies in mature, immature, pre-agential, scaffold-captured, or trauma-shaped configurations. (Section 9.4)

**Direct willing** — *Agency.* A willing-strategy in which the agent wills the target action itself, at the moment of action, through operator-bundle selection. Direct willing is one of three principal willing-strategies (alongside configurational and slingshot). It is appropriate for low-to-moderate-resistance actions and high-mastery domains; for high-resistance actions, direct willing is often less effort-efficient than configurational or slingshot strategies. (Section 6.7)

**Discriminator value** — *Empirical.* The structural feature of a prediction that distinguishes the architecture's expected outcome from the outcomes expected under rival accounts. Each prediction in the prediction profile $PP_i$ specifies its discriminator value: what the architecture predicts that other frameworks do not, or what would be inconsistent with the architecture's commitments. Discriminator value is not the same as confirmation; predictions remain prediction-ready until empirically tested. (Section 11.3)

**Dissociation** — *Agency.* A variation-family in which structural coordination across the conditions of free choice is partially disrupted, often producing split or layered agency configurations. Dissociation is *not* the same as alienation (failure of ownership-integration), confabulation (false report), or compulsion (capture); it has its own structural profile and may co-occur with these. (Section 8.12)

**Effort** — *Agency.* The structural assessment of resistance encountered and managed during an agency event. Effort tracks resistance — the difficulty the action poses given current toolkit, configuration, and substrate state — *not* the quality of the agency exercise. High-effort agency events can be low-quality (capture under struggle); low-effort agency events can be high-quality (mastery in flow). Effort moralization — treating high effort as virtuous or low effort as suspect — is a recurring drift the architecture rejects. See also: agency-quality; effort-economy; resistance; flow. (Section 6.8)

**Effort-economy** — *Agency.* The comparative assessment of effort across willing-strategies (direct, configurational, slingshot) for a given action under given resistance. Effort-economy is a structural property of the strategy-action pairing, not a moral measure of the agent. (Section 6.9)

**Eighteen predictions** — *Empirical.* The full set of formal predictions promoted in Section 11, organized into seven families with seven backbone predictions carrying the empirical spine. The eighteen predictions are prediction-ready: each has a marker set, discriminator value, pressure conditions, and explicit exclusions, but none is empirically confirmed. The architecture's empirical traction depends on the predictions surviving pressure-condition tests across the marker sets. See also: backbone predictions; prediction profile; pressure condition. (Section 11.4)

**Empirical interpretation profile $EIP_p$** — *Empirical.* The eight-component structural object that organizes the interpretation of a given empirical paradigm $p$ in terms of which architectural objects it probes. Its eight components are $T$ task-structure, $P_o$ probed object / empirical proxy, $O_d$ order-domain, $C_x$ condition-target, $B_x$ Mode B status, $R_s$ report-structure, $M_s$ marker-signal, and $Q$ interpretive caution, written $EIP_p = \langle T, P_o, O_d, C_x, B_x, R_s, M_s, Q \rangle$. The $EIP_p$ does *not* treat any paradigm as a direct measure of agency-as-such, free will, or sourcehood. See also: empirical paradigm; timing-marker non-identity. (Sections 10.2, 10.4)

**Empirical paradigm** — *Empirical.* A specific experimental or measurement paradigm used in the empirical study of agency-related phenomena (e.g., Libet-class, Wegner-class, Soon-class, Schurger-class). Empirical paradigms probe specific architectural objects through empirical proxies; they are not direct measures of agency-as-such. See also: empirical proxy; $EIP_p$. (Section 10.3)

**Empirical proxy** — *Empirical.* The measurable signal (neural readiness-potential, motor onset, ownership report, intentional binding magnitude, etc.) that an empirical paradigm uses to probe an architectural object. Empirical proxies are not identical to the architectural objects they probe; the timing-marker non-identity chain (10.6) and the bad-inferences guardrail (10.10) discipline the inference from proxy to object. (Section 10.3)

**Evaluative engagement** — *Agency.* Condition 2 of free choice: the active evaluation of contrasted live options through the agent's evaluative apparatus (operating through $PtCns$, $PCE$-over-projection, $\Pi$-weighting, or frame-relevance, depending on configuration). Evaluative engagement can fail by absence (no evaluation occurs), capture (evaluation is dominated by drive or compulsion), or narrowing (evaluation operates over an artificially restricted space). (Section 3.2)

**First-order willing** — *Agency.* See order-indexed willing; first-order willing operates over the foundational order of focus.

**Flow** — *Agency.* A variation-family characterized by deep substrate-toolkit coupling, minimal effort, low explicit deliberation, and high agency-quality. Flow is *not* loss of agency or absence of choice; it is high-mastery configuration in which the six conditions of free choice are satisfied through mastery rather than through effortful deliberation. The flow / mastery vs capture distinction is critical: flow looks similar to automaticity-capture from the outside but has a fundamentally different structural profile (mastery preserves ownership-integration and source-status; capture does not). See also: mastery; automaticity. (Section 8.13)

**Foundation coordinates and status predicate** (Foundation v5.3.3):

- $\kappa$ — *contact* coordinate; the relation by which a content makes contact with the indexed modeling I (Foundation File 3 §7.1).
- $\phi$ — *truth-indistinguishability* coordinate, with operational gloss "source-pathway / truth-verification access" used where context is affect- or agency-specific. The three-tier φ-status structure: intrinsic items outside the φ-domain, cogito at structural 1 − δ, Tier 3 contents with constructible verification pathway have φ = 1 − nδ − ε (Foundation File 3 §7.3; File 1 §1.2, §2.3).
- $\rho$ — *identity-correlation* coordinate; the relation by which a content is integrated as an I-relative content (the architecture's central relation; Foundation File 3 §7.2).
- $A_{m,t}(x)$ — *phenomenal-availability status predicate*; $A_{m,t}(x)=1$ means content $x$ is phenomenally available to modeling I $m$ at time $t$, and $A_{m,t}(x)=0$ means it is not phenomenally available at that moment. $A$ is *not* a coordinate parallel to $\kappa$, $\phi$, and $\rho$; it is a status predicate (Foundation File 3 §6.1).

**Foundation-named architectural object (application-level formal development):**

- $\Pi$ — *preservation-ranking*; foundation-named *placeholder* (Foundation File 2 §4.8) for the situational preservation-priority ranking over possible profile-configurations and losses. The foundation explicitly defers formal development of $\Pi$ as an architectural object distinct from $\rho$ to application-level work; this paper and its companion *Free Will* develop $\Pi$ as an application-level coordinate-grade object. $\Pi$ may depend on $\rho$ but is not reducible to it: $\rho$ measures structural integration, $\Pi$ measures preservation-priority (Foundation File 4 §10.7; exclusion 19).

**Foundation prerogatives:**

- $PtCns$ — *prerogative of consistency*; the structural feature by which the I's frame functions as the implicit consistency-standard against which encounters with not-I are evaluated; unifies Mode A (differentiation when integration would damage consistency) and Mode C (integration when integration extends consistency) (Foundation File 2 §4.2, §4.5; File 4 §9.5).
- $PCE$ — *prerogative of continued existence*; the structural feature by which the modeling I structurally pulls toward the path that maximizes continued existence of the maximally-self-defined I (Foundation File 2 §4.8). Not metaphysically inviolable: defeatable, misdirectable, or routable through a distorted $\Pi$ under severe profile-shape disturbance (Foundation File 4 §10.7; exclusion 20).

**Foundation modes** (the three modes of I-development; *response-types*, not predictive mechanisms — the architecture does not predict per-encounter mode-selection, Foundation File 2 §4.1, §4.5):

- *Mode A* — *adversarial differentiation*: response-type producing the I/not-I boundary via PtCns-driven differentiation from sufficiently-distanced not-I (Foundation File 2 §4.2).
- *Mode B* — *reflexive meta-reasoning*: response-type by which the I takes its own structure as object of attention. Two sub-types: internally-triggered and externally-triggered. Requires accumulated lived-I structure (zero at developmental origin, non-zero later, variable across I's) (Foundation File 2 §4.4).
- *Mode C* — *positive identification*: response-type integrating not-I content as continuous with self. PtCns-constrained; populates inside the I/not-I boundary (Foundation File 2 §4.3, §4.5).

**Foundation-level metaphysical residue** — *Open problem.* The metaphysical questions the architecture identifies as foundation-level rather than agency-application-level: ultimate sourcehood, primal not-I dependence, lawful-frame grounding, and normative sufficiency. These residues are catalogued in [Free Will §6.2] as principled limits the architecture acknowledges as structurally outside its scope rather than deferring as eventually-solvable. See also: principled limit; ultimate sourcehood; lawful-frame grounding. ([Free Will §6.2])

**Framework translation profile $FTP_f$** — *Translation.* The seven-component structural object that organizes the architecture's engagement with a given alternative framework $f$ (Frankfurt-class hierarchical identification, reasons-responsiveness compatibilism, attributionism, hard incompatibilism, libertarianism, illusionism, predictive coding and executive control, phenomenology / existentialism / wisdom-tradition family). Its seven components are $O_f$ framework object, $T_f$ translation route, $K_f$ kept / overlapping commitments, $R_f$ reduction refused, $D_f$ discriminator, $P_f$ prediction link, and $L_f$ limits / open residue, written $FTP_f = \langle O_f, T_f, K_f, R_f, D_f, P_f, L_f \rangle$. The $FTP_f$ does *not* claim refutation, absorption, or synthesis of the framework. See also: refused reduction; translation. ([Free Will §5.1])

**Free choice proper** — *Agency.* The middle tier of the three-tier configuration: an agency event satisfying all six conditions (contrastive live-option space, evaluative engagement, operator-bundle selection, non-preemptive substrate coupling, non-confabulatory Mode B reflective availability, ownership-integration) at the order or orders relevant to the action. Free choice proper is the canonical case from which the agency taxonomy is derived by structural variation. It is *not* the same as wholehearted free choice (which adds deeper integration) or free selection (which is thinner). See also: free selection; wholehearted free choice; six conditions of free choice. (Section 3.2)

**Free selection** — *Agency.* The thinnest tier of free agency: the toolkit constructs an option-space, operator-bundle selection occurs, substrate coupling enables implementation, Mode B reflective availability remains intact, and the action is owned, while evaluative engagement is implicit, minimal, or absent. Free selection is thin free choice, *not* unfree action and *not* a defective form of free choice proper. The three tiers (free selection / free choice proper / wholehearted free choice) are *not* normatively ranked; they are structural configurations that occur in different domains, conditions, and developmental windows. See also: free choice proper; wholehearted free choice; evaluative engagement; six conditions of free choice. (Section 3.4)

**Fuzzy live option** — *Agency.* A live option whose contours are not sharply specified at the moment of contrast, but which is sufficiently distinguishable for evaluative engagement and operator-bundle selection. Fuzzy live options are common in practical decision-making and do not by themselves disqualify Condition 1; the contrastive live-option space requires distinguishability, not full specification. (Section 3.2)

**Group-agency without group-mind** — *Attribution.* The architecture's stance on collective and distributed attribution: roles, relations, and source-shaping pathways across multiple agents structure the role-indexed attribution-input profile, but the architecture does *not* posit a group-mind or collective indexed modeling I. Attribution can be distributed across agents through cascade-attribution and role-indexed inputs without reifying a group-level perspective. The architecture is perspectivally realist about other agents but does not group-mind. (Section 9.13)

**Habit** — *Agency.* A variation-family in which routinized substrate coupling implements an action through low-deliberation channels. Habit is *not* the same as compulsion: chosen-habitual action preserves prior ownership-integration and can be high-quality (Condition 6 satisfied through prior selection); compulsive-habitual action does not preserve ownership-integration and operates through capture. The chosen-habit / compulsive-habit distinction (P10) is one of the architecture's backbone predictions. See also: automaticity; compulsion; flow. (Section 8.6)

**Hard incompatibilism** — *Translation.* In this paper, the family of free-will views that hold no agent can be ultimately responsible for any action because no agent can be the ultimate source of their own evaluative profile. The architecture preserves hard-incompatibilist residue: ultimate sourcehood remains an open question ([Free Will §6.2]) the architecture does not answer, and a reader committed to ultimate-sourcehood demands may legitimately decline the architecture's compatibilist-coherent stance. The architecture does *not* refute hard incompatibilism; it operates at a level where the architectural commitments hold under both compatibilist and hard-incompatibilist substrate-metaphysical assumptions. (Sections 12.5, 13.2)

**Hierarchical identification** — *Translation.* The Frankfurt-class family of free-will views that ground freedom in the identification of the agent's first-order desires with second-order desires. The architecture translates the structural insight (ownership-integration involves higher-order endorsement) but does not collapse ownership-integration to second-order endorsement alone; the architecture's six-condition account is broader and more structurally specified. ([Free Will §5.4])

**Identity-correlation ($\rho$)** — *Foundation.* See Notation and formal objects above. The foundation coordinate by which a content is integrated as an I-relative content (Foundation File 3 §7.2). The architecture's central relation. $\rho$ measures *structural integration*, not valuation, preservation-priority, or action-priority (Foundation File 4 §11.2 exclusion 19). *Not* the same as preservation-ranking ($\Pi$): identity-correlation is the integration relation; preservation-ranking is the preservation-priority relation (foundation-named application-level architectural object; Foundation File 2 §4.8). (Foundation v5.3.3)

**Illusionism** — *Translation.* The family of free-will views that hold the experience of free will is systematically illusory, often paired with claims about the unreliability of introspective reports and the post-hoc nature of decision-recognition. The architecture preserves the illusionist insight regarding source-opacity and confabulation risk but distinguishes confabulation from post-hoc recognition (which can accurately track source-pathway given source-opacity). The architecture does not adopt the illusionist conclusion that agency is unreal; it treats agency as structural configuration whose lived character is preserved. ([Free Will §5.4])

**Indexed modeling I** — *Foundation.* The primitive anchor of the inside-perspective architecture: the I-as-modeling-itself, structurally available to itself through the cogito, and indexed to its own modeling-pathway. The agency paper applies the indexed modeling I to the agency domain without redefining or developing it; the I is the perspective from which agency is structurally analyzed. The architecture is perspectivally realist about other indexed modeling I's (other agents) but does *not* posit a group-mind. (Foundation v5.3.3; Section 2.2)

**Intentional binding** — *Empirical.* The empirical paradigm class measuring perceived temporal compression between an action and its outcome, often used to probe ownership and agency. In the architecture, intentional binding is an empirical proxy that probes specific architectural objects (ownership-recognition, source-attribution under feedback) rather than agency-as-such. (Section 10.7)

**Intrinsic layer** — *Foundation.* In Foundation v5.3.3, the layer of the indexed modeling I constituted by intrinsic structural relations. The agency paper inherits the intrinsic layer as background; for full development, see Foundation v5.3.3.

**Lawful-frame grounding** — *Open problem.* The metaphysical question of why the substrate exhibits the lawful regularity the lawful-frame qualifier requires. Lawful-frame grounding is a foundation-level metaphysical residue (13.2) the architecture does not address; the architecture takes lawful-frame regularity as a precondition for its coordinates and persistence relations to be definable, and treats the question of why such regularity holds as outside its scope. See also: lawful-frame qualifier; foundation-level metaphysical residue. ([Free Will §6.2])

**Lawful-frame qualifier** — *Foundation / Agency.* The minimum structural regularity the architecture requires of the substrate for its coordinates and persistence relations to be definable. The lawful-frame qualifier is *not* a deterministic, stochastic, or indeterministic substrate-metaphysical commitment; it specifies only that there is sufficient structural regularity for the architecture's relations to hold. The architecture is implementation-neutral within the lawful-frame qualifier. (Section 3.7)

**Libertarianism** — *Translation.* In this paper, the family of free-will views that require metaphysical openness, alternative possibilities, or agent-sourcehood stronger than the architecture's structural live-option account. The architecture translates some libertarian concerns (the architecture preserves contrastive live-option space and structural sourcehood-sensitivity) but does *not* adopt substrate-indeterminism as a condition of free choice. A reader committed to libertarian metaphysical openness as a necessary condition may legitimately decline the architecture's lawful-frame qualifier; the architecture operates at a level where its commitments hold under both libertarian and non-libertarian substrate-metaphysical assumptions. ([Free Will §5.4])

**Libet-class paradigm** — *Empirical.* The family of empirical paradigms (originating with Libet's 1983 readiness-potential studies) measuring neural preparation signals prior to subjective awareness of decision. In the architecture, Libet-class paradigms probe specific architectural objects (preparation events, selection events, ownership-recognition events) through empirical proxies; they do *not* directly measure free will, agency-as-such, or the decision-event itself. The timing-marker non-identity chain (10.6) distinguishes the empirical signals from the architectural objects. See also: $EIP_p$; readiness potential; timing-marker non-identity. (Section 10.7)

**Live option** — *Agency.* A specific option that is genuinely available within the contrastive live-option space at the moment of choice, given the agent's current toolkit, configuration, and substrate state. A merely nominal alternative (one the agent could not actually select given current constraints) is not a live option. (Section 3.2)

**Live-option space** — *Agency.* The structured set of multiple distinguishable live options available at a moment of choice. The contrastive live-option space is what Condition 1 of free choice requires; the verification-toolkit constructs the live-option space through order-indexed live-option construction. See also: contrastive live-option space; verification-toolkit. (Sections 3.2, 5.4)

**Lived-I** — *Foundation.* In Foundation v5.3.3, the indexed modeling I as it is lived from the inside, with its full set of identity-correlations, preservation-rankings, and phenomenal availabilities. The agency paper inherits the lived-I as the perspective from which agency is structurally analyzed.

**Manipulation** — *Agency / Attribution.* A variation-family in which an agent's option-space, evaluative pathway, or substrate state is upstream-shaped by another agent in a way that compromises sourcehood. Manipulation is *not* ownership-failure by default: a manipulated action can be ownership-integrated (the agent recognizes it as theirs and acts wholeheartedly within it) while sourcehood remains compromised. The manipulation-not-ownership-failure-by-default discipline (8.15, 9.5) preserves the ownership / sourcehood dissociation that is central to the architecture's attribution apparatus. See also: ownership; sourcehood; source-status; ownership / sourcehood dissociation (P5). (Sections 5.9, 8.15, 9.5)

**Marker set** — *Empirical.* The specific set of empirical signals a prediction in the prediction profile $PP_i$ requires to be jointly present (or jointly absent) for the prediction to be considered confirmed (or disconfirmed). Marker sets are typically multi-marker because single-marker measurements are not architecturally discriminating; the seven backbone predictions all use multi-marker profiles. (Section 11.3)

**Mastery** — *Agency.* The structural condition of high toolkit-development in a target-domain, characterized by deep substrate-toolkit coupling, low effort relative to action complexity, and ability to satisfy the six conditions of free choice with minimal explicit deliberation. Mastery is *not* loss of agency or absence of choice; it is high-quality agency through developed toolkit-coupling. The flow / mastery vs capture distinction is critical: mastery preserves ownership-integration and source-status; capture does not. See also: flow; toolkit-development. (Section 5.8)

**Maximally-self-defined I** — *Foundation.* In Foundation v5.3.3 (File 2 §4.8; File 4 §10.7), the action-relevant configuration of the lived-I network whose preservation counts, for the modeling I under current conditions, as continuation of itself. Not just the cogito-anchor; not the body alone; not all integrated contents; the network configuration whose preservation makes the difference between "I continued" and "I did not continue" in the action-relevant sense. Situation-relative, not a fixed developmental endpoint. PCE operates over this configuration via the preservation-ranking $\Pi_{m,t}$. The agency paper inherits the maximally-self-defined I as the relevant target of PCE-operations across the agency domain; for full derivation, see Foundation File 2 §4.8 and File 4 §10.7.

**Mitigation** — *Attribution.* A repair-mode of accountability: structural addressability for action that reduces, prevents, or compensates the cascade-effects of an action. Mitigation may obtain even in cases where original-act responsibility is reduced or unclear; mitigation-availability is a profile-component in $AP_{m,t;a}$. See also: repair; repair-accountability. (Section 9.6)

**Mode A** — *Foundation.* See Notation and formal objects above. *Adversarial differentiation*: the response-type that produces the I/not-I boundary via PtCns-driven differentiation from sufficiently-distanced not-I (Foundation File 2 §4.2). *Response-type*, not predictive mechanism: the architecture does not predict per-encounter mode-selection (Foundation §4.1, §4.5). Inherited from Foundation v5.3.3.

**Mode B** — *Foundation.* See Notation and formal objects above. *Reflexive meta-reasoning*: the response-type by which the I takes its own structure as object of attention. Two sub-types: internally-triggered (spontaneous reflexive turn) and externally-triggered (external in re instantiation prompts the reflexive turn). Requires accumulated lived-I structure (zero at developmental origin, non-zero later, variable across I's; distributional shape unspecified). Response-type, not predictive mechanism (Foundation §4.1, §4.4, §4.5). *Not* the same as exercised reflection, verbal report, introspective certainty, or source-transparency. The Mode B availability vs exercise vs report distinction is critical and is preserved across Sections 7, 10, and 11. See also: Mode B reflective availability; Mode B exercise; Mode B object-domain availability. (Foundation v5.3.3; Section 7.6)

**Mode B exercise** — *Agency.* The actual exercise of Mode B reflective object-access at a moment of agency. Mode B exercise is not the same as Mode B availability: an agent may have Mode B available without exercising it, and Mode B exercise can occur without being verbally reported. (Section 7.6)

**Mode B object-domain availability** — *Agency.* The order-asymmetric availability of Mode B reflective object-access across different agency-domains. Mode B is not uniformly available across all order-engagements: an agent may have Mode B availability for the action itself while lacking it for the source-shaping pathway, or vice versa. The order-asymmetry is preserved throughout the architecture's analysis of source-compromised agency. (Section 7.6)

**Mode B reflective availability** — *Agency.* Condition 5 of free choice: the structural availability of Mode B reflective object-access for the agency-domain relevant to the action (focusing, thinking, acting, source-shaping, or ownership-integration). Mode B reflective availability must be non-confabulatory: it must accurately track the source-pathway given source-opacity, rather than constructing post-hoc reports that do not track. *Not* the same as exercised reflection, verbal report, introspective certainty, or source-transparency. Source-opacity may coexist with Mode B availability where the agent can take the relevant agency-structure as object without having full $\phi$-access to the source-pathway. See also: Mode B; Mode B exercise; post-hoc recognition; confabulation. (Sections 3.2, 7.6)

**N-order will** — *Agency.* The general form of order-indexed willing extended through toolkit-development to constructed orders beyond the three foundational orders. N-order will preserves the structural form of willing across extended target-domains (asking, directing, team coordination, institutional engagement, and beyond). See also: order-indexed willing; constructed order. (Section 5.7)

**No-agent translation** — *Translation.* The family of contemplative and wisdom-tradition views that translate agency-talk into no-agent, dependent-origination, or non-self frameworks. The architecture translates no-agent insights at the experiential and structural-availability levels (the indexed modeling I can be experienced as transparent or absent under contemplative conditions) but does *not* erase the indexed modeling I as architectural primitive: the I remains the perspective from which no-agent translation itself is structurally available. The architecture is open to no-agent translation without erasing the I. ([Free Will §5.4])

**Normative sufficiency** — *Open problem.* The metaphysical question of whether the architecture's structural attribution-apparatus is sufficient to ground normative claims (moral desert, justified blame, justified punishment, etc.). The architecture supplies structural inputs for normative attribution but does not claim normative-sufficiency closure; normative sufficiency is treated as a foundation-level metaphysical residue (13.2) requiring engagement with normative-ethical and meta-ethical apparatus the architecture does not develop. See also: foundation-level metaphysical residue. ([Free Will §6.2])

**Not-I** — *Foundation.* In Foundation v5.3.3, contents that fall outside identity-correlation with the indexed modeling I. The agency paper inherits the not-I distinction; for full development, see Foundation v5.3.3.

**Omission / withholding / refusal** — *Agency / Attribution.* Non-action configurations that must be distinguished structurally rather than collapsed into a single "non-action" category. Withholding and refusal can be selected non-actions where non-action is live, selected, and implementable (the agent could have acted otherwise but selectively did not); drift and collapse are different configurations where selection may fail or agency may contract. Non-action is *not* automatically absence of agency: a refusal can satisfy the six conditions of free choice as fully as an action. Attribution to non-action depends on the cascade-attribution test (foreseeability, controllability, role-position, mitigation-availability) just as attribution to action does. See also: attribution-object; cascade-attribution; cascade-attribution test; decision-event. (Section 8)

**Open problem** — *Open problem.* A structural question the architecture identifies as relevant to the agency domain but not resolved within the present paper. Open problems are catalogued across the two companion papers as the seventeen-entry open-problem catalogue: foundation-level metaphysical residue ([Free Will §6.2]), theological resonance ([Free Will §6.3]), and fifteen research-program problems (this paper §12.1–§12.12 plus [Free Will §6.4–§6.6]). Open problems are *not* failures of the architecture; they are principled limits or research-program directions the architecture identifies and structures for future engagement. See also: principled limit; seventeen-entry open-problem catalogue. (this paper §12 / [Free Will §6])
**Operator-bundle selection** — *Agency.* Condition 3 of free choice: the structural selection of an action-direction by the operator-bundle (the configuration of will-operators, evaluative-operators, and execution-operators) at the moment of action. Operator-bundle selection is *not* the same as deliberation (which precedes selection) or action onset (which follows selection); the deliberation / decision / trying / action / outcome separation (7.10) is preserved. (Sections 3.2, 7.10)

**Osmotic imprinting** — *Foundation.* In Foundation v5.3.3 (File 3 §8.7), substrate-level pattern formation through repeated co-occurrence in ambient experience, always operating (mechanism-online), transverse to the four kinds of imprinting (content, contact, verification-tool, mode-development). Imprinting (formation) and activation (operation) are architecturally distinct. A primary mechanism among several for source-opaque contents and dispositions. The agency paper inherits osmotic imprinting as a source-status modifier (osmotically-shaped) within the broader source-status spectrum. See also: source-status; output-imprinting cascade. (Sections 5.6, 5.9)

**Output-imprinting cascade** — *Agency.* The structural pathway by which an agent's actions imprint on the substrate, environment, or other agents in ways that become source-shaping inputs for subsequent agency events. The output-imprinting cascade is one of the architecture's central mechanisms for understanding longitudinal agency-formation, source-compromise dynamics, and cascade-attribution. See also: source-status; cascade-attribution. (Section 5.6)

**Ownership** — *Attribution.* The structural integration of an action, decision, or output as the agent's own under Condition 6 of free choice (ownership-integration). Ownership is *not* the same as responsibility, accountability, or sourcehood. Ownership concerns the agent's structural integration of the action with their own evaluative profile and modeling I; sourcehood concerns the source-status of the option-space, evaluative pathway, or shaping pathway from which the action emerges. The ownership / sourcehood dissociation (P5) is one of the architecture's backbone predictions: a manipulated action can be ownership-integrated while sourcehood is compromised. See also: ownership-integration; sourcehood; responsibility; accountability; manipulation; ownership / sourcehood dissociation (P5). (Section 9.4)

**Ownership / sourcehood dissociation (P5)** — *Empirical / Attribution.* Backbone prediction (P5 of the prediction profile $PP_i$) stating that under well-designed manipulation paradigms, ownership-reports and source-access reports can dissociate: an agent may own an act (Condition 6 intact) while source-status is externally compromised. This prediction discriminates the architecture from frameworks that collapse ownership and sourcehood into a single dimension. The dissociation is one of the architecture's central architectural commitments and is preserved throughout the attribution apparatus and the framework-translation engagement. See also: ownership; sourcehood; manipulation; backbone predictions; $AP_{m,t;a}$. ([Free Will §4.2], 11.4)

**Ownership report** — *Empirical.* The verbal or behavioral report by which an agent expresses ownership of an action. Ownership reports are empirical proxies for ownership-recognition; they are *not* identical to ownership-integration itself, and they can dissociate from it (manipulated action may produce accurate ownership reports despite source-compromise; alienated action may produce inaccurate non-ownership reports despite preserved ownership-integration). (Section 10.7)

**Ownership-integration** — *Agency.* Condition 6 of free choice: the structural integration of the action with the agent's own evaluative profile and indexed modeling I. Ownership-integration can succeed or fail independently of source-status; manipulation cases typically preserve ownership-integration while compromising sourcehood. The ownership / sourcehood dissociation runs through Sections 8 and 9 and is central to the architecture's attribution apparatus. See also: ownership; sourcehood; six conditions of free choice. (Section 3.2)

**PCE (prerogative of continued existence)** — *Foundation.* See Notation and formal objects above. The structural feature by which the modeling I structurally pulls toward the path that maximizes continued existence of the maximally-self-defined I (Foundation File 2 §4.8). Fundamental to lived consciousness; operates always; not metaphysically inviolable: PCE's directional pull can be defeated, misdirected, or routed through a distorted preservation-ranking $\Pi$ under extreme conditions including severe profile-shape disturbance (Foundation File 4 §10.7; exclusion 20). Inherited from Foundation v5.3.3.

**Phenomenal availability ($A_{m,t}(x)$)** — *Foundation.* See Notation and formal objects above. The foundation status predicate by which a content is marked as phenomenally available or unavailable to the modeling I at a time. $A_{m,t}(x)=1$ means content $x$ is present-to-the-I; $A_{m,t}(x)=0$ means it is not presently phenomenally available. $A$ is a status predicate, *not* a coordinate parallel to $\kappa$, $\phi$, and $\rho$ (Foundation File 3 §6.1). Distinct also from the foundation-named preservation-ranking $\Pi$ (an architectural object whose application-level formalization is given by this paper and its companion *Free Will*; see Foundation File 2 §4.8 for the foundation's deferral). Inherited from Foundation v5.3.3.

**Phenomenology / Existentialism** — *Translation.* Families of frameworks engaged in [Free Will §5] that analyse agency from the first-person perspective and preserve the structural reality of lived experience: phenomenology (intentionality, embodiment, temporality, first-person seriousness); existentialism (choice, self-making, anxiety, authenticity, situated existence). The architecture translates their insights into inside-perspective structural profiles, formal profile-objects, and falsifiable predictions while refusing reduction to descriptive-only phenomenology or unconstrained radical-freedom existentialism. Architectural overlap is most visible in the inside-perspective discipline, the indexed modeling I, and the developmental-window / profile-formation apparatus. See also: framework translation profile; no-agent translation; ultimate sourcehood. ([Free Will §5])

**Post-hoc recognition** — *Agency.* The structural recognition by an agent of an action's source-pathway after the action has occurred, given source-opacity at the moment of action. Post-hoc recognition is *not* the same as confabulation (which constructs reports that do not track source-pathway) or source-transparency (which has access at the moment of action). The post-hoc recognition / source-opacity / confabulation triad (7.9) preserves these distinctions structurally. See also: confabulation; Mode B reflective availability. (Section 7.9)

**Prediction profile $PP_i$** — *Empirical.* The seven-component structural object that organizes a prediction $i$. Its seven components are $S$ structural source, $T$ target architectural object, $M$ marker set, $D$ domain, $C$ comparator, $F$ failure / pressure condition, and $E$ exclusions, written $PP_i = \langle S, T, M, D, C, F, E \rangle$. The eighteen predictions of Section 11 are organized through $PP_i$. The $PP_i$ does *not* claim empirical confirmation; predictions remain prediction-ready until tested. See also: backbone predictions; eighteen predictions; pressure condition. (Sections 11.2, 11.3)

**Prediction-ready** — *Empirical.* The status of a prediction that has a marker set, discriminator value, pressure conditions, and falsification criteria specified, but has not yet been operationalized into a specific empirical paradigm or empirically tested. The eighteen predictions of Section 11 are prediction-ready; the architecture's empirical promotion is a promotion-to-prediction-ready, not a claim of confirmation. (Section 11.2)

**Predictive coding** — *Translation.* In this paper, the family of computational and neuroscientific frameworks (active inference, hierarchical predictive coding, generative modeling) that explain perception, action, and cognition through prediction-error minimization across hierarchical generative models. The architecture treats predictive coding as an open implementation candidate (substrate-level mechanism that may instantiate the architecture's coordinates and persistence relations) rather than a reduction; the architecture's commitments are implementation-neutral within the lawful-frame qualifier. ([Free Will §5.4])

**Preparation vs selection** — *Empirical.* The architectural distinction between preparation events (substrate-level priming, readiness-potential generation, option-construction) and selection events (operator-bundle selection, decision-event). The Libet-class readiness-potential is a preparation signal, not a selection signal; the timing-marker non-identity chain (10.6) preserves this distinction throughout the empirical-interface analysis. (Sections 7.10, 10.6)

**Preservation-ranking ($\Pi$)** — *Foundation-named, application-level.* See Notation and formal objects above. Foundation-named *placeholder* (Foundation File 2 §4.8) for the situational preservation-priority ranking over possible profile-configurations and losses. The foundation explicitly defers formal development of $\Pi$ as an architectural object distinct from $\rho$ to application-level work; this paper and its companion *Free Will* develop $\Pi$ as an application-level coordinate-grade object. *Not* the same as identity-correlation ($\rho$): preservation-ranking is the preservation-priority relation; identity-correlation is the structural-integration relation (Foundation File 4 §10.7; exclusion 19).

**Pressure condition** — *Empirical.* The structural condition under which a prediction in the prediction profile $PP_i$ is most likely to be tested under conditions that discriminate the architecture's expected outcome from rival outcomes. Pressure conditions are not the same as ordinary experimental conditions; they specify the configurations under which the prediction has discriminator value. Pressure-condition language preserves epistemic humility: predictions remain prediction-ready, not confirmed. (Section 11.3)

**Primal not-I** — *Foundation.* In Foundation v5.3.3, the foundational not-I from which the indexed modeling I emerges through identity-correlation operations. The agency paper does not develop the primal not-I; it appears in the agency paper only as a foundation-level metaphysical residue (13.2) and is *not* identified with God, the universe, the substrate, or any external referent. See also: foundation-level metaphysical residue.

**Primal not-I dependence** — *Open problem.* The metaphysical question of whether and how the indexed modeling I depends on the primal not-I. Primal not-I dependence is a foundation-level metaphysical residue (13.2) the architecture does not address; the architecture takes the indexed modeling I as primitive and treats the question of its dependence on the primal not-I as outside its scope. ([Free Will §6.2])

**Principled limit** — *Open problem.* A structural commitment the architecture identifies as outside its scope on principled grounds rather than as a problem to be eventually solved. Principled limits include foundation-level metaphysical residue (13.2), theological resonance under translation-not-derivation discipline (13.3), normative sufficiency, and several research-program problems whose resolution would require apparatus the architecture does not develop. The principled-limit framing is *not* defeatism; it preserves epistemic humility against overclaim. (Sections 13.2, 13.20)

**Profile-indexed attribution** — *Attribution.* The architecture's stance on attribution: attribution is computed from a structural profile $AP_{m,t;a}$ rather than delivered as a binary verdict, and the profile surfaces what is true about a particular configuration rather than collapsing the configuration to free / unfree, responsible / not-responsible, blameworthy / not-blameworthy. Profile-indexed attribution rejects responsibility-as-conserved-quantity (responsibility is not transferred wholesale between agents) and zero-sum responsibility error. See also: $AP_{m,t;a}$; zero-sum responsibility error. (Sections 9.4, 9.12)

**PtCns (prerogative of consistency)** — *Foundation.* See Notation and formal objects above. The structural feature by which the I's frame functions as the implicit consistency-standard against which encounters with not-I are evaluated (Foundation File 2 §4.2, §4.5; File 4 §9.5). Unifies Mode A (differentiation when integration would damage consistency) and Mode C (integration when integration extends consistency). Operates whenever the I encounters anything against its frame — discrepant objects, contradicting facts, violated expectations, other I's whose frames conflict with one's own, or contents that register as consistency-extending. The inter-I case (two PtCns structures simultaneously) is one manifestation among many, not the home of the concept. Renamed in v5.2.1 from "prerogative-to-be-right" to align name with structural function. Inherited from Foundation v5.3.3.

**Readiness potential** — *Empirical.* The neural preparation signal first measured by Libet (1983) preceding subjective awareness of decision. In the architecture, the readiness potential is an empirical proxy for substrate-level preparation events, not a measure of decision-event onset, free will, or agency-as-such. See also: Libet-class paradigm; preparation vs selection; timing-marker non-identity. (Section 10.7)

**Reasons-responsiveness** — *Translation.* The compatibilist family of free-will views that ground freedom in the agent's responsiveness to reasons. The architecture translates reasons-responsiveness as part of the broader compatibilist-coherent stance: the architecture's evaluative engagement (Condition 2) and Mode B reflective availability (Condition 5) overlap substantially with reasons-responsiveness conditions, but the architecture's six-condition account is broader and more structurally specified. ([Free Will §5.4])

**Recognition-lag** — *Empirical.* The structural lag between an action and the agent's reflective recognition of having selected the action, given source-opacity. Recognition-lag is *not* the same as confabulation (which would involve inaccurate post-hoc construction); it is the time-extension of post-hoc recognition. The Libet-class subjective-awareness data measure recognition-lag indirectly. (Sections 7.9, 10.7)

**Refused reduction** — *Translation.* The architecture's stance toward translation: an alternative framework can be translated by the architecture without being reduced to it. Refused reduction is the central discipline of the framework translation profile $FTP_f$: each framework is engaged at the level of its central insight without claim of refutation, absorption, or synthesis. The architecture preserves what it can translate from each framework; what it cannot translate is acknowledged as residual incommensurability. See also: translation; $FTP_f$. ([Free Will §5.3])

**Repair** — *Attribution.* A repair-mode of accountability: structural addressability for action that restores or compensates for cascade-effects. Repair may obtain even where original-act responsibility is reduced or unclear; repair-availability is a profile-component in $AP_{m,t;a}$. See also: mitigation; repair-accountability. (Section 9.6)

**Repair-accountability** — *Attribution.* The form of accountability that addresses repair, mitigation, or restoration of cascade-effects rather than blame, punishment, or moral verdict for the original act. Repair-accountability can obtain even when ownership is intact but sourcehood is compromised, when responsibility is partial, or when the original-act attribution is unclear. The architecture treats repair-accountability as a distinct attribution-mode rather than collapsing accountability to blame. (Section 9.6)

**Resistance** — *Agency.* The structural difficulty an action poses given current toolkit, configuration, and substrate state. Resistance is what effort tracks; high resistance can be managed through high-effort direct willing, configurational preparation, or slingshot strategies, depending on the action and the agent's profile. Resistance is *not* a measure of agency-quality. See also: effort; effort-economy. (Section 6.8)

**Responsibility** — *Attribution.* The structural attribution of an action or cascade to an agent for evaluative purposes. Responsibility is *not* identical to ownership (which concerns structural integration), accountability (which concerns addressability for response), or blame (which adds a normative-evaluative judgment the architecture does not deliver). Responsibility is computed from the attribution profile $AP_{m,t;a}$ as profile-indexed rather than binary, and is *not* a conserved quantity transferred wholesale between agents. See also: ownership; accountability; profile-indexed attribution; zero-sum responsibility error. (Sections 9.4, 9.12)

**Role-indexed attribution-input** — *Attribution.* A profile-component in $AP_{m,t;a}$ that captures how an agent's role-position in a system structures the attribution-inputs for an action or cascade. Role-indexed attribution-inputs allow distributed and collective attribution without group-mind reification; they are how the architecture handles institutional, organizational, and collaborative attribution-cases. See also: group-agency without group-mind. (Sections 9.13, 9.14)

**Second-order willing** — *Agency.* See order-indexed willing; second-order willing operates over the foundational order of thought.

**Section-level structural objects** (introduced in this paper):

- $AP_{m,t;a}$ — *attribution profile* indexed to agent / modeling I $t$, moment $m$, and act / action or cascade $a$ (Section 9).
- $EIP_p$ — *empirical interpretation profile* for a paradigm $p$ (Section 10).
- $PP_i$ — *prediction profile* for a prediction $i$ (Section 11).
- $FTP_f$ — *framework translation profile* for a framework $f$ ([Free Will §5]).

The four section-level objects perform distinct analytical tasks and are not interchangeable; the architecture's analytical leverage depends on keeping them distinct.

## Alphabetical glossary

**Seventeen-entry open-problem catalogue** — *Open problem.* The structured catalogue of open problems split across the two companion papers: foundation-level metaphysical residue ([Free Will §6.2]), theological resonance under translation-not-derivation discipline ([Free Will §6.3]), and fifteen research-program problems (this paper §12.1–§12.12 plus [Free Will §6.4–§6.6]), with priority map (§12.13) and handoff (§12.14). The seventeen-entry framing distinguishes the catalogue's three layers (foundation-level, theological, research-program) and preserves catalogue-hygiene against count-conflation. See also: open problem; principled limit. (this paper §12 / [Free Will §6])
**Six conditions of free choice** — *Agency.* The six interdependent structural conditions that define free choice proper: (1) contrastive live-option construction by the verification-toolkit; (2) evaluative engagement; (3) operator-bundle selection; (4) non-preemptive substrate coupling; (5) non-confabulatory Mode B reflective availability; (6) ownership-integration. The conditions are interdependent: failure of any one constitutes a structural variation in the agency-configuration (see Section 8 for the seventeen variation-families). The conditions hold across order-indexed willing domains. (Section 3.2)

**Slingshot willing** — *Agency.* A willing-strategy in which the agent uses a sequence of intermediate actions to launch a target action, often by configuring substrate or toolkit through preparatory steps that release the target action with low marginal effort. Slingshot willing is one of three principal willing-strategies (alongside direct and configurational); it is appropriate for high-resistance actions where direct willing is effort-inefficient and configurational willing requires more time than slingshot allows. (Section 6.7)

**Soon-class paradigm** — *Empirical.* The family of empirical paradigms (originating with Soon et al. 2008) decoding decision-content from neural activity prior to subjective awareness of decision. In the architecture, Soon-class paradigms probe specific architectural objects (preparation events, decision-content priming) through neural-decoding empirical proxies; they do *not* directly measure free will, agency-as-such, or the decision-event in the architectural sense. See also: $EIP_p$; preparation vs selection; timing-marker non-identity. (Section 10.7)

**Source-pathway access ($\phi$)** — *Foundation.* See Notation and formal objects above. The foundation coordinate by which the I has access to the source-status and verification-pathway of a content. *Not* the same as Mode B reflective object-access: $\phi$ concerns source-pathway access; Mode B concerns reflective object-access. The two are dissociable. (Foundation v5.3.3)

**Source-status** — *Agency / Attribution.* The structural status of the option-space, evaluative pathway, or shaping pathway from which an agency event emerges. The architecture distinguishes source-statuses including source-clean (no upstream shaping by another agent), scaffolded (shaped within developmentally-appropriate guidance), osmotically shaped (gradually integrated through low-level contact), source-compromised (upstream-shaped in ways that compromise sourcehood), source-poisoned (upstream-shaped to defeat the agent's own evaluative profile), coerced (shaped by force or threat), and manipulated (shaped without the agent's awareness or consent). Source-status is a profile-component in $AP_{m,t;a}$ and is dissociable from ownership-integration. See also: sourcehood; manipulation; ownership / sourcehood dissociation. (Sections 5.9, 9.4)

**Sourcehood** — *Attribution.* The structural assessment of the source-status of the option-space, evaluative pathway, or shaping pathway from which an action emerges. Sourcehood is *not* the same as ownership: ownership concerns the agent's structural integration of the action with their own evaluative profile and indexed modeling I; sourcehood concerns where the option-space, evaluation, or shaping came from. The ownership / sourcehood dissociation runs through Sections 8 and 9 and is one of the architecture's backbone predictions (P5: ownership / sourcehood dissociation under manipulation conditions). See also: ownership; source-status; manipulation; ultimate sourcehood. (Sections 9.4, 9.5)

**Substrate** — *Foundation.* In Foundation v5.3.3, the physical, biological, or implementation-level system on which the indexed modeling I and its operations run. The agency paper inherits substrate as a background commitment and is implementation-neutral on substrate-metaphysics within the lawful-frame qualifier. See also: lawful-frame qualifier; substrate coupling.

**Substrate coupling** — *Agency.* Condition 4 of free choice: the structural coupling of the operator-bundle selection to substrate-level implementation, in a way that does not preempt the selection (substrate-level pre-determination of action without operator-bundle selection), bypass it (substrate-level action without operator-bundle engagement), or capture it (substrate-level domination of the operator-bundle by drive, urge, or compulsion). Substrate coupling can fail through preemption, bypass, or capture; the failure modes correspond to different variation-families (compulsion, automaticity, dissociation, etc.). (Sections 3.2, 6.4)

**Theological resonance** — *Open problem.* The structural availability of the architecture for translation into theological motifs (grace-like repair, repentance-like reconfiguration, providence-like lawfulness, sourcehood-residue and ultimate-sourcehood concerns, etc.) without the architecture deriving, proving, identifying, or grounding theological claims. Theological resonance preserves the translation-not-derivation discipline: the architecture permits translation but does not license theological identification, primal-not-I-as-God identification, grace-as-architectural-primitive claims, or theological proof. Theological resonance is one of the seventeen-entry open-problem catalogue entries (13.3) and is treated as a principled limit. See also: theological identification; theological translation; principled limit. ([Free Will §6.3])

**Third-order willing** — *Agency.* See order-indexed willing; third-order willing operates over the foundational order of substrate-mediated action.

**Timing-marker non-identity** — *Empirical.* The structural distinction between empirical timing-markers (readiness-potential onset, motor-cortex activation, action onset, subjective awareness of decision, ownership report, etc.) and the architectural objects they probe (preparation events, selection events, decision-events, ownership-recognition events). Timing-marker non-identity is the architecture's central discipline against the empirical-proxy / architectural-object collapse: an empirical paradigm measuring readiness-potential is not measuring decision-event timing, free will, or agency-as-such. See also: empirical proxy; $EIP_p$. (Section 10.6)

**Toolkit-development** — *Agency.* The structural process by which the verification-toolkit develops new operations, new order-engagements, and new mastery in target-domains over time. Toolkit-development is the mechanism by which constructed orders become available beyond the three foundational orders, and is the source of the order-asymmetry in agency configurations. See also: verification-toolkit; mastery; constructed order. (Sections 5.5, 5.8)

**Trained expectation** — *Agency.* A condition in which the verification-toolkit's live-option construction is shaped by prior training such that certain options appear as default candidates and others appear as non-candidates, even when both are structurally live. Trained expectation can compromise Condition 1 (contrastive live-option space) when training has narrowed the option-space to artificial defaults, but trained expectation is also how mastery and skilled flow operate (high-quality narrowing). The mastery vs capture distinction applies. (Sections 5.4, 8.6)

**Translation** — *Translation.* The architecture's mode of engagement with alternative frameworks: structural mapping that preserves the framework's central insight where it can be translated into the architecture's vocabulary, identifies what the architecture can and cannot translate, and acknowledges residual incommensurabilities. Translation is *not* refutation, absorption, or synthesis. The framework translation profile $FTP_f$ organizes translation systematically. See also: refused reduction; $FTP_f$. ([Free Will §5.3])

**Trying** — *Agency.* The structural attempt to execute an action through operator-bundle selection and substrate coupling. Trying is *not* identical to outcome-success: an agent can try and fail (substrate resistance dominates), try with low effort and succeed (mastery), or try with high effort and partially succeed (effortful action). The deliberation / decision / trying / action / outcome separation (7.10) preserves these distinctions. (Section 7.10)

**Two-Layer Identity-Correlation Architecture** — *Foundation.* The book-projection foundational architecture established in Foundation v5.3.3, comprising the inside-perspective discipline anchored in the indexed modeling I, the identity-correlation $\rho$ as central relation, the verification-toolkit, the foundation's three coordinates ($\kappa$, $\phi$, $\rho$) together with the foundation-named preservation-ranking $\Pi$ (placeholder for application-level formalization; Foundation File 2 §4.8), the phenomenal-availability status predicate $A_{m,t}(x)$, the prerogatives ($PtCns$, $PCE$), the modes of I-development (A, B, C), and the layer-structure (intrinsic layer / asymptotic layer, the latter being the content domain $\mathsf{A}^m_t$). The agency paper is the third application paper (Layer 8) in the projected book series, building on Foundation v5.3.3, *Temporal Phenomenology*, and *Differentiated Affect*; the application-level promotion of $\Pi$ to coordinate-grade formal use is explicitly licensed by Foundation File 2 §4.8 and does not introduce new foundation-level primitives. (Section 2.2)

**Ultimate sourcehood** — *Open problem.* The metaphysical question of whether and how an agent can be the ultimate source of their own evaluative profile, free of dependence on prior causes the agent did not originate. Ultimate sourcehood is a foundation-level metaphysical residue (13.2) the architecture does not address; the architecture's compatibilist-coherent stance is consistent with ultimate sourcehood being either preserved or unattainable. A reader committed to ultimate-sourcehood demands as a precondition of free will may legitimately decline the architecture's free-choice-proper account; the architecture operates at a level where its commitments hold under both ultimate-sourcehood-preserving and ultimate-sourcehood-denying assumptions. See also: hard incompatibilism; foundation-level metaphysical residue. (Sections 13.2, 12.5)

**Verification-toolkit** — *Foundation / Agency.* The application-level coordinated set of $\phi$-bearing operations through which the indexed modeling I constructs, evaluates, and inhabits live options at each order of willing. The verification-toolkit is inherited from Foundation v5.3.3 and specialized for the agency domain in Section 5: it is the mechanism of contrastive live-option construction, evaluative engagement, and Mode B reflective availability. Toolkit-development extends the verification-toolkit through mastery and constructed orders. See also: live-option space; toolkit-development; six conditions of free choice. (Section 5.1)

**Wegner-class paradigm** — *Empirical.* The family of empirical paradigms (originating with Wegner's apparent-mental-causation framework) measuring the construction of perceived authorship over actions. In the architecture, Wegner-class paradigms probe specific architectural objects (ownership-recognition, source-attribution under feedback, the post-hoc recognition / source-opacity / confabulation distinctions) through perception-of-authorship empirical proxies; they do *not* directly measure free will or refute agency. The architecture preserves the Wegner-class insight regarding source-opacity and confabulation risk while distinguishing confabulation from accurate post-hoc recognition. See also: $EIP_p$; confabulation; post-hoc recognition. (Section 10.7)

**Wholehearted free choice** — *Agency.* The deepest tier of the three-tier configuration: an agency event satisfying all six conditions of free choice with deeper integration across the agent's evaluative profile, indexed modeling I, and order-engagements. Wholehearted free choice is *not* the same as free choice proper (which satisfies all six conditions but at less deep integration) or automatic responsibility-attribution; an agent acting wholeheartedly can still be source-compromised (the manipulation case in 2.1 demonstrates this), and ownership-integration in wholehearted free choice does not entail full responsibility-attribution. The three tiers (free selection / free choice proper / wholehearted free choice) are *not* normatively ranked; they are structural configurations that occur in different domains, conditions, and developmental windows. See also: free choice proper; free selection. (Section 3.4)

**Willing-strategies** — *Agency.* The umbrella term for the principal strategies through which agents implement actions: direct willing (will the action itself), configurational willing (configure substrate to support the action), and slingshot willing (use intermediate actions to launch the target action). Additional willing-strategies (receptive, distributed, counter-cyclical) operate in specific configurations. Willing-strategies are not normatively ranked: each strategy is appropriate for different effort-economies, resistance levels, and toolkit-configurations. See also: direct willing; configurational willing; slingshot willing; effort-economy. (Section 6.7)

**Zero-sum responsibility error** — *Attribution.* The structural error of treating responsibility as a conserved quantity such that responsibility attributed to one agent must be subtracted from another. The architecture explicitly rejects zero-sum responsibility error: profile-indexed attribution allows responsibility to be partial, distributed, or absent without redistribution constraint, and manipulation cases can leave both the manipulator and the manipulated agent with their own profile-indexed attributions without zero-sum trade-off. See also: profile-indexed attribution; responsibility. ([Free Will §4.3])
