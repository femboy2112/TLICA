# TLICA–EPIC Diagram Standard
## Hierarchical wires, expandable vertices, and the folded world–substrate–self cycle

**Version:** v0.4-draft  
**Date:** 2026-10-03  
**Status:** research/application diagram standard; foundation-extension candidate only.  
**Foundation impact:** none.  
**Author:** Leah. AI-assisted formalization and notation audit.

---

# 0. One-sentence standard

TLICA–EPIC diagrams are **ordinary directed wire graphs whose vertices may be either atomic points or recursively expandable EPIC-integrated circuits**.

That is the core standard.

The diagram does **not** use one class of wire for EPIC and another class of wire for TLICA.

Wires remain wires.

The extra expressive power lives in the vertices.

---

# 1. Why this replaces the earlier dual-trace picture

An earlier draft treated a connection between two structured objects as if it contained two parallel geometries:

- an outer EPIC shell path;
- an inner TLICA core trace.

That is visually expensive and conceptually unnecessary.

The cleaner formulation is:

$$
\boxed{
\text{one graph of wires}
+
\text{vertices with variable internal resolution}.
}
$$

EPIC operates over paths in the graph.

TLICA supplies internal structure for whichever vertices require it.

A TLICA trace therefore usually lives **inside an expanded vertex**, not as a second line running beside every external wire.

This makes the formalism much closer to the economy of Feynman diagrams:

- edges remain edges;
- vertices remain interaction/update sites;
- a vertex may be expanded when its internal mechanism is load-bearing.

---

# 2. The three visual primitives

## 2.1 Wire

A wire is a directed edge

$$
e:u\to v.
$$

Its drawing is simply

~~~text
u ─────────→ v
~~~

A wire may carry a type label such as

$$
\mathrm{obs},
\quad
\mathrm{update},
\quad
q!,
\quad
\mathrm{policy},
\quad
\mathrm{act},
\quad
\mathrm{wake}.
$$

The **arrow** gives direction.

The **label** gives semantics.

Line style may encode epistemic status, but not a second hidden ontology.

Recommended convention:

- solid = declared/used relation;
- dashed = conjectured or optional bridge;
- dotted = annotation/correspondence only.

---

## 2.2 Atomic point

An atomic point is a vertex whose internal decomposition is not load-bearing for the current diagram.

Write it as

$$
\bullet.
$$

Formally, an atomic point may still have a semantic map/operator

$$
\Phi_v,
$$

but the diagram does not expose its factorization.

Atomic does **not** mean physically or cognitively simple.

It means:

> treated as an effective point at this resolution.

---

## 2.3 EPIC-integrated circuit node

An integrated node is an open internal circuit presented externally as one vertex.

Write schematically

$$
\boxed{\mathbb V_v}
$$

or visually as a bounded mini-circuit.

Formally:

$$
\boxed{
\mathbb V_v
=
(
P_v^-,
H_v,
P_v^+,
\iota_v^-,
\iota_v^+
)
}
$$

where:

- \(P_v^-\): input boundary ports;
- \(P_v^+\): output boundary ports;
- \(H_v\): internal directed graph/circuit;
- \(\iota_v^-\): attachment of external input ports to \(H_v\);
- \(\iota_v^+\): attachment of \(H_v\) to external output ports.

The internal graph \(H_v\) may itself contain atomic points **or further integrated nodes**.

Hence the representation is recursive:

$$
\boxed{
\text{circuit inside circuit inside circuit}\;\cdots
}
$$

to whatever depth is required.

---

# 3. Port graph rather than blob graph

For rigor, wires connect **ports**, not vague object interiors.

Let each vertex \(v\) have a finite set of ports

$$
P_v=P_v^-\sqcup P_v^+.
$$

An edge is typed by a source output port and target input port:

$$
e:
p_u^+\to p_v^-.
$$

This lets one integrated node expose multiple inputs/outputs without making the diagram ambiguous.

At coarse resolution, ports may be suppressed visually when there is only one obvious connection.

---

# 4. Semantic interpretation

