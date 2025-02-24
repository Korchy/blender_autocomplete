import typing
import collections.abc
import typing_extensions
import bpy.types
import bpy_extras.io_utils
import bpy_extras.object_utils

class IMAGE_OT_convert_to_mesh_plane(
    TextureProperties_MixIn, MaterialProperties_MixIn, bpy.types.Operator
):
    """Convert selected reference images to textured mesh plane"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    t: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def draw(self, context):
        """

        :param context:
        """

    def execute(self, context):
        """

        :param context:
        """

    def invoke(self, context, _event):
        """

        :param context:
        :param _event:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """

class IMAGE_OT_import_as_mesh_planes(
    TextureProperties_MixIn,
    bpy_extras.io_utils.ImportHelper,
    bpy_extras.object_utils.AddObjectHelper,
    MaterialProperties_MixIn,
    bpy.types.Operator,
):
    """Create mesh plane(s) from image files with the appropriate aspect ratio"""

    AXIS_MODES: typing.Any
    axis_id_to_vector: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    t: typing.Any

    def align_plane(self, context, plane):
        """

        :param context:
        :param plane:
        """

    def apply_image_options(self, image):
        """

        :param image:
        """

    def apply_material_options(self, material, slot):
        """

        :param material:
        :param slot:
        """

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        :rtype: bpy.types.Struct
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        :rtype: typing.Any
        """

    def compute_plane_size(self, context, img_spec):
        """

        :param context:
        :param img_spec:
        """

    def create_image_plane(self, context, name, img_spec):
        """

        :param context:
        :param name:
        :param img_spec:
        """

    def draw(self, context):
        """

        :param context:
        """

    def draw_import_config(self, _context):
        """

        :param _context:
        """

    def draw_spatial_config(self, _context):
        """

        :param _context:
        """

    def execute(self, context):
        """

        :param context:
        """

    def import_images(self, context):
        """

        :param context:
        """

    def invoke(self, context, _event):
        """

        :param context:
        :param _event:
        """

    def single_image_spec_to_plane(self, context, img_spec):
        """

        :param context:
        :param img_spec:
        """

    def update_size_mode(self, _context):
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
    def draw_material_config(self, context):
        """

        :param context:
        """

class TextureProperties_MixIn:
    t: typing.Any

    def draw_texture_config(self, context):
        """

        :param context:
        """

def apply_texture_options(self_, texture, img_spec): ...
def auto_align_nodes(node_tree): ...
def center_in_camera(camera, ob, axis=(1, 1)): ...
def clean_node_tree(node_tree): ...
def compute_camera_size(context, center, fill_mode, aspect): ...
def create_cycles_material(self_, context, img_spec, name): ...
def create_cycles_texnode(self_, node_tree, img_spec): ...
def find_image_sequences(files): ...
def get_input_nodes(node, links): ...
def get_ref_object_space_coord(ob): ...
def get_shadeless_node(dest_node_tree): ...
def load_images(
    filenames, directory, force_reload=False, frame_start=1, find_sequences=False
): ...
def offset_planes(planes, gap, axis): ...
