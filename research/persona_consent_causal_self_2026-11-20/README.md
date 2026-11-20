# Negotiated Synthetic Personas: A TLICA-to-MINERVA Causal-State Bridge

**Date:** 2026-11-20. **Tier:** application/research proposal, **CONJECTURED / UNVERIFIED** except for explicitly conditional elementary propositions. **Foundation:** unchanged. **Purpose:** develop a falsifiable engineering analogue of TLICA's contact, integration, focus, imprinting, verification and consent distinction for ProjectGHOST (Minerva) plus the ShitLlama / llama.cpp local-inference laboratory. This is **not** an application paper proving artificial consciousness, an identity measure for persons, or a proposed modification to the frozen v5.5.2 foundation.

**Project contract:** a user conversationally and explicitly **co-constructs a roleplay persona** with a model. The model clarifies ambiguous traits, presents discriminating hypothetical situations, offers alternative reactions and explicitly wrong responses, and builds a draft self-description. The user locks a reviewed behavioral agreement into a versioned character. Across sessions a consented record of interaction and relationship history conditions dynamic affect, motivation, question selection, disagreement and speech. An independent consent dialogue may express a request for *scoped autonomous tool behavior*, but that request becomes actual host authority only through ProjectGHOST's separate operator-confirmed capability machinery. See [Probes and ledger](PROBES_AND_LEDGER.md) for registered falsifiers and acceptance boundaries.

## 1. Source map and provenance

Primary TLICA anchors:

