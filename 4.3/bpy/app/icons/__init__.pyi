import typing
import collections.abc
import typing_extensions

def new_triangles(
    range: tuple[int, int] | None, coords: bytes | None, colors: bytes | None
) -> int:
    """Create a new icon from triangle geometry.

    :param range: Pair of ints.
    :type range: tuple[int, int] | None
    :param coords: Sequence of bytes (6 floats for one triangle) for (X, Y) coordinates.
    :type coords: bytes | None
    :param colors: Sequence of bytes (12 for one triangles) for RGBA.
    :type colors: bytes | None
    :return: Unique icon value (pass to interface icon_value argument).
    :rtype: int
    """

def new_triangles_from_file(filepath: str | None) -> int:
    """Create a new icon from triangle geometry.

    :param filepath: File path.
    :type filepath: str | None
    :return: Unique icon value (pass to interface icon_value argument).
    :rtype: int
    """

def release(icon_id):
    """Release the icon."""
