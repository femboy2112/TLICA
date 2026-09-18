# Distributed Institutional Realization

## Institutional macrostates, local discontinuity, and social structure without a group mind

**Author:** Leah.  
**Status:** first full manuscript draft, research-tier v0.2.0, 2026-09-15.  
**Architecture dependency:** TLICA Foundation v5.5.0 plus the current agency, cultural-I, source-path, formation/activation, and semantic-interoperability application machinery.  
**Epistemic status:** application-level formal proposal. Several propositions below are disclosed only inside the declared formal model. No empirical validation or novelty claim against external literatures is made here.

---

## Abstract

Institutions are causally consequential without being additional minds. Governments, courts, firms, access-control systems, offices, procedures, currencies, conventions, and bureaucracies are realized through indexed people, learned dispositions, typed relations, artifacts, records, communication pathways, and physical infrastructure. Yet ordinary language compresses these distributed realization paths into expressions such as “the court ordered,” “the company fired,” or “the government did.” Two errors then become tempting: reducing the institution to a document, or reifying the institution into a collective subject.

This paper develops a TLICA-compatible alternative. The first move is to distinguish the **micro-realization** of an institution from its **institutional macrostate**. At time `t`, let

\[
X_t=(\mathbf P_t,\mathbf R_t,\mathbf D_t)
\]

collect the relevant indexed agent profiles, typed agent/artifact relations, and material-symbolic artifact states. The situational field `S_t` is kept analytically external. For a declared institutional task family `T`, let

\[
\mathrm{Resp}_T(X;s,u)
\]

be the system's response under admissible situation `s` and intervention/input `u`. Two micro-realizations are institutionally equivalent for `T` when they have the same response signature over the declared intervention domain. The institutional macrostate is then the quotient class

\[
\mathcal I^T_t=[X_t]_{\sim_T}.
\]

This revision gives the institution object nontrivial content: it is not the tuple renamed, but an equivalence class under behaviorally relevant interventions. Distinct people, artifacts, or local representations may therefore realize the same institutional macrostate when their substitutions preserve the relevant response geometry. Conversely, preserving the same people while severing a load-bearing relation may move the system into a different institutional macrostate.

The second move concerns perspective. A local observer sees only a projection of the global realization. Behavior may therefore appear abrupt, arbitrary, or “out of pocket” when the causal support required to predict it lies outside the local frame and becomes visible only at activation. This is not offered as a universal excuse and not as the truism that hidden variables exist. The claim earns content only when the proposed distributed support improves prediction and intervention selection relative to matched irrelevant or false context.

The paper separates institutional realization from the cultural-I, identity-correlation from causal participation, formation from activation, institutional macrostate from situational field, and social shorthand from literal group agency. It reinterprets the existing badge-door toy model as a finite consistency witness rather than an empirical or factorial test, states the stronger probes still required, and leaves sheaf language gated until a genuine local-to-global formalization is specified. The result is a candidate application architecture for describing socially real structure while preserving TLICA's indexed-perspective discipline.

---

# 1. The object to recover

Consider a constitution, policy manual, access-control rule set, court order, or corporate charter stored in an archive.

The artifact is real. Its semantic and legal histories may matter. But the artifact alone does not arrest anyone, open a door, transfer money, issue a license, conduct payroll, appoint a judge, or enforce a deadline.

Now add people who neither recognize nor implement its authority. The document still does not become a live institution.

Now add:

- indexed people with partial and heterogeneous local models;
- role-conditioned dispositions;
- recognized authority relations;
- records and credentials;
- communication pathways;
- procedures and update rights;
- machines, buildings, databases, and physical tokens;
- learned expectations about what happens when certain states occur.

Local reality now contains events that cannot be predicted from the nearby physical scene alone. A person presents a card and a door unlocks. A clerk denies a request after a database state changes remotely. An officer abruptly begins acting under a role whose enabling path originated outside the observer's field. A company continues functioning after many employees leave because new people occupy structurally compatible positions.

The target of this paper is the structure that makes those events intelligible without adding a supernatural or phenomenal collective subject.

The core thesis is therefore deliberately narrow:

> **An institution may be causally real as a distributed, intervention-stable organization of indexed agents, relations, artifacts, and response pathways without being an additional mind.**

This is a proposal about representation and realization, not a claim that every social pattern is an institution or that all abrupt social behavior is institutionally explained.

---

# 2. Architectural inheritance from TLICA

This application does not begin from zero.

## 2.1 Indexed perspectives are retained

TLICA's agency papers already permit collective and institutional analysis through role-indexed profiles and relational cascades while refusing an unindexed group mind. Multi-agent explanation therefore remains decomposable into indexed participants plus relational structure.

The present paper does not weaken that constraint. Whenever ordinary language says

> “the institution did X,”

formal analysis must be able to recover an implementation path through indexed agents, artifacts, records, automated procedures, and physical actions.

## 2.2 The cultural-I is precedent, not identity

