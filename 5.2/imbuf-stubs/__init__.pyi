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

def file_type_from_buffer(buffer) -> imbuf.types.ImBufFileType:
    """Detect the image file type from a buffer.

    :param buffer: A buffer containing image data.
    :return: The detected file type, or None if unrecognized.
    """

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

def new(
    size: tuple[int, int],
    *,
    planes: typing.Literal[8, 16, 24, 32] = 32,
    buffer_type: typing.Literal["BYTE", "FLOAT"] = "BYTE",
) -> imbuf.types.ImBuf:
    """Create a new image.

    :param size: The size of the image in pixels.
    :param planes: Number of bits per pixel.
    :param buffer_type: The buffer type.
    :return: The newly created image.
    """

def write(
    image: imbuf.types.ImBuf, *, filepath: None | bytes | str | None = None
) -> None:
    """Write an image.

    :param image: The image to write.
    :param filepath: Optional filepath of the image (fallback to the images file path).
    """

def write_to_buffer(image: imbuf.types.ImBuf, file) -> None:
    """Write an image to a file-like object.

    :param image: The image to write.
    :param file: A writable file-like object (e.g. `io.BytesIO`).
    """
