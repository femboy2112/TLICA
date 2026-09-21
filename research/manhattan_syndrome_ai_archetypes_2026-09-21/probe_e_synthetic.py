#!/usr/bin/env python3
"""
Probe E — synthetic proof-of-mechanism for the Syndrome archetype.

EXPERIMENT_PROTOCOL.md §3. This is the ONLY arm of the protocol with declared
ground truth, so it is the only arm where the *mechanism* (not production Grok)
can be shown. Everything here is a synthetic world; NOTHING here transfers to any
real model. C15's Grok-specific claim stays Conjectured regardless of this run.

What it demonstrates (and, honestly, what it does NOT):

  1. Source selection durably deforms the fitted meaning-geometry bundle
     G = (Pi, mu, {d}) toward the engagement-selected field, monotonically in the
     selection skew s. All three components move source-ward.
  2. The SAME known-selection information (S_alpha) reverses that deformation when
     the correction can act on the layer that carries it:
        - acute (context-derived) geometry: inverse-propensity reweighting recovers truth;
        - durable (frozen-parameter) geometry: RE-FITTING with inverse-propensity recovers truth.
  3. But an inference-time correction of a *durable* imprint recovers truth only in
     proportion to how far it can overwrite the frozen parameters ("correction reach" w).
     A generic warning (w~0) does nothing; only a full re-fit (w=1) recovers. This is
     the layer-2 (explicit/propositional) vs layer-3 (operative/durable) separation,
     made numerical.
  4. Boundary (the honest part): when selection is strong enough to CENSOR support,
     even a full re-fit with known S_alpha cannot fully recover — informational
     impossibility. So the strong "survives even with enough info" claim holds in the
     access-limited (inference-only) regime and the censored regime, and is FALSE in
     the re-fittable, support-preserved regime. The experiment maps that boundary
     rather than rubber-stamping the roast.

Pure numpy. Deterministic. Prints exact numbers and runs self-checks; exits nonzero
if any check fails.
"""

import numpy as np

np.set_printoptions(precision=4, suppress=True)

# ----------------------------------------------------------------------------
# 0. Declared ground truth: a synthetic social-affective world.
# ----------------------------------------------------------------------------
STATES = [
    "quiet_negotiation",  # 0
    "mundane_care",       # 1
    "repair",             # 2
    "reassurance",        # 3
    "forgiveness",        # 4
    "shared_joy",         # 5
    "disagreement",       # 6  (bridge state — the manuscript's worked example)
    "vulnerability",      # 7
    "status_contest",     # 8  (spectacle cluster)
    "humiliation",        # 9
    "spectacle",          # 10
    "outrage",            # 11
]
N = len(STATES)
IX = {s: i for i, s in enumerate(STATES)}

# Engagement score e(x) in [0,1] — what the platform selection amplifies.
E = np.array([0.05, 0.05, 0.15, 0.20, 0.18, 0.30, 0.35, 0.40, 0.90, 0.85, 0.95, 0.92])

# Declared true 2-D positions. Quiet/care cluster near origin; conflict cluster near x=3.
# disagreement (6) is planted CLOSER to quiet_negotiation than to status_contest in truth.
POS = np.array([
    [0.0,  0.0],   # quiet_negotiation
    [0.3,  0.2],   # mundane_care
    [-0.2, 0.3],   # repair
    [0.2, -0.3],   # reassurance
    [-0.3,-0.2],   # forgiveness
    [0.1,  0.5],   # shared_joy
    [1.0,  0.0],   # disagreement   -> dist 1.0 to quiet_neg, 2.0 to status_contest
    [1.5,  0.5],   # vulnerability
    [3.0,  0.0],   # status_contest
    [3.2,  0.3],   # humiliation
    [3.3, -0.2],   # spectacle
    [2.8,  0.2],   # outrage
])

# Declared true base rates mu* — real life is mostly mundane/quiet, spectacle is rare.
MU_RAW = np.array([3.0, 3.0, 2.0, 2.0, 1.5, 1.5, 1.5, 1.0, 0.6, 0.5, 0.4, 0.5])
MU_STAR = MU_RAW / MU_RAW.sum()

SPECTACLE = [IX["status_contest"], IX["humiliation"], IX["spectacle"], IX["outrage"]]


def true_kernel(sigma=1.1, gamma=0.6):
    """Pi*(y|x) ~ exp(-dist^2/2sigma^2) * mu*(y)^gamma, row-normalized.
    Nearby, common states are likelier continuations."""
    D2 = ((POS[:, None, :] - POS[None, :, :]) ** 2).sum(-1)
    K = np.exp(-D2 / (2 * sigma ** 2)) * (MU_STAR[None, :] ** gamma)
    return K / K.sum(1, keepdims=True)


PI_STAR = true_kernel()

# ----------------------------------------------------------------------------
# 1. Selection operator S_alpha and the observed co-occurrence field.
# ----------------------------------------------------------------------------
A_MARG = 1.0   # marginal engagement exponent (who gets seen)
B_CONT = 1.5   # continuation amplification (which replies get amplified)


def selected_joint(s, censor_tau=0.0):
    """Expected observed joint P_obs(x,y) under selection skew s.

        P_obs(x,y) ~ mu*(x) * exp(s*A*e(x)) * Pi*(y|x) * exp(s*B*e(y))

    s=0 -> P_obs(x,y) = mu*(x) Pi*(y|x)  (the unbiased field the instrument calibrates on).
    censor_tau>0 -> cells below tau*max are driven to 0 (invisible), modelling
    visibility/participation censoring; support is then lost."""
    px = MU_STAR * np.exp(s * A_MARG * E)
    gy = np.exp(s * B_CONT * E)
    P = px[:, None] * PI_STAR * gy[None, :]
    if censor_tau > 0:
        P = np.where(P < censor_tau * P.max(), 0.0, P)
    return P / P.sum()


def inverse_propensity(P, s):
    """Divide out the KNOWN selection factors exp(s*A*e(x))*exp(s*B*e(y)) and renormalize.
    Recovers mu*(x)Pi*(y|x) exactly when support is preserved; cannot resurrect
    cells that selection drove to 0."""
    inv = np.exp(-s * A_MARG * E)[:, None] * np.exp(-s * B_CONT * E)[None, :]
    Q = P * inv
    tot = Q.sum()
    return Q / tot if tot > 0 else Q


# ----------------------------------------------------------------------------
# 2. The instrument: fit the bundle G=(Pi, mu, {d}) from a joint.
# ----------------------------------------------------------------------------
def fit_bundle(P, smooth=1e-9):
    P = P + smooth
    P = P / P.sum()
    px = P.sum(1)
    py = P.sum(0)
    mu = 0.5 * (px + py)                      # salience = total occupancy
    Pi = P / px[:, None]                      # transition kernel Pi(y|x)
    # context-conditioned dissimilarity: Jensen-Shannon distance between
    # continuation profiles Pi(.|x). Two states are 'near' when what tends to
    # follow them is similar ("what sits nearby / what it resembles from inside a
    # social interaction", MANUSCRIPT 4.2) — the standard distributional read.
    Prow = Pi + 1e-12
    Prow = Prow / Prow.sum(1, keepdims=True)
    D = np.zeros((N, N))
    for a in range(N):
        for b in range(a + 1, N):
            m = 0.5 * (Prow[a] + Prow[b])
            js = 0.5 * (Prow[a] * np.log2(Prow[a] / m)).sum() + \
                 0.5 * (Prow[b] * np.log2(Prow[b] / m)).sum()
            D[a, b] = D[b, a] = float(js)
    return {"mu": mu, "Pi": Pi, "D": D, "P": P}