The diagram syntax is intentionally category-agnostic.

A concrete application chooses a semantic category \(\mathcal C\).

Examples include:

- sets and functions;
- vector spaces and linear maps;
- measurable spaces and stochastic kernels;
- smooth manifolds and smooth maps;
- relations;
- operator spaces.

A semantics map

$$
\llbracket\cdot\rrbracket
$$

assigns wires and nodes mathematical meaning in \(\mathcal C\).

For a vertex \(v\),

$$
\llbracket v\rrbracket
:
X_{P_v^-}
\to
X_{P_v^+}
$$

may be deterministic, stochastic, relational, or operator-valued according to the application.

The diagram standard does not force one universal mathematical substrate.

---

# 5. Integrated-node semantics

The internal circuit \(H_v\) induces an effective boundary behavior

$$
\boxed{
\Phi_v
=
\llbracket H_v\rrbracket.
}
$$

Thus the integrated node may be used externally exactly where an atomic effective vertex carrying \(\Phi_v\) could be used.

This is the formal meaning of:

> the circuit is a point from the outside.

---

# 6. Vertex substitution theorem

Let \(C[-]\) be any larger diagram context containing a vertex hole.

Suppose an atomic/effective vertex \(v\) and expanded circuit \(H_v\) have the same boundary ports and the same semantics:

$$
\llbracket v\rrbracket
=
\llbracket H_v\rrbracket.
$$

Then compositional semantics gives

$$
\boxed{
\llbracket C[v]\rrbracket
=
\llbracket C[H_v]\rrbracket.
}
$$

This is the core zoom invariant.

### Interpretation

If two representations have the same boundary behavior, one may replace the other without changing the semantics of the surrounding diagram.

This licenses arbitrary zoom:

~~~text
────●────
~~~

may become

~~~text
────( internal circuit )────
~~~

without changing the larger argument, provided the interface contract is preserved.

---

# 7. Approximate substitution

Real applications may only preserve boundary behavior approximately.

For an appropriate discrepancy \(d\), define

$$
\epsilon_v
=
d(
\llbracket v\rrbracket,
\llbracket H_v\rrbracket
).
$$

If

$$
\epsilon_v\le\varepsilon
$$

for a declared tolerance \(\varepsilon\), the collapsed and expanded vertices are **\(\varepsilon\)-equivalent at the interface**.

This prevents “zoom equivalence” from becoming hand-waving.

---

# 8. EPIC lives on graph paths

Let the external diagram be a directed graph

$$
G=(V,E).
$$

An EPIC path is an ordinary composable path

$$
\gamma=e_n\circ\cdots\circ e_1.
$$

Its semantics is

$$
\llbracket\gamma\rrbracket
=
\llbracket e_n\rrbracket
\circ\cdots\circ
\llbracket e_1\rrbracket
$$

with vertex factors inserted according to the chosen formalism.

EPIC therefore does **not** require a special “outer” line.

The ordinary wires of the diagram are the EPIC path substrate.

---

# 9. Internal TLICA dynamics live in expanded nodes

When a vertex represents a TLICA-relevant system, its internal graph may expose the required TLICA structure.

For a self node \(I\), the internal circuit may include, where load-bearing:

- \(G_t\): lived-I structure;
- \(\kappa\): contact;
- \(\phi\): toolkit-relative truth-indistinguishability;
- \(\rho\): identity-correlation;
- \(\sigma\): source-map adequacy diagnostic;
- \(S_t\): slack margin;
- \(\mu_t(q)\): application-level probe availability;
- \(Q_t^{\mathrm{exec}}\): executed probe family;
- live rivals;
- policy \(\pi_t\);
- Mode-B rewrite operations where foundation semantics actually license them.

These objects are **not required in every self node**.

Rule:

$$
\boxed{
\text{expand only what is load-bearing to the current claim.}
}
$$

---

# 10. The substrate node is also expandable

The substrate \(S\) is not an inert wire.

At coarse scale:

$$
W\to S\to I.
$$

At higher resolution, \(S\) may expand into a circuit containing, where justified:

