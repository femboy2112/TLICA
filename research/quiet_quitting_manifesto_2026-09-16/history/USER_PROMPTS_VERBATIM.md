# Recovered user prompts and conversation excerpts

**Coverage is partial.** This file preserves exact text from role-labeled history-retrieval records and points to the intact uploaded prompt. The search service did not provide a complete original conversation export or durable conversation URLs. Dates below are the timestamps reported by that service. A preserved string is not a claim that every original message has been recovered.

## Intact source prompts

- [Editorial + Publication Handoff](source_prompts/editorial_publication_handoff_2026-08-16.md): complete user-uploaded file, preserved byte-for-byte, including all nineteen sections, original wording and malformed math. Its SHA-256 matches the historical remaining-work audit: `70c05b09abc949dee0ab995c2d3e977f89c8875559af72c0be1fb03634b90be3`. Original filename: `Pasted markdown(20260816-224531).md`. The filename provides a date label, not a verified chat timestamp. It is a user-provided prompt artifact; sole authorship is not asserted.
- [Current archive request](source_prompts/archive_request_2026-09-16.txt): exact visible user-message body authorizing this non-main branch, with no added trailing newline. The platform’s GitHub-selection wrapper is metadata, not part of Leah’s authored request.

The uploaded handoff originally requested a canonical v2.0 and a shorter publication adaptation. Its instructions are preserved as historical evidence. Later rejection/rebase evidence governs the version interpretation; this archive does not execute the old publication instructions.

## Role-labeled retrieved messages

### M01 — user — 2026-08-17T15:55:36Z

Source: `pc_target_1` in [search log](../provenance/SEARCH_LOG.json). Completeness: **no truncation indicated by retrieval**. Original conversation URL unavailable.

````text
The other chat has gone off the rails. It is trying to make v2.0 the canonical version, but too much has been altered, and some of the original spirit has been lost. I'd like to, at a minimum, preserve v1.4 as the canonical full manifesto. If you think it's worth it, we can make a v1.5 that is more carefully worded and sourced, but I'd prefer to keep it closer in spirit to v1.4 than to the other chat's v2.0 rewrite
````

### M02 — assistant — 2026-08-17T15:56:15Z

Source: `pc_target_1` in [search log](../provenance/SEARCH_LOG.json). Completeness: **truncated**. Original conversation URL unavailable.

````text
That is the right editorial decision. **v2.0 should not become canonical merely because it is more heavily audited.** The core artifact is the one that still sounds like you and preserves the original imaginative force. So the version hierarchy should be:
- **v1.4 — canonical full manifesto / voice-preserving master**
- **v1.5 — optional careful revision, closer to v1.4 than v2.0**
- **v2.0 — alternate heavily audited adaptation, not canonical**
The test for v1.5 should not be “how much can we improve?” It should be: **what must be corrected, sourced, or clarified to make v
````

### M03 — user — 2026-08-27T01:06:12Z

Source: `pc_third` in [search log](../provenance/SEARCH_LOG.json). Completeness: **no truncation indicated by retrieval**. Original conversation URL unavailable.

````text
This is so fucking good, and I think it would make a great quantitative appendix or companion to the manifesto.
````

### M04 — user — 2026-09-16T06:14:18Z

Source: `pc_finalsearch_1` in [search log](../provenance/SEARCH_LOG.json). Completeness: **no truncation indicated by retrieval**. Original conversation URL unavailable.

````text
Please use @GitHub femboy2112/TLICA.git as the canonical source and review all our past conversations about my workplace and quiet quitting manifesto.
````

### M05 — assistant — 2026-09-16T06:14:35Z

Source: `pc_finalsearch_1` in [search log](../provenance/SEARCH_LOG.json). Completeness: **no truncation indicated by retrieval**. Original conversation URL unavailable.

````text
I’ll treat `femboy2112/TLICA` as canonical, use the repository’s current model as the baseline, and recover the workplace/manifesto history as an evidence-backed context package rather than relying on memory.
````

## Other recovered quoted wording

The [reported quotations](RETRIEVED_QUOTATIONS.md) retain additional wording from summaries and a retrieval-reported full prompt. They have weaker provenance than a role-labeled message and must not be silently promoted into a complete transcript. The full manuscripts are assistant-assisted documents, not substitutes for Leah’s original chat prompts.
