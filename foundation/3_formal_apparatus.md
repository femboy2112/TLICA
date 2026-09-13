# The Two-Layer Identity-Correlation Architecture

## File 3: Formal Apparatus

---

**Status:** Foundation document set, v5.4.2 — Layer 3 (Formal Apparatus)
**Contents:** Section 5 (Shell Walkthrough), Section 6 (Asymptotic Field), Section 7 (Three Coordinates with Identity-Correlation Profile), Section 8 (Substrate, Focus, Dynamics with Imprinting Pathways)
**Depends on:** Files 1-2
**Required for:** Files 4-6

---

## 5. The Shell Walkthrough: From Cogito Outward

Before formalizing identity-correlation, this section walks through what it picks out, by developing the shell structure outward from the cogito. The shells are not primitives of the architecture; they are contour bands of identity-correlation that emerge as the I's lived network accumulates.

### 5.1 The cogito as the innermost position

At the cogito itself: $\hat\iota_m$. The I is itself. Identity-correlation with itself is maximal by anchoring convention: $\rho_m(\hat\iota_m) = 1$. Nothing else has $\rho = 1$.

### 5.2 The first shell: contents currently being experienced as me

Surrounding the cogito are contents whose integration into the lived-I network is densest. For a healthy adult, these typically include the current felt body, current intentions in active execution, the immediate sense of being the one to whom things are happening.

In the developmental case — the newborn — this shell is nearly empty. The cogito is in place, but the integration network is not yet built. The newborn is closer to the bare core I than any later stage.

### 5.3 The second shell: stable embodied integration

Further out: the body and its standing capacities. The body is initially primal not-I — it presents itself to the I as something to be encountered, not as part of the I. Through repeated contact and developmental imprinting, the body acquires high ρ.

This happens alongside verification-tool imprinting. The infant learning that her hand persists when out of view is simultaneously imprinting object persistence and integrating the hand into her lived-I network. Content imprinting and verification-tool imprinting often co-occur.

By adult maturity, the body has high ρ across multiple integration modes. But the body never becomes the core I; ρ for any body part is strictly less than 1.

### 5.4 The third shell: deep integrations

Memories, skills, deeply-held commitments, central relationships, identity-defining projects. These are typically *not* contents of current consciousness — high ρ, low or undefined φ in the moment.

### 5.5 The fourth shell: peripheral integrations

Casual relationships, occasional skills, interests that don't define the I. ρ is positive but moderate.

### 5.6 The fifth shell: contents in current awareness without integration

A book just opened, a stranger encountered, news just heard. These contents may have high κ and various φ, but ρ is low.

### 5.7 The outer limit: strict not-I

Contents whose ρ approaches zero. The world that doesn't touch the I, the people the I never meets, the abstract structures the I doesn't engage with.

### 5.8 What the shells tell us about identity-correlation

The shell structure makes plain what identity-correlation is tracking: not how *real* a content is, not how strongly it is *contacted*, but how *integrated* it is into the lived network rooted at the cogito. Identity-correlation is the structural property of being part of the I's lived network.

---

## 6. The Asymptotic Field

### 6.1 The asymptotic content domain

For modeling I $m$ at time $t \in T_m$, let $\mathsf{A}^m_t$ be the set of non-intrinsic items in $m$'s field at $t$. This includes both conscious and unconscious contents.

Every item in $\mathsf{A}^m_t$ is in Tier 3. None reaches intrinsic universality:

$$x \in \mathsf{A}^m_t \;\text{with verification pathway defined} \;\Rightarrow\; \phi_{m,t}(x) \leq 1 - \delta.$$

For items without an apparent verification pathway constructible from the I's toolset, φ is undefined; ρ and κ remain available.

Define the **phenomenally available subset** of the asymptotic content domain:

$$\mathsf{A}^{+,m}_t := \{x \in \mathsf{A}^m_t : A_{m,t}(x) = 1\}.$$

$\mathsf{A}^m_t$ is the total asymptotic domain visible from the outside perspective; $\mathsf{A}^{+,m}_t$ is the subset that is phenomenally available to the I from inside. Latent/retrievable and unconscious-operative contents lie in $\mathsf{A}^m_t \setminus \mathsf{A}^{+,m}_t$ — they affect the lived-I network, ρ, κ, action, and disposition without currently being undergone or noticed by the I.

*This is where the conscious/unconscious distinction lives in the formal apparatus.* Phenomenal availability and φ are distinct architectural features. φ measures the I's constructible access to a content's intrinsic source or verification pathway through its current toolset. Phenomenal availability measures whether the content is present-to-the-I — whether the I is undergoing, noticing, or occurrently experiencing the content at all. These two are independent: a content can be phenomenally available with any φ status, and a content can have constructible φ without currently being phenomenally available. Let $A_{m,t}(x) \in \{0, 1\}$ be the phenomenal-availability status predicate, with $A_{m,t}(x) = 1$ meaning content $x$ is phenomenally available to modeling I $m$ at time $t$. The architecture treats $A$ as a status predicate, not a fourth coordinate parallel to κ, φ, ρ; formal development of phenomenal availability beyond status-tracking belongs in application work (particularly the differentiated-affect paper).

The four-class taxonomy of contents in $\mathsf{A}^m_t$:

- *Conscious-clear*: phenomenally available with defined φ. Worked arithmetic facts, explicit reasoning, source-traceable memory currently in operation. The I undergoes the content and has constructible access to its source/verification pathway.
- *Conscious-fuzzy* (source-opaque): phenomenally available with low or undefined source-level φ. Panic, dread, subtle unease, unlocalized discomfort, somatic affect, trauma-cue activation, novel-but-not-yet-articulated content. The I undergoes the content without constructible access to what produces it. These contents are *fully conscious*, just source-opaque — not "almost unconscious" or "partially conscious."
- *Latent / retrievable*: not phenomenally available at the current moment, but φ-pathway constructible upon activation. Stored facts, remembered procedures, available concepts, dormant skills. These are not unconscious in the strong architectural sense; they are simply not currently noticed.
- *Unconscious-operative*: not phenomenally available *and* lacking a constructible source-pathway under the I's current toolset, yet still affecting κ, ρ, salience, action, disposition, or later profile-development. Implicit biases, osmotically-formed dispositions, repressed contents, substrate-level patterns operating below phenomenal availability.

The conscious/unconscious distinction is therefore not a property of contents themselves but of the joint configuration of phenomenal availability ($A$) and verification-pathway access (φ) for a given content under the I's current toolset. Contents can move between classes: insight may move unconscious-operative content to conscious-clear by constructing a verification pathway; repression or verification-tool loss can move conscious-clear content to unconscious-operative; activation can move latent content to conscious-clear; and source-articulation can move conscious-fuzzy content to conscious-clear. Source-opacity is an architectural feature of much affective, somatic, traumatic, novel, and osmotically-imprinted experience whose source-pathways have not yet been articulated.

### 6.2 Persistence across time

Form the time-stamped token domain:

$$\widetilde{\mathsf{H}}^m_t := \{(s, x) : s \leq_m t \text{ and } x \in \mathsf{A}^m_s\}.$$

Posit a persistence equivalence relation $\sim^m_H$. The historical content domain is the quotient:

$$\mathsf{H}^m_t := \widetilde{\mathsf{H}}^m_t / \sim^m_H.$$

The relation $\sim^m_H$ is an explicit posit.

### 6.3 Inside vs. outside perspective

The full **outside-perspective** model instance:

