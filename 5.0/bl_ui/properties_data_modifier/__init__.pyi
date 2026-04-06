import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class AddModifierMenu(_bpy_types.Operator):
    bl_idname: typing.Any
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

    def invoke(self, _context, _event) -> None:
        """

        :param _context:
        :param _event:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class DATA_PT_modifiers(ModifierButtonsPanel, _bpy_types.Panel):
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

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class ModifierAddMenu:
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any

    @classmethod
    def operator_modifier_add(cls, layout, mod_type, text=None, no_icon=False) -> None:
        """

        :param layout:
        :param mod_type:
        :param text:
        :param no_icon:
        """

    @classmethod
    def operator_modifier_add_asset(cls, layout, name, icon="NONE") -> None:
        """

        :param layout:
        :param name:
        :param icon:
        """

class ModifierButtonsPanel:
    bl_context: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class OBJECT_MT_modifier_add(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class OBJECT_MT_modifier_add_color(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class OBJECT_MT_modifier_add_deform(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class OBJECT_MT_modifier_add_edit(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class OBJECT_MT_modifier_add_generate(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class OBJECT_MT_modifier_add_normals(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class OBJECT_MT_modifier_add_physics(ModifierAddMenu, _bpy_types.Menu):
    MODIFIER_TYPES_I18N_CONTEXT: typing.Any
    MODIFIER_TYPES_TO_ICONS: typing.Any
    MODIFIER_TYPES_TO_LABELS: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """
