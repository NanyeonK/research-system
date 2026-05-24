# Table 2 main estimate template for Real estate empirics.
# Replace <data_path>, controls, and fixed effects before running.

suppressPackageStartupMessages({
  library(fixest)
  library(modelsummary)
  library(ggplot2)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("rent_growth", "treatment_intensity")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

m1 <- feols(rent_growth ~ treatment_intensity, data = df)
models <- list("Baseline" = m1)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
modelsummary(
  models,
  output = "output/tables/tab02_main_real_estate.html",
  notes = rs_table_note(dv = "rent outcome", sample = "<sample>", source = "<source_script>", inference = "<se_type>")
)
