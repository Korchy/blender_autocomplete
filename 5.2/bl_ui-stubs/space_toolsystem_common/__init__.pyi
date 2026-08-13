import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types

class ToolActivePanelHelper:
    bl_label: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

class ToolDef:
    brush_type: typing.Any
    cursor: typing.Any
    data_block: typing.Any
    description: typing.Any
    draw_cursor: typing.Any
    draw_settings: typing.Any
    icon: typing.Any
    idname: typing.Any
    keymap: typing.Any
    label: typing.Any
    operator: typing.Any
    options: typing.Any
    widget: typing.Any
    widget_properties: typing.Any

class ToolSelectPanelHelper:
    def draw(self, context) -> None:
        """

        :param context:
        """

    @staticmethod
    def draw_active_tool_fallback(
        context, layout, tool, *, is_horizontal_layout=False
    ) -> None:
        """

        :param context:
        :param layout:
        :param tool:
        :param is_horizontal_layout:
        """

    @staticmethod
    def draw_active_tool_header(
        context, layout, *, show_tool_icon_always=False, tool_key=None
    ) -> None:
        """

        :param context:
        :param layout:
        :param show_tool_icon_always:
        :param tool_key:
        """

    @classmethod
    def draw_cls(cls, layout, context, detect_layout=True, scale_y=1.75) -> None:
        """

        :param layout:
        :param context:
        :param detect_layout:
        :param scale_y:
        """

    @staticmethod
    def draw_fallback_tool_items(layout, context) -> None:
        """

        :param layout:
        :param context:
        """

    @staticmethod
    def draw_fallback_tool_items_for_pie_menu(layout, context) -> None:
        """

        :param layout:
        :param context:
        """

    @classmethod
    def keymap_ui_hierarchy(cls, context_mode) -> None:
        """

        :param context_mode:
        """

    @classmethod
    def register(cls) -> None: ...
    @classmethod
    def register_ensure(cls) -> None: ...
    @staticmethod
    def tool_active_from_context(context) -> None:
        """

        :param context:
        """

    @classmethod
    def tools_all(cls) -> None: ...
    @classmethod
    def tools_from_context(cls, context, mode=None) -> None:
        """

        :param context:
        :param mode:
        """

class WM_MT_toolsystem_submenu(_bpy_types.Menu):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> None: ...
    def bl_rna_get_subclass_py(self) -> None: ...
    def draw(self, context) -> None:
        """

        :param context:
        """

def activate_by_id(context, space_type, idname, *, as_fallback=False) -> None: ...
def activate_by_id_or_cycle(
    context, space_type, idname, *, offset=1, as_fallback=False
) -> None: ...
def description_from_id(context, space_type, idname, *, use_operator=True) -> None: ...
def item_from_flat_index(context, space_type, index) -> None: ...
def item_from_id(context, space_type, idname) -> None: ...
def item_from_id_active(context, space_type, idname) -> None: ...
def item_from_id_active_with_group(context, space_type, idname) -> None: ...
def item_from_index_active(context, space_type, index) -> None: ...
def item_group_from_id(context, space_type, idname, *, coerce=False) -> None: ...
def keymap_from_id(context, space_type, idname) -> None: ...
