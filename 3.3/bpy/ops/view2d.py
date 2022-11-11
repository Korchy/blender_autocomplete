import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def edge_pan(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             inside_padding: float = 1.0,
             outside_padding: float = 0.0,
             speed_ramp: float = 1.0,
             max_speed: float = 500.0,
             delay: float = 1.0,
             zoom_influence: float = 0.0):
    ''' Pan the view when the mouse is held at an edge

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: float
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: float
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: float
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: float
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: float
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: float
    '''

    pass


def ndof(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Use a 3D mouse device to pan/zoom the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def pan(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        deltax: int = 0,
        deltay: int = 0):
    ''' Pan the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    '''

    pass


def reset(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None):
    ''' Reset the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def scroll_down(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                deltax: int = 0,
                deltay: int = 0,
                page: bool = False):
    ''' Scroll the view down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    :param page: Page, Scroll down one page
    :type page: bool
    '''

    pass


def scroll_left(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                deltax: int = 0,
                deltay: int = 0):
    ''' Scroll the view left

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    '''

    pass


def scroll_right(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 deltax: int = 0,
                 deltay: int = 0):
    ''' Scroll the view right

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    '''

    pass


def scroll_up(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              deltax: int = 0,
              deltay: int = 0,
              page: bool = False):
    ''' Scroll the view up

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: int
    :param deltay: Delta Y
    :type deltay: int
    :param page: Page, Scroll up one page
    :type page: bool
    '''

    pass


def scroller_activate(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Scroll view by mouse click and drag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smoothview(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True):
    ''' Undocumented, consider contributing <https://developer.blender.org/T51061> __.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    '''

    pass


def zoom(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         deltax: float = 0.0,
         deltay: float = 0.0,
         use_cursor_init: bool = True):
    ''' Zoom in/out the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param deltax: Delta X
    :type deltax: float
    :param deltay: Delta Y
    :type deltay: float
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: bool
    '''

    pass


def zoom_border(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                xmin: int = 0,
                xmax: int = 0,
                ymin: int = 0,
                ymax: int = 0,
                wait_for_input: bool = True,
                zoom_out: bool = False):
    ''' Zoom in the view to the nearest item contained in the border

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param xmin: X Min
    :type xmin: int
    :param xmax: X Max
    :type xmax: int
    :param ymin: Y Min
    :type ymin: int
    :param ymax: Y Max
    :type ymax: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param zoom_out: Zoom Out
    :type zoom_out: bool
    '''

    pass


def zoom_in(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: bool = None,
            *,
            zoomfacx: float = 0.0,
            zoomfacy: float = 0.0):
    ''' Zoom in the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: float
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: float
    '''

    pass


def zoom_out(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             zoomfacx: float = 0.0,
             zoomfacy: float = 0.0):
    ''' Zoom out the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: float
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: float
    '''

    pass
