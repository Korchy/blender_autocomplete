import typing
import collections.abc
import typing_extensions
import bpy.types

def get_all_referenced_ids(id: bpy.types.ID, ref_map: dict[bpy.types.ID]):
    """

    :param id: The ID to lookup.
    :type id: bpy.types.ID
    :param ref_map: The ID to lookup.
    :type ref_map: dict[bpy.types.ID]
    :return: A set of IDs directly or indirectly referenced by id.
    """

def get_id_reference_map() -> dict[bpy.types.ID]:
    """

    :return: Return a dictionary of direct data-block references for every data-block in the blend file.
    :rtype: dict[bpy.types.ID]
    """
