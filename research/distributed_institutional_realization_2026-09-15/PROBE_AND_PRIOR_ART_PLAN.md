# Probe and Prior-Art Plan — Distributed Institutional Realization

This file converts the manuscript seed into a falsifiable research program.

The primary danger is that the proposal is merely an elegant restatement of ordinary network theory, distributed cognition, role theory, social ontology, or systems engineering. The job of the next phase is therefore **not** to decorate the vocabulary. It is to force the scaffold through rival models, ablations, hostile examples, and explicit implementation.

---

# 1. Load-bearing research questions

## Q1 — Is `I_t` a real analytical object or redundant notation?

Given

\[
\mathcal I_t=\mathfrak R_t(\mathbf P_t,\mathbf R_t,\mathbf D_t,\mathbf S_t),
\]

can `I_t` support invariants, equivalence classes, or predictions that are harder or impossible to state cleanly on the raw tuple?

**Pass:** derive a stable equivalence/persistence notion, intervention result, or theorem-like statement that uses the realized object nontrivially.

**Fail:** all useful work reduces directly to the tuple; remove `I_t` as unnecessary reification.

---

## Q2 — What is specifically TLICA about the account?

Candidate TLICA-specific structure:

- indexed first-person profiles rather than generic nodes;
- identity-correlation independent of causal participation;
- source-pathway sensitivity;
- formation/activation distinction;
- osmotic imprinting;
- field-flattening as a discriminator;
- semantic-interoperability machinery;
- anti-group-mind attribution discipline.

**Pass:** at least one of these yields a prediction/discriminator not available from a simpler graph alone.

**Fail:** reclassify the project as a translation bridge rather than a distinct application theory.

---

## Q3 — Can local discontinuity be operationalized without becoming "hidden variables exist"?

Need a task where:

1. the event is locally surprising;
2. the distributed support path is known;
3. exposing the correct support improves prediction;
4. exposing matched irrelevant context does not;
5. removing a predicted support edge changes the event.

This is the cleanest probe of the central thesis.

---

# 2. Minimal computational model

Build a deliberately small simulator before any large agent model.

## 2.1 Entities

```python
Agent(
    id,
    role,
    local_model,
    identity_profile,
    source_trust,
    latent_rules,
    active_rules,
)

Artifact(
    id,
    kind,
    state,
    provenance,
    authorized_readers,
    authorized_writers,
)

Relation(
    src,
    dst,
    kind,
    valid,
    weight=None,
)

Event(
    source,
    content,
    artifact_refs,
    timestamp,
)
```

## 2.2 First toy world

Use a badge-controlled door because it contains:

- explicit roles;
- artifacts;
- source trust;
- a local abrupt event;
- easy ablations;
- no politically loaded interpretation.

### Baseline path

```text
role assignment
-> admin update
-> database state
-> credential relation
-> reader query
-> controller decision
-> actuator
-> door opens
```

### Ablations

1. duplicate badge shell only;
2. delete database entry;
3. keep entry, cut network;
4. forge admin update;
5. replace employee with compatible role-holder;
6. preserve employee, delete authorization edge;
7. corrupt local clock / time-window rule;
8. create conflicting database replicas.

### Metrics

- reachability;
- decision correctness;
- provenance validity;
- latency;
- observer predictability;
- local support visibility;
- failure class.

---

# 3. Complete factorial probe for TLICA-specific terms

Do not claim interactions without all cells.

Construct a toy institution with factors:

- `R`: relational edge intact / broken;
- `S`: source path valid / forged;
- `A`: role rule active / latent;
- `I`: role strongly identity-integrated / weakly integrated.

This yields 16 cells.

Measure:

- local behavior;
- compliance;
- reversion under field flattening;
- response to source challenge;
- persistence under role substitution.

The purpose is to distinguish:

- plain connectivity effects;
- source effects;
- activation effects;
- identity-placement effects;
- genuine interactions.

No mixed-term claim without the full factorial.

---

# 4. Local-discontinuity observer experiment

## 4.1 Design

Show participants or model observers the same terminal event under four information conditions:

1. **Local only:** only immediate scene before action.
2. **Relevant distributed support:** remote order/history/path needed for the action.
3. **Irrelevant context:** equal-length remote information unrelated to the action.
4. **Misleading rival support:** plausible but wrong causal story.

