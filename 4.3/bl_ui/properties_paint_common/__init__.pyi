import typing
import collections.abc
import typing_extensions
import bpy.types

class BrushAssetShelf:
    bl_activate_operator: typing.Any
    bl_default_preview_size: typing.Any
    bl_options: typing.Any
    brush_type_prop: typing.Any
    mode_prop: typing.Any
    tool_prop: typing.Any

    @classmethod
    def asset_poll(cls, asset):
        """

        :param asset:
        """

    @classmethod
    def brush_type_poll(cls, context, asset):
        """

        :param context:
        :param asset:
        """

    @classmethod
    def draw_context_menu(cls, context, asset, layout):
        """

        :param context:
        :param asset:
        :param layout:
        """

    @staticmethod
    def draw_popup_selector(layout, context, brush, show_name=True):
        """

        :param layout:
        :param context:
        :param brush:
        :param show_name:
        """

    @classmethod
    def get_active_asset(cls): ...
    @staticmethod
    def get_shelf_name_from_context(context):
        """

        :param context:
        """

    @classmethod
    def has_tool_with_brush_type(cls, context, brush_type):
        """

        :param context:
        :param brush_type:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class UnifiedPaintPanel:
    @staticmethod
    def get_brush_mode(context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """

    @staticmethod
    def paint_settings(context):
        """

        :param context:
        """

    @staticmethod
    def prop_unified(
        layout,
        context,
        brush,
        prop_name,
        unified_name=None,
        pressure_name=None,
        icon="NONE",
        text=None,
        slider=False,
        header=False,
    ):
        """Generalized way of adding brush options to the UI,
        along with their pen pressure setting and global toggle, if they exist.

                :param layout:
                :param context:
                :param brush:
                :param prop_name:
                :param unified_name:
                :param pressure_name:
                :param icon:
                :param text:
                :param slider:
                :param header:
        """

    @staticmethod
    def prop_unified_color(parent, context, brush, prop_name, *, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """

    @staticmethod
    def prop_unified_color_picker(parent, context, brush, prop_name, value_slider=True):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """

class VIEW3D_MT_tools_projectpaint_clone(bpy.types.Menu):
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

class VIEW3D_PT_brush_asset_shelf_filter(bpy.types.Panel):
    bl_label: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class BrushPanel(UnifiedPaintPanel):
    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class BrushSelectPanel(BrushPanel):
    bl_label: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header_preset(self, context):
        """

        :param context:
        """

class ClonePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class ColorPalettePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class DisplayPanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

class FalloffPanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class SmoothStrokePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

    def draw_header(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class StrokePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_ui_units_x: typing.Any

    def draw(self, context):
        """

        :param context:
        """

class TextureMaskPanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """

def brush_basic__draw_color_selector(context, layout, brush, gp_settings): ...
def brush_basic_gpencil_paint_settings(layout, context, brush, *, compact=False): ...
def brush_basic_gpencil_sculpt_settings(layout, _context, brush, *, compact=False): ...
def brush_basic_gpencil_vertex_settings(layout, _context, brush, *, compact=False): ...
def brush_basic_gpencil_weight_settings(layout, _context, brush, *, compact=False): ...
def brush_basic_grease_pencil_paint_settings(
    layout, context, brush, props, *, compact=False
): ...
def brush_basic_grease_pencil_vertex_settings(
    layout, context, brush, *, compact=False
): ...
def brush_basic_grease_pencil_weight_settings(
    layout, context, brush, *, compact=False
): ...
def brush_basic_texpaint_settings(layout, context, brush, *, compact=False):
    """Draw Tool Settings header for Vertex Paint and 2D and 3D Texture Paint modes."""

def brush_mask_texture_settings(layout, brush): ...
def brush_settings(layout, context, brush, popover=False):
    """Draw simple brush settings for Sculpt,
    Texture/Vertex/Weight Paint modes, or skip certain settings for the popover

    """

def brush_settings_advanced(layout, context, brush, popover=False):
    """Draw advanced brush settings for Sculpt, Texture/Vertex/Weight Paint modes."""

def brush_shared_settings(layout, context, brush, popover=False):
    """Draw simple brush settings that are shared between different paint modes."""

def brush_texture_settings(layout, brush, sculpt): ...
def draw_color_settings(context, layout, brush, color_type=False):
    """Draw color wheel and gradient settings."""
