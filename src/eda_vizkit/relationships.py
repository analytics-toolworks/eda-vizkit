"""Relationship visualizations for exploratory data analysis."""

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd

from eda_vizkit._validation import (
    require_columns,
    require_numeric_column,
)


def show_numeric_relationship(
    df: pd.DataFrame,
    *,
    x: str,
    y: str,
    ax: Axes | None = None,
) -> Axes:
    """Show the relationship between two numeric variables.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        x (str): The name of the numeric column to be used as the x-axis.
        y (str): The name of the numeric column to be used as the y-axis.
        ax (Axes | None, optional): The matplotlib Axes object to plot on. If None, a new figure and axes will be created.

    Returns:
        Axes: The matplotlib Axes object containing the plot.
    """
    require_numeric_column(df, column=x)
    require_numeric_column(df, column=y)

    if ax is None:
        _, ax = plt.subplots()

    complete = df[[x, y]].dropna()

    ax.scatter(
        complete[x],
        complete[y],
    )

    ax.set_title(f"{y} by {x}")
    ax.set_xlabel(x)
    ax.set_ylabel(y)

    return ax


def show_numeric_by_category(
    df: pd.DataFrame,
    *,
    numeric: str,
    category: str,
    ax: Axes | None = None,
) -> Axes:
    """Show a numeric distribution across categories.

    Args:
        df (pd.DataFrame): The DataFrame containing the data.
        numeric (str): The name of the numeric column.
        category (str): The name of the categorical column.
        ax (Axes | None, optional): The matplotlib Axes object to plot on. If None, a new figure and axes will be created.

    Returns:
        Axes: The matplotlib Axes object containing the plot.
    """
    require_numeric_column(df, column=numeric)
    require_columns(df, columns=[category])

    if ax is None:
        _, ax = plt.subplots()

    complete = df[[category, numeric]].dropna()

    categories = list(complete[category].drop_duplicates())

    groups = [
        complete.loc[
            complete[category] == value,
            numeric,
        ].to_numpy()
        for value in categories
    ]

    ax.boxplot(
        groups,
        tick_labels=[str(value) for value in categories],
    )

    ax.set_title(f"{numeric} by {category}")
    ax.set_xlabel(category)
    ax.set_ylabel(numeric)

    return ax
