import typing
import collections.abc
import typing_extensions
import bpy.types

class WORLD_OT_convert_volume_to_mesh(bpy.types.Operator):
    """Convert the volume of a world to a mesh. The world's volume used to be rendered by EEVEE Legacy. Conversion is needed for it to render properly"""

    bl_idname: typing.Any
    bl_label: typing.Any
    bl_options: typing.Any
    bl_rna: typing.Any
    id_data: typing.Any

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

    def execute(self, context):
        """

        :param context:
        """

    @classmethod
    def poll(cls, context):
        """

        :param context:
        """
