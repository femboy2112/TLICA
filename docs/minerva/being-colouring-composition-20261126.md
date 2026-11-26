# Base ⊕ colouring: a frozen character coloured by a family of sub-Beings

**Order:** GOD ORDER #2 / T4, 2026-11-26. **Tier:** TLICA theoretical liaison (docs only).
**Scope:** the public, abstract half of T4. It gives a formal model of a synthetic character whose **base personality is
frozen** and whose expressed character is **coloured** by a family of approved, revisable sub-Beings. It also gives the
non-leak invariants, the composition laws, and how the model refines the strata of [T3](being-state-invariants-20261126.md).
The mapping onto named host types is routed privately.

**Owner decision this note builds on.** The base personality stays frozen. Growth and variety come from colouring by a
family of customised internal sub-Beings, which also act as sub-agents. Premade sub-Beings are test fixtures, not family.
This settles the open question in T3 §4. A second owner decision fixes memory (§3a): each sub-Being keeps its own
memories, the base being can read all of them, and a sub-Being reads the base being's history only by asking her.

**Ledger labels:** Demonstrated · Observed · Conjectured · Refuted · UNVERIFIED. The definitions, laws and counterexamples
below are Demonstrated by construction or by the small worked cases given. Nothing here describes any implemented system.

---

## 1. Objects

**Character space.** X = ∏_{d∈D} X_d, one factor per character dimension. The dimensions are typed, because each type
composes differently:

| Type | Values | Examples (generic) | Colourable? |
|---|---|---|---|
| **scalar** D_sc | a bounded interval | humour level, directness, metaphor density | yes, by displacement |
| **ordinal** D_ord | a finite chain | depth: brief < balanced < deep | yes, by step displacement |
| **nominal** D_nom | a finite set, unordered | register, role label | yes, by selection |
| **fixed** D_fix | anything | values, commitments, limits, consent, initiative and autonomy envelope, lineage name | **never** |

A **floor-protected** subset D_floor ⊆ D_sc ∪ D_ord holds the epistemic dimensions (uncertainty disclosure, willingness to
disagree, citation habit). Colouring may raise them and may never lower them below the base.

**Base.** b ∈ X, written once at creation and never again. It is part of the frozen stratum (§5).

**Sub-Being.** A sub-Being k has two faces:
- a **colouring face**: an approved, versioned profile p_k = (δ_k, v_k, rev_k, parent_k), where
  - δ_k gives a bounded displacement δ_{k,d} with |δ_{k,d}| ≤ ε_d on scalar and ordinal dimensions;
  - v_k gives a proposed value on nominal dimensions;
  - supp(p_k) ∩ D_fix = ∅;
- an **agent face**: it can be run as a sub-agent whose outputs return to the host (§3, K8).

A sub-Being has its **own key** κ_k. It is never the lineage key of the base being.

**Family.** F is itself an approved, versioned object:
- a membership set of sub-Being keys;
- a total **priority order** ≺ on members (for nominal conflicts);
- recognisability **windows** r_d per dimension;
- a provenance class per member: production or fixture. Only production members compose.

**Activation.** a(t) ∈ [0,1]^F is **living state** (T3 S4). It is set by journalled events, it decays, and it says how
strongly each sub-Being is foregrounded right now. A profile is revision-scale; an activation is seconds-to-hours.

## 2. Composition (the ⊕)

χ(t) = b ⊕_F a(t) is computed fresh from the current (b, F, {p_k}, a(t)). Nothing else enters, in particular no history of
earlier activations. Per dimension:

- **d ∈ D_fix:** χ_d = b_d.
- **d ∈ D_sc:** χ_d = P_d( b_d + Σ_k a_k δ_{k,d} ), where P_d projects onto the window
  W_d = [b_d − r_d, b_d + r_d] ∩ X_d. For d ∈ D_floor the window is [b_d, b_d + r_d].
- **d ∈ D_ord:** the same, with the sum taken over the chain's integer index, then **rounded once** and projected once.
- **d ∈ D_nom:** χ_d = v_{k*,d}, where k* is the ≺-greatest member with a_k ≥ θ and d ∈ supp(p_k). If no such member
  exists, χ_d = b_d.

