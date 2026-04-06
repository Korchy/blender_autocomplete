"""
This module provides access to selection.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def load_id(id) -> None:
    """Set the selection ID.

    :param id: Number (32-bit uint).
    """
