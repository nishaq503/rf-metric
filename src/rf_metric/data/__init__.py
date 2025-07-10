"""Handling the dataset."""

import enum
import pathlib
import typing

import h5py
import numpy

from .. import utils


class NoiseLevel(str, enum.Enum):
    """Enum for noise levels in the RF dataset."""

    NEG_20 = "-20dB"
    NEG_18 = "-18dB"
    NEG_16 = "-16dB"
    NEG_14 = "-14dB"
    NEG_12 = "-12dB"
    NEG_10 = "-10dB"
    NEG_8 = "-8dB"
    NEG_6 = "-6dB"
    NEG_4 = "-4dB"
    NEG_2 = "-2dB"
    ZERO = "0dB"
    POS_2 = "+2dB"
    POS_4 = "+4dB"
    POS_6 = "+6dB"
    POS_8 = "+8dB"
    POS_10 = "+10dB"
    POS_12 = "+12dB"
    POS_14 = "+14dB"
    POS_16 = "+16dB"
    POS_18 = "+18dB"
    POS_20 = "+20dB"
    POS_22 = "+22dB"
    POS_24 = "+24dB"
    POS_26 = "+26dB"
    POS_28 = "+28dB"
    POS_30 = "+30dB"

    @classmethod
    def all_levels(cls) -> typing.Iterator["NoiseLevel"]:
        """Iterate over all noise levels."""
        return iter(cls.__members__.values())


class ModulationMode(str, enum.Enum):
    """Enum for modulation modes in the RF dataset."""

    APSK_128 = "128APSK"
    QAM_128 = "128QAM"
    APSK_16 = "16APSK"
    PSK_16 = "16PSK"
    QAM_16 = "16QAM"
    QAM_256 = "256QAM"
    APSK_32 = "32APSK"
    PSK_32 = "32PSK"
    QAM_32 = "32QAM"
    ASK_4 = "4ASK"
    APSK_64 = "64APSK"
    QAM_64 = "64QAM"
    ASK_8 = "8ASK"
    PSK_8 = "8PSK"
    AM_DSB_SC = "AM-DSB-SC"
    AM_DSB_WC = "AM-DSB-WC"
    AM_SSB_SC = "AM-SSB-SC"
    AM_SSB_WC = "AM-SSB-WC"
    BPSK = "BPSK"
    FM = "FM"
    GMSK = "GMSK"
    OOK = "OOK"
    OQPSK = "OQPSK"
    QPSK = "QPSK"

    def read(
        self,
        data_dir: pathlib.Path | None = None,
        noise_level: NoiseLevel | None = None,
    ) -> numpy.typing.ArrayLike | dict[NoiseLevel, numpy.typing.ArrayLike]:
        """Read part of the dataset corresponding to this modulation mode.

        Args:
            data_dir: Path to the directory containing the `h5` datasets. If `None`, uses the data directory from an environment variable.
            noise_level: Noise level to filter the dataset. If `None`, all noise levels are included.

        Returns:
            If a noise level is specified, returns a numpy array of the dataset for that noise level.
            Otherwise, returns a dictionary mapping noise levels to numpy arrays.

        Raises:
            FileNotFoundError:
                - If the data directory does not exist.
                - If the dataset file for the specified modulation mode does not exist.
        """
        if data_dir is None:
            data_dir = pathlib.Path(utils.config["RF_DATA_DIR"]).resolve()  # type: ignore

        if not data_dir.exists():
            raise FileNotFoundError(f"Data directory {data_dir} does not exist.")

        file_path = data_dir / f"mod_{self.value}.h5"
        if not file_path.exists():
            raise FileNotFoundError(f"Dataset file {file_path} does not exist.")

        print(f"Reading dataset from {file_path}")
        with h5py.File(file_path, "r") as file:  # type: ignore[call-arg,arg-type]
            print(f"Opened dataset file {file_path}")
            print(f"Available keys: {list(file.keys())}")
            data_x = numpy.asarray(file["X"])
            # data_y = file["Y"]
            # data_z = file["Z"]

        if noise_level is None:
            datasets: dict[NoiseLevel, numpy.typing.ArrayLike] = {}
            print("Reading all noise levels...")
            for i, nl in enumerate(NoiseLevel.all_levels()):
                start = i * 4096  # There are 4096 samples per noise level
                stop = start + 4096
                datasets[nl] = data_x[start:stop, ...]
            return datasets

        else:
            print(f"Reading dataset for noise level {noise_level}...")
            i = list(NoiseLevel.all_levels()).index(noise_level)
            start = i * 4096  # There are 4096 samples per noise level
            stop = start + 4096
            return data_x[start:stop, ...]


__all__ = [
    "NoiseLevel",
    "ModulationMode",
]
