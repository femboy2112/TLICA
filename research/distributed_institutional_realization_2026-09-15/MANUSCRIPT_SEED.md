# Distributed Institutional Realization

## Local discontinuity, relational causation, and social structure without a group mind

**Status:** application-paper seed; research branch only

**Architecture dependency:** TLICA foundation v5.5.0 and current application-level agency / cultural-I machinery

---

## Abstract

Human beings routinely act through structures that are neither reducible to a document nor plausibly modeled as an additional collective subject. Governments, courts, firms, offices, procedures, currencies, and social norms persist because many indexed people carry partial models, role-conditioned dispositions, expectations, permissions, obligations, memories, records, and response policies that mesh through material artifacts and communication pathways. The operating structure is therefore distributed across agents and primal not-I rather than located in one mind or one text.

TLICA already contains several ingredients needed to describe this: indexed modeling Is, role-indexed profiles, relational cascades, integration graphs, situational fields, source-pathway analysis, formation/activation separation, osmotic imprinting, and the cultural-I as a distributed pattern that must not be anthropomorphized into a group mind. What is missing is a canonical application-level realization map from a multi-agent relational state plus its artifacts and environment to a time-local institutional configuration.

This paper seeds that extension. Let `A = {a_1,...,a_n}` be indexed agents, `P_t = (P_1(t),...,P_n(t))` their relevant TLICA profiles, `R_t` a typed relational structure among agents and artifacts, `D_t` the material-symbolic artifacts that participate in the institution, and `S_t` the relevant situational/material field. Define an application-level institutional realization map

\[
\mathfrak R_t:(\mathbf P_t,\mathbf R_t,\mathbf D_t,\mathbf S_t)\mapsto \mathcal I_t,
\]

where `I_t` is not a subject but the realized distributed institutional configuration at time `t`. A second map

\[
\mathscr A_t:\mathcal I_t\mapsto \Delta\mathcal W_t
\]

tracks the institution's physically realized consequences in primal not-I by requiring an explicit causal path through agents, artifacts, communication, and role activation.

The construction explains one recurrent phenomenology of social life: behavior can look locally abrupt, discontinuous, or "out of pocket" when an observer projects a globally distributed causal path onto a small local frame. The apparent discontinuity is not evidence for nonphysical social causation; it can arise because the causal state that makes the behavior intelligible is distributed elsewhere in the network and only becomes locally visible at the activation point.

The paper develops this proposal, distinguishes it from simple vector aggregation, supplies government and organizational worked examples, sketches graph-, tensor-, and sheaf-like representations, derives candidate invariants and predictions, states anti-reification constraints, and identifies the discriminating probes required before any claim of explanatory superiority is warranted.

---

# 1. The object to recover

Consider a written constitution sitting in an empty archive.

The document is real. Its ink, paper, bit-patterns, legal history, and semantic content are all real in ordinary senses. Yet the document alone does not arrest anyone, collect taxes, appoint judges, transmit orders, adjudicate cases, issue licenses, or maintain public records.

Now add people who have never seen the document and do not recognize any authority relation associated with it. The text still does not become an operating government.

Now add millions of people, each carrying only partial and heterogeneous information, but connected through stable roles, procedures, records, communication channels, expectations, incentives, physical infrastructure, and enforcement pathways. Suddenly local reality contains events that are intelligible only relative to a structure no single person fully contains.

An officer executes an order authored elsewhere. A clerk rejects an application because a database state changed. A judge's sentence changes what another institution may lawfully do. A bank credits an account because a transaction cleared through a set of institutions distributed across machines and people. A worker is admitted to a restricted room because a badge encodes a role relation that almost nobody nearby can independently verify from first principles.

In ordinary language we say:

> the government did X;
> the court ordered Y;
> the bank transferred Z;
> the company fired A.

These sentences are useful, but they compress away the implementation.

TLICA needs a way to recover the implementation without committing either of two errors:

1. **document reduction:** treating the codified artifact as identical to the live institution;
2. **group-mind reification:** treating the institution as a new unindexed subject that literally believes, wants, chooses, or experiences.

The target is an intermediate object: a **distributed realized structure** that is real enough to constrain and cause events, but not a new person.

---

# 2. Existing TLICA commitments that constrain the extension

The extension is not built on a blank slate.

## 2.1 Indexed agents remain primitive to the social analysis

TLICA's agency applications already insist that multi-agent and institutional cases decompose into indexed agent-profile sets plus relational structure. Collective explanation therefore cannot silently replace `a_1,...,a_n` with an unindexed super-agent `A_group`.

Any institutional predicate that sounds intentional must be translated into an indexed path unless an actual institutional agent with legally or operationally centralized decision procedures is being described at the ordinary organizational level. Even then, the architecture must distinguish useful organizational shorthand from literal phenomenal subjecthood.

## 2.2 The cultural-I is precedent, not completion

The cultural-I already functions as an emergent distributed pattern carried across many individual Is. Its anti-anthropomorphism discipline is load-bearing: the pattern can shape inputs, expectations, routing, and interpretation without itself becoming an intending mind.

That precedent establishes that TLICA can recognize distributed social patterning.

What it does not yet fully specify is the more general realization problem:

> given many indexed profiles, relations, artifacts, and situational conditions, what exactly is the time-local institutional object that is presently realized?

