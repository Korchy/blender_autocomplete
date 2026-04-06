import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class DATA_PT_shader_fx(ShaderFxButtonsPanel, _bpy_types.Panel):
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

class ShaderFxButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any
