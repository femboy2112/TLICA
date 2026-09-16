# Distributed Institutional Realization

[← Wiki home](README.md) · Source: [`research/distributed_institutional_realization_2026-09-15/`](../research/distributed_institutional_realization_2026-09-15/README.md) · **Research note · v0.2.0 · UNVERIFIED · candidate *future* application paper**

> **Research-tier, and honest about it.** This is a research-program draft (**v0.2**), not a
> finished application paper: dated rather than versioned, headed *toward* application-paper
> status but not there. Two things about its central claim have now come apart. That the
> "institution object" is genuinely *more than a renamed list* — a real quotient that the
> response map factors through — is settled *inside the model* and has been **executed** in a
> toy (the formal half of claim C-006). But whether that object *earns its keep in the real
> world* — predicting anything the plain distributed-systems / role-theory / social-ontology
> literatures don't already (the empirical half of C-006, and C-025) — stays **UNVERIFIED**. It
> changes **nothing** in the frozen foundation. Everything reaching past the executed toys
> carries its hedge in plain sight.
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

## What is realized *now* — and why it's a *class*, not a list

Start with the concrete pile of stuff, at one moment, none of it a subject — call it the
**micro-realization**:

- **the people** and their role-conditioned profiles (`P`) — what each participant actually
  carries: their role knowledge, permissions, expectations, who they recognize as an authority;
- **the typed relations** among them and their artifacts (`R`) — *who reports to whom, who can
  command, who trusts a record from whom, who is authorized by what*. These are load-bearing:
  the same four people with their authority edges rewired are a different institution;
- **the artifacts and records** (`D`) — laws, credentials, databases, ledgers, buildings,
  network states — all sitting in ordinary physical reality.

Here is the move that makes v0.2 more than v0.1. The institution is **not** that pile renamed.
Pick a **task** you care about — say, "who can get a request of type *k* approved?" — and its
allowed situations and interventions. Two completely different piles of people-and-paperwork
count as **the same institution for that task** exactly when they *answer every question in the
task the same way*. The institution is the **equivalence class** of all micro-realizations that
share that response pattern. Swap in a different crew who preserve the answers and you have the
*same* institution; keep the exact same people but cut a load-bearing authority edge so an
answer flips, and you now have a *different* one. That is why a government survives total staff
turnover, and why the same staff can stop being that government the moment its authority
relations collapse.

The **situation** — location, time, incentives, jurisdiction, today's events — is deliberately
kept *outside* this. It doesn't help *define* the institution; it *activates* it. A fire
department is fully a fire department with no fire burning; the fire is what switches a latent
part of it on. And any sentence of the form "the institution caused this" is still only allowed
as shorthand for a spelled-out path: *record state → a message → a role activating in a specific
person → that person's physical action*. No magic, no downward causation from a group ghost —
every arrow has to be payable in the actions of indexed people and things.

> **In plain terms —** an institution isn't the rulebook and it isn't a hive mind, and it isn't
> even *this* particular set of people and files. It's the *pattern of who-can-make-what-happen*
> that a set of people-plus-relationships-plus-paperwork produces. Any pile that produces the
> same pattern counts as the same institution; change the people but keep the pattern and it
> persists; keep the people but break the pattern and it's gone. The situation isn't part of
> the institution — it's the thing that flips its switches.

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

## What the toy models actually show

Two small, deterministic, standard-library models come with this note. Both are **executed**;
both are *finite consistency witnesses* — they check that the construction is coherent and does
what the manuscript says — and **neither** is a model of a real organization or evidence for the
social theory.

**The quotient demo — the v0.2 headline** ([code](../research/distributed_institutional_realization_2026-09-15/quotient_demo.py),
[raw outputs](../research/distributed_institutional_realization_2026-09-15/quotient_demo_results.json))
builds a tiny "who may approve request-type *k*" institution and *runs* the equivalence-class
construction. Executed results (all **12** self-checks pass):

- **Distinct piles, one institution.** Six micro-realizations that differ in people, headcount,
  and record labels collapse to exactly **three** institutions. Three of them — different people,
  different counts — share the approval pattern and land in one class: swap the crew, keep the
  institution.
