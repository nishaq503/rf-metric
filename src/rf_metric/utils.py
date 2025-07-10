"""Utilities for the package."""

import logging
import pathlib

from dotenv import dotenv_values

config = dotenv_values(pathlib.Path(__file__).resolve().parents[2] / ".env")


def make_logger(name: str, level: str | None = None) -> logging.Logger:
    """Create a logger with the specified name and level."""
    logger = logging.getLogger(name)
    if level is not None:
        logger.setLevel(level)
    else:
        logger.setLevel(logging.INFO)

    return logger


__all__ = [
    "config",
    "make_logger",
]
