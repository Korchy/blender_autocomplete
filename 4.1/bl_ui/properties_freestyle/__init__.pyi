import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class MaterialFreestyleButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class RENDER_MT_lineset_context_menu(bpy_types.Menu, bpy_types._GenericUI):
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

    def draw(self, _context):
        """

        :param _context:
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

class RenderFreestyleButtonsPanel:
    bl_context: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class ViewLayerFreestyleButtonsPanel:
    bl_context: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class VIEWLAYER_UL_linesets(bpy_types.UIList, bpy_types._GenericUI):
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

    def draw_item(
        self, _context, layout, _data, item, icon, _active_data, _active_propname, index
    ):
        """

        :param _context:
        :param layout:
        :param _data:
        :param item:
        :param icon:
        :param _active_data:
        :param _active_propname:
        :param index:
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

class MATERIAL_PT_freestyle_line(
    bpy_types.Panel, MaterialFreestyleButtonsPanel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class RENDER_PT_freestyle(
    bpy_types.Panel, RenderFreestyleButtonsPanel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle(
    bpy_types.Panel, ViewLayerFreestyleButtonsPanel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_edge_detection(
    bpy_types.Panel, ViewLayerFreestyleButtonsPanel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_style_modules(
    bpy_types.Panel, ViewLayerFreestyleButtonsPanel, bpy_types._GenericUI
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class ViewLayerFreestyleEditorButtonsPanel(ViewLayerFreestyleButtonsPanel):
    bl_context: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class VIEWLAYER_PT_freestyle_lineset(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_edge_type_buttons(self, box, lineset, edge_type):
        """

        :param box:
        :param lineset:
        :param edge_type:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class ViewLayerFreestyleLineStyle(
    ViewLayerFreestyleEditorButtonsPanel, ViewLayerFreestyleButtonsPanel
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class VIEWLAYER_PT_freestyle_lineset_collection(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_lineset_edgetype(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_edge_type_buttons(self, box, lineset, edge_type):
        """

        :param box:
        :param lineset:
        :param edge_type:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_lineset_facemarks(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_lineset_visibilty(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_alpha(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_alpha_modifier(self, context, modifier):
        """

        :param context:
        :param modifier:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_color(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_color_modifier(self, context, modifier):
        """

        :param context:
        :param modifier:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_geometry(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_geometry_modifier(self, _context, modifier):
        """

        :param _context:
        :param modifier:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_strokes(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_texture(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_thickness(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_thickness_modifier(self, context, modifier):
        """

        :param context:
        :param modifier:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class ViewLayerFreestyleLinestyleStrokesSubPanel(
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class VIEWLAYER_PT_freestyle_linestyle_strokes_chaining(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLinestyleStrokesSubPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_strokes_dashedline(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLinestyleStrokesSubPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_strokes_selection(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLinestyleStrokesSubPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_strokes_sorting(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLinestyleStrokesSubPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_strokes_splitting(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLinestyleStrokesSubPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

class VIEWLAYER_PT_freestyle_linestyle_strokes_splitting_pattern(
    bpy_types.Panel,
    ViewLayerFreestyleEditorButtonsPanel,
    ViewLayerFreestyleLinestyleStrokesSubPanel,
    ViewLayerFreestyleLineStyle,
    ViewLayerFreestyleButtonsPanel,
    bpy_types._GenericUI,
):
    COMPAT_ENGINES: typing.Any
    bl_context: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_order: typing.Any
    bl_parent_id: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
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

    def path_resolve(self):
        """Returns the property from the path, raise an exception when not found."""
        ...

    def poll(self, context):
        """

        :param context:
        """
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

def draw_modifier_box_error(box, _modifier, message): ...
def draw_modifier_box_header(box, modifier): ...
def draw_modifier_color_ramp_common(box, modifier, has_range): ...
def draw_modifier_common(box, modifier): ...
def draw_modifier_curve_common(box, modifier, has_range, has_value): ...
