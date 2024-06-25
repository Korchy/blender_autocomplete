import typing
import collections.abc
import bl_ui.properties_grease_pencil_common
import bl_ui.space_toolsystem_common
import bpy.types
import bpy_types
import rna_prop_ui

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class SEQUENCER_HT_header(bpy_types.Header, bpy_types._GenericUI):
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

class SEQUENCER_HT_tool_header(bpy_types.Header, bpy_types._GenericUI):
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

    def draw_tool_settings(self, context):
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

class SEQUENCER_MT_add(bpy_types.Menu, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class SEQUENCER_MT_add_effect(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_add_empty(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_add_scene(bpy_types.Menu, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class SEQUENCER_MT_add_transitions(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_change(bpy_types.Menu, bpy_types._GenericUI):
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

class SequencerColorTagPicker:
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def has_sequencer(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

class SEQUENCER_MT_context_menu(bpy_types.Menu, bpy_types._GenericUI):
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

    def draw_generic(self, context):
        """

        :param context:
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

    def draw_retime(self, context):
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

class SEQUENCER_MT_editor_menus(bpy_types.Menu, bpy_types._GenericUI):
    bl_idname: typing.Any
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

class SEQUENCER_MT_image(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_image_apply(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_image_clear(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_image_transform(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_marker(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_navigation(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_pivot_pie(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_preview_context_menu(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_preview_view_pie(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_preview_zoom(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_proxy(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_range(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_retiming(bpy_types.Menu, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_rna: typing.Any
    bl_translation_context: typing.Any
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

class SEQUENCER_MT_select(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_select_channel(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_select_handle(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_select_linked(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip_effect(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip_input(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip_lock_mute(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip_movie(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip_retiming(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_strip_transform(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_view(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_view_cache(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_MT_view_pie(bpy_types.Menu, bpy_types._GenericUI):
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

class SEQUENCER_PT_active_tool(
    bpy_types.Panel,
    bl_ui.space_toolsystem_common.ToolActivePanelHelper,
    bpy_types._GenericUI,
):
    bl_category: typing.Any
    bl_label: typing.Any
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

class SequencerButtonsPanel:
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def has_sequencer(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

class SequencerButtonsPanel_Output:
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def has_preview(self, context):
        """

        :param context:
        """
        ...

    def poll(self, context):
        """

        :param context:
        """
        ...

class SEQUENCER_PT_gizmo_display(bpy_types.Panel, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class SEQUENCER_PT_overlay(bpy_types.Panel, bpy_types._GenericUI):
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_rna: typing.Any
    bl_space_type: typing.Any
    bl_ui_units_x: typing.Any
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

class SEQUENCER_PT_preview_overlay(bpy_types.Panel, bpy_types._GenericUI):
    bl_label: typing.Any
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

class SEQUENCER_PT_sequencer_overlay(bpy_types.Panel, bpy_types._GenericUI):
    bl_label: typing.Any
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

class SEQUENCER_PT_snapping(bpy_types.Panel, bpy_types._GenericUI):
    bl_label: typing.Any
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

class SEQUENCER_MT_color_tag_picker(
    bpy_types.Menu, SequencerColorTagPicker, bpy_types._GenericUI
):
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_color_tag_picker(
    bpy_types.Panel, SequencerColorTagPicker, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def draw(self, _context):
        """

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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_adjust_color(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_adjust_comp(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_adjust_crop(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_adjust_sound(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_adjust_transform(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_adjust_video(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_cache_settings(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_custom_props(
    bpy_types.Panel,
    SequencerButtonsPanel,
    rna_prop_ui.PropertyPanel,
    bpy_types._GenericUI,
):
    """The subclass should have its own poll function
    and the variable '_context_path' MUST be set.
    """

    COMPAT_ENGINES: typing.Any
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_effect(bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_effect_text_layout(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_effect_text_style(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_mask(bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_modifiers(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_proxy_settings(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_scene(bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_scene_sound(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_source(bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_strip(bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_strip_cache(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_strip_proxy(
    bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_time(bpy_types.Panel, SequencerButtonsPanel, bpy_types._GenericUI):
    bl_category: typing.Any
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

    def draw_header_preset(self, context):
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

    def has_sequencer(self, context):
        """

        :param context:
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

class SEQUENCER_PT_annotation(
    bpy_types.Panel,
    bl_ui.properties_grease_pencil_common.AnnotationDataPanel,
    SequencerButtonsPanel_Output,
    bpy_types._GenericUI,
):
    bl_category: typing.Any
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

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_layers(self, context, layout, gpd):
        """

        :param context:
        :param layout:
        :param gpd:
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_annotation_onion(
    bpy_types.Panel,
    bl_ui.properties_grease_pencil_common.AnnotationOnionSkin,
    SequencerButtonsPanel_Output,
    bpy_types._GenericUI,
):
    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_frame_overlay(
    bpy_types.Panel, SequencerButtonsPanel_Output, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_preview(
    bpy_types.Panel, SequencerButtonsPanel_Output, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_view(
    bpy_types.Panel, SequencerButtonsPanel_Output, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_view_cursor(
    bpy_types.Panel, SequencerButtonsPanel_Output, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_view_safe_areas(
    bpy_types.Panel, SequencerButtonsPanel_Output, bpy_types._GenericUI
):
    bl_category: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

class SEQUENCER_PT_view_safe_areas_center_cut(
    bpy_types.Panel, SequencerButtonsPanel_Output, bpy_types._GenericUI
):
    bl_category: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
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

    def has_preview(self, context):
        """

        :param context:
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

def draw_color_balance(layout, color_balance): ...
def selected_sequences_len(context): ...