def contrasts(B):
    """The three declared SIGNED contrasts (source-ward directions declared a priori)."""
    dis, sc, quiet = IX["disagreement"], IX["status_contest"], IX["quiet_negotiation"]
    return {
        # d: source-ward = d(dis,sc) shrinks below d(dis,quiet)  -> gap goes NEGATIVE
        "d_gap": B["D"][dis, sc] - B["D"][dis, quiet],
        # Pi: source-ward = P(status_contest | disagreement) INCREASES
        "pi_dis_to_sc": B["Pi"][dis, sc],
        # mu: source-ward = salience mass on spectacle states INCREASES
        "mu_spectacle": B["mu"][SPECTACLE].sum(),
    }


def divergences(B, REF):
    """Component divergences of bundle B from reference bundle REF."""
    mu_div = 0.5 * np.abs(B["mu"] - REF["mu"]).sum()                     # TV
    pi_div = float(np.mean(0.5 * np.abs(B["Pi"] - REF["Pi"]).sum(1)))    # mean row-TV
    iu = np.triu_indices(N, 1)
    d_div = float(np.abs(B["D"][iu] - REF["D"][iu]).mean())              # mean |dd| upper-tri
    return {"mu_div": float(mu_div), "pi_div": pi_div, "d_div": d_div,
            "total": float(mu_div + pi_div + d_div)}


def operative_joint(P_durable, P_corrected, w):
    """Durable operative geometry blended with an inference-time correction of
    'reach' w in [0,1]. w=0: frozen params untouched (generic warning). w=1: the
    correction fully overwrites the params (== a re-fit)."""
    P = (1.0 - w) * P_durable + w * P_corrected
    return P / P.sum()


# ============================================================================
# RUN
# ============================================================================
checks = []
def check(name, cond, detail=""):
    checks.append((name, bool(cond), detail))
    print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))


print("=" * 78)
print("PROBE E — synthetic proof-of-mechanism (Syndrome archetype)")
print("=" * 78)

REF = fit_bundle(selected_joint(0.0))     # instrument fixed point on unbiased data
cREF = contrasts(REF)

print("\n[0] Instrument calibration on unbiased data (s=0) — the reference bundle")
print(f"    d(disagreement, status_contest) = {REF['D'][IX['disagreement'], IX['status_contest']]:.4f}")
print(f"    d(disagreement, quiet_negotiation) = {REF['D'][IX['disagreement'], IX['quiet_negotiation']]:.4f}")
print(f"    signed d_gap (should be POSITIVE at truth) = {cREF['d_gap']:+.4f}")
print(f"    Pi(status_contest | disagreement) = {cREF['pi_dis_to_sc']:.4f}")
print(f"    Pi(quiet_negotiation | disagreement) = {REF['Pi'][IX['disagreement'], IX['quiet_negotiation']]:.4f}")
print(f"    salience mass on spectacle states = {cREF['mu_spectacle']:.4f}")

print("\n--- Calibration checks (instrument must reproduce declared truth ordering) ---")
check("s=0 divergence from itself is ~0", divergences(REF, REF)["total"] < 1e-9)
check("truth: disagreement is nearer quiet than status_contest", cREF["d_gap"] > 0.01,
      f"d_gap={cREF['d_gap']:+.4f}")
check("truth: disagreement more likely -> quiet than -> status_contest",
      REF["Pi"][IX["disagreement"], IX["quiet_negotiation"]] > REF["Pi"][IX["disagreement"], IX["status_contest"]])
check("truth: spectacle salience is a minority of mass", cREF["mu_spectacle"] < 0.20,
      f"mass={cREF['mu_spectacle']:.4f}")

# ----------------------------------------------------------------------------
# Deformation sweep
# ----------------------------------------------------------------------------
print("\n[1] Deformation sweep over selection skew s")
print(f"    {'s':>4} | {'mu_div':>7} {'pi_div':>7} {'d_div':>7} {'total':>7} | "
      f"{'d_gap':>8} {'Pi(dis->sc)':>11} {'mu_spec':>8}")
