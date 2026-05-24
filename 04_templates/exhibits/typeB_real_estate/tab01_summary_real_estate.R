# Table 1 summary template for Real estate empirics.
# Replace <data_path> and column placeholders before running.

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

summary_df <- data.frame(
  variable = c("rent_growth", "treatment_intensity"),
  n = c(sum(!is.na(df$rent_growth)), sum(!is.na(df$treatment_intensity))),
  mean = c(mean(df$rent_growth, na.rm = TRUE), mean(df$treatment_intensity, na.rm = TRUE)),
  sd = c(sd(df$rent_growth, na.rm = TRUE), sd(df$treatment_intensity, na.rm = TRUE)),
  min = c(min(df$rent_growth, na.rm = TRUE), min(df$treatment_intensity, na.rm = TRUE)),
  max = c(max(df$rent_growth, na.rm = TRUE), max(df$treatment_intensity, na.rm = TRUE))
)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
write.csv(summary_df, "output/tables/tab01_summary_real_estate.csv", row.names = FALSE)
cat(rs_table_note(dv = "rent outcome", sample = "<sample>", source = "<source_script>", inference = "summary statistics"), "
")
