# High-impact encounters: scattering, field reconstruction, and moving spectral zeros

**AdultClub™️ / TLICA working paper extension, 2026-10-11.**
**Origin:** Leah's high-energy collision analogy and her earlier finite/Archimedean–RH-zero analogy; preserved exactly in [AUTHOR_RECORD.md](AUTHOR_RECORD.md).
**Assistant development:** typed two-timescale system, toy double-well, exact finite counterexamples, evidence boundaries and proposed tests.
**Epistemic status:** construction-level mathematical examples **DISCLOSED within assumptions**; proposed developmental/psychological mapping **CONJECTURED / UNVERIFIED**. Not an RH proof, neural field theory, or demonstrated psychological phase transition.

## 1. The author insight and the necessary distinction

The author proposes that in ordinary encounters, incoming information is deflected through the observer's existing attractor structure and available rerouting relations; exceptional high-impact encounters can change the self-field itself. This follows the prior [field-polarity note](FIELD_POLARITY_AND_TRANSPORT.md): self-referential signed evaluations, attentional capture, and dynamical attraction are distinct objects, and individual model routes can be helpful or harmful independently of their signs.

The strongest faithful technical interpretation is not simply "a more energetic idea crosses a fixed obstacle." It is **an interaction with coupled degrees of freedom**, in which the recipient's meaning-making structure may respond by changing itself.

A pure scattering model freezes the sources generating the field. In a dynamical self-update model, those sources—learned associations, interpretive bridges, priority weights and self-related commitments—are allowed to evolve. Their updating can modify future trajectories even after the original stimulus disappears.

**Two different outcomes:**
- **Motion through the existing field:** activation, deflection, local rerouting, switching from one preexisting attractor basin to another, or strategic deference. Such a change can be dramatic or lasting without changing the generating landscape.
- **Modification of the generating field:** a change to the learned transition rule, self-referential weights, source map, set of accessible interpretive routes, or response function. The field itself is different for future probes.

Both can co-occur. Neither is equivalent to emotional intensity. High-intensity exposure can also consolidate an old defensive policy, constrain flexible inquiry, or produce no measurable long-term change.

## 2. Two timescales, not a universal threshold

Let $x_{i,t}$ be an observer's currently active response/interpretation and $G_{i,t}$ their slower learned structure (existing TLICA notation uses $G$ for slow lived-I structure). Given event $q_t$ and context $E_t$, a general schematic system is:

$$
x_{t+1}=T_{G_t}(x_t,q_t,E_t),\qquad
G_{t+1}=G_t+\varepsilon I(G_t,q_t,E_t)+J(G_t,x_t,q_t,L_t,H_t).
$$

Here $\varepsilon I$ denotes incremental imprinting, and $J$ is a **candidate** stronger context-dependent structural update. $L_t$ is a family of slack constraints, $H_t$ the observer's relevant history. Neither is a scalar energy quantity. The notation is bookkeeping: there is no measured human update operator, no assumption that $J$ is additive in reality, and no requirement that it activates only above a sharp threshold.

The physical analogy's "collision energy" must be unpacked into separable influences: stimulus salience, personal load relative to capacity, violated predictions, connection to self-referential commitments, threat or safety, repeat exposures, opportunities to probe and consolidate, and actual degrees of freedom for changing behavior.

One possible update law can have an *effective gate* depending on these variables, but a threshold is optional and may change over development. **High emotional load is neither logically necessary nor empirically sufficient for a durable change in $G$.**

## 3. Exact countermodel: basin crossing is not landscape change

Choose a scalar fast state $x$ with an illustrative tilted double-well potential,

$$
V(x;a)=(x^2-1)^2+a x.
$$

At $a=0$, minima lie at $x=\pm1$, each with value zero, separated by the barrier at $x=0$ of height $1$. Under an idealized conservative evolution with fixed $a$, a state entering a well with kinetic energy greater than the barrier can cross to the other well. But **the structural parameter $a$ is unchanged**.

