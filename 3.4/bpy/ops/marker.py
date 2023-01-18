import sys
import typing
import bpy.types

GenericType = typing.TypeVar("GenericType")


def add(override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: typing.Optional[bool] = None):
    ''' Add a new time marker

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def camera_bind(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: typing.Optional[bool] = None):
    ''' Bind the selected camera to a marker on the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           confirm: typing.Union[bool, typing.Any] = True):
    ''' Delete selected time marker(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: typing.Union[bool, typing.Any]
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: typing.Optional[bool] = None,
              *,
              frames: typing.Optional[typing.Any] = 0):
    ''' Duplicate selected time marker(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param frames: Frames
    :type frames: typing.Optional[typing.Any]
    '''

    pass


def make_links_scene(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     scene: typing.Union[str, int, typing.Any] = ''):
    ''' Copy selected markers to another scene

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param scene: Scene
    :type scene: typing.Union[str, int, typing.Any]
    '''

    pass


def move(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: typing.Optional[bool] = None,
         *,
         frames: typing.Optional[typing.Any] = 0,
         tweak: typing.Union[bool, typing.Any] = False):
    ''' Move selected time marker(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param frames: Frames
    :type frames: typing.Optional[typing.Any]
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: typing.Union[bool, typing.Any]
    '''

    pass


def rename(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           name: typing.Union[str, typing.Any] = "RenamedMarker"):
    ''' Rename first selected time marker

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param name: Name, New name for marker
    :type name: typing.Union[str, typing.Any]
    '''

    pass


def select(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: typing.Optional[bool] = None,
           *,
           wait_to_deselect_others: typing.Union[bool, typing.Any] = False,
           mouse_x: typing.Optional[typing.Any] = 0,
           mouse_y: typing.Optional[typing.Any] = 0,
           extend: typing.Union[bool, typing.Any] = False,
           camera: typing.Union[bool, typing.Any] = False):
    ''' Select time marker(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: typing.Union[bool, typing.Any]
    :param mouse_x: Mouse X
    :type mouse_x: typing.Optional[typing.Any]
    :param mouse_y: Mouse Y
    :type mouse_y: typing.Optional[typing.Any]
    :param extend: Extend, Extend the selection
    :type extend: typing.Union[bool, typing.Any]
    :param camera: Camera, Select the camera
    :type camera: typing.Union[bool, typing.Any]
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Change selection of all time markers

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_box(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: typing.Optional[bool] = None,
               *,
               xmin: typing.Optional[typing.Any] = 0,
               xmax: typing.Optional[typing.Any] = 0,
               ymin: typing.Optional[typing.Any] = 0,
               ymax: typing.Optional[typing.Any] = 0,
               wait_for_input: typing.Union[bool, typing.Any] = True,
               mode: typing.Optional[typing.Any] = 'SET',
               tweak: typing.Union[bool, typing.Any] = False):
    ''' Select all time markers using box selection

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
    :param mode: Mode * ``SET`` Set -- Set a new selection. * ``ADD`` Extend -- Extend existing selection. * ``SUB`` Subtract -- Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: typing.Union[bool, typing.Any]
    '''

    pass


def select_leftright(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: typing.Optional[bool] = None,
                     *,
                     mode: typing.Optional[typing.Any] = 'LEFT',
                     extend: typing.Union[bool, typing.Any] = False):
    ''' Select markers on and left/right of the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param extend: Extend Select
    :type extend: typing.Union[bool, typing.Any]
    '''

    pass