## 2.3 Primal not-I carries implementation

Documents, servers, badges, buildings, uniforms, roads, weapons, account ledgers, courtrooms, network links, payroll systems, written procedures, and bodies are not metaphorical. They are implemented in primal not-I.

The institutional object must therefore be hybrid:

- partly carried in agent profiles and learned dispositions;
- partly carried in relations among agents;
- partly carried in physical artifacts and records;
- partly carried in external material and incentive conditions.

A purely mental account is insufficient.

## 2.4 Formation and activation are distinct

TLICA's formation/activation distinction is critical here.

A role disposition can exist latently for years and activate abruptly when a trigger condition appears. An officer does not continuously perform arrest behavior. A judge does not continuously issue rulings. A fire alarm procedure is not continuously enacted. The distributed structure is maintained while local behavior remains quiescent.

This gives the architecture a principled way to model sharp regime switches without treating them as ontological discontinuities.

## 2.5 Situational fields remain external

The current situational field `S` is an external incentive/social environment against which behavior is tested. The proposed institutional scaffold must not absorb every external condition into the institution itself. Boundary discipline matters.

The institution may shape `S_t`, and `S_t` may activate parts of the institution, but they remain analytically separable where possible.

---

# 3. Why a simple vector of people is insufficient

The motivating intuition can be expressed as:

> imagine people as basis units and the social structure as something realized over that basis.

This is useful, but a plain vector space loses the thing we need most: relations.

Let

\[
V_A = \operatorname{span}\{e_1,\ldots,e_n\}
\]

be the free vector space over indexed people.

Then a population state

\[
v=\sum_i c_i e_i
\]

can encode participation weights, activation levels, probabilities, saliences, or other scalar summaries.

But two populations can have the same coefficient vector and radically different institutions.

A population with one judge, one clerk, one defendant, and one officer is not equivalent to the same four people with their role/authority edges permuted.

Therefore the institution cannot be represented by coefficients alone.

At minimum we need:

\[
(\mathbf P_t,\mathbf R_t),
\]

where `P_t` contains indexed agent profiles and `R_t` contains typed relations.

For many institutions, even pairwise relations are insufficient. Some institutional facts are n-ary:

- a contract binds specific parties under a recognized authority and document state;
- a vote counts only under a procedure, electorate, time window, and tally rule;
- a court order has force only under a chain involving jurisdiction, signed artifact, parties, and implementing officers;
- a financial transfer involves payer, payee, institutions, ledger states, and authorization conditions.

That suggests hypergraph, tensor, category-theoretic, or sheaf-like structure rather than a bare vector.

The vector metaphor should therefore be retained only as the intuition that **indexed people form part of the carrier basis**, not as the final formalism.

---

# 4. Core formal scaffold

## 4.1 Indexed agent family

Let

\[
\mathcal A_t = \{a_1,\ldots,a_n\}
\]

be the set of participating indexed agents at time `t`.

Each agent carries an application-relevant TLICA profile

\[
P_i(t).
\]

`P_i(t)` is not necessarily the agent's entire foundation-level state. It is a projection onto the contents, roles, source-pathways, identity-correlations, tool-use capacities, and activation variables relevant to the institutional system under study.

Collect them:

\[
\mathbf P_t=(P_1(t),\ldots,P_n(t)).
\]

## 4.2 Artifact family

Let

\[
\mathbf D_t = \{d_1,\ldots,d_m\}
\]

contain relevant external artifacts in primal not-I:

- written laws;
- contracts;
- credentials;
- keys;
- databases;
- ledgers;
- physical tokens;
- buildings;
- network states;
- official records;
- machines;
- signs;
- uniforms;
- money-like instruments;
- communication records.

Artifacts are not assumed to have agency. They participate in causal and semantic pathways.

## 4.3 Typed relational structure

Let

\[
\mathbf R_t
\]

be a typed graph or hypergraph over agents and artifacts.

Representative edge/hyperedge types include:

- `recognizes-authority-of`;
- `is-authorized-by`;
- `reports-to`;
- `can-command`;
- `must-respond-to`;
- `trusts-record-produced-by`;
- `has-access-to`;
- `owns`;
- `is-bound-by`;
- `communicates-with`;
- `verifies-through`;
- `records-state-in`;
- `can-update`;
- `can-enforce`;
- `expects-response-from`;
- `occupies-role`;
- `is-legible-as-role-to`.

The typing matters. An undifferentiated social graph is too coarse.

## 4.4 Situational/material field

Let

\[
\mathbf S_t
\]

represent external conditions relevant to activation and action:

- physical location;
- time;
- resource availability;
- incentives;
- audiences;
- hazards;
- jurisdictional context;
- market conditions;
- environmental constraints;
- current events in primal not-I.

`S_t` is not identical to the institutional structure, though the institution may alter it.

## 4.5 Realization map

Define the application-level realization operator

\[
\boxed{
\mathfrak R_t(\mathbf P_t,\mathbf R_t,\mathbf D_t,\mathbf S_t)=\mathcal I_t
}
\]

where `I_t` is the **distributed institutional realization** at time `t`.

Interpretation:

`I_t` summarizes the live pattern of institutionally relevant capacities, recognized relations, latent/active role states, artifact states, and response pathways that are jointly realized at `t`.

