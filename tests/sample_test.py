"""A sample test file for the package."""

import rf_metric


def test_add() -> None:
    """Test the `add` function."""
    assert rf_metric.add(1, 2) == 3
    assert rf_metric.add(-1, 1) == 0
    assert rf_metric.add(0, 0) == 0
    assert rf_metric.add(-5, -5) == -10
    assert rf_metric.add(100, 200) == 300
