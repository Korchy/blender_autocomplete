import typing
import collections.abc
import typing_extensions
import bpy.types

class MoveModifierToNodes(bpy.types.Operator):
    """Move inputs and outputs from in the modifier to a new node group"""

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

    def invoke(self, context, event):
        """

        :param context:
        :param event:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class NewGeometryNodeGroupTool(bpy.types.Operator):
    """Create a new geometry node group for a tool"""

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class NewGeometryNodeTreeAssign(bpy.types.Operator):
    """Create a new geometry node group and assign it to the active modifier"""

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class NewGeometryNodesModifier(bpy.types.Operator):
    """Create a new modifier with a new geometry node group"""

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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ZoneOperator:
    @classmethod
    def get_node(cls, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

def add_empty_geometry_node_group(name): ...
def create_wrapper_group(operator, modifier, old_group): ...
def edit_geometry_nodes_modifier_poll(context): ...
def geometry_modifier_poll(context): ...
def geometry_node_group_empty_modifier_new(name): ...
def geometry_node_group_empty_new(name): ...
def geometry_node_group_empty_tool_new(context): ...
def get_context_modifier(context): ...
def get_enabled_socket_with_name(sockets, name): ...
def get_socket_with_identifier(sockets, identifier): ...
def modifier_attribute_name_get(modifier, identifier): ...
def modifier_input_use_attribute(modifier, identifier): ...
def socket_idname_to_attribute_type(idname): ...