The cultural-I already provides a model of a distributed social pattern that is emergent over many individual Is without becoming an intending subject.

But cultural encoding is not the whole of institutional operation. A functioning institution may additionally require:

- typed authority relations;
- update permissions;
- provenance;
- role occupancy;
- records;
- machinery;
- access boundaries;
- activation conditions;
- communication and enforcement paths.

Accordingly, the working boundary is:

\[
\text{cultural-I}
\subseteq
\text{possible encoding component of institutional realization},
\]

not

\[
\text{cultural-I}=\text{institution}.
\]

This boundary remains application-level and should be re-audited whenever the cultural-I machinery changes.

## 2.3 Identity-correlation is not operational centrality

A person may be deeply identity-integrated with an institution and operationally peripheral. Another may dislike the institution while occupying a load-bearing role.

Therefore:

\[
\rho_i(\text{institution})
\not\equiv
\text{causal participation}_i.
\]

The distinction is structural. Whether and how the two correlate in real populations is empirical.

## 2.4 Formation is not activation

TLICA distinguishes the formation of a disposition from its activation. This becomes especially useful institutionally.

A firefighter can carry a role for years without fighting a fire. An evacuation protocol can be maintained without being enacted. A judge can occupy an office without continuously ruling. An emergency operator can possess a response policy that activates only when a particular message arrives.

Thus a sharp local regime switch need not imply that the enabling structure came into existence at the instant of action.

## 2.5 Source-path status is already available

An identical message can have different institutional force depending on provenance:

- recognized authority;
- unauthorized peer;
- forged authority;
- unknown source;
- delegated automated authority.

This application therefore reuses source-path/sourcehood machinery rather than inventing a duplicate scalar called “authority.”

## 2.6 Situational field must remain distinguishable

The previous seed placed `S_t` inside the arguments that generated the institution object while also asking to vary `S_t` independently of the institution. That creates an avoidable identifiability problem.

This draft repairs it.

The institution is defined from the presently available distributed organization:

\[
X_t=(\mathbf P_t,\mathbf R_t,\mathbf D_t),
\]

while the situational field remains external:

\[
S_t\in\mathcal S_T.
\]

The institution can alter the situation, and the situation can activate the institution, but they are not definitionally identical.

---

# 3. Why people are not enough

The motivating metaphor was to imagine people as basis units of a vector and the institution as structure realized over them.

Let

\[
V_A=\mathrm{span}\{e_1,\dots,e_n\}
\]

be a free vector space over indexed participants. A coefficient vector

\[
v=\sum_i c_i e_i
\]

could encode participation, activation, salience, probability, or another scalar feature.

But the same people with the same coefficients can instantiate radically different institutions depending on which relations hold among them.

Four people can be judge, clerk, officer, and defendant—or the same four bodies can have those role/authority edges permuted. A set of workers can retain identical individual beliefs while a critical authorization edge is removed. An organization can preserve nearly all of its personnel while its authoritative record system becomes invalid.

Therefore a person-vector cannot be the institutional object.

The vector metaphor survives only in the weak sense that people are carriers of local structure. The load-bearing object is relational.

---

# 4. Micro-realization

## 4.1 Indexed agent profiles

Let

\[
\mathcal A_t=\{a_1,\dots,a_n\}
\]

be the indexed participating agents relevant to a chosen institutional task family.

Each agent carries an application-relevant projection of their TLICA state:

\[
P_i(t).
\]

This can include, when relevant:

- role occupancy;
- recognized source paths;
- tool access;
- role-conditioned rules;
- identity-correlation placements;
- latent/active dispositions;
- semantic interface mappings;
- memory or record access;
- expectations about responses.

Collect them as

\[
\mathbf P_t=(P_1(t),\dots,P_n(t)).
\]

## 4.2 Artifacts and records

Let

\[
\mathbf D_t=\{d_1,\dots,d_m\}
\]

contain the relevant physically realized artifacts in primal not-I:

- documents;
- credentials;
- databases;
- ledgers;
- keys;
- machines;
- uniforms;
- buildings;
- network states;
- signed orders;
- message logs;
- account records;
- physical tokens.

Artifacts can constrain or transmit institutional states without being agents.

## 4.3 Typed relations

Let

\[
\mathbf R_t
\]

be a typed relation structure over agents and artifacts. A typed graph may suffice in many cases; a hypergraph or richer construction remains available when genuinely n-ary relations cannot be represented cleanly.

Representative relation types include:

- `occupies-role`;
- `recognizes-authority-of`;
- `is-authorized-by`;
- `can-update`;
- `can-read`;
- `must-respond-to`;
- `reports-to`;
- `trusts-record-from`;
- `is-bound-by`;
- `communicates-with`;
- `can-enforce`;
- `is-legible-as-role-to`;
- `has-jurisdiction-over`.

The typing is substantive. “Connected” is not enough when command, trust, access, and communication have different effects.

## 4.4 Micro-realization state

Define the micro-realization

