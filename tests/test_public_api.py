r"""Smoke tests for the public return-value contract."""

import matplotlib

matplotlib.use("Agg")

from matplotlib.axes import Axes
import matplotlib.pyplot as plt
import pandas as pd

from eda_vizkit import (
    show_categorical_distribution,
    show_missing_values,
    show_numeric_by_category,
    show_numeric_distribution,
    show_numeric_relationship,
)


def make_test_data() -> pd.DataFrame:
    """Return a small DataFrame for visualization tests."""

    return pd.DataFrame(
        {
            "species": [
                "Adelie",
                "Adelie",
                "Gentoo",
                "Gentoo",
                "Chinstrap",
            ],
            "flipper_length_mm": [
                181.0,
                186.0,
                211.0,
                217.0,
                195.0,
            ],
            "body_mass_g": [
                3750.0,
                3800.0,
                5000.0,
                5200.0,
                4100.0,
            ],
            "sex": [
                "Male",
                "Female",
                "Male",
                None,
                "Female",
            ],
        }
    )


def test_distribution_helpers_return_axes() -> None:
    """Distribution helpers return Axes objects."""

    df = make_test_data()

    assert isinstance(
        show_numeric_distribution(
            df,
            column="body_mass_g",
        ),
        Axes,
    )

    assert isinstance(
        show_categorical_distribution(
            df,
            column="species",
        ),
        Axes,
    )

    plt.close("all")


def test_relationship_helpers_return_axes() -> None:
    """Relationship helpers return Axes objects."""

    df = make_test_data()

    assert isinstance(
        show_numeric_relationship(
            df,
            x="flipper_length_mm",
            y="body_mass_g",
        ),
        Axes,
    )

    assert isinstance(
        show_numeric_by_category(
            df,
            numeric="body_mass_g",
            category="species",
        ),
        Axes,
    )

    plt.close("all")


def test_quality_helper_returns_axes() -> None:
    """Quality helper returns an Axes object."""

    df = make_test_data()

    assert isinstance(
        show_missing_values(df),
        Axes,
    )

    plt.close("all")


def test_helpers_accept_existing_axes() -> None:
    """Helpers can draw on caller-provided Axes objects."""

    df = make_test_data()

    _, ax = plt.subplots()

    result = show_numeric_distribution(
        df,
        column="body_mass_g",
        ax=ax,
    )

    assert result is ax

    plt.close("all")
