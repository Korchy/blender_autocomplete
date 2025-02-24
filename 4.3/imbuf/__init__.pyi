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
import imbuf.types

from . import types as types

def load(filepath: bytes | str) -> imbuf.types.ImBuf:
    """Load an image from a file.

    :param filepath: the filepath of the image.
    :type filepath: bytes | str
    :return: the newly loaded image.
    :rtype: imbuf.types.ImBuf
    """

def new(size: tuple[int, int]) -> imbuf.types.ImBuf:
    """Load a new image.

    :param size: The size of the image in pixels.
    :type size: tuple[int, int]
    :return: the newly loaded image.
    :rtype: imbuf.types.ImBuf
    """

def write(image: imbuf.types.ImBuf, filepath: None | bytes | str = image.filepath):
    """Write an image.

    :param image: the image to write.
    :type image: imbuf.types.ImBuf
    :param filepath: Optional filepath of the image (fallback to the images file path).
    :type filepath: None | bytes | str
    """
