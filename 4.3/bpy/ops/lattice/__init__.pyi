import typing
import collections.abc
import typing_extensions
import bpy._typing.rna_enums

def flip(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: typing.Literal["U", "V", "W"] | None = "U",
):
    """Mirror all control points without inverting the lattice deform

    :type execution_context: int | str | None
    :type undo: bool | None
    :param axis: Flip Axis, Coordinates along this axis get flipped
    :type axis: typing.Literal['U','V','W'] | None
    """

def make_regular(execution_context: int | str | None = None, undo: bool | None = None):
    """Set UVW control points a uniform distance apart

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Change selection of all UVW control points

        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_less(execution_context: int | str | None = None, undo: bool | None = None):
    """Deselect vertices at the boundary of each selection region

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_mirror(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    axis: set[bpy._typing.rna_enums.AxisFlagXyzItems] | None = {"X"},
    extend: bool | None = False,
):
    """Select mirrored lattice points

    :type execution_context: int | str | None
    :type undo: bool | None
    :param axis: Axis
    :type axis: set[bpy._typing.rna_enums.AxisFlagXyzItems] | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """

def select_more(execution_context: int | str | None = None, undo: bool | None = None):
    """Select vertex directly linked to already selected ones

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_random(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
):
    """Randomly select UVW control points

        :type execution_context: int | str | None
        :type undo: bool | None
        :param ratio: Ratio, Portion of items to select randomly
        :type ratio: float | None
        :param seed: Random Seed, Seed for the random number generator
        :type seed: int | None
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
        :type action: typing.Literal['SELECT','DESELECT'] | None
    """

def select_ungrouped(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
):
    """Select vertices without a group

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend the selection
    :type extend: bool | None
    """