$$\mathcal{M}_m = \big(\mathsf{Int},\; \hat\iota_m,\; \mathsf{N}_m,\; T_m,\; \mathsf{B}_m,\; \mathsf{S}_m,\; \Gamma^M_m,\; M_m,\; \chi_m,\; (\mathsf{A}^m_t)_t,\; (A_{m,t})_t,\; \sim^m_H,\; (\sigma^m_t)_t,\; (G^{m,k}_t)_{t,k},\; (\mathsf{Foc}^m_t)_t,\; (\mu^m_t)_t,\; \mathsf{Tools}^m_t,\; \phi_m,\; \rho_m,\; \kappa_m \big).$$

$A_{m,t}$ is a phenomenal-availability status predicate, not a fourth coordinate parallel to κ, φ, and ρ. It is included in the model instance because $\mathsf{A}^{+,m}_t = \{x \in \mathsf{A}^m_t : A_{m,t}(x) = 1\}$ is defined from it (Section 6.1).

The **inside-perspective** data:

$$\mathsf{Inside}^m_t = (\mathsf{A}^{+,m}_t,\; \mathsf{Foc}^m_t,\; Q^m_t,\; \mathsf{Tools}^m_t,\; \text{applicable test-results},\; \text{detectable }\rho\text{-effects},\; \text{contact-effects on contents}).$$

The modeling I has direct phenomenal access only to $\mathsf{A}^{+,m}_t$. Unconscious-operative contents may be included in the outside-perspective asymptotic domain $\mathsf{A}^m_t$, but from inside they are available only through effects, symptoms, activations, or later articulation — never as directly inspected contents.

The **outside-only** components:

$$\mathsf{Outside}^m = (\mathsf{N}_m,\; \mathsf{B}_m,\; \mathsf{S}_m,\; \chi_m,\; \sigma^m_t,\; \tau^m_t,\; \mathsf{O}_m,\; \Gamma^M_m).$$

The modeling I has its contents, can apply verification tools, can hold contents in focus, and can detect effects of integration and contact. It does not directly inspect source-attribution, the full contact interface, the structure of primal not-I, the substrate-dependence function, or the criterion for which items in $\mathsf{N}_m$ are actual other I's.

---

## 7. The Three Coordinates

For modeling I $m$ and content $x \in \mathsf{A}^m_t$:

$$\kappa_{m,t}(x), \qquad \phi_{m,t}(x), \qquad \vec\rho^m_t(x).$$

ρ and κ apply uniformly across the asymptotic field. φ applies only to contents with a verification pathway constructible from the I's current toolset (Tier 3 with defined pathway).

### 7.1 Contact (κ)

For an item $n \in \mathsf{N}_m$:

$$\kappa_{m,t}(n) := \chi_m(t, n).$$

For a content $x \in \mathsf{A}^m_t$ with source map defined:

$$\kappa^{\mathrm{out}}_{m,t}(x) := \sup\{\kappa_{m,t}(n) : n \in \sigma^m_t(x)\}.$$

If $\sigma^m_t(x)$ is undefined or empty, $\kappa^{\mathrm{out}}_{m,t}(x) = 0$ unless an internal-contact convention is introduced. Because this definition uses $\sigma^m_t$, content-level contact is outside-perspective.

### 7.2 Identity-correlation (ρ)

Let $K$ be a finite or countable set of integration modes. For each $m, t, k$:

$$G^{m,k}_t = (V^m_t,\; E^{m,k}_t,\; w^{m,k}_t)$$

where $V^m_t = \{\hat\iota_m\} \cup \mathsf{H}^m_t$. An edge has weight $w^{m,k}_t(u, v) \in [0, 1]$. There is no primitive `IndexedTo` relation; identity-correlation is path-based and historically constructed.

Define integration capacity by max-flow:

$$C^{m,k}_t(x) := \operatorname{MaxFlow}_{G^{m,k}_t}(\hat\iota_m,\; x).$$

For $x \neq \hat\iota_m$:

$$\rho^{m,k}_t(x) := \frac{C^{m,k}_t(x)}{1 + C^{m,k}_t(x)}, \qquad \rho^{m,k}_t(\hat\iota_m) = 1.$$

This guarantees $0 \leq \rho^{m,k}_t(x) < 1$ for every non-core node.

The vector $\vec\rho^m_t(x) := (\rho^{m,k}_t(x))_{k \in K}$ is the primary object. A scalar projection:

$$\rho_{m,t}(x) := \sum_{k \in K} a_k\, \rho^{m,k}_t(x), \qquad a_k > 0,\; \sum_k a_k = 1.$$

Max-flow is one principled aggregation choice (it respects bottlenecks, which matches the phenomenology of fragility in self-integration). Other aggregations (total flow, shortest-path) are compatible with the architecture's foundations and represent different applied choices. The architecture commits to flow-like integration over a directed historical network rooted at the cogito; max-flow is the specific instantiation explored here.

ρ is well-defined for both conscious and unconscious contents.

### 7.3 Truth-indistinguishability (φ), three-tier

Tier 1 (intrinsic items): not in the φ-domain. Have ontological status as in re; not assigned φ values.

Tier 2 (the cogito): φ(Î_m) = 1 - δ structurally. Holds for any cogniting being; not I-relative; determined by the perspectival-step relationship between universal reflexivity and indexed self-identity.

Tier 3 (other asymptotic contents with constructible verification pathway): φ is I-relative. The general form:

$$\phi_{m,t}(x) = 1 - n_{m,t}(x)\,\delta - \epsilon_{m,t}(x).$$

Both $n_{m,t}(x)$ and $\epsilon_{m,t}(x)$ are toolset-dependent and decomposition-dependent. The conditional depth $n_{m,t}(x)$ counts steps along the verification pathway constructible from $\mathsf{Tools}^m_t$; different decompositions and different toolsets yield different counts. The empirical robustness component $\epsilon_{m,t}(x)$ is given by the probe-integral construction:

$$\epsilon_{m,t}(x) = \int_{Q^m_t} (1 - q(x))\, d\mu^m_t(q),$$

with $\epsilon_{m,t}(x) + n_{m,t}(x)\,\delta \leq 1$ ensuring $\phi_{m,t}(x) \in [0, 1 - n_{m,t}(x)\,\delta]$.

What is invariant across I's is the *form* of the φ-structure (any I has φ-values for contents with constructible pathways, with both n-like and ε-like components, layered around a structurally-positioned cogito). What is I-relative is the specific values and the specific decomposition.

For any content without a verification pathway constructible from $\mathsf{Tools}^m_t$, $n$ is undefined and φ does not apply. Such content may be conscious-fuzzy / source-opaque when $A_{m,t}(x) = 1$, or unconscious-operative when $A_{m,t}(x) = 0$. Undefined φ is therefore not sufficient for unconsciousness; the joint configuration of $A$ and φ determines the content's class (Section 6.1).

The probability weight $\mu^m_t$ is generated by current focus and contact:

$$\mu^m_t = \Lambda^\mu_m\big(\mathsf{Foc}^m_t,\; \kappa^{\mathrm{out}}_{m,t},\; Q^m_t\big).$$

### 7.4 Formal non-reducibility and dynamic entanglement

The three coordinates are *formally non-reducible* — none is derivable from the others by definition. They are *dynamically entangled* — they influence each other through contingent operating dynamics.

Formal non-reducibility:

- Vary $\chi_m$ while holding the truth-profiles and graphs fixed: $\kappa_m$ changes; $\phi_m$ and $\rho_m$ do not.
- Vary the truth-profiles while holding $\chi_m$ and graphs fixed: $\phi_m$ changes; $\kappa_m$ and $\rho_m$ do not.
- Vary the graphs while holding $\chi_m$ and truth-profiles fixed: $\rho_m$ changes; $\kappa_m$ and $\phi_m$ do not.

