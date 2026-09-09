# Discriminating probes and limitations

**Status:** prospective research designs; **UNRUN / UNVERIFIED** unless explicitly identified as a package or arithmetic check in `validation_output.txt`. None is a claim that the four thinkers have been experimentally assessed.

Read with the [manuscript](MANUSCRIPT.md), [claim ledger](SOURCES_AND_CLAIM_LEDGER.md), and [integration record](INTEGRATION_AND_VALIDATION.md).

## 1. Freeze the object before assigning the person

An episode record should contain:

```text
episode_id; author; publication_date; original_source; source_family;
access_depth; exact_target_proposition; supporting_evidence;
claimed_inference; explicit_scope; opponent_objection; response;
publication_or_editing_constraints; correction_opportunity;
observed_revision; unresolved_remainder; rival_explanations;
coder_id; coder_conflicts; attribution_uncertainty
```

Use quotations only when necessary and preserve context around any extracted passage. A source's denial that it was understood is evidence to inspect, not a veto; an analyst's confidence that it was understood is not verification. Do not code response absence as refusal when there was no established opportunity to respond. Distinguish correction of wording, factual premise, inference, model, and action policy.

The sources already used to construct this paper are the **development set**. No item becomes a holdout by being renamed. Before collecting a next corpus, freeze eligibility criteria and a complete candidate list, then reserve a dated or randomly selected subset inaccessible to the coders developing the rubric. Register exclusions and missing recordings. Sample successes, corrections, and ordinary arguments as well as controversies. A clip selected because it fits the diagnosis cannot estimate that diagnosis's prevalence.

## 2. Arena hypothesis: separate reception from the speaker's inference

**Rivals:** audience reinforcement broadens confidence; the format compresses an otherwise defensible argument; the audience correctly recognizes a decisive point; critics dislike the style while the inference remains sound.

**Audience experiment:** construct equivalent arguments whose factual premise is either supported or contradicted by a supplied dossier. Cross that factor with persuasive versus neutral delivery while holding propositional content fixed. Use every cell before estimating an interaction. Randomize presentation and blind evaluators to the favored hypothesis. Participants judge proposition accuracy and rhetorical success separately, then receive the dossier and may revise.

**Pass:** delivery changes perceived truth beyond what premise quality explains, with the preregistered effect and uncertainty criterion met. **Fail:** the predicted effect is absent with adequate precision, or confidence responds appropriately to evidence regardless of delivery. **Ambiguous:** delivery changes substantive comprehension, manipulations do not preserve content, or estimates are imprecise. No numerical threshold or sample size is invented here: pilot variance and an explicitly justified power or precision analysis must precede registration.

**Controls:** a genuinely valid decisive argument; a persuasive but dossier-refuted claim; a neutral presentation with no audience cue; a mutation that changes one quantifier and should change the proposition verdict. Ethical consent and debriefing are required for manipulated social feedback.

**Person-level boundary:** this tests audience reception, not Hitchens's internal phenomenology. The corresponding archival test asks whether his subsequent claims actually cite rhetorical victory as warrant for a broader conclusion. H-03 is a candidate recording only; its complete contents have not been coded.

## 3. Reconstruction hypothesis: fidelity and credibility must be scored separately

**Rivals:** charity improves discrimination; charity produces equalization; the reconstruction changes the target; the original objection is incoherent; the method genuinely preserves and resolves it.

Prepare paired original passages and reconstructions, with separate ratings for fidelity, evidential support, and whether the reply addresses the identified objection. Include one weak argument reconstructed accurately, one strong argument reconstructed inaccurately, and one improved argument falsely attributed back to its original author. These prevent mere eloquence from passing the fidelity gate.

For the Dennett-Zahavi dispute, include relevant surrounding text and Dennett's full response before formal coding. Recruit readers competent in each tradition and a methods reviewer. Record affiliations and prior commitments; disagreement among readers is not automatically a substantive tie. Ask each side to specify a distinction whose retention or loss changes an answer.

**Pass for equalization:** equally faithful reconstructions receive similar evidential weight despite deliberately unequal supporting evidence. **Fail:** fidelity is preserved while credibility tracks evidence. **Ambiguous:** evidence quality was not successfully manipulated or the target proposition changed. A laboratory result about readers would not establish Dennett's habitual practice.

**Pass for method-relative closure in an archival episode:** a load-bearing distinction is demonstrably removed, the removal determines the apparent rebuttal, and no independent argument justifies it. **Fail:** the distinction is preserved or its rejection is independently argued. **Ambiguous:** rival accounts remain equivalent under the available probes. That is unresolved discrimination, not evidence that either tradition is meaningless.

## 4. Identity-coupling hypothesis: test alternatives to psychologizing

**Rivals:** competence-related self-protection; legitimate rebuttal of a misquotation; platform constraints; a stable but defensible view of public discussion; the critic's own error.

Build a corpus pairing domain-local corrections with similarly supported cross-domain or competence-relevant challenges. Anonymize author names for initial argument evaluation. Preserve original versions separately so that anonymization cannot erase scope, chronology, or institutional role. Have coders identify the actual objection before classifying the reply. Distinguish literal implication, substantive premise, pragmatic implication, and communicative purpose.

**Pass:** after predeclared matching, competence-relevant challenges show the specified selective reduction in engagement or revision, and alternative explanations perform worse on a fresh subset. **Fail:** responsiveness is comparable, or the alleged evasions answer the actual objections. **Ambiguous:** the corpus cannot establish exposure, matching fails, or the conclusions depend on recognizing the author.

**Controls:** W-02 as a development-set correction example; an invented perfectly valid but rude response; a polite response that evades the question; a name-swap check on the same argument. Name-swapping tests the evaluator, not Dawkins. No behavioral outcome alone uniquely identifies rho, and no private psychological diagnosis is licensed.

## 5. Model-to-policy hypothesis: retain the bridges

Record separately:

```text
causal claim -> population association -> observable indicator ->
prediction under defined conditions -> decision rule -> consequences
```

For a new study, use neutral synthetic labels rather than judging real people from appearance or inferring religion from images. Fix the outcome, observation procedure, budget, and comparison policy before optimization. Supply or vary proxy sensitivity, false-positive rates, observation costs, and outcome costs explicitly. Preserve the difference between a model's assumptions and measured properties of a setting.

**Pass for warrant substitution:** a decision is claimed to be supported by group association even when controlled changes to the observation/implementation layer reverse its performance. **Fail:** the decision is conditioned on those layers and changes appropriately. **Ambiguous:** alternatives were not made feasible under the same constraints or different values were silently optimized.

**Controls:** an informative proxy with low cost; an uninformative proxy; a systematically misleading proxy; and an accurately measured predictor whose acquisition cost exceeds its benefit. Include a no-action baseline and at least one matched-budget alternative. Do not mistake a rare outcome for proof that useful prediction is impossible, or prediction for automatic permission to act.

The exact toy worlds in the manuscript exercise only the nonimplication from association to proxy utility. They are not fitted examples, empirical holdouts, a validated screening strategy, or instructions for real-world security deployment.

## 6. Source-family audit and the weakest sufficient instrument

The initial instrument is a qualitative source-and-inference audit. No numerical interferometry, phase, amplitude, or truth score is needed. No common-basis physical transport has been declared, so no phase claim is made. No factorial interaction is claimed from the historical four-person comparison.

| Remove this source family | What becomes weaker or unavailable | What does not depend on it |
|---|---|---|
| Hitchens authored reports | The specific error/repair and probe-willingness examples | Logical distinction between defeating a defense and refuting its target |
| Dennett-Zahavi dispute | The developed methodological disagreement | Distinction between faithful representation and evidential weight |
| Dawkins public/revision reports | This person's observed argumentative and revision examples | Distinction between generation and independent checking |
| Harris-Schneier exchange | The detailed scope and operational-warrant criticism | Finite association/proxy counterexample |
| GHN study family | The selected empirical rival decomposition | The requirement to measure a proposed causal variable |
| Baldwin text | The chosen literary illustration | Normative separation of human worth and propositional credibility |

This table is a dependency analysis, **not an executed quantitative leave-one-family-out experiment**. Mirrors are grouped by originating document. Same-author sources may concern distinct episodes while sharing self-report limitations. Same-model drafting passes are not independent reviewers.

## 7. Publication gates

Before a person-level empirical claim is promoted beyond conjecture: obtain full load-bearing texts, freeze the corpus and hypotheses, use independent documented coding, establish correction opportunities, preserve contrary episodes, test a fresh subset, and report uncertainty and missingness. Before a philosophical claim is called resolved: identify the exact proposition, reconstruct the strongest live objection, and supply an argument that does not presuppose the disputed translation.

The appropriate current stopping point is an evidence-bounded research draft with named unresolved gaps. It is not contextual saturation: known source and probe gaps remain. The next verdict-changing work is the reconstruction-fidelity audit for Dennett and the episode-level correction analysis for Dawkins, where attribution is presently weakest.
