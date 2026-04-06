import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class SCENE_OT_freestyle_add_edge_marks_to_keying_set(_bpy_types.Operator):
    """Add the data paths to the Freestyle Edge Mark property of selected edges to the active keying set"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SCENE_OT_freestyle_add_face_marks_to_keying_set(_bpy_types.Operator):
    """Add the data paths to the Freestyle Face Mark property of selected polygons to the active keying set"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SCENE_OT_freestyle_fill_range_by_selection(_bpy_types.Operator):
    """Fill the Range Min/Max entries by the min/max distance between selected mesh objects and the source object (either a user-specified object or the active camera)"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SCENE_OT_freestyle_module_open(_bpy_types.Operator):
    """Open a style module file"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """
