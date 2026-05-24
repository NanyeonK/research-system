# Exhibit Templates

These templates provide v2 exhibit shells by research type. They are not result generators. Replace placeholder data paths and columns inside a live project after the relevant specs and output mapping are locked.

Common files:

- `_common/theme_econtop.R` defines a shared R theme, color palette, save helper, and placeholder data guard.
- `_common/captions/caption_style.md` defines caption metadata requirements.

Type folders:

- `typeA_asset_pricing/`
- `typeB_real_estate/`
- `typeC_forecasting/`
- `typeD_interpretable_ml/`
- `typeE_conceptual/`

Each type includes:

- `fig01_hook_<type>.R`
- `tab01_summary_<type>.R`
- `tab02_main_<type>.R`
- `tab03_robustness_<type>.R`

Type D also includes Python matplotlib mirrors under `typeD_interpretable_ml/python/`.

Rules:

- Do not fake outputs.
- Do not run templates until `<data_path>` is replaced in a project copy.
- Keep Figure 1 hook candidates tied to Human Gate 2.
- Keep every table tied to `specs/output_spec.md` and `qa/claim_verification_matrix.md`.
