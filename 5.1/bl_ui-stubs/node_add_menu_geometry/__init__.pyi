import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bl_ui.node_add_menu
import bpy.types

class NODE_MT_category_utilities_bundle_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_category_utilities_closure_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_all_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_attribute_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_color_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_operations_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_primitives_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_read_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_sample_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_topology_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_curve_write_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_geometry_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_geometry_operations_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_geometry_read_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_geometry_sample_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_geometry_write_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_grease_pencil_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_grease_pencil_operations_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_grease_pencil_read_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_grease_pencil_write_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_input_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_input_constant_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_input_gizmo_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_input_group_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_input_import_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_input_scene_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_instance_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_material_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_operations_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_primitives_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_read_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_sample_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_topology_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_uv_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_mesh_write_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_output_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_point_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_simulation_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_texture_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_deprecated_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_field_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_list_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_math_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_matrix_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_rotation_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_text_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_utilities_vector_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_volume_base(bl_ui.node_add_menu.NodeMenu):
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

    def draw(self, context) -> None:
        """

        :param context:
        """

class NODE_MT_gn_volume_operations_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_volume_primitives_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_volume_read_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_volume_sample_base(bl_ui.node_add_menu.NodeMenu):
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

class NODE_MT_gn_volume_write_base(bl_ui.node_add_menu.NodeMenu):
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
