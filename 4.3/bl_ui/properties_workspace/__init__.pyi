import typing
import collections.abc
import typing_extensions
import bpy.types
import rna_prop_ui

class WORKSPACE_PT_addons(WorkSpaceButtonsPanel, bpy.types.Panel):
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
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

class WORKSPACE_PT_custom_props(
    rna_prop_ui.PropertyPanel, WorkSpaceButtonsPanel, bpy.types.Panel
):
    """The subclass should have its own poll function
    and the variable '_context_path' MUST be set.
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
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

class WORKSPACE_PT_main(WorkSpaceButtonsPanel, bpy.types.Panel):
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
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw(self, context):
        """

        :param context:
        """

class WORKSPACE_UL_addons_items(bpy.types.UIList):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw_item(
        self,
        context,
        layout,
        _data,
        addon,
        icon,
        _active_data,
        _active_propname,
        _index,
    ):
        """

        :param context:
        :param layout:
        :param _data:
        :param addon:
        :param icon:
        :param _active_data:
        :param _active_propname:
        :param _index:
        """

    def filter_items(self, _context, data, property):
        """

        :param _context:
        :param data:
        :param property:
        """

class WorkSpaceButtonsPanel:
    bl_category: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any
