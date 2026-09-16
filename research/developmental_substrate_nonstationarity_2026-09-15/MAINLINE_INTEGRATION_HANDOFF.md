# Mainline Integration Handoff
## Developmental Substrate Nonstationarity

**Target integrator:** local Claude Code session working in `femboy2112/TLICA.git`.  
**Source branch:** `research/developmental-substrate-nonstationarity-2026-09-15`.  
**Do not merge mechanically. Reconcile against current `main`.**

---

## 0. Mission

Internalize the research dossier's load-bearing distinction into TLICA's mainline presentation of development and the Self-Applied Architecture:

> the developing I is not only accumulating lived structure and learning regulation; it is doing so through a substrate whose effective response-properties are themselves changing. The result is a moving-machine / moving-plant problem.

The integration must preserve three boundaries:

1. **phenomenology is the primary autobiographical datum;**
2. **developmental neuroscience constrains plausible mechanisms but does not prove the autobiography;**
3. **no new TLICA coordinate or causal primitive is introduced unless a separate foundation audit independently earns it.**

---

## 1. Start from repository truth, not this handoff's assumptions

Before editing:

```bash
git fetch --all --prune
git switch main
git pull --ff-only
git status --short
git log -n 12 --oneline
```

Then inspect:

- `foundation/3_formal_apparatus.md` Sections 8.1-8.11, especially v5.5.0 `G`;
- `foundation/2_access_and_development.md` developmental commitments;
- `docs/substrate-focus-and-imprinting.md`;
- `docs/modes-of-development.md`;
- `docs/the-self-in-motion.md`;
- `applications/self_applied_architecture_prose_draft_v0_1.md`;
- `applications/self_applied_architecture_v0_8.md`;
- `docs/app-self-applied-architecture.md`;
- `research/developmental_substrate_nonstationarity_2026-09-15/*` from the source branch.

Determine which Self-Applied file is currently canonical/curated. Do not assume the working-document numbering alone decides it.

---

## 2. Reconcile the version seam first

The research dossier reasons against current mainline v5.5.0 dynamics, especially the slow lived-I structure `G`.

The Self-Applied Architecture still declares an older frozen foundation base (v5.3.3) in its prose/working files.

This is a real seam. Resolve it explicitly before prose integration.

### Acceptable integration routes

**Route A — application remains v5.3.3-bounded.**  
Express developmental substrate nonstationarity using only dependencies already available in v5.3.3, and keep all v5.5.0 `G` material as a later cross-reference/research note.

**Route B — port Self-Applied Architecture to current v5.5.0.**  
Only do this after a full dependency audit of every existing application claim touched by the port. Do not change the version marker as a cosmetic update.

**Route C — split-layer integration (preferred unless audit strongly favors B).**  
Keep the Self-Applied paper's historical base honest, add an application-level developmental refinement phrased in substrate/focus/imprinting terms compatible with that base, and add a clearly labeled current-foundation note showing that v5.5.0 `G` sharpens the same mechanism.

Whichever route is chosen, document the choice in the changelog or application provenance.

---

## 3. The exact conceptual change to integrate

### Preserve Root II

Do **not** replace Root II's high-gain affective parameter.

Instead, distinguish **root** from **regime**:

- Root II = high affective gain;
- developmental regime = gain operating while substrate response-properties are comparatively nonstationary and self-directed regulation is still accumulating;
- adult regime = gain operating after relative substrate drift has slowed and/or tracking/regulatory capacity has improved.

The key sentence to earn is:

> Same Root II, different dynamical regime.

### Preserve the depression/recovery confound

Do not rewrite the developmental story as "maturation fixed it."

Keep at least these live rivals visible:

- high-gain-only;
- developmental substrate nonstationarity;
- acquired regulation through depression/suppression/recovery;
- environmental/autonomy change;
- retrospective reconstruction artifact;
- coupled model.

The coupled model may be the best current synthesis, but must remain **CONJECTURED** until the proposed probes run.

### Preserve source-map language

The useful TLICA bridge is not "young people feel irrationally."

It is:

> a real affective signal can have an incomplete or misassigned return-address when a meaningful part of its provenance lies in changing endogenous substrate state.

This belongs naturally beside the application's affective-epistemics / return-address machinery.

---

## 4. Formal integration discipline

### Allowed application notation

A time-indexed effective substrate state may be written schematically as

```text
S_eff,m(t) := Eval_t(S_m)
```

or equivalent notation.

This is an **application-level view of the existing substrate**, not a fourth coordinate.

A developmental tracking-load diagnostic may be written

```text
eta_dev(t) = tau_track(t) / tau_S(t)
```

where the timescales are not defined until an empirical application supplies measurements.

This quantity must be labeled:

- application-level;
- UNVERIFIED;
- not a truth score;
- not a new TLICA coordinate;
- not valid for numerical use without an operationalization.

### Be careful with `F`

The research manuscript sometimes displays

```text
f_t ~ F(G_t, A_t ; S_eff(t))
```

only to expose substrate mediation.

Current v5.5.0 foundation writes the field-reading as a reading of `G` and available contents, with substrate mediation described elsewhere. Do **not** silently change the foundation function signature to add `S` as an independent argument. If you believe that change is mathematically necessary, stop and perform a separate foundation-level dependency audit.