- **Break the pattern, change the institution.** Cut one load-bearing authority relation and a
  realization jumps to a *different* class even when the people are unchanged; a pure rename of
  everyone keeps the class.
- **The object is genuinely smaller than the pile.** The response map factors *exactly* through
  the class — the same answers come back whether you read the full pile or just its class, on all
  36 question-cells with zero mismatches — and there are strictly fewer classes than piles. That
  is the precise sense in which the institution "object" is not the list renamed: it *forgets*
  everything the task doesn't care about, and keeps exactly what it does.
- **A caught foot-gun.** *Approximate* sameness ("close enough on every question") turns out **not**
  to chain: the demo exhibits A≈B and B≈C but A≉C. So the tidy exact-equivalence story cannot be
  waved at noisy real data without more care — a caveat the model makes concrete rather than
  hand-waves.

**The badge-door demo** ([code](../research/distributed_institutional_realization_2026-09-15/badge_door_demo.py),
[raw outputs](../research/distributed_institutional_realization_2026-09-15/badge_door_demo_results.json))
realizes one micro-fact — "the door opens for the person at it" — and lets you run ablations
(14 self-checks pass). It genuinely shows that **cutting different pieces gives different, distinct
failures** (a cloned badge with no authorization, a deleted record, a severed link, a forged
update, an expired credential, conflicting duplicates — each fails in its own way). But v0.2 is
careful about *what the other results are worth*, because they are **built in, not discovered**:

- **"Relations beat persons" is a construction, not a finding.** Authorization in the model
  attaches to a *role*, so of course a compatible role-holder can be swapped in. This shows *one
  coherent way* an institution could be role-relative — not that real institutions generally track
  roles over persons. Telling those apart needs a rival "authority attaches to a specific person"
  model raced on fresh cases, which **hasn't been run**.
- **"Identification is irrelevant to access" is stipulated.** The code *never reads* how strongly
  anyone identifies with the institution when it decides the door — so its irrelevance is baked in,
  not learned from the run. What that *does* legitimately show is that the two ideas — **how deeply
  you identify with an institution** and **how much you causally run it** — *can* come apart
  coherently. Whether they come apart in real people is a separate, open question.
- **The old "2×2×2×2 grid" is a pipeline trace, not an experiment.** The checks run in series
  (no relation → nothing downstream even gets evaluated), so the sixteen rows are valid
  configurations but **not** an independent-factor design; no "these factors interact" claim can
  be read off it.

## What it borrows, and what it still owes

Almost everything here is **existing** theory machinery, recombined: indexed profiles and the
identity-correlation coordinate ρ, [source-pathways](app-agency-architecture.md),
[formation vs. activation](modes-of-development.md), [osmotic imprinting](app-out-of-the-cave.md),
[semantic interoperability](app-this-is-water.md), the [cultural-I](app-referent-routing.md), and
the anti-group-mind discipline the [agency papers](app-free-will.md) already state almost word for
word. The seed's job is to *name the object* those pieces gesture at and see whether naming it buys
anything.

The debts that stay open are labeled **UNVERIFIED**, not quietly rounded up:

- **Is the "institution object" more than a renamed list?** (C-006, formal half) — **answered,
  inside the model, and executed.** The quotient really is smaller than the pile and the response
  map factors through it exactly (the demo above). What is *not* settled is the **empirical** half:
  whether such task-relative institutions are *useful and stable* in real domains, or whether every
  useful thing can still be said just as well about the raw ingredients. If the latter, the object
  should be deleted — the theory gets better by getting smaller.
- **Does this out-predict the existing literatures?** (C-025) Network theory, distributed cognition,
  role theory, institutional economics, social ontology, distributed systems — no novelty is
  claimed over any of them until a primary-source comparison is actually done.

The canonical v0.2 manuscript, its claim ledger (with the v0.2 status block), the reconciliation
against `main`, and the falsification plan live in the
[research package](../research/distributed_institutional_realization_2026-09-15/README.md).

---

← Back to [the wiki home](README.md) · see also [Other Minds](other-minds.md), [Agency Architecture](app-agency-architecture.md), and the [glossary entry on "sheaf-like"](glossary.md).
