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
    """ Number of color channels."""

    filepath: str
    """ Filepath associated with this image."""

    planes: int
    """ Number of bits per pixel."""

    ppm: tuple[float, float]
    """ Pixels per meter."""

    size: tuple[int, int]
    """ Size of the image in pixels."""

    def copy(self) -> typing_extensions.Self:
        """Return a copy of the image.

        :return: A copy of the image.
        """

    def crop(self, min: tuple[int, int], max: tuple[int, int]) -> None:
        """Crop the image in-place.

        :param min: Minimum pixel coordinates (X, Y), inclusive.
        :param max: Maximum pixel coordinates (X, Y), inclusive.
        """

    def free(self) -> None:
        """Clear image data immediately (causing an error on re-use)."""

    def resize(self, size: tuple[int, int], *, method: str = "FAST") -> None:
        """Resize the image in-place.

        :param size: New size.
        :param method: Method of resizing (FAST, BILINEAR).
        """
