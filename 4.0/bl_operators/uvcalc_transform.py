import sys
import typing
import bpy_types

GenericType = typing.TypeVar("GenericType")


class AlignUVRotation(bpy_types.Operator):
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

    def draw(self, _context):
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


class RandomizeUVTransform(bpy_types.Operator):
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


def align_uv_rotation(context, method, axis, correct_aspect):
    ''' 

    '''

    pass


def align_uv_rotation_bmesh(mesh, bm, method, axis, aspect_y):
    ''' 

    '''

    pass


def align_uv_rotation_island(bm, uv_layer, faces, method, axis, aspect_y):
    ''' 

    '''

    pass


def find_rotation_auto(bm, uv_layer, faces, aspect_y):
    ''' 

    '''

    pass


def find_rotation_edge(bm, uv_layer, faces, aspect_y):
    ''' 

    '''

    pass


def find_rotation_geometry(bm, uv_layer, faces, method, axis, aspect_y):
    ''' 

    '''

    pass


def get_aspect_y(context):
    ''' 

    '''

    pass


def get_random_transform(transform_params, entropy):
    ''' 

    '''

    pass


def is_face_uv_selected(face, uv_layer, any_edge):
    ''' 

    '''

    pass


def is_island_uv_selected(island, uv_layer, any_edge):
    ''' 

    '''

    pass


def island_uv_bounds(island, uv_layer):
    ''' 

    '''

    pass


def island_uv_bounds_center(island, uv_layer):
    ''' 

    '''

    pass


def randomize_uv_transform(context, transform_params):
    ''' 

    '''

    pass


def randomize_uv_transform_bmesh(mesh, bm, transform_params):
    ''' 

    '''

    pass


def randomize_uv_transform_island(bm, uv_layer, faces, transform_params):
    ''' 

    '''

    pass
