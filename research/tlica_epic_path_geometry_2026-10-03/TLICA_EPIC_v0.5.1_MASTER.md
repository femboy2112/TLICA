# TLICA–EPIC v0.5.1
## Denotational Diagram Standard — a counting shorthand for TLICA

**Date:** 2026-10-03
**Status:** transportable master note; research/application tier; **foundation impact: none**. v0.5.1 is a readability/grammar errata pass over v0.5.0; the mathematical read-off rules are unchanged. Everything here sits around the frozen TLICA foundation (v5.5.x) and is promotion-gated.
**Supersedes:** v0.5.0 for presentation/grammar only; v0.5.0 superseded v0.4.0 Part XIII as the diagram standard. Retains v0.1–v0.4 mathematics as stated in §12.
**Author:** Leah. AI-assisted formalization, notation audit, repository reconciliation.
**Repository:** `femboy2112/TLICA`, branch `research/tlica-epic-path-geometry-2026-10-03`, base `821ce7e`.

---

## 0. How to use this file (cross-model transport)

This document is self-contained. A reader with **no access to the TLICA repository** can, from this file alone:

1. draw a TLICA–EPIC diagram under the v0.5 legend (§4);
2. read the four TLICA quantities κ, φ, ρ, D off any such diagram by counting (§5);
3. serialize a diagram as plain text (§6) so that a model without image input can carry it;
4. run the reference reader in Appendix A on that text and get the same numbers;
5. know exactly which claims are derived, which are posited, and which are conjectured (§11).

The minimum of the TLICA foundation needed for all of this is restated in §2 with the foundation's own symbols. Nothing in §2 is new; it is quoted so the file travels.

**One-line purpose.** The diagram is to TLICA what a Feynman diagram is to QED: *a sparse picture with a fixed rule that turns its shape into the algebra.* It is not a claim that TLICA is a field theory, and it is not a path integral. See §1.3 for what the analogy does and does not carry.

### 0A. Read the picture in 90 seconds

Do **not** learn ten unrelated symbols first. Read every ordinary diagram as five questions, in this order:

1. **κ — contact:** where does the world touch the diagram? Follow the contact wire and read χ.
2. **D — mediation:** how many substrate stages stand between world and the I? Count the substrate vertices on the inbound path.
3. **ρ — integration:** what has become structurally bound to the I? Follow weighted integration wires from the cogito and read max-flow.
4. **φ — verification:** does the claim's verification chain reach a tool the I actually possesses? Count ⇒ steps to ground; an open chain means φ is **undefined**, not merely low.
5. **S — actualization:** at the turnaround, which exit was realized? Read the sign of slack `S = M − Pressure`.

Then read the cycle spatially: **upper lane left→right** (world → substrate → self), turn at the gate, then **lower lane right→left** (self → substrate → world). The lower lane is later causal time, never time reversal.

A useful mnemonic is:

> **touch → mediate → integrate → verify → act.**

The full ten-glyph table in §4 is the reference manual; the five questions above are the front door.

---

## 1. Cold-start thesis

### 1.1 The problem the previous versions had

v0.1 (EPIC) had the most mathematics and a dense glyph legend nobody could read at a glance. v0.4 fixed readability by reducing the primitives to *wires, points, and expandable circuit-nodes* — but every legend entry then denoted **topology only**. A reader could recover the *shape* of the reasoning and not one TLICA quantity.

What makes a Feynman legend both sparse and powerful is not that it has few glyphs. It is that **every glyph carries an algebraic factor** — a line is `i/(p²−m²)`, a vertex is `−ieγ^μ` — and the order of the whole term is read by counting vertices. The physicist looks at the picture and writes the integral.

### 1.2 The fix

Keep the v0.4 glyph budget. Give each glyph a **denotation** (what TLICA object it is) and a **read-off** (what you compute from it). TLICA already contains three counting rules that are Feynman-shaped and were sitting unused in the foundation's File 3:

| rule | foundation source | what you count |
|---|---|---|
| φ counts steps | `φ = 1 − n·δ − ε` (File 3 §7.3) | the number `n` of steps on the verification pathway; each costs δ |
| D counts mediation stages | orders 1/2/3 (File 3 §8.5.1) | substrate vertices on the inbound path |
| ρ is a flow | `ρ = C/(1+C)`, `C = MaxFlow(î, x)` (File 3 §7.2) | flow from the cogito over weighted integration edges |

Plus κ, which is read off a single wire (`κ = χ(t, n)`, File 3 §7.1), and one **sign**: the slack gate `S = M − Pressure` (File 3 §8.11) at the turnaround vertex decides whether the outbound pass was *automatic* (`S ≤ 0`) or *slack-mediated* (`S > 0`).

So one picture, under the v0.5 legend, computes **four numbers by counting and one sign**: depth of verification (φ), order of mediation (D), flow to the self (ρ), strength of contact (κ), and which exit the actualization took (S) — without the reader opening File 3.

### 1.3 What the Feynman analogy carries and what it does not

Carries:

- glyph → factor; shape → quantity; counting → order;
- compositionality: a subsystem can be drawn as a dot when only its boundary behaviour matters (§7), which is the role the "blob"/effective-vertex plays in QFT;
- a strict separation between what is **drawn** (declared) and what is **computed** (derived), so a dashed conjectured bridge can appear in the picture without ever entering a number.

Does not carry (and the document does not claim):

- a Gaussian baseline, Wick contraction, or a perturbative series — see §10.1 for the one place in TLICA where that *is* licensed, as a gated research pointer;
- amplitudes or phases: **no declared transport, no phase** (v0.1 §22, retained);
- any scalar truth score; any collapse of κ, φ, ρ into one number.

The compact discipline, carried forward:

> **no path count without provenance; no φ update without a pathway; no phase without transport; no certainty without adequacy.**

---

## 2. TLICA foundation minimum (quoted, not new)

Everything in this section is the frozen foundation's own apparatus (Files 1–3, v5.5.x). It is restated here with the foundation's symbols so the file is self-contained. Nothing here is promoted, altered, or reinterpreted.

### 2.1 Layers, modes, and the cogito

- TLICA has two **layers**: the *intrinsic* layer (mathematical/logical structure, in re) and the *asymptotic* layer (everything acquired). The word *layer* is reserved for this distinction.
- **Modes A, B, C** are developmental/operational response-types, not layers. Mode B is the reflexive rewrite of the lived-I structure and is *not* a synonym for careful thinking.
- The **cogito** `î_m` ("I am I") is the anchor. `ρ(î) = 1`; nothing else has `ρ = 1`. `φ(î) = 1 − δ` structurally.

### 2.2 The three coordinates

For a modeling I `m`, time `t`, content `x ∈ A^m_t` (the asymptotic field):

**Contact.** For a world item `n ∈ N_m`: `κ_{m,t}(n) := χ_m(t, n)`. For a content with source map `σ`:
`κ^out_{m,t}(x) := sup{ κ(n) : n ∈ σ^m_t(x) }`, and `0` if `σ(x)` is empty or undefined. Content-level contact is outside-perspective because it uses `σ`.

**Identity-correlation.** For each integration mode `k ∈ K` there is a weighted directed graph
`G^{m,k}_t = (V, E^{m,k}_t, w^{m,k}_t)`, `V = {î_m} ∪ H^m_t`, `w ∈ [0,1]`.
Define `C^{m,k}_t(x) := MaxFlow_{G}(î_m, x)` and
`ρ^{m,k}_t(x) := C/(1+C)` for `x ≠ î`, `ρ(î) = 1`.
The vector `ρ⃗(x) = (ρ^k(x))_k` is primary; a scalar projection `Σ_k a_k ρ^k` is optional. Max-flow is the foundation's instantiation (it respects bottlenecks); other flow-like aggregations are "compatible applied choices" (see §10.2).

**Truth-indistinguishability (three tiers).** Tier 1 (intrinsic): not in the φ-domain. Tier 2 (cogito): `1 − δ`. Tier 3 (contents with a verification pathway constructible from `Tools^m_t`):

`φ_{m,t}(x) = 1 − n_{m,t}(x)·δ − ε_{m,t}(x)`,