Crucially:

\[
\mathcal I_t \neq \text{an additional subject}.
\]

It is a relational state descriptor.

## 4.6 Physical action/effect map

Define

\[
\boxed{
\mathscr A_t:\mathcal I_t\to\Delta\mathcal W_t
}
\]

where `W_t` is the relevant state of primal not-I.

This notation is admissible only if it can be expanded into a path such as

\[
\mathcal I_t
\to
\text{message/record/trigger}
\to
P_i\text{ activation}
\to
\text{agent action}
\to
\Delta\mathcal W_t.
\]

The arrow from institution to world is therefore shorthand over an implementation path, not magical downward causation.

## 4.7 Local projection

Let

\[
\pi_L(\mathcal W_t)
\]

be the world-state available to a local observer or measurement frame `L`.

The frame may omit most institutional support variables.

An event can therefore satisfy

\[
\pi_L(\mathcal W_{t^-})\approx x,
\qquad
\pi_L(\mathcal W_{t^+})\approx y,
\]

with a sharp apparent transition `x -> y`, even when the global implementation path is continuous or piecewise ordinary.

This yields the central candidate proposition.

---

# 5. Candidate Local-Projection Proposition

## 5.1 Informal statement

**Candidate proposition — distributed-support local discontinuity.**

If a local frame omits variables that carry a live causal path through a distributed institutional realization, then activation of that path can produce behavior that appears abrupt or causally unmotivated within the local projection even though the larger system contains an ordinary relational chain connecting the pre-event and post-event states.

## 5.2 Formal sketch

Let the global state be

\[
X_t=(L_t,H_t),
\]

where `L_t` contains locally observed variables and `H_t` contains hidden/distributed support variables.

Suppose global dynamics satisfy

\[
X_{t+\Delta t}=F(X_t)
\]

with no discontinuity stronger than the model already allows.

The local observer sees only

\[
Y_t=\pi_L(X_t).
\]

If

\[
\frac{\partial F_L}{\partial H}
\neq 0,
\]

then changes or threshold crossings in `H_t` can induce abrupt changes in `Y_t` even when `L_t` alone contains no apparent precursor.

Institutional realization supplies a structured interpretation of `H_t`:

\[
H_t\supseteq(\mathbf P^{\text{remote}}_t,\mathbf R_t,\mathbf D^{\text{remote}}_t,\mathbf S^{\text{remote}}_t).
\]

The proposition is therefore not mysterious. It is an observability result.

## 5.3 What would make this nontrivial

The proposition becomes scientifically useful only if TLICA contributes more than the generic statement "hidden variables can matter."

The application must show that its profile/role/source/activation machinery predicts **which hidden variables matter**, **how they are distributed**, and **which interventions sever the path**.

Otherwise the result collapses into ordinary systems theory.

That is an explicit truth debt.

---

# 6. Government as a worked example

Government is useful because ordinary language already compresses multiple ontological levels under one noun.

## 6.1 Codified object

Let

\[
D^{\text{gov}}
\]

contain constitutions, statutes, regulations, case law, orders, records, databases, credentials, forms, and related artifacts.

These artifacts can persist with no currently active governmental behavior.

Therefore

\[
D^{\text{gov}}\neq \mathcal I^{\text{gov}}_t.
\]

## 6.2 Agent-local maps

Each participating person holds only a partial profile-relative representation:

\[
M_i(D^{\text{gov}},\mathbf R_t).
\]

Examples:

- a judge carries role-specific legal models and authority expectations;
- an officer carries operational rules and command-recognition pathways;
- a clerk carries procedural and record-update rules;
- a citizen carries a partial model of obligations, rights, and expected institutional behavior;
- an attorney carries another high-resolution but role-specific representation.

No equality of maps is required.

The institution may remain operational under substantial representational heterogeneity so long as enough load-bearing compatibility conditions hold.

## 6.3 Relational realization

An order can propagate as:

\[
\text{case state}
\to
\text{judge action}
\to
\text{signed artifact}
\to
\text{record update}
\to
\text{message}
\to
\text{recipient role activation}
\to
\text{physical action}.
\]

A bystander who sees only the final physical action may experience the event as locally abrupt.

Nothing supernatural happened. The omitted support structure was simply elsewhere.

## 6.4 Counterfactual deletion tests

The example generates useful ablations.

### Delete the document while preserving every agent's learned map temporarily

Some institutional behavior may persist for a time.

Therefore the document is not sufficient and may not be moment-to-moment necessary for all outputs.

### Delete recognition/role relations while preserving the document

Institutional operation can collapse even though the artifact remains.

### Delete the communication edge

The order exists but does not propagate to the implementing agent.

### Delete the implementing agent but preserve all upstream states

The path terminates unless a redundant role-holder substitutes.

### Replace one role-holder with another who carries a compatible local section

The institution may continue with little global change.

That substitution property is evidence that the institutional structure is not identical to a particular person.

---

# 7. Institutions as local sections: the sheaf-like intuition

The sheaf analogy may be more faithful than the vector analogy.

## 7.1 Local patches

Let each role-holder or bounded organizational neighborhood define a local patch `U_i`.

A local section

\[
s_i\in\mathcal F(U_i)
\]

