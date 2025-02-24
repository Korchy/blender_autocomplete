"""
BVH tree structures for proximity searches and ray casts on geometry.

"""

import typing
import collections.abc
import typing_extensions
import bmesh.types
import bpy.types
import mathutils

class BVHTree:
    @classmethod
    def FromBMesh(cls, bmesh: bmesh.types.BMesh, epsilon: float = 0.0):
        """BVH tree based on `BMesh` data.

        :param bmesh: BMesh data.
        :type bmesh: bmesh.types.BMesh
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    @classmethod
    def FromObject(
        cls,
        object: bpy.types.Object,
        depsgraph: bpy.types.Depsgraph,
        deform: bool = True,
        render=False,
        cage: bool = False,
        epsilon: float = 0.0,
    ):
        """BVH tree based on `Object` data.

        :param object: Object data.
        :type object: bpy.types.Object
        :param depsgraph: Depsgraph to use for evaluating the mesh.
        :type depsgraph: bpy.types.Depsgraph
        :param deform: Use mesh with deformations.
        :type deform: bool
        :param render:
        :param cage: Use modifiers cage.
        :type cage: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    @classmethod
    def FromPolygons(
        cls,
        vertices: collections.abc.Sequence[collections.abc.Sequence[float]],
        polygons: collections.abc.Sequence[collections.abc.Sequence[int]],
        all_triangles: bool = False,
        epsilon: float = 0.0,
    ):
        """BVH tree constructed geometry passed in as arguments.

        :param vertices: float triplets each representing (x, y, z)
        :type vertices: collections.abc.Sequence[collections.abc.Sequence[float]]
        :param polygons: Sequence of polygons, each containing indices to the vertices argument.
        :type polygons: collections.abc.Sequence[collections.abc.Sequence[int]]
        :param all_triangles: Use when all polygons are triangles for more efficient conversion.
        :type all_triangles: bool
        :param epsilon: Increase the threshold for detecting overlap and raycast hits.
        :type epsilon: float
        """

    def find_nearest(
        self, origin, distance: float = 1.84467e19
    ) -> tuple[
        mathutils.Vector | None, mathutils.Vector | None, int | None, float | None
    ]:
        """Find the nearest element (typically face index) to a point.

                :param origin:
                :param distance: Maximum distance threshold.
                :type distance: float
                :return: Returns a tuple: (position, normal, index, distance),
        Values will all be None if no hit is found.
                :rtype: tuple[mathutils.Vector | None, mathutils.Vector | None, int | None, float | None]
        """

    def find_nearest_range(
        self, origin, distance: float = 1.84467e19
    ) -> list[tuple[mathutils.Vector, mathutils.Vector, int, float]]:
        """Find the nearest elements (typically face index) to a point in the distance range.

        :param origin:
        :param distance: Maximum distance threshold.
        :type distance: float
        :return: Returns a list of tuples (position, normal, index, distance)
        :rtype: list[tuple[mathutils.Vector, mathutils.Vector, int, float]]
        """

    def overlap(self, other_tree: typing_extensions.Self) -> list[tuple[int, int]]:
        """Find overlapping indices between 2 trees.

        :param other_tree: Other tree to perform overlap test on.
        :type other_tree: typing_extensions.Self
        :return: Returns a list of unique index pairs,      the first index referencing this tree, the second referencing the other_tree.
        :rtype: list[tuple[int, int]]
        """

    def ray_cast(
        self,
        origin: collections.abc.Sequence[float] | mathutils.Vector,
        direction: collections.abc.Sequence[float] | mathutils.Vector,
        distance: float = sys.float_info.max,
    ) -> tuple[
        mathutils.Vector | None, mathutils.Vector | None, int | None, float | None
    ]:
        """Cast a ray onto the mesh.

                :param origin: Start location of the ray in object space.
                :type origin: collections.abc.Sequence[float] | mathutils.Vector
                :param direction: Direction of the ray in object space.
                :type direction: collections.abc.Sequence[float] | mathutils.Vector
                :param distance: Maximum distance threshold.
                :type distance: float
                :return: Returns a tuple: (position, normal, index, distance),
        Values will all be None if no hit is found.
                :rtype: tuple[mathutils.Vector | None, mathutils.Vector | None, int | None, float | None]
        """

    def __init__(self, size):
        """

        :param size:
        """
