import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class AlignUVRotation(_bpy_types.Operator):
    """Align the UV islands rotation"""

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

    def draw(self, _context) -> None:
        """

        :param _context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class RandomizeUVTransform(_bpy_types.Operator):
    """Randomize the UV islands location, rotation, and scale"""

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

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

def align_uv_rotation(context, method, axis, correct_aspect) -> None: ...
def align_uv_rotation_bmesh(
    bm, method, axis, aspect_y, loop_edge_select_test_fn, face_select_test_fn
) -> None: ...
def align_uv_rotation_island(
    bm, uv_layer, faces, method, axis, aspect_y, loop_edge_select_test_fn
) -> None: ...
def find_rotation_auto(bm, uv_layer, faces, aspect_y) -> None: ...
def find_rotation_edge(
    bm, uv_layer, faces, aspect_y, loop_edge_select_test_fn
) -> None: ...
def find_rotation_geometry(bm, uv_layer, faces, axis, aspect_y) -> None: ...
def get_aspect_y(context) -> None: ...
def get_random_transform(transform_params, entropy) -> None: ...
def is_face_uv_selected_fn_from_context(scene, bm) -> None: ...
def is_face_uv_selected_for_uv_select_no_sync(face, any_edge) -> None: ...
def is_face_uv_selected_for_uv_select_sync_invalid(face, any_edge) -> None: ...
def is_face_uv_selected_for_uv_select_sync_valid(face, any_edge) -> None: ...
def is_island_uv_selected(island, any_edge, face_select_test_fn) -> None: ...
def is_loop_edge_uv_selected_fn_from_context(scene, bm) -> None: ...
def is_loop_edge_uv_selected_for_uv_select_no_sync(loop) -> None: ...
def is_loop_edge_uv_selected_for_uv_select_sync_invalid(loop) -> None: ...
def is_loop_edge_uv_selected_for_uv_select_sync_valid(loop) -> None: ...
def island_uv_bounds(island, uv_layer) -> None: ...
def island_uv_bounds_center(island, uv_layer) -> None: ...
def randomize_uv_transform(context, transform_params) -> None: ...
def randomize_uv_transform_bmesh(bm, transform_params, face_select_test_fn) -> None: ...
def randomize_uv_transform_island(uv_layer, faces, transform_params) -> None: ...
