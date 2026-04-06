"""
This module provides access to image buffer types.

[NOTE]
Image buffer is also the structure used by bpy.types.Image
ID type to store and manipulate image data at runtime.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class ImBuf:
    channels: int
    """ Number of bit-planes."""

    filepath: str
    """ filepath associated with this image."""

    planes: int
    """ Number of bits associated with this image."""

    ppm: typing.Any
    """ pixels per meter."""

    size: typing.Any
    """ size of the image in pixels."""

    def copy(self) -> typing_extensions.Self:
        """

        :return: A copy of the image.
        """

    def crop(self, min: tuple[int, int], max: tuple[int, int]) -> None:
        """Crop the image.

        :param min: X, Y minimum.
        :param max: X, Y maximum.
        """

    def free(self) -> None:
        """Clear image data immediately (causing an error on re-use)."""

    def resize(self, size: tuple[int, int], method: str = "FAST") -> None:
        """Resize the image.

        :param size: New size.
        :param method: Method of resizing (FAST, BILINEAR)
        """