where `n` is the conditional depth (number of steps on the constructible verification pathway) and
`ε_{m,t}(x) = ∫_{Q^m_t} (1 − q(x)) dμ^m_t(q)` is the probe integral, with `ε + nδ ≤ 1`.
`μ^m_t = Λ^μ_m(Foc, κ^out, Q)` is the probe weighting generated by focus and contact.
**If no pathway is constructible from the current toolset, `n` is undefined and φ does not apply** (undefined, not low).

**Formal non-reducibility.** Vary `χ` alone → only κ moves; vary truth-profiles alone → only φ moves; vary the graphs alone → only ρ moves. They are *dynamically entangled* (they influence each other in operation) but *formally independent* (not definable from one another).

### 2.3 Phenomenal availability and the four classes

`A_{m,t}(x) ∈ {0,1}` is a status predicate (not a fourth coordinate). Joint with φ:

| A | φ | class |
|---|---|---|
| 1 | defined | conscious-clear |
| 1 | low / undefined | conscious-fuzzy (source-opaque) |
| 0 | constructible on activation | latent / retrievable |
| 0 | no constructible pathway | unconscious-operative |

### 2.4 Mediation orders

Contents reach the I through the substrate `S_m`. Three characteristic orders (dominant pathway, not exclusive category), each stage lossy:

- `D = 1` salience capture: `N → S^sal → Foc` (moves focus; sharp);
- `D = 2` cognitive: `N → S^cog → î` (thoughts; propositional; usually φ-gripable);
- `D = 3` somatic-then-cognitive: `N → S^som → S^cog → î` (emotions; two compressions).

Tendency, not law: `D↑ ⇝ E[Fz]↑` (fuzziness = low explicit source-resolution from inside). `D` and `Fz` are typological, not coordinates.

### 2.5 Imprinting (the foundation's only update vertex)

An update event `e = (s, u, v, k, α, β)` on edge `(u,v)` of mode `k`:

`w_{s⁺}(u,v) = Π_{[0,1]}( (1−β)·w_{s⁻}(u,v) + α·(1 − w_{s⁻}(u,v)) )`,

with `α = 𝒜^k_m(u, v, Foc_s, λ_s(v))`, `β = ℬ^k_m(…)`, `λ_s(v) = sup κ over σ(v)`. The functions `𝒜, ℬ` are open; their *dependencies* (focus, contact) are fixed. Osmotic imprinting (ambient co-occurrence, always online, no focus required) runs underneath this.

### 2.6 Focus, slack, dynamics (named so the diagram can refer to them)

- `|Foc^m_t| ≤ M_m(t)`, capacity set by substrate.
- **Slack** `S_{m,t} = M_m(t) − Pressure_{m,t}`. `S ≤ 0`: the pressured filter dominates, focus collapses to the contact-driven term, mode-response is automatic — passive descent of the local mismatch gradient, which is *not* reward maximization and *not* the same as myopic. `S > 0`: active Mode-B reweighting is available. The gate at `S = 0` is a **named posit**; the stronger claim that felt choice dissociates from behaviour near `S = 0` is **UNVERIFIED**. Perceived slack vs actual slack can differ ("stuck but capable").
- Reflexive-differential reading: `Δ = f − b`, felt salience `V = τ‖Δ‖_ρ`, baseline law `ḃ = γ(f − b)`; slow structure `G` with `ρ = R(G)`, `f = F(G,·)`. (Quoted only; the diagram never computes these.)

### 2.7 Notation firewall (binding on every diagram in this standard)

- `φ` is truth-indistinguishability. Traces are `y_t`, `o_t`, never `φ_t`.
- `S` is slack. Probe availability is `μ_t(q)`. The bridge `S↓ ⇒ μ↓` is **CONJECTURED**, never an identity.
- `G` is the slow lived-I structure. The information tensor is `𝓘_Q`, never `G`.
- `σ` is the source map / source-map adequacy diagnostic. Not a fourth coordinate.
- *layer* = intrinsic/asymptotic only. Diagram layout uses *lane*, *stratum*, *band*.
- Nothing in this standard adds ρ, κ, φ, σ, μ, S, affect, or coherence into a single score.

---

## 3. EPIC minimum (retained from v0.1–v0.4)

Stated once, with status. These are the analytical instruments the diagram can carry as annotations; they are not glyphs.

- **Total observation map and ambiguity fiber.** `η_Q : X → Y_Q`, `𝓕_Q(x) = η_Q⁻¹(η_Q(x))`. Exact, model-relative indistinguishability. *Disclosed (definition).*
- **Probe monotonicity.** `Q₁ ⊆ Q₂ ⇒ 𝓕_{Q₂}(x) ⊆ 𝓕_{Q₁}(x)`. *Disclosed (proof: every probe in Q₁ is in Q₂).*
- **Local kernel.** `𝓚_Q(x) = ker dη_{Q,x}`; global ≠ local (x², x³ examples). *Disclosed.*
- **Resolution tensor.** `𝓘_Q = J_Q^⊤ Σ_Q^{-1} J_Q`, `ker 𝓘_Q = ker J_Q` for Σ ≻ 0; aim the next probe at `λ_min`. *Disclosed.*
- **Provenance covariance.** `y = h(x) + Bu + ε ⇒ Σ = D + BCB^⊤`; `n` copies of one bias give `I_n → 1/τ²`. **Path multiplicity ≠ independence.** *Disclosed.*
- **Pathway-state triplet.** `q ∈ Cl(Tools)` (constructible) ≠ `μ(q) > 0` (available) ≠ `q ∈ Q^exec` (executed). *Disclosed; foundation-promotion candidate A.*
- **Identifiability ≠ adequacy.** `𝓕_Q(x) = {x}` can hold with reality outside `X`; every discriminator keeps a `neither → enlarge X` branch. *Disclosed.*
- **Contextual saturation.** Survivors remain and no constructible probe separates them: "no present discriminator reaches the distinction" ≠ "the distinction is absent." *Disclosed.*
- **Three meanings of interference.** Positive aggregation (`w ≥ 0`), Möbius/cumulant signed interaction, genuine phase (only with a declared compositional character χ). **No declared transport, no phase.** *Disclosed.*
- **Loops must be typed.** Dynamical feedback ≠ transport holonomy ≠ perturbative contraction loop. No unlabelled loop. *Convention.*

---

## 4. The v0.5 legend

### 4.1 Design rule

> **Each glyph is a TLICA object; each glyph has a read-off; nothing else is a glyph.**

Ten glyphs. Everything else (lanes, line styles, labels) is a convention, not an ontology.

### 4.1.1 Five visual families

The ten glyphs are easier to learn as **five families**:

| family | glyphs | question answered |
|---|---|---|
| **anchor / content** | cogito `◉ î`, content `○/◎ x` | *what object am I reading relative to the I?* |
| **integration** | weighted wire, imprinting event `⊕` | *how strongly is it bound into the I?* → ρ |
| **verification** | `⇒` step, ground `⊥`, `q? / q!` | *does the pathway actually close?* → φ |
| **world → substrate** | contact wire, substrate vertex | *how did it arrive and through how much mediation?* → κ, D |
| **actualization** | slack gate with two exits | *which outbound mode was realized?* → sign of S |

So the legend is ten glyphs in the reference sense, but only five conceptual chunks in working memory.

### 4.2 The ten glyphs

