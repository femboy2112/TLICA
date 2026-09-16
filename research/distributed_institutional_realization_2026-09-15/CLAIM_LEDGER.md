# Claim Ledger — Distributed Institutional Realization

**Branch:** `research/distributed-institutional-realization-2026-09-15` → revised by the
v0.2.0 manuscript (`MANUSCRIPT_DRAFT_V0_2_0.md`).

**Status vocabulary:** Disclosed / Corroborated / Observed / Conjectured / UNVERIFIED / Dark / Refuted

This ledger separates claims already licensed by the current TLICA repository from new application-level hypotheses and from unresolved formal choices.

---

## v0.2 status updates (2026-09-15)

The v0.2 manuscript replaces the v0.1 realization *map* `𝕽_t(P,R,D,S)=I_t` (which risked
being the input tuple renamed) with a **quotient macrostate** `I_t^T=[X_t]_{~_T}` — the
equivalence class of micro-realizations `X_t=(P_t,R_t,D_t)` under equality of the
task-relative response signature `Σ_T`, with the situational field `S_t` kept external.
That move changes five claim statuses. The v0.1 entries below are retained as provenance;
where they conflict with this block, **this block governs.**

- **C-006 (does the institution object earn its keep?)** — split.
  - **Disclosed inside the formal model, now *executed*:** the quotient macrostate is
    *not* the raw tuple, and the response map factors uniquely through it,
    `Resp_T(X;s,u)=Respbar_T([X]_{~_T};s,u)` (Proposition 1, manuscript §7). This is
    demonstrated by [`quotient_demo.py`](quotient_demo.py) (12/12 self-checks): six
    distinct micro-realizations collapse to three macrostates, the induced `Respbar_T` is
    single-valued and reproduces `Resp_T` on all 36 `(X,s,u)` cells with zero mismatches,
    and the quotient is strictly coarser than identity (so `I^T` carries strictly less
    than `X`).
  - **UNVERIFIED (unchanged debt):** whether *useful, stable* institutional quotient
    macrostates exist in real or independently specified institutional domains. The
    formal disclosure buys the object's coherence, not its empirical payoff.
- **C-016 (role-preserving substitution preserves function)** — **construction-level, not
  empirical.** The badge-door record authorizes a *role* (`subject_role="employee"`), so
  role-preserving substitution succeeds *by construction*. The demo (and badge-door)
  exhibit *one coherent role-relative architecture*, not a general law that institutions
  track roles over persons. The real discriminator — `M_role` vs `M_person` on fresh
  holdouts — has **not** been run (manuscript §18.3).
- **C-022 (ρ / causal-participation dissociation)** — **Disclosed as a logically coherent
  dissociation in the finite model; empirical prevalence/coupling UNVERIFIED.** The
  badge-door `rho_institution` is deliberately *never read* by the access decision, so its
  inertness is *stipulated by construction*, not *discovered* by the factorial. The demo
  above sharpens the point: `Resp_T` is carrier-blind by construction.
- **C-008 (local discontinuity)** — **remains Conjectured.** Neither the badge-door nor
  the quotient demo tests the observer-level claim; that needs the
  correct/irrelevant/false-support probe (manuscript §18.4).
- **C-025 (TLICA-specific gain over rival literatures)** — **remains UNVERIFIED.** No
  novelty is claimed before the primary-source rival-framework tomography.

**Re-reading of the old "2×2×2×2 factorial":** it is a **serial-gate pipeline trace**
(`R→Src→A→Y`, identity omitted from the decision path), *not* an orthogonal
independent-factor experiment. The recorded run stays valid as a finite consistency
witness; **no mixed-term / interaction claim** may be inferred from it. A rebuilt probe
must carry all four latent factors independently in every cell (manuscript §18.2).

---

## C-001 — TLICA can represent collective/institutional cases without a group mind

**Claim.** Current TLICA application work already permits collective and institutional analysis through indexed agent profiles plus relational structure/cascades while refusing an unindexed group subject.

**Status:** **Disclosed** within repository boundary.

**Support:** current agency/free-will application language; existing anti-group-mind discipline.

**Debt:** none for the internal textual claim; external philosophical adequacy remains separate.

---

## C-002 — TLICA already contains a precedent for distributed social patterning

**Claim.** The cultural-I is treated as an emergent distributed pattern carried across individual Is rather than an intending agent.

**Status:** **Disclosed** within repository boundary.

**Debt:** determine exact boundary between cultural-I and the broader proposed institutional-realization object.

---

## C-003 — institutional realization requires more than a document

**Claim.** A codified artifact alone is insufficient to constitute the live operation of many institutions; operative realization depends on agents, relations, artifact states, and implementation pathways.

**Status:** **Observed** as a structural premise; external literature triangulation pending.

