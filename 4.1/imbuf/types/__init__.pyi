"""
This module provides access to image buffer types.

[NOTE]
Image buffer is also the structure used by bpy.types.Image
ID type to store and manipulate image data at runtime.

"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class ImBuf:
    channels: int
    """ Number of bit-planes.

    :type: int
    """

    filepath: str
    """ filepath associated with this image.

    :type: str
    """

    planes: int
    """ Number of bits associated with this image.

    :type: int
    """

    ppm: typing.Any
    """ pixels per meter."""

    size: typing.Any
    """ size of the image in pixels."""

    def copy(self) -> ImBuf:
        """

        :return: A copy of the image.
        :rtype: ImBuf
        """
        ...

    def crop(self, min, max):
        """Crop the image.

        :param min: X, Y minimum.
        :param max: X, Y maximum.
        """
        ...

    def free(self):
        """Clear image data immediately (causing an error on re-use)."""
        ...

    def resize(self, size, method: str = "FAST"):
        """Resize the image.

        :param size: New size.
        :param method: Method of resizing ('FAST', 'BILINEAR')
        :type method: str
        """
        ...