| # | glyph | name | denotation (what it IS) | read-off (what you COMPUTE) |
|---|---|---|---|---|
| 1 | `◉ î` | **cogito leg** | the root `î_m`; `ρ=1`, `φ=1−δ`; exactly one per diagram | every ρ-flow starts here; nothing else has ρ = 1 |
| 2 | `○ x` / `◎ x` | **content node** | a content `x` carrying `(κ, φ, ρ⃗)`; closed = internals suppressed, open = internals exposed as a circuit | the coordinates are read **at** this node; open a node only when its mechanism is load-bearing |
| 3 | `u ─(k:w)─▶ v` | **integration wire** | an edge of `G^{m,k}_t` with weight `w ∈ [0,1]`, mode `k`; width ∝ w, style/colour = k | `ρ(x) = C/(1+C)`, `C = MaxFlow(î → x)`; thin wire on every route = fragile integration |
| 4 | `u ═▶ v` (`−δ`) | **verification step** | one unit of conditional depth on `x`'s pathway; each costs exactly δ | `φ(x) = 1 − (#⇒ to ground)·δ − ε`; a chain that never reaches ground ⇒ φ **undefined** |
| 5 | `⊥ g` | **ground** | a verification tool `g ∈ Tools^m_t` the I actually possesses | terminates a φ-chain; no ground reachable ⇒ contextual saturation of that chain |
| 6 | `[q?]` dashed / `[q!]` solid | **probe insertion** | an external leg on a φ-chain with availability `μ(q)`; `q?` constructible-not-executed, `q!` executed with result `q(x)` | `q!` adds `μ·(1−q(x))` to ε; **`q?` adds nothing** — drawn so the hole is visible |
| 7 | `▣ S` | **substrate vertex** | one mediation stage of `S_m` (salience / cognitive / somatic); lossy | `D(x) = #▣ on the inbound path + [delivered to î]`; 1 = salience, 2 = cognitive, 3 = somatic→cognitive |
| 8 | `◇ n ~~(χ)~~▶ x` | **contact wire** | contact from a world item `n ∈ N` with strength `χ(t,n)`; a thought has no contact wire of its own | `κ(x) = χ` on a direct wire, else `sup χ` over `σ(x)`; `σ(x)` empty ⇒ κ = 0 |
| 9 | `⊕(α,β)` on a wire | **imprinting event** | an update event on an integration wire with couplings (α, β) set by focus and contact | `w ← clip_{[0,1]}((1−β)·w + α·(1−w))`; then re-read ρ |
| 10 | `◇ S` with two exits | **actualization vertex** (decision gate) | the turnaround `I → I⁺` where the cycle reverses direction; carries slack `S = M(t) − Pressure` as declared inputs; two exits, *automatic* and *slack-mediated* (Mode B) | `S ≤ 0` ⇒ **AUTOMATIC**: focus collapses to the contact-driven term, passive descent of the local mismatch gradient, no Mode-B reweighting. `S > 0` ⇒ **SLACK-MEDIATED**: reflexive reweighting available (felt choice). The threshold at 0 is a foundation **posit**. Optional perceived slack `Sp`: `Sp ≤ 0 < S` = "stuck but capable" |

### 4.3 Conventions (not glyphs)

- **solid** = declared / executed; **dashed** = CONJECTURED bridge (drawn, labelled, never computed); **dotted** = annotation, correspondence, or "outside the candidate set X".
- **Reading order is a round trip.** Upper lane, read **left → right**: `W → S → I → ◇` (inbound / reconstruction). Turn at the actualization vertex `◇`. Lower lane, read **right → left**: `◇ → I⁺ → S → W` (outbound / realization). The lower lane is later causal time, not time reversal: in general `γ_t ≠ β_t⁻¹`, `δ_t ≠ α_t⁻¹`.
- **Lower-lane wires are red** and labelled `act` (policy → action) and `wake` (action → world record). Both exits of `◇` may be drawn; the gate's sign marks one **REALIZED** and the other *not taken this cycle* (dashed/grey). Executing a probe is itself an outbound act; its result returns on the upper lane as next cycle's observation — that is how `q? → q!` actually happens.
- **The loop closes through the world**, not inside the self: a grey dashed `feedback: next cycle t+1` arc from the lower-lane world item back to the upper-lane world column. It is dynamical feedback, never holonomy.
- **One cogito per diagram.** Another mind appears as world items (its visible wake) and as *contents of this I's field* (its reconstruction). Direct mind-to-mind arrows are forbidden: `M_t ↛ M̂^B_t`; always `M_t → a_t ↦ ω_t ⇝_B M̂^B_t`.
- **Loops** must be labelled *feedback*, *recurrence*, or *holonomy* (the last only when a transport law is declared).
- **No decorative ontology.** Colour, width, rings may aid reading; they may not silently create a mathematical distinction.
- **Complexity budget.** 3–7 top-level content nodes; at most one or two open nodes; short labels; the φ-chains in their own band. If the diagram needs a full-page legend it has failed to compress.

### 4.4 Status badges (optional)

A content node may carry a small badge `κ · φ · ρ · D` under its label. Badges are *read-offs*, never inputs; if a badge disagrees with the counting rule, the badge is wrong.

---

## 5. Reading rules (the four counts)

Given a diagram (or its serialization, §6):

**R1 — ρ (flow).** For each mode `k`, take the blue integration wires of that mode as a capacity graph. `C = MaxFlow(î → x)`. `ρ^k(x) = C/(1+C)`. Parallel routes add; a chain is limited by its thinnest wire. Apply any `⊕(α,β)` events to wire weights first.

**R2 — φ (count ⇒).** Follow `⇒` from `x`. If a ground `⊥` is reachable, `n` = length of the shortest such chain, `ε = Σ μ·(1−q)` over executed `q!` legs attached to nodes on that chain (capped so `ε + nδ ≤ 1`), and `φ = 1 − nδ − ε`. If no ground is reachable, **φ is undefined** and the diagram shows where the chain stops and which `q?` could close it. `q?` contributes nothing.

**R3 — D (count ▣).** Along `x`'s inbound mediation path, `D = (number of ▣) + (1 if the path delivers to î, 0 if it only moves Foc)`. This reproduces the foundation's named orders exactly: `S^sal→Foc` = 1, `S^cog→î` = 2, `S^som→S^cog→î` = 3.

**R4 — κ (read χ).** `κ(x) = χ` if `x` has a direct contact wire; otherwise `sup χ` over the world items in `σ(x)`; `0` if `σ(x)` is empty.

**R5 — class.** From `A(x)` and whether φ is defined (table in §2.3).

