# Local Claude Bootstrap Prompt

Use this after checking out a clean local copy of `femboy2112/TLICA.git` with network access to the repository.

```text
You are taking over integration work in femboy2112/TLICA.git.

Mission:
Fully internalize the research-tier dossier on branch
`research/developmental-substrate-nonstationarity-2026-09-15`
into current main, preserving TLICA's epistemic-status discipline and without smuggling in a new coordinate, primitive, or unsupported neuroscience mechanism.

The load-bearing authorial observation is:

- phenomenologically, childhood/adolescence/young adulthood felt different from adulthood because the substrate itself was still undergoing substantial development;
- during those years affect often behaved like a persistent baseline/background pull coupled to reality, surviving changes of explicit cognitive frame;
- after a depression/suppression/recovery arc, present adult affect is still strong but is predominantly context-resolved rather than constantly ambient;
- the original intuition "constant new neurons -> untrained substrate -> noise" is NOT to be preserved literally. Replace it with the stronger and more defensible mechanism: developmental substrate nonstationarity / neural reorganization (synaptic remodeling/pruning, myelination and connectivity change, endocrine and affective-control development, etc.).

Core TLICA synthesis:

A developing I is not merely learning how to operate an unfamiliar machine. It is learning how to operate a machine whose transfer function is itself changing while learning occurs.

Preserve Root II as high affective gain. The new refinement is regime-dependent expression:

    high gain × high developmental substrate nonstationarity × young/low-bandwidth self-regulation

can yield a different phenomenology from

    high gain × lower relative substrate drift × mature accumulated self-regulation.

Same Root II, different dynamical regime.

The preferred current synthesis is coupled but UNVERIFIED:

- ordinary developmental stabilization may reduce endogenous substrate drift relative to tracking capacity;
- accumulated Mode-B/self-directed control improves tracking;
- the depression/suppression/recovery arc may have substantially retrained regulation;
- environment/autonomy and retrospective reconstruction remain live rivals.

Do not rewrite this as "maturation fixed it."

Required workflow:

1. Establish repo truth first:
   - fetch all refs;
   - inspect current main HEAD, changelog, foundation version, and validation instructions;
   - run baseline `make validate` before editing;
   - inspect current canonical Self-Applied Architecture files and determine which are source-of-truth versus retained working versions.

2. Read the entire dossier from the research branch:
   - `research/developmental_substrate_nonstationarity_2026-09-15/README.md`
   - `MANUSCRIPT_SEED.md`
   - `CLAIM_LEDGER_AND_PROBES.md`
   - `SOURCES.md`
   - `MAINLINE_INTEGRATION_HANDOFF.md`

3. Reconcile the version seam explicitly:
   - current foundation main is v5.5.0 and contains the slow lived-I structure G / Mode-B actuator repair;
   - the Self-Applied Architecture still declares an older v5.3.3 frozen base;
   - do NOT cosmetically bump the application's base version;
   - either keep the application v5.3.3-bounded and express the refinement conservatively, port it only after a dependency audit, or use a split-layer integration where the application stays historically honest and a current-foundation note explains how v5.5.0 G sharpens the mechanism.
   - Prefer the split-layer route unless the audit gives a strong reason otherwise.

4. Integrate the smallest sufficient mainline change:
   - add a durable subsection to the canonical Self-Applied Architecture near Root II / affect-axis material, tentatively titled `Developmental substrate nonstationarity: the moving-machine problem`;
   - preserve the first-person phenomenological datum;
   - correct the biological mechanism;
   - explicitly distinguish root from developmental regime;
   - connect the effect to third-order affect/source-opacity and the existing return-address/affective-epistemics machinery;
   - define adulthood as relative stabilization/tracking improvement, not a static endpoint;
   - preserve the depression/recovery confound and rival models;
   - include claim-status language.

5. Mirror the polished result into the wiki companion (`docs/app-self-applied-architecture.md`).

6. Consider, but do not assume, one small explanatory note in `docs/substrate-focus-and-imprinting.md` and/or `docs/the-self-in-motion.md` saying that developmental applications may treat the effective biological realization of the substrate as nonstationary. This must remain application-level unless a separate foundation audit demonstrates a real formal omission.

7. Formal discipline:
   - canonical TLICA coordinates remain κ, φ, ρ;
   - `eta_dev = tau_track/tau_S`, if retained, is an application-level UNVERIFIED diagnostic only;
   - do not turn source-map adequacy, developmental stage, mediation depth, fuzziness, or tracking load into new coordinates;
   - do not silently alter the v5.5.0 field-reading function signature. If you write `f_t ~ F(G_t,A_t;S_eff(t))`, the semicolon means "implemented/mediated through" and is explanatory notation only unless a separate formal audit earns a foundation change.

8. Neuroscience discipline:
   - independently verify the sources in `SOURCES.md` and add/update primary recent sources as needed;
   - preserve proxy language for MRI/myelin/connectivity measures;
   - do not claim the population literature proves Leah's autobiographical mechanism;
   - do not say adolescent development is large-scale continual addition of blank cortical neurons;
   - include at least one hostile/heterogeneity source so the literature section cannot collapse into a monotone maturation story.

9. Hostile audit before merge:
   A. maturation-fairy-tale attack;
   B. neuroscience-reduction attack;
   C. over-coherence attack against environment / learned-regulation / memory-reconstruction rivals;
   D. coordinate-smuggling / dependency audit.
   Fold valid findings instead of defending the preferred frame.

10. Preserve the dossier as provenance and register it in `research/README.md`.

11. Update changelog for curated changes.

12. Run all validation/render checks required by the repo, at minimum `make validate`.

Acceptance criteria:

- authorial phenomenology remains recognizable;
- wrong neurogenesis centerpiece is removed;
- Root II survives, regime-qualified;
- moving-machine mechanism uses existing TLICA dependencies;
- v5.3.3/v5.5.0 seam is explicit;
- depression/recovery remains a live co-cause/rival;
- affective signal truth/intensity is separate from source-map adequacy;
- neuroscience is fresh, sourced, and bounded;
- OBSERVED/CORROBORATED/CONJECTURED/UNVERIFIED/DARK statuses remain honest;
- no new coordinate is smuggled in;
- validation passes.

Do the work now. Do not just propose a plan. Make and commit the integration on a non-main working branch first, inspect the diff and validation results, then merge/fast-forward to main only if the audit passes and the repo's normal authorization/workflow permits it. Report exact commits, files changed, tests/validation, unresolved debts, and any claims you demoted or rejected during hostile review.
```
