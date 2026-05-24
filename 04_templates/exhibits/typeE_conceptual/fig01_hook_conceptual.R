# Figure 1 hook template for Conceptual or institutional.
# Replace <data_path> and column placeholders before running.

suppressPackageStartupMessages({
  library(ggplot2)
  library(fixest)
  library(modelsummary)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("stage", "friction_score", "institutional_design")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

p <- ggplot(df, aes(x = stage, y = friction_score, color = institutional_design)) +
  geom_line(linewidth = 0.8, alpha = 0.9) +
  geom_point(size = 1.4, alpha = 0.8) +
  scale_color_manual(values = rep(rs_okabe_ito, length.out = length(unique(df$institutional_design)))) +
  labs(
    title = "Figure 1. Hook for Conceptual or institutional",
    subtitle = "Replace placeholder columns with the project-specific hook design.",
    x = "stage",
    y = "friction_score",
    caption = "Source: <source_script>. Claim: <one_sentence_claim>."
  ) +
  rs_theme()

rs_save_figure(p, "output/figures/fig01_hook_conceptual.png")
