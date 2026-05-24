# Table 1 summary template for Conceptual or institutional.
# Replace <data_path> and column placeholders before running.

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

summary_df <- data.frame(
  variable = c("friction_score", "design_index"),
  n = c(sum(!is.na(df$friction_score)), sum(!is.na(df$design_index))),
  mean = c(mean(df$friction_score, na.rm = TRUE), mean(df$design_index, na.rm = TRUE)),
  sd = c(sd(df$friction_score, na.rm = TRUE), sd(df$design_index, na.rm = TRUE)),
  min = c(min(df$friction_score, na.rm = TRUE), min(df$design_index, na.rm = TRUE)),
  max = c(max(df$friction_score, na.rm = TRUE), max(df$design_index, na.rm = TRUE))
)

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)
write.csv(summary_df, "output/tables/tab01_summary_conceptual.csv", row.names = FALSE)
cat(rs_table_note(dv = "institutional outcome", sample = "<sample>", source = "<source_script>", inference = "summary statistics"), "
")
