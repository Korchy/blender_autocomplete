import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bl_ui.utils
import bpy.types

class AddPresetBase:
    bl_options: typing.Any

    @staticmethod
    def as_filename(name) -> None:
        """

        :param name:
        """

    def check(self, _context) -> None:
        """

        :param _context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

class AddPresetCamera(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Camera Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetCameraSafeAreas(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Safe Areas Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetCloth(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Cloth Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetColorManagementWhiteBalance(AddPresetBase, _bpy_types.Operator):
    """Add or remove a white balance preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetEEVEERaytracing(AddPresetBase, _bpy_types.Operator):
    """Add or remove an EEVEE ray-tracing preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetFluid(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Fluid Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetGpencilBrush(AddPresetBase, _bpy_types.Operator):
    """Add or remove Grease Pencil brush preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetGpencilMaterial(AddPresetBase, _bpy_types.Operator):
    """Add or remove Grease Pencil material preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetHairDynamics(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Hair Dynamics Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetInterfaceTheme(AddPresetBase, _bpy_types.Operator):
    """Add a custom theme to the preset list"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def post_cb(self, context, filepath) -> None:
        """

        :param context:
        :param filepath:
        """

class AddPresetKeyconfig(AddPresetBase, _bpy_types.Operator):
    """Add a custom keymap configuration to the preset list"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any

    def add(self, _context, filepath) -> None:
        """

        :param _context:
        :param filepath:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetNodeColor(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Node Color Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetOperator(AddPresetBase, _bpy_types.Operator):
    """Add or remove an Operator Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    @staticmethod
    def operator_path(operator) -> None:
        """

        :param operator:
        """

class AddPresetRender(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Render Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetTextEditor(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Text Editor Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetTrackingCamera(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Tracking Camera Intrinsics Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetTrackingSettings(AddPresetBase, _bpy_types.Operator):
    """Add or remove a motion tracking settings preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class AddPresetTrackingTrackColor(AddPresetBase, _bpy_types.Operator):
    """Add or remove a Clip Track Color Preset"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_defines: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any
    preset_values: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class ExecutePreset(_bpy_types.Operator):
    """Load a preset"""

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

    def execute(self, context) -> None:
        """

        :param context:
        """

class RemovePresetInterfaceTheme(AddPresetBase, _bpy_types.Operator):
    """Remove a custom theme from the preset list"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    def post_cb(self, context, _filepath) -> None:
        """

        :param context:
        :param _filepath:
        """

class RemovePresetKeyconfig(AddPresetBase, _bpy_types.Operator):
    """Remove a custom keymap configuration from the preset list"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    def post_cb(self, context, _filepath) -> None:
        """

        :param context:
        :param _filepath:
        """

    def pre_cb(self, context) -> None:
        """

        :param context:
        """

class SavePresetInterfaceTheme(AddPresetBase, _bpy_types.Operator):
    """Save a custom theme in the preset list"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_menu: typing.Any
    preset_subdir: typing.Any

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

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

class WM_MT_operator_presets(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

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

class WM_OT_operator_presets_cleanup(_bpy_types.Operator):
    """Remove outdated operator properties from presets that may cause problems"""

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

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_PT_operator_presets(bl_ui.utils.PresetPanel, _bpy_types.Panel):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    preset_add_operator: typing.Any
    preset_add_operator_properties: typing.Any
    preset_operator: typing.Any
    preset_subdir: typing.Any

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
