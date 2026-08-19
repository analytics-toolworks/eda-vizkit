# EDA VizKit

[![PyPI](https://img.shields.io/pypi/v/eda-vizkit?logo=pypi&label=pypi)](https://pypi.org/project/eda-vizkit/)
[![Docs Site](https://img.shields.io/badge/docs-site-blue?logo=github)](https://analytics-toolworks.github.io/eda-vizkit/)
[![Python](https://img.shields.io/python/required-version-toml?tomlFilePath=https://raw.githubusercontent.com/analytics-toolworks/eda-vizkit/main/pyproject.toml&logo=python)](https://github.com/analytics-toolworks/eda-vizkit/blob/main/pyproject.toml)
![uv](https://img.shields.io/badge/uv-managed-DE5FE9)
[![CI Status](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/ci-python-zensical.yml)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

[![CI](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/ci-python-zensical.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/ci-python-zensical.yml)
[![Docs](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/deploy-zensical.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/deploy-zensical.yml)
[![Links](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/links.yml/badge.svg?branch=main)](https://github.com/analytics-toolworks/eda-vizkit/actions/workflows/links.yml)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-brightgreen.svg)](https://github.com/analytics-toolworks/eda-vizkit/security)

<img
src="https://raw.githubusercontent.com/analytics-toolworks/eda-vizkit/main/docs/images/profile.png"
alt="profile logo"
width="110">

> Reusable visualizations for inspecting and exploring data.

EDA VizKit provides high-level Python functions for common
exploratory data analysis visualizations.
The package works with ordinary pandas DataFrames and
returns Matplotlib `Axes` objects.

EDA VizKit does not clean data, classify variables, select relationships,
make analytical decisions, or interpret results.

## Design

- Accept ordinary pandas DataFrames and explicit column names.
- Provide reusable visualizations for common EDA tasks.
- Return Matplotlib `Axes` objects.
- Never call `plt.show()`.
- Keep analytical choices visible to the caller.
- Avoid dependencies on analytical workflow frameworks.
- Keep the implementation readable and replaceable.

## Install

```shell
uv add eda-vizkit
```

## Example

```python
from eda_vizkit import show_numeric_distribution

ax = show_numeric_distribution(
    df,
    column="body_mass_g",
)

ax.set_title("Penguin Body Mass")
```

The caller controls display and composition.
In a script, for example:

```python
import matplotlib.pyplot as plt

from eda_vizkit import show_numeric_distribution

ax = show_numeric_distribution(
    df,
    column="body_mass_g",
)

plt.show()
```

## Initial API

Distributions:

- `show_numeric_distribution()`
- `show_categorical_distribution()`

Relationships:

- `show_numeric_relationship()`
- `show_numeric_by_category()`

Data quality:

- `show_missing_values()`

## Public Contract

Every public visualization helper:

- accepts already-available data,
- keeps the analytical choice explicit,
- returns a Matplotlib `Axes` object,
- never calls `plt.show()`.

This allows the visualization helpers to work in
scripts, applications, notebooks, documentation, and
other presentation environments.

## Example: Numeric Distribution

```python
from eda_vizkit import show_numeric_distribution

ax = show_numeric_distribution(
    df,
    column="flipper_length_mm",
)
```

## Example: Categorical Distribution

```python
from eda_vizkit import show_categorical_distribution

ax = show_categorical_distribution(
    df,
    column="species",
)
```

## Example: Numeric Relationship

```python
from eda_vizkit import show_numeric_relationship

ax = show_numeric_relationship(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
)
```

## Example: Numeric Variable by Category

```python
from eda_vizkit import show_numeric_by_category

ax = show_numeric_by_category(
    df,
    numeric="body_mass_g",
    category="species",
)
```

## Example: Missing Values

```python
from eda_vizkit import show_missing_values

ax = show_missing_values(df)
```

## Developer Command Reference

<details>
<summary>Show command reference</summary>

### In a machine terminal

Open a machine terminal where you want the project:

```text
git clone https://github.com/analytics-toolworks/eda-vizkit

cd eda-vizkit
code .
```

### In a VS Code terminal

```text
uv self update
uv python pin 3.14
uv python install
uv lock --upgrade
uv sync

uv run pre-commit install
uv run pre-commit autoupdate

git add -A
uv run pre-commit run --all-files
# repeat if changes were made
uv run pre-commit run --all-files

# types, tests, docs
uv run ty check
uv run python -m pytest
uv run python -m zensical build

# save progress
git add -A
git commit -m "update"
git push -u origin main
```

</details>

## Documentation

- [Documentation](https://analytics-toolworks.github.io/eda-vizkit)

## Annotations

[.annotations/annotations.md](https://github.com/analytics-toolworks/eda-vizkit/blob/main/.annotations/annotations.md)

## Citation

[CITATION.cff](https://github.com/analytics-toolworks/eda-vizkit/blob/main/CITATION.cff)

## License

[MIT](https://github.com/analytics-toolworks/eda-vizkit/blob/main/LICENSE)
