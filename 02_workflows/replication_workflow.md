# Replication Workflow

Updated: 2026-05-24

Status: v2 workflow for Phase 6. Use with `../03_agents/replication-builder.md`, `research_pipeline_v2.md`, and `paper_factory_quality_gates.md`.

Purpose

Phase 6 turns the accepted Phase 3 results and Phase 4 skeleton artifacts into a reviewer-facing replication package. It is not a cleanup folder and not a dump of the live project. It is a self-contained, minimal, verified package that rebuilds the submitted exhibits with documented dependencies, hashes, and instructions.

The workflow supports R, Python, and mixed R/Python projects. It prefers one canonical processed dataset and one package-local wrapper per shipped exhibit unless restricted data rules require a different structure.

## Entry condition

Start Phase 6 only after Human Gate 2 accepts the main analysis direction or Chan explicitly requests an early replication seed. If Human Gate 2 changes the main claim, table order, Figure 1 hook, or sample, return to Phase 3 or Phase 4 before packaging.

Required inputs:

- `project_state.md`
- `decision_log.md`
- `specs/main_spec.md`
- `specs/output_spec.md`
- `qa/gate_status.yaml`
- `qa/claim_verification_matrix.md`
- final Phase 3 result artifacts
- Phase 4 skeleton or exhibit spine
- data provenance notes
- environment notes for R, Python, or both

## Output contract

The package lives under `06_replication/` inside the project repo unless a journal-specific package root is required. It should contain:

```text
06_replication/
  README.md
  AEA_README.md
  code/
    run_all.sh
    run_main_text.sh
    run_appendix.sh
    exhibits/
  data/
  output/
    main/
    appendix/
  metadata/
    EXHIBIT_CROSSWALK.csv
    MANIFEST.csv
    HASHES.sha256
  environment/
    renv.lock
    uv.lock
    pyproject.toml
    requirements.txt
  docs/
    DATA_PROVENANCE.md
    REPRODUCIBILITY_NOTES.md
    REPLICATION_PACKAGE_OVERVIEW.md
  package_zip/
```

Not every project needs every file, but omissions must be explained in `REPRODUCIBILITY_NOTES.md`.

## Seven-stage workflow

### Stage 1. Extract dependency graph

The replication-builder reads the accepted artifacts and builds a dependency graph from exhibit to script, script to data, and script to environment. It should not rely on memory or prose claims.

Minimum graph fields:

- exhibit id
- canonical output path
- source script
- wrapper script
- input dataset
- helper files
- package dependencies
- runtime language
- restricted-data status
- expected hash after rerun

If graph extraction reveals that an exhibit cannot be traced to a script or dataset, the package is blocked. Do not fake a source path.

### Stage 2. Create master scripts

Create package-local entrypoints:

- `code/run_main_text.sh`
- `code/run_appendix.sh`
- `code/run_all.sh`

`run_all.sh` should call the other entrypoints rather than duplicating logic. Each shipped exhibit should have one thin wrapper under `code/exhibits/` where practical. The wrapper may call a live analysis generator copied into the package, but it must assert that the expected output exists.

Entrypoints must fail closed with `set -euo pipefail` for shell scripts. R and Python scripts must exit nonzero on missing data, missing dependency, or missing output.

### Stage 3. Lock environments

R projects use `renv` where possible:

```r
renv::init(bare = TRUE)
renv::snapshot(prompt = FALSE)
```

Python projects use `uv` where possible:

```bash
uv init --no-readme --bare
uv add <packages>
uv lock
```

Mixed projects should include both locks and explain the run order. If a project cannot use `renv` or `uv`, write the reason and a minimal fallback in `REPRODUCIBILITY_NOTES.md`.

Do not commit local virtual environments, package caches, or private credential files.

### Stage 4. Generate SHA256 hashes

After the package reruns successfully, hash all shipped data, code, metadata, and canonical outputs.

Recommended command:

