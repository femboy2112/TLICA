# Round 2 — Earning *metastability* against the substrate

**Epistemic status.** Research note, extension layer, not foundation. This round earns (or refutes) the borrowed word *metastability* as it is used across the archive, and audits the specific metastability language that landed in the frozen foundation at v5.5.0 (§8.11, File 3). Its central verdict survived **triangulation across three independent bearings** — object-cartography (what is the borrowed object, what is its literal source-domain contract), adversarial re-derivation (does the frozen dynamics actually earn the claim), and format/precedent (how the prior rounds graded such things) — **plus the orchestrator's own independent read of the frozen §8.7–8.11 text.** The load-bearing catch is grounded directly in the frozen text and in §8.10's own derived result; an unmerged research branch (`differential-field-model-2026-09-12`, commit `747cf1b`, **not on `main`**) is cited only as *corroborating, not load-bearing* — two of the three bearings share that citation, so it counts once, not twice. Labels use the corpus vocabulary: **Derived / Conjectured / Refuted / UNVERIFIED** (no "Demonstrated"; "Observed" is used in-body for a single clean read or relayed-but-unre-run evidence).

**Open decision this round exposes (author's to settle).** The frozen clause "*those are metastable set-points*" (§8.11) admits two readings — a **strong** one (a declarative claim that the slow structure $G$ *carries* multiple stable configurations) and a **charitable** one (a conditional naming: *where* $G$ happens to be multi-well, *call* those set-points). The two imply different repairs. This note does not decide the reading; it lays out both and hands the disambiguation to the author as part of a **gated** errata recommendation (§8), because the frozen foundation is never edited unilaterally.

**Resolved with the author (2026-09-17).** The "escape" of §2 is confirmed *apparent* (centrifugal — the felt binding weakens, the state is not forced out), does **not** require a fast rate (slow weakening suffices), and its "straw that broke the camel's back" abruptness is **Derived and numerically confirmed** as a latency effect (§2). The frozen §8.11 "rate-induced escape / floor outruns the state" label is refined accordingly (§8, E2). The *metastable set-points* reading (§3) remains the open item.

**Depends on:** [Round 0 — dynamical-substrate axioms](./dynamical_substrate_axioms_2026-09-08.md) and [Round 1 — reachability and momentum](./substrate_round1_reachability_momentum_2026-09-08.md). Reads against the frozen [foundation File 3, §§8.7–8.11](../foundation/3_formal_apparatus.md) (v5.5.0).

---

## 0. Why this round exists

[Round 0](./dynamical_substrate_axioms_2026-09-08.md) seeded *metastability* as **Conjectured**, scoped to the toolkit-closure object $\mathrm{Cl}_{\mathcal{A}}(\mathcal{T}_t)$ over frame-state space $X$, with the discriminator *exit-time ≫ intra-set mixing-time*. [Round 1](./substrate_round1_reachability_momentum_2026-09-08.md) handed metastability forward as the next ripe target, carrying three constraints: (i) **no continuity** — reachability is provably discontinuous in frame-nearness, so no argument may lean on "near frames reach near places"; (ii) **§7.4 coupling discipline** — entanglement must enter as a state-space invariant; (iii) the weight-space attractor $w^\* = \alpha/(\alpha+\beta)$ is a live candidate whose exit-time separation is to be posed **against the contraction-to-$w^\*$ dynamics, not against a bare "sticky region."**

Since those rounds landed (2026-09-08), the foundation's dynamical apparatus grew: v5.5.0 (commit `1115481`) seated the **Mode-B $G$-actuator** into §8.11 and, with it, two pieces of metastability language — *"rate-induced escape from the moving attractor"* and *"metastable set-points"* in the slow structure $G$. Round 2 therefore has two jobs: earn the borrowed word against the built dynamics, and audit whether the frozen language earns itself.

## 1. The word is overloaded — five objects under one term

The archive currently runs **five non-identical formal objects** under the single English word *metastable* (object catalogue: Bearing A, direct reads; **Verified** citations, genus assignments **Observed**):

| # | Object | Where | Genus (literal source-domain contract) | Built? |
|---|--------|-------|----------------------------------------|--------|
| (a) | $G$-multistability — "metastable set-points" | frozen §8.11 (`3_formal_apparatus.md:531`) | (i)/(ii) multi-well / almost-invariant | **No** — nominal/conditional; no $G$-potential written |
| (b) | "rate-induced escape from the moving attractor" | frozen §8.11 (`:531`) | (iii) R-tipping | Mechanism built (= §8.10); **label mismatched** |
| (c) | almost-invariant set over toolkit-closure | Round 0 (`:226-238`) | (ii) almost-invariant set, exit≫mixing | **No** — promised, untested |
| (d) | C4b "metastable cave" | `out_of_the_cave_v0_1_2.md:98-109` | *own genus* — discrete stochastic recurrence | **Yes** — proved (Borel–Cantelli) |
| (e) | neural itinerancy | branch `747cf1b:38` (not on main), cited only | (iv) heteroclinic winnerless competition | No — phenomenological motivator |

The literal contracts are genuinely distinct (source-domain definitions **Verified** against Kramers/Freidlin–Wentzell, Dellnitz–Froyland almost-invariant sets, and the Ashwin–Wieczorek–Vitolo–Cox B/N/R-tipping taxonomy):

- **(i) Kramers / multi-well:** a potential with ≥2 minima separated by a saddle; local stability; *noise-driven* escape on a timescale exponential in barrier height; fast-in-well / slow-between timescale split.
- **(ii) Almost-invariant set:** $M\subseteq X$ with exit-time ≫ intra-$M$ mixing-time; a spectral-gap / transfer-operator statement, not necessarily an energy landscape.
- **(iii) R-tipping (rate-induced):** a system tracking a *moving* attractor tips away **iff the input moves faster than the system relaxes** — needs no second basin and no bifurcation, but **does** require a critical rate.
- **(iv) Heteroclinic itinerancy:** a trajectory roaming a network of saddle "ghost attractors," never settling and never barrier-crossing.

The glossary already disclaims literalism for (b)/(d)/Lagrange-points — *"shape borrowed… not a literal thermodynamic/energy-landscape claim"* ([`glossary.md:479-485`](../docs/glossary.md)) — but that gloss was written before the v5.5.0 $G$-multistability clause landed, so it does not currently cover (a). **Round 2's task is to say, per object, which literal contract it meets.**

## 2. The felt-salience object (§8.9–8.11) — target-relocation and its latency Derived; the R-tipping *label* Refuted

**Shape (asserted by the corpus).** Mode B lets the I depart from passive gradient descent; the departure is glossed as *"rate-induced escape from the moving attractor — the floor outruns the state"* (§8.11, `:531`).

**Literal claim to earn.** That the §8.9–8.11 dynamics exhibits **genus (iii) R-tipping**: a critical rate above which the baseline $b$ fails to track its target and tips away.

**The construction.** Mode B is self-sourced imprinting that rewrites the slow structure $G$, co-modulating both of its readings: the target $f=F(G,\cdot)$ (the well's *location*) and the metric $\rho=R(G)$ (the well's *walls* — both $\Phi=\tfrac12\lVert f-b\rVert_\rho^2$ and $V=\tau\lVert\Delta\rVert_\rho$ are $\rho$-weighted, so $\rho$ *is* the felt binding strength of each content-axis). A change in $\rho$ **cancels from the baseline law** $\dot b=\gamma(f-b)$ by the natural-gradient reading (§8.10, `:519-521`), so Mode B never moves $b$ by an anti-gradient force. It moves $b$ by moving the **target** — **target-relocation** — and, separately, weakens the **felt attractor** by lowering $\rho$.

*What "escape" actually is (author's intended mechanism, tested here).* The departure is **not** literal barrier-crossing, and **not** the state falling behind a fast target. It is *apparent* — centrifugal-shaped: the attractor's felt binding $\rho$ weakens (under self- or field-driven $G$-writing) until the content that was gripping no longer grips. Nothing pushes $b$ out of a well; the well's walls come down. The mathematical signature of the escape being *apparent* is exactly the $\rho$-cancellation above — a change in binding exerts **zero force on $b$**. Because a *literal* escape needs a second basin to land in, the general phenomenology is a **committed departure to a new set-point** (§3), of which the single-well "the grip simply lapsed and I drifted" case is the degenerate limit.

*The latency (Derived, and Observed).* Because $\rho$ cancels from $\dot b$ but weights $V$, a slow decay of $\rho$ is **unregistered while the self tracks**: with $\Delta\approx0$ the felt salience $V\approx0$ *regardless of $\rho$*, and the felt signature of the weakening is $O(\Delta^2\,\dot\rho)$ — doubly suppressed. The self coasts its inertial path, not feeling the walls thin, until a **perturbation** drives $\Delta$ to $O(1)$ — the "test," the *straw* — at which point the now-lower $\rho$ finally surfaces in $V$: the pull that would have restored the state is muted, and the departure registers abruptly though the weakening was gradual. A calibrated numerical probe confirms it (committed beside this note, [`substrate_round2_metastability_2026-09-17_latency_probe.py`](substrate_round2_metastability_2026-09-17_latency_probe.py); integrator calibrated on the analytic relaxation $b(t)=f+(b_0-f)e^{-\gamma t}$ to $1.8\times10^{-5}$):

> **C1 (latency):** as $\rho$ collapses $1.0\to0.05$ (a 20× loss of binding), peak felt $V$ over the *entire* decay is $6.0\times10^{-4}$ — nothing felt.
> **C2 (readout):** an identical straw $|0.30|$ registers peak felt $V=0.288$ early ($\rho{=}0.93$) but $0.072$ late ($\rho{=}0.058$) — ratio $3.997$, matching the analytic $\sqrt{\rho_{\text{early}}/\rho_{\text{late}}}=3.997$ exactly. Same straw, a back 4× closer to breaking.

The behavioral outcome (held vs. leaves) is then gated by the *posited* slack/pressure mechanism (§8.11); this probe earns only the Derived substrate beneath it — the latency and the coupling-readout $V_{\text{peak}}\propto\sqrt\rho$. (Honesty note: **C1 (latency) is the probe's genuinely independent numerical result** — the integrator produces $\Delta\approx0$ through the $\rho$-collapse, confirming the $\rho$-cancellation. **C2 is a consistency check, not a second blind witness for $\sqrt\rho$**: the probe implements $V=\tau\sqrt\rho\,|\Delta|$ directly, so the exact ratio confirms that the *dynamics* adds no $\rho$-dependence beyond posit P1's weighting — the perturbation displaces $b$ $\rho$-independently — while the $\sqrt\rho$ law itself rests on P1, not on the run. Both adversarial bearings flagged this; it is why the readout is graded Derived-from-P1, never "Confirmed.")

*Why the frozen label is wrong-shaped.* R-tipping requires the target to move *faster* than relaxation; §8.11 insists $G$-writing is **slow** ($\dot G=O(\varepsilon),\ \varepsilon\ll\gamma$), and §8.10 proves that even a persistently moving field yields **bounded lag, never a runaway** ($\limsup V\le\tau L/\gamma$, `:525`). So the escape is *not* rate-induced (slow weakening suffices — confirmed) and *not* "the floor outrunning the state" (the state keeps its footing; the grip dissolves). The honest dynamical-systems neighbour is a **perturbation-triggered threshold-crossing over a slowly-weakening coupling** — *N*-tipping-flavored (perturbation-induced), **not** *R*-tipping. Held to its own discipline: literal *N*-tipping needs a second basin, the exact unbuilt question of §3, so the label stops at "perturbation-triggered."

> **Verdict (this part).** *Target-relocation* (Mode B moves $b$ by moving $f$, $\rho$ cancelling) is **Derived**. The *apparent/centrifugal escape* (felt binding $\rho$ weakens; no force on $b$) and its **latency** (unregistered until a perturbation reads out $\rho$) are **Derived and Observed** — analytic + calibrated probe, agreeing to three figures. The frozen **label** "rate-induced escape from the moving attractor — the floor outruns the state" is **Refuted as literal**: doubly wrong-shaped (not rate-induced; not tracking-failure). The mechanism is real and now correctly re-described; only the borrowed words overreach — the Round-1 *momentum* pattern again.

**Corroboration (Observed).** The unmerged branch `747cf1b` numerically found Mode-0 *"never escapes at any $\nu$ — only lags,"* with "sudden regime-change" left **OPEN** across three graded candidates (R1 name-inflated at $\nu_c\approx0.99$; R2 bistable escape, doubly conditional; R3 a posited resonant window). The perturbation-triggered / latent-coupling account here is a sharper, cheaper candidate for that same "sudden regime-change" slot — and it *predicts* the abruptness (latency + threshold) the rate-based candidates had to posit.

**Discriminator.** For the *rate* reading: exhibit a critical $r_c$ with a qualitative $b$-orbit change — §8.11's $\varepsilon\ll\gamma$ argues it away. For the *perturbation* reading (the earned one): the coupling-readout $V_{\text{peak}}\propto\sqrt{\rho}$ for a fixed-magnitude probe is the falsifiable signature (confirmed above); whether the post-departure state *commits* to a distinct set-point is the §3 question.

## 3. The $G$-multistability claim — unbuilt; unflagged; in tension with §8.7

**Shape.** *"Where the I's imprinted landscape itself carries more than one stable configuration, those are metastable set-points… the multi-stability lives in the slow structure $G$, not in the scalar $V$"* (§8.11, `:531`).

**Phenomenological target (author's datum, 2026-09-17).** The apparent escape of §2 *typically* lands the self in a **committed new configuration**, not a return; the single-well "the grip lapsed and I drifted" case is the **degenerate limit**, recovered when no second configuration has been carved. So the multi-stable picture is the *general* case and drift is nested inside it. This sharpens what Round 3 must build — a multi-well $G$ with single-well as its limit — but is the datum to be earned, **not** the earning.

**Literal claim to earn.** Genus (i)/(ii): that $G$'s own dynamics carries ≥2 stable configurations (a multi-well landscape, or an almost-invariant partition of $G$-space).

**What is actually written about $G$.** Only two things, both verified in the frozen text: $\dot G=O(\varepsilon),\ \varepsilon\ll\gamma$ (a timescale bound) and $R,F$ Lipschitz in $G$ (a regularity condition). **Neither entails, nor even hints at, multi-well structure** — Lipschitz-and-slow is compatible with a single well. No $G$-potential, no barrier, no equation of motion for $G$, no well-count appears anywhere in §§8.9–8.11.

**Two readings, two repairs (the open decision of the header):**

- **Strong reading** — "the multi-stability lives in the slow structure $G$" is a positive architectural location-claim. Then it is **Refuted as a literal claim**: the structure it locates is never built.
- **Charitable reading** — the "*Where…*" is a genuine conditional, an innocuous naming convention ("*if* $G$ is multi-well, *call* those set-points"). Then it is **harmless but an unflagged posit**: unlike `P1`, `P2`, and `Posit G` one sentence away, it commits to structure "beyond what the foundation forces" without the named-posit tag §8.8 explicitly requires for exactly that move (`:491`).

Either way, the *multi-well $G$ structure itself* is **Conjectured / not earned**. The unmerged branch reached the same wall from the other side: multi-basin structure is *basin-escape OPEN*, doubly conditional on an open sign ($\mathsf{Foc}_{sd}\to w^\*$; $\alpha,\beta$ both depend on $\mathsf{Foc}$, `3_formal_apparatus.md:282`) and a loop-gain>1, and the naive autonomous-fold route requires the **forbidden dependency** $w\to\alpha$ barred by the fixed-dependency discipline (§8.8, `:491`).

**Independent tension with §8.7.** §8.11's persistence clause — $G$ *"does not spontaneously re-zero (chronic conditions displace the baseline for good)"* — asserts a persistence property that §8.7 **explicitly declines to formalize**: *"The architecture does not specify rates… how persistent it is, what conditions support deactivation or revision — these are application-level questions"* (`:487`). A "for good" persistence claim is exactly a rate/persistence commitment §8.7 reserves for application-level empirical work.

> **Verdict (this part).** The multi-well $G$ landscape is **Conjectured, not earned** — no dynamics for $G$ is written that could carry it, and the sibling numerical branch independently left it OPEN. The clause's status in the frozen text is either **Refuted-as-literal** (strong reading) or an **unflagged posit** (charitable reading); the disambiguation is the author's and drives the errata shape (§8). The "for good" persistence sub-claim is **in tension with §8.7** on either reading.

**Discriminator.** Write a $G$-equation-of-motion (or a transfer operator on $G$-space) and count its stable fixed points / almost-invariant sets. Two-or-more with a genuine exit-time≫mixing-time separation earns genus (i)/(ii); one well refutes the multi-stability location-claim.

## 4. The genus-(ii) contract (Round 0's actual promise) — still Conjectured, and a *different* object

Round 0 did **not** scope metastability to the felt-salience orbit of §§8.9–8.11 (which was authored later, 2026-09-13). It scoped it to the **toolkit-closure** object $\mathrm{Cl}_{\mathcal{A}}(\mathcal{T}_t)$ over frame-state space $X$ (`dynamical_substrate_axioms_2026-09-08.md:226-238`) — a *different state space* (discrete/combinatorial closure over frames) from the continuous profile-space orbit. That contract remains **untested**, and it inherits Round 1's **no-continuity tripwire**: since $x\mapsto R(x)$ is discontinuous in frame-nearness $d$, the almost-invariant-set argument may **not** use $d$-nearness as a proxy for dynamical closeness — it must be posed against the *dynamics* (Round 1's directive: against the contraction-to-$w^\*$, not a bare sticky region).

There is, however, an adjacent object that **is** proved — but in a genus of its own. The application tier's C4b "metastable cave" ([`out_of_the_cave_v0_1_2.md:98-109`](../applications/out_of_the_cave_v0_1_2.md)) proves *almost-sure eventual escape* from a closure via a **Borel–Cantelli / Lévy** argument: non-summable recognition-probability ⇒ escape a.s. This is **Observed as an in-tier proof** (relayed; not re-derived here), but it is a **discrete stochastic point-process recurrence** result — no potential, no barrier, no exit-time-vs-mixing-time comparison. It satisfies neither genus (i) nor genus (ii) as literally stated; it is a fifth, structurally distinct object that happens to share the theme "closed-now, latent-exit."

> **Verdict (this part).** Round 0's genus-(ii) almost-invariant-set contract over toolkit-closure is **Conjectured**, unbuilt; its discriminator (exit-time ≫ mixing-time, posed against contraction-to-$w^\*$) is *specified* here but not *executed*. The proved C4b escape is a genuine result in a **different genus** and should not be conflated with the genus-(ii) promise.

## 5. Adversarial triangulation

- **Bearing — object cartography.** Located all five objects and their file:line anchors; pinned the three literal source-domain contracts; identified that the frozen §8.11 sentence welds a genus-(iii) clause (built) to a genus-(i)/(ii) clause (unbuilt) with no seam. Direct reads, **Verified**.
- **Bearing — adversarial re-derivation.** Independently re-derived §8.10's bounded-regime bound; showed the described Mode-B mechanism has no rate-dependence; found the missing Posit tag and the §8.7 persistence tension. **Verified** against the frozen text.
- **Bearing — format/precedent.** Fixed the Round-2 skeleton, the label vocabulary (no "Demonstrated"), the filename convention, and Round 1's explicit "pose exit-time against contraction-to-$w^\*$" directive.
- **Orchestrator's own read.** Re-read frozen §§8.7–8.11 directly and confirmed the four load-bearing textual facts (no Posit tag on the set-points clause; §8.10 proves bounded non-escape; $\varepsilon\ll\gamma$; §8.7 rate-agnosticism).

**Provenance discipline.** The primary catch (§2, §3) rests on the frozen text and §8.10's derived result — **not** on the unmerged branch. Two bearings additionally cite branch `747cf1b`; that corroboration is **common-mode** (one route, not two) and is labelled Observed, not counted toward the triangulation.

## 6. Ledger

| Claim | Verdict | Basis / boundary |
|-------|---------|------------------|
| Target-relocation: Mode B moves $b$ by rewriting $G$ to move $f$; $\rho$ cancels | **Derived** | §8.10 ρ-cancellation applied; verified in frozen text |
| Apparent/centrifugal escape (felt binding $\rho$ weakens; no force on $b$) + its latency | **Derived + Observed** | $\rho$-cancellation ⇒ apparent; $\Delta\approx0\Rightarrow V\approx0$ ⇒ latency; calibrated probe, $V_{\text{peak}}\propto\sqrt\rho$ (ratio 3.997 = analytic) |
| "Rate-induced escape … floor outruns the state" as a *literal* label | **Refuted** | not rate-induced (slow weakening suffices); not tracking-failure; the escape is perturbation-triggered — a genus mislabel |
| Multi-well $G$ / "metastable set-points" carries a built structure | **Conjectured (not earned)** | no $G$-dynamics written; sibling branch left OPEN; fold route needs forbidden $w\to\alpha$ |
| Frozen §8.11 set-points clause status | **Refuted-as-literal (strong reading) / unflagged posit (charitable)** | author disambiguates; §8.8 tag missing either way |
| "Does not spontaneously re-zero … for good" persistence | **In tension with §8.7** | §8.7 declines persistence rates as application-level (`:487`) |
| Genus-(ii) almost-invariant-set over toolkit-closure (Round 0's promise) | **Conjectured** | discriminator specified, not executed; no-continuity tripwire binds |
| C4b Borel–Cantelli cave-escape | **Observed (in-tier proof), different genus** | discrete recurrence, no barrier/exit-time; not the genus-(ii) contract |
| Glossary "shape not literal" umbrella | holds for (b)/(d), **does not yet cover (a)** | `glossary.md:479-485` predates the v5.5.0 clause |

## 7. Forward — Round 3 (basin / attractor) and the concrete next cut

Round 3 (basin/attractor) inherits: the weight-space attractor $w^\*=\alpha/(\alpha+\beta)$ (Round 1) is the live candidate; the **exit-time ≫ mixing-time** discriminator is the tool, and per Round 1 it is posed **against the contraction-to-$w^\*$ dynamics**, never a bare sticky region. Metastability cannot be certified until *some* multi-configuration dynamics — for $G$ or for the toolkit-closure transfer operator — is actually written down; §§8.9–8.11 supply only a single convex well for $b/V$.

The concrete experiment already named on the unmerged branch (`WORKING_MODEL.md:238`, not on main): build a monotone slow "reality-debt" variable $D$ from **only** frozen osmotic mechanisms, *without* the forbidden $w\to\alpha$ route, and test whether a two-timescale $(D,b)$ system exhibits a genuine exit-time separation. That is the discriminating build Round 3 should run — and, per the **repro discipline**, whatever probe scripts it uses must be committed (Round 1's `scratchpad/*.py` "Reproduction:" pointers were never committed and were dead links on the public repo — since removed, 2026-09-17). This round follows that discipline: its latency probe [`substrate_round2_metastability_2026-09-17_latency_probe.py`](substrate_round2_metastability_2026-09-17_latency_probe.py) is committed beside this note.

## 8. Recommended foundation errata — **GATED, not applied here**

This note is research-tier and changes no frozen text. The audit above implies a candidate errata to §8.11 (File 3), of the **same species** as the external-audit correctives v5.4.1 / v5.4.3, and it is offered **only as a recommendation for the author**, to be run through an adversarial pass (a `dalembert`/`masters`-grade attack on the equations *and* on term-consistency) and signed off before any frozen byte moves:

- **E1 (minimal, if the charitable reading is intended):** tag "metastable set-points" as a **named posit** (parity with `P1`/`P2`/`Posit G`) and make its conditional explicit, so the clause reads as a reserved name for an open direction, not a built structure.
- **E2 (sharper, if precision is preferred):** replace *"rate-induced escape from the moving attractor — the floor outruns the state"* with the accurate mechanism, now Derived-and-Observed (§2): *the felt binding $\rho$ of the occupied configuration weakens under self/field $G$-writing; because $\rho$ cancels from the baseline law the weakening is unregistered while the self tracks, so the self coasts its inertial path until a perturbation tests — and reveals — the now-weakened coupling, whereupon it departs (apparent, "centrifugal" escape; a perturbation-triggered threshold-crossing, not a rate-induced or barrier-climbing one)*. This drops the genus-(iii) vocabulary the mechanism does not earn and *adds* the latency prediction the frozen text was missing; demote the multi-well-$G$ location-claim to a labelled **open direction** (§3; the branch's R2/R3 candidates).
- **E3 (either way):** reconcile the "*for good* / does not spontaneously re-zero" persistence clause with §8.7's stated rate-agnosticism — either soften it to an application-level illustration or flag it as a posit.

**This is not applied. Not in this commit. The freeze is the author's to move.**

---

*Round 2 of the math-justification program. Foundation v5.5.0 untouched. `make validate` expected green (links + self-containment + term pins).*
