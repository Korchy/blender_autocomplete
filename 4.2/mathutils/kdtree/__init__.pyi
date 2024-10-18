"""
Generic 3-dimensional kd-tree to perform spatial searches.

```../examples/mathutils.kdtree.py```

"""

import typing
import collections.abc
import typing_extensions
import mathutils

class KDTree:
    """KdTree(size) -> new kd-tree initialized to hold size items."""

    def balance(self):
        """Balance the tree."""

    def find(
        self,
        co: collections.abc.Sequence[float] | mathutils.Vector,
        filter: collections.abc.Callable | None = None,
    ) -> tuple:
        """Find nearest point to co.

        :param co: 3d coordinates.
        :type co: collections.abc.Sequence[float] | mathutils.Vector
        :param filter: function which takes an index and returns True for indices to include in the search.
        :type filter: collections.abc.Callable | None
        :return: Returns (`Vector`, index, distance).
        :rtype: tuple
        """

    def find_n(
        self, co: collections.abc.Sequence[float] | mathutils.Vector, n: int
    ) -> list:
        """Find nearest n points to co.

        :param co: 3d coordinates.
        :type co: collections.abc.Sequence[float] | mathutils.Vector
        :param n: Number of points to find.
        :type n: int
        :return: Returns a list of tuples (`Vector`, index, distance).
        :rtype: list
        """

    def find_range(
        self, co: collections.abc.Sequence[float] | mathutils.Vector, radius: float
    ) -> list:
        """Find all points within radius of co.

        :param co: 3d coordinates.
        :type co: collections.abc.Sequence[float] | mathutils.Vector
        :param radius: Distance to search for points.
        :type radius: float
        :return: Returns a list of tuples (`Vector`, index, distance).
        :rtype: list
        """

    def insert(
        self, co: collections.abc.Sequence[float] | mathutils.Vector, index: int
    ):
        """Insert a point into the KDTree.

        :param co: Point 3d position.
        :type co: collections.abc.Sequence[float] | mathutils.Vector
        :param index: The index of the point.
        :type index: int
        """

    def __init__(self, size):
        """

        :param size:
        """
