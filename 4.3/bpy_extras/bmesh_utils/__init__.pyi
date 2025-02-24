import typing
import collections.abc
import typing_extensions

def bmesh_linked_uv_islands(bm, uv_layer) -> list[list[int]]:
    """Returns lists of faces connected by UV islands.For meshes use `bpy.types.Mesh.mesh_linked_uv_islands` instead.

    :param bm: the bmesh used to group with.
    :param uv_layer: the UV layer to source UVs from.
    :return: list of lists containing polygon indices
    :rtype: list[list[int]]
    """

def match_uv(face, vert, uv, uv_layer): ...
