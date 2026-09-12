# The Differential-Field Reformulation of TLICA — Working Model

**Status:** Exploratory research-tier working draft. Foundation (v5.3.3) frozen and UNCHANGED. Mechanism Conjectured; large parts are (honestly) a redescription of established science, with two candidate novel edges. Nothing here is promoted into the foundation.

**Date:** 2026-09-12. **Author of the model:** Leah. **Analytical synthesis:** assistant.

**Purpose:** durable capture of an in-progress dynamical/differential reformulation so the work can be resumed rather than rebuilt.

> **In plain terms —** This takes TLICA's existing pieces — the modes, the two prerogatives, salience, the choice-filter, slack — and asks whether they are the surface of one *dynamical system*: a self that reads a moving world against itself, feels the difference, and is pushed to act. Most of what falls out is known science recovered from first principles; two pieces might be genuinely new.

## 0. Genesis — the differential is derived, not imported

The theory is reconstructed cogito-up. Thought experiment: dropped into infancy with full intelligence but source-maps and self maximally scrambled — rebuild yourself from the one thing that survives the scramble. The only certainty is *I am* (cogito). The first postulate — a "first sound leap", not a theorem — is **I => not-I**: if I exist, that-which-is-not-me exists. Given the intrinsic-structure and asymptotic-field primitives, the rest of the TLICA machinery is claimed to follow.

This is Fichte's move (the I posits itself, then opposits the not-I). Its significance for the grounding below: where the Free Energy Principle *stipulates* the self/world boundary (a Markov blanket) — and is charged with tautology for exactly that — TLICA *derives* the boundary as the minimal forced first inference. The differential the self reads is therefore not borrowed from predictive processing; it is the first consequence of "I am".

**Caveat:** I => not-I is a POSTULATE (the load-bearing axiom). Fichtean lineage, minimal, but unproven — the whole edifice rests on it. "The rest follows trivially" is the hypothesis the math-justification program is grading step by step (already: reachability core Derived; toolkit-partition Refuted).

## 1. The dynamical model

**Operator/state split** (the move that keeps everything consistent):
- **Mode-B frame-STATE** — always-on. The occupied frame = a point/region in lived-I profile space (P_{m,t}) = the self's current BASELINE / "context window". Present from t=0, even when empty.
- **Mode-B reflexive OPERATOR** — the foundation's Mode B; produces resolvable/calibrated output only after structure accumulates, and carries the developmental onset the foundation describes.

**Reading and acting:**
- The self reads the **field** (the asymptotic content/reality domain A^m_t) only *against its baseline*.
- **V = felt phenomenological salience = felt magnitude of (field-content minus frame-baseline).** A FEELING, pre-judgment. NOT "hurt" (hurt is a downstream actualization). NOT a utility (V is affective magnitude, not decision-worth) — this keeps V out of the smuggled-utility trap.
- V operates on **vectors** in profile-space, not scalars. A small off-axis mismatch is a targeted update; a high-dimensional mismatch (thin toolkit / hostile environment) makes the state MORPH rather than switch.
- **A and C are signed vector updates**, selected by the SIGN of the differential against the PtCns baseline: consistency-preserving deviation -> C (integrate); consistency-damaging deviation -> A (differentiate). **PCE sets/shifts the baseline; PtCns-deviation-sign picks the branch.** This formalizes the foundation's explicitly-unformalized A/C selection rule (foundation/2_access_and_development.md:156), with both prerogatives load-bearing.
- V **pressures a filter over the choice field** available in the moment:
  - **No slack -> pressured filter dominates -> automatic A or C, no active Mode B** (greedy-local descent).
  - **Slack -> active Mode B reweights the filter -> the felt sense of having chosen** (horizon-extended; can spend local salience to escape a local basin). Slack = the uphill budget; the "underground" = climbing forever, never banking the descent.

**Dynamics:**
- Passive dynamics (no active Mode B) = **dissipative tracking of a moving field.** Because reality moves regardless of the self, V = V(x,t) is NON-autonomous: dV/dt = (partial V / partial t) minus |grad V|^2. The drive term breaks monotone descent, so the self ORBITS (chasing a moving minimum) -> **resonance** (V crosses 0, never sustains it). This is **allostasis** (stability through change; moving/anticipated setpoints — Sterling and Eyer), not fixed-point homeostasis.
- The orbit needs NO internal oscillator: it is driven. And there is **no frozen world** — the substrate is itself moving reality (interoception, autonomic, neural, metabolic), so the drive never stops; the "autonomous oscillator" category collapses into "internally driven".
- **V=0 is unreachable for a living substrate** (= thermal equilibrium = death; a living system is a non-equilibrium steady state). See section 5.
- "Ringing between attractors without settling" = neural **metastability** (Kelso/Tognoli coordination dynamics; Friston metastable brain; Rabinovich winnerless competition) = the phenomenological face of the math-justification program's Round 2 (metastability).

## 1.1 V as a functional on profile-space (formalization)

The pieces above become one object once V is written as a functional. All ingredients are native TLICA.

**Objects.**
- **Profile space** P_{m,t}: the identity-correlation profile of I *m* — the (κ, φ, ρ)-coordinated structure over the content set. Take the relevant state as a point/region *b* in a normed profile-space P, whose tangent space carries displacements.
- **Baseline** b_{m,t} ∈ P: the occupied Mode-B frame-STATE (always-on) — "where the self currently sits."
- **Field-reading** f_{m,t} ∈ P: the profile-image of the asymptotic field A^m_t *through the substrate* — "what the world, read against me right now, presses my profile toward." Substrate-mediated (the I never reads the field raw; foundation File 3, §8.5).

**The differential and V.**
- **Differential** Δ_{m,t} = f_{m,t} − b_{m,t}: a **vector** (displacement) in profile-space. This is the reference-dependent quantity — reality read *against the self-as-baseline*, never in absolute terms.
- **V (felt salience) = the ρ-weighted magnitude of the differential, scaled by temperature:**

  > **V_{m,t} = T_{m,t} · ‖ Δ_{m,t} ‖_ρ**

  where ‖·‖_ρ is a metric on profile-space weighting each axis by its identity-load (ρ): a unit mismatch on a high-ρ axis (something you deeply *are*) yields more felt salience than the same mismatch on a low-ρ axis (something peripheral). This is exactly why loss of a high-ρ content is felt as loss-of-self (the Mode C candy case) while a low-ρ mismatch barely registers. T_{m,t} ≥ 0 is the **temperature/reactivity** control parameter (§5): felt salience per unit differential (the susceptibility law dV/d(perturbation) ~ T; T→0 = inert = the death limit).

