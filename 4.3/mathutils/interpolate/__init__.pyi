"""
The Blender interpolate module

"""

import typing
import collections.abc
import typing_extensions

def poly_3d_calc(
    veclist: collections.abc.Sequence[collections.abc.Sequence[float]], pt
) -> list[float]:
    """Calculate barycentric weights for a point on a polygon.

    :param veclist: Sequence of 3D positions.
    :type veclist: collections.abc.Sequence[collections.abc.Sequence[float]]
    :param pt: 2D or 3D position.   :type pt: Sequence[float]   :return: list of per-vector weights.
    :rtype: list[float]
    """
