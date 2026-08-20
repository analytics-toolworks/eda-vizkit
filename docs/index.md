# eda-vizkit

<img
src="https://raw.githubusercontent.com/analytics-toolworks/eda-vizkit/main/docs/images/profile.png"
alt="profile logo"
width="110">

`eda-vizkit` provides small, reusable visualization utilities for exploratory
data analysis.

It is designed for analysts who want clear, consistent visual evidence without
rewriting common plotting mechanics for every project.

## Purpose

Exploratory data analysis repeatedly uses the same kinds of visualizations:

- numeric distributions
- categorical distributions
- numeric-to-numeric relationships
- numeric-by-category relationships
- missing-value summaries

`eda-vizkit` provides concise functions for these common views so analysts can
spend more time exploring and interpreting data.

## Design

`eda-vizkit` follows a small set of design rules:

- accept ordinary pandas DataFrames and explicit column names
- keep analytical choices visible to the caller
- return Matplotlib `Axes` objects
- never call `plt.show()`
- avoid dependencies on analytical workflow frameworks
- keep the implementation readable and replaceable

The caller retains control over display, composition, annotation, export, and
interactive use.

## Example

```python
from eda_vizkit import save_chart, show_numeric_relationship

ax = show_numeric_relationship(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
)

save_chart(
    ax,
    "docs/images/feature-target-scatter.png",
)
```

## See Also

- [API](./api.md)
