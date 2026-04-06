import typing
import collections.abc
import typing_extensions
import numpy.typing as npt
import bpy.ops.transform

def delete_metaelems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Delete selected metaball element(s)

    :param confirm: Confirm, Prompt for confirmation
    """

def duplicate_metaelems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Duplicate selected metaball element(s)"""

def duplicate_move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    MBALL_OT_duplicate_metaelems: duplicate_metaelems | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
) -> None:
    """Make copies of the selected metaball elements and move them

    :param MBALL_OT_duplicate_metaelems: Duplicate Metaball Elements, Duplicate selected metaball element(s)
    :param TRANSFORM_OT_translate: Move, Move selected items
    """

def hide_metaelems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    unselected: bool | None = False,
) -> None:
    """Hide (un)selected metaball element(s)

    :param unselected: Unselected, Hide unselected rather than selected
    """

def reveal_metaelems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    select: bool | None = True,
) -> None:
    """Reveal all hidden metaball elements

    :param select: Select
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all metaball elements

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

def select_random_metaelems(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    ratio: float | None = 0.5,
    seed: int | None = 0,
    action: typing.Literal["SELECT", "DESELECT"] | None = "SELECT",
) -> None:
    """Randomly select metaball elements

        :param ratio: Ratio, Portion of items to select randomly
        :param seed: Random Seed, Seed for the random number generator
        :param action: Action, Selection action to execute

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.
    """

def select_similar(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    type: typing.Literal["TYPE", "RADIUS", "STIFFNESS", "ROTATION"] | None = "TYPE",
    threshold: float | None = 0.1,
) -> None:
    """Select similar metaballs by property types

    :param type: Type
    :param threshold: Threshold
    """
