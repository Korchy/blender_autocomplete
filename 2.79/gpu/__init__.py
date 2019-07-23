import sys
import typing
import bpy

from . import offscreen

CD_MCOL = None
'''There can be more than one attribute of that type, they are differenciated by name. In blender you can retrieve the attribute data with: '''

CD_MTFACE = None
'''There can be more than one attribute of that type, they are differenciated by name. In blender, you can retrieve the attribute data with: '''

CD_ORCO = None
'''There can be only 1 attribute of that type per shader. In blender you can retrieve the attribute data with: '''

CD_TANGENT = None
'''There can be only 1 attribute of that type per shader. There is currently no way to retrieve this attribute data via the RNA API but a standalone C function to compute the tangent layer from the other layers can be obtained from blender.org. '''

GPU_DATA_16F = None
'''matrix 4x4 in column-major order '''

GPU_DATA_1F = None
'''one float '''

GPU_DATA_1I = None
'''one integer '''

GPU_DATA_2F = None
'''two floats '''

GPU_DATA_3F = None
'''three floats '''

GPU_DATA_4F = None
'''four floats '''

GPU_DATA_4UB = None
'''four unsigned byte '''

GPU_DATA_9F = None
'''matrix 3x3 in column-major order '''

GPU_DYNAMIC_AMBIENT_COLOR = None
'''See bpy.types.World.ambient_color. '''

GPU_DYNAMIC_HORIZON_COLOR = None
'''See bpy.types.World.horizon_color. '''

GPU_DYNAMIC_LAMP_ATT1: float = None
'''See bpy.types.PointLamp.linear_attenuation, bpy.types.SpotLamp.linear_attenuation. '''

GPU_DYNAMIC_LAMP_ATT2: float = None
'''See bpy.types.PointLamp.quadratic_attenuation, bpy.types.SpotLamp.quadratic_attenuation. '''

GPU_DYNAMIC_LAMP_DISTANCE: float = None
'''See bpy.types.Lamp.distance. '''

GPU_DYNAMIC_LAMP_DYNCO = None
'''Represents the position of the light in camera space. '''

GPU_DYNAMIC_LAMP_DYNCOL = None
'''See bpy.types.Lamp.color. '''

GPU_DYNAMIC_LAMP_DYNENERGY: float = None
'''See bpy.types.Lamp.energy. '''

GPU_DYNAMIC_LAMP_DYNIMAT = None
'''Matrix that converts vector in camera space to lamp space. '''

GPU_DYNAMIC_LAMP_DYNPERSMAT = None
'''mat4_perspective_to_depth is a fixed matrix defined as follow: '''

GPU_DYNAMIC_LAMP_DYNVEC = None
'''Represents the direction of light in camera space. '''

GPU_DYNAMIC_LAMP_SPOTBLEND: float = None
'''See bpy.types.SpotLamp.spot_blend. '''

GPU_DYNAMIC_LAMP_SPOTSCALE = None
'''Represents the SpotLamp local scale. '''

GPU_DYNAMIC_LAMP_SPOTSIZE: float = None
'''See bpy.types.SpotLamp.spot_size. '''

GPU_DYNAMIC_MAT_ALPHA: float = None
'''See bpy.types.Material.alpha. '''

GPU_DYNAMIC_MAT_AMB: float = None
'''See bpy.types.Material.ambient. '''

GPU_DYNAMIC_MAT_DIFFRGB = None
'''See bpy.types.Material.diffuse_color. '''

GPU_DYNAMIC_MAT_EMIT: float = None
'''See bpy.types.Material.emit. '''

GPU_DYNAMIC_MAT_HARD: float = None
'''See bpy.types.Material.specular_hardness. '''

GPU_DYNAMIC_MAT_REF: float = None
'''See bpy.types.Material.diffuse_intensity. '''

GPU_DYNAMIC_MAT_SPEC: float = None
'''See bpy.types.Material.specular_intensity. '''

GPU_DYNAMIC_MAT_SPECRGB = None
'''See bpy.types.Material.specular_color. '''

GPU_DYNAMIC_MIST_COLOR = None

GPU_DYNAMIC_MIST_DISTANCE: float = None
'''See bpy.types.WorldMistSettings.intensity. '''

GPU_DYNAMIC_MIST_ENABLE: float = None
'''See bpy.types.WorldMistSettings.use_mist. '''

GPU_DYNAMIC_MIST_INTENSITY: float = None

GPU_DYNAMIC_MIST_START: float = None
'''See bpy.types.WorldMistSettings.depth. '''

GPU_DYNAMIC_MIST_TYPE: float = None
'''See bpy.types.WorldMistSettings.falloff. '''

GPU_DYNAMIC_OBJECT_AUTOBUMPSCALE: float = None
'''Multiplier for bump-map scaling. '''

GPU_DYNAMIC_OBJECT_COLOR = None
'''See bpy.types.Object.color. '''

GPU_DYNAMIC_OBJECT_IMAT = None
'''The uniform is a 4x4 GL matrix that converts world coodinates to object coordinates (see mat4_world_to_object). '''

GPU_DYNAMIC_OBJECT_MAT = None
'''A matrix that converts object coordinates to world coordinates (see mat4_object_to_world). '''

GPU_DYNAMIC_OBJECT_VIEWIMAT = None
'''The uniform is a 4x4 GL matrix that converts coordinates in camera space to world coordinates (see mat4_cam_to_world). '''

GPU_DYNAMIC_OBJECT_VIEWMAT = None
'''A matrix that converts world coordinates to camera coordinates (see mat4_world_to_cam). '''

GPU_DYNAMIC_SAMPLER_2DBUFFER = None
'''Represents an internal texture used for certain effect (color band, etc). '''

GPU_DYNAMIC_SAMPLER_2DIMAGE = None
'''Represents a texture loaded from an image file. '''

GPU_DYNAMIC_SAMPLER_2DSHADOW = None
'''Represents a texture loaded from a shadow buffer file. '''


def export_shader(scene: 'bpy.types.Scene', material: 'bpy.types.Material'):
    '''Example: 

    :param scene: the scene in which the material in rendered. 
    :type scene: 'bpy.types.Scene'
    :param material: the material that you want to export the GLSL shader 
    :type material: 'bpy.types.Material'
    :return:  the shader source code and all associated data in a dictionary 
    '''

    pass
