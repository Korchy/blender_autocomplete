"""
BVH tree structures for proximity searches and ray casts on geometry.

"""

import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bmesh.types
import bpy.types
import mathutils

class BVHTree:
    @classmethod
    def FromBMesh(
        cls, bmesh: bmesh.types.BMesh, *, epsilon: float = 0.0
    ) -> typing_extensions.Self:
        """BVH tree based on `BMesh` data.

        :param bmesh: BMesh data.
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :return: BVHTree from BMesh data.
        """

    @classmethod
    def FromObject(
        cls,
        object: _bpy_types.Object,
        depsgraph: bpy.types.Depsgraph,
        *,
        deform: bool = True,
        cage: bool = False,
        epsilon: float = 0.0,
    ) -> typing_extensions.Self:
        """BVH tree based on `Object` data.

        :param object: Mesh object.
        :param depsgraph: Depsgraph to use for evaluating the mesh.
        :param deform: Use mesh with deformations.
        :param cage: Use modifiers cage.
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :return: BVHTree from Object data.
        """

    @classmethod
    def FromPolygons(
        cls,
        vertices: collections.abc.Sequence[collections.abc.Sequence[float]],
        polygons: collections.abc.Sequence[collections.abc.Sequence[int]],
        *,
        all_triangles: bool = False,
        epsilon: float = 0.0,
    ) -> typing_extensions.Self:
        """BVH tree constructed from geometry passed in as arguments.

        :param vertices: float triplets each representing (x, y, z) coordinates.
        :param polygons: Sequence of polygons, each containing indices to the vertices argument.
        :param all_triangles: Use when all polygons are triangles for more efficient conversion.
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :return: BVHTree from polygon data.
        """

    def find_nearest(
        self,
        origin: collections.abc.Sequence[float] | mathutils.Vector,
        distance: float = 1.84467e19,
        /,
    ) -> tuple[
        mathutils.Vector | None, mathutils.Vector | None, int | None, float | None
    ]:
        """Find the nearest element (typically face index) to a point.

                :param origin: Find nearest element to this point.
                :param distance: Maximum distance threshold.
                :return: Returns a tuple: (position, normal, index, distance),
        Values will all be None if no hit is found.
        """

    def find_nearest_range(
        self,
        origin: collections.abc.Sequence[float] | mathutils.Vector,
        distance: float = 1.84467e19,
        /,
    ) -> list[tuple[mathutils.Vector, mathutils.Vector, int, float]]:
        """Find the nearest elements (typically face index) to a point in the distance range.

        :param origin: Find nearest elements to this point.
        :param distance: Maximum distance threshold.
        :return: Returns a list of tuples (position, normal, index, distance)
        """

    def overlap(
        self,
        other_tree: typing_extensions.Self,
        /,
    ) -> list[tuple[int, int]]:
        """Find overlapping indices between 2 trees.

        :param other_tree: Other tree to perform overlap test on.
        :return: Returns a list of unique index pairs, the first index referencing this tree, the second referencing the other_tree.
        """

    def ray_cast(
        self,
        origin: collections.abc.Sequence[float] | mathutils.Vector,
        direction: collections.abc.Sequence[float] | mathutils.Vector,
        distance: float = sys.float_info.max,
        /,
    ) -> tuple[
        mathutils.Vector | None, mathutils.Vector | None, int | None, float | None
    ]:
        """Cast a ray onto the geometry.

                :param origin: Start location of the ray.
                :param direction: Direction of the ray (normalized internally).
                :param distance: Maximum distance threshold.
                :return: Returns a tuple: (position, normal, index, distance),
        Values will all be None if no hit is found.
        """

    def __init__(self, size) -> None:
        """

        :param size:
        """
