# Research note: liberal education as semantic interoperability

**Date:** 2026-08-09  
**Status:** Author-derived application note; **UNVERIFIED** as an empirical model.  
**Integration target:** [`applications/this_is_water_truth_respecting_choice_v0_1_0.md`](../applications/this_is_water_truth_respecting_choice_v0_1_0.md), especially §3.2, *Education as governance of attention*.  
**Foundation impact:** None proposed. This note is an application-level extension and should not modify the frozen TLICA foundation merely to accommodate it.

---

## 1. The missing function of liberal education

The current *This Is Water* paper reconstructs Wallace's liberal-education argument into three functions:

1. exposing the partiality of an apparently self-evident frame;
2. making attention and interpretation available as objects of choice;
3. supporting the repeated practice needed for that capacity to survive ordinary pressure.

Those functions concern **governance of one's own attention and interpretation**. They capture an important part of Wallace's target, but they leave out a distinct social function of education that the present author wants to add rather than attribute to Wallace:

> **A broad shared education can function as semantic infrastructure: a civilization-scale attempt to install enough common conceptual structure in many minds that complex ideas can be communicated among strangers with higher expected fidelity and lower translation cost.**

The point is not that two educated people will agree. The point is that they are more likely to possess overlapping conceptual primitives, historical examples, formal tools, metaphors, and distinctions with which disagreement can be represented precisely.

This is the difference between **agreement** and **interoperability**.

---

## 2. Private languages over a shared world

Every person builds an internal representational system from a partly shared and partly private history. Ordinary language supplies a public interface, but words are decoded through a much larger private graph of remembered situations, emotional weights, analogies, learned abstractions, professional schemas, cultural references, and personal experience.

Let

$$
L_i : \mathcal{W} \rightarrow \mathcal{R}_i
$$

represent, schematically, person $i$'s learned mapping from encountered world-structure $\mathcal{W}$ into an internal representational space $\mathcal{R}_i$.

Two people can occupy the same world while constructing nonidentical representations:

$$
L_A(w) \neq L_B(w).
$$

Successful communication therefore does not require identical internal states. It requires enough preserved relational structure that a receiver reconstructs the load-bearing part of the sender's object:

$$
S \xrightarrow{E_A} m \xrightarrow{D_B} \widehat S_B,
$$

with acceptable communication when

$$
\widehat S_B \sim_{I} S,
$$

where $\sim_I$ means agreement on the declared invariant or set of invariants $I$ relevant to the communication.

The invariant may be causal structure, an analogy, an emotional relation, a logical dependency, a distinction between concepts, or some other feature that must survive transport. Literal identity of representations is neither expected nor required.

---

## 3. Shared basis and conceptual coverage

A useful mathematical analogy is to treat each person's available conceptual repertoire as a basis or toolkit $B_i$ for representing a family of target objects.

If two people have little conceptual overlap, then communication may require constructing many intermediate concepts before the target relation can be transmitted. If both have acquired a broad common library $C$, then

$$
B_A \cap B_B
$$

is effectively enlarged over the domains covered by $C$, lowering the expected cost of semantic transport.

For a target family $\Omega$ of concepts or relational objects, define only schematically—not yet as a validated quantitative measure—a weighted **shared coverage**:

$$
\mathrm{Cov}_{\Omega}(A,B)
=
\sum_{x\in\Omega} w(x)\,\mathbf 1[\text{A and B possess a usable common representation of }x].
$$

The claim is not that larger coverage guarantees understanding. Rather:

$$
\mathrm{Cov}_{\Omega}(A,B)\uparrow
\quad\Longrightarrow\quad
\mathbb E[\text{translation cost}]\downarrow
$$

for communications whose load-bearing structure lies inside the covered region.

A liberal education can therefore be interpreted as an attempt to increase **cross-person conceptual coverage** over unusually generative domains: history, literature, philosophy, mathematics, natural science, politics, religion, art, rhetoric, and social thought.

The educational ideal is not literal storage of "the total knowledge of civilization." No finite curriculum can do that. The stronger and more defensible formulation is:

> **Transmit a compact but generative subset of accumulated human knowledge that gives later thinkers high coverage over recurring structures and efficient pointers into the larger archive.**

---

## 4. Sisyphus as semantic compression

Consider the statement:

> "My job feels repetitive, futile, and structured so that every apparent accomplishment is erased before the next cycle begins."

If two people share the cultural object *Sisyphus*, a single adjective can encode much of that structure:

> "My job is Sisyphean."

The word functions as a pointer to an already-installed relational object:

$$
\text{labor}
+
\text{recurrence}
+
\text{temporary progress}
+
\text{reset}
+
\text{futility}.
$$

