# Sources and provenance: positive-view representations versus TLICA learning

**Compiled:** 2026-11-10. This list distinguishes the paper's author-origin claims from TLICA's existing theory and the new, independently untested synthesis.

## External primary research

**[E1]** Randall Balestriero and Yann LeCun (2026-10-29), *Proving and Improving the Platonic Representation Hypothesis with JEPAs*, arXiv:2610.39302.  
Primary source: https://arxiv.org/abs/2610.39302  
Relevant sections: §2.1 (finite world, shared positive pairs, injective renderings, rotational uniqueness), §2.2 (positive-pair kernel mismatch and eigengaps), §2.3 (good views versus same-observation corruptions), §2.4 (their particular next-token-prediction equivalence), §4 (experiments), §7 (limitations), Appendix A (proofs).

**Precisely supported:** in the paper's idealized objective class, shared world-positive relations lead to the same population representation up to rotation when minimizers are unique up to rotation; the whitened/spectral case provides an explicit condition. The authors report better alignment with good views on their experiments and a same-corpus 21.6M-versus-900M sample comparison. These are **the authors' results**, not an independently reproduced TLICA experiment. Their theorem does not cover all action-conditioned JEPA variants, arbitrary recurrent conditioning, raw ambient association, or human learning.

**Authors' stated caveats:** finite world, injective renderings, symmetric positive laws with matched marginals, population optimality; idealized uniqueness is not proved for every full-distribution regularizer; real observations are lossy; data supervision enters via view construction; large-scale caption pairs may share upstream generated-content provenance.

**[E2]** Balestriero and LeCun's released implementation for [E1]: https://github.com/galilai-group/prh-proof  
Includes paper-linked theory, reproducibility instructions, train/evaluation scripts, and reported experiment registry. **Same author/source family as [E1]**; a code release is valuable provenance and potential reproduction infrastructure, not independent confirmation. No upstream benchmark was run for this dossier.

## Existing TLICA authoritative apparatus

**[T1]** [Foundation File 3, §§8.1–8.8](../../foundation/3_formal_apparatus.md): substrate focus capacity; contact/self focus split; probe weights; imprinting dynamics; osmotic imprinting always online, possibly negligible effective update; formation versus activation; proto-tools.

**[T2]** [Foundation File 2, §3.2](../../foundation/2_access_and_development.md): verification-tool imprinting, substrate proto-patterns, explicit Mode B access and later refinement. **Frozen foundation; no edit requested or made.**

**[T3]** [Choice as Filter, §15](../../applications/choice_as_filter_v0_1_0.md): osmotic baseline versus filter-amplified differential updates; compiled later toolkit change.

**[T4]** [Grokking as Toolkit Closure](../grokking_as_toolkit_closure_2026-08-29.md) and its [pre-existing experiment protocol](../grokking_toolkit_closure_experiment_protocol_2026-08-29.md): finite local-path overlap model, relative gauge ambiguities, actual toolkit closure versus behavioral disclosure, controls on bridge validity and degree.

**[T5]** [TLICA-HIGGS: Frame Scattering and Osmotic Imprinting](../tlica_higgs_phenomenological_mass_2026-10-21/FRAME_SCATTERING_OSMOTIC_IMPRINTING_2026-10-22.md): accidental co-occurrence can reinforce an edge in a finite recurrence even when that correlation is not objective evidence; focus-conditioned sampling and source limits.

**[T6]** [Developmental Substrate Nonstationarity](../developmental_substrate_nonstationarity_2026-09-15/README.md): distinction between learning within a substrate and learning while the substrate itself changes; no inference that the proposed JEPA model captures neural development.

**[T7]** [Semantic Optics](../semantic_optics_2026-10-01/FORMALISM.md) and [Salience, Frame and Provenance](../salience_frame_provenance_2026-10-14/FORMALISM.md): observer mapping, conditional probes, source provenance, and the necessity of not conflating interpretation with truth.

## New synthesis and independence warning

The mapping between [E1]'s normalized positive-pair kernel, [T1]'s osmotic candidate patterns, and [T4]'s validated tool overlap is **constructed here**, not extracted from any of those sources. The conjectured transition from latent embeddings to explicit mental verification tools is a proposed research mechanism. Neither [E1] nor the current TLICA archive empirically confirms that bridge.

A future evidence review should use (1) an independent theorem proof/implementation of the finite spectral case; (2) fresh, blinded representation-learning holdouts with true/corrupted pairs and explicit source tracking; and (3) if extending to biological claims, a genuinely distinct behavioral or neuroscientific measurement. Do not count several articles or code samples repeating [E1] as independent source families.
