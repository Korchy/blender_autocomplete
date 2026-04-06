import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def bake(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bake dynamic paint image sequence surface"""

def output_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    output: typing.Literal["A", "B"] | None = "A",
) -> None:
    """Add or remove Dynamic Paint output data layer

    :param output: Output Toggle
    """

def surface_slot_add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new Dynamic Paint surface slot"""

def surface_slot_remove(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove the selected surface slot"""

def type_toggle(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: bpy.stub_internal.rna_enums.PropDynamicpaintTypeItems | None = "CANVAS",
) -> None:
    """Toggle whether given type is active or not

    :param type: Type
    """
