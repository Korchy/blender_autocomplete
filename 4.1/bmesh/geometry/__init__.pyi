"""
This module provides access to bmesh geometry evaluation functions.

"""

import typing
import collections.abc
import bmesh.types
import mathutils

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def intersect_face_point(
    face: bmesh.types.BMFace, point: collections.abc.Sequence[float] | mathutils.Vector
) -> bool:
    """Tests if the projection of a point is inside a face (using the face's normal).

    :param face: The face to test.
    :type face: bmesh.types.BMFace
    :param point: The point to test.
    :type point: collections.abc.Sequence[float] | mathutils.Vector
    :return: True when the projection of the point is in the face.
    :rtype: bool
    """

    ...