Changing $a$ instead changes the actual landscape. Its derivative is $V'_x=4x(x^2-1)+a$, while $V''_{xx}=12x^2-4$. A fold/saddle-node occurs when both vanish, giving

$$
|a|=\frac{8}{3\sqrt3}\simeq1.5396007178.
$$

On one side of that fold, two minima coexist; beyond it one of the former minima disappears. This is a **model-level change in attractor structure**, not simply motion of a point to another basin.

Crucially, no single "high-energy collision" is required. If the structural parameter changes in small steps—e.g. eight artificial increments of $0.2$—its accumulated change passes the same fold value. These are chosen model units, not measurements of social experience.

The example defeats the implication **high event intensity ⇒ structural self-update**. Conversely, absence of dramatic experience does not preclude accumulated structural change.

## 4. Connection to the author's moving-zero analogy

The author also proposes that each person's global self-field is constructed in a way reminiscent of RH zero structure. The two thematic inputs were described as:
- **historical/acquisition side:** age at acquisition, early proto-model organization and history order;
- **relational/whole-field side:** self-relative event intensity and the web of field connections.

These are **not** the actual number-theoretic finite and Archimedean places, which in the RH problem encode local arithmetic/Mellin factors and a real-place Gamma factor. In the real zeta problem the completed $\xi$ is fixed; its nontrivial zeros and the critical symmetry line are not altered by a human learning event. Thus there is no RH result or prime–Gamma transport established by this analogy.

For the evolving human-field model, one could choose a *time-dependent generating function* $F_{G_t}(z)$ and inspect zeros $\mathcal Z_t$. To be scientifically informative, the function must be independently constructed from source and update rules **without fitting to desired zeros or merely relabeling coordinates**.

### A finite toy in which zeros really do move

Take

$$
F_a(z)=z^2-a.
$$

For $a=-1$, the zeros are $z=\pm i$, lying on the **illustrative reference axis** $\mathrm{Re}z=0$; for $a=0$, they coalesce at $0$; for $a=1$, they lie at $z=\pm1$, off the reference axis. Changing $a$ changes the function, so zero motion is unsurprising. This is a two-zero polynomial example, **not a model of zeta zeros or an implication about RH**.

The "critical line changes" metaphor requires an invariant criterion: a moving reference axis can simply be a moving coordinate system. Before claiming a structural self-update from displaced zeros, hold the gauge/normalization fixed and compare actual task-relevant predictions.

### Decisive obstruction: zeros alone need not encode the actual structure

Even a fixed full multiset of zeros need not uniquely identify the process generating responses.

Consider the exact matrices

$$
A_0=\begin{pmatrix}0&0\\0&0\end{pmatrix},
\qquad
A_1=\begin{pmatrix}0&1\\0&0\end{pmatrix}.
$$

Both have characteristic polynomial $\det(zI-A_j)=z^2$, hence identical zeros with multiplicity. Yet for $v=(0,1)^T$,

$$
e^{A_0}v=(0,1)^T,\qquad e^{A_1}v=(1,1)^T
$$

since $A_1^2=0$. **The same zero set can coexist with different response dynamics.** This is an exact, simple counterexample to the unqualified assertion that zeros alone capture every relevant relation in the self. To make spectra complete, supply extra assumptions or additional data such as eigenspaces/Jordan structure, residues, source and probe responses.

A zero leaving an illustrative symmetry axis could reflect structural parameter change, a gauge shift, altered observation mapping or an artifact; **it does not uniquely identify a self-update**.

## 5. What is actually measurable?

The target is a *durable change in counterfactual response geometry*, not one emotional peak.

Measure the same independently predeclared family of content-equivalent probes at baseline, after an event, and across later follow-ups, while varying context and making source/warrant explicit. Independently record: emotional intensity, expectation mismatch, perceived safety, ability to follow alternative routes, change in interpretive generalization, source memory, normative assent, and behavior.

The strongest diagnostic is whether the old baseline state can be recovered while **the future response rule still differs**. However, even persistent difference in observed responses need not identify internal $G$; multiple latent states can produce the same measured output. Blinding, repeated contexts, source records and sufficiently discriminating interventions are required.

A short-term basin switch may persist without any parameter update; conversely a slow parameter update may remain behaviorally silent until the right context arrives. Thus **no one-shot self-report distinguishes these models**.

## 6. Discriminating probe, declared before test

Design a low-stakes, ethically safe task with learned rules and several possible routes. Manipulate **event surprise/prediction error**, **salience**, and **safe opportunity to revise**, each independently, while preserving task evidence and avoiding real threats. Compare a purely fast-state switching model, a slow-parameter update model, and a hybrid model on fresh held-out contexts and post-event follow-ups.

Predictions to differentiate:
1. A **fixed-field switch** model can predict change among known strategies after a large perturbation, but under suitable state-reset/probe normalization should return the original response mapping.
2. A **structural update** model predicts post-event changes to generalization or route availability that persist across contexts, after accounting for current-state changes.
3. A **habit reinforcement** model predicts that larger affective load can intensify old defensive responses without improving epistemic integration.
4. A **gradual learning** model predicts structural shifts after accumulated smaller informative events without a singular high-intensity episode.

**Pass for the distinct structural mechanism:** a preregistered, out-of-sample improvement over fixed-geometry switching and ordinary learning alternatives, with independently grounded event/response measurements.  
**Failure:** differences disappear after controlling current state or are equally fitted by fixed-field dynamics; high salience explains only transient affect; null or opposite relation between surprise and transfer.  
**Ambiguous:** unmeasured context changes, memory contamination, no reliable state-reset proxy, or underdetermined latent models.

Do not attempt to trigger distressing experiences to test the analogy. No result in a toy simulation measures an actual observer.

## 7. What current neuroscience does and does not support

Adjacent evidence, not TLICA validation:

- Sevenster, Beckers and Kindt (2013), *Science*, [DOI 10.1126/science.1231357](https://doi.org/10.1126/science.1231357), report that prediction error was necessary for memory reconsolidation in a studied human associative-fear paradigm. That result does not mean that all model restructuring requires one particular prediction-error mechanism.
- Schwabe and Wolf (2009), *Journal of Neuroscience*, [DOI 10.1523/JNEUROSCI.0979-09.2009](https://doi.org/10.1523/JNEUROSCI.0979-09.2009), report experimentally induced stress favoring habitual behavior in humans. This is a direct caution against equating high emotional energy with flexible self-revision.
- Milton, Das and Merlo (2023), *Brain Research Bulletin*, [DOI 10.1016/j.brainresbull.2023.01.010](https://doi.org/10.1016/j.brainresbull.2023.01.010), discuss the difficulty of identifying conditions and biomarkers for memory destabilization. A clinical translation is not established by the present philosophical model.
- van Herk et al. (2024), *Neurobiology of Stress*, [DOI 10.1016/j.ynstr.2024.100659](https://doi.org/10.1016/j.ynstr.2024.100659), review mechanisms through which acute stress can compromise decision-making; again, intensity is not a universal learning accelerator.

These research programs study particular memory/action systems, not a person's whole TLICA $G$ or the mathematically defined trajectory of spectral zeros. Similarity of vocabulary is **not independent corroboration**.

## 8. Reproducibility and conclusion

The standard-library [finite_update_countermodels.py](finite_update_countermodels.py) checks the double-well barrier/fold, moving zeros of a toy polynomial, and nonuniqueness of dynamics given zeros. The local execution on 2026-10-11 passed **10/10 construction-level assertions**; results are designed finite witness checks and **not** independent empirical evidence. Re-run the script to verify this claim in the current checkout.

**Verdict:** the strong research direction is a coupled theory of **momentary trajectory, slowly evolving field, and observation-induced model revisions**. The "high-energy particle collision" metaphor motivates a *possible regime change* but does not supply a physical conserved energy, a universal threshold, a clinical claim or a zeta-theoretic identification.

> **An event can move an observer through the landscape they already inhabit, or it can change the landscape that future observations will inhabit. The difference must be established by what persists and what future probes can distinguish.**
