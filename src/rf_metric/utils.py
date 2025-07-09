"""Utilities for the package."""

import pathlib

from dotenv import dotenv_values

config = dotenv_values(pathlib.Path(__file__).resolve().parents[2] / ".env")

__all__ = [
    "config",
]
