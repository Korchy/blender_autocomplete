import sys
import typing


def code_from_builtin(shader_name: str) -> dict:
    ''' Exposes the internal shader code for query.

    :type shader_name: str
    :return: Vertex, fragment and geometry shader codes.
    '''

    pass


def from_builtin(shader_name: str):
    ''' Shaders that are embedded in the blender internal code. They all read the uniform 'mat4 ModelViewProjectionMatrix', which can be edited by the 'gpu.matrix' module. For more details, you can check the shader code with the function 'gpu.shader.code_from_builtin';

    :type shader_name: str
    :return: Shader object corresponding to the given name.
    '''

    pass


def unbind():
    ''' Unbind the bound shader object.

    '''

    pass
