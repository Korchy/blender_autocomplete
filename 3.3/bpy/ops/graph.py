import sys
import typing
import bpy.types
import bpy.ops.transform

GenericType = typing.TypeVar("GenericType")


def bake(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Bake selected F-Curves to a set of sampled points defining a similar curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def blend_to_default(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     factor: float = 0.333333):
    ''' Blend selected keys to their default value from their current position

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, How much to blend to the default value
    :type factor: float
    '''

    pass


def blend_to_neighbor(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None,
                      *,
                      factor: float = 0.333333):
    ''' Blend selected keyframes to their left or right neighbor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Blend, The blend factor with 0.5 being the current frame
    :type factor: float
    '''

    pass


def breakdown(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              factor: float = 0.333333):
    ''' Move selected keyframes to an inbetween position relative to adjacent keys

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param factor: Factor, Favor either the left or the right key
    :type factor: float
    '''

    pass


def clean(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          threshold: float = 0.001,
          channels: bool = False):
    ''' Simplify F-Curves by removing closely spaced keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param threshold: Threshold
    :type threshold: float
    :param channels: Channels
    :type channels: bool
    '''

    pass


def click_insert(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 frame: float = 1.0,
                 value: float = 1.0,
                 extend: bool = False):
    ''' Insert new keyframe at the cursor position for the active F-Curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame Number, Frame to insert keyframe on
    :type frame: float
    :param value: Value, Value for keyframe on
    :type value: float
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool
    '''

    pass


def clickselect(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                wait_to_deselect_others: bool = False,
                mouse_x: int = 0,
                mouse_y: int = 0,
                extend: bool = False,
                deselect_all: bool = False,
                column: bool = False,
                curves: bool = False):
    ''' Select keyframes by clicking on them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool
    :param mouse_x: Mouse X
    :type mouse_x: int
    :param mouse_y: Mouse Y
    :type mouse_y: int
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: bool
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: bool
    :param curves: Only Curves, Select all the keyframes in the curve
    :type curves: bool
    '''

    pass


def copy(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None):
    ''' Copy selected keyframes to the copy/paste buffer

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def cursor_set(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               frame: float = 0.0,
               value: float = 0.0):
    ''' Interactively set the current frame and value cursor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param frame: Frame
    :type frame: float
    :param value: Value
    :type value: float
    '''

    pass


def decimate(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             mode: typing.Union[str, int] = 'RATIO',
             factor: float = 0.333333,
             remove_error_margin: float = 0.0):
    ''' Decimate F-Curves by removing keyframes that influence the curve shape the least

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode, Which mode to use for decimation * RATIO Ratio -- Use a percentage to specify how many keyframes you want to remove. * ERROR Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
    :type mode: typing.Union[str, int]
    :param factor: Remove, The ratio of remaining keyframes after the operation
    :type factor: float
    :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original
    :type remove_error_margin: float
    '''

    pass


def delete(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           confirm: bool = True):
    ''' Remove all selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool
    '''

    pass


def driver_delete_invalid(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Delete all visible drivers considered invalid

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def driver_variables_copy(override_context: typing.
                          Union[typing.Dict, 'bpy.types.Context'] = None,
                          execution_context: typing.Union[str, int] = None,
                          undo: bool = None):
    ''' Copy the driver variables of the active driver

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def driver_variables_paste(override_context: typing.
                           Union[typing.Dict, 'bpy.types.Context'] = None,
                           execution_context: typing.Union[str, int] = None,
                           undo: bool = None,
                           *,
                           replace: bool = False):
    ''' Add copied driver variables to the active driver

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
    :type replace: bool
    '''

    pass


def duplicate(override_context: typing.Union[typing.
                                             Dict, 'bpy.types.Context'] = None,
              execution_context: typing.Union[str, int] = None,
              undo: bool = None,
              *,
              mode: typing.Union[int, str] = 'TRANSLATION'):
    ''' Make a copy of all selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[int, str]
    '''

    pass


def duplicate_move(
        override_context: typing.Union[typing.
                                       Dict, 'bpy.types.Context'] = None,
        execution_context: typing.Union[str, int] = None,
        undo: bool = None,
        *,
        GRAPH_OT_duplicate: 'duplicate' = None,
        TRANSFORM_OT_transform: 'bpy.ops.transform.transform' = None):
    ''' Make a copy of all selected keyframes and move them

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type GRAPH_OT_duplicate: 'duplicate'
    :param TRANSFORM_OT_transform: Transform, Transform selected items by mode type
    :type TRANSFORM_OT_transform: 'bpy.ops.transform.transform'
    '''

    pass


def easing_type(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                type: typing.Union[int, str] = 'AUTO'):
    ''' Set easing type for the F-Curve segments starting from the selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def equalize_handles(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     side: typing.Union[str, int] = 'LEFT',
                     handle_length: float = 5.0,
                     flatten: bool = False):
    ''' Ensure selected keyframes' handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param side: Side, Side of the keyframes' bezier handles to affect * LEFT Left -- Equalize selected keyframes' left handles. * RIGHT Right -- Equalize selected keyframes' right handles. * BOTH Both -- Equalize both of a keyframe's handles.
    :type side: typing.Union[str, int]
    :param handle_length: Handle Length, Length to make selected keyframes' bezier handles
    :type handle_length: float
    :param flatten: Flatten, Make the values of the selected keyframes' handles the same as their respective keyframes
    :type flatten: bool
    '''

    pass


def euler_filter(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None):
    ''' Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def extrapolation_type(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       type: typing.Union[str, int] = 'CONSTANT'):
    ''' Set extrapolation mode for selected F-Curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * CONSTANT Constant Extrapolation -- Values on endpoint keyframes are held. * LINEAR Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes. * MAKE_CYCLIC Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one doesn't exist already. * CLEAR_CYCLIC Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
    :type type: typing.Union[str, int]
    '''

    pass


def fmodifier_add(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  type: typing.Union[int, str] = 'NULL',
                  only_active: bool = True):
    ''' Add F-Modifier to the active/selected F-Curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    :param only_active: Only Active, Only add F-Modifier to active F-Curve
    :type only_active: bool
    '''

    pass


def fmodifier_copy(override_context: typing.
                   Union[typing.Dict, 'bpy.types.Context'] = None,
                   execution_context: typing.Union[str, int] = None,
                   undo: bool = None):
    ''' Copy the F-Modifier(s) of the active F-Curve

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def fmodifier_paste(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    only_active: bool = False,
                    replace: bool = False):
    ''' Add copied F-Modifiers to the selected F-Curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param only_active: Only Active, Only paste F-Modifiers on active F-Curve
    :type only_active: bool
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: bool
    '''

    pass


def frame_jump(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Place the cursor on the midpoint of selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ghost_curves_clear(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None):
    ''' Clear F-Curve snapshots (Ghosts) for active Graph Editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def ghost_curves_create(override_context: typing.
                        Union[typing.Dict, 'bpy.types.Context'] = None,
                        execution_context: typing.Union[str, int] = None,
                        undo: bool = None):
    ''' Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def handle_type(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None,
                *,
                type: typing.Union[int, str] = 'FREE'):
    ''' Set type of handle for selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def hide(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         unselected: bool = False):
    ''' Hide selected curves from Graph Editor view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param unselected: Unselected, Hide unselected rather than selected curves
    :type unselected: bool
    '''

    pass


def interpolation_type(override_context: typing.
                       Union[typing.Dict, 'bpy.types.Context'] = None,
                       execution_context: typing.Union[str, int] = None,
                       undo: bool = None,
                       *,
                       type: typing.Union[int, str] = 'CONSTANT'):
    ''' Set interpolation mode for the F-Curve segments starting from the selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type
    :type type: typing.Union[int, str]
    '''

    pass


def keyframe_insert(override_context: typing.
                    Union[typing.Dict, 'bpy.types.Context'] = None,
                    execution_context: typing.Union[str, int] = None,
                    undo: bool = None,
                    *,
                    type: typing.Union[str, int] = 'ALL'):
    ''' Insert keyframes for the specified channels

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * ALL All Channels -- Insert a keyframe on all visible and editable F-Curves using each curve's current value. * SEL Only Selected Channels -- Insert a keyframe on selected F-Curves using each curve's current value. * CURSOR_ACTIVE Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point. * CURSOR_SEL Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
    :type type: typing.Union[str, int]
    '''

    pass


def mirror(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           type: typing.Union[str, int] = 'CFRA'):
    ''' Flip selected keyframes over the selected mirror line

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * CFRA By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line. * VALUE By Values Over Cursor Value -- Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line. * YAXIS By Times Over Zero Time -- Flip times of selected keyframes, effectively reversing the order they appear in. * XAXIS By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa). * MARKER By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
    :type type: typing.Union[str, int]
    '''

    pass


def paste(override_context: typing.Union[typing.
                                         Dict, 'bpy.types.Context'] = None,
          execution_context: typing.Union[str, int] = None,
          undo: bool = None,
          *,
          offset: typing.Union[int, str] = 'START',
          merge: typing.Union[int, str] = 'MIX',
          flipped: bool = False):
    ''' Paste keyframes from copy/paste buffer for the selected channels, starting on the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param offset: Offset, Paste time offset of keys
    :type offset: typing.Union[int, str]
    :param merge: Type, Method of merging pasted keys and existing
    :type merge: typing.Union[int, str]
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    :type flipped: bool
    '''

    pass


def previewrange_set(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None):
    ''' Set Preview Range based on range of selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def reveal(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None,
           *,
           select: bool = True):
    ''' Make previously hidden curves visible again in Graph Editor view

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param select: Select
    :type select: bool
    '''

    pass


def sample(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Add keyframes on every frame between the selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_all(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               action: typing.Union[str, int] = 'TOGGLE'):
    ''' Toggle selection of all keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param action: Action, Selection action to execute * TOGGLE Toggle -- Toggle selection for all elements. * SELECT Select -- Select all elements. * DESELECT Deselect -- Deselect all elements. * INVERT Invert -- Invert selection of all elements.
    :type action: typing.Union[str, int]
    '''

    pass


def select_box(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               axis_range: bool = False,
               include_handles: bool = True,
               tweak: bool = False,
               use_curve_selection: bool = True,
               xmin: int = 0,
               xmax: int = 0,
               ymin: int = 0,
               ymax: int = 0,
               wait_for_input: bool = True,
               mode: typing.Union[str, int] = 'SET'):
    ''' Select all keyframes within the specified region

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param axis_range: Axis Range
    :type axis_range: bool
    :param include_handles: Include Handles, Are handles tested individually against the selection criteria
    :type include_handles: bool
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: bool
    :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated fcurve
    :type use_curve_selection: bool
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
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    '''

    pass


def select_circle(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  x: int = 0,
                  y: int = 0,
                  radius: int = 25,
                  wait_for_input: bool = True,
                  mode: typing.Union[str, int] = 'SET',
                  use_curve_selection: bool = True):
    ''' Select keyframe points using circle selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param x: X
    :type x: int
    :param y: Y
    :type y: int
    :param radius: Radius
    :type radius: int
    :param wait_for_input: Wait for Input
    :type wait_for_input: bool
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
    :type use_curve_selection: bool
    '''

    pass


def select_column(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  mode: typing.Union[str, int] = 'KEYS'):
    ''' Select all keyframes on the specified frame(s)

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    '''

    pass


def select_lasso(override_context: typing.
                 Union[typing.Dict, 'bpy.types.Context'] = None,
                 execution_context: typing.Union[str, int] = None,
                 undo: bool = None,
                 *,
                 path: bpy.types.
                 bpy_prop_collection['bpy.types.OperatorMousePath'] = None,
                 mode: typing.Union[str, int] = 'SET',
                 use_curve_selection: bool = True):
    ''' Select keyframe points using lasso selection

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param path: Path
    :type path: bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']
    :param mode: Mode * SET Set -- Set a new selection. * ADD Extend -- Extend existing selection. * SUB Subtract -- Subtract existing selection.
    :type mode: typing.Union[str, int]
    :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
    :type use_curve_selection: bool
    '''

    pass


def select_leftright(override_context: typing.
                     Union[typing.Dict, 'bpy.types.Context'] = None,
                     execution_context: typing.Union[str, int] = None,
                     undo: bool = None,
                     *,
                     mode: typing.Union[str, int] = 'CHECK',
                     extend: bool = False):
    ''' Select keyframes to the left or the right of the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param mode: Mode
    :type mode: typing.Union[str, int]
    :param extend: Extend Select
    :type extend: bool
    '''

    pass


def select_less(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Deselect keyframes on ends of selection islands

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_linked(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None):
    ''' Select keyframes occurring in the same F-Curves as selected ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def select_more(override_context: typing.
                Union[typing.Dict, 'bpy.types.Context'] = None,
                execution_context: typing.Union[str, int] = None,
                undo: bool = None):
    ''' Select keyframes beside already selected ones

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def smooth(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Apply weighted moving means to make selected F-Curves less bumpy

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def snap(override_context: typing.Union[typing.
                                        Dict, 'bpy.types.Context'] = None,
         execution_context: typing.Union[str, int] = None,
         undo: bool = None,
         *,
         type: typing.Union[str, int] = 'CFRA'):
    ''' Snap selected keyframes to the chosen times/values

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param type: Type * CFRA Selection to Current Frame -- Snap selected keyframes to the current frame. * VALUE Selection to Cursor Value -- Set values of selected keyframes to the cursor value (Y/Horizontal component). * NEAREST_FRAME Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets). * NEAREST_SECOND Selection to Nearest Second -- Snap selected keyframes to the nearest second. * NEAREST_MARKER Selection to Nearest Marker -- Snap selected keyframes to the nearest marker. * HORIZONTAL Flatten Handles -- Flatten handles for a smoother transition.
    :type type: typing.Union[str, int]
    '''

    pass


def snap_cursor_value(override_context: typing.
                      Union[typing.Dict, 'bpy.types.Context'] = None,
                      execution_context: typing.Union[str, int] = None,
                      undo: bool = None):
    ''' Place the cursor value on the average value of selected keyframes

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def sound_bake(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None,
               *,
               filepath: str = "",
               filter_blender: bool = False,
               filter_backup: bool = False,
               filter_image: bool = False,
               filter_movie: bool = True,
               filter_python: bool = False,
               filter_font: bool = False,
               filter_sound: bool = True,
               filter_text: bool = False,
               filter_archive: bool = False,
               filter_btx: bool = False,
               filter_collada: bool = False,
               filter_alembic: bool = False,
               filter_usd: bool = False,
               filter_obj: bool = False,
               filter_volume: bool = False,
               filter_folder: bool = True,
               filter_blenlib: bool = False,
               filemode: int = 9,
               show_multiview: bool = False,
               use_multiview: bool = False,
               display_type: typing.Union[str, int] = 'DEFAULT',
               sort_method: typing.Union[str, int] = '',
               low: float = 0.0,
               high: float = 100000.0,
               attack: float = 0.005,
               release: float = 0.2,
               threshold: float = 0.0,
               use_accumulate: bool = False,
               use_additive: bool = False,
               use_square: bool = False,
               sthreshold: float = 0.1):
    ''' Bakes a sound wave to selected F-Curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param filepath: File Path, Path to file
    :type filepath: str
    :param filter_blender: Filter .blend files
    :type filter_blender: bool
    :param filter_backup: Filter .blend files
    :type filter_backup: bool
    :param filter_image: Filter image files
    :type filter_image: bool
    :param filter_movie: Filter movie files
    :type filter_movie: bool
    :param filter_python: Filter python files
    :type filter_python: bool
    :param filter_font: Filter font files
    :type filter_font: bool
    :param filter_sound: Filter sound files
    :type filter_sound: bool
    :param filter_text: Filter text files
    :type filter_text: bool
    :param filter_archive: Filter archive files
    :type filter_archive: bool
    :param filter_btx: Filter btx files
    :type filter_btx: bool
    :param filter_collada: Filter COLLADA files
    :type filter_collada: bool
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: bool
    :param filter_usd: Filter USD files
    :type filter_usd: bool
    :param filter_obj: Filter OBJ files
    :type filter_obj: bool
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: bool
    :param filter_folder: Filter folders
    :type filter_folder: bool
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: bool
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: int
    :param show_multiview: Enable Multi-View
    :type show_multiview: bool
    :param use_multiview: Use Multi-View
    :type use_multiview: bool
    :param display_type: Display Type * DEFAULT Default -- Automatically determine display type for files. * LIST_VERTICAL Short List -- Display files as short list. * LIST_HORIZONTAL Long List -- Display files as a detailed list. * THUMBNAIL Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Union[str, int]
    :param sort_method: File sorting mode
    :type sort_method: typing.Union[str, int]
    :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
    :type low: float
    :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
    :type high: float
    :param attack: Attack Time, Value for the hull curve calculation that tells how fast the hull curve can rise (the lower the value the steeper it can rise)
    :type attack: float
    :param release: Release Time, Value for the hull curve calculation that tells how fast the hull curve can fall (the lower the value the steeper it can fall)
    :type release: float
    :param threshold: Threshold, Minimum amplitude value needed to influence the hull curve
    :type threshold: float
    :param use_accumulate: Accumulate, Only the positive differences of the hull curve amplitudes are summarized to produce the output
    :type use_accumulate: bool
    :param use_additive: Additive, The amplitudes of the hull curve are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
    :type use_additive: bool
    :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
    :type use_square: bool
    :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0
    :type sthreshold: float
    '''

    pass


def unbake(override_context: typing.Union[typing.
                                          Dict, 'bpy.types.Context'] = None,
           execution_context: typing.Union[str, int] = None,
           undo: bool = None):
    ''' Un-Bake selected F-Points to F-Curves

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_all(override_context: typing.Union[typing.
                                            Dict, 'bpy.types.Context'] = None,
             execution_context: typing.Union[str, int] = None,
             undo: bool = None,
             *,
             include_handles: bool = True):
    ''' Reset viewable area to show full keyframe range

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool
    '''

    pass


def view_frame(override_context: typing.
               Union[typing.Dict, 'bpy.types.Context'] = None,
               execution_context: typing.Union[str, int] = None,
               undo: bool = None):
    ''' Move the view to the current frame

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    '''

    pass


def view_selected(override_context: typing.
                  Union[typing.Dict, 'bpy.types.Context'] = None,
                  execution_context: typing.Union[str, int] = None,
                  undo: bool = None,
                  *,
                  include_handles: bool = True):
    ''' Reset viewable area to show selected keyframe range

    :type override_context: typing.Union[typing.Dict, 'bpy.types.Context']
    :type execution_context: typing.Union[str, int]
    :type undo: bool
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool
    '''

    pass