**R6 — S (read the sign).** At the actualization vertex, `S = M − Pressure` from the declared inputs. `S ≤ 0` ⇒ the automatic exit is REALIZED (contact-driven focus; passive descent of the local mismatch gradient; no Mode-B rewrite — note the foundation's caveat that *automatic is not the same as myopic*). `S > 0` ⇒ the slack-mediated exit is REALIZED (reflexive reweighting available). If `Sp` (perceived slack) is declared: `Sp ≤ 0 < S` reads "stuck but capable"; `S ≤ 0 < Sp` reads "over-certified". `M` and `Pressure` are open functions in the foundation; the diagram **declares** them and says so.

**R7 — what is never computed.** Dashed bridges (e.g. `anger → Pressure↑`, `S ≤ 0 → μ(q)↓`): drawn and labelled, never entering a number. The content of an action or wake (only its mode and its target are read). Any scalar combining the four coordinates.

**R8 — adequacy check.** Every discriminator `q` in the picture must leave a `neither → enlarge X` branch reachable; a content drawn dotted outside `X` with no probe reaching it is the diagram's reminder that identifiability ≠ adequacy.

---

## 6. Text serialization (the cross-model carrier)

A diagram is a list of statements, one per line, `#` for comments. This is the authoritative form; the picture is a rendering of it.

```
cogito  I
world   n  "label"
content x  "label"  [A=0|1]                 # default A=1
claim   c  "label"                          # a content used only as a chain link (hidden from tables)
sub     s  "label"                          # substrate vertex
tool    g  "label"                          # ground
wire    u -> v  [k=<mode>] [w=<0..1>]       # integration wire   (default k=0, w=1)
step    u => v                              # one verification step
probe   q? -> x  [mu=<0..1>]                # constructible, not executed
probe   q! -> x  [mu=<0..1>] [q=<0..1>]     # executed, result q(x)
contact n ~> x  [chi=<0..1>]                # contact wire
path    n -> s1 -> s2 -> I -> x             # inbound mediation path; tokens I / Foc allowed
event   u -> v  [k=] [alpha=] [beta=]       # imprinting event (applied before reading rho)
bridge  u -> v  "label"                     # CONJECTURED; drawn, never computed
source  x : y, z                            # sigma(x) = {y, z}
gate    X  M=<cap> P=<pressure> [Sp=<perceived>]  # turnaround; S=M-P
act     X -> a  "label" [mode=auto|B]       # outbound candidate action
wake    a -> n  "label"                     # action leaves world record for next cycle
delta   <value>                             # default 0.05
```

Rules: exactly one `cogito`; at most one `gate` per cycle; `probe` names ending in `?` are unexecuted, `!` executed; `path` is the only statement that may mention `Foc`; `bridge` endpoints need not be declared nodes; `act`/`wake` are the only lower-lane statements.

---

## 7. Zoom rule (compositionality)

A closed content node may be replaced by an **open circuit** with the same typed boundary ports whenever the circuit's semantics equals the node's:

`⟦circuit⟧ = ⟦node⟧ ⇒ ⟦C[node]⟧ = ⟦C[circuit]⟧` for every well-typed surrounding context `C[−]`.

With a tolerance: `d(⟦circuit⟧, ⟦node⟧) ≤ ε` gives ε-equivalence at the interface.

This is the only rule that lets a whole subsystem be drawn as a dot. It is **functoriality of the semantics map** `⟦·⟧` — a well-formedness requirement on the semantics, not a theorem derived from TLICA. It is stated as a rule, not a result. (v0.4 §63 called it a theorem; corrected here.)

Open a node only when its internals are load-bearing for the current claim. The internal circuit uses the same ten-glyph grammar; the grammar never changes with depth.

Division of labour, retained from v0.4: **EPIC governs the wires** (paths, provenance, probes, fibers); **TLICA governs the inside of opened nodes** (`G_t`, κ, φ, ρ, σ, S, μ, Mode-B rewrites where licensed). They meet at the node's boundary ports.

---

## 8. Worked example 1 — the dryer event

**Reading target.** Upper lane: the rival the self is most integrated with has no closed verification chain, and the only executed probe does not discriminate. Turnaround: pressure exceeded capacity, so the gate fired the *automatic* exit. Lower lane: the realized act is blame-and-redo; the act that would have closed the chain (running the probes) was drawn and not taken. One cause sits outside the candidate set. The wake returns as next cycle's world.

### 8.1 Serialization

```
# TLICA-EPIC v0.5 worked example 1 -- Dryer event / premature closure
# Reading target: the self-integrated hypothesis has no closed verification chain;
# the only executed probe does not discriminate; the discriminator is constructible
# but gated by a conjectured slack bridge.

delta 0.05
cogito  I

# --- world items (not-I) ---
world   n_garment  "damp garment"
world   n_other    "the other person"

# --- substrate vertices (mediation stages) ---
sub     S_sal  "salience gate"
sub     S_som  "somatic"
sub     S_cog  "cognitive"

# --- ground: verification tools in Tools_t ---
tool    g_obs  "direct observation"

# --- contents ---
content y   "clothes still damp"            A=1
content P   "my loading procedure works"    A=1
content H1  "other person ran it wrong"     A=1
content H2  "load/heat/time concern valid"  A=1
content H3  "omitted cause (outside X)"     A=0
content A   "anger / urgency"               A=1

# --- contact wires (kappa) ---
contact n_garment ~> y  chi=0.9
source  A : y                     # anger's source map runs through the garment contact
source  H1 : n_other              # H1 attributes to a not-contacted item
source  H2 : n_garment

# --- inbound mediation paths (D) ---
path    n_garment -> S_sal -> Foc -> y
path    n_garment -> S_cog -> I -> H1
path    n_garment -> S_cog -> I -> H2
path    n_garment -> S_som -> S_cog -> I -> A

# --- integration wires (rho), mode k=0 ---
wire    I  -> P   k=0 w=0.90      # a deeply integrated self-belief
wire    P  -> H1  k=0 w=0.70      # H1 hangs off P: "if my procedure works, it was them"
wire    I  -> y   k=0 w=0.10      # a fresh observation, barely integrated
wire    y  -> H2  k=0 w=0.60      # H2 hangs off the observation, not off the self
wire    I  -> A   k=0 w=0.50      # anger is moderately integrated

# --- verification chains (phi): one => per step, chain must reach a tool ---
step    y  => g_obs                           # n=1: seen directly
step    H1 => c1                              # "someone else ran it"
step    c1 => c2                              # "and ran it wrongly"
step    H2 => c3                              # "load exceeded spec"
claim   c1 "someone else ran it"
claim   c2 "...and ran it wrongly"
claim   c3 "load exceeded spec"

# --- probes ---
probe   q_obs! -> y   mu=1.0 q=1.0            # executed; confirms y, discriminates nothing
probe   q_chk? -> c2  mu=0.15                 # constructible: ask them / check cycle log
probe   q_man? -> c3  mu=0.15                 # constructible: manual / model number / load

# --- actualization vertex (turnaround I -> I+), lower lane ---
# M and P are declared inputs (open functions in the foundation). This cycle:
# anger raised pressure past capacity, so the gate is closed and the response is automatic.
gate    X  M=1.0 P=1.3                         # S = -0.3 <= 0  => AUTOMATIC
act     X -> a_auto "blame; re-run the dryer my way"            mode=auto
act     X -> a_B    "execute q_chk / q_man (check log, read manual)" mode=B
wake    a_auto -> n_other    "the other person hears the blame"
wake    a_B    -> n_garment  "garment re-run under a checked spec -> y_{t+1}"

# --- conjectured bridges (drawn dashed; never computed) ---
bridge  A -> X        "felt salience raises Pressure  [CONJECTURED map]"
bridge  X -> q_chk?   "S <= 0 lowers mu(q)  [CONJECTURED]"
bridge  X -> q_man?   "S <= 0 lowers mu(q)  [CONJECTURED]"
```

### 8.2 Picture (text form)

Read the top block left → right, turn at `<S>`, read the bottom block right → left.

```
WORLD N              SUBSTRATE S         SELF (inbound; == integration wires, width ~ w)        TURNAROUND
-------------------  ------------------  ----------------------------------------------------  ----------------
                                            ..H3..  omitted cause, OUTSIDE X (dotted, no wire)      M = 1.0
<> the other         [#] salience -> Foc    H1 <==(k0:0.70)== P <==(k0:0.90)====+                  P = 1.3
   person                                   |  other person    my procedure     |                S = -0.3 <= 0
   sigma(H1) -> here                        |  ran it wrong    works            |                => AUTOMATIC
   no contact wire   [#] cognitive -> I     v                              (O) I ==(Theta: I->I+)==> <S>
<> damp garment ~~~~~~~~~~(chi 0.9)~~~~~~~> y <------(k0:0.10)-----------------+                  /    \
                     [#] somatic -> cog     |  clothes still damp               |      realized  /      \ not taken
                                            v (k0:0.60)                        |     (S <= 0)  /        \ (S <= 0)
                                            H2  load/heat/time concern valid   v (k0:0.50)    /          \
                                            A   anger / urgency ...felt salience raises Pressure [CONJ.]...> <S>
                                                                                             /            \
<<< read right -> left  (outbound; -- = act / wake) <<<                                     v              v
<> the other person   <--wake-- [#] motor/speech <--act-- a  "blame; re-run it my way"   mode=auto  REALIZED
   hears the blame                   ^- - - - - - - - - - a' "execute q_chk / q_man"      mode=B    not taken
<> garment re-run, checked spec -> y_{t+1}   (dashed: would be next cycle's observation if a' were taken)
 ^
 '- - - feedback: next cycle t+1 (dynamical, not holonomy) - - - back to the WORLD column at the top

PHI-CHAINS   (count => to ground; each costs delta; q! adds mu(1-q); q? adds nothing)
   [q!]--> y  ==(-d)==> _|_ direct observation         n=1, eps=0   => phi(y) = 0.95
   H1 ==(-d)==> c1 ==(-d)==> c2 - - -> [q_chk?]        open, no ground => phi(H1) undefined  <- - [S<=0 lowers mu(q), CONJ.]
   H2 ==(-d)==> c3 - - -> [q_man?]                     open, no ground => phi(H2) undefined  <- - [same]

Mediation paths (grey in the figure):  garment -> salience -> Foc -> y            D = 1
                                       garment -> cognitive -> I -> H1, H2        D = 2
                                       garment -> somatic -> cognitive -> I -> A  D = 3
```

Rendered version: `diagrams/dryer_example.svg` / `.png` (same content, same numbers).

### 8.3 Read-off (output of the reference reader, Appendix A)

```
delta = 0.05   modes = ['0']
node   kappa phi     n   eps   rho     D   A  class                  pending q?
y      0.90  0.95    1   0.00  0:0.09  1   1  conscious-clear        
P      0.00  undef   -   undef 0:0.47  -   1  conscious-fuzzy        
H1     0.00  undef   -   undef 0:0.41  2   1  conscious-fuzzy        q_chk?
H2     0.00  undef   -   undef 0:0.09  2   1  conscious-fuzzy        q_man?
H3     0.00  undef   -   undef 0:0.00  -   0  unconscious-operative  
A      0.90  undef   -   undef 0:0.33  3   1  conscious-fuzzy        

actualization vertex X:  S = M - P = -0.30  ->  AUTOMATIC
  (S = 0 threshold is a foundation posit; M and P are declared inputs here)
  act a_auto   mode=auto REALIZED       blame; re-run the dryer my way
  act a_B      mode=B    not taken this cycle execute q_chk / q_man (check log, read manual)
  wake a_auto  -> n_other    the other person hears the blame
  wake a_B     -> n_garment  garment re-run under a checked spec -> y_{t+1}

CONJECTURED bridges (drawn, never computed):
  A --> X   felt salience raises Pressure  [CONJECTURED map]
  X --> q_chk?   S <= 0 lowers mu(q)  [CONJECTURED]
  X --> q_man?   S <= 0 lowers mu(q)  [CONJECTURED]
```

By hand, to show the counting:

- **ρ.** `H1`: route `î→P→H1`, bottleneck `min(0.90, 0.70) = 0.70` ⇒ `0.70/1.70 = 0.41`. `H2`: `î→y→H2`, `min(0.10, 0.60) = 0.10` ⇒ `0.09`. `P`: `0.90/1.90 = 0.47`. `A`: `0.33`. `H3`: no wire ⇒ `0`.
- **φ.** `y`: one `⇒` to ground, one `q!` with `q=1` ⇒ `ε = 0` ⇒ `φ = 1 − δ = 0.95`. `H1`, `H2`: chains end at a `q?` ⇒ no ground ⇒ **undefined** (not low — undefined).
- **D.** `y`: `S^sal → Foc` ⇒ 1. `H1`, `H2`: `S^cog → î` ⇒ 2. `A`: `S^som → S^cog → î` ⇒ 3 ⇒ expected fuzzy.
- **κ.** Only `y` has a contact wire (`χ = 0.9`). `A` inherits it via `σ(A) = {y}`. `σ(H1)` points at an uncontacted item ⇒ `κ(H1) = 0`.
- **S.** `M − Pressure = 1.0 − 1.3 = −0.3 ≤ 0` ⇒ AUTOMATIC. The `a` exit (blame; re-run it my way) is realized; the `a′` exit (execute the probes) is drawn and not taken. `M` and `P` are declared inputs; the threshold at 0 is a posit.

### 8.4 What the picture says

*Top lane.* The content with the highest ρ among the rivals (`H1`, 0.41) has an **open** φ-chain; its felt obviousness is ρ-driven, not φ-driven. The only executed probe lands on `y` and separates nothing between `H1` and `H2`. `H3` is dotted outside `X` with no probe reaching it, so the `neither → enlarge X` branch remains open.

*Turnaround.* Anger (D = 3, conscious-fuzzy, κ 0.9) is drawn with a dashed, labelled bridge to Pressure; the declared `M, P` give `S ≤ 0`; the automatic exit fires. Nothing in the gate reads H1's open chain — that is the point: **with `S ≤ 0` the open chain is behind the agent, not in front of it.**

*Bottom lane.* The realized act is blame-and-redo; its wake lands on the other person and comes back as next cycle's world. The exit that would have run the probes — and so turned `q?` into `q!` and closed H1's chain next cycle — is drawn and not taken.

> **Premature closure is the `S ≤ 0` exit with an open φ-chain behind it — and the picture shows both in one place.**

The self-coupling "felt resolution recurs" of v0.2 Example 1 needs no loop glyph: it is the triple *(high ρ on H1, open chain on H1, automatic exit)*, stable across cycles until either slack returns (`S > 0`) or the world forces a `q!` through the upper lane.

*Variant.* Change only `P=1.3` to `P=0.7` in the serialization: `S = +0.3`, the `a′` exit is REALIZED, the probes run, and next cycle's upper lane carries `q_chk!`/`q_man!` into H1's and H2's chains. Same picture, one declared number, the opposite story — which is what "automatic or slack-mediated depending on the situation" means operationally.

---

## 9. Worked example 2 — semantic wake (observer reconstruction), compact

**Reading target.** Two cogitos never share a diagram. The *observer* B is drawn; the actor's visible actions are world items; the actor's internal model `M` is a content of B's field that B **reconstructs** and never contacts. A semantic header is a world item that supplies a probe able to close B's chain.

### 9.1 Serialization

```
# TLICA-EPIC v0.5 worked example 2 -- Semantic wake (observer reconstruction), compact
# Two cogitos cannot share one diagram (one cogito leg per diagram), so the OBSERVER
# is drawn: B's field, with the actor's visible wake as world items. The actor's
# internal model M is a content of B's field that B reconstructs, never contacts.

delta 0.05
cogito  I                                   # observer B

world   n_a1  "actor's visible action 1"
world   n_a2  "actor's visible action 2"
world   n_h   "semantic header h: goal + invariant + next move"

sub     S_cog "cognitive"

tool    g_obs "direct observation"
tool    g_ask "ask the actor and compare"

content a1   "I saw action 1"                 A=1
content a2   "I saw action 2"                 A=1
content M    "the actor's model, as B reconstructs it"   A=1
content Mh   "the actor's model, reconstructed with the header"  A=1

contact n_a1 ~> a1  chi=0.8
contact n_a2 ~> a2  chi=0.8
source  M  : a1, a2
source  Mh : a1, a2, n_h

path    n_a1 -> S_cog -> I -> M
path    n_h  -> S_cog -> I -> Mh

wire    I -> a1  k=0 w=0.20
wire    I -> a2  k=0 w=0.20
wire    a1 -> M  k=0 w=0.50
wire    a2 -> M  k=0 w=0.50
wire    I -> Mh  k=0 w=0.20

# phi: the wake alone leaves M's chain open (many actor-models fit two actions);
# the header supplies a probe that can close it.
step    a1 => g_obs
step    a2 => g_obs
step    M  => c1
claim   c1 "these actions came from one coherent plan"
probe   q_fit? -> c1  mu=0.3                  # constructible: wait and see if a plan fits

step    Mh => c2
claim   c2 "the header's stated plan predicts the next action"
step    c2 => g_ask
probe   q_next! -> c2  mu=1.0 q=0.8           # executed: next action matched the header 80%
```

### 9.2 Read-off

```
delta = 0.05   modes = ['0']
node   kappa phi     n   eps   rho     D   A  class                  pending q?
a1     0.80  0.95    1   0.00  0:0.17  -   1  conscious-clear        
a2     0.80  0.95    1   0.00  0:0.17  -   1  conscious-clear        
M      0.80  undef   -   undef 0:0.29  2   1  conscious-fuzzy        q_fit?
Mh     0.80  0.70    2   0.20  0:0.17  2   1  conscious-clear
```

- `M` (reconstruction from the wake alone): ρ aggregates two parallel routes (`0.2 + 0.2 = 0.4 ⇒ 0.29`), but the chain is open ⇒ φ undefined; `B` has a model of the actor that is somewhat integrated and not verified — the "large reconstruction fiber" of v0.2 Example 2, drawn as an open chain.
- `Mh` (reconstruction with the header): the executed `q_next!` with `q = 0.8` closes the chain at `n = 2`: `φ = 1 − 0.10 − 0.20 = 0.70`. The header did not add action; it added a **probe that reaches ground**.

This is TE-011 (headers can shrink a reconstruction fiber) in counting form: the same picture, one more `q!`, one fewer undefined φ.

---

## 10. Research pointers (gated; not part of the standard)

### 10.1 Where a genuine perturbative expansion is licensed

The foundation's baseline law `ḃ = γ(f − b)` (File 3 §8.10) is linear with Green's function `G(t−s) = e^{−γ(t−s)} θ(t−s)` — an Ornstein–Uhlenbeck propagator. The nonlinearities on top of it (`ρ = R(G)` on the slow timescale, `V = τ‖Δ‖_ρ`, the slack gate at `S = 0`, any noise drive) are vertices. The Martin–Siggia–Rose / Janssen–De Dominicis response-field formalism gives a *bona fide* classical Feynman diagrammatics for exactly this class of stochastic dynamics (response lines, noise insertions, loop corrections to the mean orbit). It needs no phase and no quantum reading. **Status: pointer only; UNVERIFIED as a useful expansion for TLICA; promotion-gated.**

### 10.2 The aggregation fork

A path-sum `(I − λK)⁻¹` on the lived-I graph computes *total* flow; the foundation's ρ uses *max-flow* (bottleneck). These have different phenomenology (fragility vs. redundancy). The foundation says other aggregations are "compatible applied choices." Any diagram using a resolvent must say so in its `delta`/header line. **Default in this standard: max-flow.**

### 10.3 Contraction, not path product

v0.4 §68 (`W[γ] = ∏K_e ∏Φ_v`) is a weight along a *path*; on a graph with merges (every worked example has them) the correct object is a **tensor contraction** over internal wires with one index per leg. The v0.5 read-off rules are not a path product: ρ is a flow, φ is a chain count, so the issue does not arise in R1–R4. It arises the moment someone wants a *weighted sum over histories* — and then §10.1 is the right machinery.

### 10.4 String-diagram semantics

The glyph set with typed ports and boundary-preserving expansion is a string-diagram language. Choosing the semantic category (sets/functions for R1–R4; stochastic kernels for §10.1; linear maps for a contraction calculus) is what turns the grammar into a calculus; coherence then follows from the existing theory rather than needing a proof here. Möbius inversion on evidence subsets (v0.1 §21) and `log Z = connected diagrams` (v0.1 §18) are the same cumulant/moment relation and should be merged when that step is taken.

---

## 11. Claim ledger (v0.5 additions and corrections)

Status vocabulary: Disclosed / Corroborated / Observed / Conjectured / UNVERIFIED / Dark / Refuted. Conclusions inherit the weakest load-bearing premise. v0.1–v0.4 ledger items TE-001…TE-018 are retained unchanged except where listed.

| id | claim | status |
|---|---|---|
| TE-019 | Under the v0.5 legend, ρ, φ, κ, D of every content node are determined by the drawn graph alone (R1–R4), with no free parameter beyond δ and the declared aggregation. | **Disclosed** (constructive; Appendix A implements it) |
| TE-020 | `D = #▣ + [delivered to î]` reproduces the foundation's orders 1/2/3 exactly. | **Disclosed** (by inspection of File 3 §8.5.1 pathways) |
| TE-021 | An unexecuted probe `q?` contributes nothing to ε. | **Disclosed** as a standard rule, consistent with the pathway-state triplet (TE-006) |
| TE-022 | A chain that does not reach ground yields φ **undefined**, never "low." | **Disclosed** (File 3 §7.3 last paragraph) |
| TE-023 | Two cogitos never share one diagram; other minds enter as world items + reconstructed contents. | **Convention**, derived from the cogito anchor (one `ρ = 1`) |
| TE-024 | The zoom rule is functoriality of `⟦·⟧`, a well-formedness requirement, not a theorem. | **Correction** of v0.4 §63's label |
| TE-025 | The dryer example's readings (§8.3) follow from its serialization. | **Observed** (reader output reproduced) |
| TE-026 | Semantic headers shrink the reconstruction fiber iff they supply a probe that reaches ground (counting form of TE-011). | **Disclosed** in the formal model; real-world efficacy **UNVERIFIED** |
| TE-027 | The OU/MSR expansion of §10.1 is a useful perturbative calculus for TLICA dynamics. | **UNVERIFIED**; pointer only |
| TE-028 | The v0.5 legend improves human read-accuracy over v0.1 and v0.4. | **Conjectured / UNVERIFIED** (blinded readability task not run) |
| TE-029 | The actualization vertex's exit is determined by the sign of `S = M − Pressure` as declared. | **Disclosed** as a diagram rule; the gate itself is a foundation **posit** (File 3 §8.11), and `M`, `Pressure` are open functions supplied as inputs |
| TE-030 | Felt choice dissociates from behavioural output near `S = 0` (same action, flipped felt agency). | **UNVERIFIED** (foundation's own status); the diagram draws both exits so the claim is at least *representable* |
| TE-031 | Executing a probe is an outbound act whose result returns on the next cycle's upper lane. | **Disclosed** as a convention consistent with the v0.3 round trip; no new dynamics |
| TE-016 (revised) | TLICA–EPIC is mathematically novel. | **UNVERIFIED**; the glyph/port/expansion grammar is a string-diagram language and should be cited as such before any novelty claim |

**Foundation impact of this document: none.** Promotion candidates remain A (pathway triplet), B (φ-resolution ⇏ σ-resolution), C (typed update semantics), D (expandable vertices), all gated by F1–F12 (v0.2 Part XVI).

---

## 12. Supersession map

| version | what it contributed | status in v0.5 |
|---|---|---|
| v0.1 EPIC | fibers, kernels, 𝓘_Q, provenance covariance, holonomy, sheaf gluing, path measures, Wick licence, three interferences, dense ⊗□◇○● legend, three Graphviz examples | mathematics **retained** (§3); legend **superseded**; examples **redrawn** (§8–9) |
| v0.2 TLICA–EPIC | notation firewall, pathway triplet, typed arrows, 12 promotion gates, claim ledger TE-001…018 | **retained** (§2.7, §3, §11) |
| v0.3 dual-pass | W→S→I→S→W round trip, shell/core points, commuting compatibility squares, lifts, two-level aggregation | round trip **retained and made the reading order** (§4.3), with the turnaround promoted to a glyph (§4.2 #10); dual-trace grammar **superseded** (already by v0.4) |
| v0.4 hierarchical wires | wires + atomic/expandable vertices, ports, node-substitution, division of labour | glyph budget and expansion **retained** (§4, §7); "theorem" relabelled (TE-024); §68 path product **flagged** (§10.3); legend **superseded** (topology-only entries replaced by denotations) |
| **v0.5** | denotations + read-offs per glyph; four counting rules and one sign; round-trip reading order with an actualization vertex (automatic vs slack-mediated); text serialization; reference reader; two worked examples with computed readings | mathematical standard retained; v0.5.1 improves the front door and repairs grammar omissions |

Known housekeeping from the audit: v0.3 and v0.4 files still carry the title "v0.2.0"; v0.4 keeps Part XII live while Part XIII contradicts it; `scripts/math_terms.txt` pins *phase, gauge, transport, sheaf, manifold, fourier, amplitude* with glossary entries that disclaim the literal mathematical sense that EPIC uses, so promotion through gate F8 will need scope rungs on those pins; the EPIC branch is unmerged (12 commits ahead of `main`).

---

## 13. Final compression

> **Five visual families, ten reference glyphs. Four counts and one sign. One cogito. Read left→right, turn at the gate, read right→left. Dashed means drawn-not-computed. Open a node only when its insides matter.**

$$
\boxed{\;
\rho=\frac{C}{1+C},\ C=\mathrm{MaxFlow}(\hat\iota\to x)
\quad
\varphi = 1-(\#\Rightarrow)\,\delta-\textstyle\sum_{q!}\mu\,(1-q)
\quad
D = \#\blacksquare + [\to\hat\iota]
\quad
\kappa=\chi \text{ or } \sup_{\sigma(x)}\chi
\quad
S=M-\mathrm{Pressure}\ \begin{cases}\le 0 & \text{automatic}\\ >0 & \text{slack-mediated}\end{cases}
\;}
$$

The point was never that truth is an amplitude. The point is that a state the I cannot inspect directly is reached only through wires, steps, probes, and stages — and once each of those is a glyph with a factor, the picture *is* the shorthand.

---

## Appendix A — reference reader (Python 3, standard library only)

Save as `tlica_epic_read.py`; run `python3 tlica_epic_read.py example.tlica`. Implements R1–R5 and the imprinting event. It is a *reader*, not a model: it computes nothing the diagram does not declare.

```python
#!/usr/bin/env python3
"""
tlica_epic_read.py -- reference reader for TLICA-EPIC v0.5 diagram serializations.

Pure Python 3 standard library. No third-party packages.

A v0.5 diagram is a list of lines in the text grammar below. This script parses
the lines and computes, for every content node, the four readings that the
diagram is shorthand for:

    rho(x)   identity-correlation   = C/(1+C), C = max-flow from the cogito I to x
                                       over integration wires (per mode k)
    phi(x)   truth-indistinguishability
                                     = 1 - n*delta - eps, where n = number of
                                       verification steps (=>) on the chain from
                                       x to ground, eps = sum over EXECUTED probes
                                       on the chain of mu*(1-q). Undefined if the
                                       chain does not reach ground.
    kappa(x) contact                 = max chi over contact wires into x, or over
                                       the source-map ancestry of x if x has none.
    D(x)     mediation order         = number of substrate vertices on the inbound
                                       path from a world item to x.
    class(x) conscious-clear / conscious-fuzzy / latent / unconscious-operative,
             from (A(x), phi defined?)

Grammar (one statement per line; '#' starts a comment):

    cogito  I
    world   n  "label"
    content x  "label"  [A=0|1]
    claim   c  "label"  [A=0|1]            # a content used only as a chain link
    sub     s  "label"                     # substrate vertex
    (the token Foc may appear in a path; it is focus, not a node)
    tool    g  "label"                     # ground: a verification tool in Tools_t
    wire    u -> v  [k=<mode>] [w=<0..1>]  # integration wire (default k=0, w=1)
    step    u => v                         # one verification step (costs delta)
    probe   q? -> x [mu=<0..1>]            # constructible, NOT executed
    probe   q! -> x [mu=<0..1>] [q=<0..1>] # executed, with result q(x)
    contact n ~> x [chi=<0..1>]            # contact wire from world item n
    path    n -> s1 -> s2 -> I -> x        # inbound mediation path; D = #subs + [I on path]
    event   u -> v [k=] [alpha=] [beta=]   # imprinting event on a wire (applied)
    bridge  u -> v "label"                 # CONJECTURED modulation; never computed
    source  x : y, z                       # source map sigma(x) = {y, z}
    gate    X  M=<cap> P=<pressure> [Sp=<perceived>]
                                           # actualization vertex (the turnaround I -> I+).
                                           # S = M - P.  S <= 0: automatic;  S > 0: slack-mediated.
                                           # Sp (perceived slack) optional: Sp <= 0 < S = "stuck but capable".
    act     X -> a  "label" [mode=auto|B]  # outbound: policy -> action. Drawn; only the gate
                                           #   decides which mode is REALIZED this cycle.
    wake    a -> n  "label"                # action leaves a world record (next cycle's input)
    delta   <value>                        # default 0.05

Lower-lane statements (gate/act/wake) are declared, not computed, except the
gate's mode, which is read from the sign of S. Pressure and M are open functions
in the foundation; here they are declared inputs, and the reader says so.

Readings are returned as a dict and printed as a table.
"""
import re
import sys
from collections import defaultdict, deque

DELTA_DEFAULT = 0.05


# ---------------------------------------------------------------- parsing
def _kv(tokens):
    out = {}
    for t in tokens:
        if "=" in t:
            k, v = t.split("=", 1)
            out[k] = v
    return out


def parse(text):
    d = {
        "cogito": None, "world": {}, "content": {}, "sub": {}, "tool": {},
        "A": {}, "wire": [], "step": [], "probe": [], "contact": [],
        "path": [], "event": [], "bridge": [], "source": {}, "delta": DELTA_DEFAULT,
        "gate": {}, "act": [], "wake": [],
    }
    for raw in text.splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        kind, rest = (line.split(None, 1) + [""])[:2]
        m = re.match(r'(\S+)\s*(?:"([^"]*)")?\s*(.*)', rest)
        if kind == "cogito":
            d["cogito"] = rest.strip()
        elif kind in ("world", "content", "claim", "sub", "tool"):
            name, label, tail = m.group(1), m.group(2) or m.group(1), m.group(3)
            if kind == "claim":           # chain link: a content hidden from the table
                d["content"][name] = label
                d["A"][name] = int(_kv(tail.split()).get("A", 1))
                d.setdefault("hidden", set()).add(name)
                continue
            d[kind][name] = label
            if kind == "content":
                d["A"][name] = int(_kv(tail.split()).get("A", 1))
        elif kind == "wire" or kind == "event":
            u, v, tail = re.match(r"(\S+)\s*->\s*(\S+)\s*(.*)", rest).groups()
            kv = _kv(tail.split())
            if kind == "wire":
                d["wire"].append((u, v, kv.get("k", "0"), float(kv.get("w", 1))))
            else:
                d["event"].append((u, v, kv.get("k", "0"),
                                   float(kv.get("alpha", 0)), float(kv.get("beta", 0))))
        elif kind == "step":
            u, v = re.match(r"(\S+)\s*=>\s*(\S+)", rest).groups()
            d["step"].append((u, v))
        elif kind == "probe":
            q, x, tail = re.match(r"(\S+)\s*->\s*(\S+)\s*(.*)", rest).groups()
            kv = _kv(tail.split())
            d["probe"].append((q, x, q.endswith("!"), float(kv.get("mu", 1)),
                               float(kv.get("q", 0)) if "q" in kv else None))
        elif kind == "contact":
            n, x, tail = re.match(r"(\S+)\s*~>\s*(\S+)\s*(.*)", rest).groups()
            d["contact"].append((n, x, float(_kv(tail.split()).get("chi", 1))))
        elif kind == "path":
            d["path"].append([t.strip() for t in rest.split("->")])
        elif kind == "bridge":
            u, v, label = re.match(r'(\S+)\s*->\s*(\S+)\s*"?([^"]*)"?', rest).groups()
            d["bridge"].append((u, v, label))
        elif kind == "source":
            x, ys = re.match(r"(\S+)\s*:\s*(.*)", rest).groups()
            d["source"][x] = [y.strip() for y in ys.split(",") if y.strip()]
        elif kind == "gate":
            name, tail = (rest.split(None, 1) + [""])[:2]
            kv = _kv(tail.split())
            d["gate"][name] = {"M": float(kv["M"]), "P": float(kv["P"]),
                               "Sp": float(kv["Sp"]) if "Sp" in kv else None}
        elif kind == "act":
            X, a, label, tail = re.match(r'(\S+)\s*->\s*(\S+)\s*"([^"]*)"\s*(.*)', rest).groups()
            d["act"].append((X, a, label, _kv(tail.split()).get("mode", "?")))
        elif kind == "wake":
            a, n, label = re.match(r'(\S+)\s*->\s*(\S+)\s*"?([^"]*)"?', rest).groups()
            d["wake"].append((a, n, label))
        elif kind == "delta":
            d["delta"] = float(rest)
        else:
            raise ValueError("unknown statement: " + raw)
    if d["cogito"] is None:
        raise ValueError("diagram has no cogito leg")
    return d


# ---------------------------------------------------------------- rho
def apply_events(d):
    """Imprinting rule: w <- clip((1-beta) w + alpha (1-w)). Returns wires."""
    wires = {(u, v, k): w for (u, v, k, w) in d["wire"]}
    for (u, v, k, a, b) in d["event"]:
        w = wires.get((u, v, k), 0.0)
        wires[(u, v, k)] = min(1.0, max(0.0, (1 - b) * w + a * (1 - w)))
    return wires


def max_flow(adj, s, t):
    """Edmonds-Karp on a capacity dict adj[u][v]. Returns max-flow s->t."""
    cap = defaultdict(lambda: defaultdict(float))
    for u in adj:
        for v, c in adj[u].items():
            cap[u][v] += c
            cap[v]  # ensure key
    flow = 0.0
    while True:
        parent = {s: None}
        dq = deque([s])
        while dq and t not in parent:
            u = dq.popleft()
            for v, c in cap[u].items():
                if c > 1e-12 and v not in parent:
                    parent[v] = u
                    dq.append(v)
        if t not in parent:
            return flow
        # bottleneck
        f, v = float("inf"), t
        while parent[v] is not None:
            u = parent[v]
            f = min(f, cap[u][v])
            v = u
        v = t
        while parent[v] is not None:
            u = parent[v]
            cap[u][v] -= f
            cap[v][u] += f
            v = u
        flow += f


def rho_readings(d):
    wires = apply_events(d)
    modes = sorted({k for (_, _, k) in wires})
    I = d["cogito"]
    out = {}
    for x in d["content"]:
        vec = {}
        for k in modes:
            adj = defaultdict(dict)
            for (u, v, kk), w in wires.items():
                if kk == k:
                    adj[u][v] = w
            C = max_flow(adj, I, x)
            vec[k] = C / (1 + C)
        out[x] = vec
    return out, modes


# ---------------------------------------------------------------- phi
def phi_readings(d):
    """Follow => steps from x. Chain must end at a tool (ground)."""
    nxt = defaultdict(list)
    for (u, v) in d["step"]:
        nxt[u].append(v)
    exec_probes = defaultdict(list)   # node -> [(mu, q)]
    open_probes = defaultdict(list)   # node -> [mu]
    for (q, x, executed, mu, qval) in d["probe"]:
        if executed:
            exec_probes[x].append((mu, qval if qval is not None else 0.0))
        else:
            open_probes[x].append((q, mu))
    delta = d["delta"]
    out = {}
    for x in d["content"]:
        # BFS shortest chain to any tool
        best = None
        seen = {x: (0, [x])}
        dq = deque([x])
        while dq:
            u = dq.popleft()
            n, chain = seen[u]
            if u in d["tool"]:
                best = (n, chain)
                break
            for v in nxt[u]:
                if v not in seen:
                    seen[v] = (n + 1, chain + [v])
                    dq.append(v)
        if best is None:
            # chain is open; record where it stops and which q? could close it
            tips = [u for u in seen if not nxt[u]]
            pending = [q for u in seen for (q, _) in open_probes.get(u, [])]
            out[x] = {"phi": None, "n": None, "eps": None,
                      "open_at": tips, "pending": pending}
            continue
        n, chain = best
        eps = sum(mu * (1 - qv) for u in chain for (mu, qv) in exec_probes.get(u, []))
        eps = min(eps, 1 - n * delta)  # foundation: eps + n*delta <= 1
        out[x] = {"phi": 1 - n * delta - eps, "n": n, "eps": eps,
                  "chain": chain, "pending": []}
    return out


# ---------------------------------------------------------------- kappa, D
def kappa_readings(d):
    direct = defaultdict(float)
    for (n, x, chi) in d["contact"]:
        direct[x] = max(direct[x], chi)
    out = {}
    for x in d["content"]:
        if x in direct:
            out[x] = direct[x]
        else:
            # kappa_out(x) = sup over source map sigma(x); 0 if sigma empty
            srcs = d["source"].get(x, [])
            out[x] = max([direct.get(s, 0.0) for s in srcs] + [0.0])
    return out


def D_readings(d):
    """Mediation order = (#substrate vertices on the inbound path)
                       + (1 if the path delivers to the cogito I, 0 if it only
                          moves focus (token Foc)).
    This reproduces the foundation's named orders exactly:
        N -> S_sal -> Foc -> x        : 1 + 0 = 1   (salience capture)
        N -> S_cog -> I -> x          : 1 + 1 = 2   (cognitive)
        N -> S_som -> S_cog -> I -> x : 2 + 1 = 3   (somatic-then-cognitive)
    """
    out = {}
    I = d["cogito"]
    for p in d["path"]:
        x = p[-1]
        out[x] = sum(1 for s in p if s in d["sub"]) + (1 if I in p[:-1] else 0)
    return out


# ---------------------------------------------------------------- class
def classify(A, phi):
    if A == 1 and phi is not None:
        return "conscious-clear"
    if A == 1:
        return "conscious-fuzzy"
    if phi is not None:
        return "latent"
    return "unconscious-operative"


# ---------------------------------------------------------------- gate
def gate_readings(d):
    """S = M - Pressure (File 3 s8.11). S <= 0 -> automatic; S > 0 -> slack-mediated.
    The threshold at S = 0 is a foundation POSIT (named, not derived)."""
    out = {}
    for X, g in d["gate"].items():
        S = g["M"] - g["P"]
        mode = "automatic" if S <= 0 else "slack-mediated"
        note = ""
        if g["Sp"] is not None:
            if g["Sp"] <= 0 < S:
                note = "stuck-but-capable (perceived slack <= 0 < actual slack)"
            elif S <= 0 < g["Sp"]:
                note = "over-certified (perceived slack > 0 >= actual slack)"
        realized = [(a, label, m) for (XX, a, label, m) in d["act"] if XX == X]
        out[X] = {"S": S, "mode": mode, "note": note, "acts": realized}
    return out


# ---------------------------------------------------------------- driver
def read(text):
    d = parse(text)
    rho, modes = rho_readings(d)
    phi = phi_readings(d)
    kap = kappa_readings(d)
    D = D_readings(d)
    rows = []
    for x, label in d["content"].items():
        if x in d.get("hidden", set()):
            continue
        rows.append({
            "node": x, "label": label,
            "kappa": kap[x],
            "phi": phi[x]["phi"], "n": phi[x]["n"], "eps": phi[x]["eps"],
            "pending": phi[x]["pending"],
            "rho": rho[x], "D": D.get(x), "A": d["A"][x],
            "class": classify(d["A"][x], phi[x]["phi"]),
        })
    return d, rows


def fmt(v):
    return "undef" if v is None else ("%.2f" % v)


def main(path):
    text = open(path).read() if path != "-" else sys.stdin.read()
    d, rows = read(text)
    print("delta = %g   modes = %s" % (d["delta"], sorted({k for (_, _, k, _) in d['wire']})))
    hdr = "%-6s %-5s %-7s %-3s %-5s %-7s %-3s %-2s %-22s %s"
    print(hdr % ("node", "kappa", "phi", "n", "eps", "rho", "D", "A", "class", "pending q?"))
    for r in rows:
        rho_s = "/".join("%s:%.2f" % (k, v) for k, v in sorted(r["rho"].items()))
        print(hdr % (r["node"], fmt(r["kappa"]), fmt(r["phi"]),
                     "-" if r["n"] is None else r["n"], fmt(r["eps"]), rho_s,
                     "-" if r["D"] is None else r["D"], r["A"], r["class"],
                     ",".join(r["pending"])))
    gates = gate_readings(d)
    for X, g in gates.items():
        print("\nactualization vertex %s:  S = M - P = %.2f  ->  %s%s" % (
            X, g["S"], g["mode"].upper(), ("   [" + g["note"] + "]") if g["note"] else ""))
        print("  (S = 0 threshold is a foundation posit; M and P are declared inputs here)")
        for (a, label, m) in g["acts"]:
            tag = "REALIZED" if (m == "auto" and g["mode"] == "automatic") or (m == "B" and g["mode"] == "slack-mediated") else "not taken this cycle"
            print("  act %-8s mode=%-4s %-14s %s" % (a, m, tag, label))
        for (a, n, label) in d["wake"]:
            if any(a == aa for (aa, _, _) in g["acts"]):
                print("  wake %-7s -> %-10s %s" % (a, n, label))
    if d["bridge"]:
        print("\nCONJECTURED bridges (drawn, never computed):")
        for (u, v, label) in d["bridge"]:
            print("  %s --> %s   %s" % (u, v, label))


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "-")
```

## Appendix B — files in the transport bundle

```
TLICA_EPIC_v0.5.0_MASTER.md        this file (self-contained)
tlica_epic_read.py                 Appendix A as a file
examples/dryer.tlica               §8 serialization
examples/semantic_wake.tlica       §9 serialization
diagrams/legend.svg / .png         §4 as a one-page figure
diagrams/dryer_example.svg / .png  §8 as a figure, with the readings panel
diagrams/make_legend.py            generator for legend.svg
diagrams/make_dryer.py             generator for dryer_example.svg
diagrams/render.sh                 svg → png via headless Chromium (optional)
```

## Appendix C — minimal prompt for another model

> You are given TLICA_EPIC_v0.5.0_MASTER.md. Treat §2 as frozen foundation (do not alter), §4–§7 as the diagram standard, §6 as the serialization grammar, and Appendix A as the oracle for readings. When asked to diagram a situation: (1) write the serialization first; (2) run or hand-simulate R1–R5; (3) only then draw. Every dashed edge must be labelled CONJECTURED and must not enter any number. Never draw two cogitos. Never report a φ as "low" when its chain does not reach ground — report it as undefined and name the `q?` that would close it.