Dynamic entanglement: in operating lived consciousness, the coordinates influence each other through contingent (not definitional) mechanisms. Examples: high κ over time can increase ρ via repeated contact and integration; high ρ can bias κ via salience capture; high φ can reorganize ρ by making source/pathway distinctions available; low φ can protect high-ρ contents from correction; osmotic imprinting can alter κ and ρ without producing φ. These are dynamics, not definitions; they describe how the coordinates interact in operation, not how they reduce to one another.

The "three independent coordinates" framing therefore means *formally independent and dynamically entangled* — independent at the level of the architecture's definitions, entangled at the level of operating dynamics. Critiques that treat the independence claim as statistical or causal independence misread the architecture's commitment.

### 7.5 The unconscious-operative and conscious-fuzzy cases

For an unconscious-operative content ($A_{m,t}(x) = 0$, no constructible verification pathway):

- $\rho^{m,k}_t(x)$ well-defined.
- $\kappa^{\mathrm{out}}_{m,t}(x)$ well-defined.
- $\phi_{m,t}(x)$ undefined (no verification pathway constructible from $\mathsf{Tools}^m_t$).

Conscious-fuzzy / source-opaque contents differ only in phenomenal availability ($A_{m,t}(x) = 1$ while φ remains undefined or low). $\rho$ and $\kappa$ remain well-defined across both conscious-fuzzy and unconscious-operative cases; $A$ distinguishes whether the content is undergone by the I. A content can transition between these classes — repression moves conscious content to unconscious-operative; activation can bring unconscious-operative content into phenomenal availability as conscious-fuzzy; source-articulation can move conscious-fuzzy to conscious-clear.

### 7.6 The identity-correlation profile

The architecture's primary structural object for an I at a time is the **identity-correlation profile**:

$$P_{m,t} = \{(x, \rho_{m,t}(x)) : x \in \mathsf{A}^m_t\}.$$

Equivalently, $P_{m,t}$ may be written as a function $\rho_{m,t}: \mathsf{A}^m_t \to [0, 1]$ over the I's field, with the codomain bounded strictly below 1 for all non-core contents and reaching 1 only at $\hat\iota_m$.

The full vector profile, retaining mode-specific structure:

$$P^{\mathrm{vec}}_{m,t} = \{(x, \vec\rho^m_t(x)) : x \in \mathsf{A}^m_t\}, \qquad \vec\rho^m_t(x) = (\rho^{m,k}_t(x))_{k \in K}.$$

Profiles, not isolated values, are the unit of structural analysis. The architecture's predictions and explanatory claims operate on profile structures:

- Two I's with similar substrates and similar lived histories tend to have profiles with similar global structure (form-invariance conditional on existence; specific values vary).
- Mode disturbances (Section 10.5, File 4) produce characteristic profile-shape signatures rather than uniform ρ-shifts.
- Developmental progression (Section 4.6, File 2) corresponds to profile evolution: Phase 0 has a near-empty profile (everything either undifferentiated or ρ ≈ 0); Phase 3 has a richly populated profile with characteristic structure.
- Shells (Section 5) are coarse-grained projections of $P_{m,t}$ onto threshold bands $r_0 < r_1 < \ldots < r_n$. The lived-I network $\mathsf{L}^m_t$ is the support of $P_{m,t}$ where $\rho > 0$. Strict not-I content is where $\rho$ approaches 0.

The profile is therefore the load-bearing object for identity-correlation analysis. Single ρ values are projections of the profile onto specific contents; coarse statistics over the profile (mean ρ, support size, mode-specific densities) are summaries that lose information. Profile-to-profile comparison is what the architecture's predictions actually license.

*What the profile encodes and what it does not.* The profile $P_{m,t}$ encodes the structural integration of the I's field into the lived-I network. It is a structural-integration map, not a valuation map and not a preservation-priority ranking. The peak at $\hat\iota_m$ with $\rho = 1$ is the anchoring root of the directed graph from which max-flow is computed; it is mathematical normalization, not a claim that the cogito-I is what the I most values or would prioritize preserving over all else (see Section 2.9, File 1, for the parallel disclaimer at the foundational level). The valuation the I attaches to preserving each region of the profile under existential pressure is a separate matter, depending on dynamics (third-order pathway activation, future-state projection across the lived-I, substrate urgency) that the architecture does not currently formalize. Section 10.7, File 4, develops the architectural test case where this distinction matters most: self-sacrifice for a high-ρ non-core network member. The *evolution* of the profile over time — how the occupied baseline moves as the I reads a changing field — is formalized in Sections 8.9–8.11; the *valuation* dynamics just referenced (what the I would preserve under existential pressure) remains unformalized and is distinct from that state-evolution.

---

## 8. Substrate, Focus, and Dynamics

### 8.1 Substrate-bound focus capacity

For modeling I $m$, the substrate is

$$\mathsf{S}_m = (\mathsf{B}_m,\; \mathsf{E}_m,\; \chi_m), \qquad \mathsf{E}_m \subseteq \mathsf{N}_m.$$

The focus capacity $M_m : T_m \to \mathbb{N} \cup \{\infty\}$ is determined by substrate:

$$M_m(t) = \Gamma^M_m(\mathsf{S}_m,\; t).$$

The map $\Gamma^M_m$ is unspecified. The commitment is real dependence; the specific empirical mechanism is left open.

The modeling I cannot choose its own focus capacity:

$$\hat\iota_m \not\to M_m(t).$$

The I may allocate focus among available contents, but only within the inherited bound:

$$|\mathsf{Foc}^m_t| \leq M_m(t).$$

### 8.2 The two-phase shift in focus allocation

Focus allocation has two drivers that combine in a developmentally-shifting weighted manner:

$$\mathsf{Foc}^m_t = \mathsf{Foc}^m_t[\text{contact-driven}] \oplus \mathsf{Foc}^m_t[\text{self-directed}].$$

In the early phase, when lived-I structure is empty or near-empty, the second term is empty. Focus allocation is contact-driven; salient items in the world capture focus exogenously.

In the later phase, accumulated lived-I structure becomes available to direct focus from. Self-directed focus grows as the lived-I network grows. The transition is gradual and never complete.

### 8.3 Focus-driven probe weighting

The probability weight $\mu^m_t$ is constrained:

$$\mu^m_t = \Lambda^\mu_m\big(\mathsf{Foc}^m_t,\; \kappa^{\mathrm{out}}_{m,t},\; Q^m_t\big).$$

### 8.4 Focus-driven imprinting dynamics

An update event has form $e = (s, u, v, k, \alpha, \beta)$. The values $\alpha$ and $\beta$ are determined by focus and contact:

$$\alpha = \mathcal{A}^k_m\big(u, v,\; \mathsf{Foc}^m_s,\; \lambda^m_s(v)\big), \qquad \beta = \mathcal{B}^k_m\big(u, v,\; \mathsf{Foc}^m_s,\; \lambda^m_s(v)\big),$$

where $\lambda^m_s(v) = \sup\{\kappa_{m,s}(n) : n \in \sigma^m_s(v)\}$ when defined, 0 otherwise. The update rule:

$$w^{m,k}_{s^+}(u, v) = \Pi_{[0,1]}\Big( (1 - \beta)\, w^{m,k}_{s^-}(u, v) + \alpha\, (1 - w^{m,k}_{s^-}(u, v)) \Big).$$

### 8.5 Imprinting pathways: orders of mediation

Contents reach the modeling I through causal pathways that vary in length. The substrate $\mathsf{S}_m$ mediates between primal not-I and the I; different categories of content correspond to different mediation structures. This subsection identifies three characteristic pathway-orders and a general principle of lossy compression that operates across all pathways.

#### 8.5.1 Three orders of imprinting

Throughout this subsection, the orders categorize *contents* reaching the modeling I, not focus itself. Focus $\mathsf{Foc}^m_t$ is the I's allocation/selection structure across available contents — it is not itself a content but the function determining which contents are currently held in attention. The orders describe characteristic mediation pathways by which contents arrive at the I, and how those pathways interact with focus allocation.

