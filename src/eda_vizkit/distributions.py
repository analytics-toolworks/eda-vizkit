r"""Distribution visualizations for exploratory data analysis."""

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd

from eda_vizkit._validation import (
    require_columns,
    require_numeric_column,
)


def show_numeric_distribution(
    df: pd.DataFrame,
    *,
    column: str,
    bins: int = 20,
    ax: Axes | None = None,
) -> Axes:
    """Show the distribution of one numeric variable."""
    require_numeric_column(df, column=column)

    if bins < 1:
        raise ValueError("bins must be at least 1")

    if ax is None:
        _, ax = plt.subplots()

    values = df[column].dropna()

    ax.hist(values, bins=bins)
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")

    return ax


def show_categorical_distribution(
    df: pd.DataFrame,
    *,
    column: str,
    ax: Axes | None = None,
) -> Axes:
    """Show category frequencies for one categorical variable."""
    require_columns(df, columns=[column])

    if ax is None:
        _, ax = plt.subplots()

    counts = df[column].value_counts(dropna=False)

    labels = ["<missing>" if pd.isna(value) else str(value) for value in counts.index]

    ax.bar(labels, counts.to_numpy())
    ax.set_title(f"Distribution of {column}")
    ax.set_xlabel(column)
    ax.set_ylabel("Count")
    ax.tick_params(axis="x", labelrotation=45)

    return ax
