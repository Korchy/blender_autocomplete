import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def edge_pan(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             inside_padding: typing.Optional[typing.Any] = 1.0,
             outside_padding: typing.Optional[typing.Any] = 0.0,
             speed_ramp: typing.Optional[typing.Any] = 1.0,
             max_speed: typing.Optional[typing.Any] = 500.0,
             delay: typing.Optional[typing.Any] = 1.0,
             zoom_influence: typing.Optional[typing.Any] = 0.0):
    ''' Pan the view when the mouse is held at an edge

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param inside_padding: Inside Padding, Inside distance in UI units from the edge of the region within which to start panning
    :type inside_padding: typing.Optional[typing.Any]
    :param outside_padding: Outside Padding, Outside distance in UI units from the edge of the region at which to stop panning
    :type outside_padding: typing.Optional[typing.Any]
    :param speed_ramp: Speed Ramp, Width of the zone in UI units where speed increases with distance from the edge
    :type speed_ramp: typing.Optional[typing.Any]
    :param max_speed: Max Speed, Maximum speed in UI units per second
    :type max_speed: typing.Optional[typing.Any]
    :param delay: Delay, Delay in seconds before maximum speed is reached
    :type delay: typing.Optional[typing.Any]
    :param zoom_influence: Zoom Influence, Influence of the zoom factor on scroll speed
    :type zoom_influence: typing.Optional[typing.Any]
    '''

    pass


def ndof(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None):
    ''' Use a 3D mouse device to pan/zoom the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def pan(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None,
        *,
        deltax: typing.Optional[typing.Any] = 0,
        deltay: typing.Optional[typing.Any] = 0):
    ''' Pan the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deltax: Delta X
    :type deltax: typing.Optional[typing.Any]
    :param deltay: Delta Y
    :type deltay: typing.Optional[typing.Any]
    '''

    pass


def reset(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: typing.Optional[bool] = None):
    ''' Reset the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def scroll_down(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                deltax: typing.Optional[typing.Any] = 0,
                deltay: typing.Optional[typing.Any] = 0,
                page: typing.Union[bool, typing.Any] = False):
    ''' Scroll the view down

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deltax: Delta X
    :type deltax: typing.Optional[typing.Any]
    :param deltay: Delta Y
    :type deltay: typing.Optional[typing.Any]
    :param page: Page, Scroll down one page
    :type page: typing.Union[bool, typing.Any]
    '''

    pass


def scroll_left(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                deltax: typing.Optional[typing.Any] = 0,
                deltay: typing.Optional[typing.Any] = 0):
    ''' Scroll the view left

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deltax: Delta X
    :type deltax: typing.Optional[typing.Any]
    :param deltay: Delta Y
    :type deltay: typing.Optional[typing.Any]
    '''

    pass


def scroll_right(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: typing.Optional[bool] = None,
                 *,
                 deltax: typing.Optional[typing.Any] = 0,
                 deltay: typing.Optional[typing.Any] = 0):
    ''' Scroll the view right

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deltax: Delta X
    :type deltax: typing.Optional[typing.Any]
    :param deltay: Delta Y
    :type deltay: typing.Optional[typing.Any]
    '''

    pass


def scroll_up(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              deltax: typing.Optional[typing.Any] = 0,
              deltay: typing.Optional[typing.Any] = 0,
              page: typing.Union[bool, typing.Any] = False):
    ''' Scroll the view up

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deltax: Delta X
    :type deltax: typing.Optional[typing.Any]
    :param deltay: Delta Y
    :type deltay: typing.Optional[typing.Any]
    :param page: Page, Scroll up one page
    :type page: typing.Union[bool, typing.Any]
    '''

    pass


def scroller_activate(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: typing.Optional[bool] = None):
    ''' Scroll view by mouse click and drag

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def smoothview(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               xmin: typing.Optional[typing.Any] = 0,
               xmax: typing.Optional[typing.Any] = 0,
               ymin: typing.Optional[typing.Any] = 0,
               ymax: typing.Optional[typing.Any] = 0,
               wait_for_input: typing.Union[bool, typing.Any] = True):
    ''' Undocumented, consider `contributing <https://developer.blender.org/T51061>`__.

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Union[bool, typing.Any]
    '''

    pass


def zoom(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         deltax: typing.Optional[typing.Any] = 0.0,
         deltay: typing.Optional[typing.Any] = 0.0,
         use_cursor_init: typing.Union[bool, typing.Any] = True):
    ''' Zoom in/out the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param deltax: Delta X
    :type deltax: typing.Optional[typing.Any]
    :param deltay: Delta Y
    :type deltay: typing.Optional[typing.Any]
    :param use_cursor_init: Use Mouse Position, Allow the initial mouse position to be used
    :type use_cursor_init: typing.Union[bool, typing.Any]
    '''

    pass


def zoom_border(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None,
                *,
                xmin: typing.Optional[typing.Any] = 0,
                xmax: typing.Optional[typing.Any] = 0,
                ymin: typing.Optional[typing.Any] = 0,
                ymax: typing.Optional[typing.Any] = 0,
                wait_for_input: typing.Union[bool, typing.Any] = True,
                zoom_out: typing.Union[bool, typing.Any] = False):
    ''' Zoom in the view to the nearest item contained in the border

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Union[bool, typing.Any]
    :param zoom_out: Zoom Out
    :type zoom_out: typing.Union[bool, typing.Any]
    '''

    pass


def zoom_in(override_context: typing.Union[typing.
                                           Dict, 'bpy.types.Context'] = None,
            execution_context: typing.Union[str, int] = None,
            undo: typing.Optional[bool] = None,
            *,
            zoomfacx: typing.Optional[typing.Any] = 0.0,
            zoomfacy: typing.Optional[typing.Any] = 0.0):
    ''' Zoom in the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: typing.Optional[typing.Any]
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: typing.Optional[typing.Any]
    '''

    pass


def zoom_out(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: typing.Optional[bool] = None,
             *,
             zoomfacx: typing.Optional[typing.Any] = 0.0,
             zoomfacy: typing.Optional[typing.Any] = 0.0):
    ''' Zoom out the view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param zoomfacx: Zoom Factor X
    :type zoomfacx: typing.Optional[typing.Any]
    :param zoomfacy: Zoom Factor Y
    :type zoomfacy: typing.Optional[typing.Any]
    '''

    pass
