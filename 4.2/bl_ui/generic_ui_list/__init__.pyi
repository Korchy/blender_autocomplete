import typing
import collections.abc
import typing_extensions
import bpy.types

class GenericUIListOperator:
    """Mix-in class containing functionality shared by operators
    that deal with managing Blender list entries.
    """

    bl_options: typing.Any

    def get_active_index(self, context):
        """

        :param context:
        """

    def get_list(self, context):
        """

        :param context:
        """

    def set_active_index(self, context, index):
        """

        :param context:
        :param index:
        """

class UILIST_OT_entry_add(GenericUIListOperator, bpy.types.Operator):
    """Add an entry to the list after the current active item"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, context):
        """

        :param context:
        """

class UILIST_OT_entry_move(GenericUIListOperator, bpy.types.Operator):
    """Move an entry in the list up or down"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, context):
        """

        :param context:
        """

class UILIST_OT_entry_remove(GenericUIListOperator, bpy.types.Operator):
    """Remove the selected entry from the list"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def execute(self, context):
        """

        :param context:
        """

def draw_ui_list(
    layout: bpy.types.UILayout,
    context: bpy.types.Context | None,
    class_name: str = "UI_UL_list",
    *,
    unique_id: str,
    list_path: str,
    active_index_path: str,
    insertion_operators: bool = True,
    move_operators: str = True,
    menu_class_name: str = "",
    **kwargs,
):
    """Draw a UIList with Add/Remove/Move buttons and a menu.Additional keyword arguments are passed to `UIList.template_list`.

        :param layout: UILayout to draw the list in.
        :type layout: bpy.types.UILayout
        :param context: Blender context to get the list data from.
        :type context: bpy.types.Context | None
        :param class_name: Name of the UIList class to draw. The default is the UIList class that ships with Blender.
        :type class_name: str
        :param unique_id: Unique identifier to differentiate this from other UI lists.
        :type unique_id: str
        :param list_path: Data path of the list relative to context, eg. "object.vertex_groups".
        :type list_path: str
        :param active_index_path: Data path of the list active index integer relative to context,
    eg. "object.vertex_groups.active_index".
        :type active_index_path: str
        :param insertion_operators: Whether to draw Add/Remove buttons.
        :type insertion_operators: bool
        :param move_operators: Whether to draw Move Up/Down buttons.
        :type move_operators: str
        :param menu_class_name: Identifier of a Menu that should be drawn as a drop-down.
        :type menu_class_name: str
        :return: The right side column.
    """
