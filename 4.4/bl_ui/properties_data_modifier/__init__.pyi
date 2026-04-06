import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class AddModifierMenu(bpy.types.Operator):
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

class DATA_PT_modifiers(ModifierButtonsPanel, bpy.types.Panel):
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
    def operator_modifier_add(cls, layout, mod_type) -> None:
        """

        :param layout:
        :param mod_type:
        """

class ModifierButtonsPanel:
    bl_context: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

class OBJECT_MT_modifier_add(ModifierAddMenu, bpy.types.Menu):
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

class OBJECT_MT_modifier_add_color(ModifierAddMenu, bpy.types.Menu):
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

class OBJECT_MT_modifier_add_deform(ModifierAddMenu, bpy.types.Menu):
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

class OBJECT_MT_modifier_add_edit(ModifierAddMenu, bpy.types.Menu):
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

class OBJECT_MT_modifier_add_generate(ModifierAddMenu, bpy.types.Menu):
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

class OBJECT_MT_modifier_add_normals(ModifierAddMenu, bpy.types.Menu):
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

class OBJECT_MT_modifier_add_physics(ModifierAddMenu, bpy.types.Menu):
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
