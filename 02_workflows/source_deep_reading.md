# Source Deep Reading Workflow

Updated: 2026-05-08

## ARIS Bridge

Read `01_policies/aris_bridge.md` first.

Engine skills:
- `/alphaxiv "arxiv-id"` — LLM-optimized arXiv summary with tiered fallback. Use for ML/CS papers and any arXiv-hosted preprint.
- `/research-lit "topic"` — multi-source literature survey that writes a landscape document.
- `/semantic-scholar`, `/openalex`, `/exa-search`, `/gemini-search` — alternative search backends.
- `/research-wiki ingest` — file the extracted source into the per-project wiki when the project opts in.

Binding rules:
- ARIS summaries are inputs, not authority. Source-context grading and acceptance into a manuscript role still pass through our extraction template into `source_context.md`.
- When a source will support a central manuscript, data-source, or method claim, also apply `references/source_verification_protocol.md` and record the result in canonical `qa/source_verification.md`; legacy/equivalent paths count only if mapped in `qa/artifact_mapping.md`.
- When a source affects novelty, contribution, closest-threat positioning, or literature-boundary claims, also update `qa/threat_literature_matrix.md` using `04_templates/threat_literature_matrix_template.md`.
- Page-level evidence and direct quotes still come from the original PDF, not from the ARIS LLM summary.
- Citation must include a verifiable URL; ARIS-only references without URL are rejected.
- ARIS may flag related papers; their threat-paper status is decided in our `02_workflows/idea_evaluation.md` flow, not by ARIS.

Purpose:
- read academic PDFs without context blowups or shallow summaries
- produce reusable source extracts for project `source_context.md`, literature review, replication planning, and idea screening
- preserve original PDFs while keeping split artifacts separate

Source:
- Adapted from Scott Cunningham's `MixtapeTools` split-pdf protocol: https://github.com/scunning1975/MixtapeTools/tree/main/skills/split-pdf
- Operational upstream skill: https://github.com/scunning1975/MixtapeTools/blob/main/.claude/skills/split-pdf/SKILL.md
- Source evidence grade: `B` for workflow use. It is a concrete public PDF-reading protocol, but it is not manuscript literature evidence.
- Local deployment status: accepted by human instruction on 2026-04-30.

## Trigger

Use this workflow when:
- a paper PDF is longer than about 15 pages and needs careful reading
- a source must support a manuscript claim, idea evaluation, or source-context entry
- a paper includes data, method, appendix, or replication details that a one-shot summary could miss
- another workflow needs paper details but should avoid filling the main session with PDF page context

For short papers, abstracts, or quick triage, read the source directly and record the limitation.

## Artifact Rules

Preserve the original PDF.

Use the PDF in place when possible. Do not move or rename it only for this workflow.

Create split artifacts under:

```text
<foldername>_build/split_<pdf_basename>/
```

Create reusable extraction next to the PDF:

```text
<pdf_basename>_text.md
```

If a project keeps sources under `documents/`, `literature/`, or `docs/sources/`, keep that convention and document it in `source_context.md`.

## Reading Protocol

1. Check whether `<pdf_basename>_text.md` already exists.
2. If it exists, use it unless the user asks for a fresh read.
3. If no extract exists, split the PDF into 4-page chunks.
4. Read at most 3 chunks per batch.
5. Update running notes after each batch.
6. Preserve both working `notes.md` and final `<pdf_basename>_text.md`.

When this workflow is called inside a larger project workflow, isolate PDF reading from the parent context when tool support allows it. The parent workflow should consume the final markdown extraction, not all PDF page renders.

## Required Extraction Fields

Each extraction must include:
- research question
- audience or literature
- method and identification strategy
- data source, unit, sample, period, and access notes
- statistical methods and key specifications
- main findings with exact numbers where available
- contribution
- limitations
- replication feasibility
- what this source can support in the current project
- what this source cannot support

## Project Integration

Update `source_context.md` with:
- source path
- extraction path
- citation key if known
- evidence grade
- source verification status when the source supports a central claim
- claims supported
- claims not supported
- replication or data-use notes

For idea evaluation:
- link the source to the closest-threat paper list
- record whether the source weakens, strengthens, or redirects the idea

For writing:
- do not cite the extraction itself as evidence
- cite the original paper or dataset
- use the extraction only as a reading aid

## Guardrails

- Do not delete the original PDF.
- Do not rely on a one-shot PDF summary for source claims that matter.
- Do not treat generated extraction as a substitute for checking the original source before submission.
- Do not mix workflow-source evidence with manuscript evidence.
