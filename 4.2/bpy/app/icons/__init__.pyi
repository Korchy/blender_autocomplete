import typing
import collections.abc
import typing_extensions

def new_triangles(
    range: tuple | None,
    coords: collections.abc.Sequence[bytes] | None,
    colors: collections.abc.Sequence[bytes] | None,
) -> int:
    """Create a new icon from triangle geometry.

    :param range: Pair of ints.
    :type range: tuple | None
    :param coords: Sequence of bytes (6 floats for one triangle) for (X, Y) coordinates.
    :type coords: collections.abc.Sequence[bytes] | None
    :param colors: Sequence of ints (12 for one triangles) for RGBA.
    :type colors: collections.abc.Sequence[bytes] | None
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
