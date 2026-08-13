import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types
import rna_prop_ui

class WORKSPACE_PT_addons(WorkSpaceButtonsPanel, _bpy_types.Panel):
    addon_map: typing.Any
    bl_category: typing.Any
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    id_data: typing.Any
    owner_ids: typing.Any

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

    def draw_header(self, context) -> None:
        """

        :param context:
        """

class WORKSPACE_PT_custom_props(
    rna_prop_ui.PropertyPanel, WorkSpaceButtonsPanel, _bpy_types.Panel
):
    """The subclass should have its own poll function
    and the variable _context_path MUST be set.
    """

    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
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

class WORKSPACE_PT_main(WorkSpaceButtonsPanel, _bpy_types.Panel):
    bl_category: typing.Any
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class WORKSPACE_UL_addons_items(_bpy_types.UIList):
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

    def draw_item(
        self,
        context,
        layout,
        _data,
        addon,
        _icon,
        _active_data,
        _active_propname,
        _index,
    ) -> None:
        """

        :param context:
        :param layout:
        :param _data:
        :param addon:
        :param _icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

    def filter_items(self, _context, data, property) -> None:
        """

        :param _context:
        :param data:
        :param property:
        """

class WorkSpaceButtonsPanel:
    bl_category: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any
