# Table 2 main estimate template for Interpretable ML in finance.
# Replace <data_path>, controls, and fixed effects before running.

suppressPackageStartupMessages({
  library(fixest)
  library(modelsummary)
  library(ggplot2)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("importance", "prediction_score")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

m1 <- feols(importance ~ prediction_score, data = df)
models <- list("Baseline" = m1)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
modelsummary(
  models,
  output = "output/tables/tab02_main_interpretable_ml.html",
  notes = rs_table_note(dv = "prediction target", sample = "<sample>", source = "<source_script>", inference = "<se_type>")
)