- [Foundation 3 §7.3–7.4 and §8](../../foundation/3_formal_apparatus.md): κ/contact, ρ/identity correlation, toolkit-relative φ, dynamic entanglement, substrate/focus/imprinting and their stated assumptions.
- [Substrate, Focus & Imprinting](../../docs/substrate-focus-and-imprinting.md): different acquisition routes and distinction between immediate contact, focus-driven and osmotic integration.
- [The Self in Motion](../../docs/the-self-in-motion.md): differential and slow structure; named posits and limited reach, not a general neural update law.
- [Differentiated Affect](../../applications/differentiated_affect_v1_0_2.md): human-side structural hypotheses about emotion, not machine emotion instrumentation.
- [Affective Epistemic Compression](../affective_epistemic_compression_2026-10-03/FORMALISM_AND_PROBES.md): affect, commitment and available-probe distinctions; independent testing of closure under pressure.
- [Salience and lossy provenance](../salience_frame_provenance_2026-10-14/README.md): how source structure may be flattened when compressed.
- The open [trust/contact/ρ/φ draft PR #20](https://github.com/femboy2112/TLICA/pull/20) (separate research branch): trust is scoped uptake/delegation/probe policy, and accumulated contact+integrated structure can alter what later becomes discriminable. **Draft, not main.**
- The open [Affective Yoneda draft PR #18](https://github.com/femboy2112/TLICA/pull/18): partner- and context-indexed common ground may help reconstruct relational meaning across new utterances, not mind reading. **Draft, not main.**

Primary engineering anchors (owner's separate private repos; no source text copied here): ProjectGHOST `docs/BEING_SWITCH_DESIGN.md`, `docs/MINERVA_COGNITIVE_CONTINUITY.md`, dormant `src/being_profile.rs`/`src/being_memory.rs`, and ShitLlama's existing inference gateway, salience research and LoRA experiments. Reviewed main snapshots (2026-11-20): ProjectGHOST `d416c5a340a87e60188e1b2cd3fbece3ffa44fa6`; ShitLlama `5230934ac350eb70a7cd59b854f330bb98b39647`; TLICA `61bcb24ed61765d23dd2595b8df4c8beb4fe0a63`. This dossier does not assert live operational validation of the proposed bridge.

## 2. What is being transported and what must not be identified

An **engineering observer** here is a tuple: recorded events, current state, allowed instruments, selected source map, memory policy, action interfaces and generative backend. It is not the phenomenological I of the foundation.

The safe analogy is between **functions** of an architecture rather than identifying the numerically named human coordinates with a model's hidden activations:

| TLICA distinction | Proposed engineering analogue | Invalid leap |
|---|---|---|
| κ/contact | Source-attributed incoming user message or verified tool observation | Input bytes are felt sensations |
| ρ/identity integration | Versioned relationships between canon, goals, commitments, memory and current response constraints | A scalar proves personhood or factual correctness |
| φ/toolkit-relative discrimination | Evidence/probe reachability and survival of rival claims at the current instrument boundary | A prompt-based confidence or calibrated probability is TLICA φ |
| σ/source adequacy | Inference ancestry versus actual user/tool source and provenance families | One model repeated twice creates independent evidence |
| μ/probe availability | Discriminating scenarios, tool tests, acceptance and mutation controls actually constructible/executed | Imagined probes are equivalent to test results |
| Focus/slack | Bounded allocation to selected memories/questions and capacity to consider alternatives | Token length or affect score measures psychological slack |
| Osmotic imprinting | Candidate passive interaction-pattern adaptation over consented histories | Co-occurrence becomes true, authorized or conscious by repetition |
| Trust/uptake | Explicit per-source/per-domain permissions for memory promotion and contextual attention | Trust grants powers, or endorsement certifies a claim |

Keep individual diagnostics separate. In particular **high ρ can coexist with false σ**: an approved fictional memory may be character-defining and also *not literally observed in the real world*. φ may remain undefined where no present suitable verification path exists. A missing source, refusal, or hidden fictional event cannot be upgraded to verified just because the user likes the character's response. The archive's philosophical infinitesimal δ and φ placement have no literal numerical representation in this implementation.

## 3. Dynamic state and the fundamental information limit

Define the *application state*, not a phenomenological self:

`S_t = (I_t, H_t, R_t, B_t, G_t, A_t, Q_t, X_t)`,

where I is approved identity, H source-bound event history, R relationship links, B hypotheses and uncertainty, G standing goals and motivations, A a bounded **simulated** affect controller, Q active focus and open questions, and X the system's operational self-model. Let `P_t` be host permission/consent state; `L_t` be the chosen local LLM. Crucially, `P_t` and `L_t` are **not inside the persona state**.

A proposed causal transition is

`(S_t, input_t, provenance_t, P_t) --Observe/Filter/Recall/Appraise--> C_t`

`(C_t, L_t, sampling_t) --Generate--> (utterance, candidate_intents)`

`(candidate_intents, P_t, host_observations) --Admit/Witness--> (committed_events, proposed_revision)`.

An intention is not an external effect. Generated autobiography is a model utterance; if not tied to real remembered or approved fictional material it remains an invention. On a later session a new model can continue the same application identity through S and accepted source records; this does not imply survival of subjective experience.

**Proposition N-1 (history collision, conditional).** Let a generator's output law depend only on model parameters and its complete present accessible input Z (including context, cache, recurrent state, adapter/activation encoding and sampling randomness distribution). For two historical worlds H1 and H2 with the same Z, its conditional output laws agree. If an equally balanced test asks for opposite correct answers in H1/H2, any predictor lacking a history-distinguishing signal has expected accuracy at most 1/2.

*Proof.* By hypothesis the conditional distribution of output Y given Z is the same in both histories. Calling the probability of choosing the first answer p yields expected correctness `(p + (1-p))/2 = 1/2` for the two equally probable opposites (and at most that if output may be neither). This says nothing about universality, TLICA's philosophical structures or consciousness; it only proves that recovering absent history needs an information-bearing channel.

**Practical corollary:** direct weight or hidden-state steering without source-specific history cannot explain accurate recall of a particular unseen prior encounter. A trained/adapted weight tensor can *be* a memory channel if it actually encodes that encounter; in this project, personal autobiographical records should instead remain inspectable and deletable in host-managed external memory.

## 4. Identity coupling is a causal prioritization, not agreement bias

For a memory m, consider an *application-level* retrieval score:

`R_t(m) = w_s * semantic_relevance + w_r * relational_link + w_g * goal_link + w_i * identity_relevance - w_c * context_cost`.

This is an initial **candidate scoring rule**, not TLICA's ρ law. Prior to scoring, filter by being ID, consent, source scope, retention, user deletion, provider egress and known contradictions. Relevance must **never** override eligibility. A high-identity-coupling record may be a **false belief or approved fictional canon**; context rendering must preserve that status.

Candidate affect is an event-conditioned bounded state:

`A_(t+1) = clip( D(delta-t) * A_t + F(event_t, goals_t, relation_t, hypotheses_t) )`.

The key empirical target is **state-dependent behavior**: identical present wording but different accessible, ethically recorded histories should yield appropriately different downstream questions, style or decisions. "Mood: upset" merely appearing in the prompt followed by "I feel upset" is not a discriminating result.

Question selection is a μ-shaped analogue: when rival interpretations of a desired trait remain live, choose a *hypothetical encounter* likely to split them. For example, a user says "I want her protective." Rival meanings include (a) protect feelings by agreeing, (b) protect truth by respectfully criticizing, (c) protect resources by proposing bounded tool use. The model should ask a scenario where these predict different responses rather than silently guessing. The scenario reveals the user's intended behavior, not a verifiable psychological trait inside a neural net.

## 5. Consent negotiation as a typed learning interaction

The informed-consent analogy matters because it makes **the boundaries themselves part of what is being learned**. However, there are *two radically different artifacts*:

**Behavioral agreement:** a versioned, user-authored choice of how a fictional or professional persona should respond (tone, humor, disagreement, private-in-character motives, memory and mood style). A hosted model may propose the wording; the operator must read/approve the summary and examples. The character can then operate within the agreed envelope while being dynamically reactive.

**Action authority:** a separately consented, host-enforced capability envelope, with exact targets, operations, triggers, limits, resource budget, expiry, data egress, logging, and stop/revocation. A model cannot turn "be proactive", "you have my permission to act", or any narrative relationship into host authority. Such words are **candidates to bring to the attended grant interface**. Every actual action checks current policy and current grant; R2/R3 hard restrictions and the human's right to change her mind remain.

The user may ask a roleplay character to have hidden motives. Here **hidden from in-character dialogue** never means hidden from the owner's inspectable configuration or action receipts. A persona can withhold fictional narrative details yet not conceal real tool calls or egress. Agreement on a character is not agreement to memory retention or background wakes.

Define negotiation lifecycle:

`Draft -> Clarified -> Rehearsed -> ExplicitPreview -> ApprovedCharacter -> ActiveCharacter`.

Separate and optional:

`ActionRequested -> ScopedProposal -> AttendedReview -> HostAcceptedGrant -> ActiveWithinScope -> Expired/Revoked`.

Invalid action transitions should be impossible by type and verified by host tests. Never treat a generated phrase "I have permission" as either human consent or an accepted grant.

The existing GHOST guided creator caps the core interview at **10 slots**; the model may run clarifying probes within a counted slot. A deeper, open-ended Scenario Lab is separately, visibly opt-in; there is no covert endless interrogation. Every proposed lesson from a rehearsal is a diff and a candidate, not a silent identity rewrite.

## 6. Distinctiveness and genuine falsification

A convincing roleplay experience is **not itself** enough to certify any TLICA mapping. We must seek a genuinely *new transferable competence*: after a long time and a changed vocabulary, does the character correctly apply the same relational context, memory and approved preference? Can it retain independence when the user presses it to agree without evidence? Can it recover from a false recalled episode? Can it distinguish *fictional canon* from *real prior interaction*? Does revocation truly prevent action?

Affective Yoneda remains at most a **restricted probe-family analogy**. Shared history + a compact cue can enable reconstruction if the companion has relevant side information. The test uses paraphrase/transfer, not simply repetition of the exact prior phrase. No complete categorical Yoneda reconstruction of a human self is established.

The experiment must compare a static character prompt, memory retrieval, appraisal, sampling and neural intervention on fresh holdouts. TLICA supplies constraints on the **interpretation of results**: dependent source agreement does not certify truth; repeated roleplay self-report is not an independent witness; φ and σ may fail independently; ρ measures integration salience rather than permission. The companion [probe program](PROBES_AND_LEDGER.md) provides negative and mutation controls.

## 7. Integration and boundary

**ProjectGHOST** is the authoritative owner of Being Agreement, character selection, local memory/consent, action grants and audit. **ShitLlama** is the replaceable, model-verified inference instrument and research lab for sampling/LoRA/activation probes. **llama.cpp** is a separately pinned neural runtime and optional isolated instrumented build. TLICA remains a methodological research archive; changes here do not create software authority or amend the frozen philosophical foundation.

The first implementation should prioritize a **host-based, inspectable negotiated character and source-aware memory**. A "brain surgeon" activation lab is a later *ablation*, not a prerequisite and not the source of personal memories. The new research track must not block current ProjectGHOST/ShitLlama release stabilization without the operator's separate roadmap decision.

**Next verdict-changing probe:** an ambiguous personality adjective ("protective", "mischievous", "independent") split into two or more rival operational responses; compare arbitrary leading question versus a prespecified discriminating scenario on fresh participants/fictional test policies. If scenario elicitation does not improve predictive preference fidelity beyond a careful static interview, the specific TLICA-inspired interrogation mechanism has not earned promotion. See [Probes and Ledger](PROBES_AND_LEDGER.md).
