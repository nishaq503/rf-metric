"""The root of the package."""

from . import data, utils


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def main() -> None:
    print("Hello from rf-metric!")
    print("Configuration:")
    for var, val in utils.config.items():
        print(f"  {var}: {val}")


__all__ = [
    "data",
    "utils",
    "add",
    "main",
]