- sensory transduction;
- focus;
- salience;
- affective forcing;
- slack;
- motor realization;
- probe gating.

Again, these are typed quantities, not interchangeable synonyms.

---

# 11. World nodes may also be integrated

A world/environment vertex \(W\) may remain atomic when only its boundary effects matter.

It may be expanded when the internal environmental mechanism is relevant.

Examples:

- appliance mechanics in the dryer example;
- institutional rules in the training example;
- other-agent reconstruction dynamics in semantic wake analysis.

Thus **world, substrate, and self are roles, not visual node species**.

Each can be:

$$
\bullet
\qquad\text{or}\qquad
\mathbb V.
$$

---

# 12. Canonical two-pass layout

For self-world dynamics, use the same ordinary wire syntax but a canonical folded layout.

Inbound:

$$
W_t
\xrightarrow{\alpha_t}
S_t
\xrightarrow{\beta_t}
I_t.
$$

Internal turnaround:

$$
I_t
\xrightarrow{\Theta_I}
I_t^+.
$$

Outbound:

$$
I_t^+
\xrightarrow{\gamma_t}
S_{t+1}
\xrightarrow{\delta_t}
W_{t+1}.
$$

Visual reading:

~~~text
          reconstruction / inbound

W_t ─────────→ S_t ─────────→ I_t
                              │
                              │ Θ_I
                              ▼
W_{t+1} ←──── S_{t+1} ←──── I_t^+

           realization / outbound
~~~

Read clockwise.

The right-to-left lower lane is later in causal time.

It is not time reversal.

---

# 13. No inverse fallacy

In general,

$$
\boxed{
\gamma_t\neq\beta_t^{-1},
\qquad
\delta_t\neq\alpha_t^{-1}.
}
$$

Inbound maps reconstruct/internalize.

Outbound maps realize/control.

Their opposite visual directions encode different causal roles, not algebraic inversion.

---

# 14. Minimal reading rule

A reader should need only four facts:

1. **wire** = directed relation/transport;
2. **point** = internals suppressed;
3. **circuit node** = internals expanded;
4. **top then bottom** = inbound reconstruction, then outbound realization.

Everything else belongs in local labels or the node's internal circuit.

This is the desired Feynman-like economy.

---

# 15. Feynman analogy — exact and limited

The useful analogy is:

| Feynman-style role | TLICA–EPIC role |
|---|---|
| line / propagator | directed wire / path |
| vertex | atomic point or integrated circuit node |
| external leg | boundary wire / observation or action channel |
| vertex factor | effective boundary semantics \(\Phi_v\) |
| expanded interaction subgraph | expanded integrated node \(H_v\) |
| diagram composition | graph composition / circuit plugging |

The critical difference is that TLICA–EPIC explicitly permits a vertex to expose a recursively structured internal circuit as part of the standard notation.

The analogy does **not** imply quantum mechanics.

---

# 16. Path aggregation with integrated vertices

For a path

$$
\gamma:E\leadsto A
$$

through edges and vertices, a generic finite weight may factor as

$$
\boxed{
W[\gamma]
=
\prod_{e\in\gamma}K_e
\prod_{v\in\gamma}\Phi_v
}
$$

where:

- \(K_e\): edge/transport contribution;
- \(\Phi_v\): effective node contribution.

If a node is expanded,

$$
\Phi_v
=
\llbracket H_v\rrbracket.
$$

If its internal behavior is itself a path sum,

$$
\boxed{
\Phi_v(b\mid a)
=
\sum_{\lambda:a\leadsto b\text{ in }H_v}
w_v[\lambda].
}
$$

Therefore the “path integral inside a path integral” intuition becomes:

> the global path sum runs over the external graph; any structured vertex may contribute an effective factor obtained by summing/integrating over its own internal admissible histories.

This is cleaner than drawing a second trace beside every wire.

---

# 17. Recursive integration

Because \(H_v\) may itself contain integrated nodes,

$$
\Phi_v
$$

may recursively depend on lower-level effective factors.

Schematically:

$$
\Phi_v
=
F_v(
K_{e_1},\ldots,K_{e_m},
\Phi_{v_1},\ldots,\Phi_{v_k}
).
$$

This creates a compositional hierarchy:

$$
\boxed{
\text{global circuit}
\supset
\text{integrated node}
\supset
\text{subcircuit}
\supset
\cdots
}
$$

without changing the graph grammar.

---

# 18. Probe notation

Probe state should not require a new geometric primitive.

Use an ordinary wire to an ordinary or structured probe node.

Recommended labels:

$$
q?
=
\text{constructible / contemplated but unexecuted},
$$

$$
q!
=
\text{executed discriminator}.
$$

For example:

~~~text
H ─────→ q! ─────→ H'
~~~

or, if the probe mechanism itself matters, expand \(q!\) as an integrated circuit.

Again: **node complexity, not wire complexity**.

---

# 19. Feedback and recurrence

A feedback loop is just a directed wire returning to an earlier port/node.

It must be labeled by semantics:

- feedback;
- recurrence;
- self-coupling;
- transport holonomy, when a genuine transport law is defined.

Do not introduce a special loop glyph unless it adds information.

A loop is topology first, annotation second.

---

# 20. Status encoding

Epistemic status should remain orthogonal to graph structure.

Recommended:

- solid wire/node outline = declared or executed;
- dashed wire/node outline = conjectured / proposed;
- annotation tag = Observed, Conjectured, UNVERIFIED, Refuted, etc.

Do not encode “truth” by thicker wires, brighter color, or larger nodes.

---

# 21. The standard graph object

A diagram may be represented as

$$
\boxed{
\mathfrak D
=
(
V,
E,
P,
\tau_V,
\tau_E,
H,
\partial,
\llbracket\cdot\rrbracket,
\Pi
).
}
$$

Where:

- \(V\): vertices;
- \(E\): directed wires;
- \(P\): boundary ports;
- \(\tau_V\): vertex type/role;
- \(\tau_E\): edge semantic labels;
- \(H(v)\): optional internal circuit for integrated vertex \(v\);
- \(\partial\): port attachment/interface data;
- \(\llbracket\cdot\rrbracket\): semantic interpretation;
- \(\Pi\): provenance/source ancestry where relevant.

For atomic \(v\),

$$
H(v)=\varnothing
$$

at the displayed resolution.

For integrated \(v\),

$$
H(v)\neq\varnothing.
$$

---

# 22. Node-role typing

The node role is separate from whether the node is atomic or integrated.

A node may have role:

$$
W,\;S,\;I,\;q,\;\eta,\;\text{source},\;\text{observer},\ldots
$$

and display state:

$$
\mathrm{atomic}
\quad\text{or}\quad
\mathrm{integrated}.
$$

Thus:

$$
\tau_V(v)
=
(\text{role},\text{resolution state},\text{claim status}).
$$

This prevents “self node” from becoming a special shape that has to be relearned visually.

---

# 23. Diagram normalization

Before publishing or comparing diagrams, normalize them.

### N1 — wire preservation

If two diagrams express the same external connectivity, their wires should remain topologically identical unless a real causal/inferential difference is intended.

### N2 — node expansion only

Refinement should preferentially replace a point by an integrated circuit, not duplicate every edge into parallel shell/core traces.

### N3 — boundary preservation

Expansion must preserve declared input/output ports.

### N4 — semantic preservation

If the expanded circuit is claimed equivalent to the point, verify

$$
\llbracket H_v\rrbracket
=
\llbracket v\rrbracket
$$

or state an error bound.

### N5 — edge typing

Every non-obvious wire gets a short semantic label.

### N6 — no decorative ontology

Color, line width, rings, and shapes may aid reading but may not silently introduce new mathematical distinctions.

---

# 24. Complexity budget

The standard explicitly optimizes for glance-readability.

A normal Level-1 diagram should usually show:

- no more than 3–7 visible top-level nodes;
- ordinary wires;
- at most one or two expanded nodes;
- short edge labels;
- a tiny legend.

If understanding requires a full-page legend, the diagram has failed to compress the model.

