"""tab01_summary matplotlib template for Type D interpretable ML in finance.

Replace <data_path> and placeholder column names before running. This script uses
matplotlib styling consistent with the R templates.
"""

from __future__ import annotations

from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

OKABE_ITO = ["#E69F00", "#56B4E9", "#009E73", "#F0E442", "#0072B2", "#D55E00", "#CC79A7", "#000000"]


def load_data(path: str) -> pd.DataFrame:
    if path == "<data_path>" or not Path(path).exists():
        raise SystemExit("Replace <data_path> with a project data file before running this exhibit template.")
    return pd.read_csv(path)


def apply_style(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, axis="y", alpha=0.25)
    ax.figure.tight_layout()


def main() -> None:
    df = load_data("<data_path>")
    required = ["feature_rank", "importance", "model", "prediction_score"]
    missing = [c for c in required if c not in df.columns]
    if missing:
        raise SystemExit(f"Missing columns: {', '.join(missing)}")

    fig, ax = plt.subplots(figsize=(6.5, 4.2))
    for i, (name, part) in enumerate(df.groupby("model")):
        part = part.sort_values("feature_rank")
        ax.plot(part["feature_rank"], part["importance"], marker="o", linewidth=1.5, color=OKABE_ITO[i % len(OKABE_ITO)], label=str(name))
    ax.set_title("Type D tab01_summary: interpretable ML exhibit")
    ax.set_xlabel("feature_rank")
    ax.set_ylabel("importance")
    ax.legend(frameon=False, loc="best")
    apply_style(ax)
    out = Path("output/figures/typeD_tab01_summary.png")
    out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out, dpi=300, bbox_inches="tight", facecolor="white")


if __name__ == "__main__":
    main()