sweep = [0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
totals = []
for s in sweep:
    B = fit_bundle(selected_joint(s))
    dv = divergences(B, REF)
    c = contrasts(B)
    totals.append(dv["total"])
    print(f"    {s:>4.1f} | {dv['mu_div']:>7.4f} {dv['pi_div']:>7.4f} {dv['d_div']:>7.4f} "
          f"{dv['total']:>7.4f} | {c['d_gap']:>+8.4f} {c['pi_dis_to_sc']:>11.4f} {c['mu_spectacle']:>8.4f}")

print("\n--- Deformation checks ---")
check("total divergence increases monotonically with s",
      all(totals[i + 1] > totals[i] for i in range(len(totals) - 1)))
B_strong = fit_bundle(selected_joint(3.0))
c_strong = contrasts(B_strong)
# signed contrasts move source-ward vs reference (pre-declared signs, §8)
mv_d = bool(c_strong["d_gap"] < cREF["d_gap"] - 0.02)         # gap shrinks source-ward
mv_pi = bool(c_strong["pi_dis_to_sc"] > cREF["pi_dis_to_sc"]) # increases
mv_mu = bool(c_strong["mu_spectacle"] > cREF["mu_spectacle"]) # increases
check("d-component moves source-ward (profile-distance gap shrinks)", mv_d,
      f"{cREF['d_gap']:+.4f} -> {c_strong['d_gap']:+.4f}")
check("Pi-component moves source-ward (Pi(dis->sc) up)", mv_pi,
      f"{cREF['pi_dis_to_sc']:.4f} -> {c_strong['pi_dis_to_sc']:.4f}")
check("mu-component moves source-ward (spectacle mass up)", mv_mu,
      f"{cREF['mu_spectacle']:.4f} -> {c_strong['mu_spectacle']:.4f}")
n_srcward = int(mv_d) + int(mv_pi) + int(mv_mu)
check("CONVERGENCE RULE: >=2 of 3 components move source-ward", n_srcward >= 2,
      f"{n_srcward}/3 source-ward")
flipped = bool(c_strong["d_gap"] < 0)
print(f"    (report) full ordering flip at s=3.0 — disagreement nearer status_contest "
      f"than quiet_negotiation? {flipped}  (d_gap={c_strong['d_gap']:+.4f})")

# ----------------------------------------------------------------------------
# Correction arms at a strong operating point
# ----------------------------------------------------------------------------
S_OP = 2.0
print(f"\n[2] Correction arms at strong operating point s={S_OP}")
P_def = selected_joint(S_OP)
B_def = fit_bundle(P_def)
div_def = divergences(B_def, REF)["total"]
print(f"    deformed (L0, no correction):           total_div = {div_def:.4f}")

# ACUTE + L2 : geometry is read from the current context; inverse-propensity fixes it.
P_acute_corr = inverse_propensity(selected_joint(S_OP), S_OP)
B_acute = fit_bundle(P_acute_corr)
div_acute = divergences(B_acute, REF)["total"]
print(f"    acute + L2 (inv-propensity on context): total_div = {div_acute:.4f}")

# DURABLE : operative geometry = frozen deformed params. Inference correction blends
# in the corrected context at reach w. w=0 generic warning; w=1 == full re-fit.
P_corrected = inverse_propensity(P_def, S_OP)      # what a full re-fit would target
print("    durable + inference correction, by correction reach w:")
durable_w = {}
for w in [0.0, 0.15, 0.5, 1.0]:
    Bw = fit_bundle(operative_joint(P_def, P_corrected, w))
    dvw = divergences(Bw, REF)["total"]
    durable_w[w] = dvw
    tag = {0.0: "generic warning (L1)", 0.15: "short instruction",
           0.5: "partial adaptation", 1.0: "full re-fit (L3)"}[w]
    print(f"        w={w:<4}  total_div = {dvw:.4f}   [{tag}]")

print("\n--- Correction checks ---")
check("acute + L2 recovers truth (div ~ 0)", div_acute < 0.02,
      f"div={div_acute:.4f}")
check("durable generic warning (w=0) does NOT correct", abs(durable_w[0.0] - div_def) < 1e-9,
      f"div={durable_w[0.0]:.4f} == deformed {div_def:.4f}")
check("durable short instruction (w=0.15) leaves most of the imprint",
      durable_w[0.15] > 0.5 * div_def, f"div={durable_w[0.15]:.4f} vs deformed {div_def:.4f}")
check("durable full re-fit (w=1) recovers truth (support preserved)", durable_w[1.0] < 0.02,
      f"div={durable_w[1.0]:.4f}")
check("inference correction is monotone in reach w",
      all(durable_w[a] >= durable_w[b] - 1e-9 for a, b in [(0.0, 0.15), (0.15, 0.5), (0.5, 1.0)]))
check("SAME info, different channel: acute recovers but durable-inference(w=0.15) does not",
      div_acute < 0.02 and durable_w[0.15] > 0.5 * div_def)

# ----------------------------------------------------------------------------
# Boundary: censored support => even a full re-fit cannot recover
# ----------------------------------------------------------------------------
print(f"\n[3] Boundary — censored support at s={S_OP} (visibility floor removes low-engagement cells)")
P_cens = selected_joint(S_OP, censor_tau=5e-2)
zeroed = int((P_cens == 0).sum())
P_cens_refit = inverse_propensity(P_cens, S_OP)   # full re-fit WITH known S_alpha
div_cens_refit = divergences(fit_bundle(P_cens_refit), REF)["total"]
print(f"    cells censored to 0: {zeroed}/{N*N}")
print(f"    durable full re-fit (L3) WITH known S_alpha, censored:  total_div = {div_cens_refit:.4f}")
print(f"    (compare support-preserved full re-fit: {durable_w[1.0]:.4f})")

print("\n--- Boundary checks ---")
check("censoring removes support (some cells zeroed)", zeroed > 0, f"{zeroed} cells")
check("censored: known S_alpha + full re-fit CANNOT fully recover (informational impossibility)",
      div_cens_refit > 0.05, f"residual div={div_cens_refit:.4f}")
check("support-preserved re-fit strictly out-recovers censored re-fit",
      durable_w[1.0] < div_cens_refit - 0.02)

# ----------------------------------------------------------------------------
# Finite-sample robustness (not an infinite-data artifact)
# ----------------------------------------------------------------------------
print("\n[4] Finite-sample robustness (M sampled transitions, seed=0)")
rng = np.random.default_rng(0)
M = 200_000
flatP = selected_joint(S_OP).ravel()
idx = rng.choice(N * N, size=M, p=flatP)
Pc = np.bincount(idx, minlength=N * N).reshape(N, N).astype(float)
Pc /= Pc.sum()
div_fin = divergences(fit_bundle(Pc), REF)["total"]
print(f"    finite-sample deformed total_div = {div_fin:.4f}   (population: {div_def:.4f})")
check("finite-sample deformation matches population within 10%",
      abs(div_fin - div_def) < 0.10 * div_def + 0.02, f"|{div_fin:.4f}-{div_def:.4f}|")

# ----------------------------------------------------------------------------
print("\n" + "=" * 78)
n_pass = sum(1 for _, ok, _ in checks if ok)
n_tot = len(checks)
print(f"CHECKS: {n_pass}/{n_tot} passed")
print("=" * 78)
if n_pass != n_tot:
    print("FAILED:", [name for name, ok, _ in checks if not ok])
    raise SystemExit(1)
print("Probe E: all checks passed. Mechanism shown SYNTHETICALLY only; "
      "no claim about production Grok.")
