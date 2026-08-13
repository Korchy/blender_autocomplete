import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class ASSET_OT_open_containing_blend_file(_bpy_types.Operator):
    """Open the blend file that contains the active asset"""

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

    def cancel(self, context) -> None:
        """

        :param context:
        """

    def execute(self, context) -> None:
        """

        :param context:
        """

    def modal(self, context, event) -> None:
        """

        :param context:
        :param event:
        """

    def open_in_new_blender(self, filepath) -> None:
        """

        :param filepath:
        """

    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """

class ASSET_OT_tag_add(AssetBrowserMetadataOperator, _bpy_types.Operator):
    """Add a new keyword tag to the active asset"""

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

class ASSET_OT_tag_remove(AssetBrowserMetadataOperator, _bpy_types.Operator):
    """Remove an existing keyword tag from the active asset"""

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

class AssetBrowserMetadataOperator:
    @classmethod
    def poll(cls, context) -> None:
        """

        :param context:
        """
