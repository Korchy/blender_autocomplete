import sys
import typing

GenericType = typing.TypeVar("GenericType")


def create_from_info(shader_info):
    ''' Create shader from a GPUShaderCreateInfo.

    :param shader_info: GPUShaderCreateInfo
    :return: Shader object corresponding to the given name.
    '''

    pass


def from_builtin(shader_name: str, config: str = 'DEFAULT'):
    ''' Shaders that are embedded in the blender internal code (see :ref: built-in-shaders ). They all read the uniform mat4 ModelViewProjectionMatrix , which can be edited by the :mod: gpu.matrix module. You can also choose a shader configuration that uses clip_planes by setting the CLIPPED value to the config parameter. Note that in this case you also need to manually set the value of mat4 ModelMatrix .

    :param shader_name: One of the builtin shader names.
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