contains whatever institutionally relevant structure is locally carried there:

- role knowledge;
- permissions;
- expectations;
- records;
- source-recognition;
- action policies;
- interfaces to neighboring patches.

## 7.2 Overlap consistency

Where patches overlap, local sections must satisfy compatibility constraints sufficient for operation:

\[
s_i|_{U_i\cap U_j}
\sim
s_j|_{U_i\cap U_j}.
\]

Exact equality is usually unnecessary.

A clerk and judge need not conceptualize the entire institution identically. They need enough interoperable structure on the overlap relevant to their interaction.

## 7.3 Gluing

If compatible local sections glue, the system realizes a global institutional configuration:

\[
\{s_i\}\rightsquigarrow \mathcal I_t.
\]

This captures an important phenomenon:

> no individual needs to represent the whole for the whole pattern to be operationally realized.

## 7.4 Obstructions

Failure to glue can model institutional breakdown:

- incompatible records;
- contradictory authority claims;
- ambiguous jurisdiction;
- communication loss;
- semantic mismatch;
- duplicated identifiers;
- role conflict;
- inconsistent procedures;
- source-compromised directives;
- legitimacy collapse.

This is attractive because TLICA already cares about local models, source-pathways, semantic interoperability, and relational structure.

## 7.5 Boundary

No claim is made here that the mathematically correct final object is literally a sheaf over a topological space.

The sheaf language is a candidate formalization to be earned by specifying:

1. the base object;
2. the cover;
3. section contents;
4. restriction maps;
5. compatibility relation;
6. gluing condition;
7. observable failure modes.

Until then, "sheaf-like" is a disciplined metaphor, not a theorem.

---

# 8. Role activation and threshold-like behavior

Institutional behavior is often dormant until a condition is met.

Let agent `i` have a role-specific activation functional

\[
q_i(t)=Q_i(P_i(t),\mathbf R_t,\mathbf D_t,\mathbf S_t).
\]

Then a simplified activation rule may be written

\[
A_i^{\text{role}}(t)=
\begin{cases}
0,& q_i(t)<\theta_i,\\
1,& q_i(t)\ge\theta_i.
\end{cases}
\]

This is not claimed as literal neurobiology. It is an application-level abstraction.

The important point is structural:

\[
\text{long-lived formation}
+\text{quiet maintenance}
+\text{trigger}
\to
\text{rapid activation}.
\]

A local observer can therefore see a sharp behavioral switch even though the enabling structure was continuously present.

This mechanism is compatible with TLICA's separation between imprinting/formation and activation/operation.

---

# 9. Social reality without magical causation

The phrase "social construction" often invites a false dichotomy:

- either the object is physically fundamental;
- or it is "made up" and therefore causally unreal.

Distributed institutional realization rejects that dichotomy.

A traffic law is not a new fundamental force. Yet a person may stop a two-ton vehicle at a red light because multiple physical systems carry the relevant social structure:

- learned rule integration;
- signage;
- enforcement expectation;
- shared semantic convention;
- licensing procedures;
- road engineering;
- other drivers' expectations;
- legal artifacts.

The causal chain remains physical throughout.

What is emergent is the **organization of those physical carriers into a relational pattern**.

Thus:

\[
\text{emergent}\not\Rightarrow\text{fictional}
\]

and

\[
\text{causally real}\not\Rightarrow\text{ontologically primitive}.
\]

---

# 10. Distinguishing the institution from neighboring objects

A durable application paper must keep several nearby concepts separate.

## 10.1 Institution versus organization

An organization is usually a more bounded collection of agents, roles, and resources.

An institution may cut across many organizations and populations.

The realization scaffold should support both without assuming identity.

## 10.2 Institution versus norm

A norm is a patterned expectation or rule-like social regularity.

A norm can participate in `I_t`, but the institution may also require artifacts, formal roles, records, and infrastructure.

## 10.3 Institution versus cultural-I

The cultural-I is a distributed pattern of cultural encoding across individual Is.

Institutional realization is broader and more implementation-explicit. It includes role topology, artifacts, external records, authority edges, and material pathways.

A cultural-I may contribute to an institution without being identical to it.

## 10.4 Institution versus situational field

The institution can shape the field and the field can condition the institution.

They should not be collapsed.

## 10.5 Institution versus shared belief

Shared belief may be neither necessary nor sufficient.

Agents can disagree deeply about what the institution means while still interoperating operationally.

Conversely, broad shared belief without role, artifact, or enforcement structure may fail to instantiate the institution under study.

## 10.6 Institution versus legal text

A legal artifact is one carrier among others.

Its operational significance depends on the surrounding realization network.

---

# 11. Representational heterogeneity and interoperability

One of the most important consequences of the framework is that institutional coherence does not require identical internal representations.

Let

\[
M_i(\mathcal I_t)
\]

be agent `i`'s model of the institution.

Typically

\[
M_i(\mathcal I_t)\neq M_j(\mathcal I_t).
\]

The relevant question is whether their maps preserve enough relational structure for the required interface:

\[
\operatorname{Compat}_{ij}^{(k)}
\]

for task/interface `k`.

This connects naturally to TLICA's semantic-interoperability work.

An institution can therefore be globally functional while locally misunderstood.

It can also fail abruptly when a previously hidden mismatch reaches an interface where compatibility is required.

This predicts a class of institutional "sudden failures" that are actually accumulated incompatibilities exposed at a coupling point.

---

# 12. Persistence, redundancy, and identity through turnover

Institutions often survive replacement of individual members.

This implies that institutional identity is not simple numerical identity of its carriers.

Let

\[
\mathcal A_t\neq\mathcal A_{t+T}
\]

while

\[
\mathcal I_t\approx\mathcal I_{t+T}
\]

under a task-relevant structural equivalence.

The application therefore needs a persistence criterion.

Candidate ingredients:

- preservation of role topology;
- preservation of critical source-pathways;
- preservation of artifact/record continuity;
- preservation of interface compatibility;
- preservation of enough behavioral transition rules;
- bounded drift in constitutive norms;
- continuity of recognized authority relations.

This becomes a Ship-of-Theseus problem only if identity is demanded at an unnecessarily fine grain.

TLICA can instead define institution identity relative to a declared preservation profile.

---

# 13. Institutional failure modes

The scaffold should earn value by distinguishing failure classes.

## 13.1 Carrier failure

A required agent or artifact disappears.

## 13.2 Edge failure

A communication, authorization, trust, or access relation is severed.

## 13.3 Semantic-interface failure

Local maps remain internally coherent but cease to interoperate across an interface.

## 13.4 Source-compromise failure

A directive propagates through a valid-looking path whose upstream source has been substituted, forged, manipulated, or otherwise compromised.

## 13.5 Role-collision failure

An agent occupies incompatible role obligations with no adjudication path.

## 13.6 Record divergence

Multiple authoritative artifacts encode incompatible states.

## 13.7 Recognition collapse

Enough participants cease recognizing a role, authority, or procedure that the previous realization can no longer reproduce its outputs.

## 13.8 Activation failure

The structure exists, but the relevant trigger does not reach or activate the implementing role.

## 13.9 Overactivation

A role or rule activates outside its intended domain because the trigger classifier is too broad.

## 13.10 Drift under turnover

Local substitutions preserve superficial role occupancy while gradually changing the deeper compatibility structure until a threshold failure appears.

These failure classes should eventually be compared against established organizational and distributed-systems taxonomies.

---

# 14. Worked micro-example: badge-controlled door

A restricted door is useful because it strips away ideological complexity.

Agents:

- employee `a_e`;
- administrator `a_a`;
- security agent `a_s`.

Artifacts:

- badge `d_b`;
- access-control database `d_db`;
- door controller `d_c`.

Relations:

- `a_a can-update d_db`;
- `d_b identifies a_e`;
- `d_c trusts d_db`;
- `a_s recognizes logs from d_c`;
- `a_e occupies authorized-role r`.

A local observer at the door sees:

\[
\text{badge approaches reader}
\to
\text{door unlocks}.
\]

The behavior may look like the plastic card itself possesses authority.

The distributed realization reveals the larger path:

\[
\text{employment/role state}
\to
\text{admin database update}
\to
\text{credential relation}
\to
\text{controller query}
\to
\text{door actuator}.
\]

Ablations distinguish components:

- duplicate the plastic without the database relation: no access;
- preserve the database but sever network connectivity: perhaps no access;
- preserve credential validity but change role policy: changed access;
- replace employee with another badge-holder: access follows relational state, not physical resemblance.

This is institutional causation in miniature.

---

# 15. Worked micro-example: emergency procedure

Suppose a workplace has an emergency-response protocol.

Most of the time no visible behavior expresses it.

Yet the structure is carried through:

- training memories;
- signage;
- equipment location;
- role assignment;
- alarm semantics;
- supervisor expectations;
- building layout;
- external emergency-service interfaces.

When the alarm activates, behavior changes sharply.

Locally:

\[
\text{ordinary work}\to\text{rapid coordinated evacuation}.
\]

Globally:

\[
\text{long-lived latent structure}+\text{alarm trigger}\to\text{role activation cascade}.
\]

This case demonstrates that apparent behavioral discontinuity need not imply newly created structure. It can be activation of structure formed long before.

---

# 16. Candidate invariants

A useful formalism should identify quantities or structures whose preservation predicts institutional continuity.

Candidate invariants include:

## 16.1 Reachability

For critical action `y`, does there remain a valid path

\[
\text{trigger}\leadsto y?
\]

## 16.2 Authority-path integrity

Can the action path be traced to an admissible source under the institution's own source rules?

## 16.3 Interface compatibility

Do adjacent local sections agree sufficiently on shared variables?

## 16.4 Role substitutability

Can one carrier be replaced by another without large change to outputs?

## 16.5 Record coherence

Do authoritative artifacts encode mutually compatible state?

## 16.6 Activation margin

How close are critical role activations to threshold or ambiguity?

## 16.7 Redundancy

How many independent or partially independent paths can realize a critical function?

## 16.8 Observability gap

How much of the causal support for a local event lies outside the observer's accessible frame?

This last quantity is particularly relevant to the local-discontinuity thesis.

---

# 17. Candidate observability-gap diagnostic

Let `C(y)` be the minimal causal support set required for outcome `y` under a declared model.

Let `O_L` be the variables observable in local frame `L`.

Define an application-level support-visibility ratio

