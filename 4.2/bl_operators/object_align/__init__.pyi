import typing
import collections.abc
import typing_extensions
import bpy.types

class AlignObjects(bpy.types.Operator):
    """Align objects"""

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

def align_objects(
    context, align_x, align_y, align_z, align_mode, relative_to, bb_quality
): ...
def worldspace_bounds_from_object_bounds(bb_world): ...
def worldspace_bounds_from_object_data(depsgraph, obj): ...
