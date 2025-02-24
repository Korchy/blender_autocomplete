import typing
import collections.abc
import typing_extensions
import bpy.types
import mathutils

def edge_face_count(mesh) -> list[int]:
    """

    :return: list face users for each item in mesh.edges.
    :rtype: list[int]
    """

def edge_face_count_dict(mesh) -> dict[tuple[int, int], int]:
    """

    :return: Dictionary of edge keys with their value set to the number of faces using each edge.
    :rtype: dict[tuple[int, int], int]
    """

def edge_loops_from_edges(mesh, edges=None):
    """Edge loops defined by edgesTakes me.edges or a list of edges and returns the edge loopsreturn a list of vertex indices.
    [ [1, 6, 7, 2], ...]closed loops have matching start and end values.

    """

def mesh_linked_triangles(
    mesh: bpy.types.Mesh,
) -> list[list[bpy.types.MeshLoopTriangle]]:
    """Splits the mesh into connected triangles, use this for separating cubes from
    other mesh elements within 1 mesh data-block.

        :param mesh: the mesh used to group with.
        :type mesh: bpy.types.Mesh
        :return: Lists of lists containing triangles.
        :rtype: list[list[bpy.types.MeshLoopTriangle]]
    """

def mesh_linked_uv_islands(mesh: bpy.types.Mesh) -> list[list[int]]:
    """Returns lists of polygon indices connected by UV islands.

    :param mesh: the mesh used to group with.
    :type mesh: bpy.types.Mesh
    :return: list of lists containing polygon indices
    :rtype: list[list[int]]
    """

def ngon_tessellate(
    from_data: bpy.types.Mesh
    | list[collections.abc.Sequence[float]]
    | tuple[collections.abc.Sequence[float]],
    indices: list[int],
    fix_loops: bool = True,
    debug_print=True,
):
    """Takes a poly-line of indices (ngon) and returns a list of face
    index lists. Designed to be used for importers that need indices for an
    ngon to create from existing verts.

        :param from_data: Either a mesh, or a list/tuple of 3D vectors.
        :type from_data: bpy.types.Mesh | list[collections.abc.Sequence[float]] | tuple[collections.abc.Sequence[float]]
        :param indices: a list of indices to use this list
    is the ordered closed poly-line
    to fill, and can be a subset of the data given.
        :type indices: list[int]
        :param fix_loops: If this is enabled poly-lines
    that use loops to make multiple
    poly-lines are dealt with correctly.
        :type fix_loops: bool
    """

def triangle_random_points(
    num_points: int,
    loop_triangles: collections.abc.Sequence[bpy.types.MeshLoopTriangle],
) -> list[mathutils.Vector]:
    """Generates a list of random points over mesh loop triangles.

    :param num_points: The number of random points to generate on each triangle.
    :type num_points: int
    :param loop_triangles: Sequence of the triangles to generate points on.
    :type loop_triangles: collections.abc.Sequence[bpy.types.MeshLoopTriangle]
    :return: List of random points over all triangles.
    :rtype: list[mathutils.Vector]
    """
