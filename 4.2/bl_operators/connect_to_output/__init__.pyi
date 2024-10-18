import typing
import collections.abc
import typing_extensions
import bl_operators.node_editor.node_functions
import bpy.types

class NODE_OT_connect_to_output(
    bpy.types.Operator, bl_operators.node_editor.node_functions.NodeEditorBase
):
    bl_description: typing.Any
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

    def cleanup(self): ...
    def create_links(self, path, node, active_node_socket_id, socket_type):
        """Create links at each step in the node group path.

        :param path:
        :param node:
        :param active_node_socket_id:
        :param socket_type:
        """

    @staticmethod
    def ensure_group_output(node_tree):
        """Check if a group output node exists, otherwise create it

        :param node_tree:
        """

    def ensure_viewer_socket(self, node_tree, socket_type, connect_socket=None):
        """Check if a viewer output already exists in a node group, otherwise create it

        :param node_tree:
        :param socket_type:
        :param connect_socket:
        """

    def get_output_index(
        self, node, output_node, is_base_node_tree, socket_type, check_type=False
    ):
        """Get the next available output socket in the active node

        :param node:
        :param output_node:
        :param is_base_node_tree:
        :param socket_type:
        :param check_type:
        """

    @staticmethod
    def get_output_sockets(node_tree):
        """

        :param node_tree:
        """

    def has_socket_other_users(self, socket):
        """List the other users for this socket (other materials or geometry nodes groups)

        :param socket:
        """

    def init_shader_variables(self, space, shader_type):
        """Get correct output node in shader editor

        :param space:
        :param shader_type:
        """

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

    def is_socket_used_active_tree(self, socket):
        """Ensure used sockets in active node tree is calculated and check given socket

        :param socket:
        """

    def link_leads_to_used_socket(self, link):
        """Return True if link leads to a socket that is already used in this node

        :param link:
        """

    @classmethod
    def poll(cls, context):
        """Already implemented natively for compositing nodes.

        :param context:
        """

    @staticmethod
    def remove_socket(tree, socket):
        """

        :param tree:
        :param socket:
        """

    @classmethod
    def search_connected_viewer_sockets(cls, output_node, r_sockets, index=None):
        """From an output node, recursively scan node tree for connected viewer sockets

        :param output_node:
        :param r_sockets:
        :param index:
        """

    @classmethod
    def search_viewer_sockets_in_tree(cls, tree, r_sockets):
        """Recursively get all viewer sockets in a node tree

        :param tree:
        :param r_sockets:
        """