```bash
find code data docs metadata output environment -type f \
  ! -name '.DS_Store' -print0 | sort -z | xargs -0 sha256sum > metadata/HASHES.sha256
```

On macOS, use `shasum -a 256` if `sha256sum` is unavailable. The command used should be recorded in `REPRODUCIBILITY_NOTES.md`.

`metadata/MANIFEST.csv` should include path, role, size_bytes, sha256, and notes.

### Stage 5. Create AEA README

Create `AEA_README.md` following the spirit of the AEA Data Editor checklist.

Required sections:

- Overview
- Data availability and access conditions
- Software requirements
- Hardware and approximate runtime
- Instructions to reproduce main text exhibits
- Instructions to reproduce appendix exhibits
- Mapping from exhibits to scripts and outputs
- Description of restricted or proprietary data if any
- Random seed and stochastic procedure notes
- Expected outputs and hashes
- Contact or maintainer placeholder

If data cannot be redistributed, provide a clear restricted-data path and a synthetic or metadata-only smoke test only if Chan approves it.

### Stage 6. Self-test

Run the package from a clean shell and record the result.

Minimum self-tests:

- `bash code/run_main_text.sh`
- `bash code/run_appendix.sh` if appendix exists
- `bash code/run_all.sh`
- verify all canonical outputs exist
- verify `metadata/EXHIBIT_CROSSWALK.csv` points to existing wrapper scripts and outputs
- regenerate hashes after the final rerun

Do not declare Phase 6 complete without rerun verification.

### Stage 7. Prepare upload zip

Create an upload-ready zip under `package_zip/` only after self-test passes.

The zip should include code, data or allowed data documentation, outputs if the target repository requests them, metadata, environment locks, and README files. It should not include raw private data, credentials, local caches, agent scratch logs, or unapproved manuscript drafts.

Zenodo and OpenICPSR handling is documentation-only in this workflow. Do not implement live upload commands and do not call upload APIs without explicit approval.

## AEA Data Editor alignment

The package should make it possible for a reviewer to answer these questions:

- What data are required?
- Can the data be shared?
- Which scripts reproduce each exhibit?
- What software and package versions are needed?
- How long should the run take?
- Which outputs should appear after rerun?
- Which restrictions prevent full reproduction?
- Are hashes provided for shipped files?

If any answer is missing, Phase 6 remains incomplete.

## R and Python stack rules

For R:

- use `renv.lock` when possible
- use package-local paths
- avoid reading from the live project tree after packaging
- keep table and figure scripts deterministic
- define seeds for simulation or bootstrap steps

For Python:

- use `pyproject.toml` and `uv.lock` where possible
- use package-local paths
- set `PYTHONHASHSEED` or model seeds when relevant
- avoid notebook-only execution paths for submitted exhibits

For mixed stacks:

- define one top-level run order
- document whether R calls Python, Python calls R, or shell orchestrates both
- ensure both locks are included or justify omissions

## Metadata files

`EXHIBIT_CROSSWALK.csv` minimum columns:

```text
exhibit_id,manuscript_label,canonical_output,wrapper_script,input_dataset,runtime,source_script,claim_id,notes
```

`MANIFEST.csv` minimum columns:

```text
path,role,size_bytes,sha256,created_by,notes
```

`HASHES.sha256` should be generated from the final packaged files after self-test.

## Failure rules

Stop and return to Phase 3 or Phase 4 if:

- accepted result cannot be traced to code
- accepted exhibit cannot be rebuilt
- packaged data do not match live results
- replication changes the reported estimate
- restricted-data limits require a new disclosure decision
- environment lock cannot be produced and no fallback is documented

## Handoff packet

At the end of Phase 6, replication-builder should produce a handoff packet with:

- package root path
- zip path if created
- self-test commands and results
- manifest path
- hash file path
- unresolved restrictions
- upload readiness status
- decision needed before Zenodo, OpenICPSR, journal upload, or public release
