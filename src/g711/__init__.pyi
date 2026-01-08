from pathlib import Path

import numpy as np
import numpy.typing as npt

def decode_alaw(encoded_bts: bytes) -> npt.NDArray[np.float32]:
    """Decode the specified A-Law encoded bytes object."""

def decode_ulaw(encoded_bts: bytes) -> npt.NDArray[np.float32]:
    """Decode the specified u-Law encoded bytes object."""

def encode_alaw(audio_data: npt.NDArray[np.float32]) -> bytes:
    """Encode the specified audio array to A-Law bytes."""

def encode_ulaw(audio_data: npt.NDArray[np.float32]) -> bytes:
    """Encode the specified audio array to u-Law bytes."""

def load_alaw(path: str | Path) -> npt.NDArray[np.float32]:
    """Load and decode the specified A-Law encoded audio file."""

def load_ulaw(path: str | Path) -> npt.NDArray[np.float32]:
    """Load and decode the specified u-Law encoded audio file."""

def save_alaw(path: str | Path, audio_data: npt.NDArray[np.float32]) -> bool:
    """Encode to A-Law and save the specified audio array."""

def save_ulaw(path: str | Path, audio_data: npt.NDArray[np.float32]) -> bool:
    """Encode to u-Law and save the specified audio array."""
