"""
This module provides access to font drawing types.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class BLFImBufContext:
    """Context manager returned by `blf.bind_imbuf` that binds an image buffer
    as the destination for text drawing.
    """
