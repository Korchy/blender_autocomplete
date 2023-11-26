import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def bake_keys(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Add keyframes on every frame between the selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def clean(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          threshold: typing.Optional[typing.Any] = 0.001,
          channels: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Simplify F-Curves by removing closely spaced keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param threshold: Threshold
    :type threshold: typing.Optional[typing.Any]
    :param channels: Channels
    :type channels: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def clickselect(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        wait_to_deselect_others: typing.Optional[typing.Union[bool, typing.
                                                              Any]] = False,
        mouse_x: typing.Optional[typing.Any] = 0,
        mouse_y: typing.Optional[typing.Any] = 0,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False,
        deselect_all: typing.Optional[typing.Union[bool, typing.Any]] = False,
        column: typing.Optional[typing.Union[bool, typing.Any]] = False,
        channel: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select keyframes by clicking on them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: typing.Optional[typing.Union[bool, typing.Any]]
    :param mouse_x: Mouse X
    :type mouse_x: typing.Optional[typing.Any]
    :param mouse_y: Mouse Y
    :type mouse_y: typing.Optional[typing.Any]
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: typing.Optional[typing.Union[bool, typing.Any]]
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: typing.Optional[typing.Union[bool, typing.Any]]
    :param channel: Only Channel, Select all the keyframes in the channel under the mouse
    :type channel: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def copy(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None):
    ''' Copy selected keyframes to the internal clipboard

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def delete(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           confirm: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Remove all selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Make a copy of all selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def duplicate_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        ACTION_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_transform: typing.
        Optional['bpy.ops.transform.transform'] = None):
    ''' Make a copy of all selected keyframes and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param ACTION_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type ACTION_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type
    :type TRANSFORM_OT_transform: typing.Optional['bpy.ops.transform.transform']
    '''

    pass


def easing_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'AUTO'):
    ''' Set easing type for the F-Curve segments starting from the selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def extrapolation_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'CONSTANT'):
    ''' Set extrapolation mode for selected F-Curves

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CONSTANT`` Constant Extrapolation -- Values on endpoint keyframes are held. * ``LINEAR`` Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes. * ``MAKE_CYCLIC`` Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one doesn't exist already. * ``CLEAR_CYCLIC`` Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def frame_jump(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set the current frame to the average frame value of selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def handle_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'FREE'):
    ''' Set type of handle for selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def interpolation_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'CONSTANT'):
    ''' Set interpolation mode for the F-Curve segments starting from the selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def keyframe_insert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Any] = 'ALL'):
    ''' Insert keyframes for the specified channels

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Any]
    '''

    pass


def keyframe_type(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'KEYFRAME'):
    ''' Set type of keyframe for the selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    '''

    pass


def layer_next(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Switch to editing action in animation layer above the current action in the NLA Stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def layer_prev(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Switch to editing action in animation layer below the current action in the NLA Stack

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def markers_make_local(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Move selected scene markers to the active Action as local 'pose' markers

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def mirror(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           type: typing.Optional[typing.Any] = 'CFRA'):
    ''' Flip selected keyframes over the selected mirror line

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CFRA`` By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line. * ``XAXIS`` By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa). * ``MARKER`` By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def new(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create new action

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def paste(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          offset: typing.Optional[typing.Union[str, int]] = 'START',
          merge: typing.Optional[typing.Union[str, int]] = 'MIX',
          flipped: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param offset: Offset, Paste time offset of keys
    :type offset: typing.Optional[typing.Union[str, int]]
    :param merge: Type, Method of merging pasted keys and existing
    :type merge: typing.Optional[typing.Union[str, int]]
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    :type flipped: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def previewrange_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Set Preview Range based on extents of selected Keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def push_down(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Push action down on to the NLA stack as a new strip

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_all(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        action: typing.Optional[typing.Any] = 'TOGGLE'):
    ''' Toggle selection of all keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param action: Action, Selection action to execute * ``TOGGLE`` Toggle -- Toggle selection for all elements. * ``SELECT`` Select -- Select all elements. * ``DESELECT`` Deselect -- Deselect all elements. * ``INVERT`` Invert -- Invert selection of all elements.
    :type action: typing.Optional[typing.Any]
    '''

    pass


def select_box(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        axis_range: typing.Optional[typing.Union[bool, typing.Any]] = False,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mode: typing.Optional[typing.Any] = 'SET',
        tweak: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select all keyframes within the specified region

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param axis_range: Axis Range
    :type axis_range: typing.Optional[typing.Union[bool, typing.Any]]
    :param xmin: X Min
    :type xmin: typing.Optional[typing.Any]
    :param xmax: X Max
    :type xmax: typing.Optional[typing.Any]
    :param ymin: Y Min
    :type ymin: typing.Optional[typing.Any]
    :param ymax: Y Max
    :type ymax: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode * ``SET`` Set -- Set a new selection. * ``ADD`` Extend -- Extend existing selection. * ``SUB`` Subtract -- Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_circle(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        x: typing.Optional[typing.Any] = 0,
        y: typing.Optional[typing.Any] = 0,
        radius: typing.Optional[typing.Any] = 25,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mode: typing.Optional[typing.Any] = 'SET'):
    ''' Select keyframe points using circle selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param x: X
    :type x: typing.Optional[typing.Any]
    :param y: Y
    :type y: typing.Optional[typing.Any]
    :param radius: Radius
    :type radius: typing.Optional[typing.Any]
    :param wait_for_input: Wait for Input
    :type wait_for_input: typing.Optional[typing.Union[bool, typing.Any]]
    :param mode: Mode * ``SET`` Set -- Set a new selection. * ``ADD`` Extend -- Extend existing selection. * ``SUB`` Subtract -- Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def select_column(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'KEYS'):
    ''' Select all keyframes on the specified frame(s)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def select_lasso(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        path: typing.Optional[bpy.types.bpy_prop_collection[
            'bpy.types.OperatorMousePath']] = None,
        mode: typing.Optional[typing.Any] = 'SET'):
    ''' Select keyframe points using lasso selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param mode: Mode * ``SET`` Set -- Set a new selection. * ``ADD`` Extend -- Extend existing selection. * ``SUB`` Subtract -- Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    '''

    pass


def select_leftright(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Any] = 'CHECK',
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Select keyframes to the left or the right of the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Any]
    :param extend: Extend Select
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def select_less(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Deselect keyframes on ends of selection islands

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_linked(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select keyframes occurring in the same F-Curves as selected ones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def select_more(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Select keyframes beside already selected ones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def snap(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         type: typing.Optional[typing.Any] = 'CFRA'):
    ''' Snap selected keyframes to the times specified

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CFRA`` Selection to Current Frame -- Snap selected keyframes to the current frame. * ``NEAREST_FRAME`` Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets). * ``NEAREST_SECOND`` Selection to Nearest Second -- Snap selected keyframes to the nearest second. * ``NEAREST_MARKER`` Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def stash(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          create_new: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Store this action in the NLA stack as a non-contributing strip for later use

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param create_new: Create New Action, Create a new action once the existing one has been safely stored
    :type create_new: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def stash_and_create(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Store this action in the NLA stack as a non-contributing strip for later use, and create a new action

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def unlink(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        force_delete: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Unlink this action from the active action slot (and/or exit Tweak Mode)

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param force_delete: Force Delete, Clear Fake User and remove copy stashed in this data-block's NLA stack
    :type force_delete: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def view_all(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None):
    ''' Reset viewable area to show full keyframe range

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_frame(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Move the view to the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def view_selected(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Reset viewable area to show selected keyframes range

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass
