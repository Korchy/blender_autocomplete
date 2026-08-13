import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class NodeMenu(_bpy_types.Menu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

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
    def closure_zone(cls, layout, label) -> None:
        """

        :param layout:
        :param label:
        """

    @classmethod
    def color_mix_node(cls, context, layout, search_weight=0.0) -> None:
        """The Mix Color node, with its different blend modes available while in search.

        :param context:
        :param layout:
        :param search_weight:
        """

    @classmethod
    def draw_group_menu(cls, context, layout) -> None:
        """Show operators used for interacting with node groups.

        :param context:
        :param layout:
        """

    @classmethod
    def draw_menu(cls, layout, path) -> None:
        """Takes the given menu path and draws the corresponding menu.
        Menu paths are either explicitly defined, or based on bl_label if not.

                :param layout:
                :param path:
        """

    @classmethod
    def draw_root_assets(cls, layout) -> None:
        """

        :param layout:
        """

    @classmethod
    def for_each_element_zone(cls, layout, label) -> None:
        """

        :param layout:
        :param label:
        """

    @classmethod
    def new_empty_group(cls, layout) -> None:
        """Group Node with a newly created empty group as its assigned node-tree.

        :param layout:
        """

    @classmethod
    def node_operator(
        cls,
        layout,
        node_type,
        *,
        label=None,
        poll=None,
        search_weight=0.0,
        translate=True,
    ) -> None:
        """The main operator defined for the node menu.(e.g. Add Node for AddNodeMenu, or Swap Node for SwapNodeMenu).

        :param layout:
        :param node_type:
        :param label:
        :param poll:
        :param search_weight:
        :param translate:
        """

    @classmethod
    def node_operator_with_outputs(
        cls, context, layout, node_type, subnames, *, label=None, search_weight=0.0
    ) -> None:
        """Similar to node_operator, but with extra entries based on a enum socket while in search.

        :param context:
        :param layout:
        :param node_type:
        :param subnames:
        :param label:
        :param search_weight:
        """

    @classmethod
    def node_operator_with_searchable_enum(
        cls, context, layout, node_idname, property_name, search_weight=0.0
    ) -> None:
        """Similar to node_operator, but with extra entries based on a enum property while in search.

        :param context:
        :param layout:
        :param node_idname:
        :param property_name:
        :param search_weight:
        """

    @classmethod
    def node_operator_with_searchable_enum_socket(
        cls,
        context,
        layout,
        node_idname,
        socket_identifier,
        enum_names,
        search_weight=0.0,
    ) -> None:
        """Similar to node_operator, but with extra entries based on a enum socket while in search.

        :param context:
        :param layout:
        :param node_idname:
        :param socket_identifier:
        :param enum_names:
        :param search_weight:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

    @classmethod
    def repeat_zone(cls, layout, label) -> None:
        """

        :param layout:
        :param label:
        """

    @classmethod
    def simulation_zone(cls, layout, label) -> None:
        """

        :param layout:
        :param label:
        """

class AddNodeMenu(NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

    bl_rna: typing.Any
    draw_assets: typing.Any
    id_data: typing.Any
    main_operator_id: typing.Any
    new_empty_group_operator_id: typing.Any
    root_asset_menu: typing.Any
    use_transform: typing.Any
    zone_operator_id: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    @classmethod
    def draw_assets_for_catalog(cls, layout, catalog_path) -> None:
        """

        :param layout:
        :param catalog_path:
        """

class NODE_MT_group_base(NodeMenu):
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

class NODE_MT_layout_base(NodeMenu):
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

class SwapNodeMenu(NodeMenu):
    """A base-class defining the shared methods for AddNodeMenu and SwapNodeMenu."""

    bl_rna: typing.Any
    draw_assets: typing.Any
    id_data: typing.Any
    main_operator_id: typing.Any
    new_empty_group_operator_id: typing.Any
    root_asset_menu: typing.Any
    zone_operator_id: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    @classmethod
    def draw_assets_for_catalog(cls, layout, catalog_path) -> None:
        """

        :param layout:
        :param catalog_path:
        """

def add_closure_zone(layout, label) -> None: ...
def add_color_mix_node(context, layout, search_weight=0.0) -> None: ...
def add_empty_group(layout) -> None: ...
def add_foreach_geometry_element_zone(layout, label) -> None: ...
def add_node_type(
    layout, node_type, *, label=None, poll=None, search_weight=0.0, translate=True
) -> None:
    """Add a node type to a menu."""

def add_node_type_with_outputs(
    context, layout, node_type, subnames, *, label=None, search_weight=0.0
) -> None: ...
def add_node_type_with_searchable_enum(
    context, layout, node_idname, property_name, search_weight=0.0
) -> None: ...
def add_node_type_with_searchable_enum_socket(
    context, layout, node_idname, socket_identifier, enum_names, search_weight=0.0
) -> None: ...
def add_repeat_zone(layout, label) -> None: ...
def add_simulation_zone(layout, label) -> None:
    """Add simulation zone to a menu."""

def draw_node_group_add_menu(context, layout) -> None:
    """Add items to the layout used for interacting with node groups."""

def generate_menu(bl_idname, template, layout_base, pathing_dict=None) -> None: ...
def generate_menus(menus, template, base_dict) -> None: ...
def generate_pathing_dict(pathing_dict, menus) -> None: ...
