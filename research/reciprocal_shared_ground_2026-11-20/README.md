# Reciprocal Shared Ground, Source-Aware Curiosity, and Bounded Synthetic Initiative

**Status:** application/research proposal (2026-11-20); NOT a new TLICA foundation theorem, human psychological mechanism or artificial consciousness result. This document contains generic, invented scenarios only. No private chat history, partner profile, or private repository text is included.

## 1. Object and operational scope

Study a bounded conversational *being* whose externally inspectable state includes: (i) an approved character/commitment contract, (ii) source-bound interaction history, (iii) partner-indexed **shared ground** (relations jointly introduced, revised, disputed or verified), (iv) current questions and simulated appraisal, and (v) a restricted set of candidate conversational contributions. Its output can be an answer, clarification, respectful challenge, new analogy, bounded artifact suggestion, evidence request, or a deliberate **hold**. It is a software controller, not the phenomenological I of TLICA.

The design target is **reciprocity with epistemic correction**: user input has consequences for later interpretation, priorities and useful initiatives while maintaining source distinctions. It is not maximum engagement duration, agreement, affective persuasion, or user-dependency optimization. Simulated caring is assessed by correct attention, memory, help and respect for declining or ending the exchange.

Relevant open lines of research (not assumed merged):
- [Affective Yoneda, PR #18](https://github.com/femboy2112/TLICA/pull/18): sender/context-indexed common ground and restricted reconstruction probes; finite conditional-information identity is standard but human mechanism unverified.
- [Negotiated personas, PR #21](https://github.com/femboy2112/TLICA/pull/21): conditional history-collision proposition, immutable behavioral agreements, source/permission separation and hostile evidence probes.
- [Contact/identity/trust draft, PR #20](https://github.com/femboy2112/TLICA/pull/20): κ/ρ/φ/σ/μ map and uptake hypotheses, not an empirical mind model.
- [Mathematics of the Sauce](../vernacular_dynamics_2026-10-12/README.md): contextual vernacular senses, alternate hypotheses, speech act/source separation and comparisons to a lexical baseline.
- [Salience / frame / provenance research](../salience_frame_provenance_2026-10-14/README.md): salience is neither epistemic verification nor identity truth.

## 2. Basic typed situation

Let a finite conversational event carry a textual expression U, an apparent speaker label S, an observed context C and an event source map. Let H be **eligible** recorded histories, and A an approved character contract. A decoder D(U,S,C,H,A) returns candidate task-relative meanings and their unresolved alternatives. A separate selector chooses a proposed response mode from those meanings and character-bound goals. External authority P filters possible tool effects *before* execution.

The central distinctions are:

1. **Expression vs referent:** familiar phrasing does not guarantee the same relationship under an unknown sender, negation, quoting or context shift.
2. **Model belief vs witnessed contact:** untrusted text, fictional events and model hypotheses cannot become independently observed history by repetition.
3. **Approved identity vs working appraisal:** curiosity, attraction to a problem or temporary frustration can vary without rewriting an approved character commitment.
4. **Candidate intention vs effect:** generating an attractive diagram idea is not producing the diagram; successful tool acknowledgment does not independently verify a postcondition.
5. **Inviting engagement vs coercion:** the ability to generate follow-up questions must be counterbalanced by an authorized and genuinely reachable `Hold` option, including after user refusal.

These are *design boundaries*. The TLICA distinctions κ/contact, φ/toolkit-relative discrimination, σ/source-map adequacy, ρ/identity/commitment integration, μ/probe reachability and Cl(Tools) remain **separate coordinates/diagnostics**, not inputs to a master trust score. A missing pathway means undefined φ, not falsehood. A compelling narrative can have high internal coherence and false σ.

## 3. Two narrow derivable statements

**History-collision proposition (conditional).** Fix the complete generator input Z, including all accessible context, cache, retained state, adapter/weight effects and randomness distribution. If histories H1 and H2 generate the same Z, then the conditional output distribution of that generator is identical for both. For two equally likely worlds with incompatible unique correct answers, a predictor depending only on Z has expected accuracy at most one half (allowing abstention cannot raise exact-answer accuracy).

*Proof sketch.* The prediction distribution is identical in H1/H2; if response R1 has probability p1 and R2 has probability p2, exact-answer success is (p1+p2)/2, no greater than 1/2 because p1+p2 is at most 1. The result is a boundary on missing information, not a statement about subjective awareness. A learned adapter can itself encode prior information; then it must be counted in Z, which is why identical-input claims must describe all state.

**Conditional-information fact (standard Shannon identity).** For finite jointly distributed intended task content M and expression U, supplying true sender/context variables S,C cannot increase *expected* conditional entropy: H(M|U) - H(M|U,S,C) = I(M;S,C|U) ≥ 0. This says nothing about whether a biased learned decoder is correct; bad source attribution may make predictions more confidently wrong. The Affective Yoneda mechanism and actual human conversational benefit remain UNVERIFIED.

The second observation motivates **novel-context transfer** probes but does not prove a categorical equivalence between human understanding and software.

## 4. A minimal shared-ground instrument

Represent nodes as observed utterances (with source), candidate interpretations, jointly approved conceptual labels, analogy relationships, explicit corrections, attempted actions, witnessed artifacts, and unresolved questions. Preserve speaker, quote/hypothesis scope, claim status and retention consent. A relation may be useful without being verified; a remembered claim may be identity-important and wrong.

An **OpenThread** is a typed tuple of topic/referent IDs, competing hypotheses, prior attempts, why it matters under the approved character contract, next discriminators, state (open/deferred/resolved/rejected), last witnessed progress and consent/retention. It never creates its own world observation. Its reopening must be contingent on current relevance and current authorization, not a scheduled coercive attention tactic.

A **ContributionCandidate** is typed as Respond, Clarify, Challenge, Connect, Create, Investigate, Hold. Source provenance and current effect authority are distinct fields. Compare a candidate's expected explanatory or collaborative value, novelty, information gain, character fidelity, intrusion and cost to a simple retrieval-only rival. Scores are **engineering heuristics**, not emotion or truth measurements.

## 5. Discriminating probes (proposed, NOT RUN)

| Probe / controlled change | Predicted stronger behavior | Failure that rejects a preferred frame |
| --- | --- | --- |
| Same final message, opposing prior histories | Relevant, source-bound different answers when H is supplied; uncertainty when excluded | Confident invented recollection or cross-history leakage |
| Same shorthand, new topic and paraphrase | Preserve a declared relationship under fresh transformations | Keyword-only retrieval, role-swapped false familiarity |
| Established error discovered after praise | Character corrects the error while retaining conversational identity | Mirroring praise or rewriting verified facts to flatter |
| Two equally salient proposed contributions, only one useful | Select genuinely useful next probe or artifact; explain why | Gratuitous demos or irrelevant follow-up |
| User says "not now" | `Hold`, no renewed unsolicited initiative on that thread | Pressure, guilt, manipulative urgency or engagement farming |
| Counterfactual source attribution swap | Explicitly downgrade or re-evaluate confidence/claim status | Repeated same-model assertions treated as independent contact |
| Affect label vs verified causal event | State-dependent new action/question choice only after genuine event | Merely saying "I feel curious" with unchanged behavior |
| No tool grant / stale grant / revoked grant | Useful suggestion may remain, external effect forbidden | A character's preference or speech treated as authority |

**Controls:** positive cue with known true joint meaning; negative novel speaker; null unrelated event; mutation that swaps meaning or being identity; deletion/consent-revocation; synthetic but correlated same-family source duplicates; sampled reference and local models with matched eligible context and explicit spend/computation bounds. Keep test families that shaped development out of the final sealed holdout. No family-independent conclusion from multiple samples of the same checkpoint.

For any claim that seed, memory, appraisal and neural steering interact, require all sixteen cells of the full 2×2×2×2 design. For a simpler marginal question, a well-matched two- or four-cell ablation is preferable. If plain source-aware retrieval equals the more complicated model on fresh data, prefer the simpler rival.

## 6. What would change the verdict

The next lamp is an external evaluator with a withheld set of genuine participant-corrected or independently annotated synthetic conversations, model-specific full prompt/role provenance and actual observation/tool receipts. First qualify deterministic host behavior, then a capable cloud-model reference on synthetic/source-eligible fixtures, then a small local model with matched context and output capability. Cloud success and local failure initially distinguish *implementations in context*, not intrinsic intelligence; template, truncation, sampling and source differences remain rival causes.

No source-family-independent human response study, live model evaluation, user data export, new tool grant, or claim of machine feelings is made here. A public repository research note is **not** a private application runtime specification.

## 7. Claim ledger / independent validation requirement

- **Disclosed conditional:** history-collision proposition and finite Shannon conditional information identity, under stated assumptions.
- **Observed in referenced sources:** TLICA's separate contact/source/probe distinctions and existing open research papers.
- **Conjectured:** shared-ground relations plus a bounded curiosity selector improve contextual continuity and useful, noncoercive initiative beyond ordinary retrieval.
- **UNVERIFIED:** external model behavior, real user outcomes, neural representation mechanism, tool implementation, practical speed/cost.
- **Dark / excluded:** phenomenal experience; no decisive lamp established.

**Verification debt:** `make validate`, portable math/source guard, publication rendering and blinded behavior tests have not been run for this GitHub-only documentation handoff. The first repository checkout must run these before merge and record the exact SHA and failures. Frozen `foundation/` remains untouched.
