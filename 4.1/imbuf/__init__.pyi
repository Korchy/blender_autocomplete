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
import imbuf.types

from . import types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def load(filepath: bytes | str) -> imbuf.types.ImBuf:
    """Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: bytes | str
    :return: the newly loaded image.
    :rtype: imbuf.types.ImBuf
    """

    ...

def new(size) -> imbuf.types.ImBuf:
    """Load a new image.

    :param size: The size of the image in pixels.
    :return: the newly loaded image.
    :rtype: imbuf.types.ImBuf
    """

    ...

def write(image: imbuf.types.ImBuf, filepath: bytes | str | None = None):
    """Write an image.

    :param image: the image to write.
    :type image: imbuf.types.ImBuf
    :param filepath: Optional filepath of the image (fallback to the images file path).
    :type filepath: bytes | str | None
    """

    ...