The **record** keeps the raw contribution vector c_{k,d} = a_k δ_{k,d}, captured **before** projection, alongside χ.

Expression then takes three typed inputs, E(b, χ − b, affect). The base, the colouring deviation and the affect deviation
are never merged into one untyped "curiosity" (T3's aliasing risk, now three-way).

## 3. Non-leak invariants

| # | Invariant | Property-test shape |
|---|---|---|
| **K1** | **Base immutability.** The digest of b is constant under *every* operation, including approvals. This is stricter than T3 B7, which allowed approval. | random operation sequences, approval events included: base digest constant |
| **K2** | **Colouring approval gate.** A profile, or the family record, changes only in an event carrying an operator approval. Revisions are append-only with a parent hash; an approved revision is immutable. | sequences without approval: profile and family digests constant; one approval changes exactly one record |
| **K3** | **No self-approval.** No sub-Being, and no composed character, can approve its own profile, another member's, or the family record. | approval events with sub-Being or model origin are refused |
| **K4** | **Lineage non-leak.** Adding, removing, revising or activating a sub-Being never changes the base being's lineage key. A sub-Being key is never used as, or joined as, the lineage key. | lineage key byte-identical across all family operations; join on κ_k into lineage-keyed tables is rejected |
| **K5** | **Memory non-leak.** Memory is partitioned: the base being has a global history H_M, and each sub-Being k has its own partition H_k. Visibility follows §3a and nothing else. No memory, in any partition, feeds back into b, p_k or F. Removing k neither deletes nor rewrites H_k or H_M. | remove k: every history digest unchanged; replaying any history leaves every profile digest unchanged |
| **K6** | **Authority non-leak.** The composed character's decision authority is the base envelope's. Colouring cannot touch D_fix, so it cannot widen limits, grants, initiative or autonomy. A sub-Being's agent face runs with at most the **meet** of the base envelope and its own narrower envelope. | over all families: granted capability set ⊆ base set; agent-face grants ⊆ meet |
| **K7** | **Floor protection.** For d ∈ D_floor, χ_d ≥ b_d always. | adversarial profiles with negative δ on floor dimensions: χ_d = b_d |
| **K8** | **Agent-face outputs are observations.** What a sub-Being's agent face returns enters the host as an observation with **two-place attribution** (relayer = the sub-Being, attributed speaker = whoever's content it is). Its warrant is at most *reported*, and it reaches living state only through the reducer (T2 I1/I11; T3 B8). It never writes S1, S2 or the base being's history H_M directly; it writes only its own partition H_k. | sub-agent output claiming established warrant is held at reported; a direct write attempt is refused |
| **K9** | **Fixture isolation.** A fixture-class member never enters production composition. Copying a fixture's content makes a **new** profile with preset provenance and no approval. It must be approved fresh before it can join. | production χ is unchanged by any fixture set; a copied fixture is inert until approved |
| **K10** | **Frame non-crossing.** A sub-Being invoked inside quoted fiction, rehearsal or a hypothetical does not change a(t) (T2 I2; T3 B9). | fiction-frame events: activation vector unchanged |
| **K11** | **Engine independence.** χ is computed by the host from typed records, not by the inference engine (T3 B3). | same records under two engines: equal χ digest |
| **K12** | **Mediated upward read.** A sub-Being never reads H_M directly. It sends a read *request* to the base being, who grants, narrows or refuses it. What comes back is an observation relayed by the base being (two-place, warrant ≤ reported, scope as granted). | a direct-read mutant is refused; a granted request returns only the granted scope; a refused one returns availability = withheld{consent} |
| **K13** | **Downward visibility, sideways isolation.** The base being may read every H_k, and what she reads arrives attributed to k. Siblings j ≠ k never read each other's partitions. | read(base, H_k) succeeds with relayer k; read(j, H_k) is refused for all j ≠ k |

### 3a. Memory: an inheritance shape

The owner's framing is polymorphism. Each sub-Being *inherits from* the base being and *overrides* part of her expression.
The colouring model already is that shape: χ_k = b ⊕ p_k is "base plus overrides", and D_fix plays the role of members
that cannot be overridden (`final`). Memory follows this visibility relation:

| reader \ partition | H_M (base, global) | H_k (own) | H_j (sibling) |
|---|---|---|---|
| base being | yes | **yes, all k** | **yes, all j** |
| sub-Being k | **by request to the base being only** (K12) | yes | no (K13) |

Two cautions so the analogy is not implemented backwards:
- In ordinary class inheritance the *subclass* sees the parent's state and the parent does not see the subclass's. This
  relation runs the other way: the parent sees every child, and a child sees the parent only through a request. It is
  closer to a supervisor with visibility into its workers than to a subclass reading inherited fields. Building it with
  literal language-level inheritance would invert both arrows.
- "All their memories are accessible to her" is a **read** relation. It is not a merge. Reading H_k does not copy it into
  H_M; anything the base being concludes from it is her own new write, attributed as derived from k (warrant ⊑ inferred,
  T2 I13).

## 4. Composition laws

**L1 Commutation (Demonstrated).** χ depends only on the multiset {(a_k, p_k)} and the fixed order ≺. Summation is
commutative. The ≺-maximum does not depend on arrival order. So the order in which sub-Beings were activated is
irrelevant. **This requires projecting once, after aggregation.** Counterexample with per-step clamping: b = 0,
W = [−1, 1], δ₁ = +2, δ₂ = −1.
- Order (1, 2): clamp(0 + 2) = 1, then 1 − 1 = 0.
- Order (2, 1): −1, then clamp(−1 + 2) = 1.
- The two orders differ (0 ≠ 1). Aggregate-then-project gives clamp(+1) = 1 in both orders.

**L2 Removal reversibility (Demonstrated).** χ is a pure function of the current set, with no hysteresis. So
remove(k)∘add(k) returns exactly the previous χ. With per-step clamping it fails: add δ₁ = +2 to b = 0 gives 1; then
subtracting 2 gives −1 ≠ 0. **Corollary:** colouring must never be folded into b (that would be drift, a K1 violation),
because folded colouring cannot be removed.

**L3 Membership idempotence.** F is a set keyed by κ_k, so adding a member twice is a no-op. A duplicate under a new key is
a new member and needs its own approval (K2).

**L4 Conflict.** Dimension d is **in conflict** at t when two active members contribute with opposite signs, each
exceeding a threshold η (scalar or ordinal), or when two active members propose different nominal values. Conflict rules:
1. It is resolved by the declared rule of §2: sum for scalar and ordinal dimensions, ≺ for nominal ones. **Never by
   recency or activation order** (that would break L1).
2. It is **recorded**: the contribution vector shows both sides even when the sum cancels. Silent cancellation is the
   failure mode, because a blended middle may be what no member intended.
3. The family may declare d **exclusive**. Then a scalar conflict on d also resolves by ≺, and the losing contribution is
   recorded as suppressed.
4. Priorities belong to the **family** record, not to profiles. Two profiles cannot then both claim first place, and ties
   are unrepresentable.

**L5 Recognisability (Demonstrated).** |χ_d − b_d| ≤ r_d for every d and every family size. Without windows, n members each
contributing +ε move χ_d by nε. The frozen base would then become nominal just by the family growing. The base is frozen
*and* bounds expression; the second property is what makes the first matter.

**L6 Attribution is not separable after projection (Demonstrated).** With b = 0, W = [−1, 1] and δ₁ = δ₂ = +1:
χ({1, 2}) = χ({1}) = χ({2}) = 1 and χ(∅) = 0. Each member's marginal effect in the full family is 0, yet together they
move χ by 1. "Which sub-Being made her say that" is therefore answered from the pre-projection contribution vector, never
by differencing χ.

**L7 Activation is not colouring.** An activation event changes a(t) and nothing in S1c. A profile revision changes S1c
and nothing in a(t) except by the declared migration (§5). So "she is in a playful mood" (S4) and "her playful sub-Being
got revised" (S1c) are different events with different writers.

## 5. Fit with T3 (refinement of S1 and B7)

T3's stratum S1 (character, operator-approved revision) **splits in two**:

| Stratum | Content | Writer | Timescale |
|---|---|---|---|
| **S1b base** | b, the frozen character | creation only | never; the same immutability class as S0 |
| **S1c colouring** | the family record F and the member profiles p_k | an operator-approved revision | revision-scale |
| (S4 living state) | **+ the activation vector a(t)** | the reducer | seconds to hours; decays |

Consequences for T3's invariants:
- **B7** splits. **B7b:** the S1b digest never changes (= K1). **B7c:** the S1c digest changes only with an approval
  (= K2). Long-run affect may *propose* a colouring revision, never a base change.
- **B6** now applies to S1c. An approved colouring revision keeps S0, S1b, S3 and S4. If a revised profile changes
  support, the live a_k for that member is carried over or expired by a declared rule, never silently reset.
- **B4** extends: an affect event changes neither S1b nor S1c. Activation is S4, so B4 permits it.
- **B10** extends: colouring revisions and activations commute with outfit and engine changes on Π_{S0–S5}.
- **B13** gains a fourth identity word. A sub-Being key κ_k is not lineage (S0), not appearance (S5) and not the engine (E).
- **The T3 open question closes by design.** Keeping traits in the lineage immutability class is now *correct* for the base.
  It would only be a defect if colouring were also stored there. Colouring must live in a separate, revisable record that
  does not enter the lineage key (otherwise each approval would mint a new being or invalidate live state).
- T3's design note stands and sharpens: the base drift rate is now zero *unconditionally*, a product choice stricter than
  TLICA's model of people (`foundation/3` §8.10). Growth is relocated into an approved, removable layer, not denied.

## 6. Property-test shapes (generic)

Generate random bases, families (production and fixture members), profiles, activation sequences and approval events.

1. **Base constancy (K1):** the base digest is constant over every sequence, approvals included.
2. **Commutation (L1):** for random permutations of the same activation events, the χ digests are equal. A mutant that
   clamps per step must fail this test.
3. **Removal (L2):** add then remove a member, and χ is byte-identical to before. A mutant that folds colouring into b
   must fail this test.
4. **Recognisability (L5):** for families of size 1…n with adversarial same-sign profiles, |χ_d − b_d| ≤ r_d.
5. **Conflict record (L4):** opposite-sign members whose sum cancels produce χ_d = b_d *and* a record showing both
   contributions.
6. **Floor (K7):** negative profiles on floor dimensions leave χ_d = b_d.
7. **Non-leak (K4–K6):** across all family operations the lineage key, the history digest and the capability set are
   unchanged.
8. **Fixtures (K9):** production χ is invariant to adding or removing any fixture member. A copied fixture is inert until
   approved.
9. **Agent face (K8):** sub-agent outputs arrive two-place attributed with warrant ≤ reported. A direct-write mutant is
   refused.
10. **Frame (K10):** activation inside a fiction frame leaves a(t) unchanged.
11. **Memory visibility (K12, K13):** test the full reader × partition matrix of §3a. Direct upward and sideways reads are
    refused; downward reads carry the child's attribution; a base-being read of H_k leaves H_M unchanged until she writes.

## 7. Open design questions (for the owner)

These are values decisions, not formal ones. The defaults proposed are the conservative choice in each case.

- **Q1 Sub-Being memory. RESOLVED by the owner:** each sub-Being keeps its own partition, and the base being reads all
  of them (§3a, K5, K13).
- **Q2 Simultaneity.** May several sub-Beings be foregrounded at once (an activation vector), or one at a time (one-hot)?
  *Default:* a vector, with L4 handling conflicts. One-hot is the special case and needs no conflict rule beyond ≺.
- **Q3 What the agent face sees. RESOLVED by the owner:** only by request to the base being, who mediates (K12).
- **Q4 Retired members.** When a sub-Being is removed from the family, does its partition stay readable by the base being?
  *Default:* yes, frozen and read-only; deletion is a separate, explicit operator act.
- **Q5 Sibling exchange.** May a sub-Being learn what a sibling knows by asking the base being, who then relays it?
  *Default:* only if she chooses to relay it, and then it arrives attributed to her, as K12 already covers.

## 8. Boundaries

- This is a formal proposal. Its status words describe the definitions, not any running system.
- The worked counterexamples are hand-checked arithmetic. No code was run.
- The mapping onto named host types, and the gaps found there, are private and routed to their owners.
