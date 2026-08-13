"""
This module provides access to Blender's image manipulation API.

It provides access to image buffers outside of Blender's
bpy.types.Image data-block context.

imbuf.types.rst

:maxdepth: 1
:caption: Submodules

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import imbuf.types

from . import types as types

def load(filepath: bytes | str) -> imbuf.types.ImBuf:
    """Load an image from a file.

    :param filepath: The filepath of the image.
    :return: The newly loaded image.
    """

def load_from_buffer(buffer) -> imbuf.types.ImBuf:
    """Load an image from a buffer.

    :param buffer: A buffer containing the image data.
    :return: The newly loaded image.
    """

def new(size: tuple[int, int]) -> imbuf.types.ImBuf:
    """Create a new image.

    :param size: The size of the image in pixels.
    :return: The newly created image.
    """

def write(
    image: imbuf.types.ImBuf, *, filepath: None | bytes | str | None = None
) -> None:
    """Write an image.

    :param image: The image to write.
    :param filepath: Optional filepath of the image (fallback to the images file path).
    """
