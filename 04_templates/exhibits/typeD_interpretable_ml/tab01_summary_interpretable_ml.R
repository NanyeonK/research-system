# Table 1 summary template for Interpretable ML in finance.
# Replace <data_path> and column placeholders before running.

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

summary_df <- data.frame(
  variable = c("importance", "prediction_score"),
  n = c(sum(!is.na(df$importance)), sum(!is.na(df$prediction_score))),
  mean = c(mean(df$importance, na.rm = TRUE), mean(df$prediction_score, na.rm = TRUE)),
  sd = c(sd(df$importance, na.rm = TRUE), sd(df$prediction_score, na.rm = TRUE)),
  min = c(min(df$importance, na.rm = TRUE), min(df$prediction_score, na.rm = TRUE)),
  max = c(max(df$importance, na.rm = TRUE), max(df$prediction_score, na.rm = TRUE))
)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
write.csv(summary_df, "output/tables/tab01_summary_interpretable_ml.csv", row.names = FALSE)
cat(rs_table_note(dv = "prediction target", sample = "<sample>", source = "<source_script>", inference = "summary statistics"), "
")
