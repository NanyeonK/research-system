# Literature Layer

Updated: 2026-05-24

Status: v2 workflow. Use with `02_workflows/research_pipeline_v2.md` and `03_agents/runtime_phase_matrix.md`.

Purpose

This workflow defines the literature layer for v2 research projects. It concentrates literature work at the points where it changes project routing, design, and claim safety. It uses three sources: internal graphify over the second_brain corpus, project-level graphify over the active project corpus, and external index scans through OpenAlex and Semantic Scholar when configured.

The literature layer is a discovery and verification workflow. It does not replace source verification, citation audit, or human judgment over paper relevance. Every citation used as evidence still needs title, author, year, venue or working paper source, URL or DOI, and role in the project.

## 1. Three-layer structure

### Layer 1. Internal graphify corpus

The internal graphify corpus is the second_brain literature graph. It is used to locate known papers, concept clusters, author communities, data-setting neighbors, and bridge papers that are already in Chan's research memory.

Internal graphify is queried first because it reflects the local corpus and prior reading. It can identify papers that external search may rank poorly but that matter for Chan's research agenda.

The internal graph is not enough for novelty. Graphify findings are leads. Direct threats must be verified against source metadata and external indexes before they enter a gate packet.

### Layer 2. Project-level graphify corpus

The project-level graph is built from the active project's refs, notes, source PDFs, analysis memos, and accepted external scans. It is narrower than the internal graph and should reflect the current project state.

Project-level graphify is useful after Phase 1, once the data and method plan has narrowed. It helps detect whether the project corpus has missing communities, weak bridges, or unconnected claims.

### Layer 3. External OpenAlex and Semantic Scholar scan

External scans protect against stale internal memory. OpenAlex is the default open index. Semantic Scholar is optional and should be controlled by configuration and environment variables.

External scans must save structured results in project artifacts. They should select only needed metadata: title, authors, year, venue, DOI, OpenAlex ID, URL, cited-by count when useful, abstract snippet when available, and source index.

## 2. Scheduled calls by phase

### End of Phase 0

Goal: route selection and threat detection.

Required questions:

- Which research community does this idea belong to?
- What are the three to ten closest threat papers?
- Is the idea closer to asset pricing, real-estate empirics, forecasting, interpretable ML, or conceptual institutional work?
- Does the local corpus already contain enough direct threat coverage?
- Should Chan be asked for missing papers before scoring or routing?

Required outputs:

- Phase 0 literature scan memo under `00_phase_router/` or `refs/`.
- Direct threat list with URLs or DOI placeholders.
- Paper request to Chan when direct threats are missing or ambiguous.
- Gate note for `qa/gate_status.yaml`.

### End of Phase 1

Goal: design validation.

Required questions:

- Which papers use similar data, units, sample periods, or institutional settings?
- Which papers use similar estimators, models, or forecast designs?
- Which papers would a skeptical referee cite against the narrowed plan?
- Does the narrowed design still look novel after external index search?
- Are there missing papers that block the pilot or main spec?

Required outputs:

- Updated `refs/literature_map.md` or equivalent artifact.
- Method and data comparator list.
- Chan paper request when needed.
- Archive of wide and mid literature options with Phase 1 wide plans when the project narrows.

### End of Phase 3

Goal: novelty protection after results exist.

Required questions:

- Which recent working papers make similar claims?
- Do new results duplicate a known result in a different setting?
- Does the main claim need narrowing because a closer paper exists?
- Do the three Figure 1 hook candidates exaggerate novelty?

Required outputs:

- `03_main_analysis/novelty_scan.md`.
- Claim-specific direct threat list.
- Human Gate 2 novelty note.
- Suggested claim narrowing or waiver item when needed.

## 3. Paper request format

When the literature layer needs Chan's help, use the template in `scripts/literature/paper_request_template.md`.

A request should be short and gate-aware. It should not ask for a broad reading list when one or two blocking papers are needed. It should state whether the request blocks a gate, narrows a claim, or is useful background.

Minimum fields:

- Project.
- Phase.
- Research type.
- Paper or topic needed.
- Why it matters.
- Current closest known papers.
- Gate impact.
- Requested action.
- Deadline or next digest time.

## 4. Configuration

Use `04_templates/literature_config.example.yaml` as the example config. Do not commit real local private paths or credentials. Project-local configs may copy this template and replace placeholders.

Required placeholder keys:

- `second_brain_literature_path`.
- `project_graphify_path`.
- `openalex_email`.
- `semantic_scholar_api_key_env`.

Scripts under `scripts/literature/` accept config paths and should fail closed when required values remain placeholders.

## 5. Internal graphify protocol

Use `scripts/literature/build_internal_graphify.sh` only to build or refresh a bounded internal graphify corpus. Do not graphify File Provider placeholders directly. If the corpus is under Synology Drive and raw files are not materialized, hydrate a bounded working set first and record materialization gaps.

Use `scripts/literature/query_internal.sh` to query an existing graph. It expects a graphify output path and a query string. It does not build the graph unless explicitly run after a build step.

Internal graphify output should be treated as structured discovery evidence. It can identify clusters, bridges, and candidate papers. It cannot alone verify that a citation supports a manuscript claim.

## 6. External scan protocol

Use `scripts/literature/external_scan_openalex.py` for OpenAlex scans. It is intentionally small and dependency-light. It uses Python standard library only. It accepts query, output path, email, year filter, and result limit.

OpenAlex scans should use the polite pool email when available. If the email remains a placeholder, the script still works but warns that polite-pool behavior is not configured.

Semantic Scholar support is represented in config for future extension. Do not add live Semantic Scholar calls unless the project supplies an API key through the configured environment variable.

## 7. Verification and evidence rules

A literature scan is gate-usable only if it records the query terms, source index, date, and selected result metadata.

A paper is direct-threat usable only if it has at least a title, authors or source, year, URL or DOI, and explicit relation to the project claim.

A claim cannot be protected by saying that graphify found no connection. Absence in a local graph is not absence in the literature.

If a paper request is unresolved, mark the relevant gate as blocked, conditional, or waived. Do not silently continue as if the scan were complete.
