import sys
import typing


def code_from_builtin(pygpu_shader_name: str) -> dict:
    ''' Exposes the internal shader code for consultation.

    :param pygpu_shader_name: - 2D_FLAT_COLOR - 2D_IMAGE - 2D_SMOOTH_COLOR - 2D_UNIFORM_COLOR - 3D_FLAT_COLOR - 3D_SMOOTH_COLOR - 3D_UNIFORM_COLOR - 3D_POLYLINE_FLAT_COLOR - 3D_POLYLINE_SMOOTH_COLOR - 3D_POLYLINE_UNIFORM_COLOR
    :type pygpu_shader_name: str
    :rtype: dict
    :return: Vertex, fragment and geometry shader codes.
    '''

    pass


def from_builtin(shader_name: str, config: str = 'DEFAULT'):
    ''' Shaders that are embedded in the blender internal code. They all read the uniform mat4 ModelViewProjectionMatrix , which can be edited by the :mod: gpu.matrix module. You can also choose a shader configuration that uses clip_planes by setting the CLIPPED value to the config parameter. Note that in this case you also need to manually set the value of mat4 ModelMatrix . For more details, you can check the shader code with the :func: gpu.shader.code_from_builtin function.

    :param shader_name: - 2D_FLAT_COLOR - 2D_IMAGE - 2D_SMOOTH_COLOR - 2D_UNIFORM_COLOR - 3D_FLAT_COLOR - 3D_SMOOTH_COLOR - 3D_UNIFORM_COLOR - 3D_POLYLINE_FLAT_COLOR - 3D_POLYLINE_SMOOTH_COLOR - 3D_POLYLINE_UNIFORM_COLOR
    :type shader_name: str
    :param config: - DEFAULT - CLIPPED
    :type config: str
    :return: Shader object corresponding to the given name.
    '''

    pass


def unbind():
    ''' Unbind the bound shader object.

    '''

    pass