**Falsifier / hostile case:** identify an institution whose full relevant operation is exhausted by a static artifact with no agent/artifact-interaction realization. If such a case exists, restrict the claim to institutions with active social function.

---

## C-004 — institutional realization is not exhausted by a sum/vector over people

**Claim.** A plain coefficient vector over persons loses role/authority/communication/obligation structure and therefore cannot distinguish many institutionally different configurations.

**Status:** **Disclosed** mathematically for the proposed representation class.

**Reason:** permuting relation structure can alter function while preserving the same person basis and coefficient vector.

**Debt:** none for insufficiency of the plain vector; identify the minimal richer formalism.

---

## C-005 — typed relational structure is load-bearing

**Claim.** The proposed object requires typed relations among agents and artifacts, not merely an untyped social graph.

**Status:** **Conjectured** as a modeling requirement.

**Probe:** compare predictive adequacy of untyped versus typed graph models on toy institutional tasks.

---

## C-006 — the application-level realization map is useful

**Claim.** A map

\[
\mathfrak R_t(\mathbf P_t,\mathbf R_t,\mathbf D_t,\mathbf S_t)=\mathcal I_t
\]

provides explanatory leverage beyond existing TLICA vocabulary.

**Status:** **UNVERIFIED**.

**Primary debt:** show that `I_t` is not merely a renamed tuple.

**Pass condition:** derive at least one useful invariant, discriminator, intervention result, or prediction that becomes clearer or only expressible after introducing the realization object.

**Fail condition:** all work can be done more cleanly by direct reference to the tuple `(P,R,D,S)` with no loss.

---

## C-007 — institutional causal shorthand can be grounded in indexed physical paths

**Claim.** Statements of the form `institution -> outcome` can be treated as compressed notation for a path through agents, artifacts, communication, activation, and physical action.

**Status:** **Conjectured general discipline; Observed in worked examples**.

**Probe:** attempt path expansion for heterogeneous cases: court order, badge door, payroll action, emergency response, informal norm, market convention.

**Falsifier:** find a claimed institutional effect that cannot be represented without adding an unexplained causal primitive.

---

## C-008 — distributed support can produce apparent local discontinuity

**Claim.** A local observer can see abrupt/unmotivated behavior when causally relevant distributed state lies outside the observer's local projection and only becomes locally visible at activation.

**Status:** **Conjectured**, though the generic hidden-state version is standard systems logic.

**Truth debt:** show an institution-specific discriminator, not merely "hidden variables exist."

**Pass condition:** revealing the correctly identified distributed support improves prediction/explanation more than matched irrelevant context.

---

## C-009 — formation/activation separation naturally models institutional latency

**Claim.** TLICA's distinction between formation and activation can represent long-lived role/procedure structure that remains behaviorally latent until a trigger appears.

**Status:** **Corroborated internally** by fit with existing foundation machinery; external empirical application **UNVERIFIED**.

**Probe:** emergency-procedure and role-activation paradigms with matched formation histories and different activation conditions.

---

## C-010 — institutional operation can tolerate heterogeneous agent models

**Claim.** Agents need not share identical global representations of an institution; task-specific interface compatibility may suffice.

**Status:** **Conjectured**, strongly aligned with existing semantic-interoperability work.

**Probe:** simulation or empirical task where agents use incompatible global descriptions but compatible local interfaces.

**Discriminator:** compare global belief similarity versus interface-specific compatibility as predictors of successful coordination.

---

## C-011 — a sheaf-like formalization may fit the phenomenon

**Claim.** Local role-held sections plus overlap compatibility and gluing may provide a natural mathematical representation of institutional realization.

**Status:** **Dark / candidate formalism**.

**Required before promotion:**

1. define base object;
2. define cover;
3. define section content;
4. define restriction maps;
5. define compatibility;
6. define gluing;
7. identify nontrivial obstruction and observable consequence.

**Automatic failure condition:** if the sheaf terminology adds no formal operation beyond metaphor, remove it.

---

## C-012 — hypergraph/tensor/category formulations remain live rivals

**Claim.** Higher-order institutional relations may require formalisms richer than pairwise graphs.

**Status:** **Dark**.

**Probe:** identify minimal examples not faithfully representable by pairwise typed graphs without artificial node expansion; compare complexity and interpretability.

---

## C-013 — codified and lived institution can diverge

**Claim.** The institution inferred from authoritative formal artifacts can differ from the institution actually realized through practice, tacit norms, role behavior, and ambient imprinting.

**Status:** **Observed/conceptually robust; precise metric UNVERIFIED**.

**Probe:** choose bounded organizations where formal procedure manuals and actual workflows can both be measured.

**Candidate outputs:** discrepancy graph, path divergence, action-prediction error.

---

## C-014 — osmotic imprinting contributes to institutional reproduction

**Claim.** Some role norms and operational expectations are acquired through ambient repeated exposure rather than explicit instruction or verification.

