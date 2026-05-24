# Figure 1 hook template for Forecasting.
# Replace <data_path> and column placeholders before running.

suppressPackageStartupMessages({
  library(ggplot2)
  library(fixest)
  library(modelsummary)
})
source("04_templates/exhibits/_common/theme_econtop.R")

data_path <- "<data_path>"
df <- rs_placeholder_data(data_path)

required <- c("forecast_horizon", "loss_difference", "model")
missing <- setdiff(required, names(df))
if (length(missing) > 0) stop(paste("Missing columns:", paste(missing, collapse = ", ")), call. = FALSE)

p <- ggplot(df, aes(x = forecast_horizon, y = loss_difference, color = model)) +
  geom_line(linewidth = 0.8, alpha = 0.9) +
  geom_point(size = 1.4, alpha = 0.8) +
  scale_color_manual(values = rep(rs_okabe_ito, length.out = length(unique(df$model)))) +
  labs(
    title = "Figure 1. Hook for Forecasting",
    subtitle = "Replace placeholder columns with the project-specific hook design.",
    x = "forecast_horizon",
    y = "loss_difference",
    caption = "Source: <source_script>. Claim: <one_sentence_claim>."
  ) +
  rs_theme()

rs_save_figure(p, "output/figures/fig01_hook_forecasting.png")
