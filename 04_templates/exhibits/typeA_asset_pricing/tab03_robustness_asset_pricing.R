# Table 3 robustness template for Empirical asset pricing.
# Replace <data_path>, robustness variables, and fixed effects before running.

suppressPackageStartupMessages({
  library(fixest)
  library(modelsummary)
  library(ggplot2)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("portfolio_return", "factor_exposure")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

m1 <- feols(portfolio_return ~ factor_exposure, data = df)
# Add approved robustness models only after specs/output_spec.md permits them.
models <- list("Main" = m1)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
modelsummary(
  models,
  output = "output/tables/tab03_robustness_asset_pricing.html",
  notes = rs_table_note(dv = "excess return", sample = "<sample>", source = "<source_script>", inference = "<se_type>")
)
