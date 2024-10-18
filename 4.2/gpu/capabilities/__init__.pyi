"""
This module provides access to the GPU capabilities.

"""

import typing
import collections.abc
import typing_extensions

def compute_shader_support_get() -> bool:
    """Are compute shaders supported.

    :return: True when supported, False when not supported.
    :rtype: bool
    """

def extensions_get():
    """Get supported extensions in the current context.

    :return: Extensions.
    """

def hdr_support_get() -> bool:
    """Return whether GPU backend supports High Dynamic range for viewport.

    :return: HDR support available.
    :rtype: bool
    """

def max_batch_indices_get() -> int:
    """Get maximum number of vertex array indices.

    :return: Number of indices.
    :rtype: int
    """

def max_batch_vertices_get() -> int:
    """Get maximum number of vertex array vertices.

    :return: Number of vertices.
    :rtype: int
    """

def max_images_get() -> int:
    """Get maximum supported number of image units.

    :return: Number of image units.
    :rtype: int
    """

def max_texture_layers_get() -> int:
    """Get maximum number of layers in texture.

    :return: Number of layers.
    :rtype: int
    """

def max_texture_size_get() -> int:
    """Get estimated maximum texture size to be able to handle.

    :return: Texture size.
    :rtype: int
    """

def max_textures_frag_get() -> int:
    """Get maximum supported texture image units used for
    accessing texture maps from the fragment shader.

        :return: Texture image units.
        :rtype: int
    """

def max_textures_geom_get() -> int:
    """Get maximum supported texture image units used for
    accessing texture maps from the geometry shader.

        :return: Texture image units.
        :rtype: int
    """

def max_textures_get() -> int:
    """Get maximum supported texture image units used for
    accessing texture maps from the vertex shader and the
    fragment processor.

        :return: Texture image units.
        :rtype: int
    """

def max_textures_vert_get() -> int:
    """Get maximum supported texture image units used for
    accessing texture maps from the vertex shader.

        :return: Texture image units.
        :rtype: int
    """

def max_uniforms_frag_get() -> int:
    """Get maximum number of values held in uniform variable
    storage for a fragment shader.

        :return: Number of values.
        :rtype: int
    """

def max_uniforms_vert_get() -> int:
    """Get maximum number of values held in uniform variable
    storage for a vertex shader.

        :return: Number of values.
        :rtype: int
    """

def max_varying_floats_get() -> int:
    """Get maximum number of varying variables used by
    vertex and fragment shaders.

        :return: Number of variables.
        :rtype: int
    """

def max_vertex_attribs_get() -> int:
    """Get maximum number of vertex attributes accessible to
    a vertex shader.

        :return: Number of attributes.
        :rtype: int
    """

def max_work_group_count_get(index: int) -> int:
    """Get maximum number of work groups that may be dispatched to a compute shader.

    :param index: Index of the dimension.
    :type index: int
    :return: Maximum number of work groups for the queried dimension.
    :rtype: int
    """

def max_work_group_size_get(index: int) -> int:
    """Get maximum size of a work group that may be dispatched to a compute shader.

    :param index: Index of the dimension.
    :type index: int
    :return: Maximum size of a work group for the queried dimension.
    :rtype: int
    """

def shader_image_load_store_support_get() -> bool:
    """Is image load/store supported.

    :return: True when supported, False when not supported.
    :rtype: bool
    """
