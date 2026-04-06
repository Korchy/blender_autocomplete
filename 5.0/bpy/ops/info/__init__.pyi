import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def report_copy(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Copy selected reports to clipboard"""

def report_delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Delete selected reports"""

def report_replay(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Replay selected reports"""

def reports_display_update(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Update the display of reports in Blender UI (internal use)"""

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "SELECT",
) -> None:
    """Change selection of all visible reports

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

def select_box(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
) -> None:
    """Toggle box selection

        :param xmin: X Min
        :param xmax: X Max
        :param ymin: Y Min
        :param ymax: Y Max
        :param wait_for_input: Wait for Input
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
    """

def select_pick(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    report_index: int | None = 0,
    extend: bool | None = False,
) -> None:
    """Select reports by index

    :param report_index: Report, Index of the report
    :param extend: Extend, Extend report selection
    """
