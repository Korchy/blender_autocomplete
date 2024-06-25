import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def add_point(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0, 0),
):
    """Add New Paint Curve Point

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of vertex in area space
    :type location: typing.Any | None
    """

    ...

def add_point_slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    PAINTCURVE_OT_add_point: add_point | None = None,
    PAINTCURVE_OT_slide: slide | None = None,
):
    """Add new curve point and slide it

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point
    :type PAINTCURVE_OT_add_point: add_point | None
    :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point
    :type PAINTCURVE_OT_slide: slide | None
    """

    ...

def cursor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Place cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def delete_point(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Remove Paint Curve Point

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def draw(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Draw curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def new(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add new paint curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def select(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    location: typing.Any | None = (0, 0),
    toggle: bool | typing.Any | None = False,
    extend: bool | typing.Any | None = False,
):
    """Select a paint curve point

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of vertex in area space
    :type location: typing.Any | None
    :param toggle: Toggle, (De)select all
    :type toggle: bool | typing.Any | None
    :param extend: Extend, Extend selection
    :type extend: bool | typing.Any | None
    """

    ...

def slide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    align: bool | typing.Any | None = False,
    select: bool | typing.Any | None = True,
):
    """Select and slide paint curve point

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param align: Align Handles, Aligns opposite point handle during transform
    :type align: bool | typing.Any | None
    :param select: Select, Attempt to select a point handle before transform
    :type select: bool | typing.Any | None
    """

    ...
