import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def bake(execution_context: int | str | None = None, undo: bool | None = None):
    """Bake dynamic paint image sequence surface

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def output_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    output: typing.Literal["A", "B"] | None = "A",
):
    """Add or remove Dynamic Paint output data layer

    :type execution_context: int | str | None
    :type undo: bool | None
    :param output: Output Toggle
    :type output: typing.Literal['A','B'] | None
    """

def surface_slot_add(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Add a new Dynamic Paint surface slot

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def surface_slot_remove(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Remove the selected surface slot

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def type_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy._typing.rna_enums.PropDynamicpaintTypeItems | None = "CANVAS",
):
    """Toggle whether given type is active or not

    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy._typing.rna_enums.PropDynamicpaintTypeItems | None
    """
