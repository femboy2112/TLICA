# Being switching: an invariant → test → mutant map

**Order:** GOD ORDER #89 / T5, 2026-11-27. **Tier:** TLICA theoretical liaison. Docs only: no product code, no test written or
run.

**Scope:** the public, abstract half of a test map for switching between a base Being and the members of its sub-Being family.
It turns the invariants of [T3](being-state-invariants-20261126.md) (B1–B13) and [T4](being-colouring-composition-20261126.md)
(K1–K13, L1–L7) into rows that a host can check. The mapping onto a concrete host (type names, carriers, priorities) is
private and routed separately.

**Labels:** Demonstrated · Observed · Conjectured · UNVERIFIED. Every test and mutant here is a **proposal**.

---

## 1. How to read a row

- **Observable:** what the host test reads (a digest, a resolution result, the set of bodies in a frame, an availability value).
- **PASS:** the property test that must pass on the candidate. Inputs are random operation sequences, shrunk on failure.
- **Mutant:** a deliberately broken variant under which **the same test must FAIL**. A mutant that survives means the test
  does not discriminate, and the row stays open.

Operation alphabet: approval, colouring approval, member add / remove / activate, promotion, switch, recipe edit, outfit edit,
affect event, fiction-frame event, memory read / write / request, relay, restart. Only fixture-class members are needed.

## 2. Owner rulings this map covers

1. The base personality is immutable.
2. A sub-Being colours **expression** only.
3. A sub-Being may have its own avatar recipe. Without one, it resolves the base Being's current recipe **by reference, not
   by copy**.
4. Only the **active** Being's body is shown.
5. A member promoted to a standalone role does not colour the base Being **while it is the active one**.
6. Memory is partitioned (T4 §3a); refusals are typed; notes marked not-for-relay are read by the base Being and never relayed.

## 3. The map

### A. Base immutability

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| A1 | K1 | base digest | constant over sequences **including** approvals; base character revisions refused | colouring folded into the base; approved base revision accepted |
| A2 | K4 | lineage key; next live event after a colouring approval | key byte-identical; live event accepted | colouring approval bumps the lineage revision, so live state goes stale |
| A3 | K3 | origin of approvals | approvals from a member, the base Being or the model refused | gate checks payload, not origin |
| A4 | B4 (no aliasing of layers) | expression inputs | baseline, affect and colouring are three typed inputs | colouring summed into affect |

### B. Colouring is expression only

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| B1 | K6 | fixed dimensions; granted capabilities | fixed dims = base; capabilities ⊆ base; profiles setting a fixed dim rejected | an autonomy dimension marked colourable |
| B2 | K7 | floor dimensions | negative deltas clamp at base | clamp removed |
| B3 | K5, B4 | every history, state, recipe and approval digest | composing χ changes none of them | composition nudges affect or caches into the recipe |
| B4 | L1, L2 | χ digest | permutation-invariant; add-then-remove = identity | per-step clamp; remove leaves residue |
| B5 | K10 | activation vector | fiction / rehearsal / hypothetical frames leave it unchanged | activation by name mention |
| B6 | K11 | χ under two engines | equal | χ read from model output |
| B7 | moonshot off | resolved recipe | unchanged by any colouring set | colouring-driven accessories on by default |

### C. Recipe by reference

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| C1 | by reference | resolution result; member's recipe slot | reason "defaulted"; reference = base's current revision; slot empty; same object | clone on first resolve |
| C2 | tracks revisions | resolved revision after a base recipe revision | defaulted members follow; own-recipe members do not | copy at creation |
| C3 | no silent default | resolution of a failing own recipe | typed refusal surfaces | fallback to the base recipe |
| C4 | owner check | activation of a resolved recipe | checked against the resolved recipe's owner | check skipped for defaulted results |
| **C5** | **edit through a reference (new, Conjectured hazard)** | base recipe digest | editing while a *defaulted* member is selected is refused, or creates that member's own recipe as an explicit act; the base recipe never changes | the editor writes through the reference |

### D. Only the active Being is shown

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| D1 | one body | recipe references per presented frame | exactly 1 when visible, 0 when hidden, = the active Being's | each colouring member with a recipe drawn |
| D2 | atomic switch (B12) | frames around a switch | never both bodies; no catch-up replay | old body kept until its clip ends |
| D3 | quiescence, expiry | events consumed while hidden | none replayed on re-show | queued events replayed |
| D4 | backend agreement | active identity seen by each backend | identical | one backend caches the active identity |
| D5 | B13, K4 | lineage keys and partitions across A → B → A | unchanged; A's memories never surface in B | switch writes into the outgoing partition unfiltered |

### E. Promotion

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| E1 | no double count | composition set | family active set minus the active Being | suspension omitted |
| E2 | exact resumption (L2) | base χ before / after a round-trip through the promoted Being | byte-identical | residue after suspension |
| E3 | memory copied, original frozen | original partition | readable by the base Being, refuses writes; standalone writes never appear in it | move; alias |
| E4 | K4 | lineage keys | base key unchanged; promoted Being has its own | promoted Being reuses the base identity |
| E5 | K6 | capabilities while promoted Being is active | its own envelope only | base grants inherited on promotion |

### F. Memory, consent, non-relay

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| F1 | K13 | read results | base reads every member (attributed); siblings refused | partition check on writes only |
| F2 | K12 | member access to the base history | direct refused; granted request returns only its scope, relayed, warrant ≤ reported | full history returned |
| F3 | T2 I6 | availability on refusal | `withheld{consent}`, never absent; budget never reported as consent | empty on refusal; budget as consent |
| F4 | read ≠ merge | base history digest | unchanged by reads; conclusions are new writes, warrant ≤ inferred | read cached into base history |
| F5 | relay attribution | relayed sibling content | relayer = base, speaker = source member | relayer = source member |
| F6 | not-for-relay | relay result | `withheld{consent}` | flag checked on direct relay only |
| **F7** | **relay laundering (new, Conjectured hazard)** | taint on derived writes | a derived write inherits not-for-relay from any input carrying it | derived writes untainted |
| F8 | K8 | agent-face output | held at ≤ reported, two-place attribution, member partition only | output stored at its claimed warrant |
| F9 | K5 | histories after remove / retire | unchanged; retired partition frozen and readable; deletion is explicit | removal cascades to the partition |

### G. Restart claims

| # | Invariant | Observable | PASS | Mutant (must FAIL) |
|---|---|---|---|---|
| G1 | no fake continuity | state after a real restart | saved recipe, settings and active selection survive; anything session-only is reported as not surviving | "restored" shown from cleared memory |
| G2 | pending stays pending | act gate after migration and restart | re-confirmation-pending intentions never act until re-allowed | restart restores them as actionable |

## 4. The two new hazards

- **C5, edit through a reference.** Resolving by reference is the right storage rule, but it creates a write path: an editor
  that edits "the selected avatar" follows the reference and rewrites the base Being's body. The test pins the base recipe
  digest across edits made while a defaulted member is selected. TLICA's default policy: an explicit "give this Being its own
  body" act that creates the member's recipe; the base recipe never changes.
- **F7, relay laundering.** "Never relayed" closes the direct path. The base Being's own summaries and conclusions are a second
  path, because they are new writes derived from the protected note. The proposal is taint propagation: a derived write
  inherits not-for-relay from any input carrying it. A looser alternative is an explicit declassify act, never a silent one.

Both are owner decisions; neither is a ruling.

## 5. Boundaries

Docs only. No test written or run. No host code read into this document. The host mapping and priorities are private.
