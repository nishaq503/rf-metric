"""Tests that the environment variables were read correctly."""

import pathlib

from rf_metric.utils import config  # type: ignore[import-not-found]


def test_config() -> None:
    """Test that the configuration is read correctly."""
    assert len(config) > 0, "Configuration should not be empty"
    assert "RF_DATA_DIR" in config, "RF_DATA_DIR should be in the configuration"

    rf_data_dir = pathlib.Path(config["RF_DATA_DIR"]).resolve()  # pyright: ignore[reportArgumentType]
    assert rf_data_dir.exists(), f"RF data directory {rf_data_dir} should exist"
    assert rf_data_dir.is_dir(), (
        f"RF data directory {rf_data_dir} should be a directory"
    )

    assert "LOG_LEVEL" in config, "LOG_LEVEL should be in the configuration"
    assert config["LOG_LEVEL"] in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"], (
        f"LOG_LEVEL should be one of DEBUG, INFO, WARNING, ERROR, CRITICAL, but got {config['LOG_LEVEL']}"
    )
