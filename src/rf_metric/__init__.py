"""The root of the package."""

import numpy

from . import data, utils


def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b


def main() -> None:
    print("Hello from rf-metric!")
    print("Configuration:")
    for var, val in utils.config.items():
        print(f"  {var}: {val}")

    mod_mode = data.ModulationMode.APSK_128
    mod_data = mod_mode.read()
    if isinstance(mod_data, dict):
        print(f"Modulation mode {mod_mode} data for all noise levels:")
        for noise_level, data_array in mod_data.items():
            data_array = numpy.asarray(data_array)
            print(f"  {noise_level.value}: {data_array.shape}")
    else:
        mod_data = numpy.asarray(mod_data)
        print(f"Modulation mode {mod_mode} data shape: {mod_data.shape}")


__all__ = [
    "data",
    "utils",
    "add",
    "main",
]
