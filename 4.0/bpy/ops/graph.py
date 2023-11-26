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


def blend_offset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Shift selected keys to the value of the neighboring keys as a block

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Offset Factor, Control which key to offset towards and how far
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def blend_to_default(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Blend selected keys to their default value from their current position

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, How much to blend to the default value
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def blend_to_ease(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Blends keyframes from current state to an ease-in or ease-out curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Blend, Favor either original data or ease curve
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def blend_to_neighbor(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Blend selected keyframes to their left or right neighbor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Blend, The blend factor with 0 being the current frame
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def breakdown(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Move selected keyframes to an inbetween position relative to adjacent keys

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Favor either the left or the right key
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def butterworth_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        cutoff_frequency: typing.Optional[typing.Any] = 3.0,
        filter_order: typing.Optional[typing.Any] = 4,
        samples_per_frame: typing.Optional[typing.Any] = 1,
        blend: typing.Optional[typing.Any] = 1.0,
        blend_in_out: typing.Optional[typing.Any] = 1):
    ''' Smooth an F-Curve while maintaining the general shape of the curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve
    :type cutoff_frequency: typing.Optional[typing.Any]
    :param filter_order: Filter Order, Higher values produce a harder frequency cutoff
    :type filter_order: typing.Optional[typing.Any]
    :param samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data
    :type samples_per_frame: typing.Optional[typing.Any]
    :param blend: Blend, How much to blend to the smoothed curve
    :type blend: typing.Optional[typing.Any]
    :param blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection
    :type blend_in_out: typing.Optional[typing.Any]
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


def click_insert(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame: typing.Optional[typing.Any] = 1.0,
        value: typing.Optional[typing.Any] = 1.0,
        extend: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Insert new keyframe at the cursor position for the active F-Curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame: Frame Number, Frame to insert keyframe on
    :type frame: typing.Optional[typing.Any]
    :param value: Value, Value for keyframe on
    :type value: typing.Optional[typing.Any]
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: typing.Optional[typing.Union[bool, typing.Any]]
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
        curves: typing.Optional[typing.Union[bool, typing.Any]] = False):
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
    :param curves: Only Curves, Select all the keyframes in the curve
    :type curves: typing.Optional[typing.Union[bool, typing.Any]]
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


def cursor_set(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame: typing.Optional[typing.Any] = 0.0,
        value: typing.Optional[typing.Any] = 0.0):
    ''' Interactively set the current frame and value cursor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame: Frame
    :type frame: typing.Optional[typing.Any]
    :param value: Value
    :type value: typing.Optional[typing.Any]
    '''

    pass


def decimate(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             mode: typing.Optional[typing.Any] = 'RATIO',
             factor: typing.Optional[typing.Any] = 0.333333,
             remove_error_margin: typing.Optional[typing.Any] = 0.0):
    ''' Decimate F-Curves by removing keyframes that influence the curve shape the least

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode, Which mode to use for decimation * ``RATIO`` Ratio -- Use a percentage to specify how many keyframes you want to remove. * ``ERROR`` Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
    :type mode: typing.Optional[typing.Any]
    :param factor: Remove, The ratio of remaining keyframes after the operation
    :type factor: typing.Optional[typing.Any]
    :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original
    :type remove_error_margin: typing.Optional[typing.Any]
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


def driver_delete_invalid(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Delete all visible drivers considered invalid

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def driver_variables_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy the driver variables of the active driver

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def driver_variables_paste(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        replace: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Add copied driver variables to the active driver

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
    :type replace: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def duplicate(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        mode: typing.Optional[typing.Union[str, int]] = 'TRANSLATION'):
    ''' Make a copy of all selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param mode: Mode
    :type mode: typing.Optional[typing.Union[str, int]]
    '''

    pass


def duplicate_move(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        GRAPH_OT_duplicate: typing.Optional['duplicate'] = None,
        TRANSFORM_OT_translate: typing.
        Optional['bpy.ops.transform.translate'] = None):
    ''' Make a copy of all selected keyframes and move them

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type GRAPH_OT_duplicate: typing.Optional['duplicate']
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: typing.Optional['bpy.ops.transform.translate']
    '''

    pass


def ease(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         factor: typing.Optional[typing.Any] = 0.0):
    ''' Align keyframes on a ease-in or ease-out curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Curve Bend, Control the bend of the curve
    :type factor: typing.Optional[typing.Any]
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


def equalize_handles(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        side: typing.Optional[typing.Any] = 'LEFT',
        handle_length: typing.Optional[typing.Any] = 5.0,
        flatten: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Ensure selected keyframes' handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param side: Side, Side of the keyframes' bezier handles to affect * ``LEFT`` Left -- Equalize selected keyframes' left handles. * ``RIGHT`` Right -- Equalize selected keyframes' right handles. * ``BOTH`` Both -- Equalize both of a keyframe's handles.
    :type side: typing.Optional[typing.Any]
    :param handle_length: Handle Length, Length to make selected keyframes' bezier handles
    :type handle_length: typing.Optional[typing.Any]
    :param flatten: Flatten, Make the values of the selected keyframes' handles the same as their respective keyframes
    :type flatten: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def euler_filter(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
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


def fmodifier_add(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        type: typing.Optional[typing.Union[str, int]] = 'nullptr',
        only_active: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Add F-Modifier to the active/selected F-Curves

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type
    :type type: typing.Optional[typing.Union[str, int]]
    :param only_active: Only Active, Only add F-Modifier to active F-Curve
    :type only_active: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def fmodifier_copy(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Copy the F-Modifier(s) of the active F-Curve

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def fmodifier_paste(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        only_active: typing.Optional[typing.Union[bool, typing.Any]] = False,
        replace: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Add copied F-Modifiers to the selected F-Curves

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param only_active: Only Active, Only paste F-Modifiers on active F-Curve
    :type only_active: typing.Optional[typing.Union[bool, typing.Any]]
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def frame_jump(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Place the cursor on the midpoint of selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def gaussian_smooth(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 1.0,
        sigma: typing.Optional[typing.Any] = 0.33,
        filter_width: typing.Optional[typing.Any] = 6):
    ''' Smooth the curve using a Gaussian filter

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, How much to blend to the default value
    :type factor: typing.Optional[typing.Any]
    :param sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper
    :type sigma: typing.Optional[typing.Any]
    :param filter_width: Filter Width, How far to each side the operator will average the key values
    :type filter_width: typing.Optional[typing.Any]
    '''

    pass


def ghost_curves_clear(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Clear F-Curve snapshots (Ghosts) for active Graph Editor

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def ghost_curves_create(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

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


def hide(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
         execution_context: typing.Optional[typing.Union[str, int]] = None,
         undo: typing.Optional[bool] = None,
         *,
         unselected: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Hide selected curves from Graph Editor view

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param unselected: Unselected, Hide unselected rather than selected curves
    :type unselected: typing.Optional[typing.Union[bool, typing.Any]]
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
    :param type: Type * ``ALL`` All Channels -- Insert a keyframe on all visible and editable F-Curves using each curve's current value. * ``SEL`` Only Selected Channels -- Insert a keyframe on selected F-Curves using each curve's current value. * ``ACTIVE`` Only Active F-Curve -- Insert a keyframe on the active F-Curve using the curve's current value. * ``CURSOR_ACTIVE`` Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point. * ``CURSOR_SEL`` Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def keyframe_jump(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        next: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Jump to previous/next keyframe

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param next: Next Keyframe
    :type next: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def keys_to_samples(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        confirm: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Convert selected channels to an uneditable set of samples to save storage space

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def match_slope(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 0.0):
    ''' Blend selected keys to the slope of neighboring ones

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Defines which keys to use as slope and how much to blend towards them
    :type factor: typing.Optional[typing.Any]
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
    :param type: Type * ``CFRA`` By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line. * ``VALUE`` By Values Over Cursor Value -- Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line. * ``YAXIS`` By Times Over Zero Time -- Flip times of selected keyframes, effectively reversing the order they appear in. * ``XAXIS`` By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa). * ``MARKER`` By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def paste(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          offset: typing.Optional[typing.Union[str, int]] = 'START',
          value_offset: typing.Optional[typing.Union[str, int]] = 'NONE',
          merge: typing.Optional[typing.Union[str, int]] = 'MIX',
          flipped: typing.Optional[typing.Union[bool, typing.Any]] = False):
    ''' Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param offset: Frame Offset, Paste time offset of keys
    :type offset: typing.Optional[typing.Union[str, int]]
    :param value_offset: Value Offset, Paste keys with a value offset
    :type value_offset: typing.Optional[typing.Union[str, int]]
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
    ''' Set Preview Range based on range of selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def push_pull(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 1.0):
    ''' Exaggerate or minimize the value of the selected keys

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Factor, Control how far to push or pull the keys
    :type factor: typing.Optional[typing.Any]
    '''

    pass


def reveal(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None,
           *,
           select: typing.Optional[typing.Union[bool, typing.Any]] = True):
    ''' Make previously hidden curves visible again in Graph Editor view

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param select: Select
    :type select: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass


def samples_to_keys(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Convert selected channels from samples to keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def scale_average(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        factor: typing.Optional[typing.Any] = 1.0):
    ''' Scale selected key values by their combined average

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Scale Factor, The scale factor applied to the curve segments
    :type factor: typing.Optional[typing.Any]
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
        include_handles: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True,
        tweak: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_curve_selection: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True,
        xmin: typing.Optional[typing.Any] = 0,
        xmax: typing.Optional[typing.Any] = 0,
        ymin: typing.Optional[typing.Any] = 0,
        ymax: typing.Optional[typing.Any] = 0,
        wait_for_input: typing.Optional[typing.Union[bool, typing.Any]] = True,
        mode: typing.Optional[typing.Any] = 'SET'):
    ''' Select all keyframes within the specified region

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param axis_range: Axis Range
    :type axis_range: typing.Optional[typing.Union[bool, typing.Any]]
    :param include_handles: Include Handles, Are handles tested individually against the selection criteria
    :type include_handles: typing.Optional[typing.Union[bool, typing.Any]]
    :param tweak: Tweak, Operator has been activated using a click-drag event
    :type tweak: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve
    :type use_curve_selection: typing.Optional[typing.Union[bool, typing.Any]]
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
        mode: typing.Optional[typing.Any] = 'SET',
        use_curve_selection: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True):
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
    :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
    :type use_curve_selection: typing.Optional[typing.Union[bool, typing.Any]]
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


def select_key_handles(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        left_handle_action: typing.Optional[typing.Any] = 'SELECT',
        right_handle_action: typing.Optional[typing.Any] = 'SELECT',
        key_action: typing.Optional[typing.Any] = 'KEEP'):
    ''' For selected keyframes, select/deselect any combination of the key itself and its handles

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param left_handle_action: Left Handle, Effect on the left handle * ``SELECT`` Select. * ``DESELECT`` Deselect. * ``KEEP`` Keep -- Leave as is.
    :type left_handle_action: typing.Optional[typing.Any]
    :param right_handle_action: Right Handle, Effect on the right handle * ``SELECT`` Select. * ``DESELECT`` Deselect. * ``KEEP`` Keep -- Leave as is.
    :type right_handle_action: typing.Optional[typing.Any]
    :param key_action: Key, Effect on the key itself * ``SELECT`` Select. * ``DESELECT`` Deselect. * ``KEEP`` Keep -- Leave as is.
    :type key_action: typing.Optional[typing.Any]
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
        mode: typing.Optional[typing.Any] = 'SET',
        use_curve_selection: typing.Optional[typing.Union[bool, typing.
                                                          Any]] = True):
    ''' Select keyframe points using lasso selection

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param path: Path
    :type path: typing.Optional[bpy.types.bpy_prop_collection['bpy.types.OperatorMousePath']]
    :param mode: Mode * ``SET`` Set -- Set a new selection. * ``ADD`` Extend -- Extend existing selection. * ``SUB`` Subtract -- Subtract existing selection.
    :type mode: typing.Optional[typing.Any]
    :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
    :type use_curve_selection: typing.Optional[typing.Union[bool, typing.Any]]
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


def shear(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
          execution_context: typing.Optional[typing.Union[str, int]] = None,
          undo: typing.Optional[bool] = None,
          *,
          factor: typing.Optional[typing.Any] = 0.0,
          direction: typing.Optional[typing.Any] = 'FROM_LEFT'):
    ''' Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param factor: Shear Factor, The amount of shear to apply
    :type factor: typing.Optional[typing.Any]
    :param direction: Direction, Which end of the segment to use as a reference to shear from * ``FROM_LEFT`` From Left -- Shear the keys using the left key as reference. * ``FROM_RIGHT`` From Right -- Shear the keys using the right key as reference.
    :type direction: typing.Optional[typing.Any]
    '''

    pass


def smooth(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
           execution_context: typing.Optional[typing.Union[str, int]] = None,
           undo: typing.Optional[bool] = None):
    ''' Apply weighted moving means to make selected F-Curves less bumpy

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
    ''' Snap selected keyframes to the chosen times/values

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param type: Type * ``CFRA`` Selection to Current Frame -- Snap selected keyframes to the current frame. * ``VALUE`` Selection to Cursor Value -- Set values of selected keyframes to the cursor value (Y/Horizontal component). * ``NEAREST_FRAME`` Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets). * ``NEAREST_SECOND`` Selection to Nearest Second -- Snap selected keyframes to the nearest second. * ``NEAREST_MARKER`` Selection to Nearest Marker -- Snap selected keyframes to the nearest marker. * ``HORIZONTAL`` Flatten Handles -- Flatten handles for a smoother transition.
    :type type: typing.Optional[typing.Any]
    '''

    pass


def snap_cursor_value(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None):
    ''' Place the cursor value on the average value of selected keyframes

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    '''

    pass


def sound_to_samples(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        filepath: typing.Union[str, typing.Any] = "",
        check_existing: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_blender: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_backup: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_image: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_movie: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_python: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_font: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_sound: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_text: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_archive: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_btx: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_collada: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_alembic: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filter_usd: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_obj: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_volume: typing.Optional[typing.Union[bool, typing.Any]] = False,
        filter_folder: typing.Optional[typing.Union[bool, typing.Any]] = True,
        filter_blenlib: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        filemode: typing.Optional[typing.Any] = 9,
        show_multiview: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_multiview: typing.Optional[typing.Union[bool, typing.Any]] = False,
        display_type: typing.Optional[typing.Any] = 'DEFAULT',
        sort_method: typing.Optional[typing.Union[str, int, typing.Any]] = '',
        low: typing.Optional[typing.Any] = 0.0,
        high: typing.Optional[typing.Any] = 100000.0,
        attack: typing.Optional[typing.Any] = 0.005,
        release: typing.Optional[typing.Any] = 0.2,
        threshold: typing.Optional[typing.Any] = 0.0,
        use_accumulate: typing.Optional[typing.Union[bool, typing.
                                                     Any]] = False,
        use_additive: typing.Optional[typing.Union[bool, typing.Any]] = False,
        use_square: typing.Optional[typing.Union[bool, typing.Any]] = False,
        sthreshold: typing.Optional[typing.Any] = 0.1):
    ''' Bakes a sound wave to samples on selected channels

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param filepath: File Path, Path to file
    :type filepath: typing.Union[str, typing.Any]
    :param check_existing: Check Existing, Check and warn on overwriting existing files
    :type check_existing: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blender: Filter .blend files
    :type filter_blender: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_backup: Filter .blend files
    :type filter_backup: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_image: Filter image files
    :type filter_image: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_movie: Filter movie files
    :type filter_movie: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_python: Filter Python files
    :type filter_python: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_font: Filter font files
    :type filter_font: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_sound: Filter sound files
    :type filter_sound: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_text: Filter text files
    :type filter_text: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_archive: Filter archive files
    :type filter_archive: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_btx: Filter btx files
    :type filter_btx: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_collada: Filter COLLADA files
    :type filter_collada: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_alembic: Filter Alembic files
    :type filter_alembic: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_usd: Filter USD files
    :type filter_usd: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_obj: Filter OBJ files
    :type filter_obj: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_volume: Filter OpenVDB volume files
    :type filter_volume: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_folder: Filter folders
    :type filter_folder: typing.Optional[typing.Union[bool, typing.Any]]
    :param filter_blenlib: Filter Blender IDs
    :type filter_blenlib: typing.Optional[typing.Union[bool, typing.Any]]
    :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
    :type filemode: typing.Optional[typing.Any]
    :param show_multiview: Enable Multi-View
    :type show_multiview: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_multiview: Use Multi-View
    :type use_multiview: typing.Optional[typing.Union[bool, typing.Any]]
    :param display_type: Display Type * ``DEFAULT`` Default -- Automatically determine display type for files. * ``LIST_VERTICAL`` Short List -- Display files as short list. * ``LIST_HORIZONTAL`` Long List -- Display files as a detailed list. * ``THUMBNAIL`` Thumbnails -- Display files as thumbnails.
    :type display_type: typing.Optional[typing.Any]
    :param sort_method: File sorting mode
    :type sort_method: typing.Optional[typing.Union[str, int, typing.Any]]
    :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
    :type low: typing.Optional[typing.Any]
    :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
    :type high: typing.Optional[typing.Any]
    :param attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise)
    :type attack: typing.Optional[typing.Any]
    :param release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall)
    :type release: typing.Optional[typing.Any]
    :param threshold: Threshold, Minimum amplitude value needed to influence the envelope
    :type threshold: typing.Optional[typing.Any]
    :param use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output
    :type use_accumulate: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
    :type use_additive: typing.Optional[typing.Union[bool, typing.Any]]
    :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
    :type use_square: typing.Optional[typing.Union[bool, typing.Any]]
    :param sthreshold: all values with an absolute amplitude lower than that result in 0
    :type sthreshold: typing.Optional[typing.Any]
    '''

    pass


def time_offset(
        override_context: typing.Optional[
            typing.Union[typing.Dict, 'bpy.types.Context']] = None,
        execution_context: typing.Optional[typing.Union[str, int]] = None,
        undo: typing.Optional[bool] = None,
        *,
        frame_offset: typing.Optional[typing.Any] = 0.0):
    ''' Shifts the value of selected keys in time

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param frame_offset: Frame Offset, How far in frames to offset the animation
    :type frame_offset: typing.Optional[typing.Any]
    '''

    pass


def view_all(override_context: typing.Optional[
        typing.Union[typing.Dict, 'bpy.types.Context']] = None,
             execution_context: typing.Optional[typing.Union[str, int]] = None,
             undo: typing.Optional[bool] = None,
             *,
             include_handles: typing.Optional[typing.Union[bool, typing.
                                                           Any]] = True):
    ''' Reset viewable area to show full keyframe range

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: typing.Optional[typing.Union[bool, typing.Any]]
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
        undo: typing.Optional[bool] = None,
        *,
        include_handles: typing.Optional[typing.Union[bool, typing.
                                                      Any]] = True):
    ''' Reset viewable area to show selected keyframe range

    :type override_context: typing.Optional[typing.Union[typing.Dict, 'bpy.types.Context']]
    :type execution_context: typing.Optional[typing.Union[str, int]]
    :type undo: typing.Optional[bool]
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: typing.Optional[typing.Union[bool, typing.Any]]
    '''

    pass