Define the **mediation depth** of content $x$ at time $t$ for I $m$:

$$D_{m,t}(x) = \text{minimal dominant substrate-mediation depth by which } x \text{ reaches } \hat\iota_m.$$

$D_{m,t}(x)$ is a typological feature of contents within the architecture's existing apparatus, not a new coordinate. It describes which substrate components dominantly mediate a given content's arrival; it does not add a coordinate independent of κ, φ, ρ. Most actual contents involve multiple pathways simultaneously; $D_{m,t}(x)$ identifies the *dominant* one.

*First-order ($D = 1$): salience capture.*

$$\mathsf{N}_m \to \mathsf{S}_m^{\text{salience}} \to \mathsf{Foc}^m_t.$$

The world's impingement is minimally processed by substrate salience mechanisms and directly alters the I's focus allocation. The source map $\sigma^m_t(x)$ traces through minimal substrate-mediation — only the salience-gating components of the substrate intervene between $\mathsf{N}_m$ and the focus-shift.

This is *not* unmediated world-to-I contact. The architecture maintains throughout that the I never receives the world directly; all imprinting passes through substrate. First-order imprinting is the *minimally-mediated* case, not the unmediated one. Salience-gating substrate mechanisms (perceptual attention systems, startle response, novelty detection) are part of the substrate, and their operation is what makes first-order salience events characteristically sharp.

Examples of first-order salience events: a sudden loud sound captures attention; bright light shifts perceptual focus; a pain spike directs attention to the painful region; movement in peripheral vision draws the eye; someone's voice across a crowded room is recognized.

First-order salience events are characteristically *sharp* because mediation is minimal. The directional force of the world's impingement reaches focus allocation with limited intervening transformation.

*Second-order ($D = 2$): cognitive mediation.*

$$\mathsf{N}_m \to \mathsf{S}_m^{\text{cog}} \to \hat\iota_m.$$