Outcomes:

- predictability rating;
- arbitrariness rating;
- individual-disposition attribution;
- institutional-structure attribution;
- confidence;
- ability to identify an intervention that would prevent the event.

## 4.2 Prediction

Correct distributed support should improve prediction and intervention identification more than irrelevant context.

If only narrative coherence improves while intervention accuracy does not, the effect may be mere post-hoc storytelling.

## 4.3 Negative control

Use a genuinely spontaneous/random event where no distributed support exists. Additional institutional context should not systematically improve prediction.

---

# 5. Interface-compatibility probe

## Hypothesis

Successful distributed institutional operation depends more on task-specific interface compatibility than on global representational similarity.

## Toy implementation

Give multiple agents different internal ontologies but a shared protocol.

Compare four regimes:

1. high global similarity / high interface compatibility;
2. high global similarity / low interface compatibility;
3. low global similarity / high interface compatibility;
4. low global similarity / low interface compatibility.

If regime 3 performs substantially better than regime 2, this supports the distinction.

This is especially relevant to TLICA's semantic-interoperability program.

---

# 6. Source-path probe

Replay identical content over different provenance chains:

- recognized authority;
- recognized peer without authority;
- forged authority;
- unknown source;
- automated system with delegated authority.

Measure:

- action uptake;
- verification behavior;
- delay;
- escalation;
- downstream propagation.

Then flatten source metadata and compare.

This tests whether `SrcPath(x)` is load-bearing rather than decorative.

---

# 7. Codified-versus-lived institution probe

Choose a bounded real system where formal procedure and actual workflow are both measurable.

Potential low-risk domains:

- library checkout workflow;
- university room-booking procedure;
- open-source contribution workflow;
- small volunteer organization;
- tabletop simulation;
- software incident-response playbook.

Avoid politically or legally sensitive claims in the first empirical pass.

Represent:

\[
\mathcal I^{\text{codified}}
\]

from formal artifacts, and

\[
\mathcal I^{\text{lived}}
\]

from observed paths.

Measure:

- path overlap;
- undocumented edges;
- unused formal edges;
- substitution points;
- bottlenecks;
- prediction error for actual actions.

The key question is whether the lived representation predicts events better than the codified representation alone.

---

# 8. Persistence and turnover probe

Simulate or observe role-holder turnover.

Compare institutional output after:

1. person replacement with role/path preservation;
2. person preservation with edge destruction;
3. artifact replacement with provenance preservation;
4. artifact preservation with provenance destruction;
5. gradual local-model drift.

Derive a task-relative persistence metric.

Candidate:

\[
\operatorname{Pers}_T(\mathcal I_t,\mathcal I_{t+\Delta})
=
1-d_T(\mathcal I_t,\mathcal I_{t+\Delta}),
\]

where `d_T` is a declared task-relative structural distance.

Do not call this identity until the equivalence criterion is explicit.

---

# 9. Sheaf-formalization gate

Do not promote sheaf language until the following can be filled without handwaving.

## Base

What indexes local patches?

Candidates:

- organizational neighborhoods;
- roles;
- information-access regions;
- task interfaces;
- subsets of a typed interaction graph.

## Sections

What is assigned to each patch?

Candidates:

- local role model;
- permissions;
- recognized sources;
- local records;
- transition rules;
- semantic mappings.

## Restrictions

How is a larger local representation restricted to an overlap?

## Compatibility

Exact equality? Behavioral equivalence? Semantic translation? Constraint satisfaction?

## Gluing

What counts as a global institutional realization?

## Obstruction

Find an explicit family of locally coherent sections that cannot glue, with an observable institutional failure.

If these cannot be made precise, use typed hypergraph language instead.

---

# 10. Rival-framework provenance tomography

The project must compare against genuinely different intellectual lineages rather than several summaries of the same lineage.

Create a source map with at least these families:

| Family | Core question to compare |
|---|---|
| Social ontology / institutional facts | What makes an institutional fact exist? |
| Collective intentionality | Is shared/we intentionality required? |
| Distributed cognition | Can cognition span agents and artifacts? |
| Situated cognition | How much explanation lives in agent-environment coupling? |
| Actor-network / sociotechnical theory | How are heterogeneous human/nonhuman networks described? |
| Role theory | How do roles constrain behavior? |
| Organizational sociology | How do formal and informal structures persist/fail? |
| Institutional economics | How do rules/incentives structure behavior? |
| Distributed systems | How do state, replication, authority, failure, and consensus work across nodes? |
| Multi-agent systems | How do local policies produce global behavior? |
| Control/observability | When can hidden state be reconstructed from local outputs? |
| Sheaf/contextuality formalisms | How do local consistency and global gluing relate? |

