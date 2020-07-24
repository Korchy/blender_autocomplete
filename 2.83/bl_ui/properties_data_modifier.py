import sys
import typing
import bpy_types


class ModifierButtonsPanel:
    bl_context = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_space_type = None
    ''' '''


class DATA_PT_gpencil_modifiers(ModifierButtonsPanel, bpy_types.Panel,
                                bpy_types._GenericUI):
    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
    ''' '''

    def GP_ARMATURE(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_ARRAY(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_BUILD(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_COLOR(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_HOOK(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_LATTICE(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_MIRROR(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_MULTIPLY(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_NOISE(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_OFFSET(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_OPACITY(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_SIMPLIFY(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_SMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_SUBDIV(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_THICK(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_TIME(self, layout, ob, md):
        ''' 

        '''
        pass

    def GP_TINT(self, layout, ob, md):
        ''' 

        '''
        pass

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

    def check_conflicts(self, layout, ob):
        ''' 

        '''
        pass

    def draw(self, context):
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

    def gpencil_masking(self, layout, ob, md, use_vertex, use_curve):
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

    def poll(self, context):
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

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass


class DATA_PT_modifiers(ModifierButtonsPanel, bpy_types.Panel,
                        bpy_types._GenericUI):
    bl_context = None
    ''' '''

    bl_label = None
    ''' '''

    bl_options = None
    ''' '''

    bl_region_type = None
    ''' '''

    bl_rna = None
    ''' '''

    bl_space_type = None
    ''' '''

    id_data = None
    ''' '''

    def ARMATURE(self, layout, ob, md):
        ''' 

        '''
        pass

    def ARRAY(self, layout, _ob, md):
        ''' 

        '''
        pass

    def BEVEL(self, layout, ob, md):
        ''' 

        '''
        pass

    def BOOLEAN(self, layout, _ob, md):
        ''' 

        '''
        pass

    def BUILD(self, layout, _ob, md):
        ''' 

        '''
        pass

    def CAST(self, layout, ob, md):
        ''' 

        '''
        pass

    def CLOTH(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def COLLISION(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def CORRECTIVE_SMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def CURVE(self, layout, ob, md):
        ''' 

        '''
        pass

    def DATA_TRANSFER(self, layout, ob, md):
        ''' 

        '''
        pass

    def DECIMATE(self, layout, ob, md):
        ''' 

        '''
        pass

    def DISPLACE(self, layout, ob, md):
        ''' 

        '''
        pass

    def DYNAMIC_PAINT(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def EDGE_SPLIT(self, layout, _ob, md):
        ''' 

        '''
        pass

    def EXPLODE(self, layout, ob, md):
        ''' 

        '''
        pass

    def FLUID(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def FLUID_SIMULATION(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def HOOK(self, layout, ob, md):
        ''' 

        '''
        pass

    def LAPLACIANDEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def LAPLACIANSMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def LATTICE(self, layout, ob, md):
        ''' 

        '''
        pass

    def MASK(self, layout, ob, md):
        ''' 

        '''
        pass

    def MESH_CACHE(self, layout, _ob, md):
        ''' 

        '''
        pass

    def MESH_DEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def MESH_SEQUENCE_CACHE(self, layout, ob, md):
        ''' 

        '''
        pass

    def MIRROR(self, layout, _ob, md):
        ''' 

        '''
        pass

    def MULTIRES(self, layout, ob, md):
        ''' 

        '''
        pass

    def NORMAL_EDIT(self, layout, ob, md):
        ''' 

        '''
        pass

    def OCEAN(self, layout, _ob, md):
        ''' 

        '''
        pass

    def PARTICLE_INSTANCE(self, layout, ob, md):
        ''' 

        '''
        pass

    def PARTICLE_SYSTEM(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def REMESH(self, layout, _ob, md):
        ''' 

        '''
        pass

    def SCREW(self, layout, _ob, md):
        ''' 

        '''
        pass

    def SHRINKWRAP(self, layout, ob, md):
        ''' 

        '''
        pass

    def SIMPLE_DEFORM(self, layout, ob, md):
        ''' 

        '''
        pass

    def SKIN(self, layout, _ob, md):
        ''' 

        '''
        pass

    def SMOOTH(self, layout, ob, md):
        ''' 

        '''
        pass

    def SOFT_BODY(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def SOLIDIFY(self, layout, ob, md):
        ''' 

        '''
        pass

    def SUBSURF(self, layout, ob, md):
        ''' 

        '''
        pass

    def SURFACE(self, layout, _ob, _md):
        ''' 

        '''
        pass

    def SURFACE_DEFORM(self, layout, _ob, md):
        ''' 

        '''
        pass

    def TRIANGULATE(self, layout, _ob, md):
        ''' 

        '''
        pass

    def UV_PROJECT(self, layout, ob, md):
        ''' 

        '''
        pass

    def UV_WARP(self, layout, ob, md):
        ''' 

        '''
        pass

    def VERTEX_WEIGHT_EDIT(self, layout, ob, md):
        ''' 

        '''
        pass

    def VERTEX_WEIGHT_MIX(self, layout, ob, md):
        ''' 

        '''
        pass

    def VERTEX_WEIGHT_PROXIMITY(self, layout, ob, md):
        ''' 

        '''
        pass

    def WARP(self, layout, ob, md):
        ''' 

        '''
        pass

    def WAVE(self, layout, ob, md):
        ''' 

        '''
        pass

    def WEIGHTED_NORMAL(self, layout, ob, md):
        ''' 

        '''
        pass

    def WELD(self, layout, ob, md):
        ''' 

        '''
        pass

    def WIREFRAME(self, layout, ob, md):
        ''' 

        '''
        pass

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

    def poll(self, context):
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

    def type_recast(self):
        ''' 

        '''
        pass

    def values(self):
        ''' 

        '''
        pass

    def vertex_weight_mask(self, layout, ob, md):
        ''' 

        '''
        pass