\[
\nu_L(y)
=
\frac{|C(y)\cap O_L|}{|C(y)|}
\]

for finite support sets, or an appropriately weighted analogue.

Then low `nu_L(y)` predicts that `y` is more likely to appear unexplained, abrupt, arbitrary, or agent-intrinsic to the local observer.

This is deliberately a toy diagnostic.

Its purpose is to make the intuition falsifiable:

- expand the observer's access to omitted support variables;
- if the event becomes predictively legible, the distributed-support account gains support;
- if not, the account has failed to identify the real discriminator.

---

# 18. Predictions and discriminators

The paper should not survive as vocabulary alone.

## P1 — support revelation reduces perceived discontinuity

When observers are shown previously hidden institutionally relevant causal support, ratings of an event as arbitrary/sudden/unmotivated should decrease more than when shown irrelevant contextual detail.

## P2 — role-preserving substitution preserves output better than person-preserving edge destruction

Replacing an individual with a compatible role-holder should often perturb output less than preserving the individual while severing critical relational edges.

This distinguishes relation-first structure from person-essentialist accounts.

## P3 — document preservation is insufficient

Systems in which codified rules remain unchanged but recognition/communication/role relations are disrupted should show institutional output collapse despite artifact persistence.

## P4 — local-map identity is unnecessary

Operational success should tolerate substantial divergence in agents' global conceptual models provided interface-specific relational compatibility remains high.

## P5 — hidden incompatibility produces delayed sharp failure

Distributed systems with accumulating local-map divergence should remain apparently stable until an interface requiring the inconsistent variable is activated, after which failure can appear abrupt.

## P6 — path-specific intervention beats content-only intervention

For some institutional failures, changing a document's content without repairing propagation or recognition edges will fail, whereas repairing the path with unchanged content will restore operation.

## P7 — activation-history dissociation

Agents with similar present role behavior can differ in formation history and therefore differ under field-flattening, source perturbation, or novel contexts.

This imports a distinctly TLICA-style formation/activation discriminator.

## P8 — source-path perturbation matters even under behaviorally identical messages

Two identical directives delivered through different source chains can produce different uptake when agents track authority/source status.

## P9 — observability-gap manipulation changes attribution

Holding the actual event fixed while varying access to distributed causal support should shift whether observers attribute the event primarily to individual disposition, institutional structure, or randomness.

## P10 — institutional identity survives carrier turnover within structural bounds

Systems with high role substitutability and preserved relational invariants should maintain function across substantial membership turnover better than systems whose critical functions are person-specific.

---

# 19. Rival models that must be beaten, not renamed

A TLICA application paper only earns its complexity if it distinguishes itself from simpler descriptions.

## Rival A — ordinary network theory

Maybe everything above is just a typed graph with stateful nodes.

**Debt:** identify what TLICA's profile/source/formation/identity apparatus predicts that generic network language does not.

## Rival B — distributed cognition

Maybe the institution is simply a distributed cognitive system.

**Debt:** determine whether TLICA contributes a principled anti-group-mind distinction, identity-correlation structure, or source/activation decomposition beyond established distributed-cognition work.

## Rival C — institutional facts / status-function accounts

Maybe the correct object is already captured by established philosophical accounts of institutional reality.

**Debt:** compare realization conditions and causal implementation explicitly.

## Rival D — role theory

Maybe role-conditioned behavior plus norms is enough.

**Debt:** show why source-pathways, artifacts, local model compatibility, and activation history add predictive value.

## Rival E — actor-network / sociotechnical accounts

Maybe heterogeneous networks of human and nonhuman actants already provide the descriptive machinery.

**Debt:** compare anti-anthropomorphism, agency attribution, and first-person architecture carefully.

## Rival F — distributed systems engineering

Maybe this is fault-tolerant distributed computation translated into social language.

**Debt:** exploit that analogy where valid and isolate where human identity, meaning, source recognition, and norm integration create genuinely different structure.

## Rival G — simple hidden-variable explanation

Maybe "local discontinuity" says only that the observer missed causes.

**Debt:** identify institution-specific support variables and predict intervention outcomes.

---

# 20. Anti-reification discipline

The extension must enforce the following rules.

## Rule 1 — intention requires an indexed bearer or an explicit organizational shorthand

Do not write "the institution wanted X" as a foundation-level claim.

Translate to:

- specific agents wanted X;
- a decision procedure selected X;
- the realized structure made X the stable output;
- the institutional rule-path caused X under specified conditions.

## Rule 2 — causal arrows must expand

`Institution -> event` is allowed as compressed notation only when an implementation path can be supplied.

## Rule 3 — correlation is not responsibility

Being a carrier of part of a distributed pattern does not imply intending or endorsing the global output.

## Rule 4 — participation is graded and typed

An individual may be:

- causal carrier;
- role-holder;
- passive record source;
- coerced participant;
- beneficiary;
- observer;
- dissenter;
- external constraint;
- accidental correlate.

Do not collapse these.

## Rule 5 — emergence does not erase provenance

Global pattern descriptions must preserve enough provenance to support attribution and intervention.

---

# 21. Relation to TLICA identity-correlation

Institutions can become integrated into individual identity to varying degrees.

For content `x = my role as judge / worker / citizen / parent / soldier / scientist`, TLICA's identity-correlation machinery can track how deeply the role participates in the agent's self-model.