**Why a functional, not a scalar rule.** Δ is a vector; V reads its ρ-weighted *norm* (felt intensity), but the **direction** of Δ is retained and does the mode-selection work:
- Project Δ onto the **PtCns consistency-gradient** at b (the direction that would preserve/extend the frame's coherence). The **sign** of that projection picks the branch: consistency-*extending* deviation → **Mode C** (integrate: move b toward f); consistency-*damaging* deviation → **Mode A** (differentiate: push f out, hold/repair b). **PCE sets/shifts the baseline b; the PtCns-projection sign picks A vs C** — the research-tier formalization of the foundation's deliberately-unformalized A/C selection rule (foundation/2:156), offered here, *not* smuggled into the frozen core.
- **Dimensionality** of Δ sets update *type*: low-dimensional → a targeted update; high-dimensional mismatch (thin toolkit / hostile field) → the state **morphs** rather than switches (global reorganization of b), matching the profile-shape-disturbance vocabulary (foundation File 4, §10.5).

**Honest status.** The ρ-weighted-norm form is a MODELING CHOICE *consistent with* (not forced by) the foundation. Differential/baseline coding is the STRONG-grounded core (Schultz RPE, Helson, Kahneman–Tversky); temperature-as-gain is the susceptibility reading (§5). Conjectured as a unification; introduces no new primitive.

## 1.2 The driven orbit, formally

Passive dynamics (no active Mode B) = relaxational descent of a mismatch potential Φ(b, f_t) = ½‖f_t − b‖_ρ². Then

  > **db/dt = −γ · grad_b Φ = γ · (f_t − b) = γ · Δ_{m,t}**

— the baseline relaxes toward the field-reading (**allostasis**, Sterling & Eyer; not fixed-point homeostasis). Because reality moves regardless of the self, f_t is time-dependent, so V = V(x,t) is **non-autonomous**:

  > **dV/dt = (∂V/∂t) − ‖grad V‖²**   —   drive (field moves) minus dissipation (self descends).

When the drive term matches or exceeds dissipation, V never reaches 0: the baseline chases a moving minimum and **orbits**. No internal oscillator is needed (the orbit is *driven*), and there is no frozen world (the substrate is itself moving reality — interoceptive/autonomic/metabolic), so the drive never stops. V=0 is unreachable for a living substrate (= NESS = the T→0/death limit, §5). The never-settling ring is neural metastability (§1) = the phenomenological face of math-program Round 2.

## 1.3 Reflexive relativity (the inside view reads only differentials)

The deepest structural principle the model rests on, made explicit: **the inside (first-person) view has access only to *differentials* — observable changes against a baseline — never to *absolutes*.** This is the differential/baseline-coding core (§1.1) applied reflexively to the self's access to *itself*. Absolutes are inaccessible from inside, and they resolve in exactly two ways:

- **Gauge (unobservable → uncommitted).** Where an absolute has *no observable consequence*, the architecture should not commit to it — the way physics refuses to commit to an absolute rest frame, because no experiment inside the frame distinguishes zero velocity from any constant. *Application:* the Mode-B onset question. "Is Mode B present-but-masked or genuinely zero at developmental origin?" is an absolute-baseline question with no registrable consequence below the resolution floor. The honest architecture declares it a **non-question** and commits only to the observable **differential** — onset = the threshold-crossing into resolvable operation. (This is why the foundation onset text should read "zero *resolvable* capacity," leaving the sub-threshold absolute undetermined — and why the always-on frame-STATE reading of §1 is a *model-tier* claim about the dynamics, not a foundation commitment: presence at t=0 is a velocity-claim invisible in the t=0 still.)

- **Model (unreadable → self-modeled).** Where an absolute is not directly readable from inside, the agent runs a **self-model** of it. *Application:* the driver of a focus-deformation ("did I aim, or was I captured" — §4.1, choice/filter). This has THREE regimes, and the honest picture (established by adversarial re-test 2026-09-12; see §6.2) is graded, not clean:
  - **Clean interiors — third-person readable.** Pure top-down aiming in a sensory void (no exogenous trigger coupled in the window) = motor; a genuinely novel capture with no prior osmotic history = wind. Here an outside observer with the trajectory + the exogenous input stream can read the driver.
  - **The co-constituted middle — no sharp fact even third-person.** Osmotic activation (foundation/3:466/470/476) is exogenous-in-origin, endogenous-in-presentation, routed through the *same* salience gate as capture; and the lived-I "motor" is itself *built by imprinting from not-I*, with no timestamp at which absorbed-wind becomes self (foundation/3:264/270 continuous blend). So in the developmentally-central bulk of adult focus, "motor vs wind" is **not a clean partition** — the self that aims was built by the world it responds to.
  - **The agent's access is always the self-model.** First-person, the driver is read only through a self-model — and in the co-constituted middle this is **ontic, not merely epistemic**: there is no sharp driver-fact to read, so the self-model is doing constitutive work, not lossy estimation. This predicts agency as **simultaneously real and confabulable**, and it **is** the perceived-vs-actual-slack split (§5.1): perceived slack = what the self-model certifies; actual slack = the fact (where a fact exists at all).

**One wall, two doors.** The absolute is either gauge (unobservable → drop it — item ①/onset) or modeled (unreadable, and in the middle *co-constituted* → the agent's self-model — item ②/driver). Grounded in the architecture's own outside-perspective limits: source-attribution is explicitly outside-perspective (foundation/3, §8.5). Reflexive relativity generalizes that into the model's backbone. **Caveat (honest):** this is a MODEL-tier organizing principle; it did NOT yield a decidable driver-predicate for the frozen foundation (§6.2), and the co-constitution finding is *why* — the split it would need is intrinsically fuzzy in the middle.

## 2. This is a unification, not a new theory

Every part already lives in TLICA, scattered: felt salience (first/third-order pathways), emotion along meaning-axes (Differentiated Affect + osmotic history), self-as-baseline (PtCns), the choice-field + filter + slack (Choice-as-Filter + Referent-Routing). The contribution is the *dynamical circuit* that fuses them — not new parts.

## 3. Grounding verdict (2026-09-12 fan-out; honest)

- **Differential/baseline coding — STRONG, earned.** Dopamine reward-prediction-error (Schultz), adaptation-level theory (Helson), prospect-theory reference-dependence (Kahneman and Tversky), center-surround. The core principle is mainstream.
- **Steady-state V=0 — PARTIAL / idealization.** Baselines are NOT always re-zeroed; set-points can be permanently displaced (Diener, Lucas and Scollon). Chronic bad reality shifts the baseline for good — a metastable basin. (Relief is not resolution, made literal.)
- **V-as-FELT exceeds FEP.** FEP is agnostic on feltness; the differential is better-evidenced as a *learning* signal than as the feeling itself (Berridge liking vs wanting; Barrett/Seth add a categorization step). "It is a feeling, pre-judgment" is real content FEP does not supply.
- **Active inference / FEP — SHAPE-only, riding a contested/tautological universality.** "Any NESS + Markov blanket minimizes free energy" is close to tautological under stipulated assumptions (Bruineberg et al., The Emperor's New Markov Blankets; Aguilera et al. on non-generic blankets). The embedding argument earns COUPLING (a differential exists), NOT V's specific form (self-as-baseline, felt-quality, mode taxonomy, slack-gate). Closest real precedent: Joffily and Coricelli 2013 (valence = negative rate of change of free energy) — but that is a temporal derivative of an already-evaluated valence, not TLICA's static pre-judgment V.
- **Proto-words = redescription of holophrastic speech** (Dore primitive speech acts; Greenfield and Smith; Bloom processing-capacity) UNLESS a cross-domain dwell-ceiling is confirmed (a shared short ceiling across linguistic AND non-linguistic self-referential behavior, decoupled from vocabulary and articulation maturity). Candidate instrument: gaze-contingent eye-tracking extended into toddlerhood. Closest existing design: Lewis and Ramsay 2004 (co-emergence, not a controlled discriminator). UNRUN.
- **ADVERSARY verdict — REDESCRIPTION**, collapsing into active inference + reference-dependent affect (Helson/Kahneman) + dual-process emotion regulation (Gross; Daw model-based/model-free; Shenhav Expected Value of Control). ONE candidate does not collapse: the **slack-gated agency phenomenology** — felt-choice as a THRESHOLD on (capacity minus pressure), dissociable from behavior, sign-flipping at capacity = pressure; plausibly distinct from Expected Value of Control (which predicts allocation, not agency-phenomenology). But it is currently UNTESTABLE: slack is not operationalized, and the repo already names the "insufficient-slack unfalsifiability trap". Novelty unearned, not killed.

## 4. The two genuine edges

1. **Foundational (real, now):** the cogito-up construction. FEP asserts the boundary; TLICA derives it. A better-*founded* account of the same dynamics, and the answer to the tautology charge.
2. **Empirical (potential, unearned):** slack-gated agency. The one prediction that did not collapse. **The paper = operationalize slack independently, then test whether felt-choice dissociates from behavioral change at the capacity = pressure threshold.** Land that, and it is a rival, not a retelling.

### 4.1 Slack, operationalized

**Slack, formally.** Slack S = the room for the reflexive operator (Mode B) to deviate from greedy relaxational descent — the *uphill budget* that lets the self spend local salience to escape a local basin (horizon-extension). Passive dynamics is pure descent along −grad Φ (§1.2); active Mode B injects a reweighting w that can move b *against* the local gradient. The budget for that:

  > **S_{m,t} = M_m(t) − Pressure_{m,t}**

where M_m(t) is the inherited focus-capacity bound (foundation/3:260) and Pressure rises with V and with the *determinacy* of the demanded response. The threshold:

- **S ≤ 0** → the pressured filter dominates → automatic A/C, **no active Mode B**, no felt choice (greedy-local descent).
- **S > 0** → the reflexive operator reweights the filter → the **felt sense of having chosen** (horizon-extended).

**The sign-flip at S = 0 (capacity = pressure) is the model's live, non-redundant prediction.** Felt-choice is a *threshold* phenomenon on (capacity − pressure), dissociable from behavior: near S=0 the behavioral output can be identical on either side while the *felt agency* flips. Plausibly distinct from Shenhav EVC, which predicts control *allocation*, not agency-*phenomenology*.

**Slack splits: perceived vs actual** (native TLICA; the "stuck but capable" case). Perceived slack = what the self-model certifies the will can use; actual slack = what is really there. The gap is where "stuck but capable" lives.

**Two independent handles → the experiment** (the route out of the unfalsifiability trap; causes detailed in §5.1): environmental volatility drives **temperature T** up (Behrens: volatility → gain); toolkit incoherence drives **perceived slack** down (low Cl(Tools) certifies little). Because the two manipulations are independent, T and perceived-slack become independently addressable. **The experiment:** manipulate environmental volatility (T) and toolkit coherence (perceived slack) independently; test whether *self-reported felt-choice* dissociates from *behavioral change* across the S=0 threshold. That dissociation is what would make the model a rival rather than a retelling.

## 5. "Temperature of consciousness" (2026-09-12 note; corrected)

**Temperature = reactivity, not particle heat.** The right reading is a CONTROL PARAMETER: how hard V swings per unit of environmental perturbation — how chaotic/sensitive a being is to its environment. **High temperature => large oscillations** (volatile, sensitive, near-chaotic); low temperature => damped (stable, cool, unreactive).
- **This is tighter, not looser, than a thermodynamic reading.** "Temperature sets fluctuation amplitude" is the exact statistical-mechanics relation (fluctuation variance scales with temperature; susceptibility) — located on the macro-variable V, not on constituent particles. "High temp => large oscillations" is the susceptibility/gain law.
- **Same knob as the grounded frame:** temperature ~ inverse precision (beta) in active inference; ~ neural gain (locus-coeruleus / norepinephrine modulation, Aston-Jones and Cohen); ~ softmax/Boltzmann temperature (high = exploratory/random, low = committed); ~ proximity to criticality (susceptibility peaks near the critical point). All one parameter: output-per-input.
- **Temperature vs slack — likely two coupled axes.** Temperature = swing amplitude per perturbation (gain). Slack = room for the reflexive operator (Mode B) to reweight/damp the swing. High temp + low slack = maximally volatile; low temp + high slack = cool and deliberate. Open: does slack SET temperature, or are they independent?
- **Absolute-zero survives, reframed:** zero reactivity = perfectly unreactive = inert = dead. A living being always runs at temperature > 0 (the substrate always moves), so "V never flatlines" = "temperature never reaches zero"; death is the T -> 0 limit. This absorbs the non-equilibrium-steady-state point (section 1) as the *reason* temperature never hits zero, and drops the entropy-conjugacy (T = partial-E / partial-S) baggage: a literal thermodynamic temperature is neither needed nor claimed.

## 5.1 Control-parameter phase diagram (temperature x slack x context)

**Two knobs, not one — and slack itself splits.** Temperature (reactivity/gain) and slack (room for the reflexive operator to reweight/damp) are independent axes. Slack further divides into **perceived slack** (what the self-model certifies the will can use) vs **actual slack** (what is really available). This split is native TLICA: slack access is gated by the self-model ("stuck but capable" = high actual, low perceived slack). Both knobs interact with the **context as it pertains to the self** (how determinate the situation and its demanded action are).

Worked cells (the model's differentiated predictions):
- **High temp + low slack + determinate high-stakes context -> decisive action.** ("Someone broke in and will kill me unless I attack" -> attack.) The pressured filter has a clear peak; no reflection needed; reactivity supplies the drive. Reactive AND adaptive.
- **High temp + low slack + INDETERMINATE context -> Mode-B recursion (the underground) OR maladaptive A/C.** ("Deathly anxious, something is wrong, cannot pinpoint it.") High pressure, no room to reweight, no clear peak -> either spin in unresolvable reflection or misfire differentiation/integration onto wrong targets. The anxiety/panic cell.
- **High temp + high slack + open (many neutral) paths -> a well-reasoned, high-magnitude trajectory (possibly ultimately misguided).** Reactivity supplies magnitude, slack supplies reasoning room, open context supplies freedom to construct. The visionary/grand-folly cell: sound reasoning, big committed move, premises possibly wrong (well-reasoned is not correct).

**The two knobs have named causes — which are also the operationalization handles:**
- **A disordered/volatile environment drives temperature UP** (unpredictability -> large prediction errors -> high gain; cf. volatility -> learning-rate/gain, Behrens et al.).
- **A disordered logical toolkit (incoherent / mutually contradictory tool-joints) drives PERCEIVED slack DOWN** (an incoherent toolkit certifies little, so the self-model cannot see the slack even when actual capability exists -> "stuck but capable"). Ties low slack to toolkit-coherence (Cl(Tools)) and the perceived/actual gap.

**Why this matters for the empirical edge (section 4):** these two causes are independent manipulations of temperature and slack. Manipulate environmental disorder (temperature) and toolkit coherence (perceived slack) independently, and the phase diagram predicts distinct outcome cells. That is a candidate route OUT of the "insufficient-slack unfalsifiability trap": the handles make the axes independently addressable, which is what the slack-gated-agency edge needs to become testable. Still a structured Conjecture until the cells are actually measured — but testable-in-principle, which it was not before.

## 6. Foundation docket (GATED — foundation currently UNTOUCHED)

Two candidate foundation touches, neither done, both gated on scrutiny + Leah's explicit decision. The assistant never edits frozen v5.3.3 unilaterally.
1. **Section 4.4 Mode-B onset errata — DRAFTED (2026-09-12), awaiting sign-off.** Rewords foundation/2:134 (+ the :120 / :186 glosses) from the hard "must cross zero / No I has Mode B capacity" to the SNR reading: Mode-B capacity at origin is **bounded above by the resolution floor** set by the Mode-A/C dynamics (whether exactly zero or an unresolvable trace is below the architecture's resolving power), and **onset = the signal-to-noise separation threshold**. Brings :134 into line with the foundation's own online-but-negligible template — §8.7 File 3 ("online while effective osmotic update is arbitrarily small") and §10.5 File 4 ("not yet operating or only weakly operating"). The draft explicitly does NOT assert a full reflexive operator running at t=0 (guards against the modes-emergent overread — that larger claim does NOT ride in on the errata). Small, errata-grade; `make validate` green. Drafted on branch `research/foundation-errata-2026-09-12`; **NOT landed to main.**
2. **choice-as-filter promotion — SCRUTINY DONE (2026-09-12); VERDICT: DO NOT promote; foundation UNTOUCHED.** Corrections to the earlier read: the cascade is CONTAINED (slack is textually disjoint from choice-as-filter; the agency stack does not move), and the foundation is NOT point-coded on option selection (Foc is already an allocation/selection function the filter parameterizes; options are quotient classes O = F/~, choice_as_filter:907; free_will:191 keeps point-selection as an explicitly non-degenerate compatible description). The decisive open hinge is the image condition Im(π)=fraktur-F (§24 check 1). **§24.1 audit + design pass + two reframe re-tests all failed to discharge it:**
   - The audit is ILL-POSED: fraktur-F has no independent extensional characterization; it is defined only circularly via π.
   - A 4-candidate design pass (substrate-reachability, toolkit-definability, constraint-intersection, generative-closure) — ALL DIED. Convergent finding: TARGET-based predicates over-generate (a self-directed aim onto x and a contact-driven capture by x share support+size); ORIGIN-based predicates need a per-allocation source/basis map absent from the frozen inventory (= new faculty, C1); and the `⊕` operator (foundation/3:266) is itself never constructed.
   - Leah's **dish reframe** (self-directed = the dish aimed by its own motor, pointing at outside signal; the split is by DRIVER not target) correctly dissolved the target-based over-generation and the apparent foundation↔application "tension" (agency:307 = aimable directions; foundation/3:270 = the motor) — but a driver-predicate still died on decidability: the driver is not a property of the static allocation.
   - Leah's **velocity reframe** (the driver is a dynamical property of the trajectory, not the still) decides the CLEAN INTERIORS but does NOT close the lemma. Three clean kills (adversarial re-test): (a) **point-vs-set** — a trajectory yields ONE realized driver, never the counterfactual SET fraktur-F quantifies over; differentiating position doesn't manufacture modality; (b) the `⊕` at foundation/3:264 is a *developmental state-blend* ("weighted manner", ontogenetic), NOT an invertible drive-split; (c) **osmotic co-constitution** — "the motor is made of integrated wind" (osmotic activation is exogenous-in-origin/endogenous-in-presentation, foundation/3:466/470/476; the lived-I motor is built by imprinting from not-I), so the driver-split is intrinsically fuzzy in the developmentally-central regime, even third-person.
   - **The only thing that would discharge Im(π)=fraktur-F is a new named transition-classifier Θ(focus-shift, exogenous-antecedent)→{contact, self} — exactly the new faculty (C1) the scrutiny says to avoid.** So: choice-as-filter stays application-tier, §24.1 stays open, frozen v5.3.3 stays UNTOUCHED. **Genuine payouts (not promotable, but true):** the clean-interior/co-constituted-middle structure of the self/contact split (situated agency: the self that aims was built by the world), and the ontic grounding of "the agent can only model its driver" (§1.3).

## 7. Open work (priority order)

1. **Define V as a functional — DONE (§1.1):** V = T · ‖f − b‖_ρ (ρ-weighted differential magnitude × temperature gain); the direction of Δ selects A/C. Remaining: pin the profile-metric ‖·‖_ρ precisely and connect to math-program Round 2.
2. **Operationalize slack — DONE in form (§4.1):** S = M − Pressure; sign-flip at S=0; two independent handles (§5.1). **THE PAPER = run the dissociation experiment** (self-reported felt-choice vs behavioral change across S=0). Highest-value open item.
3. The **cross-domain infant dwell-ceiling** test (section 3) — the proto-word discriminator. UNRUN.
4. **Formalize the driven/allostatic orbit — DONE (§1.2):** db/dt = γΔ; non-autonomous dV/dt = ∂V/∂t − ‖grad V‖². Remaining: V's oscillation amplitude as the temperature readout.
5. **Onset hinge / errata — the SNR draft SMUGGLES** (asserts the reflexive operator is running at t=0 — a model-tier claim in the frozen core) and is under-scoped (5 other "zero at origin" loci). The clean route is the **gauge reading** (§1.3): declare the sub-floor absolute a non-question, commit only to observable onset — a minimal errata, OR no frozen edit at all (lean: no edit; keep the operator/state SNR reading at model tier). Foundation UNTOUCHED pending Leah.
6. **Temperature vs slack — ANSWERED: two independent knobs** (slack further splits perceived vs actual); see section 5.1. Remaining: formalize their joint action on the filter.
7. **choice-as-filter Im(π)=fraktur-F — UNDISCHARGED, CLOSED as DO-NOT-promote** (§6.2). Would need a new faculty (a transition-classifier Θ); foundation UNTOUCHED. Payouts folded into §1.3 + §6.2.
8. **Reflexive relativity (§1.3) — NEW model-tier principle** (inside view reads only differentials; absolutes are gauge or self-modeled). Remaining: formalize the clean-interior/co-constituted-middle boundary of the driver-split; connect the self-model's ontic role to perceived/actual slack.

## 8. Epistemic status ledger

- **Grounded / STRONG:** differential-baseline coding; V-as-felt exceeding FEP; V=0-unreachable as NESS.
- **PARTIAL:** steady-state re-zeroing (set-points displaceable).
- **Conjectured:** the full dynamical unification; A/C as signed vector updates; PCE-sets-baseline / PtCns-picks-branch; driven-orbit resonance.
- **Redescription (per adversary):** the model's affect/agency dynamics vs active inference + reference-dependence + emotion-regulation.
- **UNVERIFIED / untestable-as-stated:** slack-gated agency (needs slack operationalized); the proto-word discriminator (unrun); temperature-as-literal.
- **Foundation:** UNCHANGED (v5.3.3 frozen). Two gated candidate touches (section 6).

## References (author/year; grounded 2026-09-12)

Schultz (reward prediction error); Helson (adaptation-level theory, 1964); Kahneman and Tversky (prospect theory, 1979); Diener, Lucas and Scollon (hedonic-adaptation re-examination); Berridge (liking vs wanting); Seth and Critchley (interoceptive inference); Barrett (theory of constructed emotion); Friston (FEP, 2010/2019); Bruineberg, Dolega, Dewhurst, Baltieri (The Emperor's New Markov Blankets); Aguilera, Millidge, Tschantz, Buckley (sparse coupling and Markov blankets); Joffily and Coricelli (emotional valence and the free-energy principle, 2013); Gross (process model of emotion regulation); Daw, Niv, Dayan (model-based vs model-free); Shenhav, Botvinick, Cohen (Expected Value of Control); Dore (primitive speech acts, 1974); Greenfield and Smith (1976); Bloom (One Word at a Time, 1973); Lewis and Ramsay (2004); Sterling and Eyer / Sterling (allostasis); Schrodinger (What is Life?); Prigogine (dissipative structures); Kelso/Tognoli, Rabinovich (metastability); Fichte (Wissenschaftslehre, the I / not-I).