\[
\boxed{
X_t=(\mathbf P_t,\mathbf R_t,\mathbf D_t)
}
\]

for the declared scope of analysis.

`X_t` is not yet the institutional macrostate. It is the detailed realization from which institutional equivalence will be defined.

This distinction is central to the revision.

---

# 5. Institutional task families and response signatures

An institution cannot be identified independently of every possible question. A hospital can be equivalent to another hospital with respect to emergency intake while differing with respect to research administration. Two access-control systems can be equivalent with respect to “who may open this door” while differing radically in logging or audit behavior.

Accordingly, define a **task family** `T` by specifying at least:

\[
T=(\mathcal S_T,\mathcal U_T,\mathcal Y_T,\ell_T),
\]

where:

- `\mathcal S_T` is the admissible situational domain;
- `\mathcal U_T` is the admissible intervention/input domain;
- `\mathcal Y_T` is the outcome space;
- `\ell_T` is a declared comparison or loss function when exact equality is inappropriate.

For deterministic systems define

\[
\mathrm{Resp}_T(X;s,u)\in\mathcal Y_T.
\]

For stochastic systems use a response distribution

\[
\mathrm{Resp}_T(X;s,u)\in\Delta(\mathcal Y_T).
\]

The complete response signature is

\[
\Sigma_T(X):
(s,u)\mapsto\mathrm{Resp}_T(X;s,u).
\]

This signature records what the micro-realization does across the situations and interventions declared relevant to the institutional question.

---

# 6. Institutional realization as an equivalence class

## 6.1 Exact institutional equivalence

Define

\[
X\sim_T X'
\]

iff