The source map $\sigma^m_t(x)$ traces through cognitive components of $\mathsf{S}_m$ before reaching $\mathsf{N}_m$. Thoughts are the canonical case: the brain takes elements of not-I (perceptions, memories, situations, others' behaviors) and processes them into representational/cognitive form before they reach the I.

Examples: "That person insulted me." "I need to solve this problem." "This pattern looks familiar." "I should leave soon." "What did she mean by that?"

Second-order content is typically clear because it has propositional or quasi-propositional structure: content + relation + possible truth-test. The structured form makes thoughts well-suited for φ-placement in the I's verification system. Their characteristic shape is amenable to reason-tests.

Importantly, thoughts are *meta-cognitive* — the cognitive substrate produces commentary on its own internal processes and observations, factoring in current focus, prior content, learned categories, and so on. Thought-content is not the world but the cognitive substrate's representation of and operations upon the world.

*Third-order ($D = 3$): somatic-then-cognitive mediation.*

$$\mathsf{N}_m \to \mathsf{S}_m^{\text{som}} \to \mathsf{S}_m^{\text{cog}} \to \hat\iota_m.$$

The source map $\sigma^m_t(x)$ traces through somatic components of $\mathsf{S}_m$, then through cognitive components, before reaching $\mathsf{N}_m$. Emotions and physical sensations are the canonical cases: the world first alters bodily states, the body's altered state propagates to cognitive processing, and the resulting affective/sensory content reaches the I.

Examples: fear, anger, shame, grief, disgust, longing, dread, affection, anxiety; visceral sensations; hunger, fatigue, somatic discomfort; mood states mediated by hormonal or autonomic states.

Third-order content is characteristically *fuzzy* in the architecture's sense — see 8.5.4 below for the precise characterization.

#### 8.5.2 Orders as dominant pathways, not exclusive categories

The orders describe *dominant* mediation pathways, not mutually exclusive categories. Many actual contents involve all three pathway-types simultaneously, with one dominant and others contributing.

A felt sense of unease (third-order dominant) accompanied by an articulable thought about it (second-order contributing) directing focus toward something in the environment (first-order contributing) is a single complex content with a dominant pathway plus contributions from other orders. $D_{m,t}(x)$ identifies the dominant pathway; mixed-pathway dynamics are a real feature the architecture does not exclude.

#### 8.5.3 Lossy compression at each mediation stage

Each substrate-mediation layer transforms the signal, retaining some features and losing others. The signal is compressed.

Cognitive substrate processing takes nearly-infinitely detailed not-I and produces representational content that retains structural relationships (propositional, relational, comparative) while losing analog richness. This is significant compression: a perceptual scene with arbitrarily many discriminable details becomes a manageable cognitive representation.

Somatic substrate processing performs further compression. Somatic responses retain intensity, valence, action-tendency, and broad affective tone while losing much of the propositional structure. By the time third-order content reaches the I, two compression stages have operated: somatic compression of the original signal, and cognitive compression of the somatic state.

Higher-order imprinting therefore accumulates more compression. The I receives the compressed result, not the original signal.

#### 8.5.4 Fuzziness and the tendency relation

Fuzziness in the architecture's sense is *low explicit propositional information density* (or *low source-resolution*) from the I's inside perspective. This is not about absolute information content. Trained interoception, somatic awareness in skilled practitioners, expert affect-recognition, and contemplative practice can all extract substantial information from third-order content. The architecture's claim is about typical inside-perspective accessibility, not about absolute information bounds.

Define a phenomenological feature $\operatorname{Fz}_{m,t}(x)$ as the I's inside-perspective lack of explicit propositional structure or source-resolution for content $x$. Like $D$, this is a typological/descriptive feature within existing apparatus, not a new coordinate; it characterizes how undefined-or-low φ feels for high-κ contents when source-resolution is poor.

The architecture predicts a *tendency*, not a strict law:

$$D_{m,t}(x) \uparrow \;\leadsto\; \mathbb{E}[\operatorname{Fz}_{m,t}(x)] \uparrow.$$

The expectation-arrow rather than strict-arrow preserves exceptions:

- Trained somatic awareness (skilled musicians, athletes, meditators, therapists) can have third-order content with high source-resolution.
- Localized pain has third-order origins but often arrives with sharp source-localization.
- Named anger or grief in someone with extensive emotional vocabulary can have third-order content with substantial articulable structure.
- Vague thoughts (second-order content with low source-resolution) can be fuzzy despite second-order dominance.
- Intrusive but unstructured cognitions can be second-order content with low information density.

The orders predict tendencies of phenomenological signature, not strict constraints. Variation across I's and across contents within an I is a real feature of the architecture, not an exception to it.

#### 8.5.5 Information density vs intensity

Critically, fuzziness is about explicit propositional information density, not intensity. These are independent.

A panic attack has extreme intensity but low explicit propositional information density: "something is terribly wrong" without further structured detail about what, why, or how to respond. It is phenomenally available, high κ, source-opaque, undefined or low in source-level φ, and fuzzy. Its undefined φ does not make it unconscious; it means the I undergoes the content without constructible access to its intrinsic source or verification pathway. Panic attack is a paradigmatic conscious-fuzzy content (Section 6.1).

A subtle thought may have low intensity and high information density: "the proof depends on the assumption that f is continuous, which I should check." Moderate κ, well-defined φ, sharp.

A subtle emotional shift may have low intensity and low information density: a faint unease without clear object. Low κ, undefined φ, fuzzy.

This separates intensity from clarity:

- High intensity + high information density: clear and forceful (sharp pain in a known location for a person with body-awareness).
- High intensity + low information density: intense but fuzzy (panic, dread, severe but unlocalized discomfort).
- Low intensity + high information density: clear but mild (a subtle observation, a faint recognition).
- Low intensity + low information density: fuzzy and weak (background mood, vague disquiet).

The architecture predicts that body-mediated content tends toward the second and fourth signatures (variable intensity, low source-resolution); cognitive content tends toward the first and third (variable intensity, higher source-resolution). These are tendencies; exceptions exist.

#### 8.5.6 Thoughts triggering emotions

Meta-cognitive activity in the cognitive substrate (second-order content) can trigger somatic responses. The cognitive substrate's representation of a frightening situation activates body-systems that respond to the represented situation as if it were present; the somatic response then propagates back through cognitive integration to reach the I as affect. The pathway becomes:

cognitive content → somatic substrate activation → cognitive integration of somatic state → I (as affect)

Even though the originating cognitive content was second-order and clear, the resulting affective state arrives via third-order pathway with characteristic compression. This explains why thinking about a frightening possibility can produce affect without preserving the full structured content of the original thought — the thought triggers the body, the body's response gets compressed back to affect, and the affect reaches the I with reduced explicit propositional density relative to the original cognitive trigger.

This pathway accounts for:

- *Anticipatory anxiety*: thoughts about a future event activate body systems that respond as if the event were present; the resulting affect reaches the I as anxiety whose specific cognitive provenance is no longer directly accessible.
- *Anticipatory grief*: cognitive engagement with a future loss produces somatic responses that arrive as grief whose connection to the cognitive trigger has been compressed.
- *Emotionally-laden memory*: cognitive recall activates body systems that responded to the original event; the resulting affect colors the memory with intensity but typically without preserving the full original cognitive context.
- *Mood spillover*: extended cognitive engagement with a topic can produce sustained somatic states whose return to the I as mood persists after the cognitive content has shifted.

In each case, the second-order cognitive content triggers third-order pathway dynamics, with the resulting affect carrying the compression characteristics of third-order content even though the originating signal was cognitive.

The compressed thesis: emotions are typically third-order imprintings — not-I alters bodily state; bodily state alters cognitive substrate processing; the resulting affective content reaches the I. Because the signal has undergone somatic and cognitive compression, the I receives the affect as intensity, valence, action-tendency, and bodily tone more readily than as explicit causal provenance. This explains why emotions can be forceful without being clear.

#### 8.5.7 The general principle: substrate-mediation is lossy

The three orders are characteristic patterns of substrate-mediation, but the more fundamental observation is that *all imprinting from not-I to I involves substrate-mediation, and all substrate-mediation involves compression*.

The I never receives the world directly. The I receives compressed-and-transformed signals derived from the world by substrate processes the I does not directly inspect. First-order content is less compressed than second-order; second-order is less compressed than third-order; but no order delivers the signal in fully original form.

This is consistent with the architecture's existing commitment that source-attribution is outside-perspective: the I cannot fully see $\sigma^m_t$ from inside, because $\sigma^m_t$ describes substrate-mediation that occurs below the level of the I's introspective access. The orders specify *how much* of the original signal has been transformed by the time the content reaches the I.

#### 8.5.8 Connection to the three coordinates

The three pathway-orders interact with κ, φ, ρ in characteristic ways:

| Order | κ tendency | φ tendency | ρ tendency |
|---|---|---|---|
| First (D = 1) | High when active | Often well-defined for first-order salience events; structured for verification | Depends on integration history; new salience often low ρ |
| Second (D = 2) | Variable | Typically well-defined; cognitive structure supports verification | Depends on integration history; deeply held thoughts can be high ρ |
| Third (D = 3) | Often high when active | Often undefined or low; less explicit propositional structure for verification to grip | Variable; emotional patterns can be deeply integrated despite low φ |

These are tendencies, not necessities. Some first-order salience events are fuzzy (peripheral salience that captures attention without resolved content). Some third-order content is sharp (interoceptive awareness in skilled practitioners can be quite precise). The orders predict tendencies of coordinate signature, not strict constraints.

#### 8.5.9 Status of D and Fz

$D_{m,t}(x)$ and $\operatorname{Fz}_{m,t}(x)$ are typological/descriptive features within the architecture's existing apparatus. They are not new architectural coordinates. The architecture's coordinates remain κ, φ, ρ. $D$ characterizes pathway dominance for source-attribution; $\operatorname{Fz}$ describes the phenomenological signature of low source-resolution combined with low or undefined φ. Both are useful shorthand for patterns the architecture's existing apparatus can express, not additions to the apparatus.

#### 8.5.10 Profile-shape consequences

Returning to the profile $P_{m,t}$ from Section 7.6: an I's profile contains contents from all three orders, with each order contributing characteristic regions to the profile. Healthy adult profiles typically have:

- A first-order region with rapidly-varying κ (focus shifting), variable φ, and varying ρ (mostly low for new salience, moderate for habitual attentions).
- A second-order region with sustained ρ for deeply-held thoughts, projects, and beliefs; with φ structure that supports the I's reasoning capacity; and with κ that varies based on what is currently in mind.
- A third-order region with persistent ρ for integrated emotional patterns and bodily relations; often undefined or low φ across this region; κ varying with current bodily and affective state.

Profile-shape disturbances often have characteristic order-specific signatures:

- Depression's collapsed support typically affects the third-order region first and most severely (anhedonia, somatic flattening), with second-order region affected as cognitive ruminations narrow.
- Anxiety's reshaping operates strongly in third-order region (somatic activation) with second-order region pulled into threat-relevant focus.
- Dissociative phenomena often partition across orders: third-order content may be severed from second-order processing (alexithymia: feelings present without cognitive access); second-order content may be severed from first-order salience (intellectualization: thoughts present without engagement).

The order-typology gives the architecture finer-grained diagnostic vocabulary while remaining within the existing apparatus.

### 8.6 Verification-tool imprinting dynamics

Verification-tool imprinting follows the same dynamics. An encounter event for tool $T$ has form $e^T = (s, T, \alpha^T, \beta^T)$, with:

$$\alpha^T = \mathcal{A}^T_m\big(T,\; \mathsf{Foc}^m_s,\; \xi^m_s(T)\big),$$

where $\xi^m_s(T)$ measures encounter intensity for tool $T$ at time $s$.

### 8.7 Osmotic imprinting

The dynamics described in Sections 8.1–8.6 cover focus-driven and contact-driven substrate effects — content that the I attends to, things the I is in contact with, contents that reach the I through pathway-mediated delivery. The substrate has another mode of operation that runs in parallel and continuously: *osmotic imprinting*.

**The mechanism.** Osmotic imprinting is substrate-level pattern formation through repeated co-occurrence in ambient experience, operating without requiring focus on the association itself, without verification-pathway construction, and without mode operation. The substrate's response patterns get recalibrated by what it has been ambient-exposed to, regardless of whether the I attended to or articulated the pattern. Pavlov's dog is the pure substrate case: a cogniting being with limited Mode B undergoes substrate-level association formation through bell-food co-occurrence; bell alone later activates the substrate's food-response. No verification needed, no Mode operation needed. In human cogniting beings, osmotic imprinting operates alongside focus-driven mechanisms but retains its substrate-level character.

**Always operating.** The substrate is continuously patterned by ambient exposure. The architecture's commitment is that osmotic imprinting operates throughout the I's existence — not sometimes, not under specific conditions, but always. *Always operating* means that the osmotic mechanism remains online; it does not mean that every interval produces a measurable durable update. Mechanism-online status, effective bandwidth, durable imprinting, and later activation are architecturally distinct: the mechanism can be online while effective osmotic update is arbitrarily small (when ambient signal, repetition, substrate plasticity, or available bandwidth approach zero). There is a continuous tug of war between focus (the substrate's directed-attention dynamics shaped by the I's active engagement) and ambient exposure (the substrate's patterning by what surrounds the I regardless of attention). Both are always running; the balance varies with substrate state, environmental conditions, and the I's focus capacity. High-focus moments admit ambient patterning at reduced bandwidth — focus narrows but does not seal substrate channels not currently engaged. Low-focus moments (rest, mind-wandering, sleep, meditation) increase relative ambient intake. Total sensory deprivation does not stop osmotic imprinting; the substrate continues to be patterned by internal contents (proprioception, interoception, cognitive activity) ambient to the I's current configuration.

**Imprinting and activation are architecturally distinct.** Osmotic *imprinting* is formation: the substrate acquires association patterns through co-occurrence. Osmotic *activation* is operation: imprinted patterns produce later substrate responses (the bell triggers salivation; the smell triggers anxiety; the accent triggers protective response). The two are distinct mechanisms operating on the same substrate-level patterns. Imprinting requires repeated co-occurrence, sufficient ambient signal, and substrate plasticity. Activation requires substrate exposure to a triggering pattern (often a sub-component of the original co-occurrence). The I may experience activation consciously (a felt sense, an emotion, a salience capture) or pre-consciously (pre-attentive bias, autonomic adjustment); activation does not require the I to recognize what is being activated.

**Pathway-order operation.** Osmotic imprinting operates primarily through first-order and third-order pathway substrates:

- *First-order pathway substrate* ($\mathsf{S}_m^{\text{salience}}$): repeated co-occurrence recalibrates salience-gating thresholds so that patterns associated with high-salience contents acquire elevated salience-capture probability. This is the structural form of Pavlovian conditioning.
- *Third-order pathway substrate* ($\mathsf{S}_m^{\text{som}} \to \mathsf{S}_m^{\text{cog}}$): repeated co-occurrence between somatic-affective states and external contexts produces association patterns that later activate as somatic responses to those contexts. This is the structural form of trauma-cue dynamics, attachment-pattern formation, and many implicit-affect phenomena.
- *Second-order pathway substrate* ($\mathsf{S}_m^{\text{cog}}$): less directly involved in initial osmotic imprinting, but osmotically-imprinted patterns can later become explicit cognitive content through Mode B operation, external prompting, or shadow encounter.

**Transverse to the four kinds of imprinting.** Osmotic imprinting is not a fifth kind alongside content, contact, verification-tool, and mode-development imprinting (Section 10.4, File 4). It is a substrate-level mechanism that runs *underneath* and *alongside* those kinds. Each can have osmotic and non-osmotic variants: content can integrate into the lived-I network osmotically (through repeated exposure) or non-osmotically (through deliberate Mode C identification); contact relationships can develop osmotically before explicit recognition; verification tools can ground osmotically in substrate proto-patterns before explicit articulation; even mode-development can be partly osmotically shaped through the substrate-level "sufficiently distanced" thresholds osmotic imprinting establishes.

**Connection to source-opaque contents, unconscious-operative contents, and dispositions.** Osmotic imprinting is a primary mechanism by which source-opaque contents and dispositions form. Some osmotically formed patterns are unconscious-operative ($A = 0$, undefined φ): not phenomenally available, lacking a constructible source-pathway, yet affecting κ, ρ, salience, action, or disposition. Others become conscious-fuzzy ($A = 1$, undefined or low φ) when activated: the I undergoes the affect, salience-shift, bodily response, or felt sense without constructible access to the source-pathway that produced it. The phenomenological signature "I don't know why I feel this way about X" — strong response without articulable reason — is the canonical conscious-fuzzy signal of osmotic activation: the activation is phenomenally available, but its source-pathway remains opaque. Implicit attitudes, attachment patterns, trauma-cue responses, aesthetic dispositions, cultural absorptions, linguistic patterns — these are largely osmotically imprinted and operate at substrate level whether or not they become accessible to the I's explicit reasoning, and may surface as either unconscious-operative effects or conscious-fuzzy activations depending on phenomenal availability at the moment.

**Connection to verification tool development.** Osmotic imprinting also contributes to the development of verification capacity itself. The substrate can be osmotically patterned by repeated exposure to intrinsic structure as instantiated in the I's environment — counting that happens around the I before the I can count, grammatical patterns the I hears before the I can articulate grammar, reasoning patterns modeled by surrounding cogniting beings, aesthetic and modal patterns repeatedly displayed. These osmotic patterns populate the substrate with *proto-tools* — substrate-level patterns that are not yet explicit verification tools but that ground later development of explicit tools. The developmental arc:

1. Osmotic imprinting populates substrate with patterns through ambient exposure.
2. Some of these substrate patterns later become accessible to the I — through Mode B operation, through external prompting, through shadow encounter (Section 3.3, File 2), through deliberate attention.
3. When accessible, they can be refined into explicit verification tools that the I can deploy in φ-pathway construction.
4. The osmotic substrate patterns continue to operate even when not explicitly accessible; explicit tools and substrate patterns coexist throughout the I's existence.

This sharpens the architecture's account of the developmental escalator (Section 3.4, File 2): the order in which verification tools become *explicit* is shaped by temporal-scale-of-instantiation, but the substrate has often been osmotically prepared for those tools long before the explicit articulation occurs. The "I had a sense of X before I could put it into words" experience is the architectural signature — the substrate held the pattern osmotically; explicit access came later.

**The architecture does not specify rates.** Osmotic imprinting has parameters (ambient signal strength, repetition frequency, substrate plasticity, focus-bandwidth available for non-focused channels) that interact in ways the architecture does not formalize. How fast a given association forms, how persistent it is, what conditions support deactivation or revision — these are application-level questions that empirical work in classical conditioning, implicit cognition, attachment theory, and trauma research can address.

### 8.8 Why this is not free parameterization

The architecture has open functions ($\Gamma^M_m$, $\Lambda^\mu_m$, $\mathcal{A}^k_m$, $\mathcal{B}^k_m$, $\mathcal{A}^T_m$) but the dependencies are fixed. Substrate determines capacity; focus shapes probes and updates; contact shapes weighting and imprinting. The specific empirical content is application-level work. The dynamical additions of Sections 8.9–8.11 extend this open-function list — a relaxation rate $\gamma$, a mismatch potential $\Phi$, and a pressure map — under the same discipline: their forms are posited or open, but their dependencies are fixed (the baseline relaxes toward the field-reading; pressure rises with felt salience and with the determinacy of the demanded response; slack is capacity minus pressure). Where those sections commit to a specific functional form beyond what the foundation forces — the $\rho$-weighted-norm and temperature form of felt salience (Section 8.9) — the form is a *named posit*, not a fitted parameter, and is flagged as such.

### 8.9 The reflexive-differential reading

Sections 5–8.8 describe the profile $P_{m,t}$ and its imprinting at a time. The I, however, does not read its field in absolute terms. From the inside, only a *differential* against the currently-occupied baseline is registered.

Write $E_t$ for the ambient real vector space of signed functions $\mathsf{A}^m_t \to \mathbb{R}$ under pointwise operations, and $\mathcal{P}_t \subset E_t$ for **profile-space**: the admissible profiles over the I's field — the functions valued in $[0,1]$, reaching $1$ only at the cogito-anchor $\hat\iota_m$ and valued in $[0,1)$ off it (Section 7.6). $\mathcal{P}_t$ is a convex *subset* of $E_t$, not a subspace: it is not closed under sums or sign-flips (two admissible profiles need not add to an admissible one, and $-b$ is not a profile), so profiles are admissible *states* while their differences are vectors in the ambient $E_t$ — the two are not the same type of object. Let $b_{m,t} \in \mathcal{P}_t$ be the **occupied baseline**: the I's present position in $\mathcal{P}_t$, well-defined whenever the profile is, and independent of the reflexive operator of Section 8.11 (the baseline is *where the I sits*, not an exercise of Mode B, and so carries none of Mode B's developmental onset). Let $f_{m,t} \in \mathcal{P}_t$ be the **field-reading**: the substrate-mediated profile-image of the asymptotic field $\mathsf{A}^m_t$ — what the world, read against the I as it now sits, presses the profile toward — taken co-indexed with $b_{m,t}$ over the same field $\mathsf{A}^m_t$ at time $t$. The I never reads the field raw; the reading is substrate-mediated in the sense of Section 8.5. Their difference is the **differential**

$$\Delta_{m,t} = f_{m,t} - b_{m,t}, \qquad \Delta_{m,t}(x) \in (-1,1)\ \text{for each } x \in \mathsf{A}^m_t,$$

a displacement (vector) in the ambient space $E_t$, not a scalar and not itself an admissible profile. **Felt salience** $V_{m,t}$ is the magnitude of this differential: a pre-judgment feeling — not an actualized affect (that is a downstream pathway product, Section 8.5) and not a utility or decision-worth.

*What is derived.* That the inside reading is *differential* — against a baseline, never absolute — is not a new posit; it follows from the architecture's **perspectival anchoring**. Identity-correlation is already committed to be read *from the I's own frame, not absolute* (Section 2.9, File 1), and the cogito is the I's sole self-evident constant (Section 2.4, File 1) — the one fixed point it has. (This extends the *inter-observer* perspectivalism of Section 2.9 — different I's read the same content differently — to the *intra-subjective* case: a single I across time likewise has no absolute anchor beyond its own moving position; the step is licensed by the same perspectival-anchoring stance.) The I has no frame external to itself against which to read an *absolute* level of any content: any such frame would itself be not-I, hence itself perspectival, so no absolute reading is available even in principle. (Compare a system with no frame outside itself — the universe asked to measure its own velocity: with no external anchor there is no absolute reading to give, and meaning is recovered only in the relation across local frames.) What the I can read is therefore necessarily a displacement from where it now sits — a differential against its own occupied baseline. This is stronger than, and does not depend on, the source-attribution limit of Section 8.5 (that the I cannot fully see *where* a content came from): even a content whose level were somehow fully given would carry no absolute level for the I to read, because "absolute" presupposes an external anchor the I structurally cannot have.

*What is posited (named).* The specific functional form of $V$ is a posit beyond what the foundation forces, declared here:

$$\boxed{\,V_{m,t} = \tau_{m,t}\,\lVert \Delta_{m,t} \rVert_\rho\,}$$

where $\lVert\cdot\rVert_\rho$ is a $\rho$-weighted seminorm on the ambient space $E_t$ (a genuine norm only where every $\rho > 0$; see Section 8.10) weighting each axis by its identity-load $\rho$ — a unit mismatch on a high-$\rho$ axis (a content the I deeply *is*) yields more felt salience than the same mismatch on a low-$\rho$ axis, which is why loss of a high-$\rho$ content is felt as loss-of-self while a low-$\rho$ mismatch barely registers — and $\tau_{m,t} \geq 0$ is the **temperature** (reactivity, felt-salience-per-unit-differential) control parameter, written $\tau$ to keep it distinct from the time domain $T_m$ and the truth channel. The $\rho$-weighted-norm form (**Posit P1**) and the temperature parameter (**Posit P2**) are consistent with, not forced by, the rest of the architecture. The *magnitude* of $\Delta$ is $V$; its *direction* is retained and is what a mode-selection rule would read, but the architecture does not here commit to such a rule — it preserves the Mode A / Mode C biconditional of Section 4.8 (File 2) and does not turn it into a per-encounter selection predicate. A candidate sign-rule (Mode C when the differential extends the frame's consistency, Mode A when it damages it) is developed only at research tier.

### 8.10 State-evolution: the driven allostatic orbit

The occupied baseline is not static; it moves, and this section gives the equation of that motion. Sections 8.1–8.7 give the substrate's *formation*-side dynamics — how weights and associations are imprinted, slowly and continuously; this section gives the *operation*-side dynamics of the occupied baseline as it tracks the field. The two are distinct mechanisms on distinct footings, in the same spirit as (though not identical to) the imprinting-versus-activation distinction of Section 8.7.

*What is derived.* Because the differential (Section 8.9) is what the I reads, and because the field moves independently of the I — the substrate is itself moving reality: even under total sensory deprivation it "continues to be patterned by internal contents (proprioception, interoception, cognitive activity)" (Section 8.7) — the baseline dynamics is **non-autonomous**: the target it tracks is itself in motion. The differential then evolves as $\dot\Delta = \dot f - \dot b$, which under the tracking law below is $\dot\Delta = \dot f - \gamma\Delta$: the mismatch is *driven* by the field's own motion $\dot f$ and relaxed at rate $\gamma$. Two consequences follow: (i) the baseline continuously tracks a moving field-reading; (ii) *so long as the drive persists* — the field never asymptotically coming to rest, which for a living substrate is the standing condition (Section 8.7: internal contents keep patterning it) — the differential cannot **sustain** zero. Exact zero over any interval would force $\dot b = 0$ there, hence $f = b$ constant on it, contradicting a persistently moving field; instantaneous zero-crossings are *not* excluded, only sustained zero. Perpetual disequilibrium is therefore the normal condition of a living I, not a perturbation of rest — conditional precisely on the persistence of the drive, not on the bare fact that the field once moved (a field that asymptotically settled would let the baseline catch it). This is **allostasis** — stability through continuous change — not fixed-point homeostasis, and it needs no internal oscillator: the motion is driven. (The relation of the zero-differential state to the inert/death limit is treated in the posited block below.)

*What is posited (form).* Throughout this block $\rho$ denotes the **slow standing identity-load landscape** — the formation-side profile of Sections 8.1–8.7, and the metric weight in $V$ (Section 8.9) — held *fixed* on the fast operation timescale over which the baseline $b$ tracks the field-reading $f$. It is the metric *weight*, not the fast coordinate $b$: the slow $\rho$-landscape is what imprinting writes, $b$ the fast position moving over it — the formation-versus-operation split this section opened with. (Reading $\rho$ as the fast coordinate itself would add a spurious $\tfrac12(f-b)^2$ term to the gradient below; the identities hold with $\rho$ the fixed metric.) The baseline relaxes toward the field-reading by the primitive linear law

$$\frac{db_{m,t}}{dt} = \gamma\,(f_{m,t} - b_{m,t}) = \gamma\,\Delta_{m,t}, \qquad \gamma > 0.$$

On the nondegenerate support $\{\rho > 0\}$ this is exactly relaxational descent of the mismatch potential $\Phi(b, f_t) = \tfrac{1}{2}\lVert f_t - b\rVert_\rho^2$ (with $\lVert v\rVert_\rho^2 = \sum_x \rho(x)\,v(x)^2$, and $\rho$ held fixed) taken **in the $\rho$-metric**: the *natural* (metric) gradient is $\operatorname{grad}_\rho \Phi = W_\rho^{-1}\nabla_b\Phi = -(f_t - b)$ (with $W_\rho = \operatorname{diag}\rho$), so $db/dt = -\gamma\,\operatorname{grad}_\rho\Phi = \gamma\Delta$ — the metric strips the weight factor the Euclidean gradient $\nabla_b\Phi = -W_\rho(f_t - b)$ would otherwise carry. Along the flow the mismatch changes as

$$\frac{d\Phi}{dt} = \frac{\partial \Phi}{\partial t} - \gamma\,\lVert \operatorname{grad}_\rho \Phi \rVert_\rho^2$$

— drive (the field moves, raising $\Phi$) minus dissipation (the baseline descends at rate $\gamma$, the dissipation measured in the same $\rho$-metric). On a $\rho(x) = 0$ axis the primitive law still tracks ($db(x)/dt = \gamma\Delta(x)$), but $\Phi$ is flat there and the natural-gradient reading is undefined (the metric is singular): $\lVert\cdot\rVert_\rho$ is a **seminorm** on those axes, so a mismatch on a content the I is *not* identity-correlated with carries no felt magnitude and drives no descent *of $\Phi$* — a feature (loss of what one is not registers as nothing) — and $\lVert\cdot\rVert_\rho$ is a genuine norm, the descent picture exact, only on the quotient by the $\rho = 0$ axes. When the drive matches or exceeds the dissipation, $\Phi$ — hence the felt salience $V = \tau\sqrt{2\Phi}$ — does not settle: the baseline chases a moving minimum and orbits.

*The living I as a driven non-equilibrium steady state, and what death is.* This orbit is a **non-equilibrium steady state (NESS)**: held away from the $b = f$ rest-point by continuous drive balanced against dissipation, in the sense of Schrödinger's and Prigogine's dissipative structures. Two clarifications the formalism forces, against a tempting misreading. First, $V = 0$ is a *value the living orbit can cross*, not a death-state: it is reached whenever $\Phi = 0$ (the baseline instantaneously matching the field) or whenever $\tau = 0$, and a momentary $\Phi = 0$ crossing on a driven orbit is fully alive. Second, **death is not a value of $V$ at all; it is the cessation of the NESS** — the substrate ceasing to sustain the orbit: no longer forming the field-reading, or $\gamma \to 0$ (the baseline can no longer track), or $\tau \to 0$ (the differential is no longer felt). The $\tau \to 0$ limit is the *dying* direction — felt reactivity fading while mismatch may physically remain ($V \to 0$ with $\Phi > 0$) — and is offered as a **posited** model of substrate death, not derived from the equations; the architecture continues to *presuppose* consciousness (Section 2.9, File 1) rather than deriving its presence or absence from an identity-coordinate magnitude. What is *derived* is only the separation: a living I is a driven NESS, so its felt salience does not settle and its zero-crossings are not its death. The never-settling orbit is derived (consequences i–ii above); the linear-relaxation form and the rate $\gamma$ are the posited formalization, $\gamma$ being an open function whose *dependence* on substrate — not its value — is fixed, in the sense of Section 8.8.

### 8.11 Slack and the reflexive-operator gate

The dynamics of Section 8.10 is passive: pure descent along the local gradient. The reflexive operator (Mode B) can move the baseline *against* that gradient — but it is not a new mechanism. **Mode B is imprinting sourced from the I rather than from the not-I.** Osmotic imprinting (Section 8.7) is the substrate continuously writing the profile — altering $\rho$ without producing $\varphi$ (Section 7.4) — from the *contact-driven* side; Mode B is the *same* profile-writing operation from the *self-directed* side, the two poles of the focus split $\mathsf{Foc}^m_t = \mathsf{Foc}^m_t[\text{contact-driven}] \oplus \mathsf{Foc}^m_t[\text{self-directed}]$ of Section 8.2. (File 2, Section 4.4 already identifies externally-triggered Mode B with the imprinting operation viewed from the I-development side; this is that identity read at the level of the dynamics.) As a continuously-running mechanism Mode B is in this sense *always operating*, which does not conflict with its frozen developmental onset (Section 4.4, File 2): at the cogito-anchor $t = 0_{T_m}$ *exactly* its ability is zero — nothing has yet accumulated to attend to — but because osmotic imprinting is *also* always on (Section 8.7), structure accrues from the first instant, so the ability is nonzero for any $t > 0$. It is not switched off in early development, only **signal-to-noise-limited**: sparse accumulated structure and a small substrate context-window and time-constant leave the self-reading noise-dominated and not yet distinguishable from Mode A and Mode C. The onset distribution of Section 4.4 therefore marks when Mode B becomes *distinguishable and stable*, not when the mechanism begins — the mechanism is continuous; its signal-to-noise is what develops. So the reflexive reweighting *is* the I imprinting a change in its own $\rho$ — deliberately doing to itself what chronic contact does osmotically from outside — and that is what lets the baseline depart from passive descent. Because the field is always moving (Section 8.10), the departure a persistent reweighting achieves is **rate-induced escape from the moving attractor** — the floor outruns the state — which needs no second static basin and no bifurcation: the single moving well of the convex $\Phi$ suffices. Where the I's *imprinted* landscape itself carries more than one stable configuration, those are **metastable set-points** — history-sticky positions the slow $\rho$-writing has carved and does not spontaneously re-zero (chronic conditions displace the baseline for good); Mode B, as self-sourced imprinting, is how the I can re-carve one from inside. All of this operates only within a budget. Define **slack**

$$S_{m,t} = M_m(t) - \mathrm{Pressure}_{m,t},$$

where $M_m(t)$ is the inherited focus-capacity bound of Section 8.1 and $\mathrm{Pressure}_{m,t}$ is the capacity the current situation consumes — an open function rising with felt salience $V_{m,t}$ and with the determinacy of the demanded response, and carried *in the units of $M_m$* (it is what the situation spends of the same bounded capacity), so that $S$ is a capacity residual and not a difference of unlike quantities. The gate — itself a posited threshold, not a consequence of the definition of $S$:

- $S_{m,t} \leq 0$: the pressured filter dominates; focus allocation collapses to the contact-driven term of Section 8.2 and mode-response is automatic; there is no active Mode-B reweighting — passive descent of the local mismatch gradient. (This is *local relaxation of mismatch*, not maximization of present reward: $V$ is not a utility, Section 8.9. Automatic is not the same as myopic, and an automatic policy may well preserve future room.)
- $S_{m,t} > 0$: the reflexive operator can reweight the filter, moving the baseline against the local gradient — the self-directed term of Section 8.2 is available, and this is the felt sense of having chosen.

Slack thus supplies the operating condition of the two-phase focus split of Section 8.2: the self-directed term depends not only on accumulated lived-I structure but on momentary budget. Slack further divides into **perceived slack** (what the self-model certifies the will can use) and **actual slack** (what is available); their gap is the "stuck but capable" configuration — actual slack present, perceived slack low, the attempt never certified and so unused.

*Status.* $S = M_m - \mathrm{Pressure}$ is a definition atop one frozen primitive and one new open function: $M_m$ is the inherited capacity bound (Section 8.1), while $\mathrm{Pressure}_{m,t}$ is a new open function — of felt salience $V_{m,t}$ and of demanded-response determinacy — and therefore inherits the posited status of $V$ (Posits P1, P2). Its *dependence* is fixed in the sense of Section 8.8; its form is open. This $S$ is *one particular margin* — the reflexive-operating budget on focus/reweighting capacity — and does not exhaust the notion of slack: the broader construct is a **family of margins of unlike kind** (available time, regained ownership, meaningful engagement, and others; developed in *A Life Between Frames* in the research corpus), not a single fungible reserve, and this section formalizes only the one that gates Mode B. Two posited elements, flagged not asserted: (i) the **gate itself** — that positive budget is the condition for reflexive operation, with the threshold located at $S = 0$ — is a modeling posit, not a consequence of the definition of $S$ (positive budget, developmental availability of Mode B, actual reflexive firing, and felt choice are distinct, and their alignment at one threshold is the hypothesis); (ii) the stronger claim that felt-choice *dissociates* from behavioral output near $S = 0$ — the same action produced on either side of the threshold while felt agency flips — is a **prediction of the model, currently UNVERIFIED**, untestable until slack is independently operationalized. The architecture flags both rather than asserting them.

---

## End of File 3

Continued in File 4: Derived Concepts and Predictions.
