import sys
import typing
import bmesh.types

GenericType = typing.TypeVar("GenericType")


def intersect_face_point(face: 'bmesh.types.BMFace',
                         point: typing.Tuple[float]) -> bool:
    ''' Tests if the projection of a point is inside a face (using the face's normal).

    :param face: The face to test.
    :type face: 'bmesh.types.BMFace'
    :param point: The point to test.
    :type point: typing.Tuple[float]
    :rtype: bool
    :return: True when the projection of the point is in the face.
    '''

    pass
