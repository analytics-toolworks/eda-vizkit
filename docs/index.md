# eda-vizkit

<img
src="https://raw.githubusercontent.com/analytics-toolworks/eda-vizkit/main/docs/images/profile.png"
alt="profile logo"
width="110">

`eda-vizkit` provides small, reusable visualization utilities for inspecting,
comparing, and explaining trained machine-learning models and completed
experiments.

It is designed for analysts who want clear, consistent visual evidence without
rewriting common plotting mechanics for every project.

## Purpose

Applied machine-learning work repeatedly uses the same kinds of visualizations:

- decision boundaries
- confusion matrices
- prediction errors
- class distributions
- actual-versus-predicted plots
- residual plots
- feature importance
- train/test splits
- model comparisons
- split comparisons

`eda-vizkit` provides concise functions for these common views so analysts can
spend more time interpreting models and experimental results.

## Design

`eda-vizkit` follows a small set of design rules:

- work with already-trained models, predictions, and completed experiment results
- do not train models or choose models, features, metrics, or experimental settings
- use established Python visualization and machine-learning libraries underneath
- return Matplotlib `Axes` objects rather than rendering automatically
- keep visualizations inspectable, adaptable, and easy to replace
- automate plotting mechanics without reducing analytical agency

The caller retains control over display, composition, annotation, export, and
interactive use.

## Example

```python
from eda_vizkit import show_decision_boundary

ax = show_decision_boundary(
    model,
    X_test,
    y_test,
)

ax.set_title("Penguin Species Decision Boundary")
```

## See Also

- [API](./api.md)
