import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class NODE_FH_image_node(_bpy_types.FileHandler):
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

class NODE_OT_add_closure_zone(NodeAddZoneOperator, _bpy_types.Operator):
    """Add a Closure zone"""

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

class NODE_OT_add_empty_group(NodeAddOperator, _bpy_types.Operator):
    bl_description: typing.Any
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

    @staticmethod
    def create_empty_group(idname) -> None:
        """

        :param idname:
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

class NODE_OT_add_foreach_geometry_element_zone(
    NodeAddZoneOperator, _bpy_types.Operator
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

class NODE_OT_add_node(NodeAddOperator, _bpy_types.Operator):
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

    def execute(self, context) -> None:
        """

        :param context:
        """

class NODE_OT_add_repeat_zone(NodeAddZoneOperator, _bpy_types.Operator):
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

class NODE_OT_add_simulation_zone(NodeAddZoneOperator, _bpy_types.Operator):
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

class NODE_OT_add_zone(NodeAddZoneOperator, _bpy_types.Operator):
    add_default_geometry_link: typing.Any
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

class NODE_OT_collapse_hide_unused_toggle(_bpy_types.Operator):
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

class NODE_OT_interface_item_duplicate(NodeInterfaceOperator, _bpy_types.Operator):
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

class NODE_OT_interface_item_make_panel_toggle(
    NodeInterfaceOperator, _bpy_types.Operator
):
    """Make the active boolean socket a toggle for its parent panel"""

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

class NODE_OT_interface_item_new(NodeInterfaceOperator, _bpy_types.Operator):
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

class NODE_OT_interface_item_new_panel_toggle(_bpy_types.Operator):
    """Add a checkbox to the currently selected panel"""

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
    def get_panel_toggle(panel) -> None:
        """

        :param panel:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class NODE_OT_interface_item_remove(NodeInterfaceOperator, _bpy_types.Operator):
    """Remove selected items from the interface"""

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

class NODE_OT_interface_item_unlink_panel_toggle(
    NodeInterfaceOperator, _bpy_types.Operator
):
    """Make the panel toggle a stand-alone socket"""

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

class NODE_OT_swap_empty_group(NodeSwapOperator, _bpy_types.Operator):
    bl_description: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    id_prop_names: typing.Any
    image_user_settings: typing.Any
    properties_to_pass: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    @staticmethod
    def create_empty_group(idname) -> None:
        """

        :param idname:
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

class NODE_OT_swap_node(NodeSwapOperator, _bpy_types.Operator):
    """Replace the selected nodes with the specified type"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    id_prop_names: typing.Any
    image_user_settings: typing.Any
    properties_to_pass: typing.Any

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
    def get_node_sockets(node) -> None:
        """

        :param node:
        """

    @staticmethod
    def get_zone_pair(tree, node) -> None:
        """

        :param tree:
        :param node:
        """

    def transfer_node_sockets(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

class NODE_OT_swap_zone(NodeSwapOperator, ZoneOperator, _bpy_types.Operator):
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    id_prop_names: typing.Any
    image_user_settings: typing.Any
    properties_to_pass: typing.Any

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
    def get_child_items(node) -> None:
        """

        :param node:
        """

    @staticmethod
    def get_zone_pair(tree, node) -> None:
        """

        :param tree:
        :param node:
        """

    def transfer_zone_sockets(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

class NODE_OT_tree_path_parent(_bpy_types.Operator):
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

class NODE_OT_viewer_shortcut_get(_bpy_types.Operator):
    """Toggle a specific viewer node using 1,2,..,9 keys"""

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

class NODE_OT_viewer_shortcut_set(_bpy_types.Operator):
    """Create a viewer shortcut for the selected node by pressing ctrl+1,2,..9"""

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

class NodeOperator:
    def apply_node_settings(self, node) -> None:
        """

        :param node:
        """

    def create_node(self, context, node_type) -> None:
        """

        :param context:
        :param node_type:
        """

    @classmethod
    def description(cls, _context, properties) -> None:
        """

        :param _context:
        :param properties:
        """

    @staticmethod
    def deselect_nodes(context) -> None:
        """

        :param context:
        """

class NodeInterfaceOperator:
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class NodeSetting(_bpy_types.PropertyGroup):
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

class ZoneOperator:
    @classmethod
    def description(cls, _context, properties) -> None:
        """

        :param _context:
        :param properties:
        """

class NodeAddOperator(NodeOperator):
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

class NodeSwapOperator(NodeOperator):
    id_prop_names: typing.Any
    image_user_settings: typing.Any
    properties_to_pass: typing.Any

    @staticmethod
    def get_switch_items(node) -> None:
        """

        :param node:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

    def transfer_datablock_properties(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

    def transfer_image_user_settings(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

    def transfer_input_values(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

    @staticmethod
    def transfer_links(tree, old_node, new_node, is_input) -> None:
        """

        :param tree:
        :param old_node:
        :param new_node:
        :param is_input:
        """

    def transfer_node_properties(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

    def transfer_switch_data(self, old_node, new_node) -> None:
        """

        :param old_node:
        :param new_node:
        """

class NodeAddZoneOperator(ZoneOperator, NodeAddOperator):
    add_default_geometry_link: typing.Any

    def execute(self, context) -> None:
        """

        :param context:
        """

def cast_value(source, target) -> None: ...
