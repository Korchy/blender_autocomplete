import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def bmesh_linked_uv_islands(bm, uv_layer) -> list:
    """Returns lists of faces connected by UV islands.For meshes use `bpy.types.Mesh.mesh_linked_uv_islands` instead.

    :param bm: the bmesh used to group with.
    :param uv_layer: the UV layer to source UVs from.
    :return: list of lists containing polygon indices
    :rtype: list
    """

    ...

def match_uv(face, vert, uv, uv_layer): ...
