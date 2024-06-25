"""
This module provides access to GPUShader internal functions.

Built-in shaders

All built-in shaders have the mat4 ModelViewProjectionMatrix

 uniform.

Its value must be modified using the gpu.matrix module.

FLAT_COLOR


    Attributes: vec3 pos, vec4 color
    Uniforms: none



IMAGE


    Attributes: vec3 pos, vec2 texCoord
    Uniforms: sampler2D image



IMAGE_COLOR


    Attributes: vec3 pos, vec2 texCoord
    Uniforms: sampler2D image, vec4 color



SMOOTH_COLOR


    Attributes: vec3 pos, vec4 color
    Uniforms: none



UNIFORM_COLOR


    Attributes: vec3 pos
    Uniforms: vec4 color



POLYLINE_FLAT_COLOR


    Attributes: vec3 pos, vec4 color
    Uniforms: vec2 viewportSize, float lineWidth



POLYLINE_SMOOTH_COLOR


    Attributes: vec3 pos, vec4 color
    Uniforms: vec2 viewportSize, float lineWidth



POLYLINE_UNIFORM_COLOR


    Attributes: vec3 pos
    Uniforms: vec2 viewportSize, float lineWidth



"""

import typing
import collections.abc

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def create_from_info(shader_info):
    """Create shader from a GPUShaderCreateInfo.

    :param shader_info: GPUShaderCreateInfo
    :return: Shader object corresponding to the given name.
    """

    ...

def from_builtin(shader_name: str, config: str = "DEFAULT"):
    """Shaders that are embedded in the blender internal code (see `built-in-shaders`).
    They all read the uniform mat4 ModelViewProjectionMatrix,
    which can be edited by the `gpu.matrix` module.You can also choose a shader configuration that uses clip_planes by setting the CLIPPED value to the config parameter. Note that in this case you also need to manually set the value of mat4 ModelMatrix.

        :param shader_name: One of the builtin shader names.
        :type shader_name: str
        :param config: One of these types of shader configuration:

    DEFAULT

    CLIPPED
        :type config: str
        :return: Shader object corresponding to the given name.
    """

    ...

def unbind():
    """Unbind the bound shader object."""

    ...
