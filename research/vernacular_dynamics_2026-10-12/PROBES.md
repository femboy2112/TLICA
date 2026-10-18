# Risky probes, negative controls, and empirical release gates

**No human studies or real-corpus evaluations have been run.** This is a protocol sketch for later preregistration, subject to consent, privacy, and human ethics review. Do not deploy as automatic judgments of individuals.

## Predeclare four rival models

M0: lexical baseline (surface word and local sentence).
M1: context baseline (speaker role, surrounding discourse, community, and task).
M2: generic behavior-only baseline (observable actions without TLICA coordinates).
M3: proposed typed TLICA reconstruction (world/source separation, observer decoder, candidate identity integration, pathway and correction probe).

**Discriminating criterion:** if M3 does not improve held-out sense prediction, calibrated abstention, or out-of-context transport over M1/M2 without unacceptable complexity or bias, then the **incremental TLICA claim fails**. A model that simply gives every situation a new sense is not allowed to win by redescription.

## Vibe: decoder versus stable world property

**Hypothesis V1:** observer-specific context and decoding will account for residual divergence after controlling observable cues and shared task.
**Alternative:** impressions are effectively observer-invariant given adequate standardized cues.
**Pass:** preregistered additional information improves held-out prediction of independent, consented comfort/return judgments.
**Fail:** no incremental predictive improvement, or a simple situational model performs equally.
**Ambiguous:** observation is too sparse or participants' criteria changed between measures.
**Controls:** pleasant surface with masked discomfort; direct-but-kind interaction; observer with preexisting dislike; source contamination and social-desirability effects.

## Cope: three usages must not be fused

**Hypothesis C1:** credible contradiction and identity-relevant stakes jointly predict a distinct *defensive-update pattern* beyond ordinary distress regulation; a rhetorical insult is a third output channel.
**Alternative:** context and evidence-quality variables fully explain outcomes; no extra identity-coupling mechanism required.
**Pass:** stronger held-out differentiation after blinded ratings of evidence quality and separate elicitation of beliefs, without treating rhetorical accusations as mental-state labels.
**Fail:** the inferred "defensiveness" vanishes after evidence quality and ordinary coping are controlled; or accusing speech is confused with target behavior.
**Ambiguous:** no credible discriminator exists, or reliable evidence and task stakes cannot be established.
**Controls:** adaptive coping with accurate belief update; rational skepticism toward weak evidence; false accusation; sincere disagreement.

## Lost in sauce: immersion versus disorientation

**Hypothesis L1:** independent reorientation and correction probes, not immersion duration, discriminate task-absorbed flow from task-disoriented capture in a declared local setting.
**Alternative:** the term is predominantly pragmatic/humorous; no stable task-level mechanism survives context control.
**Pass:** preregistered calibration separates the classes on fresh tasks with predictable reorientation consequences.
**Fail:** equal reorientation at matched immersion or baselines dominate; no unique sense partition survives transfer.
**Ambiguous:** goals were not predeclared, the interruption itself caused error, or the episode had no meaningful objective checkpoint.
**Controls:** absorbed-but-correctable flow; bored-but-disoriented; voluntary uninterrupted immersion; confounded sleep/stress conditions without clinical attribution.

## Data and provenance plan

First use hand-authored examples strictly for unit tests, then a separately curated annotated corpus of permission-compatible public examples across platform, time and community. Preserve exact link/date, sense alternatives, speaker stance, and uncertain interpretations; avoid treating repeated copies as independent sources. Human annotators should be blinded to preferred mechanism and allowed to abstain. Split train/evaluation by author/source family and context to reduce leakage. Collect participant-correctable human material only with consent, no protected-trait profiling, and minimal data retention.

Report original and ablated results by feature family: lexical, context, direct behavior, observer interface, candidate TLICA trajectory. Corrected claims inherit their weakest empirical premise. Do not infer any person's mental illness, deception, or stable identity from a slang label.

**Future verdict-changing instrument:** randomized, low-stakes vignette sets crossing spoken label (present/absent), independently known behavioral evidence (supporting/contradicting), context (congruent/shifted), and speaker role (self-report/accusation). Require all cells before interaction claims. Predefine which rival predicts each cell; no post hoc rescue.
