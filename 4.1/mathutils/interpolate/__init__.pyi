"""
The Blender interpolate module

"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def poly_3d_calc(veclist, pt):
    """Calculate barycentric weights for a point on a polygon.

    :param veclist: list of vectors
    :param pt: point   :rtype: list of per-vector weights
    """

    ...