But institutional realization cannot be reduced to high `rho`.

An agent can perform a role instrumentally with weak identity integration while still being a crucial causal carrier.

Conversely, an agent can identify strongly with an institution while occupying no role that materially affects its operation.

Therefore:

\[
\rho_i(\text{institution})
\]

and

\[
\text{causal/structural participation}_i
\]

must remain distinct.

This separation may become one of the TLICA-specific contributions to institutional analysis.

---

# 22. Relation to sourcehood

Institutional action frequently depends on source recognition.

A message with identical propositional content can trigger different behavior depending on whether it came from:

- a recognized supervisor;
- an unauthorized peer;
- a forged account;
- an automated system;
- a court;
- an external adversary.

Thus the institution is not only a content-distribution network.

It is a **source-sensitive relational system**.

This aligns strongly with TLICA's existing source-pathway concern.

A mature application should represent, for each operative directive `x`, not only content but source path:

\[
\operatorname{SrcPath}(x)=
(d_0,a_1,d_1,a_2,\ldots,a_k).
\]

Institutional legitimacy/validity may then be modeled as path-dependent rather than content-only.

---

# 23. Relation to osmotic imprinting

Institutions reproduce themselves partly through explicit instruction and partly through ambient exposure.

New members learn:

- what counts as normal;
- who is deferred to;
- which deviations are punished;
- how forms are actually processed;
- which written rules are central versus ceremonial;
- what language signals status;
- what shortcuts are tolerated;
- what behavior makes one legible as a competent role-holder.

Much of this is not acquired through deliberate verification.

Always-on osmotic imprinting therefore supplies a natural TLICA mechanism for institutional enculturation.

This also predicts divergence between:

\[
\text{codified institution}
\]

and

\[
\text{lived institution}.
\]

The lived institution is partly reconstructed through ambient regularities that may never be written down.

---

# 24. Codified versus lived institution

Define:

\[
\mathcal I_t^{\text{codified}}
\]

as the structure inferable from authoritative formal artifacts under a declared interpretation, and

\[
\mathcal I_t^{\text{lived}}
\]

as the structure actually realized through agents, relations, artifacts, and current practice.

Then generally

\[
\mathcal I_t^{\text{codified}}
\neq
\mathcal I_t^{\text{lived}}.
\]

The gap itself becomes measurable in principle.

Large gaps may predict:

- surprise to outsiders;
- selective enforcement;
- procedural fragility;
- onboarding difficulty;
- informal power concentration;
- sudden failure when tacit carriers leave;
- disagreement about "what the institution really is."

This distinction should be handled descriptively and empirically, not rhetorically.

---

# 25. Local discontinuity as frame-relative compression artifact

The central phenomenological idea can now be restated in TLICA language.

A person observes a local patch of primal not-I.

Their operative model compresses the accessible scene.

Most remote relation-state is absent from the local model because it is irrelevant until activation reaches the patch.

When a distributed path terminates locally, behavior changes suddenly.

The observer may then attribute the event to:

- irrationality;
- arbitrary authority;
- personality;
- coincidence;
- spontaneous choice;
- hidden intention.

Sometimes those attributions are correct.

But another possibility is:

\[
\boxed{
\text{the local frame discarded the support variables that made the transition predictable.}
}
\]

This is the connection to TLICA's broader concern with lossy models.

The institutional extension adds a specific class of discarded variables: **distributed social support structure**.

---

# 26. A stronger formulation: causal support can be nonlocal relative to the observer but local to reality

"Nonlocal" here must not be confused with quantum nonlocality.

The intended meaning is simply spatially, organizationally, or informationally remote relative to the observer's frame.

The causal path remains embedded in ordinary reality:

\[
\text{remote agent/artifact}
\to
\text{communication}
\to
\text{local trigger}
\to
\text{local behavior}.
\]

Thus:

> causal support can be nonlocal to the observer's representation while remaining entirely local and ordinary in the physical substrate.

This phrasing prevents metaphysical overreach.

---

# 27. What would count as genuine explanatory gain?

The application should be considered successful only if it accomplishes at least one of the following beyond relabeling known ideas:

1. derives a new discriminator between person-local and institution-distributed causes;
2. predicts failure under specific edge/artifact/profile ablations;
3. explains why role-preserving substitution and person-preserving edge destruction differ;
4. distinguishes codified from lived institutions with measurable consequences;
5. predicts when semantic divergence is harmless versus operationally catastrophic;
6. provides a source-pathway formalism that improves attribution of institutional action;
7. connects formation history to behavior under field changes in a way rival accounts do not;
8. supplies empirically useful observability-gap measures;
9. generates a principled anti-group-mind account while preserving causal realism.

If it does none of these, it should remain a conceptual translation note rather than a full TLICA application.

---

# 28. External literature that must be triangulated

Before publication, the paper must be pressure-tested against at least these families:

- philosophy of social ontology and institutional facts;
- collective intentionality;
- distributed cognition;
- situated cognition;
- actor-network and sociotechnical approaches;
- role theory;
- organizational sociology;
- institutional economics;
- distributed systems and fault tolerance;
- graph dynamical systems;
- multi-agent systems;
- category-theoretic / sheaf-theoretic models of contextual consistency;
- control and observability theory;
- legal theory on institutional authority and validity;
- computational models of norm emergence and enforcement.