---

# 25. Three resolution levels

## L0 — graph topology

Only points and wires.

Use for conceptual orientation.

## L1 — integrated-node graph

Expand only load-bearing vertices.

This is the default working representation.

## L2 — internal circuit

Focus on a single integrated node and expose its TLICA/EPIC mechanism.

If necessary, recurse further.

The grammar is unchanged at every level.

---

# 26. Core theorem of the standard

The standard's central compositional invariant is not a shell/core commuting square.

It is **substitution invariance**.

### Theorem — semantic node substitution

If two nodes/circuits \(A\) and \(B\) have the same typed boundary and

$$
\llbracket A\rrbracket
=
\llbracket B\rrbracket,
$$

then for any well-typed surrounding diagram context \(C[-]\),

$$
\boxed{
\llbracket C[A]\rrbracket
=
\llbracket C[B]\rrbracket.
}
$$

This is what makes the notation scalable.

A complex TLICA system may be treated as a point until its internals matter.

---

# 27. What becomes simpler

The prior standard tried to encode four independent dimensions visually:

- macroscopic position;
- inbound/outbound pass;
- shell/core geometry;
- line semantics.

The revised standard removes shell/core from the edge grammar.

Now:

| Visual dimension | Meaning |
|---|---|
| connectivity / wire | relation/path |
| arrow direction | causal/inferential direction |
| upper/lower lane | inbound/outbound phase |
| node expansion | hidden vs exposed internal structure |
| short label | edge semantics |
| dashed/solid | claim/execution status |

This is materially easier to decode.

---

# 28. TLICA-specific round-trip semantics

For the canonical agent cycle:

$$
W_t
\xrightarrow{\mathrm{obs}}
S_t
\xrightarrow{\mathrm{uptake}}
I_t
\xrightarrow{\Theta_I}
I_t^+
\xrightarrow{\mathrm{policy}}
S_{t+1}
\xrightarrow{\mathrm{act}}
W_{t+1}.
$$

At L0, all six states may be points.

At L1, perhaps only \(I_t\) and \(S_t\) are expanded.

At L2, one may open \(I_t\) to show:

$$
G_t
\to
\{\kappa,\phi,\rho,\sigma,\text{rivals},Q^{\mathrm{exec}}\}
\to
\pi_t.
$$

The external wiring does not change.

That is the standard's most important visual invariant.

---

# 29. EPIC and TLICA roles

The standard cleanly separates responsibilities.

## EPIC

EPIC primarily governs:

- paths through the graph;
- candidate endpoints;
- provenance;
- path weights;
- ambiguity fibers;
- probe structure;
- external composition.

## TLICA

TLICA primarily governs:

- internal state of TLICA-relevant integrated nodes;
- identity-correlation structure;
- contact and toolkit-relative truth-indistinguishability;
- source-map diagnostics;
- slack and Mode-B dynamics where licensed;
- policy-relevant internal transformation.

They interact through node boundary semantics.

They do not require separate edge universes.

---

# 30. Foundation-extension status

The likely foundation-worthy candidate is now narrower and cleaner:

> **TLICA diagrams may admit recursively expandable effective points whose internal circuits preserve a typed boundary contract.**

That is a notation/compositionality principle.

It should be promoted only if:

1. it recurs across independent applications;
2. it prevents real ambiguities;
3. a holdout application benefits;
4. the substitution invariant can be maintained;
5. it does not impose false mechanistic decomposition.

EPIC path sums, Feynman aesthetics, and particular internal node designs remain application/research tools.

---

# 31. Final standard

The compact standard is:

$$
\boxed{
\textbf{Wires are wires. Nodes are points or integrated circuits.}
}
$$

Then:

$$
\boxed{
\textbf{follow the wires; open a node only when its internals matter.}
}
$$

For TLICA agent cycles:

$$
\boxed{
\textbf{read the upper path inward, transform at the self, read the lower path outward.}
}
$$

And for rigor:

$$
\boxed{
\textbf{expansion must preserve the node's typed boundary semantics.}
}
$$

That is the standard.
