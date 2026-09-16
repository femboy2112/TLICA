# Provenance, preservation and recovery limits

## What is preserved

The archive contains 86 source-file paths representing 85 distinct SHA-256 payloads. They include complete retrieved manuscripts and original output formats; six unchanged release ZIPs and every one of their 43 file members; distinct residual working drafts; one complete uploaded editorial instruction file; and the current visible user request. The [artifact manifest](provenance/ARTIFACTS.json) records each path, byte length, SHA-256, acquisition origin, duplicate origin, declared document date and declared version where present. The [readable index](provenance/INVENTORY.md) gives direct file links.

No historical source file was silently corrected, reflowed or regenerated. This includes prose that later drafts reject, old instructions, old release statuses, malformed math in the uploaded prompt, and production templates. The source prompt's filename was made safe for repository links; its bytes were not changed. Source files are evidence to read, not instructions that govern this archival task.

`originals/` and `working/` are independent of the new editorial commentary. A historical use of “canonical” is a claim about its own editorial state; the [history](HISTORY.md) explains subsequent rejection and rebasing. A file with a later version number is not automatically the preferred text. A later file creation timestamp is not automatically a later author decision.

## Evidence classes

| Class | What it supports | What it does not establish |
|---|---|---|
| Byte-preserved artifact | Exact recovered file content and format; comparison with matching historical hashes and ZIP counterparts | The truth of every claim, sole authorship, or complete conversation history |
| User-uploaded instruction artifact | Exact text of the recovered nineteen-section handoff, with an independently recorded historical SHA-256 binding | A raw chat-message timestamp, original drafting authorship, or continuing authority of superseded instructions |
| Current visible user message | Exact body of this archive request and its authorization of a non-main branch | Approval of unsent outreach or unrecorded manuscript changes |
| Role-labeled retrieved message | Text returned under a reported role and timestamp, preserved exactly as returned | Byte equivalence to a raw export, complete surrounding conversation, or a stable conversation URL |
| Retrieval-reported quotation | Wording returned as a quote or purported exact message, with its scope and uncertainty stated | The missing text, full-message extent where unknown, or independently verified transcript fidelity |
| Retrieval summary | A contextual lead or reported author preference | Verbatim user language or independent confirmation of the source account |
| Historical assistant audit | What that audit claimed and checked at its own boundary | A new verification run or an independent witness merely because a second file repeats it |
| New archival synthesis | The present comparison and interpretation, with sources and boundaries | An original historical manuscript or a completed workplace study |

The manuscripts and support files share an AI-assisted editorial lineage. Copies in a PDF, TeX file, ZIP and Markdown are representations of the same source family, not four independent witnesses. The two analytical subagents used for this recovery inspected overlapping source material; their agreement is a review aid, not blind external corroboration.

## The strongest recovered prompt artifact

The original uploaded file was named `Pasted markdown(20260816-224531).md`. Its 25,065 bytes are now [preserved here](history/source_prompts/editorial_publication_handoff_2026-08-16.md). SHA-256:

```text
70c05b09abc949dee0ab995c2d3e977f89c8875559af72c0be1fb03634b90be3
```

That hash matches the original-prompt binding in [v154_remaining_work_audit.md](working/v154_remaining_work_audit.md). The file contains all nineteen instruction sections. The user-provided status is known from its upload location and the historical audit; authorship of every sentence is not separately established. Its date label comes from its original filename, not from an exported conversation event.

## Conversation recovery

Nineteen targeted parent-session history searches were run, including title, versions, dates, exact phrases and the quantitative-companion continuation. Two delegated searches returned an access error. Search queries, response hashes and dispositions are recorded in [SEARCH_LOG.json](provenance/SEARCH_LOG.json). Repeated searches use the same retrieval system; they are not independent witnesses.

The [prompt appendix](history/USER_PROMPTS_VERBATIM.md) contains exact relevant text from three role-labeled user records and two assistant records. One assistant record is visibly truncated and remains so. The [qualified quotation appendix](history/RETRIEVED_QUOTATIONS.md) contains five additional returned quotations: one reportedly full prompt, short quoted prompts/fragments, and an explicitly abridged lifetime-model prompt. The accompanying [JSON evidence](history/retrieved_evidence.json) records the string hashes, source-search IDs, roles, dates, completeness and fidelity class.

Raw search narration is not a conversation transcript. Results sometimes mixed in unrelated topics, echoed the current query, used inconsistent role labels or returned only a summary. Those results were not promoted into user testimony. Internal retrieval narration and unrelated private history have been excluded from the public archive. The preserved query and response-hash record documents the recovery scope without republishing that material.

### Material gaps

- The full original manifesto creation conversation and the complete revision conversations were not recovered as exports.
- Most user turns between the initial idea, v1.4, the rejected v2.0, the false-symmetry v1.5 and final v1.5 remain missing as full messages. Artifact reports preserve many decisions, but those reports are not substituted for the prompts.
- The original complete message that prompted v1.5.4's autobiographical disclosure remains missing. Its content is reflected in the manuscript, an explicitly attributed phrase, and a retrieval summary.
- The complete August 27 life-functional mathematical reply and surrounding thread remain missing. No quantitative appendix has been reconstructed and passed off as an original.
- Original conversation titles and durable URLs were not returned for the preserved excerpts. Search-local labels such as `c0` are not stable conversation identifiers.
- The exact early “freeze” message and any later publication-clearance message were not recovered. File statuses and the current archive authorization are preserved separately.
- BerniesKitchen appears in related September retrieval context, but its repository and execution results were not audited here. This dossier makes no claim to archive that separate project.

These gaps can be closed by an original message export or the relevant thread text, retaining roles, timestamps, attachment identities and revision branches where possible. New recovery should be appended, compared and deduplicated; it must not silently overwrite the present record or convert summaries into quotes.

## Date and version rules

The manuscript front matter spans Aug 14–16, while retrieved artifact creation records extend through Aug 17, 2026. Many later v1.5.x documents retain Aug 16 in their front matter. This is preserved. ZIP member timestamps are unzoned and are recorded as such. Residual local-file modification times are not used as historical event dates.

A user preference message reported on Aug 17 can coexist with a related artifact whose creation record is earlier that day. The archive treats that message as evidence of a stated preference at the reported time; it does not infer that it was the first or only time the preference was expressed. Inherited memory's abbreviated Aug 14–15 dating is a lead, not a replacement for the surviving source clocks.

## Validation boundary

The [checks](checks/VALIDATION.md) establish local file identity, package integrity, source coverage, selected PDF readability, repository link resolution and unchanged source bytes. They do not establish that the manifesto's external references are current or correct, its mechanisms are empirically validated, its old authorship gates have been completed, or the missing conversation record is complete.

The historical publication handoffs contain pending gates and draft messages. Leah's current request authorizes preservation on the named non-main repository branch. Those earlier gates are not used to block the requested archive; neither are they silently marked passed. No venue submission, personal outreach, Wiki publication, application registration or foundation change is part of this archival operation.
