# Figure 1 hook template for Empirical asset pricing.
# Replace <data_path> and column placeholders before running.

suppressPackageStartupMessages({
  library(ggplot2)
  library(fixest)
  library(modelsummary)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("month", "portfolio_return", "portfolio")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

p <- ggplot(df, aes(x = month, y = portfolio_return, color = portfolio)) +
  geom_line(linewidth = 0.8, alpha = 0.9) +
  geom_point(size = 1.4, alpha = 0.8) +
  scale_color_manual(values = rep(rs_okabe_ito, length.out = length(unique(df$portfolio)))) +
  labs(
    title = "Figure 1. Hook for Empirical asset pricing",
    subtitle = "Replace placeholder columns with the project-specific hook design.",
    x = "month",
    y = "portfolio_return",
    caption = "Source: <source_script>. Claim: <one_sentence_claim>."
  ) +
  rs_theme()

rs_save_figure(p, "output/figures/fig01_hook_asset_pricing.png")