\[
\mathrm{Resp}_T(X;s,u)
=
\mathrm{Resp}_T(X';s,u)
\]

for every admissible

\[
(s,u)\in\mathcal S_T\times\mathcal U_T.
\]

Then define the institutional macrostate

\[
\boxed{
\mathcal I^T(X)=[X]_{\sim_T}.
}
\]

At time `t`,

\[
\mathcal I^T_t=\mathcal I^T(X_t).
\]

This is the first point at which the institution object earns formal work.

It is not

\[
\mathcal I_t=X_t
\]

under a new name.

It is a quotient object: many distinct micro-realizations may belong to the same institutional equivalence class.

## 6.2 Approximate institutional equivalence

Real institutions are noisy. Exact equality is often too strong.

For tolerance `\epsilon_T`, define

\[
X\sim_{T,\epsilon}X'
\]

when

\[
\sup_{(s,u)}
 d_T\big(
 \mathrm{Resp}_T(X;s,u),
 \mathrm{Resp}_T(X';s,u)
 \big)
\le\epsilon_T.
\]

This need not form an equivalence relation for arbitrary distances and tolerances; transitivity must be checked rather than assumed. Where transitivity fails, the appropriate object may be a clustering, pseudometric, or tolerance relation rather than a quotient.

The exact quotient therefore carries the clean formal theorem; approximate macrostates remain application-specific.

## 6.3 Why this solves the renamed-tuple problem

The previous candidate map

\[
\mathfrak R_t(\mathbf P_t,\mathbf R_t,\mathbf D_t,\mathbf S_t)=\mathcal I_t
\]

risked doing nothing more than renaming its inputs.

The revised map is the quotient projection

\[
\boxed{
q_T:X\mapsto[X]_{\sim_T}.
}
\]

Thus `I` contains strictly less micro-detail than `X` while preserving exactly the distinctions relevant to the declared response family.

This makes institutional persistence and carrier substitution expressible without pretending that identical people or artifacts must persist.

---

# 7. Factorization proposition

## Proposition 1 — response factorization through the institutional macrostate

Let `\sim_T` be defined by equality of the full response signature over `\mathcal S_T\times\mathcal U_T`. Then there exists a unique response function

\[
\overline{\mathrm{Resp}}_T
\]

on the quotient such that

\[
\mathrm{Resp}_T(X;s,u)
=
\overline{\mathrm{Resp}}_T([X]_{\sim_T};s,u).
\]

Equivalently, the diagram factors as

\[
X
\xrightarrow{q_T}
\mathcal I^T
\xrightarrow{\overline{\mathrm{Resp}}_T}
\mathcal Y_T.
\]

### Proof

By definition, all members of an equivalence class have identical response signatures. Therefore choose any representative `X` of a class `[X]` and define

\[
\overline{\mathrm{Resp}}_T([X];s,u)
:=
\mathrm{Resp}_T(X;s,u).
\]

The definition is independent of representative because equivalent microstates have equal responses for every admissible `(s,u)`. Uniqueness follows because `q_T` is surjective onto the quotient. ∎

### Interpretation

This proposition is mathematically elementary. Its value is architectural rather than novel mathematics.

It says that once task-relative response equivalence has been declared, the institution can legitimately function as a causal macrostate for that task: all micro-detail discarded by the quotient is irrelevant to the declared response family.

This is **Disclosed inside the formal model**. It does not establish that a particular real-world choice of `T`, state variables, or response map is empirically adequate.

---

# 8. Carrier substitution and institutional persistence

## 8.1 Carrier substitution

Let

\[
g:X\mapsto X'
\]

replace one or more physical carriers—people, artifacts, machines, records—while preserving some relevant role/relational organization.

If

\[
X\sim_T g(X),
\]

then

\[
\mathcal I^T(X)=\mathcal I^T(g(X)).
\]

Therefore carrier identity may change while the institutional macrostate persists.

This gives precise content to the intuition that an institution is not identical to its present members.

## 8.2 Relation destruction

Conversely, holding carrier identity fixed while severing a load-bearing relation may produce

\[
X\not\sim_T X'.
\]

The same people can therefore realize a different institution—or no functioning institution for task `T`—after relational failure.

## 8.3 Persistence over time

Define exact institutional persistence over interval `[t_0,t_1]` by

\[
\mathcal I^T_t
=
\mathcal I^T_{t_0}
\quad
\forall t\in[t_0,t_1].
\]

This is stronger than necessary for most empirical work. A more realistic account will track distance between response signatures or changes among task-relevant equivalence classes.

But the quotient construction already explains how substantial turnover can coexist with institutional persistence:

\[
X_t\neq X_{t+\Delta}
\qquad\text{while}\qquad
\mathcal I^T_t=\mathcal I^T_{t+\Delta}.
\]

---

# 9. Institution, situation, activation, output

The previous seed blurred institutional organization and situational state. The revised causal grammar is:

\[
\boxed{
X_t
\xrightarrow{q_T}
\mathcal I^T_t
}
\]

followed by

\[
\boxed{
Y_{t+\Delta}
=
\mathscr A_T(\mathcal I^T_t,S_t,U_t),
}
\]

where:

- `\mathcal I^T_t` is the available institutional macrostate;
- `S_t` is the external situational/material field;
- `U_t` is an input/intervention/event;
- `Y` is the realized outcome.

This separation matters.

A fire department can exist when there is no fire. A court can exist between cases. An evacuation system can remain formed while no alarm is active. The fire, case, or alarm is not part of the institution in the same sense as the maintained role and response structure.

The situation can instead activate a latent path:

\[
\text{formed institutional structure}
+
\text{trigger}
\to
\text{role activation}
\to
\text{local action}.
\]

This is the institutional analogue of TLICA's formation/activation distinction.

---

# 10. Local projection and apparent discontinuity

## 10.1 Local observation

Let a local observer have access only to

\[
O^L_t=\pi_L(X_t,S_t),
\]

where `\pi_L` discards most remote institutional support variables.

A globally predictable event may be locally surprising when the variables needed for prediction lie outside `O^L_t`.

The central thesis can therefore be restated:

> **Apparent local discontinuity is sometimes a property of observation under projection, not a discontinuity in the realized causal path.**

## 10.2 Predictive-gap formulation

Suppose `Y` is the terminal institutional outcome.

A candidate diagnostic is the predictive-information gap

\[
\Lambda_L^T
=
H(Y\mid O^L)
-
H(Y\mid X,S),
\]

when probabilistic quantities are well-defined.

Equivalently,

\[
\Lambda_L^T
=I(Y;X,S\mid O^L),
\]

which measures how much outcome-relevant information is missing from the local frame.

This does not by itself identify an institution. It is a general observability quantity. The institutional contribution lies in identifying the structured support variables—roles, source paths, records, activation states, interface relations—that account for the gap.

## 10.3 Nontriviality condition

The local-discontinuity thesis earns scientific content only if:

1. a specific distributed support path is named before outcome inspection;
2. exposure of the correct support improves prediction or intervention selection;
3. matched irrelevant context does not produce the same improvement;
4. plausible false support does not perform equivalently;
5. ablating a predicted support component changes the outcome in the predicted direction.

Otherwise the account degenerates into post-hoc storytelling.

---

# 11. Government as a worked ontology

The word “government” compresses several distinct objects.

## 11.1 Codified structure

Let

\[
D^{\text{gov}}
\]

contain constitutions, statutes, regulations, orders, records, credentials, databases, and other formal artifacts.

These are part of the micro-realization but not sufficient for a functioning government.

## 11.2 Local role models

Different agents hold different partial maps:

\[
M_i(D^{\text{gov}},R^{\text{gov}}).
\]

A judge, clerk, citizen, officer, regulator, and attorney need not share one total representation.

Institutional operation may depend only on compatibility at the interfaces relevant to the task.

## 11.3 Institutional macrostate

For some declared task family—for example adjudication, tax collection, or permit processing—many different personnel and artifact configurations may implement the same response signature.

The institutional macrostate is therefore not “all people added together.” It is the equivalence class of micro-realizations that preserve the declared response geometry.

This also clarifies institutional change. A government can retain the same buildings, documents, and many of the same people while a transformation of authority/provenance relations changes the institutional macrostate relevant to a task.

---

# 12. Codified institution and lived institution

Let

\[
X^{\text{codified}}
\]

be the micro-realization inferred from formal rules and declared organizational artifacts.

Let

\[
X^{\text{lived}}
\]

be the micro-realization recovered from actual operational paths.

They may differ because of:

- tacit routines;
- unused formal procedures;
- unofficial intermediaries;
- learned workarounds;
- informal trust networks;
- undocumented bottlenecks;
- role expectations acquired by osmotic exposure;
- divergence between nominal and effective authority.

The scientifically useful question is not merely whether they differ, but whether

\[
\Sigma_T(X^{\text{lived}})
\]

predicts observed institutional behavior better than

\[
\Sigma_T(X^{\text{codified}}).
\]

That is empirically testable in bounded systems.

---

# 13. Semantic interoperability as an institutional condition

An institution need not require identical internal world-models.

Let two agents possess representations

\[
M_i\neq M_j.
\]

They may still coordinate successfully if the interface relevant to task `T` preserves the required relational structure.

This motivates a distinction between:

\[
\text{global representational similarity}
\]

and

\[
\text{task-specific interface compatibility}.
\]

A particularly strong test would compare the full four cells:

1. high similarity / high compatibility;
2. high similarity / low compatibility;
3. low similarity / high compatibility;
4. low similarity / low compatibility.

If low-similarity/high-compatibility systems outperform high-similarity/low-compatibility systems on the task, the result would support the institutional relevance of TLICA's semantic-interoperability distinction.

---

# 14. Source paths and institutional force

Consider a fixed proposition:

\[
m=\text{“perform action }a\text{.”}
\]

Its institutional effect may depend on the source path:

\[
\mathrm{Effect}(m,\mathrm{SrcPath}_1)
\neq
\mathrm{Effect}(m,\mathrm{SrcPath}_2).
\]

Examples include:

- a signed court order versus an identical forged PDF;
- a supervisor command versus a coworker repeating the same words;
- an authenticated database update versus an unauthenticated write;
- an automated message issued under delegated authority versus an arbitrary bot message.

The TLICA question is not whether provenance matters—that is already common institutional structure—but whether existing source-path machinery supplies useful cross-domain distinctions without duplicate primitives.

---

# 15. Identity-correlation and causal participation

Define a task-relative operational participation measure

\[
\chi^T_i(X)
\]

only after specifying an intervention criterion—for example, the change in output distribution under admissible ablation or replacement of agent `i` or relations incident to `i`.

Then identity placement

\[
\rho_i(\text{institution})
\]

and operational participation

\[
\chi^T_i
\]

are distinct variables.

All four cells are conceptually possible:

| Identity-correlation | Operational participation | Example shape |
|---|---|---|
| high | high | deeply identified role-holder with central authority |
| high | low | devoted supporter with little operational control |
| low | high | detached clerk/operator occupying a critical path |
| low | low | peripheral participant with weak identification |

The existence of a model in which these dissociate is easy to construct. The empirical distribution of the four cells is not established by construction.

---

# 16. Attribution without group-mind reification

The macrostate abstraction does not authorize collective phenomenology.

From

\[
\mathcal I^T_t
\]

one may infer institutional capacities or response equivalence for task `T`.

One may not infer:

- a collective phenomenal subject;
- collective feelings;
- collective intent without an explicit decision procedure and indexed implementation;
- equal responsibility among all carriers;
- endorsement from participation;
- moral guilt from network membership.

Statements such as “the court intends” or “the company believes” remain ordinary-language organizational shorthand unless an attributable institutional decision procedure is explicitly defined.

Responsibility continues to require indexed production paths.

---

# 17. Re-reading the badge-door toy model

The current repository contains an executed badge-door model with:

- one baseline path;
- eight ablations;
- a nominal `2×2×2×2` grid over relation, source, activation, and identity placement;
- fourteen passing self-checks.

It is useful, but its epistemic status must be stated precisely.

## 17.1 What it genuinely demonstrates

The model is a finite constructive witness that a coherent system can represent distinct failure classes for:

- missing relation;
- severed communication;
- invalid provenance;
- inactive time window;
- record divergence;
- carrier-without-role relation.

It also demonstrates that a role-relative authorization model can preserve output under compatible role-holder substitution while failing under deletion of the authorization relation.

Therefore it establishes **mathematical possibility/internal consistency inside the declared model**.

## 17.2 What it does not test

The model's `rho_institution` variable is deliberately never read by the access decision function. Consequently, identity-correlation invariance is built into the model.

Thus the run establishes:

> there exists a coherent model in which identity-correlation is operationally inert for this access decision.

It does not establish:

> identity-correlation is generally inert in institutions.

Likewise, the record authorizes a role rather than a named person. Role-preserving substitution therefore succeeds by construction. The model demonstrates one realizable institutional architecture, not a general empirical law of institutions.

## 17.3 Why the old factorial is not fully orthogonal

The nominal four factors are not all independently exposed to the decision rule in every cell.

When the relation is absent, no authorization record exists, so downstream source and activation states are operationally censored. When source validation fails, the function returns before evaluating the activation window.

The model therefore implements a serial gate:

\[
R\to Src\to A\to Y,
\]

rather than a fully orthogonal factorial in which every latent factor remains independently measurable in every cell.

The existing output remains valid as a pipeline trace. Mixed-term claims should not be inferred from it.

This correction is important because TLICA's own complete-factorial discipline requires every cell to carry the declared factors rather than allowing earlier gates to erase them.

---

# 18. Revised computational program

## 18.1 Probe A — institutional quotient toy model

Construct two or more distinct micro-realizations

\[
X_1\neq X_2
\]

with identical response signatures over a declared task domain:

\[
\Sigma_T(X_1)=\Sigma_T(X_2).
\]

Then construct a third micro-realization

\[
X_3
\]

that differs only by a load-bearing relation and satisfies

\[
\Sigma_T(X_3)\neq\Sigma_T(X_1).
\]

This directly demonstrates the macrostate quotient:

\[
[X_1]_T=[X_2]_T\neq[X_3]_T.
\]

The important point is not merely that two runs return the same output once, but that they match over the declared intervention family.

*Implemented and executed.* This probe is realized as a deterministic standard-library
model in [`quotient_demo.py`](quotient_demo.py) (raw outputs in
[`quotient_demo_results.json`](quotient_demo_results.json)). It builds a small
"who may approve request-type `k`" institution and exhibits six distinct
micro-realizations — differing in people, headcount, and record labels — that collapse
to exactly **three** institutional macrostates. Executed results (12/12 self-checks):
distinct micro-realizations sharing a response signature land in one class
(`[X_1]_T=[X_2]_T=[X_2']_T`); a pure carrier permutation preserves the class; cutting a
single load-bearing authority relation moves a realization to a different class
(`[X_3]_T\neq[X_1]_T`) even when the *people* are unchanged; the induced
`\overline{\mathrm{Resp}}_T` is single-valued on each class and reproduces
`\mathrm{Resp}_T` on **all 36** `(X,s,u)` cells with zero mismatches (Proposition 1,
executed); the quotient is strictly coarser than identity on micro-realizations (six to
three), so `\mathcal I^T` carries strictly less than `X`; and the approximate-equivalence
relation of Section 6.2 is exhibited as **non-transitive** by an explicit counterexample,
confirming that `[X]_{\sim_{T,\epsilon}}` must not be written without a transitivity check.
The demo is a finite constructive witness of this section's construction — **Disclosed
inside the formal model** — not empirical validation of any real institution (C-006's
empirical usefulness remains **UNVERIFIED**).

## 18.2 Probe B — genuinely orthogonal four-factor model

Represent relation, source validity, activation, and identity as explicit independent latent variables in every cell.

Do not remove the source object when relation is false. Do not suppress activation state when source validation fails. Record all four states plus final response in every cell.

If the response rule is serial, say so. If interactions are claimed, estimate them from the complete cells rather than from early-return failure labels.

## 18.3 Probe C — person-relative versus role-relative rival models

Build two independent candidate architectures:

\[
M_{\text{role}}
\]

and

\[
M_{\text{person}}.
\]

Under `M_role`, authority attaches to compatible role occupancy.

Under `M_person`, authority attaches to a specific indexed carrier.

Generate holdout cases and test which architecture predicts them. This turns role-substitution from a stipulation into a model comparison.

## 18.4 Probe D — local-discontinuity observer experiment

Present the same terminal event under:

1. local-only information;
2. correct distributed support;
3. matched irrelevant context;
4. plausible false support.

Measure:

- prediction accuracy;
- intervention selection;
- confidence calibration;
- arbitrariness attribution;
- individual-disposition attribution.

The load-bearing outcome is not subjective narrative satisfaction. It is whether correct distributed support improves prediction/intervention performance specifically.

## 18.5 Probe E — codified versus lived workflow

Choose a bounded low-risk real system—open-source contribution workflow, library checkout, room booking, volunteer coordination, or software incident response.

Recover formal procedure and observed action paths separately.

Compare:

\[
\mathrm{Err}_T(X^{\text{codified}})
\quad\text{versus}\quad
\mathrm{Err}_T(X^{\text{lived}}).
\]

The lived model earns explanatory value only if it predicts actual transitions better on holdout events.

---

# 19. Institutional failure taxonomy

The micro/macro distinction supports several nonidentical failure classes.

### 19.1 Carrier failure
A required person or artifact disappears.

### 19.2 Relational failure
The carriers remain but a load-bearing authority/access/communication relation is severed.

### 19.3 Provenance failure
The content exists, but its source path is invalid or untrusted.

### 19.4 Activation failure
The disposition or rule exists but the triggering conditions are absent or incorrectly detected.

### 19.5 Interface failure
Connected components interpret the interface incompatibly.

### 19.6 Record divergence
Replicas or authoritative artifacts disagree in a way the system cannot resolve.

### 19.7 Model drift
Local participant maps diverge enough that previously compatible interfaces stop functioning.

### 19.8 Codified/lived divergence
Formal procedures and effective operational paths cease to match.

### 19.9 Capture
A formally preserved institution may move to a different task-relative macrostate because response behavior changes while surface carriers and documents remain similar.

This taxonomy should be treated as a candidate modeling vocabulary, not a claim that all institutional failures decompose uniquely into these classes.

---

# 20. Institutional invariants

The quotient construction suggests candidate invariants.

## 20.1 Response-signature invariant

By definition,

\[
\Sigma_T(X)
\]

is invariant within an exact institutional equivalence class.

## 20.2 Carrier invariance

For a class of substitutions `G_T`, institutional persistence under carrier change means

\[
q_T(gX)=q_T(X)
\quad\forall g\in G_T.
\]

## 20.3 Provenance invariance

Some institutions may tolerate replacement of a physical record while requiring preservation of its recognized provenance chain.

## 20.4 Interface invariance

Global local-model content may vary while task-relevant overlap mappings remain behaviorally equivalent.

These are not universal properties of all institutions. They are dimensions along which particular institutional task families can be characterized.

---

# 21. What would make sheaf language legitimate

The local-to-global structure still suggests sheaf-like mathematics, but the gate remains closed until all ingredients are explicit.

A formal sheaf treatment must specify:

1. base object or site;
2. cover / local patches;
3. section assigned to each patch;
4. restriction maps;
5. compatibility criterion on overlaps;
6. gluing condition;
7. a nontrivial obstruction;
8. an observable institutional consequence of that obstruction.

A promising candidate would use information-access or role neighborhoods as patches and local permission/source/transition structures as sections.

But if typed graphs plus explicit interface maps already express every needed result, the sheaf formalism should be discarded.

No declared gluing machinery, no sheaf claim.

---

# 22. Rival frameworks and novelty debt

The present architecture is not entitled to novelty merely because it uses TLICA vocabulary.

At minimum it must be compared against independent traditions including:

- social ontology / institutional facts;
- collective intentionality and shared agency;
- distributed cognition;
- situated cognition;
- actor-network and sociotechnical approaches;
- role theory;
- organizational sociology;
- institutional economics;
- distributed systems;
- multi-agent systems;
- observability and control;
- local-to-global/sheaf formalisms.

The comparison must use primary sources and provenance-normalized source families.

The key question is not “does another literature say institutions are distributed?” Many do.

The key question is whether TLICA contributes a useful combination of distinctions that competitors do not jointly preserve:

\[
\boxed{
\rho\text{ placement}
\;\perp\;
\text{causal participation},
}
\]

plus source-path status, formation/activation, indexed attribution, semantic interoperability, and perspectival observability.

If generic network or distributed-systems language explains all results equally well, this project should be presented as a translation bridge rather than a new application theory.

---

# 23. Candidate empirical predictions

These predictions remain **UNVERIFIED**.

## P1 — correct distributed support improves intervention prediction

Given a locally surprising institutional event, observers given the true distributed support path should identify effective interventions better than observers given equal-volume irrelevant or false context.

## P2 — role-preserving substitutions preserve some institutional outputs better than person-preserving relation destruction

This applies only in domains where the operative task is role-relative rather than person-relative. The rival-model probe must establish which domain one is in.

## P3 — interface compatibility can dominate global representational similarity

For distributed tasks, low-similarity/high-interface-compatibility systems can outperform high-similarity/low-interface-compatibility systems.

## P4 — source-path validity changes action uptake under fixed propositional content

Identical directives transmitted through distinct source paths produce different response distributions.

## P5 — lived workflow outpredicts codified workflow in systems with substantial tacit practice

Where informal paths are genuinely load-bearing, `X_lived` should reduce holdout transition error relative to `X_codified`.

## P6 — identity-correlation and operational centrality exhibit empirical dissociation

Real populations should contain cases in all four cells of high/low identity placement × high/low operational participation.

## P7 — local apparent arbitrariness increases as outcome-relevant support becomes less observable

This must survive irrelevant-context and false-narrative controls.

---

# 24. Boundaries and nonclaims

This paper does **not** claim:

- that institutions are conscious;
- that group minds do or do not exist metaphysically;
- that every institution requires many people;
- that every social pattern is an institution;
- that all local surprise has distributed institutional causes;
- that documents are unimportant;
- that people are literally vector basis elements;
- that identity-correlation is generally causally inert;
- that role identity always dominates person identity;
- that the quotient construction is novel mathematics;
- that the proposed state variables are empirically sufficient;
- that TLICA currently outperforms existing social or systems theories;
- that sheaf theory has been formally established here.

The quotient construction is an analytical discipline: declare the task, declare the admissible interventions, declare what microdetail is retained, and let response equivalence determine whether distinct realizations count as the same institutional macrostate.

---

# 25. Claim-status update

The v0.1 ledger should be revised as follows if this manuscript is internalized.

### C-006 — usefulness of the institutional object

**Old:** UNVERIFIED; risk of renamed tuple.

**Revised:** **Disclosed inside the formal model that a quotient macrostate is nonidentical to the micro-realization tuple and supports exact response factorization. Empirical usefulness remains UNVERIFIED.**

The debt changes from “is it literally more than a tuple?” to:

> does the task-relative quotient produce useful stable macrostates in real or independently specified institutional domains?

### C-008 — local discontinuity

Remain **Conjectured**. The correct-support versus irrelevant/false-support observer probe has not run.

### C-010 — interface compatibility

Remain **Conjectured**.

### C-015 — source-path contribution

Remain **Observed as common institutional structure; TLICA-specific gain UNVERIFIED**.

### C-016 — role substitution

Downgrade any suggestion that the existing badge model empirically supports the general claim. The old demo is a constructive existence witness because role-relative authorization was built in.

### C-022 — identity-correlation / participation dissociation

Revise to:

**Disclosed as a logically coherent dissociation in the constructed finite model; empirical prevalence and causal coupling remain UNVERIFIED.**

The previous “factorial” does not independently test the effect because rho is excluded from the decision rule by construction.

### C-025 — TLICA-specific gain

Remain **UNVERIFIED** until primary-source rival tomography and discriminating holdouts are completed.

---

# 26. Why the macrostate move matters conceptually

The original intuition can now be stated without leaning too heavily on the vector metaphor.

A person is not a scalar coordinate containing one chunk of “government.”

Rather, people and artifacts are **carriers of local structure** inside a micro-realization. Some carrier substitutions preserve the intervention-response geometry; some relation changes do not.

The institution, for a declared task, is what remains invariant under exactly those changes that do not alter the relevant response signature.

Thus:

\[
\boxed{
\text{institution}
=
\text{task-relative invariant class of distributed realizations}
}
\]

rather than

\[
\text{institution}
=
\text{document}
\]

or

\[
\text{institution}
=
\text{sum of people}
\]

or

\[
\text{institution}
=
\text{group person}.
\]

This makes precise why a government can persist through personnel turnover, why the same personnel can cease to instantiate the same institution after authority relations collapse, and why a local observer can encounter actions whose support is spatially, temporally, and representationally distributed.

---

# 27. Relation to the “cosmos first” intuition

The same architecture echoes a broader TLICA commitment: realized behavior cannot be understood by isolating only the terminal local object.

A conscious experience depends on a developmental and physical realization history. Likewise, an institutional action can depend on a distributed social and material realization history.

The point is not that everything must always be modeled at maximal scale. The point is that **compression must preserve whichever variables are load-bearing for the question being asked**.

When the local frame discards those variables, the resulting world-model may make ordinary behavior appear discontinuous.

The remedy is not infinite detail. It is task-relative retention of causal structure.

---

# 28. Research order from here

The next phase should resist adding more ontology until the following are completed:

1. implement an explicit response-signature quotient toy model with at least two distinct micro-realizations in the same macrostate and one nearby micro-realization outside it;
2. rebuild the four-factor probe with independently represented latent factors and no early-return censoring;
3. construct role-relative and person-relative rival models and compare on holdouts;
4. run the local-observer correct/irrelevant/false support experiment;
5. recover a bounded codified-versus-lived real workflow;
6. populate the primary-source rival-framework matrix;
7. attempt a genuine local-to-global obstruction before retaining any sheaf language;
8. update the claim ledger only after those probes.

The manuscript should be promoted to a finished application paper only if at least one TLICA-specific distinction survives these comparisons and produces independent explanatory or predictive gain.

---

# 29. Conclusion

Social structures can be real without being people.

The central mistake to avoid is collapsing three different levels:

\[
\text{micro-realization}
\neq
\text{institutional macrostate}
\neq
\text{local observation}.
\]

The micro-realization contains indexed people, typed relations, artifacts, records, and local profile states. The institutional macrostate is the task-relative equivalence class that preserves the declared intervention-response signature. The local observer sees only a projection of that realization and may therefore experience an activation as abrupt when its support was distributed elsewhere.

This gives the original intuition a cleaner mathematical form. People are not literally coordinates whose sum becomes government. They are among the carriers of a relational realization. An institution persists when the relevant response geometry survives changes of carrier; it changes when the response geometry changes, even if many surface carriers remain.

The model remains deliberately modest. It does not create a group mind, does not claim institutional consciousness, and does not yet establish empirical superiority over existing network, social-ontology, organizational, or distributed-systems accounts.

Its strongest current result is internal:

\[
\boxed{
\text{a task-relative institutional macrostate can be defined as a quotient of distributed micro-realizations by intervention-response equivalence.}
}
\]

The next burden is empirical and comparative: determine whether this macrostate, together with TLICA's distinctions among identity, source, activation, semantic interoperability, and local observability, predicts anything that simpler rival models do not.

Until then, the structure is a disciplined candidate—not a settled theory.
