import sys
import typing

GenericType = typing.TypeVar("GenericType")


def compute_shader_support_get() -> bool:
    ''' Are compute shaders supported.

    :rtype: bool
    :return: True when supported, False when not supported.
    '''

    pass


def extensions_get() -> typing.Tuple:
    ''' Get supported extensions in the current context.

    :rtype: typing.Tuple
    :return: Extensions.
    '''

    pass


def max_batch_indices_get() -> int:
    ''' Get maximum number of vertex array indices.

    :rtype: int
    :return: Number of indices.
    '''

    pass


def max_batch_vertices_get() -> int:
    ''' Get maximum number of vertex array vertices.

    :rtype: int
    :return: Number of vertices.
    '''

    pass


def max_texture_layers_get() -> int:
    ''' Get maximum number of layers in texture.

    :rtype: int
    :return: Number of layers.
    '''

    pass


def max_texture_size_get() -> int:
    ''' Get estimated maximum texture size to be able to handle.

    :rtype: int
    :return: Texture size.
    '''

    pass


def max_textures_frag_get() -> int:
    ''' Get maximum supported texture image units used for accessing texture maps from the fragment shader.

    :rtype: int
    :return: Texture image units.
    '''

    pass


def max_textures_geom_get() -> int:
    ''' Get maximum supported texture image units used for accessing texture maps from the geometry shader.

    :rtype: int
    :return: Texture image units.
    '''

    pass


def max_textures_get() -> int:
    ''' Get maximum supported texture image units used for accessing texture maps from the vertex shader and the fragment processor.

    :rtype: int
    :return: Texture image units.
    '''

    pass


def max_textures_vert_get() -> int:
    ''' Get maximum supported texture image units used for accessing texture maps from the vertex shader.

    :rtype: int
    :return: Texture image units.
    '''

    pass


def max_uniforms_frag_get() -> int:
    ''' Get maximum number of values held in uniform variable storage for a fragment shader.

    :rtype: int
    :return: Number of values.
    '''

    pass


def max_uniforms_vert_get() -> int:
    ''' Get maximum number of values held in uniform variable storage for a vertex shader.

    :rtype: int
    :return: Number of values.
    '''

    pass


def max_varying_floats_get() -> int:
    ''' Get maximum number of varying variables used by vertex and fragment shaders.

    :rtype: int
    :return: Number of variables.
    '''

    pass


def max_vertex_attribs_get() -> int:
    ''' Get maximum number of vertex attributes accessible to a vertex shader.

    :rtype: int
    :return: Number of attributes.
    '''

    pass


def shader_image_load_store_support_get() -> bool:
    ''' Is image load/store supported.

    :rtype: bool
    :return: True when supported, False when not supported.
    '''

    pass


def shader_storage_buffer_objects_support_get() -> bool:
    ''' Are SSBO's supported.

    :rtype: bool
    :return: True when supported, False when not supported.
    '''

    pass
