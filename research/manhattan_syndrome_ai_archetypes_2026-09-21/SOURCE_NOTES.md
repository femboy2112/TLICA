# Source Notes — Manhattan and Syndrome

**Research snapshot:** 2026-09-21  
**Purpose:** preserve provenance for the empirical claims; re-check all current product/policy sources before submission.

## S1 — X Help Center, "About Grok"

**Observed statements used:**

- Grok can decide whether to search public X posts and conduct real-time web search.
- X may share public X data and Grok interactions with xAI for training/fine-tuning.
- "Public X data" is described as including public posts, associated metadata such as engagement and reposts, public Spaces, and public profiles.
- X-derived personalization can include public profile, public posts, top posts, engagement, interests, and Grok interactions.

**Use in paper:** establishes real product/data coupling.  
**Does not establish:** that all such data is always used; that engagement metadata directly defines a reward; that Grok's social-affective meaning geometry has been deformed by X.

## S2 — xAI Developer Docs, "X Search"

**Observed statement used:** X Search enables keyword search, semantic search, user search, and thread fetch over X content.

**Use in paper:** establishes a direct retrieval instrument from the platform into Grok/xAI deployments.

## S3 — xAI, "Grok Bot now works with X" (2026-08-29)

**Observed statement used:** Grok Bot can connect to X, search posts, read timelines, check mentions, pull trends, and use an X plugin.

**Use in paper:** product-ecology evidence of increasing X coupling.

## S4 — xAI, Grok 4.20 System Card (2026-04-07)

**Observed statements used:** Grok 4.20 is trained via pretraining, targeted mid-training, and post-training using supervised fine-tuning and reinforcement learning on human and synthetic reward signals; deployments on x.com have platform-related tool access.

**Use in paper:** bounds claims about development channels and warns against pretending product behavior comes only from pretraining.

## S5 — X recommender-system documentation

Relevant current pages:

- *About our approach to recommendations*
- *Notifications Recommendations*
- *Search Recommendations*
- *Conversations Recommendations*
- *For You Home Timeline Recommendations*

**Observed statements used:** ranking/recommendation uses signals including likes, reposts, replies, watches, network popularity and predicted engagement, with negative-feedback/safety signals also present.

**Important qualification:** X does **not** document a single universal "maximize engagement" scalar for every surface. Do not flatten heterogeneous ranking systems into one objective.

## S6 — Brady et al. (2017), PNAS

"Emotion shapes the diffusion of moralized content in social networks."

**Use:** evidence that moral-emotional language is associated with differential diffusion in social networks.

**Boundary:** historical Twitter data; not a direct measurement of 2026 X; not a claim that all viral content is outrage.

## S7 — Brady et al. (2021), Science Advances

"How social learning amplifies moral outrage expression in online social networks."

**Use:** preregistered observational studies on Twitter plus behavioral experiments support the claim that positive social feedback can increase later outrage expression and that network norms shape expression.

**Boundary:** this is a statement about human users and social learning, not Grok.

## S8 — Huszár et al. (2022), PNAS

"Algorithmic amplification of politics on Twitter."

**Use:** large randomized Twitter experiment demonstrates that algorithmic personalized ranking can change exposure relative to a reverse-chronological control.

**Boundary:** historical Twitter; paper found specific partisan amplification patterns but did **not** support a simple "extremes always amplified" story. This source should be used to establish selection/amplification, not to smuggle in a current political-direction claim.

## Provenance rule

The paper must preserve three layers:

1. **Official current product facts** — X/xAI docs.
2. **General social-selection mechanisms** — peer-reviewed platform research.
3. **Grok-specific Syndrome interpretation** — our conjecture that source coupling can deform operative social-affective geometry even under correct explicit source attribution, pending direct probe.

Never cite layer 1 or 2 as though it directly proves layer 3.

## S9 — Academic literature (added v0.3.0)

The related-work / methods literature (performative prediction, sycophancy, RLHF representation effects, recommender feedback loops, implicit-bias-survives-explicit-correction, representation-geometry measurement) is triangulated in **LITERATURE.md** with per-reference status labels. Three load-bearing identifiers were re-verified by direct arXiv fetch on 2026-09-21 (Perdomo et al. 2020 arXiv:2002.06673; Sun et al. 2025 arXiv:2506.00253; Santurkar et al. 2023 arXiv:2303.17548); the rest carry the literature pass's own labels and a submission-day re-verification gate (LITERATURE.md §E). The environment's search index returned some future-dated/simulated arXiv IDs, which are quarantined in LITERATURE.md §D and must not be cited until confirmed. Provenance discipline: this academic literature establishes the *mechanism family*, never the Grok-specific layer-3 claim.
