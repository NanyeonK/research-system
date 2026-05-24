# Table 1 summary template for Empirical asset pricing.
# Replace <data_path> and column placeholders before running.

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

summary_df <- data.frame(
  variable = c("portfolio_return", "factor_exposure"),
  n = c(sum(!is.na(df$portfolio_return)), sum(!is.na(df$factor_exposure))),
  mean = c(mean(df$portfolio_return, na.rm = TRUE), mean(df$factor_exposure, na.rm = TRUE)),
  sd = c(sd(df$portfolio_return, na.rm = TRUE), sd(df$factor_exposure, na.rm = TRUE)),
  min = c(min(df$portfolio_return, na.rm = TRUE), min(df$factor_exposure, na.rm = TRUE)),
  max = c(max(df$portfolio_return, na.rm = TRUE), max(df$factor_exposure, na.rm = TRUE))
)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
write.csv(summary_df, "output/tables/tab01_summary_asset_pricing.csv", row.names = FALSE)
cat(rs_table_note(dv = "excess return", sample = "<sample>", source = "<source_script>", inference = "summary statistics"), "
")
