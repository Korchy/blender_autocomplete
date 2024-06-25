import typing
import collections.abc
import bpy.types
import bpy_types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

class BoneConstraintPanel:
    bl_context: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class ConstraintButtonsPanel:
    bl_label: typing.Any
    bl_options: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
        """

        :param context:
        """
        ...

    def get_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
        """
        ...

class ConstraintButtonsSubPanel:
    bl_label: typing.Any
    bl_region_type: typing.Any
    bl_space_type: typing.Any

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
        """

        :param context:
        """
        ...

    def get_constraint(self, _context):
        """

        :param _context:
        """
        ...

class ObjectConstraintPanel:
    bl_context: typing.Any

    def poll(self, context):
        """

        :param context:
        """
        ...

class BONE_PT_constraints(bpy_types.Panel, BoneConstraintPanel, bpy_types._GenericUI):
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

class BONE_PT_bActionConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bArmatureConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bCameraSolverConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bChildOfConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bClampToConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bDampTrackConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bDistLimitConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bFollowPathConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bFollowTrackConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bKinematicConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bLocLimitConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bLocateLikeConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bLockTrackConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bMinMaxConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bObjectSolverConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bPivotConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bPythonConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bRotLimitConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bRotateLikeConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bSameVolumeConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bShrinkwrapConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bSizeLikeConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bSizeLimitConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bSplineIKConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bStretchToConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bTrackToConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bTransLikeConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bTransformCacheConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bTransformConstraint(
    bpy_types.Panel, BoneConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class BONE_PT_bActionConstraint_action(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bActionConstraint_target(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bArmatureConstraint_bones(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bSplineIKConstraint_chain_scaling(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bSplineIKConstraint_fitting(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bTransformCacheConstraint_layers(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bTransformCacheConstraint_procedural(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bTransformCacheConstraint_time(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bTransformCacheConstraint_velocity(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bTransformConstraint_from(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class BONE_PT_bTransformConstraint_to(
    bpy_types.Panel,
    BoneConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bActionConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bActionConstraint_action(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bActionConstraint_target(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bArmatureConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bArmatureConstraint_bones(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bCameraSolverConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bChildOfConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bClampToConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bDampTrackConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bDistLimitConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bFollowPathConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bFollowTrackConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bKinematicConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bLocLimitConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bLocateLikeConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bLockTrackConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bMinMaxConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bObjectSolverConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bPivotConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bPythonConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bRotLimitConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bRotateLikeConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bSameVolumeConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bShrinkwrapConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bSizeLikeConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bSizeLimitConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bStretchToConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bTrackToConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bTransLikeConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bTransformCacheConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bTransformCacheConstraint_layers(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bTransformCacheConstraint_procedural(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bTransformCacheConstraint_time(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bTransformCacheConstraint_velocity(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bTransformConstraint(
    bpy_types.Panel, ObjectConstraintPanel, ConstraintButtonsPanel, bpy_types._GenericUI
):
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

    def draw_action(self, context):
        """

        :param context:
        """
        ...

    def draw_armature(self, context):
        """

        :param context:
        """
        ...

    def draw_camera_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_childof(self, context):
        """

        :param context:
        """
        ...

    def draw_clamp_to(self, context):
        """

        :param context:
        """
        ...

    def draw_damp_track(self, context):
        """

        :param context:
        """
        ...

    def draw_dist_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_path(self, context):
        """

        :param context:
        """
        ...

    def draw_follow_track(self, context):
        """

        :param context:
        """
        ...

    def draw_header(self, context):
        """

        :param context:
        """
        ...

    def draw_influence(self, layout, con):
        """

        :param layout:
        :param con:
        """
        ...

    def draw_kinematic(self, context):
        """

        :param context:
        """
        ...

    def draw_loc_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_locate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_lock_track(self, context):
        """

        :param context:
        """
        ...

    def draw_min_max(self, context):
        """

        :param context:
        """
        ...

    def draw_object_solver(self, context):
        """

        :param context:
        """
        ...

    def draw_pivot(self, context):
        """

        :param context:
        """
        ...

    def draw_python_constraint(self, _context):
        """

        :param _context:
        """
        ...

    def draw_rot_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_rotate_like(self, context):
        """

        :param context:
        """
        ...

    def draw_same_volume(self, context):
        """

        :param context:
        """
        ...

    def draw_shrinkwrap(self, context):
        """

        :param context:
        """
        ...

    def draw_size_like(self, context):
        """

        :param context:
        """
        ...

    def draw_size_limit(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik(self, context):
        """

        :param context:
        """
        ...

    def draw_stretch_to(self, context):
        """

        :param context:
        """
        ...

    def draw_trackto(self, context):
        """

        :param context:
        """
        ...

    def draw_trans_like(self, context):
        """

        :param context:
        """
        ...

    def draw_transform(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

    def space_template(self, layout, con, target=True, owner=True, separator=True):
        """

        :param layout:
        :param con:
        :param target:
        :param owner:
        :param separator:
        """
        ...

    def target_template(self, layout, con, subtargets=True):
        """

        :param layout:
        :param con:
        :param subtargets:
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

class OBJECT_PT_bTransformConstraint_destination(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_bTransformConstraint_source(
    bpy_types.Panel,
    ObjectConstraintPanel,
    ConstraintButtonsSubPanel,
    bpy_types._GenericUI,
):
    bl_context: typing.Any
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

    def draw_action_action(self, context):
        """

        :param context:
        """
        ...

    def draw_action_target(self, context):
        """

        :param context:
        """
        ...

    def draw_armature_bones(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_chain_scaling(self, context):
        """

        :param context:
        """
        ...

    def draw_spline_ik_fitting(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_layers(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_procedural(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_subpanel(self, context, template_func):
        """

        :param context:
        :param template_func:
        """
        ...

    def draw_transform_cache_time(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_cache_velocity(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_from(self, context):
        """

        :param context:
        """
        ...

    def draw_transform_to(self, context):
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

    def get_constraint(self, _context):
        """

        :param _context:
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

class OBJECT_PT_constraints(
    bpy_types.Panel, ObjectConstraintPanel, bpy_types._GenericUI
):
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
