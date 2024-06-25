import typing
import collections.abc
import bpy.types

GenericType1 = typing.TypeVar("GenericType1")
GenericType2 = typing.TypeVar("GenericType2")

def edge_pan(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    inside_padding: typing.Any | None = 1.0,
    outside_padding: typing.Any | None = 0.0,
    speed_ramp: typing.Any | None = 1.0,
    max_speed: typing.Any | None = 500.0,
    delay: typing.Any | None = 1.0,
    zoom_influence: typing.Any | None = 0.0,
):
    """Pan the view when the mouse is held at an edge

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: typing.Any | None
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: typing.Any | None
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: typing.Any | None
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: typing.Any | None
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: typing.Any | None
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: typing.Any | None
    """

    ...

def ndof(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Use a 3D mouse device to pan/zoom the view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def pan(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deltax: typing.Any | None = 0,
    deltay: typing.Any | None = 0,
):
    """Pan the view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: typing.Any | None
    :param deltay: Delta Y
    :type deltay: typing.Any | None
    """

    ...

def reset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Reset the view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def scroll_down(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deltax: typing.Any | None = 0,
    deltay: typing.Any | None = 0,
    page: bool | typing.Any | None = False,
):
    """Scroll the view down

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: typing.Any | None
    :param deltay: Delta Y
    :type deltay: typing.Any | None
    :param page: Page, Scroll down one page
    :type page: bool | typing.Any | None
    """

    ...

def scroll_left(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deltax: typing.Any | None = 0,
    deltay: typing.Any | None = 0,
):
    """Scroll the view left

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: typing.Any | None
    :param deltay: Delta Y
    :type deltay: typing.Any | None
    """

    ...

def scroll_right(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deltax: typing.Any | None = 0,
    deltay: typing.Any | None = 0,
):
    """Scroll the view right

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: typing.Any | None
    :param deltay: Delta Y
    :type deltay: typing.Any | None
    """

    ...

def scroll_up(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deltax: typing.Any | None = 0,
    deltay: typing.Any | None = 0,
    page: bool | typing.Any | None = False,
):
    """Scroll the view up

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: typing.Any | None
    :param deltay: Delta Y
    :type deltay: typing.Any | None
    :param page: Page, Scroll up one page
    :type page: bool | typing.Any | None
    """

    ...

def scroller_activate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Scroll view by mouse click and drag

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

    ...

def smoothview(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
):
    """Undocumented, consider contributing.

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: typing.Any | None
    :param xmax: X Max
    :type xmax: typing.Any | None
    :param ymin: Y Min
    :type ymin: typing.Any | None
    :param ymax: Y Max
    :type ymax: typing.Any | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    """

    ...

def zoom(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    deltax: typing.Any | None = 0.0,
    deltay: typing.Any | None = 0.0,
    use_cursor_init: bool | typing.Any | None = True,
):
    """Zoom in/out the view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param deltax: Delta X
    :type deltax: typing.Any | None
    :param deltay: Delta Y
    :type deltay: typing.Any | None
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool | typing.Any | None
    """

    ...

def zoom_border(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    xmin: typing.Any | None = 0,
    xmax: typing.Any | None = 0,
    ymin: typing.Any | None = 0,
    ymax: typing.Any | None = 0,
    wait_for_input: bool | typing.Any | None = True,
    zoom_out: bool | typing.Any | None = False,
):
    """Zoom in the view to the nearest item contained in the border

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param xmin: X Min
    :type xmin: typing.Any | None
    :param xmax: X Max
    :type xmax: typing.Any | None
    :param ymin: Y Min
    :type ymin: typing.Any | None
    :param ymax: Y Max
    :type ymax: typing.Any | None
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool | typing.Any | None
    :param zoom_out: Zoom Out
    :type zoom_out: bool | typing.Any | None
    """

    ...

def zoom_in(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    zoomfacx: typing.Any | None = 0.0,
    zoomfacy: typing.Any | None = 0.0,
):
    """Zoom in the view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: typing.Any | None
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: typing.Any | None
    """

    ...

def zoom_out(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    zoomfacx: typing.Any | None = 0.0,
    zoomfacy: typing.Any | None = 0.0,
):
    """Zoom out the view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: typing.Any | None
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: typing.Any | None
    """

    ...
