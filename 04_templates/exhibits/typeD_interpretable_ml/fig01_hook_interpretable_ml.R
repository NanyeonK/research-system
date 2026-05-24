# Figure 1 hook template for Interpretable ML in finance.
# Replace <data_path> and column placeholders before running.

suppressPackageStartupMessages({
  library(ggplot2)
  library(fixest)
  library(modelsummary)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("feature_rank", "importance", "model")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

p <- ggplot(df, aes(x = feature_rank, y = importance, color = model)) +
  geom_line(linewidth = 0.8, alpha = 0.9) +
  geom_point(size = 1.4, alpha = 0.8) +
  scale_color_manual(values = rep(rs_okabe_ito, length.out = length(unique(df$model)))) +
  labs(
    title = "Figure 1. Hook for Interpretable ML in finance",
    subtitle = "Replace placeholder columns with the project-specific hook design.",
    x = "feature_rank",
    y = "importance",
    caption = "Source: <source_script>. Claim: <one_sentence_claim>."
  ) +
  rs_theme()

rs_save_figure(p, "output/figures/fig01_hook_interpretable_ml.png")
