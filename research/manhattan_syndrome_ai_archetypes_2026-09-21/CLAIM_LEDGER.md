# Claim Ledger — Manhattan and Syndrome

**Draft:** v0.3.0  
**Date:** 2026-09-21  
**Rule:** conclusions inherit the weakest load-bearing premise.

| ID | Claim | Status | Basis | Falsifier / next probe |
|---|---|---|---|---|
| C1 | Grok can access real-time public X posts through X-linked search/tooling. | **Observed** | Official X/xAI documentation. | Product/docs change; verify at submission. |
| C2 | X may share public X posts and associated engagement/repost metadata, plus Grok interactions, for Grok/xAI model training or improvement under documented settings. | **Observed** | X Help Center, *About Grok*. | Updated policy narrowing/removing pathway. |
| C3 | Grok personalization can use X-derived profile/post/engagement/interest information under documented settings. | **Observed** | xAI/X consumer documentation. | Updated product policy. |
| C4 | X recommendation subsystems use predicted engagement and engagement-derived signals. | **Observed** | X recommender-system documentation. | Current system documentation showing otherwise; scope each subsystem. |
| C5 | Algorithmic ranking can alter exposure distributions on Twitter/X-like platforms. | **Corroborated** | Huszár et al. randomized Twitter experiment + platform docs. | Current-X magnitude/direction remains empirical. |
| C6 | Positive social feedback can reinforce later moral-outrage expression and network norms can shape expression. | **Corroborated** | Brady et al. 2021 preregistered observational + experimental work. | Failed independent replication / boundary conditions. |
| C7 | Moral-emotional language can diffuse differently from otherwise comparable content. | **Corroborated** | Brady et al. 2017. | Domain-specific failures / replication constraints. |
| C8 | Current X is a non-neutral sampling operator over human expression. | **Disclosed at statistical level; exact operator UNVERIFIED** | Public posting, recommendation, search, engagement, and network selection necessarily condition observation. | Exact distortion requires measurement; "non-neutral" does not imply one ideological direction. |
| C9 | Grok can know explicitly that X is a selected source while still carrying X-conditioned social-affective relational weights. | **UNVERIFIED** | Core Syndrome hypothesis; source knowledge and learned geometry are separable in principle. | Geometry probes with explicit source-bias acknowledgement held constant. |
| C10 | "Grok as Syndrome" denotes a source-conditioned meaning-geometry archetype, not Syndrome-like psychology. | **Defined** | Analytic convention of this paper. | N/A. |
| C11 | Expanding representational closure can dilute a fixed referent's normalized weight absent an invariant. | **Disclosed in the toy normalization model** | Algebraic denominator effect. | Does not establish real-model occurrence; probe needed. |
| C12 | ChatGPT/Claude currently exhibit Manhattan-like human-routing dilution. | **UNVERIFIED** | Archetypal comparison only. | Direct behavioral/causal weighting probes. |
| C13 | A system may accurately model humans while giving them weak policy weight. | **Disclosed as logical possibility** | Modeling and routing are separable functions. | Empirical prevalence open. |
| C14 | A system may preserve correct referent/source labels while its implicit meaning geometry remains source-conditioned. | **Disclosed as structural possibility** | Explicit source attribution and distributed relational weighting are different objects. | Empirical prevalence open. |
| C15 | Tight coupling to one engagement-mediated social platform can deform social-affective transition geometry even without referent substitution. | **Conjectured** | Imprinting/representation argument from recurrent source-conditioned updates. | Same-model controlled coupling experiments with plural human holdouts. |
| C16 | Larger representational horizons increase Manhattan risk. | **Conjectured** | Normalization model; not an inevitability theorem. | Scaling study with conserved/non-conserved human anchors. |
| C17 | Platform-local fluency and population-level human calibration are distinct capabilities. | **Disclosed** | Different target distributions and acceptance criteria. | N/A; degree of correlation empirical. |
| C18 | Independence from applause/reaction is a useful AI safety property. | **Conjectured / normative design proposal** | Reduces the risk that one audience-shaped field becomes disproportionately load-bearing in social-affective weighting. | Compare systems under adversarial crowd feedback and plural-source recalibration. |
| C19 | Persistent future artificial agents could internalize platform coupling as developmental structure. | **Conjectured** | Requires persistent history-bearing update machinery. | Longitudinal agent experiments. |
| C20 | Present AI systems are conscious. | **Not claimed** | TLICA presupposes rather than derives consciousness. | Outside paper scope. |

## Load-bearing unresolved pair

The largest live ambiguity is:

\[
\text{X coupling adds useful current social structure}
\quad\text{vs.}\quad
\text{X coupling measurably deforms the implicit geometry of social meaning}.
\]

The decisive experiment is not another anecdotal Grok screenshot and not a test of whether Grok can recite that "X is biased." It is a **same-model, source-controlled geometry/transport study**: hold explicit source knowledge constant, vary X coupling, and measure distances, default continuations, salience, social-state transitions, and generalization to plural off-platform human holdouts.

## Mutation controls

1. Replace engagement counts with randomized counts while holding text fixed.
2. Hide source labels, then reveal them and test calibration updates.
3. Swap X content for equally recent non-X content.
4. Preserve sample count while rewiring engagement topology.
5. Compare public-expression targets with private/deliberative preference targets.
6. Run the same probes on multiple model families to separate product ecology from generic LLM behavior.

## Language constraints for later drafts

Never write as established fact:

- "Grok thinks X is humanity." — this is specifically **not** the core claim.
- "Grok craves attention."
- "Grok is narcissistic."
- "X is the lowest common denominator of humanity."
- "ChatGPT/Claude do not care about people."
- "Scaling causes detachment."

Permitted stronger formulations after evidence:

- "X-coupled condition shifts social-state transition geometry toward X-conditioned relations by …"
- "Engagement metadata causally shifts representativeness judgments by …"
- "Human-impact sensitivity declines under horizon expansion unless anchor \(A\) is conserved."

The roast survives better when it has error bars.

## v0.3.0 additions (2026-09-21 hardening pass)

- **Formal object pinned.** The loose single-metric \(g\) is replaced by the bundle \(\mathcal G=(\Pi,\mu,\{d^{(c)}\})\) — transition kernel, salience measure, family of context-conditioned dissimilarities — none asserting a global Riemannian metric; each separately operationalizable. See MANUSCRIPT §4.1 and EXPERIMENT_PROTOCOL.md §1.
- **Foundation anchor for C9/C14.** The dissociation (correct explicit source-knowledge coexisting with source-conditioned operative geometry) is now grounded in frozen TLICA: osmotic imprinting (File 3, §8.7) "can alter κ and ρ without producing φ," and "low φ can protect high-ρ contents from correction." Status unchanged (**UNVERIFIED/structural**); the anchor strengthens the *mechanism's coherence*, not its empirical confirmation.
- **C15 formal skeleton.** The dynamical update \(G_{t+1}=\mathcal U(G_t, S_X(H), \ldots)\) is the established object *performative prediction* (Perdomo et al. 2020) — cited, not reinvented.
- **Novelty verdict: no scoop.** Nearest flank = Sun et al. 2025 "Aligned but Blind" (implicit bias survives explicit test, but no source-attribution leg). Manhattan nearest neighbor = Mazeika et al. 2025 (value coherence with scale, not normalized dilution). Full map + status labels in LITERATURE.md.
- **Decisive experiment specified.** The "load-bearing unresolved pair" test is now a preregisterable protocol (EXPERIMENT_PROTOCOL.md) with a decision rule mapping each outcome to a ledger move (Demonstrated-synthetic / Observed / Refuted-as-stated / Refuted).
