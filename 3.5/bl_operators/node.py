import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class NODE_OT_collapse_hide_unused_toggle(bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass_py(self):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def id_properties_clear(self):
        ''' 

        '''
        pass

    def id_properties_ensure(self):
        ''' 

        '''
        pass

    def id_properties_ui(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_overridable_library(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
        ''' 

        '''
        pass

    def poll_message_set(self):
        ''' 

        '''
        pass

    def pop(self):
        ''' 

        '''
        pass

    def property_overridable_library_set(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class NODE_OT_tree_path_parent(bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass_py(self):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def id_properties_clear(self):
        ''' 

        '''
        pass

    def id_properties_ensure(self):
        ''' 

        '''
        pass

    def id_properties_ui(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_overridable_library(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
        ''' 

        '''
        pass

    def poll_message_set(self):
        ''' 

        '''
        pass

    def pop(self):
        ''' 

        '''
        pass

    def property_overridable_library_set(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class NodeAddOperator:
    def create_node(self, context, node_type):
        ''' 

        '''
        pass

    def description(self, _context, properties):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def poll(self, context):
        ''' 

        '''
        pass

    def store_mouse_cursor(self, context, event):
        ''' 

        '''
        pass


class NodeSetting(bpy_types.PropertyGroup):
    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    def as_pointer(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass_py(self):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def id_properties_clear(self):
        ''' 

        '''
        pass

    def id_properties_ensure(self):
        ''' 

        '''
        pass

    def id_properties_ui(self):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_overridable_library(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def pop(self):
        ''' 

        '''
        pass

    def property_overridable_library_set(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class NODE_OT_add_node(NodeAddOperator, bpy_types.Operator):
    bl_idname = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_rna = None
    ''' '''

    id_data = None
    ''' '''

    def as_keywords(self, ignore):
        ''' 

        '''
        pass

    def as_pointer(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass(self):
        ''' 

        '''
        pass

    def bl_rna_get_subclass_py(self):
        ''' 

        '''
        pass

    def create_node(self, context, node_type):
        ''' 

        '''
        pass

    def description(self, _context, properties):
        ''' 

        '''
        pass

    def driver_add(self):
        ''' 

        '''
        pass

    def driver_remove(self):
        ''' 

        '''
        pass

    def execute(self, context):
        ''' 

        '''
        pass

    def get(self):
        ''' 

        '''
        pass

    def id_properties_clear(self):
        ''' 

        '''
        pass

    def id_properties_ensure(self):
        ''' 

        '''
        pass

    def id_properties_ui(self):
        ''' 

        '''
        pass

    def invoke(self, context, event):
        ''' 

        '''
        pass

    def is_property_hidden(self):
        ''' 

        '''
        pass

    def is_property_overridable_library(self):
        ''' 

        '''
        pass

    def is_property_readonly(self):
        ''' 

        '''
        pass

    def is_property_set(self):
        ''' 

        '''
        pass

    def items(self):
        ''' 

        '''
        pass

    def keyframe_delete(self):
        ''' 

        '''
        pass

    def keyframe_insert(self):
        ''' 

        '''
        pass

    def keys(self):
        ''' 

        '''
        pass

    def path_from_id(self):
        ''' 

        '''
        pass

    def path_resolve(self):
        ''' 

        '''
        pass

    def poll(self, context):
        ''' 

        '''
        pass

    def poll_message_set(self):
        ''' 

        '''
        pass

    def pop(self):
        ''' 

        '''
        pass

    def property_overridable_library_set(self):
        ''' 

        '''
        pass

    def property_unset(self):
        ''' 

        '''
        pass

    def store_mouse_cursor(self, context, event):
        ''' 

        '''
        pass

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass
