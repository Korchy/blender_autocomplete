import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def add(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Add a new time marker"""

def camera_bind(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Bind the selected camera to a marker on the current frame"""

def delete(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    confirm: bool | None = True,
) -> None:
    """Delete selected time marker(s)

    :param confirm: Confirm, Prompt for confirmation
    """

def duplicate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frames: int | None = 0,
) -> None:
    """Duplicate selected time marker(s)

    :param frames: Frames
    """

def make_links_scene(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    scene: str | None = "",
) -> None:
    """Copy selected markers to another scene

    :param scene: Scene
    """

def move(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    frames: int | None = 0,
    tweak: bool | None = False,
) -> None:
    """Move selected time marker(s)

    :param frames: Frames
    :param tweak: Tweak, Operator has been activated using a click-drag event
    """

def rename(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    name: str = "RenamedMarker",
) -> None:
    """Rename first selected time marker

    :param name: Name, New name for marker
    """

def select(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    wait_to_deselect_others: bool | None = False,
    use_select_on_click: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    camera: bool | None = False,
) -> None:
    """Select time marker(s)

    :param wait_to_deselect_others: Wait to Deselect Others
    :param use_select_on_click: Act on Click, Instead of selecting on mouse press, wait to see if theres drag event. Otherwise select on mouse release
    :param mouse_x: Mouse X
    :param mouse_y: Mouse Y
    :param extend: Extend, Extend the selection
    :param camera: Camera, Select the camera
    """

def select_all(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
) -> None:
    """Change selection of all time markers

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
    tweak: bool | None = False,
) -> None:
    """Select all time markers using box selection

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
        :param tweak: Tweak, Operator has been activated using a click-drag event
    """

def select_leftright(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    mode: typing.Literal["LEFT", "RIGHT"] | None = "LEFT",
    extend: bool | None = False,
) -> None:
    """Select markers on and left/right of the current frame

    :param mode: Mode
    :param extend: Extend Select
    """
