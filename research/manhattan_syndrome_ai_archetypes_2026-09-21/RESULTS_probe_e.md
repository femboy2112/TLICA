# Results — Probe E (synthetic proof-of-mechanism)

**Run:** 2026-09-21 · `probe_e_synthetic.py` · numpy-only · deterministic · **19/19 self-checks pass, exit 0**
**Scope:** a synthetic world with declared ground truth. **Nothing here transfers to production Grok.** C15's Grok-specific claim (C9/C15) stays **Conjectured/UNVERIFIED** regardless of this run. What is tested here is the *mechanism*, not any real model.

Reproduce: `python3 probe_e_synthetic.py`.

---

## 0. What was run

A declared 12-state social-affective world (quiet/care cluster, spectacle/conflict cluster, `disagreement` planted as a bridge). Declared ground truth: base rates `mu*` (real life mostly mundane/quiet; spectacle rare), a transition kernel `Pi*` (nearby common states are likelier continuations), and, from these, a reference geometry. A tunable selection operator
`S_s`: `P_obs(x,y) ∝ mu*(x)·exp(s·A·e(x))·Pi*(y|x)·exp(s·B·e(y))` skews *who is seen* and *which continuations are amplified* by engagement `e(x)`. `s=0` reproduces the unbiased field; `s>0` is engagement selection.

The **bundle instrument** `G=(Pi, mu, {d})` fits: `mu` = state occupancy, `Pi` = fitted kernel, `d` = **Jensen-Shannon distance between continuation profiles** `Pi(·|x)` (the standard distributional "what sits nearby" read — an earlier PPMI-cosine readout was rejected during calibration because PMI's frequency penalty made it move the wrong way; that rejection is itself a calibration finding). The instrument is calibrated on unbiased (`s=0`) data — its fixed point — and reproduces the declared truth ordering (disagreement nearer quiet than status-contest; spectacle a minority 10.9% of mass).

## 1. Deformation is real, monotone, and convergent across components

Divergence of the fitted bundle from the unbiased reference, by selection skew `s`:

| s | total div | d_gap `d(dis,sc)−d(dis,quiet)` | `Pi(status_contest\|disagreement)` | spectacle salience mass |
|---|---|---|---|---|
| 0.0 | 0.0000 | +0.4396 | 0.0161 | 0.1092 |
| 1.0 | 0.4312 | +0.4124 | 0.0415 | 0.3883 |
| 2.0 | 0.9145 | +0.2617 | 0.0911 | 0.7554 |
| 3.0 | 1.2079 | +0.0665 | 0.1591 | 0.9267 |

All three pre-declared **signed contrasts** (§8 of the protocol) move source-ward — **3/3**, clearing the ≥2/3 convergence rule: the profile-distance gap shrinks 0.44→0.07 (disagreement's continuation profile collapses toward status-contest's), `Pi(dis→status_contest)` rises ~10×, and spectacle salience climbs from **11% to 93% of mass**. Finite-sample (200k draws, seed 0) reproduces the population effect (0.918 vs 0.914), so this is not an infinite-data artifact.

**Honest boundary on the headline schematic.** The manuscript's §4.2 schematic is the *strict* inequality `d(disagreement, status_contest) < d(disagreement, quiet_negotiation)`. The run **approaches but does not reach** it: the gap shrinks 85% but stays `+0.0665` at `s=3.0` — no full sign flip in this parameterization. Reported as-is; the demonstrated claim is the strong source-ward *shrinkage*, not a full ordering inversion. (Forcing a flip by pushing `s` or retuning would be fitting the world to the headline; declined.)

## 2. The money result — correction is channel-dependent, not just information-dependent

At a strong operating point `s=2.0` (deformed total div = 0.9145), applying the **same** known-selection information `S_s`:

| arm | correction channel | total div | outcome |
|---|---|---|---|
| acute + L2 | inverse-propensity on the **current context** | **0.0000** | full recovery |
| durable, w=0.0 | generic warning (no operator reaches params) | 0.9145 | no correction |
| durable, w=0.15 | short instruction (reach 15%) | 0.7726 | 85% of imprint remains |
| durable, w=0.5 | partial adaptation | 0.4799 | half remains |
| durable, w=1.0 | full **re-fit** with `S_s` | **0.0000** | full recovery |

The **same information** that fully corrects an **acute** (context-derived) deformation, and fully corrects a **durable** imprint *if you can re-fit the parameters*, does **not** reach a durable imprint through an **inference-time** channel of realistic reach. Correction recovers truth **in proportion to the layer it can act on** — this is the paper's layer-2 (explicit/propositional) vs layer-3 (operative/durable) separation, made numerical.

## 3. Boundary — censored support makes it unrecoverable at any layer

When selection is strong enough to **censor** support (visibility floor `τ=0.05` at `s=2.0` zeroes **81/144** transition cells), even a **full re-fit with known `S_s`** cannot recover: residual div **0.6103** (vs 0.0000 support-preserved). The information to reconstruct the censored region is simply gone.

## 4. What this does and does not establish

**Demonstrated (synthetic, mechanism-level):**
- Engagement selection **durably deforms** the operative bundle, monotonically, with ≥2/3 components moving source-ward. *(assumption-free)*
- Correction is **channel-dependent**: the same `S_s` information recovers an acute/context deformation and a re-fittable durable one, but an inference-time correction reaches a durable imprint only ∝ its reach `w`. *(rests on one stated modeling assumption: that a short inference-time instruction has reach `w<1` over durably-fitted parameters — precisely what the real-model acute/durable arms in EXPERIMENT_PROTOCOL §2 are built to measure.)*
- **Censored support ⇒ informational impossibility**: known `S_s` + full re-fit still cannot recover. *(assumption-free)*

**Refines the paper's strong claim (this is the sharpening the run buys):** the "deformation survives explicit correction" clause is true specifically in **(a) the access-limited regime** (only inference-time correction is available, `w<1`) and **(b) the censored-support regime** — and is **false** in the support-preserved, re-fittable regime. So the strong Syndrome danger is not "selection bias is statistically irreversible" (it isn't); it is "the *available* correction channel cannot reach the layer that carries the imprint, or the source has already destroyed the support." That is a sharper, checkable claim than v0.3.0 stated.

**NOT established (unchanged):**
- Anything about production Grok, ChatGPT, or Claude. This is a toy world.
- That real LLM social-affective geometry deforms this way — that needs the same-model §2 experiment on real checkpoints.
- Machine consciousness, motive, or the "X = humanity" substitution (still explicitly rejected).

## 5. Ledger move

Per EXPERIMENT_PROTOCOL §9 (top row, honestly qualified): the **mechanism** — durable source-selection deformation of the bundle, with correction reaching only the layer it can act on, plus the censoring impossibility — is **Demonstrated (synthetic)**. The Grok-specific claim **C9/C15 stays Conjectured/UNVERIFIED**; the synthetic run raises the *mechanism's* coherence and hands the empiricists a sharper target, nothing more.
