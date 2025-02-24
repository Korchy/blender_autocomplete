import typing
import collections.abc
import typing_extensions

def add_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
):
    """Add New Paint Curve Point

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of vertex in area space
    :type location: collections.abc.Iterable[int] | None
    """

def add_point_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    PAINTCURVE_OT_add_point: add_point | None = None,
    PAINTCURVE_OT_slide: slide | None = None,
):
    """Add new curve point and slide it

    :type execution_context: int | str | None
    :type undo: bool | None
    :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point
    :type PAINTCURVE_OT_add_point: add_point | None
    :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point
    :type PAINTCURVE_OT_slide: slide | None
    """

def cursor(execution_context: int | str | None = None, undo: bool | None = None):
    """Place cursor

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def delete_point(execution_context: int | str | None = None, undo: bool | None = None):
    """Remove Paint Curve Point

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def draw(execution_context: int | str | None = None, undo: bool | None = None):
    """Draw curve

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def new(execution_context: int | str | None = None, undo: bool | None = None):
    """Add new paint curve

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    toggle: bool | None = False,
    extend: bool | None = False,
):
    """Select a paint curve point

    :type execution_context: int | str | None
    :type undo: bool | None
    :param location: Location, Location of vertex in area space
    :type location: collections.abc.Iterable[int] | None
    :param toggle: Toggle, (De)select all
    :type toggle: bool | None
    :param extend: Extend, Extend selection
    :type extend: bool | None
    """

def slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: bool | None = False,
    select: bool | None = True,
):
    """Select and slide paint curve point

    :type execution_context: int | str | None
    :type undo: bool | None
    :param align: Align Handles, Aligns opposite point handle during transform
    :type align: bool | None
    :param select: Select, Attempt to select a point handle before transform
    :type select: bool | None
    """
