# Formal ledger — Semantic Interoperability

Every equation or piece of notation that might appear in the manuscript is recorded
here with its **honest status** and its **non-claims**. The governing rule: a
formula in a philosophy paper is a claim, and a schematic formula that imitates rigor
it does not have is worse than prose (roadmap §5.1, Gate H5 — "equations only where
they clarify a structural claim rather than imitate rigor").

**Nothing in this ledger is validated.** The seeded entries are pointers to
expressions in the AI-assisted research note
[`this_is_water_semantic_interoperability_2026-08-09.md`](../../research/this_is_water_semantic_interoperability_2026-08-09.md).
The note itself marks these as schematic; several say so in as many words ("define
only schematically — not yet as a validated quantitative measure"). They are seeded
so the ledger knows what exists, **not** as an assertion that any of them is
correct, measurable, or publication-ready.

**Status vocabulary:** `definition` · `analogy` · `schematic model` · `conjecture` ·
`empirical proposal` · `boundary` (a stated non-identity) · `theorem` (reserved —
none yet). No entry may be labeled `theorem` or "validated" without a proof or a
calibrated empirical result that does not currently exist.

## Entry template

```
### F-NNN — <short name>

- **Expression:** $ ... $
- **Object type:** (map / relation / measure / schema / inequality / non-identity)
- **Symbol definitions & domains:** every symbol, its type, its domain.
- **Status:** definition | analogy | schematic model | conjecture | empirical proposal | boundary
- **Assumptions:** what must hold for the expression to mean anything.
- **Derivation / source:** where it comes from; is it derived or asserted?
- **Interpretation:** what it is meant to say, in one sentence.
- **Non-claims:** what it explicitly does NOT assert.
- **Known defects:** undefined terms, unmeasured quantities, hand-waving.
- **Verification status:** not validated | partially checked | validated (with how).
- **Publication-safe wording:** the sentence that may appear in the manuscript, if any.
```

## Seeded entries (pointers only — not validated)

### F-001 — Private representational mapping

- **Expression:** $L_i : \mathcal{W} \rightarrow \mathcal{R}_i$
- **Object type:** schematic map
- **Symbols:** $L_i$ person $i$'s learned mapping; $\mathcal{W}$ encountered world-structure; $\mathcal{R}_i$ person $i$'s internal representational space.
- **Status:** definition (schematic)
- **Source:** research note §2 (asserted, not derived).
- **Interpretation:** people build partly private internal representations of a shared world.
- **Non-claims:** not a validated cognitive or neural model; $\mathcal{W}, \mathcal{R}_i$ are not formally constructed spaces.
- **Verification status:** not validated.

### F-002 — Nonidentical representations

- **Expression:** $L_A(w) \neq L_B(w)$
- **Object type:** non-identity
- **Status:** definitional observation
- **Source:** research note §2.
- **Interpretation:** two people can occupy the same world with different internal representations.
- **Non-claims:** says nothing about how large or measurable the difference is.
- **Verification status:** not validated.

### F-003 — Encode / transmit / decode with invariant preservation

- **Expression:** $S \xrightarrow{E_A} m \xrightarrow{D_B} \widehat{S}_B$, acceptable when $\widehat{S}_B \sim_I S$
- **Object type:** schematic model + acceptance relation
- **Symbols:** $S$ source object; $E_A$ sender's encoding; $m$ message; $D_B$ receiver's decoding; $\widehat{S}_B$ reconstruction; $\sim_I$ agreement on declared invariant set $I$.
- **Status:** schematic model
- **Source:** research note §2.
- **Interpretation:** communication succeeds when the receiver reconstructs the load-bearing invariant, not the exact internal state.
- **Non-claims:** $\sim_I$ is not a defined metric; "invariant set $I$" is chosen, not derived.
- **Verification status:** not validated.

### F-004 — Weighted shared coverage

- **Expression:** $\mathrm{Cov}_{\Omega}(A,B) = \sum_{x \in \Omega} w(x)\,\mathbf{1}[\text{A and B share a usable representation of } x]$
- **Object type:** schematic measure
- **Symbols:** $\Omega$ target family of concepts/relations; $w(x)$ weight; indicator on shared usable representation.
- **Status:** schematic model — **the source explicitly says this is "not yet a validated quantitative measure."**
- **Source:** research note §3.
- **Non-claims:** $w(x)$ is unspecified; "usable common representation" is unoperationalized; the sum is not claimed to be computable or empirically fitted.
- **Known defects:** every term on the right-hand side is currently undefined for real humans.
- **Verification status:** not validated.

### F-005 — Coverage lowers expected translation cost (central conjecture)

- **Expression:** $\mathrm{Cov}_{\Omega}(A,B)\uparrow \;\Longrightarrow\; \mathbb{E}[\text{translation cost}]\downarrow$ (for communications whose load-bearing structure lies inside the covered region)
- **Object type:** conjectured implication
- **Status:** **conjecture / UNVERIFIED** as a quantitative human prediction (matches claim C-002).
- **Source:** research note §3.
- **Interpretation:** more shared coverage ⇒ cheaper faithful transport, on average, within the covered domain.
- **Non-claims:** not that coverage guarantees understanding; not a measured effect.
- **Verification status:** not validated — this is the paper's main empirical exposure.

### F-006 — New object as known object plus residual

- **Expression:** $\text{new object} = \text{known object} + \text{important residual}$
- **Object type:** heuristic schema
- **Status:** analogy / schematic
- **Source:** research note §5.
- **Interpretation:** a shared repertoire lets a novelty be expressed as "like X, except Y," inheriting prior work on X.
- **Non-claims:** "$+$" is not an algebraic operation; purely expository.
- **Verification status:** not validated.

### F-007 — Intrapersonal vs interpersonal function

- **Expression:** intrapersonal: gain alternatives to inspect one's own frame; interpersonal: gain shared representations to transport frames between minds.
- **Object type:** conceptual schema (two-row array in source)
- **Status:** schematic distinction
- **Source:** research note §6.
- **Interpretation:** liberal education has both a self-directed and a between-minds function; Paper I foregrounds the interpersonal one.
- **Non-claims:** not attributed to Wallace's text; an author-level extension.
- **Verification status:** not validated.

### F-008 — The truth boundary (load-bearing)

- **Expression:** $\text{shared language} \neq \text{shared truth}$; $\quad \text{communicability} \neq \text{correctness}$; $\quad \text{interoperability is not truth}$
- **Object type:** non-identity / boundary
- **Status:** **boundary** — the paper's load-bearing non-claim (matches C-006).
- **Source:** research note §7, §12.
- **Interpretation:** high semantic interoperability can coexist with shared falsehood; interoperability is a communicative virtue, not an epistemic one.
- **Non-claims:** does not say shared representation is worthless; says it is not sufficient for truth.
- **Verification status:** not a claim requiring empirical validation; must be stated and defended in prose.

### F-009 — Compact formulation

- **Expression:** $\text{liberal education} \approx \text{shared conceptual coverage} \rightarrow \text{lower semantic translation cost} \rightarrow \text{higher-probability faithful perspective transport}$
- **Object type:** compressed conjecture chain
- **Status:** conjectured interpretive formulation (bundles F-004, F-005, and the boundary F-008).
- **Source:** research note §12.
- **Interpretation:** the paper's thesis in one line, subject to the boundary "interoperability is not truth."
- **Non-claims:** the "$\approx$" and "$\rightarrow$" are conceptual, not quantitative; the whole chain inherits F-005's UNVERIFIED status.
- **Verification status:** not validated.

### F-010 — Round-trip reconstruction test (understanding vs. signal-echo)

- **Expression:** $x_A \xrightarrow{\text{message}} \widehat{x}_B \xrightarrow{\text{paraphrase}} \widehat{x}_A$, success when $\widehat{x}_A \sim_I x_A$
- **Object type:** schematic test + acceptance relation — the **round-trip closure of F-003** (F-003 is the one-way half; this sends it back).
- **Symbols:** $x_A$ sender's object; message; $\widehat{x}_B$ receiver's reconstruction; paraphrase-back; $\widehat{x}_A$ returned object; $\sim_I$ agreement on the declared load-bearing invariant set $I$.
- **Status:** schematic model / empirical proposal — **not validated.**
- **Assumptions:** the invariant set $I$ is **declared in advance** (else the test is unfalsifiable); some judge can assess $\sim_I$.
- **Derivation / source:** extends F-003 (research note §2); the round-trip *framing* is AI-suggested (ChatGPT via Leah, 2026-08-12) and is **pending Leah's ownership** — it is a candidate test, not an owned result.
- **Interpretation:** understanding — as opposed to mere signal-echo — is evidenced when the sender's idea survives a trip through the receiver *and back*, preserving the structure the sender declared load-bearing.
- **Non-claims:** does not define $\sim_I$ as a metric; does not claim a fluent parrot can never pass; not a validated experimental protocol.
- **Known defects:** $I$ is the entire crux and is currently a **checklist, not a measure** — candidate members: *proposition · analogy · causal structure · claim-type · confidence · source-or-reason · relevant non-claims*. The failure mode to design against: a purely *lexical* paraphrase passing without any structure transported (signal-echo).
- **Verification status:** not validated.
- **Publication-safe wording:** [ AWAITING LEAH — only after she owns the test and its invariant set ]
