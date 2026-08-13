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
    buffer_type: str
    """ Type of the image's pixel buffer ('BYTE' or 'FLOAT')."""

    channels: int
    """ Number of color channels."""

    compress: int
    """ Compression level for formats that support lossless compression levels (0 - 100, clamped)."""

    file_type: str
    """ The file type identifier."""

    filepath: bytes | str
    """ Filepath associated with this image."""

    planes: int
    """ Number of bits per pixel for the byte buffer.
Used when reading and writing image files."""

    ppm: tuple[float, float]
    """ Pixels per meter."""

    quality: int
    """ Quality for formats that support lossy compression (0 - 100, clamped)."""

    size: tuple[int, int]
    """ Size of the image in pixels."""

    def convert_buffer_type(self, buffer_type: typing.Literal["BYTE", "FLOAT"]) -> None:
        """Convert the images pixel buffer to the given type.
        When the image is already of the given type this is a no-op.
        The previous buffer is freed.

                :param buffer_type: The buffer type.
        """

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

    def with_buffer(
        self,
        *,
        write: bool = False,
        region: None | tuple[tuple[int, int], tuple[int, int]] | None = None,
    ) -> ImBufBuffer:
        """Return a context manager that yields a `memoryview` of the images pixel data, shaped (height, width, channels).Usage:

        :param write: When true the buffer is writable.
        :param region: Optional sub-region ((x_min, y_min), (x_max, y_max)), clamped to image bounds. When set the shape becomes (region_height, region_width, channels).
        :return: A context manager yielding a `memoryview` of pixel data.
        """

class ImBufBuffer: ...

class ImBufFileType:
    file_extensions: tuple[str, ...]
    """ The file extensions associated with this image file type (e.g. (".jpg", ".jpeg"))."""

    has_read_file: bool
    """ True when images of this file type can be read from a file."""

    has_read_memory: bool
    """ True when images of this file type can be read from memory."""

    has_write_file: bool
    """ True when images of this file type can be written to a file."""

    has_write_memory: bool
    """ True when images of this file type can be written to memory."""

    id: str
    """ The identifier for this image file type (e.g. "PNG", "JPEG")."""
