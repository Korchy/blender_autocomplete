import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class VertexPaintDirt(_bpy_types.Operator):
    """Generate a dirt map gradient based on cavity"""

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

def applyVertexDirt(
    me, blur_iterations, blur_strength, clamp_dirt, clamp_clean, dirt_only, normalize
) -> None: ...
def ensure_active_color_attribute(me) -> None: ...
