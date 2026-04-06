"""
Generic 3-dimensional kd-tree to perform spatial searches.

```../examples/mathutils.kdtree.py```

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import mathutils

class KDTree:
    """KdTree(size) -> new kd-tree initialized to hold size items."""

    def balance(self) -> None:
        """Balance the tree."""

    def find(
        self,
        co: collections.abc.Sequence[float],
        *,
        filter: collections.abc.Callable[int, bool] | None = None,
    ) -> tuple[mathutils.Vector, int, float]:
        """Find nearest point to co.

        :param co: 3D coordinates.
        :param filter: function which takes an index and returns True for indices to include in the search.
        :return: Returns (position, index, distance).
        """

    def find_n(
        self, co: collections.abc.Sequence[float], n: int
    ) -> list[tuple[mathutils.Vector, int, float]]:
        """Find nearest n points to co.

        :param co: 3D coordinates.
        :param n: Number of points to find.
        :return: Returns a list of tuples (position, index, distance).
        """

    def find_range(
        self, co: collections.abc.Sequence[float], radius: float
    ) -> list[tuple[mathutils.Vector, int, float]]:
        """Find all points within radius of co.

        :param co: 3D coordinates.
        :param radius: Distance to search for points.
        :return: Returns a list of tuples (position, index, distance).
        """

    def insert(self, co: collections.abc.Sequence[float], index: int) -> None:
        """Insert a point into the KDTree.

        :param co: Point 3d position.
        :param index: The index of the point.
        """

    def __init__(self, size) -> None:
        """

        :param size:
        """