For each family record:

- primary source(s);
- core object;
- unit of analysis;
- agency assumptions;
- treatment of artifacts;
- treatment of source/provenance;
- treatment of local/global mismatch;
- treatment of identity/role integration;
- predictions or formal results;
- overlap with TLICA;
- residual difference.

Then run leave-one-family-out synthesis to ensure the proposed contribution is not inherited entirely from one source family.

---

# 11. High-priority authors / search targets

These are search targets, not asserted authorities or claims of equivalence.

- John Searle — institutional facts / status functions;
- Margaret Gilbert — plural subjects / joint commitment;
- Raimo Tuomela — collective intentionality;
- Michael Bratman — shared agency;
- Edwin Hutchins — distributed cognition;
- Lucy Suchman — situated action;
- Bruno Latour / actor-network traditions;
- Erving Goffman — roles, frames, interaction order;
- Douglass North — institutions and constraints;
- Elinor Ostrom — institutional rules and collective action;
- James March / Herbert Simon — organizations and bounded rationality;
- distributed systems literature on provenance, consensus, replication, failure, and authority;
- graph dynamical systems and network controllability/observability;
- sheaf-theoretic treatments of local-to-global consistency in data, networks, and contextuality.

Do not cite from memory in publication. Recover primary/official texts.

---

# 12. Hostile examples

A good formalism must survive cases where the intuitive "institution" is weak or ambiguous.

## H1 — charismatic organization

Output depends strongly on one person. Tests limits of role substitutability.

## H2 — secret informal clique

Minimal codified artifacts; heavy trust and tacit knowledge.

## H3 — open-source protocol

Persistent rules and artifacts with highly fluid membership.

## H4 — dead institution

Documents and buildings survive after role-recognition collapses.

## H5 — occupied/contested authority

Multiple groups claim the same roles and artifacts.

## H6 — automated bureaucracy

Many decisions implemented by software with sparse human intervention.

## H7 — ritual

High social coordination and role structure but weak instrumental output.

## H8 — market convention

Distributed expectation with no centralized authority.

## H9 — language convention

Extremely distributed, self-maintaining, no clear membership boundary.

## H10 — one-person corporation

Tests whether multi-agent distribution is necessary or merely common.

Each hostile case should either fit cleanly, force a boundary restriction, or refute an overbroad claim.

---

# 13. Mutation tests

Take a working model and mutate one assumption at a time.

- remove source tracking;
- collapse all roles;
- force identical agent models;
- remove artifacts;
- remove identity-correlation;
- remove formation history;
- make all edges untyped;
- make every agent globally informed;
- eliminate redundancy;
- randomize local maps while preserving protocol.

Track which predictions survive.

This identifies what is genuinely load-bearing.

---

# 14. Mainline promotion criteria

Do **not** integrate the whole scaffold into foundation merely because it is coherent.

## Eligible for application-level mainline documentation when

- cultural-I boundary is explicit;
- no new term collides with foundation notation;
- at least one computational toy model runs;
- at least one discriminator survives controls;
- rival-framework map is populated with primary sources;
- all claims are ledgered.

## Eligible for foundation-level promotion only if

- multiple independent applications require the same object;
- the object cannot be defined cleanly as a derived summary;
- removing it creates repeated formal duplication or contradiction;
- it survives hostile examples and alternate implementations.

Default expectation: **remain application-level**.

---

# 15. Immediate next work order

1. Audit current main for every `cultural-I`, `institution`, `role-indexed`, `relational cascade`, `situational field`, and `source-path` use.
2. Build the badge-door toy simulator.
3. Run the full 2x2x2x2 factorial on relation/source/activation/identity placement.
4. Formalize one nontrivial local-to-global incompatibility example.
5. Begin primary-source prior-art matrix.
6. Rewrite the manuscript only after these probes expose which language survives.

The target is not to preserve the current formalism. The target is to discover the weakest formal object that explains the phenomena and survives contact with rivals.
