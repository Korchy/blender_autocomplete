import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bl_ui.node_add_menu
import bpy.types

class NODE_MT_compositor_node_all_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_color_adjust_base(bl_ui.node_add_menu.NodeMenu):
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

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class NODE_MT_compositor_node_color_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_color_mix_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_creative_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_filter_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_filter_blur_base(bl_ui.node_add_menu.NodeMenu):
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

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class NODE_MT_compositor_node_input_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_input_constant_base(bl_ui.node_add_menu.NodeMenu):
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

    def draw(self, _context) -> None:
        """

        :param _context:
        """

class NODE_MT_compositor_node_input_scene_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_keying_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_mask_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_math_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_output_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_texture_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_tracking_base(bl_ui.node_add_menu.NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class NODE_MT_compositor_node_transform_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_utilities_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_compositor_node_vector_base(bl_ui.node_add_menu.NodeMenu):
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
