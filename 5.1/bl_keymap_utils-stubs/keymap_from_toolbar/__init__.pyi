import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def generate(context, space_type, *, use_fallback_keys=True, use_reset=True) -> None:
    """Keymap for popup toolbar, currently generated each time."""
