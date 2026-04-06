import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class NODE_FH_image_node(bpy.types.FileHandler):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
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

    @classmethod
    def poll_drop(cls, context) -> None:
        """

        :param context:
        """

class NODE_OT_add_foreach_geometry_element_zone(
    NodeAddZoneOperator, bpy.types.Operator
):
    """Add a For Each Geometry Element zone that allows executing nodes e.g. for each vertex separately"""

    add_default_geometry_link: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    input_node_type: typing.Any
    output_node_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class NODE_OT_add_node(NodeAddOperator, bpy.types.Operator):
    """Add a node to the active tree"""

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

    @classmethod
    def description(cls, _context, properties) -> None:
        """

        :param _context:
        :param properties:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class NODE_OT_add_repeat_zone(NodeAddZoneOperator, bpy.types.Operator):
    """Add a repeat zone that allows executing nodes a dynamic number of times"""

    add_default_geometry_link: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    input_node_type: typing.Any
    output_node_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class NODE_OT_add_simulation_zone(NodeAddZoneOperator, bpy.types.Operator):
    """Add simulation zone input and output nodes to the active tree"""

    add_default_geometry_link: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    input_node_type: typing.Any
    output_node_type: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class NODE_OT_collapse_hide_unused_toggle(bpy.types.Operator):
    """Toggle collapsed nodes and hide unused sockets"""

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

class NODE_OT_interface_item_duplicate(NodeInterfaceOperator, bpy.types.Operator):
    """Add a copy of the active item to the interface"""

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

class NODE_OT_interface_item_new(NodeInterfaceOperator, bpy.types.Operator):
    """Add a new item to the interface"""

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

    @staticmethod
    def find_valid_socket_type(tree) -> None:
        """

        :param tree:
        """

class NODE_OT_interface_item_remove(NodeInterfaceOperator, bpy.types.Operator):
    """Remove active item from the interface"""

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

class NODE_OT_tree_path_parent(bpy.types.Operator):
    """Go to parent node tree"""

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

class NODE_OT_viewer_shortcut_get(bpy.types.Operator):
    """Activate a specific compositor viewer node using 1,2,..,9 keys"""

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

class NODE_OT_viewer_shortcut_set(bpy.types.Operator):
    """Create a compositor viewer shortcut for the selected node by pressing ctrl+1,2,..9"""

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

    def get_connected_viewer(self, node) -> None:
        """

        :param node:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class NodeAddOperator:
    def create_node(self, context, node_type) -> None:
        """

        :param context:
        :param node_type:
        """

    @staticmethod
    def deselect_nodes(context) -> None:
        """

        :param context:
        """

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

    @staticmethod
    def store_mouse_cursor(context, event) -> None:
        """

        :param context:
        :param event:
        """

class NodeInterfaceOperator:
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class NodeSetting(bpy.types.PropertyGroup):
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

class NodeAddZoneOperator(NodeAddOperator):
    add_default_geometry_link: typing.Any

    def execute(self, context) -> None:
        """

        :param context:
        """
