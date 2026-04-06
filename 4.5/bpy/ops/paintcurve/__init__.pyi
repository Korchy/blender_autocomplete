import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
) -> None:
    """Add New Paint Curve Point

    :param location: Location, Location of vertex in area space
    """

def add_point_slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    PAINTCURVE_OT_add_point: add_point | None = None,
    PAINTCURVE_OT_slide: slide | None = None,
) -> None:
    """Add new curve point and slide it

    :param PAINTCURVE_OT_add_point: Add New Paint Curve Point, Add New Paint Curve Point
    :param PAINTCURVE_OT_slide: Slide Paint Curve Point, Select and slide paint curve point
    """

def cursor(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Place cursor"""

def delete_point(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove Paint Curve Point"""

def draw(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Draw curve"""

def new(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add new paint curve"""

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    location: collections.abc.Iterable[int] | None = (0, 0),
    toggle: bool | None = False,
    extend: bool | None = False,
) -> None:
    """Select a paint curve point

    :param location: Location, Location of vertex in area space
    :param toggle: Toggle, (De)select all
    :param extend: Extend, Extend selection
    """

def slide(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    align: bool | None = False,
    select: bool | None = True,
) -> None:
    """Select and slide paint curve point

    :param align: Align Handles, Aligns opposite point handle during transform
    :param select: Select, Attempt to select a point handle before transform
    """