The communication is dramatically shorter because the receiver supplies most of the decompression from prior shared knowledge.

This is the same mechanism that makes a well-chosen popular-culture reference or meme high-bandwidth. Saying "Weekend at Bernie's" in the right workplace context can transmit something like:

$$
\text{institutional body persists}
+
\text{animating purpose has died}
+
\text{participants preserve the appearance of continued life}.
$$

The liberal-arts canon and internet meme culture therefore perform partially analogous communication functions at very different scales:

- **memes/popular culture:** rapidly distributed contemporary analogy primitives;
- **professional jargon:** narrow, high-bandwidth domain primitives;
- **liberal intellectual culture:** deliberately curated, historically deep, cross-domain primitives;
- **close relationships:** custom-trained private codecs with extremely high local compression.

The important variable is not prestige. It is **shared prior structure**.

---

## 5. Liberal education as a semantic standard library

On this model, one social value of liberal education is that it attempts to give strangers a partially standardized **semantic standard library**.

A person who has encountered Sisyphus, Plato's cave, Darwinian selection, statistical regression, tragedy, the scientific method, basic constitutional history, competing ethical theories, and the history of major social institutions does not merely possess isolated facts. They possess reusable representational objects.

Those objects become callable in later reasoning.

A new observation can often be expressed as:

$$
\text{new object}
=
\text{known object}
+
\text{important residual}.
$$

This supports both communication and intellectual progress. An interlocutor can say:

> "That resembles X, except for Y."

The old object supplies a shared coordinate system; the residual $Y$ identifies what is genuinely new or different.

This also provides **historical deduplication**. A person may independently rediscover a structure that has already been studied under another name. Shared intellectual culture can map the new observation onto earlier work, allowing the thinker to inherit prior successes, counterexamples, distinctions, and unresolved problems rather than restart from zero.

---

## 6. The extension to *This Is Water*

This is **not** proposed as a hidden thesis Wallace must have intended. It should be marked explicitly as a TLICA/author extension adjacent to his argument.

Wallace's delivered-address argument, as reconstructed in the current paper, concerns the capacity of education to make one's default setting visible and contestable. The proposed extension is:

> **The same broad education that increases the representational resources available for inspecting one's own frame can also increase the stock of representations shared with other people, making frames more mutually inspectable.**

Thus liberal education can have both an **intrapersonal** and an **interpersonal** function:

