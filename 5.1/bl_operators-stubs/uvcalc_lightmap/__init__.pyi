import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import _bpy_types
import bpy.types

class LightMapPack(_bpy_types.Operator):
    """Pack each faces UVs into the UV bounds"""

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

    def draw(self, context) -> None:
        """

        :param context:
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

class prettyface:
    children: typing.Any
    has_parent: typing.Any
    height: typing.Any
    rot: typing.Any
    uv: typing.Any
    width: typing.Any
    xoff: typing.Any
    yoff: typing.Any

    def place(self, xoff, yoff, xfac, yfac, margin_w, margin_h) -> None:
        """

        :param xoff:
        :param yoff:
        :param xfac:
        :param yfac:
        :param margin_w:
        :param margin_h:
        """

    def spin(self) -> None: ...

def lightmap_uvpack(
    meshes,
    PREF_SEL_ONLY=True,
    PREF_NEW_UVLAYER=False,
    PREF_PACK_IN_ONE=False,
    PREF_BOX_DIV=8,
    PREF_MARGIN_DIV=512,
) -> None:
    """BOX_DIV if the maximum division of the UV map that
    a box may be consolidated into.
    A lower value will create more clumpy boxes and more wasted space,
    and a higher value will be slower but waste less space

    """

def unwrap(operator, context, **kwargs) -> None: ...
