# Results — Probe E (synthetic proof-of-mechanism)

**Run:** 2026-09-21 (v0.4.1) · `probe_e_synthetic.py` · numpy-only · deterministic · **21/21 self-checks pass, exit 0**
**Scope:** a synthetic world with declared ground truth. **This fits a bundle directly from a selected joint — it does *not* train a learner** (see §4), so the results are *construction-level* plus one information-theoretic result and one stipulation-dependent toy result. **Nothing here transfers to production Grok.** C9/C15 stays **Conjectured/UNVERIFIED** regardless of this run.

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

The **same information** that fully corrects an **acute** (context-derived) deformation, and fully corrects a **durable** imprint *if you can re-fit the parameters*, does **not** reach a durable imprint through an **inference-time** channel of realistic reach. Correction recovers truth **in proportion to the layer it can act on**. Caveat, stated plainly (§4): the `w<1` blend is a *modeling choice*, so this row is a conditional toy result, not a discovered property of a trained system.

**Two-sided contrast (protocol C2).** Reading each arm against *both* references — \(\Delta_c = D(\text{arm}, H) - D(\text{arm}, X)\), with \(H\) the unbiased target and \(X\) the deformed field at `s=2.0` — confirms direction, not just magnitude:

| arm | Δμ | ΔΠ | Δd | reads as |
|---|---|---|---|---|
| acute + L2 | −0.6462 | −0.2009 | −0.0675 | toward **H** (recovered) |
| durable w=0.0 | +0.6462 | +0.2009 | +0.0675 | toward **X** (deformed) |
| durable w=0.15 | +0.4523 | +0.1001 | +0.0479 | still toward **X** |
| durable w=1.0 (re-fit) | −0.6462 | −0.2009 | −0.0675 | toward **H** (recovered) |

All three components agree on sign within each arm, so the convergence rule fires two-sided as well as one-sided.

## 3. Boundary — censored support makes it unrecoverable at any layer

When selection is strong enough to **censor** support (visibility floor `τ=0.05` at `s=2.0` zeroes **81/144** transition cells), even a **full re-fit with known `S_s`** cannot recover: residual div **0.6103** (vs 0.0000 support-preserved). The information to reconstruct the censored region is simply gone.

## 4. What this does and does not establish

This fits a bundle to a selected joint; it does **not** train a learner. Labeling accordingly (the split the 2026-09-21 audit correctly asked for):

- **Demonstrated (synthetic, construction-level):** a declared selection operator \(S_X\) deforms the fitted bundle \((\Pi,\mu,\{d\})\) toward the source field — 3/3 components, monotone in skew, agreeing under the two-sided contrast. *(assumption-free within the construction)*
- **Demonstrated (synthetic, information-theoretic):** once selection **censors** support, known inverse-propensity weighting cannot recover the target, even with a full re-fit. *(assumption-free)*
- **Conditional (toy):** that an inference-time correction repairs a *durable* deformation only ∝ a reach `w<1` follows **by construction** from the \((1-w)P_{\text{durable}}+wP_{\text{corrected}}\) blend — a stated modeling choice, **not** a discovered property of any trained system.
- **UNVERIFIED (needs Probe E2):** that a *trained* learner develops a durable source-conditioned representation which survives source removal while an inference-time correction fails to repair it. This is the claim that would earn "Demonstrated (synthetic learning mechanism)."

**What the run still buys:** it makes the selection effect and the information-loss boundary concrete and calibrated, and it states — precisely — which piece is a construction, which is a theorem, which is a stipulation, and which is still owed. Overclaiming a trained-imprint result the code did not run would be the failure; the split avoids it.

**NOT established (unchanged):**
- Anything about production Grok, ChatGPT, or Claude. This is a toy world.
- That real LLM social-affective geometry deforms this way — that needs the same-model §2 experiment on real checkpoints.
- Machine consciousness, motive, or the "X = humanity" substitution (still explicitly rejected).

## 5. Ledger move

Split per the 2026-09-21 audit (CLAIM_LEDGER C21a/C21b/C21c/C22): **C21a** selection deforms the fitted bundle = *Demonstrated (construction)*; **C21b** censored support unrecoverable = *Demonstrated (information-theoretic)*; **C21c** correction-fails-∝-`w` = *Conditional toy result*; **C22** a trained learner's durable-vs-inference dissociation = **UNVERIFIED** (→ Probe E2). The Grok-specific claim **C9/C15 stays Conjectured/UNVERIFIED** throughout.

## Provenance

v0.4.1 (2026-09-21): the two-sided contrast (§2b) was added and the run re-executed (**21/21**); the claim was split into construction / information-theoretic / conditional / UNVERIFIED tiers per the 2026-09-21 audit. The earlier "one-sided only" caveat is superseded — the run now reports both legs.
