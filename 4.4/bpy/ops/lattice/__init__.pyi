import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.stub_internal.rna_enums

def flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal["U", "V", "W"] | None = "U",
) -> None:
    """Mirror all control points without inverting the lattice deform

    :param axis: Flip Axis, Coordinates along this axis get flipped
    """

def make_regular(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Set UVW control points a uniform distance apart"""

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all UVW control points

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

def select_less(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Deselect vertices at the boundary of each selection region"""

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: set[bpy.stub_internal.rna_enums.AxisFlagXyzItems] | None = {"X"},
    extend: bool | None = False,
) -> None:
    """Select mirrored lattice points

    :param axis: Axis
    :param extend: Extend, Extend the selection
    """

def select_more(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Select vertex directly linked to already selected ones"""

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
) -> None:
    """Randomly select UVW control points

        :param ratio: Ratio, Portion of items to select randomly
        :param seed: Random Seed, Seed for the random number generator
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
    """

def select_ungrouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
) -> None:
    """Select vertices without a group

    :param extend: Extend, Extend the selection
    """
