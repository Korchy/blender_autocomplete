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
        """Pick an axis and align the plane to it

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
        """Given the image size in pixels and location, determine size of plane

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
        """If sizing relative to the camera, always face the camera

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
def auto_align_nodes(node_tree):
    """Given a shader node tree, arrange nodes neatly relative to the output node."""

def center_in_camera(camera, ob, axis=(1, 1)):
    """Center object along specified axis of the camera"""

def clean_node_tree(node_tree):
    """Clear all nodes in a shader node tree except the output.Returns the output node"""

def compute_camera_size(context, center, fill_mode, aspect):
    """Determine how large an object needs to be to fit or fill the camera's field of view."""

def create_cycles_material(self_, context, img_spec, name): ...
def create_cycles_texnode(self_, node_tree, img_spec): ...
def find_image_sequences(files):
    """From a group of files, detect image sequences.This returns a generator of tuples, which contain the filename,
    start frame, and length of the detected sequence

    """

def get_input_nodes(node, links):
    """Get nodes that are a inputs to the given node"""

def get_ref_object_space_coord(ob): ...
def get_shadeless_node(dest_node_tree):
    """Return a "shadeless" cycles/EEVEE node, creating a node group if nonexistent"""

def load_images(
    filenames, directory, force_reload=False, frame_start=1, find_sequences=False
):
    """Wrapper for bpy_extras.image_utils.load_image.Loads a set of images, movies, or even image sequences
    Returns a generator of ImageSpec wrapper objects later used for texture setup

    """

def offset_planes(planes, gap, axis):
    """Offset planes from each other by gap amount along a _local_ vector axisFor example, offset_planes([obj1, obj2], 0.5, Vector(0, 0, 1)) will place
    obj2 0.5 blender units away from obj1 along the local positive Z axis.This is in local space, not world space, so all planes should share
    a common scale and rotation.

    """
