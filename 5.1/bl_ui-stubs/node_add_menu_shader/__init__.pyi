import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bl_ui.node_add_menu
import bpy.types

class NODE_MT_shader_node_all_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
    id_data: typing.Any
    menu_path: typing.Any

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

class NODE_MT_shader_node_color_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, context) -> None:
        """

        :param context:
        """

class NODE_MT_shader_node_displacement_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class NODE_MT_shader_node_input_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, context) -> None:
        """

        :param context:
        """

class NODE_MT_shader_node_math_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    menu_path: typing.Any

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

class NODE_MT_shader_node_output_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, context) -> None:
        """

        :param context:
        """

class NODE_MT_shader_node_shader_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, context) -> None:
        """

        :param context:
        """

class NODE_MT_shader_node_texture_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class NODE_MT_shader_node_utilities_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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

    def draw(self, context) -> None:
        """

        :param context:
        """

class NODE_MT_shader_node_vector_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    menu_path: typing.Any

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

def cycles_shader_nodes_poll(context) -> None: ...
def eevee_shader_nodes_poll(context) -> None: ...
def line_style_shader_nodes_poll(context) -> None: ...
def object_eevee_shader_nodes_poll(context) -> None: ...
def object_not_eevee_shader_nodes_poll(context) -> None: ...
def object_shader_nodes_poll(context) -> None: ...
def world_shader_nodes_poll(context) -> None: ...
