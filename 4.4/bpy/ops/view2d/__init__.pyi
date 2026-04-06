import typing
import collections.abc
import typing_extensions
import numpy.typing as npt

def edge_pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    inside_padding: float | None = 1.0,
    outside_padding: float | None = 0.0,
    speed_ramp: float | None = 1.0,
    max_speed: float | None = 500.0,
    delay: float | None = 1.0,
    zoom_influence: float | None = 0.0,
) -> None:
    """Pan the view when the mouse is held at an edge

    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    """

def ndof(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Use a 3D mouse device to pan/zoom the view"""

def pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
) -> None:
    """Pan the view

    :param deltax: Delta X
    :param deltay: Delta Y
    """

def reset(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Reset the view"""

def scroll_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
    page: bool | None = False,
) -> None:
    """Scroll the view down

    :param deltax: Delta X
    :param deltay: Delta Y
    :param page: Page, Scroll down one page
    """

def scroll_left(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
) -> None:
    """Scroll the view left

    :param deltax: Delta X
    :param deltay: Delta Y
    """

def scroll_right(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
) -> None:
    """Scroll the view right

    :param deltax: Delta X
    :param deltay: Delta Y
    """

def scroll_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
    page: bool | None = False,
) -> None:
    """Scroll the view up

    :param deltax: Delta X
    :param deltay: Delta Y
    :param page: Page, Scroll up one page
    """

def scroller_activate(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
) -> None:
    """Scroll view by mouse click and drag"""

def smoothview(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
) -> None:
    """Undocumented, consider contributing.

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    """

def zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: float | None = 0.0,
    deltay: float | None = 0.0,
    use_cursor_init: bool | None = True,
) -> None:
    """Zoom in/out the view

    :param deltax: Delta X
    :param deltay: Delta Y
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    """

def zoom_border(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    zoom_out: bool | None = False,
) -> None:
    """Zoom in the view to the nearest item contained in the border

    :param xmin: X Min
    :param xmax: X Max
    :param ymin: Y Min
    :param ymax: Y Max
    :param wait_for_input: Wait for Input
    :param zoom_out: Zoom Out
    """

def zoom_in(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    zoomfacx: float | None = 0.0,
    zoomfacy: float | None = 0.0,
) -> None:
    """Zoom in the view

    :param zoomfacx: Zoom Factor X
    :param zoomfacy: Zoom Factor Y
    """

def zoom_out(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    zoomfacx: float | None = 0.0,
    zoomfacy: float | None = 0.0,
) -> None:
    """Zoom out the view

    :param zoomfacx: Zoom Factor X
    :param zoomfacy: Zoom Factor Y
    """
