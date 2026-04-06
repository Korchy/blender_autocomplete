import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types
import bpy_extras.io_utils
import bpy_extras.object_utils

class IMAGE_OT_convert_to_mesh_plane(
    TextureProperties_MixIn, MaterialProperties_MixIn, _bpy_types.Operator
):
    """Convert selected reference images to textured mesh plane"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def draw(self, context) -> None:
        """

        :param context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class IMAGE_OT_import_as_mesh_planes(
    TextureProperties_MixIn,
    bpy_extras.io_utils.ImportHelper,
    bpy_extras.object_utils.AddObjectHelper,
    MaterialProperties_MixIn,
    _bpy_types.Operator,
):
    """Create mesh plane(s) from image files with the appropriate aspect ratio"""

    AXIS_MODES: typing.Any
    axis_id_to_vector: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

    def align_plane(self, context, plane) -> None:
        """

        :param context:
        :param plane:
        """

    def apply_image_options(self, image) -> None:
        """

        :param image:
        """

    def apply_material_options(self, material, slot) -> None:
        """

        :param material:
        :param slot:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

    def compute_plane_size(self, context, img_spec) -> None:
        """

        :param context:
        :param img_spec:
        """

    def create_image_plane(self, context, name, img_spec) -> None:
        """

        :param context:
        :param name:
        :param img_spec:
        """

    def draw(self, context) -> None:
        """

        :param context:
        """

    def draw_import_config(self, _context) -> None:
        """

        :param _context:
        """

    def draw_spatial_config(self, _context) -> None:
        """

        :param _context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    def import_images(self, context) -> None:
        """

        :param context:
        """

    def invoke(self, context, _event) -> None:
        """

        :param context:
        :param _event:
        """

    def single_image_spec_to_plane(self, context, img_spec) -> None:
        """

        :param context:
        :param img_spec:
        """

    def update_size_mode(self, _context) -> None:
        """

        :param _context:
        """

class ImageSpec:
    """ImageSpec(image, size, frame_start, frame_offset, frame_duration)"""

    frame_duration: typing.Any
    frame_offset: typing.Any
    frame_start: typing.Any
    image: typing.Any
    size: typing.Any

class MaterialProperties_MixIn:
    def draw_material_config(self, context) -> None:
        """

        :param context:
        """

class TextureProperties_MixIn:
    def draw_texture_config(self, context) -> None:
        """

        :param context:
        """

def apply_texture_options(self_, texture, img_spec) -> None: ...
def auto_align_nodes(node_tree) -> None: ...
def center_in_camera(camera, ob, axis=(1, 1)) -> None: ...
def clean_node_tree(node_tree) -> None: ...
def compute_camera_size(context, center, fill_mode, aspect) -> None: ...
def create_cycles_material(self_, context, img_spec, name) -> None: ...
def create_cycles_texnode(self_, node_tree, img_spec) -> None: ...
def find_image_sequences(files) -> None: ...
def get_input_nodes(node, links) -> None: ...
def get_ref_object_space_coord(ob) -> None: ...
def get_shadeless_node(dest_node_tree) -> None: ...
def load_images(
    filenames, directory, force_reload=False, frame_start=1, find_sequences=False
) -> None: ...
def offset_planes(planes, gap, axis) -> None: ...
