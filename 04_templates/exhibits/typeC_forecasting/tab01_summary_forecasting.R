# Table 1 summary template for Forecasting.
# Replace <data_path> and column placeholders before running.

suppressPackageStartupMessages({
  library(fixest)
  library(modelsummary)
  library(ggplot2)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("loss_difference", "forecast_signal")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

summary_df <- data.frame(
  variable = c("loss_difference", "forecast_signal"),
  n = c(sum(!is.na(df$loss_difference)), sum(!is.na(df$forecast_signal))),
  mean = c(mean(df$loss_difference, na.rm = TRUE), mean(df$forecast_signal, na.rm = TRUE)),
  sd = c(sd(df$loss_difference, na.rm = TRUE), sd(df$forecast_signal, na.rm = TRUE)),
  min = c(min(df$loss_difference, na.rm = TRUE), min(df$forecast_signal, na.rm = TRUE)),
  max = c(max(df$loss_difference, na.rm = TRUE), max(df$forecast_signal, na.rm = TRUE))
)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
write.csv(summary_df, "output/tables/tab01_summary_forecasting.csv", row.names = FALSE)
cat(rs_table_note(dv = "forecast loss", sample = "<sample>", source = "<source_script>", inference = "summary statistics"), "
")
