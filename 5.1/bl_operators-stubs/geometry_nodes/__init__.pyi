import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class MoveModifierToNodes(_bpy_types.Operator):
    """Move inputs and outputs from in the modifier to a new node group"""

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

class NewGeometryNodeGroupTool(_bpy_types.Operator):
    """Create a new geometry node group for a tool"""

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

class NewGeometryNodeTreeAssign(_bpy_types.Operator):
    """Create a new geometry node group and assign it to the active modifier"""

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

class NewGeometryNodesModifier(_bpy_types.Operator):
    """Create a new modifier with a new geometry node group"""

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

class ZoneOperator:
    @classmethod
    def get_node(cls, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

def add_empty_geometry_node_group(name) -> None: ...
def create_wrapper_group(operator, modifier, old_group) -> None: ...
def edit_geometry_nodes_modifier_poll(context) -> None: ...
def geometry_modifier_poll(context) -> None: ...
def geometry_node_group_empty_modifier_new(name) -> None: ...
def geometry_node_group_empty_new(name) -> None: ...
def geometry_node_group_empty_tool_new(context) -> None: ...
def get_context_modifier(context) -> None: ...
def get_enabled_socket_with_name(sockets, name) -> None: ...
def get_socket_with_identifier(sockets, identifier) -> None: ...
def modifier_attribute_name_get(modifier, identifier) -> None: ...
def modifier_input_use_attribute(modifier, identifier) -> None: ...
def socket_idname_to_attribute_type(idname) -> None: ...
