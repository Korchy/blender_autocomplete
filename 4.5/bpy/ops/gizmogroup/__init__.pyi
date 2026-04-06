import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def gizmo_select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    extend: bool | None = False,
    deselect: bool | None = False,
    toggle: bool | None = False,
    deselect_all: bool | None = False,
    select_passthrough: bool | None = False,
) -> None:
    """Select the currently highlighted gizmo

    :param extend: Extend, Extend selection instead of deselecting everything first
    :param deselect: Deselect, Remove from selection
    :param toggle: Toggle Selection, Toggle the selection
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    """

def gizmo_tweak(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Tweak the active gizmo"""
