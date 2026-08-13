"""
This module provides access to bmesh geometry evaluation functions.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bmesh.types

def intersect_face_point(
    face: bmesh.types.BMFace,
    point: collections.abc.Sequence[float] | tuple[float, float, float],
) -> bool:
    """Tests if the projection of a point is inside a face (using the faces normal).

    :param face: The face to test.
    :param point: The 3D point to test.
    :return: True when the projection of the point is in the face.
    """