**Status:** **Conjectured application of existing TLICA machinery**.

**Rivals:** ordinary implicit learning, social learning, habituation, reinforcement, imitation.

**Debt:** TLICA must not rename established mechanisms; identify what profile/source/identity structure adds.

---

## C-015 — source-path identity can matter independently of message content

**Claim.** Identical propositional content may trigger different institutional responses depending on source-path validity/authority.

**Status:** **Observed as common institutional structure; formal TLICA contribution UNVERIFIED**.

**Probe:** replay identical directives across authorized, unauthorized, forged, and ambiguous source channels.

---

## C-016 — role-preserving substitution can preserve institutional function

**Claim.** Replacing a person with a compatible role-holder may perturb output less than retaining the same person while destroying critical relations.

**Status:** **Conjectured general tendency**, not universal.

**Boundary:** charismatic, person-specific, trust-specific, expert-specific, or legally named roles can violate substitutability.

**Probe:** compare substitution and edge-ablation in toy models and real bounded workflows.

---

## C-017 — institutional persistence is structural, not carrier-identity alone

**Claim.** Some institutions persist through substantial turnover when selected relational/record/source invariants remain intact.

**Status:** **Conjectured**.

**Debt:** define task-relative persistence equivalence rather than relying on intuition.

---

## C-018 — support visibility can be operationalized

**Claim.** A diagnostic such as

\[
\nu_L(y)=\frac{|C(y)\cap O_L|}{|C(y)|}
\]

or a weighted analogue can quantify how much of an outcome's causal support is visible in a local frame.

**Status:** **UNVERIFIED toy diagnostic**.

**Known weakness:** causal support sets are model-dependent and may not be uniquely minimal.

**Probe:** test robustness under alternate causal decompositions and weighting schemes.

---

## C-019 — low support visibility predicts individualizing/arbitrariness attribution

**Claim.** When observers see less of the distributed support for an event, they are more likely to explain it as arbitrary, personality-driven, spontaneous, or irrational.

**Status:** **Conjectured empirical prediction**.

**Probe:** preregistered vignette or interactive-system experiment varying only support visibility.

**Negative control:** add equal amounts of irrelevant context.

---

## C-020 — edge failures and semantic-interface failures are distinct

**Claim.** A path can fail because no connection exists or because connected agents/artifacts interpret the interface incompatibly.

**Status:** **Observed as a useful modeling distinction; TLICA-specific value UNVERIFIED**.

---

## C-021 — participation does not imply intent or responsibility

**Claim.** Carrying part of a distributed institutional pattern is insufficient to establish endorsement, intent, or responsibility for global outcomes.

**Status:** **Disclosed as architectural discipline**.

**Reason:** existing TLICA anti-anthropomorphism / attribution discipline requires indexed production paths.

---

## C-022 — identity-correlation and institutional causal participation dissociate

**Claim.** An agent may be deeply identity-integrated with an institution but causally peripheral, or weakly identified but causally central.

**Status:** **Conjectured structural dissociation**.

**Probe:** construct/locate cases occupying all four cells of high/low identity correlation × high/low causal participation.

---

## C-023 — institutional realization is not identical to the cultural-I

**Claim.** The cultural-I may be one distributed encoding component of an institution, while institutional realization additionally includes typed roles, artifacts, external records, and operational paths.

**Status:** **Conjectured boundary proposal**.

**Debt:** audit all existing cultural-I usage for conflicts before mainline integration.

---

## C-024 — institutional realization is not identical to situational field

**Claim.** `I_t` and `S_t` should remain distinct where possible; institutions can shape fields and fields can activate institutions.

**Status:** **Conjectured but strongly preferred for identifiability**.

**Probe:** construct interventions that alter field with institution fixed and institution with field approximately fixed.

---

## C-025 — TLICA-specific explanatory gain remains unpaid

**Claim.** The present scaffold has not yet shown superiority over network theory, distributed cognition, role theory, social ontology, actor-network approaches, or distributed-systems language.

**Status:** **Disclosed limitation / UNVERIFIED contribution claim**.

**Promotion gate:** no application-paper publication claim of novelty until rival-framework tomography is complete.

---

# Priority order

## Highest-priority debts

1. **C-006:** is the realization object more than notation?
2. **C-008:** does the local-discontinuity thesis yield institution-specific discriminators?
3. **C-010:** can interface compatibility outperform global representational similarity?
4. **C-015:** can source-path formalization add predictive value?
5. **C-023:** clean boundary against cultural-I.
6. **C-025:** prior-art and rival-framework comparison.

## Promotion rule

No claim moves above **Conjectured** merely because the formalism becomes elegant.

Promotion requires at least one of:

- proof inside a declared formal model;
- calibrated decisive measurement;
- independent implementation;
- empirical result with controls;
- primary-source recovery of an equivalent result plus a clear statement that TLICA is translation rather than novelty.
