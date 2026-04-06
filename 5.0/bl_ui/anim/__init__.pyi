import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class ANIM_MT_keyframe_insert_pie(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

def draw_action_and_slot_selector_for_id(layout, animated_id) -> None:
    """Draw the action and slot selector for an ID, using the given layout.The ID must be an animatable ID.Note that the slot selector is only drawn when the ID has an assigned
    Action.

    """
