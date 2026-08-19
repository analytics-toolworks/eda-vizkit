r"""Data-quality visualizations for exploratory data analysis."""

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd


def show_missing_values(
    df: pd.DataFrame,
    *,
    ax: Axes | None = None,
) -> Axes:
    """Show missing-value counts for DataFrame columns."""
    if ax is None:
        _, ax = plt.subplots()

    missing = df.isna().sum()
    missing = missing[missing > 0].sort_values(ascending=False)

    if missing.empty:
        ax.text(
            0.5,
            0.5,
            "No missing values",
            ha="center",
            va="center",
            transform=ax.transAxes,
        )
        ax.set_title("Missing values")
        ax.set_axis_off()

        return ax

    ax.bar(
        missing.index,
        missing.to_numpy(),
    )

    ax.set_title("Missing values")
    ax.set_xlabel("Variable")
    ax.set_ylabel("Missing count")
    ax.tick_params(axis="x", labelrotation=45)

    return ax
