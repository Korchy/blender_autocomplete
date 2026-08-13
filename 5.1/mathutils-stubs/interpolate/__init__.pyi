"""
The Blender interpolate module.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def poly_3d_calc(
    veclist: collections.abc.Sequence[collections.abc.Sequence[float]],
    pt: collections.abc.Sequence[float],
    /,
) -> list[float]:
    """Calculate barycentric weights for a point on a polygon.

    :param veclist: Sequence of 3D positions.
    :param pt: 2D or 3D position.
    :return: A list of weights, one per vertex in veclist.
    """
