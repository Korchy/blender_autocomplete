import typing
import collections.abc
import typing_extensions

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
):
    """Pan the view when the mouse is held at an edge

    :type execution_context: int | str | None
    :type undo: bool | None
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: float | None
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: float | None
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: float | None
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: float | None
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: float | None
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: float | None
    """

def ndof(execution_context: int | str | None = None, undo: bool | None = None):
    """Use a 3D mouse device to pan/zoom the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def pan(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
):
    """Pan the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: int | None
    :param deltay: Delta Y
    :type deltay: int | None
    """

def reset(execution_context: int | str | None = None, undo: bool | None = None):
    """Reset the view

    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scroll_down(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
    page: bool | None = False,
):
    """Scroll the view down

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: int | None
    :param deltay: Delta Y
    :type deltay: int | None
    :param page: Page, Scroll down one page
    :type page: bool | None
    """

def scroll_left(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
):
    """Scroll the view left

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: int | None
    :param deltay: Delta Y
    :type deltay: int | None
    """

def scroll_right(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
):
    """Scroll the view right

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: int | None
    :param deltay: Delta Y
    :type deltay: int | None
    """

def scroll_up(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: int | None = 0,
    deltay: int | None = 0,
    page: bool | None = False,
):
    """Scroll the view up

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: int | None
    :param deltay: Delta Y
    :type deltay: int | None
    :param page: Page, Scroll up one page
    :type page: bool | None
    """

def scroller_activate(
    execution_context: int | str | None = None, undo: bool | None = None
):
    """Scroll view by mouse click and drag

    :type execution_context: int | str | None
    :type undo: bool | None
    """

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
):
    """Undocumented, consider contributing.

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    """

def zoom(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    deltax: float | None = 0.0,
    deltay: float | None = 0.0,
    use_cursor_init: bool | None = True,
):
    """Zoom in/out the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: float | None
    :param deltay: Delta Y
    :type deltay: float | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | None
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
):
    """Zoom in the view to the nearest item contained in the border

    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: int | None
    :param xmax: X Max
    :type xmax: int | None
    :param ymin: Y Min
    :type ymin: int | None
    :param ymax: Y Max
    :type ymax: int | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | None
    :param zoom_out: Zoom Out
    :type zoom_out: bool | None
    """

def zoom_in(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    zoomfacx: float | None = 0.0,
    zoomfacy: float | None = 0.0,
):
    """Zoom in the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: float | None
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: float | None
    """

def zoom_out(
    execution_context: int | str | None = None,
    undo: bool | None = None,
    /,
    *,
    zoomfacx: float | None = 0.0,
    zoomfacy: float | None = 0.0,
):
    """Zoom out the view

    :type execution_context: int | str | None
    :type undo: bool | None
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: float | None
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: float | None
    """
