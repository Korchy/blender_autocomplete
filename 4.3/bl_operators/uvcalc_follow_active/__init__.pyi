import typing
import collections.abc
import typing_extensions
import bpy.types

class FollowActiveQuads(bpy.types.Operator):
    """Follow UVs from active quads along continuous face loops"""

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

def extend(obj, EXTEND_MODE, use_uv_selection): ...
def main(context, operator): ...
