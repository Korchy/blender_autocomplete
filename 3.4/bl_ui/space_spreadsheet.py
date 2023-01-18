import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class SPREADSHEET_HT_header(bpy_types.Header, bpy_types._GenericUI):
    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
    ''' '''

    def append(self, draw_func):
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

    def draw(self, context):
        ''' 

        '''
        pass

    def draw_collapsed_viewer_path(self, context, layout, viewer_path):
        ''' 

        '''
        pass

    def draw_full_viewer_path(self, context, layout, viewer_path):
        ''' 

        '''
        pass

    def draw_spreadsheet_context(self, layout, ctx):
        ''' 

        '''
        pass

    def draw_spreadsheet_viewer_path_icon(self, layout, space, icon):
        ''' 

        '''
        pass

    def draw_without_viewer_path(self, layout):
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

    def is_extended(self):
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

    def prepend(self, draw_func):
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

    def remove(self, draw_func):
        ''' 

        '''
        pass

    def selection_filter_available(self, space):
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
