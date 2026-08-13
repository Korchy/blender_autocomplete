import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class BrushAssetShelf:
    bl_activate_operator: typing.Any
    bl_options: typing.Any
    brush_type_prop: typing.Any
    filter_brush: typing.Any
    mode_prop: typing.Any

    @classmethod
    def asset_poll(cls, asset) -> None:
        """

        :param asset:
        """

    @classmethod
    def brush_type_poll(
        cls, context: bpy.types.Context, asset: bpy.types.AssetRepresentation
    ) -> bool:
        """Test if asset is compatible with the active tools brush type.

        :param context: The context.
        :param asset: Brush asset to test.
        :return: True when the assets brush type matches the active tool.
        """

    @classmethod
    def draw_context_menu(cls, context, asset, layout) -> None:
        """

        :param context:
        :param asset:
        :param layout:
        """

    @staticmethod
    def draw_popup_selector(
        layout: bpy.types.UILayout,
        context: bpy.types.Context,
        brush: None | bpy.types.Brush,
        show_name: bool = True,
    ) -> None:
        """Draw a brush asset-shelf popover into layout for the active paint mode.

        :param layout: Layout to draw into.
        :param context: The context.
        :param brush: Brush whose preview/name is shown on the button.
        :param show_name: Display the brush name next to the preview.
        """

    @classmethod
    def get_active_asset(cls) -> None: ...
    @staticmethod
    def get_shelf_name_from_context(context: bpy.types.Context) -> None | str:
        """Look up the brush asset-shelf identifier for the current paint mode.

        :param context: The context.
        :return: The asset-shelf bl_idname, or None when no paint mode is active.
        """

    @classmethod
    def has_tool_with_brush_type(
        cls, context: bpy.types.Context, brush_type: int
    ) -> bool:
        """Test if any tool active in the current space matches brush_type.

        :param context: The context.
        :param brush_type: Brush type identifier to match against tool brush types.
        :return: True when a registered tool uses this brush type.
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class UnifiedPaintPanel:
    @staticmethod
    def get_brush_mode(context) -> None:
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """

    @staticmethod
    def paint_settings(context) -> None:
        """

        :param context:
        """

    @staticmethod
    def prop_custom_pressure(
        layout,
        context,
        parent_row,
        brush,
        *,
        pressure_name,
        curve_visibility_name,
        custom_curve_name,
    ) -> None:
        """

        :param layout:
        :param context:
        :param parent_row:
        :param brush:
        :param pressure_name:
        :param curve_visibility_name:
        :param custom_curve_name:
        """

    @staticmethod
    def prop_unified(
        layout,
        context,
        brush,
        prop_name,
        unified_paint_settings_override=None,
        unified_name=None,
        pressure_name=None,
        text=None,
        slider=False,
        header=False,
    ) -> None:
        """Generalized way of adding brush options to the UI,
        along with their pen pressure setting and global toggle, if they exist.:param unified_paint_settings_override allows a caller to pass in a specific object for usage. Needed for
        some brush-like tools.

                :param layout:
                :param context:
                :param brush:
                :param prop_name:
                :param unified_paint_settings_override:
                :param unified_name:
                :param pressure_name:
                :param text:
                :param slider:
                :param header:
        """

    @staticmethod
    def prop_unified_color(parent, context, brush, prop_name, *, text=None) -> None:
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """

    @staticmethod
    def prop_unified_color_picker(
        parent, context, brush, prop_name, value_slider=True
    ) -> None:
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """

class VIEW3D_MT_tools_projectpaint_clone(_bpy_types.Menu):
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

class BrushPanel(UnifiedPaintPanel):
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class BrushSelectPanel(BrushPanel):
    bl_label: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header_preset(self, context) -> None:
        """

        :param context:
        """

class ClonePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class ColorPalettePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class DisplayPanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

class FalloffPanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class SmoothStrokePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_header(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class StrokePanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_ui_units_x: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

class TextureMaskPanel(BrushPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context) -> None:
        """

        :param context:
        """

def brush_asset_shelf_filter_draw(panel, context) -> None: ...
def brush_basic__draw_color_selector(context, layout, brush, gp_settings) -> None: ...
def brush_basic_grease_pencil_paint_settings(
    layout, context, brush, props, *, compact=False
) -> None: ...
def brush_basic_grease_pencil_vertex_settings(
    layout, context, brush, *, compact=False
) -> None: ...
def brush_basic_grease_pencil_weight_settings(
    layout, context, brush, *, compact=False
) -> None: ...
def brush_basic_texpaint_settings(layout, context, brush, *, compact=False) -> None:
    """Draw Tool Settings header for Vertex Paint and 2D and 3D Texture Paint modes."""

def brush_mask_texture_settings(layout, brush) -> None: ...
def brush_settings(layout, context, brush, popover=False) -> None:
    """Draw simple brush settings for Sculpt,
    Texture/Vertex/Weight Paint modes, or skip certain settings for the popover

    """

def brush_settings_advanced(layout, context, settings, brush, popover=False) -> None:
    """Draw advanced brush settings for Sculpt, Texture/Vertex/Weight Paint modes."""

def brush_shared_settings(layout, context, brush, popover=False) -> None:
    """Draw simple brush settings that are shared between different paint modes."""

def brush_texture_settings(layout, brush, sculpt) -> None: ...
def draw_auto_masking_panel(layout, brush) -> None: ...
def draw_color_jitter_panel(layout, context, brush) -> None: ...
def draw_color_settings(context, layout, brush, color_type=False) -> None:
    """Draw color wheel and gradient settings."""

def register() -> None: ...
def unregister() -> None: ...
