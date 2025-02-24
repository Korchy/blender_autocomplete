import typing
import collections.abc
import typing_extensions
import bpy.types

from . import anim as anim
from . import asset_shelf as asset_shelf
from . import generic_ui_list as generic_ui_list
from . import node_add_menu as node_add_menu
from . import node_add_menu_compositor as node_add_menu_compositor
from . import node_add_menu_geometry as node_add_menu_geometry
from . import node_add_menu_shader as node_add_menu_shader
from . import node_add_menu_texture as node_add_menu_texture
from . import properties_animviz as properties_animviz
from . import properties_collection as properties_collection
from . import properties_constraint as properties_constraint
from . import properties_data_armature as properties_data_armature
from . import properties_data_bone as properties_data_bone
from . import properties_data_camera as properties_data_camera
from . import properties_data_curve as properties_data_curve
from . import properties_data_curves as properties_data_curves
from . import properties_data_empty as properties_data_empty
from . import properties_data_grease_pencil as properties_data_grease_pencil
from . import properties_data_lattice as properties_data_lattice
from . import properties_data_light as properties_data_light
from . import properties_data_lightprobe as properties_data_lightprobe
from . import properties_data_mesh as properties_data_mesh
from . import properties_data_metaball as properties_data_metaball
from . import properties_data_modifier as properties_data_modifier
from . import properties_data_pointcloud as properties_data_pointcloud
from . import properties_data_shaderfx as properties_data_shaderfx
from . import properties_data_speaker as properties_data_speaker
from . import properties_data_volume as properties_data_volume
from . import properties_freestyle as properties_freestyle
from . import properties_grease_pencil_common as properties_grease_pencil_common
from . import properties_mask_common as properties_mask_common
from . import properties_material as properties_material
from . import properties_material_gpencil as properties_material_gpencil
from . import properties_object as properties_object
from . import properties_output as properties_output
from . import properties_paint_common as properties_paint_common
from . import properties_particle as properties_particle
from . import properties_physics_cloth as properties_physics_cloth
from . import properties_physics_common as properties_physics_common
from . import properties_physics_dynamicpaint as properties_physics_dynamicpaint
from . import properties_physics_field as properties_physics_field
from . import properties_physics_fluid as properties_physics_fluid
from . import properties_physics_geometry_nodes as properties_physics_geometry_nodes
from . import properties_physics_rigidbody as properties_physics_rigidbody
from . import (
    properties_physics_rigidbody_constraint as properties_physics_rigidbody_constraint,
)
from . import properties_physics_softbody as properties_physics_softbody
from . import properties_render as properties_render
from . import properties_scene as properties_scene
from . import properties_texture as properties_texture
from . import properties_view_layer as properties_view_layer
from . import properties_workspace as properties_workspace
from . import properties_world as properties_world
from . import space_clip as space_clip
from . import space_console as space_console
from . import space_dopesheet as space_dopesheet
from . import space_filebrowser as space_filebrowser
from . import space_graph as space_graph
from . import space_image as space_image
from . import space_info as space_info
from . import space_nla as space_nla
from . import space_node as space_node
from . import space_outliner as space_outliner
from . import space_properties as space_properties
from . import space_sequencer as space_sequencer
from . import space_spreadsheet as space_spreadsheet
from . import space_statusbar as space_statusbar
from . import space_text as space_text
from . import space_time as space_time
from . import space_toolsystem_common as space_toolsystem_common
from . import space_toolsystem_toolbar as space_toolsystem_toolbar
from . import space_topbar as space_topbar
from . import space_userpref as space_userpref
from . import space_view3d as space_view3d
from . import space_view3d_toolbar as space_view3d_toolbar
from . import utils as utils

class UI_MT_button_context_menu(bpy.types.Menu):
    """UI button context menu definition. Scripts can append/prepend this to
    add own operators to the context menu. They must check context though, so
    their items only draw in a valid context and for the correct buttons.
    """

    bl_idname: typing.Any
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class UI_MT_list_item_context_menu(bpy.types.Menu):
    """UI List item context menu definition. Scripts can append/prepend this to
    add own operators to the context menu. They must check context though, so
    their items only draw in a valid context and for the correct UI list.
    """

    bl_idname: typing.Any
    bl_label: typing.Any
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

    def draw(self, context):
        """

        :param context:
        """

class UI_UL_list(bpy.types.UIList):
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self): ...
    def bl_rna_get_subclass_py(self): ...
    @staticmethod
    def filter_items_by_name(
        pattern, bitflag, items, propname="name", flags=None, reverse=False
    ):
        """

        :param pattern:
        :param bitflag:
        :param items:
        :param propname:
        :param flags:
        :param reverse:
        """

    @classmethod
    def sort_items_by_name(cls, items, propname="name"):
        """

        :param items:
        :param propname:
        """

    @staticmethod
    def sort_items_helper(sort_data, key, reverse=False):
        """

        :param sort_data:
        :param key:
        :param reverse:
        """

def register(): ...
def translation_update(_): ...
def unregister(): ...