### No coordinate leak

The canonical coordinates remain:

- κ/contact;
- φ/toolkit-relative truth/source indistinguishability;
- ρ/identity-correlation.

`eta_dev`, mediation depth, fuzziness, developmental stage, regulation skill, and source-map adequacy are diagnostics/typological/application variables, not new coordinates.

---

## 5. Candidate mainline edits

After reconciliation, make the smallest set of edits that fully internalizes the idea.

### A. Self-Applied Architecture

Add a subsection near Root II / affect-axis material, tentatively titled:

**Developmental substrate nonstationarity: the moving-machine problem**

It should contain:

1. the first-person phenomenological distinction: developmental baseline buzz vs adult context-resolution;
2. the biological correction: reorganization/maturation, not "new blank neurons";
3. the Root-II regime interaction;
4. source-opacity / return-address mechanism;
5. adulthood as relative stabilization, not endpoint;
6. depression/recovery as causal confound;
7. an explicit status paragraph: OBSERVED vs CORROBORATED vs CONJECTURED vs UNVERIFIED.

### B. Wiki companion

Mirror the result in `docs/app-self-applied-architecture.md` in plain language.

Avoid stronger claims in the wiki than in the paper.

### C. Development/substrate docs

Only if the audit shows a real explanatory omission, add a short non-foundation explanatory note to one or both of:

- `docs/substrate-focus-and-imprinting.md`;
- `docs/the-self-in-motion.md`.

Candidate note:

> During development, "substrate" need not be treated as an effectively fixed machine. Its biological realization changes over time, so self-regulation can face a moving-target identification problem. This is an application-level developmental refinement, not an additional coordinate or a claim that adulthood becomes static.

Do **not** edit the frozen foundation merely because this note is intuitive.

### D. Research index

Register this dossier in `research/README.md` with its current epistemic status.

### E. Changelog

If any curated application or docs page changes, record what was added and what remained explicitly unverified.

---

## 6. Neuroscience source discipline

Use `SOURCES.md` as the seed, then verify the sources yourself before mainline prose.

Required source classes:

- recent developmental-plasticity review;
- primary longitudinal white-matter/myelin or connectivity study;
- primary longitudinal affect-variability study;
- primary longitudinal emotion-regulation study;
- source establishing why large-scale blank-neuron addition is the wrong general mechanism;
- hostile/heterogeneity source showing non-monotone affect development.

In prose, prefer:

> "consistent with ongoing developmental reorganization"

not:

> "neuroscience proves the substrate-noise mechanism."

Do not collapse MRI proxies into literal cellular mechanisms.

---

## 7. Hostile audit required before merge

Run at least four attacks.

### Attack 1 — Maturation fairy tale

Try to refute the idea that "adulthood stabilized the substrate and therefore solved emotion."

The final text must survive by keeping adulthood relative, plastic, and contingent.

### Attack 2 — Neuroscience reduction

Try to show that the application reduces first-person affect to brain development.

The final text must survive by keeping phenomenology primary and biology a candidate implementation/constraint.

### Attack 3 — Over-coherence

Try to explain the entire result using regulation learning, environment, or retrospective memory without developmental substrate drift.

If one rival wins, demote the developmental mechanism accordingly.

### Attack 4 — Coordinate smuggling

Search every new symbol/term and verify it has not been silently elevated to a new foundation coordinate, primitive, or truth score.

---

## 8. Validation

At minimum:

```bash
make validate
```

Also search for term drift:

```bash
grep -RniE 'new neurons|neurogenesis|nonstationar|moving.machine|moving.plant|eta_dev|baseline buzz|context.resolv' \
  applications docs foundation research
```

Check that:

- no file says development is simply "new neurons adding noise";
- no file says adult brains stop changing;
- no file claims population neuroscience validates Leah's individual trajectory;
- no file treats the coupled explanation as disclosed;
- no old Self-Applied claim is silently invalidated by a version-port.

If the repository has PDF/render gates for the application, run them too.

---

## 9. Integration acceptance criteria

Mainline integration is complete only when:

1. the developmental phenomenology is preserved clearly enough that the original author recognizes it;
2. the wrong neurogenesis centerpiece is gone;
3. Root II is preserved and regime-qualified rather than replaced;
4. the moving-machine mechanism is expressible entirely within typed TLICA dependencies;
5. the v5.3.3/v5.5.0 application seam is handled explicitly;
6. the depression/recovery confound remains live;
7. source-map adequacy is separated from affective truth/intensity;
8. the neuroscience claims are sourced and bounded;
9. claim statuses remain visible;
10. hostile audit and `make validate` pass;
11. the research dossier remains as provenance even if the polished prose is promoted elsewhere.

---

## 10. Recommended commit structure

Prefer multiple auditable commits rather than one giant rewrite:

1. `research: reconcile developmental substrate dossier with current main`
2. `docs(self-applied): add developmental substrate nonstationarity regime`
3. `docs(wiki): surface moving-machine developmental refinement`
4. `docs: register sources/status + changelog`
5. optional, only if independently justified: `foundation: ...` after a separate foundation audit

Do not force a foundation version bump merely to make the application feel complete.
