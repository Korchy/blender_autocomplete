import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform

def attribute_set(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    value_float: float | None = 0.0,
    value_float_vector_2d: collections.abc.Iterable[float] | None = (0.0, 0.0),
    value_float_vector_3d: collections.abc.Iterable[float] | None = (0.0, 0.0, 0.0),
    value_int: int | None = 0,
    value_int_vector_2d: collections.abc.Iterable[int] | None = (0, 0),
    value_color: collections.abc.Iterable[float] | None = (1.0, 1.0, 1.0, 1.0),
    value_bool: bool | None = False,
) -> None:
    """Set values of the active attribute for selected elements

    :param value_float: Value
    :param value_float_vector_2d: Value
    :param value_float_vector_3d: Value
    :param value_int: Value
    :param value_int_vector_2d: Value
    :param value_color: Value
    :param value_bool: Value
    """

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Remove selected points"""

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected points"""

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    POINTCLOUD_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Make copies of selected elements and move them

    :param POINTCLOUD_OT_duplicate: Duplicate, Copy selected points
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """(De)select all point cloud

        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    seed: int | None = 0,
    probability: float | None = 0.5,
) -> None:
    """Randomizes existing selection or create new random selection

    :param seed: Seed, Source of randomness
    :param probability: Probability, Chance of every point being included in the selection
    """

def separate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Separate selected geometry into a new point cloud"""
