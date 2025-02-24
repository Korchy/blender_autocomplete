import typing
import collections.abc
import typing_extensions

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
):
    """Select the currently highlighted gizmo

    :type execution_context: int | str | None
    :type undo: bool | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    :param deselect: Deselect, Remove from selection
    :type deselect: bool | None
    :param toggle: Toggle Selection, Toggle the selection
    :type toggle: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param select_passthrough: Only Select Unselected, Ignore the select action when the element is already selected
    :type select_passthrough: bool | None
    """

def gizmo_tweak(execution_context: int | str | None = None, undo: bool | None = None):
    """Tweak the active gizmo

    :type execution_context: int | str | None
    :type undo: bool | None
    """
