# Distributed Institutional Realization

[← Wiki home](README.md) · Source: [`research/distributed_institutional_realization_2026-09-15/`](../research/distributed_institutional_realization_2026-09-15/README.md) · **Research note · v0.1.0 · UNVERIFIED · candidate *future* application paper**

> **Research-tier, and honest about it.** This is a research-program *seed*, not a finished
> application paper: dated rather than versioned, headed *toward* application-paper status but not
> there. Its central claims are **UNVERIFIED** — specifically, that naming the "institution
> object" earns its keep at all (C-006), and that the account predicts anything the plain
> distributed-systems / role-theory / social-ontology literatures don't already (C-025). It
> changes **nothing** in the frozen foundation. What *is* exact is a small toy model of a
> badge-controlled door — everything reaching past that toy carries its hedge in plain sight.
>
> **The one thing this page is careful never to do** is turn an institution into a *mind*. A
> government, a court, a firm — this page treats them as causally real **without** treating them
> as a person that believes, wants, or chooses. That discipline is the whole point, and the
> theory it extends already insists on it.

---

## The problem: the government is not the document

Picture a written constitution sitting alone in an empty archive. The paper is real — the ink,
the legal history, the meaning of the words. But the document by itself arrests no one, collects
no tax, appoints no judge. Add people who have never seen it and recognize no authority tied to
it, and it *still* isn't a working government.

Now add millions of people — each carrying only a partial, patchy picture — connected through
stable roles, procedures, records, communication channels, expectations, and physical
infrastructure. *Now* local reality starts to contain events that only make sense relative to a
structure no single person fully holds. An officer executes an order authored elsewhere. A clerk
rejects your application because a database state changed. A badge opens a door because it encodes
a role relation almost nobody nearby could verify from scratch.

We say "the government did X," "the court ordered Y." Useful shorthand — but it hides the
implementation, and it tempts two opposite mistakes:

- **Document reduction** — pretending the codified text *is* the live institution.
- **Group-mind reification** — pretending the institution is a new *person* that literally
  believes and wants.

The target is the object in between: a **distributed realized structure** — real enough to cause
events, but not a new mind.

## What is realized *now*

The proposal is that at any moment an institution is realized jointly by four things, none of
them a subject:

- **the people** and their role-conditioned profiles (`P`) — what each participant actually
  carries: their role knowledge, permissions, expectations, who they recognize as an authority;
- **the typed relations** among them and their artifacts (`R`) — *who reports to whom, who can
  command, who trusts a record from whom, who is authorized by what*. These are load-bearing:
  the same four people with their authority edges rewired are a different institution;
- **the artifacts and records** (`D`) — laws, credentials, databases, ledgers, buildings,
  network states — all sitting in ordinary physical reality;
- **the situational field** (`S`) — location, time, incentives, jurisdiction, current events.

The institution `I` is what these *realize together* — a relational state descriptor, not an
extra agent. And any sentence of the form "the institution caused this" is only allowed as
shorthand for a spelled-out path: *record state → a message → a role activating in a specific
person → that person's physical action*. No magic, no downward causation from a group ghost —
every arrow has to be payable in the actions of indexed people and things.

> **In plain terms —** an institution isn't the rulebook and it isn't a hive mind. It's *many
> people plus their relationships plus their paperwork plus the situation*, all meshing right now
> so that pushing here makes something happen there. Take the people away and keep only the book,
> or keep the people but cut the relationships, and the "institution" stops working — which tells
> you where it actually lived.

## Why abrupt behavior can be perfectly ordinary

Here is the idea the seed is really chasing. Stand at the door and watch: a badge approaches, the
door unlocks. Locally it can look as if the *plastic card itself* has authority — the event seems
to come from nowhere. But the real path ran through a role assignment, an administrator's database
update, a credential relation, and a controller query, most of it happening far outside your view
and only *arriving* at the door in the last step.

The slogan:

> **Apparent local discontinuity can be the projection of distributed causal structure onto an
> insufficient local frame.**

A bystander who sees a person suddenly switch roles, enforce a rule, grant or deny access, arrest,
evacuate, or obey — and calls it arbitrary, irrational, or "out of pocket" — may simply be missing
the distributed support that made the transition ordinary. Sometimes the arbitrariness is real.
But another live possibility is: *the local frame threw away the variables that made the event
predictable.*

The seed is careful that this must **not** collapse into the empty truism "hidden causes exist."
To earn its keep it has to say *which* hidden variables matter, *how* they're distributed, and
*which interventions* would sever the path — and then be checkable. That debt is stated, not
hidden.

## What the toy model actually shows

The badge-controlled door is [implemented and executed](../research/distributed_institutional_realization_2026-09-15/badge_door_demo.py)
as a small, deterministic, standard-library model (raw outputs
[here](../research/distributed_institutional_realization_2026-09-15/badge_door_demo_results.json)).
It realizes one micro-fact — "the door opens for the person at it" — and lets you *run* the
ablations. Executed results (all 14 self-checks pass):

- **Cut different pieces, get different failures.** A cloned badge with no authorization relation,
  a deleted record, a severed controller-to-database link, a forged update, an expired credential,
  and conflicting duplicate records each fail — and each fails in its *own distinct way*.
- **Relations beat persons.** Swap the employee for a different authorized role-holder and the
  door still opens — access follows the *relational state*, not the physical person. Keep the same
  person but cut their authorization edge and it stays shut. (This is prediction P2: role-preserving
  substitution preserves output better than person-preserving edge destruction.)
- **Identification is irrelevant to access.** Run the full 2×2×2×2 grid over relation × source ×
  activation × *how strongly the person identifies with the institution*, and the identification
  axis is **inert** — it never moves the outcome. Only the intact relation, valid source, and
  active rule do.

That last one matters, because it makes a TLICA-specific distinction concrete: **how deeply you
identify with an institution is a different thing from how much you causally run it.** You can be
a true believer with no operational role, or a detached clerk who is nonetheless load-bearing.

> **What the demo is NOT.** It demonstrates that the scaffold is internally consistent and that its
> discriminators behave — a mathematical possibility, checked. It is **not** a model of any real
> organization or person, and it does **not** prove the social theory. It doesn't touch the two big
> open questions below.

## What it borrows, and what it still owes

Almost everything here is **existing** theory machinery, recombined: indexed profiles and the
identity-correlation coordinate ρ, [source-pathways](app-agency-architecture.md),
[formation vs. activation](modes-of-development.md), [osmotic imprinting](app-out-of-the-cave.md),
[semantic interoperability](app-this-is-water.md), the [cultural-I](app-referent-routing.md), and
the anti-group-mind discipline the [agency papers](app-free-will.md) already state almost word for
word. The seed's job is to *name the object* those pieces gesture at and see whether naming it buys
anything.

Two debts stay open and are labeled **UNVERIFIED**, not quietly rounded up:

- **Is the "institution object" more than a renamed list?** (C-006) If every useful thing can be
  said just as well about the raw ingredients, the object should be deleted — the theory gets
  better by getting smaller.
- **Does this out-predict the existing literatures?** (C-025) Network theory, distributed cognition,
  role theory, institutional economics, social ontology, distributed systems — no novelty is
  claimed over any of them until a primary-source comparison is actually done.

The full seed, its 25-entry claim ledger, the reconciliation against `main`, and the falsification
plan live in the [research package](../research/distributed_institutional_realization_2026-09-15/README.md).

---

← Back to [the wiki home](README.md) · see also [Other Minds](other-minds.md), [Agency Architecture](app-agency-architecture.md), and the [glossary entry on "sheaf-like"](glossary.md).