$$
\begin{array}{ll}
\textbf{intrapersonal:} & \text{gain alternatives with which to inspect and reorient one's own frame};\\[1mm]
\textbf{interpersonal:} & \text{gain shared representations with which to transport those frames between minds}.
\end{array}
$$

The second function matters because reflective freedom is not exercised in isolation. People reason together, argue, teach, coordinate, criticize, witness, and revise each other. A richer shared conceptual library makes it more likely that one person can communicate not merely a conclusion but **the perspective from which the conclusion became visible**.

This yields a candidate fourth educational function for §3.2:

4. **builds shared conceptual infrastructure that increases the expected fidelity of perspective transport among differently situated minds.**

The wording should preserve that this is the author's extension, not a direct textual claim about Wallace.

---

## 7. Relation to TLICA

This note does not require a new foundation coordinate.

The closest existing TLICA connection is to **toolkit-relative truth-indistinguishability $\phi$** and verification-pathway access. A shared concept can supply a previously unavailable representation, analogy, discriminator, or inferential route. In that limited sense, education can expand the toolkit closure available to a person.

But shared representation must not be confused with truth.

Two people can possess the same conceptual library and confidently share the same false model. High semantic interoperability can therefore coexist with poor source attribution, bad evidence, coordinated prejudice, or a systematically inadequate map of reality.

So:

$$
\boxed{\text{shared language} \neq \text{shared truth}}
$$

and

$$
\boxed{\text{communicability} \neq \text{correctness}.}
$$

This distinction is load-bearing. The proposed value of liberal education is that it can increase representational and communicative reach; TLICA's epistemic discipline must still ask whether the transported object is well sourced and survives appropriate verification.

---

## 8. Failure modes and hostile controls

Any integration into the paper should include the following limits.

### 8.1 Degree status is not the construct

"College graduate" is at most a noisy proxy for conceptual coverage. A person can obtain a degree without retaining a broad shared library; another can acquire a much richer one independently.

The target variable is actual usable overlap, not credential status.

### 8.2 A canon can create shared blind spots

A standardized library can improve interoperability while narrowing what is collectively representable. If everyone inherits the same omitted distinctions or source errors, communication may become extremely efficient inside a systematically defective model.

Shared priors can therefore produce both:

$$
\text{semantic interoperability}
$$

and

$$
\text{correlated compression loss}.
$$

This directly echoes the paper's warning that education can make a frame inspectable without guaranteeing that the selected replacement is true or good.

### 8.3 More vocabulary can increase pseudo-understanding

Two people may share labels while attaching materially different relational objects to them. Terminological overlap is therefore weaker than structural overlap.

A useful conversational probe is not "Do you know the term?" but:

> "Can you reconstruct the relation I am using the term to point at?"

### 8.4 Shared background does not eliminate private idiolect

Biographical experience, affect, trauma, subculture, profession, and personal analogy networks continue to shape decoding. No curriculum yields a universal lossless human codec.

The generalizable target is therefore likely a **communication procedure**, not one universal representation:

$$
\text{recover invariant}
\rightarrow
\text{estimate receiver basis}
\rightarrow
\text{choose transport}
\rightarrow
\text{request reconstruction}
\rightarrow
\text{transmit residual}.
$$

---

## 9. Candidate empirical predictions

These are **UNVERIFIED** and should remain application-level hypotheses unless independently tested.

1. **Shared-reference compression.** For a relational claim whose relevant reference object is genuinely shared, explanation length should fall while reconstruction accuracy remains stable or improves.
2. **Concept-overlap beats credential status.** Direct measures of shared conceptual repertoire should predict communication fidelity better than degree/no-degree classification.
3. **Analogy availability matters.** When sender and receiver share an analogy primitive closely matching the target structure, fewer repair turns should be required to reach an accurate paraphrase.
4. **Shared-error amplification.** High conceptual overlap built from the same defective source family can increase confidence and conversational fluency without increasing external accuracy.
5. **Perspective transport is separable from agreement.** A receiver can accurately reconstruct a sender's perspective while rejecting the sender's conclusion; measures of understanding should therefore be kept separate from assent.

Possible experimental tasks could present pairs of participants with relational descriptions, manipulate the availability of a shared reference corpus, and measure message length, paraphrase fidelity, repair turns, confidence, and factual accuracy separately.

---

## 10. Suggested insertion into §3.2

A concise paragraph suitable for incorporation after the current three-function list:

> **An author-level extension follows from this educational picture.** Broad education may do more than make one's own frame inspectable: it can also build shared conceptual infrastructure among differently situated minds. Literature, history, philosophy, mathematics, and science supply reusable objects, distinctions, and analogies that function as a partially standardized semantic library. Where two people possess enough of that library in common, a complex relational structure can often be transmitted by reference rather than rebuilt from first principles—"Sisyphean" can carry an entire model of recurring futile labor in one word. The value is not agreement and certainly not truth by consensus. It is **semantic interoperability**: increased probability that strangers can reconstruct one another's perspectives with tolerable loss, then locate their actual disagreement. This is proposed here as an extension of Wallace rather than attributed to the speech itself.

A possible fourth item after the existing three functions:

> 4. builds shared conceptual infrastructure that increases the expected fidelity of perspective transport among differently situated minds.

---

## 11. Claim ledger

| Claim | Status |
|---|---|
| The current *This Is Water* paper reconstructs education as frame exposure, selectable attention/interpretation, and sustained practice | **Observed in repository text** |
| Shared prior conceptual structure can reduce the amount of explicit information needed for communication | **Corroborated at the level of standard communication logic; exact human model not established here** |
| Liberal education should be modeled as a civilization-scale semantic interoperability layer | **Conjectured / interpretive extension** |
| Liberal education approximates a generative compression of accumulated human knowledge rather than literally containing total knowledge | **Interpretive formulation** |
| Greater actual conceptual overlap lowers expected translation cost for relevant target structures | **UNVERIFIED as a quantitative human prediction** |
| A college degree reliably implies this overlap | **Rejected** |
| Shared vocabulary or conceptual overlap implies truth | **Rejected** |
| A common canon can increase both interoperability and correlated blind spots | **Conjectured; requires empirical/historical analysis by case** |
| Perspective reconstruction and agreement are distinct variables | **Structural distinction; empirical operationalization still required** |

---

## 12. Compact formulation

The central proposal can be reduced to:

$$
\boxed{
\text{liberal education}
\approx
\text{shared conceptual coverage}
\rightarrow
\text{lower semantic translation cost}
\rightarrow
\text{higher-probability faithful perspective transport}
}
$$

subject to the critical boundary:

$$
\boxed{
\text{interoperability is not truth.}
}
$$

Wallace's insight is that education can help a person notice and choose among frames. The present extension is that a sufficiently broad shared education can also help **different people make those frames mutually visible**.
