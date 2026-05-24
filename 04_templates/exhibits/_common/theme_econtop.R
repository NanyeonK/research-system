# Common exhibit theme for research-system v2.
# Use from type-specific R scripts with:
# source("04_templates/exhibits/_common/theme_econtop.R")

suppressPackageStartupMessages({
  library(ggplot2)
})

rs_okabe_ito <- c(
  orange = "#E69F00",
  sky = "#56B4E9",
  green = "#009E73",
  yellow = "#F0E442",
  blue = "#0072B2",
  vermillion = "#D55E00",
  purple = "#CC79A7",
  black = "#000000"
)

rs_theme <- function(base_size = 10) {
  theme_minimal(base_size = base_size) +
    theme(
      text = element_text(family = "sans"),
      plot.title = element_text(face = "bold", size = base_size + 1),
      plot.subtitle = element_text(size = base_size),
      plot.caption = element_text(size = base_size - 2, hjust = 0),
      axis.title = element_text(size = base_size),
      axis.text = element_text(size = base_size - 1),
      panel.grid.minor = element_blank(),
      legend.position = "bottom",
      legend.title = element_blank()
    )
}

rs_save_figure <- function(plot, output_path, width = 6.5, height = 4.2) {
  dir.create(dirname(output_path), recursive = TRUE, showWarnings = FALSE)
  ggsave(output_path, plot = plot, width = width, height = height, dpi = 300, bg = "white")
}

rs_placeholder_data <- function(data_path) {
  if (identical(data_path, "<data_path>") || !file.exists(data_path)) {
    stop("Replace <data_path> with a project data file before running this exhibit template.", call. = FALSE)
  }
  read.csv(data_path)
}

rs_table_note <- function(dv = "MISSING", sample = "MISSING", source = "MISSING", inference = "MISSING") {
  paste0(
    "Notes: dv=", dv,
    "; sample=", sample,
    "; inference=", inference,
    "; source=", source
  )
}
