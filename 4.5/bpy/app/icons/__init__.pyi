import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def new_triangles(
    range: tuple[int, int] | None, coords: bytes | None, colors: bytes | None
) -> int:
    """Create a new icon from triangle geometry.

    :param range: Pair of ints.
    :param coords: Sequence of bytes (6 floats for one triangle) for (X, Y) coordinates.
    :param colors: Sequence of bytes (12 for one triangles) for RGBA.
    :return: Unique icon value (pass to interface icon_value argument).
    """

def new_triangles_from_file(filepath: str | None) -> int:
    """Create a new icon from triangle geometry.

    :param filepath: File path.
    :return: Unique icon value (pass to interface icon_value argument).
    """

def release(icon_id) -> None:
    """Release the icon."""
