import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.types

class BatchRenameAction(bpy.types.PropertyGroup):
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

class WM_MT_region_toggle_pie(bpy.types.Menu):
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

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class WM_MT_splash(bpy.types.Menu):
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

class WM_MT_splash_about(bpy.types.Menu):
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

class WM_MT_splash_quick_setup(bpy.types.Menu):
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

class WM_OT_batch_rename(bpy.types.Operator):
    """Rename multiple items at once"""

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

    def check(self, context) -> None:
        """

        :param context:
        """

    def draw(self, context) -> None:
        """

        :param context:
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

class WM_OT_context_collection_boolean_set(bpy.types.Operator):
    """Set boolean values for a collection of items"""

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

class WM_OT_context_cycle_array(bpy.types.Operator):
    """Set a context array value (useful for cycling the active mesh edit mode)"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_cycle_enum(bpy.types.Operator):
    """Toggle a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_cycle_int(bpy.types.Operator):
    """Set a context value (useful for cycling active material, shape keys, groups, etc.)"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_menu_enum(bpy.types.Operator):
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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_modal_mouse(bpy.types.Operator):
    """Adjust arbitrary values with mouse input"""

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

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    def modal(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

class WM_OT_context_pie_enum(bpy.types.Operator):
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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

class WM_OT_context_scale_float(bpy.types.Operator):
    """Scale a float context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_scale_int(bpy.types.Operator):
    """Scale an int context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_set_boolean(bpy.types.Operator):
    """Set a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

class WM_OT_context_set_enum(bpy.types.Operator):
    """Set a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

class WM_OT_context_set_float(bpy.types.Operator):
    """Set a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

class WM_OT_context_set_id(bpy.types.Operator):
    """Set a context value to an ID data-block"""

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

class WM_OT_context_set_int(bpy.types.Operator):
    """Set a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

class WM_OT_context_set_string(bpy.types.Operator):
    """Set a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

class WM_OT_context_set_value(bpy.types.Operator):
    """Set a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_toggle(bpy.types.Operator):
    """Toggle a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_context_toggle_enum(bpy.types.Operator):
    """Toggle a context value"""

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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_doc_view(bpy.types.Operator):
    """Open online reference docs in a web browser"""

    bl_idname: typing.Any
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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

class WM_OT_doc_view_manual(bpy.types.Operator):
    """Load online manual"""

    bl_idname: typing.Any
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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

class WM_OT_drop_blend_file(bpy.types.Operator):
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

    def draw_menu(self, menu, _context) -> None:
        """

        :param menu:
        :param _context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

class WM_OT_operator_cheat_sheet(bpy.types.Operator):
    """List all the operators in a text-block, useful for scripting"""

    bl_idname: typing.Any
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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

class WM_OT_operator_pie_enum(bpy.types.Operator):
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

    @classmethod
    def description(cls, context, props) -> None:
        """

        :param context:
        :param props:
        """

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

class WM_OT_owner_disable(bpy.types.Operator):
    """Disable add-on for workspace"""

    bl_idname: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_owner_enable(bpy.types.Operator):
    """Enable add-on for workspace"""

    bl_idname: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_path_open(bpy.types.Operator):
    """Open a path in a file browser"""

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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

class WM_OT_properties_add(bpy.types.Operator):
    """Add your own property to the data-block"""

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

class WM_OT_properties_context_change(bpy.types.Operator):
    """Jump to a different tab inside the properties editor"""

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

class WM_OT_properties_edit(bpy.types.Operator):
    """Change a custom propertys type, or adjust how it is displayed in the interface"""

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

    def check(self, context) -> None:
        """

        :param context:
        """

    @staticmethod
    def convert_custom_property_to_string(item, name) -> None:
        """

        :param item:
        :param name:
        """

    def draw(self, _context) -> None:
        """

        :param _context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    @staticmethod
    def get_property_id_type(item, property_name) -> None:
        """

        :param item:
        :param property_name:
        """

    @staticmethod
    def get_property_type(item, property_name) -> None:
        """

        :param item:
        :param property_name:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

    def property_type_update_cb(self, context) -> None:
        """

        :param context:
        """

    def subtype_items_cb(self, context) -> None:
        """

        :param context:
        """

class WM_OT_properties_edit_value(bpy.types.Operator):
    """Edit the value of a custom property"""

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

    def draw(self, context) -> None:
        """

        :param context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

class WM_OT_properties_remove(bpy.types.Operator):
    """Internal use (edit a property data_path)"""

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

class WM_OT_sysinfo(bpy.types.Operator):
    """Generate system information, saved into a text file"""

    bl_idname: typing.Any
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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

class WM_OT_tool_set_by_brush_type(bpy.types.Operator):
    """Look up the most appropriate tool for the given brush type and activate that"""

    bl_idname: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_tool_set_by_id(bpy.types.Operator):
    """Set the tool by name (for key-maps)"""

    bl_idname: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

    @staticmethod
    def space_type_from_operator(op, context) -> None:
        """

        :param op:
        :param context:
        """

class WM_OT_tool_set_by_index(bpy.types.Operator):
    """Set the tool by index (for key-maps)"""

    bl_idname: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

class WM_OT_toolbar(bpy.types.Operator):
    bl_idname: typing.Any
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

    def execute(self, context) -> None:
        """

        :param context:
        """

    @staticmethod
    def keymap_from_toolbar(
        context, space_type, *, use_fallback_keys=True, use_reset=True
    ) -> None:
        """

        :param context:
        :param space_type:
        :param use_fallback_keys:
        :param use_reset:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class WM_OT_toolbar_fallback_pie(bpy.types.Operator):
    bl_idname: typing.Any
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

class WM_OT_toolbar_prompt(bpy.types.Operator):
    """Leader key like functionality for accessing tools"""

    bl_idname: typing.Any
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

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    def modal(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

class WM_OT_url_open(bpy.types.Operator):
    """Open a website in the web browser"""

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

    def execute(self, _context) -> None:
        """

        :param _context:
        """

class WM_OT_url_open_preset(bpy.types.Operator):
    """Open a preset website in the web browser"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_property: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    preset_items: typing.Any

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

def context_path_decompose(data_path) -> None: ...
def context_path_to_rna_property(context, data_path) -> None: ...
def context_path_validate(context, data_path) -> None: ...
def description_from_data_path(base, data_path, *, prefix, value=Ellipsis) -> None: ...
def execute_context_assign(self_, context) -> None: ...
def operator_path_is_undo(context, data_path) -> None: ...
def operator_path_undo_return(context, data_path) -> None: ...
def operator_value_is_undo(value) -> None: ...
def operator_value_undo_return(value) -> None: ...
def rna_path_prop_search_for_context(self_, context, edit_text) -> None: ...
