import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

def get_all_referenced_ids(
    id: bpy.types.ID, ref_map: dict[bpy.types.ID, set[bpy.types.ID]]
) -> set[bpy.types.ID]:
    """Return a set of IDs directly or indirectly referenced by id.

    :param id: Datablock whose references were interested in.
    :param ref_map: The global ID reference map, retrieved from get_id_reference_map()
    :return: Set of datablocks referenced by id.
    """

def get_id_reference_map() -> dict[bpy.types.ID, set[bpy.types.ID]]:
    """Return a dictionary of direct data-block references for every data-block in the blend file.

    :return: Each datablock of the .blend file mapped to the set of IDs they directly reference.
    """
