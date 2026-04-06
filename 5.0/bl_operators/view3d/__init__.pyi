import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class VIEW3D_FH_camera_background_image(_bpy_types.FileHandler):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
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

    @classmethod
    def poll_drop(cls, context) -> None:
        """

        :param context:
        """

class VIEW3D_FH_empty_image(_bpy_types.FileHandler):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
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

    @classmethod
    def poll_drop(cls, context) -> None:
        """

        :param context:
        """

class VIEW3D_FH_vdb_volume(_bpy_types.FileHandler):
    bl_file_extensions: typing.Any
    bl_idname: typing.Any
    bl_import_operator: typing.Any
    bl_label: typing.Any
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

    @classmethod
    def poll_drop(cls, context) -> None:
        """

        :param context:
        """

class VIEW3D_OT_edit_mesh_extrude_individual_move(_bpy_types.Operator):
    """Extrude each individual face separately along local normals"""

    bl_idname: typing.Any
    bl_label: typing.Any
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

class VIEW3D_OT_edit_mesh_extrude_manifold_normal(_bpy_types.Operator):
    """Extrude manifold region along normals"""

    bl_idname: typing.Any
    bl_label: typing.Any
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

class VIEW3D_OT_edit_mesh_extrude_move(_bpy_types.Operator):
    """Extrude region together along the average normal"""

    bl_idname: typing.Any
    bl_label: typing.Any
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

    @staticmethod
    def extrude_region(
        operator, context, use_vert_normals, dissolve_and_intersect
    ) -> None:
        """

        :param operator:
        :param context:
        :param use_vert_normals:
        :param dissolve_and_intersect:
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

class VIEW3D_OT_edit_mesh_extrude_shrink_fatten(_bpy_types.Operator):
    """Extrude region together along local normals"""

    bl_idname: typing.Any
    bl_label: typing.Any
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

class VIEW3D_OT_transform_gizmo_set(_bpy_types.Operator):
    """Set the current transform gizmo"""

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

    def invoke(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """
