import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class FixToCameraCommon:
    """Common functionality for the Fix To Scene Camera operator + its delete button."""

    keytype: typing.Any

    def execute(self, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

    @classmethod
    def poll_message_set(cls, message) -> None:
        """

        :param message:
        """

    def report(self, level, message) -> None:
        """

        :param level:
        :param message:
        """

class OBJECT_OT_copy_global_transform(_bpy_types.Operator):
    bl_description: typing.Any
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

class OBJECT_OT_copy_relative_transform(_bpy_types.Operator):
    bl_description: typing.Any
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

class OBJECT_OT_fix_to_camera(FixToCameraCommon, _bpy_types.Operator):
    """Common functionality for the Fix To Scene Camera operator + its delete button."""

    bl_description: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    keytype: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class OBJECT_OT_paste_transform(_bpy_types.Operator):
    bl_description: typing.Any
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

    @staticmethod
    def parse_matrix(value) -> None:
        """

        :param value:
        """

    @staticmethod
    def parse_print_m4(value) -> None:
        """Parse output from Blenders print_m4() function.Expects four lines of space-separated floats.

        :param value:
        """

    @staticmethod
    def parse_repr_m4(value) -> None:
        """Four lines of (a, b, c, d) floats.

        :param value:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

    @classmethod
    def string_to_matrix(cls, value) -> None:
        """

        :param value:
        """

class Transformable:
    """Interface for a bone or an object."""

    def key_info(self) -> None: ...
    def matrix_world(self) -> None: ...
    def remove_keys_of_type(self, key_type, *, frame_start=None, frame_end=inf) -> None:
        """

        :param key_type:
        :param frame_start:
        :param frame_end:
        """

    def set_matrix_world(self, context, matrix) -> None:
        """Set the world matrix, without auto-keying.

        :param context:
        :param matrix:
        """

    def set_matrix_world_autokey(self, context, matrix) -> None:
        """Set the world matrix, and auto-key the resulting transform.

        :param context:
        :param matrix:
        """

class UnableToMirrorError:
    """Raised when mirroring is enabled but no mirror object/bone is set."""

    args: typing.Any

class OBJECT_OT_delete_fix_to_camera_keys(_bpy_types.Operator, FixToCameraCommon):
    """Common functionality for the Fix To Scene Camera operator + its delete button."""

    bl_description: typing.Any
    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any
    keytype: typing.Any

    def bl_rna_get_subclass(self) -> bpy.types.Struct:
        """

        :return: The RNA type or default when not found.
        """

    def bl_rna_get_subclass_py(self) -> typing.Any:
        """

        :return: The class or default when not found.
        """

class TransformableBone(Transformable):
    """Interface for a bone or an object."""

    def matrix_world(self) -> None: ...

class TransformableObject(Transformable):
    """Interface for a bone or an object."""

    def matrix_world(self) -> None: ...

def get_matrix(context) -> None: ...
def get_relative_ob(context) -> None:
    """Get the relative object.This is the object thats configured, or if thats empty, the active scene camera."""

def register() -> None: ...
def set_matrix(context, mat) -> None: ...
def unregister() -> None: ...
