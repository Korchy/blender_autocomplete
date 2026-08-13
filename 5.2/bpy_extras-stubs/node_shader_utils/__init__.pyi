import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

class ShaderWrapper:
    """Base class with minimal common ground for all types of shader interfaces we may want/need to implement."""

    NODES_LIST: typing.Any
    is_readonly: typing.Any
    material: typing.Any
    node_out: typing.Any
    node_texcoords: typing.Any

    def node_texcoords_get(self) -> None: ...
    def update(self) -> None: ...

class ShaderImageTextureWrapper:
    """Generic image texture-like wrapper, handling image node, some mapping (texture coordinates transformations),
    and texture coordinates source.
    """

    NODES_LIST: typing.Any
    colorspace_is_data: typing.Any
    colorspace_name: typing.Any
    extension: typing.Any
    grid_row_diff: typing.Any
    image: typing.Any
    is_readonly: typing.Any
    node_dst: typing.Any
    node_image: typing.Any
    node_mapping: typing.Any
    owner_shader: typing.Any
    projection: typing.Any
    rotation: typing.Any
    scale: typing.Any
    socket_dst: typing.Any
    texcoords: typing.Any
    translation: typing.Any
    use_alpha: typing.Any

    def copy_from(self, tex) -> None:
        """

        :param tex:
        """

    def copy_mapping_from(self, tex) -> None:
        """

        :param tex:
        """

    def extension_get(self) -> None: ...
    def extension_set(self, extension) -> None:
        """

        :param extension:
        """

    def has_mapping_node(self) -> None: ...
    def image_get(self) -> None: ...
    def image_set(self, image) -> None:
        """

        :param image:
        """

    def node_image_get(self) -> None: ...
    def node_mapping_get(self) -> None: ...
    def projection_get(self) -> None: ...
    def projection_set(self, projection) -> None:
        """

        :param projection:
        """

    def rotation_get(self) -> None: ...
    def rotation_set(self, rotation) -> None:
        """

        :param rotation:
        """

    def scale_get(self) -> None: ...
    def scale_set(self, scale) -> None:
        """

        :param scale:
        """

    def texcoords_get(self) -> None: ...
    def texcoords_set(self, texcoords) -> None:
        """

        :param texcoords:
        """

    def translation_get(self) -> None: ...
    def translation_set(self, translation) -> None:
        """

        :param translation:
        """

class PrincipledBSDFWrapper(ShaderWrapper):
    """Hard coded shader setup, based in Principled BSDF.
    Should cover most common cases on import, and gives a basic nodal shaders support for export.
    Supports basic: diffuse/spec/reflect/transparency/normal, with texturing.
    """

    NODES_LIST: typing.Any
    alpha: typing.Any
    alpha_texture: typing.Any
    base_color: typing.Any
    base_color_texture: typing.Any
    emission_color: typing.Any
    emission_color_texture: typing.Any
    emission_strength: typing.Any
    emission_strength_texture: typing.Any
    ior: typing.Any
    ior_texture: typing.Any
    is_readonly: typing.Any
    material: typing.Any
    metallic: typing.Any
    metallic_texture: typing.Any
    node_normalmap: typing.Any
    node_out: typing.Any
    node_principled_bsdf: typing.Any
    node_texcoords: typing.Any
    normalmap_strength: typing.Any
    normalmap_texture: typing.Any
    roughness: typing.Any
    roughness_texture: typing.Any
    specular: typing.Any
    specular_texture: typing.Any
    specular_tint: typing.Any
    specular_tint_texture: typing.Any
    transmission: typing.Any
    transmission_texture: typing.Any

    def alpha_get(self) -> None: ...
    def alpha_set(self, value) -> None:
        """

        :param value:
        """

    def alpha_texture_get(self) -> None: ...
    def base_color_get(self) -> None: ...
    def base_color_set(self, color) -> None:
        """

        :param color:
        """

    def base_color_texture_get(self) -> None: ...
    def emission_color_get(self) -> None: ...
    def emission_color_set(self, color) -> None:
        """

        :param color:
        """

    def emission_color_texture_get(self) -> None: ...
    def emission_strength_get(self) -> None: ...
    def emission_strength_set(self, value) -> None:
        """

        :param value:
        """

    def emission_strength_texture_get(self) -> None: ...
    def ior_get(self) -> None: ...
    def ior_set(self, value) -> None:
        """

        :param value:
        """

    def ior_texture_get(self) -> None: ...
    def metallic_get(self) -> None: ...
    def metallic_set(self, value) -> None:
        """

        :param value:
        """

    def metallic_texture_get(self) -> None: ...
    def node_normalmap_get(self) -> None: ...
    def normalmap_strength_get(self) -> None: ...
    def normalmap_strength_set(self, value) -> None:
        """

        :param value:
        """

    def normalmap_texture_get(self) -> None: ...
    def roughness_get(self) -> None: ...
    def roughness_set(self, value) -> None:
        """

        :param value:
        """

    def roughness_texture_get(self) -> None: ...
    def specular_get(self) -> None: ...
    def specular_set(self, value) -> None:
        """

        :param value:
        """

    def specular_texture_get(self) -> None: ...
    def specular_tint_get(self) -> None: ...
    def specular_tint_set(self, color) -> None:
        """

        :param color:
        """

    def specular_tint_texture_get(self) -> None: ...
    def transmission_get(self) -> None: ...
    def transmission_set(self, value) -> None:
        """

        :param value:
        """

    def transmission_texture_get(self) -> None: ...
    def update(self) -> None: ...

def node_input_value_get(node, input, default_value=None) -> None: ...
def node_input_value_set(node, input, value) -> None: ...
def rgb_to_rgba(rgb) -> None: ...
def rgba_to_rgb(rgba) -> None: ...
def values_clamp(val, minv, maxv) -> None: ...
