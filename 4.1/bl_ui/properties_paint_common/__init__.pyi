import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class UnifiedPaintPanel:
    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class VIEW3D_MT_tools_projectpaint_clone(bpy_types.Menu, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def append(self, draw_func):
        """Append a draw function to this menu,
        takes the same arguments as the menus draw function

                :param draw_func:
        """
        ...

    def as_pointer(self) -> int:
        """Returns the memory address which holds a pointer to Blender's internal data

        :return: int (memory address).
        :rtype: int
        """
        ...

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """
        ...

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """
        ...

    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_collapsible(self, context, layout):
        """

        :param context:
        :param layout:
        """
        ...

    def draw_preset(self, _context):
        """Define these on the subclass:
        - preset_operator (string)
        - preset_subdir (string)Optionally:
        - preset_add_operator (string)
        - preset_extensions (set of strings)
        - preset_operator_defaults (dict of keyword args)

                :param _context:
        """
        ...

    def driver_add(self) -> bpy.types.FCurve:
        """Adds driver(s) to the given property

        :return: The driver(s) added.
        :rtype: bpy.types.FCurve
        """
        ...

    def driver_remove(self) -> bool:
        """Remove driver(s) from the given property

        :return: Success of driver removal.
        :rtype: bool
        """
        ...

    def get(self):
        """Returns the value of the custom property assigned to key or default
        when not found (matches Python's dictionary function of the same name).

        """
        ...

    def id_properties_clear(self):
        """

        :return: Remove the parent group for an RNA struct's custom IDProperties.
        """
        ...

    def id_properties_ensure(self):
        """

        :return: the parent group for an RNA struct's custom IDProperties.
        """
        ...

    def id_properties_ui(self):
        """

        :return: Return an object used to manage an IDProperty's UI data.
        """
        ...

    def is_extended(self): ...
    def is_property_hidden(self) -> bool:
        """Check if a property is hidden.

        :return: True when the property is hidden.
        :rtype: bool
        """
        ...

    def is_property_overridable_library(self) -> bool:
        """Check if a property is overridable.

        :return: True when the property is overridable.
        :rtype: bool
        """
        ...

    def is_property_readonly(self) -> bool:
        """Check if a property is readonly.

        :return: True when the property is readonly (not writable).
        :rtype: bool
        """
        ...

    def is_property_set(self) -> bool:
        """Check if a property is set, use for testing operator properties.

        :return: True when the property has been set.
        :rtype: bool
        """
        ...

    def items(self):
        """Returns the items of this objects custom properties (matches Python's
        dictionary function of the same name).

                :return: custom property key, value pairs.
        """
        ...

    def keyframe_delete(self) -> bool:
        """Remove a keyframe from this properties fcurve.

        :return: Success of keyframe deletion.
        :rtype: bool
        """
        ...

    def keyframe_insert(self) -> bool:
        """Insert a keyframe on the property given, adding fcurves and animation data when necessary.

        :return: Success of keyframe insertion.
        :rtype: bool
        """
        ...

    def keys(self):
        """Returns the keys of this objects custom properties (matches Python's
        dictionary function of the same name).

                :return: custom property keys.
        """
        ...

    def path_from_id(self) -> str:
        """Returns the data path from the ID to this object (string).

                :return: The path from `bpy.types.bpy_struct.id_data`
        to this struct and property (when given).
                :rtype: str
        """
        ...

    def path_menu(
        self,
        searchpaths: list[str],
        operator: str,
        props_default: dict = None,
        prop_filepath: str | None = "filepath",
        filter_ext: collections.abc.Callable | None = None,
        filter_path=None,
        display_name: collections.abc.Callable | None = None,
        add_operator=None,
    ):
        """Populate a menu from a list of paths.

                :param searchpaths: Paths to scan.
                :type searchpaths: list[str]
                :param operator: The operator id to use with each file.
                :type operator: str
                :param props_default: Properties to assign to each operator.
                :type props_default: dict
                :param prop_filepath: Optional operator filepath property (defaults to "filepath").
                :type prop_filepath: str | None
                :param filter_ext: Optional callback that takes the file extensions.

        Returning false excludes the file from the list.
                :type filter_ext: collections.abc.Callable | None
                :param filter_path:
                :param display_name: Optional callback that takes the full path, returns the name to display.
                :type display_name: collections.abc.Callable | None
                :param add_operator:
        """
        ...

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def pop(self):
        """Remove and return the value of the custom property assigned to key or default
        when not found (matches Python's dictionary function of the same name).

        """
        ...

    def prepend(self, draw_func):
        """Prepend a draw function to this menu, takes the same arguments as
        the menus draw function

                :param draw_func:
        """
        ...

    def property_overridable_library_set(self) -> bool:
        """Define a property as overridable or not (only for custom properties!).

        :return: True when the overridable status of the property was successfully set.
        :rtype: bool
        """
        ...

    def property_unset(self):
        """Unset a property, will use default value afterward."""
        ...

    def remove(self, draw_func):
        """Remove a draw function that has been added to this menu

        :param draw_func:
        """
        ...

    def type_recast(self):
        """Return a new instance, this is needed because types
        such as textures can be changed at runtime.

                :return: a new instance of this object with the type initialized again.
        """
        ...

    def values(self):
        """Returns the values of this objects custom properties (matches Python's
        dictionary function of the same name).

                :return: custom property values.
        """
        ...

class BrushPanel(UnifiedPaintPanel):
    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class BrushSelectPanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class ClonePanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class ColorPalettePanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class DisplayPanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class FalloffPanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class SmoothStrokePanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class StrokePanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_ui_units_x: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

class TextureMaskPanel(BrushPanel, UnifiedPaintPanel):
    bl_label: typing.Any
    bl_options: typing.Any

    def draw(self, context):
        """

        :param context:
        """
        ...

    def get_brush_mode(self, context):
        """Get the correct mode for this context. For any context where this returns None,
        no brush options should be displayed.

                :param context:
        """
        ...

    def paint_settings(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

    def prop_unified(
        self,
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
        ...

    def prop_unified_color(self, parent, context, brush, prop_name, text=None):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param text:
        """
        ...

    def prop_unified_color_picker(
        self, parent, context, brush, prop_name, value_slider=True
    ):
        """

        :param parent:
        :param context:
        :param brush:
        :param prop_name:
        :param value_slider:
        """
        ...

def brush_basic__draw_color_selector(context, layout, brush, gp_settings, props): ...
def brush_basic_gpencil_paint_settings(layout, context, brush, compact=False): ...
def brush_basic_gpencil_sculpt_settings(layout, _context, brush, compact=False): ...
def brush_basic_gpencil_vertex_settings(layout, _context, brush, compact=False): ...
def brush_basic_gpencil_weight_settings(layout, _context, brush, compact=False): ...
def brush_basic_texpaint_settings(layout, context, brush, compact=False):
    """Draw Tool Settings header for Vertex Paint and 2D and 3D Texture Paint modes."""

    ...

def brush_mask_texture_settings(layout, brush): ...
def brush_settings(layout, context, brush, popover=False):
    """Draw simple brush settings for Sculpt,
    Texture/Vertex/Weight Paint modes, or skip certain settings for the popover

    """

    ...

def brush_settings_advanced(layout, context, brush, popover=False):
    """Draw advanced brush settings for Sculpt, Texture/Vertex/Weight Paint modes."""

    ...

def brush_shared_settings(layout, context, brush, popover=False):
    """Draw simple brush settings that are shared between different paint modes."""

    ...

def brush_texture_settings(layout, brush, sculpt): ...
def draw_color_settings(context, layout, brush, color_type=False):
    """Draw color wheel and gradient settings."""

    ...
