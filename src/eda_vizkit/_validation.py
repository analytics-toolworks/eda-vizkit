"""Internal validation helpers for eda-vizkit."""

from collections.abc import Iterable

import pandas as pd


def require_columns(
    df: pd.DataFrame,
    *,
    columns: Iterable[str],
) -> None:
    """Raise ValueError if required DataFrame columns are missing.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        columns (Iterable[str]): The required column names.

    Raises:
        ValueError: If any of the required columns are missing.
    """
    required = tuple(columns)
    missing = [column for column in required if column not in df.columns]

    if missing:
        names = ", ".join(missing)
        raise ValueError(f"Missing required columns: {names}")


def require_numeric_column(
    df: pd.DataFrame,
    *,
    column: str,
) -> None:
    """Raise ValueError if a required column is not numeric.

    Args:
        df (pd.DataFrame): The DataFrame to check.
        column (str): The name of the required numeric column.

    Raises:
        ValueError: If the column is not numeric.
    """
    require_columns(df, columns=[column])

    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column must be numeric: {column}")