The purpose is not citation accumulation. It is to discover whether the proposed object already exists under another name, which components are derivative, and where TLICA genuinely adds structure.

---

# 29. Formal development agenda

## F1 — define the carrier category

Specify agents, artifacts, roles, and relation types.

## F2 — define admissible local sections

What exactly does a role-holder carry?

## F3 — define compatibility

When are two local representations compatible enough to glue?

## F4 — define realization equivalence

When should two different carrier configurations count as the same institution for the task at hand?

## F5 — define critical-path provenance

How are source-paths represented and audited?

## F6 — define activation dynamics

How do latent role dispositions become operational?

## F7 — define institutional persistence

Which invariants must survive turnover?

## F8 — define observability gap

Can support visibility be measured without arbitrary support-set choices?

## F9 — define ablation semantics

What exactly does it mean to remove a person, edge, artifact, source relation, or recognition relation in a model?

## F10 — connect back to foundation without contamination

Demonstrate which objects are derived summaries over existing TLICA machinery and which, if any, expose a genuine missing primitive.

---

# 30. Computational toy model

A minimal simulation can instantiate:

- `N` agents;
- typed roles;
- directed authority/communication edges;
- local rule tables;
- source-trust predicates;
- artifact states;
- threshold activations;
- external events.

Example state:

```text
Agent:
    id
    role
    local_model
    source_trust
    active_rules
    latent_rules

Artifact:
    id
    type
    state
    authorized_writers

Edge:
    src
    dst
    type
    validity

Event:
    source
    content
    artifact_refs
    timestamp
```

Then compare models under interventions:

- remove document;
- remove relation;
- replace role-holder;
- forge source;
- partition network;
- introduce incompatible local maps;
- alter threshold;
- flatten external incentives;
- replay identical content over different source paths.

The output should track:

- action reachability;
- correctness relative to declared institutional rules;
- latency;
- failure mode;
- provenance;
- local observer predictability.

The simulation does not prove the social theory. It provides a calibrated testbed for internal consistency and discriminator design.

---

# 31. Candidate application-paper structure

A mature paper could use the following structure:

1. Introduction: the government-is-not-the-document problem
2. TLICA inheritance and anti-group-mind constraint
3. Distributed institutional realization object
4. Why vectors fail: relations and higher-order structure
5. Codified versus lived institution
6. Local sections and interoperability
7. Source-pathways and authority
8. Formation, activation, and apparent discontinuity
9. Local-projection proposition
10. Worked cases
11. Failure taxonomy
12. Formal toy model
13. Predictions and empirical paradigms
14. Rival-framework translations
15. Limits and open problems
16. Conclusion

---

# 32. Boundary conditions

The proposal does **not** currently establish:

- that institutions are literally vector spaces;
- that institutions are literally sheaves;
- that every social pattern is an institution;
- that every abrupt behavior has distributed institutional support;
- that the cultural-I and institutional realization are identical;
- that institutions possess consciousness;
- that institutional descriptions replace individual responsibility;
- that social causes violate physical closure;
- that the proposed realization operator is a foundation primitive;
- that TLICA has priority over existing social-ontology work.

These are explicit nonclaims.

---

# 33. Claim-status summary

**Disclosed within the current repository boundary:** TLICA already contains indexed-agent, relational, situational-field, source-sensitive, formation/activation, and distributed-cultural machinery that can host this extension without positing a group mind.

**Observed conceptually:** ordinary institutions exhibit carrier distribution, role substitution, artifact dependence, and local behavior whose support can lie outside the immediate observational frame.

**Conjectured:** a single distributed institutional realization scaffold can unify these phenomena in a way that earns application-level explanatory value.

**UNVERIFIED:** that the proposed `R_t` / `A_t` formalization predicts anything unavailable to simpler network, distributed-cognition, role, or institutional-fact models.

**Dark:** the mathematically natural final object class. Graph, hypergraph, category, sheaf, tensor-network, dynamical-system, or hybrid formulations remain live.

---

# 34. Conclusion

The central claim of this research program is modest but potentially fertile.

An institution can be real without being a person.

Its reality can consist in the presently realized organization of indexed people, their profile-conditioned dispositions, typed relations, material artifacts, records, communication channels, and situational constraints.

No single person need contain the whole structure.

No group mind need be invented.

The structure can nevertheless produce ordinary physical consequences because every operative path is implemented in agents and primal not-I.

From inside a small observational frame, such consequences can appear abrupt. A nearby person suddenly switches roles, enforces a rule, grants access, denies access, arrests, evacuates, transfers, signs, reports, or obeys. The event looks discontinuous only because the support structure was distributed outside the local projection until the moment it activated there.

The resulting research target is therefore:

\[
\boxed{
\text{distributed realization}
+\text{typed relational support}
+\text{activation}
+\text{local projection}
\Rightarrow
\text{apparent local discontinuity}
}
\]

with one strict requirement:

> every emergent explanation must be payable in indexed causal paths.

That constraint preserves TLICA's perspectival realism while allowing it to talk coherently about governments, firms, courts, norms, organizations, and other socially realized structures without either reducing them to paper or turning them into ghosts.
