# Formal contract and first results

**Scope:** finite mathematical objects and a research design. The social interpretation is an application-level hypothesis. No novelty claim is made for ordinary set intersection, Pareto order, or three-valued logic.

## 1. Task-indexed representations

Let `d` specify an episode, participating people, affected outsiders, time horizon, contemplated decision, and evidence boundary. Person `i` has a history `h_i`, presently available repertoire `T_i`, commitments `v_i`, and a provisional task representation `M_i^d`. These are distinct: an observed response does not uniquely identify its developmental history.

A cultural atlas proposes contextual information relevant to constructing or questioning `M_i^d`; it does not assign `M_i^d` from a region or genre. The participant can reject the proposed interpretation. A dynamic model might later describe changes in `(h_i,T_i,M_i^d)` under encounters, but no update law or cultural steady state is estimated here.

An episode can be encoded as a directed typed graph `G_i^d` over declared agents, resources, acts, and consequences. A transport contract gives a node map `f` and specifies relation meanings. The prototype checks whether each declared source edge `(a,r,b)` has a target edge `(f(a),r,f(b))`. Its scope is the supplied normalized graph. It neither discovers the normalization nor verifies its semantic or causal adequacy.

Require injectivity on the selected source graph, disclose target extras, and reject the empty graph as a fidelity witness. For partial transports, first identify the subgraph and omitted relations explicitly. No silent pruning to obtain a match is permitted. A relation named “causes” is still only a supplied annotation until supported by causal evidence.

**Result F1 — structural matching does not entail preference compatibility.** Consider a common world with exactly two feasible allocations `x` and `y`. Both participants know its complete transition structure. A accepts only `x`, B only `y`. The identity transport preserves every causal relation, but `{x} intersect {y}` is empty. This is an exact counterexample to the claim that sufficient mutual understanding necessarily yields a mutually acceptable option. The fixture `shared_map_real_conflict` instantiates it. It does not refute the possibility of expanding the option space.

## 2. A conditional feasible set

For a finite nonempty catalog `O`, define predicates on options:

- `R(o)`: declared reality/physical/operational conditions;
- `H(o)`: declared standing, safety, and affected-third-party requirements;
- `A_i(o)`: participant i's stated minimum acceptability conditions;
- `C_i(o)`: explicit permission for the specified proposed step.

The catalog-relative permissible set is

```
F = {o in O : R(o) and H(o) and, for every i, A_i(o) and C_i(o)}.
```

`A_i` and `C_i` are not the same. The model may predict that an option satisfies a floor while its owner withholds permission. Neither is a measurement of happiness. `H` is not derivable from preference aggregation; its normative basis and affected population must be declared and scrutinized.

The instrument never removes gates to improve a score. A blocking set is explanatory, not a recommendation to abandon a right or pressure a refusal.

## 3. Partial evidence: certified and possible sets

Each required gate is recorded as true, false, or unknown. These are evidence states *inside the supplied exercise*, not TLICA phi values. Source status is a separate condition for accepting a known gate value; a required unverified, disputed, or ablated source makes that gate unknown. Multiple references are jointly required here, not independent votes.

Define:

```
F_minus = options whose every required gate is known true
F_plus  = options with no required gate known false
pending = F_plus minus F_minus
rejected = O minus F_plus
```

**Result F2 — conditional sound bounds.** If every known true/false gate is correct and all required gates are represented, every completion of the unknown gates has a permissible set `F_completion` satisfying

```
F_minus subseteq F_completion subseteq F_plus.
```

Proof: all gates of an `F_minus` member remain true in every completion. A candidate outside `F_plus` already has a false required gate and cannot become permissible by filling unknowns. This is a conditional theorem, not a certificate that the recorded premises describe the real world. Omitted stakeholders or wrong source maps invalidate the applied conclusion.

The implementation uses strong three-valued conjunction: known false dominates unknown; otherwise any unknown yields unknown; only all true yields true. Exhaustive truth-table testing through six gates and a separately expressed set oracle check the implementation.

**Result F3 — source removal cannot create a supported option.** In this implementation, ablation changes some known gate values to unknown and leaves consent unchanged. It therefore cannot enlarge `F_minus`, although it can enlarge `F_plus` by withdrawing a previously supported rejection. This is a property of the information bookkeeping, not evidence that losing a source improves reality.

## 4. Preference without a collective happiness scalar

On the supported set, the synthetic fixture supplies each participant's ordinal rank `r_i(o)`, higher meaning preferred. Option `a` dominates `b` iff `r_i(a) >= r_i(b)` for every i and the inequality is strict for at least one i. Return all undominated supported options. Never aggregate these ranks into a truth score or interpersonal welfare sum.

Separate strictly increasing transformations of the participants' ranks preserve this set: each constituent comparison is preserved. The tests check affine examples of this general elementary fact. Unknown or unlisted candidates may change the frontier; the output labels its scope accordingly. A deployed system must also support incomplete preferences rather than force a full ranking.

## 5. Minimal blocking sets and honest obstruction types

For a fully rejected finite catalog, an inclusion-minimal blocking set is a set of named gates such that every listed option fails at least one of them, but no proper subset retains that property. Enumeration returns all such minimal sets within the prototype bounds. Minimal means inclusion-minimal, not cheapest or ethically permissible to relax.

Output meanings:

| Output | Meaning | Not licensed |
|---|---|---|
| `SUPPORTED_OPTIONS` | Some listed options pass every supplied gate | A real person is happy; globally best option found |
| `UNRESOLVED` | No supported option yet, but some have only true/unknown gates | Incompatibility or tacit consent |
| `NO_PERMISSIBLE_OPTION_IN_CATALOG` | Every listed option has a supported failing gate | Universal impossibility outside this catalog |
| `EMPTY_CATALOG_PATHWAY_GAP` | No candidate was supplied | A no-solution theorem |

A missing meaning operator is a pathway gap; competing meanings without a discriminator are a probe gap; missing testimony or measurement is an access gap; an established consent/safety constraint is a boundary. The code covers only part of that diagnostic space. It cannot decide which unrecorded explanation applies to a human episode.

## 6. Pairwise compatibility is not global compatibility

**Result F4 — exact three-party counterexample.** Let

```
O = {x,y,z}
A = {x,y}; B = {y,z}; C = {x,z}.
```

Every two of A, B, C intersect, while their three-way intersection is empty. The script checks each pair and reports the three named floors as a minimal blocking set for the full group. Hence a connected graph of dyadic agreement is not a certificate of a coherent multi-party arrangement. The result concerns this finite model, not an inevitability for American society.

## 7. Predictive overlap, not phasors

For a finite set of rival explanations and a declared probe, group rivals by predicted outcome. Count a pair as split only when both predictions are supplied and differ. Unknown predictions remain unresolved. The bootstrap reports raw pair counts with no prior probabilities; it does not call them truth mass.

This is the weakest suitable Aletheia instrument here. No sign/phase transport, Fourier basis, quantum interpretation, or speedup is asserted. Pair-count discrimination cannot establish which rival is true before the probe is run. The supplied toy probe patterns calibrate arithmetic only; no human explanation was tested.

## 8. The sheaf ambition is deferred, not smuggled in

An overlap of social memberships is not itself a topology. A cross-context translation is not automatically a restriction. A genuine sheaf model requires a declared site or base, section objects, compatible restriction maps, and locality/gluing conditions. “No global section” is meaningful only after specifying which object is meant to glue; it does not mean there is no common reality or no possibility of coexistence.

For now, use typed graphs, finite relations, provenance, and explicit compatibility constraints. The multi-party counterexample motivates later work on composition but does not prove a sociological sheaf obstruction. Upgrade the mathematics only when it adds an experimentally relevant discriminator beyond this simpler model.
