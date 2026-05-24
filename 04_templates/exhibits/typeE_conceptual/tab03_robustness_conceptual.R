# Table 3 robustness template for Conceptual or institutional.
# Replace <data_path>, robustness variables, and fixed effects before running.

suppressPackageStartupMessages({
  library(fixest)
  library(modelsummary)
  library(ggplot2)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("friction_score", "design_index")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

m1 <- feols(friction_score ~ design_index, data = df)
# Add approved robustness models only after specs/output_spec.md permits them.
models <- list("Main" = m1)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
modelsummary(
  models,
  output = "output/tables/tab03_robustness_conceptual.html",
  notes = rs_table_note(dv = "institutional outcome", sample = "<sample>", source = "<source_script>", inference = "<se_type>")
)
