import typing
import collections.abc
import typing_extensions
import bpy.ops.transform
import bpy.types
import bpy.typing

def bake_keys(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Add keyframes on every frame between the selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def blend_offset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
):
    """Shift selected keys to the value of the neighboring keys as a block

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Offset Factor, Control which key to offset towards and how far
    :type factor: float | None
    """

def blend_to_default(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
):
    """Blend selected keys to their default value from their current position

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, How much to blend to the default value
    :type factor: float | None
    """

def blend_to_ease(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
):
    """Blends keyframes from current state to an ease-in or ease-out curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Blend, Favor either original data or ease curve
    :type factor: float | None
    """

def blend_to_neighbor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
):
    """Blend selected keyframes to their left or right neighbor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Blend, The blend factor with 0 being the current frame
    :type factor: float | None
    """

def breakdown(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
):
    """Move selected keyframes to an inbetween position relative to adjacent keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Favor either the left or the right key
    :type factor: float | None
    """

def butterworth_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    cutoff_frequency: float | None = 3.0,
    filter_order: int | None = 4,
    samples_per_frame: int | None = 1,
    blend: float | None = 1.0,
    blend_in_out: int | None = 1,
):
    """Smooth an F-Curve while maintaining the general shape of the curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param cutoff_frequency: Frequency Cutoff (Hz), Lower values give a smoother curve
    :type cutoff_frequency: float | None
    :param filter_order: Filter Order, Higher values produce a harder frequency cutoff
    :type filter_order: int | None
    :param samples_per_frame: Samples per Frame, How many samples to calculate per frame, helps with subframe data
    :type samples_per_frame: int | None
    :param blend: Blend, How much to blend to the smoothed curve
    :type blend: float | None
    :param blend_in_out: Blend In/Out, Linearly blend the smooth data to the border frames of the selection
    :type blend_in_out: int | None
    """

def clean(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    threshold: float | None = 0.001,
    channels: bool | None = False,
):
    """Simplify F-Curves by removing closely spaced keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param threshold: Threshold
    :type threshold: float | None
    :param channels: Channels
    :type channels: bool | None
    """

def click_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: float | None = 1.0,
    value: float | None = 1.0,
    extend: bool | None = False,
):
    """Insert new keyframe at the cursor position for the active F-Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame Number, Frame to insert keyframe on
    :type frame: float | None
    :param value: Value, Value for keyframe on
    :type value: float | None
    :param extend: Extend, Extend selection instead of deselecting everything first
    :type extend: bool | None
    """

def clickselect(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    wait_to_deselect_others: bool | None = False,
    mouse_x: int | None = 0,
    mouse_y: int | None = 0,
    extend: bool | None = False,
    deselect_all: bool | None = False,
    column: bool | None = False,
    curves: bool | None = False,
):
    """Select keyframes by clicking on them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param wait_to_deselect_others: Wait to Deselect Others
    :type wait_to_deselect_others: bool | None
    :param mouse_x: Mouse X
    :type mouse_x: int | None
    :param mouse_y: Mouse Y
    :type mouse_y: int | None
    :param extend: Extend Select, Toggle keyframe selection instead of leaving newly selected keyframes only
    :type extend: bool | None
    :param deselect_all: Deselect On Nothing, Deselect all when nothing under the cursor
    :type deselect_all: bool | None
    :param column: Column Select, Select all keyframes that occur on the same frame as the one under the mouse
    :type column: bool | None
    :param curves: Only Curves, Select all the keyframes in the curve
    :type curves: bool | None
    """

def copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy selected keyframes to the internal clipboard

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def cursor_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame: float | None = 0.0,
    value: float | None = 0.0,
):
    """Interactively set the current frame and value cursor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame: Frame
    :type frame: float | None
    :param value: Value
    :type value: float | None
    """

def decimate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["RATIO", "ERROR"] | None = "RATIO",
    factor: float | None = 0.333333,
    remove_error_margin: float | None = 0.0,
):
    """Decimate F-Curves by removing keyframes that influence the curve shape the least

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param mode: Mode, Which mode to use for decimation

    RATIO
    Ratio -- Use a percentage to specify how many keyframes you want to remove.

    ERROR
    Error Margin -- Use an error margin to specify how much the curve is allowed to deviate from the original path.
        :type mode: typing.Literal['RATIO','ERROR'] | None
        :param factor: Remove, The ratio of remaining keyframes after the operation
        :type factor: float | None
        :param remove_error_margin: Max Error Margin, How much the new decimated curve is allowed to deviate from the original
        :type remove_error_margin: float | None
    """

def delete(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    confirm: bool | None = True,
):
    """Remove all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param confirm: Confirm, Prompt for confirmation
    :type confirm: bool | None
    """

def driver_delete_invalid(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Delete all visible drivers considered invalid

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_variables_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the driver variables of the active driver

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def driver_variables_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    replace: bool | None = False,
):
    """Add copied driver variables to the active driver

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param replace: Replace Existing, Replace existing driver variables, instead of just appending to the end of the existing list
    :type replace: bool | None
    """

def duplicate(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: bpy.typing.TransformModeTypeItems | None = "TRANSLATION",
):
    """Make a copy of all selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: bpy.typing.TransformModeTypeItems | None
    """

def duplicate_move(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    GRAPH_OT_duplicate: duplicate | None = None,
    TRANSFORM_OT_translate: bpy.ops.transform.translate | None = None,
):
    """Make a copy of all selected keyframes and move them

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param GRAPH_OT_duplicate: Duplicate Keyframes, Make a copy of all selected keyframes
    :type GRAPH_OT_duplicate: duplicate | None
    :param TRANSFORM_OT_translate: Move, Move selected items
    :type TRANSFORM_OT_translate: bpy.ops.transform.translate | None
    """

def ease(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
    sharpness: float | None = 2.0,
):
    """Align keyframes on a ease-in or ease-out curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Curve Bend, Defines if the keys should be aligned on an ease-in or ease-out curve
    :type factor: float | None
    :param sharpness: Sharpness, Higher values make the change more abrupt
    :type sharpness: float | None
    """

def easing_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.BeztripleInterpolationEasingItems | None = "AUTO",
):
    """Set easing type for the F-Curve segments starting from the selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.BeztripleInterpolationEasingItems | None
    """

def equalize_handles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    side: typing.Literal["LEFT", "RIGHT", "BOTH"] | None = "LEFT",
    handle_length: float | None = 5.0,
    flatten: bool | None = False,
):
    """Ensure selected keyframes' handles have equal length, optionally making them horizontal. Automatic, Automatic Clamped, or Vector handle types will be converted to Aligned

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param side: Side, Side of the keyframes' Bézier handles to affect

    LEFT
    Left -- Equalize selected keyframes' left handles.

    RIGHT
    Right -- Equalize selected keyframes' right handles.

    BOTH
    Both -- Equalize both of a keyframe's handles.
        :type side: typing.Literal['LEFT','RIGHT','BOTH'] | None
        :param handle_length: Handle Length, Length to make selected keyframes' Bézier handles
        :type handle_length: float | None
        :param flatten: Flatten, Make the values of the selected keyframes' handles the same as their respective keyframes
        :type flatten: bool | None
    """

def euler_filter(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Fix large jumps and flips in the selected Euler Rotation F-Curves arising from rotation values being clipped when baking physics

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def extrapolation_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal["CONSTANT", "LINEAR", "MAKE_CYCLIC", "CLEAR_CYCLIC"]
    | None = "CONSTANT",
):
    """Set extrapolation mode for selected F-Curves

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CONSTANT
    Constant Extrapolation -- Values on endpoint keyframes are held.

    LINEAR
    Linear Extrapolation -- Straight-line slope of end segments are extended past the endpoint keyframes.

    MAKE_CYCLIC
    Make Cyclic (F-Modifier) -- Add Cycles F-Modifier if one doesn't exist already.

    CLEAR_CYCLIC
    Clear Cyclic (F-Modifier) -- Remove Cycles F-Modifier if not needed anymore.
        :type type: typing.Literal['CONSTANT','LINEAR','MAKE_CYCLIC','CLEAR_CYCLIC'] | None
    """

def fmodifier_add(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.FmodifierTypeItems | None = "NULL",
    only_active: bool | None = False,
):
    """Add F-Modifier to the active/selected F-Curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.FmodifierTypeItems | None
    :param only_active: Only Active, Only add F-Modifier to active F-Curve
    :type only_active: bool | None
    """

def fmodifier_copy(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Copy the F-Modifier(s) of the active F-Curve

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def fmodifier_paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    only_active: bool | None = False,
    replace: bool | None = False,
):
    """Add copied F-Modifiers to the selected F-Curves

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param only_active: Only Active, Only paste F-Modifiers on active F-Curve
    :type only_active: bool | None
    :param replace: Replace Existing, Replace existing F-Modifiers, instead of just appending to the end of the existing list
    :type replace: bool | None
    """

def frame_jump(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Place the cursor on the midpoint of selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def gaussian_smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 1.0,
    sigma: float | None = 0.33,
    filter_width: int | None = 6,
):
    """Smooth the curve using a Gaussian filter

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, How much to blend to the default value
    :type factor: float | None
    :param sigma: Sigma, The shape of the gaussian distribution, lower values make it sharper
    :type sigma: float | None
    :param filter_width: Filter Width, How far to each side the operator will average the key values
    :type filter_width: int | None
    """

def ghost_curves_clear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Clear F-Curve snapshots (Ghosts) for active Graph Editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def ghost_curves_create(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Create snapshot (Ghosts) of selected F-Curves as background aid for active Graph Editor

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def handle_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.KeyframeHandleTypeItems | None = "FREE",
):
    """Set type of handle for selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.KeyframeHandleTypeItems | None
    """

def hide(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    unselected: bool | None = False,
):
    """Hide selected curves from Graph Editor view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param unselected: Unselected, Hide unselected rather than selected curves
    :type unselected: bool | None
    """

def interpolation_type(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: bpy.typing.BeztripleInterpolationModeItems | None = "CONSTANT",
):
    """Set interpolation mode for the F-Curve segments starting from the selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param type: Type
    :type type: bpy.typing.BeztripleInterpolationModeItems | None
    """

def keyframe_insert(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal["ALL", "SEL", "ACTIVE", "CURSOR_ACTIVE", "CURSOR_SEL"]
    | None = "ALL",
):
    """Insert keyframes for the specified channels

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    ALL
    All Channels -- Insert a keyframe on all visible and editable F-Curves using each curve's current value.

    SEL
    Only Selected Channels -- Insert a keyframe on selected F-Curves using each curve's current value.

    ACTIVE
    Only Active F-Curve -- Insert a keyframe on the active F-Curve using the curve's current value.

    CURSOR_ACTIVE
    Active Channels at Cursor -- Insert a keyframe for the active F-Curve at the cursor point.

    CURSOR_SEL
    Selected Channels at Cursor -- Insert a keyframe for selected F-Curves at the cursor point.
        :type type: typing.Literal['ALL','SEL','ACTIVE','CURSOR_ACTIVE','CURSOR_SEL'] | None
    """

def keyframe_jump(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    next: bool | None = True,
):
    """Jump to previous/next keyframe

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param next: Next Keyframe
    :type next: bool | None
    """

def keys_to_samples(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert selected channels to an uneditable set of samples to save storage space

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def match_slope(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
):
    """Blend selected keys to the slope of neighboring ones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Defines which keys to use as slope and how much to blend towards them
    :type factor: float | None
    """

def mirror(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal["CFRA", "VALUE", "YAXIS", "XAXIS", "MARKER"] | None = "CFRA",
):
    """Flip selected keyframes over the selected mirror line

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA
    By Times Over Current Frame -- Flip times of selected keyframes using the current frame as the mirror line.

    VALUE
    By Values Over Cursor Value -- Flip values of selected keyframes using the cursor value (Y/Horizontal component) as the mirror line.

    YAXIS
    By Times Over Zero Time -- Flip times of selected keyframes, effectively reversing the order they appear in.

    XAXIS
    By Values Over Zero Value -- Flip values of selected keyframes (i.e. negative values become positive, and vice versa).

    MARKER
    By Times Over First Selected Marker -- Flip times of selected keyframes using the first selected marker as the reference point.
        :type type: typing.Literal['CFRA','VALUE','YAXIS','XAXIS','MARKER'] | None
    """

def paste(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    offset: bpy.typing.KeyframePasteOffsetItems | None = "START",
    value_offset: bpy.typing.KeyframePasteOffsetValueItems | None = "NONE",
    merge: bpy.typing.KeyframePasteMergeItems | None = "MIX",
    flipped: bool | None = False,
):
    """Paste keyframes from the internal clipboard for the selected channels, starting on the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param offset: Frame Offset, Paste time offset of keys
    :type offset: bpy.typing.KeyframePasteOffsetItems | None
    :param value_offset: Value Offset, Paste keys with a value offset
    :type value_offset: bpy.typing.KeyframePasteOffsetValueItems | None
    :param merge: Type, Method of merging pasted keys and existing
    :type merge: bpy.typing.KeyframePasteMergeItems | None
    :param flipped: Flipped, Paste keyframes from mirrored bones if they exist
    :type flipped: bool | None
    """

def previewrange_set(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Set Preview Range based on range of selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def push_pull(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 1.0,
):
    """Exaggerate or minimize the value of the selected keys

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, Control how far to push or pull the keys
    :type factor: float | None
    """

def reveal(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    select: bool | None = True,
):
    """Make previously hidden curves visible again in Graph Editor view

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param select: Select
    :type select: bool | None
    """

def samples_to_keys(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Convert selected channels from samples to keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def scale_average(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 1.0,
):
    """Scale selected key values by their combined average

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Scale Factor, The scale factor applied to the curve segments
    :type factor: float | None
    """

def scale_from_neighbor(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
    anchor: typing.Literal["LEFT", "RIGHT"] | None = "LEFT",
):
    """Increase or decrease the value of selected keys in relationship to the neighboring one

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param factor: Factor, The factor to scale keys with
    :type factor: float | None
    :param anchor: Reference Key, Which end of the segment to use as a reference to scale from
    :type anchor: typing.Literal['LEFT','RIGHT'] | None
    """

def select_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    action: typing.Literal["TOGGLE", "SELECT", "DESELECT", "INVERT"] | None = "TOGGLE",
):
    """Toggle selection of all keyframes

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param action: Action, Selection action to execute

    TOGGLE
    Toggle -- Toggle selection for all elements.

    SELECT
    Select -- Select all elements.

    DESELECT
    Deselect -- Deselect all elements.

    INVERT
    Invert -- Invert selection of all elements.
        :type action: typing.Literal['TOGGLE','SELECT','DESELECT','INVERT'] | None
    """

def select_box(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    axis_range: bool | None = False,
    include_handles: bool | None = True,
    tweak: bool | None = False,
    use_curve_selection: bool | None = True,
    xmin: int | None = 0,
    xmax: int | None = 0,
    ymin: int | None = 0,
    ymax: int | None = 0,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
):
    """Select all keyframes within the specified region

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param axis_range: Axis Range
        :type axis_range: bool | None
        :param include_handles: Include Handles, Are handles tested individually against the selection criteria
        :type include_handles: bool | None
        :param tweak: Tweak, Operator has been activated using a click-drag event
        :type tweak: bool | None
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the calculated F-curve
        :type use_curve_selection: bool | None
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
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
    """

def select_circle(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    x: int | None = 0,
    y: int | None = 0,
    radius: int | None = 25,
    wait_for_input: bool | None = True,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    use_curve_selection: bool | None = True,
):
    """Select keyframe points using circle selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param x: X
        :type x: int | None
        :param y: Y
        :type y: int | None
        :param radius: Radius
        :type radius: int | None
        :param wait_for_input: Wait for Input
        :type wait_for_input: bool | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
        :type use_curve_selection: bool | None
    """

def select_column(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["KEYS", "CFRA", "MARKERS_COLUMN", "MARKERS_BETWEEN"]
    | None = "KEYS",
):
    """Select all keyframes on the specified frame(s)

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['KEYS','CFRA','MARKERS_COLUMN','MARKERS_BETWEEN'] | None
    """

def select_key_handles(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    left_handle_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "SELECT",
    right_handle_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "SELECT",
    key_action: typing.Literal["SELECT", "DESELECT", "KEEP"] | None = "KEEP",
):
    """For selected keyframes, select/deselect any combination of the key itself and its handles

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param left_handle_action: Left Handle, Effect on the left handle

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :type left_handle_action: typing.Literal['SELECT','DESELECT','KEEP'] | None
        :param right_handle_action: Right Handle, Effect on the right handle

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :type right_handle_action: typing.Literal['SELECT','DESELECT','KEEP'] | None
        :param key_action: Key, Effect on the key itself

    SELECT
    Select.

    DESELECT
    Deselect.

    KEEP
    Keep -- Leave as is.
        :type key_action: typing.Literal['SELECT','DESELECT','KEEP'] | None
    """

def select_lasso(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None = None,
    mode: typing.Literal["SET", "ADD", "SUB"] | None = "SET",
    use_curve_selection: bool | None = True,
):
    """Select keyframe points using lasso selection

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param path: Path
        :type path: bpy.types.bpy_prop_collection[bpy.types.OperatorMousePath] | None
        :param mode: Mode

    SET
    Set -- Set a new selection.

    ADD
    Extend -- Extend existing selection.

    SUB
    Subtract -- Subtract existing selection.
        :type mode: typing.Literal['SET','ADD','SUB'] | None
        :param use_curve_selection: Select Curves, Allow selecting all the keyframes of a curve by selecting the curve itself
        :type use_curve_selection: bool | None
    """

def select_leftright(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    mode: typing.Literal["CHECK", "LEFT", "RIGHT"] | None = "CHECK",
    extend: bool | None = False,
):
    """Select keyframes to the left or the right of the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param mode: Mode
    :type mode: typing.Literal['CHECK','LEFT','RIGHT'] | None
    :param extend: Extend Select
    :type extend: bool | None
    """

def select_less(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Deselect keyframes on ends of selection islands

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_linked(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select keyframes occurring in the same F-Curves as selected ones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def select_more(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Select keyframes beside already selected ones

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def shear(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    factor: float | None = 0.0,
    direction: typing.Literal["FROM_LEFT", "FROM_RIGHT"] | None = "FROM_LEFT",
):
    """Affect the value of the keys linearly, keeping the same relationship between them using either the left or the right key as reference

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param factor: Shear Factor, The amount of shear to apply
        :type factor: float | None
        :param direction: Direction, Which end of the segment to use as a reference to shear from

    FROM_LEFT
    From Left -- Shear the keys using the left key as reference.

    FROM_RIGHT
    From Right -- Shear the keys using the right key as reference.
        :type direction: typing.Literal['FROM_LEFT','FROM_RIGHT'] | None
    """

def smooth(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Apply weighted moving means to make selected F-Curves less bumpy

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def snap(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    type: typing.Literal[
        "CFRA",
        "VALUE",
        "NEAREST_FRAME",
        "NEAREST_SECOND",
        "NEAREST_MARKER",
        "HORIZONTAL",
    ]
    | None = "CFRA",
):
    """Snap selected keyframes to the chosen times/values

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param type: Type

    CFRA
    Selection to Current Frame -- Snap selected keyframes to the current frame.

    VALUE
    Selection to Cursor Value -- Set values of selected keyframes to the cursor value (Y/Horizontal component).

    NEAREST_FRAME
    Selection to Nearest Frame -- Snap selected keyframes to the nearest (whole) frame (use to fix accidental subframe offsets).

    NEAREST_SECOND
    Selection to Nearest Second -- Snap selected keyframes to the nearest second.

    NEAREST_MARKER
    Selection to Nearest Marker -- Snap selected keyframes to the nearest marker.

    HORIZONTAL
    Flatten Handles -- Flatten handles for a smoother transition.
        :type type: typing.Literal['CFRA','VALUE','NEAREST_FRAME','NEAREST_SECOND','NEAREST_MARKER','HORIZONTAL'] | None
    """

def snap_cursor_value(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Place the cursor value on the average value of selected keyframes

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def sound_to_samples(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    filepath: str = "",
    check_existing: bool | None = False,
    filter_blender: bool | None = False,
    filter_backup: bool | None = False,
    filter_image: bool | None = False,
    filter_movie: bool | None = True,
    filter_python: bool | None = False,
    filter_font: bool | None = False,
    filter_sound: bool | None = True,
    filter_text: bool | None = False,
    filter_archive: bool | None = False,
    filter_btx: bool | None = False,
    filter_collada: bool | None = False,
    filter_alembic: bool | None = False,
    filter_usd: bool | None = False,
    filter_obj: bool | None = False,
    filter_volume: bool | None = False,
    filter_folder: bool | None = True,
    filter_blenlib: bool | None = False,
    filemode: int | None = 9,
    show_multiview: bool | None = False,
    use_multiview: bool | None = False,
    display_type: typing.Literal[
        "DEFAULT", "LIST_VERTICAL", "LIST_HORIZONTAL", "THUMBNAIL"
    ]
    | None = "DEFAULT",
    sort_method: str | None = "",
    low: float | None = 0.0,
    high: float | None = 100000.0,
    attack: float | None = 0.005,
    release: float | None = 0.2,
    threshold: float | None = 0.0,
    use_accumulate: bool | None = False,
    use_additive: bool | None = False,
    use_square: bool | None = False,
    sthreshold: float | None = 0.1,
):
    """Bakes a sound wave to samples on selected channels

        :type override_context: bpy.types.Context | dict[str, typing.Any] | None
        :type execution_context: int | str | None
        :type undo: bool | None
        :param filepath: File Path, Path to file
        :type filepath: str
        :param check_existing: Check Existing, Check and warn on overwriting existing files
        :type check_existing: bool | None
        :param filter_blender: Filter .blend files
        :type filter_blender: bool | None
        :param filter_backup: Filter .blend files
        :type filter_backup: bool | None
        :param filter_image: Filter image files
        :type filter_image: bool | None
        :param filter_movie: Filter movie files
        :type filter_movie: bool | None
        :param filter_python: Filter Python files
        :type filter_python: bool | None
        :param filter_font: Filter font files
        :type filter_font: bool | None
        :param filter_sound: Filter sound files
        :type filter_sound: bool | None
        :param filter_text: Filter text files
        :type filter_text: bool | None
        :param filter_archive: Filter archive files
        :type filter_archive: bool | None
        :param filter_btx: Filter btx files
        :type filter_btx: bool | None
        :param filter_collada: Filter COLLADA files
        :type filter_collada: bool | None
        :param filter_alembic: Filter Alembic files
        :type filter_alembic: bool | None
        :param filter_usd: Filter USD files
        :type filter_usd: bool | None
        :param filter_obj: Filter OBJ files
        :type filter_obj: bool | None
        :param filter_volume: Filter OpenVDB volume files
        :type filter_volume: bool | None
        :param filter_folder: Filter folders
        :type filter_folder: bool | None
        :param filter_blenlib: Filter Blender IDs
        :type filter_blenlib: bool | None
        :param filemode: File Browser Mode, The setting for the file browser mode to load a .blend file, a library or a special file
        :type filemode: int | None
        :param show_multiview: Enable Multi-View
        :type show_multiview: bool | None
        :param use_multiview: Use Multi-View
        :type use_multiview: bool | None
        :param display_type: Display Type

    DEFAULT
    Default -- Automatically determine display type for files.

    LIST_VERTICAL
    Short List -- Display files as short list.

    LIST_HORIZONTAL
    Long List -- Display files as a detailed list.

    THUMBNAIL
    Thumbnails -- Display files as thumbnails.
        :type display_type: typing.Literal['DEFAULT','LIST_VERTICAL','LIST_HORIZONTAL','THUMBNAIL'] | None
        :param sort_method: File sorting mode
        :type sort_method: str | None
        :param low: Lowest Frequency, Cutoff frequency of a high-pass filter that is applied to the audio data
        :type low: float | None
        :param high: Highest Frequency, Cutoff frequency of a low-pass filter that is applied to the audio data
        :type high: float | None
        :param attack: Attack Time, Value for the envelope calculation that tells how fast the envelope can rise (the lower the value the steeper it can rise)
        :type attack: float | None
        :param release: Release Time, Value for the envelope calculation that tells how fast the envelope can fall (the lower the value the steeper it can fall)
        :type release: float | None
        :param threshold: Threshold, Minimum amplitude value needed to influence the envelope
        :type threshold: float | None
        :param use_accumulate: Accumulate, Only the positive differences of the envelope amplitudes are summarized to produce the output
        :type use_accumulate: bool | None
        :param use_additive: Additive, The amplitudes of the envelope are summarized (or, when Accumulate is enabled, both positive and negative differences are accumulated)
        :type use_additive: bool | None
        :param use_square: Square, The output is a square curve (negative values always result in -1, and positive ones in 1)
        :type use_square: bool | None
        :param sthreshold: Square Threshold, Square only: all values with an absolute amplitude lower than that result in 0
        :type sthreshold: float | None
    """

def time_offset(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    frame_offset: float | None = 0.0,
):
    """Shifts the value of selected keys in time

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param frame_offset: Frame Offset, How far in frames to offset the animation
    :type frame_offset: float | None
    """

def view_all(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    include_handles: bool | None = True,
):
    """Reset viewable area to show full keyframe range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | None
    """

def view_frame(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
):
    """Move the view to the current frame

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    """

def view_selected(
    override_context: bpy.types.Context | dict[str, typing.Any] | None = None,
    execution_context: int | str | None = None,
    undo: bool | None = None,
    *,
    include_handles: bool | None = True,
):
    """Reset viewable area to show selected keyframe range

    :type override_context: bpy.types.Context | dict[str, typing.Any] | None
    :type execution_context: int | str | None
    :type undo: bool | None
    :param include_handles: Include Handles, Include handles of keyframes when calculating extents
    :type include_handles: bool | None
    """
